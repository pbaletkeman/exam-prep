# QUICK REFERENCE — Iteration 5
# Databricks Certified Associate Developer for Apache Spark

> Sprint-revision card. One glance = ready to sit the exam.

---

## CRITICAL DEFAULTS — Memorise These Numbers

| Config | Default | Trap Value |
|--------|---------|-----------|
| `spark.sql.shuffle.partitions` | **200** | 100, 500 |
| `spark.driver.memory` | **1g** | 512m, 2g |
| `spark.sql.autoBroadcastJoinThreshold` | **10 MB** | 50 MB, 200 MB |
| `spark.sql.adaptive.enabled` | **true** (since 3.2) | false |
| `spark.memory.storageFraction` | **0.5** | 0.6 |
| `spark.memory.fraction` | **0.6** | 0.5 |
| `spark.sql.broadcastTimeout` | **300 s** | 60 s |
| `spark.shuffle.file.buffer` | **32 KB** | 64 KB |
| `spark.sql.optimizer.maxIterations` | **100** | 50 |
| `spark.locality.wait` | **3 s** | 5 s |
| `spark.rpc.message.maxSize` | **128 MB** | 64 MB |
| `ps.options.compute.default_index_type` | **`"distributed-sequence"`** | `"sequence"` |

---

## TOPIC 1 — ARCHITECTURE: 5 KEY ANCHORS

```
A1  shuffle.partitions → SQL/DF only (RDD = default.parallelism)
A2  Cached stages show as SKIPPED in Spark UI
A3  MEMORY_ONLY eviction → DROPPED (not to disk), LRU, recomputed from lineage
A4  AQE = true by DEFAULT since Spark 3.2
A5  Locality: PROCESS_LOCAL → NODE_LOCAL → RACK_LOCAL → ANY
```

### Storage Level Cheatsheet

| Level | In Memory? | On Disk? | Serialized? |
|-------|-----------|---------|-------------|
| `MEMORY_ONLY` | ✅ | ❌ | No (JVM objects) |
| `MEMORY_ONLY_SER` | ✅ | ❌ | **Yes** |
| `MEMORY_AND_DISK` | ✅ | ✅ (spill) | No (JVM objects) |
| `MEMORY_AND_DISK_SER` | ✅ | ✅ (spill) | **Yes** |
| `DISK_ONLY` | ❌ | ✅ | Yes |

**SER = serialised binary** → less memory, more CPU
**No SER = JVM objects** → more memory, less CPU per access

### History Server — Exact 3 Configs Required

```
spark.eventLog.enabled = true
spark.eventLog.dir = <shared storage path>
spark.history.fs.logDirectory = <same path>
```
`spark.ui.enabled` → live app UI only, NOT for History Server

### Memory Model

```
JVM Heap
└── Spark Unified Pool (spark.memory.fraction = 0.6)
    ├── Storage Fraction (storageFraction = 0.5)  ← cached data
    └── Execution Fraction (1 - storageFraction)  ← shuffle/sort
        [Execution can EVICT storage when needed]
Off-heap (NOT in JVM, NOT GC'd, NOT counted in memory.fraction)
```

### Block Manager Scope

Manages: cached RDD/DF partitions, broadcast variable data, shuffle write files
**ALL block types** — not just caching

### Kubernetes Image Config

```
spark.kubernetes.container.image    ✅ CORRECT
spark.kubernetes.executor.image     ❌ WRONG
```

### Stage Count Formula

```
Parquet read → repartition(100) → groupBy.agg → show
  Stage 1        Stage 2 (shuffle)   Stage 3 (shuffle)
= 3 stages
```

### RPC vs Broadcast vs collect()

```
spark.rpc.message.maxSize     → controls RPC messages (NOT broadcast)
spark.driver.maxResultSize    → controls collect() result size
Broadcast variables           → Torrent-style HTTP, NOT subject to RPC limit
```

### executor.instances + DRA

```
DRA (spark.dynamicAllocation.enabled=true) + spark.executor.instances
→ WARNING logged, executor.instances IGNORED
→ DRA uses minExecutors / maxExecutors
```

### Sort-merge Join: What's Expensive?

```
Shuffle WRITE → Shuffle READ → Sort/Merge
              ↑
         Most expensive (pulls data from ALL mappers across network)
```

---

