# Databricks Certified Associate Developer for Apache Spark — Quick Reference (Iteration 8)

**Edition**: Iteration 8 (100 Questions)
**Last Updated**: 2026-05-17
**Format**: Advanced lookup tables, architecture diagrams, configurations, and hard patterns

---

## Execution Model Quick Reference

| Concept | Definition | Key Detail |
|---------|-----------|-----------|
| **Job** | Triggered by action | One action = one job |
| **Stage** | Shuffle boundary | Multiple stages per job |
| **Task** | Per-partition work unit | # Tasks = # Partitions at stage boundary |
| **Executor Task Slot** | Physical execution slot | Parallelism = # task slots across all executors |

---

## Unified Memory Model Configuration

```
spark.memory.fraction=0.6          # 60% of executor memory = unified region
spark.memory.storageFraction=0.5   # 50% of unified = initial storage
                                   # (Other 50% = initial execution)
spark.memory.offHeap.enabled=false # Off-heap storage (advanced)
spark.memory.offHeap.size=0        # Off-heap region size
```

**Key Behavior**:
- Execution memory can **borrow** from storage memory
- Storage memory is **evicted** (LRU) when execution memory needs space
- Cached blocks: If `MEMORY_ONLY`, **lost on eviction**; if `MEMORY_AND_DISK`, **spilled to disk**

---

## Shuffle File Structure (Sort-Based Default)

```
Per Mapper Task:
  ┌─────────────────────────────────────────────┐
  │ Shuffle{stage}_{mapper}_{attempt}.data      │
  │ (All reducer partitions concatenated)        │
  └─────────────────────────────────────────────┘
  ┌─────────────────────────────────────────────┐
  │ Shuffle{stage}_{mapper}_{attempt}.index     │
  │ [Offset 0, Offset 1, ..., Offset N, EOF]   │
  └─────────────────────────────────────────────┘

Total Files: 2M per stage (M = # mapper tasks)
Reducer Read: Seek via index file; read only its partition range
```

---

## Shuffle Configuration Reference

| Config | Default | Use Case |
|--------|---------|----------|
| `spark.shuffle.sort.bypassMergeThreshold` | 200 | Skip sorting when # reducers ≤ threshold (no aggregation) |
| `spark.shuffle.compress` | true | Compress shuffle data in transit |
| `spark.shuffle.spill.compress` | true | Compress spilled shuffle data on disk |
| `spark.shuffle.unsafe.file.output.buffer` | 32 KB | Increase for high-bandwidth disks |
| `spark.reducer.maxSizeInFlight` | 48 MB | Max concurrent reducer bytes; increase for high bandwidth |
| `spark.shuffle.minNumPartitionsToSquareUp` | N/A (removed) | (Deprecated) |

---

## TaskContext API Reference

```scala
// Inside a task execution function (map, mapPartitions, etc.)
val ctx = TaskContext.get()  // Returns TaskContext or null on driver

ctx.partitionId()      // Zero-based partition index
ctx.attemptNumber()    // 0 = first attempt, 1 = first retry, etc.
ctx.taskId()           // Unique task ID (Long)
ctx.taskMetrics()      // Runtime metrics object
ctx.getLocalProperty("name")  // Driver-set property value
```

**Important**: `TaskContext.get()` is **null on driver**; only valid during task execution

---

## Barrier Mode Configuration

```scala
// Enable barrier execution
rdd.barrier().mapPartitions(func)
rdd.barrier().mapPartitionsWithIndex(func)

// Inside barrier task function:
val barrierCtx = BarrierTaskContext.get()
val rank = barrierCtx.partitionId()  // 0-indexed global rank
barrierCtx.barrier()                 // Wait for all tasks
val allAddresses = barrierCtx.allGather(myAddress)  // Exchange data
```

**Use Case**: Distributed deep learning (PyTorch DDP, Horovod)

**Guarantee**: All tasks start together; **entire stage restarted** on ANY task failure

---

## Scheduler Configuration

| Config | Default | Options | Use |
|--------|---------|---------|-----|
| `spark.scheduler.mode` | FIFO | FIFO, FAIR | Job scheduling policy |
| `spark.scheduler.allocation.file` | None | Path to pools.xml | FAIR scheduler pool definitions |

**FIFO** (default): Jobs run sequentially; each job gets all resources
**FAIR**: Jobs run concurrently; each pool gets minimum share

---

## Join Strategy Selection Decision Tree

