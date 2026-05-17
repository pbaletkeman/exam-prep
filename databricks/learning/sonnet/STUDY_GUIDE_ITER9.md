# Study Guide — Iteration 9
## Databricks Certified Associate Developer for Apache Spark

---

## Exam Overview

| Property | Value |
|---|---|
| **Iteration** | 9 |
| **Total Questions** | 100 |
| **Answer Type** | All `one` (single-select) |
| **Difficulty** | 10 Easy / 54 Medium / 36 Hard |
| **Generated** | 2026-04-25 |

### ⚠️ CRITICAL: Answer Distribution Alert

> **This iteration has THREE answer options used.** Unlike Iter 7 (all B) or Iter 8 (96B + 4A):
>
> - **89 questions = B** (default assumption)
> - **8 questions = A**: Q15, Q31, Q33, Q41, Q45, Q56, Q83, Q85
> - **3 questions = C**: Q1, Q3, Q4
>
> All three C answers are in the **Architecture topic (Q1–Q20)**. If you see a question about SparkSession/SparkContext, YARN memory, or stage boundaries — the answer may be **C, not B**.

---

## Topic Breakdown

| Topic | Questions | Easy | Medium | Hard |
|---|---|---|---|---|
| Architecture & Internals | Q1–Q20 | 2 | 9 | 9 |
| Spark SQL | Q21–Q40 | 1 | 13 | 6 |
| DataFrame/Dataset API | Q41–Q70 | 2 | 17 | 11 |
| Troubleshooting & Tuning | Q71–Q80 | 0 | 5 | 5 |
| Structured Streaming | Q81–Q90 | 2 | 5 | 3 |
| Spark Connect | Q91–Q95 | 1 | 3 | 1 |
| Pandas API on Spark | Q96–Q100 | 2 | 2 | 1 |

---

## Topic 1: Apache Spark Architecture & Internals (Q1–Q20)

### SparkSession and SparkContext (Q1 = **C**)

`SparkSession` wraps `SparkContext`. `SparkSession` is the unified entry point introduced in Spark 2.0. You access the `SparkContext` via `spark.sparkContext`. **Never create a SparkContext manually when using SparkSession.builder.**

- `SparkSession` → entry point for DataFrame/SQL/streaming APIs
- `spark.sparkContext` → access to the underlying RDD-level `SparkContext`
- In cluster mode: driver JVM is on a worker; local paths on submit machine are inaccessible (Q12)

### Parallelism Configs (Q2)

| Config | Controls | Default |
|---|---|---|
| `spark.default.parallelism` | RDD ops (`reduceByKey`, `join`) | # of cores in cluster |
| `spark.sql.shuffle.partitions` | DataFrame/SQL shuffle partitions | 200 |

Setting only `spark.default.parallelism` does **not** fix slow DataFrame shuffles.

### YARN Container Memory (Q3 = **C**)

```
Container Memory = executor.memory + executor.memoryOverhead + memory.offHeap.size
                 = 4 GB + 512 MB + 1 GB = 5.5 GB
```

All three regions are requested separately from YARN. `offHeap.size` is outside the JVM heap.

### Stage Boundaries (Q4 = **C**)

Each **wide transformation** (shuffle) creates a new stage boundary:

```
rdd.map → filter → groupByKey → map → join(other_rdd)
                        ↑                  ↑
                    Stage 1|2          Stage 2|3
                    = 3 stages total
```

- `map`, `filter` = narrow → pipelined within a stage
- `groupByKey`, `join` = wide → each creates a new stage

### Task-Level Parallelism (Q5)

```
Concurrent tasks = spark.executor.cores / spark.task.cpus
                 = 8 / 2 = 4 tasks
```

`spark.task.cpus > 1` is used for multi-threaded libraries like TensorFlow or BLAS to prevent CPU over-subscription.

### Speculative Execution (Q6)

`spark.speculation=true` launches a **duplicate copy** of a straggler task on another executor. Both run simultaneously; the first to finish wins. **Risk**: non-idempotent side effects (e.g., external writes) may execute twice.

### heartbeatInterval vs networkTimeout (Q7)

```
spark.executor.heartbeatInterval  <  spark.network.timeout
```

If heartbeat ≥ network timeout, the driver declares the executor dead before receiving its heartbeat → false failures. Rule: keep heartbeat at least 4× less than network timeout.

### External Shuffle Service + Dynamic Allocation (Q8)

Without `spark.shuffle.service.enabled=true`, shuffle files are stored in executor JVM processes. When dynamic allocation removes idle executors, those shuffle files are lost. The external shuffle service runs as a separate long-lived daemon and serves shuffle files independently.

### Kryo vs Java Serialization (Q9)

| Property | KryoSerializer | JavaSerializer |
|---|---|---|
| Speed | ~5–10× faster | Default (slower) |
| Output size | ~2–5× smaller | Larger |
| Class registration | Required for optimal perf | Not required |
| Config | `spark.kryo.classesToRegister` | Default |

### executor.cores and Task Slots (Q10)

