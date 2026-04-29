# GitHub Actions Learning Repository

A structured learning repository for technical certification and exam preparation. Contains study materials, hands-on notebooks, and multi-language quiz engine implementations covering GitHub Actions, Databricks (Apache Spark), and Terraform.

---

## Repository Purpose

This repository serves as a comprehensive study platform for three certification paths:

| Certification | Provider | Study Materials |
| ------------- | -------- | --------------- |
| GitHub Actions (GH-200) | GitHub / Microsoft | [githubactions/learning](githubactions/learning/) |
| Databricks Certified Associate Developer for Apache Spark | Databricks | [databricks/learning](databricks/learning/) |
| HashiCorp Certified Terraform Associate (004) | HashiCorp | [terraform/learning](terraform/learning/) |

---

## Directory Structure

```shell
.github/                             # GitHub Actions workflow files
actions-source-material/             # Source prompts for GitHub Actions study content
├── gh-200-iteration-1.md through gh-200-iteration-10.md
└── README.md
databricks/
├── learning/                        # 32 Jupyter notebooks + 32 markdown guides
│   ├── 8-WEEK-STUDY-PLAN.md
│   ├── questions/                   # 10 iterations of practice questions
│   │   └── spark-databricks-iteration-1.md through iteration-10.md
│   └── README.md
├── plan-databricksSparkExamOverview.prompt.md
├── plan-databricksSparkStudyPrompts.prompt.md
└── questions-prompt.txt
engine/                              # Shared quiz engine logic
githubactions/
├── learning/                        # GitHub Actions study materials (19 topics)
├── 01-GitHub-Actions-VS-Code-Extension.md
├── 02-Contextual-Information.md
├── ... (01–19)
├── GitHub-Workflows-Guide.md
├── 60-hour-study-plan.md
├── exam-overview.md
├── README.md
└── INDEX.md
quiz-engine/                         # Quiz engine in 8 languages
├── quiz-engine-csharp/
├── quiz-engine-dart/
├── quiz-engine-golang/
├── quiz-engine-java/
├── quiz-engine-nodejs/
├── quiz-engine-python/
├── quiz-engine-rust/
└── quiz-engine-springboot/
terraform/
├── learning/                        # 17 Jupyter notebooks + 17 markdown guides
│   ├── 8-WEEK-STUDY-PLAN.md
│   ├── questions/                   # 10 iterations + original 80 batches
│   │   ├── tf-associate-iter1-merged.md through iter10-merged.md
│   │   ├── orginal/                 # 80 original batch files
│   │   ├── answer-key.py
│   │   └── merge.py
│   └── README.md
├── plan-terraformAssociateExamOverview.prompt.md
├── plan-terraformAssociateStudyPrompts.prompt.md
└── quiz-prompt.md
```

---

## GitHub Actions Study Materials

**Location:** `githubactions/learning`

Comprehensive study materials for the **GitHub Actions (GH-200)** certification exam, covering all exam domains.

### Topics Covered

| File   | Topic |
| ------ | ----- |
| [01-GitHub-Actions-VS-Code-Extension.md](githubactions/learning/01-GitHub-Actions-VS-Code-Extension.md) | VS Code extension setup and usage |
| [02-Contextual-Information.md](githubactions/learning/02-Contextual-Information.md) | GitHub context and metadata |
| [03-Context-Availability-Reference.md](githubactions/learning/03-Context-Availability-Reference.md) | Context availability by event |
| [04-Workflow-File-Structure.md](githubactions/learning/04-Workflow-File-Structure.md) | YAML syntax and workflow anatomy |
| [05-Workflow-Trigger-Events.md](githubactions/learning/05-Workflow-Trigger-Events.md) | Triggers: push, PR, schedule, dispatch |
| [06-Custom-Environment-Variables.md](githubactions/learning/06-Custom-Environment-Variables.md) | Custom env vars and scoping |
| [07-Default-Environment-Variables.md](githubactions/learning/07-Default-Environment-Variables.md) | Built-in GitHub environment variables |
| [08-Environment-Protection-Rules.md](githubactions/learning/08-Environment-Protection-Rules.md) | Deployment environments and protection rules |
| [09-Workflow-Artifacts.md](githubactions/learning/09-Workflow-Artifacts.md) | Uploading and downloading artifacts |
| [10-Workflow-Caching.md](githubactions/learning/10-Workflow-Caching.md) | Dependency caching strategies |
| [11-Workflow-Sharing.md](githubactions/learning/11-Workflow-Sharing.md) | Reusable workflows and composite actions |
| [12-Workflow-Debugging.md](githubactions/learning/12-Workflow-Debugging.md) | Debugging and troubleshooting |
| [13-Workflows-REST-API.md](githubactions/learning/13-Workflows-REST-API.md) | GitHub REST API for workflows |
| [14-Reviewing-Deployments.md](githubactions/learning/14-Reviewing-Deployments.md) | Deployment review and approval gates |
| [15-Creating-Publishing-Actions.md](githubactions/learning/15-Creating-Publishing-Actions.md) | Building and publishing custom actions |
| [16-Managing-Runners.md](githubactions/learning/16-Managing-Runners.md) | GitHub-hosted and self-hosted runners |
| [17-GitHub-Actions-Enterprise.md](githubactions/learning/17-GitHub-Actions-Enterprise.md) | Enterprise features and governance |
| [18-Security-and-Optimization.md](githubactions/learning/18-Security-and-Optimization.md) | Security hardening and performance |
| [19-Common-Failures-Troubleshooting.md](githubactions/learning/19-Common-Failures-Troubleshooting.md) | Common failure patterns and fixes |

