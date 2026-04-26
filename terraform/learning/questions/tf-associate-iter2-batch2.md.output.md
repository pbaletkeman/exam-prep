# Terraform Associate Exam Questions

---

### Question 1 — Apply Without Init

**Difficulty**: Easy
**Answer Type**: one
**Topic**: What happens when terraform apply runs before terraform init

**Question**:
A developer clones a Terraform repository and immediately runs `terraform apply` without first running `terraform init`. What happens?

- A) Terraform applies the configuration successfully using the provider versions from the previous engineer's machine
- B) Terraform returns an error because the required provider plugins have not been downloaded yet
- C) Terraform downloads the providers on-the-fly during apply and then proceeds
- D) Terraform applies the configuration but skips any resources that require provider authentication

---

### Question 2 — Init with `~> 5.0` Constraint

**Difficulty**: Easy
**Answer Type**: one
**Topic**: Which provider version gets installed when `~> 5.0` is specified and v5.31 is available

**Question**:
A `required_providers` block specifies `version = "~> 5.0"` for the AWS provider. The latest available versions are `5.31.0` and `6.0.0`. `terraform init` is run for the first time (no lock file exists). Which version is installed?

- A) `6.0.0` — the absolute latest version available
- B) `5.31.0` — the latest version within the `>= 5.0, < 6.0` range
- C) `5.0.0` — the minimum version satisfying the constraint
- D) The command fails because `~>` requires an exact version number

---

### Question 3 — Lock File Not Committed

**Difficulty**: Easy
**Answer Type**: one
**Topic**: What happens when .terraform.lock.hcl is not committed to version control

**Question**:
A team does not commit `.terraform.lock.hcl` to their git repository. Engineer A runs `terraform init` on Monday and installs AWS provider `5.28.0`. On Tuesday, AWS provider `5.31.0` is released. Engineer B clones the repo and runs `terraform init`. What happens?

- A) Engineer B gets the same `5.28.0` version because the lock file is shared through Terraform's registry cache
- B) Engineer B gets `5.28.0` because `terraform init` always installs the minimum version satisfying the constraint
- C) Engineer B installs the latest version matching the constraint — potentially `5.31.0` — resulting in a different provider version than Engineer A
- D) `terraform init` fails because there is no lock file to verify against

---

### Question 4 — `terraform init -upgrade` Behaviour

**Difficulty**: Medium
**Answer Type**: one
**Topic**: What terraform init -upgrade does when a newer provider version is available

**Question**:
The lock file records AWS provider `5.10.0`. The `required_providers` constraint is `~> 5.0`. AWS provider `5.31.0` has since been released. `terraform init -upgrade` is run. What happens?

- A) The command fails because the lock file must be deleted manually before upgrading
- B) The command ignores the upgrade request because `5.10.0` still satisfies the constraint
- C) Terraform updates the lock file to `5.31.0` and downloads the new provider binary
- D) Terraform upgrades to the newest available version — including `6.0.0` — ignoring the constraint

---

### Question 5 — Provider Alias Resource Assignment

**Difficulty**: Medium
**Answer Type**: one
**Topic**: What happens when a resource omits a provider argument when multiple provider configs exist

**Question**:
Two AWS provider configurations are declared: a default (`region = "us-east-1"`) and an aliased one (`alias = "west", region = "us-west-2"`). An `aws_instance` resource block is written without a `provider` argument. In which region is the instance created?

- A) `us-west-2` — Terraform uses the most recently declared provider
- B) `us-east-1` — Terraform uses the default (unaliased) provider configuration
- C) Terraform returns an error because the `provider` argument is required when multiple configs exist
- D) Terraform creates an instance in both regions because it cannot determine which to use

---

### Question 6 — `terraform state rm` Effect

**Difficulty**: Medium
**Answer Type**: one
**Topic**: What happens to a cloud resource after terraform state rm is run

**Question**:
A team runs `terraform state rm aws_s3_bucket.legacy`. The S3 bucket exists in the cloud. What is the outcome?

- A) The S3 bucket is immediately deleted from AWS
- B) The S3 bucket is deleted from AWS on the next `terraform apply`
- C) The S3 bucket continues to exist in AWS but is no longer tracked or managed by Terraform
- D) Terraform marks the bucket as tainted and schedules it for replacement on the next apply

---

### Question 7 — Concurrent Local State Applies

**Difficulty**: Medium
**Answer Type**: many
**Topic**: What happens when two engineers run terraform apply simultaneously with local state

**Question**:
Two engineers working on the same project both have the local `terraform.tfstate` file on their laptops. They run `terraform apply` at the same time against the same cloud environment. Which TWO outcomes are likely? (Select two.)

- A) Terraform detects the simultaneous apply and queues them sequentially without any data loss
- B) Both applies may succeed independently, but their state files will now differ and be out of sync with each other
- C) One apply may overwrite the other's state file changes, leading to state corruption or lost resource tracking
- D) Local state automatically merges changes from both applies into a unified state file

---

### Question 8 — Plan with Sensitive Output

**Difficulty**: Medium
**Answer Type**: one
**Topic**: What happens to a sensitive output value in plan output vs state

**Question**:
An output is declared as:

```hcl
output "db_password" {
  value     = aws_db_instance.main.password
  sensitive = true
}
```

