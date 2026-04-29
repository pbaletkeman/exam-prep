# Terraform Associate Exam Questions

---

### Question 1 — HCL Block vs CLI Command

**Difficulty**: Easy
**Answer Type**: one
**Topic**: Contrast between a declarative HCL resource block and an imperative CLI command for the same infrastructure

**Question**:
Compare these two approaches to creating an EC2 instance:

**Approach A:**
```hcl
resource "aws_instance" "web" {
  ami           = "ami-0abcd1234"
  instance_type = "t3.micro"
}
```

**Approach B:**
```bash
aws ec2 run-instances --image-id ami-0abcd1234 --instance-type t3.micro
```

What is the fundamental difference in *how* each approach describes the task?

- A) Approach A creates the instance immediately; Approach B creates it only after a `plan` step
- B) Approach A declares the desired end state and lets the tool determine whether to act; Approach B issues a direct instruction to create the resource right now
- C) Approach A is multi-cloud; Approach B is AWS-specific
- D) Approach A requires Terraform to be installed; Approach B runs natively in any shell

---

### Question 2 — State File vs Configuration File

**Difficulty**: Easy
**Answer Type**: one
**Topic**: Contrast between what the state file records and what the configuration file expresses

**Question**:
What is the primary difference between a Terraform configuration file (`.tf`) and the Terraform state file (`terraform.tfstate`)?

- A) Configuration files are written in JSON; state files use HCL syntax
- B) Configuration files describe the **desired state** — what infrastructure should exist; the state file records the **current tracked state** — what Terraform believes currently exists based on the last successful apply
- C) The state file is the authoritative source for what Terraform will create next; the configuration file is advisory only
- D) Both files serve the same purpose — the state file is simply a binary-encoded version of the configuration file

---

### Question 3 — Terraform vs AWS CloudFormation Scope

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Contrast between Terraform's multi-cloud capability and CloudFormation's AWS-only scope

**Question**:
A platform team needs to manage AWS RDS instances, Azure Key Vault secrets, and GCP Cloud Storage buckets from a single IaC workflow. How does Terraform differ from AWS CloudFormation in its ability to meet this requirement?

- A) Both tools support multi-cloud management using provider plugins — CloudFormation recently added Azure and GCP providers
- B) Terraform supports managing resources across AWS, Azure, GCP, and many other providers from a single root module; CloudFormation is AWS-native and cannot manage Azure or GCP resources
- C) CloudFormation supports multi-cloud through AWS Organizations; Terraform requires separate state files per cloud provider
- D) Terraform requires a dedicated workspace per cloud provider; CloudFormation handles cross-cloud with a single template

---

### Question 4 — IaC Audit Trail vs ClickOps Audit Trail

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Contrast between the audit trail produced by IaC commits vs manual console changes

**Question**:
An engineer makes the same infrastructure change — resizing an RDS instance from `db.t3.small` to `db.t3.medium` — in two different environments. In Environment A, the change is made by updating the Terraform configuration and committing to Git before applying. In Environment B, the change is made directly through the AWS console. Six months later, a compliance audit asks who made the change and why. How do the two environments differ in their ability to answer this question?

- A) Both environments provide equivalent information — AWS CloudTrail records all API calls regardless of origin, so the auditor can find the change in both cases
- B) Environment A provides a Git commit record showing the author, timestamp, commit message, and the exact configuration change; Environment B has no entry in version control — the change is traceable only through cloud provider logs with no context about intent or approval
- C) Environment B is more auditable because AWS console changes are logged with the IAM user's identity, while Terraform applies are anonymous
- D) Neither environment has a meaningful audit trail — cloud provider logs do not retain data for six months

---

### Question 5 — First Apply vs Subsequent Apply Behaviour

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Contrast between what happens on the first apply vs a second apply with an unchanged configuration

**Question**:
A Terraform configuration declares five S3 buckets. Compare what happens on the **first** `terraform apply` to what happens on a **second** `terraform apply` run immediately after, with no configuration changes and no manual changes to the cloud environment.

- A) Both runs produce identical output: `Plan: 5 to add, 0 to change, 0 to destroy`
- B) The first apply creates all five buckets; the second apply destroys and recreates them to verify they are correct
- C) The first apply creates all five buckets (`Plan: 5 to add`); the second apply detects no difference between desired and current state and reports `No changes` — no actions are taken
- D) The first apply creates five buckets; the second apply creates five more, totalling ten

---

### Question 6 — Provisioning Tools vs Configuration Management Tools

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Contrast between infrastructure provisioning (Terraform) and configuration management (Ansible)

**Question**:
A DevOps team uses both Terraform and Ansible. A new team member asks what each tool is responsible for. Which statement best distinguishes their roles?

- A) Terraform and Ansible are interchangeable — either tool can provision cloud infrastructure and configure software on servers
- B) Terraform is used to **provision infrastructure** — creating VMs, networks, and storage in the cloud; Ansible is used for **configuration management** — installing software, managing services, and configuring applications on existing servers
- C) Terraform configures software on servers; Ansible provisions cloud infrastructure resources
- D) Terraform handles AWS resources; Ansible handles Azure and GCP resources

---

### Question 7 — Single-Cloud vs Multi-Cloud IaC Tools

**Difficulty**: Medium
**Answer Type**: many
**Topic**: Contrasting which IaC tools are limited to a single cloud provider vs those that support multiple providers

**Question**:
Consider four IaC tools: **Terraform**, **AWS CloudFormation**, **Azure Bicep**, and **Pulumi**. Which TWO of these tools are limited to managing resources from a single cloud provider and cannot natively manage resources across multiple clouds? (Select two.)

- A) Terraform — limited to AWS resources only
- B) AWS CloudFormation — limited to AWS resources only
- C) Azure Bicep — limited to Azure resources only
- D) Pulumi — limited to AWS resources only

---

### Question 8 — Drift Detection with IaC vs without IaC

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Contrast between how a team detects drift when using IaC versus when managing infrastructure manually

**Question**:
Two teams manage similar AWS environments. Team A manages all infrastructure with Terraform. Team B manages all infrastructure manually through the AWS console. An EC2 instance is resized outside of the normal process in both environments. How does each team's ability to detect the drift differ?

- A) Both teams detect drift identically — AWS Config monitors all resources and alerts both teams automatically regardless of how the infrastructure was provisioned
- B) Team A can run `terraform plan` to compare the declared desired state against the actual cloud state and detect the resized instance; Team B has no single source of truth to compare against, making drift invisible unless noticed manually
- C) Team B is better positioned to detect drift because they interact with the console daily and are more likely to notice changes
- D) Neither team can detect drift without a third-party monitoring tool — Terraform itself does not detect resource attribute changes

---

### Question 9 — Disaster Recovery: IaC vs No IaC

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Contrast between recreating a lost environment with IaC versus without it

**Question**:
Two companies lose their entire cloud environments in a catastrophic incident. Company A has all infrastructure defined in Terraform configuration files stored in Git. Company B provisioned everything manually through the cloud console with no IaC. How does the recovery path differ?

- A) Company A and Company B take the same amount of time — rebuilding from Terraform configs is not faster than rebuilding manually if the engineer knows the setup well
- B) Company A can run `terraform apply` against their configuration files to recreate the environment reproducibly and consistently; Company B must manually recreate each resource by memory or from documentation, with no guarantee of consistency or completeness
- C) Company A must first run `terraform import` to re-register all resources before applying — the advantage over Company B is minimal
- D) Both companies should use cloud provider snapshots for disaster recovery; IaC configurations are not a substitute for backup solutions

---

### Question 10 — Manual Change vs Config Change: Two Differences

**Difficulty**: Medium
**Answer Type**: many
**Topic**: Contrasting how a manual cloud change and a Terraform configuration change are tracked and applied differently

**Question**:
An infrastructure change is made in two different ways. **Method X**: An engineer updates the Terraform configuration in a `.tf` file and runs `terraform apply`. **Method Y**: An engineer directly modifies the resource using the cloud provider's web console. Which TWO statements correctly describe a difference between these two methods? (Select two.)

- A) Only Method X produces a version-controlled record of the change that can be reviewed, reverted, and audited via Git history
- B) Only Method X changes can be peer-reviewed in a pull request before being applied — Method Y bypasses the review process entirely
- C) Method Y is safer because console changes go through stricter validation than Terraform plan
- D) Method X and Method Y are equivalent — Terraform detects and absorbs console changes automatically on the next plan

---

### Question 11 — Declarative Model vs Imperative Scripting: What the Operator Specifies

**Difficulty**: Hard
**Answer Type**: one
**Topic**: Deep contrast between what an operator must define in a declarative model vs an imperative scripting approach

**Question**:
A DevOps engineer has two options for ensuring that exactly three web servers running `t3.micro` exist in AWS:

**Option 1 (Declarative):** Write a Terraform configuration declaring three `aws_instance` resources and run `terraform apply`.

**Option 2 (Imperative):** Write a bash script that checks how many instances exist, calculates the delta, and runs `aws ec2 run-instances` or `aws ec2 terminate-instances` as needed.

What is the key contrast in what the operator is responsible for defining in each option?

- A) In Option 1, the operator defines the steps; in Option 2, Terraform infers the steps from a high-level goal
- B) Option 1 requires more code — HCL is more verbose than bash for simple operations
- C) In Option 1, the operator defines *what* the end state should be; in Option 2, the operator must define *how* to reach the end state — including the logic to detect and correct any discrepancy
- D) Both options require the operator to define the same logic — the difference is only in the syntax used

---

### Question 12 — Provisioning vs Configuration Management: Full Stack Roles

**Difficulty**: Hard
**Answer Type**: many
**Topic**: Contrasting the provisioning and configuration management layers in a complete infrastructure automation stack

**Question**:
A team is building a complete automation stack. They decide to use Terraform for one layer and Ansible for another. Which TWO statements correctly describe how the responsibilities of each tool differ? (Select two.)

- A) Terraform provisions and lifecycle-manages cloud infrastructure resources (VMs, networks, databases, storage) — it creates, modifies, and destroys these resources based on HCL configuration
- B) Ansible's primary function in this stack is to provision new cloud VMs — it submits API calls to the cloud provider to launch instances and create VPCs
- C) Ansible is used to configure the operating system and software on servers after they are provisioned — installing packages, writing config files, starting services, and managing application deployments
- D) Terraform installs application software on VMs after provisioning them — it includes a built-in configuration management agent that runs after `terraform apply` completes

---

### Question 13 — Official Provider Tier vs Community Provider Tier

**Difficulty**: Easy
**Answer Type**: one
**Topic**: Contrast between who maintains Official providers and who maintains Community providers

**Question**:
Compare the **Official** provider tier and the **Community** provider tier in the Terraform ecosystem. What is the key difference in maintenance and trust level between them?

- A) Official providers are free; Community providers require a paid HashiCorp subscription to use
- B) Official providers are maintained by HashiCorp and carry the highest trust level; Community providers are maintained by individuals or organisations with no HashiCorp review or verification
- C) Official providers are distributed only through the private registry; Community providers are available on the public Terraform Registry
- D) Official providers support all Terraform features; Community providers are limited to data sources only

---

### Question 14 — `~> 5.0` vs `~> 5.0.0` Version Constraints

**Difficulty**: Easy
**Answer Type**: one
**Topic**: Contrast between the two most commonly confused pessimistic constraint operator patterns

**Question**:
Compare these two version constraints for the same provider:

- **Constraint A**: `version = "~> 5.0"`
- **Constraint B**: `version = "~> 5.0.0"`

What is the specific difference in the version ranges they permit?

- A) Both constraints are identical — they both allow any version in the `5.x.x` range
- B) Constraint A allows >= `5.0` and < `6.0` (minor and patch updates within major 5); Constraint B allows >= `5.0.0` and < `5.1.0` (patch updates only within minor 5.0)
- C) Constraint A allows only version `5.0` exactly; Constraint B allows any `5.0.x` patch version
- D) Constraint A is more restrictive than Constraint B — it excludes versions like `5.9.3` that Constraint B would permit

---

### Question 15 — `.terraform/` Directory vs `.terraform.lock.hcl` in Version Control

**Difficulty**: Easy
**Answer Type**: one
**Topic**: Contrast between the gitignore treatment of the provider cache directory and the lock file

**Question**:
Compare how the `.terraform/` directory and the `.terraform.lock.hcl` file should be treated with respect to a project's version control system. What is the key difference?

- A) Both should be committed to version control — they together ensure reproducible provider installations across the team
- B) Both should be added to `.gitignore` — they are auto-generated by `terraform init` and are too large to commit
- C) `.terraform/` should be committed; `.terraform.lock.hcl` should be gitignored because it changes frequently
- D) `.terraform/` should be gitignored (it is a local provider cache, large and machine-specific); `.terraform.lock.hcl` must be committed (it records exact provider versions and checksums for team-wide consistency)

---

### Question 16 — Provider `source` vs Provider `version` in `required_providers`

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Contrast between what the source address and the version constraint each control

**Question**:
A `required_providers` block contains both a `source` and a `version` attribute for a provider. What is the specific role of each attribute, and how do they differ?

```hcl
terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}
```

- A) `source` specifies the maximum version allowed; `version` specifies the minimum version
- B) `source` identifies where to download the provider (`<namespace>/<type>` resolving to a registry address); `version` constrains which versions of that provider are acceptable
- C) `source` configures authentication credentials; `version` configures which API endpoints are supported
- D) Both attributes are required and serve identical purposes — they together form the full provider identifier

---

### Question 17 — `terraform init` vs `terraform init -upgrade`

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Contrast between standard init and upgrade init in terms of when each should be used

**Question**:
Compare `terraform init` and `terraform init -upgrade`. A lock file exists, recording AWS provider `5.10.0` with constraint `~> 5.0`. AWS `5.31.0` is now available. What is the behavioural difference between the two commands?

