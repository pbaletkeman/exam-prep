# Databricks Certified Associate Developer for Apache Spark — Iteration 4 Quick Reference

**Fast lookup condensed reference for exam questions (Iteration 4)**

**Last Updated**: May 17, 2026

---

## Key Concepts by Topic

### Topic 1: Spark Architecture

| Concept | Key Fact |
|---------|----------|
| **`--py-files`** | Distributes `.py`/`.egg`/`.zip` to executors; adds to Python path |
| **`--files`** | Distributes files (CSV, JSON) to working dir; NOT added to path |
| **`--jars`** | Distributes JAR files to executors; adds to classpath |
| **`--packages`** | Maven coordinates (auto-download + dependency resolution) |
| **YARN Driver Location** | ApplicationMaster container on a worker node (cluster mode) |
| **Port 4040** | Live Spark application UI (driver web UI) |
| **Port 18080** | Spark History Server (completed app UIs) |
| **`spark.driver.maxResultSize`** | Max serialized size of ALL task results collected to driver |
| **`HashPartitioner`** | `abs(key.hashCode()) % numPartitions` |
| **`groupByKey()` Partitioner** | Attaches `HashPartitioner(spark.default.parallelism)` |
| **`MEMORY_ONLY_2`** | Two replicated in-memory copies on different executors |
| **`spark.task.maxFailures`** | Default 4; task aborts job if exceeded |
| **`spark.sql.files.maxPartitionBytes`** | Default 128 MB; target partition size for file reads |
| **Dynamic Allocation Bounds** | `minExecutors` (floor) and `maxExecutors` (ceiling) |
| **Executor Memory Breakdown** | Reserved (300 MB) → Execution (60%) + Storage (40%) |
| **Shuffle Spill** | In-memory buffer full + execution memory exhausted |
| **`spark.sql.warehouse.dir`** | Default `spark-warehouse` in current working dir |
| **Thrift Server** | HiveServer2-compatible JDBC/ODBC gateway |
| **Stage Boundary** | Narrow (no shuffle): filter, map, select; Wide (shuffle): repartition, join |
| **`spark.sql.files.openCostInBytes`** | ~4 MB default; biases toward co-locating small files |
| **Managed vs External** | Managed: data deleted on DROP; External: data persists |
| **Temp Views** | Session-scoped; NOT persisted to Hive metastore |
| **`TaskSetManager`** | Tracks task state, implements retries, locality-aware scheduling |
| **`spark.executor.extraJavaOptions`** | Passes JVM flags to executors (GC, agents, diagnostic) |
| **Heartbeat vs Network Timeout** | heartbeatInterval (10s) << networkTimeout (120s) |

### Topic 2: Spark SQL

| Function | Signature | Returns |
|----------|-----------|---------|
| `F.regexp_extract()` | `regexp_extract(col, pattern, groupIdx)` | Capture group idx (0=full match) |
| `F.instr()` | `instr(str, substr)` | 1-based position or 0 if not found |
| `F.translate()` | `translate(str, matchingString, replaceString)` | Char-by-char replacement |
| `F.substring_index()` | `substring_index(str, delim, count)` | First count delim-separated segments |
| `F.overlay()` | `overlay(base, insert, pos)` | Replace from position pos with insert |
| `F.add_months()` | `add_months(date_col, months)` | Date + N months (handles month-end) |
| `F.date_trunc()` | `date_trunc(unit, date_col)` | Truncate to unit (year, month, week, etc.) |
| `F.to_utc_timestamp()` | `to_utc_timestamp(ts, tz)` | Interpret local tz as UTC (adds offset) |
| `F.from_unixtime()` | `from_unixtime(unix_ts)` | Unix epoch → `'yyyy-MM-dd HH:mm:ss'` string |
| `F.arrays_overlap()` | `arrays_overlap(array1, array2)` | Boolean (common element?) |
| `F.map_from_arrays()` | `map_from_arrays(keys, values)` | MapType from two arrays |
| `F.map_concat()` | `map_concat(map1, map2)` | Merge maps; right wins on key conflict |
| `F.format_number()` | `format_number(value, decimals)` | Formatted string with thousands separators |
| `F.size()` | `size(array_col)` | Array length (null if col is null, Spark 3.0+) |
| **ROWS vs RANGE** | ROWS: physical offset; RANGE: logical value distance | Different in multi-dup scenarios |
| **EXCEPT DISTINCT** | Remove rows in left NOT in right; deduplicate result | Set difference |
| **EXCEPT ALL** | Remove one per occurrence in right; preserve extras | Bag difference |
| **INTERSECT ALL** | Intersection; preserve duplicates up to min count | Bag intersection |
| **ROLLUP(a, b)** | Grouping sets: (a, b), (a), () with NULLs for subtotals | 3 grouping levels |
| **CUBE(a, b)** | All 2^n combinations: (a,b), (a), (b), () | 4 grouping levels |
| **TABLESAMPLE** | `SELECT * FROM t TABLESAMPLE (10 PERCENT)` | Random ~10% row sample |
| **QUALIFY** | `QUALIFY RANK() OVER (...) = 1` | Filter rows after window functions |