`terraform apply` completes successfully. What is the behaviour?

- A) The password is hidden from the terminal output and is also encrypted in `terraform.tfstate`
- B) The password is displayed in the terminal but marked with a warning; it is encrypted in state
- C) The password is hidden from the terminal output (`(sensitive value)`), but it is stored in plaintext in `terraform.tfstate`
- D) The password is hidden from both the terminal and state, requiring the engineer to retrieve it from the cloud provider

---

### Question 9 — `terraform plan -refresh=false` After Manual Change

**Difficulty**: Medium
**Answer Type**: one
**Topic**: What plan -refresh=false reports when cloud has drifted

**Question**:
An engineer manually changes an EC2 instance's type from `t3.micro` to `t3.large` through the AWS console. The Terraform configuration still declares `t3.micro`. A team member runs `terraform plan -refresh=false`. What does Terraform report?

- A) Terraform detects the drift and proposes reverting the instance type to `t3.micro`
- B) Terraform reports no changes because `-refresh=false` uses cached state, which still records `t3.micro`, and the configuration also declares `t3.micro`
- C) Terraform reports no changes and automatically updates the configuration to match the new instance type
- D) Terraform returns an error because `-refresh=false` cannot be used after manual changes

---

### Question 10 — State After `terraform state mv`

**Difficulty**: Medium
**Answer Type**: one
**Topic**: What terraform state mv does to the resource in the cloud

**Question**:
An engineer runs `terraform state mv aws_instance.app aws_instance.web`. The EC2 instance is running in AWS. What is the immediate outcome?

- A) The EC2 instance is destroyed and recreated with the name `web`
- B) The state file is updated to reference the instance as `aws_instance.web`; the EC2 instance itself is untouched
- C) The command updates both the state file and the `.tf` configuration file to rename the resource
- D) The EC2 instance's Name tag is updated to `web` in AWS

---

### Question 11 — Applying with Multiple Providers and No Authentication

**Difficulty**: Medium
**Answer Type**: many
**Topic**: What happens when a provider config has no credentials at apply time

**Question**:
A configuration declares an AWS provider and a Google provider but no authentication credentials are set in the provider blocks, environment variables, or credential files. `terraform apply` is run. Which TWO outcomes are most likely? (Select two.)

- A) Terraform skips resources belonging to providers with missing credentials and applies only the remaining resources
- B) Terraform begins the apply, but resource operations fail with authentication errors when provider API calls are made
- C) `terraform plan` and `terraform apply` may fail or produce errors during provider initialisation if the providers cannot authenticate
- D) Terraform uses anonymous access where available and creates public-only resources without authentication

---

### Question 12 — Deleting the State File Before Plan

**Difficulty**: Hard
**Answer Type**: one
**Topic**: What terraform plan proposes when the state file is missing

**Question**:
A Terraform configuration manages 15 cloud resources. The `terraform.tfstate` file is accidentally deleted. `terraform plan` is run immediately after. What does Terraform propose?

- A) Terraform returns an error because it cannot run without a state file
- B) Terraform detects the 15 existing resources via API and proposes no changes
- C) Terraform treats all 15 resources as non-existent and proposes creating all of them
- D) Terraform recreates the state file automatically by querying the cloud API

---

### Question 13 — gRPC Failure Between Core and Provider

**Difficulty**: Hard
**Answer Type**: one
**Topic**: What happens if the provider plugin crashes during an apply

**Question**:
During a `terraform apply`, the AWS provider plugin process crashes mid-operation while creating a resource. What is the most likely consequence?

- A) Terraform Core detects the crash, rolls back all changes already made, and returns the infrastructure to its pre-apply state
- B) Terraform Core reports an error; the resource may be partially created in AWS but not recorded in state, requiring manual reconciliation
- C) Terraform Core restarts the provider plugin automatically and retries the failed operation from the beginning
- D) The crash causes Terraform Core to also terminate, leaving state permanently corrupted

## Answer Key

| Q# | Answer(s) | Explanation | Source | Difficulty |
|----|-----------|-----------:|--------|------------|
| 1 | B | N/A | What happens when terraform apply runs before terraform init | Easy |
| 2 | B | N/A | Which provider version gets installed when `~> 5.0` is specified and v5.31 is available | Easy |
| 3 | C | N/A | What happens when .terraform.lock.hcl is not committed to version control | Easy |
| 4 | C | N/A | What terraform init -upgrade does when a newer provider version is available | Medium |
| 5 | B | N/A | What happens when a resource omits a provider argument when multiple provider configs exist | Medium |
| 6 | C | N/A | What happens to a cloud resource after terraform state rm is run | Medium |
| 7 | B, C | N/A | What happens when two engineers run terraform apply simultaneously with local state | Medium |
| 8 | C | N/A | What happens to a sensitive output value in plan output vs state | Medium |
| 9 | B | N/A | What plan -refresh=false reports when cloud has drifted | Medium |
| 10 | B | N/A | What terraform state mv does to the resource in the cloud | Medium |
| 11 | B, C | N/A | What happens when a provider config has no credentials at apply time | Medium |
| 12 | C | N/A | What terraform plan proposes when the state file is missing | Hard |
| 13 | B | N/A | What happens if the provider plugin crashes during an apply | Hard |
