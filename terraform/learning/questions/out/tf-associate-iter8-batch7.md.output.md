# Terraform Associate Exam Questions

---

### Question 1

**Difficulty:** Easy
**Answer Type:** one
**Topic:** `terraform init` must come BEFORE `terraform plan` whenever a new module block is added

An engineer adds a brand-new `module "dns"` block with `source = "./modules/dns"` to an existing configuration. The `./modules/dns` directory exists and contains valid `.tf` files. Which of the following correctly sequences the steps the engineer must take to successfully plan and apply the new module?

A) (1) Run `terraform plan` — Terraform automatically detects and registers local module sources at plan time; (2) Run `terraform apply` if the plan looks correct
B) (1) Run `terraform init` — this registers the new module source in `.terraform/modules/modules.json` even though no download occurs for a local path; (2) Run `terraform plan` — now the module is installed and Terraform can evaluate its resources; (3) Run `terraform apply`
C) (1) Run `terraform apply -auto-approve` — the apply command installs modules before executing; no separate `terraform init` is needed for local path modules
D) (1) Copy the module files into the `.terraform/modules/` directory manually; (2) Run `terraform plan`; (3) Run `terraform apply`

---

### Question 2

**Difficulty:** Easy
**Answer Type:** one
**Topic:** Module input variable flow — declared in child, explicitly assigned in root, used by child resources

Which of the following correctly sequences how a module input variable flows from declaration to use?

A) (1) The root module assigns a value in the `module` block; (2) Terraform automatically discovers what variables the child module needs by scanning its resource arguments; (3) The child module's resources access the values directly from the root module's scope
B) (1) The child module declares the variable in its own `variables.tf` (or anywhere in the module's `.tf` files); (2) The root module explicitly assigns a value to that variable inside the `module` block argument list; (3) Resources inside the child module reference `var.<name>` to consume the value — the value flows DOWN from root to child, never automatically inherited
C) (1) The root module declares the variable in its `variables.tf`; (2) The child module automatically inherits any root variable that shares the same name — no explicit assignment is needed; (3) Resources inside the child module reference `var.<name>` as usual
D) (1) Resources inside the child module declare the values they need inline; (2) Terraform infers which root variables to pass based on matching names; (3) The root module `module` block is optional if the variable names match

---

### Question 3

**Difficulty:** Easy
**Answer Type:** many
**Topic:** Two correct sequencing facts about module outputs — declaration order and reference syntax

Which TWO of the following correctly describe sequencing facts about Terraform module outputs?

A) A child module must declare an `output` block inside its own `.tf` files BEFORE the root module can reference `module.<name>.<output_name>` — if the child module has no `output` block for a value, that value is invisible to the calling module regardless of what attributes the child's resources expose
B) The root module can reference any attribute of any resource inside a child module directly using `module.<name>.<resource_type>.<resource_name>.<attribute>` — explicit `output` blocks in the child are optional
C) A child module's `output` block must be declared BEFORE its `resource` blocks in the same `.tf` file — if `outputs.tf` is processed after `main.tf`, the output may not resolve correctly
D) Module outputs are resolved sequentially: the child module's `output` block uses a resource attribute expression (e.g., `aws_vpc.main.id`) — this expression is evaluated AFTER the resource has been planned or applied, not before; during planning, the output value may be "(known after apply)" if the resource is being created; after a successful apply, the output holds the real attribute value

---

### Question 4

**Difficulty:** Medium
**Answer Type:** one
**Topic:** Full sequence to consume a Terraform Registry module for the first time

An engineer wants to use the community `terraform-aws-modules/vpc/aws` module in a new configuration. Starting from an empty `main.tf`, which of the following correctly sequences every required step to successfully apply the module?

