# Databricks Certified Associate Developer — Quick Reference (Iteration 2)

**Edition**: Iteration 2 | **Difficulty**: 20E / 60M / 20H | **Answer Types**: 81 single / 19 multi

---

## 1. Memory Anchors — 35 Must-Know Facts (5 per Topic)

### Topic 1 — Architecture

1. **`local[*]`** runs in a single JVM using **all available logical CPU cores**
2. **`--deploy-mode cluster`**: Driver runs on a worker node; submitting machine can disconnect safely
3. **Standalone master port = 7077** (not 4040 which is Spark UI)
4. **`df.cache()` default = `MEMORY_AND_DISK`** (RDD `.cache()` default = `MEMORY_ONLY`)
5. **Accumulator reads inside Tasks return the initial value** (e.g., `0`); only the Driver sees the final

### Topic 2 — Spark SQL

6. **`createGlobalTempView` raises `AnalysisException`** if name exists; use `createOrReplaceGlobalTempView` to upsert
7. **`F.lit(100)`** creates a Column constant; **`F.to_json(col)`** returns `StringType` (JSON string)
8. **`concat_ws` skips null elements** silently — `['hello', None, 'world']` → `'hello-world'`
9. **`percent_rank` range = [0, 1]** (first row = 0); **`cume_dist` range = (0, 1]** (minimum = 1/N, never 0)
10. **`ntile(k)` uneven split**: extra rows fill **earlier** tiles (tile 1 gets the extras)

### Topic 3 — DataFrame API

11. **`spark.range(0,10)` schema**: one column named `id` of `LongType`
12. **`spark.read.text()` schema**: one column named `value` of `StringType` (one row per file line)
13. **`col != None` does NOT work** for null checks — use `isNull()`/`isNotNull()`
14. **`monotonically_increasing_id()`**: unique + increasing but **not sequential** (gaps between partitions)
15. **`mergeSchema=True`** required when reading Parquet files with different schemas

### Topic 4 — Troubleshooting

16. **`cache()` is lazy** — materialised during the **next action**, not when `.cache()` is called
17. **`MEMORY_ONLY` drops partitions** that don't fit (no spill); lineage recomputes them on access
18. **10 GB heap × `spark.memory.fraction=0.6`** = 6 GB Spark Memory (Execution + Storage)
19. **`sortWithinPartitions` = no shuffle** (local sort per partition); **`orderBy` = full shuffle** (global sort)
20. **`spark.sparkContext.setLogLevel('ERROR')`** — correct runtime log level API

### Topic 5 — Structured Streaming

21. **`writeStream.start()` returns `StreamingQuery`** (not DataFrame, not None)
22. **`rate` source schema**: `timestamp TIMESTAMP, value BIGINT` (two columns)
23. **`availableNow=True`** processes all data in multiple micro-batches then stops; **`once=True`** uses one batch
24. **`complete` output mode** requires stateful aggregation; rewrites full result on every trigger
25. **`awaitTermination()`** must be called; without it, main thread exit kills the streaming query

### Topic 6 — Spark Connect

26. **Spark Connect default gRPC port = 15002** (Standalone master = 7077; Spark UI = 4040)
27. **Classic Spark uses Py4J**; **Spark Connect uses gRPC over HTTP/2** with Protobuf logical plans
28. **Client crash ≠ job failure** in Spark Connect — Driver runs on cluster, survives client crash
29. **Results returned as Apache Arrow record batches** (columnar; efficient)
30. **No RDD API** from Spark Connect client — only DataFrame/SQL API available

### Topic 7 — Pandas API on Spark

31. **`ps.from_pandas(pdf)`** — correct conversion from native pandas to `pyspark.pandas`
32. **`psdf.to_spark()`** returns a **PySpark DataFrame** (distributed; does NOT collect to driver)
33. **`databricks.koalas` import = deprecated** since Spark 3.2 (use `pyspark.pandas`)
34. **`'distributed-sequence'` is the default index type** (unique, partition-based; no global sort)
35. **`'sequence'` index requires a global sort** → expensive at scale; avoid unless strictly necessary

---

## 2. Master Configuration Reference

