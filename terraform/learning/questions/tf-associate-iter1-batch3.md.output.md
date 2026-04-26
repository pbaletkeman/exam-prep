# Terraform Associate Exam Questions

---

### Question 1 — Core Workflow Sequence

**Difficulty**: Easy
**Answer Type**: one
**Topic**: Correct order of the core Terraform CLI workflow

**Question**:
Which of the following represents the correct core Terraform workflow sequence?

- A) `validate → init → fmt → plan → apply → destroy`
- B) `init → fmt → validate → plan → apply → destroy`
- C) `fmt → init → plan → validate → apply → destroy`
- D) `init → plan → validate → fmt → apply → destroy`

---

### Question 2 — `terraform init` Purpose

**Difficulty**: Easy
**Answer Type**: one
**Topic**: What `terraform init` does

**Question**:
Which of the following is a primary action performed by `terraform init`?

- A) It applies all pending changes from the most recent execution plan
- B) It downloads required provider plugins into the `.terraform/` directory
- C) It validates that all resource configurations are syntactically correct
- D) It formats all `.tf` files in the working directory to canonical style

---

### Question 3 — When to Re-run `terraform init`

**Difficulty**: Medium
**Answer Type**: many
**Topic**: Conditions requiring `terraform init` to be re-run

**Question**:
In which TWO situations must `terraform init` be re-run? (Select two.)

- A) When a new provider is added to `required_providers`
- B) When an output value is added to an existing module
- C) When the backend configuration is changed to a different provider
- D) When a variable default value is updated in `variables.tf`

---

### Question 4 — `terraform validate` Network Requirement

**Difficulty**: Medium
**Answer Type**: one
**Topic**: `terraform validate` network access and what it checks

**Question**:
Which statement correctly describes `terraform validate`?

- A) It requires active cloud provider credentials to verify that referenced resources exist in the target environment
- B) It performs a live API call to confirm that the AMI ID or other resource identifiers in the config are valid
- C) It checks configuration syntax and internal references without requiring network access or provider credentials
- D) It generates a full execution plan and outputs the number of resources that will be created, updated, or destroyed

---

### Question 5 — `terraform fmt` Flags

**Difficulty**: Medium
**Answer Type**: one
**Topic**: `terraform fmt -check` flag behaviour

**Question**:
What is the purpose of the `-check` flag on `terraform fmt`?

- A) It checks that all variable names follow HashiCorp's naming conventions
- B) It validates the syntax of all HCL files but does not reformat them
- C) It exits with a non-zero exit code if any files need reformatting, without modifying them — useful for CI pipelines
- D) It checks whether provider versions are compatible with the current Terraform version

---

### Question 6 — `terraform plan -out` Flag

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Saving and applying a plan file

**Question**:
What is the benefit of running `terraform plan -out=plan.tfplan` followed by `terraform apply plan.tfplan`?

- A) It allows Terraform to skip provider validation when applying the plan
- B) It guarantees that the exact set of changes reviewed in `plan` is applied, with no drift between the two steps
- C) It compresses the plan file so that it can be stored in version control alongside `.tf` files
- D) It allows `terraform apply` to run without any state file present

---

### Question 7 — Plan Output Symbols

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Meaning of `terraform plan` output symbols

**Question**:
In `terraform plan` output, what does the symbol `-/+` indicate will happen to a resource?

- A) The resource will be updated in-place with no interruption
- B) The resource will be imported into state from an existing infrastructure object
- C) The resource will be destroyed and then recreated (replacement)
- D) The resource will be moved to a different Terraform workspace

---

### Question 8 — `terraform apply -auto-approve`

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Purpose and use case of `-auto-approve`

**Question**:
What does the `-auto-approve` flag do when passed to `terraform apply`?

- A) It automatically selects the most recent saved plan file in the working directory
- B) It skips the interactive confirmation prompt before applying changes — commonly used in CI/CD pipelines
- C) It approves all individual resource creation steps sequentially without pausing
- D) It causes Terraform to apply changes to approved resources only and skip unapproved ones

