# Practice Strategy — Databricks Spark Exam (Iteration 6)

**Source**: `spark-databricks-iteration-6.md` · 100 questions · Pass ≥ 70%

---

## What Makes Iteration 6 Different

| Feature | Iter 4/5 | Iter 6 |
|---------|----------|--------|
| Answer types | `one` / `many` | `one` / `many` / **`all`** / **`none`** |
| `all` questions | 0 | 5 (e.g., Q4 — all 4 options correct) |
| `none` questions | 0 | 2 (no option is correct) |
| B-answer rate | ~55% | ~73% |
| New Spark 3.4+ functions | Few | Many: `try_add`, `array_insert`, `try_element_at`, `F.median`, `df.to()` |
| Safe arithmetic coverage | Minimal | Full coverage (`try_add/subtract/multiply/divide`) |
| Spark Connect coverage | Basic | Comprehensive (Q91–Q95) |

---

## 4-Week Study Plan

### Week 1 — Architecture + SQL (Q1–Q40)

**Goal**: Master the 40 lowest-variable questions (behavior is deterministic, well-documented).

| Day | Focus | Tasks |
|-----|-------|-------|
| Mon | Architecture core | Read STUDY_GUIDE_ITER6 §Topic 1 (all 18 sections) |
| Tue | Architecture details | Flashcards: storage levels, locality wait, deploy modes, supervise |
| Wed | SQL functions | Read STUDY_GUIDE_ITER6 §Topic 2; write out return types from memory |
| Thu | SQL drills | Practice Test A (Architecture & SQL questions below) |
| Fri | SQL edge cases | Drill: cardinality vs size, ANSI CAST, try_* functions |
| Sat | Q1–Q20 timed | Do Q1–Q20 in ≤ 18 minutes; score yourself |
| Sun | Q21–Q40 timed | Do Q21–Q40 in ≤ 18 minutes; score yourself |

**Week 1 Targets**: ≥ 17/20 Architecture · ≥ 17/20 SQL

---

### Week 2 — DataFrame API (Q41–Q70)

**Goal**: Master the largest topic (30% of exam). Emphasis on HOFs and Spark 3.x additions.

| Day | Focus | Tasks |
|-----|-------|-------|
| Mon | Struct + sampling | `withField`, `dropFields`, `sampleBy`, `checkpoint`, `df.to()` |
| Tue | HOF — arrays | `aggregate`, `zip_with`, `forall`, `exists`, `flatten`, `array_insert` |
| Wed | HOF — maps | `transform_keys`, `transform_values`, `map_zip_with`, `try_element_at` |
| Thu | Write operations | `partitionBy`, `bucketBy`, `writeTo`, compression codecs |
| Fri | Mixed DataFrame | `observe`, `tail`, `dtypes`, `inputFiles`, `median`, `overlay` |
| Sat | Q41–Q55 timed | 15 questions in 13 minutes |
| Sun | Q56–Q70 timed | 15 questions in 13 minutes |

**Week 2 Target**: ≥ 25/30 DataFrame

---

### Week 3 — Tuning + Streaming + Connect + Pandas API (Q71–Q100)

**Goal**: Clean up remaining 30 questions across 4 topics.

| Day | Focus | Tasks |
|-----|-------|-------|
| Mon | Tuning | AQE skew/coalesce, codegen, off-heap, openCostInBytes |
| Tue | Troubleshooting | Arrow selfDestruct, shuffle buffer, Kryo, missing files |
| Wed | Streaming core | Triggers, file schema, watermark, console sink, Kafka schema |
| Thu | Streaming stateful | `session_window`, `mapGroupsWithState`, `kafka.group.id` |
| Fri | Connect + Pandas API | AnalysisException timing, UDF pickling, NULL vs NaN, index types |
| Sat | Q71–Q90 timed | 20 questions in 18 minutes |
| Sun | Q91–Q100 timed | 10 questions in 9 minutes |

**Week 3 Targets**: ≥ 8/10 Troubleshooting · ≥ 8/10 Streaming · ≥ 5/5 Connect · ≥ 4/5 Pandas API

---

### Week 4 — Full Exam Practice & Weak Area Remediation

| Day | Activity |
|-----|----------|
| Mon | Full 100-question mock (90 min) using answer key; score by topic |
| Tue | Remediate any topic scoring < 75%; re-read relevant sections |
| Wed | Practice Test B (below) + trap-focused drills |
| Thu | Practice Test C (below) + all/none type question drills |
| Fri | QUICK_REFERENCE_ITER6 review; review all non-B answers |
| Sat | Light review only; no new material |
| Sun | Exam |

---

## Practice Test A — Architecture & SQL (40 Questions)

### Part 1: Architecture (20 Q)

**A1.** Which statement correctly describes the default storage level difference between `RDD.cache()` and `DataFrame.cache()`?
- A) Both use `MEMORY_AND_DISK`
- B) `RDD.cache()` uses `MEMORY_ONLY`; `DataFrame.cache()` uses `MEMORY_AND_DISK`
- C) Both use `MEMORY_ONLY`
- D) `RDD.cache()` uses `MEMORY_AND_DISK`; `DataFrame.cache()` uses `MEMORY_ONLY`

**Answer: B**

---

**A2.** `spark.locality.wait.node=10s` is set. What does this control?
- A) How long a task waits before downgrading from `PROCESS_LOCAL` to `NODE_LOCAL`
- B) How long a task waits before downgrading from `NODE_LOCAL` to `RACK_LOCAL`
- C) The total locality wait across all levels
- D) The wait before a task is killed for exceeding node timeout

