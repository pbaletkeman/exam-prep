# Databricks Certified Associate Developer for Apache Spark
# STUDY GUIDE — Iteration 4

**Exam**: Databricks Certified Associate Developer for Apache Spark
**Iteration**: 4 | 100 Questions | 20 Easy / 60 Medium / 20 Hard
**Answer Types**: 78 single-answer / 22 multi-answer
**Topics**: Architecture (20%) · SQL (20%) · DataFrame (30%) · Troubleshooting (10%) · Streaming (10%) · Spark Connect (5%) · Pandas API (5%)

---

## TABLE OF CONTENTS

1. [Apache Spark Architecture & Internals](#topic-1-apache-spark-architecture--internals)
2. [Spark SQL](#topic-2-spark-sql)
3. [DataFrame API](#topic-3-dataframe-api)
4. [Troubleshooting & Tuning](#topic-4-troubleshooting--tuning)
5. [Structured Streaming](#topic-5-structured-streaming)
6. [Spark Connect](#topic-6-spark-connect)
7. [Pandas API on Spark](#topic-7-pandas-api-on-spark)

---

## TOPIC 1: Apache Spark Architecture & Internals

### 1.1 spark-submit Flags

| Flag | Purpose |
|------|---------|
| `--py-files` | Distributes `.py`, `.egg`, `.zip` modules to executors; adds them to the Python path |
| `--files` | Distributes arbitrary files to executors (no Python path registration) |
| `--jars` | Distributes Java JAR files to executors |
| `--packages` | Downloads Maven coordinates (includes transitive dependencies) |
| `--conf` | Sets a Spark configuration property at submission time |
| `--master` | Cluster manager URL (yarn, spark://, k8s://) |
| `--deploy-mode` | `client` (driver on submitter) or `cluster` (driver on worker) |
| `--num-executors` | Number of executors to request |
| `--executor-memory` | Memory per executor (e.g., `4g`) |
| `--executor-cores` | Cores per executor |
| `--driver-memory` | Memory for the driver JVM |

**Critical distinction**: When distributing a Python utility module that must be importable on executors, use `--py-files` (NOT `--files`). `--files` distributes files but does not register them on the Python path.

### 1.2 Deploy Modes and Cluster Managers

**YARN Deploy Modes:**
- **Client mode**: Driver runs on the machine that submitted the job. Useful for interactive sessions; ApplicationMaster runs on a worker node to negotiate resources.
- **Cluster mode**: Driver runs inside the ApplicationMaster container on a worker node. The submitting client detaches after submission. Better for production jobs since the driver is co-located with executors.

**YARN Architecture:**
```
Client → ResourceManager → ApplicationMaster (on NodeManager)
                                ↓
                    TaskManager / Executors (on NodeManager)
```

In YARN **cluster mode**, the Spark Driver runs inside the **ApplicationMaster container**, which the ResourceManager launches on a worker node.

**Standalone Cluster:**
- Master: listens on port **7077** (RPC), port **8080** (Web UI)
- Workers register with Master

**History Server:**
- Displays completed application UIs
- Listens on port **18080** by default
- Live application UI is on port **4040**

### 1.3 Partitioning and Partitioners

**HashPartitioner:**
- Assigns key `k` to partition: `abs(k.hashCode()) % numPartitions`
- Keys with the same hash always land on the same partition
- Called with: `rdd.partitionBy(HashPartitioner(10))`

**RangePartitioner:**
- Uses sampling to divide the key space into ranges
- Ensures roughly equal-sized partitions based on value distribution
- Used by `sortByKey()`

**`rdd.groupByKey()` → attaches `HashPartitioner(spark.default.parallelism)` to the result RDD**

After `groupByKey()`, `rdd.partitioner` returns `HashPartitioner(spark.default.parallelism)` — NOT None and not RangePartitioner.

**Partitioner Propagation:**
- Operations that preserve the key structure (e.g., `mapValues`, `flatMapValues`) preserve the parent's partitioner
- Operations that change keys (e.g., `map`, `flatMap`) lose the partitioner

### 1.4 Storage Levels

| Storage Level | Description |
|---------------|-------------|
| `MEMORY_ONLY` | Store as deserialized Java objects in JVM heap |
| `MEMORY_AND_DISK` | Spill to disk if memory runs out |
| `MEMORY_ONLY_SER` | Store serialized (more compact) in memory |
| `DISK_ONLY` | Store only on disk |
| `MEMORY_ONLY_2` | **Two replicated copies of each partition in memory across two different executors** |
| `MEMORY_AND_DISK_2` | Two replicated copies; spills to disk |
| `OFF_HEAP` | Store off-heap (requires two configs: enabled + size > 0) |

**`MEMORY_ONLY_2` key fact**: The `_2` suffix means **two replicated copies across two executors** — NOT serialized, NOT two tiers, NOT just two partitions.

### 1.5 Task Failures and Retries

- **`spark.task.maxFailures`** (default **4**): Maximum number of times a single task can fail before the job is aborted
- NOT `spark.task.maxRetries` (doesn't exist as shown)
- NOT `spark.executor.maxTaskFailures` or `spark.stage.maxTaskAttempts`

A task attempt counter starts at 1. If `maxFailures = 4`, the task can fail 4 times total before the stage/job is aborted.

### 1.6 File Partitioning Configurations

| Config | Default | Purpose |
|--------|---------|---------|
| `spark.sql.files.maxPartitionBytes` | 128 MB | **Target maximum size of each input partition when reading files** |
| `spark.sql.files.openCostInBytes` | ~4 MB | Per-file overhead cost to encourage co-location of small files |
| `spark.sql.shuffle.partitions` | 200 | Number of partitions for post-shuffle operations |
| `spark.default.parallelism` | cluster-dependent | Default partition count for RDD operations |

**`maxPartitionBytes`**: When reading a large Parquet file, this determines the target max size of each partition. Spark splits large files into chunks of this size.

**`openCostInBytes`**: Adds an estimated cost per file to account for file-open overhead, encouraging Spark to co-locate small files into the same partition. It does NOT limit partition size — it biases the cost model toward merging small files.

### 1.7 Dynamic Resource Allocation

| Config | Description |
|--------|-------------|
| `spark.dynamicAllocation.enabled` | Enable DRA |
| `spark.dynamicAllocation.minExecutors` | **Lower bound** on executor count |
| `spark.dynamicAllocation.maxExecutors` | **Upper bound** on executor count |
| `spark.dynamicAllocation.initialExecutors` | Starting number |
| `spark.dynamicAllocation.executorIdleTimeout` | Time to remove idle executor |
| `spark.dynamicAllocation.schedulerBacklogTimeout` | Time before requesting more executors |

**Bounds pair**: `spark.dynamicAllocation.minExecutors` AND `spark.dynamicAllocation.maxExecutors`.
NOT `lowerBound`/`upperBound`, NOT `minInstances`/`maxInstances`.

### 1.8 Executor Memory Architecture

```
Total Container Memory
    └── spark.executor.memoryOverhead (YARN overhead, for off-heap, native)
    └── spark.executor.memory (JVM heap)
            └── 300 MB (reserved for system/Spark internal overhead)
            └── Remaining heap (usable Spark memory)
                    ├── spark.memory.fraction × remaining = Unified Memory
                    │       ├── Execution Memory (shuffle, sort, aggregation)
                    │       └── Storage Memory (cache, broadcast)
                    └── (1 - spark.memory.fraction) = User Memory (UDFs, data structures)
```

**Key fact**: Spark internally reserves **300 MB** of the executor heap for system overhead. The remaining heap is then divided by `spark.memory.fraction` (default 0.6).

`spark.executor.memory` specifies the JVM heap size. System overhead deduction (300 MB) happens internally, not via `spark.executor.memoryOverhead` — that's for non-JVM memory.

### 1.9 Shuffle Spill

Spark writes spill files to disk during a shuffle when:
1. **The in-memory shuffle buffer (execution memory) for a reducer is full**
2. **Available execution memory is exhausted and cannot borrow from storage memory**

Both A and D in Q12 describe the same condition at different levels of abstraction.

Does NOT spill because of:
- `spark.reducer.maxSizeInFlight` (that's a fetch size limit for the network)
- `spark.sql.files.maxPartitionBytes` (that's an input partition size)

### 1.10 Warehouse Directory

`spark.sql.warehouse.dir` controls where managed table data is stored.
Default: **`spark-warehouse` in the current working directory** (i.e., `${system:user.dir}/spark-warehouse`).

NOT `hdfs:///tmp/spark-warehouse`, NOT `/user/hive/warehouse` (that's Hive's default, not Spark's).

### 1.11 Spark Thrift Server

- HiveServer2-compatible **JDBC/ODBC gateway**
- Allows BI tools (Tableau, Power BI) and SQL clients to connect to Spark SQL
- Standard SQL interface over JDBC/ODBC drivers
- NOT the History Server, NOT the REST Submission Server

### 1.12 Stage Boundaries

Stage boundaries are inserted by the DAGScheduler when there is a **wide transformation** (shuffle):

| Transformation | Shuffle? | Stage Boundary? |
|---------------|---------|----------------|
| `filter()` | No | No |
| `map()` | No | No |
| `select()` | No | No |
| `withColumn()` | No | No |
| `repartition()` | **Yes** | **Yes** |
| `coalesce()` | No (narrow) | No |
| `groupByKey()` | Yes | Yes |
| `join()` (non-broadcast) | Yes | Yes |

**`repartition()` triggers a full shuffle** → stage boundary.
**`coalesce()` is narrow** (no shuffle) → no stage boundary.

### 1.13 Hive Metastore Integration

When Spark is configured with a Hive metastore:
- **Tables persist across sessions** ✓
- **External table data survives `DROP TABLE`** ✓ (only metadata is dropped)
- **Managed table data is deleted from warehouse on `DROP TABLE`** ✓
- `spark.table('db.my_table')` can read a registered table ✓
- **Temporary views created with `createOrReplaceTempView` are NOT stored** in the Hive metastore (session-scoped only) ✗

### 1.14 TaskSetManager

The **TaskSetManager** is the internal Spark component that:
- Tracks which tasks in a Stage have **succeeded, failed, or are pending**
- Manages **retries** up to `spark.task.maxFailures`
- Implements **locality-aware** task launch (prefers PROCESS_LOCAL, then NODE_LOCAL, etc.)

NOT responsible for: converting logical plans to stages (DAGScheduler), allocating containers (cluster manager), or managing broadcast variables.

### 1.15 Executor JVM Options

| Config | Purpose |
|--------|---------|
| `spark.executor.extraJavaOptions` | Pass extra JVM flags to executor JVMs (e.g., `-XX:+PrintGCDetails`) |
| `spark.driver.extraJavaOptions` | Pass extra JVM flags to the driver JVM |
| `spark.executor.extraClassPath` | Extra classpath entries for executors |
| `spark.executor.extraLibraryPath` | Extra library path for executors |

### 1.16 Heartbeat vs Network Timeout

| Config | Default | Description |
|--------|---------|-------------|
| `spark.network.timeout` | 120 s | Master considers executor dead if no communication for this long |
| `spark.executor.heartbeatInterval` | 10 s | Frequency executors send heartbeats to the driver |

**Critical relationship**: `heartbeatInterval` must be significantly **less than** `network.timeout`. If heartbeats arrive every 10 seconds and the network timeout is 120 seconds, there is ample margin before a live executor is declared dead.

If `heartbeatInterval >= network.timeout`, the executor would be killed while still alive.

---

## TOPIC 2: Spark SQL

### 2.1 String Functions

| Function | Returns | Notes |
|----------|---------|-------|
| `regexp_extract(col, pattern, idx)` | String (capture group) | `idx=0` = full match; `idx=1` = first capture group |
| `regexp_replace(col, pattern, replacement)` | String | Replaces matches with replacement |
| `instr(str, substr)` | Int (1-based) | 0 if not found; never null for non-null inputs |
| `locate(substr, str[, pos])` | Int (1-based) | 0 if not found; supports start position |
| `substring_index(str, delim, count)` | String | Positive count = from left; negative = from right |
| `translate(str, matchingStr, replaceStr)` | String | 1:1 character replacement; case-sensitive |
| `format_number(number, decimals)` | String | Adds locale-aware thousands separators |
| `overlay(str, replace, pos[, len])` | String | Replaces substring at position |
| `lpad(str, len, pad)` | String | Left-pad to length |
| `rpad(str, len, pad)` | String | Right-pad to length |

**`instr` example**: `instr('Hello World', 'World')` → 7 (1-based)

**`substring_index` example**:
- `substring_index('a.b.c.d', '.', 2)` → `'a.b'` (first 2 from left)
- `substring_index('a.b.c.d', '.', -2)` → `'c.d'` (last 2 from right)

**`translate` example**:
- `translate('Hello', 'aeiou', '*')` → `'H*ll*'`
- Case-sensitive: 'e' and 'o' in 'Hello' match → replaced with '*'
- `translate` replaces each character in `matchingStr` with the corresponding char in `replaceStr`

**`format_number` example**:
- `format_number(1234567.891, 2)` → `'1,234,567.89'` (StringType with commas)

**`overlay` example**:
- `overlay('Spark SQL', 'DataFrame', 7)` → `'Spark DataFrame'`
- Takes first 6 chars (`'Spark '`), inserts `'DataFrame'`, discards the rest

**`regexp_extract` vs `regexp_replace`**:
- `regexp_extract`: extracts a capture group from the first match
- `regexp_replace`: replaces all matches with a replacement string

### 2.2 Date and Timestamp Functions

| Function | Returns | Notes |
|----------|---------|-------|
| `add_months(date_col, n)` | Date | Adds n calendar months; handles month-end edge cases |
| `date_trunc(unit, date)` | Timestamp | Truncates to the specified unit |
| `date_diff(end, start)` | Int | Number of days between dates |
| `from_unixtime(unix_ts[, fmt])` | **StringType** | Formats as `'yyyy-MM-dd HH:mm:ss'` in session timezone |
| `unix_timestamp([ts, fmt])` | LongType | Converts timestamp/string to Unix epoch seconds |
| `to_utc_timestamp(ts, tz)` | Timestamp | Treats ts as local tz, converts to UTC |
| `from_utc_timestamp(ts, tz)` | Timestamp | Treats ts as UTC, converts to local tz |
| `months_between(date1, date2)` | **DoubleType** | Fractional months between two dates |
| `trunc(date, unit)` | DateType | Truncates date (no time component) |

**`date_trunc` examples**:
- `date_trunc('month', '2024-07-15')` → `2024-07-01 00:00:00`
- `date_trunc('year', '2024-07-15')` → `2024-01-01 00:00:00`
- `date_trunc('day', '2024-07-15 14:30:00')` → `2024-07-15 00:00:00`

**`from_unixtime` returns StringType**, formatted as `'yyyy-MM-dd HH:mm:ss'` in the session timezone. NOT a TimestampType, NOT a DateType.

**`to_utc_timestamp` vs `from_utc_timestamp`**:
- `to_utc_timestamp(ts, 'America/New_York')` → Assumes ts is in New York time, converts to UTC (adds the UTC offset)
- `from_utc_timestamp(ts, 'America/New_York')` → Assumes ts is UTC, converts to New York time

**`add_months` edge cases**: Jan 31 + 1 month = Feb 28/29 (not Feb 31 which doesn't exist).

### 2.3 Array Functions

| Function | Returns | Notes |
|----------|---------|-------|
| `size(array_col)` | Int | **Returns null if array_col is null** (not 0, not -1 in Spark 3+) |
| `arrays_overlap(arr1, arr2)` | Boolean | True if any element appears in both arrays |
| `array_contains(arr, value)` | Boolean | True if value is in the array |
| `array_distinct(arr)` | Array | Removes duplicate elements |
| `array_union(arr1, arr2)` | Array | Union of two arrays (deduped) |
| `array_intersect(arr1, arr2)` | Array | Intersection of two arrays |
| `array_except(arr1, arr2)` | Array | Elements in arr1 not in arr2 |
| `flatten(arr_of_arrs)` | Array | Flattens one level of nesting |
| `sort_array(arr[, asc])` | Array | Sorts array elements |
| `slice(arr, start, length)` | Array | 1-based slicing |
| `element_at(arr, index)` | Element | 1-based index access |
| `concat(arr1, arr2)` | Array | Concatenates arrays (**use this, NOT array_concat**) |

**Critical**: `size(null)` returns **null** in Spark 3+ (legacy: -1 with `spark.sql.legacy.sizeOfNull = true`).

**`arrays_overlap` example**: `arrays_overlap(array(1,2,3), array(3,4,5))` → `true` (3 is in both)

### 2.4 Map Functions

| Function | Returns | Notes |
|----------|---------|-------|
| `map_from_arrays(keys, values)` | MapType | Creates a map from two equal-length arrays |
| `map_concat(map1, map2)` | MapType | **Right map wins on duplicate keys** |
| `map_keys(map_col)` | Array | Keys of the map |
| `map_values(map_col)` | Array | Values of the map |
| `map_entries(map_col)` | Array of structs | Array of `(key, value)` structs |

**`map_concat` duplicate key behavior**: `map_concat(map1, map2)` — when both maps share a key, the **right map's value** overwrites the left map's value.

**`map_from_arrays` example**: `map_from_arrays(array('a','b'), array(1,2))` → `map('a',1,'b',2)`

### 2.5 Window Functions: ROWS vs RANGE

| Feature | ROWS BETWEEN | RANGE BETWEEN |
|---------|-------------|--------------|
| Basis | Physical row offset | Logical value distance |
| Duplicates handling | Counts physical positions | Groups by ORDER BY value |
| Use case | Count exactly N preceding rows | Include all rows with same value |

**ROWS BETWEEN example**: `ROWS BETWEEN 1 PRECEDING AND CURRENT ROW` = the 1 preceding row and current row (exactly 2 rows)

**RANGE BETWEEN example**: `RANGE BETWEEN 1 PRECEDING AND CURRENT ROW` with ORDER BY date = all rows where date is within 1 day before and including current date's value (can include many rows with the same date)

### 2.6 Aggregate and Set Operations

**`ROLLUP` super-aggregate nulls:**
- Row where `region` IS NULL AND `country` IS NULL = **grand total**
- Row where `region` has a value AND `country` IS NULL = **regional subtotal**
- Use `GROUPING()` to distinguish super-aggregate NULLs from actual NULL data
- `ROLLUP(a,b)` produces **3 grouping sets**: `(a,b)`, `(a)`, `()`
- `CUBE(a,b)` produces **4 grouping sets**: `(a,b)`, `(a)`, `(b)`, `()`
- They are NOT the same

**`EXCEPT ALL` vs `EXCEPT DISTINCT`**:
- `EXCEPT DISTINCT` (or `EXCEPT`): removes ALL occurrences of any row that appears in the right relation
- `EXCEPT ALL`: removes exactly ONE occurrence of a matching row per occurrence in the right relation — preserves extra duplicates in the left

**`INTERSECT ALL` vs `INTERSECT DISTINCT`**:
- `INTERSECT DISTINCT`: deduplicates the result; each row appears at most once
- `INTERSECT ALL`: preserves duplicate rows up to the minimum count in both sides
- They are equivalent when both sides have no duplicates
- `INTERSECT DISTINCT` can return FEWER rows than `INTERSECT ALL` is false; it's the other way: `INTERSECT ALL` can return MORE rows when duplicates exist
- Both are supported in Spark SQL since Spark 3.0

### 2.7 Special SQL Clauses

**TABLESAMPLE:**
```sql
SELECT * FROM t TABLESAMPLE (10 PERCENT)  -- ~10% random sample
SELECT * FROM t TABLESAMPLE (100 ROWS)     -- exactly 100 rows
```
NOT `LIMIT 0.1`, NOT `SAMPLE BY`, NOT `WHERE RAND() < 0.1` (which is a WHERE filter, not TABLESAMPLE)

**QUALIFY Clause (Spark 3.4+):**
Filters rows after a window function evaluation:
```sql
-- Correct:
SELECT * FROM employees
QUALIFY RANK() OVER (PARTITION BY dept ORDER BY salary DESC) = 1

-- Also correct (subquery approach):
SELECT * FROM (
  SELECT *, RANK() OVER (PARTITION BY dept ORDER BY salary DESC) AS rk
  FROM employees
) WHERE rk = 1

-- INVALID - window functions cannot be in WHERE:
SELECT * FROM employees WHERE RANK() OVER (...) = 1
```

---

## TOPIC 3: DataFrame API

### 3.1 Column Reference Ambiguity

After a join where both DataFrames have a column with the same name:
- `F.col('column_name')` **without a DataFrame qualifier** → `AnalysisException: Reference is ambiguous`
- `df['column_name']` bracket syntax → also ambiguous if column name exists in both
- Solution: Use qualified references `df1['col']` and `df2['col']`, or alias columns before joining

```python
# Problem:
joined = df1.join(df2, 'common_key')
joined.select(F.col('duplicate_col'))  # AnalysisException!

# Solution:
joined.select(df1['duplicate_col'], df2['duplicate_col'])
```

### 3.2 Writing Data

**Parquet write with Snappy compression (correct syntax):**
```python
df.write.option('compression', 'snappy').parquet('/output')
# NOT: df.write.parquet('/output', compression='snappy')
# NOT: df.write.option('codec', 'snappy').parquet('/output')
```

**`maxRecordsPerFile`:**
```python
df.write.option('maxRecordsPerFile', 100000).parquet('/out')
```
Caps each output file at 100,000 rows. NOT `rowLimit`, NOT `partitionMaxRows`.

**`write.text()` requirement:**
- Requires the DataFrame to have **exactly one column of `StringType`**
- Will fail if the schema has more than one column or if the column is not StringType
- Must explicitly cast to string first if needed: `df.select(F.col('id').cast('string'))`

**CSV write headers:**
- Default: headers are **NOT written**
- Enable: `.option('header', True)`

**Valid Parquet write options:**
| Option | Valid? | Notes |
|--------|--------|-------|
| `compression` | ✓ | codec: snappy, gzip, zstd, lz4, none |
| `maxRecordsPerFile` | ✓ | Limits rows per file |
| `partitionOverwriteMode` | ✓ | dynamic vs static partition overwrite |
| `header` | ✗ | CSV only option |
| `mergeSchema` | ✗ (on write) | Parquet read option; Delta write option but not plain Parquet |

### 3.3 Reading Data

**CSV `nullValue` option:**
```python
spark.read.csv('/path', nullValue='N/A')        # correct
spark.read.option('nullValue', 'N/A').csv('/path')  # also correct
```
NOT `na`, NOT `missingValue`, NOT `emptyValue`.

**`pathGlobFilter` option:**
```python
spark.read.option('pathGlobFilter', '*.parquet').parquet('/data')
```
Restricts file scanning to matching files. NOT `fileExtension`, NOT `includeOnly`.

**Parquet schema inference**: Reads the schema from the **Parquet file footer metadata** — fast and accurate, does NOT require scanning row data or sampling.

**`spark.read.load()` with format:**
```python
# These are equivalent:
spark.read.format('delta').load('/data/events')
spark.read.load('/data/events', format='delta')  # format as keyword arg
# NOT: spark.read.load('/data/events').format('delta')  (format() must come before load())
```

**`spark.read.delta()` shortcut**: Available in Databricks but NOT in vanilla Spark.

### 3.4 Key DataFrame Functions and Methods

**`F.input_file_name()`:**
- Returns the file path of the source file for each row
- Useful for file provenance tracking
- NOT `F.source_file()`, NOT `F.file_name()`

**`schema.json()`:**
- Returns JSON string representation of a `StructType`
- `schema.prettyJson()` returns a formatted multi-line version
- NOT `toJson()`, NOT `asJson()`

**`F.broadcast()`:**
```python
from pyspark.sql.functions import broadcast  # correct import

df1.join(broadcast(df2), 'key')
```
NOT from `pyspark.sql`, NOT from `pyspark.sql.hints`, NOT from `pyspark`.

**`df.rdd` conversion:**
- Returns an RDD of **`Row` objects**
- Fields accessible by name (`row.col_name`) or index (`row[0]`)
- NOT dicts, NOT plain tuples
- NOT zero-cost — requires serialization in modern Spark

**`df.withColumn()` on existing column:**
```python
df.withColumn('existing_col', new_expr)  # replaces in-place, no error, no duplicate
```
The existing column is **replaced in place** — no AnalysisException, no duplicate column created.

**`F.coalesce(col1, col2, col3)`:**
- Returns the **first non-null value** from the provided columns, evaluated left-to-right
- NOT sum, NOT count, NOT a combined column

**`df1.exceptAll(df2)` vs `df1.subtract(df2)`:**
- `exceptAll`: removes ONE matching row per occurrence in df2 (preserves extra duplicates in df1)
- `subtract`: removes ALL occurrences of any row present in df2 (`EXCEPT DISTINCT` semantics)

**`F.when()` without `.otherwise()`:**
```python
F.when(F.col('x') > 0, 'positive').when(F.col('x') < 0, 'negative')
# when x == 0: returns null (implicit .otherwise(None))
```

**`df.selectExpr()`:**
```python
df.selectExpr('age * 2 AS double_age')  # SQL expression string, no imports needed
# Equivalent: df.select((F.col('age') * 2).alias('double_age'))
```

**`sdf.to_pandas_on_spark()`:**
- Returns a `pyspark.pandas.DataFrame` (Pandas API on Spark)
- Data remains **distributed** on the cluster
- NOT a pandas.DataFrame (that would be `.toPandas()`)

### 3.5 StructType Equality

```python
schema1 = StructType([StructField('a', IntegerType(), True)])
schema2 = StructType([StructField('a', IntegerType(), True)])

schema1 == schema2  # True — StructType uses VALUE-BASED equality
```
`StructType` implements `__eq__` with value semantics. Two schemas with identical fields (name, type, nullable) compare as equal regardless of object identity.

### 3.6 Pandas UDFs

**Vectorized UDF (Series → Series):**
```python
from pyspark.sql.functions import pandas_udf
from pyspark.sql.types import DoubleType
import pandas as pd

@pandas_udf(returnType=DoubleType())
def my_udf(s: pd.Series) -> pd.Series:
    return s * 2
```
NOT `@udf`, NOT `@vectorized_udf`, NOT `@spark.udf.pandas`.

**`applyInPandas` (GroupedMap):**
- Invokes the function **once per group**
- Passes all rows for that group as a **single `pd.DataFrame`**
- Returns a `pd.DataFrame`
- NOT a pd.Series per group, NOT one row at a time

### 3.7 Partition Count Methods

To get the number of partitions in a DataFrame:
```python
df.rdd.getNumPartitions()  # standard method (A)
len(df.rdd.partitions)      # direct partition list count (C)
```
**`df.getNumPartitions()` does NOT exist on DataFrame** (only on RDD).
`df.repartitionNum` does NOT exist.

### 3.8 JDBC Operations

**Write with `write.jdbc()`:**
```python
df.write.jdbc(url, table='my_table', mode='overwrite', properties=props)
# Parameter name is 'table' (positional 2nd arg)
```
NOT `tableName`, NOT `dbtable` (that's for reading), NOT `targetTable`.

**Read with `read.jdbc()` parallelism:**
```python
# Option 1: Range-based partitioning
df = spark.read.jdbc(url, table='orders',
    numPartitions=10,
    partitionColumn='order_id',
    lowerBound=1,
    upperBound=1000000,
    properties=props)

# Option 2: Custom predicates
df = spark.read.jdbc(url, table='orders',
    predicates=['region = "North"', 'region = "South"', ...],
    properties=props)
```
`fetchsize` affects batch fetch performance but NOT parallelism.
`batchsize` is a **write** option for controlling rows per batch.

**JDBC subquery:**
```python
# Both work:
spark.read.jdbc(url, table='(SELECT * FROM t WHERE x > 1) t1', properties=props)  # dbtable with subquery
spark.read.option('query', 'SELECT * FROM t WHERE x > 1').format('jdbc').load()    # query option
```
Both `dbtable` (with parenthesized subquery + alias) AND the `query` option are supported.

### 3.9 DataFrame Creation

```python
# From Row objects:
from pyspark.sql import Row
spark.createDataFrame([Row(a=1, b='x'), Row(a=2, b='y')])  # correct

# From tuples with schema:
spark.createDataFrame([(1, 'x'), (2, 'y')], schema=['a', 'b'])

# From pandas DataFrame:
spark.createDataFrame(pdf)
```

### 3.10 Caching Pattern

```python
df.cache().count()  # standard pattern
```
- `cache()` is **lazy** — only marks the DataFrame for caching
- `count()` is an **action** that triggers plan execution and physically materializes data in memory
- Without `count()`, the cache is not populated until the first actual action

### 3.11 coalesce vs repartition

| Feature | `coalesce(n)` | `repartition(n)` |
|---------|--------------|-----------------|
| Shuffle | No (narrow) | Yes (full shuffle) |
| Partition balance | Uneven (merges existing) | Even distribution |
| Stage boundary | No | Yes |
| Can increase count? | Only up to current count | Yes, can increase |
| Use case | Reducing partitions (avoid shuffle) | Need balanced distribution |

---

## TOPIC 4: Troubleshooting & Tuning

### 4.1 Broadcast Join Control

| Config | Effect |
|--------|--------|
| `spark.sql.autoBroadcastJoinThreshold = -1` | **Disable all automatic broadcast joins** |
| `spark.sql.autoBroadcastJoinThreshold = 0` | Does NOT disable (0 means no threshold, effectively everything is broadcast) |
| `spark.sql.autoBroadcastJoinThreshold = 10485760` | Default (10 MB) |

**To disable**: use **-1**, NOT 0.

### 4.2 Statistics and CBO

**`ANALYZE TABLE` command:**
```sql
ANALYZE TABLE orders COMPUTE STATISTICS FOR ALL COLUMNS;
-- Updates column-level stats (min, max, NDV, null count) for CBO
```

**CBO Join Reorder** (requires both):
1. `spark.sql.cbo.enabled = true`
2. `spark.sql.cbo.joinReorder.enabled = true`

`spark.sql.cbo.enabled = true` alone is NOT sufficient for join reordering.

**`spark.sql.join.preferSortMergeJoin = true`:**
- Makes Spark prefer **SortMergeJoin over ShuffledHashJoin** when both are applicable
- Does NOT disable BroadcastHashJoin
- Does NOT force all joins to SortMergeJoin

### 4.3 CACHE TABLE Behavior

```sql
CACHE TABLE sales         -- EAGER: immediately scans and materializes
CACHE LAZY TABLE sales    -- LAZY: materializes on first query
UNCACHE TABLE sales       -- Removes from cache
```

`CACHE TABLE` (without LAZY) is **eager** — immediately scans and caches the entire table.

### 4.4 AQE Partition Coalescing

| Config | Purpose |
|--------|---------|
| `spark.sql.adaptive.advisoryPartitionSizeInBytes` | **Target partition size** AQE aims for when coalescing (default 64 MB) |
| `spark.sql.adaptive.coalescePartitions.minPartitionNum` | **Lower bound** on partition count after AQE coalescing |
| `spark.sql.adaptive.skewJoin.enabled` | Enables AQE skewed join optimization |
| `spark.sql.adaptive.skewJoin.skewedPartitionThresholdInBytes` | Partition size threshold for skew detection |

**`advisoryPartitionSizeInBytes`**: Advisory (not a hard cap) — AQE targets this size but may produce slightly different sizes.

**`coalescePartitions.minPartitionNum`**:
- Lower bound on partition count → AQE will not coalesce below this number
- Setting to 1 allows AQE to collapse ALL output to a single partition
- Does NOT directly control executor count

### 4.5 EXPLAIN Modes

| Mode | Content |
|------|---------|
| `'simple'` | Physical plan only |
| `'extended'` | All plan stages (parsed, analyzed, optimized, physical) |
| `'codegen'` | Generated Java code for whole-stage codegen |
| `'cost'` | **Includes CBO estimates: row counts and data sizes** |
| `'formatted'` | Human-readable physical plan with node IDs |

**`explain('cost')`**: Shows logical and physical plan annotated with CBO estimates. Use this when diagnosing whether the optimizer has accurate statistics.

### 4.6 ORC vs Parquet

| Scenario | Preferred Format |
|---------|----------------|
| Data produced by Apache Hive | **ORC** (Hive's native format; best statistics/BloomFilters) |
| Python pandas code outside Spark | Parquet (better ecosystem support) |
| Deeply nested arrays-of-structs | Parquet (better nested type support) |
| Apache Kafka consumers | Neither directly (use Avro or JSON) |
| General Spark analytics | Parquet (default in Spark ecosystem) |

### 4.7 In-Memory Columnar Compression

`spark.sql.inMemoryColumnarStorage.compressed` (default: `true`)
- Enables Snappy compression on **cached columnar data** in memory
- Reduces memory footprint at small CPU cost
- NOT `spark.memory.columnCompression.enabled`, NOT `spark.sql.cache.compression.codec`

---

## TOPIC 5: Structured Streaming

### 5.1 Triggers

| Trigger | Code | Behavior |
|---------|------|---------|
| Default (micro-batch) | None | Runs as fast as possible |
| Fixed interval | `trigger(processingTime='30 seconds')` | Runs every N seconds |
| **Once** | `trigger(once=True)` | **Processes all available data in one micro-batch, then stops** |
| AvailableNow | `trigger(availableNow=True)` | Like once but in multiple batches |
| Continuous | `trigger(continuous='1 second')` | Sub-millisecond latency |

**`trigger(once=True)`**: Processes ALL available source data in a single micro-batch, then automatically stops. Useful for scheduled incremental batch processing.

### 5.2 Checkpoint (Required for Fault Tolerance)

```python
query = (df.writeStream
    .option('checkpointLocation', '/path/to/checkpoint')  # REQUIRED
    .outputMode('append')
    .format('delta')
    .start('/output'))
```

The checkpoint stores:
- Source offsets (what data has been read)
- Sink commit log (what data has been written)
- State store (for stateful operations)

### 5.3 Output Modes

| Mode | What is written per trigger | Requires |
|------|---------------------------|----------|
| `append` | Only newly added rows | No agg, OR agg with watermark |
| `update` | Only rows that changed or were added | Any query |
| `complete` | **All rows in the result table** | **Aggregation required** |

**`complete` mode is NOT valid for non-aggregated queries**. It requires a full aggregation to recompute the complete result table on every trigger.

**`update` mode**: Emits only rows whose values changed or were newly created since the last trigger. Unchanged rows are NOT re-emitted.

### 5.4 Tumbling Windows

```python
from pyspark.sql.functions import window

agg = (events
    .withWatermark('timestamp', '10 minutes')
    .groupBy(window('timestamp', '5 minutes'))
    .count())
```

**Tumbling window assignment**: An event with timestamp `12:07` falls in `[12:05, 12:10)` — the 5-minute non-overlapping window that contains it.

Tumbling windows are **non-overlapping** (unlike sliding windows). Each event belongs to exactly one window.

### 5.5 foreachBatch

```python
def process_batch(batch_df, batch_id):
    # batch_df is a static DataFrame
    batch_df.write.delta('/output/delta')
    # Also write to REST API:
    batch_df.toPandas().apply(call_rest_api, axis=1)

query = (stream_df.writeStream
    .foreachBatch(process_batch)
    .start())
```

`foreachBatch` is the **multi-sink pattern** for Structured Streaming — receives each micro-batch as a static DataFrame, enabling arbitrary processing including writing to multiple sinks.

### 5.6 Kafka Integration

**`failOnDataLoss = false`:**
```python
spark.readStream.format('kafka')
    .option('failOnDataLoss', 'false')
    .load()
```
Silently skips Kafka offsets no longer available (due to retention expiry) rather than failing the query.

### 5.7 Query Monitoring

| Method | Returns | Notes |
|--------|---------|-------|
| `query.status` | Dict | Current status of the running query |
| `query.lastProgress` | Dict | Most recent micro-batch statistics |
| `query.recentProgress` | **List of dicts** | **Recently completed micro-batch reports** |
| `query.id` | UUID | Unique query identifier |
| `query.runId` | UUID | Unique run identifier (changes on restart) |

**`query.recentProgress`**: Returns a **list of dicts**, NOT a single dict, NOT a streaming DataFrame, NOT a file path.

### 5.8 StreamingQueryListener

```python
from pyspark.sql.streaming import StreamingQueryListener

class MyListener(StreamingQueryListener):
    def onQueryStarted(self, event): ...
    def onQueryProgress(self, event): ...
    def onQueryTerminated(self, event): ...

spark.streams.addListener(MyListener())
```

Monitors **ALL active streaming queries** in a Spark application without modifying individual query code. NOT `SparkListener`, NOT `QueryProgressCallback`, NOT `StreamingMetricsListener`.

### 5.9 withWatermark + window Rules

All of the following are true:
1. `withWatermark()` must be called **before** `groupBy(window(...))`
2. The watermark determines when window state is **finalized and dropped**
3. In `append` mode: results emitted only after watermark passes the window's end
4. In `complete` mode: **all** window results emitted on every trigger (regardless of watermark)
5. The watermark column should be the **same column** used in the `window()` expression

---

## TOPIC 6: Spark Connect

### 6.1 Connection Methods

```python
# Explicit remote connection:
spark = SparkSession.builder.remote('sc://host:15002').getOrCreate()

# Environment variable auto-config:
# Set SPARK_REMOTE=sc://host:15002 before running
spark = SparkSession.builder.getOrCreate()  # picks up SPARK_REMOTE automatically

# Databricks Serverless:
from databricks.connect import DatabricksSession
spark = DatabricksSession.builder.serverless().getOrCreate()
```

**`SPARK_REMOTE`** environment variable: When set to a `sc://` URL, automatically configures Spark Connect without calling `.remote()` explicitly.
NOT `SPARK_CONNECT_URL`, NOT `SPARK_SERVER_URL`, NOT `SPARK_CONNECT_SERVER`.

### 6.2 Data Serialization

Spark Connect uses **Apache Arrow** for serializing data between client and server over gRPC.
NOT Java serialization/Kryo, NOT Protobuf only (Protobuf is used for the RPC protocol/plan structure, Arrow is for data), NOT JSON.

### 6.3 Session Object in Connect

`SparkSession.getActiveSession()` in a Spark Connect application returns the **client-side proxy session object** — a lightweight local object representing the remote connection.
NOT the server-side session, NOT None.

### 6.4 Spark Connect vs spark-submit

| Aspect | Spark Connect | spark-submit |
|--------|--------------|-------------|
| Driver location | **Client machine** (lightweight local process) | Shipped to cluster (cluster mode) or client (client mode) |
| Computation | Remote Spark server | Same cluster |
| SparkContext/RDD | **NOT available** | Available |
| Multi-client sharing | **Yes** — multiple clients can share a server | No — each submit creates a new application |
| Errors | Analysis errors surface on action (server-side) | Errors surface during plan building |

`spark-submit` is NOT deprecated and will NOT be removed in Spark 4.0.

---

## TOPIC 7: Pandas API on Spark

### 7.1 SQL and I/O

**Running SQL:**
```python
import pyspark.pandas as ps

psdf.createOrReplaceTempView('my_view')
result = ps.sql('SELECT * FROM my_view WHERE x > 1')
```
NOT `ps.execute_sql()`, NOT `ps.query()`, NOT `ps.DataFrame.sql()`.

**Reading Parquet (two valid approaches):**
```python
# Approach 1: Native Pandas API on Spark
psdf = ps.read_parquet('/path')

# Approach 2: Via Spark then convert
psdf = spark.read.parquet('/path').pandas_api()

# Both are valid — answer is D (both work)
```

### 7.2 apply() with axis Parameter

```python
psdf.apply(func, axis=1)  # Row-wise: func receives each row as a pd.Series
psdf.apply(func, axis=0)  # Column-wise: func receives each column as a pd.Series
```

`axis=1` is **supported** in Pandas API on Spark (does NOT raise ValueError). Row-wise application distributes across the cluster.

### 7.3 Rolling Window

```python
psdf['value'].rolling(3).mean()
```
- Computes a **3-row trailing rolling average**
- First two rows yield **NaN** (fewer than 3 preceding values)
- Distributed across Spark partitions
- This IS supported (NOT a NotImplementedError)

### 7.4 ps.concat

```python
# Default: axis=0, stacks rows
result = ps.concat([psdf1, psdf2])

# Side-by-side by index
result = ps.concat([psdf1, psdf2], axis=1)  # requires ops_on_diff_frames=True if different plans

# Reset index
result = ps.concat([psdf1, psdf2], ignore_index=True)
```

**What is true:**
- Default concat is along `axis=0` (stacks rows) ✓
- `axis=1` requires `ops_on_diff_frames = True` when DataFrames come from different plans ✓
- `ignore_index=True` resets the resulting index ✓
- `axis=1` concat performs a **distributed merge on index values** ✓
- The result does NOT always have a default integer index (preserves input indices unless `ignore_index=True`) ✗

---

## KEY EXAM TRAPS — ITERATION 4

| Trap | Wrong | Correct |
|------|-------|---------|
| spark-submit for Python modules | `--files` | `--py-files` |
| History Server port | 4040 or 8080 | **18080** |
| groupByKey() partitioner | None or RangePartitioner | `HashPartitioner(spark.default.parallelism)` |
| MEMORY_ONLY_2 meaning | Two memory tiers | **Two replicated copies across two executors** |
| Task retry config key | `spark.task.maxRetries` | `spark.task.maxFailures` |
| size(null) in Spark 3+ | 0 or -1 | **null** |
| from_unixtime returns | TimestampType | **StringType** |
| map_concat duplicate key | Left wins | **Right wins** |
| ROLLUP vs CUBE | Same grouping sets | ROLLUP=3, CUBE=4 for (a,b) |
| EXCEPT ALL vs EXCEPT | Remove all occurrences | EXCEPT ALL: remove one per occurrence |
| Disable broadcast join | threshold=0 | **threshold=-1** |
| CBO join reorder | cbo.enabled alone | **cbo.enabled + cbo.joinReorder.enabled** |
| CACHE TABLE | Lazy | **Eager** (CACHE LAZY TABLE is lazy) |
| autoBroadcastJoinThreshold disable | 0 | **-1** |
| Parquet write option `header` | Valid | **Invalid** (CSV only) |
| Parquet write option `mergeSchema` | Valid for plain Parquet write | **Read option only** (Delta write too, but not plain Parquet) |
| `df.getNumPartitions()` | Valid | **Does NOT exist on DataFrame** (use `df.rdd.getNumPartitions()`) |
| write.jdbc() table param name | `dbtable` or `tableName` | **`table`** |
| coalesce(n) behavior | Shuffle | **No shuffle (narrow)** |
| QUALIFY clause availability | All Spark versions | **Spark 3.4+** |
| complete output mode | Works without aggregation | **Requires aggregation** |
| SPARK_REMOTE env var | SPARK_CONNECT_URL | **SPARK_REMOTE** |
| Spark Connect data format | Kryo/Java serialization | **Apache Arrow** |
| ps.read_parquet() | Only one approach | **Both ps.read_parquet() and .pandas_api() work** |
| withWatermark before/after | After groupBy | **Must be BEFORE groupBy(window(...))** |

---

## CONFIGURATION QUICK REFERENCE — ITERATION 4

| Config | Default | Purpose |
|--------|---------|---------|
| `spark.task.maxFailures` | 4 | Max task failures before job abort |
| `spark.sql.files.maxPartitionBytes` | 128 MB | Target partition size for file reads |
| `spark.sql.files.openCostInBytes` | ~4 MB | Per-file overhead for partition costing |
| `spark.dynamicAllocation.minExecutors` | 0 | DRA lower bound |
| `spark.dynamicAllocation.maxExecutors` | ∞ | DRA upper bound |
| `spark.sql.warehouse.dir` | `spark-warehouse` (cwd) | Managed table storage location |
| `spark.network.timeout` | 120 s | Executor dead timeout |
| `spark.executor.heartbeatInterval` | 10 s | Executor heartbeat frequency |
| `spark.sql.autoBroadcastJoinThreshold` | 10 MB | Broadcast join size threshold (-1 to disable) |
| `spark.sql.adaptive.advisoryPartitionSizeInBytes` | 64 MB | AQE coalesce target size |
| `spark.sql.inMemoryColumnarStorage.compressed` | true | Compress cached columnar data |
| `spark.sql.cbo.enabled` | false | Enable Cost-Based Optimizer |
| `spark.sql.cbo.joinReorder.enabled` | false | Enable CBO join reordering |
| `spark.sql.join.preferSortMergeJoin` | true | Prefer SMJ over ShuffledHashJoin |
| `spark.shuffle.partitions` | 200 | Post-shuffle partition count |