## TOPIC 2 — SQL: 5 KEY ANCHORS

```
S1  datediff(end, start) = end − start in days (signed integer)
S2  unix_timestamp() no args → LongType (NOT TimestampType)
S3  trunc(date, fmt) → DateType; date_trunc(fmt, ts) → TimestampType (diff arg order!)
S4  locate is 1-based: locate("world","hello world",1) = 7
S5  sort_array(col, False) = descending; sort_array nulls first; array_sort nulls last
```

### Date/Time Functions

| Call | Returns | Notes |
|------|---------|-------|
| `datediff('2024-01-10','2024-01-01')` | 9 | end − start |
| `unix_timestamp()` | LongType | epoch seconds |
| `trunc(date, 'month')` | DateType | col first, then fmt |
| `date_trunc('hour', ts)` | TimestampType | fmt first, then col |
| `last_day('2026-04-10')` | `'2026-04-30'` | last day of month |
| `dayofweek(date)` | **1=Sunday** | 1=Sun, 2=Mon, ..., 7=Sat |
| `initcap("hello world")` | `"Hello World"` | first letter of each word |

### Null / String Functions

```
nullif(e1, e2)         → NULL if e1=e2, else e1
locate("x", "axb", 1) → 2 (1-based start position)
soundex("Smith")       → "S530" (same as "Smyth") → StringType
format_string("%s %d", col1, col2) → StringType (printf-style)
```

### Array & Map Functions

```
array_repeat('x', 3)  → ['x','x','x']
sort_array(col, False) → descending (nulls first)
array_sort(col)        → ascending (nulls LAST)
F.reverse(str_col)    → reversed string characters
F.reverse(arr_col)    → reversed array elements
map_entries(m)        → ArrayType(StructType(key, value))
```

### Aggregates

```
percentile(col, 0.5)        → exact (full sort)
percentile_approx(col, 0.5) → approximate (Greenwald-Khanna sketch)
count_if(condition)         → rows where condition = TRUE
max_by(val_col, order_col)  → val_col from row with max order_col
nth_value(col, n)           → n-th row in window frame; NULL if <n rows
```

### GROUPING_ID Quick Reference

```
ROLLUP(A, B) produces bitmask:
  0  = A, B both in key      (finest grain)
  1  = only A in key         (B rolled up)
  2  = only B in key         (A rolled up)
  3  = neither in key        (grand total)
Column ORDER in args → determines bit positions
```

### CTE Rules

```
✅  WITH clause defines named subquery
✅  Multiple CTEs: WITH a AS (...), b AS (...) SELECT ...
✅  NOT always materialised to disk (Catalyst inlines)
❌  RECURSIVE CTEs NOT supported in Spark SQL ≤ 3.5
```

### stack() Function

```sql
SELECT stack(2, 'a', 1, 'b', 2) AS (col1, col2)
-- Result: ('a', 1) then ('b', 2)    ← 2 rows
```

### conv() and unhex()

```
F.conv("FF", 16, 10) → "255"    (StringType ALWAYS)
F.unhex(col)         → BinaryType (inverse of F.hex)
```

### SQL WINDOW Clause Position

```sql
SELECT name, salary, rank() OVER w AS rnk
FROM employees
WINDOW w AS (PARTITION BY dept ORDER BY salary DESC)
--                                                   ↑ at end of SELECT
```

---

## TOPIC 3 — DATAFRAME API: 5 KEY ANCHORS

```
D1  inferSchema=true → TWO passes over data (doubles I/O)
D2  insertInto → by column POSITION (not name), table must exist
D3  Delta overwrite new col → AnalysisException; fix: overwriteSchema=true
D4  assert_true is a Catalyst expression, NOT a UDF (much faster)
D5  toLocalIterator = one partition at a time (low driver memory)
```

### New Spark 3.x Methods

| Method | Since | Does |
|--------|-------|------|
| `df.withColumnsRenamed(dict)` | 3.4 | Rename multiple cols atomically |
| `df.unpivot(ids, vals, varCol, valCol)` | 3.4 | Wide → long format |
| `df.offset(n)` | 3.4 | Skip first n rows |
| `trigger(availableNow=True)` | 3.3 | Multi-batch drain, then stop |
| `session_window(col, gap)` | 3.2 | Gap-based streaming windows |

### df.transform vs F.transform