**Answer: B**

---

**A3.** When `spark.dynamicAllocation.shuffleTracking.enabled=true`, what can Spark DRA do?
- A) Remove any executor regardless of held shuffle data
- B) Only remove executors whose shuffle data is no longer needed downstream
- C) Automatically create an external shuffle service
- D) Reset shuffle files on idle executors

**Answer: B**

---

**A4.** `coalesce(200)` is called on a DataFrame with 100 partitions. What happens?
- A) DataFrame is repartitioned to 200 partitions via a full shuffle
- B) No operation occurs; coalesce cannot increase partition count
- C) An `IllegalArgumentException` is raised
- D) The number is rounded down to 100

**Answer: B**

---

**A5.** Which statement about `spark.driver.supervise` is CORRECT?
- A) Restarts the driver on any task failure
- B) Restarts the driver on non-zero exit; only works in cluster deploy mode; supported in Standalone but NOT YARN or Kubernetes
- C) Works with YARN, Kubernetes, and Standalone cluster modes
- D) Prevents driver OOM by restarting the JVM

**Answer: B**

---

**A6.** After an executor running map tasks crashes post-shuffle write, what happens by default?
- A) Spark fetches shuffle data from other executors
- B) Spark re-runs the map tasks on surviving executors to regenerate shuffle files
- C) The stage is skipped; only reduce tasks run on available data
- D) The application is aborted

**Answer: B**

---

**A7.** In Spark Standalone mode, which statement correctly describes the Worker daemon?
- A) The Worker daemon is the same process as the executor
- B) The Worker daemon is a persistent JVM that launches separate Executor JVMs per application; multiple Executors from different apps can run under one Worker
- C) One Worker process corresponds to exactly one Executor at a time
- D) The Worker daemon runs the DAGScheduler

**Answer: B**

---

**A8.** `spark.executor.pyspark.memory` is NOT set. What is the risk?
- A) Python UDFs are disabled
- B) Python worker memory is unbounded by Spark; the executor container may be killed by YARN or Kubernetes for exceeding the declared memory limit
- C) Arrow-based Pandas UDFs cannot run
- D) Spark raises `ConfigurationException` at session start

**Answer: B**

---

**A9.** `sc.parallelize(data)` without specifying `numSlices`. How many partitions?
- A) Always 2 (minimum)
- B) `spark.default.parallelism`
- C) 1
- D) Number of cores on the driver

**Answer: B**

---

**A10.** Which property does `spark.storage.replication.proactive=true` enable?
- A) Replication of shuffle files to external shuffle service
- B) Proactive replenishment of lost block replicas from surviving executors before cache misses occur
- C) Automatic doubling of replication factor for all cached data
- D) HDFS mirroring for off-heap data

**Answer: B**

---

**A11.** In Barrier execution mode, what happens if one task fails?
- A) Only the failed task is retried
- B) The entire barrier stage is resubmitted from the beginning
- C) The failed task is skipped
- D) The application checkpoints state and retries from the checkpoint

**Answer: B**

---

**A12.** `spark.eventLog.compress=true` and `spark.eventLog.compression.codec` are relevant to:
- A) Compressing serialized RDD partitions in memory
- B) Compressing event log files written to `spark.eventLog.dir`; History Server decompresses transparently
- C) Compressing shuffle output files
- D) Compressing Parquet files at rest

**Answer: B**

---

**A13.** What does DAGScheduler do vs TaskScheduler? Select all that apply.
- A) DAGScheduler splits RDD lineage into stages at shuffle boundaries and submits TaskSets
- B) TaskScheduler assigns tasks to executors by data locality and retries failures
- C) DAGScheduler handles executor heartbeats
- D) Both components share responsibility for Barrier synchronization

**Answer: A, B**

---

**A14.** Which statement about `spark.rdd.compress` is correct?
- A) Compresses shuffle output files
- B) Compresses serialized RDD partitions stored in memory; codec = `spark.io.compression.codec`
- C) Compresses event log files
- D) Compresses broadcast variables

**Answer: B**

---

**A15.** Application IDs in YARN have what format?
- A) `app_<uuid4>`
- B) `application_<rm-start-timestamp>_<sequence-number>`
- C) `spark_<appname>_<timestamp>`
- D) `yarn_<cluster-name>_<sequential-id>`

**Answer: B**

---

**A16.** `coalesce(1)` vs `repartition(1)` — which is more efficient for reducing to a single output file and why?
- A) `coalesce(1)` — narrow transformation, no full shuffle; moves data to one partition without redistributing all partitions
- B) `repartition(1)` — full shuffle means better data distribution
- C) They are identical in performance
- D) `repartition(1)` is faster because it uses parallel sort

**Answer: A**

---

**A17.** The two-level hash map for aggregation helps because:
- A) It avoids spilling to disk entirely
- B) Level 1 is a compact cache-friendly map; Level 2 handles overflow — together reducing object allocation and improving CPU cache hit rates
- C) It allows aggregating across network partitions without shuffle
- D) It replaces the TaskScheduler for aggregation tasks

**Answer: B**

---

**A18.** FIFO vs FAIR scheduler: a short job submitted while a long job runs. Under FAIR:
- A) The short job must wait for the long job to finish
- B) Slots are distributed across both jobs; the short job makes progress concurrently
- C) The short job preempts the long job immediately
- D) A new pool is created for the short job with dedicated resources

**Answer: B**

---

