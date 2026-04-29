# Terraform Associate Exam Questions

---

### Question 1 — IaC Benefit Name for Identical Environments

**Difficulty**: Easy
**Answer Type**: one
**Topic**: Repeatability — the IaC benefit that guarantees the same code deploys identical environments across staging and production

**Question**:
Complete the following statement by selecting the term that fills the blank:

> "Running the same Terraform configuration in the staging and production environments guarantees identical infrastructure. This IaC benefit is called ___________."

- A) Atomicity
- B) Convergence
- C) Modularity
- D) **Repeatability**

---

### Question 2 — `instance_type` Argument in an EC2 Resource Block

**Difficulty**: Easy
**Answer Type**: one
**Topic**: Completing a basic `aws_instance` resource block — the argument that specifies the EC2 instance type

**Question**:
A developer is writing their first Terraform resource block and leaves one argument name incomplete:

```hcl
resource "aws_instance" "web" {
  ami           = "ami-0abcd1234"
  ___________   = "t3.micro"
}
```

What argument name fills the blank to specify the EC2 instance size?

- A) `machine_type`
- B) `instance_size`
- C) **`instance_type`**
- D) `type`

---

### Question 3 — "Desired" End State in Declarative IaC

**Difficulty**: Easy
**Answer Type**: one
**Topic**: Completing the definition of declarative IaC — configurations express the desired end state

**Question**:
Complete the following statement:

> "Terraform configurations describe the ___________ end state of infrastructure. The tool determines what steps are necessary to reach that state, whether that means creating, modifying, or destroying resources."

- A) procedural
- B) scripted
- C) **desired**
- D) imperative

---

### Question 4 — `count = 0` to Conditionally Disable a Resource

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Using `count = 0` to declare that no instances of a resource should exist, while keeping the block in configuration

**Question**:
An engineer wants the bastion host resource block to remain in the configuration file for documentation purposes, but needs to ensure **no instances are created in the current environment**. Complete the resource block:

```hcl
resource "aws_instance" "bastion" {
  ami           = "ami-0abc1234"
  instance_type = "t3.nano"
  count         = ___________
}
```

What value fills the blank?

- A) `null`
- B) `false`
- C) `"disabled"`
- D) **`0`**

---

### Question 5 — "Drift" — Infrastructure Deviation From Desired State

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Completing the definition of infrastructure drift — when actual cloud resources diverge from the Terraform configuration

**Question**:
Complete the following statement:

> "When a cloud engineer manually modifies an EC2 instance's security group through the AWS Console — without updating the Terraform configuration — the actual state of that resource diverges from what the `.tf` files describe. This divergence is called infrastructure ___________."

- A) contamination
- B) corruption
- C) divergence
- D) **drift**

---

### Question 6 — "Audit Trail" Benefit of Version-Controlled IaC

**Difficulty**: Medium
**Answer Type**: one
**Topic**: The IaC benefit that provides a historical record of every infrastructure change via version control commits

**Question**:
Complete the following statement:

> "When infrastructure configuration files are stored in a version control system such as Git, every infrastructure change is captured as a commit — recording who made the change, when, and what was modified. This gives teams a complete ___________ of infrastructure changes."

- A) Terraform plan output
- B) `terraform.tfstate.backup`
- C) speculative plan history
- D) **audit trail**

---

### Question 7 — TWO Provisioning Tools in the IaC Landscape

**Difficulty**: Medium
**Answer Type**: many
**Topic**: Distinguishing provisioning tools (Terraform category) from configuration management tools — CloudFormation and Pulumi are provisioning tools

**Question**:
An engineer is building a comparison table of IaC tools with a "Provisioning" vs "Configuration Management" category column. Terraform belongs in the **Provisioning** category. Which TWO other tools from the list below also belong in the **Provisioning** category? (Select two.)

- A) Ansible
- B) **AWS CloudFormation**
- C) Chef
- D) **Pulumi**

---

### Question 8 — "Documentation" Benefit of IaC Configuration Files

**Difficulty**: Medium
**Answer Type**: one
**Topic**: IaC configuration files serve as living documentation of infrastructure

**Question**:
Complete the following statement from Terraform's IaC benefits:

> "Unlike a ClickOps environment where the exact infrastructure setup exists only in someone's memory or informal runbooks, IaC configuration files serve as living ___________ of what has been provisioned — always up to date because they are the authoritative source used to apply infrastructure."

- A) backups
- B) **documentation**
- C) snapshots
- D) manifests

---

### Question 9 — Declarative IaC Describes WHAT, Not HOW

**Difficulty**: Medium
**Answer Type**: one
**Topic**: In a declarative IaC approach, the engineer describes WHAT the infrastructure should look like — not the steps to create it

**Question**:
Complete the following statement that describes the Terraform configuration model:

> "In Terraform's declarative approach, the engineer describes ___________ the infrastructure should look like. Terraform determines the sequence of API calls and resource operations needed to produce that outcome."

- A) how
- B) why
- C) when
- D) **what**

---

### Question 10 — Conditional `count` Expression for Optional Resources

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Using a ternary conditional expression to set count = 1 when a boolean variable is true, otherwise count = 0

**Question**:
An engineer wants to conditionally create a bastion host only when the `create_bastion` variable is set to `true`. Complete the resource block:

```hcl
variable "create_bastion" {
  type    = bool
  default = false
}

resource "aws_instance" "bastion" {
  ami           = "ami-0abc1234"
  instance_type = "t3.nano"
  count         = var.create_bastion ? ___ : 0
}
```

What value fills the blank to create exactly one bastion instance when `create_bastion` is `true`?

- A) `true`
- B) **`1`**
- C) `"enabled"`
- D) `var.bastion_count`

---

### Question 11 — TWO Accurate Statements About IaC Solving ClickOps Problems

**Difficulty**: Medium
**Answer Type**: many
**Topic**: Identifying which IaC benefits directly address the reproducibility and drift problems of the manual ClickOps approach

**Question**:
A team is documenting why they are adopting Terraform to replace their ClickOps workflow. Which TWO of the following statements correctly complete the sentence: "We are adopting IaC because ___________"? (Select two.)

- A) **The same configuration can be applied to staging and production to guarantee identical environments, solving the problem of environments drifting apart over time through individual manual changes**
- B) IaC removes the need for cloud providers because infrastructure is simulated locally in configuration files
- C) IaC configurations run faster than manual provisioning because they use compiled binary formats
- D) **An IaC tool can compare the desired state in configuration files against the actual cloud state, detect manual changes made outside Terraform, and propose corrections**

---

### Question 12 — `resource` Keyword in HCL Block Declaration

**Difficulty**: Hard
**Answer Type**: one
**Topic**: Completing an HCL block declaration — the `resource` keyword identifies a managed infrastructure object

**Question**:
A new engineer is writing their first Terraform file. They accidentally leave out the opening keyword of the block:

```hcl
___________ "aws_s3_bucket" "assets" {
  bucket = "acme-company-assets-2024"
}
```

What keyword fills the blank to correctly declare an S3 bucket that Terraform will create and manage?

- A) `data`
- B) `module`
- C) `provider`
- D) **`resource`**

---

### Question 13 — TWO Advantages of Terraform Over AWS CloudFormation

**Difficulty**: Hard
**Answer Type**: many
**Topic**: Terraform's multi-cloud support and open-source/non-vendor-locked nature versus CloudFormation's AWS-only scope

**Question**:
A platform engineering team is choosing between Terraform and AWS CloudFormation for a new infrastructure project. Which TWO of the following correctly complete the statement: "We should choose Terraform over CloudFormation because ___________"? (Select two.)

- A) **Terraform can manage resources across AWS, Azure, and GCP in a single configuration and workflow, whereas CloudFormation only manages AWS resources**
- B) CloudFormation uses an imperative scripting model, while Terraform uses a superior declarative model
- C) Terraform plan output includes cost estimation for every resource type, while CloudFormation does not support cost estimation
- D) **Terraform is not tied to a single cloud vendor — the same tool, workflow, and skills apply whether managing AWS, Azure, GCP, or on-premises resources**

---

### Question 14 — `required_version` in the `terraform` Block

**Difficulty**: Easy
**Answer Type**: one
**Topic**: The `required_version` argument sets the minimum Terraform CLI version required to use this configuration

**Question**:
Complete the `terraform` block so that Terraform will refuse to run with any CLI version older than `1.5.0`:

```hcl
terraform {
  ___________ = ">= 1.5"

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}
```

What argument name fills the blank?

- A) `minimum_version`
- B) `terraform_version`
- C) **`required_version`**
- D) `cli_version`

---

### Question 15 — Default Registry Hostname in Provider Source Addresses

**Difficulty**: Easy
**Answer Type**: one
**Topic**: The default hostname in a Terraform provider source address is registry.terraform.io when no hostname is specified

