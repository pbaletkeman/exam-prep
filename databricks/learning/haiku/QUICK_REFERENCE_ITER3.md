# Databricks Certified Associate Developer for Apache Spark — Iteration 3 Quick Reference

**Fast lookup condensed reference for exam questions (Iteration 3)**

**Last Updated**: May 17, 2026

---

## Key Concepts by Topic

### Topic 1: Spark Architecture

| Concept | Key Fact |
|---------|----------|
| **RDD Lineage** | Chain of parent RDD dependencies; retained on failure |
| **DataFrame Lineage** | Optimized logical plan; passes through Catalyst |
| **WholeStageCodegen** | Fuses multiple operators → single JVM bytecode function |
| **Tungsten** | Binary encoding, cache-aware, off-heap memory, code generation |
| **External Shuffle Service** | Persists shuffle files independent of Executor lifetime; enables DRA |
| **Checkpoint** | Reliable storage + lineage truncation |
| **Persist** | In-memory cache + lineage retained |
| **Task Serialization** | Closure + captured variables serialized (Java or Kryo) |
| **Kryo** | Faster, smaller than Java serialization |
| **Off-Heap Memory** | `offHeap.enabled=true` + `offHeap.size=<bytes>` |
| **Python Workers** | Separate process per Executor thread; uses `memoryOverhead` |
| **Cluster Managers** | Standalone, YARN, Kubernetes all support client/cluster mode |
| **Data Locality** | PROCESS_LOCAL > NODE_LOCAL > RACK_LOCAL > ANY |
| **Resource Profile API** | Per-stage Executor config (cores, memory, GPUs) |
| **Rack Awareness** | Scheduler avoids cross-rack traffic when possible |
| **Speculation** | Launch duplicate of slow Task; `multiplier=1.5` default |
| **Unified Memory** | Execution can borrow from Storage; Storage blocks evicted on demand |
| **Shuffle Reduce** | `reducer.maxSizeInFlight` = concurrent fetch limit |

### Topic 2: Spark SQL

| Function | Signature | Returns |
|----------|-----------|---------|
| `F.transform()` | `transform(array, lambda x: expr)` | Array with transformed elements |
| `F.filter()` | `filter(array, lambda x: predicate)` | Filtered array |
| `F.aggregate()` | `aggregate(array, init, lambda acc, x: op)` | Single aggregated value |
| `F.flatten()` | `flatten(array_of_arrays)` | Flat array |
| `F.forall()` | `forall(array, lambda x: pred)` | Boolean (all satisfy?) |
| `F.exists()` | `exists(array, lambda x: pred)` | Boolean (at least one?) |
| `F.from_json()` | `from_json(col, schema)` | Struct/Array from JSON |
| `F.schema_of_json()` | `schema_of_json(sample)` | DDL string of schema |
| `F.greatest()` | `greatest(col1, col2, ...)` | Max non-null value |
| `F.least()` | `least(col1, col2, ...)` | Min non-null value |
| `F.months_between()` | `months_between(end, start)` | DoubleType (fractional months) |
| `F.lpad()` | `lpad(col, length, pad)` | Left-padded string |
| `F.rpad()` | `rpad(col, length, pad)` | Right-padded string |
| `F.element_at()` | `element_at(array, index)` | Element at **1-based** index |
| `F.slice()` | `slice(array, start, length)` | Slice using **1-based** indexing |
| `F.posexplode()` | `posexplode(array)` | Rows with `pos` column |
| `F.explode()` | `explode(array)` | One row per element |
| `F.arrays_zip()` | `arrays_zip(a, b)` | `ArrayType(StructType)` pairs |
| `F.zip_with()` | `zip_with(a, b, lambda x,y: expr)` | Element-wise operation |
| `F.array_union()` | `array_union(a, b)` | Union (deduplicated) |
| `F.array_intersect()` | `array_intersect(a, b)` | Intersection (deduplicated) |
| `F.array_except()` | `array_except(a, b)` | `a` minus `b` (deduplicated) |
| `F.array_distinct()` | `array_distinct(array)` | Distinct elements |
| `F.map_keys()` | `map_keys(map)` | Array of keys |
| `F.map_values()` | `map_values(map)` | Array of values |
| `F.map_filter()` | `map_filter(map, lambda k,v: pred)` | Filtered map |
| `F.sequence()` | `sequence(start, end)` | Array from start to end |
| `nvl()` | `nvl(col1, col2)` | col2 if col1 null, else col1 |
| `nvl2()` | `nvl2(col1, col2, col3)` | col2 if col1 NOT null, else col3 |
| `try_cast()` | `try_cast(col, type)` | Cast with null on fail (no error) |
| **PIVOT** | `groupBy('col').pivot('month').agg(sum())` | Rows→columns rotation |

### Topic 3: DataFrame API

