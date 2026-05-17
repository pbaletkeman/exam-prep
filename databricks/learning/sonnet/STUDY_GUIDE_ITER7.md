# Study Guide — Databricks Certified Associate Developer for Apache Spark
## Iteration 7

---

## 🚨 CRITICAL EXAM ALERT — READ THIS FIRST 🚨

**ALL 100 ANSWERS IN ITERATION 7 ARE ANSWER B.**

This is not a typo. Every single question in this iteration has its correct answer as option B. Before selecting any answer, confirm your reasoning matches the B explanation — but statistically, if you are unsure, B is always correct here.

**Answer type: ALL 100 questions are `one` (single-select only)** — no multi-select, no "select all that apply".

---

## Exam Overview

| Property | Value |
|---|---|
| Iteration | 7 |
| Total Questions | 100 |
| Time Limit | 90 minutes |
| Pass Score | ≥ 70% (70 correct) |
| Answer Types | 100× `one` (single answer only) |
| Difficulty | 16 Easy / 80 Medium / 4 Hard |
| Hard Questions | Q8, Q33, Q65, Q80 |
| Correct Answer | **Always B** |

### Topic Weights

| Topic | Questions | % | Range |
|---|---|---|---|
| Apache Spark Architecture & Internals | 20 | 20% | Q1–Q20 |
| Spark SQL | 20 | 20% | Q21–Q40 |
| DataFrame / Dataset API | 30 | 30% | Q41–Q70 |
| Troubleshooting & Tuning | 10 | 10% | Q71–Q80 |
| Structured Streaming | 10 | 10% | Q81–Q90 |
| Spark Connect | 5 | 5% | Q91–Q95 |
| Pandas API on Spark | 5 | 5% | Q96–Q100 |

---

## Topic 1 — Apache Spark Architecture & Internals (Q1–Q20)

### Memory Architecture

**`spark.executor.memory`** = JVM heap for each executor (the Spark unified memory pool lives here).
**`spark.executor.memoryOverhead`** = off-heap container memory allocated by YARN/K8s **above** the JVM heap; covers Python/R workers, native libs, NIO direct buffers, OS overhead; **not** GC-managed; **not** part of the unified memory pool.
**`spark.driver.memoryOverhead`** = same concept for the driver container; default = `max(driverMemory × 0.10, 384 MB)`.

### Speculative Execution

`spark.speculation=true` launches a speculative copy when **both** conditions hold simultaneously:
1. Task runtime > `spark.speculation.multiplier` (default `1.5`) × median completed task time in the stage.
2. Fraction of completed tasks ≥ `spark.speculation.quantile` (default `0.75`).

Both conditions must be true — the quantile ensures a stable median exists before comparing.

### Task Failure & Job Abort

`spark.task.maxFailures` (default `4`) — number of times a **single task** can fail (across all executors) before the entire job aborts with `SparkException`. Operates at task level, not executor or stage level.

### Job Groups

`sc.setJobGroup(groupId, description, interruptOnCancel=False)` — tags all Spark jobs submitted from the current thread with `groupId`.
`sc.cancelJobGroup(groupId)` — cancels all running/queued jobs with that tag. Useful for "Cancel Query" buttons in interactive notebooks.

### Parallelism Configs

| Config | Governs | Default |
|---|---|---|
| `spark.default.parallelism` | RDD operations (`reduceByKey`, `join`, `parallelize`) | Cluster-dependent |
| `spark.sql.shuffle.partitions` | DataFrame/SQL post-shuffle partitions | 200 |

Changing `spark.default.parallelism` does **NOT** affect DataFrame shuffle partition counts.

### Network & Heartbeat

`spark.network.timeout` (default `120s`) — umbrella default for all Spark network interactions; if the driver receives no heartbeat from an executor within this window, the executor is declared lost.
`spark.executor.heartbeatInterval` (default `10s`) — must be **much smaller** than `spark.network.timeout` to avoid false evictions from a single GC-paused heartbeat.

Rule: `heartbeatInterval << network.timeout` (default ratio is 10s vs 120s = 12×).

### RPC Message Size

`spark.rpc.message.maxSize` (default `128 MB`) — if a broadcast object exceeds this limit, Spark raises `SparkException`. Increase via `spark.conf.set("spark.rpc.message.maxSize", "256")` (value is in megabytes).