`spark.executor.cores` = number of concurrent task slots. With 16 node cores and 5 cores per executor: `floor(16/5) = 3` executors per node (uses 15 cores; 1 reserved for OS/NodeManager).

### Rolling Event Logs (Q11)

`spark.eventLog.rolling.enabled=true` splits event logs into multiple smaller files based on `spark.eventLog.rolling.maxFileSize`. Prevents a single file from growing to gigabytes for long-running streaming apps. History Server can load segments on demand.

### Small File Grouping: openCostInBytes (Q13)

`spark.sql.files.openCostInBytes` (default: 4 MB) is added to each file's size when computing partition splits. A 1 KB file is treated as ~4 MB, so ~32 small files pack into one 128 MB partition instead of creating 10,000 single-file partitions.

### Shuffle Data Fetching (Q14)

`spark.reducer.maxSizeInFlight` (default: 48 MB) bounds how much map output data one reducer fetches concurrently. Lowering reduces network saturation; raising improves throughput when network is not saturated.

### shuffle.compress vs shuffle.spill.compress (Q15 = **A**)

| Config | What it compresses |
|---|---|
| `spark.shuffle.compress` | **Shuffle output block files** (map task output) |
| `spark.shuffle.spill.compress` | **Intermediate spill files** (during in-memory sort) |

Both default to `true` and use the codec from `spark.io.compression.codec`.

### Broadcast Compression (Q16)

`spark.broadcast.compress=true` (default). Broadcast blocks are compressed at the driver before transmission using `spark.io.compression.codec`. For large broadcast variables this significantly reduces network I/O.

### Periodic GC for Cleaner (Q17)

`spark.cleaner.periodicGC.interval` (default: 30 min). Spark's `ContextCleaner` uses weak references. This setting triggers JVM GC on the driver so those weak references are actually collected and unpersisted RDDs/destroyed broadcasts are cleaned up.

### Off-Heap Memory (Q18)

`spark.memory.offHeap.enabled=true` + `spark.memory.offHeap.size=2g`. Both **execution and storage memory** can use the off-heap pool via Tungsten's direct memory manager. Reduces GC pause times since off-heap is not tracked by JVM GC.

### Dynamic Allocation Idle Timeout (Q19)

`spark.dynamicAllocation.executorIdleTimeout=60s`. After 60 seconds with no running tasks, Spark requests the cluster manager to decommission the executor. Executors with cached data are retained longer (`cachedExecutorIdleTimeout`).

### CBO Histogram Collection (Q20)

`spark.sql.statistics.histogram.enabled` must be `true` (default: **false**) for `ANALYZE TABLE ... COMPUTE STATISTICS FOR COLUMNS` to collect height-balanced histograms. Without this, only basic stats (min, max, count, nullCount) are gathered. Histograms allow the CBO to estimate selectivity of range predicates.

---

## Topic 2: Spark SQL (Q21–Q40)

### String Padding: LPAD/RPAD (Q21)

```sql
LPAD(code, 8, '0')   -- pads LEFT  with '0' to total length 8
RPAD(code, 8, '0')   -- pads RIGHT with '0' to total length 8
```

If the string is already longer than `len`, it is truncated from the right.

### locate(substr, str, pos) — 1-based (Q22)

```sql
locate('at', 'data at scale', 6)  -- returns 8
-- 'at' found at positions 2 and 8; searching from pos 6 → finds position 8
-- Returns 0 when not found
```

### repeat(str, n) Edge Cases (Q23)

```sql
repeat('ab', 0)   -- returns ''  (empty string)
repeat('ab', -1)  -- returns ''  (empty string)
repeat(NULL, 3)   -- returns NULL
```

### Tumbling Windows in SQL (Q24)

```sql
SELECT window(event_time, '10 minutes'), count(*)
FROM events GROUP BY window(event_time, '10 minutes')
```

Result column `window` is a struct `{start: TimestampType, end: TimestampType}`. Works in both batch and streaming.

### unix_timestamp vs to_timestamp (Q25)

| Function | Returns |
|---|---|
| `unix_timestamp(str, fmt)` | `LongType` (epoch seconds since 1970-01-01 UTC) |
| `to_timestamp(str, fmt)` | `TimestampType` |

Default format for both: `yyyy-MM-dd HH:mm:ss`.

### timestampadd (Q26 — Spark 3.3+)

```sql
TIMESTAMPADD('HOUR', 3, event_ts)
-- Argument order: unit string, integer delta, timestamp
-- Valid units: 'YEAR', 'MONTH', 'WEEK', 'DAY', 'HOUR', 'MINUTE', 'SECOND'
-- Introduced in Spark 3.3
```

### typeof(expr) (Q27)

```sql
typeof(ARRAY(1, 2, 3))  -- returns 'array<int>'
typeof(MAP('a', 1))     -- returns 'map<string,int>'
```

Returns the full DDL type string including nested types.

### stack(n, ...) — Unpivot to Rows (Q28)

```sql
stack(2, 'q1', 100, 'q2', 200)
-- Returns 2 rows, 2 columns:
-- Row 1: ('q1', 100)
-- Row 2: ('q2', 200)
-- Column names default to col0, col1
```

