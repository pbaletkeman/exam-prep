# Databricks Certified Associate Developer for Apache Spark — Quick Reference (Iteration 7)

**Edition**: Iteration 7 (100 Questions)
**Last Updated**: 2026-05-17
**Format**: Fast lookup tables, formulas, memory anchors, and exam patterns

---

## Configuration Quick Reference

### Critical Executor Configuration

| Config | Default | Purpose | Key Insight |
|--------|---------|---------|-------------|
| `spark.executor.memory` | 1g | JVM heap size per executor | Request made by cluster manager |
| `spark.executor.memoryOverhead` | max(10%, 384 MB) | Off-heap container memory | Python/R process, NIO buffers, OS overhead |
| `spark.executor.memoryOverhead` + `spark.executor.memory` | N/A | **Total container request** | What YARN/K8s actually allocates |
| `spark.executor.heartbeatInterval` | 10s | Heartbeat send frequency | **Must be 10× less than `network.timeout`** |
| `spark.network.timeout` | 120s | Global network interaction timeout | Triggers executor loss if heartbeat not received |
| `spark.task.maxFailures` | 4 | Individual task failure limit | Reaches → **job aborts** |
| `spark.speculation` | false | Enable speculative task duplication | Threshold: `1.5× median duration` + `75% stage complete` |

### Shuffle & Partitioning

| Config | Default | Use | When to Tune |
|--------|---------|-----|--------------|
| `spark.sql.shuffle.partitions` | 200 | Post-shuffle partition count for DataFrames | Increase for large tables (>100 GB), decrease for small data |
| `spark.default.parallelism` | Varies | RDD operation partition count | Only affects RDDs; **not** DataFrames |
| `spark.shuffle.sort.bypassMergeThreshold` | 200 | Threshold for BypassMergeSortShuffleWriter | Lower reduces file handles open simultaneously |
| `spark.reducer.maxSizeInFlight` | 48 MB | Max concurrent remote shuffle bytes per reducer | Increase for bandwidth-rich networks; decrease for tight memory |
| `spark.io.compression.codec` | lz4 | Shuffle compression algorithm | Use `zstd` if network is bottleneck (higher compression) |

### Adaptive Query Execution (AQE)

| Config | Default | Purpose |
|--------|---------|---------|
| `spark.sql.adaptive.enabled` | true (Spark 3.2+) | Enable AQE dynamic optimizations |
| `spark.sql.adaptive.advisoryPartitionSizeInBytes` | 64 MB | Target size for dynamic partition coalescing |
| `spark.sql.adaptive.localShuffleReader.enabled` | true | Read locally-written shuffle blocks from disk |
| `spark.sql.adaptive.skewJoin.enabled` | true | Detect and optimize skewed joins |
| `spark.sql.adaptive.skewJoin.skewedPartitionFactor` | 5 | Multiplier to identify skew: `factor × median` |
| `spark.sql.adaptive.skewJoin.skewedPartitionThresholdInBytes` | 256 MB | Absolute threshold for skew detection |

### Caching & Storage

| Config | Default | Effect |
|--------|---------|--------|
| `spark.memory.offHeap.enabled` | false | Use off-heap memory for caching (requires manual management) |
| `spark.memory.offHeap.size` | 0 | Size of off-heap memory region (if enabled) |

---

## Function Reference Tables

### Date/Time Functions

| Function | Return Type | Example | Key Detail |
|----------|------------|---------|-----------|
| `timestampdiff(unit, ts1, ts2)` | IntegerType | `timestampdiff('HOUR', t1, t2)` | Truncates to complete units; 4.75 hours → 4 |
| `months_between(d1, d2)` | DoubleType | Result ≈ 2.16129 | Fractional = days ÷ 31 |
| `last_day(date)` | DateType | `'2026-02-28'` | Correctly handles leap years |
| `next_day(date, dow)` | DateType | `next_day('Sat', 'MON')` → Monday 2 days later | Returns date **after** input on specified weekday |
| `from_unixtime(sec, fmt)` | StringType | `from_unixtime(1745539200, 'yyyy-MM-dd')` | Interprets epoch in session timezone |
| `date_add(date, n)` | DateType | `date_add('2026-01-28', 5)` → `'2026-02-02'` | Rolls over month/year boundaries |
| `to_timestamp(str, fmt)` | TimestampType | `to_timestamp('25/04/2026', 'dd/MM/yyyy')` | Format required for non-ISO strings |
| `dayofweek(date)` | IntegerType | Saturday → `7` | Java Calendar: Sun=1, Sat=7 |
| `unix_timestamp(str, fmt)` | LongType | Current time as epoch seconds | Interprets in session timezone |

