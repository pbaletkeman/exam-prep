# Databricks Certified Associate Developer — Practice Strategy (Iteration 2)

**Edition**: Iteration 2 | **Difficulty**: 20E / 60M / 20H | **Answer Types**: 81 single / 19 multi-answer

---

## Overview

This document provides a structured study plan, four mock tests, a common pitfalls matrix, and exam-day strategy for the Databricks Certified Associate Developer for Apache Spark certification. All materials align with the Iteration 2 question bank (100 questions).

**Iteration 2 at a Glance:**
- 20 Easy | 60 Medium | 20 Hard
- **81 single-answer | 19 multi-answer** (multi-answer questions require selecting ALL correct choices)
- 7 Topics in 90 minutes (average ~54 seconds per question)

---

## 4-Week Daily Study Plan

### Week 1 — Foundations (Architecture + SQL)

**Goal:** Build solid understanding of Spark internals and SQL functions.

| Day | Focus Area | Activities |
|-----|-----------|-----------|
| Monday | Architecture Fundamentals | Study deploy modes (client vs cluster), `local[*]`, Standalone port 7077, `--deploy-mode` flag. Write examples from memory. |
| Tuesday | Memory and Executors | Study Executor memory model (heap, Spark Memory fraction, overhead). Calculate `spark.memory.fraction` examples. Understand `MEMORY_ONLY_SER` vs `MEMORY_ONLY` vs `MEMORY_AND_DISK`. |
| Wednesday | Accumulators and Broadcast | Practice accumulator trap (Tasks read initial value; Driver reads final). Practice broadcast variable creation and `.value` access. |
| Thursday | DRA + Speculative Execution | Dynamic Resource Allocation requirements (external shuffle service). Speculative execution duplicate task behaviour. Stage count analysis (groupBy + orderBy = ~3 stages). |
| Friday | SQL Functions Part 1 | Drill `F.lit()`, `F.to_json()`, `concat_ws` null behaviour, `F.split()`, `F.date_format()`, `F.current_timestamp()` (evaluated once). |
| Saturday | SQL Functions Part 2 | Drill `F.approx_count_distinct` (HyperLogLog), `explode` vs `explode_outer`, `F.coalesce()`, `GROUPING SETS`, `CROSS JOIN` size. |
| Sunday | Review Week 1 + Mock Test 1 | Take Mock Test 1 (40 questions). Score and review all misses. |

---

### Week 2 — Intermediate (Window Functions + DataFrame API)

**Goal:** Master window functions, join types, and DataFrame operations.

| Day | Focus Area | Activities |
|-----|-----------|-----------|
| Monday | Window Functions | `percent_rank` vs `cume_dist` formulas and ranges. `ntile` uneven distribution rule (earlier tiles get extras). `lead()`/`lag()` boundary row behaviour (returns null). |
| Tuesday | Window Frames | Valid frame specifications (rowsBetween, rangeBetween). Shared Window spec reuse (optimizer may consolidate, not guaranteed). |
| Wednesday | DataFrame Creation | `spark.range()` schema (id:LongType). `spark.read.text()` schema (value:StringType). `toDF(*names)` renames by position. `mergeSchema=True` for Parquet schema evolution. |
| Thursday | Joins Deep Dive | All 7 join types. Ambiguous column reference after join (AnalysisException). Default join type = inner. Multi-column join syntax. `crossJoin()` = Cartesian product. |
| Friday | Null Handling + Filtering | `isNull()`/`isNotNull()`. Why `col != None` fails. `na.drop()` vs `dropna()`. `when()` without `otherwise()` = null. |
| Saturday | Collections + Transforms | `array_contains()`, `explode`/`explode_outer`/`posexplode`. `unionByName` vs `union` (name vs position). `allowMissingColumns=True`. |
| Sunday | Review Week 2 + Mock Test 2 | Take Mock Test 2 (50 questions). Score and review. |

---

### Week 3 — Advanced (Streaming + Tuning + Spark Connect)

**Goal:** Cover all streaming concepts, tuning patterns, and Spark Connect.

