# Databricks Certified Associate Developer for Apache Spark — Study Guide (Iteration 1)

**Edition**: Iteration 1 (100 Questions)
**Generated**: 2026-05-17
**Total Content**: 20,000+ words across 7 topic sections
**Difficulty Split**: 20 Easy / 60 Medium / 20 Hard
**Answer Types**: 77 single-answer / 23 multi-answer
**Study Focus**: Foundational mastery — Architecture, SQL, DataFrame API, Streaming, Spark Connect, Pandas API

---

## Table of Contents

1. [Apache Spark Architecture & Internals](#topic-1-apache-spark-architecture--internals)
2. [Spark SQL](#topic-2-spark-sql)
3. [DataFrame API](#topic-3-dataframe-api)
4. [Troubleshooting & Tuning](#topic-4-troubleshooting--tuning)
5. [Structured Streaming](#topic-5-structured-streaming)
6. [Spark Connect](#topic-6-spark-connect)
7. [Pandas API on Spark](#topic-7-pandas-api-on-spark)

---

## TOPIC 1: Apache Spark Architecture & Internals

**Weight: 20% (Questions 1–20)**

### Driver & Cluster Manager

**Driver Program**

The Driver is the process where your application's `main()` function runs. Its responsibilities:
- Creates the `SparkSession` (and internally, `SparkContext`)
- Converts user code into a logical plan, then into a DAG of Stages
- Schedules Tasks on Executors via the DAGScheduler and TaskScheduler
- Collects results back from Executors when an action is called
- Maintains the application's state (registered accumulators, broadcast vars, etc.)

```
User Code (Driver)
   └── SparkSession
         └── SparkContext
               ├── DAGScheduler     → splits DAG into Stages
               └── TaskScheduler   → sends Tasks to Executors
```

**Cluster Manager (Resource Manager)**

Allocates physical resources (CPU cores, memory) to the Driver and Executors. Spark supports:

| Cluster Manager | Description |
|----------------|-------------|
| **Local** | Single JVM; development only |
| **Standalone** | Spark's built-in; simple; no Hadoop needed |
| **YARN** | Hadoop resource manager; multi-tenant |
| **Kubernetes** | Container-native; cloud-friendly |
| **Mesos** | Legacy; deprecated in Spark 3.2 |

**Executors**

Worker processes that:
- Execute Tasks assigned by the Driver
- Store cached data (in their JVM heap or off-heap)
- Report task results back to the Driver
- Each executor is a long-running JVM process on a worker node

---

### SparkSession vs SparkContext

**SparkContext** (Spark 1.x entry point)
- Low-level API entry point
- Manages connection to cluster manager
- Creates RDDs, broadcasts, accumulators
- One `SparkContext` per JVM

**SparkSession** (Spark 2.0+ unified entry point)
- Wraps `SparkContext`, `SQLContext`, `HiveContext`
- Entry point for: DataFrames, Datasets, Spark SQL, Structured Streaming
- Access underlying context: `spark.sparkContext`
- **Recommended**: Always use `SparkSession` in Spark 2.0+

```python
from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("MyApp") \
    .config("spark.sql.shuffle.partitions", "50") \
    .getOrCreate()

# Access underlying context if needed
sc = spark.sparkContext
```

---

### DAG, Stages, and Tasks

**DAG (Directed Acyclic Graph)**

Spark models computation as a DAG of RDD or DataFrame operations:
- **Nodes**: transformations (each RDD/DataFrame)
- **Edges**: dependencies (narrow or wide)
- Built lazily; only materialised when an action is triggered

**DAGScheduler**

- Converts the DAG into physical Stages
- Handles stage-level fault tolerance (reruns failed stages)
- Submits Stages to the TaskScheduler

**Stage Boundaries**

A new Stage is created at every **wide dependency** (shuffle):

```
Stage 1: read CSV → filter → select    ← narrow transforms (no shuffle)
    ↕  SHUFFLE (e.g., groupBy, join via SortMergeJoin, distinct)
Stage 2: aggregate → sort              ← next stage begins after shuffle
```

**Narrow vs Wide Transformations**

| Type | Definition | Examples | Stage Boundary? |
|------|-----------|----------|-----------------|
| **Narrow** | Each output partition depends on ≤ 1 input partition | `filter`, `select`, `map`, `withColumn`, `limit` | No |
| **Wide** | Output partitions depend on multiple input partitions | `groupBy`, `join` (SortMergeJoin), `distinct`, `orderBy`, `repartition` | Yes (shuffle) |

**Tasks**

- The smallest unit of work in Spark
- **One Task per partition** per Stage
- Tasks run on Executor cores (1 Task uses 1 core)
- Failed Tasks are retried up to `spark.task.maxFailures` (default: 4)

---

### Lazy Evaluation

**Why Lazy?**

Transformations in Spark are NOT executed immediately. They build a query plan. Execution only starts when an **action** is called.

**Benefits of Lazy Evaluation**

1. **Catalyst Optimisation**: Catalyst can reorganise and simplify the plan before execution
2. **Operation Fusion**: Multiple narrow transformations combined into a single pass (no intermediate materialisation)
3. **Lineage-Based Recovery**: Lost partitions recomputed from lineage (no need for full re-scan)
4. **Query Pruning**: Unused columns and rows can be eliminated at planning time

**Transformations vs Actions**

| Category | Behaviour | Examples |
|----------|-----------|----------|
| **Transformation** | Lazy; builds plan only | `filter`, `select`, `join`, `groupBy`, `withColumn`, `map` |
| **Action** | Triggers execution; returns result | `count()`, `show()`, `collect()`, `write.parquet()`, `take(n)`, `first()` |

---

### Partitioning & Parallelism

**Input Partitions**

- Determined by file splits (HDFS block size, Parquet row groups, etc.)
- Configured via `spark.sql.files.maxPartitionBytes` (default: 128 MB)
- More partitions = more parallel tasks; fewer = larger tasks

**Post-Shuffle Partitions**

After a shuffle (`groupBy`, `join`, etc.):
- Configured via `spark.sql.shuffle.partitions` (default: 200)
- Often too high for small data (creates many tiny tasks) and too low for very large data
- AQE (Adaptive Query Execution) can coalesce small post-shuffle partitions automatically

**Default Parallelism**

`spark.default.parallelism` affects RDD operations (not SQL/DataFrame). For DataFrames, use `spark.sql.shuffle.partitions`.

---

### Fault Tolerance

**Lineage-Based Recovery** (for DataFrames/RDDs)

- Spark records the full transformation history (DAG) of each partition
- If a partition is lost (executor failure), it is recomputed from source using the lineage
- No need for explicit replication

**Caching & Checkpointing**

- **`cache()`/`persist()`**: Stores intermediate results; avoids re-computation of expensive transformations; NOT fault-tolerant by default (if executor fails, recomputed from lineage)
- **`checkpoint()`**: Truncates lineage; writes data to reliable storage (HDFS/S3); used when lineage is very long (iterative algorithms)

**Task-Level Retry**

- Tasks are retried up to `spark.task.maxFailures` (default: 4) on different executors
- Speculative execution (`spark.speculation=true`): Launches backup copies of slow tasks

---

### Broadcast Variables & Accumulators

**Broadcast Variables**

- Efficiently distribute large read-only data to all executors (once per node, not per task)
- Use case: Small lookup tables, model parameters
- Automatically used for small tables in joins (BroadcastHashJoin)

```python
lookup = {"US": "United States", "CA": "Canada"}
bc_lookup = sc.broadcast(lookup)

# Access inside transformation:
udf_lookup = udf(lambda code: bc_lookup.value.get(code), StringType())
```

**Accumulators**

- Variables that are only "added" to (associative and commutative)
- Workers can only update (add); Driver reads the final value
- Use case: Counters (e.g., count bad records), sum metrics

```python
bad_records = sc.accumulator(0)

def process_row(row):
    if row['amount'] < 0:
        bad_records.add(1)
    return row

df.rdd.foreach(process_row)
print(f"Bad records: {bad_records.value}")
```

---

## TOPIC 2: Spark SQL

**Weight: 20% (Questions 21–40)**

### Catalyst Optimizer

**Optimisation Pipeline**

```
SQL/DataFrame API
      ↓
Unresolved Logical Plan   (parse SQL; unknown column types)
      ↓ [Analysis]
Resolved Logical Plan     (resolve columns, types, functions)
      ↓ [Logical Optimisation]
Optimised Logical Plan    (predicate pushdown, constant folding, etc.)
      ↓ [Physical Planning]
Physical Plan(s)          (choose join strategy, operator implementation)
      ↓ [Code Generation]
Compiled RDD Code         (optimised JVM bytecode via Tungsten)
```

**Key Logical Optimisations**

| Optimisation | What It Does | Example |
|-------------|-------------|---------|
| **Predicate Pushdown** | Moves filters as close to source as possible (read less data) | `filter` before `join` |
| **Projection Pushdown** | Drops unused columns early (for columnar formats like Parquet) | Only read needed columns |
| **Constant Folding** | Evaluates constant expressions at planning time | `1 + 1` → `2` |
| **Boolean Simplification** | Simplifies boolean expressions | `x AND TRUE` → `x` |
| **Null Propagation** | Resolves null semantics early | `x AND NULL` → `NULL` |

---

### Spark SQL Syntax

**Creating Temp Views**

```python
df.createOrReplaceTempView("employees")
df.createOrReplaceGlobalTempView("global_employees")  # accessible across sessions

# Query using SQL
result = spark.sql("SELECT dept, COUNT(*) as cnt FROM employees GROUP BY dept")
```

**DDL Operations**

```sql
-- Create a table in the metastore
CREATE TABLE IF NOT EXISTS sales (
    id INT,
    amount DOUBLE,
    date DATE
) USING PARQUET;

-- Create from query
CREATE TABLE silver_sales AS
SELECT * FROM bronze_sales WHERE amount > 0;

-- Add partition
ALTER TABLE sales ADD PARTITION (year=2025);
```

**DML Operations**

```sql
INSERT INTO sales VALUES (1, 100.0, '2025-01-01');
INSERT OVERWRITE sales SELECT * FROM new_sales;
```

---

### Join Types

| Type | Rows Returned | Common Use Case |
|------|--------------|-----------------|
| `INNER` | Matching rows only | Standard join |
| `LEFT` / `LEFT OUTER` | All left rows + matching right | Keep all left rows |
| `RIGHT` / `RIGHT OUTER` | Matching left + all right rows | Keep all right rows |
| `FULL` / `FULL OUTER` | All rows from both sides | Union with null-fill |
| `LEFT SEMI` | Left rows that have a match (no right columns) | Filter by existence |
| `LEFT ANTI` | Left rows that have NO match | Find unmatched rows |
| `CROSS` | Cartesian product | All combinations |

---

### Window Functions

**Syntax**

```python
from pyspark.sql.window import Window
from pyspark.sql.functions import row_number, rank, dense_rank, lag, lead, sum as spark_sum

w = Window.partitionBy("dept").orderBy("salary")

df = df.withColumn("row_num", row_number().over(w)) \
       .withColumn("rank",    rank().over(w)) \
       .withColumn("d_rank",  dense_rank().over(w))
```

**Ranking Functions Compared**

Given salaries: 100, 200, 200, 300

| Function | Results | Explanation |
|----------|---------|-------------|
| `row_number()` | 1, 2, 3, 4 | Unique; arbitrary for ties |
| `rank()` | 1, 2, 2, 4 | Ties get same rank; gap after ties |
| `dense_rank()` | 1, 2, 2, 3 | Ties get same rank; NO gap |

**Aggregate Window Functions**

```python
w_all = Window.partitionBy("dept").rowsBetween(Window.unboundedPreceding, Window.currentRow)

df = df.withColumn("running_total", spark_sum("sales").over(w_all))
```

---

### Aggregations

**Standard Aggregation**

```python
from pyspark.sql.functions import count, sum, avg, min, max, countDistinct

df.groupBy("dept") \
  .agg(
      count("*").alias("total"),
      avg("salary").alias("avg_salary"),
      countDistinct("employee_id").alias("unique_employees")
  )
```

**Rollup & Cube**

```python
# ROLLUP: Subtotals along hierarchy (dept → total)
df.rollup("dept", "year").agg(sum("sales"))

# CUBE: All combinations of grouping columns
df.cube("dept", "year").agg(sum("sales"))
```

**GROUPING SETS** (SQL only)

```sql
SELECT dept, year, SUM(sales)
FROM fact_sales
GROUP BY GROUPING SETS ((dept, year), (dept), ())
```

---

## TOPIC 3: DataFrame API

**Weight: 30% (Questions 41–70)**

### Schema & Data Types

**Schema Definition**

```python
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, DoubleType

schema = StructType([
    StructField("id", IntegerType(), nullable=False),
    StructField("name", StringType(), nullable=True),
    StructField("salary", DoubleType(), nullable=True),
])

df = spark.read.schema(schema).csv("/data/employees.csv")
```

**DDL Schema String**

```python
# Shorter syntax:
df = spark.read.schema("id INT NOT NULL, name STRING, salary DOUBLE").csv("/data/employees.csv")
```

**Type Coercion**

Spark automatically casts types where possible. Explicit casting:

```python
from pyspark.sql.functions import col
df = df.withColumn("salary_int", col("salary").cast("int"))
```

---

### Column Operations

**Selecting Columns**

```python
df.select("id", "name")                    # by name
df.select(col("id"), col("name"))          # using col()
df.select(df["id"], df["name"])            # using df[]
df.select("*")                             # all columns
```

**Filtering Rows**

```python
df.filter(col("salary") > 50000)
df.filter("salary > 50000")               # SQL string predicate
df.where(col("dept").isin(["HR", "IT"]))
df.filter(col("name").isNotNull())
```

**Adding/Modifying Columns**

```python
df.withColumn("bonus", col("salary") * 0.1)
df.withColumn("salary", col("salary").cast("double"))  # overwrite existing
df.withColumnRenamed("salary", "annual_salary")
df.drop("temp_col")
```

---

### Sorting & Deduplication

**Sorting**

```python
df.orderBy("salary")                           # ascending (default)
df.orderBy(col("salary").desc())               # descending
df.orderBy(col("dept").asc(), col("salary").desc_nulls_last())
df.sort("salary", ascending=False)             # alias
```

**Deduplication**

```python
df.distinct()                                  # all columns unique
df.dropDuplicates(["id"])                      # unique on specific columns
df.dropDuplicates(["id", "date"])
```

---

### Joins

**Join Syntax**

```python
# Basic join
result = df1.join(df2, on="employee_id", how="inner")

# Multiple keys
result = df1.join(df2, on=["id", "dept"], how="left")

# Different column names
result = df1.join(df2, df1["emp_id"] == df2["employee_id"], how="inner")
```

**Join Strategies**

| Strategy | Trigger | Configuration |
|----------|---------|---------------|
| BroadcastHashJoin | One side < 10 MB threshold | `spark.sql.autoBroadcastJoinThreshold` |
| SortMergeJoin | Default for large tables; both sides sorted | Default for large joins |
| ShuffleHashJoin | One side small; hash table in memory | Controlled by optimizer |
| BroadcastNestedLoopJoin | Non-equi joins; last resort | Automatic |

---

### Reading & Writing Data

**CSV**

```python
df = spark.read.option("header", True) \
               .option("inferSchema", True) \
               .option("delimiter", ",") \
               .csv("/data/input.csv")

df.write.option("header", True) \
        .mode("overwrite") \
        .csv("/output/path")
```

**Parquet**

```python
df = spark.read.parquet("/data/input.parquet")
df.write.partitionBy("year", "month").parquet("/output/path")
```

**Delta Lake**

```python
df = spark.read.format("delta").load("/delta/table")
df.write.format("delta").mode("overwrite").save("/delta/table")
```

**Write Modes**

| Mode | Behaviour |
|------|-----------|
| `overwrite` | Delete existing data; write new |
| `append` | Add to existing data |
| `error` (default) | Fail if data exists |
| `ignore` | Skip write if data exists |

---

### User-Defined Functions (UDFs)

**Python UDF**

```python
from pyspark.sql.functions import udf
from pyspark.sql.types import StringType

def categorise_salary(salary):
    if salary is None:
        return "Unknown"
    return "High" if salary > 100000 else "Low"

salary_udf = udf(categorise_salary, StringType())
df = df.withColumn("category", salary_udf(col("salary")))
```

**UDF Limitations**

- Python UDFs break JVM execution; data serialised/deserialised between JVM and Python
- Cannot benefit from Catalyst optimisation
- Performance penalty vs built-in functions

**Pandas UDF (Vectorised UDF)**

```python
from pyspark.sql.functions import pandas_udf
import pandas as pd

@pandas_udf(DoubleType())
def tax_calculator(salary: pd.Series) -> pd.Series:
    return salary * 0.2

df = df.withColumn("tax", tax_calculator(col("salary")))
```

Pandas UDFs use Apache Arrow for efficient data transfer; much faster than Python UDFs.

---

### Built-in Functions Reference

**String Functions**

```python
from pyspark.sql.functions import upper, lower, trim, concat, split, substring, regexp_replace

df.withColumn("upper_name", upper(col("name")))
df.withColumn("initials", substring(col("name"), 1, 1))
df.withColumn("parts", split(col("full_name"), " "))
df.withColumn("cleaned", regexp_replace(col("text"), "[^a-zA-Z]", ""))
```

**Date Functions**

```python
from pyspark.sql.functions import current_date, datediff, date_add, date_format, to_date, year, month

df.withColumn("today", current_date())
df.withColumn("days_since", datediff(current_date(), col("hire_date")))
df.withColumn("year_hired", year(col("hire_date")))
df.withColumn("formatted", date_format(col("hire_date"), "yyyy-MM-dd"))
```

**Null Handling**

```python
from pyspark.sql.functions import coalesce, isnull, isnan, when

df.withColumn("safe_salary", coalesce(col("salary"), lit(0)))
df.fillna({"salary": 0, "dept": "Unknown"})
df.dropna(subset=["id", "salary"])
df.filter(col("salary").isNotNull())
```

**Conditional Logic**

```python
from pyspark.sql.functions import when, lit

df.withColumn("band",
    when(col("salary") > 100000, "Senior")
    .when(col("salary") > 50000, "Mid")
    .otherwise("Junior")
)
```

---

## TOPIC 4: Troubleshooting & Tuning

**Weight: 10% (Questions 71–80)**

### Common Performance Issues

**Data Skew**

*Problem*: One partition has disproportionately more data → that task takes much longer than others.

*Symptoms*: Most tasks finish in seconds; a few tasks take minutes; Stage stragglers in Spark UI.

*Solutions*:
1. **Salting**: Add random prefix to skewed keys; unsalt after aggregation
2. **AQE Skew Join**: `spark.sql.adaptive.skewJoin.enabled=true` (default in Spark 3.x)
3. **Broadcast Join**: If one side is small enough
4. **Repartition**: `df.repartition(n, col("key"))` to spread data

**Small Files Problem**

*Problem*: Many tiny files → many tasks with low work; task scheduling overhead dominates.

*Solutions*:
1. `df.coalesce(n)` — reduce partition count before writing (no shuffle; only reduces)
2. `df.repartition(n)` — redistribute to exactly N partitions (causes shuffle)
3. **Delta Lake `OPTIMIZE`**: Compacts small files into target size

**OOM (Out of Memory)**

*Problem*: Executor runs out of memory.

*Symptoms*: "GC overhead limit exceeded", task retries, executor lost.

*Solutions*:
- Reduce partition size (increase partition count)
- Increase `spark.executor.memory`
- Use `.persist(StorageLevel.DISK_ONLY)` or avoid caching large DFs
- Check for accidental `collect()` on very large DataFrames

---

### Caching Strategy

**When to Cache**

- DataFrame used more than once in the same application
- Expensive computation (many joins/aggregations) before multi-use
- Iterative algorithms (ML training loops)

**When NOT to Cache**

- DataFrame used only once
- Large DataFrame that won't fit in memory (will trigger eviction loops)
- Data that changes (stale cache)

**Cache vs Persist**

```python
df.cache()  # == df.persist(StorageLevel.MEMORY_AND_DISK)
df.persist(StorageLevel.MEMORY_ONLY)
df.persist(StorageLevel.MEMORY_ONLY_SER)
df.unpersist()  # Release cache when done
```

---

### Spark UI Key Metrics

| Tab | What to Look For |
|-----|-----------------|
| **Jobs** | Failed jobs; slow jobs vs expected |
| **Stages** | Long-running stages; data skew (task duration histogram) |
| **Tasks** | Duration outliers; GC time; shuffle read/write |
| **Storage** | Cached DataFrames; fraction in memory vs disk |
| **SQL** | Query plans; predicate pushdown evidence |

---

### Tuning Configuration Reference

| Config | Default | Tune When |
|--------|---------|-----------|
| `spark.sql.shuffle.partitions` | 200 | Too small for large data; too large for small data |
| `spark.sql.autoBroadcastJoinThreshold` | 10 MB | Increase if executors have more memory |
| `spark.executor.memory` | 1 GB | Increase if OOM errors |
| `spark.executor.cores` | 1 | Set to 4-5 for batch jobs |
| `spark.sql.adaptive.enabled` | true (Spark 3.x) | AQE handles many tuning tasks automatically |

---

## TOPIC 5: Structured Streaming

**Weight: 10% (Questions 81–90)**

### Streaming Concepts

**Micro-Batch vs Continuous Processing**

| Mode | Latency | Throughput | Use Case |
|------|---------|-----------|----------|
| **Micro-Batch** (default) | ~1 second | High | Most streaming workloads |
| **Continuous Processing** | ~1 millisecond | Lower | Ultra-low latency; limited operations |

**Trigger Modes**

```python
# Default micro-batch: Process as fast as possible
query = df.writeStream.trigger(processingTime="0 seconds").start()

# Fixed interval micro-batch
query = df.writeStream.trigger(processingTime="10 seconds").start()

# Once: Process all available data; then stop
query = df.writeStream.trigger(once=True).start()

# Available Now: Like Once but multiple micro-batches
query = df.writeStream.trigger(availableNow=True).start()
```

---

### Sources & Sinks

**Common Streaming Sources**

```python
# Kafka
df = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "broker:9092") \
    .option("subscribe", "my-topic") \
    .load()

# Rate (for testing)
df = spark.readStream.format("rate").option("rowsPerSecond", 100).load()

# File source (reads new files added to directory)
df = spark.readStream \
    .schema(schema) \
    .parquet("/streaming/input/")
```

**Common Streaming Sinks**

```python
# Console (testing)
query = df.writeStream.format("console").start()

# Delta Lake
query = df.writeStream \
    .format("delta") \
    .option("checkpointLocation", "/checkpoints/delta") \
    .start("/delta/output")

# Kafka
query = df.writeStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "broker:9092") \
    .option("topic", "output-topic") \
    .start()
```

---

### Output Modes

| Mode | Rows Written | Requires | Use Case |
|------|-------------|----------|----------|
| **Append** | New rows only | Watermark (if aggregation) | Simple log-style outputs |
| **Complete** | All rows of result table | Aggregation | Small result sets (e.g., dashboard) |
| **Update** | Changed rows only | Aggregation | Efficient sink (e.g., database upsert) |

---

### Watermarking & Late Data

```python
from pyspark.sql.functions import window

df.withWatermark("event_time", "10 minutes") \
  .groupBy(window("event_time", "5 minutes")) \
  .count()
```

**Watermark Semantics**
- Tracks `max(event_time) − delay` as the watermark
- Events arriving BEFORE watermark are dropped (too late)
- State for windows older than watermark is evicted (memory freed)
- **Append mode** only safe with watermark (guarantees no future updates to closed windows)

---

### Checkpointing & Fault Tolerance

```python
query = df.writeStream \
    .option("checkpointLocation", "/path/to/checkpoint") \
    .format("delta") \
    .start()
```

**What Checkpoint Stores**
1. **Offsets**: Where we are in each source (Kafka offsets, file lists)
2. **Commits**: Which batches have been successfully written
3. **State**: Current aggregation state (for stateful operations)

**Exactly-Once Semantics**
Requires:
1. **Replayable source** (e.g., Kafka with committed offsets, file source)
2. **Idempotent or transactional sink** (e.g., Delta Lake)
3. **Checkpoint location** for offset tracking

---

## TOPIC 6: Spark Connect

**Weight: 5% (Questions 91–95)**

### What Is Spark Connect?

Introduced in Apache Spark 3.4, **Spark Connect** provides a decoupled client–server architecture for Spark:

```
Client (Python/Scala/Java/R)      Server (JVM Spark)
  ├── SparkSession (thin client) ──── gRPC ────> SparkConnectServer
  ├── Local plan building                        └── Remote execution
  └── Lazy plan serialisation                    └── Results streamed back
```

**Key Differences from Classic Spark**

| Feature | Classic Spark | Spark Connect |
|---------|--------------|---------------|
| Driver location | Same process as user code | Remote (server-side) |
| Connection | Direct JVM | gRPC over network |
| Plan building | JVM in-process | Client-side (serialised protobuf) |
| `SparkContext` | Always available | Not available on client |
| Use case | Local/embedded | Remote/multi-tenant |

---

### Spark Connect Use Cases

1. **Notebooks & IDEs**: Connect to a remote Spark cluster without heavyweight driver process
2. **Multi-tenant clusters**: Multiple users connect to a shared Spark server
3. **Thin clients**: Lightweight Python script connects to big Spark cluster
4. **CI/CD**: Run Spark queries against remote cluster from test environment

---

### Limitations of Spark Connect

- `SparkContext` is not available (no low-level RDD operations from client)
- Accumulators and broadcast variables have limited support
- Some legacy APIs unavailable
- Slightly higher latency (gRPC round-trips for plan building)

---

### Connecting to a Spark Connect Server

```python
from pyspark.sql import SparkSession

# Connect to remote Spark Connect server
spark = SparkSession.builder \
    .remote("sc://localhost:15002") \
    .getOrCreate()

# Use same DataFrame API as classic Spark
df = spark.read.parquet("/remote/data/")
df.groupBy("dept").count().show()
```

---

## TOPIC 7: Pandas API on Spark

**Weight: 5% (Questions 96–100)**

### What Is the Pandas API on Spark?

Formerly known as **Koalas** (databricks/koalas), the Pandas API on Spark (`pyspark.pandas`) allows developers to write pandas-style code that executes on Spark.

```python
import pyspark.pandas as ps

# Read data (returns Spark-backed pandas-like DataFrame)
df = ps.read_csv("/data/employees.csv")

# Use familiar pandas syntax
result = df.groupby("dept")["salary"].mean()
print(result)
```

---

### Pandas API vs PySpark DataFrame API

| Aspect | Pandas API on Spark | PySpark DataFrame API |
|--------|--------------------|-----------------------|
| Syntax | Pandas-compatible | Spark-native |
| Target user | Pandas users migrating to Spark | Spark-native users |
| Operations | Pandas-style (`.loc`, `.iloc`, etc.) | `select`, `filter`, `groupBy` |
| Execution | Spark under the hood | Spark under the hood |
| Lazy evaluation | No (more eager) | Yes (lazy) |
| Performance | Slightly less optimised | Fully optimised |

---

### Converting Between APIs

```python
import pyspark.pandas as ps
from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate()

# Spark DataFrame → Pandas API on Spark
ps_df = spark_df.pandas_api()

# Pandas API on Spark → Spark DataFrame
spark_df = ps_df.to_spark()

# Pandas API on Spark → local pandas
pandas_df = ps_df.to_pandas()  # Careful: collects all data to driver!
```

---

### Pandas API Limitations

- **Not a full pandas replacement**: Some operations not supported or behave differently
- **No guaranteed row order**: Spark DataFrames are unordered (index handling differs from pandas)
- **Performance**: Some pandas operations trigger large shuffles on Spark
- **Index semantics**: Spark DataFrames don't have a natural index; Pandas API emulates it

---

### Default Index Types

```python
# Default: sequence index (0, 1, 2, ...) — consistent but can be slow for large data
ps.set_option("compute.default_index_type", "sequence")

# Distributed: partitioned index — faster but non-contiguous
ps.set_option("compute.default_index_type", "distributed")

# Distributed-sequence: best of both (costly for very large data)
ps.set_option("compute.default_index_type", "distributed-sequence")
```

---

## Critical Concepts Rapid Review

### Must-Know Facts

| Concept | Key Fact |
|---------|----------|
| SparkSession | Unified entry point in Spark 2.0+; wraps SparkContext |
| Actions | Trigger execution; examples: `count()`, `show()`, `collect()`, `write.*` |
| Narrow transforms | No shuffle; same stage; examples: `filter`, `select`, `withColumn` |
| Wide transforms | Cause shuffle; new stage; examples: `groupBy`, `join` (SortMergeJoin), `distinct`, `orderBy` |
| `spark.sql.shuffle.partitions` | Controls post-shuffle partition count (default: 200) |
| Broadcast join threshold | `spark.sql.autoBroadcastJoinThreshold` (default: 10 MB) |
| `row_number` vs `rank` vs `dense_rank` | row_number: unique; rank: gaps; dense_rank: no gaps |
| Lazy evaluation | Transformations deferred; action triggers execution |
| Cache location | MEMORY_AND_DISK (default for `cache()`); explicit with `persist()` |
| Exactly-once streaming | Replayable source + idempotent sink + checkpoint |
| Spark Connect | gRPC-based remote architecture; no SparkContext on client |
| Pandas API on Spark | `pyspark.pandas`; pandas syntax on Spark engine |
| Append mode | Only new rows to sink; requires watermark for aggregations |
| Complete mode | Entire result table each micro-batch; requires aggregation |
| UDF penalty | Python UDFs serialise/deserialise across JVM; prefer built-ins or pandas UDF |
