# Quick Reference — Databricks Certified Associate Developer for Apache Spark
## Iteration 8

---

## 🚨 ANSWER KEY — ALL 100 QUESTIONS

### Critical: Answer Distribution
- **96 questions = B**
- **4 questions = A: Q31, Q60, Q71, Q81**

### 10×10 Answer Grid

|    | ×0 | ×1 | ×2 | ×3 | ×4 | ×5 | ×6 | ×7 | ×8 | ×9 |
|----|----|----|----|----|----|----|----|----|----|----|
| 0× | — | B | B | B | B | B | B | B | B | B |
| 1× | B | B | B | B | B | B | B | B | B | B |
| 2× | B | B | B | B | B | B | B | B | B | B |
| 3× | **A** | B | B | B | B | B | B | B | B | B |
| 4× | B | B | B | B | B | B | B | B | B | B |
| 5× | B | B | B | B | B | B | B | B | B | B |
| 6× | **A** | B | B | B | B | B | B | B | B | B |
| 7× | **A** | B | B | B | B | B | B | B | B | B |
| 8× | **A** | B | B | B | B | B | B | B | B | B |
| 9× | B | B | B | B | B | B | B | B | B | B |
| 10× | B | | | | | | | | | |

*Row ×0 = Q1–9, row 1× = Q10–19, row 3× = Q30–39, 3×0 = Q30, 3×1 = Q31, etc.*

### Full Answer Key — Column Format

```
Q1=B  Q2=B  Q3=B  Q4=B  Q5=B  Q6=B  Q7=B  Q8=B  Q9=B  Q10=B
Q11=B Q12=B Q13=B Q14=B Q15=B Q16=B Q17=B Q18=B Q19=B Q20=B
Q21=B Q22=B Q23=B Q24=B Q25=B Q26=B Q27=B Q28=B Q29=B Q30=B
Q31=A Q32=B Q33=B Q34=B Q35=B Q36=B Q37=B Q38=B Q39=B Q40=B
Q41=B Q42=B Q43=B Q44=B Q45=B Q46=B Q47=B Q48=B Q49=B Q50=B
Q51=B Q52=B Q53=B Q54=B Q55=B Q56=B Q57=B Q58=B Q59=B Q60=A
Q61=B Q62=B Q63=B Q64=B Q65=B Q66=B Q67=B Q68=B Q69=B Q70=B
Q71=A Q72=B Q73=B Q74=B Q75=B Q76=B Q77=B Q78=B Q79=B Q80=B
Q81=A Q82=B Q83=B Q84=B Q85=B Q86=B Q87=B Q88=B Q89=B Q90=B
Q91=B Q92=B Q93=B Q94=B Q95=B Q96=B Q97=B Q98=B Q99=B Q100=B
```

### Why the A Answers

| Q# | Why A, not B? |
|---|---|
| Q31 | `to_utc_timestamp` = local→UTC (not the other way round). Option A gives the correct directional definition. |
| Q60 | `how="all"` = ALL columns null; `how="any"` = AT LEAST ONE column null. Option A has the definitions the right way round; B reverses them. |
| Q71 | AQE coalesce config (`coalescePartitions.enabled=true`, `advisoryPartitionSizeInBytes`) is described in option A; option B wrongly describes `shuffle.partitions=auto`. |
| Q81 | Correct listener registration (`spark.streams.addListener()`), correct 3 callbacks (`onQueryStarted`, `onQueryProgress`, `onQueryTerminated`) is in option A; option B wrongly labels it a Databricks-proprietary API. |

---

## Topic-by-Topic Answer Key

### Architecture Q1–Q20 (all B)

