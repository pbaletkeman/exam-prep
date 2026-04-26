# Terraform Associate (004) — Question Bank Iter 5 Batch 1

**Iteration**: 5
**Iteration Style**: Comparison and contrast — distinguish between two similar concepts
**Batch**: 1
**Objective**: 1 — IaC Concepts
**Generated**: 2026-04-25
**Total Questions**: 12
**Difficulty Split**: 2 Easy / 8 Medium / 2 Hard
**Answer Types**: 9 `one` / 3 `many` / 0 `none`

---

# Terraform Associate (004) — Question Bank Iter 5 Batch 2

**Iteration**: 5
**Iteration Style**: Comparison and contrast — distinguish between two similar concepts
**Batch**: 2
**Objective**: 2 — Terraform Fundamentals (Providers & State)
**Generated**: 2026-04-25
**Total Questions**: 13
**Difficulty Split**: 3 Easy / 8 Medium / 2 Hard
**Answer Types**: 10 `one` / 3 `many` / 0 `none`

---

# Terraform Associate (004) — Question Bank Iter 5 Batch 3

**Iteration**: 5
**Iteration Style**: Comparison and contrast — distinguish between two similar concepts
**Batch**: 3
**Objective**: 3 — Core Workflow & CLI
**Generated**: 2026-04-25
**Total Questions**: 13
**Difficulty Split**: 3 Easy / 8 Medium / 2 Hard
**Answer Types**: 10 `one` / 3 `many` / 0 `none`

---

# Terraform Associate (004) — Question Bank Iter 5 Batch 4

**Iteration**: 5
**Iteration Style**: Comparison and contrast — distinguish between two similar concepts
**Batch**: 4
**Objective**: 4a — Resources, Data & Dependencies
**Generated**: 2026-04-25
**Total Questions**: 13
**Difficulty Split**: 3 Easy / 8 Medium / 2 Hard
**Answer Types**: 10 `one` / 3 `many` / 0 `none`

---

# Terraform Associate (004) — Question Bank Iter 5 Batch 5

**Iteration**: 5
**Iteration Style**: Comparison and contrast — distinguish between two similar concepts
**Batch**: 5
**Objective**: 4b — Variables, Outputs, Types & Functions
**Generated**: 2026-04-25
**Total Questions**: 13
**Difficulty Split**: 3 Easy / 8 Medium / 2 Hard
**Answer Types**: 10 `one` / 3 `many` / 0 `none`

---

# Terraform Associate (004) — Question Bank Iter 5 Batch 6

**Iteration**: 5
**Iteration Style**: Comparison and contrast — distinguish between two similar concepts
**Batch**: 6
**Objective**: 4c — Custom Conditions & Sensitive Data
**Generated**: 2026-04-25
**Total Questions**: 13
**Difficulty Split**: 3 Easy / 8 Medium / 2 Hard
**Answer Types**: 10 `one` / 3 `many` / 0 `none`

---

# Terraform Associate (004) — Question Bank Iter 5 Batch 7

**Iteration**: 5
**Iteration Style**: Comparison and contrast — distinguish between two similar concepts
**Batch**: 7
**Objective**: 5 — Terraform Modules
**Generated**: 2026-04-25
**Total Questions**: 13
**Difficulty Split**: 3 Easy / 8 Medium / 2 Hard
**Answer Types**: 10 `one` / 3 `many` / 0 `none`

---

# Terraform Associate (004) — Question Bank Iter 5 Batch 8

**Iteration**: 5
**Iteration Style**: Comparison and contrast — distinguish between two similar concepts
**Batch**: 8
**Objective**: 7 — Maintaining State + 8 — HCP Terraform
**Generated**: 2026-04-25
**Total Questions**: 13
**Difficulty Split**: 3 Easy / 8 Medium / 2 Hard
**Answer Types**: 10 `one` / 3 `many` / 0 `none`

---

---

## Questions

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

**Answer**: B

**Explanation**:
Approach A is **declarative** — it describes *what* should exist, not *how* to create it. Terraform compares this desired state to the current state and decides whether to create, update, or leave the resource unchanged. Approach B is **imperative** — it directly commands AWS to run instances right now, regardless of what already exists. Running Approach B twice would create two instances; running `terraform apply` with Approach A twice would create one instance on the first run and make no changes on the second.

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

**Answer**: B

**Explanation**:
`.tf` configuration files are the human-authored source of truth for **desired state** — they express what the infrastructure *should* look like. The `terraform.tfstate` file tracks **current state** — the real-world attributes of resources Terraform has previously provisioned, refreshed during the last plan or apply. During `terraform plan`, Terraform compares these two to determine the diff. Editing the state file directly is not equivalent to editing configuration files; the state file is not where desired state is expressed.

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

**Answer**: B

**Explanation**:
Terraform's provider plugin model supports 3,000+ providers, enabling a single configuration to manage resources across AWS, Azure, GCP, and other platforms simultaneously. AWS CloudFormation is an AWS service that provisions only AWS resources — it has no native mechanism for managing Azure Key Vault or GCP Cloud Storage. Teams with multi-cloud requirements should evaluate Terraform or similar multi-cloud tools rather than CloudFormation, which is designed specifically for the AWS ecosystem.

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

**Answer**: B

**Explanation**:
In Environment A, the Terraform configuration change is a Git commit with an author, timestamp, message (explaining why), and a reviewable diff of exactly what changed. This is a structured, version-controlled audit trail that satisfies compliance requirements with full context. In Environment B, the change may appear in AWS CloudTrail logs with a caller identity, but there is no version-controlled record of *why* the change was made, no peer review, and no single source of truth in code. IaC provides a richer, more intentional audit trail than ClickOps.

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

**Answer**: C

**Explanation**:
On the first apply, Terraform detects that none of the five desired buckets exist and plans to create all of them. After a successful apply, the state file records all five buckets. On the second apply, Terraform refreshes each bucket's state from the provider API, finds it matches the configuration exactly, and reports "No changes. Your infrastructure matches the configuration." This idempotent behaviour is a defining characteristic of declarative IaC — repeated applies with an unchanged configuration are always safe.

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

**Answer**: B

**Explanation**:
Terraform's primary role is **infrastructure provisioning** — it creates, modifies, and destroys cloud resources such as VMs, VPCs, load balancers, databases, and storage. Ansible's primary role is **configuration management** — once a server is running, Ansible installs packages, manages config files, starts and stops services, and configures the operating system and applications. The two tools are complementary and often used together: Terraform brings up the infrastructure, then Ansible configures the servers it created.

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

**Answer**: B, C

**Explanation**:
AWS CloudFormation is an AWS-native service that provisions only AWS resources — it has no capability to manage Azure or GCP resources. Azure Bicep is a Microsoft-native IaC language that deploys only to Azure via Azure Resource Manager. Both are single-cloud tools. Terraform and Pulumi, by contrast, both support multiple cloud providers through plugin ecosystems, enabling management of AWS, Azure, GCP, and other resources from a single workflow. Pulumi uses general-purpose programming languages (TypeScript, Python, Go) rather than a DSL, but is provider-agnostic.

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

**Answer**: B

**Explanation**:
Terraform maintains a record of desired state (configuration files) and can refresh current state during `terraform plan` by querying the provider API. If the EC2 instance's `instance_type` was changed outside of Terraform, `plan` will show a diff between the desired type and the actual type — drift is made explicit and actionable. Team B has no equivalent mechanism: there is no configuration file to compare against, so the only way to detect the change is manual inspection or a separate monitoring tool. IaC makes drift visible and measurable; ClickOps does not.

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

**Answer**: B

**Explanation**:
IaC's disaster recovery benefit is one of its most tangible advantages. Company A's Terraform configurations are the complete, executable definition of their environment — running `terraform apply` recreates every resource precisely as configured. Company B's engineers must rebuild each component manually, relying on memory, documentation (if it exists and is current), and individual expertise. Manual reconstruction is slow, error-prone, and often produces an environment that differs from the original. IaC enables reliable, repeatable recovery from code.

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

**Answer**: A, B

**Explanation**:
Method X (IaC) produces two key advantages over Method Y (ClickOps). (A) The configuration change is a Git commit with an author, timestamp, and diff — it can be reviewed, reverted, and included in compliance audits. Method Y leaves no record in version control. (B) Because Method X uses code, the change can go through a pull request review before apply, enabling peer oversight. Method Y bypasses any code review or approval process. Option D is incorrect: while Terraform detects the drift during the next plan, it does not silently absorb console changes — it proposes reverting them to match the desired state.

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

**Answer**: C

**Explanation**:
This contrast is the essence of declarative vs imperative. In the declarative model (Option 1), the operator specifies only *what* should exist: "three `t3.micro` EC2 instances." Terraform determines the current state, calculates the diff, and decides the steps. In the imperative model (Option 2), the operator must code all of that logic themselves: query current count, compare to desired, decide to add or remove, handle API calls, deal with errors, and ensure convergence. The declarative approach offloads the how to the tool; the imperative approach keeps it in the operator's script.

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

**Answer**: A, C

**Explanation**:
The two tools cover complementary but non-overlapping primary responsibilities. (A) Terraform's role is infrastructure provisioning: it uses HCL to declare cloud resources and manages their full lifecycle via provider API calls. (C) Ansible's role is configuration management: once Terraform has created a VM, Ansible connects over SSH and configures it — installing packages, managing files, starting services. (B) is incorrect: launching VMs and creating VPCs are provisioning tasks handled by Terraform, not Ansible's primary purpose. (D) is incorrect: Terraform does not have a built-in configuration management agent; `terraform apply` manages cloud API resources, not in-guest software installation.

---

---

## Questions

---

### Question 1 — Official Provider Tier vs Community Provider Tier

**Difficulty**: Easy
**Answer Type**: one
**Topic**: Contrast between who maintains Official providers and who maintains Community providers

**Question**:
Compare the **Official** provider tier and the **Community** provider tier in the Terraform ecosystem. What is the key difference in maintenance and trust level between them?

- A) Official providers are free; Community providers require a paid HashiCorp subscription to use
- B) Official providers are maintained by HashiCorp and carry the highest trust level; Community providers are maintained by individuals or organisations with no HashiCorp review or verification
- C) Official providers are distributed only through the private registry; Community providers are available on the public Terraform Registry
- D) Official providers support all Terraform features; Community providers are limited to data sources only

**Answer**: B

**Explanation**:
The Terraform provider registry uses three tiers. **Official** providers (e.g., `hashicorp/aws`, `hashicorp/azurerm`) are built and maintained directly by HashiCorp — they carry the highest trust level and are held to strict quality and security standards. **Community** providers are contributed by individuals or organisations, receive no formal HashiCorp review, and carry the lowest trust level. A middle **Partner** tier exists for providers maintained by technology companies that have partnered with HashiCorp and undergone some level of review.

---

### Question 2 — `~> 5.0` vs `~> 5.0.0` Version Constraints

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

**Answer**: B

**Explanation**:
The `~>` pessimistic constraint allows updates to the **rightmost non-zero component**. `~> 5.0` (two components) allows the rightmost component (`0`) to increase — meaning any `5.x` is permitted, resulting in `>= 5.0, < 6.0`. `~> 5.0.0` (three components) allows only the patch component to increase — meaning only `5.0.x` is permitted, resulting in `>= 5.0.0, < 5.1.0`. This distinction is heavily tested on the exam.

---

### Question 3 — `.terraform/` Directory vs `.terraform.lock.hcl` in Version Control

**Difficulty**: Easy
**Answer Type**: one
**Topic**: Contrast between the gitignore treatment of the provider cache directory and the lock file

**Question**:
Compare how the `.terraform/` directory and the `.terraform.lock.hcl` file should be treated with respect to a project's version control system. What is the key difference?

- A) Both should be committed to version control — they together ensure reproducible provider installations across the team
- B) Both should be added to `.gitignore` — they are auto-generated by `terraform init` and are too large to commit
- C) `.terraform/` should be committed; `.terraform.lock.hcl` should be gitignored because it changes frequently
- D) `.terraform/` should be gitignored (it is a local provider cache, large and machine-specific); `.terraform.lock.hcl` must be committed (it records exact provider versions and checksums for team-wide consistency)

**Answer**: D

**Explanation**:
`.terraform/` contains the actual downloaded provider binaries and other local state — it is large, machine-specific, and regenerated from the lock file by `terraform init`. It belongs in `.gitignore`. `.terraform.lock.hcl` is a small, text-based file recording the exact provider version and cryptographic hashes installed. Committing it to VCS ensures every team member and CI pipeline installs the same provider versions, making builds reproducible. Without committing the lock file, different engineers may silently install different provider versions.

---

### Question 4 — Provider `source` vs Provider `version` in `required_providers`

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

**Answer**: B

**Explanation**:
`source` identifies the provider's **location** — using the format `<hostname>/<namespace>/<type>` (hostname defaults to `registry.terraform.io` when omitted). It tells Terraform where to find and download the provider binary. `version` constrains **which release of that provider** is acceptable — Terraform will only install a version satisfying the declared constraint. They serve orthogonal purposes: `source` answers "which provider?", `version` answers "which release of that provider?".

---

### Question 5 — `terraform init` vs `terraform init -upgrade`

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Contrast between standard init and upgrade init in terms of when each should be used

**Question**:
Compare `terraform init` and `terraform init -upgrade`. A lock file exists, recording AWS provider `5.10.0` with constraint `~> 5.0`. AWS `5.31.0` is now available. What is the behavioural difference between the two commands?

- A) `terraform init` downloads `5.31.0`; `terraform init -upgrade` installs `5.10.0` as a downgrade safety measure
- B) Both commands install `5.31.0` because it satisfies the constraint — the `-upgrade` flag has no effect when a newer version is available
- C) `terraform init` uses the lock file and installs `5.10.0` (reproducible); `terraform init -upgrade` re-evaluates constraints and installs the newest satisfying version (`5.31.0`), updating the lock file
- D) `terraform init` fails if the lock file is outdated; `-upgrade` is required to resolve the conflict

**Answer**: C

**Explanation**:
`terraform init` respects the existing lock file and installs the pinned version (`5.10.0`), ensuring reproducibility. This is the standard behaviour for day-to-day work where you want consistent provider versions. `terraform init -upgrade` ignores the current lock file entries, re-evaluates all version constraints against the registry, installs the newest version satisfying each constraint, and updates the lock file to record the new versions. Use `-upgrade` only when you intentionally want to adopt a newer provider release.

---

### Question 6 — Default Provider Configuration vs Aliased Provider Configuration

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

**Answer**: B

**Explanation**:
When multiple configurations of the same provider exist, Terraform's assignment rule is clear: any resource **without** a `provider` argument is automatically assigned to the **default (unaliased)** configuration — in this case the `us-east-1` provider. To use the aliased configuration, a resource must **explicitly** declare `provider = aws.west`. This design lets most resources use the default provider while only specific resources explicitly opt in to alternative configurations (e.g., multi-region deployments).

---

### Question 7 — `terraform state mv` vs `terraform state rm`

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Contrast between what state mv and state rm do to the tracked state and the actual cloud resource

**Question**:
Compare `terraform state mv aws_instance.old aws_instance.new` and `terraform state rm aws_instance.web`. What is the key difference in what each command does to the Terraform state and to the actual cloud resource?

- A) `state mv` deletes the cloud resource; `state rm` renames it
- B) Both commands delete the cloud resource but differ in whether they also update the configuration file
- C) `state mv` renames the resource's address in state (the cloud resource is unchanged and remains managed); `state rm` removes the resource from state entirely (the cloud resource is unchanged but Terraform no longer tracks or manages it)
- D) `state mv` and `state rm` are equivalent — both stop Terraform from managing the resource while leaving it in the cloud

**Answer**: C

**Explanation**:
`terraform state mv` is used to **rename** a resource address in state — for example when you rename a resource block in your configuration file. The cloud resource is not touched; Terraform simply updates its internal tracking name. The resource remains under Terraform management. `terraform state rm` **removes** the resource from state entirely — the cloud resource continues to exist, but Terraform no longer has a record of it and will not manage it on future plans or applies. Common use case for `state rm`: releasing a resource from Terraform management without destroying it.

---

### Question 8 — Local State vs Remote State: Safety and Access

**Difficulty**: Medium
**Answer Type**: many
**Topic**: Contrasting local and remote state on concurrent apply safety and team accessibility

**Question**:
Compare local state (`terraform.tfstate` on a local disk) and remote state (e.g., stored in S3 or HCP Terraform). Which TWO statements correctly describe a difference between them with respect to **concurrent apply safety** and **team access**? (Select two.)

- A) Local state provides locking — if two engineers run `terraform apply` simultaneously, Terraform automatically queues the second apply until the first completes
- B) Remote state backends support locking — a lock is acquired at the start of a plan or apply and released on completion, preventing concurrent applies from corrupting state
- C) Local state is stored on the individual engineer's machine — other team members cannot access the current state without manually receiving a copy of the file
- D) Remote state and local state are equivalent in terms of team access — both are equally accessible to any engineer with repository access

