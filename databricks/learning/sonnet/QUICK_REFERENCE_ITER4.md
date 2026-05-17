# QUICK REFERENCE — Iteration 4
# Databricks Certified Associate Developer for Apache Spark

**Iteration**: 4 | **Answer Types**: 78 single / 22 multi
**Format**: 35 memory anchors · lookup tables · checklists

---

## PART 1: 35 MEMORY ANCHORS (5 per topic)

### Topic 1 — Architecture

| ID | Anchor | Fact |
|----|--------|------|
| A1 | **Python module deploy flag** | `--py-files` distributes `.py`/`.egg`/`.zip` AND adds to Python path; `--files` does NOT add to path |
| A2 | **History Server port** | Live app UI = **4040** · Standalone Master = **8080** · History Server = **18080** |
| A3 | **HashPartitioner formula** | `abs(key.hashCode()) % numPartitions` — same hash → same partition |
| A4 | **MEMORY_ONLY_2 meaning** | `_2` = **two replicated copies across two different executors** (NOT two tiers, NOT serialized) |
| A5 | **heartbeat vs network timeout** | `heartbeatInterval` (default 10s) must be **significantly less than** `network.timeout` (default 120s) |

### Topic 2 — Spark SQL

| ID | Anchor | Fact |
|----|--------|------|
| A6 | **size(null) in Spark 3+** | Returns **null** — NOT 0, NOT -1 (legacy -1 requires `spark.sql.legacy.sizeOfNull = true`) |
| A7 | **from_unixtime return type** | Returns **StringType** `'yyyy-MM-dd HH:mm:ss'` — NOT TimestampType |
| A8 | **map_concat duplicate keys** | **Right map wins** — left map's value is overwritten |
| A9 | **ROLLUP vs CUBE grouping sets** | `ROLLUP(a,b)` = **3** sets: `(a,b),(a),()`; `CUBE(a,b)` = **4** sets: `(a,b),(a),(b),()` |
| A10 | **QUALIFY clause** | Filters rows after window evaluation — available since **Spark 3.4**; window functions cannot go in WHERE |

### Topic 3 — DataFrame API