A) (1) Run `terraform apply` — Terraform downloads the module automatically during apply when it detects a `module` block for the first time
B) (1) Add the `module` block with `source = "terraform-aws-modules/vpc/aws"` and `version = "~> 5.0"` plus required input arguments; (2) Run `terraform init` — Terraform contacts the registry, resolves the version constraint, and downloads the module source to `.terraform/modules/`; (3) Run `terraform plan` — Terraform evaluates the module's resources and generates a proposed execution plan; (4) Review the plan; (5) Run `terraform apply` to create the VPC and its dependent resources
C) (1) Run `terraform init` first (before adding any `module` block) — this pre-fetches available modules; (2) Add the `module` block; (3) Run `terraform plan`; (4) Run `terraform apply`
D) (1) Download the module source from GitHub manually; (2) Place it in `./modules/vpc/`; (3) Change `source` to `"./modules/vpc"`; (4) Run `terraform init`; (5) Run `terraform plan`; (6) Run `terraform apply`

---

### Question 5

**Difficulty:** Medium
**Answer Type:** one
**Topic:** Upgrading a pinned registry module version — `terraform init -upgrade` required, plain `terraform init` is insufficient

An engineer has been using `terraform-aws-modules/vpc/aws` version `~> 4.0` and the module has been cached in `.terraform/modules/`. They update the constraint to `version = "~> 5.0"` in the `module` block. Which of the following correctly sequences what happens when they run `terraform init` WITHOUT the `-upgrade` flag, and what the correct sequence should be to actually get version 5?

A) Running `terraform init` without `-upgrade` always re-downloads modules to the latest version matching the constraint — changing the `version` argument is sufficient to trigger a fresh download
B) (1) Engineer changes `version = "~> 5.0"` in the configuration → (2) Runs `terraform init` without `-upgrade` → (3) Terraform sees the existing cached module, and because a version in the `4.x` range is already cached and the new constraint `~> 5.0` is NOT satisfied by the cached version, Terraform will download the 5.x version — `terraform init` always re-evaluates constraints against the cache and fetches if needed
C) (1) Engineer changes `version = "~> 5.0"` → (2) Runs `terraform init` without `-upgrade` → (3) Terraform may use the previously cached `4.x` version if it is still recorded in the lock file and does not re-evaluate the updated constraint; to force Terraform to download the new version matching `~> 5.0`, the correct sequence is: update the `version` constraint → run `terraform init -upgrade` (the `-upgrade` flag instructs Terraform to re-evaluate version constraints and update the lock file with newer versions) → run `terraform plan`
D) To upgrade a module version, the engineer must delete `.terraform/modules/` entirely, then run `terraform init`, then run `terraform plan` — `terraform init -upgrade` has no effect on module version selection

---

### Question 6

**Difficulty:** Medium
**Answer Type:** one
**Topic:** Creating a local reusable module — the order in which a standard module's files should be created and what each provides

An engineer is authoring a new reusable child module at `./modules/database/`. They want to follow the standard Terraform module structure. Which of the following correctly sequences the logical order in which each standard file is created and why each comes before the next?

A) (1) `main.tf` first — declare resources before you know what variables you need; (2) `variables.tf` second — add variables after you see what's needed; (3) `outputs.tf` last — expose values only after the resource arguments are finalised
B) (1) `variables.tf` — declare the module's input interface first so you know what values the module accepts; (2) `main.tf` — write resources that reference `var.<name>` values you just declared; (3) `outputs.tf` — expose resource attribute values (e.g., `aws_db_instance.main.endpoint`) for callers to consume; (4) `versions.tf` — declare required Terraform and provider version constraints; (5) `README.md` — document the module's purpose, inputs, outputs, and usage examples
C) (1) `README.md` first — document the module before writing any code; (2) `versions.tf`; (3) `outputs.tf` — outputs must be declared before resources so Terraform knows what to expose; (4) `main.tf`; (5) `variables.tf` last — variables are optional and can be added only if needed
D) The file creation order is strictly enforced by Terraform — `versions.tf` must always be processed before `variables.tf` and `main.tf`; Terraform returns an error if these files are created out of order

---

### Question 7

**Difficulty:** Medium
**Answer Type:** one
**Topic:** Git-sourced module with `?ref=` — what happens if you change the ref without re-running `terraform init`

An engineer is using a Git-sourced module:

```hcl
module "firewall" {
  source = "git::https://github.com/acme/infra-modules.git//modules/firewall?ref=v1.2.0"
}
```

They upgrade the ref to `?ref=v1.3.0` in the `source` URL. Which of the following correctly sequences what happens when they run `terraform plan` WITHOUT re-running `terraform init`?

A) `terraform plan` detects the changed `?ref=` value and automatically re-clones the repository at the new ref — no manual `terraform init` is needed because Terraform tracks git refs dynamically
B) `terraform plan` succeeds but uses the previously cached `v1.2.0` code from `.terraform/modules/firewall/` — the plan is silently generated against the old module version; no warning is shown that the source URL has changed
C) `terraform plan` fails with an error indicating that the module source has changed and `terraform init` must be re-run — changing the `?ref=` value (or any part of the `source` URL) is treated as a source change that requires `terraform init` to re-download and cache the new ref before plan can proceed
D) `terraform plan` fails with a Git authentication error — the `?ref=` parameter is a Git fetch argument and can only be evaluated by re-running `terraform init -upgrade`

---

### Question 8

**Difficulty:** Medium
**Answer Type:** one
**Topic:** Nested module output chain — in what order are outputs resolved when a grandchild module's output flows to the root

A root module calls module A, which in turn calls module B (a "grandchild" from the root's perspective). Module B has an `output "subnet_id"` block. Module A has an `output "subnet_id"` block that references `module.b.subnet_id`. The root module outputs `module.a.subnet_id`. During `terraform apply`, which of the following correctly sequences when each output resolves to its final real value?

A) (1) Root module output resolves first using `module.a.subnet_id` → (2) Module A output resolves → (3) Module B creates the subnet and its output resolves last
B) (1) Module B's resources are created first (because they are the deepest dependency) → (2) Module B's `output "subnet_id"` resolves to the real `aws_subnet.main.id` value → (3) Module A's `output "subnet_id"` resolves using `module.b.subnet_id` (now a known value) → (4) Root module's `output "subnet_id"` resolves using `module.a.subnet_id` (now a known value) — outputs propagate UP the module call chain from deepest to shallowest
C) All three outputs resolve simultaneously at the end of apply — Terraform batches all output evaluation into a single post-apply step regardless of nesting depth
D) Module A's outputs resolve first because the root module calls module A directly — module B is processed independently and its output is injected into module A afterward

---

### Question 9

**Difficulty:** Medium
**Answer Type:** many
**Topic:** Two correct sequencing differences between local path and registry module during `terraform init`

Which TWO of the following correctly describe sequencing differences between how a local path module and a Terraform Registry module are handled during `terraform init`?

A) For a **local path module** (`source = "./modules/vpc"`), `terraform init` does NOT download any files — it only records the module path in `.terraform/modules/modules.json`; the module code is read directly from the local filesystem at plan/apply time; for a **registry module** (`source = "terraform-aws-modules/vpc/aws"`), `terraform init` contacts `registry.terraform.io`, resolves the `version` constraint, downloads the full module source tree, and caches it in `.terraform/modules/` — no network call is needed for a local path module, but a registry module REQUIRES network access during `terraform init`
B) For a **local path module**, `terraform init` downloads the files from the local path into `.terraform/modules/` just like it does for registry modules — the only difference is that no version resolution is performed; for a **registry module**, `terraform init` also resolves versions; both types result in an identical cache structure
C) For a **registry module**, `terraform init` must be run BEFORE `terraform plan` — without it, plan fails; for a **local path module**, `terraform plan` can be run without prior `terraform init` because no downloading is required — the files are already present on disk
D) For a **local path module**, changing the files inside the module directory takes effect on the NEXT `terraform plan` without re-running `terraform init` — because `terraform plan` reads the module source directly from the local path; for a **registry module**, changing the cached files in `.terraform/modules/` is overwritten the next time `terraform init` is run — the cached source is managed by Terraform and should not be hand-edited

---

### Question 10

**Difficulty:** Medium
**Answer Type:** one
**Topic:** Replacing a local module with a registry module — complete migration sequence in correct order

