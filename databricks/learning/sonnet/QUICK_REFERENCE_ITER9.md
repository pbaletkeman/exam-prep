# Quick Reference — Iteration 9
## Databricks Certified Associate Developer for Apache Spark

---

## ⚠️ CRITICAL WARNING — Answer Distribution

> **Iteration 9 uses THREE answer options.** Do not assume all B!
>
> | Option | Count | Questions |
> |---|---|---|
> | **B** | 89 | All except the 11 below |
> | **A** | 8 | Q15, Q31, Q33, Q41, Q45, Q56, Q83, Q85 |
> | **C** | 3 | Q1, Q3, Q4 |

---

## Full Answer Grid (10×10)

```
     Q1  Q2  Q3  Q4  Q5  Q6  Q7  Q8  Q9  Q10
     C   B   C   C   B   B   B   B   B   B

     Q11 Q12 Q13 Q14 Q15 Q16 Q17 Q18 Q19 Q20
     B   B   B   B   A   B   B   B   B   B

     Q21 Q22 Q23 Q24 Q25 Q26 Q27 Q28 Q29 Q30
     B   B   B   B   B   B   B   B   B   B

     Q31 Q32 Q33 Q34 Q35 Q36 Q37 Q38 Q39 Q40
     A   B   A   B   B   B   B   B   B   B

     Q41 Q42 Q43 Q44 Q45 Q46 Q47 Q48 Q49 Q50
     A   B   B   B   A   B   B   B   B   B

     Q51 Q52 Q53 Q54 Q55 Q56 Q57 Q58 Q59 Q60
     B   B   B   B   B   A   B   B   B   B

     Q61 Q62 Q63 Q64 Q65 Q66 Q67 Q68 Q69 Q70
     B   B   B   B   B   B   B   B   B   B

     Q71 Q72 Q73 Q74 Q75 Q76 Q77 Q78 Q79 Q80
     B   B   B   B   B   B   B   B   B   B

     Q81 Q82 Q83 Q84 Q85 Q86 Q87 Q88 Q89 Q90
     B   B   A   B   A   B   B   B   B   B

     Q91 Q92 Q93 Q94 Q95 Q96 Q97 Q98 Q99 Q100
     B   B   B   B   B   B   B   B   B   B
```

---

## Non-B Answer Explanations (Why A or C, Not B)

### C Answers (Q1, Q3, Q4) — ALL in Architecture Topic

| Q# | Answer | One-line reason |
|---|---|---|
| Q1 | **C** | SparkSession **wraps** SparkContext; access via `spark.sparkContext` |
| Q3 | **C** | YARN total = heap(4GB) + overhead(512MB) + offHeap(1GB) = **5.5 GB** |
| Q4 | **C** | Two wide transforms (groupByKey + join) = **3 stages**, not 2 |

### A Answers (Q15, Q31, Q33, Q41, Q45, Q56, Q83, Q85)

| Q# | Answer | One-line reason |
|---|---|---|
| Q15 | **A** | `shuffle.compress` = output block files; `spill.compress` = intermediate spill files |
| Q31 | **A** | `reduce(arr, 0, (acc,x)->acc+x)` = 10; optional 4th `finish` arg transforms final accumulator |
| Q33 | **A** | `start_date + make_interval(1, 6)` adds 1 year 6 months; option A shows correct syntax |
| Q41 | **A** | `withMetadata` → access via `df.schema["col"].metadata`; data unchanged |
| Q45 | **A** | `collect_list` with default orderBy frame → running list `['login','click','purchase']` at row 3 |
| Q56 | **A** | `F.lit(None)` creates NullType; Parquet rejects it; fix: `.cast("string")` |
| Q83 | **A** | Shared checkpoint path = state corruption; each query needs its own unique path |
| Q85 | **A** | `epochId` = deduplication key for idempotent `foreachBatch`; same epochId on retry |

---

## Topic-by-Topic Answer Key with One-Line Summaries

### Architecture (Q1–Q20)

