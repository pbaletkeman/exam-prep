# Quick Reference — Databricks Spark Exam (Iteration 6)

> Condensed cheatsheet. Pair with `STUDY_GUIDE_ITER6.md` for full explanations.

---

## Exam Stats

| Metric | Value |
|--------|-------|
| Questions | 100 |
| Time | 90 minutes (~54 sec/question) |
| Pass threshold | ≈ 70% (70 correct) |
| Easy / Medium / Hard | 20 / 60 / 20 |
| Single-answer (`one`) | 73 |
| Multi-answer (`many`) | 20 |
| All-correct (`all`) | 5 |
| None-correct (`none`) | 2 |

---

## ⚠️ Iteration 6 Critical Alerts

1. **`all` type** — ALL four options correct (e.g., Q4 Barrier execution). Must select A, B, C, D.
2. **`none` type** — NONE of the options is correct. Watch for "none of the above" or plausible-but-all-wrong distractors.
3. **B-answer dominance** — Most single-select questions have B as the answer. Do NOT default to B without reasoning.
4. **"deflate" is NOT a valid Parquet codec** — answer D in Q65 (trick question).
5. **ANSI CAST failure** → exception, not NULL.
6. **`cardinality(NULL)` → NULL** / `size(NULL)` → −1.

---

## Topic Weight & Question Map

| Topic | Questions | Weight |
|-------|-----------|--------|
| 1 — Architecture & Internals | Q1–Q20 | 20% |
| 2 — Spark SQL | Q21–Q40 | 20% |
| 3 — DataFrame/Dataset API | Q41–Q70 | 30% |
| 4 — Troubleshooting & Tuning | Q71–Q80 | 10% |
| 5 — Structured Streaming | Q81–Q90 | 10% |
| 6 — Spark Connect | Q91–Q95 | 5% |
| 7 — Pandas API on Spark | Q96–Q100 | 5% |

---

## Topic 1 — Architecture Memory Anchors

```
RDD.cache()        → MEMORY_ONLY
DataFrame.cache()  → MEMORY_AND_DISK
coalesce(n)        → cannot increase, no shuffle, no-op if n≥current
repartition(n)     → can increase, always full shuffle

FIFO  → 1 job gets ALL slots      FAIR → slots shared across jobs

DAGScheduler → stages + TaskSets  TaskScheduler → tasks to executors

sc.parallelize(data, n) → n partitions
sc.parallelize(data)    → spark.default.parallelism partitions

deploy-mode cluster → spark-submit exits; driver on cluster
deploy-mode client  → spark-submit IS the driver

spark.driver.supervise → restart on crash; STANDALONE only (not YARN, not K8s)
spark.rdd.compress     → compress cached RDD partitions in memory
spark.eventLog.compress → compress event log (codec: eventLog.compression.codec, default zstd)

Barrier mode → all tasks start simultaneously; BarrierContext.allGather();
               any failure → full stage resubmit; MPI workloads

openCostInBytes → per-file padding for small file merging
```

---

## Topic 2 — Spark SQL Function Cheatsheet

### Return Types