```python
df.transform(func)            # func(df) → DataFrame pipeline chaining
F.transform(array_col, func)  # element-wise on array elements
```

### foreach vs foreachPartition

```
df.foreach(f)          → f called ONCE per Row; receives Row
df.foreachPartition(f) → f called ONCE per partition; receives iterator of Rows
→ foreachPartition more efficient for external connections (amortised setup cost)
→ both return None (not DataFrame!)
```

### mapInPandas

```python
df.mapInPandas(func, schema)
# func: Iterator[pd.DataFrame] → Iterator[pd.DataFrame]
# Applied partition-by-partition (no groupBy required)
# Full partition as pandas DF (via Arrow)
```

### saveAsTable vs insertInto

| | `saveAsTable` | `insertInto` |
|-|--------------|-------------|
| Schema | Uses DataFrame schema | Ignores column names |
| Column matching | By name | **By position** |
| Table exists? | Not required | **Must exist** |

### CSV Options

```
sep / delimiter → both valid aliases for field separator
nullValue       → written for NULL column values (default "")
emptyValue      → written for empty string values (default "")
inferSchema=true → 2 full passes, doubles I/O
```

### Hash Functions

```
F.hash(*cols)     → MurmurHash3, IntegerType (32-bit), non-cryptographic
F.xxhash64(*cols) → xxHash64,    LongType (64-bit),    non-cryptographic
```

### schema Methods

```
df.schema.simpleString() → "struct<id:int,name:string>"
df.schema.toDDL()        → "`id` INT,`name` STRING"     (DDL-ready)
```

### Null Helpers

```
df.na.drop(thresh=2) → keep rows with ≥ 2 non-null values
df.na.fill(0, subset=["age"]) → fill null only in listed columns
F.raise_error(msg) → RuntimeException for EVERY evaluated row
F.assert_true(cond, msg) → NULL if true; RuntimeException if false/null
F.levenshtein(c1,c2) → IntegerType edit distance
```

### Delta Schema

```python
.mode("overwrite")                        # → AnalysisException if new col
.mode("overwrite").option("overwriteSchema","true")  # ✅ allowed
```

### JDBC Options

```
fetchsize → rows per round-trip from DB server
  higher = fewer round-trips, more executor memory per task
```

---

## TOPIC 4 — TROUBLESHOOTING: 5 KEY ANCHORS

```
T1  Arrow: arrow.pyspark.enabled=true + PyArrow installed → fast JVM↔Python transfer
T2  Column pruning ≠ predicate pushdown (complementary, not the same)
T3  spark.task.cpus=2 on 8-core executor → 4 concurrent tasks (halved)
T4  Off-heap: offHeap.enabled=true + offHeap.size > 0; NOT in JVM heap
T5  AQE coalesce target: advisoryPartitionSizeInBytes
```

### Catalyst Optimisation Pair

```
Column pruning:    remove unused columns from plan → less I/O
Predicate pushdown: move row filters to data source → fewer rows
→ BOTH can apply to same query simultaneously
→ DIFFERENT things, not aliases
```

### broadcastTimeout

```
spark.sql.broadcastTimeout = 300 s
→ driver waits for executors to RECEIVE broadcast variable
→ increase when: slow network OR large broadcast payload
```

### sortBeforeRepartition

```
spark.sql.execution.sortBeforeRepartition = true (default)
→ sorts each map-side partition by repartition key before shuffle write
→ reduces sort cost in downstream stages that also sort by same key
```

### Optimizer Iterations

```
spark.sql.optimizer.maxIterations = 100
→ if plan doesn't converge: WARNING logged (no exception!)
→ Spark continues with best plan produced so far
→ increase for very complex queries
```

### Off-heap Memory

```
spark.memory.offHeap.enabled = true
spark.memory.offHeap.size    = <positive bytes>
→ NOT part of spark.memory.fraction
→ NOT subject to JVM GC
→ reduces GC pressure
```

### AQE Partition Coalescing

```
Target merged partition size: spark.sql.adaptive.advisoryPartitionSizeInBytes
Lower bound on count:         spark.sql.adaptive.coalescePartitions.minPartitionNum
```

### ignoreMissingFiles

```
spark.sql.files.ignoreMissingFiles = true
→ query continues when input files deleted between planning and execution
→ use in data lakes with concurrent compaction
```

