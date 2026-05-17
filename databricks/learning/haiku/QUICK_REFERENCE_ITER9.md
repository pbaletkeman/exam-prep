# Databricks Certified Associate Developer for Apache Spark — Quick Reference (Iteration 9)

**Edition**: Iteration 9 (100 Questions)
**Last Updated**: 2026-05-17
**Format**: Fast lookup tables, decision trees, memory anchors

---

## Core API Quick Reference

| Concept | Definition | Key Detail |
|---------|-----------|-----------|
| **SparkSession** | Unified entry point (Spark 2.0+) | Wraps SparkContext; use `spark.sparkContext` for RDD access |
| **SparkContext** | Low-level cluster communication | Accessed via `spark.sparkContext`; never create manually |
| **DataFrame** | Distributed table with schema | Optimized by Catalyst; primary API for analytics |
| **RDD** | Distributed collection (untyped) | Use when DataFrame insufficient; manual control |
| **Dataset** (Scala/Java) | Strongly-typed distributed collection | Type safety + Catalyst optimization |

---

## Parallelism Configuration Quick Reference

| Config | Default | Scope | Impact |
|--------|---------|-------|--------|
| `spark.default.parallelism` | Core count × 8 (approx) | RDD transformations only | Partition count for `reduceByKey`, `join`, etc. |
| `spark.sql.shuffle.partitions` | 200 | DataFrame/SQL shuffles | Post-shuffle partition count for DataFrames |

**Critical**: Setting `spark.default.parallelism` does NOT affect DataFrame shuffle partitions

---

## DataFrame Schema & Data Types

```python
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, DoubleType

schema = StructType([
    StructField("name", StringType(), nullable=True),
    StructField("age", IntegerType(), nullable=False),
])

df = spark.read.schema(schema).parquet("path")
```

**Best Practice**: Always provide explicit schema (avoids inference surprises)

---

## Join Types Comparison

| Join | Left Rows | Right Rows | Result | Use |
|------|-----------|-----------|--------|-----|
| **INNER** | Match | Match | ✓ Matching only | Common rows |
| **LEFT** | All | Match | ✓ All from left | Keep left rows |
| **RIGHT** | Match | All | ✓ All from right | Keep right rows |
| **FULL** | All | All | ✓ All rows | Complete result |
| **CROSS** | All | All | All × All | Cartesian |
| **LEFT SEMI** | Match | Match | ✓ Left (no right cols) | Filter left by right |
| **LEFT ANTI** | No match | - | ✓ Non-matching left | Exclude by right |

---

## Join Strategy Selection

```
Does one side fit in memory (< 10 MB)?
  → Yes: BroadcastHashJoin (fastest)
  → No: Both sides shuffled
    → Shuffle? (memory available for build-side hash table)
      → Yes: ShuffleHashJoin
      → No: SortMergeJoin (default for large joins)
```

---

## Window Function Reference

| Function | Behavior | Default Frame |
|----------|----------|----------------|
| `row_number()` | Unique sequential | Full partition (no orderBy) or cumulative (with orderBy) |
| `rank()` | Rank with gaps | Same as above |
| `dense_rank()` | Rank without gaps | Same as above |
| `ntile(n)` | Divide into n buckets | Same as above |
| `lag(col, offset)` | Value from prior row | Requires `orderBy` |
| `lead(col, offset)` | Value from next row | Requires `orderBy` |
| `sum(col).over(w)` | Aggregate within window | Cumulative if `orderBy` |

**Default Frame Semantics**:
- **With `orderBy`**: `RANGE BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW` (cumulative)
- **Without `orderBy`**: `ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING` (full partition)

---

## Caching Decision Matrix

| Situation | Cache? | Why |
|-----------|--------|-----|
| Single use | No | Overhead not recouped |
| Multiple actions | Yes | Avoid recomputation |
| Large data > executor memory | Maybe | Risk of spill/OOM |
| Iterative algorithm | Yes | Saves recomputation across iterations |
| Very fast source (e.g., CSV) | No | Overhead may exceed read cost |

---

## GroupBy Aggregation Patterns

