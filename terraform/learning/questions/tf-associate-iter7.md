# Terraform Associate (004) — Question Bank Iter 7 Batch 1

**Iteration**: 7
**Iteration Style**: Fill-in-the-blank / complete the HCL — given a partial configuration or partial statement, select the term or argument that correctly fills the blank
**Batch**: 1
**Objective**: 1 — IaC Concepts
**Generated**: 2026-04-25
**Total Questions**: 13
**Difficulty Split**: 3 Easy / 8 Medium / 2 Hard
**Answer Types**: 10 `one` / 3 `many` / 0 `none`

---

# Terraform Associate (004) — Question Bank Iter 7 Batch 2

**Iteration**: 7
**Iteration Style**: Fill-in-the-blank / complete the HCL — given a partial configuration or partial statement, select the term or argument that correctly fills the blank
**Batch**: 2
**Objective**: 2 — Terraform Fundamentals (Providers & State)
**Generated**: 2026-04-25
**Total Questions**: 13
**Difficulty Split**: 3 Easy / 8 Medium / 2 Hard
**Answer Types**: 10 `one` / 3 `many` / 0 `none`

---

# Terraform Associate (004) — Question Bank Iter 7 Batch 3

**Iteration**: 7
**Iteration Style**: Fill-in-the-blank / complete the HCL — given a partial configuration or partial statement, select the term or argument that correctly fills the blank
**Batch**: 3
**Objective**: 3 — Core Workflow & CLI
**Generated**: 2026-04-25
**Total Questions**: 13
**Difficulty Split**: 3 Easy / 8 Medium / 2 Hard
**Answer Types**: 10 `one` / 3 `many` / 0 `none`

---

# Terraform Associate (004) — Question Bank Iter 7 Batch 4

**Iteration**: 7
**Iteration Style**: Fill-in-the-blank / complete the HCL — given a partial configuration or partial statement, select the term or argument that correctly fills the blank
**Batch**: 4
**Objective**: 4 — Resources, Data & Dependencies (prompt05 + prompt09)
**Generated**: 2026-04-25
**Total Questions**: 13
**Difficulty Split**: 3 Easy / 8 Medium / 2 Hard
**Answer Types**: 10 `one` / 3 `many` / 0 `none`

---

# Terraform Associate (004) — Question Bank Iter 7 Batch 5

**Iteration**: 7
**Iteration Style**: Fill-in-the-blank / complete the HCL — given a partial configuration or partial statement, select the term or argument that correctly fills the blank
**Batch**: 5
**Objective**: 4b — Variables, Outputs, Types & Functions (prompt06 + prompt07 + prompt08)
**Generated**: 2026-04-25
**Total Questions**: 13
**Difficulty Split**: 3 Easy / 8 Medium / 2 Hard
**Answer Types**: 10 `one` / 3 `many` / 0 `none`

---

# Terraform Associate (004) — Question Bank Iter 7 Batch 6

**Iteration**: 7
**Iteration Style**: Fill-in-the-blank / complete the HCL — every question presents a partial HCL snippet or partial statement with a `___________` placeholder; select which option correctly fills the blank
**Batch**: 6
**Objective**: 4c — Custom Conditions & Sensitive Data
**Generated**: 2026-04-25
**Total Questions**: 13
**Difficulty Split**: 3 Easy / 8 Medium / 2 Hard
**Answer Types**: 10 `one` / 3 `many` / 0 `none`

---

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

# Terraform Associate (004) — Question Bank Iter 7 Batch 8

**Iteration**: 7
**Iteration Style**: Fill-in-the-blank / complete the HCL — every question presents a partial HCL snippet or partial statement with a `___________` placeholder; select which option correctly fills the blank
**Batch**: 8
**Objectives**: 6 (State Backends & Locking) + 7 (Importing & State Inspection) + 8 (HCP Terraform)
**Source Prompts**: prompt12, prompt13, prompt14, prompt15
**Generated**: 2026-04-25
**Total Questions**: 13
**Difficulty Split**: 3 Easy / 8 Medium / 2 Hard
**Answer Types**: 10 `one` / 3 `many` / 0 `none`

---

---

## Questions

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

**Answer**: D

**Explanation**:
Repeatability is one of the core IaC benefits listed in Terraform learning materials: "Same code → identical environment every time." Because infrastructure is described as version-controlled code, any environment — staging, production, QA, disaster-recovery — can be provisioned from the same configuration and will produce structurally identical results. Atomicity, convergence, and modularity are related software engineering concepts but are not the named IaC benefit for this property.

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

**Answer**: C

**Explanation**:
In the `aws_instance` resource, the argument `instance_type` sets the EC2 instance family and size (e.g., `"t3.micro"`, `"m5.large"`). The argument name is specific to the AWS provider. `machine_type` is the equivalent argument name in the `google_compute_instance` resource (GCP); `instance_size` does not exist in any major provider; `type` is a meta-argument used for resource type alias patterns but not for setting the instance family here.

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

**Answer**: C

**Explanation**:
The core characteristic of a declarative IaC tool like Terraform is that you describe the **desired** end state — what you want to exist — rather than the **procedural** or **imperative** sequence of commands to create it. Terraform then compares that desired state against the current tracked state and calculates the minimum set of actions (create, update, or destroy) to reconcile the difference. "Scripted" and "imperative" describe the opposite approach, where an operator writes step-by-step instructions.

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

**Answer**: D

**Explanation**:
Setting `count = 0` tells Terraform the desired number of instances of this resource is zero. If any instances currently exist in state, Terraform plans to destroy them; if none exist, no action is taken. The resource block remains in the configuration file as documentation of the resource's definition without affecting infrastructure. `null` and `false` are not valid values for `count`; `"disabled"` is a string and would cause a type error since `count` requires a non-negative integer.

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

**Answer**: D

**Explanation**:
**Drift** is the specific term used in Terraform (and IaC tooling in general) for the condition where the actual state of cloud resources no longer matches what the configuration declares as the desired state. Drift is caused by out-of-band changes: manual console modifications, other automation tools acting on the same resources, auto-scaling events, or provider-side changes. Terraform can detect drift by comparing the refreshed state (queried from the cloud API) against the configuration during `terraform plan`. "Divergence" is a synonymous English word but not the recognised technical IaC term used in Terraform documentation and exam objectives.

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

**Answer**: D

**Explanation**:
An **audit trail** is one of the explicitly listed IaC benefits that addresses a key limitation of the manual ClickOps approach: "No audit trail — who changed what and when?" By defining infrastructure as code in a version-controlled repository, every change becomes a commit with a timestamp, author, and diff. This is valuable for security reviews, compliance audits, incident post-mortems, and team collaboration. `terraform.tfstate.backup` is the previous state file (not an audit history); plan output shows a proposed diff but is not a persistent change record.

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

**Answer**: B, D

**Explanation**:
**Provisioning tools** create and manage cloud infrastructure resources (virtual machines, networks, storage, databases). **AWS CloudFormation** (B) and **Pulumi** (D) are both provisioning tools — they declare and manage cloud infrastructure, placing them in the same category as Terraform. **Ansible** (A) and **Chef** (C) are primarily **configuration management tools** — they manage the state of software, packages, files, and services on existing servers, rather than provisioning the servers themselves. (Note: tools like Ansible have some infrastructure provisioning modules, but their primary classification is configuration management.)

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

**Answer**: B

**Explanation**:
**Documentation** is one of the listed IaC benefits: "Config files serve as living documentation of infrastructure." Because the configuration file must exactly match the deployed infrastructure (otherwise Terraform would show a diff on the next plan), the `.tf` files are always a current, accurate description of what exists. This is qualitatively different from separate documentation files that can fall out of sync. New team members can read the configuration files to understand the entire infrastructure without needing knowledge transfer from the original authors. "Manifests" is used in Kubernetes contexts; "backups" and "snapshots" describe point-in-time copies.

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

**Answer**: D

**Explanation**:
The fundamental distinction between declarative and imperative tools is **what** vs **how**. Terraform's HCL configuration says "I want 3 EC2 instances of type `t3.micro` in `us-east-1`" — it declares the desired end state (**what**). Terraform then handles the **how**: calling the AWS EC2 `RunInstances` API, waiting for provisioning to complete, writing state, etc. An imperative tool (like a shell script) would require the engineer to write each of those steps explicitly. This "what not how" principle is why Terraform can detect changes and only apply the minimum necessary modifications — it always works toward the declared desired state, regardless of the current state.

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

**Answer**: B

**Explanation**:
The `count` meta-argument requires a non-negative integer value. The ternary expression `var.create_bastion ? 1 : 0` evaluates to `1` when `create_bastion` is `true` (creating one instance) and `0` when it is `false` (creating no instances). `true` is a boolean and would cause a type error since `count` expects a number. `"enabled"` is a string — also invalid. `var.bastion_count` would work if such a variable existed, but it is not declared and would be an error. The `bool ? 1 : 0` conditional count pattern is the canonical Terraform idiom for optional resource creation.

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

**Answer**: A, D

**Explanation**:
**(A)** addresses the **repeatability** and **environment consistency** problem of ClickOps: manually provisioned environments inevitably diverge because different operators make different changes at different times. IaC solves this by using the same code as the single source of truth for all environments. **(D)** addresses the **drift detection** capability: IaC tools can query the cloud API to compare actual resource attributes against the configuration and flag deviations, a capability that is impossible with manual approaches. **(B)** is false — IaC still communicates with cloud providers; nothing is simulated. **(C)** is false — HCL is interpreted, not compiled, and provisioning speed is dominated by cloud API latency, not the configuration format.

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

**Answer**: D

