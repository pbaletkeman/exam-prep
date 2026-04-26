# Terraform Associate (004) — Question Bank Iter 4 Batch 1

**Iteration**: 4
**Iteration Style**: Error identification — spot the mistake in config, workflow, or claim
**Batch**: 1
**Objective**: 1 — IaC Concepts
**Generated**: 2026-04-25
**Total Questions**: 12
**Difficulty Split**: 2 Easy / 8 Medium / 2 Hard
**Answer Types**: 9 `one` / 3 `many` / 0 `none`

---

# Terraform Associate (004) — Question Bank Iter 4 Batch 2

**Iteration**: 4
**Iteration Style**: Error identification — spot the mistake in config, workflow, or claim
**Batch**: 2
**Objective**: 2 — Terraform Fundamentals (Providers & State)
**Generated**: 2026-04-25
**Total Questions**: 13
**Difficulty Split**: 2 Easy / 9 Medium / 2 Hard
**Answer Types**: 10 `one` / 3 `many` / 0 `none`

---

# Terraform Associate (004) — Question Bank Iter 4 Batch 3

**Iteration**: 4
**Iteration Style**: Error identification — spot the mistake in config, workflow, or claim
**Batch**: 3
**Objective**: 3 — Core Workflow & CLI
**Generated**: 2026-04-25
**Total Questions**: 13
**Difficulty Split**: 2 Easy / 9 Medium / 2 Hard
**Answer Types**: 10 `one` / 3 `many` / 0 `none`

---

# Terraform Associate (004) — Question Bank Iter 4 Batch 4

**Iteration**: 4
**Iteration Style**: Error identification — spot the mistake in config, workflow, or claim
**Batch**: 4
**Objective**: 4a — Resources, Data & Dependencies
**Generated**: 2026-04-25
**Total Questions**: 13
**Difficulty Split**: 2 Easy / 9 Medium / 2 Hard
**Answer Types**: 10 `one` / 3 `many` / 0 `none`

---

# Terraform Associate (004) — Question Bank Iter 4 Batch 5

**Iteration**: 4
**Iteration Style**: Error identification — spot the mistake in a claim, config, or workflow description
**Batch**: 5
**Objective**: 4b — Variables, Outputs, Types & Functions
**Generated**: 2026-04-25
**Total Questions**: 13
**Difficulty Split**: 3 Easy / 8 Medium / 2 Hard
**Answer Types**: 10 `one` / 3 `many` / 0 `none`

---

# Terraform Associate (004) — Question Bank Iter 4 Batch 6

**Iteration**: 4
**Iteration Style**: Error identification — spot the mistake in a claim, config, or workflow description
**Batch**: 6
**Objective**: 4c — Custom Conditions & Sensitive Data
**Generated**: 2026-04-25
**Total Questions**: 12
**Difficulty Split**: 2 Easy / 8 Medium / 2 Hard
**Answer Types**: 9 `one` / 3 `many` / 0 `none`

---

# Terraform Associate (004) — Question Bank Iter 4 Batch 7

**Iteration**: 4
**Iteration Style**: Error identification — spot the mistake in a claim, config, or workflow description
**Batch**: 7
**Objective**: 5 — Modules + 6 — State Backends
**Generated**: 2026-04-25
**Total Questions**: 13
**Difficulty Split**: 2 Easy / 9 Medium / 2 Hard
**Answer Types**: 10 `one` / 3 `many` / 0 `none`

---

---

---

## Questions

---

### Question 1 — Incorrect Idempotency Definition

**Difficulty**: Easy
**Answer Type**: one
**Topic**: Identifying the error in a definition of idempotency

**Question**:
A team lead explains idempotency to a new hire:

> "Idempotency means Terraform is thorough — every time you run `terraform apply`, it destroys the existing infrastructure and recreates it from scratch to ensure everything matches the configuration exactly."

What is the error in this explanation?

- A) There is no error — destroy-and-recreate on every apply is exactly how Terraform ensures consistency
- B) Idempotency means the *opposite* — applying the same configuration multiple times produces the same end state without unnecessary changes; if the infrastructure already matches, no actions are taken
- C) The error is that idempotency only applies to the first apply — subsequent applies always trigger a full rebuild
- D) The error is that `terraform apply` never destroys resources — only `terraform destroy` can do that

**Answer**: B

**Explanation**:
Idempotency means applying the same configuration N times produces the same result. After the first successful apply, running `terraform apply` again against an unchanged configuration reports "No changes. Your infrastructure matches the configuration." — no destroy-and-recreate cycle occurs. Terraform plans only the *difference* between desired and current state; if there is no difference, it takes no action. The team lead has confused "thorough" with idempotent.

---

### Question 2 — Incorrect Claim About `count = 0`

**Difficulty**: Easy
**Answer Type**: one
**Topic**: Identifying the error in a claim that `count = 0` is invalid syntax

**Question**:
During a code review, an engineer comments:

> "This is a syntax error — `count = 0` is not allowed in a `resource` block. The `count` meta-argument must be at least `1` or it should be removed entirely."

What is the error in this comment?

- A) The comment is correct — `count = 0` raises a Terraform validation error
- B) The comment is correct, but `count = 0` is allowed only in module blocks, not resource blocks
- C) The comment is incorrect — `count = 0` is valid and useful; it tells Terraform the desired number of instances is zero, so any existing instances will be planned for destruction
- D) The comment is partially correct — `count = 0` is allowed but only when combined with a `lifecycle` block

**Answer**: C

**Explanation**:
`count = 0` is perfectly valid Terraform syntax and is a deliberate pattern used to conditionally disable a resource without removing its block from the configuration. When `count = 0`, Terraform's desired state for that resource is zero instances, so if any currently exist in state, they will be planned for destruction. This is equivalent to saying "this resource should not exist." There is no minimum value requirement for `count`.

---

### Question 3 — State File Described as Desired State

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Identifying the error in conflating the state file with desired state

**Question**:
A senior engineer is onboarding new team members and says:

> "The `terraform.tfstate` file is the source of truth for your desired infrastructure. Edit it directly when you want to change what Terraform will build on the next apply."

What is the error in this statement?

- A) There is no error — `terraform.tfstate` is both the desired state and the current state record
- B) The error is that the state file records the **current** tracked state of infrastructure (what Terraform believes exists), not the desired state; desired state is expressed in the `.tf` configuration files
- C) The error is that `terraform.tfstate` is read-only and cannot be edited under any circumstances
- D) The error is that the state file is not a source of truth at all — Terraform queries the cloud provider API every time without using it

**Answer**: B

**Explanation**:
The `terraform.tfstate` file records **current state** — what Terraform believes currently exists in the cloud, based on the last successful apply. Desired state is expressed in `.tf` configuration files. The two are compared during `terraform plan` to determine what changes to make. Directly editing the state file bypasses Terraform's safety checks and is discouraged for making configuration changes; `.tf` files are the correct place to declare desired infrastructure.

---

### Question 4 — Drift Defined as "Unrun Apply"

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Identifying the error in a definition of infrastructure drift

**Question**:
A developer writes this entry in a team wiki:

> "Infrastructure drift occurs when a developer updates the `.tf` configuration files but forgets to run `terraform apply`. The infrastructure has 'drifted' away from what the code says."

What is the error in this definition?

- A) There is no error — this is the correct definition of infrastructure drift
- B) The error is minor — the developer should have written `terraform plan` instead of `terraform apply`
- C) The error is that this scenario describes an **unapplied change**, not drift; drift specifically refers to when **real cloud infrastructure** diverges from the desired or tracked state — typically caused by manual out-of-band changes to the cloud, not unrun applies
- D) The error is that drift can only occur after `terraform destroy` has been run

**Answer**: C

**Explanation**:
Infrastructure drift is when the actual state of cloud resources diverges from what Terraform tracks — for example, a resource modified directly through the cloud console, resized by an autoscaler outside Terraform's control, or deleted manually. An engineer updating `.tf` files without running `terraform apply` has simply made an unapplied configuration change, not caused drift. The infrastructure hasn't changed — the configuration has. These are distinct scenarios that require different responses.

---

### Question 5 — Terraform and Ansible Both Called "Config Management"

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Identifying the error in classifying Terraform as a configuration management tool

**Question**:
A job posting reads:

> "We use Terraform and Ansible as our configuration management stack. Both tools install and configure software on our servers."

What is the error in this job posting?

- A) There is no error — Terraform and Ansible both fall under the configuration management category
- B) The error is that Ansible is a provisioning tool, not a configuration management tool
- C) The error is that Terraform is a **provisioning** tool used to create and manage infrastructure — not a configuration management tool; Ansible is the configuration management tool that installs and configures software on existing servers
- D) The error is that Terraform and Ansible cannot be used together in the same toolchain

**Answer**: C

**Explanation**:
Terraform and Ansible serve complementary but distinct roles. Terraform is a **provisioning** tool — it creates, modifies, and destroys cloud infrastructure resources (VMs, networks, storage). Ansible is a **configuration management** tool — it installs packages, manages services, and configures software on existing servers. Calling Terraform a "configuration management" tool is incorrect and conflates two separate IaC categories. Both tools together form a complete infrastructure automation stack.

---

### Question 6 — CloudFormation Described as Multi-Cloud

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Identifying the error in a claim that CloudFormation supports multi-cloud

**Question**:
An architect presents the following to their team:

> "We'll use AWS CloudFormation as our IaC tool because it supports multi-cloud — we can manage both our AWS RDS databases and our Azure blob storage containers from a single CloudFormation template."

What is the error in this statement?

- A) There is no error — CloudFormation supports Azure resources through an AWS-Azure partnership feature
- B) The error is that CloudFormation is AWS-only and cannot manage Azure resources; Terraform is the tool that supports managing resources across multiple cloud providers from a single configuration
- C) The error is that CloudFormation uses YAML/JSON templates which are less capable than HCL for multi-cloud scenarios
- D) The error is that Azure blob storage cannot be managed by any IaC tool

**Answer**: B

**Explanation**:
AWS CloudFormation is an AWS-native service that can only provision and manage AWS resources. It has no native capability to manage Azure, GCP, or other cloud provider resources. Terraform, by contrast, uses a provider plugin model that supports 3,000+ providers, enabling management of AWS and Azure (and many other) resources from a single root module configuration. An architect requiring multi-cloud IaC should evaluate Terraform, not CloudFormation.

---

### Question 7 — Two Incorrect Claims About IaC Benefits

**Difficulty**: Medium
**Answer Type**: many
**Topic**: Identifying TWO incorrect statements from a list of IaC benefit claims

**Question**:
A team writes four statements about the benefits of IaC in their documentation. Which TWO statements contain errors? (Select two.)

- A) "IaC enables disaster recovery — if an environment is lost, it can be recreated by applying the configuration files"
- B) "IaC eliminates infrastructure drift entirely — once infrastructure is managed by Terraform, no drift can ever occur"
- C) "Storing Terraform configuration in Git provides a version-controlled audit trail of every infrastructure change"
- D) "IaC is slower than manual console provisioning because every change must go through code review and a CI/CD pipeline"

**Answer**: B, D

**Explanation**:
Option B is incorrect: IaC *detects and can remediate* drift, but it does not eliminate it. Drift still occurs whenever someone makes manual out-of-band changes to cloud resources. Option D is incorrect: IaC is faster than manual provisioning at scale — automated pipelines can provision dozens of resources in minutes, while manual console work is slow and error-prone. Options A and C are correct statements about IaC benefits.

---

### Question 8 — IaC Said to Remove the Need for Audit Trails

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Identifying the error in claiming IaC removes the need for auditing

**Question**:
A compliance officer is told by a developer:

> "Now that we use Terraform, we don't need to worry about audit trails anymore — IaC tools handle everything automatically and there's nothing to track."

What is the error in this statement?

- A) There is no error — IaC tools built-in auditing eliminates the need for external audit mechanisms
- B) The error is that the statement inverts the relationship: IaC *creates* and *enhances* the audit trail — every infrastructure change committed to version control is traceable with author, timestamp, and message; IaC does not remove the need for auditing
- C) The error is that `terraform plan` creates the audit trail, not version control
- D) The error is that audit trails are only relevant for security resources, not infrastructure

**Answer**: B

**Explanation**:
One of IaC's primary benefits *is* audit trail creation. When configuration changes are committed to version control (Git), every infrastructure modification becomes a traceable record: who changed it, when, what changed, and why (via commit message). This is a significant improvement over ClickOps, which leaves no automatic version history. The developer's statement is backwards — IaC improves audit capability, it does not eliminate the concept of auditing.

---

### Question 9 — Two Incorrect Claims About Declarative vs Imperative

**Difficulty**: Medium
**Answer Type**: many
**Topic**: Identifying TWO incorrect statements about declarative and imperative IaC approaches

**Question**:
Four statements are made about declarative and imperative IaC approaches. Which TWO contain errors? (Select two.)

- A) "In a declarative approach, you describe the desired end state and the tool determines how to reach it"
- B) "Ansible playbooks are primarily imperative — they define ordered tasks to execute on target systems"
- C) "Terraform is imperative because it ultimately makes sequential API calls to cloud providers to create resources"
- D) "The declarative model guarantees idempotency — re-applying the same desired state configuration produces no changes if the current state already matches"

**Answer**: C, D

**Explanation**:
Option C is incorrect: the fact that Terraform uses API calls internally does not make it imperative. The *programming model* is what determines declarative vs imperative. Terraform's model is declarative — you describe desired state in HCL and Terraform determines the steps. Executing API calls is the implementation detail, not the model. Option D is also incorrect as stated: while declarative tools are designed to be idempotent, the guarantee is specifically about repeated applies with an *unchanged* configuration — it does not mean the same config is always a no-op in every scenario (e.g., the first apply always creates resources). The statement's absolute phrasing ("guarantees") without that qualifier makes it misleading. Options A and B are correct statements.

---

### Question 10 — Current State Described as Configuration Files

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Identifying the error in swapping "current state" and "desired state" definitions

**Question**:
A team's onboarding guide contains this paragraph:

> "In Terraform, current state refers to what your `.tf` files say the infrastructure should look like. Desired state is what actually exists in the cloud right now. Terraform's job is to make the desired state match the current state."

What is the error in this paragraph?

- A) There is no error — this correctly describes the relationship between current state and desired state
- B) The error is that `.tf` files represent **desired state**, not current state; what actually exists in the cloud (as tracked by the state file) is **current state**; Terraform reconciles by making current state match desired state — not the reverse
- C) The error is that the state file, not `.tf` files, represents desired state
- D) The error is minor — "current state" and "desired state" are interchangeable terms in Terraform documentation

**Answer**: B

**Explanation**:
The paragraph has the definitions completely swapped. **Desired state** is what `.tf` configuration files declare the infrastructure should look like. **Current state** is what actually exists in the cloud (tracked in the Terraform state file). Terraform's reconciliation direction is always: *bring current state toward desired state*. Making current state match desired state means creating, updating, or destroying resources until the cloud matches what the configuration declares. The paragraph's reversed definitions would cause serious conceptual confusion.

---

### Question 11 — Idempotency Applied to a First-Time Apply

**Difficulty**: Hard
**Answer Type**: one
**Topic**: Identifying the error in applying idempotency to mean "zero changes always"

**Question**:
A developer argues:

> "Idempotency means `terraform apply` is always safe to run because it will never make any changes — it's idempotent, so the result is always zero resources added, zero changed, and zero destroyed."

What is the specific error in this reasoning?

- A) There is no error — an idempotent operation always produces zero changes
- B) The error is that idempotency means the same **end state** is produced when applying the same configuration multiple times — the first apply *does* create resources; subsequent applies against an unchanged configuration with unchanged infrastructure produce no changes; "zero changes" is only the outcome when the infrastructure already matches the desired state
- C) The error is that idempotency is a property of `terraform plan`, not `terraform apply`
- D) The error is that the developer used the word "safe" — idempotent operations can still be dangerous

**Answer**: B

**Explanation**:
Idempotency does not mean "no changes ever." It means applying the same input multiple times produces the same result — the same desired end state. The *first* `terraform apply` on a new configuration creates all declared resources (many adds, zero changes). A *subsequent* apply with the same unchanged configuration and unchanged infrastructure produces no changes. If the infrastructure has drifted (e.g., a resource was deleted manually), apply *will* make changes to restore the desired state. "Always zero changes" is a fundamental misunderstanding of idempotency.

---

### Question 12 — Two Errors in a Declarative IaC Description

**Difficulty**: Hard
**Answer Type**: many
**Topic**: Identifying TWO incorrect claims in a developer's description of how declarative Terraform works

**Question**:
A developer writes a blog post about Terraform with these four claims. Which TWO contain errors? (Select two.)

- A) "When you write `resource \"aws_instance\" \"web\" { instance_type = \"t3.micro\" }`, you are describing what you want to exist — Terraform figures out how to create, update, or skip it based on current state"
- B) "Terraform's declarative model means you write step-by-step API calls in HCL that Terraform executes in order — like a shell script but with better syntax"
- C) "Because Terraform is declarative, running the same configuration against an already-provisioned environment makes no changes — the desired state is already satisfied"
- D) "Terraform is multi-cloud because its declarative model means the same HCL syntax works natively for all providers without any provider-specific blocks"

