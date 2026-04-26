# Terraform Associate Exam Questions

---

### Question 1 — `terraform plan` Errors After Adding a New Module Block

**Difficulty**: Easy
**Answer Type**: one
**Topic**: New module source requires terraform init before plan/apply will work

**Question**:
An engineer adds a new module block to an existing configuration:

```hcl
module "dns" {
  source = "./modules/dns"
  zone   = var.hosted_zone
}
```

The `./modules/dns` directory exists and contains valid `.tf` files. The engineer runs `terraform plan` immediately and receives: `Error: Module not installed. Run "terraform init"`. What is the cause and fix?

- A) The `./modules/dns` directory is missing a `main.tf` file — Terraform requires this filename to recognise a local module
- B) Local path modules cannot be used until they are published to the Terraform Registry
- C) **`terraform plan` does not install or register module sources** — even for local path modules, Terraform must record the module in `.terraform/modules/modules.json` before it can be used; this registration happens during `terraform init`; the engineer must run `terraform init` after adding any new `module` block (or changing an existing `source` argument), then run `terraform plan`; `terraform init` for a local path module does not download anything — it simply registers the module path
- D) The error occurs because `./modules/dns` is a relative path — Terraform requires absolute paths for local modules

---

### Question 2 — Child Module Variable Not Receiving Value From Root

**Difficulty**: Easy
**Answer Type**: one
**Topic**: Parent variables are not automatically inherited — must be explicitly passed as module arguments

**Question**:
An engineer has a root module variable:

```hcl
variable "environment" {
  type    = string
  default = "production"
}
```

The child module `modules/tagging/main.tf` also declares a variable named `environment`. The engineer calls the module without passing the variable:

```hcl
module "tagging" {
  source = "./modules/tagging"
}
```

Inside the child module, `var.environment` resolves to `null` (or errors if the child module has no default). The engineer expects the root `var.environment` value to be inherited automatically. What is the cause and fix?

- A) The child module must declare `inherit = true` in its `variable` block to accept values from the parent scope
- B) Variables are only automatically inherited when the child module is in the same directory as the root module
- C) **Terraform does not automatically pass any root module variables to child modules** — every input a child module needs must be explicitly assigned in the `module` block; the naming of a variable in the child module is irrelevant to whether the parent passes it; the fix is to explicitly pass the variable: `module "tagging" { source = "./modules/tagging"; environment = var.environment }`
- D) The issue is that `var.environment` has a `default`, which prevents it from being passed to child modules — only required variables are passed automatically

---

### Question 3 — Module Output Referenced Before It Is Declared in the Child Module

**Difficulty**: Easy
**Answer Type**: one
**Topic**: A module output that was never declared causes a reference error

**Question**:
An engineer calls a module and references one of its outputs:

```hcl
resource "aws_instance" "web" {
  subnet_id = module.networking.public_subnet_id
}
```

Running `terraform plan` fails: `Error: Unsupported attribute — This object does not have an attribute named "public_subnet_id"`. The engineer inspects `modules/networking/outputs.tf` and finds only this output declared:

```hcl
output "subnet_id" {
  value = aws_subnet.public.id
}
```

What is the cause and the two possible fixes?

- A) Module outputs must use the same name as the resource attribute they expose — `subnet_id` cannot expose `aws_subnet.public.id` without renaming the resource
- B) Module outputs are not accessible from the root module — they can only be referenced by other resources within the same child module
- C) **The output is declared as `subnet_id` in the child module, but the root module references `public_subnet_id` — the names do not match**; Terraform resolves module outputs by the exact name declared in the child module's `output` block; the two fixes are: (1) update the child module's `outputs.tf` to declare `output "public_subnet_id"` instead of `output "subnet_id"`, or (2) update the root module reference to `module.networking.subnet_id` to match the existing output name; the best choice depends on which name is more descriptive
- D) The error occurs because `outputs.tf` must be in the root module, not in the child module directory

---

### Question 4 — `version` Constraint Used with a Git URL Causes `terraform init` Error

**Difficulty**: Medium
**Answer Type**: one
**Topic**: The version argument is only valid for registry sources — Git sources use ?ref= instead

**Question**:
An engineer migrates a module source from the Terraform Registry to an internal GitHub repository. They keep the `version` argument:

```hcl
module "vpc" {
  source  = "github.com/acme/terraform-modules//modules/vpc"
  version = "~> 3.0"
  cidr    = var.vpc_cidr
}
```

Running `terraform init` produces: `Error: Invalid module configuration — Cannot use version constraint with a Git source`. What is the cause and fix?