| Function | Input | Returns | Notes |
|----------|-------|---------|-------|
| `split_part(s, d, n)` | String | String | 1-based position |
| `try_divide(a, b)` | Numeric | Same / NULL | NULL on div-by-zero |
| `try_add(a, b)` | Numeric | Same / NULL | NULL on overflow |
| `any_value(col IGNORE NULLS)` | Any | Same | Arbitrary non-null |
| `bool_and(col)` | Boolean | Boolean / NULL | Ignores NULLs |
| `bool_or(col)` | Boolean | Boolean / NULL | Ignores NULLs |
| `bit_or(col)` | Integer | Integer | `[5,3,8]` → 15 |
| `make_date(y,m,d)` | Int,Int,Int | DateType | NULL if invalid |
| `make_timestamp(...)` | Int × 6 | TimestampType | NULL if invalid |
| `unix_date(d)` | DateType | **IntegerType** | Days since epoch |
| `date_from_unix_date(n)` | Integer | DateType | Inverse of unix_date |
| `regexp_like(s, p)` | String | **BooleanType** | true/false |
| `regexp_extract(s, p, i)` | String | **StringType** | '' if no match |
| `regexp_count(s, p)` | String | Integer | Non-overlapping matches |
| `width_bucket(v, lo, hi, n)` | Numeric | Integer | 0=below, n+1=above |
| `array_compact(arr)` | Array | Array | Removes NULLs only |
| `startswith(s, p)` | String | BooleanType | NULL if either NULL |
| `inline(arr_of_structs)` | Array | Multiple rows | TGF; struct → columns |
| `named_struct('k',v,...)` | Mixed | StructType | Explicit field names |
| `struct(col1, col2)` | Cols | StructType | Column names as fields |
| `from_csv(s, schema)` | String | StructType | Flat only |
| `schema_of_csv(sample)` | String | **StringType DDL** | Not StructType object |
| `cardinality(col)` | Array/Map | Long / **NULL** | SQL-standard NULL |
| `size(col)` | Array/Map | Long / **-1** | Legacy NULL=-1 |
| `overlay(s, r, p, l)` | String | String | 1-based pos |
| `median(col)` | Numeric | Double | **Approximate** |
| `percentile_approx(c,0.5)` | Numeric | Double | Same as median |
| `date_diff / datediff(e,s)` | Date | IntegerType | Identical aliases |

### ANSI vs Non-ANSI CAST

| `spark.sql.ansi.enabled` | `CAST('abc' AS INT)` |
|--------------------------|----------------------|
| `false` (default) | Returns `NULL` |
| `true` | Raises `SparkNumberFormatException` |

---

## Topic 3 — DataFrame API Quick-Reference

### Struct Operations (Spark 3.1+)

```python
# Add/replace field in StructType column
df.withColumn("address", df["address"].withField("zip", F.lit("00000")))

# Remove field from StructType column
df.withColumn("profile", df["profile"].dropFields("ssn"))
```

### Higher-Order Functions

| HOF | Purpose | Key Behavior |
|-----|---------|--------------|
| `transform(arr, f)` | Map over array | Returns same-length array |
| `filter(arr, pred)` | Filter array | Returns shorter array |
| `aggregate(arr, zero, merge, finish?)` | Fold/reduce | 4th arg optional |
| `zip_with(a1, a2, f)` | Pairwise merge | Element-wise; same length |
| `forall(arr, pred)` | All elements match | false if ANY fails |
| `exists(arr, pred)` | Any element matches | true if ANY passes |
| `flatten(arr)` | Flatten nested array | `[[1,2],[3]]` → `[1,2,3]` |
| `transform_keys(map, f)` | Transform map keys | Keys changed; values same |
| `transform_values(map, f)` | Transform map values | Values changed; keys same |
| `map_zip_with(m1, m2, f)` | Merge two maps | Per-key merge function |

### Key Method Behaviors

| Method | Key Fact |
|--------|----------|
| `df.tail(n)` | LAST n rows (not first) |
| `df.dtypes` | List of `(name, type_str)` tuples |
| `df.inputFiles()` | List of absolute input file paths |
| `df.sampleBy(col, fractions)` | Keys not in fractions → EXCLUDED |
| `df.checkpoint(eager=True)` | Immediate write; eager=False defers |
| `df.to(schema)` | Match by name + auto-cast; raises if col missing |
| `df.observe(obs, *exprs)` | Inline metrics; no extra job |
| `df.crossJoin(df2)` | Cartesian product; requires crossJoin.enabled |
| `writeTo().createOrReplace()` | Drop + recreate table |
| `writeTo().append()` | Add without removing data |
| `write.bucketBy().saveAsTable()` | ONLY saveAsTable; path-based fails |
| `partitionBy()` | No auto-coalesce; files per leaf = DF partitions with that key |
| `array_insert(arr, pos, val)` | 1-based; inserts BEFORE current element at pos |
| `try_element_at(col, idx)` | NULL if OOB (not exception) |
| `array_remove(col, val)` | Removes ALL occurrences of val |
| `array_distinct(col)` | Keeps FIRST occurrence of each distinct value |
| `current_timestamp()` | Non-deterministic; same value for all rows within one execution |

