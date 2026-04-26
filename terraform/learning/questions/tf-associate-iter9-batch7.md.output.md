# Terraform Associate Exam Questions

---

### Question 1

**Difficulty:** Easy
**Answer Type:** one
**Topic:** `terraform get` vs `terraform init` for module installation — which statement is FALSE?

Which of the following statements about the `terraform get` command is FALSE?

A) `terraform get` downloads and installs module sources into `.terraform/modules/` — it performs the same module-caching work that `terraform init` performs for modules
B) `terraform get` is a standalone command that downloads module sources but does NOT install or update providers — to install providers, a full `terraform init` (or `terraform init -upgrade`) is still required
C) `terraform get` also installs required providers defined in `terraform { required_providers {} }` blocks — because modules often declare their own required providers, `terraform get` automatically resolves and installs those providers at the same time to keep the local cache consistent
D) Running `terraform init` performs a superset of what `terraform get` does — `terraform init` installs providers, initialises the backend, AND downloads modules; `terraform get` handles only the module download step

---

### Question 2

**Difficulty:** Easy
**Answer Type:** one
**Topic:** Standard module file naming convention — which statement is TRUE?

Which of the following statements about the standard file structure for a publishable Terraform module is TRUE?

A) Terraform enforces a mandatory file structure — a module MUST contain exactly three files named `main.tf`, `variables.tf`, and `outputs.tf`; any other filenames cause `terraform init` to ignore the module directory
B) The standard module file structure (`main.tf`, `variables.tf`, `outputs.tf`, `versions.tf`, `README.md`) is a **convention** recommended for readability and registry publishing — Terraform itself does not enforce specific filenames; any `.tf` file in the directory is processed equally regardless of name; multiple `.tf` files are merged into a single logical configuration
C) `variables.tf` and `outputs.tf` are special filenames that Terraform processes before `main.tf` — this processing order is guaranteed and means input variables are always resolved before resource blocks are evaluated
D) The `versions.tf` file, which contains the `terraform { required_providers {} }` block, must exist in the module root directory — placing `required_providers` in `main.tf` is not supported and causes a provider resolution error

---

### Question 3

**Difficulty:** Easy
**Answer Type:** many
**Topic:** `count` and `for_each` meta-arguments on module blocks — which TWO statements are TRUE?

Which TWO of the following statements about using `count` and `for_each` on a `module` block are TRUE?

A) `count` and `for_each` are NOT valid meta-arguments on `module` blocks — they are supported only on `resource` and `data` blocks; applying them to a `module` block causes a syntax error
B) When `for_each = { prod = "10.0.0.0/16", dev = "10.1.0.0/16" }` is set on a module block, Terraform creates two module instances; inside the module, `each.key` and `each.value` are available just as they are in a `for_each` resource; the instances are addressed as `module.<name>["prod"]` and `module.<name>["dev"]`
C) When `count = 3` is set on a module block, Terraform creates three separate module instances; the instances are addressed as `module.<name>[0]`, `module.<name>[1]`, and `module.<name>[2]`, and `count.index` is available inside the module for distinguishing instances
D) `for_each` on a module block requires that the module itself contain no resources — only data sources are permitted inside a module instantiated with `for_each`

---

### Question 4

**Difficulty:** Medium
**Answer Type:** one
**Topic:** `depends_on` on a module block — which statement is TRUE?

Which of the following statements about using `depends_on` in a `module` block is TRUE?

A) `depends_on` is not supported on `module` blocks — it can only be used on `resource` blocks; adding `depends_on` to a module block causes a `terraform init` error
B) `depends_on` on a `module` block should be used routinely for all module relationships — Terraform recommends explicitly declaring all inter-module dependencies using `depends_on` to ensure correct ordering, even when output-to-input relationships already establish the order
C) `depends_on` on a `module` block instructs Terraform to apply the entire target module **after** the listed resources or modules have been applied — it is specifically intended for cases where a module depends on something that Terraform CANNOT detect automatically (a "hidden dependency"), such as a resource whose output is not directly referenced by any module input but whose side effects must complete first
D) `depends_on` on a `module` block has no effect when both dependencies are in the same Terraform root module — it only controls ordering between root modules in a workspace with multiple configurations

---

### Question 5

**Difficulty:** Medium
**Answer Type:** one
**Topic:** `.terraform.lock.hcl` and module version tracking — which statement is FALSE?