**A19.** In client deploy mode, what happens when the `spark-submit` process is killed?
- A) Only the application is killed; the driver continues on the cluster
- B) The driver is killed immediately since spark-submit IS the driver in client mode
- C) Spark checkpoints state and restarts automatically
- D) YARN restarts the driver on a cluster node

**Answer: B**

---

**A20.** `spark.sql.execution.arrow.maxRecordsPerBatch=1000` (vs default 10000). Effect?
- A) Arrow is disabled for Pandas UDFs
- B) Smaller batches: less memory pressure per round trip but more serialization overhead
- C) Only 1000 rows per DataFrame are processed
- D) The batch size is always rounded up to the next power of 2

**Answer: B**

---

### Part 2: SQL (20 Q)

**B1.** `split_part('apple:banana:cherry', ':', 3)` returns:
- A) `'apple'`
- B) `'cherry'`
- C) `['cherry']`
- D) `null`

**Answer: B**

---

**B2.** `try_divide(numerator, 0)` returns:
- A) `Infinity`
- B) `NULL`
- C) `ArithmeticException`
- D) `0`

**Answer: B**

---

**B3.** `any_value(score IGNORE NULLS)` when all values in the group are NULL returns:
- A) `0`
- B) `NULL`
- C) First non-null value found earlier in the DataFrame
- D) `AnalysisException`

**Answer: B**

---

**B4.** `make_date(2026, 13, 1)` (month=13, invalid) returns:
- A) `DateType` clamped to December 31
- B) `NULL`
- C) `DateTimeException`
- D) `2026-01-01` (month wraps to January)

**Answer: B**

---

**B5.** `regexp_like('hello world', 'world')` returns what type?
- A) `StringType` (`'world'` if match, `''` if no match)
- B) `BooleanType` (`true`)
- C) `IntegerType` (1 or 0)
- D) `ArrayType` (all matches)

**Answer: B**

---

**B6.** `width_bucket(95.0, 0.0, 100.0, 10)` returns:
- A) `9`
- B) `10`
- C) `11` (95 ≥ 100 not true; it's just below max)
- D) `9.5`

**Answer: B** *(95.0 falls in bucket 10 out of 10; each bucket = 10 units wide; bucket 10 = 90–100)*

---

**B7.** `bool_and(flag)` over a group containing `[true, NULL, true]` returns:
- A) `NULL` because NULL is present
- B) `true` — NULLs are ignored
- C) `false` — any NULL makes bool_and false
- D) `AnalysisException` — NULL not allowed in bool_and

**Answer: B**

---

**B8.** `bit_or([6, 3])`: what is 6 OR 3 in binary? (`110 | 011`)
- A) `5` (`101`)
- B) `7` (`111`)
- C) `2` (`010`)
- D) `9`

**Answer: B**

---

**B9.** `array_compact(array(1, NULL, NULL, 3, 2))` returns:
- A) `[1, 2, 3]` (sorted)
- B) `[1, 3, 2]` (order preserved, NULLs removed)
- C) `[1, NULL, NULL, 3, 2]` (unchanged)
- D) `[1, 3]` (removes both NULLs and last duplicate)

**Answer: B**

---

**B10.** `startswith('Databricks', NULL)` returns:
- A) `false`
- B) `NULL`
- C) `true` (empty prefix always matches)
- D) `AnalysisException`

**Answer: B**

---

**B11.** `unix_date(current_date())` returns what type and what value?
- A) `LongType` seconds since epoch
- B) `IntegerType` days since 1970-01-01
- C) `TimestampType`
- D) `StringType` ISO date

**Answer: B**

---

**B12.** `schema_of_csv('"Alice",30,true')` returns what type?
- A) `StructType` object
- B) `StringType` DDL string (e.g., `'_c0 STRING, _c1 INT, _c2 BOOLEAN'`)
- C) `MapType` of field names to types
- D) `ArrayType(StringType)`

**Answer: B**

---

**B13.** `cardinality(NULL)` returns:
- A) `-1`
- B) `NULL`
- C) `0`
- D) `AnalysisException`

**Answer: B**

---

**B14.** `size(NULL)` with default settings returns:
- A) `NULL`
- B) `-1`
- C) `0`
- D) `AnalysisException`

**Answer: B**

---

**B15.** `from_csv(col, 'name STRING, scores ARRAY<INT>')` — what happens?
- A) Parses successfully; scores column becomes an array
- B) Fails or ignores the nested type — `from_csv` supports flat schemas only
- C) Automatically converts to `from_json` for the nested portion
- D) Returns `NULL` for the nested field

**Answer: B**

---

**B16.** `regexp_count('Spark SQL Spark', 'Spark')` returns:
- A) `1`
- B) `2`
- C) `3`
- D) `0`

**Answer: B**

---

**B17.** `try_add(2147483647, 1)` (Integer.MAX_VALUE + 1) with ANSI mode OFF returns:
- A) `-2147483648` (wraps to Integer.MIN_VALUE)
- B) `NULL`
- C) `ArithmeticException`
- D) `2147483647` (clamps to max)

**Answer: B**

---

**B18.** With `spark.sql.ansi.enabled=true`, `SELECT CAST('xyz' AS INT)` returns:
- A) `NULL`
- B) Raises `SparkNumberFormatException`
- C) Returns `0`
- D) Raises `AnalysisException` at planning time

**Answer: B**

---

**B19.** `date_from_unix_date(0)` returns:
- A) `NULL`
- B) `1970-01-01` as `DateType`
- C) `0` as `IntegerType`
- D) `1970-01-01T00:00:00Z` as `TimestampType`

**Answer: B**

---

