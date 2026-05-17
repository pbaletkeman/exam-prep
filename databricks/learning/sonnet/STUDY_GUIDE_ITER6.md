# Databricks Spark Developer Exam — Study Guide (Iteration 6)

**Source**: `spark-databricks-iteration-6.md`
**Questions**: 100 | **Difficulty**: 20 Easy / 60 Medium / 20 Hard
**Answer Types**: 73 `one` / 20 `many` / **5 `all`** / **2 `none`** ← new types in Iter 6
**Pass Target**: ≥ 70 correct (70%)

---

## ⚠️ Iteration 6 Unique Features

1. **`all` type questions (5 total)** — ALL four options are correct. Q4 is confirmed `all`: A, B, C, D all correct for barrier execution mode. Must select every option to get credit.
2. **`none` type questions (2 total)** — NONE of the options A–D is the correct answer. Watch for "none of the above is correct" as an option, or for situations where all distractors are plausible but wrong.
3. **Very high B-answer rate in single-select questions** — statistically unusual. Do NOT default to B without verifying; it is a trap pattern.
4. **New Spark 3.4–3.5 functions heavily tested**: `try_add`, `try_divide`, `array_insert`, `try_element_at`, `F.to()`, `array_compact`, `F.median`.

---

## Topic 1: Apache Spark Architecture & Internals (Q1–Q20, 20%)

### 1.1 Storage Levels & Caching

| Abstraction | `.cache()` Default StorageLevel |
|-------------|--------------------------------|
| `RDD` | `MEMORY_ONLY` |
| `DataFrame` / `Dataset` | `MEMORY_AND_DISK` |

- `spark.rdd.compress=true` (default `false`): compresses serialized cached RDD partitions in memory; codec = `spark.io.compression.codec`; reduces cache footprint at cost of CPU
- `StorageLevel.OFF_HEAP` requires explicit specification; not applied automatically
- `spark.storage.replication.proactive` (default `false`): when `true`, Spark proactively replicates a lost cached block replica from a surviving executor — prevents cache miss + full recomputation; most beneficial with DRA + replication storage levels (`MEMORY_AND_DISK_2`, etc.)

### 1.2 Scheduling

**FIFO vs FAIR:**
- `FIFO` (default): first-queued job receives ALL executor slots before later jobs can start
- `FAIR`: distributes executor slots across all concurrently running jobs; short jobs make progress while long jobs execute

**Locality wait overrides:**
- `spark.locality.wait` (default `3s`): global default wait before downgrading locality
- `spark.locality.wait.process`, `spark.locality.wait.node`, `spark.locality.wait.rack`: independently override the global value per locality-level transition
- Setting `spark.locality.wait.node=10s` makes Spark wait 10 s before downgrading from `NODE_LOCAL` → `RACK_LOCAL`

### 1.3 DAGScheduler vs TaskScheduler

| Component | Responsibility |
|-----------|---------------|
| `DAGScheduler` | Splits RDD lineage into stages at shuffle boundaries; tracks stage dependencies; submits `TaskSet`s to `TaskScheduler` |
| `TaskScheduler` | Interfaces with cluster manager backend; assigns tasks to executors by data locality; retries failed tasks up to `spark.task.maxFailures`; reports completion back to `DAGScheduler` |

> **Wrong**: DAGScheduler handles executor restarts. **Wrong**: DAGScheduler runs on executors.

### 1.4 Barrier Execution Mode (Q4 — ALL answers correct)

All four facts are true:
- A) All tasks must start **simultaneously** — if insufficient slots, the stage waits
- B) Designed for **MPI-style workloads** (e.g., distributed deep learning training)
- C) `BarrierContext` provides `allGather()` coordination primitive
- D) Any task failure → **entire barrier stage resubmits** (not just the failed task)

### 1.5 Python Worker Memory

- `spark.executor.pyspark.memory`: off-heap memory budget for the **Python worker process** per executor (outside JVM heap)
- If unset: Python worker memory is unbounded by Spark — only by the OS → executor container may be killed by YARN or Kubernetes for exceeding declared memory limit
- Not the same as JVM heap; not the same as `spark.executor.memoryOverhead`

### 1.6 Dynamic Resource Allocation

- `spark.dynamicAllocation.shuffleTracking.enabled` (default `true` in Spark 3.0+): Spark tracks which executors hold shuffle data needed by downstream stages
- DRA may only remove executors whose shuffle data is no longer needed
- Makes the **external shuffle service optional** for DRA on YARN and Kubernetes

### 1.7 Event Log & History Server

- `spark.eventLog.compress=true`: compresses event log files written to `spark.eventLog.dir`
- Codec: `spark.eventLog.compression.codec` (default `zstd`)
- History Server decompresses transparently when rendering the Spark UI
- Not related to shuffle compression; not encryption

### 1.8 `coalesce()` Semantics (Q8 — many: A, B, D correct)