**Answer**: B, C

**Explanation**:
(B) Remote state backends that support locking (e.g., S3+DynamoDB, Azure Blob, HCP Terraform) acquire a state lock at the start of operations, preventing simultaneous applies from corrupting state. Local state has no locking mechanism at all — concurrent applies can cause race conditions and state file corruption. (C) Local state lives on the individual engineer's filesystem — team members cannot access it without manually sharing the file, making collaboration difficult and error-prone. Remote state is centrally stored and accessible to all team members and CI pipelines with appropriate permissions.

---

### Question 9 — `terraform state show` vs `terraform show`

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Contrast between the targeted state show command and the full-state show command

**Question**:
Compare `terraform state show aws_instance.web` and `terraform show`. What does each command display, and how do they differ in scope?

- A) `terraform state show aws_instance.web` shows the planned changes for that resource; `terraform show` shows the entire configuration
- B) `terraform state show aws_instance.web` displays all tracked attributes of that single resource from state; `terraform show` displays the entire state (all resources) or the contents of a saved plan file
- C) Both commands are identical — `terraform state show <address>` is just a filtered alias for `terraform show`
- D) `terraform state show` requires a remote backend; `terraform show` works with both local and remote state

**Answer**: B

**Explanation**:
`terraform state show <address>` is a **targeted** command — it queries the state for a single resource address and displays all its tracked attributes (instance ID, IP addresses, tags, etc.). This is useful for inspecting one specific resource. `terraform show` is a **broad** command — without arguments it displays the entire current state file (all managed resources); with a plan file argument (e.g., `terraform show tfplan`), it shows the content of a saved plan. The distinction is scope: one resource vs the whole state or a plan file.

---

### Question 10 — `sensitive = true` on Output vs Encrypting the Remote Backend

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Contrast between terminal display masking and actual state-at-rest encryption

**Question**:
An engineer has a database password stored in Terraform. They declare `sensitive = true` on the output that exposes it. A colleague suggests this is sufficient protection for the password. Compare what `sensitive = true` actually protects vs what an encrypted remote backend protects. Are they correct?

- A) Yes — `sensitive = true` both hides the password in terminal output and encrypts it in the state file, providing complete protection
- B) No — `sensitive = true` only masks the value in terminal output (displaying `(sensitive value)` instead); the password is still stored in **plaintext** in the state file. An encrypted remote backend (e.g., S3 with SSE) protects the state file **at rest** — they address different attack surfaces and both are needed
- C) Yes — Terraform automatically encrypts all `sensitive = true` values in state, so no additional backend encryption is needed
- D) No — `sensitive = true` provides no protection at all; only encrypted remote backends should be used for secrets in Terraform

**Answer**: B

**Explanation**:
`sensitive = true` is a **display-only** protection — it prevents Terraform from printing the value in `plan`, `apply`, and `output` terminal output. It has absolutely no effect on how the value is stored in the state file. All resource attributes — including passwords — are stored in `terraform.tfstate` as **plaintext JSON**, regardless of the `sensitive` flag. An encrypted remote backend (e.g., AWS S3 with server-side encryption, Azure Blob with encryption, HCP Terraform) protects the state file contents at rest on disk. Both are necessary for comprehensive secret protection in production.

---

### Question 11 — Committed Lock File vs No Lock File: Two Team Impact Differences

**Difficulty**: Medium
**Answer Type**: many
**Topic**: Contrasting two specific risks of not committing the lock file vs always committing it

**Question**:
Team A always commits `.terraform.lock.hcl` to their Git repository. Team B adds `.terraform.lock.hcl` to `.gitignore`, treating it as a local-only file. Which TWO statements correctly describe a risk specific to Team B's approach that Team A does not face? (Select two.)

- A) Team B's engineers may install different provider versions on different days as new versions are released, causing subtle, hard-to-reproduce behaviour differences between team members
- B) Team B's CI pipeline cannot run `terraform plan` because the lock file is required to be present during automated runs
- C) Team B cannot verify provider integrity — without the lock file's cryptographic hashes, Terraform cannot confirm that downloaded providers match what was originally installed
- D) Team B can use `terraform init -upgrade` to address this; Team A cannot because their lock file prevents upgrades

**Answer**: A, C

**Explanation**:
(A) Without a shared lock file, each engineer's `terraform init` independently selects the newest version satisfying the constraint. As new provider versions are released, engineers running `terraform init` at different times install different versions — causing subtle behavioural differences that are difficult to diagnose. (C) The lock file's cryptographic hashes (`h1:...`, `zh:...` entries) allow Terraform to verify that downloaded provider binaries match what was originally vetted by the team. Without the lock file, Terraform cannot perform this integrity check — a security concern in environments with strict supply-chain requirements. (D) is incorrect: Team A can still run `terraform init -upgrade` at any time to intentionally update versions.

---

### Question 12 — gRPC Plugin Architecture vs Hypothetical Monolithic Architecture

**Difficulty**: Hard
**Answer Type**: one
**Topic**: Contrast between Terraform's separate-process provider model and a hypothetical built-in provider model

**Question**:
Terraform uses a gRPC-based plugin architecture where each provider runs as a **separate process** from Terraform Core. Compare this to a hypothetical design where all provider code is compiled directly into the Terraform CLI binary. What is the most significant operational advantage the actual gRPC plugin model provides?

- A) gRPC communication is faster than in-process function calls, making provider operations significantly more performant than the monolithic alternative
- B) Providers can be **upgraded independently** of Terraform Core — new AWS provider features can be released and adopted without reinstalling or upgrading the Terraform CLI binary itself; conversely, Terraform Core can be upgraded without requiring all providers to be rebuilt simultaneously
- C) The separate process model is more secure because provider crashes cannot be detected by Terraform Core — failures are silently handled
- D) gRPC enforces stronger schema validation than in-process calls — the monolithic model would allow invalid resource attributes to bypass provider schema checks

**Answer**: B

**Explanation**:
The primary operational advantage of the gRPC plugin architecture is **independent versioning and upgradability**. In the separate-process model, the Terraform CLI binary (Core) and each provider plugin are distinct, versioned artifacts. Teams can upgrade the AWS provider from `5.10.0` to `5.31.0` without changing Terraform Core, and can upgrade Terraform Core without requiring every provider to release a new version simultaneously. In a hypothetical monolithic design, any provider update would require a full rebuild and redistribution of the entire Terraform binary — dramatically slowing the ecosystem's ability to ship provider updates independently.

---

### Question 13 — Three Sources of Truth During `terraform plan`

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

**Answer**: C

**Explanation**:
All three sources play distinct roles. The `.tf` files express **desired state** — what should exist. The `terraform.tfstate` file records **known state** — what Terraform believed to be true after the last successful apply. During `terraform plan`, Terraform **refreshes** known state by querying each resource via the provider API — this updates its view of **actual state** (what really exists now, including any out-of-band changes). Terraform then diffs desired (config) against the refreshed actual state to determine what changes are needed: create, update, or destroy. Running `terraform plan -refresh=false` skips the live API calls and uses the cached state directly, which is faster but may miss drift.

---

---

## Questions

---

### Question 1 — `terraform fmt` vs `terraform validate`: What Each Checks

**Difficulty**: Easy
**Answer Type**: one
**Topic**: Contrast between what `fmt` enforces and what `validate` enforces, and what they share in common

**Question**:
Compare `terraform fmt` and `terraform validate`. What does each command check, and what do they have in common?

- A) `terraform fmt` checks for undeclared variables; `terraform validate` checks for inconsistent indentation — both require cloud provider credentials
- B) `terraform fmt` corrects HCL code style and formatting (indentation, alignment, whitespace); `terraform validate` checks syntax correctness, undeclared references, type errors, and invalid argument names — both are fully offline and require no provider credentials or network access
- C) `terraform fmt` validates that resource arguments match the provider schema; `terraform validate` formats the output of `terraform plan` for readability
- D) Both commands are identical in what they check — `validate` is simply the strict mode of `fmt`

**Answer**: B

**Explanation**:
`terraform fmt` is concerned exclusively with **code style** — it rewrites `.tf` files (or reports differences) to match HashiCorp's canonical formatting conventions: consistent indentation, aligned `=` signs, and normalised whitespace. `terraform validate` is concerned with **logical correctness** — it catches undeclared variable references, invalid resource argument names, type mismatches, and other configuration errors that formatting cannot detect. Crucially, both commands are entirely offline: neither makes any API calls or requires cloud provider credentials, making them safe to run in any environment.

---

### Question 2 — `terraform plan` vs `terraform apply`: State File Impact

**Difficulty**: Easy
**Answer Type**: one
**Topic**: Contrast between which command reads state without modifying it and which modifies state

**Question**:
Compare `terraform plan` and `terraform apply` with respect to how each interacts with the Terraform state file. Which statement correctly describes the difference?

- A) `terraform plan` reads and writes the state file; `terraform apply` writes a new state file and archives the old one
- B) `terraform plan` generates and displays an execution plan without modifying the state file; `terraform apply` executes the plan and updates the state file to reflect the changes made
- C) Both commands modify the state file — `plan` updates it with the proposed changes and `apply` confirms them
- D) Neither command modifies the state file — state is only changed by `terraform state mv` and `terraform state rm`

**Answer**: B

**Explanation**:
`terraform plan` is a **read-only** command with respect to state — it refreshes the current state by querying the provider API, computes the diff between desired and current state, and outputs the proposed changes, but it does not write any changes to the state file. `terraform apply` **writes** to the state file: as each resource is created, updated, or destroyed, the state is updated to record the new real-world attributes. This distinction is important — `plan` is always safe to run repeatedly; `apply` is the operation that causes real changes.

---

### Question 3 — `terraform workspace new` vs `terraform workspace select`

**Difficulty**: Easy
**Answer Type**: one
**Topic**: Contrast between creating a new workspace and selecting an existing one

**Question**:
Compare `terraform workspace new staging` and `terraform workspace select staging`. What is the key functional difference between these two commands?

- A) Both commands are identical — `new` and `select` are aliases for the same operation
- B) `terraform workspace new staging` creates a new workspace named `staging` (it fails if `staging` already exists) and switches to it; `terraform workspace select staging` switches to the existing workspace named `staging` (it fails if `staging` does not yet exist)
- C) `terraform workspace new staging` copies the current workspace's state to `staging`; `terraform workspace select staging` creates an empty new workspace
- D) `terraform workspace new staging` creates the workspace but does not switch to it; `terraform workspace select staging` switches to it without creating it

**Answer**: B

**Explanation**:
`terraform workspace new <name>` creates a brand-new, empty workspace with the given name — if a workspace with that name already exists, the command returns an error. It also automatically switches to the newly created workspace. `terraform workspace select <name>` switches the current context to an already-existing workspace — if no workspace with that name exists, the command returns an error. The two commands are complementary: `new` is for first-time creation; `select` is for switching between existing workspaces.

---

### Question 4 — `terraform apply` with No Saved Plan vs `terraform apply plan.tfplan`

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

**Answer**: B

**Explanation**:
When `terraform apply` is run without a saved plan file, Terraform internally executes a fresh plan at that moment — this ensures it captures the most current state, but it also means the changes applied could differ from what was reviewed if the environment changed in between. When `terraform plan -out=release.tfplan` saves the plan and `terraform apply release.tfplan` applies it, Terraform executes **exactly** the operations captured in the plan file, with no re-evaluation. This is the production best practice: plan, review, then apply the exact saved plan to guarantee what was approved is what runs.

---

### Question 5 — `terraform init` vs `terraform init -reconfigure`

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Contrast between standard backend init and forced backend reconfiguration

**Question**:
A team changes the backend configuration in their `terraform` block from one S3 bucket to a different S3 bucket. They run `terraform init`. Terraform prompts them to choose between migrating state or continuing without migrating. Compare this behaviour to running `terraform init -reconfigure`. What is the operational difference?

- A) `terraform init -reconfigure` migrates all state from the old backend to the new backend automatically; standard `terraform init` requires manual confirmation
- B) `terraform init -reconfigure` initialises the new backend configuration without migrating any existing state and without prompting — the old backend's state is left in place and the new backend starts empty; standard `terraform init` offers the option to migrate state to the new backend
- C) Both commands produce identical behaviour — `-reconfigure` is simply a flag that suppresses the interactive prompt while still migrating state
- D) `-reconfigure` is only valid for the first `terraform init` run; after a backend exists, only standard `terraform init` can be used

**Answer**: B

**Explanation**:
When a backend changes, standard `terraform init` detects the difference and prompts: "Do you want to copy existing state to the new backend?" — offering to migrate state via the equivalent of `terraform init -migrate-state`. `terraform init -reconfigure` takes a different approach: it **forces re-initialisation of the new backend without moving any state**. The old backend retains its state; the new backend starts with an empty state file. This is useful when you intentionally want a fresh state (e.g., starting a new environment) but risks state loss if used accidentally when migration was intended.

---

### Question 6 — `terraform fmt` (No Flags) vs `terraform fmt -diff`

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Contrast between in-place formatting and diff-only preview

**Question**:
Compare running `terraform fmt` with no flags versus `terraform fmt -diff`. A `.tf` file has inconsistent indentation. What happens to the file in each case?

- A) Both commands modify the file — `-diff` additionally shows the changes that were made
- B) `terraform fmt` (no flags) rewrites the file directly on disk to canonical format; `terraform fmt -diff` displays a unified diff showing what would change **without writing any changes to disk**
- C) `terraform fmt` (no flags) only prints the file names that need formatting; `-diff` both shows and applies the changes
- D) Both commands are read-only — to actually reformat a file you must pipe the diff output back to the file manually

**Answer**: B

**Explanation**:
`terraform fmt` without flags is the **action** mode: it reads all `.tf` files, applies canonical formatting, and writes the corrected content back to disk. Files that were already correctly formatted are untouched. `terraform fmt -diff` is the **preview** mode: it computes the same formatting changes but outputs them as a unified diff to stdout without writing anything to disk. This is useful for reviewing what `fmt` would change before applying it. The `-check` flag is a third variant — also read-only, but exits with code 1 rather than displaying a diff.

---

### Question 7 — `terraform plan -refresh=false` vs Standard `terraform plan`

**Difficulty**: Medium
**Answer Type**: many
**Topic**: Contrasting two key differences between a refresh-skipping plan and a full live-query plan

**Question**:
Compare `terraform plan` (standard) with `terraform plan -refresh=false`. Which TWO statements correctly describe a difference between the two? (Select two.)

- A) Standard `terraform plan` queries the live provider API to refresh each resource's actual current attributes before computing the diff; `terraform plan -refresh=false` uses the cached state from the last apply without making any API calls
- B) `terraform plan -refresh=false` is more accurate than standard `terraform plan` because it avoids potential API rate-limiting errors
- C) If an out-of-band change was made to a resource in the cloud (e.g., a tag changed via the console), standard `terraform plan` detects this and includes it in the plan diff; `terraform plan -refresh=false` does not detect the drift because it never queries the live API
- D) Both commands always produce identical plan output — the `-refresh=false` flag only affects performance, not the content of the plan

**Answer**: A, C

**Explanation**:
(A) Standard `terraform plan` begins with a **refresh** phase — it queries the provider API for each managed resource to get its current real-world attributes, updating the in-memory state used for planning. `-refresh=false` skips this phase entirely and uses the state file as-is. (C) As a direct consequence, standard plan detects **drift** (changes made outside Terraform) because it sees the live attribute values; `-refresh=false` misses any drift because it never checks live state. The trade-off is speed vs accuracy: `-refresh=false` is faster in large environments but risks producing an incomplete or incorrect plan if the real infrastructure has drifted from the cached state.

---

### Question 8 — `terraform output` vs `terraform output -json`

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Contrast between human-readable output display and structured JSON output for scripting

**Question**:
Compare `terraform output` (no flags) and `terraform output -json`. A configuration has two outputs: a string `vpc_id` and a list `subnet_ids`. How does the format of each command's response differ, and which is more appropriate for use in a CI script?

- A) Both return identical data — the only difference is that `-json` wraps the output in a JSON array
- B) `terraform output` prints all output values in human-readable format (strings quoted, lists formatted); `terraform output -json` returns a structured JSON object with `sensitive`, `type`, and `value` metadata fields for each output — the JSON format is the appropriate choice for CI scripts and programmatic processing
- C) `terraform output -json` is only valid for outputs declared with `type = "string"` — list outputs require `terraform output` without flags
- D) `terraform output` returns values without quotes for scripting; `-json` adds quotes and type annotations for documentation purposes

**Answer**: B

**Explanation**:
`terraform output` formats values for human consumption — string values are displayed with surrounding double quotes (e.g. `"vpc-0abc123"`), and lists are displayed in a readable multi-line format. It is convenient for quick manual inspection. `terraform output -json` returns a machine-readable JSON document where each output name maps to an object containing the actual `value`, the Terraform `type`, and a `sensitive` boolean. This structured format is the correct choice for CI pipelines, shell scripts, or external tools that need to parse and use output values programmatically, as it avoids quote handling issues and provides type information.

