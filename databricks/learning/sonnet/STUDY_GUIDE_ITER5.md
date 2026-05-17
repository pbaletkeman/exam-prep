# STUDY GUIDE — Iteration 5
# Databricks Certified Associate Developer for Apache Spark

**Coverage**: All 100 questions across 7 topics
**New topics vs Iter 4**: Storage levels SER variants, Block Manager, off-heap memory, RPC limits, sort-merge join I/O, Kubernetes, locality levels, pipelining; SQL: datediff, nullif, trunc vs date_trunc, locate, dayofweek, percentile exact vs approx, count_if, max_by, stack, get_json_object, sort_array direction, WINDOW clause, array_repeat, map_entries, GROUPING_ID, nth_value; DataFrame: transform, toLocalIterator, struct, withColumnsRenamed, foreach vs foreachPartition, mapInPandas, saveAsTable vs insertInto, levenshtein, thresh in na.drop, unpivot, raise_error, fetchsize, inferSchema cost, hash vs xxhash64, conv, unhex, overwriteSchema, simpleString vs toDDL, to_csv, sort_array vs array_sort nulls, reverse polymorphic, format_string, soundex, assert_true, offset; Streaming: availableNow trigger, inputRowsPerSecond, schema inference failure, console sink, session_window, Kafka schema, kafka.group.id, maxOffsetsPerTrigger, flatMapGroupsWithState; Connect: AnalysisException timing, token auth URL, no-JVM client; Pandas: spark.cache/explain, default_index_type, to_delta, NaN vs NULL

---

## TOPIC 1: Apache Spark Architecture & Internals

### 1.1 Key Configuration Pairs (Frequently Tested)

**`spark.sql.shuffle.partitions` vs `spark.default.parallelism`:**
- `spark.sql.shuffle.partitions`: controls post-shuffle partitions for **Spark SQL and DataFrame** operations (default 200)
- `spark.default.parallelism`: controls default partition count for **RDD operations** such as `parallelize()`, `reduceByKey()`, `groupByKey()` (default = total cores)
- These are NOT interchangeable — they govern separate layers

**`spark.driver.memory` default:** `1g` (not 512m, not 2g)

**`spark.sql.autoBroadcastJoinThreshold` default:** `10 MB`
- When one table's estimated size is ≤ 10 MB, Spark auto-selects BroadcastHashJoin
- Disable with -1 (NOT 0)

**`spark.sql.adaptive.enabled` default:** `true` since **Spark 3.2** (not false, not cluster-dependent)

### 1.2 Storage Levels — Deep Dive

| Level | Memory? | Disk? | Serialized? | Replicas |
|-------|---------|-------|-------------|---------|
| `MEMORY_ONLY` | ✅ | ❌ | No (JVM objects) | 1 |
| `MEMORY_ONLY_SER` | ✅ | ❌ | **Yes** (binary) | 1 |
| `MEMORY_AND_DISK` | ✅ | ✅ (spill) | No (JVM objects) | 1 |
| `MEMORY_AND_DISK_SER` | ✅ | ✅ (spill) | **Yes** (binary) | 1 |
| `DISK_ONLY` | ❌ | ✅ | Yes | 1 |
| `MEMORY_ONLY_2` | ✅ | ❌ | No | **2** |

**`MEMORY_AND_DISK_SER` vs `MEMORY_AND_DISK`:**
- `_SER` stores partitions as **serialised binary** in both memory and on disk → less memory, more CPU
- Without `_SER` stores as **deserialized JVM objects** → more memory, less CPU per read

**Eviction of `MEMORY_ONLY` partition:**
- Dropped from memory entirely — **NOT written to disk** (no disk fallback)
- If needed again, Spark **recomputes from lineage**
- Eviction candidates selected by **LRU** (Least Recently Used) policy

**`DISK_ONLY` partition on executor failure:**
- Disk is local to the failed executor → data lost with executor
- Spark **recomputes from lineage** (does NOT fail the job)

