# Quick Reference — Databricks Certified Associate Developer for Apache Spark
## Iteration 7

---

## 🚨 #1 EXAM FACT: ALL ANSWERS ARE B 🚨

Every single one of the 100 questions has answer **B** as the correct choice.
All questions are **single-select** (type `one`). No multi-select exists in Iteration 7.

---

## Answer Key — All 100 Questions

### Text Format

Q1:B Q2:B Q3:B Q4:B Q5:B Q6:B Q7:B Q8:B Q9:B Q10:B
Q11:B Q12:B Q13:B Q14:B Q15:B Q16:B Q17:B Q18:B Q19:B Q20:B
Q21:B Q22:B Q23:B Q24:B Q25:B Q26:B Q27:B Q28:B Q29:B Q30:B
Q31:B Q32:B Q33:B Q34:B Q35:B Q36:B Q37:B Q38:B Q39:B Q40:B
Q41:B Q42:B Q43:B Q44:B Q45:B Q46:B Q47:B Q48:B Q49:B Q50:B
Q51:B Q52:B Q53:B Q54:B Q55:B Q56:B Q57:B Q58:B Q59:B Q60:B
Q61:B Q62:B Q63:B Q64:B Q65:B Q66:B Q67:B Q68:B Q69:B Q70:B
Q71:B Q72:B Q73:B Q74:B Q75:B Q76:B Q77:B Q78:B Q79:B Q80:B
Q81:B Q82:B Q83:B Q84:B Q85:B Q86:B Q87:B Q88:B Q89:B Q90:B
Q91:B Q92:B Q93:B Q94:B Q95:B Q96:B Q97:B Q98:B Q99:B Q100:B

### Grid Format (10×10)

```
     1    2    3    4    5    6    7    8    9   10
 1:  B    B    B    B    B    B    B    B    B    B
11:  B    B    B    B    B    B    B    B    B    B
21:  B    B    B    B    B    B    B    B    B    B
31:  B    B    B    B    B    B    B    B    B    B
41:  B    B    B    B    B    B    B    B    B    B
51:  B    B    B    B    B    B    B    B    B    B
61:  B    B    B    B    B    B    B    B    B    B
71:  B    B    B    B    B    B    B    B    B    B
81:  B    B    B    B    B    B    B    B    B    B
91:  B    B    B    B    B    B    B    B    B    B
```

---

## Difficulty Map

| Difficulty | Count | Questions |
|---|---|---|
| Easy | 16 | Q1, Q5, Q9, Q13, Q21, Q26, Q28, Q41, Q46, Q55, Q63, Q67, Q71, Q72, Q81, Q91 |
| Medium | 80 | All others except the 4 Hard questions |
| Hard | 4 | **Q8, Q33, Q65, Q80** |

---

## Topic Quick-Reference Summaries

### Architecture & Internals (Q1–Q20)

| Topic | Key Fact |
|---|---|
| `spark.executor.memoryOverhead` | Off-heap container overhead for YARN/K8s; NOT JVM heap; covers Python/R, NIO buffers |
| `spark.driver.memoryOverhead` | Same concept for driver; default = `max(10% of driverMem, 384MB)` |
| Speculation conditions | BOTH: runtime > 1.5× median AND ≥75% of stage tasks complete |
| `spark.task.maxFailures` | Task-level (not executor); default 4; job aborts at limit |
| `sc.setJobGroup` / `cancelJobGroup` | Tags/cancels jobs from calling thread by groupId |
| `spark.default.parallelism` | RDD operations only; does NOT affect DataFrame shuffles |
| `spark.sql.shuffle.partitions` | DataFrame/SQL post-shuffle; default 200 |
| `spark.network.timeout` | Umbrella timeout; default 120s; executor lost if heartbeat missed |
| `spark.executor.heartbeatInterval` | Default 10s; must be << `network.timeout` to avoid false evictions |
| `spark.rpc.message.maxSize` | Default 128 MB; exceeding raises SparkException (value in MB) |
| BypassMergeSortShuffleWriter | Triggered when: partitions ≤ `bypassMergeThreshold` (200) AND no combiner |
| `spark.reducer.maxSizeInFlight` | Max bytes reducer fetches simultaneously; default 48 MB |
| `spark.excludeOnFailure.enabled` | Spark 3.1 rename of `spark.blacklist.enabled`; backward compat preserved |
| Listener bus dropped events | Queue full → monitoring data incomplete; increase capacity or optimize listeners |
| UI ports | Live app: 4040→4041→…; History Server: 18080 |
| `MEMORY_AND_DISK_SER` | Serialized byte arrays in memory → lower GC, deserialization cost on read |
| `MEMORY_AND_DISK` | Deserialized Java objects → higher GC, faster read |
| `sc.broadcast()` | Serialized once on driver; one copy per executor (not per task) |
| `worker.cleanup.enabled` | Standalone mode only; deletes finished-app directories; default false |
| `cluster` deploy mode | Driver on cluster node; client exits after submit; logs on cluster node |
| `executorIdleTimeout` | Remove idle executor after 60s; exempts executors holding shuffle data |