| Day | Focus Area | Activities |
|-----|-----------|-----------|
| Monday | Structured Streaming Basics | `writeStream.start()` → StreamingQuery. Rate source schema (timestamp+value). Socket limitations. `awaitTermination()` necessity. |
| Tuesday | Streaming Triggers and Modes | `once=True` (single batch) vs `availableNow=True` (multiple batches, Spark 3.3+). Output modes: append/update/complete — when to use each. |
| Wednesday | Streaming Advanced | Watermark cutoff formula: `max_seen − delay`. `foreachBatch` for multiple sinks. Memory sink + `queryName`. Delta Lake as source. |
| Thursday | Troubleshooting and Tuning | `cache()` laziness trap. `MEMORY_ONLY` drops partitions. `sortWithinPartitions` (no shuffle) vs `orderBy` (full shuffle). GC OOM fix: increase executor memory OR shuffle partitions OR reduce executor cores. |
| Friday | Spark Connect | Port 15002 (gRPC). Py4J vs gRPC protocol change. Client crash resilience. No RDD API. Arrow results. Version compatibility. |
| Saturday | Pandas API on Spark | `ps.from_pandas()`. `to_spark()` returns PySpark DF. Koalas deprecated. `distributed-sequence` vs `sequence` index trade-off. |
| Sunday | Review Week 3 + Mock Test 3 | Take Mock Test 3 (60 questions). Score and review. |

---

### Week 4 — Integration and Exam Readiness

**Goal:** Integrate all topics, stress-test weak areas, final review.

| Day | Focus Area | Activities |
|-----|-----------|-----------|
| Monday | Common Pitfalls Drill | Work through the pitfalls matrix below. Focus on traps you missed in Mock Tests 1-3. |
| Tuesday | Configuration Deep Dive | Know ALL 12 config properties in Quick Reference Table 2. Practice mental calculations for `spark.memory.fraction`. |
| Wednesday | Topic 1 + 4 Full Review | Re-read Study Guide Topic 1 and Topic 4. Write 10 key facts from memory without looking. |
| Thursday | Topic 2 + 3 Full Review | Re-read Study Guide Topics 2 and 3. Drill function return types and syntax. |
| Friday | Topic 5 + 6 + 7 Full Review | Re-read Study Guide Topics 5, 6, 7. Focus on Spark Connect architecture (new for Iter 2). |
| Saturday | Timed Practice + Weak Spot Review | Review all Quick Reference memory anchors (35 facts). Do any lingering topic drills. |
| Sunday | Mock Test 4 (Full 100Q) | Take Mock Test 4 under exam conditions. 90 minutes. No notes. |

---

## Mock Test 1 — Foundations (40 Questions)

**Time Limit:** 36 minutes (simulates 54 seconds/question pace)
**Answer types:** ~33 single-answer / ~7 multi-answer

### Questions by Topic

**Topic 1 — Architecture (10 questions)**

1. What does `local[*]` mean as a Spark master URL?
   - A) Connect to Standalone cluster using all worker nodes
   - B) Run locally in a single JVM using all available logical CPU cores
   - C) Run locally with a dynamic thread count capped at the machine's memory
   - D) Run in client mode with auto-scaling workers

2. The `--deploy-mode` flag in `spark-submit` controls:
   - A) Whether the cluster runs on YARN or Kubernetes
   - B) Where the Driver process runs (client machine or worker node)
   - C) How many Executors are initially allocated
   - D) Which output format the application writes

3. What is the default gRPC port for Spark Connect?
   - A) 4040
   - B) 7077
   - C) 8080
   - D) 15002

4. Which statement about accumulators is true?
   - A) Tasks can both read and write accumulator values
   - B) Only the Driver can read the final accumulated value after an action
   - C) Reading an accumulator inside a Task returns the current running total
   - D) Accumulators are replicated across Executors like broadcast variables

5. `spark.default.parallelism` controls default partition count for: *(single)*
   - A) DataFrame shuffle operations
   - B) RDD operations (e.g., reduceByKey)
   - C) Both RDD and DataFrame operations equally
   - D) Number of input file partitions

6. The default storage level for `df.cache()` on a PySpark DataFrame is: *(single)*
   - A) `MEMORY_ONLY`
   - B) `MEMORY_AND_DISK_SER`
   - C) `MEMORY_AND_DISK`
   - D) `DISK_ONLY`

