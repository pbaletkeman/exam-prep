# PRACTICE STRATEGY — Iteration 4
# Databricks Certified Associate Developer for Apache Spark

**Iteration**: 4 | 100 Questions | 20 Easy / 60 Medium / 20 Hard
**Answer Mix**: 78 single-answer / 22 multi-answer
**Topic Weights**: Architecture 20% · SQL 20% · DataFrame 30% · Troubleshooting 10% · Streaming 10% · Connect 5% · Pandas 5%

---

## SECTION 1: 4-WEEK DAILY STUDY PLAN

### Week 1 — Architecture & SQL Foundation

| Day | Focus | Activity | Time |
|-----|-------|----------|------|
| Mon | Architecture Core | Read Study Guide §1.1–1.5 (spark-submit, YARN modes, History Server, HashPartitioner, Storage Levels, task failures) | 45 min |
| Tue | Architecture Deep | Study Guide §1.6–1.11 (file configs, DRA, executor memory layout, shuffle spill, warehouse.dir, Thrift Server) | 45 min |
| Wed | Architecture Advanced | Study Guide §1.12–1.16 (stage boundaries, Hive metastore, TaskSetManager, extraJavaOptions, heartbeat vs timeout) | 45 min |
| Thu | SQL Strings & Dates | Study Guide §2.1–2.2 (regexp_extract, instr, substring_index, translate, format_number, overlay, date_trunc, from_unixtime, to_utc_timestamp) | 45 min |
| Fri | SQL Arrays/Maps/Windows | Study Guide §2.3–2.5 (size(null), arrays_overlap, map_from_arrays, map_concat right-wins, ROWS vs RANGE) | 45 min |
| Sat | SQL Set Operations | Study Guide §2.6–2.7 (ROLLUP/CUBE, EXCEPT ALL, INTERSECT ALL, TABLESAMPLE, QUALIFY) | 45 min |
| Sun | Week 1 Review | Quick Reference anchors A1–A10; write out all 10 from memory | 30 min |

### Week 2 — DataFrame API & Troubleshooting

| Day | Focus | Activity | Time |
|-----|-------|----------|------|
| Mon | DataFrame Write | Study Guide §3.1–3.2 (column ambiguity, Parquet write options, maxRecordsPerFile, write.text, CSV headers) | 45 min |
| Tue | DataFrame Read | Study Guide §3.3 (nullValue, pathGlobFilter, Parquet schema, load() format, JDBC dbtable subquery) | 45 min |
| Wed | DataFrame Functions | Study Guide §3.4 (input_file_name, schema.json, broadcast import, df.rdd returns Rows, withColumn behavior, F.coalesce) | 45 min |
| Thu | DataFrame Advanced | Study Guide §3.5–3.11 (StructType equality, @pandas_udf, applyInPandas, getNumPartitions, write.jdbc table, read.jdbc parallelism) | 45 min |
| Fri | Troubleshooting | Study Guide §4.1–4.7 (broadcast disable=-1, ANALYZE TABLE, CACHE TABLE eager, advisoryPartitionSizeInBytes, ORC vs Parquet, CBO two configs, explain modes) | 45 min |
| Sat | Practice Test 1 | Architecture + SQL focus (40 Q) | 60 min |
| Sun | Review Test 1 | Score, identify gaps, re-study weak areas | 30 min |

### Week 3 — Streaming, Connect & Pandas

| Day | Focus | Activity | Time |
|-----|-------|----------|------|
| Mon | Streaming Triggers & Modes | Study Guide §5.1–5.3 (trigger once, checkpointLocation, append/update/complete modes, complete requires agg) | 45 min |
| Tue | Streaming Windowing | Study Guide §5.4–5.5 (5-min tumbling windows, foreachBatch multi-sink, withWatermark ordering) | 45 min |
| Wed | Streaming Monitoring | Study Guide §5.6–5.9 (failOnDataLoss, recentProgress=list of dicts, StreamingQueryListener, all 5 withWatermark rules) | 45 min |
| Thu | Spark Connect | Study Guide §6.1–6.4 (SPARK_REMOTE env var, Arrow serialization, proxy session, DatabricksSession.serverless, Connect vs submit) | 45 min |
| Fri | Pandas API on Spark | Study Guide §7.1–7.4 (ps.sql, two Parquet read paths, apply axis=1, rolling(3) NaN, ps.concat rules) | 45 min |
| Sat | Practice Test 2 | SQL + DataFrame focus (50 Q) | 75 min |
| Sun | Review Test 2 | Score, focus on multi-answer questions | 30 min |

### Week 4 — Integration & Exam Simulation

| Day | Focus | Activity | Time |
|-----|-------|----------|------|
| Mon | Trap Review | Work through all 25 traps in Study Guide trap table; verify each without looking at answer | 45 min |
| Tue | Practice Test 3 | Troubleshooting + Streaming + Connect + Pandas (60 Q) | 90 min |
| Wed | Review Test 3 | Score analysis; drill failing areas | 45 min |
| Thu | Quick Reference Anchors | Write all 35 anchors A1–A35 from memory; score < 30: re-study topic | 30 min |
| Fri | Full Simulation | Practice Test 4 (100 Q, 120-minute timer) | 120 min |
| Sat | Final Review | Score by topic; re-read trap table; review 10-Point Checklist | 45 min |
| Sun | Exam Day Prep | Light review of Quick Reference Part 2 (configs) and Part 7 (set operations) | 20 min |

---

## SECTION 2: PRACTICE TEST 1 — Architecture & SQL Focus (40 Questions)

**Target time**: 48 minutes (72 seconds per question)
**Passing goal**: 30/40 (75%)

### Architecture Questions (20)

**Q1.** Which spark-submit flag distributes a Python utility module so it is importable by executor tasks?
- A) `--files`
- B) `--py-files`
- C) `--jars`
- D) `--packages`

**Q2.** What is the default port for the Spark History Server Web UI?
- A) 4040
- B) 7077
- C) 8080
- D) **18080**

**Q3.** A team submits a Spark job in YARN cluster mode. Where does the Spark Driver run?
- A) On the machine that submitted the job (the client)
- B) On the ResourceManager node
- C) **Inside the ApplicationMaster container on a worker node**
- D) On any available NodeManager

**Q4.** An RDD is produced by calling `rdd.groupByKey()`. Which partitioner is attached to the resulting RDD?
- A) None
- B) **HashPartitioner(spark.default.parallelism)**
- C) RangePartitioner
- D) HashPartitioner(rdd.getNumPartitions())

**Q5.** Storage level `MEMORY_ONLY_2` creates:
- A) Two storage tiers: memory first, then disk on overflow
- B) A memory copy plus a compressed replica
- C) **Two replicated copies of each partition across two separate executors**
- D) Two partitions from each original partition

**Q6.** `spark.task.maxFailures = 4` means:
- A) A task can retry 4 times (5 total attempts)
- B) **A task can fail a total of 4 times before the job is aborted**
- C) The stage fails after 4 task failures across all tasks
- D) Each task is allowed 4 retries in addition to the initial attempt

