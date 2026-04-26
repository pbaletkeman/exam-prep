# Terraform Associate Exam Questions

---

### Question 1 — Flawed Claim: `version` Argument Valid with GitHub Module Source

**Difficulty**: Easy
**Answer Type**: one
**Topic**: Which module source types support the `version` argument

**Question**:
A developer writes:

```hcl
module "vpc" {
  source  = "github.com/acme/terraform-modules//modules/vpc"
  version = "~> 3.0"
  cidr    = "10.0.0.0/16"
}
```

and claims: "The `version = \"~> 3.0\"` constraint works exactly the same as it does for Terraform Registry modules — it restricts which tagged release `terraform init` downloads from GitHub."

What is wrong with this claim?

- A) Nothing — the `version` argument works with GitHub module sources using semantic versioning
- B) The claim is wrong: the `version` argument is only valid for Terraform Registry and private registry sources; using it with a GitHub URL causes a `terraform init` error — the correct way to pin a Git source is the `?ref=` query parameter (e.g., `?ref=v3.0.0`)
- C) The claim is wrong: `version` works with GitHub sources but uses the GitHub release API, not semantic version constraints
- D) The claim is wrong: the `version` argument is only valid when `source` begins with `git::https://` — bare GitHub URLs do not support versioning

---

### Question 2 — Flawed HCL: Module Output Referenced with Wrong Syntax

**Difficulty**: Easy
**Answer Type**: one
**Topic**: Correct syntax for referencing a child module's output in the root module

**Question**:
Read this root module configuration:

```hcl
module "networking" {
  source = "./modules/networking"
}

resource "aws_instance" "web" {
  ami       = "ami-0abc123"
  subnet_id = output.networking.public_subnet_id
}
```

What is wrong with this configuration?

- A) Nothing — `output.networking.public_subnet_id` is the correct syntax to reference a child module output
- B) The configuration is wrong: child module outputs are referenced as `module.<name>.<output_name>` — the correct reference here is `module.networking.public_subnet_id`; there is no `output.<module_name>` syntax
- C) The configuration is wrong: child module outputs cannot be used directly in resource arguments — they must first be assigned to a local value
- D) The configuration is wrong: the `subnet_id` argument requires an `aws_subnet` resource reference, not a module output

---

### Question 3 — Flawed Claim: `.terraform/modules/` Should Be Committed to Git

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Whether the `.terraform/modules/` directory should be committed to version control

**Question**:
A new team member reads their company's Terraform onboarding guide, which states:

> "Commit the `.terraform/modules/` directory to version control. This eliminates the need for teammates to run `terraform init` when checking out the repository — the module cache is ready to use immediately."

What is wrong with this guidance?

- A) Nothing — committing `.terraform/modules/` is the recommended practice for improving team checkout speed
- B) The guidance is wrong: `.terraform/modules/` is a local cache directory that should be **excluded from version control** (via `.gitignore`); each developer and CI pipeline runs `terraform init` to populate it from the declared module sources — committing it creates unnecessary bloat and can cause version inconsistencies
- C) The guidance is wrong: `.terraform/modules/` is encrypted with a workspace-specific key and cannot be shared across machines even if committed
- D) The guidance is wrong: committing `.terraform/modules/` is not supported by GitHub because module caches exceed the 100 MB file size limit

---

### Question 4 — Flawed Claim: `terraform init` Is a One-Time Step

**Difficulty**: Medium
**Answer Type**: one
**Topic**: When `terraform init` must be re-run within an existing workspace

**Question**:
An experienced developer advises a teammate:

> "You only need to run `terraform init` once per workspace — after the initial setup, Terraform discovers module changes automatically during `terraform plan` and downloads any new modules it finds."

What is wrong with this advice?

- A) Nothing — `terraform init` is only required once per workspace; `terraform plan` handles module discovery automatically
- B) The advice is wrong: `terraform init` must be re-run whenever a new `module` block is added, an existing module's `source` is changed, or a module version is updated — `terraform plan` does not automatically install missing or updated modules and will raise an error if a new module has not been initialised
- C) The advice is wrong: `terraform init` must be re-run on every single `terraform plan` execution to ensure providers and modules are up to date
- D) The advice is wrong: modules are not downloaded by `terraform init` at all — they are resolved dynamically during `terraform plan`

