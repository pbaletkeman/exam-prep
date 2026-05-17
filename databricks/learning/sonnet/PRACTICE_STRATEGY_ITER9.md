# Practice Strategy — Iteration 9
## Databricks Certified Associate Developer for Apache Spark

---

## ⚠️ Exam Day Answer Distribution Reminder

> **89 × B, 8 × A, 3 × C**
>
> If you are seeing mostly B and doubting yourself — that is correct. 89% of answers are B.
> But the 11 exceptions are real and examinable. Know them cold before you enter the room.
>
> All 3 × C answers are in Q1–Q20 (Architecture). Mark every Architecture question for review.

---

## 4-Week Study Plan

### Week 1 — Architecture + SQL Foundation (Q1–Q40)

| Day | Focus | Task |
|---|---|---|
| Mon | Architecture overview | Read STUDY_GUIDE Architecture section; memorize memory model |
| Tue | Architecture — non-B traps | Review Q1, Q3, Q4, Q7, Q9, Q10; run memory math |
| Wed | Architecture — configs | Config Defaults Cheatsheet; copy by hand without looking |
| Thu | SQL functions: string, numeric | Practice LPAD, locate, repeat, ILIKE, LIKE ANY, reduce |
| Fri | SQL functions: date/time | make_interval, TIMESTAMPADD, unix_timestamp vs to_timestamp |
| Sat | SQL functions: map/array | map_contains_key, array_position, reduce/finish, to_number vs try_to_number |
| Sun | **Practice Test A** | Q1–Q40; score and review all wrong answers |

### Week 2 — DataFrame/Dataset API (Q41–Q70)

| Day | Focus | Task |
|---|---|---|
| Mon | Metadata + null handling | Q41(withMetadata), Q56(F.lit(None)), Q52(nullif) |
| Tue | Window functions | Q45(collect_list window), Q47(observe), Q48(rint) |
| Wed | I/O: Parquet, ORC, JDBC | Q51(partitionOverwrite), Q59(bucketBy), Q60(saveAsTable), Q61(predicates), Q68(ORC options) |
| Thu | Pandas API integration | Q53(mapInPandas vs applyInPandas), Q62(applyInArrow) |
| Fri | Sorting, hashing, repartition | Q43(array_sort), Q55(xxhash64 vs hash), Q57(repartitionByRange) |
| Sat | Schema, type inspection | Q54(schema.json), Q64(binaryFile), Q99(psdf.spark.schema) |
| Sun | **Practice Test B** | Q41–Q70; score and review all wrong answers |

### Week 3 — Tuning + Streaming (Q71–Q100)

| Day | Focus | Task |
|---|---|---|
| Mon | Tuning: AQE, CBO | Q71(nonEmptyPartitionRatio), Q76(rangeExchange), Q78(forceApply), Q80(prometheus) |
| Tue | Tuning: memory, files | Q72(memoryMapThreshold), Q73(int96Rebase), Q75(ORC vectorize), Q79(serverThreads) |
| Wed | Streaming: query management | Q81(streams.active), Q82(awaitAnyTermination), Q83(checkpoint paths!) |
| Thu | Streaming: output modes, joins | Q85(epochId), Q86(append+groupBy error), Q87(metrics), Q88(stream-stream outer) |
| Fri | Streaming: partitioning, throttle | Q89(partitionBy), Q90(maxBytesPerTrigger) |
| Sat | Spark Connect + Pandas API | Q91–Q95 (Connect), Q96–Q100 (Pandas API) |
| Sun | **Practice Test C** | Q71–Q100; score and review all wrong answers |

### Week 4 — Integration Review + Exam Prep

