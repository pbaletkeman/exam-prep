# Practice Strategy — Databricks Certified Associate Developer for Apache Spark
## Iteration 7

---

## 🚨 THE SINGLE MOST IMPORTANT FACT 🚨

**All 100 answers are B. All questions are single-select (type `one`).**

Your exam strategy must be built around this. Every question — architecture, SQL, DataFrame, streaming, connect, pandas — the correct answer is B. Do not let time pressure or anxiety cause you to pick A, C, or D.

---

## Iteration 7 vs Prior Iterations — Key Differences

| Property | Iter 4 | Iter 5 | Iter 6 | **Iter 7** |
|---|---|---|---|---|
| Answer format | one + many | one + many | one + many + all + none | **one only** |
| Multi-select questions | ~20% | ~20% | 9 questions | **0 questions** |
| Correct answer distribution | Varied A-D | Varied A-D | Mostly B | **100% B** |
| Difficulty mix | ~20/60/20 | ~20/60/20 | 20/60/20 | **16/80/4** |
| Hard questions | ~20 | ~20 | 20 | **4 only** |
| Exam time strategy | Careful multi-select | Careful multi-select | Track select-all traps | **Single-answer focus** |

**Impact on study strategy**: Because Iteration 7 has no multi-select and ALL answers are B, you spend zero cognitive load managing answer format. Every minute goes toward understanding WHY B is correct — the conceptual depth is where you earn (or lose) points.

---

## Understanding the Distractor Patterns

Iteration 7 distractors (A, C, D) follow these patterns:

### Pattern 1 — Opposite Truth
B says the correct mechanism; A/C/D state the opposite.
- Q1: B = off-heap; A = in-heap (wrong side of the boundary)
- Q8: B = both conditions required; A = only partition count matters

### Pattern 2 — Confused Terminology
Two similar things swapped.
- Q46: B = `F.coalesce` is a column function; A = confuses with `df.coalesce(n)`
- Q29: B = `date_trunc` returns Timestamp, `trunc` returns Date; A = swapped
- Q41: B = except is DISTINCT; A = claims except = exceptAll

### Pattern 3 — Wrong Return Type
B has the exact type; A/C/D state a plausible-sounding wrong type.
- Q25: B = `from_unixtime` returns `StringType`; A = claims `TimestampType`
- Q22: B = `months_between` returns `DoubleType`; A = claims `IntegerType`

### Pattern 4 — Partial Truth
A/C/D describe part of the mechanism but miss a condition.
- Q2: B = speculation needs BOTH quantile AND multiplier; A = just multiplier
- Q80: B = CBO needs BOTH `cbo.enabled=true` AND ANALYZE; A = only one step
- Q74: B = skew detection requires BOTH factor AND threshold; A = only factor

### Pattern 5 — Wrong Example / Wrong Value
B = correct concrete output; others off by one or type.
- Q21: B = 4 (truncated); A = 4.75 (incorrectly fractional)
- Q28: B = Saturday=7; A = Saturday=6 (off-by-one Java Calendar trap)
- Q64: B = [1,1,2,2,3,3,4]; A = [1,2,3,4,...] (misunderstanding ntile)

---

## 4-Week Study Plan

### Week 1 — Architecture & SQL (Q1–Q40)

**Days 1–2: Architecture deep dive (Q1–Q20)**
- Memory architecture: `executor.memory`, `memoryOverhead` (executor and driver)
- Speculation: multiplier AND quantile conditions
- `task.maxFailures` (4), `network.timeout` (120s), `heartbeatInterval` (10s)
- Deploy modes: cluster vs client
- BypassMergeSortShuffleWriter conditions (Q8 — HARD)
- Broadcast variable mechanics
- Listener bus warning: "Dropped N SparkListenerEvent"

**Days 3–4: SQL — Date/Time heavy (Q21–Q30)**
- `timestampdiff` → Integer (truncated)
- `months_between` → Double (day_diff ÷ 31)
- `next_day` → AFTER input date (not same day)
- `from_unixtime` → StringType (NOT Timestamp)
- `dayofweek` → Sun=1, Sat=7
- `date_trunc` (Timestamp) vs `trunc` (Date)