- A) `terraform init` downloads `5.31.0`; `terraform init -upgrade` installs `5.10.0` as a downgrade safety measure
- B) Both commands install `5.31.0` because it satisfies the constraint — the `-upgrade` flag has no effect when a newer version is available
- C) `terraform init` uses the lock file and installs `5.10.0` (reproducible); `terraform init -upgrade` re-evaluates constraints and installs the newest satisfying version (`5.31.0`), updating the lock file
- D) `terraform init` fails if the lock file is outdated; `-upgrade` is required to resolve the conflict

---

### Question 18 — Default Provider Configuration vs Aliased Provider Configuration

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Contrast between how Terraform assigns resources to the default provider vs an aliased provider

**Question**:
Two AWS provider configurations are declared in the same root module:

```hcl
provider "aws" {
  region = "us-east-1"
}

provider "aws" {
  alias  = "west"
  region = "us-west-2"
}
```

An engineer adds a new `aws_instance` resource block without specifying a `provider` argument. Compare how Terraform assigns this resource to a provider, and contrast this with how a resource that explicitly sets `provider = aws.west` is assigned.

- A) Resources without a `provider` argument are assigned to whichever provider was declared first in the file; the `provider = aws.west` reference overrides this order
- B) Resources without a `provider` argument are assigned to the **default (unaliased)** provider (`us-east-1`); resources that specify `provider = aws.west` are explicitly assigned to the aliased provider (`us-west-2`)
- C) Both resources use the same provider — the alias only affects resource naming, not which region is used
- D) Resources without a `provider` argument are rejected — Terraform requires explicit provider assignment whenever aliases are present

---

### Question 19 — `terraform state mv` vs `terraform state rm`

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Contrast between what state mv and state rm do to the tracked state and the actual cloud resource

**Question**:
Compare `terraform state mv aws_instance.old aws_instance.new` and `terraform state rm aws_instance.web`. What is the key difference in what each command does to the Terraform state and to the actual cloud resource?

- A) `state mv` deletes the cloud resource; `state rm` renames it
- B) Both commands delete the cloud resource but differ in whether they also update the configuration file
- C) `state mv` renames the resource's address in state (the cloud resource is unchanged and remains managed); `state rm` removes the resource from state entirely (the cloud resource is unchanged but Terraform no longer tracks or manages it)
- D) `state mv` and `state rm` are equivalent — both stop Terraform from managing the resource while leaving it in the cloud

---

### Question 20 — Local State vs Remote State: Safety and Access

**Difficulty**: Medium
**Answer Type**: many
**Topic**: Contrasting local and remote state on concurrent apply safety and team accessibility

**Question**:
Compare local state (`terraform.tfstate` on a local disk) and remote state (e.g., stored in S3 or HCP Terraform). Which TWO statements correctly describe a difference between them with respect to **concurrent apply safety** and **team access**? (Select two.)

- A) Local state provides locking — if two engineers run `terraform apply` simultaneously, Terraform automatically queues the second apply until the first completes
- B) Remote state backends support locking — a lock is acquired at the start of a plan or apply and released on completion, preventing concurrent applies from corrupting state
- C) Local state is stored on the individual engineer's machine — other team members cannot access the current state without manually receiving a copy of the file
- D) Remote state and local state are equivalent in terms of team access — both are equally accessible to any engineer with repository access

---

### Question 21 — `terraform state show` vs `terraform show`

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Contrast between the targeted state show command and the full-state show command

**Question**:
Compare `terraform state show aws_instance.web` and `terraform show`. What does each command display, and how do they differ in scope?

- A) `terraform state show aws_instance.web` shows the planned changes for that resource; `terraform show` shows the entire configuration
- B) `terraform state show aws_instance.web` displays all tracked attributes of that single resource from state; `terraform show` displays the entire state (all resources) or the contents of a saved plan file
- C) Both commands are identical — `terraform state show <address>` is just a filtered alias for `terraform show`
- D) `terraform state show` requires a remote backend; `terraform show` works with both local and remote state

---

### Question 22 — `sensitive = true` on Output vs Encrypting the Remote Backend

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Contrast between terminal display masking and actual state-at-rest encryption

**Question**:
An engineer has a database password stored in Terraform. They declare `sensitive = true` on the output that exposes it. A colleague suggests this is sufficient protection for the password. Compare what `sensitive = true` actually protects vs what an encrypted remote backend protects. Are they correct?

- A) Yes — `sensitive = true` both hides the password in terminal output and encrypts it in the state file, providing complete protection
- B) No — `sensitive = true` only masks the value in terminal output (displaying `(sensitive value)` instead); the password is still stored in **plaintext** in the state file. An encrypted remote backend (e.g., S3 with SSE) protects the state file **at rest** — they address different attack surfaces and both are needed
- C) Yes — Terraform automatically encrypts all `sensitive = true` values in state, so no additional backend encryption is needed
- D) No — `sensitive = true` provides no protection at all; only encrypted remote backends should be used for secrets in Terraform

---

### Question 23 — Committed Lock File vs No Lock File: Two Team Impact Differences

**Difficulty**: Medium
**Answer Type**: many
**Topic**: Contrasting two specific risks of not committing the lock file vs always committing it

**Question**:
Team A always commits `.terraform.lock.hcl` to their Git repository. Team B adds `.terraform.lock.hcl` to `.gitignore`, treating it as a local-only file. Which TWO statements correctly describe a risk specific to Team B's approach that Team A does not face? (Select two.)

- A) Team B's engineers may install different provider versions on different days as new versions are released, causing subtle, hard-to-reproduce behaviour differences between team members
- B) Team B's CI pipeline cannot run `terraform plan` because the lock file is required to be present during automated runs
- C) Team B cannot verify provider integrity — without the lock file's cryptographic hashes, Terraform cannot confirm that downloaded providers match what was originally installed
- D) Team B can use `terraform init -upgrade` to address this; Team A cannot because their lock file prevents upgrades

---

### Question 24 — gRPC Plugin Architecture vs Hypothetical Monolithic Architecture

**Difficulty**: Hard
**Answer Type**: one
**Topic**: Contrast between Terraform's separate-process provider model and a hypothetical built-in provider model

**Question**:
Terraform uses a gRPC-based plugin architecture where each provider runs as a **separate process** from Terraform Core. Compare this to a hypothetical design where all provider code is compiled directly into the Terraform CLI binary. What is the most significant operational advantage the actual gRPC plugin model provides?

- A) gRPC communication is faster than in-process function calls, making provider operations significantly more performant than the monolithic alternative
- B) Providers can be **upgraded independently** of Terraform Core — new AWS provider features can be released and adopted without reinstalling or upgrading the Terraform CLI binary itself; conversely, Terraform Core can be upgraded without requiring all providers to be rebuilt simultaneously
- C) The separate process model is more secure because provider crashes cannot be detected by Terraform Core — failures are silently handled
- D) gRPC enforces stronger schema validation than in-process calls — the monolithic model would allow invalid resource attributes to bypass provider schema checks

---

### Question 25 — Three Sources of Truth During `terraform plan`

**Difficulty**: Hard
**Answer Type**: one
**Topic**: Contrast between the roles of desired state, known state, and actual state during planning

**Question**:
During `terraform plan`, Terraform consults three distinct sources of information. Compare the role of each source and explain what Terraform does with them to generate the plan output:

1. The `.tf` configuration files (desired state)
2. The `terraform.tfstate` file (known state)
3. The live cloud resources (actual state, queried via provider API)

What is the correct description of how all three contribute to the plan?

- A) Terraform uses only the `.tf` files and `terraform.tfstate`; it does not make live API calls during `terraform plan`
- B) Terraform discards the `terraform.tfstate` during plan and compares only the `.tf` files against the live cloud state
- C) Terraform first **refreshes** known state by querying live cloud resources via the provider API (updating its view of actual state), then compares the refreshed actual state against the desired state in `.tf` files — the diff between desired and actual produces the plan of changes needed
- D) Terraform uses only the live cloud resources and the `.tf` files; the state file is only consulted during `terraform apply` to record results

---

### Question 26 — `terraform fmt` vs `terraform validate`: What Each Checks

**Difficulty**: Easy
**Answer Type**: one
**Topic**: Contrast between what `fmt` enforces and what `validate` enforces, and what they share in common

**Question**:
Compare `terraform fmt` and `terraform validate`. What does each command check, and what do they have in common?

- A) `terraform fmt` checks for undeclared variables; `terraform validate` checks for inconsistent indentation — both require cloud provider credentials
- B) `terraform fmt` corrects HCL code style and formatting (indentation, alignment, whitespace); `terraform validate` checks syntax correctness, undeclared references, type errors, and invalid argument names — both are fully offline and require no provider credentials or network access
- C) `terraform fmt` validates that resource arguments match the provider schema; `terraform validate` formats the output of `terraform plan` for readability
- D) Both commands are identical in what they check — `validate` is simply the strict mode of `fmt`

---

### Question 27 — `terraform plan` vs `terraform apply`: State File Impact

**Difficulty**: Easy
**Answer Type**: one
**Topic**: Contrast between which command reads state without modifying it and which modifies state

**Question**:
Compare `terraform plan` and `terraform apply` with respect to how each interacts with the Terraform state file. Which statement correctly describes the difference?

- A) `terraform plan` reads and writes the state file; `terraform apply` writes a new state file and archives the old one
- B) `terraform plan` generates and displays an execution plan without modifying the state file; `terraform apply` executes the plan and updates the state file to reflect the changes made
- C) Both commands modify the state file — `plan` updates it with the proposed changes and `apply` confirms them
- D) Neither command modifies the state file — state is only changed by `terraform state mv` and `terraform state rm`

---

### Question 28 — `terraform workspace new` vs `terraform workspace select`

**Difficulty**: Easy
**Answer Type**: one
**Topic**: Contrast between creating a new workspace and selecting an existing one

**Question**:
Compare `terraform workspace new staging` and `terraform workspace select staging`. What is the key functional difference between these two commands?

- A) Both commands are identical — `new` and `select` are aliases for the same operation
- B) `terraform workspace new staging` creates a new workspace named `staging` (it fails if `staging` already exists) and switches to it; `terraform workspace select staging` switches to the existing workspace named `staging` (it fails if `staging` does not yet exist)
- C) `terraform workspace new staging` copies the current workspace's state to `staging`; `terraform workspace select staging` creates an empty new workspace
- D) `terraform workspace new staging` creates the workspace but does not switch to it; `terraform workspace select staging` switches to it without creating it

---

### Question 29 — `terraform apply` with No Saved Plan vs `terraform apply plan.tfplan`

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Contrast between implicit re-planning and deterministic saved-plan execution

**Question**:
An engineer reviews the output of `terraform plan` showing 3 resources to add. They then wait 10 minutes before applying. Compare the two approaches below — what is the key difference in what actually gets applied?

- **Approach A**: Run `terraform apply` (no saved plan) 10 minutes after reviewing the plan
- **Approach B**: Run `terraform plan -out=release.tfplan`, review the output, then run `terraform apply release.tfplan`

- A) Both approaches apply the same changes — Terraform re-uses the plan output from the previous run regardless
- B) In Approach A, Terraform performs a **new implicit plan** at apply time — if the infrastructure changed in the 10-minute gap, the actual changes may differ from what was reviewed; in Approach B, the exact plan that was reviewed is applied with no re-planning, guaranteeing deterministic execution
- C) Approach A is safer because Terraform re-plans to incorporate any recent changes; Approach B may apply a stale plan that is no longer valid
- D) Both approaches result in an interactive prompt — the only difference is file I/O overhead

---

### Question 30 — `terraform init` vs `terraform init -reconfigure`

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Contrast between standard backend init and forced backend reconfiguration

**Question**:
A team changes the backend configuration in their `terraform` block from one S3 bucket to a different S3 bucket. They run `terraform init`. Terraform prompts them to choose between migrating state or continuing without migrating. Compare this behaviour to running `terraform init -reconfigure`. What is the operational difference?

- A) `terraform init -reconfigure` migrates all state from the old backend to the new backend automatically; standard `terraform init` requires manual confirmation
- B) `terraform init -reconfigure` initialises the new backend configuration without migrating any existing state and without prompting — the old backend's state is left in place and the new backend starts empty; standard `terraform init` offers the option to migrate state to the new backend
- C) Both commands produce identical behaviour — `-reconfigure` is simply a flag that suppresses the interactive prompt while still migrating state
- D) `-reconfigure` is only valid for the first `terraform init` run; after a backend exists, only standard `terraform init` can be used

---

### Question 31 — `terraform fmt` (No Flags) vs `terraform fmt -diff`

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Contrast between in-place formatting and diff-only preview

**Question**:
Compare running `terraform fmt` with no flags versus `terraform fmt -diff`. A `.tf` file has inconsistent indentation. What happens to the file in each case?

- A) Both commands modify the file — `-diff` additionally shows the changes that were made
- B) `terraform fmt` (no flags) rewrites the file directly on disk to canonical format; `terraform fmt -diff` displays a unified diff showing what would change **without writing any changes to disk**
- C) `terraform fmt` (no flags) only prints the file names that need formatting; `-diff` both shows and applies the changes
- D) Both commands are read-only — to actually reformat a file you must pipe the diff output back to the file manually

---

### Question 32 — `terraform plan -refresh=false` vs Standard `terraform plan`

**Difficulty**: Medium
**Answer Type**: many
**Topic**: Contrasting two key differences between a refresh-skipping plan and a full live-query plan

**Question**:
Compare `terraform plan` (standard) with `terraform plan -refresh=false`. Which TWO statements correctly describe a difference between the two? (Select two.)