```
INPUT: Two DataFrames, join condition exists

1. Check broadcast hint (/*+ BROADCAST(...) */)
   → Yes: Force BroadcastHashJoin

2. Check CBO enabled & statistics exist
   → Yes: Use cost-based decision
   → No: Use heuristics (below)

3. Check smaller side size vs spark.sql.broadcastTimeout (10 MB)
   → Smaller < 10 MB: BroadcastHashJoin
   → Smaller >= 10 MB: → Go to 4

4. Check if both sides fit in executor memory after partition
   → Yes: ShuffleHashJoin (less common)
   → No: SortMergeJoin (default)
```

---

## Join Strategy Comparison

| Join Type | Shuffle | Stages | Memory | Use Case |
|-----------|---------|--------|--------|----------|
| **Broadcast Hash** | None | 1 | Small side must fit | One side < 10 MB |
| **Shuffle Hash** | Both | 2+ (shuffle + hash) | Both fit per partition | Medium-sized joins |
| **Sort-Merge** | Both | 2+ (shuffle + sort) | Unbounded | Large joins; default |
| **Cartesian** | None | 1 (if no condition) | O(left×right) | No condition (rare) |

---

## Catalyst Optimizer Rules (Examples)

| Rule | Input → Output | Impact |
|------|---|--------|
| **Predicate Pushdown** | Filter above scan | Push filter to source; skip unrelated blocks |
| **Projection Pushdown** | Select all columns | Select needed columns only; skip others |
| **Constant Folding** | `1 + 1` in expression | Evaluate at plan time: `2` |
| **Null Elimination** | `col IS NOT NULL AND col IS NULL` | Rewrite to `FALSE` (no rows) |
| **Column Pruning** | Subquery with extra columns | Remove unneeded columns early |

---

## Cost-Based Optimizer (CBO) Requirements

1. **Enable**: `spark.sql.cbo.enabled=true`
2. **Collect Stats**: `ANALYZE TABLE table_name COMPUTE STATISTICS`
3. **Optional Column Stats**: `ANALYZE TABLE ... FOR COLUMNS col1, col2`

**Without Stats**: CBO falls back to heuristics (e.g., broadcast threshold)

---

## Streaming State & Checkpoint Configuration

```
spark.sql.streaming.checkpointLocation=/path/to/checkpoint

# In checkpoint directory:
├── offsets/               # Source offset per micro-batch
├── commits/               # Commit log (batch confirmed)
└── state/                 # State snapshots (aggregations, joins)
```

**Fault Recovery**: On restart, replay from last committed offset

---

## Output Mode Selection for Streaming Aggregations

| Mode | When Data Emitted | State Requirement | Watermark Suitable |
|------|-------------------|-------------------|-------------------|
| **Append** | After watermark passes window end | Bounded (old state evicted) | ✓ Yes |
| **Update** | When aggregate value changes | Partial (may be unbounded) | ✗ Not ideal |
| **Complete** | Every trigger | Unbounded (all state kept) | ✗ No (infinite growth) |

---

## Broadcast Variable Lifecycle

```
Driver: val bvar = sc.broadcast(large_object)
         ↓ (serialized once)

Block Manager: Distribute via torrent to executors
         ↓
Executor 1: Receive, deserialize once, cache
Executor 2: Receive, deserialize once, cache
Executor 3: Receive, deserialize once, cache
         ↓
Tasks on same executor: Share cached copy (no re-deserialization)
```

**Cost**: Serialization overhead (once on driver) + network bandwidth (to all executors)

---

## Accumulator Semantics

| Operation | Timing | Value Seen |
|-----------|--------|------------|
| `acc.add(value)` | Inside task execution | Task-local; not visible to driver immediately |
| `acc.value` on driver during execution | Partial | Only includes completed partitions |
| `acc.value` after action completes | Final | All tasks have updated accumulator |

**Guarantee**: At-least-once (tasks retry → accumulator incremented multiple times on retry)

---

## Data Skew Mitigation Strategies

| Strategy | How It Works | Trade-off |
|----------|-------------|----------|
| **Salting (Manual)** | Add random suffix to skewed key; split into multiple partitions | Extra unsalting step; more partitions |
| **AQE Skew Join** | Automatically detect skew; split partitions & replicate other side | Requires `spark.sql.adaptive.skewJoin.enabled=true` |
| **Different Join Strategy** | Use broadcast if one side is small (avoids shuffle) | Requires one side to fit in memory |
| **Pre-aggregation** | Aggregate locally before join | Changes query semantics; not always applicable |

---

## Small File Problem Solutions

| Approach | Method | Trade-off |
|----------|--------|----------|
| **On Write** | `coalesce(1)` before write | May cause OOM if data large |
| **On Read** | `spark.sql.files.maxPartitionBytes=128MB` | Merges small files automatically |
| **Proactive** | Write with planned partitions | Requires knowing output size upfront |

---

## GC Tuning Configuration

