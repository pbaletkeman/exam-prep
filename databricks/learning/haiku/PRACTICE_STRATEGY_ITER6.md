# Databricks Certified Associate Developer for Apache Spark — Iteration 6 Practice Strategy

**3-Week Study Plan & Mock Test Suites (Iteration 6)**

**Last Updated**: May 17, 2026

---

## Table of Contents

1. [Study Plan Overview](#study-plan-overview)
2. [Week 1: Foundation (Topics 1–2)](#week-1-foundation-topics-1--2)
3. [Week 2: Application (Topics 3–4)](#week-2-application-topics-3--4)
4. [Week 3: Advanced + Testing (Topics 5–7)](#week-3-advanced--testing-topics-5--7)
5. [Mock Test Suites](#mock-test-suites)
6. [Exam Day Strategy](#exam-day-strategy)
7. [Success Tracking](#success-tracking)

---

## Study Plan Overview

**Duration**: 3 weeks, 21 hours total (3 hours/day, 7 days/week)

**Daily Structure**:
- **First 1.5 hours**: Concept review from STUDY_GUIDE_ITER6.md
- **Next 1 hour**: Practice questions with detailed review
- **Final 30 min**: Flashcard review, weak area drills

**Difficulty Progression**:
- Week 1: Fundamentals (easy + medium questions)
- Week 2: Application & edge cases (medium + hard questions)
- Week 3: Advanced topics + comprehensive testing (all difficulty levels)

**Target Metrics**:
- **Minimum passing**: 75/100 (75%)
- **Stretch goal**: 80/100 (80%)
- **Mock test scores should trend upward** across Week 1 → Week 2 → Week 3

---

## Week 1: Foundation (Topics 1–2)

### Day 1: Spark Architecture Core (Q1–Q10 focus)

**Learning Objectives**:
- Understand RDD vs DataFrame caching mechanisms
- Distinguish FIFO from FAIR scheduling modes
- Explain DAGScheduler vs TaskScheduler responsibilities
- Recognize barrier execution mode use cases

**Concept Review** (90 min):
1. Read STUDY_GUIDE_ITER6: **Sections 1.1–1.5**
   - RDD cache defaults (MEMORY_ONLY)
   - DataFrame cache defaults (MEMORY_AND_DISK)
   - FIFO vs FAIR scheduler modes
   - DAG scheduling and task scheduling layers
   - Barrier execution mode and synchronized task launch
2. Create comparison matrix: RDD vs DataFrame caching
3. Trace example: "How does barrier mode handle task failure?" (entire stage replays)

**Practice Questions** (60 min):
- Review Q1, Q2, Q3, Q4, Q5 from spark-databricks-iteration-6.md
- For each question:
  - Answer without looking at answer key
  - Check your answer against key
  - If incorrect, re-read relevant STUDY_GUIDE section
  - Note the exact concept gap
- **Scoring Target**: 4/5 correct (80%)

**Flashcard Drills** (30 min):
- Create 5 flashcards:
  - RDD cache default? → MEMORY_ONLY
  - DataFrame cache default? → MEMORY_AND_DISK
  - When to use FAIR scheduler? → Shared clusters with concurrent jobs
  - What does DAGScheduler track? → Stage dependencies, shuffle boundaries
  - How long do barrier tasks wait? → Until all are ready or timeout

---

### Day 2: Spark Architecture Advanced (Q6–Q15 focus)

**Learning Objectives**:
- Explain Python worker memory constraints
- Understand dynamic resource allocation and shuffle tracking
- Recognize worker vs executor lifecycle
- Analyze recovery strategies for executor loss

**Concept Review** (90 min):
1. Read STUDY_GUIDE_ITER6: **Sections 1.6–1.10**
   - Python worker memory isolation
   - Shuffle tracking and DRA enablement
   - Worker daemon vs executor process model
   - Proactive replication benefits
   - Non-equi join strategies
2. Diagram: Worker → Executor relationship
3. Scenario: "What happens if an executor with shuffle data is lost?"

**Practice Questions** (60 min):
- Review Q6, Q7, Q8, Q9, Q10 from question bank
- Trace through each scenario:
  - Q7: coalesce(n) with various partition counts
  - Q8: Barrier mode task failure recovery
  - Q10: Locality wait overrides
- **Scoring Target**: 4/5 correct

**Flashcard Drills** (30 min):
- Key concepts:
  - `spark.executor.pyspark.memory` purpose? → Off-heap budget for Python workers
  - Shuffle tracking benefit? → DRA can remove executors without blocking
  - Worker daemon responsibility? → Register with Master, launch executors
  - Proactive replication trigger? → Executor eviction (DRA), loss detected
  - coalesce() can increase partitions? → NO (narrow transformation only)

---

### Day 3: Spark Architecture Completion (Q11–Q20 focus)

**Learning Objectives**:
- Analyze cluster deploy mode driver lifecycle
- Understand data locality wait mechanics
- Recognize application naming and ID generation
- Connect all architecture concepts

**Concept Review** (90 min):
1. Read STUDY_GUIDE_ITER6: **Sections 1.11–1.20**
   - Cluster deploy mode driver behavior
   - Data locality wait transitions
   - Driver supervision in Standalone mode
   - Two-level hash map aggregation
   - Event log compression
   - Stage recomputation on executor loss
2. Comparison: Cluster mode vs Client mode
3. Scenario: "Why does compression reduce memory without full recompute?"

**Practice Questions** (60 min):
- Review Q11–Q20 from question bank
- Detailed trace:
  - Q11: Cluster deploy mode driver reconnection
  - Q12: Locality wait overrides per transition
  - Q15: Driver supervision in different cluster managers
  - Q19: Shuffle data recovery with/without external service
  - Q20: Application ID generation across simultaneous submissions
- **Scoring Target**: 4/5 correct

**Flashcard Drills** (30 min):
- Key distinctions:
  - Cluster mode driver where? → On cluster node (logs on cluster)
  - Client mode driver where? → On submitting machine
  - Locality wait for PROCESS_LOCAL→NODE_LOCAL? → `spark.locality.wait.process` override
  - Two-level hash map what for? → Cache efficiency + reduced GC pressure
  - Event log compression codec? → Default = zstd

**End-of-Day Check**: Complete practice quiz on Q1–Q20; target 16/20 (80%)

---

### Day 4: Spark SQL Fundamentals (Q21–Q30 focus)

**Learning Objectives**:
- Master date/time function return types
- Understand safe arithmetic operations
- Learn regex function distinctions
- Recognize NULL handling patterns

**Concept Review** (90 min):
1. Read STUDY_GUIDE_ITER6: **Sections 2.1–2.10**
   - Date/time functions (make_date, unix_date, date_from_unix_date)
   - Safe arithmetic (try_divide, try_add)
   - Regex functions (regexp_like, regexp_extract, regexp_count)
   - NULL handling in aggregates
   - Array functions (array_compact, array_distinct, array_remove)
2. Create function reference card with return types
3. Test: "What does `make_date(2026, 13, 5)` return?" → `NULL` (invalid month)

**Practice Questions** (60 min):
- Review Q21–Q30 from question bank
- Function signature verification:
  - Q21: make_date return type? Behavior on invalid input?
  - Q22: unix_date return type and interpretation
  - Q23: try_divide vs regular division
  - Q24: regexp_like vs regexp_extract return types
  - Q25–Q30: Array function behavior, edge cases
- **Scoring Target**: 5/10 correct (50% is acceptable for new functions)

**Flashcard Drills** (30 min):
- Function flashcards:
  - `make_date(y,m,d)` returns? → DateType (not string; null if invalid)
  - `unix_date()` returns? → IntegerType days (not seconds!)
  - `try_divide(10, 0)` returns? → NULL (not exception)
  - `regexp_like()` returns? → BooleanType
  - `regexp_extract()` returns? → StringType (captured group text)
  - `array_compact()` does what? → Remove NULL; preserve order

---

### Day 5: Spark SQL Functions (Q31–Q40 focus)

**Learning Objectives**:
- Understand aggregate function NULL semantics
- Master string parsing functions (from_csv vs from_json)
- Recognize data type inference functions
- Connect SQL concepts to architecture

**Concept Review** (90 min):
1. Read STUDY_GUIDE_ITER6: **Sections 2.11–2.20**
   - bool_and / bool_or NULL handling
   - Aggregate functions (bit_and, bit_or, bit_xor, product)
   - String parsing (inline, from_csv, from_json)
   - Schema inference functions
   - Date arithmetic and safe operations
2. Decision table: When to use `from_csv` vs `from_json`
3. Scenario: "Why does `from_csv()` not support nested arrays?"

**Practice Questions** (60 min):
- Review Q31–Q40 from question bank
- Deep dives:
  - Q31: bool_and NULL handling vs simple AND operator
  - Q32: Nested struct construction with `named_struct`
  - Q33: from_csv limitations vs from_json capabilities
  - Q34: schema_of_csv inference results
  - Q35–Q40: Edge cases and return type confirmations
- **Scoring Target**: 6/10 correct

**Flashcard Drills** (30 min):
- Aggregate behavior:
  - `bool_and([true, true, NULL])` returns? → `true` (NULL ignored)
  - `bool_or([false, false, NULL])` returns? → `false` (NULL ignored)
  - `product([2, 3, NULL])` returns? → `6` (NULL ignored)
  - `cardinality(NULL)` returns? → `NULL` (not empty!)
  - `size(NULL)` returns? → `-1` (with default `spark.sql.legacy.sizeOfNull=false`)

**End-of-Week Check**: Complete full practice quiz on Q1–Q40; target 32/40 (80%)

---

### Day 6–7: Week 1 Review & Practice Drills

**Saturday (Day 6)**: Deep Review & Reinforcement (3 hours)
- **90 min**: Re-read QUICK_REFERENCE memory anchors for Topics 1–2
- **60 min**: Timed drill on Q1–Q20 (20 questions in 30 minutes)
- **30 min**: Timed drill on Q21–Q40 (20 questions in 30 minutes)
- **Target**: 32/40 total (80%)

**Sunday (Day 7)**: Rest + Light Review (2 hours)
- **60 min**: Create personalized flashcard deck with weak topics
- **60 min**: Casual review of flashcards (no pressure)
- **Evening**: Rest & prepare mentally for Week 2

**Week 1 Assessment**:
- ✓ Passed Q1–Q20 drill? (target 16/20)
- ✓ Passed Q21–Q40 drill? (target 16/20)
- ✓ Can explain RDD vs DataFrame caching without notes?
- ✓ Can distinguish FIFO vs FAIR scheduler in your own words?

---

## Week 2: Application (Topics 3–4)

### Day 1–2: DataFrame API Part 1 (Q41–Q55 focus)

**Learning Objectives**:
- Master DataFrame transformations and HOFs
- Understand checkpoint eager vs lazy
- Recognize write semantics and partitioning

**Concept Review** (180 min across 2 days):
1. Read STUDY_GUIDE_ITER6: **Sections 3.1–3.10**
   - Stratified sampling (sampleBy)
   - Checkpointing (eager vs lazy)
   - Aggregation (product)
   - Schema projection (to)
   - HOF operations (transform_keys, transform_values, zip_with)
   - Struct field operations (withField, dropFields)
2. Hands-on: Simulate DataFrame transformations in pseudocode
3. Edge cases: "What if `sampleBy()` key is not in fractions dict?"

**Practice Questions** (60–120 min):
- Review Q41–Q55 from question bank
- Trace through each transformation:
  - Q41: sampleBy row counts per stratum
  - Q42: checkpoint eager=True vs eager=False timing
  - Q43: product aggregate NULL handling
  - Q44: to() schema projection vs select()
  - Q45–Q55: HOF chain behavior, struct updates, array functions
- **Scoring Target**: 9/15 correct

---

### Day 3–4: DataFrame API Part 2 & Tuning (Q56–Q80 focus)

**Learning Objectives**:
- Understand write modes and partitioning directory structure
- Recognize AQE skew join handling
- Master code generation and off-heap memory
- Analyze performance configurations

**Concept Review** (180 min):
1. Read STUDY_GUIDE_ITER6: **Sections 3.11–3.20 + 4.1–4.10**
   - Write APIs (writeTo, createOrReplace vs append)
   - Partitioning behavior and file layout
   - Cross joins with guarding configuration
   - AQE skew handling (skew detection, splitting, replication)
   - Code generation (whole-stage, field limits)
   - Off-heap configuration and Tungsten
2. Diagram: Write partitioning directory structure
3. Trade-off analysis: Performance vs memory vs CPU

**Practice Questions** (60–120 min):
- Review Q56–Q80 from question bank
- Complex scenarios:
  - Q56: writeTo createOrReplace atomicity
  - Q57–Q60: Partitioning and file layout
  - Q61–Q65: CrossJoin guard and Cartesian products
  - Q66–Q70: Array/map HOFs and safe access
  - Q71–Q80: AQE, codegen, off-heap, Kryo
- **Scoring Target**: 12/25 correct (48% acceptable for tuning topics)

**End-of-Week Check**: Complete full practice quiz on Q41–Q80; target 48/40 (80%)

---

### Day 5–7: Week 2 Review & Mock Test 1

**Thursday (Day 5)**: DataFrame API Review (3 hours)
- **90 min**: Deep dive into weak DataFrame topics
- **90 min**: Timed drill Q41–Q70 (30 questions in 45 minutes)
- **Target**: 24/30 (80%)

**Friday (Day 6)**: Tuning & Configuration Review (3 hours)
- **90 min**: Re-read Tuning sections 4.1–4.10
- **90 min**: Timed drill Q71–Q80 (10 questions in 15 minutes)
- **Target**: 8/10 (80%)

**Saturday (Day 7)**: MOCK TEST 1 — Full Exam Simulation (3 hours)

**Mock Test 1 Execution**:
- **Timing**: 120 minutes for all 100 questions
- **Environment**: Quiet space, no reference materials, no interruptions
- **Questions**: Use Q1–Q100 from spark-databricks-iteration-6.md
- **Format**: Record score, time per section, weak topics

**Mock Test 1 Scoring**:
```
Q1–Q20 (Architecture): ___/20
Q21–Q40 (SQL): ___/20
Q41–Q70 (DataFrame): ___/30
Q71–Q80 (Tuning): ___/10
Q81–Q90 (Streaming): ___/10
Q91–Q95 (Spark Connect): ___/5
Q96–Q100 (Pandas API): ___/5
------------------------
TOTAL SCORE: ___/100
PASS/FAIL: (≥75 = PASS, <75 = NEEDS WORK)
```

**Post-Test Analysis** (2 hours):
- Identify questions answered incorrectly
- Group by topic to find patterns
- Re-read STUDY_GUIDE sections for top 3 weak areas
- Update weak topic flashcards

---

## Week 3: Advanced + Testing (Topics 5–7)

### Day 1–2: Streaming Fundamentals (Q81–Q90 focus)

**Learning Objectives**:
- Master streaming trigger modes and semantics
- Understand watermarks and late data
- Recognize Kafka source characteristics
- Learn stateful streaming operations

**Concept Review** (180 min):
1. Read STUDY_GUIDE_ITER6: **Sections 5.1–5.10**
   - Trigger modes (once vs availableNow vs continuous)
   - Progress metrics (inputRowsPerSecond vs processedRowsPerSecond)
   - Watermarks and late data thresholds
   - Session windows (gap-based, not fixed)
   - Kafka source schema and schema requirement
   - Consumer group risks
   - Rate limiting (maxOffsetsPerTrigger)
2. Streaming state machine: Understand micro-batch sequencing
3. Edge case: "What if Kafka consumer group is shared across 2 queries?"

**Practice Questions** (60–120 min):
- Review Q81–Q90 from question bank
- Streaming logic verification:
  - Q81: trigger(once) vs trigger(availableNow) – micro-batch behavior
  - Q82: Progress metrics difference
  - Q83: Watermark and late data threshold calculation
  - Q84: Console sink limitations
  - Q85–Q90: Session windows, Kafka schema, group IDs, state recovery
- **Scoring Target**: 7/10 correct

---

### Day 3–4: Spark Connect & Pandas API (Q91–Q100 focus)

**Learning Objectives**:
- Understand Spark Connect error timing and client-server model
- Recognize token authentication
- Learn Pandas API on Spark NULL semantics
- Understand index type trade-offs

**Concept Review** (180 min):
1. Read STUDY_GUIDE_ITER6: **Sections 6.1–7.5**
   - Analysis exception error surfacing (action time, not transformation time)
   - Token authentication in gRPC URL
   - Python UDF serialization and execution
   - Client survivability on server crash
   - Pandas API caching and explain
   - Index type performance trade-offs
   - NULL vs NaN handling differences
   - Delta writing from Pandas API
2. Architecture: Client ↔ gRPC ↔ Server with UDF serialization
3. Edge case: "How does Pandas API on Spark handle NaN in sum()?"

**Practice Questions** (60–120 min):
- Review Q91–Q100 from question bank
- Advanced topics:
  - Q91–Q95: Spark Connect error timing, auth, UDFs, crashes
  - Q96–Q100: Pandas API on Spark (caching, index types, NULL/NaN)
- **Scoring Target**: 8/10 correct

---

### Day 5: Final Review & Mock Test 2 (3 hours)

**Mock Test 2 Execution** (120 minutes):
- Use Q1–Q100 again (can re-attempt to improve understanding)
- Record scores and compare to Mock Test 1
- **Improvement Target**: +5 points from Mock Test 1

**Post-Test Analysis** (60 min):
- Review incorrect answers
- Focus on topics still below 80% pass rate
- Update weak-area flashcards

**Scoring Goal for Mock Test 2**: ≥80/100 (80%)

---

### Day 6: Comprehensive Review (3 hours)

**Targeted Deep Dive**:
- **60 min**: Review QUICK_REFERENCE memory anchors (all 7 topics)
- **90 min**: Timed drills on historically weak topics
- **30 min**: Flashcard review (rapid-fire 50 flashcards)

**Competency Check**:
- ✓ Can explain streaming watermark behavior in <2 minutes?
- ✓ Can distinguish NULL vs NaN in Pandas API on Spark?
- ✓ Can trace Spark Connect error surfacing without notes?

---

### Day 7: Final Exam Preparation & Mock Test 3

**Final Review** (90 min):
- Light review of QUICK_REFERENCE (no heavy studying)
- Verify all function signatures and return types
- Mental preparation and confidence building

**Mock Test 3 Execution** (120 minutes):

**Full Exam Simulation**:
```
Conditions:
- 120 minutes for all 100 questions
- No reference materials
- Quiet environment
- Timed sections (track pace)
```

**Scoring Rubric**:
```
Q1–Q20 (Architecture): ___/20
Q21–Q40 (SQL): ___/20
Q41–Q70 (DataFrame): ___/30
Q71–Q80 (Tuning): ___/10
Q81–Q90 (Streaming): ___/10
Q91–Q95 (Spark Connect): ___/5
Q96–Q100 (Pandas API): ___/5
------------------------
TOTAL SCORE: ___/100

SUCCESS CRITERIA:
- ≥75: PASS (eligible for exam)
- ≥80: STRETCH GOAL (confident)
- <75: NEEDS MORE PREP (review weak areas)
```

**Post-Test Review** (60 min):
- Analyze any remaining errors
- For any persistent weak spots, re-read relevant STUDY_GUIDE section
- Celebrate progress from Mock Test 1 → Mock Test 3

**Rest & Preparation**:
- Evening: Light dinner, early rest
- Day before exam: Light review (30 min), mental preparation, avoid cramming
- Exam day: Breakfast, hydration, arrive early, stay confident

---

## Mock Test Suites

### Mock Test 1 (Mid-Week 2)

**Question Selection** (100 questions):
- Q1–Q20: Architecture & Internals (all difficulty)
- Q21–Q40: Spark SQL (all difficulty)
- Q41–Q70: DataFrame API (easy–hard)
- Q71–Q80: Tuning (medium–hard)
- Q81–Q90: Streaming (medium–hard)
- Q91–Q95: Spark Connect (medium–hard)
- Q96–Q100: Pandas API (medium)

**Timing**: 120 minutes (1 min 12 sec per question)

**Scoring Template**:
```
Section | Count | Score | Notes
--------|-------|-------|-------
Arch    |   20  | __/20 | Weak in [topic]?
SQL     |   20  | __/20 |
Frame   |   30  | __/30 |
Tuning  |   10  | __/10 |
Stream  |   10  | __/10 |
Connect |    5  | __/5  |
Pandas  |    5  | __/5  |
--------|-------|-------|-------
TOTAL   |  100  | __/100| Pass? ≥75?
```

**Post-Test Actions**:
1. Identify 3 weak topics
2. Re-read relevant STUDY_GUIDE sections (1 hour)
3. Create targeted flashcards for weak topics
4. Schedule 30-min drill on weak topics (before Day 3)

---

### Mock Test 2 (End-Week 3)

**Question Selection**: Same 100 questions as Mock Test 1 (or alternate set if preferred)

**Key Differences from Mock Test 1**:
- You now have 1.5 weeks of study behind you
- Should recognize questions you struggled with before
- **Goal**: Demonstrate 5–10 point improvement over Mock Test 1

**Scoring Template**: Same as Mock Test 1

**Improvement Tracking**:
```
Topic    | Mock 1 | Mock 2 | Change | Target
---------|--------|--------|---------|-------
Arch     | __/20  | __/20  | +__     | 18/20
SQL      | __/20  | __/20  | +__     | 18/20
Frame    | __/30  | __/30  | +__     | 27/30
Tuning   | __/10  | __/10  | +__     | 9/10
Stream   | __/10  | __/10  | +__     | 9/10
Connect  | __/5   | __/5   | +__     | 4/5
Pandas   | __/5   | __/5   | +__     | 4/5
---------|--------|--------|---------|-------
TOTAL    | __/100 | __/100 | +__     | 80/100
```

---

### Mock Test 3 (Final Day of Week 3)

**Question Selection**: Same 100 questions as Mock Tests 1 & 2

**Highest-Stakes Simulation**:
- **Final confidence checkpoint** before real exam
- Simulate exact exam conditions (quiet, timed, no materials)
- **Goal**: Achieve ≥80/100 (80%)

**Scoring Template**: Same as Mock Test 1

**Success Criteria**:
- **Minimum**: 75/100 (eligible to take real exam)
- **Stretch Goal**: 80/100 (high confidence)
- **Excellent**: 85+/100 (mastery)

**If ≥75/100**:
- ✓ Ready for real exam
- Celebrate, rest, prepare mentally for exam day

**If <75/100**:
- Identify specific weak topics
- Commit to 4–5 hours of targeted review before real exam
- Consider delaying exam by 1 week for additional prep

---

## Exam Day Strategy

### Pre-Exam (24 Hours Before)

**1 Hour Before Bed**:
- Light review of QUICK_REFERENCE (memory anchors only, no deep study)
- Walk through 1–2 easy questions to build confidence
- Visualize successful exam completion

**Night Before**:
- Set 2 alarms
- Prepare clothing and materials (ID, exam confirmation)
- Early sleep (target 8 hours)

### Exam Morning

**2 Hours Before Exam**:
- Light breakfast (protein + carbs)
- Hydration (water, not caffeine)
- 15-min review of key function return types (flashcards)
- Avoid cramming new material

**30 Minutes Before**:
- Arrive at testing center early
- Use restroom
- Take 5 deep breaths to calm nerves
- Positive self-talk ("I've prepared well; I know this material")

### During Exam (120 minutes)

**Time Allocation** (120 minutes / 100 questions = 1.2 min per question):

| Section | Questions | Time | Pace |
|---------|-----------|------|------|
| Q1–Q20  | 20        | 25 min | 1.25 min/q |
| Q21–Q40 | 20        | 25 min | 1.25 min/q |
| Q41–Q70 | 30        | 36 min | 1.2 min/q |
| Q71–Q80 | 10        | 12 min | 1.2 min/q |
| Q81–Q90 | 10        | 12 min | 1.2 min/q |
| Q91–Q100| 10        | 10 min | 1.0 min/q |
| TOTAL   | 100       | 120 min| |

**Strategy by Question Type**:

**Multiple Choice (1 answer)** (1 min/question):
1. Read question and all 4 options
2. Eliminate 1–2 obviously wrong options
3. Choose between remaining options
4. Flag for review if uncertain

**Select All That Apply** (1.5 min/question):
1. Read the question carefully (note "select all")
2. Evaluate each option independently (true/false for each)
3. Mark each option accordingly
4. Double-check before moving forward

**Management**:
- **First Pass** (90 min): Answer all questions (mark uncertain ones)
- **Review Pass** (20 min): Return to flagged questions; make final decisions
- **Final Check** (10 min): Verify no blank answers; spot-check logic

### Answer Strategy by Topic

**Architecture (Q1–Q20)**:
- Focus on **default behaviors** and **configuration names**
- Eliminate options with wrong component (e.g., "TaskScheduler determines stages" = wrong, that's DAGScheduler)
- Verify return types and default values

**SQL (Q21–Q40)**:
- Verify **function return types** (make_date → DateType, not string)
- Check **NULL handling** (NULL vs exception vs special values)
- Trace through examples mentally

**DataFrame (Q41–Q70)**:
- Trace through **transformation chains** step-by-step
- Verify **column names** and **schema projection** results
- Check **write semantics** (createOrReplace vs append)

**Tuning (Q71–Q80)**:
- Focus on **configuration trade-offs** (memory vs CPU vs performance)
- Understand **side effects** of enabling/disabling features
- Recognize **when optimizations apply** (not universal)

**Streaming (Q81–Q90)**:
- Verify **trigger mode behavior** (micro-batch count, latency)
- Check **watermark math** (threshold = watermark − delay)
- Understand **state persistence** and **recovery semantics**

**Spark Connect (Q91–Q95)**:
- Focus on **error timing** (action time, not transformation time)
- Verify **authentication** and **serialization** details
- Check **client-server** behavior

**Pandas API (Q96–Q100)**:
- Distinguish **NULL vs NaN** handling
- Verify **index type performance** trade-offs
- Check **API method** behavior (cache, explain, write)

### Post-Exam

**Immediately After**:
- Rest (1–2 hours)
- Reflect on exam experience (what went well, what was challenging)
- Avoid obsessing over individual questions

**Within 24 Hours**:
- Check exam results (most systems provide immediate feedback)
- Celebrate passing or plan next steps if needed

---

## Success Tracking

### Daily Progress Checklist

**Each Day, Check Off**:
- ☐ Completed concept review (90 min)
- ☐ Completed practice questions (60 min)
- ☐ Completed flashcard drills (30 min)
- ☐ Scored ≥70% on practice questions
- ☐ Updated weak-topic flashcards
- ☐ Felt confident with today's material

### Weekly Assessment

**End of Each Week**:
- ☐ Completed all 21 hours (3 hours × 7 days)
- ☐ Mock test score ≥70/100
- ☐ Identified weak topics for next week
- ☐ Updated overall progress chart

**Progress Tracking Chart**:
```
Week | Topics | Mock Score | Status | Next Focus
-----|--------|-----------|--------|-------------
  1  | 1–2    | __/100    | ✓/✗    | [weak topic]
  2  | 3–4    | __/100    | ✓/✗    | [weak topic]
  3  | 5–7    | __/100    | ✓/✗    | Ready for exam
```

### Red Flags

**If You See These, Take Action**:
- ☑ Mock test score <70/100 after Week 1 → Add 1 extra study hour daily
- ☑ Consistently weak in same topic → Re-read STUDY_GUIDE section; find YouTube explanation
- ☑ Feeling overwhelmed → Break into smaller daily goals; take 1 rest day
- ☑ Time management issues → Practice timed drills daily (15 min each)

### Final Readiness Checklist

**Before Taking Real Exam**:
- ☐ Scored ≥80/100 on Mock Test 3?
- ☐ Can explain all 7 topics in your own words?
- ☐ Comfortable with function return types and NULL handling?
- ☐ Understand configuration trade-offs and defaults?
- ☐ Confident with streaming and Spark Connect concepts?
- ☐ Ready to manage 120 minutes and stay calm?

**If All Boxes Checked**: **YOU ARE READY FOR THE EXAM**

---

**End of Practice Strategy (Iteration 6)**

Use this 3-week plan alongside STUDY_GUIDE_ITER6.md and QUICK_REFERENCE_ITER6.md to achieve exam success.

**Final Reminder**: Consistent daily effort (3 hours/day for 3 weeks) beats last-minute cramming. Trust the process, stay disciplined, and celebrate progress!