- A) Standard `terraform plan` queries the live provider API to refresh each resource's actual current attributes before computing the diff; `terraform plan -refresh=false` uses the cached state from the last apply without making any API calls
- B) `terraform plan -refresh=false` is more accurate than standard `terraform plan` because it avoids potential API rate-limiting errors
- C) If an out-of-band change was made to a resource in the cloud (e.g., a tag changed via the console), standard `terraform plan` detects this and includes it in the plan diff; `terraform plan -refresh=false` does not detect the drift because it never queries the live API
- D) Both commands always produce identical plan output — the `-refresh=false` flag only affects performance, not the content of the plan

---

### Question 33 — `terraform output` vs `terraform output -json`

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Contrast between human-readable output display and structured JSON output for scripting

**Question**:
Compare `terraform output` (no flags) and `terraform output -json`. A configuration has two outputs: a string `vpc_id` and a list `subnet_ids`. How does the format of each command's response differ, and which is more appropriate for use in a CI script?

- A) Both return identical data — the only difference is that `-json` wraps the output in a JSON array
- B) `terraform output` prints all output values in human-readable format (strings quoted, lists formatted); `terraform output -json` returns a structured JSON object with `sensitive`, `type`, and `value` metadata fields for each output — the JSON format is the appropriate choice for CI scripts and programmatic processing
- C) `terraform output -json` is only valid for outputs declared with `type = "string"` — list outputs require `terraform output` without flags
- D) `terraform output` returns values without quotes for scripting; `-json` adds quotes and type annotations for documentation purposes

---

### Question 34 — `terraform plan -target` vs Full `terraform plan`

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Contrast between a targeted partial plan and a complete plan covering all resources

**Question**:
A configuration manages 30 resources. An engineer is debugging a single resource and runs `terraform plan -target=aws_instance.debug`. Compare this to running a full `terraform plan` with no target. What risk does the targeted approach introduce that the full plan does not?

- A) Targeted plans are more accurate because fewer resources are evaluated — there is no additional risk
- B) Targeted plans take longer because Terraform must first scan all 30 resources before filtering to the target
- C) A targeted plan only evaluates the specified resource and its direct dependencies — it may miss cascading changes to downstream resources that depend on the target, producing an **incomplete view** that does not reflect all the changes a full apply would cause; a full plan shows the complete picture
- D) Targeted plans lock the state file, preventing other engineers from running plans simultaneously

---

### Question 35 — `terraform destroy` (Full) vs `terraform destroy -target`

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Contrast between full environment destruction and targeted single-resource destruction

**Question**:
A production environment has 50 resources. An engineer needs to destroy only one obsolete EC2 instance (`aws_instance.legacy`). Compare running `terraform destroy` (no flags) versus `terraform destroy -target=aws_instance.legacy`. What is the critical difference in scope?

- A) Both commands destroy the same set of resources — `-target` is only valid with `apply`, not `destroy`
- B) `terraform destroy` (no flags) plans to destroy **all 50 resources** managed by the configuration; `terraform destroy -target=aws_instance.legacy` destroys only the targeted resource (and any resources that depend on it) — the other 49 resources are unaffected
- C) `terraform destroy -target` is not recommended because it deletes the entire resource group containing the target
- D) `terraform destroy` (no flags) only destroys resources in the current workspace; `-target` destroys the resource across all workspaces

---

### Question 36 — `~` Symbol vs `-/+` Symbol in Plan Output

**Difficulty**: Medium
**Answer Type**: many
**Topic**: Contrasting two key differences between update-in-place and replacement plan operations

**Question**:
Compare the `~` symbol and the `-/+` symbol in `terraform plan` output. Which TWO statements correctly distinguish these two plan operations? (Select two.)

- A) `~` indicates an **update in-place** — the existing resource object continues to exist and only specific attribute values are changed without destroying and recreating the resource
- B) `-/+` indicates that the resource will be **destroyed and then recreated** — a new resource object is provisioned to replace the old one, and the resource experiences downtime during the transition
- C) Both `~` and `-/+` result in the same final state — they differ only in whether Terraform prompts for confirmation
- D) `~` means the resource is being moved to a different Terraform workspace; `-/+` means it is being moved between providers

---

### Question 37 — `terraform init -migrate-state` vs `terraform init -reconfigure`

**Difficulty**: Hard
**Answer Type**: one
**Topic**: Deep contrast between migrating state to a new backend vs discarding the old backend's state record

**Question**:
A team is changing their Terraform backend from an S3 bucket in `us-east-1` to a new S3 bucket in `eu-west-1`. Their existing state file contains 40 resources. Compare `terraform init -migrate-state` and `terraform init -reconfigure` for this scenario. What is the critical operational difference?

- A) Both flags copy the state to the new backend — `-reconfigure` additionally cleans up the old backend
- B) `-migrate-state` and `-reconfigure` are equivalent; the distinction only matters when changing backend types, not when changing buckets within the same backend type
- C) `terraform init -migrate-state` copies the existing state from the old S3 bucket to the new S3 bucket before switching the active backend — all 40 resource records are preserved and Terraform continues managing them; `terraform init -reconfigure` initialises the new backend without copying any state — the new backend starts empty, and the 40 resources would appear unmanaged on the next plan
- D) `terraform init -reconfigure` is the recommended approach for cross-region state migration because `-migrate-state` only supports same-region moves

---

### Question 38 — `terraform graph` vs `terraform console`

**Difficulty**: Hard
**Answer Type**: one
**Topic**: Contrast between static dependency graph output and interactive expression evaluation

**Question**:
Compare `terraform graph` and `terraform console` as diagnostic and development tools. What does each command help the operator understand, and how do they differ in their interaction model and output?

- A) Both tools are interactive REPLs — `terraform graph` explores the dependency graph interactively; `terraform console` explores resource attributes interactively
- B) `terraform graph` is used to test HCL expressions before committing them; `terraform console` generates a visual map of resource dependencies
- C) `terraform graph` produces a **one-shot DOT-format text output** of the static resource dependency graph — it shows how resources depend on each other and what ordering Terraform will use for operations; it is non-interactive and requires Graphviz to render visually. `terraform console` is an **interactive REPL** that evaluates HCL expressions and built-in functions against the current configuration and state — it is used to test and debug expressions, functions, and variable references before embedding them in configuration files
- D) Both commands are deprecated — `terraform graph` was replaced by `terraform state list` and `terraform console` was replaced by `terraform validate`

---

### Question 39 — `resource` Block vs `data` Block: Management Model

**Difficulty**: Easy
**Answer Type**: one
**Topic**: Contrast between how Terraform treats a `resource` block and a `data` block

**Question**:
Compare a `resource` block and a `data` block in Terraform. What is the fundamental difference in how Terraform treats each one?

- A) Both blocks create and manage cloud infrastructure — `data` blocks are simply read-only after initial creation
- B) A `resource` block defines infrastructure that Terraform creates, updates, and destroys as part of its state-managed lifecycle; a `data` block queries existing infrastructure in read-only mode — it never creates, modifies, or destroys anything, and the queried object is not tracked as a managed resource in state
- C) `data` blocks are identical to `resource` blocks but execute during `terraform init` rather than `terraform apply`
- D) A `resource` block is used only for compute resources; a `data` block is used for networking and storage resources that already exist

---

### Question 40 — `count` vs `for_each`: Iteration Model

**Difficulty**: Easy
**Answer Type**: one
**Topic**: Contrast between numeric `count` iteration and key-based `for_each` iteration

**Question**:
Compare the `count` and `for_each` meta-arguments for creating multiple resource instances. What is the key structural difference between how they identify each instance?

- A) `count` is used for map-based resources; `for_each` is used for list-based resources — they are interchangeable for all other scenarios
- B) `count` creates a fixed number of identical instances identified by a zero-based integer index (`count.index`); `for_each` creates one instance per key in a map or element in a set, with each instance identified by a string key (`each.key`) and accessible value (`each.value`)
- C) `count` supports string keys; `for_each` supports only numeric indexes — they serve opposite roles from what their names suggest
- D) Both meta-arguments use the same `each.key` / `each.value` syntax to reference the current iteration context

---

### Question 41 — Implicit Dependency vs `depends_on`

**Difficulty**: Easy
**Answer Type**: one
**Topic**: Contrast between when Terraform auto-detects dependencies and when `depends_on` is required

**Question**:
Compare implicit dependencies and the `depends_on` meta-argument. When does Terraform create an implicit dependency automatically, and when must `depends_on` be used instead?

- A) Implicit dependencies are created when two resources share the same provider; `depends_on` is used when resources are in different providers
- B) Terraform creates an implicit dependency when a resource references an attribute of another resource (e.g., `subnet_id = aws_subnet.public.id`) — no `depends_on` is needed for these; `depends_on` is required only when a dependency exists that Terraform cannot detect through attribute references, such as IAM permissions that must be active before a resource uses them
- C) `depends_on` is always required — Terraform never infers ordering automatically from attribute references
- D) Implicit dependencies are detected through `var.*` references; `depends_on` is used for resource attribute references

---

### Question 42 — `create_before_destroy = true` vs Default Replacement Order

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Contrast between the default destroy-first replacement sequence and the reversed create-first sequence

**Question**:
An `aws_lb_target_group` must be replaced because an immutable argument changed. Compare the two replacement strategies below — what is the operational difference?

- **Strategy A**: No `lifecycle` block (default behaviour)
- **Strategy B**: `lifecycle { create_before_destroy = true }`

- A) Both strategies result in identical behaviour — the default has always been create-before-destroy
- B) Strategy A (default) destroys the existing target group first and then creates the replacement, which causes the load balancer to have no target group during the transition; Strategy B creates the replacement target group first and only destroys the old one after the new one is successfully provisioned, maintaining availability during the transition
- C) Strategy B is only relevant for resources that support zero-downtime updates; for stateless resources like target groups, both strategies are identical
- D) Strategy A is safer because destroying first ensures no duplicate resources exist in the cloud simultaneously

---

### Question 43 — `prevent_destroy` vs `ignore_changes`

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Contrast between destruction protection and drift suppression in `lifecycle` blocks

**Question**:
Compare `prevent_destroy = true` and `ignore_changes = [tags]` in a `lifecycle` block. What does each protect against, and in what scenario would you use each?

- A) Both arguments prevent Terraform from making any changes to a resource — they serve the same purpose but one is for destroy operations and the other for update operations
- B) `prevent_destroy = true` causes Terraform to return an error if a plan includes the destruction of that resource — protecting against accidental deletion of critical resources like production databases; `ignore_changes = [tags]` tells Terraform to disregard drift in the listed attributes, so external changes to those attributes (e.g., tags added by an automation tool) do not appear as unwanted changes in future plans
- C) `prevent_destroy` ignores all planned changes; `ignore_changes` only prevents destruction — they are named in the reverse of their actual purpose
- D) `prevent_destroy` applies only during `terraform destroy` operations; it has no effect when a resource is destroyed as part of a replacement during `terraform apply`

---

### Question 44 — `count` Instance Address vs `for_each` Instance Address

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Contrast between the bracket notation used for `count` instances and `for_each` instances

**Question**:
A configuration has two resources that create three web instances — one using `count = 3` and one using `for_each = toset(["us-east-1", "eu-west-1", "ap-southeast-1"])`. How does the state address format differ between these two approaches?

- A) Both use numeric indexes — `aws_instance.web[0]`, `aws_instance.web[1]`, etc.
- B) `count` instances are addressed with zero-based integer indexes (e.g., `aws_instance.web[0]`, `aws_instance.web[1]`, `aws_instance.web[2]`); `for_each` instances are addressed using their string key (e.g., `aws_instance.web["us-east-1"]`, `aws_instance.web["eu-west-1"]`)
- C) Both use string keys — `count` generates keys from `count.index` converted to a string
- D) `for_each` instances are addressed with integer indexes; `count` instances use string keys derived from each resource's `id` attribute

---

### Question 45 — `moved` Block vs `terraform state mv`

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Contrast between the HCL-based `moved` block and the CLI `state mv` command for renaming resources

**Question**:
A team needs to rename a resource in their Terraform configuration from `aws_instance.server` to `aws_instance.api`. Compare using a `moved` block in configuration versus running `terraform state mv aws_instance.server aws_instance.api`. What is the key operational difference?

- A) Both approaches are identical in effect — the `moved` block is simply the newer syntax for `terraform state mv`
- B) A `moved` block is declared in HCL and processed during `terraform plan`/`apply` — it is version-controlled alongside the configuration, can be reviewed in pull requests, and is executed automatically for all team members on their next apply; `terraform state mv` is an imperative CLI command that manipulates the state file directly and immediately, bypassing the plan/apply workflow — the change takes effect for whoever runs the command but is not tracked in configuration
- C) `terraform state mv` is preferred because it provides rollback capabilities; the `moved` block permanently alters the state with no way to revert
- D) `moved` blocks can only rename resources within a module; `terraform state mv` is required for root module renames

---

### Question 46 — `removed` Block (`destroy = false`) vs `terraform state rm`

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Contrast between declaratively un-tracking a resource and imperatively removing it from state

**Question**:
An `aws_instance.legacy` resource was created by Terraform but should now be managed manually outside Terraform. The team wants Terraform to stop tracking it without destroying it in AWS. Compare these two approaches:

- **Approach A**: Add a `removed` block with `lifecycle { destroy = false }`
- **Approach B**: Run `terraform state rm aws_instance.legacy`

What is the key difference?

- A) Both approaches destroy the EC2 instance in AWS and remove it from state simultaneously
- B) Approach A (`removed` block) is declarative — it is committed to the configuration and applied through the plan/apply workflow, giving the team visibility and auditability; Approach B (`terraform state rm`) is an imperative CLI command that removes the resource from state immediately without going through a plan — effective immediately but not tracked in configuration
- C) `terraform state rm` keeps the resource in the state file as read-only; the `removed` block completely deletes the state entry
- D) The `removed` block with `destroy = false` is only valid in Terraform Enterprise; `terraform state rm` must be used in open-source Terraform

---

### Question 47 — `ignore_changes = [specific_attrs]` vs `ignore_changes = all`

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Contrast between targeted drift suppression and complete drift suppression

