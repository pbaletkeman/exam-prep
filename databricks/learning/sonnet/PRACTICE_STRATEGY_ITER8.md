# Practice Strategy — Databricks Certified Associate Developer for Apache Spark
## Iteration 8

---

## ⚠️ Iteration 7 vs Iteration 8: Difficulty Spike Warning

This iteration is fundamentally harder. Before any practice, absorb this comparison:

| Dimension | Iteration 7 | Iteration 8 | Change |
|---|---|---|---|
| Easy questions | 16 | 9 | −44% |
| Medium questions | 80 | 55 | −31% |
| Hard questions | **4** | **36** | **+800%** |
| Non-B answers | **0** (all B) | **4** (Q31, Q60, Q71, Q81) | New trap |
| Requires deep conceptual knowledge | Rarely | Frequently | Major shift |
| Can pass by B-pattern alone | Yes | **No** (4 A answers, all in hard topics) | Critical |

**Implication:** You cannot rely on pattern-guessing for Iter 8. The 36 Hard questions test nuanced differences between similar concepts. The 4 A-answers are all in areas that require careful reasoning (timezone direction, null semantics, AQE config, streaming listener API).

---

## Study Priority Matrix

Study in this order — hardest, most trap-heavy topics first:

| Priority | Topic | Hard Qs | Non-B Traps | Key Concepts to Master |
|---|---|---|---|---|
| 🔴 1 | Tuning (Q71–Q80) | 6 of 10 | **Q71=A** | AQE (coalesce, skew, BHJ), GC, spill, memory math |
| 🔴 2 | Streaming (Q81–Q90) | 5 of 10 | **Q81=A** | Triggers, output modes, stateful ops, listener API |
| 🔴 3 | SQL HOF + dates (Q21–Q40) | 10 of 20 | **Q31=A** | HOF edge cases, timezone direction, error-tolerant functions |
| 🟡 4 | Architecture (Q1–Q20) | 9 of 20 | None | Memory model, shuffle, barrier mode, accumulators |
| 🟡 5 | DataFrame API (Q41–Q70) | 11 of 30 | **Q60=A** | DS V2, null handling, write options, ambiguous columns |
| 🟢 6 | Spark Connect (Q91–Q95) | 2 of 5 | None | gRPC, plan flow, TLS, unsupported APIs |
| 🟢 7 | Pandas API (Q96–Q100) | 2 of 5 | None | Index types, ops_on_diff_frames, shortcut_limit |

---

## The 4 Must-Know A-Answers

Memorise these before anything else. They are your biggest trap:

### Q31=A: Timezone Conversion Direction
```
to_utc_timestamp(ts, tz)    →  LOCAL → UTC    (add offset if tz is behind UTC)
from_utc_timestamp(ts, tz)  →  UTC → LOCAL    (subtract offset if tz is behind UTC)

Memory hook: "to_utc" = going TO utc = local is the input
             "from_utc" = coming FROM utc = UTC is the input
```

### Q60=A: na.drop how Parameter
```
how="any"  →  drop row if ANY column is null    (more rows dropped)
how="all"  →  drop row only if ALL columns null  (fewer rows dropped)

Memory hook: "all" = "all must be null before I drop you" = stricter = fewer dropped
             "any" = "any null and you're out" = looser = more dropped
```

### Q71=A: AQE Coalesce Configuration
```
Correct config: spark.sql.adaptive.coalescePartitions.enabled = true
Advisory size:  spark.sql.adaptive.advisoryPartitionSizeInBytes = 64 MB (default)

Common wrong answer: "AQE uses shuffle.partitions=auto"  — WRONG, there is no "auto" value
AQE coalesces adjacent small shuffle partitions after a shuffle completes.
```

### Q81=A: StreamingQueryListener
```
Registration: spark.streams.addListener(myListener)  — standard OSS API
Callbacks:
  onQueryStarted(event: QueryStartedEvent)
  onQueryProgress(event: QueryProgressEvent)
  onQueryTerminated(event: QueryTerminatedEvent)

Common wrong answer: "this is a Databricks-proprietary API, not available in OSS Spark" — WRONG
```

---

## 4-Week Study Plan

### Week 1: Architecture + SQL Hard Questions

**Days 1–2: Memory Model and Shuffle (Q1–Q10, Q15, Q16)**
- Unified memory (execution + storage), storageFraction, eviction watermark
- Sort shuffle: 2×M files; hash shuffle: M×R files
- TaskContext, attemptNumber, accumulator double-counting (Q13)
- Draw the memory diagram from scratch

