# Terraform Associate Exam Questions

---

### Question 1

**Difficulty:** Easy
**Answer Type:** one
**Topic:** Destroy order in a resource dependency chain

A Terraform configuration contains three resources with the following dependency chain: `aws_vpc.main` ← `aws_subnet.public` ← `aws_instance.web` (the instance depends on the subnet, and the subnet depends on the VPC). When `terraform destroy` runs, which resource is destroyed FIRST?

A) `aws_vpc.main` — the dependency anchor is always removed first to cascade the destruction downward
B) The three resources are destroyed in parallel because all destroy operations are independent
C) `aws_subnet.public` — Terraform always begins destruction in the middle of the dependency chain
D) `aws_instance.web` — Terraform destroys in REVERSE dependency order; the most-dependent resource (the one at the "leaf" of the graph) is always destroyed first, followed by resources it depended on

---

### Question 2

**Difficulty:** Easy
**Answer Type:** one
**Topic:** Correct three-step sequence for the `moved` block lifecycle

An engineer renames a Terraform resource from `aws_instance.app` to `aws_instance.web` in the HCL. Without any additional steps, `terraform plan` would show the old instance being destroyed and a new one being created. The engineer wants to avoid this. Which of the following correctly sequences ALL the steps required to rename the resource in state without a destroy-and-recreate cycle?

A) (1) Run `terraform state mv aws_instance.app aws_instance.web` to rename in state → (2) Rename the resource block in HCL → (3) Run `terraform apply` to sync
B) (1) Rename the resource block in HCL → (2) Add a `moved { from = aws_instance.app; to = aws_instance.web }` block → (3) Run `terraform apply` — Terraform updates the state address; after a successful apply the `moved` block can optionally be removed
C) (1) Add a `moved` block → (2) Run `terraform init` → (3) Rename the resource block in HCL → (4) Run `terraform apply`
D) (1) Run `terraform apply` with the old name to record the current state → (2) Add a `moved` block → (3) Rename the HCL block → (4) Run `terraform apply` again

---

### Question 3

**Difficulty:** Easy
**Answer Type:** many
**Topic:** When in the plan/apply sequence are data sources evaluated?

Which TWO of the following correctly describe when Terraform reads a data source during the plan/apply lifecycle?

A) Data sources are always read during `terraform init` — the results are cached in `.terraform/` and reused by all subsequent plan and apply operations
B) Data sources whose filter arguments are fully known at plan time are read during the **plan phase** — their results are included in the plan output so you can see what value the data source resolved to before committing to an apply
C) Data sources whose filter arguments depend on computed values from other resources (values not yet known until those resources are created) are **deferred to the apply phase** — the plan shows these data source results as "(known after apply)" and any resources that depend on them inherit the same uncertainty
D) Data sources are always read during the apply phase, never during planning, because Terraform cannot guarantee state stability at plan time

---

### Question 4

**Difficulty:** Medium
**Answer Type:** one
**Topic:** Creation order given a three-resource dependency chain where the chain direction must be read correctly

A Terraform configuration has three resources: `aws_security_group.web`, `aws_instance.web`, and `aws_lb_target_group_attachment.web`. The instance references the security group's `id`, and the attachment references the instance's `id`. In what order does Terraform create these resources during `terraform apply`?

A) `aws_lb_target_group_attachment.web` → `aws_instance.web` → `aws_security_group.web` (attachment first because it is the most-dependent and needs to be ready before the others)
B) All three are created simultaneously because Terraform maximises parallelism and resolves dependencies dynamically at runtime
C) `aws_security_group.web` → `aws_instance.web` → `aws_lb_target_group_attachment.web` (the dependency root is created first; resources are created in topological order from least-dependent to most-dependent)
D) `aws_instance.web` → `aws_security_group.web` → `aws_lb_target_group_attachment.web` (compute resources always take priority over networking and attachment resources)

---

### Question 5

**Difficulty:** Medium
**Answer Type:** one
**Topic:** Sequence of operations when `replace_triggered_by` fires

An Auto Scaling Group (ASG) has the following lifecycle block:

```hcl
resource "aws_autoscaling_group" "web" {
  lifecycle {
    replace_triggered_by = [aws_launch_template.web]
  }
}
```

An engineer updates the `aws_launch_template.web` resource (changes the AMI). Which of the following correctly sequences what Terraform does during the NEXT `terraform apply`?