Which of the following statements about the `.terraform.lock.hcl` file and module versions is FALSE?

A) The `.terraform.lock.hcl` file tracks **provider** version selections — it records the exact provider version resolved by `terraform init` and the provider's checksums so that subsequent `terraform init` runs on any machine reproduce the same provider version
B) The `.terraform.lock.hcl` file records the resolved versions of **Terraform Registry modules** in addition to providers — this means that after `terraform init`, both the exact provider versions AND the exact module versions are pinned in the lock file, and all team members will use the identical module and provider versions when they run `terraform init`
C) Module version pinning for Terraform Registry modules is NOT managed by `.terraform.lock.hcl` — module versions are resolved each time `terraform init` runs based on the `version` constraint in the `module` block; the resolved version is cached in `.terraform/modules/modules.json` but is NOT recorded in the lock file; to ensure reproducible module versions, the `version` constraint in the `module` block should be as specific as possible (e.g., `"= 5.1.0"`)
D) The `.terraform.lock.hcl` file should be committed to version control — committing it ensures consistent provider versions across all team members and CI/CD environments; `terraform init -upgrade` is used to intentionally update the lock file to newer provider versions

---

### Question 6

**Difficulty:** Medium
**Answer Type:** one
**Topic:** Addressing module resources in Terraform commands — which statement is TRUE?

Which of the following statements about how module resources are addressed in Terraform CLI commands is TRUE?

A) Resources inside a module are addressed using the format `module.<module_name>.<resource_type>.<resource_name>` — for example, `module.networking.aws_vpc.main`; this address is used in `terraform state list`, `terraform state show`, `terraform taint`, `terraform destroy -target`, and similar commands
B) Resources inside a module cannot be targeted individually — `terraform apply -target` can only reference top-level root module resources; entire modules must be applied as a unit
C) Resources inside a module are addressed the same way as root-module resources — `aws_vpc.main` regardless of which module declares them; the module name is omitted from addresses in all CLI commands
D) The module resource address format uses a colon separator: `module:<module_name>:<resource_type>:<resource_name>` — the colon syntax is required to distinguish module addresses from root-level resource addresses in command output

---

### Question 7

**Difficulty:** Medium
**Answer Type:** one
**Topic:** Module `providers` meta-argument — which statement is TRUE?

Which of the following statements about the `providers` meta-argument in a `module` block is TRUE?

A) The `providers` argument in a `module` block is used to pass **input variables** to the module — it is an alternative to listing inputs directly in the `module` block and is useful when there are many variables to pass
B) By default, a child module inherits all provider configurations from its parent module — no explicit `providers` argument is needed unless you want the child module to use a **different** provider configuration (for example, a provider aliased to a different region); in that case, `providers = { aws = aws.us-west-2 }` passes the aliased provider to the child module
C) The `providers` argument must be specified in every `module` block — if it is omitted, Terraform raises an error about unresolved provider references inside the child module; there is no default provider inheritance behaviour
D) The `providers` argument accepts only provider aliases — passing a non-aliased default provider using `providers = { aws = aws }` is invalid HCL syntax

---

### Question 8

**Difficulty:** Medium
**Answer Type:** many
**Topic:** Terraform Registry published modules — which TWO statements are TRUE?

Which TWO of the following statements about modules published to the Terraform Registry are TRUE?

A) Any user or organisation can publish a public module to the Terraform Registry — the only requirement is that the module source code lives in a GitHub repository named following the convention `terraform-<PROVIDER>-<NAME>` (e.g., `terraform-aws-vpc`); modules from other version control systems (GitLab, Bitbucket) cannot be published to the public registry
B) Published registry modules support the `version` argument in the calling `module` block, allowing operators to use constraint expressions such as `"~> 5.0"` (compatible with 5.x), `">= 4.0, < 6.0"` (range), or `"= 5.1.0"` (exact pin) — the Terraform Registry serves as the version resolver
C) Terraform private registries (available through HCP Terraform and Terraform Enterprise) allow organisations to publish modules internally — these private modules use the same `<NAMESPACE>/<MODULE>/<PROVIDER>` source format and `version` argument as public registry modules, but are only accessible to authenticated members of the organisation
D) When a `module` block references a Terraform Registry module without specifying a `version` argument, `terraform init` always downloads the oldest published version to ensure maximum backwards compatibility — operators must explicitly set a `version` constraint to get a newer version

