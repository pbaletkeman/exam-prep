# PRACTICE STRATEGY — Iteration 5
# Databricks Certified Associate Developer for Apache Spark

**Exam profile:** 100 questions · 120 minutes · 1.2 min/question
**Format:** 78 single-answer, 22 multi-answer
**Pass threshold:** ~70% (70/100)

---

## TOPIC WEIGHTS & STAKES

| Topic | Questions | % of Exam | Questions to Pass (at 70%) |
|-------|-----------|-----------|---------------------------|
| Architecture | Q1–Q20 | **20%** | ≥14/20 |
| SQL | Q21–Q40 | **20%** | ≥14/20 |
| DataFrame API | Q41–Q70 | **30%** | ≥21/30 |
| Troubleshooting | Q71–Q80 | **10%** | ≥7/10 |
| Structured Streaming | Q81–Q90 | **10%** | ≥7/10 |
| Spark Connect | Q91–Q95 | **5%** | ≥3–4/5 |
| Pandas API | Q96–Q100 | **5%** | ≥3–4/5 |

**Strategy:** DataFrame (30%) is worth the most — master it first. Architecture and SQL together are 40% — both high-value. Streaming, Connect, and Pandas are smaller but often the source of tricky multi-answer questions.

---

## 4-WEEK STUDY PLAN

### Week 1 — Foundation (Architecture + SQL)

| Day | Focus | Activity |
|-----|-------|----------|
| 1 | Architecture core | Read STUDY_GUIDE_ITER5 §Topic 1. Memorise defaults table. |
| 2 | Storage levels | Drill storage level table. Write from memory: 5 levels + SER vs non-SER. |
| 3 | Memory model | Sketch unified memory model (storageFraction, execution, off-heap). |
| 4 | Architecture review | Practice Test 1 — Architecture only (20 Qs). Score. Fix gaps. |
| 5 | Date/time SQL | Read §2.1. Drill `trunc` vs `date_trunc` arg orders. `unix_timestamp` = LongType. |
| 6 | SQL functions | Arrays, maps, aggregates, GROUPING_ID, CTEs. Stack/nth_value. |
| 7 | SQL review | Practice Test 2 — SQL only (20 Qs). Score. Fix gaps. |

### Week 2 — DataFrame Deep Dive

| Day | Focus | Activity |
|-----|-------|----------|
| 8 | New methods | `transform`, `toLocalIterator`, `withColumnsRenamed`, `unpivot`, `offset`. |
| 9 | Read/write | `saveAsTable` vs `insertInto`, Delta `overwriteSchema`, `inferSchema`, CSV options. |
| 10 | Column functions | `levenshtein`, `soundex`, `assert_true`, `raise_error`, `conv`, `unhex`, `hash` vs `xxhash64`. |
| 11 | Null handling | `na.drop(thresh)`, `na.fill(subset)`, `when/otherwise`, NaN vs NULL distinction. |
| 12 | foreach/mapInPandas | `foreach` vs `foreachPartition`; `mapInPandas` signature and use. |
| 13 | Schema methods | `simpleString` vs `toDDL`, `F.to_csv`, `F.struct` result shape. |
| 14 | DataFrame review | Practice Test 3 — DataFrame only (30 Qs). Score. Fix gaps. |

### Week 3 — Streaming, Troubleshooting, Connect, Pandas

| Day | Focus | Activity |
|-----|-------|----------|
| 15 | Troubleshooting | Arrow config, column pruning vs pushdown, `task.cpus`, off-heap, AQE coalescing. |
| 16 | Streaming basics | Triggers, schema inference error, console sink, `inputRowsPerSecond`. |
| 17 | Streaming advanced | Watermark/late data math, `session_window`, Kafka schema, `kafka.group.id`. |
| 18 | stateful streaming | `flatMapGroupsWithState` rules (0+ rows, modes, timeouts, checkpoint). |
| 19 | Spark Connect | `AnalysisException` timing, token URL, no-JVM, UDF support, server crash. |
| 20 | Pandas API | `spark.cache`, `spark.explain`, index types, `to_delta`, NaN vs NULL. |
| 21 | Full review | Practice Test 4 — all 7 topics (40 Qs). Score. Identify weakest topic. |

### Week 4 — Simulation & Polish

| Day | Focus | Activity |
|-----|-------|----------|
| 22 | Weak topic review | Re-read STUDY_GUIDE sections for 2 lowest-scoring topics. |
| 23 | QUICK_REFERENCE drill | Cover answer column. Test yourself on each anchor card. |
| 24 | Pitfalls matrix | Read all 35 traps. For each one, recall WHY the wrong answer is wrong. |
| 25 | Full mock exam | Practice Test 5 (100 Qs). Full 120-min simulation. Score. |
| 26 | Gap analysis | Review only the questions missed. Read explanations carefully. |
| 27 | Final sprint | Run through answer key table in QUICK_REFERENCE. |
| 28 | Exam day | Skim QUICK_REFERENCE anchors. Trust your preparation. |