| Operation | Behavior |
|-----------|----------|
| `df.describe(cols)` | count, mean, stddev, min, max |
| `df.summary()` | count, mean, stddev, min, **25%, 50%, 75%**, max |
| `df.stat.corr('a', 'b')` | Pearson correlation (float) |
| `df.stat.approxQuantile('col', [0.25, 0.5], 0.05)` | Approx quantiles with error tolerance |
| `df.stat.crosstab('a', 'b')` | Contingency table; rows=a values, cols=b values, cells=counts |
| `df.stat.freqItems(['col'], support=0.01)` | Frequent items ≥1% |
| `df.limit(n)` | First n rows (no order) |
| `df.sample(0.1, False)` | ~10% sample without replacement |
| `df.randomSplit([0.8, 0.2])` | Split into ~80%/20% (not exact) |
| `df.printSchema()` | Print schema; returns None |
| `df.hint('repartition', 10)` | Suggest repartition (advisory) |
| `df.transform(func)` | Apply func(df) for chaining |
| **Write**: `bucketBy(16, 'key').sortBy('col').saveAsTable()` | 16 buckets; enables bucket join |
| **Write**: `insertInto()` | Match columns **by position** |
| **Write**: `writeTo('cat.schema.table').append()` | v2 API; explicit operations |
| `df.checkpoint()` | Distributed storage + lineage truncation |
| `df.localCheckpoint()` | Local disk (fast, not fault-tolerant) |
| `F.create_map(k1, v1, k2, v2)` | MapType column |
| `F.element_at(array, 2)` | Element at **1-based index** 2 |
| `StructType.fromDDL('id BIGINT, name STRING')` | Create schema from DDL |
| `df.observe('name', F.count(), F.sum())` | Inline metrics; no separate aggregation |
| **Delta**: `spark.read.format('delta').option('versionAsOf', 2).load()` | Time travel |

### Topic 4: Troubleshooting & Tuning

| Config/Tool | Purpose |
|-------------|---------|
| `df.explain('formatted')` | Physical plan + readable layout |
| `df.explain('codegen')` | Generated JVM source code |
| `spark.conf.set('key', val)` | Set config at runtime |
| `spark.sql.adaptive.enabled=true` | AQE enabled (coalesce, skew, join switch) |
| `spark.sql.adaptive.skewJoin.skewedPartitionThresholdInBytes` | Bytes threshold for skew detection |
| `spark.locality.wait` | Wait time before relaxing data locality |
| `spark.shuffle.compress=true` | Compress shuffle files (default lz4) |
| `spark.io.compression.codec` | **Default: `lz4`** |
| `spark.executor.cores=4-5` | Optimal; 16+ cores = HDFS + GC bottleneck |
| **Skew Mitigation**: Salting | Add random salt (0 to N-1) + replicate small table |
| **Skew Mitigation**: AQE | `spark.sql.adaptive.skewJoin.enabled=true` |
| **Skew Mitigation**: Broadcast | Use `broadcast()` for small table |

### Topic 5: Structured Streaming

| Trigger | Behavior |
|---------|----------|
| `trigger(processingTime='30s')` | New batch every 30s |
| `trigger(once=True)` | Single batch; stop after |
| `trigger(availableNow=True)` | Multiple batches efficiently; stop after |
| `trigger(continuous='1s')` | No micro-batch boundaries; sub-ms latency; checkpoint async |

| Concept | Key Fact |
|---------|----------|
| **File Source** | `maxFilesPerTrigger=5` = rate control |
| **Kafka Source** | `startingOffsets='earliest'` = from beginning if no checkpoint |
| **Stream-Static Join** | Static side re-read per batch; current snapshot used |
| **`dropDuplicates()`** | Requires watermark to bound state |
| **`mapGroupsWithState`** | User state per group key; exactly one output per group/batch |
| **`query.status`** | Current state dict |
| **`query.lastProgress`** | Most recent batch metrics |
| **Global `orderBy`** | NOT supported (unbounded stream) |

### Topic 6: Spark Connect

| Concept | Key Fact |
|---------|----------|
| **Connection** | `SparkSession.builder.remote('sc://host:15002').getOrCreate()` |
| **Plan Analysis** | Happens on server when action triggered |
| **Errors** | Raised by server, returned to client |
| **Databricks Serverless** | Uses Spark Connect; no RDD API; instant provisioning |
| **Multi-Language** | gRPC API language-agnostic; no JVM required |
| **SSL** | `sc://host:15002/;use_ssl=true` |

### Topic 7: Pandas API on Spark

| Operation | Behavior |
|-----------|----------|
| `ps.merge(left, right, on='key', how='inner')` | Join pyspark.pandas DataFrames |
| `ps.get_dummies(psdf, columns=['color'])` | One-hot encoding (distributed) |
| `ps.read_csv('s3://bucket/file.csv')` | Cloud storage supported |
| `ps.set_option('compute.ops_on_diff_frames', True)` | Allow inter-DataFrame operations |
| `ps.set_option('compute.shortcut_limit', 1000)` | Collect/cache DataFrames ≤1000 rows locally |
| **Shortcut Impact**: `len()` on small DF → instant; large DF → Spark job |

---

## Exam Question Patterns (Iteration 3)