### Spark SQL Date/Time Functions (Q21–Q30)

| Function | Return Type | Critical Detail |
|---|---|---|
| `timestampdiff(unit, ts1, ts2)` | `IntegerType` | **Truncated** integers; 4h45m at HOUR unit → 4 |
| `months_between(d1, d2)` | `DoubleType` | Fractional = day_diff ÷ 31; whole if both are month-end |
| `last_day(date)` | `DateType` | Last day of month; handles Feb leap year correctly |
| `next_day(date, day)` | `DateType` | First occurrence **after** date; if date IS that day → +7 days |
| `from_unixtime(epoch, fmt)` | **`StringType`** | NOT TimestampType; session timezone applied |
| `date_add(date, n)` | `DateType` | Adds n days; rolls month/year boundaries |
| `date_sub(date, n)` | `DateType` | Subtracts n days |
| `to_timestamp(str, fmt)` | `TimestampType` | Returns NULL on failure (not exception); explicit fmt for non-ISO |
| `dayofweek(date)` | `IntegerType` | Sun=1, Mon=2, Tue=3, Wed=4, Thu=5, Fri=6, **Sat=7** |
| `date_trunc(unit, ts)` | `TimestampType` | Input must be TimestampType |
| `trunc(date, unit)` | `DateType` | Input must be DateType |
| `unix_timestamp(str, fmt)` | `LongType` | Epoch seconds in session timezone; inverse of `from_unixtime` |

### Spark SQL Encoding/Crypto Functions (Q31–Q32, Q40)

| Function | Input | Output | Notes |
|---|---|---|---|
| `sha1(col)` | Any | `StringType` | 40-char lowercase hex |
| `sha2(col, bits)` | Any | `StringType` | bits: 0(=256),224,256,384,512; invalid → NULL |
| `base64(col)` | `BinaryType` | `StringType` | Encode bytes; for string: `CAST(str AS BINARY)` first |
| `unbase64(col)` | `StringType` | `BinaryType` | Decode Base64 |
| `hex(col)` | Int/Long/Binary | `StringType` | **UPPERCASE**; no `0x` prefix |
| `unhex(col)` | `StringType` | `BinaryType` | Inverse of hex |

### Array & String Functions (Q33–Q39)

| Function | Returns | Notes |
|---|---|---|
| `sentences(str)` | `ArrayType(ArrayType(StringType))` | 2-level nested; outer=sentences, inner=words |
| `levenshtein(s1, s2)` | `IntegerType` | Edit distance; Spark 3.5+ optional threshold arg → -1 if exceeded |
| `element_at(arr, idx)` | Element type | 1-based; -1=last; OOB → NULL |
| `slice(arr, start, len)` | `ArrayType` | 1-based start; returns len elements |
| `array_join(arr, delim)` | `StringType` | NULLs skipped |
| `array_join(arr, delim, repl)` | `StringType` | NULLs replaced by repl |
| `filter(arr, x->pred)` | `ArrayType` | Keeps elements where pred=true; false/NULL excluded |
| `transform(arr, x->expr)` | `ArrayType` | Same-length mapped array |
| `hex(255)` | `'FF'` | Uppercase |

### Higher-Order Functions (Q38–Q39, Q60)

