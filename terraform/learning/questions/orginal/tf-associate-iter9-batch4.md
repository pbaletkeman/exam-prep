---
iteration: 9
batch: 4
style: "Which is true / which is false?"
style_note: >
  Every question presents one or more statements about a Terraform concept and asks
  the candidate to identify which statement(s) are TRUE, or which statement(s) are
  FALSE. Distractors are plausible-sounding misconceptions.
topics:
  - Resources & Data Blocks (Objective 4 — prompt05)
  - Dependencies & Lifecycle (Objective 4 — prompt09)
sources:
  - prompt05-resource-data-blocks.md
  - prompt09-dependencies-lifecycle.md
question_count: 13
difficulty_split: "3 Easy / 8 Medium / 2 Hard"
answer_type_split: "10 one / 3 many"
---

# Terraform Associate (004) — Iteration 9 · Batch 4
## Resources, Data & Dependencies · Which Is True / Which Is False?

---

### Question 1

**Difficulty:** Easy
**Answer Type:** one
**Topic:** Variable and local references — which statement is TRUE?

Which of the following statements about how `var.*` and `local.*` references affect Terraform's dependency graph is TRUE?

A) Referencing `var.region` inside two different resource blocks creates an implicit dependency edge between those resources — Terraform will serialise their creation in the order they appear in the configuration file
B) `local.*` references create the strongest type of dependency edge in Terraform's graph — resources that reference the same local value are always created last, after all other resources
C) `var.*` and `local.*` references do NOT create dependency edges between resources — variables and locals are simply resolved values, not resources; only direct references to another resource's attribute (e.g., `aws_vpc.main.id`) create implicit dependency edges in the DAG
D) `var.*` references create dependency edges only when the variable type is `string` — list and map variable references are ignored by the dependency graph builder

**Answer:** C

**Explanation:** Terraform's dependency graph is built exclusively from **resource attribute references** — expressions of the form `<resource_type>.<local_name>.<attribute>` (e.g., `aws_vpc.main.id`) or `module.<name>.<output>`. When two resources both reference `var.region`, there is no edge between them because `var.region` is a scalar value resolved before graph construction begins — it is not a resource and has no creation lifecycle. The two resources will be created in parallel (assuming no other dependency). Similarly, `local.*` references are computed values, not resources, and create no graph edges. Only attribute references to other managed resources or module outputs create edges. Options A, B, and D all incorrectly claim that variable or local references create dependency edges.

---

### Question 2

**Difficulty:** Easy
**Answer Type:** one
**Topic:** `ignore_changes = all` — which statement is FALSE?

Which of the following statements about the `ignore_changes = all` lifecycle argument is FALSE?

A) `ignore_changes = all` instructs Terraform to ignore ALL attribute drift on the resource — on every subsequent plan, Terraform will detect zero differences for that resource regardless of what has changed in the actual cloud infrastructure
B) `ignore_changes = all` is the broadest form of `ignore_changes` — instead of listing specific attributes, it suppresses drift detection for every attribute of the resource simultaneously
C) `ignore_changes = all` is restricted to compute resources (such as `aws_instance`) — it cannot be applied to networking, storage, or database resources because those resource types do not support the `all` keyword in their lifecycle blocks
D) `ignore_changes = all` can be useful for resources that are heavily managed by external tooling or processes outside Terraform, where drift detection would always produce noisy false-positive changes

**Answer:** C

**Explanation:** Option C is FALSE. `ignore_changes = all` is a **Terraform Core lifecycle feature** — it is not restricted to any category of resource type. It is available on ANY resource block, regardless of provider or resource type: compute, networking, storage, database, IAM, DNS, Kubernetes objects, etc. The `lifecycle` block and all its arguments (`create_before_destroy`, `prevent_destroy`, `ignore_changes`, `replace_triggered_by`) are meta-arguments provided by Terraform Core, not by individual providers. Option A is true — with `ignore_changes = all`, Terraform treats that resource as permanently in sync and proposes zero changes for it on every plan. Option B is true — `all` is the wildcard form that replaces listing individual attributes. Option D is true — this is the intended use case for `ignore_changes = all`, such as resources managed by an external scheduler or config management tool.