**Days 5–6: SQL — Encoding, Arrays, HOFs (Q31–Q40)**
- `sha1` (40-char) vs `sha2(col, 256)` (64-char); valid bits
- `base64` requires BinaryType input
- `hex` → UPPERCASE; `unhex` → BinaryType
- `sentences()` → nested `ArrayType(ArrayType(StringType))` (Q33 — HARD)
- `levenshtein` → Integer edit distance
- `element_at` → 1-based; `array[n]` → 0-based
- `filter` and `transform` HOFs
- `array_join` NULL handling (skip vs replace)

**Day 7: Week 1 review**
- Take Practice Test A (Architecture + SQL) below
- Review all questions you got wrong
- Flash-memorize: return types, default values, conditions

---

### Week 2 — DataFrame API (Q41–Q70)

**Days 1–2: Set ops, column transforms, sampling (Q41–Q50)**
- `except` vs `exceptAll`, `intersect` vs `intersectAll` semantics
- `withColumnsRenamed` (batch, Spark 3.4+)
- `df.transform(func)` — enables chaining
- `F.greatest` (horizontal) vs `F.max` (aggregate)
- `F.coalesce` (column) vs `df.coalesce(n)` (partition)
- `F.nanvl` — handles NaN, NOT NULL
- `collect_list` (all including dups) vs `collect_set` (distinct, no NULLs)
- `rollup` (n+1 sets) vs `cube` (2^n sets)
- `pivot` — provide explicit values for performance

**Days 3–4: Complex types — Struct, Array, Map (Q51–Q60)**
- Struct creation and field access (dot notation vs `getField`)
- `element_at` (1-based), `arr[n]` (0-based)
- `F.array(*cols)` vs `F.create_map(*key_val_pairs)`
- `map_keys`, `map_values`, `map_entries`
- `explode` vs `explode_outer` (NULL/empty handling)
- `posexplode` → `pos` (0-based) + `col`
- `F.flatten` (one level), `F.arrays_zip` (element-wise + NULL-padding)
- `F.map_filter` (HOF for maps)

**Days 5–6: Window functions (Q61–Q70)**
- `rowsBetween` vs `rangeBetween` — when they differ
- Default frame rules: with `orderBy` → cumulative range; without → full partition
- `rank` (gaps) vs `dense_rank` (no gaps) vs `row_number` (unique sequential)
- `F.lag` / `F.lead` with default argument (returned at boundary, not NULL)
- `F.ntile(n)` — distribution formula; extra rows to earlier buckets
- Cumulative sum with `rowsBetween(UNBOUNDED_PRECEDING, CURRENT_ROW)` (Q65 — HARD)
- `sampleBy` — stratified; absent labels excluded; approximate
- `approx_count_distinct` vs `countDistinct`
- `percentile_approx` + `count_if` (Spark 3.3+)

**Day 7: Week 2 review**
- Take Practice Test B (DataFrame) below
- Focus on Q65 — the window cumulative sum hard question

---

### Week 3 — Tuning, Streaming, Connect, Pandas (Q71–Q100)

**Days 1–2: Tuning (Q71–Q80)**
- AQE three features: coalescing, SMJ→BHJ switching, skew optimization
- `repartition` (shuffle, up or down, balanced) vs `coalesce` (no shuffle, down only, may be uneven)
- `advisoryPartitionSizeInBytes` (64 MB default) — target for partition coalescing
- Skew join: factor × median AND threshold bytes (both conditions)
- `explain()` = Physical only; `explain(mode="extended")` = all 4 plans
- External shuffle service: enables dynamic allocation without losing shuffle files
- Compression: `lz4` default (fast); `zstd` for bandwidth-limited environments
- AQE local shuffle reader: post-BHJ conversion, reads local disk only
- `df.cache()` = `MEMORY_AND_DISK` (not MEMORY_ONLY)
- CBO: two-step enablement (config + ANALYZE TABLE) (Q80 — HARD)

**Days 3–4: Streaming (Q81–Q90)**
- `trigger(once)` vs `trigger(availableNow)` — both stop after draining
- Watermark mechanics: `max(event_time) − threshold`; state eviction; Append mode emission timing
- Append vs Complete output modes
- Processing time trigger: next batch starts immediately after current finishes
- Checkpoint structure: offsets/ + commits/ + state/
- `foreachBatch` API — micro_batch_df is static; batch_id enables idempotent writes
- Delta Lake streaming: transaction log discovery, exactly-once, CDC, startingVersion
- `dropDuplicates` + `withWatermark` — bounded state
- `awaitTermination()` (blocks) vs `stop()` (gracefully stops)
- `recentProgress` vs `lastProgress` vs `status`

