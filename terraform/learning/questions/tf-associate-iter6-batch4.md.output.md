# Terraform Associate Exam Questions

---

### Question 1 — Subnet Created Before VPC

**Difficulty**: Easy
**Answer Type**: one
**Topic**: Understanding that implicit dependency from attribute reference controls creation order

**Question**:
An engineer writes a Terraform configuration with an `aws_vpc` and an `aws_subnet`. They expect Terraform to create the subnet first because it is declared first in the file. Instead, Terraform creates the VPC first. The engineer asks why. What is the correct explanation?

- A) Terraform creates resources in alphabetical order by resource type — `aws_subnet` comes before `aws_vpc` alphabetically, but Terraform uses the reverse alphabetical order as a safety measure
- B) Terraform creates resources in the order they are declared in configuration files — the VPC being created first means it must have been declared first
- C) Terraform infers creation order from the **dependency graph, not file declaration order** — because the subnet's `vpc_id` argument references `aws_vpc.main.id`, Terraform detects an implicit dependency and ensures the VPC is created before the subnet; file order is irrelevant to execution order
- D) The VPC is created first only because it uses the default provider; resources using aliased providers are always created last

---

### Question 2 — Data Source Returns Stale AMI

**Difficulty**: Easy
**Answer Type**: one
**Topic**: Understanding when data sources are evaluated and how to force a refresh

**Question**:
An engineer uses a data source to look up the latest Ubuntu AMI and passes it to an EC2 instance. Six months later, a new Ubuntu AMI is released. The engineer runs `terraform apply` but the EC2 instance is not updated — it still uses the old AMI. The engineer assumes the data source is refreshing automatically. What explains this behaviour?

- A) Data sources are evaluated only during `terraform init` — after initialisation, the result is cached permanently
- B) The data source is re-evaluated on every `terraform plan` and `terraform apply`; if the AMI has changed, Terraform will detect the new value and plan a replacement for the EC2 instance automatically
- C) Data sources **are** re-evaluated on each plan, but changing the AMI ID returned by the data source does not automatically cause the EC2 instance to be replaced unless the resource has a `ForceNew` constraint on `ami` — and `aws_instance.ami` is indeed `ForceNew`; if the plan shows no changes, the most likely explanation is that the data source filter is still returning the same AMI (e.g., the `most_recent = true` filter resolved to the same ID), not that the data source is stale; the engineer should verify by running `terraform plan` and examining the data source result
- D) Data sources cache their results in `.terraform/` for 30 days to avoid repeated API calls during planning

---

### Question 3 — `prevent_destroy` Blocks Teardown Pipeline

**Difficulty**: Easy
**Answer Type**: one
**Topic**: Understanding that prevent_destroy causes terraform apply/destroy to error and how to override it

**Question**:
A team has `lifecycle { prevent_destroy = true }` on their production RDS instance. When a junior engineer runs `terraform destroy` on the environment teardown pipeline, it fails with: `Error: Instance cannot be destroyed`. The engineer asks: "How do we destroy this resource when we're ready to decommission the environment?" What is the correct answer?

- A) Run `terraform destroy -force` — this flag overrides `prevent_destroy` for a single destroy operation
- B) The only way to destroy a `prevent_destroy`-protected resource is to use the AWS console directly
- C) `prevent_destroy = true` is a **configuration-level guard** — to destroy the resource, the engineer must **remove or change the `prevent_destroy` setting** in the configuration file and then run `terraform apply` (or `terraform destroy`) again; there is no runtime flag to override it; this is by design — the guard forces a deliberate code change before destruction can proceed
- D) Set `TF_PREVENT_DESTROY=false` in the environment before running `terraform destroy`

---

### Question 4 — Two Resources Created in Wrong Order Despite `depends_on`

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Diagnosing why depends_on alone on a data source may not be enough to control ordering with IAM

**Question**:
An engineer creates an EC2 instance with an IAM instance profile. The instance starts but immediately fails because the attached IAM role does not yet have the S3 read policy attached — the policy attachment resource is not complete by the time the instance boots and attempts to use it. The engineer added `aws_instance.app` to depend on `aws_iam_role.app`, but forgot to include the policy resource in `depends_on`. What is the most precise diagnosis and fix?