---

## PRACTICE TEST 1 — Architecture (20 Questions)

*Single answer unless marked (multi)*

**1.** What is the default value of `spark.sql.shuffle.partitions`?
a) 10  b) **200**  c) 500  d) 1000

**2.** Which storage level stores partitions as serialised binary in memory AND spills serialised to disk?
a) MEMORY_ONLY  b) MEMORY_AND_DISK  c) **MEMORY_AND_DISK_SER**  d) DISK_ONLY_SER

**3.** `spark.sql.adaptive.enabled` defaults to true in which Spark version?
a) Spark 2.4  b) Spark 3.0  c) **Spark 3.2**  d) Spark 3.4

**4.** [multi] Which three configs are required to set up the History Server?
a) `spark.eventLog.enabled=true`  b) `spark.eventLog.dir`  c) `spark.history.fs.logDirectory`  d) `spark.ui.enabled=true`

**5.** What happens to a `MEMORY_ONLY` partition when it is evicted?
a) It is written to disk  b) **It is dropped and recomputed from lineage**  c) It is archived to HDFS  d) The task fails

**6.** What does the Spark Block Manager manage?
a) Task scheduling only  b) Shuffle data only  c) **All block types: cached RDD/DF, broadcast, and shuffle files**  d) JVM heap allocation

**7.** What is the correct task locality preference order (most to least)?
a) ANY → RACK_LOCAL → NODE_LOCAL → PROCESS_LOCAL  b) **PROCESS_LOCAL → NODE_LOCAL → RACK_LOCAL → ANY**  c) NODE_LOCAL → PROCESS_LOCAL → RACK_LOCAL → ANY  d) PROCESS_LOCAL → RACK_LOCAL → NODE_LOCAL → ANY

**8.** `spark.driver.memory` default value is:
a) 512m  b) **1g**  c) 2g  d) 4g

**9.** A Spark job does: read.parquet → repartition(100) → groupBy.agg → show. How many stages?
a) 1  b) 2  c) **3**  d) 4

**10.** What does `spark.rpc.message.maxSize` NOT control?
a) Large RPC messages causing SparkException  b) Maximum message size between driver and executors  c) **Broadcast variable distribution**  d) Can be increased to handle larger messages

**11.** In the Spark UI, how are stages that read from cache displayed?
a) Completed  b) **Skipped**  c) Cached  d) Passed

**12.** Which is the correct Kubernetes container image config?
a) `spark.kubernetes.executor.image`  b) **`spark.kubernetes.container.image`**  c) `spark.kubernetes.docker.image`  d) `spark.container.image`

**13.** What is `spark.sql.autoBroadcastJoinThreshold` default?
a) 50 MB  b) 100 MB  c) **10 MB**  d) 200 MB

**14.** When `spark.executor.instances=10` and `spark.dynamicAllocation.enabled=true` are both set, what happens?
a) DRA is disabled; executor.instances wins  b) Both configs are used: min=0, max=10  c) **Warning logged; executor.instances ignored; DRA uses min/maxExecutors**  d) SparkException at startup

**15.** In a sort-merge join, which phase is most expensive?
a) **Shuffle READ (pulling partition data from all mappers)**  b) Local sort on each executor  c) Shuffle WRITE (mapping side)  d) Merge phase

**16.** [multi] Which of the following are true for `MEMORY_ONLY` eviction? *(select 3)*
a) **Evicted partition is dropped (not written to disk)**  b) **Evicted partition is recomputed from lineage if needed again**  c) **LRU policy selects eviction candidates**  d) Partition is serialized before eviction

**17.** `spark.memory.storageFraction` default is:
a) 0.3  b) 0.4  c) **0.5**  d) 0.6

**18.** What does `sc.setCheckpointDir()` require?
a) Any writable local directory  b) **Reliable distributed filesystem (HDFS, S3) accessible by all executors**  c) HDFS only (S3 not supported)  d) Network-attached storage on the driver

**19.** Which is true about pipelined transformations within one stage?
a) Each transformation creates a separate intermediate RDD  b) **Records flow through all narrow operators without intermediate materialisation**  c) Only SQL transformations are pipelined; DataFrame transforms are not  d) Pipelining requires WholeStageCodeGen to be explicitly enabled

