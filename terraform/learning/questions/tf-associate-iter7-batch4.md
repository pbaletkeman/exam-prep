# Terraform Associate (004) — Question Bank Iter 7 Batch 4

**Iteration**: 7
**Iteration Style**: Fill-in-the-blank / complete the HCL — given a partial configuration or partial statement, select the term or argument that correctly fills the blank
**Batch**: 4
**Objective**: 4 — Resources, Data & Dependencies (prompt05 + prompt09)
**Generated**: 2026-04-25
**Total Questions**: 13
**Difficulty Split**: 3 Easy / 8 Medium / 2 Hard
**Answer Types**: 10 `one` / 3 `many` / 0 `none`

---

## Questions

---

### Question 1 — `ignore_changes` Prevents Drift Detection

**Difficulty**: Easy
**Answer Type**: one
**Topic**: The ignore_changes lifecycle argument tells Terraform to ignore drift for listed attributes — useful when a resource auto-manages its own tags or other fields outside Terraform

**Question**:
An Auto Scaling Group updates its `desired_capacity` attribute at runtime based on scaling policies. Every time `terraform plan` runs, Terraform detects this as drift and wants to revert the value. Complete the `lifecycle` block to tell Terraform to stop detecting drift on `desired_capacity`:

```hcl
resource "aws_autoscaling_group" "web" {
  min_size         = 1
  max_size         = 10
  desired_capacity = 3

  lifecycle {
    ___________ = [desired_capacity]
  }
}
```

What lifecycle argument fills the blank?

- A) `skip_changes`
- B) `suppress_drift`
- C) `no_update`
- D) **`ignore_changes`**

**Answer**: D

**Explanation**:
`ignore_changes` is a `lifecycle` meta-argument that accepts a list of attribute names (without quotes). When attributes are listed in `ignore_changes`, Terraform does not include them in its drift detection during plan — changes to those attributes in the real infrastructure are silently ignored rather than flagged as configuration drift. This is essential for resources like Auto Scaling Groups (`desired_capacity`), instances managed by spot schedulers (`instance_type`), or resources whose tags are modified by external tooling (`tags["LastModified"]`). `skip_changes`, `suppress_drift`, and `no_update` are not valid lifecycle arguments.

---

### Question 2 — TWO Correct Statements About the `moved` Block

**Difficulty**: Easy
**Answer Type**: many
**Topic**: The moved block records a state rename or relocation — it allows resources to be renamed or moved into modules without destroy and recreate

**Question**:
Which TWO of the following statements about the `moved` block are correct? (Select two.)

- A) **A `moved` block renames a resource in Terraform state — mapping the old address (`from`) to the new address (`to`) so that Terraform treats the existing cloud object as the resource at the new address, avoiding a destroy-and-recreate cycle**
- B) After a `moved` block is applied, it must remain in the configuration permanently — removing it causes Terraform to destroy the resource on the next apply
- C) **A `moved` block can also relocate a resource from the root module into a child module by setting `from = aws_instance.web` and `to = module.web_tier.aws_instance.server` — Terraform updates the state address without touching the cloud resource**
- D) The `moved` block requires running `terraform state mv` first before the block takes effect — it is a documentation-only declaration

**Answer**: A, C

**Explanation**:
**(A)** The `moved` block maps an old resource address (`from`) to a new address (`to`) in state. When Terraform processes a `moved` block during apply, it updates the state entry to use the new address — no destroy or create API calls are made. **(C)** `moved` also handles cross-module relocations: setting `from = aws_instance.web` and `to = module.web_tier.aws_instance.server` moves the state entry into the module's address namespace, reflecting the new code structure. **(B)** is false — after a successful apply that processes the `moved` block, the block can be safely removed from configuration; the resource is now tracked under its new address. **(D)** is false — `moved` is a live Terraform directive, not documentation-only; it does not require a separate `terraform state mv` command.

---

### Question 3 — Default Parallelism Value

**Difficulty**: Easy
**Answer Type**: one
**Topic**: Terraform's default concurrent operations limit is 10 — controllable with -parallelism

**Question**:
Complete the following statement about Terraform's execution model:

> "Terraform applies operations in parallel for resources with no dependencies. By default, Terraform runs up to ___________ concurrent operations at a time. This can be adjusted with the `-parallelism=<n>` flag on `terraform plan` or `terraform apply`."

What number fills the blank?

- A) 1
- B) 5
- C) 20
- D) **10**

**Answer**: D

**Explanation**:
Terraform's default parallelism limit is **10** — it will run at most 10 concurrent provider API calls (creates, updates, reads, destroys) at the same time for resources that have no dependency relationship. This value can be overridden: `terraform apply -parallelism=20` increases throughput for large configurations, while `terraform apply -parallelism=1` forces sequential execution (useful for debugging or for providers with strict rate limits). The dependency graph determines which operations *can* run in parallel — parallelism caps how many of those eligible operations execute simultaneously.

