# Databricks Certified Associate Developer for Apache Spark — Iteration 5 Study Guide

**Comprehensive study guide for exam questions (Iteration 5)**

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

### 1.1 spark.sql.shuffle.partitions vs spark.default.parallelism

**Key Distinction**:
- **`spark.sql.shuffle.partitions`** (default 200): Governs the number of **post-shuffle partitions** in Spark SQL and DataFrame operations. When a shuffle occurs (e.g., `groupBy`, `join`, `repartition`), the result is distributed across this many partitions.
- **`spark.default.parallelism`** (default: number of cores in the cluster): Governs the default partition count for **RDD operations** such as `parallelize()`, `reduceByKey()`, and other RDD-level transformations.

**Code Example**:
```python
# DataFrame shuffle → uses spark.sql.shuffle.partitions (200)
df.groupBy('key').count()  # Result has 200 partitions

# RDD reduceByKey → uses spark.default.parallelism
rdd = sc.parallelize([1, 2, 3]).reduceByKey(...)  # Result has spark.default.parallelism partitions
```

### 1.2 spark.driver.memory Default

**Default Value**: `1g` (1 gigabyte)

When not explicitly configured, the Spark driver's JVM heap is set to 1 GB, suitable for development but often insufficient for production applications that call `collect()` on large results.

### 1.3 StorageLevel.DISK_ONLY Recomputation

**Failure Behavior**:
- When an executor storing a `DISK_ONLY` partition fails, the partition data on that executor's disk is lost.
- Spark **recomputes** the partition from its RDD or DataFrame lineage rather than failing the job.
- The recomputed partition is then stored at the configured `StorageLevel` on a surviving executor.

**Lesson**: `DISK_ONLY` provides write-through caching for read-heavy workloads, with fault tolerance through lineage recomputation.

### 1.4 History Server Configuration

**Multi-Part Setup**:
- **Application Side**:
  - `spark.eventLog.enabled = true`: Enables event logging
  - `spark.eventLog.dir = /shared/path`: Points to shared durable storage (HDFS, S3) for event logs
- **History Server Side**:
  - `spark.history.fs.logDirectory = /shared/path`: Must match the application's `spark.eventLog.dir`
- **NOT Required**:
  - `spark.ui.enabled`: Controls only the live running application UI, not the History Server

### 1.5 Cached Stages in Spark UI

**Display Behavior**: Stages whose output is already materialized in memory cache are marked as **Skipped** in the Spark UI — they are not re-executed. Spark simply reads the in-memory blocks and proceeds to the next stage.

### 1.6 Block Manager Responsibilities

**Scope**: The Block Manager on each executor manages **all** block types:
- RDD partitions (cached and uncached)
- DataFrame/DataSet partitions (cached)
- Broadcast variable data (replicas on executors)
- Shuffle write blocks (mapper output stored locally during shuffle)

### 1.7 spark.memory.storageFraction

**Default**: `0.5` (50%)

**Mechanics**:
- Defines the initial fraction of Spark's unified memory (after reserving 300 MB for system) allocated to **storage** (caching).
- Remaining fraction (50%) is available for **execution** (shuffle, sort, aggregation).
- When execution memory runs low, Spark can **evict** cached blocks from the storage region to free space.
- Setting to `1.0` leaves zero initial execution allocation, forcing execution to evict storage before any task memory is available — likely causing performance issues.

### 1.8 StorageLevel.MEMORY_AND_DISK_SER vs MEMORY_AND_DISK

**Key Difference**:
- **`MEMORY_AND_DISK_SER`**: Partitions are stored in **serialized** (binary) format both in memory and on disk, using less memory but requiring CPU overhead for serialization/deserialization on every access.
- **`MEMORY_AND_DISK`**: Partitions are stored as **deserialized** JVM objects in memory and on disk, using more memory but avoiding deserialization overhead per access.

**Use Case**: `MEMORY_AND_DISK_SER` for memory-constrained clusters; `MEMORY_AND_DISK` for CPU-constrained clusters.

### 1.9 Kubernetes Docker Image Configuration

**Property**: `spark.kubernetes.container.image`

When deploying with `spark-submit --master k8s://...`, this property specifies the Docker image used for both driver and executor pods.

### 1.10 spark.rpc.message.maxSize

**Default**: 128 MB

