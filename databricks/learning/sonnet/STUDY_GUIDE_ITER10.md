# Study Guide — Iteration 10
## Databricks Certified Associate Developer for Apache Spark

**Source**: `spark-databricks-iteration-10.md`
**Questions**: 100 | Easy: 10 | Medium: 54 | Hard: 36
**Answer distribution**: 99 × B, **1 × A (Q76)** ← memorise this exception

---

## ⚠️ CRITICAL ALERT — Q76 Answer is A, NOT B

> **Q76**: Which config controls Parquet compression independently of the global codec?
> **Answer A**: `spark.sql.parquet.compression.codec` overrides `spark.io.compression.codec` for Parquet writes only; default is `snappy`.

Every other question in this iteration answers **B**. This is the single exception — do not let pattern-matching trick you on exam day.

---

## Topic 1 — Apache Spark Architecture (Q1–Q20)

### 1.1 Memory Management

#### Broadcast Join Threshold (Q1 — Easy)
- `spark.sql.autoBroadcastJoinThreshold` default = **10 MiB (10 485 760 bytes)**
- Tables at or below this size are automatically broadcast → BroadcastHashJoin
- Disable: set to `-1`
- AQE can also trigger runtime broadcast conversion based on actual shuffle sizes

#### Unified Memory Pool (Q2 — Medium)
| Config | Default | Role |
|---|---|---|
| `spark.memory.fraction` | 0.6 | Fraction of JVM heap forming the unified pool (above reserved ~300 MiB) |
| `spark.memory.storageFraction` | 0.5 | Soft floor below which storage won't be shrunk by execution pressure |

- **Lower `storageFraction`** → execution can claim more of the pool
- `(1 - fraction) × heap` = user memory
- `fraction × heap` = unified pool (storage + execution share freely)

#### Off-Heap Overhead (Q3 — Hard)
| Config | Behavior |
|---|---|
| `spark.executor.memoryOverheadFactor` (Spark 3.3+) | `max(factor × executor.memory, 384 MiB)` |
| `spark.executor.memoryOverhead` (absolute MiB) | **Takes precedence** if also set |

- Example: `factor=0.15`, `executor.memory=8g` → `max(0.15 × 8192, 384)` = **1228 MiB**
- If both set, `memoryOverhead` wins; `memoryOverheadFactor` is ignored

### 1.2 Compression & Codec (Q4 — Medium, Q76 — Hard)

| Config | Default | Scope |
|---|---|---|
| `spark.io.compression.codec` | `lz4` | Shuffle files, broadcast vars, serialized RDD partitions (global) |
| `spark.sql.parquet.compression.codec` | `snappy` | Parquet writes only — **overrides global** |

- Supported codecs: `lz4`, `lzf`, `snappy`, `zstd`, `none`, `gzip`, `brotli`, `lzo`
- Per-write override: `df.write.option("compression", "zstd")`
- Global enable/disable: `spark.shuffle.compress`, `spark.broadcast.compress`

### 1.3 Catalyst & Plan Optimization (Q5, Q9, Q13 — Hard; Q12 — Medium)

#### Exchange Reuse (Q5)
- `spark.sql.exchange.reuse=true` (default) enables `ReuseExchange` optimizer rule
- Replaces duplicate `ShuffleExchangeExec` nodes with `ReusedExchangeExec`
- The shuffle is computed **once**; its materialized output is consumed by both branches
- Valuable in self-joins and multi-branch aggregations

#### Catalyst Max Iterations (Q9)
- `spark.sql.optimizer.maxIterations` (default **100**)
- Error: `AnalysisException: Max iterations (100) reached for batch Resolution`
- Cause: deeply nested/correlated subqueries prevent plan convergence
- Fix: increase to 200–500

#### Plan Cache (Q13)
- `spark.sql.planCacheSize` (default **100**) = LRU cache for parsed+analysed logical plans from `spark.sql()` calls
- Cache hit skips parsing & analysis (but not optimization/planning)
- Increase for apps with many distinct repeated SQL strings

