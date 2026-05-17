# Practice Strategy — Databricks Spark Associate (Iteration 3)

**100 questions | 20E / 60M / 20H | 79 single / 21 multi-answer**

---

## 4-Week Study Plan

### Week 1 — Foundation (Architecture + SQL Fundamentals)

| Day | Focus | Target Topics | Activity |
|-----|-------|--------------|---------|
| Mon | Architecture Core | WholeStageCodegen, Tungsten, checkpoint vs persist | Read Study Guide §1.2–1.5, memory anchors A1–A3 |
| Tue | Architecture Memory | Unified Memory, off-heap, serialization (Kryo) | Read §1.6–1.7, practice off-heap config pattern |
| Wed | Architecture Operations | Heartbeat, Python UDF model, cluster managers | Read §1.8–1.11, compare cluster manager table |
| Thu | Architecture Advanced | Locality, speculative, Resource Profile, stage counting | Read §1.12–1.16, drill stage-count scenarios |
| Fri | SQL — Functions I | from_json, struct, to_timestamp, greatest, transform | Read §2.1–2.3, practice HOF syntax |
| Sat | SQL — HOF | filter, aggregate, forall, exists, zip_with | Read §2.4, write out HOF signatures from memory |
| Sun | Review Week 1 | All architecture + SQL HOF anchors | Self-quiz on A1–A10 |

### Week 2 — Intermediate SQL + DataFrame API

| Day | Focus | Target Topics | Activity |
|-----|-------|--------------|---------|
| Mon | SQL — Array Structural | flatten, posexplode, slice, sequence, arrays_zip | Read §2.5, distinguish 1-based vs 0-based indexing |
| Tue | SQL — Map Functions | map_keys, map_values, map_filter, create_map | Read §2.6, write map schema examples |
| Wed | SQL — Date/String/Safety | months_between, lpad, try_cast, nvl/nvl2 | Read §2.7–2.8, A9/A10 drills |
| Thu | SQL — Advanced SQL | PIVOT, LATERAL VIEW, BROADCAST hint, first(ignorenulls) | Read §2.9–2.12, SQL hint syntax practice |
| Fri | DataFrame — Describe/Stats | describe, summary, corr, approxQuantile, freqItems | Read §3.1–3.2, compare describe vs summary |
| Sat | DataFrame — Transforms | limit, sample, randomSplit, hint, transform, observe | Read §3.3, method chaining practice |
| Sun | Review Week 2 | SQL + DataFrame basics A6–A15 | Self-quiz on all 15 anchors so far |

### Week 3 — Advanced DataFrame + Troubleshooting + Streaming

| Day | Focus | Target Topics | Activity |
|-----|-------|--------------|---------|
| Mon | DataFrame — Array/Map Ops | array set ops, zip_with, map_filter, arrays_zip | Read §3.4, array set ops table |
| Tue | DataFrame — Schema/Write | StructType.fromDDL, MapType, insertInto, writeTo | Read §3.5–3.7, schema construction examples |
| Wed | DataFrame — Advanced | bucketBy, localCheckpoint, na.replace, crosstab | Read §3.8–3.12, na.replace vs na.fill drill |
| Thu | Troubleshooting — Basics | EXPLAIN modes, spark.conf.set, CBO, AQE configs | Read §4.1–4.4, EXPLAIN mode table |
| Fri | Troubleshooting — Advanced | locality.wait, shuffle compress, lz4 codec, cores | Read §4.5–4.7, A16–A20 anchors |
| Sat | Streaming — Core | Trigger modes, maxFilesPerTrigger, stream-static join | Read §5.1–5.3, trigger table |
| Sun | Streaming — Advanced | query.status/lastProgress, Kafka offsets, watermark, mapGroupsWithState | Read §5.4–5.9 |

### Week 4 — Connect + Pandas + Full Exam Simulation

| Day | Focus | Target Topics | Activity |
|-----|-------|--------------|---------|
| Mon | Spark Connect | remote(), server-side analysis, Serverless, gRPC | Read §6.1–6.4, Spark Connect vs Classic table |
| Tue | Pandas API on Spark | ps.merge, ops_on_diff_frames, read_csv, get_dummies, shortcut_limit | Read §7.1–7.5, A31–A35 drills |
| Wed | Mock Test 1 | 40Q (architecture-heavy) | Take Mock Test 1 below |
| Thu | Mock Test 2 | 50Q (SQL + DataFrame) | Take Mock Test 2 below |
| Fri | Mock Test 3 | 60Q (full topics, timed) | Take Mock Test 3 below |
| Sat | Weak Area Remediation | Target any topic scoring < 70% | Re-read Study Guide sections + anchors |
| Sun | Mock Test 4 (Full Exam) | 100Q full simulation | Take Mock Test 4 below |

---

## Mock Test 1 — Architecture Focus (40 Questions)

**Time limit: 40 minutes | Single-answer unless marked [MULTI]**

1. WholeStageCodegen fuses multiple pipeline operators into:
   - A) A Scala RDD transformation chain
   - B) A single optimized JVM bytecode function
   - C) A DataFrame Plan Node
   - D) A Python vectorized UDF
   **Answer: B**

2. `df.checkpoint()` differs from `df.persist()` because checkpoint:
   - A) Uses faster memory storage
   - B) Writes to reliable distributed storage and **truncates lineage**
   - C) Keeps the lineage intact
   - D) Only works with YARN
   **Answer: B**

3. To enable off-heap Tungsten memory, which properties must BOTH be set? [MULTI]
   - A) `spark.memory.offHeap.enabled = true`
   - B) `spark.memory.offHeap.size` (positive byte value)
   - C) `spark.tungsten.enabled = true`
   - D) `spark.executor.memoryOffHeap = 4g`
   **Answer: A, B**

