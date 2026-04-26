# Terraform Associate Exam Questions

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
### Question 13 — Provider Definition

**Difficulty**: Easy
**Answer Type**: one
**Topic**: What a Terraform provider is

**Question**:
Which of the following best describes a Terraform provider?

- A) A HashiCorp-managed cloud platform that stores Terraform state remotely
- B) A plugin that bridges Terraform's HCL configuration to a target cloud or service API
- C) A built-in Terraform block that defines authentication credentials in a `.tf` file
- D) A version of the Terraform CLI binary compiled for a specific operating system
### Question 14 — Provider Tiers

**Difficulty**: Easy
**Answer Type**: one
**Topic**: Provider tier classification

**Question**:
Terraform providers are classified into three tiers. Which tier is maintained directly by HashiCorp and carries the highest level of trust?

- A) Community
- B) Partner
- C) Official
- D) Verified
### Question 15 — Plugin Architecture Communication

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Terraform Core and provider communication protocol

**Question**:
How does Terraform Core communicate with a provider plugin during execution?

- A) Through direct function calls within the same process binary
- B) Via HTTP REST API calls to a locally running provider web server
- C) Via gRPC, with the provider running as a separate process from Terraform Core
- D) Through shared memory mapped files in the `.terraform/` directory
### Question 16 — Provider Source Address Format

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Provider source address and default registry hostname

**Question**:
A `required_providers` block declares `source = "hashicorp/aws"`. What is the fully qualified source address that Terraform resolves this to?

- A) `github.com/hashicorp/aws`
- B) `registry.terraform.io/hashicorp/aws`
- C) `releases.hashicorp.com/hashicorp/aws`
- D) `hashicorp.com/terraform/providers/aws`
### Question 17 — `terraform init` Provider Download

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Where terraform init installs providers

**Question**:
When `terraform init` is run, where are provider plugins downloaded to?

- A) `~/.terraform.d/plugins/`
- B) `terraform.tfstate`
- C) `.terraform/providers/`
- D) `providers.lock/`
### Question 18 — Dependency Lock File

**Difficulty**: Medium
**Answer Type**: one
**Topic**: `.terraform.lock.hcl` purpose and version control

**Question**:
What is the purpose of the `.terraform.lock.hcl` file, and how should it be treated with respect to version control?

- A) It records the current Terraform state and must never be committed to version control
- B) It records exact provider versions and checksums installed; it must be committed to version control
- C) It is a temporary cache file generated on each `terraform init` run and should be added to `.gitignore`
- D) It stores encrypted provider credentials and must be committed but kept private
### Question 19 — Pessimistic Constraint Operator

**Difficulty**: Medium
**Answer Type**: one
**Topic**: `~>` version constraint operator behaviour

**Question**:
A `required_providers` block specifies `version = "~> 5.0"` for the AWS provider. Which versions are permitted by this constraint?

- A) Exactly version 5.0.0 only
- B) Any version >= 5.0.0 with no upper limit
- C) Any version >= 5.0 and < 6.0 (minor and patch updates within major version 5)
- D) Any version >= 5.0.0 and < 5.1.0 (patch updates only within minor version 5.0)
### Question 20 — Provider Alias

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Provider alias for multiple configurations

**Question**:
When is a provider `alias` required in a Terraform configuration?

- A) Whenever a provider block is declared inside a module rather than the root module
- B) When more than one configuration of the same provider is needed, such as managing resources in multiple regions
- C) Whenever a provider version constraint is specified in the `required_providers` block
- D) When Terraform is run with a non-default workspace
### Question 21 — What `terraform.tfstate` Stores

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Content and purpose of the Terraform state file

**Question**:
What does the `terraform.tfstate` file contain?

- A) The raw HCL configuration for all resources managed by Terraform
- B) A log of every `terraform apply` command that has been executed
- C) A JSON mapping of Terraform resource addresses to their real-world resource IDs and attributes
- D) The compiled binary representation of a Terraform execution plan
### Question 22 — Three Sources During Plan

**Difficulty**: Medium
**Answer Type**: many
**Topic**: Sources Terraform compares during `terraform plan`

**Question**:
When `terraform plan` runs, Terraform compares information from multiple sources to determine what changes are needed. Which TWO of the following are sources that Terraform uses during planning? (Select two.)

- A) The Terraform Registry API to check for provider updates
- B) The `.tf` configuration files representing the desired state
- C) The `terraform.tfstate` file representing the last-known resource state
- D) The `.terraform.lock.hcl` file representing installed provider versions
### Question 23 — Local vs Remote State

**Difficulty**: Hard
**Answer Type**: one
**Topic**: Differences between local and remote Terraform state

**Question**:
Which of the following is a characteristic of local Terraform state that makes it unsuitable for team environments?

- A) Local state files use a binary format that cannot be read or backed up
- B) Local state provides no locking mechanism, meaning concurrent `terraform apply` runs by different team members can corrupt state
- C) Local state is automatically deleted after each `terraform apply` completes
- D) Local state cannot store resource attribute values, only resource addresses
### Question 24 — `sensitive = true` and State

**Difficulty**: Hard
**Answer Type**: one
**Topic**: Behaviour of `sensitive = true` in outputs vs state storage

**Question**:
A Terraform output is declared with `sensitive = true`. What is the effect of this setting on how the value is handled?

- A) The value is encrypted with AES-256 before being written to `terraform.tfstate`
- B) The value is redacted from `terraform.tfstate` entirely and stored in a separate secrets file
- C) The value is masked in terminal output but is still stored in plaintext in `terraform.tfstate`
- D) The value is masked in terminal output and also removed from any remote backend storage
### Question 25 — `terraform state` Commands

**Difficulty**: Medium
**Answer Type**: many
**Topic**: Terraform state CLI subcommands

**Question**:
Which TWO `terraform state` subcommands would be appropriate for inspecting state without modifying it? (Select two.)

- A) `terraform state rm`
- B) `terraform state list`
- C) `terraform state push`
- D) `terraform state show`
### Question 26 — Core Workflow Sequence

**Difficulty**: Easy
**Answer Type**: one
**Topic**: Correct order of the core Terraform CLI workflow

**Question**:
Which of the following represents the correct core Terraform workflow sequence?

- A) `validate → init → fmt → plan → apply → destroy`
- B) `init → fmt → validate → plan → apply → destroy`
- C) `fmt → init → plan → validate → apply → destroy`
- D) `init → plan → validate → fmt → apply → destroy`
### Question 27 — `terraform init` Purpose

**Difficulty**: Easy
**Answer Type**: one
**Topic**: What `terraform init` does

**Question**:
Which of the following is a primary action performed by `terraform init`?

- A) It applies all pending changes from the most recent execution plan
- B) It downloads required provider plugins into the `.terraform/` directory
- C) It validates that all resource configurations are syntactically correct
- D) It formats all `.tf` files in the working directory to canonical style
### Question 28 — When to Re-run `terraform init`