**Explanation**:
In Terraform HCL, the `resource` keyword identifies a **managed resource** — infrastructure that Terraform creates, reads, updates, and destroys through the lifecycle of the configuration. The block structure is `resource "<TYPE>" "<NAME>" { ... }`. Each of the four available block keywords serves a distinct purpose: `data` declares a **data source** (read-only lookup of existing infrastructure or external data); `module` calls a **child module** (reusable configuration bundle); `provider` configures a **provider** (the plugin that communicates with a cloud API). Using `data "aws_s3_bucket" "assets" { ... }` would attempt to look up an existing bucket by name, not create one.

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

**Answer**: A, D

**Explanation**:
**(A)** is accurate and is the primary technical advantage: Terraform's provider model supports multi-cloud management from a single tool. AWS CloudFormation exclusively manages AWS resources; there is no CloudFormation equivalent for Azure or GCP resources. **(D)** is also accurate and states the organisational implication: adopting Terraform means teams build skills and workflows that are reusable across any cloud provider — avoiding vendor lock-in at the tooling layer. **(B)** is false — CloudFormation is also declarative; you declare desired stacks in JSON or YAML templates, and CloudFormation reconciles them. **(C)** is false — cost estimation in Terraform is an HCP Terraform feature, not a CLI feature for all resource types; CloudFormation also has cost estimation through AWS Cost Calculator integrations.

---

---

## Questions

---

### Question 1 — `required_version` in the `terraform` Block

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

**Answer**: C

**Explanation**:
`required_version` is the argument in the `terraform {}` block that constrains which versions of the Terraform CLI can execute the configuration. If a team member runs an older CLI that does not satisfy the constraint (e.g., Terraform 1.3.x with `>= 1.5`), Terraform will immediately return an error and refuse to proceed. This prevents accidental use of older CLI versions that may behave differently or lack features the configuration depends on. The argument name is `required_version` — not `minimum_version`, `terraform_version`, or `cli_version`, which do not exist.

---

### Question 2 — Default Registry Hostname in Provider Source Addresses

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

**Answer**: D

**Explanation**:
Provider source addresses follow the format `<hostname>/<namespace>/<type>`. When the hostname is omitted — as in the short form `"hashicorp/aws"` — Terraform uses the default hostname `registry.terraform.io`. The fully qualified address is therefore `registry.terraform.io/hashicorp/aws`. This is the public Terraform Provider Registry where Official, Partner, and Community providers are hosted. `releases.hashicorp.com` is where HashiCorp CLI binaries are distributed; `app.terraform.io` is the HCP Terraform (formerly Terraform Cloud) hostname; neither is the default provider registry host.

---

### Question 3 — `terraform init -upgrade` Flag

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

**Answer**: D

**Explanation**:
`terraform init -upgrade` instructs Terraform to ignore the existing lock file and re-resolve all providers to the newest versions that satisfy the declared constraints. After the upgrade, it writes the new versions and updated checksums back to `.terraform.lock.hcl`. This is the correct deliberate workflow for advancing provider versions: run `terraform init -upgrade`, review the updated lock file diff, commit the new lock file to version control. Without `-upgrade`, `terraform init` honours the existing lock file and will not install a newer version even if one is available. `-reconfigure` is for backend reconfiguration, not provider versions.

---

### Question 4 — Provider Alias Reference in a Resource Block

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

**Answer**: D

**Explanation**:
The `provider` meta-argument in a resource block takes the value `<provider_type>.<alias>` — written **without quotes** as a reference expression, not a string. For an AWS provider with `alias = "europe"`, the reference is `aws.europe`. The format is always the provider type label (matching the key in `required_providers`, e.g., `aws`) followed by a dot and the alias name. `"aws.europe"` (with quotes) would be a string literal — not a provider reference — and would cause a validation error. `"europe"` alone is missing the provider type prefix. Using the correct unquoted `aws.europe` reference tells Terraform to use the `eu-west-1` provider configuration for this resource.

---

### Question 5 — `terraform.tfstate.backup` — Only One Backup Kept

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

**Answer**: D

**Explanation**:
`terraform.tfstate.backup` is overwritten on every apply — it always contains the state from the **most recently completed** apply, not the one before that or an original snapshot. Terraform does not maintain a rolling history of state files locally; the backup file provides only one level of undo. This is why remote backends with versioning enabled (such as S3 with `versioning = true`) are strongly recommended for production use — they retain the full history of every state version, allowing recovery from any previous point. After each successful apply: the old `terraform.tfstate` becomes the new `terraform.tfstate.backup`, and the newly written state becomes the new `terraform.tfstate`.

---

### Question 6 — `terraform plan -refresh=false`

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

**Answer**: D

**Explanation**:
`terraform plan -refresh=false` tells Terraform to skip the live resource refresh step and generate the plan entirely from the values cached in the state file. This significantly reduces planning time in large environments where API round-trips dominate. The trade-off is that any drift — resources changed outside Terraform since the last apply — will not be detected. This flag is appropriate when you have high confidence that the state file accurately reflects reality (e.g., immediately after a clean apply in a controlled environment). `-no-refresh`, `-fast`, and `-cached` are not valid Terraform flags. The correct syntax is `-refresh=false` (using the equals form).

---

### Question 7 — `terraform show -json` for Machine-Readable State

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

**Answer**: D

**Explanation**:
`terraform show` without flags produces a human-readable text representation of the current state — useful for reading in a terminal but not suitable for scripting. Adding the `-json` flag switches the output format to structured JSON, which can be parsed by tools like `jq`, processed by CI scripts, or consumed by other automation. This is the standard approach for extracting specific resource attributes from state in automated pipelines. `terraform show plan.tfplan -json` also works to output a saved plan file as JSON. `-machine`, `-output`, and `-parse` are not valid `terraform show` flags.

---

### Question 8 — `terraform state pull` Writes to stdout

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

**Answer**: D

**Explanation**:
`terraform state pull` outputs the current state — whether from a local backend or a remote backend like S3 or HCP Terraform — directly to **stdout**. This makes it useful in two ways: (1) for inspection: pipe it to `jq` to query specific values (`terraform state pull | jq '.resources[] | select(.type=="aws_instance")'`); (2) for backup: redirect to a file (`terraform state pull > backup.tfstate`). Writing to stdout rather than to a fixed file preserves the existing `terraform.tfstate` on disk and gives the operator full control over what to do with the output. This is the read counterpart to `terraform state push`, which uploads a local file to the remote backend.

---

### Question 9 — `sensitive = true` Scope

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

**Answer**: D

**Explanation**:
`sensitive = true` on an output variable (or a variable declaration) instructs Terraform to mask the value in **terminal** display — replacing it with `(sensitive value)` when printing plan or apply output. It is a display-only protection. The underlying value is still written to `terraform.tfstate` in plaintext JSON, just like any other resource attribute. This is a critical security distinction: an operator who can read the state file (or run `terraform output -json`) can always retrieve sensitive values. Proper protection requires an **encrypted remote backend** (e.g., S3 with server-side encryption, HCP Terraform with native encryption) — not just `sensitive = true`. The exam frequently tests this "display-only, not encryption" distinction.

---

### Question 10 — Fourth State Purpose: Performance

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

**Answer**: D

**Explanation**:
The fourth explicitly named purpose of Terraform state is **performance**. In a large infrastructure with hundreds or thousands of resources, querying every resource's current attributes from the cloud API on every plan would be prohibitively slow. The state file caches resource attributes from the last apply, so Terraform can compute the plan diff using local data without a complete API refresh. When a full refresh is needed, `terraform plan` (without `-refresh=false`) still queries the API to detect drift, but the cached state means the refresh is targeted rather than exhaustive. The other three purposes — identity mapping, diff computation, and metadata — are equally important but performance is a commonly overlooked fourth reason that state is required.

---

### Question 11 — TWO Limitations of Local State vs Remote State

**Difficulty**: Medium
**Answer Type**: many
**Topic**: Local state has no locking and no sharing — both are required for team collaboration and production safety

**Question**:
A solo developer has been using a local `terraform.tfstate` file for a prototype. Their team is now growing. Which TWO limitations of local state make it unsuitable for team use? (Select two.)

- A) **Local state has no locking** — when two team members run `terraform apply` concurrently, there is no mechanism to prevent both writes from corrupting the state file; remote backends like S3 + DynamoDB provide locking to ensure only one operation modifies state at a time
- B) Local state cannot store resource attribute values — it only stores resource addresses
- C) **Local state has no built-in sharing mechanism** — the `terraform.tfstate` file lives on one engineer's workstation; other team members cannot access it without manually copying the file, making collaboration impractical and error-prone; remote backends (S3, Azure Blob, HCP Terraform) store state in a location all team members can reach
- D) Local state cannot track more than 50 resources — it has a hard limit for small projects only

**Answer**: A, C

**Explanation**:
The two critical local state limitations for team environments are locking and sharing. **(A) No locking**: local state relies on OS file locking, which is unreliable across machines and completely absent when working with a shared file. Two concurrent `terraform apply` runs can interleave state writes, producing corrupted or inconsistent state. Remote backends provide atomic locking (DynamoDB for S3, native locking for HCP Terraform) that serialises operations. **(C) No sharing**: the `terraform.tfstate` file is just a local file. If Engineer A has it on their laptop, Engineer B cannot see current state without a manual file transfer — which introduces version conflicts, lost changes, and confusion about which copy is authoritative. Remote backends give all team members (and CI pipelines) a single shared source of truth. **(B)** is false — local state stores full attribute values. **(D)** is false — there is no resource count limit.

---

### Question 12 — gRPC Protocol Between Terraform Core and Provider

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

**Answer**: D