A) Terraform replaces the launch template first (destroy old template → create new template), THEN replaces the ASG (destroy old ASG → create new ASG) — in that order, because the ASG depends on the template
B) Terraform replaces the ASG first, then updates the launch template — the ASG replacement must precede the template change to avoid traffic disruption
C) Terraform updates the launch template in-place (`~`) and separately schedules the ASG for replacement during the next maintenance window
D) Terraform updates `aws_launch_template.web` first (or creates the new version), and then — because the `replace_triggered_by` constraint is satisfied — marks `aws_autoscaling_group.web` for replacement (`-/+`) in the SAME plan; both changes are applied in dependency order: template first, then ASG replacement

---

### Question 6

**Difficulty:** Medium
**Answer Type:** one
**Topic:** Correct sequence to stop managing a resource without destroying it using the `removed` block (Terraform 1.7+)

An engineer wants Terraform to stop tracking `aws_s3_bucket.legacy` in state, but they do NOT want the bucket to be deleted — it should continue to exist in AWS after the operation. Which of the following correctly sequences all required steps using the Terraform 1.7+ `removed` block approach?

A) (1) Delete the `resource "aws_s3_bucket" "legacy"` block from HCL → (2) Run `terraform apply` → the bucket is automatically retained because S3 buckets are never auto-deleted
B) (1) Run `terraform state rm aws_s3_bucket.legacy` → (2) Delete the resource block from HCL → (3) Run `terraform apply` (shows no changes because state entry is gone)
C) (1) Add a `removed { from = aws_s3_bucket.legacy; lifecycle { destroy = false } }` block to the configuration (the original resource block can be deleted simultaneously) → (2) Run `terraform apply` — Terraform removes the state entry for the bucket but makes no API calls to delete the cloud resource
D) (1) Set `prevent_destroy = true` in the resource's lifecycle block → (2) Delete the resource block → (3) Run `terraform apply` — `prevent_destroy` automatically retains the resource in AWS when the block is removed

---

### Question 7

**Difficulty:** Medium
**Answer Type:** one
**Topic:** `count` index shift when inserting an item in the middle of a list — sequence of unintended operations

An engineer uses `count` to create three S3 buckets from a list:

```hcl
variable "bucket_names" {
  default = ["alpha", "gamma", "delta"]
}

resource "aws_s3_bucket" "buckets" {
  count  = length(var.bucket_names)
  bucket = var.bucket_names[count.index]
}
```

The engineer inserts `"beta"` between `"alpha"` and `"gamma"`, making the list `["alpha", "beta", "gamma", "delta"]`. Which of the following correctly sequences the operations Terraform plans for the existing resources?

A) Terraform only creates one new resource (`aws_s3_bucket.buckets[1]` named "beta") — existing resources at indexes 1 and 2 are unchanged
B) Because `count` uses stable string keys, inserting "beta" at index 1 only shifts the display order — no resources are destroyed or recreated
C) Terraform's plan shows: `aws_s3_bucket.buckets[1]` updated from "gamma" to "beta" (or replaced if the `bucket` argument is immutable), `aws_s3_bucket.buckets[2]` updated from "delta" to "gamma", and `aws_s3_bucket.buckets[3]` created as "delta" — inserting an item in the middle shifts all subsequent integer indexes, causing Terraform to interpret those as attribute changes or replacements on existing resources
D) Terraform destroys all four buckets and recreates them in the new order — any insertion into a `count`-managed list always causes a full teardown

---

### Question 8

**Difficulty:** Medium
**Answer Type:** one
**Topic:** `for_each` key stability when adding a new element — sequence of operations

An engineer creates three S3 buckets using `for_each`:

```hcl
resource "aws_s3_bucket" "buckets" {
  for_each = toset(["alpha", "gamma", "delta"])
  bucket   = each.key
}
```

They add `"beta"` to the set, making it `toset(["alpha", "beta", "gamma", "delta"])`. Which of the following correctly sequences the operations Terraform plans?