### Shuffle Internals

**`BypassMergeSortShuffleWriter`** is selected when:
1. Reduce partitions ≤ `spark.shuffle.sort.bypassMergeThreshold` (default `200`), AND
2. No map-side aggregation (no combiner).

This path writes one file per reduce partition without sorting — avoids CPU cost of sorting but opens many file handles simultaneously. Only efficient for small partition counts.

**`spark.reducer.maxSizeInFlight`** (default `48 MB`) — max total bytes a single reducer can request simultaneously from all remote shuffle map outputs. Limits peak memory during shuffle read.

### Executor Exclusion

`spark.excludeOnFailure.enabled` (Spark 3.1+) — renamed from `spark.blacklist.enabled` (terminology change). Temporarily excludes executors/nodes that exceed per-executor failure thresholds. Both names recognized in Spark 3.1 for backward compatibility.

### Listener Bus

`spark.scheduler.listenerbus.eventqueue.capacity` (default `10000`) — bounded async queue decoupling scheduler from monitoring consumers. Log warning **"Dropped N SparkListenerEvent events"** = queue filled; monitoring data incomplete; increase capacity or optimize slow listeners.

### Web UI Ports

| Service | Default Port |
|---|---|
| Live application UI | 4040 (increments: 4041, 4042, …) |
| Spark History Server | 18080 |

Second app on same host → port 4041.

### Storage Levels

| Level | In-Memory Format | Disk Format | Notes |
|---|---|---|---|
| `MEMORY_AND_DISK` | Deserialized Java objects | Serialized | Default cache; high GC pressure |
| `MEMORY_AND_DISK_SER` | Serialized byte arrays | Serialized | Lower GC pressure; deserialization cost on read |
| `DISK_ONLY` | — | Serialized | No heap usage |
| `OFF_HEAP` | Off-heap native | — | Requires `spark.memory.offHeap.enabled=true` |

### Broadcast Variables

`sc.broadcast(value)` — driver serializes once; sends to each executor via block manager (torrent-style in cluster mode); **all tasks on the same executor share one deserialized copy**. O(executors) transfers instead of O(tasks).

### Standalone Worker Cleanup

`spark.worker.cleanup.enabled` (default `false`) — when `true`, worker daemons periodically delete working directories of finished applications. Controlled by `spark.worker.cleanup.interval` (default `1800s`) and `spark.worker.cleanup.appDataTtl` (default `7 days`). Standalone-mode only; no effect on YARN/Kubernetes.

### Deploy Modes

| Mode | Driver Location | Client After Submit |
|---|---|---|
| `client` | Submitting process | Must stay connected; logs appear locally |
| `cluster` | Cluster node | Exits after acceptance; driver logs on cluster |

### Dynamic Allocation

`spark.dynamicAllocation.executorIdleTimeout` (default `60s`) — idle executors are removed after this period. Executors with tracked shuffle data (when `shuffleTracking.enabled=false`) are **not** removed to preserve shuffle outputs.

---

## Topic 2 — Spark SQL (Q21–Q40)

### Date & Timestamp Functions

| Function | Return Type | Key Behavior |
|---|---|---|
| `timestampdiff(unit, ts1, ts2)` | `IntegerType` | Truncated (not rounded) complete units; Spark 3.3+ |
| `months_between(d1, d2)` | `DoubleType` | Fractional: day_diff ÷ 31; whole if both are month-end |
| `last_day(date)` | `DateType` | Last calendar day of the month; handles leap years |
| `next_day(date, dayName)` | `DateType` | First occurrence of dayName **after** the date (not same day) |
| `from_unixtime(epoch, fmt)` | `StringType` | Epoch → formatted string in session timezone; NOT TimestampType |
| `date_add(date, n)` | `DateType` | Adds n calendar days; rolls over month/year |
| `date_sub(date, n)` | `DateType` | Subtracts n calendar days |
| `to_timestamp(str, fmt)` | `TimestampType` | Returns NULL on parse failure (not exception); explicit fmt for non-ISO |
| `dayofweek(date)` | `IntegerType` | Java Calendar: Sunday=1, Monday=2, …, Saturday=7 |
| `date_trunc(unit, ts)` | `TimestampType` | Truncates timestamp; input must be TimestampType |
| `trunc(date, unit)` | `DateType` | Truncates date; input must be DateType |
| `unix_timestamp(str, fmt)` | `LongType` | String → epoch seconds in session timezone; inverse of `from_unixtime` |