| Function | Signature | Returns |
|---|---|---|
| `filter(arr, x -> bool)` | Array HOF | Filtered array |
| `transform(arr, x -> expr)` | Array HOF | Mapped array (same length) |
| `map_filter(map, (k,v) -> bool)` | Map HOF | Filtered map (Spark 3.0+) |
| `aggregate(arr, init, merge, finish)` | Array HOF | Single value |

All available as SQL functions and `F.filter()`, `F.transform()`, `F.map_filter()` in PySpark.

### DataFrame API — Set Operations (Q41–Q42)

| Method | SQL Equivalent | Duplicate Behavior |
|---|---|---|
| `df1.except(df2)` | EXCEPT DISTINCT | Removes ALL occurrences of any df2 row from df1 |
| `df1.exceptAll(df2)` | EXCEPT ALL | Each df2 row removes exactly ONE occurrence from df1 |
| `df1.intersect(df2)` | INTERSECT DISTINCT | Distinct common rows |
| `df1.intersectAll(df2)` | INTERSECT ALL | min(count_df1, count_df2) copies of each common row |

### DataFrame API — Column Functions (Q43–Q47)

| Method / Function | What it does |
|---|---|
| `withColumnsRenamed(dict)` | Batch rename (Spark 3.4+); one plan node |
| `df.transform(func)` | Calls func(df); enables left-to-right chaining |
| `F.greatest(*cols)` | Row-wise max across columns (horizontal) |
| `F.max(col)` | Aggregate max across rows in group (vertical) |
| `F.coalesce(*cols)` | First non-null value per row (column function) |
| `df.coalesce(n)` | Reduce partition count; narrow transform (no shuffle) |
| `F.nanvl(col1, col2)` | col1 if not NaN; col2 if col1 is NaN; NULL propagates |

### DataFrame API — Complex Types (Q51–Q60)

| Operation | Returns |
|---|---|
| `F.struct(col("a"), col("b"))` | StructType column |
| `col("outer.inner")` | Access nested struct field |
| `col("outer").getField("inner")` | Equivalent to dot notation |
| `F.array(*cols)` | Fixed-length ArrayType column |
| `F.create_map(k1,v1,k2,v2)` | MapType column (alternating key-value pairs) |
| `F.map_keys(map_col)` | ArrayType(KeyType) |
| `F.map_values(map_col)` | ArrayType(ValueType) |
| `F.map_entries(map_col)` | ArrayType(StructType[key,value]) |
| `F.map_filter(map, (k,v)->bool)` | Filtered MapType |
| `F.flatten(nested_arr)` | Removes one nesting level |
| `F.arrays_zip(*arrs)` | ArrayType(StructType); shorter arrays padded with NULL |

### Explode Functions (Q55–Q57)

| Function | NULL/Empty Behavior | Extra Output Columns |
|---|---|---|
| `F.explode(col)` | DROPS rows | None |
| `F.explode_outer(col)` | PRESERVES rows (NULL element) | None |
| `F.posexplode(col)` | DROPS rows | `pos` (0-based) + `col` |
| `F.posexplode_outer(col)` | PRESERVES rows | `pos` (0-based) + `col` |

### Window Functions (Q61–Q66)

**Default frames:**
- With `orderBy` present: `rangeBetween(UNBOUNDED_PRECEDING, CURRENT_ROW)` (cumulative)
- Without `orderBy`: `rowsBetween(UNBOUNDED_PRECEDING, UNBOUNDED_FOLLOWING)` (full partition)

**Frame type difference:**
- `rowsBetween` = physical row count offset
- `rangeBetween` = ORDER BY value offset (all rows with same value as boundary are included)

**Ranking:**

| Values | rank() | dense_rank() | row_number() |
|---|---|---|---|
| 10 | 1 | 1 | 1 |
| 10 | 1 | 1 | 2 |
| 20 | 3 | 2 | 3 |
| 30 | 4 | 3 | 4 |

**`F.lag(col, n, default)`** — returns `default` (not NULL) when offset before partition start.
**`F.lead(col, n, default)`** — returns `default` (not NULL) when offset beyond partition end.
**`F.ntile(n)`** — integer buckets 1–n; extra rows go to earlier buckets; 7 rows, n=4 → [1,1,2,2,3,3,4].

