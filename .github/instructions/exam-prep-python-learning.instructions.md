---
name: exam-prep-python-learning
description: "Exam prep learning guide for Python solutions. Emphasizes understanding over memorization, code quality, and continuous improvement through peer review. Triggers teaching assistant for feedback on correctness, design, and best practices. Use when: working on exam-prep solutions, reviewing solutions for completeness, preparing for assessments."
applyTo: "**/*.py"
---

# Python Exam Prep Learning Standards

You are preparing solutions for professional assessment. These standards ensure your work demonstrates mastery, not just functionality.

## Philosophy

**Understanding over memorization.** Your goal is to demonstrate deep comprehension of concepts, design patterns, and problem-solving approaches—not to memorize solutions.

**Code quality reflects thinking.** The way you structure, name, and organize code reveals your problem-solving approach and technical judgment. Exam prep solutions should be production-quality.

**Feedback drives improvement.** Regularly request code reviews using the teaching assistant to identify blindspots and elevate your solutions iteratively.

## Solution Quality Standards

### Correctness & Robustness

- [ ] Solution solves the stated problem completely and correctly
- [ ] Handles edge cases and boundary conditions (empty inputs, None, zero, single item, large inputs)
- [ ] Error handling is explicit and meaningful (catches expected errors, provides context)
- [ ] No assumptions about inputs without validation or documentation
- [ ] Solution is testable (can you write tests for it? If not, refactor for testability)

### Design & Architecture

- [ ] Code structure reflects the problem domain (clarity of intent over brevity)
- [ ] Functions have single, well-defined responsibilities
- [ ] Coupling is minimal; dependencies are explicit (parameters, not globals)
- [ ] Design patterns are applied appropriately (if used, they solve actual problems)
- [ ] Data flow is clear and auditable (not hidden in side effects)

### Python Idioms & Readability

- [ ] Code follows PEP 8 style guide and Python conventions
- [ ] Variable/function/class names are descriptive and intentional
- [ ] Code uses Python strengths (comprehensions, context managers, generators) appropriately
- [ ] Type hints are present and accurate (required for function signatures)
- [ ] Comments explain "why," not "what" (code should be self-documenting for "what")

### Performance & Efficiency

- [ ] You've considered algorithmic complexity (Big O) and justified choices
- [ ] No obvious inefficiencies (nested loops where unnecessary, string concatenation in loops, etc.)
- [ ] Memory usage is reasonable; no unnecessary copies or retentions
- [ ] You can explain trade-offs you've made (simplicity vs. efficiency, clarity vs. speed)

### Testing & Verification

- [ ] Solution includes unit tests covering normal cases, edge cases, and error conditions
- [ ] Tests are meaningful (test behavior, not implementation details)
- [ ] You've manually tested with realistic inputs
- [ ] You can explain how you verified correctness

## Before Submitting

Use this checklist:

- [ ] **Code Review**: Request feedback from the teaching assistant on the solution
- [ ] **Understand Feedback**: Make sure you understand *why* each suggestion matters
- [ ] **Iterate**: Revise based on feedback and re-submit for second review if substantive changes
- [ ] **Justify Choices**: Be ready to explain every significant design decision
- [ ] **Test Coverage**: All meaningful code paths are tested
- [ ] **Documentation**: README or docstrings explain the approach and any non-obvious decisions
- [ ] **Clean Workspace**: Remove debug code, commented-out sections, and temporary scaffolding

## Continuous Improvement Process

1. **Write the solution** - Get something working
2. **Request teaching assistant review** - Ask for feedback on correctness, design, and Python idioms
3. **Understand the feedback** - Don't just apply suggestions; understand why they matter
4. **Iterate** - Implement improvements and request follow-up review if significant changes
5. **Reflect** - What did you learn? How would you approach this differently next time?
6. **Move to next problem** - Carry lessons learned forward

## When to Request Teaching Assistant Feedback

- [ ] After initial working solution: "Review this for correctness and design"
- [ ] Before major refactoring: "Is this approach sound? Should I consider alternatives?"
- [ ] When uncertain about idioms: "Is this the Pythonic way to solve this?"
- [ ] For performance concerns: "Does this scale well? Any obvious inefficiencies?"
- [ ] For architectural questions: "Is my structure clear and maintainable?"
- [ ] Before considering solution "done": "What am I missing? Final pass?"

## What Excellence Looks Like

Excellence in exam prep is:
- **Correct**: Solves the actual problem, handles edge cases, passes comprehensive tests
- **Clear**: Anyone reading it understands the intent without explanation
- **Considered**: Design decisions are intentional, justified, and explained
- **Competent**: Demonstrates mastery of Python idioms, standard library, and problem-solving
- **Confident**: You can defend every choice and explain alternatives you rejected
- **Continuous**: You reflect on feedback and improve with each solution

This is not about perfect code—it's about demonstrating that you understand what you're doing and why.