---

### Question 9 — `terraform plan -target` vs Full `terraform plan`

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Contrast between a targeted partial plan and a complete plan covering all resources

**Question**:
A configuration manages 30 resources. An engineer is debugging a single resource and runs `terraform plan -target=aws_instance.debug`. Compare this to running a full `terraform plan` with no target. What risk does the targeted approach introduce that the full plan does not?

- A) Targeted plans are more accurate because fewer resources are evaluated — there is no additional risk
- B) Targeted plans take longer because Terraform must first scan all 30 resources before filtering to the target
- C) A targeted plan only evaluates the specified resource and its direct dependencies — it may miss cascading changes to downstream resources that depend on the target, producing an **incomplete view** that does not reflect all the changes a full apply would cause; a full plan shows the complete picture
- D) Targeted plans lock the state file, preventing other engineers from running plans simultaneously

**Answer**: C

**Explanation**:
`terraform plan -target` is intentionally scoped — it limits Terraform's analysis to the targeted resource and the resources it explicitly depends on. Resources that **depend on** the target (downstream) are not evaluated. This means the plan may not show changes that would propagate through the dependency chain on a full apply. Terraform itself warns: "Note: Objects have changed outside of Terraform" or "This plan was saved to: ... you are responsible for knowing this is incomplete." `-target` is appropriate for emergency fixes or exploratory debugging, but should **not** be used as a normal workflow pattern — full plans give the complete and correct picture.

---

### Question 10 — `terraform destroy` (Full) vs `terraform destroy -target`

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Contrast between full environment destruction and targeted single-resource destruction

**Question**:
A production environment has 50 resources. An engineer needs to destroy only one obsolete EC2 instance (`aws_instance.legacy`). Compare running `terraform destroy` (no flags) versus `terraform destroy -target=aws_instance.legacy`. What is the critical difference in scope?

- A) Both commands destroy the same set of resources — `-target` is only valid with `apply`, not `destroy`
- B) `terraform destroy` (no flags) plans to destroy **all 50 resources** managed by the configuration; `terraform destroy -target=aws_instance.legacy` destroys only the targeted resource (and any resources that depend on it) — the other 49 resources are unaffected
- C) `terraform destroy -target` is not recommended because it deletes the entire resource group containing the target
- D) `terraform destroy` (no flags) only destroys resources in the current workspace; `-target` destroys the resource across all workspaces

**Answer**: B

**Explanation**:
`terraform destroy` without flags is equivalent to `terraform apply -destroy` — it plans the destruction of **every** resource tracked in the current state. Running this accidentally in production would schedule 50 resources for deletion. `terraform destroy -target=aws_instance.legacy` limits the blast radius to only the specified resource and its dependents (if any). This is the safe, surgical approach when you need to remove a single resource without touching the rest of the environment. As with `plan -target`, Terraform warns that the resulting plan is incomplete.

---

### Question 11 — `~` Symbol vs `-/+` Symbol in Plan Output

**Difficulty**: Medium
**Answer Type**: many
**Topic**: Contrasting two key differences between update-in-place and replacement plan operations

**Question**:
Compare the `~` symbol and the `-/+` symbol in `terraform plan` output. Which TWO statements correctly distinguish these two plan operations? (Select two.)

- A) `~` indicates an **update in-place** — the existing resource object continues to exist and only specific attribute values are changed without destroying and recreating the resource
- B) `-/+` indicates that the resource will be **destroyed and then recreated** — a new resource object is provisioned to replace the old one, and the resource experiences downtime during the transition
- C) Both `~` and `-/+` result in the same final state — they differ only in whether Terraform prompts for confirmation
- D) `~` means the resource is being moved to a different Terraform workspace; `-/+` means it is being moved between providers

**Answer**: A, B

**Explanation**:
(A) The `~` prefix signals an **in-place update** — Terraform modifies specific attributes of the existing resource object via the provider API (e.g., updating a tag or resizing a volume) without destroying it. The resource ID stays the same throughout. (B) The `-/+` prefix signals a **replacement** — Terraform destroys the existing resource and creates a brand-new one in its place. This happens when an attribute change cannot be applied in-place (e.g., changing an EC2 instance's AMI or a database's `engine_version`). Replacement operations cause service downtime and result in a new resource ID. Understanding which changes trigger replacement vs in-place update is an important exam skill.

---

### Question 12 — `terraform init -migrate-state` vs `terraform init -reconfigure`

**Difficulty**: Hard
**Answer Type**: one
**Topic**: Deep contrast between migrating state to a new backend vs discarding the old backend's state record

**Question**:
A team is changing their Terraform backend from an S3 bucket in `us-east-1` to a new S3 bucket in `eu-west-1`. Their existing state file contains 40 resources. Compare `terraform init -migrate-state` and `terraform init -reconfigure` for this scenario. What is the critical operational difference?

- A) Both flags copy the state to the new backend — `-reconfigure` additionally cleans up the old backend
- B) `-migrate-state` and `-reconfigure` are equivalent; the distinction only matters when changing backend types, not when changing buckets within the same backend type
- C) `terraform init -migrate-state` copies the existing state from the old S3 bucket to the new S3 bucket before switching the active backend — all 40 resource records are preserved and Terraform continues managing them; `terraform init -reconfigure` initialises the new backend without copying any state — the new backend starts empty, and the 40 resources would appear unmanaged on the next plan
- D) `terraform init -reconfigure` is the recommended approach for cross-region state migration because `-migrate-state` only supports same-region moves

**Answer**: C

**Explanation**:
`terraform init -migrate-state` is the correct flag when you want to **move** your state from one backend to another — it reads the existing state from the current backend, writes it to the new backend, and updates the backend configuration. All 40 resource records transfer to the new location, and Terraform continues managing them seamlessly. `terraform init -reconfigure` initialises the new backend cleanly **without any state migration** — it is appropriate when you intentionally want a fresh state (e.g., setting up a new environment) or when the old state will be managed separately. Using `-reconfigure` when migration was intended would result in a new empty state, and the next `terraform plan` would propose creating all 40 resources again — a dangerous situation in production.

---

### Question 13 — `terraform graph` vs `terraform console`

**Difficulty**: Hard
**Answer Type**: one
**Topic**: Contrast between static dependency graph output and interactive expression evaluation

**Question**:
Compare `terraform graph` and `terraform console` as diagnostic and development tools. What does each command help the operator understand, and how do they differ in their interaction model and output?

- A) Both tools are interactive REPLs — `terraform graph` explores the dependency graph interactively; `terraform console` explores resource attributes interactively
- B) `terraform graph` is used to test HCL expressions before committing them; `terraform console` generates a visual map of resource dependencies
- C) `terraform graph` produces a **one-shot DOT-format text output** of the static resource dependency graph — it shows how resources depend on each other and what ordering Terraform will use for operations; it is non-interactive and requires Graphviz to render visually. `terraform console` is an **interactive REPL** that evaluates HCL expressions and built-in functions against the current configuration and state — it is used to test and debug expressions, functions, and variable references before embedding them in configuration files
- D) Both commands are deprecated — `terraform graph` was replaced by `terraform state list` and `terraform console` was replaced by `terraform validate`

**Answer**: C

**Explanation**:
`terraform graph` and `terraform console` serve completely different purposes and have different interaction models. `terraform graph` is a **batch output tool** — running it produces a DOT language text graph to stdout representing the dependency relationships between all managed resources. It answers "in what order will Terraform create/destroy these resources?" You pipe this output to Graphviz to produce a visual diagram. It is non-interactive and makes no state modifications. `terraform console` is an **interactive REPL** — you type HCL expressions (`format("Hello, %s!", var.name)`, `length(var.subnets)`) and the console evaluates them immediately against the current module's variables and state. It is invaluable for debugging complex expressions and testing function calls before using them in production configuration.

---

---

## Questions

---

### Question 1 — `resource` Block vs `data` Block: Management Model

**Difficulty**: Easy
**Answer Type**: one
**Topic**: Contrast between how Terraform treats a `resource` block and a `data` block

**Question**:
Compare a `resource` block and a `data` block in Terraform. What is the fundamental difference in how Terraform treats each one?

- A) Both blocks create and manage cloud infrastructure — `data` blocks are simply read-only after initial creation
- B) A `resource` block defines infrastructure that Terraform creates, updates, and destroys as part of its state-managed lifecycle; a `data` block queries existing infrastructure in read-only mode — it never creates, modifies, or destroys anything, and the queried object is not tracked as a managed resource in state
- C) `data` blocks are identical to `resource` blocks but execute during `terraform init` rather than `terraform apply`
- D) A `resource` block is used only for compute resources; a `data` block is used for networking and storage resources that already exist

**Answer**: B

**Explanation**:
`resource` blocks define the infrastructure Terraform owns — objects are created on first apply, updated when configuration changes, and destroyed when removed from configuration or when `terraform destroy` is run. These objects are tracked in the state file. `data` blocks perform read-only queries against the provider API to retrieve attributes of objects that exist outside Terraform's management (e.g., a shared VPC ID or the latest AMI). The provider fetches the data, Terraform makes the attributes available in the configuration, but no resource is provisioned and nothing is written to state as a managed object.

---

### Question 2 — `count` vs `for_each`: Iteration Model

**Difficulty**: Easy
**Answer Type**: one
**Topic**: Contrast between numeric `count` iteration and key-based `for_each` iteration

**Question**:
Compare the `count` and `for_each` meta-arguments for creating multiple resource instances. What is the key structural difference between how they identify each instance?

- A) `count` is used for map-based resources; `for_each` is used for list-based resources — they are interchangeable for all other scenarios
- B) `count` creates a fixed number of identical instances identified by a zero-based integer index (`count.index`); `for_each` creates one instance per key in a map or element in a set, with each instance identified by a string key (`each.key`) and accessible value (`each.value`)
- C) `count` supports string keys; `for_each` supports only numeric indexes — they serve opposite roles from what their names suggest
- D) Both meta-arguments use the same `each.key` / `each.value` syntax to reference the current iteration context

**Answer**: B

**Explanation**:
`count` is integer-based — you specify how many copies to create, and each instance is distinguished by `count.index` (0, 1, 2…). This works well for identical or near-identical resources but makes addressing fragile when items are added or removed (indexes shift). `for_each` is key-based — it accepts a `set(string)` or `map`, and each instance is keyed by a stable string identifier. Inside the block, `each.key` refers to the current key and `each.value` refers to the map value for that key. Because keys are stable strings, adding or removing one item from a `for_each` collection does not affect the addresses of other instances.

---

### Question 3 — Implicit Dependency vs `depends_on`

**Difficulty**: Easy
**Answer Type**: one
**Topic**: Contrast between when Terraform auto-detects dependencies and when `depends_on` is required

**Question**:
Compare implicit dependencies and the `depends_on` meta-argument. When does Terraform create an implicit dependency automatically, and when must `depends_on` be used instead?

- A) Implicit dependencies are created when two resources share the same provider; `depends_on` is used when resources are in different providers
- B) Terraform creates an implicit dependency when a resource references an attribute of another resource (e.g., `subnet_id = aws_subnet.public.id`) — no `depends_on` is needed for these; `depends_on` is required only when a dependency exists that Terraform cannot detect through attribute references, such as IAM permissions that must be active before a resource uses them
- C) `depends_on` is always required — Terraform never infers ordering automatically from attribute references
- D) Implicit dependencies are detected through `var.*` references; `depends_on` is used for resource attribute references

**Answer**: B

**Explanation**:
Terraform automatically builds its dependency graph by scanning resource attribute references. When `aws_subnet.public` sets `vpc_id = aws_vpc.main.id`, Terraform sees the reference and guarantees `aws_vpc.main` is created first — no explicit `depends_on` is needed. `depends_on` is reserved for relationships that exist in the real world but cannot be expressed as attribute references — the most common example is an IAM role policy that must be fully propagated before an EC2 instance can use the role. Because the instance doesn't reference any attribute of the policy, Terraform can't detect the dependency; `depends_on` makes it explicit. Overusing `depends_on` reduces parallelism and should be avoided when an attribute reference suffices.

---

### Question 4 — `create_before_destroy = true` vs Default Replacement Order

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

**Answer**: B

**Explanation**:
Terraform's default replacement order is **destroy then create** — the existing resource is removed before the new one is provisioned. For resources that serve live traffic or are referenced by other infrastructure (like a load balancer target group), this creates a gap during which the old resource is gone but the new one doesn't exist yet. Setting `create_before_destroy = true` reverses the order: the new resource is created and confirmed healthy first, then the old one is destroyed. The plan still shows a `-/+` symbol, but the actual execution order is reversed. This is the correct approach for any resource where a downtime window is unacceptable.

---

### Question 5 — `prevent_destroy` vs `ignore_changes`

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Contrast between destruction protection and drift suppression in `lifecycle` blocks

**Question**:
Compare `prevent_destroy = true` and `ignore_changes = [tags]` in a `lifecycle` block. What does each protect against, and in what scenario would you use each?

- A) Both arguments prevent Terraform from making any changes to a resource — they serve the same purpose but one is for destroy operations and the other for update operations
- B) `prevent_destroy = true` causes Terraform to return an error if a plan includes the destruction of that resource — protecting against accidental deletion of critical resources like production databases; `ignore_changes = [tags]` tells Terraform to disregard drift in the listed attributes, so external changes to those attributes (e.g., tags added by an automation tool) do not appear as unwanted changes in future plans
- C) `prevent_destroy` ignores all planned changes; `ignore_changes` only prevents destruction — they are named in the reverse of their actual purpose
- D) `prevent_destroy` applies only during `terraform destroy` operations; it has no effect when a resource is destroyed as part of a replacement during `terraform apply`

**Answer**: B

**Explanation**:
`prevent_destroy = true` is a **destruction guard** — if any plan (whether from `terraform destroy`, a configuration change that implies replacement, or any other scenario) would destroy the protected resource, Terraform aborts with an error. It is commonly applied to production databases, DNS zones, and other resources where accidental deletion would cause data loss. `ignore_changes` is a **drift suppression** tool — it tells Terraform to accept that certain attribute values may be changed outside Terraform (e.g., by Auto Scaling groups, tagging automations, or other tools) and to not flag those changes as configuration drift. Removing or updating ignored attributes from the Terraform config won't trigger an update. The two serve orthogonal purposes: one guards deletion; the other suppresses noise from known external changes.

---

### Question 6 — `count` Instance Address vs `for_each` Instance Address

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Contrast between the bracket notation used for `count` instances and `for_each` instances

**Question**:
A configuration has two resources that create three web instances — one using `count = 3` and one using `for_each = toset(["us-east-1", "eu-west-1", "ap-southeast-1"])`. How does the state address format differ between these two approaches?

- A) Both use numeric indexes — `aws_instance.web[0]`, `aws_instance.web[1]`, etc.
- B) `count` instances are addressed with zero-based integer indexes (e.g., `aws_instance.web[0]`, `aws_instance.web[1]`, `aws_instance.web[2]`); `for_each` instances are addressed using their string key (e.g., `aws_instance.web["us-east-1"]`, `aws_instance.web["eu-west-1"]`)
- C) Both use string keys — `count` generates keys from `count.index` converted to a string
- D) `for_each` instances are addressed with integer indexes; `count` instances use string keys derived from each resource's `id` attribute

**Answer**: B

**Explanation**:
The state address format directly reflects the iteration mechanism used. `count` instances are identified by their zero-based integer index in square brackets — removing `aws_instance.web[1]` from a `count = 3` collection shifts `aws_instance.web[2]` to `aws_instance.web[1]`, which Terraform treats as a deletion and recreation. `for_each` instances are addressed by their string key from the set or map — `aws_instance.web["us-east-1"]` is a stable address that doesn't shift when other entries are added or removed. This stability of `for_each` addresses is a primary reason it is preferred over `count` for heterogeneous resource collections.

---

### Question 7 — `moved` Block vs `terraform state mv`

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Contrast between the HCL-based `moved` block and the CLI `state mv` command for renaming resources

**Question**:
A team needs to rename a resource in their Terraform configuration from `aws_instance.server` to `aws_instance.api`. Compare using a `moved` block in configuration versus running `terraform state mv aws_instance.server aws_instance.api`. What is the key operational difference?

- A) Both approaches are identical in effect — the `moved` block is simply the newer syntax for `terraform state mv`
- B) A `moved` block is declared in HCL and processed during `terraform plan`/`apply` — it is version-controlled alongside the configuration, can be reviewed in pull requests, and is executed automatically for all team members on their next apply; `terraform state mv` is an imperative CLI command that manipulates the state file directly and immediately, bypassing the plan/apply workflow — the change takes effect for whoever runs the command but is not tracked in configuration
- C) `terraform state mv` is preferred because it provides rollback capabilities; the `moved` block permanently alters the state with no way to revert
- D) `moved` blocks can only rename resources within a module; `terraform state mv` is required for root module renames