**Question**:
Complete the following statement:

> "When a provider source address is written in the short form `hashicorp/aws`, Terraform expands it to the fully qualified address `___________.terraform.io/hashicorp/aws` by supplying the default registry hostname."

What word fills the blank?

- A) `releases`
- B) `providers`
- C) `app`
- D) **`registry`**

---

### Question 16 — `terraform init -upgrade` Flag

**Difficulty**: Easy
**Answer Type**: one
**Topic**: The -upgrade flag on terraform init advances locked provider versions to the newest versions satisfying constraints

**Question**:
A team has `.terraform.lock.hcl` pinned to AWS provider `5.28.0`. A new `5.35.0` version has been released. The team wants to deliberately update the lock file to use the newer version. Complete the command:

```bash
terraform init ___________
```

What flag fills the blank?

- A) `--refresh`
- B) `--update`
- C) `-reconfigure`
- D) **`-upgrade`**

---

### Question 17 — Provider Alias Reference in a Resource Block

**Difficulty**: Medium
**Answer Type**: one
**Topic**: A resource block references an aliased provider using the `provider = <type>.<alias>` syntax

**Question**:
An engineer defines two AWS provider configurations — a default (`us-east-1`) and an aliased (`eu-west-1`). Complete the resource block so the S3 bucket is created in `eu-west-1`:

```hcl
provider "aws" {
  region = "us-east-1"
}

provider "aws" {
  alias  = "europe"
  region = "eu-west-1"
}

resource "aws_s3_bucket" "eu_assets" {
  bucket   = "acme-eu-assets-2024"
  provider = ___________
}
```

What value fills the blank?

- A) `"aws.europe"`
- B) `aws_europe`
- C) `"europe"`
- D) **`aws.europe`**

---

### Question 18 — `terraform.tfstate.backup` — Only One Backup Kept

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Terraform keeps only one .tfstate.backup file — the previous state from the most recent apply

**Question**:
Complete the following statement:

> "Terraform automatically creates `terraform.tfstate.backup` before each apply. This file contains the state from the ___________ successful apply — **not** a full history of all previous states."

What word or phrase fills the blank?

- A) original
- B) first
- C) oldest
- D) **previous (most recent)**

---

### Question 19 — `terraform plan -refresh=false`

**Difficulty**: Medium
**Answer Type**: one
**Topic**: The -refresh=false flag skips live API queries and plans against the cached state — faster but potentially stale

**Question**:
A team runs `terraform plan` in a large production environment with hundreds of resources. Each plan takes 8 minutes because Terraform queries the live API for every resource. An engineer wants to run a faster plan using only the cached state file without making any live API calls. Complete the command:

```bash
terraform plan ___________
```

What flag fills the blank?

- A) `-no-refresh`
- B) `-fast`
- C) `-cached`
- D) **`-refresh=false`**

---

### Question 20 — `terraform show -json` for Machine-Readable State

**Difficulty**: Medium
**Answer Type**: one
**Topic**: The -json flag on terraform show outputs state in machine-readable JSON format suitable for parsing by scripts

**Question**:
A CI/CD pipeline needs to parse Terraform state values programmatically using a script. Complete the command to produce machine-readable JSON output of the current state:

```bash
terraform show ___________
```

What flag fills the blank?

- A) `-machine`
- B) `-output`
- C) `-parse`
- D) **`-json`**

---

### Question 21 — `terraform state pull` Writes to stdout

**Difficulty**: Medium
**Answer Type**: one
**Topic**: terraform state pull downloads the current remote state and writes it to stdout for inspection or backup

**Question**:
Complete the following statement about the `terraform state pull` command:

> "Running `terraform state pull` downloads the current remote state and writes it to ___________, making it easy to inspect the raw state JSON or create a local backup file using shell redirection."

What word or phrase fills the blank?

- A) a file named `state-backup.json` in the current directory
- B) the `.terraform/` directory
- C) `terraform.tfstate` in the current directory, overwriting the local copy
- D) **`stdout`**

---

### Question 22 — `sensitive = true` Scope

**Difficulty**: Medium
**Answer Type**: one
**Topic**: sensitive = true only controls terminal display — the value is still written to state in plaintext

**Question**:
Complete the following statement about Terraform's `sensitive = true` argument:

> "Setting `sensitive = true` on an output variable prevents the value from appearing in ___________ output. It does **not** encrypt or redact the value from the `terraform.tfstate` file, where it remains stored in plaintext."

What word fills the blank?

- A) state
- B) log file
- C) remote backend
- D) **terminal**

---

### Question 23 — Fourth State Purpose: Performance

**Difficulty**: Medium
**Answer Type**: one
**Topic**: One of the four state purposes is performance caching — avoiding live API queries for every resource on every plan

**Question**:
Terraform state serves four primary purposes. Complete the fourth one:

> 1. **Resource identity mapping** — maps `aws_instance.web` → `i-0abcd1234ef567890`
> 2. **Computing diffs** — compares desired state vs known state vs actual state
> 3. **Metadata tracking** — stores dependency information and provider details
> 4. **___________ ** — caches resource attribute values so Terraform does not need to query every resource from the live API on every plan

What word fills the blank for the fourth purpose?

- A) Encryption
- B) Serialisation
- C) Locking
- D) **Performance**

---

### Question 24 — TWO Limitations of Local State vs Remote State

**Difficulty**: Medium
**Answer Type**: many
**Topic**: Local state has no locking and no sharing — both are required for team collaboration and production safety

**Question**:
A solo developer has been using a local `terraform.tfstate` file for a prototype. Their team is now growing. Which TWO limitations of local state make it unsuitable for team use? (Select two.)

- A) **Local state has no locking** — when two team members run `terraform apply` concurrently, there is no mechanism to prevent both writes from corrupting the state file; remote backends like S3 + DynamoDB provide locking to ensure only one operation modifies state at a time
- B) Local state cannot store resource attribute values — it only stores resource addresses
- C) **Local state has no built-in sharing mechanism** — the `terraform.tfstate` file lives on one engineer's workstation; other team members cannot access it without manually copying the file, making collaboration impractical and error-prone; remote backends (S3, Azure Blob, HCP Terraform) store state in a location all team members can reach
- D) Local state cannot track more than 50 resources — it has a hard limit for small projects only

---

### Question 25 — gRPC Protocol Between Terraform Core and Provider

**Difficulty**: Hard
**Answer Type**: one
**Topic**: Terraform Core communicates with provider plugins over gRPC — providers run as separate processes

**Question**:
Complete the following description of Terraform's plugin architecture:

> "When Terraform executes a plan or apply, it launches each required provider as a **separate process**. Terraform Core communicates with these provider processes using **___________** — a high-performance remote procedure call framework. The provider process then makes HTTPS API calls to the target cloud service."

What protocol name fills the blank?

- A) REST
- B) JSON-RPC
- C) SOAP
- D) **gRPC**

---

### Question 26 — TWO Contents of a `.terraform.lock.hcl` Provider Entry

**Difficulty**: Hard
**Answer Type**: many
**Topic**: Each provider entry in the lock file contains the exact installed version and cryptographic hashes — both are required for reproducibility and verification

**Question**:
A team reviews a `.terraform.lock.hcl` file entry:

```hcl
provider "registry.terraform.io/hashicorp/aws" {
  version     = "5.31.0"
  constraints = "~> 5.0"
  hashes = [
    "h1:abc123...",
    "zh:def456...",
  ]
}
```

Which TWO of the following correctly describe the purpose of properties in this lock file entry? (Select two.)

- A) **The `version` field records the exact provider version that was installed** — on every subsequent `terraform init` (without `-upgrade`), Terraform installs this exact version rather than re-resolving from the constraint; this ensures all team members and CI pipelines use identical provider behaviour regardless of when they initialise
- B) The `constraints` field is used by Terraform to re-download the provider if the `version` field is missing; it is only a fallback and serves no purpose when `version` is present
- C) **The `hashes` field contains cryptographic checksums of the provider binary for each supported platform** — when `terraform init` downloads the provider, it verifies the binary's hash against the recorded values; if the hash does not match (e.g., the binary has been tampered with or the wrong binary was downloaded), Terraform refuses to proceed; this prevents supply-chain attacks
- D) The `hashes` field stores the SHA-256 checksum of the `.terraform.lock.hcl` file itself, used to detect if the lock file was manually modified

---

### Question 27 — Saving a Plan to a File with `-out`

**Difficulty**: Easy
**Answer Type**: one
**Topic**: The `-out` flag saves the execution plan to a binary file for a deterministic later apply

**Question**:
A CI pipeline should generate a plan in one stage and apply it in a later stage — ensuring the exact same changes reviewed in the plan are the ones applied. Complete the plan command:

```bash
terraform plan ___________ plan.tfplan
```

