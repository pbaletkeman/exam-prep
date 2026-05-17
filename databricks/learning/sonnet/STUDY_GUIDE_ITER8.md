# Study Guide — Databricks Certified Associate Developer for Apache Spark
## Iteration 8

---

## Exam Overview

| Property | Value |
|---|---|
| Exam | Databricks Certified Associate Developer for Apache Spark |
| Iteration | 8 |
| Total Questions | 100 |
| Time Limit | 90 minutes |
| Pass Score | ≥ 70% (70 correct) |
| Answer Format | All single-select (`one`) |
| Difficulty Split | 9 Easy / 55 Medium / **36 Hard** |

### 🚨 CRITICAL: Answer Distribution

**96 questions have answer B. 4 questions have answer A.**

| Question | Answer | Topic |
|---|---|---|
| Q31 | **A** | `to_utc_timestamp` vs `from_utc_timestamp` (they are inverses — description in A is correct) |
| Q60 | **A** | `na.drop(how="all")` drops rows where ALL columns are null; `how="any"` drops rows where ANY column is null |
| Q71 | **A** | AQE coalesce — answer A correctly describes `coalescePartitions.enabled=true` and advisoryPartitionSizeInBytes |
| Q81 | **A** | `StreamingQueryListener` registered via `spark.streams.addListener()` with three callbacks |

**All other 96 questions: answer B.**

This is the single most important fact to memorize before the exam.

---

## Topic 1: Apache Spark Architecture & Internals (Q1–Q20)

### 1.1 Jobs, Stages, and Tasks (Q1)

- **Action** → triggers a **Job**
- **DAGScheduler** splits job into **Stages** at shuffle boundaries
- **Number of tasks in a stage** = **number of input partitions** (each partition → exactly one task)
- `spark.executor.cores` does NOT determine task count — it determines parallelism within an executor

### 1.2 Unified Memory Model (Q2) — HARD

The unified memory region is bounded by `spark.memory.fraction` (default **0.6**) of JVM heap.

```
JVM Heap
├── Reserved (300 MB or 1.5× classloading)
├── Unified Memory Region (memory.fraction × heap = 0.6 × heap)
│   ├── Storage Memory   (storageFraction × unified = 0.5 × unified)  ← cached data
│   └── Execution Memory (1 − storageFraction × unified)              ← shuffle/sort/join
└── User Memory (1 − memory.fraction = 0.4 × heap)                    ← UDFs, user objects
```

**Key rule**: Execution can evict storage blocks **above** the `storageFraction` watermark. Evicted blocks go to disk (if storage level permits) or are dropped (recomputed on next access). Execution is **dominant over storage** under pressure.

### 1.3 Sort-Based Shuffle File Layout (Q3) — HARD

Default shuffle writes exactly **2 files per mapper task**:
- **1 data file**: all reducer partition data concatenated in sorted order
- **1 index file**: byte offsets for each reducer partition's segment

Total files: `2 × M` instead of `M × R` (old hash shuffle). The index file lets each reducer seek directly to its slice.

### 1.4 TaskContext (Q4) — HARD

Inside a `mapPartitionsWithIndex` or any partition function:
```python
ctx = TaskContext.get()        # returns null on driver
ctx.partitionId()              # 0-based partition index
ctx.attemptNumber()            # 0 = first attempt, 1 = first retry
ctx.stageId()                  # current stage ID
```
`TaskContext` is thread-local and only valid during task execution.

### 1.5 Barrier Execution Mode (Q5) — HARD

`rdd.barrier().mapPartitions(...)` enables barrier mode:
- All tasks in the stage **start simultaneously**
- If any single task fails → **entire stage fails** (not individual task retry)
- Required for deep-learning frameworks (PyTorch DDP, Horovod) where all workers must exchange addresses via `BarrierTaskContext.barrier()` and `allGather()` before training begins

### 1.6 FAIR vs FIFO Scheduler (Q6) — HARD

| Property | FIFO (default) | FAIR |
|---|---|---|
| Behavior | Jobs run one at a time in submission order | Tasks from multiple concurrent jobs interleaved |
| Short job penalty | Short job waits behind long job | Short job completes without waiting |
| Config | Default | `spark.scheduler.mode=FAIR` |
| Use case | Batch processing | Interactive notebooks, multi-tenant |
| Pools | N/A | Configure pools with weights and `minShare` |

### 1.7 Python Worker Reuse (Q7) — HARD

`spark.python.worker.reuse=true` (default):
- Python worker processes are **reused across tasks on the same executor**
- Workers call `recv_task()` in a loop — avoids repeated Python startup + module import
- Heavy imports (pandas, NumPy) amortized across many tasks

When `false`: new Python process spawned per task (clean state, but slow).

**Warning**: With reuse=true, global state mutations persist across tasks within the same worker.

### 1.8 Checkpoint vs Persist (Q8) — HARD

| Property | `rdd.checkpoint()` | `rdd.persist(DISK_ONLY)` |
|---|---|---|
| Lineage | **Truncated** — new base RDD with no parents | **Retained** — full lineage preserved |
| Storage | Fault-tolerant FS (HDFS/S3 via `sc.setCheckpointDir()`) | Executor local disk |
| On executor failure | Data is safe (in HDFS/S3) | Must recompute from lineage |
| Use case | Long iterative lineage (PageRank) | Temporary disk-based caching |
| Extra write pass | Yes (materializes the data) | No extra pass |

### 1.9 Data Locality Degradation (Q9) — HARD

Spark prefers data-local tasks. When preferred node is busy, it waits `spark.locality.wait` (default **3s**) before degrading:

```
PROCESS_LOCAL → NODE_LOCAL → RACK_LOCAL → ANY
     (3s wait)      (3s wait)    (3s wait)
```

Individual overrides: `spark.locality.wait.process`, `.node`, `.rack`

Longer wait = less network I/O, more idle CPU; shorter wait = faster task start but more data transfer.

### 1.10 Tungsten UnsafeRow (Q10) — HARD