**`dayofweek` convention trap**: Saturday = **7** (not 6). ISO conversion: `((dayofweek(col) + 5) % 7) + 1`.

**`next_day` trap**: if the date IS already the specified day, returns the NEXT occurrence (7 days later), not the same date.

**`timestampdiff` trap**: returns truncated integer, not a decimal. 4h 45m with unit `HOUR` → **4**.

### Cryptographic & Encoding Functions

| Function | Input Type | Output Type | Notes |
|---|---|---|---|
| `sha1(col)` | Any | `StringType` | 40-char lowercase hex (160-bit) |
| `sha2(col, bits)` | Any | `StringType` | 64-char hex for 256-bit; valid bits: 0(=256), 224, 256, 384, 512; invalid → NULL |
| `base64(col)` | `BinaryType` | `StringType` | Encode binary as Base64; to encode a string: `CAST(str AS BINARY)` first |
| `unbase64(col)` | `StringType` | `BinaryType` | Decode Base64 string to bytes |
| `hex(col)` | Int/Long/Binary | `StringType` | Uppercase hex string; no `0x` prefix |
| `unhex(col)` | `StringType` | `BinaryType` | Inverse of `hex` |

### Text & Array Functions

**`sentences(str)`** — returns `ArrayType(ArrayType(StringType))`: outer array = sentences, inner arrays = words. Splits at `.?!` boundaries then at word boundaries; punctuation excluded.

**`levenshtein(str1, str2)`** — returns `IntegerType` edit distance. `'kitten'→'sitting'` = 3. Spark 3.5+: optional `threshold` argument; returns `-1` if distance exceeds threshold.

### Array Indexing

| Function | Index Convention | Out-of-Bounds |
|---|---|---|
| `element_at(array, idx)` | 1-based positive; -1 = last | Returns NULL |
| `array[idx]` (DataFrame API) | 0-based | Returns NULL |
| Python list `[idx]` | 0-based | Raises IndexError |

**`slice(array, start, length)`** — 1-based `start`; returns `length` elements from `start`.

### Array Collection Functions

| Function | Behavior |
|---|---|
| `array_join(arr, delim)` | Skips NULL elements |
| `array_join(arr, delim, null_replacement)` | Substitutes NULL elements with replacement |
| `filter(arr, x -> pred)` | Keeps elements where pred = true; false/NULL excluded |
| `transform(arr, x -> expr)` | Maps each element; returns same-length array |
| `flatten(ArrayType(ArrayType(T)))` | Removes one nesting level → flat `ArrayType(T)` |
| `arrays_zip(*arrays)` | Produces `ArrayType(StructType)`; shorter arrays padded with NULL |

### Higher-Order Functions (HOFs)

`filter(array, lambda)`, `transform(array, lambda)`, `map_filter(map, lambda)` — all available as SQL functions and `F.filter()`, `F.transform()`, `F.map_filter()` in PySpark (Spark 3.1+/3.0+).

---

## Topic 3 — DataFrame / Dataset API (Q41–Q70)

### Set Operations

| Operation | Semantics | Duplicates |
|---|---|---|
| `df1.except(df2)` | SQL `EXCEPT DISTINCT` | Removes all occurrences of any df2 row from df1 |
| `df1.exceptAll(df2)` | SQL `EXCEPT ALL` | Each df2 occurrence removes exactly one df1 occurrence |
| `df1.intersect(df2)` | SQL `INTERSECT DISTINCT` | Returns distinct rows common to both |
| `df1.intersectAll(df2)` | SQL `INTERSECT ALL` | Returns `min(count_df1, count_df2)` copies of each common row |

### Column Renaming

`withColumnRenamed(old, new)` — single rename, adds one `Project` node to the logical plan.
`withColumnsRenamed({"old1": "new1", "old2": "new2"})` (Spark 3.4+) — batch rename in a single plan node; preferred for multiple renames.

### Key Transformations

`df.transform(func)` — calls `func(df)` and returns the result; enables left-to-right chaining: `df.transform(f1).transform(f2)` ≡ `f2(f1(df))`. No caching, no eager execution.

`F.greatest(*cols)` — row-wise maximum across multiple columns (horizontal).
`F.max(col)` — aggregate maximum across all rows in a group (vertical).

