# Terraform Associate Exam Questions

---

### Question 1 — New Module Source Added Without terraform init

**Difficulty**: Easy
**Answer Type**: one
**Topic**: What happens when a new module source is added but `terraform init` has not been re-run

**Question**:
An engineer adds this block to an existing configuration for the first time:

```hcl
module "networking" {
  source   = "./modules/networking"
  vpc_cidr = "10.0.0.0/16"
}
```

The `./modules/networking` directory exists but `terraform init` has not been re-run since the block was added. What happens when `terraform plan` is run?

- A) The plan succeeds and proposes all resources defined inside the networking module
- B) Terraform raises an error indicating the module is not installed and `terraform init` must be run
- C) The module resources are silently skipped without error until `terraform init` is next executed
- D) Terraform automatically downloads and installs the local module during the plan operation

---

### Question 2 — terraform state rm Effect on Next Plan

**Difficulty**: Easy
**Answer Type**: one
**Topic**: What `terraform plan` shows immediately after `terraform state rm` removes a managed resource

**Question**:
An engineer runs:

```bash
terraform state rm aws_s3_bucket.assets
```

The `aws_s3_bucket.assets` resource block still exists in `main.tf` and the actual S3 bucket still exists in AWS. What does the next `terraform plan` propose?

- A) No changes — the resource was removed from tracking, so Terraform ignores it in future plans
- B) Destroy `aws_s3_bucket.assets` — since it is absent from state, Terraform treats it as unmanaged drift
- C) Create `aws_s3_bucket.assets` — since it is absent from state, Terraform treats it as a new resource to provision
- D) An error: Terraform refuses to plan when the state and configuration are out of sync

---

### Question 3 — Accessing a Child Module Output

**Difficulty**: Easy
**Answer Type**: one
**Topic**: The address used in the root module to reference a specific output from a child module

**Question**:
A child module is instantiated in the root module as:

```hcl
module "database" {
  source = "./modules/database"
}
```

The child module exports:

```hcl
output "connection_string" {
  value = aws_db_instance.main.endpoint
}
```

How does the root module reference the `connection_string` output?

- A) `var.database.connection_string`
- B) `module.database.connection_string`
- C) `database.outputs.connection_string`
- D) `output.database.connection_string`

---

### Question 4 — Passing Undeclared Input to Child Module

**Difficulty**: Medium
**Answer Type**: one
**Topic**: What happens at plan time when the root module passes an argument the child module never declared

**Question**:
A root module calls a child module:

```hcl
module "compute" {
  source      = "./modules/compute"
  ami         = "ami-0abc123"
  environment = var.environment
  debug_mode  = true   # not declared in ./modules/compute/variables.tf
}
```

The child module has no `variable "debug_mode"` block. What happens when `terraform plan` is run?

- A) `debug_mode` is silently ignored — unknown inputs are discarded without error
- B) Terraform raises an error: an argument named `debug_mode` is not expected in this module
- C) The value is available inside the child module as an implicit local: `local.debug_mode`
- D) `terraform plan` succeeds but emits a warning advising the team to declare the variable

---

### Question 5 — version Argument on a Local Module Source

**Difficulty**: Medium
**Answer Type**: one
**Topic**: What terraform init does when `version` is specified alongside a local path module source

**Question**:
A module block is written as:

```hcl
module "networking" {
  source  = "./modules/networking"
  version = "~> 1.0"
}
```

What happens when `terraform init` is run?

- A) The `version` constraint is silently ignored because local paths have no version registry
- B) Terraform raises an error: `version` is not valid for local module sources
- C) Terraform checks the `versions.tf` file inside `./modules/networking/` to verify the constraint is satisfied
- D) Terraform creates a `MODULE_VERSION` file in the module directory to record the pinned version

---

### Question 6 — Backend Changed Without Re-Running terraform init

**Difficulty**: Medium
**Answer Type**: one
**Topic**: What happens when the backend block is changed but `terraform init` has not been re-run

**Question**:
A team edits `main.tf` to switch from a `local` backend to an `s3` backend. Without re-running `terraform init`, an engineer immediately runs `terraform plan`. What happens?

- A) `terraform plan` detects the backend change, automatically reconfigures to S3, and proceeds with planning
- B) `terraform plan` reads state from the old local `terraform.tfstate` file and displays a plan based on that state
- C) Terraform raises an error: the backend configuration has changed and `terraform init` must be run to apply it
- D) Terraform raises an authentication error because the S3 credentials have not been initialised

---

### Question 7 — terraform state mv Followed by HCL Rename

**Difficulty**: Medium
**Answer Type**: one
**Topic**: What terraform plan shows after state mv and a matching HCL resource label rename

**Question**:
An engineer executes:

```bash
terraform state mv aws_instance.web aws_instance.web_server
```

The HCL configuration is also updated to rename the resource block from `aws_instance "web"` to `aws_instance "web_server"`. What does `terraform plan` propose on the next run?

- A) Destroy `aws_instance.web` and create `aws_instance.web_server` — the rename is treated as a replacement
- B) No changes — the resource exists in state under the new name and the configuration matches
- C) An in-place update — only metadata attributes like `tags.Name` are updated to reflect the rename
- D) An error: `terraform state mv` cannot be used for renames; a `moved` block must be used instead

---

### Question 8 — terraform apply -refresh-only After Manual Resize

**Difficulty**: Medium
**Answer Type**: many
**Topic**: What `terraform apply -refresh-only` does and does not modify

**Question**:
After an engineer manually resizes an EC2 instance from `t3.micro` to `t3.small` in the AWS Console, a colleague runs `terraform apply -refresh-only`. Which TWO statements correctly describe what this command does? (Select two.)