`UnsafeRow` is a **binary, off-heap (or on-heap) row format**:
- Fields stored as compact bytes: **null bitset** (fixed-width prefix) + fixed fields + variable-length fields appended
- No Java object boxing → dramatically reduced GC pressure
- Fields accessed via `getLong()`, `getInt()`, `getUTF8String()` (direct memory reads)
- Data can be compared, sorted, hashed **without deserialization**
- Used by SQL physical operators, sort-merge join, aggregate hash maps

### 1.11 Dynamic Allocation vs Fixed Instances (Q11)

When both are set:
```
spark.executor.instances=10
spark.dynamicAllocation.enabled=true
```
→ `spark.executor.instances` is **ignored** (Spark logs a warning)
→ Use `spark.dynamicAllocation.maxExecutors` / `minExecutors` for bounds

### 1.12 maxPartitionBytes (Q12)

`spark.sql.files.maxPartitionBytes` (default **128 MB**):
- Caps data per input partition when scanning files
- Partition count ≈ `ceil(total_bytes / maxPartitionBytes)` (subject to `openCostInBytes`)
- **Reduce** it: more parallelism, fewer memory issues per task
- **Increase** it: fewer tasks, useful for many small files (reduces overhead)

### 1.13 Accumulators — Double-Counting Risk (Q13)

Accumulators updated inside a **transformation** may count higher than expected when:
1. A task **fails and is retried** — failed attempt's increment is NOT rolled back
2. A cached partition is evicted and the transformation is re-executed for a downstream action

**Solution**: Only rely on accumulators updated inside **actions** (not transformations), or use aggregation functions for exact counting.

### 1.14 Broadcast Timeout (Q14)

`spark.sql.broadcastTimeout` (default **300 seconds**):
- Max time driver waits to complete broadcasting a relation to all executors
- Exceeded → `SparkException: Could not execute broadcast in X secs`
- Increase for: large broadcast tables on slow networks, complex nested schemas
- Does NOT fall back to SMJ automatically (job fails)

### 1.15 Config Precedence (Q15)

Lowest to highest:
```
spark-defaults.conf < SparkConf (programmatic) < spark-submit CLI flags
```
CLI `--deploy-mode cluster` overrides `spark.submit.deployMode=client` in defaults.

### 1.16 RDD Compression (Q16)

`spark.rdd.compress=true` (default **false**):
- Compresses serialized RDD partitions in memory (`MEMORY_ONLY_SER`) or on disk
- Uses codec from `spark.io.compression.codec`
- Trade-off: smaller memory/disk footprint ↔ CPU for compress/decompress
- Best when: memory is bottleneck, CPUs underutilized
- For DataFrames: use `spark.sql.inMemoryColumnarStorage.compressed` instead

### 1.17 Driver Max Result Size (Q17)

`spark.driver.maxResultSize` (default **1 GB**):
- Caps total serialized size of results collected to driver from all tasks
- Exceeded → `SparkException: Job aborted ... bigger than spark.driver.maxResultSize`
- Set to `0` to disable (not recommended — driver OOM risk)
- Guard against accidental `df.collect()` on large DataFrames

### 1.18 addFile vs addJar (Q18)

| Method | What it distributes | How workers access |
|---|---|---|
| `sc.addFile(path)` | Arbitrary file (config, model, script) | `SparkFiles.get("filename")` → local path |
| `sc.addJar(path)` | JAR file | Added to **executor classpath** automatically |

Both propagate to all current and future executors (including dynamic allocation additions).

### 1.19 Arrow for toPandas (Q19)

`spark.sql.execution.arrow.pyspark.enabled=true`:
- `df.toPandas()` and `spark.createDataFrame(pandas_df)` use **Apache Arrow columnar IPC**
- Bypasses row-by-row Py4J serialization → **10–100× faster** for large DataFrames
- Constraint: all columns must have Arrow-compatible types; MapType, complex ArrayType may fall back
- Fallback behavior controlled by `spark.sql.execution.arrow.pyspark.fallback.enabled`

### 1.20 Web UI Retention (Q20)

`spark.ui.retainedJobs` / `spark.ui.retainedStages` (both default **1000**):
- Control how many completed job/stage summaries kept in **driver's in-memory Web UI cache**
- FIFO eviction when limit reached
- Prevents unbounded driver heap growth in long-running apps (notebooks, streaming)
- Separate from History Server settings (`spark.history.ui.maxApplications`)

---

## Topic 2: Spark SQL (Q21–Q40)

### 2.1 String Functions

| Function | Behavior | Key Detail |
|---|---|---|
| `regexp_replace(col, pat, repl)` | Replace all matches | Returns **original string** (not null) if no match |
| `overlay(str, repl, pos, len)` | Replace by position (1-based) | No regex; `len` defaults to `length(repl)` |
| `soundex(str)` | 4-char phonetic code (e.g., R163) | Fuzzy name matching; `null` → `null`, empty → empty |
| `initcap(str)` | Title case (first letter of each word upper) | Words split by any non-alpha character |
| `upper(str)` / `lower(str)` | All uppercase / all lowercase | |

### 2.2 Array Functions

| Function | Behavior | Null handling |
|---|---|---|
| `array_distinct(arr)` | Unique elements, first-occurrence order | `null` = distinct value (retained once) |
| `array_union(a1, a2)` | Distinct elements from both | Deduplicates; `null` elements compared equal |
| `array_intersect(a1, a2)` | Distinct elements in both | Deduplicates |
| `array_except(a1, a2)` | Distinct elements in a1 not in a2 | Deduplicates |
| `sequence(start, stop, step)` | Range array (inclusive) | Negative step → descending; wrong direction → empty array |
| `map_from_entries(arr_of_structs)` | Array of 2-field structs → MapType | Duplicate keys: **last value wins** |

### 2.3 Higher-Order Functions (HOFs) — HARD

| HOF | Behavior | Empty array | Null handling |
|---|---|---|---|
| `aggregate(arr, zero, merge, finish)` | **Fold-left**: starts with `zero`, applies `merge(acc, elem)` left-to-right; optional `finish(acc)` post-processes | Returns `zero` (or `finish(zero)`) | `null` array → `null` result |
| `forall(arr, pred)` | `true` if pred holds for ALL elements | **Vacuously `true`** | `null` array → `null` |
| `exists(arr, pred)` | `true` if pred holds for ANY element | Returns **`false`** | `null` array → `null` |
| `zip_with(a1, a2, func)` | Element-wise merge | Result length = **length of longer array**; shorter padded with `null` | Either `null` → `null` result |

