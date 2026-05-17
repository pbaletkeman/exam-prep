# Databricks Certified Associate Developer for Apache Spark — Quick Reference (Iteration 10)

**Edition**: Iteration 10 (100 Questions)
**Last Updated**: 2026-05-17
**Format**: Fast lookup tables, decision trees, memory anchors

---

## Memory Layout Quick Reference

```
JVM Heap (spark.executor.memory, default 1 GB)
├── Reserved Memory (~300 MB)
├── User Memory [(1 - fraction) × heap]
└── Unified Memory Pool [fraction × heap] ← spark.memory.fraction (default 0.6)
    ├── Storage Memory [storageFraction × unified] ← spark.memory.storageFraction (default 0.5)
    └── Execution Memory [(1 - storageFraction) × unified]

Off-Heap Memory [spark.executor.memoryOverhead] ← default 10% of executor.memory
```

---

## Memory Configuration Quick Reference

| Config | Default | Impact | Use |
|--------|---------|--------|-----|
| `spark.executor.memory` | 1 GB | Total JVM heap per executor | Scale for large data |
| `spark.executor.memoryOverhead` | 10% of memory (min 384 MB) | Off-heap for system buffers, Python workers | Critical for PySpark |
| `spark.memory.fraction` | 0.6 | Fraction of heap for unified pool | Reduce for large user code |
| `spark.memory.storageFraction` | 0.5 | Storage soft floor within unified pool | Increase to protect cache; decrease for execution |
| `spark.memory.offHeap.enabled` | false | Enable off-heap caching | Use for large caches (project Tungsten) |
| `spark.memory.offHeap.size` | 0 | Off-heap storage size | Set if offHeap.enabled=true |

---

## Storage Level Selection Quick Reference

| Level | Memory | Disk | Serialized | GC Pressure | Use Case |
|-------|--------|------|-----------|-----------|----------|
| `MEMORY_ONLY` | ✓ | ✗ | No | High | Small data; fast access |
| `MEMORY_ONLY_SER` | ✓ | ✗ | Yes | Low | Medium data; GC reduction |
| `MEMORY_AND_DISK` | ✓ | ✓ | No | High | Large data; spill allowed |
| `MEMORY_AND_DISK_SER` | ✓ | ✓ | Yes | Low | Large data; GC + spill |
| `DISK_ONLY` | ✗ | ✓ | Yes | None | Checkpoint; recovery |

---

## Broadcast Join Configuration

| Config | Default | Meaning | Tune When |
|--------|---------|---------|-----------|
| `spark.sql.autoBroadcastJoinThreshold` | 10 MiB | Automatic broadcast size limit | Increase (100-500 MB) if memory allows; disable (-1) if OOM |

**Decision Logic**:
- One side ≤ 10 MiB → Broadcast Hash Join
- Both sides > 10 MiB → Sort-Merge Join (shuffles both)
- AQE enabled → Runtime broadcast possible if observed size < 10 MiB

---

## GC Tuning Quick Reference

**Symptoms of GC Pressure**:
- "GC overhead limit exceeded" errors
- Long pause times (> 10 seconds) in logs
- Tasks failing with OutOfMemoryError
- Executor heartbeat timeout

**Tuning Strategy**:

```bash
# 1. Use G1GC for large heaps
--conf spark.executor.extraJavaOptions="-XX:+UseG1GC -XX:MaxGCPauseMillis=30"

# 2. Increase executor memory
--executor-memory 8g  # Scale from 4g

# 3. Use serialized storage
df.cache(StorageLevel.MEMORY_ONLY_SER)

# 4. Monitor GC pauses
--conf spark.executor.extraJavaOptions="-XX:+PrintGCDetails"
```

---

## Catalyst Optimizer Phases

| Phase | What | When Applied |
|-------|------|--------------|
| **Analysis** | Resolve column names, types, functions | Always |
| **Logical Optimization** | Predicate pushdown, projection pushdown, constant folding | Always |
| **Cost-Based Optimization** | Join order, join strategy based on cardinality | If `spark.sql.cbo.enabled=true` + `ANALYZE TABLE` statistics |
| **Physical Planning** | Choose executor strategy (broadcast vs sort-merge) | Always |
| **Code Generation** | Compile to optimized Java bytecode | Always |