- A) ✅ Narrow transformation — no full shuffle
- B) ✅ If `n >= current count` → **no-op**; DataFrame retains original partition count
- C) ❌ Cannot increase partition count without shuffle — use `repartition(n)` for that
- D) ✅ `coalesce(1)` more efficient than `repartition(1)` for reducing to a single file (repartition forces full shuffle)

### 1.9 Arrow Batch Size for Pandas UDFs

- `spark.sql.execution.arrow.maxRecordsPerBatch` (default `10000`): max rows per Arrow record batch transferred between JVM executor and Python worker during Pandas UDF execution
- Smaller → less memory pressure, more serialization round trips
- Larger → higher throughput, higher peak memory per batch

### 1.10 Physical Join Strategy for Non-Equi Joins

- Non-equi join (`df1.value > df2.threshold`) has no equal-key → cannot use `SortMergeJoin` or `BroadcastHashJoin`
- Spark uses: **`BroadcastNestedLoopJoin`** (if one side broadcastable) or **`CartesianProduct` with filter**
- Spark does NOT raise AnalysisException; it does NOT auto-rewrite as equi-join

### 1.11 Deploy Modes

| Mode | spark-submit Lifecycle | Driver Location | Logs |
|------|----------------------|----------------|------|
| `--deploy-mode client` | Process IS the driver; runs until app completes | Client machine | Client machine |
| `--deploy-mode cluster` | Exits after acceptance | Cluster node | Cluster node |

### 1.12 `sc.parallelize()` Partition Count

- With `numSlices`: exactly `numSlices` partitions
- Without `numSlices`: uses `spark.default.parallelism` as default

### 1.13 `spark.driver.supervise`

- Restarts driver process on non-zero exit code (crash or failure)
- **Only effective** in `--deploy-mode cluster`; no effect in client mode
- **Supported**: Spark Standalone cluster mode
- **NOT supported**: YARN cluster mode, Kubernetes cluster mode

### 1.14 Two-Level Hash Map (Aggregation)

- `spark.sql.codegen.aggregate.map.twolevel.enabled` (default `true`)
- Level 1: compact, fixed-size, cache-friendly hash map (fast path)
- Level 2: full-sized overflow hash map (handles overflow from Level 1)
- Benefit: better CPU cache hit rates, reduced object allocation pressure
- Not related to whole-stage code generation

### 1.15 Worker Daemon vs Executor (Standalone Mode)

- **Worker daemon**: persistent JVM per cluster node; registers with Master; manages local resources; **launches Executor JVMs**
- **Executor**: separate JVM launched per application on a Worker node
- Multiple Executors from different applications can run under one Worker simultaneously
- Worker is NOT the executor; they are separate processes

### 1.16 `spark.rdd.compress`

- `spark.rdd.compress=true` (default `false`): compresses **serialized cached RDD partitions in memory**
- Codec: `spark.io.compression.codec`
- Reduces cache memory footprint at cost of CPU (compress on write, decompress on read)
- Not shuffle compression; not lineage metadata compression

### 1.17 Stage Re-computation After Executor Loss Post Shuffle Write

**Scenario**: executor lost after completing shuffle map output writes, before reduce tasks read them.
- Shuffle files on lost executor's **local disk** → inaccessible
- Spark must **re-run map tasks** on surviving executors to regenerate shuffle data
- **Exception**: if an external shuffle service was deployed and held the files → no recomputation required
- Spark does NOT fetch from driver; does NOT abort the application

### 1.18 `spark.app.name` and Application ID (Q20 — many: A, B, C correct)

- A) ✅ `spark.app.name` is human-readable; visible in Spark UI, History Server, cluster UI
- B) ✅ Application ID is system-generated by cluster manager; accessible via `spark.sparkContext.applicationId`
- C) ✅ YARN format: `application_<rm-start-timestamp>_<sequence-number>`
- D) ❌ Two apps with same `spark.app.name` do **NOT** share an Application ID

---

## Topic 2: Spark SQL (Q21–Q40, 20%)

### 2.1 `split_part()` (Spark 3.3+)

- `split_part(str, delimiter, pos)`: splits by delimiter, returns token at **1-based** position
- `split_part('a:b:c:d', ':', 2)` → `'b'`
- Returns the substring at position, not an array, not a range

### 2.2 Safe Arithmetic (Spark 3.4+)

| Function | Unsafe behavior | Safe behavior |
|----------|----------------|---------------|
| `try_divide(10, 0)` | `ArithmeticException` | Returns `NULL` |
| `try_add(MAX_INT, 1)` | Overflow wrap / exception | Returns `NULL` |
| `try_subtract(MIN_INT, 1)` | Overflow / exception | Returns `NULL` |
| `try_multiply(MAX_INT, 2)` | Overflow / exception | Returns `NULL` |

### 2.3 `any_value()` (Spark 3.3+)