**Difficulty**: Medium
**Answer Type**: many
**Topic**: Conditions requiring `terraform init` to be re-run

**Question**:
In which TWO situations must `terraform init` be re-run? (Select two.)

- A) When a new provider is added to `required_providers`
- B) When an output value is added to an existing module
- C) When the backend configuration is changed to a different provider
- D) When a variable default value is updated in `variables.tf`
### Question 29 — `terraform validate` Network Requirement

**Difficulty**: Medium
**Answer Type**: one
**Topic**: `terraform validate` network access and what it checks

**Question**:
Which statement correctly describes `terraform validate`?

- A) It requires active cloud provider credentials to verify that referenced resources exist in the target environment
- B) It performs a live API call to confirm that the AMI ID or other resource identifiers in the config are valid
- C) It checks configuration syntax and internal references without requiring network access or provider credentials
- D) It generates a full execution plan and outputs the number of resources that will be created, updated, or destroyed
### Question 30 — `terraform fmt` Flags

**Difficulty**: Medium
**Answer Type**: one
**Topic**: `terraform fmt -check` flag behaviour

**Question**:
What is the purpose of the `-check` flag on `terraform fmt`?

- A) It checks that all variable names follow HashiCorp's naming conventions
- B) It validates the syntax of all HCL files but does not reformat them
- C) It exits with a non-zero exit code if any files need reformatting, without modifying them — useful for CI pipelines
- D) It checks whether provider versions are compatible with the current Terraform version
### Question 31 — `terraform plan -out` Flag

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Saving and applying a plan file

**Question**:
What is the benefit of running `terraform plan -out=plan.tfplan` followed by `terraform apply plan.tfplan`?

- A) It allows Terraform to skip provider validation when applying the plan
- B) It guarantees that the exact set of changes reviewed in `plan` is applied, with no drift between the two steps
- C) It compresses the plan file so that it can be stored in version control alongside `.tf` files
- D) It allows `terraform apply` to run without any state file present
### Question 32 — Plan Output Symbols

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Meaning of `terraform plan` output symbols

**Question**:
In `terraform plan` output, what does the symbol `-/+` indicate will happen to a resource?

- A) The resource will be updated in-place with no interruption
- B) The resource will be imported into state from an existing infrastructure object
- C) The resource will be destroyed and then recreated (replacement)
- D) The resource will be moved to a different Terraform workspace
### Question 33 — `terraform apply -auto-approve`

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Purpose and use case of `-auto-approve`

**Question**:
What does the `-auto-approve` flag do when passed to `terraform apply`?

- A) It automatically selects the most recent saved plan file in the working directory
- B) It skips the interactive confirmation prompt before applying changes — commonly used in CI/CD pipelines
- C) It approves all individual resource creation steps sequentially without pausing
- D) It causes Terraform to apply changes to approved resources only and skip unapproved ones
### Question 34 — `terraform apply -replace`

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Forcing resource replacement with `-replace`

**Question**:
Which command is the current (Terraform 1.5+) recommended way to force a specific resource to be destroyed and recreated on the next apply?

- A) `terraform taint aws_instance.web`
- B) `terraform apply -replace="aws_instance.web"`
- C) `terraform destroy -target=aws_instance.web` followed by `terraform apply`
- D) `terraform state rm aws_instance.web` followed by `terraform apply`
### Question 35 — `terraform output -raw`

**Difficulty**: Medium
**Answer Type**: one
**Topic**: `terraform output -raw` use case

**Question**:
What does `terraform output -raw db_password` return, and when is this flag useful?

- A) The output value formatted as a JSON object with metadata fields
- B) The raw string value with no surrounding quotes — useful when piping the value into scripts or other commands
- C) The encrypted form of the output value for use with external secrets managers
- D) A diff showing the current output value versus the previous apply's value
### Question 36 — `terraform console` Purpose

**Difficulty**: Medium
**Answer Type**: one
**Topic**: What `terraform console` is used for

**Question**:
What is the primary purpose of `terraform console`?

- A) To display the current Terraform state in an interactive paginated viewer
- B) To provide an interactive REPL where Terraform expressions and built-in functions can be tested
- C) To monitor the progress of a running `terraform apply` operation in real time
- D) To inspect and modify resource attributes in the state file interactively
### Question 37 — `terraform destroy` Equivalence

**Difficulty**: Hard
**Answer Type**: one
**Topic**: Relationship between `terraform destroy` and `terraform apply -destroy`

**Question**:
Which statement about `terraform destroy` is correct?

- A) `terraform destroy` permanently deletes the state file after all resources are removed
- B) `terraform destroy` is equivalent to `terraform apply -destroy` and both prompt for confirmation by default
- C) `terraform destroy` only removes resources created in the current workspace, while `terraform apply -destroy` removes all workspaces
- D) `terraform destroy` is deprecated and has been replaced by `terraform apply -destroy` in Terraform 1.5+
### Question 38 — `terraform fmt` and `terraform validate` Scope

**Difficulty**: Hard
**Answer Type**: many
**Topic**: Distinguishing what `fmt` and `validate` check

**Question**:
Which TWO of the following issues would `terraform validate` detect but `terraform fmt` would NOT? (Select two.)

- A) Inconsistent indentation in a `resource` block
- B) A variable referenced in a resource block that is not declared anywhere in the configuration
- C) Misaligned `=` signs in argument assignments
- D) An unsupported argument name passed to a resource type
### Question 39 — Resource Block Syntax

**Difficulty**: Easy
**Answer Type**: one
**Topic**: Resource block syntax and components

**Question**:
Which of the following correctly shows the required structure of a Terraform resource block?

- A) `resource { type = "aws_instance" name = "web" }`
- B) `resource "aws_instance" "web" { ... }`
- C) `resource aws_instance web { ... }`
- D) `provider "aws_instance" "web" { ... }`
### Question 40 — Data Source Purpose

**Difficulty**: Easy
**Answer Type**: one
**Topic**: What a data source does

**Question**:
What is the purpose of a `data` block in a Terraform configuration?

- A) To define a new cloud resource that Terraform will create and manage
- B) To query an existing infrastructure object in read-only mode without creating or managing it
- C) To store sensitive values such as passwords and API keys securely
- D) To declare default values for input variables used across modules
### Question 41 — Data Source Reference Format

**Difficulty**: Medium
**Answer Type**: one
**Topic**: How to reference a data source attribute

**Question**:
A data source is declared as `data "aws_ami" "ubuntu" { ... }`. What is the correct syntax to reference its `id` attribute in a resource block?

- A) `aws_ami.ubuntu.id`
- B) `data.ubuntu.aws_ami.id`
- C) `data.aws_ami.ubuntu.id`
- D) `source.aws_ami.ubuntu.id`
### Question 42 — Meta-Arguments Available to All Resources