**Explanation**:
Terraform's plugin architecture uses **gRPC** (Google Remote Procedure Call) for communication between the Terraform Core binary and provider plugin processes. gRPC was chosen because it provides strong typing via Protocol Buffers, efficient binary serialisation, and bidirectional streaming — suitable for the high-frequency CRUD calls Terraform makes to providers during plan and apply. The separation into distinct processes means providers can be upgraded, versioned, and distributed independently of Terraform Core. The provider process, in turn, translates Terraform's gRPC calls into the specific HTTPS API calls required by the target service (AWS, Azure, GCP, etc.). REST, JSON-RPC, and SOAP are other RPC/API protocols but are not used for Terraform Core ↔ provider plugin communication.

---

### Question 13 — TWO Contents of a `.terraform.lock.hcl` Provider Entry

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

**Answer**: A, C

**Explanation**:
**(A)** The `version` property is the lock file's primary reproducibility mechanism — it pins the exact installed version so that `terraform init` on any machine at any future time installs `5.31.0`, not the newest `~> 5.0`-compatible version available at that moment. This is what makes provider installations deterministic across team members and CI pipelines. **(C)** The `hashes` array contains platform-specific cryptographic checksums (`h1:` prefix for the zip archive hash, `zh:` for the individual binary) that `terraform init` verifies on download. This prevents a compromised registry or man-in-the-middle attack from substituting a malicious binary without detection. **(B)** is false — `constraints` records what constraint was in effect when the version was selected, primarily for informational/audit purposes; it is not a fallback. **(D)** is false — hashes verify the **provider binary**, not the lock file itself.

---

---

## Questions

---

### Question 1 — Saving a Plan to a File with `-out`

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

**Answer**: C

**Explanation**:
`terraform plan -out=plan.tfplan` serialises the execution plan to a binary file called `plan.tfplan`. This file captures the exact proposed changes at the moment the plan was generated — including any variable values and the refreshed state. When `terraform apply plan.tfplan` is later run, Terraform applies precisely those changes without re-evaluating the configuration or prompting for confirmation. This two-stage pattern is the recommended CI/CD approach: plan in one job (get human or automated review), then apply the saved file in a separate job. The flag is `-out=<filename>` — not `-save`, `-export`, or `-write`.

---

### Question 2 — `terraform output -raw` for Scripting

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

**Answer**: D

**Explanation**:
`terraform output -raw <name>` outputs a single string output value with no surrounding quotes, no trailing newline when piped, and no additional formatting — making it suitable for direct shell variable assignment: `DB_HOST=$(terraform output -raw db_endpoint)`. Without `-raw`, `terraform output db_endpoint` prints the value with its type annotation and quotes. The `-json` flag (not shown as an option here) outputs all values as a JSON object. `-raw` is only valid for string-type outputs; using it on a list or map output will produce an error. `-plain`, `-string`, and `-noformat` are not valid `terraform output` flags.

---

### Question 3 — `terraform workspace show`

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

**Answer**: D

**Explanation**:
`terraform workspace show` prints the name of the currently active Terraform workspace to stdout — for example, `staging` or `default`. This is useful in scripts and shell prompts to conditionally behave based on the active workspace. The full workspace subcommand set is: `list` (show all), `new <name>` (create), `select <name>` (switch), `delete <name>` (remove), and `show` (display current). `current`, `active`, and `status` are not valid workspace subcommands.

---

### Question 4 — `terraform fmt -diff` Shows Changes Without Writing

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

**Answer**: D

**Explanation**:
`terraform fmt -diff` computes the canonical format for each `.tf` file and prints the diff to stdout (in unified diff format) without writing any changes to disk. This is useful when an engineer wants to review what formatting corrections would be made before committing to them. It differs from `-check`, which exits non-zero when files need formatting but produces no diff output. Combining both is possible: `terraform fmt -check -diff` exits non-zero AND shows the diff — a common CI pattern that both fails the build and provides actionable output. `-preview`, `-dry-run`, and `-show` are not valid `terraform fmt` flags.

---

### Question 5 — `terraform plan -destroy`

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

**Answer**: D

**Explanation**:
`terraform plan -destroy` produces an execution plan showing all the resources Terraform would remove if `terraform destroy` were run — using the familiar `-` prefix symbols in the output. No changes are made to infrastructure or state. This is the recommended pre-flight check before a destructive operation. The saved-plan variant also works: `terraform plan -destroy -out=destroy.tfplan` saves the destruction plan, which can then be reviewed and applied with `terraform apply destroy.tfplan` for a fully deterministic, reviewable destroy workflow. `terraform destroy` itself is equivalent to `terraform apply -destroy`, but neither performs a preview — they prompt for and then execute the destruction.

---

### Question 6 — TWO Plan Symbols That Result in a Net-New Resource After Apply

**Difficulty**: Medium
**Answer Type**: many
**Topic**: Both + (pure create) and -/+ (replacement — destroy then create) result in a new resource existing after apply

**Question**:
A `terraform plan` output contains four types of operations. Which TWO operation symbols result in a **brand-new resource object being created in the cloud** after `terraform apply` completes? (Select two.)

- A) **`+`** — a pure create: a new resource that does not yet exist will be provisioned
- B) `~` — an in-place update: the existing resource is modified without replacement
- C) **`-/+`** — a replacement: the existing resource is destroyed and a completely new one is created in its place
- D) `-` — a pure destroy: the existing resource is removed and nothing is created

**Answer**: A, C

**Explanation**:
**(A) `+`** represents a pure creation — Terraform will call the provider's Create API to provision a new resource that currently has no corresponding object in state or in the cloud. **(C) `-/+`** represents a replacement — Terraform must destroy the existing resource and create a brand-new one because the changed attribute (marked `# forces replacement`) cannot be modified in-place; after apply, a new resource with a new ID exists. **(B) `~`** is an in-place update — the same resource continues to exist with modified attribute values, no new object is created. **(D) `-`** is a pure destroy — the resource is removed and nothing is created in its place. Both `+` and `-/+` contribute to the "N to add" count in the plan summary line.

---

### Question 7 — `terraform apply -replace` to Force Recreate a Resource

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

**Answer**: D

**Explanation**:
`terraform apply -replace="aws_instance.web"` marks the specified resource for forced replacement: Terraform plans a `-/+` operation (destroy then create) for that resource even if its configuration has not changed, then immediately applies it. This is the current approach introduced in Terraform 0.15.2 and made the primary recommendation with `terraform taint` being deprecated. The `-replace` flag is preferred because it combines the "mark for replacement" and "apply" steps into a single operation with full plan visibility — the engineer sees the `-/+` in the plan before committing. `terraform taint` required a separate state-modification step and could be confusing. `-recreate`, `-taint`, and `-force-replace` are not valid flags.

---

### Question 8 — `terraform init -reconfigure`

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

**Answer**: D

**Explanation**:
`terraform init -reconfigure` forces Terraform to adopt the new backend configuration defined in the `terraform {}` block without asking about migrating existing state or consulting any previous backend configuration. It discards the cached backend configuration and starts fresh with what is currently declared. This is appropriate when: (1) state migration is handled by a separate out-of-band process, (2) switching to a completely different backend type, or (3) the CI environment should not be prompted interactively. The alternative, `terraform init -migrate-state`, attempts to copy the existing state to the new backend. `-force`, `-skip-migrate`, and `-reset` are not valid `terraform init` flags.

---

### Question 9 — `terraform graph` Outputs DOT Format

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

**Answer**: D

**Explanation**:
`terraform graph` outputs the dependency graph between all resources, data sources, and modules in a configuration using the **DOT** graph description language (defined by the Graphviz project). DOT is a simple plain-text format that describes nodes and edges. To turn the DOT output into a visual image, pipe it through Graphviz's `dot` command: `terraform graph | dot -Tsvg > graph.svg` (SVG) or `terraform graph | dot -Tpng > graph.png` (PNG). This is useful for understanding complex dependency chains, debugging unexpected plan ordering, or documenting infrastructure topology. JSON, XML, and Mermaid are not the output format of `terraform graph`.

---

### Question 10 — TWO Flags That Work on Both `terraform plan` and `terraform apply`

**Difficulty**: Medium
**Answer Type**: many
**Topic**: -var and -var-file are valid flags on both terraform plan and terraform apply for supplying input variable values

**Question**:
An engineer is writing a deployment script. They need to pass input variable values to both the plan and apply steps. Which TWO of the following flags are valid on **both** `terraform plan` and `terraform apply`? (Select two.)

- A) **`-var "region=us-east-1"`** — passes a single variable value inline; accepted by both plan and apply
- B) `-approve` — skips the apply confirmation prompt; only valid on apply
- C) `-out=plan.tfplan` — saves the plan to a file; only valid on plan
- D) **`-var-file=prod.tfvars`** — loads variable values from a `.tfvars` file; accepted by both plan and apply

**Answer**: A, D

**Explanation**:
Both `terraform plan` and `terraform apply` accept variable-supplying flags because both commands may need to evaluate the full configuration (and therefore resolve variable values). **(A) `-var "key=value"`** passes a single variable value inline and is valid on both. **(D) `-var-file=<file>`** loads a file of variable assignments (`.tfvars` format) and is also valid on both. Using the same flags on both commands ensures the plan and apply see identical variable values — critical for the two-stage CI pattern where `plan` and `apply` run as separate steps (though in that case a saved plan file is even better). **(B) `-approve`** does not exist — the flag is `-auto-approve`, and it only applies to `terraform apply`. **(C) `-out=`** saves a plan file and is only a `terraform plan` flag.

---

### Question 11 — Applying a Saved Plan File Skips the Confirmation Prompt

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

**Answer**: D