| Q# | Answer | One-Line Summary |
|---|---|---|
| Q1 | B | Tasks/stage = number of partitions |
| Q2 | B | Execution evicts storage above storageFraction watermark |
| Q3 | B | Sort shuffle: 1 data + 1 index file per mapper (2×M total) |
| Q4 | B | `TaskContext.get().partitionId()` + `.attemptNumber()` |
| Q5 | B | Barrier mode: all tasks start simultaneously; whole stage fails on any failure |
| Q6 | B | Default = FIFO; FAIR interleaves concurrent jobs |
| Q7 | B | `python.worker.reuse=true` keeps Python worker alive across tasks |
| Q8 | B | `checkpoint()` truncates lineage; `persist(DISK_ONLY)` retains lineage |
| Q9 | B | Locality: PROCESS_LOCAL→NODE_LOCAL→RACK_LOCAL→ANY (3s each) |
| Q10 | B | UnsafeRow = binary off-heap format, fields via getLong/getInt, no GC |
| Q11 | B | `executor.instances` **ignored** when dynamic allocation enabled |
| Q12 | B | `maxPartitionBytes` caps data per input partition (default 128 MB) |
| Q13 | B | Accumulators double-count on task retries |
| Q14 | B | `broadcastTimeout` = driver wait time to complete broadcast (default 300s) |
| Q15 | B | CLI flags override `spark-defaults.conf` (CLI wins) |
| Q16 | B | `rdd.compress` compresses serialized RDD partitions |
| Q17 | B | `driver.maxResultSize` caps total serialized result to driver (default 1 GB) |
| Q18 | B | `addFile` → `SparkFiles.get()`; `addJar` → executor classpath |
| Q19 | B | Arrow enabled → columnar IPC for `toPandas`/`createDataFrame`, 10–100× faster |
| Q20 | B | `retainedJobs`/`retainedStages` = FIFO-evicted in-memory Web UI cache |

### SQL Q21–Q40 (Q31=A, rest B)

| Q# | Answer | One-Line Summary |
|---|---|---|
| Q21 | B | `regexp_replace` no match → returns original string |
| Q22 | B | `overlay(str, repl, pos, len)` = positional replacement, no regex |
| Q23 | B | `soundex()` = 4-char phonetic code for fuzzy matching |
| Q24 | B | `initcap()` = title case (first letter per word upper) |
| Q25 | B | `array_distinct()` = unique elements; null preserved once |
| Q26 | B | `array_union/intersect/except` = set ops; all deduplicate |
| Q27 | B | `aggregate()` = fold-left; optional `finish` post-processes accumulator |
| Q28 | B | `forall([]) = true`; `exists([]) = false`; null array → null |
| Q29 | B | `zip_with` result length = longer array; shorter padded with null |
| Q30 | B | `map_from_entries` = array of 2-field structs → MapType; dup keys: last wins |
| Q31 | **A** | `to_utc_timestamp` = local→UTC; `from_utc_timestamp` = UTC→local |
| Q32 | B | `make_date` invalid → **null** (no exception) |
| Q33 | B | `datediff` = integer days; `timestampdiff` = any unit (Spark 3.3+) |
| Q34 | B | `sequence(start, stop, step)` negative step → descending array |
| Q35 | B | `try_cast` → null; `try_divide` → null for ÷0 |
| Q36 | B | `UNPIVOT` (Spark 3.4+) converts wide columns to rows |
| Q37 | B | `QUALIFY` filters on window results without subquery (Spark 3.3+) |
| Q38 | B | `TABLESAMPLE(10 PERCENT)` ≈ 10%; `TABLESAMPLE(100 ROWS)` ≤ 100 rows |
| Q39 | B | `LATERAL VIEW OUTER` preserves null/empty array rows |
| Q40 | B | `schema_of_json()` returns DDL string; string literal only |

### DataFrame Q41–Q70 (Q60=A, rest B)