---

### Question 3

**Difficulty:** Easy
**Answer Type:** many
**Topic:** Which TWO statements about `for_each` are TRUE?

Which TWO of the following statements about the `for_each` meta-argument are TRUE?

A) `for_each` accepts a `set(string)` or a `map` as its value — it does NOT accept a plain `list(string)` directly; to use a list, it must first be converted to a set using `toset()` (e.g., `for_each = toset(var.names)`)
B) `for_each` accepts any collection type including `list(string)`, `set(string)`, and `map` — no type conversion is needed regardless of whether the input is a list or a set
C) Inside a resource block that uses `for_each`, `each.key` holds the current iteration's key (the map key or the set element value) and `each.value` holds the corresponding value from the map; for a set, `each.key` and `each.value` are identical since each element IS its own key
D) `for_each` and `count` can be declared together on the same resource block — `for_each` controls the naming while `count` controls the total number of instances

**Answer:** A, C

**Explanation:** **(A)** is TRUE. `for_each` only accepts `set(string)` or `map` — NOT a raw `list(string)`. Lists are ordered and allow duplicates, which would create ambiguous resource addresses. To use a list with `for_each`, you must wrap it in `toset()`: `for_each = toset(var.subnet_names)`. `toset()` deduplicates elements and converts them to a set. **(C)** is TRUE. Inside a `for_each` resource block, `each.key` is the current key. For a `map`, `each.key` is the map key and `each.value` is the corresponding value. For a `set(string)`, each element serves as its own key — so `each.key` and `each.value` are identical (both equal the element string). **(B)** is FALSE — lists are not directly accepted by `for_each`. **(D)** is FALSE — `for_each` and `count` are mutually exclusive meta-arguments; using both on the same resource block causes an error.

---

### Question 4

**Difficulty:** Medium
**Answer Type:** one
**Topic:** `replace_triggered_by` lifecycle argument — which statement is TRUE?

Which of the following statements about the `replace_triggered_by` lifecycle argument is TRUE?

A) `replace_triggered_by` is a shorthand alias for `depends_on` — both arguments create the same type of dependency edge and are interchangeable
B) `replace_triggered_by` forces a resource to be replaced (destroyed and recreated) whenever any resource or attribute listed in it changes — even if the resource's own configuration attributes have not changed; this is useful for resources like Auto Scaling Groups that should cycle when their launch template changes
C) `replace_triggered_by` only works with resources in the same module — you cannot reference a resource from a parent or child module in the `replace_triggered_by` list
D) `replace_triggered_by` is equivalent to `ignore_changes` with the opposite effect — where `ignore_changes` suppresses replacements, `replace_triggered_by` forces them for listed attributes during in-place updates

**Answer:** B

**Explanation:** `replace_triggered_by` is a lifecycle argument that causes the resource to be REPLACED (destroy + recreate, shown as `-/+` in the plan) when any of the listed resources or attributes change — even when the resource's own declared attributes have not changed at all. The canonical use case is an Auto Scaling Group (ASG) that references a Launch Template: if the launch template is updated, the ASG's own HCL configuration may not change (it still references the same `aws_launch_template.web` resource), but you want the ASG to cycle its instances using the new template. By adding `replace_triggered_by = [aws_launch_template.web]` to the ASG's lifecycle block, Terraform detects any change to the launch template and plans an ASG replacement. Option A is false — `replace_triggered_by` triggers replacement, while `depends_on` only orders operations. Option C is false — cross-module references are supported. Option D is false — `replace_triggered_by` and `ignore_changes` are independent mechanisms with unrelated semantics.

---

### Question 5

**Difficulty:** Medium
**Answer Type:** one
**Topic:** `removed` block — which statement is FALSE?

Which of the following statements about the `removed` block (Terraform 1.7+) is FALSE?