| ID | Anchor | Fact |
|----|--------|------|
| A11 | **broadcast() import** | `from pyspark.sql.functions import broadcast` — NOT from hints, NOT from pyspark directly |
| A12 | **df.rdd content** | Returns RDD of **`Row` objects** — NOT dicts, NOT plain tuples |
| A13 | **write.text() requirement** | Requires **exactly one column of StringType** — will fail otherwise |
| A14 | **df.getNumPartitions()** | Does NOT exist on DataFrame — use `df.rdd.getNumPartitions()` or `len(df.rdd.partitions)` |
| A15 | **write.jdbc() table param** | Second positional arg is `table` — NOT `dbtable` (that's a read option), NOT `tableName` |

### Topic 4 — Troubleshooting

| ID | Anchor | Fact |
|----|--------|------|
| A16 | **Disable broadcast join** | Set threshold to **-1** (NOT 0) — `-1` disables; `0` has different effect |
| A17 | **CBO join reorder** | Needs TWO configs: `cbo.enabled = true` AND `cbo.joinReorder.enabled = true` |
| A18 | **CACHE TABLE behavior** | Eager (immediate scan) — `CACHE LAZY TABLE` is the lazy variant |
| A19 | **explain('cost')** | Shows **CBO estimates**: row counts and data sizes per operator |
| A20 | **ORC preferred when** | Data produced by Apache Hive (ORC is Hive's native format with best statistics) |

### Topic 5 — Streaming

| ID | Anchor | Fact |
|----|--------|------|
| A21 | **trigger(once=True)** | Processes ALL available data in ONE micro-batch then **automatically stops** |
| A22 | **complete mode restriction** | Complete output mode **requires aggregation** — invalid for non-aggregated queries |
| A23 | **5-min tumbling window for 12:07** | Falls in `[12:05, 12:10)` only — tumbling windows are non-overlapping |
| A24 | **recentProgress type** | Returns a **list of dicts** — NOT a single dict, NOT a streaming DataFrame |
| A25 | **StreamingQueryListener** | From `pyspark.sql.streaming` — monitors ALL queries without modifying each one |

### Topic 6 — Spark Connect

| ID | Anchor | Fact |
|----|--------|------|
| A26 | **SPARK_REMOTE env var** | Set to `sc://host:port` — auto-configures Connect without calling `.remote()` |
| A27 | **Connect data serialization** | **Apache Arrow** (NOT Kryo, NOT Protobuf for data, NOT JSON) |
| A28 | **Databricks Serverless session** | `DatabricksSession.builder.serverless().getOrCreate()` |
| A29 | **Connect vs submit: driver location** | Connect = **client machine**; submit cluster mode = worker node |
| A30 | **Connect multi-client sharing** | Multiple clients CAN share one Spark Connect server session |

### Topic 7 — Pandas API on Spark

| ID | Anchor | Fact |
|----|--------|------|
| A31 | **ps.sql()** | Runs SQL against Pandas API on Spark temp views — NOT `ps.execute_sql()` |
| A32 | **Two ways to read Parquet** | `ps.read_parquet('/path')` AND `spark.read.parquet('/path').pandas_api()` — both valid |
| A33 | **apply(func, axis=1)** | **Row-wise** — func receives each row as `pd.Series` |
| A34 | **rolling(3).mean() first rows** | First two rows yield **NaN** (insufficient preceding values) |
| A35 | **ps.concat axis=1 requirement** | Requires `ops_on_diff_frames = True` when DataFrames come from different plans |

---

## PART 2: MASTER CONFIG REFERENCE TABLE

| Configuration Property | Default | Key Facts |
|----------------------|---------|-----------|
| `spark.task.maxFailures` | **4** | Max task failures before job abort |
| `spark.sql.files.maxPartitionBytes` | **128 MB** | Target max bytes per input partition (file reads) |
| `spark.sql.files.openCostInBytes` | **~4 MB** | Per-file overhead; co-locates small files |
| `spark.sql.shuffle.partitions` | **200** | Post-shuffle partition count |
| `spark.network.timeout` | **120 s** | Executor declared dead if no contact for this long |
| `spark.executor.heartbeatInterval` | **10 s** | Heartbeat frequency (must be << network.timeout) |
| `spark.sql.autoBroadcastJoinThreshold` | **10 MB** | Auto-broadcast if table ≤ this; **-1 to disable** |
| `spark.sql.adaptive.advisoryPartitionSizeInBytes` | **64 MB** | AQE target coalesce partition size |
| `spark.sql.adaptive.coalescePartitions.minPartitionNum` | depends | Lower bound on AQE coalesced partitions |
| `spark.sql.inMemoryColumnarStorage.compressed` | **true** | Compress cached columnar data (Snappy) |
| `spark.sql.cbo.enabled` | **false** | Enables Cost-Based Optimizer |
| `spark.sql.cbo.joinReorder.enabled` | **false** | Enables CBO multi-join reordering |
| `spark.sql.join.preferSortMergeJoin` | **true** | Prefer SMJ over ShuffledHashJoin |
| `spark.dynamicAllocation.minExecutors` | **0** | DRA lower bound |
| `spark.dynamicAllocation.maxExecutors` | **∞** | DRA upper bound |
| `spark.sql.warehouse.dir` | **`spark-warehouse` (cwd)** | Managed table storage location |

---

## PART 3: PORT AND ENDPOINT REFERENCE

| Port | Service | Notes |
|------|---------|-------|
| **4040** | Live Application UI | Per running application; increments if port taken (4041, 4042…) |
| **7077** | Standalone Master RPC | Worker registration and driver submission port |
| **8080** | Standalone Master Web UI | Cluster overview UI |
| **18080** | **Spark History Server** | Displays completed application event logs |
| **10000** | Thrift Server (HiveServer2) | JDBC/ODBC connections |
| **15002** | Spark Connect gRPC | Default Connect server port |

---

## PART 4: STAGE COUNT QUICK GUIDE

| Operation Pattern | Stage Count | Reason |
|-----------------|-------------|--------|
| map → filter → collect | 1 | All narrow transformations |
| repartition → map → collect | 2 | repartition = shuffle boundary |
| groupBy → agg | 2 | Shuffle for groupBy |
| groupBy → agg → filter → show | 2 | Filter after agg is narrow |
| join (non-broadcast) → select | 3 | Two shuffles: one per side |
| broadcast join → select | 2 | Broadcast = 1 shuffle (or 0 if both already distributed) |
| distinct → count | 2 | distinct = shuffle |

---

## PART 5: SPARK SQL FUNCTIONS CHEATSHEET — ITERATION 4

### String Functions

| Function | Signature | Returns | Key Behavior |
|----------|-----------|---------|-------------|
| `regexp_extract` | `(col, pattern, idx)` | String | `idx=0` = full match; `idx=1` = group 1 |
| `regexp_replace` | `(col, pattern, replacement)` | String | Replaces ALL matches |
| `instr` | `(str, substr)` | Int | 1-based; **0 if not found**; never null |
| `locate` | `(substr, str[, pos])` | Int | 1-based; supports start position |
| `substring_index` | `(str, delim, count)` | String | `+n` = from left; `-n` = from right |
| `translate` | `(str, matchingStr, replaceStr)` | String | 1:1 char replacement; case-sensitive |
| `format_number` | `(number, decimals)` | **StringType** | Adds thousands separators: `1,234,567.89` |
| `overlay` | `(str, replace, pos[, len])` | String | Replaces from pos; discards remainder |

### Date/Time Functions

| Function | Returns | Key Fact |
|----------|---------|---------|
| `add_months(date, n)` | DateType | Handles month-end edge cases |
| `date_trunc('month', date)` | TimestampType | → `YYYY-MM-01 00:00:00` |
| `from_unixtime(ts)` | **StringType** | `'yyyy-MM-dd HH:mm:ss'` in session TZ |
| `to_utc_timestamp(ts, tz)` | TimestampType | Treats ts as local tz → converts to UTC |
| `from_utc_timestamp(ts, tz)` | TimestampType | Treats ts as UTC → converts to local tz |
| `months_between(d1, d2)` | **DoubleType** | Fractional months |

### Array/Map Functions

| Function | Key Fact |
|----------|---------|
| `size(null)` | **Returns null** in Spark 3+ (NOT 0, NOT -1) |
| `arrays_overlap(a, b)` | True if ANY element appears in both |
| `map_from_arrays(keys, vals)` | Creates map from two equal-length arrays |
| `map_concat(m1, m2)` | **Right map wins** on duplicate keys |
| `concat(arr1, arr2)` | Use for array concatenation (NOT `array_concat` — doesn't exist) |

---

## PART 6: WINDOW FUNCTION REFERENCE

### ROWS vs RANGE

| | `ROWS BETWEEN` | `RANGE BETWEEN` |
|--|---------------|----------------|
| Basis | Physical row offset | Logical ORDER BY value distance |
| With duplicates | Counts N physical positions | Includes all rows with same boundary value |
| Example | `1 PRECEDING` = exactly the 1 row before | `1 PRECEDING` = all rows where value is within 1 of current |

### Window Frame Types

```sql
-- Tumbling (fixed per partition):
PARTITION BY dept ORDER BY salary
ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW  -- running total

-- Sliding:
ORDER BY date ROWS BETWEEN 6 PRECEDING AND CURRENT ROW  -- 7-row window

-- RANGE-based:
ORDER BY price RANGE BETWEEN 10 PRECEDING AND 10 FOLLOWING  -- value ±10
```

---

## PART 7: SET OPERATIONS REFERENCE

| Operation | Behavior | Duplicates |
|-----------|----------|-----------|
| `EXCEPT` / `EXCEPT DISTINCT` | Remove ALL occurrences of rows in right | Deduplicates |
| `EXCEPT ALL` | Remove ONE occurrence per match in right | Preserves extra left duplicates |
| `INTERSECT` / `INTERSECT DISTINCT` | Common rows | Deduplicates result |
| `INTERSECT ALL` | Common rows up to min count in both | Preserves duplicates up to min count |
| `UNION` | All rows | Deduplicates |
| `UNION ALL` | All rows | Preserves all duplicates |

---

## PART 8: OUTPUT MODE DECISION TREE

```
Is the query aggregated?
├── NO  → append or update only (complete NOT valid)
└── YES → all three modes are available
           ├── append: need watermark; emits only after watermark passes window end
           ├── update: emits changed/new rows each trigger
           └── complete: emits ALL rows in result every trigger
```

---

## PART 9: COALESCE vs REPARTITION QUICK GUIDE

| | `coalesce(n)` | `repartition(n)` |
|-|--------------|-----------------|
| Shuffle? | **No** (narrow) | **Yes** (full shuffle) |
| Stage boundary? | No | Yes |
| Partition balance | Uneven (merges existing) | Even |
| Can increase n? | Up to current count only | Yes |
| Best for | Reducing without shuffle | Even distribution, increasing partitions |

---

## PART 10: JDBC READ/WRITE OPTION REFERENCE

### Read Options (spark.read.jdbc)

| Option | Purpose |
|--------|---------|
| `numPartitions` | Number of parallel read tasks |
| `partitionColumn` | Column to split on (must be numeric) |
| `lowerBound` | Lower bound for range split |
| `upperBound` | Upper bound for range split |
| `predicates` | List of WHERE clauses (one per partition) |
| `fetchsize` | Rows fetched per DB round-trip (performance, not parallelism) |
| `dbtable` | Table name OR subquery in parentheses |
| `query` | Explicit SQL query as alternative to `dbtable` |

### Write Options (df.write.jdbc)

| Parameter | Type | Notes |
|-----------|------|-------|
| `url` | String | JDBC connection URL |
| `table` | String | **Target table name** (positional arg 2) |
| `mode` | String | overwrite, append, ignore, error |
| `properties` | Dict | driver, user, password, etc. |
| `batchsize` | Int | Rows per batch write (NOT related to parallelism) |

---

## PART 11: SPARK CONNECT COMPARISON TABLE

| Aspect | Spark Connect | Classic (spark-submit) |
|--------|--------------|----------------------|
| Driver location | **Client machine** | Cluster (cluster mode) or client (client mode) |
| Dependency shipping | Not required | --jars, --py-files, --files |
| SparkContext / RDD | **NOT available** | Available |
| Multi-client | **Yes** | No (each submit = new app) |
| Error discovery | Server-side on action | During plan building |
| Data serialization | **Apache Arrow** | Java / Kryo |
| Connection string | `sc://host:port` | `spark://` or `yarn://` |
| Env var shortcut | `SPARK_REMOTE` | None |

---

## PART 12: PARQUET WRITE OPTIONS — VALID vs INVALID

| Option | Valid for Parquet Write? | Notes |
|--------|------------------------|-------|
| `compression` | ✓ Valid | Values: snappy, gzip, zstd, lz4, none |
| `maxRecordsPerFile` | ✓ Valid | Caps rows per output file |
| `partitionOverwriteMode` | ✓ Valid | dynamic vs static overwrite |
| `header` | ✗ CSV ONLY | Not a Parquet option |
| `mergeSchema` | ✗ Read option | For reading Parquet with schema evolution; Delta write too but not plain Parquet write |

---

## PART 13: PANDAS API ON SPARK QUICK REFERENCE

| Operation | Code | Notes |
|-----------|------|-------|
| Create from Parquet | `ps.read_parquet('/path')` or `.pandas_api()` | Both valid |
| Run SQL | `ps.sql('SELECT ...')` | Against registered temp views |
| Row-wise apply | `psdf.apply(func, axis=1)` | Supported; distributes across cluster |
| Column-wise apply | `psdf.apply(func, axis=0)` | Column as pd.Series |
| Rolling mean | `psdf['col'].rolling(n).mean()` | First n-1 rows are NaN |
| Side-by-side concat | `ps.concat([a, b], axis=1)` | Requires `ops_on_diff_frames=True` |
| Row stack | `ps.concat([a, b])` | Default axis=0 |
| Reset index on concat | `ps.concat([a, b], ignore_index=True)` | New integer index |

---

## PART 14: DEPLOYMENT MODES PORT CHEATSHEET

```
spark-submit --master spark://host:7077 \
             --deploy-mode cluster \
             --py-files utils.py \
             app.py

History Server: http://host:18080
Live App UI:    http://host:4040
Standalone UI:  http://host:8080
```

---

## 10-POINT EXAM SUCCESS CHECKLIST — ITERATION 4

| # | Check | Common Error |
|---|-------|-------------|
| 1 | `--py-files` vs `--files` | Using `--files` for Python modules (won't be importable) |
| 2 | History Server = port 18080 | Confusing with 4040 (live app) or 8080 (standalone UI) |
| 3 | `size(null)` = null in Spark 3+ | Answering 0 or -1 |
| 4 | `from_unixtime` returns StringType | Answering TimestampType |
| 5 | Disable broadcast join = -1 (NOT 0) | Using 0 which has different semantics |
| 6 | CBO join reorder needs TWO configs | Setting only `cbo.enabled = true` |
| 7 | `CACHE TABLE` is eager | Thinking it's lazy (CACHE LAZY TABLE is lazy) |
| 8 | `complete` mode requires aggregation | Applying it to non-aggregated queries |
| 9 | `df.getNumPartitions()` doesn't exist | Calling it on DataFrame instead of RDD |
| 10 | EXCEPT ALL vs EXCEPT: one-per-occurrence vs all | Confusing multiset vs set semantics |