**CBO Requirements**:
- `spark.sql.cbo.enabled=true`
- `ANALYZE TABLE table_name COMPUTE STATISTICS` (table + column stats)

---

## Shuffle Configuration Quick Reference

| Config | Default | Impact |
|--------|---------|--------|
| `spark.sql.shuffle.partitions` | 200 | Post-shuffle partition count |
| `spark.shuffle.compress` | true | Compress shuffle blocks |
| `spark.shuffle.spill.compress` | true | Compress spilled data to disk |
| `spark.reducer.maxSizeInFlight` | 48 MB | Max concurrent fetch from mappers |
| `spark.shuffle.sort.bypassMergeThreshold` | 200 | Skip sorting if # reducers ≤ threshold |

---

## Partition Count Tuning Guide

| Data Size | Recommended Partitions | Per-Partition Size |
|-----------|------------------------|-------------------|
| < 1 GB | 50-100 | 10-20 MB |
| 1-100 GB | 200-500 | 2-5 MB |
| 100+ GB | 500-2000 | 0.5-2 MB |

**Dynamic Coalescing (AQE)**:
- Enabled: `spark.sql.adaptive.coalescePartitions.enabled=true`
- Merges partitions < median size (reduces task count)

---

## Skew Mitigation Strategies

| Strategy | How | Trigger |
|----------|-----|---------|
| **AQE Skew Join** | Automatic partition split for skewed joins | `spark.sql.adaptive.skewJoin.enabled=true` (default in 3.x) |
| **Manual Salting** | Add random suffix to split key; unsalt after join | Manual code change; requires unsalting |
| **Join Strategy** | Use broadcast if one side < 10 MiB | Automatic if threshold allows |

**Skew Detection (AQE)**:
- Partition > `skewFactor` (default 5) × median size = SKEWED
- Skewed partitions split into sub-partitions; processed in parallel

---

## Dynamic Allocation Configuration

| Config | Default | Meaning |
|--------|---------|---------|
| `spark.dynamicAllocation.enabled` | false | Enable dynamic scaling |
| `spark.dynamicAllocation.minExecutors` | 0 | Minimum executors to keep |
| `spark.dynamicAllocation.maxExecutors` | infinity | Maximum executors to scale to |
| `spark.dynamicAllocation.executorIdleTimeout` | 60s | Time before idle executor removed |

---

## Executor Lifecycle Configuration

| Config | Default | Meaning |
|--------|---------|---------|
| `spark.executor.instances` | 1 | Static # of executors (if dynamic disabled) |
| `spark.executor.cores` | 1 | # cores per executor | | `spark.executor.memory` | 1 GB | Memory per executor |
| `spark.task.cpus` | 1 | CPU cores per task |
| `spark.rpc.numRetries` | 3 | Max task retry attempts |
| `spark.executor.heartbeatInterval` | 10s | Heartbeat frequency |
| `spark.network.timeout` | 120s | Network timeout (executor heartbeat deadline) |

---

## Executor Loss Recovery

**Heartbeat Failure Flow**:

```
Executor silent for 10+ seconds
  ↓ (Driver notices missing heartbeat)
Mark executor as DEAD after spark.network.timeout (120s)
  ↓
Tasks on dead executor → Attempt Retry (up to spark.task.maxFailures = 4)
  ↓
Shuffle blocks regenerated if mapper task rerun
  ↓
Task succeeds on new executor or fails after max retries
```

---

## Data Locality Preference

| Locality | Network Overhead | Performance Impact |
|----------|------------------|-------------------|
| PROCESS_LOCAL | None (same executor) | 1× (baseline) |
| NODE_LOCAL | Minimal (same node) | ~1.2-2× |
| RACK_LOCAL | Moderate (cross-rack) | ~2-5× |
| ANY | High (cross-datacenter) | ~5-10× |

**Locality Wait** (default 3s): Spark waits before falling back to lower locality level

---

## Large Cluster Tuning (100+ nodes)

```
spark.executor.cores=5            # Avoid high core counts (task overhead)
spark.executor.memory=16g         # Larger executors; fewer shuffle ops
spark.sql.shuffle.partitions=2000 # High parallelism
spark.driver.maxResultSize=2g     # Driver memory for result collection
```

