# Terraform Associate (004) — Question Bank Iter 1 Batch 1

**Iteration**: 1
**Iteration Style**: Foundational recall — define terms, name commands, identify blocks
**Batch**: 1
**Objective**: 1 — IaC Concepts
**Generated**: 2026-04-25
**Total Questions**: 12
**Difficulty Split**: 2 Easy / 8 Medium / 2 Hard
**Answer Types**: 9 `one` / 3 `many` / 0 `none`

---

# Terraform Associate (004) — Question Bank Iter 1 Batch 2

**Iteration**: 1
**Iteration Style**: Foundational recall — define terms, name commands, identify blocks
**Batch**: 2
**Objective**: 2 — Terraform Fundamentals (Providers & State)
**Generated**: 2026-04-25
**Total Questions**: 13
**Difficulty Split**: 2 Easy / 9 Medium / 2 Hard
**Answer Types**: 11 `one` / 2 `many` / 0 `none`

---

# Terraform Associate (004) — Question Bank Iter 1 Batch 3

**Iteration**: 1
**Iteration Style**: Foundational recall — define terms, name commands, identify flags
**Batch**: 3
**Objective**: 3 — Core Workflow & CLI
**Generated**: 2026-04-25
**Total Questions**: 13
**Difficulty Split**: 2 Easy / 9 Medium / 2 Hard
**Answer Types**: 10 `one` / 3 `many` / 0 `none`

---

# Terraform Associate (004) — Question Bank Iter 1 Batch 4

**Iteration**: 1
**Iteration Style**: Foundational recall — define terms, name commands, identify blocks
**Batch**: 4
**Objective**: 4a — Resources, Data & Dependencies
**Generated**: 2026-04-25
**Total Questions**: 13
**Difficulty Split**: 2 Easy / 9 Medium / 2 Hard
**Answer Types**: 10 `one` / 3 `many` / 0 `none`

---

# Terraform Associate (004) — Question Bank Iter 1 Batch 5

**Iteration**: 1
**Iteration Style**: Foundational recall — define terms, name commands, identify blocks
**Batch**: 5
**Objective**: 4b — Variables, Outputs, Types & Functions
**Generated**: 2026-04-25
**Total Questions**: 13
**Difficulty Split**: 2 Easy / 9 Medium / 2 Hard
**Answer Types**: 10 `one` / 3 `many` / 0 `none`

---

# Terraform Associate (004) — Question Bank Iter 1 Batch 6

**Iteration**: 1
**Iteration Style**: Foundational recall — define terms, name commands, identify blocks
**Batch**: 6
**Objective**: 4c — Custom Conditions & Sensitive Data
**Generated**: 2026-04-25
**Total Questions**: 12
**Difficulty Split**: 2 Easy / 8 Medium / 2 Hard
**Answer Types**: 9 `one` / 3 `many` / 0 `none`

---

# Terraform Associate (004) — Question Bank Iter 1 Batch 7

**Iteration**: 1
**Iteration Style**: Foundational recall — define terms, name commands, identify blocks
**Batch**: 7
**Objective**: 5 — Modules + 6 — State Backends
**Generated**: 2026-04-25
**Total Questions**: 13
**Difficulty Split**: 2 Easy / 9 Medium / 2 Hard
**Answer Types**: 10 `one` / 3 `many` / 0 `none`

---

# Terraform Associate (004) — Question Bank Iter 1 Batch 8

**Iteration**: 1
**Iteration Style**: Foundational recall — define terms, name commands, identify blocks
**Batch**: 8
**Objective**: 7 — Maintaining Infra + 8 — HCP Terraform
**Generated**: 2026-04-25
**Total Questions**: 13
**Difficulty Split**: 2 Easy / 9 Medium / 2 Hard
**Answer Types**: 10 `one` / 3 `many` / 0 `none`

---

---

## Questions

---

### Question 1 — IaC Definition

**Difficulty**: Easy
**Answer Type**: one
**Topic**: What Infrastructure as Code is

**Question**:
Which of the following best defines Infrastructure as Code (IaC)?

- A) A method of provisioning cloud infrastructure exclusively through graphical web consoles
- B) The practice of managing and provisioning infrastructure through machine-readable configuration files instead of manual processes
- C) A scripting approach where an operator runs CLI commands in sequence to build servers
- D) A monitoring strategy that detects when infrastructure deviates from a known baseline

**Answer**: B

**Explanation**:
IaC is the practice of defining infrastructure — servers, networks, databases, and so on — in machine-readable configuration files rather than through manual console clicks or ad-hoc commands. Terraform is a leading IaC tool that uses HCL configuration files to represent the desired state of infrastructure.

---

### Question 2 — Desired State vs Current State

**Difficulty**: Easy
**Answer Type**: one
**Topic**: Desired state and current state concepts

**Question**:
In the context of Terraform, what does "desired state" refer to?

- A) The actual infrastructure resources that exist in the cloud provider right now
- B) The previous version of infrastructure before the last `terraform apply`
- C) What your `.tf` configuration files say the infrastructure should look like
- D) The contents of the `terraform.tfstate` file after the last successful apply

**Answer**: C

**Explanation**:
Desired state is what your Terraform configuration files declare the infrastructure should look like. Current state is what actually exists in the cloud. Terraform's job is to reconcile the gap between the two by planning and applying the minimal set of changes needed.

---

### Question 3 — Idempotency

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Idempotency in IaC

**Question**:
A Terraform configuration that creates three EC2 instances is applied successfully. An operator runs `terraform apply` a second time against the same unchanged configuration. What is the expected result?

- A) Terraform creates three additional EC2 instances, resulting in six total
- B) Terraform destroys the existing instances and recreates them
- C) Terraform reports that no changes are needed and makes no modifications
- D) Terraform returns an error because the resources already exist

**Answer**: C

**Explanation**:
Idempotency means applying the same configuration multiple times produces the same outcome. When the current state already matches the desired state, Terraform detects no difference and reports "No changes. Your infrastructure matches the configuration." No resources are created, modified, or destroyed.

---

### Question 4 — Declarative vs Imperative

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Declarative approach in Terraform

**Question**:
Which statement correctly describes the declarative approach used by Terraform?

- A) You write step-by-step instructions telling Terraform exactly how to create each resource
- B) You describe the desired end state of your infrastructure and Terraform determines the steps required to reach it
- C) You provide Terraform with shell scripts that it executes in order on the target cloud provider
- D) You specify only the resources to delete; Terraform infers what should be created from provider defaults

**Answer**: B

**Explanation**:
Terraform is declarative — you describe *what* you want (e.g., "three EC2 instances of type t3.micro"), and Terraform calculates *how* to get there by comparing desired state to current state. This contrasts with imperative tools such as Ansible playbooks or shell scripts, where you specify the exact steps to execute.

---

### Question 5 — IaC Benefits

**Difficulty**: Medium
**Answer Type**: many
**Topic**: Benefits of using IaC

**Question**:
Which TWO of the following are recognized benefits of managing infrastructure with IaC tools like Terraform? (Select two.)

- A) Infrastructure changes require no code review since they are applied automatically
- B) Every infrastructure change is captured as a version-controlled commit, providing a full audit trail
- C) Provider-specific web consoles become unnecessary and are disabled by the IaC tool
- D) Identical environments can be reproduced reliably from the same configuration code

**Answer**: B, D

**Explanation**:
Two core benefits of IaC are repeatability (the same code deploys identical environments every time) and auditability (every change is a commit, creating a traceable history). IaC does not disable provider consoles, and infrastructure-as-code changes should still go through review processes like pull requests.

---

### Question 6 — Multi-Cloud Support

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Terraform multi-cloud capability

**Question**:
Which of the following best describes Terraform's approach to managing resources across multiple cloud providers?

- A) Terraform requires a separate state file and CLI installation for each cloud provider
- B) Terraform can manage resources across AWS, Azure, GCP, and other providers within a single workflow using provider plugins
- C) Terraform delegates cross-cloud provisioning to AWS CloudFormation, which acts as a broker
- D) Terraform supports only one cloud provider per workspace; multi-cloud requires separate root modules that cannot share state

**Answer**: B

**Explanation**:
Terraform's provider plugin model allows a single Terraform configuration to declare resources across multiple cloud providers simultaneously. A single `.tf` file can contain `aws_`, `azurerm_`, and `google_` resources. This multi-cloud capability is a key differentiator from single-cloud tools such as CloudFormation (AWS only) and ARM templates (Azure only).

---

### Question 7 — IaC Tooling Landscape

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Terraform vs other IaC tools

**Question**:
An operator wants to provision infrastructure on both AWS and Azure from a single set of configuration files. Which tool is best suited for this requirement?

- A) AWS CloudFormation
- B) Azure Resource Manager (ARM) templates
- C) Terraform
- D) Google Cloud Deployment Manager

**Answer**: C

**Explanation**:
AWS CloudFormation manages only AWS resources, ARM templates manage only Azure resources, and Google Cloud Deployment Manager manages only GCP resources. Terraform is provider-agnostic and can manage resources across all three — and many other providers — using a single unified workflow.

---

### Question 8 — Drift Detection

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Infrastructure drift and IaC

**Question**:
What is "infrastructure drift" in the context of IaC?

- A) The gradual increase in cost of cloud resources over time
- B) A discrepancy between the infrastructure described in configuration files and the actual infrastructure that exists in the cloud
- C) The latency introduced when Terraform communicates with a remote cloud API
- D) A versioning conflict between two different Terraform providers

**Answer**: B

**Explanation**:
Infrastructure drift occurs when the actual state of cloud resources diverges from the desired state expressed in configuration files — for example, when someone manually modifies a resource through the cloud console. Terraform can detect drift by comparing its state file with the real infrastructure, and remediate it by re-applying the configuration.

---

### Question 9 — IaC vs Manual Provisioning

**Difficulty**: Medium
**Answer Type**: many
**Topic**: Drawbacks of manual (ClickOps) provisioning

**Question**:
Which TWO of the following are drawbacks of manually provisioning infrastructure through a cloud provider's web console instead of using IaC? (Select two.)

- A) Web consoles require a paid subscription that IaC tools eliminate
- B) Manual changes leave no automatic version-controlled audit trail of who changed what and when
- C) Manually provisioned environments are difficult to reproduce identically, leading to environment inconsistencies
- D) Web consoles do not support creating virtual machines or networking resources

**Answer**: B, C

**Explanation**:
Manual provisioning (sometimes called ClickOps) produces no automatic version history, making it hard to track changes over time. It also makes reproducing environments reliably nearly impossible since there is no single source of truth. IaC solves both problems by capturing infrastructure as code committed to version control.

---

### Question 10 — Declarative vs Imperative Tools

**Difficulty**: Hard
**Answer Type**: one
**Topic**: Classifying IaC tools by approach

**Question**:
A team currently uses Ansible playbooks to configure servers step by step and is evaluating Terraform as an addition to their toolchain. Which statement correctly describes how the two tools differ in their primary approach?

- A) Ansible is declarative; Terraform is imperative
- B) Both Ansible and Terraform are declarative; they differ only in the cloud providers they support
- C) Ansible playbooks are primarily imperative — specifying steps to execute; Terraform is declarative — specifying the desired end state
- D) Terraform is imperative for resource creation but declarative for resource deletion

**Answer**: C

