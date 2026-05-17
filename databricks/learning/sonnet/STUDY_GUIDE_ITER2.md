# Databricks Certified Associate Developer for Apache Spark — Study Guide (Iteration 2)

**Edition**: Iteration 2 (100 Questions)
**Generated**: 2026-05-17
**Difficulty Split**: 20 Easy / 60 Medium / 20 Hard
**Answer Types**: 81 single-answer / 19 multi-answer

---

## Table of Contents

1. [Topic 1 — Apache Spark Architecture & Internals](#topic-1--apache-spark-architecture--internals)
2. [Topic 2 — Spark SQL](#topic-2--spark-sql)
3. [Topic 3 — DataFrame API](#topic-3--dataframe-api)
4. [Topic 4 — Troubleshooting & Tuning](#topic-4--troubleshooting--tuning)
5. [Topic 5 — Structured Streaming](#topic-5--structured-streaming)
6. [Topic 6 — Spark Connect](#topic-6--spark-connect)
7. [Topic 7 — Pandas API on Spark](#topic-7--pandas-api-on-spark)

---

## Topic 1 — Apache Spark Architecture & Internals

### 1.1 Cluster Managers and Master URLs

Spark supports three cluster managers:

| Cluster Manager | Master URL Pattern | Default Port |
|----------------|-------------------|-------------|
| Standalone | `spark://hostname:7077` | **7077** |
| YARN | `yarn` | N/A |
| Kubernetes | `k8s://https://host:port` | N/A |
| Local (dev) | `local`, `local[N]`, `local[*]` | N/A |

**Local mode URL variants:**
- `local` — single thread, no parallelism
- `local[2]` — 2 threads
- `local[*]` — **all available logical CPU cores** as worker threads (same JVM)
- `local[*,3]` — all cores, retry 3 times on failure

**Standalone ports to remember:**
- `7077` — master URI (for spark-submit or SparkSession)
- `8080` — Standalone master web UI
- `4040` — Spark application web UI (per running app)
- `18080` — History Server web UI

---

### 1.2 Deploy Modes: Client vs Cluster

Controlled by `--deploy-mode` in `spark-submit`.

| Aspect | Client Mode | Cluster Mode |
|--------|-------------|-------------|
| Driver location | Submitting machine | Worker node inside cluster |
| Default for spark-submit | **Yes** | No |
| Databricks default | No | **Yes** (Driver runs in cluster) |
| If submitting machine crashes | **Job fails** (Driver dies) | Job continues (Driver on cluster) |
| Log location | Local stdout of submitting machine | Worker node logs |
| Use case | Interactive dev, debugging | Production jobs |

**Critical Exam Pattern — Client Mode Risk:**
If the submitting machine (e.g., CI server, laptop) is killed in client mode, the Driver process is killed, and the entire Spark application fails. Spark has no mechanism to migrate or restart the Driver automatically.

---

### 1.3 Accumulators

An **Accumulator** is a distributed shared variable that:
- Can only have values **added** by Tasks (associative + commutative operations)
- Can only be **read by the Driver** (final value after action completes)
- Tasks reading an accumulator inside a UDF or `foreachPartition()` get back the **initial value** (e.g., `0`) — not the globally accumulated total

```python
counter = spark.sparkContext.accumulator(0)

def count_errors(row):
    if row['status'] == 'ERROR':
        counter.add(1)  # Tasks can add
    return row

df.foreach(count_errors)
print(counter.value)   # Driver reads final value after action
```

**Trap:** If you read `counter.value` inside the UDF/lambda, you get `0` (the initial value), not the running total. Only the Driver sees the final accumulated value.

---

### 1.4 Broadcast Variables

**Creating and accessing:**
```python
lookup = spark.sparkContext.broadcast({'A': 1, 'B': 2, 'C': 3})

# Access inside a UDF or transformation
def map_func(row):
    return lookup.value['A']   # .value unwraps the wrapper
```

**Key facts:**
- Serialized once and **cached on each Executor node** (not re-sent per Task)
- **Immutable** — Tasks cannot modify the broadcast; changes do not propagate back to the Driver
- If an Executor fails, the broadcast is **automatically re-sent** to the replacement Executor
- Created via `spark.sparkContext.broadcast(value)`
- Accessed via `.value` attribute
- Explicitly destroyed via `.destroy()` (they do not auto-expire after an action)

---

### 1.5 Configuration Properties

| Property | Default | Controls |
|----------|---------|---------|
| `spark.sql.shuffle.partitions` | 200 | Partitions after DataFrame/SQL shuffle (groupBy, join) |
| `spark.default.parallelism` | Depends on cluster | Default partitions for **RDD** operations (reduceByKey, join on RDDs) |
| `spark.sql.files.maxPartitionBytes` | 128 MB | Target max bytes per input partition when reading files |
| `spark.sql.autoBroadcastJoinThreshold` | 10 MB | Table size below which Spark auto-broadcasts in a join |
| `spark.executor.memoryOverhead` | `executorMemory * 0.1`, min 384 MB | Off-heap memory per Executor |
| `spark.memory.fraction` | 0.6 | Fraction of JVM heap allocated to Spark Memory |
| `spark.dynamicAllocation.enabled` | false | Enable Dynamic Resource Allocation |
| `spark.speculation` | false | Enable speculative execution |
| `spark.executor.cores` | 1 (YARN), all (Standalone) | Cores per Executor |

**Critical Distinction:** `spark.default.parallelism` applies to **RDD** operations. `spark.sql.shuffle.partitions` applies to **DataFrame and SQL** operations. They are independent settings.

---

### 1.6 Input Partitioning

When Spark reads a large file from HDFS:
- One partition per HDFS block approximately
- Target max partition size controlled by `spark.sql.files.maxPartitionBytes` (default 128 MB)
- Result: a 1 GB file with 128 MB blocks → ~8 partitions

This is NOT the same as `spark.sql.shuffle.partitions` (200), which only applies after a shuffle.

---

### 1.7 Speculative Execution

Enabled via `spark.speculation = true`.

**What it does:**
1. Detects "straggler" Tasks that run significantly slower than others in the same Stage
2. Launches **duplicate copies** of those slow Tasks on other Executor slots
3. Whichever copy finishes first — its result is used
4. The remaining running copies are cancelled

**What it does NOT do:**
- It does NOT pipeline stages (run next Stage before current finishes)
- It does NOT pre-compute transformations eagerly
- It does NOT pre-fetch shuffle data

---

### 1.8 TaskScheduler vs DAGScheduler

| Component | Responsibility |
|-----------|---------------|
| DAGScheduler | Converts user's DataFrame operations into a logical DAG; detects shuffle boundaries; splits plan into Stages |
| TaskScheduler | Sends individual **Tasks** within a ready Stage to available Executor slots on worker nodes |
| Cluster Manager | Allocates CPU/memory containers (YARN ResourceManager, Kubernetes API server, Standalone Master) |

---

### 1.9 Executor Memory Model

**Total Executor memory breakdown:**

```
Total Container Memory
├── JVM Heap (spark.executor.memory)
│   ├── Spark Memory (spark.memory.fraction × heap = default 60%)
│   │   ├── Execution Memory — shuffle buffers, sort buffers, hash join maps
│   │   └── Storage Memory — cached DataFrames, broadcast variables
│   └── User Memory (remaining 40%) — Python dicts, non-Spark data structures
└── Off-Heap / Overhead (spark.executor.memoryOverhead)
    — OS overhead, Python worker processes, native libraries
```

**Example:** 10 GB heap, `spark.memory.fraction = 0.6`:
- Spark Memory = 10 × 0.6 = **6 GB** (split between Execution and Storage)
- User Memory = 10 × 0.4 = 4 GB

**`spark.executor.memoryOverhead`:**
- Lives **outside** the JVM heap
- Used for OS overhead, Python workers (PySpark UDFs), native C/C++ libraries
- Default: `max(executorMemory × 0.1, 384 MB)`
- If PySpark UDFs use a lot of memory, increase this

---

### 1.10 Storage Levels

| Storage Level | Description | When Used |
|--------------|-------------|-----------|
| `MEMORY_AND_DISK` | Memory first; spill to disk if full | **Default for `df.cache()`** |
| `MEMORY_ONLY` | Memory only; **drops** partitions if full (no spill) | Default for RDD `.cache()` |
| `MEMORY_ONLY_SER` | Serialized binary in memory; drops if full | Compact footprint; slower reads |
| `DISK_ONLY` | Disk only | Very large datasets |
| `MEMORY_AND_DISK_SER` | Serialized in memory; spills serialized to disk | Best of both SER variants |

**`MEMORY_ONLY` vs `MEMORY_ONLY_SER`:**
- `MEMORY_ONLY`: stores deserialized Java/Python objects — **fast reads, large heap**
- `MEMORY_ONLY_SER`: stores compact binary — **smaller heap, must deserialize on each read**
- `MEMORY_ONLY` drops partitions that don't fit; `MEMORY_AND_DISK` spills them

---

### 1.11 Dynamic Resource Allocation (DRA)

Enabled with `spark.dynamicAllocation.enabled = true`.

**What DRA does:**
- Automatically **adds Executors** when Tasks are queued and more capacity is needed
- Automatically **removes idle Executors** after a configurable timeout (returns resources to cluster)
- Requires an **external shuffle service** so shuffle files remain accessible after Executors are removed
- Works on YARN, Standalone, and Kubernetes (not limited to one)

---

### 1.12 Stage Count Analysis

```python
df = spark.read.parquet('/data/logs')           # Stage 1 starts: scan
counted = df.groupBy('level').count()            # Stage 1: scan + partial agg
                                                  # shuffle boundary → Stage 2: reduce-side agg
sorted_df = counted.orderBy(col('count').desc()) # shuffle boundary → Stage 3: sort + write
sorted_df.write.parquet('/output')
```

Approximate stage count: **3 stages**
- Stage 1: FileScan + partial aggregation (map-side)
- Stage 2: Final aggregation (reduce-side) + sort exchange
- Stage 3: Sort merge + write

Each shuffle (groupBy, orderBy) introduces a Stage boundary.

---

### 1.13 Actions vs Transformations (Key Exam List)

**Actions** (trigger a Spark Job):
`count()`, `show()`, `collect()`, `take()`, `first()`, `write.*`, `foreach()`, `toPandas()`

**Transformations** (lazy; extend logical plan only):
`filter()`, `select()`, `groupBy()`, `agg()`, `join()`, `withColumn()`, `orderBy()`, `distinct()`, `map()`, `flatMap()`

---

## Topic 2 — Spark SQL

### 2.1 Temp View Lifecycle and Scope

| View Type | Scope | Creation | Removal |
|-----------|-------|----------|---------|
| Session temp view | Single SparkSession | `createOrReplaceTempView()` | Session ends or `dropTempView()` |
| Global temp view | All sessions in same app | `createOrReplaceGlobalTempView()` | App ends or `dropGlobalTempView()` |

**Key Catalog methods:**
- `spark.catalog.dropTempView('name')` — remove session-scoped view
- `spark.catalog.dropGlobalTempView('name')` — remove global view
- `createGlobalTempView('name')` raises `AnalysisException` if name already exists (does NOT replace)
- `createOrReplaceGlobalTempView('name')` is the safe upsert form

---

### 2.2 Key Functions from Topic 2

#### Null-Safe and Conditional

| Function | Description | Result Type |
|----------|-------------|-------------|
| `F.coalesce(c1, c2, c3)` | First non-null value | Same as inputs |
| `F.nullif(c, value)` | Returns null if c == value, else c | Same as input |
| `F.when(cond, val).otherwise(else_val)` | Conditional expression | Depends |
| `F.when(cond, val)` (no otherwise) | Returns **null** when condition is false | Nullable |

#### Type Conversion and Literal

| Function | Description |
|----------|-------------|
| `F.lit(value)` | Creates a Column for a constant scalar value |
| `col('x').cast('double')` | Cast column to a type |
| `F.to_json(col)` | Serialize struct/map/array to JSON **StringType** |
| `F.from_json(col, schema)` | Parse JSON string to struct |

#### String Functions

| Function | Description | Return Type |
|----------|-------------|-------------|
| `F.split(col, pattern)` | Split string into parts | `ArrayType(StringType)` |
| `F.concat_ws(sep, *cols)` | Concatenate with separator; **skips nulls** | `StringType` |
| `F.regexp_replace(col, pattern, replacement)` | Regex substitution | `StringType` |
| `F.trim(col)` | Remove leading/trailing whitespace | `StringType` |

**`concat_ws` null behaviour:** When applied to an array containing null elements, `null` elements are silently **skipped**. `['hello', None, 'world']` with separator `'-'` → `'hello-world'`.

#### Date and Time Functions

| Function | Description | Return Type |
|----------|-------------|-------------|
| `F.date_add(col, days)` | Add N days to a date | `DateType` |
| `F.date_sub(col, days)` | Subtract N days | `DateType` |
| `F.datediff(end, start)` | Days between two dates | `IntegerType` |
| `F.date_format(col, fmt)` | Format date as string | `StringType` |
| `F.current_timestamp()` | Current timestamp (eval once at query start) | `TimestampType` |
| `F.current_date()` | Current date | `DateType` |

**`F.current_timestamp()` important:** Evaluated **once at query planning time**, not per-row. Every row in the result gets the same timestamp value.

**`F.date_format` pattern examples:**
- `'yyyy-MM-dd'` → `'2024-03-15'`
- `'yyyy-MM'` → `'2024-03'`
- `'HH:mm:ss'` → `'14:30:00'`

#### Array and Struct Functions

| Function | Description |
|----------|-------------|
| `F.explode(col)` | One row per array/map element; **drops** null/empty array rows |
| `F.explode_outer(col)` | Like explode but **preserves** null/empty rows (outputs null) |
| `F.posexplode(col)` | Like explode but also returns integer position index |
| `F.array_contains(col, value)` | Boolean: does array contain value? |
| `F.size(col)` | Number of elements in array/map |
| `F.to_json(col)` | Serialize struct to JSON string |

**`explode` vs `explode_outer`:**
```python
# Source DataFrame:
# id=1, tags=['a','b']
# id=2, tags=None

df.select('id', F.explode('tags'))
# Result: id=1 'a', id=1 'b'   (row 2 dropped because tags is null)

df.select('id', F.explode_outer('tags'))
# Result: id=1 'a', id=1 'b', id=2 null   (null row preserved)
```

#### Statistical Functions

| Function | Description |
|----------|-------------|
| `F.approx_count_distinct(col, rsd)` | HyperLogLog approximate distinct count |
| `F.count(col)` | Exact count (null-excluding) |
| `F.count('*')` | Row count (null-inclusive) |
| `F.countDistinct(col)` | Exact distinct count (expensive on large sets) |

**`approx_count_distinct`:** Uses the **HyperLogLog** probabilistic algorithm. Much faster than `countDistinct` on large datasets. Second parameter `rsd` is maximum relative standard deviation (default 0.05 = 5% error).

---

### 2.3 SQL Conditional Expressions

Valid in `selectExpr()` and `F.expr()`:

```sql
-- CASE WHEN (always valid)
CASE WHEN score > 80 THEN 'high' WHEN score > 50 THEN 'medium' ELSE 'low' END AS grade

-- IF() (Spark SQL dialect)
IF(score > 80, 'high', IF(score > 50, 'medium', 'low')) AS grade

-- NULLIF() (returns null if equal to second arg)
NULLIF(score, 0) AS adjusted_score
```

**Not valid in Spark SQL:**
- `IIF()` — SQL Server only
- `SWITCH()` — does not exist in Spark SQL

---

### 2.4 Window Functions

#### Ranking Functions Comparison

| Function | Formula | Range | Ties Behaviour |
|----------|---------|-------|---------------|
| `row_number()` | Sequential 1,2,3... | `[1, N]` | Arbitrary ordering of ties |
| `rank()` | Position with gaps | `[1, N]` | Ties share lowest rank; gaps after tie group |
| `dense_rank()` | Position without gaps | `[1, distinct_count]` | Ties share rank; no gaps |
| `percent_rank()` | `(rank − 1) / (N − 1)` | `[0.0, 1.0]` | Minimum is exactly 0 |
| `cume_dist()` | `rank / N` | `(0, 1]` | Minimum is `1/N`, never 0 |
| `ntile(k)` | Bucket 1 to k | `[1, k]` | Extra rows fill **earlier** tiles |

**`percent_rank` vs `cume_dist`:**
- `percent_rank`: can produce 0.0 (first row always 0)
- `cume_dist`: minimum is `1/N`, never 0; always ends at 1.0

**`ntile` with uneven split:** For `ntile(3)` on 10 rows:
- 10 ÷ 3 = 3 remainder 1
- **Tile 1 gets 4 rows**, tiles 2 and 3 each get 3 rows
- Extra rows always fill **earlier** tiles first

**`lead()` and `lag()` boundary behaviour:**
- `lag(col, 1)` on the **first row** → `null` (no prior row)
- `lead(col, 1)` on the **last row** → `null` (no following row)
- A default value can be provided: `F.lead('col', 1, 0).over(w)` returns `0` instead of `null`

---

### 2.5 Window Frame Specifications

Valid frame specs:
```python
# Cumulative: unbounded start to current row
Window.partitionBy('dept').orderBy('salary').rowsBetween(Window.unboundedPreceding, Window.currentRow)

# Numeric range: ±100 units from current value
Window.orderBy('value').rangeBetween(-100, 100)

# Current row to end of partition
Window.partitionBy('dept').rowsBetween(Window.currentRow, Window.unboundedFollowing)

# Entire partition (sum of all)
Window.partitionBy('dept').rowsBetween(Window.unboundedPreceding, Window.unboundedFollowing)
```

**Invalid:** `rowsBetween(Window.currentRow, -1)` — end boundary is before start boundary.

**Sharing a Window spec:**
```python
w = Window.partitionBy('dept').orderBy('salary')
df.withColumn('rank', F.rank().over(w)) \
  .withColumn('dense_rank', F.dense_rank().over(w)) \
  .withColumn('running_total', F.sum('salary').over(w))
```
Each `.withColumn()` computes independently. Spark's optimizer **may** consolidate same-spec windows into one pass, but this is not guaranteed. It does not raise an error.

---

### 2.6 GROUPING SETS, ROLLUP, CUBE

| Construct | Produces |
|-----------|---------|
| `GROUPING SETS ((), (region))` | Grand total row (empty grouping) + region subtotals |
| `ROLLUP(a, b)` | All combinations: (a,b), (a), () |
| `CUBE(a, b)` | All 4 combinations: (a,b), (a), (b), () |

**GROUPING SETS rules:**
- Computes multiple grouping combinations in **a single query pass**
- Non-active grouping columns appear as `null` in the result
- Has native SQL syntax — not limited to `rollup()` DataFrame API

---

### 2.7 Join Types Reference

| Join Type | Returns |
|-----------|---------|
| `inner` | Rows matching in both |
| `left` / `left_outer` | All left rows + matched right (null if no match) |
| `right` / `right_outer` | All right rows + matched left (null if no match) |
| `full` / `full_outer` | All rows from both; null where no match |
| `left_semi` | Left rows that **have** a match in right; **no right columns** |
| `left_anti` | Left rows that **have no** match in right; no right columns |
| `cross` | Cartesian product (every × every) |

**CROSS JOIN size:** 100 rows × 50 rows = **5,000 rows**

---

### 2.8 Catalyst Optimiser

When both predicate pushdown and projection pushdown apply:
```python
df = spark.read.parquet('/data/events')
result = df.filter(col('year') == 2024) \
           .select('event_id', 'event_type') \
           .filter(col('event_type') == 'click')
```
Catalyst produces: **FileScan with both filters pushed down + only required columns read**. The physical execution is not the user's code order — it's the optimised plan.

---

## Topic 3 — DataFrame API

### 3.1 Column Reference Methods

```python
df['column_name']           # Dict-style access
df.column_name              # Attribute-style
col('column_name')          # pyspark.sql.functions.col
F.col('column_name')        # Same via alias
```

---

### 3.2 Key DataFrame Methods

#### Creation

```python
spark.range(0, 10)          # Schema: single column "id" of LongType
spark.read.text('/file')    # Schema: single column "value" of StringType (one row per line)
spark.createDataFrame(data, schema)
df.toDF('col1', 'col2', 'col3')   # Rename ALL columns by position
```

**`spark.range()` schema:** Column is named `id` (not `index`), type is `LongType` (not `IntegerType`).

**`spark.read.text()` schema:** Single column named `value` of `StringType`.

**`toDF(*names)`:** Renames all columns by position. If column count doesn't match, raises an error.

#### Column Operations

```python
df.drop('column_name')               # Remove a column; returns new DF
df.withColumn('new_col', expr)       # Add or replace column
df.withColumnRenamed('old', 'new')   # Rename column
col('amount_str').cast('double')     # Cast (not F.cast(); not .asDouble())
```

**`drop()`:** Use `df.drop('col')`. `df.remove()` and `df.delete()` do not exist.

**`cast()` syntax:** `col('x').cast('double')` — the cast is a method on the Column object, not a standalone function.

#### Null Handling

```python
df.fillna({'col1': 0, 'col2': 'unknown'})   # Fill nulls per column
df.dropna(subset=['email'])                  # Drop rows where email is null
col('email').isNull()
col('email').isNotNull()
~col('email').isNull()    # Equivalent to isNotNull()
```

**Filtering not-null — valid approaches:**
- `df.filter(col('email').isNotNull())` ✓
- `df.filter(~col('email').isNull())` ✓
- `df.na.drop(subset=['email'])` ✓
- `df.filter(col('email') != None)` ✗ (Python None comparison doesn't work correctly in Spark)

#### `when().otherwise()` Chain

```python
# Correct chaining
F.when(col('score') > 80, 'high') \
 .when(col('score') > 50, 'medium') \
 .otherwise('low')

# when() without otherwise → null for non-matching rows (no error)
F.when(col('score') > 90, 'A')  # returns null for score=75
```

---

### 3.3 Sorting and Deduplication

```python
df.orderBy('salary')                 # WIDE (global sort; causes full shuffle)
df.orderBy(col('salary').desc())     # Descending global sort
df.sortWithinPartitions('salary')    # NARROW (sorts each partition independently; no shuffle)

df.distinct()                        # Remove duplicate rows (all columns must match)
df.dropDuplicates(['user_id'])       # Remove rows with duplicate user_id values
```

**`sortWithinPartitions` vs `orderBy`:**
- `sortWithinPartitions`: sorts rows **within each partition only**; no shuffle; output not globally ordered
- `orderBy`: global sort; requires full shuffle to collect all rows in order; produces globally sorted result

---

### 3.4 Joins

#### Default Join Type
`df1.join(df2, on='id')` with no `how` parameter → **`'inner'`**

#### Join Syntax Variants

```python
# By common column name (deduplicates join key in result)
df1.join(df2, 'user_id', 'inner')
df1.join(df2, ['user_id', 'event_date'], 'inner')

# By condition (keeps both columns — can cause ambiguity)
df1.join(df2, df1.id == df2.id, 'inner')

# Cross join
df1.crossJoin(df2)   # Cartesian product; every row1 × every row2
```

#### Ambiguous Column Reference After Join

```python
result = df_orders.join(df_customers, df_orders.id == df_customers.id, 'inner')
result.select('id').show()  # RAISES AnalysisException — 'id' is ambiguous!
```

When joining on a condition (not a column name string), **both DataFrames contribute their `id` column** to the result. Referencing `'id'` is ambiguous. Fix:
```python
result.select(df_orders['id']).show()    # Reference explicitly
# OR: join on string key to auto-deduplicate
df_orders.join(df_customers, 'id', 'inner').select('id').show()  # OK
```

---

### 3.5 Combining DataFrames

| Method | Behaviour |
|--------|-----------|
| `union(other)` | Combines by **position** — column order must match or results are wrong |
| `unionByName(other)` | Combines by **column name** — order doesn't matter |
| `unionByName(other, allowMissingColumns=True)` | Fills missing columns with `null` |

**`unionByName` vs `union` trap:**
- `union()` silently produces wrong results if columns are in different order
- `unionByName()` raises `AnalysisException` if column count/names differ (unless `allowMissingColumns=True`)
- Neither method removes duplicates (use `.distinct()` after if needed)

---

### 3.6 Array and Map Operations

```python
F.array_contains(col('skills'), 'Python')   # Boolean: is 'Python' in skills array?
F.explode(col('items'))                      # One row per array element
F.explode_outer(col('items'))               # Like explode; preserves null/empty rows
F.posexplode(col('items'))                  # Returns (pos, element) pairs

# Correct syntax — NOT:
col('skills').contains('Python')  # This is a string substring check, not array check
F.isin(col('skills'), 'Python')   # isin() is for scalars, not arrays
```

---

### 3.7 Read and Write

#### Reading

```python
# CSV
spark.read.option('header', True).option('inferSchema', True).csv('/data')

# JSON — multi-line option required for pretty-printed JSON
spark.read.option('multiline', True).json('/data')

# Parquet (schema is embedded; most efficient)
spark.read.parquet('/data')

# Text — one row per line, single column 'value' of StringType
spark.read.text('/data/file.txt')
```

#### Write Modes

| Mode | Behaviour |
|------|-----------|
| `'overwrite'` | Delete existing data; write new data |
| `'append'` | Add new data; **preserve** existing |
| `'ignore'` | Do nothing if path exists; **preserve** existing |
| `'error'` / `'errorIfExists'` | **Raise error** if path exists; **preserve** existing |

**Modes that preserve existing data:** `append`, `ignore`, `error` (all three preserve; only `overwrite` deletes)

---

### 3.8 Schema and Types

#### Schema Definition

```python
from pyspark.sql.types import StructType, StructField, StringType, IntegerType

schema = StructType([
    StructField('id', IntegerType(), nullable=False),
    StructField('name', StringType(), nullable=True)
])

# DDL string alternative
schema = 'id INT NOT NULL, name STRING'
```

#### Schema Evolution — mergeSchema

When writing two batches with different schemas to the same Parquet directory:
```python
# Batch 1: id, name
# Batch 2: id, name, email   (new column added)

# Default read — may only return common columns or raise an error
spark.read.parquet('/data/')

# Correct approach — merge all schemas
spark.read.option('mergeSchema', True).parquet('/data/')
# OR: spark.conf.set('spark.sql.parquet.mergeSchema', 'true')
```
The `email` column appears as `null` for rows from batch 1 (before the column was added).

---

### 3.9 Useful Utility Functions

| Function | Description | Note |
|----------|-------------|------|
| `F.monotonically_increasing_id()` | Globally unique, monotonically increasing ID | **Not sequential** — gaps exist between partitions |
| `F.first(col).over(w)` | First value in window | Returns first row's value per window orderBy |
| `F.lag(col, n).over(w)` | Previous Nth value | Returns **null** for first N rows |
| `F.lead(col, n).over(w)` | Next Nth value | Returns **null** for last N rows |

**`monotonically_increasing_id()`:** Guarantees uniqueness and monotonic increase across partitions but is **not sequential** — there are intentional gaps between partition ranges. Do not use when you need 0,1,2,3... sequence.

---

### 3.10 GroupBy Aggregation Result Schema

```python
result = df.groupBy('region', 'category').agg(
    F.count('*').alias('total_orders'),
    F.sum('revenue').alias('total_revenue'),
    F.avg('discount').alias('avg_discount')
)
```

**Facts about this result:**
- `groupBy` key columns (`region`, `category`) appear first
- Aggregate columns appear in the order specified in `agg()`
- Result has exactly **5 columns**: region, category, total_orders, total_revenue, avg_discount
- `count('*')` returns `LongType` (not `IntegerType`)
- `groupBy().agg(F.count('*'))` and `groupBy().count()` differ slightly in column naming but semantically equivalent

---

### 3.11 Pandas UDF vs Python UDF

| Aspect | Python UDF | Pandas UDF (Vectorised) |
|--------|------------|------------------------|
| Decorator | `@F.udf(returnType)` | `@F.pandas_udf(returnType)` |
| Data transfer | Per-row serialization/deserialization between JVM and Python | Columnar batches via **Apache Arrow** |
| Performance | Slow (row-by-row JVM↔Python roundtrip) | **Much faster** (Arrow avoids per-row overhead) |
| Input type | Single row values | `pandas.Series` |
| Null handling | Must handle None explicitly | Pandas NaN/None conventions apply |

**Why Pandas UDFs are faster:** The JVM transfers data as Arrow record batches — entire column chunks move in a single serialisation step instead of row-by-row. This avoids the bottleneck of individual Python pickle serialisation per row.

---

### 3.12 Partition Pruning

When a DataFrame was written with `.partitionBy('country')`, directory structure is:
```
/data/events/country=US/
/data/events/country=UK/
/data/events/country=DE/
```

Reading with a filter:
```python
df.filter(col('country') == 'US').count()
```

Spark applies **partition pruning** — reads only `/data/events/country=US/`, skipping all other directories. This is a major I/O optimization.

---

## Topic 4 — Troubleshooting & Tuning

### 4.1 Cache Lifecycle

```python
df.cache()        # Registers intent — NOT immediately materialised
df.count()        # Action — THIS triggers materialisation in Executor memory
df.unpersist()    # Removes cached blocks from Executor memory and disk
```

**Key exam point:** `cache()` is lazy — it only materialises during the **next action** that triggers execution. Calling `cache()` alone has no immediate effect.

**`unpersist()`:**
- Removes cached blocks from Executor memory **and** disk
- Frees storage capacity for other data
- Does NOT delete underlying source files

---

### 4.2 Storage Level Decision Guide

| Situation | Recommended Level |
|-----------|------------------|
| Dataset fits comfortably in memory | `MEMORY_ONLY` (fast) |
| Dataset may not fit; can't recompute | `MEMORY_AND_DISK` (default cache) |
| Memory-constrained; recompute is OK | `MEMORY_ONLY` (drops partitions) |
| Need compact footprint; tolerate slower reads | `MEMORY_ONLY_SER` |

**MEMORY_ONLY behaviour:** When a partition doesn't fit, it is **dropped** (not spilled). The next access **recomputes** it from lineage. This is fast if recomputation is cheap; dangerous if it's expensive.

**MEMORY_AND_DISK:** Spills to disk instead of dropping. The default for `df.cache()` on DataFrames.

---

### 4.3 Memory Tuning

**`spark.memory.fraction` (default 0.6):**
- Controls what fraction of JVM heap is Spark Memory
- `heap_gb × 0.6` = Spark Memory (shared between Execution and Storage)
- Example: 10 GB heap × 0.6 = **6 GB Spark Memory**

**OOM: GC overhead limit exceeded on Executors:**
- Root cause: too much data per Task, insufficient heap, too many concurrent Tasks
- Fixes: increase `spark.executor.memory`, reduce `spark.executor.cores` (fewer concurrent Tasks), increase `spark.sql.shuffle.partitions` (smaller per-partition data)

---

### 4.4 Sorting

```python
df.sortWithinPartitions('col')   # No shuffle; local sort only
df.orderBy('col')                # WIDE transformation; full shuffle for global sort
```

`sortWithinPartitions` use case: pre-sort data within partitions before writing (e.g., for local merge performance) without incurring the cost of a global sort.

---

### 4.5 Salting for Skew Mitigation

When one join key value dominates (e.g., 80% of rows have `country='US'`):

**Salting steps:**
1. Add a random salt integer (0 to N-1) to the **large/skewed** DataFrame's join key
2. Replicate each row of the **small** DataFrame N times with salt values 0 to N-1
3. Join on the **composite key** (original key + salt value)
4. This distributes the skewed key across N partitions

```python
import pyspark.sql.functions as F
N = 10

# Step 1: Salt the large DataFrame
large_salted = large_df.withColumn('salt', (F.rand() * N).cast('int')) \
    .withColumn('join_key_salted', F.concat('join_key', F.lit('_'), 'salt'))

# Step 2: Replicate the small DataFrame N times
small_replicated = small_df.withColumn('salt', F.explode(F.array([F.lit(i) for i in range(N)]))) \
    .withColumn('join_key_salted', F.concat('join_key', F.lit('_'), 'salt'))

# Step 3: Join on composite key
result = large_salted.join(small_replicated, 'join_key_salted', 'inner')
```

---

### 4.6 Executor Cores Tuning

**Best practice:** `spark.executor.cores` = **4 or 5 cores per Executor**

**Why not 1?** Each Executor has JVM startup overhead; too many Executors waste resources.

**Why not 32 (all cluster cores)?** A single Executor with many cores suffers from:
- HDFS client throughput degradation (HDFS recommends ≤5 connections per client)
- High GC pressure (large heap + many objects)
- Reduced fault isolation

---

### 4.7 Log Level Control

```python
spark.sparkContext.setLogLevel('ERROR')   # Suppress INFO and WARN; show only ERROR
```

Note: `spark.conf.set('spark.log.level', 'ERROR')` is not the correct API for runtime log level control in PySpark.

---

## Topic 5 — Structured Streaming

### 5.1 Starting a Streaming Query

```python
query = df.writeStream \
    .format('console') \
    .outputMode('append') \
    .option('checkpointLocation', '/chk') \
    .start()

type(query)  # StreamingQuery — NOT a DataFrame, NOT None, NOT a Future
```

**`writeStream.start()` returns a `StreamingQuery`** object. This handle allows:
- `query.awaitTermination()` — block until query stops
- `query.stop()` — programmatically stop the query
- `query.status` — check current status
- `query.recentProgress` — recent micro-batch metrics

**`awaitTermination()` is required:** If the main thread exits without calling it, the streaming query terminates because streaming runs in a background thread of the Python driver process.

---

### 5.2 Sources and Sinks

#### Production Sources

| Source | Characteristics |
|--------|----------------|
| Kafka | Fault-tolerant; offsets tracked; replay supported; recommended for production |
| Delta Lake | Transaction log provides replay; schema enforcement; exactly-once compatible |
| Auto Loader (Databricks) | File-based; incremental; handles schema evolution |

#### Development Sources

| Source | Schema | Limitation |
|--------|--------|-----------|
| `rate` | `timestamp TIMESTAMP, value BIGINT` | Synthetic data only |
| `socket` | `value STRING` | Not fault-tolerant; no replay; not for production |

**`rate` source schema:** Two columns: `timestamp` (TimestampType) + `value` (BIGINT counter).

**Socket source limitations:**
- Data received during downtime is **lost** — no offset tracking, no replay
- Only text/string data
- No fault tolerance
- Single host:port only

---

### 5.3 Output Modes

| Mode | Condition for Use | Behaviour |
|------|------------------|-----------|
| `append` | Stateless queries; watermarked aggregations | Only new finalized rows are output |
| `update` | Any query | Only changed rows since last trigger |
| `complete` | **Stateful aggregations required** | Full aggregation result on every trigger |

**`complete` mode use case:** Streaming queries with `groupBy().count()` or similar — the full updated aggregate table is rewritten on each trigger. Appropriate when consumers need to see the complete current state.

**Append mode + aggregation:** Requires a watermark to bound the aggregation state. Without watermark, Spark doesn't know when aggregations are final, so `append` mode is not allowed.

---

### 5.4 Triggers

| Trigger | Behaviour |
|---------|-----------|
| `trigger(processingTime='10 seconds')` | Micro-batch every 10 seconds |
| `trigger(once=True)` | Process all available data in **one micro-batch**, then stop |
| `trigger(availableNow=True)` | Process all available data in **multiple micro-batches**, then stop |
| `trigger(continuous='1 second')` | Experimental continuous processing mode |

**`availableNow` vs `once`:**
- `once=True` → single large micro-batch (one commit)
- `availableNow=True` → multiple micro-batches respecting rate limits and watermarks (Spark 3.3+)
- `availableNow` is preferred because it avoids memory pressure from loading all data at once

---

### 5.5 Watermarks and Late Data

```python
df.withWatermark('event_time', '10 minutes') \
  .groupBy(F.window('event_time', '5 minutes')) \
  .count()
```

**Watermark cutoff:** `max_seen_event_time − watermark_delay`

**Example:** max seen = `12:15`, delay = `10 minutes` → cutoff = `12:05`
- Event with `event_time = 12:07` → `12:07 ≥ 12:05` → **included**
- Event with `event_time = 12:00` → `12:00 < 12:05` → **dropped as late**

---

### 5.6 foreachBatch

```python
def process_batch(batch_df, batch_id):
    batch_df.write.format('delta').mode('append').save('/delta/table')
    batch_df.write.format('kafka').option('topic', 'output').save()

query = streaming_df.writeStream.foreachBatch(process_batch).start()
```

**Why use `foreachBatch`:**
- Write the same micro-batch to **multiple output sinks**
- Apply full batch DataFrame API operations (including joins to static data)
- Implement custom sink logic

**Limitations:** Does not automatically enforce exactly-once; checkpointing still required for at-least-once.

---

### 5.7 Memory Sink

```python
query = streaming_df.writeStream \
    .format('memory') \
    .queryName('my_results') \
    .outputMode('complete') \
    .start()

# Query the in-memory table by queryName
spark.sql("SELECT * FROM my_results").show()
```

The `queryName` option defines the SQL table name for querying the in-memory accumulation.

---

### 5.8 Delta Lake as Streaming Source

```python
# Reading a Delta table as a streaming source
spark.readStream.format('delta').load('/delta/table')
```

**Delta Lake streaming advantages:**
- Transaction log enables replay from any **version or timestamp**
- Exactly-once semantics with checkpointing
- Schema enforcement — incompatible schema changes fail the stream
- Can simultaneously be a source (one query) and a sink (another query)

---

## Topic 6 — Spark Connect

### 6.1 Architecture Comparison

| Aspect | Classic Spark | Spark Connect |
|--------|--------------|---------------|
| Client-Driver communication | **Py4J** socket bridge (JVM embedded in application) | **gRPC over HTTP/2** (logical plans as Protobuf) |
| Driver location | Inside application process | On the **cluster** (separate from client) |
| Client crash impact | Kills Driver → job fails | Driver survives; job continues; client can reconnect |
| RDD API available to client | Yes | **No** — only DataFrame/SQL API |
| Connection URL | `spark://host:port` | `sc://host:port` |
| Default gRPC port | N/A | **15002** |
| Result format to client | Python objects via Py4J | **Apache Arrow record batches** |

---

### 6.2 Ports to Remember

| Service | Port |
|---------|------|
| Standalone master URI | 7077 |
| Spark UI | 4040 |
| Spark Connect gRPC | **15002** |
| Standalone master web UI | 8080 |
| History Server | 18080 |

---

### 6.3 Spark Connect Key Properties

**Language support:** Any language with a gRPC client library — Go, Rust, Java, Python, Scala, etc.

**No local JVM required:** The client library uses gRPC; the JVM runs on the cluster server.

**Results as Arrow:** Query results are streamed to the client as Apache Arrow record batches — efficient columnar binary format.

**Multi-client:** Multiple clients can connect to the same Spark Connect server simultaneously.

**Version compatibility:** Spark Connect supports version negotiation — a 3.4 client can interoperate with a 3.5 server. Teams can upgrade server and client independently (minor version compatibility).

---

### 6.4 Spark Connect Limitations

- `SparkContext` is **not available** on the client (no RDD API)
- Low-level JVM operations not supported
- `spark.sparkContext.broadcast()` and other `SparkContext` methods unavailable from client
- Configuration changes must be made server-side or through Session configurations

---

## Topic 7 — Pandas API on Spark

### 7.1 Module and Import

```python
import pyspark.pandas as ps    # Current recommended import (Spark 3.2+)
# import databricks.koalas as ks  # DEPRECATED legacy import
```

**Koalas history:** The Koalas project (by Databricks) implemented the pandas API on Spark. It was **merged into PySpark core in Spark 3.2** as `pyspark.pandas`. The `databricks.koalas` import still works in Databricks Runtime but is **deprecated** — use `pyspark.pandas`.

---

### 7.2 Conversion Functions

| From | To | Method |
|------|----|--------|
| Native pandas DataFrame | `pyspark.pandas` DataFrame | `ps.from_pandas(pdf)` |
| `pyspark.pandas` DataFrame | PySpark (distributed) DataFrame | `psdf.to_spark()` |
| PySpark DataFrame | `pyspark.pandas` DataFrame | `sdf.pandas_api()` |
| `pyspark.pandas` DataFrame | Native pandas DataFrame | `psdf.to_pandas()` |

**`to_spark()` returns:** A **PySpark DataFrame** (distributed; no data collected to driver).

**`to_pandas()` warning:** Collects **all data** to the driver — dangerous on large DataFrames.

**`ps.from_pandas(pdf)`:** The correct way to convert a native pandas DataFrame to `pyspark.pandas`. Not `pdf.to_spark()` (that doesn't exist on a native pandas DF).

---

### 7.3 Index Types

| Index Type | Behaviour | Performance |
|-----------|-----------|-------------|
| `'distributed'` | Non-unique integers; partition ID-based | Fastest |
| `'distributed-sequence'` | Globally unique; partition ID + row offset (no full shuffle) | **Default**; fast |
| `'sequence'` | Strictly sequential 0,1,2,3... with no gaps | **Expensive** — requires global sort (full shuffle) |

**`distributed-sequence` (default):**
- Globally unique integer index without a global sort
- Uses partition ID and row offset within each partition
- Not strictly sequential (gaps between partitions)
- Much cheaper than `'sequence'`

**`sequence` index performance penalty:**
- Generates strictly sequential index (0,1,2,3...)
- Requires a **global sort** (full shuffle) across all partitions to assign sequential IDs
- Very expensive at scale — use only when a downstream library strictly requires it

---

### 7.4 Differences from Native Pandas

| Behaviour | Native pandas | Pandas API on Spark |
|-----------|--------------|-------------------|
| Row order | Deterministic | **Not guaranteed** |
| Index | Sequential by default | `distributed-sequence` by default |
| Collection to driver | Always in memory | Only on explicit `to_pandas()` |
| Scale | Single machine | Distributed (Spark cluster) |
| Operations | Eager | Lazy (Spark execution model) |
