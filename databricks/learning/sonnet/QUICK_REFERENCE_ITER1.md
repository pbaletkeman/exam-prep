# Databricks Certified Associate Developer for Apache Spark — Quick Reference (Iteration 1)

**Edition**: Iteration 1 (100 Questions)
**Generated**: 2026-05-17
**Format**: Fast-lookup tables, decision matrices, memory anchors
**Difficulty Split**: 20 Easy / 60 Medium / 20 Hard
**Unique Coverage**: Spark Connect + Pandas API on Spark (not in Iter 7–10)

---

## Table of Contents

1. [Topic 1 — Architecture Quick Reference](#topic-1--architecture-quick-reference)
2. [Topic 2 — Spark SQL Quick Reference](#topic-2--spark-sql-quick-reference)
3. [Topic 3 — DataFrame API Quick Reference](#topic-3--dataframe-api-quick-reference)
4. [Topic 4 — Troubleshooting Quick Reference](#topic-4--troubleshooting-quick-reference)
5. [Topic 5 — Structured Streaming Quick Reference](#topic-5--structured-streaming-quick-reference)
6. [Topic 6 — Spark Connect Quick Reference](#topic-6--spark-connect-quick-reference)
7. [Topic 7 — Pandas API on Spark Quick Reference](#topic-7--pandas-api-on-spark-quick-reference)
8. [Master Configs Table](#master-configurations-table)
9. [Memory Anchors](#memory-anchors)
10. [10-Point Exam Success Checklist](#10-point-exam-success-checklist)

---

## TOPIC 1 — Architecture Quick Reference

### Component Responsibilities

| Component | Primary Role | Runs Where |
|-----------|-------------|-----------|
| **Driver** | Builds DAG; schedules Tasks; collects results | Master/client node |
| **SparkContext** | Low-level API; RDD creation; broadcasts/accumulators | Inside Driver |
| **SparkSession** | Unified API (DataFrames, SQL, Streaming) | Inside Driver |
| **DAGScheduler** | Splits DAG into Stages; stage fault tolerance | Inside Driver |
| **TaskScheduler** | Assigns Tasks to Executor slots | Inside Driver |
| **Executor** | Runs Tasks; stores cached data | Worker nodes |
| **Cluster Manager** | Allocates resources to Driver/Executors | Separate process |

---

### Transformation Classification

| Transformation | Type | Stage Boundary? |
|---------------|------|-----------------|
| `filter()` | Narrow | No |
| `select()` | Narrow | No |
| `withColumn()` | Narrow | No |
| `map()` | Narrow | No |
| `flatMap()` | Narrow | No |
| `union()` | Narrow | No |
| `groupBy()` | Wide | YES |
| `join()` (SortMergeJoin) | Wide | YES |
| `orderBy()` / `sort()` | Wide | YES |
| `distinct()` | Wide | YES |
| `repartition()` | Wide | YES |
| `coalesce()` | Narrow* | No (*reduces only) |
| `reduceByKey()` | Wide | YES |

---

### Actions vs Transformations — Quick Test

**Actions** (trigger execution): `count()`, `show()`, `collect()`, `take(n)`, `first()`, `write.*`, `foreach()`, `reduce()`

**Transformations** (lazy): everything else — `filter`, `select`, `join`, `groupBy`, `withColumn`, `map`, `flatMap`, `distinct`, `orderBy`

---

### Ranking Functions Cheat Sheet

Given values: 100, 200, 200, 300

| Function | Result | Rule |
|----------|--------|------|
| `row_number()` | 1, 2, 3, 4 | Always unique |
| `rank()` | 1, 2, 2, 4 | Ties skip next rank(s) |
| `dense_rank()` | 1, 2, 2, 3 | Ties do NOT skip |

---

### Memory Anchors — Topic 1 (5)

1. **Driver = Brain**: Builds the DAG, schedules everything; SparkContext lives here
2. **Executor = Muscle**: Does actual data processing; stores cache
3. **Narrow = No Shuffle = Same Stage**: `filter`, `select`, `map` never cross stage boundaries
4. **Wide = Shuffle = New Stage**: Any operation that requires data from other partitions
5. **Tasks = One Per Partition**: If a stage has 200 partitions → 200 tasks

---

## TOPIC 2 — Spark SQL Quick Reference

### Join Types at a Glance

| Type | Left Rows | Right Rows | Adds nulls? |
|------|----------|-----------|------------|
| `inner` | Match only | Match only | No |
| `left` | All | Match only | Right side |
| `right` | Match only | All | Left side |
| `full` | All | All | Both sides |
| `left_semi` | Match only | None (not included) | No |
| `left_anti` | Non-match only | None | No |
| `cross` | All | All | No |

---

### SQL Aggregation Functions

| Function | Returns |
|----------|---------|
| `COUNT(*)` | Row count including nulls |
| `COUNT(col)` | Non-null count |
| `COUNT(DISTINCT col)` | Distinct non-null values |
| `SUM(col)` | Sum of non-null values |
| `AVG(col)` | Mean of non-null values |
| `MAX(col)` | Maximum value |
| `MIN(col)` | Minimum value |

---

### Catalyst Optimisation Quick Checklist

| Optimisation | What It Does |
|-------------|-------------|
| Predicate Pushdown | Filters moved toward data source |
| Projection Pushdown | Unneeded columns dropped early (Parquet/ORC) |
| Constant Folding | Static expressions evaluated at plan time |
| Join Reordering | Smaller tables joined first |
| Broadcast Propagation | Small tables auto-broadcast |

---

### Memory Anchors — Topic 2 (5)

1. **`createOrReplaceTempView`** = Session-scoped; **`createOrReplaceGlobalTempView`** = Cross-session
2. **LEFT SEMI** = Only left columns; only matching left rows (≈ EXISTS subquery)
3. **LEFT ANTI** = Only left columns; only NON-matching rows (≈ NOT EXISTS)
4. **`dense_rank` = No Gaps**: Consecutive numbers even with ties
5. **Rollup ⊂ Cube**: Rollup is hierarchical subtotals; Cube is all combinations

---

## TOPIC 3 — DataFrame API Quick Reference

### Column Reference Methods

```python
df.select("column_name")         # string
df.select(col("column_name"))    # col() function
df.select(df["column_name"])     # df subscript
df.select(df.column_name)        # attribute (works if no spaces/special chars)
```

### Write Modes

| Mode | Existing Data Behaviour |
|------|------------------------|
| `overwrite` | Delete all; write new |
| `append` | Add new rows alongside existing |
| `error` / `errorifexists` | Raise exception (default) |
| `ignore` | Skip write silently |

---

### Null Handling Functions

| Function | Use |
|----------|-----|
| `isNull()` | Filter null values |
| `isNotNull()` | Filter non-null values |
| `coalesce(c1, c2, ...)` | First non-null value |
| `fillna(value, subset)` | Replace nulls with value |
| `dropna(how, subset)` | Remove rows with nulls |

---

### UDF Type Comparison

| Type | Performance | Optimisation | Best For |
|------|------------|-------------|---------|
| Built-in functions | Fastest | Full Catalyst support | Always prefer |
| Pandas UDF (vectorised) | Fast (Arrow) | Partial | Vectorisable logic |
| Python UDF | Slow (JVM↔Python) | None | Complex custom logic |

---

### Common Data Formats

| Format | Read | Partitioning | Schema Evolution | Best For |
|--------|------|-------------|-----------------|---------|
| CSV | `.csv()` | No | Manual | Raw/legacy |
| JSON | `.json()` | No | Limited | Semi-structured |
| Parquet | `.parquet()` | Yes (built-in) | Yes | Analytics; most common |
| Delta | `.format("delta")` | Yes | Yes (MERGE SCHEMA) | Lakehouse |
| ORC | `.orc()` | Yes | Yes | Hive workloads |

---

### When Function Decision Tree

```
Need conditional column?
  └── Single condition → when(condition, value).otherwise(other)
  └── Multiple conditions → chain .when().when().otherwise()
  └── SQL equivalent → CASE WHEN ... THEN ... ELSE ... END
```

---

### Memory Anchors — Topic 3 (5)

1. **`distinct()` vs `dropDuplicates(cols)`**: `distinct` = all columns; `dropDuplicates` = specified subset
2. **`coalesce` vs `repartition`**: `coalesce` = merge partitions (no shuffle); `repartition` = redistribute (with shuffle)
3. **`orderBy` causes shuffle** (wide); all data must be globally sorted
4. **Pandas UDF uses Arrow**: Transfers data as columnar batch → 10–100x faster than Python UDF
5. **UDFs break Catalyst**: Built-in functions always preferred; UDFs are black boxes to optimiser

---

## TOPIC 4 — Troubleshooting Quick Reference

### Symptom → Diagnosis → Fix Matrix

| Symptom | Likely Cause | Fix |
|---------|-------------|-----|
| Most tasks fast; few very slow | Data Skew | Salting; AQE skew join; broadcast |
| All tasks slow; shuffle read huge | Too few partitions | Increase `spark.sql.shuffle.partitions` |
| Many tiny tasks; fast but many | Too many small partitions | `coalesce(n)` before write |
| OOM on executor | Partition too large | Increase partitions; reduce `maxPartitionBytes` |
| OOM on driver | `collect()` on large DF | Never collect large data; use write instead |
| High GC time | Too much heap pressure | Reduce memory usage; increase `spark.executor.memory` |

---

### Cache Storage Levels

| Level | Memory | Disk | Serialised | Replicated |
|-------|--------|------|-----------|-----------|
| `MEMORY_ONLY` | Yes | No | No | No |
| `MEMORY_AND_DISK` | Yes | Yes (overflow) | No | No |
| `MEMORY_ONLY_SER` | Yes (compressed) | No | Yes | No |
| `DISK_ONLY` | No | Yes | Yes | No |
| `MEMORY_AND_DISK_2` | Yes | Yes | No | Yes (×2) |

`cache()` = `MEMORY_AND_DISK`

---

### Memory Anchors — Topic 4 (5)

1. **Skew = Slow tail tasks**: One partition has 10× more data than others
2. **coalesce ≠ repartition**: `coalesce` only shrinks (no shuffle); `repartition` can grow or shrink (shuffle)
3. **cache() ≠ checkpoint()**: `cache()` keeps lineage; `checkpoint()` truncates lineage + writes to storage
4. **Spark UI Stage tab**: Task duration histogram instantly reveals skew (long right tail)
5. **`unpersist()` frees memory**: Always call when cached DF no longer needed

---

## TOPIC 5 — Structured Streaming Quick Reference

### Output Mode Compatibility

| Operation | Append | Complete | Update |
|-----------|--------|----------|--------|
| Simple select/filter | Yes | No | No |
| Aggregation without watermark | No | Yes | Yes |
| Aggregation with watermark | Yes | Yes | Yes |
| `dropDuplicates` | Yes (with watermark) | No | No |

---

### Trigger Types

| Trigger | Code | Behaviour |
|---------|------|-----------|
| Default | (none) | Process as fast as possible |
| Fixed interval | `processingTime="10 seconds"` | Run every N seconds |
| Once | `once=True` | Run one batch; stop |
| Available Now | `availableNow=True` | Process all available; stop |

---

### Watermark Semantics

```
Watermark = max(event_time seen) − delay_threshold
Events with event_time < watermark → DROPPED
Windows ending before watermark → EVICTED from state store
```

---

### Exactly-Once Requirements

1. **Replayable source**: Kafka (committed offsets), file source (idempotent re-read)
2. **Idempotent/transactional sink**: Delta Lake, custom idempotent write
3. **Checkpoint**: Stores offsets + committed batch IDs

---

### Memory Anchors — Topic 5 (5)

1. **Append = Only new rows**: Cannot update previously emitted rows
2. **Complete = Whole table every batch**: All result rows rewritten; suitable for small aggregates
3. **Watermark required for Append mode** with aggregations (guarantees windows are closed)
4. **Checkpoint = Fault tolerance**: Without it, streaming restarts from scratch
5. **`once=True`** = Batch-style trigger: Process available data once, then stop

---

## TOPIC 6 — Spark Connect Quick Reference

### Architecture Comparison

| Aspect | Classic Spark | Spark Connect |
|--------|--------------|---------------|
| Entry point | `SparkSession` (in-process) | `SparkSession.builder.remote(url)` |
| Plan building | In JVM Driver | Client-side (protobuf) |
| Transport | In-process | gRPC over network |
| `SparkContext` available | Yes | No |
| RDD operations | Yes | No |
| Use case | Embedded/local | Remote multi-tenant |

---

### Connection URL Format

```
sc://host:port
sc://localhost:15002
```

---

### Supported in Spark Connect

- All DataFrame API operations (`select`, `filter`, `join`, `groupBy`, etc.)
- Spark SQL queries
- Structured Streaming (with limitations)
- Python/Scala/Java/R clients

### NOT Supported in Spark Connect

- `SparkContext` / RDD operations (client-side)
- Full accumulator support
- Some legacy MLlib APIs

---

### Memory Anchors — Topic 6 (5)

1. **Spark Connect = Remote Spark**: Client sends plan via gRPC; server executes
2. **No `SparkContext` on client**: Only DataFrame/SQL API available
3. **`sc://` = Spark Connect URL prefix**: Distinguishes from classic JDBC connections
4. **Introduced in Spark 3.4**: Relatively new; exam tests conceptual understanding
5. **Use case = Notebooks & CI/CD**: Lightweight clients connect to shared cluster

---

## TOPIC 7 — Pandas API on Spark Quick Reference

### Key Differences: Pandas vs Pandas API on Spark

| Feature | pandas | Pandas API on Spark |
|---------|--------|---------------------|
| Import | `import pandas as pd` | `import pyspark.pandas as ps` |
| Execution | Local (single machine) | Distributed (Spark cluster) |
| Data size | Fits in RAM | Scales to PB |
| Row order guaranteed | Yes | No (Spark is unordered) |
| Index semantics | Natural int index | Emulated; configurable type |
| `collect()` needed | N/A | Avoid; expensive |

---

### Conversion Functions

| From | To | Code |
|------|----|------|
| Spark DF | Pandas API DF | `spark_df.pandas_api()` |
| Pandas API DF | Spark DF | `ps_df.to_spark()` |
| Pandas API DF | pandas DF | `ps_df.to_pandas()` (collects!) |
| pandas DF | Pandas API DF | `ps.from_pandas(pd_df)` |

---

### Default Index Types

| Type | Speed | Consistency | Use When |
|------|-------|-------------|---------|
| `sequence` | Slow (sequential scan) | Yes | Small data; full pandas compatibility |
| `distributed` | Fast | No (gaps/non-contiguous) | Large data; performance priority |
| `distributed-sequence` | Medium | Yes | Balance; default for most cases |

---

### Pandas API Operations to Avoid (Performance)

- `.apply()` with non-vectorisable Python functions (triggers slow UDF path)
- `.loc` / `.iloc` with complex slicing (forces collect)
- Sorting without partitioning (global sort = huge shuffle)
- Converting to pandas (`to_pandas()`) on large DataFrames

---

### Memory Anchors — Topic 7 (5)

1. **`pyspark.pandas`** = Formerly Koalas; same import name since Spark 3.2
2. **Syntax = pandas; engine = Spark**: Write pandas code; run on distributed cluster
3. **`to_pandas()` = DANGER on large data**: Collects everything to driver RAM
4. **No guaranteed row order**: Spark's distributed nature means rows can come back in any order
5. **`ps_df.to_spark()`** = Escape hatch: Convert back to native PySpark DataFrame

---

## Master Configurations Table

| Property | Default | Category | Notes |
|----------|---------|----------|-------|
| `spark.sql.shuffle.partitions` | 200 | Parallelism | Reduce for small data; AQE can override |
| `spark.sql.autoBroadcastJoinThreshold` | 10 MB | Joins | -1 disables broadcasts |
| `spark.default.parallelism` | cores × 2 | RDD parallelism | For RDD ops; not SQL |
| `spark.executor.memory` | 1 GB | Resources | Increase for OOM |
| `spark.executor.cores` | 1 | Resources | 4–5 typical for batch |
| `spark.sql.files.maxPartitionBytes` | 128 MB | Input | Controls input partition size |
| `spark.sql.adaptive.enabled` | true (3.x) | AQE | Enables dynamic optimisation |
| `spark.sql.adaptive.skewJoin.enabled` | true (3.x) | AQE | Handles data skew automatically |
| `spark.speculation` | false | Fault tol. | Enables speculative task execution |
| `spark.task.maxFailures` | 4 | Fault tol. | Retry limit per task |

---

## Memory Anchors (All Topics)

### Topic 1 — Architecture
1. Driver = Brain; Executor = Muscle
2. Narrow = No Shuffle = Same Stage
3. Wide = Shuffle = New Stage
4. Tasks = One Per Partition
5. SparkSession = Unified entry point (Spark 2.0+)

### Topic 2 — Spark SQL
1. `createOrReplaceTempView` = Session scope
2. `LEFT SEMI` = EXISTS-style filter
3. `LEFT ANTI` = NOT EXISTS-style filter
4. `dense_rank` = No gaps on ties
5. Rollup = Hierarchical; Cube = All combinations

### Topic 3 — DataFrame API
1. `distinct()` = all columns; `dropDuplicates(cols)` = specific cols
2. `coalesce` = shrink (no shuffle); `repartition` = any size (shuffle)
3. `orderBy` is WIDE (shuffle required)
4. Pandas UDF uses Arrow → much faster than Python UDF
5. UDFs are black boxes to Catalyst

### Topic 4 — Troubleshooting
1. Skew = Slow tail tasks
2. `coalesce` only shrinks (no shuffle)
3. `cache()` keeps lineage; `checkpoint()` truncates it
4. Spark UI Stage tab → task duration histogram reveals skew
5. Always `unpersist()` when done

### Topic 5 — Structured Streaming
1. Append = new rows only
2. Complete = whole table every batch
3. Watermark required for Append + aggregation
4. Checkpoint = fault tolerance + exactly-once
5. `once=True` = one batch then stop

### Topic 6 — Spark Connect
1. Client sends plan via gRPC; server executes
2. No `SparkContext` on client
3. URL prefix: `sc://`
4. Introduced in Spark 3.4
5. Use case: remote notebooks and CI/CD

### Topic 7 — Pandas API on Spark
1. `pyspark.pandas` = formerly Koalas
2. Pandas syntax; Spark engine
3. `to_pandas()` = dangerous on large data
4. No guaranteed row order
5. `ps_df.to_spark()` = escape back to native Spark DF

---

## 10-Point Exam Success Checklist

| # | Check | Must Know |
|---|-------|----------|
| 1 | **Transformations vs Actions** | Know every common action; everything else is lazy |
| 2 | **Narrow vs Wide** | `filter/select/withColumn` = narrow; `groupBy/join/orderBy/distinct` = wide |
| 3 | **Ranking Functions** | `row_number` = unique; `rank` = gaps; `dense_rank` = no gaps |
| 4 | **shuffle.partitions** | Default 200; this config controls POST-SHUFFLE partitions |
| 5 | **Join Types** | Inner/Left/Right/Full/Semi/Anti/Cross — know what rows each returns |
| 6 | **Streaming Output Modes** | Append=new; Complete=all; Update=changed |
| 7 | **Watermark** | Required for Append mode aggregations; drops late data |
| 8 | **Spark Connect** | gRPC client-server; `sc://` URL; no SparkContext on client |
| 9 | **Pandas API** | `pyspark.pandas`; pandas syntax; `to_spark()` / `to_pandas()` conversions |
| 10 | **UDF Performance** | Built-in > Pandas UDF > Python UDF; UDFs bypass Catalyst |