| Q# | Answer | One-Line Summary |
|---|---|---|
| Q41 | B | `write.mode("overwrite")` = deletes existing directory |
| Q42 | B | `partitionBy` = Hive-style directory tree; partition cols removed from file |
| Q43 | B | `bucketBy(64, "user_id")` = 64 fixed buckets; join skips shuffle when both tables match |
| Q44 | B | `writeTo()` = DS V2 API; supports `overwrite(condition)`, `createOrReplace`, etc. |
| Q45 | B | `observe()` = compute named metrics in single pass during action |
| Q46 | B | `freqItems()` = Misra-Gries; `support` = minimum fraction threshold |
| Q47 | B | Pandas scalar UDF receives Series per Arrow batch; standard UDF receives one scalar |
| Q48 | B | `localCheckpoint()` = executor local disk; truncates lineage; NOT fault-tolerant |
| Q49 | B | `F.input_file_name()` = fully qualified source file path per row |
| Q50 | B | `stat.crosstab()` = contingency table; col1=rows, col2=columns, cells=counts |
| Q51 | B | `regexp_extract` no match → **`""`** (empty string), not null |
| Q52 | B | `split(str, pat, limit)` → at most `limit` elements; last = remainder |
| Q53 | B | `from_json` permissive: missing=null, extra ignored, malformed=all-null struct |
| Q54 | B | `StructType.fromDDL()` parses DDL; all fields nullable by default |
| Q55 | B | `randomSplit` reproducible with seed; cache source to avoid double-scan |
| Q56 | B | `hint("broadcast")` forces BHJ regardless of size threshold |
| Q57 | B | `encode(str, charset)` → Binary; `decode(binary, charset)` → String |
| Q58 | B | `maxRecordsPerFile` limits rows per output file (splits within task) |
| Q59 | B | `sortWithinPartitions` = no shuffle; `orderBy` = global sort + shuffle |
| Q60 | **A** | `na.drop(how="all")` = ALL null; `how="any"` = ANY null |
| Q61 | B | Resolve ambiguous join column via `df1["id"]` or list-of-string join |
| Q62 | B | `when()` chain without `.otherwise()` → **null** for unmatched rows |
| Q63 | B | `df.select(F.col("*"), new_col)` = all columns + appended new column |
| Q64 | B | `withColumn` on existing name silently **overwrites** the column |
| Q65 | B | `df.toDF(*names)` renames all columns; count mismatch → AnalysisException |
| Q66 | B | `crossJoin` = Cartesian product M×N; enabled by default in Spark 3.x |
| Q67 | B | `selectExpr()` accepts SQL expression strings; `"*"` expands all columns |
| Q68 | B | `distinct()` = all columns; `dropDuplicates(["id"])` = on subset |
| Q69 | B | `F.expr()` for complex SQL; `F.col() + F.col()` for simple arithmetic |
| Q70 | B | `rowsBetween` = physical rows; `rangeBetween` = includes tied ORDER BY peers |

### Troubleshooting Q71–Q80 (Q71=A, rest B)

| Q# | Answer | One-Line Summary |
|---|---|---|
| Q71 | **A** | AQE coalesce: `coalescePartitions.enabled=true`; merges adjacent small partitions |
| Q72 | B | `storageFraction` = fraction of unified memory protected from eviction (default 0.5) |
| Q73 | B | `EXPLAIN CODEGEN` shows generated Java; `!` marks pipeline breaks |
| Q74 | B | Skew join: few straggler tasks; AQE splits + replicates |
| Q75 | B | `autoBroadcastJoinThreshold=-1` completely disables auto broadcast |
| Q76 | B | Both ORC & Parquet are columnar; Parquet = ecosystem standard; ORC = Hive ACID |
| Q77 | B | G1GC recommended; `-XX:+UseG1GC` in `executor.extraJavaOptions` |
| Q78 | B | `inMemoryColumnarStorage.batchSize` = rows per cache batch (default 10000) |
| Q79 | B | `eventLog.enabled=true` writes events to `eventLog.dir` for History Server |
| Q80 | B | Shuffle spill: `Shuffle Spill (Memory)` + `Shuffle Spill (Disk)` in Stage UI |

### Streaming Q81–Q90 (Q81=A, rest B)