---

## TOPIC 5 — STREAMING: 5 KEY ANCHORS

```
SS1  Streaming file sources require EXPLICIT schema (no inference)
SS2  Console sink: all 3 output modes, dev/test only, NOT durable
SS3  watermark = max_event_time − delay; events past finalised window → DROPPED
SS4  Kafka schema always BINARY (key, value); fixed 7 columns
SS5  flatMapGroupsWithState: 0+ rows; append/update modes; NOT complete
```

### Trigger Comparison

| Trigger | Stops? | How many batches? |
|---------|--------|-----------------|
| `processingTime='5s'` | No (continuous) | Ongoing |
| `once=True` | Yes | **One mega-batch** |
| `availableNow=True` *(3.3+)* | Yes | **Multiple batches** (then stop) |

### Kafka Fixed Schema

```
key           → BinaryType   ← always binary, YOU decode
value         → BinaryType   ← always binary, YOU decode
topic         → StringType
partition     → IntegerType
offset        → LongType
timestamp     → TimestampType
timestampType → IntegerType
```

### Kafka Group ID

```
kafka.group.id NOT set (default) → Spark generates unique ID, manages offsets internally ✅
kafka.group.id IS set            → may conflict with internal checkpoint offsets ⚠️
```

### Watermark Late Data

```
Watermark = max(event_time_seen) − delay
Event is DROPPED if its window's end < current watermark
Example:
  Event time = 10:03, window = [10:00, 10:10)
  Delay = 5 min, processing time = 10:20
  Watermark = 10:15
  10:10 < 10:15 → window finalised → event DROPPED
```

### Session Window

```python
session_window("event_time", "30 minutes")   # Spark 3.2+
# New session when gap between events > 30 minutes
# Dynamic boundaries (not fixed tumbling windows)
```

### flatMapGroupsWithState Rules

```
vs mapGroupsWithState:
  flatMap → 0, 1, or MANY rows per group (not exactly 1)
Output modes: append or update (NOT complete)
Timeouts: ProcessingTimeTimeout or EventTimeTimeout
State: persisted in checkpoint → survives restart
```

---

## TOPIC 6 — SPARK CONNECT: 5 KEY ANCHORS

```
C1  AnalysisException → at ACTION time (not at transformation time)
C2  Token in URL: sc://host:15002/;token=my_token
C3  No JVM needed on client machine
C4  Python UDFs: supported (serialised to server); RDD ops: NOT supported
C5  Server crash: client alive, queries lost, must resubmit
```

### Connection URL Format

```python
# sc:// scheme, semicolon-separated params after path
SparkSession.builder.remote("sc://host:15002/;token=my_token").getOrCreate()
```

### UDF Support in Connect

```
Python UDFs    ✅ supported (serialised to server)
@pandas_udf    ✅ supported (Arrow serialisation)
SparkContext   ❌ NOT available
RDD ops        ❌ NOT available
```

### AnalysisException Timing

```
df.select(F.col("nonexistent"))   # No error yet — just builds plan
df.show()                          # ← AnalysisException raised HERE
# Plan sent to server for analysis only at action time
```

---

## TOPIC 7 — PANDAS API ON SPARK: 5 KEY ANCHORS

```
P1  psdf.spark.cache()   → caches underlying Spark DF
P2  psdf.spark.explain() → Spark physical plan
P3  default_index_type   = "distributed-sequence" (not "sequence"!)
P4  psdf.to_delta(path)  → valid convenience wrapper
P5  NaN ≠ NULL: dropna/isna operate on NULL only (NaN not treated as missing)
```

### Index Types

```
"distributed"          → fastest; non-contiguous values
"distributed-sequence" → fast; monotonically increasing per partition (DEFAULT)
"sequence"             → slowest; globally ordered (requires global sort)
```

### NaN vs NULL in Pandas-on-Spark

| Operation | NULL | NaN |
|-----------|------|-----|
| `isna()` / `isnull()` | **True** | **False** |
| `dropna()` | **Drops** | Does NOT drop |
| `fillna(0)` | **Fills** | Does NOT fill |

### spark.cache() vs spark.explain()

```python
psdf.spark.cache()    # → returns new psdf backed by cached Spark DF
psdf.spark.explain()  # → prints physical plan (same as .to_spark().explain())
```