7. In cluster deploy mode, if the submitting machine crashes: *(single)*
   - A) The job fails immediately
   - B) The Driver continues running on the cluster; the job is unaffected
   - C) The Cluster Manager restarts the Driver on the submitting machine
   - D) The job pauses and waits for the submitting machine to recover

8. Which of the following are true about broadcast variables? *(multi — select all that apply)*
   - A) Serialized and cached on each Executor
   - B) Accessed via the `.value` attribute
   - C) Mutable — Tasks can update values
   - D) Re-sent to an Executor if that Executor fails
   - E) Automatically destroyed after each action completes

9. `spark.executor.memoryOverhead` is used for: *(single)*
   - A) The Spark Memory region (Execution + Storage)
   - B) Off-heap memory: OS overhead, Python worker processes, native libraries
   - C) User Memory for application code and data structures
   - D) Shuffle spill buffers within the JVM

10. Approximately how many Stages does this DAG produce?
    `read → groupBy → orderBy → write.parquet` *(single)*
    - A) 1
    - B) 2
    - C) 3
    - D) 5

**Topic 2 — Spark SQL (10 questions)**

11. `createGlobalTempView('events')` is called when 'events' already exists: *(single)*
    - A) Silently replaces the existing view
    - B) Creates a second view with a suffix
    - C) Raises `AnalysisException`
    - D) Creates a session-scoped view instead

12. What does `F.lit(100)` return? *(single)*
    - A) The integer value 100
    - B) A Column representing the constant scalar value 100
    - C) A DataFrame with one row containing 100
    - D) A Python dictionary with key 'lit' and value 100

13. `F.to_json(col('address'))` returns what type? *(single)*
    - A) `StructType`
    - B) `MapType`
    - C) `BinaryType`
    - D) `StringType`

14. `concat_ws('-', array('hello', null, 'world'))` returns: *(single)*
    - A) `'hello-null-world'`
    - B) `'hello-world'`
    - C) `null`
    - D) Raises `AnalysisException`

15. Which expression is valid in `selectExpr()`? *(multi — select all that apply)*
    - A) `CASE WHEN score > 80 THEN 'high' ELSE 'low' END`
    - B) `IF(score > 80, 'high', 'low')`
    - C) `NULLIF(score, 0)`
    - D) `IIF(score > 80, 'high', 'low')`
    - E) `SWITCH(score, 80, 'high', 'low')`

16. `F.approx_count_distinct` uses which algorithm? *(single)*
    - A) Bloom filter
    - B) Count-Min Sketch
    - C) HyperLogLog
    - D) MinHash

17. `ntile(3)` on 10 rows: how many rows in tile 1? *(single)*
    - A) 3
    - B) 4
    - C) 2
    - D) 5

18. `percent_rank()` on the first row in its window returns: *(single)*
    - A) `1/N`
    - B) `0.0`
    - C) `1.0`
    - D) `null`

19. `lead()` on the last row in a window returns: *(single)*
    - A) The same value as the current row
    - B) The last non-null value in the window
    - C) `null` (unless a default is specified)
    - D) Raises an AnalysisException

20. How does Catalyst handle `df.filter(col('status')=='active').select('id','name')`? *(single)*
    - A) Executes filter first, then select
    - B) Executes select first to reduce columns, then filter
    - C) Pushes both filter and projection to the FileScan
    - D) No optimization is applied

**Topic 3 — DataFrame API (10 questions)**

21. `spark.range(0, 5)` produces a DataFrame with what schema? *(single)*
    - A) `id: IntegerType`
    - B) `id: LongType`
    - C) `index: LongType`
    - D) `value: LongType`

22. `spark.read.text('/file.txt')` produces what schema? *(single)*
    - A) `line: StringType`
    - B) `value: StringType`
    - C) `content: StringType`
    - D) `text: StringType`

23. Valid ways to filter null values? *(multi — select all that apply)*
    - A) `df.filter(col('email').isNotNull())`
    - B) `df.filter(~col('email').isNull())`
    - C) `df.na.drop(subset=['email'])`
    - D) `df.filter(col('email') != None)`

24. `F.when(col('score') > 90, 'A')` with no `otherwise()` — what happens for score=75? *(single)*
    - A) Returns `'F'` (default failing grade)
    - B) Returns `null`
    - C) Raises an AnalysisException
    - D) Returns the original score value

