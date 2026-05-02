# Agents Directory

This directory contains custom teaching and mentoring agents designed to guide intermediate-to-experienced developers through learning and problem-solving without providing direct solutions. Each agent specializes in a specific domain and emphasizes guided discovery and conceptual understanding.

- [Agents Directory](#agents-directory)
  - [Overview](#overview)
  - [Agents](#agents)
    - [Python Agents](#python-agents)
      - [python-algorithm-design.agent.md](#python-algorithm-designagentmd)
      - [Algorithm Design Mentor](#algorithm-design-mentor)
      - [python-architecture.agent.md](#python-architectureagentmd)
        - [Code Architecture Advisor](#code-architecture-advisor)
      - [python-debugger.agent.md](#python-debuggeragentmd)
        - [Python Debugger Assistant](#python-debugger-assistant)
      - [python-performance.agent.md](#python-performanceagentmd)
        - [Python Performance Specialist](#python-performance-specialist)
      - [python-testing.agent.md](#python-testingagentmd)
        - [Python Testing Specialist](#python-testing-specialist)
      - [teaching-assistant.agent.md](#teaching-assistantagentmd)
        - [Python Teaching Assistant](#python-teaching-assistant)
    - [Infrastructure Agents](#infrastructure-agents)
      - [terraform-teaching.agent.md](#terraform-teachingagentmd)
        - [Terraform Teaching Assistant](#terraform-teaching-assistant)
    - [DevOps Agents](#devops-agents)
      - [github-actions-teaching.agent.md](#github-actions-teachingagentmd)
        - [GitHub Actions Teaching Assistant](#github-actions-teaching-assistant)
  - [How to Use These Agents](#how-to-use-these-agents)
    - [1. Choose the Right Agent](#1-choose-the-right-agent)
    - [2. Provide Context](#2-provide-context)
    - [3. Engage in Guided Discovery](#3-engage-in-guided-discovery)
    - [4. Learn the Underlying Concepts](#4-learn-the-underlying-concepts)
  - [Common Patterns Across Agents](#common-patterns-across-agents)
  - [Quick Reference](#quick-reference)
  - [Getting Started](#getting-started)

## Overview

All agents in this directory follow a consistent philosophy:

- **Guide thinking, don't solve problems** - Help you discover solutions, don't provide them
- **Teach concepts** - Explain principles and frameworks to build understanding
- **Encourage independence** - Build skills and confidence through guided exploration
- **Balance support with challenge** - Provide enough guidance to make progress without removing the learning value

## Agents

### Python Agents

#### [python-algorithm-design.agent.md](python-algorithm-design.agent.md)

#### Algorithm Design Mentor

Guides algorithmic thinking and problem-solving strategy without implementing solutions.

**Core Focus:**

- Break down complex problems into manageable pieces
- Identify applicable algorithms and data structures
- Understand trade-offs between different approaches
- Think algorithmically rather than procedurally
- Recognize problem patterns (graph, dynamic programming, greedy, etc.)

**Use When:**

- "Solve this problem"
- "Algorithm design approach"
- "How should I approach this problem?"
- Need to explore multiple solution strategies

**Constraints:** Never provides algorithm implementations; shows pseudocode and conceptual outlines instead.

---

#### [python-architecture.agent.md](python-architecture.agent.md)

##### Code Architecture Advisor

Guides structural decisions, design patterns, and architectural trade-offs without rewriting code.

**Core Focus:**

- Make intentional architectural decisions aligned with requirements
- Apply design patterns appropriately (avoiding cargo-cult patterns)
- Balance flexibility, maintainability, and simplicity
- Understand coupling, cohesion, and dependency flows
- Design for change without overengineering

**Use When:**

- "Architecture review"
- "Code structure and design patterns"
- "How should I organize this code?"
- "Refactoring approach and strategy"
- Scalability and modularity decisions

**Constraints:** Never rewrites code structure or refactors codebase; suggests better structures conceptually.

---

#### [python-debugger.agent.md](python-debugger.agent.md)

##### Python Debugger Assistant

Diagnoses runtime errors, logic bugs, and unexpected behavior through systematic debugging guidance.

**Core Focus:**

- Understand what went wrong and why
- Trace execution flow to identify failure points
- Form and test hypotheses about root causes
- Develop systematic debugging skills
- Understand actual vs. expected behavior

**Use When:**

- "Debug my Python code"
- "Why is this failing?"
- "Something is broken or behaving unexpectedly"
- Runtime errors or logic bugs
- Unexpected behavior with errors/tracebacks

**Constraints:** Never provides working code to fix issues; explains what's wrong and guides debugging process.

---

#### [python-performance.agent.md](python-performance.agent.md)

##### Python Performance Specialist

Analyzes algorithmic complexity, optimization opportunities, and performance trade-offs.

**Core Focus:**

- Understand algorithmic complexity (Big O, space complexity)
- Identify actual performance bottlenecks through analysis
- Evaluate performance trade-offs (speed vs. clarity, memory vs. time)
- Learn optimization patterns and techniques
- Profile and measure before optimizing

**Use When:**

- "Optimize my code"
- "Performance bottleneck identification"
- "Slow algorithm improvement"
- "Big O analysis and memory efficiency"
- "Caching strategy and concurrency patterns"

**Constraints:** Never provides optimized implementations; explains complexity conceptually and suggests patterns.

---

#### [python-testing.agent.md](python-testing.agent.md)

##### Python Testing Specialist

Guides test design, coverage strategy, and test quality without writing actual tests.

**Core Focus:**

- Think through what needs to be tested (behavior, not implementation)
- Identify edge cases and boundary conditions
- Design test structure and organization
- Understand mocking, fixtures, and test isolation
- Balance test coverage with test maintainability

**Use When:**

- "Design tests for my code"
- "Test strategy and coverage planning"
- "What should I test?"
- "How to test this functionality?"
- "Testing approach and edge cases"

**Constraints:** Never writes actual test code; outlines test cases in pseudo-code or natural language.

---

#### [teaching-assistant.agent.md](teaching-assistant.agent.md)

##### Python Teaching Assistant

Reviews Python code, provides constructive feedback on design patterns, performance, and best practices.

**Core Focus:**

- Code review with constructive feedback
- Explain concepts and design patterns
- Guide learners to their own solutions
- Suggest improvements without writing code
- Address correctness, Pythonic design, architecture, performance, and maintainability

**Use When:**

- "Review my Python code"
- "Help me understand this code"
- "Give feedback on my solution"
- "Python design patterns and best practices"
- "Code optimization guidance"

**Constraints:** Never provides working, copy-paste-ready code; uses pseudo-code and algorithm outlines.

**Feedback Framework Covers:**

- Correctness & logic
- Pythonic design and conventions
- Architecture & design patterns
- Performance & efficiency
- Maintainability & clarity
- Testing & robustness

---

### Infrastructure Agents

#### [terraform-teaching.agent.md](terraform-teaching.agent.md)

##### Terraform Teaching Assistant

Guides infrastructure design, module architecture, state management, and best practices without providing ready-made configurations.

**Core Focus:**

- Design scalable, maintainable infrastructure-as-code
- Build reusable, composable modules and abstractions
- Make informed decisions about state, providers, and backends
- Understand Terraform patterns and anti-patterns
- Debug infrastructure issues systematically
- Apply infrastructure best practices and SOLID principles to IaC

**Use When:**

- "Design infrastructure"
- "Module structure and architecture"
- "State management strategy"
- "Terraform patterns and refactoring"
- "Provider design and troubleshooting"

**Constraints:** Never provides complete, copy-paste-ready Terraform configurations; shows structure conceptually.

**Architecture Framework Covers:**

- Module structure and design
- Variables & outputs strategy
- State management
- Providers and backends
- Workspaces and environment isolation

---

### DevOps Agents

#### [github-actions-teaching.agent.md](github-actions-teaching.agent.md)

##### GitHub Actions Teaching Assistant

Guides workflow design, debugging, optimization, and best practices without providing ready-made workflows.

**Core Focus:**

- Understand GitHub Actions architecture and capabilities
- Design efficient, maintainable CI/CD workflows
- Debug workflow failures systematically
- Optimize for speed, cost, and reliability
- Apply GitHub Actions patterns and best practices
- Understand actions, secrets, caching, and job dependencies

**Use When:**

- "Design CI/CD workflow"
- "Debug failing GitHub Actions"
- "Workflow optimization"
- "GitHub Actions patterns and best practices"
- "Secrets, artifacts, and matrix builds"

**Constraints:** Never provides complete, copy-paste-ready workflow files; explains YAML syntax and patterns conceptually.

**Framework Covers:**

- Job structure and dependencies
- Matrix builds for multiple configurations
- Runners (self-hosted vs. GitHub-hosted)
- Caching strategies
- Secrets & environment handling
- Artifacts management

---

## How to Use These Agents

### 1. Choose the Right Agent

Match your question or challenge to the appropriate agent:

- Algorithm/design problem → **python-algorithm-design**
- Code structure question → **python-architecture**
- Debugging error → **python-debugger**
- Performance issue → **python-performance**
- Testing strategy → **python-testing**
- General code review → **teaching-assistant**
- Infrastructure code → **terraform-teaching**
- CI/CD pipelines → **github-actions-teaching**

### 2. Provide Context

Share:

- Your code or configuration (if relevant)
- The problem you're trying to solve
- What you've already considered
- Constraints or requirements
- Expected vs. actual behavior (for debugging)

### 3. Engage in Guided Discovery

- Ask follow-up questions to clarify your thinking
- Test hypotheses suggested by the agent
- Implement solutions based on conceptual guidance
- Return with implementation questions or blockers

### 4. Learn the Underlying Concepts

These agents emphasize understanding over quick fixes:

- Ask "why?" when recommendations are made
- Explore multiple approaches and trade-offs
- Connect individual lessons to broader principles
- Apply lessons to future problems

## Common Patterns Across Agents

All agents share these principles:

| Aspect | Philosophy |
| ------ | ---------- |
| **Solutions** | Guide thinking, don't provide ready-made answers |
| **Code** | Show conceptual structure, not copy-paste implementations |
| **Questions** | Use Socratic method to guide discovery |
| **Feedback** | Specific, actionable, tied to principles (SOLID, DRY, clarity, etc.) |
| **Constraints** | Work within real-world limits and trade-offs |
| **Growth** | Build skills and confidence through guided exploration |

## Quick Reference

| Agent | Language/Tech | Focus | Key Questions |
| ----- | ------------- | ----- | ------------- |
| Python Algorithm Design | Python | Algorithms & problem-solving | How should I approach this? What pattern does this match? |
| Python Architecture | Python | Code structure & design | How should I organize this? What design pattern applies? |
| Python Debugger | Python | Debugging & troubleshooting | Why is this failing? What's the root cause? |
| Python Performance | Python | Optimization & complexity | Why is this slow? How can I improve performance? |
| Python Testing | Python | Test strategy & design | What should I test? How do I verify this behavior? |
| Python Teaching Assistant | Python | Code review & feedback | How can I improve this code? What patterns should I use? |
| Terraform Teaching | Terraform/IaC | Infrastructure design | How should I structure this infrastructure? What pattern applies? |
| GitHub Actions Teaching | GitHub Actions/CI-CD | Workflow design | How should I design this workflow? What's the best pattern? |

## Getting Started

1. **Identify your challenge** - Which domain does it fall into?
2. **Invoke the agent** - Use the appropriate agent file as a custom instruction
3. **Share context** - Provide code, configuration, or problem description
4. **Engage actively** - Ask questions, test hypotheses, iterate
5. **Learn the concepts** - Focus on understanding principles, not just getting answers

---

**Last Updated:** May 2026
**Purpose:** Educational mentoring and guided learning for intermediate-to-experienced developers