Additional resources:

- [GitHub-Workflows-Guide.md](githubactions/learning/GitHub-Workflows-Guide.md) — Complete reference guide
- [study-plan.md](githubactions/learning/study-plan.md) — Exam study plan
- [exam-overview.md](githubactions/learning/exam-overview.md) — Exam structure and domains

---

## Databricks Learning Materials

**Location:** `databricks/learning/`

Comprehensive study materials for the **Databricks Certified Associate Developer for Apache Spark** exam. **32 Jupyter notebooks** with paired markdown documentation covering 7 topic areas, plus an **8-week study plan** and **1.1K+ practice questions** across 10 iterations.

### Getting Started

Begin with the **[8-WEEK-STUDY-PLAN.md](databricks/8-WEEK-STUDY-PLAN.md)** for a structured learning roadmap that organizes all 32 prompts into realistic weekly milestones.

### Topic Areas (7 major topics, 32 prompts)

| Topic | Prompts | Focus |
| ----- | ------- | ----- |
| **1 — Spark Core Architecture & Internals** | 1–7 | Cluster architecture, execution models, lazy evaluation, shuffling, broadcasting, fault tolerance, GC |
| **2 — Spark SQL** | 8–11 | SQL fundamentals, built-in functions, window functions, query optimization |
| **3 — DataFrame API** | 12–23 | Creation, selection, manipulation, filtering, aggregations, joins, combining, I/O, partitioning, schemas, UDFs |
| **4 — Performance Tuning & Debugging** | 24–26 | Tuning techniques, common errors, debugging |
| **5 — Structured & Stateful Streaming** | 27–28 | Streaming fundamentals, windows, watermarking |
| **6 — Spark Connect** | 29 | Architecture and usage |
| **7 — Pandas API on Spark** | 30 | pyspark.pandas integration |
| **Practice & Capstone** | 31–32 | Practice exam (20 questions) + hands-on capstone project |

### Practice Questions (10 iterations, 1.1K+ total questions)

The [`questions/`](databricks/learning/questions/) directory contains **10 iterative refinements** of practice questions:

- **Iteration 1–10**: Progressive difficulty and coverage (55 → 215+ questions per iteration)
- Each iteration covers all exam topics with increasing complexity
- Use iterations sequentially for self-assessment and targeted practice

### Parent Directory Resources

- **[plan-databricksSparkExamOverview.prompt.md](databricks/plan-databricksSparkExamOverview.prompt.md)** — Exam format, structure, scoring, registration
- **[plan-databricksSparkStudyPrompts.prompt.md](databricks/plan-databricksSparkStudyPrompts.prompt.md)** — Prompt specifications for all 32 notebooks
- **[questions-prompt.txt](databricks/questions-prompt.txt)** — Template for generating and refining questions

See [databricks/learning/README.md](databricks/learning/README.md) for the complete index and organization details.

---

## Terraform Learning Materials

**Location:** `terraform/learning/`

Comprehensive study materials for the **HashiCorp Certified Terraform Associate (004)** exam. **17 Jupyter notebooks** with paired markdown documentation covering all 8 exam objectives, plus an **8-week study plan** and **1.1K+ practice questions** across 10 iterations.

### Getting Started

Begin with the **[8-WEEK-STUDY-PLAN.md](terraform/8-WEEK-STUDY-PLAN.md)** for a structured learning roadmap that organizes all 17 prompts into realistic weekly milestones.

### Exam Objectives (8 objectives, 17 prompts)

| Objective | Prompts | Topics |
| --------- | ------- | ------ |
| **1 — IaC Concepts** | prompt01 | Infrastructure as Code, idempotency, declarative vs imperative |
| **2 — Terraform Fundamentals** | prompt02 | Providers, plugin model, `required_providers`, version constraints |
| **3 — Terraform State** | prompt03 | State purpose, state file, `terraform.tfstate` |
| **4 — Core Workflow** | prompt04 | init, plan, apply, destroy, fmt, validate |
| **5 — Configuration** | prompt05–10 | Resources, data sources, variables, locals, outputs, functions, lifecycle, conditions |
| **6 — Modules** | prompt11 | Module types, sources, inputs, outputs, registry |
| **7 — State Advanced** | prompt12 | Backends, locking, S3+DynamoDB, drift detection, import |
| **8 — HCP Terraform** | prompt14–15 | Workspaces, runs, variables, policies, RBAC, OIDC, governance, security |
| **Practice & Capstone** | prompt16–17 | 25-question practice exam + hands-on capstone project |

