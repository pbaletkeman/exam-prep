# Terraform Associate Exam Questions

---

### Question 1 — Importing a `for_each` Resource: Correct `to` Address Syntax

**Difficulty**: Medium
**Answer Type**: one
**Topic**: When the target resource uses `for_each`, the `import` block's `to` argument must include the specific instance key in square bracket notation — `resource_type.name["key"]` — the same syntax used in plan output and state addresses

**Scenario**:
A team manages EC2 instances using `for_each` keyed by server role:

```hcl
resource "aws_instance" "server" {
  for_each      = var.servers
  ami           = each.value.ami
  instance_type = each.value.instance_type
}
```

Currently `var.servers` has keys `"web"` and `"api"`. A pre-existing `"db"` instance (`i-0xyz789abc123`) was created manually and needs to be brought under Terraform management. The engineer writes an import block:

```hcl
import {
  to = ???
  id = "i-0xyz789abc123"
}
```

**Question**:
What is the correct value for the `to` argument?

- A) `aws_instance.server` — the `for_each` key is implied by the `id` argument; Terraform resolves the target instance from the cloud resource ID
- B) `aws_instance.server["db"]` — when the target resource uses `for_each`, the `to` argument must include the specific instance key in square brackets using the same notation used in plan output and state addresses
- C) `aws_instance.server.db` — dot notation is valid for both module path traversal and `for_each` key references within a resource address
- D) `aws_instance.server[db]` — the key is placed in square brackets without quotes; unquoted identifiers are valid for `for_each` string keys in import blocks

---

### Question 2 — `TF_LOG=TRACE` in CI Exposes Plaintext Credentials in Log Files

**Difficulty**: Medium
**Answer Type**: one
**Topic**: `TF_LOG=TRACE` captures all provider plugin activity including HTTP request headers and payloads — if combined with `TF_LOG_PATH`, plaintext credentials can be persisted to files in CI artifact storage; debug logging should be unset after debugging and log files purged

**Scenario**:
A DevOps engineer adds `TF_LOG=TRACE` and `TF_LOG_PATH=/tmp/terraform-debug.log` to a CI pipeline to debug an intermittent provider API issue. The fix is confirmed and the debugging variables are left in the pipeline for "future use." A security team audit two weeks later discovers that every CI run has been writing log files that contain the AWS secret access key in plaintext within provider HTTP request payloads.

**Question**:
What is the root cause of this credential exposure, and what should the engineer have done?

- A) `TF_LOG=TRACE` is a security vulnerability in the Terraform binary that always writes provider credentials to `/var/log/syslog` — it should never be used even locally
- B) `TRACE` level logging captures all provider plugin activity including HTTP request headers and response bodies. Provider API calls include authentication data (AWS Signature headers, tokens) that appear in plaintext in the trace output. After resolving the debugging issue, the engineer should have unset `TF_LOG` (or set it to `OFF`) and removed `TF_LOG_PATH`. Any log files stored in CI artifacts should be purged or treated as sensitive. Best practice is to use short-lived, scoped credentials for debug sessions so that any inadvertently logged credentials are already expired
- C) The exposure was caused by `TF_LOG_PATH` alone — without this variable, Terraform discards log output to `/dev/null`, making it safe to leave `TF_LOG=TRACE` permanently set in CI
- D) `TF_LOG=TRACE` only captures Terraform core operations and does not include provider plugin network traffic — the credential exposure was caused by a misconfigured provider independently logging its own authentication headers, unrelated to `TF_LOG`

---

### Question 3 — "Plan" Workspace Permission Cannot Trigger or Confirm Applies

**Difficulty**: Easy
**Answer Type**: one
**Topic**: HCP Terraform's "Plan" workspace permission allows triggering speculative plans only — applying a plan requires at minimum "Write" permission

**Scenario**:
A junior developer is onboarded to an HCP Terraform workspace with "Plan" access. They've been asked to deploy a bug fix and attempt to click "Confirm & Apply" on a completed plan in the HCP Terraform UI. The button is greyed out and they receive an authorization error.

**Question**:
What is the explanation?

- A) The workspace is in remote execution mode — only local execution mode allows users to confirm applies from the UI regardless of permission level
- B) The "Plan" permission in HCP Terraform allows a user to trigger speculative plans but does not grant the ability to queue, trigger, or confirm apply runs. Applying a run requires at minimum "Write" permission on the workspace
- C) The apply button is disabled because the run is in "plan pending review" status — any user including those with "Plan" permission can confirm applies once a teammate with "Admin" access approves the review gate
- D) CLI-only: applies can only be confirmed via `terraform apply` from the CLI — the HCP Terraform UI always requires Admin permission to confirm an apply regardless of other permission levels