- `any_value(col IGNORE NULLS)`: returns an **arbitrary non-null** value from the group (no ordering guarantee)
- `IGNORE NULLS`: skips NULLs; returns `NULL` only if **every** group value is NULL
- Not `mode()`, not `first()`, not deterministic

### 2.4 `make_date()` / `make_timestamp()`

| Function | Returns | On NULL/out-of-range |
|----------|---------|---------------------|
| `make_date(y, m, d)` | `DateType` | Returns `NULL` |
| `make_timestamp(y, m, d, h, min, sec)` | `TimestampType` | Returns `NULL` |

- `make_date(2026, 12, 25)` → `DateType` (not StringType, not TimestampType)

### 2.5 `regexp_like()` vs `regexp_extract()`

| Function | Returns | On no match |
|----------|---------|------------|
| `regexp_like(str, pattern)` | `BooleanType` | `false` |
| `regexp_extract(str, pattern, idx)` | `StringType` | Empty string `''` |

- NOT aliases; NOT different regex flavors; NOT SQL-only vs API-only

### 2.6 `width_bucket()`

- `width_bucket(value, min, max, num_buckets)`: returns **1-based** integer bucket number
- `value < min` → returns `0`
- `value >= max` → returns `num_buckets + 1`
- Not a window function; no `OVER` clause needed

### 2.7 `bool_and()` / `bool_or()` NULL Handling

- Both **ignore NULLs** (same convention as `sum`, `avg`)
- `bool_and`: `true` only if every non-null value is `true`
- `bool_or`: `true` if at least one non-null value is `true`
- Both return `NULL` only when **all** values in the group are `NULL`

### 2.8 `bit_or()` Aggregate

- `bit_or([5, 3, 8])`: `0101 | 0011 | 1000 = 1111` = **15**
- Not max, not sum, not count of most-bits

### 2.9 `array_compact()` (Spark 3.4+)

- `array_compact(array(1, NULL, 2, NULL, 3))` → `array(1, 2, 3)`
- Removes **all NULL elements**, preserves order of non-null elements
- Does NOT sort; does NOT move NULLs; does NOT raise error

### 2.10 `startswith()` / `endswith()` (Spark 3.3+)

- Returns `BooleanType` — `true` if match, `false` otherwise
- Returns `NULL` if either argument is `NULL`
- Not `IntegerType`; not `StringType`

### 2.11 `inline()` Table-Generating Function

- `inline(array_of_structs)`: explodes `ArrayType(StructType)` → one row per element, each struct field becomes a **separate output column**
- Can be used directly in `SELECT` without `LATERAL VIEW`
- `SELECT inline(array(struct(1,'a'), struct(2,'b')))` → 2 rows with struct fields unpacked

### 2.12 `named_struct()` vs `struct()`

- `named_struct('x', col1, 'y', col2)`: custom field names `x`, `y`
- `struct(col1, col2)`: field names come from input column names
- NOT aliases; NOT MapType vs StructType

### 2.13 `from_csv()` (Spark 3.0+)

- `from_csv(col, 'a INT, b STRING')`: parses CSV string → `StructType`
- **Flat only** — no nested objects or arrays (CSV is inherently flat)
- `from_json` supports nesting; `from_csv` does not

### 2.14 `schema_of_csv()` (Spark 3.0+)

- `schema_of_csv('"hello",42,true')` → `StringType` value like `'_c0 STRING, _c1 INT, _c2 BOOLEAN'`
- Returns a **DDL string**, not a `StructType` object
- Can be passed directly to `from_csv()`

### 2.15 `cardinality()` vs `size()` NULL Handling

| Function | Input = NULL | Behavior |
|----------|-------------|----------|
| `cardinality(col)` | `NULL` | Returns `NULL` (SQL-standard) |
| `size(col)` | `NULL` | Returns `-1` (legacy; controlled by `spark.sql.legacy.sizeOfNull`) |

### 2.16 `unix_date()` / `date_from_unix_date()` (Spark 3.1+)

- `unix_date(date_col)`: returns **`IntegerType`** count of **days** since `1970-01-01` (NOT seconds)
- `date_from_unix_date(n)`: returns `DateType` for the date N days after epoch; **inverse** of `unix_date`
- Not `unix_timestamp()` which returns seconds as `LongType`

### 2.17 `regexp_count()` (Spark 3.4+)

- Returns count of **non-overlapping occurrences** of pattern in string
- `regexp_count('abcabc', 'a.c')` → `2` (matches `'abc'` twice)
- Not 0/1 like `regexp_like`; not `regexp_extract_all` size

### 2.18 ANSI Mode

- `spark.sql.ansi.enabled=true`
- `CAST('abc' AS INT)` → raises **`SparkNumberFormatException`** (NOT returns NULL)
- Non-ANSI mode (default): invalid CAST silently returns `NULL`

---

