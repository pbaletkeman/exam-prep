# Databricks Certified Associate Developer for Apache Spark — Iteration 6 Study Guide

**Comprehensive study guide for exam questions (Iteration 6)**

**Last Updated**: May 17, 2026

---

## Table of Contents

1. [Topic 1: Apache Spark Architecture & Internals](#topic-1-apache-spark-architecture--internals)
2. [Topic 2: Spark SQL](#topic-2-spark-sql)
3. [Topic 3: DataFrame/DataSet API](#topic-3-dataframedataset-api)
4. [Topic 4: Troubleshooting & Tuning](#topic-4-troubleshooting--tuning)
5. [Topic 5: Structured Streaming](#topic-5-structured-streaming)
6. [Topic 6: Spark Connect](#topic-6-spark-connect)
7. [Topic 7: Pandas API on Spark](#topic-7-pandas-api-on-spark)

---

## Topic 1: Apache Spark Architecture & Internals

### 1.1 RDD vs DataFrame Cache Defaults

**Key Distinction**:
- **`RDD.cache()`** defaults to **`MEMORY_ONLY`**: Partitions stored in memory; if evicted, they are recomputed from lineage.
- **`DataFrame.cache()`** (and `Dataset.cache()`) defaults to **`MEMORY_AND_DISK`**: Partitions stored in memory; if evicted from memory, they spill to disk rather than being recomputed.

**Reason**: DataFrames have more reliable fault tolerance via Catalyst optimizer, so disk spillover is preferred over recomputation. RDDs lack such optimization, so `MEMORY_ONLY` is the default.

### 1.2 FIFO vs FAIR Scheduler Modes

**FIFO Mode (default)**:
- Processes Jobs in **submission order**.
- The first-queued Job receives **all available executor slots** before later Jobs can start.
- Favors long-running jobs; short jobs may starve.

**FAIR Mode**:
- Distributes executor slots across **all concurrently running Jobs**.
- Short jobs can make progress while long jobs execute.
- Reduces latency for interactive queries in shared clusters.

**Configuration**: `spark.scheduler.mode=FAIR`

### 1.3 DAGScheduler vs TaskScheduler Responsibilities

**DAGScheduler** (runs on driver):
- Splits the RDD lineage graph into **stages** at shuffle boundaries.
- Tracks stage dependencies.
- Submits `TaskSet`s to the `TaskScheduler`.

**TaskScheduler** (runs on driver):
- Interfaces with the **cluster manager backend** to acquire executor slots.
- Assigns individual tasks to executors based on **data locality** (`PROCESS_LOCAL` → `NODE_LOCAL` → `RACK_LOCAL` → `ANY`).
- Retries failed tasks up to `spark.task.maxFailures`.
- Reports task completion back to the `DAGScheduler`.

### 1.4 Barrier Execution Mode

**Definition**: A special execution mode where **all tasks in a barrier stage must start simultaneously**.

**Key Guarantees**:
- If the cluster cannot provide enough free slots for all tasks at once, the stage **waits** until sufficient resources become available.
- Tasks cannot be launched incrementally or partially.

**Use Case**: MPI-style distributed workloads (distributed deep learning training) where peer tasks need to exchange data or synchronise checkpoints.

**API**: `BarrierContext` provides `allGather()` for exchanging data across all running tasks in the barrier stage.

**Failure Handling**: If any task in a barrier stage fails, Spark re-submits the **entire stage from scratch** rather than retrying only the failed task.

### 1.5 spark.executor.pyspark.memory — Python Worker Memory

**Purpose**: Controls the amount of memory **outside the executor JVM heap** that each Python worker process may consume per executor.

**Default**: Unset (unbounded by Spark)

**Risk of Not Setting**:
- Python worker memory is **unbounded** — governed only by OS limits.
- The Python worker can consume memory beyond the container's declared memory limit (from the cluster manager).
- Result: The executor **container is killed by YARN or Kubernetes** for exceeding the memory limit, failing the entire executor.

**Mitigation**: Set `spark.executor.pyspark.memory` to a safe value (e.g., `1g` for a 4GB executor) to cap Python memory consumption and prevent container kills.

### 1.6 Dynamic Resource Allocation — Shuffle Tracking

**`spark.dynamicAllocation.shuffleTracking.enabled`** (default `true` in Spark 3.0+):
- Spark **tracks which executors hold shuffle data** still required by downstream stages.
- DRA may only remove executors whose shuffle data is **no longer needed** by any downstream stage.

**Benefit**: Makes the **external shuffle service optional** for DRA on YARN and Kubernetes.
- Without shuffle tracking, DRA cannot remove executors with unread shuffle data → must preserve them indefinitely → less effective scaling.

### 1.7 Event Log Compression

**`spark.eventLog.compress=true`**:
- Enables **compression of event log files** written to `spark.eventLog.dir`.
- Produces **smaller log files** that the History Server **decompresses transparently**.

**Configuration**:
- **`spark.eventLog.compression.codec`** (default `zstd`): Controls the compression algorithm.
- Supported: `zstd`, `gzip`, `lz4`, `uncompressed`.

### 1.8 coalesce() Semantics

**Narrow Transformation**: `coalesce()` combines partitions **without a full shuffle**.

**Partition Count Behaviour**:
- If `n >= current partition count`: **No-op**; the DataFrame retains its original number of partitions.
- If `n < current partition count`: Merges partitions down to `n`.
- **Cannot increase partitions**: `coalesce(n)` is a no-op when `n > current count` (unlike `repartition(n)` which always shuffles).

**Efficiency**: `coalesce(1)` is **more efficient than `repartition(1)`** for reducing to a single file because it avoids a full shuffle.

### 1.9 Arrow Batch Size for Pandas UDFs

**`spark.sql.execution.arrow.maxRecordsPerBatch`** (default `10000`):
- Controls the maximum number of **rows in each Arrow record batch** transferred between the JVM executor and Python worker when executing Pandas UDFs.

**Trade-offs**:
- **Smaller values**: Reduce per-batch memory pressure but increase serialization round-trip overhead.
- **Larger values**: Improve throughput but increase peak memory per batch.

### 1.10 Non-Equi Joins — Physical Strategy

**Scenario**: `df1.join(df2, df1.value > df2.threshold, "inner")`

**Physical Join Strategy**: **`BroadcastNestedLoopJoin`** (if one side is broadcastable) or **`CartesianProduct` with a filter**.

**Why Not SortMergeJoin or BroadcastHashJoin?**
- Both require **equal-key hashing** on join columns.
- Non-equi joins have **no equi-join key** → hashing is inapplicable.
- Spark falls back to nested loop or Cartesian product approaches.

**Broadcast Preference**: Spark broadcasts the smaller side when possible to reduce network I/O.

### 1.11 Cluster Deploy Mode — Driver Lifecycle

**Cluster Mode**:
- `spark-submit` **launches the driver on a cluster node** and exits almost immediately after acceptance.
- Driver logs reside on the **cluster node** (not the submitting machine).
- The `spark-submit` process itself **does not remain connected** to the driver.

**Client Mode**:
- The `spark-submit` process **itself IS the driver** and runs until the application completes.
- Driver logs appear on the **submitting machine**.
- The `spark-submit` process stays connected throughout execution.

### 1.12 Data Locality Wait — Per-Level Configuration

**Per-Level Override Settings**:
- **`spark.locality.wait.process`**: Override for `PROCESS_LOCAL` → `NODE_LOCAL` transition.
- **`spark.locality.wait.node`**: Override for `NODE_LOCAL` → `RACK_LOCAL` transition.
- **`spark.locality.wait.rack`**: Override for `RACK_LOCAL` → `ANY` transition.

Each per-level setting **independently overrides `spark.locality.wait`** (default `3s`) for its respective transition.

### 1.13 Proactive Block Replication

**`spark.storage.replication.proactive`** (default `false`):
- When `true`, Spark **detects lost cached block replicas** (e.g., executor evicted by DRA).
- Spark **immediately replicates the lost block** from a surviving replica to another live executor.
- **Benefit**: Replenishes the lost copy **before a cache miss** forces full recomputation.

**Most Beneficial When**: Clusters with executor churn (Dynamic Resource Allocation with replication-factor storage levels like `MEMORY_AND_DISK_2`).

### 1.14 sc.parallelize() Partition Count

**Behaviour**:
- **When `numSlices` is provided**: Spark creates **exactly that many partitions**.
- **When `numSlices` is omitted**: Spark uses **`spark.default.parallelism`** as the default partition count.

### 1.15 spark.driver.supervise — Driver Auto-Restart

**`spark.driver.supervise=true`**:
- Spark **automatically restarts the driver process** if it exits with a **non-zero exit code** (application failure or crash).

**Scope**:
- **Only effective in cluster deploy mode** (`--deploy-mode cluster`); has **no effect in client mode**.
- Supported in **Spark Standalone cluster mode**.
- **NOT supported** in YARN cluster mode or Kubernetes cluster mode.

### 1.16 Two-Level Hash Map for Aggregation

**`spark.sql.codegen.aggregate.map.twolevel.enabled`** (default `true`):
- Implements a **two-level hash map strategy** for hash-based aggregations.

**Mechanism**:
- **Level 1**: A compact, **cache-friendly fixed-size hash map**.
- **Level 2**: A standard **full-sized hash map** for overflow entries.

**Benefit**: Improves **CPU cache hit rates** and reduces **object allocation pressure** compared to a single large hash map.

### 1.17 Worker Daemon vs Executor in Standalone Mode

**Worker Daemon**:
- A persistent **JVM process on each cluster node**.
- **Registers with the Master** to advertise available resources.
- **Manages local resources** and launches separate **Executor JVM processes** for each application assigned to that node.

**Executor**:
- A separate **JVM process** launched by the Worker daemon.
- **Multiple executors from different applications** can run under a single Worker simultaneously.

### 1.18 spark.rdd.compress — RDD Caching Compression

**`spark.rdd.compress=true`** (default `false`):
- Compresses the **serialized representation** of cached RDD partitions **in memory**.
- Reduces memory footprint at the cost of **CPU overhead for compression/decompression on every access**.

**Configuration**: **`spark.io.compression.codec`** controls the compression algorithm (default `snappy`).

### 1.19 Stage Re-computation When Executor Lost After Shuffle Write

**Scenario**: An executor is lost **after writing shuffle map output** but **before reduce tasks read those files**.

**Spark's Behavior**:
- Shuffle files on the lost executor's **local disk are inaccessible**.
- Spark **must re-run the map tasks** that wrote to that executor on **surviving executors** to regenerate the lost shuffle data.
- **Exception**: If an **external shuffle service** was deployed and held the files independently (not on the executor's local disk), no recomputation is required.

### 1.20 spark.app.name and Application ID

**`spark.app.name`**:
- A **human-readable label** visible in the Spark UI, History Server, and cluster manager UI.
- Set via `SparkConf` or the `--name` flag in `spark-submit`.

**Application ID**:
- **System-generated by the cluster manager**.
- Accessible at runtime via `spark.sparkContext.applicationId`.
- In YARN: Follows format `application_<rm-start-timestamp>_<sequence-number>` (e.g., `application_1714000000000_0001`).

**Uniqueness**: Two applications running simultaneously with the same `spark.app.name` **do NOT share the same Application ID** — each receives a unique ID from the cluster manager.

---

## Topic 2: Spark SQL

### 2.1 split_part() Function (Spark 3.3+)

**Syntax**: `split_part(str, delimiter, position)`

**Behavior**: Splits the string by the delimiter and returns the **1-based token at the specified position**.

**Example**: `split_part('a:b:c:d', ':', 2)` → `'b'` (the second token)

### 2.2 try_divide() — Safe Division (Spark 3.4+)

**Behavior**: `try_divide(dividend, divisor)` returns **`NULL` when the divisor is zero**, instead of raising an `ArithmeticException`.

**Use Case**: Safely dividing by columns that may contain zeros without requiring explicit `CASE WHEN` guards.

### 2.3 any_value() — Arbitrary Value Selection (Spark 3.3+)

**With `IGNORE NULLS`**: Returns an **arbitrary non-null value** from the group without ordering guarantees.

**`NULL` Handling**: Returns `NULL` **only if every value in the group is `NULL`**; otherwise ignores `NULL` values when selecting a candidate.

### 2.4 make_date() Function

**Syntax**: `make_date(year, month, day)`

**Return Type**: **`DateType`** (not StringType or TimestampType)

**Example**: `make_date(2026, 12, 25)` → `DATE '2026-12-25'`

### 2.5 regexp_like() vs regexp_extract()

**`regexp_like(str, pattern)`**:
- **Return Type**: `BooleanType`
- Returns `true` if `str` **matches** the regex pattern, `false` otherwise.

**`regexp_extract(str, pattern, idx)`**:
- **Return Type**: `StringType`
- Returns the text **captured by group `idx`** (returning an empty string if the pattern does not match).

### 2.6 width_bucket() Function

**Syntax**: `width_bucket(value, min_value, max_value, num_buckets)`

**Return**: A **1-based integer bucket number** for `value` within `num_buckets` equal-width buckets.

**Boundaries**:
- Values **below `min_value`** return `0`.
- Values **>= `max_value`** return `num_buckets + 1`.

### 2.7 make_timestamp() Function

**Syntax**: `make_timestamp(year, month, day, hour, minute, second)`

**Return Type**: **`TimestampType`**

**`NULL` Handling**: If any component is **`NULL` or out of range**, the function returns **`NULL`** (matching `make_date()` behavior); it does **NOT raise an error**.

### 2.8 bool_and() / bool_or() — NULL Handling

**`bool_and(col)`**:
- Returns `true` **only if every non-null value is `true`** (NULLs are ignored).
- Returns `NULL` **only when all values in the group are `NULL`**.

**`bool_or(col)`**:
- Returns `true` **if at least one non-null value is `true`** (NULLs are ignored).
- Returns `NULL` **only when all values in the group are `NULL`**.

### 2.9 bit_and / bit_or / bit_xor Aggregate Functions

**Example**: `bit_or([5, 3, 8])`
- Computes bitwise OR: `5 | 3 | 8 = 0101 | 0011 | 1000 = 1111 = 15`

**NULL Handling**: Ignores `NULL` values; returns `NULL` only if all values are `NULL`.

### 2.10 array_compact() Function (Spark 3.4+)

**Behavior**: Removes **all `NULL` elements** from the array, **preserving the order** of remaining non-null elements.

**Example**: `array_compact([1, NULL, 2, NULL, 3])` → `[1, 2, 3]`

### 2.11 startswith() / endswith() Functions (Spark 3.3+)

**Return Type**: **`BooleanType`**

**Example**: `startswith("hello", "he")` → `true`

**`NULL` Propagation**: Returns **`NULL` if either argument is `NULL`**.

### 2.12 inline() — Table-Generating Function

**Definition**: Explodes an `ArrayType(StructType(...))` column into multiple rows, with each struct's fields becoming separate output columns.

**Example**:
```sql
SELECT inline(array(struct(1, 'a'), struct(2, 'b')))
-- Output: Two rows with columns from each struct unpacked
```

### 2.13 named_struct() vs struct()

**`struct(col1, col2)`**:
- Creates a `StructType` using the **input column names** as field names.
- If columns are unnamed (auto-generated), field names become `col1`, `col2`.

**`named_struct('x', col1, 'y', col2)`**:
- Allows **explicit custom field names** (`'x'`, `'y'`) for the resulting `StructType`.
- More flexible for renaming fields inline.

### 2.14 from_csv() Function (Spark 3.0+)

**Behavior**: Parses a **CSV-formatted string column** and returns a `StructType` column with declared fields.

**Syntax**: `from_csv(col, 'a INT, b STRING')`

**vs `from_json()`**:
- `from_csv` does **NOT support nested objects or arrays** since CSV is inherently flat.
- `from_json` supports complex nested structures.

### 2.15 schema_of_csv() Function (Spark 3.0+)

**Behavior**: Infers the schema from a **sample CSV string** and returns it as a **DDL-formatted `StringType`** value.

**Example**: `schema_of_csv('"hello",42,true')` → `'_c0 STRING, _c1 INT, _c2 BOOLEAN'`

**Use**: Output can be passed to `from_csv(col, schema_of_csv(...))` for consistent schema inference.

### 2.16 cardinality() vs size() NULL Handling

**`cardinality(col)`** (SQL-standard):
- Returns **`NULL` when `col` is `NULL`**.

**`size(col)`** (legacy behavior):
- Returns **`-1` when `col` is `NULL`** (default, controlled by `spark.sql.legacy.sizeOfNull`).

### 2.17 unix_date() Function (Spark 3.1+)

**Return Type**: **`IntegerType`** (NOT LongType)

**Value**: Number of **days since the Unix epoch** (`1970-01-01`)

**Example**: `unix_date(date'2026-04-25')` returns an integer count of days from the epoch to that date.

### 2.18 date_from_unix_date() Function (Spark 3.1+)

**Behavior**: Converts an integer day offset into a **`DateType`** value.

**Inverse**: `date_from_unix_date` is the **inverse of `unix_date(date_col)`**.

**Example**: `date_from_unix_date(20203)` returns the date 20203 days after `1970-01-01`.

### 2.19 try_add() / try_subtract() / try_multiply() Safe Arithmetic (Spark 3.4+)

**Behavior**: Returns **`NULL` on arithmetic overflow** instead of raising an `ArithmeticException`.

**Example**: `try_add(2147483647, 1)` (Integer.MAX_VALUE + 1) → `NULL`

**Use Case**: Safely handling arithmetic operations on large numbers without wrapping or exceptions.

### 2.20 regexp_count() Function (Spark 3.4+)

**Behavior**: Returns the **total number of non-overlapping occurrences** of the regex pattern in the string.

**Example**: `regexp_count('abcabc', 'a.c')` → `2` (the pattern `a.c` matches `abc` twice)

---

## Topic 3: DataFrame/DataSet API

### 3.1 df.sampleBy() — Stratified Sampling

**Syntax**: `df.sampleBy("status", {"active": 0.5, "inactive": 0.1}, seed=42)`

**Behavior**: **Stratified sampling** — for each value in the `status` column, independently samples the specified fraction:
- ~50% of rows where `status='active'`
- ~10% of rows where `status='inactive'`

**Rows Excluded**: Rows whose `status` value is **not in the `fractions` dictionary** are **excluded** from the result.

### 3.2 df.checkpoint() Eager vs Lazy

**`eager=True`**:
- **Immediately triggers an action** to materialise and write the DataFrame to the checkpoint directory.
- Returns a new DataFrame backed by the checkpoint data.

**`eager=False`**:
- **Defers checkpointing** until the next action is called on the returned DataFrame.
- The checkpoint is written lazily as part of that subsequent action.

### 3.3 F.product() Aggregate Function (Spark 3.2+)

**Behavior**: Computes the **product (multiplication) of all non-null values** within each group.

**`NULL` Handling**: `NULL` values are **ignored** — same convention as `sum()` and `avg()`.

**Example**: `df.groupBy("category").agg(F.product("price"))` multiplies all prices per category.

### 3.4 df.to() — Project to Target Schema (Spark 3.4+)

**Behavior**: **Reorders and casts columns** to match the target schema.

**Key Differences from `df.select()`**:
- Matches columns by **name** (not position).
- **Automatically casts types**.
- Raises `AnalysisException` if a column in the target schema is **missing** from the DataFrame.

### 3.5 F.transform_keys() HOF on MapType (Spark 3.1+)

**Syntax**: `F.transform_keys(map_col, lambda k, v: ...)`

**Behavior**: Applies the lambda to **each key** in the map, **replacing keys** while keeping values unchanged.

**Example**: `transform_keys({"math": 90}, lambda k, v: F.upper(k))` → `{"MATH": 90}`

### 3.6 F.transform_values() HOF on MapType (Spark 3.1+)

**Syntax**: `F.transform_values(map_col, lambda k, v: ...)`

**Behavior**: Applies the lambda to **each value** in the map, **replacing values** while keeping keys unchanged.

**Example**: `transform_values({"apples": 5}, lambda k, v: v * 2)` → `{"apples": 10}`

### 3.7 df.withField() — Update Nested Struct Field (Spark 3.1+)

**Syntax**: `df.withColumn("address", df["address"].withField("country", F.lit("US")))`

**Behavior**: **Adds or replaces a named field** within a `StructType` column **without reconstructing the entire struct**.

### 3.8 df.dropFields() — Remove Struct Fields (Spark 3.1+)

**Syntax**: `df.withColumn("profile", df["profile"].dropFields("ssn"))`

**Behavior**: **Removes named fields** from a `StructType` column, returning the modified column with remaining fields.

### 3.9 df.tail(n) — Retrieve Last N Rows (Spark 3.0+)

**Return Type**: Python **list of `Row` objects**

**Key Difference**: `df.tail(5)` returns the **last 5 rows**; `df.limit(5).collect()` returns the **first 5 rows**.

### 3.10 F.array_insert() Function (Spark 3.4+)

**Syntax**: `F.array_insert(arr, pos, value)`

**Behavior**: Inserts `value` at the **1-based position `pos`**, **shifting existing elements right**.

**Example**: `array_insert(["a", "b", "c"], 2, "new")` → `["a", "new", "b", "c"]`

### 3.11 F.aggregate() HOF — Custom Fold (Spark 3.1+)

**Syntax**: `F.aggregate(arr, zero, lambda acc, x: acc + x)`

**Behavior**: Performs a **fold** over array elements using the merge function, starting with the zero value.

**Example**: `aggregate([1, 2, 3, 4], 0, lambda acc, x: acc + x)` → `10`

### 3.12 F.zip_with() HOF (Spark 3.1+)

**Syntax**: `F.zip_with(arr1, arr2, lambda x, y: x + y)`

**Behavior**: **Element-wise applies** the merge function to corresponding elements from two arrays.

**Example**: `zip_with([10, 20], [1, 2], lambda x, y: x + y)` → `[11, 22]`

### 3.13 F.exists() and F.forall() HOF on Arrays (Spark 3.1+)

**`forall(arr, predicate)`**:
- Returns `true` **only when every element satisfies** the predicate.
- Returns `false` if **any element fails** the predicate.

**`exists(arr, predicate)`** (implicit):
- Returns `true` if **at least one element** satisfies the predicate.

### 3.14 F.flatten() on Nested Arrays

**Behavior**: Takes an `ArrayType(ArrayType(...))` and returns a **single-level `ArrayType`** by concatenating all inner arrays.

**Example**: `flatten([[1, 2], [3, 4], [5]])` → `[1, 2, 3, 4, 5]`

### 3.15 df.writeTo() v2 API — createOrReplace() vs append()

**`createOrReplace()`**:
- **Atomically drops and recreates** the table if it exists.
- **Replaces all existing data**.

**`append()`**:
- **Adds rows to** the existing table without removing prior data.
- Creates the table if it does not exist.

### 3.16 F.try_element_at() Safe Array/Map Access (Spark 3.4+)

**Behavior**: Returns **`NULL` when the 1-based index is out of range** (or key absent in a map), instead of throwing an exception.

**vs `F.element_at()`**: `element_at` raises an error on out-of-bounds access; `try_element_at` returns `NULL`.

### 3.17 F.array_remove() and F.array_distinct()

**`array_remove(arr, value)`**:
- Removes **all occurrences** of the specified value from the array.

**`array_distinct(arr)`**:
- Removes **duplicate elements**, keeping the **first occurrence** of each distinct value.

### 3.18 F.date_diff() vs F.datediff() (Spark 3.5+)

**Both Functions Are Aliases**:
- `F.date_diff(end, start)` (snake_case, Spark 3.5+ naming convention)
- `F.datediff(end, start)` (camelCase, older naming)

**Functionally identical**: Both return `IntegerType` days from start to end.

### 3.19 df.crossJoin() — Cartesian Product

**Behavior**: Produces the **Cartesian product** — every row of `df1` paired with every row of `df2`.

**Result Size**: `df1.count() × df2.count()` rows

**Guard**: **`spark.sql.crossJoin.enabled=true`** must be set to allow `crossJoin()` (prevents accidental Cartesian products).

### 3.20 write.partitionBy() Behavior

**Directory Structure**:
- Creates directories: `year=<val>/month=<val>/` with part files inside each leaf directory.

**Partition Columns in Data Files**:
- Partition columns are **excluded** from the data files written inside each partition directory.
- Their values are **encoded in the directory name only**.

**Output Files Per Partition**:
- Number of files per partition directory equals the **number of DataFrame partitions** with that key combination.
- NOT automatically coalesced to one file per partition.

---

## Topic 4: Troubleshooting & Tuning

### 4.1 AQE Skew Join Handling

**`spark.sql.adaptive.skewJoin.enabled=true`** (default):
- AQE **detects oversized shuffle partitions** (exceeding threshold settings).
- For each skewed partition, Spark:
  - **Splits the skewed side** into multiple sub-partitions.
  - **Replicates** the corresponding matching partition from the other side.
  - Processes each sub-partition pair as a **separate task**.

**Benefit**: Reduces **maximum task duration** without reshuffling the entire dataset.

### 4.2 Arrow pyspark.selfDestruct.enabled

**`spark.sql.execution.arrow.pyspark.selfDestruct.enabled=true`**:
- **Releases each Java Arrow buffer immediately** after it is copied into the pandas DataFrame.
- **Reduces peak JVM heap usage** during `toPandas()`.

**Mechanism**: Without this setting, all Arrow batches are held in memory simultaneously until all copying is complete; with it enabled, each batch is freed immediately after use.

### 4.3 Whole-Stage Code Generation

**`spark.sql.codegen.wholeStage`** (default `true`):
- **Fuses multiple operators** within a stage into a **single compiled Java method**.
- Reduces **virtual function call overhead**.
- Enables **JIT compiler** to generate efficient **native code** for the entire pipeline.

**Auto-Disabling**:
- Automatically disabled for operators with **> `spark.sql.codegen.maxFields`** (default 100) input or output fields.
- Very wide schemas become counterproductive for code generation.

**Debugging**: Setting `spark.sql.codegen.wholeStage=false` disables code generation, which produces cleaner stack traces for diagnosing codegen errors.

### 4.4 maxPartitionBytes and openCostInBytes Interaction

**`spark.sql.files.maxPartitionBytes`** (default 128 MB):
- Maximum data size per input partition.

**`spark.sql.files.openCostInBytes`** (default 4 MB):
- **Virtual padding cost per file** to account for file-open overhead.

**Interaction**: A file of size N is treated as `N + openCostInBytes` when determining partition assignments.

**Effect**: **Many small files are merged into the same partition** when their total padded size stays under `maxPartitionBytes`, reducing the number of tasks that each open just one tiny file.

### 4.5 coalescePartitions.parallelismFirst

**`spark.sql.adaptive.coalescePartitions.parallelismFirst`** (default `true`):

**When `true`**:
- AQE prioritises `advisoryPartitionSizeInBytes` (default 64 MB).
- Ignores `coalescePartitions.minPartitionNum`.
- May produce fewer partitions than `minPartitionNum`.

**When `false`**:
- AQE respects `minPartitionNum` as a **lower bound**.
- Protects parallelism at the expense of potentially producing smaller-than-advisory partitions.

### 4.6 spark.sql.files.ignoreMissingFiles

**Default (`false`)**:
- Spark raises `FileNotFoundException` when a file is deleted between query planning and execution.

**`true`**:
- Spark **skips missing files** and returns only the data that was successfully read.
- Useful for directories where files may be deleted concurrently (e.g., data lakes with concurrent compaction).

### 4.7 shuffle.file.buffer — Write Buffering

**`spark.shuffle.file.buffer`** (default 32 KB):
- In-memory write buffer size for each **shuffle output file stream** on the executor.

**Effect of Increasing**:
- **Reduces system call frequency** to flush data to disk.
- **Improves shuffle write throughput**.
- **Cost**: Additional executor heap memory per concurrent shuffle write stream.

### 4.8 Off-Heap Memory Configuration

**`spark.memory.offHeap.enabled=true` and `spark.memory.offHeap.size`**:

**Characteristics**:
- Allocated **outside the JVM heap** using `sun.misc.Unsafe`.
- **NOT subject to JVM garbage collection** → reduces GC pause times.
- **Per-executor**: `offHeap.size` is additional to `spark.executor.memory` and not reflected in `--executor-memory`.

**Usage**:
- Used by the Tungsten execution engine for storing **sort buffers**, **hash tables**, and **cached data** (when `StorageLevel.OFF_HEAP` is explicitly specified).
- **NOT automatic**: On-heap caching is not disabled when off-heap is enabled.

### 4.9 sortBeforeRepartition

**`spark.sql.execution.sortBeforeRepartition`** (default `true`):
- Before a **hash-based repartition shuffle**, Spark **sorts records within each map-side partition** by their hash value.

**Benefits**:
- Improves **sequential disk writes** during the shuffle write phase.
- Reduces **random I/O**.

**Cost**: **Pre-sort CPU overhead** — can be disabled to trade write efficiency for lower CPU usage.

### 4.10 spark.kryo.registrationRequired

**Default (`false`)**:
- Unregistered Kryo classes fall back to Java serialization.

**`true`**:
- Spark raises **`KryoException` for any unregistered class**, **causing the job to fail**.
- Enforces **strict Kryo registration** — smaller serialized sizes and faster serialization.
- Requires all serialized classes to be explicitly registered via `spark.kryo.classesToRegister` or a custom `KryoRegistrator`.

---

## Topic 5: Structured Streaming

### 5.1 trigger(availableNow=True) vs trigger(once=True)

**`trigger(once=True)`**:
- Processes **all available data in a single mega-batch**, then stops.
- May cause **memory issues** for large backlogs.

**`trigger(availableNow=True)`** (Spark 3.3+):
- Processes all available data across **multiple micro-batches**.
- **Respects rate limits**: `maxFilesPerTrigger`, `maxBytesPerTrigger`, etc.
- Same "catch up and stop" semantics but with **better parallelism and fault tolerance**.

### 5.2 Streaming Progress Metrics

**`inputRowsPerSecond`**:
- Rate at which **rows arrive at the source** (measured from source metadata like Kafka lag or file modification times).

**`processedRowsPerSecond`**:
- Rate at which **rows were actually processed** by the streaming query in the last micro-batch.

**Relationship**: If the source is faster than the query can process, `inputRowsPerSecond > processedRowsPerSecond`; if the query is catching up, the reverse may be true.

### 5.3 Streaming File Source — Schema Requirement

**Requirement**: Streaming file sources **raise `AnalysisException`** if no explicit schema is provided.

**Reason**: Unlike batch reads, Spark **cannot scan the full dataset upfront** for schema inference; streaming sources must have an explicit schema.

### 5.4 Console Sink Characteristics

**Output**: Prints each micro-batch's output to **driver stdout**.

**Use Case**: **Debugging and development only** — NOT for production.

**Key Limitations**:
- **Not fault-tolerant**: Does not support checkpoint-based recovery across restarts.
- **No exactly-once delivery guarantee**.
- Supports all three output modes: `append`, `update`, `complete`.

### 5.5 Watermark + Append Mode — Late Data Handling

**Scenario**: Watermark at `12:08` with delay `10 min` → drop threshold is `12:08 - 10 min = 11:58`.

**Event Arrival**: Event with `event_time = 12:03` arrives.

**Outcome**: Since `12:03 > 11:58`, the event is **NOT dropped** and is **appended to output** (it is still considered "on time").

### 5.6 session_window() — Gap-Based Sessions (Spark 3.2+)

**Definition**: Defines **dynamic session windows** based on inactivity gaps.

**Behavior**:
- A session **starts with the first event** and **extends as long as** subsequent events arrive **within the gap duration**.
- The session **closes when no new event** arrives within the gap.

**Key Difference**: Unlike fixed tumbling or sliding windows, **sessions have variable duration** depending on event arrival patterns.

### 5.7 Kafka Source Schema

**Fixed Schema**:
- `key`: `BinaryType`
- `value`: `BinaryType`
- `topic`: `StringType`
- `partition`: `IntegerType`
- `offset`: `LongType`
- `timestamp`: `TimestampType`
- `timestampType`: `IntegerType`

**Payload Decoding**: The actual message payload is in the `value` column as **raw bytes** and must be decoded explicitly (e.g., `F.from_json()`, `CAST(...AS STRING)`).

### 5.8 kafka.group.id Option — Risks

**Problem**: When a fixed `kafka.group.id` is set:
- Kafka brokers **track committed offsets** for that consumer group.
- Multiple Spark streaming queries sharing the same `group.id` **interfere with each other's offset tracking**.

**Recommendation**: **Do NOT set** `kafka.group.id`; let Spark manage offsets **internally in the checkpoint directory** (the default behavior).

### 5.9 maxOffsetsPerTrigger Option

**Purpose**: **Caps the total number of Kafka offsets (rows)** read across all partitions per micro-batch trigger.

**Benefit**: Limits the amount of data processed in each batch, preventing a **single large burst** from creating an oversized micro-batch and causing **memory pressure or long processing times**.

### 5.10 flatMapGroupsWithState vs mapGroupsWithState

**`mapGroupsWithState`**:
- Emits **exactly one output row** per group per trigger.

**`flatMapGroupsWithState`**:
- Emits **zero or more output rows** per group per trigger.
- Supports a `timeout` mechanism (`ProcessingTimeTimeout` or `EventTimeTimeout`) for idle groups.
- Required output mode: `append` or `update` (NOT `complete`).
- State persists in checkpoint and survives query restarts.

---

## Topic 6: Spark Connect

### 6.1 Analysis Exception Error Surfacing

**Timing**: `AnalysisException` errors surface **when an action is triggered** (e.g., `collect()`, `show()`, `count()`).

**Mechanism**:
- The **logical plan is sent to the Spark Connect server only at action time**.
- The server performs **analysis and raises exceptions** at that point.
- **NOT at transformation time** — column references are not validated on the client side.

### 6.2 Token-Based Authentication

**Method**: Embed the token in the `sc://` URL using semicolon-separated parameters:

```python
SparkSession.builder.remote("sc://host:15002/;token=mySecretToken").getOrCreate()
```

The token is forwarded by the gRPC client as a header on every request.

### 6.3 PySpark Without Local JVM

**Key Advantage**: You can run `from pyspark.sql import SparkSession` on a machine **without Java installed**, then **connect to a remote Spark Connect server** to execute queries.

**Why**: The gRPC stub replaces the local Py4J gateway; the JVM runs only on the remote server.

### 6.4 Python UDF Execution in Spark Connect

**Serialization**:
- Python UDFs are **pickled on the client** and sent to the server as part of the gRPC plan.
- The server **deserializes and executes** the UDF in a Python worker process on the **executor side**.

**Behavior**: Identical to classic PySpark UDF execution, except the serialized function travels **over the network** rather than through Py4J.

**External Libraries**: Must be available on the **executor environment** (e.g., via `--py-files`), not just the client machine.

### 6.5 Spark Connect Server Crash Impact

**Client Survivability**:
- The **client Python process survives** (unlike classic PySpark where a JVM crash kills the driver process).

**Query Impact**:
- Queries **running at the time of the crash are lost**.
- In-progress queries receive an **error on their next request**.
- The developer can **reconnect and resubmit** queries after the server restarts (no automatic replay).

---

## Topic 7: Pandas API on Spark

### 7.1 Caching Pandas-on-Spark DataFrame

**Method**: `psdf.spark.cache()`

**Behavior**: The `.spark` accessor provides a bridge to native Spark DataFrame operations.

**Action**: Caches the underlying Spark DataFrame in memory using `MEMORY_AND_DISK` storage level.

**Result**: Subsequent operations on `psdf` that trigger Spark actions read from the cached data rather than recomputing from the source.

### 7.2 psdf.spark.explain() — Physical Plan

**Output**: Prints the **logical and physical execution plans** of the underlying Spark DataFrame.

**Equivalence**: `psdf.spark.explain(extended=True)` is equivalent to `psdf.to_spark().explain(extended=True)`.

**Use Case**: Understanding how Pandas API on Spark translates pandas-style operations into Spark execution plans.

### 7.3 default_index_type Options

**`"sequence"`**:
- Assigns a **globally sorted sequential index** starting at 0.
- Requires a **global sort** → slow for large DataFrames.
- Guarantees strict ordering matching pandas' behavior.

**`"distributed-sequence"`** (default):
- Assigns **monotonically increasing per-partition integers** without a global sort.
- **Fast** but not globally ordered.
- Trade-off: Good for most use cases.

**`"distributed"`**:
- Uses `monotonically_increasing_id()` → **fastest**.
- **Non-contiguous** index values per partition.
- May produce unexpected results for operations requiring stable contiguous indices (like `iloc`).

### 7.4 psdf.to_delta() Convenience Method

**Behavior**: Writes the Pandas-on-Spark DataFrame to the specified path in **Delta Lake format**.

**Equivalence**: `psdf.to_delta(path)` ≡ `psdf.to_spark().write.format("delta").save(path)`

**Convenience**: Simplifies saving to Delta without switching to the Spark DataFrame API.

### 7.5 NULL vs NaN Semantics

**Native Pandas**:
- `NaN` and `None` (NULL) both treated as missing for numeric columns.
- Propagated by most operations.

**Pandas API on Spark**:
- Missing values represented as **Spark SQL `NULL`** internally.
- `NaN` and `NULL` are **distinct**:
  - `psdf.isna()` returns `True` for both.
  - `psdf.dropna()` drops rows with `NULL` but does NOT drop rows with `NaN`.
  - `psdf.fillna(0)` fills `NULL` values but does NOT fill `NaN` in float columns.

**Aggregation Difference**:
- `sum()` and `avg()` ignore `NULL` values.
- `NaN` values in double columns **propagate through arithmetic** — `sum([1.0, NaN, 2.0])` returns `NaN`, not `3.0`.

---

**End of Study Guide (Iteration 6)**

Use this guide alongside the QUICK_REFERENCE_ITER6.md and PRACTICE_STRATEGY_ITER6.md for comprehensive exam preparation.
