# Databricks Certified Associate Developer for Apache Spark — Iteration 4 Study Guide

**Comprehensive study guide for exam questions (Iteration 4)**

**Last Updated**: May 17, 2026

---

## Table of Contents

1. [Topic 1: Apache Spark Architecture & Internals](#topic-1-apache-spark-architecture--internals)
2. [Topic 2: Spark SQL](#topic-2-spark-sql)
3. [Topic 3: DataFrame API](#topic-3-dataframe-api)
4. [Topic 4: Troubleshooting & Tuning](#topic-4-troubleshooting--tuning)
5. [Topic 5: Structured Streaming](#topic-5-structured-streaming)
6. [Topic 6: Spark Connect](#topic-6-spark-connect)
7. [Topic 7: Pandas API on Spark](#topic-7-pandas-api-on-spark)

---

## Topic 1: Apache Spark Architecture & Internals

### 1.1 Submitting Applications: spark-submit Flags

**`--py-files` vs `--files` vs `--jars` vs `--packages`**:
- **`--py-files`**: Distributes `.py`, `.egg`, or `.zip` files to executors and adds them to the Python path. Use for utility modules.
- **`--files`**: Distributes arbitrary files (CSV, JSON, config) to all executors. Files are available locally in the executor working directory but NOT added to the Python path.
- **`--jars`**: Distributes JAR files to all executors and adds them to the classpath.
- **`--packages`**: Specifies Maven coordinates (e.g., `org.apache.hadoop:hadoop-aws:3.2.0`) for automatic download and dependency resolution.

**Example**:
```bash
spark-submit \
  --py-files s3://bucket/myutils.zip \
  --files /local/config.json \
  --jars /local/custom.jar \
  --packages org.apache.hadoop:hadoop-aws:3.2.0 \
  app.py
```

### 1.2 Cluster Managers & Deployment Modes

**YARN Cluster Mode**:
- Client submits the application to the YARN ResourceManager.
- ResourceManager allocates a container for the **ApplicationMaster**.
- The ApplicationMaster (running on a worker node) launches the Spark Driver inside its own JVM.
- The client detaches after submission; the ApplicationMaster manages the driver lifecycle.

**Key Port Numbers**:
- **4040**: Live Spark application UI (driver web UI)
- **7077**: Spark Standalone Master RPC port (for cluster communication)
- **8080**: Spark Standalone Master web UI (cluster manager UI)
- **18080**: Spark History Server (displays completed application UIs)

### 1.3 Driver Memory Configuration

**`spark.driver.maxResultSize`**:
- Controls the **total serialized size of all task results** that can be collected back to the driver (via `collect()`, `take()`, etc.).
- Default: 1 GB
- If `df.collect()` produces results larger than this threshold, Spark throws a `SparkException`.
- Does NOT limit driver heap size (use `spark.driver.memory` for that).

**Example**:
```python
spark.conf.set('spark.driver.maxResultSize', '4g')  # Allow up to 4 GB of results
df.collect()  # Now supports larger result sets
```

### 1.4 RDD Partitioning & Partitioners

**`HashPartitioner`**:
- For a PairRDD, `rdd.partitionBy(new HashPartitioner(10))` assigns key `k` to partition `abs(k.hashCode()) % numPartitions`.
- All keys with the same hash code land on the same partition.
- Enables efficient lookups and co-locations in subsequent operations (e.g., `join()`, `groupByKey()`).

**`groupByKey()` Partitioner**:
- When `rdd.groupByKey()` is called without an explicit partitioner, Spark applies a shuffle.
- The resulting RDD is attached with a **`HashPartitioner(spark.default.parallelism)`** (e.g., `HashPartitioner(200)` in typical cluster configurations).
- This partitioner is accessible via `rdd.partitioner` property.

### 1.5 Storage Level Replication

**`MEMORY_ONLY_2`** vs **`MEMORY_ONLY`**:
- **`MEMORY_ONLY`**: Single copy of each partition cached in memory on one executor.
- **`MEMORY_ONLY_2`**: **Two replicated copies** of each partition in memory on **two different executors**.
- The `_2` suffix provides in-memory fault tolerance: if one executor fails, the cached data is still available from another executor.
- Useful for critical, frequently-reused DataFrames in production clusters.

### 1.6 Task Retry & Failure Handling

**`spark.task.maxFailures`**:
- Default: 4
- Controls how many times a single task can fail before Spark aborts the entire stage/job.
- If a task fails due to network errors, deserialization issues, or other transient issues, Spark retries.
- Once exceeded, the whole job terminates with failure.

### 1.7 Parquet Partition Size Tuning

**`spark.sql.files.maxPartitionBytes`**:
- Default: 128 MB
- When reading file-based sources (Parquet, ORC, CSV), Spark calculates split boundaries to keep partitions roughly below this threshold.
- Smaller values → more partitions → finer parallelism but higher scheduling overhead.
- Larger values → fewer partitions → lower overhead but potentially uneven work distribution.

### 1.8 Dynamic Resource Allocation

**Bounds**:
- **`spark.dynamicAllocation.minExecutors`**: Minimum number of executors Spark maintains (even if idle).
- **`spark.dynamicAllocation.maxExecutors`**: Maximum number of executors Spark can allocate on demand.

**Example**:
```python
spark.conf.set('spark.dynamicAllocation.enabled', 'true')
spark.conf.set('spark.dynamicAllocation.minExecutors', 2)
spark.conf.set('spark.dynamicAllocation.maxExecutors', 100)
```

Executors are added when pending tasks accumulate; removed when idle for a time (default 60 s).

### 1.9 Executor Memory Breakdown

**Spark Memory Hierarchy**:
1. **Total Executor Memory** = `spark.executor.memory` (e.g., 4 GB)
2. **Reserved System Memory** = 300 MB (hard-coded)
3. **Available Memory for Spark** = Total − Reserved = 3.7 GB
4. **Divided by `spark.memory.fraction`** (default 0.6):
   - **Execution Memory** = 3.7 × 0.6 = 2.22 GB (shuffle buffers, sort space)
   - **Storage Memory** = 3.7 × 0.4 = 1.48 GB (caches, broadcasts)

**Execution-Storage Borrowing**:
- When Execution memory exhausts, Spark can borrow from Storage.
- Storage blocks are evicted as needed; they can be recomputed.

### 1.10 Shuffle Spill & Write Amplification

**When does shuffle spill to disk?**:
- The in-memory shuffle buffer (execution memory) for a reducer fills up.
- Memory pressure: Spark cannot borrow sufficient memory from Storage pool because it's also occupied.
- Both conditions describe the same scenario from different perspectives.

**Mitigation**:
- Increase `spark.executor.memory` or executor core count.
- Reduce `spark.shuffle.partitions` to increase bytes per partition, reducing spill frequency.
- Use `repartition()` earlier to redistribute data more evenly.

### 1.11 Warehouse Directory

**`spark.sql.warehouse.dir`**:
- Default: `${system:user.dir}/spark-warehouse` (i.e., `spark-warehouse` subdirectory of the current working directory).
- Stores managed table data when tables are created without an explicit `LOCATION`.
- Paths can be set to HDFS or cloud storage for production.

```python
spark.conf.set('spark.sql.warehouse.dir', 's3://my-bucket/spark-warehouse')
```

### 1.12 Spark Thrift Server

**Purpose**:
- HiveServer2-compatible JDBC/ODBC gateway.
- Allows BI tools (Tableau, Looker) and SQL clients (DBeaver, SQL clients) to connect via standard SQL drivers.
- Translates JDBC/ODBC requests into Spark SQL execution.

**Starting the Thrift Server**:
```bash
$SPARK_HOME/sbin/start-thriftserver.sh
# Listen on localhost:10000 by default
```

Clients connect via JDBC URL: `jdbc:hive2://localhost:10000`

### 1.13 Stage Boundaries & Shuffles

**Narrow Transformations** (no stage boundary):
- `filter()`, `map()`, `select()`, `withColumn()`
- Each partition's input depends on one input partition → no shuffle.

**Wide Transformations** (create stage boundary):
- `repartition()`, `groupByKey()`, `join()`, `aggregation()`
- Cause a full shuffle exchange; DAGScheduler inserts a new stage boundary.

**`coalesce(n)` Edge Case**:
- `coalesce()` is narrow when **reducing** partition count (no shuffle).
- `coalesce()` triggers a shuffle if **increasing** partition count.
- `repartition()` always shuffles.

### 1.14 File Open Cost

**`spark.sql.files.openCostInBytes`**:
- Default: ~4 MB
- Adds a per-file overhead estimate when computing partition splits.
- **Purpose**: Biases Spark toward co-locating small files into the same partition to amortise file open overhead.
- Without this, Spark might create one partition per small file, leading to excessive task overhead.

**Example**:
- Reading 1000 small 1 MB files from S3.
- With `openCostInBytes = 4MB`, Spark groups small files into partitions to avoid 1000 tiny tasks.

### 1.15 Hive Metastore Persistence

**Managed vs External Tables**:
- **Managed Tables**: Data physically stored in `spark.sql.warehouse.dir`. On `DROP TABLE`, both metadata AND data are deleted.
- **External Tables**: Data stored outside the warehouse (e.g., S3, HDFS). On `DROP TABLE`, metadata is deleted but data persists on disk.

**Cross-Session Persistence**:
- Tables registered in a Hive metastore persist across Spark session restarts.
- `spark.table('db.my_table')` retrieves the registered table in a new session.

**Temporary Views**:
- Created with `df.createOrReplaceTempView('name')` or `df.createTempView('name')`.
- Session-scoped; stored in memory, NOT in the Hive metastore.
- Dropped when the session ends.

### 1.16 Advanced Executor Management

**`TaskSetManager` Role**:
- Tracks success/failure/pending state of every task in a stage.
- Implements retry logic (up to `spark.task.maxFailures`).
- Handles **locality-aware task scheduling**: tries to launch tasks on nodes with cached data or task input.

**`spark.executor.extraJavaOptions`**:
- Passes additional JVM flags to the executor JVM at launch.
- Used for GC tuning (e.g., `-XX:+PrintGCDetails`), diagnostic agents, or custom JVM options.

**Heartbeat & Network Timeout**:
- **`spark.executor.heartbeatInterval`** (default 10 s): Executors send heartbeats to the driver.
- **`spark.network.timeout`** (default 120 s): Driver waits this long before declaring an executor dead.
- **Requirement**: `heartbeatInterval << networkTimeout` (e.g., 10 s << 120 s).
- If `heartbeatInterval` is too close to `networkTimeout`, normal heartbeat delays can cause false "executor dead" detection.

---

## Topic 2: Spark SQL

### 2.1 String Functions

**`regexp_extract(col, pattern, groupIdx)`**:
- Extracts the capture group at position `groupIdx` from the first regex match.
- `groupIdx = 0`: Returns the entire match.
- `groupIdx = 1, 2, ...`: Returns specific capture groups.

```python
import pyspark.sql.functions as F
df = spark.createDataFrame([('foo123bar',)], ['text'])
df.withColumn('digits', F.regexp_extract(F.col('text'), r'(\d+)', 1)).show()
# Output: '123'
```

**`instr(str, substr)`**:
- Returns the **1-based position** of the first occurrence of `substr` in `str`.
- Returns **0** if not found.
- Never returns `null` for non-null inputs (returns 0 if not found).

**`translate(str, matchingString, replaceString)`**:
- Replaces each character in `str` that appears in `matchingString` with the corresponding character in `replaceString`.
- Case-sensitive; character-by-character mapping.

```python
F.translate(F.lit('Hello'), F.lit('aeiou'), F.lit('*'))
# 'e' → '*', 'o' → '*' (matching chars in 'aeiou' replaced by '*')
# Result: 'H*ll*'
```

**`substring_index(str, delim, count)`**:
- Splits the string by delimiter and returns the first `count` segments.
- Negative `count`: returns segments from the right.

```python
F.substring_index(F.lit('a.b.c.d'), F.lit('.'), 2)  # 'a.b'
F.substring_index(F.lit('a.b.c.d'), F.lit('.'), -2)  # 'c.d'
```

**`overlay(base, insert, pos)`**:
- Replaces a substring of `base` starting at position `pos` with `insert`.
- Position is 1-based.

```python
F.overlay(F.lit('Spark SQL'), F.lit('DataFrame'), 7)
# Start at position 7, replace: 'Spark DataFrame' (first 6 chars kept, rest replaced)
```

### 2.2 Date & Time Functions

**`add_months(date_col, months)`**:
- Adds `months` calendar months to `date_col`.
- Handles month-end edge cases (e.g., Jan 31 + 1 month = Feb 28/29).

**`date_trunc(unit, date_col)`**:
- Truncates `date_col` to the specified unit.
- Units: `'year'`, `'quarter'`, `'month'`, `'week'`, `'day'`, etc.

```python
F.date_trunc('month', F.lit('2024-07-15'))  # '2024-07-01'
```

**`to_utc_timestamp(ts_col, timezone)`**:
- Interprets `ts_col` as a **local timestamp in the specified timezone** and converts it to **UTC**.
- Example: `ts_col = '2024-01-15 12:00:00'` (interpreted as EST) → converts to `'2024-01-15 17:00:00'` UTC (EST is UTC-5).

**`from_unixtime(unix_ts_col)`**:
- Converts Unix epoch seconds (LongType) to a `StringType` formatted as `'yyyy-MM-dd HH:mm:ss'` in the **session local timezone**.

### 2.3 Array & Map Functions

**`arrays_overlap(array1, array2)`**:
- Returns `true` if the two arrays share at least one common element.

```python
F.arrays_overlap(F.array(1, 2, 3), F.array(3, 4, 5))  # true (element 3 is common)
```

**`map_from_arrays(keys_array, values_array)`**:
- Constructs a `MapType` from two equal-length arrays.

```python
F.map_from_arrays(F.array('a', 'b'), F.array(1, 2))  # map('a', 1, 'b', 2)
```

**`map_concat(map1, map2, ...)`**:
- Merges multiple maps left-to-right.
- When keys overlap, **right map wins** (rightmost value overwrites leftmost).

**`format_number(value, decimal_places)`**:
- Formats a number with thousands separators and fixed decimal places.
- Returns `StringType`.

```python
F.format_number(1234567.891, 2)  # '1,234,567.89'
```

### 2.4 Window Functions & RANGE vs ROWS

**`ROWS BETWEEN ... AND ...`**:
- Based on **physical row offsets**.
- `ROWS BETWEEN 1 PRECEDING AND CURRENT ROW`: The previous row + current row (2 rows).

**`RANGE BETWEEN ... AND ...`**:
- Based on **logical value distance** from the current row's ORDER BY value.
- When ORDER BY column has duplicate values, multiple rows can fall within the RANGE.

```sql
-- Example: Price column has duplicates
RANGE BETWEEN 1 PRECEDING AND CURRENT ROW
-- If current row price = 100, includes all rows with price in [99, 100]
```

### 2.5 Set Operations: EXCEPT & INTERSECT

**`EXCEPT DISTINCT`** (or simply `EXCEPT`):
- Returns rows in the **left relation that do NOT exist in the right relation**.
- Deduplicates the result.

**`EXCEPT ALL`**:
- Removes one occurrence of each matching row per occurrence in the right relation.
- Preserves extra duplicates.

```sql
-- Left: 1, 1, 1, 2
-- Right: 1, 3
-- EXCEPT DISTINCT: 2
-- EXCEPT ALL: 1, 1, 2 (one '1' matched and removed)
```

**`INTERSECT ALL`**:
- Returns the intersection of two relations, preserving duplicates **up to the minimum count** in both sides.

### 2.6 Aggregate Operations

**`ROLLUP(col1, col2)`**:
- Produces **multiple grouping sets** with subtotals at different aggregation levels.
- Sets: `(col1, col2)`, `(col1)`, `()` (grand total).
- Super-aggregate rows have `NULL` in the non-grouped columns; use `GROUPING()` to distinguish from actual `NULL` data.

**`CUBE(col1, col2)`**:
- Produces all **2^n** combinations of grouping columns.
- For `CUBE(col1, col2)`: sets are `(col1, col2)`, `(col1)`, `(col2)`, `()`.

### 2.7 TABLESAMPLE & SQL Features

**`TABLESAMPLE (10 PERCENT)`**:
- Randomly samples approximately 10% of rows from a table.
- **Approximate**: actual percentage may vary.

```sql
SELECT * FROM t TABLESAMPLE (10 PERCENT)
```

**`QUALIFY` Clause** (Spark 3.4+):
- Filters rows **after** window functions are evaluated.
- Eliminates need for subqueries with window functions.

```sql
SELECT * FROM employees
QUALIFY RANK() OVER (PARTITION BY dept ORDER BY salary DESC) = 1
-- Returns the highest-salary employee per department
```

### 2.8 Data Type Functions

**`size(array_col)`**:
- Returns the length of the array.
- **Spark 3.0+**: Returns `null` if `array_col` is `null` (legacy behavior returns `-1` with `spark.sql.legacy.sizeOfNull=true`).

**`instr()` Return Type**:
- Returns `IntegerType` (1-based position or 0).
- The return value is always non-null for non-null inputs.

---

## Topic 3: DataFrame API

### 3.1 Column Reference Ambiguity

**Ambiguous Column References After Join**:
- After `df1.join(df2, ...)`, if both DataFrames have a column named `'name'`:
  - `F.col('name')` **without a DataFrame qualifier** → `AnalysisException: Reference is ambiguous`
  - `df1['name']` or `df1.name` → Correctly references the column from `df1` **if both sides have the same name**; still ambiguous without clarification in some contexts.
- **Safe approach**: Use `df1.col('name')` or explicitly alias columns before join.

### 3.2 Write Operations

**Parquet Compression**:
```python
df.write.option('compression', 'snappy').parquet('/output')
# Not: .option('codec', 'snappy')  ← wrong key for Parquet
```

**CSV Headers**:
```python
# Default: headers NOT written
df.write.option('header', True).csv('/output')
```

**Write Text Files**:
- Requires exactly **one column of `StringType`**.
- All other types must be explicitly cast to string first.

**`maxRecordsPerFile`**:
- Limits rows per output file.

```python
df.write.option('maxRecordsPerFile', 100000).parquet('/output')
# Creates multiple files, each with up to 100K rows
```

### 3.3 Read Operations

**`pathGlobFilter`**:
- Restricts file scan to only files matching the glob pattern.
- Excludes `.crc`, `_SUCCESS`, and other non-data files.

```python
spark.read.option('pathGlobFilter', '*.parquet').parquet('/data')
```

**CSV `nullValue` Option**:
```python
spark.read.csv('/path', nullValue='N/A')
# Maps the literal string 'N/A' to null
```

**Schema Inference from Parquet**:
- Spark reads the schema embedded in the Parquet file footer (metadata block).
- Does NOT scan row data; fast and accurate.

### 3.4 DataFrame Broadcasting & Hints

**`F.broadcast()` Import**:
```python
from pyspark.sql.functions import broadcast
df_small_hinted = broadcast(df_small)
result = df_large.join(df_small_hinted, 'key', 'inner')  # Enforces BroadcastHashJoin
```

**`df.hint('repartition', 10)`**:
- Advisory hint; may be ignored by the optimizer.
- Requests a repartition to `n` partitions.

### 3.5 RDD Conversion Caveats

**`df.rdd` Returns**:
- An RDD of `Row` objects (NOT plain dicts or tuples).
- Fields accessible by name: `row.col_name` or by index: `row[0]`.
- Modern Spark still uses RDD internally, but DataFrame operations are preferred.

### 3.6 Column Replacement & withColumn

**`df.withColumn('existing_col', new_expr)`**:
- If `existing_col` already exists in `df`, it is **replaced in-place** with the result of `new_expr`.
- Does NOT create a duplicate column; does NOT raise an error.

### 3.7 Null Handling

**`F.coalesce(col1, col2, col3)`**:
- Returns the **first non-null value** from the provided columns (evaluated left-to-right).
- Standard null-safe fallback pattern.

```python
F.coalesce(F.col('email'), F.col('alternate_email'), F.lit('no-email'))
```

### 3.8 Set Operations

**`df1.exceptAll(df2)` vs `df1.subtract(df2)`**:
- **`exceptAll`**: Removes one matching row from `df1` per occurrence in `df2`; preserves extra duplicates.
- **`subtract`**: Removes **all** occurrences of any row present in `df2` (equivalent to `EXCEPT DISTINCT` in SQL).

### 3.9 DataFrame Creation & JDBC

**From Row Objects**:
```python
spark.createDataFrame([Row(a=1, b='x'), Row(a=2, b='y')])
# Schema inferred from Row field names and types
```

**JDBC Write Parameters**:
- `url`: JDBC connection string.
- `table`: Target table name.
- `mode`: Write mode (`overwrite`, `append`, etc.).
- `properties`: Dict with driver, user, password, etc.

```python
df.write.jdbc(url, 'target_table', mode='append', properties=props)
```

**JDBC Read with Parallelism**:
```python
spark.read.jdbc(url, 'table',
  numPartitions=10,
  partitionColumn='id',
  lowerBound=1,
  upperBound=1000000,
  properties=props)
# Creates 10 partitions with predicates on 'id' ranges
```

**Alternative with Predicates**:
```python
spark.read.jdbc(url, 'table',
  predicates=['id < 100000', 'id >= 100000 AND id < 200000', ...],
  properties=props)
# Custom WHERE clauses per partition
```

### 3.10 Pandas UDFs

**Decorator & Import**:
```python
from pyspark.sql.functions import pandas_udf
@pandas_udf('double')  # or explicit StructType
def my_udf(s: pd.Series) -> pd.Series:
    return s * 2
```

**Grouped Map UDF** (`applyInPandas`):
- Invoked once per group.
- Receives all rows for a group as a single `pd.DataFrame`.

```python
df.groupby('department').applyInPandas(process_group_df, schema=result_schema)
# process_group_df receives one DataFrame per department with all its employees
```

### 3.11 Caching & Lazy Evaluation

**`df.cache().count()`**:
- `cache()` is lazy; it marks the DataFrame for caching but does NOT materialize data.
- `count()` is an **action**; it forces execution and materializes the cached data in memory.

### 3.12 Schema Definition & Equality

**`StructType.fromDDL()`**:
```python
schema = StructType.fromDDL('id BIGINT, name STRING, amount DECIMAL(10, 2)')
df = spark.read.schema(schema).csv('/path')
```

**`StructType` Equality**:
- Two independently created `StructType` schemas with identical fields compare `==` as `True`.
- Uses **value-based equality**, not reference equality.

```python
schema1 = StructType.fromDDL('a INT, b STRING')
schema2 = StructType.fromDDL('a INT, b STRING')
schema1 == schema2  # True
```

### 3.13 DataFrame Operations

**`df.getNumPartitions()` Doesn't Exist**:
- Use `df.rdd.getNumPartitions()` or `len(df.rdd.partitions)`.

**Generic Load API**:
```python
# Using format parameter
df = spark.read.load('/data/events', format='delta')

# Using chained .format()
df = spark.read.format('delta').load('/data/events')

# Delta shortcut (Databricks only)
df = spark.read.delta('/data/events')  # Only in Databricks
```

**`selectExpr()` for SQL Expressions**:
```python
df.selectExpr('age * 2 AS double_age', 'name')
# Evaluates SQL expressions inline without importing functions
```

**`when()` Default Behavior**:
```python
F.when(F.col('x') > 0, 'positive').when(F.col('x') < 0, 'negative')
# No .otherwise() → returns null for unmatched rows (e.g., when x == 0)
```

### 3.14 DataFrame to Pandas API on Spark

**`sdf.to_pandas_on_spark()`**:
- Returns a `pyspark.pandas.DataFrame` (Pandas API on Spark).
- Keeps data distributed; does NOT collect to driver.

### 3.15 Coalesce vs Repartition for Output Files

**Key Difference**:
- **`coalesce(5)`**: Narrow transformation; merges existing partitions WITHOUT a shuffle. Fast for reducing partition count.
- **`repartition(5)`**: Wide transformation; performs a full shuffle to redistribute data evenly. Slower but ensures even distribution.

```python
# 100 partitions → 5 output files
df.coalesce(5).write.parquet('/output')  # No shuffle; may have uneven file sizes
df.repartition(5).write.parquet('/output')  # Full shuffle; balanced file sizes
```

### 3.16 Write Options

**Valid Parquet Write Options**:
- `compression` (e.g., `'snappy'`, `'gzip'`, `'zstd'`)
- `maxRecordsPerFile` (row limit per file)
- `partitionOverwriteMode` (e.g., `'dynamic'` for partition-level overwrites)

**Invalid for Parquet**:
- `header` (CSV-only)
- `mergeSchema` (Parquet read option or Delta write option, not plain Parquet write)

---

## Topic 4: Troubleshooting & Tuning

### 4.1 Broadcast Join Threshold

**Disabling Broadcast Joins**:
```python
spark.conf.set('spark.sql.autoBroadcastJoinThreshold', -1)
# Prevents automatic broadcast joins; use only when small tables are misidentified
```

### 4.2 Cost-Based Optimizer (CBO)

**Enable CBO**:
```python
spark.conf.set('spark.sql.cbo.enabled', 'true')
```

**Update Table Statistics**:
```sql
ANALYZE TABLE orders COMPUTE STATISTICS FOR ALL COLUMNS
-- Collects min, max, NDV (number of distinct values), null count per column
-- CBO uses these for join ordering and strategy selection
```

**Join Reordering**:
```python
spark.conf.set('spark.sql.cbo.joinReorder.enabled', 'true')
# Requires spark.sql.cbo.enabled = true
# Reorders multi-join chains to minimize data shuffled
```

### 4.3 In-Memory Caching

**Eager vs Lazy Cache**:
```sql
CACHE TABLE sales
-- Eager: Immediately scans and materialises the table

CACHE LAZY TABLE sales
-- Lazy: Marks for caching; materialization happens on first query
```

### 4.4 Adaptive Query Execution (AQE)

**Coalesce Partitions**:
- **`spark.sql.adaptive.advisoryPartitionSizeInBytes`** (default 64 MB): AQE's target partition size after post-shuffle coalescing.
- Advisory; AQE may not achieve exact target but aims for this range.

**Coalesce Min Partition Count**:
- **`spark.sql.adaptive.coalescePartitions.minPartitionNum`** (default 1): Lower bound on partition count after AQE coalesces.
- Prevents over-coalescing; setting to `1` allows collapsing all output to a single partition.

### 4.5 ORC vs Parquet

**When to Use ORC**:
- Native format for Apache Hive; excellent for Hive → Spark pipelines.
- Supports ORC-specific features (BloomFilters, stripe-level predicate pushdown).

**When to Use Parquet**:
- Better support in non-Hive ecosystems (Arrow, Python pandas).
- More mature in Spark ecosystem.

### 4.6 Join Strategy Selection

**SortMergeJoin Preference**:
```python
spark.conf.set('spark.sql.join.preferSortMergeJoin', 'true')
# Prefers SortMergeJoin over ShuffledHashJoin
# Does NOT affect BroadcastHashJoin
```

### 4.7 EXPLAIN Output Modes

**Modes**:
- **`formatted`**: Human-readable physical plan with stage boundaries.
- **`extended`**: All logical and physical plans.
- **`codegen`**: Shows generated JVM source code.
- **`cost`**: Includes CBO estimates (row count, data size per operator).

```python
df.explain('cost')  # Shows estimated row counts and sizes
```

### 4.8 Columnar Cache Compression

**In-Memory Columnar Storage**:
```python
spark.conf.set('spark.sql.inMemoryColumnarStorage.compressed', 'true')
# Default: true; enables Snappy compression on cached columnar data
# Reduces memory footprint at the cost of some CPU
```

---

## Topic 5: Structured Streaming

### 5.1 Trigger Types

**`trigger(once=True)`**:
- Processes all available source data in a **single micro-batch**.
- Automatically stops after completion.
- Useful for incremental batch processing in a scheduled job.

**`trigger(processingTime='30s')`**:
- Starts a new micro-batch every 30 seconds (if data is available).

**`trigger(continuous='1s')`**:
- Continuous mode (sub-millisecond latency target).
- No micro-batch boundaries; much more complex semantics.

### 5.2 Checkpoint Location

**Required for Fault Tolerance**:
```python
query = df_stream.writeStream \
  .option('checkpointLocation', '/path/to/checkpoint') \
  .start()
```

- Stores source offsets and sink commit log.
- On restart, Spark resumes from the last committed offset.
- Enables **exactly-once** guarantees.

### 5.3 Output Modes

**`append` Mode**:
- Emits only new rows added to the result table.
- Works for non-aggregated and aggregated streams.

**`update` Mode**:
- Emits rows whose values **changed or were newly created** since the last trigger.
- Smaller output footprint than `complete`.
- Does NOT re-emit unchanged rows.

**`complete` Mode**:
- Emits the **entire result table** on every trigger.
- Requires full aggregation; NOT supported for non-aggregated streams.

### 5.4 Streaming Limitations for Non-Aggregated Queries

**No `complete` Mode Without Aggregation**:
- `complete` mode requires accumulating the entire result table.
- For non-aggregated streams (append-only), `complete` is meaningless and raises `AnalysisException`.
- Valid modes: `append` and `update`.

### 5.5 Watermarks & State Management

**Window + Watermark**:
```python
df_stream.withWatermark('event_time', '10 minutes') \
  .groupBy(F.window(F.col('event_time'), '5 minutes')) \
  .agg(F.sum('value'))
```

- Watermark tracks progress; when watermark passes window end time, the window is finalized and state is dropped.
- In `append` mode, results for a window are emitted only **after the watermark advances past the window's end time**.

### 5.6 Advanced Streaming Patterns

**`foreachBatch(func)`**:
- Receives each micro-batch as a **complete static DataFrame** (plus batch ID).
- Enables arbitrary multi-sink writes, deduplication, or unsupported operations.

```python
def write_to_multiple_sinks(batch_df, batch_id):
    batch_df.write.mode('append').saveAsTable('delta_table')
    batch_df.write.mode('append').option('url', '...').jdbc(...)

query = df_stream.writeStream.foreachBatch(write_to_multiple_sinks).start()
```

**Kafka `failOnDataLoss` Option**:
```python
spark.readStream \
  .option('kafka.bootstrap.servers', '...') \
  .option('subscribe', 'events') \
  .option('failOnDataLoss', False) \
  .load()
# Silently skips Kafka offsets no longer available (data retention expired)
# Instead of failing the query
```

**Query Progress Monitoring**:
```python
query.recentProgress  # List of dicts; each dict is one micro-batch progress report
query.status  # Current state (ACTIVE, TERMINATED, ERROR)
```

**Streaming Query Listener**:
```python
from pyspark.sql.streaming import StreamingQueryListener

class MyListener(StreamingQueryListener):
    def onQueryStarted(self, event): ...
    def onQueryProgress(self, event): ...
    def onQueryTerminated(self, event): ...

spark.streams.addListener(MyListener())
# Monitors all active streaming queries cluster-wide
```

---

## Topic 6: Spark Connect

### 6.1 Connection Setup

**Explicit Connection**:
```python
from pyspark.sql import SparkSession
session = SparkSession.builder.remote('sc://localhost:15002').getOrCreate()
```

**Environment Variable**:
```bash
export SPARK_REMOTE=sc://localhost:15002
# Python code can then use:
session = SparkSession.builder.getOrCreate()  # Auto-connects to SPARK_REMOTE URL
```

### 6.2 Data Serialization

**Apache Arrow**:
- Spark Connect uses **Apache Arrow columnar format** for data transfer over gRPC.
- Avoids Java/Kryo serialization overhead.
- Efficient for columnar data and client-side processing.

### 6.3 Session Proxy & Server-Side Execution

**Client-Side Proxy**:
```python
session = SparkSession.builder.remote('sc://...').getOrCreate()
# This is a proxy object representing the remote connection

session.getActiveSession() == session  # True; returns the proxy
# NOT the server-side session (server session is not marshalled back)
```

**Plan Analysis**:
- Logical plan is built on the client.
- **Physical plan analysis and execution happen on the server**.
- Results are transferred back to the client over gRPC.

### 6.4 Databricks Serverless

**Builder Pattern**:
```python
from databricks.sdk.sql import get_workspace_by_id
session = get_workspace_by_id(...).get_query_execution_context().SparkSession
# OR use DatabricksSession
from databricks.sdk import DatabricksSession
session = DatabricksSession.builder.serverless().getOrCreate()
```

### 6.5 Spark Connect vs spark-submit

**Key Differences**:
- **Spark Connect**: Client code runs locally; server runs computation remotely. Multiple clients can share the same server session.
- **`spark-submit`**: Driver code runs on the cluster. Submissions are isolated.

**RDD APIs**:
- Spark Connect does NOT expose `SparkContext` or RDD APIs.
- DataFrame/SQL APIs only.

---

## Topic 7: Pandas API on Spark

### 7.1 SQL on Pandas DataFrames

**`ps.sql()` Query**:
```python
import pyspark.pandas as ps
psdf = ps.read_parquet('/path')
psdf.createOrReplaceTempView('temp_view')
result = ps.sql('SELECT * FROM temp_view WHERE col > 10')
```

### 7.2 Reading Data

**Multiple Valid Approaches**:
```python
# Direct Pandas API on Spark
psdf = ps.read_parquet('/path')

# Via Spark DataFrame
sdf = spark.read.parquet('/path')
psdf = sdf.pandas_api()  # Both A and C are valid
```

### 7.3 Row-wise Operations

**`apply(func, axis=1)`**:
- Row-wise application.
- `func` receives each row as a `pd.Series` with column names as the index.

```python
def double_row(row):
    return row * 2

psdf.apply(double_row, axis=1)  # Apply to each row
```

### 7.4 Rolling Windows

**`rolling(window_size).agg(func)`**:
- 3-row trailing rolling average.
- First two rows are `NaN` (insufficient preceding values).

```python
psdf['value'].rolling(3).mean()
# Row 0: NaN
# Row 1: NaN
# Row 2: mean(rows 0-2)
# Row 3: mean(rows 1-3)
```

### 7.5 Concatenation

**`ps.concat([psdf1, psdf2])`**:
- Default `axis=0`: Stack rows (append).
- `axis=1`: Join side-by-side by index.

```python
# axis=0 (default)
ps.concat([psdf1, psdf2])  # Rows from both DataFrames stacked

# axis=1 requires ops_on_diff_frames = True if DataFrames from different plans
ps.set_option('compute.ops_on_diff_frames', True)
ps.concat([psdf1, psdf2], axis=1)  # Columns joined by index
```

**`ignore_index` Option**:
```python
ps.concat([psdf1, psdf2], ignore_index=True)  # Reset the resulting index
```

---

**End of Study Guide (Iteration 4)**

Use this guide alongside the QUICK_REFERENCE_ITER4.md and PRACTICE_STRATEGY_ITER4.md for comprehensive exam preparation.