25. What is the default join type in `df1.join(df2, 'user_id')`? *(single)*
    - A) `left`
    - B) `full`
    - C) `inner`
    - D) `left_semi`

**Topic 4 — Troubleshooting (5 questions)**

26. When is `df.cache()` actually materialised? *(single)*
    - A) Immediately when `.cache()` is called
    - B) During the next action that triggers plan execution
    - C) On the next transformation applied to df
    - D) When the SparkSession is stopped

27. `MEMORY_ONLY` when a partition doesn't fit in memory: *(single)*
    - A) Spills to disk
    - B) Raises OOM exception
    - C) **Drops the partition** (recomputes on next access)
    - D) Compresses the partition to fit

28. 10 GB heap, `spark.memory.fraction=0.6` → Spark Memory = ? *(single)*
    - A) 4 GB
    - B) 5 GB
    - C) 6 GB
    - D) 3 GB

29. `sortWithinPartitions` vs `orderBy` — key difference? *(single)*
    - A) `sortWithinPartitions` is faster because it uses more memory
    - B) `orderBy` produces a global sort with full shuffle; `sortWithinPartitions` sorts per-partition with no shuffle
    - C) They are identical in behavior
    - D) `sortWithinPartitions` is the default; `orderBy` is the explicit form

30. Which config controls auto-broadcast join threshold? *(single)*
    - A) `spark.broadcast.maxSize`
    - B) `spark.sql.autoBroadcastJoinThreshold`
    - C) `spark.driver.maxBroadcastSize`
    - D) `spark.sql.broadcastTimeout`

**Topic 5-7 — Streaming, Connect, Pandas API (10 questions)**

31. `writeStream.start()` returns: *(single)*
    - A) DataFrame
    - B) StreamingQuery
    - C) Future
    - D) None

32. `rate` source schema: *(single)*
    - A) `value BIGINT`
    - B) `key STRING, value STRING`
    - C) `timestamp TIMESTAMP, value BIGINT`
    - D) `id LONG, data STRING`

33. `trigger(availableNow=True)` vs `trigger(once=True)`: *(single)*
    - A) They are identical
    - B) `availableNow` uses multiple micro-batches; `once` uses a single micro-batch
    - C) `availableNow` is for streaming; `once` is for batch
    - D) `once` is recommended for production; `availableNow` is deprecated

34. `complete` output mode requires: *(single)*
    - A) A watermark on the streaming query
    - B) Stateful aggregations (e.g., groupBy().count())
    - C) Delta Lake as the source
    - D) Kafka as the output sink

35. Spark Connect uses which protocol to replace Py4J? *(single)*
    - A) HTTP/1.1 REST with JSON
    - B) WebSockets
    - C) gRPC over HTTP/2 with Protocol Buffers
    - D) Apache Thrift

36. In Spark Connect, results are returned to the client as: *(single)*
    - A) Python pickle objects
    - B) JSON arrays
    - C) Apache Arrow record batches
    - D) CSV text

37. `ps.from_pandas(pdf)` converts: *(single)*
    - A) A PySpark DataFrame to a pyspark.pandas DataFrame
    - B) A native pandas DataFrame to a pyspark.pandas DataFrame
    - C) A native pandas DataFrame to a PySpark DataFrame
    - D) A CSV file to a pyspark.pandas DataFrame

38. `psdf.to_spark()` returns: *(single)*
    - A) Native pandas DataFrame collected to driver
    - B) PySpark DataFrame (distributed)
    - C) List of Row objects
    - D) pyspark.pandas DataFrame with reset index

39. `databricks.koalas` import status: *(single)*
    - A) Current recommended method
    - B) Raises ImportError on DBR 12+
    - C) Deprecated since Spark 3.2 (use pyspark.pandas)
    - D) Unrelated to pyspark.pandas

40. `'sequence'` index in pyspark.pandas requires: *(single)*
    - A) A broadcast join
    - B) A global sort (full shuffle) — expensive at scale
    - C) A repartition to 1 partition
    - D) Python UDFs for index assignment

---