4. Which data locality level means data is in the same Executor JVM process?
   - A) NODE_LOCAL
   - B) PROCESS_LOCAL
   - C) RACK_LOCAL
   - D) JVM_LOCAL
   **Answer: B**

5. Which config controls how much in-flight shuffle data a reducer fetches at once?
   - A) `spark.shuffle.maxBytesInFlight`
   - B) `spark.reducer.maxSizeInFlight`
   - C) `spark.shuffle.fetchBytes`
   - D) `spark.executor.shuffle.maxMemory`
   **Answer: B**

6. Kryo serialization is configured with which property?
   - A) `spark.kryo.enabled = true`
   - B) `spark.serializer = org.apache.spark.serializer.KryoSerializer`
   - C) `spark.rdd.serializer = kryo`
   - D) `spark.kryo.serializer = true`
   **Answer: B**

7. What happens when an Executor's heartbeat timeout is exceeded? [MULTI]
   - A) Driver marks the Executor as lost
   - B) Tasks running on that Executor are rescheduled
   - C) The entire Spark application fails immediately
   - D) The Cluster Manager is asked to launch a replacement Executor
   **Answer: A, B, D**

8. The external shuffle service enables:
   - A) Faster shuffle file compression
   - B) Executor removal by DRA without losing shuffle data
   - C) Distributing shuffle files to HDFS automatically
   - D) Using off-heap memory for shuffle
   **Answer: B**

9. Python UDF execution uses a separate Python worker process because:
   - A) Python requires a JVM to run
   - B) Data is pickled and exchanged via a local socket between JVM and Python
   - C) Python workers run on the Driver, not Executors
   - D) Python UDFs are compiled to native code first
   **Answer: B**

10. Which cluster manager does NOT require a Hadoop installation?
    - A) YARN
    - B) Kubernetes
    - C) Standalone
    - D) Both B and C
    **Answer: D (Standalone and Kubernetes both work without Hadoop)**

11. A 10 GB DataFrame is broadcast-joined to a 5 MB lookup table, then grouped by region. How many Stages?
    - A) 1
    - B) 2
    - C) 3
    - D) 4
    **Answer: B**

12. `spark.speculation.multiplier` controls:
    - A) How often speculation checks run
    - B) How many times slower than the median a task must be before speculation triggers
    - C) The maximum number of speculative copies per Task
    - D) The fraction of Tasks that must complete before speculation starts
    **Answer: B**

13. The Resource Profile API [MULTI]:
    - A) Allows different Executor configs per stage
    - B) Is only supported on YARN
    - C) Attaches to RDDs via `rdd.withResources(profile)`
    - D) Supports requesting GPU resources per stage
    **Answer: A, C, D**

14. Spark's Unified Memory Model handles a join needing more memory than available by:
    - A) Failing with OOM immediately
    - B) Evicting cached Storage blocks to free space for Execution
    - C) Spilling to disk immediately without using Storage Memory
    - D) Canceling the cache operation entirely
    **Answer: B**

15. Which is the correct spark.locality.wait trade-off?
    - A) Higher wait = less data locality, faster task launch
    - B) Higher wait = better data locality, potentially delayed task launch
    - C) Higher wait = more speculative tasks
    - D) `spark.locality.wait` does not affect task scheduling
    **Answer: B**

16. Which can cancel a running Spark Job programmatically? [MULTI]
    - A) `spark.sparkContext.cancelJob(jobId)`
    - B) `spark.sparkContext.cancelAllJobs()`
    - C) `spark.sparkContext.cancelJobGroup(groupId)`
    - D) `spark.stop()`
    **Answer: A, B, C, D**

17. `localCheckpoint()` differs from `checkpoint()` because localCheckpoint:
    - A) Stores data on HDFS but faster
    - B) Stores data on local Executor disk (not fault-tolerant across Executor failure)
    - C) Does not truncate lineage
    - D) Requires `setCheckpointDir()` to be called first
    **Answer: B**

18. PROCESS_LOCAL locality is preferred because:
    - A) It avoids any network transfer by reading from HDFS
    - B) Data is in the same Executor JVM process — zero network and zero IPC
    - C) It co-locates data with the Driver
    - D) It uses RDMA for data transfer
    **Answer: B**

19. Rack awareness helps by:
    - A) Always ensuring PROCESS_LOCAL scheduling
    - B) Preferring RACK_LOCAL to reduce cross-rack bandwidth when closer options are unavailable
    - C) Only affecting broadcast variable distribution
    - D) Eliminating shuffle entirely
    **Answer: B**

20. The default shuffle compression codec `spark.io.compression.codec` is:
    - A) snappy
    - B) gzip
    - C) lz4
    - D) zstd
    **Answer: C**

21. With 16 cores per Executor, what performance problem most likely occurs?
    - A) Executor OOM from the JVM heap
    - B) HDFS client throughput bottleneck and increased GC pressure
    - C) Driver overload tracking too many Tasks
    - D) WholeStageCodegen disabled for large Executors
    **Answer: B**

22. AQE skew join splitting is controlled by which byte threshold config?
    - A) `spark.sql.adaptive.skewJoin.skewedPartitionFactor`
    - B) `spark.sql.adaptive.skewJoin.skewedPartitionThresholdInBytes`
    - C) `spark.sql.adaptive.maxSkewBytes`
    - D) `spark.sql.adaptive.skewJoin.enabled`
    **Answer: B**