**Explanation**:
Ansible playbooks define ordered tasks to execute (imperative), while Terraform configuration declares the desired end state and lets the tool determine the necessary steps (declarative). In practice, Ansible can behave in a declarative manner for some modules, but its primary model is task-based and imperative, making it complementary to Terraform rather than a replacement.

---

### Question 11 — IaC and Disaster Recovery

**Difficulty**: Hard
**Answer Type**: one
**Topic**: Disaster recovery with IaC

**Question**:
A production environment is completely lost due to a datacenter failure. The team has their Terraform configuration files and a backup of the Terraform state stored in a remote backend. Which statement best describes how IaC helps in this scenario?

- A) IaC cannot help because the cloud resources themselves are gone and must be rebuilt manually
- B) The team can run `terraform apply` using the existing configuration to recreate the entire environment reproducibly, with the state backup used to avoid recreating already-restored resources
- C) The team must first run `terraform import` for every resource before any apply can proceed
- D) IaC helps only if the same Terraform version that created the original infrastructure is installed

**Answer**: B

**Explanation**:
One of IaC's most valuable properties is disaster recovery — the entire infrastructure environment is encoded in configuration files and can be recreated by running `terraform apply`. Having a remote state backup allows Terraform to track which resources have already been restored during incremental recovery. There is no requirement to import resources or match exact Terraform versions for a basic apply.

---

### Question 12 — IaC Audit Trail

**Difficulty**: Medium
**Answer Type**: many
**Topic**: Version control and auditability of IaC

**Question**:
Which TWO of the following capabilities does storing Terraform configuration in a version control system (such as Git) provide? (Select two.)

- A) Automatic application of infrastructure changes whenever a commit is pushed, without any additional tooling
- B) A historical record of every infrastructure change, including who made it and when
- C) The ability to review proposed infrastructure changes through pull requests before they are applied
- D) Real-time synchronization of cloud resources with the repository without needing `terraform apply`

**Answer**: B, C

**Explanation**:
Version-controlling Terraform configuration provides a full audit trail (who changed what and when, via commit history) and enables collaborative review of infrastructure changes through pull requests before they reach production. Automatic application on commit requires additional CI/CD tooling and does not happen by default; real-time resource synchronization is not a Git or Terraform feature.

---

---

## Questions

---

### Question 1 — Provider Definition

**Difficulty**: Easy
**Answer Type**: one
**Topic**: What a Terraform provider is

**Question**:
Which of the following best describes a Terraform provider?

- A) A HashiCorp-managed cloud platform that stores Terraform state remotely
- B) A plugin that bridges Terraform's HCL configuration to a target cloud or service API
- C) A built-in Terraform block that defines authentication credentials in a `.tf` file
- D) A version of the Terraform CLI binary compiled for a specific operating system

**Answer**: B

**Explanation**:
A provider is a Terraform plugin responsible for authenticating to a cloud or service API, implementing CRUD operations for resources, exposing data sources, validating configuration, and mapping resource attributes to and from state. Every resource in Terraform belongs to a provider.

---

### Question 2 — Provider Tiers

**Difficulty**: Easy
**Answer Type**: one
**Topic**: Provider tier classification

**Question**:
Terraform providers are classified into three tiers. Which tier is maintained directly by HashiCorp and carries the highest level of trust?

- A) Community
- B) Partner
- C) Official
- D) Verified

**Answer**: C

**Explanation**:
The three provider tiers are Official (maintained by HashiCorp — e.g., AWS, Azure, GCP), Partner (maintained by technology partners and reviewed/approved by HashiCorp), and Community (maintained by individuals or organisations with no HashiCorp verification). Official providers carry the highest trust level.

---

### Question 3 — Plugin Architecture Communication

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Terraform Core and provider communication protocol

**Question**:
How does Terraform Core communicate with a provider plugin during execution?

- A) Through direct function calls within the same process binary
- B) Via HTTP REST API calls to a locally running provider web server
- C) Via gRPC, with the provider running as a separate process from Terraform Core
- D) Through shared memory mapped files in the `.terraform/` directory

**Answer**: C

**Explanation**:
Terraform Core and provider plugins run as **separate processes** that communicate over **gRPC**. This separation allows providers to be upgraded independently of Terraform Core. The provider binary in turn makes HTTPS API calls to the target cloud service.

---

### Question 4 — Provider Source Address Format

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Provider source address and default registry hostname

**Question**:
A `required_providers` block declares `source = "hashicorp/aws"`. What is the fully qualified source address that Terraform resolves this to?

- A) `github.com/hashicorp/aws`
- B) `registry.terraform.io/hashicorp/aws`
- C) `releases.hashicorp.com/hashicorp/aws`
- D) `hashicorp.com/terraform/providers/aws`

**Answer**: B

**Explanation**:
The full source address format is `<hostname>/<namespace>/<type>`. When the hostname is omitted, Terraform defaults to `registry.terraform.io`. So `hashicorp/aws` resolves to `registry.terraform.io/hashicorp/aws`.

---

### Question 5 — `terraform init` Provider Download

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Where terraform init installs providers

**Question**:
When `terraform init` is run, where are provider plugins downloaded to?

- A) `~/.terraform.d/plugins/`
- B) `terraform.tfstate`
- C) `.terraform/providers/`
- D) `providers.lock/`

**Answer**: C

**Explanation**:
`terraform init` downloads required provider plugins into the `.terraform/providers/` directory within the working directory. It also creates or updates the dependency lock file `.terraform.lock.hcl` to record the exact provider versions and their checksums.

---

### Question 6 — Dependency Lock File

**Difficulty**: Medium
**Answer Type**: one
**Topic**: `.terraform.lock.hcl` purpose and version control

**Question**:
What is the purpose of the `.terraform.lock.hcl` file, and how should it be treated with respect to version control?

- A) It records the current Terraform state and must never be committed to version control
- B) It records exact provider versions and checksums installed; it must be committed to version control
- C) It is a temporary cache file generated on each `terraform init` run and should be added to `.gitignore`
- D) It stores encrypted provider credentials and must be committed but kept private

**Answer**: B

**Explanation**:
`.terraform.lock.hcl` records the exact provider version installed, the version constraint from `required_providers`, and cryptographic hashes for verification. It **must be committed** to version control so all team members and CI pipelines use identical provider versions. Use `terraform init -upgrade` to update versions within constraints.

---

### Question 7 — Pessimistic Constraint Operator

**Difficulty**: Medium
**Answer Type**: one
**Topic**: `~>` version constraint operator behaviour

**Question**:
A `required_providers` block specifies `version = "~> 5.0"` for the AWS provider. Which versions are permitted by this constraint?

- A) Exactly version 5.0.0 only
- B) Any version >= 5.0.0 with no upper limit
- C) Any version >= 5.0 and < 6.0 (minor and patch updates within major version 5)
- D) Any version >= 5.0.0 and < 5.1.0 (patch updates only within minor version 5.0)

**Answer**: C

**Explanation**:
The pessimistic constraint operator `~>` allows updates to the rightmost version component. `~> 5.0` allows >= 5.0 and < 6.0 (minor and patch updates within major version 5). By contrast, `~> 5.0.0` would allow only patch updates (>= 5.0.0 and < 5.1.0). This is one of the most commonly tested version constraint questions on the exam.

---

### Question 8 — Provider Alias

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Provider alias for multiple configurations

**Question**:
When is a provider `alias` required in a Terraform configuration?

- A) Whenever a provider block is declared inside a module rather than the root module
- B) When more than one configuration of the same provider is needed, such as managing resources in multiple regions
- C) Whenever a provider version constraint is specified in the `required_providers` block
- D) When Terraform is run with a non-default workspace

**Answer**: B

**Explanation**:
A provider alias is required when you need multiple configurations of the same provider — for example, deploying to both `us-east-1` and `us-west-2` using the AWS provider, or managing two separate AWS accounts. The aliased provider is referenced on a resource using `provider = aws.alias_name`.

---

### Question 9 — What `terraform.tfstate` Stores

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Content and purpose of the Terraform state file

**Question**:
What does the `terraform.tfstate` file contain?

- A) The raw HCL configuration for all resources managed by Terraform
- B) A log of every `terraform apply` command that has been executed
- C) A JSON mapping of Terraform resource addresses to their real-world resource IDs and attributes
- D) The compiled binary representation of a Terraform execution plan

**Answer**: C

**Explanation**:
`terraform.tfstate` is a JSON file that maps each HCL resource (e.g., `aws_instance.web`) to its real-world identifier (e.g., `i-0abcd1234ef567890`) and all tracked attributes. This mapping is what allows Terraform to compute diffs, track metadata, and avoid querying every resource on every plan.

---

### Question 10 — Three Sources During Plan

**Difficulty**: Medium
**Answer Type**: many
**Topic**: Sources Terraform compares during `terraform plan`

**Question**:
When `terraform plan` runs, Terraform compares information from multiple sources to determine what changes are needed. Which TWO of the following are sources that Terraform uses during planning? (Select two.)

- A) The Terraform Registry API to check for provider updates
- B) The `.tf` configuration files representing the desired state
- C) The `terraform.tfstate` file representing the last-known resource state
- D) The `.terraform.lock.hcl` file representing installed provider versions

**Answer**: B, C

**Explanation**:
During `terraform plan`, Terraform compares three sources: the desired state (your `.tf` configuration), the known state (`terraform.tfstate`), and the actual state (live cloud resources queried via the provider API). The lock file and Registry are not part of the planning comparison — they are used during `terraform init`.

---

### Question 11 — Local vs Remote State

**Difficulty**: Hard
**Answer Type**: one
**Topic**: Differences between local and remote Terraform state

**Question**:
Which of the following is a characteristic of local Terraform state that makes it unsuitable for team environments?

- A) Local state files use a binary format that cannot be read or backed up
- B) Local state provides no locking mechanism, meaning concurrent `terraform apply` runs by different team members can corrupt state
- C) Local state is automatically deleted after each `terraform apply` completes
- D) Local state cannot store resource attribute values, only resource addresses

**Answer**: B

**Explanation**:
Local state (`terraform.tfstate` in the working directory) has no locking, no sharing, and no encryption. Without locking, two operators running `terraform apply` simultaneously can overwrite each other's state changes, causing corruption. Remote backends such as S3, Azure Blob, or HCP Terraform provide state locking, shared access, and optional encryption — making them required for all team and production workloads.

---

### Question 12 — `sensitive = true` and State

**Difficulty**: Hard
**Answer Type**: one
**Topic**: Behaviour of `sensitive = true` in outputs vs state storage

**Question**:
A Terraform output is declared with `sensitive = true`. What is the effect of this setting on how the value is handled?

- A) The value is encrypted with AES-256 before being written to `terraform.tfstate`
- B) The value is redacted from `terraform.tfstate` entirely and stored in a separate secrets file
- C) The value is masked in terminal output but is still stored in plaintext in `terraform.tfstate`
- D) The value is masked in terminal output and also removed from any remote backend storage

**Answer**: C

**Explanation**:
`sensitive = true` on an output value suppresses it from being displayed in terminal output during `terraform apply` or `terraform output`. However, it does **not** encrypt or remove the value from state — the attribute remains stored in plaintext in `terraform.tfstate`. To protect sensitive values at rest, you must use a remote backend with encryption (e.g., S3 with server-side encryption enabled).

---

### Question 13 — `terraform state` Commands