## Topic 3: DataFrame/DataSet API (Q41–Q70, 30%)

### 3.1 Stratified Sampling — `df.sampleBy()`

- `df.sampleBy("status", fractions={"active": 0.5, "inactive": 0.1}, seed=42)`
- Independently samples the specified fraction per value in the key column
- Rows whose key value is **NOT in the fractions dict are excluded** from the result

### 3.2 Checkpointing

| Mode | Behavior |
|------|----------|
| `df.checkpoint(eager=True)` | Immediately triggers action; materialises + writes to checkpoint dir; returns DataFrame backed by checkpoint |
| `df.checkpoint(eager=False)` | Defers checkpointing until next action is called on the returned DataFrame |

### 3.3 `F.product()` (Spark 3.2+)

- `df.groupBy("category").agg(F.product("price"))`: computes multiplication of all non-null values per group
- NULL values ignored (same convention as `sum()`, `avg()`)
- Not mean; not Cartesian product

### 3.4 `df.to(target_schema)` (Spark 3.4+)

- Matches columns **by name** (not position)
- **Automatically casts** types to match target schema
- Raises `AnalysisException` if a column in `target_schema` is missing from `df`
- `df.select()` does NOT auto-cast types

### 3.5 `F.transform_keys()` (Spark 3.1+)

- `F.transform_keys("scores", lambda k, v: F.upper(k))` on `{"math": 90, "science": 85}`
- Result: `{"MATH": 90, "SCIENCE": 85}` — transforms keys, keeps values unchanged
- Lambda CAN accept Spark Column expressions like `F.upper(k)`

### 3.6 `F.transform_values()` (Spark 3.1+)

- `F.transform_values("inventory", lambda k, v: v * 2)` on `{"apples": 5, "bananas": 3}`
- Result: `{"apples": 10, "bananas": 6}` — transforms values, keeps keys unchanged
- Returns MapType (not ArrayType)

### 3.7 Struct Field Operations (Spark 3.1+)

| Method | Syntax | Effect |
|--------|--------|--------|
| `Column.withField(name, col)` | `df["address"].withField("country", F.lit("US"))` | Adds or replaces a named struct field; no full reconstruction needed |
| `Column.dropFields(*names)` | `df["profile"].dropFields("ssn")` | Removes named fields from struct |

- NOT `DataFrame.withField()` or `DataFrame.drop("struct.field")` with dot notation

### 3.8 `df.tail(n)` (Spark 3.0+)

- Returns the **last** `n` rows as a Python list of `Row` objects
- `df.limit(5).collect()` returns the **first** 5 rows
- They retrieve from **opposite ends** of the DataFrame

### 3.9 `F.array_insert()` (Spark 3.4+)

- `F.array_insert(arr, pos, value)`: inserts at **1-based position**, shifting elements right
- `array_insert(["a","b","c"], 2, "new")` → `["a", "new", "b", "c"]`
- Position 2 inserts BEFORE the current element at position 2

### 3.10 `F.aggregate()` HOF (Spark 3.1+)

- `F.aggregate(col, zero, merge_func)`: fold over array elements
- `F.aggregate(F.col("nums"), F.lit(0), lambda acc, x: acc + x)` for `[1,2,3,4]` → `10`
- 4th argument (`finish_func`) is optional

### 3.11 `F.zip_with()` HOF (Spark 3.1+)

- `F.zip_with(arr1, arr2, lambda x, y: x + y)` for `[10,20,30]` and `[1,2,3]`
- Result: `[11, 22, 33]` — element-wise merge

### 3.12 `F.forall()` / `F.exists()` HOF (Spark 3.1+)

- `F.forall(arr, pred)`: `true` **only if ALL** elements satisfy predicate
- `F.forall(F.col("scores"), lambda x: x >= 60)` for `[72, 85, 55, 90]` → `false` (55 < 60)
- `F.exists(arr, pred)`: `true` if **at least one** element satisfies predicate

### 3.13 `F.flatten()`

- `F.flatten(col)` on `[[1,2],[3,4],[5]]` → `[1, 2, 3, 4, 5]`
- Concatenates all inner arrays; `ArrayType(ArrayType(...))` → `ArrayType(...)`

### 3.14 `df.writeTo()` v2 DataSource API

| Method | Behavior |
|--------|----------|
| `.createOrReplace()` | Creates table if not exists; atomically drops + recreates if exists; **replaces all data** |
| `.append()` | Creates table if not exists; **adds rows** without removing prior data |

### 3.15 `F.try_element_at()` (Spark 3.4+)

- Returns `NULL` when 1-based index is out of range (array) or key absent (map)
- `F.element_at()` throws exception on out-of-bounds; `F.try_element_at()` returns NULL
- Clamps to last element? No — returns NULL

### 3.16 `F.array_remove()` vs `F.array_distinct()`