| Day | Focus | Task |
|---|---|---|
| Mon | Full mock exam | Q1–Q100 timed (75 min); do not check answers mid-test |
| Tue | Analyze mock results | Review every wrong/flagged question with source file |
| Wed | Non-B flashcard drill | 30 reps on Q1, Q3, Q4, Q15, Q31, Q33, Q41, Q45, Q56, Q83, Q85 |
| Thu | Hard question review | All 36 Hard questions (see list below); group by topic |
| Fri | Config cheatsheet from memory | Write all defaults without looking; check against cheatsheet |
| Sat | Pitfalls matrix review | Read every row; mentally explain each correct fact |
| Sun | **Exam Day** | See Exam Day Guide at end of this file |

---

## Practice Test A — Architecture + SQL (Q1–Q40)

Complete this test before checking answers. Mark confidence: ✓ sure / ? unsure / ✗ guessing.

| Q# | Topic | Your Answer | Correct | Tag |
|---|---|---|---|---|
| 1 | Architecture | | **C** | ★ SparkSession/SparkContext relationship |
| 2 | Architecture | | B | shuffle.partitions vs default.parallelism |
| 3 | Architecture | | **C** | ★ YARN total memory math |
| 4 | Architecture | | **C** | ★ Stage count with multiple wide transforms |
| 5 | Architecture | | B | Executor concurrency = cores/cpus |
| 6 | Architecture | | B | Speculative execution risk |
| 7 | Architecture | | B | heartbeatInterval < networkTimeout |
| 8 | Architecture | | B | External shuffle service |
| 9 | Architecture | | B | Kryo serialization benefits |
| 10 | Architecture | | B | Executors per node calculation |
| 11 | Architecture | | B | Rolling event logs |
| 12 | Architecture | | B | Cluster mode driver location |
| 13 | Architecture | | B | openCostInBytes small file grouping |
| 14 | Architecture | | B | reducer.maxSizeInFlight |
| 15 | Architecture | | **A** | ★ compress vs spill.compress |
| 16 | Architecture | | B | broadcast.compress default |
| 17 | Architecture | | B | cleaner.periodicGC.interval |
| 18 | Architecture | | B | Off-heap execution + storage |
| 19 | Architecture | | B | executorIdleTimeout |
| 20 | Architecture | | B | CBO histogram config |
| 21 | SQL | | B | LPAD behavior |
| 22 | SQL | | B | locate with start position |
| 23 | SQL | | B | repeat(str, 0) = empty string |
| 24 | SQL | | B | window() struct output |
| 25 | SQL | | B | unix_timestamp vs to_timestamp return types |
| 26 | SQL | | B | TIMESTAMPADD argument order |
| 27 | SQL | | B | typeof() DDL string |
| 28 | SQL | | B | stack() unpivot |
| 29 | SQL | | B | map_contains_key with null value |
| 30 | SQL | | B | array_position returns 0, not null |
| 31 | SQL | | **A** | ★ reduce() with optional finish arg |
| 32 | SQL | | B | date_part QUARTER |
| 33 | SQL | | **A** | ★ make_interval syntax |
| 34 | SQL | | B | ILIKE ANY multi-pattern |
| 35 | SQL | | B | DECODE with NULL input |
| 36 | SQL | | B | to_csv output |
| 37 | SQL | | B | date_part vs date_trunc difference |
| 38 | SQL | | B | LIKE ANY patterns |
| 39 | SQL | | B | second() returns DoubleType |
| 40 | SQL | | B | to_number vs try_to_number |

**Test A Score: ___ / 40** — Target: 36+ before exam

---

## Practice Test B — DataFrame API (Q41–Q70)

