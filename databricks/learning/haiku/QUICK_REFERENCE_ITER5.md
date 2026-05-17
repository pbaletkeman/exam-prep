# Databricks Certified Associate Developer for Apache Spark — Iteration 5 Quick Reference

**Fast-lookup reference guide for exam preparation (Iteration 5)**

---

## Function Reference Tables

### Spark SQL Date/Time Functions

| Function | Return Type | Example | Notes |
|----------|-------------|---------|-------|
| `datediff(end, start)` | Int | `datediff('2026-05-20', '2026-05-10')` → 10 | end − start in days; positive = end is later |
| `unix_timestamp()` | LongType | `unix_timestamp()` → 1778793600 | Current epoch time (seconds since 1970-01-01 UTC) |
| `initcap(str)` | StringType | `initcap('hello world')` → `'Hello World'` | Capitalize first letter of each word |
| `trunc(date, fmt)` | DateType | `trunc('2026-05-15', 'month')` → `'2026-05-01'` | Truncate date to unit; accepts DateType |
| `date_trunc(fmt, ts)` | TimestampType | `date_trunc('hour', ts)` | Truncate timestamp; accepts TimestampType |
| `last_day(date)` | DateType | `last_day('2026-02-15')` → `'2026-02-28'` | Last day of the month |
| `dayofweek(date)` | Int | `dayofweek('2026-05-10')` → 1 (Sun) | 1=Sun, 2=Mon, ..., 7=Sat |
| `locate(substr, str)` | Int | `locate('world', 'hello world')` → 7 | 1-based index; returns 0 if not found |

### Spark SQL Aggregate Functions

| Function | Return Type | Example | Notes |
|----------|-------------|---------|-------|
| `count_if(condition)` | LongType | `count_if(age > 18)` | Count rows where condition = true |
| `percentile(col, p)` | DoubleType | `percentile(salary, 0.5)` | Exact median; requires full sort; not scalable |
| `percentile_approx(col, p, acc)` | DoubleType | `percentile_approx(salary, 0.5, 0.01)` | Approximate percentile; uses quantile sketch |
| `max_by(value_col, order_col)` | Same as value_col | `max_by(salary, perf_score)` | Value from row with max order_col (Spark 3.0+) |
| `GROUPING_ID(*cols)` | LongType | `GROUPING_ID(dept, region)` with ROLLUP | Bitmask: 0 = grouped; 1 = rolled up |

### DataFrame String Functions

| Function | Return Type | Example | Notes |
|----------|-------------|---------|-------|
| `F.soundex(col)` | StringType | `soundex('Smith')` → `'S530'` | Phonetic code for fuzzy name matching |
| `F.reverse(col)` | StringType \| ArrayType | `reverse('hello')` → `'olleh'` | Polymorphic: works on strings and arrays |
| `F.format_string(fmt, *cols)` | StringType | `format_string("%s: %d", name, count)` | Printf-style formatting |
| `F.levenshtein(col1, col2)` | IntegerType | `levenshtein('cat', 'car')` → 1 | Edit distance (insertions/deletions/substitutions) |
| `F.initcap(col)` | StringType | `initcap('hello world')` → `'Hello World'` | Capitalize first letter of each word |
| `F.conv(num_str, from_base, to_base)` | StringType | `conv('FF', 16, 10)` → `'255'` | Base conversion; returns StringType |
| `F.unhex(col)` | BinaryType | `unhex('48656C6C6F')` → binary | Inverse of hex(); pairs of hex digits → bytes |

### DataFrame Array/Map Functions

| Function | Return Type | Example | Notes |
|----------|-------------|---------|-------|
| `F.array_repeat(elem, count)` | ArrayType | `array_repeat('x', 3)` → `['x', 'x', 'x']` | Repeat element count times |
| `F.sort_array(arr, asc=True)` | ArrayType | `sort_array([3, 1, 2], True)` → `[1, 2, 3]` | Nulls at beginning; asc=False for descending |
| `F.array_sort(arr)` | ArrayType | `array_sort([3, 1, None, 2])` → `[1, 2, 3, None]` | Nulls at end |
| `F.map_entries(map_col)` | ArrayType(StructType) | `map_entries(map('a', 1))` → `[{a, 1}]` | Convert map to array of {key, value} structs |