**Difficulty**: Medium
**Answer Type**: many
**Topic**: Terraform state CLI subcommands

**Question**:
Which TWO `terraform state` subcommands would be appropriate for inspecting state without modifying it? (Select two.)

- A) `terraform state rm`
- B) `terraform state list`
- C) `terraform state push`
- D) `terraform state show`

**Answer**: B, D

**Explanation**:
`terraform state list` lists all resource addresses currently tracked in state, and `terraform state show <address>` displays all attributes of a specific resource — both are read-only operations. By contrast, `terraform state rm` removes a resource from state (destructive), and `terraform state push` uploads a local state file to a remote backend (potentially overwriting it).

---

---

## Questions

---

### Question 1 — Core Workflow Sequence

**Difficulty**: Easy
**Answer Type**: one
**Topic**: Correct order of the core Terraform CLI workflow

**Question**:
Which of the following represents the correct core Terraform workflow sequence?

- A) `validate → init → fmt → plan → apply → destroy`
- B) `init → fmt → validate → plan → apply → destroy`
- C) `fmt → init → plan → validate → apply → destroy`
- D) `init → plan → validate → fmt → apply → destroy`

**Answer**: B

**Explanation**:
The standard Terraform workflow is: `init` (download providers/backend), `fmt` (format HCL), `validate` (check syntax and references), `plan` (preview changes), `apply` (provision resources), and finally `destroy` (tear down). Running `init` first is mandatory — no other command can succeed until the working directory is initialised.

---

### Question 2 — `terraform init` Purpose

**Difficulty**: Easy
**Answer Type**: one
**Topic**: What `terraform init` does

**Question**:
Which of the following is a primary action performed by `terraform init`?

- A) It applies all pending changes from the most recent execution plan
- B) It downloads required provider plugins into the `.terraform/` directory
- C) It validates that all resource configurations are syntactically correct
- D) It formats all `.tf` files in the working directory to canonical style

**Answer**: B

**Explanation**:
`terraform init` initialises the working directory. Its key actions include: downloading provider plugins to `.terraform/providers/`, creating or updating `.terraform.lock.hcl`, configuring the backend, and caching module source code to `.terraform/modules/`. It must be run before any other workflow command.

---

### Question 3 — When to Re-run `terraform init`

**Difficulty**: Medium
**Answer Type**: many
**Topic**: Conditions requiring `terraform init` to be re-run

**Question**:
In which TWO situations must `terraform init` be re-run? (Select two.)

- A) When a new provider is added to `required_providers`
- B) When an output value is added to an existing module
- C) When the backend configuration is changed to a different provider
- D) When a variable default value is updated in `variables.tf`

**Answer**: A, C

**Explanation**:
`terraform init` must be re-run when: (1) a new provider is added (the plugin needs to be downloaded), (2) the backend is changed or reconfigured (use `-migrate-state` or `-reconfigure`), or (3) a new module source is added. Adding output values or changing variable defaults does not require re-initialisation because no plugins or backend configuration changes occur.

---

### Question 4 — `terraform validate` Network Requirement

**Difficulty**: Medium
**Answer Type**: one
**Topic**: `terraform validate` network access and what it checks

**Question**:
Which statement correctly describes `terraform validate`?

- A) It requires active cloud provider credentials to verify that referenced resources exist in the target environment
- B) It performs a live API call to confirm that the AMI ID or other resource identifiers in the config are valid
- C) It checks configuration syntax and internal references without requiring network access or provider credentials
- D) It generates a full execution plan and outputs the number of resources that will be created, updated, or destroyed

**Answer**: C

**Explanation**:
`terraform validate` checks HCL syntax, ensures variables and references are valid, and confirms type compatibility — all without connecting to any provider API. It does **not** verify whether referenced cloud resources (e.g., an AMI ID) actually exist. This makes it safe to run in air-gapped or unauthenticated environments.

---

### Question 5 — `terraform fmt` Flags

**Difficulty**: Medium
**Answer Type**: one
**Topic**: `terraform fmt -check` flag behaviour

**Question**:
What is the purpose of the `-check` flag on `terraform fmt`?

- A) It checks that all variable names follow HashiCorp's naming conventions
- B) It validates the syntax of all HCL files but does not reformat them
- C) It exits with a non-zero exit code if any files need reformatting, without modifying them — useful for CI pipelines
- D) It checks whether provider versions are compatible with the current Terraform version

**Answer**: C

**Explanation**:
`terraform fmt -check` scans all `.tf` files and exits with code 1 if any file is not already in canonical format. It makes **no changes** to any file. This is the standard way to enforce formatting rules in a CI pipeline — the build fails if a developer submits unformatted code.

---

### Question 6 — `terraform plan -out` Flag

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Saving and applying a plan file

**Question**:
What is the benefit of running `terraform plan -out=plan.tfplan` followed by `terraform apply plan.tfplan`?

- A) It allows Terraform to skip provider validation when applying the plan
- B) It guarantees that the exact set of changes reviewed in `plan` is applied, with no drift between the two steps
- C) It compresses the plan file so that it can be stored in version control alongside `.tf` files
- D) It allows `terraform apply` to run without any state file present

**Answer**: B

**Explanation**:
When `terraform apply` is run without a saved plan, Terraform re-runs the plan internally — if infrastructure changed between the plan and apply, the actual changes may differ from what was reviewed. Saving the plan with `-out` and then applying it directly ensures the **exact** plan that was reviewed is what gets executed, which is the recommended practice for production workflows and CI/CD pipelines.

---

### Question 7 — Plan Output Symbols

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Meaning of `terraform plan` output symbols

**Question**:
In `terraform plan` output, what does the symbol `-/+` indicate will happen to a resource?

- A) The resource will be updated in-place with no interruption
- B) The resource will be imported into state from an existing infrastructure object
- C) The resource will be destroyed and then recreated (replacement)
- D) The resource will be moved to a different Terraform workspace

**Answer**: C

**Explanation**:
The four plan symbols are: `+` (create), `~` (update in-place), `-` (destroy), and `-/+` (destroy then recreate — replacement). A replacement occurs when a change to a resource argument requires destroying the existing object and creating a new one, such as changing the `ami` attribute on an `aws_instance`.

---

### Question 8 — `terraform apply -auto-approve`

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Purpose and use case of `-auto-approve`

**Question**:
What does the `-auto-approve` flag do when passed to `terraform apply`?

- A) It automatically selects the most recent saved plan file in the working directory
- B) It skips the interactive confirmation prompt before applying changes — commonly used in CI/CD pipelines
- C) It approves all individual resource creation steps sequentially without pausing
- D) It causes Terraform to apply changes to approved resources only and skip unapproved ones

**Answer**: B

**Explanation**:
By default, `terraform apply` prints the execution plan and requires the user to type `yes` before proceeding. The `-auto-approve` flag suppresses this prompt, allowing the command to run non-interactively. It is commonly used in CI/CD pipelines where human interaction is not possible, but should be used with caution in production environments.

---

### Question 9 — `terraform apply -replace`

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Forcing resource replacement with `-replace`

**Question**:
Which command is the current (Terraform 1.5+) recommended way to force a specific resource to be destroyed and recreated on the next apply?

- A) `terraform taint aws_instance.web`
- B) `terraform apply -replace="aws_instance.web"`
- C) `terraform destroy -target=aws_instance.web` followed by `terraform apply`
- D) `terraform state rm aws_instance.web` followed by `terraform apply`

**Answer**: B

**Explanation**:
`terraform apply -replace="<address>"` is the current approach for forcing a resource recreation. The older `terraform taint` command has been deprecated since Terraform 1.5. While `state rm` followed by `apply` would also recreate the resource, it removes the resource from state first (losing tracked attributes), which is a different and more disruptive operation.

---

### Question 10 — `terraform output -raw`

**Difficulty**: Medium
**Answer Type**: one
**Topic**: `terraform output -raw` use case

**Question**:
What does `terraform output -raw db_password` return, and when is this flag useful?

- A) The output value formatted as a JSON object with metadata fields
- B) The raw string value with no surrounding quotes — useful when piping the value into scripts or other commands
- C) The encrypted form of the output value for use with external secrets managers
- D) A diff showing the current output value versus the previous apply's value

**Answer**: B

**Explanation**:
`terraform output -raw <name>` prints the string value of a named output with no surrounding quotes or newline padding. Without `-raw`, string outputs are printed with double quotes (e.g., `"mypassword"`). The raw form is useful when piping the value to another command such as `aws secretsmanager put-secret-value --secret-string $(terraform output -raw db_password)`.

---

### Question 11 — `terraform console` Purpose

**Difficulty**: Medium
**Answer Type**: one
**Topic**: What `terraform console` is used for

**Question**:
What is the primary purpose of `terraform console`?

- A) To display the current Terraform state in an interactive paginated viewer
- B) To provide an interactive REPL where Terraform expressions and built-in functions can be tested
- C) To monitor the progress of a running `terraform apply` operation in real time
- D) To inspect and modify resource attributes in the state file interactively

**Answer**: B

**Explanation**:
`terraform console` launches an interactive Read-Eval-Print Loop (REPL) that evaluates HCL expressions against the current state and configuration. It is primarily used to test functions (e.g., `length(["a","b","c"])`) and expressions before using them in configuration files. It does not modify state.

---

### Question 12 — `terraform destroy` Equivalence

**Difficulty**: Hard
**Answer Type**: one
**Topic**: Relationship between `terraform destroy` and `terraform apply -destroy`

**Question**:
Which statement about `terraform destroy` is correct?

- A) `terraform destroy` permanently deletes the state file after all resources are removed
- B) `terraform destroy` is equivalent to `terraform apply -destroy` and both prompt for confirmation by default
- C) `terraform destroy` only removes resources created in the current workspace, while `terraform apply -destroy` removes all workspaces
- D) `terraform destroy` is deprecated and has been replaced by `terraform apply -destroy` in Terraform 1.5+

**Answer**: B

**Explanation**:
`terraform destroy` is a convenience alias for `terraform apply -destroy`. Both commands plan and execute the destruction of all resources managed by the current configuration, and both prompt for interactive confirmation unless `-auto-approve` is supplied. Neither deletes the state file — they update it to reflect that all resources have been removed.

---

### Question 13 — `terraform fmt` and `terraform validate` Scope

**Difficulty**: Hard
**Answer Type**: many
**Topic**: Distinguishing what `fmt` and `validate` check

**Question**:
Which TWO of the following issues would `terraform validate` detect but `terraform fmt` would NOT? (Select two.)

- A) Inconsistent indentation in a `resource` block
- B) A variable referenced in a resource block that is not declared anywhere in the configuration
- C) Misaligned `=` signs in argument assignments
- D) An unsupported argument name passed to a resource type

**Answer**: B, D

**Explanation**:
`terraform fmt` only applies cosmetic formatting — it fixes indentation, alignment, and whitespace but cannot detect logical or semantic errors. `terraform validate` checks for: undeclared variables or references (B), unsupported argument names for a given resource type (D), type mismatches, and invalid module inputs. Indentation issues (A) and misaligned `=` signs (C) are purely formatting concerns that `fmt` corrects but `validate` ignores.

---

---

## Questions

---

### Question 1 — Resource Block Syntax

**Difficulty**: Easy
**Answer Type**: one
**Topic**: Resource block syntax and components