**Difficulty**: Medium
**Answer Type**: many
**Topic**: Resource meta-arguments

**Question**:
Which TWO of the following are valid meta-arguments that can be added to any Terraform resource block? (Select two.)

- A) `source`
- B) `depends_on`
- C) `backend`
- D) `lifecycle`
### Question 43 — Implicit vs Explicit Dependencies

**Difficulty**: Medium
**Answer Type**: one
**Topic**: How implicit dependencies are created

**Question**:
What causes Terraform to automatically create an implicit dependency between two resources?

- A) Both resources sharing the same provider configuration
- B) One resource's argument referencing an attribute of another resource (e.g., `aws_vpc.main.id`)
- C) Both resources being declared in the same `.tf` file
- D) A `var.*` or `local.*` value being used in both resource blocks
### Question 44 — `depends_on` Use Case

**Difficulty**: Medium
**Answer Type**: one
**Topic**: When to use `depends_on`

**Question**:
In which situation should `depends_on` be used in a Terraform resource block?

- A) To define the order in which output values are displayed after `terraform apply`
- B) To force a resource to be replaced instead of updated in-place
- C) To express a dependency that Terraform cannot detect through attribute references, such as an IAM policy attachment
- D) To ensure a resource is created before any data sources in the configuration are read
### Question 45 — `lifecycle` `create_before_destroy`

**Difficulty**: Medium
**Answer Type**: one
**Topic**: `create_before_destroy` lifecycle argument

**Question**:
What is the effect of setting `create_before_destroy = true` in a resource's `lifecycle` block?

- A) Terraform creates a backup of the resource's state before applying any destroy operation
- B) Terraform provisions the replacement resource first and only destroys the old resource after the new one is ready, minimising downtime
- C) Terraform creates the resource before any `terraform plan` is executed
- D) Terraform ensures the resource is created before all other resources in the configuration, regardless of dependencies
### Question 46 — `lifecycle` `prevent_destroy`

**Difficulty**: Medium
**Answer Type**: one
**Topic**: `prevent_destroy` lifecycle argument

**Question**:
What happens when `prevent_destroy = true` is set in a resource's `lifecycle` block and a plan includes destroying that resource?

- A) Terraform skips the destroy step and leaves the resource unchanged without any error
- B) Terraform prompts the user for a special override passphrase before allowing the destroy
- C) Terraform returns an error and refuses to create a plan that includes destroying the resource
- D) Terraform creates a backup of the resource in a separate workspace before destroying it
### Question 47 — `lifecycle` `ignore_changes`

**Difficulty**: Medium
**Answer Type**: one
**Topic**: `ignore_changes` lifecycle argument

**Question**:
What is the purpose of the `ignore_changes` argument in a resource's `lifecycle` block?

- A) It prevents Terraform from reading the resource's current state during `terraform plan`
- B) It tells Terraform to ignore drift on specified attributes, so changes to those attributes outside Terraform do not trigger an update
- C) It suppresses `terraform plan` output for the listed attributes to keep logs concise
- D) It forces Terraform to skip validation of the listed arguments during `terraform validate`
### Question 48 — `replace_triggered_by` Lifecycle Argument

**Difficulty**: Medium
**Answer Type**: one
**Topic**: `replace_triggered_by` lifecycle argument

**Question**:
What does the `replace_triggered_by` argument in a `lifecycle` block do?

- A) It replaces the resource's provider with the one specified in the argument list
- B) It causes the resource to be destroyed and recreated whenever any resource or attribute listed in the argument changes
- C) It triggers a `terraform plan` automatically when a listed resource is modified outside Terraform
- D) It forces the resource to be replaced on every `terraform apply` regardless of any changes
### Question 49 — `moved` Block Purpose

**Difficulty**: Hard
**Answer Type**: one
**Topic**: What the `moved` block does in Terraform state

**Question**:
What is the purpose of the `moved` block in Terraform?

- A) It migrates a resource to a different cloud provider without destroying and recreating it
- B) It renames or relocates a resource address in the state file without destroying and recreating the real infrastructure
- C) It moves a resource's configuration from one `.tf` file to another and updates imports automatically
- D) It transfers a resource's state to a different Terraform workspace while keeping the resource in the current cloud account
### Question 50 — Default Parallelism

**Difficulty**: Hard
**Answer Type**: one
**Topic**: Terraform default parallelism and the `-parallelism` flag

**Question**:
What is the default number of concurrent operations Terraform uses during `terraform apply`, and how can it be changed?

- A) Default is 5; change with `terraform apply -concurrent=10`
- B) Default is 10; change with `terraform apply -parallelism=<n>`
- C) Default is unlimited; Terraform always maximises concurrency up to available CPU cores
- D) Default is 1 (sequential); change with `terraform apply -parallel=true`
### Question 51 — When Data Sources Are Read

**Difficulty**: Medium
**Answer Type**: many
**Topic**: Timing of data source reads during plan and apply

**Question**:
During which TWO phases can a Terraform data source be read? (Select two.)

- A) During `terraform init`, when providers are downloaded
- B) During the `plan` phase, when the data source's query arguments are fully known
- C) During the `apply` phase, when the data source's query arguments depend on a value not known until apply
- D) During `terraform validate`, when syntax is checked
### Question 52 — Variable Input Precedence

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Order of variable value precedence (highest wins)

**Question**:
A Terraform variable named `region` has a `default` of `"us-east-1"` in its declaration, a value of `"eu-west-1"` in `terraform.tfvars`, and is also set via `TF_VAR_region=ap-southeast-1` in the shell environment. Which value does Terraform use?

- A) `"us-east-1"` — the `default` in the variable block always wins
- B) `"eu-west-1"` — `terraform.tfvars` overrides environment variables
- C) `"ap-southeast-1"` — `TF_VAR_*` environment variables have higher precedence than `.tfvars` files
- D) Terraform raises an error because the variable is set in multiple places
### Question 53 — Variable Block Argument: `sensitive`

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Effect of `sensitive = true` on variables vs state

**Question**:
What is the effect of declaring `sensitive = true` on an input variable?

- A) The variable's value is encrypted before being stored in `terraform.tfstate`
- B) The variable's value is hidden in terminal output during `plan` and `apply` but is still stored in plaintext in the state file
- C) The variable's value is excluded from the state file entirely
- D) The variable cannot be passed via environment variables — only via `-var` flag
### Question 54 — Validation Block Scope

**Difficulty**: Medium
**Answer Type**: one
**Topic**: What a variable `validation` block can reference

**Question**:
Which of the following expressions is valid inside a variable's `validation` block `condition` argument?

- A) `length(aws_instance.web.id) > 0`
- B) `local.environment != ""`
- C) `contains(["dev", "staging", "prod"], var.environment)`
- D) `data.aws_ami.ubuntu.id != ""`
### Question 55 — Locals vs Input Variables