| Function | Removes |
|----------|---------|
| `array_remove(col, value)` | All occurrences of the specific `value` |
| `array_distinct(col)` | Duplicate elements; keeps **first occurrence** of each distinct value |

### 3.17 `F.date_diff` vs `F.datediff` (Spark 3.5+)

- Both return `IntegerType` count of days from `start` to `end`
- `F.date_diff` (snake_case): Spark 3.5+ new name
- `F.datediff` (camelCase): older alias
- **Functionally identical**

### 3.18 `df.crossJoin()`

- Cartesian product: `df1.count() × df2.count()` rows
- Requires `spark.sql.crossJoin.enabled=true` to guard against unintentional use
- Not an inner join; not an outer join; not a union

### 3.19 `write.partitionBy()` Behavior (Q60 — many: A, B, C correct)

- A) ✅ Creates `year=val/month=val/` directory hierarchy
- B) ✅ Partition columns are **excluded** from data files (values encoded in directory name)
- C) ✅ Files per leaf dir = number of DataFrame partitions containing that key combination
- D) ❌ Does NOT auto-coalesce to one file per partition key

### 3.20 `write.bucketBy()`

- **Only** works with `saveAsTable` (bucketing metadata stored in Hive/Spark metastore)
- NOT compatible with `save(path)` or `format(...).save(path)`
- `sortBy` is optional; adds sort within each bucket file (not global sort)

### 3.21 `current_timestamp()` / `current_date()` Evaluation

- Non-deterministic; evaluated at **start of each query execution**
- All rows within a single execution share the **same** timestamp
- Two `show()` calls on the same DataFrame reference may produce different timestamps

### 3.22 Parquet Compression Codecs

- **Valid**: `snappy`, `gzip`, `brotli`, `lz4`, `zstd`, `uncompressed`
- **INVALID**: `deflate` (Q65 trap — deflate is NOT a valid Parquet codec in Spark)

### 3.23 `F.map_zip_with()` HOF (Spark 3.1+)

- `F.map_zip_with(map1, map2, lambda k, v1, v2: v1 - v2)`
- For `prices={"apple": 1.5, "banana": 0.8}` and `discounts={"apple": 0.1, "banana": 0.05}`
- Result: `{"apple": 1.4, "banana": 0.75}` — merges by key, applies function per key

### 3.24 `df.inputFiles()`

- Returns Python list of **absolute paths** of all input files contributing to the DataFrame
- Not a DataFrame; not a dict; not available only for RDDs

### 3.25 `F.median()` vs `F.percentile_approx()` (Spark 3.4+)

| Function | Type | Algorithm |
|----------|------|-----------|
| `F.median(col)` | Approximate | Greenwald-Khanna sketch (same as percentile_approx) |
| `F.percentile_approx(col, 0.5)` | Approximate | Greenwald-Khanna sketch |
| `percentile(col, 0.5)` SQL only | Exact | Sort-based |

- `F.median` is shorthand for `F.percentile_approx(col, 0.5)` — not exact

### 3.26 `df.observe()` (Spark 3.3+) (Q69 — many: A, B, D correct)

- A) ✅ Attaches aggregate expressions; metrics computed during the action; no separate query needed
- B) ✅ `Observation.get` (or `.wait()`) blocks until action completes; returns metrics as Python dict
- C) ❌ Works with **batch DataFrames** too (not streaming-only)
- D) ✅ Multiple `observe()` calls can be chained for different metrics in one pass

### 3.27 ANSI Mode CAST (Q70 — answer C)

- `spark.sql.ansi.enabled=true` + `SELECT CAST('abc' AS INT)` → raises `SparkNumberFormatException`
- Default non-ANSI: invalid CAST silently returns `NULL`
- ANSI does NOT return `NULL`; does NOT return `0`; error is at **runtime** (not query-planning time)

### 3.28 `F.overlay()` String Replacement (Spark 3.0+)

- `F.overlay(input, replace, pos, len)`: replaces `len` characters starting at **1-based** `pos`
- `overlay('abcdef', 'XY', 3, 2)`: positions 3–4 (`'cd'`) replaced by `'XY'` → `'abXYef'`

### 3.29 `df.dtypes`

- Python list of `(column_name, type_string)` tuples
- Not a StructType; not a dict; not DataType objects

---

## Topic 4: Troubleshooting & Tuning (Q71–Q80, 10%)

### 4.1 AQE Skew Join (Q71)

- `spark.sql.adaptive.skewJoin.enabled` (default `true`)
- **Detects**: partitions exceeding `skewedPartitionThresholdInBytes` AND `skewedPartitionFactor × median`
- **Action**: splits skewed side into sub-partitions; replicates the matching non-skewed partition for each sub-partition pair
- Does NOT repartition entire dataset; does NOT convert to broadcast hash join automatically

### 4.2 Arrow `selfDestruct` for `toPandas()`