A) The `removed` block is used to stop Terraform from managing a resource while optionally keeping the actual cloud resource intact — it provides a declarative way to "forget" a resource without destroying it
B) Setting `lifecycle { destroy = false }` inside a `removed` block tells Terraform to remove the resource's state entry without issuing any destroy API call — the cloud resource continues to exist and run normally after the apply
C) The `removed` block is the only way to stop Terraform from managing a resource in Terraform 1.7+ — running `terraform state rm` to achieve the same result is deprecated and will be removed in a future version
D) The `removed` block is a version-controlled, declarative alternative to `terraform state rm` — it achieves the same state-removal outcome but is expressed in HCL and goes through the normal plan/apply workflow

**Answer:** C

**Explanation:** Option C is FALSE. `terraform state rm` is NOT deprecated — it remains a fully supported, actively maintained CLI command for removing resource entries from state. The `removed` block and `terraform state rm` are complementary tools, not competing replacements. The `removed` block is a declarative, version-controlled approach (express the intent in HCL, apply through the normal workflow, record the change in Git) while `terraform state rm` is an imperative, ad-hoc approach (run a CLI command directly). Both are valid. Option A is true — the `removed` block's purpose is to detach Terraform management from a resource. Option B is true — `lifecycle { destroy = false }` inside `removed` is the syntax that keeps the cloud resource alive while removing it from state. Option D is true — the `removed` block achieves state removal through the plan/apply workflow with full audit trail.

---

### Question 6

**Difficulty:** Medium
**Answer Type:** one
**Topic:** `depends_on` and parallelism — which statement is TRUE?

Which of the following statements about `depends_on` and its effect on performance is TRUE?

A) `depends_on` has no performance impact — Terraform's scheduler ignores explicit dependency declarations and always maximises parallelism regardless of any `depends_on` declarations
B) `depends_on` increases parallelism by giving Terraform advance knowledge of the dependency structure — without it, Terraform must wait to discover dependencies at runtime, which is slower
C) `depends_on` adds an explicit dependency edge to the Terraform DAG, serialising the creation of the dependent resource after ALL resources listed in `depends_on` complete — this reduces the potential parallelism of the apply, which is why `depends_on` should be used sparingly and only when implicit dependencies cannot capture the relationship
D) `depends_on` is only evaluated during `terraform destroy` — it has no effect on the ordering of resource creation during `terraform apply`

**Answer:** C

**Explanation:** Every edge added to Terraform's Directed Acyclic Graph (DAG) is a serialisation constraint: resource B cannot start until all resources that B depends on (directly or transitively) have finished. `depends_on` adds explicit edges that Terraform cannot derive from attribute references alone. These additional edges are necessary for correctness in cases like IAM propagation, but they come at a cost: the dependent resource must wait for all listed resources to complete before it can start, even if those resources could otherwise have overlapped in time. This is why the Terraform documentation specifically advises using `depends_on` sparingly — every unnecessary `depends_on` reduces the concurrency Terraform can achieve, making large applies slower. Option A is false — Terraform absolutely respects dependency edges when scheduling. Option B inverts the truth. Option D is false — `depends_on` affects both apply and destroy ordering.

---

### Question 7

**Difficulty:** Medium
**Answer Type:** one
**Topic:** `terraform apply -target` — which statement is FALSE?

Which of the following statements about `terraform apply -target` is FALSE?

A) `terraform apply -target=aws_instance.web` limits the apply to the specified resource and its dependency chain — only the targeted resource and any resources it depends on are included in the apply operation
B) Using `-target` is recommended as a standard day-to-day workflow practice because it allows precise, surgical updates to individual resources and prevents unintended changes to other infrastructure in the same configuration
C) Frequent use of `-target` can cause state drift — by applying changes to only a subset of resources, other resources in the configuration may become out of sync with the state file, leading to unexpected plan output on subsequent full applies
D) Terraform emits a warning when `-target` is used, reminding the engineer that the resulting plan and state may be incomplete

**Answer:** B

**Explanation:** Option B is FALSE. HashiCorp explicitly discourages using `-target` as a regular workflow practice. The warning message Terraform prints when `-target` is used states: "WARNING: Resource targeting is in effect... The -target option is not for routine use." The risks include: state drift (other resources are not updated, leaving the configuration and state out of sync), incomplete plans (resource dependencies that were skipped may produce unexpected results on the next full apply), and a false sense of safety (assuming the skipped resources are unaffected when they may actually need changes). `-target` is a break-glass tool for specific scenarios — such as bringing up a single resource for initial testing or recovering from a partial apply failure — not a routine update mechanism. Options A, C, and D are all accurate statements about `-target` behaviour and its documented risks.