### String & Crypto Functions

| Function | Input/Output | Example | Note |
|----------|-------------|---------|------|
| `sha1(col)` | Any → StringType | 40-char lowercase hex | 160-bit (SHA-1) |
| `sha2(col, bits)` | Any → StringType | `sha2(col, 256)` → 64 chars | Bit-lengths: 0, 224, 256, 384, 512 |
| `base64(binary)` | BinaryType → StringType | Base64-encoded text | Encode string: `base64(CAST(str AS BINARY))` |
| `unbase64(str)` | StringType → BinaryType | Decoded bytes | Inverse of `base64` |
| `hex(int/long/binary)` | IntegerType, LongType, BinaryType → StringType | `hex(255)` → `'FF'` | Uppercase, no prefix |
| `unhex(str)` | StringType → BinaryType | `unhex('FF')` → byte(255) | Inverse of `hex` |
| `sentences(str)` | StringType → ArrayType(ArrayType(StringType)) | `[["Hello", "world"], ["How", "are"]]` | Tokenizes sentences then words; excludes punctuation |
| `levenshtein(str1, str2)` | StringType → IntegerType | Edit distance: `levenshtein('kitten', 'sitting')` → `3` | Spark 3.5+: accepts `threshold` arg |

### Array Operations

| Function | Return Type | Example | Indexing |
|----------|------------|---------|----------|
| `element_at(arr, idx)` | Element type | `element_at([10,20,30], -1)` → `30` | 1-based positive; negative for reverse; out-of-bounds → `NULL` |
| `slice(arr, start, len)` | ArrayType | `slice([10,20,30,40], 2, 2)` → `[20,30]` | 1-based start position |
| `array_join(arr, delim, nullRepl)` | StringType | `array_join(['a', NULL, 'c'], '-', 'N/A')` → `'a-N/A-c'` | Without nullRepl, NULLs skipped |
| `flatten(nested)` | ArrayType(T) | `flatten([[1,2], [3,4]])` → `[1,2,3,4]` | Removes one level of nesting |
| `arrays_zip(arr1, arr2)` | ArrayType(StructType) | Zips elements into structs | Shorter arrays padded with `NULL` |
| `filter(arr, func)` | ArrayType | `filter([1,2,3,4,5], x -> x > 3)` → `[4,5]` | Keeps where predicate is `true` |
| `transform(arr, func)` | ArrayType | `transform([1,2,3], x -> x*x)` → `[1,4,9]` | Maps every element |

### Map Operations

| Function | Return Type | Example | Notes |
|----------|------------|---------|-------|
| `create_map(key1, val1, ...)` | MapType(K, V) | Alternating key-value args | Creates map per row |
| `map_keys(map)` | ArrayType(KeyType) | Extracts all keys | Order non-deterministic |
| `map_values(map)` | ArrayType(ValueType) | Extracts all values | Consistent order with `map_keys` |
| `map_filter(map, func)` | MapType(K, V) | Keeps entries where `(k, v)` predicate true | Retains only matching entries |

---

## Window Function Reference

| Function | Behavior | Example | Frame Requirement |
|----------|----------|---------|-------------------|
| `F.lag(col, offset, default)` | Value from offset rows before | `lag(price, 2, 0.0)` | Requires `orderBy` |
| `F.lead(col, offset, default)` | Value from offset rows after | `lead(price, 1, 0.0)` | Requires `orderBy` |
| `F.rank()` | Rank with gaps after ties | `[1, 1, 3, 4]` for values `[10, 10, 20, 30]` | Requires `orderBy` |
| `F.dense_rank()` | Rank without gaps | `[1, 1, 2, 3]` for same values | Requires `orderBy` |
| `F.row_number()` | Unique sequential regardless of ties | `[1, 2, 3, 4]` for same values | Requires `orderBy` |
| `F.ntile(n)` | Divide into n buckets | `[1,1,2,2,3,3,4]` for 7 rows, n=4 | Requires `orderBy` |
| `F.sum(col).over(w)` | Cumulative sum (with `orderBy`) | Sums from partition start to current row | Default frame: `rangeBetween(UNBOUNDED_PRECEDING, CURRENT_ROW)` if `orderBy` present |