**Question**:
Compare `ignore_changes = [tags, user_data]` with `ignore_changes = all` in a `lifecycle` block. What is the key operational risk difference between these two forms?

- A) Both forms are equivalent — listing attributes is just a more verbose way of writing `all`
- B) `ignore_changes = [tags, user_data]` suppresses drift only for the explicitly listed attributes — changes to any unlisted attribute (e.g., `instance_type`) are still detected and shown in plan; `ignore_changes = all` suppresses drift detection for **every** attribute of the resource, meaning configuration changes to any argument will silently have no effect in future plans — this can cause Terraform to diverge permanently from the actual state of the resource
- C) `ignore_changes = all` is the safer option because it ensures no unintentional changes are applied to the resource
- D) `ignore_changes = [tags, user_data]` causes Terraform to import those attributes from the live resource on every plan; `ignore_changes = all` skips the refresh phase for the resource entirely

---

### Question 48 — Data Source Read at Plan vs Data Source Read at Apply

**Difficulty**: Medium
**Answer Type**: many
**Topic**: Contrasting TWO scenarios that determine whether a data source is read during plan or deferred to apply

**Question**:
Compare when a data source is read during the `plan` phase versus when it is deferred to the `apply` phase. Which TWO statements correctly describe this difference? (Select two.)

- A) A data source whose filter arguments are all known static values or already-resolved references is read during `terraform plan` — the result is available in the plan output
- B) All data sources are always read during `terraform apply`, never during `terraform plan`
- C) A data source whose filter arguments depend on a value that is only known after another resource is created (e.g., filtering by the ID of a resource being created in the same apply) is deferred and read during `terraform apply` after its dependency is provisioned
- D) Data sources are read during `terraform init` — neither `plan` nor `apply` triggers data source queries

---

### Question 49 — `replace_triggered_by` vs `depends_on`

**Difficulty**: Medium
**Answer Type**: many
**Topic**: Contrasting TWO key differences between the `replace_triggered_by` lifecycle argument and the `depends_on` meta-argument

**Question**:
Compare `replace_triggered_by` in a `lifecycle` block with the `depends_on` meta-argument. Which TWO statements correctly describe a difference between these two? (Select two.)

- A) `depends_on` controls **execution ordering** — it ensures one resource is fully created before another begins, but it does not force any resource to be destroyed or recreated; `replace_triggered_by` forces the resource to be **destroyed and recreated** when a referenced resource or attribute changes
- B) Both `replace_triggered_by` and `depends_on` are interchangeable — they differ only in syntax
- C) `replace_triggered_by` creates a dependency that also acts as a **replacement trigger** — when the referenced resource changes, the resource with `replace_triggered_by` is scheduled for replacement in the next plan; `depends_on` only controls ordering and never triggers replacement
- D) `depends_on` causes a replacement; `replace_triggered_by` only controls creation order

---

### Question 50 — `count` vs `for_each`: Accepted Input Types and Mutual Exclusivity

**Difficulty**: Hard
**Answer Type**: many
**Topic**: Contrasting TWO technical constraints that differ between `count` and `for_each`

**Question**:
Compare `count` and `for_each` on two specific technical constraints. Which TWO statements are correct? (Select two.)

- A) `count` accepts any non-negative integer value; `for_each` accepts a `map` or a `set(string)` — it does NOT accept a plain `list(string)` without first converting it with `toset()`
- B) `for_each` accepts a plain `list(string)` directly — no type conversion is needed
- C) `count` and `for_each` are mutually exclusive — a single resource block cannot use both simultaneously; attempting to do so causes a Terraform validation error
- D) `count` and `for_each` can be combined on a single resource — `count` controls the number of copies and `for_each` assigns a key to each

---

### Question 51 — `create_before_destroy` vs `replace_triggered_by`: Two Lifecycle Mechanisms Affecting Replacement

**Difficulty**: Hard
**Answer Type**: one
**Topic**: Deep contrast between the two `lifecycle` arguments that both involve resource replacement but serve different purposes

**Question**:
Both `create_before_destroy = true` and `replace_triggered_by = [...]` involve resource replacement in Terraform. Compare them — what distinct problem does each solve, and can they be used together?

- A) They are synonyms — `replace_triggered_by` is the newer name for `create_before_destroy` introduced in Terraform 1.2+
- B) `create_before_destroy = true` controls **when in the replacement sequence** the new resource is provisioned relative to the old one (create-first vs destroy-first) — it does not change what triggers a replacement; `replace_triggered_by = [...]` controls **what events trigger a replacement** — it causes the resource to be replaced when a referenced resource or attribute changes, even if the resource's own configuration hasn't changed; the two are orthogonal and can be combined to get both a triggered replacement and a safe create-before-destroy sequence
- C) `replace_triggered_by` overrides `create_before_destroy` — if both are set, Terraform uses destroy-first ordering regardless
- D) `create_before_destroy` triggers replacements proactively; `replace_triggered_by` only changes the sequencing of a replacement that was already planned for other reasons

---

### Question 52 — `var.*` vs `local.*`: External Input vs Internal Computed Value

**Difficulty**: Easy
**Answer Type**: one
**Topic**: Contrast between input variables and local values in purpose, scope, and mutability

**Question**:
Compare an input variable (`var.*`) and a local value (`local.*`) in Terraform. What is the fundamental difference between the two?

- A) Input variables and locals are interchangeable — locals are simply a shorthand for variables that have a default value
- B) An input variable (`var.*`) is an externally supplied value — it can be set by a caller via CLI flags, `.tfvars` files, or environment variables, and it forms part of the module's interface; a local value (`local.*`) is an internally computed value — it is calculated from other values within the module, cannot be set by callers, and is not part of the module's external interface
- C) Local values can be set from outside the module via `TF_LOCAL_*` environment variables; input variables cannot be overridden at runtime
- D) Input variables can reference resource attribute values in their `default` argument; locals cannot reference resource attributes

---

### Question 53 — Variable with `default` vs Required Variable

**Difficulty**: Easy
**Answer Type**: one
**Topic**: Contrast between optional variables (with default) and required variables (no default)

**Question**:
Compare a variable block that includes a `default` argument with one that omits it. What is the operational difference during `terraform apply`?

- A) Variables without a `default` are always invalid — Terraform requires a default on every variable
- B) A variable with a `default` is optional — if no value is provided through any input mechanism, Terraform uses the default and does not prompt the operator; a variable without a `default` is required — Terraform will interactively prompt the operator for a value if none is provided, or fail if running non-interactively without one
- C) Variables with `default` are evaluated at `terraform init`; variables without `default` are evaluated at `terraform apply`
- D) A variable without a `default` causes Terraform to use `null` if no value is supplied — there is no interactive prompt

---

### Question 54 — `list(string)` vs `set(string)`: Ordering and Uniqueness

**Difficulty**: Easy
**Answer Type**: one
**Topic**: Contrast between the `list` and `set` collection types in Terraform

**Question**:
Compare the `list(string)` and `set(string)` types in Terraform. What are the two key differences between them?

- A) `list(string)` is unordered and unique; `set(string)` is ordered and allows duplicates — they are opposites of their intuitive names
- B) A `list(string)` is ordered (elements have a defined position accessible by index) and allows duplicate values; a `set(string)` is unordered (no guaranteed element order) and enforces uniqueness — duplicate values are silently removed when a list is converted to a set
- C) Both types are ordered and unique — the only difference is that `set(string)` can hold mixed types
- D) `list(string)` and `set(string)` are interchangeable — Terraform accepts either type wherever a collection of strings is expected

---

### Question 55 — `terraform.tfvars` vs `*.auto.tfvars`: Auto-Loading Mechanics

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Contrast between the two automatically loaded variable file mechanisms and their precedence relationship

**Question**:
Compare `terraform.tfvars` and files matching `*.auto.tfvars` (e.g., `prod.auto.tfvars`). What are the two key differences between them?

- A) `terraform.tfvars` is automatically loaded; `*.auto.tfvars` files must be specified explicitly with `-var-file` — they are not auto-loaded
- B) `terraform.tfvars` is a single fixed filename that Terraform auto-loads; `*.auto.tfvars` is a naming pattern — any file ending in `.auto.tfvars` is auto-loaded automatically; additionally, values in `*.auto.tfvars` files have **higher precedence** than `terraform.tfvars`, so `prod.auto.tfvars` overrides the same variable set in `terraform.tfvars`
- C) Both are identical in mechanics and precedence — the `.auto.` in the filename has no special meaning to Terraform
- D) `*.auto.tfvars` has lower precedence than `terraform.tfvars` because it uses a wildcard pattern rather than a fixed filename

---

### Question 56 — `output` Block vs `local` Value: Cross-Module vs Intra-Module

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Contrast between the purpose of output values and local values in module composition

**Question**:
Compare an `output` block and a `locals` block value. What is the key difference in where each value is accessible?

- A) Both `output` blocks and `local` values are accessible by the parent module — `locals` are simply the private variant of outputs
- B) A `local` value is scoped to the module in which it is defined and cannot be accessed by any caller — it is an internal computed value for reducing repetition within one module; an `output` value is the module's public interface — it exposes a value to the parent module (via `module.<name>.<output>`) or to the operator after apply (via `terraform output`)
- C) `output` values are only accessible during `terraform plan`; `local` values persist and are accessible during `terraform apply`
- D) Both `output` and `local` values can be accessed cross-module; `output` values are simply re-exported locals with no functional difference

---

### Question 57 — `map(string)` vs `object({...})`: Homogeneous vs Heterogeneous Attributes

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Contrast between the flexible but homogeneous `map` type and the structured but heterogeneous `object` type

**Question**:
Compare the `map(string)` type and the `object({ name = string, port = number })` type. What is the key structural difference between them?

- A) `map(string)` requires a fixed set of declared keys; `object({...})` allows any key to be added at runtime
- B) A `map(string)` is homogeneous — all values must be the same type (string in this case), but any key can be present and new keys can be added without changing the type definition; an `object({...})` is heterogeneous — each named attribute has its own individually declared type, the set of allowed attributes is fixed by the declaration, and different attributes can hold different types (e.g., `name` is a string while `port` is a number)
- C) Both types are identical — `map(string)` is simply shorthand for `object({})` with all string values
- D) `object({...})` accepts only string values for all attributes; `map(string)` allows values of any type

---

### Question 58 — `lookup()` vs Direct Map Indexing `map["key"]`

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Contrast between safe key lookup with a default and direct bracket indexing on error behaviour

**Question**:
Compare `lookup(var.ami_ids, "us-west-2", "ami-default")` with `var.ami_ids["us-west-2"]`. What is the key difference in behaviour when the key `"us-west-2"` does not exist in the map?

- A) Both expressions throw a Terraform error if the key does not exist — `lookup()` provides no additional safety
- B) `lookup(var.ami_ids, "us-west-2", "ami-default")` returns the third argument (`"ami-default"`) when the key is absent — no error is raised; `var.ami_ids["us-west-2"]` causes a Terraform error at plan or apply time if the key does not exist in the map
- C) `var.ami_ids["us-west-2"]` silently returns `null` when the key is absent; `lookup()` returns an error
- D) Both expressions return `null` for missing keys — the difference is only in syntax style

---

### Question 59 — `concat()` vs `flatten()`: Combining Lists vs Removing Nesting

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Contrast between joining multiple flat lists and flattening a single nested list structure

**Question**:
Compare `concat(list_a, list_b)` and `flatten([list_a, [list_b, list_c]])`. What problem does each function solve, and when would you choose one over the other?

- A) Both functions are identical — `flatten` simply uses different syntax to call the same underlying list-joining operation as `concat`
- B) `concat(list_a, list_b)` takes two or more already-flat lists as separate arguments and joins them into a single flat list; `flatten([list_a, [list_b, list_c]])` takes a single argument that is a list potentially containing nested sublists and recursively removes the nesting — use `concat` when joining known flat collections, and `flatten` when the input may contain lists nested within lists (e.g., a `for` expression that produces a list of lists)
- C) `concat` is for joining strings; `flatten` is for joining lists — they operate on different types
- D) `flatten` only removes one level of nesting; `concat` is required for deeply nested structures

---

### Question 60 — `coalesce()` vs `try()`: Two Different Fallback Mechanisms

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Contrast between null/empty-string fallback and expression-error fallback

**Question**:
Compare `coalesce(var.region, var.fallback_region, "us-east-1")` and `try(var.config["region"], "us-east-1")`. What kind of fallback does each function provide?

- A) Both functions are interchangeable — they both return the first non-null value from their arguments
- B) `coalesce()` returns the first argument in its list that is neither `null` nor an empty string — it evaluates all arguments and returns the first one with a meaningful value; `try()` evaluates its first expression and returns the fallback only if the expression itself produces a **runtime error** — it does not treat `null` or empty string as a failure condition
- C) `try()` returns the first non-null value; `coalesce()` suppresses errors from invalid expressions
- D) `coalesce()` is for numeric fallbacks only; `try()` is for string fallbacks only

---

### Question 61 — `[for ...]` vs `{for ...}`: List vs Map Output from `for` Expressions

**Difficulty**: Medium
**Answer Type**: many
**Topic**: Contrasting TWO key differences between list-producing and map-producing `for` expressions

**Question**:
Compare `[for n in var.names : upper(n)]` and `{for n in var.names : n => upper(n)}`. Which TWO statements correctly describe a difference between these two forms? (Select two.)

- A) The `[for ...]` form with square brackets produces a **list** — elements are ordered and accessible by zero-based index; the `{for ...}` form with curly braces and `=>` produces a **map** — elements are accessible by their declared key
- B) Both forms always produce a list — the curly braces in `{for ...}` are purely cosmetic and have no effect on the output type
- C) The map form `{for ...}` requires that the key expression (left side of `=>`) produce a unique value for each iteration — duplicate keys cause a Terraform error; the list form `[for ...]` has no such uniqueness requirement
- D) The list form `[for ...]` requires specifying both a key and a value separated by `=>`; the map form only specifies a single transform expression