**Answer**: B, D

**Explanation**:
Option B is incorrect: HCL is not a sequence of API calls. Declarative HCL describes the desired end state — Terraform internally determines what API calls to make. Writing "step-by-step API calls in HCL" describes an imperative model, not a declarative one. Option D is incorrect: while Terraform supports multiple cloud providers, each provider requires its own `provider` block and uses provider-specific resource types (e.g., `aws_instance` vs `azurerm_virtual_machine`). The "same HCL works natively for all providers without provider-specific blocks" is false. Options A and C are correct descriptions of declarative Terraform behaviour.

---

---

## Questions

---

### Question 1 — Wrong Provider Source Address Format

**Difficulty**: Easy
**Answer Type**: one
**Topic**: Identifying a GitHub URL used incorrectly as a provider source address

**Question**:
A developer writes this `required_providers` block:

```hcl
terraform {
  required_providers {
    aws = {
      source  = "github.com/hashicorp/terraform-provider-aws"
      version = "~> 5.0"
    }
  }
}
```

What is the error in this configuration?

- A) The `version` constraint `"~> 5.0"` is invalid inside `required_providers` — version constraints must be declared in a separate `terraform_version` block
- B) The `source` value is incorrect — Terraform provider source addresses use the format `<namespace>/<type>` (defaulting to `registry.terraform.io`); GitHub repository URLs are not valid source addresses
- C) There is no error — Terraform supports GitHub URLs as an alternative source address for providers
- D) The error is that `"aws"` is the wrong local name — it must match the provider type exactly as `"hashicorp/aws"`

**Answer**: B

**Explanation**:
Provider source addresses follow the format `<hostname>/<namespace>/<type>`, where the hostname defaults to `registry.terraform.io` when omitted. The correct source address for the official AWS provider is `"hashicorp/aws"` (short form) or `"registry.terraform.io/hashicorp/aws"` (fully qualified). GitHub repository URLs such as `"github.com/hashicorp/terraform-provider-aws"` are not valid Terraform provider source address formats and would cause `terraform init` to fail.

---

### Question 2 — Lock File Incorrectly Added to `.gitignore`

**Difficulty**: Easy
**Answer Type**: one
**Topic**: Identifying the error in treating `.terraform.lock.hcl` the same as `.terraform/`

**Question**:
A developer updates the team's `.gitignore` file and adds this comment explaining their change:

```
# Both of these are auto-generated by terraform init and should never be committed.
.terraform/
.terraform.lock.hcl
```

What is the error in this reasoning?

- A) There is no error — both `.terraform/` and `.terraform.lock.hcl` are auto-generated and should be gitignored
- B) The error is the opposite — `.terraform/` should be committed but `.terraform.lock.hcl` should be gitignored
- C) The error is that `.terraform.lock.hcl` **must be committed** to version control so all team members and CI pipelines use the same provider versions; `.terraform/` (the plugin cache directory) is correctly gitignored
- D) The error is that `.gitignore` cannot affect Terraform behaviour — both files are always available regardless of git settings

**Answer**: C

**Explanation**:
`.terraform/` is a local plugin cache directory that is machine-specific, large, and regenerated by `terraform init` — it correctly belongs in `.gitignore`. `.terraform.lock.hcl`, however, **must be committed to version control**: it records the exact provider version and cryptographic hashes installed, ensuring every team member and CI pipeline uses identical provider versions. Omitting it from VCS allows different engineers to silently install different provider versions, causing inconsistent behaviour.

---

### Question 3 — `~> 5.0.0` Claimed Equivalent to `~> 5.0`

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Identifying the error in claiming two different pessimistic constraints allow the same range

**Question**:
During a code review, an engineer comments:

> "`version = \"~> 5.0.0\"` and `version = \"~> 5.0\"` are effectively identical — both allow any `5.x.x` version. You can use them interchangeably."

What is the error in this comment?

- A) There is no error — both constraints allow any version in the `5.x.x` range
- B) The error is that `~> 5.0` and `~> 5.0.0` both restrict to patch-level changes — the constraints are identical but the comment used the wrong term
- C) The error is that `"~> 5.0"` allows minor and patch updates (>= `5.0`, < `6.0`), while `"~> 5.0.0"` allows only patch updates (>= `5.0.0`, < `5.1.0`) — they permit different version ranges
- D) The error is that `~>` is not valid when used with three-component version numbers like `5.0.0`

**Answer**: C

**Explanation**:
The `~>` pessimistic constraint operator allows updates to the rightmost component specified. `"~> 5.0"` (two components) allows the minor version to increment: `>= 5.0` and `< 6.0` — any `5.x` version. `"~> 5.0.0"` (three components) allows only the patch version to increment: `>= 5.0.0` and `< 5.1.0` — only `5.0.x` versions. These are distinct ranges, and using `~> 5.0.0` where `~> 5.0` was intended would prevent installation of `5.1.0`, `5.2.0`, and all later `5.x` minor releases.

---

### Question 4 — Provider Reference Written as Quoted String

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Identifying the error in using a quoted string for the `provider` meta-argument

**Question**:
Read this resource configuration:

```hcl
provider "aws" {
  alias  = "west"
  region = "us-west-2"
}

resource "aws_instance" "replica" {
  provider      = "aws.west"
  ami           = "ami-0xyz"
  instance_type = "t3.micro"
}
```

What is the error in this resource block?

- A) The error is that `alias` cannot be combined with a `region` argument in the same provider block
- B) The error is that the `provider` meta-argument value `"aws.west"` is a quoted string — provider references must be written as an unquoted reference: `provider = aws.west`
- C) There is no error — both `provider = "aws.west"` and `provider = aws.west` are equivalent in Terraform
- D) The error is that the `provider` meta-argument is only allowed on module blocks, not resource blocks

**Answer**: B

**Explanation**:
The `provider` meta-argument on a resource block takes a provider reference — a specific HCL expression syntax in the form `<provider_type>.<alias>` — not a quoted string. Writing `provider = "aws.west"` treats the value as a literal string, which is a type error in Terraform. The correct form is the unquoted reference `provider = aws.west`. This distinction is important: the unquoted form tells Terraform to resolve the reference to the aliased `provider "aws" { alias = "west" }` configuration.

---

### Question 5 — Duplicate Provider Blocks Without Alias

**Difficulty**: Medium
**Answer Type**: many
**Topic**: Identifying TWO correct statements about what is wrong with duplicate provider blocks that lack an alias

**Question**:
Read this configuration:

```hcl
provider "aws" {
  region = "us-east-1"
}

provider "aws" {
  region = "us-west-2"
}
```

Which TWO statements correctly identify what is wrong with this configuration? (Select two.)

- A) Terraform returns a validation error — you cannot declare two `provider "aws"` blocks without giving the second one a unique `alias` argument
- B) There is no error — Terraform automatically selects the most recently declared provider block for all AWS resources
- C) The fix is to add `alias = "<name>"` to the second provider block, for example `alias = "west"`, so each configuration has a unique identity
- D) The fix is to move the second provider block into a separate `.tf` file — Terraform allows one provider block per file but multiple across files

**Answer**: A, C

**Explanation**:
Terraform requires every `provider` block for the same provider type to have a unique identity. The first (or only) block is the default configuration with no alias. Any additional blocks for the same provider must include a distinct `alias` argument — for example, `alias = "west"`. Without it, Terraform raises a validation error similar to "each provider configuration must have a unique alias." Splitting provider blocks across files has no effect — the uniqueness requirement applies across the entire configuration, not per file.

---

### Question 6 — `terraform state rm` Claimed to Delete Cloud Resource

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Identifying the error in claiming `terraform state rm` removes the resource from both state and the cloud

**Question**:
A team documents their cleanup process:

> "To decommission an S3 bucket managed by Terraform, we run `terraform state rm aws_s3_bucket.archive`. This removes the bucket from both our state file and AWS simultaneously — it's faster and safer than `terraform destroy` for individual resources."

What is the error in this documentation?

- A) There is no error — `terraform state rm` deletes the resource from both state and the cloud provider
- B) The error is that `terraform state rm` requires a `-force` flag to remove S3 buckets specifically
- C) The error is that `terraform state rm` only removes the resource from the **state file** — it does not delete the actual S3 bucket from AWS; the bucket continues to exist and Terraform simply stops managing it
- D) The error is that individual resources can only be destroyed using `terraform destroy -target`, not `terraform state rm`

**Answer**: C

**Explanation**:
`terraform state rm` is a state-only operation — it removes the resource address from the `terraform.tfstate` file but makes no API calls to delete the actual cloud resource. After running `terraform state rm aws_s3_bucket.archive`, the S3 bucket continues to exist in AWS, consuming storage and incurring costs; Terraform simply no longer tracks it. This command is used when you want to stop managing a resource with Terraform without destroying it (e.g., handing it off to manual management). To actually delete the bucket, use `terraform destroy -target=aws_s3_bucket.archive` or remove its block from the configuration and run `terraform apply`.

---

### Question 7 — `terraform plan -refresh=false` Claimed to Detect Drift

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Identifying the error in using `-refresh=false` for infrastructure drift monitoring

**Question**:
A DevOps team writes this procedure in their runbook:

> "To monitor for infrastructure drift, our scheduled pipeline runs `terraform plan -refresh=false` every hour. If the plan shows changes, we know someone made an out-of-band modification."

What is the error in this procedure?

- A) There is no error — `terraform plan -refresh=false` is the recommended approach for drift detection
- B) The error is that drift detection requires `terraform plan -detailed-exitcode`, not `-refresh=false`
- C) The error is that `terraform plan -refresh=false` **skips the live API refresh** and compares the configuration only against the cached state file — it cannot detect out-of-band changes made after the last apply because it never queries the actual infrastructure
- D) The error is minor — `-refresh=false` detects drift but displays it differently from a normal `terraform plan`

**Answer**: C

**Explanation**:
`terraform plan -refresh=false` compares the configuration (desired state) against the local state file (last known state) without making any API calls to check the real infrastructure. If someone manually changes a cloud resource after the last apply, the state file still records the old values, and `-refresh=false` sees no difference — the drift is invisible. To detect out-of-band changes, a plain `terraform plan` (which refreshes live resource state by default) or `terraform plan -refresh-only` is required, as these query the provider API and compare the actual infrastructure against state.

---

### Question 8 — `required_version` Placed Inside `required_providers`

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Identifying the error in placing `required_version` inside a provider object in `required_providers`

**Question**:
Read this `terraform` block:

```hcl
terraform {
  required_providers {
    aws = {
      source           = "hashicorp/aws"
      version          = "~> 5.0"
      required_version = ">= 1.5"
    }
  }
}
```

What is the error in this configuration?

- A) There is no error — `required_version` is a valid key inside a `required_providers` provider object
- B) The error is that `required_version` must use the `~>` operator, not `>=`
- C) The error is that `required_version` is an argument of the `terraform {}` block itself, not a property of a provider entry in `required_providers`; a provider object only accepts `source` and `version`
- D) The error is that `required_version` must be declared in a separate `version.tf` file

**Answer**: C

**Explanation**:
`required_version` constrains the **Terraform CLI version** and is a top-level argument inside the `terraform {}` block — not a property nested inside a provider entry in `required_providers`. A `required_providers` provider object accepts only `source` and `version`. The corrected configuration places `required_version` at the `terraform {}` block level:

```hcl
terraform {
  required_version = ">= 1.5"
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}
```

Placing `required_version` inside the provider object results in an unexpected argument error.

---

### Question 9 — Incorrect Claims About `terraform.tfstate.backup`

**Difficulty**: Medium
**Answer Type**: many
**Topic**: Identifying TWO errors in claims about what `terraform.tfstate.backup` stores and retains

**Question**:
A wiki article makes four claims about `terraform.tfstate.backup`. Which TWO contain errors? (Select two.)

- A) "`terraform.tfstate.backup` is automatically created before each `terraform apply` to preserve the previous state"
- B) "`terraform.tfstate.backup` maintains a rolling history of every previous state, allowing rollback to any earlier version"
- C) "Only one `terraform.tfstate.backup` file exists at a time — it is overwritten on each apply with the state from the previous apply"
- D) "`terraform.tfstate.backup` provides the same versioning capability as enabling S3 bucket versioning for a remote backend"

**Answer**: B, D

**Explanation**:
Option B is incorrect: `terraform.tfstate.backup` stores only **one** previous state — the state that existed immediately before the most recent apply. It is not a rolling history and does not allow rollback to arbitrary earlier versions; each apply overwrites the single backup file. Option D is incorrect: S3 bucket versioning stores every version of every state file indefinitely and supports restoring to any point in time. `terraform.tfstate.backup` provides no such capability — it is a single-file safety net, not versioned storage. Options A and C are both correct descriptions of how the backup file works.

---

### Question 10 — `terraform state push` Used to Read State

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Identifying the error in confusing `terraform state push` with `terraform state pull`

**Question**:
A developer writes this CI pipeline step in their documentation:

> "To inspect the raw state JSON in our pipeline without direct backend access, we use `terraform state push` — it downloads the current remote state to stdout so we can pipe it into `jq` for analysis."

What is the error in this description?

- A) There is no error — `terraform state push` downloads the current state to stdout
- B) The error is that state inspection in a CI pipeline requires `terraform show -json` rather than any `state` subcommand
- C) The error is that `terraform state push` **uploads** a local state file to a remote backend (a write operation) — not downloads; `terraform state pull` is the command that downloads the current remote state to stdout as JSON
- D) The error is that neither `push` nor `pull` produces JSON output — the `-json` flag is required for JSON format

**Answer**: C

**Explanation**:
The `terraform state` subcommands `push` and `pull` are inverse operations: `terraform state pull` reads the current state from the configured remote backend and writes it to stdout as JSON — it is the read/download operation. `terraform state push` reads a local state file and uploads it to the configured remote backend, overwriting the current remote state — it is a write/upload operation and potentially destructive. Confusing these two in a pipeline could cause an engineer to accidentally overwrite production state instead of reading it.

---

### Question 11 — Core↔Provider Communication Described as HTTP REST

**Difficulty**: Hard
**Answer Type**: one
**Topic**: Identifying the error in claiming Terraform Core communicates with provider plugins via HTTP REST

**Question**:
A blog post explains Terraform's plugin architecture:

> "When Terraform Core needs to perform a resource operation, it makes HTTP REST API calls to the provider plugin's built-in web server, which is listening on a local port. The plugin then forwards these requests to the cloud provider's API."

What is the error in this description?

- A) There is no error — Terraform Core communicates with providers via HTTP REST on localhost
- B) The error is that the provider plugin does not run as a separate process — it is compiled into the Terraform Core binary at build time
- C) The error is in the communication protocol: Terraform Core and provider plugins communicate via **gRPC** (not HTTP REST) over a Unix socket or localhost port; the providers then make HTTPS calls to cloud APIs, but the Core↔Plugin channel is gRPC
- D) The error is that the provider plugin forwards requests to the cloud API using gRPC — not HTTPS

**Answer**: C

**Explanation**:
Terraform Core and provider plugins are separate processes that communicate via **gRPC** — a high-performance remote procedure call framework, not HTTP REST. The provider plugin runs as a child process launched by Terraform Core and exposes a gRPC service that Core calls to perform CRUD operations. The provider *then* makes HTTPS API calls to the target cloud service. This two-layer architecture (Core ↔ gRPC ↔ Provider ↔ HTTPS ↔ Cloud API) is the correct description. The separation via gRPC is what allows provider upgrades independently of Terraform Core upgrades.

---

### Question 12 — Alias Name Mismatch Between Provider Block and Resource Reference

**Difficulty**: Hard
**Answer Type**: many
**Topic**: Identifying TWO problems caused by an alias mismatch between a provider block and a resource's `provider` argument

**Question**:
Read this configuration:

```hcl
provider "aws" {
  region = "us-east-1"
}

provider "aws" {
  alias  = "western"
  region = "us-west-2"
}

resource "aws_vpc" "secondary" {
  provider   = aws.west
  cidr_block = "10.1.0.0/16"
}
```

Which TWO statements correctly identify the problems in this configuration? (Select two.)

- A) `aws.west` does not refer to any declared provider configuration — the alias is `"western"`, so the correct reference is `aws.western`
- B) The `provider` meta-argument causes a validation error here because it must match the declared alias exactly — `aws.west` is not resolvable and Terraform will report an error
- C) The second `provider "aws"` block is invalid because each provider can only have one configuration per workspace
- D) The VPC will be created in `us-east-1` because Terraform falls back to the default provider when the aliased reference is unresolvable

**Answer**: A, B

**Explanation**:
The aliased provider block declares `alias = "western"`, making its reference `aws.western`. The resource block references `aws.west`, which does not match any declared provider configuration. Terraform cannot resolve this reference and raises a validation error (option B is correct). Option A is correct because the mismatch is the root cause — the fix is to change the resource to `provider = aws.western`. Option C is incorrect: multiple configurations of the same provider are explicitly supported via aliases. Option D is incorrect: Terraform does not silently fall back to the default provider when an unresolvable alias is referenced — it raises an error instead.

---

### Question 13 — `>= 5.0` Claimed Equivalent to `~> 5.0`