---

### Question 4 — `terraform_remote_state` Reading a Sensitive Output from Another Workspace

**Difficulty**: Hard
**Answer Type**: many
**Topic**: `terraform_remote_state` can access outputs marked `sensitive = true` in the source workspace — the value is not encrypted or blocked from cross-workspace reads; the sensitivity marking propagates into the consuming workspace, where the value is redacted in plan/apply output

**Scenario**:
The `networking` workspace declares an output for a database password:

```hcl
output "db_password" {
  value     = random_password.db.result
  sensitive = true
}
```

The `compute` workspace reads it:

```hcl
data "terraform_remote_state" "networking" {
  backend = "remote"
  config = {
    organization = "my-org"
    workspaces = { name = "networking" }
  }
}

resource "aws_db_instance" "app" {
  password = data.terraform_remote_state.networking.outputs.db_password
}
```

**Question**:
Which TWO statements accurately describe the behaviour?

- A) `terraform_remote_state` cannot read outputs marked `sensitive = true` — the marking encrypts the value in the source workspace's state file and prevents cross-workspace access
- B) The `db_password` output value is accessible to the `compute` workspace via `terraform_remote_state` — `sensitive = true` in the `networking` workspace controls display suppression in the producing workspace's CLI output but does not encrypt or block the value in state
- C) In the `compute` workspace, `data.terraform_remote_state.networking.outputs.db_password` is treated as a sensitive value — it will be redacted in the compute workspace's plan and apply output because the sensitivity marking propagates from the producing workspace through the remote state data source into the consuming workspace
- D) Any resource in the `compute` workspace that references this value must also declare `sensitive = true` explicitly on the resource block — failing to do so causes an apply-time sensitivity violation error

---

### Question 6 — VCS Integration Only Triggers Runs on the Configured Branch

**Difficulty**: Medium
**Answer Type**: one
**Topic**: HCP Terraform VCS workspaces trigger plan-and-apply runs only on pushes to the configured trigger branch — direct pushes to feature branches do not trigger runs; speculative plans for feature branches are triggered by opening a pull request targeting the configured branch

**Scenario**:
A team connects their HCP Terraform workspace to a GitHub repository with `main` as the VCS trigger branch. A developer pushes commits modifying `.tf` files to a feature branch `feature/add-security-groups`. They wait for a run to appear in HCP Terraform but nothing triggers. The developer is confused — they expected at minimum a speculative plan to run for their feature branch.

**Question**:
Why did no run trigger, and when would a speculative plan appear?

- A) HCP Terraform triggers speculative plans on all branches by default — the missing run indicates the `.tf` changes were in a subdirectory that doesn't match the workspace's configured working directory
- B) HCP Terraform VCS workspaces only trigger runs based on the configured branch. A direct push to a feature branch triggers no run. A speculative plan is triggered when the developer **opens a pull request** targeting the configured branch (e.g., `feature/add-security-groups` → `main`) — the speculative plan is displayed in the PR. A push or merge to `main` triggers a plan-and-apply run
- C) Feature branch pushes trigger speculative plans only when the branch name matches a `branch_prefix_filter` pattern configured in the workspace — the run was not triggered because no prefix filter was configured
- D) GitHub must be configured to send a new webhook event each time a feature branch is created — without this one-time setup step per branch, HCP Terraform's webhook is unaware of commits to new branches

---

### Question 7 — Legacy CLI Import Succeeds But `terraform plan` Shows Replacement

**Difficulty**: Medium
**Answer Type**: one
**Topic**: `terraform import` only adds the resource to the state file — it does not update the configuration; when the resource block in `.tf` files is incomplete or incorrect, the next plan computes a diff and may show destructive changes to reconcile configuration against state

**Scenario**:
An engineer imports an existing RDS instance into Terraform management:

```bash
terraform import aws_db_instance.main myapp-rds-prod
```

The command succeeds. The only resource block in the configuration is:

```hcl
resource "aws_db_instance" "main" {
  identifier = "myapp-rds-prod"
  engine     = "mysql"
}
```

Running `terraform plan` immediately after produces:

```
aws_db_instance.main must be replaced
  ~ engine_version     = "8.0.36" -> null (forces replacement)
  ~ instance_class     = "db.t3.medium" -> null (forces replacement)
  ~ allocated_storage  = 100 -> null (forces replacement)
```