---

### Question 4 — `replace_triggered_by` Forces Replacement on Dependency Change

**Difficulty**: Medium
**Answer Type**: one
**Topic**: The replace_triggered_by lifecycle argument forces the resource to be replaced whenever a referenced resource or attribute changes — useful for propagating changes through indirectly linked resources like ASG and launch template

**Question**:
A `aws_autoscaling_group` resource depends on a `aws_launch_template`. When the launch template changes, Terraform updates the template but the existing ASG instances do not cycle through the new template unless the ASG itself is replaced. Complete the `lifecycle` block to force the ASG to be replaced whenever the launch template changes:

```hcl
resource "aws_autoscaling_group" "web" {
  min_size = 2
  max_size = 10

  launch_template {
    id      = aws_launch_template.web.id
    version = "$Latest"
  }

  lifecycle {
    ___________ = [aws_launch_template.web]
  }
}
```

What lifecycle argument fills the blank?

- A) `force_replace_on`
- B) `triggers`
- C) `recreate_when`
- D) **`replace_triggered_by`**

**Answer**: D

**Explanation**:
`replace_triggered_by` accepts a list of resource references (or specific resource attribute references). Whenever any of the listed resources change — even if the change doesn't affect an attribute that the current resource directly reads — Terraform plans a `-/+` (replace) operation for the resource. This is the correct way to propagate launch template changes through to an Auto Scaling Group: when the launch template is updated, `replace_triggered_by = [aws_launch_template.web]` ensures the ASG is also replaced, causing instances to be cycled with the new template configuration. `force_replace_on`, `triggers`, and `recreate_when` are not valid lifecycle arguments.

---

### Question 5 — `ignore_changes = all`

**Difficulty**: Medium
**Answer Type**: one
**Topic**: ignore_changes = all tells Terraform to ignore ALL attribute drift for a resource — the resource is created once and never updated by Terraform thereafter

**Question**:
A team manages an EC2 instance that is heavily customised by an external configuration management tool after Terraform creates it. Every `terraform plan` detects multiple drift items. The team wants Terraform to create the instance once and then ignore all future drift permanently. Complete the `lifecycle` block:

```hcl
resource "aws_instance" "managed_externally" {
  ami           = data.aws_ami.ubuntu.id
  instance_type = "t3.medium"

  lifecycle {
    ignore_changes = ___________
  }
}
```

What value fills the blank?

- A) `["*"]`
- B) `[all]`
- C) `"all"`
- D) **`all`**

**Answer**: D

**Explanation**:
`ignore_changes = all` (without quotes, without brackets) is the special keyword form that tells Terraform to ignore drift on every attribute of the resource. After the resource is initially created, Terraform will never plan an update to it regardless of how much its real-world state diverges from the configuration — it is effectively "create-only" from Terraform's perspective. This is appropriate for resources fully managed by an external system after initial provisioning. The value `all` is a keyword, not a string literal — it must not be wrapped in quotes or brackets. `["*"]`, `[all]` (in brackets), and `"all"` (in quotes) are all invalid forms.

---

### Question 6 — `removed` Block with `destroy = false`

**Difficulty**: Medium
**Answer Type**: one
**Topic**: The removed block with destroy = false stops Terraform from tracking a resource without destroying the underlying cloud object

**Question**:
A team wants to stop managing an EC2 instance with Terraform — the instance should continue running in AWS, but Terraform should no longer track or manage it. Complete the `removed` block:

```hcl
removed {
  from = aws_instance.legacy_server

  lifecycle {
    destroy = ___________
  }
}
```

What value fills the blank?

- A) `true`
- B) `null`
- C) `"retain"`
- D) **`false`**

**Answer**: D

**Explanation**:
The `removed` block (introduced in Terraform 1.7) removes a resource from Terraform's state management. When `destroy = false`, Terraform removes the resource from the state file during the next apply but does **not** call the provider's Destroy API — the cloud object continues to exist and run independently. When `destroy = true`, Terraform removes the resource from state AND destroys the cloud object (equivalent to a normal removal of the resource block). The `removed` block requires specifying the `from` address of the resource being de-adopted. After apply, the `removed` block itself can be deleted from configuration. `null`, `"retain"`, and any other values are not valid for `destroy`.

---

### Question 7 — Data Sources Read During `apply` for Computed Values

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Data sources are normally evaluated during plan — but if their arguments depend on values that are not known until apply (computed values), they are deferred and read during the apply phase instead

**Question**:
Complete the following statement about when Terraform evaluates data sources:

> "A data source is usually read during the **plan** phase. However, if any of the data source's filter arguments depend on a value that is not yet known at plan time — such as the `id` of a resource that has not yet been created — Terraform defers reading the data source until the ___________ phase, when that value becomes available."

What word fills the blank?

- A) `init`
- B) `validate`
- C) `refresh`
- D) **`apply`**

**Answer**: D

**Explanation**:
Terraform evaluates data sources during the **plan** phase so that the plan output can show the full effect of all changes. However, if a data source's filter argument references a value that won't exist until a resource is created — for example, `id = aws_vpc.main.id` where `aws_vpc.main` is being created in the same apply — that value is "unknown" at plan time. In this case, Terraform defers the data source read until the **apply** phase, after the upstream resource is created and its `id` is known. The plan will show the data source result as "known after apply" rather than displaying the actual queried values.

---

### Question 8 — Aliased Provider Reference Syntax

**Difficulty**: Medium
**Answer Type**: one
**Topic**: When a provider has an alias, a resource references it with the provider meta-argument using the syntax provider = <provider_name>.<alias>

**Question**:
A configuration declares two AWS provider configurations — a default (us-east-1) and an aliased one for us-west-2:

```hcl
provider "aws" {
  region = "us-east-1"
}

provider "aws" {
  alias  = "west"
  region = "us-west-2"
}
```

Complete the resource block so the EC2 instance is created in us-west-2:

```hcl
resource "aws_instance" "west_server" {
  ___________ = aws.west
  ami           = "ami-0abc123"
  instance_type = "t3.micro"
}
```

What meta-argument fills the blank?

- A) `region`
- B) `alias`
- C) `configuration`
- D) **`provider`**

**Answer**: D

**Explanation**:
The `provider` meta-argument on a resource block specifies which provider configuration the resource should use. When a provider has an alias, the syntax is `provider = <provider_name>.<alias>` — in this case `provider = aws.west`. Without this meta-argument, a resource automatically uses the default (non-aliased) provider configuration for its type. The `provider` meta-argument value uses dot notation but does **not** use quotes — `aws.west` is a provider reference expression, not a string. `region`, `alias`, and `configuration` are not valid meta-argument names on a resource block.

---

### Question 9 — TWO Consequences of Frequent `-target` Usage

**Difficulty**: Medium
**Answer Type**: many
**Topic**: Using -target for partial applies is convenient but should be used sparingly — it can cause state drift and leaves other resources out of sync

**Question**:
Which TWO of the following accurately describe a consequence or risk of using `terraform apply -target=<resource>` frequently? (Select two.)

- A) **State drift — resources not included in the `-target` scope are not refreshed or updated, so the state file may become inconsistent with the real infrastructure over time**
- B) `-target` permanently marks the targeted resource as "priority" in the state file — subsequent applies without `-target` will always process that resource first
- C) **Dependency chain gaps — if the targeted resource depends on other resources that also have pending changes, those dependencies may not be applied, leaving the configuration partially reconciled**
- D) Using `-target` disables all provider authentication — the apply runs in offline mode and only modifies the state file, not the real cloud infrastructure

**Answer**: A, C

**Explanation**:
**(A)** When `-target` scopes an apply to a subset of resources, all other resources in the configuration are skipped — they are not refreshed, updated, or validated. Over time this creates state drift: the state file may no longer accurately reflect the real state of non-targeted resources. **(C)** Even within the targeted resource's dependency chain, `-target` has a defined but narrow scope — it includes direct dependencies of the targeted resource but may miss transitive or sibling dependencies that also have pending changes. This can leave the overall configuration in a partially reconciled state where some dependent resources have changes that haven't been applied. Terraform itself warns: "Note: Objects have changed outside of Terraform" and recommends using `-target` only for exceptional situations. **(B)** is false — `-target` is a one-time flag with no persistent effect on the state file's resource ordering. **(D)** is false — `-target` applies normally against real cloud infrastructure with full provider authentication.

---

### Question 10 — Destroy Order Is the Reverse of Creation Order

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Terraform builds a dependency graph for both creation and destruction — destroy operations execute in topological reverse order so that dependents are removed before their dependencies

**Question**:
Complete the following statement about Terraform's destroy ordering:

> "Terraform builds a Directed Acyclic Graph (DAG) for both creation and destruction. During a destroy operation, the order is the ___________ of creation order — resources that depend on others are destroyed first, and the resources they depend on are destroyed last."

What word fills the blank?

- A) `duplicate`
- B) `parallel`
- C) `extension`
- D) **`reverse`**

**Answer**: D

**Explanation**:
Terraform's dependency graph drives both creation and destruction ordering, but in opposite directions. During creation, Terraform follows topological order: dependencies are created first (e.g., VPC → subnet → EC2 instance). During destruction, the order is **reversed**: dependents must be removed before the resources they depend on, so the EC2 instance is destroyed first, then the subnet, then the VPC. Attempting to destroy a resource that another resource still references would cause a provider API error (e.g., trying to delete a VPC that still has subnets). The reversed destroy order prevents these dependency violations automatically.