### 1.3 Memory Architecture

**Unified memory model:**
- `spark.memory.fraction` (default 0.6): fraction of JVM heap for Spark's unified pool (after 300 MB reserved)
- `spark.memory.storageFraction` (default 0.5): fraction of unified pool initially for storage (caching)
- Remaining fraction = execution (shuffle, sort, aggregation)
- Execution can **evict storage blocks** when it needs memory
- Setting `storageFraction=1.0` → zero initial allocation for execution

**Off-heap memory:**
- Enable: `spark.memory.offHeap.enabled=true` AND `spark.memory.offHeap.size=<positive>`
- NOT part of JVM heap → NOT subject to GC → does NOT count toward `spark.memory.fraction`
- Used for both storage and execution; reduces GC pressure

### 1.4 Spark Components

**Block Manager:**
Runs on each executor. Manages ALL blocks: cached RDD/DataFrame partitions, broadcast variable data, shuffle write files. NOT execution memory (that is managed by the MemoryManager).

**History Server setup (all 3 required):**
- `spark.eventLog.enabled = true` on the application
- `spark.eventLog.dir` → shared durable storage (HDFS/S3) — accessible by app AND History Server
- `spark.history.fs.logDirectory` on History Server → same path as `eventLog.dir`
- `spark.ui.enabled` is NOT required for History Server (it controls the live app UI only)

**Cached stages in Spark UI:** shown as **Skipped** (not Failed, not Running, not absent)

### 1.5 Cluster Managers & Deployment

**Kubernetes — Docker image config:**
```
spark.kubernetes.container.image    ← correct (both driver & executor pods)
spark.kubernetes.executor.image     ← WRONG
spark.kubernetes.docker.image       ← WRONG
```

**`spark.executor.instances` + `spark.dynamicAllocation.enabled=true`:**
- Spark logs a WARNING and **ignores `spark.executor.instances`**
- Dynamic allocation wins; uses `minExecutors` / `maxExecutors` instead

**`sc.setCheckpointDir()` requirement:**
- Must be a **reliable, distributed filesystem** (HDFS, S3, GCS) accessible by ALL executors
- `/tmp` does NOT provide reliable checkpointing

### 1.6 Scheduling & Execution

**Task locality order (most → least preferred):**
```
PROCESS_LOCAL → NODE_LOCAL → RACK_LOCAL → ANY
```
Spark waits `spark.locality.wait` (default 3s) at each level before downgrading.

**Transformations within one stage are pipelined:**
Each record flows through all narrow operators (filter, map, select) in sequence. No intermediate full materialisation. Enabled by WholeStageCodeGen.

**Stage count for:**
```python
df = spark.read.parquet(...)          # Stage 1: read
   .repartition(100)                  # Shuffle → Stage 2
   .groupBy("region").agg(sum(...))   # Shuffle → Stage 3
   .show()
```
Answer: **3 stages**

### 1.7 Shuffle & Networking

**Sort-merge join shuffle phases:**
- **Shuffle READ** is typically more expensive: each reducer pulls data from ALL mapper output files across the network/disk before the merge can begin

**`spark.reducer.maxReqsInFlight`:** max concurrent shuffle block fetch requests a single **reducer task** can issue to remote executors

**`spark.shuffle.file.buffer` (default 32 KB):** write buffer per shuffle output file — larger value → fewer syscalls → better sequential write throughput

**`spark.sql.execution.sortBeforeRepartition` (default true):** sorts each map-side partition by the repartition key before writing shuffle files → improves locality for downstream sort stages

**`spark.rpc.message.maxSize` (default 128 MB):**
- Governs point-to-point RPC messages
- Broadcast variables use **Torrent-style HTTP** distribution — **NOT subject** to this limit
- `collect()` result size governed by **`spark.driver.maxResultSize`**, not this config