**B20.** `inline(array(struct(1, 'a'), struct(2, 'b')))` used in `SELECT`:
- A) Raises `AnalysisException` — inline can only be used with `LATERAL VIEW`
- B) Explodes the array: produces 2 rows with each struct's fields as separate columns
- C) Returns a single row containing the original array
- D) Returns only the first element

**Answer: B**

---

## Practice Test B — DataFrame API (30 Questions)

**C1.** `df.sampleBy("tier", fractions={"gold": 0.5, "silver": 0.2})` on a DataFrame with tiers gold, silver, bronze. What happens to bronze rows?
- A) Bronze is sampled at 50% by default
- B) All bronze rows are excluded from the result
- C) Bronze rows are included but not sampled (all included)
- D) `KeyError` is raised

**Answer: B**

---

**C2.** `df.checkpoint(eager=False)` — when does the checkpoint write occur?
- A) Immediately when `checkpoint()` is called
- B) When the next action is called on the returned DataFrame
- C) At the end of the Spark session
- D) Never — eager=False disables checkpointing

**Answer: B**

---

**C3.** `df.to(target_schema)` where target_schema has a column not in df. What happens?
- A) The missing column is added with NULL values
- B) `AnalysisException` is raised
- C) The column is silently dropped from the target schema
- D) The column is added with a default value of 0

**Answer: B**

---

**C4.** `F.forall(F.col("scores"), lambda x: x >= 60)` for `[80, 90, 59, 70]` returns:
- A) `true` (majority pass)
- B) `false` (59 < 60 means not ALL pass)
- C) `3` (count of passing elements)
- D) `NULL`

**Answer: B**

---

**C5.** `F.aggregate(F.col("nums"), F.lit(1), lambda acc, x: acc * x)` for `[1, 2, 3, 4, 5]` returns:
- A) `15` (sum)
- B) `120` (product: 1×1×2×3×4×5)
- C) `5` (last element)
- D) `AnalysisException` — aggregate requires IntegerType zero

**Answer: B**

---

**C6.** `F.array_insert(F.col("arr"), 1, "first")` for `["a", "b", "c"]` returns:
- A) `["a", "b", "c", "first"]`
- B) `["first", "a", "b", "c"]`
- C) `["first", "b", "c"]` (replaces element 1)
- D) `["a", "first", "b", "c"]`

**Answer: B** *(position 1 inserts before element at position 1)*

---

**C7.** `F.try_element_at(F.col("arr"), 99)` for an array with 5 elements returns:
- A) Element 5 (clamps to last)
- B) `NULL`
- C) `ArrayIndexOutOfBoundsException`
- D) Element 1 (wraps around)

**Answer: B**

---

**C8.** `df.tail(3)` vs `df.limit(3).collect()` — what's the difference?
- A) Both return the first 3 rows
- B) `tail(3)` returns LAST 3 rows; `limit(3).collect()` returns FIRST 3 rows
- C) `tail(3)` returns a DataFrame; `limit(3).collect()` returns a list
- D) They are identical

**Answer: B**

---

**C9.** `write.partitionBy("year", "month").save(path)` — how many files per `year=2024/month=3/` directory?
- A) Always exactly 1 file
- B) One file per Spark partition containing data for that year+month combination
- C) One file per executor
- D) Configurable; default is 200 files

**Answer: B**

---

**C10.** `df.write.bucketBy(10, "user_id").save("/tmp/output")` — what happens?
- A) Creates 10 bucket files at /tmp/output
- B) Fails — `bucketBy` only works with `saveAsTable()`
- C) Falls back to `partitionBy` with 10 partitions
- D) Writes to 10 directories

**Answer: B**

---

**C11.** `F.map_zip_with(m1, m2, lambda k, v1, v2: v1 + v2)` for `{"x": 10}` and `{"x": 5, "y": 3}` — what happens to key `"y"`?
- A) `"y"` is excluded (only keys in m1 are merged)
- B) `"y"` appears in result with value `None + 3 = None` (NULL for missing key in m1)
- C) `AnalysisException` — maps must have identical keys
- D) `"y"` appears with value `3` (pass-through)

**Answer: B** *(key present in m2 but not m1 → v1 is NULL; lambda result = NULL + 3 = NULL)*

---

**C12.** `F.transform_keys(F.col("prices"), lambda k, v: F.concat(k, F.lit("_usd")))` on `{"apple": 1.5}` returns:
- A) `{"apple": 1.5}` (unchanged — transform_keys cannot use Spark functions)
- B) `{"apple_usd": 1.5}`
- C) `{"APPLE": 1.5}` (uses upper by default)
- D) `AnalysisException`

**Answer: B**

---

**C13.** `Column.withField("city", F.lit("NYC"))` on a struct column `address(street STRING, zip STRING)` returns:
- A) A new StructType with only the `city` field
- B) A new StructType with `street`, `zip`, and `city` fields added
- C) `AnalysisException` — cannot add new fields, only replace
- D) A MapType with the new key-value pair

**Answer: B**

---

**C14.** `F.median(F.col("salary"))` uses which algorithm?
- A) Exact sort-based median
- B) Approximate Greenwald-Khanna sketch (same as `percentile_approx(col, 0.5)`)
- C) Reservoir sampling
- D) Exact median only for DoubleType columns

**Answer: B**

---

**C15.** `df.observe(obs, F.count("*"), F.mean("price"))` — when are the metrics available?
- A) Immediately after `observe()` is called
- B) Only after an action completes on the DataFrame; `Observation.get` blocks until then
- C) Only in streaming mode
- D) After `df.cache()` is called