- `spark.sql.execution.arrow.pyspark.selfDestruct.enabled=true`
- Releases each JVM Arrow buffer **immediately** after copying into the pandas DataFrame
- Reduces **peak driver JVM heap** usage during `toPandas()`
- Not file deletion; not unpersist; not prevention of `to_spark()`

### 4.3 Whole-Stage Code Generation (Q73 — many: A, B, C correct)

- A) ✅ Fuses multiple operators within a stage into one compiled Java method; reduces virtual dispatch; enables JIT
- B) ✅ Auto-disabled when input/output fields exceed `spark.sql.codegen.maxFields` (default `100`)
- C) ✅ Disabling is a valid debugging technique for codegen errors — produces cleaner stack traces
- D) ❌ Does NOT replace Tungsten binary memory format

### 4.4 Input Partition Sizing

| Config | Default | Effect |
|--------|---------|--------|
| `spark.sql.files.maxPartitionBytes` | `128 MB` | Max data per input partition |
| `spark.sql.files.openCostInBytes` | `4 MB` | Virtual padding added per file to account for file-open overhead |

- `openCostInBytes` causes small files to be merged into the same partition when their total padded size stays under `maxPartitionBytes`
- They work together; they are NOT independent; `openCostInBytes` is NOT subtracted from `maxPartitionBytes`

### 4.5 AQE Partition Coalescing — `parallelismFirst`

- `spark.sql.adaptive.coalescePartitions.parallelismFirst` (default `true`)
- When `true`: targets `advisoryPartitionSizeInBytes`; **ignores** `minPartitionNum` (may produce few large partitions)
- When `false`: respects `minPartitionNum` as a lower bound on merged partition count (protects parallelism at expense of partition size target)

### 4.6 Missing Files

- `spark.sql.files.ignoreMissingFiles` (default `false`)
- `false` (default): raises `FileNotFoundException` when a file is missing at read time
- `true`: skips missing files; returns only successfully read data

### 4.7 Shuffle Write Buffer

- `spark.shuffle.file.buffer` (default `32k`): in-memory write buffer per shuffle output file stream
- Increasing: fewer syscalls → better write throughput; cost = more executor heap per write stream
- Controls the **write path** only (not the read/fetch path)

### 4.8 Off-Heap Memory (Q78 — many: A, B, D correct)

- A) ✅ Allocated outside JVM heap using `sun.misc.Unsafe`; not subject to GC → reduces GC pauses
- B) ✅ `spark.memory.offHeap.size` is per-executor; ADDITIONAL to `spark.executor.memory`; not in `--executor-memory`
- C) ❌ On-heap caching is NOT automatically disabled; must specify `StorageLevel.OFF_HEAP` explicitly
- D) ✅ Used by Tungsten for sort buffers, hash tables; and for cached data when `OFF_HEAP` storage level is specified

### 4.9 `spark.sql.execution.sortBeforeRepartition`

- Default `true`
- Sorts records within each **map-side partition** by their hash value before the repartition shuffle write
- Improves sequential disk writes during shuffle write phase; reduces random I/O
- Trade-off: extra pre-sort CPU overhead; disable to reduce CPU at cost of random writes
- NOT a global sort; NOT `repartitionByRange`

### 4.10 Kryo `registrationRequired`

- `spark.kryo.registrationRequired=true`: raises `KryoException` for any unregistered class → job fails
- All serialized classes must be registered via `spark.kryo.classesToRegister` or custom `KryoRegistrator`
- Default `false`: Kryo writes full class name for unregistered classes (larger bytes, slower, but works)

---

## Topic 5: Structured Streaming (Q81–Q90, 10%)

### 5.1 Trigger Modes

| Trigger | Behavior |
|---------|----------|
| `trigger(once=True)` | Processes all available data in **one** micro-batch; then stops |
| `trigger(availableNow=True)` (Spark 3.3+) | Processes all available data across **multiple** micro-batches (respects rate limits like `maxFilesPerTrigger`); then stops |

- `availableNow` provides "catch up and stop" with better parallelism and rate limiting than `once`

### 5.2 Query Progress Metrics

- `inputRowsPerSecond`: rate at which rows **arrive at the source** (from source metadata: Kafka lag, file times)
- `processedRowsPerSecond`: rate at which rows were **actually processed** in the last micro-batch
- Source rate > processing rate → query is falling behind (backlog growing)

### 5.3 Streaming File Source Schema

- Schema **must be specified explicitly** for all file-based streaming sources
- `spark.readStream.format("json").load(path)` without `.schema(...)` → `AnalysisException`
- Schema inference is NOT available for streaming (cannot scan full dataset upfront)

### 5.4 Console Sink

- Prints each micro-batch output to **driver stdout**
- **Debugging/development only**: not fault-tolerant; no exactly-once delivery; not production-ready
- Does not write to HDFS; does not buffer until `stop()`

### 5.5 Watermark + Append Mode