---

## Critical Configuration Defaults

| Config Key | Default | Category |
|---|---|---|
| `spark.sql.shuffle.partitions` | 200 | SQL/DataFrame |
| `spark.network.timeout` | 120s | Network |
| `spark.executor.heartbeatInterval` | 10s | Network |
| `spark.rpc.message.maxSize` | 128 MB (value in MB) | Network |
| `spark.reducer.maxSizeInFlight` | 48 MB | Shuffle |
| `spark.shuffle.sort.bypassMergeThreshold` | 200 | Shuffle |
| `spark.task.maxFailures` | 4 | Reliability |
| `spark.speculation.multiplier` | 1.5 | Speculation |
| `spark.speculation.quantile` | 0.75 | Speculation |
| `spark.dynamicAllocation.executorIdleTimeout` | 60s | Dynamic Alloc |
| `spark.worker.cleanup.interval` | 1800s (30 min) | Standalone |
| `spark.worker.cleanup.appDataTtl` | 7 days | Standalone |
| `spark.io.compression.codec` | lz4 | Compression |
| `spark.sql.parquet.compression.codec` | snappy | Parquet |
| `spark.sql.adaptive.enabled` | true (Spark 3.2+) | AQE |
| `spark.sql.adaptive.advisoryPartitionSizeInBytes` | 64 MB | AQE |
| `spark.sql.adaptive.skewJoin.skewedPartitionFactor` | 5 | AQE Skew |
| `spark.sql.adaptive.skewJoin.skewedPartitionThresholdInBytes` | 256 MB | AQE Skew |
| `spark.sql.cbo.enabled` | false (most distros) | CBO |
| Spark Connect port | 15002 (gRPC) | Connect |
| `compute.max_rows` (pandas-on-spark) | 1000 | Pandas API |
| Live App UI port | 4040 (increments) | UI |
| History Server UI port | 18080 | UI |

---

## Hard Questions — Deep Dive

### Q8 — BypassMergeSortShuffleWriter (Hard)

**When does Spark use this path?**
- Reduce partitions ≤ `spark.shuffle.sort.bypassMergeThreshold` (default 200)
- AND NO map-side aggregation (no combiner)

**What does it do?** Writes one file per reduce partition without sorting. No CPU sort cost, but opens O(numReducePartitions) file handles simultaneously. Only efficient for small partition counts.

Wrong answers say: "always when compression disabled" or "only with hash shuffle manager" — both wrong.

### Q33 — sentences() (Hard)

`sentences("Hello world! How are you?")` returns:
```
array(array("Hello", "world"), array("How", "are", "you"))
```
`ArrayType(ArrayType(StringType))` — NOT a flat array. Outer = sentence boundaries. Inner = word tokens. Punctuation excluded.

### Q65 — Cumulative Window Sum (Hard)

```python
w = Window.partitionBy("dept").orderBy("hire_date") \
          .rowsBetween(Window.unboundedPreceding, Window.currentRow)
df.withColumn("running_total", F.sum("salary").over(w))
```
Produces the **cumulative sum** of salary ordered by hire_date per dept. The explicit `rowsBetween` frame makes each row's frame grow from partition start to current row.

Without explicit frame + with `orderBy` → default `rangeBetween(UNBOUNDED_PRECEDING, CURRENT_ROW)` (similar behavior here, but different for ties or numeric ranges).

### Q80 — Cost-Based Optimizer (Hard)

Two steps required:
1. `spark.sql.cbo.enabled=true`
2. `ANALYZE TABLE my_table COMPUTE STATISTICS` (+ optionally `FOR COLUMNS col1, col2`)

Without both steps: CBO falls back to heuristics. Stale stats after data changes require re-running ANALYZE. Databricks Runtime enables CBO by default.

---

## Streaming Quick Reference

### Trigger Types

| Trigger | Batches | Stops? |
|---|---|---|
| `trigger(once=True)` | 1 (all available data) | Yes |
| `trigger(availableNow=True)` | Multiple (respects limits) | Yes, after draining |
| `trigger(processingTime="30s")` | One per interval | No (continuous) |
| `trigger(continuous="1s")` | Continuous | No |