**Question**:
Why does Terraform plan a replacement immediately after a successful import?

- A) `terraform import` creates a pending-state entry that requires one additional `terraform apply` to finalize — the replacement is expected and will not destroy the actual RDS instance during this finalization apply
- B) `terraform import` only adds the resource to the state file with its actual attributes — it does not modify the `.tf` configuration. The resource block declares only `identifier` and `engine`, omitting required attributes (`engine_version`, `instance_class`, `allocated_storage`). Terraform plans to reconcile the sparse configuration against the state, and because these omitted attributes would be set to null or defaults, Terraform plans a replacement. The engineer must run `terraform state show aws_db_instance.main`, record all actual attributes, and update the configuration to fully match the existing instance before re-running `terraform plan`
- C) The replacement is triggered because `engine = "mysql"` without an explicit `engine_version` causes Terraform to interpret this as a request to replace the instance with the latest MySQL version
- D) The state lock from `terraform import` expires after 60 seconds — running `terraform plan` after the lock expires causes Terraform to lose the import context and plan a full replacement

---

### Question 8 — Soft-Mandatory Policy Failure: Which Roles Can Override

**Difficulty**: Medium
**Answer Type**: one
**Topic**: `soft-mandatory` Sentinel/OPA policy failures block a run but can be overridden by authorised users — workspace Admins and organisation Owners can override; users with only "Write" permission cannot

**Scenario**:
An HCP Terraform workspace has a Sentinel policy set attached with `enforcement_level = "soft-mandatory"`. The policy requires all EC2 instances to include a `CostCenter` tag. A plan runs for a change that adds two new EC2 instances without the required tag. The policy check fails and the run is blocked. A DevOps engineer with "Admin" workspace permission sees the failure in the HCP Terraform UI and wants to know if they can override it and proceed — the tag will be added in a follow-up PR.

**Question**:
Can the Admin user override the soft-mandatory policy failure and allow the run to proceed?

- A) No — `soft-mandatory` and `hard-mandatory` both block runs unconditionally; the only difference between them is the icon colour in the UI
- B) Yes — a workspace Admin can override a `soft-mandatory` policy failure by clicking "Override & Continue" in the HCP Terraform UI. The override is recorded in the audit trail. The team should remediate the underlying policy violation (add the `CostCenter` tag) in a follow-up change
- C) No — `soft-mandatory` policy failures can only be overridden by the HCP Terraform organisation Owner; workspace-level Admin cannot override policy failures regardless of workspace permission
- D) Yes — any user with at least "Write" workspace permission can override a `soft-mandatory` failure, because Write is sufficient to trigger and approve all run types

---

### Question 9 — Run Triggers Must Be Explicitly Configured — No Implicit Chaining

**Difficulty**: Easy
**Answer Type**: one
**Topic**: HCP Terraform workspace run triggers must be explicitly configured — workspaces do not automatically run when a workspace they depend on via `terraform_remote_state` completes an apply

**Scenario**:
A team manages `networking` and `compute` as separate HCP Terraform workspaces. The `compute` workspace reads VPC and subnet IDs from `networking` via `terraform_remote_state`. After successfully applying changes in `networking` (new subnet added), the team expects `compute` to automatically queue a run to pick up the new subnet ID. Nothing happens — `compute` never runs.

**Question**:
What is the explanation?

- A) HCP Terraform automatically queues a run in all workspaces that read from a workspace via `terraform_remote_state` when that workspace's state is updated — the missing trigger indicates a misconfigured `terraform_remote_state` data source
- B) Workspace run triggers must be **explicitly configured** in HCP Terraform — workspaces are independent by default regardless of state dependencies. To automatically queue a `compute` run after `networking` applies, the team must add `networking` as a configured Run Trigger source for the `compute` workspace in the HCP Terraform settings
- C) Run triggers only function between workspaces in the same HCP Terraform Project — workspaces in separate Projects cannot trigger each other
- D) Run triggers work in the reverse direction only — the consuming workspace (`compute`) must be configured to trigger the producing workspace (`networking`), not the other way around

---

### Question 10 — Cost Estimation Appears in HCP Terraform Run After Planning, Before Apply

**Difficulty**: Medium
**Answer Type**: one
**Topic**: HCP Terraform cost estimation runs after the plan phase completes and displays the projected monthly cost delta in the plan review UI — before the apply button is available — allowing teams to see cost impact before confirming the apply

**Scenario**:
A team is preparing to apply a Terraform plan that provisions five `m5.xlarge` EC2 instances across two availability zones. The engineering manager wants to see the projected monthly cost increase before anyone clicks "Confirm & Apply." The team lead assures the manager that HCP Terraform will display this automatically as part of the run.