- Watermark threshold = `max_event_time - delay`
- With watermark at `12:08` and `10 min` delay → drop threshold = `11:58`
- Event at `12:03`: `12:03 > 11:58` → **NOT dropped** → appended to output

### 5.6 `session_window()` (Spark 3.2+)

- Gap-based **dynamic** window: session extends as long as events arrive within the gap duration
- Session closes when no event arrives within the gap
- Variable duration (unlike fixed tumbling or sliding windows)
- Available in PySpark DataFrame API (not SQL-only)

### 5.7 Kafka Source — Fixed Schema

Always produces:
```
key           BinaryType
value         BinaryType
topic         StringType
partition     IntegerType
offset        LongType
timestamp     TimestampType
timestampType IntegerType
```
- Decode `value` with `F.from_json()`, `CAST(value AS STRING)`, etc.
- Schema is NOT inferred from message content; NOT configurable via `option("schema", ...)`

### 5.8 `kafka.group.id` Risk

- If set: Kafka brokers track committed offsets for that consumer group
- Multiple concurrent Spark queries sharing the same `group.id` → **interfere** with each other's offset tracking
- Spark recommendation: **don't set** `kafka.group.id`; let Spark manage offsets via checkpoint directory

### 5.9 `maxOffsetsPerTrigger`

- `.option("maxOffsetsPerTrigger", "10000")`: caps total Kafka offsets read across **all partitions** per trigger
- Prevents large backlog from creating oversized micro-batches → avoids memory pressure and long processing times
- Not partition limit; not lag alert threshold; not starting offset

### 5.10 `mapGroupsWithState` vs `flatMapGroupsWithState`

| Operator | Output per group per trigger |
|----------|------------------------------|
| `mapGroupsWithState` | Exactly **one** row |
| `flatMapGroupsWithState` | **Zero or more** rows (Iterator) |

- `flatMapGroupsWithState` enables: emit nothing for intermediate state updates; emit multiple events per state transition

---

## Topic 6: Spark Connect (Q91–Q95, 5%)

### 6.1 `AnalysisException` Timing

- **Classic PySpark**: analysis (column resolution, schema validation) at transformation time via local Py4J
- **Spark Connect**: logical plan sent to server ONLY at **action time** (`collect()`, `show()`, `count()`); `AnalysisException` raised at that point
- Spark Connect does NOT suppress AnalysisExceptions; does NOT validate at session creation

### 6.2 Token Authentication in URL

```
sc://hostname:15002/;token=mySecretToken
```
- `;token=<value>` suffix in the `sc://` URL
- Forwarded by gRPC client as a header on every request
- NOT as a separate `.option("token", ...)` call; NOT environment variable

### 6.3 No Local JVM Required

- **Classic PySpark**: local JVM (Py4J gateway) required on client machine to translate Python calls to JVM
- **Spark Connect**: replaces Py4J with a gRPC stub; serializes logical plans sent over network
- JVM runs only on the remote Spark Connect **server**; no local JVM installation needed

### 6.4 Python UDF Serialization

- Python UDFs are **pickled** on the client
- Sent to Spark Connect server as part of the gRPC plan
- Deserialized and executed in a Python worker process **on the executor** side
- Identical to classic PySpark UDF execution model; just travels over the network

### 6.5 Server Crash Impact

- In-flight queries are **lost** (server holds all session state + execution state)
- **Client Python process SURVIVES** (unlike classic PySpark where JVM crash kills the driver)
- Developer can reconnect and resubmit queries
- No automatic retry or standby failover; no client-side buffering of results

---

## Topic 7: Pandas API on Spark (Q96–Q100, 5%)

### 7.1 `psdf.spark.cache()`

- Caches underlying Spark DataFrame with **`MEMORY_AND_DISK`** storage level
- Equivalent to `psdf.to_spark().cache()`
- Does NOT convert to native pandas; does NOT write to Delta; IS available directly on `psdf`

### 7.2 `psdf.spark.explain()`

- `psdf.spark.explain(extended=True)`: shows logical + physical execution plans
- Equivalent to `psdf.to_spark().explain(extended=True)`
- Not pandas memory summary; not an operation diff

### 7.3 `default_index_type` Options

| Type | Speed | Index Values | Notes |
|------|-------|-------------|-------|
| `"distributed"` | **Fastest** | Non-contiguous; may not start at 0 | Uses `monotonically_increasing_id()`; `iloc` may be unexpected |
| `"distributed-sequence"` | **Slowest** | Contiguous 0-based | Requires global sort/count; matches pandas behavior most closely |

### 7.4 `psdf.to_delta()`

- `psdf.to_delta("/mnt/output/my_table")`: writes to Delta Lake format
- Equivalent to `psdf.to_spark().write.format("delta").save(path)`
- Creates table if not exists; NOT always append mode

### 7.5 NULL vs NaN Semantics (Q100 — many: A, C, D correct)