---

### Question 62 — `sensitive = true` on a Variable vs `sensitive = true` on an Output

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Contrast between how sensitive masking behaves differently for variables and outputs

**Question**:
Both input variables and output blocks support `sensitive = true`. What is a key difference in how the masking behaviour works for each?

- A) They are identical in every respect — `sensitive = true` on a variable and on an output both produce exactly the same masking behaviour in every context
- B) `sensitive = true` on an **input variable** hides the value in plan and apply terminal output for any expression that uses the variable; `sensitive = true` on an **output** hides the value in the `terraform apply` summary and in the general `terraform output` listing — however, querying a sensitive output directly by name (`terraform output db_password`) or using `terraform output -json` reveals the plaintext value, making direct name-based queries an intentional escape hatch
- C) `sensitive = true` on an output permanently encrypts the value so it can never be retrieved; sensitive variables are only masked in the terminal but remain retrievable
- D) Sensitive output values are excluded from the state file; sensitive variable values are not

---

### Question 63 — `tuple` vs `list`: Fixed Mixed-Type vs Variable Homogeneous

**Difficulty**: Hard
**Answer Type**: many
**Topic**: Contrasting TWO structural differences between the `tuple` type and the `list` type

**Question**:
Compare the `tuple([string, number, bool])` type and the `list(string)` type. Which TWO statements correctly describe a structural difference between them? (Select two.)

- A) A `tuple` has a **fixed length** — the number of elements is defined in the type declaration and cannot change; a `list` has a **variable length** — elements can be added or removed without changing the type definition
- B) A `tuple` and a `list` both enforce that all elements are the same type — the only difference is that `tuple` also enforces element count
- C) A `tuple` allows **different types at different positions** — e.g., `tuple([string, number, bool])` holds a string at position 0, a number at position 1, and a bool at position 2; a `list` requires **all elements to be the same type** — a `list(string)` can only hold strings at every position
- D) A `list` type allows mixed element types by default; a `tuple` restricts all elements to the same type declared in its definition

---

### Question 64 — Variable Precedence: Specific Ordering Contrasts

**Difficulty**: Hard
**Answer Type**: many
**Topic**: Contrasting TWO specific precedence relationships in Terraform's variable input chain

**Question**:
Terraform resolves variable values from multiple sources using a defined precedence order. Which TWO statements correctly describe specific precedence relationships in that chain? (Select two.)

- A) `TF_VAR_*` environment variables have **higher** precedence than `*.auto.tfvars` files — if both set the same variable, the environment variable value is used
- B) `*.auto.tfvars` files have **higher** precedence than `terraform.tfvars` — if both set the same variable, the value from the `.auto.tfvars` file wins
- C) `terraform.tfvars` has **higher** precedence than `TF_VAR_*` environment variables — if both set the same variable, the `terraform.tfvars` value is used
- D) The `default` value in a variable block has **higher** precedence than `terraform.tfvars` — if both are present, the default is used

---

### Question 65 — `validation` Block vs `precondition`: When Each Runs

**Difficulty**: Easy
**Answer Type**: one
**Topic**: Contrast between the timing and triggering point of variable validation and lifecycle preconditions

**Question**:
Compare a `validation` block inside a `variable` declaration with a `precondition` block inside a resource's `lifecycle`. What is the key difference in when each runs during the Terraform workflow?

- A) Both run at the same point — they are two syntactic alternatives for the same assertion mechanism
- B) A `validation` block runs **before `terraform plan`** — it is evaluated during input variable processing and halts the run before any infrastructure analysis begins; a `precondition` runs **during `terraform apply`**, just before Terraform modifies the specific resource that contains it
- C) A `precondition` runs before `terraform plan`; a `validation` block runs after the plan is approved but before apply begins
- D) Both run after `terraform apply` completes — they are post-deployment verification tools

---

### Question 66 — `precondition` vs `postcondition`: Before vs After the Resource Change

**Difficulty**: Easy
**Answer Type**: one
**Topic**: Contrast between what precondition and postcondition assert and when each runs relative to the resource change

**Question**:
Compare a `precondition` and a `postcondition` declared in the same resource's `lifecycle` block. What is the key difference in their execution order and access to resource attributes?

- A) `precondition` and `postcondition` run at the same time — they differ only in whether the condition expression returns true or false
- B) A `precondition` runs **before** the resource is created or updated — it asserts that prerequisites are met and cannot use `self` to reference the resource's new attribute values; a `postcondition` runs **after** the resource change completes — it asserts that the created/updated resource meets requirements, and `self` references the resource's post-change attributes
- C) A `postcondition` runs before the resource change and uses `self` to reference the previous state; a `precondition` runs after and uses `self` to reference the new state
- D) Both can use `self`, but `precondition` uses the current (pre-change) `self` and `postcondition` uses the planned (post-change) `self`

---

### Question 67 — `check` Block vs `precondition`: Blocking vs Non-Blocking Failures

**Difficulty**: Easy
**Answer Type**: one
**Topic**: Contrast between the failure behaviour of check blocks and preconditions

**Question**:
Compare a failing `check` block assertion with a failing `precondition`. What is the fundamental difference in how Terraform handles each failure?

- A) Both a failing `check` block and a failing `precondition` block apply and allow all resources to be created
- B) A failing `precondition` **blocks** the apply — Terraform halts before modifying the resource and exits with a non-zero status; a failing `check` block assertion is a **warning only** — Terraform displays the error message but all resource changes proceed normally and the apply exits successfully
- C) A failing `check` block blocks the apply; a failing `precondition` produces a warning only
- D) Both a failing `check` block and a failing `precondition` roll back any resources already created in the same apply run

---

### Question 68 — `validation` Block Scope vs `precondition` Scope: What Each Can Reference

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Contrast between the expression scope allowed in validation conditions and precondition conditions

**Question**:
Compare what a `validation` block's `condition` and a `precondition`'s `condition` are each allowed to reference in their expressions. What is the key difference?

- A) Both are restricted to referencing only `var.<name>` — neither can reference data sources or resource attributes
- B) A `validation` block's `condition` can **only** reference `var.<variable_name>` — the specific variable being validated; a `precondition`'s `condition` can reference any value available at plan time, including data sources, other resource attributes, locals, and variables
- C) A `precondition`'s `condition` can only reference `self`; a `validation` block's `condition` can reference any expression including resources
- D) Both can reference any expression — the difference is only in when they are evaluated, not what they can reference

---

### Question 69 — `sensitive = true` on Variable: Terminal Masking vs State Protection

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Contrast between what sensitive=true on a variable actually protects vs what it does not protect

**Question**:
A variable is declared `sensitive = true` for a database password. Compare the protection this provides in two contexts: terminal output and the Terraform state file. What is the accurate description of each?

- A) `sensitive = true` both masks the value in terminal output AND encrypts it in the state file — it provides complete protection in both contexts
- B) `sensitive = true` **masks** the value in terminal output during `plan` and `apply` (showing `(sensitive value)` instead of the plaintext), but it provides **no protection** in the state file — the value is still stored in plaintext in `terraform.tfstate`; protecting it at rest requires an encrypted remote backend
- C) `sensitive = true` protects the value in the state file but has no effect on terminal output — the plaintext value is always shown during plan and apply
- D) `sensitive = true` removes the value from the state file entirely — it is never persisted anywhere

---

### Question 70 — `validation` Block vs `check` Block: Where Each Is Declared

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Contrast between the structural location of a validation block and a check block in HCL

**Question**:
Compare where a `validation` block and a `check` block are declared in a Terraform configuration. How does their structural location differ, and what does that difference imply?

- A) Both `validation` and `check` blocks are top-level HCL blocks — they sit at the root of any `.tf` file alongside `resource` and `provider` blocks
- B) A `validation` block is declared **nested inside a `variable` block** — it is scoped to that specific variable and can only reference that variable; a `check` block is a **top-level block** — it sits at the root of a `.tf` file like a `resource` or `output` block, and it can reference any infrastructure value in scope, optionally including a scoped `data` source
- C) A `check` block is nested inside a `resource` block's `lifecycle`; a `validation` block is a top-level block
- D) Both are nested inside the `lifecycle` block of the resource they guard

---

### Question 71 — `precondition` Failure vs `postcondition` Failure: Resource State After Each

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Contrast between the resource's state in AWS after a precondition failure vs a postcondition failure

**Question**:
An `aws_instance` resource has both a `precondition` and a `postcondition`. Compare the state of the EC2 instance in AWS after each type of failure:

- **Scenario A**: The `precondition` condition evaluates to `false` during apply
- **Scenario B**: The `postcondition` condition evaluates to `false` during apply

What is the difference in the real-world resource state between the two scenarios?

- A) In both scenarios, the EC2 instance is created in AWS — Terraform only removes it after the failure is acknowledged
- B) In Scenario A (precondition failure), the EC2 instance is **never created** in AWS — Terraform halts before making the API call; in Scenario B (postcondition failure), the EC2 instance **has been created** in AWS — Terraform only evaluates the postcondition after the API call succeeds, meaning the resource exists even though Terraform's apply failed
- C) In both scenarios, Terraform automatically destroys the resource and returns the infrastructure to its pre-apply state
- D) In Scenario A, the EC2 instance is created and then immediately destroyed; in Scenario B, the instance is never created

---

### Question 72 — `sensitive` Variable Propagation vs Explicit `sensitive` Output

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Contrast between automatic sensitive propagation and explicit output sensitivity declaration

**Question**:
Compare two approaches for preventing a database password from appearing in terminal output:

- **Approach A**: Declare `variable "db_password" { sensitive = true }` and use `var.db_password` in a resource; do not declare any output
- **Approach B**: Declare the variable without `sensitive`, but declare `output "db_password" { value = var.db_password; sensitive = true }`

What is a key difference between these two approaches?

- A) Both approaches are exactly equivalent in all scenarios — sensitive propagation and explicit output sensitivity are interchangeable
- B) In Approach A, the `sensitive = true` on the variable causes Terraform to **automatically propagate** the sensitive marker to any expression that uses `var.db_password` — plan output, error messages, and any output that references it will be masked without needing explicit `sensitive = true` on the output; in Approach B, only the specific `output` block is masked — `var.db_password` itself is not marked sensitive, so if it appears in plan output or error messages elsewhere in the configuration, it may not be automatically redacted
- C) Approach B is more secure than Approach A because explicitly marking an output as sensitive also encrypts the value in the state file
- D) Approach A prevents the value from being stored in state; Approach B stores it in state but masks it in terminal output

---

### Question 73 — `check` Block With Scoped Data Source vs `check` Block Without

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Contrast between a check block that embeds a scoped data source and one that references module-level values

**Question**:
Compare these two `check` block patterns:

**Pattern A** — scoped data source inside check:
```hcl
check "endpoint_health" {
  data "http" "ping" {
    url = "https://${aws_lb.web.dns_name}/health"
  }
  assert {
    condition     = data.http.ping.status_code == 200
    error_message = "Health endpoint returned ${data.http.ping.status_code}."
  }
}
```

**Pattern B** — no scoped data source:
```hcl
check "db_endpoint_set" {
  assert {
    condition     = can(tostring(aws_db_instance.main.endpoint))
    error_message = "Database endpoint attribute is not set."
  }
}
```

What is the key difference in scope between the two patterns?

- A) Pattern A is invalid — a `check` block cannot contain a `data` source; only `assert` blocks are allowed
- B) In Pattern A, the `data "http" "ping"` source is **scoped to the `check` block** — it is only evaluated during the check and its result is not accessible elsewhere in the module; in Pattern B, no data source is needed because the assert references an attribute directly from a resource already in state — the check block's assert can reference any module-level resource or data source without embedding a scoped source
- C) Pattern B is invalid because a `check` block must always contain a `data` source block
- D) The scoped data source in Pattern A is automatically added to the module's data sources and can be referenced from other resources

---

### Question 74 — Three Condition Mechanisms: Failure Behaviour Comparison

**Difficulty**: Medium
**Answer Type**: many
**Topic**: Contrasting TWO failure behaviour differences across the three assertion mechanisms

**Question**:
Terraform provides three condition assertion mechanisms: `validation`, `precondition`/`postcondition`, and `check`. Which TWO statements correctly describe a contrast in their failure behaviour? (Select two.)

- A) A failing `validation` condition halts Terraform **before any plan is generated** — the run aborts with the error_message and no infrastructure analysis is performed; a failing `check` assertion produces a **warning** that is displayed but does not prevent the apply from completing
- B) A failing `precondition` halts the apply **before modifying the target resource** — the resource is never created or updated; a failing `postcondition` halts the apply **after the resource has been created or updated** — the resource already exists in the cloud provider when the failure is reported
- C) `validation`, `precondition`, and `postcondition` all produce warnings only — none of them block the apply
- D) A failing `check` assertion blocks the apply and triggers a rollback of any resources created during the run

---

### Question 75 — `validation` Block vs `check` Block: What Each Can Reference

**Difficulty**: Hard
**Answer Type**: one
**Topic**: Deep contrast between the expression scope and structural rules governing validation conditions and check assertions

**Question**:
Both `validation` blocks and `check` block assertions use a `condition` expression that must evaluate to a boolean. Compare the expression scope rules for each — what can each reference, and what structural rule constrains the `check` block that does not apply to `validation`?

- A) Both `validation` and `check` block conditions are restricted to referencing only `var.<name>` — no other values are permitted in either context
- B) A `validation` block's `condition` can only reference `var.<variable_name>` — all other references are forbidden; a `check` block's `assert` condition can reference any module-level value (resources, data sources, locals, variables); however, if a `check` block includes a scoped `data` source, the data source reference in the assert must use the `data.<type>.<name>` form scoped to the check — and that scoped source cannot be referenced outside the `check` block
- C) A `check` block's condition is restricted to referencing only `data` source attributes; a `validation` block can reference any value including resource attributes
- D) Both can reference resource attributes and data source results — the only difference is that `validation` is evaluated earlier in the workflow

