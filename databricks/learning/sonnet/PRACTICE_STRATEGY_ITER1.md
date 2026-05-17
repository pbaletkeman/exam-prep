# Databricks Certified Associate Developer for Apache Spark — Practice Strategy (Iteration 1)

**Edition**: Iteration 1 (100 Questions)
**Generated**: 2026-05-17
**Difficulty Split**: 20 Easy / 60 Medium / 20 Hard
**Answer Types**: 77 single-answer / 23 multi-answer
**Scoring Targets**: Easy ≥85% | Medium ≥70% | Hard ≥65%
**Unique Topics**: Spark Connect + Pandas API on Spark

---

## Table of Contents

1. [Iteration 1 Exam Profile](#iteration-1-exam-profile)
2. [4-Week Study Plan](#4-week-study-plan)
3. [Mock Test 1 — Foundational Baseline](#mock-test-1--foundational-baseline)
4. [Mock Test 2 — Intermediate Focus](#mock-test-2--intermediate-focus)
5. [Mock Test 3 — Advanced Targeting](#mock-test-3--advanced-targeting)
6. [Mock Test 4 — Full Simulation](#mock-test-4--full-simulation)
7. [Common Pitfalls Matrix](#common-pitfalls-matrix)
8. [Multi-Answer Strategy](#multi-answer-strategy)
9. [Topic Weighting Study Allocation](#topic-weighting-study-allocation)
10. [Exam Day Strategy](#exam-day-strategy)

---

## Iteration 1 Exam Profile

### Key Characteristics

| Attribute | Iter 1 Value | Context vs Iter 7–10 |
|-----------|-------------|---------------------|
| Easy questions | 20 (20%) | More Easy than Iter 7–10 |
| Medium questions | 60 (60%) | Similar to Iter 7–10 |
| Hard questions | 20 (20%) | Fewer Hard than Iter 8–10 |
| Single-answer | 77 | Standard |
| Multi-answer | 23 | Standard |
| Unique topics | Spark Connect, Pandas API | Not in other iterations |

### Topic Distribution

| Topic | Questions | % of Exam | Weight Priority |
|-------|----------|-----------|----------------|
| 1. Architecture & Internals | 20 | 20% | High |
| 2. Spark SQL | 20 | 20% | High |
| 3. DataFrame API | 30 | **30%** | **Highest** |
| 4. Troubleshooting & Tuning | 10 | 10% | Medium |
| 5. Structured Streaming | 10 | 10% | Medium |
| 6. Spark Connect | 5 | 5% | Lower (but unique) |
| 7. Pandas API on Spark | 5 | 5% | Lower (but unique) |

### Scoring Target Analysis

To pass at 70%:
- Need **70 correct out of 100**
- Target: Easy 17/20 (85%) + Medium 42/60 (70%) + Hard 13/20 (65%)

---

## 4-Week Study Plan

### Week 1 — Core Foundations (Topics 1, 2)

**Week 1 Goal**: Master Spark Architecture and Spark SQL; build mental models for execution planning

---

#### Day 1 — Architecture Foundations (2 hours)

| Time | Activity | Resource |
|------|----------|----------|
| 0:00–0:30 | Read Architecture section of STUDY_GUIDE_ITER1.md (Driver, SparkSession, DAG) | Study Guide |
| 0:30–1:00 | Learn transformation types (Narrow vs Wide); complete classification table | Quick Reference Topic 1 |
| 1:00–1:30 | Memorise 5 Architecture Memory Anchors; test recall without notes | Quick Reference |
| 1:30–2:00 | Write out, from memory: component table, stage boundary examples | Self-test |

**Day 1 Target Questions**: Q1–Q7 (Driver, SparkSession, Transformations, Stages, Tasks)

**Day 1 Self-Assessment**:
- [ ] Can I name all 5 Spark components and their roles without notes?
- [ ] Can I classify 10 random transformations as Narrow or Wide?
- [ ] Can I explain why `filter` and `select` don't cause new stages?

---

#### Day 2 — Lazy Evaluation & Parallelism (2 hours)

| Time | Activity | Resource |
|------|----------|----------|
| 0:00–0:30 | Study lazy evaluation; list 4 benefits; write example plan graph | Study Guide |
| 0:30–1:00 | Practice identifying actions vs transformations with 20 code examples | Quick Reference |
| 1:00–1:30 | Study partitioning: input vs shuffle partitions; key configs | Study Guide Topic 1 |
| 1:30–2:00 | Flash-test: config properties and their defaults | Master Configs Table |

**Day 2 Target Questions**: Q8–Q14 (Lazy eval, actions, partitions, configs)

**Day 2 Self-Assessment**:
- [ ] Can I list 4 benefits of lazy evaluation from memory?
- [ ] Do I know `spark.sql.shuffle.partitions` default (200)?
- [ ] Can I distinguish 5 actions from 5 transformations without hesitation?

---

#### Day 3 — Fault Tolerance & Broadcasts (2 hours)

| Time | Activity | Resource |
|------|----------|----------|
| 0:00–0:30 | Study fault tolerance: lineage, checkpoint, cache | Study Guide |
| 0:30–1:00 | Study broadcast variables and accumulators | Study Guide |
| 1:00–1:30 | Study join strategies; broadcast threshold config | Study Guide |
| 1:30–2:00 | Review Topic 1 memory anchors; write out from memory | Quick Reference |

**Day 3 Target Questions**: Q15–Q20 (Fault tolerance, broadcasts, accumulators)

**Day 3 Self-Assessment**:
- [ ] Can I explain lineage-based recovery in 2 sentences?
- [ ] Do I know `spark.sql.autoBroadcastJoinThreshold` default (10 MB)?
- [ ] What is the difference between `cache()` and `checkpoint()`?

---

#### Day 4 — Spark SQL: Joins & Aggregations (2 hours)

| Time | Activity | Resource |
|------|----------|----------|
| 0:00–0:40 | Study all 7 join types; practice matching join type to result description | Quick Reference Topic 2 |
| 0:40–1:20 | Study aggregation functions; practice ROLLUP vs CUBE vs GROUPING SETS | Study Guide Topic 2 |
| 1:20–2:00 | Write SQL queries using each join type once; review temp view syntax | Study Guide |

**Day 4 Target Questions**: Q21–Q30 (Join types, aggregations, SQL syntax)

**Day 4 Self-Assessment**:
- [ ] Can I explain LEFT SEMI vs LEFT ANTI with examples?
- [ ] Can I write a GROUP BY query with COUNT, SUM, AVG, countDistinct?
- [ ] Do I know what ROLLUP vs CUBE produces?

---

#### Day 5 — Spark SQL: Window Functions & Catalyst (2 hours)

| Time | Activity | Resource |
|------|----------|----------|
| 0:00–0:40 | Study Window functions: syntax, partitionBy, orderBy, rowsBetween | Study Guide Topic 2 |
| 0:40–1:10 | Master row_number vs rank vs dense_rank with tie examples | Quick Reference |
| 1:10–1:40 | Study Catalyst optimisation pipeline; 5 key optimisations | Study Guide |
| 1:40–2:00 | Topic 2 memory anchors; full recall test | Quick Reference |

**Day 5 Target Questions**: Q31–Q40 (Window functions, Catalyst, SQL DDL)

**Day 5 Self-Assessment**:
- [ ] Given values [10, 20, 20, 30], can I produce row_number/rank/dense_rank results?
- [ ] Can I sketch the Catalyst optimisation pipeline from memory?
- [ ] Do I know all 5 Spark SQL memory anchors?

---

#### Day 6 — Week 1 Practice Test (2 hours)

Run **Mock Test 1** (40 questions, Topics 1 & 2 only). Score and review.

#### Day 7 — Week 1 Review & Gap Filling (1.5 hours)

Review all questions answered incorrectly in Mock Test 1. Re-read corresponding Study Guide sections. Update personal error log.

---

### Week 2 — DataFrame API Deep Dive (Topic 3)

**Week 2 Goal**: Master the DataFrame API (30% of exam — single largest topic)

---

#### Day 8 — Schema, Types, Column Operations (2 hours)

| Time | Activity | Resource |
|------|----------|----------|
| 0:00–0:40 | Study schema definition: StructType, DDL strings, inferSchema | Study Guide Topic 3 |
| 0:40–1:20 | Practice column reference methods; filtering syntax variations | Study Guide |
| 1:20–2:00 | Practice withColumn, withColumnRenamed, drop; null handling functions | Quick Reference Topic 3 |

**Day 8 Target Questions**: Q41–Q50 (Schema, column ops, filtering, null handling)

---

#### Day 9 — Sorting, Deduplication, Joins (2 hours)

| Time | Activity | Resource |
|------|----------|----------|
| 0:00–0:30 | Study sort/orderBy; understand why orderBy is wide | Study Guide |
| 0:30–1:00 | Study distinct vs dropDuplicates; coalesce vs repartition | Study Guide |
| 1:00–1:40 | Study DataFrame joins: syntax, multiple keys, different column names | Study Guide |
| 1:40–2:00 | Write out join strategies table; practice recognising which strategy fires | Quick Reference |

**Day 9 Target Questions**: Q51–Q60 (Sorting, deduplication, joins)

---

#### Day 10 — Reading, Writing, File Formats (2 hours)

| Time | Activity | Resource |
|------|----------|----------|
| 0:00–0:40 | Study all 4 write modes; practice predicting output for each | Quick Reference Topic 3 |
| 0:40–1:20 | Study format comparison: CSV, JSON, Parquet, Delta, ORC | Study Guide |
| 1:20–2:00 | Practice read/write syntax for each format; study partitionBy | Study Guide |

**Day 10 Target Questions**: Q55–Q65 (Read/write, formats, modes)

---

#### Day 11 — UDFs & Built-in Functions (2 hours)

| Time | Activity | Resource |
|------|----------|----------|
| 0:00–0:40 | Study Python UDF syntax and limitations; understand the JVM penalty | Study Guide |
| 0:40–1:10 | Study Pandas UDF (vectorised); understand Arrow advantage | Study Guide |
| 1:10–1:40 | Study built-in string/date/null/conditional functions | Study Guide |
| 1:40–2:00 | Topic 3 memory anchors; full 5-anchor recall test | Quick Reference |

**Day 11 Target Questions**: Q61–Q70 (UDFs, built-in functions, when/otherwise)

---

#### Day 12 — Topic 3 Deep Dive Practice (2 hours)

25-question self-test focusing exclusively on Topic 3 questions. Aim for 75%+ correct.

---

#### Day 13 — Week 2 Practice Test (2 hours)

Run **Mock Test 2** (50 questions, Topics 1–3). Score and review.

#### Day 14 — Week 2 Review & Error Analysis (1.5 hours)

Review missed questions. Categorise errors: careless mistake vs knowledge gap vs trap. Re-read relevant Study Guide sections.

---

### Week 3 — Performance, Streaming, and Unique Topics

**Week 3 Goal**: Master Troubleshooting/Tuning, Structured Streaming, Spark Connect, and Pandas API

---

#### Day 15 — Troubleshooting & Tuning (2 hours)

| Time | Activity | Resource |
|------|----------|----------|
| 0:00–0:40 | Study data skew: symptoms, solutions (salting, AQE, broadcast) | Study Guide Topic 4 |
| 0:40–1:10 | Study small files problem; coalesce vs repartition decision | Study Guide |
| 1:10–1:40 | Study OOM causes; caching strategy; Spark UI tabs | Study Guide |
| 1:40–2:00 | Master Symptom→Diagnosis→Fix matrix | Quick Reference Topic 4 |

**Day 15 Target Questions**: Q71–Q80 (Data skew, small files, OOM, caching)

---

#### Day 16 — Structured Streaming (2 hours)

| Time | Activity | Resource |
|------|----------|----------|
| 0:00–0:30 | Study micro-batch vs continuous processing | Study Guide Topic 5 |
| 0:30–1:00 | Study sources and sinks; checkpoint location syntax | Study Guide |
| 1:00–1:30 | Study output modes: compatibility matrix | Quick Reference Topic 5 |
| 1:30–2:00 | Study watermarks: semantics, late data, memory management | Study Guide |

**Day 16 Target Questions**: Q81–Q90 (Triggers, modes, watermarks, exactly-once)

---

#### Day 17 — Spark Connect (2 hours)

| Time | Activity | Resource |
|------|----------|----------|
| 0:00–0:40 | Study architecture comparison: Classic vs Spark Connect | Study Guide Topic 6 |
| 0:40–1:10 | Study use cases; limitations; `sc://` URL format | Study Guide |
| 1:10–1:40 | Practise recognising Spark Connect scenarios in question stems | Quick Reference Topic 6 |
| 1:40–2:00 | Topic 6 memory anchors × 5; full recall test | Quick Reference |

**Day 17 Target Questions**: Q91–Q95 (Spark Connect architecture, usage, limitations)

---

#### Day 18 — Pandas API on Spark (2 hours)

| Time | Activity | Resource |
|------|----------|----------|
| 0:00–0:40 | Study Pandas API overview; compare with PySpark DataFrame API | Study Guide Topic 7 |
| 0:40–1:10 | Study conversion functions: to_spark, pandas_api, to_pandas | Quick Reference Topic 7 |
| 1:10–1:40 | Study index types; avoid performance pitfalls | Study Guide |
| 1:40–2:00 | Topic 7 memory anchors × 5; full recall test | Quick Reference |

**Day 18 Target Questions**: Q96–Q100 (Pandas API usage, conversions, limitations)

---

#### Day 19 — Configuration Mastery (2 hours)

| Time | Activity | Resource |
|------|----------|----------|
| 0:00–0:45 | Flash-card all 10 configs from Master Configurations Table | Quick Reference |
| 0:45–1:30 | Practise scenario questions: "What config controls…?" for each property | Study Guide |
| 1:30–2:00 | Focus on most-tested configs: shuffle.partitions, autoBroadcastJoinThreshold | Study Guide |

---

#### Day 20 — Week 3 Practice Test (2 hours)

Run **Mock Test 3** (60 questions, Topics 1–7 mixed). Score and review.

#### Day 21 — Week 3 Error Analysis (1.5 hours)

Review all errors. Focus on Spark Connect and Pandas API (new topics). Re-test weak areas with targeted 10-question mini-tests.

---

### Week 4 — Exam Readiness & Final Simulation

**Week 4 Goal**: Reach exam-ready state with ≥70% on full simulations; build confidence

---

#### Day 22 — Multi-Answer Question Mastery (2 hours)

Dedicated to multi-select (23 questions in Iter 1). Practice elimination strategy.

| Time | Activity |
|------|----------|
| 0:00–0:30 | Review multi-answer strategy (see section below) |
| 0:30–1:30 | Work through 20 practice multi-select questions; apply process |
| 1:30–2:00 | Review errors; identify trigger words ("all that apply", "which of the following are true") |

---

#### Day 23 — Hard Question Focus (2 hours)

Focus exclusively on Hard difficulty questions (20 in Iter 1). These often involve:
- Subtle config value vs config name distinctions
- Edge cases in join strategy selection
- Streaming mode compatibility edge cases
- Multi-hop transformations requiring mental plan execution

---

#### Day 24 — Full Exam Simulation 1 (2.5 hours)

Run **Mock Test 4** (all 100 questions, 2 hours timed). Simulate exam conditions:
- No notes, no reference
- 72 seconds per question average
- Do not second-guess; go with first instinct

Score and categorise: correct / careless mistake / knowledge gap

---

#### Day 25 — Simulation Review & Weak Area Attack (2 hours)

For each wrong answer in Mock Test 4:
1. Identify the topic
2. Re-read the specific concept in STUDY_GUIDE_ITER1.md
3. Create a personal "I was wrong because…" note
4. Write one example that would have given you the right answer

---

#### Day 26 — Final Config & Memory Anchor Review (1.5 hours)

Final recall test of:
- All 10 config properties (name, default, purpose)
- All 35 memory anchors (7 topics × 5 each)
- All join type definitions
- All output mode compatibility rules

---

#### Day 27 — Light Review + Rest (1 hour)

- Quickly scan Quick Reference; no deep study
- Focus on the 10-Point Success Checklist
- Sleep well; exam performance depends on rest

---

#### Day 28 — Exam Day

See Exam Day Strategy section at end of this document.

---

## Mock Test 1 — Foundational Baseline

**Focus**: Topics 1 & 2 (Architecture + Spark SQL)
**Questions**: 40
**Time Limit**: 48 minutes
**Passing Score**: 28/40 (70%)

### Architecture Questions (20)

| Q# | Topic | Concept Tested | Difficulty |
|----|-------|---------------|------------|
| M1-1 | Architecture | SparkSession as unified entry point | Easy |
| M1-2 | Architecture | Driver responsibilities | Easy |
| M1-3 | Architecture | Actions that trigger execution | Easy |
| M1-4 | Architecture | Narrow transformation examples | Easy |
| M1-5 | Architecture | DAGScheduler role | Medium |
| M1-6 | Architecture | Stage boundary operations | Medium |
| M1-7 | Architecture | Tasks per partition relationship | Medium |
| M1-8 | Architecture | Lazy evaluation benefits (multi) | Medium |
| M1-9 | Architecture | `spark.sql.shuffle.partitions` config | Medium |
| M1-10 | Architecture | `spark.sql.autoBroadcastJoinThreshold` | Medium |
| M1-11 | Architecture | Fault tolerance via lineage (multi) | Medium |
| M1-12 | Architecture | Executor memory regions | Medium |
| M1-13 | Architecture | Broadcast variable use case | Medium |
| M1-14 | Architecture | Accumulator semantics | Medium |
| M1-15 | Architecture | coalesce vs repartition | Medium |
| M1-16 | Architecture | `spark.sql.files.maxPartitionBytes` | Hard |
| M1-17 | Architecture | AQE adaptive coalescing | Hard |
| M1-18 | Architecture | Speculative execution config | Hard |
| M1-19 | Architecture | Checkpoint vs cache semantics | Hard |
| M1-20 | Architecture | Stage fault tolerance details | Hard |

### Spark SQL Questions (20)

| Q# | Topic | Concept Tested | Difficulty |
|----|-------|---------------|------------|
| M1-21 | SQL | Basic join type results | Easy |
| M1-22 | SQL | createOrReplaceTempView scope | Easy |
| M1-23 | SQL | COUNT(*) vs COUNT(col) | Easy |
| M1-24 | SQL | INNER JOIN row selection | Easy |
| M1-25 | SQL | Left outer join null-fill behaviour | Medium |
| M1-26 | SQL | LEFT SEMI join semantics | Medium |
| M1-27 | SQL | LEFT ANTI join semantics | Medium |
| M1-28 | SQL | row_number vs rank vs dense_rank | Medium |
| M1-29 | SQL | Window function partitionBy/orderBy | Medium |
| M1-30 | SQL | Aggregate: groupBy with multiple funcs | Medium |
| M1-31 | SQL | ROLLUP subtotal structure | Medium |
| M1-32 | SQL | CUBE combination structure | Medium |
| M1-33 | SQL | Catalyst predicate pushdown | Medium |
| M1-34 | SQL | Catalyst constant folding | Medium |
| M1-35 | SQL | Running total with window frame | Hard |
| M1-36 | SQL | Global temp view scope | Hard |
| M1-37 | SQL | Complex window with lag/lead | Hard |
| M1-38 | SQL | GROUPING SETS semantics | Hard |
| M1-39 | SQL | Catalyst optimisation pipeline order | Hard |
| M1-40 | SQL | BroadcastHashJoin vs SortMergeJoin trigger | Hard |

### Mock Test 1 Scoring Template

```
Architecture Results:    ___/20
Spark SQL Results:       ___/20
Total:                   ___/40  (Target: ≥28)

Easy:   ___/8   Target ≥7    (85%)
Medium: ___/24  Target ≥17   (70%)
Hard:   ___/8   Target ≥5    (65%)

Weak areas identified:
1. _______________
2. _______________
3. _______________
```

---

## Mock Test 2 — Intermediate Focus

**Focus**: Topics 1–3 (Architecture + SQL + DataFrame API)
**Questions**: 50
**Time Limit**: 60 minutes
**Passing Score**: 35/50 (70%)

### DataFrame API Questions (30)

| Q# | Concept | Difficulty |
|----|---------|------------|
| M2-1 | Schema definition with StructType | Easy |
| M2-2 | Reading CSV with options | Easy |
| M2-3 | `filter` syntax with string predicate | Easy |
| M2-4 | `withColumn` to add new column | Easy |
| M2-5 | `write.mode("overwrite")` behaviour | Easy |
| M2-6 | Column reference: 4 methods | Medium |
| M2-7 | `fillna` vs `dropna` semantics | Medium |
| M2-8 | `coalesce(n)` function behaviour | Medium |
| M2-9 | `when().otherwise()` conditional logic | Medium |
| M2-10 | `orderBy(col.desc())` syntax | Medium |
| M2-11 | `dropDuplicates(cols)` vs `distinct()` | Medium |
| M2-12 | Join: multiple key columns | Medium |
| M2-13 | Join: different column names | Medium |
| M2-14 | Parquet partitionBy write | Medium |
| M2-15 | `write.mode("append")` behaviour | Medium |
| M2-16 | UDF Python vs Pandas performance | Medium |
| M2-17 | `pandas_udf` decorator syntax | Medium |
| M2-18 | String function: `regexp_replace` | Medium |
| M2-19 | Date function: `datediff` | Medium |
| M2-20 | `isNull()` vs `isNotNull()` filter | Medium |
| M2-21 | BroadcastHashJoin trigger conditions | Hard |
| M2-22 | `repartition` vs `coalesce` shuffle | Hard |
| M2-23 | Python UDF serialisation penalty | Hard |
| M2-24 | `write.mode("error")` default | Hard |
| M2-25 | `coalesce()` function (SQL function) vs partition op | Hard |
| M2-26 | DDL schema string syntax | Hard |
| M2-27 | Cast type coercion order | Hard |
| M2-28 | Complex UDF with null handling | Hard |
| M2-29 | Pandas UDF Arrow transfer details | Hard |
| M2-30 | Schema inference vs explicit schema | Hard |

### Mock Test 2 Scoring Template

```
Architecture (10):   ___/10
Spark SQL (10):      ___/10
DataFrame API (30):  ___/30
Total:               ___/50  (Target: ≥35)

Easy:   ___/10  Target ≥9
Medium: ___/30  Target ≥21
Hard:   ___/10  Target ≥7

DataFrame API sub-score analysis:
  Column ops:  ___/7
  Read/Write:  ___/6
  UDFs:        ___/5
  Built-ins:   ___/6
  Joins/Sort:  ___/6
```

---

## Mock Test 3 — Advanced Targeting

**Focus**: Topics 4–7 (Tuning + Streaming + Connect + Pandas) + mixed Topics 1–3
**Questions**: 60
**Time Limit**: 72 minutes
**Passing Score**: 42/60 (70%)

### New Topic Sections

| Section | Q Count | Topics |
|---------|---------|--------|
| Troubleshooting | 10 | Data skew, OOM, caching, Spark UI |
| Structured Streaming | 10 | Sources, modes, watermarks, checkpoints |
| Spark Connect | 5 | Architecture, limitations, URL format |
| Pandas API | 5 | Syntax, conversions, limitations |
| Mixed Review | 30 | All topics |

### Troubleshooting Sub-Questions

| Q# | Concept | Difficulty |
|----|---------|------------|
| M3-T1 | Data skew symptom identification | Easy |
| M3-T2 | Small files problem solution | Easy |
| M3-T3 | Cache vs checkpoint trade-offs | Medium |
| M3-T4 | OOM: driver vs executor causes | Medium |
| M3-T5 | `coalesce` before write (small files fix) | Medium |
| M3-T6 | Spark UI: which tab for skew | Medium |
| M3-T7 | AQE skew join config | Medium |
| M3-T8 | `unpersist()` timing | Medium |
| M3-T9 | Salting strategy for skew | Hard |
| M3-T10 | Storage level selection | Hard |

### Streaming Sub-Questions

| Q# | Concept | Difficulty |
|----|---------|------------|
| M3-S1 | Append mode definition | Easy |
| M3-S2 | Checkpoint location option | Easy |
| M3-S3 | Complete mode definition | Medium |
| M3-S4 | `trigger(processingTime="10 seconds")` | Medium |
| M3-S5 | Watermark: drop late data | Medium |
| M3-S6 | Exactly-once requirements | Medium |
| M3-S7 | `trigger(once=True)` behaviour | Medium |
| M3-S8 | Output mode with aggregation | Medium |
| M3-S9 | Watermark + append mode requirement | Hard |
| M3-S10 | Kafka source options | Hard |

### Mock Test 3 Scoring Template

```
Topics 1–3 (Mixed 30):      ___/30
Troubleshooting (10):       ___/10
Structured Streaming (10):  ___/10
Spark Connect (5):          ___/5
Pandas API (5):             ___/5
Total:                      ___/60  (Target: ≥42)

Spark Connect accuracy:  ___/5  (Target ≥4)
Pandas API accuracy:     ___/5  (Target ≥4)
```

---

## Mock Test 4 — Full Simulation

**Focus**: All 7 Topics
**Questions**: 100 (matches real exam)
**Time Limit**: 120 minutes (72 sec/question average)
**Passing Score**: 70/100 (70%)

### Full Exam Distribution

| Topic | Questions | Target Correct | Minimum Passing |
|-------|----------|----------------|-----------------|
| 1. Architecture | 20 | 15 | 12 |
| 2. Spark SQL | 20 | 15 | 12 |
| 3. DataFrame API | 30 | 22 | 18 |
| 4. Troubleshooting | 10 | 7 | 6 |
| 5. Streaming | 10 | 7 | 6 |
| 6. Spark Connect | 5 | 4 | 3 |
| 7. Pandas API | 5 | 4 | 3 |
| **TOTAL** | **100** | **74** | **70** |

### Exam Simulation Rules

1. **No notes** during the test
2. **No reference materials**
3. **Timer set** for 120 minutes
4. **Answer all questions** — no blank answers (no penalty for guessing)
5. **Flag uncertain questions** for review; return if time permits
6. **Do not spend > 3 minutes on any single question** during first pass

### Mock Test 4 Scoring Template

```
Topic 1 — Architecture:         ___/20   (___%)
Topic 2 — Spark SQL:            ___/20   (___%)
Topic 3 — DataFrame API:        ___/30   (___%)
Topic 4 — Troubleshooting:      ___/10   (___%)
Topic 5 — Streaming:            ___/10   (___%)
Topic 6 — Spark Connect:        ___/5    (___%)
Topic 7 — Pandas API:           ___/5    (___%)
─────────────────────────────────────────────────
TOTAL:                          ___/100  (___%)

By Difficulty:
  Easy   (20 total):   ___/20  (___%)   [Target ≥85%]
  Medium (60 total):   ___/60  (___%)   [Target ≥70%]
  Hard   (20 total):   ___/20  (___%)   [Target ≥65%]

By Answer Type:
  Single-answer (77):  ___/77  (___%)
  Multi-answer  (23):  ___/23  (___%)

PASS / FAIL: _______________
```

---

## Common Pitfalls Matrix

### Iteration 1 Specific Traps

| Topic | Common Pitfall | How to Avoid |
|-------|---------------|-------------|
| Architecture | Confusing `spark.default.parallelism` (RDD) with `spark.sql.shuffle.partitions` (SQL) | Exam always says "after a shuffle" → SQL config |
| Architecture | Thinking `coalesce()` causes a shuffle | It doesn't — it only reduces partitions |
| Architecture | Forgetting that `orderBy` is WIDE (causes shuffle) | Global sort must shuffle all data |
| SQL | LEFT SEMI returns only LEFT columns (not right) | "Semi" = partial join; only left side |
| SQL | LEFT ANTI returns NON-matching rows | Anti = opposite; keep what doesn't match |
| SQL | Confusing rank() gaps with dense_rank() | dense = no gaps; rank = gap after tie group |
| DataFrame | `distinct()` works on all columns; `dropDuplicates(cols)` on subset | Know which you need |
| DataFrame | `coalesce(n)` function vs `coalesce()` partition op | In SQL context: `coalesce()` = null fallback function |
| DataFrame | Pandas UDF requires `@pandas_udf` decorator + type hint or return type | Not just any function |
| Streaming | Append mode with aggregation REQUIRES watermark | Without watermark → error or Complete mode needed |
| Streaming | `trigger(once=True)` stops after ONE batch | Use `availableNow=True` for multiple batches |
| Streaming | Complete mode requires aggregation | Can't use Complete on raw non-aggregated stream |
| Spark Connect | `SparkContext` NOT available on client | Only DataFrame/SQL API available |
| Spark Connect | URL format is `sc://host:port` not `spark://` | `sc://` is the Spark Connect prefix |
| Pandas API | `to_pandas()` collects ALL data to driver | Always dangerous on large DataFrames |
| Pandas API | Row order NOT guaranteed | Unlike pandas; Spark is unordered |
| Pandas API | `pyspark.pandas` is the module (not `koalas`) | Koalas was merged into PySpark 3.2+ |

---

### Multi-Answer Trap Patterns

| Pattern | What the Exam Does | Your Defence |
|---------|------------------|--------------|
| "All of the following EXCEPT" | Lists mostly-correct items; one wrong | Check each option independently |
| Partially correct multi-select | One option sounds right but has subtle error | Read every word of each option |
| Near-duplicate options | Two similar-sounding options; only one correct | Look for the differentiating word |
| "Which are TRUE" | Tests exact semantics | Verify each statement as a standalone fact |

---

## Multi-Answer Strategy

### 23 Multi-Answer Questions in Iteration 1

These questions (23% of the exam) require selecting 2–4 correct options. They carry equal weight to single-answer questions.

### Process for Multi-Answer Questions

**Step 1 — Read the full stem carefully**
Identify: What concept is being tested? What qualifies as "correct"?

**Step 2 — Evaluate each option independently**
For each option, ask: "Is this statement TRUE, ignoring all other options?"

**Step 3 — Apply your domain knowledge first**
Do NOT eliminate based on gut feel. Verify each option against what you know.

**Step 4 — Eliminate clear negatives first**
If an option is obviously false, eliminate it. This narrows the selection.

**Step 5 — For borderline options**
Look for: absolute words ("always", "never", "all") — these are often wrong.
Nuanced words ("typically", "usually") — more likely to be correct.

**Step 6 — Review your selection**
Before moving on: "Does this set of answers make logical sense together?"

### Multi-Answer Confidence Scoring

Rate your confidence per option:
- **High confidence correct**: Include it
- **High confidence wrong**: Exclude it
- **Uncertain**: Lean toward inclusion if the statement is generally positive/true
- **Never blank**: Select your best estimate; no penalty for wrong answers

---

## Topic Weighting Study Allocation

### Recommended Study Time by Topic

| Topic | Exam Weight | Recommended Study % | Rationale |
|-------|------------|--------------------|---------|
| 3. DataFrame API | 30% | 30% | Highest weight; most varied sub-topics |
| 1. Architecture | 20% | 20% | Foundation; everything else builds on it |
| 2. Spark SQL | 20% | 20% | Complex joins and window functions |
| 4. Troubleshooting | 10% | 10% | Scenario-based; needs pattern recognition |
| 5. Streaming | 10% | 10% | Mode compatibility; watermark semantics |
| 6. Spark Connect | 5% | 5% | Conceptual; unique to this iteration |
| 7. Pandas API | 5% | 5% | Conceptual; syntax recognition |

### Daily Session Structure (2-hour standard session)

```
0:00–0:10   Review previous session's weak areas (10 min)
0:10–0:50   New concept study (40 min)
0:50–1:20   Practice application / code writing (30 min)
1:20–1:45   Memory anchor recall test for the topic (25 min)
1:45–2:00   Summarise learnings; note questions you're unsure about (15 min)
```

---

## Exam Day Strategy

### Pre-Exam (Night Before)

- Review the 10-Point Success Checklist (Quick Reference)
- Review all 35 Memory Anchors once through
- **Do not study new material** the night before; only review
- Get 8 hours sleep; cognitive performance drops sharply with fatigue

### Pre-Exam (Morning Of)

- Light review of Master Configs Table (10 entries; 15 minutes max)
- Review the Common Pitfalls Matrix briefly
- No deep study; trust your preparation

---

### During the Exam

**Time Management**

| Phase | Duration | Actions |
|-------|----------|---------|
| First pass | 90 min | Answer all 100 questions; flag uncertain |
| Review pass | 25 min | Return to flagged questions |
| Final check | 5 min | Verify no blanks; submit |

**Average pace**: 72 seconds per question on first pass.

---

### Question Attack Strategy

**Easy Questions (20)** — Aim for 100%; no more than 30 seconds each

**Medium Questions (60)** — Apply process; flag if taking > 90 seconds

**Hard Questions (20)** — Best effort; eliminate clearly wrong options; make a decision and move on

---

### Decision Framework for Uncertain Questions

```
Is this a DEFINITION question?
  → Match the exact technical definition to the answer

Is this a CODE question?
  → Walk through the code mentally; apply syntax rules

Is this a SCENARIO question?
  → Map the scenario to the Symptom→Diagnosis→Fix matrix

Is this a CONFIG question?
  → Recall: name, default, what it controls

Still uncertain?
  → Eliminate obvious wrong answers → Pick the "most complete" remaining option
  → NEVER leave blank
```

---

### Topic-Specific Exam Tips

| Topic | Key Tip |
|-------|---------|
| Architecture | Check if question asks about RDD parallelism (default.parallelism) or SQL (shuffle.partitions) |
| SQL | For ranking: write out 4 sample values and apply each function mentally |
| DataFrame | Distinguish `coalesce(n)` partition op vs `coalesce(c1, c2)` null function |
| Troubleshooting | Skew = tail tasks slow; OOM = executor dead; small files = many fast tasks |
| Streaming | Check mode + aggregation compatibility before selecting output mode answer |
| Spark Connect | If question mentions "remote connection" or "gRPC" → Spark Connect |
| Pandas API | If question mentions `pyspark.pandas` or migration from pandas → Pandas API topic |

---

### Final Success Equation

```
Pass = Solid Architecture Foundation
     + Strong DataFrame API (30% of exam!)
     + Join Type Mastery
     + Streaming Mode Fluency
     + Spark Connect Basics (conceptual only)
     + Pandas API Basics (conceptual only)
     + Config Recall (10 key properties)
     + Multi-Answer Discipline
```

---

## Progress Tracking Log

Use this template throughout your 4-week preparation:

```
Week 1 Completion: ___/7 days
Week 2 Completion: ___/7 days
Week 3 Completion: ___/7 days
Week 4 Completion: ___/7 days

Mock Test Scores:
  Mock Test 1: ___/40  (___%)   Date: __________
  Mock Test 2: ___/50  (___%)   Date: __________
  Mock Test 3: ___/60  (___%)   Date: __________
  Mock Test 4: ___/100 (___%)   Date: __________

Topic Mastery Self-Assessment (1=Weak, 5=Strong):
  Topic 1 — Architecture:    ___/5
  Topic 2 — Spark SQL:       ___/5
  Topic 3 — DataFrame API:   ___/5
  Topic 4 — Troubleshooting: ___/5
  Topic 5 — Streaming:       ___/5
  Topic 6 — Spark Connect:   ___/5
  Topic 7 — Pandas API:      ___/5

Exam Date Booked: __________
Ready to book exam? Mock Test 4 ≥70% → YES
```