---

### Question 5 — Flawed HCL: DynamoDB Lock Table with Wrong `hash_key` Attribute Name

**Difficulty**: Medium
**Answer Type**: one
**Topic**: The required partition key attribute name for a DynamoDB table used for S3 backend state locking

**Question**:
A team provisions a DynamoDB table for Terraform state locking:

```hcl
resource "aws_dynamodb_table" "tf_lock" {
  name         = "terraform-state-locks"
  billing_mode = "PAY_PER_REQUEST"
  hash_key     = "StateFileLock"

  attribute {
    name = "StateFileLock"
    type = "S"
  }
}

terraform {
  backend "s3" {
    bucket         = "company-tfstate"
    key            = "prod/terraform.tfstate"
    region         = "us-east-1"
    dynamodb_table = "terraform-state-locks"
    encrypt        = true
  }
}
```

What is wrong with this configuration?

- A) Nothing — the `hash_key` attribute can be any valid string name; `"StateFileLock"` is acceptable
- B) The configuration is wrong: the DynamoDB table's `hash_key` must be named exactly `"LockID"` — the Terraform S3 backend hardcodes this attribute name when writing and reading lock records; a different name causes locking to fail silently or raise errors
- C) The configuration is wrong: the DynamoDB table must use `"terraform.lock"` as the `hash_key` to match the format expected by the S3 backend
- D) The configuration is wrong: the `hash_key` type must be `"N"` (Number), not `"S"` (String), for the S3 backend locking to function correctly

---

### Question 6 — Flawed Claim: `terraform state rm` Deletes the Cloud Resource

**Difficulty**: Medium
**Answer Type**: one
**Topic**: What `terraform state rm` does and does not do to the cloud resource

**Question**:
A developer on the team explains `terraform state rm`:

> "Use `terraform state rm aws_s3_bucket.logs` when you want to decommission a managed resource — it removes the bucket from state and also deletes it from AWS in a single atomic operation, which is safer than running `terraform destroy -target` because it doesn't risk cascading deletions."

What is wrong with this explanation?

- A) Nothing — `terraform state rm` removes the resource from both Terraform state and AWS in one step
- B) The explanation is wrong: `terraform state rm` removes the resource **only from the state file** — the actual AWS resource (the S3 bucket) is not touched in any way and continues to exist in AWS; Terraform simply stops managing it
- C) The explanation is wrong: `terraform state rm` is not valid for S3 resources — it can only be used with compute resources
- D) The explanation is wrong: `terraform state rm` sends a delete request to AWS but waits for manual confirmation before updating the state file

---

### Question 7 — Flawed Claim: `terraform plan -refresh-only` Updates the State File

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Whether `terraform plan -refresh-only` writes any changes to the state file

**Question**:
An operator explains drift remediation to a new team member:

> "When someone manually modifies a resource in the AWS Console, running `terraform plan -refresh-only` is the correct command to safely sync the state file with the current cloud reality — it reads the live resource attributes and updates `terraform.tfstate` to match, without making any infrastructure changes."

What is wrong with this explanation?

- A) Nothing — `terraform plan -refresh-only` reads live cloud resources and updates the state file
- B) The explanation is wrong: `terraform plan -refresh-only` only **shows** the drift between the state file and the current cloud state — it does not write anything to the state file; to actually update the state, the operator must run `terraform apply -refresh-only`
- C) The explanation is wrong: `terraform plan -refresh-only` re-applies all infrastructure to match the configuration — it is not a safe read-only command
- D) The explanation is wrong: only `terraform refresh` (not `plan -refresh-only`) updates the state file

---

### Question 8 — Flawed Claim: Every Child Module Requires Its Own `provider` Block

**Difficulty**: Medium
**Answer Type**: one
**Topic**: How provider configuration flows to child modules in Terraform

**Question**:
A team's Terraform style guide states:

> "Every child module that creates AWS resources must include its own `provider "aws" {}` block declaring the region and profile. Provider configuration is scoped to each module and is not automatically available to child modules from the root."

What is wrong with this style guide rule?

- A) Nothing — every child module must redeclare its provider configuration independently
- B) The rule is wrong: child modules **automatically inherit** the root module's default provider configuration — they do not need their own `provider "aws" {}` blocks; adding redundant provider blocks in child modules can cause "conflicting configurations" errors and is not a recommended practice
- C) The rule is wrong: child modules cannot declare `provider` blocks at all — only the root module is allowed to configure providers
- D) The rule is wrong: provider configuration is only required in leaf modules (modules with no children); intermediate modules inherit automatically but leaf modules do not

---

### Question 9 — Flawed HCL: `version` Constraint on Local Path Module Source

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Identifying that `version` is invalid alongside a local path module source

**Question**:
An engineer pins a locally developed module with:

```hcl
module "compute" {
  source  = "./modules/compute"
  version = "~> 1.5"
  ami     = "ami-0abc123"
}
```

and says: "The `version = \"~> 1.5\"` constraint ensures we don't accidentally pick up breaking changes if a teammate bumps the module version."

What is wrong with this configuration?

- A) Nothing — `version` constraints are valid for local path module sources and work as expected
- B) The configuration is wrong: the `version` argument is not valid for local path sources — it causes `terraform init` to raise an error; local modules have no version registry to consult, and code changes are controlled via the file system (or, for git repos, via `?ref=` on the source URL)
- C) The configuration is wrong: local path modules require `version = "0.0.0"` as a placeholder — any other version string causes an error
- D) The configuration is wrong: the `~>` operator is only valid for provider version constraints, not for module version constraints

---

### Question 10 — Two Errors in `for_each` Module Block

**Difficulty**: Medium
**Answer Type**: many
**Topic**: Errors when using `count.index` in a `for_each` module and accessing instances with a numeric index

**Question**:
An engineer writes this configuration to deploy three server instances:

```hcl
module "server" {
  for_each     = toset(["web", "api", "worker"])
  source       = "./modules/server"
  service_name = count.index
  instance_type = "t3.micro"
}

output "web_instance_id" {
  value = module.server[0].instance_id
}
```

Which TWO statements correctly identify the errors? (Select two.)

- A) `count.index` is not available inside a `for_each` module block — it is only valid when the module uses `count`; the correct reference to the current element's key is `each.key`
- B) `toset()` is not a valid collection type for `for_each` on a module block — only maps are supported
- C) `module.server[0]` uses a numeric index, but `for_each` with a set of strings addresses instances using their string keys — the correct reference is `module.server["web"]`
- D) `for_each` cannot be used on a `module` block — it is only valid for `resource` blocks

---

### Question 11 — Two Flawed Claims About `terraform.tfstate.backup`

**Difficulty**: Medium
**Answer Type**: many
**Topic**: The scope and content of `terraform.tfstate.backup` and when it is created

**Question**:
A developer documents local backend behaviour with two claims:

> **Claim 1**: "`terraform.tfstate.backup` maintains a rolling five-version history — each `terraform apply` appends a new snapshot, and the oldest is automatically pruned once the history exceeds five entries."
> **Claim 2**: "When using a remote S3 backend, `terraform.tfstate.backup` is automatically created in the working directory after every `terraform apply` as a local safety copy of the updated remote state."

Which TWO statements correctly identify the errors? (Select two.)

- A) Claim 1 is **wrong**: `terraform.tfstate.backup` is a **single file containing only one snapshot** — the state immediately before the most recent apply; it is completely overwritten on each apply with no history retention
- B) Claim 1 is **correct**: a rolling five-version history is maintained in `terraform.tfstate.backup`
- C) Claim 2 is **wrong**: `terraform.tfstate.backup` is only created by the **local backend**; when using a remote backend (such as S3), no local backup file is written to the working directory during apply
- D) Claim 2 is **correct**: remote backends always write a local `terraform.tfstate.backup` for disaster recovery purposes

---