### Parquet Compression Codecs

| Valid | Invalid |
|-------|---------|
| `snappy`, `gzip`, `brotli`, `lz4`, `zstd`, `uncompressed` | **`deflate`** ← NOT valid |

---

## Topic 4 — Tuning Quick-Reference

| Config | Default | Effect |
|--------|---------|--------|
| `spark.sql.files.maxPartitionBytes` | 128 MB | Max input partition size |
| `spark.sql.files.openCostInBytes` | 4 MB | Per-file padding for small file merge |
| `spark.sql.adaptive.skewJoin.enabled` | true | AQE skew join sub-partitioning |
| `spark.sql.adaptive.coalescePartitions.parallelismFirst` | true | true=ignore minPartitionNum; false=respect it |
| `spark.sql.codegen.maxFields` | 100 | Fields > this → codegen disabled |
| `spark.shuffle.file.buffer` | 32k | Write buffer per shuffle output stream |
| `spark.sql.execution.sortBeforeRepartition` | true | Sort by hash before repartition write |
| `spark.sql.files.ignoreMissingFiles` | false | true=skip missing files; false=raise exception |
| `spark.kryo.registrationRequired` | false | true=KryoException on unregistered class |
| `spark.memory.offHeap.enabled` | false | Enable off-heap Tungsten memory |
| `spark.memory.offHeap.size` | 0 | Per-executor off-heap budget (extra to executor.memory) |
| `arrow.pyspark.selfDestruct.enabled` | false | Free Arrow buffers after toPandas() copy |

### Off-Heap Memory Facts

```
✅ Outside JVM heap → not GC'd
✅ offHeap.size is per-executor ADDITIONAL to spark.executor.memory
✅ Used by Tungsten + explicit OFF_HEAP storage level
❌ Does NOT automatically disable on-heap caching
```

---

## Topic 5 — Streaming Quick-Reference

### Triggers

| Trigger | Batches until stop |
|---------|-------------------|
| `trigger(once=True)` | 1 (one mega-batch) |
| `trigger(availableNow=True)` | Multiple (rate-limited) |
| `trigger(processingTime="10 seconds")` | Continuous |
| `trigger(continuous="1 second")` | Epoch-based |

### Kafka Source Fixed Schema

```
key           BinaryType   ← decode yourself
value         BinaryType   ← decode yourself
topic         StringType
partition     IntegerType
offset        LongType
timestamp     TimestampType
timestampType IntegerType
```

### Watermark Drop Threshold

```
drop_threshold = max_event_time - delay
event.event_time > drop_threshold → NOT dropped → appended
event.event_time ≤ drop_threshold → dropped (late data)
```

### State Operators

| Operator | Rows emitted per group per trigger |
|----------|-----------------------------------|
| `mapGroupsWithState` | Exactly 1 |
| `flatMapGroupsWithState` | 0 or more (Iterator) |

---

## Topic 6 — Spark Connect Quick-Reference

```
sc://host:port/;token=<value>     ← token placement in URL

Classic PySpark: local JVM (Py4J) required
Spark Connect: no local JVM; gRPC stub → remote server

AnalysisException timing:
  Classic → at transformation
  Connect → at ACTION time

Server crash: client Python SURVIVES (reconnect + resubmit possible)
UDFs: pickled on client → gRPC plan → deserialized on executor
```

---

## Topic 7 — Pandas API Quick-Reference