### Window Frame Semantics

| Frame Type | Boundary | Semantics |
|-----------|----------|-----------|
| `rowsBetween(UNBOUNDED_PRECEDING, CURRENT_ROW)` | Physical rows | Includes all rows from start through current by physical position |
| `rangeBetween(UNBOUNDED_PRECEDING, CURRENT_ROW)` | ORDER BY values | Includes all rows with ORDER BY value ≤ current row value |
| Default with `orderBy` | `rangeBetween(...)` | **Cumulative** (rows with same ORDER BY value included in same frame) |
| Default without `orderBy` | `rowsBetween(UNBOUNDED_PRECEDING, UNBOUNDED_FOLLOWING)` | **Full partition** |

---

## Streaming Configuration

| Config | Default | Purpose |
|--------|---------|---------|
| `spark.streaming.receiver.writeAheadLog.enabled` | false | WAL for driver recovery (deprecated for Structured Streaming) |

### Trigger Modes

| Trigger | Behavior | Stopping Condition |
|---------|----------|-------------------|
| `trigger(processingTime="30s")` | Start new batch every 30s (or immediately if previous batch took longer) | Runs indefinitely until `stop()` called |
| `trigger(once=True)` | Process all available data in **one** micro-batch | Stops after consuming all currently available data |
| `trigger(availableNow=True)` (Spark 3.3+) | Process all available data in **multiple** micro-batches respecting size limits | Stops after consuming all currently available data |
| `trigger(continuous="1s")` (experimental) | Continuous mode with 1-second epoch | Data processed with minimal latency |

### Output Modes for Aggregations

| Mode | Emit When | Use Case | Watermark Compatible |
|------|-----------|----------|----------------------|
| `Append` | After watermark passes window end | Immutable results, append-only sinks | Yes |
| `Update` | When aggregate changes | Real-time dashboards (row updates) | Partial (state not evicted) |
| `Complete` | Every trigger (entire result table) | Small, fully deterministic aggregations | No (unbounded state) |

---

## DataFrame API Patterns

### Set Operations

| Operation | Behavior |
|-----------|----------|
| `df1.except(df2)` | EXCEPT DISTINCT: all unique rows in df1 not in df2 |
| `df1.exceptAll(df2)` | EXCEPT ALL: each df2 row removes one df1 row |
| `df1.intersect(df2)` | INTERSECT DISTINCT: unique common rows |
| `df1.intersectAll(df2)` | INTERSECT ALL: multiplicity = min(count_df1, count_df2) |

### Grouping Patterns

| Operation | Grouping Sets Produced | Example Rows |
|-----------|----------------------|--------------|
| `groupBy('year', 'quarter')` | 1: (year, quarter) | Full detail |
| `rollup('year', 'quarter')` | 3: (yr, q), (yr, NULL), (NULL, NULL) | Detail + year subtotals + grand total |
| `cube('year', 'quarter')` | 4: (yr, q), (yr, NULL), (NULL, q), (NULL, NULL) | All subsets of dimensions |

### Join Strategy Indicators

| Condition | Default Join Type | AQE Might Switch To |
|-----------|-------------------|-------------------|
| One side < broadcast threshold (default 10 MB) | BroadcastHashJoin | BroadcastHashJoin (no change) |
| One side < broadcast threshold but initially planned as SMJ | SortMergeJoin | **BroadcastHashJoin** (AQE switch) |
| Both sides large, no skew | SortMergeJoin | SortMergeJoin |
| One side large but skewed | SortMergeJoin | **Skew-optimized join** (split + replicate) |

---

## Spark Connect & Pandas API Summary

