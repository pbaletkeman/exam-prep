# Quick Reference — Iteration 10
## Spark / Databricks Exam Prep

> **Pattern alert**: 99 of 100 answers are **B**. The sole exception is **Q76 → Answer A**.

---

## ⚠️ Q76 EXCEPTION — Answer is A

> `spark.sql.parquet.compression.codec` (default `snappy`) overrides `spark.io.compression.codec` for Parquet writes only.
> Valid options: `none`, `uncompressed`, `snappy`, `gzip`, `lzo`, `brotli`, `lz4`, `zstd`
> Per-write override: `df.write.option("compression", "zstd")`

---

## TOPIC 1: Apache Spark Architecture (Q1–Q20)

### Memory
| Config | Default | What it does |
|---|---|---|
| `spark.sql.autoBroadcastJoinThreshold` | **10 MiB** | Auto-broadcast when table ≤ this size; `-1` disables |
| `spark.memory.fraction` | 0.6 | Unified pool = `0.6 × heap` (above ~300 MiB reserved) |
| `spark.memory.storageFraction` | 0.5 | Soft floor for storage within unified pool |
| `spark.executor.memoryOverheadFactor` | 0.1 | Off-heap = `max(factor × mem, 384 MiB)`; **overridden by `memoryOverhead`** |

### Compression
| Config | Default |
|---|---|
| `spark.io.compression.codec` | `lz4` (global: shuffle, broadcast, RDD) |
| `spark.sql.parquet.compression.codec` | `snappy` (Parquet only — **Q76 answer A**) |

### AQE
| Config | Spark 3.1 | Spark 3.2+ |
|---|---|---|
| `spark.sql.adaptive.enabled` | `false` | **`true`** ← migration change (Q71) |

| Config | Default | Purpose |
|---|---|---|
| `spark.sql.adaptive.coalescePartitions.minPartitionSize` | 1 MiB | Floor: AQE keeps merging until ≥ this (Q6) |
| `spark.sql.adaptive.localShuffleReader.enabled` | `true` | After SMJ→BHJ: read shuffle files locally (Q20) |
| `spark.sql.exchange.reuse` | `true` | Replace duplicate shuffles with `ReusedExchangeExec` (Q5) |

### Catalyst & Plans
| Config | Default | Purpose |
|---|---|---|
| `spark.sql.optimizer.maxIterations` | 100 | Max Catalyst rule-batch iterations; increase for complex queries (Q9) |
| `spark.sql.planCacheSize` | 100 | LRU cache for parsed+analysed SQL plans (Q13) |

### Files & Formats
| Config | Default | Behaviour |
|---|---|---|
| `spark.sql.files.ignoreCorruptFiles` | `false` | Skip unreadable files (Q14) |
| `spark.sql.files.ignoreMissingFiles` | `false` | Skip files deleted after planning (Q14) |
| `spark.sql.parquet.mergeSchema` | `false` | Union schemas from all Parquet files; missing cols → `null` (Q11) |
| `spark.sql.parquet.filterPushdown` | `true` | Skip Parquet row groups via min/max stats (Q12) |

### Other Architecture
| Topic | Fact |
|---|---|
| SparkConf priority | Programmatic > `--submit-flags` > `spark-defaults.conf` (Q16) |
| `SparkSession.newSession()` | Shares `SparkContext`; isolates temp views, SQL configs, UDFs (Q10) |
| Global temp views | Shared across all sessions via `global_temp` DB |
| `spark.sql.legacy.timeParserPolicy` | `CORRECTED` (3.x default) vs `LEGACY` (Spark 2.x behaviour) (Q17) |
| `spark.sql.jsonGenerator.ignoreNullFields` | `true` in Spark 3.x — omits null fields from `to_json` output (Q18) |
| `spark.sql.sources.useV1SourceList` | CSV of format names forced to V1 code path (Q19) |
| `spark.shuffle.service.db.enabled` | `false` default; `true` = LevelDB persistence for ESS state (Q7) |
| Scheduler delay | Task submit → executor begin executing; caused by large closures/network (Q8) |

---

## TOPIC 2: Spark SQL (Q21–Q40)

### Array HOFs
| Function | Output | Null/Empty row |
|---|---|---|
| `F.transform(arr, func)` | Same-length array, transformed | Keeps all |
| `F.filter(arr, func)` | Variable-length array (subset) | Keeps row; empty array `[]` |
| `F.explode(arr)` | One row per element | **Drops** null/empty rows |
| `F.explode_outer(arr)` | One row per element | **Preserves** → `null` element |
| `F.posexplode(arr)` | `pos` (0-based Int) + `col` columns | Drops null/empty |
| `F.inline(arr_of_structs)` | One row per struct; fields → columns | Drops null/empty |
| `F.inline_outer(arr_of_structs)` | Same | Preserves |
| `F.arrays_zip(a, b)` | `ArrayType(StructType([a, b]))` | Shorter padded with `null` |
| `F.slice(arr, start, length)` | Sub-array — **1-based** start | `start=-1` = last element |
| `F.element_at(arr, idx)` | Element — **1-based**, `-1` = last | `null` if out of range (non-ANSI) |