**Answer: B**

---

**C16.** `F.overlay("ABCDE", "XYZ", 2, 3)` — what is the result?
- A) `"AXYZDE"` *(pos 2, len 1)*
- B) `"AXYZDE"` *(2 chars removed starting at pos 2)*

Corrected: `overlay("ABCDE", "XYZ", 2, 3)` replaces 3 chars starting at pos 2 (B,C,D) with "XYZ" → `"AXYZE"`

- A) `"AXYZE"`
- B) `"AXYZDE"`
- C) `"XYZDE"`
- D) `"ABXYZ"`

**Answer: A** *(pos=2 means replace starting at B; len=3 removes BCD; inserts XYZ → AXYZE)*

---

**C17.** Which Parquet compression codec is INVALID in Spark?
- A) `brotli`
- B) `zstd`
- C) `lz4`
- D) `deflate`

**Answer: D**

---

**C18.** `F.array_remove(F.col("tags"), "spark")` for `["spark", "sql", "spark", "python"]` returns:
- A) `["sql", "spark", "python"]` (removes first occurrence only)
- B) `["sql", "python"]` (removes ALL occurrences)
- C) `["spark", "sql", "python"]` (removes last occurrence only)
- D) `["spark", "sql", "spark", "python"]` (unchanged; use array_distinct instead)

**Answer: B**

---

**C19.** `current_timestamp()` is called in `df.withColumn("ts", F.current_timestamp())`. Two separate `show()` calls:
- A) Always produce the same timestamp (deterministic)
- B) May produce different timestamps — non-deterministic, evaluated at start of each query execution
- C) Always produce different timestamps
- D) Produce a timestamp rounded to the nearest second

**Answer: B**

---

**C20.** `df.dtypes` returns:
- A) A `StructType` schema object
- B) A Python list of `(column_name, type_string)` tuples
- C) A dict mapping column names to `DataType` objects
- D) A list of `DataType` objects

**Answer: B**

---

**C21.** `F.date_diff(end, start)` vs `F.datediff(end, start)`:
- A) `date_diff` is an alias for `datediff`; both return `IntegerType` days; functionally identical
- B) `date_diff` returns `LongType`; `datediff` returns `IntegerType`
- C) `date_diff` is for Spark SQL; `datediff` is for DataFrame API
- D) `date_diff` uses UTC; `datediff` uses session timezone

**Answer: A**

---

**C22.** `df.writeTo("catalog.schema.table").createOrReplace()` vs `.append()`:
- A) Both create if not exists; `createOrReplace` also drops first if exists
- B) `createOrReplace` atomically drops + recreates; `append` adds without removing data
- C) `createOrReplace` fails if table exists; `append` always succeeds
- D) They are identical for new tables

**Answer: B**

---

**C23.** `F.product(F.col("qty"))` aggregates `[3, NULL, 4, 2]`. Result?
- A) `0` (NULL treated as 0)
- B) `24` (NULLs ignored; 3 × 4 × 2 = 24)
- C) `NULL` (NULL propagates)
- D) `AnalysisException` — product requires non-null inputs

**Answer: B**

---

**C24.** `F.flatten(F.col("nested"))` on `[[1, 2], [], [3]]` returns:
- A) `[[1, 2], [], [3]]` (unchanged)
- B) `[1, 2, 3]` (empty inner arrays removed, others concatenated)
- C) `[1, 2, 0, 3]` (empty arrays become 0)
- D) `NULL`

**Answer: B**

---

**C25.** `df.crossJoin(df2)` requires which config?
- A) `spark.sql.crossJoin.required=true`
- B) `spark.sql.crossJoin.enabled=true`
- C) `spark.sql.joins.crossJoin=true`
- D) No config required; crossJoin is always allowed

**Answer: B**

---

**C26.** `df.inputFiles()` returns:
- A) A Spark DataFrame with file metadata
- B) A Python list of absolute input file paths
- C) A dict of file paths to partition counts
- D) A set of file names (not full paths)

**Answer: B**

---

**C27.** `F.zip_with(arr1, arr2, lambda x, y: x - y)` for `[10, 20]` and `[3, 7]` returns:
- A) `[13, 27]`
- B) `[7, 13]`
- C) `[10, 20, 3, 7]`
- D) `NULL`

**Answer: B**

---

**C28.** `F.array_distinct(F.col("items"))` for `["a", "b", "a", "c", "b"]` returns:
- A) `["a", "b", "c"]` (sorted unique values)
- B) `["a", "b", "c"]` (order of first occurrence preserved)
- C) `["b", "a", "c"]` (reverse order)
- D) `["a", "b", "a", "c", "b"]` (unchanged)

**Answer: B** *(preserves first occurrence order: a, b, c)*

---

**C29.** `F.transform_values(F.col("scores"), lambda k, v: v * 1.1)` on `{"math": 80}` returns:
- A) `{"math": 80}` (transform_values requires integer lambdas)
- B) `{"math": 88.0}` (80 × 1.1)
- C) `{"math_scaled": 88.0}` (key is modified to indicate scaling)
- D) `AnalysisException` — lambda must accept only value, not key

**Answer: B**

---

**C30.** With `spark.sql.ansi.enabled=true`, what does `element_at(array("a","b"), 5)` do?
- A) Returns `NULL`
- B) Raises `SparkArrayIndexOutOfBoundsException`
- C) Returns the last element `"b"`
- D) Returns `"a"` (wraps around)

**Answer: B** *(ANSI mode: element_at raises exception; use try_element_at for NULL return)*