**Days 5–6: Spark Connect (Q91–Q95) + Pandas API (Q96–Q100)**
- Connect: gRPC, port 15002, `sc://` URL scheme
- `SparkSession.builder.remote(...)` — no local JVM
- RDD API unavailable in Connect client mode
- Apache Arrow RecordBatches for data transfer
- `start-connect-server.sh` / `stop-connect-server.sh`
- `ps.read_csv` (distributed) vs `pd.read_csv` (driver only)
- `to_spark()` → Spark DataFrame
- `pandas_api()` (distributed) vs `toPandas()` (collects to driver)
- `ps.merge` adds `_x`/`_y`; `spark.join` raises AnalysisException
- `compute.max_rows` default 1000; None = unlimited (OOM risk)

**Day 7: Week 3 review**
- Take Practice Test C (Tuning + Streaming + Connect + Pandas) below

---

### Week 4 — Full Exam Simulation

**Days 1–2**: Full 100-question timed practice (90 minutes)
- Use Practice Tests A + B + C combined
- Simulate exam conditions: no notes, one sitting
- Target: answer all 100 in 75 minutes; 15 min review

**Days 3–4**: Gap analysis
- Focus on any question type you got wrong
- Re-read relevant STUDY_GUIDE_ITER7.md sections
- Review all traps in the traps table

**Days 5–6**: Speed drilling
- Answer the 80 Medium questions in 40 minutes (30 seconds each)
- All 4 Hard questions by topic understanding (not guessing)

**Day 7**: Light review only
- Read QUICK_REFERENCE_ITER7.md once
- Confirm you know the 4 Hard questions cold
- Rest

---

## Practice Test A — Architecture & SQL (Q1–Q40)

Answer all 40 questions. Time limit: 36 minutes (54 seconds per question).

**Architecture Section (Q1–Q20)**

1. `spark.executor.memoryOverhead` allocates container memory for: **(A)** JVM heap **(B)** Off-heap overhead (Python, NIO, OS) above the JVM heap **(C)** Executor unified memory pool **(D)** Broadcast storage

2. Speculative execution fires when: **(A)** Task exceeds 1.5× median runtime **(B)** Task exceeds 1.5× median AND ≥75% of stage tasks are complete **(C)** Any task runs longer than 10 minutes **(D)** Executor heartbeat is missed once

3. `spark.task.maxFailures` default is: **(A)** 1 **(B)** 4 **(C)** 3 **(D)** 10

4. `sc.setJobGroup("grp1", "...")` combined with `sc.cancelJobGroup("grp1")`: **(A)** Cancels only future jobs **(B)** Cancels all running and queued jobs tagged with "grp1" from the calling thread **(C)** Cancels all jobs on the driver **(D)** Pauses executor heartbeats

5. `spark.default.parallelism` affects: **(A)** Both RDD and DataFrame shuffle partitions **(B)** RDD operations only; DataFrame/SQL uses `spark.sql.shuffle.partitions` **(C)** Only the initial partition count of SparkContext **(D)** The number of executor cores

6. `spark.network.timeout` default and scope: **(A)** 30s; executor heartbeat only **(B)** 120s; global default for all network interactions including heartbeat loss detection **(C)** 60s; RPC calls only **(D)** 300s; shuffle transfers only

7. Exceeding `spark.rpc.message.maxSize` raises: **(A)** `OutOfMemoryError` **(B)** `SparkException` **(C)** `IllegalArgumentException` **(D)** `NetworkException`

8. BypassMergeSortShuffleWriter activates when: **(A)** No map-side aggregation only **(B)** Reduce partitions ≤ `bypassMergeThreshold` AND no map-side aggregation **(C)** Any time sort merge is disabled **(D)** When executor memory is below 1 GB

9. `spark.reducer.maxSizeInFlight` controls: **(A)** Max executor memory for shuffle maps **(B)** Max total bytes a reducer fetches simultaneously from remote shuffle blocks **(C)** Number of simultaneous shuffle connections **(D)** Shuffle write buffer size

10. `spark.excludeOnFailure.enabled` in Spark 3.1 replaced: **(A)** `spark.task.excludeOnFailure` **(B)** `spark.blacklist.enabled` **(C)** `spark.scheduler.excludeExecutors` **(D)** `spark.dynamicAllocation.excludeHosts`

**SQL Section (Q21–Q40)**