### 1.8 AQE (Adaptive Query Execution)

**Post-shuffle partition coalescing:**
- Target merge size: `spark.sql.adaptive.advisoryPartitionSizeInBytes`
- Minimum partition count lower bound: `spark.sql.adaptive.coalescePartitions.minPartitionNum`

**Catalyst optimizer iterations:**
- `spark.sql.optimizer.maxIterations` (default 100)
- If plan doesn't converge: **logs a WARNING** and proceeds with best plan — does NOT throw an error

---

## TOPIC 2: Spark SQL

### 2.1 Date & Time Functions

| Function | Input Type | Return Type | Notes |
|----------|-----------|------------|-------|
| `datediff(end, start)` | DateType | IntegerType | `end − start` in days (positive if end > start) |
| `unix_timestamp()` | (no args) | **LongType** | Current epoch seconds — NOT TimestampType |
| `trunc(date, fmt)` | DateType | **DateType** | Truncates to month/year; arg order: date first |
| `date_trunc(fmt, ts)` | TimestampType | **TimestampType** | Truncates to hour/minute/second; arg order: fmt first |
| `last_day(date)` | DateType | DateType | Last day of month: `last_day('2026-04-10')` = `'2026-04-30'` |
| `dayofweek(date)` | DateType | IntegerType | **1=Sunday**, 2=Monday, ..., 7=Saturday |
| `initcap(str)` | StringType | StringType | Capitalises first letter of each word |

**`trunc` vs `date_trunc` — key difference:**
- `trunc(date, 'month')` → DateType (e.g., `2024-07-01`)
- `date_trunc('hour', timestamp)` → TimestampType (e.g., `2024-07-15 14:00:00`)
- **Argument order is different!** `trunc(col, fmt)` vs `date_trunc(fmt, col)`

### 2.2 String & Pattern Functions

| Function | Returns | Notes |
|----------|---------|-------|
| `initcap("hello world")` | `"Hello World"` | First letter of each word capitalised |
| `locate("world", "hello world", 1)` | 7 | 1-based indexing, start pos=1; "world" starts at position 7 |
| `soundex(col)` | StringType | Phonetic code; "Smith" = "Smyth" = S530 |
| `format_string("%s has %d items", col1, col2)` | StringType | printf-style; col refs are valid args |
| `nullif(expr1, expr2)` | expr1 or NULL | Returns NULL if expr1 = expr2, else returns expr1 |

**`locate(substr, str, pos)` details:**
- Uses **1-based** indexing
- `pos` is the starting position for search (1 = beginning)
- Returns 0 if not found (like `instr`)

### 2.3 Array & Map Functions

| Function | Returns | Notes |
|----------|---------|-------|
| `array_repeat('x', 3)` | `['x','x','x']` | Repeats element N times |
| `sort_array(col, True/False)` | ArrayType | True=ascending, False=**descending**; nulls at **beginning** |
| `array_sort(col)` | ArrayType | Always ascending; nulls at **end** |
| `map_entries(map_col)` | `ArrayType(StructType(key,value))` | One struct per K-V pair |
| `F.reverse(col)` | Same type as input | On String: reverses chars; on Array: reverses element order |

**`sort_array` vs `array_sort` null placement:**
- `sort_array(col, asc=True)`: nulls at the **beginning** (first)
- `array_sort(col)`: nulls at the **end** (last)

### 2.4 Aggregate & Analytic Functions

**`percentile` vs `percentile_approx`:**
- `percentile(col, 0.5)` = **exact** median via full sort — not scalable for large data
- `percentile_approx(col, 0.5)` = approximate via **Greenwald–Khanna** sketch — scalable

**`count_if(condition)`:** counts rows where boolean condition = **true** (not just non-null)

**`max_by(value_col, ordering_col)`:** introduced **Spark 3.0** — returns `value_col` from the row with the max `ordering_col` within the group