**Q7.** What does `spark.sql.files.openCostInBytes` control?
- A) The maximum size of any single partition
- B) The chunk size for reading large files
- C) **The estimated cost per file opening, used to co-locate small files into the same partition**
- D) The maximum file size Spark will attempt to read

**Q8.** Dynamic Resource Allocation bounding configurations are: *(Multi)*
- A) `spark.dynamicAllocation.minExecutors`
- B) `spark.dynamicAllocation.maxExecutors`
- C) `spark.dynamicAllocation.lowerBound`
- D) `spark.dynamicAllocation.upperBound`

**Q9.** Spark internally reserves how much of the executor JVM heap for system overhead before applying `spark.memory.fraction`?
- A) 512 MB
- B) **300 MB**
- C) 256 MB
- D) 10% of total memory

**Q10.** When does Spark write shuffle spill files to disk? *(Multi)*
- A) When `spark.sql.files.maxPartitionBytes` is exceeded
- B) **When the execution memory buffer is full**
- C) When the number of partitions exceeds `spark.default.parallelism`
- D) **When execution memory is exhausted and cannot borrow from storage memory**

**Q11.** Default value of `spark.sql.warehouse.dir`:
- A) `/tmp/spark-warehouse`
- B) `/user/hive/warehouse`
- C) `/var/spark/warehouse`
- D) **`spark-warehouse` in the current working directory**

**Q12.** Which statement about Spark Thrift Server is correct?
- A) It exposes Spark APIs via a REST endpoint
- B) **It is a HiveServer2-compatible JDBC/ODBC gateway to Spark SQL**
- C) It provides the Web UI for monitoring running applications
- D) It stores structured streaming checkpoints

**Q13.** Which transformation introduces a stage boundary?
- A) `filter()`
- B) `map()`
- C) **`repartition()`**
- D) `coalesce()`

**Q14.** The requirement for `spark.executor.heartbeatInterval` relative to `spark.network.timeout` is:
- A) They should be equal
- B) `heartbeatInterval` should be greater than `network.timeout`
- C) **`heartbeatInterval` must be significantly less than `network.timeout`**
- D) There is no relationship between these two configs

**Q15.** Which config correctly specifies the Spark Driver's maximum serialized task result size that can be sent back?
- A) `spark.driver.maxResultSize`
- B) `spark.task.maxResultSize`
- C) `spark.executor.maxResultSize`
- D) `spark.result.maxBytes`

**Q16.** A temporary view created with `createOrReplaceTempView` is:
- A) Persisted in the Hive metastore and visible across sessions
- B) Stored in HDFS under `spark.sql.warehouse.dir`
- C) **Session-scoped and NOT stored in the Hive metastore**
- D) Automatically converted to a global temp view

**Q17.** `spark.executor.extraJavaOptions` is used to:
- A) Add Python packages to executor Python environments
- B) **Pass extra JVM flags to executor JVM processes**
- C) Set additional classpath entries for executor JVMs
- D) Configure native library paths for executors

**Q18.** What does `TaskSetManager` do? *(Multi)*
- A) **Tracks which tasks in a Stage have succeeded, failed, or are pending**
- B) **Manages task retries up to `spark.task.maxFailures`**
- C) Converts logical plans into physical stages
- D) Negotiates executor containers from the cluster manager

**Q19.** The `spark.sql.files.maxPartitionBytes` config default is:
- A) 64 MB
- B) **128 MB**
- C) 256 MB
- D) 512 MB

**Q20.** In a Spark standalone cluster, worker nodes register with the Master on port:
- A) 4040
- B) **7077**
- C) 8080
- D) 18080

### SQL Questions (20)

**Q21.** `regexp_extract('2024-07-15', '(\d{4})-(\d{2})-(\d{2})', 2)` returns:
- A) `'2024'`
- B) **`'07'`**
- C) `'15'`
- D) `'2024-07-15'`

**Q22.** `instr('Apache Spark', 'Spark')` returns:
- A) 6
- B) **8**
- C) 7
- D) 0

**Q23.** `size(null)` in Spark 3+ returns:
- A) 0
- B) -1
- C) **null**
- D) Throws NullPointerException

**Q24.** `substring_index('a.b.c.d', '.', -2)` returns:
- A) `'a.b'`
- B) `'b.c.d'`
- C) **`'c.d'`**
- D) `'a.b.c'`

**Q25.** `format_number(1234567.891, 2)` returns:
- A) `1234567.89` (Double)
- B) **`'1,234,567.89'` (String)**
- C) `'1234567.89'` (String without commas)
- D) `1,234,567.89` (Double with formatting)

**Q26.** `from_unixtime(1000000000)` returns:
- A) A TimestampType value
- B) A DateType value
- C) **A StringType value in 'yyyy-MM-dd HH:mm:ss' format**
- D) A LongType epoch seconds value

**Q27.** `date_trunc('month', '2024-07-15')` returns:
- A) **`2024-07-01 00:00:00`**
- B) `2024-07-15 00:00:00`
- C) `2024-01-01 00:00:00`
- D) `2024-07-31 23:59:59`

**Q28.** `arrays_overlap(array(1, 2, 3), array(3, 4, 5))` returns:
- A) `false`
- B) **`true`**
- C) `null`
- D) `array(3)`

**Q29.** When `map_concat(map('a', 1, 'b', 2), map('b', 10, 'c', 3))` is called, the value for key `'b'` is:
- A) 2 (left wins)
- B) **10 (right wins)**
- C) Error — duplicate keys are not allowed
- D) null

**Q30.** `ROLLUP(region, country)` produces how many grouping sets?
- A) 2
- B) **3**
- C) 4
- D) 5

**Q31.** `CUBE(region, country)` produces how many grouping sets?
- A) 2
- B) 3
- C) **4**
- D) 5

**Q32.** Table `t` has rows: `(1),(1),(2)`. `t EXCEPT ALL (SELECT 1)` returns:
- A) `(2)` only (removes all 1s)
- B) `(1),(2)` **(removes one occurrence of 1, keeps the other)**
- C) Empty
- D) `(1),(1),(2)` (no change)

**Q33.** The QUALIFY clause is available starting in which Spark version?
- A) Spark 3.0
- B) Spark 3.2
- C) Spark 3.3
- D) **Spark 3.4**

**Q34.** `overlay('Spark SQL', 'DataFrame', 7)` returns:
- A) `'DataFrame SQL'`
- B) `'Spark DataFrame'`
- C) `'Spark DaSQLrame'`
- D) `'Spark SQLDataFrame'`

**Q35.** `to_utc_timestamp(ts, 'America/New_York')`:
- A) Treats `ts` as UTC and converts to New York time
- B) **Treats `ts` as New York local time and converts to UTC**
- C) Returns the UTC offset of New York timezone
- D) Adds the UTC offset to `ts` without timezone conversion

