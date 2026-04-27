# Terraform Associate Exam Questions

---

### Question 1 — `import` Block vs CLI Import

**Difficulty**: Easy
**Answer Type**: one
**Topic**: Which import method is preferred in Terraform 1.5+ and why

**Question**:
What is the primary advantage of using an `import` block (Terraform 1.5+) over the legacy `terraform import` CLI command?

- A) The `import` block is faster because it uses parallel imports; the CLI command is sequential
- B) The `import` block can be previewed with `terraform plan` before changes are applied, and can optionally generate HCL configuration automatically
- C) The `import` block supports all resource types; the CLI command only supports AWS resources
- D) The `import` block requires no existing resource block in configuration; the CLI command requires one

---

### Question 2 — `import` Block Syntax

**Difficulty**: Easy
**Answer Type**: one
**Topic**: Required arguments in an `import` block

**Question**:
Which two arguments are required in an `import` block?

- A) `source` and `destination`
- B) `resource` and `cloud_id`
- C) `to` and `id`
- D) `address` and `provider_id`

---

### Question 3 — CLI Import Pre-Requisite

**Difficulty**: Medium
**Answer Type**: one
**Topic**: What must exist in configuration before running `terraform import` CLI command

**Question**:
What must exist in the Terraform configuration before running `terraform import aws_s3_bucket.assets my-bucket-name`?

- A) Nothing — `terraform import` creates both the state entry and the HCL resource block automatically
- B) An `import` block referencing the same resource address
- C) A `resource "aws_s3_bucket" "assets" {}` block must already exist in the configuration files
- D) A `data "aws_s3_bucket" "assets" {}` block must exist to look up the bucket first

---

### Question 4 — `terraform plan -generate-config-out`

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Purpose of the `-generate-config-out` flag

**Question**:
What does `terraform plan -generate-config-out=generated.tf` do?

- A) Saves the execution plan to a file named `generated.tf` that can be passed to `terraform apply`
- B) Generates HCL resource configuration for resources referenced in `import` blocks and writes it to `generated.tf`
- C) Exports all existing resources in state as HCL configuration into `generated.tf`
- D) Generates a Terraform provider configuration block and appends it to `generated.tf`

---

### Question 5 — `TF_LOG` Verbosity Order

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Order of `TF_LOG` levels from most to least verbose

**Question**:
Which ordering correctly lists Terraform's `TF_LOG` levels from **most verbose** to **least verbose**?

- A) `ERROR > WARN > INFO > DEBUG > TRACE > OFF`
- B) `TRACE > DEBUG > INFO > WARN > ERROR > OFF`
- C) `DEBUG > TRACE > INFO > WARN > ERROR > OFF`
- D) `INFO > DEBUG > TRACE > WARN > ERROR > OFF`

---

### Question 6 — `TF_LOG_PATH` and Separate Core/Provider Logging

**Difficulty**: Medium
**Answer Type**: many
**Topic**: `TF_LOG_PATH`, `TF_LOG_CORE`, and `TF_LOG_PROVIDER` environment variables

**Question**:
Which TWO statements correctly describe Terraform's logging environment variables? (Select two.)

- A) `TF_LOG_PATH=/tmp/tf.log` causes Terraform to write log output to that file instead of stderr
- B) `TF_LOG_CORE=DEBUG` and `TF_LOG_PROVIDER=TRACE` allow setting different log levels for Terraform core and provider plugins independently
- C) `TF_LOG_PATH` must be set to an absolute path; relative paths are not supported
- D) Setting `TF_LOG_PROVIDER=TRACE` also automatically sets `TF_LOG_CORE=TRACE`

---

### Question 7 — HCP Terraform `cloud` Block

**Difficulty**: Medium
**Answer Type**: one
**Topic**: The `cloud` block and when it was introduced

**Question**:
What is the preferred way to connect a Terraform configuration to HCP Terraform (Terraform 1.1+), and which two arguments does it require?

- A) `backend "remote"` block with `hostname` and `token` arguments
- B) `cloud` block with `organization` and `workspaces` arguments
- C) `cloud` block with `hostname` and `workspace_id` arguments
- D) `provider "tfe"` block with `organization` and `token` arguments

---

### Question 8 — `terraform login` Token Storage

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Where `terraform login` stores the API token

**Question**:
Where does `terraform login` store the HCP Terraform API token after a successful browser-based authentication?