**Question**:
At which point in the HCP Terraform run lifecycle does cost estimation appear, and what does it show?

- A) Cost estimation is a post-apply report — it appears in the workspace's "Cost Reports" section after the infrastructure is created and actual billing has begun
- B) Cost estimation runs after the plan phase and is displayed in the run's plan review UI — the same screen where a user would click "Confirm & Apply." It shows the projected monthly cost change (e.g., "+$972.00/month") broken down by resource, before any apply is triggered. The manager can review the cost impact before approving
- C) Cost estimation runs during `terraform plan` on the engineer's local machine when the `TF_VAR_cost_estimation=true` environment variable is set — the estimate appears in terminal output before the plan summary
- D) Cost estimation requires a separate API call after the plan completes — the team must query the HCP Terraform API endpoint `/runs/{run-id}/cost-estimate` to retrieve the data; it is not automatically displayed in the run UI

---

### Question 11 — Generated Config Must Be Reviewed Before Apply; Skipping Review Causes Destructive Plan

**Difficulty**: Hard
**Answer Type**: many
**Topic**: `terraform plan -generate-config-out` produces a starting-point configuration that may have incomplete or default attribute representations — it must be reviewed and adjusted before applying; failure to verify "No changes" after the import apply leads to destructive subsequent plans

**Scenario**:
A team imports an existing S3 bucket with a complex lifecycle configuration:

```hcl
import {
  to = aws_s3_bucket.assets
  id = "company-assets-prod-2019"
}
```

They run `terraform plan -generate-config-out=generated.tf`, which produces a `generated.tf` file. Without reviewing it, they immediately run `terraform apply`. The apply reports success. On the very next `terraform plan` they see:

```
aws_s3_bucket.assets must be replaced
  ~ force_destroy   = true -> null (forces replacement)
  ~ lifecycle_rule  = [<5 complex rules>] -> null
```

**Question**:
Which TWO statements accurately explain what happened and what the correct workflow requires?

- A) The generated configuration may have incomplete or incorrectly defaulted attribute representations that do not match the bucket's actual desired configuration. Running `terraform apply` without reviewing and adjusting `generated.tf` accepted a configuration that does not accurately describe the existing bucket — attributes missing from the generated file will appear as planned changes on the next plan
- B) `terraform plan -generate-config-out` produces a configuration guaranteed to be a complete and accurate representation of the resource. If the next plan shows changes, it means the S3 bucket was modified by another process between the import apply and the subsequent plan
- C) The import workflow requires a post-import verification step: run `terraform plan` after the import apply and confirm the output is "No changes. Your infrastructure matches the configuration." If any changes appear, the generated configuration must be adjusted to match the actual resource attributes before proceeding
- D) The `lifecycle_rule` and `force_destroy` attributes disappeared because Terraform automatically strips lifecycle-sensitive attributes from generated configs during the apply phase as a safety mechanism

---

### Question 12 — Two Configurations Sharing the Same HCP Terraform Workspace Causes State Collision

**Difficulty**: Hard
**Answer Type**: many
**Topic**: Each HCP Terraform workspace maintains exactly one state file — two Terraform configurations pointing to the same workspace overwrite each other's state on every apply; the correct architecture is one workspace per environment with variable sets for shared configuration

**Scenario**:
A team manages production and staging environments. Both environment configurations have identical `cloud` blocks:

```hcl
terraform {
  cloud {
    organization = "my-org"
    workspaces {
      name = "app-shared"
    }
  }
}
```

A staging apply runs and creates five test EC2 instances. The next production plan shows those five test instances as already existing (no planned creation), and the production-exclusive resources — a load balancer and three security groups — are missing from state and shown as "to be created."

**Question**:
Which TWO statements accurately explain what happened and the correct architectural fix?

- A) Each HCP Terraform workspace holds a single state file. Both configurations target `app-shared`, so they share the same state. The staging apply wrote a new state version containing only the five test EC2 instances and overwrote the previous state, which contained the production load balancer and security groups. Production's infrastructure now exists in AWS but is absent from state
- B) HCP Terraform merges state from multiple configurations into a single workspace — this is expected shared-workspace behaviour and is safe as long as resource names do not collide
- C) The correct architecture is one dedicated workspace per environment — `app-production` and `app-staging`. Each workspace maintains independent state, run history, variables, and access permissions. For configuration that must be shared across workspaces (such as provider credentials or common tags), variable sets are the appropriate mechanism
- D) The collision is caused by the missing `prefix` argument in the `cloud` block — setting `prefix = "prod-"` and `prefix = "staging-"` in the respective configurations would allow them to coexist safely within the same `app-shared` workspace by namespacing their state