```python
# Single key
df.groupBy("dept").count()

# Multiple keys
df.groupBy("dept", "year").sum("salary")

# Multi-aggregate
df.groupBy("dept").agg(
    F.count("*").alias("count"),
    F.avg("salary").alias("avg"),
    F.max("bonus").alias("max")
)

# Rollup (hierarchical subtotals)
df.rollup("year", "month").agg(F.sum("sales"))
# Result: (year, month), (year, NULL), (NULL, NULL)

# Cube (all combinations)
df.cube("dept", "region").agg(F.sum("revenue"))
# Result: All 2^2 = 4 combinations
```

---

## Streaming Trigger Configuration

| Trigger | Behavior | Use Case |
|---------|----------|----------|
| `processingTime("30s")` | Start batch every 30s | Predictable intervals |
| `once=True` | Process all available, stop | One-time backfill |
| `availableNow=True` | Process all available (with limits), stop | Better than once=True |
| `continuous("1s")` | Experimental; low-latency | Not recommended; experimental |

---

## Watermarking Configuration

```python
df_watermarked = (df
    .withWatermark("event_time", "10 minutes")
    .groupBy(F.window("event_time", "5 minutes"))
    .agg(F.count("*")))

result = df_watermarked.writeStream \
    .outputMode("append") \  # Only safe mode with watermark
    .option("checkpointLocation", "/path/to/checkpoint") \
    .start()
```

**Watermark Effect**:
- Events before watermark: Dropped
- State older than watermark: Evicted (bounds memory)

---

## Output Mode Selection for Streaming

| Mode | Emit When | State | Watermark Safe |
|------|-----------|-------|---|
| **Append** | After watermark passes | Bounded (old state evicted) | ✓ Yes |
| **Update** | Value changes | Partial | ⚠️ Maybe |
| **Complete** | Every trigger | Unbounded | ✗ No |

---

## Memory Configuration Quick Reference

```
spark.executor.memory=4g              # JVM heap per executor
spark.executor.memoryOverhead=0.1g    # Off-heap per executor
spark.memory.fraction=0.6             # % of memory = unified region
spark.memory.storageFraction=0.5      # % of unified = storage (initial)
```

**Key**: Execution memory can evict storage memory under pressure

---

## Shuffle Configuration

| Config | Default | Use |
|--------|---------|-----|
| `spark.sql.shuffle.partitions` | 200 | Post-shuffle partition count |
| `spark.shuffle.sort.bypassMergeThreshold` | 200 | Skip sorting if # reducers ≤ threshold |
| `spark.shuffle.compress` | true | Compress shuffle data |
| `spark.reducer.maxSizeInFlight` | 48 MB | Max concurrent shuffle bytes |

---

## GC Tuning Configuration

```
--conf spark.executor.extraJavaOptions="-XX:+UseG1GC -XX:MaxGCPauseMillis=30"
```

- Use G1GC for heaps > 4 GB
- Target pause: 30 ms typical
- Increase executor memory to reduce GC frequency

---

## Network Failure Configuration

| Config | Default | Meaning |
|--------|---------|---------|
| `spark.rpc.numRetries` | 3 | Max retry attempts |
| `spark.rpc.retry.wait` | 3s | Initial wait; exponential backoff (3s → 6s → 12s) |
| `spark.network.timeout` | 120s | Global network timeout |

---

## Broadcast Variable Lifecycle

```
Driver: val bvar = sc.broadcast(obj)
         ↓ Serialize (once)
Executors: Receive, deserialize (once), cache
Tasks: Share cached copy (no re-serialization)
```

**Use Cases**: Large lookup tables, configuration, ML models
**Anti-Patterns**: Large DataFrames (use hint instead), non-serializable objects

---

## Accumulator Semantics

| Operation | Timing | Visibility |
|-----------|--------|-----------|
| `acc.add(value)` | Task execution | Not visible to driver yet |
| `acc.value` (during action) | While running | Partial (incomplete partitions) |
| `acc.value` (after action) | After completion | Final value |

**Guarantee**: At-least-once (retries increment multiple times)

---

## Data Skew Mitigation Strategies

| Strategy | How | Trade-off |
|----------|-----|-----------|
| **Salting** | Add random suffix to split skewed key | Extra unsalting; more partitions |
| **AQE Skew** | Automatic detection + split | Requires `spark.sql.adaptive.skewJoin.enabled=true` |
| **Join Strategy** | Use broadcast if one side small | Requires < 10 MB one side |