---

### Question 9

**Difficulty:** Medium
**Answer Type:** one
**Topic:** Passing a child module output as an input to another child module — which statement is TRUE?

Which of the following statements about passing one child module's output as an input to another child module in the root configuration is TRUE?

A) Module outputs can only be passed to `resource` blocks in the root module — they cannot be passed directly as inputs to other `module` blocks; if a value from module A needs to reach module B, it must first be assigned to a local value in the root module
B) The root module can directly pass a child module's output as an input to another child module by referencing `module.<source_module>.<output_name>` in the receiving module's `module` block argument — Terraform automatically determines the correct dependency ordering: module B will not be evaluated until module A has completed, because module B's input depends on module A's output
C) Passing a child module's output to another child module creates a circular dependency and is always rejected by Terraform's configuration validation
D) Module A's output can be passed to module B's input only if both modules are in the same local directory — cross-directory module output composition is not supported

---

### Question 10

**Difficulty:** Medium
**Answer Type:** one
**Topic:** `terraform init -upgrade` and module versions — which statement is FALSE?

Which of the following statements about `terraform init -upgrade` and module version resolution is FALSE?

A) `terraform init -upgrade` causes Terraform to re-evaluate all `version` constraints for Terraform Registry modules and download the latest version that satisfies each constraint, replacing any previously cached module version in `.terraform/modules/`
B) For local path modules, `terraform init -upgrade` performs a full module re-download from a remote source — because local modules can change at any time, `-upgrade` forces Terraform to fetch the latest code from the original remote registry location to ensure the cached copy is current
C) `terraform init -upgrade` also upgrades provider versions — it consults the `version` constraints in `required_providers` blocks and the lock file, updates the lock file to the latest satisfying provider versions, and downloads the new provider binaries
D) `terraform init -upgrade` is the recommended command to explicitly adopt a newer minor or patch version of a module or provider when your constraints permit it — after running it, the updated selections should be reviewed and committed to version control

---

### Question 11

**Difficulty:** Hard
**Answer Type:** one
**Topic:** Four statements about module `for_each` instance addressing — only ONE is TRUE

Four statements about how `for_each` module instances are addressed in Terraform are presented below. Which is the ONLY TRUE statement?

A) When `for_each` is set on a module block, all instances share a single address — Terraform identifies individual instances internally but they are all listed under `module.<name>` without a key suffix; this is why `terraform state list` shows `module.vpc` rather than `module.vpc["prod"]`
B) When `for_each = toset(["prod", "dev"])` is set on a module block, the module instances are addressed as `module.<name>["prod"]` and `module.<name>["dev"]`; referencing a specific instance's output in the root module uses `module.<name>["prod"].<output_name>`; in `terraform apply -target`, the correct flag to target only the prod instance is `-target='module.vpc["prod"]'`
C) Module `for_each` instances are addressed using numeric indices regardless of whether `for_each` was given a map or a set — Terraform converts all `for_each` collections to indexed lists internally; `module.vpc[0]` and `module.vpc[1]` are always the correct addressing format
D) When `for_each` is used on a module block, the `each.key` and `each.value` references are only available in the root module's `module` block argument list — resources inside the child module CANNOT access `each.key` or `each.value`; child module resources must use input variables to receive the key values

---

### Question 12

**Difficulty:** Hard
**Answer Type:** many
**Topic:** Module meta-arguments — which TWO statements are TRUE?

Which TWO of the following statements about module meta-arguments (`count`, `for_each`, `depends_on`, `providers`, `version`) are TRUE?

A) The `version` meta-argument is valid on `module` blocks that use EITHER a Terraform Registry source OR a Git-based source — for Git sources, `version` is interpreted as a semantic version constraint and matched against the repository's release tags
B) All five module meta-arguments (`count`, `for_each`, `depends_on`, `providers`, `version`) can be used simultaneously on the same `module` block — there are no restrictions on combining them
C) `count` and `for_each` are mutually exclusive on a module block — a single module block cannot use both at the same time; attempting to set both `count` and `for_each` on the same `module` block causes a Terraform configuration error
D) The `providers` meta-argument in a module block maps the child module's **required provider names** to provider configurations in the calling module — if a child module has `required_providers { aws = { source = "hashicorp/aws" } }`, the parent can map it using `providers = { aws = aws.us-west-2 }` to supply an aliased provider to the child