### Configuration Quick Reference

| Setting | Default | Purpose | Example |
|---------|---------|---------|---------|
| `spark.sql.shuffle.partitions` | 200 | Post-shuffle partition count (SQL/DF) | `spark.conf.set('spark.sql.shuffle.partitions', 100)` |
| `spark.driver.memory` | 1g | Driver JVM heap size | Increase for `collect()` on large results |
| `spark.executor.cores` | 1 | Cores per executor | Combined with `spark.task.cpus` for multi-core tasks |
| `spark.task.cpus` | 1 | CPU cores required per task | Set to 2+ for multi-threaded native library tasks |
| `spark.memory.offHeap.enabled` | false | Enable off-heap memory allocation | Set to `true` to reduce GC pressure |
| `spark.memory.offHeap.size` | 0 | Off-heap memory bytes | E.g., `1g` |
| `spark.memory.storageFraction` | 0.5 | Fraction of unified memory for storage (cache) | Remaining fraction for execution |
| `spark.sql.autoBroadcastJoinThreshold` | 10m | Max table size for automatic broadcast join | -1 disables; measured by Spark's estimate |
| `spark.dynamicAllocation.enabled` | false | Enable dynamic executor scaling | With `spark.executor.instances` → ignored |
| `spark.dynamicAllocation.minExecutors` | N/A | Min executor count | Required when dynamic allocation enabled |
| `spark.dynamicAllocation.maxExecutors` | N/A | Max executor count | Cap on executor scaling |
| `spark.sql.broadcastTimeout` | 300s | Wait time for executor to receive broadcast | Increase for large broadcasts or slow networks |
| `spark.sql.adaptive.enabled` | true (3.2+) | Enable Adaptive Query Execution | Default on; controls AQE features |
| `spark.sql.files.ignoreMissingFiles` | false | Skip missing input files (not error) | Useful for data lakes with concurrent compaction |
| `spark.shuffle.file.buffer` | 32k | Write buffer per shuffle output file | Larger = fewer syscalls, better throughput |
| `spark.sql.adaptive.advisoryPartitionSizeInBytes` | 64m | Target size for AQE partition coalescing | Post-shuffle partition merging |
| `spark.executor.maxResultSize` | 1g | Max result size returned to driver | Governs `collect()`; RPC size limit separate |
| `spark.rpc.message.maxSize` | 128m | Max RPC message size | Limits single RPC payload; set with `spark.rpc.message.maxSize` |
| `spark.sql.execution.arrow.pyspark.enabled` | false | Use Arrow for JVM↔Python transfer | Enable for `toPandas()`, Pandas UDFs |
| `spark.eventLog.enabled` | false | Enable event logging for History Server | Must be `true` for History Server |
| `spark.eventLog.dir` | /tmp/spark-events | Durable storage path for event logs | Must be HDFS/S3/shared network path |

### Topic Difficulty Breakdown (Iteration 5)

| Topic | Questions | Easy | Medium | Hard | Percentage |
|-------|-----------|------|--------|------|-----------|
| Apache Spark Architecture & Internals | 1–20 | 4 | 11 | 5 | 20% |
| Spark SQL | 21–40 | 6 | 12 | 2 | 20% |
| DataFrame/DataSet API | 41–70 | 4 | 19 | 7 | 30% |
| Troubleshooting & Tuning | 71–80 | 0 | 7 | 3 | 10% |
| Structured Streaming | 81–90 | 1 | 7 | 2 | 10% |
| Spark Connect | 91–95 | 0 | 3 | 2 | 5% |
| Pandas API on Spark | 96–100 | 1 | 3 | 1 | 5% |

### Exam Question Patterns

**Single-Choice (78 questions)**: One correct answer among four options.

**Multiple-Choice (22 questions)**: Two or more correct answers among four options; marked with "Select all that apply."

**Answer Modality**:
- Recognize correct answer (ABC questions)
- Avoid common pitfalls (misconceptions)
- Match behavior to configuration
- Understand Spark internal vs external behavior

### Memory Anchors for Each Topic