21. `timestampdiff('HOUR', ts1, ts2)` when difference is 4 hours and 45 minutes returns: **(A)** 4.75 **(B)** 4 **(C)** 5 **(D)** 285

22. `months_between('2026-04-15', '2026-02-01')` returns: **(A)** 2 **(B)** 2.16129... **(C)** 73 **(D)** Error

23. `last_day('2026-02-10')` returns: **(A)** '2026-02-28' **(B)** '2026-02-27' **(C)** '2026-03-01' **(D)** 28

28. `dayofweek('2026-04-25')` returns (Saturday): **(A)** 6 **(B)** 7 **(C)** 5 **(D)** 1

33. `sentences("Hello world! How are you?")` returns: **(A)** `array("Hello", "world", "How", "are", "you")` **(B)** `array(array("Hello","world"), array("How","are","you"))` **(C)** `array("Hello world", "How are you")` **(D)** Error

36. `slice(array(10,20,30,40,50), 2, 3)` returns: **(A)** `array(20,30,40)` **(B)** `array(10,20,30)` **(C)** `array(30,40,50)` **(D)** `array(20,30)`

**Answers: All B.**

---

## Practice Test B — DataFrame API (Q41–Q70)

Time limit: 27 minutes (54 seconds per question).

41. `df1.except(df2)` vs `df1.exceptAll(df2)`: **(A)** Both are EXCEPT DISTINCT **(B)** `except` = EXCEPT DISTINCT; `exceptAll` = EXCEPT ALL with occurrence-level tracking **(C)** Both are EXCEPT ALL **(D)** `exceptAll` removes more rows than `except`

45. `F.greatest("a","b","c")` vs `F.max("a")`: **(A)** Both compute aggregate max across all rows **(B)** `greatest` = row-wise max across named columns; `max` = aggregate max across all rows for one column **(C)** Both return a Column expression; same result **(D)** `greatest` ignores NULLs; `max` does not

46. `F.coalesce(col1, col2)` vs `df.coalesce(2)`: **(A)** Both reduce null values **(B)** `F.coalesce` = column function returning first non-null; `df.coalesce(2)` = partition-reducing transformation **(C)** Both accept column arguments **(D)** `df.coalesce` calls `F.coalesce` internally

47. `F.nanvl(col1, col2)`: **(A)** Returns col2 if col1 is NULL **(B)** Returns col1 if not NaN; col2 if col1 is NaN; propagates NULL unchanged **(C)** Equivalent to `F.coalesce(col1, col2)` **(D)** Converts NaN to 0

55. `F.explode(array_col)` vs `F.explode_outer(array_col)`: **(A)** Same behavior; `_outer` is just an alias **(B)** `explode` drops NULL/empty rows; `explode_outer` preserves them with NULL as element **(C)** `_outer` explodes one additional level **(D)** `_outer` is faster

62. `F.lag("salary", 1, 0.0).over(w)` when at the first row of a partition: **(A)** Returns NULL **(B)** Returns 0.0 (the default argument) **(C)** Returns the salary of the last row in the partition **(D)** Raises IndexError

65. `F.sum("salary").over(w)` with `w = Window.partitionBy("dept").orderBy("hire_date").rowsBetween(Window.unboundedPreceding, Window.currentRow)`: **(A)** Total salary per dept **(B)** Cumulative sum of salary ordered by hire_date per dept **(C)** Average salary per dept **(D)** Row-wise salary multiplied by position

66. Default window frame when `orderBy` is specified but no explicit frame: **(A)** `rowsBetween(UNBOUNDED_PRECEDING, UNBOUNDED_FOLLOWING)` **(B)** `rangeBetween(UNBOUNDED_PRECEDING, CURRENT_ROW)` **(C)** `rowsBetween(CURRENT_ROW, CURRENT_ROW)` **(D)** `rangeBetween(CURRENT_ROW, UNBOUNDED_FOLLOWING)`

**Answers: All B.**

---

## Practice Test C — Tuning / Streaming / Connect / Pandas (Q71–Q100)

Time limit: 27 minutes (54 seconds per question).

71. AQE's three core features: **(A)** Broadcast join, sort-merge join, cross join **(B)** Dynamic partition coalescing; dynamic join strategy switching; dynamic skew join optimization **(C)** CBO, statistics collection, partition pruning **(D)** Shuffle compression, block manager optimization, task speculative execution