**20.** `spark.reducer.maxReqsInFlight` controls:
a) **Max concurrent shuffle block fetch requests per reducer task**  b) Max concurrent executor connections per driver  c) Max in-flight RPC calls from driver to cluster manager  d) Max shuffle partitions processed before a spill

---

**Practice Test 1 Answer Key:**

| Q | A | Q | A | Q | A | Q | A |
|---|---|---|---|---|---|---|---|
| 1 | b | 6 | c | 11 | b | 16 | a,b,c |
| 2 | c | 7 | b | 12 | b | 17 | c |
| 3 | c | 8 | b | 13 | c | 18 | b |
| 4 | a,b,c | 9 | c | 14 | c | 19 | b |
| 5 | b | 10 | c | 15 | a | 20 | a |

**Score:** ___/20 · Target: ≥14

---

## PRACTICE TEST 2 — SQL (20 Questions)

**1.** `datediff('2024-07-10', '2024-07-01')` returns:
a) -9  b) **9**  c) DateType 9 days  d) 0

**2.** What type does `unix_timestamp()` (no arguments) return?
a) TimestampType  b) StringType  c) **LongType**  d) DoubleType

**3.** `trunc(date_col, 'month')` returns:
a) TimestampType truncated to first of month  b) **DateType truncated to first of month**  c) StringType like '2024-07'  d) IntegerType (month number)

**4.** `dayofweek('2024-01-07')` where Jan 7, 2024 is a Sunday returns:
a) 7  b) 0  c) **1**  d) 6

**5.** `locate("world", "hello world", 1)` returns:
a) 6  b) **7**  c) 0  d) 5

**6.** `sort_array(col, False)` sorts:
a) Ascending, nulls first  b) Descending, nulls last  c) **Descending, nulls first**  d) Ascending, nulls last

**7.** How does `array_sort(col)` place null elements?
a) **At the end (last)**  b) At the beginning (first)  c) Removes nulls  d) Raises an error

**8.** `nullif("error", "error")` returns:
a) "error"  b) ""  c) **NULL**  d) false

**9.** `stack(2, 'a', 1, 'b', 2)` produces:
a) One row: ('a', 1, 'b', 2)  b) **Two rows: ('a', 1) and ('b', 2)**  c) Four rows, one per value  d) A MapType column

**10.** `percentile_approx(col, 0.5)` uses which algorithm?
a) Full sort  b) **Greenwald–Khanna sketch**  c) HyperLogLog  d) T-Digest

**11.** `count_if(age > 18)` counts:
a) All rows with non-null age  b) **Only rows where age > 18 is TRUE**  c) Rows where age > 18 is TRUE or NULL  d) Rows where age is not null

**12.** `max_by(salary, start_date)` was introduced in:
a) Spark 2.4  b) **Spark 3.0**  c) Spark 3.2  d) Spark 3.4

**13.** [multi] Which are true about CTEs in Spark SQL?
a) **WITH clause defines a named subquery**  b) **Multiple CTEs supported in one WITH clause**  c) CTEs are always materialised to disk for performance  d) **Recursive CTEs (WITH RECURSIVE) not supported in Spark 3.5**

**14.** `F.conv("FF", 16, 10)` returns:
a) Integer 255 as IntegerType  b) **String "255" as StringType**  c) String "11111111" (binary)  d) NULL

**15.** `F.unhex(col)` returns:
a) LongType integer  b) **BinaryType**  c) StringType decoded string  d) IntegerType

**16.** `get_json_object('{"user":{"name":"Alice"}}', '$.user.name')` returns:
a) Struct with field name  b) **StringType "Alice"**  c) MapType  d) ArrayType

**17.** In the SQL WINDOW clause, where does `WINDOW w AS (...)` appear?
a) Before the FROM clause  b) After the WHERE clause but before GROUP BY  c) **At the end of the SELECT statement**  d) Inside the OVER clause directly

**18.** For ROLLUP(dept, team), `GROUPING_ID = 3` represents:
a) Both dept and team in the group key  b) Only dept in the group key  c) Only team in the group key  d) **Grand total (neither dept nor team in key)**

**19.** `nth_value(salary, 3)` returns:
a) The 3rd highest salary in the whole table  b) **The salary from the 3rd row of the current window frame; NULL if <3 rows in frame**  c) The third quartile of salary  d) The salary for employee #3

**20.** `date_trunc('hour', timestamp_col)` returns:
a) DateType truncated to the day  b) StringType in format 'YYYY-MM-DD HH'  c) **TimestampType truncated to the start of the hour**  d) LongType epoch truncated to nearest hour

---

**Practice Test 2 Answer Key:**