**Difficulty**: Hard
**Answer Type**: one
**Topic**: Identifying the error in claiming `>=` and `~>` produce the same version selection behaviour

**Question**:
An engineer opens a pull request changing the AWS provider constraint and comments:

> "I've updated `version = \"~> 5.0\"` to `version = \">= 5.0\"` — they're functionally equivalent since both select the latest available `5.x` provider version when you run `terraform init`."

What is the error in this reasoning?

- A) There is no error — `>= 5.0` and `~> 5.0` select the same set of versions
- B) The error is that `>= 5.0` is a syntax error in Terraform version constraints — only `~>` is supported for open-ended ranges
- C) The error is that `>= 5.0` has **no upper bound** and would also permit versions `6.0`, `7.0`, and beyond, whereas `~> 5.0` restricts the range to `>= 5.0` and `< 6.0`; the change allows any future major version to be installed, which could introduce breaking changes
- D) The error is that `>= 5.0` selects the minimum satisfying version (`5.0.0`) while `~> 5.0` always selects the latest — so they select different versions, not just different ranges

**Answer**: C

**Explanation**:
`~> 5.0` is a bounded pessimistic constraint that allows `>= 5.0` and `< 6.0` — it stays within major version 5. `>= 5.0` has no upper bound: it allows `5.x`, `6.x`, `7.x`, and any future version, meaning a new major provider release with breaking changes could be installed automatically during `terraform init`. These constraints are not equivalent and the change weakens version pinning significantly. The recommended approach for provider version constraints in production is `~> <major>.<minor>` to allow patch updates while preventing unexpected major-version changes.

---

---

## Questions

---

### Question 1 — `terraform validate` Claimed to Require Credentials

**Difficulty**: Easy
**Answer Type**: one
**Topic**: Identifying the error in claiming `terraform validate` needs cloud provider credentials

**Question**:
A team's onboarding guide states:

> "Before running `terraform validate`, ensure your AWS credentials are configured in your environment. The command connects to the provider API to verify that referenced resources — such as AMI IDs and IAM role ARNs — actually exist."

What is the error in this guidance?

- A) There is no error — `terraform validate` requires provider credentials to verify resource attribute values
- B) The error is that `terraform validate` does not check resource references at all — only `terraform plan` reads `.tf` files
- C) The error is that `terraform validate` performs **no network calls and requires no provider credentials** — it checks only HCL syntax and static configuration consistency (undefined references, type errors, invalid arguments) without querying any cloud API
- D) The error is that AMI IDs must be validated with `terraform plan`, not `terraform validate`, because `validate` only handles provider block syntax

**Answer**: C

**Explanation**:
`terraform validate` is a fully offline command — it checks HCL syntax, verifies that all variable and resource references are declared, confirms argument names are valid for each resource type, and detects type mismatches. It makes zero API calls and requires no credentials. Verifying that a referenced AMI ID or IAM role actually exists in the cloud only occurs during `terraform plan` or `terraform apply`, when the provider plugin queries the live API.

---

### Question 2 — `-` Plan Symbol Described as Update

**Difficulty**: Easy
**Answer Type**: one
**Topic**: Identifying the error in claiming the `-` plan symbol means an in-place update

**Question**:
A developer reads a `terraform plan` summary that includes this line:

```
  # aws_security_group.old will be removed
- resource "aws_security_group" "old" {
    - id   = "sg-0abc123def" -> null
    - name = "legacy-sg"    -> null
  }
```

The developer comments: "The `-` prefix means this security group will be updated in-place — the attributes shown in red are being modified."

What is the error in this interpretation?

- A) There is no error — the `-` prefix indicates an in-place update of the resource's attributes
- B) The error is that `-` indicates a **destroy** (deletion) operation — the security group will be permanently removed from the cloud; an in-place update is shown with the `~` prefix
- C) The error is that `-` means the resource is being moved to a different Terraform workspace
- D) The error is that `-` next to individual attribute lines always indicates a replacement, not a standalone destroy

**Answer**: B

**Explanation**:
The four `terraform plan` symbols are: `+` (create), `~` (update in-place), `-` (destroy), and `-/+` (destroy then recreate — replacement). The `-` prefix on the resource block means the resource will be **destroyed** — removed from the cloud entirely. Individual attribute lines also prefixed with `-` show the current values being removed. An in-place modification — where the resource continues to exist with changed attribute values — uses the `~` prefix on the resource block.

---

### Question 3 — `terraform fmt -check` Claimed to Reformat Files

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Identifying the error in claiming `terraform fmt -check` writes formatting changes to disk

**Question**:
A CI pipeline script includes this step with the following comment:

```bash
# Reformat all .tf files to canonical style, then fail the build if any were changed
terraform fmt -check
```

What is the error in this script?

- A) There is no error — `terraform fmt -check` reformats files and exits with code 1 if any were changed
- B) The error is that `-check` is not a valid flag for `terraform fmt`
- C) The error is that `terraform fmt -check` is **read-only** — it checks whether files need reformatting and exits with code 1 if they do, but it does **not** write any changes to disk; to actually reformat files and then check, run `terraform fmt` first (no flags)
- D) The error is that the CI script should use `terraform fmt -diff` instead of `terraform fmt -check` to write and verify changes simultaneously

**Answer**: C

**Explanation**:
`terraform fmt -check` is a **non-destructive gate**: it scans all `.tf` files, exits with code 1 if any file is not in canonical format, and exits with code 0 if all files are already correctly formatted. It makes no changes to any file. The comment in the script is therefore misleading — `-check` does not reformat. The correct CI pattern is either: (1) run `terraform fmt` (writes changes, exits 0) and then `terraform fmt -check` to verify, or (2) simply run `terraform fmt -check` as a gate that requires developers to run `terraform fmt` locally before pushing.

---

### Question 4 — `terraform init -reconfigure` Claimed to Migrate State

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Identifying the error in using `-reconfigure` when state migration is required

**Question**:
A team's runbook says:

> "To change from local state to an S3 remote backend, add the `backend \"s3\"` block to your configuration and run `terraform init -reconfigure`. This will reconfigure the backend and migrate your existing local state to S3 automatically."

What is the error in this runbook?

- A) There is no error — `terraform init -reconfigure` migrates state from the old backend to the new one
- B) The error is that backend changes require running `terraform state push` before `terraform init`
- C) The error is that `terraform init -reconfigure` forces Terraform to reconfigure the backend but **does not migrate existing state** — it may discard the current state location and start fresh; to copy existing state to the new backend, `terraform init -migrate-state` is the correct flag
- D) The error is that state migration from local to S3 requires running `terraform apply -migrate-state`, not an `init` flag

**Answer**: C

**Explanation**:
`terraform init -reconfigure` ignores any existing backend state and reconfigures the working directory to use the new backend from scratch — it does not migrate existing state. `terraform init -migrate-state` is the correct flag when switching backends: it detects the existing local state and prompts to copy it to the new backend (S3) before completing initialization. Using `-reconfigure` in this scenario risks leaving the existing state behind in the local file while the working directory points to an empty remote backend.

---

### Question 5 — `terraform plan -target` Claims About Dependencies

**Difficulty**: Medium
**Answer Type**: many
**Topic**: Identifying TWO errors in claims about how `-target` handles dependencies

**Question**:
A wiki article makes four claims about `terraform plan -target`. Which TWO contain errors? (Select two.)

- A) "Using `-target` emits a warning that the resulting plan may be incomplete and is not a reliable representation of the full configuration"
- B) "`terraform plan -target=aws_instance.web` plans only `aws_instance.web` exactly — its upstream dependencies (such as a security group or subnet it references) are excluded from the plan entirely"
- C) "`terraform plan -target` is the recommended approach for routine production applies because it limits the blast radius to only the intended resource"
- D) "The targeted resource and any resources it transitively depends on are included in the plan"

**Answer**: B, C

**Explanation**:
Option B is incorrect: `-target` includes the targeted resource **and all of its dependencies** — resources that the target depends on are also planned because Terraform must resolve the full dependency chain to safely plan the targeted resource. Excluding dependencies would produce an invalid plan. Option C is incorrect: HashiCorp explicitly discourages routine use of `-target` in production. It is intended for exceptional circumstances (e.g., breaking a circular dependency or recovering from a partial failure), not standard workflows. Using it routinely can cause the state to diverge from the intended configuration. Options A and D are both correct descriptions.

---

### Question 6 — `terraform graph` Output Described as JSON

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Identifying the error in claiming `terraform graph` produces JSON output

**Question**:
A developer writes this shell script step in their documentation:

```bash
# Generate a dependency graph in JSON format and pipe it to jq for processing
terraform graph | jq '.'
```

What is the error in this approach?

- A) There is no error — `terraform graph` outputs JSON and can be piped directly to `jq`
- B) The error is that `terraform graph` requires the `-json` flag to produce machine-readable output, just like `terraform show`
- C) The error is that `terraform graph` outputs **DOT format** — a plain-text graph description language used by Graphviz — not JSON; piping it to `jq` will fail because DOT text is not valid JSON
- D) The error is that `terraform graph` outputs XML and must be converted to JSON before processing

**Answer**: C

**Explanation**:
`terraform graph` produces output in **DOT language** — a plain-text format understood by Graphviz for rendering directed graphs. DOT output looks like `digraph { ... }` with node and edge declarations, which is structurally incompatible with JSON. Piping it to `jq` will produce a parse error. The standard usage is `terraform graph | dot -Tsvg > graph.svg` to render the dependency graph as an SVG image using the Graphviz `dot` tool.

---

### Question 7 — `terraform destroy` Claimed to Delete the State File

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Identifying the error in claiming `terraform destroy` removes the state file after execution

**Question**:
An engineer documents a cleanup procedure:

> "After running `terraform destroy` to remove all cloud resources, Terraform also deletes the `terraform.tfstate` file since there is nothing left to track — this keeps the working directory clean."

What is the error in this documentation?

- A) There is no error — `terraform destroy` removes all resources and then deletes `terraform.tfstate`
- B) The error is that `terraform destroy` deletes `terraform.tfstate.backup` but not `terraform.tfstate`
- C) The error is that `terraform destroy` **does not delete the state file** — after all resources are destroyed, `terraform.tfstate` remains on disk but contains an empty resources list; the state file records that no resources are currently managed
- D) The error is that `terraform destroy` always leaves one backup copy of `terraform.tfstate` per resource destroyed

**Answer**: C

**Explanation**:
`terraform destroy` updates the state file to reflect that all managed resources have been removed — it does not delete `terraform.tfstate`. After a successful destroy, the state file exists on disk but contains an empty (or near-empty) resources array, indicating that no infrastructure is currently tracked. This behaviour is intentional: preserving the state file means the backend configuration and workspace context remain intact for future use, even if no resources are currently managed.

---

### Question 8 — `terraform apply` Without Saved Plan Claimed to Guarantee Reviewed Changes

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Identifying the error in claiming `terraform apply` without a plan file applies exactly what `terraform plan` showed

**Question**:
A team's deployment procedure states:

> "Step 1: Run `terraform plan` and review the output carefully. Step 2: Run `terraform apply`. This guarantees that exactly the changes shown in Step 1 will be applied — no more, no fewer."

What is the error in this procedure?

- A) There is no error — `terraform apply` always applies exactly the changes shown by the most recent `terraform plan`
- B) The error is that `terraform apply` must be run before `terraform plan` in the correct workflow order
- C) The error is that `terraform apply` without a saved plan file **re-runs the plan internally** at apply time — if infrastructure has changed between the plan and apply steps, the applied changes may differ from what was reviewed; to guarantee the exact plan is applied, use `terraform plan -out=file` followed by `terraform apply file`
- D) The error is that `terraform plan` output is only valid for 60 seconds — after that, `terraform apply` automatically refreshes and re-plans

**Answer**: C

**Explanation**:
`terraform apply` without a saved plan file performs an **implicit plan** at apply time, right before requesting confirmation. If any infrastructure changed between the explicit `terraform plan` in Step 1 and the apply in Step 2 — due to a concurrent change, a manual modification, or a resource timing issue — the implicit plan will reflect the updated state, potentially differing from what was reviewed. The only way to guarantee that the exact reviewed plan is applied is to save the plan with `terraform plan -out=release.tfplan` and apply it with `terraform apply release.tfplan`.

---

### Question 9 — `terraform fmt` Claimed to Recurse by Default

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Identifying the error in claiming `terraform fmt` includes subdirectories without a flag

**Question**:
A documentation page states:

> "`terraform fmt` automatically formats all `.tf` files in the current directory **and all subdirectories** recursively. No additional flags are needed for a multi-module repository where modules live in subdirectories."

What is the error in this statement?

- A) There is no error — `terraform fmt` recurses into subdirectories by default
- B) The error is that `terraform fmt` can only format a single file at a time — the directory scope requires a separate tool
- C) The error is that `terraform fmt` **only processes `.tf` files in the current directory by default** — it does not recurse into subdirectories unless the `-recursive` flag is explicitly provided; for a multi-module repository, `terraform fmt -recursive` is required to format all modules
- D) The error is that `terraform fmt` does not support subdirectories at all, even with `-recursive`

**Answer**: C

**Explanation**:
`terraform fmt` without flags scans and formats `.tf` files in the **current working directory only**. Subdirectories are ignored unless the `-recursive` flag is provided. In a typical Terraform repository where modules reside in subdirectories (e.g., `modules/networking/`, `modules/compute/`), running `terraform fmt` from the root would leave module files unformatted. The correct command to format an entire repository is `terraform fmt -recursive` run from the repository root.

---

### Question 10 — Wrong Conditions Claimed to Require `terraform init` Re-run

**Difficulty**: Medium
**Answer Type**: many
**Topic**: Identifying TWO conditions incorrectly listed as requiring `terraform init` to be re-run

**Question**:
A team's wiki lists five actions that it claims require re-running `terraform init`. Which TWO are **incorrectly** listed as requiring a re-run? (Select two.)

- A) Adding a new provider to `required_providers` in `main.tf`
- B) Adding a new `output` block to an existing module that the root configuration already sources
- C) Changing the `backend` block from local to a remote S3 backend
- D) Updating the `default` value of an existing `variable` block in `variables.tf`

**Answer**: B, D

**Explanation**:
`terraform init` must be re-run when: a new provider plugin needs to be downloaded (A), the backend configuration changes (C), or a new module source is added. **Adding an `output` block** (B) and **changing a variable's `default` value** (D) are purely configuration changes — they do not affect provider plugins, backend configuration, or module sources. No plugin download or backend reconfiguration is required, so `terraform init` does not need to be re-run for either of these changes.

---

### Question 11 — `terraform console` Claimed to Modify State

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Identifying the error in claiming `terraform console` writes to the state file when expressions are evaluated

**Question**:
An engineer warns their team:

> "Be careful when using `terraform console` interactively — if you evaluate an expression that references a managed resource, Terraform may update that resource's state entry as a side effect. Always use a read-only state backend when running `terraform console` in production."

What is the error in this warning?

- A) There is no error — `terraform console` can trigger state updates when resource attributes are evaluated
- B) The error is that `terraform console` requires a writable state backend to function correctly
- C) The error is that `terraform console` is a **read-only REPL** — it evaluates HCL expressions and functions against the current configuration and state without modifying state, without making any provider API calls, and without triggering any resource changes; it is completely safe to run in any environment
- D) The error is that `terraform console` only reads from local state files — it cannot evaluate expressions referencing resources in a remote backend

**Answer**: C

**Explanation**:
`terraform console` is a purely read-only interactive session. It evaluates HCL expressions and built-in functions (e.g., `length()`, `format()`, `toset()`) against the current configuration and state, but it never writes to the state file or makes any provider API calls. No resource changes occur regardless of what expressions are evaluated. The warning is factually incorrect and creates unnecessary fear about using a safe and useful debugging tool. `terraform console` can safely be used in any environment, including those connected to production remote backends.

---

### Question 12 — `terraform plan` Run Before `terraform init`

**Difficulty**: Hard
**Answer Type**: one
**Topic**: Identifying the error in a workflow that runs `terraform plan` before `terraform init`

**Question**:
A new developer proposes this workflow for reviewing changes:

> "To quickly preview what Terraform would do without committing to downloading providers, run `terraform plan` first. Terraform will automatically infer the required providers from the configuration and generate a preview plan. Once you're satisfied, run `terraform init` to download the providers, then `terraform apply` to execute."

What is the error in this proposed workflow?

- A) There is no error — `terraform plan` can generate a preview plan before providers are downloaded
- B) The error is only cosmetic — `terraform plan` before `terraform init` is valid but produces a warning that providers are not yet downloaded
- C) The error is that `terraform plan` requires a **fully initialised working directory** — providers must already be downloaded and the backend must be configured before `plan` can execute; running `plan` before `init` returns an error such as "This configuration has not been initialized" and no plan is generated
- D) The error is only relevant for remote backends — for local state, `terraform plan` can run before `terraform init`

**Answer**: C

**Explanation**:
`terraform init` is a prerequisite for every other Terraform workflow command. It downloads provider plugins to `.terraform/`, configures the backend, and caches module sources. `terraform plan` cannot execute without provider binaries present — it needs the provider plugins to determine resource schemas, validate configuration, and compute the diff between desired and actual state. Running `plan` before `init` fails with an error indicating the directory is not initialized. The correct workflow is always: `init` → `fmt` → `validate` → `plan` → `apply`.