**Difficulty**: Easy
**Answer Type**: one
**Topic**: Difference between `locals` and `variable` blocks

**Question**:
What is the key difference between a `locals` block and a `variable` block in Terraform?

- A) Locals can only hold string values; variables can hold any type
- B) Variables are external inputs that can be set by the caller; locals are internal computed values that cannot be set from outside the module
- C) Locals are shared across all modules in a configuration; variables are scoped to a single module
- D) Variables must always have a `default` value; locals do not require a value expression
### Question 56 — Module Output Reference Syntax

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Referencing a child module's output value

**Question**:
A root configuration uses a child module declared as `module "network" { ... }`. The child module has an output named `vpc_id`. What is the correct way to reference this output in the root module?

- A) `network.vpc_id`
- B) `output.network.vpc_id`
- C) `module.network.vpc_id`
- D) `var.network.vpc_id`
### Question 57 — `count` vs `for_each` — Preferred Usage

**Difficulty**: Easy
**Answer Type**: one
**Topic**: When to prefer `for_each` over `count`

**Question**:
Why is `for_each` generally preferred over `count` when creating multiple resource instances in Terraform?

- A) `for_each` supports more resource types than `count`
- B) `for_each` uses named keys to identify instances, so removing one item does not force recreation of all subsequent instances
- C) `for_each` is faster to apply because it uses parallel execution; `count` is sequential
- D) `for_each` allows resources to span multiple providers; `count` is limited to a single provider
### Question 58 — `count.index` and Splat Expressions

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Accessing `count`-based resource instances

**Question**:
A resource is declared with `count = 3`. What does the splat expression `aws_instance.web[*].id` return?

- A) The ID of the first instance only (`aws_instance.web[0].id`)
- B) A map of index-to-ID pairs: `{ 0 = "i-aaa", 1 = "i-bbb", 2 = "i-ccc" }`
- C) A list containing the `id` attribute of all three instances
- D) An error — splat expressions only work with `for_each`, not `count`
### Question 59 — `for_each` with a Set — `each.key` vs `each.value`

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Behaviour of `each.key` and `each.value` when `for_each` uses a set

**Question**:
When `for_each` is assigned a **set** of strings (e.g., `toset(["alice", "bob"])`), what is the relationship between `each.key` and `each.value` inside the resource block?

- A) `each.key` is the zero-based index; `each.value` is the string element
- B) `each.key` and `each.value` are both equal to the set element string
- C) `each.key` is the set element string; `each.value` is always `null` for sets
- D) Sets do not support `each.key` — only `each.value` is available
### Question 60 — `for` Expression with Filter

**Difficulty**: Medium
**Answer Type**: one
**Topic**: `for` expression syntax with an `if` filter clause

**Question**:
Which `for` expression correctly produces a list of names from `var.names` that are longer than 4 characters?

- A) `[for name in var.names : name where length(name) > 4]`
- B) `[for name in var.names : name if length(name) > 4]`
- C) `[for name in var.names | length(name) > 4 : name]`
- D) `filter(var.names, n => length(n) > 4)`
### Question 61 — `lookup` Function

**Difficulty**: Medium
**Answer Type**: one
**Topic**: `lookup()` function signature and default value

**Question**:
What does `lookup({a = 1, b = 2}, "c", 99)` return?

- A) `null` — the key `"c"` does not exist in the map
- B) An error — `lookup` raises an exception when the key is not found
- C) `99` — the third argument is returned as the default when the key is not found
- D) `0` — `lookup` always returns 0 for missing numeric map entries
### Question 62 — `cidrsubnet` Function

**Difficulty**: Hard
**Answer Type**: one
**Topic**: `cidrsubnet()` function parameters and result

**Question**:
What does `cidrsubnet("10.0.0.0/16", 8, 2)` return?

- A) `"10.0.0.0/24"`
- B) `"10.0.1.0/24"`
- C) `"10.0.2.0/24"`
- D) `"10.2.0.0/24"`
### Question 63 — `flatten` vs `compact` Functions

**Difficulty**: Hard
**Answer Type**: many
**Topic**: Distinguishing `flatten()` and `compact()` use cases

**Question**:
Which TWO statements correctly describe the difference between `flatten()` and `compact()`? (Select two.)

- A) `flatten(["a", ["b", "c"]])` returns `["a", "b", "c"]` by removing nested list structure
- B) `compact(["a", "", null, "b"])` returns `["a", "b"]` by removing empty strings and null values
- C) `flatten()` removes duplicate values from a flat list
- D) `compact()` recursively unwraps nested lists into a single flat list
### Question 64 — `templatefile` vs `file` Functions

**Difficulty**: Medium
**Answer Type**: many
**Topic**: When to use `templatefile()` instead of `file()`

**Question**:
Which TWO statements correctly describe the difference between `file()` and `templatefile()`? (Select two.)

- A) `file(path)` reads the file content as a raw string with no variable substitution
- B) `templatefile(path, vars)` renders the file as a template, substituting `${var_name}` placeholders with values from the `vars` map
- C) `file()` supports `.tpl` template files; `templatefile()` only supports `.txt` files
- D) `templatefile()` can only reference Terraform input variables; it cannot reference locals or computed values
### Question 65 — Three Condition Mechanisms Overview

**Difficulty**: Easy
**Answer Type**: one
**Topic**: The three Terraform condition mechanisms and where each is declared

**Question**:
Which of the following correctly lists all three Terraform mechanisms for asserting conditions on infrastructure?

- A) `assert` block, `check` block, `guard` block
- B) `validation` block, `precondition`/`postcondition` in `lifecycle`, `check` block
- C) `validation` block, `check` block, `enforce` block
- D) `precondition` block, `postcondition` block, `verify` block
### Question 66 — `validation` Block — When It Runs

**Difficulty**: Easy
**Answer Type**: one
**Topic**: When variable `validation` blocks are evaluated

**Question**:
When does a `validation` block inside a `variable` declaration run?

- A) After `terraform apply` completes, to verify the applied configuration
- B) During `terraform init`, when providers are downloaded
- C) Before `terraform plan`, as part of input variable evaluation
- D) Only when explicitly triggered by `terraform validate`
### Question 67 — `validation` Block Condition Constraints

**Difficulty**: Medium
**Answer Type**: one
**Topic**: What a `validation` condition can reference

**Question**:
Which restriction applies to the `condition` expression inside a variable `validation` block?

- A) It must return a number, which is compared to zero to determine pass/fail
- B) It can only reference `var.<variable_name>` — not resources, data sources, or locals
- C) It must use only built-in string functions; numeric comparisons are not allowed
- D) It can reference any variable in the same module but not variables from child modules
### Question 68 — `precondition` vs `postcondition` — Timing

