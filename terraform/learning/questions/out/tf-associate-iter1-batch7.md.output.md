# Terraform Associate Exam Questions

---

### Question 1 — Root Module Definition

**Difficulty**: Easy
**Answer Type**: one
**Topic**: What the root module is in a Terraform configuration

**Question**:
What is the Terraform **root module**?

- A) The first module listed in `modules.json` inside `.terraform/`
- B) The working directory from which you run `terraform apply`, containing the top-level configuration files
- C) A published module on the Terraform Registry that all other modules depend on
- D) The `main.tf` file specifically — variables.tf and outputs.tf belong to child modules

---

### Question 2 — Valid Module Source Types

**Difficulty**: Medium
**Answer Type**: many
**Topic**: Which source types are valid for the `source` argument in a module block

**Question**:
Which TWO of the following are valid values for the `source` argument in a `module` block? (Select two.)

- A) `"./modules/networking"` — a relative local path to a subdirectory
- B) `"hashicorp/consul/aws"` — a Terraform Registry module reference
- C) `"provider::aws::vpc"` — a provider-namespaced module reference
- D) `"module.networking"` — a reference to another module in the same configuration

---

### Question 3 — Double-Slash `//` in Module Source

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Meaning of `//` in a Git-based module source URL

**Question**:
In the module source `"github.com/org/infra-modules//modules/vpc"`, what does the `//` (double slash) signify?

- A) It is a URL comment indicator and the text after it is ignored
- B) It separates the repository root from a subdirectory path within the repository
- C) It indicates that the module should be downloaded twice for redundancy
- D) It is a typo — only a single slash is valid in module source paths

---

### Question 4 — `version` Argument Restriction

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Which module source types support the `version` argument

**Question**:
For which module source type is the `version` argument valid?

- A) Local paths only (`"./modules/vpc"`)
- B) Git URLs only (`"git::https://..."`)
- C) Terraform Registry and private registry sources only
- D) All source types support the `version` argument

---

### Question 5 — Module Cache Location

**Difficulty**: Easy
**Answer Type**: one
**Topic**: Where `terraform init` caches downloaded module source code

**Question**:
Where does `terraform init` cache downloaded child module source code?

- A) `~/.terraform/modules/` in the user's home directory
- B) `terraform.tfstate` alongside the state data
- C) `.terraform/modules/` in the current working directory
- D) `/tmp/terraform-modules/` in a system temporary directory

---

### Question 6 — Variable Inheritance Between Modules

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Whether child modules inherit variables from the root module automatically

**Question**:
A root module declares `variable "region" { default = "us-east-1" }`. A child module also needs a `region` value. Which statement is correct?

- A) The child module automatically inherits `var.region` from the root module without any additional configuration
- B) The child module inherits the variable only if it is declared in both `variables.tf` files
- C) Variables are never automatically inherited — the root module must explicitly pass the value as an input argument in the `module` block
- D) Variables are inherited only for built-in types (string, number, bool); complex types must be passed explicitly

---

### Question 7 — Standard Module File Structure

**Difficulty**: Medium
**Answer Type**: many
**Topic**: Files that belong in a standard Terraform module structure

**Question**:
Which TWO files are part of the standard, recommended Terraform module file structure? (Select two.)

- A) `versions.tf` — declares required Terraform and provider versions
- B) `state.tf` — declares the backend configuration for the module's state
- C) `providers.tf` — required to re-declare the provider in every child module
- D) `outputs.tf` — declares the output values exposed by the module

---

### Question 8 — Backend Block Location in HCL

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Where the `backend` block is declared in Terraform configuration

**Question**:
Where must the `backend` block be declared in a Terraform configuration?

- A) In a dedicated `backend.tf` file at the root of the module
- B) Inside the `terraform {}` block, which is typically placed in `versions.tf` or `main.tf`
- C) Inside a `provider` block, alongside authentication credentials
- D) In `terraform.tfvars` as a backend-specific variable assignment

---

### Question 9 — `terraform.tfstate.backup` Purpose

**Difficulty**: Medium
**Answer Type**: one
**Topic**: What `terraform.tfstate.backup` contains and its limitations

**Question**:
What does `terraform.tfstate.backup` contain when using the local backend?