**`nth_value(col, n)`:** value of `col` from the **n-th row** of the current window frame; returns NULL if fewer than n rows in frame

### 2.5 SQL Features

**`nullif(expr1, expr2)`:** Returns NULL if expr1 = expr2; otherwise returns expr1
Use case: convert sentinel value to NULL (e.g., `nullif(status, 'N/A')`)

**`stack(n, v1, v2, ...)`:**
Transposes every n values into a row:
```sql
SELECT stack(2, 'a', 1, 'b', 2) AS (letter, num)
-- Returns: ('a', 1) and ('b', 2) — TWO rows
```

**`get_json_object(json_str, '$.user.name')`:**
- Returns **StringType** scalar value
- Supports nested JSONPath ($.user.name works)

**`F.conv("FF", 16, 10)`:**
- Converts hex FF → decimal 255
- Return type is always **StringType** (result = `"255"`)

**`F.unhex(col)`:**
- Interprets hex digit pairs as bytes
- Returns **BinaryType** — inverse of `F.hex(col)`

### 2.6 Window Functions & Clauses

**SQL WINDOW clause syntax:**
```sql
SELECT name, rank() OVER w AS rnk
FROM employees
WINDOW w AS (PARTITION BY dept ORDER BY salary DESC)
```
The WINDOW clause comes at the end of the SELECT statement.

**GROUPING_ID bitmask:**
- Bit value 1 = column is rolled up (aggregated), 0 = column is in grouping key
- `GROUPING_ID` value 0 = finest grain (all columns in group key)
- `GROUPING_ID` value 3 (binary `11`) for ROLLUP(dept, team) = grand total row
- Column **order matters** — changing order changes bitmask values

### 2.7 CTE Behaviour

**Common Table Expressions in Spark SQL:**
- `WITH ranked AS (...)` — defines a named subquery ✅
- Multiple CTEs separated by commas ✅
- NOT always materialised to disk — Catalyst typically inlines them ✅
- **Recursive CTEs (`WITH RECURSIVE`) NOT supported** in Spark SQL through 3.5 ✅

---

## TOPIC 3: DataFrame/DataSet API

### 3.1 Useful Methods — New in Iter 5

**`df.columns`:** Returns Python **list of strings** (not StructType, not tuples)

**`df.transform(func)`:** Calls `func(df)` and returns the resulting DataFrame. Used for clean pipeline chaining:
```python
df.transform(add_audit_cols).transform(cast_types).transform(apply_business_rules)
```

**`df.toLocalIterator()`:** Streams one partition at a time to driver — peak driver memory = one partition. `collect()` pulls entire result at once.

**`df.withColumnsRenamed({"old1":"new1","old2":"new2"})`:** Spark 3.4+ — renames multiple columns atomically in one call.

**`df.unpivot(ids, values, variableColumnName, valueColumnName)`:** Spark 3.4+ — wide→long format (melt). `ids` kept as-is; `values` columns become two new columns.

**`df.offset(n)`:** Spark 3.4+ — skips first n rows. Equivalent to SQL `OFFSET n`.

### 3.2 foreach vs foreachPartition

| Method | Call frequency | Argument | Return |
|--------|---------------|----------|--------|
| `df.foreach(func)` | Once **per Row** | Single `Row` object | None |
| `df.foreachPartition(func)` | Once **per partition** | Iterator of `Row` objects | None |

`foreachPartition` is more efficient for external connections — setup cost (DB open) amortised over all rows in the partition.

### 3.3 mapInPandas vs applyInPandas

| Method | Grouping | Function receives | Function returns |
|--------|---------|-------------------|-----------------|
| `applyInPandas(func, schema)` | GroupBy key | `pd.DataFrame` per group | `pd.DataFrame` |
| `mapInPandas(func, schema)` | Partition | Iterator of `pd.DataFrame` per partition | Iterator of `pd.DataFrame` |