#### Parquet Filter Pushdown (Q12)
- `spark.sql.parquet.filterPushdown=true` (default)
- Parquet reader checks **row group min/max statistics** in file footer → skips non-matching row groups entirely
- Bloom filters (Parquet 1.12+) can further refine equality predicates

### 1.4 AQE Deep Dive (Q6, Q15, Q20 — various)

| AQE Config | Default | Purpose |
|---|---|---|
| `spark.sql.adaptive.enabled` | `true` (Spark 3.2+) | Master AQE switch |
| `spark.sql.adaptive.coalescePartitions.enabled` | `true` | Merge small post-shuffle partitions |
| `spark.sql.adaptive.coalescePartitions.minPartitionSize` | 1 MiB (Spark 3.2+) | **Floor size** — merging stops only when >= this |
| `spark.sql.adaptive.localShuffleReader.enabled` | `true` | After SMJ→BHJ, read shuffle locally |

- **`minPartitionSize` (Q6)**: prevents AQE stopping early with many sub-MiB partitions
- **`coalescePartitions` (Q15)**: `spark.sql.shuffle.partitions` is a **suggestion**, not a floor — AQE can go lower
- **`localShuffleReader` (Q20)**: after AQE converts SMJ → BHJ, executors read their **own local** shuffle files, eliminating cross-node fetch

### 1.5 Shuffle & External Shuffle Service (Q7 — Hard)
- `spark.shuffle.service.db.enabled=true` persists shuffle block registrations to **LevelDB**
- Survives ESS restart → jobs don't need full stage re-computation if files still on disk
- Default: `false`

### 1.6 Spark UI & Debugging (Q8 — Medium)
**Scheduler Delay** = time from TaskScheduler submitting task → executor begins executing
- Includes: task serialization, network transmission to executor, executor thread-pool queuing
- High values caused by: large captured closures, slow network, many concurrent task launches

### 1.7 SparkSession (Q10 — Medium)
- `SparkSession.newSession()` = shares `SparkContext` (cluster resources) + shares Spark defaults
- Isolated per session: **temp views, SQL configs, registered UDFs**
- Global temp views remain shared via `global_temp` database across all sessions

### 1.8 Parquet Schema Evolution (Q11 — Medium)
- `spark.sql.parquet.mergeSchema=true` (default false)
- Reads footer schema from **all** files → unions into merged schema
- Missing columns → `null`
- Per-read: `spark.read.option("mergeSchema", "true")`
- Cost: extra I/O to read all footers before scanning

### 1.9 Error Handling for File Reads (Q14 — Medium)
| Config | Default | Handles |
|---|---|---|
| `spark.sql.files.ignoreCorruptFiles` | `false` | Truncated/unparseable files → emit 0 rows |
| `spark.sql.files.ignoreMissingFiles` | `false` | File deleted after planning → skip silently |

- **Independent** — must enable each separately; no single `ignoreErrors` setting

### 1.10 SparkConf Priority (Q16 — Medium)
Priority (highest → lowest):
1. `SparkConf().set()` in code — **wins**
2. `spark-submit` flags (e.g., `--executor-memory 6g`)
3. `spark-defaults.conf`

### 1.11 Date/Time Parser Policy (Q17 — Hard)
| Value | Behaviour |
|---|---|
| `CORRECTED` (Spark 3.x default) | Strict Proleptic Gregorian; may return `null` for Spark 2.x-valid dates |
| `LEGACY` | Java `SimpleDateFormat` lenient — restores Spark 2.x compatibility |
| `EXCEPTION` | Throws on ambiguous inputs |

Config: `spark.sql.legacy.timeParserPolicy`

### 1.12 JSON Generator (Q18 — Medium)
- `spark.sql.jsonGenerator.ignoreNullFields=true` (default in Spark 3.x)
- Omits struct fields with `null` values from `to_json()` output and JSON file writes
- `false` → produces explicit `"field": null`

