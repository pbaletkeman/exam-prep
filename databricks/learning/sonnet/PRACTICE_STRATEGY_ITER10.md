# Practice Strategy — Iteration 10
## Databricks Certified Associate Developer for Apache Spark

**Total questions**: 100 | **Unique correct answer**: B (99×) + **A (Q76 only)**

---

## Step 0 — Read This First

This iteration has an unusual property: **all 99 answers are B except Q76 (Answer A)**.

This is both a gift and a trap:
- Gift: you can quickly check yourself — if you chose anything other than B, you need a reason.
- Trap: pattern matching will lull you into choosing B for Q76. The exam will exploit this.

**Commit to memory before anything else**: Q76 = Answer A, `spark.sql.parquet.compression.codec`.

---

## Step 1 — Triage by Difficulty (Day 1 or Session 1)

Work through questions in this order to build momentum and identify gaps efficiently.

### Easy Questions (10 total) — Target: 100%
Attempt all easy questions first as a warm-up and confidence builder.

| Q# | Topic | Key fact to recall |
|---|---|---|
| Q1 | `autoBroadcastJoinThreshold` | 10 MiB default |
| Q15 | AQE coalescePartitions | Can go below `shuffle.partitions` |
| Q21 | `F.transform` | Element-wise, same-length output |
| Q26 | `to_date` vs `to_timestamp` | DateType vs TimestampType |
| Q30 | `concat_ws` | Skips nulls |
| Q60 | `F.lag` with default | Returns `default` at boundary |
| Q69 | `describe` vs `summary` | `summary` adds percentiles |
| Q84 | `processAllAvailable()` | Test-only blocking call |
| Q91 | `builder.remote()` | `sc://` scheme, no local JVM |
| Q96 | `psdf.melt()` | Wide → long |

If you miss any easy question, read its explanation in the STUDY_GUIDE before continuing.

---

### Medium Questions (54 total) — Target: ≥ 85%

Group by subtopic for focused sessions:

#### Session A — Architecture configs (Q2, Q4, Q6, Q8, Q10–Q12, Q14, Q16, Q18)
Priority focus:
- `memory.fraction` / `memory.storageFraction` interaction
- `lz4` vs `snappy` codec defaults
- `mergeSchema` cost
- `ignoreCorruptFiles` vs `ignoreMissingFiles` independence
- SparkConf priority order

#### Session B — Array/Map/String/Date SQL (Q22–Q24, Q27–Q28, Q31, Q33, Q35, Q36, Q38–Q39)
Priority focus:
- `explode` vs `explode_outer` — null/empty row retention
- `posexplode` output column names: `pos` + `col`
- `get_json_object` always returns StringType
- `split` with limit — third element absorbs rest
- `hex` → String; `unhex` → **Binary** (not integer)
- Leap year day count: 2024 March 1 = day 61

#### Session C — DataFrame API (Q41–Q43, Q46, Q48–Q51, Q53–Q54, Q56–Q57, Q61, Q63–Q65, Q67–Q68, Q70)
Priority focus:
- `df.transform(func)` = `func(df)` — no magic, just chaining
- `union` (position) vs `unionByName` (name) — same trap appears twice (Q51 + Q70)
- `insertInto` (position) vs `saveAsTable append` (name)
- `createGlobalTempView` raises; `createOrReplace` is safe
- `element_at` on maps returns null (not error) in non-ANSI mode
- `describe()` limited to 5 stats; `summary()` adds percentiles
- `withColumns(dict)` for batch column addition (Spark 3.3+)
- `F.greatest` ignores nulls (only null if all null)

#### Session D — Streaming + Connect + Pandas API (Q71, Q75, Q81–Q83, Q86, Q88–Q89, Q92, Q94–Q97, Q99–Q100)
Priority focus:
- AQE `false → true` at Spark 3.2
- Timestamp timezone display: UTC 12:00 → NY 08:00 (UTC-4)
- `processingTime` trigger never concurrent
- `writeStream.toTable` updates catalog; `start(path)` doesn't
- Rate source: `timestamp` + `value` (two columns)
- Memory sink → temp view accessible via `spark.sql()`
- `streaming.numShufflePartitions` is streaming-only
- `spark.addArtifact()` replaces `sc.addFile()/addJar()`
- Port 15002 is the Connect default
- `conf.set()` → session-scoped in Connect
- `psdf.melt()` = wide to long
- `psdf.assign()` = immutable (returns new); `[]` = in-place
- `psdf.explode()` preserves null/empty as NaN

---

### Hard Questions (36 total) — Target: ≥ 70%

These require deeper reasoning. Do these after the medium questions.

#### Architecture Hard (Q3, Q5, Q7, Q9, Q13, Q17, Q19, Q20)