**Days 3–4: SQL — HOF Edge Cases (Q25–Q30, Q34)**
- `forall([]) = true`, `exists([]) = false`
- `zip_with` length = max of inputs, null padding
- `aggregate`: fold-left with finish function
- `sequence` with negative step → descending

**Days 5–7: SQL — Functions that surprise (Q22, Q23, Q31, Q32, Q35–Q39)**
- `overlay` vs `regexp_replace` (positional vs regex)
- `to_utc_timestamp` vs `from_utc_timestamp` direction (**Q31=A**)
- `make_date` → null on invalid (not exception)
- `try_cast`, `try_divide` → null on failure
- `UNPIVOT`, `QUALIFY`, `LATERAL VIEW OUTER`

**Week 1 Goal:** Correctly answer all Q1–Q40 in under 22 minutes.

---

### Week 2: DataFrame API Hard Questions

**Days 1–2: Write API and DS V2 (Q41–Q45, Q58)**
- `write.mode()` table, `writeTo()` vs `write.` differences
- `partitionBy` removes columns from data files
- `bucketBy` skips shuffle on matching join
- `maxRecordsPerFile` splits within a task

**Days 3–4: Null Handling and DataFrame Transformations (Q60–Q68)**
- `na.drop(how=)` direction (**Q60=A**)
- Ambiguous column resolution strategies (Q61)
- `when().otherwise()` — missing `otherwise` → null (Q62)
- `withColumn` on existing name = silent overwrite (Q64)
- `distinct` vs `dropDuplicates` subset (Q68)

**Days 5–7: Advanced DataFrame (Q46–Q59, Q69–Q70)**
- `freqItems` (Misra-Gries), `observe` (single-pass metrics), `crosstab`
- `localCheckpoint` not fault-tolerant (Q48)
- `regexp_extract` no match → `""` not null (Q51)
- `from_json` permissive mode rules (Q53)
- `rowsBetween` vs `rangeBetween` (Q70)

**Week 2 Goal:** Correctly answer all Q41–Q70 in under 30 minutes.

---

### Week 3: Tuning + Streaming + Connect + Pandas

**Days 1–2: Tuning Deep Dive (Q71–Q80)**
- AQE: `coalescePartitions.enabled`, `advisoryPartitionSizeInBytes` (**Q71=A**)
- Skew join resolution: AQE splits + replicates (Q74)
- `autoBroadcastJoinThreshold=-1` = disable all auto BHJ (Q75)
- `EXPLAIN CODEGEN` reads and pipeline break `!` markers (Q73)
- `eventLog.enabled=true` + path for History Server (Q79)
- Shuffle spill metrics: what to look for in Stage UI (Q80)

**Days 3–4: Streaming Deep Dive (Q81–Q90)**
- `spark.streams.addListener()` and 3 callbacks (**Q81=A**)
- `mapGroupsWithState` vs `flatMapGroupsWithState` output cardinality (Q82)
- `Trigger.Once()` vs `Trigger.AvailableNow()` (Q85)
- Stream-static join: no late row recovery (Q87)
- `orderBy` on streaming → AnalysisException (Q88)
- Continuous processing limitations (Q89)
- Rate source schema: timestamp + value columns (Q90)

**Days 5–6: Spark Connect + Pandas API (Q91–Q100)**
- gRPC plan flow, protobuf, TLS URL format (Q91–Q95)
- `ops_on_diff_frames`, `shortcut_limit`, `distributed-sequence` vs `sequence` (Q96–Q100)

**Day 7: Full Review of all 4 A-Answers + Config Defaults Cheatsheet**

**Week 3 Goal:** Correctly answer all Q71–Q100 in under 30 minutes.

---

### Week 4: Full Practice Tests + Reinforcement

**Days 1–2:** Take Practice Test Set 1 (Architecture) below. Review every wrong answer.

**Days 3–4:** Take Practice Test Set 2 (SQL + DataFrame) below. Focus on HOF edge cases and null semantics.

**Days 5–6:** Take Practice Test Set 3 (Tuning + Streaming + Connect + Pandas) below.

**Day 7:** Take the source file (all 100 Iter 8 questions) as a timed full mock exam. Target: 90 minutes, ≥85 correct.

---

## Practice Test Set 1 — Architecture (Q1–Q20)

Answer these without looking at the key. Give yourself 11 minutes (33 seconds each).