**Explanation**:
When you run `terraform apply plan.tfplan` (providing a saved plan file as the argument), Terraform applies the plan **without pausing for confirmation** — it assumes the operator already reviewed the output of `terraform plan -out=plan.tfplan` and is now intentionally executing those changes. This is one of the key reasons the two-stage `plan -out` → `apply <file>` pattern is used in CI/CD: it separates the review step (plan) from the execution step (apply) and makes the apply step deterministic and non-interactive without requiring the `-auto-approve` flag. In contrast, running `terraform apply` without a saved plan file always shows the plan and then pauses for confirmation unless `-auto-approve` is provided.

---

### Question 12 — `terraform console` is an Interactive REPL

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

**Answer**: D

**Explanation**:
`terraform console` is an interactive **REPL** (Read-Eval-Print Loop) — a shell-like interface where each expression entered is read, evaluated against the current configuration and state context, and its result printed immediately. Engineers use it to: experiment with built-in functions (`cidrsubnet`, `format`, `toset`, etc.) before putting them in `.tf` files; inspect computed values from state (e.g., `aws_instance.web.public_ip`); and verify that complex expressions like `for` expressions produce the expected output. The console does not modify infrastructure or state — it is purely a read/evaluate tool. `terraform console` requires `terraform init` to have been run (so providers and modules are available) but makes no cloud API calls.

---

### Question 13 — TWO Items That `terraform init` Downloads and Configures

**Difficulty**: Hard
**Answer Type**: many
**Topic**: terraform init downloads provider plugin binaries AND caches module source code — both go into subdirectories of .terraform/

**Question**:
A developer runs `terraform init` in a working directory that has both `required_providers` declarations and `module` blocks sourcing external modules. Which TWO items does `terraform init` download and set up in the working directory? (Select two.)

- A) **Provider plugin binaries** — downloaded from the Terraform Registry (or a mirror) into `.terraform/providers/`, based on the `required_providers` block; the exact versions installed are recorded in `.terraform.lock.hcl`
- B) The Terraform Core binary itself — `terraform init` checks for a newer CLI version and auto-updates the `terraform` executable
- C) **Module source code** — external module sources (registry modules, Git repos, or HTTP archives referenced in `module` blocks) are downloaded and cached into `.terraform/modules/`, making them available for plan and apply
- D) The `terraform.tfstate` file — `terraform init` bootstraps an empty state file if one does not already exist

**Answer**: A, C

**Explanation**:
`terraform init` performs three main setup operations: **(A)** it reads the `required_providers` block and downloads each provider plugin binary into `.terraform/providers/`, recording the exact version and checksum in `.terraform.lock.hcl`; **(C)** it reads all `module` blocks that reference external sources (Terraform Registry modules, Git URLs, HTTP archives, etc.) and downloads them into `.terraform/modules/`, making the module code available for subsequent plan/apply operations. It also configures the backend (if declared). **(B)** is false — `terraform init` never modifies the Terraform CLI binary itself; CLI upgrades are performed separately (e.g., via `tfenv`, package managers, or manual download). **(D)** is false — `terraform init` does not create `terraform.tfstate`; the state file is created on the first `terraform apply` when resources are provisioned.

---

---

## Questions

---

### Question 1 — `ignore_changes` Prevents Drift Detection

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

**Answer**: D

**Explanation**:
`ignore_changes` is a `lifecycle` meta-argument that accepts a list of attribute names (without quotes). When attributes are listed in `ignore_changes`, Terraform does not include them in its drift detection during plan — changes to those attributes in the real infrastructure are silently ignored rather than flagged as configuration drift. This is essential for resources like Auto Scaling Groups (`desired_capacity`), instances managed by spot schedulers (`instance_type`), or resources whose tags are modified by external tooling (`tags["LastModified"]`). `skip_changes`, `suppress_drift`, and `no_update` are not valid lifecycle arguments.

---

### Question 2 — TWO Correct Statements About the `moved` Block

**Difficulty**: Easy
**Answer Type**: many
**Topic**: The moved block records a state rename or relocation — it allows resources to be renamed or moved into modules without destroy and recreate

**Question**:
Which TWO of the following statements about the `moved` block are correct? (Select two.)

- A) **A `moved` block renames a resource in Terraform state — mapping the old address (`from`) to the new address (`to`) so that Terraform treats the existing cloud object as the resource at the new address, avoiding a destroy-and-recreate cycle**
- B) After a `moved` block is applied, it must remain in the configuration permanently — removing it causes Terraform to destroy the resource on the next apply
- C) **A `moved` block can also relocate a resource from the root module into a child module by setting `from = aws_instance.web` and `to = module.web_tier.aws_instance.server` — Terraform updates the state address without touching the cloud resource**
- D) The `moved` block requires running `terraform state mv` first before the block takes effect — it is a documentation-only declaration

**Answer**: A, C

**Explanation**:
**(A)** The `moved` block maps an old resource address (`from`) to a new address (`to`) in state. When Terraform processes a `moved` block during apply, it updates the state entry to use the new address — no destroy or create API calls are made. **(C)** `moved` also handles cross-module relocations: setting `from = aws_instance.web` and `to = module.web_tier.aws_instance.server` moves the state entry into the module's address namespace, reflecting the new code structure. **(B)** is false — after a successful apply that processes the `moved` block, the block can be safely removed from configuration; the resource is now tracked under its new address. **(D)** is false — `moved` is a live Terraform directive, not documentation-only; it does not require a separate `terraform state mv` command.

---

### Question 3 — Default Parallelism Value

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

**Answer**: D

**Explanation**:
Terraform's default parallelism limit is **10** — it will run at most 10 concurrent provider API calls (creates, updates, reads, destroys) at the same time for resources that have no dependency relationship. This value can be overridden: `terraform apply -parallelism=20` increases throughput for large configurations, while `terraform apply -parallelism=1` forces sequential execution (useful for debugging or for providers with strict rate limits). The dependency graph determines which operations *can* run in parallel — parallelism caps how many of those eligible operations execute simultaneously.

---

### Question 4 — `replace_triggered_by` Forces Replacement on Dependency Change

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

**Answer**: D

**Explanation**:
`replace_triggered_by` accepts a list of resource references (or specific resource attribute references). Whenever any of the listed resources change — even if the change doesn't affect an attribute that the current resource directly reads — Terraform plans a `-/+` (replace) operation for the resource. This is the correct way to propagate launch template changes through to an Auto Scaling Group: when the launch template is updated, `replace_triggered_by = [aws_launch_template.web]` ensures the ASG is also replaced, causing instances to be cycled with the new template configuration. `force_replace_on`, `triggers`, and `recreate_when` are not valid lifecycle arguments.

---

### Question 5 — `ignore_changes = all`

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

**Answer**: D

**Explanation**:
`ignore_changes = all` (without quotes, without brackets) is the special keyword form that tells Terraform to ignore drift on every attribute of the resource. After the resource is initially created, Terraform will never plan an update to it regardless of how much its real-world state diverges from the configuration — it is effectively "create-only" from Terraform's perspective. This is appropriate for resources fully managed by an external system after initial provisioning. The value `all` is a keyword, not a string literal — it must not be wrapped in quotes or brackets. `["*"]`, `[all]` (in brackets), and `"all"` (in quotes) are all invalid forms.

---

### Question 6 — `removed` Block with `destroy = false`

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

**Answer**: D

**Explanation**:
The `removed` block (introduced in Terraform 1.7) removes a resource from Terraform's state management. When `destroy = false`, Terraform removes the resource from the state file during the next apply but does **not** call the provider's Destroy API — the cloud object continues to exist and run independently. When `destroy = true`, Terraform removes the resource from state AND destroys the cloud object (equivalent to a normal removal of the resource block). The `removed` block requires specifying the `from` address of the resource being de-adopted. After apply, the `removed` block itself can be deleted from configuration. `null`, `"retain"`, and any other values are not valid for `destroy`.

---

### Question 7 — Data Sources Read During `apply` for Computed Values

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

**Answer**: D

**Explanation**:
Terraform evaluates data sources during the **plan** phase so that the plan output can show the full effect of all changes. However, if a data source's filter argument references a value that won't exist until a resource is created — for example, `id = aws_vpc.main.id` where `aws_vpc.main` is being created in the same apply — that value is "unknown" at plan time. In this case, Terraform defers the data source read until the **apply** phase, after the upstream resource is created and its `id` is known. The plan will show the data source result as "known after apply" rather than displaying the actual queried values.

---

### Question 8 — Aliased Provider Reference Syntax

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

**Answer**: D

**Explanation**:
The `provider` meta-argument on a resource block specifies which provider configuration the resource should use. When a provider has an alias, the syntax is `provider = <provider_name>.<alias>` — in this case `provider = aws.west`. Without this meta-argument, a resource automatically uses the default (non-aliased) provider configuration for its type. The `provider` meta-argument value uses dot notation but does **not** use quotes — `aws.west` is a provider reference expression, not a string. `region`, `alias`, and `configuration` are not valid meta-argument names on a resource block.

---

### Question 9 — TWO Consequences of Frequent `-target` Usage

**Difficulty**: Medium
**Answer Type**: many
**Topic**: Using -target for partial applies is convenient but should be used sparingly — it can cause state drift and leaves other resources out of sync

**Question**:
Which TWO of the following accurately describe a consequence or risk of using `terraform apply -target=<resource>` frequently? (Select two.)

- A) **State drift — resources not included in the `-target` scope are not refreshed or updated, so the state file may become inconsistent with the real infrastructure over time**
- B) `-target` permanently marks the targeted resource as "priority" in the state file — subsequent applies without `-target` will always process that resource first
- C) **Dependency chain gaps — if the targeted resource depends on other resources that also have pending changes, those dependencies may not be applied, leaving the configuration partially reconciled**
- D) Using `-target` disables all provider authentication — the apply runs in offline mode and only modifies the state file, not the real cloud infrastructure