### map_contains_key vs map[key] IS NOT NULL (Q29 — Spark 3.3+)

| Expression | Key absent | Key present, value null | Key present, value non-null |
|---|---|---|---|
| `map['key'] IS NOT NULL` | `false` | `false` (wrong!) | `true` |
| `map_contains_key(map, 'key')` | `false` | `true` (correct!) | `true` |

Use `map_contains_key` to distinguish missing keys from null-valued keys.

### array_position Returns 0, Not null (Q30)

```sql
array_position(array('a', 'b', 'c'), 'd')  -- returns 0 (not found)
array_position(array('a', 'b', 'c'), 'a')  -- returns 1 (1-based!)
```

### reduce() with Optional Finish (Q31 = **A**)

```sql
reduce(array(1, 2, 3, 4), 0, (acc, x) -> acc + x)
-- Returns 10 (0+1+2+3+4)

-- Optional 4th argument: finish function
reduce(array(1,2,3), 1, (acc,x)->acc*x, acc->acc+100)
-- 1*1*2*3=6, then 6+100=106
```

The answer is **A** because option A correctly states that the optional 4th `finish` argument transforms the final accumulator.

### date_part for Quarter (Q32)

```sql
date_part('QUARTER', TIMESTAMP '2024-08-15 14:30:00')  -- returns 3
-- August = Q3
-- Equivalent to: EXTRACT(QUARTER FROM source)
-- Valid fields: 'YEAR', 'MONTH', 'DAY', 'HOUR', 'MINUTE', 'SECOND', 'WEEK', 'DOW'
```

### make_interval (Q33 = **A**)

```sql
start_date + make_interval(1, 6)
-- Adds 1 year and 6 months
-- make_interval(years, months, weeks, days, hours, mins, secs)
-- Introduced in Spark 3.0
```

Answer is **A** because option A correctly shows `start_date + make_interval(1, 6)`.

### ILIKE — Case-Insensitive LIKE (Q34 — Spark 3.3+)

```sql
description ILIKE '%error%'          -- matches 'Error', 'ERROR', 'eRrOr'
event_name ILIKE ANY ('click_%', 'tap_%')  -- multi-pattern case-insensitive
```

More explicit and readable than `LOWER(col) LIKE LOWER(pattern)`.

### DECODE with NULL (Q35)

```sql
DECODE(status, 'A', 'Active', 'I', 'Inactive', 'Unknown')
-- For status=NULL: returns 'Unknown' (the default)
-- DECODE treats NULL=NULL as equal for search values,
-- but status=NULL doesn't match 'A' or 'I', so default is returned
```

### to_csv(struct, options) (Q36)

```sql
to_csv(row_data, map('sep', '|'))
-- {id:1, name:'Alice', score:99.5}  →  '1|Alice|99.5'
-- Serializes struct fields as delimiter-separated values in schema order
-- Inverse of from_csv()
```

### date_part vs date_trunc (Q37)

```sql
date_part('MONTH', event_ts)        -- returns integer: 8 (for August)
date_trunc('MONTH', event_ts)       -- returns timestamp: '2024-08-01 00:00:00'
```

`date_part` = extracts a numeric component. `date_trunc` = truncates to start of unit.

### LIKE ANY — Multi-Pattern (Q38 — Spark 3.3+)

```sql
event_name LIKE ANY ('click_%', 'tap_%', 'swipe_%')
-- Returns true if any pattern matches
-- LIKE ALL: requires all patterns to match
-- ILIKE ANY: case-insensitive multi-pattern
```

### second(ts) Returns Double (Q39)

```sql
second(TIMESTAMP '2024-08-15 14:30:45.123456')  -- returns 45.123456 as DoubleType
-- Includes fractional seconds for TIMESTAMP input
-- Returns 0.0 for DateType (no time component)
```

### to_number vs try_to_number (Q40 — Spark 3.3+)

| Function | On format mismatch |
|---|---|
| `to_number(str, format)` | **Raises** `SparkNumberFormatException` |
| `try_to_number(str, format)` | **Returns** `null` |

```sql
to_number('$1,234.56', '$9,999.99')   -- returns DECIMAL
try_to_number('invalid', '$9,999.99') -- returns null safely
```

---

## Topic 3: DataFrame/Dataset API (Q41–Q70)

### withMetadata (Q41 = **A**)

```python
df2 = df.withMetadata("score", {"description": "normalized", "unit": "percent"})
# Data is unchanged; metadata attached to StructField
df2.schema["score"].metadata  # retrieves the dict
```

Answer is **A**: `df2.schema["score"].metadata` returns the metadata, column data unchanged.

### Bitwise NOT as Logical NOT (Q42)

```python
df.filter(~F.col("is_deleted"))
# ~ calls Column.__invert__() → equivalent to NOT is_deleted
# Keeps rows where is_deleted=false
# Rows where is_deleted=null evaluate to null → excluded by filter
```

### array_sort with Custom Comparator (Q43)

