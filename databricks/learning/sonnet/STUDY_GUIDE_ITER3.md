# Databricks Certified Associate Developer — Study Guide (Iteration 3)

**Edition**: Iteration 3 | **Difficulty**: 20E / 60M / 20H | **Answer Types**: 79 single / 21 multi-answer

---

## Topic 1 — Apache Spark Architecture & Internals (Q1–Q20)

### 1.1 Lineage: RDD vs DataFrame

**RDD lineage** is a chain of parent RDD dependencies tracked in a Directed Acyclic Graph (DAG). Each transformation records its parent, enabling Spark to recompute lost partitions by replaying the lineage from stable input data.

**DataFrame lineage** is stored as an *optimized logical plan*. Before execution, the Catalyst optimizer rewrites the logical plan through a series of rule-based and cost-based transformations, producing a physical plan. This is fundamentally different from RDD lineage — the optimizer can push down filters, reorder joins, and fuse operators in ways that are impossible at the raw RDD level.

Both use the same underlying DAG engine, but DataFrame lineage passes through Catalyst before reaching the execution layer.

### 1.2 WholeStageCodegen

WholeStageCodegen is part of Spark's **Tungsten** execution engine. It fuses multiple operators (e.g., `filter`, `project`, `hash aggregate`) that fall within a single pipeline stage into **a single optimized JVM bytecode function**. This eliminates virtual function dispatch overhead — instead of calling separate `eval()` methods on each operator per row, the generated code processes rows in a tight loop with no abstraction boundary.

In the physical plan, stages where WholeStageCodegen applies are prefixed with `*` (e.g., `*(1) Filter`, `*(1) HashAggregate`). Stages lacking codegen show no `*` prefix.

### 1.3 Tungsten Project

Tungsten provides three categories of improvements:
1. **Binary data encoding** — stores data in off-heap or managed on-heap memory in a compact binary format, eliminating Java object overhead and reducing GC pressure
2. **Cache-aware computation** — sorts data to improve CPU cache hit rate (cache-aware sorting, aggregation)
3. **Code generation (WholeStageCodegen)** — generates optimized JVM bytecode per pipeline, eliminating interpreted virtual dispatch

### 1.4 External Shuffle Service

The external shuffle service is a daemon running on each worker node that stores **shuffle intermediate files** and serves them to downstream Tasks. Its key function: it decouples shuffle data lifetime from Executor lifetime.

Without it, if an Executor is removed by **Dynamic Resource Allocation (DRA)**, its shuffle output files would be lost — forcing costly recomputation. With the external shuffle service, the worker daemon retains the files, so Executors can be safely removed and added without data loss.

**Requirement:** DRA (`spark.dynamicAllocation.enabled = true`) requires the external shuffle service to be running.

### 1.5 `df.checkpoint()` vs `df.persist()`

| | `checkpoint()` | `persist()` |
|-|---------------|-------------|
| Storage | Reliable distributed storage (HDFS/cloud), configured by `sc.setCheckpointDir()` | Executor memory and/or disk (configurable storage level) |
| Lineage | **Truncated** (the lineage graph is severed) | **Retained** (full lineage kept for recomputation) |
| Fault tolerance | Yes — data survives Executor failure | Storage-level dependent (MEMORY_ONLY = no; MEMORY_AND_DISK = spill) |
| Speed | Slower (writes to remote storage) | Faster (writes to local memory/disk) |
| Laziness | **Eager** — triggers an action immediately | **Lazy** — materialised on next action |

**`localCheckpoint()`** is a middle ground: stores on **local Executor disk**, truncates lineage, faster than remote checkpoint but **not fault-tolerant** across Executor failure.

### 1.6 Task Serialization

When the Driver sends a Task to an Executor, it serializes the **closure** — the function to execute plus any variables captured (referenced) within that function's scope. This serialized payload is sent via the TaskScheduler.

Two serializers are available:
- **Java serialization** (default) — standard JVM object serialization; slower, larger
- **Kryo serialization** — faster and more compact; configured with `spark.serializer = org.apache.spark.serializer.KryoSerializer`; classes can be registered for additional efficiency (`spark.kryo.registrationRequired`)

Classes used in Tasks must implement `java.io.Serializable` (Java) or be registered/configured (Kryo).

### 1.7 Off-Heap Memory for Tungsten

Off-heap memory allows Tungsten to store binary data outside the JVM managed heap, reducing GC pressure. Two properties **must both** be set:

```python
spark.conf.set('spark.memory.offHeap.enabled', 'true')
spark.conf.set('spark.memory.offHeap.size', '4g')  # positive byte value
```

Setting only one of these has no effect.

### 1.8 Executor Heartbeat and Timeout

Executors send periodic heartbeat messages to the Driver. Two config properties are relevant:
- `spark.executor.heartbeatInterval` (default 10s) — how often Executors send heartbeats
- `spark.network.timeout` (default 120s) — timeout before declaring an Executor lost