A team has been using a hand-authored local module at `./modules/vpc`. They decide to replace it with the community `terraform-aws-modules/vpc/aws` registry module. Which of the following correctly sequences every step of the migration?

A) (1) Delete `./modules/vpc`; (2) Run `terraform destroy` to remove the existing VPC; (3) Replace `source` with the registry reference; (4) Run `terraform init`; (5) Run `terraform apply` to recreate the VPC
B) (1) Update the `module "vpc"` block: replace `source = "./modules/vpc"` with `source = "terraform-aws-modules/vpc/aws"` and add `version = "~> 5.0"`; (2) Align input argument names to match the registry module's expected variables (the local and registry modules may use different variable names); (3) Update any root module references to module outputs (output names may differ between modules); (4) Run `terraform init` — Terraform downloads the registry module; (5) Run `terraform plan` — review carefully; the plan may show resource replacements if argument names or resource naming patterns changed; (6) Run `terraform apply` after confirming the plan is acceptable
C) (1) Run `terraform init` first with the old source still in place; (2) Update `source` to the registry reference; (3) Run `terraform init` again; (4) Run `terraform apply -replace=module.vpc` to force recreation
D) (1) Add a SECOND `module` block for the registry module alongside the existing local module block; (2) Run `terraform init`; (3) Run `terraform apply`; (4) Then delete the local module block and run `terraform apply` again

---

### Question 11

**Difficulty:** Medium
**Answer Type:** one
**Topic:** Module output value timing — "known after apply" during planning vs real value after apply

During `terraform plan`, the root module references `module.networking.vpc_id`, which is the output of a child module that creates a new `aws_vpc` resource. The VPC does not yet exist in state. Which of the following correctly sequences what happens to the `module.networking.vpc_id` value from plan time through apply completion?

A) `module.networking.vpc_id` holds the real VPC ID during `terraform plan` — Terraform pre-fetches resource IDs from AWS during planning so the full dependency graph can be validated; the value is a real AWS resource ID like `vpc-0a1b2c3d`
B) (1) During `terraform plan`: `aws_vpc.main` is planned for creation — its `id` attribute will be assigned by AWS and is not yet known; the child module's `output "vpc_id"` expression resolves to `(known after apply)`; the root module references `module.networking.vpc_id`, which also shows as `(known after apply)` in the plan output — any resource in the root module that uses this value also shows `(known after apply)` for that argument; (2) During `terraform apply`: the VPC is created and AWS assigns it an ID (e.g., `vpc-0a1b2c3d4e5f`); Terraform reads back the ID; the child module output resolves to the real value; downstream resources in the root that depend on `module.networking.vpc_id` receive the real ID and are created in dependency order
C) (1) During `terraform plan`: `module.networking.vpc_id` shows `null` because the VPC does not exist yet; (2) During `terraform apply`: the value transitions from `null` to the real ID — `null` and `(known after apply)` are equivalent in plan output
D) If a child module output depends on a `(known after apply)` resource attribute, `terraform plan` aborts with an error — plans cannot proceed when any module output is unresolvable at plan time

---

### Question 12

**Difficulty:** Hard
**Answer Type:** one
**Topic:** Complete production workflow — discover, evaluate, pin, adopt, and apply a registry module including all intermediate verification steps in correct order

A security-conscious team wants to adopt a Terraform Registry module for the first time in a production environment. Which of the following correctly sequences ALL steps of a responsible adoption workflow, including steps that are often skipped in non-production environments?