```python
# Descending sort: return 1 when l < r (l should come after r)
F.array_sort(F.col("scores"), lambda l, r:
    F.when(l < r, F.lit(1)).when(l > r, F.lit(-1)).otherwise(F.lit(0)))

# Default ascending with nulls last:
F.array_sort(F.col("scores"))

# Also valid (sort_array):
F.sort_array(F.col("scores"), asc=False)
```

### F.window_time() for Watermark (Q44 — Spark 3.4+)

```python
F.window_time(F.col("window"))
# Extracts the window end timestamp for use with withWatermark()
# F.col("window.end") works for display but NOT for watermark integration
```

### collect_list over Ordered Window (Q45 = **A**)

```python
w = Window.partitionBy("user_id").orderBy("event_time")
# Default frame: RANGE BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
# For the 3rd row (purchase):
F.collect_list("event").over(w)  # → ['login', 'click', 'purchase']
```

Answer is **A**: running list up to and including the current row.

### withWatermark on Batch = No-op (Q46)

`df.withWatermark("event_time", "10 minutes")` on a batch DataFrame is silently ignored. No error, no data filtering. Allows same code for batch and streaming.

### df.observe() in Streaming (Q47)

```python
df.observe("my_metrics", F.count("*").alias("row_count"), F.sum("amount").alias("total"))
# Metrics are collected per micro-batch
# Accessible via: progress.observedMetrics["my_metrics"] in StreamingQueryListener
# Also: query.recentProgress
```

### F.rint() — Banker's Rounding (Q48)

```python
F.rint(F.col("value"))
# Returns DoubleType (NOT IntegerType)
# Uses IEEE 754 round-half-even (banker's rounding):
#   2.5 → 2.0 (rounds to even)
#   3.5 → 4.0 (rounds to even)
# For integer output: F.round(col, 0).cast("int")
```

### Global Temp Views (Q49)

```python
df.createOrReplaceGlobalTempView("user_events")
# Access:
spark.sql("SELECT * FROM global_temp.user_events")
# Lifetime: JVM lifetime (shared across all SparkSessions in same JVM)
# Regular temp view: session-scoped only
```

### approx_percentile vs approxQuantile Accuracy Direction (Q50)

| Function | Accuracy param | Direction |
|---|---|---|
| `F.approx_percentile(col, p, accuracy)` | `accuracy` (default: 10000) | **Higher = more accurate** |
| `df.stat.approxQuantile(col, probs, relErr)` | `relativeError` | **Lower = more accurate** (0.0 = exact) |

The two APIs define accuracy **inversely**. Don't confuse them.

### Dynamic vs Static Partition Overwrite (Q51)

```python
# Default (STATIC): deletes ALL partitions before writing
df.write.mode("overwrite").partitionBy("date").parquet("/data")  # DANGEROUS!

# Dynamic: only overwrites partitions present in new data
df.write.mode("overwrite") \
  .option("partitionOverwriteMode", "dynamic") \
  .partitionBy("date").parquet("/data")
# Or: spark.conf.set("spark.sql.sources.partitionOverwriteMode", "dynamic")
```

### F.nullif() — Replace Sentinel with null (Q52)

```python
F.nullif(F.col("status_code"), F.lit(-1))
# Returns null when status_code == -1, otherwise returns status_code
# Equivalent to: CASE WHEN expr1 = expr2 THEN NULL ELSE expr1 END
```

### mapInPandas vs applyInPandas (Q53)

| API | Requires groupBy? | Function signature |
|---|---|---|
| `df.mapInPandas(func, schema)` | **No** — partition-level | `Iterator[pd.DataFrame] → Iterator[pd.DataFrame]` |
| `groupBy().applyInPandas(func, schema)` | **Yes** | `pd.DataFrame → pd.DataFrame` per group |

Use `mapInPandas` for partition-level transformations without grouping.

### Schema Representation Methods (Q54)

| Method | Returns | Use for |
|---|---|---|
| `df.schema.json()` | Full JSON with nullable + metadata | Programmatic parsing |
| `df.schema.simpleString()` | Compact DDL string `"struct<id:int>"` | Quick inspection |
| `df.schema.treeString()` | Indented tree (same as `printSchema()`) | Human reading |

### F.xxhash64 vs F.hash (Q55)

| Function | Algorithm | Return type | Output size |
|---|---|---|---|
| `F.xxhash64(*cols)` | xxHash64 (Spark 3.0+) | `LongType` | 64-bit |
| `F.hash(*cols)` | MurmurHash3 | `IntegerType` | 32-bit |

xxHash64 has lower collision probability due to larger output space. Both are non-cryptographic.

### F.lit(None) Must Be Cast (Q56 = **A**)

```python
# WRONG — produces NullType column, rejected by Parquet/ORC:
df.withColumn("opt", F.lit(None))

# CORRECT — cast to specific type:
df.withColumn("opt", F.lit(None).cast("string"))
df.withColumn("opt", F.lit(None).cast(T.StringType()))
```

Answer is **A**: root cause is `NullType`; fix is casting.

### repartitionByRange vs repartition (Q57)