**Mock Test 1 Answer Key:**
1-B, 2-B, 3-D, 4-B, 5-B, 6-C, 7-B, 8-A,B,D, 9-B, 10-C, 11-C, 12-B, 13-D, 14-B, 15-A,B,C, 16-C, 17-B, 18-B, 19-C, 20-C, 21-B, 22-B, 23-A,B,C, 24-B, 25-C, 26-B, 27-C, 28-C, 29-B, 30-B, 31-B, 32-C, 33-B, 34-B, 35-C, 36-C, 37-B, 38-B, 39-C, 40-B

**Scoring:** 36-40 = Excellent | 30-35 = Good | 24-29 = Review needed | <24 = Re-study topics

---

## Mock Test 2 — Intermediate (50 Questions)

**Time Limit:** 45 minutes
**Answer types:** ~41 single-answer / ~9 multi-answer

Focus: Higher proportion of Medium difficulty questions. Topics 2, 3, 4 emphasis.

### Quick Question Format (50Q Condensed)

**Architecture (10Q):**
1. Standalone cluster master URI uses which port? → **7077**
2. `MEMORY_ONLY_SER` stores data as: → serialized binary (compact; must deserialize on read)
3. DRA requires which external service? → External shuffle service
4. Execution Memory handles: → shuffle buffers, sort buffers, hash join maps
5. TaskScheduler responsibility: → Send individual Tasks to available Executor slots
6. Off-heap memory for Python workers: → `spark.executor.memoryOverhead`
7. `spark.speculation=true` → Launches duplicate Tasks for stragglers; first to finish wins
8. `broadcast.value['A']` — how to access broadcast variable: → via `.value` attribute
9. Input partitions from a 1 GB file (128 MB blocks): → ~8 partitions
10. `filter()` and `groupBy().agg()` are: → Transformations (lazy; no Job triggered)

**SQL (10Q):**
11. Remove session-scoped temp view: → `spark.catalog.dropTempView('name')`
12. SQL `coalesce(a, b, c)` returns: → First non-null value
13. `F.date_add(col('d'), 7)` returns: → DateType
14. `F.current_timestamp()` evaluation: → Once at query planning time (same for all rows)
15. `explode` on 3 rows × 2 elements = how many rows? → 6
16. `F.split(col, ',')` return type: → `ArrayType(StringType)`
17. `percent_rank()` minimum value: → 0.0 (first row)
18. `cume_dist()` minimum value: → `1/N` (never 0)
19. `ntile(4)` on 9 rows: tile 1 size? → 3 rows (9÷4=2 r1; first 1 tile gets extra)
20. Window frame `rowsBetween(currentRow, -1)`: → **Invalid** (end before start)

**DataFrame API (15Q):**
21. `left_semi` join returns: → Left rows with a match; no right columns
22. `left_anti` join returns: → Left rows with no match; no right columns
23. `unionByName(other, allowMissingColumns=True)` missing cols: → Filled with null
24. `union()` alignment: → By position (not by name)
25. Joining `df1.id == df2.id` then `select('id')`: → AnalysisException (ambiguous)
26. `F.array_contains(col('arr'), 'x')` return type: → `BooleanType`
27. Parquet schema evolution option: → `.option('mergeSchema', True)`
28. `monotonically_increasing_id()` guarantee: → Unique + increasing; NOT sequential
29. Pandas UDF faster than Python UDF because: → Arrow columnar batches (no per-row JVM↔Python)
30. `df.filter(col('country')=='US')` on partitioned Parquet: → Partition pruning (only country=US/ read)
31. `df.drop('col')` → Removes column; returns new DataFrame
32. `toDF('a','b','c')` renames by: → Position (all columns)
33. Write mode that silently skips if path exists: → `ignore`
34. `F.datediff(end, start)` return type: → `IntegerType` (number of days)
35. `F.lag('score', 1)` on first row: → `null`

**Troubleshooting (8Q):**
36. `df.unpersist()` does: → Removes cached blocks from Executor memory and disk
37. GC overhead OOM on Executor — fix options: → Increase executor memory, reduce executor cores, increase shuffle.partitions
38. Best executor cores per Executor for HDFS: → 4 or 5
39. `sortWithinPartitions` → no shuffle; `orderBy` → full shuffle ← TRUE/FALSE: → **TRUE**
40. `spark.sparkContext.setLogLevel('ERROR')` → suppresses INFO/WARN ← CORRECT API: → Yes
41. Salting step for skewed join (multi): → Salt large DF, replicate small DF N times, join on composite key
42. 5 GB heap, fraction=0.6: → 3 GB Spark Memory
43. `MEMORY_AND_DISK` default for: → `df.cache()` (DataFrame cache)

