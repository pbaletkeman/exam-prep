# Terraform Associate Exam Questions

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

## Answer Key

| Q# | Answer(s) | Explanation | Source | Difficulty |
|----|-----------|-----------:|--------|------------|
| 1 | C | N/A | The three-part `NAMESPACE/MODULE/PROVIDER` format for a Terraform Registry module source | Easy |
| 2 | D | N/A | Completing the `value` argument in a child module output block to expose a resource attribute | Easy |
| 3 | A, D | N/A | What `terraform init` writes for module caching and what `.terraform/modules/` contains | Easy |
| 4 | C | N/A | What the pessimistic constraint operator `~>` means in a module `version` argument | Medium |
| 5 | D | N/A | How to reference a module hosted as a downloadable ZIP archive at an HTTPS URL | Medium |
| 6 | C | N/A | The conventional filename for `required_providers` and Terraform version constraints in a module | Medium |
| 7 | C | N/A | How to explicitly pass a root module variable to a child module input argument | Medium |
| 8 | D | N/A | How to access a single element from a child module output that returns a list | Medium |
| 9 | C | N/A | The correct prefix for a module sourced from a Git repository over SSH | Medium |
| 10 | B, D | N/A | How Terraform supports nested module calls and multiple child modules from the root | Medium |
| 11 | D | N/A | Which file in the standard module structure holds all input `variable` block declarations | Medium |
| 12 | B | N/A | What Terraform records in `.terraform/modules/modules.json` after running `terraform init` | Hard |
| 13 | A, C | N/A | Valid S3 and GCS module source syntax, and the scope of the `version` argument | Hard |