`F.coalesce(*cols)` — **column function**: first non-null value per row.
`df.coalesce(n)` — **DataFrame transformation**: reduce partition count (no shuffle).

`F.nanvl(col1, col2)` — returns `col1` if not NaN; `col2` if col1 is NaN; propagates NULL unchanged. Does NOT handle NULL. Combine with `F.coalesce` to handle both: `F.coalesce(F.nanvl(col, F.lit(0.0)), F.lit(0.0))`.

### Collection Functions

`F.collect_list(col)` — all values including duplicates and NULLs; non-deterministic order.
`F.collect_set(col)` — distinct values only; silently drops NULLs; non-deterministic order.

### Grouping & Aggregation

`rollup("a", "b")` produces n+1 grouping sets: `(a, b)`, `(a, NULL)`, `(NULL, NULL)`.
`cube("a", "b")` produces 2^n grouping sets: `(a, b)`, `(a, NULL)`, `(NULL, b)`, `(NULL, NULL)`.

`pivot(col, values)` — without explicit values: runs an extra job to discover distinct values (schema non-deterministic). **Always provide explicit values** in production.

### Struct & Complex Types

`F.struct(col("a"), col("b"))` → `StructType` column with fields `a` and `b`.
Access: `col("outer.inner")` or `col("outer").getField("inner")` — equivalent.
`F.array(*cols)` → fixed-length `ArrayType` column.
`F.create_map(k1, v1, k2, v2, ...)` → `MapType` column; alternating key-value expressions.
`F.map_keys(map_col)` → `ArrayType(KeyType)`.
`F.map_values(map_col)` → `ArrayType(ValueType)`.
`F.map_entries(map_col)` → `ArrayType(StructType[key, value])`.

### Explode Functions

| Function | NULL/Empty Behavior | Extra Columns |
|---|---|---|
| `F.explode(col)` | Drops rows with NULL/empty array | None |
| `F.explode_outer(col)` | Preserves rows (emits NULL element) | None |
| `F.posexplode(col)` | Drops NULL/empty | `pos` (0-based) + `col` |
| `F.posexplode_outer(col)` | Preserves rows | `pos` (0-based) + `col` |

`F.flatten(nested_arr)` — removes one nesting level.
`F.arrays_zip(*arrs)` — element-wise zip; shorter arrays padded with NULL.

### Window Functions

Default frame when `orderBy` is present (no explicit frame): `rangeBetween(UNBOUNDED_PRECEDING, CURRENT_ROW)`.
Default frame when NO `orderBy`: `rowsBetween(UNBOUNDED_PRECEDING, UNBOUNDED_FOLLOWING)`.

| Function | Ties | Gaps |
|---|---|---|
| `F.rank()` | Same rank for ties | Gaps after tie group |
| `F.dense_rank()` | Same rank for ties | No gaps |
| `F.row_number()` | Unique sequential | N/A |

`F.lag(col, n, default)` — `default` is returned when offset goes before partition start (not NULL).
`F.lead(col, n, default)` — `default` is returned when offset goes beyond partition end.

`F.ntile(n)` — assigns buckets 1–n as evenly as possible; extra rows go to earlier buckets. For 7 rows, n=4: `[1,1,2,2,3,3,4]`.

`rowsBetween` vs `rangeBetween`:
- `rowsBetween` = physical row offset (counts rows).
- `rangeBetween` = value offset on the ORDER BY column (includes all rows with the same value as the boundary).

### Sampling

`sampleBy("col", fractions={val: rate, ...}, seed)` — stratified sampling; labels absent from `fractions` are excluded entirely; approximate rates (not exact counts).

### Aggregation Functions

| Function | Description | Version |
|---|---|---|
| `F.approx_count_distinct(col, rsd)` | HyperLogLog++ estimate; default rsd=0.05 | All |
| `F.countDistinct(col)` | Exact deduplication via shuffle | All |
| `F.percentile_approx(col, q, accuracy)` | Greenwald-Khanna approximation | All |
| `F.count_if(condition)` | Counts rows where condition is true | Spark 3.3+ |

---

## Topic 4 — Troubleshooting & Tuning (Q71–Q80)

### Adaptive Query Execution (AQE)

Enabled by default in Spark 3.2+ (`spark.sql.adaptive.enabled=true`). Three core features:

1. **Dynamic partition coalescing** — merges small post-shuffle partitions toward `spark.sql.adaptive.advisoryPartitionSizeInBytes` (default `64 MB`).
2. **Dynamic join strategy switching** — converts sort-merge join → broadcast hash join when runtime side size falls below broadcast threshold.
3. **Dynamic skew join optimization** — splits skewed partitions (size > `skewedPartitionFactor × median` AND > `skewedPartitionThresholdInBytes`) and replicates the other side.

**`spark.sql.adaptive.localShuffleReader.enabled`** — after AQE converts SMJ → BHJ, allows executors to read only locally-written shuffle blocks from disk, eliminating cross-network transfers.

### Partitioning

`df.repartition(n)` — full shuffle; can increase or decrease; produces balanced partitions; supports `repartition(n, col)`.
`df.coalesce(n)` — narrow transformation (no shuffle); can only **decrease**; may produce uneven partitions; cheaper.

Use `repartition` to increase parallelism or balance skewed data. Use `coalesce` only to reduce before writes.

### Query Plan Analysis

`df.explain()` — Physical Plan only.
`df.explain(True)` or `df.explain(mode="extended")` — all four plans: Parsed Logical → Analyzed Logical → Optimized Logical → Physical.
`df.explain(mode="cost")` — Physical Plan + CBO statistics.

### External Shuffle Service

`spark.shuffle.service.enabled=true` — long-running node daemon serves shuffle files independently of executor lifecycle. Enables dynamic allocation without losing shuffle outputs when executors are removed.

### Compression Codecs

| Codec | Speed | Ratio | Notes |
|---|---|---|---|
| `lz4` (default) | Very fast | Moderate | `spark.io.compression.codec` default |
| `snappy` | Fast | Moderate | Popular alternative |
| `zstd` | Moderate | High | Preferred when network bandwidth is the bottleneck |
| `deflate` | Slow | High | Not the default |

`spark.sql.parquet.compression.codec` (default `snappy`) — separate setting for Parquet files.

### Caching

`df.cache()` = `df.persist(StorageLevel.MEMORY_AND_DISK)`. Deserialized Java objects in JVM heap; spills to disk when full. Always call `df.unpersist()` when data is no longer needed.

### Cost-Based Optimizer (CBO)

Two-step enablement:
1. `spark.sql.cbo.enabled=true` (default false in most distributions; enabled in Databricks Runtime).
2. `ANALYZE TABLE my_table COMPUTE STATISTICS` (+ optionally `FOR COLUMNS col1, col2` for histograms).

Without `ANALYZE`, CBO falls back to heuristics. Stale statistics require re-running `ANALYZE`.

---

## Topic 5 — Structured Streaming (Q81–Q90)

### Triggers

| Trigger | Behavior |
|---|---|
| `trigger(once=True)` | One micro-batch; processes all available data; then stops |
| `trigger(availableNow=True)` | Multiple micro-batches (respects `maxFilesPerTrigger`); then stops; Spark 3.3+ |
| `trigger(processingTime="30 seconds")` | Fixed interval; if batch takes 45s, next starts immediately after |
| `trigger(continuous="1 second")` | Low-latency continuous processing |

`availableNow` is the recommended replacement for `once` for large data volumes.

### Watermarks & Output Modes

`withWatermark("ts", "10 minutes")`:
- Watermark = `max(event_time) − 10 minutes`
- Events older than watermark = dropped
- State for past windows evicted
- With **Append** mode: window result emitted only after watermark passes window end

| Output Mode | State Retention | When to Use |
|---|---|---|
| Append | State evicted after watermark passes | Watermarked aggregations; immutable results |
| Complete | ALL state retained forever (unbounded) | Small bounded aggregations only |
| Update | Updated rows per trigger; no automatic eviction | When partial updates are acceptable |

### Checkpoint Contents

`option("checkpointLocation", "/path")` persists:
1. **`offsets/`** — source offsets per completed micro-batch.
2. **`commits/`** — confirmation a batch committed successfully.
3. **`state/`** — stateful operation snapshots (aggregations, joins, deduplication).

### Key Streaming APIs

`foreachBatch(func(micro_batch_df, batch_id))` — `micro_batch_df` is a static DataFrame; `batch_id` enables idempotent writes; used for sinks without native streaming support.

