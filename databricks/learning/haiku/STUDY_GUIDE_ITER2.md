# Databricks Certified Associate Developer for Apache Spark — Iteration 2 Study Guide

**Comprehensive learning material based on the updated 100-question exam bank (Iteration 2)**

**Last Updated**: May 17, 2026

---

## Overview

This study guide covers all 7 topics in the Databricks Spark certification exam, with specific attention to iteration-2 question patterns. Use this alongside the exam questions to build deep understanding.

**Key Differences in Iteration-2**:
- Deeper coverage of Spark architecture (deploy modes, cluster managers, executor memory)
- Additional streaming concepts (Delta Lake sources, version compatibility)
- More nuanced window function edge cases
- Expanded Spark Connect discussion

---

## Topic 1: Apache Spark Architecture & Internals (20% - Questions 1–20)

### 1.1 Local Mode vs Cluster Mode

**Local Mode** (`local[*]`):
- Single JVM process on submitting machine
- `local[*]` uses **all available logical CPU cores** as worker threads
- Ideal for development, testing, small datasets
- No cluster required

**Cluster Mode Deployment**:

| Aspect | Client Mode | Cluster Mode |
|--------|------------|--------------|
| **Driver Location** | Submitting machine | Worker node inside cluster |
| **Submit Machine Disconnect** | Kills Driver, job fails | Job continues; client can reconnect |
| **Logs Location** | Submitting machine | Worker node that runs Driver |
| **Best For** | Development, interactive notebooks | Production jobs, CI/CD pipelines |
| **Risk** | Submit machine failure = total job loss | Isolated from submit machine issues |

**Flag**: Use `--deploy-mode client` or `--deploy-mode cluster` with `spark-submit`.

### 1.2 Cluster Manager URIs & Ports

| Cluster Manager | Master URI | Default Port | Spark UI Port | History Server |
|-----------------|-----------|------------|---|---|
| **Local** | `local[*]` | N/A | 4040 | N/A |
| **Standalone** | `spark://hostname:PORT` | **7077** | 4040 | 18080 (shared) |
| **YARN** | `yarn` (client) or `yarn` (cluster) | YARN handles | 4040 | 19888 (YARN) |
| **Kubernetes** | `k8s://https://...:6443` | K8s API | 4040 | Varies |

**Key Point**: The Standalone master listens on **7077** for Driver registration and Task scheduling.

### 1.3 Dynamic Resource Allocation (DRA)

**What It Does**:
- Automatically adds Executors when Tasks queue up (no available Executors)
- Automatically removes idle Executors after `spark.dynamicAllocation.executorIdleTimeout` (default 60s)
- Reduces wasted resources in multi-tenant environments

**Requirements**:
- External Shuffle Service (so shuffle files outlive Executor removal)
- Enabled: `spark.dynamicAllocation.enabled = true`
- Compatible with YARN, Standalone, and Kubernetes

### 1.4 Executors, Drivers, and Memory

**Unified Memory Model**:
```
Executor Heap = spark.executor.memory (e.g., 4 GB)
  ├─ Spark Memory (spark.memory.fraction × heap) — 60% by default = 2.4 GB
  │  ├─ Storage Memory (cache, broadcast variables)
  │  └─ Execution Memory (shuffle buffers, sort, hash joins)
  ├─ User Memory (40% by default = 1.6 GB)
  └─ Reserved (some JVM overhead)

Off-Heap Memory = spark.executor.memoryOverhead (default 10% × executor.memory)
  └─ OS overhead, Python worker processes, native libraries
```

**Tuning Tips**:
- `spark.executor.memoryOverhead`: Increase for PySpark (Python workers), ML libraries (pandas, numpy)
- `spark.memory.fraction`: Typically leave at 0.6; increase if caching dominates
- `spark.executor.cores`: 4–5 cores per Executor is optimal; higher values degrade HDFS throughput

### 1.5 Accumulators: Shared Variables for Count/Sum

**What Are Accumulators**:
- Distributed variables that only support **associative and commutative** additions
- Tasks can only **write** (increment); only the Driver can **read** the final value
- Common use: counting events, summing values across Tasks

