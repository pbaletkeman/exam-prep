# Terraform Associate Exam Questions

---

### Question 1 — Three Condition Mechanisms Overview

**Difficulty**: Easy
**Answer Type**: one
**Topic**: The three Terraform condition mechanisms and where each is declared

**Question**:
Which of the following correctly lists all three Terraform mechanisms for asserting conditions on infrastructure?

- A) `assert` block, `check` block, `guard` block
- B) `validation` block, `precondition`/`postcondition` in `lifecycle`, `check` block
- C) `validation` block, `check` block, `enforce` block
- D) `precondition` block, `postcondition` block, `verify` block

---

### Question 2 — `validation` Block — When It Runs

**Difficulty**: Easy
**Answer Type**: one
**Topic**: When variable `validation` blocks are evaluated

**Question**:
When does a `validation` block inside a `variable` declaration run?

- A) After `terraform apply` completes, to verify the applied configuration
- B) During `terraform init`, when providers are downloaded
- C) Before `terraform plan`, as part of input variable evaluation
- D) Only when explicitly triggered by `terraform validate`

---

### Question 3 — `validation` Block Condition Constraints

**Difficulty**: Medium
**Answer Type**: one
**Topic**: What a `validation` condition can reference

**Question**:
Which restriction applies to the `condition` expression inside a variable `validation` block?

- A) It must return a number, which is compared to zero to determine pass/fail
- B) It can only reference `var.<variable_name>` — not resources, data sources, or locals
- C) It must use only built-in string functions; numeric comparisons are not allowed
- D) It can reference any variable in the same module but not variables from child modules

---

### Question 4 — `precondition` vs `postcondition` — Timing

**Difficulty**: Medium
**Answer Type**: one
**Topic**: When `precondition` and `postcondition` run relative to resource changes

**Question**:
What is the key timing difference between a `precondition` and a `postcondition` in a resource's `lifecycle` block?

- A) `precondition` runs during `terraform plan`; `postcondition` runs during `terraform validate`
- B) `precondition` runs before the resource is changed during apply; `postcondition` runs after the resource change completes
- C) `precondition` validates input variables; `postcondition` validates output values
- D) Both run at the same time — the distinction is only in the error message text

---

### Question 5 — `self` in `postcondition`

**Difficulty**: Medium
**Answer Type**: one
**Topic**: The `self` reference available in `postcondition` blocks

**Question**:
What does `self` refer to in a `postcondition` block within a resource's `lifecycle`?

- A) The Terraform module that contains the resource
- B) The provider that manages the resource
- C) The resource instance that was just created or updated
- D) The previous state of the resource before the change

---

### Question 6 — `check` Block Failure Behaviour

**Difficulty**: Medium
**Answer Type**: one
**Topic**: How a failing `check` block assertion affects `terraform apply`

**Question**:
What happens when an `assert` condition inside a `check` block evaluates to `false` during `terraform apply`?

- A) The apply is immediately halted and all changes are rolled back
- B) Terraform pauses and prompts the user to confirm whether to continue despite the failed assertion
- C) A warning is displayed but the apply continues and completes successfully
- D) The resource associated with the `check` block is marked as tainted for replacement on the next run

---

### Question 7 — `check` Block Introduction Version

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Which Terraform version introduced the `check` block

**Question**:
In which version of Terraform was the `check` block introduced?

- A) Terraform 1.0
- B) Terraform 1.3
- C) Terraform 1.5
- D) Terraform 1.7

---

### Question 8 — `check` Block Optional Data Source

**Difficulty**: Medium
**Answer Type**: one
**Topic**: The optional scoped data source inside a `check` block

**Question**:
What is the purpose of including a `data` block inside a `check` block?

- A) To import an existing resource into state as part of the health check
- B) To provide a scoped, read-only data source that is used only within that `check` block's assertions
- C) To declare a dependency so the check runs after a specific resource is created
- D) To override the provider used for the assertion data retrieval

---

### Question 9 — Sensitive Output `sensitive = true`

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Effect of `sensitive = true` on an `output` block

**Question**:
An output block is declared with `sensitive = true`. What is the effect on how Terraform handles this output?

- A) The output is encrypted with a provider-managed key before being stored in state
- B) The output value is shown in plan output but hidden during `terraform output` commands
- C) The output value is redacted in terminal display but still stored in plaintext in the state file
- D) The output is excluded from `terraform output` and cannot be retrieved programmatically

---

### Question 10 — Sensitive Data in State — Critical Fact

**Difficulty**: Hard
**Answer Type**: one
**Topic**: How `sensitive = true` interacts with `terraform.tfstate` storage

**Question**:
A team marks their database password variable and output as `sensitive = true`. A new engineer asks why the password is still visible when they open `terraform.tfstate` in a text editor. What is the correct explanation?

- A) The password is only encrypted if the team has enabled KMS integration in the provider block
- B) `sensitive = true` protects values in transit between modules but not in the final state file
- C) `sensitive = true` only controls terminal display — all attribute values are always stored in plaintext in the state file regardless of this setting
- D) The state file should be unreadable — the engineer must have the wrong version of Terraform

---

### Question 11 — Mitigations for Sensitive Data in State

**Difficulty**: Hard
**Answer Type**: many
**Topic**: Recommended approaches to protect sensitive values stored in Terraform state

**Question**:
Which TWO of the following are correct mitigations for the risk that sensitive values are stored in plaintext in Terraform state? (Select two.)

- A) Set `sensitive = true` on all variables and outputs containing secrets
- B) Use a remote backend that supports encryption at rest, such as S3 with server-side encryption or HCP Terraform
- C) Never commit `terraform.tfstate` to source control and restrict access to the state storage location
- D) Use the `prevent_destroy` lifecycle argument to prevent state files from being accidentally deleted

---

### Question 12 — Comparing the Three Condition Mechanisms

**Difficulty**: Medium
**Answer Type**: many
**Topic**: Failure behaviour of `validation`, `precondition`/`postcondition`, and `check`

**Question**:
Which TWO of the following statements correctly describe how Terraform condition mechanisms handle failures? (Select two.)

- A) A failed `validation` block halts execution before `terraform plan` generates an execution plan
- B) A failed `check` block assertion causes `terraform apply` to roll back all changes made in the current run
- C) A failed `precondition` block halts `terraform apply` before the resource is modified
- D) A failed `postcondition` block converts the failing resource to a warning and allows subsequent resources to continue applying

## Answer Key

| Q# | Answer(s) | Explanation | Source | Difficulty |
|----|-----------|-----------:|--------|------------|
| 1 | B | N/A | The three Terraform condition mechanisms and where each is declared | Easy |
| 2 | C | N/A | When variable `validation` blocks are evaluated | Easy |
| 3 | B | N/A | What a `validation` condition can reference | Medium |
| 4 | B | N/A | When `precondition` and `postcondition` run relative to resource changes | Medium |
| 5 | C | N/A | The `self` reference available in `postcondition` blocks | Medium |
| 6 | C | N/A | How a failing `check` block assertion affects `terraform apply` | Medium |
| 7 | C | N/A | Which Terraform version introduced the `check` block | Medium |
| 8 | B | N/A | The optional scoped data source inside a `check` block | Medium |
| 9 | C | N/A | Effect of `sensitive = true` on an `output` block | Medium |
| 10 | C | N/A | How `sensitive = true` interacts with `terraform.tfstate` storage | Hard |
| 11 | B, C | N/A | Recommended approaches to protect sensitive values stored in Terraform state | Hard |
| 12 | A, C | N/A | Failure behaviour of `validation`, `precondition`/`postcondition`, and `check` | Medium |