---

### Question 13

**Difficulty:** Hard
**Answer Type:** one
**Topic:** Four statements about how Terraform modules handle provider requirements — only ONE is TRUE

Four statements about provider requirements and module composition are presented below. Which is the ONLY TRUE statement?

A) A child module MUST redeclare all providers it uses in its own `terraform { required_providers {} }` block — if a child module uses `aws_instance` without declaring `hashicorp/aws` as a required provider, `terraform init` resolves no provider for the child module and the configuration errors
B) When a child module does NOT declare `required_providers`, Terraform automatically discovers all provider requirements by inspecting which resource types the module uses and resolves the appropriate provider versions from the registry — no explicit provider declaration is needed anywhere in the module tree
C) A child module should declare its own `required_providers` specifying the providers it uses and their minimum version constraints — this is best practice because it documents the module's requirements, enables independent version validation, and ensures that callers who install the module via `terraform init` get a compatible provider version; the root module's lock file still governs the actual installed version, but the child's declaration constrains what is acceptable
D) Provider requirements declared in a child module's `required_providers` are completely ignored by the root module — only the root module's `required_providers` block affects provider version resolution; child module `required_providers` declarations exist solely for documentation purposes and have no effect on `terraform init`

## Answer Key

| Q# | Answer(s) | Explanation | Source | Difficulty |
|----|-----------|-----------:|--------|------------|
| 1 | C | ** Option C is FALSE. `terraform get` performs ONLY the module download step — it does NOT install providers or configure the backend. Its scope is strictly limited to populating `.terraform/modules/` with module source code. Provider installation is handled exclusively by `terraform init`. Option B is TRUE — this is the defining characteristic of `terraform get`. Option A is TRUE for the module portion of `terraform init`'s work. Option D is TRUE — `terraform init` is a superset: it handles backend initialisation, provider installation, and module downloads, while `terraform get` handles only the last part. In practice, `terraform init` is used almost exclusively; `terraform get` is rarely needed standalone. | ** `terraform get` vs `terraform init` for module installation — which statement is FALSE? | ** Easy |
| 2 | B | ** The file names `main.tf`, `variables.tf`, `outputs.tf`, `versions.tf`, and `README.md` are a widely adopted **convention**, not a Terraform requirement. Terraform processes all `.tf` files in a directory as a single logical configuration unit — file names carry no semantic meaning to the Terraform engine. You could put all resources, variables, and outputs in a single `everything.tf` file and it would work identically. The standard names are recommended because they make the module's structure immediately understandable to other engineers and are expected by the Terraform Registry for module documentation. Option A is false — Terraform imposes no file naming rules. Option C is false — Terraform does not use file processing order; all `.tf` files are merged into one configuration graph. Option D is false — `required_providers` can appear in any `.tf` file in the module root. | ** Standard module file naming convention — which statement is TRUE? | ** Easy |
| 3 | B, C | ** **(B)** is TRUE. `for_each` is fully valid on `module` blocks. When a map or set is provided, Terraform creates one module instance per element. Each instance is addressed with the map key as its index: `module.vpc["prod"]` and `module.vpc["dev"]`. Within the module, `each.key` and `each.value` are available for use in resource arguments, just as in `for_each` resources. **(C)** is TRUE. `count` is also valid on `module` blocks. Each instance is numerically indexed: `module.vpc[0]`, `module.vpc[1]`, `module.vpc[2]`. `count.index` is available inside the module for distinguishing instances. **(A)** is FALSE — `count` and `for_each` ARE supported on `module` blocks; this is an officially documented feature. **(D)** is FALSE — there is no restriction on resource types inside a module instantiated with `for_each`; all resource types are permitted. | ** `count` and `for_each` meta-arguments on module blocks — which TWO statements are TRUE? | ** Easy |
| 4 | C | ** `depends_on` is valid on `module` blocks and is the correct mechanism for expressing **hidden dependencies** — ordering requirements that Terraform cannot infer automatically from data flow. For example, if a module provisions EC2 instances but relies on an IAM policy that was created in another resource block without any attribute reference creating a graph edge, `depends_on` can explicitly declare that the module must wait. However, `depends_on` should be used sparingly and only for genuine hidden dependencies — overuse defeats Terraform's ability to parallelise and can mask design problems. Option A is false — `depends_on` IS valid on module blocks. Option B is false — using `depends_on` "routinely" is discouraged; Terraform automatically infers dependencies from output-to-input references, which is always preferred. Option D is false — `depends_on` applies within a single root module configuration and affects resource graph ordering within that module. | ** `depends_on` on a module block — which statement is TRUE? | ** Medium |
| 5 | B | ** Option B is FALSE. The `.terraform.lock.hcl` file tracks **provider** versions and checksums ONLY — it does NOT record module version selections. Module version resolution is handled separately: the version constraint in the `module` block guides `terraform init`, and the resolved version is cached in `.terraform/modules/modules.json` (which is typically NOT committed to version control). There is no module equivalent of the provider lock file. To ensure reproducible module versions, use a tight `version` constraint (e.g., `version = "= 5.1.0"`) or use a Git source with `?ref=` pinned to a specific tag or commit. Option A correctly describes what the lock file does track. Option C correctly explains the module version resolution mechanism. Option D correctly describes the commit-to-VCS recommendation for the lock file. | ** `.terraform.lock.hcl` and module version tracking — which statement is FALSE? | ** Medium |
| 6 | A | ** Module resources are addressed in the Terraform CLI using the dot-separated format `module.<module_name>.<resource_type>.<resource_name>`. For example, `terraform state show module.networking.aws_vpc.main` shows the state entry for the `aws_vpc.main` resource inside the `networking` module. For `for_each` module instances, the address includes the key: `module.vpc["prod"].aws_subnet.main`. This addressing scheme is used consistently across all commands that accept resource addresses: `terraform state list`, `terraform state show`, `terraform state mv`, `terraform destroy -target`, `terraform apply -target`, and `terraform taint`. Option B is false — individual module resources CAN be targeted with `-target` using the full module address. Option C is false — the module name is always part of the address for module-owned resources. Option D is false — colons are not used in Terraform resource addresses. | ** Addressing module resources in Terraform commands — which statement is TRUE? | ** Medium |
| 7 | B | ** By default, Terraform automatically passes the default (non-aliased) provider configurations from the calling module to child modules. No `providers` argument is needed for the common case. The `providers` meta-argument is required only when you want to pass a **different** provider configuration to the child — most commonly a provider alias. A typical use case is a child module that manages resources in a non-default AWS region: `providers = { aws = aws.us-west-2 }` maps the child module's `aws` provider to the parent's aliased `aws.us-west-2` configuration. Option A is false — `providers` is strictly for passing provider configurations, not input variables. Option C is false — provider inheritance is automatic; `providers` is optional. Option D is false — passing the default, non-aliased provider with `providers = { aws = aws }` is valid and sometimes used to be explicit. | ** Module `providers` meta-argument — which statement is TRUE? | ** Medium |
| 8 | B, C | ** **(B)** is TRUE. Registry-sourced modules support version constraints via the `version` argument. Constraint expressions follow the same syntax as provider version constraints: `~>` for compatible versions (pessimistic constraint), range expressions with `>=` and `<`, and exact pins with `=`. The registry resolves the constraint against published module versions and downloads the highest version that satisfies the constraint. **(C)** is TRUE. HCP Terraform and Terraform Enterprise both support private module registries. Private modules use the identical three-part `<NAMESPACE>/<MODULE>/<PROVIDER>` source format and the `version` argument — the only difference is that they are access-controlled and only available to authenticated users of that organisation. **(A)** is partially true but incorrect on the VCS restriction — the Terraform Registry supports GitHub as the primary VCS for module publishing, but GitLab and Bitbucket are also supported for the public registry. **(D)** is FALSE — when no `version` is specified, `terraform init` downloads the **latest** published version, not the oldest. This is why specifying a `version` constraint is recommended for production configurations. | ** Terraform Registry published modules — which TWO statements are TRUE? | ** Medium |
| 9 | B | ** The root module can compose child modules by wiring one module's output directly to another module's input. For example: `module "compute" { source = "./modules/compute"; subnet_id = module.networking.public_subnet_id }` passes the `public_subnet_id` output from the `networking` module as an input to the `compute` module. Terraform's dependency graph automatically infers that `compute` depends on `networking` — because `compute`'s input contains a reference to `networking`'s output, Terraform knows to apply `networking` first and `compute` second. This is the idiomatic way to compose Terraform modules and is strongly preferred over explicit `depends_on` when a genuine data dependency exists. Option A is false — module outputs CAN be passed directly to other module blocks. Option C is false — A → B chaining is not circular; circular would be A → B → A. Option D is false — modules from any source (local, registry, Git) can be composed this way. | ** Passing a child module output as an input to another child module — which statement is TRUE? | ** Medium |
| 10 | B | ** Option B is FALSE. Local path modules have no remote source to download from — they ARE the source (a directory on the local filesystem). `terraform init -upgrade` has no special effect on local path modules because there is nothing to upgrade from a remote location; the files on disk ARE the current version. Running `terraform init` or `terraform init -upgrade` for a local path module simply re-registers the path in `.terraform/modules/modules.json` — no downloading or version comparison occurs. Option A is TRUE — `-upgrade` refreshes Terraform Registry module version resolution and re-downloads if a newer satisfying version is available. Option C is TRUE — `-upgrade` also applies to providers, updating the lock file. Option D is TRUE — this is the intended workflow for deliberately adopting new versions while respecting constraints. | ** `terraform init -upgrade` and module versions — which statement is FALSE? | ** Medium |
| 11 | B | ** **(B)** is the ONLY TRUE statement. For `for_each` module instances, the address uses the element key as the instance index, enclosed in square brackets with quotes for string keys: `module.vpc["prod"]`, `module.vpc["dev"]`. Resources inside those instances use the full address `module.vpc["prod"].aws_subnet.main`. The `-target` flag accepts the quoted key syntax: `-target='module.vpc["prod"]'`. Option A is false — Terraform DOES include the key suffix in addresses; `terraform state list` shows `module.vpc["prod"]` and `module.vpc["dev"]` as separate entries. Option C is false — `for_each` instances use the actual map/set keys as indices (string keys), not numeric indices; numeric indices are used by `count`, not `for_each`. Option D is false — `each.key` and `each.value` ARE available inside the child module's resource blocks when the module is instantiated with `for_each`; this is a key feature that allows child module resources to differentiate between instances. | ** Four statements about module `for_each` instance addressing — only ONE is TRUE | ** Hard |
| 12 | C, D | ** **(C)** is TRUE. `count` and `for_each` are mutually exclusive on both `resource` blocks and `module` blocks. Terraform requires you to choose one or the other — you cannot set both simultaneously. Using both causes a configuration error: "The arguments count and for_each are both defined for this module; only one is allowed." **(D)** is TRUE. The `providers` meta-argument maps provider names as understood by the CHILD module (based on the provider's local name in the child's `required_providers`) to provider configurations in the PARENT. This allows a child module designed to use `aws` to receive a specifically aliased provider (e.g., `aws.us-west-2`) from the parent. **(A)** is FALSE — the `version` argument is valid ONLY for Terraform Registry and private registry sources; it causes an error when used with Git-based sources, where `?ref=` is used instead. **(B)** is FALSE — `count` and `for_each` cannot be combined (see C), and `version` is not valid with non-registry sources. | ** Module meta-arguments — which TWO statements are TRUE? | ** Hard |
| 13 | C | ** **(C)** is the ONLY TRUE statement. Best practice for publishable Terraform modules is to declare `required_providers` in a `versions.tf` file, specifying the providers the module uses along with a minimum version constraint. This serves multiple purposes: it documents the module's dependencies, enables the Terraform Registry to display provider requirements, and ensures that `terraform init` validates provider compatibility when the module is consumed. The root module's `.terraform.lock.hcl` governs the exact provider version installed in the workspace, but the child module's `required_providers` contributes its constraints to the overall resolution. **(A)** is false — child modules do NOT MUST redeclare providers; Terraform inherits provider configurations from the root. Missing `required_providers` in a child is valid (though not best practice). **(B)** is false — Terraform does NOT auto-discover providers from resource type names without declarations; while it can infer provider association from resource type prefixes, explicit `required_providers` is needed for version resolution and source specification. **(D)** is false — child module `required_providers` declarations are NOT ignored; they contribute version constraints to the overall provider resolution and are surfaced in registry documentation. | ** Four statements about how Terraform modules handle provider requirements — only ONE is TRUE | ** Hard |