---

### Question 8

**Difficulty:** Medium
**Answer Type:** one
**Topic:** Resource address format — which statement is TRUE?

Which of the following statements about Terraform resource address formats is TRUE?

A) A resource's address within its own module is always prefixed with `module.root.` — for example, an EC2 instance declared in the root module as `resource "aws_instance" "web"` has the address `module.root.aws_instance.web`
B) The address `aws_instance.web` refers to a resource only when used within the same module where it is declared — when referenced from the root module, the address automatically includes the full provider namespace, becoming `hashicorp/aws.aws_instance.web`
C) A resource declared in the root module as `resource "aws_instance" "web"` has the local address `aws_instance.web` within that module; when the same resource is referenced from an external context (such as a `terraform state` command or an error message), its fully qualified address is `aws_instance.web` (root module resources have no module prefix); a resource inside a child module called `compute` would be addressed as `module.compute.aws_instance.web`
D) Resource addresses always include the provider name as a prefix — for example, `aws.aws_instance.web` or `azurerm.azurerm_resource_group.rg` — to disambiguate resources when multiple providers are in use

**Answer:** C

**Explanation:** Terraform resource addresses follow a predictable format. Within the root module, the address is simply `<TYPE>.<LOCAL_NAME>` — e.g., `aws_instance.web`. There is no `module.root.` prefix for root module resources. In `terraform state` commands, plan output, error messages, and `moved` blocks, root module resources are referenced without any module prefix. Resources inside a child module named `compute` are addressed as `module.compute.<TYPE>.<LOCAL_NAME>` — e.g., `module.compute.aws_instance.web`. If the child module is instantiated with `count` or `for_each`, the address includes the index: `module.compute[0].aws_instance.web` or `module.compute["prod"].aws_instance.web`. Option A is false — root module resources have no `module.root.` prefix. Option B is false — the provider namespace is not included in resource addresses. Option D is false — provider names are not part of resource addresses.

---

### Question 9

**Difficulty:** Medium
**Answer Type:** one
**Topic:** Data source with computed inputs — which statement is TRUE?

Which of the following statements about a data source whose filter arguments depend on computed values from unbuilt resources is TRUE?

A) Terraform prohibits data source filter arguments from referencing computed attributes of resources that do not yet exist — the configuration will fail validation with an error at plan time if any data source references an attribute that is "known after apply"
B) When a data source's filter arguments depend on an attribute of a resource that does not yet exist (a computed/"known after apply" value), Terraform defers reading the data source until the apply phase — the plan output shows the data source result and any resources depending on it as "(known after apply)", and the actual API call to read the data source happens during apply after the dependency is created
C) When a data source references a "(known after apply)" attribute, Terraform uses the last known value from the state file as a substitute — this prevents any "unknown" values from propagating to downstream resources
D) Data sources are always read during the plan phase, regardless of whether their inputs are known — Terraform uses placeholder values for any unknown inputs and corrects them automatically during apply without any visible indication in the plan output

**Answer:** B

**Explanation:** This is a nuanced but important exam topic. If a data source's filter argument references a resource attribute that cannot be determined until that resource is actually created (a "computed" value), Terraform cannot read the data source during the planning phase because the input doesn't exist yet. Instead, Terraform defers the data source read to the apply phase. In the plan output, both the data source result and any resources that depend on the data source result appear as `(known after apply)`. After the dependency resource is created during apply, Terraform reads the data source using the now-known input value, then uses the result for any downstream resources in the same apply run. Option A is false — Terraform handles this case gracefully rather than failing validation. Option C is false — Terraform does not substitute stale state values; it marks things as unknown and resolves them during apply. Option D is false — data sources with unknown inputs are explicitly NOT read during the plan phase.

---

### Question 10

**Difficulty:** Medium
**Answer Type:** many
**Topic:** Which TWO statements about the `moved` block are TRUE?

Which TWO of the following statements about the `moved` block are TRUE?