What flag fills the blank to save the plan to a file named `plan.tfplan`?

- A) `-save`
- B) `-export`
- C) **`-out=`**
- D) `-write`

---

### Question 28 — `terraform output -raw` for Scripting

**Difficulty**: Easy
**Answer Type**: one
**Topic**: The -raw flag outputs a single output value as a plain string without surrounding quotes — suitable for shell variable assignment

**Question**:
A shell script needs to capture the database endpoint output value as a plain string for use in another command. When the engineer runs `terraform output db_endpoint`, the result is printed with surrounding quotes: `"rds.example.com"`. Complete the command to get the value without quotes:

```bash
terraform output ___________ db_endpoint
```

What flag fills the blank?

- A) `-plain`
- B) `-string`
- C) `-noformat`
- D) **`-raw`**

---

### Question 29 — `terraform workspace show`

**Difficulty**: Easy
**Answer Type**: one
**Topic**: The workspace show subcommand prints the name of the currently active workspace

**Question**:
An engineer is working in a terminal and cannot remember which workspace is currently active. Complete the command to display the current workspace name:

```bash
terraform workspace ___________
```

What subcommand fills the blank?

- A) `current`
- B) `active`
- C) `status`
- D) **`show`**

---

### Question 30 — `terraform fmt -diff` Shows Changes Without Writing

**Difficulty**: Medium
**Answer Type**: one
**Topic**: The -diff flag prints the formatting diff to stdout without modifying any files on disk

**Question**:
An engineer wants to see exactly what `terraform fmt` would change in their files — without actually writing those changes to disk. Complete the command:

```bash
terraform fmt ___________
```

What flag fills the blank?

- A) `-preview`
- B) `-dry-run`
- C) `-show`
- D) **`-diff`**

---

### Question 31 — `terraform plan -destroy`

**Difficulty**: Medium
**Answer Type**: one
**Topic**: The -destroy flag on terraform plan shows a preview of what terraform destroy would remove, without making any changes

**Question**:
Before running `terraform destroy` in a production environment, a team wants to review exactly which resources will be deleted. Complete the command that generates a **read-only preview** of the destruction without making any changes:

```bash
terraform plan ___________
```

What flag fills the blank?

- A) `-preview-destroy`
- B) `-simulate-destroy`
- C) `-dry-destroy`
- D) **`-destroy`**

---

### Question 32 — TWO Plan Symbols That Result in a Net-New Resource After Apply

**Difficulty**: Medium
**Answer Type**: many
**Topic**: Both + (pure create) and -/+ (replacement — destroy then create) result in a new resource existing after apply

**Question**:
A `terraform plan` output contains four types of operations. Which TWO operation symbols result in a **brand-new resource object being created in the cloud** after `terraform apply` completes? (Select two.)

- A) **`+`** — a pure create: a new resource that does not yet exist will be provisioned
- B) `~` — an in-place update: the existing resource is modified without replacement
- C) **`-/+`** — a replacement: the existing resource is destroyed and a completely new one is created in its place
- D) `-` — a pure destroy: the existing resource is removed and nothing is created

---

### Question 33 — `terraform apply -replace` to Force Recreate a Resource

**Difficulty**: Medium
**Answer Type**: one
**Topic**: The -replace flag forces a specific resource to be destroyed and recreated — the current replacement for the deprecated terraform taint command

**Question**:
An EC2 instance has become unhealthy and an engineer wants to force Terraform to destroy and recreate it on the next apply. The deprecated `terraform taint` command used to handle this. Complete the current (Terraform 1.5+) approach:

```bash
terraform apply ___________="aws_instance.web"
```

What flag fills the blank?

- A) `-recreate`
- B) `-taint`
- C) `-force-replace`
- D) **`-replace`**

---

### Question 34 — `terraform init -reconfigure`

**Difficulty**: Medium
**Answer Type**: one
**Topic**: The -reconfigure flag forces terraform init to reconfigure the backend without migrating or asking about existing state

**Question**:
An engineer changes the backend configuration in a CI environment where state migration is handled separately. They want `terraform init` to accept the new backend configuration without prompting about state migration. Complete the command:

```bash
terraform init ___________
```

What flag fills the blank?

- A) `-force`
- B) `-skip-migrate`
- C) `-reset`
- D) **`-reconfigure`**

---

### Question 35 — `terraform graph` Outputs DOT Format

**Difficulty**: Medium
**Answer Type**: one
**Topic**: terraform graph outputs the resource dependency graph in DOT language format — renderable by Graphviz

**Question**:
Complete the following statement about the `terraform graph` command:

> "Running `terraform graph` prints the resource dependency graph to stdout in ___________ format — a graph description language used by the Graphviz toolset. Pipe the output to `dot -Tsvg > graph.svg` to produce a visual diagram."

What word fills the blank?

- A) JSON
- B) XML
- C) Mermaid
- D) **DOT**

---

### Question 36 — TWO Flags That Work on Both `terraform plan` and `terraform apply`

**Difficulty**: Medium
**Answer Type**: many
**Topic**: -var and -var-file are valid flags on both terraform plan and terraform apply for supplying input variable values

**Question**:
An engineer is writing a deployment script. They need to pass input variable values to both the plan and apply steps. Which TWO of the following flags are valid on **both** `terraform plan` and `terraform apply`? (Select two.)

- A) **`-var "region=us-east-1"`** — passes a single variable value inline; accepted by both plan and apply
- B) `-approve` — skips the apply confirmation prompt; only valid on apply
- C) `-out=plan.tfplan` — saves the plan to a file; only valid on plan
- D) **`-var-file=prod.tfvars`** — loads variable values from a `.tfvars` file; accepted by both plan and apply

---

### Question 37 — Applying a Saved Plan File Skips the Confirmation Prompt

**Difficulty**: Medium
**Answer Type**: one
**Topic**: When terraform apply is given a saved plan file as an argument, it does not pause for interactive confirmation — the plan was already reviewed

**Question**:
Complete the following statement:

> "When `terraform apply` is given a saved plan file as its argument — for example, `terraform apply plan.tfplan` — it does ___________ pause to prompt `Do you want to perform these actions?` because the operator reviewed the plan before saving it."

What word fills the blank?

- A) always
- B) sometimes
- C) only briefly
- D) **not**

---

### Question 38 — `terraform console` is an Interactive REPL

**Difficulty**: Hard
**Answer Type**: one
**Topic**: terraform console is an interactive REPL for evaluating HCL expressions, testing functions, and inspecting state values without modifying anything

**Question**:
Complete the following description:

> "`terraform console` opens an interactive ___________ (Read-Eval-Print Loop) where engineers can type HCL expressions — such as `length([\"a\",\"b\",\"c\"])` or `format(\"%s-%s\", var.env, var.region)` — and immediately see the evaluated result. This is useful for testing functions and expressions before using them in configuration files."

What acronym fills the blank?

- A) CLI
- B) API
- C) IDE
- D) **REPL**

---

### Question 39 — TWO Items That `terraform init` Downloads and Configures

**Difficulty**: Hard
**Answer Type**: many
**Topic**: terraform init downloads provider plugin binaries AND caches module source code — both go into subdirectories of .terraform/

**Question**:
A developer runs `terraform init` in a working directory that has both `required_providers` declarations and `module` blocks sourcing external modules. Which TWO items does `terraform init` download and set up in the working directory? (Select two.)

- A) **Provider plugin binaries** — downloaded from the Terraform Registry (or a mirror) into `.terraform/providers/`, based on the `required_providers` block; the exact versions installed are recorded in `.terraform.lock.hcl`
- B) The Terraform Core binary itself — `terraform init` checks for a newer CLI version and auto-updates the `terraform` executable
- C) **Module source code** — external module sources (registry modules, Git repos, or HTTP archives referenced in `module` blocks) are downloaded and cached into `.terraform/modules/`, making them available for plan and apply
- D) The `terraform.tfstate` file — `terraform init` bootstraps an empty state file if one does not already exist

---

### Question 40 — `ignore_changes` Prevents Drift Detection

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

### Question 41 — TWO Correct Statements About the `moved` Block

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

### Question 42 — Default Parallelism Value

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

### Question 43 — `replace_triggered_by` Forces Replacement on Dependency Change

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

### Question 44 — `ignore_changes = all`

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

### Question 45 — `removed` Block with `destroy = false`

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

### Question 46 — Data Sources Read During `apply` for Computed Values

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

### Question 47 — Aliased Provider Reference Syntax

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

### Question 48 — TWO Consequences of Frequent `-target` Usage

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

### Question 49 — Destroy Order Is the Reverse of Creation Order

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

### Question 50 — `depends_on` for IAM Policy Attachment

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

### Question 51 — Resource Address Format from Root Module

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