- A) The double-slash `//` in the source path is causing a parse error — replace it with a single slash
- B) Private GitHub repositories require an OAuth token configured in the `credentials` block before `version` can be used
- C) **The `version` argument is only valid for Terraform Registry and private registry sources** — for Git-based sources (including bare GitHub URLs, `git::https://`, and `git::ssh://`), `version` is not supported and causes a `terraform init` error; to pin a Git source to a specific version, use the `?ref=` query parameter in the source URL appended after the path: `"github.com/acme/terraform-modules//modules/vpc?ref=v3.0.0"`; after updating the source URL, remove the `version` argument
- D) The `version` argument syntax `"~> 3.0"` is only valid for provider version constraints — module versions use a different syntax

---

### Question 5 — Module Changes Not Reflected — `terraform init` Not Re-run After Source Change

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Changing a module source or version requires terraform init to update the cache

**Question**:
An engineer bumps a Terraform Registry module version from `~> 4.0` to `~> 5.0`:

```hcl
module "vpc" {
  source  = "terraform-aws-modules/vpc/aws"
  version = "~> 5.0"
}
```

After saving the file, they run `terraform plan`. The plan shows resources and arguments from the `v4.x` module schema — new `v5.x` arguments are not recognised, and the plan appears unchanged from before. What is the cause?

- A) The Terraform Registry caches module versions permanently — once `v4.x` is cached, it is never replaced unless the `.terraform` directory is deleted manually
- B) The `~> 5.0` constraint is ambiguous — use an exact version like `= 5.1.0` so Terraform can resolve the correct version
- C) **Changing a module's `source` or `version` argument requires re-running `terraform init`** to download and cache the new version; `terraform plan` uses the module source already cached in `.terraform/modules/` and does not re-check the version constraint; without running `init`, the plan continues to use the previously downloaded `v4.x` code; the fix is to run `terraform init -upgrade` (or just `terraform init`) to resolve the updated version constraint and download the `v5.x` module
- D) Module version changes only take effect on `terraform apply` — `terraform plan` always uses the previously applied version

---

### Question 6 — Root Module Cannot Access Resources Inside a Child Module Directly

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Module encapsulation — resources inside child modules are not directly accessible from outside

**Question**:
An engineer has a child module `modules/networking` that creates a VPC (`aws_vpc.main`). In the root module, they try to reference the VPC resource directly:

```hcl
output "vpc_arn" {
  value = module.networking.aws_vpc.main.arn
}
```

Running `terraform plan` fails: `Error: Unsupported attribute`. What is the cause and fix?

- A) The VPC resource ARN is not an available attribute on `aws_vpc` — use `id` instead of `arn`
- B) Resources inside child modules must be imported into the root module state before they can be referenced
- C) **Resources inside a child module are encapsulated and not directly accessible from outside the module** — the only values a child module exposes to its callers are explicitly declared `output` blocks; to access `aws_vpc.main.arn` from the root module, the child module's `outputs.tf` must declare an output: `output "vpc_arn" { value = aws_vpc.main.arn }`, and the root module then references `module.networking.vpc_arn`
- D) The correct syntax for accessing a child module resource is `module.networking::aws_vpc.main.arn` — the double-colon operator separates the module address from the resource address

---

### Question 7 — Module Destroyed Unexpectedly After Being Renamed

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Renaming a module block label changes all resource addresses and causes destroy+create

**Question**:
An engineer renames a module block from `"network"` to `"networking"` for clarity:

```hcl
# Before
module "network" { ... }

# After
module "networking" { ... }
```

Running `terraform plan` shows all resources from the module being destroyed and recreated. The engineer did not change any resource configurations inside the module — only the module block label. Why?

- A) Terraform detects that the module source changed and destroys the old module's resources to avoid conflicts
- B) The rename caused a circular dependency in the dependency graph, forcing Terraform to rebuild all resources
- C) **The module block label (`"network"` vs `"networking"`) is part of every resource's state address** — resources inside the module are tracked in state as `module.network.<resource>` and `module.network.<resource>`; when the label changes to `"networking"`, Terraform sees `module.networking.<resource>` addresses with no prior state entries, concludes they are new resources to create, and sees `module.network.<resource>` entries with no configuration, concluding they should be destroyed; the fix is to use a `moved` block to tell Terraform the resources have been relocated without recreating them: `moved { from = module.network to = module.networking }`
- D) Terraform requires `terraform state mv` to be run manually for every resource inside the renamed module before plan will show no changes

---

### Question 8 — `module.vpc` Outputs All Showing as `(known after apply)` at Plan Time

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Module outputs that depend on computed values will be unknown at plan time

**Question**:
A root module calls a VPC module and references one of its outputs for a security group:

```hcl
resource "aws_security_group" "app" {
  vpc_id = module.vpc.vpc_id
}
```

During `terraform plan`, the security group shows `vpc_id = (known after apply)` even though the VPC appears to already exist in state. On closer inspection, the engineer notices that the VPC module also creates a new internet gateway in this run, and `module.vpc.vpc_id` is shown as `(known after apply)`. Why?

- A) Module outputs are always `(known after apply)` — they can never be resolved at plan time
- B) The security group resource's `vpc_id` argument does not support references to module outputs — it must reference the VPC resource directly
- C) **If the module itself is being changed during this plan run** — even if only one internal resource (like the internet gateway) is new — all of the module's outputs may be marked `(known after apply)` if any output value transitively depends on a computed attribute; the root module references `module.vpc.vpc_id`, but if the `vpc_id` output value is derived from an attribute of a resource being created or modified in this apply, it cannot be resolved until apply time; the engineer should check that `module.vpc.vpc_id` is derived from a stable, already-existing resource attribute (e.g., `aws_vpc.main.id`) rather than a newly-computed one
- D) The `(known after apply)` is caused by the security group referencing the module output indirectly — use `module.vpc.vpc_id` in a `locals` block first to materialise the value before it can be used in a resource

---

### Question 9 — TWO Issues That Require Re-running `terraform init` for Modules

**Difficulty**: Medium
**Answer Type**: many
**Topic**: Identifying which module-related changes require terraform init before plan/apply

**Question**:
Which TWO of the following changes to a module configuration require the engineer to run `terraform init` before `terraform plan` will succeed? (Select two.)

- A) Adding a new `locals` block inside an existing child module directory
- B) **Adding a new `module` block with a new `source` argument** — Terraform must install and register the module source in `.terraform/modules/` before it can be used; running `plan` without `init` produces "Module not installed"
- C) Changing a `count` argument on an existing module block from `1` to `2`
- D) **Changing a `module` block's `source` argument to a different URL or path** — when the source changes, Terraform needs to download or re-register the new source; the old cached source in `.terraform/modules/` is no longer correct; `terraform init` resolves and caches the updated source

---

### Question 10 — Module Published to Terraform Registry — `version` Must Be Set

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Using a registry module without a version constraint is risky and may break on future runs

**Question**:
An engineer calls a community module from the Terraform Registry without specifying a `version`:

```hcl
module "vpc" {
  source = "terraform-aws-modules/vpc/aws"
  cidr   = "10.0.0.0/16"
}
```

After several months, they run `terraform init` on a new CI runner and `terraform plan` shows a large number of unexpected changes — new resources, removed arguments, and deprecated warnings. The engineer's configuration has not changed. What is the most likely cause?

- A) Omitting `version` causes Terraform to use the oldest available version rather than the latest — the CI runner resolved a different old version
- B) Terraform Registry modules are immutable once published — the changes must have come from a different provider version, not the module
- C) **Without a `version` constraint, `terraform init` resolves to the latest published version** of the module; over several months, the module may have released a new major version with breaking changes (new required inputs, removed resources, changed defaults); on the original machine, the previously downloaded version was cached, so `plan` was stable; on the new CI runner with an empty `.terraform/modules/` cache, `init` downloaded the latest version, which introduced breaking changes; the fix is to always pin a version constraint: `version = "~> 5.0"` — this ensures `init` resolves a compatible version on any machine
- D) The issue is that `terraform.lock.hcl` was committed to the repository — this file locks modules to old versions and prevents new CI runners from getting the current version

---

### Question 11 — TWO Consequences of Not Declaring an Output in a Child Module

**Difficulty**: Hard
**Answer Type**: many
**Topic**: Child module encapsulation — two effects when a needed value is not declared as an output

**Question**:
An engineer's root module needs to pass a security group ID (created inside a child module) to another resource in the root module. The child module does not declare an `output` for the security group ID. Which TWO of the following are correct descriptions of what happens? (Select two.)

- A) **Terraform raises an error when the root module references `module.<name>.<attr>` for an attribute not declared as an output** — the attribute simply does not exist on the module object; the root module cannot access any value from a child module unless that value is explicitly exported via an `output` block in the child module
- B) The security group ID can still be accessed from the root module using the `data "terraform_remote_state"` data source, which bypasses module encapsulation
- C) **The only fix is to add an `output` block to the child module that exposes the security group ID** — there is no workaround; module encapsulation is enforced at the language level; the output can be declared as `output "security_group_id" { value = aws_security_group.app.id }` in the child module's `outputs.tf`, after which `module.<name>.security_group_id` becomes a valid reference in the root module
- D) The root module can reference the security group ID using `module.<name>.resource.aws_security_group.app.id` — the `resource.` prefix provides direct resource access across module boundaries