| Q# | Question Summary | Your Answer | Correct |
|---|---|---|---|
| Q1 | How many tasks run in a stage? | | B |
| Q2 | What happens when execution needs memory from storage region? | | B |
| Q3 | How many files does sort shuffle create per mapper? | | B |
| Q4 | How to get partition ID and attempt number inside a task? | | B |
| Q5 | Barrier mode behavior on single task failure? | | B |
| Q6 | What is the difference between FIFO and FAIR schedulers? | | B |
| Q7 | What does `python.worker.reuse=true` do? | | B |
| Q8 | Difference between `checkpoint()` and `persist(DISK_ONLY)` re lineage? | | B |
| Q9 | Order of locality preference in task scheduling? | | B |
| Q10 | What is UnsafeRow and why does it reduce GC pressure? | | B |
| Q11 | What happens to `executor.instances` when dynamic allocation is on? | | B |
| Q12 | What does `maxPartitionBytes` control? | | B |
| Q13 | Can accumulators double-count on retries? | | B |
| Q14 | What does `broadcastTimeout` control? | | B |
| Q15 | Which configuration source takes precedence: CLI or spark-defaults? | | B |
| Q16 | What does `spark.rdd.compress` do? | | B |
| Q17 | What does `driver.maxResultSize` cap? | | B |
| Q18 | Difference between `addFile` and `addJar`? | | B |
| Q19 | What does enabling Arrow do for `toPandas()`? | | B |
| Q20 | What are `retainedJobs`/`retainedStages`? | | B |

**Score: __ / 20**

---

## Practice Test Set 2 — SQL + DataFrame (Q21–Q70)

Answer these without looking at the key. Give yourself 27 minutes.

| Q# | Question Summary | Your Answer | Correct |
|---|---|---|---|
| Q21 | `regexp_replace` when pattern not found? | | B |
| Q22 | What does `overlay` do vs regex functions? | | B |
| Q23 | What does `soundex()` return? | | B |
| Q24 | What does `initcap()` do? | | B |
| Q25 | `array_distinct` behavior with nulls? | | B |
| Q26 | `array_union/intersect/except` — do they deduplicate? | | B |
| Q27 | `aggregate()` with a finish function? | | B |
| Q28 | `forall([])` and `exists([])` results? | | B |
| Q29 | `zip_with` with arrays of different lengths? | | B |
| Q30 | `map_from_entries` with duplicate keys? | | B |
| Q31 | Direction of `to_utc_timestamp` vs `from_utc_timestamp`? | | **A** |
| Q32 | `make_date` on invalid date (e.g., Feb 30)? | | B |
| Q33 | `datediff` vs `timestampdiff`? | | B |
| Q34 | `sequence` with negative step? | | B |
| Q35 | `try_cast` and `try_divide` on failure? | | B |
| Q36 | What does `UNPIVOT` do? (Spark version?) | | B |
| Q37 | What does `QUALIFY` do? | | B |
| Q38 | `TABLESAMPLE(10 PERCENT)` vs `(100 ROWS)`? | | B |
| Q39 | `LATERAL VIEW OUTER` vs `LATERAL VIEW`? | | B |
| Q40 | What does `schema_of_json()` accept as argument? | | B |
| Q41 | `write.mode("overwrite")` behavior on existing path? | | B |
| Q42 | What does `partitionBy` do to partition columns in the data file? | | B |
| Q43 | What does `bucketBy(64, "user_id")` do for joins? | | B |
| Q44 | `writeTo()` vs `write.` which API? | | B |
| Q45 | What does `df.observe()` compute? | | B |
| Q46 | `freqItems()` algorithm? | | B |
| Q47 | How does a Pandas scalar UDF receive data? | | B |
| Q48 | Is `localCheckpoint()` fault-tolerant? | | B |
| Q49 | `F.input_file_name()` returns what? | | B |
| Q50 | `df.stat.crosstab()` returns what? | | B |
| Q51 | `regexp_extract` no match → ? | | B |
| Q52 | `split(str, pat, limit)` behavior? | | B |
| Q53 | `from_json` permissive: missing field, extra field, malformed? | | B |
| Q54 | `StructType.fromDDL()` nullable default? | | B |
| Q55 | `randomSplit` reproducibility? | | B |
| Q56 | `hint("broadcast")` behavior? | | B |
| Q57 | `encode()` and `decode()` return types? | | B |
| Q58 | `maxRecordsPerFile` controls? | | B |
| Q59 | `sortWithinPartitions` vs `orderBy` — shuffle? | | B |
| Q60 | `na.drop(how="all")` vs `how="any"`? | | **A** |
| Q61 | How to resolve ambiguous column in join? | | B |
| Q62 | `when()` without `.otherwise()` → unmatched? | | B |
| Q63 | `select(F.col("*"), new_col)` — what results? | | B |
| Q64 | `withColumn` on existing column name? | | B |
| Q65 | `df.toDF(*names)` mismatch in count? | | B |
| Q66 | `crossJoin` result size? | | B |
| Q67 | `selectExpr()` accepts what? | | B |
| Q68 | `distinct()` vs `dropDuplicates(["id"])`? | | B |
| Q69 | `F.expr()` vs `F.col()` — when to use each? | | B |
| Q70 | `rowsBetween` vs `rangeBetween` for ties? | | B |