A) (1) Add `module` block → (2) Run `terraform apply` directly in production — trusted registry modules do not need review before adoption
B) (1) Search `registry.terraform.io` and review the module's source code, examples, and README for correctness and security posture; (2) Pin the module to a specific version constraint (e.g., `version = "= 5.4.0"` or `"~> 5.4"`) in a non-production environment first — never use an unpinned module in production; (3) Add the `module` block with the pinned source and version and all required inputs; (4) Run `terraform init` to download and cache the module; (5) Run `terraform plan` in a non-production environment and carefully review the proposed resources; (6) Run `terraform apply` in non-production and verify the infrastructure behaves as expected; (7) Lock the exact version in `.terraform.lock.hcl` and commit the lockfile to version control; (8) Promote the same pinned version and lockfile to production; (9) Run `terraform init` in the production workspace (uses lockfile-recorded version); (10) Run `terraform plan` in production and review; (11) Run `terraform apply` in production
C) (1) Add `module` block without a `version` argument — unpinned modules always use the latest version which is inherently the most secure; (2) Run `terraform init`; (3) Run `terraform apply` — the registry guarantees module correctness so no further review is needed
D) (1) Clone the module's GitHub repository; (2) Run a security scan on the source; (3) Copy the module files to a local path; (4) Change `source` to the local path; (5) Remove the `version` argument — local modules do not support `version`; (6) Run `terraform init`; (7) Run `terraform apply` — using a local copy is always preferred over registry modules in production

---

### Question 13

**Difficulty:** Hard
**Answer Type:** many
**Topic:** Two correct sequencing facts distinguishing when module input variables are resolved versus when module outputs are resolved across the plan/apply lifecycle

Which TWO of the following correctly describe sequencing differences between when module INPUT variables are resolved and when module OUTPUT values are resolved during the Terraform plan and apply lifecycle?

A) Module INPUT variables are resolved during `terraform plan` — when Terraform evaluates a `module` block, it immediately resolves all input argument expressions (e.g., `vpc_cidr = var.vpc_cidr`) using values that are already known at plan time (root variable values, literals, and attributes of already-known resources); if an input argument depends on a `(known after apply)` value, the child module receives an unknown input and downstream resources within the child module will also show `(known after apply)` in the plan — input resolution happens at the START of module evaluation, before the child's resources are planned
B) Module OUTPUT values are always fully resolved during `terraform plan` — even for newly created resources, Terraform pre-computes output values by simulating the AWS API response; outputs are never `(known after apply)` in any production plan
C) Module INPUT variables are resolved AFTER `terraform apply` completes — they cannot be evaluated during planning because input values may change between plan and apply
D) Module OUTPUT values are resolved AFTER the apply phase of the specific resources that the output expression references — if `output "vpc_id"` references `aws_vpc.main.id` and that VPC is being created in this apply run, the output value is `(known after apply)` during planning and resolves to the real ID only after the VPC resource is applied; this means module outputs that depend on newly created resources become real values LATER in the apply run than module inputs (which are resolved at plan time from already-known expressions)

## Answer Key