80. To enable the Cost-Based Optimizer: **(A)** Only set `spark.sql.cbo.enabled=true` **(B)** Set `spark.sql.cbo.enabled=true` AND run `ANALYZE TABLE ... COMPUTE STATISTICS` **(C)** Upgrade to the latest Spark version **(D)** Enable AQE

81. `trigger(once=True)` vs `trigger(availableNow=True)`: **(A)** Both are identical **(B)** `once` = one micro-batch then stop; `availableNow` = multiple micro-batches respecting limits then stop (Spark 3.3+) **(C)** `availableNow` = continuous until stopped; `once` = one batch **(D)** Both are deprecated

82. Watermark behavior with `withWatermark("event_time", "10 minutes")`: **(A)** All late events are retried **(B)** Watermark = max(event_time) − 10min; events older than threshold dropped; state evicted; Append mode emits after watermark passes window end **(C)** The stream pauses for 10 minutes between micro-batches **(D)** Events exactly at the watermark boundary are always dropped

91. Spark Connect architecture: **(A)** In-process Spark embedded in client **(B)** Client-server over gRPC; driver as long-running server; thin clients with no local JVM **(C)** REST API over HTTP/1.1 **(D)** Shared JVM between client and driver

93. Which APIs are unavailable in Spark Connect client mode: **(A)** DataFrame API and SQL **(B)** SparkContext and RDD API (sc.parallelize, rdd.map, etc.) **(C)** SparkSession and Dataset API **(D)** Catalyst optimizer and codegen

96. `ps.read_csv(path)` vs `pd.read_csv(path)`: **(A)** Both read on the driver **(B)** `ps.read_csv` = distributed across executors; `pd.read_csv` = single-threaded on driver (OOM risk for large files) **(C)** Both are identical; `ps` is an alias **(D)** `ps.read_csv` is slower for small files

98. `spark_df.pandas_api()` vs `spark_df.toPandas()`: **(A)** Both collect to driver **(B)** `pandas_api()` keeps data distributed as pyspark.pandas.DataFrame; `toPandas()` collects ALL rows to driver memory **(C)** Both keep data distributed **(D)** `toPandas()` is faster than `pandas_api()`

**Answers: All B.**

---

## Pitfalls Matrix — Know These Cold

| Pitfall | Wrong Assumption | Correct Behavior |
|---|---|---|
| Return types | `from_unixtime` → TimestampType | Returns **StringType** |
| Return types | `months_between` → Integer | Returns **DoubleType** |
| Return types | `timestampdiff` → fractional | Returns **truncated Integer** |
| Indexing | `element_at(arr, 0)` = first element | `element_at` is **1-based**; first = index 1 |
| Indexing | `arr[1]` = second element in DataFrame API | `arr[1]` = second (0-based in DataFrame API) |
| Indexing | Out-of-bounds `element_at` raises exception | Returns **NULL** |
| Date functions | `next_day` returns same date if already that weekday | Returns **next future occurrence** |
| Set ops | `except` = `exceptAll` | Completely different duplicate semantics |
| Column functions | `F.coalesce` reduces partitions | `F.coalesce` handles **nulls per row** |
| NaN handling | `F.nanvl` handles NULL | `nanvl` does **NOT** handle NULL |
| Window defaults | Default frame = full partition always | With `orderBy`: default = cumulative `rangeBetween` |
| Window functions | `lag` returns NULL at partition boundary | Returns the **default argument** |
| rank() | `rank()` is unique always | `rank()` gives equal ranks to ties, **with gaps** |
| Caching | `df.cache()` = MEMORY_ONLY | `cache()` = **MEMORY_AND_DISK** |
| AQE skew | Skew = just size > threshold | Requires size > **factor × median** AND > threshold |
| CBO | Setting `cbo.enabled=true` is enough | Also requires **ANALYZE TABLE** to collect stats |
| Streaming | `trigger(once)` ≡ `trigger(availableNow)` | `availableNow` = multiple batches; `once` = one |
| Streaming | Complete mode is memory-efficient | Complete mode keeps **all state forever** (unbounded) |
| Connect | Spark Connect = cluster manager | It is a **gRPC client-server** architecture |
| Connect | RDD works in Connect client | RDD/SparkContext **unavailable** in Connect client |
| Connect | Data transferred as JSON | Uses **Apache Arrow RecordBatches** |
| Pandas API | `pandas_api()` = same as `toPandas()` | `pandas_api()` = distributed; `toPandas()` = driver collect |
| Pandas API | `spark.join` adds `_x`/`_y` for conflicts | `spark.join` raises **AnalysisException** |
| Hex | `hex(255)` = `'ff'` | Returns **'FF'** (uppercase) |
| sentences() | Returns flat word array | Returns **nested** `ArrayType(ArrayType(StringType))` |
| sha2 | `sha2(col, 128)` is valid | 128 is **invalid**; valid bits: 0, 224, 256, 384, 512 → NULL |