**Score: __ / 50**

---

## Practice Test Set 3 — Tuning + Streaming + Connect + Pandas (Q71–Q100)

Answer these without looking at the key. Give yourself 16 minutes.

| Q# | Question Summary | Your Answer | Correct |
|---|---|---|---|
| Q71 | AQE coalesce config property name? | | **A** |
| Q72 | `storageFraction` protects what from eviction? | | B |
| Q73 | `EXPLAIN CODEGEN` and what `!` means? | | B |
| Q74 | Skew join symptom and AQE solution? | | B |
| Q75 | How to disable all auto broadcast joins? | | B |
| Q76 | ORC vs Parquet — which for Hive ACID? | | B |
| Q77 | Recommended GC algorithm and where to set it? | | B |
| Q78 | `inMemoryColumnarStorage.batchSize` controls? | | B |
| Q79 | How to enable event logging? | | B |
| Q80 | How to identify shuffle spill in Spark UI? | | B |
| Q81 | StreamingQueryListener registration and callbacks? | | **A** |
| Q82 | `mapGroupsWithState` vs `flatMapGroupsWithState` output? | | B |
| Q83 | `failOnDataLoss=true` for Kafka — what happens on missing offsets? | | B |
| Q84 | `complete` output mode behavior? | | B |
| Q85 | `Trigger.Once()` vs `Trigger.AvailableNow()`? | | B |
| Q86 | `maxFilesPerTrigger` controls? | | B |
| Q87 | Stream-static join: can late streaming rows recover? | | B |
| Q88 | `orderBy()` on streaming DataFrame? | | B |
| Q89 | Continuous processing limitations? | | B |
| Q90 | Rate source schema columns and types? | | B |
| Q91 | Spark Connect architecture overview? | | B |
| Q92 | When is the plan sent to the server? | | B |
| Q93 | How to configure TLS in Connect URL? | | B |
| Q94 | Which APIs are NOT available via Spark Connect? | | B |
| Q95 | How does Spark Connect handle version independence? | | B |
| Q96 | How to convert pandas DF to Pandas-on-Spark? | | B |
| Q97 | How to enable cross-DataFrame operations? | | B |
| Q98 | `ps.get_dummies()` does what? | | B |
| Q99 | `shortcut_limit` purpose? | | B |
| Q100 | `sequence` vs `distributed-sequence` index type? | | B |

**Score: __ / 30**

---

## Common Pitfalls Matrix

| Concept | Common Wrong Assumption | Correct Fact |
|---|---|---|
| `na.drop(how=)` | "all" drops more rows | "any" drops more — "all" requires ALL null (**Q60=A**) |
| `to_utc_timestamp` | "to" means from UTC | "to" = destination is UTC = input is local (**Q31=A**) |
| AQE coalesce config | `shuffle.partitions=auto` | `adaptive.coalescePartitions.enabled=true` (**Q71=A**) |
| StreamingQueryListener | Databricks-proprietary | Standard OSS API (**Q81=A**) |
| `forall([])` | false (like `exists`) | **true** (vacuously) — opposite of `exists` |
| `regexp_extract` no match | null | **empty string `""`** — opposite of `regexp_replace` |
| `regexp_replace` no match | exception | returns **original string** unchanged |
| `make_date` invalid | exception | returns **null** |
| `zip_with` length | min of inputs | **max of inputs** — shorter padded with null |
| `checkpoint()` lineage | truncated — same as persist | persist keeps lineage; checkpoint **truncates** |
| `localCheckpoint()` | fault-tolerant | **NOT fault-tolerant** |
| Barrier mode failure | only failed task retried | **entire stage** fails and restarts |
| `executor.instances` with DA | used normally | **ignored** when dynamic allocation is on |
| `withColumn` existing col | raises error | **silent overwrite** |
| `distinct()` vs `dropDuplicates` | same behavior | `dropDuplicates(["id"])` uses subset |
| `when()` without `otherwise` | raises error | returns **null** for unmatched |
| `df.toDF(*names)` count mismatch | pads with None | raises **AnalysisException** |
| Sort shuffle files | M × R like hash | **2 × M** (1 data + 1 index per mapper) |
| `autoBroadcastJoinThreshold=-1` | just lowers threshold | **disables** broadcast joins entirely |
| `storageFraction` | execution is protected | **storage** is protected from execution eviction |
| `TABLESAMPLE(10 PERCENT)` | exact 10% | **approximate** (Bernoulli) |
| `LATERAL VIEW` empty array | drops row | `OUTER` keyword needed to **preserve** row |
| `schema_of_json` argument | accepts column ref | **string literal only** |
| Streaming `complete` mode | needs watermark | **cannot use watermark** with complete mode |
| `Trigger.Once` vs `AvailableNow` | same thing | AvailableNow processes all backlog in **multiple** batches |
| Continuous processing | supports stateful ops | **stateless only** |
| Spark Connect `sc` access | available | **SparkContext/RDD not available** |
| Pandas API cross-DF ops | works by default | raises **ValueError** without `ops_on_diff_frames=True` |