**Answer**: A, C

**Explanation**:
**(A)** When `-target` scopes an apply to a subset of resources, all other resources in the configuration are skipped — they are not refreshed, updated, or validated. Over time this creates state drift: the state file may no longer accurately reflect the real state of non-targeted resources. **(C)** Even within the targeted resource's dependency chain, `-target` has a defined but narrow scope — it includes direct dependencies of the targeted resource but may miss transitive or sibling dependencies that also have pending changes. This can leave the overall configuration in a partially reconciled state where some dependent resources have changes that haven't been applied. Terraform itself warns: "Note: Objects have changed outside of Terraform" and recommends using `-target` only for exceptional situations. **(B)** is false — `-target` is a one-time flag with no persistent effect on the state file's resource ordering. **(D)** is false — `-target` applies normally against real cloud infrastructure with full provider authentication.

---

### Question 10 — Destroy Order Is the Reverse of Creation Order

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

**Answer**: D

**Explanation**:
Terraform's dependency graph drives both creation and destruction ordering, but in opposite directions. During creation, Terraform follows topological order: dependencies are created first (e.g., VPC → subnet → EC2 instance). During destruction, the order is **reversed**: dependents must be removed before the resources they depend on, so the EC2 instance is destroyed first, then the subnet, then the VPC. Attempting to destroy a resource that another resource still references would cause a provider API error (e.g., trying to delete a VPC that still has subnets). The reversed destroy order prevents these dependency violations automatically.

---

### Question 11 — `depends_on` for IAM Policy Attachment

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

**Answer**: D

**Explanation**:
`depends_on` is the meta-argument for declaring explicit dependencies that Terraform cannot infer from attribute references. In this case, the EC2 instance references `aws_iam_instance_profile.app.name` — but the instance profile's *attached policy* (`aws_iam_role_policy_attachment.s3_access`) has no attribute referenced by the instance. Without `depends_on`, Terraform might create the EC2 instance in parallel with or before the policy attachment, causing the instance to start before the IAM policy is active. The `depends_on` value is a list of resource references (not strings) — they must be bare references like `aws_iam_role_policy_attachment.s3_access`, not quoted names. `depends_on` should be used sparingly because it reduces Terraform's ability to parallelise operations.

---

### Question 12 — Resource Address Format from Root Module

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

**Answer**: D

**Explanation**:
The full resource address for a managed resource declared inside a child module follows the pattern `module.<MODULE_LABEL>.<RESOURCE_TYPE>.<RESOURCE_NAME>`. The `<MODULE_LABEL>` is the local name given to the module in the calling configuration's `module` block — in this case `web_tier` from `module "web_tier" { ... }`. The complete address is `module.web_tier.aws_instance.server`. This address format is used in `terraform state` commands, `-target` flags, `moved` blocks, and `removed` blocks. Within the child module itself, the resource is addressed as simply `aws_instance.server` — the `module.web_tier.` prefix is only needed from outside the module.

---

### Question 13 — TWO Collection Types Usable Directly with `for_each`

**Difficulty**: Hard
**Answer Type**: many
**Topic**: for_each accepts only map or set(string) values directly — a list(string) must be converted with toset() first; tuples and other collection types are not supported

**Question**:
Which TWO collection types can be passed directly to the `for_each` meta-argument **without any conversion function**? (Select two.)

- A) `list(string)` — e.g., `for_each = ["us-east-1", "us-west-2"]`
- B) **`set(string)` — e.g., `for_each = toset(["us-east-1", "us-west-2"])` where the argument's type is a set; also accepted when the variable is already declared as `set(string)`**
- C) **`map(string)` — e.g., `for_each = { web = "t3.micro", db = "r5.large" }`; each.key = "web" or "db", each.value = the instance type string**
- D) `tuple` — e.g., `for_each = ["us-east-1", true, 80]`

**Answer**: B, C

**Explanation**:
`for_each` accepts exactly two collection types directly: **(B) `set(string)`** — a set of unique string values; each element becomes both the instance key and `each.key` (with `each.value` also equal to `each.key` for a set); and **(C) `map(any)`** — a map where each key becomes the instance address key, `each.key` is the map key, and `each.value` is the corresponding map value. **(A) `list(string)`** cannot be used directly — Terraform rejects it because lists have numeric indexes and allow duplicates, which would make instance addresses ambiguous. The fix is to wrap the list with `toset()`: `for_each = toset(var.regions)`. **(D) Tuples** are not supported by `for_each` at all — they are ordered collections with mixed types and cannot be iterated with stable string keys.

---

---

## Questions

---

### Question 1 — `nullable = false` Prevents Null Assignment

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

**Answer**: D

**Explanation**:
By default, Terraform variables have `nullable = true` — a caller can explicitly pass `null` to any variable, overriding any `default` value (resulting in `null` being used). Setting `nullable = false` causes Terraform to reject `null` as a supplied value — if a caller passes `null`, Terraform returns a validation error. This is useful for required string or object variables where `null` would cause downstream errors. `required`, `non_null`, and `allow_null` are not valid variable block arguments; `nullable` is the correct argument.

---

### Question 2 — `count.index` Is Zero-Based

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

**Answer**: D

**Explanation**:
When `count` is used, Terraform exposes `count.index` inside the resource block — a zero-based integer representing which instance is currently being evaluated. For `count = 3`, the three instances have `count.index` values of `0`, `1`, and `2`. Instances are addressed externally as `aws_instance.web[0]`, `aws_instance.web[1]`, and `aws_instance.web[2]`. Interpolating `count.index` into a tag or name is the standard pattern for distinguishing `count`-created instances. `count.number`, `count.position`, and `count.id` are not valid — `count.index` is the only attribute exposed by the `count` object.

---

### Question 3 — Referencing a Child Module Output

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

**Answer**: D

**Explanation**:
Child module outputs are accessed from the parent module using `module.<MODULE_LABEL>.<OUTPUT_NAME>`. The `<MODULE_LABEL>` is the name given in the `module` block declaration — here `"network"`. The full reference is `module.network.public_subnet_id`. This reference also creates an implicit dependency: `aws_instance.web` will not be created until the `module.network` resources have been applied and `public_subnet_id` is known. `network.public_subnet_id` (missing the `module.` prefix), `var.network.public_subnet_id`, and `output.network.public_subnet_id` are all invalid reference formats.

---

### Question 4 — `flatten()` Removes Nesting from a List of Lists

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

**Answer**: D

**Explanation**:
`flatten(list)` takes a list that may contain nested lists (at any depth) and returns a single-level list of all elements. `flatten([["subnet-aaa", "subnet-bbb"], ["subnet-ccc", "subnet-ddd"]])` produces `["subnet-aaa", "subnet-bbb", "subnet-ccc", "subnet-ddd"]`. This is commonly needed when `for` expressions iterate over modules that each output a list, resulting in a list-of-lists. `concat()` joins multiple list *arguments* passed separately — it does not unwrap a pre-existing nested list variable. `merge()` is for maps. `tolist()` converts a set to a list but does not remove nesting.

---

### Question 5 — `compact()` Removes Nulls and Empty Strings

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

**Answer**: D

**Explanation**:
`compact(list)` returns a new list with all empty strings (`""`) and `null` values removed. It is specifically designed for cleaning up lists that may contain conditionally absent values. `distinct()` removes duplicate values but retains empty strings. `trim()` removes characters from the edges of a single string — it does not operate on lists. `filter()` is not a built-in Terraform function; filtering in Terraform is done with a `for` expression using an `if` condition: `[for v in local.raw_sg_ids : v if v != ""]`. `compact()` is the correct and idiomatic choice for this pattern.

---

### Question 6 — `merge()` Combines Maps with Later Values Winning

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

**Answer**: D

**Explanation**:
`merge(map1, map2, ...)` combines all provided maps into one. When the same key appears in multiple arguments, the value from the **rightmost (last) argument wins**. Here, `Environment = "unknown"` from `local.default_tags` is overridden by `Environment = var.environment` from `local.env_tags` because `local.env_tags` is the second argument. The result is `{ ManagedBy = "terraform", Environment = <var.environment>, Team = "platform" }`. This makes `merge()` the standard pattern for base-tags-plus-overrides composition. `concat()` joins lists, `zipmap()` creates a map from two separate key/value lists, and `coalesce()` returns the first non-null scalar value from a list of arguments.

---

### Question 7 — `jsonencode()` Serialises a Value to JSON

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

**Answer**: D

**Explanation**:
`jsonencode(value)` converts any Terraform value — a map, list, object, string, number, or bool — to its JSON string representation. It is the standard way to inline structured data (IAM policies, ECS task definitions, Lambda configurations) directly in HCL without a separate JSON file. The inverse is `jsondecode(str)`, which parses a JSON string back to a Terraform value. `tojson()`, `encode_json()`, and `json()` are not built-in Terraform functions — only `jsonencode()` and `jsondecode()` exist for JSON encoding/decoding.

---

### Question 8 — `dynamic` Block Iterator Variable Defaults to the Block Type Label

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

**Answer**: D

**Explanation**:
Inside a `dynamic` block's `content` body, the iterator variable defaults to the **same name as the block type label** — here `ingress`. You reference the current element's value with `ingress.value.<attribute>` and its key with `ingress.key`. This is analogous to `each.value` / `each.key` in a `for_each` resource block, but the variable name is derived from the `dynamic` block's label rather than being fixed as `each`. If the default name is unsuitable, you can override it with the `iterator` argument: adding `iterator = rule` inside the `dynamic` block means you'd write `rule.value.from_port` in `content`. `each`, `self`, and `item` are not the default iterator name — the block type label is.