### Question 52 — TWO Collection Types Usable Directly with `for_each`

**Difficulty**: Hard
**Answer Type**: many
**Topic**: for_each accepts only map or set(string) values directly — a list(string) must be converted with toset() first; tuples and other collection types are not supported

**Question**:
Which TWO collection types can be passed directly to the `for_each` meta-argument **without any conversion function**? (Select two.)

- A) `list(string)` — e.g., `for_each = ["us-east-1", "us-west-2"]`
- B) **`set(string)` — e.g., `for_each = toset(["us-east-1", "us-west-2"])` where the argument's type is a set; also accepted when the variable is already declared as `set(string)`**
- C) **`map(string)` — e.g., `for_each = { web = "t3.micro", db = "r5.large" }`; each.key = "web" or "db", each.value = the instance type string**
- D) `tuple` — e.g., `for_each = ["us-east-1", true, 80]`

---

### Question 53 — `nullable = false` Prevents Null Assignment

**Difficulty**: Easy
**Answer Type**: one
**Topic**: The nullable argument on a variable controls whether callers can explicitly pass null — setting nullable = false makes the variable reject null even though variables accept null by default

**Question**:
A module declares a required string variable and wants to ensure callers can never explicitly pass `null` — even though Terraform variables accept `null` by default. Complete the variable block:

```hcl
variable "environment" {
  type        = string
  description = "Deployment environment"
  ___________ = false
}
```

What argument fills the blank?

- A) `required`
- B) `non_null`
- C) `allow_null`
- D) `nullable`

---

### Question 54 — `count.index` Is Zero-Based

**Difficulty**: Easy
**Answer Type**: one
**Topic**: count.index provides the zero-based position of the current resource instance when the count meta-argument is used

**Question**:
Complete the resource block to tag each EC2 instance with a unique name that includes its zero-based position number:

```hcl
resource "aws_instance" "web" {
  count         = 3
  ami           = "ami-0abc123"
  instance_type = "t3.micro"

  tags = {
    Name = "web-server-${___________}"
  }
}
```

What expression fills the blank?

- A) `count.number`
- B) `count.position`
- C) `count.id`
- D) `count.index`

---

### Question 55 — Referencing a Child Module Output

**Difficulty**: Easy
**Answer Type**: one
**Topic**: A parent module accesses a child module's output using the syntax module.<module_label>.<output_name>

**Question**:
A root configuration calls a child module that exposes an output named `public_subnet_id`. Complete the resource block to use that output as the subnet for an EC2 instance:

```hcl
module "network" {
  source = "./modules/network"
}

resource "aws_instance" "web" {
  ami       = data.aws_ami.ubuntu.id
  subnet_id = ___________
}
```

What expression fills the blank?

- A) `network.public_subnet_id`
- B) `var.network.public_subnet_id`
- C) `output.network.public_subnet_id`
- D) `module.network.public_subnet_id`

---

### Question 56 — `flatten()` Removes Nesting from a List of Lists

**Difficulty**: Medium
**Answer Type**: one
**Topic**: The flatten() function collapses a nested list-of-lists into a single flat list — useful when for expressions or module outputs produce lists of lists

**Question**:
A local value aggregates subnet IDs across two availability zones, producing a list of lists. Complete the local to produce a single flat list:

```hcl
locals {
  nested_ids = [
    ["subnet-aaa", "subnet-bbb"],
    ["subnet-ccc", "subnet-ddd"],
  ]
  all_subnet_ids = ___________(local.nested_ids)
}
```

After evaluation, `local.all_subnet_ids` should be `["subnet-aaa", "subnet-bbb", "subnet-ccc", "subnet-ddd"]`. What function fills the blank?

- A) `concat()`
- B) `merge()`
- C) `tolist()`
- D) `flatten()`

---

### Question 57 — `compact()` Removes Nulls and Empty Strings

**Difficulty**: Medium
**Answer Type**: one
**Topic**: The compact() function removes null values and empty strings from a list — useful for cleaning up optional or conditionally populated lists before using them as resource arguments

**Question**:
A local builds a list of security group IDs where some entries may be empty strings (from conditionally created resources). Complete the local to remove the empty strings:

```hcl
locals {
  raw_sg_ids   = ["sg-aaa", "", "sg-bbb", ""]
  clean_sg_ids = ___________(local.raw_sg_ids)
}
```

After evaluation, `local.clean_sg_ids` should be `["sg-aaa", "sg-bbb"]`. What function fills the blank?

- A) `distinct()`
- B) `trim()`
- C) `filter()`
- D) `compact()`

---

### Question 58 — `merge()` Combines Maps with Later Values Winning

**Difficulty**: Medium
**Answer Type**: one
**Topic**: The merge() function combines multiple maps — when the same key appears in more than one argument, the value from the rightmost (last) argument wins

**Question**:
Complete the local so that the final tags map combines default tags with environment-specific overrides — and when both maps share a key, the environment-specific value takes precedence:

```hcl
locals {
  default_tags = {
    ManagedBy   = "terraform"
    Environment = "unknown"
  }

  env_tags = {
    Environment = var.environment
    Team        = "platform"
  }

  final_tags = ___________(local.default_tags, local.env_tags)
}
```

What function fills the blank so that `Environment` uses `var.environment` instead of `"unknown"`?

- A) `concat()`
- B) `zipmap()`
- C) `coalesce()`
- D) `merge()`

---

### Question 59 — `jsonencode()` Serialises a Value to JSON

**Difficulty**: Medium
**Answer Type**: one
**Topic**: The jsonencode() function converts any Terraform value (map, list, object) to its JSON string representation — commonly used for inline IAM policies and ECS task definitions

**Question**:
An IAM policy document is constructed as a Terraform map and must be serialised to a JSON string for the `policy` argument. Complete the resource block:

```hcl
resource "aws_iam_role_policy" "s3_read" {
  name = "s3-read"
  role = aws_iam_role.app.id

  policy = ___________(
    {
      Version = "2012-10-17"
      Statement = [
        {
          Effect   = "Allow"
          Action   = ["s3:GetObject"]
          Resource = "*"
        }
      ]
    }
  )
}
```

What function fills the blank?

- A) `tojson()`
- B) `encode_json()`
- C) `json()`
- D) `jsonencode()`

---

### Question 60 — `dynamic` Block Iterator Variable Defaults to the Block Type Label

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Inside a dynamic block's content, the iterator variable name defaults to the block type label — used to access each.value and each.key for the current element

**Question**:
A `dynamic` block generates multiple `ingress` rules for a security group. Complete the `content` block to reference the current rule's `from_port`:

```hcl
resource "aws_security_group" "web" {
  name = "web-sg"

  dynamic "ingress" {
    for_each = var.ingress_rules

    content {
      from_port   = ___________.value.from_port
      to_port     = ingress.value.to_port
      protocol    = ingress.value.protocol
      cidr_blocks = ["0.0.0.0/0"]
    }
  }
}
```

What iterator variable name fills the blank?

- A) `each`
- B) `self`
- C) `item`
- D) `ingress`

---

### Question 61 — Splat Expression Extracts an Attribute from Every Instance

**Difficulty**: Medium
**Answer Type**: one
**Topic**: The splat expression [*] extracts the same attribute from every element of a list-type resource reference — it is shorthand for a for expression iterating the list

**Question**:
Three EC2 instances are created with `count = 3`. An output should expose all three instance IDs as a list. Complete the output value:

```hcl
resource "aws_instance" "web" {
  count         = 3
  ami           = "ami-0abc123"
  instance_type = "t3.micro"
}

output "all_instance_ids" {
  value = aws_instance.web___________.id
}
```

What expression fills the blank (inserted between `web` and `.id`) to collect all IDs as a list?

- A) `[0]`
- B) `.all`
- C) `[count]`
- D) `[*]`

---

### Question 62 — TWO Correct Statements About the `try()` Function

**Difficulty**: Medium
**Answer Type**: many
**Topic**: try() evaluates each expression left to right and returns the first one that does not produce an error — it is the idiomatic fallback pattern for optional map keys or absent object attributes

**Question**:
Which TWO of the following statements about the `try()` function are correct? (Select two.)

- A) `try(expr1, expr2, ...)` evaluates each expression left to right and returns the result of the first expression that does not produce an error — if `expr1` errors, Terraform silently tries `expr2`, and so on
- B) `try()` is equivalent to a standard ternary conditional — it evaluates both branches and chooses based on the truthiness of the first argument
- C) `try()` can safely access a potentially absent map key: `try(var.settings["optional_key"], "default_value")` returns `"default_value"` if `"optional_key"` is absent or if accessing it produces any error
- D) `try()` only accepts string expressions — using it with numeric or boolean expressions causes a type error

---

### Question 63 — `templatefile()` Uses `path.module` for Reliable Template Paths