| Q# | Must-know |
|---|---|
| Q3 | `memoryOverhead` (absolute MiB) beats `memoryOverheadFactor`; calc: max(0.15×8192, 384)=1228 |
| Q5 | `ReuseExchange`: same shuffle computed once, shared via `ReusedExchangeExec` |
| Q7 | `spark.shuffle.service.db.enabled=true` → LevelDB; survives ESS restart |
| Q9 | `maxIterations` default = 100; raise for deeply correlated queries |
| Q13 | `planCacheSize` = LRU cache count for SQL logical plans |
| Q17 | `LEGACY` = Spark 2.x lenient parser; `CORRECTED` = strict (3.x default) |
| Q19 | `useV1SourceList` = CSV of format names → forced V1 code path |
| Q20 | After AQE SMJ→BHJ: `LocalShuffleReaderExec` reads own local files only |

#### SQL Hard (Q25, Q29, Q32, Q34, Q37, Q40)

| Q# | Must-know |
|---|---|
| Q25 | `arrays_zip` pads shorter array with null; output field names = input column names |
| Q29 | `json_tuple` parses once for n fields → more efficient than n×`get_json_object` |
| Q32 | `element_at` 1-based; `-1` = last; vs `[]` = 0-based |
| Q34 | `F.levenshtein(l, r) <= n` = filter by edit distance |
| Q37 | `F.map_filter(map, lambda k, v: cond)` = MapType output |
| Q40 | `map_keys`/`map_values` ordering is **non-deterministic** |

#### DataFrame API Hard (Q44–Q45, Q47, Q52, Q55, Q58, Q62, Q66)

| Q# | Must-know |
|---|---|
| Q44 | `F.map_entries(map)` → `ArrayType(StructType([key, value]))` |
| Q45 | `F.inline(arr_of_structs)` → one row per struct; field names become columns |
| Q47 | `df.stat.bloomFilter()` returns a `BloomFilter` object NOT a DataFrame |
| Q52 | `F.named_struct(lit("x"), lit(3.0), ...)` alternates name literals + values |
| Q55 | `countMinSketch` returns `CountMinSketch` object for frequency estimates |
| Q58 | `percent_rank` first=0.0; `cume_dist` first>0 (always at least 1/n) |
| Q62 | `F.slice(arr, 2, 3)` = `["b","c","d"]` (1-based; not 0-based like Python) |
| Q66 | `F.from_json(col, ArrayType(schema))` needed for JSON array strings |

#### Streaming + Tuning Hard (Q72, Q74, Q76, Q78, Q80, Q82, Q85, Q87, Q90)

| Q# | Must-know |
|---|---|
| Q72 | `mapKeyDedupPolicy=LAST_WIN` = keep last for duplicate map keys |
| Q74 | `inSetSwitchThreshold=10` → 11+ values use HashSet O(1) |
| **Q76** | **Answer A** — `spark.sql.parquet.compression.codec` |
| Q78 | Reduce `arrow.maxRecordsPerBatch` to lower peak memory in `toPandas()` |
| Q80 | `fallBackToHdfs=true` → `getContentSummary()` for size when no Hive stats |
| Q82 | Watermark bounds dedup state; late dupes after delay may not be caught |
| Q85 | Stream-static: static re-read each batch; no watermark/state needed |
| Q87 | RocksDB provider = off-heap state; avoids JVM GC for large state |
| Q90 | Kafka `startingOffsets` ignored if checkpoint exists |

#### Connect Hard (Q93, Q98)

| Q# | Must-know |
|---|---|
| Q93 | `./sbin/start-connect-server.sh --packages "..."` |
| Q98 | `ps.DataFrame.merge()` all join types; fully distributed (no driver collection) |

---

## Step 2 — Targeted Trap Drills

These are the most likely exam pitfalls. Drill each until automatic.

### Trap 1: Q76 is Answer A

Write it out 3 times: `spark.sql.parquet.compression.codec` → **Answer A**. Every other answer in this iteration is B. Q76 is the exception.

### Trap 2: `union` vs `unionByName` — Position vs Name (Q51 + Q70)

Both columns have `(a, b)` vs `(b, a)`:
- `union` → columns matched by **position** → silent wrong values
- `insertInto` → also by **position** — same trap in write context

Quick rule: **"ByName" = safe**

### Trap 3: `element_at` vs `[]` indexing (Q32, Q54)

| Access | Indexing |
|---|---|
| `F.element_at(arr, n)` | **1-based** — `1` = first, `-1` = last |
| `arr[n]` subscript | **0-based** |

### Trap 4: `bloomFilter` returns an object, not a DataFrame (Q47)

`df.stat.bloomFilter("col", n, fpp)` → `BloomFilter` object
- NOT a filtered DataFrame
- Serialize and use `mightContain(value)` in downstream jobs

### Trap 5: `from_json` schema for JSON arrays (Q66)

- JSON object `{}` → pass `StructType`
- JSON array `[{}, {}]` → **must** pass `ArrayType(StructType(...))`
- Passing wrong schema returns null rows silently

### Trap 6: `describe()` cannot compute percentiles (Q57, Q69)

