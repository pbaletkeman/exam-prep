# Quick Reference — Databricks Spark Associate (Iteration 3)

**100 questions | 20E / 60M / 20H | 79 single-answer / 21 multi-answer**

---

## 35 Memory Anchors (5 per Topic)

### Topic 1 — Architecture
| # | Anchor | Fact |
|---|--------|------|
| A1 | **WholeStageCodegen** = operator fusion | Fuses filter/project/agg into **one** JVM bytecode function; stages with codegen show `*` prefix |
| A2 | **checkpoint() truncates lineage** | Writes to reliable storage (HDFS/cloud); `persist()` retains lineage; `localCheckpoint()` = Executor disk only |
| A3 | **Off-heap = TWO properties** | `spark.memory.offHeap.enabled=true` **AND** `spark.memory.offHeap.size` (>0); one alone does nothing |
| A4 | **PROCESS_LOCAL = fastest** | Data in same Executor JVM; locality order: PROCESS_LOCAL > NODE_LOCAL > RACK_LOCAL > ANY |
| A5 | **spark.reducer.maxSizeInFlight** | Controls concurrent in-flight shuffle data on the reduce side; tune when reducers OOM |

### Topic 2 — Spark SQL
| # | Anchor | Fact |
|---|--------|------|
| A6 | **schema_of_json() returns STRING** | Returns a DDL string like `'STRUCT<id: BIGINT>'`, NOT a Python StructType object |
| A7 | **filter() not array_filter()** | Higher-order array filter = `F.filter()`, NOT `F.array_filter()` (doesn't exist) |
| A8 | **nvl2 logic: NOT null → col2** | `nvl2(c1, c2, c3)` = if c1 is NOT null → c2; if null → c3 (opposite of nvl) |
| A9 | **lpad pads LEFT** | `F.lpad('42', 6, '0')` → `'000042'`; right-pad = `F.rpad()` |
| A10 | **try_cast returns null** | `try_cast('abc' AS INT)` → null (no exception); Spark SQL 3.4+ |

### Topic 3 — DataFrame API
| # | Anchor | Fact |
|---|--------|------|
| A11 | **element_at uses 1-based index** | `element_at(array, 2)` returns 2nd element (1-indexed); same for `slice(start=2, ...)` |
| A12 | **F.array_concat() DOES NOT EXIST** | Use `F.concat(col_a, col_b)` to concatenate arrays (includes duplicates) |
| A13 | **insertInto = by position** | Matches columns by position, not name; `saveAsTable + append` matches by name — safer |
| A14 | **na.replace() ≠ na.fill()** | `replace()` substitutes specific values (NOT nulls); `fill()` handles null values |
| A15 | **summary() adds quartiles** | `describe()` = count/mean/stddev/min/max; `summary()` adds 25%/50%/75% |

### Topic 4 — Troubleshooting
| # | Anchor | Fact |
|---|--------|------|
| A16 | **Default codec = lz4 (NOT snappy)** | `spark.io.compression.codec` default = `lz4`; common wrong answer = snappy |
| A17 | **CBO = join reordering** | CBO reorders multi-table joins to minimize intermediate sizes (requires ANALYZE TABLE) |
| A18 | **explain('formatted') = node IDs** | Most readable physical plan; includes node IDs and subplan summaries |
| A19 | **16 cores/executor = HDFS bottleneck** | HDFS client not designed for high concurrency; recommended: 4-5 cores per executor |
| A20 | **Repartition by join key = WORSE for skew** | `repartition(n, skewedKey)` concentrates skewed key; use AQE or salting instead |

### Topic 5 — Streaming
| # | Anchor | Fact |
|---|--------|------|
| A21 | **orderBy in streaming = AnalysisException** | Global sort not supported on unbounded streams; raises `AnalysisException` |
| A22 | **dropDuplicates needs watermark** | Without watermark: unbounded state growth; watermark bounds when old state can be dropped |
| A23 | **query.lastProgress = last batch metrics** | Python dict with batchId, inputRows, processingTime; `query.status` = current state dict |
| A24 | **Continuous = sub-millisecond** | `trigger(continuous='1s')` = continuous Tasks, async checkpoint; NOT same as processingTime='1s' |
| A25 | **startingOffsets='earliest' = checkpoint wins** | On restart with checkpoint, uses saved offsets regardless of startingOffsets setting |

### Topic 6 — Spark Connect
| # | Anchor | Fact |
|---|--------|------|
| A26 | **.remote() not .master()** | Spark Connect client: `.builder.remote('sc://host')`, NOT `.builder.master('sc://host')` |
| A27 | **Analysis happens server-side** | Errors raised on action (`.count()`, `.collect()`), not on DataFrame definition |
| A28 | **Serverless = no SparkContext** | `spark.sparkContext` unavailable in Databricks Serverless; RDD API not exposed |
| A29 | **SSL = ;use_ssl=true in URL** | `sc://hostname:15002/;use_ssl=true` — appended to the sc:// connection string |
| A30 | **gRPC + Protobuf = any language** | Spark Connect enables non-JVM languages (Rust, Go, etc.); results as Apache Arrow |

### Topic 7 — Pandas API on Spark
| # | Anchor | Fact |
|---|--------|------|
| A31 | **ops_on_diff_frames = False by default** | Cross-DF operations raise error; enable with `ps.set_option('compute.ops_on_diff_frames', True)` |
| A32 | **ps.get_dummies stays distributed** | One-hot encoding result is still a pyspark.pandas DF (NOT collected to driver) |
| A33 | **ps.merge = both syntaxes valid** | `ps.merge(l, r, on=...)` AND `l.merge(r, on=...)` both work |
| A34 | **shortcut_limit = 1000 rows** | Below limit: data eagerly cached, `len()` instant; above: full Spark job triggered |
| A35 | **ps.read_csv supports cloud paths** | Delegates to Spark connector; `s3://`, `gs://`, `abfss://` all work natively |

---

## Master Config Reference Table

| Property | Default | Controls |
|----------|---------|---------|
| `spark.sql.shuffle.partitions` | 200 | Shuffle output partition count |
| `spark.memory.fraction` | 0.6 | Fraction of JVM heap for Spark Memory |
| `spark.memory.storageFraction` | 0.5 | Storage fraction within Spark Memory |
| `spark.memory.offHeap.enabled` | false | Enable off-heap Tungsten memory |
| `spark.memory.offHeap.size` | 0 | Off-heap size in bytes (must be >0) |
| `spark.serializer` | JavaSerializer | `KryoSerializer` for speed/compactness |
| `spark.reducer.maxSizeInFlight` | 48m | Max in-flight shuffle data per reducer |
| `spark.io.compression.codec` | lz4 | Shuffle/RDD compression codec |
| `spark.shuffle.compress` | true | Compress shuffle output files to disk |
| `spark.speculation.multiplier` | 1.5 | Slow-task multiple before speculative launch |
| `spark.locality.wait` | 3s | Wait time before relaxing data locality |
| `spark.sql.adaptive.enabled` | true | Enable AQE (Spark 3.0+) |
| `spark.sql.adaptive.skewJoin.enabled` | true | AQE auto-split skewed partitions |
| `spark.sql.adaptive.skewJoin.skewedPartitionThresholdInBytes` | 256m | Byte threshold for skewed partition |
| `spark.executor.memoryOverhead` | 10% / 384m | Off-heap memory for Python workers, native libs |
| `spark.dynamicAllocation.enabled` | false | Enable DRA (requires external shuffle service) |

---

## Locality Level Hierarchy

```
PROCESS_LOCAL  → data in same Executor JVM process          (fastest)
    ↓ (wait spark.locality.wait)
NODE_LOCAL     → same node, different JVM process
    ↓ (wait spark.locality.wait)
RACK_LOCAL     → same rack, different node
    ↓ (wait spark.locality.wait)
ANY            → anywhere in cluster                        (slowest)
```

Rack awareness reduces cross-rack bandwidth when PROCESS_LOCAL and NODE_LOCAL are unavailable.

---

## Stage Count Quick Guide

| Query Pattern | Stages | Why |
|---------------|--------|-----|
| Scan + filter + write | 1 | No shuffle |
| BroadcastHashJoin + groupBy | **2** | 1 shuffle (for groupBy) |
| SortMergeJoin + write | **3** | 2 shuffles (both sides) |
| SortMergeJoin + groupBy | **4** | 3 shuffles (both join sides + groupBy) |
| Union + write | 1 per side + 1 | Union doesn't shuffle; write does |

**Key rule**: Each **shuffle exchange** = 1 stage boundary. Broadcast joins do NOT create stage boundaries.

---

## Higher-Order Functions Cheatsheet

| Function | Signature | Returns | Notes |
|----------|-----------|---------|-------|
| `F.transform(arr, lambda x: ...)` | `(ArrayType, x→y)` | `ArrayType` | Maps each element |
| `F.filter(arr, lambda x: ...)` | `(ArrayType, x→bool)` | `ArrayType` | Keeps elements where True |
| `F.aggregate(arr, init, merge, finish?)` | `(ArrayType, T, (T,x)→T)` | `T` | Reduces to single value |
| `F.forall(arr, lambda x: ...)` | `(ArrayType, x→bool)` | `BooleanType` | True if ALL match |
| `F.exists(arr, lambda x: ...)` | `(ArrayType, x→bool)` | `BooleanType` | True if ANY matches |
| `F.zip_with(arr_a, arr_b, lambda x,y: ...)` | Two arrays + (x,y)→z | `ArrayType` | Element-wise merge |
| `F.map_filter(map, lambda k,v: ...)` | `(MapType, (k,v)→bool)` | `MapType` | Keeps entries where True |
| `F.flatten(arr)` | `ArrayType(ArrayType)` | `ArrayType` | Concatenates inner arrays |
| `F.posexplode(arr)` | `ArrayType` | Rows + `pos` col | Zero-based index column |
| `F.element_at(arr, n)` | `ArrayType, Int` | `T` | **1-based** indexing |
| `F.slice(arr, start, len)` | `ArrayType, Int, Int` | `ArrayType` | **1-based** start |
| `F.sequence(start, stop)` | Two ints/longs | `ArrayType(LongType)` | Inclusive range |
| `F.arrays_zip(*arrs)` | Multiple arrays | `ArrayType(StructType)` | Positional pairing |

---

## Array Set Operations Summary

| Function | Exists? | Result | Deduplicates? |
|----------|---------|--------|---------------|
| `F.array_union(a, b)` | ✅ | Elements in a OR b | Yes |
| `F.array_intersect(a, b)` | ✅ | Elements in BOTH | Yes |
| `F.array_except(a, b)` | ✅ | Elements in a NOT in b | Yes |
| `F.array_distinct(a)` | ✅ | All unique elements of a | Yes |
| `F.concat(a, b)` | ✅ | Concatenated, all elements | **No** |
| `F.array_concat(a, b)` | ❌ | **DOES NOT EXIST** | — |

---

## Null Handling Cheatsheet

| Function | What It Handles | Returns Null? |
|----------|----------------|---------------|
| `df.na.fill(val, subset)` | **Null values** → replace with val | No |
| `df.na.replace(vals, rep, subset)` | **Specific values** (not null) → replace | No |
| `df.na.drop(thresh, subset)` | Drops rows with nulls | — |
| `F.coalesce(*cols)` | First non-null value | Only if all null |
| `nvl(c1, c2)` | Returns c2 if c1 IS null | No |
| `nvl2(c1, c2, c3)` | Returns c2 if c1 NOT null; c3 if null | No |
| `F.greatest(*cols)` | Largest **non-null** across columns | Only if all null |
| `F.least(*cols)` | Smallest **non-null** across columns | Only if all null |
| `try_cast(expr AS type)` | Returns null on failed cast | Yes (on failure) |
| `F.forall(arr, pred)` | Returns null if array is null | Yes (null array) |
| `F.exists(arr, pred)` | Returns null if array is null | Yes (null array) |

---

## Write API Comparison

| Method | Column Matching | Fault-Safe? | Notes |
|--------|----------------|-------------|-------|
| `df.write.insertInto('t')` | **By position** | No | Silently wrong if col order differs |
| `df.write.mode('append').saveAsTable('t')` | **By name** | Yes | Preferred for append |
| `df.writeTo('cat.schema.t').append()` | By name | Yes | v2 API; catalog-format-aware |
| `df.writeTo('cat.schema.t').overwritePartitions()` | By name | Yes | Replaces matching partitions only |
| `df.writeTo('cat.schema.t').createOrReplace()` | By name | Yes | Create or full replace |

---

## Streaming Output Modes Reference

| Mode | When to Use | Supported Aggregations |
|------|-------------|----------------------|
| `append` | Append-only rows (default for non-aggregated) | No aggregations / windowed agg with watermark |
| `complete` | Full result table each batch | All aggregations (no watermark required) |
| `update` | Only changed/new rows | All aggregations |

**Global sort (`orderBy`)** raises `AnalysisException` in all streaming modes.

---

## Streaming Trigger Reference

| Trigger | Code | Latency | Notes |
|---------|------|---------|-------|
| Micro-batch | `processingTime='30 seconds'` | Seconds | Standard mode |
| As fast as possible | (no trigger) | Seconds | Processes each batch immediately |
| Once | `once=True` | N/A | One batch, then stop |
| Available now | `availableNow=True` | N/A | Multiple batches until caught up (3.3+) |
| Continuous | `continuous='1 second'` | Sub-millisecond | Experimental; async checkpoint; limited ops |

---

## Spark Connect vs Classic

| Feature | Classic Spark | Spark Connect |
|---------|--------------|---------------|
| Session creation | `.builder.master('local')...` | `.builder.remote('sc://host')...` |
| Plan analysis | Client-side (on creation) | **Server-side (on action)** |
| SparkContext / RDD | Available | **NOT available** |
| Language support | JVM only natively | Any gRPC language |
| Transport | Internal RPC | **gRPC + Protobuf** |
| Results format | JVM objects | **Apache Arrow** |
| SSL config | N/A | `;use_ssl=true` in URL |
| Databricks Serverless | No | **Yes (required)** |

---

## CBO vs AQE vs Rule-Based

| Optimizer | Timing | Requires | What It Does |
|-----------|--------|---------|--------------|
| Rule-Based | Plan compilation | Nothing | Push-down predicates, eliminate projections, fold constants |
| CBO | Plan compilation | `ANALYZE TABLE + COMPUTE STATISTICS` | **Reorder joins**, choose join type by estimated size |
| AQE | **Runtime** (at shuffle boundaries) | `spark.sql.adaptive.enabled=true` | Coalesce partitions, convert SMJ→BHJ, **split skewed partitions** |

---

## Skewed Join Decision Matrix

| Scenario | Best Solution |
|----------|--------------|
| Small skewed table fits in memory | `broadcast()` hint → BroadcastHashJoin |
| AQE enabled, random skew | AQE skewJoin auto-split |
| Systematic key skew (Spark <= 3.0 or no AQE) | Salting (add random prefix to key) |
| Repartition by join key | **Do NOT do this** — makes skew worse |
| Increase shuffle partitions | Minor relief; does NOT fix single-key skew |

---

## Pandas API on Spark — Key Differences from Native Pandas

| Operation | Native pandas | pyspark.pandas |
|-----------|--------------|----------------|
| Operations between DFs | Always works | Requires `ops_on_diff_frames=True` |
| `len(df)` | Always instant | May trigger Spark job (above shortcut_limit) |
| `get_dummies()` result | Local pandas DF | **Distributed** pyspark.pandas DF |
| Cloud path in `read_csv()` | Needs boto3/gcsfs | Works natively (delegates to Spark) |
| `merge()` | `.merge(r, on=...)` | Both `.merge()` and `ps.merge()` valid |

---

## DataFrame Method Quick Index

| Method | Returns | Notes |
|--------|---------|-------|
| `df.describe(*cols)` | DataFrame | count/mean/stddev/min/max rows |
| `df.summary(*stats)` | DataFrame | Adds 25%/50%/75% quartiles |
| `df.limit(n)` | DataFrame | At most n rows, no ordering |
| `df.sample(fraction, ...)` | DataFrame | Approximate %; correct syntax shown |
| `df.randomSplit([w1, w2], seed)` | List[DataFrame] | Approximate splits |
| `df.stat.corr('c1', 'c2')` | float | Pearson correlation |
| `df.stat.approxQuantile('c', probs, err)` | List[float] | Approximate quantiles |
| `df.stat.freqItems(['c1'], support)` | DataFrame | One row with frequent item arrays |
| `df.stat.crosstab('c1', 'c2')` | DataFrame | Cross-tabulation (contingency table) |
| `df.hint('name', *params)` | DataFrame | Advisory hint (not guaranteed) |
| `df.transform(func)` | DataFrame | `func(df)` for method chaining |
| `df.observe('name', *metrics)` | DataFrame | Inline metrics via QueryExecutionListener |
| `df.printSchema()` | None | Prints to console |
| `df.explain(mode)` | None | Prints plan to console |
| `df.checkpoint()` | DataFrame | Materializes to reliable storage |
| `df.localCheckpoint()` | DataFrame | Materializes to Executor disk (not fault-tolerant) |

---

## EXPLAIN Modes Comparison

| Mode | Shows | Use When |
|------|-------|---------|
| `df.explain()` (default) | Physical plan | Quick check |
| `df.explain('formatted')` | Physical plan + node IDs + formatted | Complex plans, easiest to read |
| `df.explain('extended')` | Logical + physical plans | Understanding optimizer transforms |
| `df.explain('cost')` | Physical plan + cost estimates | CBO diagnostics |
| `df.explain('codegen')` | Generated Java bytecode | Diagnosing codegen suppression |

---

## Schema Construction Reference

| Approach | Syntax | Use When |
|----------|--------|---------|
| DDL string | `StructType.fromDDL('id BIGINT, name STRING')` | Quick, concise definition |
| StructType/StructField | `StructType([StructField('id', IntegerType(), True)])` | Programmatic/complex schemas |
| `F.schema_of_json(sample)` | Returns **DDL string**, NOT StructType | Inferring from JSON samples |
| spark.read inference | `.option('inferSchema', True)` | Development only (triggers action) |

---

## Checkpoint/Persist Decision Tree

```
Need fault-tolerant storage?
├── Yes → df.checkpoint() (HDFS/cloud; truncates lineage; slower)
│         └── Need faster (OK with Executor failure risk)?
│             └── Yes → df.localCheckpoint() (Executor disk; truncates lineage)
└── No → df.persist(storageLevel)
          └── Need lineage preserved?
              └── Yes → df.persist() (keeps lineage; memory/disk configurable)
```

---

## 10-Point Exam Success Checklist (Iteration 3 Specific)

| # | Check |
|---|-------|
| 1 | **Off-heap**: Two properties required (`enabled=true` AND `size>0`) |
| 2 | **checkpoint vs persist**: checkpoint = HDFS + truncates lineage; persist = retains lineage |
| 3 | **lz4 not snappy**: `spark.io.compression.codec` default = **lz4** |
| 4 | **filter() not array_filter()**: higher-order filter uses `F.filter()` |
| 5 | **element_at and slice = 1-based**: index 2 on ['a','b','c'] = 'b' |
| 6 | **na.replace ≠ na.fill**: replace = specific values; fill = nulls |
| 7 | **orderBy in streaming = AnalysisException**: global sort not supported |
| 8 | **schema_of_json = DDL string, not StructType object** |
| 9 | **16 cores/executor = HDFS bottleneck**: stick to 4-5 cores per executor |
| 10 | **Repartition by join key worsens skew**: use AQE or broadcast instead |