**Difficulty**: Medium
**Answer Type**: one
**Topic**: When `precondition` and `postcondition` run relative to resource changes

**Question**:
What is the key timing difference between a `precondition` and a `postcondition` in a resource's `lifecycle` block?

- A) `precondition` runs during `terraform plan`; `postcondition` runs during `terraform validate`
- B) `precondition` runs before the resource is changed during apply; `postcondition` runs after the resource change completes
- C) `precondition` validates input variables; `postcondition` validates output values
- D) Both run at the same time — the distinction is only in the error message text
### Question 69 — `self` in `postcondition`

**Difficulty**: Medium
**Answer Type**: one
**Topic**: The `self` reference available in `postcondition` blocks

**Question**:
What does `self` refer to in a `postcondition` block within a resource's `lifecycle`?

- A) The Terraform module that contains the resource
- B) The provider that manages the resource
- C) The resource instance that was just created or updated
- D) The previous state of the resource before the change
### Question 70 — `check` Block Failure Behaviour

**Difficulty**: Medium
**Answer Type**: one
**Topic**: How a failing `check` block assertion affects `terraform apply`

**Question**:
What happens when an `assert` condition inside a `check` block evaluates to `false` during `terraform apply`?

- A) The apply is immediately halted and all changes are rolled back
- B) Terraform pauses and prompts the user to confirm whether to continue despite the failed assertion
- C) A warning is displayed but the apply continues and completes successfully
- D) The resource associated with the `check` block is marked as tainted for replacement on the next run
### Question 71 — `check` Block Introduction Version

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Which Terraform version introduced the `check` block

**Question**:
In which version of Terraform was the `check` block introduced?

- A) Terraform 1.0
- B) Terraform 1.3
- C) Terraform 1.5
- D) Terraform 1.7
### Question 72 — `check` Block Optional Data Source

**Difficulty**: Medium
**Answer Type**: one
**Topic**: The optional scoped data source inside a `check` block

**Question**:
What is the purpose of including a `data` block inside a `check` block?

- A) To import an existing resource into state as part of the health check
- B) To provide a scoped, read-only data source that is used only within that `check` block's assertions
- C) To declare a dependency so the check runs after a specific resource is created
- D) To override the provider used for the assertion data retrieval
### Question 73 — Sensitive Output `sensitive = true`

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Effect of `sensitive = true` on an `output` block

**Question**:
An output block is declared with `sensitive = true`. What is the effect on how Terraform handles this output?

- A) The output is encrypted with a provider-managed key before being stored in state
- B) The output value is shown in plan output but hidden during `terraform output` commands
- C) The output value is redacted in terminal display but still stored in plaintext in the state file
- D) The output is excluded from `terraform output` and cannot be retrieved programmatically
### Question 74 — Sensitive Data in State — Critical Fact

**Difficulty**: Hard
**Answer Type**: one
**Topic**: How `sensitive = true` interacts with `terraform.tfstate` storage

**Question**:
A team marks their database password variable and output as `sensitive = true`. A new engineer asks why the password is still visible when they open `terraform.tfstate` in a text editor. What is the correct explanation?

- A) The password is only encrypted if the team has enabled KMS integration in the provider block
- B) `sensitive = true` protects values in transit between modules but not in the final state file
- C) `sensitive = true` only controls terminal display — all attribute values are always stored in plaintext in the state file regardless of this setting
- D) The state file should be unreadable — the engineer must have the wrong version of Terraform
### Question 75 — Mitigations for Sensitive Data in State

**Difficulty**: Hard
**Answer Type**: many
**Topic**: Recommended approaches to protect sensitive values stored in Terraform state

**Question**:
Which TWO of the following are correct mitigations for the risk that sensitive values are stored in plaintext in Terraform state? (Select two.)

- A) Set `sensitive = true` on all variables and outputs containing secrets
- B) Use a remote backend that supports encryption at rest, such as S3 with server-side encryption or HCP Terraform
- C) Never commit `terraform.tfstate` to source control and restrict access to the state storage location
- D) Use the `prevent_destroy` lifecycle argument to prevent state files from being accidentally deleted
### Question 76 — Comparing the Three Condition Mechanisms

**Difficulty**: Medium
**Answer Type**: many
**Topic**: Failure behaviour of `validation`, `precondition`/`postcondition`, and `check`

**Question**:
Which TWO of the following statements correctly describe how Terraform condition mechanisms handle failures? (Select two.)

- A) A failed `validation` block halts execution before `terraform plan` generates an execution plan
- B) A failed `check` block assertion causes `terraform apply` to roll back all changes made in the current run
- C) A failed `precondition` block halts `terraform apply` before the resource is modified
- D) A failed `postcondition` block converts the failing resource to a warning and allows subsequent resources to continue applying
### Question 77 — Root Module Definition

**Difficulty**: Easy
**Answer Type**: one
**Topic**: What the root module is in a Terraform configuration

**Question**:
What is the Terraform **root module**?

- A) The first module listed in `modules.json` inside `.terraform/`
- B) The working directory from which you run `terraform apply`, containing the top-level configuration files
- C) A published module on the Terraform Registry that all other modules depend on
- D) The `main.tf` file specifically — variables.tf and outputs.tf belong to child modules
### Question 78 — Valid Module Source Types

**Difficulty**: Medium
**Answer Type**: many
**Topic**: Which source types are valid for the `source` argument in a module block

**Question**:
Which TWO of the following are valid values for the `source` argument in a `module` block? (Select two.)

- A) `"./modules/networking"` — a relative local path to a subdirectory
- B) `"hashicorp/consul/aws"` — a Terraform Registry module reference
- C) `"provider::aws::vpc"` — a provider-namespaced module reference
- D) `"module.networking"` — a reference to another module in the same configuration
### Question 79 — Double-Slash `//` in Module Source

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Meaning of `//` in a Git-based module source URL

**Question**:
In the module source `"github.com/org/infra-modules//modules/vpc"`, what does the `//` (double slash) signify?

- A) It is a URL comment indicator and the text after it is ignored
- B) It separates the repository root from a subdirectory path within the repository
- C) It indicates that the module should be downloaded twice for redundancy
- D) It is a typo — only a single slash is valid in module source paths
### Question 80 — `version` Argument Restriction

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Which module source types support the `version` argument

**Question**:
For which module source type is the `version` argument valid?

- A) Local paths only (`"./modules/vpc"`)
- B) Git URLs only (`"git::https://..."`)
- C) Terraform Registry and private registry sources only
- D) All source types support the `version` argument
### Question 81 — Module Cache Location

**Difficulty**: Easy
**Answer Type**: one
**Topic**: Where `terraform init` caches downloaded module source code

**Question**:
Where does `terraform init` cache downloaded child module source code?