A) Terraform destroys all four buckets and recreates them in alphabetical order — sets are unordered, so Terraform treats the new set as a completely new collection
B) Terraform creates only `aws_s3_bucket.buckets["beta"]` — the resources keyed `"alpha"`, `"gamma"`, and `"delta"` are untouched because their string keys are unchanged; this is the key advantage of `for_each` over `count` for collections where items may be added or removed
C) Terraform creates `aws_s3_bucket.buckets["beta"]` and also plans an update on `aws_s3_bucket.buckets["gamma"]` because adding a new key between "alpha" and "gamma" shifts the alphabetical position of "gamma"
D) Terraform plans four creates and four destroys — `for_each` with `toset()` always triggers a full replacement when the set contents change

---

### Question 9

**Difficulty:** Medium
**Answer Type:** many
**Topic:** Two correct ordering statements about `depends_on` vs implicit dependencies

Which TWO of the following correctly describe the ordering relationship between implicit dependencies (attribute references) and explicit `depends_on` declarations?

A) Implicit dependencies and `depends_on` both result in the same topological execution ordering — if resource B depends on resource A through either mechanism, Terraform always creates A before B and destroys B before A
B) `depends_on` is processed BEFORE implicit dependency edges during graph construction — resources listed in `depends_on` always execute before any attribute-referenced dependencies
C) When a resource has BOTH an implicit dependency (attribute reference to resource A) AND a `depends_on = [resource_B]` declaration, Terraform creates resource A and resource B before the dependent resource — both dependency edges are respected and combined in the graph; the dependent resource starts only after ALL its dependencies (implicit and explicit) have completed
D) Implicit dependencies override `depends_on` declarations — if a resource references an attribute of resource A, any `depends_on = [resource_B]` on the same resource is silently ignored

---

### Question 10

**Difficulty:** Medium
**Answer Type:** one
**Topic:** Aliased provider declaration must precede resources using it

An engineer wants to deploy resources in two AWS regions using provider aliases. Which of the following correctly identifies what must be done FIRST before a resource can use `provider = aws.us-west`?

A) Run `terraform apply` with the default provider configuration first — the alias is automatically derived from the default provider's region
B) The `provider "aws" { alias = "us-west"; region = "us-west-2" }` block must be declared in the configuration before any resource references it with `provider = aws.us-west`; `terraform init` must also have been run so the provider plugin is installed — without the alias declaration, the `provider = aws.us-west` reference in the resource block is invalid and `terraform validate` will fail
C) Run `terraform workspace new us-west` — workspace creation automatically registers a new provider alias for the workspace's region
D) Add `providers = { aws = aws.us-west }` to the module block in the root configuration — this implicitly creates the alias without a separate `provider` block

---

### Question 11

**Difficulty:** Hard
**Answer Type:** one
**Topic:** Complete sequence of how Terraform executes the dependency graph during apply

Which of the following correctly describes the COMPLETE sequence of how Terraform executes a dependency graph containing resources with mixed dependencies during `terraform apply`?

A) Terraform processes all resource blocks in the order they appear in `.tf` files — alphabetically by filename, then by block order within each file
B) (1) Terraform builds the full DAG by scanning all resource attribute references and `depends_on` declarations → (2) Resources with no dependencies (graph roots) are started IMMEDIATELY and in PARALLEL (up to the `-parallelism` limit, default 10) → (3) As each resource operation completes, Terraform evaluates which newly unblocked resources (those whose dependencies have all completed) can now start → (4) Those newly unblocked resources begin execution in parallel → (5) This wave-by-wave parallel execution continues until all resources in the graph are complete
C) Terraform executes all resources sequentially in a single thread — parallelism only applies to provider API calls within a single resource operation, not to separate resource operations
D) (1) Build DAG → (2) Execute all resources in strict alphabetical order by resource address (e.g., `aws_instance` before `aws_vpc`) → (3) Dependencies are checked after each resource completes and missing dependencies cause a rollback

---

### Question 12

**Difficulty:** Hard
**Answer Type:** one
**Topic:** Complete sequence of events when a data source depends on a not-yet-known computed value

A configuration contains the following:

```hcl
resource "aws_instance" "app" {
  ami           = "ami-0abc123"
  instance_type = "t3.micro"
}

data "aws_eip" "app_ip" {
  filter {
    name   = "instance-id"
    values = [aws_instance.app.id]
  }
}

resource "aws_route53_record" "app" {
  records = [data.aws_eip.app_ip.public_ip]
}
```

This is the first apply — `aws_instance.app` does not yet exist. Which of the following correctly sequences what Terraform does across BOTH the plan and apply phases?