| Q | A | Q | A | Q | A | Q | A |
|---|---|---|---|---|---|---|---|
| 1 | b | 6 | c | 11 | b | 16 | b |
| 2 | c | 7 | a | 12 | b | 17 | c |
| 3 | b | 8 | c | 13 | a,b,d | 18 | d |
| 4 | c | 9 | b | 14 | b | 19 | b |
| 5 | b | 10 | b | 15 | b | 20 | c |

**Score:** ___/20 · Target: ≥14

---

## PRACTICE TEST 3 — DataFrame API (30 Questions)

**1.** `df.columns` returns:
a) A StructType schema  b) **A Python list of column name strings**  c) A dict of {name: type}  d) An iterator of Column objects

**2.** `df.transform(func)` calls:
a) func on each row  b) **func(df) and returns the resulting DataFrame**  c) func on each partition  d) func on a Pandas DataFrame representation

**3.** `df.toLocalIterator()` returns data how?
a) All partitions collected to driver at once  b) **One partition at a time to the driver**  c) As a Pandas DataFrame  d) As a lazy iterator that triggers per-element fetches

**4.** [multi] Which are true about `df.foreach` vs `df.foreachPartition`?
a) **foreach calls func once per Row**  b) **foreachPartition calls func once per partition with iterator**  c) Both return a new DataFrame  d) **foreachPartition more efficient for external connections**

**5.** `df.withColumnsRenamed({"old":"new"})` was introduced in Spark:
a) 3.2  b) 3.3  c) **3.4**  d) 3.5

**6.** `df.unpivot(ids, values, varCol, valCol)` transforms:
a) Long to wide format  b) **Wide to long format**  c) Transposes rows and columns  d) Drops value columns and encodes as JSON

**7.** `df.offset(10)` does:
a) Returns every 10th row  b) **Skips the first 10 rows**  c) Returns the 10th partition  d) Shifts row indices by 10

**8.** `saveAsTable` vs `insertInto` — which is true?
a) **saveAsTable uses DataFrame schema; insertInto uses column position**  b) Both are identical aliases  c) insertInto uses column names; saveAsTable uses position  d) saveAsTable always creates external (unmanaged) table

**9.** With `df.write.format("delta").mode("overwrite").save(path)` where DataFrame has a new column:
a) Delta auto-merges the new column  b) **Raises AnalysisException; fix with .option("overwriteSchema","true")**  c) Silently drops the new column  d) Stores new column values as NULL

**10.** `df.na.drop(thresh=2)` keeps rows that have:
a) Fewer than 2 null values  b) **At least 2 non-null values**  c) Exactly 2 non-null values  d) Fewer than 2 columns

**11.** `df.na.fill(0, subset=["age","score"])` fills:
a) All numeric nulls with 0  b) **Nulls in age and score columns only**  c) Rows matching the subset condition  d) A random 0%-100% sample of nulls

**12.** `F.raise_error("bad data")` when used as a column expression:
a) Logs a warning for each row  b) **Raises RuntimeException for every row where evaluated**  c) Returns the message string as a column value  d) Only raises at collect() time

**13.** `F.assert_true(condition, errMsg)` — which is NOT true?
a) Returns NULL when condition is true  b) Raises RuntimeException when condition is false  c) Can be used inside df.select()  d) **Is equivalent to a Python UDF with the same performance**

**14.** [multi] `F.hash(*cols)` vs `F.xxhash64(*cols)` — select all true:
a) **F.hash uses MurmurHash3, returns IntegerType**  b) **F.xxhash64 uses xxHash64, returns LongType**  c) F.xxhash64 is cryptographically secure  d) **Both are non-cryptographic, intended for partitioning/bucketing**

**15.** `F.conv("FF", 16, 10)` return type is:
a) IntegerType  b) LongType  c) **StringType**  d) DoubleType

**16.** `F.unhex("48656c6c6f")` returns:
a) The integer 48656c6c6f  b) **BinaryType bytes for "Hello"**  c) StringType "Hello"  d) NULL

**17.** `F.levenshtein(col1, col2)` return type is:
a) BooleanType  b) **IntegerType**  c) DoubleType  d) StringType

**18.** `F.soundex("Smyth")` returns:
a) `"S000"` — a standard Soundex code  b) **`"S530"` — same as soundex("Smith")**  c) BooleanType true if same pronunciation as reference  d) DoubleType similarity score

**19.** `F.reverse(array_col)` where array_col = [1,2,3] returns:
a) [1,2,3] (no change)  b) Raises AnalysisException  c) **[3,2,1]**  d) The last element only: 3

**20.** `F.format_string("%s has %d items", F.col("name"), F.col("count"))` returns:
a) A StructType  b) **StringType with printf-style substitution**  c) An error (column refs not allowed)  d) The literal format string unchanged