**`aggregate` use case**: Computing average by accumulating `(sum, count)` struct as `zero`, then `finish = sum/count`.

**`forall` vs `exists` empty array trap**: `forall([]) = TRUE`, `exists([]) = FALSE`

**`zip_with` length trap**: Unlike Python `zip` (truncates), `zip_with` uses the **longer** array (pads shorter with null).

### 2.4 Timestamp and Date Functions

**Q31 = A — `to_utc_timestamp` vs `from_utc_timestamp` (they are INVERSES):**

| Function | Direction | Example |
|---|---|---|
| `to_utc_timestamp(ts, tz)` | Local time in `tz` → UTC | `to_utc_timestamp('2026-04-25 10:00:00', 'US/Eastern')` → `'2026-04-25 14:00:00'` |
| `from_utc_timestamp(ts, tz)` | UTC → local time in `tz` | `from_utc_timestamp('2026-04-25 14:00:00', 'US/Eastern')` → `'2026-04-25 10:00:00'` |

Both accept IANA timezone strings (`'US/Eastern'`) or UTC offset strings (`'+05:30'`).

| Function | Returns | Behavior on invalid |
|---|---|---|
| `make_date(y, m, d)` | DateType or **null** | Returns **null** for invalid dates (e.g., Feb 30) — no exception |
| `make_timestamp(y,m,d,h,min,sec,tz)` | TimestampType or **null** | Same null-on-invalid convention |
| `datediff(end, start)` | IntegerType (calendar days) | Negative when end < start |
| `timestampdiff('DAY', start, end)` | IntegerType (truncated, any unit) | Spark 3.3+; use for sub-day or larger-than-day units |

### 2.5 Error-Tolerant Functions (Q35) — HARD

| Function | On Error | Spark Version |
|---|---|---|
| `try_cast(expr AS type)` | Returns **null** instead of throwing | 3.2+ |
| `try_divide(a, b)` | Returns **null** when b=0 (no ArithmeticException) | 3.2+ |

Use the `try_*` family for ETL pipelines with dirty data where individual bad values should become null.

### 2.6 SQL Syntax Features

**UNPIVOT (Q36) — Spark 3.4+ SQL syntax** — HARD:
```sql
SELECT id, quarter, revenue
FROM sales
UNPIVOT (revenue FOR quarter IN (Q1, Q2, Q3, Q4))
```
- Converts wide columns into rows (inverse of PIVOT)
- DataFrame API equivalent: `selectExpr("stack(4, 'Q1', Q1, 'Q2', Q2, 'Q3', Q3, 'Q4', Q4) AS (quarter, revenue)")`

**QUALIFY (Q37) — Spark 3.3+** — HARD:
```sql
SELECT *, row_number() OVER (PARTITION BY dept ORDER BY salary DESC) AS rn
FROM emp
QUALIFY rn = 1
```
- Filters on window function results **without a subquery**
- Evaluated after WHERE, GROUP BY, HAVING, and window computation
- Saves one CTE/subquery layer

**TABLESAMPLE (Q38)**:
- `TABLESAMPLE (10 PERCENT)`: Bernoulli ~10% probability per row (varies per run)
- `TABLESAMPLE (100 ROWS)`: at most 100 rows (like LIMIT but with sampling semantics)
- Neither is reproducible across runs without a fixed seed; use `df.sample(fraction, seed)` for reproducibility

**LATERAL VIEW OUTER (Q39)**:
- `LATERAL VIEW explode(tags)`: drops rows where `tags` is null or empty
- `LATERAL VIEW OUTER explode(tags)`: **preserves** those rows with `tag = null` (SQL equivalent of `explode_outer()`)

**schema_of_json (Q40)**:
```python
sample = '{"id":1,"name":"Alice"}'
schema_str = schema_of_json(sample)  # returns DDL string: 'STRUCT<id: BIGINT, name: STRING>'
df.withColumn("parsed", F.from_json("json_col", schema_str))
```
- Returns a **DDL-format schema string**, not a StructType object
- Accepts a **string literal** only (not a column expression)
- For dynamic per-row schema inference: use `spark.read.json(rdd_of_strings)`

---

## Topic 3: DataFrame / DataSet API (Q41–Q70)

### 3.1 Write Modes and File Layout

**Write modes (Q41)**:
| Mode | Behavior |
|---|---|
| `"overwrite"` | **Deletes entire existing directory** then writes new data |
| `"append"` | Adds new files; existing files untouched |
| `"error"` (default) | Raises exception if path exists |
| `"ignore"` | Skips write silently if path exists |

**partitionBy (Q42)**:
```
output_path/year=2025/month=01/part-00000.parquet
output_path/year=2025/month=02/part-00001.parquet
```
- Hive-style partition directories
- Partition column values encoded in path, **removed from Parquet file contents**
- Enables partition pruning (`WHERE year=2025` skips other directories)

**bucketBy (Q43)**:
- `write.bucketBy(64, "user_id").sortBy("user_id").saveAsTable("t")`
- Writes 64 fixed-bucket files; all rows with same `user_id` → same bucket
- Two tables bucketed by same key + same bucket count → **join skips shuffle entirely**
- Requires `saveAsTable()` (registered in Hive Metastore); `save()` does not enable bucket join optimization

**writeTo V2 API (Q44)**:
- `df.writeTo("catalog.schema.table").append()` uses **DataSource V2**
- Richer operations: `.overwrite(condition)`, `.overwritePartitions()`, `.create()`, `.replace()`, `.createOrReplace()`
- `.overwrite(condition)` = delete matching rows then insert (partial overwrite)
- Respects existing schema and partition layout

**maxRecordsPerFile (Q58)**:
- `df.write.option("maxRecordsPerFile", 100000).parquet(path)`
- Splits a single output partition into multiple files if row count > limit
- Does NOT add shuffle (partition count unchanged; only splits within a task)