---

## Practice Test C — Tuning, Streaming, Connect, Pandas API (30 Questions)

**D1.** AQE skew join detects a skewed partition. What does it do?
- A) Converts the join to BroadcastHashJoin automatically
- B) Splits the skewed partition into sub-partitions; replicates the matching non-skewed partition for each pair
- C) Adds a filter to exclude outlier data
- D) Repartitions the entire dataset uniformly

**Answer: B**

---

**D2.** `spark.sql.adaptive.coalescePartitions.parallelismFirst=true` (default). Effect?
- A) Targets `minPartitionNum` as primary goal; ignores `advisoryPartitionSizeInBytes`
- B) Targets `advisoryPartitionSizeInBytes`; ignores `minPartitionNum` entirely
- C) Uses whichever config produces more partitions
- D) Only applicable when DRA is enabled

**Answer: B**

---

**D3.** `spark.sql.execution.arrow.pyspark.selfDestruct.enabled=true` helps by:
- A) Preventing Arrow from being used for small DataFrames
- B) Releasing JVM Arrow buffers immediately after copying to pandas, reducing peak heap during toPandas()
- C) Caching the Arrow result for repeated `toPandas()` calls
- D) Converting Arrow to Parquet format before copying

**Answer: B**

---

**D4.** Whole-stage code generation is auto-disabled when:
- A) More than 10 stages exist in the DAG
- B) Operator input/output fields exceed `spark.sql.codegen.maxFields` (default 100)
- C) The cluster has fewer than 4 cores per executor
- D) AQE is enabled

**Answer: B**

---

**D5.** `spark.sql.files.ignoreMissingFiles=true`. A file is deleted between plan and execution:
- A) `FileNotFoundException` is raised
- B) The missing file is skipped; only successfully read data is returned
- C) Spark re-plans the query around the missing file
- D) The partition containing the missing file returns NULL rows

**Answer: B**

---

**D6.** `spark.shuffle.file.buffer=128k` (increased from default 32k). Effect?
- A) Reduces executor memory usage
- B) Reduces syscall frequency for shuffle writes; increases executor heap usage per write stream
- C) Speeds up shuffle reads
- D) Increases default task count after shuffle

**Answer: B**

---

**D7.** Off-heap memory (`spark.memory.offHeap.enabled=true`). Select all true statements.
- A) Not subject to JVM garbage collection
- B) `offHeap.size` is per-executor; additional to `spark.executor.memory`
- C) Automatically disables on-heap caching
- D) Used by Tungsten and OFF_HEAP storage level

**Answer: A, B, D**

---

**D8.** `spark.kryo.registrationRequired=true` and a class is NOT registered. What happens?
- A) Spark falls back to Java serialization silently
- B) `KryoException` is raised; the task/job fails
- C) The unregistered class is serialized with full class name (larger but functional)
- D) `AnalysisException` at session creation

**Answer: B**

---

**D9.** `spark.sql.execution.sortBeforeRepartition=true`. What is sorted?
- A) Output rows globally across all partitions
- B) Records within each map-side partition by hash value before repartition shuffle write
- C) Keys within each shuffle reduce partition
- D) Broadcast join probe-side records

**Answer: B** *(not a global sort; per map-partition sort by hash for better sequential disk writes)*

---

**D10.** `spark.sql.files.openCostInBytes=4MB`. Effect?
- A) Limits max Parquet row group size to 4MB
- B) Adds 4MB virtual padding per file when computing partition sizes, encouraging merging of small files
- C) Forces files larger than 4MB to be split into multiple partitions
- D) Allocates 4MB buffer per file descriptor

**Answer: B**

---

**D11.** `trigger(availableNow=True)` vs `trigger(once=True)`. How do they differ?
- A) Identical — both process all available data in one batch then stop
- B) `once` uses one micro-batch; `availableNow` uses multiple micro-batches (respecting rate limits), then stops
- C) `availableNow` is deprecated in favor of `once`
- D) `once` is for streaming; `availableNow` is for batch

**Answer: B**

---

**D12.** A streaming query reads from a file source without `.schema()`. What happens?
- A) Spark infers the schema from the first file
- B) `AnalysisException` — streaming file sources require explicit schema
- C) Spark uses `StringType` for all columns as fallback
- D) Spark reads metadata from the checkpoint for schema

**Answer: B**

---

**D13.** Console sink limitations (select all true):
- A) Not fault-tolerant — no checkpoint of output
- B) Prints to driver stdout
- C) Suitable for production with `outputMode=append`
- D) Not suitable for production use

**Answer: A, B, D**

---

**D14.** Watermark: current max event time = `14:30`; delay = `15 min`. Drop threshold?
- A) `14:00`
- B) `14:15`
- C) `14:30`
- D) `14:45`

**Answer: B** *(14:30 - 15 min = 14:15)*

---

**D15.** An event arrives at event_time `14:10` with the watermark threshold at `14:15`. Is it dropped?
- A) No — `14:10` is recent enough
- B) Yes — `14:10 ≤ 14:15` so it is dropped as late data
- C) No — watermark only affects window closing, not event filtering
- D) Depends on `outputMode`

**Answer: B** *(14:10 ≤ 14:15 → event is dropped / late data)*

---

**D16.** `session_window` — a session closes when:
- A) The window duration of 10 minutes elapses from session start
- B) No event arrives within the configured gap duration
- C) A watermark passes the session start time
- D) The batch trigger fires

**Answer: B**

---