| Q# | Topic | Your Answer | Correct | Tag |
|---|---|---|---|---|
| 41 | DataFrame | | **A** | ★ withMetadata schema field access |
| 42 | DataFrame | | B | ~ (bitwise NOT) on boolean column |
| 43 | DataFrame | | B | array_sort with custom comparator |
| 44 | DataFrame | | B | window_time() for watermark |
| 45 | DataFrame | | **A** | ★ collect_list running window |
| 46 | DataFrame | | B | withWatermark on batch = no-op |
| 47 | DataFrame | | B | df.observe() and StreamingQueryListener |
| 48 | DataFrame | | B | F.rint() banker's rounding |
| 49 | DataFrame | | B | Global temp view namespace |
| 50 | DataFrame | | B | approx_percentile vs approxQuantile accuracy |
| 51 | DataFrame | | B | partitionOverwriteMode=dynamic |
| 52 | DataFrame | | B | F.nullif semantics |
| 53 | DataFrame | | B | mapInPandas vs applyInPandas |
| 54 | DataFrame | | B | schema.json() content |
| 55 | DataFrame | | B | xxhash64 vs hash return types |
| 56 | DataFrame | | **A** | ★ F.lit(None) NullType and Parquet |
| 57 | DataFrame | | B | repartitionByRange vs repartition |
| 58 | DataFrame | | B | regexp_extract_all returns array |
| 59 | DataFrame | | B | bucketBy requires saveAsTable |
| 60 | DataFrame | | B | saveAsTable schema validation |
| 61 | DataFrame | | B | JDBC predicates vs partitionColumn |
| 62 | DataFrame | | B | applyInArrow vs applyInPandas |
| 63 | DataFrame | | B | F.raise_error() exception type |
| 64 | DataFrame | | B | binaryFile source columns |
| 65 | DataFrame | | B | Delta overwrite schema option |
| 66 | DataFrame | | B | stat.cov vs stat.corr |
| 67 | DataFrame | | B | Temp view vs global temp view scope |
| 68 | DataFrame | | B | ORC vs Parquet compression option keys |
| 69 | DataFrame | | B | array_min null behavior |
| 70 | DataFrame | | B | df.offset().limit() API |

**Test B Score: ___ / 30** — Target: 27+ before exam

---

## Practice Test C — Streaming + Connect + Pandas API (Q71–Q100)

| Q# | Topic | Your Answer | Correct | Tag |
|---|---|---|---|---|
| 71 | Tuning | | B | nonEmptyPartitionRatioForBroadcastJoin |
| 72 | Tuning | | B | memoryMapThreshold mmap behavior |
| 73 | Tuning | | B | parquet INT96 rebase mode |
| 74 | Tuning | | B | caseSensitive=false ambiguous column |
| 75 | Tuning | | B | orc.impl=native for vectorized reads |
| 76 | Tuning | | B | rangeExchange.sampleSizePerPartition |
| 77 | Tuning | | B | planChangeLog.level for AQE |
| 78 | Tuning | | B | adaptive.forceApply |
| 79 | Tuning | | B | shuffle.io.serverThreads |
| 80 | Tuning | | B | ui.prometheus.enabled |
| 81 | Streaming | | B | spark.streams.active |
| 82 | Streaming | | B | awaitAnyTermination |
| 83 | Streaming | | **A** | ★ Shared checkpoint corruption |
| 84 | Streaming | | B | query.exception() return values |
| 85 | Streaming | | **A** | ★ epochId for idempotent foreachBatch |
| 86 | Streaming | | B | append mode + groupBy without watermark |
| 87 | Streaming | | B | streaming.metricsEnabled |
| 88 | Streaming | | B | stream-stream outer join watermark requirement |
| 89 | Streaming | | B | writeStream.partitionBy() |
| 90 | Streaming | | B | maxBytesPerTrigger throttle |
| 91 | Connect | | B | Spark Connect gRPC port |
| 92 | Connect | | B | Client plan building and protobuf execution |
| 93 | Connect | | B | spark.sparkContext in Connect client |
| 94 | Connect | | B | pyspark[connect] dependencies |
| 95 | Connect | | B | Connect extension registration |
| 96 | Pandas API | | B | groupby().transform() semantics |
| 97 | Pandas API | | B | psdf.spark.apply() escape hatch |
| 98 | Pandas API | | B | plot() and compute.max_rows |
| 99 | Pandas API | | B | psdf.spark.schema returns StructType |
| 100 | Pandas API | | B | MultiIndex support |

**Test C Score: ___ / 30** — Target: 27+ before exam