- A) IAM propagation is always instant — the instance failure is caused by a misconfigured security group blocking S3 access, not a missing dependency
- B) The implicit dependency on `aws_iam_role.app` ensures the role exists before the instance, but does not guarantee the **policy attachment** (`aws_iam_role_policy` or `aws_iam_role_policy_attachment`) is complete; the engineer must add the policy attachment resource to the `depends_on` list on `aws_instance.app` so Terraform waits for the policy to be attached before creating the instance
- C) Adding any `depends_on` entry to a resource causes Terraform to serialize all subsequent resource creations — the issue must be something else
- D) `depends_on` cannot reference `aws_iam_role_policy` resources — it only accepts module references

---

### Question 5 — `count` Removal Causes Unexpected Destroy+Create

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Understanding that removing a count item by index causes all subsequent instances to shift and be replaced

**Question**:
An engineer uses `count = 3` to create three S3 buckets, named `bucket-0`, `bucket-1`, and `bucket-2`. They later need to remove `bucket-1`. They remove element 1 from the list and set `count = 2`. On running `terraform plan`, they see that `bucket-1` will be destroyed and `bucket-2` will also be destroyed and recreated as a different bucket. Why does `bucket-2` get recreated?

- A) `count` always destroys and recreates all instances when the count value is reduced
- B) Removing element 1 from the list **shifts the index of the remaining elements** — what was index 2 (`bucket-2`) becomes index 1 (`bucket-1`) in the new count; Terraform sees `aws_s3_bucket.this[1]` as a different instance in state vs the new configuration, triggering a destroy+create; this index-shifting problem is why `for_each` with stable string keys is preferred over `count` when the set of instances may change
- C) S3 bucket names are globally unique — Terraform must destroy all buckets with sequential names when any one is removed
- D) This only happens when `count` is reduced from 3 to 2 — reducing to 1 or 0 would not trigger the shift

---

### Question 6 — `ignore_changes` Not Preventing Drift Detection

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Understanding the correct syntax for ignore_changes and common mistakes

**Question**:
An engineer uses Auto Scaling Groups and wants Terraform to ignore the `desired_capacity` attribute (which the ASG manages automatically). They add this lifecycle block:

```hcl
lifecycle {
  ignore_changes = "desired_capacity"
}
```

On the next `terraform plan`, Terraform still shows a change to `desired_capacity`. What is the error?

- A) `desired_capacity` cannot be ignored — it is a required attribute that Terraform always manages
- B) `ignore_changes` is only available in Terraform Enterprise — the community edition always manages all attributes
- C) The **`ignore_changes` argument requires a list value**, not a bare string — the correct syntax is `ignore_changes = [desired_capacity]` (square brackets, no quotes around the attribute name); using a string instead of a list causes Terraform to silently ignore the argument or return a validation error, leaving the attribute tracked normally
- D) The engineer must also add `create_before_destroy = true` alongside `ignore_changes` for the latter to take effect

---

### Question 7 — `for_each` Fails on a `list(string)`

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Understanding that for_each does not accept a plain list and requires a set or map

**Question**:
An engineer writes:

```hcl
variable "bucket_names" {
  type    = list(string)
  default = ["logs", "backups", "assets"]
}

resource "aws_s3_bucket" "this" {
  for_each = var.bucket_names
  bucket   = each.key
}
```

`terraform plan` returns an error: `The given "for_each" argument value is unsuitable: must be a map, or set of strings, and you have provided a value of type list of string`. What is the fix?

- A) Change `for_each = var.bucket_names` to `for_each = count(var.bucket_names)` — `for_each` requires a count value, not the list directly
- B) `for_each` does not support string resources — it only works with numeric types; use `count = length(var.bucket_names)` instead
- C) Wrap the list in the `toset()` function: `for_each = toset(var.bucket_names)` — `for_each` requires a `set(string)` or `map`; `toset()` converts a `list(string)` to a `set(string)` by deduplicating values and removing ordering; after this conversion, `each.key` and `each.value` will both hold the bucket name for each iteration
- D) Change the variable type to `set(string)` in the variable declaration and leave `for_each` as-is — `for_each` accepts sets only from variable declarations, not inline values

---

### Question 8 — Resource Recreated Every Apply Due to `replace_triggered_by`

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Diagnosing unintended constant replacement caused by replace_triggered_by referencing a frequently changing resource