A) Terraform reads the data source during the plan phase using a placeholder ID, then re-reads it during apply once the real ID is available — both phases produce accurate results
B) During plan: Terraform cannot read `data.aws_eip.app_ip` because `aws_instance.app.id` is not yet known (it is a computed value that will only exist after the instance is created) — the plan marks the data source result and all downstream attributes as "(known after apply)"; During apply: Terraform first creates `aws_instance.app` (now the instance ID is known), THEN reads `data.aws_eip.app_ip` using the real instance ID, THEN creates `aws_route53_record.app` using the resolved IP — in that exact sequence
C) Terraform fails at the plan stage with a permanent error — data sources that depend on computed resource attributes can never be used in the same configuration that creates those resources
D) During plan: the data source is read with a nil value, causing `aws_route53_record.app` to be created with an empty `records` list; during apply, a second apply is required to correct the DNS record with the real IP

---

### Question 13

**Difficulty:** Hard
**Answer Type:** many
**Topic:** `create_before_destroy` propagation through dependency chains

Which TWO of the following correctly describe how `lifecycle { create_before_destroy = true }` interacts with resources that have dependents in the graph?

A) `create_before_destroy = true` is "viral" — if resource A has `create_before_destroy = true` and resource B depends on resource A, Terraform implicitly propagates `create_before_destroy` to resource B as well; this is required because creating the new A before destroying the old A means B (which depends on A) may also need to be handled in create-before-destroy order to avoid referencing a resource that no longer exists
B) `create_before_destroy = true` is isolated to the resource it is declared on — dependent resources are never affected and always use the default destroy-then-create replacement order regardless of what their dependencies are doing
C) When resource A has `create_before_destroy = true` and is being replaced, the sequence for the entire sub-graph involving A and its dependent B is: (1) create new A → (2) create new B (pointing to new A) → (3) destroy old B → (4) destroy old A — preserving the create-before-destroy guarantee at every level
D) `create_before_destroy = true` only affects the `terraform destroy` command — it has no effect during `terraform apply` replacements triggered by configuration changes

## Answer Key