**Difficulty**: Hard
**Answer Type**: one
**Topic**: templatefile(path, vars) renders a file as a template substituting supplied variables — path.module provides the path to the current module directory, ensuring the file is found regardless of where terraform is invoked

**Question**:
A module needs to generate EC2 user data by rendering a shell script template stored in the same directory as the module's `.tf` files. Complete the `user_data` argument:

```hcl
resource "aws_instance" "app" {
  ami           = data.aws_ami.ubuntu.id
  instance_type = "t3.micro"

  user_data = templatefile("${___________}/user_data.sh.tpl", {
    environment = var.environment
    app_name    = local.app_name
  })
}
```

What path variable fills the blank?

- A) `path.root`
- B) `path.cwd`
- C) `path.workspace`
- D) `path.module`

---

### Question 64 — `cidrsubnet()` Arguments: prefix, newbits, netnum

**Difficulty**: Hard
**Answer Type**: one
**Topic**: cidrsubnet(prefix, newbits, netnum) divides a CIDR block into subnets — newbits is the additional bits borrowed from the host portion to extend the prefix length, and netnum is the zero-based subnet index

**Question**:
A VPC uses `10.0.0.0/16`. An engineer wants to compute the second subnet (`netnum = 1`) with a `/24` prefix. Borrowing 8 bits from the host portion of a `/16` produces `/24` subnets. Complete the expression:

```hcl
locals {
  subnet_cidr = cidrsubnet("10.0.0.0/16", ___________, 1)
}
```

What value fills the blank so that `local.subnet_cidr` evaluates to `"10.0.1.0/24"`?

- A) `4`
- B) `16`
- C) `24`
- D) `8`

---

### Question 65 — TWO Correct Statements About `for` Expression `if` Filter Clauses

**Difficulty**: Hard
**Answer Type**: many
**Topic**: A for expression can include an if clause to filter elements — the clause is optional, works in both list and map comprehensions, and can call built-in functions in its condition

**Question**:
Which TWO of the following statements about `for` expressions with `if` filter clauses are correct? (Select two.)

- A) An `if` clause in a `for` expression filters the output — only elements for which the condition is `true` are included: `[for n in var.names : n if length(n) > 4]` returns only names longer than 4 characters
- B) The `if` clause is mandatory in a `for` expression — omitting it causes a validation error because Terraform cannot determine which elements to include
- C) The `if` clause works in both list comprehensions `[for ...]` and map comprehensions `{for ...}` — `{for k, v in var.servers : k => v if v != ""}` is valid and produces a map containing only entries whose value is non-empty
- D) A `for` expression `if` clause can reference variables and locals, but cannot call built-in functions such as `length()`, `contains()`, or `startswith()` — function calls inside `if` clauses are a syntax error

---

### Question 66 — `check` Block Terraform Version

**Difficulty**: Easy
**Answer Type**: one
**Topic**: Which Terraform version introduced the `check` block

**Question**:
Complete the statement with the correct Terraform version:

> "The `check` block for top-level infrastructure health assertions was introduced in Terraform ___________."

- A) `0.14`
- B) `1.0`
- C) `1.3`
- D) `1.5`

---

### Question 67 — `sensitive = true` on an Output Block

**Difficulty**: Easy
**Answer Type**: one
**Topic**: The argument that prevents an output value from appearing in terminal output

**Question**:
Complete the output block so that the database connection endpoint does not appear in plain text during `terraform apply` or `terraform output`:

```hcl
output "db_connection_string" {
  value       = aws_db_instance.main.endpoint
  description = "Database connection endpoint"
  ___________ = true
}
```

- A) `secret`
- B) `masked`
- C) `redact`
- D) `sensitive`

---

### Question 68 — `self` Keyword Inside a `postcondition`

**Difficulty**: Easy
**Answer Type**: one
**Topic**: Which keyword references the resource's post-change attributes inside a `postcondition`

**Question**:
Complete the `postcondition` condition to verify that the EC2 instance has a public IP address after it is created:

```hcl
resource "aws_instance" "app" {
  ami           = data.aws_ami.ubuntu.id
  instance_type = "t3.micro"

  lifecycle {
    postcondition {
      condition     = ___________.public_ip != null
      error_message = "Instance must have a public IP address."
    }
  }
}
```

- A) `resource`
- B) `this`
- C) `aws_instance`
- D) `self`

---

### Question 69 — `error_message` Argument in a `validation` Block

**Difficulty**: Medium
**Answer Type**: one
**Topic**: The argument name that provides user feedback when a validation condition fails

**Question**:
Complete the `validation` block with the argument that supplies the message Terraform displays when the condition evaluates to `false`:

```hcl
variable "instance_count" {
  type = number

  validation {
    condition     = var.instance_count >= 1 && var.instance_count <= 10
    ___________ = "instance_count must be between 1 and 10."
  }
}
```

- A) `message`
- B) `error`
- C) `fail_message`
- D) `error_message`

---

### Question 70 — `precondition` Block Inside `lifecycle`

**Difficulty**: Medium
**Answer Type**: one
**Topic**: The block type name for asserting prerequisites before a resource is changed

**Question**:
An engineer wants to verify that the selected AMI is `x86_64` architecture before creating the EC2 instance. Complete the `lifecycle` block with the correct assertion block type:

```hcl
resource "aws_instance" "web" {
  ami           = data.aws_ami.ubuntu.id
  instance_type = var.instance_type

  lifecycle {
    ___________ {
      condition     = data.aws_ami.ubuntu.architecture == "x86_64"
      error_message = "The selected AMI must be x86_64 architecture."
    }
  }
}
```

- A) `assert`
- B) `validation`
- C) `check`
- D) `precondition`

---

### Question 71 — `check` Block Outer Structure

**Difficulty**: Medium
**Answer Type**: one
**Topic**: The top-level block keyword that contains a scoped `data` source and an `assert` block

**Question**:
Complete the outer block declaration that creates a named health monitor containing a scoped `data` source and an `assert`:

```hcl
___________ "app_health" {
  data "http" "probe" {
    url = "https://${aws_lb.web.dns_name}/health"
  }

  assert {
    condition     = data.http.probe.status_code == 200
    error_message = "Health check returned ${data.http.probe.status_code}, expected 200."
  }
}
```

- A) `lifecycle`
- B) `monitor`
- C) `validation`
- D) `check`

---

### Question 72 — `can()` Function in a `check` Block Assertion

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Using `can()` inside a `check` block to test whether an attribute expression succeeds

**Question**:
Complete the `check` block assertion to verify that the database endpoint can be successfully converted to a string — indicating it has been assigned and is accessible:

```hcl
check "database_accessible" {
  assert {
    condition     = ___________(tostring(aws_db_instance.main.endpoint))
    error_message = "Database endpoint is not accessible or not yet assigned."
  }
}
```

- A) `try()`
- B) `is_valid()`
- C) `coalesce()`
- D) `can()`

---

### Question 73 — `nonsensitive()` Function

**Difficulty**: Medium
**Answer Type**: one
**Topic**: The function that removes the sensitive marking from a value to allow it in a non-sensitive output

**Question**:
A variable is marked sensitive, but after a security review the team confirms this particular value is safe to display. Complete the output to explicitly remove the sensitive marking:

```hcl
variable "cluster_name" {
  type      = string
  sensitive = true
}

output "cluster_name_display" {
  value = ___________(var.cluster_name)
}
```

- A) `reveal()`
- B) `plaintext()`
- C) `expose()`
- D) `nonsensitive()`

---

### Question 74 — `check` Block: Version and Execution Timing

**Difficulty**: Medium
**Answer Type**: many
**Topic**: When the check block runs and which Terraform version introduced it

**Question**:
Which **TWO** of the following statements about the `check` block are correct?

- A) The `check` block was introduced in Terraform `1.5`
- B) A failing `check` block `assert` halts `terraform apply` with a non-zero exit code, preventing the deployment from completing
- C) The `check` block runs on every `terraform plan` AND every `terraform apply` — not just on apply
- D) The `check` block can only be declared inside a resource's `lifecycle` block — it is not a top-level block type

---

### Question 75 — `postcondition`: `self` and Failure Behaviour

**Difficulty**: Medium
**Answer Type**: many
**Topic**: What postcondition self references and how a failing postcondition affects apply

**Question**:
Which **TWO** of the following statements about `postcondition` blocks are correct?

- A) A `postcondition` runs **before** the resource is created or modified — if the condition fails, the resource change is prevented
- B) Inside a `postcondition`, the `self` keyword references the resource as it exists **after the change has completed** — including attributes only known after creation, such as `public_ip` or `id`
- C) A failing `postcondition` condition halts the apply **after** the resource has been changed, exits with a non-zero status code, and marks the run as failed
- D) `postcondition` blocks can only reference `var.<name>` values — they cannot use `self` or reference other resource attributes

