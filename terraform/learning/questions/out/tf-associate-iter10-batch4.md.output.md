# Terraform Associate Exam Questions

---

### Question 1 — Zero-Downtime RDS Replacement Required

**Difficulty**: Medium
**Answer Type**: one
**Topic**: `create_before_destroy = true` reverses replacement order to avoid downtime when a resource must be replaced

**Scenario**:
A team is updating a production RDS instance parameter group. The parameter group argument is immutable, so changing it forces a replacement: Terraform's plan shows `-/+`. By default, Terraform will destroy the old RDS instance first and then create the new one. Even a few seconds of downtime is unacceptable because the database serves a real-time payment processing service. The team wants Terraform to provision the replacement RDS instance, confirm it is healthy, and only then remove the old one.

**Question**:
Which lifecycle configuration correctly implements this zero-downtime replacement order?

- A) Add `prevent_destroy = true` to the `lifecycle` block — this forces Terraform to create the new instance before it is permitted to schedule the destroy
- B) Add `create_before_destroy = true` to the `lifecycle` block — this instructs Terraform to provision the replacement resource first and only destroy the original after the new one exists
- C) Add `replace_triggered_by = [aws_db_parameter_group.new]` to the `lifecycle` block — this triggers the replacement in a create-first order automatically
- D) Add `ignore_changes = [parameter_group_name]` — this prevents the replacement from occurring and allows the parameter group change to be applied in-place

---

### Question 2 — Auto Scaling Group Keeps Reverting to Minimum Capacity

**Difficulty**: Medium
**Answer Type**: one
**Topic**: `ignore_changes` suppresses drift detection for specified attributes managed outside Terraform

**Scenario**:
An operations team uses Terraform to manage an AWS Auto Scaling Group (ASG) with `min_size = 2`. During production incidents, the on-call engineer manually scales the ASG up via the AWS console — setting `min_size = 10` to handle a traffic surge. When the incident is resolved and the next scheduled `terraform apply` runs, Terraform detects the drift and reverts `min_size` back to `2`, which causes the group to scale in aggressively. The team wants Terraform to stop overwriting `min_size` on every apply while still managing all other ASG attributes.

**Question**:
Which configuration change correctly prevents Terraform from reverting `min_size`?

- A) Remove the `min_size` argument from the resource block entirely — Terraform will use the AWS default and stop detecting changes to that attribute
- B) Add a `lifecycle` block with `ignore_changes = [min_size]` to the ASG resource — Terraform will no longer detect or revert drift on that specific attribute
- C) Add `depends_on = [aws_cloudwatch_metric_alarm.traffic]` — this tells Terraform to defer changes to the ASG until the alarm fires, preventing premature reverts
- D) Set `create_before_destroy = true` — this pauses the apply until manual changes are confirmed, avoiding the revert

---

### Question 3 — `for_each` Fails with a `list(string)` Variable

**Difficulty**: Easy
**Answer Type**: one
**Topic**: `for_each` requires a `map` or `set(string)`; a `list(string)` must be converted with `toset()`

**Scenario**:
A developer wants to create one AWS IAM user for each username in a list. They write:

```hcl
variable "usernames" {
  type    = list(string)
  default = ["alice", "bob", "carol"]
}

resource "aws_iam_user" "team" {
  for_each = var.usernames
  name     = each.key
}
```

Running `terraform plan` immediately fails with: `The given "for_each" argument value is unsuitable: the "for_each" meta-argument must be a map, or a set of strings, and you have provided a value of type list of string.`

**Question**:
What is the minimal fix to the `for_each` argument that resolves the error?

- A) Change `for_each = var.usernames` to `for_each = count(var.usernames)` — the `count()` function converts a list to the correct type
- B) Change the `for_each` meta-argument to `count = length(var.usernames)` and reference users by `count.index`
- C) Change `for_each = var.usernames` to `for_each = toset(var.usernames)` — the `toset()` function converts the list to a `set(string)`, which `for_each` accepts
- D) Change the variable type from `list(string)` to `tuple` — tuples are accepted directly by `for_each`

---

### Question 4 — Legacy S3 Bucket Must Be Removed from Terraform Without Deletion