---

### Question 13 — Wrong Claims About `terraform apply -replace` and `terraform taint`

**Difficulty**: Hard
**Answer Type**: many
**Topic**: Identifying TWO errors in claims comparing `terraform apply -replace` with `terraform taint`

**Question**:
A blog post makes four claims about `terraform apply -replace` and `terraform taint`. Which TWO contain errors? (Select two.)

- A) "`terraform taint` was deprecated in favour of `terraform apply -replace`, which is the recommended approach for forcing resource replacement in Terraform 1.x"
- B) "`terraform apply -replace` requires a configuration change to the targeted resource — if the configuration is unchanged, the command has no effect and Terraform skips the replacement"
- C) "Running `terraform apply -replace=<address>` causes the plan output to show a `-/+` symbol for the targeted resource, indicating destroy-then-recreate"
- D) "`terraform apply -replace` can only be used in conjunction with `terraform plan -out` — the saved plan file is required to invoke the replace behaviour"

**Answer**: B, D

**Explanation**:
Option B is incorrect: `terraform apply -replace` forces replacement **regardless of whether the configuration has changed**. Its entire purpose is to trigger a destroy-then-recreate cycle even when the HCL definition is identical to the last applied state — for example, to recover a corrupted or unhealthy resource. Option D is incorrect: `-replace` does not require a saved plan file; it is an inline flag passed directly to `terraform apply` (or `terraform plan`) and works without any prior `-out` step. Options A and C are both correct: `terraform taint` is deprecated and `-replace` is the modern equivalent that produces a `-/+` plan symbol.

---

---

## Questions

---

### Question 1 — `data` Block Claimed to Create Resources

**Difficulty**: Easy
**Answer Type**: one
**Topic**: Identifying the error in claiming a `data` block provisions infrastructure

**Question**:
A developer comments on a pull request:

> "Adding `data "aws_vpc" "existing" { id = "vpc-0abc12345" }` to my configuration will look up the VPC **and** add it to the Terraform state file as a managed resource — just like a `resource` block would, except Terraform won't destroy it on `terraform destroy`."

What is the error in this comment?

- A) There is no error — a `data` block creates a resource just like a `resource` block, but with destroy protection
- B) The error is that `data` blocks require a `provider` meta-argument to be explicitly set; without one, the lookup cannot succeed
- C) The error is that a `data` block **never creates or manages resources** — it performs a read-only query against the provider API to retrieve information about an already-existing object; no resource is provisioned and the result is not added to state as a managed resource
- D) The error is that `id` is not a valid filter argument inside a `data "aws_vpc"` block — VPCs must be looked up by `cidr_block`

**Answer**: C

**Explanation**:
A `data` block (data source) is read-only — it queries the provider API for information about an existing object and exposes its attributes for use in the configuration. It does not create, update, or destroy any cloud resource, and the queried object is not tracked in state as a managed resource. Only `resource` blocks define infrastructure that Terraform creates and manages. The comparison to a `resource` block with destroy protection is fundamentally wrong.

---

### Question 2 — `create_before_destroy` Described as the Default Behaviour

**Difficulty**: Easy
**Answer Type**: one
**Topic**: Identifying the error in claiming Terraform's default replacement order is create-then-destroy

**Question**:
A team's onboarding guide states:

> "When Terraform replaces a resource — for example, because an immutable attribute was changed — it creates the new resource first and only destroys the old one after the replacement is ready. This create-before-destroy strategy is Terraform's default behaviour. You can disable it by setting `create_before_destroy = false` in the `lifecycle` block."

What is the error in this guide?

- A) There is no error — Terraform always creates the replacement before destroying the original
- B) The error is that `create_before_destroy = false` is not a valid value; the argument is boolean and only `true` is accepted
- C) The error is that **Terraform's default replacement order is destroy-first, then create** — the original resource is destroyed before the replacement is provisioned; `create_before_destroy = true` must be explicitly set in the `lifecycle` block to reverse this order and avoid downtime
- D) The error is that `create_before_destroy` applies to all resource operations, not just replacements — it affects creates and updates as well

**Answer**: C

**Explanation**:
By default, when a resource must be replaced (e.g., changing the `ami` on an EC2 instance), Terraform destroys the old resource first and then creates the new one. This destroy-before-create default can cause downtime for resources that serve live traffic. Setting `create_before_destroy = true` in the `lifecycle` block reverses the order — the replacement is created first, and only after it succeeds is the old resource destroyed. The guide has the default behaviour backwards.

---

### Question 3 — `count` and `for_each` Claimed Usable Together

**Difficulty**: Medium
**Answer Type**: many
**Topic**: Identifying TWO errors in claims about the `count` and `for_each` meta-arguments

**Question**:
A wiki article makes four claims about Terraform meta-arguments. Which TWO contain errors? (Select two.)

- A) "A resource block can use both `count` and `for_each` simultaneously — `count` controls how many copies exist while `for_each` provides a named key for each copy, allowing combined matrix-style resource creation"
- B) "With `count = 3`, the valid values of `count.index` are 0, 1, and 2 — indexing starts at zero, so the third instance has `count.index = 2`"
- C) "`for_each` accepts a plain `list(string)` value directly, without requiring any type conversion — Terraform iterates over the list elements natively"
- D) "When `for_each` is assigned a `map`, `each.key` holds the map key and `each.value` holds the corresponding map value for each iteration"

**Answer**: A, C

**Explanation**:
Option A is incorrect: `count` and `for_each` are **mutually exclusive** meta-arguments — they cannot be used on the same resource block. Using both causes a validation error. Option C is incorrect: `for_each` requires a `set(string)` or `map` value — it does not accept a plain `list`. A list must be converted first with `toset([...])` for a set or wrapped in a `tomap()` call for map-style iteration. Options B and D are both correct descriptions of `count.index` and `for_each` map behaviour.

---

### Question 4 — Implicit Dependency Described as Requiring `depends_on`

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Identifying the error in claiming `depends_on` is required for attribute-reference dependencies

**Question**:
During a code review, an engineer comments:

> "This configuration has a bug — `aws_instance.web` sets `subnet_id = aws_subnet.public.id`, but there's no `depends_on = [aws_subnet.public]` in the instance block. Without an explicit `depends_on`, Terraform has no way to know the subnet must be created first and may attempt to create the instance before the subnet exists."

What is the error in this review comment?

- A) There is no error — `depends_on` is always required when one resource references another resource's attribute
- B) The error is that `depends_on` must reference the VPC, not the subnet — Terraform only traces dependencies one level deep
- C) The error is that **Terraform automatically detects implicit dependencies through attribute references** — because `aws_instance.web` uses `aws_subnet.public.id` as an argument value, Terraform infers that the subnet must be created first without any explicit `depends_on`; adding it here is unnecessary and reduces parallelism
- D) The error is that dependency ordering is only enforced during `terraform destroy`, not `terraform apply`

**Answer**: C

**Explanation**:
Terraform builds a dependency graph by scanning resource attribute references. When `aws_instance.web` uses `aws_subnet.public.id`, Terraform detects the reference and automatically adds a dependency edge: the subnet must be created (and its `id` known) before the instance can be created. This is called an **implicit dependency**. `depends_on` is reserved for dependencies that cannot be expressed through attribute references — typically IAM policy attachments or other side-effects that Terraform cannot detect. Using `depends_on` unnecessarily introduces serialisation that limits Terraform's ability to run operations in parallel.

---

### Question 5 — `prevent_destroy` Claimed to Block `terraform state rm`

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Identifying the error in claiming `prevent_destroy` protects against `terraform state rm`

**Question**:
A senior engineer tells their team:

> "I've added `lifecycle { prevent_destroy = true }` to our production RDS instance. This is a complete safeguard — nobody can remove this resource from Terraform management through `terraform destroy`, a `terraform apply` that would replace it, **or** `terraform state rm`. It's the last line of defence against any accidental deletion."

What is the error in this claim?

- A) There is no error — `prevent_destroy = true` blocks all mechanisms that could remove the resource from Terraform management
- B) The error is that `prevent_destroy` does not block `terraform apply` replacements — it only prevents `terraform destroy`
- C) The error is that `prevent_destroy = true` **only prevents plan-time operations** that would destroy the resource (such as `terraform destroy` or config-driven replacements) — it does **not** protect against `terraform state rm`, which directly manipulates the state file and completely bypasses lifecycle hooks
- D) The error is that `prevent_destroy` requires a remote backend to function — it has no effect when state is stored locally

**Answer**: C

**Explanation**:
`prevent_destroy = true` causes Terraform to raise an error during the **plan** phase if any plan would destroy the resource — this blocks both `terraform destroy` and replacements triggered by configuration changes. However, `terraform state rm` operates **directly on the state file** and bypasses all plan-phase checks including lifecycle hooks. Running `terraform state rm aws_db_instance.prod` removes the resource from state without triggering any lifecycle evaluation, leaving the actual RDS instance running but unmanaged by Terraform. The engineer's claim that `prevent_destroy` is a complete safeguard is incorrect.

---

### Question 6 — `ignore_changes` Claimed to Hide Resource from `terraform plan`

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Identifying the error in claiming `ignore_changes = all` makes a resource invisible to plan

**Question**:
A team documents their use of `ignore_changes`:

> "We've applied `lifecycle { ignore_changes = all }` to our Auto Scaling Group. This makes the resource completely invisible to `terraform plan` — it won't appear in plan output at all, and Terraform treats it as unmanaged going forward."

What is the error in this documentation?

- A) There is no error — `ignore_changes = all` removes the resource from Terraform's awareness entirely
- B) The error is that `ignore_changes = all` is invalid syntax — the `all` keyword is not accepted; individual attribute names must be listed
- C) The error is that `ignore_changes = all` **does not hide the resource from plan or remove it from Terraform management** — Terraform still tracks the resource in state, still refreshes its current values, and still includes it in the plan; `ignore_changes = all` only means Terraform will not propose changes to update attribute values that have drifted, not that the resource is unmanaged
- D) The error is that `ignore_changes = all` must be combined with `prevent_destroy = true` to suppress all plan output for a resource

**Answer**: C

**Explanation**:
`ignore_changes = all` instructs Terraform to skip drift-based update proposals for all attributes of the resource — if the real-world state differs from the configuration, Terraform notes the difference but does not propose an update plan. The resource is still fully tracked in state, still refreshed during `terraform plan`, and still visible in plan output (for example, if a replacement is triggered by something outside `ignore_changes` scope). It does **not** make the resource unmanaged or invisible. To stop managing a resource entirely, the `removed` block with `lifecycle { destroy = false }` should be used instead.

---

### Question 7 — `count.index` Starting Value Claimed as 1

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Identifying the error in a comment claiming `count.index` starts at 1

**Question**:
A developer adds this comment to their configuration:

```hcl
resource "aws_instance" "worker" {
  count         = 3
  ami           = "ami-0abc123"
  instance_type = "t3.micro"

  tags = {
    # count.index starts at 1 for the first instance
    Name = "worker-${count.index}"  # produces: "worker-1", "worker-2", "worker-3"
  }
}
```

What is the error in this comment?

- A) There is no error — `count.index` begins at 1, so with `count = 3` the tag values are `"worker-1"`, `"worker-2"`, and `"worker-3"`
- B) The error is that `count.index` cannot be used inside a `tags` block — it is only valid in top-level resource arguments such as `ami` or `instance_type`
- C) The error is that `count.index` **starts at 0**, not 1 — with `count = 3`, the three instances have `count.index` values of 0, 1, and 2, producing tag values `"worker-0"`, `"worker-1"`, and `"worker-2"`, not `"worker-1"`, `"worker-2"`, `"worker-3"`
- D) The error is that `count.index` returns a floating-point number by default and must be converted to a string with `tostring()` before use in string interpolation

**Answer**: C

**Explanation**:
`count.index` is zero-based — the first instance has index 0, the second has index 1, and so on. With `count = 3`, the valid index values are 0, 1, and 2. The comment incorrectly documents the tag values as `"worker-1"` through `"worker-3"`. The actual tags produced are `"worker-0"`, `"worker-1"`, and `"worker-2"`. This is a common off-by-one misconception, especially for engineers accustomed to 1-based indexing in other tools.

---

### Question 8 — Wrong Claims About `depends_on` on a Data Source

**Difficulty**: Medium
**Answer Type**: many
**Topic**: Identifying TWO errors in claims about adding `depends_on` to a `data` block

**Question**:
A team wiki makes four claims about the following data source configuration:

```hcl
data "aws_s3_objects" "uploads" {
  bucket     = "my-app-uploads"
  depends_on = [aws_iam_role_policy.app_s3]
}
```

Which TWO claims contain errors? (Select two.)

- A) "Adding `depends_on` to a `data` block is invalid HCL syntax — only `resource` blocks support `depends_on`; using it inside a `data` block causes a validation error"
- B) "When `depends_on` is added to a data source, the data source read is deferred from the plan phase to the apply phase, even when no computed values are involved"
- C) "Adding `depends_on` to a data source with empty results will cause the data source to return `null` on every subsequent plan, permanently breaking the configuration"
- D) "`depends_on` on the data source ensures that `aws_iam_role_policy.app_s3` is fully created or updated before the data source queries the provider API"

**Answer**: A, C

**Explanation**:
Option A is incorrect: `depends_on` is valid on `data` blocks — it is a supported meta-argument for both `resource` and `data` blocks. Option C is incorrect: adding `depends_on` does not cause the data source to return `null` results permanently; it simply defers the read to the apply phase, where the data source queries the provider normally after the dependency is resolved. Options B and D are both accurate: `depends_on` on a data source does defer the read to apply (even with fully known values), and it ensures the listed dependency is applied before the query runs.

---

### Question 9 — Resource `id` Attribute Claimed to Be User-Defined

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Identifying the error in claiming the `id` attribute of a managed resource can be set in HCL

**Question**:
A new team member asks how to reference the ID of `aws_instance.web`. A colleague responds:

> "Just add `id = "my-custom-instance-id"` to the `aws_instance.web` resource block in your HCL. Terraform will use that string as the resource's ID in both state and the cloud, and you can then reference it as `aws_instance.web.id` in other resources."

What is the error in this response?

- A) There is no error — the `id` argument can be set in any resource block to provide a stable identifier
- B) The error is that `id` can be set on `data` blocks but not on `resource` blocks
- C) The error is that the `id` attribute of a managed resource is a **read-only value assigned by the cloud provider** after the resource is created — it cannot be set in the resource block configuration; Terraform stores the provider-assigned ID in state, where it can be referenced as `aws_instance.web.id`
- D) The error is that `id` is a reserved keyword in Terraform HCL and will cause a parse error if used as an argument name in any block type

**Answer**: C

**Explanation**:
The `id` attribute is a **computed** value — it is assigned by the cloud provider (e.g., AWS assigns an instance ID like `i-0abc1234def`) when the resource is created and stored in state by Terraform. It cannot be set or overridden in the HCL configuration; Terraform does not expose it as a settable argument. After apply, `aws_instance.web.id` reads the provider-assigned value from state. Attempting to add `id = "custom-value"` to most resource blocks will produce a validation error because `id` is not a valid configurable argument for those resource types.

---

### Question 10 — `for_each` with a `list(string)` Variable

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Identifying the error in using a list-type variable directly with `for_each`

**Question**:
A developer writes the following configuration and claims it is valid:

```hcl
variable "regions" {
  type    = list(string)
  default = ["us-east-1", "us-west-2", "eu-west-1"]
}

resource "aws_s3_bucket" "regional" {
  for_each = var.regions
  bucket   = "data-${each.value}"
}
```

What is the error in this configuration?

- A) There is no error — `for_each` natively accepts a `list(string)` variable and iterates over its elements
- B) The error is that `var.regions` must be wrapped in `tomap()` before it can be used with `for_each`
- C) The error is that `for_each` **does not accept a `list` type** — it requires a `set(string)` or `map`; the correct fix is `for_each = toset(var.regions)` to convert the list to a set before iterating
- D) The error is that `each.value` is the wrong reference when iterating a variable — `each.key` must be used instead

**Answer**: C

**Explanation**:
`for_each` accepts only `set(string)` or `map` types — passing a `list(string)` directly causes a validation error because lists allow duplicate values and have a defined order, which conflicts with `for_each`'s requirement for stable, unique keys. The fix is to convert the list with `toset(var.regions)`, which deduplicates the values and creates a set that `for_each` can iterate. When iterating a set, `each.key` and `each.value` both refer to the current set element (e.g., `"us-east-1"`).

---

### Question 11 — `depends_on` Claimed to Override Lifecycle Hooks

**Difficulty**: Hard
**Answer Type**: one
**Topic**: Identifying the error in claiming `depends_on` can override `prevent_destroy`

**Question**:
An engineer explains to a junior colleague:

> "The `depends_on` meta-argument doesn't just control creation order — it can also override lifecycle protections. If resource B has `depends_on = [resource_A]`, and resource A needs to be destroyed, Terraform will temporarily bypass `prevent_destroy = true` on resource B to satisfy the dependency chain. This is how Terraform handles cascading destroys."