| Q# | Answer(s) | Explanation | Source | Difficulty |
|----|-----------|-----------:|--------|------------|
| 1 | D | ** Terraform's destroy order is the exact reverse of its create order. During `terraform apply`, Terraform creates resources from the root of the dependency graph outward — dependencies first, dependents after. During `terraform destroy`, this ordering is flipped: dependents are destroyed first, then the resources they depended on. In this chain, `aws_instance.web` depends on `aws_subnet.public`, which depends on `aws_vpc.main`. Destroy order: (1) `aws_instance.web` → (2) `aws_subnet.public` → (3) `aws_vpc.main`. Destroying the VPC first would fail — the subnet and instance still reference it. Terraform's DAG prevents this by reversing the edges for destruction. | ** Destroy order in a resource dependency chain | ** Easy |
| 2 | B | ** The `moved` block approach requires two things to exist simultaneously when `terraform apply` runs: the renamed HCL resource block AND the `moved` block mapping the old address to the new one. The correct sequence is: (1) Rename the resource block in HCL from `aws_instance.app` to `aws_instance.web`; (2) Add a `moved { from = aws_instance.app; to = aws_instance.web }` block in the same or any `.tf` file in the module; (3) Run `terraform apply` — Terraform processes the `moved` block, updates the state entry to the new address, and reports no infrastructure changes. After a successful apply, the `moved` block has done its job and can be safely removed from configuration. Option A uses the older `terraform state mv` CLI approach, which also works but is not the `moved` block workflow. Option C incorrectly inserts `terraform init` as a required step and requires the HCL rename to happen after — Terraform needs both the new block name and the `moved` block to coexist. | ** Correct three-step sequence for the `moved` block lifecycle | ** Easy |
| 3 | B, C | ** Terraform evaluates data sources at two possible points depending on when their inputs are known. **(B)** If all filter arguments in the data source block are fully known at plan time (e.g., a static tag or a known variable value), Terraform reads the data source during the plan phase — this allows the plan output to show you the resolved value (such as an AMI ID) before you approve the apply. **(C)** If a filter argument depends on an attribute of a resource that does not yet exist (a "computed" value), Terraform cannot query the data source during planning because the input is not yet available. In this case, the data source read is deferred to apply time, and the plan output marks the data source result and any downstream attributes as "(known after apply)". Option A is false — data sources are never read or cached during `terraform init`. Option D is false — data sources are frequently read during the plan phase when inputs are known. | ** When in the plan/apply sequence are data sources evaluated? | ** Easy |
| 4 | C | ** Terraform builds a Directed Acyclic Graph (DAG) from the configuration's attribute references and executes operations in topological order — dependencies are always created before the resources that depend on them. In this chain: `aws_security_group.web` has no dependencies (it is the root), so it is created first. `aws_instance.web` references `aws_security_group.web.id`, so it cannot start until the security group is ready — it is created second. `aws_lb_target_group_attachment.web` references `aws_instance.web.id`, so it is created last. This mirrors the destroy order in reverse: attachment → instance → security group during destruction. Option A describes the destroy order, not the create order. | ** Creation order given a three-resource dependency chain where the chain direction must be read correctly | ** Medium |
| 5 | D | ** `replace_triggered_by` makes a resource's replacement contingent on a change to another resource or attribute. When the launch template changes, Terraform's plan for this apply includes: (1) update or replace `aws_launch_template.web` first (it is the dependency), and (2) mark `aws_autoscaling_group.web` for replacement (`-/+`) because the `replace_triggered_by` constraint is now satisfied. Both operations are included in the SAME plan and executed in the correct dependency order — the template change is applied before the ASG replacement, because the ASG implicitly depends on the template. The ASG replacement is not deferred to a future apply or a maintenance window. Option B reverses the order. Option C is incorrect — `replace_triggered_by` triggers a full replacement, not an in-place update. | ** Sequence of operations when `replace_triggered_by` fires | ** Medium |
| 6 | C | ** The `removed` block (introduced in Terraform 1.7) is the declarative way to stop tracking a resource without destroying it. The sequence is: (1) Remove the original `resource "aws_s3_bucket" "legacy"` block from configuration (or keep it alongside the `removed` block — Terraform accepts either) and add a `removed` block pointing to the old address with `lifecycle { destroy = false }`; (2) Run `terraform apply` — Terraform processes the `removed` block, removes `aws_s3_bucket.legacy` from state, and — because `destroy = false` — does NOT call the S3 delete API. The bucket persists untouched in AWS. Option A is wrong — deleting a resource block without a `removed` block or `prevent_destroy` causes Terraform to plan a destroy. Option D is wrong — `prevent_destroy = true` causes `terraform apply` to error when the resource block is removed, not silently retain the resource. | ** Correct sequence to stop managing a resource without destroying it using the `removed` block (Terraform 1.7+) | ** Medium |
| 7 | C | ** `count`-based resources are addressed by integer index: `aws_s3_bucket.buckets[0]`, `[1]`, `[2]`. When a new item is inserted before the end of the list, all subsequent indexes shift. Terraform compares the new desired state (index → name mapping) against the old state (index → name mapping) and sees the bucket name at indexes 1, 2, and 3 has "changed." Since `aws_s3_bucket.bucket` is immutable (ForceNew), Terraform may plan a replacement (`-/+`) for each shifted resource, or at minimum a configuration drift for each. Only the insertion at the very END of a count list is safe — appending adds a new resource at a new index without touching existing indexes. This is a key reason why `for_each` with stable string keys is preferred over `count` for most real-world resources. | ** `count` index shift when inserting an item in the middle of a list — sequence of unintended operations | ** Medium |
| 8 | B | ** `for_each` resources are addressed by their stable string key: `aws_s3_bucket.buckets["alpha"]`, `["gamma"]`, `["delta"]`. When `"beta"` is added to the set, Terraform computes the diff: three existing keys (`"alpha"`, `"gamma"`, `"delta"`) are unchanged — their state entries still match the configuration — and one new key (`"beta"`) is present in configuration but not in state. Terraform plans a single create: `aws_s3_bucket.buckets["beta"]`. The existing resources are completely unaffected. This string-key stability is the primary advantage of `for_each` over `count` — adding, removing, or reordering elements only affects the specific keys that changed, not every resource with a subsequent index. | ** `for_each` key stability when adding a new element — sequence of operations | ** Medium |
| 9 | A, C | ** **(A)** Both implicit (attribute reference) and explicit (`depends_on`) dependencies result in identical ordering behavior — Terraform adds a directed edge to the DAG in both cases, ensuring the depended-upon resource is created first and destroyed last. The mechanism of detection differs (automatic vs manual), but the graph effect is the same. **(C)** When a resource has both types of dependency, Terraform combines ALL edges from both sources into the dependency graph. The dependent resource will only begin execution after every dependency — whether implicit or explicit — has completed. There is no priority or override between the two types. Option B is false — there is no processing priority between implicit and explicit edges; they are all incorporated into the same DAG simultaneously. Option D is false — `depends_on` is never ignored; it adds additional dependency edges that constrain ordering beyond what attribute references alone would provide. | ** Two correct ordering statements about `depends_on` vs implicit dependencies | ** Medium |
| 10 | B | ** Using a provider alias requires two things to exist before any resource can reference it: (1) a `provider "aws" { alias = "us-west"; region = "us-west-2" }` block declared in the configuration (typically in `providers.tf` or `main.tf`) — this is what defines the alias and its configuration; (2) `terraform init` must have run to ensure the provider plugin is installed for the working directory. A resource using `provider = aws.us-west` references the alias by name — if the alias block is absent, `terraform validate` will return an error because the reference cannot be resolved. Declaration order within `.tf` files does not matter (Terraform loads all `.tf` files in a directory before processing), but the alias block must be present somewhere in the configuration before apply. Workspaces and module blocks do not create provider aliases. | ** Aliased provider declaration must precede resources using it | ** Medium |
| 11 | B | ** Terraform's execution model is a parallel wave-based traversal of the dependency DAG. The complete sequence is: (1) Parse all configuration files and build the complete dependency graph from attribute references and `depends_on` declarations; (2) Identify all "ready" resources — those whose dependencies have already completed (on the first wave, these are resources with no dependencies at all); (3) Launch those ready resources in parallel, subject to the concurrency limit (default: 10 simultaneous operations, overridable with `terraform apply -parallelism=N`); (4) As each resource operation finishes, re-evaluate the graph to find newly unblocked resources (those whose last pending dependency just completed); (5) Immediately start the newly unblocked resources; (6) Repeat until all resources are done. This model maximises parallelism while strictly respecting the dependency ordering. File declaration order and alphabetical order have no influence on execution sequence. | ** Complete sequence of how Terraform executes the dependency graph during apply | ** Hard |
| 12 | B | ** When a data source filter argument references a computed attribute (one that is only known after a resource is created), Terraform defers the data source read to apply time. The full sequence across both phases: **Plan phase** — Terraform detects that `aws_instance.app.id` is not yet known, marks `data.aws_eip.app_ip` as "(known after apply)", and propagates this uncertainty to `aws_route53_record.app.records`; the plan shows both the data source result and the DNS record as "(known after apply)" for affected attributes. **Apply phase** — Terraform creates `aws_instance.app` first (getting a real instance ID), then reads `data.aws_eip.app_ip` using the now-known instance ID (getting a real Elastic IP), then creates `aws_route53_record.app` with the resolved public IP. All three operations occur in a single apply — no second apply is required. Option A is wrong — Terraform does not use placeholder IDs to read data sources; it defers the read entirely. | ** Complete sequence of events when a data source depends on a not-yet-known computed value | ** Hard |
| 13 | A, C | ** **(A)** `create_before_destroy` propagates upward through the dependency graph. If resource A has this lifecycle setting and resource B depends on A, Terraform must also apply create-before-destroy to B. The reasoning: to create the new A before destroying the old A (the setting's goal), B is still attached to the old A. For Terraform to safely detach B from the old A and point it to the new A, B itself must go through a create-before-destroy replacement. Terraform enforces this automatically — the setting is "viral" up the dependency chain. **(C)** Describes the correct four-step sequence for the full sub-graph: new A is created first (because `create_before_destroy = true`), then new B is created pointing at the new A, then old B is destroyed, then old A is destroyed. This ordering ensures no resource is ever in a state where it references a deleted dependency. Option B is false — the propagation behavior described in A and C contradicts it. Option D is false — `create_before_destroy` applies to all replacement scenarios during `terraform apply`, not just `terraform destroy`. | ** `create_before_destroy` propagation through dependency chains | ** Hard |