**Question**:
An engineer adds `replace_triggered_by = [aws_launch_template.web]` to an Auto Scaling Group resource to ensure the ASG is recycled when the launch template changes. After deploying, the ASG is replaced on every `terraform apply` — even when nothing has changed. What is the most likely cause?

- A) `replace_triggered_by` always forces a replacement on every apply — this is the expected behaviour
- B) The `aws_launch_template.web` resource itself has **`create_before_destroy = true`**, causing it to be replaced on every apply, which then triggers the ASG replacement through `replace_triggered_by`; the fix is to remove `create_before_destroy` from the launch template
- C) The `aws_launch_template.web` resource **has an attribute that changes on every apply** — for example, if the launch template has `latest_version` or similar computed attribute that increments on each apply even with no configuration changes, `replace_triggered_by` detects this as a change and triggers ASG replacement; the engineer should scope `replace_triggered_by` to a specific stable attribute rather than the entire resource, or investigate why the launch template resource reports changes on every apply
- D) `replace_triggered_by` is incompatible with Auto Scaling Groups — it should only be used with stateless resources like EC2 instances

---

### Question 9 — `removed` Block Destroys Resource Unexpectedly

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Understanding that removed block destroy=false is needed to stop managing without destroying

**Question**:
An engineer wants to stop managing an EC2 instance with Terraform without deleting it from AWS. They have heard about the `removed` block (Terraform 1.7+) and add it to their configuration. On the next `terraform apply`, the instance is deleted. What did the engineer most likely forget?

- A) The `removed` block always stops Terraform from managing a resource without any cloud-side effect — the instance deletion must have been triggered by something else
- B) The engineer forgot to run `terraform state rm` before using the `removed` block — the two must be used together
- C) The `removed` block has a **`lifecycle { destroy = false }` sub-block** that must be explicitly set — without it, the default behaviour of `removed` is to **destroy** the resource and remove it from state; setting `destroy = false` tells Terraform to stop tracking the resource but leave it running in the cloud; the engineer forgot this sub-block and got the default destroy behaviour
- D) `removed` blocks are only supported in HCP Terraform — in the open-source CLI, they always destroy the resource

---

### Question 10 — Two Scenarios Where `depends_on` Is Required

**Difficulty**: Medium
**Answer Type**: many
**Topic**: Identifying TWO scenarios where implicit dependency detection is insufficient and depends_on is needed

**Question**:
Which TWO of the following scenarios require `depends_on` because Terraform cannot detect the dependency through attribute references alone? (Select two.)

- A) An EC2 instance references `aws_subnet.public.id` in its `subnet_id` argument — Terraform must be told explicitly via `depends_on` that the instance depends on the subnet
- B) An EC2 instance uses an IAM instance profile, and the instance's startup script reads from an S3 bucket that the attached IAM role must have permission to access — the policy attachment has no attribute referenced by the instance, so Terraform has no way to detect the dependency automatically
- C) A `null_resource` with a `local-exec` provisioner runs a script that calls an API exposed by an `aws_api_gateway_rest_api` resource — no attribute of the API gateway is referenced in the `null_resource` block, so `depends_on` is needed to ensure the API is deployed before the script runs
- D) An `aws_db_instance` is referenced by its endpoint in an `aws_instance` user_data script using string interpolation — Terraform must be told via `depends_on` that the instance depends on the database

---

### Question 11 — Circular Dependency Error

**Difficulty**: Hard
**Answer Type**: one
**Topic**: Diagnosing a cycle in the dependency graph and knowing how to resolve it

**Question**:
An engineer receives the error: `Error: Cycle: aws_security_group.app, aws_instance.web`. Their configuration has `aws_instance.web` referencing `aws_security_group.app.id` in its `vpc_security_group_ids`, and `aws_security_group.app` referencing `aws_instance.web.private_ip` in an ingress rule. What explains the error and how should it be resolved?

- A) The error means both resources have `prevent_destroy = true` — removing those lifecycle blocks will resolve the cycle
- B) A **dependency cycle** exists: `aws_instance.web` depends on `aws_security_group.app` (for the security group ID), and simultaneously `aws_security_group.app` depends on `aws_instance.web` (for the private IP in the ingress rule); Terraform's DAG cannot resolve circular dependencies and errors immediately; the resolution is to break the cycle — for example, remove the private IP reference from the security group ingress rule and use a CIDR block instead, or restructure the ingress rule to reference a different stable value
- C) Cycles are resolved automatically on `terraform apply` — the error only appears during `terraform plan` and can be ignored
- D) The cycle is caused by both resources being in the same `.tf` file — moving one to a separate file resolves the dependency conflict