**21.** `df.schema.simpleString()` returns:
a) SQL DDL string like `` `id` INT ``  b) **Compact string like `struct<id:int,name:string>`**  c) JSON representation  d) Python dict

**22.** `df.schema.toDDL()` is useful for:
a) Logging schema for debugging  b) **Generating column definitions for CREATE TABLE statements**  c) Serialising schema to JSON  d) Comparing schemas between DataFrames

**23.** `F.to_csv(struct_col)` returns:
a) Writes CSV to disk, returns NULL  b) **StringType CSV-formatted string**  c) ArrayType of field values  d) BinaryType CSV bytes

**24.** `sort_array(col, asc=True)` vs `array_sort(col)` — null placement:
a) Both place nulls at the beginning  b) sort_array: nulls last; array_sort: nulls first  c) **sort_array: nulls first; array_sort: nulls last**  d) Both place nulls at the end

**25.** When reading CSV, `inferSchema=true` causes Spark to:
a) Infer schema lazily with zero extra cost  b) **Make two full passes over the data, doubling I/O**  c) Run schema inference only on the driver, not executors  d) Disable predicate pushdown

**26.** Which CSV option controls how NULL column values are written?
a) `emptyValue`  b) **`nullValue`**  c) Both are the same option  d) `naValue`

**27.** `df.mapInPandas(func, schema)` — what does func receive?
a) A Pandas DataFrame for the entire DataFrame  b) A single Row as a Pandas Series  c) **An iterator of Pandas DataFrames, one per partition**  d) A single Pandas DataFrame per group key

**28.** `F.struct(F.col("lat"), F.col("lon"))` returns a column of type:
a) `ArrayType([DoubleType, DoubleType])`  b) **`StructType([StructField("lat",...), StructField("lon",...)])`**  c) `MapType(StringType, DoubleType)`  d) `TupleType` with two elements

**29.** `df.show()` default truncation length is:
a) 10 characters  b) 50 characters  c) No truncation  d) **20 characters**

**30.** JDBC option `fetchsize` controls:
a) Max JDBC connections in parallel  b) **Rows fetched per round-trip from the database**  c) Max row size in bytes  d) Query timeout in seconds

---

**Practice Test 3 Answer Key:**

| Q | A | Q | A | Q | A | Q | A |
|---|---|---|---|---|---|---|---|
| 1 | b | 9 | b | 17 | b | 25 | b |
| 2 | b | 10 | b | 18 | b | 26 | b |
| 3 | b | 11 | b | 19 | c | 27 | c |
| 4 | a,b,d | 12 | b | 20 | b | 28 | b |
| 5 | c | 13 | d | 21 | b | 29 | d |
| 6 | b | 14 | a,b,d | 22 | b | 30 | b |
| 7 | b | 15 | c | 23 | b | | |
| 8 | a | 16 | b | 24 | c | | |

**Score:** ___/30 · Target: ≥21

---

## PRACTICE TEST 4 — Troubleshooting + Streaming + Connect + Pandas (40 Questions)

### Troubleshooting (10 Qs)

**T1.** `spark.sql.execution.arrow.pyspark.enabled=true` applies to:
a) GPU-accelerated SQL via RAPIDS  b) **toPandas(), createDataFrame(pandas_df), Pandas UDFs**  c) Parquet reads bypassing JVM  d) Shuffle data serialisation between executors

**T2.** What Python package must be installed to enable Arrow acceleration?
a) numpy  b) pandas  c) **pyarrow**  d) scipy

**T3.** Column pruning vs predicate pushdown — which is true?
a) They are the same optimisation  b) **Column pruning removes unused columns; predicate pushdown moves row filters to source — both can apply simultaneously**  c) Column pruning is physical; predicate pushdown is logical — they can't both apply  d) Column pruning = Parquet only; predicate pushdown = ORC only

**T4.** `spark.sql.broadcastTimeout=300` controls:
a) **How long driver waits for executors to receive a broadcast variable**  b) Maximum duration of any SQL query with a broadcast join  c) How long broadcast data is kept in executor memory  d) Timeout for ANALYZE TABLE when computing broadcast statistics

**T5.** Setting `spark.task.cpus=2` on an 8-core executor means:
a) **Only 4 tasks run concurrently per executor**  b) Tasks get 2x speed from parallelism  c) Executor requests 8 * 2 = 16 total cores  d) No change — cores per task has no effect on task count

**T6.** If `spark.sql.optimizer.maxIterations=100` is reached before convergence, Spark:
a) Throws PlanNotConvergedException and cancels  b) **Logs a warning and proceeds with best plan produced so far**  c) Reverts to unoptimised plan  d) Falls back to broadcast hash joins for all joins