**Difficulty**: Medium
**Answer Type**: one
**Topic**: `removed` block with `lifecycle { destroy = false }` stops Terraform managing a resource without deleting it

**Scenario**:
An organisation has a legacy S3 bucket that was provisioned by Terraform three years ago and contains compliance archives that must be retained permanently. The infrastructure team decides to remove the bucket from Terraform management entirely — it will no longer be tracked or modified by Terraform — but under no circumstances should the bucket or its contents be deleted. A junior engineer suggests deleting the `aws_s3_bucket.compliance_archive` resource block from the configuration and running `terraform apply`. The team lead rejects this approach.

**Question**:
Why does the team lead reject the proposed approach, and what is the correct alternative?

- A) The team lead rejects it because deleting a resource block and running `terraform apply` causes Terraform to destroy the corresponding cloud resource. The correct alternative is to add a `removed` block with `lifecycle { destroy = false }` to explicitly stop tracking the resource without issuing a delete API call
- B) The team lead rejects it because Terraform requires a two-step process: first run `terraform state rm` to remove it from state, then delete the resource block. Running `terraform apply` with only the block deleted would cause a validation error
- C) The team lead rejects it because deleting a resource block does nothing — Terraform continues to manage resources whose blocks are removed, reading their state from the state file
- D) The team lead rejects it because `terraform apply` requires the `-confirm-orphan` flag when resource blocks are deliberately removed to prevent accidental deletions

---

### Question 5 — Module Refactoring Moves Resources from Root to Child Module

**Difficulty**: Medium
**Answer Type**: one
**Topic**: `moved` block with `to = module.<name>.<type>.<name>` relocates a resource's state entry to a module address

**Scenario**:
A team has been managing several networking resources at the root module level for months: `aws_vpc.main`, `aws_subnet.public`, and `aws_internet_gateway.main`. The team is refactoring the configuration to introduce a reusable `networking` module. After creating the module and moving the resource blocks into `modules/networking/`, they update the root configuration to call the module. Running `terraform plan` shows three destroys and three creates — Terraform treats the new module-path addresses as entirely new resources and the old root-level addresses as orphans to be destroyed.

**Question**:
What must the team add to prevent the destroy+create cycle for each resource being moved into the module?

- A) Add `lifecycle { prevent_destroy = true }` to each resource block inside the module — this prevents Terraform from scheduling the root-level resources for deletion
- B) Add a `moved` block for each resource in the root configuration, mapping from the old root address to the new module address, e.g., `from = aws_vpc.main` / `to = module.networking.aws_vpc.main`
- C) Export the existing resource IDs as outputs from the root module and pass them as inputs to the child module, then run `terraform apply` with `-target=module.networking`
- D) Run `terraform state mv aws_vpc.main module.networking.aws_vpc.main` for each resource before applying — `moved` blocks are only for renaming within the same module level

---

### Question 6 — EC2 Instance Fails on Startup Because IAM Policy Isn't Ready

**Difficulty**: Medium
**Answer Type**: one
**Topic**: `depends_on` required for IAM policy attachments because no attribute reference exists between the IAM resource and the consuming resource

**Scenario**:
A team provisions an EC2 instance with an IAM instance profile that grants S3 read access. The Terraform configuration creates the IAM role, attaches the policy, creates the instance profile, and associates it with the EC2 instance. Terraform successfully applies all resources, but the application running on the EC2 instance intermittently fails to read from S3 at startup because the IAM policy has not fully propagated by the time the instance boots. The team adds a `depends_on` reference to the EC2 instance pointing to the IAM role policy attachment. The intermittent failures stop.

**Question**:
Why was `depends_on` necessary here when Terraform already references `aws_iam_instance_profile.app` in the EC2 resource block?

- A) `depends_on` is always required between IAM resources and compute resources — Terraform never infers IAM dependencies automatically regardless of attribute references
- B) Terraform detected the `aws_iam_instance_profile.app` attribute reference and created a dependency edge between the instance profile and the EC2 instance. However, the `aws_iam_role_policy.s3_read` attachment has no attribute referenced in the EC2 block — Terraform cannot detect that dependency through attributes alone. `depends_on` explicitly adds the missing edge so Terraform waits for the policy attachment before creating the instance
- C) `depends_on` prevents Terraform from parallelising the apply, which gives IAM time to propagate before the instance starts — it works purely as a timing delay mechanism and has nothing to do with the dependency graph
- D) The IAM policy attachment creates a dependency cycle with the instance profile, which Terraform normally skips. `depends_on` overrides cycle detection to allow the attachment to be applied first