23. Which approaches mitigate data skew in a large join? [MULTI]
    - A) Enable AQE with skewJoin.enabled=true
    - B) Salting — add random prefix to join key
    - C) Repartition by join key (concentrate before join)
    - D) Broadcast the smaller table if it fits in memory
    **Answer: A, B, D (C makes skew WORSE)**

24. CBO's primary optimization for multi-table queries is:
    - A) Converting all joins to broadcast
    - B) Reordering joins to minimize intermediate result sizes
    - C) Auto-partitioning tables before joining
    - D) Eliminating correlated subqueries
    **Answer: B**

25. `EXPLAIN CODEGEN` is useful for:
    - A) Viewing SQL text reformatted by Spark
    - B) Identifying expressions that prevent WholeStageCodegen
    - C) Showing cost estimates for each plan node
    - D) Viewing the unresolved logical plan
    **Answer: B**

26. `df.explain('formatted')` vs `df.explain()`:
    - A) They are identical
    - B) 'formatted' shows node IDs and subplan details — more readable
    - C) 'formatted' only shows logical plan
    - D) 'formatted' includes execution statistics
    **Answer: B**

27. Which correctly changes shuffle partition count at runtime?
    - A) `spark.conf.set('spark.sql.shuffle.partitions', 50)`
    - B) `spark.sql.shuffle.partitions = 50`
    - C) `spark.conf.set('spark.shuffle.partitions', 50)`
    - D) `spark.sparkContext.setShufflePartitions(50)`
    **Answer: A**

28. `spark.shuffle.compress = true` compresses:
    - A) Shuffle input data before sending to Executors
    - B) Shuffle output files written during the map phase
    - C) Broadcast variables during distribution
    - D) Task serialization payloads
    **Answer: B**

29. Tungsten's three improvements are: [MULTI]
    - A) Binary data encoding (off-heap or managed heap)
    - B) Cache-aware computation
    - C) WholeStageCodegen / code generation
    - D) Automatic broadcast join selection
    **Answer: A, B, C**

30. `spark.speculation.interval` controls:
    - A) How slow a task must be before speculation
    - B) The interval between checks for straggler Tasks
    - C) The multiplier for speculative Task replication
    - D) When to cancel speculative copies
    **Answer: B**

31. DataFrame lineage is stored as:
    - A) A chain of parent RDD dependencies
    - B) An optimized logical plan processed by Catalyst before execution
    - C) A physical plan with operator IDs
    - D) A series of SQL strings
    **Answer: B**

32. Resource Profile API attaches to a DataFrame via:
    - A) `df.withResourceProfile(profile)`
    - B) `rdd.withResources(profile)`
    - C) `spark.conf.set('resource.profile', profile)`
    - D) `df.hint('resource-profile', profileId)`
    **Answer: B**

33. To prevent Executor removal from causing DRA failures, you need:
    - A) `spark.executor.instances` set to a minimum
    - B) External shuffle service running on worker nodes
    - C) `spark.dynamicAllocation.cachedExecutorIdleTimeout`
    - D) Kryo serialization enabled
    **Answer: B**

34. Which is true about Executor heartbeat timeout recovery? [MULTI]
    - A) Tasks are rescheduled on other Executors
    - B) A replacement Executor is requested from the Cluster Manager
    - C) The application immediately fails
    - D) The Driver marks the Executor as lost
    **Answer: A, B, D**

35. `spark.memory.storageFraction` (default 0.5) means:
    - A) 50% of total JVM heap is Storage memory
    - B) 50% of the Spark Memory region is initially reserved for Storage
    - C) Storage memory can never exceed 50% of total memory
    - D) 50% of on-disk data is in Storage
    **Answer: B**

36. Python UDF memory problem on YARN is fixed by:
    - A) Increasing `spark.driver.memory`
    - B) Increasing `spark.executor.memoryOverhead`
    - C) Reducing UDF input size
    - D) Disabling WholeStageCodegen
    **Answer: B**

37. Standalone mode's resource tracking is done by:
    - A) YARN ResourceManager
    - B) Spark Master tracking available worker resources
    - C) Kubernetes API server
    - D) Zookeeper
    **Answer: B**

38. The `spark.speculation.quantile` config controls:
    - A) How much slower a task must be
    - B) Fraction of tasks that must complete before speculation can start
    - C) Memory threshold for speculative reads
    - D) Number of speculative copies allowed
    **Answer: B**

39. What does increasing `spark.locality.wait` trade off?
    - A) More memory for better locality
    - B) Better data locality at the cost of potentially delayed task launch
    - C) More CPU for data locality
    - D) Less shuffle data for better locality
    **Answer: B**

40. Which config directly controls Task task failure retry count?
    - A) `spark.task.retryDelay`
    - B) `spark.task.maxFailures`
    - C) `spark.executor.failureRetries`
    - D) `spark.speculation.retries`
    **Answer: B**

**Mock Test 1 Scoring:**
- 38–40: Excellent architecture foundation
- 34–37: Good, review missed items
- 28–33: Spend more time on Architecture in Week 1
- < 28: Re-read Study Guide §Topic 1 entirely

---

## Mock Test 2 — SQL & DataFrame (50 Questions)

**Time limit: 50 minutes | Single-answer unless marked [MULTI]**

1. `F.from_json(col('payload'), schema)` returns:
   - A) A StringType JSON string
   - B) A StructType or MapType column parsed from JSON
   - C) A Python dict
   - D) A list of rows
   **Answer: B**

2. `F.schema_of_json('{"id":1}')` returns:
   - A) A Python StructType object
   - B) A StringType DDL string (e.g., `'STRUCT<id: BIGINT>'`)
   - C) A JSON schema object
   - D) None — it cannot be used as a scalar function
   **Answer: B**