```python
df.repartitionByRange(n, col)
# Samples column to estimate quantiles → assigns rows to contiguous value ranges
# Partition 0 has lowest values, partition n-1 has highest

df.repartition(n, col)
# Hash-based → similar values may end up in different partitions
# No ordering guarantee
```

### regexp_extract_all — All Matches (Q58 — Spark 3.1+)

```python
F.regexp_extract_all(F.col("log_line"), pattern, 0)
# Returns ArrayType(StringType) with ALL non-overlapping matches
# idx=0: full match | idx>0: specific capture group
# regexp_extract(col, pattern, 1) only returns the FIRST match
```

### partitionBy + bucketBy Combination (Q59)

```python
df.write \
  .partitionBy("region") \          # partition pruning for region= filters
  .bucketBy(16, "order_id") \       # bucket-merge join elimination
  .sortBy("order_date") \           # efficient range scans within bucket
  .saveAsTable("orders")            # bucketBy REQUIRES saveAsTable
```

### saveAsTable Append Validates Schema (Q60)

`saveAsTable` with `mode("append")` adds data to the existing metastore table's location and **validates schema compatibility**. No schema changes occur. To change the schema: use `mode("overwrite")` with `option("overwriteSchema", "true")` for Delta.

### JDBC Custom Predicates (Q61)

```python
spark.read.jdbc(url, table, predicates=[
    "id < 1000",
    "id BETWEEN 1000 AND 4999",
    "id BETWEEN 5000 AND 9999",
    "id >= 10000"
], properties=props)
# Each predicate → one JDBC partition with custom WHERE clause
# Unlike lowerBound/upperBound: allows non-uniform, non-numeric splits
```

### applyInArrow — RecordBatch Format (Q62 — Spark 3.3+)

| API | Data format per group |
|---|---|
| `groupBy().applyInArrow(func, schema)` | `pyarrow.RecordBatch` (no Pandas conversion overhead) |
| `groupBy().applyInPandas(func, schema)` | `pandas.DataFrame` |

`applyInArrow` skips Arrow-to-Pandas conversion for better performance.

### F.raise_error() — Inline Data Validation (Q63 — Spark 3.1+)

```python
F.when(F.col("price") < 0, F.raise_error("Negative price detected")) \
 .otherwise(F.col("price"))
# Raises SparkRuntimeException when evaluated
# F.assert_true(condition, errMsg) is also valid
```

### binaryFile Format — 4 Columns (Q64)

```python
spark.read.format("binaryFile").load("/images/")
# Produces 4 columns:
# path (string), modificationTime (timestamp), length (long), content (binary)
# option("pathGlobFilter", "*.png") filters by filename pattern
```

### Delta overwriteSchema Option (Q65)

```python
df.write.format("delta").mode("overwrite") \
  .option("overwriteSchema", "true") \    # permits schema replacement
  .save("/delta/events")
# Without this: AnalysisException on schema mismatch
# mergeSchema=true: adds new columns without removing existing ones
```

### stat.cov vs stat.corr (Q66)

| Method | Returns | Range | Scale dependent? |
|---|---|---|---|
| `df.stat.cov("c1", "c2")` | Sample covariance (float) | Unbounded | Yes |
| `df.stat.corr("c1", "c2")` | Pearson correlation (float) | [-1, 1] | No |

Both are **eager actions** returning Python floats.

### Temp View Scope (Q67)

```python
# Session A:
df.createOrReplaceTempView("sales_staging")  # session-scoped only!

# Session B: CANNOT access sales_staging
# Use createOrReplaceGlobalTempView for cross-session sharing:
df.createOrReplaceGlobalTempView("sales_global")
spark.sql("SELECT * FROM global_temp.sales_global")  # accessible everywhere
```

### ORC Compression Option Key (Q68)

```python
# ORC uses native option key (NOT 'compression' like Parquet):
df.write.format("orc").option("orc.compress", "zlib")  # CORRECT
# Valid values: none, snappy, zlib (default), lzo

# Parquet (different key):
df.write.format("parquet").option("compression", "snappy")
```

### array_min/array_max Ignore Nulls (Q69)

```python
F.array_min(F.col("scores"))  # [3, null, 1, 5] → 1 (ignores null)
F.array_max(F.col("scores"))  # [3, null, 1, 5] → 5 (ignores null)
# Returns null only for empty array or all-null array
```

### df.offset(n) — Row Skipping (Q70 — Spark 3.4+)

```python
df.offset(100).limit(50)
# Equivalent to SQL: SELECT * FROM t LIMIT 50 OFFSET 100
# Skips first 100 rows, returns next 50
# Always combine with orderBy() for deterministic results
```

---

## Topic 4: Troubleshooting & Tuning (Q71–Q80)

### AQE: nonEmptyPartitionRatioForBroadcastJoin (Q71)

If the fraction of **non-empty post-shuffle partitions** falls below this threshold (default: **0.2 = 20%**), AQE may convert the join to a Broadcast Hash Join. With 85% empty partitions = 15% non-empty < 20% threshold → AQE switches to BHJ.