**Streaming (7Q):**
44. Memory sink table access: → `spark.sql("SELECT * FROM <queryName>")`
45. Delta Lake streaming source advantage: → Transaction log; replay from version/timestamp
46. Watermark: max_seen=12:15, delay=10min → cutoff = **12:05**
47. Event at 12:00 with cutoff 12:05: → **Dropped** (12:00 < 12:05)
48. `foreachBatch` use case: → Write to multiple sinks; apply batch API in micro-batch
49. Socket source limitation (multi): → Not fault-tolerant; no replay; text only; no offset tracking
50. `awaitTermination()` not called → streaming query terminates with main thread

---

**Scoring Target:** 45/50 to pass with confidence

---

## Mock Test 3 — Advanced (60 Questions)

**Time Limit:** 54 minutes
**Answer types:** ~49 single-answer / ~11 multi-answer

This test emphasises Hard questions and multi-answer scenarios from all 7 topics.

### 60Q Condensed Scenario Set

Use the full Study Guide and Quick Reference to create your own scenario questions from the items below. For each item, write a scenario + 4 options before checking the answer:

**Hard Architecture (5Q):**
- Stage count for `scan → groupBy → orderBy → write` pipeline
- Unified Memory Model: which region handles shuffle buffers?
- `MEMORY_ONLY_SER` vs `MEMORY_ONLY`: memory/speed trade-off
- DRA multi-answer: what does it do? (adds/removes Executors, requires external shuffle service)
- Broadcast variable multi-answer: serialized, immutable, `.value`, re-sent on failure

**Hard SQL (5Q):**
- `ntile(3)` on 10 rows: exact distribution per tile
- Window frame `rowsBetween(currentRow, -1)`: valid or raises error?
- Catalyst optimizer: what is the physical plan for filter + select on Parquet?
- `GROUPING SETS` with empty grouping `()`: produces grand total row with nulls
- `percent_rank` vs `cume_dist`: formulas, ranges, minimum values

**Hard DataFrame API (10Q):**
- `spark.range(0,10)` column name and type
- `spark.read.text()` column name and type
- Ambiguous column reference after join on condition vs on string key
- `monotonically_increasing_id()`: unique + increasing ≠ sequential
- `mergeSchema=True`: when and why
- Pandas UDF vs Python UDF: Arrow transfer advantage
- Partition pruning: what physically happens
- `unionByName` vs `union`: name vs position; `allowMissingColumns`
- GroupBy agg result schema: key columns first, count returns LongType
- Shared Window spec: optimizer may (not guaranteed) consolidate

**Hard Troubleshooting (5Q):**
- GC OOM: root cause + fix combination
- Executor cores tuning: 4-5 per Executor; why not 1; why not all
- Salting all steps: salt large, replicate small, join composite
- `spark.memory.fraction` calculation with custom value
- `MEMORY_ONLY` drops vs `MEMORY_AND_DISK` spills

**Hard Streaming (5Q):**
- Watermark late-data calculation: event at 12:00, max=12:15, delay=10min → dropped
- `availableNow` vs `once`: multiple vs single micro-batch
- `awaitTermination` necessity: streaming thread lifecycle
- `complete` mode: requires stateful aggregation
- Delta Lake streaming: multi-answer (replay, schema enforcement, simultaneously source+sink)

**Medium All Topics — Remaining 30Q:** Build scenarios from Quick Reference tables 2-15 in QUICK_REFERENCE_ITER2.md.

---

**Scoring Target:** 53/60 = 88% (exam passing threshold is approximately 70%)

---

## Mock Test 4 — Full Exam Simulation (100 Questions)

**Time Limit:** 90 minutes (exam-exact)
**Answer types:** 81 single-answer / 19 multi-answer
**Conditions:** No notes, no reference materials, timed

### Setup Instructions

1. Print or have STUDY_GUIDE_ITER2.md and QUICK_REFERENCE_ITER2.md physically available but **put them face-down**
2. Set a 90-minute timer
3. Write answers on paper or a separate document — do NOT look up answers during the test
4. After 90 minutes, stop and score