**Answer**: B

**Explanation**:
The core difference is **declarative vs imperative**. A `moved` block is HCL — it is committed to version control, reviewed like any configuration change, and applied as part of the normal plan/apply workflow. Every team member who runs `terraform plan` will see the rename operation and can apply it safely. `terraform state mv` is a direct state manipulation command — it modifies the state file immediately without a plan and is typically not tracked in version control. It is useful for one-off manual fixes or emergency corrections but lacks the auditability and team coordination of the `moved` block approach. The `moved` block was introduced in Terraform 1.1 as the preferred declarative approach to state refactoring.

---

### Question 8 — `removed` Block (`destroy = false`) vs `terraform state rm`

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

**Answer**: B

**Explanation**:
Both approaches achieve the same end result — the resource is removed from Terraform's state and Terraform stops managing it, leaving the AWS resource intact. The distinction is process: the `removed` block (introduced in Terraform 1.7) is a declarative HCL approach that is version-controlled, visible in the plan output, and applied consistently across the team. `terraform state rm` is a direct CLI state manipulation — it removes the entry immediately, making no API calls. It is not tracked in configuration and leaves no record of the decision in the codebase. For team environments and auditability, the `removed` block is the preferred approach.

---

### Question 9 — `ignore_changes = [specific_attrs]` vs `ignore_changes = all`

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Contrast between targeted drift suppression and complete drift suppression

**Question**:
Compare `ignore_changes = [tags, user_data]` with `ignore_changes = all` in a `lifecycle` block. What is the key operational risk difference between these two forms?

- A) Both forms are equivalent — listing attributes is just a more verbose way of writing `all`
- B) `ignore_changes = [tags, user_data]` suppresses drift only for the explicitly listed attributes — changes to any unlisted attribute (e.g., `instance_type`) are still detected and shown in plan; `ignore_changes = all` suppresses drift detection for **every** attribute of the resource, meaning configuration changes to any argument will silently have no effect in future plans — this can cause Terraform to diverge permanently from the actual state of the resource
- C) `ignore_changes = all` is the safer option because it ensures no unintentional changes are applied to the resource
- D) `ignore_changes = [tags, user_data]` causes Terraform to import those attributes from the live resource on every plan; `ignore_changes = all` skips the refresh phase for the resource entirely

**Answer**: B

**Explanation**:
`ignore_changes` with a specific list is a **surgical** suppression — only the named attributes are excluded from drift detection. If an engineer changes `instance_type` in the Terraform config, that change is still detected and applied. `ignore_changes = all` is a **blanket** suppression — it tells Terraform to never report or apply any configuration changes to the resource after it is initially created. This is occasionally appropriate for resources where all attributes are externally managed after creation, but it carries significant risk: if a configuration change is made (e.g., to `security_groups`), Terraform will silently ignore it, and the actual resource will never reflect the intent of the configuration. The targeted form is strongly preferred; `all` should only be used when explicitly intended.

---

### Question 10 — Data Source Read at Plan vs Data Source Read at Apply

**Difficulty**: Medium
**Answer Type**: many
**Topic**: Contrasting TWO scenarios that determine whether a data source is read during plan or deferred to apply

**Question**:
Compare when a data source is read during the `plan` phase versus when it is deferred to the `apply` phase. Which TWO statements correctly describe this difference? (Select two.)

- A) A data source whose filter arguments are all known static values or already-resolved references is read during `terraform plan` — the result is available in the plan output
- B) All data sources are always read during `terraform apply`, never during `terraform plan`
- C) A data source whose filter arguments depend on a value that is only known after another resource is created (e.g., filtering by the ID of a resource being created in the same apply) is deferred and read during `terraform apply` after its dependency is provisioned
- D) Data sources are read during `terraform init` — neither `plan` nor `apply` triggers data source queries

**Answer**: A, C

**Explanation**:
(A) When a data source's arguments are fully resolved — either static values like `owners = ["099720109477"]` or references to already-existing resources — Terraform reads it during the `plan` phase. The resolved value appears in the plan output, giving the operator visibility into what the data source returns. (C) When a data source's arguments depend on a computed value that doesn't exist yet (e.g., filtering by the ID of an `aws_vpc` that is being created in the same `terraform apply`), Terraform cannot query the data source during plan because the input doesn't exist. In this case, the data source read is deferred to the apply phase, after the dependency is created and its attributes are known. The plan output shows the data source result as `(known after apply)`.

---

### Question 11 — `replace_triggered_by` vs `depends_on`

**Difficulty**: Medium
**Answer Type**: many
**Topic**: Contrasting TWO key differences between the `replace_triggered_by` lifecycle argument and the `depends_on` meta-argument

**Question**:
Compare `replace_triggered_by` in a `lifecycle` block with the `depends_on` meta-argument. Which TWO statements correctly describe a difference between these two? (Select two.)

- A) `depends_on` controls **execution ordering** — it ensures one resource is fully created before another begins, but it does not force any resource to be destroyed or recreated; `replace_triggered_by` forces the resource to be **destroyed and recreated** when a referenced resource or attribute changes
- B) Both `replace_triggered_by` and `depends_on` are interchangeable — they differ only in syntax
- C) `replace_triggered_by` creates a dependency that also acts as a **replacement trigger** — when the referenced resource changes, the resource with `replace_triggered_by` is scheduled for replacement in the next plan; `depends_on` only controls ordering and never triggers replacement
- D) `depends_on` causes a replacement; `replace_triggered_by` only controls creation order

**Answer**: A, C

**Explanation**:
(A and C together capture the complete contrast.) `depends_on` is an **ordering constraint** — it tells Terraform "resource B cannot be created until resource A is complete" but has no opinion on what happens to resource B when resource A changes in the future. `replace_triggered_by` is a **change-reactive replacement trigger** — it establishes both an ordering dependency and a rule that says "whenever the referenced resource or attribute changes, force this resource to be replaced." A common use case is coupling an `aws_autoscaling_group` to its `aws_launch_template` — when the launch template is updated, `replace_triggered_by` ensures the ASG is replaced with the new template, even if no ASG configuration attribute itself changed.

---

### Question 12 — `count` vs `for_each`: Accepted Input Types and Mutual Exclusivity

**Difficulty**: Hard
**Answer Type**: many
**Topic**: Contrasting TWO technical constraints that differ between `count` and `for_each`

**Question**:
Compare `count` and `for_each` on two specific technical constraints. Which TWO statements are correct? (Select two.)

- A) `count` accepts any non-negative integer value; `for_each` accepts a `map` or a `set(string)` — it does NOT accept a plain `list(string)` without first converting it with `toset()`
- B) `for_each` accepts a plain `list(string)` directly — no type conversion is needed
- C) `count` and `for_each` are mutually exclusive — a single resource block cannot use both simultaneously; attempting to do so causes a Terraform validation error
- D) `count` and `for_each` can be combined on a single resource — `count` controls the number of copies and `for_each` assigns a key to each

**Answer**: A, C

**Explanation**:
(A) `for_each` is strict about input types — it accepts a `map(any)` or a `set(string)`, but not a raw `list`. Lists have ordered integer indexes and can contain duplicates, which conflicts with `for_each`'s requirement for unique stable keys. To use a list as a `for_each` input, convert it first: `for_each = toset(var.regions)`. `count` simply takes a non-negative integer. (C) The two meta-arguments are **mutually exclusive** — combining `count` and `for_each` on the same resource block is a validation error. Terraform allows only one instance-creation mechanism per resource. Attempting to use both causes `terraform validate` to fail with an error indicating that only one of `count` or `for_each` may be defined.

---

### Question 13 — `create_before_destroy` vs `replace_triggered_by`: Two Lifecycle Mechanisms Affecting Replacement

**Difficulty**: Hard
**Answer Type**: one
**Topic**: Deep contrast between the two `lifecycle` arguments that both involve resource replacement but serve different purposes

**Question**:
Both `create_before_destroy = true` and `replace_triggered_by = [...]` involve resource replacement in Terraform. Compare them — what distinct problem does each solve, and can they be used together?

- A) They are synonyms — `replace_triggered_by` is the newer name for `create_before_destroy` introduced in Terraform 1.2+
- B) `create_before_destroy = true` controls **when in the replacement sequence** the new resource is provisioned relative to the old one (create-first vs destroy-first) — it does not change what triggers a replacement; `replace_triggered_by = [...]` controls **what events trigger a replacement** — it causes the resource to be replaced when a referenced resource or attribute changes, even if the resource's own configuration hasn't changed; the two are orthogonal and can be combined to get both a triggered replacement and a safe create-before-destroy sequence
- C) `replace_triggered_by` overrides `create_before_destroy` — if both are set, Terraform uses destroy-first ordering regardless
- D) `create_before_destroy` triggers replacements proactively; `replace_triggered_by` only changes the sequencing of a replacement that was already planned for other reasons

**Answer**: B

**Explanation**:
The two lifecycle arguments address completely different dimensions of replacement: **sequencing** vs **triggering**. `create_before_destroy = true` answers the question "in what order do the destroy and create happen?" — it reverses the default destroy-first sequence to create-first, minimising downtime during any replacement regardless of what caused it. `replace_triggered_by = [aws_launch_template.web]` answers the question "what changes should cause this resource to be replaced?" — it adds a dependency-based replacement trigger so that when the referenced resource changes, the current resource is also scheduled for replacement, even if no attribute of the current resource's configuration has changed. Because they control different aspects of replacement, they are orthogonal: a resource can use both to ensure that replacements triggered by upstream changes are also performed in a zero-downtime create-before-destroy order.

---

---

## Questions

---

### Question 1 — `var.*` vs `local.*`: External Input vs Internal Computed Value

**Difficulty**: Easy
**Answer Type**: one
**Topic**: Contrast between input variables and local values in purpose, scope, and mutability

**Question**:
Compare an input variable (`var.*`) and a local value (`local.*`) in Terraform. What is the fundamental difference between the two?

- A) Input variables and locals are interchangeable — locals are simply a shorthand for variables that have a default value
- B) An input variable (`var.*`) is an externally supplied value — it can be set by a caller via CLI flags, `.tfvars` files, or environment variables, and it forms part of the module's interface; a local value (`local.*`) is an internally computed value — it is calculated from other values within the module, cannot be set by callers, and is not part of the module's external interface
- C) Local values can be set from outside the module via `TF_LOCAL_*` environment variables; input variables cannot be overridden at runtime
- D) Input variables can reference resource attribute values in their `default` argument; locals cannot reference resource attributes

**Answer**: B

**Explanation**:
The core distinction is **who controls the value**. Input variables are the module's public interface — callers (or operators) supply their values through `.tfvars` files, CLI flags, environment variables, or module `var =` arguments. Locals are private — they are computed inside the module and cannot be set from outside. A local can reference variables, resource attributes, data sources, and other locals; an input variable's `default` is restricted to static values (it cannot reference resources or data sources). When designing a module, you expose variables for things callers need to customise and use locals for intermediate values that simplify expressions internally.

---

### Question 2 — Variable with `default` vs Required Variable

**Difficulty**: Easy
**Answer Type**: one
**Topic**: Contrast between optional variables (with default) and required variables (no default)

**Question**:
Compare a variable block that includes a `default` argument with one that omits it. What is the operational difference during `terraform apply`?

- A) Variables without a `default` are always invalid — Terraform requires a default on every variable
- B) A variable with a `default` is optional — if no value is provided through any input mechanism, Terraform uses the default and does not prompt the operator; a variable without a `default` is required — Terraform will interactively prompt the operator for a value if none is provided, or fail if running non-interactively without one
- C) Variables with `default` are evaluated at `terraform init`; variables without `default` are evaluated at `terraform apply`
- D) A variable without a `default` causes Terraform to use `null` if no value is supplied — there is no interactive prompt

**Answer**: B

**Explanation**:
The `default` argument determines whether a variable is optional or required. With a `default`, Terraform falls back to that value when no other input mechanism provides one — the operator is never prompted. Without a `default`, Terraform treats the variable as required. In an interactive terminal, Terraform will prompt the operator to type a value. In a non-interactive environment (CI/CD pipeline, automated apply), the absence of a value causes Terraform to fail with an error — it does not use `null` as an implicit default. This makes the `default` argument the mechanism for making variables optional.

---

### Question 3 — `list(string)` vs `set(string)`: Ordering and Uniqueness

**Difficulty**: Easy
**Answer Type**: one
**Topic**: Contrast between the `list` and `set` collection types in Terraform

**Question**:
Compare the `list(string)` and `set(string)` types in Terraform. What are the two key differences between them?

- A) `list(string)` is unordered and unique; `set(string)` is ordered and allows duplicates — they are opposites of their intuitive names
- B) A `list(string)` is ordered (elements have a defined position accessible by index) and allows duplicate values; a `set(string)` is unordered (no guaranteed element order) and enforces uniqueness — duplicate values are silently removed when a list is converted to a set
- C) Both types are ordered and unique — the only difference is that `set(string)` can hold mixed types
- D) `list(string)` and `set(string)` are interchangeable — Terraform accepts either type wherever a collection of strings is expected

**Answer**: B

**Explanation**:
`list(string)` preserves insertion order and permits duplicate values — elements are accessible by their zero-based index (e.g., `var.names[0]`). `set(string)` has no defined order and automatically removes duplicates — you cannot access set elements by index. This distinction matters practically: `for_each` does not accept a raw `list` (because lists can have duplicates, which conflict with the requirement for unique instance keys), so `toset(var.regions)` is used to convert a list to a set before passing it to `for_each`. Understanding which type a function or meta-argument expects is important for avoiding type errors.

---

### Question 4 — `terraform.tfvars` vs `*.auto.tfvars`: Auto-Loading Mechanics

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Contrast between the two automatically loaded variable file mechanisms and their precedence relationship

**Question**:
Compare `terraform.tfvars` and files matching `*.auto.tfvars` (e.g., `prod.auto.tfvars`). What are the two key differences between them?

- A) `terraform.tfvars` is automatically loaded; `*.auto.tfvars` files must be specified explicitly with `-var-file` — they are not auto-loaded
- B) `terraform.tfvars` is a single fixed filename that Terraform auto-loads; `*.auto.tfvars` is a naming pattern — any file ending in `.auto.tfvars` is auto-loaded automatically; additionally, values in `*.auto.tfvars` files have **higher precedence** than `terraform.tfvars`, so `prod.auto.tfvars` overrides the same variable set in `terraform.tfvars`
- C) Both are identical in mechanics and precedence — the `.auto.` in the filename has no special meaning to Terraform
- D) `*.auto.tfvars` has lower precedence than `terraform.tfvars` because it uses a wildcard pattern rather than a fixed filename

**Answer**: B

**Explanation**:
Both file types are automatically loaded without requiring a `-var-file` flag, but they differ in two ways. First, **naming**: `terraform.tfvars` is a single specific filename that Terraform always looks for; `*.auto.tfvars` is a pattern — any file whose name ends in `.auto.tfvars` (e.g., `network.auto.tfvars`, `prod.auto.tfvars`) is auto-loaded, allowing teams to organise variables across multiple files. Second, **precedence**: `*.auto.tfvars` files have higher precedence than `terraform.tfvars`. If `terraform.tfvars` sets `region = "us-east-1"` and `prod.auto.tfvars` sets `region = "eu-west-1"`, the value from `prod.auto.tfvars` wins. Multiple `.auto.tfvars` files are processed in lexical (alphabetical) order, with later files winning over earlier ones.

---

### Question 5 — `output` Block vs `local` Value: Cross-Module vs Intra-Module

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Contrast between the purpose of output values and local values in module composition

**Question**:
Compare an `output` block and a `locals` block value. What is the key difference in where each value is accessible?

- A) Both `output` blocks and `local` values are accessible by the parent module — `locals` are simply the private variant of outputs
- B) A `local` value is scoped to the module in which it is defined and cannot be accessed by any caller — it is an internal computed value for reducing repetition within one module; an `output` value is the module's public interface — it exposes a value to the parent module (via `module.<name>.<output>`) or to the operator after apply (via `terraform output`)
- C) `output` values are only accessible during `terraform plan`; `local` values persist and are accessible during `terraform apply`
- D) Both `output` and `local` values can be accessed cross-module; `output` values are simply re-exported locals with no functional difference

**Answer**: B

**Explanation**:
`locals` are private to the module — they are purely an internal DRY mechanism. No caller can reference `local.common_tags` from outside the module. `output` blocks are the module's export interface — a parent module consuming a child module accesses its outputs via `module.<name>.<output_name>`, and a root module's outputs are displayed after `terraform apply` and queryable with `terraform output`. When a child module computes a subnet ID that a parent module needs to assign to an EC2 instance, the subnet ID must be declared as an `output` in the child. If the subnet ID is only needed inside the child module itself, a `local` is sufficient.

---

### Question 6 — `map(string)` vs `object({...})`: Homogeneous vs Heterogeneous Attributes

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Contrast between the flexible but homogeneous `map` type and the structured but heterogeneous `object` type