### Map HOFs
| Function | Output |
|---|---|
| `F.map_filter(map, lambda k, v: bool)` | MapType (filtered entries) |
| `F.map_keys(map)` | ArrayType(key) — **order non-deterministic** |
| `F.map_values(map)` | ArrayType(val) — index i matches map_keys i |
| `F.map_entries(map)` | `ArrayType(StructType([key, value]))` |

### JSON Functions
| Function | Returns | Key trap |
|---|---|---|
| `F.get_json_object(col, "$.path")` | **StringType always** | Numeric JSON values → string |
| `F.json_tuple(col, *fields)` | Multiple StringType (`c0`, `c1`...) | Parses once → more efficient |
| `F.from_json(col, schema)` | Typed struct/map/array | Use `ArrayType(schema)` for JSON arrays |
| `F.to_json(col)` | StringType JSON | Respects `ignoreNullFields` |
| `F.schema_of_json(lit(s))` | DDL schema **string** (not StructType) | Call `.first()[0]` to get value |
| `F.schema_of_csv(lit(s))` | DDL schema **string** | Fields named `_c0`, `_c1`... |

### String Functions
| Function | Behaviour |
|---|---|
| `F.concat_ws(sep, *cols)` | Join with separator; **skips nulls** |
| `F.split(col, pattern, limit)` | Regex split; `limit=n` → max n elements |
| `F.base64(binary)` → StringType | `F.unbase64(str)` → BinaryType |
| `F.hex(col)` → StringType hex | `F.unhex(str)` → **BinaryType** (not integer!) |
| `F.levenshtein(l, r)` | Edit distance IntegerType |
| `F.format_string(fmt, *cols)` | Printf-style; handles type conversion |
| `F.sentences(text)` | `ArrayType(ArrayType(StringType()))` |

### Date/Time
| Function | Returns | Notes |
|---|---|---|
| `to_date(col, fmt)` | DateType | No time; no TZ issues |
| `to_timestamp(col, fmt)` | TimestampType | TZ-aware |
| `F.dayofyear(date)` | Int 1–366 | 2024 leap year → March 1 = **day 61** |

### Aggregation
| Function | Null handling |
|---|---|
| `F.greatest(*cols)` | Ignores nulls; `null` only if **all** null |
| `F.least(*cols)` | Same |
| `F.rand(seed)` | Uniform [0, 1); fixed seed = reproducible |
| `F.randn(seed)` | Standard normal; fixed seed = reproducible |

---

## TOPIC 3: DataFrame / Dataset API (Q41–Q70)

### Spark Version Methods
| Added in | Method |
|---|---|
| 3.0 | `df.transform(func)` — fluent chaining sugar for `func(df)` |
| 3.1 | `df.unionByName(other, allowMissingColumns=True)` |
| 3.1 | `writeStream.toTable(name)` |
| 3.3 | `df.withColumns(dict)` — batch add/replace columns |
| 3.4 | `df.unpivot(ids, values, varCol, valCol)` / `df.melt(...)` |
| 3.4 | `F.try_element_at` — always null-safe |

### Union
| Method | Alignment | Missing cols |
|---|---|---|
| `union` / `unionAll` | **By position** | Error if count differs |
| `unionByName` | **By name** | Error unless `allowMissingColumns=True` |

### Write / Insert
| Method | Column matching |
|---|---|
| `df.write.insertInto(table)` | **By position** — silent wrong-column writes if order differs |
| `df.write.mode("append").saveAsTable(table)` | **By name** — safe |

### Stats
| Method | Returns | Use case |
|---|---|---|
| `df.stat.bloomFilter(col, n, fpp)` | `BloomFilter` object | "Is X in the set?" no false negatives |
| `df.stat.countMinSketch(col, eps, conf, seed)` | `CountMinSketch` object | Frequency estimates |
| `df.describe()` | DataFrame | count, mean, stddev, min, max only |
| `df.summary(*stats)` | DataFrame | + percentiles `"25%"`, `"99%"` etc. |

### Window Functions
| Function | First row value | Formula |
|---|---|---|
| `F.percent_rank()` | **0.0** | `(rank−1)/(n−1)` |
| `F.cume_dist()` | **> 0** (e.g., 1/n) | `rows_leq / n` |
| `F.ntile(4)` over 10 rows | Bucket 1 | Sizes: 3, 3, 2, 2 (larger first) |
| `F.lag(col, 1, default)` | `default` value | No preceding row at boundary |
| `F.lead(col, 1, default)` | `default` value | No following row at boundary |

### Struct / Nested
| Operation | Syntax |
|---|---|
| Create struct | `F.struct(col1.alias("f1"), col2.alias("f2"))` |
| Explicit names | `F.named_struct(lit("x"), lit(3.0), lit("y"), lit(4.0))` |
| Access nested | `df.select("address.city")` = `df.select(F.col("address.city"))` |
| Literal dot in name | `F.col("`field.name`")` (backtick escape) |
| Map → structs | `F.map_entries(map_col)` |
| Struct array → cols | `F.inline(arr_of_structs)` |