### Question 12 — Flawed Claim: `terraform state push` Prompts Before Overwriting

**Difficulty**: Hard
**Answer Type**: one
**Topic**: Whether `terraform state push` provides safety prompts before overwriting remote state

**Question**:
A platform engineer documents the state restoration workflow:

> "If a state file becomes corrupt, `terraform state push backup.tfstate` is a safe recovery tool — before overwriting the remote state, it displays a diff of what will change and requires the operator to type 'yes' to confirm, preventing accidental overwrites in shared environments."

What is wrong with this documentation?

- A) Nothing — `terraform state push` always prompts for confirmation and shows a diff before overwriting remote state
- B) The documentation is wrong: `terraform state push` **does not prompt for confirmation** and does not display a diff — it immediately overwrites the remote state file with the contents of the provided local file; it is a dangerous command that can silently destroy the remote state without any safety checks, and should only be used as a last resort by operators who have already verified the file to push is correct
- C) The documentation is wrong: `terraform state push` only works for the local backend — it cannot overwrite a remote S3 backend state
- D) The documentation is wrong: `terraform state push` requires the `-force` flag to be added before it will overwrite an existing remote state; without `-force` it is read-only

---

### Question 13 — Two Errors About `terraform state mv` and `moved` Blocks

**Difficulty**: Hard
**Answer Type**: many
**Topic**: What `terraform state mv` does and does not modify, and what `moved` blocks can address

**Question**:
A team's runbook contains two claims about renaming resources:

> **Claim 1**: "After running `terraform state mv aws_instance.old aws_instance.new`, Terraform automatically adds a `moved` block to `main.tf` to track the rename for teammates who apply from a fresh checkout — no manual HCL update is required."
> **Claim 2**: "`moved` blocks can only be used to rename resources at the root module level — they cannot move a resource into a module, rename a module call, or address resources inside a child module from the root."

Which TWO statements correctly identify the errors? (Select two.)

- A) Claim 1 is **wrong**: `terraform state mv` **only modifies the state file** — it never writes to any HCL files; teammates applying from a fresh state or importing the project will encounter a mismatch unless the engineer also manually updates the resource label in `main.tf` and (optionally) adds a `moved` block for history
- B) Claim 1 is **correct**: `terraform state mv` automatically adds a `moved` block to `main.tf`
- C) Claim 2 is **wrong**: `moved` blocks support a wide range of restructuring scenarios including moving a root-level resource into a module (`from = aws_instance.web` → `to = module.compute.aws_instance.web`), renaming a module call, and addressing resources within nested modules — they are not limited to root-level resource renames
- D) Claim 2 is **correct**: `moved` blocks only support root-level resource renames

## Answer Key

| Q# | Answer(s) | Explanation | Source | Difficulty |
|----|-----------|-----------:|--------|------------|
| 1 | B | N/A | Which module source types support the `version` argument | Easy |
| 2 | B | N/A | Correct syntax for referencing a child module's output in the root module | Easy |
| 3 | B | N/A | Whether the `.terraform/modules/` directory should be committed to version control | Medium |
| 4 | B | N/A | When `terraform init` must be re-run within an existing workspace | Medium |
| 5 | B | N/A | The required partition key attribute name for a DynamoDB table used for S3 backend state locking | Medium |
| 6 | B | N/A | What `terraform state rm` does and does not do to the cloud resource | Medium |
| 7 | B | N/A | Whether `terraform plan -refresh-only` writes any changes to the state file | Medium |
| 8 | B | N/A | How provider configuration flows to child modules in Terraform | Medium |
| 9 | B | N/A | Identifying that `version` is invalid alongside a local path module source | Medium |
| 10 | A, C | N/A | Errors when using `count.index` in a `for_each` module and accessing instances with a numeric index | Medium |
| 11 | A, C | N/A | The scope and content of `terraform.tfstate.backup` and when it is created | Medium |
| 12 | B | N/A | Whether `terraform state push` provides safety prompts before overwriting remote state | Hard |
| 13 | A, C | N/A | What `terraform state mv` does and does not modify, and what `moved` blocks can address | Hard |