**Question**:
Compare the `map(string)` type and the `object({ name = string, port = number })` type. What is the key structural difference between them?

- A) `map(string)` requires a fixed set of declared keys; `object({...})` allows any key to be added at runtime
- B) A `map(string)` is homogeneous — all values must be the same type (string in this case), but any key can be present and new keys can be added without changing the type definition; an `object({...})` is heterogeneous — each named attribute has its own individually declared type, the set of allowed attributes is fixed by the declaration, and different attributes can hold different types (e.g., `name` is a string while `port` is a number)
- C) Both types are identical — `map(string)` is simply shorthand for `object({})` with all string values
- D) `object({...})` accepts only string values for all attributes; `map(string)` allows values of any type

**Answer**: B

**Explanation**:
`map(string)` is a **homogeneous** collection — every value must be a string, but the set of keys is open-ended. You can add new keys to a `map(string)` variable without changing its type constraint. `object({name=string, port=number})` is a **heterogeneous** structured type — each declared attribute has its own type constraint, and only the declared attributes are valid (the schema is closed). This means `port` can be a number while `name` is a string — impossible in a `map(string)`. Choose `map(string)` when managing a variable-length collection of uniform values (e.g., resource tags); choose `object({...})` when modeling a structured configuration with named fields of specific types.

---

### Question 7 — `lookup()` vs Direct Map Indexing `map["key"]`

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Contrast between safe key lookup with a default and direct bracket indexing on error behaviour

**Question**:
Compare `lookup(var.ami_ids, "us-west-2", "ami-default")` with `var.ami_ids["us-west-2"]`. What is the key difference in behaviour when the key `"us-west-2"` does not exist in the map?

- A) Both expressions throw a Terraform error if the key does not exist — `lookup()` provides no additional safety
- B) `lookup(var.ami_ids, "us-west-2", "ami-default")` returns the third argument (`"ami-default"`) when the key is absent — no error is raised; `var.ami_ids["us-west-2"]` causes a Terraform error at plan or apply time if the key does not exist in the map
- C) `var.ami_ids["us-west-2"]` silently returns `null` when the key is absent; `lookup()` returns an error
- D) Both expressions return `null` for missing keys — the difference is only in syntax style

**Answer**: B

**Explanation**:
`lookup(map, key, default)` is a **safe accessor** — its third argument is a fallback value returned when the specified key is not present in the map. This is useful for optional per-region or per-environment configuration where not every key may exist. Direct bracket indexing (`map["key"]`) is an **unsafe accessor** — if the key doesn't exist, Terraform raises a runtime error. Use `lookup()` when absence of a key is a valid and expected situation that should gracefully fall back to a default value; use direct indexing when the key is guaranteed to exist and an error on absence is the correct behaviour.

---

### Question 8 — `concat()` vs `flatten()`: Combining Lists vs Removing Nesting

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Contrast between joining multiple flat lists and flattening a single nested list structure

**Question**:
Compare `concat(list_a, list_b)` and `flatten([list_a, [list_b, list_c]])`. What problem does each function solve, and when would you choose one over the other?

- A) Both functions are identical — `flatten` simply uses different syntax to call the same underlying list-joining operation as `concat`
- B) `concat(list_a, list_b)` takes two or more already-flat lists as separate arguments and joins them into a single flat list; `flatten([list_a, [list_b, list_c]])` takes a single argument that is a list potentially containing nested sublists and recursively removes the nesting — use `concat` when joining known flat collections, and `flatten` when the input may contain lists nested within lists (e.g., a `for` expression that produces a list of lists)
- C) `concat` is for joining strings; `flatten` is for joining lists — they operate on different types
- D) `flatten` only removes one level of nesting; `concat` is required for deeply nested structures

**Answer**: B

**Explanation**:
`concat(a, b, c)` is a variadic function — it accepts multiple flat list arguments and joins them in order. It does not handle nesting: `concat(["a"], [["b", "c"]])` would produce `["a", ["b", "c"]]` — the inner list remains nested. `flatten` is designed specifically to **remove nesting** from a list that contains sublists. It recursively flattens all levels, so `flatten([["a"], [["b", "c"]]])` produces `["a", "b", "c"]`. A common real-world use case for `flatten` is in `for` expressions over modules or `for_each` resources that each return a list of objects — the result is a list of lists that needs flattening before being used in a subsequent `for_each`.

---

### Question 9 — `coalesce()` vs `try()`: Two Different Fallback Mechanisms

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Contrast between null/empty-string fallback and expression-error fallback

**Question**:
Compare `coalesce(var.region, var.fallback_region, "us-east-1")` and `try(var.config["region"], "us-east-1")`. What kind of fallback does each function provide?

- A) Both functions are interchangeable — they both return the first non-null value from their arguments
- B) `coalesce()` returns the first argument in its list that is neither `null` nor an empty string — it evaluates all arguments and returns the first one with a meaningful value; `try()` evaluates its first expression and returns the fallback only if the expression itself produces a **runtime error** — it does not treat `null` or empty string as a failure condition
- C) `try()` returns the first non-null value; `coalesce()` suppresses errors from invalid expressions
- D) `coalesce()` is for numeric fallbacks only; `try()` is for string fallbacks only

**Answer**: B

**Explanation**:
`coalesce(a, b, c)` is a **null/empty-string filter** — it scans its arguments in order and returns the first one that is not `null` and not an empty string `""`. It is used for optional configuration values where several inputs might be null and you want the first meaningful one. `try(expr, fallback)` is an **error suppressor** — it evaluates its first argument and, if that expression would throw a runtime error (e.g., accessing a map key that doesn't exist, or calling a function with an invalid input), it returns the fallback instead. If the first expression succeeds, `try()` returns its result regardless of whether the value is `null`. Use `coalesce()` for optional values with ordered defaults; use `try()` for defensive access to values that may not exist in a data structure.

---

### Question 10 — `[for ...]` vs `{for ...}`: List vs Map Output from `for` Expressions

**Difficulty**: Medium
**Answer Type**: many
**Topic**: Contrasting TWO key differences between list-producing and map-producing `for` expressions

**Question**:
Compare `[for n in var.names : upper(n)]` and `{for n in var.names : n => upper(n)}`. Which TWO statements correctly describe a difference between these two forms? (Select two.)

- A) The `[for ...]` form with square brackets produces a **list** — elements are ordered and accessible by zero-based index; the `{for ...}` form with curly braces and `=>` produces a **map** — elements are accessible by their declared key
- B) Both forms always produce a list — the curly braces in `{for ...}` are purely cosmetic and have no effect on the output type
- C) The map form `{for ...}` requires that the key expression (left side of `=>`) produce a unique value for each iteration — duplicate keys cause a Terraform error; the list form `[for ...]` has no such uniqueness requirement
- D) The list form `[for ...]` requires specifying both a key and a value separated by `=>`; the map form only specifies a single transform expression

**Answer**: A, C

**Explanation**:
(A) The outer delimiter is what determines the output type — this is one of the most practically important distinctions in Terraform expressions. Square brackets produce a list; curly braces with `=>` produce a map. The downstream consumer of the value must receive the correct type (e.g., a `for_each` that expects a map would error if given a list). (C) The map form has a uniqueness constraint on keys — because a map cannot have duplicate keys, if the key expression produces the same value for two different iterations, Terraform raises an error. The list form has no such restriction — the same transformed value can appear multiple times in the resulting list. This is an important consideration when the input collection may have repeated values.

---

### Question 11 — `sensitive = true` on a Variable vs `sensitive = true` on an Output

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Contrast between how sensitive masking behaves differently for variables and outputs

**Question**:
Both input variables and output blocks support `sensitive = true`. What is a key difference in how the masking behaviour works for each?

- A) They are identical in every respect — `sensitive = true` on a variable and on an output both produce exactly the same masking behaviour in every context
- B) `sensitive = true` on an **input variable** hides the value in plan and apply terminal output for any expression that uses the variable; `sensitive = true` on an **output** hides the value in the `terraform apply` summary and in the general `terraform output` listing — however, querying a sensitive output directly by name (`terraform output db_password`) or using `terraform output -json` reveals the plaintext value, making direct name-based queries an intentional escape hatch
- C) `sensitive = true` on an output permanently encrypts the value so it can never be retrieved; sensitive variables are only masked in the terminal but remain retrievable
- D) Sensitive output values are excluded from the state file; sensitive variable values are not

**Answer**: B

**Explanation**:
Both settings suppress values in terminal output during plan and apply, but their behaviour diverges when outputs are accessed directly. A sensitive input variable's value is redacted wherever it appears in plan/apply output — the masking follows the value as it propagates through the configuration. A sensitive output is shown as `(sensitive value)` in the general `terraform output` listing (all outputs) and in the apply summary — this prevents accidental exposure in logs. However, `terraform output db_password` (querying by specific name) and `terraform output -json` both intentionally return the plaintext value, because the operator is explicitly requesting that value and is assumed to have authorised access. Neither setting encrypts the state file — sensitive values are still stored in plaintext in `terraform.tfstate`.

---

### Question 12 — `tuple` vs `list`: Fixed Mixed-Type vs Variable Homogeneous

**Difficulty**: Hard
**Answer Type**: many
**Topic**: Contrasting TWO structural differences between the `tuple` type and the `list` type

**Question**:
Compare the `tuple([string, number, bool])` type and the `list(string)` type. Which TWO statements correctly describe a structural difference between them? (Select two.)

- A) A `tuple` has a **fixed length** — the number of elements is defined in the type declaration and cannot change; a `list` has a **variable length** — elements can be added or removed without changing the type definition
- B) A `tuple` and a `list` both enforce that all elements are the same type — the only difference is that `tuple` also enforces element count
- C) A `tuple` allows **different types at different positions** — e.g., `tuple([string, number, bool])` holds a string at position 0, a number at position 1, and a bool at position 2; a `list` requires **all elements to be the same type** — a `list(string)` can only hold strings at every position
- D) A `list` type allows mixed element types by default; a `tuple` restricts all elements to the same type declared in its definition

**Answer**: A, C

**Explanation**:
(A) Tuples are fixed-length — the type declaration specifies exactly how many elements exist and in what order. A `tuple([string, number, bool])` always has exactly three elements. Lists are variable-length — you can have zero, one, or many elements and the list type does not encode a count. (C) Tuples are per-position typed — element 0 is a string, element 1 is a number, element 2 is a bool; each position can hold a different type. Lists are uniformly typed — every element of a `list(string)` must be a string; you cannot mix strings and numbers. Together, tuples combine the per-position typing of objects with the ordered numeric indexing of lists, making them useful for representing structured records accessed by index rather than by name.

---

### Question 13 — Variable Precedence: Specific Ordering Contrasts

**Difficulty**: Hard
**Answer Type**: many
**Topic**: Contrasting TWO specific precedence relationships in Terraform's variable input chain

**Question**:
Terraform resolves variable values from multiple sources using a defined precedence order. Which TWO statements correctly describe specific precedence relationships in that chain? (Select two.)

- A) `TF_VAR_*` environment variables have **higher** precedence than `*.auto.tfvars` files — if both set the same variable, the environment variable value is used
- B) `*.auto.tfvars` files have **higher** precedence than `terraform.tfvars` — if both set the same variable, the value from the `.auto.tfvars` file wins
- C) `terraform.tfvars` has **higher** precedence than `TF_VAR_*` environment variables — if both set the same variable, the `terraform.tfvars` value is used
- D) The `default` value in a variable block has **higher** precedence than `terraform.tfvars` — if both are present, the default is used

**Answer**: A, B

**Explanation**:
(A) The full precedence order from highest to lowest is: CLI `-var` flag → `TF_VAR_*` environment variables → `*.auto.tfvars` files → `terraform.tfvars` → `-var-file` flag → `default`. `TF_VAR_*` sits above `*.auto.tfvars`, so an environment variable overrides any auto-loaded file. (B) `*.auto.tfvars` files sit above `terraform.tfvars` in the precedence chain, so `prod.auto.tfvars` overrides a value set in `terraform.tfvars`. (C) is incorrect — `TF_VAR_*` is higher than `terraform.tfvars`, not the other way around. (D) is incorrect — the `default` is the **lowest** precedence fallback; any other input source overrides it.

---

---

## Questions

---

### Question 1 — `validation` Block vs `precondition`: When Each Runs

**Difficulty**: Easy
**Answer Type**: one
**Topic**: Contrast between the timing and triggering point of variable validation and lifecycle preconditions

**Question**:
Compare a `validation` block inside a `variable` declaration with a `precondition` block inside a resource's `lifecycle`. What is the key difference in when each runs during the Terraform workflow?

- A) Both run at the same point — they are two syntactic alternatives for the same assertion mechanism
- B) A `validation` block runs **before `terraform plan`** — it is evaluated during input variable processing and halts the run before any infrastructure analysis begins; a `precondition` runs **during `terraform apply`**, just before Terraform modifies the specific resource that contains it
- C) A `precondition` runs before `terraform plan`; a `validation` block runs after the plan is approved but before apply begins
- D) Both run after `terraform apply` completes — they are post-deployment verification tools

**Answer**: B

**Explanation**:
The timing difference is fundamental to understanding when each assertion catches a problem. `validation` runs at the earliest possible moment — during input variable processing, before planning, before any infrastructure is analysed. If the condition fails, no plan is generated. `precondition` runs mid-apply, immediately before Terraform makes changes to the resource that declares it. This means planning has already succeeded and other resources may have already been modified before the precondition is evaluated. Use `validation` for catching bad inputs early; use `precondition` for asserting conditions on resource-level prerequisites that can only be verified once planning is underway.

---

### Question 2 — `precondition` vs `postcondition`: Before vs After the Resource Change

**Difficulty**: Easy
**Answer Type**: one
**Topic**: Contrast between what precondition and postcondition assert and when each runs relative to the resource change

**Question**:
Compare a `precondition` and a `postcondition` declared in the same resource's `lifecycle` block. What is the key difference in their execution order and access to resource attributes?

- A) `precondition` and `postcondition` run at the same time — they differ only in whether the condition expression returns true or false
- B) A `precondition` runs **before** the resource is created or updated — it asserts that prerequisites are met and cannot use `self` to reference the resource's new attribute values; a `postcondition` runs **after** the resource change completes — it asserts that the created/updated resource meets requirements, and `self` references the resource's post-change attributes
- C) A `postcondition` runs before the resource change and uses `self` to reference the previous state; a `precondition` runs after and uses `self` to reference the new state
- D) Both can use `self`, but `precondition` uses the current (pre-change) `self` and `postcondition` uses the planned (post-change) `self`

**Answer**: B

**Explanation**:
`precondition` is a **gate before change** — it evaluates conditions that must be true before Terraform is allowed to touch the resource. Because the resource hasn't been modified yet, `self` cannot refer to the resource's new state, so `precondition` conditions typically reference data sources, other resources, or input variables. `postcondition` is a **gate after change** — it asserts that the resource, after being created or updated, meets expectations. The `self` keyword is valid here and refers to the resource as it exists after the apply operation. For example, a postcondition might assert `self.public_ip != null` to verify that the just-created instance has the expected attribute.

---

### Question 3 — `check` Block vs `precondition`: Blocking vs Non-Blocking Failures

**Difficulty**: Easy
**Answer Type**: one
**Topic**: Contrast between the failure behaviour of check blocks and preconditions

**Question**:
Compare a failing `check` block assertion with a failing `precondition`. What is the fundamental difference in how Terraform handles each failure?

- A) Both a failing `check` block and a failing `precondition` block apply and allow all resources to be created
- B) A failing `precondition` **blocks** the apply — Terraform halts before modifying the resource and exits with a non-zero status; a failing `check` block assertion is a **warning only** — Terraform displays the error message but all resource changes proceed normally and the apply exits successfully
- C) A failing `check` block blocks the apply; a failing `precondition` produces a warning only
- D) Both a failing `check` block and a failing `precondition` roll back any resources already created in the same apply run

**Answer**: B

**Explanation**:
This is one of the most important distinctions for the exam. `precondition` failures are **hard stops** — when the condition expression returns false, Terraform aborts the apply before modifying the resource, exits with a non-zero status code, and the error_message is displayed. `check` block failures are intentionally **soft** — the assertion failure is surfaced as a warning, but Terraform continues applying all planned changes and exits successfully. The `check` block was designed for continuous health monitoring (e.g., HTTP endpoint availability) where a transient failure should be visible to operators without blocking infrastructure deployment. Use `precondition` when a condition must be satisfied for the resource to be safe to create; use `check` for ongoing health assertions that should never block a deployment.

---

### Question 4 — `validation` Block Scope vs `precondition` Scope: What Each Can Reference

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Contrast between the expression scope allowed in validation conditions and precondition conditions

**Question**:
Compare what a `validation` block's `condition` and a `precondition`'s `condition` are each allowed to reference in their expressions. What is the key difference?