**D17.** Kafka source schema — what type is the `value` column?
- A) `StringType`
- B) `BinaryType`
- C) `MapType(StringType, StringType)`
- D) Inferred from the first message

**Answer: B**

---

**D18.** Setting `kafka.group.id` to a fixed value in Spark Streaming. Risk?
- A) Spark cannot commit Kafka offsets without a group.id
- B) Multiple Spark queries sharing the same group.id interfere with each other's offset tracking
- C) Kafka broker rejects connections from Spark
- D) Spark uses sequential polling instead of consumer groups

**Answer: B**

---

**D19.** `maxOffsetsPerTrigger=5000` — what does it limit?
- A) Offsets per Kafka partition per trigger
- B) Total Kafka offsets across all partitions per trigger
- C) Maximum lag before a backpressure alert is raised
- D) Number of Kafka partitions read per trigger

**Answer: B**

---

**D20.** `mapGroupsWithState` emits how many rows per group per trigger?
- A) Zero or one
- B) Exactly one
- C) Zero or more
- D) Depends on the state timeout

**Answer: B**

---

**D21.** In Spark Connect, `AnalysisException` surfaces when:
- A) The transformation (e.g., `.filter()`) is applied — local validation on client
- B) An action (e.g., `.collect()`) is triggered — plan sent to server for analysis
- C) The SparkSession is created
- D) The schema is explicitly provided

**Answer: B**

---

**D22.** Token authentication URL format for Spark Connect:
- A) `sc://host:15002?token=myToken`
- B) `sc://host:15002/;token=myToken`
- C) `sc://token:myToken@host:15002`
- D) `sc://host:15002#token=myToken`

**Answer: B**

---

**D23.** Spark Connect eliminates the local JVM requirement because:
- A) It uses REST API instead of gRPC
- B) It replaces Py4J with a gRPC stub; the JVM runs only on the remote server
- C) Python operators are compiled to native code on the client
- D) All execution happens on the driver machine as pure Python

**Answer: B**

---

**D24.** Spark Connect server crashes mid-query. What happens to the client Python process?
- A) The Python process is killed along with the JVM
- B) The Python process survives; the developer can reconnect and resubmit
- C) Spark automatically retries the query on a standby server
- D) The query result is partially returned from the checkpoint

**Answer: B**

---

**D25.** How are Python UDFs handled in Spark Connect?
- A) UDFs are not supported in Spark Connect
- B) Pickled on client → sent as part of gRPC plan → deserialized and run in Python worker on executor
- C) Compiled to JVM bytecode on the client and sent to the server
- D) Evaluated on the client and results sent to server

**Answer: B**

---

**D26.** `psdf.spark.cache()` applies what storage level?
- A) `MEMORY_ONLY`
- B) `MEMORY_AND_DISK`
- C) `OFF_HEAP`
- D) `DISK_ONLY`

**Answer: B**

---

**D27.** `default_index_type="distributed"` — key characteristic?
- A) Contiguous 0-based index; matches pandas behavior
- B) Non-contiguous; uses `monotonically_increasing_id()`; fastest option
- C) Sorted index; requires a shuffle
- D) Requires a schema with an explicit integer primary key

**Answer: B**

---

**D28.** `psdf.fillna(0)` on a float column with both NULLs and NaN values. Result?
- A) Fills both NULL and NaN with 0
- B) Fills NULL with 0; NaN remains unchanged
- C) Fills NaN with 0; NULL remains unchanged
- D) Raises `TypeError` for NaN

**Answer: B**

---

**D29.** `sum([1.0, float('nan'), 2.0])` computed by Spark SQL aggregation. Result?
- A) `3.0` (NaN treated like NULL and ignored)
- B) `NaN` (NaN propagates through arithmetic)
- C) `NULL` (NaN causes NULL propagation)
- D) `AnalysisException`

**Answer: B**

---

**D30.** `psdf.to_delta("/mnt/output")` is equivalent to:
- A) `psdf.to_spark().write.format("parquet").save("/mnt/output")`
- B) `psdf.to_spark().write.format("delta").save("/mnt/output")`
- C) `psdf.spark.write.delta("/mnt/output")`
- D) `delta.DeltaTable.create(psdf, "/mnt/output")`

**Answer: B**

---

## Practice Test Answer Keys (Summary)

### Test A (Architecture + SQL)
```
A1:B  A2:B  A3:B  A4:B  A5:B  A6:B  A7:B  A8:B  A9:B  A10:B
A11:B A12:B A13:AB A14:B A15:B A16:A A17:B A18:B A19:B A20:B
B1:B  B2:B  B3:B  B4:B  B5:B  B6:B  B7:B  B8:B  B9:B  B10:B
B11:B B12:B B13:B B14:B B15:B B16:B B17:B B18:B B19:B B20:B
```

### Test B (DataFrame API)
```
C1:B  C2:B  C3:B  C4:B  C5:B  C6:B  C7:B  C8:B  C9:B  C10:B
C11:B C12:B C13:B C14:B C15:B C16:A C17:D C18:B C19:B C20:B
C21:A C22:B C23:B C24:B C25:B C26:B C27:B C28:B C29:B C30:B
```

### Test C (Tuning + Streaming + Connect + Pandas)
```
D1:B  D2:B  D3:B  D4:B  D5:B  D6:B  D7:ABD D8:B  D9:B  D10:B
D11:B D12:B D13:ABD D14:B D15:B D16:B D17:B D18:B D19:B D20:B
D21:B D22:B D23:B D24:B D25:B D26:B D27:B D28:B D29:B D30:B
```

---

## Pitfalls Matrix by Topic