### 3.2 DataFrame Statistics and Observation

**observe() (Q45)** — HARD:
- `df.observe("metrics", F.count(F.lit(1)).alias("cnt"), F.mean("val").alias("avg_val"))`
- Metrics computed **in a single pass** alongside the normal action (write, collect)
- Retrieve via `QueryExecutionListener.onSuccess()` → `ObservedMetrics` map
- No extra scan over the data

**freqItems() (Q46)** — HARD:
- `df.stat.freqItems(["col1"], support=0.01)` → approximate heavy hitters
- Uses **Misra-Gries / Space-Saving** algorithm (single pass, no full shuffle)
- Result: `ArrayType` column per input column with frequent item values
- `support` = minimum fraction of rows (default 1%)
- May include false positives; will NOT miss true heavy hitters
- Returns `ArrayType`, not a map

**crosstab() (Q50)**:
- `df.stat.crosstab("col1", "col2")` → contingency table
- col1 distinct values → rows; col2 distinct values → columns; cells = counts
- Bounded by `spark.sql.crossJoin.maxValues` (default 1000) columns

### 3.3 Pandas UDF (Q47) — HARD

| UDF Type | Data passed per call | Serialization |
|---|---|---|
| Standard Python UDF | One Python scalar per row | Row-by-row via Py4J; slow |
| Scalar Pandas UDF | `pandas.Series` per Arrow batch | Arrow columnar batches; **10–100× faster** |

Pandas UDF is called **once per batch** (not once per partition, not once per row).
All columns must have Arrow-compatible types.

### 3.4 Checkpointing

**localCheckpoint() (Q48)**:
- Materializes DataFrame on **executor local disk** (no HDFS required)
- Truncates lineage
- **NOT fault-tolerant**: if executor dies, data is lost (lineage cannot be recomputed)
- Use for iterative algorithms where cheap lineage truncation is more important than fault tolerance

**checkpoint() (regular)**:
- Writes to configured reliable filesystem (HDFS/S3 via `sc.setCheckpointDir()`)
- Fault-tolerant but slower (extra write pass)

### 3.5 Input File Name (Q49)

```python
df = spark.read.csv(directory_path)
df = df.withColumn("source_file", F.input_file_name())
```
- Returns fully qualified path of the source file for each row
- Works for: CSV, JSON, Parquet, ORC, text (file-based sources)
- Empty string for non-file sources (JDBC)
- Evaluated per task

### 3.6 String Operations on DataFrames

**regexp_extract (Q51)**:
- `F.regexp_extract(col, pattern, groupIndex)` → returns the captured group
- **Returns `""` (empty string) when no match** — NOT null
- Returns `null` only when input is null
- `groupIndex=0` → entire match

**split with limit (Q52)**:
- `F.split(str, pattern, limit)` → at most `limit` elements; last element = remaining unsplit string
- `limit=0` (default): splits all, removes trailing empty strings
- `limit=-1`: splits all, **preserves** trailing empty strings
- Matches Java `String.split(regex, limit)` semantics

### 3.7 JSON Parsing and Schema

**from_json permissive behavior (Q53)** — HARD:
- Missing field → `null`
- Extra field in JSON → **silently ignored**
- Malformed JSON → all fields `null` (no exception)
- To capture corrupt records: pass `{"columnNameOfCorruptRecord": "_corrupt"}` in options