---

### Question 7 — Data Source Returns a Value That Won't Be Known Until Apply

**Difficulty**: Hard
**Answer Type**: one
**Topic**: Data sources whose arguments contain computed (unknown-until-apply) values are deferred and read during `apply`, not `plan`

**Scenario**:
A team is writing a configuration that creates a new VPC and then immediately uses a data source to look up the route tables associated with that VPC in order to configure VPN gateway attachments. The data source's `filter` block references `aws_vpc.main.id`. When the team runs `terraform plan`, the data source section shows `(known after apply)` for its result. The team is surprised — they expected the data source to resolve during the plan phase so they could see the full plan output.

**Question**:
Why does the data source show `(known after apply)` during plan?

- A) Data sources are always deferred to the apply phase; they never resolve during `terraform plan` regardless of whether their arguments are known or unknown
- B) The VPC's `id` attribute is assigned by AWS only after the resource is created. Since `aws_vpc.main.id` is not known at plan time (the VPC does not yet exist), Terraform cannot evaluate the data source's filter during plan — the data source is deferred to the apply phase when the VPC's ID becomes available
- C) The `(known after apply)` marker means the data source has no matching results and will create the resource instead of querying existing ones during apply
- D) Data sources referenced from the same Terraform configuration as their filter dependency always fail with errors; they must be placed in a separate Terraform workspace

---

### Question 8 — Launch Template Update Does Not Refresh Running Instances

**Difficulty**: Medium
**Answer Type**: one
**Topic**: `replace_triggered_by` forces the dependent resource to be replaced when a referenced upstream resource changes

**Scenario**:
A team manages an Auto Scaling Group (ASG) and an associated Launch Template in Terraform. The launch template specifies the AMI, instance type, and user data script. When the team updates the launch template to use a new hardened AMI, `terraform apply` succeeds and creates a new launch template version. However, the ASG continues running instances based on the old launch template version — Terraform does not replace the ASG because none of the ASG's own configuration attributes changed. The team needs existing ASG instances to be replaced when the launch template changes.

**Question**:
Which lifecycle configuration on the ASG resource causes Terraform to replace the ASG whenever the launch template changes?

- A) Add `depends_on = [aws_launch_template.web]` to the ASG resource — this ensures Terraform always applies the launch template before the ASG, propagating template changes automatically to running instances
- B) Add `ignore_changes = [aws_launch_template.web]` to the ASG's `lifecycle` block — this prevents the ASG from being replaced when the launch template changes unexpectedly
- C) Add `replace_triggered_by = [aws_launch_template.web]` in the ASG resource's `lifecycle` block — this instructs Terraform to replace the ASG whenever the launch template resource changes, even if none of the ASG's own attributes changed
- D) Add `create_before_destroy = true` to the launch template's `lifecycle` block — creating the new template version first automatically triggers instance refresh in the ASG

---

### Question 9 — Nightly Teardown Pipeline Blocked by `prevent_destroy`

**Difficulty**: Medium
**Answer Type**: many
**Topic**: `prevent_destroy = true` causes `terraform apply` and `terraform destroy` to error; must be removed from config before destroying

**Scenario**:
A team runs an automated nightly pipeline that destroys a temporary integration testing environment to save costs, using `terraform destroy -auto-approve`. Last week, a developer added `lifecycle { prevent_destroy = true }` to a test database resource to avoid accidental deletion during development. The nightly destroy pipeline now fails every night with: `Error: Instance cannot be destroyed. Resource aws_db_instance.test has lifecycle.prevent_destroy set to true`. The developer is on vacation and is unavailable to review. The pipeline owner needs to understand the options.

**Question**:
Which TWO statements accurately describe the situation and the available remediation?