---

## Pitfalls Matrix (30+ rows)

| Concept | Wrong Assumption | Correct Fact | Q# |
|---|---|---|---|
| SparkSession vs SparkContext | SparkSession IS the SparkContext | SparkSession **wraps** SparkContext; access via `spark.sparkContext` | Q1 |
| YARN container memory | heap + overhead = total | heap + overhead + offHeap = total | Q3 |
| Stage count | Each wide transform = 1 stage | N wide transforms = N+1 stages (each adds 1 boundary) | Q4 |
| shuffle.spill.compress | Same as shuffle.compress | spill.compress = intermediate spill files; compress = output blocks | Q15 |
| reduce() finish arg | reduce(arr, init, func) is complete | 4th arg `finish` applied to final accumulator before returning | Q31 |
| make_interval | `dateadd` or interval literal only | `ts + make_interval(years, months)` is valid direct arithmetic | Q33 |
| withMetadata | Returns modified column type | Returns same DataFrame; access via `df.schema["col"].metadata` | Q41 |
| collect_list window default frame | Entire window or last row | Default `orderBy()` RANGE frame → running cumulative list | Q45 |
| F.lit(None) | Creates nullable column for Parquet | Creates NullType; must cast: `F.lit(None).cast("string")` | Q56 |
| Shared checkpoint | Shared path is fine across queries | State corruption; each query needs unique checkpoint path | Q83 |
| foreachBatch at-exactly-once | foreachBatch is at-least-once | epochId = unique deduplication key; same epochId = retry → skip | Q85 |
| array_position miss | Returns null if not found | Returns 0 (Long); always check > 0 not IS NOT NULL | Q30 |
| map_contains_key | map[key] IS NOT NULL is equivalent | map[key] IS NOT NULL misses entries where key→null | Q29 |
| to_number vs try_to_number | Both tolerate format mismatch | to_number raises exception; try_to_number returns null | Q40 |
| locate() return | 0-indexed position | 1-indexed; returns 0 if not found | Q22 |
| repeat(str, 0) | Returns null for zero repetitions | Returns empty string `''` | Q23 |
| xxhash64 vs hash | Both return same type | xxhash64 → LongType (64-bit); hash → IntegerType (32-bit) | Q55 |
| rint() rounding | Always rounds 0.5 up | Banker's rounding: 2.5→2.0, 3.5→4.0 | Q48 |
| approx_percentile accuracy | Higher is better | Higher = more accurate (lower relative error) | Q50 |
| approxQuantile relError | Higher is better | Lower relError = more accurate (inverse of accuracy) | Q50 |
| repartitionByRange | Same as repartition | repartition = hash-based; repartitionByRange = quantile/sort-based | Q57 |
| partitionOverwriteMode | Overwrites ALL partitions by default | Default is static (overwrite all); set dynamic to overwrite only touched | Q51 |
| withWatermark on batch | Same as streaming | Silently ignored on batch DataFrames | Q46 |
| Append mode + groupBy | Always works | Without watermark → AnalysisException at planning time | Q86 |
| Stream-stream outer join | Only one stream needs watermark | BOTH streams must have withWatermark for outer join | Q88 |
| spark.sparkContext in Connect | Available via SparkSession | Raises PySparkNotImplementedError; use DataFrame APIs instead | Q93 |
| Spark Connect port | Standard web port | gRPC port 15002 (not 4040 which is Spark UI) | Q91 |
| temp view scope | Shared across sessions | Session-scoped; global_temp.view shared across sessions same JVM | Q49/Q67 |
| orc.compress option | Same as parquet compression key | ORC: `orc.compress`=`zlib`; Parquet: `compression`=`snappy` | Q68 |
| CBO histograms | Always collected | Must set `statistics.histogram.enabled=true` explicitly | Q20 |
| heartbeatInterval vs networkTimeout | Can be any values | heartbeatInterval MUST be < networkTimeout | Q7 |
| openCostInBytes | Used for executor allocation | Used for grouping small input files into partitions | Q13 |
| Kryo registration | Optional for performance | Required for custom classes; `spark.kryo.classesToRegister` | Q9 |
| executorIdleTimeout | Applies always | Only active when dynamic allocation is enabled | Q19 |
| schema.json() | Same as simpleString() | json() includes nullable and metadata fields; simpleString() is compact DDL | Q54 |