3. `F.transform(col('scores'), lambda x: x * 1.1)`:
   - A) Multiplies each element of the scores array by 1.1
   - B) Renames the scores column
   - C) Filters scores above 1.1
   - D) Raises an error (no Python lambdas in transform)
   **Answer: A**

4. The correct higher-order filter for arrays is:
   - A) `F.array_filter(col('tags'), lambda x: x.startswith('a'))`
   - B) `F.filter(col('tags'), lambda x: x.startswith('a'))`
   - C) `F.select_if(col('tags'), ...)`
   - D) `F.where(col('tags'), ...)`
   **Answer: B**

5. `F.aggregate(col('amounts'), F.lit(0), lambda acc, x: acc + x)` computes:
   - A) Product of all elements
   - B) Sum of all elements starting from 0
   - C) Maximum value
   - D) Count of non-zero elements
   **Answer: B**

6. `F.flatten(col('nested'))` on `ArrayType(ArrayType(IntegerType))`:
   - A) Returns sum of all integers
   - B) Returns a single flat `ArrayType(IntegerType)`
   - C) Returns a JSON string
   - D) Raises error if arrays differ in length
   **Answer: B**

7. `F.months_between(col('end'), col('start'))` returns:
   - A) IntegerType (complete months)
   - B) DoubleType (fractional months, can be negative)
   - C) StringType formatted as '3 months 5 days'
   - D) DateType midpoint
   **Answer: B**

8. `F.lpad(col('code'), 6, '0')` on value `'42'` returns:
   - A) `'420000'`
   - B) `'000042'`
   - C) `'42    '`
   - D) `'42'`
   **Answer: B**

9. `F.posexplode(col('items'))` adds which extra column?
   - A) A UUID identifier
   - B) A zero-based integer position column `pos`
   - C) A row ID from the original DataFrame
   - D) Nothing extra — it's identical to explode
   **Answer: B**

10. PIVOT requires: [MULTI]
    - A) Long-to-wide rotation of rows
    - B) An aggregate function (SUM, AVG, COUNT, etc.)
    - C) `FOR column IN (values)` specification
    - D) Only available in DataFrame API, not SQL
    **Answer: A, B, C**

11. `nvl2(col1, col2, col3)` returns:
    - A) col2 if col1 IS null, else col3
    - B) col2 if col1 is NOT null, else col3
    - C) First non-null of col1, col2, col3
    - D) col3 if col1 is zero
    **Answer: B**

12. `F.map_values(col('metadata'))` returns:
    - A) A MapType with only the values
    - B) An ArrayType with all map values
    - C) A StructType column
    - D) A StringType JSON of values
    **Answer: B**

13. `try_cast('abc' AS INT)` in Spark SQL returns:
    - A) Exception
    - B) null
    - C) 0
    - D) Truncated to 0
    **Answer: B**

14. `LATERAL VIEW explode(tags) t AS tag` produces:
    - A) One row per element in the tags array per original row
    - B) Filters rows with empty tags
    - C) Joins only rows where tags has ≥2 elements
    - D) Invalid syntax
    **Answer: A**

15. `F.forall()` and `F.exists()` on null arrays return:
    - A) False
    - B) True
    - C) null
    - D) Exception
    **Answer: C**

16. `df.describe('salary')` returns:
    - A) One row showing data type
    - B) DataFrame with count/mean/stddev/min/max rows
    - C) Python dict
    - D) Single mean value
    **Answer: B**

17. `df.summary()` vs `df.describe()`:
    - A) Identical
    - B) summary adds 25%/50%/75% quartiles
    - C) describe adds quartiles
    - D) summary only works on numeric columns
    **Answer: B**

18. `df.stat.corr('price', 'qty')` returns:
    - A) DataFrame with correlation statistics
    - B) Python float (Pearson correlation)
    - C) StructType column
    - D) Slope and intercept
    **Answer: B**

19. `df.randomSplit([0.8, 0.2], seed=42)`:
    - A) Guarantees exactly 80%/20%
    - B) Approximately 80%/20%; seed for reproducibility; exact count depends on partitioning
    - C) Sorts and takes first 80%
    - D) Creates stratified samples
    **Answer: B**

20. `df.hint('repartition', 10)`:
    - A) Immediately repartitions to 10 partitions
    - B) Provides advisory hint; optimizer may honor it
    - C) Sets `spark.sql.shuffle.partitions = 10`
    - D) Adds a plan comment only
    **Answer: B**

21. `df.transform(func)` enables:
    - A) SQL string transformation
    - B) Method chaining of custom DataFrame functions
    - C) Pandas UDF per row
    - D) RDD conversion, apply, and back
    **Answer: B**

22. `F.element_at(col('colors'), 2)` on `['red','green','blue']` returns:
    - A) 'red' (0-based index 0)
    - B) 'green' (1-based index 2)
    - C) 'blue' (0-based index 2)
    - D) Error
    **Answer: B**

23. Array set operations that exist in PySpark: [MULTI]
    - A) `F.array_union(a, b)`
    - B) `F.array_intersect(a, b)`
    - C) `F.array_except(a, b)`
    - D) `F.array_concat(a, b)`
    - E) `F.array_distinct(a)`
    **Answer: A, B, C, E (D does NOT exist; use F.concat())**

24. `F.sequence(lit(1), lit(5))` returns:
    - A) LongType value 5
    - B) ArrayType(LongType) containing [1,2,3,4,5]
    - C) DataFrame with 5 rows
    - D) Error (requires column references)
    **Answer: B**