```
psdf.spark.cache()            → MEMORY_AND_DISK
psdf.spark.explain(extended=True) → logical + physical plans
psdf.to_delta(path)           → write to Delta Lake
psdf.to_spark()               → convert to Spark DataFrame

Index types:
  "distributed"          FASTEST; non-contiguous; monotonically_increasing_id()
  "distributed-sequence" SLOWEST; 0-based contiguous; requires global sort

NULL vs NaN in float columns:
  fillna(0)  → fills NULL only; NaN unchanged
  dropna()   → drops NULL rows; NaN may not be dropped
  sum([1.0, NaN, 2.0]) → NaN (propagates through arithmetic)
  sum([1.0, NULL, 2.0]) → 3.0 (NULL ignored by SQL aggregations)
```

---

## Complete Answer Key — Q1 to Q100

```
Q1:B   Q2:B   Q3:B   Q4:ABCD  Q5:B
Q6:B   Q7:B   Q8:ABD  Q9:B   Q10:B
Q11:B  Q12:A  Q13:B  Q14:B   Q15:ABC
Q16:B  Q17:B  Q18:B  Q19:B   Q20:ABC
Q21:B  Q22:B  Q23:B  Q24:B   Q25:B
Q26:B  Q27:B  Q28:B  Q29:A   Q30:A
Q31:B  Q32:B  Q33:B  Q34:B   Q35:B
Q36:B  Q37:B  Q38:B  Q39:B   Q40:B
Q41:B  Q42:B  Q43:B  Q44:A   Q45:A
Q46:B  Q47:B  Q48:A  Q49:A   Q50:B
Q51:B  Q52:B  Q53:B  Q54:A   Q55:B
Q56:B  Q57:B  Q58:A  Q59:B   Q60:ABC
Q61:B  Q62:B  Q63:B  Q64:A   Q65:D
Q66:B  Q67:A  Q68:B  Q69:ABD  Q70:C
Q71:B  Q72:B  Q73:ABC Q74:A  Q75:B
Q76:B  Q77:B  Q78:ABD Q79:C  Q80:B
Q81:B  Q82:B  Q83:B  Q84:B   Q85:B
Q86:B  Q87:B  Q88:B  Q89:B   Q90:B
Q91:B  Q92:B  Q93:B  Q94:B   Q95:B
Q96:B  Q97:B  Q98:B  Q99:B   Q100:ACD
```

### Answer Distribution Summary

| Answer | Count |
|--------|-------|
| A only | 12 (Q12, Q29, Q30, Q44, Q45, Q48, Q49, Q54, Q58, Q64, Q67, Q74) |
| B only | 73 approx |
| C only | 2 (Q70, Q79) |
| D only | 1 (Q65) |
| Multi (A,B,C,D) | 1 (Q4) |
| Multi (A,B,D) | 3 (Q8, Q69, Q78) |
| Multi (A,B,C) | 2 (Q15, Q20, Q60, Q73 — 4 total) |
| Multi (A,C,D) | 1 (Q100) |

---

## Grid View Answer Key (10×10)

```
     1    2    3    4    5    6    7    8    9    10
1: [ B  ][ B  ][ B  ][ABCD][ B  ][ B  ][ B  ][ABD ][ B  ][ B  ]
2: [ B  ][ A  ][ B  ][ B  ][ABC ][ B  ][ B  ][ B  ][ B  ][ABC ]
3: [ B  ][ B  ][ B  ][ B  ][ B  ][ B  ][ B  ][ B  ][ A  ][ A  ]
4: [ B  ][ B  ][ B  ][ B  ][ B  ][ B  ][ B  ][ B  ][ B  ][ B  ]
5: [ B  ][ B  ][ B  ][ A  ][ A  ][ B  ][ B  ][ A  ][ A  ][ B  ]
6: [ B  ][ B  ][ B  ][ A  ][ B  ][ B  ][ B  ][ A  ][ B  ][ABC ]
7: [ B  ][ B  ][ B  ][ A  ][ B  ][ B  ][ A  ][ B  ][ABD ][ C  ]
8: [ B  ][ B  ][ABC ][ A  ][ B  ][ B  ][ B  ][ABD ][ C  ][ B  ]
9: [ B  ][ B  ][ B  ][ B  ][ B  ][ B  ][ B  ][ B  ][ B  ][ B  ]
10:[ B  ][ B  ][ B  ][ B  ][ B  ][ B  ][ B  ][ B  ][ B  ][ACD ]
```
*(Row = tens digit, Col = ones digit. Row 1 = Q1–Q10; Row 2 = Q11–Q20; etc.)*