### Topic 3: DataFrame API

| Operation | Behavior |
|-----------|----------|
| **Ambiguous Refs** | `F.col('name')` after join → AnalysisException if both sides have same col |
| **CSV Compression** | `.option('compression', 'snappy')` for Parquet (not 'codec') |
| **CSV Headers** | `.option('header', True)` to write headers |
| **Text Write** | Requires exactly 1 `StringType` column |
| **`maxRecordsPerFile`** | Cap rows per output file; splits across files |
| **`pathGlobFilter`** | `.option('pathGlobFilter', '*.parquet')` to filter files |
| **`nullValue` (read)** | `.csv(nullValue='N/A')` maps literal string to null |
| **Parquet Schema** | Read from file footer metadata (fast; no data scan) |
| **`F.broadcast()`** | `from pyspark.sql.functions import broadcast` |
| **`df.rdd`** | Returns RDD of `Row` objects (not dicts/tuples) |
| **`withColumn('existing', expr)`** | Replaces existing column (no duplicate) |
| **`F.coalesce(c1, c2, c3)`** | First non-null value (null-safe fallback) |
| **`exceptAll()` vs `subtract()`** | exceptAll removes one per occurrence; subtract removes all |
| **`spark.createDataFrame(rows)`** | Schema inferred from Row field names |
| **JDBC Write** | `df.write.jdbc(url, table, mode, properties)` |
| **JDBC Read Parallelism** | `numPartitions` + `partitionColumn` + `lowerBound`/`upperBound` |
| **JDBC Read Predicates** | `.option('predicates', [...]).jdbc(...)` for custom WHERE clauses |
| **CSV Header Write** | `.option('header', True)` (default: no headers) |
| **`@pandas_udf`** | `from pyspark.sql.functions import pandas_udf` |
| **`applyInPandas`** | One call per group; receives full group DataFrame |
| **`cache().count()`** | cache() is lazy; count() materializes (action) |
| **`StructType` Equality** | Value-based `==` (not reference-based) |
| **`getNumPartitions()`** | `.rdd.getNumPartitions()` or `len(.rdd.partitions)` |
| **Generic Load** | `spark.read.load(path, format='delta')` |
| **`selectExpr()`** | SQL expressions inline: `selectExpr('age * 2 AS double_age')` |
| **`when()` Default** | No `.otherwise()` → null for unmatched rows |
| **`to_pandas_on_spark()`** | Returns Pandas API on Spark (distributed) |
| **`coalesce()` vs `repartition()`** | coalesce: narrow (no shuffle); repartition: full shuffle |
| **Parquet Write Options** | compression, maxRecordsPerFile, partitionOverwriteMode |
| **Invalid Parquet Options** | header (CSV-only); mergeSchema (read/Delta write only) |

### Topic 4: Troubleshooting & Tuning