---

### Question 76 — Vault Provider Data Source Type

**Difficulty**: Hard
**Answer Type**: one
**Topic**: The correct Vault provider data source type for reading a key-value secret

**Question**:
An engineer uses the HashiCorp Vault provider to dynamically fetch database credentials at apply time. Complete the `data` block with the correct Vault data source type:

```hcl
data "___________" "db_creds" {
  path = "secret/database/prod"
}

resource "aws_db_instance" "main" {
  username = data.db_creds.data["username"]
  password = data.db_creds.data["password"]
}
```

- A) `vault_secret`
- B) `vault_kv_secret`
- C) `vault_generic_secret`
- D) `vault_database_secret`

---

### Question 77 — `precondition` Is the Wrong Tool for Post-Creation Checks

**Difficulty**: Hard
**Answer Type**: one
**Topic**: Why a postcondition must be used (not a precondition) to verify a newly created resource attribute

**Question**:
An engineer writes the following lifecycle block expecting to verify that the EC2 instance has a public IP after creation:

```hcl
resource "aws_instance" "web" {
  ami           = data.aws_ami.ubuntu.id
  instance_type = "t3.micro"

  lifecycle {
    precondition {
      condition     = self.public_ip != null
      error_message = "Instance must have a public IP."
    }
  }
}
```

Why is this the wrong assertion mechanism for this check?

- A) The `precondition` block does not support boolean expressions — it requires a numeric comparison
- B) The `precondition` runs **before** the resource is created or updated — for a brand-new resource, `self.public_ip` will always be `null` at that point because the instance has not been provisioned yet; the correct tool is a `postcondition`, which runs **after** the resource change and where `self` references the resource's newly created attributes
- C) `self` is not a valid reference inside any `lifecycle` block — both `precondition` and `postcondition` must reference other resources by their full resource address
- D) The issue is that `public_ip` is not a valid attribute of `aws_instance` — the correct attribute is `public_ip_address`

---

### Question 78 — Vault Dynamic Secrets: Two Correct Statements

**Difficulty**: Hard
**Answer Type**: many
**Topic**: What the Vault provider pattern achieves and what it does not protect

**Question**:
Which **TWO** of the following statements about using the HashiCorp Vault provider to supply dynamic secrets to Terraform are correct?

- A) When the `vault_generic_secret` data source is used, Terraform reads credentials from Vault at plan/apply time — the credentials are not stored as literals in any Terraform `.tf` configuration file or `.tfvars` file
- B) Values retrieved from Vault data sources are automatically excluded from `terraform.tfstate` — the Vault integration is specifically designed to prevent secrets from appearing in state
- C) The Vault provider pattern prevents static, long-lived credentials from being embedded in Terraform configuration files — this reduces the risk of secrets being committed to source control
- D) Using the Vault provider means Terraform never stores the retrieved secret values anywhere — neither in state nor in memory during execution

---

### Question 79 — Terraform Registry Module Source Format

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

### Question 80 — Child Module Output Block Value

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

### Question 81 — `terraform init` Module Caching

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

### Question 82 — `~>` Compatible Version Constraint

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

### Question 83 — HTTP Archive Module Source

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

### Question 84 — `versions.tf` Convention

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

### Question 85 — Explicit Variable Passing to a Child Module

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

### Question 86 — Indexing Into a Module List Output

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

### Question 87 — Generic Git SSH Module Source

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

### Question 88 — Module Composition: Two Correct Statements

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

### Question 89 — Standard Module Structure: Input Variables File

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

### Question 90 — `modules.json` After `terraform init`

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

### Question 91 — S3 and GCS Module Sources: Two Correct Statements

**Difficulty**: Hard
**Answer Type**: many
**Topic**: Valid S3 and GCS module source syntax, and the scope of the `version` argument

**Question**:
Which **TWO** of the following statements about Terraform module sources are correct?

- A) An Amazon S3 bucket can be used as a module source using the `s3::` prefix — for example: `"s3::https://s3-us-west-2.amazonaws.com/mybucket/vpc.zip"`
- B) All module source types — including local paths, Git URLs, S3 buckets, and HTTP archives — support the `version` argument in the `module` block to pin the downloaded version
- C) A Google Cloud Storage (GCS) bucket can be used as a module source using the `gcs::` prefix — for example: `"gcs::https://www.googleapis.com/storage/v1/mybucket/vpc.zip"`
- D) GitHub module sources using the bare `github.com/...` format do not support subdirectory selection — the `//` double-slash convention is only valid when using the `git::https://` prefix

---

### Question 92 — `terraform force-unlock` Command Syntax

**Difficulty**: Easy
**Answer Type**: one
**Topic**: Correct syntax for releasing a stuck state lock using `terraform force-unlock`

**Question**:
Complete the command used to forcibly release a stuck state lock when the lock ID is `abc-12345`:

```bash
terraform ___________ abc-12345
```

- A) `state unlock`
- B) `unlock-state`
- C) `force-unlock`
- D) `state release`

---

### Question 93 — `terraform login` Credential Storage Location

**Difficulty**: Easy
**Answer Type**: one
**Topic**: Where `terraform login` writes the API token for HCP Terraform authentication

**Question**:
Complete the sentence: After running `terraform login` and authenticating via the browser, the API token is stored in ___________.

- A) `~/.terraform/credentials.json`
- B) `~/.terraform.d/credentials.tfrc.json`
- C) `./terraform.tfvars` in the working directory
- D) `~/.config/terraform/token`

---

### Question 94 — TF_LOG Verbosity Ordering

**Difficulty**: Easy
**Answer Type**: many
**Topic**: Correct relative verbosity of `TF_LOG` levels and which level is the most verbose

**Question**:
Which **TWO** of the following statements about `TF_LOG` log levels are correct?

- A) `TRACE` is the most verbose level — it captures all API calls, full request/response bodies, and internal Terraform core operations; `DEBUG` is the next level down
- B) `WARN` produces more output than `INFO` — warnings include all informational messages plus additional warning-level detail
- C) The full verbosity order from most to least verbose is: `TRACE > DEBUG > INFO > WARN > ERROR`; setting a level includes all messages at that level and less verbose levels — `INFO` would show `INFO`, `WARN`, and `ERROR` messages
- D) `ERROR` and `OFF` are the same — setting `TF_LOG=ERROR` disables logging just as `TF_LOG=OFF` does

---

### Question 95 — `terraform state mv` to Rename a Resource

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Using `terraform state mv` to rename a resource address in state without destroying it

**Question**:
Complete the command to rename the resource `aws_instance.web` to `aws_instance.web_server` in state without destroying or recreating the infrastructure:

```bash
terraform state mv ___________ ___________
```

- A) `aws_instance.web` `aws_instance.web_server`
- B) `--from aws_instance.web` `--to aws_instance.web_server`
- C) `"aws_instance" "web"` `"aws_instance" "web_server"`
- D) `-source=aws_instance.web` `-dest=aws_instance.web_server`

---

### Question 96 — `terraform init` Flag to Migrate State to a New Backend

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Which `terraform init` flag to use when changing backends and you want to transfer existing state

**Question**:
An engineer adds an S3 backend to a previously local-only configuration and wants to migrate the existing `terraform.tfstate` to the new S3 bucket. Complete the command:

```bash
terraform init ___________
```

- A) `-backend-migrate`
- B) `-reconfigure`
- C) `-migrate-state`
- D) `-force-copy`

---

### Question 97 — `cloud` Block Workspace Selection by Tags

**Difficulty**: Medium
**Answer Type**: one
**Topic**: How to configure the `cloud` block to select workspaces matching a set of tags rather than a single name

**Question**:
Complete the `cloud` block so the configuration targets all HCP Terraform workspaces tagged with `env=production`:

```hcl
terraform {
  cloud {
    organization = "acme-corp"

    workspaces {
      ___________ = ["env=production"]
    }
  }
}
```

- A) `filter`
- B) `name`
- C) `tags`
- D) `labels`

---

### Question 98 — `TF_TOKEN_` Environment Variable for HCP Terraform

**Difficulty**: Medium
**Answer Type**: one
**Topic**: The exact environment variable name used to provide an HCP Terraform API token in CI/CD pipelines

**Question**:
Complete the environment variable export that provides a Terraform API token for `app.terraform.io` without running `terraform login`:

```bash
export ___________="your-api-token-here"
```

- A) `TF_API_TOKEN`
- B) `TF_CLOUD_TOKEN`
- C) `TF_TOKEN_app_terraform_io`
- D) `TERRAFORM_CLOUD_CREDENTIAL`

---

### Question 99 — `terraform_remote_state` Backend Type for HCP Terraform

**Difficulty**: Medium
**Answer Type**: one
**Topic**: The correct `backend` value in a `terraform_remote_state` data source when reading from an HCP Terraform workspace