`dropDuplicates(["id"]).withWatermark(...)` — state store bounded by watermark; without watermark, state grows unboundedly.

`query.awaitTermination()` — blocks calling thread until query stops.
`query.stop()` — gracefully stops the query (finishes current micro-batch).
`query.recentProgress` — list of per-batch metric dicts: `batchId`, `numInputRows`, `inputRowsPerSecond`, `processedRowsPerSecond`, `durationMs`.
`query.lastProgress` — most recent batch dict.
`query.status` — current query state.

### Delta Lake Streaming Advantages

- Reads via transaction log (no directory listing overhead).
- Exactly-once semantics natively.
- Change Data Feed (`readChangeFeed=true`) for insert/update/delete streaming.
- `startingVersion` / `startingTimestamp` options.

---

## Topic 6 — Spark Connect (Q91–Q95)

### Architecture

Spark Connect (Spark 3.4+) — decoupled client-server over **gRPC** (default port `15002`):
- Driver runs as a separate **long-running server** process.
- Thin clients connect remotely; no local JVM in client process.
- Multi-language: Python, Scala, Go, R.
- Client crashes cannot bring down running jobs.

### Connection

```python
SparkSession.builder.remote("sc://hostname:15002").getOrCreate()
```

Requires `pyspark[connect]` extras. Uses `sc://` scheme (not `spark://` or `grpc://`).

### Unavailable in Client Mode

`SparkContext` and the **entire RDD API** are NOT available:
- `sc.parallelize`, `rdd.map`, `rdd.filter`, etc.
- `sc.broadcast()` (via SparkContext)
- `sc.addFile()`
- `sc.setJobGroup()` / `sc.cancelJobGroup()`
- Accumulators via SparkContext

Only the structured DataFrame/SQL/Dataset API is available.

### Data Transfer

Results transferred as **Apache Arrow RecordBatches** over gRPC. Arrow's columnar, zero-copy-friendly format minimizes serialization overhead and enables efficient Pandas interop.

### Server Lifecycle

Start: `./sbin/start-connect-server.sh --packages org.apache.spark:spark-connect_2.12:<version>`
Stop: `./sbin/stop-connect-server.sh`

The server is a long-running service — multiple concurrent clients, each with an isolated `SparkSession`. Unlike `spark-submit` apps which terminate when finished.

---

## Topic 7 — Pandas API on Spark (Q96–Q100)

### Reading Data

`ps.read_csv(path)` — **distributed** across Spark executors; scales with cluster; returns `pyspark.pandas.DataFrame`.
`pd.read_csv(path)` — **single-threaded** on driver; limited by driver memory; OOM risk for large files.

### Conversion APIs

`psdf.to_spark()` — returns underlying `pyspark.sql.DataFrame`; data stays on cluster; exposes native Spark APIs (window functions, streaming writes, etc.).
`spark_df.pandas_api()` (Spark 3.2+) — returns `pyspark.pandas.DataFrame`; data stays distributed; operations execute as Spark jobs.
`spark_df.toPandas()` — **collects ALL rows to driver memory**; OOM risk for large datasets.

### Merge Duplicate Handling

`ps.merge(left, right, on=key, how=type)` — **Pandas semantics**: conflicting non-join column names get `_x` / `_y` suffixes automatically.
`spark_df.join(other, on=key)` — keeps original names; ambiguous access raises `AnalysisException`.

### Safety Limit

`ps.set_option("compute.max_rows", 2000)` — raises `ValueError` when a collect-to-driver operation would exceed the limit.
Default: `1000`. Setting `None` disables entirely (OOM risk).
Read current: `ps.get_option("compute.max_rows")`.

---

## Key Traps & Common Wrong Answers Table