### storage.memoryMapThreshold (Q72)

`spark.storage.memoryMapThreshold` (default: 2 MB). Blocks **larger** than threshold → `mmap` (memory-mapped I/O). Blocks **smaller** than threshold → regular `read()` syscalls. `mmap` reduces JVM heap copies for large blocks but adds overhead for small ones.

### Parquet INT96 Timestamp Rebase (Q73)

`spark.sql.parquet.int96RebaseModeInWrite=LEGACY` rebases timestamps to the Julian calendar used by older Hive tools. Default `EXCEPTION` forces developers to choose explicitly to prevent silent data corruption.

### Case-Sensitive Column Resolution (Q74)

With default `spark.sql.caseSensitive=false`: having both `CustomerID` and `customerid` causes `AnalysisException` (ambiguous). Fix: `spark.sql.caseSensitive=true` enables case-sensitive matching so `df.select("customerid")` picks the lowercase column.

### ORC Native Implementation (Q75)

`spark.sql.orc.impl=native` (default since Spark **2.3**). Enables `spark.sql.orc.enableVectorizedReader=true` for columnar batch processing. Setting `impl=hive` reverts to Hive ORC library (no vectorized reads).

### rangeExchange.sampleSizePerPartition (Q76)

`spark.sql.execution.rangeExchange.sampleSizePerPartition` (default: **100**). Controls how many rows are sampled per partition for range boundary estimation in `repartitionByRange`. Increase to 1000+ for better accuracy with skewed distributions.

### AQE Plan Change Logging (Q77)

`spark.sql.planChangeLog.level=INFO` makes AQE plan transformation log entries visible in standard application logs. Default is `TRACE` (too verbose). Log entries include the rule name (e.g., `DynamicJoinSelection`) and before/after plan snippets.

### AQE forceApply (Q78)

`spark.sql.adaptive.forceApply=true` (default: false) forces AQE to process **all** queries, including those without shuffle or broadcast operations. Primarily used for testing/debugging. Adds overhead without practical benefit in production.

### Shuffle I/O Server Threads (Q79)

`spark.shuffle.io.serverThreads` (default: `max(3, numCores/4)`) controls Netty thread pool size for the shuffle data server. Increasing it allows more parallel connections and reduces `FetchFailedException` events when many executors fetch concurrently.

### Prometheus Metrics Endpoint (Q80)

`spark.ui.prometheus.enabled=true` exposes metrics at:
```
http://driver:4040/metrics/prometheus
```
Requires Prometheus sink configured in `metrics.properties`. Reports input/processed rows, latency, and other streaming metrics.

---

## Topic 5: Structured Streaming (Q81–Q90)

### queryName() — Naming Streaming Queries (Q81)

```python
q = df.writeStream.format("console").queryName("sensor_monitor").start()
# Find by iterating:
spark.streams.active  # list of all active queries
# Filter by name: [q for q in spark.streams.active if q.name == "sensor_monitor"]
# Names must be unique among concurrently active queries in the session
# For memory sink: query name becomes the queryable table name
```

### awaitAnyTermination (Q82)

```python
spark.streams.awaitAnyTermination()  # blocks until ANY query terminates
query.awaitTermination()             # blocks until THIS specific query terminates
spark.streams.active                 # property: list of all active StreamingQuery objects
```

### Shared Checkpoint = State Corruption (Q83 = **A**)

```python
# WRONG — both queries overwrite each other's checkpoint files:
spark.conf.set("spark.sql.streaming.checkpointLocation", "/checkpoints")

# CORRECT — each query gets its own path:
df1.writeStream.option("checkpointLocation", "/checkpoints/queryA").start()
df2.writeStream.option("checkpointLocation", "/checkpoints/queryB").start()
```

Answer is **A**: shared checkpoint root causes state corruption; each query needs its own unique path.

### StreamingQuery.exception() (Q84)

```python
query.awaitTermination(timeout=30)  # returns after timeout or query stop
if query.exception():               # None = still running or clean stop
    print(f"Failed: {query.exception()}")
```

### foreachBatch Idempotency with epochId (Q85 = **A**)

```python
def process_batch(df, epochId):
    # epochId is the same on retry of a failed micro-batch!
    # Must use epochId as deduplication key:
    df.write.format("delta").option("txnVersion", epochId) \
      .option("txnAppId", "my_app").mode("append").save(path)
    # Or: conditional upsert/MERGE keyed on epochId
```

Answer is **A**: use `epochId` as a transactional deduplication key; Spark does NOT guarantee exactly-once to `foreachBatch`.

### Append Mode + Aggregation + No Watermark (Q86)

```python
# This raises AnalysisException at planning time:
df.groupBy("category").agg(F.sum("amount")) \
  .writeStream.outputMode("append").start()

# Fix 1: add watermark
df.withWatermark("event_time", "1 hour") \
  .groupBy("category", F.window("event_time", "10 min")) \
  .agg(F.sum("amount")) \
  .writeStream.outputMode("append").start()

# Fix 2: change output mode
.writeStream.outputMode("complete").start()
```