- A) `~/.terraform/modules/` in the user's home directory
- B) `terraform.tfstate` alongside the state data
- C) `.terraform/modules/` in the current working directory
- D) `/tmp/terraform-modules/` in a system temporary directory
### Question 82 — Variable Inheritance Between Modules

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Whether child modules inherit variables from the root module automatically

**Question**:
A root module declares `variable "region" { default = "us-east-1" }`. A child module also needs a `region` value. Which statement is correct?

- A) The child module automatically inherits `var.region` from the root module without any additional configuration
- B) The child module inherits the variable only if it is declared in both `variables.tf` files
- C) Variables are never automatically inherited — the root module must explicitly pass the value as an input argument in the `module` block
- D) Variables are inherited only for built-in types (string, number, bool); complex types must be passed explicitly
### Question 83 — Standard Module File Structure

**Difficulty**: Medium
**Answer Type**: many
**Topic**: Files that belong in a standard Terraform module structure

**Question**:
Which TWO files are part of the standard, recommended Terraform module file structure? (Select two.)

- A) `versions.tf` — declares required Terraform and provider versions
- B) `state.tf` — declares the backend configuration for the module's state
- C) `providers.tf` — required to re-declare the provider in every child module
- D) `outputs.tf` — declares the output values exposed by the module
### Question 84 — Backend Block Location in HCL

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Where the `backend` block is declared in Terraform configuration

**Question**:
Where must the `backend` block be declared in a Terraform configuration?

- A) In a dedicated `backend.tf` file at the root of the module
- B) Inside the `terraform {}` block, which is typically placed in `versions.tf` or `main.tf`
- C) Inside a `provider` block, alongside authentication credentials
- D) In `terraform.tfvars` as a backend-specific variable assignment
### Question 85 — `terraform.tfstate.backup` Purpose

**Difficulty**: Medium
**Answer Type**: one
**Topic**: What `terraform.tfstate.backup` contains and its limitations

**Question**:
What does `terraform.tfstate.backup` contain when using the local backend?

- A) A complete versioned history of all previous state files since the project was created
- B) The state from the most recent apply — a single snapshot of the previous state, not a full history
- C) A backup of the state from 24 hours ago, automatically updated on a daily schedule
- D) An encrypted copy of the current state file for disaster recovery
### Question 86 — `terraform init -migrate-state` vs `-reconfigure`

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Difference between `terraform init -migrate-state` and `terraform init -reconfigure`

**Question**:
What is the difference between `terraform init -migrate-state` and `terraform init -reconfigure` when changing backends?

- A) `-migrate-state` only works with S3 backends; `-reconfigure` works with all backend types
- B) `-migrate-state` copies existing state to the new backend; `-reconfigure` reinitialises the backend without migrating existing state
- C) `-reconfigure` is for switching from local to remote backends; `-migrate-state` is for switching between two remote backends
- D) Both flags are identical — they are aliases for the same operation
### Question 87 — S3 Backend State Locking

**Difficulty**: Medium
**Answer Type**: one
**Topic**: How the S3 backend implements state locking

**Question**:
When using the S3 backend, which AWS service provides state locking, and what attribute name is required?

- A) S3 object tagging with a tag key of `TerraformLock`
- B) AWS Systems Manager Parameter Store with a parameter named `terraform-lock`
- C) DynamoDB with a table attribute named `LockID`
- D) CloudWatch Events with a rule named after the state file key
### Question 88 — `terraform force-unlock` Usage

**Difficulty**: Hard
**Answer Type**: one
**Topic**: When and how to use `terraform force-unlock`

**Question**:
When should `terraform force-unlock <LOCK_ID>` be used, and what is the risk?

- A) It should be used routinely after every `terraform apply` to clean up lock artifacts; it carries no risk
- B) It should be used only when you are certain no other `terraform apply` or `plan` is actively running — using it while another operation holds the lock can corrupt state
- C) It should be used whenever `terraform plan` runs slowly, as it removes lock contention caused by stale read locks
- D) It can only be run by the user who created the lock; other users receive a permission error
### Question 89 — `plan -refresh-only` vs `apply -refresh-only`

**Difficulty**: Hard
**Answer Type**: many
**Topic**: Distinguishing `terraform plan -refresh-only` from `terraform apply -refresh-only`

**Question**:
Which TWO statements correctly describe the behaviour of the `-refresh-only` flag? (Select two.)

- A) `terraform plan -refresh-only` shows what has drifted in the cloud compared to state, but proposes no infrastructure changes
- B) `terraform apply -refresh-only` modifies cloud resources to match the Terraform configuration, resolving drift by re-applying desired state
- C) `terraform apply -refresh-only` updates the state file to reflect the current actual state of cloud resources, without creating, modifying, or destroying any infrastructure
- D) `terraform plan -refresh-only` is equivalent to `terraform refresh`, which is a deprecated command that both refreshes state and applies the plan in one step
### Question 90 — `import` Block vs CLI Import

**Difficulty**: Easy
**Answer Type**: one
**Topic**: Which import method is preferred in Terraform 1.5+ and why

**Question**:
What is the primary advantage of using an `import` block (Terraform 1.5+) over the legacy `terraform import` CLI command?

- A) The `import` block is faster because it uses parallel imports; the CLI command is sequential
- B) The `import` block can be previewed with `terraform plan` before changes are applied, and can optionally generate HCL configuration automatically
- C) The `import` block supports all resource types; the CLI command only supports AWS resources
- D) The `import` block requires no existing resource block in configuration; the CLI command requires one
### Question 91 — `import` Block Syntax

**Difficulty**: Easy
**Answer Type**: one
**Topic**: Required arguments in an `import` block

**Question**:
Which two arguments are required in an `import` block?

- A) `source` and `destination`
- B) `resource` and `cloud_id`
- C) `to` and `id`
- D) `address` and `provider_id`
### Question 92 — CLI Import Pre-Requisite

**Difficulty**: Medium
**Answer Type**: one
**Topic**: What must exist in configuration before running `terraform import` CLI command

**Question**:
What must exist in the Terraform configuration before running `terraform import aws_s3_bucket.assets my-bucket-name`?

- A) Nothing — `terraform import` creates both the state entry and the HCL resource block automatically
- B) An `import` block referencing the same resource address
- C) A `resource "aws_s3_bucket" "assets" {}` block must already exist in the configuration files
- D) A `data "aws_s3_bucket" "assets" {}` block must exist to look up the bucket first
### Question 93 — `terraform plan -generate-config-out`

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Purpose of the `-generate-config-out` flag

**Question**:
What does `terraform plan -generate-config-out=generated.tf` do?

- A) Saves the execution plan to a file named `generated.tf` that can be passed to `terraform apply`
- B) Generates HCL resource configuration for resources referenced in `import` blocks and writes it to `generated.tf`
- C) Exports all existing resources in state as HCL configuration into `generated.tf`
- D) Generates a Terraform provider configuration block and appends it to `generated.tf`
### Question 94 — `TF_LOG` Verbosity Order

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Order of `TF_LOG` levels from most to least verbose