---

## Small File Problem Solutions

| Approach | Method | Trade-off |
|----------|--------|-----------|
| **Write** | `coalesce(n)` before write | May cause OOM if data large |
| **Read** | `maxPartitionBytes` merges small files | Automatic; reduces task count |
| **Proactive** | Plan partition count upfront | Requires size knowledge |

---

## Memory Anchors by Topic (Iteration 9)

### Topic 1: Core Spark Concepts
1. **SparkSession wraps SparkContext** — access via `spark.sparkContext` for RDD ops
2. **RDD vs DataFrame**: RDD = low-level control; DataFrame = Catalyst optimized
3. **`spark.default.parallelism` = RDD operations ONLY**; DataFrames use `spark.sql.shuffle.partitions`
4. **Lazy evaluation**: Transformations define plan; actions trigger execution
5. **Narrow vs Wide**: Narrow (map, filter) = single stage; Wide (groupBy, join) = shuffle + new stage

### Topic 2: Spark SQL & DataFrame
1. **Schema inference**: Parquet (fast) vs JSON (slower); use explicit schema in production
2. **Join types**: INNER (matching), OUTER (all rows), SEMI (filter left), ANTI (exclude left)
3. **Join strategies**: Broadcast (< 10 MB) → Shuffle Hash → Sort-Merge
4. **Nullable**: Advisory hint; Spark doesn't enforce (unlike SQL databases)

### Topic 3: Advanced Transformations
1. **Window functions**: Default frame cumulative with `orderBy`; full partition without
2. **When to cache**: Multiple accesses; iterative algorithms; complex pipelines
3. **GroupBy/Rollup/Cube**: `rollup` = hierarchy; `cube` = all combinations
4. **NULL in rollup**: Indicates aggregation level, not data null; use `F.grouping()` to detect

### Topic 4: Performance & Tuning
1. **Optimal partition size**: 1-2 MB per partition
2. **Catalyst phases**: Parse → Analyze → Optimize (predicate pushdown, projection pushdown) → Plan → Execute
3. **CBO requires**: Stats via `ANALYZE TABLE`
4. **GC tuning**: Use G1GC for large heaps; increase memory or use `_SER` storage levels

### Topic 5: Streaming
1. **Triggers**: `processingTime` (interval-based); `once` (backfill); `availableNow` (better than once)
2. **Watermark**: `max(event_time) − threshold`; enables state eviction; requires Append mode
3. **State store**: Checkpointed; survives restarts; structure: offsets/, commits/, state/
4. **Exactly-once**: Idempotent state + idempotent sink

### Topic 6: Distributed Patterns
1. **Broadcast**: Serialize once (driver) → distribute → deserialize once (executor) → cache → task share
2. **Accumulator**: Write during tasks; read after action completes; at-least-once guarantee
3. **Anti-patterns**: Broadcasting large DataFrames (use hint); broadcasting non-serializable objects

### Topic 7: Production Reliability
1. **Skew symptoms**: One task much slower; stage latency = max(partition latencies)
2. **Skew mitigation**: Salting (manual) or AQE (automatic); different join strategy
3. **Small files**: Many partitions with little data; solution: coalesce on write or `maxPartitionBytes` on read
4. **Network retries**: Exponential backoff 3s → 6s → 12s; total ~21s for 3 retries

---

## 10-Point Success Checklist

- [ ] SparkSession wraps SparkContext; use `spark.sparkContext` for RDD access
- [ ] `spark.default.parallelism` affects RDD operations only, not DataFrames
- [ ] Lazy evaluation: transformations define plan; actions execute
- [ ] Window functions default to cumulative frame if `orderBy` present
- [ ] Broadcast join requires one side < 10 MB
- [ ] Watermarking bounds state; requires Append mode for safety
- [ ] Execution memory can evict storage memory under pressure
- [ ] Catalyst optimizations: predicate/projection pushdown, constant folding
- [ ] Data skew: salting (manual) or AQE (automatic)
- [ ] Exactly-once streaming needs idempotent state + idempotent sink