| Topic | Most Common Mistake | Correct Behavior |
|-------|--------------------|--------------------|
| Architecture | Assuming coalesce increases partitions | coalesce cannot increase; use repartition |
| Architecture | Confusing Worker daemon with Executor | Worker launches Executor JVMs; separate processes |
| Architecture | Barrier mode retries only failed task | Entire stage resubmits |
| SQL | `cardinality(NULL)` = -1 | NULL (SQL-standard) |
| SQL | `size(NULL)` = NULL | -1 (legacy default) |
| SQL | `unix_date` returns seconds | IntegerType DAYS |
| SQL | `from_csv` supports nested types | Flat only |
| SQL | ANSI CAST returns NULL | Exception |
| SQL | `split_part` is 0-indexed | 1-indexed |
| DataFrame | `df.tail(5)` is first 5 | LAST 5 rows |
| DataFrame | `df.to()` = `df.select()` | `to()` auto-casts by name; `select()` does not |
| DataFrame | `partitionBy` auto-merges to 1 file | No auto-coalesce |
| DataFrame | `bucketBy` works with path writes | Only `saveAsTable` |
| DataFrame | `array_remove` removes first occurrence | Removes ALL occurrences |
| DataFrame | `deflate` is valid Parquet codec | NOT valid |
| DataFrame | `F.median()` is exact | Approximate |
| DataFrame | `observe()` is streaming-only | Works with batch DataFrames too |
| Tuning | `offHeap.size` replaces executor.memory | Additional to executor.memory |
| Tuning | Off-heap disables on-heap caching | No, must specify OFF_HEAP explicitly |
| Tuning | `parallelismFirst=true` respects minPartitionNum | Ignores it |
| Streaming | `trigger(once)` = multiple batches | One batch then stop |
| Streaming | Streaming schema is inferred | Must be explicit |
| Streaming | `mapGroupsWithState` emits 0+ rows | Exactly 1 row |
| Streaming | `kafka.group.id` is required | Creates interference risk |
| Connect | `AnalysisException` at transformation | At action time |
| Connect | Client Python dies on server crash | Client survives |
| Pandas API | `fillna(0)` fills NaN too | Only NULL; NaN is separate |
| Pandas API | `distributed` index is contiguous | Non-contiguous |

---

## Multi-Answer & All/None Strategy

### Handling `many` type (20 questions)
1. Read ALL options before selecting
2. Apply positive test: is this statement true based on your knowledge?
3. Apply negative test: is there any specific reason this statement is false?
4. Known multi-answer patterns in Iter 6:
   - Q8: coalesce → `A, B, D` (C is wrong: cannot increase count)
   - Q15: supervise → `A, B, C` (D is fabricated)
   - Q20: app.name → `A, B, C` (D is wrong: same name ≠ same ID)
   - Q60: partitionBy → `A, B, C` (D is wrong: no auto-coalesce)
   - Q69: observe → `A, B, D` (C is wrong: not streaming-only)
   - Q73: codegen → `A, B, C` (D is wrong: Tungsten unaffected)
   - Q78: off-heap → `A, B, D` (C is wrong: on-heap not disabled)
   - Q100: NULL/NaN → `A, C, D` (B is wrong: dropna behavior incorrect)

### Handling `all` type (5 questions)
- When you believe ALL four options are correct, select ALL FOUR
- Q4 (Barrier execution) is confirmed `all` type: A, B, C, D
- Do not second-guess — if the evidence supports all four, select all

### Handling `none` type (2 questions)
- Occurs when NONE of A, B, C, D is the correct answer
- Symptoms: all options have a plausible-sounding error; "none of the above" may be option D or E
- Strategy: verify each option is actually wrong before concluding none is correct

---

## Exam Day Checklist

**30 minutes before:**
- [ ] Review the QUICK_REFERENCE_ITER6 answer key (memorize non-B answers)
- [ ] Review the 7 multi-answer patterns above
- [ ] Review the Parquet codec trap (deflate = invalid) and ANSI mode CAST trap

**During exam:**
- [ ] For single-answer: read all 4 options before committing; B is likely but not always correct
- [ ] For multi-answer: start by identifying which options are definitely wrong; select remaining
- [ ] For `all` type: if every option is defensible, select all four
- [ ] Time budget: target ≤ 45 seconds for Easy, ≤ 60 seconds for Medium, ≤ 90 seconds for Hard
- [ ] Flag Hard questions; answer anyway; revisit if time allows
- [ ] Topic 3 (DataFrame) = 30% → don't rush HOF questions; they're worth the time

**Key non-B answers to remember:**
```
Q12: A  (locality wait override)
Q29: A  (bit_or result = 15)
Q30: A  (array_compact → removes NULLs)
Q44: A  (df.to() vs df.select())
Q45: A  (transform_keys → uppercase keys)
Q48: A  (Column.dropFields)
Q49: A  (df.tail → last rows)
Q54: A  (F.flatten)
Q58: A  (date_diff aliases)
Q64: A  (F.overlay result)
Q67: A  (df.inputFiles)
Q74: A  (openCostInBytes effect)
Q65: D  (deflate not valid)
Q70: C  (ANSI CAST raises exception)
Q79: C  (sortBeforeRepartition)
```

**Multi-answer questions (select multiple):**
```
Q4:   A,B,C,D  Q8:   A,B,D    Q15:  A,B,C
Q20:  A,B,C    Q60:  A,B,C    Q69:  A,B,D
Q73:  A,B,C    Q78:  A,B,D    Q100: A,C,D
```