**`mapInPandas`:** partition-by-partition, no groupBy required. Function must take and yield iterators of `pd.DataFrame`.

### 3.4 Column Functions

**`F.struct(col1, col2)`:**
- Returns `StructType([StructField("col1",...), StructField("col2",...)])`
- Fields named after input columns

**`F.raise_error(msg)`** (Spark 3.1+):
- Raises `RuntimeException` for **every row** where the column is evaluated (condition: false or NULL)
- NOT a UDF — it is a native Catalyst expression (much faster than Python UDF)
- Typically used inside `when()` for inline data quality enforcement

**`F.assert_true(condition, errMsg)`** (Spark 3.1+):
- Returns **NULL** column value when condition = true
- Raises `RuntimeException` when condition = false or NULL
- Used inside `df.select()` for inline validation
- NOT equivalent to a UDF — far lower overhead

**`F.levenshtein(col1, col2)`:** Returns **IntegerType** edit distance. Not boolean, not DoubleType.

**`F.soundex(col)`:** Returns **StringType** Soundex phonetic code. "Smith" and "Smyth" → same code `S530`.

**`F.hash(*cols)`:** MurmurHash3, returns **IntegerType** (32-bit)
**`F.xxhash64(*cols)`:** xxHash64, returns **LongType** (64-bit); both are non-cryptographic

**`F.conv("FF", 16, 10)`:** Base conversion; always returns **StringType** (result: `"255"`)

**`F.reverse(col)`:** Polymorphic — reverses string chars OR array elements. Return type = input type.

**`F.format_string(fmt, *cols)`:** printf-style formatting; accepts Column references; returns StringType.

**`F.to_csv(struct_col)`:** Serialises struct to **StringType** CSV-formatted string. Fields in struct schema order.

### 3.5 Null Handling

**`df.na.drop(thresh=N)`:** Keeps row only if it has **at least N non-null values**. (Not: drop if MORE than N nulls.)

**`df.na.fill(0, subset=[...])`:** Fills nulls with 0 only in the listed columns.

**`F.when()` without `.otherwise()`:** Unmatched rows → **null** (same as Iter 4).

### 3.6 Read/Write Details

**`saveAsTable` vs `insertInto`:**
- `saveAsTable`: creates/replaces table using DataFrame's schema (schema-aware)
- `insertInto`: inserts by **column position** (NOT column name); target table **must already exist**; dangerous if column order differs

**Delta overwrite with new column:**
```python
df.write.format("delta").mode("overwrite").save("/delta/my_table")
# → AnalysisException if new column not in existing schema
# Fix: .option("overwriteSchema", "true")
```

**JDBC `fetchsize`:** rows per round-trip from database server. Larger = fewer round-trips, more executor memory.

**CSV `inferSchema=true`:** makes **TWO full passes** over data → doubles I/O cost. Always prefer explicit schema.

**CSV `sep` and `delimiter`:** both are **valid aliases** for the same option.

**CSV `nullValue` vs `emptyValue`:**
- `nullValue`: string written for **NULL** database values (default `""`)
- `emptyValue`: string written for **empty string** (zero-length) values (default `""`)
- They are distinct: database NULL ≠ empty string

### 3.7 Schema Methods

**`schema.simpleString()`:** compact internal format — `struct<id:int,name:string>`
**`schema.toDDL()`:** SQL DDL format — `` `id` INT,`name` STRING `` — suitable for CREATE TABLE

### 3.8 Performance Trade-offs

**Arrow-accelerated data transfer:**
- Config: `spark.sql.execution.arrow.pyspark.enabled=true`
- Applies to: `toPandas()`, `createDataFrame(pandas_df)`, Pandas UDFs
- Requires: **PyArrow installed** in Python environment

---

## TOPIC 4: Troubleshooting & Tuning

### 4.1 Catalyst Optimisations