---

### Question 76 — `postcondition` with `self` vs `precondition` with External References

**Difficulty**: Hard
**Answer Type**: many
**Topic**: Contrasting TWO specific technical rules about expression references in preconditions and postconditions

**Question**:
Compare the expression reference rules for `precondition` and `postcondition` blocks. Which TWO statements correctly describe a difference? (Select two.)

- A) `self` is valid **only** in a `postcondition` — it refers to the resource after it has been created or updated; `self` is **not valid** in a `precondition` because the resource hasn't been created/modified yet when the precondition is evaluated
- B) A `precondition` can reference any value that is known at plan time — including other resource attributes, data sources, locals, and variables — but not `self`; a `postcondition` can reference all of those plus `self` to inspect the resource's own post-change attributes
- C) `self` is valid in both `precondition` and `postcondition`; the difference is that `self` in a `precondition` refers to the planned state while `self` in a `postcondition` refers to the applied state
- D) A `postcondition` can only reference `self` — it cannot reference other resources or module-level values

---

### Question 77 — `sensitive = true` vs Vault Dynamic Secrets: Protection Depth

**Difficulty**: Hard
**Answer Type**: one
**Topic**: Deep contrast between Terraform-native sensitive masking and HashiCorp Vault dynamic secrets as competing approaches to secret handling

**Question**:
Compare two approaches to managing a database password in Terraform:

- **Approach A**: Declare `variable "db_password" { sensitive = true }` and pass the password via `TF_VAR_db_password` at apply time
- **Approach B**: Use the Vault provider with a `data "vault_generic_secret"` data source to retrieve credentials dynamically during apply — no password variable in the Terraform configuration

What are the two most significant security differences between these approaches?

- A) Approach A is more secure because `sensitive = true` encrypts the value in state; Approach B stores the Vault token in state instead
- B) In Approach A, the password value **exists in the Terraform state file in plaintext** (despite the `sensitive = true` masking in terminal output) — anyone with read access to state can retrieve it; in Approach B, the credentials are **fetched dynamically** at apply time and are typically **short-lived** (dynamic secrets with a TTL) — they may never be stored in state as a sensitive value, and the Vault token used for authentication can be separately controlled and rotated independently of the database password
- C) Both approaches store the password in state — the only difference is that Approach B uses a second-factor Vault token alongside it
- D) Approach B is less secure because Vault data source results are never marked sensitive and will always appear in plaintext in terminal output and state

---

### Question 78 — Root Module vs Child Module: Role and Location

**Difficulty**: Easy
**Answer Type**: one
**Topic**: Contrast between what the root module and a child module are in a Terraform configuration

**Question**:
Compare the **root module** with a **child module** in Terraform. What is the key difference between the two?

- A) The root module is always stored on the Terraform Registry; a child module is always a local directory
- B) The root module is the working directory from which you run Terraform commands — it contains the top-level `.tf` files you execute; a child module is any module called via a `module` block from the root or from another module — it may be a local subdirectory, a registry module, or a Git source
- C) The root module can only call one child module at a time; child modules can call unlimited other child modules
- D) A child module is the first module Terraform processes; the root module is processed last after all child modules complete

---

### Question 79 — Local Path Module Source vs Terraform Registry Module Source

**Difficulty**: Easy
**Answer Type**: one
**Topic**: Contrast between how local path and Terraform Registry module sources are specified and what constraints each supports

**Question**:
Compare a local path module source with a Terraform Registry module source. What is the key structural and capability difference?

- A) A local path source uses `http://` as the prefix; a registry source uses `registry://` as the prefix
- B) A local path source begins with `./` or `../` and references a directory on the local filesystem — the `version` argument is **not supported** for local paths; a Terraform Registry source uses the three-part `<NAMESPACE>/<MODULE>/<PROVIDER>` format and **does support** the `version` argument for version constraints
- C) Both local path and registry sources support the `version` argument — the difference is that local paths require a full absolute path while registry sources use a relative namespace
- D) A registry source begins with `./registry/` to distinguish it from a local path; a local path omits the prefix entirely

---

### Question 80 — `version` Argument vs `?ref=` Query Parameter: Registry Pin vs Git Pin

**Difficulty**: Easy
**Answer Type**: one
**Topic**: Contrast between how registry modules and Git-sourced modules are pinned to a specific version

**Question**:
Compare pinning a Terraform Registry module to a specific version versus pinning a Git-sourced module to a specific version. What is the correct mechanism for each?

- A) Both registry modules and Git-sourced modules use the `version` argument in the `module` block — the syntax is identical for both source types
- B) Terraform Registry modules are pinned using the `version` argument in the `module` block (e.g., `version = "~> 5.0"`); Git-sourced modules are pinned using the `?ref=` query parameter in the `source` URL (e.g., `?ref=v2.1.0`) — the `version` argument is **not valid** for Git sources and causes a `terraform init` error
- C) Git-sourced modules use the `version` argument; registry modules use the `?ref=` query parameter in their registry URL
- D) Both source types accept the `version` argument, but for Git sources it must contain a full commit SHA rather than a semantic version string

---

### Question 81 — Child Module Variable Inheritance vs Explicit Input Passing

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Contrast between the assumption that child modules inherit parent variables and the actual explicit-passing requirement

**Question**:
A root module declares `variable "environment" {}` and its value is `"production"`. A child module also needs the environment name. Compare these two approaches:

- **Approach A**: Assume the child module automatically inherits `var.environment` from the root module — no input assignment in the `module` block
- **Approach B**: Explicitly pass the value in the `module` block: `environment = var.environment`

Which approach is correct, and why?

- A) Approach A is correct — child modules automatically inherit all variables declared in the calling module
- B) Approach B is correct — child modules do **not** inherit variables from their caller; every input a child module needs must be explicitly passed as an argument in the `module` block; if a variable is not passed, the child module uses its `default` value or fails if the variable has no default
- C) Both approaches work — Approach A uses implicit inheritance while Approach B uses explicit passing; the result is the same
- D) Approach A is correct for `string` variables; Approach B is only required for `list` and `map` types

---

### Question 82 — Referencing a Child Module Output vs Referencing a Resource Attribute

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Contrast between the syntax for accessing a child module's output and accessing a managed resource's attribute directly

**Question**:
Compare the syntax for referencing a value from a child module versus referencing an attribute from a managed resource directly. Given a module named `networking` with an output `vpc_id`, and a resource `aws_vpc` named `main` with attribute `id`, what is the correct syntax for each?

- A) Both use the same `resource.<name>.<attribute>` pattern — there is no distinction between module outputs and resource attributes at the reference level
- B) A child module output is referenced as `module.<module_name>.<output_name>` (e.g., `module.networking.vpc_id`); a managed resource attribute is referenced as `<resource_type>.<resource_name>.<attribute>` (e.g., `aws_vpc.main.id`) — the `module.` prefix clearly identifies a module output while the resource type prefix identifies a direct resource reference
- C) A child module output is referenced as `output.<module_name>.<output_name>`; a resource attribute uses `resource.<type>.<name>.<attr>`
- D) Both use `var.<name>` — module outputs and resource attributes are both treated as variable references in HCL

---

### Question 83 — `.terraform/modules/` Cache vs `.terraform/providers/` Cache

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Contrast between the purpose of the modules cache directory and the providers cache directory inside .terraform/

**Question**:
After running `terraform init`, two subdirectories are created inside `.terraform/`: `modules/` and `providers/`. Compare what each directory contains and why each needs to be refreshed.

- A) Both directories cache the same content — `modules/` stores a backup copy of the provider binaries and `providers/` stores a backup of the module source code
- B) `.terraform/modules/` contains the downloaded or locally-registered **module source code** for all `module` blocks in the configuration — it must be refreshed (by re-running `terraform init`) when a module `source` or `version` changes; `.terraform/providers/` contains the **provider plugin binaries** — it must be refreshed when the `required_providers` configuration changes or a new provider version is needed
- C) `.terraform/modules/` caches provider binaries; `.terraform/providers/` caches module source code — the names are inverted from what most developers expect
- D) Both directories are updated automatically on every `terraform plan` — no manual `terraform init` re-run is required after source changes

---

### Question 84 — Registry Module Source Format vs GitHub URL Format

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Contrast between the structural format of a Terraform Registry module source and a GitHub URL module source

**Question**:
Compare the format of a Terraform Registry module source and a GitHub module source. What are the key structural differences, and what capability does only one of them support?

- A) A Terraform Registry source uses `registry://` as a URL scheme; a GitHub source uses `github://` — they are otherwise structurally identical
- B) A Terraform Registry source uses the three-part `<NAMESPACE>/<MODULE>/<PROVIDER>` format (e.g., `"terraform-aws-modules/vpc/aws"`) and supports the `version` argument; a GitHub source uses a URL beginning with `github.com/` or `git::https://github.com/` and does **not** support the `version` argument — version pinning is done with `?ref=` in the URL
- C) A GitHub source uses the three-part namespace format; a Terraform Registry source uses a full HTTPS URL
- D) Both formats are valid for the `version` argument — the only difference is the URL protocol used

---

### Question 85 — `//` Double-Slash Subdirectory Separator vs `?ref=` Query Parameter in Git URLs

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Contrast between the two URL annotation mechanisms used in Git-based module sources

**Question**:
A module source reads:
```hcl
source = "github.com/acme/terraform-modules//modules/vpc?ref=v3.1.0"
```

Compare what `//modules/vpc` and `?ref=v3.1.0` each control. What is the difference?

- A) `//modules/vpc` pins the git checkout to a specific ref; `?ref=v3.1.0` selects a subdirectory
- B) `//modules/vpc` is the **subdirectory separator** — it tells Terraform to use the `modules/vpc` folder within the repository as the module root rather than the repository root; `?ref=v3.1.0` is the **git ref pin** — it specifies which tag, branch, or commit to check out; they are two independent mechanisms that can be combined in the same URL
- C) Both `//modules/vpc` and `?ref=v3.1.0` are version constraints — `//` specifies the major version and `?ref=` specifies the patch version
- D) `?ref=v3.1.0` is required when using `//` — without `?ref=`, the `//` separator is ignored by Terraform

---

### Question 86 — Child Module `output` Block vs Root Module `output` Block: Declaration and Access

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Contrast between how child module outputs and root module outputs are declared and how they are accessed differently

**Question**:
Compare an `output` block declared in a **child module** with an `output` block declared in the **root module**. How does the declaration differ, and how is each accessed?

- A) Child module `output` blocks use a different syntax than root module `output` blocks — child modules must use `export` instead of `output`
- B) The `output` block syntax is **identical** in both child and root modules — both use `output "<name>" { value = ... }`; however, their access pattern differs: a child module output is accessed from the caller as `module.<module_name>.<output_name>`, while a root module output is displayed in the terminal after `terraform apply` and is accessible via `terraform output <name>` — it is not referenced from a parent (the root has no caller)
- C) Child module `output` blocks must include `export = true` to be visible from the calling module; root module outputs are always visible without any extra argument
- D) Root module outputs are declared in a separate `outputs.tf` file; child module outputs must be declared in `main.tf`

---

### Question 87 — Two Differences Between Registry Module and Local Module

**Difficulty**: Medium
**Answer Type**: many
**Topic**: Contrasting TWO key differences between a published Terraform Registry module and a local path module

**Question**:
Compare a module sourced from the Terraform Registry with a module sourced from a local path. Which TWO statements correctly describe a difference? (Select two.)

- A) A Terraform Registry module supports the `version` argument and is downloaded by `terraform init` into `.terraform/modules/`; a local path module does **not** support `version` and is read directly from the filesystem — no downloading occurs during `terraform init`
- B) A Terraform Registry module must follow the naming convention `terraform-<PROVIDER>-<NAME>` to be publicly published; a local path module has no naming convention requirements — it can be named anything
- C) Both registry modules and local path modules require the `version` argument — without it, `terraform init` raises an error for both source types
- D) Local path modules support the `?ref=` query parameter for version pinning; registry modules use the `version` argument

---

### Question 88 — `terraform init` Re-run for New Module Source vs New Provider

**Difficulty**: Hard
**Answer Type**: one
**Topic**: Contrast between why terraform init must be re-run after adding a new module source vs adding a new provider

**Question**:
Both adding a new `module` block with a new `source` and adding a new `required_providers` entry require re-running `terraform init`. Compare the specific reason `terraform init` is needed in each case — what does it do differently for modules vs providers?

- A) `terraform init` does the same thing in both cases — it validates syntax and writes a lock file
- B) When a new **module source** is added, `terraform init` needs to **download or register the module source code** into `.terraform/modules/` — without this, Terraform cannot find the module's `.tf` files and `terraform plan` fails with "module not installed"; when a new **provider** is added, `terraform init` needs to **download the provider plugin binary** into `.terraform/providers/` and update `.terraform.lock.hcl` with the provider's version and hash — without this, Terraform cannot make API calls to the provider
- C) When a new module source is added, `terraform init` updates `.terraform.lock.hcl` with the module's hash; when a new provider is added, it updates `.terraform/modules/modules.json`
- D) For new module sources, `terraform init` is optional if the source is a local path; for new providers, it is always required — there is no scenario where a provider can be used without running `terraform init`

---

### Question 89 — Two Differences Between Module Input via Literal and via Expression

**Difficulty**: Hard
**Answer Type**: many
**Topic**: Contrasting TWO differences between hardcoding a module input as a literal value vs passing it as an expression referencing a root variable

**Question**:
Compare these two `module` blocks:

**Block A** — literal values:
```hcl
module "networking" {
  source      = "./modules/networking"
  environment = "production"
  vpc_cidr    = "10.0.0.0/16"
}
```