**T7.** `spark.sql.files.ignoreMissingFiles=true` allows:
a) Skip empty partition directories  b) **Continue when files deleted between planning and execution**  c) Skip files with mismatched schemas  d) Suppress errors only during checkpoint recovery

**T8.** Off-heap memory — which is FALSE?
a) Enabled with offHeap.enabled=true and positive offHeap.size  b) Reduces GC pressure by allocating outside JVM heap  c) **Counted as part of spark.memory.fraction**  d) Not subject to JVM garbage collection

**T9.** `spark.shuffle.file.buffer=32k` setting affects:
a) Network receive buffer for shuffle fetch  b) Max shuffle partitions before spill  c) **In-memory write buffer per shuffle output file**  d) Total size of all shuffle files per executor

**T10.** AQE post-shuffle partition coalescing target size is configured by:
a) `spark.sql.adaptive.skewJoin.skewedPartitionFactor`  b) **`spark.sql.adaptive.advisoryPartitionSizeInBytes`**  c) `spark.sql.adaptive.autoBroadcastJoinThreshold`  d) `spark.sql.adaptive.localShuffleReader.enabled`

### Streaming (10 Qs)

**T11.** `trigger(availableNow=True)` vs `trigger(once=True)`:
a) Identical — availableNow is the new name for once  b) **availableNow uses multiple micro-batches respecting per-batch limits; once uses one mega-batch**  c) availableNow runs forever; once stops after one batch  d) availableNow = Kafka only; once = file sources only

**T12.** `query.inputRowsPerSecond` reports:
a) Rows fully processed and written to sink per second  b) **Source ingestion rate for the last micro-batch**  c) Average throughput since query start  d) Theoretical max throughput based on resources

**T13.** Streaming JSON read without providing a schema:
a) Spark infers schema by scanning all current files  b) **AnalysisException — explicit schema required**  c) Uses default schema: single StringType "value" column  d) Infers schema from first batch, updates dynamically

**T14.** [multi] Console sink — select all true:
a) **Writes to driver stdout**  b) **Development/testing only, not production**  c) **Supports append, update, and complete output modes**  d) Persists data durably and supports checkpoint recovery

**T15.** Event_time=10:03, watermark delay=5min, processing_time=10:20. What happens?
a) Event included in [10:00,10:10) window  b) **Event dropped — watermark ≈ 10:15, past end of [10:00,10:10) window**  c) Event assigned to next open window [10:10,10:20)  d) WatermarkViolationException thrown

**T16.** `session_window("event_time", "30 minutes")` creates:
a) Fixed 30-minute tumbling windows  b) **Dynamic gap-based sessions; new session when 30-min gap observed**  c) Sliding windows advancing 30 min per batch  d) Global window with 30-min late grace period

**T17.** The Kafka source DataFrame key column type is:
a) StringType  b) IntegerType  c) **BinaryType**  d) Inferred from message content

**T18.** When `kafka.group.id` is NOT set, Spark:
a) Raises an error — group.id is required  b) **Generates a unique group ID per query and manages offsets internally**  c) Uses round-robin partition assignment without a group  d) Falls back to direct partition assignment by offset

**T19.** `maxOffsetsPerTrigger` for Kafka controls:
a) Lifetime maximum messages to consume  b) **Max Kafka messages per micro-batch trigger**  c) Max Kafka partitions per executor per trigger  d) Max wait time before processing an empty batch

**T20.** [multi] `flatMapGroupsWithState` — select all true:
a) **Can emit 0 or more output rows per group**  b) **Supports processing-time and event-time timeouts**  c) **Requires append or update output mode (not complete)**  d) **State persisted in checkpoint; survives restarts**

### Spark Connect (5 Qs)

**T21.** In Spark Connect, when is an `AnalysisException` surfaced?
a) When the transformation method is called  b) **When an action (collect, show, count) is called**  c) When F.col("nonexistent") is created  d) Never — analysis errors are only logged on server

**T22.** Token-based authentication in Spark Connect URL:
a) `.option("token","my_token")` on the builder  b) **`sc://host:15002/;token=my_token`** embedded in URL  c) `SPARK_CONNECT_TOKEN` environment variable  d) Not supported in open-source Spark Connect

**T23.** Which scenario requires Spark Connect and would fail in classic PySpark?
a) Running `spark.sql("SELECT 1")` from any Python process  b) **Connecting to remote Spark from a client machine without Java installed**  c) Creating a UDF with `@udf(returnType=LongType())`  d) Reading `spark.read.parquet("s3://...")`