**Column pruning:** removes unreferenced columns from the plan early → less I/O and memory
**Predicate pushdown:** moves row filters closer to the data source → fewer rows read
Both are **complementary** — a query can benefit from both simultaneously.

**CBO:**
- `spark.sql.cbo.enabled=true` alone → smarter join strategy selection based on statistics
- `spark.sql.cbo.joinReorder.enabled=true` (also needed) → join reordering
- `ANALYZE TABLE t COMPUTE STATISTICS FOR ALL COLUMNS` → updates column NDV, min, max, null count

### 4.2 Broadcast

**`spark.sql.broadcastTimeout` (default 300s):**
Time driver waits for executor nodes to **receive and acknowledge** a broadcast variable.
Increase when: slow network OR very large broadcast payload.

### 4.3 Multi-core Tasks

**`spark.task.cpus=2`:**
Each task requests 2 CPUs → 8-core executor runs only **4 concurrent tasks** instead of 8.
Halves task-level parallelism per executor.

### 4.4 File Handling

**`spark.sql.files.ignoreMissingFiles=true`:**
Allows query to continue when files deleted between planning and execution.
Used in data lakes with concurrent compaction jobs.

### 4.5 Off-heap Memory

Enable: `spark.memory.offHeap.enabled=true` + `spark.memory.offHeap.size=<positive>`
- Reduces GC pressure (outside JVM heap)
- Does NOT contribute to `spark.memory.fraction`
- NOT subject to JVM GC

### 4.6 AQE Coalescing

**AQE post-shuffle partition coalescing:**
- `spark.sql.adaptive.advisoryPartitionSizeInBytes` = target merged size
- `spark.sql.adaptive.coalescePartitions.minPartitionNum` = lower bound on partition count

---

## TOPIC 5: Structured Streaming

### 5.1 Triggers

| Trigger | Behaviour |
|---------|----------|
| `trigger(processingTime='5 seconds')` | Fixed interval micro-batches |
| `trigger(once=True)` | All available data in **one mega-batch**, then stop |
| `trigger(availableNow=True)` *(Spark 3.3+)* | All available data across **multiple micro-batches** (respects per-batch limits), then stop |
| `trigger(continuous='1 second')` | Experimental continuous processing |

**`availableNow` vs `once` difference:**
`once` = one enormous batch; `availableNow` = multiple smaller batches (respects `maxFilesPerTrigger`, better fault tolerance)

### 5.2 Progress & Monitoring

**`query.inputRowsPerSecond`:** ingestion rate from the source during the **last** micro-batch (rows / batch duration). Not cumulative.

**`query.lastProgress`:** single dict for the most recent batch
**`query.recentProgress`:** list of dicts for recently completed batches

### 5.3 Schema Inference — Streaming

**Streaming file sources (JSON, CSV, Parquet) do NOT support schema inference.**
Must provide explicit schema → otherwise `AnalysisException`.

### 5.4 Console Sink

- Writes each micro-batch output to driver **stdout**
- Dev/testing only — NOT production
- Supports **all three** output modes: `append`, `update`, `complete`
- NOT durable — no checkpoint recovery

### 5.5 Late Data & Watermark

**Late event dropped when:**
`watermark = max_event_time_seen − delay`
If `event_time` falls in a window whose end < current watermark → event **silently discarded**

**Example:** event_time=10:03, watermark delay=5min, processing_time=10:20
Watermark ≈ 10:15. Window [10:00,10:10) ends at 10:10 < 10:15 → **dropped**

### 5.6 Session Windows

**`session_window("event_time", "30 minutes")`** (Spark 3.2+):
Dynamic, gap-based sessions. New session starts when no event seen for 30 minutes. Window boundaries are NOT fixed in advance.

### 5.7 Kafka Source

**Fixed schema:**
```
key             BinaryType
value           BinaryType
topic           StringType
partition       IntegerType
offset          LongType
timestamp       TimestampType
timestampType   IntegerType
```
Always binary — deserialization is application responsibility.