**Q36.** Which window frame specification counts the **exact** physical preceding row, not all rows with the same ORDER BY value?
- A) **`ROWS BETWEEN 1 PRECEDING AND CURRENT ROW`**
- B) `RANGE BETWEEN 1 PRECEDING AND CURRENT ROW`
- C) `ROWS BETWEEN CURRENT ROW AND 1 FOLLOWING`
- D) `RANGE BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW`

**Q37.** `TABLESAMPLE (10 PERCENT)` samples approximately 10% using:
- A) Reservoir sampling (exact count)
- B) Random row ID generation
- C) **A probabilistic/approximate random sample of rows**
- D) A top 10% slice by primary key

**Q38.** `INTERSECT ALL` vs `INTERSECT DISTINCT`: Which is true?
- A) They always return the same rows
- B) `INTERSECT ALL` returns only distinct rows
- C) `INTERSECT DISTINCT` can return MORE rows than `INTERSECT ALL`
- D) **`INTERSECT ALL` preserves duplicates up to the minimum occurrence count in both sides**

**Q39.** `add_months('2024-01-31', 1)` returns:
- A) `2024-02-31` (invalid — throws exception)
- B) `2024-03-02` (carries over)
- C) **`2024-02-29` (month-end adjustment for 2024 leap year)**
- D) `2024-02-28` (truncated)

**Q40.** Which correctly uses QUALIFY to keep only the row with the highest salary per department?
- A) `SELECT * FROM employees WHERE RANK() OVER (...) = 1`
- B) **`SELECT * FROM employees QUALIFY RANK() OVER (PARTITION BY dept ORDER BY salary DESC) = 1`**
- C) `SELECT * FROM employees HAVING RANK() OVER (...) = 1`
- D) `SELECT *, RANK() OVER (...) AS rk FROM employees QUALIFY rk = 1`

### Practice Test 1 — Answer Key

| Q | A | Q | A | Q | A | Q | A |
|---|---|---|---|---|---|---|---|
| 1 | B | 11 | D | 21 | B | 31 | C |
| 2 | D | 12 | B | 22 | B | 32 | B |
| 3 | C | 13 | C | 23 | C | 33 | D |
| 4 | B | 14 | C | 24 | C | 34 | B |
| 5 | C | 15 | A | 25 | B | 35 | B |
| 6 | B | 16 | C | 26 | C | 36 | A |
| 7 | C | 17 | B | 27 | A | 37 | C |
| 8 | A,B | 18 | A,B | 28 | B | 38 | D |
| 9 | B | 19 | B | 29 | B | 39 | C |
| 10 | B,D | 20 | B | 30 | B | 40 | B |

**Score**: __/40 | Passing: 30+ | Strength topics: ___ | Weak topics: ___

---

## SECTION 3: PRACTICE TEST 2 — SQL & DataFrame Focus (50 Questions)

**Target time**: 60 minutes (72 seconds per question)
**Passing goal**: 38/50 (75%)

### SQL Questions (20)

**Q1.** `translate('Hello World', 'lo', '*-')` returns:
- A) `'He**- W-r*d'`
- B) **`'He**- W*r-d'`**
- C) `'He**-W*r-d'`
- D) `'H*l-* W*r-d'`

**Q2.** `map_from_arrays(array('x','y'), array(10, 20))` returns:
- A) `array(struct('x',10), struct('y',20))`
- B) **`map('x',10,'y',20)`**
- C) `struct('x':10, 'y':20)`
- D) `array(map('x',10), map('y',20))`

**Q3.** Which of the following correctly uses TABLESAMPLE?
- A) `SELECT * FROM orders SAMPLE 10 PERCENT`
- B) `SELECT * FROM orders LIMIT 10%`
- C) **`SELECT * FROM orders TABLESAMPLE (10 PERCENT)`**
- D) `SELECT * FROM orders WHERE RAND() < 0.10`

**Q4.** `ROLLUP(a, b)` produces which grouping sets? *(Multi)*
- A) **`(a, b)`**
- B) **`(a)`**
- C) **`()`**
- D) `(b)`

**Q5.** `CUBE(a, b)` produces which grouping sets? *(Multi)*
- A) **`(a, b)`**
- B) **`(a)`**
- C) **`(b)`**
- D) **`()`**

**Q6.** Which function returns a 1-based integer position, returning 0 if the substring is not found?
- A) `substring()`
- B) **`instr()`**
- C) `position()`
- D) `find()`

**Q7.** `overlay('Hello World', 'Spark', 7, 5)` replaces starting at position 7 with length 5. Result:
- A) `'Hello Spark'`
- B) **`'Hello Spark'`** (same here — 'World' is replaced by 'Spark')
- C) `'HelloSpark World'`
- D) Throws an exception — overlay requires 3 arguments

**Q8.** Which statement about `INTERSECT ALL` is true?
- A) It always returns distinct rows
- B) It is equivalent to `INTERSECT DISTINCT`
- C) **It preserves duplicate rows up to the minimum count in both relations**
- D) It was added in Spark 3.4

**Q9.** In which Spark 3 version was `INTERSECT ALL` added?
- A) Spark 3.4
- B) Spark 3.3
- C) Spark 3.2
- D) **Spark 3.0**

**Q10.** A QUALIFY clause without a window function in the expression:
- A) Works — it filters rows by an arbitrary condition
- B) Works — it filters using the last window function in SELECT
- C) **Is invalid — QUALIFY requires a window function expression**
- D) Falls back to HAVING semantics

### SQL Answers (Q1–Q10)

| Q | A | Notes |
|---|---|-------|
| 1 | B | l→* and o→- so Hello→He**- , World→W*r-d |
| 2 | B | map_from_arrays creates a map |
| 3 | C | TABLESAMPLE is the correct syntax |
| 4 | A,B,C | ROLLUP(a,b) = (a,b),(a),() — NOT (b) |
| 5 | A,B,C,D | CUBE(a,b) = (a,b),(a),(b),() |
| 6 | B | instr() is 1-based, 0 if not found |
| 7 | A | Replaces chars 7-11 ('World') with 'Spark' |
| 8 | C | INTERSECT ALL preserves duplicates |
| 9 | D | Both INTERSECT ALL and EXCEPT ALL added in Spark 3.0 |
| 10 | C | QUALIFY must reference a window function |

### DataFrame Questions (30)

**Q11.** After joining `df1` and `df2` where both have a column `status`, which code resolves the ambiguity?
- A) `joined.select(F.col('status'))` — works fine
- B) `joined.select('status')` — works fine
- C) **`joined.select(df1['status'], df2['status'])`** — explicit DataFrame references
- D) `joined.select(F.col('df1.status'), F.col('df2.status'))` — with backticks

**Q12.** Which code correctly writes a DataFrame to Parquet with Snappy compression?
- A) `df.write.parquet('/out', compression='snappy')`
- B) **`df.write.option('compression', 'snappy').parquet('/out')`**
- C) `df.write.option('codec', 'snappy').parquet('/out')`
- D) `df.write.format('parquet').snappy('/out')`

