# Databricks Spark Certification — Iteration 2 Quick Reference

**Condensed lookup guide for rapid review and exam prep**

**Last Updated**: May 17, 2026

---

## Part 1: Key Definitions & Formulas (Iteration 2 Focus)

### Spark Execution & Deployment

| Concept | Definition | Key Detail |
|---------|-----------|-----------|
| **local[*]** | Single JVM using all available logical CPU cores | Development/testing only |
| **Client Mode** | Driver on submitting machine | Submit machine crash = job failure |
| **Cluster Mode** | Driver on worker node inside cluster | Job survives submit machine failure |
| **Standalone Port** | 7077 (master), 8080 (web UI), 18080 (history) | Classic Apache Spark cluster manager |
| **Executor Memory** | `spark.executor.memory` (heap) + `spark.executor.memoryOverhead` (off-heap) | Off-heap: OS overhead, Python workers, native libs |
| **Spark Memory** | `heap × spark.memory.fraction` (default 60%) | Storage + Execution regions |
| **Accumulator** | Write-only distributed variable; only Driver reads final value | Tasks see initial value if they read |
| **Broadcast Variable** | Serialized once, cached on each Executor; accessed via `.value` | Immutable; re-sent on Executor failure |

### Spark Architecture Concepts

| Concept | Definition |
|---------|-----------|
| **Lazy Evaluation** | Transformations don't execute until an action is called |
| **Narrow Transform** | Each output partition depends on ≤1 input; no shuffle (filter, select, withColumn) |
| **Wide Transform** | All-to-all redistribution; full shuffle (groupBy, orderBy, join, distinct) |
| **DAG** | Directed Acyclic Graph; logical execution plan optimized by Catalyst |
| **Stage** | Group of tasks split at shuffle boundaries; one stage per wide transformation |
| **Task** | Unit of work; one per partition in a stage; executes in parallel |
| **Speculative Execution** | Duplicate stragglers on other Executors; first finishes wins |
| **Lineage** | Sequence of transformations; used to recompute lost partitions |

### Storage Levels

| Level | Heap? | Disk Spill? | Serialized? | Replication | When? |
|-------|-------|---|---|---|---|
| `MEMORY_ONLY` | ✅ | ❌ (dropped) | ❌ | ❌ | Recompute if lost; fastest |
| `MEMORY_AND_DISK` | ✅ | ✅ | ❌ | ❌ | DataFrame default; balanced |
| `MEMORY_ONLY_SER` | ✅ | ❌ | ✅ | ❌ | Saves memory; deserialization overhead |
| `MEMORY_ONLY_2` | ✅ | ❌ | ❌ | ✅ | Fault tolerance via replication |

---

## Part 2: Spark SQL & Catalyst

### Catalyst Optimization Pipeline

```
SQL String
  ↓ Parse
Unresolved Logical Plan
  ↓ Analyze (resolve columns, types)
Analyzed Logical Plan
  ↓ Optimize (Predicate Pushdown, Projection Pushdown, etc.)
Optimized Logical Plan
  ↓ Physical Plan
Executable Plan
```

### Predicate Pushdown & Projection Pushdown

**Predicate Pushdown**:
- ✅ Works on **source columns** (columns read directly from file)
- ❌ Doesn't work on **derived columns** (created by withColumn, expressions)
- Location: Moved as early as possible, ideally to FileScan

**Projection Pushdown**:
- Select only required columns (not all)
- Reduces I/O by not reading unnecessary columns from file

### Window Function Edge Cases

| Function | Edge Case | Result |
|----------|-----------|--------|
| `lead(col, 1)` | Last row in partition | `null` |
| `lag(col, 1)` | First row in partition | `null` |
| `rank()` | Ties | Skips after ties (1, 2, 2, 4) |
| `dense_rank()` | Ties | No skips (1, 2, 2, 3) |
| `percent_rank()` | Min/Max value | Range: [0, 1] |
| `cume_dist()` | Min/Max value | Range: (0, 1] |
| `ntile(3)` with 10 rows | Uneven split | 4, 3, 3 (extra to first buckets) |