**Question**:
Which ordering correctly lists Terraform's `TF_LOG` levels from **most verbose** to **least verbose**?

- A) `ERROR > WARN > INFO > DEBUG > TRACE > OFF`
- B) `TRACE > DEBUG > INFO > WARN > ERROR > OFF`
- C) `DEBUG > TRACE > INFO > WARN > ERROR > OFF`
- D) `INFO > DEBUG > TRACE > WARN > ERROR > OFF`
### Question 95 — `TF_LOG_PATH` and Separate Core/Provider Logging

**Difficulty**: Medium
**Answer Type**: many
**Topic**: `TF_LOG_PATH`, `TF_LOG_CORE`, and `TF_LOG_PROVIDER` environment variables

**Question**:
Which TWO statements correctly describe Terraform's logging environment variables? (Select two.)

- A) `TF_LOG_PATH=/tmp/tf.log` causes Terraform to write log output to that file instead of stderr
- B) `TF_LOG_CORE=DEBUG` and `TF_LOG_PROVIDER=TRACE` allow setting different log levels for Terraform core and provider plugins independently
- C) `TF_LOG_PATH` must be set to an absolute path; relative paths are not supported
- D) Setting `TF_LOG_PROVIDER=TRACE` also automatically sets `TF_LOG_CORE=TRACE`
### Question 96 — HCP Terraform `cloud` Block

**Difficulty**: Medium
**Answer Type**: one
**Topic**: The `cloud` block and when it was introduced

**Question**:
What is the preferred way to connect a Terraform configuration to HCP Terraform (Terraform 1.1+), and which two arguments does it require?

- A) `backend "remote"` block with `hostname` and `token` arguments
- B) `cloud` block with `organization` and `workspaces` arguments
- C) `cloud` block with `hostname` and `workspace_id` arguments
- D) `provider "tfe"` block with `organization` and `token` arguments
### Question 97 — `terraform login` Token Storage

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Where `terraform login` stores the API token

**Question**:
Where does `terraform login` store the HCP Terraform API token after a successful browser-based authentication?

- A) `terraform.tfvars` in the current working directory
- B) `.terraform/credentials.json` in the current working directory
- C) `~/.terraform.d/credentials.tfrc.json` in the user's home directory
- D) The token is never stored on disk — it is only held in memory for the current session
### Question 98 — HCP Terraform Run Types

**Difficulty**: Medium
**Answer Type**: one
**Topic**: The three HCP Terraform run types

**Question**:
Which HCP Terraform run type runs a plan but **never applies** — typically triggered by a pull request to show what would change?

- A) Plan-only run
- B) Speculative plan
- C) Plan-and-apply run
- D) Dry-run
### Question 99 — HCP Terraform Policy Enforcement Levels

**Difficulty**: Medium
**Answer Type**: one
**Topic**: The three Sentinel/OPA policy enforcement levels

**Question**:
Which HCP Terraform policy enforcement level **blocks a run** when a policy fails but **allows an authorised user to override** the failure and proceed?

- A) `advisory`
- B) `soft-mandatory`
- C) `hard-mandatory`
- D) `blocking`
### Question 100 — Variable Sets in HCP Terraform

**Difficulty**: Medium
**Answer Type**: one
**Topic**: What variable sets are and how they are used

**Question**:
What is the purpose of a **variable set** in HCP Terraform?

- A) A set of required variables that must be declared in every workspace's `variables.tf`
- B) A reusable collection of Terraform or environment variables that can be assigned to multiple workspaces or an entire organisation
- C) A list of sensitive variable names whose values are automatically redacted from run logs
- D) A JSON file that defines default variable values, similar to `terraform.tfvars`
### Question 101 — HCP Terraform Workspace Permissions

**Difficulty**: Hard
**Answer Type**: many
**Topic**: The four workspace-level permission tiers in HCP Terraform

**Question**:
Which TWO statements correctly describe HCP Terraform workspace-level permissions? (Select two.)

- A) The **Write** permission allows a user to trigger runs and approve applies, but not to manage workspace settings or team access
- B) The **Plan** permission allows a user to trigger full plan-and-apply runs without any additional approval
- C) The **Read** permission allows a user to view run history, state, and variables but not trigger any runs
- D) The **Admin** permission is required to change workspace variables — the Write permission does not allow variable changes
### Question 102 — Dynamic Provider Credentials (OIDC)

**Difficulty**: Hard
**Answer Type**: one
**Topic**: Purpose and benefit of dynamic provider credentials using OIDC in HCP Terraform

**Question**:
What is the primary security benefit of using **dynamic provider credentials** (OIDC) in HCP Terraform workspaces?

- A) OIDC credentials are stored in HCP Terraform's vault and rotated every 24 hours automatically
- B) OIDC eliminates the need to store long-lived static cloud credentials in HCP Terraform — each run receives a short-lived token that expires after the run completes
- C) OIDC allows multiple cloud providers to share a single set of credentials, reducing the number of secrets to manage
- D) OIDC enables HCP Terraform to bypass multi-factor authentication requirements for cloud providers



## Answer Key