### Practice Questions (10 iterations, 1.1K+ total questions)

The [`questions/`](terraform/learning/questions/) directory contains **10 iterative refinements** of merged practice questions:

- **Iteration 1–10**: Progressive difficulty and coverage (55 → 215+ questions per iteration)
- Original **80 batch files** archived in `questions/orginal/` for reference
- Supporting utilities: `answer-key.py` and `merge.py` for question management
- Use iterations sequentially for self-assessment and targeted practice

### Parent Directory Resources

- **[8-WEEK-STUDY-PLAN.md](terraform/8-WEEK-STUDY-PLAN.md)** — Structured learning roadmap with weekly milestones
- **[plan-terraformAssociateExamOverview.prompt.md](terraform/plan-terraformAssociateExamOverview.prompt.md)** — Exam format, structure, objectives, registration
- **[plan-terraformAssociateStudyPrompts.prompt.md](terraform/plan-terraformAssociateStudyPrompts.prompt.md)** — Prompt specifications for all 17 notebooks
- **[quiz-prompt.md](terraform/quiz-prompt.md)** — Template for generating and refining questions

See [terraform/learning/README.md](terraform/learning/README.md) for the complete index and organization details.

---

## Quiz Engine

**Location:** `quiz-engine/`

The quiz engine is implemented in 8 programming languages to allow practice with different technology stacks. Each implementation is functionally equivalent.

| Directory | Language / Framework |
| --------- | -------------------- |
| [quiz-engine-csharp](quiz-engine/quiz-engine-csharp/README.md) | C# (.NET) |
| [quiz-engine-dart](quiz-engine/quiz-engine-dart/README.md) | Dart |
| [quiz-engine-golang](quiz-engine/quiz-engine-golang/README.md) | Go |
| [quiz-engine-java](quiz-engine/quiz-engine-java/README.md) | Java |
| [quiz-engine-nodejs](quiz-engine/quiz-engine-nodejs/README.md) | Node.js (JavaScript) |
| [quiz-engine-python](quiz-engine/quiz-engine-python/README.md) | Python |
| [quiz-engine-rust](quiz-engine/quiz-engine-rust/README.md) | Rust |
| [quiz-engine-springboot](quiz-engine/quiz-engine-springboot/README.md) | Java (Spring Boot) |

See [quiz-engine/README.md](quiz-engine/README.md) for setup instructions for each implementation.

---

## Prompt Engineering Source Material

**Location:** [actions-source-material](actions-source-material/README.md)

Iteration prompts used during the development of the GitHub Actions study content. Contains 10 iterations of refined prompt engineering (gh-200-iteration-1.md through gh-200-iteration-10.md) showing the evolution of the question-generation prompts.

---

## Getting Started

### For GitHub Actions Certification

1. Start with [githubactions/exam-overview.md](githubactions/exam-overview.md) for exam structure
2. Follow [githubactions/study-plan.md](githubactions/study-plan.md) for a guided study path
3. Work through topics 01–19 in order
4. Use the [quiz-engine](quiz-engine/) for practice questions

### For Databricks Certification

1. Start with [databricks/learning/8-WEEK-STUDY-PLAN.md](databricks/learning/8-WEEK-STUDY-PLAN.md)
2. Review [databricks/learning/README.md](databricks/learning/README.md) for complete structure
3. Work through 32 notebooks by topic area, reading paired `.md` files for summaries
4. Use the 10 practice question iterations for progressive self-assessment
5. Take the practice exam (prompt31) for final readiness check

### For Terraform Certification

1. Start with [terraform/learning/8-WEEK-STUDY-PLAN.md](terraform/8-WEEK-STUDY-PLAN.md)
2. Review [terraform/learning/README.md](terraform/learning/README.md) for complete structure
3. Work through 17 notebooks in order, reading paired `.md` files for summaries
4. Use the 10 practice question iterations for progressive self-assessment
5. Take the practice exam (prompt16) for readiness check
6. Complete the capstone project (prompt17) for hands-on practice

---

## Prerequisites

| Section | Requirements |
| ------- | ------------ |
| GitHub Actions notebooks | GitHub account, VS Code with GitHub Actions extension |
| Databricks notebooks | Databricks account (Community Edition is free) or Jupyter |
| Terraform notebooks | Terraform CLI >= 1.5.0 installed |
| Quiz engine | Language runtime for the implementation you want to use |