**Behavior**:
- Limits the size of RPC messages between driver and executors.
- Attempting to send a larger message throws a `SparkException`.
- **Broadcast variables** transferred over RPC are subject to this limit.
- **`collect()` results** are governed by `spark.driver.maxResultSize`, NOT this limit — they use a separate channel.
- Can be increased by setting a larger value (e.g., `256` MB).

### 1.11 Sort-Merge Join I/O Cost

**More Expensive Phase**: **Shuffle read**

In a sort-merge join:
- **Shuffle write**: Mapper sorts its output into partition buckets and writes to local disk.
- **Shuffle read**: Reducer must pull data from **all mapper output files** across the network and disk, then sort. This pulling of remote data over the network/disk is the bottleneck.

### 1.12 spark.sql.adaptive.enabled Default (Spark 3.2+)

**Default**: `true`

Adaptive Query Execution is enabled by default starting with Spark 3.2, automatically optimizing queries at runtime.

### 1.13 spark.executor.instances with Dynamic Allocation

**Behavior**: When both `spark.executor.instances` (fixed count) and `spark.dynamicAllocation.enabled = true` are set:
- Spark **logs a warning** and **ignores** `spark.executor.instances`.
- Dynamic allocation uses `spark.dynamicAllocation.minExecutors` and `spark.dynamicAllocation.maxExecutors` to control the executor count.

### 1.14 Checkpoint Directory Requirements

**Storage Requirement**: `sc.setCheckpointDir()` must point to a **reliable, distributed file system** (HDFS, S3, GCS, etc.) **accessible by all executors**.

Checkpoint data must survive executor failures and be readable when re-executing failed stages; local filesystem or driver-only paths are insufficient.

### 1.15 Stage Count in DAG

**Example**:
```python
df = spark.read.parquet("s3://bucket/data/")
result = df.repartition(100).groupBy("region").agg(F.sum("sales"))
result.show()
```

**Stages**:
1. **Stage 1**: Read Parquet file
2. **Stage 2**: Shuffle from `repartition(100)` (wide transformation)
3. **Stage 3**: Shuffle from `groupBy().agg()` (wide transformation)

**Total: 3 stages**

### 1.16 Task Locality Preference Order

**Spark's Locality Levels** (most to least preferred):
1. `PROCESS_LOCAL`: Data in the task's executor JVM (same process)
2. `NODE_LOCAL`: Data on the same node as the executor
3. `RACK_LOCAL`: Data in the same rack as the node
4. `ANY`: Data anywhere in the cluster

Spark waits `spark.locality.wait` (default 3 s) before downgrading to the next level.

### 1.17 spark.reducer.maxReqsInFlight

**Purpose**: Controls the maximum number of **concurrent shuffle block fetch requests** that a single reducer task can issue to remote executors simultaneously.

Prevents network saturation by limiting how many parallel remote reads one task can do.

### 1.18 MEMORY_ONLY Cache Eviction

**Behavior**:
- When a partition cached at `StorageLevel.MEMORY_ONLY` is evicted to free execution memory:
  - The partition is **dropped from memory entirely** — NOT written to disk.
  - If subsequently needed, Spark **recomputes** it from lineage.
  - Eviction candidates are selected using **LRU (Least Recently Used)** policy.

### 1.19 Pipelined Execution Within Stages

**Mechanism**: Transformations within a stage (narrow ops like filter, map, select) are **pipelined** — each record flows through all operators in sequence without full materialization between them.

Enables **WholeStageCodeGen** optimization: Catalyst generates a single compiled JVM method for the entire stage pipeline.

### 1.20 spark.sql.autoBroadcastJoinThreshold

**Default**: `10 MB`

When one table's estimated size is **at or below** this threshold, Spark automatically selects a `BroadcastHashJoin` without requiring an explicit `broadcast()` hint.

---

## Topic 2: Spark SQL

### 2.1 datediff Function

**Syntax**: `datediff(endDate, startDate)`

**Return**: Integer number of days from `startDate` to `endDate` (i.e., `endDate − startDate`).
- Positive when `endDate` is after `startDate`.
- Negative when `endDate` is before `startDate`.

### 2.2 unix_timestamp() with No Arguments

**Return Type**: `LongType`

`unix_timestamp()` with no arguments returns the **current Unix epoch timestamp** (seconds since 1970-01-01 00:00:00 UTC) as a `LongType` column.

### 2.3 initcap Function

**Definition**: Initializes the first character of each word (whitespace-delimited) to uppercase, rest to lowercase.