---

## Hard Question Flash Cards (36 Questions)

Study both sides before practice tests. Cover the back, say the answer, then check.

### Architecture Flash Cards

**Q3 — YARN Memory Math**
- Front: Executor: 4GB heap, 512MB overhead, 1GB offHeap. What does YARN allocate?
- Back: **C — 5.5 GB** (heap + overhead + offHeap = 4+0.5+1 = 5.5)

**Q4 — Stage Count**
- Front: Query has groupByKey + join + 3 filters + 2 maps. How many stages?
- Back: **C — 3 stages** (each wide transform adds 1 boundary: groupByKey→2 stages, join→3 stages)

**Q5 — Concurrent Tasks**
- Front: executor.cores=8, spark.task.cpus=2. How many concurrent tasks per executor?
- Back: **B — 4** (8/2 = 4)

**Q7 — Timeout Config Order**
- Front: What constraint must hold between heartbeatInterval and networkTimeout?
- Back: **B — heartbeatInterval < networkTimeout** (heartbeat must arrive before timeout triggers)

**Q9 — Kryo Benefits**
- Front: What are the quantified benefits of Kryo over Java serialization?
- Back: **B — 5-10× faster, 2-5× smaller**; needs `spark.kryo.classesToRegister` for custom classes

**Q11 — Rolling Event Logs**
- Front: How do you prevent event logs growing unbounded in long-running apps?
- Back: **B — `spark.eventLog.rolling.enabled=true`** splits into size-bounded files

**Q13 — Small File Grouping**
- Front: What config controls when Spark groups small input files into one partition?
- Back: **B — `spark.sql.files.openCostInBytes`** (default 4MB)

**Q15 — Shuffle Compress vs Spill Compress ★A**
- Front: Difference between `spark.shuffle.compress` and `spark.shuffle.spill.compress`?
- Back: **A** — `shuffle.compress` = final output shuffle blocks; `spill.compress` = intermediate spill files written when sort buffer is full

**Q18 — Off-Heap Memory**
- Front: When off-heap is enabled, which memory operations use it?
- Back: **B — BOTH execution (shuffle/sort) AND storage (cache)** use off-heap

### SQL Flash Cards

**Q26 — TIMESTAMPADD**
- Front: Add 3 hours to timestamp. Correct TIMESTAMPADD syntax?
- Back: **B — `TIMESTAMPADD('HOUR', 3, ts)`** — unit FIRST, then delta, then timestamp

**Q29 — map_contains_key**
- Front: Map `{key: null}`. Does `map_contains_key(m, key)` return true?
- Back: **B — YES** — `map_contains_key` is true even when value is null; `m[key] IS NOT NULL` would miss it

**Q31 — reduce() finish arg ★A**
- Front: `reduce(array(1,2,3,4), 0, (acc,x)->acc+x, x->x*2)`. What does 4th arg do?
- Back: **A — `finish` arg transforms final accumulator** before returning; result = (0+1+2+3+4)*2 = 20

**Q34 — ILIKE ANY**
- Front: Case-insensitive multi-pattern match in Spark 3.3+?
- Back: **B — `col ILIKE ANY ('pat1', 'pat2')`** — Spark 3.3+; ILIKE = case-insensitive LIKE

**Q38 — LIKE ANY**
- Front: Match against multiple patterns with OR logic?
- Back: **B — `col LIKE ANY ('click_%', 'tap_%')`** — Spark 3.3+

**Q40 — to_number vs try_to_number**
- Front: `to_number('abc', '999')` — what happens?
- Back: **B — raises exception**; use `try_to_number('abc', '999')` to return null instead