### Miscellaneous
| Topic | Fact |
|---|---|
| `createGlobalTempView` | Raises `TempTableAlreadyExistsException` if taken |
| `createOrReplaceGlobalTempView` | Safe; replaces atomically |
| `df.explain(mode="codegen")` | Shows generated Java from whole-stage codegen |
| `df.na.replace(val, None, subset)` | Convert specific value → null |
| Self-join alias | `df.alias("a").join(df.alias("b"), ...)` — avoids ambiguous columns |

---

## TOPIC 4: Troubleshooting & Tuning (Q71–Q80)

| Config | Default | Purpose |
|---|---|---|
| `spark.sql.adaptive.enabled` | **`true`** (3.2+) | AQE master switch; was `false` in 3.1 (Q71) |
| `spark.sql.mapKeyDedupPolicy` | `EXCEPTION` | `LAST_WIN` = keep last on duplicate map key (Q72) |
| `spark.sql.columnNameOfCorruptRecord` | `_corrupt_record` | Must be in schema as StringType for PERMISSIVE mode (Q73) |
| `spark.sql.optimizer.inSetSwitchThreshold` | 10 | > threshold → `InSet` HashSet O(1) lookup (Q74) |
| `spark.sql.session.timeZone` | JVM default | UTC 12:00 with NY (UTC-4) → displays 08:00 (Q75) |
| **`spark.sql.parquet.compression.codec`** | `snappy` | **Q76 answer A** — Parquet-only compression |
| `spark.sql.debug.maxToStringFields` | 25 | Fields shown in plan/schema toString (Q77) |
| `spark.sql.execution.arrow.maxRecordsPerBatch` | 10 000 | Rows per Arrow batch in `toPandas()`; reduce to lower peak mem (Q78) |
| `spark.sql.repl.eagerEval.enabled` | `false` | Auto HTML render in Jupyter/Zeppelin (Q79) |
| `spark.sql.statistics.fallBackToHdfs` | `false` | Estimate size from HDFS when Hive stats absent (Q80) |

---

## TOPIC 5: Structured Streaming (Q81–Q90)

| Topic | Key fact |
|---|---|
| `processingTime` trigger | Next batch starts immediately if current > interval; never concurrent (Q81) |
| `dropDuplicates` + watermark | Watermark bounds state; late dupes may not be deduped (Q82) |
| `writeStream.toTable(name)` | Catalog write; vs `start(path)` = raw path, no catalog update (Q83) |
| `processAllAvailable()` | **Test only** — blocks until all data processed (Q84) |
| Stream-static join | Static re-evaluated each micro-batch; no watermark/state needed (Q85) |
| Rate source columns | `timestamp` (TimestampType) + `value` (LongType, 0-based) (Q86) |
| RocksDB state store | `providerClass=RocksDBStateStoreProvider` → off-heap, no GC pressure (Q87) |
| Memory sink | Temp view named by `queryName`; query via `spark.sql("SELECT * FROM name")` (Q88) |
| `spark.sql.streaming.numShufflePartitions` | Streaming-only shuffle partition override (Q89) |
| Kafka `startingOffsets` | Ignored on restart with valid checkpoint; only applies to first start (Q90) |

---

## TOPIC 6: Spark Connect (Q91–Q95)

| Topic | Fact |
|---|---|
| Session creation | `SparkSession.builder.remote("sc://host:15002").getOrCreate()` (Q91) |
| Default port | **15002** (`spark.connect.grpc.binding.port`) (Q94) |
| Artifact distribution | `spark.addArtifact("file.py")` replaces `sc.addFile()` / `sc.addJar()` (Q92) |
| Start server | `./sbin/start-connect-server.sh --packages "..."` (Q93) |
| Session config | `spark.conf.set()` → scoped to this client's session via gRPC (Q95) |
| No SparkContext | `spark.sparkContext` raises `PySparkNotImplementedError` |

---

## TOPIC 7: Pandas API on Spark (Q96–Q100)

| Method | Behaviour |
|---|---|
| `psdf.melt(id_vars, value_vars, var_name, value_name)` | Wide → long; mirrors `pandas.melt` (Q96) |
| `psdf.pivot_table(values, index, columns, aggfunc)` | Aggregated pivot; `fill_value` for NaN (Q97) |
| `psdf.merge(other, how, on)` | All join types; **fully distributed** (Q98) |
| `psdf.assign(col=lambda df: expr)` | Returns **new** DataFrame (immutable/functional) (Q99) |
| `psdf["col"] = val` | Mutates in-place (pandas-style) (Q99) |
| `psdf.explode(col)` | Null/empty → `NaN` row preserved (like `F.explode_outer`) (Q100) |

---

## Answer Key Summary

| Qs | Topic | Answer |
|---|---|---|
| 1–20 | Spark Architecture | **B** (all) |
| 21–40 | Spark SQL | **B** (all) |
| 41–75 | DataFrame API + Tuning | **B** (all) |
| **76** | Parquet compression | **A ← EXCEPTION** |
| 77–100 | Tuning + Streaming + Connect + Pandas | **B** (all) |