**Question**:
Which of the following correctly shows the required structure of a Terraform resource block?

- A) `resource { type = "aws_instance" name = "web" }`
- B) `resource "aws_instance" "web" { ... }`
- C) `resource aws_instance web { ... }`
- D) `provider "aws_instance" "web" { ... }`

**Answer**: B

**Explanation**:
A resource block requires two labels after the `resource` keyword: the provider type (e.g., `aws_instance`) and the local name (e.g., `web`), both in double quotes, followed by a configuration block in `{ }`. The local name is used to reference this resource elsewhere in the configuration as `aws_instance.web`.

---

### Question 2 — Data Source Purpose

**Difficulty**: Easy
**Answer Type**: one
**Topic**: What a data source does

**Question**:
What is the purpose of a `data` block in a Terraform configuration?

- A) To define a new cloud resource that Terraform will create and manage
- B) To query an existing infrastructure object in read-only mode without creating or managing it
- C) To store sensitive values such as passwords and API keys securely
- D) To declare default values for input variables used across modules

**Answer**: B

**Explanation**:
A `data` block (data source) queries existing infrastructure in read-only mode. It retrieves information about a pre-existing resource — such as an AMI ID or a VPC ID — that Terraform did not create. Data sources never create, update, or destroy resources; they only read and expose attributes for use in the configuration.

---

### Question 3 — Data Source Reference Format

**Difficulty**: Medium
**Answer Type**: one
**Topic**: How to reference a data source attribute

**Question**:
A data source is declared as `data "aws_ami" "ubuntu" { ... }`. What is the correct syntax to reference its `id` attribute in a resource block?

- A) `aws_ami.ubuntu.id`
- B) `data.ubuntu.aws_ami.id`
- C) `data.aws_ami.ubuntu.id`
- D) `source.aws_ami.ubuntu.id`

**Answer**: C

**Explanation**:
Data source attributes are referenced using `data.<TYPE>.<NAME>.<ATTRIBUTE>`. For a data source declared as `data "aws_ami" "ubuntu"`, the `id` attribute is accessed as `data.aws_ami.ubuntu.id`. This is distinct from resource references, which omit the `data.` prefix (e.g., `aws_instance.web.id`).

---

### Question 4 — Meta-Arguments Available to All Resources

**Difficulty**: Medium
**Answer Type**: many
**Topic**: Resource meta-arguments

**Question**:
Which TWO of the following are valid meta-arguments that can be added to any Terraform resource block? (Select two.)

- A) `source`
- B) `depends_on`
- C) `backend`
- D) `lifecycle`

**Answer**: B, D

**Explanation**:
Meta-arguments are special arguments supported by all resource blocks regardless of provider. The five meta-arguments are: `count`, `for_each`, `depends_on`, `provider`, and `lifecycle`. `source` is used in `required_providers` and `module` blocks, not resource blocks. `backend` is a root-level configuration block, not a resource argument.

---

### Question 5 — Implicit vs Explicit Dependencies

**Difficulty**: Medium
**Answer Type**: one
**Topic**: How implicit dependencies are created

**Question**:
What causes Terraform to automatically create an implicit dependency between two resources?

- A) Both resources sharing the same provider configuration
- B) One resource's argument referencing an attribute of another resource (e.g., `aws_vpc.main.id`)
- C) Both resources being declared in the same `.tf` file
- D) A `var.*` or `local.*` value being used in both resource blocks

**Answer**: B

**Explanation**:
Terraform builds its dependency graph by scanning for attribute references between resources. When resource B uses `aws_vpc.main.id` as an argument value, Terraform infers that B depends on A and ensures A is created first. References to `var.*` and `local.*` do **not** create dependency edges because variables and locals are not resources.

---

### Question 6 — `depends_on` Use Case

**Difficulty**: Medium
**Answer Type**: one
**Topic**: When to use `depends_on`

**Question**:
In which situation should `depends_on` be used in a Terraform resource block?

- A) To define the order in which output values are displayed after `terraform apply`
- B) To force a resource to be replaced instead of updated in-place
- C) To express a dependency that Terraform cannot detect through attribute references, such as an IAM policy attachment
- D) To ensure a resource is created before any data sources in the configuration are read

**Answer**: C

**Explanation**:
`depends_on` is used for dependencies that exist in the real world but are not expressed through attribute references. The canonical example is an IAM policy: an EC2 instance may need an IAM role policy to be fully attached before the instance starts, but Terraform cannot detect this relationship through HCL references alone. Overusing `depends_on` reduces Terraform's ability to parallelise operations.

---

### Question 7 — `lifecycle` `create_before_destroy`

**Difficulty**: Medium
**Answer Type**: one
**Topic**: `create_before_destroy` lifecycle argument

**Question**:
What is the effect of setting `create_before_destroy = true` in a resource's `lifecycle` block?

- A) Terraform creates a backup of the resource's state before applying any destroy operation
- B) Terraform provisions the replacement resource first and only destroys the old resource after the new one is ready, minimising downtime
- C) Terraform creates the resource before any `terraform plan` is executed
- D) Terraform ensures the resource is created before all other resources in the configuration, regardless of dependencies

**Answer**: B

**Explanation**:
By default, when a resource must be replaced (e.g., changing an immutable attribute), Terraform destroys the old resource first, then creates the new one. Setting `create_before_destroy = true` reverses this order — the replacement is created first, and only after it is successfully provisioned is the old resource destroyed. This is commonly used for load balancer target groups, certificates, and other resources where downtime must be avoided.

---

### Question 8 — `lifecycle` `prevent_destroy`

**Difficulty**: Medium
**Answer Type**: one
**Topic**: `prevent_destroy` lifecycle argument

**Question**:
What happens when `prevent_destroy = true` is set in a resource's `lifecycle` block and a plan includes destroying that resource?

- A) Terraform skips the destroy step and leaves the resource unchanged without any error
- B) Terraform prompts the user for a special override passphrase before allowing the destroy
- C) Terraform returns an error and refuses to create a plan that includes destroying the resource
- D) Terraform creates a backup of the resource in a separate workspace before destroying it

**Answer**: C

**Explanation**:
`prevent_destroy = true` instructs Terraform to raise an error if any execution plan would destroy that resource. This acts as a guardrail against accidental deletion of critical infrastructure like production databases or networking resources. To destroy such a resource intentionally, you must first remove the `prevent_destroy` setting from the configuration.

---

### Question 9 — `lifecycle` `ignore_changes`

**Difficulty**: Medium
**Answer Type**: one
**Topic**: `ignore_changes` lifecycle argument

**Question**:
What is the purpose of the `ignore_changes` argument in a resource's `lifecycle` block?

- A) It prevents Terraform from reading the resource's current state during `terraform plan`
- B) It tells Terraform to ignore drift on specified attributes, so changes to those attributes outside Terraform do not trigger an update
- C) It suppresses `terraform plan` output for the listed attributes to keep logs concise
- D) It forces Terraform to skip validation of the listed arguments during `terraform validate`

**Answer**: B

**Explanation**:
`ignore_changes` accepts a list of attribute names. When Terraform detects drift on a listed attribute (i.e., the real-world value differs from the state value), it ignores the difference and does not plan an update. This is useful for attributes managed externally — for example, an Auto Scaling Group's `desired_capacity` that is adjusted by AWS automatically and should not be reverted by Terraform on each apply.

---

### Question 10 — `replace_triggered_by` Lifecycle Argument

**Difficulty**: Medium
**Answer Type**: one
**Topic**: `replace_triggered_by` lifecycle argument

**Question**:
What does the `replace_triggered_by` argument in a `lifecycle` block do?

- A) It replaces the resource's provider with the one specified in the argument list
- B) It causes the resource to be destroyed and recreated whenever any resource or attribute listed in the argument changes
- C) It triggers a `terraform plan` automatically when a listed resource is modified outside Terraform
- D) It forces the resource to be replaced on every `terraform apply` regardless of any changes

**Answer**: B

**Explanation**:
`replace_triggered_by` accepts a list of resource references or resource attribute references. When any of the referenced items change (even if the current resource's own arguments have not changed), Terraform marks the resource for replacement (destroy + create). A common use case is replacing an Auto Scaling Group when its launch template is updated.

---

### Question 11 — `moved` Block Purpose

**Difficulty**: Hard
**Answer Type**: one
**Topic**: What the `moved` block does in Terraform state

**Question**:
What is the purpose of the `moved` block in Terraform?

- A) It migrates a resource to a different cloud provider without destroying and recreating it
- B) It renames or relocates a resource address in the state file without destroying and recreating the real infrastructure
- C) It moves a resource's configuration from one `.tf` file to another and updates imports automatically
- D) It transfers a resource's state to a different Terraform workspace while keeping the resource in the current cloud account

**Answer**: B

**Explanation**:
The `moved` block tells Terraform that a resource previously tracked under one address (e.g., `aws_instance.old_name`) is now known under a different address (e.g., `aws_instance.new_name`). Terraform updates the state file to reflect the new address without issuing any API calls to destroy or recreate the real resource. This is essential when refactoring configuration or moving resources into modules.

---

### Question 12 — Default Parallelism

**Difficulty**: Hard
**Answer Type**: one
**Topic**: Terraform default parallelism and the `-parallelism` flag

**Question**:
What is the default number of concurrent operations Terraform uses during `terraform apply`, and how can it be changed?

- A) Default is 5; change with `terraform apply -concurrent=10`
- B) Default is 10; change with `terraform apply -parallelism=<n>`
- C) Default is unlimited; Terraform always maximises concurrency up to available CPU cores
- D) Default is 1 (sequential); change with `terraform apply -parallel=true`

**Answer**: B

**Explanation**:
Terraform applies resource operations in parallel for resources with no inter-dependencies, with a default concurrency of 10. This can be tuned with `-parallelism=<n>` on `plan`, `apply`, or `destroy`. The dependency graph (DAG) determines which operations can safely run in parallel; only independent resources are processed concurrently.

---

### Question 13 — When Data Sources Are Read

**Difficulty**: Medium
**Answer Type**: many
**Topic**: Timing of data source reads during plan and apply

**Question**:
During which TWO phases can a Terraform data source be read? (Select two.)

- A) During `terraform init`, when providers are downloaded
- B) During the `plan` phase, when the data source's query arguments are fully known
- C) During the `apply` phase, when the data source's query arguments depend on a value not known until apply
- D) During `terraform validate`, when syntax is checked

**Answer**: B, C

**Explanation**:
Data sources are typically read during the **plan** phase so their results can inform the plan output. However, if a data source's arguments depend on a value that is only computed during apply (such as the ID of a resource being created in the same run), the data source read is deferred to the **apply** phase. `terraform init` and `terraform validate` do not read data sources.

---

---

## Questions

---

### Question 1 — Variable Input Precedence

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Order of variable value precedence (highest wins)

**Question**:
A Terraform variable named `region` has a `default` of `"us-east-1"` in its declaration, a value of `"eu-west-1"` in `terraform.tfvars`, and is also set via `TF_VAR_region=ap-southeast-1` in the shell environment. Which value does Terraform use?

- A) `"us-east-1"` — the `default` in the variable block always wins
- B) `"eu-west-1"` — `terraform.tfvars` overrides environment variables
- C) `"ap-southeast-1"` — `TF_VAR_*` environment variables have higher precedence than `.tfvars` files
- D) Terraform raises an error because the variable is set in multiple places