| API | Available | Unavailable | Data Location |
|-----|-----------|------------|----------------|
| Spark Connect DataFrame/SQL | ✓ | RDD, SparkContext, accumulators, broadcast | Distributed on server; results streamed as Arrow |
| `pyspark.pandas` | ✓ Most operations | Full pandas ecosystem edge cases | Distributed (backed by Spark DataFrame) |
| `ps.read_csv()` | ✓ Distributed read | Single-machine limitations | Executor-distributed |
| `spark_df.pandas_api()` | ✓ Returns pandas-API wrapper | Raw RDD access | Distributed; operations execute as Spark jobs |
| `spark_df.toPandas()` | ✓ Collects to driver | Suitable only for small results | Driver memory (risk of OOM) |

---

## Memory Anchors by Topic

### Topic 1: Apache Spark Architecture & Internals
1. **`executor.memoryOverhead`** = off-heap container memory (Python, NIO, native libs); **not** part of JVM heap
2. **Speculation** triggers when task time > `1.5 × median` **AND** `75%` of stage is done
3. **`network.timeout` >> `heartbeatInterval`** (10:1 ratio) to prevent false evictions
4. **`spark.default.parallelism`** ≠ affects DataFrames; use `spark.sql.shuffle.partitions` instead
5. **RPC message size** limit: increase config if broadcast exceeds 128 MB
6. **BypassMergeSortShuffleWriter**: used when reduce partitions ≤ 200 AND no map-side aggregation
7. **ExcludeOnFailure**: tracks executor/node failures; `task.maxFailures` aborts job globally

### Topic 2: Spark SQL & Built-in Functions
1. **`timestampdiff`** returns `IntegerType` (truncated); 4.75 hours = 4
2. **`months_between`** = whole months + (days ÷ 31), returns `DoubleType`
3. **`next_day`** returns first date **after** input on specified weekday
4. **`from_unixtime`** → `StringType`; **`unix_timestamp`** → `LongType` (both interpret in session TZ)
5. **`dayofweek`** Java convention (Sun=1, Sat=7); **not** ISO (Mon=1)
6. **SHA functions** both return uppercase hex `StringType`: `sha1` = 40 chars, `sha2(256)` = 64 chars
7. **`sentences`** → nested arrays: tokenize at sentence then word boundaries

### Topic 3: DataFrame & DataSet API
1. **`except`** vs **`exceptAll`**: former removes all occurrences of any row; latter removes one-to-one
2. **`F.coalesce(*cols)`** (function) ≠ `df.coalesce(n)` (transformation)
3. **`F.greatest(*cols)`** = row-wise max (horizontal); `F.max()` = aggregate (vertical)
4. **`collect_list`** includes duplicates & NULLs; **`collect_set`** excludes both
5. **`rollup(a, b)`** → 3 grouping sets (detail, a subtotal, grand total)
6. **`explode`** drops NULL/empty; **`explode_outer`** preserves as NULL rows
7. **`F.struct`** & **`F.array`** create nested types; access with dot notation or `getField`

### Topic 4: Troubleshooting & Tuning
1. **AQE** three features: dynamic coalesce, join switch, skew optimization
2. **`repartition(n)`** = full shuffle, balances partitions; **`coalesce(n)`** = narrow, can only decrease
3. **`lz4`** = fast but moderate compression; **`zstd`** = high compression, higher CPU (choose when network is bottleneck)
4. **External shuffle service**: survives executor removal; critical for dynamic allocation
5. **Cost-based optimizer**: requires `ANALYZE TABLE` to collect statistics
6. **Default window frame** with `orderBy`: `rangeBetween(UNBOUNDED_PRECEDING, CURRENT_ROW)` = cumulative

### Topic 5: Structured Streaming
1. **Watermark** = `max(event_time) − threshold`; events older are dropped, state is evicted
2. **`trigger(availableNow=True)`** respects size limits; **`trigger(once=True)`** = one giant batch
3. **Append mode**: only suitable for watermarked aggregations; Complete requires infinite state
4. **`foreachBatch(func)`** enables custom sinks; `batch_id` enables idempotent writes
5. **Delta streaming**: uses transaction log (efficient), supports Change Data Feed (DML events)
6. **`awaitTermination()`** blocks; **`stop()`** actively stops (graceful current batch finish)