#### Architecture & Internals
- **200**: Default `spark.sql.shuffle.partitions`
- **1g**: Default `spark.driver.memory`
- **300s**: Default `spark.sql.broadcastTimeout`
- **LRU**: Cache eviction policy (Least Recently Used)
- **PROCESS_LOCAL → NODE_LOCAL → RACK_LOCAL → ANY**: Locality preference order

#### Spark SQL
- **1-based**: Indexing in `locate()` (not 0-based)
- **False**: Nulls at end in `array_sort()`; True: nulls at beginning in `sort_array()`
- **GROUPING_ID = 0**: All columns grouped; GROUPING_ID = 3: Both rolled up (bitmask)
- **Recursive CTEs**: NOT supported in Spark SQL through 3.5

#### DataFrame API
- **`.columns`**: Returns Python list of strings
- **`.transform(func)`**: Calls `func(df)` and returns DataFrame
- **`.toLocalIterator()`**: Streams one partition at a time (safe for memory)
- **`.collect()`**: Materializes entire DataFrame in driver memory (risky)
- **`foreachPartition`**: Efficient for per-connection setup (database writes)

#### Troubleshooting & Tuning
- **Arrow**: Columnar format for JVM↔Python transfer; requires PyArrow
- **Column pruning**: Removes unreferenced columns; Predicate pushdown: moves filters to source
- **Off-heap**: Allocated outside JVM heap, not subject to GC
- **AQE coalescing**: Target `spark.sql.adaptive.advisoryPartitionSizeInBytes` = 64 MB (default)

#### Structured Streaming
- **`trigger(once=True)`**: Single mega-batch
- **`trigger(availableNow=True)`**: Multiple micro-batches, better for large backlogs
- **Watermark = processing_time − delay**: Late data past watermark is dropped
- **`session_window`**: Dynamic; new session on gap > timeout
- **Console sink**: stdout output; development only; supports all output modes

#### Spark Connect
- **Client-side**: No JVM required
- **Server-side**: Analysis errors surfaced at action time
- **UDF serialization**: Sent to server; external libraries on executor environment
- **Server crash**: Client does NOT crash; in-progress query lost; no auto-replay

#### Pandas API on Spark
- **`NULL` vs `NaN`**: Distinct in pandas-on-Spark; both missing in native pandas
- **`psdf.dropna()`**: Drops `NULL` rows; does NOT drop `NaN`
- **`psdf.spark.cache()`**: Bridge to Spark DataFrame operations
- **`default_index_type`**: `"distributed-sequence"` (default); `"sequence"` (slow, fully ordered); `"distributed"` (fastest, non-contiguous)

### 7-Day Study Progression (Quick Track)

**Day 1 (3 hours)**: Architecture & Internals + Spark SQL
- Read STUDY_GUIDE sections 1 and 2
- Memorize 10 key configuration defaults
- Review Answer Key for Q1–40

**Day 2 (3 hours)**: DataFrame API (Part A)
- Read STUDY_GUIDE section 3 (first half: columns, transform, iterators, structs)
- Review Answer Key for Q41–55

**Day 3 (3 hours)**: DataFrame API (Part B) + Troubleshooting
- Read STUDY_GUIDE section 3 (second half: sorting, caching, I/O)
- Read STUDY_GUIDE section 4 (Troubleshooting & Tuning)
- Review Answer Key for Q56–80

**Day 4 (3 hours)**: Structured Streaming + Spark Connect
- Read STUDY_GUIDE sections 5 and 6
- Review Answer Key for Q81–95

**Day 5 (3 hours)**: Pandas API on Spark + Mixed Review
- Read STUDY_GUIDE section 7
- Review Answer Key for Q96–100
- Quick review of 5 random questions from each topic

**Day 6 (3 hours)**: Full Mock Test
- Take full 100-question practice test under timed conditions (2 hours)
- Review incorrect answers (1 hour)

**Day 7 (3 hours)**: Final Review + Exam Readiness Drill
- Review QUICK_REFERENCE tables (30 min)
- Targeted review of weak topic areas (90 min)
- Exam day checklist and mental preparation (60 min)

---

**Total Study Time**: 21 hours over 7 days (3 hours/day)

Use this guide for quick lookups during study and exam practice. Cross-reference with STUDY_GUIDE_ITER5.md for detailed explanations.

---

**End of Quick Reference (Iteration 5)**
