# Terraform Associate Exam Questions

---

### Question 1 — `data` Block Claimed to Create Resources

**Difficulty**: Easy
**Answer Type**: one
**Topic**: Identifying the error in claiming a `data` block provisions infrastructure

**Question**:
A developer comments on a pull request:

> "Adding `data "aws_vpc" "existing" { id = "vpc-0abc12345" }` to my configuration will look up the VPC **and** add it to the Terraform state file as a managed resource — just like a `resource` block would, except Terraform won't destroy it on `terraform destroy`."

What is the error in this comment?

- A) There is no error — a `data` block creates a resource just like a `resource` block, but with destroy protection
- B) The error is that `data` blocks require a `provider` meta-argument to be explicitly set; without one, the lookup cannot succeed
- C) The error is that a `data` block **never creates or manages resources** — it performs a read-only query against the provider API to retrieve information about an already-existing object; no resource is provisioned and the result is not added to state as a managed resource
- D) The error is that `id` is not a valid filter argument inside a `data "aws_vpc"` block — VPCs must be looked up by `cidr_block`

---

### Question 2 — `create_before_destroy` Described as the Default Behaviour

**Difficulty**: Easy
**Answer Type**: one
**Topic**: Identifying the error in claiming Terraform's default replacement order is create-then-destroy

**Question**:
A team's onboarding guide states:

> "When Terraform replaces a resource — for example, because an immutable attribute was changed — it creates the new resource first and only destroys the old one after the replacement is ready. This create-before-destroy strategy is Terraform's default behaviour. You can disable it by setting `create_before_destroy = false` in the `lifecycle` block."

What is the error in this guide?

- A) There is no error — Terraform always creates the replacement before destroying the original
- B) The error is that `create_before_destroy = false` is not a valid value; the argument is boolean and only `true` is accepted
- C) The error is that **Terraform's default replacement order is destroy-first, then create** — the original resource is destroyed before the replacement is provisioned; `create_before_destroy = true` must be explicitly set in the `lifecycle` block to reverse this order and avoid downtime
- D) The error is that `create_before_destroy` applies to all resource operations, not just replacements — it affects creates and updates as well

---

### Question 3 — `count` and `for_each` Claimed Usable Together

**Difficulty**: Medium
**Answer Type**: many
**Topic**: Identifying TWO errors in claims about the `count` and `for_each` meta-arguments

**Question**:
A wiki article makes four claims about Terraform meta-arguments. Which TWO contain errors? (Select two.)

- A) "A resource block can use both `count` and `for_each` simultaneously — `count` controls how many copies exist while `for_each` provides a named key for each copy, allowing combined matrix-style resource creation"
- B) "With `count = 3`, the valid values of `count.index` are 0, 1, and 2 — indexing starts at zero, so the third instance has `count.index = 2`"
- C) "`for_each` accepts a plain `list(string)` value directly, without requiring any type conversion — Terraform iterates over the list elements natively"
- D) "When `for_each` is assigned a `map`, `each.key` holds the map key and `each.value` holds the corresponding map value for each iteration"

---

### Question 4 — Implicit Dependency Described as Requiring `depends_on`

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Identifying the error in claiming `depends_on` is required for attribute-reference dependencies

**Question**:
During a code review, an engineer comments:

> "This configuration has a bug — `aws_instance.web` sets `subnet_id = aws_subnet.public.id`, but there's no `depends_on = [aws_subnet.public]` in the instance block. Without an explicit `depends_on`, Terraform has no way to know the subnet must be created first and may attempt to create the instance before the subnet exists."

What is the error in this review comment?

- A) There is no error — `depends_on` is always required when one resource references another resource's attribute
- B) The error is that `depends_on` must reference the VPC, not the subnet — Terraform only traces dependencies one level deep
- C) The error is that **Terraform automatically detects implicit dependencies through attribute references** — because `aws_instance.web` uses `aws_subnet.public.id` as an argument value, Terraform infers that the subnet must be created first without any explicit `depends_on`; adding it here is unnecessary and reduces parallelism
- D) The error is that dependency ordering is only enforced during `terraform destroy`, not `terraform apply`