---

## Exam Day Decision Tree

```
Question received
    │
    ├─ Identify answer type: one / many / all / none
    │       └─ Multi-select: read ALL options before selecting ANY
    │
    ├─ Identify topic from keywords
    │       Architecture → storage levels, scheduling, DAG, memory
    │       SQL → function return types, NULL handling, ANSI mode
    │       DataFrame → HOFs, struct ops, write modes, array functions
    │       Tuning → AQE, codegen, partitioning, off-heap
    │       Streaming → triggers, schema, watermark, Kafka
    │       Connect → timing, URL, no-JVM, crash behavior
    │       Pandas API → NULL/NaN, index types, explain/cache
    │
    ├─ Check for known traps
    │       "deflate" → always wrong (Parquet codec)
    │       "coalesce increases partitions" → always wrong
    │       "cardinality(NULL) = -1" → wrong (that's size())
    │       "ANSI CAST returns NULL" → wrong (raises exception)
    │       "trigger(once) = multiple batches" → wrong (1 batch only)
    │       "client Python dies on server crash" → wrong (client survives)
    │
    ├─ B is dominant but not universal — verify before selecting
    │       Non-B correct answers: Q12(A), Q29(A), Q30(A), Q44(A),
    │       Q45(A), Q48(A), Q49(A), Q54(A), Q58(A), Q64(A), Q67(A),
    │       Q74(A), Q65(D), Q70(C), Q79(C), multi-select questions
    │
    └─ Time check: 90 min ÷ 100 Q = 54 sec avg
            Easy questions → target 30 sec
            Hard questions → cap at 90 sec; mark and return
```

---

## Critical Config Defaults (Exam-Relevant)

| Config | Default | What changes if you flip it |
|--------|---------|----------------------------|
| `spark.sql.ansi.enabled` | `false` | Invalid CAST → exception (not NULL) |
| `spark.sql.legacy.sizeOfNull` | `false` | size(NULL) → NULL (not -1) |
| `spark.sql.crossJoin.enabled` | `false` | crossJoin() requires explicit enable |
| `spark.sql.adaptive.enabled` | `true` | AQE active |
| `spark.sql.adaptive.skewJoin.enabled` | `true` | AQE skew join active |
| `spark.sql.adaptive.coalescePartitions.parallelismFirst` | `true` | Ignores minPartitionNum |
| `spark.sql.codegen.wholeStage` | `true` | Fused operators |
| `spark.sql.codegen.maxFields` | `100` | Auto-disables codegen when exceeded |
| `spark.sql.files.ignoreMissingFiles` | `false` | FileNotFoundException on missing file |
| `spark.sql.files.maxPartitionBytes` | `128 MB` | Max input partition size |
| `spark.sql.files.openCostInBytes` | `4 MB` | Small file merging padding |
| `spark.shuffle.file.buffer` | `32k` | Write buffer per shuffle output |
| `spark.storage.replication.proactive` | `false` | Proactive replica replenishment |
| `spark.kryo.registrationRequired` | `false` | KryoException on unregistered class |
| `spark.executor.pyspark.memory` | unset | Unbounded Python worker memory |
| `spark.dynamicAllocation.shuffleTracking.enabled` | `true` | DRA without external shuffle service |