```python
counter = spark.sparkContext.accumulator(0)
# In a UDF or foreachPartition:
counter.add(1)  # Each Task adds to counter

# On Driver after action:
total = counter.value  # Only now can Driver see the sum
```

**Critical Misconception**:
- ❌ Tasks can read accumulator values
- ✅ Tasks see the **initial value** (e.g., 0) if they try to read; only Driver sees the final accumulated value after the action

### 1.6 Broadcast Variables

**What They Are**:
- Large read-only objects (lookup tables, ML models) that must be efficiently distributed to all Executors
- Spark serializes once and caches on each Executor; Tasks read locally without network transfer

**Usage**:
```python
lookup = spark.sparkContext.broadcast({'A': 1, 'B': 2})
# In UDF or Task:
value = lookup.value['A']  # Access via .value
```

**Key Points**:
- Created on Driver; serialized once; cached on all Executors
- Access via `.value` attribute to unwrap the broadcast wrapper
- Automatically re-sent if an Executor fails
- Destroyed via `.destroy()` or automatically when `SparkContext` stops

### 1.7 Lazy Evaluation & The DAG

**Lazy Evaluation**:
- Transformations (`.filter()`, `.select()`, `.groupBy()`) do **not** execute immediately
- Only **actions** (`.count()`, `.show()`, `.write()`, `.collect()`) trigger execution
- Spark builds a Directed Acyclic Graph (DAG) of transformations; Catalyst optimizes the full plan before execution

**Actions** (trigger execution):
- `count()`, `collect()`, `show()`, `first()`, `take(n)`
- `write.parquet()`, `write.csv()`, `write.format()`
- `foreach()`, `foreachPartition()`, `saveAsTextFile()`

**Transformations** (lazy; return DataFrame):
- `filter()`, `select()`, `withColumn()` (narrow — no shuffle)
- `groupBy()`, `orderBy()`, `join()`, `distinct()` (wide — triggers shuffle)

### 1.8 Stages, Tasks, and Shuffles

**Execution Hierarchy**:
```
Application
  └─ Job (triggered by each action)
    └─ Stage (split at shuffle boundaries)
      └─ Task (one per partition, executes in parallel on available cores)
```

**Narrow vs Wide Transformations**:

| Type | Definition | Examples | Shuffle? | Stage Boundary? |
|------|-----------|----------|----------|-----------------|
| **Narrow** | Each output partition depends on ≤1 input partition | filter, select, withColumn | No | No |
| **Wide** | All-to-all redistribution; each output depends on all inputs | groupBy, orderBy, join | Yes | Yes |

**Stage Counting**:
- Start with 1 stage
- Add 1 stage for each wide transformation (shuffle boundary)
- Example: `read.parquet → groupBy → orderBy → write` = 3 stages

### 1.9 Caching & Persistence