`initcap("hello world")` → `"Hello World"`

### 2.4 nullif Function

**Syntax**: `nullif(expr1, expr2)`

**Return**:
- `NULL` if `expr1 = expr2`
- Otherwise returns `expr1`

Useful for replacing sentinel values with `NULL` (e.g., converting `-1` or empty string to `NULL`).

### 2.5 trunc vs date_trunc

**Key Distinction**:
- **`trunc(date, fmt)`**: Accepts `DateType`, returns `DateType` truncated to unit (e.g., `'month'`, `'year'`).
- **`date_trunc(fmt, timestamp)`**: Accepts `TimestampType`, returns `TimestampType` truncated to finer unit (e.g., `'hour'`, `'minute'`).

### 2.6 locate Function Indexing

**Indexing**: Uses **1-based** indexing (not 0-based).

`locate("world", "hello world", 1)` → `7` (position of first character of "world")

### 2.7 dayofweek Function

**Definition**: Returns day of week as integer where `1 = Sunday`, `2 = Monday`, ..., `7 = Saturday`.

### 2.8 last_day Function

**Definition**: Returns the last day of the month for the given date.

`last_day('2026-04-10')` → `'2026-04-30'` (April has 30 days)

### 2.9 percentile vs percentile_approx

**Key Difference**:
- **`percentile(col, p)`**: Computes exact percentile using a full sort of the column data. Does not scale well for large distributed datasets.
- **`percentile_approx(col, p, accuracy)`**: Uses a Greenwald–Khanna quantile sketch to compute an approximate percentile with bounded error. Highly scalable for distributed data.

### 2.10 count_if Aggregate

**Definition**: Counts the number of rows in the group where the boolean `condition` evaluates to `true`.

`count_if(col > 0)` → count of rows where col is positive.

### 2.11 max_by Function

**Introduced**: Spark 3.0

**Definition**: Returns the value of `value_col` from the row that has the **maximum** value of `ordering_col` within the group.

`max_by(salary, performance_score)` → highest salary for best performer.

### 2.12 CTE (WITH Clause) in Spark SQL

**Syntax**:
```sql
WITH cte_name AS (
  SELECT ... FROM ...
)
SELECT * FROM cte_name
```

**Features**:
- Named subqueries defined in the `WITH` clause.
- Multiple CTEs supported, separated by commas.
- Spark optimizes CTEs via Catalyst (typically inlines them; not always materialized to disk).
- Recursive CTEs (e.g., `WITH RECURSIVE`) are **not supported** in Spark SQL through version 3.5.

### 2.13 stack Function

**Syntax**: `stack(n, v1, v2, v3, ..., vN*n)`

**Behavior**: Transposes every `n` values into a new row.

`stack(2, 'a', 1, 'b', 2)` → Two rows: `('a', 1)` and `('b', 2)`

### 2.14 get_json_object Function

**Syntax**: `get_json_object(json_string, jsonpath_expr)`

**Return**: `StringType` containing the scalar value extracted from the JSON string using JSONPath.

`get_json_object('{"user":{"name":"Alice"}}', '$.user.name')` → `"Alice"`

### 2.15 sort_array Function

**Syntax**: `sort_array(array_col, ascending: Boolean)`

- `sort_array(arr, True)`: Ascending order (default)
- `sort_array(arr, False)`: **Descending** order

### 2.16 map_entries Function

**Return Type**: `ArrayType(StructType(key, value))`

Converts a map into an array of struct entries, one struct per key-value pair.

`map_entries(map('a', 1, 'b', 2))` → `[{a, 1}, {b, 2}]`

### 2.17 ROLLUP and GROUPING_ID

**`GROUPING_ID` Bitmask**:
- Bit `0` (rightmost) represents the rightmost column in the `ROLLUP` list.
- Bit is `1` if that column is rolled up (aggregated); `0` if grouped.
- Value `0` (binary `00`) means all columns are in the grouping key (finest grain).
- Value `3` (binary `11`) means both columns are rolled up (grand total).

### 2.18 nth_value Window Function

**Definition**: Returns the value of `col` from the `n`-th row of the window frame (ordered by the `ORDER BY` expression).

Returns `NULL` if fewer than `n` rows exist in the frame.

---

## Topic 3: DataFrame/DataSet API

### 3.1 df.columns Return Type

**Return Type**: Python **list of strings**

`df.columns` → `['id', 'name', 'email']`