**Q13.** `write.text()` fails when the DataFrame:
- A) Has more than 1 million rows
- B) Has string columns with null values
- C) **Has more than one column, or any column that is not StringType**
- D) Has no primary key column

**Q14.** Which option reads only Parquet files from a mixed directory?
- A) `spark.read.option('fileExtension', '.parquet').load('/dir')`
- B) **`spark.read.option('pathGlobFilter', '*.parquet').load('/dir')`**
- C) `spark.read.option('includeOnly', 'parquet').load('/dir')`
- D) `spark.read.parquet('/dir', filterExtension=True)`

**Q15.** `F.coalesce(col1, col2, col3)` returns:
- A) The sum of all non-null values
- B) **The first non-null value from left to right**
- C) The most common non-null value
- D) A Column that replaces all nulls with zero

**Q16.** `df1.exceptAll(df2)` vs `df1.subtract(df2)`:
- A) They are functionally identical
- B) **`exceptAll` preserves extra duplicates from df1; `subtract` removes all occurrences of matching rows**
- C) `subtract` is more efficient because it avoids a shuffle
- D) `exceptAll` is not available in PySpark

**Q17.** `df.withColumn('existing_col', new_expr)` when `existing_col` already exists:
- A) Raises AnalysisException — cannot overwrite
- B) Creates a duplicate column named `existing_col`
- C) **Replaces the existing column in place**
- D) Adds a new column with an auto-generated suffix

**Q18.** Which returns `true`?

```python
s1 = StructType([StructField('a', IntegerType(), True)])
s2 = StructType([StructField('a', IntegerType(), True)])
s1 == s2
```

- A) False — different object references
- B) **True — StructType uses value-based equality**
- C) Raises TypeError
- D) False — StructType does not implement `__eq__`

**Q19.** `df.rdd` returns:
- A) An RDD of `dict` objects
- B) An RDD of `tuple` objects
- C) **An RDD of `Row` objects**
- D) An RDD of `list` objects

**Q20.** `applyInPandas` invokes the function:
- A) Once per row with a pd.Series
- B) Once per partition with a pd.DataFrame
- C) **Once per group with a pd.DataFrame**
- D) Once per column with a pd.Series

**Q21.** Correct import for the `broadcast` hint function:
- A) `from pyspark.sql import broadcast`
- B) **`from pyspark.sql.functions import broadcast`**
- C) `from pyspark.sql.hints import broadcast`
- D) `from pyspark import broadcast`

**Q22.** `schema.json()` returns:
- A) A Python dict representing the schema
- B) **A JSON string representation of the StructType**
- C) Raises AttributeError — use `schema.toJson()` instead
- D) A formatted multi-line JSON string (same as prettyJson)

**Q23.** To get the partition count of a DataFrame:
- A) `df.getNumPartitions()` — direct method
- B) `df.partitionCount()` — standard method
- C) **`df.rdd.getNumPartitions()`** — via RDD
- D) `df.numPartitions` — property access

**Q24.** `df.write.jdbc(url, ???, mode='overwrite', properties=props)` — the second positional argument name is:
- A) `dbtable`
- B) `tableName`
- C) `targetTable`
- D) **`table`**

**Q25.** Which two options enable parallel reading in `read.jdbc()`? *(Multi)*
- A) **`numPartitions + partitionColumn + lowerBound + upperBound`**
- B) `fetchsize` — fetch batch size
- C) **`predicates` — list of WHERE clause strings**
- D) `batchsize` — write batch size

**Q26.** `df.selectExpr('salary * 1.1 AS adjusted_salary')` is equivalent to:
- A) `df.select('salary * 1.1').alias('adjusted_salary')`
- B) **`df.select((F.col('salary') * 1.1).alias('adjusted_salary'))`**
- C) `df.withColumnRenamed('salary', 'adjusted_salary')`
- D) `df.filter('salary * 1.1')`

**Q27.** `F.when(F.col('score') >= 90, 'A').when(F.col('score') >= 80, 'B')` for score=75:
- A) Returns `'C'`
- B) Returns `''` (empty string)
- C) Raises ValueError — must always end with `.otherwise()`
- D) **Returns `null` (implicit `.otherwise(None)`)**

**Q28.** `sdf.to_pandas_on_spark()` returns:
- A) A `pandas.DataFrame` collected on the driver
- B) **A `pyspark.pandas.DataFrame` (distributed)**
- C) A Spark DataFrame with Pandas-style indexing
- D) A Pandas Series

**Q29.** CSV write: headers are written by default?
- A) Yes
- B) **No — must explicitly set `.option('header', True)`**
- C) Only when the DataFrame has named columns
- D) Only in overwrite mode

**Q30.** Which creates a DataFrame in append mode from a list of Row objects?
- A) `spark.createDataFrame(Row(a=1), Row(a=2))`
- B) **`spark.createDataFrame([Row(a=1), Row(a=2)])`**
- C) `spark.sql("SELECT 1 AS a UNION ALL SELECT 2")`
- D) `sc.parallelize([Row(a=1), Row(a=2)]).toDF()`

**Q31.** `cache().count()` pattern:
- A) `cache()` is eager — data is materialized immediately on cache() call
- B) **`cache()` is lazy — `count()` triggers the action that materializes data in memory**
- C) `count()` returns None when used after `cache()`
- D) Data is cached after the NEXT action following `count()`

**Q32.** Which Parquet write option limits the maximum number of rows per output file?
- A) `partitionSize`
- B) `rowsPerFile`
- C) **`maxRecordsPerFile`**
- D) `fileRecordLimit`

**Q33.** `coalesce(1)` vs `repartition(1)`:
- A) Equivalent — both reduce to 1 partition
- B) **`coalesce(1)` has no shuffle; `repartition(1)` does a full shuffle**
- C) `repartition(1)` is the preferred method to avoid data skew
- D) `coalesce(1)` performs a partial shuffle

**Q34.** Which correctly reads Parquet with format specified as a keyword argument?
- A) `spark.read.parquet('/path').format('parquet')`
- B) `spark.read.format('parquet').load()` (missing path)
- C) **`spark.read.load('/path', format='parquet')`**
- D) `spark.read.load('/path').setFormat('parquet')`

**Q35.** A CSV has `"N/A"` strings for missing values. The correct read option is:
- A) `.option('na', 'N/A')`
- B) `.option('missingValue', 'N/A')`
- C) `.option('emptyValue', 'N/A')`
- D) **`.option('nullValue', 'N/A')`**

**Q36.** `F.input_file_name()` returns:
- A) The Spark application name
- B) The HDFS root of the dataset
- C) **The source file path for each row**
- D) The partition file that wrote the row (output side)

**Q37.** The correct decorator syntax for a Pandas UDF returning DoubleType is:
- A) `@udf(returnType=DoubleType())`
- B) **`@pandas_udf(returnType=DoubleType())`**
- C) `@vectorized_udf(DoubleType())`
- D) `@spark.udf.register(DoubleType())`