25. `insertInto('t')` vs `write.mode('append').saveAsTable('t')`:
    - A) Identical
    - B) insertInto matches by position; saveAsTable by name
    - C) insertInto enables schema evolution; saveAsTable does not
    - D) insertInto works only on partitioned tables
    **Answer: B**

26. `StructType.fromDDL('id BIGINT, name STRING')`:
    - A) Parses DDL string into a StructType
    - B) Parses DDL into a Python dict
    - C) Executes SQL to create a table
    - D) Not a valid method
    **Answer: A**

27. `MapType` StructField is correctly defined as:
    - A) `StructField('x', MapType(StringType(), DoubleType()), True)`
    - B) `StructField('x', {'STRING': 'DOUBLE'}, True)`
    - C) `StructField('x', 'MAP<STRING, DOUBLE>', True)`
    - D) `MapField('x', key=StringType(), value=DoubleType())`
    **Answer: A**

28. Ways to write Parquet that are valid: [MULTI]
    - A) `df.write.parquet('/path')`
    - B) `df.write.format('parquet').save('/path')`
    - C) `df.write.save('/path', format='parquet')`
    - D) `df.write.format('parquet').mode('overwrite').save('/path')`
    **Answer: A, B, D (C has invalid syntax — save() has no format= parameter)**

29. `F.zip_with(col('a'), col('b'), lambda x, y: x + y)`:
    - A) Concatenates both arrays
    - B) Returns element-wise sum of corresponding positions
    - C) Returns a map from a to b
    - D) Filters to elements in both
    **Answer: B**

30. `bucketBy(16, 'user_id').sortBy('event_time')` enables:
    - A) 16 partitions by user_id for partition pruning
    - B) Shuffle-free SortMergeJoin when joining two identically bucketed tables
    - C) Adds a bucket_id column for fast lookups
    - D) 16 Parquet row groups sorted by both columns
    **Answer: B**

31. `df.stat.freqItems(['col'], support=0.01)`:
    - A) Exact frequency distribution
    - B) DataFrame with one row containing arrays of items appearing in ≥1% of rows
    - C) Count of distinct values
    - D) Pivot table of frequencies
    **Answer: B**

32. `df.observe('metrics', F.count(lit(1)).alias('cnt'))`:
    - A) Adds a count column to every row
    - B) Attaches inline metrics collected via QueryExecutionListener (no separate job)
    - C) Creates a real-time streaming listener
    - D) Immediately triggers an action
    **Answer: B**

33. `F.map_filter(col('scores'), lambda k, v: v > 50)`:
    - A) Filtered array of values > 50
    - B) New MapType with only key-value pairs where value > 50
    - C) BooleanType: any value > 50?
    - D) Error — map_filter is for arrays
    **Answer: B**

34. `df.na.replace(['N/A', ''], 'missing', subset=['status'])`:
    - A) Replaces null values in status with 'missing'
    - B) Replaces specific string values ('N/A', '') with 'missing'; nulls unchanged
    - C) Replaces all columns with 'missing'
    - D) Error — only numeric columns supported
    **Answer: B**

35. `df.stat.crosstab('gender', 'education')` first column is named:
    - A) 'gender'
    - B) 'gender_education'
    - C) 'crosstab'
    - D) Unnamed index
    **Answer: B**

36. `F.arrays_zip(col('names'), col('scores'))` returns:
    - A) Concatenated array
    - B) `ArrayType(StructType)` pairing elements by position
    - C) MapType keyed by names
    - D) Error if any element is null
    **Answer: B**

37. `F.slice(col('items'), start=2, length=3)` on `['a','b','c','d','e']`:
    - A) `['a','b','c']`
    - B) `['b','c','d']`
    - C) `['c','d','e']`
    - D) `['b','c']`
    **Answer: B**

38. `df.writeTo('cat.schema.t').overwritePartitions()`:
    - A) Same as `mode('overwrite').saveAsTable('t')`
    - B) Replaces only the matching partitions, not the whole table
    - C) Creates a new table only
    - D) Not valid — writeTo only supports append
    **Answer: B**

39. Delta Lake time travel by timestamp:
    - A) `.option('timestampOf', '2024-01-01')`
    - B) `.option('timestampAsOf', '2024-01-01')`
    - C) `.withTimestamp('2024-01-01')`
    - D) `.version('2024-01-01')`
    **Answer: B**

40. `F.greatest()` on columns where one is null:
    - A) Returns null if any column is null
    - B) Returns the largest non-null value (ignores nulls)
    - C) Raises an error
    - D) Returns 0 for null columns
    **Answer: B**

41. Which SQL function returns the first non-null value across multiple columns?
    - A) `nvl()`
    - B) `greatest()`
    - C) `coalesce()`
    - D) `first()`
    **Answer: C**

42. `first(col, ignorenulls=True)` in a window function:
    - A) Always returns null for the first row
    - B) Returns the first non-null value in the ordered partition
    - C) Returns 0 for null replacements
    - D) Not supported in window context
    **Answer: B**

43. `F.create_map(lit('k1'), col('v1'), lit('k2'), col('v2'))` returns:
    - A) StructType with fields k1 and k2
    - B) MapType(StringType, <v1_type>) with two entries per row
    - C) ArrayType with alternating keys and values
    - D) Error — must be same type
    **Answer: B**

44. `df.printSchema()` returns:
    - A) StructType Python object
    - B) None (side-effect print to console)
    - C) JSON file of schema
    - D) Triggers schema inference action
    **Answer: B**

45. `df.stat.approxQuantile('salary', [0.5], 0.05)`:
    - A) Exact median
    - B) Approximate median within 5% relative error
    - C) Returns Python dict
    - D) Triggers full sort
    **Answer: B**

