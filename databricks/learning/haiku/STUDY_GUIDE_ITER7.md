# Databricks Certified Associate Developer for Apache Spark — Study Guide (Iteration 7)

**Edition**: Iteration 7 (100 Questions)
**Last Updated**: 2026-05-17
**Total Content**: 16,000+ words across 7 topic sections
**Difficulty Split**: 16 Easy / 80 Medium / 4 Hard

---

## Table of Contents

1. [Apache Spark Architecture & Internals](#topic-1-apache-spark-architecture--internals)
2. [Spark SQL & Built-in Functions](#topic-2-spark-sql--built-in-functions)
3. [DataFrame & DataSet API](#topic-3-dataframe--dataset-api)
4. [Troubleshooting & Tuning](#topic-4-troubleshooting--tuning)
5. [Structured Streaming](#topic-5-structured-streaming)
6. [Spark Connect](#topic-6-spark-connect)
7. [Pandas API on Spark](#topic-7-pandas-api-on-spark)

---

## TOPIC 1: Apache Spark Architecture & Internals

### Memory Management & Executor Configuration

**`spark.executor.memoryOverhead`** — Off-Heap Container Memory

- **Definition**: The amount of non-JVM memory allocated to each executor container by YARN or Kubernetes, **in addition to** the JVM heap set by `spark.executor.memory`
- **Purpose**: Reserves space for Python/R worker processes, native library allocations (OpenSSL, Zlib), NIO direct buffers, and OS-level overhead
- **Key Detail**: This memory is **NOT** part of the Spark unified memory pool and is **NOT** garbage-collected by the JVM
- **Default**: `max(10% of executor.memory, 384 MB)`
- **Formula**: Total executor container request = `spark.executor.memory + spark.executor.memoryOverhead`
- **Common Pitfall**: Setting only `spark.executor.memory` while ignoring `memoryOverhead` can cause YARN/K8s to evict executors prematurely due to OOM, even though the JVM heap hasn't filled up
- **When to Increase**: For PySpark applications (Python process overhead), or when using libraries with native code components

**`spark.driver.memoryOverhead`** — Driver Container Memory

- Similar to executor overhead, but applied to the **driver container**
- Default: `max(10% of spark.driver.memory, 384 MB)`
- Critical in Spark Connect scenarios where the driver process must accommodate additional gRPC management overhead

---

### Task Execution & Failure Handling

**`spark.task.maxFailures`** (Default: 4)

- **Definition**: The maximum number of times a **single task** can fail before Spark aborts the entire job
- **Failure Counting**: Each time a task's attempt ends with an error, the failure count increments; retries on different executors count as separate attempts
- **Behavior**: Once a task reaches `maxFailures`, Spark immediately terminates the job with a `SparkException`
- **Distinct from `spark.max.retries`** (driver-level executor failure retry count)
- **Tuning**: Increase if transient network errors are common; decrease if quick failure detection is desired

**`spark.speculation`** — Speculative Task Execution

- **When It Triggers**:
  1. At least `spark.speculation.quantile` (default `0.75` = 75%) of the stage's tasks must be complete (providing a stable median task duration)
  2. **AND** a running task's elapsed time exceeds `spark.speculation.multiplier` (default `1.5`) × median completed task time
- **What It Does**: Launches a duplicate copy of the task on a different executor; the first copy to finish wins, the duplicate is killed
- **Use Case**: Mitigation for slow/stalled tasks due to straggler nodes, bad hardware, or garbage collection pauses
- **Downside**: Wasted resources (both copies run simultaneously), potential duplicate processing if both complete before one is killed
- **Configuration**:
  ```
  spark.speculation=true
  spark.speculation.multiplier=1.5        # Task must be 1.5× slower than median
  spark.speculation.quantile=0.75         # Stage must be 75% complete
  spark.speculation.timeout=100ms         # Recheck interval
  ```

---

### Driver-Executor Communication

**`spark.network.timeout`** (Default: 120 seconds)

- **Definition**: Global umbrella timeout for all network interactions between Spark components
- **Primary Use**: Determines how long the driver waits for an executor's heartbeat before declaring the executor lost
- **Cascade Effect**: When an executor is declared lost:
  1. All running tasks on that executor are re-submitted to other executors
  2. The executor's cached data is lost (shuffle files, RDD cache)
  3. If dynamic allocation is enabled, the executor may be removed entirely
- **Related Config**: `spark.executor.heartbeatInterval` (default `10s`) — **must be much less than** `network.timeout`
  - **Why**: A single GC pause or I/O delay on an executor can cause a heartbeat to arrive late; if `heartbeatInterval ≈ network.timeout`, a minor delay exceeds the timeout and triggers false executor eviction
  - **Safe Practice**: Maintain a 10× buffer: `heartbeatInterval = 10s`, `network.timeout = 120s`

**`sc.setJobGroup()` & `sc.cancelJobGroup()`** — Interactive Job Management

- **`sc.setJobGroup(groupId, description, interruptOnCancel=False)`**:
  - Tags all Spark jobs submitted from the **current thread** with a group ID
  - Visible in Spark UI under the Jobs tab
  - Useful for associating related jobs in multi-threaded applications or notebooks
- **`sc.cancelJobGroup(groupId)`**:
  - Cancels all running and queued jobs with the matching `groupId`
  - If `interruptOnCancel=True`, also interrupts the underlying Java threads
  - Enables user-initiated cancellation ("Cancel Query" button in UI or notebook)
- **Use Case**: Multi-user notebook environments where one user's "Cancel" should only affect their jobs, not others'

---

### Partitioning & Parallelism

**`spark.default.parallelism`** vs **`spark.sql.shuffle.partitions`**

| Aspect | `spark.default.parallelism` | `spark.sql.shuffle.partitions` |
|--------|---------------------------|------------------------------|
| **API** | RDD operations (`reduceByKey`, `join`, `parallelize`) | DataFrame/SQL operations & shuffles |
| **Scope** | Controls default partition count when not explicitly specified | Specifically controls post-shuffle partition count |
| **Default** | Varies by cluster type (e.g., 8× core count on local) | 200 |
| **Impact** | No effect on DataFrame shuffles | Critical for DataFrame/SQL shuffle performance |
| **Tuning** | Less common in modern Spark (most workloads use DataFrames) | Frequently tuned; AQE auto-coalesces if enabled |

- **Common Mistake**: Increasing `spark.default.parallelism` expecting DataFrame shuffles to respect it — **they don't**; use `spark.sql.shuffle.partitions` instead

---

### Broadcasting & Remote Procedure Calls

**`spark.rpc.message.maxSize`** (Default: 128 MB)

- **What It Limits**: Maximum size of a single RPC message, including broadcast variables sent via `sc.broadcast()`
- **Behavior When Exceeded**: Spark raises `SparkException`: "RPC message size exceeds [128] MB"
- **How to Fix**: Increase the config: `spark.conf.set("spark.rpc.message.maxSize", "512")` (value in MB)
- **Architectural Note**: This is separate from `spark.sql.maxPlanStringLength` (SQL plan serialization limit)

**Broadcasting Best Practices**

- Driver serializes the broadcast value **once**
- Transmitted to each executor via block manager (using torrent-like peer distribution in cluster mode to avoid driver bottleneck)
- Within a single executor, all concurrent tasks **share one deserialized copy** cached in the executor's broadcast cache
- **Key Efficiency**: O(executors) network transfers, not O(tasks)
- **Suitable for**: Tables < ~1 GB (broadcast join threshold default `spark.sql.broadcastTimeout = 300s`)

---

### Shuffle Optimization & Memory Management

**`spark.shuffle.sort.bypassMergeThreshold`** (Default: 200)

- **When Used**: `BypassMergeSortShuffleWriter` is invoked for a stage when:
  1. Downstream reduce partitions ≤ `bypassMergeThreshold` (default 200)
  2. AND the shuffle does **not** require map-side aggregation (no combiner)
- **Mechanism**: Writes one file per output partition directly **without sorting**; then concatenates files — avoids CPU cost of sorting
- **Trade-off**: Opens O(numReducePartitions) file handles simultaneously — only efficient for small partition counts
- **Key Detail**: If `bypassMergeThreshold` is exceeded, falls back to `SortShuffleWriter` which sorts all map output

**`spark.reducer.maxSizeInFlight`** (Default: 48 MB)

- **Definition**: Maximum total **bytes** of remote shuffle blocks a single reducer task may request simultaneously
- **Purpose**: Prevents reducer tasks from overwhelming remote shuffle servers with too many concurrent fetch requests
- **Tuning Trade-off**:
  - **Lower values** (e.g., 24 MB): Reduced peak memory during shuffle read, but more round-trips (higher latency)
  - **Higher values** (e.g., 96 MB): Higher throughput, but higher peak reducer memory consumption
- **Typical Setting**: Match to network bandwidth; for 1 Gbps, 48 MB is a reasonable default

---

### Executor Lifecycle & Dynamic Allocation

**`spark.excludeOnFailure.enabled`** — Executor/Node Exclusion (Renamed from "Blacklist")

- **Spark 3.1+ Change**: `spark.blacklist.enabled` is deprecated; use `spark.excludeOnFailure.enabled`
- **Functionality**: Tracks per-executor and per-node task failure counts
- **When a Threshold is Exceeded**: Temporarily **excludes** (avoids scheduling new tasks on) that executor or node
- **Configuration**:
  ```
  spark.excludeOnFailure.enabled=true
  spark.excludeOnFailure.task.maxFailures=5    # Exclude executor after 5 task failures
  spark.excludeOnFailure.node.maxFailures=3    # Exclude node after 3 executor failures
  spark.excludeOnFailure.enabled.stage.duration=1h  # How long to maintain the exclusion list
  ```
- **Distinct from `spark.task.maxFailures`**: Task max failures aborts the **job**; exclusion merely avoids **scheduling** on bad executors

**`spark.dynamicAllocation.executorIdleTimeout`** (Default: 60 seconds)

- **Behavior**: When an executor has been idle (no running tasks) for longer than this timeout, Spark requests the cluster manager to remove it
- **Exception**: Executors holding shuffle data are not removed (to preserve shuffle outputs) — unless `spark.dynamicAllocation.shuffleTracking.enabled=false`
- **Rationale**: Reduces cluster cost during quiet periods by releasing resources immediately
- **Risk**: If an executor is removed and a task later tries to fetch its shuffle blocks, the blocks are lost and must be re-computed

---

### Cluster Mode & Web UI

**Client vs Cluster Deploy Mode**

| Aspect | `--deploy-mode client` | `--deploy-mode cluster` |
|--------|----------------------|--------------------------|
| **Driver Location** | Runs in submitting client process | Runs on a cluster node (assigned by cluster manager) |
| **Client Lifetime** | Must stay alive for entire job | Can exit after job is submitted |
| **Driver Logs** | Visible on local terminal | On the cluster node (viewable via UI) |
| **Use Case** | Development, interactive shells | Production, long-running jobs, CI/CD |
| **Network Requirement** | Client must maintain cluster connectivity | No requirement after submission |

**Spark Web UI Port Allocation**

- **First Application**: Port 4040
- **Second Application**: Port 4041 (increments from 4040 until a free port is found)
- **Spark History Server**: Port 18080 (separate service, runs independently of live applications)
- **Port Binding**: If port 4040 is already in use, Spark auto-increments; can be overridden via `spark.ui.port` config

---

### Storage & Caching

**Storage Level Serialization Trade-offs**

| Storage Level | Memory Format | Disk Format | GC Impact | Use Case |
|---------------|--------------|------------|-----------|----------|
| `MEMORY_ONLY` | Deserialized objects | N/A | High (many small objects) | Fast access, ample memory |
| `MEMORY_ONLY_SER` | Serialized bytes | N/A | Low (large byte arrays) | Memory pressure, high GC overhead |
| `MEMORY_AND_DISK` | Deserialized (JVM) | Serialized (disk) | High | Hybrid spill scenario |
| `MEMORY_AND_DISK_SER` | Serialized (JVM) | Serialized (disk) | Low | Tight memory + high GC overhead |
| `DISK_ONLY` | N/A | Serialized | None | Massive spillover |
| `OFF_HEAP` | Off-heap (Unsafe) | Serialized (disk) | None | External memory management |

- **`_SER` Variants**: Use serialized byte arrays in memory, reducing GC pressure but requiring CPU cost for deserialization on reads
- **Selection**: Profile GC frequency; if high, prefer `_SER` variants

**Event Listener Bus**

- **`spark.scheduler.listenerbus.eventqueue.capacity`** (Default: 10000)
  - Bounded asynchronous queue for scheduler events (task completion, stage completion, job progress)
  - Consumer threads (UI, History Server, custom listeners) process events from this queue
  - **When Queue Fills**: Events are dropped, triggering a log warning `"Dropped N SparkListenerEvent events"`
  - **Implication**: Monitoring data is incomplete; UI and metrics are inaccurate
  - **Fix**: Increase queue capacity or optimize slow custom listeners

---

## TOPIC 2: Spark SQL & Built-in Functions

### Date & Time Functions

**`timestampdiff(unit, startTs, endTs)`** — Truncated Time Difference (Spark 3.3+)

- **Return Type**: `IntegerType` (not fractional)
- **Behavior**: Returns the **complete units elapsed**, truncating fractional units toward zero
- **Example**: `timestampdiff('HOUR', ts1='09:00:00', ts2='13:45:00')` → `4` (not 4.75)
- **Valid Units**: `'YEAR'`, `'MONTH'`, `'WEEK'`, `'DAY'`, `'HOUR'`, `'MINUTE'`, `'SECOND'`
- **Contrast**: `months_between()` returns `DoubleType` with fractional months

**`months_between(date1, date2)`** — Fractional Month Calculation

- **Return Type**: `DoubleType`
- **Behavior**: Computes whole months + fractional days ÷ 31 (fixed assumption)
- **Example**:
  - Input: `date1='2026-03-20'`, `date2='2026-01-15'`
  - Calculation: 2 months + 5 days → `2 + (5 ÷ 31)` → ≈ `2.16129`
- **Edge Case**: Both dates on month end → returns whole number (no fractional part)
- **Historical Note**: The 31-day divisor is fixed for backward compatibility, despite actual month lengths varying

**`last_day(date)`** — Last Day of Month

- **Return Type**: `DateType`
- **Behavior**: Returns the final day of the same month and year
- **Example**: `last_day('2026-02-10')` → `'2026-02-28'`
- **Leap Year Handling**: Correctly returns `'2024-02-29'` for February in a leap year
- **Use Case**: Quarter-end reporting, finding month boundary dates

**`next_day(date, dayOfWeek)`** — Next Occurrence of a Weekday

- **Behavior**: Returns the **first date AFTER the input** that falls on the specified day of week
- **Example**: `next_day('2026-04-25', 'MON')` where `'2026-04-25'` is a Saturday → `'2026-04-27'` (next Monday)
- **Important**: If input is already the target weekday, returns the **same weekday of the next week** (not the same date)
- **Valid Day Names**: `'MON'`, `'TUE'`, `'WED'`, `'THU'`, `'FRI'`, `'SAT'`, `'SUN'` (case-insensitive)

**`from_unixtime(epochSeconds, format)`** — Unix Epoch to Formatted String

- **Return Type**: `StringType`
- **Behavior**: Interprets the Unix epoch (seconds since `1970-01-01 00:00:00 UTC`) in the **session's local timezone**
- **Format Pattern**: Standard `java.time.DateTimeFormatter` patterns (e.g., `'yyyy-MM-dd'`, `'HH:mm:ss'`)
- **Default Format**: `'yyyy-MM-dd HH:mm:ss'` if no format is provided
- **Inverse**: `unix_timestamp()` performs the opposite conversion

**`date_add(date, days)` / `date_sub(date, days)`** — Date Arithmetic

- **Behavior**: Adds or subtracts days with automatic month/year rollover
- **Return Type**: `DateType`
- **Example**: `date_add('2026-01-28', 5)` → `'2026-02-02'` (correctly rolls over month boundary)
- **Inverse Relationship**: `date_add(d, n)` is equivalent to `date_sub(d, -n)`

**`to_timestamp(str, format)`** — String to Timestamp Conversion

- **With Format**: `to_timestamp('25/04/2026 14:30', 'dd/MM/yyyy HH:mm')` → `TimestampType`
  - Required when the string deviates from ISO 8601 standard
- **Without Format**: `to_timestamp('2026-04-25T14:30:00')` → `TimestampType`
  - Expects ISO 8601 format (e.g., `'yyyy-MM-ddTHH:mm:ss'` or `'yyyy-MM-dd HH:mm:ss'`)
- **Null Behavior**: Returns `NULL` on parse failure (lenient), unlike `CAST(... AS TIMESTAMP)` in ANSI mode which raises an error
- **Return Type**: Always `TimestampType`

**`dayofweek(date)`** — Day of Week Numbering

- **Convention**: Java `Calendar` standard: **Sunday=1, Monday=2, ..., Saturday=7**
- **Example**: `dayofweek('2026-04-25')` where `'2026-04-25'` is a Saturday → `7`
- **ISO Conversion**: To convert to ISO weekday (Monday=1): `((dayofweek(col) + 5) % 7) + 1`
- **Note**: SQL standard uses ISO (Monday=1), but Spark uses Java convention for backward compatibility

**`date_trunc(unit, timestamp)` vs `trunc(date, format)`**

| Function | Input Type | Output Type | Example | Use Case |
|----------|-----------|-------------|---------|----------|
| `date_trunc('MONTH', ts)` | `TimestampType` | `TimestampType` (midnight) | `'2026-04-01 00:00:00'` | Timestamp precision |
| `trunc(date, 'MM')` | `DateType` | `DateType` | `'2026-04-01'` | Date-only truncation |

- **Units for `date_trunc`**: `'YEAR'`, `'QUARTER'`, `'MONTH'`, `'WEEK'`, `'DAY'`, `'HOUR'`, `'MINUTE'`, `'SECOND'`

**`unix_timestamp(str, format)`** — String to Unix Epoch

- **Return Type**: `LongType` (seconds since epoch)
- **Timezone**: Interprets the timestamp string in the **session's local timezone**
- **Inverse**: `from_unixtime()` converts epoch → formatted string
- **Default Behavior** (no arguments): `unix_timestamp()` returns the current time as epoch seconds

---

### String & Cryptographic Functions

**`sha1(col)` / `sha2(col, bitLength)`** — Cryptographic Hash Functions

- **Return Type**: Both return `StringType` containing lowercase hexadecimal
- **`sha1(col)`**:
  - 160-bit digest → 40-character hex string
  - Example: `sha1(col('name'))` → `'356a192b7913b04c54574d18c28d46e6395428ab'`
- **`sha2(col, bitLength)`**:
  - Valid bit-lengths: `0` (equiv. to 256), `224`, `256`, `384`, `512`
  - `sha2(col, 256)` → 64-character hex string
  - `sha2(col, 512)` → 128-character hex string
  - Invalid bit-length → `NULL`
- **Use Case**: Password hashing (single-pass only, not suitable for security), data fingerprinting

**`base64(binaryCol)` / `unbase64(stringCol)`** — Binary Encoding

- **`base64(col)`**: Input `BinaryType` → Output `StringType` (Base64-encoded text)
- **`unbase64(col)`**: Input `StringType` → Output `BinaryType` (decoded bytes)
- **String Encoding**: To encode a `StringType` column first: `base64(CAST(str_col AS BINARY))`
- **Example**:
  ```sql
  SELECT base64(CAST('hello' AS BINARY)) → 'aGVsbG8='
  SELECT CAST(unbase64('aGVsbG8=') AS STRING) → 'hello'
  ```

**`hex(col)` / `unhex(stringCol)`** — Hexadecimal Encoding

- **`hex(col)`**:
  - Accepts: `IntegerType`, `LongType`, or `BinaryType`
  - Returns: `StringType` uppercase hex (no `'0x'` prefix)
  - Example: `hex(255)` → `'FF'`; `hex(CAST('A' AS BINARY))` → `'41'`
- **`unhex(col)`**:
  - Input: `StringType` hex digits
  - Output: `BinaryType` decoded bytes
  - Example: `unhex('FF')` → single byte with value 255

---

### Text Processing & NLP

**`sentences(str)`** — Hierarchical Tokenization

- **Return Type**: `ArrayType(ArrayType(StringType))`
- **Behavior**: Tokenizes text at **sentence boundaries first** (`.!?` delimiters), then at **word boundaries** within each sentence
- **Punctuation**: Excluded from tokens
- **Example**:
  ```
  sentences("Hello world! How are you?")
  → [["Hello", "world"], ["How", "are", "you"]]
  ```
- **Use Case**: NLP preprocessing for document analysis, sentence-level semantics

**`levenshtein(str1, str2, threshold=None)`** — Edit Distance

- **Return Type**: `IntegerType`
- **Behavior**: Minimum single-character edits (insert, delete, substitute) to transform `str1` into `str2`
- **Example**: `levenshtein('kitten', 'sitting')` → `3` (substitute k→s, e→i, append g)
- **Spark 3.5+**: Accepts optional `threshold` — if distance exceeds threshold, returns `-1` (optimization for early termination)
- **Use Case**: Fuzzy matching, duplicate detection, spell checking

---

### Array Operations

**`element_at(array_or_map, index_or_key)`** — Indexed Access with 1-based Convention

- **For Arrays**:
  - **Positive Index** (1-based): `element_at([10, 20, 30], 1)` → `10` (first element)
  - **Negative Index** (reverse): `element_at([10, 20, 30], -1)` → `30` (last element); `-2` → `20` (second-to-last)
  - **Out of Bounds**: Returns `NULL` (no exception)
- **For Maps**:
  - `element_at(map_col, key)` → returns value for the key or `NULL` if absent
  - Key must match exactly (type-sensitive)

**`slice(array, start, length)`** — Sub-array Extraction

- **Parameters**:
  - `start`: 1-based position (1 = first element)
  - `length`: Number of elements to extract
- **Example**: `slice([10, 20, 30, 40, 50], 2, 3)` → `[20, 30, 40]`
- **Boundary Handling**: If `start + length` exceeds array bounds, returns available elements up to the end

**`array_join(array, delimiter, nullReplacement='')`** — Join Array Elements

- **Behavior**: Concatenates non-null elements with delimiter; `NULL` elements are either skipped or replaced
- **With `nullReplacement`**: `array_join(['a', NULL, 'c'], '-', 'N/A')` → `'a-N/A-c'`
- **Without `nullReplacement`**: `array_join(['a', NULL, 'c'], '-')` → `'a-c'` (NULLs skipped)

**`flatten(nestedArray)`** — Flatten One Level of Nesting

- **Input**: `ArrayType(ArrayType(T))`
- **Output**: `ArrayType(T)` with one level of nesting removed
- **Example**: `flatten([[1,2], [3,4], [5]])` → `[1, 2, 3, 4, 5]`

**`arrays_zip(array1, array2, ...)`** — Combine Multiple Arrays Element-Wise

- **Return Type**: `ArrayType(StructType)`
- **Behavior**: Zips corresponding elements from all input arrays into struct elements
- **Example**:
  ```sql
  arrays_zip(['Alice', 'Bob'], [95, 87])
  → [{name: 'Alice', score: 95}, {name: 'Bob', score: 87}]
  ```
- **Different Lengths**: Shorter arrays are padded with `NULL`

**Higher-Order Array Functions**

- **`filter(array, lambda)`**: Keeps elements where predicate returns `true`
  - Example: `filter([1, 2, 3, 4, 5], x -> x > 3)` → `[4, 5]`
  - `NULL` or `false` results are excluded
- **`transform(array, lambda)`**: Applies function to every element (map)
  - Example: `transform([1, 2, 3], x -> x * x)` → `[1, 4, 9]`
  - Same-length output as input

---

### Map Operations

**`create_map(key1, value1, key2, value2, ...)`** — Constructing Maps

- **Alternating Arguments**: Key and value expressions alternate
- **Return Type**: `MapType(KeyType, ValueType)`
- **Example**:
  ```sql
  create_map(lit('name'), col('user_name'), lit('role'), col('user_role'))
  → {'name': 'Alice', 'role': 'admin'}
  ```

**`map_keys(mapCol)` / `map_values(mapCol)`** — Extracting Keys and Values

- **`map_keys`**: Returns `ArrayType(KeyType)` containing all map keys
- **`map_values`**: Returns `ArrayType(ValueType)` containing all map values
- **Order**: Non-deterministic within a row; consistent across both calls for the same row

**`map_filter(mapCol, lambda)`** — Filter Map Entries

- **Behavior**: Retains only key-value pairs where the lambda `(key, value)` returns `true`
- **Example**: `map_filter({'math': 95, 'english': 82, 'science': 91}, (k, v) -> v >= 90)` → `{'math': 95, 'science': 91}`
- **Return Type**: Same `MapType` as input

---

## TOPIC 3: DataFrame & DataSet API

### Set Operations

**`df.except()` (EXCEPT DISTINCT) vs `df.exceptAll()`** (EXCEPT ALL)

- **`df.except(other)`**: Removes from `df` every row that appears anywhere in `other`, **regardless of duplication**
  - Result: All distinct rows in `df` that don't appear in `other`
  - Example: `[1, 1, 2] except [1]` → `[2]`
- **`df.exceptAll(other)`** (Spark 2.4+): Each occurrence in `other` removes exactly one matching occurrence from `df`
  - Result: Preserves duplicates; row count = `count_df − min(count_df, count_other)`
  - Example: `[1, 1, 2] exceptAll [1]` → `[1, 2]`

**`df.intersect()`** (INTERSECT DISTINCT) vs `df.intersectAll()`**

- **`df.intersect(other)`**: Distinct rows common to both DataFrames
- **`df.intersectAll(other)`**: All common rows with multiplicity = `min(count_df1, count_df2)`
  - Example: `[1, 1, 1] intersectAll [1, 1]` → `[1, 1]`

---

### Column Manipulation & Renaming

**`df.withColumnsRenamed(colsMap)`** — Batch Rename (Spark 3.4+)

- **Syntax**: `df.withColumnsRenamed({'old_name': 'new_name', 'another_old': 'new_another'})`
- **Advantage over chained `withColumnRenamed`**:
  - Single logical plan node (one `Project` node)
  - Chained calls create multiple `Project` nodes, deepening the plan and increasing optimization overhead
- **Order Preservation**: Column order is preserved; only column names change

---

### Transformation Chaining

**`df.transform(func)`** — Function Chaining Pattern

- **Syntax**: `df.transform(func1).transform(func2).transform(func3)`
- **Equivalent To**: `func3(func2(func1(df)))` but reads left-to-right
- **No Performance Overhead**: Purely syntactic sugar; no caching or eager evaluation
- **Use Case**: Composable, modular transformation functions in a clean, readable chain
- **Example**:
  ```python
  def add_audit(df):
      return df.withColumn("created_at", F.current_timestamp())

  def uppercase_name(df):
      return df.withColumn("name", F.upper(F.col("name")))

  result = df.transform(add_audit).transform(uppercase_name)
  ```

---

### Aggregate Functions

**Row-Wise Aggregate Functions**

- **`F.greatest(*cols)`**: Returns the largest value **per row** across specified columns (horizontal operation)
  - Example: `F.greatest(col('a'), col('b'), col('c'))` → per-row max of the three columns
  - **Contrast**: `F.max(col)` is a group-level aggregate (vertical)

**Conditional Aggregation**

- **`F.count_if(condition)`** (Spark 3.3+): Counts rows where the boolean condition is `true`
  - Equivalent to: `SUM(CASE WHEN condition THEN 1 ELSE 0 END)`
  - Example: `F.count_if(col('status') == 'failed')` → number of failed rows
  - **Null Behavior**: Rows where condition is `false` or `NULL` are not counted

**Null Handling in Aggregates**

- **`F.coalesce(*cols)`** (column function, not DataFrame method): Returns first non-null value per row
  - **Distinct from `df.coalesce(n)`** which reduces partitions
  - Example: `F.coalesce(col('a'), col('b'), F.lit(0))` → if `a` is not null, use `a`; else if `b` not null, use `b`; else use `0`

- **`F.nanvl(col1, col2)`**: Returns `col1` if not `NaN`; `col2` if `col1` is `NaN`; propagates `NULL` unchanged
  - Handles IEEE 754 NaN separately from SQL `NULL`

**Collection Aggregates**

- **`F.collect_list(col)`**: Collects all values (including duplicates and NULLs) into an array per group
  - Order is non-deterministic unless combined with an ordered window function
- **`F.collect_set(col)`**: Collects distinct values (excludes duplicates and NULLs)
  - Order is also non-deterministic

**Approximate Aggregates**

- **`F.approx_count_distinct(col, rsd=0.05)`**:
  - Uses HyperLogLog++ algorithm with relative standard deviation (RSD) parameter
  - `rsd=0.05` → ±5% accuracy
  - Significantly more memory-efficient than `F.countDistinct()` which requires exact deduplication
  - Preferred for large datasets where approximation is acceptable

- **`F.percentile_approx(col, quantile, accuracy=10000)`**:
  - Greenwald-Khanna algorithm for approximate percentile
  - `accuracy` parameter: higher → better precision, more memory
  - Accepts a list of quantiles: `[0.25, 0.5, 0.75]` → returns array of approximate percentiles

---

### Grouping & Pivot

**`df.rollup()`** — Hierarchical Subtotals

- **`df.rollup('year', 'quarter').agg(...)`** produces:
  1. `(year, quarter)` — full detail grouping
  2. `(year, NULL)` — subtotals per year
  3. `(NULL, NULL)` — grand total
- **Pattern**: Rolls up from most specific (rightmost) to general; n dimensions → n+1 grouping sets
- **NULL Representation**: `NULL` in the result indicates the aggregation level; distinguish from actual data nulls using `F.grouping(col)` which returns `1` when the column is aggregated at that level

**`df.pivot(col, values)`** — Creating Pivot Tables

- **Explicit Values Recommended**: `df.groupBy('category').pivot('quarter', ['Q1', 'Q2', 'Q3', 'Q4']).agg(...)`
  - Eliminates preliminary scan to discover distinct values
  - Reduces Spark jobs by one (no extra full-table scan)
  - Makes schema deterministic (not dependent on runtime data)
  - Controls output column order
- **Without Values**: Spark must scan the entire DataFrame to discover distinct pivot values — extra job cost

---

### Nested Data Structures

**Creating Structs and Arrays**

- **`F.struct(col('a'), col('b'))`**: Creates a `StructType` column with fields `a` and `b`
  - Nested fields accessible: `col('structcol.a')` or `col('structcol').getField('a')`
  - Rename fields: `F.struct(col('a').alias('alpha'), col('b').alias('beta'))`
- **`F.array(col('a'), col('b'), col('c'))`**: Creates a fixed-length `ArrayType` column
  - Element access: 1-based with `element_at()` or 0-based with bracket notation `[idx]` in DataFrame API
  - All columns must be compatible types (or castable to a common type)

**Exploding Collections**

- **`F.explode(col('items'))`**:
  - For arrays: one row per element (drops rows where array is NULL or empty)
  - For maps: one row per key-value pair
- **`F.explode_outer(col('items'))`**:
  - Preserves rows with NULL or empty collections by emitting one row with `NULL` as the value
  - Analogous to LEFT JOIN vs INNER JOIN
- **`F.posexplode(col('items'))`**:
  - Produces two columns: `pos` (0-based integer index) and `col` (element value)
  - `posexplode_outer` is the NULL-preserving variant

---

### Aggregation with Set Semantics

**Approximate Algorithms**

- **`F.approx_count_distinct(col)`**: Estimate unique count via HyperLogLog
  - Much faster and lower memory than exact `countDistinct` which requires shuffle-based deduplication
  - Trade-off: Approximate result (±5% by default)

---

## TOPIC 4: Troubleshooting & Tuning

### Adaptive Query Execution (AQE)

**Three Core AQE Features** (`spark.sql.adaptive.enabled=true`, default in Spark 3.2+)

1. **Dynamic Partition Coalescing**:
   - After shuffle, small post-shuffle partitions are merged into fewer larger ones
   - Reduces task count without changing result
   - Controlled by `spark.sql.adaptive.advisoryPartitionSizeInBytes` (default 64 MB)
   - **Tuning**: Increase for large clusters (more parallelism desired), decrease for small data (fewer tasks)

2. **Dynamic Join Strategy Switching**:
   - Runtime: If one side of a sort-merge join becomes smaller than broadcast threshold, convert to broadcast join
   - Avoids expensive merge-sort setup for small tables
   - **Requirement**: Must have stats from left side first (it's part of the first stage)

3. **Skew Join Optimization**:
   - Detects partitions exceeding `skewJoin.skewedPartitionFactor × median` AND `skewedPartitionThresholdInBytes`
   - Splits oversized partitions, replicates the other side
   - Transparent to user; no hints required
   - **Configuration**:
     ```
     spark.sql.adaptive.skewJoin.enabled=true
     spark.sql.adaptive.skewJoin.skewedPartitionFactor=5
     spark.sql.adaptive.skewJoin.skewedPartitionThresholdInBytes=256MB
     ```

### Partitioning Strategies

**`df.repartition(n)` vs `df.coalesce(n)`**

| Aspect | `repartition(n)` | `coalesce(n)` |
|--------|-----------------|---------------|
| **Shuffle** | Full shuffle (exchange) | No shuffle (narrow) |
| **Partition Count** | Can increase or decrease | Can only decrease |
| **Partition Size** | Roughly balanced | Often unbalanced |
| **Use Case** | Increase parallelism, re-partition by column, balance skew | Reduce small partitions before write |
| **Cost** | Higher (network I/O) | Lower (local merge) |
| **Syntax** | `repartition(n)` or `repartition(n, col)` | `coalesce(n)` |

- **Skew Remedy**: `repartition(n)` with column argument can re-distribute based on specific column values

### Memory & Compression

**`spark.io.compression.codec`** (Default: `lz4`)

| Codec | Speed | Compression Ratio | CPU | Use Case |
|-------|-------|------------------|-----|----------|
| `lz4` | Fastest | Moderate | Low | Default; shuffles within a node |
| `snappy` | Fast | Moderate | Low | Similar to lz4; HDFS default |
| `zstd` | Slower | High | Higher | Cross-rack shuffles, bandwidth bottleneck |
| `gzip` | Slowest | Highest | Highest | Archival; rarely for Spark runtime |

- **Selection**: Use `zstd` when network (not CPU) is the bottleneck; use `lz4` for CPU-constrained clusters

**Caching & Persistence**

- **`df.cache()`**: Shorthand for `persist(StorageLevel.MEMORY_AND_DISK)`
  - Deserialized Java objects in executor JVM heap
  - Spills to disk when memory full
  - Returns the same DataFrame object (in-place modification)
  - **Always call `df.unpersist()`** when no longer needed

---

### Shuffle Service & Skewed Joins

**External Shuffle Service** (`spark.shuffle.service.enabled=true`)

- **Problem It Solves**: Without it, removing an idle executor loses its shuffle files (breaking downstream tasks)
- **Solution**: Long-running node daemon (independent of executor processes) serves shuffle blocks
- **Consequence**: Executors can be safely removed without losing shuffle data
- **Requirement**: Only applicable with dynamic allocation (`spark.dynamicAllocation.enabled=true`)

---

### Advanced Tuning

**Cost-Based Optimizer (CBO)**

- **Prerequisites**:
  1. `spark.sql.cbo.enabled=true` (default false in open-source; enabled in Databricks)
  2. Run `ANALYZE TABLE table_name COMPUTE STATISTICS` to gather table-level stats
  3. Optionally: `ANALYZE TABLE ... COMPUTE STATISTICS FOR COLUMNS col1, col2` for column-level histograms
- **What It Does**: Uses row count and size estimates to choose between broadcast join vs sort-merge join
- **Without Stats**: Falls back to heuristic rules (e.g., "always broadcast if < 10 MB")
- **Refresh**: Re-run `ANALYZE` after significant data changes

---

## TOPIC 5: Structured Streaming

### Triggers & Micro-Batching

**`trigger(processingTime="30 seconds")`** — Fixed-Interval Batches

- **Behavior**: Attempts to start a new micro-batch every 30 seconds
- **Overrun**: If a batch takes 45 seconds, the next batch starts immediately after (not after an additional 30s delay)
- **Queueing**: Batches queue up if sustained processing time exceeds the interval; no parallel execution
- **Use Case**: Predictable, time-based data arrival

**`trigger(once=True)`** vs **`trigger(availableNow=True)`** (Spark 3.3+)

- **`trigger(once=True)`**: Reads **all available data in a single micro-batch**, then stops
  - Risk: One enormous batch can exceed memory limits or max job duration
  - Use for small datasets
- **`trigger(availableNow=True)`**: Reads all available data but respects `maxFilesPerTrigger`, `maxBytesPerTrigger`, splitting into multiple micro-batches
  - Better fault tolerance (smaller checkpoints)
  - Recommended replacement for `once=True` in production
- **Both**: Stop after consuming available data; useful for backfill or batch-style processing of a data lake

---

### Watermarking & Late Data

**`withWatermark(eventTimeCol, delayThreshold)`** — Late Data Tolerance

- **Watermark Calculation**: `threshold = max(event_time_seen) − delayThreshold`
- **Behavior**:
  - Events with `event_time < threshold` are **dropped** (considered too late)
  - State for windows older than threshold is **evicted** from memory (bounds state size)
- **Configuration**: `df.withWatermark("event_time", "10 minutes").groupBy(F.window("event_time", "5 minutes")).count()`
- **Output Mode Integration**:
  - **Append Mode**: Results emit only after watermark passes window end (guarantees no further updates)
  - **Complete Mode**: Incompatible with watermark (would require infinite state retention)
  - **Update Mode**: Results emit as they change; state may still be unbounded

---

### Streaming Aggregations

**Deduplication with Watermark** — Bounded State

- **Without Watermark**: Deduplication state grows unboundedly (all ever-seen IDs kept in memory)
- **With Watermark**: State is evicted for events older than the watermark threshold
- **Trade-off**: Late duplicates arriving after watermark threshold are no longer detected (may be emitted as new events)
- **Configuration**: `df.withWatermark("ts", "1 hour").dropDuplicates(["event_id"])`

---

### Sink Patterns

**`writeStream.foreachBatch(func)`** — Custom Per-Batch Processing

- **Signature**: `func(micro_batch_df, batch_id)` where:
  - `micro_batch_df`: Static DataFrame containing current batch data
  - `batch_id`: Monotonically increasing integer (reused on replay)
- **Use Case**: Write to sinks without native streaming support (JDBC, REST APIs, multiple output tables)
- **Idempotent Writes**: Use `batch_id` to avoid duplicates on replay — ensure same `batch_id` → same write result

**Delta Lake Streaming Advantages**

- **Efficient Discovery**: Uses transaction log instead of directory listing (scales better)
- **Exactly-Once Semantics**: Built-in exactly-once guarantees (no duplicates/data loss on retry)
- **Change Data Feed**: Capture insert, update, delete events: `option("readChangeFeed", "true")`
- **Historical Starts**: `startingVersion` and `startingTimestamp` options to begin reading from a specific point

---

### Query Lifecycle

**`query.awaitTermination()` vs `query.stop()`**

- **`awaitTermination()`**: **Blocks** the calling thread until the query terminates (error, stop called, natural end)
  - `awaitTermination(timeoutMs)` returns `True` if query stopped within timeout, `False` otherwise
  - **Use**: Keep driver alive while query runs; detect completion in tests
- **`stop()`**: **Actively stops** the query, gracefully finishing the current micro-batch before shutdown
  - No blocking; returns immediately
  - **Use**: User-initiated cancellation, cleanup in finally blocks

**`query.recentProgress`** — Per-Batch Metrics

- **Returns**: List of dictionaries (one per recent batch) containing:
  - `batchId`, `timestamp`, `numInputRows`, `inputRowsPerSecond`, `processedRowsPerSecond`
  - Source `endOffset`, sink `numOutputRows`
  - `durationMs` breakdown (planning, getting offsets, writing output, etc.)
- **Use Case**: Monitor throughput, diagnose bottlenecks, detect lag
- **`query.lastProgress`**: Most recent batch dictionary only
- **`query.status`**: Current state (active batch, stage)

---

## TOPIC 6: Spark Connect

### Architecture & Connection

**Spark Connect Overview** (Spark 3.4+)

- **Architecture**: Thin client (minimal JVM footprint) ↔ remote server (gRPC port 15002) ↔ Spark cluster
- **Benefit**: Client crashes don't crash the server; multi-language clients (Python, Scala, Go, R) share the same server
- **Protocol**: gRPC with Apache Arrow for columnar data transfer
- **Session Isolation**: Each client connection gets its own isolated `SparkSession` with independent config

**Connection & Limitations**

- **Connection**: `SparkSession.builder.remote("sc://hostname:15002").getOrCreate()`
  - Requires `pyspark[connect]` extras
  - No local JVM started in client process
- **Unavailable APIs**:
  - `SparkContext` and RDD operations (`sc.parallelize`, `rdd.map`, accumulators, `sc.broadcast()`, `sc.addFile()`, `sc.setJobGroup()`)
  - Reason: RDD API cannot be efficiently serialized over gRPC
  - **Workaround**: Refactor to use DataFrame/Dataset APIs
- **Available APIs**: All structured DataFrame, Dataset, and SQL APIs; high-level transformations and actions

**Server Lifecycle**

- **Start**: `./sbin/start-connect-server.sh --packages ...` or `spark-submit --class org.apache.spark.sql.connect.service.SparkConnectServer`
- **Behavior**: Long-running service (not a one-time job); accepts multiple concurrent client sessions
- **Stop**: `./sbin/stop-connect-server.sh`
- **Client Lifecycle**: Client can exit; server continues running; subsequent clients reconnect to the same server

**Data Transfer**

- **Serialization**: Results serialized as Apache Arrow RecordBatches streamed over gRPC
- **Benefits**: Columnar, zero-copy-friendly format; enables efficient Pandas interop on client
- **Example Flow**: `df.collect()` triggers server to execute plan, serialize results as Arrow, stream to client

---

## TOPIC 7: Pandas API on Spark

### DataFrame Distributed Operations

**`ps.read_csv(path)` vs `pd.read_csv(path)`**

- **`pyspark.pandas.read_csv(path)`**:
  - Reads distributed across Spark executors
  - Scales with cluster size
  - Supports glob patterns and directory paths
  - Returns `pyspark.pandas.DataFrame` (backed by Spark DataFrame)
  - Suitable for large files
- **`pandas.read_csv(path)`**:
  - Reads entirely on driver node (single-threaded)
  - Limited by driver memory (typically 4-32 GB)
  - Suitable for small files only
  - Returns native `pandas.DataFrame`

**`psdf.to_spark()` & `spark_df.pandas_api()`** — API Conversion

- **`psdf.to_spark()`**: Converts Pandas-on-Spark DataFrame → native Spark DataFrame
  - **Use**: When you need native Spark APIs (window functions, streaming writes, custom aggregations)
  - **Index Handling**: Use `to_spark(index_col="my_index")` to control how index is represented
- **`spark_df.pandas_api()`**: Wraps Spark DataFrame in Pandas API (Spark 3.2+)
  - **Key**: Data stays distributed; operations execute as Spark jobs (not collecting to driver)
  - **Contrast**: `spark_df.toPandas()` collects **all rows** to driver memory (risk of OOM for large data)
  - **Use**: When you want Pandas-like syntax for large distributed datasets

### Merge & Set Operations

**`ps.merge()` — Pandas-like Merge with Automatic Suffix Handling**

- **Behavior**: Follows Pandas merge semantics exactly
- **Duplicate Columns**: When both DataFrames have non-join columns with the same name, result includes both with `_x` and `_y` suffixes
  - Example: `ps.merge(left, right, on='id', how='left')` with both having `name` column → result has `name_x`, `name_y`
- **Contrast**: `spark_df.join()` keeps original names and raises `AnalysisException` on ambiguous access
- **Advantage**: Automatic suffix handling matches Pandas behavior, reducing merge logic bugs

### Configuration & Safety

**`ps.set_option("compute.max_rows", n)`** — Prevent Accidental Memory Overflow

- **Purpose**: Safety limit on operations that collect data to the driver (`.to_pandas()`, `repr()` in notebooks, materializations)
- **Default**: `1000`
- **Behavior**: Raises `ValueError` if operation would return more than `n` rows
- **Disable**: `ps.set_option("compute.max_rows", None)` → allows arbitrarily large collections (**risk of driver OOM**)
- **Recommendation**: Keep a reasonable limit in production; only disable for explicitly bounded results

---

## Comprehensive Formula Reference

| Formula | Description | Example |
|---------|-------------|---------|
| `months_between(d1, d2)` | Months + (days ÷ 31) | `months_between('2026-03-20', '2026-01-15')` ≈ 2.16 |
| `date_add(d, n)` | Add n calendar days | `date_add('2026-01-28', 5)` = `'2026-02-02'` |
| `next_day(d, dow)` | First occurrence of day after d | `next_day('2026-04-25', 'MON')` = `'2026-04-27'` |
| `dayofweek(d)` | Java convention (Sun=1, Sat=7) | `dayofweek('2026-04-25')` = `7` (Saturday) |
| `element_at(arr, idx)` | 1-based positive, negative for reverse | `element_at([1,2,3], -1)` = `3` |
| `slice(arr, start, len)` | 1-based start, n elements | `slice([10,20,30,40], 2, 2)` = `[20,30]` |
| `ntile(n)` | Divide into n buckets | `ntile(4)` on 7 rows = `[1,1,2,2,3,3,4]` |
| `lag(col, offset, default)` | Value from offset rows before | `lag(price, 2, 0.0)` for first 2 rows = `0.0` |

---

## Key Takeaways

1. **Configuration Relationships**: `executor.memory` + `executor.memoryOverhead` = container request
2. **Timeout Cascades**: `heartbeatInterval` << `network.timeout` prevents false evictions
3. **Partition Tuning**: Use `spark.sql.shuffle.partitions` for DataFrames (not `spark.default.parallelism`)
4. **AQE Benefits**: Three features (coalesce, join switch, skew) work together for automatic optimization
5. **Watermarking**: Bounds state size by evicting old events; trade-off with late data handling
6. **Spark Connect**: Decoupled client-server model; RDD API not available
7. **Pandas-on-Spark**: Data stays distributed; use `pandas_api()` not `toPandas()` for large data