**`kafka.group.id`:**
- When set: uses fixed consumer group → may conflict with Spark's internal checkpoint offsets
- When not set (recommended): Spark generates unique group ID per query and manages offsets internally

**`maxOffsetsPerTrigger`:** caps messages consumed per micro-batch trigger — primary backlog throttle.

### 5.8 flatMapGroupsWithState

- Emits **zero or more** rows per group (unlike `mapGroupsWithState` = exactly one)
- Supports timeouts: `ProcessingTimeTimeout` or `EventTimeTimeout`
- Output mode: **append or update** (NOT complete)
- State persisted in checkpoint → survives query restarts

---

## TOPIC 6: Spark Connect

### 6.1 Error Surfacing

**`AnalysisException` timing:**
Errors (non-existent column, type mismatch) are surfaced **at action time** (`collect()`, `show()`, `count()`), NOT when the transformation is defined. The logical plan is sent to the server for analysis only when an action is triggered.

### 6.2 Authentication

**Token in connection URL:**
```python
SparkSession.builder.remote("sc://host:15002/;token=my_token").getOrCreate()
```
Semicolon-separated parameters after the path segment.

### 6.3 No-JVM Client

A machine without Java installed can:
- `import pyspark.sql.SparkSession`
- Call `.remote("sc://...")`
- Execute queries on the remote Spark Connect server
- The **local JVM is NOT required** on the client machine

### 6.4 UDFs in Spark Connect

- Python UDFs: **supported** — serialised and sent to server; execute on executors
- External Python libs: must be available on **executor environment** (not just client)
- Pandas UDFs (`@pandas_udf`): **supported** via Arrow serialization
- `SparkContext` / RDD operations: **NOT available** via Spark Connect ← common exam trap

### 6.5 Server Crash

- Client Python process does NOT crash
- In-progress queries are **lost**
- No automatic replay
- Client must reconnect and resubmit

---

## TOPIC 7: Pandas API on Spark

### 7.1 Spark Accessor Methods

| Method | Description |
|--------|-------------|
| `psdf.spark.cache()` | Caches underlying Spark DF; returns new psdf backed by cached data |
| `psdf.spark.explain()` | Prints Spark physical plan (= `psdf.to_spark().explain()`) |
| `psdf.spark.hint(...)` | Passes hints to the underlying Spark plan |

### 7.2 Index Types

**`ps.options.compute.default_index_type` default: `"distributed-sequence"`**

| Index Type | Speed | Global Order | Notes |
|-----------|-------|-------------|-------|
| `"distributed"` | Fastest | No (non-contiguous) | Random per-partition values |
| `"distributed-sequence"` | **Fast (default)** | **Not strict** | Monotonically increasing per partition |
| `"sequence"` | Slowest | **Strict** | Global sort required |

### 7.3 Writing Delta

Both are valid:
```python
psdf.to_delta("/path/to/delta_table")               # convenience wrapper
psdf.to_spark().write.format("delta").save("/path") # underlying call
```

### 7.4 NaN vs NULL (Critical Difference)

| | Native Pandas | Pandas API on Spark |
|-|---------------|---------------------|
| Missing representation | NaN and None both treated as missing | **NULL** = missing (Spark SQL); **NaN** = distinct non-null float value |
| `fillna(0)` fills | Both NaN and None | Only NULL — NaN is NOT filled |
| `dropna()` drops | NaN and None rows | Only NULL rows — NaN rows NOT dropped |
| `isna()`/`isnull()` | True for both | **True for NULL, False for NaN** |

---

## KEY TRAPS — Iteration 5