What is the error in this explanation?

- A) There is no error — `depends_on` does override `prevent_destroy` when cascading destroy operations require it
- B) The error is that `depends_on` only affects destroy ordering — it has no effect on create ordering
- C) The error is that `depends_on` **controls execution ordering only** — it has no effect on lifecycle hooks whatsoever; `prevent_destroy = true` continues to block any plan that would destroy the protected resource regardless of `depends_on` relationships; lifecycle hooks and dependency ordering are entirely independent mechanisms in Terraform's execution model
- D) The error is that `depends_on` cannot reference resources in different modules — it is only valid between resources declared in the same configuration file

**Answer**: C

**Explanation**:
`depends_on` affects the **order** in which resource operations are executed — it tells Terraform which resources must be applied or destroyed before others. Lifecycle hooks (`prevent_destroy`, `create_before_destroy`, `ignore_changes`, `replace_triggered_by`) are orthogonal controls that govern **how** operations are performed. They are completely independent mechanisms. `prevent_destroy = true` will raise a plan-time error on any destroy operation — no `depends_on` relationship overrides this. If Terraform needs to destroy resource B to satisfy a dependency chain but B has `prevent_destroy = true`, the plan fails with an error, and the engineer must manually remove `prevent_destroy` before the operation can proceed.

---

### Question 12 — Wrong Claims About the `removed` Block

**Difficulty**: Hard
**Answer Type**: many
**Topic**: Identifying TWO errors in claims about the `removed` block's behaviour

**Question**:
A Terraform 1.7+ runbook makes four claims about the `removed` block. Which TWO contain errors? (Select two.)

- A) "The `removed` block with `lifecycle { destroy = false }` stops Terraform from managing the resource but leaves the real cloud resource running and unaffected in the provider account"
- B) "A `removed` block with `lifecycle { destroy = false }` deletes both the Terraform state entry **and** the real cloud resource — the `destroy = false` setting only suppresses the interactive confirmation prompt before deletion"
- C) "After `terraform apply` successfully processes a `removed` block, the block must remain in the configuration permanently to prevent future `terraform plan` runs from flagging the resource address as unknown and attempting to recreate it"
- D) "After `terraform apply` processes a `removed` block, the block can be safely deleted from the configuration — subsequent plans will not attempt to recreate or re-manage the resource because it is no longer in state"

**Answer**: B, C

**Explanation**:
Option B is incorrect: `lifecycle { destroy = false }` instructs Terraform to remove the resource from state **without** destroying the real cloud resource — the cloud resource continues to run unmanaged. The `destroy = false` flag controls whether the actual infrastructure is deleted, not whether a confirmation prompt is shown. Option C is incorrect: the `removed` block only needs to be present for the transitional apply that removes the resource from state; once apply succeeds and the resource is no longer in state, the `removed` block has served its purpose and should be deleted. Future plans will simply not reference the resource. Options A and D are both accurate descriptions of the `removed` block's behaviour.

---

### Question 13 — `replace_triggered_by` Claimed to Work on Data Sources

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Identifying the error in claiming `replace_triggered_by` is valid in a `data` block's `lifecycle`

**Question**:
A developer proposes adding the following to a data source to ensure it re-reads when an IAM role changes:

```hcl
data "aws_iam_policy_document" "app" {
  statement {
    actions   = ["s3:GetObject"]
    resources = ["arn:aws:s3:::my-bucket/*"]
  }

  lifecycle {
    replace_triggered_by = [aws_iam_role.app]
  }
}
```

The developer claims: "`replace_triggered_by` in the `lifecycle` block will force this data source to be re-read whenever `aws_iam_role.app` changes."

What is the error in this configuration and claim?

- A) There is no error — `replace_triggered_by` is valid in the `lifecycle` block of both `resource` and `data` blocks
- B) The error is only in the reference syntax — `replace_triggered_by` inside a `data` block must use `data.` prefix references, not resource addresses
- C) The error is that `lifecycle` blocks — and all lifecycle meta-arguments including `replace_triggered_by` — are **not supported on `data` blocks**; lifecycle meta-arguments only apply to `resource` blocks; data sources are re-evaluated based on their argument values and dependency changes, not lifecycle hooks
- D) The error is that `replace_triggered_by` requires a list of attribute references (e.g., `aws_iam_role.app.arn`), not full resource addresses

**Answer**: C

**Explanation**:
`lifecycle` blocks are a `resource`-only feature in Terraform — they cannot be placed inside a `data` block. All four lifecycle meta-arguments (`create_before_destroy`, `prevent_destroy`, `ignore_changes`, and `replace_triggered_by`) are exclusive to `resource` blocks. Adding a `lifecycle` block to a `data` block causes a validation error. Data sources are re-evaluated during plan or apply based on their argument values and any `depends_on` declarations — not through lifecycle triggers. The correct way to ensure a data source re-reads after a related resource changes is to use `depends_on = [aws_iam_role.app]` in the `data` block, which defers the read to the apply phase.

---

---

## Questions

---

### Question 1 — Flawed Claim: `default` Sets the Type

**Difficulty**: Easy
**Answer Type**: one
**Topic**: What `default` does vs what `type` does in a variable block

**Question**:
A colleague makes the following claim:

> "Setting a `default` value on a variable is all you need — it both makes the variable optional and automatically infers its type constraint, so you never need a separate `type` argument."

What is wrong with this claim?

- A) Nothing is wrong — `default` does make the variable optional and Terraform does infer the type from it
- B) The claim is wrong about type inference: Terraform does infer the type from the default, but the variable is still required
- C) The claim is wrong about type constraints: while `default` does make the variable optional, Terraform does **not** enforce a type constraint based on the default — an explicit `type` argument is needed to validate that callers provide the correct type
- D) The claim is wrong because `default` values are ignored if a `type` constraint is also declared

**Answer**: C

**Explanation**:
`default` does make a variable optional — if no value is provided through any input mechanism, the default is used. However, Terraform does not enforce a strict type constraint based solely on the default value. Without an explicit `type` argument, a caller could supply a value of a different type (e.g., pass a number to a variable whose default is a string). The `type` argument is what enforces type validation; `default` only controls whether the variable is required. Both serve distinct purposes and should be declared separately.

---

### Question 2 — Flawed Claim: `sensitive = true` Encrypts State

**Difficulty**: Easy
**Answer Type**: one
**Topic**: What `sensitive = true` on a variable actually does vs does not do

**Question**:
A new engineer reads the documentation and concludes:

> "If I set `sensitive = true` on a variable, its value will be encrypted in `terraform.tfstate`, so I don't need to worry about securing the state file."

Which part of this conclusion is incorrect?

- A) The conclusion is correct — `sensitive = true` causes Terraform to encrypt the value before writing it to state
- B) The conclusion is incorrect — `sensitive = true` hides the value in terminal output but the value is still stored in **plaintext** in the state file; securing the state file is still required
- C) The conclusion is incorrect — `sensitive = true` prevents the value from being stored in state at all
- D) The conclusion is incorrect — `sensitive = true` only applies to output blocks, not variable blocks

**Answer**: B

**Explanation**:
`sensitive = true` on a variable causes Terraform to redact the value from terminal output during `plan` and `apply`, displaying `(sensitive value)` instead. It does **not** encrypt or omit the value from `terraform.tfstate` — the plaintext value is written to state like any other attribute. Anyone with read access to the state file can view sensitive variable values. Protecting sensitive data at rest requires using an encrypted remote backend (such as HCP Terraform or an S3 bucket with server-side encryption).

---

### Question 3 — Flawed Claim: Locals Are Evaluated at Apply Time Only

**Difficulty**: Easy
**Answer Type**: one
**Topic**: When `locals` are evaluated in the Terraform workflow

**Question**:
An engineer explains to a junior colleague:

> "Locals in Terraform are lazy — they're only evaluated during `terraform apply`, not during `terraform plan`. This means a local that references an unknown resource attribute won't cause any issues at plan time."

What is wrong with this explanation?

- A) Nothing — locals are indeed evaluated only at apply time
- B) The explanation is wrong: locals are evaluated during `terraform plan` as well; if a local references a known value it resolves at plan time, and if it references an unknown value the local itself becomes unknown (shown as `(known after apply)`) but no error is raised for that reason alone
- C) The explanation is wrong: locals are evaluated at `terraform init` time, before plan or apply
- D) The explanation is wrong: locals that reference resource attributes cause an immediate error at plan time, regardless of whether the value is known

**Answer**: B

**Explanation**:
Terraform evaluates `locals` during the planning phase, not exclusively at apply time. When a local references a value that is already known (such as a variable default or a static string), it is fully resolved during plan. When a local references an attribute that will only be known after resource creation (such as `aws_instance.web.id`), the local's value is shown as `(known after apply)` in the plan — not deferred silently. This means plan output accurately reflects which values are computed and which are still unknown, which is important for understanding dependency chains.

---

### Question 4 — Flawed Claim: `output sensitive = true` Removes Value from State

**Difficulty**: Medium
**Answer Type**: one
**Topic**: What `sensitive = true` on an output block does vs does not do

**Question**:
A configuration has the following output:

```hcl
output "db_password" {
  value     = aws_db_instance.main.password
  sensitive = true
}
```

A developer claims: "Setting `sensitive = true` on this output removes the password from Terraform state, so the state file is safe to store unencrypted."

What is wrong with this claim?

- A) Nothing — `sensitive = true` on an output block does remove the value from state
- B) The claim is wrong: `sensitive = true` on an output only suppresses the value in terminal display; the underlying resource attribute (`aws_db_instance.main.password`) is still stored in plaintext in state as part of the resource's own attributes
- C) The claim is wrong: `sensitive = true` on an output causes an error during apply because passwords cannot be exposed as outputs
- D) The claim is wrong: `sensitive = true` only affects `terraform output` commands; it has no effect on `terraform apply` output

**Answer**: B

**Explanation**:
`sensitive = true` on an output block suppresses the value from being displayed in `terraform apply` summary and in `terraform output` (all outputs listing). However, it does not remove the value from the state file — the resource attribute `aws_db_instance.main.password` is written to state as part of the resource's tracked attributes, independent of any output declaration. The output block itself also stores the value reference in state. Encrypting the state backend is always required when sensitive data is managed by Terraform.

---

### Question 5 — Flawed Variable Precedence Order

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Correct ordering of variable input precedence (highest to lowest)

**Question**:
A team's internal wiki documents the following variable input precedence order (highest to lowest):

> 1. `terraform.tfvars` (auto-loaded)
> 2. `*.auto.tfvars` files
> 3. `TF_VAR_*` environment variables
> 4. `-var` CLI flag
> 5. `default` in the variable block

Which error does this list contain?

- A) `terraform.tfvars` should be above `*.auto.tfvars`
- B) The `-var` CLI flag and `TF_VAR_*` environment variables are listed in the wrong order — `-var` has the highest precedence and both are above `.tfvars` files; the list also incorrectly places `.tfvars` files above environment variables
- C) `default` in the variable block should be listed first (highest priority)
- D) There are no errors — this is the correct precedence order

**Answer**: B

**Explanation**:
The correct Terraform variable precedence from highest to lowest is: (1) CLI `-var` flag and `TF_VAR_*` environment variables — these are at the **same** highest level and both outrank all file-based sources; (2) `*.auto.tfvars` files; (3) `terraform.tfvars`; (4) `-var-file` flag; (5) `default` in the variable block. The wiki incorrectly ranks `terraform.tfvars` and `*.auto.tfvars` above environment variables and the `-var` flag. In reality, any `TF_VAR_*` environment variable or `-var` flag overrides any `.tfvars` file value.

---

### Question 6 — Flawed Claim: `toset()` Preserves List Order

**Difficulty**: Medium
**Answer Type**: one
**Topic**: What `toset()` does to ordering when converting a list

**Question**:
An engineer writes the following and comments on it:

```hcl
locals {
  regions_list = ["us-east-1", "eu-west-1", "ap-southeast-1"]
  regions_set  = toset(local.regions_list)
}
```

> "I'm using `toset()` here so that `for_each` can iterate over the regions. The set will maintain the same order as my original list — `us-east-1` first, `eu-west-1` second, `ap-southeast-1` third."

What is wrong with this comment?

- A) Nothing — `toset()` preserves insertion order from the source list
- B) The comment is wrong: `toset()` removes duplicates but **does not guarantee ordering** — sets in Terraform are unordered; iteration order over the resulting set is not guaranteed to match the original list order
- C) The comment is wrong: `toset()` converts the list to a map, not a set
- D) The comment is wrong: `toset()` can only be used with `count`, not `for_each`

**Answer**: B

**Explanation**:
Sets in Terraform are **unordered collections** — they do not have a defined element order. `toset()` converts a list to a set, which removes duplicates, but the resulting set does not preserve the original list's order. When `for_each` iterates over a set, the iteration order is not guaranteed to be alphabetical, insertion-order, or any other predictable sequence. If ordering matters, use a list with `count` or rely on stable map keys with `for_each`. The key benefit of `toset()` for `for_each` is stable key-based addressing, not ordering.

---

### Question 7 — Flawed Claim: `for` on a Map Always Produces a List

**Difficulty**: Medium
**Answer Type**: one
**Topic**: What output type a `for` expression produces based on its delimiter

**Question**:
A developer reviewing HCL code states:

> "A `for` expression always produces a list. The outer delimiter is just a style choice — you can use `{...}` or `[...]` interchangeably and always get a list back."

Which of the following best describes the error in this statement?

- A) The statement is correct — `for` expressions always produce lists in Terraform
- B) The statement is wrong: the outer delimiter determines the output type — `[for ...]` (square brackets) produces a **list**, while `{for ... : key => value}` (curly braces with `=>`) produces a **map (object)**; they are not interchangeable
- C) The statement is wrong: `for` expressions always produce maps, not lists
- D) The statement is wrong: `{...}` produces a set, not a map

**Answer**: B

**Explanation**:
The outer delimiter of a `for` expression is not a style choice — it controls the output type. `[for item in collection : expr]` produces a **list**. `{for k, v in collection : key_expr => value_expr}` produces a **map**. These two forms have different syntax requirements (the map form requires the `=>` operator and typically two iteration variables) and produce incompatible types. Using a map output where a list is expected, or vice versa, will cause a type error. The distinction is fundamental to writing correct Terraform expressions.

---

### Question 8 — Flawed Claim: `lookup()` Default Argument Is Optional

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Whether the default argument to `lookup()` is required or optional

**Question**:
An engineer writes:

```hcl
locals {
  port = lookup(var.service_config, "port")
}
```

And explains: "I don't need to pass a default to `lookup()` — the third argument is optional, so if the key is missing, it just returns `null`."

What is wrong with this explanation?

- A) Nothing — the third argument to `lookup()` is optional and returns `null` when omitted
- B) The explanation is wrong: omitting the default from `lookup()` causes Terraform to raise an error if the key is not found; the default argument is required to make the call safe against missing keys
- C) The explanation is wrong: `lookup()` requires exactly four arguments
- D) The explanation is wrong: `lookup()` cannot be used with variables — only with literals

**Answer**: B

**Explanation**:
`lookup(map, key, default)` has a third argument that, while syntactically optional in some Terraform versions, is strongly recommended. When the key does not exist and no default is provided, Terraform raises an error. The safe pattern is always to provide a default value: `lookup(var.service_config, "port", 443)`. Omitting the default and assuming a `null` return is incorrect — Terraform does not silently return `null` for missing keys when `lookup()` is called without a default. Always supply a meaningful fallback to avoid plan-time failures.

---

### Question 9 — Flawed Claim: `merge()` Deep-Merges Nested Maps

**Difficulty**: Medium
**Answer Type**: one
**Topic**: How `merge()` handles nested map keys (shallow vs deep merge)

**Question**:
A developer uses the following to combine configuration maps:

```hcl
locals {
  base = {
    tags = { Environment = "dev", Team = "platform" }
    region = "us-east-1"
  }
  override = {
    tags = { Environment = "production" }
  }
  config = merge(local.base, local.override)
}
```

The developer expects `local.config.tags` to equal `{ Environment = "production", Team = "platform" }` — the `Team` key preserved from `base` and `Environment` overridden. What is wrong with this expectation?

- A) Nothing — `merge()` performs a deep recursive merge, so the `tags` maps are merged together
- B) The expectation is wrong: `merge()` performs a **shallow merge only** — when `override.tags` and `base.tags` share the same top-level key (`"tags"`), the entire `tags` map from `override` replaces the one from `base`; the result is `local.config.tags = { Environment = "production" }` with `Team` lost
- C) The expectation is wrong: `merge()` will raise an error because both maps contain the same top-level key `"tags"`
- D) The expectation is wrong: `merge()` only works on flat maps with string values; nested maps cause a type error

**Answer**: B

**Explanation**:
`merge()` performs a **shallow (top-level) merge only**. When two maps share the same key, the value from the last map wins — the entire value is replaced, not recursively merged. In this example, both `local.base` and `local.override` have a `"tags"` key. The `override` map is the last argument, so its `tags` value (`{ Environment = "production" }`) completely replaces the `base` tags map. The `Team` key is lost because Terraform does not recurse into nested maps to merge them. To achieve deep merging, you would need to explicitly merge the nested maps: `merge(local.base.tags, local.override.tags)`.