- A) `prevent_destroy = true` causes Terraform to error on any plan that includes a destroy operation for that resource — whether from `terraform destroy` or from a configuration-driven replacement. It does not prevent `terraform state rm` from removing the resource's state entry without destroying the cloud resource
- B) `prevent_destroy = true` is enforced at the cloud provider API level — the protection cannot be bypassed even if removed from the Terraform configuration, requiring a support ticket to AWS to unlock
- C) To allow the nightly destroy to succeed, the `prevent_destroy = true` setting must be removed from the resource block's `lifecycle` configuration, and `terraform init` must be re-run to update the provider schema before the destroy can proceed
- D) To allow the nightly destroy to succeed, `prevent_destroy = true` must be removed from the resource block's `lifecycle` configuration and the configuration re-applied or the destroy re-run — `prevent_destroy` is a Terraform-only guard evaluated at plan time; once removed from the config, the destroy plan will no longer error

---

### Question 10 — Middle Username Removed from `count`-Based IAM Users Causes Unexpected Replacements

**Difficulty**: Hard
**Answer Type**: one
**Topic**: Removing an element from the middle of a `count`-indexed list causes all subsequent instances to shift indices and be replaced

**Scenario**:
A team manages five IAM users using `count` and a `list(string)` variable:

```hcl
variable "usernames" {
  default = ["alice", "bob", "carol", "dave", "eve"]
}

resource "aws_iam_user" "team" {
  count = length(var.usernames)
  name  = var.usernames[count.index]
}
```

When `bob` leaves the company, the team removes `"bob"` from the list, leaving `["alice", "carol", "dave", "eve"]`. They expect Terraform to plan a single deletion of `aws_iam_user.team[1]`. Instead, `terraform plan` shows one deletion and three replacements. The team is confused.

**Question**:
What causes the three unexpected replacements?

- A) The `aws_iam_user` resource type does not support `count` — using it with `for_each` instead would have prevented the replacements entirely
- B) Removing `"bob"` at index 1 causes all subsequent list elements to shift down by one index: `carol` moves from index 2 to 1, `dave` from 3 to 2, and `eve` from 4 to 3. Terraform sees `team[1]` through `team[3]` as having new `name` values and plans to replace them. Only `team[4]` (the former `eve` at the last index) is deleted
- C) Terraform detects that the list length decreased and plans to delete all existing `count` instances before creating the new set, resulting in five deletes and four creates
- D) The `count.index` is not recalculated after an element is removed — Terraform reuses the old indices, causing the last element `eve` to have an orphaned index that triggers a cascade replacement

---

### Question 11 — Terraform Detects a Circular Dependency and Errors

**Difficulty**: Hard
**Answer Type**: one
**Topic**: Circular dependencies (cycles) in the resource graph cause Terraform to error; resolution requires restructuring references or using `data` sources

**Scenario**:
A developer writes a Terraform configuration where `aws_security_group.app` references `aws_security_group.db.id` (the app security group allows outbound traffic to the DB security group), and `aws_security_group.db` references `aws_security_group.app.id` (the DB security group allows inbound traffic from the app security group). Running `terraform plan` fails immediately with: `Error: Cycle: aws_security_group.app, aws_security_group.db`. The developer is unsure how to model this bidirectional security group relationship.

**Question**:
Which approach correctly resolves the circular dependency while preserving the intended security group rules?

- A) Add `depends_on = [aws_security_group.db]` to `aws_security_group.app` and `depends_on = [aws_security_group.app]` to `aws_security_group.db` — explicit `depends_on` overrides cycle detection and establishes a valid ordering
- B) Create both security groups without referencing each other (no ingress/egress rules in the group blocks themselves), then define the ingress and egress rules as separate `aws_security_group_rule` resources that reference each security group's `id` — this breaks the cycle by removing the circular attribute references from the group blocks
- C) Merge both security groups into a single `aws_security_group` resource — Terraform can handle self-referential rules within a single resource block without cycle errors
- D) Use `ignore_changes = [ingress, egress]` on both security group resources — this tells Terraform to ignore the circular references during planning

---

### Question 12 — Data Source Looks Up a Resource Created in the Same Apply

**Difficulty**: Hard
**Answer Type**: many
**Topic**: Data sources depending on newly created resources are deferred to apply phase; plan output shows `(known after apply)` for data source results