| Q# | Answer(s) | Explanation | Source | Difficulty |
|----|-----------|-----------:|--------|------------|
| 1 | B | ** Even for a local path module that requires no download, `terraform init` must be run before `terraform plan` whenever a new `module` block is added (or an existing `source` argument is changed). During `terraform init`, Terraform registers the module path in `.terraform/modules/modules.json`. Without this registration, `terraform plan` immediately errors: "Module not installed. Run `terraform init`." The correct sequence is always: **(1)** add the `module` block; **(2)** run `terraform init` (for a local path this is fast — it just records the path); **(3)** run `terraform plan`; **(4)** run `terraform apply`. Option A is incorrect — `terraform plan` does not install modules. Option C is incorrect — `terraform apply` does not install modules either. Option D is incorrect — manually copying files to `.terraform/modules/` does not create the required `modules.json` registration, and Terraform would still fail. | ** `terraform init` must come BEFORE `terraform plan` whenever a new module block is added | ** Easy |
| 2 | B | ** Module input variables follow a strict three-step flow: **(1) Declaration** — the child module defines what inputs it accepts by declaring `variable` blocks in its own `.tf` files (conventionally `variables.tf`). **(2) Assignment** — the root module (or any calling module) must explicitly assign values to those inputs inside the `module` block: `environment = var.environment`. Terraform NEVER automatically inherits variables from parent to child — name matching is irrelevant. **(3) Consumption** — resources inside the child module reference the assigned value using standard `var.<name>` syntax. This explicit, declared-at-the-boundary design is intentional: it makes module interfaces clear and prevents accidental coupling between parent and child scope. A child variable with no default and no assignment from the caller causes a `terraform init`/`plan` error about a missing required argument. | ** Module input variable flow — declared in child, explicitly assigned in root, used by child resources | ** Easy |
| 3 | A, D | ** **(A)** Child module resources are encapsulated — their attributes are NOT directly accessible from the calling module. The ONLY values a child module exposes are those declared in explicit `output` blocks. If `aws_vpc.main.id` is not exposed via an `output` block, `module.networking.vpc_id` is undefined and causes a reference error. The output declaration must exist in the child module's code before the caller can reference it. **(D)** A child module output expression like `value = aws_vpc.main.id` is evaluated relative to the Terraform lifecycle: during `terraform plan` for a resource being created for the first time, `aws_vpc.main.id` is computed/unknown — the module output will show as `(known after apply)` in the plan. After `terraform apply` completes, the VPC has been created, its `id` attribute is populated, and the module output holds the real string. Option B is false — direct cross-module resource references are not supported; outputs are required. Option C is false — Terraform processes all `.tf` files in a directory as a single unit and file ordering within the directory does not determine evaluation order. | ** Two correct sequencing facts about module outputs — declaration order and reference syntax | ** Easy |
| 4 | B | ** Consuming a Terraform Registry module follows this sequence: **(1) Add the `module` block** in your configuration with the three-part registry source (`terraform-aws-modules/vpc/aws`), a `version` constraint, and all required input arguments. The `version` argument is only valid for registry sources, not local paths or Git URLs. **(2) Run `terraform init`** — this is the download step. Terraform contacts `registry.terraform.io`, resolves the version constraint against published releases, downloads the module source code, and caches it in `.terraform/modules/vpc/`. The module is also recorded in `.terraform/modules/modules.json`. **(3) Run `terraform plan`** — now that the module is installed, Terraform can evaluate its resource configurations and produce a plan. **(4) Review the plan** — verify that the proposed resources match expectations. **(5) Run `terraform apply`** — Terraform creates the VPC and all resources the module provisions. Omitting `terraform init` after adding the `module` block causes an "Module not installed" error at plan time. | ** Full sequence to consume a Terraform Registry module for the first time | ** Medium |
| 5 | C | ** Terraform uses a lock file (`.terraform.lock.hcl`) to record the exact versions of providers and modules that were selected. When you run `terraform init` without `-upgrade`, Terraform respects the existing lock file entries and will NOT automatically upgrade to a newer version even if the constraint now allows it. The correct sequence to upgrade a module version is: **(1)** Update `version = "~> 5.0"` in the `module` block. **(2)** Run `terraform init -upgrade` — the `-upgrade` flag tells Terraform to re-evaluate all version constraints against the registry/source, download newer qualifying versions, and update `.terraform.lock.hcl` to record the new selections. **(3)** Run `terraform plan` — now the plan is generated using the 5.x module code. Without `-upgrade`, Terraform is conservative and prefers the already-cached version to ensure reproducibility. Simply changing the constraint without `-upgrade` may still use the old version depending on what is locked. | ** Upgrading a pinned registry module version — `terraform init -upgrade` required, plain `terraform init` is insufficient | ** Medium |
| 6 | B | ** While Terraform processes all `.tf` files in a directory as a single logical unit (file order does not affect evaluation), the LOGICAL authoring sequence for a well-structured module follows the data flow: **(1) `variables.tf`** — define the module's input interface first. This clarifies what parameters callers must (or can) provide and gives you a clear contract to code against. **(2) `main.tf`** — write resource and data source blocks that reference `var.<name>` values declared in step 1. Having the variable declarations first means resources can be written against a known interface. **(3) `outputs.tf`** — once resources are defined, identify which attributes callers need and expose them via `output` blocks that reference resource attributes (e.g., `aws_db_instance.main.endpoint`). **(4) `versions.tf`** — add `terraform` and `required_providers` blocks to lock the minimum Terraform and provider versions the module needs. **(5) `README.md`** — document the module's purpose, inputs, outputs, and usage examples so consumers understand how to call it. Option D is false — Terraform imposes no file ordering within a directory; all `.tf` files are merged before evaluation. | ** Creating a local reusable module — the order in which a standard module's files should be created and what each provides | ** Medium |
| 7 | C | ** Changing any part of a module `source` URL — including the `?ref=` query parameter — constitutes a source change. `terraform plan` (and `terraform apply`) do NOT automatically re-download module sources. They rely entirely on the already-cached module code in `.terraform/modules/`. When Terraform detects that the recorded source URL in `modules.json` no longer matches the `source` argument in the configuration, it reports an error and instructs the engineer to run `terraform init`. The correct sequence after changing `?ref=v1.2.0` to `?ref=v1.3.0` is: **(1)** Update the `source` URL in the `module` block. **(2)** Run `terraform init` — Terraform re-clones the repository checking out the new `v1.3.0` tag and updates `.terraform/modules/`. **(3)** Run `terraform plan` — the plan is now generated against the new module code. This requirement prevents silent version drift: the plan you see always corresponds to the module code that was explicitly installed. | ** Git-sourced module with `?ref=` — what happens if you change the ref without re-running `terraform init` | ** Medium |
| 8 | B | ** Terraform's dependency graph ensures that deeper modules are applied BEFORE shallower modules when the outputs of one module feed into another. The sequencing follows data flow from the bottom of the call chain to the top: **(1)** Module B's resources (e.g., `aws_subnet.main`) are created first because no other module's output depends on module B — it is the deepest node in the dependency graph. **(2)** After `aws_subnet.main` is created and Terraform reads back its `id`, module B's `output "subnet_id"` resolves to the real subnet ID string. **(3)** Module A's `output "subnet_id"` expression `module.b.subnet_id` can now be evaluated using the real value from step 2 — it resolves. **(4)** The root module's `output "subnet_id"` expression `module.a.subnet_id` resolves using the value from step 3. This bottom-up propagation of output values is the natural consequence of Terraform's directed acyclic graph (DAG) evaluation: producers are always applied before consumers. | ** Nested module output chain — in what order are outputs resolved when a grandchild module's output flows to the root | ** Medium |
| 9 | A, D | ** **(A)** The key distinction is what `terraform init` DOES with each source type. For a local path module, `terraform init` simply records the path in `modules.json` — no file copying, no network call. The actual `.tf` files are read from the local filesystem at plan time. For a registry module, `terraform init` performs a full download: it contacts the registry API, resolves the version constraint, and copies the module source to `.terraform/modules/<name>/`. Network connectivity is required. **(D)** A direct consequence of the no-copy behavior for local modules: if you edit a file inside `./modules/vpc/`, the next `terraform plan` sees your change immediately — no `terraform init` re-run is needed (unless the `source` argument itself changes). For a registry module, the cached copy in `.terraform/modules/` is considered authoritative. Terraform does not re-download on every plan. If the registry module source changes, you must run `terraform init` again (with `-upgrade` if upgrading the version). Option B is false — local path modules are NOT copied into `.terraform/modules/`. Option C is false — local path modules also require `terraform init` before plan; the registration step is still mandatory. | ** Two correct sequencing differences between local path and registry module during `terraform init` | ** Medium |
| 10 | B | ** Migrating from a local module to a registry module is a multi-step process that must respect both Terraform mechanics and the risk of unintended resource changes. The correct sequence: **(1) Update the `module` block** — change `source` to the three-part registry format and add a `version` constraint. **(2) Align input arguments** — the local module's variable names may not match the registry module's interface (e.g., local `vpc_cidr` vs registry `cidr`). Mismatched inputs cause `terraform init`/`plan` errors. **(3) Update output references** — if the root module references child module outputs (`module.vpc.vpc_id`), verify those output names match what the registry module exposes. **(4) Run `terraform init`** — downloads the registry module to `.terraform/modules/`. **(5) Run `terraform plan`** — CRITICAL step. Because the local and registry modules may use different internal resource naming, Terraform may plan to DESTROY and RECREATE resources (e.g., the VPC). Review the plan carefully before applying. **(6) Run `terraform apply`** only after confirming the plan is safe — use `moved` blocks or `terraform import` if Terraform plans to recreate resources that should be adopted in place. | ** Replacing a local module with a registry module — complete migration sequence in correct order | ** Medium |
| 11 | B | ** The sequence captures a fundamental aspect of Terraform's planning model: **(1) Plan time** — `aws_vpc.main` is a new resource. Its `id` attribute will be assigned by AWS after creation, so it is a "computed" attribute — unknown before apply. The child module's `output "vpc_id"` expression `aws_vpc.main.id` therefore evaluates to `(known after apply)`. The parent's reference `module.networking.vpc_id` inherits this unknown status. In the plan output, any resource argument using this value also shows `(known after apply)`. Terraform does NOT abort — it represents unknown values with a special sentinel and continues planning downstream resources with the understanding that the actual value will be resolved during apply. **(2) Apply time** — Terraform creates `aws_vpc.main` first (because downstream resources depend on it). AWS assigns the real ID. Terraform reads back the attribute, the child module output resolves to `vpc-0a1b2c3d4e5f`, and all downstream resources in the root module that depend on this value receive the real ID and are created in the correct dependency order. The "known after apply" sentinel is a plan-only concept — it never appears in the actual state file. | ** Module output value timing — "known after apply" during planning vs real value after apply | ** Medium |
| 12 | B | ** A production-grade module adoption sequence addresses three concerns: safety, reproducibility, and promotion. **(1) Review** — before writing any code, read the module's source, understand what resources it creates, and check for security posture (e.g., does it open 0.0.0.0/0 by default?). The registry hosts third-party modules — they are not automatically vetted by HashiCorp unless marked "Verified". **(2) Pin to a specific version** — production infrastructure should never use a floating `version` constraint (`>= 5.0`) or, worse, no constraint at all, because a new module release could change resource configurations unexpectedly. **(3) Non-production first** — adopt in dev/staging before production to verify behavior. **(4) terraform init** — downloads the module. **(5) terraform plan** — review the proposed resources carefully. **(6) terraform apply in non-production** — validate functional correctness. **(7) Commit the lockfile** — `.terraform.lock.hcl` records the exact module version; committing it ensures every team member and CI system uses the identical version. **(8-11) Promote to production** — use the same version and lockfile so production mirrors non-production exactly. Option C is insecure — unpinned modules drift. Option D introduces manual maintenance burden and loses the version-constraint safety net. | ** Complete production workflow — discover, evaluate, pin, adopt, and apply a registry module including all intermediate verification steps in correct order | ** Hard |
| 13 | A, D | ** **(A)** Module input variables are evaluated at plan time as part of the module call evaluation. When Terraform evaluates the `module` block, it immediately resolves all input argument expressions from the calling scope. Inputs that come from root variables, literals, or already-known resource attributes are fully resolved during planning — the child module's resources are planned with these known input values. Inputs that depend on `(known after apply)` values propagate that unknown status into the child module, causing the child's resources to also show unknown values in the plan. The key timing fact: inputs are resolved at the BEGINNING of child module evaluation, which happens during `terraform plan`. **(D)** Module output values reference resource attributes that may themselves be computed (unknown until apply). When a module output references a newly-created resource's ID, the output is `(known after apply)` during planning. The output value only becomes a real, concrete value during the apply phase — specifically, after the resource the output depends on has been applied and its attribute is populated. This creates a clear timing difference: inputs are resolved at PLAN time (from the calling scope), while outputs that depend on computed attributes are resolved at APPLY time (after the resources they reference are created). Option B is false — module outputs CAN be `(known after apply)` when they reference newly created resources. Option C is false — inputs are fully resolvable at plan time for non-computed values. | ** Two correct sequencing facts distinguishing when module input variables are resolved versus when module outputs are resolved across the plan/apply lifecycle | ** Hard |