**StructType.fromDDL (Q54)** — HARD:
```python
schema = StructType.fromDDL("id BIGINT, name STRING, ts TIMESTAMP")
```
- Parses DDL string → identical `StructType` as programmatic construction
- All fields are **nullable by default** (can't set `nullable=False` via DDL; use programmatic API)
- Useful when schema stored in config files or returned by `schema_of_json()`

### 3.8 Sampling

**randomSplit (Q55)** — HARD:
```python
train, test = df.randomSplit([0.8, 0.2], seed=42)
```
- Splits are **reproducible** with a fixed seed on stable input
- `train` and `test` are lazy; if source is re-scanned separately, a row could theoretically appear in both
- **Solution**: `df.cache()` before `randomSplit` to guarantee exactly one scan

### 3.9 Join Hints and Strategies

**hint("broadcast") (Q56)**:
- Forces broadcast hash join regardless of `autoBroadcastJoinThreshold`
- Overrides threshold but NOT physical memory — too large = OOM
- Other hints: `MERGE` (sort-merge), `SHUFFLE_HASH`, `SHUFFLE_REPLICATE_NL`
- SQL equivalent: `/*+ BROADCAST(t) */`

**Resolving ambiguous join columns (Q61)** — HARD:

After `result = df1.join(df2, df1.id == df2.id, "inner")`, both `id` columns exist:
```python
# WRONG — ambiguous:
result.select("id")
result.select(F.col("id"))

# CORRECT options:
result.select(df1["id"], ...)                  # reference original DataFrame object
df2.withColumnRenamed("id", "id_right")       # rename before joining
df1.join(df2, ["id"])                          # list-of-strings join deduplicates automatically
```

**crossJoin (Q66)** — HARD:
- `df1.crossJoin(df2)` → `M × N` output rows (Cartesian product)
- `spark.sql.crossJoin.enabled=true` by default in Spark 3.x
- No predicates are pushed into cross joins — filter explicitly before/after

### 3.10 Column Operations

**encode/decode (Q57)**:
- `F.encode(str_col, charset)` → StringType → **BinaryType** (using named charset)
- `F.decode(binary_col, charset)` → BinaryType → **StringType** (inverse)
- Supported charsets: `'UTF-8'`, `'UTF-16'`, `'US-ASCII'`, `'ISO-8859-1'`
- NOT base64 (that's `F.base64`/`F.unbase64`); NOT URL encoding

**sortWithinPartitions vs orderBy (Q59)** — HARD:
| Method | Shuffle? | Global order? | Use case |
|---|---|---|---|
| `df.orderBy("col")` | Yes (range shuffle) | **Yes** | Full sorted output |
| `df.sortWithinPartitions("col")` | No | **No** (local only) | Improve Parquet min/max stats without shuffle cost |

**na.drop (Q60) = A** — HARD:
- `df.na.drop(how="all")` → drops rows where **ALL** columns are null
- `df.na.drop(how="any")` → drops rows where **AT LEAST ONE** column is null
- Optional `subset=["col1","col2"]` limits which columns are checked
- `df.na.fill({"col1": 0, "col2": "unknown"})` fills per-column; type must be compatible

**when/otherwise (Q62)**:
- `F.when(cond, val).when(cond2, val2)` with **no `.otherwise()`** → unmatched rows return **`null`**
- Not an error; equivalent to SQL `CASE WHEN ... END` with no `ELSE`

**withColumn overwrite (Q64)**:
- `df.withColumn("price", F.col("price") * 1.1)` silently **overwrites** `price`
- No error, no warning; the old column is replaced
- To keep both: `withColumnRenamed("price", "old_price")` first

**toDF rename (Q65)**:
- `df.toDF("a", "b", "c")` renames all columns in order
- Count mismatch → `AnalysisException: The number of columns doesn't match`

**selectExpr (Q67)** — HARD:
```python
df.selectExpr("*", "price * 0.9 as discounted", "upper(name) as name_upper")
```
- Accepts arbitrary SQL expression strings parsed by Catalyst
- `"*"` expands to all columns
- Equivalent to `df.select(F.expr("..."))` per expression

**dropDuplicates vs distinct (Q68)**:
- `df.distinct()` → removes exact duplicates across **all columns**
- `df.dropDuplicates(["id"])` → removes rows with same `id`, keeping first occurrence; **retains all columns**
- `dropDuplicates()` (no args) ≡ `distinct()`

**F.expr vs F.col (Q69)**:
- `F.expr("col1 + col2")` → parses SQL expression string; preferred for complex SQL (CASE WHEN, window functions, STRUCT literals)
- `F.col("col1") + F.col("col2")` → Python operator overloading; cleaner for simple arithmetic
- Both produce identical physical plans for equivalent expressions

### 3.11 Window Functions

**ROWS vs RANGE (Q70)** — HARD:

| Frame | Boundary | Tie behavior |
|---|---|---|
| `rowsBetween(unboundedPreceding, currentRow)` | By **physical row position** | Strict running total: exactly rows 1..current |
| `rangeBetween(unboundedPreceding, currentRow)` | By **ORDER BY value ≤ current** | Includes all rows with tied ORDER BY values |

For `SUM()` with ties in ORDER BY:
- ROWS → strict running total (different values per tied row)
- RANGE → all tied rows get the same cumulative sum (frame extends to include peers)

RANGE requires ORDER BY on a sortable numeric/date column; for non-unique ORDER BY values it may include more rows than expected.

---

## Topic 4: Troubleshooting & Tuning (Q71–Q80)

### 4.1 AQE Post-Shuffle Coalesce (Q71) — ANSWER IS A — HARD

**Q71 answer is A** (option A correctly states):
- Enabled by `spark.sql.adaptive.coalescePartitions.enabled=true` (**default true** when AQE is enabled)
- After a shuffle, AQE examines actual shuffle output sizes
- Merges **small adjacent** shuffle partitions into fewer larger ones
- Target size: `spark.sql.adaptive.advisoryPartitionSizeInBytes` (default **64 MB**)
- Lower bound: `spark.sql.adaptive.coalescePartitions.minPartitionNum`
- Applies **greedily from left to right** (adjacent only, not arbitrary)

Other AQE features:
- Dynamic join strategy switching: SMJ → BHJ when runtime stats show table is small enough
- Skew join optimization: splits skewed partitions + replicates matching side

### 4.2 storageFraction (Q72) — HARD

`spark.memory.storageFraction` (default **0.5**):
- Fraction of the unified memory region that is **protected from eviction** by execution
- Storage memory **below** this watermark = safe from execution eviction
- Storage **above** this watermark = can be evicted by execution
- Higher value → more cached data protected → execution must spill sooner
- Lower value → execution borrows more freely → less cached data preserved

### 4.3 EXPLAIN CODEGEN (Q73) — HARD

`df.explain("codegen")` or `EXPLAIN CODEGEN SELECT ...`:
- Shows **generated Java source code** for each Whole-Stage Code Generation (WSCG) pipeline
- Fused operators compiled into a single `generate` class (tight loop, no intermediate materializations)
- Pipeline breaks (`!`) indicate operators that do NOT support WSCG:
  - Python UDFs
  - Some SortMergeJoin configurations
  - Some streaming operators
- Distinct from `explain("extended")` which shows 4-level plan text

### 4.4 Skew Join (Q74)

Symptoms: few tasks with vastly higher shuffle read bytes / longer duration in Stage detail.

AQE skew join (enabled by default with AQE):
- Detection: `skewedPartitionFactor` (size > factor × median AND size > `skewedPartitionThresholdInBytes`)
- Fix: splits skewed partition into sub-partitions + **replicates** matching partition from other side
- Does NOT require manual salting by the user

### 4.5 Disable Broadcast Joins (Q75)

`spark.sql.autoBroadcastJoinThreshold=-1` → completely disables auto broadcast
- Prefer SMJ or shuffle hash join for all tables
- `-1` = disable; `0` = disable for all non-trivially-empty tables
- Per-query: `NO_BROADCAST` SQL hint or `df.hint("merge")`

### 4.6 ORC vs Parquet (Q76) — HARD

| Property | ORC | Parquet |
|---|---|---|
| Both | Columnar, splittable, compressed, predicate pushdown, schema evolution | Same |
| Native ACID | Yes (Hive ACID) | No |
| Built-in indexes | Stripe-level stats, bloom filters, row indexes | Row group stats + bloom filters |
| Ecosystem | Hive, legacy pipelines | Arrow, Delta Lake, Iceberg, Databricks, Flink, Presto |
| Complex types | Good | **Better** for deeply nested types (MAP<LIST<STRUCT>>) |
| Choose when | Hive ACID tables, legacy pipelines | Delta Lake, Iceberg, cross-platform, streaming |

Both ORC and Parquet are **columnar** (not one row-based, one columnar — a common misconception).

### 4.7 G1GC for Executors (Q77) — HARD

G1GC is the **recommended** collector for Spark executors:
```
spark.executor.extraJavaOptions=-XX:+UseG1GC -XX:G1HeapRegionSize=16m -XX:InitiatingHeapOccupancyPercent=35 -XX:MaxGCPauseMillis=200
```
- Designed for large heaps (>4 GB)
- Incremental region collection → reduced stop-the-world pauses
- Long GC pauses manifest as heartbeat timeouts (`Lost executor`) or slow task completion
- NOT Serial GC (high overhead), NOT CMS (deprecated in modern JDK), NOT ZGC by default

### 4.8 Columnar Cache Batch Size (Q78)

`spark.sql.inMemoryColumnarStorage.batchSize` (default **10000**):
- Number of rows per columnar batch when caching with `df.cache()` / `MEMORY_AND_DISK`
- Larger batches → better compression (run-length, dictionary) + better vectorized throughput
- Smaller batches → less memory per batch
- Change requires re-caching to take effect

### 4.9 Event Logging (Q79)

`spark.eventLog.enabled=true`:
- Writes all application events (job/stage/task start-end, executor add/remove, metrics) to `spark.eventLog.dir`
- Dir must be on shared/distributed FS (HDFS, S3) for History Server access
- History Server reconstructs completed application UIs from these logs
- Without it: metrics from completed applications are unrecoverable

### 4.10 Shuffle Spill (Q80)

Causes: sort buffer or aggregation hash map exceeds available execution memory → data spills to local disk.

Two Spark UI Stage metrics confirm spill:
1. **`Shuffle Spill (Memory)`** — bytes of in-memory data serialized and written to disk
2. **`Shuffle Spill (Disk)`** — actual compressed bytes written to disk

Reduction strategies: increase executor memory, reduce `spark.sql.shuffle.partitions`, increase `spark.memory.fraction`.

---

## Topic 5: Structured Streaming (Q81–Q90)

### 5.1 StreamingQueryListener (Q81) — ANSWER IS A — HARD

**Q81 answer is A** (option A correctly states):
```python
spark.streams.addListener(myListener)  # myListener extends StreamingQueryListener
```
Three callbacks:
1. `onQueryStarted(event)` — fired when a new streaming query begins
2. `onQueryProgress(event)` — fired at the end of **each micro-batch** with `StreamingQueryProgress` (input rows, rate, batch duration, offsets)
3. `onQueryTerminated(event)` — fired when a query stops (normally or with exception)

Standard way to export streaming metrics to Prometheus/Datadog without polling.

### 5.2 mapGroupsWithState vs flatMapGroupsWithState (Q82) — HARD

| Property | mapGroupsWithState | flatMapGroupsWithState |
|---|---|---|
| Output per group | **Exactly 1** record | **0 or more** records |
| Output modes | Update only | **Update + Append** |
| Timeout call | Function called with empty iterator | Same |
| Use case | Session summary per batch | Sessionisation (emit on close), event patterns |

### 5.3 Kafka failOnDataLoss (Q83) — HARD

`option("failOnDataLoss", "true")` (default):
- Raises `StreamingQueryException` if offsets Spark planned to read are **no longer available** in Kafka
- Causes: short Kafka retention, topic partition deletion

`option("failOnDataLoss", "false")`:
- Skips missing offsets with a warning; continues from next available offset
- Preferred when Kafka retention is aggressive and some data loss is acceptable

### 5.4 Output Modes (Q84)

`outputMode("complete")`:
- Rewrites **entire result table** to sink every micro-batch
- Required for stateful aggregations **without a watermark** (old groups can still be updated)
- Only suitable for small result tables (not file sinks at scale)

`outputMode("append")`:
- Writes only **new rows** since last trigger
- Required for aggregations WITH watermark (rows emitted only after watermark passes)

`outputMode("update")`:
- Writes only **rows that changed** since last trigger

### 5.5 Trigger Types (Q85)

| Trigger | Behavior | Spark Version |
|---|---|---|
| `Trigger.Once()` | All data in **one** micro-batch, then stop | All versions |
| `Trigger.AvailableNow()` | All data in **multiple** rate-limited micro-batches, then stop | Spark 3.3+ |
| `Trigger.ProcessingTime("30 seconds")` | Fixed interval micro-batches, continuous | All versions |
| `Trigger.Continuous("1 second")` | Truly continuous (experimental, limited operators) | Spark 3.x experimental |

`AvailableNow` preferred over `Once` for backfill (avoids single enormous micro-batch).

### 5.6 maxFilesPerTrigger (Q86)

`option("maxFilesPerTrigger", 10)`:
- Limits new files consumed **per micro-batch** for file streaming sources
- Excess files queued for subsequent batches
- Default: no limit (all available files per batch)
- Useful for throttling when files arrive faster than Spark can process

### 5.7 Stream-Static Join (Q87) — HARD

- Streaming side: new rows from source
- Static side: **re-read in full each micro-batch** (unless cached)
- Output mode must be `append`
- Limitation: **late streaming rows that miss a match cannot be recovered** — the static side is not updated retroactively
- No watermark/state maintained for static side
- No `complete` output mode

### 5.8 orderBy Unsupported in Streaming (Q88)

`AnalysisException: Sorting is not supported on streaming DataFrames/Datasets, unless it is on aggregated DataFrame/Dataset in Complete output mode`

Global sort requires seeing all rows first → impossible for infinite stream. Sorting only allowed within a `complete`-mode streaming aggregation.

### 5.9 Continuous Processing (Q89) — HARD

`Trigger.Continuous("1 second")` (experimental):
- Tasks run **continuously without micro-batches**
- Records processed and written record-by-record (not in batches)
- Epoch interval = how often offsets are committed and state checkpointed
- End-to-end latency: **milliseconds** (vs seconds for micro-batch)
- Limitations: stateless `map`-like operations only; Kafka and Rate sources only; checkpointing is asynchronous

### 5.10 Rate Source (Q90)

```python
df = spark.readStream.format("rate").option("rowsPerSecond", 100).load()
```
Output columns: **exactly two**:
- `timestamp` (`TimestampType`) — time the row was generated
- `value` (`LongType`) — monotonically increasing counter starting from 0

Use for: load testing, development without Kafka/files, testing watermarks and stateful operations.

---

## Topic 6: Spark Connect (Q91–Q95)

### 6.1 Architecture (Q91)

Spark Connect introduces **decoupled client-server architecture**:
- Spark driver = **remote gRPC server** (long-lived shared cluster service)
- Language clients (Python, Scala, Java, Go, R) connect over **gRPC/protobuf** on port **15002** (default)
- Client constructs **unresolved logical plan locally** → sends to server for analysis, optimization, execution
- No Spark internals in client process; no local JVM required
- URL scheme: `sc://host:port/`

### 6.2 Client-Side Plan Construction (Q92) — HARD

When `df.filter(F.col("age") > 30)` is called in a Spark Connect client:
1. **Locally**: Creates a `Filter` plan node on top of existing plan tree in client memory — **no network call**
2. When an **action** is triggered (`.show()`, `.collect()`, `.write`):
   - Client serializes the **entire plan as protobuf**
   - Sends to Spark Connect server via gRPC
   - Server analyzes, optimizes, executes, streams results back

No analysis or execution occurs client-side for transformations.

### 6.3 TLS/SSL Configuration (Q93)

Secure connection URL format:
```python
SparkSession.builder.remote("sc://myhost:15002/;use_ssl=true;token=mytoken").getOrCreate()
```
- `use_ssl=true` enables TLS for gRPC channel
- `token=<bearer_token>` for token-based authentication
- Databricks clusters use this with TLS enabled by default

### 6.4 Unavailable APIs in Spark Connect (Q94) — HARD

**NOT available** through Spark Connect client:
- `SparkContext` and all `sc.*` methods
- `sc.parallelize()`, `sc.addFile()`, `sc.addJar()`, `sc.broadcast()` (low-level)
- `sc.setCheckpointDir()`
- All direct **RDD operations** (`rdd.map()`, `rdd.filter()`, etc.)

**Available** through Spark Connect:
- Full DataFrame/Dataset/SQL API
- `spark.sql()`, `spark.read.*`, `spark.write.*`, `df.select()`, `df.groupBy().agg()`
- Scalar UDFs and Pandas UDFs registered via `spark.udf.register()`

### 6.5 Protobuf Versioning (Q95)

Protobuf field numbering provides **forward and backward compatibility**:
- Older clients can send plans to newer servers (unknown fields ignored)
- Newer clients can connect to older servers (missing fields use default values)
- Language clients (Python, Scala, Java) versioned **independently** from Spark server
- Key operational advantage for managed services where server upgrades lag client releases

---

## Topic 7: Pandas API on Spark (Q96–Q100)

### 7.1 Converting to/from Pandas-on-Spark

```python
import pyspark.pandas as ps

# pandas → Pandas-on-Spark (distributed)
psdf = ps.from_pandas(pdf)       # canonical method
psdf = ps.DataFrame(pdf)        # equivalent

# Pandas-on-Spark → native pandas (collects to driver)
pdf = psdf.to_pandas()
```

### 7.2 Cross-DataFrame Operations (Q97)

```python
psdf1 + psdf2  # raises ValueError by default!
```
- Two separately created Pandas-on-Spark DataFrames have different internal index origins
- Operation requires an implicit shuffle join → disabled by default
- Enable: `ps.set_option("compute.ops_on_diff_frames", True)` (be aware of shuffle cost)

### 7.3 get_dummies — One-Hot Encoding (Q98)

```python
ps.get_dummies(psdf, columns=["category"])
```
- Replaces `category` with binary columns: `category_A`, `category_B`, `category_C`
- Original column dropped; cell = 1 if row had that value, 0 otherwise
- `null` values → all-zeros (no `category_nan` column unless `dummy_na=True`)
- Mirrors `pandas.get_dummies` behavior

### 7.4 shortcut_limit (Q99) — HARD

`ps.options.compute.shortcut_limit` (default **1000**):
- When a Pandas-on-Spark DataFrame has fewer rows than this limit, some operations (e.g., notebook repr/display) **collect to driver and use native Pandas** instead of Spark
- Avoids Spark job overhead for trivially small DataFrames
- `0` = disable short-circuit (always use Spark)
- Higher value = more operations use the Pandas fast path

### 7.5 Index Types (Q100) — HARD

| Index Type | IDs | Shuffle Required? | iloc-compatible? |
|---|---|---|---|
| `"sequence"` | Globally **consecutive** integers (0, 1, 2, …) | **YES** (full sort) | Yes |
| `"distributed-sequence"` (default) | Unique but **non-consecutive** (monotonically increasing per partition) | **No** | Unreliable |

Switch index type: `ps.set_option("compute.default_index_type", "sequence")`

Use `"sequence"` when you need pandas-compatible consecutive integer index; accept the shuffle cost.

---

## Hard Question Summary (36 Hard Questions)

| Question | Topic | Key Concept |
|---|---|---|
| Q2 | Architecture | Execution evicts storage above storageFraction watermark |
| Q3 | Architecture | Sort shuffle: 1 data file + 1 index file per mapper |
| Q4 | Architecture | TaskContext.get().partitionId() / attemptNumber() |
| Q5 | Architecture | Barrier mode: all tasks start together; whole stage fails on any task failure |
| Q6 | Architecture | FIFO default; FAIR interleaves concurrent jobs |
| Q7 | Architecture | python.worker.reuse=true reuses workers across tasks |
| Q8 | Architecture | checkpoint() truncates lineage; persist(DISK_ONLY) retains lineage |
| Q9 | Architecture | Locality degradation: PROCESS_LOCAL → NODE_LOCAL → RACK_LOCAL → ANY |
| Q10 | Architecture | UnsafeRow: binary off-heap, no GC, direct memory reads |
| Q27 | SQL | aggregate() fold-left; optional finish() post-processes accumulator |
| Q28 | SQL | forall([]) = true; exists([]) = false |
| Q29 | SQL | zip_with pads shorter array with null (like zip_longest) |
| Q30 | SQL | map_from_entries: array of 2-field structs; duplicate keys: last wins |
| Q35 | SQL | try_cast/try_divide return null instead of throwing |
| Q36 | SQL | UNPIVOT SQL syntax (Spark 3.4+) converts wide columns to rows |
| Q37 | SQL | QUALIFY filters on window function results without subquery (Spark 3.3+) |
| Q45 | DataFrame | observe() computes metrics in single pass alongside action |
| Q46 | DataFrame | freqItems uses Misra-Gries algorithm; support = minimum fraction |
| Q47 | DataFrame | Pandas UDF passes Series per Arrow batch; 10-100× faster |
| Q53 | DataFrame | from_json permissive: missing=null, extra ignored, malformed=all-null |
| Q54 | DataFrame | StructType.fromDDL parses DDL string; all fields nullable by default |
| Q55 | DataFrame | randomSplit reproducible with seed; cache source to avoid double-scan |
| Q59 | DataFrame | sortWithinPartitions = no shuffle; orderBy = global sort with shuffle |
| Q60 | DataFrame | na.drop(how="all") = ALL null; how="any" = ANY null **(Answer A)** |
| Q61 | DataFrame | Resolve ambiguous join columns via df1["id"] or list-of-string join |
| Q66 | DataFrame | crossJoin = Cartesian product M×N rows |
| Q67 | DataFrame | selectExpr accepts SQL expression strings |
| Q70 | DataFrame | ROWS = physical row count; RANGE = includes tied ORDER BY peers |
| Q71 | Tuning | AQE coalesce: merges adjacent small post-shuffle partitions **(Answer A)** |
| Q72 | Tuning | storageFraction: protects storage below watermark from execution eviction |
| Q73 | Tuning | EXPLAIN CODEGEN shows generated Java; ! marks pipeline breaks |
| Q76 | Tuning | ORC = Hive ACID; Parquet = ecosystem standard |
| Q77 | Tuning | G1GC recommended for executor; -XX:+UseG1GC |
| Q81 | Streaming | StreamingQueryListener: 3 callbacks via spark.streams.addListener() **(Answer A)** |
| Q82 | Streaming | mapGroupsWithState = exactly 1 output; flatMapGroupsWithState = 0 or more |
| Q83 | Streaming | failOnDataLoss=true raises on missing Kafka offsets; false skips them |
| Q87 | Streaming | Stream-static join: static re-read each batch; late rows cannot recover |
| Q89 | Streaming | Continuous processing: ms latency; stateless only; Kafka/Rate only |
| Q92 | Connect | Client builds plan locally; sends protobuf on action only |
| Q94 | Connect | SparkContext/RDD APIs unavailable in Connect client |
| Q99 | Pandas | shortcut_limit: short-circuits small DataFrames to local Pandas |
| Q100 | Pandas | sequence index = consecutive (shuffle); distributed-sequence = non-consecutive (no shuffle) |

---

## Iteration 8 vs Prior Iterations — Key Differences

| Property | Iter 7 | **Iter 8** |
|---|---|---|
| Difficulty: Easy | 16 | **9** |
| Difficulty: Medium | 80 | **55** |
| Difficulty: Hard | 4 | **36** |
| All answers same | YES (all B) | **NO: 96×B, 4×A** |
| Non-B answers | None | **Q31=A, Q60=A, Q71=A, Q81=A** |
| HOFs covered | filter, transform, map_filter | **aggregate, forall, exists, zip_with, map_from_entries** |
| Key SQL additions | sentences(), slice() | **QUALIFY, UNPIVOT, try_cast/try_divide, TABLESAMPLE, schema_of_json** |
| Barrier mode | Not covered | **Q5 (Hard)** |
| UnsafeRow/Tungsten | Not covered | **Q10 (Hard)** |
| GC tuning | Not covered | **Q77 (Hard)** |
| StreamingQueryListener | Not covered | **Q81 (Hard, Answer A)** |
| Continuous processing | Not covered | **Q89 (Hard)** |
| Pandas-on-Spark index types | Not covered | **Q100 (Hard)** |

---

## Common Traps — Iteration 8

| Trap | Wrong Assumption | Correct Understanding |
|---|---|---|
| Non-B answers | All answers are B (like Iter 7) | Q31, Q60, Q71, Q81 are **A** |
| Q71 confusion | AQE answer is B | **Q71=A** (AQE coalesce config is in option A) |
| Q81 confusion | Listener answer is B | **Q81=A** (correct listener registration is in option A) |
| zip_with length | Truncates to shorter array (Python zip) | Pads shorter with null (zip_longest behavior) |
| forall/exists empty | Both return null or both return false | forall([])=**true**, exists([])=**false** |
| aggregate finish | Required argument | **Optional** (returns accumulator directly if omitted) |
| regexp_extract no match | Returns null | Returns **empty string `""`** |
| from_json malformed | Raises exception | Returns struct with **all fields null** |
| StructType.fromDDL nullable | Can set nullable=False via DDL | **All fields nullable=True**; use programmatic API for non-nullable |
| randomSplit guarantees | No overlap guaranteed | Possible overlap if source re-scanned; **cache first** |
| checkpoint vs localCheckpoint | Both fault-tolerant | `localCheckpoint` = **NOT fault-tolerant** |
| storageFraction | Absolute heap limit for storage | Fraction of **unified region** protected from eviction |
| ORC vs Parquet | ORC = row-based | **Both are columnar** |
| G1GC vs default | ZGC is Spark default | **G1GC is recommended**; must be explicitly set |
| Continuous trigger | Another name for micro-batch | **Truly continuous** — no micro-batches; millisecond latency |
| stream-static join | Can recover late rows | **Cannot** — late streaming rows that miss are gone |
| `outputMode("complete")` | Always best for aggregations | Only for **small result tables** without watermark |
| to_utc_timestamp | Converts UTC→local | Converts **local→UTC** (from_utc_timestamp does UTC→local) |
| QUALIFY | Synonym for HAVING | Filters on **window function results** (HAVING = aggregate results) |
| ps.shortcut_limit | Limits distributed computation | Short-circuits small DataFrames to **local Pandas** |
| distributed-sequence index | Consecutive integers | **Non-consecutive** (only unique per partition; no shuffle) |