**Block B** — expression references:
```hcl
module "networking" {
  source      = "./modules/networking"
  environment = var.environment
  vpc_cidr    = var.vpc_cidr
}
```

Which TWO statements correctly describe a difference between the two approaches? (Select two.)

- A) Block B allows the same module instantiation to receive different values depending on how the root configuration is called or what `.tfvars` values are supplied — the module behaviour can vary across environments without modifying the `module` block; Block A hardcodes the values and requires editing `main.tf` to change the environment or CIDR
- B) Block A creates a **plan-time constant** dependency for the module inputs — Terraform can resolve the values during the graph construction phase without needing to evaluate variable expressions; Block B introduces a dependency on root variable values that must be resolved before the module inputs are finalised, but this adds no meaningful performance overhead in practice
- C) Block A is always more secure than Block B — hardcoded values cannot be overridden by malicious `.tfvars` files
- D) Passing expressions as in Block B causes Terraform to re-create the module's resources on every `terraform apply`, while Block A keeps resources stable because the values never change

---

### Question 90 — Standard Module File Structure vs Monolithic Single-File Module

**Difficulty**: Hard
**Answer Type**: one
**Topic**: Deep contrast between the recommended standard module file layout and collapsing everything into a single main.tf

**Question**:
The Terraform community recommends a standard module file structure:

```
module/
├── main.tf       — core resource definitions
├── variables.tf  — input variable declarations
├── outputs.tf    — output value declarations
└── versions.tf   — required_providers and terraform version constraint
```

Compare this against putting all declarations in a single `main.tf`. What are the two most significant practical differences?

- A) Using multiple files is mandatory — Terraform raises a validation error if variable declarations appear in `main.tf`
- B) Terraform is **file-agnostic** within a module directory — all `.tf` files in a directory are merged into a single namespace at parse time, so splitting across files versus using one file makes **no functional difference to Terraform itself**; the practical differences are entirely for **human maintainability**: the standard layout makes it immediately clear where to find variable definitions (`variables.tf`) and exported values (`outputs.tf`), while a monolithic `main.tf` requires scanning the entire file; for published or shared modules, the standard layout is a community convention that sets user expectations about where to look for the module's interface
- C) Using the standard layout allows Terraform to parse files in parallel, improving plan performance for large modules; a single `main.tf` forces sequential parsing
- D) `versions.tf` must be a separate file — it cannot be placed in `main.tf` because `terraform init` reads `versions.tf` before any other file during provider installation

---

### Question 91 — Local Backend vs S3 Backend: Collaboration and Safety

**Difficulty**: Easy
**Answer Type**: one
**Topic**: Contrast between the limitations of the local backend and the capabilities of a remote S3 backend

**Question**:
Compare the **local backend** (default `terraform.tfstate` file) with the **S3 backend**. What is the most significant operational difference between the two?

- A) The local backend encrypts state automatically; the S3 backend stores state in plaintext unless `encrypt = true` is set
- B) The local backend stores state in a file on the workstation running Terraform — it offers no collaboration support, no built-in locking, and no encryption; the S3 backend stores state in a shared S3 bucket — it enables team collaboration, supports state locking via DynamoDB, and supports server-side encryption at rest
- C) Both backends support state locking — the local backend uses a file lock while S3 uses DynamoDB; encryption is optional in both cases
- D) The S3 backend can only be used with AWS resources; the local backend supports all providers

---

### Question 92 — `terraform plan -refresh-only` vs `terraform apply -refresh-only`

**Difficulty**: Easy
**Answer Type**: one
**Topic**: Contrast between the plan-only and apply forms of the refresh-only flag

**Question**:
Compare `terraform plan -refresh-only` with `terraform apply -refresh-only`. What is the key difference between the two commands?

- A) `terraform plan -refresh-only` updates state to match the cloud; `terraform apply -refresh-only` only shows what has drifted without changing state
- B) `terraform plan -refresh-only` shows what drift exists between actual cloud resources and Terraform state — it **does not change state** and makes no modifications anywhere; `terraform apply -refresh-only` **updates state** to match the actual cloud resource values, reconciling drift — no infrastructure is created, modified, or destroyed in either case
- C) Both commands are identical — `-refresh-only` has the same effect regardless of whether it is used with `plan` or `apply`
- D) `terraform apply -refresh-only` creates new resources to match any detected drift; `terraform plan -refresh-only` only shows the diff

---

### Question 93 — `cloud` Block vs `backend "remote"`: Preferred HCP Terraform Connection

**Difficulty**: Easy
**Answer Type**: one
**Topic**: Contrast between the cloud block and the legacy remote backend for connecting to HCP Terraform

**Question**:
Compare the `cloud` block (Terraform 1.1+) with the `backend "remote"` block as methods for connecting to HCP Terraform. What is the key difference?

- A) `backend "remote"` is the current standard; the `cloud` block is a deprecated alias introduced for backward compatibility
- B) The `cloud` block is the **preferred, modern method** for connecting to HCP Terraform — it supports workspace selection by tags (in addition to name) and integrates features specific to HCP Terraform; `backend "remote"` is the **legacy method** — it is still valid and functional but predates HCP Terraform-specific features; HashiCorp recommends migrating to the `cloud` block
- C) Both blocks are exactly equivalent — the `cloud` block is simply renamed from `backend "remote"` with no functional differences
- D) The `cloud` block only supports HCP Terraform Free tier; `backend "remote"` is required for paid HCP Terraform tiers

---

### Question 94 — `terraform init -migrate-state` vs `terraform init -reconfigure`

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Contrast between the two init flags used when changing a backend configuration

**Question**:
Compare `terraform init -migrate-state` with `terraform init -reconfigure`. When would you use each, and what does each do with existing state?

- A) Both flags are equivalent — they both migrate state to the new backend without user confirmation
- B) `terraform init -migrate-state` **copies existing state** from the old backend to the newly configured backend — it is used when you want to preserve your state history when switching backends; `terraform init -reconfigure` **ignores the existing state** and reconfigures the backend without migrating — it is used when you want to start fresh or when the state has already been manually moved
- C) `terraform init -reconfigure` migrates state; `terraform init -migrate-state` discards it — the flags are inverted from what their names suggest
- D) `-migrate-state` only works when switching between two remote backends; it cannot migrate from the local backend to a remote backend

---

### Question 95 — `terraform state mv` vs `terraform state rm`

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Contrast between the purpose and effect of terraform state mv and terraform state rm

**Question**:
Compare `terraform state mv` with `terraform state rm`. Both modify what Terraform tracks in state — what is the fundamental difference between them?

- A) `terraform state mv` deletes a resource from both state and the cloud; `terraform state rm` only removes it from state while leaving the cloud resource intact
- B) `terraform state mv` **relocates** a resource within state — it renames or moves the resource's address (e.g., from `aws_instance.web` to `aws_instance.web_server`, or from a root resource into a module) without destroying or re-creating anything; `terraform state rm` **removes** a resource entry from state entirely — Terraform stops managing it, but the actual cloud resource is left untouched; the resource becomes unmanaged drift
- C) `terraform state rm` renames a resource; `terraform state mv` deletes it permanently from both state and the cloud provider
- D) Both commands are equivalent — the only difference is that `terraform state mv` requires confirmation while `terraform state rm` does not

---

### Question 96 — HCP Terraform Workspace Variables vs Variable Sets

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Contrast between workspace-specific variables and variable sets in HCP Terraform

**Question**:
Compare **workspace variables** with **variable sets** in HCP Terraform. What is the key difference in scope and reusability?

- A) Workspace variables are reusable across all workspaces in an organisation; variable sets are scoped to a single workspace only
- B) Workspace variables are defined **per workspace** — they apply only to that specific workspace and must be configured individually for each workspace that needs them; variable sets are **reusable collections** of variables that can be assigned to multiple workspaces or an entire organisation — a single change to a variable set propagates to all assigned workspaces
- C) Both workspace variables and variable sets work identically — the only difference is that variable sets have a different UI panel in HCP Terraform
- D) Variable sets are used only for Terraform input variables; workspace variables are used only for environment variables (like `AWS_ACCESS_KEY_ID`)

---

### Question 97 — Speculative Plan vs Plan-and-Apply Run in HCP Terraform

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Contrast between a speculative plan run and a plan-and-apply run in HCP Terraform

**Question**:
Compare a **speculative plan** run with a **plan-and-apply** run in HCP Terraform. What is the fundamental difference?

- A) A speculative plan is faster because it skips the refresh phase; a plan-and-apply run always refreshes state before planning
- B) A speculative plan is **read-only** — it computes what changes would occur but **can never progress to an apply**; it is triggered by pull requests or API calls and posts its results as status checks; a plan-and-apply run **can apply changes** — it proceeds through planning and, based on workspace settings, either auto-applies or waits for manual confirmation before applying
- C) A plan-and-apply run is triggered only by manual CLI commands; a speculative plan is triggered only by VCS events
- D) Both run types can apply infrastructure changes — the difference is that a speculative plan requires an additional approval step before applying

---

### Question 98 — `TF_LOG_CORE` vs `TF_LOG_PROVIDER` vs `TF_LOG`

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Contrast between the granular log variables and the combined TF_LOG variable

**Question**:
Compare `TF_LOG_CORE`, `TF_LOG_PROVIDER`, and `TF_LOG`. How do the granular variables differ from the single combined variable?

- A) `TF_LOG_CORE` and `TF_LOG_PROVIDER` are deprecated aliases for `TF_LOG` — they all control the same log stream
- B) `TF_LOG` sets a **single log level for all Terraform output** — both the core engine and provider plugins log at the same verbosity; `TF_LOG_CORE` and `TF_LOG_PROVIDER` are **independent controls** — `TF_LOG_CORE` controls only the Terraform core engine's log output, and `TF_LOG_PROVIDER` controls only the provider plugin log output; this allows operators to enable `TRACE` for a specific provider while keeping core logs at a quieter level (or vice versa), reducing noise when debugging provider-specific issues
- C) `TF_LOG_PROVIDER` sets log output for all Terraform runs in a project; `TF_LOG_CORE` sets it for a specific workspace; `TF_LOG` is the organisation-wide default
- D) `TF_LOG_CORE` and `TF_LOG_PROVIDER` only apply when `TF_LOG_PATH` is also set — without a path, only `TF_LOG` produces output

---

### Question 99 — Sentinel vs OPA: Two HCP Terraform Policy Frameworks

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Contrast between Sentinel and OPA as the two policy enforcement frameworks in HCP Terraform

**Question**:
HCP Terraform supports two policy enforcement frameworks: **Sentinel** and **OPA (Open Policy Agent)**. What is the key difference between them?

- A) Sentinel is used for cost estimation policies; OPA is used for security compliance policies — they target different policy domains
- B) Sentinel uses **HashiCorp's proprietary Sentinel DSL** — it is developed and maintained by HashiCorp and is tightly integrated with HCP Terraform's policy workflow; OPA uses **Rego**, an open-source policy language maintained by the Open Policy Agent community — it offers broader ecosystem support and is used across many tools beyond Terraform; both frameworks enforce the same three enforcement levels (advisory, soft-mandatory, hard-mandatory) in HCP Terraform
- C) OPA policies run before the plan; Sentinel policies run after the plan but before the apply — they execute at different points in the run lifecycle
- D) Sentinel is available on all HCP Terraform tiers; OPA is only available on the Enterprise tier and cannot be used in the Free or Plus plans

---

### Question 100 — Three Policy Enforcement Levels: Two Key Contrasts

**Difficulty**: Medium
**Answer Type**: many
**Topic**: Contrasting TWO of the three HCP Terraform policy enforcement levels

**Question**:
HCP Terraform policy sets support three enforcement levels: `advisory`, `soft-mandatory`, and `hard-mandatory`. Which TWO statements correctly describe a contrast between these levels? (Select two.)

- A) An `advisory` policy failure displays a warning but **does not block the run** — the plan-and-apply continues regardless of the policy result; a `hard-mandatory` policy failure **always blocks the run** and cannot be overridden by any user, including organisation owners
- B) A `soft-mandatory` policy failure blocks the run by default but can be **overridden** by a user with sufficient permissions (typically an organisation owner or designated override role) — the run can then proceed despite the policy failure; `hard-mandatory` failure **cannot be overridden** by any user under any circumstances
- C) `advisory` policies only apply to speculative plans; `soft-mandatory` and `hard-mandatory` policies apply to plan-and-apply runs
- D) All three enforcement levels cause the run to fail with a non-zero exit code — the difference is only in how the failure message is displayed in the UI

---

### Question 101 — HCP Terraform Owner Role vs Workspace Admin Permission

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Contrast between organisation-level Owner role and workspace-level Admin permission in HCP Terraform

**Question**:
Compare the **Owner** organisation-level role with the **Admin** workspace-level permission in HCP Terraform. What is the scope difference?

- A) Owner and Admin are the same role — "Owner" is the UI label and "Admin" is the API name for the same permission level
- B) **Owner** is an **organisation-level role** — it grants full access to all settings, workspaces, teams, and governance across the entire organisation; **Admin** is a **workspace-level permission** — it grants full control over a specific workspace (managing variables, team access, workspace settings, and run approvals) but has no authority over other workspaces or organisation-level settings unless that permission is explicitly granted on each workspace
- C) Admin is a superset of Owner — an Admin can manage organisation-level settings in addition to workspace-level settings
- D) Owner role is limited to read-only access across all workspaces; Admin is the role that allows applying changes

---

### Question 102 — Import Block Workflow vs CLI Import Workflow: Two Key Differences

**Difficulty**: Hard
**Answer Type**: many
**Topic**: Contrasting TWO workflow differences between the declarative import block (Terraform 1.5+) and the legacy terraform import CLI command

**Question**:
Compare the workflow for importing an existing resource using the declarative `import` block versus the legacy `terraform import` CLI command. Which TWO statements correctly describe a difference between the two workflows? (Select two.)