---

### Question 12 — `moved` Block Applied But Resource Still Recreated

**Difficulty**: Hard
**Answer Type**: one
**Topic**: Diagnosing why a moved block did not prevent destroy+create — common mistakes in moved block syntax

**Question**:
An engineer renames `resource "aws_instance" "web"` to `resource "aws_instance" "web_server"` and adds:

```hcl
moved {
  from = "aws_instance.web"
  to   = "aws_instance.web_server"
}
```

Running `terraform plan` still shows `1 to destroy, 1 to add`. What is the error in the `moved` block?

- A) The `moved` block is in the wrong file — it must be in `main.tf` and cannot be in any other `.tf` file
- B) The `moved` block requires a `provider` argument to be specified alongside the `from` and `to` addresses
- C) The **`from` and `to` values in a `moved` block must be bare references, not quoted strings** — the correct syntax is `from = aws_instance.web` and `to = aws_instance.web_server` (without quotes); using quoted strings causes Terraform to treat the values as string literals rather than resource address references, which fails validation or is ignored; without a valid `moved` block, Terraform does not know about the rename and plans a destroy+create as it would without any `moved` block
- D) `moved` blocks can only be used when the resource is being moved between modules — renaming within the same module requires `terraform state mv` instead

---

### Question 13 — `data` Source Reads Stale Value During Apply

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Understanding the known-after-apply problem for data sources that depend on resources being created in the same apply

**Question**:
An engineer creates an `aws_security_group` resource and a `data "aws_security_group"` data source that filters by the security group's name in the same Terraform configuration. They expect the data source to return the newly created security group. During `terraform plan`, the data source shows `(known after apply)` instead of the security group's attributes. The engineer asks why. What is the correct explanation?

- A) Data sources can never reference resources created in the same Terraform configuration — they are always evaluated before any resources are created
- B) The data source must use the resource's `id` attribute, not the `name` filter — `name`-based filters only work against pre-existing resources
- C) The data source **depends on the security group being created**, but during `terraform plan` the security group does not exist yet (it will be created on apply); Terraform detects this dependency and defers the data source read until `terraform apply`, when the security group will exist — this is the "known after apply" behaviour; the attributes are shown as `(known after apply)` in the plan; after apply completes, the data source will have been read and its attributes will be available; the preferred alternative is to reference the resource's attributes directly (`aws_security_group.app.id`) rather than re-querying via a data source for a resource Terraform itself is creating
- D) The `(known after apply)` message means the data source is misconfigured — it cannot be used in the same configuration as a resource of the same type

## Answer Key

| Q# | Answer(s) | Explanation | Source | Difficulty |
|----|-----------|-----------:|--------|------------|
| 1 | C | N/A | Understanding that implicit dependency from attribute reference controls creation order | Easy |
| 2 | C | N/A | Understanding when data sources are evaluated and how to force a refresh | Easy |
| 3 | C | N/A | Understanding that prevent_destroy causes terraform apply/destroy to error and how to override it | Easy |
| 4 | B | N/A | Diagnosing why depends_on alone on a data source may not be enough to control ordering with IAM | Medium |
| 5 | B | N/A | Understanding that removing a count item by index causes all subsequent instances to shift and be replaced | Medium |
| 6 | C | N/A | Understanding the correct syntax for ignore_changes and common mistakes | Medium |
| 7 | C | N/A | Understanding that for_each does not accept a plain list and requires a set or map | Medium |
| 8 | C | N/A | Diagnosing unintended constant replacement caused by replace_triggered_by referencing a frequently changing resource | Medium |
| 9 | C | N/A | Understanding that removed block destroy=false is needed to stop managing without destroying | Medium |
| 10 | B, C | N/A | Identifying TWO scenarios where implicit dependency detection is insufficient and depends_on is needed | Medium |
| 11 | B | N/A | Diagnosing a cycle in the dependency graph and knowing how to resolve it | Hard |
| 12 | C | N/A | Diagnosing why a moved block did not prevent destroy+create — common mistakes in moved block syntax | Hard |
| 13 | C | N/A | Understanding the known-after-apply problem for data sources that depend on resources being created in the same apply | Medium |
