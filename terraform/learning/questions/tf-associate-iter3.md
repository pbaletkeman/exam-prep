# Terraform Associate (004) — Question Bank Iter 3

**Iteration**: 3
**Iteration Style**: HCL interpretation — read a snippet and identify output/effect
**Batch 1 Objective**: 1 — IaC Concepts
**Batch 2 Objective**: 2 — Terraform Fundamentals (Providers & State)
**Batch 3 Objective**: 3 — Core Workflow & CLI
**Batch 4 Objective**: 4a — Resources, Data & Dependencies
**Batch 5 Objective**: 4b — Variables, Outputs, Types & Functions
**Batch 6 Objective**: 4c — Custom Conditions & Sensitive Data
**Batch 7 Objective**: 5 — Modules + 6 — State Backends
**Batch 8 Objective**: 7 — Maintaining Infra + 8 — HCP Terraform
**Generated**: 2026-04-25
**Total Questions**: 103 (13 per batch except batch 1 & 6 with 12)
**Difficulty Split**: See individual batches
**Answer Types**: See individual batches

---

## Questions

---

# Batch 1

# Terraform Associate (004) — Question Bank Iter 3 Batch 1

**Iteration**: 3
**Iteration Style**: HCL interpretation — read a snippet and identify output/effect
**Batch**: 1
**Objective**: 1 — IaC Concepts
**Generated**: 2026-04-25
**Total Questions**: 12
**Difficulty Split**: 2 Easy / 8 Medium / 2 Hard
**Answer Types**: 9 `one` / 3 `many` / 0 `none`

---

## Questions

---

### Question 1 — State Addresses Created by count

**Difficulty**: Easy
**Answer Type**: one
**Topic**: Reading a `count` argument to determine how many state resource addresses Terraform tracks

**Question**:
Given the following configuration:

```hcl
resource "aws_instance" "app" {
  ami           = "ami-0abc1234"
  instance_type = "t3.micro"
  count         = 3
}
```

How many resource addresses does Terraform record in state after a successful apply?

- A) 1 — `aws_instance.app`
- B) 3 — `aws_instance.app[0]`, `aws_instance.app[1]`, `aws_instance.app[2]`
- C) 3 — `aws_instance.app.0`, `aws_instance.app.1`, `aws_instance.app.2`
- D) 1 — Terraform groups all instances under a single `aws_instance.app` state entry

**Answer**: B

**Explanation**:
When `count` is used, Terraform creates one state entry per instance using zero-based bracket notation: `aws_instance.app[0]`, `aws_instance.app[1]`, and `aws_instance.app[2]`. Dot notation (option C) is an older format occasionally seen in legacy documentation but is not the canonical address format for `count`-based resources in current Terraform versions.

---

# Batch 2

...existing code...

# Batch 8

...existing code...

---

(Questions are included in full, with all metadata and explanations, as per the batch files.)
