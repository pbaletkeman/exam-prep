# Terraform Associate Exam Questions

---

### Question 1 — TF_LOG Without TF_LOG_PATH

**Difficulty**: Easy
**Answer Type**: one
**Topic**: Where Terraform writes log output when `TF_LOG` is set but `TF_LOG_PATH` is not

**Question**:
An engineer sets the following before running a command:

```bash
export TF_LOG=TRACE
terraform apply
```

No `TF_LOG_PATH` variable is set. Where does Terraform write the log output?

- A) To a file named `terraform.log` created automatically in the current working directory
- B) To stderr — all log output is written to the standard error stream
- C) To stdout, interleaved with the normal plan and apply output
- D) Logging is disabled when `TF_LOG_PATH` is not configured

---

### Question 2 — VCS Pull Request Triggers a Run

**Difficulty**: Easy
**Answer Type**: one
**Topic**: Which HCP Terraform run type is automatically triggered when a pull request is opened

**Question**:
A team has connected an HCP Terraform workspace to a GitHub repository. A developer opens a pull request targeting the `main` branch. What does HCP Terraform automatically do?

- A) It queues a plan-and-apply run that immediately applies changes to the workspace
- B) It queues a plan-only run that waits for manual approval before it can be applied
- C) It triggers a speculative plan and posts the result as a status check on the pull request
- D) Nothing happens until the pull request is merged; HCP Terraform only reacts to merge events

---

### Question 3 — terraform state show Output

**Difficulty**: Easy
**Answer Type**: one
**Topic**: What `terraform state show` outputs for a specific resource

**Question**:
An engineer runs:

```bash
terraform state show aws_instance.web
```

What does this command output?

- A) A JSON document representing the entire state file
- B) The HCL resource block exactly as it appears in the Terraform configuration file
- C) All recorded attributes of the `aws_instance.web` resource as stored in the state file
- D) An execution plan showing what Terraform would change about `aws_instance.web`

---

### Question 4 — CLI Import When Resource Already in State

**Difficulty**: Medium
**Answer Type**: one
**Topic**: What happens when `terraform import` targets a resource address already tracked in state

**Question**:
A resource `aws_s3_bucket.logs` already exists in the Terraform state file and is actively managed. An engineer runs:

```bash
terraform import aws_s3_bucket.logs existing-log-bucket
```

What happens?

- A) The import succeeds and refreshes the state entry with the latest attributes from the cloud
- B) Terraform raises an error indicating that `aws_s3_bucket.logs` is already managed in state
- C) Terraform creates a second, duplicate state entry for the same cloud resource
- D) The existing state entry is silently overwritten with the newly imported attributes

---

### Question 5 — import Block With an Invalid Cloud Resource ID

**Difficulty**: Medium
**Answer Type**: one
**Topic**: When Terraform surfaces an error if the `import` block's `id` does not match any real cloud resource

**Question**:
An engineer writes this configuration:

```hcl
import {
  to = aws_instance.app
  id = "i-DOESNOTEXIST"
}

resource "aws_instance" "app" {
  ami           = "ami-0abc123"
  instance_type = "t3.micro"
}
```

The instance ID `i-DOESNOTEXIST` does not correspond to any real EC2 instance. What happens when `terraform plan` is run?

- A) The import is silently skipped and Terraform plans to create a new `aws_instance.app`
- B) The plan succeeds but Terraform logs a warning about the invalid ID
- C) Terraform raises a provider error during the planning phase because the resource with that ID was not found in the cloud
- D) The error only surfaces at `terraform apply` time; the plan phase cannot validate cloud resource IDs

---

### Question 6 — generate-config-out When Resource Block Already Exists

**Difficulty**: Medium
**Answer Type**: one
**Topic**: What happens when `-generate-config-out` is used but the target resource block already exists

**Question**:
An engineer has this configuration in `main.tf`:

```hcl
import {
  to = aws_vpc.main
  id = "vpc-0abc1234"
}

resource "aws_vpc" "main" {
  cidr_block = "10.0.0.0/16"
}
```

The engineer then runs:

```bash
terraform plan -generate-config-out=generated.tf
```

What happens?

- A) The existing `resource "aws_vpc" "main"` block in `main.tf` is overwritten with the generated version
- B) Terraform raises an error: `-generate-config-out` cannot be used when the resource block already exists in configuration
- C) A second copy of the resource block is written to `generated.tf`, and Terraform warns about the duplication
- D) The `-generate-config-out` flag is silently ignored since a resource block already exists; the plan proceeds normally

---

### Question 7 — Run Trigger From Upstream Workspace Apply

**Difficulty**: Medium
**Answer Type**: one
**Topic**: What HCP Terraform does to a downstream workspace when an upstream apply completes via a run trigger

**Question**:
Workspace B (`compute`) is configured in HCP Terraform with Workspace A (`networking`) set as a **run trigger** source. Workspace A manages the VPC and subnets that Workspace B depends on. Workspace A's `terraform apply` completes successfully. What does HCP Terraform do next?

- A) Workspace B immediately begins executing without a separate planning phase
- B) Workspace B is automatically queued for a new plan-and-apply run
- C) Workspace B receives a notification in the UI but requires a developer to manually trigger a run
- D) Workspace B triggers a run only if Workspace A's apply produced at least one resource change

---

### Question 8 — hard-mandatory Policy Failure Outcomes

**Difficulty**: Medium
**Answer Type**: many
**Topic**: What happens when a `hard-mandatory` Sentinel policy fails

**Question**:
A `hard-mandatory` Sentinel policy assigned to a workspace fails during a plan. Which TWO statements correctly describe what happens next? (Select two.)

- A) The run is blocked and cannot proceed to apply
- B) An organisation Owner can override the failure from the HCP Terraform UI to allow the run to proceed
- C) No user or role can override the failure — the policy code must pass before the run can continue
- D) The run proceeds to apply but records the policy failure in the audit log as a warning

---

### Question 9 — soft-mandatory Override Attempt by Write-Level User

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Whether a user with Write workspace permission can override a soft-mandatory policy failure

**Question**:
A `soft-mandatory` Sentinel policy fails during a run in an HCP Terraform workspace. A developer with **Write** workspace permission attempts to override the policy failure using the override button in the HCP Terraform UI. What happens?

- A) The override succeeds — Write permission includes the ability to override soft-mandatory policy failures
- B) The override fails — overriding soft-mandatory policies requires the "Manage Policy Overrides" permission, which is not included in Write access
- C) The override button is not visible to the developer — it is only shown to users with Admin workspace permission
- D) The override succeeds only if the developer is also a member of the team that manages the failing policy set

---

### Question 10 — Health Assessment Detects Drift

**Difficulty**: Medium
**Answer Type**: many
**Topic**: What HCP Terraform does when a scheduled health assessment detects configuration drift

**Question**:
HCP Terraform health assessments are enabled for a workspace. On its next scheduled run, the assessment detects that an EC2 instance's `instance_type` was manually changed in the AWS Console from `t3.micro` to `t3.small`. Which TWO things happen as a result? (Select two.)

- A) HCP Terraform automatically queues a `terraform apply` run to revert the instance type back to `t3.micro`
- B) The workspace's health status is marked as drifted in the HCP Terraform UI
- C) Notifications are sent to configured notification destinations alerting the team to the detected drift
- D) The workspace is locked to prevent further runs until the team manually resolves the drift

---

### Question 11 — terraform_remote_state Output That Does Not Exist

**Difficulty**: Medium
**Answer Type**: one
**Topic**: What happens at plan time when a `terraform_remote_state` reference targets a nonexistent output

**Question**:
A root module uses this configuration:

```hcl
data "terraform_remote_state" "network" {
  backend = "remote"
  config = {
    organization = "my-org"
    workspaces = { name = "networking" }
  }
}

resource "aws_instance" "app" {
  subnet_id = data.terraform_remote_state.network.outputs.private_subnet_id
}
```

The `networking` workspace state exists and is accessible, but it does **not** export an output named `private_subnet_id`. What happens during `terraform plan`?

- A) `subnet_id` is set to `null` — Terraform treats missing remote state outputs as null values
- B) Terraform raises an error during planning because `private_subnet_id` does not exist in the remote workspace outputs
- C) `terraform plan` succeeds but `aws_instance.app` is omitted from the plan until the output exists
- D) Terraform substitutes an empty string `""` and emits a warning about the missing output

---

### Question 12 — Workspace Variable Overrides Variable Set

**Difficulty**: Hard
**Answer Type**: one
**Topic**: Variable precedence when the same key is defined in both a variable set and a workspace variable

**Question**:
An HCP Terraform organisation has a variable set named "Shared Defaults" containing:

```
environment = "default"
```

This variable set is assigned to all workspaces. The `production` workspace also has a workspace-level variable defined directly:

```
environment = "production"
```

When Terraform runs in the `production` workspace, what value does `var.environment` have?

- A) `"default"` — variable sets take precedence over workspace-level variables
- B) `"production"` — workspace-level variables take precedence over variable sets
- C) An error is raised — HCP Terraform does not allow the same variable key to be defined in both a variable set and a workspace variable
- D) The run prompts the user to choose which value to use before planning begins

---

### Question 13 — TF_LOG_CORE and TF_LOG Interaction

**Difficulty**: Hard
**Answer Type**: many
**Topic**: How `TF_LOG_CORE` overrides `TF_LOG` and the resulting log output per component

**Question**:
An engineer configures these environment variables before running `terraform apply`:

```bash
export TF_LOG=DEBUG
export TF_LOG_CORE=OFF
```

Which TWO statements correctly describe the resulting logging behaviour? (Select two.)

- A) No logs are produced at all — `TF_LOG_CORE=OFF` disables all Terraform logging globally
- B) Provider plugin logs are produced at `DEBUG` level
- C) Terraform core logs are suppressed
- D) `TF_LOG=DEBUG` overrides `TF_LOG_CORE=OFF` for core components because it was set earlier

## Answer Key

| Q# | Answer(s) | Explanation | Source | Difficulty |
|----|-----------|-----------:|--------|------------|
| 1 | B | N/A | Where Terraform writes log output when `TF_LOG` is set but `TF_LOG_PATH` is not | Easy |
| 2 | C | N/A | Which HCP Terraform run type is automatically triggered when a pull request is opened | Easy |
| 3 | C | N/A | What `terraform state show` outputs for a specific resource | Easy |
| 4 | B | N/A | What happens when `terraform import` targets a resource address already tracked in state | Medium |
| 5 | C | N/A | When Terraform surfaces an error if the `import` block's `id` does not match any real cloud resource | Medium |
| 6 | B | N/A | What happens when `-generate-config-out` is used but the target resource block already exists | Medium |
| 7 | B | N/A | What HCP Terraform does to a downstream workspace when an upstream apply completes via a run trigger | Medium |
| 8 | A, C | N/A | What happens when a `hard-mandatory` Sentinel policy fails | Medium |
| 9 | B | N/A | Whether a user with Write workspace permission can override a soft-mandatory policy failure | Medium |
| 10 | B, C | N/A | What HCP Terraform does when a scheduled health assessment detects configuration drift | Medium |
| 11 | B | N/A | What happens at plan time when a `terraform_remote_state` reference targets a nonexistent output | Medium |
| 12 | B | N/A | Variable precedence when the same key is defined in both a variable set and a workspace variable | Hard |
| 13 | B, C | N/A | How `TF_LOG_CORE` overrides `TF_LOG` and the resulting log output per component | Hard |