- A) A complete versioned history of all previous state files since the project was created
- B) The state from the most recent apply — a single snapshot of the previous state, not a full history
- C) A backup of the state from 24 hours ago, automatically updated on a daily schedule
- D) An encrypted copy of the current state file for disaster recovery

---

### Question 10 — `terraform init -migrate-state` vs `-reconfigure`

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Difference between `terraform init -migrate-state` and `terraform init -reconfigure`

**Question**:
What is the difference between `terraform init -migrate-state` and `terraform init -reconfigure` when changing backends?

- A) `-migrate-state` only works with S3 backends; `-reconfigure` works with all backend types
- B) `-migrate-state` copies existing state to the new backend; `-reconfigure` reinitialises the backend without migrating existing state
- C) `-reconfigure` is for switching from local to remote backends; `-migrate-state` is for switching between two remote backends
- D) Both flags are identical — they are aliases for the same operation

---

### Question 11 — S3 Backend State Locking

**Difficulty**: Medium
**Answer Type**: one
**Topic**: How the S3 backend implements state locking

**Question**:
When using the S3 backend, which AWS service provides state locking, and what attribute name is required?

- A) S3 object tagging with a tag key of `TerraformLock`
- B) AWS Systems Manager Parameter Store with a parameter named `terraform-lock`
- C) DynamoDB with a table attribute named `LockID`
- D) CloudWatch Events with a rule named after the state file key

---

### Question 12 — `terraform force-unlock` Usage

**Difficulty**: Hard
**Answer Type**: one
**Topic**: When and how to use `terraform force-unlock`

**Question**:
When should `terraform force-unlock <LOCK_ID>` be used, and what is the risk?

- A) It should be used routinely after every `terraform apply` to clean up lock artifacts; it carries no risk
- B) It should be used only when you are certain no other `terraform apply` or `plan` is actively running — using it while another operation holds the lock can corrupt state
- C) It should be used whenever `terraform plan` runs slowly, as it removes lock contention caused by stale read locks
- D) It can only be run by the user who created the lock; other users receive a permission error

---

### Question 13 — `plan -refresh-only` vs `apply -refresh-only`

**Difficulty**: Hard
**Answer Type**: many
**Topic**: Distinguishing `terraform plan -refresh-only` from `terraform apply -refresh-only`

**Question**:
Which TWO statements correctly describe the behaviour of the `-refresh-only` flag? (Select two.)

- A) `terraform plan -refresh-only` shows what has drifted in the cloud compared to state, but proposes no infrastructure changes
- B) `terraform apply -refresh-only` modifies cloud resources to match the Terraform configuration, resolving drift by re-applying desired state
- C) `terraform apply -refresh-only` updates the state file to reflect the current actual state of cloud resources, without creating, modifying, or destroying any infrastructure
- D) `terraform plan -refresh-only` is equivalent to `terraform refresh`, which is a deprecated command that both refreshes state and applies the plan in one step

## Answer Key

| Q# | Answer(s) | Explanation | Source | Difficulty |
|----|-----------|-----------:|--------|------------|
| 1 | B | N/A | What the root module is in a Terraform configuration | Easy |
| 2 | A, B | N/A | Which source types are valid for the `source` argument in a module block | Medium |
| 3 | B | N/A | Meaning of `//` in a Git-based module source URL | Medium |
| 4 | C | N/A | Which module source types support the `version` argument | Medium |
| 5 | C | N/A | Where `terraform init` caches downloaded module source code | Easy |
| 6 | C | N/A | Whether child modules inherit variables from the root module automatically | Medium |
| 7 | A, D | N/A | Files that belong in a standard Terraform module structure | Medium |
| 8 | B | N/A | Where the `backend` block is declared in Terraform configuration | Medium |
| 9 | B | N/A | What `terraform.tfstate.backup` contains and its limitations | Medium |
| 10 | B | N/A | Difference between `terraform init -migrate-state` and `terraform init -reconfigure` | Medium |
| 11 | C | N/A | How the S3 backend implements state locking | Medium |
| 12 | B | N/A | When and how to use `terraform force-unlock` | Hard |
| 13 | A, C | N/A | Distinguishing `terraform plan -refresh-only` from `terraform apply -refresh-only` | Hard |
