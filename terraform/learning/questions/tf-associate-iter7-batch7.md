# Terraform Associate (004) — Question Bank Iter 7 Batch 7

**Iteration**: 7
**Iteration Style**: Fill-in-the-blank / complete the HCL — every question presents a partial HCL snippet or partial statement with a `___________` placeholder; select which option correctly fills the blank
**Batch**: 7
**Objective**: 5 — Interact with Terraform Modules
**Generated**: 2026-04-25
**Total Questions**: 13
**Difficulty Split**: 3 Easy / 8 Medium / 2 Hard
**Answer Types**: 10 `one` / 3 `many` / 0 `none`

---

## Questions

---

### Question 1 — Terraform Registry Module Source Format

**Difficulty**: Easy
**Answer Type**: one
**Topic**: The three-part `NAMESPACE/MODULE/PROVIDER` format for a Terraform Registry module source

**Question**:
Complete the `source` argument with the correct Terraform Registry format for the community VPC module published by the `terraform-aws-modules` organisation:

```hcl
module "vpc" {
  source  = "___________"
  version = "~> 5.0"

  name = "my-vpc"
  cidr = "10.0.0.0/16"
}
```

- A) `"aws::vpc::terraform-aws-modules"`
- B) `"registry.terraform.io/terraform-aws-modules/vpc"`
- C) `"terraform-aws-modules/vpc/aws"`
- D) `"module://terraform-aws-modules/vpc/aws"`

**Answer**: C

**Explanation**:
Terraform Registry module sources use the three-part `<NAMESPACE>/<MODULE>/<PROVIDER>` format. The namespace identifies the organisation or user publishing the module, the module name describes what it provisions, and the provider name indicates the target cloud. The default registry (`registry.terraform.io`) is implied — you do not include the hostname in the source string. For the well-known community VPC module, the correct address is `"terraform-aws-modules/vpc/aws"`. Options A and D use fictional prefixes. Option B omits the required provider component of the three-part format.

---

### Question 2 — Child Module Output Block Value

**Difficulty**: Easy
**Answer Type**: one
**Topic**: Completing the `value` argument in a child module output block to expose a resource attribute

**Question**:
Complete the output block inside a child module so it exposes the VPC resource's ID to the parent module:

```hcl
resource "aws_vpc" "main" {
  cidr_block = var.vpc_cidr
}

output "vpc_id" {
  value = ___________
}
```

- A) `var.vpc_id`
- B) `module.main.id`
- C) `output.vpc.id`
- D) `aws_vpc.main.id`

**Answer**: D

**Explanation**:
Inside a child module, resources are referenced by their type and local name — `aws_vpc.main.id` is the standard resource attribute reference. The `output` block exposes this value to the calling (parent) module, which then accesses it using `module.<module_name>.vpc_id`. Option A (`var.vpc_id`) would reference an input variable named `vpc_id`, which is not declared here. Option B (`module.main.id`) would reference a child module named `main`, not a resource. Option C (`output.vpc.id`) is not valid Terraform syntax — outputs in the same module are not referenced with an `output.` prefix.

---

### Question 3 — `terraform init` Module Caching

**Difficulty**: Easy
**Answer Type**: many
**Topic**: What `terraform init` writes for module caching and what `.terraform/modules/` contains

**Question**:
Which **TWO** of the following statements about `terraform init` and module caching are correct?

- A) `terraform init` downloads remote module source code (registry, Git, HTTP) into `.terraform/modules/` in the working directory; a `modules.json` manifest inside this directory maps each module name to its resolved local path
- B) Local path modules (e.g., `source = "./modules/networking"`) are downloaded and physically copied into `.terraform/modules/` just like registry modules — both types are stored in the same cache format
- C) `.terraform/modules/` is only created when at least one Terraform Registry module is referenced — configurations using only local path modules never have this directory
- D) After `terraform init`, subsequent `terraform plan` and `terraform apply` operations read module source code from `.terraform/modules/` (or the original local path for local sources) — they do not contact remote sources again unless `terraform init` is re-run

**Answer**: A, D

**Explanation**:
Two key facts about module caching: (1) `terraform init` creates `.terraform/modules/` and writes a `modules.json` manifest recording every module in the configuration; for **remote** modules (registry, Git, HTTP archive), the source code is also downloaded into subdirectories within `.terraform/modules/` (option A is correct); (2) after init, `terraform plan` and `terraform apply` rely on the locally cached module code and do not re-contact remote sources — re-running `terraform init` is required to refresh a remote module source (option D is correct). Option B is wrong — local path modules are **not** copied; Terraform reads them directly from the `./` path and only registers them in `modules.json`. Option C is wrong — `.terraform/modules/` is created for all configurations that include any `module` block, local or remote.