- A) ✅ NaN and NULL are **distinct** internally; different behavior in aggregations and filtering
- B) ❌ `psdf.dropna()` drops NULL rows; by default does NOT drop NaN unless stored as NULL
- C) ✅ `psdf.fillna(0)` fills NULL but NOT NaN in float columns; use `F.isnan()` or `replace(float('nan'), None)` for NaN
- D) ✅ SQL aggregations ignore NULL; NaN **propagates** through arithmetic: `sum([1.0, NaN, 2.0])` = `NaN`

---

## Key Traps Table

| # | Trap Scenario | Wrong Assumption | Correct Answer |
|---|--------------|-----------------|----------------|
| 1 | `coalesce(n)` when n > current count | Increases partitions | No-op; cannot increase without shuffle |
| 2 | `RDD.cache()` vs `DF.cache()` | Same StorageLevel | RDD=MEMORY_ONLY; DF=MEMORY_AND_DISK |
| 3 | Non-equi join strategy | SortMergeJoin | BroadcastNestedLoopJoin or CartesianProduct |
| 4 | `try_divide(10, 0)` | ArithmeticException | Returns NULL |
| 5 | `try_add(MAX_INT, 1)` | Overflow wrap-around | Returns NULL |
| 6 | ANSI CAST `'abc' AS INT` | Returns NULL | Raises SparkNumberFormatException |
| 7 | `cardinality(NULL)` | Returns 0 or -1 | Returns NULL |
| 8 | `size(NULL)` | Returns NULL | Returns -1 (legacy default) |
| 9 | `unix_date()` return type | LongType seconds | IntegerType DAYS |
| 10 | `make_timestamp` out-of-range | Exception | Returns NULL |
| 11 | `bool_and` / `bool_or` with NULLs | NULL causes false | NULLs ignored; NULL result only if ALL are NULL |
| 12 | `bit_or([5,3,8])` | 8 (max value) or sum | 15 (bitwise OR) |
| 13 | `array_compact` | Sorts elements | Only removes NULLs, preserves order |
| 14 | `startswith` return type | IntegerType or StringType | BooleanType |
| 15 | `inline()` in SELECT | Requires LATERAL VIEW | Valid directly in SELECT |
| 16 | `named_struct` vs `struct` | Identical output | named_struct allows explicit custom field names |
| 17 | `from_csv` nested support | Supports nesting like from_json | Flat only — no nested objects/arrays |
| 18 | `F.aggregate` 4th arg | Required | Optional (finish function) |
| 19 | `F.forall` with one failing | True (majority pass) | false — ALL must pass |
| 20 | `array_insert(arr, 2, "new")` | Inserts after element 2 | Inserts BEFORE current element 2 |
| 21 | `try_element_at` OOB | Clamps to last or throws | Returns NULL |
| 22 | `partitionBy` one file per key | Spark auto-coalesces | No auto-coalesce; files = DF partitions per key |
| 23 | `bucketBy` with `save(path)` | Works anywhere | Only with `saveAsTable` |
| 24 | `current_timestamp()` per-row | Each row unique | All rows in one execution share same value |
| 25 | Parquet `"deflate"` compression | Valid codec | INVALID — use snappy/gzip/brotli/lz4/zstd |
| 26 | `df.tail(5)` vs `limit(5)` | Same as first 5 | LAST 5 rows |
| 27 | `df.to()` vs `df.select()` | Both same | `to()` auto-casts; `select()` does not |
| 28 | `sampleBy` unspecified key rows | All rows included | Rows with key not in fractions dict EXCLUDED |
| 29 | `checkpoint(eager=False)` | Writes immediately | Deferred to next action |
| 30 | `F.median()` vs exact | Exact result | Approximate (same as percentile_approx) |
| 31 | `trigger(once)` vs `availableNow` | Same behavior | `once` = 1 batch; `availableNow` = multiple batches |
| 32 | `kafka.group.id` risk | Required for Kafka | Interferes if shared; Spark prefers checkpoint-based offset management |
| 33 | `mapGroupsWithState` output | Variable rows | Exactly 1 row per group per trigger |
| 34 | Spark Connect `AnalysisException` timing | At transformation | At ACTION time only |
| 35 | `psdf.fillna(0)` fills NaN | Both NULL and NaN filled | Only NULL; NaN needs separate handling |
| 36 | `distributed` index contiguous | Starts at 0, contiguous | Non-contiguous; may not start at 0 |
| 37 | `spark.driver.supervise` on YARN | Supported | NOT supported in YARN or Kubernetes cluster mode |
| 38 | `spark.executor.pyspark.memory` JVM | JVM heap setting | Off-heap Python worker memory |
| 39 | `split_part` 0-based position | Position 0 = first | 1-based; position 2 = second token |
| 40 | `schema_of_csv` return type | StructType object | DDL StringType — usable directly in `from_csv()` |