| # | Trap | Correct Answer |
|---|------|---------------|
| 1 | `spark.driver.memory` default is 2g | Default is **1g** |
| 2 | `autoBroadcastJoinThreshold` default is 200 MB | Default is **10 MB** |
| 3 | AQE was off by default before 3.2 | Default **true since Spark 3.2** |
| 4 | DISK_ONLY partition failure → job fails | Spark **recomputes from lineage** |
| 5 | `spark.ui.enabled` needed for History Server | NOT required; only `eventLog.enabled`, `eventLog.dir`, `history.fs.logDirectory` |
| 6 | Broadcast vars limited by `rpc.message.maxSize` | Broadcast uses HTTP Torrent — **NOT subject** to RPC message limit |
| 7 | Shuffle READ is cheaper than shuffle WRITE | **Shuffle READ is more expensive** in sort-merge join |
| 8 | `executor.instances` and DRA → DRA uses instances as max | DRA **ignores** `executor.instances`; warns and uses `minExecutors`/`maxExecutors` |
| 9 | Locality order: ANY → NODE_LOCAL → PROCESS_LOCAL | Correct order: **PROCESS_LOCAL → NODE_LOCAL → RACK_LOCAL → ANY** |
| 10 | `MEMORY_ONLY` eviction → written to disk | **Dropped entirely** — no disk fallback; recomputed from lineage |
| 11 | `spark.memory.storageFraction=1.0` is fine | Leaves zero execution memory → tasks must evict storage before any execution |
| 12 | `MEMORY_AND_DISK_SER` uses Kryo | Uses **Java serialisation** (not Kryo unless globally configured) |
| 13 | `unix_timestamp()` returns TimestampType | Returns **LongType** (epoch seconds) |
| 14 | `trunc` and `date_trunc` are interchangeable | NOT interchangeable — different input/return types AND arg order |
| 15 | `locate` is 0-based | **1-based** indexing; returns 0 if not found |
| 16 | `sort_array(col, False)` = ascending | False = **descending** |
| 17 | `array_sort` and `sort_array` both place nulls at start | `sort_array` = nulls first; `array_sort` = **nulls last** |
| 18 | `percentile_approx` always returns exact when accuracy is high | `percentile_approx` is approximate; only `percentile` is exact |
| 19 | `count_if` counts non-null values | Counts rows where condition = **true** |
| 20 | `max_by` introduced in Spark 3.3 | Introduced in **Spark 3.0** |
| 21 | CTEs are always materialised to disk | **Not always** — Catalyst typically inlines them |
| 22 | Recursive CTEs supported in Spark 3.4+ | NOT supported through **Spark 3.5** |
| 23 | `F.conv` returns IntegerType | Always returns **StringType** |
| 24 | `df.transform(func)` is like `F.transform(col, func)` | They are different! `df.transform` is DataFrame-level; `F.transform` is array element-wise |
| 25 | `toLocalIterator` returns a Pandas DataFrame | Returns Python **iterator** of Row objects |
| 26 | `insertInto` uses column names | Uses column **position** — dangerous if order differs |
| 27 | `assert_true` is implemented as a Python UDF | It's a native **Catalyst expression** (far faster) |
| 28 | `levenshtein` returns a boolean or float | Returns **IntegerType** edit distance |
| 29 | `inferSchema=true` is a one-pass operation | Makes **two full passes** over data (doubles I/O) |
| 30 | Streaming AnalysisException surfaces at transformation time | Surfaces at **action time** in Spark Connect |
| 31 | `trigger(availableNow=True)` runs forever | Processes all available data then **stops** |
| 32 | `kafka.group.id` is required | NOT required; omitting it is recommended for Spark-managed offsets |
| 33 | `flatMapGroupsWithState` uses `complete` output mode | Requires **append or update**, NOT complete |
| 34 | `psdf.cache()` is valid | Must use **`psdf.spark.cache()`** |
| 35 | `psdf.dropna()` drops NaN rows | Drops **NULL** rows; NaN is NOT dropped by `dropna()` |

---

*Do not overwrite this file — it is part of the Iteration 5 study library.*