| Config/Tool | Purpose |
|-------------|---------|
| `spark.sql.autoBroadcastJoinThreshold = -1` | Disable automatic broadcast joins |
| `ANALYZE TABLE t COMPUTE STATISTICS FOR ALL COLUMNS` | Collect column stats for CBO |
| `CACHE TABLE t` | Eager cache (immediate materialization) |
| `CACHE LAZY TABLE t` | Lazy cache (materialize on first query) |
| `spark.sql.adaptive.advisoryPartitionSizeInBytes = 64m` | AQE target partition size (advisory) |
| **ORC Use Case** | Native Hive format; good for Hive pipelines |
| `spark.sql.cbo.enabled = true` | Activate Cost-Based Optimizer |
| `spark.sql.cbo.joinReorder.enabled = true` | Requires CBO enabled; reorder multi-joins |
| `spark.sql.join.preferSortMergeJoin = true` | Prefer SortMergeJoin over ShuffledHashJoin |
| `df.explain('cost')` | Physical plan with CBO estimates (row count, size) |
| `spark.sql.inMemoryColumnarStorage.compressed = true` | Snappy compression on cached data (default) |
| `spark.sql.adaptive.coalescePartitions.minPartitionNum = 1` | Lower bound on partitions after AQE coalesce |

### Topic 5: Structured Streaming

| Trigger | Behavior |
|---------|----------|
| `trigger(once=True)` | Single batch, then auto-stop |
| `trigger(processingTime='30s')` | New batch every 30s (if data available) |
| `trigger(continuous='1s')` | Continuous mode; sub-ms latency target |

| Concept | Key Fact |
|---------|----------|
| **Checkpoint Required** | `.option('checkpointLocation', '/path')` for fault tolerance |
| **`append` Mode** | New rows only; supports all query types |
| **`update` Mode** | Changed or new rows only; smaller output than complete |
| **`complete` Mode** | Entire result table; requires aggregation |
| **Non-Agg `complete`** | NOT supported; raises AnalysisException |
| **Watermark Effect** | State dropped when watermark passes window end |
| **`append` + Watermark** | Window results emitted AFTER watermark advances past end |
| **`foreachBatch(func)`** | Receives micro-batch DataFrame + batch ID; enables multi-sink writes |
| **`failOnDataLoss = false`** | Silently skip unavailable Kafka offsets (data retention expired) |
| **`query.recentProgress`** | List of dicts; each dict = one micro-batch progress report |
| **`StreamingQueryListener`** | `from pyspark.sql.streaming import StreamingQueryListener` |
| **Window + Watermark Required** | `withWatermark()` must precede `groupBy(window(...))` |

### Topic 6: Spark Connect

| Concept | Key Fact |
|---------|----------|
| **Connection** | `SparkSession.builder.remote('sc://host:15002').getOrCreate()` |
| **Env Variable** | `SPARK_REMOTE=sc://host:15002` (auto-detected) |
| **Serialization** | Apache Arrow columnar format (fast, efficient) |
| **Session Proxy** | `getActiveSession()` returns client-side proxy |
| **Plan Analysis** | Server-side execution; results returned over gRPC |
| **Databricks Serverless** | `DatabricksSession.builder.serverless().getOrCreate()` |
| **RDD APIs** | NOT supported in Spark Connect (DataFrame/SQL only) |
| **vs spark-submit** | Connect: lightweight client + remote server; submit: driver on cluster |

### Topic 7: Pandas API on Spark

| Operation | Behavior |
|-----------|----------|
| `ps.sql('SELECT ...')` | SQL query against registered temp views |
| `ps.read_parquet()` | Read to Pandas API on Spark DataFrame |
| `.to_pandas_on_spark()` | Convert Spark DF to Pandas API on Spark |
| `apply(func, axis=1)` | Row-wise application; func receives each row as Series |
| `rolling(3).mean()` | 3-row trailing average; first 2 rows = NaN |
| `ps.concat([df1, df2], axis=0)` | Stack rows (default) |
| `ps.concat([df1, df2], axis=1)` | Join side-by-side by index (requires `ops_on_diff_frames=True`) |
| `ignore_index=True` | Reset resulting index |
| **axis=1 merge logic** | Distributed index-based merge (E=correct) |

---

## Configuration Quick Reference