| Q# | Ans | One-line summary |
|---|---|---|
| 1 | **C** | SparkSession wraps SparkContext; `spark.sparkContext` returns it |
| 2 | B | `spark.default.parallelism` = RDD only; `sql.shuffle.partitions` = DataFrame shuffles |
| 3 | **C** | YARN container memory = heap + overhead + offHeap = 5.5 GB |
| 4 | **C** | 3 stages: groupByKey(1st boundary) + join(2nd boundary) |
| 5 | B | Concurrent tasks = executor.cores / task.cpus = 8/2 = 4 |
| 6 | B | Speculative: duplicate task on another executor; non-idempotent risk |
| 7 | B | heartbeatInterval must be **less than** networkTimeout |
| 8 | B | External shuffle service preserves shuffle files after dynamic alloc removes executor |
| 9 | B | Kryo: 5-10× faster, 2-5× smaller; needs `spark.kryo.classesToRegister` |
| 10 | B | executor.cores=5 with 16 cores/node → floor(16/5)=3 executors per node |
| 11 | B | `eventLog.rolling.enabled=true` splits logs into size-bounded files |
| 12 | B | Cluster mode: driver runs on worker node; local paths on submit machine unavailable |
| 13 | B | `openCostInBytes` (4MB default) groups small files into single partitions |
| 14 | B | `reducer.maxSizeInFlight` (48MB) bounds per-reducer concurrent fetch |
| 15 | **A** | `shuffle.compress`=output files; `shuffle.spill.compress`=intermediate spills |
| 16 | B | `broadcast.compress=true` (default); compressed before transmission |
| 17 | B | `cleaner.periodicGC.interval` triggers JVM GC on driver (default 30 min) |
| 18 | B | Off-heap: both execution AND storage memory use off-heap pool |
| 19 | B | `executorIdleTimeout`: decommissions executor after N seconds idle |
| 20 | B | `statistics.histogram.enabled=true` needed for CBO histograms |

### Spark SQL (Q21–Q40)

| Q# | Ans | One-line summary |
|---|---|---|
| 21 | B | `LPAD(code, 8, '0')` pads left to length 8; truncates if longer |
| 22 | B | `locate('at', str, 6)` → 8 (1-based search from pos 6) |
| 23 | B | `repeat('ab', 0)` → empty string `''` (not null) |
| 24 | B | `window(timeCol, '10 min')` → struct `{start, end}` tumbling window |
| 25 | B | `unix_timestamp` → LongType; `to_timestamp` → TimestampType |
| 26 | B | `TIMESTAMPADD('HOUR', 3, ts)` — unit, delta, timestamp order (Spark 3.3+) |
| 27 | B | `typeof(ARRAY(1,2,3))` → `'array<int>'` full DDL string |
| 28 | B | `stack(2, 'q1',100,'q2',200)` → 2 rows, 2 columns |
| 29 | B | `map_contains_key` is true even when value is null; map[key] IS NOT NULL misses this |
| 30 | B | `array_position` returns 0 (not null) when element not found; 1-based |
| 31 | **A** | `reduce()` = 10; optional 4th arg `finish` applied to final accumulator |
| 32 | B | `date_part('QUARTER', ts)` → 3 for August |
| 33 | **A** | `make_interval(1, 6)` = 1yr 6mo; added directly to timestamp |
| 34 | B | `ILIKE` (Spark 3.3+) case-insensitive LIKE; `ILIKE ANY` multi-pattern |
| 35 | B | `DECODE` with status=NULL → no branch matches → returns default |
| 36 | B | `to_csv(struct, map('sep','|'))` → `'1|Alice|99.5'` |
| 37 | B | `date_part('MONTH', ts)` → int 8; `date_trunc('MONTH', ts)` → `2024-08-01 00:00:00` |
| 38 | B | `LIKE ANY ('click_%', 'tap_%')` multi-pattern (Spark 3.3+) |
| 39 | B | `second(ts)` → DoubleType including fractional seconds (45.123456) |
| 40 | B | `to_number` raises exception; `try_to_number` returns null on mismatch |

### DataFrame/Dataset API (Q41–Q70)