### DataFrame Flash Cards

**Q44 — window_time()**
- Front: How to get the window end timestamp compatible with watermarks?
- Back: **B — `F.window_time(windowCol)`** (Spark 3.4+); plain `windowCol.end` breaks watermark

**Q47 — df.observe()**
- Front: Where does `df.observe("name", ...)` metric appear in streaming?
- Back: **B — `query.recentProgress["observedMetrics"]["name"]`** or `progress.observedMetrics["name"]` in StreamingQueryListener

**Q50 — Accuracy Direction**
- Front: `approx_percentile(accuracy=10000)` vs `approxQuantile(relError=0.001)`. Which is more accurate?
- Back: **B** — for `approx_percentile`: higher=more accurate; for `approxQuantile`: lower relError=more accurate (opposite conventions!)

**Q53 — mapInPandas vs applyInPandas**
- Front: Which requires a groupBy, which doesn't?
- Back: **B — `applyInPandas` requires groupBy** (applied per group); **`mapInPandas`** = no groupBy, iterates all partitions

**Q55 — xxhash64 vs hash**
- Front: Return types of `F.xxhash64(*cols)` and `F.hash(*cols)`?
- Back: **B — xxhash64 → LongType (64-bit); hash → IntegerType (32-bit MurmurHash3)**

**Q57 — repartitionByRange**
- Front: How does `repartitionByRange` differ from `repartition`?
- Back: **B — repartitionByRange = quantile sampling + range-based assignment** (sort-compatible); `repartition` = hash-based (random distribution)

**Q60 — saveAsTable schema validation**
- Front: Appending to existing table with different schema via `saveAsTable`. What happens?
- Back: **B — AnalysisException**; use `.option("overwriteSchema", "true")` when overwriting, or match schema when appending

**Q62 — applyInArrow**
- Front: What is the advantage of `applyInArrow` vs `applyInPandas`?
- Back: **B — processes Apache Arrow RecordBatch directly** (no Pandas conversion overhead); Spark 3.3+

**Q65 — Delta overwrite schema**
- Front: How to overwrite a Delta table and change its schema?
- Back: **B — `.option("overwriteSchema", "true")`** required in addition to write mode "overwrite"

**Q68 — ORC vs Parquet compression keys**
- Front: Option key for compression in ORC? In Parquet?
- Back: **B — ORC: `orc.compress`=`zlib`; Parquet: `compression`=`snappy`** (different keys!)

**Q70 — offset().limit()**
- Front: SQL `SELECT * FROM t LIMIT 50 OFFSET 100` equivalent in DataFrame API?
- Back: **B — `df.offset(100).limit(50)`** (Spark 3.4+)

### Tuning Flash Cards

**Q71 — nonEmptyPartitionRatio**
- Front: AQE converts sort-merge join to broadcast join when what condition is met?
- Back: **B — fewer than `nonEmptyPartitionRatioForBroadcastJoin` (0.2 = 20%) of post-shuffle partitions are non-empty**

**Q73 — Parquet INT96 rebase**
- Front: Writing timestamp data that will be read by Hive (Julian calendar)?
- Back: **B — `spark.sql.parquet.int96RebaseModeInWrite=LEGACY`** writes Julian-compatible timestamps

**Q75 — ORC vectorized reads**
- Front: What config enables vectorized ORC reads?
- Back: **B — `spark.sql.orc.impl=native`** (default since 2.3); also `orc.enableVectorizedReader=true`

**Q76 — Range sampling**
- Front: Sorted shuffle partitions are uneven. What config helps?
- Back: **B — increase `spark.sql.execution.rangeExchange.sampleSizePerPartition`** (default 100)

**Q79 — FetchFailedException**
- Front: Shuffle fetch failures under high load. What config to tune?
- Back: **B — `spark.shuffle.io.serverThreads`** — increase Netty server thread pool size

### Streaming Flash Cards