---

### Question 10 — Flawed Claim: `nonsensitive()` Permanently Removes Sensitive Marking from State

**Difficulty**: Medium
**Answer Type**: one
**Topic**: What `nonsensitive()` does and does not affect

**Question**:
A developer uses `nonsensitive()` to unwrap a sensitive value before passing it to a resource argument and claims:

> "Once I wrap a value with `nonsensitive()`, Terraform permanently removes the sensitive marking from that value everywhere — including in state and in all downstream references."

What is wrong with this claim?

- A) Nothing — `nonsensitive()` permanently removes the sensitive marking from the value across all contexts
- B) The claim is wrong: `nonsensitive()` only removes the sensitive marking for the **specific expression** where it is used, allowing that value to be displayed in plan output; it does not change how the underlying source (the original sensitive variable or attribute) is marked, and the source value remains sensitive in other contexts
- C) The claim is wrong: `nonsensitive()` is not a valid Terraform function
- D) The claim is wrong: `nonsensitive()` removes the value from state entirely

**Answer**: B

**Explanation**:
`nonsensitive(value)` is a Terraform function that removes the sensitive marking from a value for the purpose of the current expression, allowing it to appear in plan output or be passed to arguments that don't accept sensitive values. It does **not** permanently alter the source variable or attribute's sensitive marking — the original source remains sensitive. Callers of the same sensitive variable elsewhere still see it as sensitive. `nonsensitive()` should be used with care and only when the developer is certain the value is safe to expose; it does not affect state storage.

---

### Question 11 — Flawed Claim: `coalesce()` and `coalescelist()` Are Interchangeable

**Difficulty**: Hard
**Answer Type**: one
**Topic**: Distinguishing `coalesce()` from `coalescelist()` and their input types

**Question**:
An engineer writes the following and explains their reasoning:

```hcl
locals {
  fallback_region = coalesce(var.primary_region, var.secondary_region, "us-east-1")
  fallback_list   = coalesce(var.allowed_ports, [80, 443])
}
```

> "`coalesce()` works for both scalar values and lists — it just returns the first non-null, non-empty value regardless of type."

What is wrong with this code and explanation?

- A) Nothing — `coalesce()` accepts any type including lists
- B) The second usage is wrong: `coalesce()` is designed for **scalar values** (strings, numbers, bools) and returns the first non-null, non-empty string; for returning the first non-empty **list**, `coalescelist()` should be used instead
- C) The first usage is wrong: `coalesce()` only accepts exactly two arguments
- D) Both usages are wrong: `coalesce()` only works with boolean values

**Answer**: B

**Explanation**:
`coalesce(str1, str2, ...)` accepts scalar values and returns the first that is not null and not an empty string. It is designed for string/scalar fallback patterns. `coalescelist(list1, list2, ...)` is the collection counterpart — it accepts lists and returns the first non-empty list. Using `coalesce()` with a list argument (like `[80, 443]`) will cause a type error because `coalesce()` does not accept list inputs. The correct function for the second local is `coalescelist(var.allowed_ports, [80, 443])`.

---

### Question 12 — Flawed Claim: `can()` Returns the Value on Success

**Difficulty**: Hard
**Answer Type**: many
**Topic**: What `can()` returns vs what `try()` returns

**Question**:
A developer writes the following code and makes two claims about it:

```hcl
locals {
  settings = { timeout = 30 }
  a = can(local.settings["timeout"])
  b = try(local.settings["timeout"], 0)
}
```

> **Claim 1**: "`local.a` equals `30` — `can()` evaluates the expression and returns its value when it succeeds."
> **Claim 2**: "`local.b` equals `30` — `try()` evaluates `local.settings["timeout"]` successfully and returns its value."

Which TWO statements correctly identify errors or accuracies in these claims? (Select two.)

- A) Claim 1 is **wrong**: `can(expr)` always returns a **boolean** (`true` if the expression succeeds without error, `false` if it errors) — it never returns the expression's value; `local.a` equals `true`, not `30`
- B) Claim 1 is **correct**: `can()` returns the value of the expression when it succeeds
- C) Claim 2 is **correct**: `try()` evaluates the first expression successfully (`local.settings["timeout"]` = `30`) and returns `30`; the fallback `0` is never used
- D) Claim 2 is **wrong**: `try()` always returns the last fallback argument regardless of whether earlier expressions succeed

**Answer**: A, C

**Explanation**:
`can(expr)` is a predicate function — it always returns a **boolean**. It returns `true` if the expression can be evaluated without error, and `false` if it would error. It never returns the expression's value. Claim 1 incorrectly treats `can()` like `try()`. `try(expr1, fallback)` evaluates each argument in order and returns the **value** of the first one that succeeds without error. Since `local.settings["timeout"]` exists and equals `30`, `try()` returns `30` immediately without needing the fallback. Claim 2 is correct.

---

### Question 13 — Flawed Claim: `length()` on `null` Returns Zero

**Difficulty**: Medium
**Answer Type**: one
**Topic**: What `length()` does when called with a `null` argument

**Question**:
A developer writes:

```hcl
variable "tags" {
  type    = map(string)
  default = null
  nullable = true
}

locals {
  tag_count = length(var.tags)
}
```

The developer claims: "If `var.tags` is `null`, `length()` will safely return `0` — it handles `null` gracefully just like an empty collection."

What is wrong with this claim?

- A) Nothing — `length()` returns `0` for `null` values
- B) The claim is wrong: `length()` does **not** accept `null` — calling `length(null)` raises an error; the developer should guard against null with a conditional expression such as `var.tags != null ? length(var.tags) : 0` or use `try(length(var.tags), 0)`
- C) The claim is wrong: `length()` returns `-1` for `null` values to indicate an undefined collection
- D) The claim is wrong: the `nullable = true` setting prevents `var.tags` from ever being `null`, so the scenario cannot occur

**Answer**: B

**Explanation**:
`length()` requires a non-null string, list, or map argument. Passing `null` to `length()` causes a Terraform error — it does not return `0` or any other default value. When a variable may be `null` (e.g., when `nullable = true` and no default is provided, or when the default is explicitly `null`), callers must guard against null before calling `length()`. Safe patterns include: `var.tags != null ? length(var.tags) : 0` (conditional expression) or `try(length(var.tags), 0)` (using `try()` to catch the error). The `nullable = true` setting explicitly allows `null` values — it does not prevent them.

---

---

## Questions

---

### Question 1 — Flawed Claim: `check` Block Failure Blocks Apply

**Difficulty**: Easy
**Answer Type**: one
**Topic**: Whether a failing `check` block assertion blocks `terraform apply`

**Question**:
A colleague explains the three Terraform condition mechanisms and states:

> "A failed `check` block assertion works just like a failed `precondition` — it blocks `terraform apply` and prevents the infrastructure from being created or modified."

What is wrong with this explanation?

- A) Nothing — `check` block failures and `precondition` failures both block apply
- B) The explanation is wrong: `check` block failures are **warnings only** — they do not block apply; all resources are still created or updated and the apply exits successfully
- C) The explanation is wrong: `check` block failures are more severe than `precondition` failures — they abort the entire Terraform run including `init`
- D) The explanation is wrong: `check` block failures only block apply if they contain a scoped `data` source

**Answer**: B

**Explanation**:
The `check` block is intentionally **non-blocking**. A failing `assert` condition inside a `check` block produces a **warning** message but does not prevent the apply from completing. All resource changes proceed normally and the apply exits with a success status. This is the key design difference from `precondition`, which halts apply before the target resource is modified. `check` blocks are designed for continuous health monitoring where a failure should be surfaced to operators without risking blocked deployments.

---

### Question 2 — Flawed Claim: `validation` Runs During Apply

**Difficulty**: Easy
**Answer Type**: one
**Topic**: When variable `validation` blocks are evaluated in the Terraform workflow

**Question**:
A team's internal wiki states:

> "Variable `validation` blocks run during `terraform apply`, after the operator has reviewed and approved the execution plan. If a variable fails validation at this point, Terraform aborts the apply."

What is wrong with this description?

- A) Nothing — variable validation runs during `terraform apply` after plan approval
- B) The description is wrong: variable `validation` blocks run **before `terraform plan`** — they are evaluated during input variable processing, which happens before any planning; an invalid variable aborts before a plan is ever generated
- C) The description is wrong: variable `validation` blocks only run when explicitly invoked with `terraform validate`
- D) The description is wrong: variable `validation` blocks run at `terraform init` time when providers are registered

**Answer**: B

**Explanation**:
Variable `validation` blocks are evaluated as part of **input variable processing**, which occurs before `terraform plan` generates any execution plan. A validation failure halts Terraform immediately, displaying the `error_message` — no plan is generated, no diff is computed, and no apply can proceed. The team's wiki is incorrect in describing this as a post-plan, apply-time check. This early evaluation is precisely what makes `validation` useful: catching bad inputs before any infrastructure analysis occurs.

---

### Question 3 — Flawed HCL: `validation` Condition References a Local

**Difficulty**: Medium
**Answer Type**: one
**Topic**: What a `validation` block's `condition` is allowed to reference

**Question**:
An engineer writes the following to validate that an environment variable matches an allowed list defined in a local:

```hcl
locals {
  allowed_envs = ["dev", "staging", "production"]
}

variable "environment" {
  type = string

  validation {
    condition     = contains(local.allowed_envs, var.environment)
    error_message = "environment must be one of: dev, staging, production."
  }
}
```

What is wrong with this configuration?

- A) Nothing — a `validation` block can reference any value available in the module
- B) The configuration is wrong: `validation` block conditions can only reference `var.<variable_name>`; referencing `local.allowed_envs` is not permitted and causes a Terraform error
- C) The configuration is wrong: `contains()` cannot be used inside a `validation` block condition
- D) The configuration is wrong: `locals` must be declared after all `variable` blocks in a Terraform file

**Answer**: B

**Explanation**:
A `validation` block's `condition` argument is restricted to referencing only `var.<variable_name>` — the specific variable being validated. This restriction exists because validation runs before planning, when local values, resources, and data sources have not yet been computed. Referencing `local.allowed_envs` inside a validation condition causes Terraform to raise an error about an invalid reference. The correct fix is to inline the list directly: `contains(["dev", "staging", "production"], var.environment)`.

---

### Question 4 — Flawed Claim: `self` Available in `precondition`

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Which lifecycle condition blocks allow use of the `self` reference

**Question**:
An engineer documents lifecycle conditions and writes:

> "`self` is available in both `precondition` and `postcondition` blocks — you can use `self.<attribute>` in either to inspect the resource's current or desired state before or after a change."

What is wrong with this documentation?

- A) Nothing — `self` is available in both `precondition` and `postcondition`
- B) The documentation is wrong: `self` is only available in `postcondition` blocks; `precondition` blocks cannot use `self` because the resource has not yet been created or updated when the precondition is evaluated
- C) The documentation is wrong: `self` is only available in `precondition` blocks; `postcondition` blocks must reference the resource by its full address
- D) The documentation is wrong: `self` is not valid in either block; resource attributes must always be referenced by their full address

**Answer**: B

**Explanation**:
`self` is a special reference that points to the resource instance **after** it has been created or updated. This makes it available only in `postcondition` blocks, where the resource's resulting attributes can be inspected. In a `precondition`, the resource has not yet been modified — there are no new attribute values to reference via `self`. `precondition` conditions typically reference variables, data sources, or other already-known values instead. Using `self` in a `precondition` causes a Terraform error.

---

### Question 5 — Flawed Claim: `check` Block Introduced in Terraform 1.3

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Which Terraform version introduced the `check` block

**Question**:
A team's migration runbook contains the following statement:

> "The `check` block was introduced in Terraform 1.3 as part of the same release that added `moved` blocks, enabling non-blocking infrastructure health assertions."

Which two facts in this statement are incorrect?

- A) Nothing — the `check` block was introduced in 1.3 alongside `moved` blocks
- B) The `check` block was introduced in **Terraform 1.5**, not 1.3; and `moved` blocks were introduced in **Terraform 1.1**, not in the same release as `check` — the two features were added in different versions
- C) The `check` block was introduced in Terraform 1.7; `moved` blocks were introduced in 1.3
- D) The `check` block was introduced in Terraform 1.5; `moved` blocks were also introduced in Terraform 1.5 in the same release

**Answer**: B

**Explanation**:
The `check` block was introduced in **Terraform 1.5**, not 1.3. The `moved` block was introduced earlier, in **Terraform 1.1**, as a way to rename or restructure resources in state without destroying and recreating them. The `import` block (declarative resource import) was introduced in the **same 1.5 release** as `check`. The runbook contains two errors: the wrong version for `check` and the wrong claim that `check` and `moved` were released together.

---

### Question 6 — Flawed Claim: Failed `postcondition` Destroys Resource and Removes from State

**Difficulty**: Medium
**Answer Type**: one
**Topic**: What happens to a resource in AWS and in state when its `postcondition` fails

**Question**:
A developer explains postcondition behaviour to their team:

> "When a `postcondition` fails after a resource is created, Terraform automatically destroys the resource to maintain a consistent, valid state — it removes the resource from AWS and from `terraform.tfstate` so the next apply starts clean."

What is wrong with this explanation?

- A) Nothing — Terraform does automatically destroy resources that fail postconditions
- B) The explanation is wrong: when a `postcondition` fails, the resource **remains in AWS and remains recorded in `terraform.tfstate`**; Terraform does not perform an automatic rollback, destroy, or state removal — the apply exits with a failure status and the team must investigate manually
- C) The explanation is wrong: when a `postcondition` fails, the resource is kept in AWS but is removed from state so the next plan treats it as a new resource to be imported
- D) The explanation is wrong: when a `postcondition` fails, the resource is destroyed in AWS but remains in state as an orphaned record

**Answer**: B

**Explanation**:
A `postcondition` runs **after** the resource change has already been applied. By the time the postcondition is evaluated, the resource exists in AWS and has been written to `terraform.tfstate`. Terraform does not roll back, destroy, or remove the resource on postcondition failure — it exits with a non-zero status and displays the `error_message`. The resource remains in both AWS and state with its actual attributes. This is the critical operational implication of postconditions: failure is caught after the fact, requiring manual investigation, unlike `precondition` which prevents the change entirely.

---

### Question 7 — Flawed HCL: `precondition` Placed Outside `lifecycle` Block

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Where `precondition` and `postcondition` blocks must be declared inside a resource

**Question**:
An engineer writes the following resource to prevent deployment to a test environment:

```hcl
resource "aws_instance" "web" {
  ami           = "ami-0abc123"
  instance_type = "t3.micro"

  precondition {
    condition     = var.environment != "test"
    error_message = "This resource cannot be deployed to the test environment."
  }
}
```

What is wrong with this configuration?

- A) Nothing — `precondition` blocks can be placed directly inside any resource block
- B) The configuration is wrong: `precondition` blocks must be declared **inside a `lifecycle` block** within the resource; placing `precondition` directly as a resource argument is invalid syntax
- C) The configuration is wrong: `precondition` cannot reference variables — it can only reference data source attributes
- D) The configuration is wrong: `precondition` blocks must be placed in a separate `conditions` file, not inside the resource block

**Answer**: B

**Explanation**:
`precondition` and `postcondition` are **nested inside the `lifecycle` block** of a resource or data source — they are not top-level resource arguments. The correct structure is:

```hcl
lifecycle {
  precondition {
    condition     = var.environment != "test"
    error_message = "This resource cannot be deployed to the test environment."
  }
}
```

Placing `precondition` directly in the resource block body is invalid HCL and will cause a parse error. The `lifecycle` block is the only place where `precondition`, `postcondition`, `create_before_destroy`, `prevent_destroy`, `ignore_changes`, and `replace_triggered_by` can be declared.

---

### Question 8 — Two Flawed Claims About `check` Block Structure

**Difficulty**: Medium
**Answer Type**: many
**Topic**: Where `check` blocks can be placed and whether a scoped `data` source is required

**Question**:
A developer documents the `check` block and makes two structural claims:

> **Claim 1**: "A `check` block can be placed inside a resource block to validate that specific resource's post-deployment state, similar to `postcondition`."
> **Claim 2**: "A `check` block must always include both a `data` block and an `assert` block — the `data` block is required; an `assert` block alone is not valid."

Which TWO statements correctly identify what is wrong with these claims? (Select two.)

- A) Claim 1 is **wrong**: `check` blocks are **top-level configuration blocks** — they cannot be nested inside resource blocks; their placement is similar to `resource` or `data` blocks at the root of a module
- B) Claim 1 is **correct**: `check` blocks can be placed inside resource blocks
- C) Claim 2 is **wrong**: the `data` block inside a `check` block is **optional** — a `check` block with only an `assert` block is perfectly valid
- D) Claim 2 is **correct**: a `check` block with only an `assert` and no `data` block causes a Terraform parse error

**Answer**: A, C