**Question**:
Complete the `terraform_remote_state` data source to read outputs from another HCP Terraform workspace named `networking-production`:

```hcl
data "terraform_remote_state" "networking" {
  backend = "___________"
  config = {
    organization = "acme-corp"
    workspaces = {
      name = "networking-production"
    }
  }
}
```

- A) `"hcp"`
- B) `"cloud"`
- C) `"remote"`
- D) `"terraform_cloud"`

---

### Question 100 — Sentinel Policy Enforcement Level That Cannot Be Overridden

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Which HCP Terraform policy enforcement level blocks a run and cannot be overridden by any user

**Question**:
Complete the sentence: A Sentinel or OPA policy set with enforcement level ___________ will block a run when the policy fails, and **no user in the organisation — including owners — can override the failure**.

- A) `soft-mandatory`
- B) `advisory`
- C) `blocking`
- D) `hard-mandatory`

---

### Question 101 — Private Registry Module Source Format

**Difficulty**: Medium
**Answer Type**: one
**Topic**: The source string format for referencing a module from an HCP Terraform private registry

**Question**:
Complete the `source` argument to reference a module named `vpc` published in the `my-org` HCP Terraform private registry under the `aws` provider:

```hcl
module "vpc" {
  source  = "___________"
  version = "~> 2.1"
}
```

- A) `"private.terraform.io/my-org/vpc/aws"`
- B) `"my-org/vpc/aws"`
- C) `"app.terraform.io/my-org/vpc/aws"`
- D) `"registry.terraform.io/private/my-org/vpc/aws"`

---

### Question 102 — Sentinel vs OPA: Two Correct Statements

**Difficulty**: Medium
**Answer Type**: many
**Topic**: Differences between Sentinel (HashiCorp DSL) and OPA (Rego) as HCP Terraform policy frameworks

**Question**:
Which **TWO** of the following statements about HCP Terraform policy enforcement are correct?

- A) Sentinel uses HashiCorp's own domain-specific language (DSL); OPA (Open Policy Agent) policies are written in Rego — both frameworks are supported natively in HCP Terraform as policy enforcement options
- B) Sentinel and OPA are mutually exclusive — an HCP Terraform organisation must choose one framework and cannot use both simultaneously
- C) Both Sentinel and OPA policy sets can be assigned enforcement levels: `advisory`, `soft-mandatory`, or `hard-mandatory`
- D) OPA policies can only be used for cost estimation checks; Sentinel is the only framework that can evaluate Terraform plan data for resource-level policy enforcement

---

### Question 103 — `TF_LOG_CORE` and `TF_LOG_PROVIDER` Env Vars

**Difficulty**: Hard
**Answer Type**: one
**Topic**: Using `TF_LOG_CORE` and `TF_LOG_PROVIDER` to get separate log streams for the Terraform core binary and provider plugins

**Question**:
An engineer wants to see `DEBUG`-level logs from the Terraform core binary only, while seeing `TRACE`-level logs from provider plugins only. Complete the environment variable exports:

```bash
export ___________=DEBUG
export ___________=TRACE
```

- A) `TF_LOG_BINARY` and `TF_LOG_PLUGINS`
- B) `TF_LOG_CORE` and `TF_LOG_PROVIDER`
- C) `TF_CORE_LOG` and `TF_PROVIDER_LOG`
- D) `TF_LOG_TERRAFORM` and `TF_LOG_PLUGIN`

---

### Question 104 — HCP Terraform Health Assessments: Underlying Command

**Difficulty**: Hard
**Answer Type**: one
**Topic**: What operation HCP Terraform Health Assessments perform on a configurable schedule to detect infrastructure drift

**Question**:
Complete the sentence: HCP Terraform Health Assessments work by automatically running ___________ on a configurable schedule — if the result shows drift between actual cloud resources and Terraform state, the assessment is marked as unhealthy and notifications can be triggered.

- A) `terraform apply -refresh-only` — reconciling state with actual resources on every scheduled run
- B) `terraform validate` — checking configuration syntax and provider schema compliance
- C) `terraform plan -refresh-only` — detecting drift without modifying state or infrastructure
- D) `terraform state pull` — downloading and comparing the remote state to the cloud resource API responses



## Answer Key