**Scenario**:
A team is writing a configuration that creates a new AWS KMS key and then immediately uses a data source (`data "aws_kms_alias"`) to look up the alias ARN of that same key, which they need to pass to an S3 bucket encryption configuration. During `terraform plan`, the S3 bucket's `kms_master_key_id` argument shows `(known after apply)` and the data source itself shows `(known after apply)` for all its outputs. The team is trying to understand why the plan is not fully resolvable.

**Question**:
Which TWO statements accurately explain the behaviour?

- A) The KMS key's alias ARN is assigned by AWS only after the key is created. Since the key does not exist yet at plan time, the data source's query cannot be executed — it is deferred to the apply phase when the key exists and the alias ARN is retrievable
- B) Data sources that reference newly created resource attributes always produce errors during plan — the only solution is to use `terraform apply` with `-refresh-only` before a standard apply
- C) The `(known after apply)` value propagates downstream: because the data source result is unknown at plan time, any resource arguments that reference the data source result are also shown as `(known after apply)` in the plan output
- D) Terraform resolves all data sources at plan time regardless of their dependencies; the `(known after apply)` marker means the S3 bucket is misconfigured and will fail during apply

---

### Question 13 — New Resource Must Be Deployed into a Specific AWS Region

**Difficulty**: Easy
**Answer Type**: one
**Topic**: The `provider` meta-argument on a resource selects an aliased provider configuration for that specific resource

**Scenario**:
A team manages infrastructure in `us-east-1` as their primary region. Their Terraform configuration declares a default AWS provider for `us-east-1` and an aliased provider for `eu-west-1`:

```hcl
provider "aws" {
  region = "us-east-1"
}

provider "aws" {
  alias  = "ireland"
  region = "eu-west-1"
}
```

The team needs to create a new S3 bucket specifically in `eu-west-1` for GDPR data residency compliance. All other resources in the configuration should remain in `us-east-1`.

**Question**:
What must the S3 bucket resource block include to deploy into `eu-west-1`?

- A) Set `region = "eu-west-1"` as a top-level argument inside the `aws_s3_bucket` resource block
- B) Include `provider = aws.ireland` as a meta-argument in the `aws_s3_bucket` resource block, referencing the aliased provider configuration for `eu-west-1`
- C) Create a new `terraform workspace` named `ireland` — workspaces automatically route resources to the region matching the workspace name
- D) Include `alias = "ireland"` as a meta-argument in the `aws_s3_bucket` resource block to select the aliased provider

## Answer Key

| Q# | Answer(s) | Explanation | Source | Difficulty |
|----|-----------|-----------:|--------|------------|
| 1 | B | N/A | `create_before_destroy = true` reverses replacement order to avoid downtime when a resource must be replaced | Medium |
| 2 | B | N/A | `ignore_changes` suppresses drift detection for specified attributes managed outside Terraform | Medium |
| 3 | C | N/A | `for_each` requires a `map` or `set(string)`; a `list(string)` must be converted with `toset()` | Easy |
| 4 | A | N/A | `removed` block with `lifecycle { destroy = false }` stops Terraform managing a resource without deleting it | Medium |
| 5 | B | N/A | `moved` block with `to = module.<name>.<type>.<name>` relocates a resource's state entry to a module address | Medium |
| 6 | B | N/A | `depends_on` required for IAM policy attachments because no attribute reference exists between the IAM resource and the consuming resource | Medium |
| 7 | B | N/A | Data sources whose arguments contain computed (unknown-until-apply) values are deferred and read during `apply`, not `plan` | Hard |
| 8 | C | N/A | `replace_triggered_by` forces the dependent resource to be replaced when a referenced upstream resource changes | Medium |
| 9 | A, D | N/A | `prevent_destroy = true` causes `terraform apply` and `terraform destroy` to error; must be removed from config before destroying | Medium |
| 10 | B | N/A | Removing an element from the middle of a `count`-indexed list causes all subsequent instances to shift indices and be replaced | Hard |
| 11 | B | N/A | Circular dependencies (cycles) in the resource graph cause Terraform to error; resolution requires restructuring references or using `data` sources | Hard |
| 12 | A, C | N/A | Data sources depending on newly created resources are deferred to apply phase; plan output shows `(known after apply)` for data source results | Hard |
| 13 | B | N/A | The `provider` meta-argument on a resource selects an aliased provider configuration for that specific resource | Easy |