A) After a successful `terraform apply` that processes a `moved` block, the `moved` block has served its purpose and can be safely deleted from the configuration — the resource is now tracked under its new address and no further `moved` block is needed
B) If a `moved` block is accidentally removed from a configuration BEFORE the apply that would process it, Terraform will silently skip the rename and the resource will retain its old address in state permanently with no further action possible
C) A `moved` block can relocate a resource FROM the root module INTO a child module — for example, `from = aws_instance.web` and `to = module.compute.aws_instance.server` is valid and moves the state entry into the child module's address namespace without destroying the cloud resource
D) `moved` blocks are processed by Terraform only when `terraform init -upgrade` is run — they are not processed during a normal `terraform plan` or `terraform apply` cycle

**Answer:** A, C

**Explanation:** **(A)** is TRUE. The `moved` block is ephemeral in nature — once Terraform applies the state rename, the block has done its job. It is safe (and encouraged) to remove it from configuration afterwards. The resource is now tracked at its new address, and future plans will use the new address directly without needing the `moved` block. **(C)** is TRUE. `moved` blocks support cross-module relocations: `from = aws_instance.web` (root module) and `to = module.compute.aws_instance.server` (child module) is valid syntax. Terraform updates the state address to reflect the new module path without any API calls to the cloud resource. **(B)** is FALSE. If you remove a `moved` block before applying it, the situation is not permanent — the old state entry still exists. You can re-add the `moved` block, use `terraform state mv` as an alternative, or re-introduce the old resource name in HCL. Terraform does not permanently lock state addresses. **(D)** is FALSE — `moved` blocks are processed during normal `terraform plan` and `terraform apply`; `terraform init -upgrade` is unrelated to state operations.

---

### Question 11

**Difficulty:** Medium
**Answer Type:** one
**Topic:** `prevent_destroy` scope — which statement is FALSE?

Which of the following statements about `prevent_destroy = true` is FALSE?

A) `prevent_destroy = true` causes `terraform plan` to return an error if the proposed plan includes destroying the protected resource — it does not wait until `terraform apply` to raise the error
B) `prevent_destroy = true` can be bypassed at runtime by passing the `-force-destroy` flag to `terraform destroy` — this allows emergency teardowns without modifying the configuration
C) The only way to destroy a resource protected by `prevent_destroy = true` is to first remove or disable the `prevent_destroy` setting in the configuration, then run `terraform apply` or `terraform destroy` — there is no runtime flag to override it, by design
D) `prevent_destroy = true` is intentionally impossible to bypass with a flag because its purpose is to force a deliberate, reviewable, version-controlled configuration change before destruction can occur

**Answer:** B

**Explanation:** Option B is FALSE. There is NO `-force-destroy` flag on `terraform destroy` (or any other runtime flag) that bypasses `prevent_destroy = true`. This is a deliberate design decision, not an oversight: `prevent_destroy` is meant to be a code-level guard that forces a deliberate code review and commit before anything can be destroyed. If `-force-destroy` existed, the protection would be trivially defeated by any engineer with CLI access. The ONLY way to destroy a `prevent_destroy`-protected resource is to edit the `.tf` file to remove or disable `prevent_destroy = true`, commit the change, and then run apply or destroy. Options A, C, and D are all accurate: the error is raised at plan time (not apply time), the configuration change is the only override, and this behaviour is by design.

---

### Question 12

**Difficulty:** Hard
**Answer Type:** one
**Topic:** Four statements about lifecycle meta-arguments — only ONE is TRUE

Four statements about Terraform lifecycle meta-arguments are presented below. Which is the ONLY TRUE statement?