```
--conf spark.executor.extraJavaOptions="-XX:+UseG1GC -XX:MaxGCPauseMillis=30"
```

**For Large Heaps (> 4 GB)**:
- Enable G1GC: `-XX:+UseG1GC`
- Set pause target: `-XX:MaxGCPauseMillis=30` (milliseconds)

**For High GC Pressure**:
- ↑ Executor memory
- Use serialized storage level (`_SER` variants)
- Reduce task size (smaller objects created)

---

## Network Failure Recovery Configuration

| Config | Default | Exponential Backoff |
|--------|---------|-------------------|
| `spark.rpc.numRetries` | 3 | Retry up to 3 times |
| `spark.rpc.retry.wait` | 3s | Wait 3s → 6s → 12s (exponential) |
| `spark.network.timeout` | 120s | Global timeout (covers all retries) |

**Total Max Wait**: ~21 seconds for 3 retries (3 + 6 + 12)

---

## Serialization Framework Comparison

| Serializer | Speed | Size | Use |
|-----------|-------|------|-----|
| **Java** | Slow | Large | Default (compatible) |
| **Kryo** | Fast | Compact | Production (register classes) |

**Configuration**:
```
spark.serializer=org.apache.spark.serializer.KryoSerializer
spark.kryo.registrationRequired=false  # Or true for strict
```

---

## Memory Anchors by Topic (Iteration 8)

### Topic 1: Spark Architecture (Advanced)
1. **Task count = partition count** at stage boundary (not executor cores)
2. **Unified memory**: Execution can **evict** storage (storage memory is "bonus")
3. **Shuffle files**: 2M files (one data + one index per mapper); index enables seekable reads
4. **TaskContext**: `TaskContext.get()` → null on driver; valid only during task execution
5. **Barrier mode**: All tasks start together; entire stage restarted on any failure (DL frameworks)
6. **FAIR scheduler**: Concurrent jobs with pool-based resource sharing
7. **Serialization**: Kyro faster than Java; register classes for best performance

### Topic 2: SQL Optimization (Advanced)
1. **Catalyst pipeline**: Parse → Analyze → Optimize → Plan → Execute
2. **Predicate/projection pushdown**: Most impactful optimizations
3. **CBO requires**: Stats collected via `ANALYZE TABLE`
4. **Join selection**: BroadcastHashJoin (if < 10 MB) → ShuffleHashJoin → SortMergeJoin
5. **Join hints**: Force strategy with `/*+ BROADCAST(table) */`

### Topic 3: DataFrame API (Advanced)
1. **Checkpointing**: Break DAG lineage; save intermediate results to disk
2. **Stateful ops**: Window functions, groupBy, joins maintain state
3. **Cache invalidation**: Manual via `unpersist()`; stale data not auto-invalidated
4. **Bucketing**: Pre-partitioned storage; avoids shuffle on bucketed join/groupBy

### Topic 4: Performance Tuning (Advanced)
1. **Shuffle tuning**: Adjust `shuffle.partitions`, `reducer.maxSizeInFlight`, compression
2. **GC tuning**: Use G1GC for large heaps; prefer `_SER` storage levels
3. **Skew detection**: One task much slower than others
4. **OOM debugging**: Heap dumps, profilers, closure inspection

### Topic 5: Streaming (Advanced)
1. **State store**: In-memory + checkpointed; survives restarts
2. **Exactly-once**: Idempotent state updates + idempotent sinks
3. **Output mode**: Append (bounded) ✓ with watermark; Complete (unbounded) ✗
4. **Offset management**: Kafka (native); file system (path list); custom sources vary

### Topic 6: Distributed Patterns
1. **Broadcast**: Serialized once (driver); deserialized once per executor
2. **Accumulators**: Write from tasks; read from driver (after action)
3. **At-least-once guarantee**: Task retries → accumulator incremented multiple times

### Topic 7: Edge Cases & Hardening
1. **Data skew**: Salting or AQE automatic detection
2. **Small file problem**: `coalesce(1)` on write or `maxPartitionBytes` on read
3. **Network retries**: 3s → 6s → 12s exponential backoff (3 attempts)
4. **Idempotency**: Deterministic UDFs + stateless transforms + idempotent sinks

---

## 7-Point Success Checklist

- [ ] Understand unified memory model (execution can evict storage)
- [ ] Know shuffle file structure (1 data + 1 index per mapper)
- [ ] TaskContext is null on driver; valid only in task execution
- [ ] Barrier mode for distributed ML frameworks (all tasks sync)
- [ ] FAIR scheduler enables concurrent job execution
- [ ] CBO requires statistics; heuristics without them
- [ ] Exactly-once streaming needs idempotent state + idempotent sinks