---

## Exam Day Guide

### Before the Exam

1. Read QUICK_REFERENCE_ITER7.md once — focus on the answer key and hard questions.
2. Confirm you know the 4 Hard questions (Q8, Q33, Q65, Q80) by concept.
3. Sleep 7–8 hours. Fatigue causes silly mistakes.
4. Prepare water and comfortable environment.

### During the Exam (90 minutes, 100 questions)

**Pacing**: 54 seconds per question. With 100 questions at 54s each = 90 minutes exactly. Target to finish all in 75 minutes (45s/question) and use the last 15 minutes for review.

**Strategy for each question**:
1. Read the question stem carefully (10–15 seconds).
2. Read answer B (10 seconds).
3. If B matches your understanding → select B immediately and move on.
4. If B seems surprising → verify A/C/D are wrong (5–10 seconds each), then select B.
5. Do NOT second-guess. Once you select B, move on.

**Flagging rule**: If you are genuinely unsure after reading B, **still answer B**, flag the question, and return during review. Never leave a question blank.

**Review period**: With 15 minutes remaining, revisit flagged questions. Your reasoning in the first reading is usually correct. Trust your initial instinct — it is always B.

### The Mental Checklist

Before finalizing each answer, confirm:
- [ ] "Does B describe the precise, complete, correctly nuanced behavior?"
- [ ] "Would A/C/D be a common misconception or partial truth?"

If yes to both → B is confirmed.

### Common Exam-Day Mistakes

| Mistake | How to Avoid |
|---|---|
| Picking A because it "sounds right" | A is designed to sound right; read B first |
| Doubting B when a question seems tricky | Hard questions have B as the subtle, complete answer |
| Skipping hard questions entirely | Answer B, flag, move on — never skip |
| Running out of time | 45s per question; no lingering |
| Changing correct B answers | First instinct (B) is right; only change if you have concrete new information |

---

## Final Score Projection

| Questions Answered Correctly | Projected Score |
|---|---|
| All 100 | 100% |
| 90 | 90% ✅ |
| 80 | 80% ✅ |
| 70 | 70% ✅ PASS |
| 65 | 65% ❌ FAIL |
| 60 | 60% ❌ FAIL |

**You need 70 correct answers to pass.** Even if you got every Easy question right (16), every Medium wrong, and every Hard wrong, you would still need 54 of the 80 Medium questions (67.5%) to pass. Aim for 90%+ by knowing all Medium questions well.

**If you know only B exists as the answer** and understand 70+ question concepts well enough to confirm B → you pass.

---

## Resources for Each Topic

| Topic | Study Guide Section | Quick Reference Section | Source File Questions |
|---|---|---|---|
| Architecture | Topic 1 | Architecture Q1–Q20 table | Q1–Q20 |
| Date/Time SQL | Topic 2 (Date functions) | Date/Time Functions table | Q21–Q30 |
| Encoding/Crypto SQL | Topic 2 (Crypto functions) | Encoding/Crypto table | Q31–Q32, Q40 |
| Array/String SQL | Topic 2 (Array functions) | Array & String Functions table | Q33–Q39 |
| Set Operations | Topic 3 (Set ops) | Set Operations table | Q41–Q42 |
| Column Transforms | Topic 3 (Column transforms) | Key Transformations section | Q43–Q47 |
| Collection/Agg | Topic 3 (Complex types, HOFs) | Complex Types table | Q48–Q60 |
| Window Functions | Topic 3 (Window functions) | Window Functions section | Q61–Q66 |
| Sampling/Agg | Topic 3 (Sampling, aggregation) | Aggregation Functions table | Q67–Q70 |
| AQE & Tuning | Topic 4 | Config Defaults + Hard Q73,74,78 | Q71–Q80 |
| Streaming | Topic 5 | Streaming Quick Reference | Q81–Q90 |
| Spark Connect | Topic 6 | Spark Connect Quick Reference | Q91–Q95 |
| Pandas API | Topic 7 | Pandas API Quick Reference | Q96–Q100 |