A) `create_before_destroy = true` and `prevent_destroy = true` can never be declared together in the same `lifecycle` block — Terraform raises a configuration error because the two arguments conflict: `create_before_destroy` assumes a replacement will happen, while `prevent_destroy` blocks any replacement
B) `ignore_changes` with a list of attributes (e.g., `ignore_changes = [tags]`) tells Terraform to never create or update the resource for those attributes — Terraform will also skip creating the resource if the initial `terraform apply` only has values for the ignored attributes
C) `replace_triggered_by` accepts a list of resource references or specific resource attributes — when a referenced resource OR attribute changes on apply, Terraform plans the resource as a forced replacement (`-/+`), even if none of that resource's own declared attributes have changed; `replace_triggered_by` only triggers on changes, not on initial resource creation
D) The four lifecycle arguments (`create_before_destroy`, `prevent_destroy`, `ignore_changes`, `replace_triggered_by`) are mutually exclusive — only one can be declared per `lifecycle` block; declaring two or more causes a validation error

**Answer:** C

**Explanation:** Option C is the ONLY TRUE statement. `replace_triggered_by` accepts resource references (e.g., `aws_launch_template.web`) or specific attribute references (e.g., `aws_launch_template.web.image_id`). When any listed resource or attribute changes on an apply, Terraform marks the resource for replacement in the plan (shown with `-/+`), regardless of whether the resource's own configuration attributes changed. Additionally, `replace_triggered_by` only evaluates for changes — it does not trigger on the INITIAL creation of a resource (there is nothing to "change from" on the first apply). Option A is FALSE — `create_before_destroy` and `prevent_destroy` can absolutely coexist in the same `lifecycle` block; `create_before_destroy` controls the ORDER of replacement, while `prevent_destroy` blocks replacement from being planned at all; they can coexist because they address different scenarios. Option B is FALSE — `ignore_changes` only affects DRIFT DETECTION on existing managed resources; it does not affect the initial creation of a resource. If a resource doesn't exist yet, Terraform creates it normally regardless of `ignore_changes`. Option D is FALSE — all four lifecycle arguments are independent and can be combined freely in a single `lifecycle` block.

---

### Question 13

**Difficulty:** Hard
**Answer Type:** many
**Topic:** Which TWO statements about Terraform's dependency graph (DAG) are TRUE?

Which TWO of the following statements about Terraform's dependency graph are TRUE?

A) Terraform builds a Directed Acyclic Graph (DAG) where each node represents a resource and each directed edge represents a dependency — the "acyclic" property guarantees no circular dependencies exist; if a circular dependency is detected (e.g., resource A references B and B references A), Terraform returns a configuration error rather than attempting to execute an infinite loop
B) Resources with no dependencies between them are always executed strictly sequentially — Terraform processes one resource at a time in alphabetical order by resource type to ensure reproducible, deterministic apply outputs
C) The destroy order in Terraform is the topological REVERSE of the create order — in a chain where A ← B ← C (C depends on B, B depends on A), creation order is A → B → C and destruction order is C → B → A; this guarantees that no resource is destroyed while another resource that depends on it still exists
D) Adding `depends_on` between two resources that already have an implicit attribute-reference dependency is harmless but redundant — the graph edge already exists, so the explicit `depends_on` adds no new constraint and has no effect on execution order or parallelism

**Answer:** A, C

**Explanation:** **(A)** is TRUE. The "acyclic" in DAG is a correctness requirement: Terraform cannot execute a plan if the dependency graph contains a cycle (A depends on B, B depends on A — who gets created first?). Terraform detects cycles during graph construction and immediately returns an error like `Cycle: aws_instance.web, aws_security_group.web_sg` before any plan or apply operation. Engineers must resolve cycles by redesigning the dependency structure. **(C)** is TRUE. Terraform's destroy ordering is the exact topological reverse of create ordering. This guarantees referential integrity during teardown — you can never have a situation where Terraform destroys a VPC while subnets that reference it still exist, because the subnets (being more dependent) are always destroyed first. **(B)** is FALSE — resources without dependencies between them are executed IN PARALLEL (up to the `-parallelism` limit, default 10), not sequentially. Sequential execution of independent resources would dramatically slow down large environments. **(D)** is FALSE. Adding a redundant `depends_on` that duplicates an existing implicit dependency IS NOT fully harmless. While it doesn't change correctness (the edge already exists), it CAN reduce parallelism in some cases: `depends_on` on a resource propagates to ALL resources that depend on the dependent resource, potentially creating broader serialisation than the original attribute reference alone. Terraform documentation notes this propagation effect as a reason to use `depends_on` sparingly.
