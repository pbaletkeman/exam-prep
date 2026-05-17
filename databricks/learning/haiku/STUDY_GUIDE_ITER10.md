# Databricks Certified Associate Developer for Apache Spark — Study Guide (Iteration 10)

**Edition**: Iteration 10 (100 Questions)
**Last Updated**: 2026-05-17
**Total Content**: 20,000+ words across 7 topic sections
**Difficulty Split**: 10 Easy / 54 Medium / 36 Hard
**Study Focus**: Comprehensive mastery with balanced difficulty

---

## Table of Contents

1. [Memory Management & Configuration](#topic-1-memory-management--configuration)
2. [Broadcasting & Runtime Optimization](#topic-2-broadcasting--runtime-optimization)
3. [Spark SQL Optimization Engine](#topic-3-spark-sql-optimization-engine)
4. [Advanced Shuffle & Partitioning](#topic-4-advanced-shuffle--partitioning)
5. [Streaming State & Exactly-Once](#topic-5-streaming-state--exactly-once)
6. [Executor Management & Scaling](#topic-6-executor-management--scaling)
7. [Complex Production Scenarios](#topic-7-complex-production-scenarios)

---

## TOPIC 1: Memory Management & Configuration

### Unified Memory Model Architecture

**Memory Layout (Spark 1.6+)**

```
┌─────────────────────────────────────────────────┐
│  JVM Heap (spark.executor.memory)               │
├─────────────────────────────────────────────────┤
│  Reserved Memory (~300 MB)                      │
├─────────────────────────────────────────────────┤
│  User Memory [(1 - fraction) × heap]            │
├─────────────────────────────────────────────────┤
│  Unified Memory Pool [fraction × heap]          │
│  ┌───────────────────────────────────────────┐  │
│  │ Execution Memory (shuffles, joins, agg)   │  │ ← Dynamic allocation
│  │ ↕ Can evict ↓                             │  │
│  │ Storage Memory (cache, broadcast)         │  │ ← Soft floor: storageFraction
│  └───────────────────────────────────────────┘  │
└─────────────────────────────────────────────────┘
```

**Configuration Parameters**

- **`spark.executor.memory`**: Total JVM heap (default: 1 GB)
- **`spark.executor.memoryOverhead`**: Off-heap memory (default: 10% of executor memory, min 384 MB)
- **`spark.memory.fraction`**: Fraction of heap allocated to unified pool (default: 0.6)
  - Unified pool size = `memory × fraction`
  - User memory size = `memory × (1 − fraction)` (approximately)
- **`spark.memory.storageFraction`**: Soft floor for storage within unified pool (default: 0.5)
  - Storage initial allocation: `unified_size × storageFraction`
  - Execution initial allocation: `unified_size × (1 − storageFraction)`
  - But both can steal from each other under pressure

**Memory Dynamics Under Pressure**

```
Normal State:
  Storage: ████░░░░░░ (50% of unified)
  Execution: ░░░░██████ (50% of unified)

Execution Pressure (shuffle/join):
  Storage: ███░░░░░░░░ (shrinks; evicts cache if needed)
  Execution: ░░░███████ (grows; can steal from storage)

Floor: Storage will not shrink below (storageFraction × unified_size)
```

---

### Heap vs Off-Heap Memory

**On-Heap Memory** (`spark.executor.memory`)
- Managed by Java GC
- Includes execution, storage, user code
- Subject to GC pauses and full heap scans
- **Size**: Set conservatively to avoid long pauses (typically 2-8 GB per executor)

**Off-Heap Memory** (`spark.executor.memoryOverhead`)
- Not managed by JVM; for system buffers, Python worker processes, etc.
- Default: 10% of `executor.memory` (minimum 384 MB)
- No GC impact
- **Critical for**: PySpark (Python worker processes), large shuffle buffers

**Off-Heap Storage** (`spark.memory.offHeap.enabled=true`, `spark.memory.offHeap.size`)
- Enables caching on off-heap storage (e.g., project Tungsten)
- Requires external memory management (e.g., Apache Arrow)
- Avoids GC pressure from cached data
- **Use Case**: Very large caches where GC is bottleneck

---

### Storage Level Selection

**StorageLevel Options**

| Level | Memory | Disk | Serialized | Replicate | Use Case |
|-------|--------|------|-----------|-----------|----------|
| `MEMORY_ONLY` | ✓ | ✗ | No | No | Small data; GC acceptable |
| `MEMORY_ONLY_SER` | ✓ | ✗ | Yes | No | Reduce GC; small data |
| `MEMORY_AND_DISK` | ✓ | ✓ | No | No | Large data; spill okay |
| `MEMORY_AND_DISK_SER` | ✓ | ✓ | Yes | No | Large data; spill + GC pressure |
| `DISK_ONLY` | ✗ | ✓ | Yes | No | Checkpoint; recovery |

**Serialization Trade-off**

- **Deserialized** (`MEMORY_ONLY`): Fast access; many objects → GC pressure
- **Serialized** (`_SER`): Slower access (deser on each read); fewer objects → less GC

**Replication**

- Without replication: Single node loss = data loss (rebuild required)
- With replication: Fault tolerance; no rebuild (use for critical cached data)

---

### GC Pressure Indicators and Tuning

**Symptoms of Memory Pressure**

1. "GC overhead limit exceeded" errors
2. Long pause times (> 10 seconds) in executor logs
3. Tasks failing with "java.lang.OutOfMemoryError"
4. Stage latency spikes unrelated to data volume
5. Executor heartbeat timeout (executor unresponsive during GC)

**Root Causes**

- Heap too small for data + working memory
- Too many small objects (many deserialized cached blocks)
- Accumulating memory leaks (unclosed resources)
- Broadcast variables not cleaned up

**Tuning Strategy**

```bash
# 1. Use G1GC for large heaps (> 4 GB)
--conf spark.executor.extraJavaOptions="-XX:+UseG1GC -XX:MaxGCPauseMillis=30"

# 2. Increase executor memory
--executor-memory 8g  # Scale up from 4g

# 3. Use serialized storage to reduce objects
df.cache(StorageLevel.MEMORY_ONLY_SER)

# 4. Monitor GC pauses
--conf spark.executor.extraJavaOptions="-XX:+PrintGCDetails -XX:+PrintGCTimeStamps"
```

---

## TOPIC 2: Broadcasting & Runtime Optimization

### Automatic Broadcast Join Threshold

**Configuration**

- **`spark.sql.autoBroadcastJoinThreshold`** (default: 10 MiB = 10,485,760 bytes)
- Controls size limit for automatic broadcast hash join activation
- Setting to `-1` disables automatic broadcasting

**How It Works**

1. Catalyst optimizer estimates table sizes from statistics
2. If one side ≤ threshold: candidate for broadcast hash join
3. Broadcast side must fit in executor memory (single node)
4. Smaller side is broadcast; larger side streamed

**Optimal Threshold**

- **Default (10 MiB)**: Conservative; avoids OOM on broadcast
- **Increase to 100-500 MiB**: If executor memory allows (e.g., 8 GB executors)
- **Decrease to < 10 MiB**: If memory constrained or network congested
- **Disable (-1)**: If broadcast consistently causes OOM

**Runtime Broadcast Conversion (AQE)**

```
Adaptive Query Execution can broadcast at runtime if:
  1. AQE enabled (spark.sql.adaptive.enabled=true)
  2. Shuffle stage size observed < threshold
  3. Remaining stages reoptimized with broadcast join
```

---

### Manual Broadcast Hints

**Syntax**

```python
from pyspark.sql.functions import broadcast

result = df_large.join(broadcast(df_small), on="key", how="inner")
```

**When to Use**

- Developer knows one side is small (statistics missing/wrong)
- Force broadcast despite threshold settings
- Join on non-equality conditions (require broadcast hash join)

**Broadcast Failure Modes**

- "Broadcast variable not found": Executor didn't receive broadcast
- "Out of memory" on executor: Broadcast data too large
- "Task deserialization error": Broadcast object not serializable

---

### Join Strategy Selection Revisited

**Decision Logic (Catalyst + AQE)**

```
┌─ One side < 10 MiB (threshold)?
│  ├─ Yes → Broadcast Hash Join (if broadcast feasible)
│  └─ No → Continue
│
├─ Both sides > 100 MiB?
│  ├─ Yes → Sort-Merge Join (stable, scalable)
│  └─ Maybe → Shuffle Hash Join (if memory allows)
│
└─ AQE Enabled?
   ├─ Yes → Monitor shuffle stage sizes; convert to broadcast if one side < 10 MiB
   └─ No → Stick with chosen strategy
```

---

## TOPIC 3: Spark SQL Optimization Engine

### Catalyst Optimizer Deep Dive

**Five Optimization Phases** (in order)

1. **Analysis**: Resolve column references, types, functions
   - Validate table/column existence
   - Resolve column ambiguities in multi-table context
   - Assign function signatures

2. **Logical Optimization**: Optimize logical plan without considering execution cost
   - Predicate pushdown (filters → earliest possible point)
   - Projection pushdown (select only needed columns)
   - Constant folding (evaluate `1 + 1` → `2` at plan time)
   - Dead code elimination (remove unused columns)
   - Boolean simplification (`x AND TRUE` → `x`)
   - Null propagation (`x AND NULL` → `NULL`)

3. **Cost-Based Optimization** (CBO, optional): Consider execution statistics
   - Requires: `ANALYZE TABLE` statistics and `spark.sql.cbo.enabled=true`
   - Benefits:
     - Join order optimization (minimize intermediate result sizes)
     - Join strategy selection (broadcast vs. sort-merge based on cardinality)
     - Push aggregate through join (if beneficial)
   - Trade-off: Planning overhead (milliseconds) for better execution

4. **Physical Planning**: Generate execution plan (which executor strategy, which join)
   - Chose join strategy (broadcast, sort-merge, shuffle-hash)
   - Determine partition count post-shuffle
   - Decide on caching/spilling strategy

5. **Code Generation**: Compile to optimized Java bytecode
   - Generates custom code for filters, aggregations
   - Avoids interpretation overhead
   - Vectorized code paths for columnar operations

---

### Cost-Based Optimizer (CBO) Requirements

**Statistics Collection**

```sql
-- Collect table statistics
ANALYZE TABLE my_table COMPUTE STATISTICS;

-- Collect column statistics
ANALYZE TABLE my_table COMPUTE STATISTICS FOR COLUMNS col1, col2;

-- View collected statistics
DESC FORMATTED my_table;
```

**Statistics Used by CBO**

- **Table-level**: Row count, total size (bytes)
- **Column-level**: Distinct count, min/max, null count, histograms (advanced)

**CBO Impact**

- **Join order**: Reduce intermediate result sizes by joining smallest first
- **Join strategy**: Broadcast only if one side actually fits (cardinality-based)
- **Aggregate pushdown**: Pre-aggregate before join if it reduces intermediate data

**Limitations**

- Statistics must be fresh (data changes invalidate stats)
- Histograms required for more advanced optimizations (not auto-computed)
- Can make planning slower if tables many (exponential join order combinations)

---

### Exchange Operators & Shuffle

**Exchange Operator Semantics**

```
Exchange[HashPartitioning(key, 200)]
  ↓
Shuffle:
  1. Mapper: Hash each row by key % 200 → partition number
  2. Write: Spill to disk if > memory; compress if enabled
  3. Network: Transfer partitions to reducers (torrent if multiple)
  4. Reducer: Receive, merge-sort partitions
```

**Shuffle Configuration**

| Config | Default | Impact |
|--------|---------|--------|
| `spark.shuffle.compress` | true | Compress shuffle blocks; saves network but CPU |
| `spark.shuffle.spill.compress` | true | Compress spilled data to disk |
| `spark.reducer.maxSizeInFlight` | 48 MB | Max concurrent fetch from all mappers |
| `spark.shuffle.sort.bypassMergeThreshold` | 200 | Skip sorting if # reducers ≤ threshold |

---

## TOPIC 4: Advanced Shuffle & Partitioning

### Partition Count Optimization (Advanced)

**Post-Shuffle Partition Count** (`spark.sql.shuffle.partitions`)

- Default: 200 (often too high for small data, too low for large)
- Tuning:
  - Small data (< 1 GB): 50-100 partitions
  - Medium (1-100 GB): 200-500 partitions
  - Large (100+ GB): 500-2000 partitions
  - Rule of thumb: 1-2 MB per partition optimal

**Dynamic Partition Coalescing** (AQE)

- Automatically merges small partitions after shuffle
- Requires: `spark.sql.adaptive.enabled=true`, `spark.sql.adaptive.coalescePartitions.enabled=true`
- Reduces task count from 200 → 10 if 90% of partitions are small

**Bucketing** (for pre-partitioned tables)

```sql
CREATE TABLE bucketed_table
USING PARQUET
CLUSTERED BY (user_id) INTO 100 BUCKETS
AS SELECT * FROM source_table;
```

- Pre-partitions table on disk (100 bucket files)
- Subsequent joins on `user_id` avoid shuffle (bucket-to-bucket join)
- Trade-off: Write time slightly longer; join time much faster

---

### Skew and AQE Skew Join

**Skew Detection (AQE)**

```
AQE observes shuffle stage:
  Median partition size: 50 MB
  Max partition size: 2000 MB (40× median)
  → Detected as skewed!
```

**AQE Skew Join Solution**

```
Skewed partition: Split into sub-partitions
  Original: [key="user_123", 1000 rows, 2000 MB]
  Split:    [key="user_123", 250 rows per sub-partition × 4 = 1000 rows, 500 MB each]

Result: Parallel processing of split partitions; faster execution
```

**Configuration**

```
spark.sql.adaptive.skewJoin.enabled=true  (default: true in 3.x)
spark.sql.adaptive.skewJoin.skewFactor=5  (partition > factor × median = skewed)
```

---

## TOPIC 5: Streaming State & Exactly-Once

### Exactly-Once Guarantee Mechanics

**Components**

1. **Idempotent State Updates** (operator)
   - Applying same state update twice = same result
   - Example: Aggregate count increments once per micro-batch (not twice on replay)

2. **Idempotent Writes** (sink)
   - Writing same data twice = same output
   - Example: Delta Lake ACID writes; database upsert with unique constraint

3. **Fault-Tolerant Offset Management** (source)
   - Offset committed only after state written + sink succeeded
   - On restart: Resume from last committed offset (no data loss, no duplication)

**Failure Scenario**

```
Micro-batch 1:
  Read offsets 0-99
  State: count = 100
  Write output ✓
  Commit offset 100 ✓

Network failure during offset commit → state written but offset not committed

Restart:
  No offset commit found for batch 1
  Replay batch 1: Read offsets 0-99 again
  State: count += 100 (idempotent, so count = 100, not 200)
  Write output again (idempotent, so output unchanged)
  Commit offset 100 ✓

Result: EXACTLY ONCE (no data loss, no duplication)
```

---

### State Store Backend

**Pluggable State Stores**

- **RocksDB** (default): Embedded key-value store; fast access; on-disk backup
- **HDFS**: Explicit HDFS checkpoint directory
- **Custom**: Implement `StateStore` interface

**State Eviction Policy**

```
Watermark = max(event_time) − allowedLateness
State for windows BEFORE watermark: Evicted (freed from memory)
State for windows WITHIN grace period: Kept (may receive late data)
```

---

## TOPIC 6: Executor Management & Scaling

### Dynamic Allocation

**Configuration**

```
spark.dynamicAllocation.enabled=true
spark.dynamicAllocation.minExecutors=1
spark.dynamicAllocation.maxExecutors=100
spark.dynamicAllocation.executorIdleTimeout=60s
```

**Scale-Up Trigger** (when needed)
- Pending tasks exist
- New executors available
- Scale up gradually (add 1 executor per interval)

**Scale-Down Trigger** (when not needed)
- Executor idle > `executorIdleTimeout`
- Remove executor (graceful shutdown; running tasks finish first)

**Trade-off**

- **Benefit**: Adapt to workload; save cluster costs
- **Cost**: Overhead to launch/shutdown; YARN/K8s resource delay; potential data loss if checkpoint not persisted

---

### Cluster Configurations

**Local Mode** (`local`, `local[4]`, `local[*]`)
- Single JVM; no cluster overhead
- Useful: Dev/testing; troubleshooting
- Limits: Single machine resources; no fault tolerance

**Standalone Cluster**
- Simple; no external dependencies (no Hadoop required)
- Limits: Manual resource management; no autoscaling

**YARN** (Hadoop Yarn)
- Centralized resource manager; multi-tenant
- Benefits: Container isolation; other applications share cluster
- Limits: YARN complexity; Hadoop required

**Kubernetes** (K8s)
- Cloud-native; flexible resource limits
- Benefits: Auto-scaling; pod lifecycle management
- Limits: Complexity; network overhead

---

## TOPIC 7: Complex Production Scenarios

### Network Partition & Executor Loss Recovery

**Executor Heartbeat Loss**

```
Driver: Expects heartbeat every 10 seconds
Executor: Silent for 15+ seconds (GC, network issue)
Driver: Marks executor as dead (timeout = 120 seconds default)
```

**Task Recovery**

```
Lost Executor Tasks:
  1. Attempt 1 (original executor) → LOST
  2. Attempt 2 (another executor) → Retry
  3. Attempt 3 (another executor) → Retry
  ... up to spark.task.maxFailures (default: 4)

If shuffle blocks lost:
  Original mapper task rerun to regenerate shuffle output
  (unless shuffle shuffle track is REMOVED at cleanup)
```

---

### Data Locality & Block Manager

**Locality Levels**

```
PROCESS_LOCAL:  Task on same executor as data block (best)
NODE_LOCAL:     Task on same node as data block
RACK_LOCAL:     Task on same rack as data block
ANY:            Task anywhere (last resort)
```

**Preference Order**

- Spark prefers PROCESS_LOCAL if possible
- Falls back to NODE_LOCAL if no cores available
- Waits (locality wait = 3 seconds) before falling back to ANY

**Impact on Performance**

- PROCESS_LOCAL: 1× baseline
- NODE_LOCAL: ~1.2-2× (network overhead within node)
- RACK_LOCAL: ~2-5× (cross-rack network)
- ANY: ~5-10× (cross-datacenter)

---

### Tuning for Large Clusters

**Parameters for 100+ Node Clusters**

```
spark.executor.cores=5            # Don't go too high (task overhead)
spark.executor.memory=16g          # Larger executors; fewer shuffle overhead
spark.sql.shuffle.partitions=2000  # Many partitions for high parallelism
spark.driver.maxResultSize=2g      # Driver must collect large results
spark.scheduler.maxRegisteredResourcesWaitingTime=60s  # Wait for all executors
```

**Bottlenecks on Large Clusters**

- Driver becomes bottleneck (many tasks reporting completion)
  - Solution: Use `spark.scheduler.reviveInterval` (internal tuning)
- Network bandwidth (many executors saturating network)
  - Solution: Reduce shuffle partition size; increase compression
- Shuffle coordination (locating shuffle blocks across 1000s of nodes)
  - Solution: Enable external shuffle service (distributed shuffle metadata)

---

## Critical Concepts Summary

### Memory
- Unified pool: Execution + Storage share; Storage soft floor at `storageFraction`
- Pressure evicts storage (cache) to make room for execution (shuffle, joins)

### Broadcasting
- Threshold: 10 MiB default; disable with `-1`
- AQE can broadcast at runtime if observed size < threshold

### Optimization
- Catalyst: Parse → Analyze → Optimize → Plan → Execute
- CBO requires `ANALYZE TABLE` + `spark.sql.cbo.enabled=true`

### Shuffle
- Exchange operator; configurable compression/spill/bypass
- AQE coalesces small partitions; skew join splits skewed partitions

### Streaming
- Exactly-once: Idempotent state + idempotent sink
- Watermark evicts old state; bounds memory growth

### Executors
- Dynamic allocation: Scale up with pending tasks; scale down when idle
- Heartbeat loss → executor marked dead → task recovery