**Q38.** Parquet schema inference reads the schema from:
- A) The first row of each file
- B) A separate `.schema` metadata file
- C) A statistical sample of rows
- D) **The file footer metadata**

**Q39.** The `mergeSchema` option for plain Parquet:
- A) Is a valid write option that merges all partition schemas
- B) Must be set on both read and write sides
- C) **Is a read option only — Spark uses it to unify schemas across Parquet files**
- D) Is the same as `enforceSchema`

**Q40.** `F.when()` with multiple conditions, no otherwise: for unmatched rows, the column value is:
- A) `0` (numeric default)
- B) `''` (empty string)
- C) Raises a runtime error
- D) **`null`**

### Practice Test 2 — Answer Key (Full 50 Questions)

**SQL (Q1–Q10):** See earlier answer key in this section.

**DataFrame (Q11–Q40):**

| Q | A | Q | A | Q | A | Q | A |
|---|---|---|---|---|---|---|---|
| 11 | C | 21 | B | 31 | B | -- | -- |
| 12 | B | 22 | B | 32 | C | -- | -- |
| 13 | C | 23 | C | 33 | B | -- | -- |
| 14 | B | 24 | D | 34 | C | -- | -- |
| 15 | B | 25 | A,C | 35 | D | -- | -- |
| 16 | B | 26 | B | 36 | C | -- | -- |
| 17 | C | 27 | D | 37 | B | -- | -- |
| 18 | B | 28 | B | 38 | D | -- | -- |
| 19 | C | 29 | B | 39 | C | -- | -- |
| 20 | C | 30 | B | 40 | D | -- | -- |

**Score**: __/50 | Passing: 38+ | Time used: ___

---

## SECTION 4: PRACTICE TEST 3 — Troubleshooting, Streaming, Connect & Pandas (30 Questions)

**Target time**: 36 minutes
**Passing goal**: 23/30 (75%)

**Q1.** To completely disable automatic broadcast joins:
- A) `spark.sql.autoBroadcastJoinThreshold = 0`
- B) `spark.sql.broadcastJoin.enabled = false`
- C) **`spark.sql.autoBroadcastJoinThreshold = -1`**
- D) `spark.sql.broadcast.disabled = true`

**Q2.** To enable CBO join reorder, which TWO configs are required? *(Multi)*
- A) **`spark.sql.cbo.enabled = true`**
- B) **`spark.sql.cbo.joinReorder.enabled = true`**
- C) `spark.sql.optimizer.joinReorder = true`
- D) `spark.sql.adaptive.enabled = true`

**Q3.** `CACHE TABLE sales` vs `CACHE LAZY TABLE sales`:
- A) Both are lazy — cache is populated on first query
- B) **`CACHE TABLE` is eager (scans immediately); `CACHE LAZY TABLE` is lazy**
- C) Both are eager
- D) `CACHE TABLE` is deprecated — use `CACHE LAZY TABLE`

**Q4.** `spark.sql.adaptive.advisoryPartitionSizeInBytes` controls:
- A) The maximum allowed partition size during a shuffle
- B) The initial partition count when AQE is enabled
- C) **The target partition size AQE aims for when coalescing small partitions**
- D) The threshold above which AQE splits large partitions

**Q5.** Which format is preferred when data is produced by Apache Hive?
- A) Parquet — best general-purpose format
- B) Avro — better for streaming
- C) JSON — human-readable
- D) **ORC — Hive's native format with best statistics support**

**Q6.** `explain('cost')` displays:
- A) The actual CPU time spent on each plan node
- B) The estimated execution time
- C) **CBO row count and data size estimates for each plan node**
- D) Only the physical plan without statistics

**Q7.** `spark.sql.adaptive.coalescePartitions.minPartitionNum = 1` allows AQE to:
- A) Use at least 1 partition regardless
- B) **Coalesce all output into a single partition if input is small enough**
- C) Force exactly 1 partition always
- D) Has no effect — minPartitionNum must be > 1

**Q8.** `spark.sql.inMemoryColumnarStorage.compressed = true` (default):
- A) Compresses data when writing to the warehouse directory
- B) Uses zstd for all Parquet write operations
- C) **Enables Snappy compression for in-memory cached columnar data**
- D) Requires `CACHE LAZY TABLE` to take effect

**Q9.** `trigger(once=True)` in Structured Streaming:
- A) Processes data for exactly 1 second then stops
- B) Processes the first available micro-batch then stops
- C) **Processes ALL currently available data in one micro-batch then stops**
- D) Is equivalent to `trigger(processingTime='1 second')`

**Q10.** `checkpointLocation` stores which items? *(Multi)*
- A) **Source offsets (what data has been read)**
- B) **Sink commit log (what data has been written)**
- C) **State store data (for stateful operations like windowed aggregations)**
- D) Executor JVM heap dumps

**Q11.** Output mode `complete` is invalid when:
- A) The query has more than 1 million rows in the result
- B) The checkpoint directory is missing
- C) The sink is Delta format
- D) **The query has no aggregation**

**Q12.** Event timestamp `12:07` with a 5-minute tumbling window falls in which window?
- A) `[12:00, 12:05)`
- B) **`[12:05, 12:10)`**
- C) `[12:07, 12:12)`
- D) Both `[12:00, 12:05)` and `[12:05, 12:10)`

**Q13.** `foreachBatch` is the correct pattern for:
- A) Reading data from multiple Kafka topics simultaneously
- B) **Writing micro-batch output to multiple sinks**
- C) Applying sliding window aggregations
- D) Processing records from a streaming DataFrame one row at a time

**Q14.** `failOnDataLoss = false` in Kafka streaming:
- A) Silently ignores all errors including network failures
- B) Retries failed micro-batches indefinitely
- C) **Silently skips Kafka offsets that are no longer available due to retention**
- D) Falls back to batch mode when data is unavailable

**Q15.** `query.recentProgress` returns:
- A) The most recent dict of micro-batch statistics
- B) A streaming DataFrame of progress events
- C) A file path to the checkpoint progress log
- D) **A list of dicts for recently completed micro-batches**

**Q16.** `StreamingQueryListener` must be imported from:
- A) `pyspark.sql`
- B) `pyspark.streaming`
- C) **`pyspark.sql.streaming`**
- D) `pyspark.sql.functions`

**Q17.** Regarding `withWatermark()` and `groupBy(window(...))`, which is correct?
- A) `withWatermark` must come AFTER `groupBy`
- B) **`withWatermark` must be called BEFORE `groupBy(window(...))`**
- C) The order doesn't matter — Spark resolves dependencies automatically
- D) `withWatermark` is only valid with `update` output mode

**Q18.** The environment variable that auto-configures Spark Connect without calling `.remote()`:
- A) `SPARK_CONNECT_URL`
- B) `SPARK_SERVER_URL`
- C) `SPARK_CONNECT_SERVER`
- D) **`SPARK_REMOTE`**