**Answer**: C

**Explanation**:
Terraform's variable precedence order from highest to lowest is: CLI `-var` flag and `TF_VAR_*` environment variables (tied at top) → `*.auto.tfvars` files → `terraform.tfvars` → `-var-file` flag → `default` in the variable block. Because `TF_VAR_region` and CLI `-var` share the highest level, `TF_VAR_region=ap-southeast-1` overrides the value in `terraform.tfvars`. Terraform does not error when a variable is set from multiple sources.

---

### Question 2 — Variable Block Argument: `sensitive`

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Effect of `sensitive = true` on variables vs state

**Question**:
What is the effect of declaring `sensitive = true` on an input variable?

- A) The variable's value is encrypted before being stored in `terraform.tfstate`
- B) The variable's value is hidden in terminal output during `plan` and `apply` but is still stored in plaintext in the state file
- C) The variable's value is excluded from the state file entirely
- D) The variable cannot be passed via environment variables — only via `-var` flag

**Answer**: B

**Explanation**:
`sensitive = true` causes Terraform to redact the variable's value from terminal output (showing `(sensitive value)` in plans and applies). It does **not** encrypt or omit the value from `terraform.tfstate` — the value is still stored in plaintext. Protecting sensitive values at rest requires an encrypted remote backend.

---

### Question 3 — Validation Block Scope

**Difficulty**: Medium
**Answer Type**: one
**Topic**: What a variable `validation` block can reference

**Question**:
Which of the following expressions is valid inside a variable's `validation` block `condition` argument?

- A) `length(aws_instance.web.id) > 0`
- B) `local.environment != ""`
- C) `contains(["dev", "staging", "prod"], var.environment)`
- D) `data.aws_ami.ubuntu.id != ""`

**Answer**: C

**Explanation**:
A `validation` block's `condition` argument can **only** reference `var.<name>` — the variable being validated. It cannot reference resources, data sources, locals, or other variables. This is because validation runs before planning, at a point when no infrastructure state or computed values are available. Option C is valid because it only uses `var.environment`.

---

### Question 4 — Locals vs Input Variables

**Difficulty**: Easy
**Answer Type**: one
**Topic**: Difference between `locals` and `variable` blocks

**Question**:
What is the key difference between a `locals` block and a `variable` block in Terraform?

- A) Locals can only hold string values; variables can hold any type
- B) Variables are external inputs that can be set by the caller; locals are internal computed values that cannot be set from outside the module
- C) Locals are shared across all modules in a configuration; variables are scoped to a single module
- D) Variables must always have a `default` value; locals do not require a value expression

**Answer**: B

**Explanation**:
`variable` blocks define the external interface of a module — their values can be set by the user via CLI, `.tfvars` files, or environment variables. `locals` are internal to the module; they compute intermediate values from other expressions and cannot be overridden by the module's callers. Locals are referenced as `local.<name>` and appear in neither the module's input nor output interface.

---

### Question 5 — Module Output Reference Syntax

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Referencing a child module's output value

**Question**:
A root configuration uses a child module declared as `module "network" { ... }`. The child module has an output named `vpc_id`. What is the correct way to reference this output in the root module?

- A) `network.vpc_id`
- B) `output.network.vpc_id`
- C) `module.network.vpc_id`
- D) `var.network.vpc_id`

**Answer**: C

**Explanation**:
Child module output values are referenced from the parent using `module.<module_label>.<output_name>`. For a module declared as `module "network"`, the `vpc_id` output is accessed as `module.network.vpc_id`. This creates an implicit dependency: any resource using this reference will not be created until the `network` module has applied successfully.

---

### Question 6 — `count` vs `for_each` — Preferred Usage

**Difficulty**: Easy
**Answer Type**: one
**Topic**: When to prefer `for_each` over `count`

**Question**:
Why is `for_each` generally preferred over `count` when creating multiple resource instances in Terraform?

- A) `for_each` supports more resource types than `count`
- B) `for_each` uses named keys to identify instances, so removing one item does not force recreation of all subsequent instances
- C) `for_each` is faster to apply because it uses parallel execution; `count` is sequential
- D) `for_each` allows resources to span multiple providers; `count` is limited to a single provider

**Answer**: B

**Explanation**:
With `count`, resource instances are addressed by numeric index (e.g., `resource[0]`, `resource[1]`). If an element is removed from the middle of the list, all instances after it are renumbered and recreated. `for_each` addresses instances by stable string keys (e.g., `resource["web"]`), so removing one key only affects that single instance. This makes `for_each` the recommended choice whenever instances have a meaningful identity.

---

### Question 7 — `count.index` and Splat Expressions

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Accessing `count`-based resource instances

**Question**:
A resource is declared with `count = 3`. What does the splat expression `aws_instance.web[*].id` return?

- A) The ID of the first instance only (`aws_instance.web[0].id`)
- B) A map of index-to-ID pairs: `{ 0 = "i-aaa", 1 = "i-bbb", 2 = "i-ccc" }`
- C) A list containing the `id` attribute of all three instances
- D) An error — splat expressions only work with `for_each`, not `count`

**Answer**: C

**Explanation**:
The splat expression `[*]` extracts a named attribute from every element in a list-like collection and returns a list. For a resource with `count = 3`, `aws_instance.web[*].id` returns a list of all three IDs: `["i-aaa", "i-bbb", "i-ccc"]`. Splat works with `count`-based resources; `for_each`-based resources use `values(resource_type.name)[*].attribute` or a `for` expression instead.

---

### Question 8 — `for_each` with a Set — `each.key` vs `each.value`

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Behaviour of `each.key` and `each.value` when `for_each` uses a set

**Question**:
When `for_each` is assigned a **set** of strings (e.g., `toset(["alice", "bob"])`), what is the relationship between `each.key` and `each.value` inside the resource block?

- A) `each.key` is the zero-based index; `each.value` is the string element
- B) `each.key` and `each.value` are both equal to the set element string
- C) `each.key` is the set element string; `each.value` is always `null` for sets
- D) Sets do not support `each.key` — only `each.value` is available

**Answer**: B

**Explanation**:
For a map, `each.key` is the map key and `each.value` is the corresponding value. For a **set**, because set elements have no separate key and value, both `each.key` and `each.value` are set to the element itself. This means you can use either `each.key` or `each.value` interchangeably when iterating over a set with `for_each`.

---

### Question 9 — `for` Expression with Filter

**Difficulty**: Medium
**Answer Type**: one
**Topic**: `for` expression syntax with an `if` filter clause

**Question**:
Which `for` expression correctly produces a list of names from `var.names` that are longer than 4 characters?

- A) `[for name in var.names : name where length(name) > 4]`
- B) `[for name in var.names : name if length(name) > 4]`
- C) `[for name in var.names | length(name) > 4 : name]`
- D) `filter(var.names, n => length(n) > 4)`

**Answer**: B

**Explanation**:
Terraform's `for` expression supports an optional `if` clause to filter elements: `[for <item> in <collection> : <value> if <condition>]`. The `if` keyword appears after the value expression and filters out elements where the condition is false. Options A, C, and D use invalid syntax — Terraform's `for` expressions do not use `where`, pipe filtering, or a `filter()` function.

---

### Question 10 — `lookup` Function

**Difficulty**: Medium
**Answer Type**: one
**Topic**: `lookup()` function signature and default value

**Question**:
What does `lookup({a = 1, b = 2}, "c", 99)` return?

- A) `null` — the key `"c"` does not exist in the map
- B) An error — `lookup` raises an exception when the key is not found
- C) `99` — the third argument is returned as the default when the key is not found
- D) `0` — `lookup` always returns 0 for missing numeric map entries

**Answer**: C

**Explanation**:
`lookup(map, key, default)` retrieves the value for `key` from `map`, or returns `default` if the key does not exist. In this case, the key `"c"` is absent from `{a = 1, b = 2}`, so the function returns the default value `99`. Always providing a default to `lookup` is recommended to prevent errors from missing keys.

---

### Question 11 — `cidrsubnet` Function

**Difficulty**: Hard
**Answer Type**: one
**Topic**: `cidrsubnet()` function parameters and result

**Question**:
What does `cidrsubnet("10.0.0.0/16", 8, 2)` return?

- A) `"10.0.0.0/24"`
- B) `"10.0.1.0/24"`
- C) `"10.0.2.0/24"`
- D) `"10.2.0.0/24"`

**Answer**: C

**Explanation**:
`cidrsubnet(prefix, newbits, netnum)` divides a CIDR block into subnets. It borrows `newbits` (8) additional bits from the host portion, making the new prefix length 16 + 8 = /24. Then it selects the `netnum`-th (2nd) subnet in that space. The subnets in order are: `10.0.0.0/24` (netnum 0), `10.0.1.0/24` (netnum 1), `10.0.2.0/24` (netnum 2). So the result is `"10.0.2.0/24"`.

---

### Question 12 — `flatten` vs `compact` Functions

**Difficulty**: Hard
**Answer Type**: many
**Topic**: Distinguishing `flatten()` and `compact()` use cases

**Question**:
Which TWO statements correctly describe the difference between `flatten()` and `compact()`? (Select two.)

- A) `flatten(["a", ["b", "c"]])` returns `["a", "b", "c"]` by removing nested list structure
- B) `compact(["a", "", null, "b"])` returns `["a", "b"]` by removing empty strings and null values
- C) `flatten()` removes duplicate values from a flat list
- D) `compact()` recursively unwraps nested lists into a single flat list

**Answer**: A, B

**Explanation**:
`flatten()` takes a list that may contain nested lists and returns a single flat list — it collapses nesting, not duplicates. `compact()` takes a flat list of strings and removes any empty string (`""`) or `null` elements, returning only non-empty values. `flatten` does not deduplicate (use `distinct()` for that), and `compact` does not unwrap nesting.

---

### Question 13 — `templatefile` vs `file` Functions

**Difficulty**: Medium
**Answer Type**: many
**Topic**: When to use `templatefile()` instead of `file()`

**Question**:
Which TWO statements correctly describe the difference between `file()` and `templatefile()`? (Select two.)

- A) `file(path)` reads the file content as a raw string with no variable substitution
- B) `templatefile(path, vars)` renders the file as a template, substituting `${var_name}` placeholders with values from the `vars` map
- C) `file()` supports `.tpl` template files; `templatefile()` only supports `.txt` files
- D) `templatefile()` can only reference Terraform input variables; it cannot reference locals or computed values

**Answer**: A, B

**Explanation**:
`file(path)` reads and returns the raw content of a file exactly as-is, with no template processing. `templatefile(path, vars)` reads the file and renders it as a template, replacing `${var_name}` placeholders with the values provided in the `vars` map — useful for generating EC2 user-data scripts or configuration files. Both functions can work with any file extension; the `.tpl` convention is a naming practice, not a requirement.

---

---

## Questions

---

### Question 1 — Three Condition Mechanisms Overview

**Difficulty**: Easy
**Answer Type**: one
**Topic**: The three Terraform condition mechanisms and where each is declared

**Question**:
Which of the following correctly lists all three Terraform mechanisms for asserting conditions on infrastructure?

- A) `assert` block, `check` block, `guard` block
- B) `validation` block, `precondition`/`postcondition` in `lifecycle`, `check` block
- C) `validation` block, `check` block, `enforce` block
- D) `precondition` block, `postcondition` block, `verify` block