- A) Both are restricted to referencing only `var.<name>` — neither can reference data sources or resource attributes
- B) A `validation` block's `condition` can **only** reference `var.<variable_name>` — the specific variable being validated; a `precondition`'s `condition` can reference any value available at plan time, including data sources, other resource attributes, locals, and variables
- C) A `precondition`'s `condition` can only reference `self`; a `validation` block's `condition` can reference any expression including resources
- D) Both can reference any expression — the difference is only in when they are evaluated, not what they can reference

**Answer**: B

**Explanation**:
The scope restriction exists because of when each mechanism runs. `validation` runs before planning — at that point, only input variable values are available. Terraform enforces this by requiring that the `condition` only reference `var.<variable_name>`. Any attempt to reference a resource, data source, or local will produce a validation error at parse time. `precondition` runs during the apply phase, where the full configuration has been planned — resources, data sources, locals, and other variables are all resolved and available. This broader scope is what makes `precondition` suitable for checking things like whether a referenced AMI has the correct architecture (`data.aws_ami.ubuntu.architecture == "x86_64"`) or whether a dependency has the expected attribute value.

---

### Question 5 — `sensitive = true` on Variable: Terminal Masking vs State Protection

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Contrast between what sensitive=true on a variable actually protects vs what it does not protect

**Question**:
A variable is declared `sensitive = true` for a database password. Compare the protection this provides in two contexts: terminal output and the Terraform state file. What is the accurate description of each?

- A) `sensitive = true` both masks the value in terminal output AND encrypts it in the state file — it provides complete protection in both contexts
- B) `sensitive = true` **masks** the value in terminal output during `plan` and `apply` (showing `(sensitive value)` instead of the plaintext), but it provides **no protection** in the state file — the value is still stored in plaintext in `terraform.tfstate`; protecting it at rest requires an encrypted remote backend
- C) `sensitive = true` protects the value in the state file but has no effect on terminal output — the plaintext value is always shown during plan and apply
- D) `sensitive = true` removes the value from the state file entirely — it is never persisted anywhere

**Answer**: B

**Explanation**:
`sensitive = true` is a **display filter** — it tells Terraform to redact the value whenever it would appear in terminal output, plan files, or error messages, replacing it with `(sensitive value)`. This prevents the value from appearing in CI/CD logs or on-screen during operator runs. However, it provides absolutely no protection for the state file: the plaintext value is written to `terraform.tfstate` just like any other attribute. Anyone with read access to the state file can see the password. To protect sensitive values at rest, teams must use an encrypted remote backend such as HCP Terraform (which encrypts state) or S3 with server-side encryption, combined with strict IAM access controls.

---

### Question 6 — `validation` Block vs `check` Block: Where Each Is Declared

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Contrast between the structural location of a validation block and a check block in HCL

**Question**:
Compare where a `validation` block and a `check` block are declared in a Terraform configuration. How does their structural location differ, and what does that difference imply?

- A) Both `validation` and `check` blocks are top-level HCL blocks — they sit at the root of any `.tf` file alongside `resource` and `provider` blocks
- B) A `validation` block is declared **nested inside a `variable` block** — it is scoped to that specific variable and can only reference that variable; a `check` block is a **top-level block** — it sits at the root of a `.tf` file like a `resource` or `output` block, and it can reference any infrastructure value in scope, optionally including a scoped `data` source
- C) A `check` block is nested inside a `resource` block's `lifecycle`; a `validation` block is a top-level block
- D) Both are nested inside the `lifecycle` block of the resource they guard

**Answer**: B

**Explanation**:
The structural location of each block reflects its purpose and scope. A `validation` block is nested inside the `variable` block it validates — it is tightly scoped and can only reference `var.<variable_name>`. Multiple `validation` blocks can exist within a single variable. A `check` block is a top-level block — it stands independently at the root of any `.tf` file and can reference any value available in the module, including resource attributes and data source results. Optionally, a `check` block can declare its own scoped `data` source inside it (which is only used for the check's assertions and not available elsewhere in the module). This top-level placement reflects the `check` block's role as an independent infrastructure health assertion rather than an input constraint.

---

### Question 7 — `precondition` Failure vs `postcondition` Failure: Resource State After Each

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

**Answer**: B

**Explanation**:
`precondition` acts as a **pre-flight check** — if it fails, Terraform aborts before making the API call to create or modify the resource. The resource does not exist in AWS. `postcondition` acts as a **post-creation check** — Terraform only evaluates it after successfully creating or updating the resource. If the postcondition then fails, the resource **already exists** in AWS, but the Terraform apply has exited with an error. This is an important operational distinction: a postcondition failure leaves real infrastructure behind. The resource may be in an unexpected state (e.g., an instance without a public IP), and the operator must investigate and potentially taint or destroy the resource manually before the configuration can be remediated.

---

### Question 8 — `sensitive` Variable Propagation vs Explicit `sensitive` Output

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

**Answer**: B

**Explanation**:
When `sensitive = true` is set on the **variable**, Terraform marks the value itself as sensitive throughout the entire configuration. Any expression that references `var.db_password` — whether in a resource argument, a local, or an output — inherits the sensitive marker automatically. Plan output will show `(sensitive value)` for all such references, and if an undeclared output tries to expose the value, Terraform forces the user to acknowledge `sensitive = true`. In Approach B, only the declared output is masked — the variable value itself has no sensitive marker, so if it appears in a plan diff for a resource argument, it might be shown in plaintext. For comprehensive protection across the entire configuration, marking the variable as sensitive is the more thorough approach.

---

### Question 9 — `check` Block With Scoped Data Source vs `check` Block Without

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

**Answer**: B

**Explanation**:
A `check` block optionally accepts a single scoped `data` source declaration inside it. This scoped data source is evaluated only during the check's execution — it is not accessible from any other part of the module. This is useful when the health assertion requires fetching external data (e.g., an HTTP call to a load balancer endpoint) that has no other use in the configuration. Pattern B omits the scoped data source entirely and instead references `aws_db_instance.main.endpoint` directly — this is valid because `check` block assert conditions can reference any resource or data source that is already in scope at the module level. The two patterns represent different approaches to sourcing the data being checked, not a difference in the check's blocking/non-blocking behaviour.

---

### Question 10 — Three Condition Mechanisms: Failure Behaviour Comparison

**Difficulty**: Medium
**Answer Type**: many
**Topic**: Contrasting TWO failure behaviour differences across the three assertion mechanisms

**Question**:
Terraform provides three condition assertion mechanisms: `validation`, `precondition`/`postcondition`, and `check`. Which TWO statements correctly describe a contrast in their failure behaviour? (Select two.)

- A) A failing `validation` condition halts Terraform **before any plan is generated** — the run aborts with the error_message and no infrastructure analysis is performed; a failing `check` assertion produces a **warning** that is displayed but does not prevent the apply from completing
- B) A failing `precondition` halts the apply **before modifying the target resource** — the resource is never created or updated; a failing `postcondition` halts the apply **after the resource has been created or updated** — the resource already exists in the cloud provider when the failure is reported
- C) `validation`, `precondition`, and `postcondition` all produce warnings only — none of them block the apply
- D) A failing `check` assertion blocks the apply and triggers a rollback of any resources created during the run

**Answer**: A, B

**Explanation**:
(A) captures the contrast between `validation` (earliest possible failure — before plan) and `check` (non-blocking warning). `validation` prevents any planning from occurring; `check` allows full apply completion and only emits a warning. (B) captures the contrast between the two `lifecycle` conditions: `precondition` fails before the resource is touched (resource does not exist), while `postcondition` fails after the resource has been created/updated (resource exists in a potentially unexpected state). Options C and D are incorrect: `validation` and `precondition`/`postcondition` are hard stops that fail the run; `check` never blocks or rolls back anything.

---

### Question 11 — `validation` Block vs `check` Block: What Each Can Reference

**Difficulty**: Hard
**Answer Type**: one
**Topic**: Deep contrast between the expression scope and structural rules governing validation conditions and check assertions

**Question**:
Both `validation` blocks and `check` block assertions use a `condition` expression that must evaluate to a boolean. Compare the expression scope rules for each — what can each reference, and what structural rule constrains the `check` block that does not apply to `validation`?

- A) Both `validation` and `check` block conditions are restricted to referencing only `var.<name>` — no other values are permitted in either context
- B) A `validation` block's `condition` can only reference `var.<variable_name>` — all other references are forbidden; a `check` block's `assert` condition can reference any module-level value (resources, data sources, locals, variables); however, if a `check` block includes a scoped `data` source, the data source reference in the assert must use the `data.<type>.<name>` form scoped to the check — and that scoped source cannot be referenced outside the `check` block
- C) A `check` block's condition is restricted to referencing only `data` source attributes; a `validation` block can reference any value including resource attributes
- D) Both can reference resource attributes and data source results — the only difference is that `validation` is evaluated earlier in the workflow

**Answer**: B

**Explanation**:
`validation` blocks enforce a strict **scope restriction** at parse time: the condition can only reference `var.<variable_name>`. This is enforced because validation runs before planning when no other values exist. `check` block assertions have a **broad scope** — they can reference any module-level resource, data source, or local that is available at plan/apply time. The key structural nuance for `check` blocks is the scoped `data` source option: a `check` block can optionally declare one `data` source block inside it, which is evaluated exclusively for the check. That scoped data source is addressed as `data.<type>.<name>` within the assert condition, but it is not part of the module's global namespace and cannot be referenced by any resource, output, or local outside the `check` block. This isolation prevents check-only data fetches from accidentally affecting resource dependencies.

---

### Question 12 — `postcondition` with `self` vs `precondition` with External References

**Difficulty**: Hard
**Answer Type**: many
**Topic**: Contrasting TWO specific technical rules about expression references in preconditions and postconditions

**Question**:
Compare the expression reference rules for `precondition` and `postcondition` blocks. Which TWO statements correctly describe a difference? (Select two.)

- A) `self` is valid **only** in a `postcondition` — it refers to the resource after it has been created or updated; `self` is **not valid** in a `precondition` because the resource hasn't been created/modified yet when the precondition is evaluated
- B) A `precondition` can reference any value that is known at plan time — including other resource attributes, data sources, locals, and variables — but not `self`; a `postcondition` can reference all of those plus `self` to inspect the resource's own post-change attributes
- C) `self` is valid in both `precondition` and `postcondition`; the difference is that `self` in a `precondition` refers to the planned state while `self` in a `postcondition` refers to the applied state
- D) A `postcondition` can only reference `self` — it cannot reference other resources or module-level values

**Answer**: A, B

**Explanation**:
(A) `self` is reserved for `postcondition` — it refers to the resource or data source that contains the `lifecycle` block, as it exists after the create/update operation. Because `precondition` runs before the resource is touched, there is no "self" resource yet (or the resource exists in its previous state), so `self` is not permitted. (B) `precondition` has access to the full module scope at plan time — it can reference data sources, other resources' attributes, locals, and variables. This is what makes preconditions powerful for asserting cross-resource prerequisites (e.g., "the AMI I'm about to use must be x86_64"). After the resource change, `postcondition` adds `self` to that same scope, allowing assertions on the resource's own resulting attributes. (C) is incorrect — `self` is not valid in `precondition`. (D) is incorrect — `postcondition` can reference module-level values in addition to `self`.

---

### Question 13 — `sensitive = true` vs Vault Dynamic Secrets: Protection Depth

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

**Answer**: B

**Explanation**:
`sensitive = true` is a **display control** — it prevents the password from appearing in terminal output and plan files, but the value is written to `terraform.tfstate` in plaintext. Any user or system with read access to the state file (a CI agent, a developer with S3 bucket access, a leaked backup) can retrieve the password. The Vault dynamic secrets approach eliminates this problem in two ways: (1) the actual database credential never exists in the Terraform configuration at all — it is fetched from Vault at runtime; (2) Vault can issue **dynamic credentials** with a short TTL that are unique per apply run and automatically expire, so even if they were captured from a log, they would soon be invalid. The Vault provider does still store the data source results in state (data source results are always in state), but those credentials may be short-lived. The separation of concerns — Vault manages secrets, Terraform manages infrastructure — is the architectural benefit that goes beyond what `sensitive = true` alone can provide.

---

---

## Questions

---

### Question 1 — Root Module vs Child Module: Role and Location

**Difficulty**: Easy
**Answer Type**: one
**Topic**: Contrast between what the root module and a child module are in a Terraform configuration

**Question**:
Compare the **root module** with a **child module** in Terraform. What is the key difference between the two?

- A) The root module is always stored on the Terraform Registry; a child module is always a local directory
- B) The root module is the working directory from which you run Terraform commands — it contains the top-level `.tf` files you execute; a child module is any module called via a `module` block from the root or from another module — it may be a local subdirectory, a registry module, or a Git source
- C) The root module can only call one child module at a time; child modules can call unlimited other child modules
- D) A child module is the first module Terraform processes; the root module is processed last after all child modules complete

**Answer**: B

**Explanation**:
Every Terraform configuration directory is a module. The **root module** is specifically the working directory from which you run `terraform init`, `terraform plan`, and `terraform apply`. It is the entry point of execution. A **child module** is any module instantiated by a `module` block — whether sourced from a local relative path (`./modules/vpc`), the Terraform Registry (`hashicorp/consul/aws`), or a Git URL. A single root module can call many child modules, and child modules can in turn call further child modules. The distinction is structural: root is the top of the call hierarchy; child is anything below it.

---

### Question 2 — Local Path Module Source vs Terraform Registry Module Source

**Difficulty**: Easy
**Answer Type**: one
**Topic**: Contrast between how local path and Terraform Registry module sources are specified and what constraints each supports

**Question**:
Compare a local path module source with a Terraform Registry module source. What is the key structural and capability difference?

- A) A local path source uses `http://` as the prefix; a registry source uses `registry://` as the prefix
- B) A local path source begins with `./` or `../` and references a directory on the local filesystem — the `version` argument is **not supported** for local paths; a Terraform Registry source uses the three-part `<NAMESPACE>/<MODULE>/<PROVIDER>` format and **does support** the `version` argument for version constraints
- C) Both local path and registry sources support the `version` argument — the difference is that local paths require a full absolute path while registry sources use a relative namespace
- D) A registry source begins with `./registry/` to distinguish it from a local path; a local path omits the prefix entirely

**Answer**: B

**Explanation**:
Local path module sources point to a directory on the local filesystem. They require a relative path starting with `./` or `../` and do not support the `version` argument — there is no versioning concept for a local directory. Terraform Registry sources use the standardised `<NAMESPACE>/<MODULE>/<PROVIDER>` format (e.g., `terraform-aws-modules/vpc/aws`) and support `version` with constraint syntax (`~> 5.0`, `>= 4.0, < 6.0`). Registry modules are downloaded by `terraform init` and cached in `.terraform/modules/`. Local path modules are read directly from the filesystem; no downloading occurs, but `terraform init` must still be run to register them.

---

### Question 3 — `version` Argument vs `?ref=` Query Parameter: Registry Pin vs Git Pin

**Difficulty**: Easy
**Answer Type**: one
**Topic**: Contrast between how registry modules and Git-sourced modules are pinned to a specific version

**Question**:
Compare pinning a Terraform Registry module to a specific version versus pinning a Git-sourced module to a specific version. What is the correct mechanism for each?

- A) Both registry modules and Git-sourced modules use the `version` argument in the `module` block — the syntax is identical for both source types
- B) Terraform Registry modules are pinned using the `version` argument in the `module` block (e.g., `version = "~> 5.0"`); Git-sourced modules are pinned using the `?ref=` query parameter in the `source` URL (e.g., `?ref=v2.1.0`) — the `version` argument is **not valid** for Git sources and causes a `terraform init` error
- C) Git-sourced modules use the `version` argument; registry modules use the `?ref=` query parameter in their registry URL
- D) Both source types accept the `version` argument, but for Git sources it must contain a full commit SHA rather than a semantic version string

**Answer**: B

**Explanation**:
The versioning mechanism differs depending on where the module is sourced. For **Terraform Registry** and **private registry** sources, the `version` argument in the `module` block accepts constraint expressions (e.g., `"~> 5.0"`) and `terraform init` resolves the constraint against the registry's published versions. For **Git-based sources** (GitHub URLs, `git::https://`, `git::ssh://`), the `version` argument is invalid — using it causes a `terraform init` error. Instead, the `?ref=` query parameter is appended to the source URL to pin the checkout to a specific git tag, branch, or commit SHA (e.g., `"github.com/org/repo//modules/vpc?ref=v2.1.0"`).

---

### Question 4 — Child Module Variable Inheritance vs Explicit Input Passing

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

**Answer**: B

**Explanation**:
Child modules have **complete scope isolation** from their callers. A variable defined in the root module is not visible inside a child module unless it is explicitly passed as an argument in the `module` block. This is by design — it enforces explicit contracts between modules and makes data flow clear and auditable. If the child module declares `variable "environment" {}` with no default, and the caller does not pass `environment = var.environment`, Terraform will raise an error: "No value for required variable." If the child has a `default`, that default is used. The explicit-passing requirement is fundamental to Terraform module design.

