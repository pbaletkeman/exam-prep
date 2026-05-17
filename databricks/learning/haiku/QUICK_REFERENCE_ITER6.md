# Databricks Certified Associate Developer for Apache Spark — Iteration 6 Quick Reference

**Fast-lookup reference guide for exam topics (Iteration 6)**

**Last Updated**: May 17, 2026

---

## Table of Contents

1. [Spark SQL Functions Reference](#spark-sql-functions-reference)
2. [Configuration Quick Reference](#configuration-quick-reference)
3. [Memory Anchors by Topic](#memory-anchors-by-topic)
4. [7-Day Accelerated Study Progression](#7-day-accelerated-study-progression)
5. [Exam Pattern Recognition](#exam-pattern-recognition)

---

## Spark SQL Functions Reference

### Date/Time Functions

| Function | Returns | Key Behavior | Key When |
|----------|---------|--------------|----------|
| `make_date(y, m, d)` | `DateType` | Constructs a date from integer components; `NULL` if any component is out of range | Out-of-range handling |
| `make_timestamp(y, m, d, h, min, s)` | `TimestampType` | Same as `make_date` but for timestamps | Timestamp construction |
| `unix_date(date_col)` | `IntegerType` | Days since epoch (`1970-01-01`) | Different from `unix_timestamp` (seconds) |
| `date_from_unix_date(days)` | `DateType` | Inverse of `unix_date()` | Converting day offsets to dates |
| `date_diff(end, start)` / `datediff(end, start)` | `IntegerType` | Days from start to end; both are aliases (Spark 3.5+) | Identical functions |
| `split_part(str, delim, pos)` | `StringType` | 1-based position in split string | `split_part('a:b:c', ':', 2)` → `'b'` |
| `startswith(str, prefix)` / `endswith(str, suffix)` | `BooleanType` | Boolean check; returns `NULL` if either arg is `NULL` | String prefix/suffix matching |

### Arithmetic Functions

| Function | Behavior | vs Similar |
|----------|----------|-----------|
| `try_divide(n, d)` | Returns `NULL` on divide-by-zero | vs `n / d` which raises error |
| `try_add(a, b)` | Returns `NULL` on overflow | vs `a + b` which wraps or raises |
| `try_subtract(a, b)` | Returns `NULL` on underflow | vs `a - b` |
| `try_multiply(a, b)` | Returns `NULL` on overflow | vs `a * b` |

### Array Functions

| Function | Input/Output | Behavior |
|----------|-------------|----------|
| `array_compact(arr)` | `ArrayType` → `ArrayType` | Remove all `NULL` elements; preserve order |
| `array_distinct(arr)` | `ArrayType` → `ArrayType` | Remove duplicates; keep first occurrence |
| `array_remove(arr, val)` | `ArrayType`, scalar → `ArrayType` | Remove all occurrences of `val` |
| `array_insert(arr, pos, val)` | `ArrayType`, 1-based position → `ArrayType` | Insert `val` at 1-based position; shift right |
| `flatten(nested_arr)` | `ArrayType(ArrayType)` → `ArrayType` | Concatenate all inner arrays |
| `element_at(col, idx)` | `ArrayType`, 1-based idx → element | Returns element or raises error if out-of-bounds |
| `try_element_at(col, idx)` | `ArrayType`, 1-based idx → element | Returns `NULL` if out-of-bounds (Spark 3.4+) |

### Regex Functions

| Function | Return Type | Behavior |
|----------|-------------|----------|
| `regexp_like(str, pattern)` | `BooleanType` | `true` if pattern matches; `false` otherwise |
| `regexp_extract(str, pattern, group_idx)` | `StringType` | Extracted text from capture group; empty string if no match |
| `regexp_count(str, pattern)` | `IntegerType` | Count of non-overlapping matches |

### Aggregate Functions

| Function | NULL Handling | Special Behavior |
|----------|---------------|-----------------|
| `bool_and(col)` | Ignores `NULL`; returns `NULL` only if all are `NULL` | `true` iff all non-null values are `true` |
| `bool_or(col)` | Ignores `NULL`; returns `NULL` only if all are `NULL` | `true` iff any non-null value is `true` |
| `bit_and(col)` / `bit_or(col)` / `bit_xor(col)` | Ignores `NULL` | Bitwise aggregation across all values |
| `any_value(col IGNORE NULLS)` | Skips `NULL` when selecting | Arbitrary non-null value from group (Spark 3.3+) |
| `product(col)` | Ignores `NULL` | Multiplication of all non-null values (Spark 3.2+) |
| `median(col)` | Approximate aggregate | Same as `percentile_approx(col, 0.5)` (Spark 3.4+) |

### String Functions

| Function | Input/Output |
|----------|-------------|
| `overlay(str, replace, pos, len)` | Replace `len` chars starting at 1-based `pos` with `replace` |
| `startswith(str, prefix)` | `BooleanType` |
| `endswith(str, suffix)` | `BooleanType` |

### Struct/Map Functions

| Function | Input/Output | Behavior |
|----------|-------------|----------|
| `named_struct('x', col1, 'y', col2)` | → `StructType` | Custom field names in resulting struct |
| `struct(col1, col2)` | → `StructType` | Uses input column names as field names |
| `from_csv(col, schema_str)` | `StringType` → `StructType` | Parse CSV string to struct; no nested support |
| `schema_of_csv(sample_csv)` | → `StringType` DDL | Infer schema from sample CSV string |
| `inline(array_of_structs)` | `ArrayType(StructType)` → rows | Explode struct fields into separate columns |
| `from_json(col, schema_str)` | `StringType` → `StructType` | Parse JSON string to struct; supports nested |

### Utility Functions

| Function | Behavior |
|----------|----------|
| `width_bucket(val, min, max, num_buckets)` | 1-based bucket number (0 if <min, num_buckets+1 if >=max) |
| `cardinality(col)` | Count elements in array/map; returns `NULL` for `NULL` input |
| `size(col)` | Count elements; returns `-1` for `NULL` (legacy; see `spark.sql.legacy.sizeOfNull`) |

---

## Configuration Quick Reference

### Memory & Resource Management

| Configuration | Default | Purpose | Trade-off |
|---------------|---------|---------|-----------|
| `spark.executor.pyspark.memory` | Unset (unbounded) | Off-heap Python worker memory per executor | Prevent container kills from unbounded Python |
| `spark.memory.offHeap.enabled` | `false` | Enable off-heap memory (outside JVM heap) | Reduced GC pauses; additional memory config |
| `spark.memory.offHeap.size` | 0 | Off-heap budget per executor (additional to `spark.executor.memory`) | Fine-tune for Tungsten operations |
| `spark.rdd.compress` | `false` | Compress serialized cached RDD partitions | Reduce cache footprint; increase CPU |

### Scheduler & Locality

| Configuration | Default | Purpose |
|---------------|---------|---------|
| `spark.scheduler.mode` | `FIFO` | `FIFO` = strict job order; `FAIR` = distribute across concurrent jobs |
| `spark.locality.wait` | `3s` | Wait for preferred locality before downgrading |
| `spark.locality.wait.process` | (inherits from above) | Wait before `PROCESS_LOCAL` → `NODE_LOCAL` transition |
| `spark.locality.wait.node` | (inherits from above) | Wait before `NODE_LOCAL` → `RACK_LOCAL` transition |

### Execution & Code Generation

| Configuration | Default | Purpose |
|---------------|---------|---------|
| `spark.sql.codegen.wholeStage` | `true` | Fuse multiple operators into single compiled method |
| `spark.sql.codegen.maxFields` | 100 | Disable codegen if operator has > this many fields |
| `spark.sql.codegen.aggregate.map.twolevel.enabled` | `true` | Two-level hash map for aggregations (cache-friendly) |
| `spark.sql.adaptive.skewJoin.enabled` | `true` | Handle skewed shuffle partitions in joins |
| `spark.sql.adaptive.coalescePartitions.parallelismFirst` | `true` | Prioritize target partition size over min partition count |

### File I/O & Partitioning

| Configuration | Default | Purpose |
|---------------|---------|---------|
| `spark.sql.files.maxPartitionBytes` | 128 MB | Max data per input partition for file-based scans |
| `spark.sql.files.openCostInBytes` | 4 MB | Virtual per-file padding for merge logic |
| `spark.sql.files.ignoreMissingFiles` | `false` | Skip files deleted between planning & execution |
| `spark.sql.crossJoin.enabled` | `false` | Allow `crossJoin()` (prevents accidental Cartesian products) |

### Shuffle & Performance

| Configuration | Default | Purpose |
|---------------|---------|---------|
| `spark.shuffle.file.buffer` | 32 KB | Write buffer size per shuffle output stream |
| `spark.sql.execution.sortBeforeRepartition` | `true` | Sort map-side partition by hash before repartition shuffle |
| `spark.sql.execution.arrow.maxRecordsPerBatch` | 10000 | Max rows per Arrow batch for Pandas UDFs |
| `spark.sql.execution.arrow.pyspark.selfDestruct.enabled` | `false` | Release Arrow buffers immediately after copying to pandas |

### Streaming

| Configuration | Default | Purpose |
|---------------|---------|---------|
| `spark.dynamicAllocation.shuffleTracking.enabled` | `true` | Track executors with needed shuffle data for DRA |
| `spark.sql.streaming.checkpointLocation` | N/A | Required for structured streaming queries |

### Event Logging & Serialization

| Configuration | Default | Purpose |
|---------------|---------|---------|
| `spark.eventLog.compress` | `false` | Compress event log files |
| `spark.eventLog.compression.codec` | `zstd` | Compression codec for event logs |
| `spark.kryo.registrationRequired` | `false` | Fail on unregistered Kryo classes |
| `spark.sql.legacy.sizeOfNull` | `false` | Return `-1` for `size(NULL)` (true = `false` for compatibility) |

### Spark Connect

| Configuration | Purpose |
|---------------|---------|
| `spark.connect.grpc.port` | Server port (default 15002) |

---

## Memory Anchors by Topic

### Topic 1: Spark Architecture (Q1–Q20)

**Caching Defaults**: RDD=MEMORY_ONLY, DataFrame=MEMORY_AND_DISK

**Job Scheduling**: FIFO (strict order, starves short jobs) vs FAIR (distributes resources across concurrent jobs)

**DAG vs Task Scheduler**: DAG = stages & shuffles; TaskScheduler = tasks & locality

**Barrier Mode**: ALL tasks must start simultaneously; entire stage resubmits on any failure

**Python Memory**: `spark.executor.pyspark.memory` = off-heap Python worker budget (unbounded without it)

**Shuffle Tracking**: DRA can only remove executors without needed shuffle data

**coalesce() Trick**: Cannot increase partitions; always narrow (no shuffle)

**Worker/Executor**: Worker = persistent process per node; Executor = JVM launched by Worker

**Recovery Loss**: Map-stage task loss requires re-running map tasks unless external shuffle service exists

### Topic 2: Spark SQL (Q21–Q40)

**Date/Time Tricks**:
- `make_date()` → `DateType` (not string!)
- `unix_date()` → `IntegerType` days (not seconds!)
- `date_from_unix_date()` is the inverse of `unix_date()`

**Safe Arithmetic**: `try_divide()`, `try_add()` return `NULL` on error (not exception!)

**Regex Flavors**: `regexp_like()` → boolean; `regexp_extract()` → captured text; `regexp_count()` → occurrence count

**NULL Propagation**: `bool_and()/bool_or()` ignore NULLs; `cardinality()` returns NULL for NULL input; `size()` returns -1

**Aggregate Safety**: `any_value(col IGNORE NULLS)` returns arbitrary non-null value

**String Parsing**: `from_csv()` = flat only; `from_json()` = nested OK; both use `schema_of_*()` for inference

### Topic 3: DataFrame API (Q41–Q70)

**LOB Sampling**: `sampleBy(col, fractions_dict)` stratifies per key value

**Checkpointing**: `eager=True` = immediate action; `eager=False` = deferred until next action

**HOF Naming**: `transform_keys()` changes keys; `transform_values()` changes values; `zip_with()` merges element-wise

**Struct Updates**: `withField()` = add/replace field; `dropFields()` = remove fields (no full reconstruction!)

**Array Helpers**: `array_insert()` at 1-based position; `array_distinct()` removes dupes; `array_remove()` removes all occurrences

**Safe Access**: `try_element_at()` returns NULL on out-of-bounds (vs `element_at()` which raises)

**Tail Trick**: `df.tail(5)` = last 5 rows; `df.limit(5)` = first 5 rows

**Write Partitioning**: `partitionBy()` creates `col=val/` dirs; partition columns excluded from data files

### Topic 4: Tuning & Troubleshooting (Q71–Q80)

**Skew Handling**: AQE splits skewed partition, replicates matching partition, processes sub-pairs separately

**Code Generation**: Whole-stage codegen fuses operators; auto-disabled for >100 fields; disable for debugging codegen errors

**Partition Merging**: `openCostInBytes` adds virtual per-file cost to merge many small files into same partition

**Arrow Efficiency**: `selfDestruct.enabled` = release Arrow buffers immediately after pandas copy

**Off-Heap**: Separate from executor heap; not GC'd; used by Tungsten & explicit `OFF_HEAP` storage level

**Kryo Strictness**: `registrationRequired=true` = fail on unregistered classes; requires explicit registration

### Topic 5: Streaming (Q81–Q90)

**Trigger Modes**: `once=true` = single mega-batch; `availableNow=true` = multiple micro-batches with rate limits

**Watermark Math**: Threshold = current_watermark - delay_duration; events AFTER threshold are "on time"

**Session Windows**: Gap-based (not fixed time); close when no event for gap duration

**Kafka Schema**: Always fixed `[key BinaryType, value BinaryType, topic, partition, offset, timestamp, timestampType]`

**Consumer Groups**: Don't set fixed `kafka.group.id` (causes multi-query interference); let Spark manage via checkpoint

**Rate Limiting**: `maxOffsetsPerTrigger` = cap total offsets per micro-batch across all partitions

### Topic 6: Spark Connect (Q91–Q95)

**Error Timing**: Analysis errors surface at **action time** (server-side), not transformation time

**Token Auth**: `sc://host:port/;token=secretvalue` in URL

**No Local JVM**: Client sends serialized plans to gRPC server; JVM only on server

**UDF Serialization**: Python UDFs pickled on client, sent over gRPC, unpickled on executor

**Crash Resilience**: Client Python process survives; running queries lost; can reconnect & resubmit

### Topic 7: Pandas API on Spark (Q96–Q100)

**Caching**: `psdf.spark.cache()` = wraps underlying Spark cache

**Index Types**: `"distributed"` = fastest (non-contiguous); `"distributed-sequence"` = default (monotonic per partition); `"sequence"` = slowest (globally sorted)

**NULL vs NaN**: Different semantics; `fillna()` fills NULL but not NaN; `dropna()` drops NULL but not NaN (by default); NaN propagates in arithmetic aggregates

---

## 7-Day Accelerated Study Progression

**Objective**: Master all 100 questions in 7 days (3 hours/day) for final exam preparation

### Day 1: Architecture & SQL (Q1–40) — 3 hours

**9:00–10:30 AM** (1.5 hours): Topic 1 fundamentals (Q1–Q20)
- Read STUDY_GUIDE sections 1.1–1.20
- Review caching defaults, scheduler modes, DAGScheduler vs TaskScheduler
- Flashcard: RDD vs DataFrame cache defaults

**10:30–12:00 PM** (1.5 hours): Topic 2 fundamentals (Q21–Q40)
- Read STUDY_GUIDE sections 2.1–2.20
- Focus on function return types (make_date → DateType, not string!)
- Flashcard: try_*() functions return NULL, not exceptions

**Evening Review** (30 min): Re-read quick reference tables; create personal note cards

---

### Day 2: DataFrame API Part 1 (Q41–55) — 3 hours

**9:00–11:00 AM** (2 hours): DataFrame fundamentals (Q41–Q55)
- Read STUDY_GUIDE sections 3.1–3.7
- Understand stratified sampling, checkpointing eager vs lazy
- Trace through HOF examples (transform_keys, transform_values)

**11:00 AM–12:00 PM** (1 hour): Practice Q41–Q55 problems
- Work through 15 practice questions
- Focus on output schema understanding

**Evening**: Flashcards on DataFrame transforms and HOFs

---

### Day 3: DataFrame API Part 2 & Tuning (Q56–80) — 3 hours

**9:00–10:30 AM** (1.5 hours): DataFrame continuation (Q56–Q70)
- Read STUDY_GUIDE sections 3.8–3.20
- Understand writing, partitioning, write modes

**10:30 AM–12:00 PM** (1.5 hours): Tuning & Troubleshooting (Q71–Q80)
- Read STUDY_GUIDE sections 4.1–4.10
- Understand AQE, code generation, off-heap memory
- Focus on configuration trade-offs

**Evening**: Test yourself on Q41–Q80 (40 questions)

---

### Day 4: Streaming & Spark Connect (Q81–95) — 3 hours

**9:00–10:30 AM** (1.5 hours): Structured Streaming (Q81–Q90)
- Read STUDY_GUIDE sections 5.1–5.10
- Understand watermarks, session windows, Kafka sources
- Trace through consumer group risks

**10:30 AM–12:00 PM** (1.5 hours): Spark Connect & Pandas API (Q91–Q100)
- Read STUDY_GUIDE sections 6.1–7.5
- Understand error timing, authentication, schema fixed issues
- Learn NULL vs NaN semantics

**Evening**: Flashcards on streaming & connect concepts

---

### Day 5: Full Mock Test 1 (Q1–100) — 3 hours

**9:00 AM–12:00 PM**: Complete timed practice test (100 questions, 120 minutes)
- Simulate exam conditions: time limit, no reference materials
- Record scores by topic
- Identify weak areas

**Afternoon**: Review incorrect answers; update flashcards with gaps

---

### Day 6: Targeted Review & Mock Test 2 — 3 hours

**9:00–10:00 AM** (1 hour): Deep dive on weak topic areas from Day 5
- Reread relevant STUDY_GUIDE sections
- Revisit function signatures and edge cases

**10:00 AM–1:00 PM** (2 hours): Full mock test 2 (100 questions, 120 minutes)
- Attempt under exam conditions
- Track improvement against Day 5

**Evening**: Review answers; identify remaining weak spots

---

### Day 7: Final Review & Mock Test 3 — 3 hours

**9:00–10:00 AM** (1 hour): High-impact review
- Review QUICK_REFERENCE memory anchors (1 page per topic)
- Verify mastery of Q1–Q100 answer patterns

**10:00 AM–1:00 PM** (2 hours): Final mock test 3 (100 questions, 120 minutes)
- Full exam simulation
- Goal: 75%+ (80%+ is stretch goal)

**1:00–3:00 PM**: Final review
- Analyze any remaining incorrect answers
- Visualize exam success
- Rest before real exam

---

## Exam Pattern Recognition

### Question Type Patterns

**Type 1: "Which statement correctly describes..."** (Multiple Choice, One Answer)
- **Answer Strategy**: Read all options; eliminate obviously false statements; use key terms to narrow choices
- **Exam Weight**: ~73% of questions
- **Example**: Q1 (RDD vs DataFrame cache), Q2 (FIFO vs FAIR scheduler)

**Type 2: "Which of the following statements... are correct? (Select all that apply)"** (Multiple Choice, Many Answers)
- **Answer Strategy**: Treat each option as independent true/false; common traps = one correct option with plausible incorrect options
- **Exam Weight**: ~20% of questions
- **Example**: Q4 (Barrier mode statements), Q8 (coalesce semantics), Q20 (Application ID behavior)

**Type 3: "All of the following except..."** (Select the False Option)
- **Answer Strategy**: All but one statement are correct; read carefully for negation or subtle differences
- **Exam Weight**: ~5% of questions
- **Example**: Q65 (Parquet compression codecs)

**Type 4: "None of the above"** (Select the Correct Option or None)
- **Answer Strategy**: If all options are clearly false, answer is "none"; rare in Databricks exams
- **Exam Weight**: ~2% of questions

### Difficulty Distribution

**Easy (20%)**: Function return types, basic configuration, straightforward naming
- Example: Q24 (make_date), Q49 (df.tail), Q84 (console sink)
- **Strategy**: Answer quickly; verify once; move on

**Medium (60%)**: Function behavior, interaction effects, edge case handling, configuration trade-offs
- Example: Q2 (scheduler modes), Q42 (checkpoint eager), Q71 (skew join)
- **Strategy**: Read carefully; trace through examples; check NULL handling

**Hard (20%)**: Multi-concept questions, rare edge cases, performance interactions, system behavior
- Example: Q4 (barrier execution), Q10 (non-equi joins), Q19 (executor loss recovery)
- **Strategy**: Break into smaller pieces; use process of elimination; consider side effects

### Correct Answer Patterns

**Pattern 1: Detailed Explanation is Often Correct**
- Correct answers tend to include **specific mechanisms** and **edge cases**.
- Wrong answers are often **vague** or **overly simplistic**.
- **Example**: Q9 (Arrow batch size) — correct answer names the config, explains memory/latency trade-off.

**Pattern 2: NULL Handling is Frequently Tested**
- Topic-specific NULL behaviors: `cardinality()` → NULL, `size()` → -1, `bool_and/or()` → ignore NULLs
- **Prepare**: Know each function's NULL convention before the exam.

**Pattern 3: "Default Behavior" Questions Distinguish Correct Answers**
- `spark.sql.legacy.sizeOfNull=false` (default) → `size(NULL)` returns -1
- `spark.dynamicAllocation.shuffleTracking.enabled=true` (default in 3.0+)
- **Prepare**: Memorize key defaults from the QUICK_REFERENCE table.

**Pattern 4: Return Type Matters**
- `make_date()` → `DateType`, NOT `StringType`
- `unix_date()` → `IntegerType` days, NOT `LongType` seconds
- `regexp_like()` → `BooleanType`, NOT `StringType`
- **Prepare**: Create flashcard for every function with its return type.

**Pattern 5: "vs" Questions Test Distinctions**
- `try_divide()` vs `/` (NULL vs exception)
- `coalesce(1)` vs `repartition(1)` (narrow vs shuffle)
- `FIFO` vs `FAIR` (job order vs resource distribution)
- **Prepare**: Understand the **exact difference** not just similarities.

### Answer Modality Insights

**Multiple Choice (73% of exam)**:
- **Time per question**: ~45 seconds
- **Strategy**: Eliminate 2 obviously wrong options first; choose between remaining 2

**Select All That Apply (20%)**:
- **Time per question**: ~60 seconds (each option requires independent judgment)
- **Strategy**: Read each option as a standalone statement; mark independently; common trap = marking related but incorrect options

**All/None (5–7%)**:
- **Time per question**: ~30 seconds
- **Strategy**: Scan for the option that **all sub-statements are correct**; or confirm all are true

---

**End of Quick Reference (Iteration 6)**

Use this alongside STUDY_GUIDE_ITER6.md and PRACTICE_STRATEGY_ITER6.md for exam mastery.