---

## Hard Questions Flash Cards (36 questions)

For each, cover the answer column and practice recalling the key fact:

| Q# | Hard Concept | Key Answer Fact |
|---|---|---|
| Q5 | Barrier mode failure | Whole stage fails and restarts |
| Q8 | checkpoint vs persist lineage | checkpoint truncates; persist retains |
| Q9 | Locality level degradation | PROCESS→NODE→RACK→ANY (3s each) |
| Q10 | UnsafeRow layout | Binary off-heap, no GC, field access by offset |
| Q13 | Accumulator on retry | Double-counts — use only for debugging |
| Q17 | maxResultSize | Caps total serialized result to driver (default 1 GB) |
| Q20 | retainedJobs/Stages | FIFO-evicted Web UI in-memory cache |
| Q27 | aggregate HOF | fold-left; finish function post-processes accumulator |
| Q28 | forall/exists empty | forall=true, exists=false |
| Q29 | zip_with length | max of inputs; shorter padded null |
| Q30 | map_from_entries dups | last value wins |
| Q31 | Timezone direction | to_utc=local→UTC; from_utc=UTC→local (**A**) |
| Q35 | try_ functions | try_cast/try_divide → null (no exception) |
| Q36 | UNPIVOT | Wide columns → rows; Spark 3.4+ |
| Q37 | QUALIFY | Filter on window result without subquery |
| Q39 | LATERAL VIEW OUTER | Preserves null/empty rows |
| Q43 | bucketBy join | Skips shuffle when both sides match |
| Q44 | writeTo DS V2 | Supports overwrite(condition), append(condition) |
| Q47 | Pandas scalar UDF | Receives Series per Arrow batch (not scalar) |
| Q48 | localCheckpoint | NOT fault-tolerant (executor local disk) |
| Q51 | regexp_extract no match | `""` empty string |
| Q53 | from_json permissive | Missing=null, extra ignored, malformed=all-null |
| Q59 | sortWithinPartitions | No shuffle; orderBy = shuffle |
| Q60 | na.drop how="all" | ALL columns null; how="any" = ANY null (**A**) |
| Q61 | Ambiguous join column | Use df1["id"] or list-of-string join keys |
| Q70 | rangeBetween ties | Includes all rows tied on ORDER BY value |
| Q71 | AQE coalesce config | coalescePartitions.enabled=true (**A**) |
| Q74 | Skew join AQE | Splits large partition + replicates other side |
| Q73 | EXPLAIN CODEGEN | Shows Java; `!` = pipeline break |
| Q80 | Shuffle spill detection | Look for Shuffle Spill (Memory) and Shuffle Spill (Disk) |
| Q81 | StreamingQueryListener | addListener(); onQueryStarted/Progress/Terminated (**A**) |
| Q82 | mapGroups vs flatMapGroups | map=exactly 1; flatMap=0 or more |
| Q85 | AvailableNow trigger | Multiple micro-batches; stops when caught up |
| Q87 | Stream-static join | Static re-read each batch; late rows cannot recover |
| Q89 | Continuous processing | ms latency; stateless only; Kafka/Rate only |
| Q95 | Protobuf versioning | Field numbers allow independent client/server versions |

---

## Exam Day Checklist