46. `F.posexplode(col('items'))` returns compared to `explode()`:
    - A) Fewer rows (skips nulls)
    - B) Same rows plus a pos column with zero-based index
    - C) Map of positions to values
    - D) Identical
    **Answer: B**

47. Which `forall/exists` statements are true? [MULTI]
    - A) `forall` returns True if all elements match predicate
    - B) `exists` returns True if at least one element matches
    - C) Both return BooleanType
    - D) Null array → returns null for both
    **Answer: A, B, C, D**

48. `df.limit(50)` guarantees:
    - A) Top 50 rows by default sort
    - B) At most 50 rows, no ordering guarantee
    - C) Random 50-row sample
    - D) Exactly 50 partitions
    **Answer: B**

49. `df.sample(fraction=0.1, withReplacement=False)` correct syntax:
    - A) Yes — this is the correct method signature
    - B) No — it should be `df.randomSample(0.1)`
    - C) No — should be `df.limit(int(df.count()*0.1))`
    - D) No — `fraction` is not a valid parameter
    **Answer: A**

50. `df.localCheckpoint()` stores on:
    - A) HDFS / cloud storage
    - B) Local Executor disk (not fault-tolerant across Executor failure)
    - C) Driver local disk
    - D) In-memory only
    **Answer: B**

**Mock Test 2 Scoring:**
- 47–50: Excellent SQL/DataFrame mastery
- 42–46: Good, review missed items
- 35–41: Re-read Study Guide §Topic 2–3
- < 35: Focus Week 2 deep dive on SQL and DataFrame API

---

## Mock Test 3 — Troubleshooting + Streaming + Connect + Pandas (60Q, Timed)

**Target time: 60 minutes**

### Troubleshooting (Q1–20)

1. `df.explain('formatted')` shows: **B) Physical plan with node IDs and readable format**
2. Correct shuffle partition runtime change: **A) `spark.conf.set('spark.sql.shuffle.partitions', 50)`**
3. CBO enables (with statistics): **B) Join reordering to minimize intermediate sizes**
4. AQE byte skew threshold config: **B) `spark.sql.adaptive.skewJoin.skewedPartitionThresholdInBytes`**
5. `spark.locality.wait` tradeoff: **B) Higher = better locality, potentially delayed launch**
6. `EXPLAIN CODEGEN` shows: **A) Generated Java bytecode from WholeStageCodegen**
7. `spark.shuffle.compress = true`: **B) Compresses shuffle output files written to disk**
8. Default `spark.io.compression.codec`: **C) lz4**
9. 16 cores/Executor problem: **B) HDFS throughput bottleneck + GC pressure**
10. Effective skew mitigations [MULTI]: **A (AQE), B (salting), E (broadcast)** — C worsens skew
11. EXPLAIN 'extended' shows: **Both logical and physical plans**
12. `spark.sql.cbo.enabled = true` requires: **`ANALYZE TABLE ... COMPUTE STATISTICS` first**
13. AQE auto-coalesces small partitions via: **`spark.sql.adaptive.coalescePartitions.enabled`**
14. Setting 4-5 cores per Executor solves: **HDFS throughput and GC pressure**
15. `spark.speculation.interval` controls: **How often Spark checks for straggler Tasks**
16. Salting fixes skew by: **Distributing load across multiple keys via random prefix**
17. `spark.io.compression.codec = snappy` vs `lz4`: **snappy has moderate compression; lz4 is faster**
18. EXPLAIN 'cost' requires: **CBO and table statistics**
19. `spark.locality.wait.rack` can override rack-level wait: **True**
20. Broadcasting a table to avoid skew works when: **The table fits in Executor memory**

### Streaming (Q21–40)

21. `trigger(processingTime='30 seconds')`: **B) New micro-batch every 30 seconds**
22. `maxFilesPerTrigger=5`: **B) Limits new files processed per micro-batch to 5**
23. Stream-static join — static side: **B) Read once per micro-batch (current snapshot)**
24. `query.status` returns: **B) Python dict of current query state**
25. `startingOffsets='earliest'` on restart with checkpoint: **B) Uses checkpoint offset**
26. `dropDuplicates` + watermark [MULTI]: **A (requires watermark), B (unbounded without), D (state dropped below watermark)**
27. Continuous Processing trigger: **B) Sub-millisecond; async checkpoint; no micro-batch boundary**
28. `query.lastProgress` returns: **B) Python dict with most recent micro-batch metrics**
29. `stream_df.orderBy('event_time')`: **B) AnalysisException — global sort not supported**
30. `mapGroupsWithState` [MULTI]: **A (arbitrary state), B (Python via applyInPandasWithState), D (exactly 1 row per group per batch)**
31. Streaming `complete` mode requires: **A stateful aggregation**
32. `trigger(availableNow=True)`: **Processes all available data in multiple micro-batches, then stops**
33. Kafka `startingOffsets='latest'` on first start: **Skips all historical data**
34. `dropDuplicates` without watermark: **Unbounded state growth**
35. `query.status['isTriggerActive']`: **True when a micro-batch is currently running**
36. Streaming append mode outputs: **Only newly appended rows per micro-batch**
37. Stream-stream join requires: **Watermarks on both sides to bound state**
38. `trigger(once=True)` processes: **All available data in one micro-batch, then stops**
39. Continuous Processing supports: **Simple stateless transformations (map, filter)**
40. `mapGroupsWithState` state on restart: **Automatically restored from checkpoint**

### Spark Connect (Q41–50)