### 3.2 df.transform Function

**Purpose**: Applies a user-defined function to the entire DataFrame.

`df.transform(func)` calls `func(df)` and returns the resulting DataFrame, enabling clean chaining of DataFrame-level transformations.

### 3.3 df.toLocalIterator vs df.collect

**Key Difference**:
- **`toLocalIterator()`**: Streams partitions one at a time to the driver. Peak driver memory ≈ size of one partition.
- **`collect()`**: Materializes the **entire** DataFrame in driver memory at once. Peak driver memory ≈ total DataFrame size.

`toLocalIterator()` is safer for large results.

### 3.4 F.struct Column Schema

**Return Type**: `StructType([StructField("lat", ...), StructField("lon", ...)])`

Fields are named after the input column objects:
```python
F.struct(F.col("lat"), F.col("lon"))  # StructType with field names "lat" and "lon"
```

### 3.5 df.withColumnsRenamed (Spark 3.4+)

**Syntax**:
```python
df.withColumnsRenamed({"old1": "new1", "old2": "new2"})
```

Renames multiple columns in a single atomic call, equivalent to chaining multiple `withColumnRenamed` calls.

### 3.6 foreach vs foreachPartition

**Key Differences**:
- **`foreach(func)`**: Invokes `func` once per **row**, receiving a single `Row` object.
- **`foreachPartition(func)`**: Invokes `func` once per **partition**, receiving an iterator of `Row` objects.

`foreachPartition` is more efficient for operations with per-connection setup cost (e.g., database writes).

### 3.7 mapInPandas Function

**Pattern**:
```python
df.mapInPandas(func, schema)
```

Applies `func` partition-by-partition:
- Each partition arrives as an **iterator** of `pd.DataFrame` chunks.
- `func` must **yield** an iterator of `pd.DataFrame` objects back.
- Results are assembled into a Spark DataFrame with the given `schema`.

### 3.8 saveAsTable vs insertInto

**Key Difference**:
- **`saveAsTable`**: Creates or **replaces** the table using the DataFrame's schema.
- **`insertInto`**: Appends or overwrites an **existing** table by **column position** (not column name), risking silent data misalignment if column order differs.

### 3.9 F.levenshtein Function

**Return Type**: `IntegerType` (edit distance)

Computes the Levenshtein edit distance (minimum insertions, deletions, or substitutions) between two strings.

### 3.10 df.na.drop(thresh=n)

**Behavior**: Keeps a row only if it has **at least** `thresh` **non-null** values.

`df.na.drop(thresh=2)` drops rows with fewer than 2 non-null columns.

### 3.11 df.unpivot (Spark 3.4+)

**Purpose**: Melts wide format to long format.

Each column in `values` becomes two output columns: one for the column name (`variableColumnName`) and one for its value (`valueColumnName`); `ids` columns are preserved.

### 3.12 df.show() Truncation

**Default**: Truncates string values to **20 characters**.

`df.show(truncate=False)` or `df.show(truncate=0)` displays full column values.

### 3.13 F.raise_error Function

**Behavior**: Always raises a `RuntimeException` with the given message when the column expression is evaluated.

Used inside `when()` conditions to enforce data quality rules inline.

### 3.14 JDBC fetchsize Option

**Purpose**: Controls the JDBC row batch size per network round-trip.

Increasing it reduces network round-trips to the database at the cost of higher executor memory per task.

### 3.15 CSV inferSchema Performance Impact

**Behavior**: With `inferSchema=true`, Spark makes **two full passes** over the CSV data:
1. First pass infers column types.
2. Second pass reads with the inferred schema.

This **doubles I/O cost** compared to providing an explicit schema.

### 3.16 CSV sep vs delimiter Option

**Both are Valid Aliases**:
- `.option("sep", "|")`
- `.option("delimiter", "|")`

Both set the same underlying option for CSV field separator.

### 3.17 F.hash vs F.xxhash64

**Differences**:
- **`F.hash(*cols)`**: Uses MurmurHash3, returns `IntegerType` (32-bit).
- **`F.xxhash64(*cols)`**: Uses xxHash64, returns `LongType` (64-bit).

Both are **non-cryptographic** and intended for partitioning/bucketing, not password hashing.

### 3.18 F.conv Function

**Behavior**: `F.conv("FF", 16, 10)` converts hexadecimal `FF` to decimal `255`.

**Return Type**: Always `StringType` (e.g., `"255"`).