### Topic Distribution for 100Q

| Topic | Questions | Easy | Medium | Hard |
|-------|-----------|------|--------|------|
| 1. Architecture | 20 | 4 | 12 | 4 |
| 2. Spark SQL | 20 | 4 | 12 | 4 |
| 3. DataFrame API | 30 | 6 | 18 | 6 |
| 4. Troubleshooting | 10 | 2 | 6 | 2 |
| 5. Streaming | 10 | 2 | 6 | 2 |
| 6. Spark Connect | 5 | 1 | 3 | 1 |
| 7. Pandas API | 5 | 1 | 3 | 1 |

### Generating Your Own Full 100Q Test

Use the actual Iteration 2 question file at:
`c:\Users\Pete\Desktop\exam-prep-1\databricks\learning\questions\spark-databricks-iteration-2.md`

Study all 100 questions WITHOUT looking at the answer key first, then verify against the Answer Key section at the bottom of the file.

### Scoring Scale

| Score | Result | Action |
|-------|--------|--------|
| 90-100 | Outstanding | Ready for exam; review any misses |
| 80-89 | Strong Pass | Ready; strengthen weak spots |
| 70-79 | Marginal Pass | One more week of targeted study |
| 60-69 | Near Miss | Focus on weakest 2 topics; re-test |
| <60 | Not Ready | Full restart on weak topics |

---

## Common Pitfalls Matrix