```python
# Broadcasting & Join Strategy
spark.conf.set('spark.sql.autoBroadcastJoinThreshold', -1)
spark.conf.set('spark.sql.join.preferSortMergeJoin', 'true')

# Cost-Based Optimizer
spark.conf.set('spark.sql.cbo.enabled', 'true')
spark.conf.set('spark.sql.cbo.joinReorder.enabled', 'true')

# Adaptive Query Execution
spark.conf.set('spark.sql.adaptive.enabled', 'true')
spark.conf.set('spark.sql.adaptive.advisoryPartitionSizeInBytes', '67108864')  # 64 MB
spark.conf.set('spark.sql.adaptive.coalescePartitions.minPartitionNum', 1)

# In-Memory Caching
spark.conf.set('spark.sql.inMemoryColumnarStorage.compressed', 'true')

# Streaming
spark.conf.set('spark.streaming.stopGracefullyOnShutdown', 'true')
```

---

## Exam Question Patterns (Iteration 4)

### Easy Questions (20 Questions)
- `spark-submit` flags (Q1)
- YARN cluster deployment (Q2)
- Configuration key purposes (Q3–Q4)
- Function signatures (Q21–Q24)
- DataFrame method behavior (Q41–Q45)
- Trigger definitions (Q81–Q82)
- Pandas API basics (Q96–Q97)

### Medium Questions (60 Questions)
- Partitioner behavior (Q5–Q6)
- Storage level replication (Q7)
- Task failure handling (Q8)
- File partitioning (Q9–Q16)
- String/date/array functions (Q25–Q35)
- DataFrame read/write options (Q46–Q62)
- Tuning configurations (Q73–Q78)
- Streaming output modes (Q83–Q88)
- Spark Connect basics (Q93–Q94)
- Pandas API operations (Q98–Q99)

### Hard Questions (20 Questions)
- Hive metastore persistence (Q17)
- TaskSetManager responsibilities (Q18)
- JVM options passing (Q19)
- Network timeout tuning (Q20)
- String overlays & set operations (Q37–Q40)
- Schema equality & JDBC (Q65–Q70)
- AQE partition coalescing (Q79–Q80)
- Streaming listeners & window management (Q89–Q90)
- Spark Connect vs spark-submit (Q95)
- Pandas API advanced operations (Q100)

---

## Memory Anchors

### 1-Based Indexing (SQL/DataFrame APIs)
- `instr()` returns 1-based position
- `element_at()` uses 1-based indexing
- `overlay()` position is 1-based
- `date_trunc()` returns first day of period

### Default Configurations
- **`spark.sql.files.maxPartitionBytes`** = 128 MB
- **`spark.sql.files.openCostInBytes`** ≈ 4 MB
- **`spark.task.maxFailures`** = 4
- **`spark.executor.heartbeatInterval`** = 10 s
- **`spark.network.timeout`** = 120 s
- **Reserved executor memory** = 300 MB
- **`spark.memory.fraction`** = 0.6 (Execution/Storage split)

### Serialization Formats
- Parquet: embedded schema in footer (fast inference)
- ORC: native Hive format (BloomFilters, stripe-level pushdown)
- Arrow: Spark Connect data transfer (columnar, efficient)

### Stage Boundaries
- Narrow: filter, map, select, withColumn (no shuffle)
- Wide: repartition, join, groupBy, aggregation (shuffle)

### Spark Connect Specifics
- Client runs locally; server runs computation
- Multiple clients can share same server session
- NO RDD API support
- Apache Arrow for data transfer

### Streaming State Management
- Watermark enables state cleanup
- `append` mode emits after watermark passes window
- `complete` mode requires aggregation
- `foreachBatch` receives entire micro-batch DataFrame

---

## Study Progression for Iteration 4

**Day 1**: Architecture (Q1–20) — Focus on spark-submit flags, cluster managers, configuration keys

**Day 2**: SQL (Q21–40) — String/date/array functions, ROLLUP/CUBE, EXCEPT/INTERSECT/TABLESAMPLE

**Day 3**: DataFrame API (Q41–70) — Read/write options, column operations, JDBC patterns, schema handling

**Day 4**: Troubleshooting (Q71–80) — CBO, AQE, join strategies, caching, explain modes

**Day 5**: Streaming (Q81–90) — Triggers, output modes, checkpoints, watermarks, listeners

**Day 6**: Spark Connect + Pandas (Q91–100) — Connection patterns, Arrow serialization, Pandas operations

**Day 7**: Practice test + review of weak areas

---

**End of Quick Reference (Iteration 4)**

Print this page and review before the exam. Combine with STUDY_GUIDE_ITER4 for detailed explanations.