41. Correct Spark Connect session creation:
    - A) `.builder.master('sc://localhost').getOrCreate()`
    - B) `.builder.remote('sc://localhost').getOrCreate()`
    **Answer: B**

42. When do AnalysisExceptions appear in Spark Connect?
    - A) On transformation definition
    - B) On action trigger (plan sent to server)
    **Answer: B**

43. Databricks Serverless uses Spark Connect and therefore [MULTI]:
    - A) SparkContext is unavailable
    - B) RDD API is unavailable
    - C) Supports multi-language (Python, Scala, SQL)
    - D) spark.sparkContext raises an error
    **Answer: A, B, C, D**

44. SSL in Spark Connect URL: **sc://host:15002/;use_ssl=true**
45. gRPC enables Rust to use Spark Connect: **No JVM required; results as Apache Arrow**
46. Spark Connect transport: **gRPC with Protocol Buffers (not Py4J or Netty directly)**
47. Plan sent to server when: **Action triggered (.count(), .collect(), .show())**
48. Databricks Serverless notebook process isolation: **Isolated from Spark Driver**
49. Official Spark Connect clients include: **Python, Scala, Java**
50. Multi-language Serverless uses: **Single Spark Connect server for all languages**

### Pandas API on Spark (Q51–60)

51. Both valid ps.merge syntaxes: **`ps.merge(l, r, on=...)` AND `l.merge(r, on=...)`**
52. `ops_on_diff_frames` default is: **False (disabled)**
53. `ps.read_csv('s3://bucket/file.csv')`: **Works — delegates to Spark's connector**
54. `ps.get_dummies()` result: **Distributed pyspark.pandas DF (NOT collected)**
55. `compute.shortcut_limit` default: **1000 rows**
56. Above shortcut_limit, `len(psdf)` triggers: **Full distributed Spark job**
57. `ps.get_dummies()` column naming: **`<col>_<value>` (e.g., color_red)**
58. `drop_first=True` in get_dummies: **Drops first dummy to avoid multicollinearity**
59. Cross-DF addition requires: **`ps.set_option('compute.ops_on_diff_frames', True)`**
60. pyspark.pandas DF operations stay: **Distributed on Spark cluster**

**Mock Test 3 Scoring:**
- 55–60: Excellent breadth
- 48–54: Good performance
- 40–47: Focus on Streaming + Connect
- < 40: Review Study Guide §Topic 4–7

---

## Mock Test 4 — Full 100-Question Simulation

**Time: 120 minutes | Real exam conditions**

### Answer Key (by topic section)

**Architecture (Q1–20):**
1-B, 2-B, 3-AB, 4-B, 5-B, 6-B, 7-ABD, 8-B, 9-B, 10-D, 11-B, 12-B, 13-ACD, 14-B, 15-B, 16-ABCD, 17-B, 18-B, 19-B, 20-B

**SQL (Q21–40):**
21-B, 22-B, 23-A, 24-B, 25-A, 26-B, 27-B, 28-B, 29-B, 30-B, 31-B, 32-ABC, 33-A, 34-B, 35-B, 36-A, 37-B, 38-B, 39-B, 40-ABCE

**DataFrame (Q41–70):**
41-B, 42-B, 43-B, 44-B, 45-A, 46-B, 47-D, 48-B, 49-B, 50-B, 51-B, 52-ABCE, 53-B, 54-B, 55-A, 56-B, 57-B, 58-A, 59-ABE, 60-B, 61-B, 62-B, 63-B, 64-B, 65-ABCE, 66-B, 67-B, 68-B, 69-ABCE, 70-B

**Troubleshooting (Q71–80):**
71-B, 72-A, 73-B, 74-B, 75-B, 76-ABD, 77-B, 78-C, 79-B, 80-ABE

**Streaming (Q81–90):**
81-B, 82-B, 83-B, 84-B, 85-B, 86-ABD, 87-B, 88-B, 89-B, 90-ABD

**Connect (Q91–95):**
91-B, 92-B, 93-ABDE, 94-A, 95-B

**Pandas API (Q96–100):**
96-D, 97-B, 98-A, 99-ABDE, 100-B

### Mock Test 4 Scoring Scale

| Score | Result | Action |
|-------|--------|--------|
| 85–100 | Ready to certify | Schedule exam this week |
| 78–84 | Strong pass likely | Review weak topics, 1 more day |
| 70–77 | Borderline | Re-read weak sections, retry in 2-3 days |
| 60–69 | Needs work | 2 more study days + retry mock test |
| < 60 | Not ready | Restart Week 3–4 plan |

---

## Iteration 3 Common Pitfalls Matrix (24 Critical Traps)