### 1.13 Data Source V1 vs V2 Routing (Q19 — Hard)
- `spark.sql.sources.useV1SourceList` = comma-separated format names forced onto V1 code path
- Removing a format enables its V2 `TableProvider` implementation
- Built-in formats like Parquet/ORC have both V1 and V2 implementations

---

## Topic 2 — Spark SQL (Q21–Q40)

### 2.1 Array Higher-Order Functions

| Function | Returns | Null/Empty handling |
|---|---|---|
| `F.transform(arr, func)` | Same-length array, elements transformed | Keeps all elements |
| `F.filter(arr, func)` | Variable-length array, elements where predicate=true | Drops non-matching; empty array `[]` if none match |
| `F.posexplode(arr)` | Two columns: `pos` (IntegerType, 0-based), `col` (element) | Drops null/empty rows |
| `F.posexplode_outer(arr)` | Same but preserves null/empty rows as `(null, null)` | Preserves |
| `F.explode(arr)` | One row per element | Drops null/empty rows |
| `F.explode_outer(arr)` | One row per element | Preserves null/empty as `null` element |
| `F.inline(arr_of_structs)` | One row per struct element, columns = struct fields | Drops null/empty |
| `F.inline_outer(arr_of_structs)` | Same but preserves | Preserves |

#### arrays_zip (Q25 — Hard)
- `F.arrays_zip(col_a, col_b)` → `ArrayType(StructType([StructField("a", ...), StructField("b", ...)]))`
- Field names = **input column names**
- Arrays of **different lengths** → shorter padded with `null` (unlike Python's `zip` which truncates)

#### slice (Q62 — Hard)
- `F.slice(arr, start, length)` — **1-based** indexing
- `start=-1` = last element, `start=1` = first element
- Truncates silently if `start + length > array length`
- Example: `slice(["a","b","c","d","e"], 2, 3)` → `["b","c","d"]`

#### element_at (Q32 — Hard, Q54 — Medium)
- **1-based** for arrays; negative = from end; `-1` = last element
- `[]` subscript is **0-based**
- Returns `null` for missing key/out-of-range index in non-ANSI mode
- `F.try_element_at` (Spark 3.4+) = always null-safe regardless of ANSI mode

### 2.2 Map Higher-Order Functions (Q37, Q40, Q44)

| Function | Purpose |
|---|---|
| `F.map_filter(map, lambda k, v: bool)` | Remove entries where predicate = false |
| `F.map_keys(map)` | → `ArrayType(key_type)` — **non-deterministic order** |
| `F.map_values(map)` | → `ArrayType(val_type)` — index `i` matches `map_keys` index `i` |
| `F.map_entries(map)` | → `ArrayType(StructType([key, value]))` — enables array HOFs on maps |
| `F.map_from_entries(arr_of_structs)` | Inverse of `map_entries` |

### 2.3 JSON Functions (Q27–Q29)

| Function | Input | Output | Notes |
|---|---|---|---|
| `F.from_json(col, schema)` | JSON string | Struct/Map/ArrayType | Schema must be `ArrayType(...)` for JSON arrays |
| `F.to_json(col)` | Struct/Map/Array | StringType JSON | Respects `ignoreNullFields` |
| `F.get_json_object(col, "$.path")` | JSON string | **StringType** always | Single value; null if path missing |
| `F.json_tuple(col, *fields)` | JSON string | Multiple StringType cols (`c0`, `c1`, ...) | **Parses once** for all fields — more efficient |
| `F.schema_of_json(lit(sample))` | JSON literal | DDL schema string | Not a StructType object |
| `F.schema_of_csv(lit(sample))` | CSV literal | DDL schema string | Fields named `_c0`, `_c1`, ... |

**Key traps:**
- `get_json_object` always returns `StringType` — never numeric
- `from_json` with `StructType` schema fails on JSON arrays — must use `ArrayType(element_schema)`
- `json_tuple` output columns are positional: `c0`, `c1`, `c2`

### 2.4 String Functions (Q30–Q31, Q33–Q35, Q38)

| Function | Behaviour |
|---|---|
| `F.concat_ws(sep, *cols)` | Joins with separator; **skips nulls** (no double separator) |
| `F.split(col, pattern, limit)` | Regex split; `limit=n` = at most `n-1` splits, `n` elements total |
| `F.base64(col)` | `BinaryType` → `StringType` (Base64) |
| `F.unbase64(col)` | `StringType` → `BinaryType` |
| `F.hex(col)` | Int/Long/Binary/String → `StringType` hex |
| `F.unhex(col)` | Hex `StringType` → `BinaryType` (not an integer!) |
| `F.levenshtein(l, r)` | Edit distance as `IntegerType`; `<= 2` for typo detection |
| `F.format_string(fmt, *cols)` | Printf-style; handles type conversion automatically |
| `F.sentences(text)` | → `ArrayType(ArrayType(StringType()))` — array of sentence arrays |

**`split` with limit trap (Q31):**
`split("/usr/local/bin/spark", "/", 3)` → `["", "usr", "local/bin/spark"]`
- Leading empty string before first `/` is retained

### 2.5 Date/Time Functions (Q26, Q39)

| Function | Return type | Notes |
|---|---|---|
| `to_date(col, format)` | `DateType` | No time component, no timezone issues |
| `to_timestamp(col, format)` | `TimestampType` | Timezone-aware |
| `F.dayofyear(date)` | `IntegerType` 1–366 | 2024 is leap year; March 1 = day **61** |

**Leap year check**: divisible by 4, not by 100 unless also by 400

### 2.6 Aggregate/Utility (Q63–Q64)

| Function | Distribution | Null handling |
|---|---|---|
| `F.greatest(*cols)` | Row-wise max across columns | Ignores nulls; null only if **all** null |
| `F.least(*cols)` | Row-wise min across columns | Same |
| `F.rand(seed)` | Uniform [0.0, 1.0) | Fixed seed = reproducible |
| `F.randn(seed)` | Standard normal (mean=0, σ=1) | Fixed seed = reproducible |

---

## Topic 3 — DataFrame/Dataset API (Q41–Q70)

### 3.1 New Methods by Spark Version

| Version | Method | Purpose |
|---|---|---|
| 3.0 | `df.transform(func)` | Fluent pipeline chaining — sugar for `func(df)` |
| 3.1 | `df.unionByName(other, allowMissingColumns=True)` | Schema union with null-fill |
| 3.3 | `df.withColumns(dict)` | Add/replace multiple columns in one projection |
| 3.3 | `df.withColumnsRenamed(dict)` | Batch rename |
| 3.4 | `df.unpivot(ids, values, varCol, valCol)` | Wide → long; also available as `df.melt` |
| 3.4 | `F.try_element_at(col, index)` | Always null-safe element access |

### 3.2 Union Operations (Q46, Q51)

| Method | Column alignment | Missing columns |
|---|---|---|
| `df.union(other)` | **By position** — silent wrong-value pairing if order differs | Error if count differs |
| `df.unionByName(other)` | **By name** | Error unless `allowMissingColumns=True` |
| `df.unionByName(other, allowMissingColumns=True)` | By name | Missing → filled with `null` |

**Always prefer `unionByName`** when combining DataFrames from different sources.

### 3.3 Struct Operations (Q43, Q44, Q45, Q52, Q68)

| Operation | Code |
|---|---|
| Create struct | `F.struct(col1.alias("f1"), col2.alias("f2"))` |
| Create with explicit names | `F.named_struct(lit("x"), lit(3.0), lit("y"), lit(4.0))` |
| Access nested field | `df.select("address.city")` or `F.col("address.city")` — identical |
| Field name with literal dot | Use backticks: `F.col("`field.name`")` |
| Map → array of structs | `F.map_entries(map_col)` → `ArrayType(StructType([key, value]))` |
| Array of structs → columns | `F.inline(arr_of_structs)` — one row per element, struct fields become columns |

### 3.4 Statistical Functions (Q47, Q55, Q57)

| Method | Returns | Purpose |
|---|---|---|
| `df.stat.bloomFilter(col, n, fpp)` | `BloomFilter` object | Set-membership: no false negatives, `fpp` false positives |
| `df.stat.countMinSketch(col, eps, confidence, seed)` | `CountMinSketch` object | Frequency estimation: upper-bound with bounded error |
| `df.describe(*cols)` | DataFrame | Fixed 5 stats: count, mean, stddev, min, max |
| `df.summary(*stats)` | DataFrame | Flexible: + percentiles `"25%"`, `"99%"`, etc. |

**BloomFilter trap**: `bloomFilter()` returns a `BloomFilter` object, NOT a filtered DataFrame.

### 3.5 Window Functions (Q58–Q60)

| Function | Formula | First row value |
|---|---|---|
| `F.percent_rank()` | `(rank − 1) / (n − 1)` | **0.0** |
| `F.cume_dist()` | `rows_leq_current / n` | **> 0** (always, at minimum = 1/n) |
| `F.ntile(n)` | Assigns bucket 1–n | Bucket 1 = lowest-ordered rows |
| `F.lag(col, offset, default)` | Value from `offset` rows before | Returns `default` if no preceding row |
| `F.lead(col, offset, default)` | Value from `offset` rows after | Returns `default` if no following row |

**ntile bucket sizes**: For 10 rows, `ntile(4)` → buckets of 3, 3, 2, 2 (larger first)

### 3.6 Avro / Write Options (Q49, Q50, Q70)

| Topic | Key fact |
|---|---|
| Avro format | **Separate package** — add `org.apache.spark:spark-avro_2.12:x.x.x` |
| `timestampFormat` option | Controls `TimestampType` → string serialization in CSV/JSON writes |
| `dateFormat` option | Controls `DateType` → string serialization |
| `insertInto(table)` | Inserts **by position** — column order must match table schema |
| `saveAsTable(table, append)` | Inserts **by name** — safe regardless of column order |

### 3.7 Other DataFrame API (Q41, Q53, Q56, Q61, Q65, Q67)

| Method / Topic | Key fact |
|---|---|
| `df.transform(func)` | Sugar for `func(df)`; enables: `df.filter(...).transform(f1).transform(f2)` |
| `createGlobalTempView` | Raises `TempTableAlreadyExistsException` if name taken |
| `createOrReplaceGlobalTempView` | Safe to call repeatedly |
| `df.explain(mode="codegen")` | Shows generated Java source from whole-stage codegen |
| Other modes: `simple`, `extended`, `cost`, `formatted` | |
| `df.withColumns(dict)` (3.3+) | Single projection vs chained `withColumn` overhead |
| `df.na.replace(val, None, subset)` | Converts specific value to null (inverse of `fillna`) |
| Self-join alias (Q67) | `df.alias("a").join(df.alias("b"), ...)` — disambiguates column lineage |

---

## Topic 4 — Troubleshooting & Tuning (Q71–Q80)

### 4.1 AQE Version History (Q71)
- Spark 3.0: AQE introduced (default `false`)
- Spark 3.1: AQE default still `false`
- **Spark 3.2+**: AQE default changed to **`true`** — partition coalescing now automatic

### 4.2 Configuration Quick Reference

| Config | Default | Purpose |
|---|---|---|
| `spark.sql.mapKeyDedupPolicy` | `EXCEPTION` | `LAST_WIN` = keep last value for duplicate map keys |
| `spark.sql.columnNameOfCorruptRecord` | `_corrupt_record` | Column name in PERMISSIVE mode for bad records |
| `spark.sql.optimizer.inSetSwitchThreshold` | 10 | List size at which `IN(...)` → `HashSet` O(1) lookup |
| `spark.sql.session.timeZone` | JVM default | Affects timestamp display + timezone-sensitive functions |
| `spark.sql.parquet.compression.codec` | `snappy` | **(Answer A in Q76)** Parquet-only compression |
| `spark.sql.debug.maxToStringFields` | 25 | Max fields in plan/schema toString output |
| `spark.sql.execution.arrow.maxRecordsPerBatch` | 10 000 | Rows per Arrow batch in `toPandas()` / `createDataFrame()` |
| `spark.sql.repl.eagerEval.enabled` | `false` | Auto-render DataFrame as HTML in Jupyter/Zeppelin |
| `spark.sql.statistics.fallBackToHdfs` | `false` | Estimate table size from HDFS when Hive stats absent |

### 4.3 Key Tuning Scenarios

**PERMISSIVE mode corrupt records (Q73):**
- Schema must include a field named `_corrupt_record` (or custom name) as `StringType`
- Without this field in the schema, malformed records are stored in a hidden column

**Timestamp timezone (Q75):**
- `UTC 12:00` with `session.timeZone=America/New_York` (UTC-4 EDT) → displayed as `08:00`
- Internally stored as microseconds since epoch; display converts to session timezone

**HashSet IN-list (Q74):**
- `inSetSwitchThreshold=10` → lists of 11+ values use `InSet` (HashSet O(1))
- 10 or fewer → `In` (sequential O(n) comparison)

**HDFS statistics fallback (Q80):**
- `spark.sql.statistics.fallBackToHdfs=true` → calls `fs.getContentSummary()` for size estimate
- Enables broadcast join without `ANALYZE TABLE` — less accurate but non-null
- Adds planning overhead for tables with many files

---

## Topic 5 — Structured Streaming (Q81–Q90)

### 5.1 Trigger Behavior (Q81 — Medium)

`processingTime("30 seconds")`:
- If batch finishes in < 30s → wait remainder before next batch
- If batch takes > 30s → next batch starts **immediately** after current completes
- **Never concurrent** — two batches never run simultaneously

### 5.2 Stateful Operations (Q82, Q87)

**dropDuplicates + watermark (Q82):**
- Without watermark → state grows **unbounded**
- With watermark → keys with event_time older than `max_event_time − delay` are evicted
- Late duplicates after watermark delay are **not deduplicated**

**RocksDB state store (Q87):**
- `spark.sql.streaming.stateStore.providerClass=org.apache.spark.sql.execution.streaming.state.RocksDBStateStoreProvider`
- Off-heap storage → no JVM GC pressure for large state
- Available in OSS Spark 3.2+ (separate module) and Databricks Runtime

### 5.3 Output & Sources (Q83, Q84, Q86, Q88, Q89)

| Topic | Key fact |
|---|---|
| `writeStream.toTable(name)` (3.1+) | Catalog-managed write; updates metadata; vs `start(path)` which doesn't |
| `processAllAvailable()` | **Test only** — blocks until all current data processed; not for production |
| Rate source columns | `timestamp` (TimestampType) + `value` (LongType, 0-based counter) |
| Memory sink | Results in temp view named by `queryName`; query with `spark.sql("SELECT * FROM name")` |
| `spark.sql.streaming.numShufflePartitions` | Streaming-only shuffle partition override (doesn't affect batch SQL) |

### 5.4 Kafka Integration (Q90 — Hard)

| Scenario | `startingOffsets` behaviour |
|---|---|
| First start (no checkpoint) | Used as specified (`"earliest"`, `"latest"`, or per-partition JSON) |
| Restart with valid checkpoint | **Ignored** — resumes from checkpoint committed offsets |

- To replay data: delete the checkpoint directory first

### 5.5 Stream-Static Join (Q85 — Hard)
- Static side is **re-evaluated each micro-batch** (if based on live source, changes are visible)
- **No watermark needed** — no state store required
- Contrast: stream-stream join requires watermarks on **both** sides

---

## Topic 6 — Spark Connect (Q91–Q95)

### 6.1 Session Creation (Q91 — Easy)
```python
spark = SparkSession.builder.remote("sc://host.example.com:15002").getOrCreate()
```
- Uses gRPC (`sc://` scheme)
- No local JVM, `SparkContext`, or executors on client side
- `spark.sparkContext` raises `PySparkNotImplementedError`
- Default port: **15002** (`spark.connect.grpc.binding.port`)

### 6.2 Artifact Distribution (Q92 — Medium)
```python
spark.addArtifact("utils.py")           # replaces sc.addFile()
spark.addArtifact("custom_funcs.jar")   # replaces sc.addJar()
```
- Uploaded over gRPC channel, cached on server, distributed to executors

### 6.3 Server Management (Q93, Q94 — Hard, Medium)
```bash
# Start server with packages
./sbin/start-connect-server.sh --packages "io.delta:delta-spark_2.12:3.0.0"
# Stop
./sbin/stop-connect-server.sh
```
- Accepts all `spark-submit` arguments: `--packages`, `--jars`, `--conf`, `--num-executors`
- Default port: **15002**

### 6.4 Session Configuration (Q95 — Medium)
- `spark.conf.set(key, value)` → serialized as gRPC request context
- Scoped to **this client's session only**
- Static server-startup configs cannot be overridden per-session

---

## Topic 7 — Pandas API on Spark (Q96–Q100)

### 7.1 Reshape Operations (Q96, Q97)
```python
# Wide → long (mirrors pandas.melt)
psdf.melt(id_vars=["user_id"], value_vars=["q1","q2","q3"], var_name="quarter", value_name="score")

# Aggregated pivot
psdf.pivot_table(values="sales", index="region", columns="product", aggfunc="sum")
# fill_value replaces NaN for missing combinations
```

### 7.2 Join (Q98 — Hard)
- `ps.DataFrame.merge()` supports: `inner`, `left`, `right`, `outer`, `cross`, `left_semi`, `left_anti`
- **Fully distributed** — no driver collection; translates to native Spark join

### 7.3 Column Assignment (Q99 — Medium)
| Style | Returns | Mutates? |
|---|---|---|
| `psdf.assign(col=lambda df: expr)` | **New** DataFrame | No (functional) |
| `psdf["col"] = value` | Void | **Yes** (pandas-style in-place) |

`assign` enables method chaining; multiple columns can reference each other in order.

### 7.4 explode (Q100 — Medium)
- `psdf.explode("tags")` follows **pandas** semantics
- Null/empty list rows → produce a row with `NaN` (preserved)
- Different from `F.explode` (which **drops** null/empty rows)
- Same as `F.explode_outer` semantics
- Under the hood: Pandas API on Spark uses `explode_outer`

---

## Summary: Highest-Yield Facts

| # | Fact | Q |
|---|---|---|
| 1 | **Q76 answer is A** — `spark.sql.parquet.compression.codec` | 76 |
| 2 | `autoBroadcastJoinThreshold` default = 10 MiB | 1 |
| 3 | `memory.fraction`=0.6, `memory.storageFraction`=0.5 | 2 |
| 4 | `memoryOverhead` (absolute) **beats** `memoryOverheadFactor` | 3 |
| 5 | `lz4` is global default; `snappy` is Parquet default | 4, 76 |
| 6 | AQE default changed `false→true` in **Spark 3.2** | 71 |
| 7 | `SparkConf` programmatic > submit flags > defaults file | 16 |
| 8 | `LEGACY` timeParserPolicy restores Spark 2.x date parsing | 17 |
| 9 | `element_at` = 1-based; `[]` subscript = 0-based | 32 |
| 10 | `get_json_object` always returns `StringType` | 28 |
| 11 | `json_tuple` parses JSON **once** for multiple fields | 29 |
| 12 | `from_json` needs `ArrayType(schema)` for JSON arrays | 66 |
| 13 | `union` = by position; `unionByName` = by name | 51 |
| 14 | `insertInto` = by position; `saveAsTable` = by name | 70 |
| 15 | `bloomFilter()` returns a BloomFilter object, not a DataFrame | 47 |
| 16 | `describe()` = 5 stats only; `summary()` adds percentiles | 57, 69 |
| 17 | `percent_rank()` first row = 0.0; `cume_dist()` first row > 0 | 58 |
| 18 | `startingOffsets` ignored when checkpoint exists (Kafka) | 90 |
| 19 | `processAllAvailable()` is test-only | 84 |
| 20 | `psdf.explode()` preserves null/empty as NaN (unlike `F.explode`) | 100 |