- `df.describe()` → fixed: count, mean, stddev, min, max
- `df.summary("25%", "75%")` → flexible, supports any percentile

### Trap 7: `get_json_object` always StringType (Q28)

Even if the JSON value is a number like `42`, the result is the **string** `"42"`.
Use `F.from_json` with a schema to get typed values.

### Trap 8: `processAllAvailable()` is test-only (Q84)

In production, new data may keep arriving → this call could block forever.
Use `query.awaitTermination(timeoutMs)` in production.

### Trap 9: `startingOffsets` ignored with checkpoint (Q90)

On restart, Spark uses committed checkpoint offsets. `startingOffsets` only applies to the first (checkpointless) start. Delete checkpoint to replay.

### Trap 10: `psdf.explode()` preserves null/empty (Q100)

Pandas-on-Spark follows **pandas** semantics:
- null/empty → preserved as `NaN` row
- Different from `F.explode` which **drops** null/empty rows
- Same as `F.explode_outer`

---

## Step 3 — Version Awareness Drill

Many questions depend on knowing which Spark version introduced something. Quick recall:

| Version | Change |
|---|---|
| 3.0 | `df.transform(func)` added |
| 3.1 | `unionByName(allowMissingColumns=True)`, `writeStream.toTable()` |
| **3.2** | **AQE default = `true`** (major behaviour change), `minPartitionSize` added |
| 3.3 | `df.withColumns(dict)`, `df.withColumnsRenamed(dict)` |
| 3.4 | `df.unpivot()` / `df.melt()`, `F.try_element_at()` |

---

## Step 4 — Configuration Grouping Drill

Practise recalling configs by their category and default:

### Memory group
- `autoBroadcastJoinThreshold` = **10 MiB**
- `memory.fraction` = **0.6** | `memory.storageFraction` = **0.5**
- `io.compression.codec` = **lz4** | `parquet.compression.codec` = **snappy**

### AQE group (all default `true` in Spark 3.2+)
- `adaptive.enabled` | `coalescePartitions.enabled` | `localShuffleReader.enabled` | `exchange.reuse`

### Debugging group
- `debug.maxToStringFields` = **25** (fields in plan output)
- `repl.eagerEval.enabled` = **false** (auto HTML in Jupyter)
- `execution.arrow.maxRecordsPerBatch` = **10 000**

### Streaming group
- `streaming.numShufflePartitions` (streaming-only override)
- `stateStore.providerClass` (default = HDFSBacked; use RocksDB for large state)

### Spark Connect group
- `connect.grpc.binding.port` = **15002**

---

## Step 5 — Self-Assessment Targets

Before sitting the real exam, practise until you consistently hit these marks:

| Difficulty | Target score |
|---|---|
| Easy (Q1, 15, 21, 26, 30, 60, 69, 84, 91, 96) | 10/10 |
| Medium (54 questions) | ≥ 46/54 (85%) |
| Hard (36 questions) | ≥ 25/36 (70%) |
| **Overall** | **≥ 81/100 (81%)** |

If you're below target on medium questions, focus sessions on the subtopic group where you're weakest. If below target on hard questions, spend extra time on the trap drills in Step 2.

---

## Iteration 10 Connections to Other Iterations

These topics reinforce or extend material from previous iterations:

| Topic | Previous coverage | Iteration 10 addition |
|---|---|---|
| AQE | Iteration 6 (enabled/disabled) | Spark 3.2 default flip (Q71), localShuffleReader (Q20) |
| Broadcast joins | Iteration 5 (basics) | 10 MiB threshold default (Q1) |
| Union operations | Iteration 4 (basic union) | `allowMissingColumns` option (Q46), position vs name trap (Q51) |
| Streaming watermarks | Iteration 8 (aggregation) | dedup state bounding (Q82) |
| JSON functions | Iteration 7 (from_json/to_json) | `get_json_object` always StringType (Q28), ArrayType schema (Q66) |
| Parquet | Iteration 3 (basics) | Filter pushdown (Q12), mergeSchema (Q11), compression (Q76) |

---

## Final Checklist Before Exam

- [ ] Q76 answer is **A** — said out loud at least 3 times
- [ ] Can recall: `autoBroadcastJoinThreshold` = 10 MiB
- [ ] Can recall: AQE default = `true` from Spark 3.2
- [ ] Can recall: `union` = position; `unionByName` = name; `insertInto` = position
- [ ] Can recall: `describe()` = 5 stats; `summary()` = + percentiles
- [ ] Can recall: `element_at` = 1-based; `[]` = 0-based
- [ ] Can recall: `get_json_object` always returns StringType
- [ ] Can recall: `from_json` with JSON array → schema must be `ArrayType(...)`
- [ ] Can recall: `bloomFilter()` returns object, NOT a DataFrame
- [ ] Can recall: Connect default port = 15002
- [ ] Can recall: `startingOffsets` ignored when checkpoint exists
- [ ] Can recall: `psdf.explode()` preserves null/empty; `F.explode()` drops them