**Q19.** Spark Connect uses which format to transfer data between client and server?
- A) Java serialization
- B) Kryo serialization
- C) Protobuf (for data)
- D) **Apache Arrow**

**Q20.** `SparkSession.getActiveSession()` in a Spark Connect application returns:
- A) The server-side SparkSession object
- B) None if called outside of a Spark action
- C) **A client-side proxy session object**
- D) The SparkContext (for backward compatibility)

**Q21.** Databricks Serverless connect is initiated with:
- A) `SparkSession.builder.remote('databricks://serverless').getOrCreate()`
- B) `SparkSession.builder.serverless().getOrCreate()`
- C) **`DatabricksSession.builder.serverless().getOrCreate()`**
- D) `spark.connect.serverless().start()`

**Q22.** Which Spark Connect capability is NOT available?
- A) Running SQL via `spark.sql()`
- B) Reading Parquet with `spark.read.parquet()`
- C) Using streaming with `readStream`
- D) **Creating and using SparkContext / RDD operations**

**Q23.** `ps.sql('SELECT * FROM my_view')` in Pandas API on Spark requires:
- A) A Hive metastore connection
- B) `spark.sql.legacy.pySpark = true`
- C) **`my_view` to be registered as a temp view**
- D) Converting the DataFrame to pandas first

**Q24.** Which two approaches both correctly read a Parquet file into Pandas API on Spark DataFrame? *(Multi)*
- A) **`ps.read_parquet('/path')`**
- B) `pd.read_parquet('/path').to_spark()`
- C) **`spark.read.parquet('/path').pandas_api()`**
- D) `ps.from_pandas(pd.read_parquet('/path'))`

**Q25.** `psdf.apply(func, axis=1)`:
- A) Raises NotImplementedError — axis=1 is not supported
- B) Applies func column-wise
- C) **Applies func row-wise; each row passed as a pd.Series**
- D) Applies func to the first column only

**Q26.** `psdf['value'].rolling(3).mean()` for the first 2 rows returns:
- A) 0.0
- B) The mean of the available rows
- C) The value of the single available row
- D) **NaN (insufficient preceding values)**

**Q27.** `ps.concat([a, b], axis=1)` requires which setting?
- A) No special setting — it works by default
- B) `spark.sql.legacy.concat.enabled = true`
- C) **`spark.sql.execution.pandas.ops_on_diff_frames.enabled = true`**
- D) Both DataFrames must have identical schemas

**Q28.** `ps.concat([a, b], ignore_index=True)`:
- A) Raises ValueError — ignore_index is not supported
- B) Drops all row indices from both DataFrames
- C) **Creates a new default integer index for the concatenated result**
- D) Keeps the original index but renames it to 0

**Q29.** Update output mode:
- A) Emits ALL rows in the result table on every trigger
- B) Emits only newly appended rows (no updates to existing rows)
- C) **Emits only rows that were changed or added since the last trigger**
- D) Requires aggregation to function correctly

**Q30.** `explain('formatted')` vs `explain('extended')`:
- A) `formatted` includes all 4 plan stages; `extended` shows physical only
- B) They are identical in output
- C) **`formatted` is human-readable physical plan with node IDs; `extended` shows all 4 plan stages**
- D) `extended` is deprecated — use `formatted` instead

### Practice Test 3 — Answer Key

| Q | A | Q | A | Q | A |
|---|---|---|---|---|---|
| 1 | C | 11 | D | 21 | C |
| 2 | A,B | 12 | B | 22 | D |
| 3 | B | 13 | B | 23 | C |
| 4 | C | 14 | C | 24 | A,C |
| 5 | D | 15 | D | 25 | C |
| 6 | C | 16 | C | 26 | D |
| 7 | B | 17 | B | 27 | C |
| 8 | C | 18 | D | 28 | C |
| 9 | C | 19 | D | 29 | C |
| 10 | A,B,C | 20 | C | 30 | C |

**Score**: __/30 | Passing: 23+ | Time used: ___

---

## SECTION 5: PRACTICE TEST 4 — Full 100-Question Simulation

**Time limit**: 120 minutes (72 seconds per question)
**Passing goal**: 70/100 (70%)

**Instructions:**
1. Use the question pool from Practice Tests 1, 2, and 3 (70 questions already written)
2. Add the following 30 supplemental questions to complete the 100-question simulation
3. Simulate exam conditions: no reference materials, time yourself

### Supplemental Questions (Q71–Q100)

**Q71.** Which correctly describes `MEMORY_ONLY_2` storage level?
- A) Data is stored in memory; spills to disk if full; one copy
- B) Data is stored in memory; kept in two encoding tiers
- C) **Data is kept as two replicated copies across two different executors**
- D) Data is serialized and stored in memory; one copy

**Q72.** `spark.sql.files.openCostInBytes` affects partition planning by:
- A) Setting a hard cap on partition size
- B) Determining when to split a large file into multiple partitions
- C) **Adding a simulated overhead cost per file to encourage merging small files**
- D) Limiting the number of files per partition

**Q73.** `HashPartitioner` assigns key `k` to partition number:
- A) `k % numPartitions`
- B) **`abs(k.hashCode()) % numPartitions`**
- C) `hash(k) % numPartitions` (Python hash)
- D) `Math.abs(k) % numPartitions`

**Q74.** DRA removes an idle executor after:
- A) `spark.dynamicAllocation.removeDelay` seconds
- B) **`spark.dynamicAllocation.executorIdleTimeout` seconds**
- C) `spark.network.timeout` seconds
- D) `spark.executor.heartbeatInterval` × 3 seconds

**Q75.** The Spark Thrift Server is most similar to which standard technology?
- A) REST API gateway
- B) Apache Kafka broker
- C) **HiveServer2 (JDBC/ODBC gateway)**
- D) Apache ZooKeeper coordination service

**Q76.** Which transformation does NOT create a stage boundary?
- A) `rdd.groupByKey()`
- B) `df.join(other, 'key')` without broadcast
- C) **`df.withColumn('x', F.col('y') + 1)`**
- D) `df.repartition(100)`

**Q77.** `spark.sql.warehouse.dir = 'spark-warehouse'` means:
- A) A relative path from the cluster home directory
- B) **The `spark-warehouse` directory in the current working directory of the driver**
- C) `/tmp/spark-warehouse` on the driver
- D) `hdfs:///spark-warehouse`

**Q78.** CBO (`spark.sql.cbo.enabled = true`) by itself enables:
- A) Join reordering
- B) Adaptive query execution
- C) **Smarter join strategy selection based on statistics (but NOT join reordering)**
- D) Automatic statistics collection

**Q79.** `ANALYZE TABLE t COMPUTE STATISTICS FOR ALL COLUMNS` updates:
- A) Only table-level row count and size
- B) **Column-level statistics: NDV, min, max, null count for all columns**
- C) The query plan cache
- D) Partition statistics only