---

### Question 9 — Splat Expression Extracts an Attribute from Every Instance

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

**Answer**: D

**Explanation**:
The splat expression `[*]` extracts a single named attribute from every element of a list resource reference. `aws_instance.web[*].id` is exactly equivalent to `[for r in aws_instance.web : r.id]` — it produces a `list(string)` containing the `id` of each of the three `count`-created instances. Splat expressions work on any `count`-based resource reference (which behaves as a list). They do not work directly on `for_each`-based resources (which produce maps); those require an explicit `for` expression: `[for k, v in aws_instance.server : v.id]`. `[0]` accesses only the first element. `.all` and `[count]` are not valid Terraform expressions.

---

### Question 10 — TWO Correct Statements About the `try()` Function

**Difficulty**: Medium
**Answer Type**: many
**Topic**: try() evaluates each expression left to right and returns the first one that does not produce an error — it is the idiomatic fallback pattern for optional map keys or absent object attributes

**Question**:
Which TWO of the following statements about the `try()` function are correct? (Select two.)

- A) `try(expr1, expr2, ...)` evaluates each expression left to right and returns the result of the first expression that does not produce an error — if `expr1` errors, Terraform silently tries `expr2`, and so on
- B) `try()` is equivalent to a standard ternary conditional — it evaluates both branches and chooses based on the truthiness of the first argument
- C) `try()` can safely access a potentially absent map key: `try(var.settings["optional_key"], "default_value")` returns `"default_value"` if `"optional_key"` is absent or if accessing it produces any error
- D) `try()` only accepts string expressions — using it with numeric or boolean expressions causes a type error

**Answer**: A, C

**Explanation**:
**(A)** `try()` accepts one or more expressions and evaluates them left to right. It returns the value of the first expression that succeeds without a runtime error. If all expressions error, Terraform raises an error. **(C)** A common use case is optional map key access: `try(var.settings["optional_key"], "default_value")`. If the key doesn't exist, the index expression errors, `try()` catches that silently, and returns `"default_value"`. **(B)** is false — `try()` is not a conditional; it does not test truthiness and does not evaluate branches in parallel. It is an error-catching mechanism that evaluates expressions in sequence. **(D)** is false — `try()` works with any Terraform expression type: strings, numbers, booleans, lists, maps, and objects.

---

### Question 11 — `templatefile()` Uses `path.module` for Reliable Template Paths

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

**Answer**: D

**Explanation**:
`path.module` is the filesystem path of the directory containing the current module's `.tf` files. Using `"${path.module}/user_data.sh.tpl"` ensures the template is found relative to the module that declares it — regardless of where `terraform` is invoked or whether the module is called from a different root. `path.root` refers to the root module's directory, which would break if this code lives in a child module. `path.cwd` is the process working directory at the time `terraform` is run — this changes based on where the CLI is invoked and is unsuitable for module-relative file references. `path.workspace` is not a valid Terraform path variable.

---

### Question 12 — `cidrsubnet()` Arguments: prefix, newbits, netnum

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

**Answer**: D

**Explanation**:
`cidrsubnet(prefix, newbits, netnum)` has three parameters: **prefix** — the base CIDR block; **newbits** — the number of *additional* bits to borrow from the host portion (extending the prefix length by that many bits); **netnum** — the zero-based index of the desired subnet. A `/16` plus 8 borrowed bits produces `/24` subnets (16 + 8 = 24). With `netnum = 1`: subnet 0 = `10.0.0.0/24`, subnet 1 = `10.0.1.0/24`. The answer is `8` (the additional bits to borrow), not `24` (the resulting prefix length). Passing `24` for `newbits` would attempt to borrow 24 bits from a `/16`, creating a `/40` prefix — invalid for IPv4. Passing `16` would produce a `/32`, and `4` would produce a `/20`.

---

### Question 13 — TWO Correct Statements About `for` Expression `if` Filter Clauses

**Difficulty**: Hard
**Answer Type**: many
**Topic**: A for expression can include an if clause to filter elements — the clause is optional, works in both list and map comprehensions, and can call built-in functions in its condition

**Question**:
Which TWO of the following statements about `for` expressions with `if` filter clauses are correct? (Select two.)

- A) An `if` clause in a `for` expression filters the output — only elements for which the condition is `true` are included: `[for n in var.names : n if length(n) > 4]` returns only names longer than 4 characters
- B) The `if` clause is mandatory in a `for` expression — omitting it causes a validation error because Terraform cannot determine which elements to include
- C) The `if` clause works in both list comprehensions `[for ...]` and map comprehensions `{for ...}` — `{for k, v in var.servers : k => v if v != ""}` is valid and produces a map containing only entries whose value is non-empty
- D) A `for` expression `if` clause can reference variables and locals, but cannot call built-in functions such as `length()`, `contains()`, or `startswith()` — function calls inside `if` clauses are a syntax error

**Answer**: A, C

**Explanation**:
**(A)** The `if` clause is an optional filter evaluated per element — elements where the condition is `true` are included, those where it is `false` are skipped. `[for n in var.names : n if length(n) > 4]` produces a list of only the names with more than 4 characters. **(C)** The `if` clause is valid in both list comprehensions (`[for ...]`) and map comprehensions (`{for ... : key => value}`). The example `{for k, v in var.servers : k => v if v != ""}` builds a filtered map. **(B)** is false — the `if` clause is entirely optional; `[for n in var.names : upper(n)]` is a valid `for` expression with no filter. **(D)** is false — `if` clause conditions can freely invoke any built-in Terraform function: `length()`, `contains()`, `startswith()`, `can()`, and others are all permitted inside filter conditions.

---

## Questions

---

### Question 1 — `check` Block Terraform Version

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

**Answer**: D

**Explanation**:
The `check` block is a relatively recent addition — it shipped in **Terraform 1.5**. Prior to 1.5, Terraform had `validation` blocks (for variables) and `precondition`/`postcondition` blocks (inside `lifecycle`), but no top-level non-blocking assertion mechanism. The `check` block runs on every `plan` and `apply`, optionally contains a scoped `data` source, and produces warnings (not errors) when its `assert` condition fails. Knowing the version is a direct exam fact.

---

### Question 2 — `sensitive = true` on an Output Block

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

**Answer**: D

**Explanation**:
The `sensitive` argument is valid on both `variable` and `output` blocks. Setting `sensitive = true` on an output instructs Terraform to show `(sensitive value)` in terminal output, plan summaries, and the default `terraform output` listing instead of the actual value. When a sensitive output is consumed by a parent module, the parent module also treats that value as sensitive. Critically, `sensitive = true` only controls **display** — the value is still stored in plaintext in `terraform.tfstate`. Options A, B, and C (`secret`, `masked`, `redact`) are not valid Terraform arguments.

---

### Question 3 — `self` Keyword Inside a `postcondition`

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

**Answer**: D

**Explanation**:
Inside a `postcondition` block, the special keyword `self` refers to the resource that declares the `lifecycle` block — specifically, the resource **as it exists after the change has been applied**. This means `self.public_ip` refers to the newly assigned public IP, `self.id` refers to the just-created resource ID, and so on. `self` is only valid inside `postcondition` — it is not available in `precondition` for referencing the new resource's attributes (since the resource hasn't been created or updated yet when `precondition` runs). Options A, B, and C are not valid references in this context.

---

### Question 4 — `error_message` Argument in a `validation` Block

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

**Answer**: D

**Explanation**:
A `validation` block requires exactly two arguments: `condition` (the boolean expression that must be `true` for the value to be valid) and `error_message` (the string Terraform displays when `condition` is `false`). The `error_message` must be a non-empty string and should clearly describe the constraint — for example, what range or set of values is acceptable. Options A (`message`), B (`error`), and C (`fail_message`) are not valid Terraform argument names for this purpose. Note also that the `condition` in this example (`var.instance_count >= 1 && var.instance_count <= 10`) is a valid numeric range check — validation blocks are not limited to string functions.

---

### Question 5 — `precondition` Block Inside `lifecycle`

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

**Answer**: D

**Explanation**:
`precondition` is the block type used inside a `lifecycle` block to assert conditions that must be true **before** Terraform makes changes to the resource. If the `condition` evaluates to `false`, Terraform halts the apply before touching the resource and displays the `error_message`. The condition can reference `data.*` sources, other resources, input variables, and locals — but not `self` (because the resource hasn't been changed yet). Option A (`assert`) is the block used inside a `check` block. Option B (`validation`) is only valid inside a `variable` block. Option C (`check`) is a top-level block, not a `lifecycle` sub-block.

---

### Question 6 — `check` Block Outer Structure

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

**Answer**: D

**Explanation**:
`check` is the top-level block keyword (introduced in Terraform 1.5) that contains infrastructure health assertions. A `check` block can optionally include a scoped `data` source — the `data` block declared inside a `check` block is **only** evaluated within that `check` block context and is not accessible outside it. The `assert` sub-block contains the `condition` and `error_message`. A failing `assert` inside a `check` block produces a **warning**, not an error — the apply continues and exits with a success code. Options A, B, and C are not valid top-level block types with this structure.

---

### Question 7 — `can()` Function in a `check` Block Assertion

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

**Answer**: D

**Explanation**:
`can(expression)` returns `true` if the expression evaluates without producing an error, and `false` if it throws an error. Wrapping `tostring(aws_db_instance.main.endpoint)` in `can()` tests whether the endpoint attribute is accessible and can be coerced to a string — if the attribute is `null` or the resource failed to provision, the expression would fail and `can()` returns `false`, triggering the assertion message. This pattern is useful inside `check` blocks for non-blocking health checks. Option A (`try()`) returns a fallback value on error — it doesn't return a boolean. Options B and C (`is_valid()`, `coalesce()`) are not the right functions for this purpose.

---

### Question 8 — `nonsensitive()` Function

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

**Answer**: D

**Explanation**:
`nonsensitive(value)` is a built-in Terraform function that removes the sensitive marking from a value, allowing it to be used in contexts that do not accept sensitive values — such as an output that should be displayed in terminal output without the `(sensitive value)` mask. Without `nonsensitive()`, assigning a sensitive variable to a non-sensitive output would cause Terraform to either propagate the sensitive marking or raise an error. This function should be used cautiously: only call it when you have confirmed that exposing the value is intentional and acceptable. Options A, B, and C (`reveal`, `plaintext`, `expose`) are not Terraform built-in functions.

---

### Question 9 — `check` Block: Version and Execution Timing

**Difficulty**: Medium
**Answer Type**: many
**Topic**: When the check block runs and which Terraform version introduced it

**Question**:
Which **TWO** of the following statements about the `check` block are correct?

- A) The `check` block was introduced in Terraform `1.5`
- B) A failing `check` block `assert` halts `terraform apply` with a non-zero exit code, preventing the deployment from completing
- C) The `check` block runs on every `terraform plan` AND every `terraform apply` — not just on apply
- D) The `check` block can only be declared inside a resource's `lifecycle` block — it is not a top-level block type