---

### Question 5 — `prevent_destroy` Claimed to Block `terraform state rm`

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Identifying the error in claiming `prevent_destroy` protects against `terraform state rm`

**Question**:
A senior engineer tells their team:

> "I've added `lifecycle { prevent_destroy = true }` to our production RDS instance. This is a complete safeguard — nobody can remove this resource from Terraform management through `terraform destroy`, a `terraform apply` that would replace it, **or** `terraform state rm`. It's the last line of defence against any accidental deletion."

What is the error in this claim?

- A) There is no error — `prevent_destroy = true` blocks all mechanisms that could remove the resource from Terraform management
- B) The error is that `prevent_destroy` does not block `terraform apply` replacements — it only prevents `terraform destroy`
- C) The error is that `prevent_destroy = true` **only prevents plan-time operations** that would destroy the resource (such as `terraform destroy` or config-driven replacements) — it does **not** protect against `terraform state rm`, which directly manipulates the state file and completely bypasses lifecycle hooks
- D) The error is that `prevent_destroy` requires a remote backend to function — it has no effect when state is stored locally

---

### Question 6 — `ignore_changes` Claimed to Hide Resource from `terraform plan`

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Identifying the error in claiming `ignore_changes = all` makes a resource invisible to plan

**Question**:
A team documents their use of `ignore_changes`:

> "We've applied `lifecycle { ignore_changes = all }` to our Auto Scaling Group. This makes the resource completely invisible to `terraform plan` — it won't appear in plan output at all, and Terraform treats it as unmanaged going forward."

What is the error in this documentation?

- A) There is no error — `ignore_changes = all` removes the resource from Terraform's awareness entirely
- B) The error is that `ignore_changes = all` is invalid syntax — the `all` keyword is not accepted; individual attribute names must be listed
- C) The error is that `ignore_changes = all` **does not hide the resource from plan or remove it from Terraform management** — Terraform still tracks the resource in state, still refreshes its current values, and still includes it in the plan; `ignore_changes = all` only means Terraform will not propose changes to update attribute values that have drifted, not that the resource is unmanaged
- D) The error is that `ignore_changes = all` must be combined with `prevent_destroy = true` to suppress all plan output for a resource

---

### Question 7 — `count.index` Starting Value Claimed as 1

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Identifying the error in a comment claiming `count.index` starts at 1

**Question**:
A developer adds this comment to their configuration:

```hcl
resource "aws_instance" "worker" {
  count         = 3
  ami           = "ami-0abc123"
  instance_type = "t3.micro"

  tags = {
    # count.index starts at 1 for the first instance
    Name = "worker-${count.index}"  # produces: "worker-1", "worker-2", "worker-3"
  }
}
```

What is the error in this comment?

- A) There is no error — `count.index` begins at 1, so with `count = 3` the tag values are `"worker-1"`, `"worker-2"`, and `"worker-3"`
- B) The error is that `count.index` cannot be used inside a `tags` block — it is only valid in top-level resource arguments such as `ami` or `instance_type`
- C) The error is that `count.index` **starts at 0**, not 1 — with `count = 3`, the three instances have `count.index` values of 0, 1, and 2, producing tag values `"worker-0"`, `"worker-1"`, and `"worker-2"`, not `"worker-1"`, `"worker-2"`, `"worker-3"`
- D) The error is that `count.index` returns a floating-point number by default and must be converted to a string with `tostring()` before use in string interpolation

---

### Question 8 — Wrong Claims About `depends_on` on a Data Source

**Difficulty**: Medium
**Answer Type**: many
**Topic**: Identifying TWO errors in claims about adding `depends_on` to a `data` block

**Question**:
A team wiki makes four claims about the following data source configuration:

```hcl
data "aws_s3_objects" "uploads" {
  bucket     = "my-app-uploads"
  depends_on = [aws_iam_role_policy.app_s3]
}
```

Which TWO claims contain errors? (Select two.)

- A) "Adding `depends_on` to a `data` block is invalid HCL syntax — only `resource` blocks support `depends_on`; using it inside a `data` block causes a validation error"
- B) "When `depends_on` is added to a data source, the data source read is deferred from the plan phase to the apply phase, even when no computed values are involved"
- C) "Adding `depends_on` to a data source with empty results will cause the data source to return `null` on every subsequent plan, permanently breaking the configuration"
- D) "`depends_on` on the data source ensures that `aws_iam_role_policy.app_s3` is fully created or updated before the data source queries the provider API"

---

### Question 9 — Resource `id` Attribute Claimed to Be User-Defined

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Identifying the error in claiming the `id` attribute of a managed resource can be set in HCL

**Question**:
A new team member asks how to reference the ID of `aws_instance.web`. A colleague responds:

> "Just add `id = "my-custom-instance-id"` to the `aws_instance.web` resource block in your HCL. Terraform will use that string as the resource's ID in both state and the cloud, and you can then reference it as `aws_instance.web.id` in other resources."

What is the error in this response?

- A) There is no error — the `id` argument can be set in any resource block to provide a stable identifier
- B) The error is that `id` can be set on `data` blocks but not on `resource` blocks
- C) The error is that the `id` attribute of a managed resource is a **read-only value assigned by the cloud provider** after the resource is created — it cannot be set in the resource block configuration; Terraform stores the provider-assigned ID in state, where it can be referenced as `aws_instance.web.id`
- D) The error is that `id` is a reserved keyword in Terraform HCL and will cause a parse error if used as an argument name in any block type

---

### Question 10 — `for_each` with a `list(string)` Variable

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Identifying the error in using a list-type variable directly with `for_each`

**Question**:
A developer writes the following configuration and claims it is valid:

```hcl
variable "regions" {
  type    = list(string)
  default = ["us-east-1", "us-west-2", "eu-west-1"]
}

resource "aws_s3_bucket" "regional" {
  for_each = var.regions
  bucket   = "data-${each.value}"
}
```

What is the error in this configuration?

- A) There is no error — `for_each` natively accepts a `list(string)` variable and iterates over its elements
- B) The error is that `var.regions` must be wrapped in `tomap()` before it can be used with `for_each`
- C) The error is that `for_each` **does not accept a `list` type** — it requires a `set(string)` or `map`; the correct fix is `for_each = toset(var.regions)` to convert the list to a set before iterating
- D) The error is that `each.value` is the wrong reference when iterating a variable — `each.key` must be used instead

---

### Question 11 — `depends_on` Claimed to Override Lifecycle Hooks

**Difficulty**: Hard
**Answer Type**: one
**Topic**: Identifying the error in claiming `depends_on` can override `prevent_destroy`

**Question**:
An engineer explains to a junior colleague:

> "The `depends_on` meta-argument doesn't just control creation order — it can also override lifecycle protections. If resource B has `depends_on = [resource_A]`, and resource A needs to be destroyed, Terraform will temporarily bypass `prevent_destroy = true` on resource B to satisfy the dependency chain. This is how Terraform handles cascading destroys."

What is the error in this explanation?

- A) There is no error — `depends_on` does override `prevent_destroy` when cascading destroy operations require it
- B) The error is that `depends_on` only affects destroy ordering — it has no effect on create ordering
- C) The error is that `depends_on` **controls execution ordering only** — it has no effect on lifecycle hooks whatsoever; `prevent_destroy = true` continues to block any plan that would destroy the protected resource regardless of `depends_on` relationships; lifecycle hooks and dependency ordering are entirely independent mechanisms in Terraform's execution model
- D) The error is that `depends_on` cannot reference resources in different modules — it is only valid between resources declared in the same configuration file

---

### Question 12 — Wrong Claims About the `removed` Block