### Timing Strategy
```
100 questions / 90 minutes = 54 seconds per question

Budget:
  Easy (9 questions)   →  20–25 sec each  (save ~5 min)
  Medium (55 questions) →  50–60 sec each  (use ~50 min)
  Hard (36 questions)  →  75–90 sec each  (use ~50 min)

Total: ~105 min budget → need to move fast on Easy/Medium to create buffer

Flag hard questions you are unsure about. Return after first pass.
```

### Flag These Immediately (highest trap probability)
- Any question about `na.drop(how=)` → think carefully, answer is **A** style
- Any question about timezone conversion → "to_utc" = local→UTC
- Any question about AQE coalesce config property name
- Any question about `StreamingQueryListener` registration
- Any question about `forall`/`exists` with empty array
- Any question about `regexp_extract` vs `regexp_replace` no-match return value
- Any question about HOF length for `zip_with`
- Any question about shuffle file count

### Decision Protocol for Hard Questions
```
Step 1: Eliminate obviously wrong options first
Step 2: For two similar remaining options, ask "what's the subtle difference?"
Step 3: If question involves direction/order (timezone, null semantics), slow down
Step 4: If answer B feels "too safe", double-check — Q31/Q60/Q71/Q81 are A
Step 5: Never leave blank — if unsure: B is correct 96% of the time
```

### Last-Minute Recall: The 4 A-Answers
```
Q31  →  A  (to_utc=local→UTC direction)
Q60  →  A  (how="all"=ALL null; how="any"=ANY null)
Q71  →  A  (AQE coalescePartitions.enabled=true)
Q81  →  A  (spark.streams.addListener, 3 callbacks, OSS API)
```

### High-Value Quick Wins
```
Before exam, review these 5 config values from memory:
  maxPartitionBytes = 128 MB
  autoBroadcastJoinThreshold = 10 MB
  broadcastTimeout = 300 s
  shuffle.partitions = 200
  advisoryPartitionSizeInBytes = 64 MB (AQE coalesce target)
```

---

## Key Formulas and Rules to Memorize

### HOF Empty-Array Rules
```
forall([], pred)   = true   (vacuous truth — nothing violated the predicate)
exists([], pred)   = false  (nothing satisfied it)
aggregate([], zero, f) = zero (the zero accumulator returned unchanged)
filter([], pred)   = []
transform([], f)   = []
zip_with([], [], f) = []
```

### HOF Null-Array Rules
```
Any HOF with null array input → null output (universal rule)
Exception: aggregate with null zero accumulator → null
```

### Sort Shuffle Math
```
M mappers × 2 files each = 2M total files
(1 data file + 1 index file per mapper)
```

### Memory Math
```
Unified memory = JVM heap × memory.fraction (0.6)
Storage fraction = unified × storageFraction (0.5)
Execution fraction = unified × (1 - storageFraction) but can borrow

Max broadcast = autoBroadcastJoinThreshold bytes for auto; -1 = disabled
```

### Streaming State Cardinality
```
mapGroupsWithState    → exactly 1 row output per group per batch
flatMapGroupsWithState → 0 or more rows per group per batch
```

### Write Mode Decision
```
new data, never overwrite old? → append
always want clean slate?       → overwrite (deletes existing directory)
fail if exists (safe default)? → error
silently skip if exists?       → ignore
```

### Output Mode Decision
```
only care about new/changed rows? → update
want to expose entire aggregation? → complete (no watermark allowed)
insert-only, no aggregation?     → append
```

---

## Progress Tracker

Use this to track your readiness across topics:

| Topic | Practice Test Score | Hard Qs Correct | Confidence |
|---|---|---|---|
| Architecture (Q1–Q20) | __ / 20 | __ / 9 | 🔴🟡🟢 |
| SQL (Q21–Q40) | __ / 20 | __ / 10 | 🔴🟡🟢 |
| DataFrame (Q41–Q70) | __ / 30 | __ / 11 | 🔴🟡🟢 |
| Tuning (Q71–Q80) | __ / 10 | __ / 6 | 🔴🟡🟢 |
| Streaming (Q81–Q90) | __ / 10 | __ / 5 | 🔴🟡🟢 |
| Connect (Q91–Q95) | __ / 5 | __ / 2 | 🔴🟡🟢 |
| Pandas (Q96–Q100) | __ / 5 | __ / 2 | 🔴🟡🟢 |
| **Total** | **__ / 100** | **__ / 45** | |

Target: ≥85/100 on two consecutive practice runs before sitting the real exam.