| Q# | Answer(s) | Explanation | Source | Difficulty |
|---|---|---|---|---|
| 2 | B | N/A | What Infrastructure as Code is | Easy |
| 3 | C | N/A | Desired state and current state concepts | Easy |
| 4 | C | N/A | Idempotency in IaC | Medium |
| 5 | B | N/A | Declarative approach in Terraform | Medium |
| 6 | B, D | N/A | Benefits of using IaC | Medium |
| 7 | B | N/A | Terraform multi-cloud capability | Medium |
| 8 | C | N/A | Terraform vs other IaC tools | Medium |
| 9 | B | N/A | Infrastructure drift and IaC | Medium |
| 10 | B, C | N/A | Drawbacks of manual (ClickOps) provisioning | Medium |
| 11 | C | N/A | Classifying IaC tools by approach | Hard |
| 12 | B | N/A | Disaster recovery with IaC | Hard |
| 13 | B, C | N/A | Version control and auditability of IaC | Medium |
| 14 | B | N/A | What a Terraform provider is | Easy |
| 15 | C | N/A | Provider tier classification | Easy |
| 16 | C | N/A | Terraform Core and provider communication protocol | Medium |
| 17 | B | N/A | Provider source address and default registry hostname | Medium |
| 18 | C | N/A | Where terraform init installs providers | Medium |
| 19 | B | N/A | `.terraform.lock.hcl` purpose and version control | Medium |
| 20 | C | N/A | `~>` version constraint operator behaviour | Medium |
| 21 | B | N/A | Provider alias for multiple configurations | Medium |
| 22 | C | N/A | Content and purpose of the Terraform state file | Medium |
| 23 | B, C | N/A | Sources Terraform compares during `terraform plan` | Medium |
| 24 | B | N/A | Differences between local and remote Terraform state | Hard |
| 25 | C | N/A | Behaviour of `sensitive = true` in outputs vs state storage | Hard |
| 26 | B, D | N/A | Terraform state CLI subcommands | Medium |
| 27 | B | N/A | Correct order of the core Terraform CLI workflow | Easy |
| 28 | B | N/A | What `terraform init` does | Easy |
| 29 | A, C | N/A | Conditions requiring `terraform init` to be re-run | Medium |
| 30 | C | N/A | `terraform validate` network access and what it checks | Medium |
| 31 | C | N/A | `terraform fmt -check` flag behaviour | Medium |
| 32 | B | N/A | Saving and applying a plan file | Medium |
| 33 | C | N/A | Meaning of `terraform plan` output symbols | Medium |
| 34 | B | N/A | Purpose and use case of `-auto-approve` | Medium |
| 35 | B | N/A | Forcing resource replacement with `-replace` | Medium |
| 36 | B | N/A | `terraform output -raw` use case | Medium |
| 37 | B | N/A | What `terraform console` is used for | Medium |
| 38 | B | N/A | Relationship between `terraform destroy` and `terraform apply -destroy` | Hard |
| 39 | B, D | N/A | Distinguishing what `fmt` and `validate` check | Hard |
| 40 | B | N/A | Resource block syntax and components | Easy |
| 41 | B | N/A | What a data source does | Easy |
| 42 | C | N/A | How to reference a data source attribute | Medium |
| 43 | B, D | N/A | Resource meta-arguments | Medium |
| 44 | B | N/A | How implicit dependencies are created | Medium |
| 45 | C | N/A | When to use `depends_on` | Medium |
| 46 | B | N/A | `create_before_destroy` lifecycle argument | Medium |
| 47 | C | N/A | `prevent_destroy` lifecycle argument | Medium |
| 48 | B | N/A | `ignore_changes` lifecycle argument | Medium |
| 49 | B | N/A | `replace_triggered_by` lifecycle argument | Medium |
| 50 | B | N/A | What the `moved` block does in Terraform state | Hard |
| 51 | B | N/A | Terraform default parallelism and the `-parallelism` flag | Hard |
| 52 | B, C | N/A | Timing of data source reads during plan and apply | Medium |
| 53 | C | N/A | Order of variable value precedence (highest wins) | Medium |
| 54 | B | N/A | Effect of `sensitive = true` on variables vs state | Medium |
| 55 | C | N/A | What a variable `validation` block can reference | Medium |
| 56 | B | N/A | Difference between `locals` and `variable` blocks | Easy |
| 57 | C | N/A | Referencing a child module's output value | Medium |
| 58 | B | N/A | When to prefer `for_each` over `count` | Easy |
| 59 | C | N/A | Accessing `count`-based resource instances | Medium |
| 60 | B | N/A | Behaviour of `each.key` and `each.value` when `for_each` uses a set | Medium |
| 61 | B | N/A | `for` expression syntax with an `if` filter clause | Medium |
| 62 | C | N/A | `lookup()` function signature and default value | Medium |
| 63 | C | N/A | `cidrsubnet()` function parameters and result | Hard |
| 64 | A, B | N/A | Distinguishing `flatten()` and `compact()` use cases | Hard |
| 65 | A, B | N/A | When to use `templatefile()` instead of `file()` | Medium |
| 66 | B | N/A | The three Terraform condition mechanisms and where each is declared | Easy |
| 67 | C | N/A | When variable `validation` blocks are evaluated | Easy |
| 68 | B | N/A | What a `validation` condition can reference | Medium |
| 69 | B | N/A | When `precondition` and `postcondition` run relative to resource changes | Medium |
| 70 | C | N/A | The `self` reference available in `postcondition` blocks | Medium |
| 71 | C | N/A | How a failing `check` block assertion affects `terraform apply` | Medium |
| 72 | C | N/A | Which Terraform version introduced the `check` block | Medium |
| 73 | B | N/A | The optional scoped data source inside a `check` block | Medium |
| 74 | C | N/A | Effect of `sensitive = true` on an `output` block | Medium |
| 75 | C | N/A | How `sensitive = true` interacts with `terraform.tfstate` storage | Hard |
| 76 | B, C | N/A | Recommended approaches to protect sensitive values stored in Terraform state | Hard |
| 77 | A, C | N/A | Failure behaviour of `validation`, `precondition`/`postcondition`, and `check` | Medium |
| 78 | B | N/A | What the root module is in a Terraform configuration | Easy |
| 79 | A, B | N/A | Which source types are valid for the `source` argument in a module block | Medium |
| 80 | B | N/A | Meaning of `//` in a Git-based module source URL | Medium |
| 81 | C | N/A | Which module source types support the `version` argument | Medium |
| 82 | C | N/A | Where `terraform init` caches downloaded module source code | Easy |
| 83 | C | N/A | Whether child modules inherit variables from the root module automatically | Medium |
| 84 | A, D | N/A | Files that belong in a standard Terraform module structure | Medium |
| 85 | B | N/A | Where the `backend` block is declared in Terraform configuration | Medium |
| 86 | B | N/A | What `terraform.tfstate.backup` contains and its limitations | Medium |
| 87 | B | N/A | Difference between `terraform init -migrate-state` and `terraform init -reconfigure` | Medium |
| 88 | C | N/A | How the S3 backend implements state locking | Medium |
| 89 | B | N/A | When and how to use `terraform force-unlock` | Hard |
| 90 | A, C | N/A | Distinguishing `terraform plan -refresh-only` from `terraform apply -refresh-only` | Hard |
| 91 | B | N/A | Which import method is preferred in Terraform 1.5+ and why | Easy |
| 92 | C | N/A | Required arguments in an `import` block | Easy |
| 93 | C | N/A | What must exist in configuration before running `terraform import` CLI command | Medium |
| 94 | B | N/A | Purpose of the `-generate-config-out` flag | Medium |
| 95 | B | N/A | Order of `TF_LOG` levels from most to least verbose | Medium |
| 96 | A, B | N/A | `TF_LOG_PATH`, `TF_LOG_CORE`, and `TF_LOG_PROVIDER` environment variables | Medium |
| 97 | B | N/A | The `cloud` block and when it was introduced | Medium |
| 98 | C | N/A | Where `terraform login` stores the API token | Medium |
| 99 | B | N/A | The three HCP Terraform run types | Medium |
| 100 | B | N/A | The three Sentinel/OPA policy enforcement levels | Medium |
| 101 | B | N/A | What variable sets are and how they are used | Medium |
| 102 | A, C | N/A | The four workspace-level permission tiers in HCP Terraform | Hard |
| 103 | B | N/A | Purpose and benefit of dynamic provider credentials using OIDC in HCP Terraform | Hard |