- A) `terraform.tfvars` in the current working directory
- B) `.terraform/credentials.json` in the current working directory
- C) `~/.terraform.d/credentials.tfrc.json` in the user's home directory
- D) The token is never stored on disk — it is only held in memory for the current session

---

### Question 9 — HCP Terraform Run Types

**Difficulty**: Medium
**Answer Type**: one
**Topic**: The three HCP Terraform run types

**Question**:
Which HCP Terraform run type runs a plan but **never applies** — typically triggered by a pull request to show what would change?

- A) Plan-only run
- B) Speculative plan
- C) Plan-and-apply run
- D) Dry-run

---

### Question 10 — HCP Terraform Policy Enforcement Levels

**Difficulty**: Medium
**Answer Type**: one
**Topic**: The three Sentinel/OPA policy enforcement levels

**Question**:
Which HCP Terraform policy enforcement level **blocks a run** when a policy fails but **allows an authorised user to override** the failure and proceed?

- A) `advisory`
- B) `soft-mandatory`
- C) `hard-mandatory`
- D) `blocking`

---

### Question 11 — Variable Sets in HCP Terraform

**Difficulty**: Medium
**Answer Type**: one
**Topic**: What variable sets are and how they are used

**Question**:
What is the purpose of a **variable set** in HCP Terraform?

- A) A set of required variables that must be declared in every workspace's `variables.tf`
- B) A reusable collection of Terraform or environment variables that can be assigned to multiple workspaces or an entire organisation
- C) A list of sensitive variable names whose values are automatically redacted from run logs
- D) A JSON file that defines default variable values, similar to `terraform.tfvars`

---

### Question 12 — HCP Terraform Workspace Permissions

**Difficulty**: Hard
**Answer Type**: many
**Topic**: The four workspace-level permission tiers in HCP Terraform

**Question**:
Which TWO statements correctly describe HCP Terraform workspace-level permissions? (Select two.)

- A) The **Write** permission allows a user to trigger runs and approve applies, but not to manage workspace settings or team access
- B) The **Plan** permission allows a user to trigger full plan-and-apply runs without any additional approval
- C) The **Read** permission allows a user to view run history, state, and variables but not trigger any runs
- D) The **Admin** permission is required to change workspace variables — the Write permission does not allow variable changes

---

### Question 13 — Dynamic Provider Credentials (OIDC)

**Difficulty**: Hard
**Answer Type**: one
**Topic**: Purpose and benefit of dynamic provider credentials using OIDC in HCP Terraform

**Question**:
What is the primary security benefit of using **dynamic provider credentials** (OIDC) in HCP Terraform workspaces?

- A) OIDC credentials are stored in HCP Terraform's vault and rotated every 24 hours automatically
- B) OIDC eliminates the need to store long-lived static cloud credentials in HCP Terraform — each run receives a short-lived token that expires after the run completes
- C) OIDC allows multiple cloud providers to share a single set of credentials, reducing the number of secrets to manage
- D) OIDC enables HCP Terraform to bypass multi-factor authentication requirements for cloud providers

## Answer Key

| Q# | Answer(s) | Explanation | Source | Difficulty |
|----|-----------|-----------:|--------|------------|
| 1 | B | N/A | Which import method is preferred in Terraform 1.5+ and why | Easy |
| 2 | C | N/A | Required arguments in an `import` block | Easy |
| 3 | C | N/A | What must exist in configuration before running `terraform import` CLI command | Medium |
| 4 | B | N/A | Purpose of the `-generate-config-out` flag | Medium |
| 5 | B | N/A | Order of `TF_LOG` levels from most to least verbose | Medium |
| 6 | A, B | N/A | `TF_LOG_PATH`, `TF_LOG_CORE`, and `TF_LOG_PROVIDER` environment variables | Medium |
| 7 | B | N/A | The `cloud` block and when it was introduced | Medium |
| 8 | C | N/A | Where `terraform login` stores the API token | Medium |
| 9 | B | N/A | The three HCP Terraform run types | Medium |
| 10 | B | N/A | The three Sentinel/OPA policy enforcement levels | Medium |
| 11 | B | N/A | What variable sets are and how they are used | Medium |
| 12 | A, C | N/A | The four workspace-level permission tiers in HCP Terraform | Hard |
| 13 | B | N/A | Purpose and benefit of dynamic provider credentials using OIDC in HCP Terraform | Hard |