| Question | Trap | Correct Fact |
|---|---|---|
| Q1 | `memoryOverhead` = heap memory | It is OFF-heap container overhead (not JVM heap) |
| Q2 | Speculation fires on timeout alone | Both quantile AND multiplier conditions must hold simultaneously |
| Q3 | `task.maxFailures` = executor-level | It is individual TASK failure count |
| Q5 | The two parallelism configs are aliases | Completely separate: one for RDD, one for DataFrame/SQL |
| Q8 | BypassMerge = default sort behavior | Only when partitions ≤ threshold AND no map-side aggregation |
| Q21 | `timestampdiff` returns fractional hours | Returns truncated IntegerType |
| Q22 | `months_between` returns integer | Returns DoubleType with day_diff ÷ 31 fraction |
| Q23 | `last_day` returns day number | Returns full DateType value |
| Q24 | `next_day` returns same date if already that day | Always returns the NEXT future occurrence |
| Q25 | `from_unixtime` returns TimestampType | Returns StringType |
| Q28 | `dayofweek` Saturday = 6 | Saturday = 7 (Java Calendar: Sunday=1) |
| Q33 | `sentences()` returns flat array | Returns `ArrayType(ArrayType(StringType))` (nested) |
| Q35 | Negative index raises exception | Returns NULL for out-of-bounds; -1 = last element |
| Q40 | `hex` returns lowercase | Returns UPPERCASE hex string |
| Q41 | `except` and `exceptAll` are aliases | Completely different duplicate semantics |
| Q45 | `F.greatest` = aggregate max | Row-wise horizontal function, not an aggregate |
| Q46 | `F.coalesce` and `df.coalesce` are the same | Completely different: column null-handling vs partition reduction |
| Q47 | `nanvl` handles NULL | `nanvl` does NOT handle NULL; propagates NULL unchanged |
| Q49 | `rollup` = `cube` | rollup: n+1 sets; cube: 2^n sets |
| Q55 | `explode` preserves NULL/empty rows | `explode` DROPS them; use `explode_outer` to preserve |
| Q62 | `lag` returns NULL at partition boundary | Returns the `default` argument (third parameter) |
| Q63 | `row_number` gives equal rank to ties | Always unique sequential; `rank` gives equal rank with gaps |
| Q65 | `sum().over()` always = full partition sum | With `orderBy` + explicit `rowsBetween` frame = cumulative sum |
| Q66 | Default frame with `orderBy` = full partition | Default is `rangeBetween(UNBOUNDED_PRECEDING, CURRENT_ROW)` |
| Q79 | `df.cache()` default = MEMORY_ONLY | Default is MEMORY_AND_DISK |
| Q91 | Spark Connect = new cluster manager | It is a client-server gRPC API architecture |
| Q93 | RDD API works in Spark Connect | SparkContext and RDD API are NOT available |
| Q94 | Connect uses Java serialization | Uses Apache Arrow RecordBatches over gRPC |
| Q98 | `pandas_api()` = same as `toPandas()` | `pandas_api()` keeps data distributed; `toPandas()` collects to driver |
| Q99 | `spark.join` adds `_x`/`_y` suffixes | Spark raises AnalysisException; `ps.merge` adds suffixes |

---

## Hard Questions Summary (Q8, Q33, Q65, Q80)

### Q8 — BypassMergeSortShuffleWriter
Two conditions required simultaneously: reduce partitions ≤ `bypassMergeThreshold` (200) AND no map-side aggregation. This path writes one file per partition without sorting — avoids CPU cost but opens many file handles.

### Q33 — sentences()
`sentences("Hello world! How are you?")` returns `array(array("Hello","world"), array("How","are","you"))` — a 2-level nested structure. Not a flat array.

### Q65 — Cumulative Window Sum
`rowsBetween(Window.unboundedPreceding, Window.currentRow)` defines a growing frame from partition start to the current row — this produces a cumulative sum ordered by `hire_date` per `dept`.

### Q80 — Cost-Based Optimizer
Two-step process: `spark.sql.cbo.enabled=true` + `ANALYZE TABLE ... COMPUTE STATISTICS`. Without both steps, the CBO has no statistics and falls back to heuristics. Stale stats require re-running ANALYZE.

---

## Iteration 7 vs Prior Iterations

| Property | Iter 4 | Iter 5 | Iter 6 | **Iter 7** |
|---|---|---|---|---|
| Answer Types | one/many | one/many | one/many/all/none | **one only** |
| Multi-select questions | Some | Some | 9 | **0** |
| Correct answers | Mix A–D | Mix A–D | Mostly B | **ALL B** |
| Difficulty (Easy/Med/Hard) | Variable | Variable | 20/60/20 | **16/80/4** |
| Hard Qs | Multiple | Multiple | Multiple | **4 only** |

Iteration 7 is the simplest format — 100% single-answer, but the conceptual depth (especially Architecture and DataFrame API) is high.