**Explanation**:
`check` blocks are **top-level** configuration constructs — they are declared at the same level as `resource`, `data`, `variable`, and `output` blocks. They cannot be nested inside a resource block (Claim 1 is wrong). The scoped `data` block inside a `check` block is entirely optional — `check` blocks with only an `assert` block are valid and commonly used to assert conditions on already-known infrastructure values such as resource attribute lengths or computed expressions (Claim 2 is wrong). The scoped `data` block is used when the assertion requires fetching live external data, such as an HTTP health check.

---

### Question 9 — Flawed Claim: Sensitive Variable Propagates Automatically to Output

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Whether `sensitive = true` on a variable automatically marks referencing outputs as sensitive

**Question**:
A developer marks a variable as sensitive and then creates an output referencing it:

```hcl
variable "db_password" {
  type      = string
  sensitive = true
}

output "db_connection_string" {
  value = "postgresql://admin:${var.db_password}@db.example.com/prod"
}
```

The developer says: "Since I've marked `var.db_password` as sensitive, Terraform will automatically treat `db_connection_string` as sensitive too — no changes to the output block are needed."

What is wrong with this claim?

- A) Nothing — Terraform automatically marks outputs as sensitive when they reference sensitive variables
- B) The claim is wrong: Terraform **detects** that the output references a sensitive value and raises a **plan error** requiring `sensitive = true` to be explicitly added to the output block — automatic propagation does not occur without user action
- C) The claim is wrong: Terraform silently allows the output to expose the sensitive value in plaintext; no error or automatic protection is applied
- D) The claim is wrong: sensitive variables cannot be interpolated into output values at all — they must be referenced directly with `value = var.db_password`

**Answer**: B

**Explanation**:
Terraform does detect sensitivity propagation and will raise a **plan error** when a sensitive value flows into an output that is not marked `sensitive = true`. The error message is: *"Output refers to Terraform-sensitive values. To protect these values, mark the output as sensitive."* This is not automatic protection — it is an error requiring the developer to explicitly add `sensitive = true` to the output block. The requirement is deliberate: Terraform forces conscious acknowledgement rather than silently hiding values that might be important to expose in some contexts.

---

### Question 10 — Two Flawed Claims About Condition Mechanism Failure Behaviour

**Difficulty**: Hard
**Answer Type**: many
**Topic**: When and how `validation`, `precondition`, and `check` failures are raised

**Question**:
A team's study guide contains the following two statements about condition mechanism failure behaviour:

> **Claim 1**: "A failed `validation` block is treated as a non-fatal warning during `terraform plan` — the plan still generates and shows proposed changes, but an advisory message is displayed."
> **Claim 2**: "A failed `precondition` produces a warning and allows the resource to be created anyway — it is the operator's responsibility to act on the warning."

Which TWO statements correctly identify the errors? (Select two.)

- A) Claim 1 is **wrong**: a failed `validation` block is a **fatal error that halts Terraform before any plan is generated** — it is not a warning, and no execution plan is produced
- B) Claim 1 is **correct**: validation failures are non-fatal warnings and the plan proceeds
- C) Claim 2 is **wrong**: a failed `precondition` is a **fatal error that halts `terraform apply` before the resource is created or modified** — the resource is not created and the apply exits with a failure
- D) Claim 2 is **correct**: precondition failures are warnings that allow the resource to be created

**Answer**: A, C

**Explanation**:
Both claims mischaracterize fatal conditions as warnings. `validation` failures (Claim 1) abort Terraform **before plan** — no plan is generated and no changes are shown. It is not a warning. `precondition` failures (Claim 2) abort `terraform apply` **before the resource is changed** — the resource is not created and the apply exits with a non-zero status. It is not a warning. Only `check` block failures are true warnings that allow apply to complete. Confusing these three mechanisms on the exam is a common error; the key is: `validation` = fatal before plan, `precondition`/`postcondition` = fatal during apply, `check` = warning only.

---

### Question 11 — Flawed Claim: Scoped `data` Source in `check` Block Has Fatal Errors Like Top-Level `data`

**Difficulty**: Hard
**Answer Type**: one
**Topic**: How errors from a scoped `data` source inside a `check` block differ from top-level `data` source errors

**Question**:
A developer adds a `check` block with a scoped HTTP data source:

```hcl
check "api_health" {
  data "http" "probe" {
    url = "https://api.internal.example.com/health"
  }

  assert {
    condition     = data.http.probe.status_code == 200
    error_message = "API health check failed with status ${data.http.probe.status_code}."
  }
}
```

During `terraform apply`, the internal API is unreachable and the HTTP request times out. The developer claims: "This HTTP data source inside the `check` block will behave exactly like a top-level `data` source — a connection failure will cause a fatal error and abort the apply."

What is wrong with this claim?

- A) Nothing — a data source error inside a `check` block is fatal and aborts apply, just like a top-level `data` source error
- B) The claim is wrong: a data source error inside a `check` block is treated the same as a failing `assert` condition — it produces a **warning** and does not abort the apply; this is one of the key differences between scoped and top-level `data` sources
- C) The claim is wrong: the scoped `data` source inside a `check` block is never actually executed during apply — it is only evaluated during `terraform plan`
- D) The claim is wrong: `check` block data sources automatically retry three times before deciding whether to fail or warn

**Answer**: B

**Explanation**:
A `data` block scoped inside a `check` block does **not** behave like a top-level `data` block. Top-level data source failures are fatal and abort the apply. A scoped data source inside a `check` block is part of the check's non-blocking context — errors (including connection failures, timeouts, or invalid responses) are treated as check failures and produce a **warning** rather than a fatal error. All other resources in the apply continue unaffected. This is a critical distinction: the same HTTP provider `data "http"` block behaves differently depending on whether it is placed at the top level or inside a `check` block.

---

### Question 12 — Two Flawed Claims About Retrieving Sensitive Output Values

**Difficulty**: Medium
**Answer Type**: many
**Topic**: Which `terraform output` command forms expose sensitive output values in plaintext

**Question**:
A developer sets `sensitive = true` on an output named `db_password` and makes two claims about retrieval:

> **Claim 1**: "Running `terraform output -json` will display sensitive outputs as `(sensitive value)` in the JSON, the same way `terraform output` (no arguments) does — sensitive values are always hidden in any output format."
> **Claim 2**: "Running `terraform output db_password` (querying the single output by name) will display `(sensitive value)` — there is no way to retrieve the actual value using the `terraform output` command."

Which TWO statements correctly identify the errors? (Select two.)

- A) Claim 1 is **wrong**: `terraform output -json` **reveals sensitive output values in plaintext** in the JSON response — it does not redact them as `(sensitive value)`
- B) Claim 1 is **correct**: `terraform output -json` always hides sensitive values
- C) Claim 2 is **wrong**: `terraform output db_password` (querying a single output by name) **displays the actual plaintext value** — only the aggregate `terraform output` (no arguments) listing redacts sensitive values
- D) Claim 2 is **correct**: querying a sensitive output by name always returns `(sensitive value)`

**Answer**: A, C

**Explanation**:
`sensitive = true` on an output suppresses the value in the aggregate `terraform output` listing — it appears as `(sensitive value)`. However, both `terraform output -json` and `terraform output <name>` (single output by name) **display the actual plaintext value**. `terraform output -raw <name>` also returns the raw plaintext. This is an important exam distinction: the sensitive flag is a display guard for the summary view, not a hard access control. It reinforces why the state file must be stored in an encrypted backend — the value is always retrievable by anyone with access to the state or to a terminal running these specific output commands.

---

---

## Questions

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

**Answer**: B

**Explanation**:
The `version` argument in a `module` block is exclusively supported for **Terraform Registry** and **private registry** sources. For any Git-based source — including bare GitHub URLs, `git::https://`, and `git::ssh://` — the `version` argument is invalid and causes `terraform init` to raise an error. To pin a Git-based module to a specific version, use the `?ref=` query parameter with a tag, branch, or commit SHA: `"github.com/acme/terraform-modules//modules/vpc?ref=v3.0.0"`.

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

**Answer**: B

**Explanation**:
Child module outputs are accessed using the expression `module.<module_label>.<output_name>`. The label `"networking"` comes from the `module "networking"` block declaration, making the correct reference `module.networking.public_subnet_id`. The syntax `output.networking.public_subnet_id` does not exist and causes a Terraform error about an invalid reference. Module outputs can be used directly in any resource argument, local, or root output — no intermediate local assignment is needed.

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

**Answer**: B

**Explanation**:
`.terraform/modules/` is a **local cache directory** generated by `terraform init`. It is analogous to `node_modules/` in Node.js projects — each developer populates it by running `terraform init`, which downloads module sources according to the declared `source` and `version` constraints. Committing this directory adds unnecessary repository bloat, can commit platform-specific binaries or paths, and can cause teammates to use stale or inconsistent module code if the cache is not regenerated after source changes. The standard practice is to add `.terraform/` to `.gitignore` and always run `terraform init` after checkout.

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

**Answer**: B

**Explanation**:
`terraform init` must be re-run any time a module source is added, removed, or changed in the configuration. It is responsible for downloading and caching module source code into `.terraform/modules/`. If a new `module` block is added and `terraform init` has not been re-run, `terraform plan` raises an error: "Module not installed — run `terraform init`." The command does not need to be re-run on every single plan (option C is incorrect), but it is not a one-time-only step either. Re-running `init` is always safe — it only refreshes what has changed.

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

**Answer**: B

**Explanation**:
The Terraform S3 backend writes lock acquisition entries to DynamoDB using a hardcoded partition key attribute named **`"LockID"`**. This is a fixed Terraform implementation requirement — the attribute name is not configurable. DynamoDB itself accepts any attribute name, so the table will be created successfully with `hash_key = "StateFileLock"`, but Terraform will fail when attempting to acquire or release a lock because it looks for an item with the `"LockID"` attribute. Every S3 backend locking example uses exactly `hash_key = "LockID"` with `type = "S"` for this reason.

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

**Answer**: B

**Explanation**:
`terraform state rm` is a **state file manipulation command** — it removes the specified resource record from `terraform.tfstate` without making any API calls to the cloud provider. The AWS S3 bucket remains fully intact and operational. After the command runs, Terraform no longer manages the resource: it is "forgotten" from Terraform's perspective. On the next `terraform plan`, if the resource block still exists in configuration, Terraform will plan to **create** it (not destroy it), because it is no longer in state. The command is used to stop Terraform management, not to delete infrastructure.

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

**Answer**: B

**Explanation**:
`terraform plan -refresh-only` is a **read-only drift report** — it queries live cloud resources, computes the difference from the current state, and displays what would change, but writes nothing to the state file. It is the drift-detection equivalent of `terraform plan` (which also never writes state). To actually update the state file to reflect cloud reality, the operator must run `terraform apply -refresh-only` and confirm the proposed state changes. The two commands are deliberately separated: `plan` always shows; `apply` always writes. Note: `terraform refresh` is deprecated and `apply -refresh-only` is its replacement.

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

**Answer**: B

**Explanation**:
Terraform propagates the default (non-aliased) provider configuration from the root module to all child modules automatically. A child module that creates `aws_*` resources does not need its own `provider "aws" {}` block — it uses the configuration inherited from the root. The `providers` argument in a `module` block is only needed when using **aliased providers** (e.g., deploying the same module to multiple regions) or when the root module needs to explicitly override which provider configuration a child module receives. Redundant provider declarations in child modules can cause Terraform errors about conflicting configurations.

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

**Answer**: B

**Explanation**:
The `version` argument in a `module` block is only valid for modules sourced from the **Terraform Registry** or a private registry — sources that have an associated version registry to query. For local path sources (those beginning with `./` or `../`), the `version` argument is invalid and causes `terraform init` to fail with an error. Local module code is pinned by the state of the file system at the time of use. For Git-based sources, versioning is handled with `?ref=v1.5.0` in the URL. There is no mechanism to apply semantic version constraints to local paths.

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

**Answer**: A, C

**Explanation**:
Two distinct errors exist. First, `count.index` is only available inside blocks that use `count` — it is undefined when `for_each` is used instead. The correct reference to the current iteration's key in a `for_each` block is `each.key` (for the key) or `each.value` (for the value). Here, `service_name = each.key` would resolve to `"web"`, `"api"`, or `"worker"` for each instance. Second, `for_each` on a set of strings addresses each module instance using its string key in bracket notation: `module.server["web"]`, `module.server["api"]`, `module.server["worker"]`. Numeric indexing (`module.server[0]`) is only valid when `count` is used. Both `toset()` and `for_each` on module blocks are valid (options B and D are incorrect).

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

**Answer**: A, C

**Explanation**:
`terraform.tfstate.backup` is a **single-file, single-snapshot** backup created only by the local backend. It is overwritten on each apply and holds no history beyond the immediately preceding state (Claim 1 is wrong — there is no rolling history). When using a remote backend such as S3, Terraform reads and writes state to the remote backend only — no local `terraform.tfstate.backup` file is created on apply (Claim 2 is wrong). Teams using remote backends rely on backend-native versioning (e.g., S3 object versioning) for state history, not local backup files.

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

**Answer**: B

**Explanation**:
`terraform state push` is a low-level, **non-interactive command** — it writes the provided file directly to the remote backend without displaying a diff, requesting confirmation, or performing any safety validation. A simple `terraform state push stale-backup.tfstate` can immediately overwrite a production state file, removing all resource tracking for changes that occurred since the backup was created. Terraform does include a serial number check (it will warn if the remote serial is higher than the local serial), but it can be bypassed with `-force`. This is why `terraform state push` is documented as a dangerous escape hatch, not a routine recovery tool. State restoration should be done through backend-native mechanisms (S3 versioning, HCP Terraform history) whenever possible.

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

**Answer**: A, C

**Explanation**:
`terraform state mv` is a **state file manipulation command** — it renames or relocates a resource's address within `terraform.tfstate` only; it does not touch any `.tf` configuration files (Claim 1 is wrong). The engineer must separately update the HCL resource label to match, or the next plan will propose destroying the old name and creating the new one. `moved` blocks (introduced in Terraform 1.1) are significantly more capable than Claim 2 suggests: they support renaming resources at any module level, moving resources from root into a module, moving resources between modules, and renaming module calls themselves (Claim 2 is wrong). `moved` blocks are the preferred declarative approach because they record the change in source control, helping teammates who apply from a fresh state.

---

---

iteration: 4
batch: 8
style: Error Identification
topics:
  - Importing Infrastructure & State Inspection
  - HCP Terraform — Workspaces, Runs, State
  - HCP Terraform — Governance, Security & Advanced
question_count: 13
difficulty_split: "2 Easy / 9 Medium / 2 Hard"
answer_type_split: "10 one / 3 many"
---

# Terraform Associate (004) — Iteration 4, Batch 8
## Error Identification × Importing + HCP Terraform

Each question presents a flawed claim, incorrect HCL snippet, or wrong workflow description.
Identify the specific error in the statement or configuration provided.

---

### Question 1 — CLI Import and HCL Generation

**Difficulty**: Easy
**Answer Type**: one
**Topic**: Whether the CLI `terraform import` command supports the `-generate-config-out` flag

**Question**:
A developer states: "The `terraform import` CLI command supports the `-generate-config-out` flag just like the declarative `import` block — you can run `terraform import -generate-config-out=generated.tf aws_instance.web i-0abc123` to automatically create the HCL resource block for the imported resource."

What is wrong with this claim?

- A) The flag is named `-config-out`, not `-generate-config-out`, for the CLI import command
- B) The `-generate-config-out` flag is exclusive to `terraform plan` when used with a declarative `import` block — the CLI `terraform import` command does not support this flag and never generates HCL
- C) The flag works but requires an existing resource block to be present before it can generate the configuration
- D) The flag is valid but only outputs JSON, not HCL

**Answer**: B

**Explanation**:
`-generate-config-out` is not a flag on `terraform import`. It is an option for `terraform plan` that works only when a declarative `import` block is already present in the configuration. The workflow is: add an `import` block → run `terraform plan -generate-config-out=generated.tf` → review and clean up the generated HCL → run `terraform apply`. The legacy CLI `terraform import` command only writes the resource to state; it never generates HCL configuration under any circumstances.

---

### Question 2 — TF_LOG Default Output Destination

**Difficulty**: Easy
**Answer Type**: one
**Topic**: Where Terraform writes log output when `TF_LOG` is set but `TF_LOG_PATH` is not

**Question**:
An operator says: "If you set `TF_LOG=DEBUG` without setting `TF_LOG_PATH`, Terraform has nowhere to write the logs — logging is effectively disabled. You must set `TF_LOG_PATH=terraform.log` to activate debug output."

What is wrong with this claim?

- A) `TF_LOG=DEBUG` is not a valid log level — the minimum valid level is `INFO`
- B) When `TF_LOG` is set but `TF_LOG_PATH` is not, Terraform writes log output to **stderr** — `TF_LOG_PATH` is optional and only redirects output from stderr to a file
- C) `TF_LOG_PATH` defaults to `terraform.log` in the working directory, so logging is active by default without explicitly setting it
- D) Terraform writes logs to stdout when `TF_LOG_PATH` is absent, which may mix with plan output

**Answer**: B

**Explanation**:
`TF_LOG_PATH` is entirely optional. Without it, Terraform emits log output to **stderr**, which is separate from the stdout used for plan and apply output. Setting `TF_LOG=DEBUG` alone is sufficient to enable debug logging — it will appear in the terminal's stderr stream. `TF_LOG_PATH` is used specifically to redirect that stderr output to a file, which is useful in automated pipelines where you want to capture logs separately. Logging is never "disabled" simply because `TF_LOG_PATH` is absent.