---

### Question 12 — Module Refactored Internally — Root Module Plan Shows Replacements

**Difficulty**: Hard
**Answer Type**: one
**Topic**: Internal module resource address changes (due to refactoring) cause unexpected replace plans

**Question**:
An engineer refactors a child module, renaming an internal resource from `aws_subnet.public` to `aws_subnet.public_primary`. No inputs or outputs change. After running `terraform init`, the next `terraform plan` shows the subnet being destroyed and recreated. The engineer expected no infrastructure change since only the name changed. What is the cause and fix?

- A) Terraform always recreates subnets when modules are re-initialised — this is an AWS provider constraint
- B) The `terraform init` command deleted the old subnet state entry as part of module cache refresh
- C) **The resource's state address changed** — inside the module, the resource was previously tracked as `module.<name>.aws_subnet.public`; after renaming, Terraform looks for `module.<name>.aws_subnet.public_primary`, finds no state entry, and plans to create it; simultaneously, it sees `module.<name>.aws_subnet.public` in state with no matching configuration and plans to destroy it; to resolve this without recreating infrastructure, the engineer should add a `moved` block **inside the child module's** `main.tf` or `moved.tf`: `moved { from = aws_subnet.public; to = aws_subnet.public_primary }` — this instructs Terraform to update the state address without modifying the resource
- D) The replacement is caused by the subnet's `cidr_block` being a `ForceNew` attribute — any change to the subnet triggers a replace; the resource name change is unrelated

---

### Question 13 — Private Registry Module Requires Token But Authentication Is Not Configured

**Difficulty**: Hard
**Answer Type**: one
**Topic**: Private registry modules require credentials configured in CLI config or environment

**Question**:
An engineer's team publishes internal modules to a private Terraform registry at `registry.acme.internal`. A new developer clones the repository and runs `terraform init`. The init fails with: `Error: Failed to query available provider mirrors — Could not retrieve module metadata; 401 Unauthorized`. The module block in question is:

```hcl
module "networking" {
  source  = "registry.acme.internal/acme/networking/aws"
  version = "~> 2.0"
}
```

The module works on all other team members' machines. What is the most likely cause and fix?

- A) Private registry hostnames must be registered with HashiCorp before modules hosted on them can be downloaded — the team needs to submit a registration request
- B) The `source` format is wrong for private registries — they require a `private::` prefix
- C) **The new developer has not configured authentication credentials for the private registry** — Terraform uses the CLI configuration file (`~/.terraformrc` on Linux/macOS, `%APPDATA%\terraform.rc` on Windows) to store credentials for private registry hosts; without a `credentials` block containing a valid token for `registry.acme.internal`, all requests to that host return `401 Unauthorized`; the fix is to add the credentials block: `credentials "registry.acme.internal" { token = "<API_TOKEN>" }` — or use the `terraform login registry.acme.internal` command if the registry supports interactive login; team members whose machines already work have this configured locally
- D) The error is caused by the `version = "~> 2.0"` constraint not matching any published version — the developer should use `version = ">= 2.0"` for broader compatibility

## Answer Key

| Q# | Answer(s) | Explanation | Source | Difficulty |
|----|-----------|-----------:|--------|------------|
| 1 | C | N/A | New module source requires terraform init before plan/apply will work | Easy |
| 2 | C | N/A | Parent variables are not automatically inherited — must be explicitly passed as module arguments | Easy |
| 3 | C | N/A | A module output that was never declared causes a reference error | Easy |
| 4 | C | N/A | The version argument is only valid for registry sources — Git sources use ?ref= instead | Medium |
| 5 | C | N/A | Changing a module source or version requires terraform init to update the cache | Medium |
| 6 | C | N/A | Module encapsulation — resources inside child modules are not directly accessible from outside | Medium |
| 7 | C | N/A | Renaming a module block label changes all resource addresses and causes destroy+create | Medium |
| 8 | C | N/A | Module outputs that depend on computed values will be unknown at plan time | Medium |
| 9 | B, D | N/A | Identifying which module-related changes require terraform init before plan/apply | Medium |
| 10 | C | N/A | Using a registry module without a version constraint is risky and may break on future runs | Medium |
| 11 | A, C | N/A | Child module encapsulation — two effects when a needed value is not declared as an output | Hard |
| 12 | C | N/A | Internal module resource address changes (due to refactoring) cause unexpected replace plans | Hard |
| 13 | C | N/A | Private registry modules require credentials configured in CLI config or environment | Hard |