| Q# | Answer(s) | Explanation | Source | Difficulty |
|---|---|---|---|---|
| 2 | D | N/A | Repeatability — the IaC benefit that guarantees the same code deploys identical environments across staging and production | Easy |
| 3 | C | N/A | Completing a basic `aws_instance` resource block — the argument that specifies the EC2 instance type | Easy |
| 4 | C | N/A | Completing the definition of declarative IaC — configurations express the desired end state | Easy |
| 5 | D | N/A | Using `count = 0` to declare that no instances of a resource should exist, while keeping the block in configuration | Medium |
| 6 | D | N/A | Completing the definition of infrastructure drift — when actual cloud resources diverge from the Terraform configuration | Medium |
| 7 | D | N/A | The IaC benefit that provides a historical record of every infrastructure change via version control commits | Medium |
| 8 | B, D | N/A | Distinguishing provisioning tools (Terraform category) from configuration management tools — CloudFormation and Pulumi are provisioning tools | Medium |
| 9 | B | N/A | IaC configuration files serve as living documentation of infrastructure | Medium |
| 10 | D | N/A | In a declarative IaC approach, the engineer describes WHAT the infrastructure should look like — not the steps to create it | Medium |
| 11 | B | N/A | Using a ternary conditional expression to set count = 1 when a boolean variable is true, otherwise count = 0 | Medium |
| 12 | A, D | N/A | Identifying which IaC benefits directly address the reproducibility and drift problems of the manual ClickOps approach | Medium |
| 13 | D | N/A | Completing an HCL block declaration — the `resource` keyword identifies a managed infrastructure object | Hard |
| 14 | A, D | N/A | Terraform's multi-cloud support and open-source/non-vendor-locked nature versus CloudFormation's AWS-only scope | Hard |
| 15 | C | N/A | The `required_version` argument sets the minimum Terraform CLI version required to use this configuration | Easy |
| 16 | D | N/A | The default hostname in a Terraform provider source address is registry.terraform.io when no hostname is specified | Easy |
| 17 | D | N/A | The -upgrade flag on terraform init advances locked provider versions to the newest versions satisfying constraints | Easy |
| 18 | D | N/A | A resource block references an aliased provider using the `provider = <type>.<alias>` syntax | Medium |
| 19 | D | N/A | Terraform keeps only one .tfstate.backup file — the previous state from the most recent apply | Medium |
| 20 | D | N/A | The -refresh=false flag skips live API queries and plans against the cached state — faster but potentially stale | Medium |
| 21 | D | N/A | The -json flag on terraform show outputs state in machine-readable JSON format suitable for parsing by scripts | Medium |
| 22 | D | N/A | terraform state pull downloads the current remote state and writes it to stdout for inspection or backup | Medium |
| 23 | D | N/A | sensitive = true only controls terminal display — the value is still written to state in plaintext | Medium |
| 24 | D | N/A | One of the four state purposes is performance caching — avoiding live API queries for every resource on every plan | Medium |
| 25 | A, C | N/A | Local state has no locking and no sharing — both are required for team collaboration and production safety | Medium |
| 26 | D | N/A | Terraform Core communicates with provider plugins over gRPC — providers run as separate processes | Hard |
| 27 | A, C | N/A | Each provider entry in the lock file contains the exact installed version and cryptographic hashes — both are required for reproducibility and verification | Hard |
| 28 | C | N/A | The `-out` flag saves the execution plan to a binary file for a deterministic later apply | Easy |
| 29 | D | N/A | The -raw flag outputs a single output value as a plain string without surrounding quotes — suitable for shell variable assignment | Easy |
| 30 | D | N/A | The workspace show subcommand prints the name of the currently active workspace | Easy |
| 31 | D | N/A | The -diff flag prints the formatting diff to stdout without modifying any files on disk | Medium |
| 32 | D | N/A | The -destroy flag on terraform plan shows a preview of what terraform destroy would remove, without making any changes | Medium |
| 33 | A, C | N/A | Both + (pure create) and -/+ (replacement — destroy then create) result in a new resource existing after apply | Medium |
| 34 | D | N/A | The -replace flag forces a specific resource to be destroyed and recreated — the current replacement for the deprecated terraform taint command | Medium |
| 35 | D | N/A | The -reconfigure flag forces terraform init to reconfigure the backend without migrating or asking about existing state | Medium |
| 36 | D | N/A | terraform graph outputs the resource dependency graph in DOT language format — renderable by Graphviz | Medium |
| 37 | A, D | N/A | -var and -var-file are valid flags on both terraform plan and terraform apply for supplying input variable values | Medium |
| 38 | D | N/A | When terraform apply is given a saved plan file as an argument, it does not pause for interactive confirmation — the plan was already reviewed | Medium |
| 39 | D | N/A | terraform console is an interactive REPL for evaluating HCL expressions, testing functions, and inspecting state values without modifying anything | Hard |
| 40 | A, C | N/A | terraform init downloads provider plugin binaries AND caches module source code — both go into subdirectories of .terraform/ | Hard |
| 41 | D | N/A | The ignore_changes lifecycle argument tells Terraform to ignore drift for listed attributes — useful when a resource auto-manages its own tags or other fields outside Terraform | Easy |
| 42 | A, C | N/A | The moved block records a state rename or relocation — it allows resources to be renamed or moved into modules without destroy and recreate | Easy |
| 43 | D | N/A | Terraform's default concurrent operations limit is 10 — controllable with -parallelism | Easy |
| 44 | D | N/A | The replace_triggered_by lifecycle argument forces the resource to be replaced whenever a referenced resource or attribute changes — useful for propagating changes through indirectly linked resources like ASG and launch template | Medium |
| 45 | D | N/A | ignore_changes = all tells Terraform to ignore ALL attribute drift for a resource — the resource is created once and never updated by Terraform thereafter | Medium |
| 46 | D | N/A | The removed block with destroy = false stops Terraform from tracking a resource without destroying the underlying cloud object | Medium |
| 47 | D | N/A | Data sources are normally evaluated during plan — but if their arguments depend on values that are not known until apply (computed values), they are deferred and read during the apply phase instead | Medium |
| 48 | D | N/A | When a provider has an alias, a resource references it with the provider meta-argument using the syntax provider = <provider_name>.<alias> | Medium |
| 49 | A, C | N/A | Using -target for partial applies is convenient but should be used sparingly — it can cause state drift and leaves other resources out of sync | Medium |
| 50 | D | N/A | Terraform builds a dependency graph for both creation and destruction — destroy operations execute in topological reverse order so that dependents are removed before their dependencies | Medium |
| 51 | D | N/A | depends_on is used when Terraform cannot detect a real dependency through attribute references — the most common case is IAM permissions that must propagate before a resource can use them | Medium |
| 52 | D | N/A | When referencing a managed resource from the root module context, the full address includes the module prefix: module.<module_name>.<resource_type>.<resource_name> | Hard |
| 53 | B, C | N/A | for_each accepts only map or set(string) values directly — a list(string) must be converted with toset() first; tuples and other collection types are not supported | Hard |
| 54 | D | N/A | The nullable argument on a variable controls whether callers can explicitly pass null — setting nullable = false makes the variable reject null even though variables accept null by default | Easy |
| 55 | D | N/A | count.index provides the zero-based position of the current resource instance when the count meta-argument is used | Easy |
| 56 | D | N/A | A parent module accesses a child module's output using the syntax module.<module_label>.<output_name> | Easy |
| 57 | D | N/A | The flatten() function collapses a nested list-of-lists into a single flat list — useful when for expressions or module outputs produce lists of lists | Medium |
| 58 | D | N/A | The compact() function removes null values and empty strings from a list — useful for cleaning up optional or conditionally populated lists before using them as resource arguments | Medium |
| 59 | D | N/A | The merge() function combines multiple maps — when the same key appears in more than one argument, the value from the rightmost (last) argument wins | Medium |
| 60 | D | N/A | The jsonencode() function converts any Terraform value (map, list, object) to its JSON string representation — commonly used for inline IAM policies and ECS task definitions | Medium |
| 61 | D | N/A | Inside a dynamic block's content, the iterator variable name defaults to the block type label — used to access each.value and each.key for the current element | Medium |
| 62 | D | N/A | The splat expression [*] extracts the same attribute from every element of a list-type resource reference — it is shorthand for a for expression iterating the list | Medium |
| 63 | A, C | N/A | try() evaluates each expression left to right and returns the first one that does not produce an error — it is the idiomatic fallback pattern for optional map keys or absent object attributes | Medium |
| 64 | D | N/A | templatefile(path, vars) renders a file as a template substituting supplied variables — path.module provides the path to the current module directory, ensuring the file is found regardless of where terraform is invoked | Hard |
| 65 | D | N/A | cidrsubnet(prefix, newbits, netnum) divides a CIDR block into subnets — newbits is the additional bits borrowed from the host portion to extend the prefix length, and netnum is the zero-based subnet index | Hard |
| 66 | A, C | N/A | A for expression can include an if clause to filter elements — the clause is optional, works in both list and map comprehensions, and can call built-in functions in its condition | Hard |
| 67 | D | N/A | Which Terraform version introduced the `check` block | Easy |
| 68 | D | N/A | The argument that prevents an output value from appearing in terminal output | Easy |
| 69 | D | N/A | Which keyword references the resource's post-change attributes inside a `postcondition` | Easy |
| 70 | D | N/A | The argument name that provides user feedback when a validation condition fails | Medium |
| 71 | D | N/A | The block type name for asserting prerequisites before a resource is changed | Medium |
| 72 | D | N/A | The top-level block keyword that contains a scoped `data` source and an `assert` block | Medium |
| 73 | D | N/A | Using `can()` inside a `check` block to test whether an attribute expression succeeds | Medium |
| 74 | D | N/A | The function that removes the sensitive marking from a value to allow it in a non-sensitive output | Medium |
| 75 | A, C | N/A | When the check block runs and which Terraform version introduced it | Medium |
| 76 | B, C | N/A | What postcondition self references and how a failing postcondition affects apply | Medium |
| 77 | C | N/A | The correct Vault provider data source type for reading a key-value secret | Hard |
| 78 | B | N/A | Why a postcondition must be used (not a precondition) to verify a newly created resource attribute | Hard |
| 79 | A, C | N/A | What the Vault provider pattern achieves and what it does not protect | Hard |
| 80 | C | N/A | The three-part `NAMESPACE/MODULE/PROVIDER` format for a Terraform Registry module source | Easy |
| 81 | D | N/A | Completing the `value` argument in a child module output block to expose a resource attribute | Easy |
| 82 | A, D | N/A | What `terraform init` writes for module caching and what `.terraform/modules/` contains | Easy |
| 83 | C | N/A | What the pessimistic constraint operator `~>` means in a module `version` argument | Medium |
| 84 | D | N/A | How to reference a module hosted as a downloadable ZIP archive at an HTTPS URL | Medium |
| 85 | C | N/A | The conventional filename for `required_providers` and Terraform version constraints in a module | Medium |
| 86 | C | N/A | How to explicitly pass a root module variable to a child module input argument | Medium |
| 87 | D | N/A | How to access a single element from a child module output that returns a list | Medium |
| 88 | C | N/A | The correct prefix for a module sourced from a Git repository over SSH | Medium |
| 89 | B, D | N/A | How Terraform supports nested module calls and multiple child modules from the root | Medium |
| 90 | D | N/A | Which file in the standard module structure holds all input `variable` block declarations | Medium |
| 91 | B | N/A | What Terraform records in `.terraform/modules/modules.json` after running `terraform init` | Hard |
| 92 | A, C | N/A | Valid S3 and GCS module source syntax, and the scope of the `version` argument | Hard |
| 93 | C | N/A | Correct syntax for releasing a stuck state lock using `terraform force-unlock` | Easy |
| 94 | B | N/A | Where `terraform login` writes the API token for HCP Terraform authentication | Easy |
| 95 | A, C | N/A | Correct relative verbosity of `TF_LOG` levels and which level is the most verbose | Easy |
| 96 | A | N/A | Using `terraform state mv` to rename a resource address in state without destroying it | Medium |
| 97 | C | N/A | Which `terraform init` flag to use when changing backends and you want to transfer existing state | Medium |
| 98 | C | N/A | How to configure the `cloud` block to select workspaces matching a set of tags rather than a single name | Medium |
| 99 | C | N/A | The exact environment variable name used to provide an HCP Terraform API token in CI/CD pipelines | Medium |
| 100 | C | N/A | The correct `backend` value in a `terraform_remote_state` data source when reading from an HCP Terraform workspace | Medium |
| 101 | D | N/A | Which HCP Terraform policy enforcement level blocks a run and cannot be overridden by any user | Medium |
| 102 | C | N/A | The source string format for referencing a module from an HCP Terraform private registry | Medium |
| 103 | A, C | N/A | Differences between Sentinel (HashiCorp DSL) and OPA (Rego) as HCP Terraform policy frameworks | Medium |
| 104 | B | N/A | Using `TF_LOG_CORE` and `TF_LOG_PROVIDER` to get separate log streams for the Terraform core binary and provider plugins | Hard |
| 105 | C | N/A | What operation HCP Terraform Health Assessments perform on a configurable schedule to detect infrastructure drift | Hard |