| Q# | Answer | One-Line Summary |
|---|---|---|
| Q81 | **A** | `spark.streams.addListener()`; 3 callbacks: Started, Progress, Terminated |
| Q82 | B | `mapGroupsWithState` = exactly 1 output; `flatMapGroupsWithState` = 0 or more |
| Q83 | B | `failOnDataLoss=true` raises on missing Kafka offsets; false skips |
| Q84 | B | `complete` mode rewrites entire result table; needed without watermark |
| Q85 | B | `Trigger.Once()` = 1 micro-batch; `AvailableNow()` = multi micro-batch (Spark 3.3+) |
| Q86 | B | `maxFilesPerTrigger` limits new files per micro-batch |
| Q87 | B | Stream-static join: static re-read each batch; late streaming rows cannot recover |
| Q88 | B | `orderBy()` on streaming DF → AnalysisException (requires seeing all rows) |
| Q89 | B | Continuous processing: ms latency; stateless only; Kafka/Rate sources only |
| Q90 | B | Rate source: `timestamp` (TimestampType) + `value` (LongType from 0) |

### Spark Connect Q91–Q95 (all B)

| Q# | Answer | One-Line Summary |
|---|---|---|
| Q91 | B | Spark Connect = decoupled gRPC client-server; plan built locally, sent on action |
| Q92 | B | Transformations build local plan; action serializes protobuf and sends to server |
| Q93 | B | TLS: `sc://host:port/;use_ssl=true;token=...` in connection URL |
| Q94 | B | SparkContext/RDD APIs NOT available via Connect client |
| Q95 | B | Protobuf field numbers allow client/server version independence |

### Pandas API Q96–Q100 (all B)

| Q# | Answer | One-Line Summary |
|---|---|---|
| Q96 | B | `ps.from_pandas(pdf)` converts pandas DF to Pandas-on-Spark |
| Q97 | B | Cross-DF ops raise ValueError; enable with `ops_on_diff_frames=True` |
| Q98 | B | `ps.get_dummies()` = one-hot encoding; one binary column per distinct value |
| Q99 | B | `shortcut_limit=1000`: small DFs short-circuit to local Pandas |
| Q100 | B | `sequence` = consecutive (shuffle); `distributed-sequence` = non-consecutive (no shuffle) |

---

## Cheatsheet: Key Configuration Defaults

| Config | Default | Controls |
|---|---|---|
| `spark.memory.fraction` | **0.6** | Fraction of JVM heap for unified memory |
| `spark.memory.storageFraction` | **0.5** | Fraction of unified region protected from eviction |
| `spark.sql.files.maxPartitionBytes` | **128 MB** | Max data per input partition |
| `spark.sql.autoBroadcastJoinThreshold` | **10 MB** | Auto-broadcast size threshold; -1 = disable |
| `spark.sql.broadcastTimeout` | **300 s** | Max driver wait for broadcast completion |
| `spark.sql.shuffle.partitions` | **200** | Number of partitions after a shuffle |
| `spark.sql.adaptive.enabled` | **true** | Enables AQE |
| `spark.sql.adaptive.advisoryPartitionSizeInBytes` | **64 MB** | Target partition size for AQE coalesce |
| `spark.driver.maxResultSize` | **1 GB** | Max serialized result collected to driver |
| `spark.locality.wait` | **3 s** | Wait per locality level before degrading |
| `spark.python.worker.reuse` | **true** | Reuse Python workers across tasks |
| `spark.sql.inMemoryColumnarStorage.batchSize` | **10000** | Rows per columnar cache batch |
| `spark.ui.retainedJobs` / `retainedStages` | **1000** | In-memory Web UI history cache size |
| `ps.options.compute.shortcut_limit` | **1000** | Small DF → local Pandas short-circuit threshold |

---

## Cheatsheet: HOF Quick Reference

| HOF | Empty Array | Null Array | Length of Result |
|---|---|---|---|
| `forall(arr, pred)` | **true** (vacuously) | **null** | N/A (boolean) |
| `exists(arr, pred)` | **false** | **null** | N/A (boolean) |
| `aggregate(arr, zero, merge)` | Returns `zero` | **null** | N/A (scalar) |
| `zip_with(a1, a2, func)` | `[]` | **null** | **max(len(a1), len(a2))** — pads shorter |
| `filter(arr, pred)` | `[]` | **null** | 0 to len(arr) |
| `transform(arr, func)` | `[]` | **null** | Same as input |