| Q# | Ans | One-line summary |
|---|---|---|
| 41 | **A** | `withMetadata` → `df.schema["col"].metadata`; data unchanged |
| 42 | B | `~F.col("is_deleted")` = logical NOT; null evaluates to null (excluded) |
| 43 | B | `array_sort(arr, lambda l,r: when(l<r, lit(1)))` for descending |
| 44 | B | `F.window_time(windowCol)` (3.4+) for watermark-compatible window end |
| 45 | **A** | `collect_list` over `orderBy()` window → running list `['login','click','purchase']` |
| 46 | B | `withWatermark` on batch DataFrame = no-op (silently ignored) |
| 47 | B | `df.observe()` → `progress.observedMetrics["name"]` in StreamingQueryListener |
| 48 | B | `F.rint()` → DoubleType; 2.5→2.0, 3.5→4.0 (banker's rounding) |
| 49 | B | Global temp views: `global_temp.view_name`; lifetime = JVM |
| 50 | B | `approx_percentile` accuracy: **higher=better**; `approxQuantile` relError: **lower=better** |
| 51 | B | `partitionOverwriteMode=dynamic` to overwrite only touched partitions |
| 52 | B | `F.nullif(expr, lit(-1))` → null when equal, else expr1 |
| 53 | B | `mapInPandas` = no groupBy; `applyInPandas` = per group |
| 54 | B | `schema.json()` = full JSON with nullable + metadata |
| 55 | B | `xxhash64` → LongType 64-bit; `hash` → IntegerType 32-bit |
| 56 | **A** | `F.lit(None)` = NullType; Parquet rejects; fix: `.cast("string")` |
| 57 | B | `repartitionByRange` = range/quantile-based; `repartition` = hash-based |
| 58 | B | `regexp_extract_all` → ArrayType with ALL matches (Spark 3.1+) |
| 59 | B | `partitionBy("region")` + `bucketBy(16,"id")` + `sortBy()`; bucketBy→saveAsTable |
| 60 | B | `saveAsTable` append validates schema; overwriteSchema=true to change |
| 61 | B | JDBC `predicates` = custom WHERE clauses; one partition per predicate |
| 62 | B | `applyInArrow` → RecordBatch (no Pandas overhead); Spark 3.3+ |
| 63 | B | `F.raise_error(msg)` raises SparkRuntimeException (Spark 3.1+) |
| 64 | B | binaryFile: 4 columns — path, modificationTime, length, content |
| 65 | B | Delta overwrite: `.option("overwriteSchema", "true")` required |
| 66 | B | `stat.cov` = unbounded sample covariance; `stat.corr` = Pearson [-1,1] |
| 67 | B | Temp views = session-scoped; global temp views shared via `global_temp.*` |
| 68 | B | ORC: `option("orc.compress", "zlib")`; Parquet: `option("compression", ...)` |
| 69 | B | `array_min` ignores nulls; returns null only for empty or all-null array |
| 70 | B | `df.offset(100).limit(50)` = SQL LIMIT 50 OFFSET 100 (Spark 3.4+) |

### Troubleshooting & Tuning (Q71–Q80)

| Q# | Ans | One-line summary |
|---|---|---|
| 71 | B | `nonEmptyPartitionRatioForBroadcastJoin`=0.2; <20% non-empty → AQE switches to BHJ |
| 72 | B | `memoryMapThreshold`: blocks > threshold use mmap; smaller use read() |
| 73 | B | `parquet.int96RebaseModeInWrite=LEGACY` for Hive INT96 Julian calendar compat |
| 74 | B | `caseSensitive=false` → CustomerID + customerid → ambiguous AnalysisException |
| 75 | B | `orc.impl=native` (default since 2.3) enables vectorized ORC reads |
| 76 | B | `rangeExchange.sampleSizePerPartition`=100 default; increase for skewed data |
| 77 | B | `planChangeLog.level=INFO` shows AQE plan changes in standard logs |
| 78 | B | `adaptive.forceApply=true` forces AQE on all queries (for testing only) |
| 79 | B | `shuffle.io.serverThreads` = Netty pool size; increase to reduce FetchFailedException |
| 80 | B | `ui.prometheus.enabled=true` → `/metrics/prometheus` endpoint on port 4040 |

### Structured Streaming (Q81–Q90)

| Q# | Ans | One-line summary |
|---|---|---|
| 81 | B | `spark.streams.active` → filter on `.name` to find named query |
| 82 | B | `spark.streams.awaitAnyTermination()` blocks until ANY query stops |
| 83 | **A** | Shared checkpoint path → state corruption; per-query unique path required |
| 84 | B | `query.exception()` returns None (active/clean stop) or StreamingQueryException |
| 85 | **A** | `epochId` = deduplication key for idempotent foreachBatch |
| 86 | B | Append mode + groupBy aggregation + no watermark → AnalysisException |
| 87 | B | `streaming.metricsEnabled=true` → Dropwizard MetricRegistry streaming metrics |
| 88 | B | Stream-stream outer join: BOTH streams must have `withWatermark()` |
| 89 | B | `writeStream.partitionBy("date","hour")` → Hive-style subdirs; pruning supported |
| 90 | B | `maxBytesPerTrigger="100m"` byte-based throttle; mutually exclusive with maxFilesPerTrigger |

### Spark Connect (Q91–Q95)

| Q# | Ans | One-line summary |
|---|---|---|
| 91 | B | Spark Connect: gRPC port 15002; `remote("sc://host:15002")`; no Java needed |
| 92 | B | Client builds logical plan; action → protobuf via gRPC → server optimizes + executes |
| 93 | B | `spark.sparkContext` → PySparkNotImplementedError; replace with DataFrame APIs |
| 94 | B | `pip install pyspark[connect]` adds grpcio, grpcio-status, googleapis-common-protos |
| 95 | B | `spark.connect.extensions.relation.classes` registers RelationPlugin on server |

### Pandas API on Spark (Q96–Q100)

| Q# | Ans | One-line summary |
|---|---|---|
| 96 | B | `groupby().transform(func)` = group-preserving; same length as input |
| 97 | B | `psdf.spark.apply(lambda sdf: ...)` = escape hatch to native Spark; wraps result back |
| 98 | B | `plot()` internally calls `toPandas()` capped by `compute.max_rows` (default 1000) |
| 99 | B | `psdf.spark.schema` → StructType with full type info (not Pandas dtype) |
| 100 | B | MultiIndex: supported for creation + basic ops; sortlevel/reindex = partial support |

---

## Configuration Defaults Cheatsheet

### Memory & Resources

| Config | Default | Effect |
|---|---|---|
| `spark.sql.shuffle.partitions` | 200 | DataFrame shuffle partition count |
| `spark.default.parallelism` | # cores | RDD op parallelism |
| `spark.executor.memory` | 1g | JVM heap per executor |
| `spark.executor.memoryFraction` | — | Use `spark.memory.fraction` instead |
| `spark.memory.fraction` | 0.6 | Fraction of heap for execution+storage |
| `spark.memory.storageFraction` | 0.5 | Fraction of memory.fraction for storage |
| `spark.memory.offHeap.enabled` | false | Enable off-heap memory pool |
| `spark.executor.memoryOverhead` | max(384MB, 10% of executor.memory) | YARN overhead |

### Performance & AQE

| Config | Default | Effect |
|---|---|---|
| `spark.sql.adaptive.enabled` | true (3.2+) | Adaptive Query Execution |
| `spark.sql.adaptive.forceApply` | false | Force AQE on all queries |
| `spark.sql.planChangeLog.level` | TRACE | Log AQE plan changes at this level |
| `spark.sql.autoBroadcastJoinThreshold` | 10MB | Tables smaller than this get broadcast |
| `spark.sql.adaptive.nonEmptyPartitionRatioForBroadcastJoin` | 0.2 | AQE BHJ conversion threshold |
| `spark.sql.execution.rangeExchange.sampleSizePerPartition` | 100 | Range sampling accuracy |
| `spark.sql.statistics.histogram.enabled` | false | Enable CBO histogram collection |
| `spark.sql.caseSensitive` | false | Case-insensitive column resolution |
| `spark.sql.sources.partitionOverwriteMode` | static | Partition overwrite behavior |

### Shuffle

| Config | Default | Effect |
|---|---|---|
| `spark.shuffle.compress` | true | Compress shuffle output files |
| `spark.shuffle.spill.compress` | true | Compress shuffle intermediate spills |
| `spark.reducer.maxSizeInFlight` | 48MB | Max bytes a reducer fetches concurrently |
| `spark.shuffle.service.enabled` | false | External shuffle service |
| `spark.shuffle.io.serverThreads` | max(3, cores/4) | Netty server threads for shuffle |

### File I/O

| Config | Default | Effect |
|---|---|---|
| `spark.sql.files.openCostInBytes` | 4MB | Small file grouping threshold |
| `spark.storage.memoryMapThreshold` | 2MB | Blocks > threshold use mmap |
| `spark.sql.orc.impl` | native | ORC reader implementation |
| `spark.sql.orc.enableVectorizedReader` | true | Vectorized ORC reads |
| `spark.sql.parquet.int96RebaseModeInWrite` | EXCEPTION | INT96 timestamp rebase mode |

### Streaming

| Config | Default | Effect |
|---|---|---|
| `spark.sql.streaming.metricsEnabled` | false | Dropwizard metrics registration |
| `spark.eventLog.rolling.enabled` | false | Rolling event log splitting |
| `spark.ui.prometheus.enabled` | false | `/metrics/prometheus` endpoint |

### Networking & GC

| Config | Default | Effect |
|---|---|---|
| `spark.executor.heartbeatInterval` | 10s | Heartbeat to driver |
| `spark.network.timeout` | 120s | Must be > heartbeatInterval |
| `spark.broadcast.compress` | true | Compress broadcast variables |
| `spark.cleaner.periodicGC.interval` | 30min | JVM GC trigger on driver |
| `spark.dynamicAllocation.executorIdleTimeout` | 60s | Remove idle executors |

---

## Function Quick Reference

### String Functions

| Function | Returns | Behavior |
|---|---|---|
| `LPAD(str, len, pad)` | string | Pad left to length len |
| `RPAD(str, len, pad)` | string | Pad right to length len |
| `locate(substr, str, pos)` | int | 1-based position; 0 if not found |
| `repeat(str, n)` | string | '' for n≤0, null for null input |
| `to_csv(struct, opts)` | string | Struct → delimiter-separated |
| `ILIKE` (3.3+) | boolean | Case-insensitive LIKE |
| `LIKE ANY (...)` (3.3+) | boolean | OR of multiple patterns |

### Date/Time Functions

| Function | Returns | Notes |
|---|---|---|
| `unix_timestamp(str, fmt)` | LongType | Epoch seconds |
| `to_timestamp(str, fmt)` | TimestampType | Full timestamp |
| `TIMESTAMPADD(unit, n, ts)` | TimestampType | Spark 3.3+; unit first |
| `date_part('QUARTER', ts)` | double/int | Numeric component |
| `date_trunc('MONTH', ts)` | timestamp | Start of period |
| `second(ts)` | DoubleType | Includes fractional seconds |
| `make_interval(y, mo)` | interval | y years, mo months |

### Array Functions

| Function | Returns | Notes |
|---|---|---|
| `array_position(arr, val)` | LongType | 1-based; 0 if not found |
| `array_min(arr)` | element type | Ignores nulls |
| `array_max(arr)` | element type | Ignores nulls |
| `array_sort(arr, comparator)` | array | Custom lambda comparator |
| `regexp_extract_all(col, pat, idx)` | ArrayType | All matches (3.1+) |
| `reduce(arr, zero, func, finish?)` | any | 4th arg optional |
| `stack(n, ...)` | multiple rows | Unpivot N rows |

### Map Functions

| Function | Returns | Notes |
|---|---|---|
| `map_contains_key(map, key)` (3.3+) | boolean | True even for null values |
| `typeof(expr)` | string | DDL type string |

### Numeric Functions

| Function | Returns | Algorithm |
|---|---|---|
| `F.rint(col)` | DoubleType | Banker's rounding (half-even) |
| `F.round(col, n)` | DoubleType | Traditional rounding |
| `F.xxhash64(*cols)` | LongType | xxHash64 (64-bit) |
| `F.hash(*cols)` | IntegerType | MurmurHash3 (32-bit) |
| `to_number(str, fmt)` | Decimal | Raises on mismatch |
| `try_to_number(str, fmt)` | Decimal | Null on mismatch (3.3+) |

### Null Functions

| Function | Returns | Notes |
|---|---|---|
| `F.nullif(expr1, expr2)` | type of expr1 | null if equal, else expr1 |
| `F.lit(None).cast("type")` | typed null | Always cast before writing |
| `F.coalesce(*cols)` | first non-null | Multiple columns |

### Schema/Type Functions

| Function | Returns | Notes |
|---|---|---|
| `df.schema["col"].metadata` | dict | Access via field metadata |
| `df.withMetadata(col, meta)` | DataFrame | Attaches metadata to field |
| `schema.json()` | string | Full JSON representation |
| `schema.simpleString()` | string | Compact DDL string |
| `schema.treeString()` | string | Human-readable tree |

---

## Decision Trees

### "Is the answer B?" Quick Test

```
Is the question about...
├── SparkSession wrapping SparkContext? → C (Q1)
├── YARN total container memory? → C (Q3)
├── How many stages from groupByKey+join? → C (Q4)
├── shuffle.compress vs spill.compress distinction? → A (Q15)
├── reduce() with optional finish argument? → A (Q31)
├── make_interval syntax for date arithmetic? → A (Q33)
├── withMetadata and schema field access? → A (Q41)
├── collect_list running window result? → A (Q45)
├── F.lit(None) causing NullType error? → A (Q56)
├── Shared checkpoint path causing corruption? → A (Q83)
├── foreachBatch epochId for idempotency? → A (Q85)
└── Anything else? → B (89% probability)
```

### Wide vs Narrow Transformation

```
Transformation type?
├── Narrow: map, filter, flatMap, mapPartitions, union
│   → Pipelined within same stage (no shuffle)
└── Wide: groupByKey, groupBy, join, reduceByKey, repartition, sort
    → Creates stage boundary (shuffle)
    → Each wide transform adds one stage boundary
    → N wide transforms → N+1 stages
```

### Memory Type Decision

```
Which memory region?
├── JVM heap
│   ├── Execution (shuffle/sort/aggregation): spark.memory.fraction × heap
│   └── Storage (cache/broadcast): spark.memory.storageFraction × above
├── Off-heap (Tungsten direct memory)
│   ├── Enabled by: spark.memory.offHeap.enabled=true
│   ├── Size: spark.memory.offHeap.size
│   └── Both execution AND storage can use off-heap
└── memoryOverhead (YARN only)
    └── Overhead = max(384MB, 10% of executor.memory)
    └── Used by: native code, Python UDFs, containers
```

### Streaming Output Mode vs Aggregation

```
Has aggregation (groupBy + agg)?
├── YES
│   ├── complete mode → always works
│   ├── update mode → works, emits changed rows only
│   └── append mode
│       ├── Has withWatermark? → works
│       └── No watermark? → AnalysisException at planning!
└── NO aggregation
    ├── append mode → standard; new rows only
    └── update/complete → errors or unsupported
```

### JDBC Partitioning Strategy

```
Data volume and distribution?
├── Numeric column, uniform distribution
│   → lowerBound / upperBound / numPartitions
├── Non-numeric or non-uniform
│   → predicates = ["region='US'", "region='EU'", ...]
├── Column for partition filter known
│   → partitionColumn + lowerBound + upperBound
└── Need exactly-once with ordering
    → Single connection (no parallelism) + predicates for safety
```

### Checkpoint Strategy

```
Running multiple streaming queries?
├── Same checkpoint path for all → ❌ CORRUPTION (Q83=A)
├── One unique path per query → ✅ CORRECT
│   q1.writeStream.option("checkpointLocation", "/ckpt/q1").start()
│   q2.writeStream.option("checkpointLocation", "/ckpt/q2").start()
└── Shared root with unique subfolders is fine:
    /checkpoints/query_name_1/
    /checkpoints/query_name_2/
```

---

## Spark Connect Quick Reference

| Aspect | Standard PySpark | Spark Connect |
|---|---|---|
| Installation | `pip install pyspark` + JVM | `pip install pyspark[connect]` |
| JVM required? | Yes | No |
| Connection | Local or spark-submit | `SparkSession.builder.remote("sc://host:15002")` |
| Transport | JVM in-process | gRPC (default port 15002) |
| Data format | JVM row format | Apache Arrow |
| `spark.sparkContext` | Available | ❌ PySparkNotImplementedError |
| `sc.parallelize()` | Available | ❌ → use `spark.createDataFrame()` |
| `sc.textFile()` | Available | ❌ → use `spark.read.text()` |
| `sc.addFile()` | Available | ❌ → use shared filesystem |

---

## Iteration 9 vs Iteration 8 Answer Key Comparison

| Q# | Iter 8 | Iter 9 | Changed? |
|---|---|---|---|
| Q1 | B | **C** | Yes |
| Q3 | B | **C** | Yes |
| Q4 | B | **C** | Yes |
| Q15 | B | **A** | Yes |
| Q31 | B | **A** | Yes |
| Q33 | B | **A** | Yes |
| Q41 | B | **A** | Yes |
| Q45 | B | **A** | Yes |
| Q56 | B | **A** | Yes |
| Q83 | B | **A** | Yes |
| Q85 | B | **A** | Yes |
| Iter 8 non-B | Q31=A, Q60=A, Q71=A, Q81=A | — | Different set! |

**Iter 8 non-B answers (Q31, Q60, Q71, Q81) are all B in Iter 9.**
**Iter 9 non-B answers (Q1, Q3, Q4, Q15, Q31, Q33, Q41, Q45, Q56, Q83, Q85) are all B in Iter 8.**
Do not carry over memory from Iter 8 to Iter 9!