---

### Question 11 — `depends_on` for IAM Policy Attachment

**Difficulty**: Medium
**Answer Type**: one
**Topic**: depends_on is used when Terraform cannot detect a real dependency through attribute references — the most common case is IAM permissions that must propagate before a resource can use them

**Question**:
An EC2 instance uses an IAM instance profile that grants S3 access. The IAM policy attachment does not provide any attribute that the EC2 instance references directly. However, the policy must be fully propagated before the instance starts. Complete the resource block:

```hcl
resource "aws_instance" "app" {
  ami                  = data.aws_ami.ubuntu.id
  instance_type        = "t3.micro"
  iam_instance_profile = aws_iam_instance_profile.app.name

  ___________ = [
    aws_iam_role_policy_attachment.s3_access
  ]
}
```

What meta-argument fills the blank?

- A) `requires`
- B) `after`
- C) `prerequisites`
- D) **`depends_on`**

**Answer**: D

**Explanation**:
`depends_on` is the meta-argument for declaring explicit dependencies that Terraform cannot infer from attribute references. In this case, the EC2 instance references `aws_iam_instance_profile.app.name` — but the instance profile's *attached policy* (`aws_iam_role_policy_attachment.s3_access`) has no attribute referenced by the instance. Without `depends_on`, Terraform might create the EC2 instance in parallel with or before the policy attachment, causing the instance to start before the IAM policy is active. The `depends_on` value is a list of resource references (not strings) — they must be bare references like `aws_iam_role_policy_attachment.s3_access`, not quoted names. `depends_on` should be used sparingly because it reduces Terraform's ability to parallelise operations.

---

### Question 12 — Resource Address Format from Root Module

**Difficulty**: Hard
**Answer Type**: one
**Topic**: When referencing a managed resource from the root module context, the full address includes the module prefix: module.<module_name>.<resource_type>.<resource_name>

**Question**:
A root configuration calls a child module named `web_tier`, which internally declares `resource "aws_instance" "server"`. Complete the full resource address used to reference this instance from the root module — for example, when using `-target` or reading from state output:

```
module.___________.aws_instance.server
```

What label fills the blank to correctly address the resource inside a module called `web_tier`?

- A) `root`
- B) `aws_instance`
- C) `server`
- D) **`web_tier`**

**Answer**: D

**Explanation**:
The full resource address for a managed resource declared inside a child module follows the pattern `module.<MODULE_LABEL>.<RESOURCE_TYPE>.<RESOURCE_NAME>`. The `<MODULE_LABEL>` is the local name given to the module in the calling configuration's `module` block — in this case `web_tier` from `module "web_tier" { ... }`. The complete address is `module.web_tier.aws_instance.server`. This address format is used in `terraform state` commands, `-target` flags, `moved` blocks, and `removed` blocks. Within the child module itself, the resource is addressed as simply `aws_instance.server` — the `module.web_tier.` prefix is only needed from outside the module.

---

### Question 13 — TWO Collection Types Usable Directly with `for_each`

**Difficulty**: Hard
**Answer Type**: many
**Topic**: for_each accepts only map or set(string) values directly — a list(string) must be converted with toset() first; tuples and other collection types are not supported

**Question**:
Which TWO collection types can be passed directly to the `for_each` meta-argument **without any conversion function**? (Select two.)

- A) `list(string)` — e.g., `for_each = ["us-east-1", "us-west-2"]`
- B) **`set(string)` — e.g., `for_each = toset(["us-east-1", "us-west-2"])` where the argument's type is a set; also accepted when the variable is already declared as `set(string)`**
- C) **`map(string)` — e.g., `for_each = { web = "t3.micro", db = "r5.large" }`; each.key = "web" or "db", each.value = the instance type string**
- D) `tuple` — e.g., `for_each = ["us-east-1", true, 80]`

**Answer**: B, C

**Explanation**:
`for_each` accepts exactly two collection types directly: **(B) `set(string)`** — a set of unique string values; each element becomes both the instance key and `each.key` (with `each.value` also equal to `each.key` for a set); and **(C) `map(any)`** — a map where each key becomes the instance address key, `each.key` is the map key, and `each.value` is the corresponding map value. **(A) `list(string)`** cannot be used directly — Terraform rejects it because lists have numeric indexes and allow duplicates, which would make instance addresses ambiguous. The fix is to wrap the list with `toset()`: `for_each = toset(var.regions)`. **(D) Tuples** are not supported by `for_each` at all — they are ordered collections with mixed types and cannot be iterated with stable string keys.

---