---

### Question 3 — Swapped `import` Block Arguments

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Correct use of the `to` and `id` arguments in a declarative `import` block

**Question**:
Read this `import` block:

```hcl
import {
  to = "i-0abcd1234ef567890"
  id = aws_instance.web
}
```

A colleague reviews this and says: "Looks correct — `to` takes the cloud resource identifier and `id` takes the Terraform resource address."

What is wrong with this configuration and the colleague's explanation?

- A) The `import` block requires a `provider` argument in addition to `to` and `id`
- B) The arguments are swapped — `to` must be the Terraform resource address (unquoted, e.g., `aws_instance.web`) and `id` must be the cloud provider's resource identifier (e.g., `"i-0abcd1234ef567890"`)
- C) Both values must be quoted strings — using an unquoted reference for `id` causes a syntax error
- D) The `import` block must be placed inside the `resource "aws_instance" "web"` block, not at the root level

**Answer**: B

**Explanation**:
In a declarative `import` block, `to` specifies the **Terraform resource address** — the target resource block in your configuration, written as an unquoted expression (e.g., `aws_instance.web`). `id` specifies the **cloud provider's resource identifier** — a string such as an AWS instance ID (e.g., `"i-0abcd1234ef567890"`). The configuration shown has these reversed: the cloud ID is in `to` and the resource address is in `id`. The colleague's explanation compounds the error by also describing the arguments in the wrong order. This would cause a configuration error during `terraform plan`.

---

### Question 4 — `cloud` Block and `backend` Block Coexistence

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Whether `cloud` and `backend` blocks can be used together in the same `terraform {}` block

**Question**:
A team uses HCP Terraform for production and a local backend for local development. A developer proposes this configuration to support both:

```hcl
terraform {
  cloud {
    organization = "acme-corp"
    workspaces {
      name = "production"
    }
  }

  backend "local" {}
}
```

The developer claims: "This configuration lets Terraform fall back to the local backend when HCP Terraform is unavailable and use the `cloud` block when it is reachable."

What is the error in this configuration and claim?

- A) The `cloud` block and `backend` block are mutually exclusive within a single `terraform {}` block — Terraform raises a configuration error if both are declared simultaneously
- B) The `backend "local"` block overrides the `cloud` block because backend declarations always take precedence
- C) The `cloud` block overrides `backend "local"` silently, making the `backend` block unreachable but not an error
- D) This is valid Terraform syntax; the blocks serve different lifecycle phases and do not conflict

**Answer**: A

**Explanation**:
The `cloud` block and any `backend` block are **mutually exclusive** in a `terraform {}` block. Terraform raises an error during `terraform init` if both are present: you cannot declare `cloud` and `backend` in the same configuration. There is no fallback or precedence mechanism — the two are simply incompatible declarations. Teams that want to switch between backends for different environments must use separate configuration files or variable-based backend selection strategies, not coexisting declarations. The `cloud` block was introduced in Terraform 1.1 specifically to supersede the `backend "remote"` approach and cannot be combined with any `backend` block.

---

### Question 5 — Sentinel Enforcement Level Descriptions

**Difficulty**: Medium
**Answer Type**: many
**Topic**: Distinguishing `advisory`, `soft-mandatory`, and `hard-mandatory` enforcement level behaviour

**Question**:
A team lead explains Sentinel policy enforcement levels to new engineers. Which TWO of the following statements contain an error? (Select two.)

- A) The `advisory` enforcement level logs a warning when a policy fails but allows the run to continue — it does not block the apply
- B) The `advisory` enforcement level blocks the apply when a policy fails — it is less strict than `soft-mandatory` only because the failure is displayed as a warning rather than a hard stop
- C) There is no mechanism to override a `soft-mandatory` policy failure — once blocked, the only resolution is to fix the configuration or remove the policy
- D) The `hard-mandatory` enforcement level blocks the run and provides no override mechanism — not even organisation Owners can bypass a `hard-mandatory` failure

**Answer**: B, C

**Explanation**:
Two statements contain errors. (B) is wrong: `advisory` does NOT block the run — the policy failure is surfaced as a warning in the HCP Terraform UI and logs, but the run proceeds to apply regardless. Only `soft-mandatory` and `hard-mandatory` actually block the run. (C) is also wrong: `soft-mandatory` failures CAN be overridden by a user who holds the "Manage Policy Overrides" permission — this is the deliberate distinction between `soft-mandatory` and `hard-mandatory`. (A) is correct: `advisory` warns but does not block. (D) is correct: `hard-mandatory` failures cannot be overridden by anyone, including Owners, making it the appropriate enforcement level for non-negotiable compliance requirements.

---

### Question 6 — Health Assessment Auto-Apply Claim

**Difficulty**: Medium
**Answer Type**: one
**Topic**: What HCP Terraform health assessments do when they detect drift, and what they cannot do

**Question**:
A platform engineer describes HCP Terraform health assessments: "When a health assessment detects that cloud resources have drifted from the configuration — for example, an EC2 instance type was manually changed in the AWS Console — HCP Terraform automatically queues a `terraform apply -refresh-only` run to pull the drift into state, keeping your state file accurate without any manual intervention."

What is the error in this description?

- A) Health assessments run `terraform apply` (not `-refresh-only`) to restore the resource to the configuration-defined state
- B) Health assessments run `terraform plan -refresh-only` — they are read-only drift detection operations and **never automatically queue or execute any apply**, even a `-refresh-only` apply
- C) Health assessments do not detect instance type changes — they only detect resource deletions
- D) Health assessments are triggered manually, not on a schedule

**Answer**: B

**Explanation**:
HCP Terraform health assessments are read-only scheduled operations that execute `terraform plan -refresh-only` to detect drift. When drift is found, the workspace's health status in the UI is updated to show it as drifted and configured notification destinations are alerted. The health assessment system **never automatically queues any apply** — not a standard apply, not a `-refresh-only` apply. The engineering team receives the notification and decides how to respond: they might queue a manual `terraform apply -refresh-only` to update the state, or queue a standard `terraform apply` to restore the actual resources. Automatic remediation would be a significant operational risk and is not a feature of health assessments.

---

### Question 7 — Speculative Plan Approval Claim

**Difficulty**: Medium
**Answer Type**: one
**Topic**: The lifecycle limitations of speculative plans in HCP Terraform

**Question**:
A developer explains HCP Terraform run types: "A speculative plan is like a standard plan but with lower risk — it runs through the planning phase and shows what changes would occur. If the speculative plan shows **no infrastructure changes** (i.e., no resources will be created, modified, or destroyed), a workspace Admin can approve it to proceed to apply, since there is nothing harmful to execute."

What is the error in this statement?

- A) Speculative plans cannot be approved for apply under any circumstance — they are strictly informational and the run lifecycle ends at the plan stage regardless of the plan output
- B) Only organisation Owners (not workspace Admins) can approve a speculative plan that shows no changes
- C) Speculative plans that show no changes are automatically applied by HCP Terraform without requiring approval
- D) Speculative plans can only be triggered via the HCP Terraform UI, not via VCS pull request webhooks

**Answer**: A

**Explanation**:
Speculative plans are a distinct run type designed specifically for informational purposes — commonly triggered by pull requests to give teams visibility into planned infrastructure changes before merging. They **never progress to apply under any circumstances**, regardless of whether the plan shows changes or no changes, and regardless of who attempts to approve them. No approval option is presented in the HCP Terraform UI for speculative plans. If a team wants a plan-and-apply run, they must trigger a standard plan-and-apply run type. This distinction is fundamental to the VCS workflow: PR events produce speculative plans; merge events produce plan-and-apply runs.

---

### Question 8 — `terraform login` Token Storage Location

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Where `terraform login` stores the HCP Terraform API token on disk

**Question**:
A DevOps engineer documents the `terraform login` workflow: "Running `terraform login` opens a browser to authenticate with HCP Terraform. Once complete, the API token is saved to `.terraform/credentials.json` inside your current working directory — this is why you should add `.terraform/` to your `.gitignore` to prevent the token from being committed to version control."

What is the specific error in this documentation?

- A) The token is stored in memory only for the duration of the current shell session — no file is written to disk
- B) The file is written to `.terraform.d/credentials.tfrc.json` inside the current working directory, not `.terraform/credentials.json`
- C) The token is saved to `~/.terraform.d/credentials.tfrc.json` in the user's **home directory** — not in the project's `.terraform/` directory
- D) `terraform login` saves the token to the system keychain, not a file, on supported operating systems

**Answer**: C

**Explanation**:
`terraform login` saves the HCP Terraform API token to `~/.terraform.d/credentials.tfrc.json` in the **user's home directory** (`~` on Unix/macOS, `%APPDATA%\terraform.d` on Windows) — not inside the project's `.terraform/` folder. While adding `.terraform/` to `.gitignore` is correct practice (to prevent committing state locks and provider plugins), the token is not stored there. The home-directory storage means the token persists across Terraform projects and working directories for that OS user. This distinction matters because `.terraform/` is project-scoped and typically gitignored anyway, whereas a token in the home directory is user-scoped and shared across all projects.

---

### Question 9 — HCP Terraform Audit Log Properties

**Difficulty**: Medium
**Answer Type**: many
**Topic**: The immutability and exportability of HCP Terraform audit logs

**Question**:
A compliance officer reviews HCP Terraform's audit logging capabilities. Which TWO of the following statements about HCP Terraform audit logs contain an error? (Select two.)

- A) Every action taken in an HCP Terraform organisation is logged, including run triggers, variable changes, team membership updates, and policy overrides
- B) Organisation Owners can edit or redact audit log entries containing sensitive information before exporting them to external systems
- C) Audit logs are immutable — no user, including Owners, can modify or delete individual log entries
- D) Audit logs are stored internally within HCP Terraform and cannot be exported to external SIEM or log management systems

**Answer**: B, D

**Explanation**:
Two statements contain errors. (B) is wrong: HCP Terraform audit logs are **immutable** — no user can edit, redact, or delete individual entries, including organisation Owners. This immutability is an intentional compliance design choice that ensures audit trails cannot be tampered with after the fact. (D) is also wrong: audit logs **can be exported** to external systems — they are designed for integration with SIEM platforms and log management tools, enabling organisations to aggregate Terraform activity with other infrastructure audit data. (A) is correct: audit logs capture all significant actions across the organisation. (C) is correct and restates the immutability property accurately.

---

### Question 10 — `import` Block Workflow Step Order

**Difficulty**: Medium
**Answer Type**: one
**Topic**: The correct sequence of steps when using a declarative `import` block with `-generate-config-out`

**Question**:
A developer explains the `import` block workflow to a colleague:

> "Step 1: Run `terraform plan -generate-config-out=generated.tf` — this scans the `import` requirements and generates the HCL skeleton.
> Step 2: Add an `import` block to your configuration with the correct `to` and `id` values to match the generated skeleton.
> Step 3: Run `terraform apply` to complete the import."

What is the error in this workflow description?

- A) Step 3 should be `terraform import`, not `terraform apply`
- B) The `import` block must be added to the configuration **before** running `terraform plan -generate-config-out` — the flag generates HCL for resources already referenced by existing `import` blocks and cannot discover what to generate without them
- C) Step 1 should use `terraform apply -generate-config-out`, not `terraform plan -generate-config-out`
- D) The generated file from `-generate-config-out` must be manually renamed to `main.tf` before `terraform apply` will process it

**Answer**: B

**Explanation**:
The described workflow has Steps 1 and 2 in the wrong order. The correct sequence is: (1) **Add the `import` block** with `to` and `id` to your configuration first. (2) **Run `terraform plan -generate-config-out=generated.tf`** — Terraform uses the `import` blocks already present to know which resources need HCL generated. Without an existing `import` block, the flag has no resources to target and will not produce any useful configuration. (3) Review and clean up `generated.tf`. (4) **Run `terraform apply`** to execute the import. The `-generate-config-out` flag does not scan or discover import targets autonomously — it only generates HCL for resources explicitly referenced in `import` blocks.

---

### Question 11 — `terraform state list` Capabilities

**Difficulty**: Medium
**Answer Type**: one
**Topic**: What `terraform state list` outputs versus what `terraform state show` outputs

**Question**:
A developer states: "Use `terraform state list` to get a full inventory of your managed infrastructure — it outputs each resource along with all its current attribute values like IP addresses, ARNs, instance types, and tags. It is the fastest way to see the complete current state of every resource in one view."

What is the error in this description?

- A) `terraform state list` does not read from the state file — it queries the cloud provider API directly
- B) `terraform state list` only outputs **resource addresses** (one per line, e.g., `aws_instance.web`) — it does not display attribute values; use `terraform state show <address>` to see all recorded attributes for a specific resource
- C) `terraform state list` is a deprecated command — `terraform show` is the recommended replacement for listing all managed resources
- D) `terraform state list` only shows resources in the root module and cannot list resources inside child modules

**Answer**: B

**Explanation**:
`terraform state list` produces a simple list of **resource addresses** — each line contains just an address such as `module.vpc.aws_subnet.public[0]` or `aws_instance.web`. It provides an index of what is tracked in state, not the attribute values. To inspect the attributes (IP addresses, ARNs, configuration values, etc.) of a specific resource, use `terraform state show <address>`. To see a human-readable view of all state at once, use `terraform show`. The distinction matters operationally: `state list` is used to find the correct address to pass to `state show`, `state rm`, or `terraform import`.

---

### Question 12 — HCP Terraform Private Registry Source Address

**Difficulty**: Hard
**Answer Type**: one
**Topic**: Correct source address format for modules published to the HCP Terraform private registry

**Question**:
A team publishes an internal VPC module to their HCP Terraform organisation's private registry. A developer writes this module reference in a root configuration:

```hcl
module "vpc" {
  source  = "registry.terraform.io/acme-corp/vpc/aws"
  version = "~> 2.0"
}
```

The developer claims: "This is correct — private registry modules follow the same source address format as the public Terraform Registry, using `registry.terraform.io` as the hostname."

What is the error?

- A) Private registry modules do not use a hostname prefix at all — the format is `<org>/<module>/<provider>` without any host component
- B) The correct hostname for the HCP Terraform private registry is `app.terraform.io`, not `registry.terraform.io` — the source address should be `app.terraform.io/acme-corp/vpc/aws`
- C) The private registry requires the full URL format: `https://app.terraform.io/app/acme-corp/registry/modules/private/vpc/aws`
- D) Private registry modules cannot be versioned with `~>` constraints — an exact version must be specified

**Answer**: B

**Explanation**:
HCP Terraform's private registry uses `app.terraform.io` as its hostname, not `registry.terraform.io`. The correct source address for a private registry module is `app.terraform.io/<org>/<module>/<provider>` — for example, `app.terraform.io/acme-corp/vpc/aws`. The public Terraform Registry (registry.terraform.io) hosts community and HashiCorp-published modules and uses no hostname prefix in module source addresses (just `<namespace>/<module>/<provider>`). Using `registry.terraform.io` as the hostname for a private module causes Terraform to look for the module in the public registry, where it does not exist, resulting in a module not found error during `terraform init`.

---

### Question 13 — Dynamic Provider Credentials (OIDC) Misconceptions

**Difficulty**: Hard
**Answer Type**: many
**Topic**: How OIDC dynamic provider credentials work and what they replace in HCP Terraform

**Question**:
An engineer prepares training material on dynamic provider credentials. Which TWO of the following statements contain an error? (Select two.)

- A) With OIDC dynamic credentials, no long-lived static cloud credentials (e.g., AWS access key + secret key) need to be stored in HCP Terraform workspace variables — each run receives a short-lived token scoped to that run
- B) OIDC trust is established by storing the cloud provider's OIDC client secret as a sensitive environment variable in HCP Terraform — HCP Terraform presents this secret to authenticate itself to the cloud provider during each run
- C) When a run begins, HCP Terraform generates a signed JWT (JSON Web Token) that it presents to the cloud provider; the cloud provider validates the token against its configured OIDC trust relationship with HCP Terraform's issuer endpoint
- D) OIDC dynamic credentials are available for any Terraform provider registered in the public registry — any provider that supports AWS-compatible API calls can automatically use OIDC authentication with HCP Terraform

**Answer**: B, D

**Explanation**:
Two statements contain errors. (B) is wrong: OIDC trust does **not** use a shared client secret stored in HCP Terraform. Instead, the **cloud provider** (AWS, Azure, GCP) is configured to trust HCP Terraform as an OIDC identity provider using HCP Terraform's public OIDC discovery endpoint. Token authenticity is verified using asymmetric cryptography (public/private key pairs), not shared secrets — this is the core security advantage of OIDC over static credentials. (D) is also wrong: OIDC dynamic credentials require explicit trust configuration on the cloud provider side and are only supported for specific cloud providers (primarily AWS, Azure, and GCP) that implement OIDC federation. It is not an automatic capability available to any provider in the public registry. (A) is correct: this accurately describes the no-static-credentials benefit. (C) is correct: this accurately describes the JWT-based token exchange mechanism.

---