**Answer**: B

**Explanation**:
Terraform provides three condition assertion mechanisms: (1) `validation` blocks inside `variable` declarations for validating input values before planning, (2) `precondition` and `postcondition` blocks inside a resource's `lifecycle` block for asserting conditions before and after resource changes, and (3) top-level `check` blocks for continuous infrastructure health assertions that produce warnings without blocking applies.

---

### Question 2 — `validation` Block — When It Runs

**Difficulty**: Easy
**Answer Type**: one
**Topic**: When variable `validation` blocks are evaluated

**Question**:
When does a `validation` block inside a `variable` declaration run?

- A) After `terraform apply` completes, to verify the applied configuration
- B) During `terraform init`, when providers are downloaded
- C) Before `terraform plan`, as part of input variable evaluation
- D) Only when explicitly triggered by `terraform validate`

**Answer**: C

**Explanation**:
Variable `validation` blocks run before `terraform plan` evaluates any infrastructure — they are evaluated as part of input variable processing. If the `condition` expression returns false, Terraform displays the `error_message` and halts before generating the plan. This early failure prevents invalid inputs from reaching the planning stage.

---

### Question 3 — `validation` Block Condition Constraints

**Difficulty**: Medium
**Answer Type**: one
**Topic**: What a `validation` condition can reference

**Question**:
Which restriction applies to the `condition` expression inside a variable `validation` block?

- A) It must return a number, which is compared to zero to determine pass/fail
- B) It can only reference `var.<variable_name>` — not resources, data sources, or locals
- C) It must use only built-in string functions; numeric comparisons are not allowed
- D) It can reference any variable in the same module but not variables from child modules

**Answer**: B

**Explanation**:
A `validation` block's `condition` is restricted to referencing only `var.<variable_name>` — the variable being validated. This restriction exists because validation runs before planning, when no resource, data source, or local values are available. Options C and D describe nonexistent restrictions; numeric comparisons are perfectly valid in validation conditions.

---

### Question 4 — `precondition` vs `postcondition` — Timing

**Difficulty**: Medium
**Answer Type**: one
**Topic**: When `precondition` and `postcondition` run relative to resource changes

**Question**:
What is the key timing difference between a `precondition` and a `postcondition` in a resource's `lifecycle` block?

- A) `precondition` runs during `terraform plan`; `postcondition` runs during `terraform validate`
- B) `precondition` runs before the resource is changed during apply; `postcondition` runs after the resource change completes
- C) `precondition` validates input variables; `postcondition` validates output values
- D) Both run at the same time — the distinction is only in the error message text

**Answer**: B

**Explanation**:
`precondition` is evaluated before Terraform applies a change to the resource. If it fails, the apply is halted before the resource is modified. `postcondition` is evaluated after the resource change completes and can reference `self` to inspect the resulting resource attributes. If a postcondition fails, the apply is marked as failed even though the resource was already changed.

---

### Question 5 — `self` in `postcondition`

**Difficulty**: Medium
**Answer Type**: one
**Topic**: The `self` reference available in `postcondition` blocks

**Question**:
What does `self` refer to in a `postcondition` block within a resource's `lifecycle`?

- A) The Terraform module that contains the resource
- B) The provider that manages the resource
- C) The resource instance that was just created or updated
- D) The previous state of the resource before the change

**Answer**: C

**Explanation**:
In a `postcondition` block, `self` is a special reference that points to the resource instance that was just created or updated during the current apply. This allows the postcondition to inspect the actual resulting attributes — for example, checking that `self.public_ip != null` to confirm a public IP was assigned. `self` is only available in `postcondition`, not in `precondition`.

---

### Question 6 — `check` Block Failure Behaviour

**Difficulty**: Medium
**Answer Type**: one
**Topic**: How a failing `check` block assertion affects `terraform apply`

**Question**:
What happens when an `assert` condition inside a `check` block evaluates to `false` during `terraform apply`?

- A) The apply is immediately halted and all changes are rolled back
- B) Terraform pauses and prompts the user to confirm whether to continue despite the failed assertion
- C) A warning is displayed but the apply continues and completes successfully
- D) The resource associated with the `check` block is marked as tainted for replacement on the next run

**Answer**: C

**Explanation**:
The `check` block is intentionally designed to be non-blocking. When an `assert` condition fails, Terraform emits a warning message but does **not** fail the apply. This makes `check` blocks suitable for continuous health monitoring — for example, verifying an HTTP endpoint returns a 200 status code after deployment — without risking accidental apply failures that would block infrastructure changes.

---

### Question 7 — `check` Block Introduction Version

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Which Terraform version introduced the `check` block

**Question**:
In which version of Terraform was the `check` block introduced?

- A) Terraform 1.0
- B) Terraform 1.3
- C) Terraform 1.5
- D) Terraform 1.7

**Answer**: C

**Explanation**:
The `check` block was introduced in **Terraform 1.5**. It provides a top-level mechanism for asserting infrastructure health conditions on every plan and apply, producing warnings rather than errors when assertions fail. The same release also introduced the HCL `import` block for managing existing resource imports declaratively.

---

### Question 8 — `check` Block Optional Data Source

**Difficulty**: Medium
**Answer Type**: one
**Topic**: The optional scoped data source inside a `check` block

**Question**:
What is the purpose of including a `data` block inside a `check` block?

- A) To import an existing resource into state as part of the health check
- B) To provide a scoped, read-only data source that is used only within that `check` block's assertions
- C) To declare a dependency so the check runs after a specific resource is created
- D) To override the provider used for the assertion data retrieval

**Answer**: B

**Explanation**:
A `check` block can optionally contain a nested `data` block that is scoped exclusively to that check. This allows the assertion to query live infrastructure (for example, making an HTTP request to a health endpoint) using data that is not needed anywhere else in the configuration. The scoped `data` block does not affect the rest of the configuration's dependency graph.

---

### Question 9 — Sensitive Output `sensitive = true`

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Effect of `sensitive = true` on an `output` block

**Question**:
An output block is declared with `sensitive = true`. What is the effect on how Terraform handles this output?

- A) The output is encrypted with a provider-managed key before being stored in state
- B) The output value is shown in plan output but hidden during `terraform output` commands
- C) The output value is redacted in terminal display but still stored in plaintext in the state file
- D) The output is excluded from `terraform output` and cannot be retrieved programmatically

**Answer**: C

**Explanation**:
Marking an output as `sensitive = true` causes Terraform to display `(sensitive value)` instead of the actual value in terminal output during `plan`, `apply`, and `terraform output`. However, the value is still written in plaintext to `terraform.tfstate`. To actually protect sensitive output values, you must use a remote backend with encryption at rest and restrict access to the state file.

---

### Question 10 — Sensitive Data in State — Critical Fact

**Difficulty**: Hard
**Answer Type**: one
**Topic**: How `sensitive = true` interacts with `terraform.tfstate` storage

**Question**:
A team marks their database password variable and output as `sensitive = true`. A new engineer asks why the password is still visible when they open `terraform.tfstate` in a text editor. What is the correct explanation?

- A) The password is only encrypted if the team has enabled KMS integration in the provider block
- B) `sensitive = true` protects values in transit between modules but not in the final state file
- C) `sensitive = true` only controls terminal display — all attribute values are always stored in plaintext in the state file regardless of this setting
- D) The state file should be unreadable — the engineer must have the wrong version of Terraform

**Answer**: C

**Explanation**:
`sensitive = true` is purely a display control. It prevents the value from appearing in `terraform plan` and `terraform apply` terminal output. It has no effect on how the value is stored in `terraform.tfstate` — all resource and output attribute values, including those marked sensitive, are stored in **plaintext JSON** in the state file. Protecting secrets at rest requires using an encrypted remote backend (such as S3 with SSE, or HCP Terraform) and restricting who can access the state file.

---

### Question 11 — Mitigations for Sensitive Data in State

**Difficulty**: Hard
**Answer Type**: many
**Topic**: Recommended approaches to protect sensitive values stored in Terraform state

**Question**:
Which TWO of the following are correct mitigations for the risk that sensitive values are stored in plaintext in Terraform state? (Select two.)

- A) Set `sensitive = true` on all variables and outputs containing secrets
- B) Use a remote backend that supports encryption at rest, such as S3 with server-side encryption or HCP Terraform
- C) Never commit `terraform.tfstate` to source control and restrict access to the state storage location
- D) Use the `prevent_destroy` lifecycle argument to prevent state files from being accidentally deleted

**Answer**: B, C

**Explanation**:
`sensitive = true` (option A) only masks terminal output and does not protect data in state — it is not a mitigation for state exposure. `prevent_destroy` (option D) protects resources from being destroyed, not state files. The correct mitigations are: using an **encrypted remote backend** (B) to protect data at rest, and **restricting access to the state file** and never committing it to version control (C).

---

### Question 12 — Comparing the Three Condition Mechanisms

**Difficulty**: Medium
**Answer Type**: many
**Topic**: Failure behaviour of `validation`, `precondition`/`postcondition`, and `check`

**Question**:
Which TWO of the following statements correctly describe how Terraform condition mechanisms handle failures? (Select two.)

- A) A failed `validation` block halts execution before `terraform plan` generates an execution plan
- B) A failed `check` block assertion causes `terraform apply` to roll back all changes made in the current run
- C) A failed `precondition` block halts `terraform apply` before the resource is modified
- D) A failed `postcondition` block converts the failing resource to a warning and allows subsequent resources to continue applying

**Answer**: A, C

**Explanation**:
`validation` failures (A) stop Terraform before planning — invalid variable values are caught immediately. `precondition` failures (C) abort the apply before the target resource is modified, protecting the resource from being created in an invalid state. By contrast, `check` block failures (B) never abort the apply — they are warnings only. `postcondition` failures (D) do fail the apply; they do not produce warnings and do not allow the rest of the run to continue unaffected.

---

---

## Questions

---

### Question 1 — Root Module Definition

**Difficulty**: Easy
**Answer Type**: one
**Topic**: What the root module is in a Terraform configuration

**Question**:
What is the Terraform **root module**?

- A) The first module listed in `modules.json` inside `.terraform/`
- B) The working directory from which you run `terraform apply`, containing the top-level configuration files
- C) A published module on the Terraform Registry that all other modules depend on
- D) The `main.tf` file specifically — variables.tf and outputs.tf belong to child modules

**Answer**: B

**Explanation**:
In Terraform, every directory containing `.tf` files is a module. The **root module** is the working directory from which you execute Terraform commands (`terraform init`, `terraform plan`, `terraform apply`). Modules called from the root are **child modules**. There is no special "root module" published separately — it is simply the local directory you are working in.

---

### Question 2 — Valid Module Source Types

**Difficulty**: Medium
**Answer Type**: many
**Topic**: Which source types are valid for the `source` argument in a module block

**Question**:
Which TWO of the following are valid values for the `source` argument in a `module` block? (Select two.)

- A) `"./modules/networking"` — a relative local path to a subdirectory
- B) `"hashicorp/consul/aws"` — a Terraform Registry module reference
- C) `"provider::aws::vpc"` — a provider-namespaced module reference
- D) `"module.networking"` — a reference to another module in the same configuration

**Answer**: A, B

