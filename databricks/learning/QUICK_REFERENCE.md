# Databricks Spark Certification — Quick Reference & Concept Index

**A condensed reference for rapid review and last-minute prep**

---

## Part 1: Key Definitions & Formulas

### Spark Architecture Fundamentals

| Concept | Definition | Example |
|---------|-----------|---------|
| **Action** | Operation that triggers a Spark job (returns value or writes data) | `collect()`, `count()`, `show()`, `write.parquet()` |
| **Transformation** | Lazy operation that returns a new DataFrame; doesn't execute | `filter()`, `select()`, `join()`, `groupBy()` |
| **Narrow** | Transformation where each output partition depends on ≤1 input partition; no shuffle | `filter()`, `select()`, `withColumn()` |
| **Wide** | Transformation requiring shuffle (all-to-all data exchange); creates stage boundary | `groupBy()`, `distinct()`, `orderBy()`, `join()` |
| **DAG** | Directed Acyclic Graph; logical execution plan (sequence of transformations) | Spark computes and optimizes the DAG before execution |
| **Stage** | Group of tasks that can execute in parallel; split at shuffle boundaries | Shuffle → new stage |
| **Task** | Unit of work; one per partition in a stage | 100 partitions → 100 tasks (execute in parallel on available cores) |
| **Shuffle** | All-to-all data redistribution across network (expensive) | Triggered by `groupBy()`, `orderBy()`, `join()` |
| **Lineage** | Record of the sequence of transformations; used to recompute lost partitions | Lost partition recomputed without re-reading source |
| **Spark Session** | Unified entry point for DataFrame/SQL/Streaming operations (Spark 2.0+) | `spark.read.parquet()`, `spark.sql()`, `spark.readStream` |
| **Driver** | Process that runs SparkContext; converts user code → DAG; schedules tasks | Orchestrator; usually runs on single machine |
| **Executor** | Process that runs tasks on partitions; stores cached data | Distributed across cluster nodes |

### Performance Concepts

| Concept | Definition | Impact |
|---------|-----------|--------|
| **Lazy Evaluation** | Transformations don't execute until an action is called | Allows Catalyst to optimize the full plan before execution |
| **Pipelining** | Multiple narrow transformations execute in single pass (no intermediate storage) | Reduces memory pressure and I/O |
| **Predicate Pushdown** | Filters moved closer to data source for early elimination | Reduces data scanned; only works on source columns |
| **Broadcast Join** | Small table replicated to all executors; larger table scanned once | Avoids expensive shuffle; requires size < threshold |
| **Skew** | Uneven data distribution; some partitions much larger than others | Some tasks 10–100× slower than median; AQE can mitigate |
| **Fault Tolerance** | Ability to recover from task/executor failures | Spark recomputes lost partitions from lineage; no full re-scan |

### SQL & Catalyst

| Term | Meaning |
|------|---------|
| **Catalyst** | Spark's query optimizer; parses SQL → logical plan → optimized logical plan → physical plan |
| **Cost-Based Optimizer (CBO)** | Uses table statistics to choose optimal join order and strategies; requires `ANALYZE TABLE` |
| **Adaptive Query Execution (AQE)** | Runtime optimizer that coalesces small partitions, switches join strategies, handles skew |
| **Predicate** | Condition in a WHERE/filter clause |
| **Window Function** | Per-partition aggregation without reducing row count; includes `rank()`, `row_number()`, `lag()`, `lead()`, etc. |

---

## Part 2: Configuration & Tuning Reference

### Critical Spark Configurations