**Answer**: A, C

**Explanation**:
Two key exam facts about `check` blocks: (1) it was **introduced in Terraform 1.5** — earlier versions do not support the `check` block syntax; (2) it runs on **both `terraform plan` and `terraform apply`** — not just apply. This makes it useful for surfacing infrastructure health issues during planning, before any changes are applied. Option B is wrong — a failing `check` assertion is a **warning only** and never prevents the apply from completing; the exit code remains 0 (success). Option D is wrong — `check` is a **top-level block** in Terraform configuration, not a sub-block inside `lifecycle`.

---

### Question 10 — `postcondition`: `self` and Failure Behaviour

**Difficulty**: Medium
**Answer Type**: many
**Topic**: What postcondition self references and how a failing postcondition affects apply

**Question**:
Which **TWO** of the following statements about `postcondition` blocks are correct?

- A) A `postcondition` runs **before** the resource is created or modified — if the condition fails, the resource change is prevented
- B) Inside a `postcondition`, the `self` keyword references the resource as it exists **after the change has completed** — including attributes only known after creation, such as `public_ip` or `id`
- C) A failing `postcondition` condition halts the apply **after** the resource has been changed, exits with a non-zero status code, and marks the run as failed
- D) `postcondition` blocks can only reference `var.<name>` values — they cannot use `self` or reference other resource attributes

**Answer**: B, C

**Explanation**:
`postcondition` runs **after** the resource change (option A is wrong — that describes `precondition`). Inside a `postcondition`, `self` refers to the resource in its **post-change state** — all attributes that are computed during creation (such as `public_ip`, `id`, `arn`) are accessible through `self` (option B is correct). If the `condition` evaluates to `false`, Terraform halts the apply, exits with a non-zero status code, and surfaces the `error_message` — the resource has already been created or updated at this point (option C is correct). Option D is incorrect — `postcondition` can freely reference `self`, data sources, locals, and other resources; it is `validation` (not `postcondition`) that is restricted to only `var.<name>`.

---

### Question 11 — Vault Provider Data Source Type

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

**Answer**: C

**Explanation**:
`vault_generic_secret` is the Vault provider data source used to read a key-value secret from any Vault secrets engine path. The `path` argument specifies the Vault path, and the `.data` attribute on the resulting object is a map of the key-value pairs stored at that path. This pattern — fetching credentials from Vault at plan/apply time — is a key security improvement over storing secrets in `.tf` files or `.tfvars` files, because the credentials never appear as literals in source-controlled configuration. Options A, B, and D are plausible names but not the correct Vault provider resource type for a generic KV secret.

---

### Question 12 — `precondition` Is the Wrong Tool for Post-Creation Checks

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

**Answer**: B

**Explanation**:
`precondition` runs **before** the resource is created or modified. For a new resource, there is no existing state — `self.public_ip` will always be `null` before provisioning. This means the precondition would always fail for a new resource, which is the opposite of the intended behaviour. The engineer should use a `postcondition` instead: it runs **after** the resource change, `self` references the resource in its newly created state, and a failing condition halts the apply with the error message. The distinction is fundamental: `precondition` = gate before change (check prerequisites); `postcondition` = gate after change (verify the created resource meets expectations). Option C is wrong — `self` is valid in `postcondition`; option D is incorrect attribute naming.

---

### Question 13 — Vault Dynamic Secrets: Two Correct Statements

**Difficulty**: Hard
**Answer Type**: many
**Topic**: What the Vault provider pattern achieves and what it does not protect

**Question**:
Which **TWO** of the following statements about using the HashiCorp Vault provider to supply dynamic secrets to Terraform are correct?

- A) When the `vault_generic_secret` data source is used, Terraform reads credentials from Vault at plan/apply time — the credentials are not stored as literals in any Terraform `.tf` configuration file or `.tfvars` file
- B) Values retrieved from Vault data sources are automatically excluded from `terraform.tfstate` — the Vault integration is specifically designed to prevent secrets from appearing in state
- C) The Vault provider pattern prevents static, long-lived credentials from being embedded in Terraform configuration files — this reduces the risk of secrets being committed to source control
- D) Using the Vault provider means Terraform never stores the retrieved secret values anywhere — neither in state nor in memory during execution

**Answer**: A, C

**Explanation**:
The primary security benefit of the Vault provider pattern is that credentials are **fetched at runtime** (plan/apply), so they never appear as plaintext strings in `.tf` files or `.tfvars` files — reducing the risk of accidental source-control commits of secrets (options A and C are correct). However, option B is **wrong**: values retrieved from `data` sources, including Vault secrets, **are stored in `terraform.tfstate`** in plaintext — Vault does not make state storage exempt from this. Option D is also **wrong**: Terraform stores all resource and data source attribute values in state, and values are held in memory during execution. The mitigation for state exposure is still required: encrypted remote backends, restricted IAM/RBAC on the state file, and never committing `.tfstate` to source control.

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

---

## Questions

---

### Question 1 — `terraform force-unlock` Command Syntax

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

**Answer**: C

**Explanation**:
`terraform force-unlock LOCK_ID` is the command used to manually release a state lock when a Terraform process died while holding it. The lock ID is displayed in the error message when another operation encounters the existing lock — for example: `Error acquiring the state lock: Lock Info: ID: abc-12345`. You pass that ID directly to `force-unlock`. Use this command with caution: only run it when you are certain no other operation is actually in progress, because releasing a lock held by a live process could lead to concurrent state writes and corruption. Options A (`state unlock`), B (`unlock-state`), and D (`state release`) are not valid Terraform commands.

---

### Question 2 — `terraform login` Credential Storage Location

**Difficulty**: Easy
**Answer Type**: one
**Topic**: Where `terraform login` writes the API token for HCP Terraform authentication

**Question**:
Complete the sentence: After running `terraform login` and authenticating via the browser, the API token is stored in ___________.

- A) `~/.terraform/credentials.json`
- B) `~/.terraform.d/credentials.tfrc.json`
- C) `./terraform.tfvars` in the working directory
- D) `~/.config/terraform/token`

**Answer**: B

**Explanation**:
`terraform login` opens a browser window, prompts you to log in to HCP Terraform (or Terraform Enterprise), generates an API token, and writes it to `~/.terraform.d/credentials.tfrc.json`. This is the default credential store for Terraform CLI. The file uses a JSON format that maps hostnames to their tokens, so tokens for multiple registries can coexist. If you prefer not to use `terraform login`, you can alternatively set the `TF_TOKEN_app_terraform_io` environment variable to provide the token directly — useful in CI/CD pipelines where storing files is impractical. Option A uses a path that does not exist. Option C (`terraform.tfvars`) is for variable values, not credentials. Option D is not a path Terraform uses.

---

### Question 3 — TF_LOG Verbosity Ordering

**Difficulty**: Easy
**Answer Type**: many
**Topic**: Correct relative verbosity of `TF_LOG` levels and which level is the most verbose

**Question**:
Which **TWO** of the following statements about `TF_LOG` log levels are correct?

- A) `TRACE` is the most verbose level — it captures all API calls, full request/response bodies, and internal Terraform core operations; `DEBUG` is the next level down
- B) `WARN` produces more output than `INFO` — warnings include all informational messages plus additional warning-level detail
- C) The full verbosity order from most to least verbose is: `TRACE > DEBUG > INFO > WARN > ERROR`; setting a level includes all messages at that level and less verbose levels — `INFO` would show `INFO`, `WARN`, and `ERROR` messages
- D) `ERROR` and `OFF` are the same — setting `TF_LOG=ERROR` disables logging just as `TF_LOG=OFF` does

**Answer**: A, C

**Explanation**:
`TF_LOG` supports six values in decreasing verbosity order: `TRACE`, `DEBUG`, `INFO`, `WARN`, `ERROR`, and `OFF`. Setting a level captures all messages at that level **and all less-verbose levels** — so `INFO` includes `INFO`, `WARN`, and `ERROR` messages. `TRACE` is the most verbose and is used by HashiCorp support for deep debugging because it includes all HTTP API calls and responses (option A). The full ordering `TRACE > DEBUG > INFO > WARN > ERROR` is correct (option C). Option B is wrong — `WARN` is **less** verbose than `INFO` (fewer messages), not more. Option D is wrong — `ERROR` still emits error-level log messages; `OFF` is the level that completely disables logging output.

---

### Question 4 — `terraform state mv` to Rename a Resource

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

