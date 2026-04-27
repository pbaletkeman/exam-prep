# Terraform Associate (004) Exam — 8-Week Study Plan

**Duration:** 8 weeks | **Study Time:** 5 hours per week (40 hours total) | **Target:** 70% passing score

---

## Overview

This study plan covers all 8 official exam objectives and uses the 17 learning modules in `terraform\learning\`. Each week balances foundational concepts with hands-on practice and progressive difficulty.

**Study Materials:**
- 17 learning notebooks (prompts 01-17) with both `.ipynb` (interactive) and `.md` (reference) formats
- [25-question practice exam](learning/prompt16-practice-exam-questions-all-objectives.md) ([notebook](learning/prompt16-practice-exam-questions-all-objectives.ipynb))
- [Hands-on capstone project](learning/prompt17-hands-on-capstone-project.md) ([notebook](learning/prompt17-hands-on-capstone-project.ipynb))
- 10+ iterations of exam-style practice questions in `learning/questions/`

---

## Weekly Schedule Overview

| Week | Theme | Hours | Focus |
|------|-------|-------|-------|
| 1 | Foundations & IaC Concepts | 5 | Core IaC principles, Terraform purpose, provider model |
| 2 | Core Terraform Workflow | 5 | CLI commands, state basics, initialization |
| 3 | Configuration Language (HCL) Fundamentals | 5 | Resources, data blocks, variables, outputs |
| 4 | Advanced Configuration (HCL) | 5 | Complex types, built-in functions, expressions, conditions |
| 5 | Resource Management & Dependencies | 5 | Dependencies, lifecycle, resource behavior |
| 6 | Modules & State Management | 5 | Modules, state backends, locking, remote state |
| 7 | Advanced State & HCP Terraform | 5 | State inspection, importing, HCP Terraform basics |
| 8 | Governance, Security & Exam Prep | 5 | HCP Terraform governance, practice exams, final review |

---

## Week 1: Foundations & IaC Concepts
**Time:** 5 hours | **Exam Objectives:** 1, 2

### Learning Goals
- Understand IaC principles and advantages
- Explain Terraform's position in the IaC landscape
- Understand Terraform providers and the plugin model
- Know when and how Terraform interacts with providers

### Daily Schedule (45 min/day × 5 days = 3.75 hours study + 1.25 hours practice)

**Day 1-2: What is Infrastructure as Code? (1.5 hours)**
- **Read:** [prompt01-what-is-iac.md](learning/prompt01-what-is-iac.md) (15 min)
  - Core IaC concepts: desired state vs current state
  - Idempotency and declarative configuration
  - Advantages: reproducibility, audit trail, speed, no drift
  - Why Terraform vs other tools
- **Study:** [prompt01-what-is-iac.ipynb](learning/prompt01-what-is-iac.ipynb) (45 min)
  - Run code examples, interact with concepts
- **Quiz yourself:**
  - What is the difference between desired state and current state?
  - Why is idempotency important in IaC?
  - Name 3 advantages of IaC over manual provisioning

**Day 3-4: Providers & Plugin Model (1.5 hours)**
- **Read:** [prompt02-providers-plugin-model.md](learning/prompt02-providers-plugin-model.md) (15 min)
  - What is a provider? (e.g., AWS, Azure, Google Cloud, etc.)
  - Plugin model: how Terraform downloads and uses providers
  - Version constraints (`>=`, `~>`, `=`)
  - Multiple providers in one configuration
- **Study:** [prompt02-providers-plugin-model.ipynb](learning/prompt02-providers-plugin-model.ipynb) (45 min)
  - Provider configuration examples
  - Multi-cloud scenarios
- **Key concepts:**
  - Required providers in `terraform.lock.hcl`
  - Provider inheritance and aliasing

**Day 5: Practice & Review (1.25 hours)**
- Re-read Prompts 01-02 (summary pass)
- Answer practice questions from `learning\questions\` related to Objectives 1-2
- Create a one-page summary of IaC principles and providers
- **Checkpoint:** You should be able to explain:
  - What IaC is and its benefits
  - How Terraform providers work
  - Why version locking matters

---

## Week 2: Core Terraform Workflow
**Time:** 5 hours | **Exam Objectives:** 3, 4

### Learning Goals
- Master all Terraform CLI commands
- Understand the write → plan → apply workflow
- Know when and how to use each command
- Understand initialization, validation, and formatting

### Daily Schedule

**Day 1-2: Terraform CLI Commands (1.5 hours)**
- **Read:** [prompt04-core-workflow-cli.md](learning/prompt04-core-workflow-cli.md) (20 min)
  - Full CLI command reference: `init`, `fmt`, `validate`, `plan`, `apply`, `destroy`
  - Flags and options for each command
  - Workflow sequence and order
  - Manual intervention points
- **Study:** [prompt04-core-workflow-cli.ipynb](learning/prompt04-core-workflow-cli.ipynb) (50 min)
  - Run through full workflow examples
  - Understand plan output
  - Apply changes and review
- **Key skills:**
  - `terraform init` -upgrade, -reconfigure, -migrate-state
  - `terraform plan` -out=FILE
  - `terraform apply` with and without plan file

**Day 3: State Fundamentals (1 hour)**
- **Read:** [prompt03-terraform-state.md](learning/prompt03-terraform-state.md) (15 min)
  - What is state and why it matters
  - Local vs remote state concepts
  - State file structure
- **Study:** [prompt03-terraform-state.ipynb](learning/prompt03-terraform-state.ipynb) (30 min)
  - Explore state JSON structure
  - How Terraform uses state to plan changes
- **Checkpoint:** Understand:
  - Why Terraform needs a state file
  - How state tracks resources
  - Dangers of manual state editing

**Day 4-5: Workflow Practice (1.5 hours)**
- **Hands-on:**
  - Practice the full workflow: `init` → `fmt` → `validate` → `plan` → `apply` → `destroy`
  - Use one of the simple examples from prompts
  - Run `terraform show` and `terraform state list` to inspect
- **Review:**
  - Command flags and options
  - Error messages and troubleshooting
- **Practice questions:** Focus on CLI command usage and workflow sequencing

---

## Week 3: Configuration Language (HCL) Fundamentals
**Time:** 5 hours | **Exam Objectives:** 3, 5, 6

### Learning Goals
- Write valid HCL with resource and data blocks
- Use input variables and output values
- Understand block syntax and attribute references
- Use locals for reusable values
- Understand dependencies via references

### Daily Schedule

**Day 1-2: Resources & Data Blocks (1.5 hours)**
- **Read:** [prompt05-resource-data-blocks.md](learning/prompt05-resource-data-blocks.md) (15 min)
  - Resource vs data block differences
  - Block syntax: type, name, and arguments
  - Attribute references (`resource.type.name.attribute`)
  - Creating cross-resource dependencies through references
- **Study:** [prompt05-resource-data-blocks.ipynb](learning/prompt05-resource-data-blocks.ipynb) (50 min)
  - Build example resources
  - Reference attributes from other resources
  - Use data sources to read external data
- **Practical:**
  - Write a simple resource block
  - Reference attributes from it in another resource
  - Use a data source to look up existing infrastructure

**Day 3-4: Variables, Locals & Outputs (1.5 hours)**
- **Read:** [prompt06-variables-locals-outputs.md](learning/prompt06-variables-locals-outputs.md) (20 min)
  - Input variables: declaring, types, defaults, descriptions
  - Locals: computed values, scoping
  - Outputs: exposing values, sensitive data
  - Variable precedence and tfvars files
- **Study:** [prompt06-variables-locals-outputs.ipynb](learning/prompt06-variables-locals-outputs.ipynb) (50 min)
  - Define variables with validation
  - Use locals to simplify configuration
  - Output values in different formats
- **Key skills:**
  - Type constraints (string, number, bool, list, map, object, set, tuple)
  - Default values and validation
  - Sensitive outputs

**Day 5: Syntax & Practice (1 hour)**
- Write a small configuration that uses:
  - Resource block
  - Data block
  - Input variable
  - Local value
  - Output value
- Verify with `terraform validate`
- Answer practice questions on HCL syntax

---

## Week 4: Advanced Configuration (HCL)
**Time:** 5 hours | **Exam Objectives:** 6, 8

### Learning Goals
- Master complex data types (lists, maps, objects, sets, tuples)
- Use built-in functions (string, numeric, collection, encoding, etc.)
- Write expressions and conditionals
- Implement custom validation and check blocks
- Handle sensitive data

### Daily Schedule

**Day 1-2: Complex Types & Collections (1.5 hours)**
- **Read:** [prompt07-complex-types-collections.md](learning/prompt07-complex-types-collections.md) (15 min)
  - Lists, maps, sets, objects, tuples
  - Type constraints and combinations
  - When to use each type
  - Accessing elements: indexing and attribute access
- **Study:** [prompt07-complex-types-collections.ipynb](learning/prompt07-complex-types-collections.ipynb) (50 min)
  - Declare complex variable types
  - Access nested elements
  - Loop and transform collections
- **Practical:**
  - Define a variable with a complex type
  - Access nested values
  - Transform collections

**Day 3: Built-in Functions & Expressions (1 hour)**
- **Read:** [prompt08-builtin-functions-expressions.md](learning/prompt08-builtin-functions-expressions.md) (15 min)
  - String functions: upper, lower, split, join, replace, regex
  - Numeric functions: min, max, ceil, floor
  - Collection functions: length, keys, values, lookup, contains
  - Encoding/decoding: jsonencode, jsondecode, base64encode, yamldecode
  - Date functions: now, formatdate, timeadd
  - Filesystem: file, fileexists, dirname, basename
- **Study:** [prompt08-builtin-functions-expressions.ipynb](learning/prompt08-builtin-functions-expressions.ipynb) (45 min)
  - Use common functions in expressions
  - Combine functions for complex transformations
  - Handle errors with try-catch

**Day 4: Custom Conditions & Sensitive Data (1 hour)**
- **Read:** [prompt10-custom-conditions-sensitive-data.md](learning/prompt10-custom-conditions-sensitive-data.md) (15 min)
  - Custom condition blocks (`validation`, `check`)
  - Sensitive data: `sensitive = true` parameter
  - Vault integration concepts
  - Handling secrets in configuration
- **Study:** [prompt10-custom-conditions-sensitive-data.ipynb](learning/prompt10-custom-conditions-sensitive-data.ipynb) (45 min)
  - Implement validation blocks
  - Mark outputs as sensitive
  - Test error conditions

**Day 5: Advanced Practice (1 hour)**
- Write configuration using:
  - Complex types and collections
  - Multiple built-in functions
  - Validation logic
  - Sensitive outputs
- Answer questions on functions and types

---

## Week 5: Resource Management & Dependencies
**Time:** 5 hours | **Exam Objectives:** 6, 8

### Learning Goals
- Understand implicit and explicit dependencies
- Master the dependency graph and execution order
- Use meta-arguments: `depends_on`, `count`, `for_each`, `lifecycle`, `provider`
- Handle resource behavior: create, update, delete, replace
- Understand resource addressing

### Daily Schedule

**Day 1-2: Dependencies & Lifecycle (1.5 hours)**
- **Read:** [prompt09-dependencies-lifecycle.md](learning/prompt09-dependencies-lifecycle.md) (15 min)
  - Implicit dependencies (references create edges in the graph)
  - Explicit dependencies with `depends_on`
  - Lifecycle meta-argument: `create_before_destroy`, `prevent_destroy`, `ignore_changes`
  - Resource addressing: `resource.type.name`
- **Study:** [prompt09-dependencies-lifecycle.ipynb](learning/prompt09-dependencies-lifecycle.ipynb) (50 min)
  - Create resources with implicit dependencies
  - Use `depends_on` for non-obvious relationships
  - Implement lifecycle rules
- **Practical:**
  - Draw or describe the dependency graph for a sample config
  - Understand execution order from the graph
  - Use `terraform plan` to verify order

**Day 3-4: count & for_each (1.5 hours)**
- **Content:** (covered in Prompt 05-06 and 09)
  - `count` for creating multiple instances
  - `for_each` for mapping over collections
  - When to use each (count: simple indexing, for_each: semantic meaning)
  - Splat syntax: `resource.type.name[*].attribute`
  - Resource references to indexed/mapped resources
- **Practical:**
  - Create 5 resources using `count`
  - Create resources using `for_each` with map
  - Reference specific instances in outputs

**Day 5: Resource Behavior & Practice (1 hour)**
- Review: `terraform plan` output interpretation
- Understand diff annotations: `+`, `~`, `-`, `!` (replace)
- Practice identifying:
  - What will be created, updated, replaced, destroyed
  - Why resources will be replaced vs updated
- Answer practice questions on dependencies and meta-arguments

---

## Week 6: Modules & State Management
**Time:** 5 hours | **Exam Objectives:** 5, 7

### Learning Goals
- Source and use Terraform modules
- Understand module structure and variable scope
- Configure local, Git, and registry modules
- Master state backends and remote state
- Implement state locking
- Understand state migration

### Daily Schedule

**Day 1-2: Terraform Modules (1.5 hours)**
- **Read:** [prompt11-terraform-modules.md](learning/prompt11-terraform-modules.md) (15 min)
  - Module concept: encapsulation and reusability
  - Module block syntax and variable passing
  - Module sources: local path, Git, Terraform Registry
  - Version constraints for published modules
  - Variable scope within modules
- **Study:** [prompt11-terraform-modules.ipynb](learning/prompt11-terraform-modules.ipynb) (50 min)
  - Define a simple module with inputs and outputs
  - Use the module in a root configuration
  - Test module variable isolation
- **Practical:**
  - Create a child module directory with variables, outputs, resources
  - Call it from a root module
  - Pass variables and consume outputs

**Day 3-4: State Backends & Remote State (1.5 hours)**
- **Read:** [prompt12-state-backends-locking-remote-state.md](learning/prompt12-state-backends-locking-remote-state.md) (15 min)
  - Backend concept: local, remote (S3, Terraform Cloud, etc.)
  - Backend block configuration
  - State locking: why and how
  - Remote state advantages: team collaboration, safety
  - State migration between backends
- **Study:** [prompt12-state-backends-locking-remote-state.ipynb](learning/prompt12-state-backends-locking-remote-state.ipynb) (50 min)
  - Configure different backend types
  - Understand state locking behavior
  - Migrate state (conceptually; actual cloud not required)
- **Key knowledge:**
  - Backends supported: S3 (AWS), Azure Storage, GCS, Terraform Cloud
  - DynamoDB locking with S3 backend
  - Consistency and durability guarantees

**Day 5: State Management Practice (1 hour)**
- Review state file contents and structure
- Understand `terraform.tfstate` vs `.terraform`
- Practice questions on modules and state

---

## Week 7: Advanced State & HCP Terraform
**Time:** 5 hours | **Exam Objectives:** 7, 8

### Learning Goals
- Import existing infrastructure into state
- Inspect and manipulate state safely
- Understand moved and removed blocks
- Basics of HCP Terraform
- Workspaces and remote state data sources
- Run triggers and team access

### Daily Schedule

**Day 1-2: Importing & State Inspection (1.5 hours)**
- **Read:** [prompt13-importing-infrastructure-state-inspection.md](learning/prompt13-importing-infrastructure-state-inspection.md) (15 min)
  - `terraform import` command: when and how
  - Writing import blocks (Terraform 1.5+)
  - `terraform state list`, `terraform state show`
  - `terraform state rm` (dangerous, but know it)
  - Verbose logging with `TF_LOG`
- **Study:** [prompt13-importing-infrastructure-state-inspection.ipynb](learning/prompt13-importing-infrastructure-state-inspection.ipynb) (50 min)
  - Practice importing a resource
  - Inspect state with CLI commands
  - Understand import addresses
- **Key skills:**
  - Syntax: `terraform import resource.type.name resource-id`
  - Handling resource addresses
  - Verifying import completeness

**Day 3-4: HCP Terraform Basics (1.5 hours)**
- **Read:** [prompt14-hcp-terraform-workspaces-runs-state.md](learning/prompt14-hcp-terraform-workspaces-runs-state.md) (15 min)
  - What is HCP Terraform (Terraform Cloud)
  - Workspaces: concept and purpose (not Terraform native workspaces)
  - VCS-driven and CLI-driven workflows
  - Runs: planning and applying in HCP
  - State data source to reference remote state
- **Read:** [prompt15-hcp-terraform-governance-security-advanced.md](learning/prompt15-hcp-terraform-governance-security-advanced.md) (15 min)
  - Teams and permissions
  - Policy as Code (Sentinel, OPA)
  - Variable sets and dynamic credentials
  - Cost estimation
  - Health assessments and drift detection
- **Study:** [prompt14-hcp-terraform-workspaces-runs-state.ipynb](learning/prompt14-hcp-terraform-workspaces-runs-state.ipynb) and [prompt15-hcp-terraform-governance-security-advanced.ipynb](learning/prompt15-hcp-terraform-governance-security-advanced.ipynb) (40 min)
  - Understand HCP concepts without a live account if needed
  - Review policy examples
  - Understand governance features

**Day 5: State & HCP Practice (1 hour)**
- Review moved and removed blocks
- Understand state refactoring use cases
- Answer practice questions on state management and HCP

---

## Week 8: Governance, Security & Exam Prep
**Time:** 5 hours | **Exam Objectives:** All (1-8), comprehensive review

### Learning Goals
- Comprehensive review of all objectives
- Practice exam questions under timed conditions
- Hands-on capstone project
- Identify weak areas and final study
- Build confidence for exam day

### Daily Schedule

**Day 1: Capstone Project (1.5 hours)**
- **Read:** [prompt17-hands-on-capstone-project.md](learning/prompt17-hands-on-capstone-project.md) (15 min)
  - Project structure and requirements
  - All exam objectives integrated in one project
  - Providers used: random, local, null (no cloud credentials needed)
- **Study & Execute:** [prompt17-hands-on-capstone-project.ipynb](learning/prompt17-hands-on-capstone-project.ipynb) (1.5 hours)
  - Complete the full project from scratch
  - Work through: `init` → `plan` → `apply` → `destroy`
  - Implement modules, variables, outputs, conditions
  - Test all major features

**Day 2: Practice Exam (1.5 hours)**
- **Read & Study:** [prompt16-practice-exam-questions-all-objectives.md](learning/prompt16-practice-exam-questions-all-objectives.md) (15 min overview)
- **Take the exam:** [prompt16-practice-exam-questions-all-objectives.ipynb](learning/prompt16-practice-exam-questions-all-objectives.ipynb) (1.5 hours)
  - 25 questions under timed conditions (simulate 30-40 min for 25 Qs)
  - Don't look at answers until you finish
  - Review all answers and explanations
  - Note any weak areas

**Day 3-4: Iterative Practice Questions (1.5 hours)**
- Work through exam-style questions in [learning/questions/](learning/questions/)
- Use the merged files for bulk practice: [tf-associate-iter*.md](learning/questions/)
- Focus on weak areas identified from Prompt 16
- Use [answer-key.py](learning/questions/answer-key.py) to check your answers
- **Target:** At least 70% accuracy on practice questions

**Day 5: Final Review & Exam Prep (1 hour)**
- **One-page summaries** on tricky topics:
  - State management and backends
  - Module scoping and variable passing
  - Dependency graph and `depends_on`
  - Meta-arguments: count, for_each, lifecycle
  - HCP Terraform features
  - Built-in functions and complex types
- **Exam logistics review:**
  - Register at developer.hashicorp.com/certifications
  - Test your proctoring software setup
  - Know the passing score (70% = ~40 out of 57 questions)
  - Review exam rules (no aids, 60 minutes, ~57 questions)
- **Final checklist:**
  - [ ] Completed all 17 prompts
  - [ ] Scored 70%+ on Prompt 16 (25-Q practice exam)
  - [ ] Can explain all 8 objectives
  - [ ] Comfortable with Terraform CLI workflow
  - [ ] Understand HCL, modules, state, and dependencies
  - [ ] Know when to use count vs for_each
  - [ ] Ready for exam day!

---

## Daily Study Template

Each day should follow this pattern (adjust timing as needed):

1. **Overview** (5 min): Skim the learning objectives for the day
2. **Deep Study** (30-40 min): Read markdown, study notebook, run examples
3. **Hands-On Practice** (10-15 min): Write config, run commands, test
4. **Review & Quiz** (5-10 min): Summarize key points, answer questions
5. **Rest & Consolidate** (take a break)

---

## Study Tips

### Before You Start
- [ ] Set up a quiet study space
- [ ] Have terminal + editor (VS Code with Terraform extension recommended)
- [ ] Install Terraform locally (`terraform version` to verify)
- [ ] Have the notebooks and markdown files open for quick reference

### During Study Sessions
- [ ] **Code along:** Don't just read code; type it and run it
- [ ] **Experiment:** Modify examples, break things, understand error messages
- [ ] **Take notes:** Summarize each section in your own words
- [ ] **Ask questions:** If something doesn't make sense, revisit it or explain it aloud

### Track Progress
- [ ] Check off each module as you complete it
- [ ] Log your practice exam scores (goal: 70%+)
- [ ] Note weak areas and revisit before the exam
- [ ] Keep a "gotchas" list of things you often forget

### One Week Before Exam
- [ ] Take full practice exams under timed conditions
- [ ] Review any remaining weak areas
- [ ] Get good sleep the night before
- [ ] Arrive 15 min early to proctored exam

### Exam Day
- [ ] Read each question carefully (not just first sentence)
- [ ] Flag uncertain questions and return to them
- [ ] Don't panic if a question seems hard — you only need 70%
- [ ] Use the full 60 minutes; don't rush

---

## Resources Summary

| Resource | Type | Count | Purpose |
|----------|------|-------|---------|
| Learning modules | `.ipynb` + `.md` | 17 | Comprehensive coverage, interactive learning |
| Practice questions | `.md` files | 10+ iterations | Exam-style questions with answers |
| Capstone project | Hands-on | 1 (Prompt 17) | Integrate all objectives, no cloud needed |
| Exam overview | Reference | 1 (this plan) | Exam format, objectives, timing |

---

## Success Criteria

### By End of Week 8, You Should Be Able To:

- [ ] Explain Infrastructure as Code and its advantages
- [ ] Initialize, plan, apply, and destroy a Terraform workspace
- [ ] Write valid HCL with resources, data, variables, outputs, and locals
- [ ] Use complex types and built-in functions
- [ ] Understand Terraform's dependency graph and execution order
- [ ] Create and use Terraform modules
- [ ] Configure state backends and understand remote state
- [ ] Import existing infrastructure and inspect state
- [ ] Explain HCP Terraform features and governance
- [ ] Score 70%+ on practice exams
- [ ] Pass the HashiCorp Certified: Terraform Associate (004) exam

---

## Contingency: If Behind Schedule

If you fall behind, prioritize in this order:

1. **Weeks 1-3:** Foundations, CLI, basic HCL (non-negotiable)
2. **Week 4:** Functions and complex types (important for ~30% of exam)
3. **Week 5:** Dependencies and meta-arguments (critical for ~25% of exam)
4. **Week 6:** Modules and state (important for ~20% of exam)
5. **Week 7-8:** Advanced state, HCP, practice exams (review + polish)

**If very short on time:**
- Focus on prompts: 1, 2, 3, 4, 5, 6, 9, 11, 12, 16
- Skip deep study of Prompts 7-8, 10 (functions) but know the names and high-level use
- Still do the capstone (Prompt 17) to test integration
- Do Prompt 16 (practice exam) multiple times

---

## Post-Exam

Congratulations on earning your Terraform Associate certification!

- **Certificate validity:** 2 years
- **Recertification:** Take the exam again or achieve advanced certifications (Terraform Professional, Cloud solutions)
- **Next steps:** Consider cloud-specific certifications (AWS, Azure, GCP) or Terraform Professional cert

---

**Study Plan Created:** April 26, 2026
**Exam Objective:** HashiCorp Certified: Terraform Associate (004)
**Target Score:** 70% (passing), 85%+ (excellent)
**Weekly Commitment:** 5 hours (manageable alongside work/life)