---

## Cheatsheet: String Function Returns

| Function | No Match / Invalid Input | Null Input |
|---|---|---|
| `regexp_replace(col, pat, repl)` | Returns **original string** | null |
| `regexp_extract(col, pat, idx)` | Returns **`""`** (empty string) | null |
| `split(str, pat, limit)` | Array with full string as only element | null |
| `soundex(str)` | Works on any ASCII string | null |
| `make_date(y, m, d)` | Returns **null** (no exception) | null |
| `try_cast(expr AS type)` | Returns **null** | null |
| `try_divide(a, b)` when b=0 | Returns **null** | null |
| `overlay(str, repl, pos)` | Always produces output | null |

---

## Cheatsheet: Timestamp Direction

```
to_utc_timestamp(ts, tz)    →  LOCAL TIME → UTC      (think: "to UTC")
from_utc_timestamp(ts, tz)  →  UTC → LOCAL TIME      (think: "from UTC")

Example (US/Eastern, UTC-4 in summer):
  to_utc_timestamp('2026-04-25 10:00', 'US/Eastern')   = '2026-04-25 14:00'  (added 4h)
  from_utc_timestamp('2026-04-25 14:00', 'US/Eastern') = '2026-04-25 10:00'  (subtracted 4h)
```

---

## Cheatsheet: Shuffle File Layout

```
Hash Shuffle (legacy):          M × R files  (M mappers, R reducers)
Sort Shuffle (current default): 2 × M files  (1 data file + 1 index file per mapper)
```

---

## Cheatsheet: Write Modes

| Mode | Existing Path Exists | Existing Path Absent |
|---|---|---|
| `overwrite` | Deletes and rewrites | Creates |
| `append` | Adds new files | Creates |
| `error` (default) | **Raises exception** | Creates |
| `ignore` | **Silently skips** | Creates |

---

## Cheatsheet: Checkpoint Comparison

| Property | `checkpoint()` | `localCheckpoint()` |
|---|---|---|
| Storage | Reliable FS (HDFS/S3) | Executor local disk |
| Fault-tolerant | **Yes** | **No** |
| Lineage truncated | Yes | Yes |
| Requires `setCheckpointDir()` | **Yes** | No |
| Speed | Slower (extra network write) | Faster |

---

## Cheatsheet: Streaming Triggers

| Trigger | One Batch? | Stops After? | Rate Limits Applied? |
|---|---|---|---|
| `Trigger.Once()` | Yes (one) | Yes | No |
| `Trigger.AvailableNow()` | No (many) | Yes | **Yes** |
| `Trigger.ProcessingTime("30s")` | Recurring | No | Yes |
| `Trigger.Continuous("1s")` | N/A (continuous) | No | Very limited |

---

## Cheatsheet: Streaming Output Modes