| # | Topic | The Trap | Correct Answer |
|---|-------|---------|----------------|
| P1 | Architecture | Off-heap needs only `enabled=true` | Needs BOTH `enabled=true` AND `size>0` |
| P2 | Architecture | `checkpoint()` is lazy | checkpoint() is **EAGER** — materializes on next action |
| P3 | Architecture | `localCheckpoint()` = fault-tolerant | `localCheckpoint()` is NOT fault-tolerant (Executor disk only) |
| P4 | Architecture | Default codec = snappy | Default `spark.io.compression.codec` = **lz4** |
| P5 | Architecture | Standalone requires Hadoop | Standalone does **NOT** require Hadoop |
| P6 | Architecture | Repartition by key helps skew | Repartition concentrates skewed key — makes it **WORSE** |
| P7 | Architecture | 16 cores/Executor = max parallelism | 16 cores = HDFS bottleneck + GC pressure; recommend 4-5 |
| P8 | SQL | `F.array_filter()` exists | Use **`F.filter()`** — `F.array_filter()` does not exist |
| P9 | SQL | `schema_of_json()` returns StructType | Returns a **StringType DDL string**, not a Python StructType |
| P10 | SQL | `nvl2` returns col2 if null | `nvl2` returns col2 if **NOT null**; col3 if null |
| P11 | SQL | `to_timestamp()` is a standalone function | `to_timestamp()` exists as `F.to_timestamp()`; `cast()` is a **Column method**, not `F.cast()` |
| P12 | SQL | PIVOT not available in SQL syntax | Spark SQL **does** have PIVOT syntax |
| P13 | SQL | `try_cast` raises exception | `try_cast` returns **null** on failure |
| P14 | SQL | `months_between` returns int | Returns **DoubleType** (fractional, can be negative) |
| P15 | DataFrame | `F.array_concat()` concatenates arrays | `F.array_concat()` does **NOT** exist; use `F.concat()` |
| P16 | DataFrame | `element_at` is 0-based | `F.element_at()` and `F.slice()` use **1-based** indexing |
| P17 | DataFrame | `na.replace()` handles nulls | `na.replace()` handles specific values; use `na.fill()` for nulls |
| P18 | DataFrame | `insertInto` matches by name | `insertInto` matches by **position** — dangerous if schema differs |
| P19 | DataFrame | `describe()` includes quartiles | `describe()` has no quartiles; **`summary()`** adds 25%/50%/75% |
| P20 | Streaming | orderBy works in streaming | `orderBy` raises **AnalysisException** in streaming |
| P21 | Streaming | `dropDuplicates` works without watermark | Without watermark = **unbounded state growth** |
| P22 | Streaming | Continuous = `processingTime='1s'` | Continuous is a different mode: `trigger(continuous='1s')` with sub-ms latency |
| P23 | Connect | `.master('sc://...')` works for Spark Connect | Must use **`.remote('sc://...')`** for Spark Connect |
| P24 | Pandas API | `ps.get_dummies()` collects to driver | Result stays **distributed** as pyspark.pandas DataFrame |

---

## Exam Day Strategy

### Time Management (120 minutes / 100 questions)

**Pace target:** 1.2 minutes per question average
- Single-answer questions: aim for ~1 minute
- Multi-answer questions: aim for ~1.5–2 minutes (more options to evaluate)
- Hard questions: cap at 3 minutes, flag and return

**Recommended approach:**
1. First pass (75 min): Answer all single-answer questions you're confident on; flag hard ones
2. Multi-answer pass (25 min): Tackle all [MULTI] questions — eliminate clearly wrong options first
3. Review pass (20 min): Return to flagged questions

### Multi-Answer Question Technique (21 questions in Iter 3)

For multi-select questions:
1. Read the question stem twice
2. Identify EACH option independently (treat each as True/False)
3. Note any "only supported on X" or "not supported" language — these are often false distractors
4. Common Iter 3 multi-select traps:
   - Resource Profile: "only on YARN" → **False** (works on K8s too)
   - PIVOT: "only DataFrame API" → **False** (SQL syntax exists)
   - `F.array_concat()` in array set ops → **Does not exist**

### Topic-by-Topic Time Allocation

| Topic | Questions | Target Time | Priority |
|-------|-----------|------------|---------|
| DataFrame API | 30 | 33 min | High (most questions) |
| Architecture | 20 | 24 min | High (complex concepts) |
| Spark SQL | 20 | 22 min | High (many function names) |
| Streaming | 10 | 12 min | Medium |
| Troubleshooting | 10 | 11 min | Medium |
| Spark Connect | 5 | 6 min | Lower |
| Pandas API on Spark | 5 | 6 min | Lower |

### Elimination Technique for Hard Questions

When unsure, eliminate using these patterns:
1. **"Only works on X"** — usually the wrong answer (Spark tries to support all cluster managers)
2. **"Raises an error immediately"** — usually wrong unless it's about unsupported streaming ops
3. **"They are identical"** — almost always wrong when comparing two similar methods
4. **Function names with prefixes** — `F.array_concat()` doesn't exist; `F.array_filter()` doesn't exist
5. **0-based vs 1-based indexing** — `element_at` and `slice` are 1-based (unlike Python)

### Last-Minute Review Targets (30 minutes before exam)

Review these high-frequency confusions:
1. lz4 (not snappy) as default codec
2. Off-heap needs TWO properties
3. element_at = 1-based indexing
4. F.filter() not F.array_filter()
5. na.replace ≠ na.fill
6. describe() has no quartiles; summary() does
7. insertInto = by position (not name)
8. orderBy in streaming = AnalysisException
9. schema_of_json = DDL string, not StructType
10. .remote() not .master() for Spark Connect

---

## Progress Tracking Template

| Week | Mock Test | Score | Weak Topics | Action Taken |
|------|-----------|-------|-------------|-------------|
| 4 Wed | Mock Test 1 (40Q) | /40 | | |
| 4 Thu | Mock Test 2 (50Q) | /50 | | |
| 4 Fri | Mock Test 3 (60Q) | /60 | | |
| 4 Sun | Mock Test 4 (100Q) | /100 | | |

**Target progression:**
- Mock 1: ≥ 32/40 (80%)
- Mock 2: ≥ 40/50 (80%)
- Mock 3: ≥ 48/60 (80%)
- Mock 4: ≥ 82/100 (82%) → Exam-ready

**Multi-answer accuracy tracking:**
| Test | Multi-Qs | Fully Correct | Partially Correct | Wrong |
|------|---------|--------------|------------------|-------|
| Mock 1 | — | — | — | — |
| Mock 4 | 21 | | | |

Target: ≥ 16/21 fully correct on multi-answer questions.