```python
# Shuffle
spark.conf.set('spark.sql.shuffle.partitions', 50)           # Default 200; tune based on data size
spark.conf.set('spark.sql.autoBroadcastJoinThreshold', '10MB') # Tables < 10MB auto-broadcast

# Adaptive Query Execution
spark.conf.set('spark.sql.adaptive.enabled', True)           # Enable AQE (default in 3.2+)
spark.conf.set('spark.sql.adaptive.coalescePartitions.enabled', True)
spark.conf.set('spark.sql.adaptive.skewJoin.enabled', True)

# Memory
spark.conf.set('spark.executor.memory', '4g')                # Per-executor heap
spark.conf.set('spark.driver.memory', '2g')                  # Driver heap

# Storage
spark.conf.set('spark.memory.fraction', 0.6)                 # 60% for storage, 40% for execution
```

### When to Tune What

| Symptom | Root Cause | Fix |
|---------|-----------|-----|
| Many tasks completing in milliseconds | Too many partitions after shuffle | Reduce `spark.sql.shuffle.partitions` or use `coalesce()` |
| One task 10–100× slower than others | Data skew on join/group column | Enable AQE skew handling; consider salting |
| Executor OOM errors | Not enough executor memory | Increase `spark.executor.memory`; check for memory leaks |
| Driver OOM during `collect()` | Collected dataset > driver heap | Increase `spark.driver.memory` OR reduce data before `collect()` |
| Filter not pushed to file reader | Filter on derived column | Reorder: push source-column filters first |

---

## Part 3: DataFrame API Cheat Sheet

### Selection & Projection

```python
df.select('col1', 'col2')                          # Select columns by name
df.select(col('col1'), col('col2') * 2)           # Column expressions
df.selectExpr('col1', 'col2 * 1.1 AS col2_scaled') # SQL expressions
df['col1']                                         # Subscript (returns Series)
```

### Filtering

```python
df.filter(col('age') > 25)
df.where(col('status') == 'active')              # Alias for filter
df.filter((col('age') > 25) & (col('salary') > 50000))  # Compound conditions
```

### NULL Handling

```python
df.isNull()                                       # Detect NULLs
df.isNotNull()                                    # Detect non-NULLs
df.fillna(0)                                      # Fill with scalar
df.fillna({'col1': 0, 'col2': 'Unknown'})        # Column-specific fills
df.dropna()                                       # Drop rows with any NULL
df.dropna(thresh=2)                               # Keep rows with ≥2 non-null values
```

### Adding/Modifying Columns

```python
df.withColumn('bonus', col('salary') * 0.1)      # Add or replace
df.withColumnRenamed('old_name', 'new_name')     # Rename
df.drop('col1')                                   # Remove columns
```

### Joins

```python
df_a.join(df_b, on='id', how='inner')            # Equi-join
df_a.join(df_b, (df_a.id == df_b.emp_id), how='left')  # Complex condition
df_a.join(broadcast(small_df), on='id')          # Broadcast small table
df_a.hint('broadcast').join(small_df, on='id')   # Hint for broadcast
```

### Set Operations

```python
df_a.union(df_b)                                  # Union by position (not name!)
df_a.unionByName(df_b)                            # Union by name
df_a.intersect(df_b)                              # Rows in both
df_a.subtract(df_b)                               # Rows in df_a, not in df_b
```

### Grouping & Aggregation

```python
df.groupBy('dept').count()                        # Simple count
df.groupBy('dept').agg(
  F.sum('salary'),
  F.avg('salary'),
  F.countDistinct('id')
)
df.groupBy('year').rollup('year', 'quarter').sum('amount')  # Hierarchical totals
df.groupBy('year').cube('year', 'quarter').sum('amount')    # All combinations
```

### Repartition & Coalesce

```python
df.repartition(200)                               # Full shuffle; increase/decrease partitions
df.repartition(10, 'customer_id')                 # Hash partition by column
df.coalesce(10)                                   # Merge partitions; avoid shuffle if decreasing
```

### Reading & Writing

```python
spark.read.parquet('/path')
spark.read.csv('/path', header=True)
spark.read.json('/path')

df.write.mode('overwrite').parquet('/output')     # Replace if exists
df.write.mode('append').parquet('/output')        # Add to existing
df.write.partitionBy('year', 'month').parquet('/output')  # Hive partitioning
```