---

### Question 13 — `terraform show -json` for Machine-Readable State in Scripts

**Difficulty**: Easy
**Answer Type**: one
**Topic**: `terraform show -json` outputs the full current state as structured JSON for programmatic consumption — it is the correct interface for scripts and tooling that need to inspect resource attributes without parsing human-readable text

**Scenario**:
A platform team builds an internal automation tool that reads Terraform-managed EC2 instance public IPs and registers them in an internal DNS system. A junior engineer proposes calling `terraform state list` to get all resource addresses and then calling `terraform state show <address>` for each one, parsing the human-readable output with regex. A senior engineer recommends a single command instead.

**Question**:
Which command is correct for this use case, and why?

- A) `terraform state list` followed by `terraform state show` for each resource — this provides the most complete human-readable output and regex parsing is standard practice for infrastructure automation scripts
- B) `terraform show -json` — this outputs the full current state as a structured JSON document. A script can parse it with standard JSON libraries to locate all `aws_instance` resources and extract `public_ip` attributes in a single invocation, without shell-parsing human-readable text or invoking multiple commands
- C) `terraform output -json` — this outputs all declared Terraform outputs as JSON, which provides complete access to all resource attributes including those not explicitly declared as outputs
- D) `terraform state pull` — this downloads the raw backend state JSON, which is the most complete and portable machine-readable representation of all resource attributes and is the recommended interface for automation tooling

## Answer Key

| Q# | Answer(s) | Explanation | Source | Difficulty |
|----|-----------|-----------:|--------|------------|
| 1 | B | N/A | When the target resource uses `for_each`, the `import` block's `to` argument must include the specific instance key in square bracket notation — `resource_type.name["key"]` — the same syntax used in plan output and state addresses | Medium |
| 2 | B | N/A | `TF_LOG=TRACE` captures all provider plugin activity including HTTP request headers and payloads — if combined with `TF_LOG_PATH`, plaintext credentials can be persisted to files in CI artifact storage; debug logging should be unset after debugging and log files purged | Medium |
| 3 | B | N/A | HCP Terraform's "Plan" workspace permission allows triggering speculative plans only — applying a plan requires at minimum "Write" permission | Easy |
| 4 | B, C | N/A | `terraform_remote_state` can access outputs marked `sensitive = true` in the source workspace — the value is not encrypted or blocked from cross-workspace reads; the sensitivity marking propagates into the consuming workspace, where the value is redacted in plan/apply output | Hard |
| 5 | B | N/A | HCP Terraform VCS workspaces trigger plan-and-apply runs only on pushes to the configured trigger branch — direct pushes to feature branches do not trigger runs; speculative plans for feature branches are triggered by opening a pull request targeting the configured branch | Medium |
| 6 | B | N/A | `terraform import` only adds the resource to the state file — it does not update the configuration; when the resource block in `.tf` files is incomplete or incorrect, the next plan computes a diff and may show destructive changes to reconcile configuration against state | Medium |
| 7 | B | N/A | `soft-mandatory` Sentinel/OPA policy failures block a run but can be overridden by authorised users — workspace Admins and organisation Owners can override; users with only "Write" permission cannot | Medium |
| 8 | B | N/A | HCP Terraform workspace run triggers must be explicitly configured — workspaces do not automatically run when a workspace they depend on via `terraform_remote_state` completes an apply | Easy |
| 9 | B | N/A | HCP Terraform cost estimation runs after the plan phase completes and displays the projected monthly cost delta in the plan review UI — before the apply button is available — allowing teams to see cost impact before confirming the apply | Medium |
| 10 | A, C | N/A | `terraform plan -generate-config-out` produces a starting-point configuration that may have incomplete or default attribute representations — it must be reviewed and adjusted before applying; failure to verify "No changes" after the import apply leads to destructive subsequent plans | Hard |
| 11 | A, C | N/A | Each HCP Terraform workspace maintains exactly one state file — two Terraform configurations pointing to the same workspace overwrite each other's state on every apply; the correct architecture is one workspace per environment with variable sets for shared configuration | Hard |
| 12 | B | N/A | `terraform show -json` outputs the full current state as structured JSON for programmatic consumption — it is the correct interface for scripts and tooling that need to inspect resource attributes without parsing human-readable text | Easy |
