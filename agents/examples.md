# Agent Usage Examples

Quick reference for how to use each agent in the agents directory. Use these as starting points-adapt them to your specific challenges.

- [Agent Usage Examples](#agent-usage-examples)
  - [Python Problem-Solving Journey](#python-problem-solving-journey)
    - [1️⃣ Algorithm \& Design Phase](#1️⃣-algorithm--design-phase)
    - [2️⃣ Code Review Phase](#2️⃣-code-review-phase)
    - [3️⃣ Architecture \& Structure](#3️⃣-architecture--structure)
    - [4️⃣ Debugging Phase](#4️⃣-debugging-phase)
    - [5️⃣ Performance Optimization](#5️⃣-performance-optimization)
    - [6️⃣ Testing Strategy](#6️⃣-testing-strategy)
  - [Infrastructure \& DevOps](#infrastructure--devops)
    - [Terraform Module Design](#terraform-module-design)
    - [GitHub Actions CI/CD](#github-actions-cicd)
  - [Real-World Workflow Examples](#real-world-workflow-examples)
    - [Scenario 1: Learning to Solve a New Algorithm Problem](#scenario-1-learning-to-solve-a-new-algorithm-problem)
    - [Scenario 2: Refactoring for Better Architecture](#scenario-2-refactoring-for-better-architecture)
    - [Scenario 3: Building a Pipeline with Infrastructure](#scenario-3-building-a-pipeline-with-infrastructure)
  - [Quick Lookup by Problem Type](#quick-lookup-by-problem-type)
  - [Tips for Getting the Most from Agents](#tips-for-getting-the-most-from-agents)
    - [✅ DO:](#-do)
    - [❌ DON'T:](#-dont)

---

## Python Problem-Solving Journey

### 1️⃣ Algorithm & Design Phase

**When:** You're solving a new problem and need to think through the approach strategically.

```plaintext
@python-algorithm-design
I need to find the most common element in a list of 1 million items.
I've considered sorting and hashing, but I'm not sure which is better for this scale.
What approach should I take?
```

```plaintext
@python-algorithm-design
I'm trying to detect cycles in a directed graph. I know graph algorithms exist,
but I'm not sure which one applies here. Walk me through how I should approach this.
```

```plaintext
@python-algorithm-design
I need to merge K sorted lists efficiently. I have some ideas but want to explore
the trade-offs before implementing. What are my options?
```

---

### 2️⃣ Code Review Phase

**When:** You've written a solution and want feedback before moving forward.

```plaintext
@teaching-assistant
I just implemented a solution to merge K sorted lists using a heap.
Please review my approach for correctness, Pythonic style, and any potential issues.
```

```plaintext
@teaching-assistant
Review my code for:
- Design patterns I should be using
- Performance red flags
- Best practices I might be missing
- Any architectural improvements
```

```plaintext
@teaching-assistant
I used a class-based approach for this utility, but I'm wondering if it's over-engineered.
Is this a good design decision or should I simplify it?
```

---

### 3️⃣ Architecture & Structure

**When:** You need guidance on how to organize or restructure your code.

```plaintext
@python-architecture
I have several utilities for data processing. Currently everything is in one file.
How should I organize this as the module grows? What patterns should I consider?
```

```plaintext
@python-architecture
I'm building a multi-step data pipeline. Should I use classes, functions, or a combination?
What are the trade-offs of each approach for maintainability?
```

```plaintext
@python-architecture
How can I reduce coupling between my parser module and the data transformation logic?
What design patterns might help here?
```

---

### 4️⃣ Debugging Phase

**When:** Your code is broken and you need to figure out why.

```plaintext
@python-debugger
I'm getting a TypeError: 'NoneType' object is not subscriptable on line 42.
Here's my traceback: [paste traceback]
What's causing this and how do I systematically find the root cause?
```

```plaintext
@python-debugger
My function returns incorrect results for edge cases (empty lists, negative numbers).
Expected: [correct output]
Actual: [incorrect output]
What might be wrong in my logic?
```

```plaintext
@python-debugger
My code sometimes works and sometimes fails mysteriously.
It seems like a race condition or state issue. How do I debug this?
```

---

### 5️⃣ Performance Optimization

**When:** Your code works but is too slow.

```plaintext
@python-performance
My function processes a list of 100,000 items and takes 30 seconds.
I think it might be the nested loop, but I'm not sure.
Walk me through how to analyze this algorithmically.
```

```plaintext
@python-performance
I'm concatenating strings in a loop building a large output.
I know this is inefficient, but why and what should I do instead?
```

```plaintext
@python-performance
Here's my recursive solution: [code]
It works for small inputs but times out on large ones.
What's the complexity and how should I think about optimization?
```

---

### 6️⃣ Testing Strategy

**When:** You need to design comprehensive test coverage.

```plaintext
@python-testing
I've written a function that validates email addresses with regex.
What edge cases should I test for? How should I structure my test cases?
```

```plaintext
@python-testing
I'm writing tests for a function that makes API calls and processes results.
What should be mocked vs. real? How do I design this test?
```

```plaintext
@python-testing
My module has multiple interconnected components. How do I design tests
so they're maintainable but also catch real bugs?
```

---

## Infrastructure & DevOps

### Terraform Module Design

**When:** You're planning or reviewing infrastructure-as-code structure.

```plaintext
@terraform-teaching
I'm building a reusable module for AWS VPCs.
What variables should be inputs vs. hardcoded?
How do I balance flexibility with simplicity?
```

```plaintext
@terraform-teaching
My Terraform grows and I have a lot of copy-paste across environments.
How should I structure modules and workspaces to avoid this duplication?
```

```plaintext
@terraform-teaching
I have modules with tight coupling and hard-coded values.
What patterns should I use to decouple them and improve reusability?
```

---

### GitHub Actions CI/CD

**When:** You need help designing or debugging workflows.

```plaintext
@github-actions-teaching
I want to build a matrix workflow that tests my code across Python 3.8 to 3.12.
What's the right approach? How do I structure the matrix and dependencies?
```

```plaintext
@github-actions-teaching
My workflow is failing inconsistently. It passes locally but fails in CI.
What's the right strategy to debug this? What should I check?
```

```plaintext
@github-actions-teaching
I have secrets I need to pass to my workflow. How do I handle this securely?
What's the best practice for secrets management?
```

---

## Real-World Workflow Examples

### Scenario 1: Learning to Solve a New Algorithm Problem

1. **Start with @python-algorithm-design**

   ```plaintext
   I need to implement a solution to the longest common subsequence problem.
   I understand the problem but not sure about the approach.
   Should I use recursion, dynamic programming, or something else?
   What's the thought process?
   ```

2. **Implement your solution**

3. **Review with @teaching-assistant**

   ```plaintext
   I implemented LCS using dynamic programming with memoization.
   Is my approach solid? Any improvements to the code structure?
   ```

4. **If broken → @python-debugger**

   ```plaintext
   My solution gives wrong results on this test case: [example]
   Expected: X, Got: Y
   ```

5. **If slow → @python-performance**

   ```plaintext
   My solution works but is O(n²) space. Can this be optimized?
   What patterns should I research?
   ```

6. **Design tests with @python-testing**

   ```plaintext
   What test cases should I write for LCS?
   What edge cases matter most?
   ```

---

### Scenario 2: Refactoring for Better Architecture

1. **Start with @python-architecture**

   ```plaintext
   I have a 500-line module doing data parsing and transformation.
   How should I split this into separate concerns?
   ```

2. **Review refactoring plan with @teaching-assistant**

   ```plaintext
   Here's my proposed structure. Is this a good design?
   What principles should guide this refactoring?
   ```

3. **If performance changes → @python-performance**

   ```plaintext
   After refactoring to separate modules, performance dropped.
   What might be the cause? How do I diagnose this?
   ```

4. **Test to ensure nothing broke → @python-testing**

   ```plaintext
   I refactored significantly. What test strategy ensures
   I haven't introduced bugs?
   ```

---

### Scenario 3: Building a Pipeline with Infrastructure

1. **Plan infrastructure with @terraform-teaching**

   ```plaintext
   I need to create a data pipeline with compute and storage.
   How should I structure the Terraform? What's the modular approach?
   ```

2. **Automate with @github-actions-teaching**

   ```plaintext
   I want CI/CD that validates infrastructure and deploys on merge.
   What workflow pattern should I use?
   ```

3. **If workflow fails → Debug**

   ```plaintext
   My deployment workflow fails on apply but passes on plan.
   What could cause this and how do I troubleshoot?
   ```

---

## Quick Lookup by Problem Type

| Problem | Agent | Example Prompt |
| ------- | ----- | --------------- |
| "How do I solve this?" | python-algorithm-design | "Walk me through the algorithmic approach" |
| "How should I structure this?" | python-architecture | "Should I use classes or functions here?" |
| "Why is this broken?" | python-debugger | "I get this error: [traceback]. What's wrong?" |
| "Why is this slow?" | python-performance | "This function is O(n²), can it be better?" |
| "What should I test?" | python-testing | "What edge cases should I cover?" |
| "Is this good code?" | teaching-assistant | "Review my solution for patterns and style" |
| "How to structure infrastructure?" | terraform-teaching | "How should I organize these modules?" |
| "How to build this workflow?" | github-actions-teaching | "Design a matrix workflow for multiple versions" |

---

## Tips for Getting the Most from Agents

### ✅ DO:

- Be **specific** about your problem and constraints
- Share **relevant code or configuration** (don't dump everything, focus on the problem area)
- Explain **what you've already considered**
- Ask **follow-up questions** if something isn't clear
- **Iterate** — test ideas, come back with results

### ❌ DON'T:

- Ask for complete, ready-to-use implementations (agents guide, don't write code)
- Skip context (harder for agent to help without understanding your situation)
- Expect code in copy-paste form (learn the concepts instead)
- Stop after first answer (engage more deeply to understand the principles)

---

**Need help choosing an agent?** See [README.md](README.md) for detailed descriptions of each agent's strengths.