---

## Part 4: Structured Streaming Quick Reference

### Core Concepts

```python
# Check if streaming
df.isStreaming  # True for streaming; False for batch

# Read from Kafka
spark.readStream \
  .format('kafka') \
  .option('kafka.bootstrap.servers', 'localhost:9092') \
  .option('subscribe', 'topic1') \
  .load()

# Read from files (requires schema)
schema = 'id INT, name STRING'
spark.readStream.schema(schema).csv('/data/stream')
```

### Writing Streaming DataFrames

```python
df.writeStream \
  .option('checkpointLocation', '/checkpoints/my_query') \
  .outputMode('append') \          # append, update, or complete
  .trigger(processingTime='1 second') \  # or once=True, availableNow=True
  .format('parquet') \
  .start('/output')
```

### Watermarks for Late Data

```python
df.withWatermark('event_time', '10 minutes') \
  .groupBy(F.window('event_time', '5 minutes')) \
  .count()

# Watermark = max_event_time - 10 minutes
# Windows older than watermark are finalized and state is cleaned up
# Late events within 10 minutes are still processed
```

### Output Mode Selection

| Mode | When to Use | Example |
|------|-------------|---------|
| `append` | Stateless queries; windowed agg with watermark | Filter, map, windowed group by |
| `update` | Stateful agg without watermark | Non-windowed group by; overwrites state |
| `complete` | Full result table (small data only) | Aggregation on small dataset |

---

## Part 5: Troubleshooting & Debugging Shortcuts

### Spark UI Access

```
Local Mode:        http://localhost:4040 (active app)
History Server:    http://<server>:18080
Cluster Mode:      http://<driver-host>:4040
```

### Explain Plans

```python
df.explain()              # Physical plan (short)
df.explain('extended')    # All 4 stages: unresolved → analyzed → optimized → physical
df.explain('cost')        # With row/byte estimates
df.explain('codegen')     # Generated bytecode
```

### Reading Physical Plans

Key indicators:
- `Exchange` = shuffle (expensive)
- `FileScan` with `PushedFilters: []` = filter NOT pushed down (inefficient)
- `*(1)` and `*(2)` = different WholeStageCodegen units (stage boundaries)
- `SortMergeJoin`, `BroadcastHashJoin`, `NestedLoopJoin` = join strategy
- Estimated rows/bytes help identify bottlenecks

### Identifying Issues in Spark UI

| Issue | Look For | Action |
|-------|----------|--------|
| Tiny tasks (ms duration) | Many tasks in single stage | Reduce `spark.sql.shuffle.partitions` |
| Data skew | Max task duration >> median | Enable AQE skew handling |
| Predicate not pushed | EXPLAIN: `PushedFilters: []` | Move filters on source columns earlier |
| Executor OOM | Executor logs show OOM error | Increase `spark.executor.memory` |
| Driver OOM during `collect()` | Driver logs show OOM | Increase `spark.driver.memory` or reduce data |

---

## Part 6: Type Reference

### Common Data Types

```python
from pyspark.sql.types import *

# Numeric
ByteType()       # 8-bit
ShortType()      # 16-bit
IntegerType()    # 32-bit
LongType()       # 64-bit (default for integers)
FloatType()      # 32-bit floating point
DoubleType()     # 64-bit floating point
DecimalType(10, 2)  # 10 total digits, 2 after decimal

# Text & Binary
StringType()     # UTF-8 string
BinaryType()     # Raw bytes

# Temporal
DateType()       # Date (no time)
TimestampType()  # Timestamp (with time)

# Complex
ArrayType(IntegerType())    # Array of integers
MapType(StringType(), IntegerType())  # Map<String, Int>
StructType([
  StructField('id', IntegerType(), nullable=False),
  StructField('name', StringType(), nullable=True)
])
```

