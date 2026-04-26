# Terraform Associate Exam Questions

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

## Answer Key

| Q# | Answer(s) | Explanation | Source | Difficulty |
|----|-----------|-----------:|--------|------------|
| 1 | D | N/A | The ignore_changes lifecycle argument tells Terraform to ignore drift for listed attributes — useful when a resource auto-manages its own tags or other fields outside Terraform | Easy |
| 2 | A, C | N/A | The moved block records a state rename or relocation — it allows resources to be renamed or moved into modules without destroy and recreate | Easy |
| 3 | D | N/A | Terraform's default concurrent operations limit is 10 — controllable with -parallelism | Easy |
| 4 | D | N/A | The replace_triggered_by lifecycle argument forces the resource to be replaced whenever a referenced resource or attribute changes — useful for propagating changes through indirectly linked resources like ASG and launch template | Medium |
| 5 | D | N/A | ignore_changes = all tells Terraform to ignore ALL attribute drift for a resource — the resource is created once and never updated by Terraform thereafter | Medium |
| 6 | D | N/A | The removed block with destroy = false stops Terraform from tracking a resource without destroying the underlying cloud object | Medium |
| 7 | D | N/A | Data sources are normally evaluated during plan — but if their arguments depend on values that are not known until apply (computed values), they are deferred and read during the apply phase instead | Medium |
| 8 | D | N/A | When a provider has an alias, a resource references it with the provider meta-argument using the syntax provider = <provider_name>.<alias> | Medium |
| 9 | A, C | N/A | Using -target for partial applies is convenient but should be used sparingly — it can cause state drift and leaves other resources out of sync | Medium |
| 10 | D | N/A | Terraform builds a dependency graph for both creation and destruction — destroy operations execute in topological reverse order so that dependents are removed before their dependencies | Medium |
| 11 | D | N/A | depends_on is used when Terraform cannot detect a real dependency through attribute references — the most common case is IAM permissions that must propagate before a resource can use them | Medium |
| 12 | D | N/A | When referencing a managed resource from the root module context, the full address includes the module prefix: module.<module_name>.<resource_type>.<resource_name> | Hard |
| 13 | B, C | N/A | for_each accepts only map or set(string) values directly — a list(string) must be converted with toset() first; tuples and other collection types are not supported | Hard |