| Mode | Writes What | Aggregation Required? | Watermark? |
|---|---|---|---|
| `append` | Only new rows | Optional | With aggregation: yes |
| `update` | Only changed rows | Optional | Optional |
| `complete` | **Entire result table** | **Required** | No (can't use with watermark) |

---

## Cheatsheet: na.drop how Parameter

```
df.na.drop(how="any")   → drops rows where AT LEAST ONE column is null
df.na.drop(how="all")   → drops rows where ALL columns are null
                         ↑ "all" means fewer rows dropped (stricter criterion)
```

---

## Cheatsheet: window frame

```
ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
  → counts by physical row position
  → strict running total (no tie sharing)

RANGE BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
  → includes all rows with ORDER BY value ≤ current row's value
  → tied rows share the same cumulative value (frame extends to peers)
```

---

## Cheatsheet: Spark Connect Availability

| API | Available via Connect? |
|---|---|
| `spark.sql()` | ✅ Yes |
| `spark.read.parquet()` | ✅ Yes |
| `df.groupBy().agg()` | ✅ Yes |
| `spark.udf.register()` | ✅ Yes |
| `sc.parallelize()` | ❌ No |
| `sc.addFile()` / `sc.addJar()` | ❌ No |
| `rdd.map()` / any RDD op | ❌ No |
| `sc.setCheckpointDir()` | ❌ No |
| `sc.broadcast()` (low-level) | ❌ No |

---

## Cheatsheet: Pandas API on Spark Index Types

| Index Type | Consecutive? | Shuffle? | Positional `iloc`? |
|---|---|---|---|
| `"distributed-sequence"` (default) | **No** (unique per partition) | No | Unreliable |
| `"sequence"` | **Yes** (0,1,2,…) | Yes | Yes |

Change: `ps.set_option("compute.default_index_type", "sequence")`

---

## Cheatsheet: ORC vs Parquet Summary

| | ORC | Parquet |
|---|---|---|
| Format | Columnar | Columnar |
| Native ACID | Yes (Hive) | No |
| Ecosystem | Hive, legacy | Delta, Iceberg, Arrow, Flink, Presto |
| Complex nested types | Good | **Better** |
| Choose when | Hive ACID pipelines | Delta Lake, Databricks, cross-platform |

---

## Cheatsheet: GC Recommendation

```
Recommended: G1GC
Flag: -XX:+UseG1GC
Where: spark.executor.extraJavaOptions

Key tuning flags:
  -XX:G1HeapRegionSize=16m            (set for large heaps)
  -XX:InitiatingHeapOccupancyPercent=35  (trigger concurrent marking earlier)
  -XX:MaxGCPauseMillis=200             (pause time target)
```

---

## Exam Decision Tree: "What kind of shuffle/join is this?"

```
Join question?
├── Tiny table (< threshold)? → Broadcast Hash Join (BHJ)
│     └── Override threshold? → use hint("broadcast")  Q56
│     └── Disable auto-BHJ?  → autoBroadcastJoinThreshold=-1  Q75
├── Both tables bucketed same way? → Bucket join (no shuffle)  Q43
├── Sort-Merge Join? → global sort + 2 shuffles
└── Cross join? → crossJoin(), M×N rows  Q66

Sort question?
├── Global order needed? → orderBy() → shuffle  Q59
└── Local per-partition? → sortWithinPartitions() → no shuffle  Q59
```

---

## Exam Decision Tree: "What does this streaming trigger do?"

```
Want to run all backlog data, then stop?
├── Small backlog (fits in one batch) → Trigger.Once()
└── Large backlog (needs rate limits) → Trigger.AvailableNow()  (Spark 3.3+)

Want continuous scheduled runs? → Trigger.ProcessingTime("30 seconds")
Want millisecond latency (experimental, stateless only)? → Trigger.Continuous("1 second")
```

---

## Exam Decision Tree: "Which memory config?"

```
Execution evicting too much cached data?
  → Increase spark.memory.storageFraction (protect more storage)  Q72

Shuffle spill happening?
  → Increase spark.memory.fraction (more unified memory)
  → Or reduce shuffle partitions (fewer, larger tasks)  Q80

Input partitions too large → executor OOM?
  → Decrease spark.sql.files.maxPartitionBytes  Q12

Auto-broadcast causing OOM?
  → Set spark.sql.autoBroadcastJoinThreshold=-1  Q75
```

---

## Iteration 8 Difficulty Summary

| Topic | Q Range | Easy | Medium | Hard | Non-B Answers |
|---|---|---|---|---|---|
| Architecture | Q1–Q20 | 1 | 10 | 9 | None |
| SQL | Q21–Q40 | 1 | 9 | 10 | Q31=A |
| DataFrame API | Q41–Q70 | 1 | 18 | 11 | Q60=A |
| Tuning | Q71–Q80 | 0 | 4 | 6 | Q71=A |
| Streaming | Q81–Q90 | 0 | 5 | 5 | Q81=A |
| Spark Connect | Q91–Q95 | 0 | 3 | 2 | None |
| Pandas API | Q96–Q100 | 1 | 2 | 2 | None |
| **Total** | **Q1–Q100** | **4** | **51** | **45** | **4 = A** |

*Note: Difficulty totals may differ from header (9/55/36) due to easy/medium boundary differences in classification.*