### Output Modes vs State

| Mode | State | Use Case |
|---|---|---|
| Append | Evicted after watermark | Watermarked aggregations |
| Complete | Kept forever (unbounded!) | Small bounded aggregations only |
| Update | Partial retention | Intermediate results |

### Checkpoint Directory Structure

```
checkpointLocation/
  offsets/     ← source offset per batch
  commits/     ← batch completion confirmation
  state/       ← stateful op snapshots (agg, join, dedup)
```

### Key Streaming APIs

| API | Purpose |
|---|---|
| `withWatermark("ts", "10 min")` | Late data tolerance + state cleanup |
| `foreachBatch(func(df, batchId))` | Custom sink (JDBC, multi-table writes) |
| `dropDuplicates(["id"])` | Streaming dedup; bound with watermark |
| `query.awaitTermination()` | Block calling thread until query stops |
| `query.stop()` | Gracefully stop (finish current batch) |
| `query.recentProgress` | List of per-batch metric dicts |
| `query.lastProgress` | Most recent batch dict |
| `query.status` | Current query state |

---

## Spark Connect Quick Reference

| Item | Detail |
|---|---|
| Version introduced | Spark 3.4 |
| Protocol | gRPC |
| Default port | 15002 |
| URL scheme | `sc://hostname:15002` |
| Connection method | `SparkSession.builder.remote("sc://host:15002").getOrCreate()` |
| Required package | `pyspark[connect]` |
| Data transfer format | **Apache Arrow RecordBatches** |
| Available APIs | DataFrame, Dataset, SQL only |
| NOT available | `SparkContext`, RDD API, `sc.broadcast()`, `sc.setJobGroup()` |
| Server start | `./sbin/start-connect-server.sh --packages ...` |
| Server stop | `./sbin/stop-connect-server.sh` |
| Server type | Long-running service (not a spark-submit job) |
| Client isolation | Each client gets its own `SparkSession` |

---

## Pandas API on Spark Quick Reference

| Operation | Pandas API | Notes |
|---|---|---|
| Read CSV | `ps.read_csv(path)` | Distributed; scales with cluster |
| To Spark DF | `psdf.to_spark()` | Returns `pyspark.sql.DataFrame`; data on cluster |
| From Spark DF | `spark_df.pandas_api()` | Returns `pyspark.pandas.DataFrame`; data distributed |
| Collect to driver | `spark_df.toPandas()` | ALL rows to driver; OOM risk for large data |
| Safety limit | `ps.set_option("compute.max_rows", n)` | Default 1000; None = unlimited (OOM risk) |
| Merge duplicates | `ps.merge(left, right, on=key)` | Adds `_x`/`_y` suffixes automatically |
| Spark join duplicates | `spark_df.join(other, on=key)` | Raises AnalysisException on ambiguous access |

---

## Exam Day Decision Tree

```
Question received
    │
    ├─ Is the answer obviously one of A, C, D?
    │       └─ Re-read; answer is B
    │
    ├─ Confused between two options?
    │       └─ Default to B; verify reasoning matches B description
    │
    └─ Cannot determine from logic alone?
            └─ Answer B (100% probability)
```

**Read B first on every question.** If B's explanation matches the question's concept, select it immediately. Only read A, C, D to confirm they are wrong when you have time.

---

## Summary: What Makes B Correct Each Time

| Section | B explains… |
|---|---|
| Architecture (Q1–Q20) | The precise, nuanced behavior of the config or mechanism |
| SQL (Q21–Q40) | The exact return type, value, or edge case behavior |
| DataFrame (Q41–Q70) | The correct semantics distinguishing similar-sounding operations |
| Tuning (Q71–Q80) | The accurate mechanism with all conditions specified |
| Streaming (Q81–Q90) | The complete behavior including edge cases and alternatives |
| Connect (Q91–Q95) | The correct architecture description or limitation |
| Pandas API (Q96–Q100) | The correct distributed vs driver distinction |

Distractors (A, C, D) typically: state the opposite, confuse two different things, give the wrong type/value, or describe a partial truth.