### Streaming Metrics via Dropwizard (Q87)

`spark.sql.streaming.metricsEnabled=true` (default: **false**). Registers streaming metrics with Dropwizard `MetricRegistry`. Makes `inputRowsPerSecond`, `processedRowsPerSecond`, latency available to JMX, Prometheus, Graphite sinks.

### Stream-Stream Outer Join: Both Watermarks Required (Q88)

```python
# WRONG — only orders_stream has watermark:
orders_stream.withWatermark("order_time", "1 hour") \
  .join(payments_stream, on="order_id", how="left_outer")
# → AnalysisException: both streams need withWatermark()

# CORRECT:
orders_stream.withWatermark("order_time", "1 hour") \
  .join(
    payments_stream.withWatermark("pay_time", "1 hour"),
    on="order_id", how="left_outer")
```

Inner stream-stream joins: watermark not required but state grows unboundedly without it.

### writeStream.partitionBy() (Q89)

```python
df.writeStream.format("parquet") \
  .partitionBy("date", "hour") \
  .option("path", "/output").start()
# Produces: /output/date=2024-08-15/hour=10/part-*.parquet
# Each micro-batch appends new files under appropriate partition directory
# Enables partition pruning for downstream batch readers
```

### maxBytesPerTrigger (Q90)

```python
df.readStream.option("maxBytesPerTrigger", "100m")
# Limits total bytes read per micro-batch (~100 MB)
# More predictable than maxFilesPerTrigger when files vary in size
# maxBytesPerTrigger and maxFilesPerTrigger are MUTUALLY EXCLUSIVE
```

---

## Topic 6: Spark Connect (Q91–Q95)

### What is Spark Connect (Q91 — Spark 3.4+)

- **Architecture**: Decoupled client/server via **gRPC** (default port **15002**)
- **Data transfer**: Apache Arrow
- **Client installation**: `pip install pyspark[connect]` — no Java required
- **Connection**: `SparkSession.builder.remote("sc://cluster-host:15002").getOrCreate()`

### Client/Server Plan Execution (Q92)

| Location | What happens |
|---|---|
| Client | Builds unresolved logical plan using Spark Connect DSL |
| On action (e.g., `collect()`) | Plan serialized to **protobuf**, sent via gRPC |
| Server | Catalyst optimization + cluster execution |
| Return | Results streamed back as **Arrow batches** |

### SparkContext Not Available in Connect (Q93)

```python
# In Spark Connect session:
spark.sparkContext  # → PySparkNotImplementedError

# Migration:
sc.textFile("path")   → spark.read.text("path")
sc.parallelize(data)  → spark.createDataFrame(data, schema)
sc.addFile("path")    → use shared filesystem (HDFS/S3)
```

### pip install pyspark[connect] (Q94)

The `[connect]` extra adds `grpcio`, `grpcio-status`, and `googleapis-common-protos`. No JRE required on the client machine.

### Custom Relation Extension (Q95)

`spark.connect.extensions.relation.classes` registers server-side `RelationPlugin` implementations that interpret custom protobuf `Any` messages from clients and translate them into Spark logical plans.

---

## Topic 7: Pandas API on Spark (Q96–Q100)

### groupby().transform() — Group-Preserving (Q96)

```python
psdf.groupby("category")["amount"].transform(lambda s: s - s.mean())
# Returns Series of SAME LENGTH as input (group-preserving)
# Each value = amount - group_mean(amount)
# Unlike apply(): no reduction to one row per group
```

### spark.apply() — Escape Hatch (Q97)

```python
psdf.spark.apply(lambda sdf: sdf.repartitionByRange(10, "id"))
# sdf: pyspark.sql.DataFrame → must return pyspark.sql.DataFrame
# Result is automatically wrapped back as Pandas-on-Spark DataFrame
# Enables any native Spark API not in the Pandas API surface
```

### plot() Uses compute.max_rows (Q98)

```python
psdf.plot(kind="bar")  # internally calls toPandas() which is capped!
# ps.get_option("compute.max_rows")  → default: 1000
# Groups beyond limit silently dropped

# Fix:
ps.set_option("compute.max_rows", None)  # disable limit (use with caution)
```

### psdf.spark.schema — StructType Access (Q99)

```python
psdf.spark.schema  # returns pyspark.sql.types.StructType
# Equivalent to psdf.to_spark().schema
# Includes: ArrayType, MapType, StructType nesting, nullable flags, metadata
# psdf.dtypes → pandas-compatible type objects (less detail)
```

### MultiIndex Support and Limitations (Q100)

`ps.MultiIndex` is **partially supported**:
- ✅ Creation: `from_tuples`, `from_arrays`, `from_frame`
- ✅ Basic indexing and filtering
- ⚠️ `sortlevel()`, complex `reindex()` — not implemented or slow due to distributed execution constraints

---

## Hard Questions Summary (36 Total)