**`cache()` vs `persist()`**:
- `cache()` is shorthand for `persist(StorageLevel.MEMORY_AND_DISK)`
- DataFrame `cache()` defaults to `MEMORY_AND_DISK` (not RDD's `MEMORY_ONLY`)
- `persist()` allows custom storage level

**Storage Levels**:

| Level | Storage | Spill to Disk | Serialized | Replication | Use Case |
|-------|---------|---------------|-----------|------------|----------|
| `MEMORY_ONLY` | Heap | ❌ (dropped) | ❌ (objects) | ❌ | Fast; recompute from lineage if lost |
| `MEMORY_AND_DISK` | Heap + local disk | ✅ | ❌ | ❌ | Balanced; large DataFrames |
| `MEMORY_ONLY_SER` | Heap | ❌ (dropped) | ✅ (binary) | ❌ | Slow deserialize; saves memory |
| `DISK_ONLY` | Local disk | ✅ | ✅ | ❌ | Very large; low memory systems |
| `*_2` | Any of above | + | + | ✅ (2 copies) | Fault tolerance; big shuffle |

**Lazy Materialization**:
- `cache()` marks the DataFrame for caching but doesn't materialize until the next **action** executes
- `unpersist()` removes cached blocks from memory, freeing storage

### 1.10 Speculative Execution

**What It Does**:
- Detects straggler Tasks (unusually slow)
- Launches duplicate copies of the stragglers on other Executors
- Whichever finishes first wins; duplicates are cancelled
- Reduces job latency from slow nodes/tasks

**Configuration**: `spark.speculation = true` (disabled by default)

### 1.11 Fault Tolerance via Lineage

**How Spark Recovers Lost Partitions**:
1. Every transformation is recorded as a step in the DAG (lineage)
2. If an Executor fails and loses partitions, Spark recomputes them from the lineage
3. Recomputation uses the original source data (no re-read of source files, only rerun the operations)

---

## Topic 2: Spark SQL (20% - Questions 21–40)

### 2.1 SparkSession & Catalog API

**SparkSession** (Spark 2.0+):
- Unified entry point for DataFrame, SQL, and Streaming operations
- Replaces SparkContext + SQLContext

```python
spark.read.parquet()              # DataFrame API
spark.sql("SELECT * FROM table")  # SQL API
spark.readStream...               # Streaming
spark.catalog.listTables()        # Catalog API
```

### 2.2 Temporary Views

**Scope**:

| Type | Scope | Lifetime | Visibility | Method |
|------|-------|----------|-----------|--------|
| **Temp View** | Session | Session duration | Only current session | `createTempView()` |
| **Global Temp View** | App-wide | App duration | All sessions in app | `createGlobalTempView()` |
| **Replace Variant** | — | — | Overwrites if exists | `createOrReplaceXxx()` |

**Error Handling**:
- `createTempView('name')` raises `AnalysisException` if `name` already exists
- `createOrReplaceTempView('name')` overwrites silently
- `dropTempView('name')` via `spark.catalog.dropTempView()`

### 2.3 Catalyst Optimizer

**Catalyst Optimization Pipeline**:
1. **Parsing**: SQL string → Abstract Syntax Tree (AST)
2. **Analysis**: Resolve column names, table references, data types → Logical Plan
3. **Optimization**: Apply rule-based rewrites
   - **Predicate Pushdown**: Move filters to earliest point (ideally before FileScan)
   - **Projection Pushdown**: Select only required columns
   - **Constant Folding**: Simplify expressions
   - **Join Reordering**: Apply CBO to reorder joins for efficiency
4. **Physical Planning**: Generate executable plans with physical operators

**Key Insight**: Predicate pushdown only works on **source columns**, not derived columns.

```python
# ✅ Pushed down to FileScan
df.filter(col('year') == 2024).select('event_id')

# ❌ NOT pushed down (predicate on derived column)
df.withColumn('year_bucket', col('year') // 10).filter(col('year_bucket') == 202)
```

### 2.4 Adaptive Query Execution (AQE)

**Runtime Optimizer** (enabled by default in Spark 3.2+):
- Coalesces small partitions after a shuffle (reduces tiny tasks)
- Switches join strategies at runtime (e.g., from SortMergeJoin to BroadcastHashJoin if one side is small)
- Detects and mitigates data skew by dynamically splitting skewed partitions

**Configuration**:
```python
spark.conf.set('spark.sql.adaptive.enabled', True)
spark.conf.set('spark.sql.adaptive.coalescePartitions.enabled', True)
spark.conf.set('spark.sql.adaptive.skewJoin.enabled', True)
```

### 2.5 Window Functions

**Concepts**:
- **Partition**: Group of rows for independent window calculation
- **Order**: Sort order within each partition
- **Frame**: Subset of rows relative to current row (e.g., current row ± N rows)

**Function Types**:

| Category | Functions | Notes |
|----------|-----------|-------|
| **Ranking** | `rank()`, `dense_rank()`, `row_number()` | rank() skips after ties; dense_rank() doesn't |
| **Percentile** | `percent_rank()`, `cume_dist()`, `ntile(n)` | percent_rank: [0, 1]; cume_dist: (0, 1] |
| **Aggregate** | `sum()`, `avg()`, `min()`, `max()`, `count()` | Over window with optional frame |
| **Lag/Lead** | `lag(col, offset)`, `lead(col, offset)` | Returns null at boundary (first/last row) |
| **First/Last** | `first()`, `last()` | First/last row in window frame |

**Edge Cases**:
- `lead()` on the last row returns `null` (no next row)
- `lag()` on the first row returns `null` (no prior row)
- Both accept a `default` parameter to replace `null`

### 2.6 Cost-Based Optimizer (CBO)

**Requirement**: Table statistics must be collected via `ANALYZE TABLE table_name COMPUTE STATISTICS`

**Benefits**:
- Optimal join order (reduces intermediate data volume)
- Correct join strategy selection (BroadcastHashJoin vs SortMergeJoin)

### 2.7 Built-In Functions

**String/Array/Map Functions**:

| Function | Behavior |
|----------|----------|
| `F.split(col, delimiter)` | Returns `ArrayType(StringType)` |
| `F.explode(col)` | One output row per array element; drops null/empty arrays |
| `F.explode_outer(col)` | Preserves null/empty arrays as single null row |
| `F.array_contains(col, value)` | Boolean: does array contain value? |
| `F.concat_ws(sep, col_or_array)` | Joins array elements with separator; skips nulls |
| `F.to_json(col)` | Serializes struct/map to JSON StringType |

**Date/Time Functions**:

| Function | Return Type | Notes |
|----------|------------|-------|
| `F.date_add(col, days)` | DateType | Adds days to date |
| `F.datediff(end, start)` | IntegerType | Days between two dates |
| `F.date_format(col, pattern)` | StringType | Formats date as string (e.g., `'yyyy-MM-dd'`) |
| `F.current_timestamp()` | TimestampType | Evaluated once at query start; same for all rows |

**Null-Safe Functions**:

| Function | Behavior |
|----------|----------|
| `F.coalesce(col1, col2, col3)` | First non-null value |
| `F.fillna(value)` | Replace nulls with value |
| `F.isNull()` / `F.isNotNull()` | Boolean tests |

**Other Functions**:

| Function | Purpose |
|----------|---------|
| `F.lit(value)` | Create literal Column object |
| `F.approx_count_distinct(col)` | HyperLogLog approximate distinct count |
| `F.when(condition, value)` | Conditional: if true return value |
| `F.case()` | Multi-way branching |

### 2.8 Conditional Expressions

**In PySpark**:
```python
F.when(col('score') > 80, 'high') \
  .when(col('score') > 50, 'medium') \
  .otherwise('low')
```

**In SQL (via selectExpr or expr)**:
```python
selectExpr("CASE WHEN score > 80 THEN 'high' WHEN score > 50 THEN 'medium' ELSE 'low' END AS grade")
selectExpr("IF(score > 80, 'high', IF(score > 50, 'medium', 'low')) AS grade")
selectExpr("IIF(score > 80, 'high', 'low') AS grade")
selectExpr("NULLIF(score, 0) AS adjusted_score")  # Returns null if score == 0
```

### 2.9 Grouping & Aggregation

**groupBy() Output**:
- Grouping key columns appear **first** in result schema
- Aggregate columns follow in order specified in `agg()`

**Advanced Grouping**:
```python
df.groupBy('dept').rollup('dept', 'quarter').sum('sales')      # Hierarchical subtotals
df.groupBy('dept').cube('dept', 'quarter').sum('sales')        # All combinations
df.groupBy().agg(F.sum('revenue'))                             # Single group (grand total)
```

### 2.10 GROUPING SETS

**Purpose**: Compute multiple grouping combinations in one pass

```python
spark.sql("""
  SELECT region, category, SUM(amount)
  FROM sales
  GROUP BY GROUPING SETS ((region), (category), ())
""")
```

Produces:
- Rows grouped by region (category = null)
- Rows grouped by category (region = null)
- Grand total row (both = null)

---

## Topic 3: DataFrame API (30% - Questions 41–70)

### 3.1 Basic Operations

**Selection & Projection**:
```python
df.select('col1', 'col2')                          # By name
df.select(col('col1'), col('col2') * 2)           # Column expressions
df.drop('col1')                                    # Remove column
df[df.columns[0]]                                  # Subscript (returns Series)
```

**Filtering**:
```python
df.filter(col('age') > 25)
df.where((col('age') > 25) & (col('salary') > 50000))  # Compound (AND)
```

### 3.2 NULL Handling

**Detection & Filling**:
```python
df.isNull()                       # Boolean column
df.isNotNull()                    # Boolean column
df.fillna(0)                      # Fill all nulls with 0
df.fillna({'col1': 0, 'col2': ''}) # Column-specific fills
df.dropna()                       # Drop rows with any null
df.dropna(thresh=2)               # Keep rows with ≥2 non-null values
df.na.drop(subset=['email'])      # Drop if email is null
```

**NaN (Not a Number)**:
- `fillna()` fills `NULL` only, not NaN
- Use `F.isnan(col)` to detect NaN
- Replace NaN with `F.when(F.isnan(col), value).otherwise(col)`

### 3.3 Adding/Modifying Columns

```python
df.withColumn('bonus', col('salary') * 0.1)  # Add/replace
df.withColumnRenamed('old', 'new')            # Rename
df.drop('col1', 'col2')                       # Remove multiple
```

### 3.4 Joins

**Equi-Join** (most common):
```python
df_orders.join(df_customers, on='id', how='inner')
```

**Complex Condition**:
```python
df_a.join(df_b, (df_a.id == df_b.emp_id) & (df_a.date == df_b.event_date), 'inner')
```

**Broadcast Hint**:
```python
df_large.join(broadcast(df_small), on='id')       # DataFrame hint
df_large.join(df_small.hint('broadcast'), on='id')  # SQL hint
```

**Join Types**:

| Type | Behavior | Ambiguous Columns |
|------|----------|-------------------|
| `'inner'` | Matching rows only | Both sides kept as separate columns |
| `'left'` | All left rows; right nulls where no match | Same |
| `'right'` | All right rows; left nulls | Same |
| `'full'` | All rows from both; nulls where no match | Same |
| `'left_semi'` | Left rows with match in right (no right cols) | Not applicable |
| `'left_anti'` | Left rows with NO match in right | Not applicable |
| `'cross'` | Cartesian product | All columns from both |

**Ambiguous Column Issue**:
```python
result = df_orders.join(df_customers, df_orders.id == df_customers.id)
# result.select('id')  # ERROR: ambiguous (both have 'id')
# result.select(df_orders.id)  # OK: explicit reference
# result.select(df_orders.id, df_customers.id)  # OK: both columns
```

### 3.5 Set Operations

**By Position** (default):
```python
df_a.union(df_b)           # Aligns by position, not name!
df_a.unionByName(df_b)     # Aligns by name (safer)
```

**Other Set Ops**:
```python
df_a.intersect(df_b)       # Rows in both
df_a.subtract(df_b)        # Rows in df_a, not in df_b
```

### 3.6 Grouping & Aggregation

**Basic**:
```python
df.groupBy('dept').count()
df.groupBy('dept').agg(F.sum('salary'), F.avg('salary'), F.countDistinct('id'))
```

**Result Schema**:
- Grouping columns appear first
- Aggregate columns follow in order specified

### 3.7 Repartition & Coalesce

| Operation | Shuffle? | Use Case |
|-----------|----------|----------|
| `repartition(200)` | ✅ Yes | Increase or decrease partitions |
| `repartition(10, col('id'))` | ✅ Yes | Hash partition by column |
| `coalesce(10)` | ✅ (only if increasing) | Merge adjacent partitions; avoid shuffle if decreasing |

**Key Insight**: `coalesce(10)` when you have 200 partitions avoids a full shuffle (merges adjacent partitions). But `coalesce(200)` when you have 10 partitions still shuffles.

### 3.8 Writing DataFrames

**Modes**:

| Mode | Behavior | Data Preserved? |
|------|----------|-----------------|
| `'overwrite'` | Delete and replace | ❌ No |
| `'append'` | Add to existing | ✅ Yes |
| `'ignore'` | Do nothing if exists | ✅ Yes |
| `'error'` | Raise exception if exists | ✅ Yes |

**Partitioning**:
```python
df.write.partitionBy('year', 'month').parquet('/output')
# Creates year=2024/month=01/, year=2024/month=02/, etc.
```

**Schema Merging**:
```python
spark.read.option('mergeSchema', True).parquet('/output')
# Reads schema from all files and merges (nullable columns for missing)
```

### 3.9 Reading Files

**Text**:
```python
spark.read.text('/data/file.txt')  # One 'value' column (StringType)
```

**CSV**:
```python
spark.read.csv('/data/file.csv', header=True)
```

**JSON**:
```python
spark.read.json('/data/file.json')                          # One JSON object per line
spark.read.option('multiline', True).json('/data/file.json')  # Multi-line JSON
```

### 3.10 Schemas & Data Types

**struct Access**:
```python
col('address.city')           # Dot notation
col('address').getField('city')  # getField()
```

**Array Access**:
```python
col('items')[0]               # First element
col('items').getItem(0)       # First element (getItem)
F.explode(col('items'))       # Explode to rows
```

### 3.11 Advanced DataFrame Operations

**`toDF()` Rename**:
```python
df.toDF('col1', 'col2', 'col3')  # Rename all columns by position
```

**`when().otherwise()` Chaining**:
```python
# Both forms are equivalent:
F.when(col('score') > 80, 'A').when(col('score') > 50, 'B').otherwise('C')
F.when(col('score') > 80, 'A').otherwise(F.when(col('score') > 50, 'B').otherwise('C'))
```

**Window Functions in DataFrames**:
```python
from pyspark.sql import Window
w = Window.partitionBy('dept').orderBy('salary').rowsBetween(Window.unboundedPreceding, Window.currentRow)
df.withColumn('running_sum', F.sum('salary').over(w))
```

**Partition Pruning**:
```python
df = spark.read.parquet('/data/events')  # Written with .partitionBy('country')
df.filter(col('country') == 'US')       # Spark prunes to only country=US/ directory
```

**Schema Evolution**:
- Parquet supports schema merging with `.option('mergeSchema', True)`
- Missing columns in old files are filled with null
- New columns in old files are silently ignored

### 3.12 UDFs

**Standard Python UDF** (slow per-row):
```python
@F.udf(returnType='string')
def process(x):
    return x.upper()

df.withColumn('upper_text', process(col('text')))
```

**Pandas UDF** (vectorized, fast):
```python
@F.pandas_udf('string')
def process(batch):
    return batch.str.upper()
```

**Performance**: Pandas UDFs use Apache Arrow for columnar batch transfer between JVM and Python worker → **10–100× faster** than per-row Python UDFs.

---

## Topic 4: Troubleshooting & Tuning (10% - Questions 71–80)

### 4.1 Spark UI Access

```
Local:           http://localhost:4040
Standalone:      http://driver-host:4040
Standalone UI:   http://master-host:8080
History Server:  http://server-host:18080
```

### 4.2 EXPLAIN & Physical Plans

```python
df.explain()                    # Short physical plan
df.explain('extended')          # All 4 stages (unresolved, analyzed, optimized, physical)
df.explain('cost')              # With row/byte estimates
df.explain('codegen')           # Generated bytecode
```

**Reading Physical Plans**:
- `Exchange` = shuffle (expensive)
- `FileScan` with `PushedFilters: []` = filter not pushed (inefficient)
- `BroadcastHashJoin` vs `SortMergeJoin` = join strategy choice
- `*(1)`, `*(2)` = WholeStageCodegen unit boundaries
- Partition count at each stage indicates parallelism

### 4.3 Performance Tuning

**Problem: Too Many Small Tasks**
- Symptom: Many tasks complete in milliseconds
- Cause: Too many partitions after shuffle
- Fix: Reduce `spark.sql.shuffle.partitions` or use `coalesce()`

**Problem: Data Skew**
- Symptom: One task 10–100× slower than others
- Cause: Uneven data distribution on join/group key
- Fix: Enable AQE skew handling; consider salting

**Problem: Executor OOM**
- Symptom: `OutOfMemoryError: Java heap space` on Executors
- Cause: Not enough memory for in-flight data
- Fix: Increase `spark.executor.memory`; reduce `spark.sql.shuffle.partitions`; increase `spark.executor.cores` to limit concurrency

**Problem: Driver OOM During `collect()`**
- Symptom: `OutOfMemoryError` on Driver after `collect()`
- Cause: Collected data exceeds Driver heap
- Fix: Increase `spark.driver.memory` OR reduce data before collect

### 4.4 Configurations

**Shuffle**:
```python
spark.conf.set('spark.sql.shuffle.partitions', 50)  # Default 200; tune based on data
spark.conf.set('spark.sql.autoBroadcastJoinThreshold', '10MB')  # Auto-broadcast threshold
```

**Executor**:
```python
spark.conf.set('spark.executor.cores', 4)              # 4–5 cores optimal
spark.conf.set('spark.executor.memory', '4g')          # Heap memory
spark.conf.set('spark.executor.memoryOverhead', '512m') # Off-heap (PySpark, ML libs)
```

**Memory**:
```python
spark.conf.set('spark.memory.fraction', 0.6)           # 60% for Spark Memory
```

**Speculation**:
```python
spark.conf.set('spark.speculation', True)              # Enable straggler detection
```

### 4.5 Salting for Skew Mitigation

**Steps**:
1. Add random salt (0 to N-1) to large skewed DataFrame's join key
2. Replicate small DataFrame N times, each with different salt (0 to N-1)
3. Join on composite key (original key + salt)
4. Aggregate results if needed (remove salt after join)

### 4.6 Executor Cores Tuning

**Best Practice**: 4–5 cores per Executor
- Balances parallelism with per-Executor overhead
- High core counts (20+) degrade HDFS throughput (thread contention on single HDFS client)
- Very low core counts (1–2) reduce parallelism

### 4.7 Debugging: setLogLevel

```python
spark.sparkContext.setLogLevel('ERROR')  # Show only ERROR messages
```

---

## Topic 5: Structured Streaming (10% - Questions 81–90)

### 5.1 Streaming Fundamentals

**Micro-Batch Model**:
- Input stream divided into micro-batches
- Each micro-batch treated as a bounded DataFrame
- Executed as Spark SQL jobs in sequence

**Streaming vs Batch**:
- Streaming: Unbounded data arrival; continuous processing
- Batch: Bounded data; one-time processing

### 5.2 StreamingQuery Object

```python
query = df.writeStream.start()  # Returns StreamingQuery

query.status              # Current status (ACTIVE, STOPPED, etc.)
query.lastProgress        # Metrics from last micro-batch
query.awaitTermination()  # Blocks until query stops
query.stop()              # Stop the query
```

### 5.3 Triggers

```python
.trigger(processingTime='1 second')   # Micro-batch every 1 second
.trigger(once=True)                   # Process all available data in single batch; stop
.trigger(availableNow=True)           # (Spark 3.3+) Process all available in multiple batches; stop
.trigger(continuous='1 second')       # Continuous mode (experimental)
```

### 5.4 Output Modes

| Mode | Use Case | Stateful Agg | Stateless Ops |
|------|----------|---|---|
| `'append'` | Windowed agg with watermark; stateless queries | ✅ (with watermark) | ✅ |
| `'update'` | Non-windowed agg; update on state change | ✅ | ❌ |
| `'complete'` | Full result needed; small data only | ✅ | ❌ |

### 5.5 Event-Time & Watermarks

**Event-Time Processing**:
- `event_time` column: When data was generated
- Processing-time: When Spark processes the data
- Event-time allows handling of late-arriving data

**Watermarks**:
```python
df.withWatermark('event_time', '10 minutes') \
  .groupBy(F.window('event_time', '5 minutes')) \
  .count()
```

Watermark = max_event_time - 10 minutes

- Events older than watermark are considered "late" and dropped
- Allows Spark to finalize windows and clean up state
- Essential for append mode with windowed aggregations

### 5.6 Checkpoints

**Purpose**:
- Store offsets (input positions)
- Store aggregation state
- Enable exactly-once semantics and recovery

```python
.option('checkpointLocation', '/checkpoints/my_query') \
```

**Mandatory for**:
- Stateful aggregations (groupBy, dropDuplicates)
- Exactly-once delivery
- Recovery after failure

### 5.7 Sources & Sinks

**Common Sources**:
- Kafka, Kinesis, Event Hubs (fault-tolerant; support replay)
- File source (supports Parquet, CSV, JSON, ORC)
- Rate source (for testing; generates monotonically increasing values)
- Socket source (for testing only; not fault-tolerant)
- Delta Lake (supports exactly-once semantics and version replay)

**Common Sinks**:
- File (Parquet, CSV, JSON, ORC)
- Kafka, Kinesis, Event Hubs
- Console (print to stdout)
- Memory (in-memory table for SQL queries)
- Delta Lake (supports exactly-once, schema enforcement)
- `foreachBatch()` (custom processing; allows multiple sinks per batch)

### 5.8 Delta Lake as Source/Sink

**Benefits**:
- Transaction log enables exactly-once semantics
- Can replay from any historical version or timestamp
- Enforces schema on write; fails on incompatible changes
- Supports both streaming source and sink simultaneously

---

## Topic 6: Spark Connect (5% - Questions 91–95)

### 6.1 Architecture

**Classic Spark**:
- Py4J socket bridge between Python and JVM
- Driver runs in application process
- App crash = Driver crash = job failure

**Spark Connect** (gRPC client-server):
- gRPC over HTTP/2 (not Py4J)
- Protocol Buffers for request serialization
- Apache Arrow for result batches
- Driver runs separately on cluster
- Client crash ≠ job failure; client can reconnect

### 6.2 Connection

```python
from pyspark.sql import SparkSession

spark = SparkSession.builder \
  .remote('sc://hostname:15002') \
  .getOrCreate()
```

**Default Port**: 15002

### 6.3 Client Requirements

- No local JVM required
- Spark Connect Python library only
- Any language with gRPC support can be a client (Go, Rust, Java, Python, etc.)

### 6.4 Capabilities

**Supported**:
- DataFrame API
- SQL API
- Structured Streaming
- Caching, RDD-like distributed operations

**Not Supported**:
- RDD API (classic Spark's `.parallelize()`, `.map()`, `.reduce()`)
- Broadcast variables (limited support)
- Accumulators (limited support)

### 6.5 Version Compatibility

- Spark Connect supports version negotiation
- A 3.4 client can interoperate with a 3.5 server
- Teams can upgrade client and server libraries independently

---

## Topic 7: Pandas API on Spark (5% - Questions 96–100)

### 7.1 Import & Conversion

**Import**:
```python
import pyspark.pandas as ps  # Recommended (Spark 3.2+)
# Legacy:
import databricks.koalas as ks  # Deprecated but still works
```

**Conversion**:
```python
pdf = pandas.DataFrame(...)
psdf = ps.from_pandas(pdf)  # pandas → pyspark.pandas
psdf = ps.from_spark(sdf)   # PySpark DataFrame → pyspark.pandas

sdf = psdf.to_spark()       # pyspark.pandas → PySpark (distributed!)
pdf = psdf.to_pandas()      # pyspark.pandas → pandas (collects to Driver!)
```

**⚠️ Warning**: `to_pandas()` collects all data to the Driver — only use on small results!

### 7.2 Index Types

**Default** (`'distributed-sequence'`):
- Uses partition ID + within-partition row offset
- Globally unique; no shuffle required
- Not strictly sequential (gaps between partitions)
- Fast; recommended for most use cases

**`'sequence'`**:
- Strictly sequential integers (0, 1, 2, 3, ...)
- Requires global sort (full shuffle)
- Expensive; only use if strict sequencing is required

### 7.3 Operations

- Most pandas API methods work: `.groupby()`, `.agg()`, `.join()`, `.merge()`, `.rolling()`, etc.
- Under the hood: distributed on cluster via PySpark
- Row ordering is non-deterministic for tied values (no guaranteed order)

### 7.4 Best Practices

- Use `'distributed-sequence'` (default) for most use cases
- Avoid `to_pandas()` on large results
- Use `to_spark()` to convert back to PySpark DataFrame (distributed)

---

## Study Tips & Strategies

### Concept Linking

When you learn a concept, link it to:
1. **Real-world scenario**: How is this used in production?
2. **Related concept**: What other concepts depend on this?
3. **Code example**: How do you code it?
4. **Exam question**: Which exam question tests this?

### Active Recall

- ❌ Re-read the guide
- ✅ Close the guide and explain the concept aloud
- ✅ Answer related exam questions from scratch
- ✅ Write code examples without looking

### Spaced Repetition

- Day 1: Learn concept, answer 3 questions
- Day 3: Re-answer same 3 questions
- Day 7: Re-answer same 3 questions
- Day 14: Final check

---

**End of Study Guide (Iteration 2)**

This guide covers all material in the updated exam bank. Combine it with the QUICK_REFERENCE_ITER2 for rapid review and PRACTICE_STRATEGY_ITER2 for structured study planning.