---

## FUNCTION RETURN TYPE CHEATSHEET

| Function | Return Type |
|----------|------------|
| `datediff(end, start)` | IntegerType |
| `unix_timestamp()` | **LongType** |
| `trunc(date, fmt)` | **DateType** |
| `date_trunc(fmt, ts)` | **TimestampType** |
| `dayofweek(date)` | IntegerType (1=Sunday) |
| `levenshtein(c1,c2)` | **IntegerType** |
| `soundex(col)` | **StringType** |
| `F.conv(str, from, to)` | **StringType** (always) |
| `F.unhex(col)` | **BinaryType** |
| `F.to_csv(struct_col)` | **StringType** |
| `F.hash(*cols)` | **IntegerType** (32-bit) |
| `F.xxhash64(*cols)` | **LongType** (64-bit) |
| `map_entries(map_col)` | `ArrayType(StructType(key,value))` |
| `format_string(fmt, ...)` | **StringType** |
| `get_json_object(j, path)` | **StringType** |
| `nullif(e1, e2)` | Same type as e1, or NULL |

---

## ANSWER KEY QUICK-SCAN (Q1–Q100)

| Q | Ans | Q | Ans | Q | Ans | Q | Ans | Q | Ans |
|---|-----|---|-----|---|-----|---|-----|---|-----|
| 1 | B | 21 | B | 41 | B | 61 | A | 81 | B |
| 2 | B | 22 | C | 42 | B | 62 | B | 82 | B |
| 3 | B | 23 | C | 43 | B | 63 | B | 83 | B |
| 4 | A,B,C | 24 | B | 44 | B | 64 | A | 84 | A,B,C |
| 5 | B | 25 | A | 45 | B | 65 | B | 85 | B |
| 6 | C | 26 | B | 46 | A,B,D | 66 | B | 86 | B |
| 7 | A,B,C,D | 27 | C | 47 | B | 67 | B | 87 | B |
| 8 | A | 28 | C | 48 | A | 68 | B | 88 | B |
| 9 | B | 29 | A | 49 | B | 69 | A,B,C | 89 | B |
| 10 | A,C,D | 30 | B | 50 | B | 70 | B | 90 | A,B,C,D |
| 11 | A | 31 | B | 51 | B | 71 | B | 91 | B |
| 12 | B | 32 | A,B,D | 52 | A | 72 | B | 92 | B |
| 13 | C | 33 | B | 53 | B | 73 | A | 93 | B |
| 14 | B | 34 | B | 54 | B | 74 | A | 94 | A,B,D |
| 15 | C | 35 | B | 55 | B | 75 | B | 95 | B |
| 16 | B | 36 | A | 56 | C | 76 | B | 96 | B |
| 17 | A | 37 | B | 57 | A,B,D | 77 | B | 97 | B |
| 18 | A,B,C | 38 | B | 58 | B | 78 | A,B,D | 98 | B |
| 19 | B | 39 | A,B,C,D | 59 | B | 79 | A | 99 | C |
| 20 | B | 40 | B | 60 | B | 80 | B | 100 | A,C,D |

**Multi-answer questions (22 total):**
Q4, Q7, Q10, Q18, Q32, Q39, Q46, Q57, Q69, Q78, Q84, Q90, Q94, Q100

---

## EXAM DAY DECISION TREE

```
Question mentions default value?
  → Check defaults table above first

Question about RDD vs DataFrame/SQL config?
  → default.parallelism (RDD) vs shuffle.partitions (SQL/DF)

Question about null handling?
  → distinguish: NULL vs NaN (Pandas-on-Spark trap)
  → when/otherwise without otherwise → null
  → dropna drops NULL, not NaN

Question about storage level?
  → _SER suffix = serialised binary
  → MEMORY_ONLY eviction = dropped, not to disk

Question about streaming?
  → schema inference = NOT supported for file sources
  → Kafka value/key = always BinaryType (you decode)
  → watermark: events past finalised window = DROPPED

Question about Spark 3.x+ features?
  → withColumnsRenamed, unpivot, offset = Spark 3.4+
  → availableNow trigger = Spark 3.3+
  → session_window = Spark 3.2+
  → AQE default=true = Spark 3.2+
```

---

*Do not overwrite this file — it is part of the Iteration 5 study library.*