### 3.19 F.unhex Function

**Behavior**: Interprets each pair of hexadecimal digits in the input string as a byte.

**Return Type**: `BinaryType` (inverse of `F.hex(col)`).

### 3.20 Delta overwriteSchema Option

**Behavior**: By default, Delta raises an `AnalysisException` when the write schema does not match the existing table schema.

**Fix**: Add `.option("overwriteSchema", "true")` to allow the schema to be replaced.

### 3.21 schema.simpleString vs schema.toDDL

**Difference**:
- **`simpleString()`**: Compact internal representation like `struct<id:int,name:string>`
- **`toDDL()`**: SQL DDL-compatible string like `` `id` INT,`name` STRING `` suitable for `CREATE TABLE` statements

### 3.22 F.to_csv Function

**Behavior**: Serializes each struct value to a `StringType` CSV-formatted string with fields in struct schema order.

### 3.23 df.na.fill(value, subset=cols)

**Behavior**: Replaces null values with `value` **only** in the specified `subset` columns.

### 3.24 F.sort_array vs F.array_sort Null Handling

**Null Placement**:
- **`sort_array(col, asc=True)`**: Places nulls **at the beginning** in ascending-sorted result.
- **`array_sort(col)`**: Places nulls **at the end** in ascending-sorted result.

Both sort non-null elements in ascending order.

### 3.25 F.reverse Polymorphism

**Behavior**:
- On `StringType`: Reverses the characters of the string.
- On `ArrayType`: Reverses the order of array elements.

Return type matches input type.

### 3.26 F.format_string Function

**Syntax**: `F.format_string(fmt, *cols)`

Applies `printf`-style formatting (e.g., `%s`, `%d`, `%f`) with column values substituted left-to-right.

`F.format_string("%s has %d items", name_col, count_col)` → formatted `StringType` column.

### 3.27 CSV nullValue vs emptyValue Options

**Distinction**:
- **`nullValue`** (default `""`): String written for `NULL` column values.
- **`emptyValue`** (default `""`): String written for empty (zero-length) `StringType` values.

Semantically different: a database `NULL` ≠ empty string.

### 3.28 F.soundex Function

**Purpose**: Returns Soundex phonetic code for string matching.

`soundex("Smith")` and `soundex("Smyth")` both return `"S530"`, enabling fuzzy name matching.

### 3.29 F.assert_true Function (Spark 3.1+)

**Behavior**:
- Returns `NULL` for rows where condition is `true`.
- Raises `RuntimeException` for rows where condition is `false` or `NULL`.

Used inside `df.select()` for inline data quality validation with low overhead (native Catalyst expression, not Python UDF).

### 3.30 df.offset(n) Function (Spark 3.4+)

**Purpose**: Skips the first `n` rows, equivalent to SQL `OFFSET n` clause.

Useful for pagination in combination with `df.limit()`.

---

## Topic 4: Troubleshooting & Tuning

### 4.1 Arrow Columnar Format for Python

**Option**: `spark.sql.execution.arrow.pyspark.enabled = true`

**Benefit**: Uses Apache Arrow columnar format for JVM↔Python data transfer in:
- `toPandas()`
- `createDataFrame(pandas_df)`
- Pandas UDFs

Significantly reduces serialization overhead.

**Requirement**: PyArrow must be installed in the Python environment.

### 4.2 Column Pruning vs Predicate Pushdown

**Distinction**:
- **Column Pruning**: Removes unreferenced columns from the query plan early, reducing I/O and memory.
- **Predicate Pushdown**: Moves row-level filters as close to the data source as possible, reducing rows read.

Complementary optimizations: a query can benefit from both simultaneously.

### 4.3 spark.sql.broadcastTimeout

**Default**: 300 seconds

**Purpose**: How long the driver waits for each executor to **acknowledge receipt** of a broadcast variable over the network.

**When to Increase**: When executors are slow to start or the broadcast payload is very large and takes time to fetch over a slow network.

### 4.4 spark.task.cpus Configuration

**Setting**: `spark.task.cpus=2`

**Effect**: Tells Spark each task requires 2 CPU cores; an 8-core executor runs only 4 concurrent tasks instead of 8.

**Use Case**: Tasks that use multi-threaded native libraries requiring multiple cores.

### 4.5 spark.sql.optimizer.maxIterations

**Default**: 100