**Explanation**:
Terraform supports multiple module source types including local paths (starting with `./` or `../`), Terraform Registry references in the format `<NAMESPACE>/<MODULE>/<PROVIDER>`, GitHub URLs, generic Git URLs, HTTP archives, S3 buckets, and GCS buckets. Option C uses a fictional `provider::` syntax that does not exist. Option D is the syntax for *referencing* a module's outputs, not for sourcing a module definition.

---

### Question 3 — Double-Slash `//` in Module Source

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Meaning of `//` in a Git-based module source URL

**Question**:
In the module source `"github.com/org/infra-modules//modules/vpc"`, what does the `//` (double slash) signify?

- A) It is a URL comment indicator and the text after it is ignored
- B) It separates the repository root from a subdirectory path within the repository
- C) It indicates that the module should be downloaded twice for redundancy
- D) It is a typo — only a single slash is valid in module source paths

**Answer**: B

**Explanation**:
In Terraform module sources that point to a Git repository or archive, the `//` (double slash) is a separator that marks the boundary between the **repository root URL** and a **subdirectory path** within that repository. Everything before `//` identifies the repository; everything after identifies the specific folder to use as the module root. This convention is intentional and documented — it is not a typo.

---

### Question 4 — `version` Argument Restriction

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Which module source types support the `version` argument

**Question**:
For which module source type is the `version` argument valid?

- A) Local paths only (`"./modules/vpc"`)
- B) Git URLs only (`"git::https://..."`)
- C) Terraform Registry and private registry sources only
- D) All source types support the `version` argument

**Answer**: C

**Explanation**:
The `version` argument in a `module` block is only supported for modules sourced from the **Terraform Registry** or a **private registry**. For Git-based sources, you pin a version using the `?ref=` query parameter (e.g., `git::https://github.com/org/repo.git?ref=v1.2.0`). For local paths there is no versioning mechanism. Specifying `version` with a local or Git source causes an error.

---

### Question 5 — Module Cache Location

**Difficulty**: Easy
**Answer Type**: one
**Topic**: Where `terraform init` caches downloaded module source code

**Question**:
Where does `terraform init` cache downloaded child module source code?

- A) `~/.terraform/modules/` in the user's home directory
- B) `terraform.tfstate` alongside the state data
- C) `.terraform/modules/` in the current working directory
- D) `/tmp/terraform-modules/` in a system temporary directory

**Answer**: C

**Explanation**:
`terraform init` downloads child module source code into the `.terraform/modules/` directory within the current working directory. This cache directory also contains a `modules.json` index file. You should re-run `terraform init` any time you add, remove, or change module sources in your configuration, so that the cache is updated.

---

### Question 6 — Variable Inheritance Between Modules

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Whether child modules inherit variables from the root module automatically

**Question**:
A root module declares `variable "region" { default = "us-east-1" }`. A child module also needs a `region` value. Which statement is correct?

- A) The child module automatically inherits `var.region` from the root module without any additional configuration
- B) The child module inherits the variable only if it is declared in both `variables.tf` files
- C) Variables are never automatically inherited — the root module must explicitly pass the value as an input argument in the `module` block
- D) Variables are inherited only for built-in types (string, number, bool); complex types must be passed explicitly

**Answer**: C

**Explanation**:
Terraform modules have **no implicit variable inheritance**. Even if the root module declares `variable "region"`, a child module cannot access `var.region` unless the root module explicitly passes it as an input argument in the `module` block (e.g., `region = var.region`). The child module must also have its own `variable "region"` block to declare the input. This explicit-passing requirement applies to all variable types.

---

### Question 7 — Standard Module File Structure

**Difficulty**: Medium
**Answer Type**: many
**Topic**: Files that belong in a standard Terraform module structure

**Question**:
Which TWO files are part of the standard, recommended Terraform module file structure? (Select two.)

- A) `versions.tf` — declares required Terraform and provider versions
- B) `state.tf` — declares the backend configuration for the module's state
- C) `providers.tf` — required to re-declare the provider in every child module
- D) `outputs.tf` — declares the output values exposed by the module

**Answer**: A, D

**Explanation**:
The standard module structure includes: `main.tf` (core resources), `variables.tf` (input variable declarations), `outputs.tf` (output value declarations), `versions.tf` (required providers and version constraints), and `README.md`. Option B is incorrect — child modules do not have their own backend configuration; only the root module configures the backend. Option C is incorrect — child modules do not need to redeclare providers; they inherit the provider configuration from the root module unless an alias or explicit `providers` argument is used.

---

### Question 8 — Backend Block Location in HCL

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Where the `backend` block is declared in Terraform configuration

**Question**:
Where must the `backend` block be declared in a Terraform configuration?

- A) In a dedicated `backend.tf` file at the root of the module
- B) Inside the `terraform {}` block, which is typically placed in `versions.tf` or `main.tf`
- C) Inside a `provider` block, alongside authentication credentials
- D) In `terraform.tfvars` as a backend-specific variable assignment

**Answer**: B

**Explanation**:
The `backend` block must be nested inside the `terraform {}` configuration block. While it can technically appear in any `.tf` file, it is conventionally placed in `versions.tf` or `main.tf`. The `backend` block cannot be placed inside a `provider` block or in `.tfvars` files — those files only accept variable value assignments.

---

### Question 9 — `terraform.tfstate.backup` Purpose

**Difficulty**: Medium
**Answer Type**: one
**Topic**: What `terraform.tfstate.backup` contains and its limitations

**Question**:
What does `terraform.tfstate.backup` contain when using the local backend?

- A) A complete versioned history of all previous state files since the project was created
- B) The state from the most recent apply — a single snapshot of the previous state, not a full history
- C) A backup of the state from 24 hours ago, automatically updated on a daily schedule
- D) An encrypted copy of the current state file for disaster recovery

**Answer**: B

**Explanation**:
`terraform.tfstate.backup` stores only the **single most recent previous state** — the state as it was just before the last apply. It is overwritten on each apply and does not provide versioned history. To maintain a full history of state changes, you need a remote backend with versioning enabled (such as S3 with object versioning, or HCP Terraform which provides state history natively).

---

### Question 10 — `terraform init -migrate-state` vs `-reconfigure`

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Difference between `terraform init -migrate-state` and `terraform init -reconfigure`

**Question**:
What is the difference between `terraform init -migrate-state` and `terraform init -reconfigure` when changing backends?

- A) `-migrate-state` only works with S3 backends; `-reconfigure` works with all backend types
- B) `-migrate-state` copies existing state to the new backend; `-reconfigure` reinitialises the backend without migrating existing state
- C) `-reconfigure` is for switching from local to remote backends; `-migrate-state` is for switching between two remote backends
- D) Both flags are identical — they are aliases for the same operation

**Answer**: B

**Explanation**:
When you change the `backend` block configuration and re-run `terraform init`, Terraform detects the change and requires you to choose a migration strategy. `terraform init -migrate-state` prompts Terraform to copy any existing state from the old backend into the new one. `terraform init -reconfigure` reinitialises the backend silently, discarding the migration prompt and leaving the old state in place — useful when the old state is no longer relevant or has already been handled manually.

---

### Question 11 — S3 Backend State Locking

**Difficulty**: Medium
**Answer Type**: one
**Topic**: How the S3 backend implements state locking

**Question**:
When using the S3 backend, which AWS service provides state locking, and what attribute name is required?

- A) S3 object tagging with a tag key of `TerraformLock`
- B) AWS Systems Manager Parameter Store with a parameter named `terraform-lock`
- C) DynamoDB with a table attribute named `LockID`
- D) CloudWatch Events with a rule named after the state file key

**Answer**: C

**Explanation**:
The S3 backend uses **DynamoDB** for state locking. You must create a DynamoDB table with a hash key (partition key) attribute named exactly `LockID` of type String. The table name is referenced in the backend block's `dynamodb_table` argument. When Terraform acquires a lock, it writes an item to this table; when the operation completes, the item is deleted. If the lock is not released (e.g., due to a crash), use `terraform force-unlock` with the lock ID.

---

### Question 12 — `terraform force-unlock` Usage

**Difficulty**: Hard
**Answer Type**: one
**Topic**: When and how to use `terraform force-unlock`

**Question**:
When should `terraform force-unlock <LOCK_ID>` be used, and what is the risk?

- A) It should be used routinely after every `terraform apply` to clean up lock artifacts; it carries no risk
- B) It should be used only when you are certain no other `terraform apply` or `plan` is actively running — using it while another operation holds the lock can corrupt state
- C) It should be used whenever `terraform plan` runs slowly, as it removes lock contention caused by stale read locks
- D) It can only be run by the user who created the lock; other users receive a permission error

**Answer**: B

**Explanation**:
`terraform force-unlock` manually releases a state lock that was not automatically released — typically because a process crashed or was interrupted while holding the lock. The lock ID to pass is shown in the error message Terraform displays when a lock is encountered. The **critical risk** is using it while another legitimate operation is actually running: if two applies run simultaneously against the same state, the state file can become corrupted. Only use `force-unlock` after confirming that no other operation is in progress.

---

### Question 13 — `plan -refresh-only` vs `apply -refresh-only`

**Difficulty**: Hard
**Answer Type**: many
**Topic**: Distinguishing `terraform plan -refresh-only` from `terraform apply -refresh-only`

**Question**:
Which TWO statements correctly describe the behaviour of the `-refresh-only` flag? (Select two.)

- A) `terraform plan -refresh-only` shows what has drifted in the cloud compared to state, but proposes no infrastructure changes
- B) `terraform apply -refresh-only` modifies cloud resources to match the Terraform configuration, resolving drift by re-applying desired state
- C) `terraform apply -refresh-only` updates the state file to reflect the current actual state of cloud resources, without creating, modifying, or destroying any infrastructure
- D) `terraform plan -refresh-only` is equivalent to `terraform refresh`, which is a deprecated command that both refreshes state and applies the plan in one step

**Answer**: A, C

**Explanation**:
`terraform plan -refresh-only` reads the current state of cloud resources and shows what differs from the recorded state, but does not propose any resource creates, updates, or deletes — it is a read-only drift report. `terraform apply -refresh-only` performs the same drift detection and then **updates only the state file** to match the actual cloud resources; it does not make any changes to the infrastructure itself. Option B is incorrect — `-refresh-only` never modifies cloud resources. Option D is incorrect — `terraform refresh` is the deprecated equivalent of `apply -refresh-only`, not `plan -refresh-only`.

---

---

## Questions

---

### Question 1 — `import` Block vs CLI Import

**Difficulty**: Easy
**Answer Type**: one
**Topic**: Which import method is preferred in Terraform 1.5+ and why

**Question**:
What is the primary advantage of using an `import` block (Terraform 1.5+) over the legacy `terraform import` CLI command?

- A) The `import` block is faster because it uses parallel imports; the CLI command is sequential
- B) The `import` block can be previewed with `terraform plan` before changes are applied, and can optionally generate HCL configuration automatically
- C) The `import` block supports all resource types; the CLI command only supports AWS resources
- D) The `import` block requires no existing resource block in configuration; the CLI command requires one

**Answer**: B

**Explanation**:
The `import` block (introduced in Terraform 1.5) is the preferred method because it is declarative and integrates into the standard plan/apply workflow — you can run `terraform plan` to preview what will be imported before committing. It also supports `terraform plan -generate-config-out=file.tf` to automatically generate the HCL resource configuration for the imported resource. The legacy `terraform import` CLI command imperatively modifies state immediately with no plan preview and does not generate configuration.

