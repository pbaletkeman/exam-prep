# Databricks Certified Associate Developer for Apache Spark — Study Guide

**A comprehensive learning guide to master Apache Spark fundamentals**

---

## Table of Contents

1. [Exam Overview](#exam-overview)
2. [Topic 1: Apache Spark Architecture & Internals](#topic-1-apache-spark-architecture--internals)
3. [Topic 2: Spark SQL](#topic-2-spark-sql)
4. [Topic 3: DataFrame API](#topic-3-dataframe-api)
5. [Topic 4: Troubleshooting & Tuning](#topic-4-troubleshooting--tuning)
6. [Topic 5: Structured Streaming](#topic-5-structured-streaming)
7. [Topic 6: Spark Connect](#topic-6-spark-connect)
8. [Topic 7: Pandas API on Spark](#topic-7-pandas-api-on-spark)
9. [Study Tips & Strategies](#study-tips--strategies)
10. [Quick Reference Checklists](#quick-reference-checklists)

---

## Exam Overview

- **Total Questions**: 100
- **Difficulty Distribution**: 20 Easy / 60 Medium / 20 Hard
- **Question Types**: 77 single-choice / 23 multiple-choice (select all that apply)
- **Time Limit**: ~90 minutes (typical for Databricks certification exams)
- **Passing Score**: Usually ~75% (varies by Databricks)

### Recommended Study Approach

1. **Read the study guide** — Learn foundational concepts in each topic
2. **Answer practice questions** — Test your understanding on the 100-question bank
3. **Review explanations** — Study the answer key to understand why each answer is correct
4. **Identify weak areas** — Re-read sections where you scored poorly
5. **Practice timing** — Take timed mock exams to build exam-day confidence

---

## Topic 1: Apache Spark Architecture & Internals

### 1.1 Execution Hierarchy

Spark organizes work in a strict hierarchy:

```
Application
  ↓
Job (one per action)
  ↓
Stage (split at shuffle boundaries)
  ↓
Task (one per partition)
```

**Example:**
```python
df.filter(col('year') == 2024) \       # Lazy — no action yet
  .groupBy('category').sum('amount') \ # Lazy — no action yet
  .write.parquet('/output')             # Action! Triggers execution
```

This creates **1 Application → 1 Job → 2 Stages → Many Tasks** (one per partition in each stage).

### 1.2 Driver and Executors

| Component | Role |
|-----------|------|
| **Driver** | Runs SparkContext/SparkSession; converts user code → DAG; schedules tasks via TaskScheduler |
| **Executors** | Run tasks on partitions; cache data blocks; return results to Driver |
| **Cluster Manager** | Allocates CPU/memory resources (YARN, Kubernetes, Standalone, Local) |

### 1.3 Transformations vs Actions

**Transformations** (Lazy):
- Do NOT trigger execution
- Return a new DataFrame
- Examples: `filter()`, `select()`, `join()`, `withColumn()`, `groupBy().sum()`

**Actions** (Eager):
- Trigger a Spark job
- Return a value to the driver or write to storage
- Examples: `collect()`, `count()`, `show()`, `write.parquet()`

### 1.4 Narrow vs Wide Transformations

**Narrow Transformations**:
- No shuffle required
- Each output partition depends on exactly one input partition
- Examples: `filter()`, `select()`, `withColumn()`, `map()`, `flatMap()`
- **Performance Impact**: Minimal overhead; can pipeline multiple narrow operations

**Wide Transformations**:
- Require shuffle (all-to-all data exchange across the network)
- Each output partition may depend on multiple input partitions
- Examples: `groupBy()`, `join()`, `distinct()`, `orderBy()`, `repartition()`
- **Performance Impact**: Expensive; creates stage boundaries

### 1.5 Lazy Evaluation Benefits

Spark defers execution until an action is called, enabling:

1. **Plan Optimization**: Catalyst optimizer can reorder operations and apply rule-based optimizations
2. **Pipelining**: Multiple narrow transformations fuse into a single stage with no intermediate materialization
3. **Fault Tolerance via Lineage**: Lost partitions are recomputed from their lineage without a full source scan
4. **Pruning**: Unnecessary operations can be eliminated before execution

### 1.6 DAG Scheduler vs Task Scheduler

| Component | Responsibility |
|-----------|-----------------|
| **DAGScheduler** | Converts logical DAG → physical Stages; handles fault tolerance at stage level (re-submits failed stages) |
| **TaskScheduler** | Assigns tasks to available Executor cores; handles task-level failures (retries) |

### 1.7 Shuffles and Stage Boundaries

A **shuffle** is created when data must be redistributed across partitions. It creates a **stage boundary** because:

1. All tasks in the previous stage must complete before the shuffle writes
2. All shuffle data is written to disk (for fault tolerance)
3. The next stage reads shuffle data from all previous tasks

Common shuffle operations:
- `groupBy()`, `distinct()`
- `join()` (most implementations)
- `orderBy()`, `sort()`
- `repartition()`

### 1.8 Shuffle Partitions Configuration

After a shuffle, the number of output partitions is controlled by:
- **`spark.sql.shuffle.partitions`** (default 200) — for SQL/DataFrame operations
- **`spark.default.parallelism`** — for RDD operations

**Tuning Tip**: If your data is smaller than typical, reduce shuffle partitions to avoid many tiny tasks.

### 1.9 Broadcasting and Hash Joins

**BroadcastHashJoin**:
- Small table is broadcast to all Executors
- No shuffle needed
- Conditions:
  - One side must be smaller than `spark.sql.autoBroadcastJoinThreshold` (default 10 MB)
  - Spark must be able to estimate the table's size (statistics are available)

**Force Broadcast**:
```python
from pyspark.sql.functions import broadcast

df.join(broadcast(small_df), on='id')           # Explicit broadcast
df.hint('broadcast').join(small_df, on='id')    # Using hint
```

### 1.10 Fault Tolerance and Lineage

- Spark reconstructs lost partitions from their **lineage** (the recorded DAG of transformations)
- No need to re-read the original data
- `checkpoint()` breaks the lineage and stores a snapshot to a reliable store (useful for long-running jobs)

**Persist Storage Levels**:
```python
df.persist(StorageLevel.MEMORY_ONLY)           # In memory only; evicts if full
df.persist(StorageLevel.MEMORY_AND_DISK)       # Memory + disk spillover
df.persist(StorageLevel.MEMORY_AND_DISK_SER)   # Serialized (smaller, less GC)
df.persist(StorageLevel.DISK_ONLY)             # Disk only
```

### 1.11 Common Pitfalls

| Pitfall | Problem | Solution |
|---------|---------|----------|
| Calling `collect()` on a large DataFrame | Brings all data to Driver heap → OutOfMemory | Use `limit()` or write to storage instead |
| Excessive `groupBy()` operations | Each groups triggers a shuffle | Combine aggregations in a single `groupBy().agg()` |
| Not tuning shuffle partitions | 200 default partitions is often wrong | Adjust to match data size (~100 MB per partition is ideal) |
| Forgetting lazy evaluation | Thinking `select()` executes immediately | Remember: only actions trigger execution |

---

## Topic 2: Spark SQL

### 2.1 SparkSession — The Unified Entry Point

Spark 2.0+ introduced `SparkSession` as the single entry point for:
- DataFrames & Datasets
- SQL queries
- Streaming
- Configuration

```python
from pyspark.sql import SparkSession

spark = SparkSession.builder \
  .appName('my_app') \
  .config('spark.sql.shuffle.partitions', 50) \
  .getOrCreate()

# All roads lead here
df = spark.read.parquet('/data')                       # DataFrame API
result = spark.sql('SELECT * FROM my_table')           # SQL
```

### 2.2 Temporary Views

| Type | Scope | Lifetime | Reference |
|------|-------|----------|-----------|
| Session Temp View | Single session | Until session ends | `SELECT * FROM view_name` |
| Global Temp View | All sessions in app | Until app ends | `SELECT * FROM global_temp.view_name` |
| Permanent Table | Across sessions | Until dropped | Uses metastore |

```python
# Session-scoped temp view
df.createOrReplaceTempView('sales')
spark.sql('SELECT * FROM sales')

# Global temp view
df.createOrReplaceGlobalTempView('events_global')
spark.sql('SELECT * FROM global_temp.events_global')
```

### 2.3 The Catalyst Optimizer

Catalyst is Spark's query optimizer. It performs:

1. **Parsing** — SQL string → unresolved logical plan
2. **Analysis** — Resolve column references against schema
3. **Optimization** — Apply rule-based transformations:
   - **Predicate Pushdown**: Move filters closer to the source (e.g., into ParquetFileScan)
   - **Constant Folding**: Compute constant expressions at plan time (e.g., `2 * 3 = 6`)
   - **Dead Code Elimination**: Remove unused columns
   - **Join Reordering**: Rearrange joins to minimize data size
4. **Physical Planning** — Generate executable code (bytecode via WholeStageCodegen)

### 2.4 Predicate Pushdown Limitations

Filters can only be pushed down if they depend on source columns:

```python
# ✓ Pushdown works — direct column reference
df.filter(col('year') == 2024).read()

# ✗ Pushdown fails — filter depends on derived column
df.withColumn('processed_date', F.to_date(col('raw_ts'))) \
  .filter(col('processed_date') == '2024-01-01')
# The filter cannot be pushed past the withColumn
```

### 2.5 Adaptive Query Execution (AQE)

AQE makes runtime optimizations based on actual data statistics after partial execution:

| Feature | Benefit |
|---------|---------|
| **Coalescing Partitions** | Merges many small post-shuffle partitions into fewer, larger ones (reduces task overhead) |
| **Join Strategy Switching** | May switch SortMergeJoin → BroadcastHashJoin at runtime if one side is discovered to be small |
| **Skew Handling** | Splits severely skewed partitions to avoid straggler tasks |

**Enable AQE** (enabled by default in Spark 3.2+):
```python
spark.conf.set('spark.sql.adaptive.enabled', True)
spark.conf.set('spark.sql.adaptive.coalescePartitions.enabled', True)
spark.conf.set('spark.sql.adaptive.skewJoin.enabled', True)
```

### 2.6 Window Functions

Window functions perform per-partition aggregations and comparisons without reducing the number of rows:

```python
from pyspark.sql.window import Window
from pyspark.sql import functions as F

w = Window.partitionBy('dept').orderBy('salary DESC')

df.withColumn('salary_rank', F.rank().over(w)) \
  .withColumn('dept_avg_salary', F.avg('salary').over(w)) \
  .show()
```

**Common Window Functions**:

| Function | Behavior | Notes |
|----------|----------|-------|
| `row_number()` | Sequential 1, 2, 3, ... | Unique; no gaps |
| `rank()` | 1, 2, 2, 4, ... | Skips after ties |
| `dense_rank()` | 1, 2, 2, 3, ... | No gaps after ties |
| `lag()` / `lead()` | Previous/next row value | Useful for comparisons |
| `first()` / `last()` | First/last value in frame | Aggregate within window |
| `sum()` / `avg()` | Cumulative aggregate | Respects frame boundaries |

**Frame Specification**:
```python
# Default for ordered windows: from start of partition to current row (cumulative)
w = Window.partitionBy('dept').orderBy('hire_date')

# Explicit sliding window (±1 rows around current)
w.rangeBetween(Window.unboundedPreceding, Window.currentRow)

# All rows in partition (no order constraint)
w.rowsBetween(Window.unboundedPreceding, Window.unboundedFollowing)
```

### 2.7 Built-in SQL Functions

**String Functions**:
```python
F.upper(col('name'))              # Uppercase
F.lower(col('name'))              # Lowercase
F.trim(col('name'))               # Remove leading/trailing spaces
F.substring(col('name'), 1, 3)    # Extract substring
F.split(col('email'), '@')        # Split into array
F.regexp_replace(col('x'), '[0-9]', '*')  # Regex replacement
```

**Date/Time Functions**:
```python
F.year(col('hire_date'))          # Extract year
F.month(col('hire_date'))         # Extract month
F.to_date(col('timestamp_str'))   # Parse string to date
F.current_date()                  # Today's date
```

**Collection Functions** (Higher-Order):
```python
F.transform(col('items'), lambda x: x * 2)         # Map over array
F.filter(col('items'), lambda x: x > 10)           # Filter array
F.aggregate(col('items'), 0, lambda a, x: a + x)   # Fold/reduce array
```

### 2.8 Grouping and Aggregation

**Standard GroupBy**:
```python
df.groupBy('dept', 'year') \
  .agg(
    F.sum('salary').alias('total_salary'),
    F.avg('salary').alias('avg_salary'),
    F.count('*').alias('headcount'),
    F.countDistinct('employee_id').alias('unique_employees'),
    F.max('salary').alias('max_salary')
  ) \
  .show()
```

**Rollup and Cube**:
```python
# Rollup: hierarchical subtotals (left-to-right)
df.groupBy('year', 'quarter').rollup('year', 'quarter').sum('amount')
# Produces: totals by (year, quarter), (year), and grand total

# Cube: all combinations (more expensive than rollup)
df.groupBy('year', 'quarter').cube('year', 'quarter').sum('amount')
# Produces: totals by (year, quarter), (year), (quarter), and grand total
```

**Important**: NULL values in aggregation
- `F.sum()`, `F.avg()`, `F.max()`, `F.min()` **ignore NULL**
- `F.count(col('x'))` counts non-NULL values
- `F.count('*')` counts all rows including those with NULL

### 2.9 Cost-Based Optimizer (CBO)

The CBO uses table statistics to choose optimal join orders and strategies:

```python
# Collect statistics (must be done explicitly)
spark.sql('ANALYZE TABLE sales COMPUTE STATISTICS')

# Check if stats are available
spark.catalog.getTable('sales')  # See if stats are populated
```

Without statistics, Spark uses heuristics (which may be suboptimal for large datasets).

### 2.10 Common Pitfalls

| Pitfall | Issue | Fix |
|---------|-------|-----|
| Forgetting to register UDFs for SQL | DataFrame API UDF ≠ SQL UDF | Use `spark.udf.register('func', my_func, returnType)` |
| Using wrong aggregate function for NULLs | `count('*')` vs `count(col)` behave differently | Use `count(col)` to ignore NULLs; `count('*')` includes them |
| Not pushing down predicates | Reading unnecessary data from storage | Write filters on source columns early; avoid derived columns in filters |
| Window function frame misunderstanding | Wrong cumulative results | Understand default vs explicit frame specification |

---

## Topic 3: DataFrame API

### 3.1 Basic Operations

**Select Columns**:
```python
df.select('id', 'name', 'email')              # String column names
df.select(col('id'), col('name'))             # Column expressions
df.selectExpr('id', 'name', 'salary * 1.1 AS bonus')  # SQL expressions
```

**Filter Rows**:
```python
df.filter(col('age') > 25)                    # Narrow transformation
df.where(col('status') == 'active')           # Alias for filter()
df.filter((col('age') > 25) & (col('salary') > 50000))  # AND condition
```

**Add/Modify Columns**:
```python
df.withColumn('bonus', col('salary') * 0.1)  # Add new column (or replace if exists)
df.withColumnRenamed('emp_id', 'employee_id')  # Rename column
df.drop('unwanted_col')                       # Remove column
```

**Sorting**:
```python
df.sort('age')                                # Ascending (default)
df.orderBy(col('salary').desc())              # Descending (alias for sort)
df.sort(col('dept'), col('salary').desc())    # Multiple columns
```

### 3.2 Handling NULL Values

**Detection**:
```python
df.filter(col('email').isNull())              # Find NULLs
df.filter(col('email').isNotNull())           # Find non-NULLs
df.filter(F.isnan(col('score')))             # Find NaN (floating-point only)
```

**Filling**:
```python
df.fillna(0)                                  # Fill all numeric NULLs with 0
df.fillna({'salary': 0, 'dept': 'Unknown'})  # Column-specific fills
df.fillna(0, subset=['salary'])               # Fill specific columns
```

**Dropping**:
```python
df.dropna()                                   # Drop rows with any NULL
df.dropna(how='all')                          # Drop rows where all values are NULL
df.dropna(thresh=3)                           # Keep rows with at least 3 non-null values
df.dropna(subset=['email', 'phone'])          # Drop if email or phone is NULL
```

**Important**: `fillna()` does NOT fill NaN (floating-point NaN is a distinct value):
```python
df = spark.createDataFrame([(1, float('nan')), (2, None)], ['id', 'value'])
df.fillna(0.0).show()
# Result: id=1 still has NaN (not replaced); id=2 has 0.0 (NULL replaced)
```

### 3.3 Joins

**Basic Syntax**:
```python
df_a.join(df_b, on='id', how='inner')        # Equi-join on id; inner join

df_a.join(df_b, (df_a.id == df_b.emp_id), how='left')  # Complex join condition
```

**Join Types**:

| Type | Description | NULL Rows |
|------|-------------|-----------|
| `inner` | Only matching rows | None |
| `left` (outer) | All left rows + matches from right | Right side NULLs for unmatched left |
| `right` (outer) | All right rows + matches from left | Left side NULLs for unmatched right |
| `full` (outer) | All rows from both sides | Both sides NULLs for unmatched |
| `left_semi` | Left rows where a match exists (no right columns in output) | N/A |
| `left_anti` | Left rows where NO match exists | N/A |
| `cross` | Cartesian product (all combinations) | N/A |

**Broadcasting for Performance**:
```python
from pyspark.sql.functions import broadcast

# Force broadcast if small_df < broadcast threshold
df_large.join(broadcast(small_df), on='id')
```

### 3.4 Set Operations

**Union** (positional alignment):
```python
df_a.union(df_b)        # Combine rows; aligns by position, NOT name
df_a.unionByName(df_b)  # Combine rows; aligns by name (Spark 3.1+)
```

⚠️ **Gotcha**: `union()` aligns columns by position. If schemas differ, column order matters:
```python
df_a = sc.createDataFrame([(1, 'Alice')], ['id', 'name'])
df_b = sc.createDataFrame([('Bob', 2)], ['name', 'id'])

# union() aligns by position:
# Position 0: id(1) from df_a unioned with name('Bob') from df_b → column 1 has 'Bob'!
result = df_a.union(df_b)  # Oops: second row's 'id' is 'Bob' (a string)
```

**Intersect & Subtract**:
```python
df_a.intersect(df_b)    # Rows in both (deduped)
df_a.subtract(df_b)     # Rows in df_a but NOT in df_b (deduped)
```

### 3.5 Grouping and Aggregation

**Single Aggregation**:
```python
df.groupBy('dept').agg(
  F.sum('salary').alias('total'),
  F.avg('salary').alias('avg_salary'),
  F.count('*').alias('headcount')
).show()
```

**Multiple Aggregations with Different Functions**:
```python
df.groupBy('category', 'year') \
  .agg(
    F.sum('revenue').alias('total_revenue'),
    F.count('*').alias('transaction_count'),
    F.max('amount').alias('largest_transaction'),
    F.stddev('amount').alias('std_deviation')
  ) \
  .show()
```

**Deduplicate**:
```python
df.distinct()                          # Remove row duplicates (considers all columns)
df.dropDuplicates(['email', 'dept'])   # Remove rows where email+dept combination is duplicated
```

### 3.6 Repartition vs Coalesce

| Method | Shuffle? | Use Case |
|--------|----------|----------|
| `repartition(n)` | Always | Increase or decrease partitions; distribute by column hash |
| `coalesce(n)` | Only if decreasing | Reduce partitions efficiently (combine adjacent partitions) |

```python
df.repartition(200)                    # Full shuffle; use if increasing partitions
df.coalesce(10)                        # Avoid shuffle if decreasing partitions
df.repartition(10, 'customer_id')      # Hash partition on column
```

**Rule of Thumb**:
- Increasing partitions? Use `repartition()`
- Decreasing partitions? Use `coalesce()`

### 3.7 Schemas and Data Types

**Define Schema Explicitly**:
```python
from pyspark.sql.types import StructType, StructField, IntegerType, StringType, DoubleType

schema = StructType([
  StructField('id', IntegerType(), nullable=False),
  StructField('name', StringType(), nullable=True),
  StructField('salary', DoubleType(), nullable=True),
])

df = spark.createDataFrame(data, schema)
```

**Common Types**:
- `ByteType()`, `ShortType()`, `IntegerType()`, `LongType()` — Integers
- `FloatType()`, `DoubleType()` — Floats
- `StringType()`, `BinaryType()` — Text/binary
- `BooleanType()` — True/False
- `DateType()`, `TimestampType()` — Temporal
- `ArrayType()`, `MapType()`, `StructType()` — Nested
- `DecimalType(precision, scale)` — Fixed-point decimal

**Nested Structures**:
```python
# Access struct field
df.select(col('address.city'))          # Dot notation
df.select(col('address').getField('city'))  # getField()

# Access map value
df.select(col('metadata')['key'])       # Bracket notation
df.select(col('metadata').getItem('key'))  # getItem()

# Access array element
df.select(col('items')[0])              # First element (bracket notation)
df.select(col('items').getItem(0))      # First element (getItem())

# Explode array to rows
df.select(F.explode(col('items')))      # Each array element becomes a row
```

### 3.8 User-Defined Functions (UDFs)

**DataFrame API UDF**:
```python
from pyspark.sql.functions import udf
from pyspark.sql.types import StringType, IntegerType

@udf(returnType=StringType())
def classify(score):
    if score is None:
        return None
    return 'high' if score > 80 else 'low'

df.withColumn('class', classify(col('score'))).show()
```

**SQL-Accessible UDF**:
```python
# Register UDF for use in spark.sql()
spark.udf.register('classify', classify, StringType())

spark.sql('SELECT id, classify(score) as class FROM scores').show()
```

**Important**: Python UDFs are slower than native Catalyst expressions. Prefer built-in functions.

### 3.9 Writing DataFrames

**Write Modes**:
```python
df.write.mode('overwrite').parquet('/output')    # Replace if exists
df.write.mode('append').parquet('/output')       # Append to existing
df.write.mode('ignore').parquet('/output')       # Skip if exists (no error)
df.write.mode('error').parquet('/output')        # Error if exists (default)
```

**Partitioned Write**:
```python
df.write \
  .partitionBy('year', 'month') \
  .mode('overwrite') \
  .parquet('/output/events')

# Creates directory structure:
# /output/events/year=2024/month=01/part-*.parquet
# /output/events/year=2024/month=02/part-*.parquet
# ... columns 'year' and 'month' are removed from data files
```

**Bucketing** (for optimized joins/aggregations):
```python
df.write \
  .bucketBy(10, 'id') \
  .sortBy('id') \
  .mode('overwrite') \
  .parquet('/output/bucketed')

# Creates 10 bucket files, each sorted by 'id'
# Useful for subsequent joins on 'id'
```

### 3.10 Common Pitfalls

| Pitfall | Issue | Solution |
|---------|-------|----------|
| `union()` with different schemas | Columns align by position, not name | Use `unionByName()` for safety |
| `fillna()` doesn't fill NaN | NaN is not NULL | Use `F.isnan()` with `when().otherwise()` |
| Writing to the same path twice | Second write may fail or corrupt files | Use unique paths or `mode('overwrite')` explicitly |
| Forgetting `alias()` after aggregation | Resulting column names are auto-generated | Always use `.alias()` for clarity |
| JOIN creating massive output | Cartesian product from non-equi joins | Double-check join condition logic |

---

## Topic 4: Troubleshooting & Tuning

### 4.1 Using the Spark UI

**Access the UI**:
- **Local mode**: `http://localhost:4040` (active applications)
- **Cluster mode**: `http://<driver-host>:4040`
- **History Server**: `http://<server>:18080`

**Key Tabs**:

| Tab | Insights |
|-----|----------|
| **Jobs** | List of actions (jobs); see status, stages, duration |
| **Stages** | Breakdown of each stage; task counts, duration, shuffle stats |
| **Tasks** | Individual task durations; identify stragglers |
| **Storage** | Cached DataFrames; memory usage and partitions |
| **SQL** | SQL query details; logical/physical plans |

### 4.2 Explain and Physical Plans

**Explain**:
```python
df.explain()                    # Physical plan (short)
df.explain('extended')          # All four plan stages (unresolved → physical)
df.explain('cost')              # Estimated row/byte counts
df.explain('codegen')           # Generated bytecode
```

**Reading Physical Plans**:
```
*(1) FileScan parquet [id#3, name#4] Filters: [(year#5 = 2024)] PushedFilters: [(year = 2024)]
*(1) Filter (year#5 = 2024)
Exchange hashpartitioning(dept#1, 200)
*(2) HashAggregate(keys=[dept#1], functions=[sum(amount#6)])
```

Key observations:
- `*(1)` and `*(2)` indicate different stages (WholeStageCodegen units)
- `Exchange` = shuffle
- `FileScan` with `PushedFilters: []` means predicate NOT pushed down (inefficient)
- `HashAggregate` = aggregation; `SortMergeJoin` = join type

### 4.3 Identifying Performance Problems

**Problem 1: Many Tiny Tasks**
- **Symptom**: Many tasks complete in milliseconds; total job time is long
- **Root Cause**: Too many partitions after a shuffle
- **Fix**: Reduce `spark.sql.shuffle.partitions` or use `coalesce()`

**Problem 2: Data Skew**
- **Symptom**: One or two tasks take 10–100× longer than others
- **Root Cause**: Some partition(s) have much more data than others
- **Fix**:
  - Investigate join/group columns for skew (EXPLAIN shows join strategy)
  - Use AQE skew handling: `spark.sql.adaptive.skewJoin.enabled = true`
  - Consider salting (add random suffix to skew key before grouping)

**Problem 3: Predicate NOT Pushed Down**
- **Symptom**: EXPLAIN shows `PushedFilters: []`; filters run after FileScan
- **Root Cause**: Filter depends on derived column or unsupported expression
- **Fix**: Reorder operations; push source-column filters earlier

**Problem 4: Driver OOM**
- **Symptom**: `OutOfMemoryError: Java heap space` on Driver
- **Root Cause**: Called `collect()` on large DataFrame
- **Fix**: Increase `spark.driver.memory` OR reduce dataset before `collect()`

### 4.4 Adaptive Query Execution (AQE) Recap

AQE makes three runtime optimizations:

1. **Coalescing**: Merge small post-shuffle partitions
2. **Join Strategy Switching**: SortMergeJoin → BroadcastHashJoin if build side is small
3. **Skew Handling**: Split large skewed partitions to avoid stragglers

**Enable**:
```python
spark.conf.set('spark.sql.adaptive.enabled', True)  # Enables all three features
```

### 4.5 Tuning Configurations

| Config | Default | Guidance |
|--------|---------|----------|
| `spark.sql.shuffle.partitions` | 200 | Reduce if many tiny tasks; increase if uneven distribution |
| `spark.sql.autoBroadcastJoinThreshold` | 10 MB | Lower if broadcasts OOM; raise to auto-broadcast larger tables |
| `spark.executor.memory` | 1G | Increase if executor OOM; watch GC logs |
| `spark.driver.memory` | 1G | Increase if driver OOM (e.g., from `collect()`) |
| `spark.sql.adaptive.enabled` | True (3.2+) | Always enable for adaptive optimizations |
| `spark.sql.adaptive.coalescePartitions.enabled` | True (3.2+) | Enable to auto-merge small partitions |
| `spark.sql.adaptive.skewJoin.enabled` | True (3.2+) | Enable to handle partition skew |

### 4.6 Common Pitfalls

| Pitfall | Issue | Fix |
|---------|-------|-----|
| Calling `show()` on large DataFrame | Can take a long time | Use `show(10)` or `limit(10).show()` |
| Not checking EXPLAIN before optimizing | Tuning the wrong thing | Always run `explain('extended')` first |
| Broadcasting a large table | Causes executor OOM | Lower `spark.sql.autoBroadcastJoinThreshold` |
| Ignoring GC logs | Memory pressure going unnoticed | Monitor Spark UI; adjust GC settings if needed |

---

## Topic 5: Structured Streaming

### 5.1 Streaming vs Batch

| Aspect | Batch | Streaming |
|--------|-------|-----------|
| Data | Bounded (all data available) | Unbounded (continuous flow) |
| Processing | One-time full process | Continuous micro-batches |
| DataFrame Property | `isStreaming = False` | `isStreaming = True` |
| Actions | Can use `collect()`, `count()` | Limited actions (mostly `writeStream`) |

### 5.2 Micro-Batch Architecture

Structured Streaming processes data in small batches:

```
Trigger fires → Micro-batch read → Process → Output → Update state → Next batch
```

**Trigger Types**:

| Trigger | Behavior |
|---------|----------|
| `trigger(processingTime='1 second')` | Process when 1 second has elapsed (default) |
| `trigger(once=True)` | Process all available data and stop (good for testing) |
| `trigger(availableNow=True)` | Process all available data with full parallelism and stop (Spark 3.3+) |
| `trigger(continuous='100ms')` | Experimental; low-latency continuous processing |

### 5.3 Output Modes

| Mode | Content | Use Case |
|------|---------|----------|
| `append` | Only newly processed rows | Stateless queries; windowed aggregations with watermark |
| `update` | Updated rows since last batch | Aggregations without watermark (overwrites state) |
| `complete` | Full result table | Aggregations (small tables only) |

**Valid Combinations**:
- Stateless query: only `append` mode
- Aggregation without watermark: `update` or `complete` modes
- Aggregation with watermark: `append`, `update`, or `complete` modes

### 5.4 Event-Time Processing and Watermarks

**Event Time vs Processing Time**:
- **Event Time**: Timestamp when the event occurred (in the data)
- **Processing Time**: Timestamp when Spark processes the event (wall-clock time)

Late-arriving events complicate windowed aggregations:

```python
# Without watermark: all events are processed; no state cleanup
df.groupBy(F.window('timestamp', '5 minutes')).count()

# With watermark: allows late events up to 10 minutes after the window ends
df.withWatermark('timestamp', '10 minutes') \
  .groupBy(F.window('timestamp', '5 minutes')) \
  .count()
```

**Watermark Logic**:
- Tracks the maximum event time seen in the current batch
- Watermark = max_event_time - allowedLateness
- Discards state for windows that are older than the watermark (guaranteed no more late events)
- Allows reprocessing of events up to the watermark threshold

### 5.5 Reading from Sources

**Kafka Source** (most common):
```python
df = spark.readStream \
  .format('kafka') \
  .option('kafka.bootstrap.servers', 'localhost:9092') \
  .option('subscribe', 'topic1,topic2') \
  .load()

# df contains: key (BinaryType), value (BinaryType), timestamp, partition, offset
# Must cast/parse value:
df.select(col('value').cast('string')).show()
```

**File Source** (requires explicit schema):
```python
schema = 'id INT, name STRING, amount DOUBLE'

df = spark.readStream \
  .schema(schema) \
  .csv('/data/streaming')  # Must provide explicit schema
```

### 5.6 Checkpointing for Fault Tolerance

Checkpoints store:
- Processed offset log (where to resume after restart)
- Stateful operator state (e.g., groupBy aggregation state)

```python
df.writeStream \
  .option('checkpointLocation', '/checkpoints/my_query') \
  .outputMode('append') \
  .format('parquet') \
  .start('/output')
```

**Without checkpoint**: On failure, all state is lost; deduplication and watermarks reset.

### 5.7 Stateful Operations

**Stateless** (no state required):
```python
df.filter(col('amount') > 100)  # Each row processed independently
df.select(col('id'), col('amount') * 1.1)
```

**Stateful** (state must be maintained across batches):
```python
df.groupBy('customer_id').count()  # Must remember totals across batches
df.dropDuplicates('id')  # Must remember seen IDs
```

Stateful operations with checkpoint:
```python
df.dropDuplicates('event_id') \
  .writeStream \
  .option('checkpointLocation', '/checkpoints/dedup') \
  .start()
```

### 5.8 Common Pitfalls

| Pitfall | Issue | Fix |
|---------|-------|-----|
| No checkpoint on stateful query | State lost on failure; duplicates/wrong results | Always set `checkpointLocation` for prod |
| Forgetting to parse Kafka value | Binary value not decoded | `cast('string')` or deserialize from JSON/Avro |
| `append` mode without watermark on agg | Results never emitted | Add watermark or use `update`/`complete` mode |
| Ignoring event time skew | Late events silently dropped | Use appropriate watermark threshold |
| `collect()` on streaming DataFrame | Not supported | Use `foreach()` or `foreachBatch()` sink |

---

## Topic 6: Spark Connect

### 6.1 What is Spark Connect?

Spark Connect is a **separation of concerns**:
- **Client**: Lightweight; builds logical plans (no JVM required)
- **Server**: Full Spark cluster; executes logical plans

Benefits:
- **Lightweight Clients**: No JVM overhead on client machine
- **Language Agnostic**: Python, SQL, R clients can connect to same server
- **Better Resource Isolation**: Long-running clients don't consume executor resources

### 6.2 Connection and URL Scheme

```python
from pyspark.sql import SparkSession

# Connect to remote Spark Connect server
spark = SparkSession.builder \
  .remote('sc://hostname:15002') \
  .getOrCreate()

# Everything else is the same
df = spark.read.parquet('/data')
df.filter(col('year') == 2024).show()
```

**URL Scheme**: `sc://` (not `spark://` or `grpc://`)

### 6.3 API Compatibility and Limitations

**What Works** (same as classic Spark):
- DataFrame API: `select()`, `filter()`, `join()`, etc.
- SQL: `spark.sql()` queries
- Streaming (Spark Connect-compatible sources)
- UDFs: Python, scalar, and vector UDFs

**What Does NOT Work**:
- **RDD API**: No `SparkContext`, no `textFile()`, `map()`, `reduce()`, etc.
- **Low-level operations**: No `sc.broadcast()`, `sc.parallelize()` direct access

### 6.4 Spark Connect Architecture

```
Client
  ↓ (gRPC + Protocol Buffers: logical plan)
Spark Connect Server
  ↓ (classifies logical plan as normal Spark DAG)
Spark Driver
  ↓
Executors
  ↑ (results as Apache Arrow batches)
Client (receives Arrow data, converts to Pandas DataFrame)
```

**Data Transfer**: Results are returned as Apache Arrow record batches (efficient columnar format).

### 6.5 Migrating from RDD to Spark Connect

**RDD Code** (NOT supported via Spark Connect):
```python
rdd = sc.textFile('/data/raw.txt')
word_counts = rdd.flatMap(lambda l: l.split()) \
                 .map(lambda w: (w, 1)) \
                 .reduceByKey(lambda a, b: a + b)
```

**DataFrame Equivalent** (works via Spark Connect):
```python
df = spark.read.text('/data/raw.txt')
word_counts = df.select(F.explode(F.split(col('value'), ' ')).alias('word')) \
                .groupBy('word').count() \
                .select(col('word'), col('count'))
```

---

## Topic 7: Pandas API on Spark

### 7.1 Overview

Pandas API on Spark (formerly Koalas) provides a **Pandas-like API** on top of Spark:

```python
import pyspark.pandas as ps  # Note: not 'pandas'

# Read data
ps_df = ps.read_csv('/data/file.csv')

# Pandas-like operations (execute on Spark!)
ps_df[ps_df['age'] > 25].groupby('dept')['salary'].mean()

# Convert back to PySpark
spark_df = ps_df.to_spark()
```

### 7.2 Key Differences from Pandas

| Aspect | Pandas | Pandas API on Spark |
|--------|--------|-------------------|
| Execution | Single-machine in-process | Distributed on Spark cluster |
| Memory Limit | RAM on single machine | Cluster aggregate memory |
| Row Ordering | Deterministic | Non-deterministic (distributed) |
| Speed | Fast for small data (<1GB) | Slow for tiny data (overhead); fast for large |

### 7.3 Common Operations

```python
# Selection
ps_df['column']
ps_df[['col1', 'col2']]
ps_df.loc[0:5]  # Row slicing (limited support)

# Filtering
ps_df[ps_df['age'] > 30]

# Grouping
ps_df.groupby('dept')['salary'].mean()
ps_df.groupby('dept').agg({'salary': 'sum', 'id': 'count'})

# Joining
ps_df1.merge(ps_df2, on='id', how='inner')

# Sorting (non-deterministic order for ties)
ps_df.sort_values('age')

# Concatenation
ps.concat([ps_df1, ps_df2], axis=0)
```

### 7.4 Conversion Between PySpark and Pandas API on Spark

```python
# PySpark DataFrame → Pandas API on Spark
spark_df = spark.read.parquet('/data')
ps_df = ps.from_spark(spark_df)

# Pandas API on Spark → PySpark DataFrame
ps_df.to_spark()

# Pandas API on Spark → Local Pandas (⚠️ DANGER: collects to driver)
ps_df.to_pandas()  # All data moves to driver memory!
```

**⚠️ WARNING**: `to_pandas()` calls `collect()` internally. For large DataFrames, this causes **OutOfMemoryError on the Driver**. Use only for small data.

### 7.5 Index Types and Performance

**Index Types**:
```python
ps.set_option('compute.default_index_type', 'distributed')  # Default
ps.set_option('compute.default_index_type', 'sequence')     # Alternative
```

| Index Type | Behavior | Performance |
|------------|----------|-------------|
| `'distributed'` | Partition-local indices; no global coordination | Fast |
| `'sequence'` | Global sequential integers (0, 1, 2, ...) | Slow (requires global sort/shuffle) |

**Avoid `'sequence'` index for large DataFrames** — it triggers a global sort across all partitions.

### 7.6 Row Order and Determinism

Pandas API on Spark does **NOT** guarantee row ordering for tie-breaking:

```python
ps_df.sort_values('salary')
# For employees with the same salary, their order may differ between runs
# (depends on partition assignment and task execution order)
```

Use `reset_index(drop=True)` if you need stable indices.

### 7.7 Common Pitfalls

| Pitfall | Issue | Fix |
|---------|-------|-----|
| Calling `to_pandas()` on large data | Collects all data to driver → OOM | Only call on small samples |
| Expecting deterministic row order | Ties have non-deterministic ordering | Add a tiebreaker column if needed |
| Using `'sequence'` index for large data | Triggers expensive global sort | Keep default `'distributed'` index |
| Mixing Pandas and Pandas API on Spark | Incompatible APIs (one is single-machine, other is distributed) | Be clear about which library you're using |

---

## Study Tips & Strategies

### 1. Create a Concept Map

Organize topics by relationships:
```
Spark Architecture
  ├─ Driver, Executors, SparkSession
  ├─ Transformations (lazy)
  │   ├─ Narrow (no shuffle)
  │   └─ Wide (shuffle → stage boundary)
  ├─ Actions (eager)
  └─ Fault Tolerance via Lineage
```

### 2. Hands-On Practice

**Set up a local Spark environment**:
```bash
# Using pyspark locally
pip install pyspark
python
>>> from pyspark.sql import SparkSession
>>> spark = SparkSession.builder.appName('test').getOrCreate()
>>> df = spark.read.csv('/path/to/file.csv', header=True)
>>> df.filter(df.age > 25).groupBy('dept').count().show()
```

### 3. Study by Question Type

- **Easy Questions** (20): Vocabulary and basic concepts. Master these to build confidence.
- **Medium Questions** (60): Scenario-based. Understand the "why" behind each answer.
- **Hard Questions** (20): Complex interactions. Connect multiple concepts.

### 4. Time Yourself

When doing practice tests:
- Set a 90-minute timer
- Aim for ~1 minute per question
- Flag hard questions and come back if time permits

### 5. Review Wrong Answers Aggressively

For every mistake, ask:
- What concept did I misunderstand?
- Why was the correct answer better?
- How would I spot this mistake again?

### 6. Use the Answer Key Explanations

The answer key references source topics (e.g., `topic1-prompt3-lazy-evaluation.md`). Use these references to deepen your understanding.

### 7. Teach Someone Else

Explain a concept to a colleague. If you can't explain it clearly, you don't understand it yet.

---

## Quick Reference Checklists

### Spark Architecture Quick Check

- [ ] **Lazy Evaluation**: Understand that transformations don't execute until an action
- [ ] **Wide vs Narrow**: Identify which operations trigger shuffles
- [ ] **Execution Hierarchy**: App → Job → Stage → Task
- [ ] **Broadcast vs Sort-Merge**: Know when to broadcast (< 10 MB threshold)
- [ ] **Persist Storage Levels**: MEMORY_ONLY vs MEMORY_AND_DISK vs SER
- [ ] **Lineage**: Lost partitions are recomputed from DAG

### Spark SQL Quick Check

- [ ] **SparkSession**: Unified entry point for SQL, DataFrames, streaming
- [ ] **Catalyst Optimizer**: Parses → Analyzes → Optimizes → Physical plan
- [ ] **Predicate Pushdown**: Works on source columns; fails on derived columns
- [ ] **Window Functions**: Understand partition, order, and frame specification
- [ ] **Aggregation NULLs**: `count(*)` vs `count(col)`; `sum()` ignores NULLs
- [ ] **AQE**: Coalescing, join strategy switching, skew handling

### DataFrame API Quick Check

- [ ] **Select, Filter, Join**: Core operations are intuitive
- [ ] **NULL vs NaN**: `fillna()` only fills NULLs; use `isnan()` for floats
- [ ] **Union by Position**: `union()` aligns by column order, not name
- [ ] **Repartition vs Coalesce**: Repartition shuffles; coalesce avoids it
- [ ] **Write Modes**: Overwrite, append, ignore, error(default)
- [ ] **Partitioned Writes**: Creates Hive-style directory structure

### Troubleshooting & Tuning Quick Check

- [ ] **Spark UI Port**: Local = 4040; History = 18080
- [ ] **EXPLAIN**: Physical plan; use `'extended'` for all four stages
- [ ] **Identify Skew**: Check max vs median task duration in Spark UI
- [ ] **Tiny Tasks**: Too many partitions; reduce with `coalesce()`
- [ ] **Predicate Not Pushed**: EXPLAIN shows `PushedFilters: []`
- [ ] **AQE Benefits**: Always enable; fixes most optimization issues automatically

### Structured Streaming Quick Check

- [ ] **isStreaming Property**: Check if DataFrame is streaming or batch
- [ ] **Triggers**: `processingTime`, `once`, `availableNow`, `continuous`
- [ ] **Output Modes**: `append` (stateless), `update`/`complete` (stateful)
- [ ] **Watermark**: Define lateness threshold for late-arriving events
- [ ] **Checkpoint**: Store processed offsets and state for fault tolerance
- [ ] **Kafka Source**: Returns binary `value`; must cast/parse

### Spark Connect Quick Check

- [ ] **URL Scheme**: `sc://hostname:15002` (not `spark://`)
- [ ] **No RDD API**: DataFrames and SQL work; RDD/SparkContext don't
- [ ] **Architecture**: Client sends logical plans; server executes; results as Arrow

### Pandas API on Spark Quick Check

- [ ] **Import**: `import pyspark.pandas as ps` (not regular `pandas`)
- [ ] **Conversion**: `ps.from_spark(spark_df)` to create; `.to_spark()` to convert
- [ ] **⚠️ to_pandas()**: Collects to driver; only for small data!
- [ ] **Index Types**: `'distributed'` (fast); `'sequence'` (slow, avoids)
- [ ] **Row Ordering**: Non-deterministic for ties; data is distributed

---

## Final Exam Tips

1. **Read questions carefully**. Many wrong answers are close but subtly incorrect.
2. **Use process of elimination** on tough questions. Often 1–2 answers are clearly wrong.
3. **Watch for absolute statements** ("always", "never"). These are often false traps.
4. **For "select all that apply"**: Read each option independently. One wrong answer doesn't eliminate the whole set.
5. **Manage your time**: Easy questions first, flag hard ones, come back if time permits.
6. **Trust your preparation**: You've studied the concepts. Don't second-guess yourself.

Good luck with your exam! 🎓