---

## Part 3: DataFrame API Cheat Sheet (Iteration 2 Additions)

### Joins: Handling Ambiguous Columns

```python
# After join, both DataFrames have 'id' column
result = df_orders.join(df_customers, df_orders.id == df_customers.id)

# ❌ ERROR: ambiguous
result.select('id')

# ✅ Explicit reference
result.select(df_orders.id, df_customers.id)
```

### Set Operations: Position vs Name

```python
# ❌ WRONG: Aligns by position!
df_a.union(df_b)  # Matches columns by position, NOT name

# ✅ CORRECT: Aligns by name
df_a.unionByName(df_b)
```

### Explode Variants

```python
F.explode(col('items'))        # Drops null/empty arrays
F.explode_outer(col('items'))  # Preserves null/empty as single null row
```

### Common Functions

| Function | Behavior |
|----------|----------|
| `F.coalesce(col1, col2, col3)` | First non-null value |
| `F.array_contains(col, value)` | Boolean: does array contain value? |
| `F.split(col, delim)` | String → ArrayType(StringType) |
| `F.concat_ws(sep, col)` | Join array elements; skips nulls |
| `F.to_json(col)` | Struct/map → JSON string |
| `F.datediff(end, start)` | Days between dates (IntegerType) |
| `F.date_format(col, pattern)` | Date → formatted string |
| `F.monotonically_increasing_id()` | Unique, monotonic, but gapped |

### toDF() Rename All Columns

```python
df.toDF('col1', 'col2', 'col3')  # Rename by position
```

### Write Modes

| Mode | Preserves Existing? |
|------|---|
| `'overwrite'` | ❌ No |
| `'append'` | ✅ Yes |
| `'ignore'` | ✅ Yes (writes nothing) |
| `'error'` | ✅ Yes (raises exception) |

### Schema Merging on Read

```python
spark.read.option('mergeSchema', True).parquet('/output')
# Merges schemas from all files; missing columns = null
```

### Partition Pruning

```python
df = spark.read.parquet('/data/events')  # Written with .partitionBy('country')
df.filter(col('country') == 'US')       # Reads ONLY country=US/ directory
```

---

## Part 4: Streaming Quick Reference (Iteration 2)

### Output Mode Selection Guide

| Query Type | Output Mode | Checkpoint Required? |
|-----------|---|---|
| Windowed agg + watermark | `'append'` | ✅ Yes |
| Non-windowed groupBy | `'update'` | ✅ Yes |
| Small stateful agg | `'complete'` | ✅ Yes |
| Stateless (filter, select) | `'append'` | ❌ No |

### Watermark Formula

```
Watermark = max_event_time - allowed_lateness

Events with event_time < Watermark are considered LATE and DROPPED
```

### Triggers

| Trigger | Behavior |
|---------|----------|
| `processingTime='1 second'` | Micro-batch every 1 second |
| `once=True` | Single micro-batch; all data at once; stop |
| `availableNow=True` | Multiple micro-batches; process all available; stop |
| `continuous='1 second'` | Experimental; true streaming (not micro-batch) |

### Sources & Fault Tolerance

| Source | Fault Tolerant? | Supports Replay? |
|--------|---|---|
| Kafka/Event Hubs | ✅ Yes | ✅ Yes |
| File | ✅ Yes | ✅ Yes |
| Rate | ✅ Yes | ✅ Yes (regenerates) |
| Socket | ❌ No | ❌ No |
| Delta Lake | ✅ Yes | ✅ Yes (any version) |

### StreamingQuery Controls

```python
query = df.writeStream.start()
query.status           # Current status
query.lastProgress     # Metrics from last batch
query.awaitTermination()  # Block until query stops
query.stop()           # Stop the query
```

---

## Part 5: Troubleshooting & Tuning Shortcuts (Iteration 2)

### Problem → Root Cause → Fix