- A) The EC2 instance is resized back to `t3.micro` to match the `instance_type` in the Terraform configuration
- B) The Terraform state file is updated to record `instance_type = "t3.small"` to match the actual cloud state
- C) No cloud resources are created, modified, or destroyed
- D) The `terraform.tfvars` file is updated to set `instance_type = "t3.small"`

---

### Question 9 — S3 Backend Without DynamoDB Locking During Concurrent Applies

**Difficulty**: Medium
**Answer Type**: one
**Topic**: What risk exists when using an S3 backend without a DynamoDB lock table configured

**Question**:
Two engineers share an S3 backend for state storage, but the backend block does not include a `dynamodb_table` argument. Both engineers run `terraform apply` at exactly the same time against the same workspace. What is the risk?

- A) Terraform automatically queues the second apply to run after the first completes
- B) Both applies succeed without issue because S3 provides native atomic write locking
- C) The state file can become corrupted — without a DynamoDB lock table, nothing prevents both applies from writing state simultaneously
- D) The second apply fails with a 409 Conflict error from S3 because concurrent uploads are rejected

---

### Question 10 — Root Variable Not Explicitly Passed to Child Module

**Difficulty**: Medium
**Answer Type**: one
**Topic**: What happens when a child module's required variable is not passed in the module block

**Question**:
The root module defines:

```hcl
variable "region" {
  default = "us-east-1"
}
```

The child module `./modules/network` declares:

```hcl
variable "region" {}   # no default
```

The root module calls:

```hcl
module "network" {
  source   = "./modules/network"
  vpc_cidr = "10.0.0.0/16"
  # 'region' is NOT passed here
}
```

What happens during `terraform plan`?

- A) The child module uses `"us-east-1"` — it inherits `var.region` from the root module automatically
- B) Terraform raises an error: the required input variable `region` is not set for module `network`
- C) The child module uses an empty string `""` as the value for `var.region`
- D) Terraform reads the `TF_VAR_region` environment variable and passes it to the child module automatically

---

### Question 11 — terraform state pull Output

**Difficulty**: Medium
**Answer Type**: many
**Topic**: What `terraform state pull` outputs and how it can be used

**Question**:
An engineer runs `terraform state pull` on a workspace that uses an S3 remote backend. Which TWO statements correctly describe the behaviour? (Select two.)

- A) `terraform state pull` downloads the current remote state and prints it to stdout as a JSON document
- B) `terraform state pull` downloads the current remote state and saves it automatically as `terraform.tfstate` in the working directory
- C) The output can be captured using shell redirection: `terraform state pull > backup.tfstate`
- D) `terraform state pull` acquires a write lock on the state file for the duration of the command

---

### Question 12 — Leftover Local State After terraform init -migrate-state

**Difficulty**: Hard
**Answer Type**: one
**Topic**: What happens to the old local terraform.tfstate after a successful migration to a remote backend

**Question**:
A team switches from the local backend to an S3 backend and runs `terraform init -migrate-state`. The migration completes successfully. What is the status of the old `terraform.tfstate` file in the working directory?

- A) The file is automatically deleted — Terraform removes it to prevent a stale local state from being used accidentally
- B) The file is renamed to `terraform.tfstate.migrated` to indicate it has been superseded by the remote backend
- C) The file remains in the working directory unchanged; Terraform no longer reads from it but does not remove it
- D) The file is moved to `.terraform/state-backup/` by the migration process

---

### Question 13 — terraform.tfstate.backup After Multiple Applies

**Difficulty**: Hard
**Answer Type**: many
**Topic**: What terraform.tfstate.backup contains after multiple applies and its limitation as a backup mechanism

**Question**:
An engineer runs three consecutive `terraform apply` operations on a local-backend configuration. After all three applies complete, which TWO statements correctly describe `terraform.tfstate.backup`? (Select two.)

- A) `terraform.tfstate.backup` contains state snapshots from all three previous applies — it is a rolling three-entry history
- B) `terraform.tfstate.backup` contains only the state snapshot from immediately before the most recent (third) apply
- C) The content of `terraform.tfstate.backup` at this point represents the state as it existed after the second apply completed
- D) `terraform.tfstate.backup` stores the two most recent snapshots and automatically prunes older ones

## Answer Key

| Q# | Answer(s) | Explanation | Source | Difficulty |
|----|-----------|-----------:|--------|------------|
| 1 | B | N/A | What happens when a new module source is added but `terraform init` has not been re-run | Easy |
| 2 | C | N/A | What `terraform plan` shows immediately after `terraform state rm` removes a managed resource | Easy |
| 3 | B | N/A | The address used in the root module to reference a specific output from a child module | Easy |
| 4 | B | N/A | What happens at plan time when the root module passes an argument the child module never declared | Medium |
| 5 | B | N/A | What terraform init does when `version` is specified alongside a local path module source | Medium |
| 6 | C | N/A | What happens when the backend block is changed but `terraform init` has not been re-run | Medium |
| 7 | B | N/A | What terraform plan shows after state mv and a matching HCL resource label rename | Medium |
| 8 | B, C | N/A | What `terraform apply -refresh-only` does and does not modify | Medium |
| 9 | C | N/A | What risk exists when using an S3 backend without a DynamoDB lock table configured | Medium |
| 10 | B | N/A | What happens when a child module's required variable is not passed in the module block | Medium |
| 11 | A, C | N/A | What `terraform state pull` outputs and how it can be used | Medium |
| 12 | C | N/A | What happens to the old local terraform.tfstate after a successful migration to a remote backend | Hard |
| 13 | B, C | N/A | What terraform.tfstate.backup contains after multiple applies and its limitation as a backup mechanism | Hard |