### Accessing Nested Data

```python
# Struct
col('address.city')                 # Dot notation
col('address').getField('city')     # getField()

# Array
col('items')[0]                     # First element (bracket notation)
col('items').getItem(0)             # First element (getItem())
F.explode(col('items'))             # Explode array to rows

# Map
col('metadata')['key']              # Bracket notation
col('metadata').getItem('key')      # getItem()
```

---

## Part 7: Exam Question Patterns

### Identify These Patterns Quickly

**Pattern 1: Narrow vs Wide**
- If options mention `groupBy`, `distinct`, `orderBy`, `join()` → likely WIDE (shuffle)
- If options mention `filter`, `select`, `withColumn()` → likely NARROW (no shuffle)

**Pattern 2: Action vs Transformation**
- If options mention `collect()`, `count()`, `show()`, `write` → likely ACTION
- If options return DataFrame → likely TRANSFORMATION

**Pattern 3: NULL vs NaN**
- `fillna()` fills NULL; doesn't fill NaN
- Use `F.isnan()` to detect floating-point NaN
- `count('*')` counts NULLs; `count(col)` skips NULLs

**Pattern 4: Union by Position**
- `union()` aligns columns by position, NOT name
- Use `unionByName()` for name-based alignment

**Pattern 5: Lazy Execution**
- Transformations return DataFrame but don't execute
- Only actions trigger execution
- This enables Catalyst optimization

**Pattern 6: Config Tuning**
- Too many tiny tasks? Reduce shuffle partitions
- Executor OOM? Increase executor memory
- Driver OOM on `collect()`? Increase driver memory OR reduce data
- Broadcast not happening? Lower `autoBroadcastJoinThreshold`

**Pattern 7: Performance**
- Skew (uneven partition sizes) → AQE skew handling or salting
- Predicate not pushed → EXPLAIN shows `PushedFilters: []`
- Many partitions after shuffle → use `coalesce()`

---

## Part 8: Last-Minute Memory Tips

### The "Big 7" of Spark Optimization

1. **Lazy Evaluation**: Transformations don't execute until action
2. **Catalyst**: Optimizer that rewrites logical plans
3. **Predicate Pushdown**: Filters moved to source; only works on source columns
4. **Broadcast Join**: Small table replicated; avoids shuffle if < 10 MB (by default)
5. **Partitioning**: 200 default shuffle partitions often wrong; tune to data size
6. **Adaptive Query Execution**: Runtime optimizer; fixes coalescing, join strategy, skew
7. **Lineage & Fault Tolerance**: Lost partitions recomputed from DAG; no full re-scan

### The "Big 3" of Streaming

1. **Checkpoints**: Store offsets and state for fault tolerance
2. **Watermarks**: Define lateness threshold; enable append mode with windowed aggs
3. **Output Modes**: `append` (stateless), `update`/`complete` (stateful)

### The "Big 2" of Troubleshooting

1. **Spark UI**: Always check physical plan EXPLAIN and task durations
2. **Scaling**: Tiny tasks? Reduce partitions. Big tasks? Increase partitions.

---

## Part 9: Exam Strategy Reminders

✅ **DO:**
- Read each question carefully (watch for subtle differences in wording)
- Use process of elimination (rule out clearly wrong answers)
- Understand the "why" for each answer (not just memorize)
- Flag hard questions and come back if time permits
- Review EXPLAIN output before optimizing

❌ **DON'T:**
- Second-guess your preparation
- Spend too long on a single question
- Assume "always" or "never" are correct (they usually aren't)
- Forget that unions align by position, not name
- Call `collect()` on large DataFrames
- Use `repartition()` when `coalesce()` would work better
- Forget that `count(*)` includes NULLs

---

**Final Tip**: Trust your preparation and stay calm. You've studied the concepts thoroughly. The exam is testing your understanding, not trick questions. Good luck! 🚀