| Q# | Topic | Key Concept |
|---|---|---|
| Q3=**C** | Architecture | YARN total = heap(4G)+overhead(512M)+offHeap(1G) = **5.5 GB** |
| Q4=**C** | Architecture | 3 stages: groupByKey + join create two shuffle boundaries |
| Q5 | Architecture | Concurrent tasks = 8/2 = 4; spark.task.cpus for multi-threaded libs |
| Q7 | Architecture | heartbeatInterval **must be less than** networkTimeout |
| Q9 | Architecture | Kryo: 5-10× faster, 2-5× smaller; needs class registration |
| Q11 | Architecture | Rolling event logs prevent oversized History Server files |
| Q13 | Architecture | openCostInBytes groups small files into single partition |
| Q15=**A** | Architecture | shuffle.compress=output blocks; spill.compress=intermediate spill files |
| Q18 | Architecture | Off-heap: both execution AND storage use off-heap pool |
| Q26 | SQL | timestampadd: unit first, delta second, timestamp third (Spark 3.3+) |
| Q29 | SQL | map_contains_key vs map[key] IS NOT NULL for null-valued keys |
| Q31=**A** | SQL | reduce() with optional 4th finish argument |
| Q34 | SQL | ILIKE (Spark 3.3+) case-insensitive without lower() call |
| Q38 | SQL | LIKE ANY (pattern1, ...) multi-pattern matching (Spark 3.3+) |
| Q40 | SQL | to_number raises; try_to_number returns null on mismatch |
| Q44 | DataFrame | window_time() for watermark integration (Spark 3.4+) |
| Q47 | DataFrame | df.observe() → observedMetrics in StreamingQueryListener |
| Q50 | DataFrame | approx_percentile accuracy= higher→better; approxQuantile relError= lower→better |
| Q53 | DataFrame | mapInPandas: no groupBy needed; applyInPandas: requires groupBy |
| Q55 | DataFrame | xxhash64=LongType 64-bit; hash=IntegerType 32-bit |
| Q57 | DataFrame | repartitionByRange: range-based; repartition: hash-based |
| Q60 | DataFrame | saveAsTable append validates schema compatibility |
| Q62 | DataFrame | applyInArrow: RecordBatch (no Pandas overhead); Spark 3.3+ |
| Q65 | DataFrame | Delta overwriteSchema=true to replace schema on overwrite |
| Q68 | DataFrame | ORC uses orc.compress key (not 'compression'); Parquet uses 'compression' |
| Q70 | DataFrame | df.offset(n) skips first n rows; Spark 3.4+ |
| Q71 | Tuning | nonEmptyPartitionRatioForBroadcastJoin default=0.2 |
| Q73 | Tuning | parquet.int96RebaseModeInWrite=LEGACY for Julian calendar compat |
| Q75 | Tuning | orc.impl=native default since Spark 2.3; enables vectorized reads |
| Q77 | Tuning | planChangeLog.level=INFO to see AQE plan changes |
| Q79 | Tuning | shuffle.io.serverThreads to reduce FetchFailedException |
| Q83=**A** | Streaming | Shared checkpoint root = corruption; each query needs its own path |
| Q86 | Streaming | Append mode + aggregation + no watermark = AnalysisException |
| Q88 | Streaming | Stream-stream outer join: BOTH streams need withWatermark() |
| Q93 | Connect | sparkContext raises PySparkNotImplementedError in Connect |
| Q98 | Pandas API | plot() capped by compute.max_rows (default 1000) |

---

## Iteration Comparison Table

| Property | Iter 7 | Iter 8 | Iter 9 |
|---|---|---|---|
| Easy | 36 | 9 | 10 |
| Medium | 60 | 55 | 54 |
| Hard | 4 | 36 | 36 |
| B answers | 100 | 96 | 89 |
| A answers | 0 | 4 | 8 |
| C answers | 0 | 0 | **3** |
| Answer options used | 1 (B only) | 2 (B + A) | **3 (B + A + C)** |
| Biggest trap | All B | Q71=A (Troubleshooting) | Q1=C (first question!) |

---

## Common Traps in Iteration 9

| Trap | Wrong assumption | Correct answer |
|---|---|---|
| Q1 | "First question must be B" | Answer is **C** (SparkSession wraps SparkContext) |
| Q3 | "Only heap+overhead count for YARN" | Off-heap also added → **5.5 GB (C)** |
| Q4 | "groupByKey = 2 stages max" | join adds a 3rd → **3 stages (C)** |
| Q15 | "B is the default answer" | shuffle.compress vs spill.compress distinction → **A** |
| Q31 | "B about finish function" | Option A correctly states finish is optional 4th arg → **A** |
| Q33 | "B for make_interval syntax" | Option A shows correct syntax → **A** |
| Q41 | "B for withMetadata" | Option A correctly describes schema-level metadata → **A** |
| Q45 | "B for collect_list window" | Option A has the running list result → **A** |
| Q56 | "B for lit(None)" | Option A correctly explains NullType + fix → **A** |
| Q83 | "B for checkpoint" | Option A correctly states corruption and fix → **A** |
| Q85 | "C for foreachBatch exactly-once" | Option A correctly requires idempotency → **A** |