| Problem | Root Cause | Fix |
|---------|-----------|-----|
| Many tasks in ms | Too many partitions | Reduce `spark.sql.shuffle.partitions` or `coalesce()` |
| One task 10–100× slower | Data skew | Enable AQE skew; consider salting |
| GC overhead OOM | Too much live data per Executor | Reduce cores, increase memory, increase shuffle partitions |
| Executor OOM | Not enough Executor memory | Increase `spark.executor.memory` |
| Driver OOM on `collect()` | Collected data > Driver heap | Increase `spark.driver.memory` OR reduce data before collect |
| Filter not pushed | Predicate on derived column | Move filter to source columns earlier |
| Tiny partition after shuffle | Auto-broadcast didn't trigger | Lower `spark.sql.autoBroadcastJoinThreshold` |

### Critical Configurations

```python
spark.conf.set('spark.sql.shuffle.partitions', 50)           # Tune by data size
spark.conf.set('spark.sql.autoBroadcastJoinThreshold', '10MB') # Auto-broadcast < 10MB
spark.conf.set('spark.executor.cores', 4)                    # 4–5 optimal; avoid 20+
spark.conf.set('spark.executor.memory', '4g')                # Heap memory
spark.conf.set('spark.executor.memoryOverhead', '512m')      # Off-heap (Python, ML libs)
spark.conf.set('spark.memory.fraction', 0.6)                 # 60% Spark Memory; 40% User
spark.conf.set('spark.sql.adaptive.enabled', True)           # Enable AQE (Spark 3.2+)
spark.conf.set('spark.speculation', True)                    # Straggler detection
```

### EXPLAIN Output Indicators

| Pattern | Meaning |
|---------|---------|
| `Exchange` | Shuffle (expensive) |
| `PushedFilters: []` | Filter NOT pushed (inefficient) |
| `BroadcastHashJoin` | Broadcast join (fast) |
| `SortMergeJoin` | Shuffle join (slower) |
| `*(1) *(2)` | Different WholeStageCodegen units (stage boundary) |

---

## Part 6: Spark Connect (Iteration 2 Focus)

### Architecture Comparison

| Aspect | Classic Spark | Spark Connect |
|--------|---|---|
| **Client-Server** | Py4J socket (JVM must be local) | gRPC over HTTP/2 |
| **Driver Location** | Embedded in app | Separate on cluster |
| **App Crash Impact** | Driver crashes; job fails | Job continues; client can reconnect |
| **JVM Required** | Yes (on client) | No (client-side) |
| **Supported Languages** | Python, Scala, R, SQL | Any language with gRPC client |
| **Default Port** | N/A | 15002 |

### Spark Connect URL Scheme

```python
spark = SparkSession.builder.remote('sc://hostname:15002').getOrCreate()
```

### Capabilities

✅ **Supported**:
- DataFrame API
- SQL API
- Structured Streaming
- Caching
- Catalog operations

❌ **Not Supported**:
- RDD API
- Broadcast variables (limited)
- Accumulators (limited)

### Version Compatibility

- Supports version negotiation
- 3.4 client ↔ 3.5 server: Works fine
- Teams can upgrade independently

---

## Part 7: Pandas API on Spark (Iteration 2)

### Import Statements

```python
import pyspark.pandas as ps  # ✅ Recommended (Spark 3.2+)
import databricks.koalas as ks  # ⚠️ Deprecated but works
```

### Conversion Cheat Sheet

```python
pdf = pandas.DataFrame(...)
psdf = ps.from_pandas(pdf)    # pandas → pyspark.pandas
psdf = ps.from_spark(sdf)     # PySpark → pyspark.pandas

sdf = psdf.to_spark()         # pyspark.pandas → PySpark (distributed)
pdf = psdf.to_pandas()        # pyspark.pandas → pandas (collects to Driver!)
```

### Index Types