### Topic 6: Spark Connect
1. **Client-server over gRPC** (port 15002); thin client, no local JVM
2. **RDD API unavailable** in client mode (SparkContext, sc.parallelize, accumulators)
3. **Arrow serialization**: columnar, zero-copy, efficient Pandas interop
4. **Server lifecycle**: long-running service; clients are ephemeral
5. **Same DataFrame/SQL API**, just serialized over gRPC

### Topic 7: Pandas API on Spark
1. **`ps.read_csv`** = distributed; **`pd.read_csv`** = driver-only
2. **`to_spark()`** → native Spark DataFrame (enables window functions); **`pandas_api()`** → wrapped Spark (stays distributed)
3. **`toPandas()`** = **collect to driver** (OOM risk); use `pandas_api()` for large data
4. **`ps.merge()`** auto-adds `_x`/`_y` suffixes (Pandas semantics); **`spark_df.join()`** raises error on ambiguous columns
5. **`compute.max_rows`** = safety guard against accidental driver overload; default 1000

---

## 7-Day Accelerated Study Progression

| Day | Topics Covered | Focus |
|-----|----------------|-------|
| **Day 1** | Topic 1: Spark Architecture (Q1-Q20) | Memory, executors, failures, speculation, network |
| **Day 2** | Topic 2: Spark SQL (Q21-Q40) | Date functions, cryptography, arrays, maps, string processing |
| **Day 3** | Topic 3: DataFrame API - Part 1 (Q41-Q55) | Set ops, renaming, transforms, aggregates, collection ops |
| **Day 4** | Topic 3: DataFrame API - Part 2 (Q56-Q70) | Exploding, window functions, approximation algorithms |
| **Day 5** | Topic 4: Tuning (Q71-Q80), Topic 5: Streaming (Q81-Q85) | AQE, partitioning, compression, watermarking, triggers |
| **Day 6** | Topic 5: Streaming continued (Q86-Q90), Topic 6: Spark Connect (Q91-Q95) | Sinks, query lifecycle, client-server architecture |
| **Day 7** | Topic 7: Pandas API (Q96-Q100) | Distributed Pandas, conversions, safety limits |

---

## Exam Pattern Recognition

### High-Frequency Patterns

**Pattern 1: Configuration Relationships**
- `executor.memory + executor.memoryOverhead = container request`
- `heartbeatInterval << network.timeout`
- Always check if a config is about container allocation vs JVM heap vs behavior

**Pattern 2: Return Type Distinctions**
- `timestampdiff` → `IntegerType`; `months_between` → `DoubleType`
- `from_unixtime` → `StringType`; `unix_timestamp` → `LongType`
- Many functions return `NULL` on invalid input, not exceptions

**Pattern 3: Window Semantics**
- **Default frame with `orderBy`**: cumulative, not full partition
- **Without `orderBy`**: full partition frame
- Lag/lead require `orderBy`; `NULL` if out of bounds or use `default` arg

**Pattern 4: Pandas vs Spark DataFrame API**
- Pandas-on-Spark wraps Spark but **stays distributed**
- `.toPandas()` = **collect to driver** (OOM risk)
- `.pandas_api()` = wrapped Spark (distributed operations)

**Pattern 5: Streaming Output Modes**
- **Append** ✓ with watermark → emit after window closes
- **Complete** ✗ with watermark → requires unbounded state (impractical)
- **Update** ✓ but state not guaranteed evicted

---

## Exam Success Checklist

- [ ] Know the 3 AQE features by name and mechanism
- [ ] Distinguish `except` vs `exceptAll`, `intersect` vs `intersectAll`
- [ ] Recognize window frame default changes based on `orderBy` presence
- [ ] Understand executor.memoryOverhead ≠ JVM heap
- [ ] Know watermark = `max − threshold` and its effect on state
- [ ] RDD API unavailable in Spark Connect
- [ ] `toPandas()` collects; `pandas_api()` stays distributed
- [ ] `dayofweek` returns Java convention (Sun=1, Sat=7)
- [ ] `timestampdiff` truncates; `months_between` is fractional
- [ ] AQE local shuffle reader activates after join strategy switch