---

### Question 2 — `import` Block Syntax

**Difficulty**: Easy
**Answer Type**: one
**Topic**: Required arguments in an `import` block

**Question**:
Which two arguments are required in an `import` block?

- A) `source` and `destination`
- B) `resource` and `cloud_id`
- C) `to` and `id`
- D) `address` and `provider_id`

**Answer**: C

**Explanation**:
An `import` block requires exactly two arguments: `to` specifies the Terraform resource address that will manage the resource (e.g., `aws_instance.web`), and `id` specifies the cloud provider's identifier for the existing resource (e.g., `"i-0abcd1234ef567890"`). The syntax is: `import { to = resource_type.name  id = "provider-id" }`.

---

### Question 3 — CLI Import Pre-Requisite

**Difficulty**: Medium
**Answer Type**: one
**Topic**: What must exist in configuration before running `terraform import` CLI command

**Question**:
What must exist in the Terraform configuration before running `terraform import aws_s3_bucket.assets my-bucket-name`?

- A) Nothing — `terraform import` creates both the state entry and the HCL resource block automatically
- B) An `import` block referencing the same resource address
- C) A `resource "aws_s3_bucket" "assets" {}` block must already exist in the configuration files
- D) A `data "aws_s3_bucket" "assets" {}` block must exist to look up the bucket first

**Answer**: C

**Explanation**:
The legacy `terraform import` CLI command only writes the resource to state — it does not generate HCL. The corresponding resource block (e.g., `resource "aws_s3_bucket" "assets" {}`) must already exist in the configuration files before running the command. After importing, you use `terraform state show aws_s3_bucket.assets` to view all attributes and then manually update the resource block to match the actual resource configuration.

---

### Question 4 — `terraform plan -generate-config-out`

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Purpose of the `-generate-config-out` flag

**Question**:
What does `terraform plan -generate-config-out=generated.tf` do?

- A) Saves the execution plan to a file named `generated.tf` that can be passed to `terraform apply`
- B) Generates HCL resource configuration for resources referenced in `import` blocks and writes it to `generated.tf`
- C) Exports all existing resources in state as HCL configuration into `generated.tf`
- D) Generates a Terraform provider configuration block and appends it to `generated.tf`

**Answer**: B

**Explanation**:
`terraform plan -generate-config-out=generated.tf` is used in conjunction with `import` blocks. When Terraform encounters an `import` block for a resource that has no existing HCL configuration, it generates the resource block based on the live cloud resource's attributes and writes it to the specified output file. You then review, adjust, and commit the generated file before running `terraform apply` to complete the import.

---

### Question 5 — `TF_LOG` Verbosity Order

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Order of `TF_LOG` levels from most to least verbose

**Question**:
Which ordering correctly lists Terraform's `TF_LOG` levels from **most verbose** to **least verbose**?

- A) `ERROR > WARN > INFO > DEBUG > TRACE > OFF`
- B) `TRACE > DEBUG > INFO > WARN > ERROR > OFF`
- C) `DEBUG > TRACE > INFO > WARN > ERROR > OFF`
- D) `INFO > DEBUG > TRACE > WARN > ERROR > OFF`

**Answer**: B

**Explanation**:
Terraform's logging levels in order from most to least verbose are: `TRACE` (all API calls and responses), `DEBUG` (detailed debugging), `INFO` (general operational messages), `WARN` (warning conditions), `ERROR` (error conditions only), and `OFF` (logging disabled). Setting `TF_LOG=TRACE` produces the maximum amount of output and is used for deep debugging of provider and core behaviour.

---

### Question 6 — `TF_LOG_PATH` and Separate Core/Provider Logging

**Difficulty**: Medium
**Answer Type**: many
**Topic**: `TF_LOG_PATH`, `TF_LOG_CORE`, and `TF_LOG_PROVIDER` environment variables

**Question**:
Which TWO statements correctly describe Terraform's logging environment variables? (Select two.)

- A) `TF_LOG_PATH=/tmp/tf.log` causes Terraform to write log output to that file instead of stderr
- B) `TF_LOG_CORE=DEBUG` and `TF_LOG_PROVIDER=TRACE` allow setting different log levels for Terraform core and provider plugins independently
- C) `TF_LOG_PATH` must be set to an absolute path; relative paths are not supported
- D) Setting `TF_LOG_PROVIDER=TRACE` also automatically sets `TF_LOG_CORE=TRACE`

**Answer**: A, B

**Explanation**:
`TF_LOG_PATH` redirects log output from stderr to a specified file path, making it easy to capture logs for review. `TF_LOG_CORE` and `TF_LOG_PROVIDER` allow independent log level control for Terraform's core engine and provider plugins respectively — useful when you need detailed provider API traces without the noise of core debug messages. Options C and D describe nonexistent restrictions; the variables are independent of each other.

---

### Question 7 — HCP Terraform `cloud` Block

**Difficulty**: Medium
**Answer Type**: one
**Topic**: The `cloud` block and when it was introduced

**Question**:
What is the preferred way to connect a Terraform configuration to HCP Terraform (Terraform 1.1+), and which two arguments does it require?

- A) `backend "remote"` block with `hostname` and `token` arguments
- B) `cloud` block with `organization` and `workspaces` arguments
- C) `cloud` block with `hostname` and `workspace_id` arguments
- D) `provider "tfe"` block with `organization` and `token` arguments

**Answer**: B

**Explanation**:
Starting with Terraform 1.1, the `cloud` block inside the `terraform {}` block is the preferred way to connect to HCP Terraform. It requires `organization` (the HCP Terraform organisation name) and `workspaces` (specifying either a workspace `name` or `tags` to select workspaces dynamically). The legacy `backend "remote"` block remains valid but is no longer the recommended approach.

---

### Question 8 — `terraform login` Token Storage

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Where `terraform login` stores the API token

**Question**:
Where does `terraform login` store the HCP Terraform API token after a successful browser-based authentication?

- A) `terraform.tfvars` in the current working directory
- B) `.terraform/credentials.json` in the current working directory
- C) `~/.terraform.d/credentials.tfrc.json` in the user's home directory
- D) The token is never stored on disk — it is only held in memory for the current session

**Answer**: C

**Explanation**:
`terraform login` opens a browser to authenticate with HCP Terraform and stores the resulting API token in `~/.terraform.d/credentials.tfrc.json` in the user's home directory. This file persists across sessions and is used automatically by subsequent Terraform commands. The token can alternatively be provided via the `TF_TOKEN_app_terraform_io` environment variable, which is preferred for CI/CD pipelines to avoid storing credentials on disk.

---

### Question 9 — HCP Terraform Run Types

**Difficulty**: Medium
**Answer Type**: one
**Topic**: The three HCP Terraform run types

**Question**:
Which HCP Terraform run type runs a plan but **never applies** — typically triggered by a pull request to show what would change?

- A) Plan-only run
- B) Speculative plan
- C) Plan-and-apply run
- D) Dry-run

**Answer**: B

**Explanation**:
A **speculative plan** is a read-only plan that never progresses to apply. It is typically triggered automatically when a pull request is opened against a VCS-connected workspace, giving reviewers visibility into what infrastructure changes the PR would cause. It cannot be approved for apply — it is informational only. A **plan-only** run performs a full plan that can later be approved for apply. A **plan-and-apply** run combines both steps.

---

### Question 10 — HCP Terraform Policy Enforcement Levels

**Difficulty**: Medium
**Answer Type**: one
**Topic**: The three Sentinel/OPA policy enforcement levels

**Question**:
Which HCP Terraform policy enforcement level **blocks a run** when a policy fails but **allows an authorised user to override** the failure and proceed?

- A) `advisory`
- B) `soft-mandatory`
- C) `hard-mandatory`
- D) `blocking`

**Answer**: B

**Explanation**:
HCP Terraform supports three policy enforcement levels: `advisory` (failure shows a warning but the run continues), `soft-mandatory` (failure blocks the run, but a user with sufficient permissions can override and allow it to proceed), and `hard-mandatory` (failure blocks the run with no override possible — the policy must pass for the run to continue). `blocking` is not a valid enforcement level.

---

### Question 11 — Variable Sets in HCP Terraform

**Difficulty**: Medium
**Answer Type**: one
**Topic**: What variable sets are and how they are used

**Question**:
What is the purpose of a **variable set** in HCP Terraform?

- A) A set of required variables that must be declared in every workspace's `variables.tf`
- B) A reusable collection of Terraform or environment variables that can be assigned to multiple workspaces or an entire organisation
- C) A list of sensitive variable names whose values are automatically redacted from run logs
- D) A JSON file that defines default variable values, similar to `terraform.tfvars`

**Answer**: B

**Explanation**:
Variable sets allow teams to define a collection of variables (such as cloud provider credentials) once and assign them to multiple workspaces or an entire organisation, avoiding duplication. For example, a "AWS Credentials" variable set containing `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY` environment variables can be applied to all workspaces that deploy to AWS. Variables in a set can be marked sensitive to hide their values in the UI.

---

### Question 12 — HCP Terraform Workspace Permissions

**Difficulty**: Hard
**Answer Type**: many
**Topic**: The four workspace-level permission tiers in HCP Terraform

**Question**:
Which TWO statements correctly describe HCP Terraform workspace-level permissions? (Select two.)

- A) The **Write** permission allows a user to trigger runs and approve applies, but not to manage workspace settings or team access
- B) The **Plan** permission allows a user to trigger full plan-and-apply runs without any additional approval
- C) The **Read** permission allows a user to view run history, state, and variables but not trigger any runs
- D) The **Admin** permission is required to change workspace variables — the Write permission does not allow variable changes

**Answer**: A, C

**Explanation**:
HCP Terraform's four workspace permission levels are: **Read** (view runs, state, variables — no triggering), **Plan** (trigger speculative plans only), **Write** (trigger and approve runs — the standard developer permission), and **Admin** (manage all workspace settings including team access and variables). Option B is incorrect — **Plan** only allows speculative plans, not full applies. Option D is incorrect — Write permission does allow variable management; Admin is required for workspace settings and team access control.

---

### Question 13 — Dynamic Provider Credentials (OIDC)

**Difficulty**: Hard
**Answer Type**: one
**Topic**: Purpose and benefit of dynamic provider credentials using OIDC in HCP Terraform

**Question**:
What is the primary security benefit of using **dynamic provider credentials** (OIDC) in HCP Terraform workspaces?

- A) OIDC credentials are stored in HCP Terraform's vault and rotated every 24 hours automatically
- B) OIDC eliminates the need to store long-lived static cloud credentials in HCP Terraform — each run receives a short-lived token that expires after the run completes
- C) OIDC allows multiple cloud providers to share a single set of credentials, reducing the number of secrets to manage
- D) OIDC enables HCP Terraform to bypass multi-factor authentication requirements for cloud providers

**Answer**: B

**Explanation**:
Dynamic provider credentials use OpenID Connect (OIDC) to allow HCP Terraform workspaces to authenticate to cloud providers (AWS, Azure, GCP) without storing long-lived static access keys. Instead, each run requests a short-lived identity token from HCP Terraform, which the cloud provider validates against its configured trust relationship with HCP Terraform as the OIDC issuer. The credentials are scoped to a single run and expire automatically, significantly reducing the risk of credential leakage compared to storing static keys.

---