| Type | Behavior | Performance | Use Case |
|------|----------|---|---|
| `'distributed-sequence'` | Unique; partition ID + offset; gapped | Fast (no shuffle) | Default; most cases |
| `'sequence'` | Strictly sequential (0, 1, 2, 3, ...) | Slow (global sort) | Only if strict sequencing needed |

### ⚠️ Memory Warnings

- `to_pandas()` **collects all data to Driver** → OOM on large data
- Use `to_spark()` to stay distributed
- Only `to_pandas()` when result is small

---

## Part 8: Exam Question Patterns (Iteration 2)

### Pattern Recognition Tricks

**Pattern 1: Deploy Mode Failures**
- Client mode + submit machine crashes = job fails
- Cluster mode + submit machine crashes = job continues
- Use cluster mode for production jobs

**Pattern 2: Configuration Tuning**
- Too many tiny tasks → reduce shuffle partitions or coalesce
- Executor OOM → increase executor memory OR increase shuffle partitions
- Broadcast not happening → lower broadcast threshold

**Pattern 3: Accumulator Reads**
- Tasks reading accumulators see initial value (e.g., 0)
- Only Driver sees final value after action

**Pattern 4: Join Ambiguity**
- After join, column exists twice if both DataFrames have same name
- Must use qualified reference (df1.col) to disambiguate

**Pattern 5: Union Position vs Name**
- `union()` aligns by position (column order matters!)
- `unionByName()` aligns by name (safer)

**Pattern 6: Watermark & Late Data**
- Watermark = max_event_time − 10 minutes
- Events earlier than watermark are dropped
- Essential for append mode with windowed aggs

**Pattern 7: Storage Level Tradeoffs**
- `MEMORY_ONLY` fastest but drops partitions if full
- `MEMORY_AND_DISK` balanced; DataFrame default
- `MEMORY_ONLY_SER` saves space; deserialization overhead

---

## Part 9: Last-Minute Memory Tips

### The "Big 5" of Spark Architecture (Iteration 2)

1. **Deploy Mode**: Client (single point of failure) vs Cluster (resilient)
2. **Lazy Evaluation**: Only actions execute; Catalyst optimizes full DAG
3. **Narrow vs Wide**: Narrow (no shuffle) vs Wide (shuffle → new stage)
4. **Catalyst Optimization**: Predicate pushdown (source columns), projection pushdown
5. **Lineage & Fault Tolerance**: Lost partitions recomputed from DAG

### The "Big 3" of Streaming (Iteration 2)

1. **Watermarks**: Define lateness threshold; enable append mode with windowed aggs
2. **Checkpoints**: Store offsets and state; mandatory for exactly-once
3. **Output Modes**: append (stateless/windowed), update (stateful), complete (full result)

### The "Big 2" of Troubleshooting

1. **Spark UI**: Always check physical plan and task durations
2. **Scaling**: Tiny tasks? Reduce partitions. Big tasks? Increase partitions.

### The "Big 1" of Pandas API

- `to_pandas()` collects to Driver → OOM risk; only for small results

---

## Part 10: Exam Strategy Reminders

### DO:
- ✅ Read each question carefully (spot subtle wording differences)
- ✅ Process of elimination (rule out clearly wrong answers)
- ✅ Understand the "why" for each answer
- ✅ Flag hard questions; come back if time permits
- ✅ Review EXPLAIN output before optimizing
- ✅ Know when to use cluster vs client mode
- ✅ Understand watermark formula exactly

### DON'T:
- ❌ Second-guess well-known concepts
- ❌ Spend too long on one question
- ❌ Assume "always" or "never" are correct
- ❌ Forget that `union()` aligns by position, not name
- ❌ Call `collect()` on large DataFrames
- ❌ Use `repartition()` when `coalesce()` would work better
- ❌ Ignore client mode failure risks in production
- ❌ Forget Watermark = max_event_time − allowed_lateness

---

**Final Tip**: Trust your preparation. You've covered all 7 topics across 100 questions (Iteration 2). The exam is testing your understanding, not trick questions. Take a deep breath and do your best. Good luck! 🚀