- A) The `import` block workflow supports **running `terraform plan` before any state changes are made** — the engineer can preview the import (and optionally generate HCL with `-generate-config-out`) before committing; the CLI `terraform import` command **immediately writes the resource to state** with no plan preview step — there is no way to preview what will be imported before the state is modified
- B) The CLI `terraform import` command **requires an existing resource block** in the configuration before it can run — the block body can be empty, but the block must exist; the `import` block can be added to configuration and used with `terraform plan -generate-config-out=generated.tf` to have Terraform **generate the resource block automatically** — the engineer starts with only the `import` block and no resource block
- C) Both workflows require the resource block to exist before the import command runs — the `import` block offers no config generation capability
- D) The CLI `terraform import` command can import multiple resources in a single run; the `import` block can only import one resource per block

---

### Question 103 — Dynamic OIDC Credentials vs Static Environment Variable Credentials in HCP Terraform

**Difficulty**: Hard
**Answer Type**: one
**Topic**: Deep contrast between dynamic OIDC-based provider authentication and static credential storage in HCP Terraform workspaces

**Question**:
Compare two approaches for authenticating an HCP Terraform workspace to AWS:

- **Approach A**: Store `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY` as sensitive environment variables in an HCP Terraform variable set
- **Approach B**: Configure dynamic provider credentials using OIDC — the workspace requests a short-lived token from HCP Terraform's OIDC provider, which AWS validates against a trusted identity provider, and returns temporary credentials

What are the two most significant security differences between these approaches?

- A) Approach A is more secure because the credentials are marked sensitive and are never shown in logs; Approach B exposes credentials in the plan output because OIDC tokens are not marked sensitive
- B) In Approach A, the **static credentials are long-lived** — they persist in HCP Terraform's variable storage indefinitely and if exfiltrated (e.g., from a compromised CI system or leaked variable export) they remain valid until manually rotated; in Approach B, credentials are **short-lived and scoped per run** — they are issued fresh for each Terraform run with a TTL, so a captured credential becomes useless quickly; additionally, Approach B **eliminates static secret storage** entirely — no `AWS_ACCESS_KEY_ID` or `AWS_SECRET_ACCESS_KEY` is stored anywhere in HCP Terraform, which removes a class of secret-leakage risk
- C) Approach A credentials are encrypted using HCP Terraform's AES-256 key management; Approach B credentials are stored in plaintext because they are temporary
- D) Both approaches have equivalent security — the static credentials in Approach A are marked sensitive, which provides the same protection as OIDC's short-lived tokens



## Answer Key

| Q# | Answer(s) | Explanation | Source | Difficulty |
|---|---|---|---|---|
| 2 | B | N/A | Contrast between a declarative HCL resource block and an imperative CLI command for the same infrastructure | Easy |
| 3 | B | N/A | Contrast between what the state file records and what the configuration file expresses | Easy |
| 4 | B | N/A | Contrast between Terraform's multi-cloud capability and CloudFormation's AWS-only scope | Medium |
| 5 | B | N/A | Contrast between the audit trail produced by IaC commits vs manual console changes | Medium |
| 6 | C | N/A | Contrast between what happens on the first apply vs a second apply with an unchanged configuration | Medium |
| 7 | B | N/A | Contrast between infrastructure provisioning (Terraform) and configuration management (Ansible) | Medium |
| 8 | B, C | N/A | Contrasting which IaC tools are limited to a single cloud provider vs those that support multiple providers | Medium |
| 9 | B | N/A | Contrast between how a team detects drift when using IaC versus when managing infrastructure manually | Medium |
| 10 | B | N/A | Contrast between recreating a lost environment with IaC versus without it | Medium |
| 11 | A, B | N/A | Contrasting how a manual cloud change and a Terraform configuration change are tracked and applied differently | Medium |
| 12 | C | N/A | Deep contrast between what an operator must define in a declarative model vs an imperative scripting approach | Hard |
| 13 | A, C | N/A | Contrasting the provisioning and configuration management layers in a complete infrastructure automation stack | Hard |
| 14 | B | N/A | Contrast between who maintains Official providers and who maintains Community providers | Easy |
| 15 | B | N/A | Contrast between the two most commonly confused pessimistic constraint operator patterns | Easy |
| 16 | D | N/A | Contrast between the gitignore treatment of the provider cache directory and the lock file | Easy |
| 17 | B | N/A | Contrast between what the source address and the version constraint each control | Medium |
| 18 | C | N/A | Contrast between standard init and upgrade init in terms of when each should be used | Medium |
| 19 | B | N/A | Contrast between how Terraform assigns resources to the default provider vs an aliased provider | Medium |
| 20 | C | N/A | Contrast between what state mv and state rm do to the tracked state and the actual cloud resource | Medium |
| 21 | B, C | N/A | Contrasting local and remote state on concurrent apply safety and team accessibility | Medium |
| 22 | B | N/A | Contrast between the targeted state show command and the full-state show command | Medium |
| 23 | B | N/A | Contrast between terminal display masking and actual state-at-rest encryption | Medium |
| 24 | A, C | N/A | Contrasting two specific risks of not committing the lock file vs always committing it | Medium |
| 25 | B | N/A | Contrast between Terraform's separate-process provider model and a hypothetical built-in provider model | Hard |
| 26 | C | N/A | Contrast between the roles of desired state, known state, and actual state during planning | Hard |
| 27 | B | N/A | Contrast between what `fmt` enforces and what `validate` enforces, and what they share in common | Easy |
| 28 | B | N/A | Contrast between which command reads state without modifying it and which modifies state | Easy |
| 29 | B | N/A | Contrast between creating a new workspace and selecting an existing one | Easy |
| 30 | B | N/A | Contrast between implicit re-planning and deterministic saved-plan execution | Medium |
| 31 | B | N/A | Contrast between standard backend init and forced backend reconfiguration | Medium |
| 32 | B | N/A | Contrast between in-place formatting and diff-only preview | Medium |
| 33 | A, C | N/A | Contrasting two key differences between a refresh-skipping plan and a full live-query plan | Medium |
| 34 | B | N/A | Contrast between human-readable output display and structured JSON output for scripting | Medium |
| 35 | C | N/A | Contrast between a targeted partial plan and a complete plan covering all resources | Medium |
| 36 | B | N/A | Contrast between full environment destruction and targeted single-resource destruction | Medium |
| 37 | A, B | N/A | Contrasting two key differences between update-in-place and replacement plan operations | Medium |
| 38 | C | N/A | Deep contrast between migrating state to a new backend vs discarding the old backend's state record | Hard |
| 39 | C | N/A | Contrast between static dependency graph output and interactive expression evaluation | Hard |
| 40 | B | N/A | Contrast between how Terraform treats a `resource` block and a `data` block | Easy |
| 41 | B | N/A | Contrast between numeric `count` iteration and key-based `for_each` iteration | Easy |
| 42 | B | N/A | Contrast between when Terraform auto-detects dependencies and when `depends_on` is required | Easy |
| 43 | B | N/A | Contrast between the default destroy-first replacement sequence and the reversed create-first sequence | Medium |
| 44 | B | N/A | Contrast between destruction protection and drift suppression in `lifecycle` blocks | Medium |
| 45 | B | N/A | Contrast between the bracket notation used for `count` instances and `for_each` instances | Medium |
| 46 | B | N/A | Contrast between the HCL-based `moved` block and the CLI `state mv` command for renaming resources | Medium |
| 47 | B | N/A | Contrast between declaratively un-tracking a resource and imperatively removing it from state | Medium |
| 48 | B | N/A | Contrast between targeted drift suppression and complete drift suppression | Medium |
| 49 | A, C | N/A | Contrasting TWO scenarios that determine whether a data source is read during plan or deferred to apply | Medium |
| 50 | A, C | N/A | Contrasting TWO key differences between the `replace_triggered_by` lifecycle argument and the `depends_on` meta-argument | Medium |
| 51 | A, C | N/A | Contrasting TWO technical constraints that differ between `count` and `for_each` | Hard |
| 52 | B | N/A | Deep contrast between the two `lifecycle` arguments that both involve resource replacement but serve different purposes | Hard |
| 53 | B | N/A | Contrast between input variables and local values in purpose, scope, and mutability | Easy |
| 54 | B | N/A | Contrast between optional variables (with default) and required variables (no default) | Easy |
| 55 | B | N/A | Contrast between the `list` and `set` collection types in Terraform | Easy |
| 56 | B | N/A | Contrast between the two automatically loaded variable file mechanisms and their precedence relationship | Medium |
| 57 | B | N/A | Contrast between the purpose of output values and local values in module composition | Medium |
| 58 | B | N/A | Contrast between the flexible but homogeneous `map` type and the structured but heterogeneous `object` type | Medium |
| 59 | B | N/A | Contrast between safe key lookup with a default and direct bracket indexing on error behaviour | Medium |
| 60 | B | N/A | Contrast between joining multiple flat lists and flattening a single nested list structure | Medium |
| 61 | B | N/A | Contrast between null/empty-string fallback and expression-error fallback | Medium |
| 62 | A, C | N/A | Contrasting TWO key differences between list-producing and map-producing `for` expressions | Medium |
| 63 | B | N/A | Contrast between how sensitive masking behaves differently for variables and outputs | Medium |
| 64 | A, C | N/A | Contrasting TWO structural differences between the `tuple` type and the `list` type | Hard |
| 65 | A, B | N/A | Contrasting TWO specific precedence relationships in Terraform's variable input chain | Hard |
| 66 | B | N/A | Contrast between the timing and triggering point of variable validation and lifecycle preconditions | Easy |
| 67 | B | N/A | Contrast between what precondition and postcondition assert and when each runs relative to the resource change | Easy |
| 68 | B | N/A | Contrast between the failure behaviour of check blocks and preconditions | Easy |
| 69 | B | N/A | Contrast between the expression scope allowed in validation conditions and precondition conditions | Medium |
| 70 | B | N/A | Contrast between what sensitive=true on a variable actually protects vs what it does not protect | Medium |
| 71 | B | N/A | Contrast between the structural location of a validation block and a check block in HCL | Medium |
| 72 | B | N/A | Contrast between the resource's state in AWS after a precondition failure vs a postcondition failure | Medium |
| 73 | B | N/A | Contrast between automatic sensitive propagation and explicit output sensitivity declaration | Medium |
| 74 | B | N/A | Contrast between a check block that embeds a scoped data source and one that references module-level values | Medium |
| 75 | A, B | N/A | Contrasting TWO failure behaviour differences across the three assertion mechanisms | Medium |
| 76 | B | N/A | Deep contrast between the expression scope and structural rules governing validation conditions and check assertions | Hard |
| 77 | A, B | N/A | Contrasting TWO specific technical rules about expression references in preconditions and postconditions | Hard |
| 78 | B | N/A | Deep contrast between Terraform-native sensitive masking and HashiCorp Vault dynamic secrets as competing approaches to secret handling | Hard |
| 79 | B | N/A | Contrast between what the root module and a child module are in a Terraform configuration | Easy |
| 80 | B | N/A | Contrast between how local path and Terraform Registry module sources are specified and what constraints each supports | Easy |
| 81 | B | N/A | Contrast between how registry modules and Git-sourced modules are pinned to a specific version | Easy |
| 82 | B | N/A | Contrast between the assumption that child modules inherit parent variables and the actual explicit-passing requirement | Medium |
| 83 | B | N/A | Contrast between the syntax for accessing a child module's output and accessing a managed resource's attribute directly | Medium |
| 84 | B | N/A | Contrast between the purpose of the modules cache directory and the providers cache directory inside .terraform/ | Medium |
| 85 | B | N/A | Contrast between the structural format of a Terraform Registry module source and a GitHub URL module source | Medium |
| 86 | B | N/A | Contrast between the two URL annotation mechanisms used in Git-based module sources | Medium |
| 87 | B | N/A | Contrast between how child module outputs and root module outputs are declared and how they are accessed differently | Medium |
| 88 | A, B | N/A | Contrasting TWO key differences between a published Terraform Registry module and a local path module | Medium |
| 89 | B | N/A | Contrast between why terraform init must be re-run after adding a new module source vs adding a new provider | Hard |
| 90 | A, B | N/A | Contrasting TWO differences between hardcoding a module input as a literal value vs passing it as an expression referencing a root variable | Hard |
| 91 | B | N/A | Deep contrast between the recommended standard module file layout and collapsing everything into a single main.tf | Hard |
| 92 | B | N/A | Contrast between the limitations of the local backend and the capabilities of a remote S3 backend | Easy |
| 93 | B | N/A | Contrast between the plan-only and apply forms of the refresh-only flag | Easy |
| 94 | B | N/A | Contrast between the cloud block and the legacy remote backend for connecting to HCP Terraform | Easy |
| 95 | B | N/A | Contrast between the two init flags used when changing a backend configuration | Medium |
| 96 | B | N/A | Contrast between the purpose and effect of terraform state mv and terraform state rm | Medium |
| 97 | B | N/A | Contrast between workspace-specific variables and variable sets in HCP Terraform | Medium |
| 98 | B | N/A | Contrast between a speculative plan run and a plan-and-apply run in HCP Terraform | Medium |
| 99 | B | N/A | Contrast between the granular log variables and the combined TF_LOG variable | Medium |
| 100 | B | N/A | Contrast between Sentinel and OPA as the two policy enforcement frameworks in HCP Terraform | Medium |
| 101 | A, B | N/A | Contrasting TWO of the three HCP Terraform policy enforcement levels | Medium |
| 102 | B | N/A | Contrast between organisation-level Owner role and workspace-level Admin permission in HCP Terraform | Medium |
| 103 | A, B | N/A | Contrasting TWO workflow differences between the declarative import block (Terraform 1.5+) and the legacy terraform import CLI command | Hard |
| 104 | B | N/A | Deep contrast between dynamic OIDC-based provider authentication and static credential storage in HCP Terraform workspaces | Hard |