### Easy Questions (20 Questions)
- **Cluster Manager Definitions**: Standalone vs YARN vs Kubernetes
- **Function Signatures**: `F.from_json()`, `F.struct()`, `F.greatest()`
- **DataFrame Methods**: `df.describe()`, `df.limit()`, `df.printSchema()`
- **Streaming Triggers**: `processingTime` behavior

### Medium Questions (60 Questions)
- **Tradeoff Analysis**: Checkpoint vs persist; Kryo vs Java serialization
- **Scenario Debugging**: "PySpark OOM" → Python worker overhead
- **Configuration**: `spark.conf.set()`, `spark.locality.wait`
- **Complex Operations**: `F.aggregate()`, `df.stat.crosstab()`, window functions
- **Design Decisions**: When to use bucketBy, when to salt

### Hard Questions (20 Questions)
- **Multi-Stage Implications**: Stage count given query DAG
- **Memory Model**: Unified memory borrowing; executor cores tradeoff
- **Advanced Streaming**: `mapGroupsWithState` with watermark
- **Optimization Trade-offs**: Skew mitigation salting costs vs benefits
- **Language Integration**: Spark Connect with Rust/non-JVM languages

---

## Configuration Quick Reference

```python
# Memory & Execution
spark.conf.set('spark.executor.memory', '4g')
spark.conf.set('spark.executor.cores', 4)
spark.conf.set('spark.driver.memory', '4g')
spark.conf.set('spark.memory.offHeap.enabled', 'true')
spark.conf.set('spark.memory.offHeap.size', '1g')
spark.conf.set('spark.executor.pyspark.memory', '1g')  # Python worker memory

# Serialization
spark.conf.set('spark.serializer', 'org.apache.spark.serializer.KryoSerializer')

# SQL & Optimization
spark.conf.set('spark.sql.shuffle.partitions', 200)
spark.conf.set('spark.sql.autoBroadcastJoinThreshold', '10m')
spark.conf.set('spark.sql.adaptive.enabled', 'true')
spark.conf.set('spark.sql.adaptive.coalescePartitions.enabled', 'true')
spark.conf.set('spark.sql.adaptive.skewJoin.enabled', 'true')
spark.conf.set('spark.sql.adaptive.skewJoin.skewedPartitionThresholdInBytes', '67108864')  # 64 MB

# Performance Tuning
spark.conf.set('spark.shuffle.compress', 'true')
spark.conf.set('spark.io.compression.codec', 'lz4')
spark.conf.set('spark.locality.wait', '3s')
spark.conf.set('spark.speculation', 'true')
spark.conf.set('spark.speculation.multiplier', 1.5)

# Streaming
spark.conf.set('spark.streaming.stopGracefullyOnShutdown', 'true')

# Pandas API on Spark
spark.conf.set('spark.sql.execution.pandas.respectSessionTimeZone', 'true')
ps.set_option('compute.ops_on_diff_frames', False)
ps.set_option('compute.shortcut_limit', 1000)
```

---

## Last-Minute Memory Anchors

### Indexing (1-based in Spark SQL)
- `element_at(array, 2)` → second element (1-based)
- `slice(array, start=2, length=3)` → elements at indices 2, 3, 4

### Serialization
- **Default**: Java serialization (slow)
- **Kryo**: Faster, more compact
- **Config**: `spark.serializer = 'org.apache.spark.serializer.KryoSerializer'`

### Memory Overhead
- PySpark uses `spark.executor.memoryOverhead` + `spark.executor.pyspark.memory`
- Python process memory is **off-heap** (outside JVM)

### Compression Default
- `spark.io.compression.codec` default is **`lz4`** (not gzip)

### Data Locality Order
1. PROCESS_LOCAL (same JVM) — fastest
2. NODE_LOCAL (same machine)
3. RACK_LOCAL (same rack)
4. ANY (anywhere) — slowest

### Checkpoint vs Persist
- `persist()` → memory/disk, lineage retained, fast recompute
- `checkpoint()` → distributed storage, lineage truncated, slower recompute but breaks long chains

### Execution Memory Borrowing
- Storage can be evicted when Execution needs space (unified model)
- Not true for old fixed-partition model

### Spark Connect
- **Language-agnostic** gRPC (no JVM on client required)
- **Plan analysis** happens on server when action triggered
- **Error handling**: Errors from server returned to client

---

## Study Progression for Iteration 3

**Day 1**: Architecture (Q1–20) — Focus on RDD/DataFrame difference, Tungsten, external shuffle service

**Day 2**: SQL (Q21–40) — Drill into higher-order functions (transform, filter, aggregate), array operations

**Day 3**: DataFrame API (Q41–70) — Master statistics (describe, summary, corr, quantile), write operations, Delta

**Day 4**: Troubleshooting (Q71–80) — EXPLAIN variants, CBO, AQE, skew mitigation

**Day 5**: Streaming (Q81–90) — Triggers, state management, watermarks

**Day 6**: Spark Connect + Pandas (Q91–100) — gRPC architecture, pyspark.pandas options

**Day 7**: Practice test + review of weak areas

---

**End of Quick Reference (Iteration 3)**

Print this page and review before the exam. Combine with STUDY_GUIDE_ITER3 for detailed explanations.