---

### Question 4 — `~>` Compatible Version Constraint

**Difficulty**: Medium
**Answer Type**: one
**Topic**: What the pessimistic constraint operator `~>` means in a module `version` argument

**Question**:
Complete the explanation: `version = "~> 5.0"` in a `module` block is equivalent to ___________.

- A) `>= 5.0` — any version 5.0 or higher, including 6.x, 7.x, and beyond
- B) `= 5.0` — pins to exactly version 5.0 and rejects all other versions including patch releases
- C) `>= 5.0, < 6.0` — the `~>` pessimistic constraint allows the **rightmost** specified component to increment freely while locking all components to the left
- D) `>= 5.0, < 5.1` — only 5.0.x patch releases are permitted

**Answer**: C

**Explanation**:
The `~>` operator is called the **pessimistic constraint operator** (or compatible-release operator). Its behaviour is determined by the **rightmost version component** in the constraint expression. `"~> 5.0"` specifies that the minor component (`0`) may increment freely, while the major component is locked at `5` — equivalent to `>= 5.0, < 6.0`. This permits `5.0`, `5.1`, `5.14`, etc., but rejects `6.0`. If the constraint were `"~> 5.0.1"`, the rightmost component would be the patch level, restricting to `>= 5.0.1, < 5.1.0`. Option A is too permissive (no upper bound). Option B locks to a single exact version. Option D over-restricts to only patch-level updates.

---

### Question 5 — HTTP Archive Module Source

**Difficulty**: Medium
**Answer Type**: one
**Topic**: How to reference a module hosted as a downloadable ZIP archive at an HTTPS URL

**Question**:
Complete the `source` argument to reference a module that is packaged as a ZIP archive served at an HTTPS URL:

```hcl
module "vpc" {
  source = "___________"
}
```

The archive is hosted at: `https://example.com/modules/vpc.zip`

- A) `"zip::https://example.com/modules/vpc.zip"`
- B) `"archive::https://example.com/modules/vpc.zip"`
- C) `"http::https://example.com/modules/vpc.zip"`
- D) `"https://example.com/modules/vpc.zip"`

**Answer**: D

**Explanation**:
For HTTPS-hosted archive files, Terraform uses the URL directly as the `source` value — no special prefix is required when the URL path ends with a recognized archive extension (`.zip`, `.tar.gz`, `.tar.bz2`, `.tar.xz`). Terraform detects the archive type from the file extension and automatically downloads and extracts it during `terraform init`. Options A (`zip::`), B (`archive::`), and C (`http::`) are not valid Terraform module source prefixes — they are fictional syntax that Terraform does not recognise.

---

### Question 6 — `versions.tf` Convention

**Difficulty**: Medium
**Answer Type**: one
**Topic**: The conventional filename for `required_providers` and Terraform version constraints in a module

**Question**:
Complete the blank with the filename that follows the standard Terraform module structure convention for declaring `required_providers` and `terraform` version constraints:

```
module/
├── main.tf          # Core resource definitions
├── variables.tf     # Input variable declarations
├── outputs.tf       # Output value declarations
├── ___________      # required_providers and terraform version constraints
└── README.md        # Documentation
```

- A) `providers.tf`
- B) `constraints.tf`
- C) `versions.tf`
- D) `terraform.tf`

**Answer**: C

**Explanation**:
`versions.tf` is the community and HashiCorp-recommended convention for the file that contains the `terraform` block with `required_version` and `required_providers` declarations. Separating this into its own file makes it easy for module consumers and automated tools to quickly locate version constraints without reading through resource definitions. The standard module file set is: `main.tf` (resources), `variables.tf` (input variables), `outputs.tf` (output values), `versions.tf` (version constraints), and `README.md` (documentation). Option A (`providers.tf`) is sometimes used for `provider {}` configuration blocks — a distinct concern from `required_providers`. Options B and D are not standard conventions.

---

### Question 7 — Explicit Variable Passing to a Child Module

**Difficulty**: Medium
**Answer Type**: one
**Topic**: How to explicitly pass a root module variable to a child module input argument

**Question**:
Complete the `module` block so the root module's `var.environment` value is passed to the child module's `environment` input variable:

```hcl
variable "environment" {
  type    = string
  default = "production"
}

module "tagging" {
  source      = "./modules/tagging"
  ___________ = var.environment
}
```

- A) `inherit`
- B) `input`
- C) `environment`
- D) `pass`

**Answer**: C

**Explanation**:
In a `module` block, child module input variables are assigned using the variable's name as the argument key. The argument name must exactly match the `variable` block name declared inside the child module. Here, the child module declares `variable "environment"`, so the assignment is `environment = var.environment`. Terraform does **not** automatically pass or inherit any variables from parent to child scope — every value a child module needs must be explicitly assigned in the `module` block, regardless of whether the argument names match. Options A (`inherit`), B (`input`), and D (`pass`) are not valid argument names in a `module` block.

---

### Question 8 — Indexing Into a Module List Output

**Difficulty**: Medium
**Answer Type**: one
**Topic**: How to access a single element from a child module output that returns a list

**Question**:
A child module exposes the following output:

```hcl
output "public_subnet_ids" {
  value = aws_subnet.public[*].id
}
```

Complete the root module resource argument to assign the **first** public subnet ID:

```hcl
resource "aws_instance" "web" {
  ami       = data.aws_ami.ubuntu.id
  subnet_id = ___________
}
```

- A) `module.networking.public_subnet_ids`
- B) `module.networking.public_subnet_ids.first`
- C) `module.networking.public_subnet_ids["0"]`
- D) `module.networking.public_subnet_ids[0]`

**Answer**: D

**Explanation**:
Module outputs that return lists are accessed using standard Terraform index notation — `[0]` for the first element (zero-based index), `[1]` for the second, and so on. The full reference `module.networking.public_subnet_ids[0]` resolves to the string ID of the first subnet. Option A returns the entire list, which is not valid for `subnet_id` (a single string argument). Option B (`.first`) is not a valid Terraform attribute or method — there is no `.first` accessor on lists. Option C uses a string key `"0"` which is object/map notation — list elements must be indexed with integer literals.

---

### Question 9 — Generic Git SSH Module Source

**Difficulty**: Medium
**Answer Type**: one
**Topic**: The correct prefix for a module sourced from a Git repository over SSH

**Question**:
Complete the `source` argument to reference a module using the generic Git provider over SSH:

```hcl
module "example" {
  source = "___________git@github.com/example/module.git"
}
```

- A) `ssh::`
- B) `git+ssh::`
- C) `git::ssh://`
- D) `github+ssh::`

**Answer**: C

**Explanation**:
For generic Git sources using the SSH transport protocol, Terraform uses the `git::ssh://` prefix. The full source value takes the form `"git::ssh://git@github.com/example/module.git"`. The `git::` prefix instructs Terraform to treat the URL as a Git repository rather than a plain file download, and `ssh://` specifies the transport. For HTTPS Git sources, the pattern is `git::https://`. For bare GitHub URLs without any prefix (e.g., `"github.com/org/repo"`), Terraform infers the HTTPS Git protocol automatically. Options A (`ssh::`), B (`git+ssh::`), and D (`github+ssh::`) are not valid Terraform module source prefixes.

---

### Question 10 — Module Composition: Two Correct Statements

**Difficulty**: Medium
**Answer Type**: many
**Topic**: How Terraform supports nested module calls and multiple child modules from the root

**Question**:
Which **TWO** of the following statements about Terraform module composition are correct?

- A) A root module is restricted to calling at most one child module — to use multiple modules, each must be combined into a single composite module first
- B) Child modules can themselves contain `module` blocks that call further nested child modules — Terraform supports arbitrary nesting depth with no enforced limit
- C) A grandchild module's output values are automatically propagated to the root module without any intermediate output declarations — Terraform traverses the call tree transparently
- D) A root module can call multiple independent child modules, and each of those child modules can in turn call their own nested child modules

**Answer**: B, D

**Explanation**:
Terraform supports arbitrary **module composition**: a root module can call any number of child modules, and each child module can itself instantiate further child modules — there is no enforced nesting depth limit (option D is correct; option B elaborates the same point from the child module's perspective — both are correct). Option A is wrong — a root module can call an unlimited number of child modules simultaneously. Option C is wrong — grandchild outputs are **not** automatically visible to the root module; the intermediate module must explicitly declare an `output` block that re-exposes the nested value, and the root must then reference it as `module.<parent>.<output_name>`. Outputs do not propagate automatically up the call chain.

---

### Question 11 — Standard Module Structure: Input Variables File

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Which file in the standard module structure holds all input `variable` block declarations

**Question**:
A team is building a reusable Terraform module following the recommended standard file structure. They want to place all input `variable` block declarations in a single, conventionally named file. Which filename should they use?

```
module/
├── main.tf
├── ___________
├── outputs.tf
├── versions.tf
└── README.md
```

- A) `inputs.tf`
- B) `args.tf`
- C) `params.tf`
- D) `variables.tf`