**T24.** [multi] UDFs in Spark Connect — select all true:
a) **UDFs registered via spark.udf.register() are serialised and sent to the server**  b) **External Python libs must be on executor environment, not client**  c) Python UDFs cannot be used — only SQL built-ins  d) **Arrow-optimised Pandas UDFs supported via Spark Connect**

**T25.** If the Spark Connect server crashes and restarts:
a) In-progress queries auto-replay from checkpoint  b) **Client process stays alive; queries lost; must reconnect and resubmit**  c) All client processes crash immediately  d) Server state preserved across restart via persistent state store

### Pandas API (5 Qs)

**T26.** How do you cache a pandas-on-Spark DataFrame?
a) `psdf.cache()`  b) **`psdf.spark.cache()`**  c) `psdf.to_spark().cache()` then reconvert  d) `ps.cache(psdf)` module-level function

**T27.** `psdf.spark.explain()` displays:
a) Pandas operation sequence  b) **Spark physical execution plan**  c) Memory usage per partition  d) SQL query that would be generated

**T28.** Default value of `ps.options.compute.default_index_type`:
a) `"sequence"` (globally ordered)  b) **`"distributed-sequence"` (fast, not strictly ordered)**  c) `"distributed"` (fastest, random)  d) `RangeIndex` (same as pandas)

**T29.** Which method writes a pandas-on-Spark DF to Delta?
a) `psdf.to_delta(path)` only  b) `psdf.to_spark().write.format("delta").save(path)` only  c) **Both a) and b) are valid**  d) `ps.write_delta(psdf, path)` module function only

**T30.** [multi] NaN vs NULL in Pandas-on-Spark — select all true:
a) **NaN in float cols is a distinct non-null value; NULL is the missing indicator**  b) fillna(0) fills both NULL and NaN  c) **dropna() drops NULL rows but NOT NaN rows**  d) **isna()/isnull() returns True for NULL, False for NaN**

---

**Practice Test 4 Answer Key:**

| Q | A | Q | A | Q | A |
|---|---|---|---|---|---|
| T1 | b | T11 | b | T21 | b |
| T2 | c | T12 | b | T22 | b |
| T3 | b | T13 | b | T23 | b |
| T4 | a | T14 | a,b,c | T24 | a,b,d |
| T5 | a | T15 | b | T25 | b |
| T6 | b | T16 | b | T26 | b |
| T7 | b | T17 | c | T27 | b |
| T8 | c | T18 | b | T28 | b |
| T9 | c | T19 | b | T29 | c |
| T10 | b | T20 | a,b,c,d | T30 | a,c,d |

**Score:** ___/40 · Target: ≥28

---

## PITFALLS MATRIX — 35 Traps by Topic

### Architecture Pitfalls (10)

| # | Wrong Assumption | Correct Fact |
|---|-----------------|-------------|
| A1 | `driver.memory` default = 2g | Default = **1g** |
| A2 | `autoBroadcastJoinThreshold` = 200 MB | Default = **10 MB** |
| A3 | AQE was off by default before 3.2 | **true since Spark 3.2** |
| A4 | DISK_ONLY partition failure → job fails | Spark **recomputes from lineage** |
| A5 | History Server needs `spark.ui.enabled=true` | NOT needed — only 3 eventLog configs |
| A6 | Broadcast limited by `rpc.message.maxSize` | Broadcast uses HTTP Torrent — **NOT subject to RPC limit** |
| A7 | Shuffle READ is cheaper than WRITE | **Shuffle READ is more expensive** (pulls from all mappers) |
| A8 | `executor.instances` wins when set with DRA | DRA **ignores** `executor.instances` |
| A9 | Locality order: ANY → NODE_LOCAL → PROCESS_LOCAL | **PROCESS_LOCAL → NODE_LOCAL → RACK_LOCAL → ANY** |
| A10 | `MEMORY_ONLY` eviction → written to disk | **Dropped entirely**, LRU, recomputed |

### SQL Pitfalls (10)

| # | Wrong Assumption | Correct Fact |
|---|-----------------|-------------|
| S1 | `unix_timestamp()` returns TimestampType | Returns **LongType** |
| S2 | `trunc` and `date_trunc` have same arg order | `trunc(col, fmt)` vs `date_trunc(fmt, col)` — **different** |
| S3 | `locate` is 0-based | **1-based**; returns 0 if not found |
| S4 | `sort_array(col, False)` = ascending | False = **descending** |
| S5 | `array_sort` and `sort_array` both put nulls first | `sort_array` = nulls first; `array_sort` = **nulls last** |
| S6 | `percentile_approx` with high accuracy = exact | `percentile_approx` is **always approximate** |
| S7 | `count_if` counts non-null values | Counts rows where condition = **TRUE** |
| S8 | CTEs always materialised to disk | **NOT always** — Catalyst typically inlines them |
| S9 | Recursive CTEs supported in Spark 3.4+ | **NOT supported through Spark 3.5** |
| S10 | `F.conv` returns IntegerType | Always returns **StringType** |