**Behavior**: Catalyst applies optimisation rules in fixed-point batches. If the plan doesn't stabilise within `maxIterations`, Spark **logs a warning** and proceeds with the best plan produced so far (does NOT throw an error).

For very complex queries, increasing the limit may yield a better optimised plan.

### 4.6 spark.sql.files.ignoreMissingFiles

**Behavior**: Allows a query to proceed without error when input files are missing or deleted between planning and execution.

**Use Case**: Data lakes with concurrent compaction jobs that may delete or move files.

### 4.7 spark.shuffle.file.buffer

**Default**: 32 KB

**Purpose**: Sets the in-memory write buffer size for each shuffle output file written by a mapper task.

Increasing it reduces the number of `write()` syscalls and improves sequential disk write throughput.

### 4.8 Off-Heap Memory Configuration

**Enable**:
```python
spark.memory.offHeap.enabled = true
spark.memory.offHeap.size = <bytes>
```

**Benefits**:
- Allocates storage/execution memory **outside the JVM heap**, reducing GC pressure.
- Not subject to JVM garbage collection (allocated directly from OS memory).

**NOT** counted toward `spark.memory.fraction` because it's outside the JVM heap.

### 4.9 spark.sql.execution.sortBeforeRepartition

**Default**: `true`

**Behavior**: Sorts each map-side partition by the repartition key before writing shuffle files.

**Benefit**: Improves data locality for downstream stages that sort or range-partition on the same key, reducing the sort cost in the next stage.

### 4.10 AQE Partition Coalescing

**Feature**: AQE automatically merges small post-shuffle partitions into larger ones.

**Configuration**:
- **`spark.sql.adaptive.advisoryPartitionSizeInBytes`** (default 64 MB): Target merged size.
- **`spark.sql.adaptive.coalescePartitions.minPartitionNum`** (default 1): Lower bound on resulting partition count.

Addresses the problem of 2,000 small shuffle partitions causing excessive task scheduling overhead.

---

## Topic 5: Structured Streaming

### 5.1 trigger(once=True) vs trigger(availableNow=True) (Spark 3.3+)

**Difference**:
- **`trigger(once=True)`**: Processes **all available data in a single mega-batch**, then stops. May cause memory issues for large backlogs.
- **`trigger(availableNow=True)`**: Processes all available data across **multiple micro-batches** (respecting per-batch limits like `maxFilesPerTrigger`), then stops. Better parallelism, fault tolerance, and memory efficiency.

### 5.2 inputRowsPerSecond Metric

**Definition**: Rate of rows **ingested from the source** during the last micro-batch interval, calculated as `rows / batch_duration_seconds`.

Not a cumulative metric or theoretical maximum; refreshed per micro-batch.

### 5.3 Streaming File Source Schema Inference

**Behavior**: Streaming file sources **do not support** schema inference.

Spark raises an `AnalysisException` if no explicit schema is provided. An explicit schema is **mandatory** for streaming file reads.

### 5.4 Console Sink Characteristics

**Features**:
- Writes each micro-batch's output to driver **stdout**.
- Intended for development and testing only (not production).
- Supports all three output modes: `append`, `update`, `complete`.
- **NOT durable**: Does not support checkpoint-based recovery across restarts.

### 5.5 Watermark Late Data Handling

**Example**:
- Event with `event_time = 10:03` arrives at processing time `10:20`.
- Watermark at processing time `10:20` ≈ `10:20 − 5 min = 10:15`.
- Window `[10:00, 10:10)` is finalized (end time 10:10 is before watermark 10:15).
- Late event (event_time 10:03) is **silently dropped**.

### 5.6 session_window Function (Spark 3.2+)

**Purpose**: Defines a **dynamic session window** based on inactivity gaps.

A new session starts when no event is observed within the timeout (e.g., 30 minutes) after the last event in the current session.

Window boundaries are **not fixed in advance**; they depend on event arrival patterns.

### 5.7 Kafka Source Schema

**Fixed Schema**:
- `key`: `BinaryType`
- `value`: `BinaryType`
- `topic`: `StringType`
- `partition`: `IntegerType`
- `offset`: `LongType`
- `timestamp`: `TimestampType`
- `timestampType`: `IntegerType`

Deserialization of key/value is left to the application.

### 5.8 kafka.group.id Option

**Recommendation**: **Do NOT set** this option.

When set, Spark reuses that consumer group ID, which can conflict with Spark's internal checkpoint-based offset management. Spark generates a unique group ID per query when not set, ensuring clean offset management.