**Answer**: D

**Explanation**:
The standard Terraform module structure uses `variables.tf` as the conventional filename for all `variable` block declarations. This convention is widely adopted by the community and expected by documentation-generation tools like `terraform-docs`, which automatically extract variable descriptions, types, and defaults from this file. The complete standard file set is: `main.tf` (core resource definitions), `variables.tf` (input variable declarations), `outputs.tf` (output value declarations), `versions.tf` (Terraform and provider version constraints), and `README.md` (module documentation). Options A (`inputs.tf`), B (`args.tf`), and C (`params.tf`) are not standard Terraform naming conventions.

---

### Question 12 — `modules.json` After `terraform init`

**Difficulty**: Hard
**Answer Type**: one
**Topic**: What Terraform records in `.terraform/modules/modules.json` after running `terraform init`

**Question**:
A project uses two module blocks — one with `source = "./modules/networking"` (local path) and one with `source = "terraform-aws-modules/vpc/aws"` (Terraform Registry). After running `terraform init`, which of the following best describes the contents of `.terraform/modules/modules.json`?

- A) Only the Terraform Registry module is recorded — local path modules are excluded from `modules.json` because no file downloading occurs for them
- B) `modules.json` contains a manifest of **all** module blocks in the configuration — both local path and remote sources — recording each module's logical name, its source address, and the local path where its `.tf` files are found
- C) `modules.json` stores the SHA256 hash of each module's source code and is used exclusively for integrity verification during `terraform apply`
- D) `modules.json` is only created when at least one `version` argument is present in a module block — modules without version constraints are not recorded

**Answer**: B

**Explanation**:
`.terraform/modules/modules.json` is a metadata manifest created by `terraform init` that records **every** module block in the configuration — including both local path and remote sources. For each module, it records the logical name (the label in the `module` block), the source address, and the local filesystem path where the module's `.tf` files reside. For remote modules (registry, Git, HTTP archive), the path points to the downloaded code inside `.terraform/modules/<name>/`. For local path modules, the path points to the original `./modules/...` directory — no copying occurs. This manifest is how `terraform plan` and `terraform apply` locate module source code without re-downloading it. Option A is wrong — local modules are included. Option C mischaracterises the file's purpose. Option D is wrong — all modules are recorded regardless of `version` constraints.

---

### Question 13 — S3 and GCS Module Sources: Two Correct Statements

**Difficulty**: Hard
**Answer Type**: many
**Topic**: Valid S3 and GCS module source syntax, and the scope of the `version` argument

**Question**:
Which **TWO** of the following statements about Terraform module sources are correct?

- A) An Amazon S3 bucket can be used as a module source using the `s3::` prefix — for example: `"s3::https://s3-us-west-2.amazonaws.com/mybucket/vpc.zip"`
- B) All module source types — including local paths, Git URLs, S3 buckets, and HTTP archives — support the `version` argument in the `module` block to pin the downloaded version
- C) A Google Cloud Storage (GCS) bucket can be used as a module source using the `gcs::` prefix — for example: `"gcs::https://www.googleapis.com/storage/v1/mybucket/vpc.zip"`
- D) GitHub module sources using the bare `github.com/...` format do not support subdirectory selection — the `//` double-slash convention is only valid when using the `git::https://` prefix

**Answer**: A, C

**Explanation**:
Terraform supports a broad range of module source types beyond local paths and the Terraform Registry. Amazon S3 buckets are a valid source using the `s3::` prefix followed by the HTTPS URL of the ZIP object (option A is correct). Google Cloud Storage buckets are equally valid using the `gcs::` prefix followed by the GCS API URL (option C is correct). Option B is wrong — the `version` argument is **exclusively** supported for Terraform Registry and private registry sources; using it with Git, HTTP, S3, or GCS sources causes a `terraform init` error. To pin a Git source to a specific commit, use `?ref=`. Option D is wrong — the `//` double-slash subdirectory separator works with **all** Git-based source formats, including bare `github.com/...` URLs, not just `git::https://` URLs.