### DataFrame Pitfalls (10)

| # | Wrong Assumption | Correct Fact |
|---|-----------------|-------------|
| D1 | `df.transform(func)` = `F.transform(col, func)` | **Different**: `df.transform` is DataFrame-level; `F.transform` is array element-wise |
| D2 | `toLocalIterator` returns Pandas DataFrame | Returns Python **iterator of Row objects** |
| D3 | `insertInto` uses column names | Uses column **position** — dangerous |
| D4 | `assert_true` is a Python UDF | Native **Catalyst expression** (much faster) |
| D5 | `levenshtein` returns boolean or float | Returns **IntegerType** edit distance |
| D6 | `inferSchema=true` is zero-cost | **Two full passes** — doubles I/O |
| D7 | CSV `sep` valid, `delimiter` is not | **Both are valid aliases** |
| D8 | Delta overwrite silently handles schema | Raises **AnalysisException**; need `overwriteSchema=true` |
| D9 | `na.drop(thresh=2)` drops rows with >2 nulls | Drops rows with **fewer than 2 non-null** values |
| D10 | `mapInPandas` is like `applyInPandas` | `mapInPandas` = partition-level; `applyInPandas` = group-level |

### Streaming/Connect/Pandas Pitfalls (5)

| # | Wrong Assumption | Correct Fact |
|---|-----------------|-------------|
| P1 | Streaming schema inference works for JSON files | **AnalysisException** — must provide explicit schema |
| P2 | `trigger(availableNow=True)` runs forever | Processes backlog across multiple batches, **then stops** |
| P3 | `flatMapGroupsWithState` uses complete output mode | Only **append or update** (NOT complete) |
| P4 | `psdf.cache()` is valid | Must use **`psdf.spark.cache()`** |
| P5 | `psdf.dropna()` drops NaN rows | Drops **NULL** rows; **NaN** is NOT dropped by dropna() |

---

## MULTI-ANSWER STRATEGY

**22 of 100 questions** are multi-answer (`many`). Identify them early — they tend to cluster around:
- Architecture: Q4, Q7, Q10, Q18
- SQL: Q32, Q39
- DataFrame: Q46, Q57, Q69
- Troubleshooting: Q78
- Streaming: Q84, Q90
- Connect: Q94
- Pandas: Q100

**Multi-answer heuristics:**
- "Select all that apply" = eliminate clearly wrong options first
- Absolutes like "always", "never", "only", "cannot" are usually wrong
- Options saying things ARE identical/interchangeable are usually wrong
- Look for complementary pairs that are BOTH correct (column pruning + predicate pushdown; hash = int + xxhash64 = long)

---

## EXAM DAY STRATEGY

### Timing

```
100 questions, 120 minutes = 1.2 min/question
First pass: 60 min (mark all uncertain)
Review pass: 45 min (uncertain questions + multi-answer)
Buffer: 15 min (final check)
```

### Question Triage

| Type | Action |
|------|--------|
| Know immediately | Answer and move on (30 sec) |
| 2 options remaining | Pick better one, flag for review |
| All options wrong | Re-read question stem carefully; flag |
| Multi-answer | Eliminate impossible options first |

### Common Tells in Wrong Answers

- "always" / "never" / "only" → usually wrong
- "equivalent to", "identical to", "interchangeable" → usually wrong
- "raises an error" when result is just a warning → usually wrong
- "no performance difference" when there clearly is one → usually wrong
- The answer that sounds most complex/clever → often a trap

### Topic Order Priority

1. **DataFrame (30%)** — score the most questions here
2. **Architecture (20%)** — high weight, testable defaults
3. **SQL (20%)** — function knowledge, return types
4. **Streaming (10%)** — know the gotchas (schema, watermark, Kafka)
5. **Troubleshooting (10%)** — Arrow, AQE, off-heap
6. **Connect (5%)** — focus on 5 anchors only
7. **Pandas (5%)** — focus on NaN vs NULL, spark accessor

### Score Bands

| Score | Status | Action |
|-------|--------|--------|
| ≥85 | Excellent | Ready |
| 75–84 | Good | Review weak topics, sit exam |
| 70–74 | Borderline | One more week; review pitfalls matrix |
| 60–69 | Not ready | Focus on DataFrame + Architecture |
| <60 | Need more prep | Restart Week 2 |

---

*Do not overwrite this file — it is part of the Iteration 5 study library.*