| Property | Default | Controls |
|----------|---------|---------|
| `spark.sql.shuffle.partitions` | 200 | Partitions after **DataFrame/SQL** shuffle |
| `spark.default.parallelism` | Cluster-dependent | Default partitions for **RDD** operations only |
| `spark.sql.files.maxPartitionBytes` | 128 MB | Max input partition size from files |
| `spark.sql.autoBroadcastJoinThreshold` | 10 MB | Auto-broadcast table size threshold |
| `spark.memory.fraction` | 0.6 | JVM heap fraction for Spark Memory region |
| `spark.executor.memory` | 1g | JVM heap per Executor |
| `spark.executor.memoryOverhead` | 10% of mem, min 384 MB | Off-heap (OS, Python workers, native libs) |
| `spark.executor.cores` | 1 (YARN) | CPU cores per Executor |
| `spark.dynamicAllocation.enabled` | false | Enable Dynamic Resource Allocation |
| `spark.speculation` | false | Enable speculative execution for straggler Tasks |
| `spark.sql.adaptive.enabled` | true (Spark 3.0+) | Enable Adaptive Query Execution |
| `spark.sql.parquet.mergeSchema` | false | Auto-merge Parquet schemas on read |

---

## 3. Storage Levels Reference

| Level | Memory | Disk | Serialised | On Memory Overflow |
|-------|--------|------|-----------|-------------------|
| `MEMORY_AND_DISK` | ✓ | ✓ (spill) | No | Spill to disk |
| `MEMORY_ONLY` | ✓ | ✗ | No | **Drop partition** (recompute) |
| `MEMORY_ONLY_SER` | ✓ (binary) | ✗ | Yes | Drop partition |
| `MEMORY_AND_DISK_SER` | ✓ (binary) | ✓ (binary) | Yes | Spill to disk |
| `DISK_ONLY` | ✗ | ✓ | Yes | N/A |

**`df.cache()` default = `MEMORY_AND_DISK`**
**RDD `.cache()` default = `MEMORY_ONLY`**

---

## 4. Deploy Mode Comparison

| Aspect | `client` | `cluster` |
|--------|----------|-----------|
| Driver location | Submitting machine | Worker node in cluster |
| `spark-submit` default | **Yes** | No |
| Databricks default | No | **Yes** |
| Machine crash kills job? | **Yes** (Driver dies) | **No** (Driver on cluster) |
| Best for | Interactive dev, debugging | Production, automated jobs |
| Log location | Submitter stdout | Worker node logs |

---

## 5. Window Function Comparison Table

| Function | Formula | Range | Min value |
|----------|---------|-------|----------|
| `row_number()` | Sequential 1…N | [1, N] | 1 |
| `rank()` | Position (with gaps) | [1, N] | 1 |
| `dense_rank()` | Position (no gaps) | [1, D] | 1 |
| `percent_rank()` | `(rank-1)/(N-1)` | [0, 1] | **0** |
| `cume_dist()` | `rank/N` | (0, 1] | `1/N` |
| `ntile(k)` | Bucket assignment | [1, k] | 1 |
| `lag(col, n)` | Previous Nth row | — | null if n rows from start |
| `lead(col, n)` | Next Nth row | — | null if n rows from end |

**`ntile` distribution rule:** When N rows ÷ k tiles has remainder R, the first **R tiles** each get one extra row.

---

## 6. Join Types Quick Reference

| Type | Returns | Right Cols Included? |
|------|---------|---------------------|
| `inner` (default) | Matching rows only | Yes |
| `left` | All left + matched right | Yes (null where no match) |
| `right` | All right + matched left | Yes (null where no match) |
| `full` | All rows from both | Yes (null where no match) |
| `left_semi` | Left rows **with** match | **No** |
| `left_anti` | Left rows **without** match | **No** |
| `cross` | Cartesian product | Yes |

---

## 7. SQL Functions Type Reference

| Function | Input | Return Type |
|----------|-------|-------------|
| `F.split(col, pattern)` | StringType | `ArrayType(StringType)` |
| `F.to_json(col)` | Struct/Map/Array | `StringType` |
| `F.date_format(col, fmt)` | Date/Timestamp | `StringType` |
| `F.datediff(end, start)` | Date, Date | `IntegerType` |
| `F.date_add(col, n)` | Date | `DateType` |
| `F.current_timestamp()` | — | `TimestampType` |
| `F.lit(value)` | Python scalar | Column (matches value type) |
| `F.approx_count_distinct(col)` | Any | `LongType` |
| `F.count('*')` | — | `LongType` |
| `F.monotonically_increasing_id()` | — | `LongType` |
| `F.array_contains(col, val)` | `ArrayType`, scalar | `BooleanType` |
| `F.coalesce(*cols)` | Multiple | Same as input |

---

## 8. Streaming Source Comparison