---

### Question 5 — Referencing a Child Module Output vs Referencing a Resource Attribute

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Contrast between the syntax for accessing a child module's output and accessing a managed resource's attribute directly

**Question**:
Compare the syntax for referencing a value from a child module versus referencing an attribute from a managed resource directly. Given a module named `networking` with an output `vpc_id`, and a resource `aws_vpc` named `main` with attribute `id`, what is the correct syntax for each?

- A) Both use the same `resource.<name>.<attribute>` pattern — there is no distinction between module outputs and resource attributes at the reference level
- B) A child module output is referenced as `module.<module_name>.<output_name>` (e.g., `module.networking.vpc_id`); a managed resource attribute is referenced as `<resource_type>.<resource_name>.<attribute>` (e.g., `aws_vpc.main.id`) — the `module.` prefix clearly identifies a module output while the resource type prefix identifies a direct resource reference
- C) A child module output is referenced as `output.<module_name>.<output_name>`; a resource attribute uses `resource.<type>.<name>.<attr>`
- D) Both use `var.<name>` — module outputs and resource attributes are both treated as variable references in HCL

**Answer**: B

**Explanation**:
Terraform uses distinct namespaces for different reference types. **Module outputs** are accessed via `module.<module_name>.<output_name>` — the `module.` prefix identifies that the value comes from a child module's declared `output` block. **Resource attributes** are accessed via `<resource_type>.<resource_name>.<attribute>` — no `resource.` prefix is needed; the resource type itself serves as the namespace. For example, `module.networking.vpc_id` retrieves the `vpc_id` output from the `networking` module, while `aws_vpc.main.id` retrieves the `id` attribute directly from the `aws_vpc.main` resource. Using the wrong syntax (e.g., `output.networking.vpc_id`) is invalid and causes a plan-time error.

---

### Question 6 — `.terraform/modules/` Cache vs `.terraform/providers/` Cache

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Contrast between the purpose of the modules cache directory and the providers cache directory inside .terraform/

**Question**:
After running `terraform init`, two subdirectories are created inside `.terraform/`: `modules/` and `providers/`. Compare what each directory contains and why each needs to be refreshed.

- A) Both directories cache the same content — `modules/` stores a backup copy of the provider binaries and `providers/` stores a backup of the module source code
- B) `.terraform/modules/` contains the downloaded or locally-registered **module source code** for all `module` blocks in the configuration — it must be refreshed (by re-running `terraform init`) when a module `source` or `version` changes; `.terraform/providers/` contains the **provider plugin binaries** — it must be refreshed when the `required_providers` configuration changes or a new provider version is needed
- C) `.terraform/modules/` caches provider binaries; `.terraform/providers/` caches module source code — the names are inverted from what most developers expect
- D) Both directories are updated automatically on every `terraform plan` — no manual `terraform init` re-run is required after source changes

**Answer**: B

**Explanation**:
`terraform init` populates both directories with distinct content. `.terraform/modules/` contains the source code for every module referenced by a `module` block — for local path modules this is a reference; for registry and Git sources this is downloaded content. The file `.terraform/modules/modules.json` tracks the mapping. `.terraform/providers/` contains the binary executables for every provider declared in `required_providers`. If you add a new module `source` or change a `version` constraint, you must re-run `terraform init` to update `.terraform/modules/`. Similarly, adding or changing a provider requires re-running `terraform init` to download the new binary into `.terraform/providers/`. Neither directory is updated automatically during `plan` or `apply`.

---

### Question 7 — Registry Module Source Format vs GitHub URL Format

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Contrast between the structural format of a Terraform Registry module source and a GitHub URL module source

**Question**:
Compare the format of a Terraform Registry module source and a GitHub module source. What are the key structural differences, and what capability does only one of them support?

- A) A Terraform Registry source uses `registry://` as a URL scheme; a GitHub source uses `github://` — they are otherwise structurally identical
- B) A Terraform Registry source uses the three-part `<NAMESPACE>/<MODULE>/<PROVIDER>` format (e.g., `"terraform-aws-modules/vpc/aws"`) and supports the `version` argument; a GitHub source uses a URL beginning with `github.com/` or `git::https://github.com/` and does **not** support the `version` argument — version pinning is done with `?ref=` in the URL
- C) A GitHub source uses the three-part namespace format; a Terraform Registry source uses a full HTTPS URL
- D) Both formats are valid for the `version` argument — the only difference is the URL protocol used

**Answer**: B

**Explanation**:
These two source types look different and behave differently. A **Terraform Registry** source is a compact, slash-delimited identifier: `<NAMESPACE>/<MODULE>/<PROVIDER>`. It integrates with the registry API, supports semantic `version` constraints, and is the format for publicly published modules on `registry.terraform.io`. A **GitHub** source is a URL — `github.com/org/repo` or `git::https://github.com/org/repo.git` — and it interacts with the Git protocol. It does not support the `version` argument; pinning is done via `?ref=v2.0.0` in the URL. The `//` double-slash separator is used with GitHub sources to specify a subdirectory: `github.com/org/repo//modules/vpc?ref=v1.0.0`.

---

### Question 8 — `//` Double-Slash Subdirectory Separator vs `?ref=` Query Parameter in Git URLs

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

**Answer**: B

**Explanation**:
These are two independent URL annotation mechanisms for Git-based module sources. The **double-slash `//`** is a path separator that tells Terraform: "the module root is inside a subdirectory of this repository." Everything after `//` (up to `?`) is the path to the module's root within the checked-out repository. Without `//`, Terraform uses the repository root as the module root. The **`?ref=` query parameter** is a git checkout instruction: it tells `terraform init` which git ref (tag, branch, or SHA) to check out. Without `?ref=`, `terraform init` checks out the default branch. Both mechanisms can be combined in a single source URL and serve entirely different purposes — one selects the directory, the other selects the commit.

---

### Question 9 — Child Module `output` Block vs Root Module `output` Block: Declaration and Access

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Contrast between how child module outputs and root module outputs are declared and how they are accessed differently

**Question**:
Compare an `output` block declared in a **child module** with an `output` block declared in the **root module**. How does the declaration differ, and how is each accessed?

- A) Child module `output` blocks use a different syntax than root module `output` blocks — child modules must use `export` instead of `output`
- B) The `output` block syntax is **identical** in both child and root modules — both use `output "<name>" { value = ... }`; however, their access pattern differs: a child module output is accessed from the caller as `module.<module_name>.<output_name>`, while a root module output is displayed in the terminal after `terraform apply` and is accessible via `terraform output <name>` — it is not referenced from a parent (the root has no caller)
- C) Child module `output` blocks must include `export = true` to be visible from the calling module; root module outputs are always visible without any extra argument
- D) Root module outputs are declared in a separate `outputs.tf` file; child module outputs must be declared in `main.tf`

**Answer**: B

**Explanation**:
The `output` block uses the same HCL syntax regardless of whether it is in a child or root module. The difference is in how the value flows. A **child module output** exposes a value from inside the module to its caller — the caller accesses it as `module.<module_name>.<output_name>`. If the child's output is not declared, the value is private to that module. A **root module output** exposes a value to the operator — it is printed to the terminal after `terraform apply` and can be queried with `terraform output`. Root module outputs cannot be referenced as `module.root.*` because the root module has no caller. Both use exactly the same declaration syntax: `output "name" { value = ... }`.

---

### Question 10 — Two Differences Between Registry Module and Local Module

**Difficulty**: Medium
**Answer Type**: many
**Topic**: Contrasting TWO key differences between a published Terraform Registry module and a local path module

**Question**:
Compare a module sourced from the Terraform Registry with a module sourced from a local path. Which TWO statements correctly describe a difference? (Select two.)

- A) A Terraform Registry module supports the `version` argument and is downloaded by `terraform init` into `.terraform/modules/`; a local path module does **not** support `version` and is read directly from the filesystem — no downloading occurs during `terraform init`
- B) A Terraform Registry module must follow the naming convention `terraform-<PROVIDER>-<NAME>` to be publicly published; a local path module has no naming convention requirements — it can be named anything
- C) Both registry modules and local path modules require the `version` argument — without it, `terraform init` raises an error for both source types
- D) Local path modules support the `?ref=` query parameter for version pinning; registry modules use the `version` argument

**Answer**: A, B

**Explanation**:
(A) `version` is only supported for registry sources. When `terraform init` processes a registry module with a `version` constraint, it queries the registry API, resolves the version, and downloads the source code to `.terraform/modules/`. For a local path module, `terraform init` simply registers the path in `.terraform/modules/modules.json` — no download occurs and `version` is not a valid argument. (B) Published Terraform Registry modules must follow the naming pattern `terraform-<PROVIDER>-<NAME>` (e.g., `terraform-aws-vpc`) for discoverability and registry compliance. Local modules in your own directory have no such naming requirement. (C) is wrong — `version` is optional even for registry modules (though recommended). (D) is wrong — `?ref=` applies to Git sources, not local paths.

---

### Question 11 — `terraform init` Re-run for New Module Source vs New Provider

**Difficulty**: Hard
**Answer Type**: one
**Topic**: Contrast between why terraform init must be re-run after adding a new module source vs adding a new provider

**Question**:
Both adding a new `module` block with a new `source` and adding a new `required_providers` entry require re-running `terraform init`. Compare the specific reason `terraform init` is needed in each case — what does it do differently for modules vs providers?

- A) `terraform init` does the same thing in both cases — it validates syntax and writes a lock file
- B) When a new **module source** is added, `terraform init` needs to **download or register the module source code** into `.terraform/modules/` — without this, Terraform cannot find the module's `.tf` files and `terraform plan` fails with "module not installed"; when a new **provider** is added, `terraform init` needs to **download the provider plugin binary** into `.terraform/providers/` and update `.terraform.lock.hcl` with the provider's version and hash — without this, Terraform cannot make API calls to the provider
- C) When a new module source is added, `terraform init` updates `.terraform.lock.hcl` with the module's hash; when a new provider is added, it updates `.terraform/modules/modules.json`
- D) For new module sources, `terraform init` is optional if the source is a local path; for new providers, it is always required — there is no scenario where a provider can be used without running `terraform init`

**Answer**: B

**Explanation**:
`terraform init` performs distinct operations for modules and providers. For **modules**: it resolves the `source` URL, downloads remote module code (or registers local paths), and writes the mapping to `.terraform/modules/modules.json`. Running `terraform plan` without doing this for a new `module` block produces: "Module not installed. Run `terraform init`." For **providers**: it queries the provider registry, downloads the provider binary executable for the target platform, and records the version and cryptographic hash in `.terraform.lock.hcl`. Running `terraform plan` without installing a new provider produces: "Provider not installed." The two operations affect different directories (`.terraform/modules/` vs `.terraform/providers/`) and different metadata files (`modules.json` vs `.terraform.lock.hcl`). Note that for local path modules, the init step is still required to register the module even though no download occurs.

---

### Question 12 — Two Differences Between Module Input via Literal and via Expression

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

**Answer**: A, B

**Explanation**:
(A) is the primary practical difference: Block B makes the module reusable and environment-agnostic. By passing `var.environment` and `var.vpc_cidr`, the same module block can represent different infrastructure configurations simply by changing the input variables — via `-var` flags, `.tfvars` files, or workspace-specific variable sets. Block A bakes `"production"` and `"10.0.0.0/16"` directly into the configuration; changing them requires editing the source file. (B) describes a real but practically insignificant technical distinction: literal values in Block A are graph-time constants whereas Block B requires variable evaluation first. In any real Terraform run, this difference is imperceptible. (C) is a false security claim — the `source` argument and module identity provide no protection against malicious inputs in either case. (D) is incorrect — Terraform plans changes based on the resolved value compared to state, not based on whether the value came from a literal or variable.

---

### Question 13 — Standard Module File Structure vs Monolithic Single-File Module

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

**Answer**: B

**Explanation**:
Terraform treats all `.tf` files in a directory as part of a **single flat namespace** — there is no concept of file-level scoping or execution order. A `resource` block in `variables.tf` is just as valid as one in `main.tf`; an `output` block in `main.tf` works identically to one in `outputs.tf`. Splitting declarations across files versus keeping them in one file makes zero functional difference to how Terraform plans or applies. The standard layout is entirely a **convention for humans**: it makes modules navigable, reduces the cognitive load of contributors, and matches the expectations of anyone who has worked with public Terraform modules. For published modules on the Terraform Registry, following the standard structure is especially important because users will look in `variables.tf` for the module's interface and `outputs.tf` for its exported values. Options A, C, and D all incorrectly imply that Terraform's internal processing depends on the file structure.

---

---

## Questions

---

### Question 1 — Local Backend vs S3 Backend: Collaboration and Safety

**Difficulty**: Easy
**Answer Type**: one
**Topic**: Contrast between the limitations of the local backend and the capabilities of a remote S3 backend

**Question**:
Compare the **local backend** (default `terraform.tfstate` file) with the **S3 backend**. What is the most significant operational difference between the two?

- A) The local backend encrypts state automatically; the S3 backend stores state in plaintext unless `encrypt = true` is set
- B) The local backend stores state in a file on the workstation running Terraform — it offers no collaboration support, no built-in locking, and no encryption; the S3 backend stores state in a shared S3 bucket — it enables team collaboration, supports state locking via DynamoDB, and supports server-side encryption at rest
- C) Both backends support state locking — the local backend uses a file lock while S3 uses DynamoDB; encryption is optional in both cases
- D) The S3 backend can only be used with AWS resources; the local backend supports all providers

**Answer**: B

**Explanation**:
The local backend is the default and requires no configuration, but it has three critical limitations for team use: (1) state is stored on a single workstation, so teammates cannot share it; (2) there is no reliable locking mechanism — two engineers running `terraform apply` simultaneously can corrupt the state; (3) sensitive values in state are in plaintext in a local file. The S3 backend addresses all three: state is stored in a central, accessible S3 bucket; locking is provided by a DynamoDB table with a `LockID` hash key; and `encrypt = true` enables SSE at rest. These differences make the S3 backend (or HCP Terraform) the standard choice for any team environment.

---

### Question 2 — `terraform plan -refresh-only` vs `terraform apply -refresh-only`

**Difficulty**: Easy
**Answer Type**: one
**Topic**: Contrast between the plan-only and apply forms of the refresh-only flag

**Question**:
Compare `terraform plan -refresh-only` with `terraform apply -refresh-only`. What is the key difference between the two commands?

- A) `terraform plan -refresh-only` updates state to match the cloud; `terraform apply -refresh-only` only shows what has drifted without changing state
- B) `terraform plan -refresh-only` shows what drift exists between actual cloud resources and Terraform state — it **does not change state** and makes no modifications anywhere; `terraform apply -refresh-only` **updates state** to match the actual cloud resource values, reconciling drift — no infrastructure is created, modified, or destroyed in either case
- C) Both commands are identical — `-refresh-only` has the same effect regardless of whether it is used with `plan` or `apply`
- D) `terraform apply -refresh-only` creates new resources to match any detected drift; `terraform plan -refresh-only` only shows the diff

**Answer**: B

**Explanation**:
Both commands are read-side operations — neither creates, modifies, nor destroys infrastructure. The distinction is about what changes. `terraform plan -refresh-only` is purely observational: it queries the cloud provider for current resource attributes, compares them to state, and shows any differences. No state file is written. `terraform apply -refresh-only` takes that same refresh and **writes the result to state**, updating Terraform's recorded values to match what actually exists in the cloud. This is the appropriate command when you want to acknowledge drift (e.g., a team member manually updated a tag in the console) and align state without reverting the cloud change.

---

### Question 3 — `cloud` Block vs `backend "remote"`: Preferred HCP Terraform Connection

**Difficulty**: Easy
**Answer Type**: one
**Topic**: Contrast between the cloud block and the legacy remote backend for connecting to HCP Terraform

**Question**:
Compare the `cloud` block (Terraform 1.1+) with the `backend "remote"` block as methods for connecting to HCP Terraform. What is the key difference?

- A) `backend "remote"` is the current standard; the `cloud` block is a deprecated alias introduced for backward compatibility
- B) The `cloud` block is the **preferred, modern method** for connecting to HCP Terraform — it supports workspace selection by tags (in addition to name) and integrates features specific to HCP Terraform; `backend "remote"` is the **legacy method** — it is still valid and functional but predates HCP Terraform-specific features; HashiCorp recommends migrating to the `cloud` block
- C) Both blocks are exactly equivalent — the `cloud` block is simply renamed from `backend "remote"` with no functional differences
- D) The `cloud` block only supports HCP Terraform Free tier; `backend "remote"` is required for paid HCP Terraform tiers

**Answer**: B