### 5.9 maxOffsetsPerTrigger Option

**Purpose**: Caps the number of Kafka messages processed per micro-batch trigger.

Primary throttle preventing the streaming query from consuming an unbounded backlog in one batch, protecting downstream sinks from being overwhelmed.

### 5.10 flatMapGroupsWithState Features

**Capabilities**:
- Emits **zero or more** output rows per group invocation (unlike `mapGroupsWithState` which emits exactly one).
- Supports timeout mechanisms (`ProcessingTimeTimeout` or `EventTimeTimeout`) to trigger function for idle groups.
- Requires output mode `append` or `update` (NOT `complete`).
- State is persisted in the streaming checkpoint and survives query restarts.

---

## Topic 6: Spark Connect

### 6.1 Analysis Exception Error Surfacing

**Timing**: Analysis errors (e.g., referencing non-existent column) are surfaced **when an action** (`collect()`, `show()`, `count()`) is called.

The logical plan is sent to the Spark Connect server only at action time; the server performs analysis and returns any errors to the client.

### 6.2 Token-Based Authentication

**Method**: Embed token in connection URL using semicolon-separated parameters:
```python
SparkSession.builder.remote("sc://host:15002/;token=my_token").getOrCreate()
```

### 6.3 Spark Connect Without JVM

**Advantage**: You can run `from pyspark.sql import SparkSession` on a machine **without Java installed**, then connect to a remote Spark Connect server to execute queries.

This is a key advantage over classic PySpark (which requires a local JVM).

### 6.4 UDF Handling in Spark Connect

**Serialization**:
- UDFs registered via `spark.udf.register()` are **serialized and sent to the server** for execution.
- External Python libraries must be available on the **executor environment** (e.g., via `--py-files`), not just the client machine.
- **Python UDFs are fully supported** in Spark Connect; only `SparkContext` / RDD APIs are unavailable.
- **Arrow-optimized Pandas UDFs** (`@pandas_udf`) are supported via Spark Connect using Apache Arrow for data serialization.

### 6.5 Spark Connect Server Crash Impact

**Behavior**: An in-progress query is **lost**; the client must reconnect and re-submit.

The client Python process itself does **NOT crash** when the server crashes — it receives a connection error. No automatic query replay occurs unless the application implements it.

---

## Topic 7: Pandas API on Spark

### 7.1 Caching Pandas-on-Spark DataFrame

**Method**: `psdf.spark.cache()`

The `.spark` accessor provides a bridge to native Spark DataFrame operations. Caches the underlying Spark DataFrame and returns a new pandas-on-Spark DataFrame backed by the cached data.

### 7.2 psdf.spark.explain()

**Output**: Prints the **Spark physical execution plan** for the underlying Spark DataFrame (identical to `psdf.to_spark().explain()`).

Useful for diagnosing performance issues from within the Pandas API on Spark.

### 7.3 default_index_type Options

**Default**: `"distributed-sequence"`

**Options**:
- **`"distributed-sequence"`** (default): Monotonically increasing per-partition integers without a global sort (fast, but not strictly globally ordered).
- **`"sequence"`**: Triggers a global sort; strictly globally ordered but slow.
- **`"distributed"`**: Fastest but produces non-contiguous values per partition.

### 7.4 Writing Pandas-on-Spark to Delta

**Both Valid**:
```python
# Option A: Convenience method
psdf.to_delta("/path/to/delta_table")

# Option B: Via Spark DataFrame
psdf.to_spark().write.format("delta").save("/path/to/delta_table")
```

### 7.5 Missing Value Representation

**Key Difference from Native Pandas**:
- Native pandas: `None` and `float('nan')` both treated as missing for numeric columns.
- Pandas-on-Spark: Missing values = Spark SQL `NULL` internally; `NaN` in float columns is a **distinct non-null value**.

**Consequence**:
- `psdf.dropna()` drops rows with Spark SQL `NULL` but does **NOT** drop `NaN` float values.
- `psdf.isna()`/`psdf.isnull()` return `True` for `NULL` but `False` for `NaN`.
- `psdf.fillna(0)` fills Spark `NULL` values but does **NOT** fill `NaN` float values.

---

**End of Study Guide (Iteration 5)**

Use this guide alongside the QUICK_REFERENCE_ITER5.md and PRACTICE_STRATEGY_ITER5.md for comprehensive exam preparation.