| Source | Fault-Tolerant | Replay | Schema | Use For |
|--------|----------------|--------|--------|---------|
| Kafka | Yes | Yes (offsets) | Binary/String | Production |
| Delta Lake | Yes | Yes (versions) | Enforced | Production |
| `rate` | N/A | N/A | timestamp+value | Testing |
| `socket` | **No** | **No** | value STRING | **Dev only** |

---

## 9. Streaming Output Mode Reference

| Mode | Query Type | Behaviour |
|------|-----------|-----------|
| `append` | Stateless / watermarked aggs | New final rows only |
| `update` | Any | Changed rows since last trigger |
| `complete` | **Stateful aggs required** | Full result table every trigger |

---

## 10. Pandas API Conversion Reference

| Operation | Code | Notes |
|-----------|------|-------|
| pandas → ps | `ps.from_pandas(pdf)` | Distributed DF |
| ps → PySpark | `psdf.to_spark()` | Returns PySpark DataFrame |
| PySpark → ps | `sdf.pandas_api()` | Distributed ps DF |
| ps → pandas | `psdf.to_pandas()` | Collects to driver — risky at scale |
| Set index type | `ps.set_option('compute.default_index_type', 'sequence')` | Global setting |

---

## 11. Trigger Modes Reference

| Trigger | Behaviour | Production? |
|---------|-----------|------------|
| `processingTime='N seconds'` | Micro-batch every N seconds | Yes |
| `once=True` | All data in ONE micro-batch, then stop | Batch backfill |
| `availableNow=True` | All data in MULTIPLE batches, then stop (3.3+) | Preferred backfill |
| `continuous='N seconds'` | Experimental low-latency | Experimental only |

---

## 12. Spark Connect vs Classic Spark

| Feature | Classic Spark | Spark Connect |
|---------|--------------|---------------|
| Client-Driver transport | Py4J socket | **gRPC / HTTP/2** |
| Driver location | Application process | Cluster |
| Client crash → job fail? | **Yes** | **No** |
| RDD API | Available | **Not available** |
| Result format | Python objects | **Apache Arrow batches** |
| Default port | N/A | **15002** |
| Connection string | `spark://host:7077` | `sc://host:15002` |
| Multi-language | Python/Scala/Java | Any gRPC language |

---

## 13. Write Modes — Preservation Table

| Mode | If path/table exists... | Existing data preserved? |
|------|------------------------|--------------------------|
| `overwrite` | Deletes and rewrites | **No** |
| `append` | Adds new data alongside | **Yes** |
| `ignore` | Does nothing (skip silently) | **Yes** |
| `error` | Raises exception | **Yes** (but throws error) |

---

## 14. Null Filtering Cheatsheet

```python
# VALID approaches to filter not-null
df.filter(col('email').isNotNull())          # ✓
df.filter(~col('email').isNull())             # ✓
df.na.drop(subset=['email'])                  # ✓
df.dropna(subset=['email'])                   # ✓

# INVALID — Python None comparison doesn't work
df.filter(col('email') != None)              # ✗ — always True (never filters)
df.filter(col('email') !== None)             # ✗ — syntax error
```

---

## 15. 10-Point Exam Success Checklist

- [ ] **1. `cache()` is LAZY** — nothing materialises until the next action. Don't assume data is cached after calling `.cache()` alone.
- [ ] **2. `df.cache()` default = `MEMORY_AND_DISK`** — NOT `MEMORY_ONLY`. RDD cache is `MEMORY_ONLY`. Don't mix them up.
- [ ] **3. `when()` without `otherwise()` returns null** for non-matching rows — not an error, not zero.
- [ ] **4. `col != None` is a Python trap** — use `isNotNull()` or `isNull()` for null checks in Spark.
- [ ] **5. `union()` is by position; `unionByName()` is by name** — using `union()` when schemas differ by column order produces silently wrong results.
- [ ] **6. `monotonically_increasing_id()` is NOT sequential** — guaranteed unique and increasing, but gaps exist between partitions.
- [ ] **7. Accumulator reads inside Tasks return the initial value** — only the Driver reads the final accumulated total.
- [ ] **8. Spark Connect gRPC port = 15002** — not 7077 (Standalone), not 4040 (Spark UI).
- [ ] **9. `'sequence'` index in pandas-on-Spark requires a global sort** (full shuffle) — expensive at scale. Default is `'distributed-sequence'`.
- [ ] **10. `lead()`/`lag()` on boundary rows return null** — `lag()` on first row = null, `lead()` on last row = null.