**Bottlenecks**:
- Driver: Many tasks reporting completion → use internal tuning
- Network: Many executors saturating bandwidth → reduce shuffle size
- Shuffle metadata: External shuffle service helps locate blocks

---

## State Store & Watermarking

| Config | Default | Impact |
|--------|---------|--------|
| `spark.sql.streaming.checkpointLocation` | required | State and offset storage directory |

**State Eviction**:
- Watermark = `max(event_time) − allowedLateness`
- State for windows BEFORE watermark = EVICTED (freed)
- State WITHIN grace period = KEPT (may receive late data)

---

## Memory Anchors by Topic (Iteration 10)

### Topic 1: Memory Management
1. **Unified pool**: Execution + Storage share; Storage has soft floor (`storageFraction`)
2. **Pressure dynamics**: Execution steals from Storage when needed; Storage won't shrink below soft floor
3. **Off-heap**: 10% of executor.memory; critical for Python workers; avoids GC
4. **Storage levels**: Serialized (_SER) = less GC; Deserialized = faster access

### Topic 2: Broadcasting
1. **Threshold**: 10 MiB default (`spark.sql.autoBroadcastJoinThreshold`)
2. **Automatic**: Catalyst checks table size; broadcasts if ≤ 10 MiB
3. **AQE Runtime**: Can broadcast at runtime if observed size < 10 MiB
4. **Manual**: Use `broadcast()` hint to force broadcast

### Topic 3: Catalyst & CBO
1. **Phases**: Parse → Analyze → Optimize (logical) → Plan (physical) → Generate (code)
2. **Key optimizations**: Predicate pushdown (most impactful), projection pushdown, constant folding
3. **CBO**: Requires `spark.sql.cbo.enabled=true` + `ANALYZE TABLE` statistics
4. **Join order**: CBO minimizes intermediate result sizes; important for multi-way joins

### Topic 4: Shuffle & Partitioning
1. **Partition size**: 1-2 MB optimal; too small → task overhead; too large → memory pressure
2. **AQE coalescing**: Merges partitions < median; automatic if enabled
3. **Skew join**: Split partitions > 5× median; processes in parallel (automatic with AQE)
4. **Bucketing**: Pre-partitions on disk; subsequent joins avoid shuffle (if join key = bucket key)

### Topic 5: Streaming
1. **Exactly-once**: Idempotent state + idempotent sink + fault-tolerant offset management
2. **State eviction**: Watermark triggers eviction of state for windows in past
3. **Checkpoint**: Stores offsets, commits, state; enables recovery
4. **Append mode**: Only safe mode with watermark (watermark guarantees no updates to past windows)

### Topic 6: Executors
1. **Dynamic allocation**: Scale up with pending tasks; scale down when idle
2. **Heartbeat**: Executor sends every 10s; loss after 120s → marked dead
3. **Task recovery**: Up to 4 retries; shuffle blocks regenerated if mapper rerun
4. **Locality**: PROCESS_LOCAL preferred; falls back to NODE_LOCAL, RACK_LOCAL, ANY

### Topic 7: Production
1. **Large cluster**: 100+ nodes → increase partition count; use larger executors
2. **Network**: External shuffle service for cluster > 50 nodes
3. **GC tuning**: G1GC for large heaps; serialized storage; increase memory
4. **Bottlenecks**: Driver (many tasks), network (shuffle), shuffle metadata (block location)

---

## 10-Point Success Checklist

- [ ] Unified memory: Storage soft floor at `storageFraction`; execution steals as needed
- [ ] Broadcast threshold: 10 MiB default; increase if memory allows; disable with -1
- [ ] Catalyst: Predicate + projection pushdown most impactful optimizations
- [ ] CBO: Requires statistics + `spark.sql.cbo.enabled=true` for join order optimization
- [ ] Partition size: 1-2 MB optimal; AQE coalesces automatically if enabled
- [ ] Skew: AQE detects (partition > 5× median); splits automatically; manual salting fallback
- [ ] Exactly-once: Idempotent state + idempotent sink + offset management
- [ ] Executor loss: Heartbeat loss after 120s; task recovery up to 4 retries; shuffle regeneration
- [ ] Dynamic allocation: Scale up with pending tasks; scale down when idle > 60s
- [ ] Data locality: PROCESS_LOCAL preferred; 3s wait before fallback to lower levels
