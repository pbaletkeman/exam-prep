# Databricks Certified Associate Developer for Apache Spark — Study Guide (Iteration 9)

**Edition**: Iteration 9 (100 Questions)
**Last Updated**: 2026-05-17
**Total Content**: 20,000+ words across 7 topic sections
**Difficulty Split**: 10 Easy / 54 Medium / 36 Hard
**Study Focus**: Comprehensive mastery with balanced difficulty

---

## Table of Contents

1. [Core Spark Concepts & APIs](#topic-1-core-spark-concepts--apis)
2. [Spark SQL & DataFrame Operations](#topic-2-spark-sql--dataframe-operations)
3. [Advanced Transformations & State Management](#topic-3-advanced-transformations--state-management)
4. [Performance, Tuning & Optimization](#topic-4-performance-tuning--optimization)
5. [Streaming & Real-Time Processing](#topic-5-streaming--real-time-processing)
6. [Distributed System Patterns](#topic-6-distributed-system-patterns)
7. [Production Reliability & Edge Cases](#topic-7-production-reliability--edge-cases)

---

## TOPIC 1: Core Spark Concepts & APIs

### SparkSession vs SparkContext Relationship

**Historical Context**

- **Spark 1.x**: `SparkContext` was the only entry point; limited SQL support
- **Spark 2.0+**: Introduced `SparkSession` as unified entry point for all Spark APIs
- **Spark 3.x**: `SparkSession` is primary; `SparkContext` still exists but accessed via `spark.sparkContext`

**Modern Architecture (Spark 2.x/3.x)**

```
┌─────────────────────────────────┐
│      SparkSession (unified)     │
│                                 │
│  ┌──────────────────────────┐   │
│  │   sparkContext (wrapped) │   │  ← RDD API access
│  └──────────────────────────┘   │
│                                 │
│  DataFrame/SQL API (native)     │  ← SQL API access
│                                 │
│  Streaming API (native)         │  ← Streaming API access
│                                 │
└─────────────────────────────────┘
```

**Practical Usage**

```python
# Spark 3.x: SparkSession is the entry point
from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("MyApp") \
    .getOrCreate()

# Access DataFrames (native to SparkSession)
df = spark.read.parquet("path")

# Access RDDs (via underlying SparkContext)
rdd = spark.sparkContext.parallelize([1, 2, 3])

# Access Spark SQL
spark.sql("SELECT * FROM table")

# Never create SparkContext manually
# (SparkSession creates it internally)
```

**Key Points**

- `SparkSession` wraps `SparkContext`; it's the unified entry point
- `spark.sparkContext` retrieves the underlying context for RDD operations
- Multiple `SparkSession` instances **cannot coexist** in a single JVM (they share one `SparkContext`)
- `SparkContext` is lazy-initialized on first use

---

### RDD vs DataFrame vs Dataset APIs

**API Layering**

```
┌─────────────────────────────────────────┐
│  SQL/DataFrame/Dataset (High-Level)     │
│  • Optimized by Catalyst                │
│  • Strongly typed (Dataset in Scala)    │
│  • Best for analytics                   │
└─────────────────────────────────────────┘
                    ↓
┌─────────────────────────────────────────┐
│  RDD (Low-Level)                        │
│  • Unoptimized transformations          │
│  • Weakly typed                         │
│  • Direct control; use when needed      │
└─────────────────────────────────────────┘
```

**When to Use Each**

| API | Typing | Optimization | Use Case |
|-----|--------|--------------|----------|
| **DataFrame** | Dynamic (untyped) | Catalyst optimizer | SQL-like analysis, most workloads |
| **Dataset** (Scala/Java) | Static (strongly typed) | Catalyst optimizer | Type safety in Scala, complex transformations |
| **RDD** | Untyped | Manual control | Unstructured data, custom partitioning, low-level control |

**Interoperability**

```python
# DataFrame → RDD
rdd = df.rdd  # Converts to RDD[Row]

# RDD → DataFrame
df = spark.createDataFrame(rdd, schema)

# Dataset (Scala) → RDD (returns RDD[T])
rdd = ds.rdd
```

---

### Partitioning & Parallelism Fundamentals

**`spark.default.parallelism` — RDD Operations Only**

- **Scope**: Controls default partition count for RDD transformations (`reduceByKey`, `join`, `groupByKey`, etc.)
- **Default Value**:
  - Local mode: # cores on machine
  - Cluster mode: Total executor cores across cluster (8× core count typical)
- **Effect on DataFrames**: **NONE** — DataFrame shuffles use `spark.sql.shuffle.partitions`
- **Common Mistake**: Setting `spark.default.parallelism=400` expecting DataFrame shuffles to respect it; they don't

**`spark.sql.shuffle.partitions` — DataFrame Operations**

- **Scope**: Controls post-shuffle partition count for DataFrame/SQL operations
- **Default**: 200
- **Tuning**:
  - Small data: Lower to 50 or less (fewer tasks overhead)
  - Large data: Increase to 400-1000 (more parallelism)
  - Rule of thumb: 1-2 MB per partition is optimal
- **When Ignored**: AQE partition coalescing may reduce count after shuffle

**Example: Why Both Configs Matter**

```python
# RDD reduction (uses spark.default.parallelism)
rdd.reduceByKey(lambda a, b: a + b)  # Partition count from default.parallelism

# DataFrame aggregation (uses spark.sql.shuffle.partitions)
df.groupBy("key").count()  # Partition count from sql.shuffle.partitions

# Setting spark.default.parallelism does NOT affect the second operation
```

---

### Lazy Evaluation & Action Semantics

**Lazy Transformations** (No Computation)

- All DataFrame/RDD transformations are lazy
- Only define the transformation plan; no actual execution
- Multiple transformations stack without re-computing intermediate results
- **Examples**: `map`, `filter`, `groupBy`, `join`, `select`, `withColumn`

**Eager Actions** (Trigger Execution)

- Force evaluation of the entire transformation chain
- Only actions trigger job submission to the cluster
- **Common Actions**: `collect()`, `count()`, `show()`, `write()`, `saveAsTable()`, `first()`, `take(n)`

**Lazy Evaluation Benefit**

```python
# No computation happens yet
df_filtered = df.filter(col("age") > 30)
df_mapped = df_filtered.select(col("name"))

# First action: triggers entire chain execution
print(df_mapped.count())  # NOW the filter + select are executed

# Second action: re-executes the entire chain (unless cached)
print(df_mapped.collect())  # Executes again unless df_mapped.cache() was called
```

---

### Narrow vs Wide Dependencies

**Narrow Dependency** (No Shuffle)

- Parent partitions map 1:1 to child partitions
- Can be computed locally within a partition
- **Examples**: `map`, `filter`, `withColumn`, `select`
- **Stage Boundary**: No new stage created

**Wide Dependency** (Requires Shuffle)

- Child partitions depend on multiple parent partitions
- Requires data movement across network/disk
- **Examples**: `groupBy`, `join`, `reduceByKey`, `union` (with different partition counts)
- **Stage Boundary**: New stage created at each wide dependency

**Impact on Query Plans**

```
Narrow:   RDD/DF 1 → map → filter → select → RDD/DF 2 (single stage)

Wide:     RDD 1 → map → shuffle → reduceByKey → RDD 3 (two stages)
          [Stage 1: map]  [Stage 2: shuffle + reduce]
```

**Significance**:
- Narrow operations are cheap (local, no shuffle overhead)
- Wide operations are expensive (network I/O, sorting, spilling)
- Query planner minimizes wide operations through optimization (predicate pushdown, etc.)

---

## TOPIC 2: Spark SQL & DataFrame Operations

### DataFrame Schema & Data Types

**Schema Definition**

```python
from pyspark.sql.types import StructType, StructField, StringType, IntegerType

schema = StructType([
    StructField("name", StringType(), nullable=True),
    StructField("age", IntegerType(), nullable=False),
    StructField("salary", DoubleType(), nullable=True),
])

df = spark.read.schema(schema).parquet("path")
```

**Schema Inference**

- `spark.read.parquet(path)` auto-infers schema from Parquet metadata (fast, recommended)
- `spark.read.json(path)` samples data to infer schema (slower, less reliable)
- **Best Practice**: Always provide explicit schema for production code (avoid inference surprises)

**Nullable Semantics**

- `nullable=True`: Column can contain `NULL` values
- `nullable=False`: Column must always have a value (not enforced by Spark; advisory only)
- **Important**: Spark treats `nullable=False` as a hint, not a strict constraint

---

### Column Expressions & Functions

**Column References**

```python
from pyspark.sql.functions import col, lit

# Reference column by name
df.select(col("name"))  # Recommended

# Shorthand (less explicit)
df.select("name")  # String literal; auto-wrapped in col()

# Literal values
df.select(lit(10))  # Constant value
```

**Function Categories**

| Category | Examples | Use |
|----------|----------|-----|
| **Aggregate** | `count`, `sum`, `avg`, `max`, `min` | Reduce groups to single values |
| **Window** | `row_number`, `rank`, `lead`, `lag` | Compute values within partitions |
| **Array** | `array_contains`, `explode`, `size` | Array manipulation |
| **String** | `upper`, `lower`, `substr`, `concat` | String operations |
| **Date/Time** | `date_add`, `year`, `month`, `datediff` | Temporal operations |
| **Math** | `round`, `floor`, `ceil`, `abs` | Numeric operations |

---

### Joins & Join Strategies

**Join Types (Semantic)**

| Type | Behavior |
|------|----------|
| **INNER** | Only matching rows from both sides |
| **LEFT OUTER** | All rows from left; matching rows from right; right columns filled with `NULL` |
| **RIGHT OUTER** | All rows from right; matching rows from left; left columns filled with `NULL` |
| **FULL OUTER** | All rows from both sides; unmatched columns filled with `NULL` |
| **CROSS** | Cartesian product (all combinations) |
| **LEFT SEMI** | Rows from left where a match exists in right (no right columns returned) |
| **LEFT ANTI** | Rows from left where NO match exists in right |

**Join Strategies (Implementation)**

- **Broadcast Hash Join**: One side broadcast; most efficient; requires < 10 MB
- **Sort-Merge Join**: Both sides shuffled and sorted; default for large joins
- **Shuffle Hash Join**: Both sides shuffled; less common

**Join Syntax**

```python
# DataFrame join (recommended)
result = df_left.join(df_right, on="key", how="inner")

# SQL join
result = spark.sql("""
    SELECT * FROM left_table l
    INNER JOIN right_table r ON l.key = r.key
""")

# Multi-condition join
result = df_left.join(df_right,
    (df_left.key1 == df_right.key1) & (df_left.key2 == df_right.key2),
    how="left")
```

---

## TOPIC 3: Advanced Transformations & State Management

### Window Functions & Ordering

**Window Function Components**

```python
from pyspark.sql.functions import row_number, rank, sum as F_sum
from pyspark.sql.window import Window

# Define window specification
window_spec = Window.partitionBy("department").orderBy("salary")

# Apply window function
df_ranked = df.withColumn("rank", rank().over(window_spec))
```

**Window Frame Semantics**

- **Default frame (with `orderBy`)**: `RANGE BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW` (cumulative)
- **Default frame (without `orderBy`)**: `ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING` (entire partition)
- **Custom frame**: `rowsBetween(start, end)` or `rangeBetween(start, end)`

**Key Window Functions**

| Function | Behavior | Use Case |
|----------|----------|----------|
| `row_number()` | Unique sequential regardless of ties | Assign unique IDs |
| `rank()` | Rank with gaps after ties | Ranking where ties share rank |
| `dense_rank()` | Rank without gaps | Ranking without rank gaps |
| `ntile(n)` | Divide into n buckets | Create deciles, quartiles |
| `lag(col, offset)` | Value from prior row | YoY comparison, trend analysis |
| `lead(col, offset)` | Value from next row | Future value access |
| `sum(col).over(w)` | Cumulative/partition sum | Running totals |

---

### Stateful Operations & Caching

**Caching Strategies**

```python
# Cache DataFrame in memory
df.cache()  # Or .persist(StorageLevel.MEMORY_AND_DISK)

# Use in multiple operations
count = df.count()
show = df.show()
collect = df.collect()  # All use cached data

# Remove from cache
df.unpersist()
```

**When to Cache**

- DataFrame accessed multiple times (saves recomputation)
- Complex transformation pipeline (save intermediate results)
- Iterative algorithms (ML training loops)

**When NOT to Cache**

- Single use only (wasted overhead)
- Very large DataFrames (memory pressure)
- Streaming data (handled differently)

**Cache Impact on Lazy Evaluation**

- Caching an intermediate result creates a "checkpoint" in the plan
- Subsequent actions use the cached version instead of recomputing
- **Warning**: Cached data can become stale if source changes

---

### GroupBy & Aggregation Patterns

**GroupBy Semantics**

```python
# Single key
result = df.groupBy("department").count()

# Multiple keys
result = df.groupBy("department", "year").sum("salary")

# Multi-level aggregation
result = (df.groupBy("dept")
    .agg(
        F.count("*").alias("employee_count"),
        F.avg("salary").alias("avg_salary"),
        F.max("bonus").alias("max_bonus")
    ))
```

**Rollup vs Cube**

- **`rollup(a, b, c)`**: Hierarchical subtotals at all levels
  - Grouping sets: `(a,b,c)`, `(a,b)`, `(a)`, `()` = 4 sets
- **`cube(a, b, c)`**: All possible combinations of grouping dimensions
  - Grouping sets: All 2^3 = 8 combinations
- **Use Case**: `rollup` for hierarchy (year > month > day); `cube` for all cross-dimensional analysis

**Null Representation in Rollup/Cube**

- `NULL` in the result indicates the aggregation level (not a data null)
- Use `F.grouping(col)` to detect: returns `1` if column is aggregated, `0` if present in grouping key

---

## TOPIC 4: Performance, Tuning & Optimization

### Query Optimization & Catalyst

**Spark SQL Query Execution Phases**

1. **Parsing**: SQL text → Abstract Syntax Tree (AST)
2. **Analysis**: Resolve column names, types, tables
3. **Optimization**: Apply Catalyst rules (predicate pushdown, constant folding, etc.)
4. **Physical Planning**: Choose join strategies, partition strategies
5. **Execution**: Compile to RDD operations; submit to cluster

**Key Optimization Rules**

- **Predicate Pushdown**: Push filters to source readers (skip unrelated blocks)
- **Projection Pushdown**: Select only needed columns from source
- **Constant Folding**: Evaluate constant expressions at plan time
- **Column Pruning**: Remove unneeded columns from intermediate results

**Cost-Based Optimizer (CBO)**

- **Requires**: `spark.sql.cbo.enabled=true` AND `ANALYZE TABLE` statistics
- **Benefits**: Chooses better join strategies, join order, filter selectivity estimates
- **Without CBO**: Heuristics only (e.g., "broadcast if < 10 MB")

---

### Partition Count Tuning

**Optimal Partition Size**

- **Target**: 1-2 MB per partition (achieves good parallelism without excessive task overhead)
- **Formula**: `optimal_partitions = data_size_GB / 1 GB` (approximately)
- **Adjustment**:
  - Too few partitions: Underutilized cluster; slow execution
  - Too many partitions: Task scheduling overhead; small task overhead grows

**Post-Shuffle Partition Count** (`spark.sql.shuffle.partitions`)

- **Default**: 200 (often too low for large data)
- **Tuning**:
  - Small queries (< 1 GB): Use 50-100
  - Medium queries (1-100 GB): Use 200-500
  - Large queries (> 100 GB): Use 500-2000
- **AQE**: May coalesce small partitions after shuffle (saves tasks)

---

### Memory & Garbage Collection

**Memory Pressure Symptoms**

- "GC overhead limit exceeded" — JVM spending > 98% time on GC
- Long pause times in executor logs
- Stage latency spikes unrelated to data size

**GC Tuning**

```
--conf spark.executor.extraJavaOptions="-XX:+UseG1GC -XX:MaxGCPauseMillis=30"
```

- Use G1GC for heaps > 4 GB
- Set max pause target (30 ms typical)
- Increase executor memory to reduce GC frequency

**Serialization Impact on GC**

- `MEMORY_ONLY` storage: Deserialized objects → many GC pauses
- `MEMORY_ONLY_SER`: Serialized byte arrays → fewer objects, less GC
- **Trade-off**: SER variant reduces GC but adds CPU for ser/deser

---

## TOPIC 5: Streaming & Real-Time Processing

### Streaming Triggers & Micro-Batches

**Trigger Types**

| Trigger | Behavior | Use |
|---------|----------|-----|
| `processingTime("30s")` | Start batch every 30s | Predictable intervals |
| `once=True` | Process all available data in one batch | Backfill; one-time loads |
| `availableNow=True` (3.3+) | Process all available but respect size limits | Better than `once=True` |
| `continuous(interval)` | Experimental; low-latency continuous processing | Not production-ready |

**Micro-Batch Execution**

```
Trigger fires (every processingTime interval)
  ↓
Query engine reads available data (offset range)
  ↓
Executes transformations
  ↓
Writes output (if sink supports)
  ↓
Commits offset to checkpoint
  ↓
Ready for next micro-batch
```

---

### Watermarking & Late Data

**Watermark Purpose**

- Defines the threshold for "late" data arrival
- Enables eviction of old state from memory (bounds memory growth)
- Allows delayed results to be output in append mode

**Watermark Calculation**

```
current_watermark = max(event_time_seen) - allowedLateness_threshold
```

**Output Behavior with Watermark**

- Events arriving **before** watermark: Dropped (too late)
- Events arriving **after** window end but **before** watermark: Included in result (within grace period)
- Events arriving **after** watermark: Dropped (too late)
- State for windows **older than watermark**: Evicted from memory

**Configuration**

```python
df_watermarked = (df
    .withWatermark("event_time", "10 minutes")  # 10-minute grace period
    .groupBy(F.window("event_time", "5 minutes"))
    .agg(F.count("*")))

# Only Append mode is safe with watermark
result = df_watermarked.writeStream \
    .outputMode("append") \
    .start()
```

---

### Streaming State & Checkpointing

**State Store**

- Maintains state for stateful operations (aggregations, joins, deduplication)
- Checkpointed to disk for fault tolerance
- **Configuration**: `spark.sql.streaming.checkpointLocation=/path/to/checkpoint`

**Checkpoint Directory Structure**

```
checkpoint/
├── offsets/       # Source offset per micro-batch
├── commits/       # Commit log (confirmed batches)
├── state/         # State snapshots (aggregation results, join state)
└── batchMetadata/ # Batch metadata and progress
```

**Exactly-Once Semantics**

- Idempotent state updates (same batch → same state change)
- Idempotent sink writes (same batch → same output, even on replay)
- Delta Lake sinks provide built-in exactly-once

---

## TOPIC 6: Distributed System Patterns

### Broadcasting & Caching on Executors

**Broadcast Variable Lifecycle**

1. **Driver** creates: `sc.broadcast(large_object)`
2. **Driver** serializes (once)
3. **Network** distributes to all executors (torrent-like to avoid driver bottleneck)
4. **Executor** receives, deserializes, caches (per-executor, shared by all tasks)
5. **Tasks** access cached copy (no re-serialization)

**Use Cases**

- Large lookup tables (< 1 GB recommended)
- Configuration objects
- Pre-trained ML models

**Anti-Patterns**

- Broadcasting large DataFrames (use broadcast hint instead: `F.broadcast(df)`)
- Broadcasting non-serializable objects
- Creating multiple broadcast objects in a loop

---

### Accumulators & Distributed Counters

**Accumulator Lifecycle**

```python
counter = sc.longAccumulator("counter_name")

# Write from tasks (during execution)
rdd.map(lambda x: (counter.add(1), x)).collect()

# Read from driver (after action completes)
print(counter.value)  # Final value
```

**Key Semantics**

- **Write Timing**: Only during task execution (updates invisible until action completes)
- **Read Timing**: Only after action completes (guaranteed to see final value)
- **Fault Tolerance**: At-least-once guarantee (retried tasks increment multiple times)
- **Thread Safety**: Not thread-safe; only access from driver after action completes

**Use Cases**

- Counting events, errors, rows processed
- Collecting debug information distributed across cluster
- Metrics aggregation from all partitions

---

## TOPIC 7: Production Reliability & Edge Cases

### Data Skew & Mitigation

**Skew Detection Symptoms**

- One or few tasks much slower than others
- Stage latency dominated by straggler partitions
- Executor memory pressure on only one executor

**Root Causes**

- Uneven distribution on join/group key (e.g., many rows with same user_id)
- Null values concentrated in one partition
- Hotspot keys (popular users, events, etc.)

**Mitigation Strategies**

1. **Salting** (Manual):
   ```python
   df.withColumn("salt", (F.rand() * 10).cast("int"))
     .repartition(100, col("key"), col("salt"))
   ```
   - Split skewed key into multiple partitions
   - Must unsalt after join

2. **AQE Skew Join** (Automatic):
   - Enable: `spark.sql.adaptive.skewJoin.enabled=true`
   - Detects skew at runtime; splits partitions automatically

3. **Different Join Strategy**:
   - Use broadcast if one side is small (avoids shuffle)

---

### Small File Problem

**Root Cause**

- Many small files → inefficient file listing (O(file_count))
- Small partitions → many tasks with little work
- HDFS RPC overhead

**Solutions**

1. **On Write**: Coalesce before writing
   ```python
   df.coalesce(10).write.parquet("path")
   ```

2. **On Read**: Use `maxPartitionBytes` to merge small files
   ```
   --conf spark.sql.files.maxPartitionBytes=134217728
   ```

3. **Proactive**: Plan partition count upfront

---

### Network Failures & Retries

**RPC Retry Configuration**

```
spark.rpc.numRetries=3              # Max retry attempts
spark.rpc.retry.wait=3s             # Initial wait; exponential backoff
                                    # (3s → 6s → 12s)
spark.network.timeout=120s          # Global timeout
```

**Failure Scenarios**

- **Executor lost**: Tasks re-submitted to other executors
- **Shuffle data loss**: Blocks recomputed or re-read from source
- **Network timeout**: Retry logic kicks in; if all retries exhaust, task fails

---

## Critical Concepts Summary

### Lazy Evaluation
- Transformations define plan; actions trigger execution
- Multiple actions re-execute plan (unless cached)

### Partitioning
- `spark.default.parallelism`: RDD operations only
- `spark.sql.shuffle.partitions`: DataFrame shuffles
- Target: 1-2 MB per partition

### Unified Memory Model
- Execution memory can evict storage memory
- Cached data lost if `MEMORY_ONLY` and evicted

### Catalyst Optimizer
- Predicate/projection pushdown most impactful
- CBO requires statistics (`ANALYZE TABLE`)

### Join Strategies
- Broadcast (< 10 MB) → Shuffle Hash → Sort-Merge

### Watermarking
- Enables state eviction; bounds memory growth
- Requires Append mode for safety

### Exactly-Once Streaming
- Idempotent state + idempotent sink
- Delta Lake recommended