**Q80.** `spark.sql.join.preferSortMergeJoin = true`:
- A) Forces all joins to use SortMergeJoin
- B) Disables BroadcastHashJoin
- C) Disables ShuffledHashJoin entirely
- D) **Prefers SortMergeJoin over ShuffledHashJoin when both are applicable**

**Q81.** A streaming query in `update` output mode:
- A) Requires aggregation
- B) Emits all rows in the result table
- C) **Emits only rows that changed or were newly added since the last trigger**
- D) Requires a watermark

**Q82.** `query.lastProgress` vs `query.recentProgress`:
- A) Both return the same single dict
- B) **`lastProgress` = single dict for the most recent batch; `recentProgress` = list of dicts**
- C) `lastProgress` is a list; `recentProgress` is a single dict
- D) They are identical

**Q83.** `failOnDataLoss = false` does NOT skip:
- A) Expired Kafka partitions
- B) Deleted topic partitions
- C) Kafka offsets beyond the retention period
- D) **Active network connection failures to the Kafka broker**

**Q84.** Spark Connect's `SPARK_REMOTE` must be set to a URL starting with:
- A) `spark://`
- B) `spark-connect://`
- C) **`sc://`**
- D) `grpc://`

**Q85.** Which statement about Spark Connect is FALSE?
- A) Multiple clients can share one Spark Connect server
- B) The driver runs on the client machine
- C) Apache Arrow is used for data transfer
- D) **SparkContext is available through the Connect session for RDD operations**

**Q86.** `ps.read_parquet('/data')` returns:
- A) `pandas.DataFrame` (local)
- B) `pyspark.sql.DataFrame`
- C) **`pyspark.pandas.DataFrame` (distributed)**
- D) `pyarrow.Table`

**Q87.** `psdf['col'].rolling(window=3).sum()` for rows 1, 2, 3, 4 with values 10, 20, 30, 40:
- A) `NaN, NaN, 60, 60`
- B) `10, 30, 60, 90`
- C) `NaN, 30, 60, 90`
- D) **`NaN, NaN, 60, 90`**

**Q88.** Which statement about `ps.concat([a, b])` default behavior is true?
- A) **Default axis is 0 (stacks rows)**
- B) Default axis is 1 (side-by-side columns)
- C) The result always has a default integer index
- D) Both DataFrames must have the same number of rows

**Q89.** `@pandas_udf(returnType=DoubleType())` — the function receives and returns:
- A) Single row values (scalar UDF behavior)
- B) Python lists
- C) **`pandas.Series` input and `pandas.Series` output**
- D) `pandas.DataFrame` input and `pandas.Series` output

**Q90.** `df.selectExpr` accepts:
- A) Column objects only
- B) Lambda functions
- C) **SQL expression strings**
- D) Python format strings

**Q91.** `sdf.to_pandas_on_spark()` keeps data:
- A) Collected to the driver as a local pandas DataFrame
- B) In Arrow format on disk
- C) **Distributed across the Spark cluster**
- D) In the JVM off-heap memory

**Q92.** The second positional parameter of `df.write.jdbc(url, ???)` is:
- A) `schema`
- B) `dbtable`
- C) `tableName`
- D) **`table`**

**Q93.** To read a JDBC table with parallelism using explicit WHERE predicates:
- A) `.option('numPartitions', 10)` alone
- B) `.option('partitionColumn', 'id')` alone
- C) `.option('fetchsize', 1000)` for parallelism
- D) **`.option('predicates', [...])` where each predicate is a separate partition**

**Q94.** Parquet schema is inferred from:
- A) The first row group
- B) A sample of 100 rows
- C) A separate `.schema` file in the directory
- D) **The file footer (Parquet metadata block at the end of each file)**

**Q95.** `F.when(condition, value)` without `.otherwise()` for unmatched rows returns:
- A) The string `'null'`
- B) `0` for numeric columns
- C) Raises an exception at runtime
- D) **`null`**

**Q96.** `exceptAll` returns:
- A) All rows from df1 not in df2 (deduped)
- B) **All rows from df1 minus one occurrence per matching row in df2**
- C) Rows from df2 not in df1
- D) Distinct rows present in both df1 and df2

**Q97.** What does `schema.json()` return for `StructType([StructField('x', IntegerType(), True)])`?
- A) A Python dict
- B) A StructField list
- C) Raises AttributeError — use `str(schema)` instead
- D) **A JSON string representation of the StructType**

**Q98.** `coalesce(1)` on a DataFrame with 100 partitions:
- A) Triggers a full shuffle to produce 1 balanced partition
- B) Reduces to 1 partition; may trigger a shuffle
- C) **Reduces to 1 partition; NO shuffle (narrow transformation)**
- D) Is equivalent to `repartition(1)`

**Q99.** Which option is NOT valid for a standard (non-Delta) Parquet write?
- A) `compression`
- B) `maxRecordsPerFile`
- C) `partitionOverwriteMode`
- D) **`header`**

**Q100.** `F.coalesce(F.lit(None), F.lit(None), F.lit(42))` returns:
- A) null
- B) 0
- C) **42**
- D) Raises NullPointerException

### Practice Test 4 — Supplemental Answer Key (Q71–Q100)

| Q | A | Q | A | Q | A |
|---|---|---|---|---|---|
| 71 | C | 81 | C | 91 | C |
| 72 | C | 82 | B | 92 | D |
| 73 | B | 83 | D | 93 | D |
| 74 | B | 84 | C | 94 | D |
| 75 | C | 85 | D | 95 | D |
| 76 | C | 86 | C | 96 | B |
| 77 | B | 87 | D | 97 | D |
| 78 | C | 88 | A | 98 | C |
| 79 | B | 89 | C | 99 | D |
| 80 | D | 90 | C | 100 | C |

**Full Test 4 Score**: __/100 | Passing: 70+ | Time used: ___

---

## SECTION 6: COMMON PITFALLS MATRIX