When an Executor fails to heartbeat within the timeout:
1. Driver marks the Executor as **lost**
2. Tasks running on that Executor are **rescheduled** on other available Executors
3. Driver requests the Cluster Manager to **launch a replacement Executor**
4. The application does NOT fail (Tasks are retried automatically up to `spark.task.maxFailures`)

### 1.9 Python UDF Execution Model

PySpark Python UDFs execute through the following process:
1. Executor JVM receives a Task with a Python UDF
2. A **separate Python worker process** is spawned per Executor thread (or reused from a pool)
3. Row data is **pickled** (serialized using Python's pickle protocol) by the JVM
4. Pickled data is sent to the Python worker via a **local socket**
5. The Python worker processes the data and returns pickled results
6. The JVM unpickles results and continues the execution plan

This per-row pickle/unpickle cycle is the primary reason Python UDFs are slower than Scala/Java UDFs. **Pandas UDFs (Arrow-based)** avoid per-row serialization by transferring columnar Apache Arrow batches, which is significantly faster.

### 1.10 Python Worker Memory and Container OOM

Python worker processes run **outside the JVM heap**. Their memory is not controlled by `spark.executor.memory` (which only governs the JVM heap). When using Python UDFs heavily, containers can exceed their total memory limit because:

- JVM heap (`spark.executor.memory`)
- Python worker memory
- Native library overhead

Fix: Increase **`spark.executor.memoryOverhead`** (or `spark.executor.pyspark.memory` for more precise control of the Python worker's memory allowance).

### 1.11 Cluster Manager Comparison

| | Standalone | YARN | Kubernetes |
|-|-----------|------|-----------|
| Requires Hadoop? | **No** | Yes | No |
| Resource tracking | Spark Master | ResourceManager + NodeManager | Pod specifications |
| Deploy modes | client + cluster | client + cluster | client + cluster |
| Driver location | Submitter or worker | AM container | Pod |
| Master URL format | `spark://host:7077` | `yarn` | `k8s://https://host:port` |

Key facts:
- Standalone does **NOT** require a Hadoop installation
- All three support both client and cluster deploy modes
- Kubernetes uses Pods for Driver and Executor containers with the `k8s://` master URL

### 1.12 Data Locality Levels

Spark's TaskScheduler prefers the highest (most local) level available, waiting `spark.locality.wait` time before falling back to the next level:

| Level | Data Location | Speed |
|-------|--------------|-------|
| `PROCESS_LOCAL` | **Same Executor JVM process** | Fastest |
| `NODE_LOCAL` | Same node, different process | Very fast |
| `RACK_LOCAL` | Same rack, different node | Fast |
| `ANY` | Anywhere in the cluster | Slowest |

`spark.locality.wait` — time to wait before relaxing locality. Higher = better locality but potentially longer task launch delay when preferred nodes are busy.

### 1.13 Speculative Execution Configuration

`spark.speculation = true` enables speculative execution. When enabled, a Task running much slower than the median for its stage triggers a speculative duplicate Task on another Executor. The first to complete wins; the other is cancelled.

Key configs:
- `spark.speculation.multiplier` — how many times slower than the median a Task must be before a speculative copy launches (default: 1.5)
- `spark.speculation.quantile` — fraction of Tasks that must complete before any speculative launch (default: 0.75)
- `spark.speculation.interval` — how often Spark checks for straggler Tasks (default: 100ms)

### 1.14 Resource Profile API

Available since Spark 3.1, the Resource Profile API enables **different Executor resource configurations per Stage** within a single application:

```python
from pyspark.resource import ResourceProfileBuilder, TaskResourceRequests, ExecutorResourceRequests

builder = ResourceProfileBuilder()
task_req = TaskResourceRequests().cpus(4)
exec_req = ExecutorResourceRequests().cores(4).memory('8g').memoryOverhead('2g')
profile = builder.require(exec_req).require(task_req).build()

rdd.withResources(profile)  # attach to RDD
```

- Works on YARN and **Kubernetes** (not Standalone-only)
- Enables GPU resource requests per stage
- Default profile applies to all stages with no explicit profile

### 1.15 Stage Count Analysis (Broadcast Join)

```python
large = spark.read.parquet('/data/events')         # 10 GB
small = spark.read.parquet('/data/lookup')          # 5 MB
joined = large.join(broadcast(small), 'event_type')
result = joined.groupBy('region').agg(F.sum('revenue'))
result.write.parquet('/output')
```

With `autoBroadcastJoinThreshold = 10 MB` (and small = 5 MB), Spark uses a **BroadcastHashJoin**:
- Broadcast joins do NOT add a shuffle boundary (no Stage 0 → Stage 1 split at the join)
- The `groupBy` requires a shuffle → Stage boundary

**Result: 2 Stages**
- Stage 1: scan large + broadcast join + partial aggregation (map-side)
- Stage 2: shuffle + final aggregation + write

If it were a SortMergeJoin instead: 3 Stages (scan large, scan small, join+agg+write).

### 1.16 Unified Memory Model — Execution vs Storage Borrowing

Spark's Unified Memory Model allows the Execution and Storage regions to borrow from each other:

- If **Storage** holds cached blocks and **Execution** needs more memory for a join: Spark **evicts** (spills to disk or drops) cached Storage blocks to satisfy the Execution Memory demand
- If **Execution** is underutilised and **Storage** needs more room for caching: Storage can borrow from the Execution region
- Execution memory that has been borrowed by Storage **cannot be forcibly evicted** once in use — it will be returned naturally when Execution tasks complete

This dynamic sharing is controlled by `spark.memory.fraction` (default 0.6) and `spark.memory.storageFraction` (default 0.5 of the Spark Memory region).

### 1.17 Shuffle Reduce-Side Memory

`spark.reducer.maxSizeInFlight` (default 48 MB) — the maximum amount of shuffle data a single reduce-side Task fetches concurrently from all remote Executors at once. Lowering it reduces memory pressure on the reduce side; raising it increases throughput at the cost of more memory.

This is directly related to `Unable to acquire memory` errors during the shuffle reduce phase — the reducer is trying to hold too much in-flight shuffle data in memory simultaneously.

### 1.18 Job Cancellation API

```python
# Cancel a specific Job by ID
spark.sparkContext.cancelJob(jobId)

# Cancel all running Jobs
spark.sparkContext.cancelAllJobs()

# Tag Jobs with a group, then cancel the entire group
spark.sparkContext.setJobGroup('my-group', 'description')
# ... run Jobs ...
spark.sparkContext.cancelJobGroup('my-group')

# Stop the entire SparkSession (cancels all Jobs)
spark.stop()

# Cancel a Stage (note: this is Stage-level, not Job-level)
spark.sparkContext.cancelStage(stageId)
```

---

## Topic 2 — Spark SQL (Q21–Q40)

### 2.1 Core JSON Functions

**`F.from_json(col, schema)`** — parses a `StringType` JSON column into a structured column (`StructType` or `MapType`). A schema must be provided.

```python
schema = StructType([StructField('id', IntegerType()), StructField('name', StringType())])
df.withColumn('parsed', F.from_json(col('payload'), schema))
```

**`F.to_json(col)`** — converts a `StructType`, `MapType`, or `ArrayType` column to a `StringType` JSON string. Returns `StringType`.

**`F.schema_of_json(json_string)`** — returns a `StringType` DDL string describing the inferred schema of a JSON literal, e.g., `'STRUCT<id: BIGINT, name: STRING, scores: ARRAY<DOUBLE>>'`. This is useful for deriving schemas programmatically but returns a **string**, not a `StructType` Python object.

### 2.2 Struct Functions

**`F.struct(*cols)`** — creates a `StructType` column from the provided columns:
```python
F.struct(col('first_name'), col('last_name'))  # → StructType{first_name: String, last_name: String}
```

**`F.to_timestamp(col, format)`** — parses a `StringType` column to `TimestampType` with an explicit format:
```python
F.to_timestamp(col('event_ts'), 'yyyy-MM-dd HH:mm:ss')
```
Note: `F.cast()` is a Column method (`col('x').cast('timestamp')`), not a standalone function.

### 2.3 Comparison and Null Functions

**`F.greatest(*cols)`** — returns the largest **non-null** value across the specified columns per row:
```python
F.greatest(col('price_a'), col('price_b'), col('price_c'))
```

**`F.least(*cols)`** — returns the smallest non-null value.

**`nvl(col1, col2)`** — returns `col2` if `col1` is null; otherwise returns `col1`. Equivalent to `coalesce(col1, col2)`.

**`nvl2(col1, col2, col3)`** — returns `col2` if `col1` is **NOT** null; returns `col3` if `col1` **IS** null.

### 2.4 Higher-Order Array Functions

These functions operate on `ArrayType` columns with lambda expressions:

**`F.transform(col, lambda x: ...)`** — applies lambda to each element, returns same-length array:
```python
F.transform(col('scores'), lambda x: x * 1.1)  # multiply each element
```

**`F.filter(col, lambda x: ...)`** — filters array to elements satisfying the predicate:
```python
F.filter(col('tags'), lambda x: x.startswith('a'))
# NOT F.array_filter() — that function does not exist
```

**`F.aggregate(col, initialValue, merge_fn)`** — reduces array to a single value:
```python
F.aggregate(col('amounts'), F.lit(0), lambda acc, x: acc + x)  # sum
```

**`F.forall(col, lambda x: ...)`** — returns `True` if ALL elements satisfy predicate:
```python
F.forall(col('scores'), lambda x: x > 0)
```

**`F.exists(col, lambda x: ...)`** — returns `True` if AT LEAST ONE element satisfies predicate:
```python
F.exists(col('scores'), lambda x: x > 100)
```

Both `forall()` and `exists()` return `BooleanType`. If the array column is **null**, both return **null**.

**`F.zip_with(col_a, col_b, lambda x, y: ...)`** — element-wise operation across two same-length arrays:
```python
F.zip_with(col('a'), col('b'), lambda x, y: x + y)  # element-wise sum
```

### 2.5 Array Structural Functions

**`F.flatten(col)`** — concatenates nested arrays (`ArrayType(ArrayType(T))` → `ArrayType(T)`):
```python
# [[1,2],[3,4]] → [1,2,3,4]
F.flatten(col('nested'))
```

**`F.posexplode(col)`** — like `explode()` but adds a `pos` column with the **zero-based integer index**:
```python
# Original: items=['a','b','c']
# explode → 'a', 'b', 'c'
# posexplode → (0,'a'), (1,'b'), (2,'c')
```

**`F.slice(col, start, length)`** — extracts a sub-array using **1-based indexing**:
```python
# ['a','b','c','d','e'], start=2, length=3 → ['b','c','d']
F.slice(col('items'), start=2, length=3)
```

**`F.sequence(start, stop)`** — generates an array of values from start to stop (inclusive):
```python
F.sequence(lit(1), lit(5))  # → ArrayType(LongType): [1, 2, 3, 4, 5]
```

**`F.arrays_zip(*cols)`** — pairs corresponding elements from multiple arrays into `ArrayType(StructType)`:
```python
F.arrays_zip(col('names'), col('scores'))
# → [{names: 'Alice', scores: 95}, {names: 'Bob', scores: 82}, ...]
```

**`F.element_at(col, index)`** — extracts one element from an array using **1-based indexing**:
```python
# ['red','green','blue'], index=2 → 'green'
F.element_at(col('colors'), 2)
```

### 2.6 Map Functions

**`F.map_keys(col)`** — extracts map keys as `ArrayType`
**`F.map_values(col)`** — extracts map values as `ArrayType`

```python
# metadata: MapType(StringType, IntegerType)
F.map_values(col('metadata'))  # → ArrayType(IntegerType)
```

**`F.map_filter(col, lambda k, v: ...)`** — returns a new `MapType` with only entries where predicate is true:
```python
F.map_filter(col('scores'), lambda k, v: v > 50)  # keeps only entries with value > 50
```

**`F.create_map(*alternating_key_value_cols)`** — creates a `MapType` column:
```python
F.create_map(lit('k1'), col('v1'), lit('k2'), col('v2'))
# → MapType(StringType, <v1_type>) with two entries per row
```

### 2.7 Date and Time Functions

**`F.months_between(end, start)`** — returns `DoubleType` (fractional months; negative if end < start):
```python
F.months_between(col('end_date'), col('start_date'))  # 2.5 = 2.5 months between
```

**`F.lpad(col, length, pad)`** — pads on the **LEFT** to reach target length:
```python
F.lpad(col('code'), 6, '0')  # '42' → '000042'
```

**`F.rpad(col, length, pad)`** — pads on the **RIGHT**.

### 2.8 Safe Cast and SQL Safety Functions

**`try_cast(expr AS type)`** — Spark SQL (3.4+): returns **null** instead of raising an error when the cast fails:
```sql
SELECT try_cast('abc' AS INT)  -- returns null, not an exception
```

**`try_divide(a, b)`** — returns null on divide-by-zero instead of raising an error.

### 2.9 SQL PIVOT Syntax

PIVOT rotates row values into columns (long → wide format):

```sql
SELECT *
FROM df
PIVOT (
  SUM(revenue)             -- aggregate function (required)
  FOR product_type          -- column whose values become new column headers
  IN ('Electronics', 'Books', 'Clothing')  -- explicit value list
)
```

Also available via DataFrame API: `df.groupBy('region').pivot('product_type').agg(F.sum('revenue'))`

Key facts:
- **Aggregate function is required** in PIVOT
- Pivot values can be pre-specified (IN list) or discovered dynamically (DataFrame API, more expensive)
- Spark SQL **does have** PIVOT syntax (not just DataFrame API)

### 2.10 LATERAL VIEW Explode

LATERAL VIEW is Spark SQL's table-generating function syntax:

```sql
SELECT user_id, tag
FROM events
LATERAL VIEW explode(tags) t AS tag
```

This creates one row per array element per original row — equivalent to `F.explode()` in the DataFrame API.

### 2.11 SQL Hints

```sql
SELECT /*+ BROADCAST(products) */ a.order_id, b.product_name
FROM orders a
JOIN products b ON a.product_id = b.product_id
```

The `/*+ BROADCAST(table_name) */` hint instructs Catalyst to use a **BroadcastHashJoin** for the specified table, overriding the automatic `autoBroadcastJoinThreshold`-based decision. The table name in the hint must match an alias or table name in the query.

### 2.12 Window Functions — First with ignorenulls

`F.first(col, ignorenulls=True)` in a window context returns the first **non-null** value in the window partition (ordered by the window spec):

```python
w = Window.partitionBy('dept').orderBy('hire_date')
df.withColumn('first_score', F.first('score', ignorenulls=True).over(w))
```

If the first several rows in a partition have null scores, `first_score` returns the value from the first row that has a non-null score.

---

## Topic 3 — DataFrame API (Q41–Q70)

### 3.1 Summary and Describe Methods

**`df.describe(*cols)`** — returns a DataFrame with summary statistics rows for specified columns:
- Rows: `count`, `mean`, `stddev`, `min`, `max`
- Works on numeric and string columns
- Returns `StringType` values for all statistics

**`df.summary(*statistics)`** — like `describe()` but additionally includes:
- Approximate **quartiles**: `25%`, `50%` (median), `75%`
- Can specify which statistics to show: `df.summary('count', '25%', '75%', 'max')`

### 3.2 Sampling and Statistical Methods

**`df.sample(fraction, withReplacement, seed)`** — random sample:
```python
df.sample(fraction=0.1, withReplacement=False, seed=42)
```

**`df.randomSplit([0.8, 0.2], seed=42)`** — splits into multiple DataFrames:
- Split is **approximate** (not exact) due to partition boundaries
- Seed ensures reproducibility across runs

**`df.stat.corr('col_a', 'col_b')`** — returns a Python `float` (Pearson correlation coefficient)

**`df.stat.approxQuantile('col', probabilities, relativeError)`** — computes approximate quantiles:
```python
df.stat.approxQuantile('salary', [0.25, 0.5, 0.75], 0.05)
```
Equivalent to `df.agg(F.percentile_approx('salary', [0.25, 0.5, 0.75]))`.

**`df.stat.freqItems(['col1', 'col2'], support=0.01)`** — returns a DataFrame with one row containing arrays of approximate frequent items (appearing in ≥1% of rows) for each column.

**`df.stat.crosstab('col1', 'col2')`** — produces a cross-tabulation (contingency table):
- Rows = distinct values of `col1`
- Columns = distinct values of `col2`
- Cells = count of rows with that combination
- First column named `col1_col2` (e.g., `gender_education_level`)

### 3.3 DataFrame Transformation and Utility Methods

**`df.limit(n)`** — returns at most N rows; **no guaranteed ordering**.

**`df.hint('name', *args)`** — provides an advisory optimizer hint:
```python
df.hint('repartition', 10)   # suggests ~10 partitions
df.hint('broadcast')          # suggests broadcast join
```
These are hints, not guaranteed actions — Catalyst may ignore them if they conflict with its cost model.

**`df.transform(func)`** — enables clean method chaining of custom transformation functions:
```python
def add_audit_cols(df):
    return df.withColumn('created_at', F.current_timestamp())

def clean_nulls(df):
    return df.na.fill('unknown')

result = df.transform(add_audit_cols).transform(clean_nulls)
```
Equivalent to `clean_nulls(add_audit_cols(df))` but reads left-to-right.

**`df.observe('name', *metrics)`** — attaches named inline metrics to a query:
```python
df.observe('my_metrics',
    F.count(lit(1)).alias('row_count'),
    F.sum('revenue').alias('total_revenue'))
```
Metrics are collected via `QueryExecutionListener` during query execution, without a separate aggregation job.

**`df.printSchema()`** — prints schema tree to console; returns `None`.

**`df.explain('formatted')`** — physical plan with readable layout, node IDs, and subplan details. More navigable than default `df.explain()` for complex plans.

### 3.4 Array Set Operations

```python
F.array_union(col('a'), col('b'))       # elements in either, deduplicated
F.array_intersect(col('a'), col('b'))   # elements in both, deduplicated
F.array_except(col('a'), col('b'))      # elements in a but NOT in b, deduplicated
F.array_distinct(col('a'))              # removes duplicates from single array

# DOES NOT EXIST:
# F.array_concat() ← use F.concat(col('a'), col('b')) instead (preserves duplicates)
```

### 3.5 Schema Definition from DDL

```python
# DDL string → StructType
schema = StructType.fromDDL('id BIGINT, name STRING, active BOOLEAN')

# MapType field in StructType
StructField('attributes', MapType(StringType(), DoubleType()), True)

# NOT valid:
# StructType.parse(...)          ← doesn't exist
# StructField('x', 'MAP<S,D>')   ← type must be TypeObject, not string
```

### 3.6 Write API — insertInto vs saveAsTable

| | `insertInto('table')` | `write.mode('append').saveAsTable('table')` |
|-|-----------------------|--------------------------------------------|
| Column matching | **By position** | **By name** |
| Schema evolution | No | No (unless Delta with mergeSchema) |
| Risk | Silently wrong if column order differs | Safe regardless of column order |

**Use `saveAsTable` with mode='append' for safety** when schema may differ between the DataFrame and the target table.

### 3.7 `writeTo()` v2 Write API

```python
df.writeTo('catalog.schema.table') \
  .createOrReplace()          # create if not exists, replace if does

df.writeTo('catalog.schema.table') \
  .overwritePartitions()      # overwrite matching partitions only

df.writeTo('catalog.schema.table') \
  .append()                   # append to existing table
```

`writeTo()` is the v2 catalog API — required for Delta Lake, Iceberg, and other table formats with advanced operations. `saveAsTable()` is v1 and doesn't support all of these operations.

### 3.8 Bucket Write for Shuffle-Free Joins

```python
df.write \
  .bucketBy(16, 'user_id') \
  .sortBy('event_time') \
  .saveAsTable('events_bucketed')
```

This writes 16 fixed bucket files, each containing rows where `hash(user_id) % 16` maps to that bucket, sorted within each bucket by `event_time`.

**Optimization:** If two tables are bucketed on the same key with the **same number of buckets**, a join between them can **eliminate the shuffle** in SortMergeJoin — each bucket pair is joined locally without redistribution.

### 3.9 Delta Lake Reading

```python
# By path
spark.read.format('delta').load('/path/to/delta')

# By table name (metastore)
spark.read.table('my_delta_table')

# Time travel by version
spark.read.format('delta').option('versionAsOf', 2).load('/path')

# Time travel by timestamp
spark.read.format('delta').option('timestampAsOf', '2024-01-01').load('/path')
```

Delta Lake enforces schema by default, preventing writes with incompatible schemas without explicit schema evolution options (`mergeSchema`, `overwriteSchema`).

### 3.10 `na.replace()` vs `na.fill()`

```python
# replace() — substitutes specific VALUES (not nulls)
df.na.replace(['N/A', 'Unknown', ''], 'missing', subset=['status'])
# → replaces 'N/A', 'Unknown', '' with 'missing'; null stays null

# fill() — fills NULL values with a replacement
df.na.fill('unknown', subset=['status'])
# → replaces null with 'unknown'; existing string values unchanged
```

**`na.replace()` does NOT affect null values.** Use `na.fill()` for nulls.

### 3.11 `localCheckpoint()` vs `checkpoint()`

| | `localCheckpoint()` | `checkpoint()` |
|-|--------------------|----------------|
| Storage | Local Executor disk | Reliable distributed storage (HDFS/cloud) |
| Speed | Faster | Slower |
| Fault-tolerant? | **No** (if Executor dies, data is lost) | **Yes** |
| Lineage truncated? | Yes | Yes |
| Requires `setCheckpointDir`? | No | Yes |

### 3.12 `df.stat.crosstab()` Detail

The result has:
- First column named `<col1>_<col2>` (e.g., `gender_education_level`)
- One column per distinct value of col2
- One row per distinct value of col1
- Cells contain the count of rows with that combination

This is equivalent to `df.groupBy('gender', 'education_level').count()` pivoted on `education_level`.

---

## Topic 4 — Troubleshooting & Tuning (Q71–Q80)

### 4.1 EXPLAIN Modes

```python
df.explain()              # default: physical plan
df.explain('simple')      # same as default
df.explain('extended')    # logical + physical plans
df.explain('formatted')   # physical plan with node IDs and readable format (recommended)
df.explain('cost')        # physical plan with cost estimates (requires CBO)
df.explain('codegen')     # shows generated Java code from WholeStageCodegen
```

`explain('formatted')` is most useful for navigating complex plans with many operators — it includes subplan IDs and argument summaries.

`explain('codegen')` is useful for diagnosing whether expressions are preventing code generation.

### 4.2 Runtime Configuration Changes

```python
# Change shuffle partitions at runtime (correct)
spark.conf.set('spark.sql.shuffle.partitions', 50)

# NOT this (not valid Python attribute access):
# spark.sql.shuffle.partitions = 50

# NOT this (wrong property name — note: 'shuffle' vs 'sql.shuffle'):
# spark.conf.set('spark.shuffle.partitions', 50)  # wrong key
```

### 4.3 Cost-Based Optimizer (CBO)

When CBO is enabled (`spark.sql.cbo.enabled = true`) and table statistics are collected (`ANALYZE TABLE ... COMPUTE STATISTICS`), Spark can:
- **Reorder joins** in multi-table queries to minimize the size of intermediate results
- Choose between `SortMergeJoin` and `BroadcastHashJoin` based on estimated sizes
- Filter selectivity estimation

Without statistics, CBO falls back to rule-based decisions only.

### 4.4 AQE Configurations

| Config | Controls |
|--------|---------|
| `spark.sql.adaptive.enabled` | Enable/disable AQE (default: true in Spark 3.0+) |
| `spark.sql.adaptive.skewJoin.enabled` | Enable AQE skew join splitting |
| `spark.sql.adaptive.skewJoin.skewedPartitionFactor` | Multiple of median size that marks a partition as skewed |
| `spark.sql.adaptive.skewJoin.skewedPartitionThresholdInBytes` | Byte threshold above which a partition is skewed |
| `spark.sql.adaptive.coalescePartitions.enabled` | Automatically coalesce small shuffle partitions |

### 4.5 Data Locality Wait

`spark.locality.wait` (default 3s) — Spark waits this long at each locality level before relaxing to the next less-local level.

**Trade-off:** Higher `spark.locality.wait` → better data locality → less network I/O → but potential Task launch delays when preferred Executors are busy with other Tasks.

**Practical use:** Lower it in very large clusters where all nodes are roughly equidistant (e.g., cloud object storage). Keep it higher when data locality matters (e.g., HDFS co-located with compute).

### 4.6 Shuffle Compression and Codecs

`spark.shuffle.compress` (default: `true`) — compresses shuffle output files written during the map phase. Reduces disk I/O at the cost of CPU.

`spark.io.compression.codec` — controls which codec is used:
- Default: **`lz4`** (fast, moderate compression)
- Alternatives: `snappy` (moderate speed/compression), `zstd` (high compression), `gzip` (slowest, highest compression)
- `lz4` is the default — NOT `snappy` (a common confusion)

### 4.7 Executor Cores and HDFS Throughput

The recommended executor core count is **4–5 cores per Executor** for HDFS-heavy workloads. Setting too many cores per Executor (e.g., 16) causes:
1. **HDFS client bottleneck** — HDFS client is not designed for very high concurrent thread counts (typically performs well up to 4-5 concurrent readers per client instance)
2. **GC pressure** — 16 concurrent Tasks share one JVM heap; more object churn → more frequent GC → potential GC pause OOM

### 4.8 Skewed Join Mitigations

| Technique | How It Helps |
|-----------|-------------|
| AQE skew join splitting | Auto-splits oversize skewed partitions into smaller chunks |
| Salting | Adds random salt to skewed key; join on composite key distributes load |
| Broadcast hint | If small table fits in memory, use BroadcastHashJoin — avoids shuffle entirely |
| More shuffle partitions | Minor relief; doesn't fix single-key skew |
| `repartition(n, joinKey)` | **Concentrates** skewed key — typically makes it **worse** |

---

## Topic 5 — Structured Streaming (Q81–Q90)

### 5.1 Trigger Modes

| Trigger | Code | Behaviour |
|---------|------|-----------|
| Processing time | `processingTime='30 seconds'` | New micro-batch every 30s (or after previous completes) |
| Once | `once=True` | All available data in ONE micro-batch, then stop |
| Available now | `availableNow=True` | All available data in multiple micro-batches, then stop (3.3+) |
| Continuous | `continuous='1 second'` | Sub-millisecond experimental; async checkpoint |
| Default (no trigger) | — | New micro-batch as fast as possible |

### 5.2 File Source Rate Control

`.option('maxFilesPerTrigger', 5)` — limits how many **new files** are processed per micro-batch. Useful for controlling ingestion rate from file-based sources (S3, GCS, ADLS, HDFS) to avoid processing bursts.

### 5.3 Stream-Static Join

```python
static_lookup = spark.read.parquet('/lookup')       # static (batch) DF
stream_events = spark.readStream.format('kafka')... # streaming DF

joined = stream_events.join(static_lookup, 'product_id')  # valid!
```

- The static side is **read once per micro-batch** (current snapshot)
- The streaming side drives the micro-batch triggers
- No watermark required on the static side
- The join produces a streaming result

### 5.4 StreamingQuery Monitoring

**`query.status`** — Python dict of the **current state**:
```python
{
  'message': 'Processing new data',
  'isDataAvailable': True,
  'isTriggerActive': True
}
```

**`query.lastProgress`** — Python dict with **metrics from the most recently completed micro-batch**:
```python
{
  'id': 'query-uuid',
  'runId': 'run-uuid',
  'batchId': 42,
  'numInputRows': 5000,
  'inputRowsPerSecond': 250.0,
  'processedRowsPerSecond': 310.0,
  'durationMs': {...}
}
```

### 5.5 Kafka Source Configuration

`.option('startingOffsets', 'earliest')`:
- **First start (no checkpoint)**: reads from offset 0 for each partition
- **Restart with checkpoint**: resumes from the saved checkpoint offset

`.option('startingOffsets', 'latest')`:
- **First start**: begins from the most recent offset (skips historical data)
- **Restart**: resumes from checkpoint

### 5.6 `dropDuplicates` in Streaming

```python
stream_df \
    .withWatermark('event_time', '10 minutes') \
    .dropDuplicates(['event_id', 'event_time'])
```

- **Requires a watermark** so Spark knows when deduplication state for old event IDs can be safely discarded
- Without watermark: state grows **unboundedly** (must remember all seen event IDs forever)
- State for events where `event_time` falls below the watermark is dropped safely

### 5.7 Continuous Processing

`trigger(continuous='1 second')` — experimental low-latency mode:
- Tasks run **continuously** without waiting for a micro-batch trigger
- Checkpoints at the specified interval (not per-batch as in micro-batch mode)
- Supports only a limited set of operations (no stateful aggregations)
- Achieves sub-millisecond latency vs micro-batch's ~100ms minimum

### 5.8 Streaming Sort Limitation

```python
stream_df.orderBy('event_time')  # AnalysisException!
```

Global `orderBy` is **not supported** in Structured Streaming. You cannot globally sort an unbounded stream because there is always the possibility of late-arriving data. `sortWithinPartitions` is technically allowed but doesn't produce a globally ordered stream.

### 5.9 `mapGroupsWithState` and Stateful Processing

**`mapGroupsWithState`** allows arbitrary per-group state management across micro-batches:
- Maintains a user-defined state object per group key
- Available in Python via **`applyInPandasWithState`**
- Must emit **exactly one output row** per group per batch (unlike `flatMapGroupsWithState`)
- State is automatically **restored from checkpoint** on restart
- Watermark is **optional** — state can use timeout policies (processing-time or event-time)

---

## Topic 6 — Spark Connect (Q91–Q95)

### 6.1 Spark Connect Client Session

```python
# Correct: use .remote() with sc:// URI
spark = SparkSession.builder.remote('sc://localhost').getOrCreate()
spark = SparkSession.builder.remote('sc://hostname:15002').getOrCreate()

# With TLS/SSL
spark = SparkSession.builder.remote('sc://hostname:15002/;use_ssl=true').getOrCreate()
```

Note: `.master('sc://...')` does NOT work — the Spark Connect client uses `.remote()`.

### 6.2 Plan Evaluation — Server-Side Analysis

In Spark Connect, transformations (e.g., `df.filter(col('x') > 5)`) build a **local client-side logical plan** but do NOT send it to the server. No analysis occurs client-side.

When an **action** is triggered (`.count()`, `.show()`, `.collect()`):
1. The accumulated logical plan is serialized to Protobuf
2. Sent to the Spark Connect server via gRPC
3. The server analyzes the plan (resolves columns, validates types)
4. Any `AnalysisException` (e.g., missing column) is raised and returned to the client

This is a key difference from classic Spark where analysis happens during plan construction.

### 6.3 Databricks Serverless and Spark Connect

In Databricks Serverless notebooks:
- **Uses Spark Connect** as the underlying protocol between the notebook and the remote Spark cluster
- **No `SparkContext` access** — the RDD API is unavailable
- **No `spark.sparkContext`** — this raises an error
- Notebook process is **isolated from the Spark Driver** (improved reliability)
- Supports **Python, Scala, and SQL** via a single Spark Connect server
- Enables instant cluster provisioning (no JVM startup on the client)

### 6.4 Multi-Language Support via gRPC

Spark Connect exposes a **language-agnostic gRPC API** with a Protocol Buffers schema for the logical plan. Any language with a gRPC client library can implement a Spark Connect client:
- Official clients: Python, Scala, Java (R in progress)
- Community/custom clients: Rust, Go, any gRPC language
- **No local JVM required** — just a gRPC library and the generated Protobuf stubs
- Results returned as **Apache Arrow record batches** (universal columnar format)

---

## Topic 7 — Pandas API on Spark (Q96–Q100)

### 7.1 Merging pyspark.pandas DataFrames

```python
# Both are valid and equivalent
result = ps.merge(left_psdf, right_psdf, on='user_id', how='inner')
result = left_psdf.merge(right_psdf, on='user_id', how='inner')
```

`pyspark.pandas` DataFrame's `.merge()` follows the same API as native pandas, but executes on Spark.

### 7.2 Cross-DataFrame Operations (`ops_on_diff_frames`)

```python
psdf1 = ps.DataFrame({'a': [1, 2, 3]})
psdf2 = ps.DataFrame({'b': [4, 5, 6]})

# This FAILS by default:
result = psdf1['a'] + psdf2['b']  # OperationNotAllowedError

# Enable it:
ps.set_option('compute.ops_on_diff_frames', True)
result = psdf1['a'] + psdf2['b']  # now works (triggers an implicit join)
```

Operations between different `pyspark.pandas` DataFrames require an implicit join. This is disabled by default because implicit joins can be expensive and unintended.

### 7.3 Cloud Storage with `ps.read_csv()`

```python
ps.read_csv('s3://my-bucket/data/file.csv')       # works
ps.read_csv('gs://my-bucket/data/file.csv')       # works
ps.read_csv('abfss://container@account.dfs.core.windows.net/data/file.csv')  # works
```

`pyspark.pandas` delegates file I/O to Spark's distributed file system connector, so all cloud paths supported by Spark work natively. Local path or `s3://` both work.

### 7.4 `ps.get_dummies()` — One-Hot Encoding

```python
psdf_encoded = ps.get_dummies(psdf, columns=['color'])
# → columns: color_red, color_blue, color_green, ...
```

- Creates one boolean column per distinct value (one-hot encoding)
- Result remains a **distributed pyspark.pandas DataFrame** (NOT collected to driver)
- Column naming: `<original_col>_<value>`
- `drop_first=True` drops the first dummy to avoid multicollinearity in modeling

### 7.5 `compute.shortcut_limit`

`pyspark.pandas` has a `compute.shortcut_limit` option (default: 1000):
- If a `pyspark.pandas` DataFrame has **fewer rows than this limit**, Spark eagerly collects and caches the data locally — subsequent operations (like `len()`) are instant
- If the DataFrame has **more rows than the limit**, operations like `len()` trigger a **full distributed Spark job** to count rows

```python
ps.get_option('compute.shortcut_limit')  # 1000 by default
ps.set_option('compute.shortcut_limit', 5000)  # increase threshold
```

This explains why `len(psdf)` is sometimes instant (small DF cached) and sometimes triggers a Spark job (large DF exceeds limit).