**Difficulty**: Hard
**Answer Type**: many
**Topic**: Identifying TWO errors in claims about the `removed` block's behaviour

**Question**:
A Terraform 1.7+ runbook makes four claims about the `removed` block. Which TWO contain errors? (Select two.)

- A) "The `removed` block with `lifecycle { destroy = false }` stops Terraform from managing the resource but leaves the real cloud resource running and unaffected in the provider account"
- B) "A `removed` block with `lifecycle { destroy = false }` deletes both the Terraform state entry **and** the real cloud resource — the `destroy = false` setting only suppresses the interactive confirmation prompt before deletion"
- C) "After `terraform apply` successfully processes a `removed` block, the block must remain in the configuration permanently to prevent future `terraform plan` runs from flagging the resource address as unknown and attempting to recreate it"
- D) "After `terraform apply` processes a `removed` block, the block can be safely deleted from the configuration — subsequent plans will not attempt to recreate or re-manage the resource because it is no longer in state"

---

### Question 13 — `replace_triggered_by` Claimed to Work on Data Sources

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Identifying the error in claiming `replace_triggered_by` is valid in a `data` block's `lifecycle`

**Question**:
A developer proposes adding the following to a data source to ensure it re-reads when an IAM role changes:

```hcl
data "aws_iam_policy_document" "app" {
  statement {
    actions   = ["s3:GetObject"]
    resources = ["arn:aws:s3:::my-bucket/*"]
  }

  lifecycle {
    replace_triggered_by = [aws_iam_role.app]
  }
}
```

The developer claims: "`replace_triggered_by` in the `lifecycle` block will force this data source to be re-read whenever `aws_iam_role.app` changes."

What is the error in this configuration and claim?

- A) There is no error — `replace_triggered_by` is valid in the `lifecycle` block of both `resource` and `data` blocks
- B) The error is only in the reference syntax — `replace_triggered_by` inside a `data` block must use `data.` prefix references, not resource addresses
- C) The error is that `lifecycle` blocks — and all lifecycle meta-arguments including `replace_triggered_by` — are **not supported on `data` blocks**; lifecycle meta-arguments only apply to `resource` blocks; data sources are re-evaluated based on their argument values and dependency changes, not lifecycle hooks
- D) The error is that `replace_triggered_by` requires a list of attribute references (e.g., `aws_iam_role.app.arn`), not full resource addresses

## Answer Key

| Q# | Answer(s) | Explanation | Source | Difficulty |
|----|-----------|-----------:|--------|------------|
| 1 | C | N/A | Identifying the error in claiming a `data` block provisions infrastructure | Easy |
| 2 | C | N/A | Identifying the error in claiming Terraform's default replacement order is create-then-destroy | Easy |
| 3 | A, C | N/A | Identifying TWO errors in claims about the `count` and `for_each` meta-arguments | Medium |
| 4 | C | N/A | Identifying the error in claiming `depends_on` is required for attribute-reference dependencies | Medium |
| 5 | C | N/A | Identifying the error in claiming `prevent_destroy` protects against `terraform state rm` | Medium |
| 6 | C | N/A | Identifying the error in claiming `ignore_changes = all` makes a resource invisible to plan | Medium |
| 7 | C | N/A | Identifying the error in a comment claiming `count.index` starts at 1 | Medium |
| 8 | A, C | N/A | Identifying TWO errors in claims about adding `depends_on` to a `data` block | Medium |
| 9 | C | N/A | Identifying the error in claiming the `id` attribute of a managed resource can be set in HCL | Medium |
| 10 | C | N/A | Identifying the error in using a list-type variable directly with `for_each` | Medium |
| 11 | C | N/A | Identifying the error in claiming `depends_on` can override `prevent_destroy` | Hard |
| 12 | B, C | N/A | Identifying TWO errors in claims about the `removed` block's behaviour | Hard |
| 13 | C | N/A | Identifying the error in claiming `replace_triggered_by` is valid in a `data` block's `lifecycle` | Medium |