| # | Topic | Pitfall | Correct Answer |
|---|-------|---------|---------------|
| 1 | Architecture | Using `--files` for Python modules | Must use `--py-files` |
| 2 | Architecture | Thinking History Server is on port 4040 | History Server = **18080**; live app = 4040 |
| 3 | Architecture | Assuming `groupByKey()` returns RDD with no partitioner | Returns RDD with `HashPartitioner(default.parallelism)` |
| 4 | Architecture | Thinking `MEMORY_ONLY_2` is serialized or two tiers | Two **replicated copies** across two executors |
| 5 | Architecture | Confusing `spark.task.maxRetries` with correct config | Correct: `spark.task.maxFailures` |
| 6 | Architecture | Thinking `heartbeatInterval > network.timeout` is OK | Must be significantly **less than** |
| 7 | Architecture | Thinking `coalesce()` creates a stage boundary | coalesce is narrow (no shuffle); repartition is wide |
| 8 | SQL | `size(null)` = 0 or -1 | `size(null)` = **null** in Spark 3+ |
| 9 | SQL | `from_unixtime` returns TimestampType | Returns **StringType** |
| 10 | SQL | Left map wins in `map_concat` | **Right map wins** |
| 11 | SQL | `ROLLUP(a,b)` = 4 sets like CUBE | ROLLUP = **3** sets; CUBE = **4** sets |
| 12 | SQL | `EXCEPT ALL` removes all occurrences | Removes **one per occurrence** (multiset semantics) |
| 13 | SQL | `QUALIFY` available since Spark 3.0 | Only since **Spark 3.4** |
| 14 | SQL | `ROWS BETWEEN` and `RANGE BETWEEN` behave the same | ROWS = physical offset; RANGE = value-based |
| 15 | DataFrame | `broadcast()` imported from `pyspark.sql` | Import from **`pyspark.sql.functions`** |
| 16 | DataFrame | `df.rdd` returns dicts or tuples | Returns **Row objects** |
| 17 | DataFrame | `write.text()` works with any schema | Requires **exactly one StringType column** |
| 18 | DataFrame | `df.getNumPartitions()` works on DataFrame | Does NOT exist; use `df.rdd.getNumPartitions()` |
| 19 | DataFrame | Second arg of `write.jdbc()` is `dbtable` | Second arg is **`table`** |
| 20 | DataFrame | `header` is a valid Parquet write option | CSV only; **NOT valid** for Parquet |
| 21 | DataFrame | `mergeSchema` is a Parquet write option | **Read option** only (for plain Parquet) |
| 22 | Troubleshooting | `autoBroadcastJoinThreshold = 0` disables broadcast | Must be **-1** to disable |
| 23 | Troubleshooting | `cbo.enabled = true` alone enables join reorder | Needs **cbo.joinReorder.enabled = true** too |
| 24 | Troubleshooting | `CACHE TABLE` is lazy | `CACHE TABLE` is **eager** |
| 25 | Streaming | `complete` mode works for all queries | Requires **aggregation** |
| 26 | Streaming | `recentProgress` returns a single dict | Returns a **list of dicts** |
| 27 | Streaming | `withWatermark` can come after `groupBy` | Must come **before** `groupBy(window(...))` |
| 28 | Connect | `SPARK_CONNECT_URL` is the env var | Correct var is **`SPARK_REMOTE`** |
| 29 | Connect | SparkContext/RDD available in Connect | **NOT available** via Spark Connect |
| 30 | Pandas API | Only `ps.read_parquet()` works | Both `ps.read_parquet()` AND `.pandas_api()` work |

---

## SECTION 7: SCORING AND TARGET BANDS

### By Topic (Iter 4 Distribution)

| Topic | Questions (approx.) | Target Score | Weakness Threshold |
|-------|---------------------|-------------|-------------------|
| Architecture | 20 | 15+ (75%) | < 12 → Rework §1 |
| SQL | 20 | 15+ (75%) | < 12 → Rework §2 |
| DataFrame | 30 | 23+ (75%) | < 18 → Rework §3 |
| Troubleshooting | 10 | 8+ (80%) | < 6 → Rework §4 |
| Streaming | 10 | 8+ (80%) | < 6 → Rework §5 |
| Spark Connect | 5 | 4+ (80%) | < 3 → Rework §6 |
| Pandas API | 5 | 4+ (80%) | < 3 → Rework §7 |
| **Total** | **100** | **70+ (70%)** | **< 60 → Full re-study** |

### Practice Test Progression

| Test | Questions | Scoring |
|------|-----------|--------|
| Test 1 (Arch + SQL) | 40 Q | Green: 33+, Yellow: 28–32, Red: <28 |
| Test 2 (SQL + DF) | 50 Q | Green: 40+, Yellow: 35–39, Red: <35 |
| Test 3 (Trouble + Stream + Connect + Pandas) | 30 Q | Green: 24+, Yellow: 20–23, Red: <20 |
| Test 4 (Full Sim) | 100 Q | Pass: 70+, Close: 65–69, Re-study: <65 |

---

## SECTION 8: EXAM DAY STRATEGY

### Time Management (120 minutes, 100 questions)

| Phase | Time | Action |
|-------|------|--------|
| Questions 1–25 | 0–30 min | Architecture + SQL: 72 sec/Q |
| Questions 26–55 | 30–66 min | DataFrame: 72 sec/Q |
| Questions 56–65 | 66–78 min | Troubleshooting: 72 sec/Q |
| Questions 66–75 | 78–90 min | Streaming: 72 sec/Q |
| Questions 76–80 | 90–96 min | Connect: 72 sec/Q |
| Questions 81–85 | 96–102 min | Pandas API: 72 sec/Q |
| Review + Flag Revisit | 102–120 min | Review flagged questions |

### Multi-Answer Question Technique

1. Read ALL options before answering — multi-answer options may all be correct
2. Eliminate clearly wrong options first
3. For "select all that apply" — think independently for each option (T/F)
4. Common multi-answer counts in Iter 4: 2 correct (most), 3 correct (some), 4–5 correct (few)
5. Don't assume exactly 2 answers — count based on evidence

### Question Reading Strategy

1. Read the question stem carefully — identify the key constraint (function name, config key, output type)
2. Watch for absolute words: "always", "never", "only", "must" — often reveals wrong options
3. For code questions: mentally trace execution before looking at options
4. For config questions: recall the EXACT config key (many traps use similar-sounding keys)
5. Flag and return: if >90 seconds spent, flag and move on

### High-Value Review Priority (Last 18 Minutes)

| Priority | Items |
|----------|-------|
| 1st | Multi-answer questions flagged (check count again) |
| 2nd | Architecture port numbers (4040 vs 8080 vs 18080) |
| 3rd | Return type distinctions (StringType vs TimestampType for from_unixtime) |
| 4th | Null behavior (size(null), when without otherwise) |
| 5th | Config key exact names (maxFailures not maxRetries, table not dbtable) |

---

## SECTION 9: PROGRESS TRACKING TEMPLATE

```
ITERATION 4 — STUDY PROGRESS
==============================

Week 1 Review Score (Anchors A1-A10 from memory): __ / 10
Week 2 Practice Test 1 Score: __ / 40  |  Date: ___
Week 3 Practice Test 2 Score: __ / 50  |  Date: ___
Week 4 Practice Test 3 Score: __ / 30  |  Date: ___
Week 4 Practice Test 4 Score: __ / 100 |  Date: ___

Topic Weakness Log:
- Architecture weak areas: _______________________
- SQL weak areas: ________________________________
- DataFrame weak areas: __________________________
- Troubleshooting weak areas: ____________________
- Streaming weak areas: __________________________
- Connect weak areas: ____________________________
- Pandas API weak areas: _________________________

Traps I Keep Getting Wrong:
1. _______________________________________________
2. _______________________________________________
3. _______________________________________________

Final Anchor Test (all 35 from memory): __ / 35

EXAM DATE: ___________   TARGET: 70+/100
```

---

*Do not overwrite this file — it is part of the Iteration 4 study library.*