**Explanation**:
Both blocks connect a local Terraform configuration to HCP Terraform, but they differ in capability and intent. The `cloud` block was introduced in Terraform 1.1 specifically for HCP Terraform and supports features that `backend "remote"` does not — most notably the ability to select workspaces by **tags** rather than only by name. This allows a single configuration to target multiple workspaces matching a tag filter, enabling workspace-per-environment patterns. `backend "remote"` predates these additions and only supports workspace selection by name. HashiCorp's documentation now directs users to the `cloud` block as the canonical way to integrate with HCP Terraform, while `backend "remote"` remains supported for existing configurations.

---

### Question 4 — `terraform init -migrate-state` vs `terraform init -reconfigure`

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Contrast between the two init flags used when changing a backend configuration

**Question**:
Compare `terraform init -migrate-state` with `terraform init -reconfigure`. When would you use each, and what does each do with existing state?

- A) Both flags are equivalent — they both migrate state to the new backend without user confirmation
- B) `terraform init -migrate-state` **copies existing state** from the old backend to the newly configured backend — it is used when you want to preserve your state history when switching backends; `terraform init -reconfigure` **ignores the existing state** and reconfigures the backend without migrating — it is used when you want to start fresh or when the state has already been manually moved
- C) `terraform init -reconfigure` migrates state; `terraform init -migrate-state` discards it — the flags are inverted from what their names suggest
- D) `-migrate-state` only works when switching between two remote backends; it cannot migrate from the local backend to a remote backend

**Answer**: B

**Explanation**:
When you change the backend configuration in a `terraform {}` block (e.g., switching from local to S3, or changing the S3 bucket), `terraform init` detects the change and refuses to proceed without one of these flags. `-migrate-state` is the safe option: it reads the state from the old backend and copies it to the new backend, so no state history is lost. You would use this when adopting a remote backend for the first time (migrating local state to S3 or HCP Terraform) or when reorganising where state is stored. `-reconfigure` skips migration entirely — it just applies the new backend configuration and treats it as starting fresh. Use this when the state has already been moved manually, when you know the new backend already contains the correct state, or when you intentionally want to abandon the current state location.

---

### Question 5 — `terraform state mv` vs `terraform state rm`

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Contrast between the purpose and effect of terraform state mv and terraform state rm

**Question**:
Compare `terraform state mv` with `terraform state rm`. Both modify what Terraform tracks in state — what is the fundamental difference between them?

- A) `terraform state mv` deletes a resource from both state and the cloud; `terraform state rm` only removes it from state while leaving the cloud resource intact
- B) `terraform state mv` **relocates** a resource within state — it renames or moves the resource's address (e.g., from `aws_instance.web` to `aws_instance.web_server`, or from a root resource into a module) without destroying or re-creating anything; `terraform state rm` **removes** a resource entry from state entirely — Terraform stops managing it, but the actual cloud resource is left untouched; the resource becomes unmanaged drift
- C) `terraform state rm` renames a resource; `terraform state mv` deletes it permanently from both state and the cloud provider
- D) Both commands are equivalent — the only difference is that `terraform state mv` requires confirmation while `terraform state rm` does not

**Answer**: B

**Explanation**:
`terraform state mv` is used for **refactoring** — when you rename a resource label in HCL or move a resource into a module, `terraform state mv` updates the state entry to match the new address. Without it, Terraform would plan to destroy the old resource and create a new one. Examples: renaming `aws_instance.web` to `aws_instance.web_server`, or moving it into `module.compute.aws_instance.server`. The cloud resource is untouched throughout. `terraform state rm` is used for **abandonment** — when you want Terraform to stop managing a resource. The state entry is deleted, the cloud resource remains, and on the next `terraform plan` the resource appears as new (because it is in the config but not in state). Both are state-only operations with no cloud API calls.

---

### Question 6 — HCP Terraform Workspace Variables vs Variable Sets

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Contrast between workspace-specific variables and variable sets in HCP Terraform

**Question**:
Compare **workspace variables** with **variable sets** in HCP Terraform. What is the key difference in scope and reusability?

- A) Workspace variables are reusable across all workspaces in an organisation; variable sets are scoped to a single workspace only
- B) Workspace variables are defined **per workspace** — they apply only to that specific workspace and must be configured individually for each workspace that needs them; variable sets are **reusable collections** of variables that can be assigned to multiple workspaces or an entire organisation — a single change to a variable set propagates to all assigned workspaces
- C) Both workspace variables and variable sets work identically — the only difference is that variable sets have a different UI panel in HCP Terraform
- D) Variable sets are used only for Terraform input variables; workspace variables are used only for environment variables (like `AWS_ACCESS_KEY_ID`)

**Answer**: B

**Explanation**:
Workspace variables are the simplest form of variable management in HCP Terraform — you define a value directly on a workspace and it applies to runs in that workspace only. This is fine for workspace-specific values but becomes repetitive when multiple workspaces need the same credentials or settings. Variable sets solve this: you define a named collection of variables once (e.g., "AWS Credentials" containing `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY`) and assign it to as many workspaces as needed — or to the entire organisation. When credentials rotate, updating the variable set automatically propagates the change to all assigned workspaces. Variable sets can contain both Terraform input variables and environment variables.

---

### Question 7 — Speculative Plan vs Plan-and-Apply Run in HCP Terraform

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Contrast between a speculative plan run and a plan-and-apply run in HCP Terraform

**Question**:
Compare a **speculative plan** run with a **plan-and-apply** run in HCP Terraform. What is the fundamental difference?

- A) A speculative plan is faster because it skips the refresh phase; a plan-and-apply run always refreshes state before planning
- B) A speculative plan is **read-only** — it computes what changes would occur but **can never progress to an apply**; it is triggered by pull requests or API calls and posts its results as status checks; a plan-and-apply run **can apply changes** — it proceeds through planning and, based on workspace settings, either auto-applies or waits for manual confirmation before applying
- C) A plan-and-apply run is triggered only by manual CLI commands; a speculative plan is triggered only by VCS events
- D) Both run types can apply infrastructure changes — the difference is that a speculative plan requires an additional approval step before applying

**Answer**: B

**Explanation**:
The speculative plan is designed for **visibility without risk** — it evaluates what a configuration change would do, but it is architecturally incapable of applying. No matter how long you wait, a speculative plan will never apply. It is used in VCS workflows to give pull request reviewers a preview of infrastructure impact. A plan-and-apply run is the standard operational run — it computes a plan and then, depending on the workspace's apply method setting, either automatically applies (auto-apply mode) or pauses for a human to review and confirm. Understanding that speculative plans are permanently non-applying is important for VCS workflow questions on the exam.

---

### Question 8 — `TF_LOG_CORE` vs `TF_LOG_PROVIDER` vs `TF_LOG`

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Contrast between the granular log variables and the combined TF_LOG variable

**Question**:
Compare `TF_LOG_CORE`, `TF_LOG_PROVIDER`, and `TF_LOG`. How do the granular variables differ from the single combined variable?

- A) `TF_LOG_CORE` and `TF_LOG_PROVIDER` are deprecated aliases for `TF_LOG` — they all control the same log stream
- B) `TF_LOG` sets a **single log level for all Terraform output** — both the core engine and provider plugins log at the same verbosity; `TF_LOG_CORE` and `TF_LOG_PROVIDER` are **independent controls** — `TF_LOG_CORE` controls only the Terraform core engine's log output, and `TF_LOG_PROVIDER` controls only the provider plugin log output; this allows operators to enable `TRACE` for a specific provider while keeping core logs at a quieter level (or vice versa), reducing noise when debugging provider-specific issues
- C) `TF_LOG_PROVIDER` sets log output for all Terraform runs in a project; `TF_LOG_CORE` sets it for a specific workspace; `TF_LOG` is the organisation-wide default
- D) `TF_LOG_CORE` and `TF_LOG_PROVIDER` only apply when `TF_LOG_PATH` is also set — without a path, only `TF_LOG` produces output

**Answer**: B

**Explanation**:
`TF_LOG` is the coarse-grained control: set it to `DEBUG` or `TRACE` and everything — core engine, provider plugins, gRPC calls — logs at that level. This is often more output than needed. The granular variables offer surgical control: `TF_LOG_CORE=TRACE` turns on maximum verbosity for the Terraform core engine (graph traversal, state operations, plan computation) while provider logs remain silent, and `TF_LOG_PROVIDER=TRACE` does the opposite — maximally verbose provider plugin logging while core remains quiet. This separation is particularly useful when debugging why a provider API call is failing (use `TF_LOG_PROVIDER=TRACE`) versus debugging unexpected plan behaviour (use `TF_LOG_CORE=DEBUG`).

---

### Question 9 — Sentinel vs OPA: Two HCP Terraform Policy Frameworks

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Contrast between Sentinel and OPA as the two policy enforcement frameworks in HCP Terraform

**Question**:
HCP Terraform supports two policy enforcement frameworks: **Sentinel** and **OPA (Open Policy Agent)**. What is the key difference between them?

- A) Sentinel is used for cost estimation policies; OPA is used for security compliance policies — they target different policy domains
- B) Sentinel uses **HashiCorp's proprietary Sentinel DSL** — it is developed and maintained by HashiCorp and is tightly integrated with HCP Terraform's policy workflow; OPA uses **Rego**, an open-source policy language maintained by the Open Policy Agent community — it offers broader ecosystem support and is used across many tools beyond Terraform; both frameworks enforce the same three enforcement levels (advisory, soft-mandatory, hard-mandatory) in HCP Terraform
- C) OPA policies run before the plan; Sentinel policies run after the plan but before the apply — they execute at different points in the run lifecycle
- D) Sentinel is available on all HCP Terraform tiers; OPA is only available on the Enterprise tier and cannot be used in the Free or Plus plans

**Answer**: B

**Explanation**:
Both Sentinel and OPA are supported policy-as-code frameworks in HCP Terraform that evaluate infrastructure plans before apply. The primary difference is language and origin. **Sentinel** is HashiCorp's own policy language — it was designed specifically for the HashiCorp ecosystem and integrates deeply with HCP Terraform's run workflow. **OPA** (Open Policy Agent) uses the Rego language, is open-source, and has a large community outside Terraform. Teams that already use OPA across their infrastructure toolchain (Kubernetes admission control, API gateway policies, etc.) may prefer OPA for consistency. Both frameworks support the same three enforcement levels and both can access the Terraform plan as structured data for evaluation. For the exam, know that both exist and that Sentinel is HashiCorp-native while OPA is community/open-source.

---

### Question 10 — Three Policy Enforcement Levels: Two Key Contrasts

**Difficulty**: Medium
**Answer Type**: many
**Topic**: Contrasting TWO of the three HCP Terraform policy enforcement levels

**Question**:
HCP Terraform policy sets support three enforcement levels: `advisory`, `soft-mandatory`, and `hard-mandatory`. Which TWO statements correctly describe a contrast between these levels? (Select two.)

- A) An `advisory` policy failure displays a warning but **does not block the run** — the plan-and-apply continues regardless of the policy result; a `hard-mandatory` policy failure **always blocks the run** and cannot be overridden by any user, including organisation owners
- B) A `soft-mandatory` policy failure blocks the run by default but can be **overridden** by a user with sufficient permissions (typically an organisation owner or designated override role) — the run can then proceed despite the policy failure; `hard-mandatory` failure **cannot be overridden** by any user under any circumstances
- C) `advisory` policies only apply to speculative plans; `soft-mandatory` and `hard-mandatory` policies apply to plan-and-apply runs
- D) All three enforcement levels cause the run to fail with a non-zero exit code — the difference is only in how the failure message is displayed in the UI

**Answer**: A, B

**Explanation**:
(A) captures the contrast between the weakest and strongest levels. `advisory` is informational — the policy result is shown in the run output, but a failure is a warning only and the apply proceeds normally. `hard-mandatory` is an absolute gate — no one can override it, not even organisation owners; the run cannot proceed until the policy violation is resolved in the configuration. (B) captures the middle ground: `soft-mandatory` blocks like `hard-mandatory` initially, but designated users (typically organisation owners or a specific override role) can manually override the block and allow the run to continue. This gives organisations a "break glass" option for exceptional circumstances while still enforcing a default gate. (C) is incorrect — enforcement levels apply to plan-and-apply runs, not selectively to speculative vs. non-speculative. (D) is incorrect — `advisory` does not cause run failure.

---

### Question 11 — HCP Terraform Owner Role vs Workspace Admin Permission

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Contrast between organisation-level Owner role and workspace-level Admin permission in HCP Terraform

**Question**:
Compare the **Owner** organisation-level role with the **Admin** workspace-level permission in HCP Terraform. What is the scope difference?

- A) Owner and Admin are the same role — "Owner" is the UI label and "Admin" is the API name for the same permission level
- B) **Owner** is an **organisation-level role** — it grants full access to all settings, workspaces, teams, and governance across the entire organisation; **Admin** is a **workspace-level permission** — it grants full control over a specific workspace (managing variables, team access, workspace settings, and run approvals) but has no authority over other workspaces or organisation-level settings unless that permission is explicitly granted on each workspace
- C) Admin is a superset of Owner — an Admin can manage organisation-level settings in addition to workspace-level settings
- D) Owner role is limited to read-only access across all workspaces; Admin is the role that allows applying changes

**Answer**: B

**Explanation**:
HCP Terraform has a two-tier permission model. At the **organisation level**, there are two roles: **Owner** (full access to everything — workspaces, teams, policies, billing, SSO, audit logs, registry) and **Member** (access defined at the workspace level only). At the **workspace level**, four permissions exist: Read, Plan, Write, and Admin. Workspace **Admin** grants full control over that workspace — managing variables, configuring VCS connection, managing team access to the workspace, triggering and approving runs — but this authority is scoped to that single workspace. An operator with workspace Admin on `production` cannot modify `staging` or organisation-level policies unless they are also an organisation Owner or have Admin on `staging` separately. This granular model allows organisations to delegate workspace management without granting organisation-wide authority.

---

### Question 12 — Import Block Workflow vs CLI Import Workflow: Two Key Differences

**Difficulty**: Hard
**Answer Type**: many
**Topic**: Contrasting TWO workflow differences between the declarative import block (Terraform 1.5+) and the legacy terraform import CLI command

**Question**:
Compare the workflow for importing an existing resource using the declarative `import` block versus the legacy `terraform import` CLI command. Which TWO statements correctly describe a difference between the two workflows? (Select two.)

- A) The `import` block workflow supports **running `terraform plan` before any state changes are made** — the engineer can preview the import (and optionally generate HCL with `-generate-config-out`) before committing; the CLI `terraform import` command **immediately writes the resource to state** with no plan preview step — there is no way to preview what will be imported before the state is modified
- B) The CLI `terraform import` command **requires an existing resource block** in the configuration before it can run — the block body can be empty, but the block must exist; the `import` block can be added to configuration and used with `terraform plan -generate-config-out=generated.tf` to have Terraform **generate the resource block automatically** — the engineer starts with only the `import` block and no resource block
- C) Both workflows require the resource block to exist before the import command runs — the `import` block offers no config generation capability
- D) The CLI `terraform import` command can import multiple resources in a single run; the `import` block can only import one resource per block

**Answer**: A, B

**Explanation**:
(A) is the most operationally significant difference: the `import` block is declarative and integrates with the standard plan/apply cycle. You can run `terraform plan` to see exactly what will be imported — and Terraform will validate that the configuration matches the resource — before a single change is made to state. The CLI command bypasses this safety net: it writes to state immediately upon execution. (B) is the second major difference: the CLI command has always required the resource block to pre-exist (otherwise Terraform has no address to write the state entry to). The `import` block enables a new workflow where you start with only the `import` block and run `terraform plan -generate-config-out=generated.tf` — Terraform queries the provider, reads the resource's current attributes, and generates a complete HCL resource block. You then review and clean up the generated file before running `terraform apply` to complete the import. (C) is incorrect — the `import` block does support config generation. (D) is incorrect — you can have multiple `import` blocks and the CLI can be scripted to run multiple times.

---

### Question 13 — Dynamic OIDC Credentials vs Static Environment Variable Credentials in HCP Terraform

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

**Answer**: B

**Explanation**:
The security difference is fundamental, not cosmetic. **Approach A** stores IAM credentials that are valid indefinitely (or until manually rotated) as workspace variables. Even though HCP Terraform marks them sensitive and encrypts them at rest, they represent a persistent secret that must be managed, rotated, and protected. Any system with access to the HCP Terraform API or the workspace can potentially exfiltrate them, and a leaked key remains dangerous until it is revoked. **Approach B** (dynamic OIDC credentials) eliminates the concept of a stored secret entirely. HCP Terraform acts as an OIDC identity provider — it issues a signed JWT for each run, AWS's IAM identity provider validates the JWT, and AWS returns temporary credentials (via `AssumeRoleWithWebIdentity`) with a short TTL. These credentials are unique per run, expire automatically, and nothing persistent is stored in HCP Terraform. The residual risk of a leaked credential is minimal because it expires quickly. This architecture — often called "keyless authentication" or "workload identity" — is the recommended security model for HCP Terraform-to-cloud authentication.

---