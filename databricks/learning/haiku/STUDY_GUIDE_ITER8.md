# Databricks Certified Associate Developer for Apache Spark — Study Guide (Iteration 8)

**Edition**: Iteration 8 (100 Questions)
**Last Updated**: 2026-05-17
**Total Content**: 20,000+ words across 7 topic sections
**Difficulty Split**: 9 Easy / 55 Medium / 36 Hard
**Study Focus**: Advanced architecture, optimization, internals, and edge cases

---

## Table of Contents

1. [Apache Spark Architecture & Internals (Advanced)](#topic-1-apache-spark-architecture--internals-advanced)
2. [Spark SQL Optimization & Query Planning](#topic-2-spark-sql-optimization--query-planning)
3. [DataFrame & Dataset API (Advanced)](#topic-3-dataframe--dataset-api-advanced)
4. [Performance Tuning & Optimization](#topic-4-performance-tuning--optimization)
5. [Structured Streaming (Advanced)](#topic-5-structured-streaming-advanced)
6. [Distributed Computing Patterns](#topic-6-distributed-computing-patterns)
7. [Edge Cases & Production Hardening](#topic-7-edge-cases--production-hardening)

---

## TOPIC 1: Apache Spark Architecture & Internals (Advanced)

### Execution Model & Task Scheduling

**Job, Stage, Task Relationship**

- **Job**: Triggered by an action (`.collect()`, `.write()`, `.count()`, etc.)
- **Stage**: Created at shuffle boundaries; DAGScheduler breaks the DAG at wide dependencies
- **Task**: One task per **partition** at that stage
- **Key Formula**: `num_tasks_in_stage = num_partitions_at_stage_boundary`
- **Example**: If a DataFrame has 200 partitions going into a `groupBy` (wide dependency), the shuffle creates 200 map tasks + 200 reduce tasks (post-shuffle partition count = `spark.sql.shuffle.partitions`, default 200)

**Why Tasks Are Partition-Bound**

- Each partition is logically independent (no cross-partition communication needed within a stage)
- Spark's parallelism is achieved by running multiple tasks concurrently, one per partition
- A partition can be processed by any executor with available resources (data locality is a secondary optimization)

---

### Unified Memory Model & Eviction Policies

**Unified Memory Architecture** (Spark 1.6+)

```
┌─────────────────────────────────────────────────────────────┐
│ Executor Total Memory: spark.executor.memory (e.g., 4GB)   │
├─────────────────────────────────────────────────────────────┤
│                  Unified Memory Region                       │
│  ┌────────────────────────────────────────────────────────┐ │
│  │ spark.memory.fraction (default 0.6 = 60% of 4GB = 2.4GB) │
│  │                                                          │
│  │ ┌──────────────────────────────────────────────────────┤ │
│  │ │  Storage Memory (RDD cache, DataFrame cache)         │ │
│  │ │  Initial: 50% of unified (1.2GB)                     │ │
│  │ │  Can shrink if execution memory demands it           │ │
│  │ └──────────────────────────────────────────────────────┤ │
│  │                                                          │
│  │ ┌──────────────────────────────────────────────────────┤ │
│  │ │  Execution Memory (shuffle buffers, temp data)       │ │
│  │ │  Initial: 50% of unified (1.2GB)                     │ │
│  │ │  Can borrow from storage if needed                   │ │
│  │ └──────────────────────────────────────────────────────┤ │
│  └────────────────────────────────────────────────────────┘ │
├─────────────────────────────────────────────────────────────┤
│  Reserved Memory: spark.memory.offHeap.size (default 0)    │
│  System Memory: ~300MB (OS, JVM overhead)                  │
└─────────────────────────────────────────────────────────────┘
```

**Memory Borrowing Under Pressure**

- **Storage eviction threshold**: When execution memory needs space, Spark evicts cached blocks from storage
- **Eviction order**: Least-recently-used (LRU) blocks are evicted first
- **Cached block fate**: If evicted and storage level doesn't permit disk spill (e.g., `MEMORY_ONLY`), the block is lost and must be recomputed on next access; if storage level is `MEMORY_AND_DISK`, the block is written to disk first
- **Execution memory dominance**: In practice, execution memory is dominant; storage memory acts as a "bonus" that gets evicted when needed
- **Implication**: Very large cache sizes may be evicted frequently if the job is execution-heavy; better to use smaller caches or use `MEMORY_AND_DISK` storage level

**Key Configuration**

```
spark.memory.fraction=0.6              # 60% of executor memory = unified region
spark.memory.storageFraction=0.5       # 50% of unified = storage (initial)
                                       # Other 50% = execution (initial)
spark.memory.offHeap.enabled=false     # Disable off-heap storage (advanced feature)
spark.memory.offHeap.size=0            # Off-heap memory region (if enabled)
```

---

### Shuffle Write Implementation & File Structure

**Sort-Based Shuffle (Default)**

- **Per-mapper output**: ONE data file + ONE index file (not M × R files)
  - Data file: All reducer partitions' data concatenated in sorted order by partition ID
  - Index file: Array of byte offsets marking where each reducer partition's data starts
  - Total files: 2M (2 per mapper task)
- **Significance of Index File**:
  - Allows reducers to **seek directly** to their portion of the data file
  - Eliminates the need to read all mapper output; only read the relevant range
  - Reduces network I/O and disk reads
  - File format: Binary array of N+1 offsets for N partitions (first offset = 0, last offset = file size)

**Shuffle Write File Layout Example**

```
Mapper Task 0 produces 3 reducer partitions:
  Partition 0: bytes 0-999
  Partition 1: bytes 1000-1999
  Partition 2: bytes 2000-2999

Shuffle0_0_0.data file (3000 bytes): [Partition 0 data][Partition 1 data][Partition 2 data]
Shuffle0_0_0.index file (offsets):   [0, 1000, 2000, 3000]

Reducer Task (partition 1) reads:
  1. Fetch Shuffle0_0_0.index → learns partition 1 data is at bytes 1000-2000
  2. Seek to byte 1000 in Shuffle0_0_0.data
  3. Read exactly 1000 bytes (2000 - 1000)
```

**Bypass Merge Sort Shuffle** (when certain conditions met)

- Conditions: Reduce partitions ≤ `spark.shuffle.sort.bypassMergeThreshold` AND no map-side aggregation
- Behavior: **Skip sorting entirely**; write one file per reducer partition directly, then concatenate
- Trade-off: Lower CPU (no sorting), but more file handles open simultaneously (M × R files)
- Use case: Small number of reducers where file handle overhead is acceptable

---

### Task Context & In-Task Metadata Access

**TaskContext API**

- **Where Available**: Only within task execution (inside `map`, `mapPartitions`, `mapPartitionsWithIndex`, etc. functions)
- **Access Pattern**: `TaskContext.get()` (Scala/Java) or `TaskContext.get()` (PySpark) returns the current task's context object
- **Key Methods**:
  - `taskId()`: Unique task ID (Long)
  - `partitionId()`: Zero-based partition index (Int)
  - `attemptNumber()`: Task attempt count (0 = first attempt, 1 = first retry, etc.)
  - `taskMetrics()`: Runtime metrics (bytes written, bytes read, etc.)
  - `getLocalProperty(name)`: Retrieve driver-set properties (job group, description, etc.)

- **On Driver**: `TaskContext.get()` returns `null`; task context only exists during task execution on executors
- **Thread Safety**: `TaskContext` is thread-local; valid only in the task execution thread

**Use Case Example**

```python
# Logging partition-specific information during task execution
def process_partition(iterator):
    ctx = TaskContext.get()
    partition_id = ctx.partitionId()
    attempt = ctx.attemptNumber()
    print(f"Processing partition {partition_id}, attempt {attempt}")
    for row in iterator:
        yield row

rdd.mapPartitions(process_partition).collect()
```

---

### Barrier Execution Mode (Deep Learning Integration)

**Barrier Mode Requirement**

- **Standard Spark Tasks**: Tasks are independent; any can fail and be retried individually; stage progresses as long as one copy of each task succeeds
- **Barrier Mode Tasks**: **All tasks in the stage must start and complete together**; if ANY task fails, the ENTIRE stage is restarted (all tasks reset)

**Triggering Barrier Mode**

```scala
rdd.barrier().mapPartitions(func)  // Scala
rdd.barrier().mapPartitionsWithIndex(func)
```

**Synchronization Primitive: BarrierTaskContext**

```python
from pyspark.barrier import BarrierTaskContext

def init_distributed_training(iterator):
    barrier_ctx = BarrierTaskContext.get()
    rank = barrier_ctx.partitionId()  # Global rank (0 to num_partitions-1)

    # Barrier: Wait for all tasks to reach this point
    barrier_ctx.barrier()

    # All tasks now have the same rank assignment
    # Exchange addresses with allGather (e.g., for PyTorch rendezvous)
    my_address = f"10.0.0.{rank}:12355"
    all_addresses = barrier_ctx.allGather(my_address)

    # Initialize distributed trainer with all addresses
    # ... trainer = DistributedTrainer(all_addresses) ...

    # Process data
    for row in iterator:
        yield row
```

**Why Barrier Mode Matters for DL**

- Deep learning frameworks (PyTorch DDP, Horovod, TensorFlow distributed) require all workers to initialize together
- Each worker needs to know the addresses of all other workers (rendezvous)
- Gradient synchronization expects all workers to be active simultaneously
- Spark's normal task independence breaks this assumption → requires barrier mode

---

### Job & Task Scheduling Policies

**Default Scheduler: FIFO (First-In-First-Out)**

- Jobs submitted from the same application run **sequentially** by default
- Each job acquires all cluster resources; next job waits for completion
- **Limitation**: Suboptimal for interactive jobs (e.g., Spark SQL queries in a notebook where each query is a separate job)

**FAIR Scheduler** (`spark.scheduler.mode=FAIR`)

- Multiple jobs run **concurrently**, each assigned a pool
- Each pool gets a minimum share of resources
- Within a pool, tasks are assigned using FIFO or FAIR (configurable)
- **Configuration**:
  ```
  spark.scheduler.mode=FAIR
  spark.scheduler.allocation.file=/path/to/pools.xml
  ```
- **Use Case**: Multi-tenant environments, shared clusters, interactive applications

**Pool Configuration** (pools.xml example)

```xml
<?xml version="1.0"?>
<allocations>
  <pool name="production">
    <schedulingMode>FAIR</schedulingMode>
    <weight>1</weight>
    <minShare>10</minShare>  <!-- Minimum executor cores this pool gets -->
  </pool>
  <pool name="interactive">
    <schedulingMode>FIFO</schedulingMode>
    <weight>2</weight>  <!-- Gets 2x the resources of production if both are running -->
    <minShare>5</minShare>
  </pool>
</allocations>
```

**Setting Job Pool for a Job**

```scala
sc.setLocalProperty("spark.scheduler.pool", "interactive")
df.collect()  // This job runs in the "interactive" pool
```

---

### Serialization & Object Storage

**Spark Serialization Framework**

- **Default**: Java serialization (slow, verbose)
- **Alternative**: Kyro (faster, more compact)
- **Configuration**:
  ```
  spark.serializer=org.apache.spark.serializer.KryoSerializer
  spark.kryo.registrationRequired=false  # Or true for strict mode
  ```

**When Serialization Occurs**

1. **Broadcast variables**: Driver → executors
2. **Task arguments** (closure): Driver → executors
3. **Shuffle data** (unless `spark.shuffle.compress` applies): Mapper → reducer
4. **RDD cache**: Memory → storage or disk
5. **Accumulator updates**: Executor → driver

**Serialization Impact**

- Large closures → slow shipping to executors
- Complex objects (e.g., large DataFrames in closure) → inefficiency
- Custom objects without serialization awareness → OOM risk

**Best Practice**: Keep closures minimal; move data selection to DataFrame/SQL level

---

## TOPIC 2: Spark SQL Optimization & Query Planning

### Catalyst Optimizer & Query Planning Phases

**Spark SQL Query Execution Pipeline**

```
SQL/DataFrame API
       ↓
  [Parser] → Unresolved Logical Plan
       ↓
  [Analyzer] → Analyzed Logical Plan (types resolved, columns checked)
       ↓
  [Optimizer] → Optimized Logical Plan (Catalyst rules applied)
       ↓
  [Planner] → Physical Plan (join strategy selection, etc.)
       ↓
  [Execution] → RDD operations
```

**Catalyst Optimizer Key Rules**

| Rule | Effect | Example |
|------|--------|---------|
| **Predicate Pushdown** | Push filters to data source | `SELECT * FROM table WHERE id > 100` → pushes filter to Parquet reader (skips blocks) |
| **Projection Pushdown** | Select only needed columns | `SELECT name FROM users` → reads only name column from Parquet |
| **Constant Folding** | Evaluate constant expressions at plan time | `WHERE 1 + 1 = 2` → optimizes to `true`, no runtime evaluation |
| **Boolean Simplification** | Simplify Boolean expressions | `WHERE col = col` → `true` |
| **Null Elimination** | Remove impossible conditions | `WHERE col IS NOT NULL AND col IS NULL` → `false` (no rows) |
| **Column Pruning** | Remove unused columns from intermediate results | Subqueries with extra columns → pruned away |

**Cost-Based Optimizer (CBO)** — Advanced Optimization Using Statistics

- Requires: `spark.sql.cbo.enabled=true` AND `ANALYZE TABLE ... COMPUTE STATISTICS`
- Uses: Table row count, column cardinality, histograms to rank alternate plans
- Decisions: Broadcast join vs sort-merge join, join order, filter selectivity estimation
- Without CBO: Heuristic rules only (e.g., "always broadcast if < 10 MB")

---

### Join Strategy Selection

**Broadcast Hash Join** (Most Desired)

- **Condition**: One side < broadcast threshold (default `spark.sql.broadcastTimeout = 10 MB`)
- **Execution**: Small side serialized, broadcast to all executors; large side streamed through
- **Advantage**: Single-stage operation; no shuffle required
- **Cost**: Memory on all executors; small side must fit in memory

**Shuffle Hash Join** (Less Common)

- **Condition**: Both sides small enough to fit in executor memory after partitioning
- **Execution**: Both sides shuffled by join key, then hash joined per partition
- **Advantage**: Distributes build-side construction across executors
- **Use Case**: Medium-sized joins where broadcast is too large

**Sort-Merge Join** (Default for Large Joins)

- **Condition**: Joins on sortable types (numeric, string); no size constraints
- **Execution**:
  1. Both sides repartitioned by join key (shuffle)
  2. Both sides sorted within partition
  3. Streams merged partition-by-partition
- **Advantage**: Scales to any data size; predictable memory usage
- **Cost**: Two shuffles (repartition + sort); higher latency
- **Optimization**: If data is already sorted on join key, sort can be skipped

**Cartesian Join** (Explicitly Requested Only)

- No join condition; produces all possible row combinations
- Result size = `left_rows × right_rows` (often huge!)
- Rarely used intentionally; usually indicates a query bug

---

### Query Optimization Barriers & Hints

**Optimization Barriers**

- Certain operations prevent some optimizations:
  - `LIMIT` without `ORDER BY`: Can't estimate row count downstream (prevents some optimizations)
  - `UNION` vs `UNION ALL`: `UNION` requires deduplication (removes some optimizations)
  - User-defined functions (UDFs): Optimizer can't predict UDF output (treats as black box)

**Join Hints** — Manual Join Strategy Specification

```sql
SELECT /*+ BROADCAST(small_table) */ *
FROM large_table
JOIN small_table ON large_table.id = small_table.id;

-- Or in PySpark:
from pyspark.sql import functions as F
df_large.join(F.broadcast(df_small), on='id')
```

**Hint Types**:
- `BROADCAST(table)`: Force broadcast hash join
- `SHUFFLE_HASH(table)`: Force shuffle hash join
- `SORT_MERGE(table)`: Force sort-merge join (rarely useful)

**When to Use Hints**:
- Optimizer chose suboptimal strategy (detected via `explain`)
- Statistics are stale or missing
- Problem is reproducible and tuning is worth the maintenance cost

---

## TOPIC 3: DataFrame & Dataset API (Advanced)

### Stateful RDD Operations & Checkpointing

**Checkpointing RDDs**

- **Purpose**: Break the lineage to prevent stack overflow on very deep DAGs and to save intermediate results
- **Eager Checkpoint**: `rdd.checkpoint()` → saves to disk/HDFS immediately when action is triggered
- **Lazy Checkpoint**: `rdd.localCheckpoint()` → saves to local executor disk (faster, but lost on executor failure)
- **Configuration**:
  ```
  sc.setCheckpointDir("hdfs:///checkpoints")
  ```
- **After Checkpointing**: Original RDD can be garbage collected; only checkpoint data remains

**Stateful Transformations**

- **Stateful**: Operations that maintain state across partitions or micro-batches
  - RDD: `mapWithState`, `reduceByKeyAndWindow` (streaming only)
  - DataFrame: Window functions, `groupBy`, stateful joins
- **State Management**: Spark manages state implicitly; developer doesn't directly control it
- **Memory Implication**: State must fit in executor memory; unbounded state growth causes OOM

---

### Caching Strategies & Reuse

**When to Cache**

- DataFrame accessed multiple times (e.g., multiple actions or joins)
- Complex transformation pipeline (save intermediate results)
- Iterative algorithms (ML training loops)

**When NOT to Cache**

- Single use only (wasted overhead)
- Very large DataFrames that don't fit in memory
- Streaming data (streaming context handles caching differently)

**Cache Invalidation**

- Cached data becomes stale if source changes (automatic invalidation not guaranteed)
- Use `unpersist(blocking=false)` to immediately mark cache for removal (non-blocking)
- Use `unpersist(blocking=true)` for blocking removal (ensure disk cleanup before proceeding)

---

### Partitioning Strategies & Custom Partitioners

**Repartitioning by Column**

```scala
df.repartition(100, col("user_id"))  // Re-partition into 100 partitions by user_id
```

- Ensures all rows with the same `user_id` go to the same partition
- Useful before a join or `groupBy` on `user_id` to avoid shuffle
- **Cost**: One full shuffle

**Bucketing** — Pre-partitioned Storage

```scala
df.write
  .bucketBy(100, "user_id")  // 100 buckets on user_id
  .sortBy("timestamp")        // Sort within bucket by timestamp
  .mode("overwrite")
  .option("path", "/user/hive/warehouse/users_bucketed")
  .saveAsTable("users_bucketed")
```

- **Advantage**: On next read, `JOIN` or `GROUP BY` on the bucketed column avoids shuffle
- **Use Case**: Frequently joined tables, repeated joins
- **Trade-off**: Bucketing decisions are permanent (for that table); requires re-writing data

---

## TOPIC 4: Performance Tuning & Optimization

### Advanced Configuration Tuning

**Shuffle Tuning Parameters**

| Parameter | Default | Tuning Guide |
|-----------|---------|--------------|
| `spark.sql.shuffle.partitions` | 200 | ↓ for small data; ↑ for large data (e.g., >100 GB) |
| `spark.shuffle.sort.bypassMergeThreshold` | 200 | ↓ to avoid sorting for even fewer reducers; ↑ if file handles are limited |
| `spark.reducer.maxSizeInFlight` | 48 MB | ↑ for high-bandwidth networks; ↓ for tight memory |
| `spark.shuffle.compress` | true | Keep enabled unless CPU is the bottleneck |
| `spark.shuffle.spill.compress` | true | Compress data spilled to disk during shuffle |
| `spark.shuffle.unsafe.file.output.buffer` | 32 KB | ↑ for high-bandwidth disks |

**Network Tuning**

| Parameter | Default | Effect |
|-----------|---------|--------|
| `spark.rpc.numRetries` | 3 | Retries for failed RPC messages |
| `spark.rpc.retry.wait` | 3s | Wait time between retries (exponential backoff) |
| `spark.network.timeout` | 120s | Global network timeout |
| `spark.blockManager.port` | dynamic | Block manager port; leave dynamic unless binding to specific port |

---

### Garbage Collection Tuning

**GC Pressure Indicators**

- **Symptom**: Long pauses, slow stages despite low CPU
- **Root Cause**: JVM heap fragmentation, full GC collections
- **Diagnostic**: Enable GC logs: `-XX:+PrintGCDetails -XX:+PrintGCTimeStamps` in `spark.executor.extraJavaOptions`

**GC Tuning Strategies**

1. **Increase Executor Memory**: More heap → less frequent GC
2. **Use `_SER` Storage Levels**: Serialized objects → fewer GC pauses
3. **Enable G1GC**: `-XX:+UseG1GC` for large heaps (>4 GB)
4. **Reduce Task Size**: Smaller tasks → less object creation
5. **Avoid Large Closures**: Don't capture large DataFrames in UDFs

**Example GC Configuration**

```
--conf spark.executor.extraJavaOptions="-XX:+UseG1GC -XX:MaxGCPauseMillis=30"
```

---

## TOPIC 5: Structured Streaming (Advanced)

### Streaming State & Fault Tolerance

**State Store Backend**

- **Default**: In-memory state (fast, but lost on restart)
- **Checkpoint-Backed**: State persisted to HDFS/S3 at checkpoint locations
- **Configuration**:
  ```
  spark.sql.streaming.stateStore.providerClass=
    org.apache.spark.sql.streaming.state.HDFSBackedStateStoreProvider
  ```

**Exactly-Once Processing Guarantee**

- **Idempotent State Updates**: Same input micro-batch → same state change (replayable)
- **Checkpointing**: Driver state + offset commits + output atomicity
- **Implementation**:
  1. Offset range of micro-batch is recorded
  2. State is updated (and checkpointed)
  3. Output is written (sink must be idempotent or support retries)
  4. Offset is committed
- **Failure Recovery**: On restart, replay from the last committed offset

**Output Idempotency Requirement**

| Sink Type | Idempotency | Notes |
|-----------|-------------|-------|
| Parquet/Delta | Natural | Partitioned writes are idempotent (same partition, same data) |
| Kafka | Manual | Use idempotent producer config; partition key + value uniqueness |
| JDBC | Manual | Use UPSERT or DELETE+INSERT; ensure primary key constraints |
| Foreach | Depends | Must implement idempotent logic in sink function |

---

### Streaming Source & Sink Selection

**Recommended Source-Sink Pairs for Exactly-Once**

- **Delta Lake → Delta Lake** (best): Native exactly-once support
- **Kafka → Delta Lake**: Idempotent writes + Kafka transactional reads
- **Delta Lake → JDBC** (with care): Ensure JDBC sink is idempotent

**Sources with Built-in Offset Management**

| Source | Offset Type | Reliability |
|--------|-------------|-------------|
| Kafka | Topic partition + offset | Highest (broker-managed) |
| File system | List of file paths | High (but incomplete file handling) |
| Socket | Implicit | Lowest (no true offset concept) |
| Rate | Implicit | Very high (synthetic) |
| Structured Streaming custom sources | Custom | Depends on implementation |

---

## TOPIC 6: Distributed Computing Patterns

### Broadcasting & Distributed Caching

**Broadcast Lifecycle**

1. **Driver creates broadcast variable**: `sc.broadcast(value)`
2. **Driver serializes value** (once)
3. **Value is sent to executors** via block manager (torrent-like distribution to avoid driver bottleneck)
4. **Executor deserializes and caches** (per-executor cache, shared by all tasks on that executor)
5. **Tasks access cached value** (no re-serialization)
6. **Unpersist** (optional): `broadcast_var.unpersist()`

**Broadcast Variable Anti-Patterns**

- Broadcasting large DataFrames (use broadcast hint instead: `F.broadcast(df)`)
- Broadcasting non-serializable objects (custom classes without `Serializable` interface)
- Broadcasting inside loop (creates multiple broadcast objects)

---

### Accumulator Pattern & Shared State

**Accumulator Use Cases**

- **Counters**: Count events, errors, rows processed
- **Metrics**: Sum/min/max of values across partitions
- **Distributed Debug Logging**: Collect log messages from all tasks

**Accumulator Semantics**

- **Write from Tasks**: Only during task execution (reading on driver during execution returns partial count)
- **Read from Driver**: Only after action completion (guaranteed to see final value)
- **Lazy Evaluation**: Accumulators updated only when action executes
- **Fault Tolerance**: On task retry, accumulator is re-incremented (at-least-once guarantee, not exactly-once)

**Example**

```scala
val error_count = sc.longAccumulator("error_count")

df.mapPartitions { iterator =>
  iterator.map { row =>
    try {
      process(row)
    } catch {
      case e: Exception =>
        error_count.add(1)
        null
    }
  }
}.collect()

println(s"Errors: ${error_count.value}")  // Read after action
```

---

## TOPIC 7: Edge Cases & Production Hardening

### Data Skew & Mitigation

**Skew Detection**

- **Symptom**: One or few tasks much slower than others; stage latency dominated by stragglers
- **Root Cause**: Uneven data distribution on join/group key (e.g., many rows with the same user_id)
- **Impact**: Partition takes 10× longer than others; overall stage latency = max(partition latencies)

**Skew Mitigation Strategies**

1. **Salting** (Manual Skew Key Splitting):
   ```scala
   df.withColumn("salt", (rand() * 10).cast("int"))
     .repartition(100, col("key"), col("salt"))
   ```
   - Adds random suffix to skewed key
   - Splits single partition into many
   - Must un-salt after join

2. **AQE Skew Join Optimization** (Automatic):
   - If `spark.sql.adaptive.skewJoin.enabled=true`, Spark detects skew and splits partitions automatically
   - No manual salting needed

3. **Different Join Strategy**: If one side is small but skewed, use broadcast join to avoid shuffle

---

### Small File Problem & Mitigation

**Root Cause**

- Reading/writing many small files is inefficient:
  - File listing overhead (O(file_count))
  - Small partition size → many tasks with little work
  - Excessive HDFS RPC calls

**Solutions**

1. **On Write**: Use `coalesce(1)` before write to reduce output partitions
   ```scala
   df.coalesce(1).write.parquet("path")  // Single output file
   ```
   - Risk: May cause memory issues if data doesn't fit in memory

2. **On Read**: Use `spark.sql.files.maxPartitionBytes` to merge small files into fewer partitions
   ```
   --conf spark.sql.files.maxPartitionBytes=134217728  # 128 MB
   ```

3. **Proactive**: Write with larger target partition size
   ```scala
   df.repartition(optimal_num_partitions).write.parquet("path")
   ```

---

### Out-of-Memory Errors & Debugging

**OOM Types**

| Error | Location | Cause | Solution |
|-------|----------|-------|----------|
| `GC overhead limit exceeded` | Executor JVM heap | Too many objects; heap fragmented | ↑ executor memory; use serialized storage |
| `OutOfMemoryError: Java heap space` | Executor JVM heap | Single task too large | ↓ partition count; use `mapPartitions` for streaming |
| `OutOfMemoryError: Unable to allocate X memory` | Off-heap (native) | Off-heap memory exhausted (rare) | Check native library leaks |
| `Direct buffer memory exceeded` | Direct ByteBuffer pool | NIO buffers (shuffle) too many | ↑ `spark.executor.memoryOverhead` |

**Debugging OOM**

- Enable heap dumps: `-XX:+HeapDumpOnOutOfMemoryError -XX:HeapDumpPath=/tmp`
- Analyze dump with Eclipse MAT or similar to find memory leaks
- Check if closure is capturing large objects (use `.map(row => row.field)` instead of `.map(f)` if `f` is a large object)

---

### Network Failures & Retry Logic

**Spark RPC Retry Mechanism**

- **`spark.rpc.numRetries`** (default 3): Max retry attempts for failed RPC calls
- **`spark.rpc.retry.wait`** (default 3s): Wait time before first retry; exponential backoff
- **Exponential Backoff**: Retry wait doubles after each failure (3s, 6s, 12s, ...)
- **Total Max Wait**: ~21 seconds for 3 retries with 3s base

**Transient Failure Recovery**

- **Executor lost**: Tasks on that executor are re-submitted to other executors
- **Shuffle data loss**: If executor removed before shuffle read, blocks are recomputed (re-read from source or re-run mapper)
- **Long retry waits**: May exceed `spark.network.timeout` if network is really slow (configure timeout appropriately)

---

### Data Consistency & Idempotency

**Idempotent Operations** (Safe to Retry)

- **Deterministic UDF**: Same input → same output (e.g., `upper(col)`, `col + 1`)
- **Stateless transformations**: No external side effects (e.g., `filter`, `map`, `select`)
- **Idempotent sinks**: Overwrite mode, partition-based deduplication

**Non-Idempotent Operations** (Unsafe to Retry)

- **Non-deterministic UDF**: Random results (e.g., `rand()`, external API calls)
- **Stateful operations**: Maintain state across partitions (e.g., window functions on non-deterministic ordering)
- **Non-idempotent sinks**: Append mode without deduplication

**Best Practice for Exactly-Once**

- Ensure all UDFs are deterministic
- Use Delta Lake or idempotent sinks
- Avoid `APPEND` mode for sinks unless source provides exactly-once reads (e.g., Kafka with offset management)

---

## Critical Advanced Concepts Summary

### Unified Memory Model
- Storage and execution memory share a pool; execution can evict storage under pressure
- Storage level determines fate of evicted blocks (MEMORY_ONLY → lost; MEMORY_AND_DISK → disk spill)

### Shuffle File Structure
- One data file + one index file per mapper task (not M × R files)
- Index file enables seekable reads by reducer, avoiding unnecessary I/O

### Task Context
- Access partition ID and attempt number via `TaskContext.get()` during task execution
- Not available on driver; thread-local to task execution thread

### Barrier Execution Mode
- Required for distributed DL frameworks (PyTorch, Horovod)
- All tasks start together; entire stage restarted on any failure
- Synchronization via `BarrierTaskContext.barrier()` and `allGather()`

### FAIR Scheduler
- Allows concurrent job execution with resource sharing
- Pool-based resource allocation; configurable within-pool scheduling

### Catalyst Optimizer
- Multi-phase: parse → analyze → optimize → plan → execute
- CBO requires statistics; heuristics used without them

### Broadcast Hash Join
- Most efficient; requires one side to fit in memory
- Serialized once on driver, deserialized once per executor

### Stateful Streaming
- State must be checkpointed for fault tolerance
- Exactly-once requires idempotent state updates and output sinks

### Data Skew
- Manual salting or AQE automatic detection
- Impact: Stage latency = max(partition latencies)