**Answer**: A

**Explanation**:
`terraform state mv <SOURCE_ADDRESS> <DESTINATION_ADDRESS>` takes exactly two positional arguments — the current resource address and the new resource address. Both are positional, not named flags. This command updates the state file to reflect the new name without modifying any cloud infrastructure. The typical workflow is: (1) rename the `resource` block label in your `.tf` file, (2) run `terraform state mv aws_instance.web aws_instance.web_server` to align state with the configuration change. Without the `state mv`, the next `terraform plan` would show a destroy of `aws_instance.web` and a create of `aws_instance.web_server`. Options B and D use non-existent flags. Option C passes separate type and label strings instead of the combined `TYPE.LABEL` address format.

---

### Question 5 — `terraform init` Flag to Migrate State to a New Backend

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

**Answer**: C

**Explanation**:
`terraform init -migrate-state` is the flag that tells Terraform to detect the change in backend configuration and offer to copy the existing state to the new backend. If you confirm the prompt, Terraform reads the current state from the old backend (local file in this case) and writes it to the new backend (S3 bucket). This preserves state continuity — no resources need to be re-imported. The contrasting flag, `-reconfigure`, also re-initialises the backend but **discards the migration prompt** — it reconfigures the backend without attempting to copy existing state, which means existing local state would be abandoned and the new backend would start empty. Use `-reconfigure` when you intentionally want a fresh state (e.g., switching to a completely unrelated environment).

---

### Question 6 — `cloud` Block Workspace Selection by Tags

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

**Answer**: C

**Explanation**:
Inside the `cloud` block's `workspaces` sub-block, you can select workspaces in two mutually exclusive ways: by `name` (a single workspace name string) or by `tags` (a list of tag strings — only workspaces that have **all** of the specified tags are selected). Tag-based selection enables workspace-per-environment patterns where a single configuration targets multiple workspaces matching the tag filter. This is a key advantage of the `cloud` block over the legacy `backend "remote"` block, which only supports workspace selection by name. Option A (`filter`) and D (`labels`) are not valid arguments in the `workspaces` sub-block. Option B (`name`) would work for selecting a single workspace by name, but cannot accept a list of tag values.

---

### Question 7 — `TF_TOKEN_` Environment Variable for HCP Terraform

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

**Answer**: C

**Explanation**:
Terraform supports a `TF_TOKEN_<HOSTNAME>` environment variable pattern where the hostname component uses underscores in place of periods and hyphens. For the default HCP Terraform host `app.terraform.io`, the variable name is `TF_TOKEN_app_terraform_io`. Setting this variable provides the API token without requiring `terraform login` or a credentials file — making it the standard approach in CI/CD pipelines. Terraform reads this variable during `terraform init` and subsequent operations to authenticate to HCP Terraform. If both `TF_TOKEN_app_terraform_io` and a stored credentials file exist, the environment variable takes precedence. Options A (`TF_API_TOKEN`), B (`TF_CLOUD_TOKEN`), and D (`TERRAFORM_CLOUD_CREDENTIAL`) are not recognised by Terraform.

---

### Question 8 — `terraform_remote_state` Backend Type for HCP Terraform

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

**Answer**: C

**Explanation**:
When reading remote state from an HCP Terraform workspace using a `terraform_remote_state` data source, the `backend` argument must be set to `"remote"`. Despite the `cloud` block being the preferred way to connect a working configuration to HCP Terraform, the `terraform_remote_state` data source still uses `backend = "remote"` with an `organization` and `workspaces.name` in its `config` block. The `config` arguments mirror the legacy `backend "remote"` configuration syntax. Setting `backend = "remote"` does not use the local filesystem; Terraform contacts the HCP Terraform API to fetch the state outputs from the specified workspace. Options A (`"hcp"`), B (`"cloud"`), and D (`"terraform_cloud"`) are not valid `terraform_remote_state` backend values.

---

### Question 9 — Sentinel Policy Enforcement Level That Cannot Be Overridden

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Which HCP Terraform policy enforcement level blocks a run and cannot be overridden by any user

**Question**:
Complete the sentence: A Sentinel or OPA policy set with enforcement level ___________ will block a run when the policy fails, and **no user in the organisation — including owners — can override the failure**.

- A) `soft-mandatory`
- B) `advisory`
- C) `blocking`
- D) `hard-mandatory`

**Answer**: D

**Explanation**:
HCP Terraform policy enforcement has three levels: `advisory` (policy failure is a warning only — the run continues), `soft-mandatory` (failure blocks the run but an authorised user can override and proceed), and `hard-mandatory` (failure blocks the run permanently — it **cannot be overridden** by anyone, including organisation owners). Hard-mandatory policies represent compliance requirements that must be satisfied before any apply can proceed. `soft-mandatory` is useful for policies that normally must pass but may need an escape hatch for emergencies. `advisory` is suitable for informational checks or phased rollouts of new policies. Option B (`advisory`) allows the run to continue. Option A (`soft-mandatory`) allows overriding. Option C (`blocking`) is not a valid enforcement level name.

---

### Question 10 — Private Registry Module Source Format

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

**Answer**: C

**Explanation**:
Modules published in an HCP Terraform private registry use the format `app.terraform.io/<ORGANIZATION>/<MODULE>/<PROVIDER>`. The hostname `app.terraform.io` identifies the HCP Terraform registry (as opposed to `registry.terraform.io` for the public registry). The organisation name, module name, and provider name follow the same three-part structure used by the public registry. During `terraform init`, Terraform authenticates to `app.terraform.io` using the stored credential (from `terraform login` or `TF_TOKEN_app_terraform_io`) and downloads the private module. Option B (`"my-org/vpc/aws"`) is the format for the public Terraform Registry and would resolve to `registry.terraform.io`. Options A and D use fictional hostnames.

---

### Question 11 — Sentinel vs OPA: Two Correct Statements

**Difficulty**: Medium
**Answer Type**: many
**Topic**: Differences between Sentinel (HashiCorp DSL) and OPA (Rego) as HCP Terraform policy frameworks

**Question**:
Which **TWO** of the following statements about HCP Terraform policy enforcement are correct?

- A) Sentinel uses HashiCorp's own domain-specific language (DSL); OPA (Open Policy Agent) policies are written in Rego — both frameworks are supported natively in HCP Terraform as policy enforcement options
- B) Sentinel and OPA are mutually exclusive — an HCP Terraform organisation must choose one framework and cannot use both simultaneously
- C) Both Sentinel and OPA policy sets can be assigned enforcement levels: `advisory`, `soft-mandatory`, or `hard-mandatory`
- D) OPA policies can only be used for cost estimation checks; Sentinel is the only framework that can evaluate Terraform plan data for resource-level policy enforcement

**Answer**: A, C

**Explanation**:
HCP Terraform natively supports two policy frameworks: Sentinel (using HashiCorp's own DSL) and OPA — Open Policy Agent (using the Rego language). Both are first-class options for writing and enforcing infrastructure policies (option A is correct). Both frameworks also share the same three enforcement levels — `advisory`, `soft-mandatory`, and `hard-mandatory` — applied at the policy set level (option C is correct). Option B is wrong — organisations can use both Sentinel and OPA simultaneously; different policy sets can use different frameworks, and all apply during runs. Option D is wrong — OPA in HCP Terraform evaluates Terraform plan data just as Sentinel does; it is not restricted to cost estimation, and both frameworks can perform resource-level checks.

---

### Question 12 — `TF_LOG_CORE` and `TF_LOG_PROVIDER` Env Vars

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

**Answer**: B

**Explanation**:
Terraform provides two granular log environment variables that override `TF_LOG` for specific subsystems: `TF_LOG_CORE` controls log verbosity for the Terraform core binary (the orchestrator that reads configuration, manages state, and calls providers), while `TF_LOG_PROVIDER` controls log verbosity for provider plugins (the binaries that communicate with cloud APIs). When both are set, `TF_LOG` is ignored in favour of the more specific variables. This separation is valuable when debugging provider API issues (set `TF_LOG_PROVIDER=TRACE` for full API call detail) while keeping core output at a lower verbosity level to reduce noise. Options A, C, and D are not valid Terraform environment variable names.

---

### Question 13 — HCP Terraform Health Assessments: Underlying Command

**Difficulty**: Hard
**Answer Type**: one
**Topic**: What operation HCP Terraform Health Assessments perform on a configurable schedule to detect infrastructure drift

**Question**:
Complete the sentence: HCP Terraform Health Assessments work by automatically running ___________ on a configurable schedule — if the result shows drift between actual cloud resources and Terraform state, the assessment is marked as unhealthy and notifications can be triggered.

- A) `terraform apply -refresh-only` — reconciling state with actual resources on every scheduled run
- B) `terraform validate` — checking configuration syntax and provider schema compliance
- C) `terraform plan -refresh-only` — detecting drift without modifying state or infrastructure
- D) `terraform state pull` — downloading and comparing the remote state to the cloud resource API responses

**Answer**: C

**Explanation**:
HCP Terraform Health Assessments perform a `terraform plan -refresh-only` on a configurable schedule (e.g., daily or weekly). This operation queries the cloud provider APIs for the current state of all managed resources and compares them to what is recorded in Terraform state — without writing any changes to state or infrastructure. If attributes differ (e.g., a tag was manually changed, a security group rule was added outside Terraform), the assessment flags the workspace as drifted and can send notifications via email, Slack, or PagerDuty. Option A (`terraform apply -refresh-only`) is wrong — a health assessment never automatically modifies state; it is read-only. Option B (`terraform validate`) checks configuration syntax — it cannot detect live infrastructure drift. Option D (`terraform state pull`) only downloads state; it does not query the cloud provider for live resource attributes.