**Q83 — Shared Checkpoint Path ★A**
- Front: Two streaming queries share the same checkpointLocation. What is the risk?
- Back: **A — state corruption**; each query MUST have its own unique checkpoint directory

**Q85 — foreachBatch epochId ★A**
- Front: How to make foreachBatch idempotent (handle retries without duplicates)?
- Back: **A — use `epochId` as a transactional dedup key**; on retry, same epochId → skip already-processed batch

**Q86 — Append + groupBy without watermark**
- Front: `df.groupBy("key").count().writeStream.outputMode("append")` — what happens?
- Back: **B — AnalysisException at planning time**; append mode with aggregation requires watermark

**Q88 — Stream-stream outer join**
- Front: Outer join of two streaming DataFrames — watermark requirement?
- Back: **B — BOTH streams must have `withWatermark()`** (not just one)

### Spark Connect Flash Card

**Q93 — spark.sparkContext in Connect**
- Front: Client code calls `spark.sparkContext.parallelize([1,2,3])`. Client uses Spark Connect.
- Back: **B — PySparkNotImplementedError**; use `spark.createDataFrame([(1,),(2,),(3,)])` instead

### Pandas API Flash Cards

**Q98 — plot() and max_rows**
- Front: `psdf["price"].plot()` on 1M-row DataFrame. How much data is plotted?
- Back: **B — first `compute.max_rows` rows** (default 1000); internally calls `toPandas()` on that subset

---

## Exam Day Guide

### Before You Start

1. Write on scratch paper:
   - **89B / 8A / 3C**
   - **A answers: Q15, Q31, Q33, Q41, Q45, Q56, Q83, Q85**
   - **C answers: Q1, Q3, Q4 (ALL in Architecture)**

2. Time allocation for 100 questions (75 minutes):
   - Target: 45 seconds per question average
   - Flag any question taking > 90 seconds, move on, return later
   - Reserve 10 minutes at end for flagged questions

### Architecture Section (Q1–Q20) — C-Alert Zone

- **Automatically flag Q1, Q3, Q4** for review — confirm C is correct
- Q1: Is this about the wrapping relationship? → C
- Q3: Is this a memory addition problem? Add heap + overhead + offHeap → C
- Q4: Count the wide transforms, add 1 → C

### When You Are Unsure

```
1. Is it about one of the 11 non-B topics? → check your scratch paper
2. Does option B describe the standard, expected behavior? → probably B
3. Do two options seem equivalent? → pick B (89% base rate)
4. Is the question in Architecture (Q1-20)? → double-check against C possibility
5. Still unsure? → B (the default)
```

### Confidence Categories

- **Green (answer immediately):** Q1, Q3, Q4, Q15, Q31, Q33, Q41, Q45, Q56, Q83, Q85 — you know these cold
- **Yellow (verify once):** Hard questions you studied; check your logic once then commit
- **Red (flag and return):** Any question where you read option text and feel confused; come back fresh

### Common Exam Traps Recap

| Trap | Remember |
|---|---|
| "Mostly B, so this must be B" | 11 questions are NOT B — don't skip thinking |
| "It was B in Iter 8" | Iter 8 and 9 have DIFFERENT non-B sets |
| YARN memory | offHeap is ADDED to heap+overhead |
| Stage count | Each wide transform adds exactly one boundary |
| array_position miss | Returns 0 (zero), not null |
| map_contains_key | True even with null value for the key |
| F.lit(None) | NullType — must cast before writing to typed format |
| to_number fail | Raises exception (not null); use try_to_number for null |
| Checkpoint sharing | Never share; unique path per query |
| Append + groupBy | Needs watermark or will fail at planning |

### Final 5-Minute Check

Before submitting:
- Verify you answered all 100 questions
- Re-check any flagged questions
- Confirm Q1=C, Q3=C, Q4=C on scratch paper vs exam
- Confirm Q83=A, Q85=A — the streaming non-B answers are easy to forget under pressure