| Pitfall | Wrong Assumption | Correct Answer | Where It Appears |
|---------|-----------------|----------------|-----------------|
| `df.cache()` default storage level | `MEMORY_ONLY` | `MEMORY_AND_DISK` | Q15, Topic 1 |
| `df.cache()` materialisation | Immediate | Next action only | Q71, Topic 4 |
| `when()` without `otherwise()` | Returns 0 or raises error | Returns **null** | Q42, Topic 3 |
| `col('x') != None` | Works as null check | Doesn't work (Python None comparison) | Q63, Topic 3 |
| `union()` column alignment | By name | By **position** | Q47, Topic 3 |
| Accumulator inside Task | Reads current total | Reads **initial value** (e.g., 0) | Q7, Topic 1 |
| `monotonically_increasing_id()` | Sequential (0,1,2...) | Unique + increasing; **gaps exist** | Q55, Topic 3 |
| `spark.default.parallelism` | Controls DataFrame shuffles | Controls **RDD** shuffles only | Q8, Topic 1 |
| `lead()` on last row | Raises error | Returns **null** | Q37, Topic 2 |
| `lag()` on first row | Raises error | Returns **null** | Q57, Topic 3 |
| Spark Connect port | 7077 (Standalone) | **15002** (gRPC) | Q91, Topic 6 |
| `ps.from_pandas()` | `pdf.to_spark()` (doesn't exist on native pandas) | `ps.from_pandas(pdf)` | Q96, Topic 7 |
| `'sequence'` index cost | Fast (just numbers) | Requires **global sort** (expensive) | Q100, Topic 7 |
| `to_spark()` result | Collects to driver | Returns **PySpark DF** (distributed) | Q97, Topic 7 |
| `MEMORY_ONLY` overflow | Spills to disk | **Drops partition** (recomputes) | Q73, Topic 4 |
| `ntile` uneven distribution | Later tiles get extras | **Earlier tiles** get the extra rows | Q38, Topic 2 |
| `concat_ws` with null | Returns null or 'hello-null-world' | **Skips nulls** silently | Q33, Topic 2 |
| `percent_rank` minimum | `1/N` | **0.0** (first row always 0) | Q36, Topic 2 |
| `cume_dist` minimum | 0.0 | **`1/N`** (never exactly 0) | Q36, Topic 2 |
| Cross join size | 150 (100+50) | **5,000** (100×50 Cartesian) | Q35, Topic 2 |
| Pandas UDF advantage | Runs on Driver | **Arrow columnar batches** to Python workers | Q68, Topic 3 |
| `sortWithinPartitions` | Produces global order | **Per-partition only**; no shuffle | Q75, Topic 4 |
| `availableNow=True` | Same as `once=True` | Multiple micro-batches (once=single batch) | Q85, Topic 5 |
| `writeStream.start()` return | DataFrame / None | **StreamingQuery** | Q81, Topic 5 |
| Client crash in client mode | Job continues | **Job fails** (Driver in application process) | Q5, Topic 1 |
| Client crash in Spark Connect | Job fails | **Job continues** (Driver on cluster) | Q93, Topic 6 |

---

## Exam Day Strategy

### Timing Management (90 minutes, 100 questions)

| Phase | Questions | Target Time | Notes |
|-------|-----------|-------------|-------|
| Phase 1: Quick wins | Easy questions (first pass) | 20 minutes | Don't overthink; trust first instinct |
| Phase 2: Medium difficulty | Bulk of exam | 45 minutes | Use elimination; mark uncertain ones |
| Phase 3: Hard + review | Hard Q + flagged | 20 minutes | Spend more time here |
| Buffer | — | 5 minutes | Final review of flagged answers |

### Multi-Answer Question Strategy

**Iteration 2 has 19 multi-answer questions** (approximately 1 in 5 questions).

Identification: The question stem includes **(Select all that apply)** or **"which of the following are true"**.

**Approach:**
1. Evaluate each option **independently** as true/false before looking at other options
2. Do NOT assume "exactly 2 correct" or "exactly 3 correct" — select all that are true
3. Elimination works: if you're confident 2 options are wrong, the answer is among the remaining
4. The most common trap: an option is almost right but has one wrong detail (e.g., "DRA works only on YARN" — FALSE, it works on YARN, Standalone, and Kubernetes)

### Topic Prioritisation by Question Count

1. **Topic 3 — DataFrame API (30Q = 30%)** — Highest weight; most important
2. **Topic 1 — Architecture (20Q = 20%)** — Second highest
3. **Topic 2 — Spark SQL (20Q = 20%)** — Equal second
4. **Topic 4 — Troubleshooting (10Q = 10%)** — Important; high difficulty
5. **Topic 5 — Streaming (10Q = 10%)** — Important; high difficulty
6. **Topics 6 + 7 (5Q each = 10% total)** — Fewer questions but distinct content

### Answer Elimination Technique

For any question where you're unsure:
1. **Eliminate obviously wrong options first** — often 2 options can be ruled out immediately
2. **Look for "always/never/must" language** — absolute statements are usually wrong
3. **Look for "may/can/typically"** — qualified statements are usually correct
4. **For config questions**: if the option is a real property name but controls something else, it's a distractor (e.g., `spark.driver.maxBroadcastSize` is not a real property)

### Last-Minute Review Targets

The night before the exam, quickly review these 10 items:

1. `df.cache()` = `MEMORY_AND_DISK` (not `MEMORY_ONLY`)
2. `cache()` materialises on the next action (lazy)
3. `spark.default.parallelism` = RDD only; `spark.sql.shuffle.partitions` = DataFrame/SQL
4. `when()` without `otherwise()` = null
5. `col != None` doesn't work — use `isNull()`
6. Spark Connect port = **15002**
7. `writeStream.start()` returns **StreamingQuery**
8. `ntile` extra rows → earlier tiles
9. `concat_ws` skips null elements
10. `'sequence'` index = global sort (expensive)

---

## Progress Tracking Template

Copy and fill in after each study session:

```
Date: ___________
Session focus: ___________
Topics covered: ___________
Mock test taken: Mock Test ___ / Score: ___/___
Pitfalls identified today:
  1.
  2.
  3.
Planned focus for next session:
```

---

## Score Projection

Based on your Mock Test scores, project exam readiness:

| Mock 1 (40Q) | Mock 2 (50Q) | Mock 3 (60Q) | Mock 4 (100Q) | Exam Readiness |
|-------------|-------------|-------------|--------------|---------------|
| ≥36 (90%) | ≥45 (90%) | ≥53 (88%) | ≥80 (80%) | Ready ✓ |
| 32-35 (80%) | 40-44 (80%) | 48-52 (80%) | 70-79 (70%) | Almost Ready |
| <32 (<80%) | <40 (<80%) | <48 (<80%) | <70 (<70%) | More Study Needed |

The actual exam passing threshold is approximately 70%. Target 80%+ on all mocks to have a comfortable buffer.