---

### Question 9 — `terraform apply -replace`

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Forcing resource replacement with `-replace`

**Question**:
Which command is the current (Terraform 1.5+) recommended way to force a specific resource to be destroyed and recreated on the next apply?

- A) `terraform taint aws_instance.web`
- B) `terraform apply -replace="aws_instance.web"`
- C) `terraform destroy -target=aws_instance.web` followed by `terraform apply`
- D) `terraform state rm aws_instance.web` followed by `terraform apply`

---

### Question 10 — `terraform output -raw`

**Difficulty**: Medium
**Answer Type**: one
**Topic**: `terraform output -raw` use case

**Question**:
What does `terraform output -raw db_password` return, and when is this flag useful?

- A) The output value formatted as a JSON object with metadata fields
- B) The raw string value with no surrounding quotes — useful when piping the value into scripts or other commands
- C) The encrypted form of the output value for use with external secrets managers
- D) A diff showing the current output value versus the previous apply's value

---

### Question 11 — `terraform console` Purpose

**Difficulty**: Medium
**Answer Type**: one
**Topic**: What `terraform console` is used for

**Question**:
What is the primary purpose of `terraform console`?

- A) To display the current Terraform state in an interactive paginated viewer
- B) To provide an interactive REPL where Terraform expressions and built-in functions can be tested
- C) To monitor the progress of a running `terraform apply` operation in real time
- D) To inspect and modify resource attributes in the state file interactively

---

### Question 12 — `terraform destroy` Equivalence

**Difficulty**: Hard
**Answer Type**: one
**Topic**: Relationship between `terraform destroy` and `terraform apply -destroy`

**Question**:
Which statement about `terraform destroy` is correct?

- A) `terraform destroy` permanently deletes the state file after all resources are removed
- B) `terraform destroy` is equivalent to `terraform apply -destroy` and both prompt for confirmation by default
- C) `terraform destroy` only removes resources created in the current workspace, while `terraform apply -destroy` removes all workspaces
- D) `terraform destroy` is deprecated and has been replaced by `terraform apply -destroy` in Terraform 1.5+

---

### Question 13 — `terraform fmt` and `terraform validate` Scope

**Difficulty**: Hard
**Answer Type**: many
**Topic**: Distinguishing what `fmt` and `validate` check

**Question**:
Which TWO of the following issues would `terraform validate` detect but `terraform fmt` would NOT? (Select two.)

- A) Inconsistent indentation in a `resource` block
- B) A variable referenced in a resource block that is not declared anywhere in the configuration
- C) Misaligned `=` signs in argument assignments
- D) An unsupported argument name passed to a resource type

## Answer Key

| Q# | Answer(s) | Explanation | Source | Difficulty |
|----|-----------|-----------:|--------|------------|
| 1 | B | N/A | Correct order of the core Terraform CLI workflow | Easy |
| 2 | B | N/A | What `terraform init` does | Easy |
| 3 | A, C | N/A | Conditions requiring `terraform init` to be re-run | Medium |
| 4 | C | N/A | `terraform validate` network access and what it checks | Medium |
| 5 | C | N/A | `terraform fmt -check` flag behaviour | Medium |
| 6 | B | N/A | Saving and applying a plan file | Medium |
| 7 | C | N/A | Meaning of `terraform plan` output symbols | Medium |
| 8 | B | N/A | Purpose and use case of `-auto-approve` | Medium |
| 9 | B | N/A | Forcing resource replacement with `-replace` | Medium |
| 10 | B | N/A | `terraform output -raw` use case | Medium |
| 11 | B | N/A | What `terraform console` is used for | Medium |
| 12 | B | N/A | Relationship between `terraform destroy` and `terraform apply -destroy` | Hard |
| 13 | B, D | N/A | Distinguishing what `fmt` and `validate` check | Hard |
