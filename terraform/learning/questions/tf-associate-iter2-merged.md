# Terraform Associate Exam Questions

### Question 1 — Second Apply with Unchanged Config

**Difficulty**: Easy
**Answer Type**: one
**Topic**: What Terraform reports when infrastructure already matches the configuration

**Question**:
A Terraform configuration that provisions three EC2 instances is applied successfully. No changes are made to the configuration files or the infrastructure. `terraform apply` is run again. What does Terraform report?

- A) `Error: 3 resources already exist. Run terraform import to manage them.`
- B) `Apply complete! Resources: 3 added, 0 changed, 0 destroyed.`
- C) `No changes. Your infrastructure matches the configuration.`
- D) `Warning: State drift detected. Run terraform refresh before applying.`

### Question 2 — Manual Deletion Followed by Plan

**Difficulty**: Easy
**Answer Type**: one
**Topic**: Terraform's response when a resource is manually deleted from the cloud

**Question**:
A Terraform configuration declares three EC2 instances. All three are running. An administrator manually terminates one of the instances through the AWS console. A team member then runs `terraform plan`. What does Terraform propose?

- A) Terraform detects no changes because it only checks the state file, not the actual cloud
- B) Terraform proposes creating one EC2 instance to restore the desired count of three
- C) Terraform proposes destroying the remaining two instances to match the deleted resource
- D) Terraform returns an error because the state file is now out of sync

### Question 3 — Reducing Instance Count

**Difficulty**: Medium
**Answer Type**: one
**Topic**: What happens when a declarative config reduces a resource count

**Question**:
A configuration currently manages five EC2 instances (`count = 5`). A developer updates the configuration to `count = 3` and runs `terraform apply`. What happens to the extra two instances?

- A) The two extra instances are left running; Terraform only creates new resources, never destroys
- B) Terraform returns an error because reducing count requires manual removal first
- C) Terraform destroys the two instances that are no longer described by the desired state
- D) Terraform marks the two instances as tainted so they are replaced on the next apply

### Question 4 — Increasing Instance Count

**Difficulty**: Medium
**Answer Type**: one
**Topic**: What terraform plan shows when count is increased

**Question**:
A configuration currently manages two running EC2 instances (`count = 2`). A developer changes the configuration to `count = 5` and runs `terraform plan`. What does the plan output show?

- A) `Plan: 5 to add, 0 to change, 0 to destroy.` — Terraform creates all five from scratch
- B) `Plan: 3 to add, 0 to change, 0 to destroy.` — Terraform creates only the three additional instances
- C) `Plan: 2 to destroy, 5 to add` — Terraform destroys and recreates all instances
- D) `Error: count cannot be increased after initial apply`

### Question 5 — Out-of-Band Tag Change

**Difficulty**: Medium
**Answer Type**: one
**Topic**: What happens when a manual change is made outside Terraform then apply runs

**Question**:
A Terraform configuration provisions an EC2 instance with the tag `Environment = "production"`. A cloud administrator manually changes the tag to `Environment = "legacy"` using the AWS console. A developer then runs `terraform apply`. What happens?

- A) Terraform ignores tag changes because tags are not tracked in state
- B) Terraform detects the drift and overwrites the tag back to `Environment = "production"` to match the desired state
- C) Terraform leaves the tag as `Environment = "legacy"` and updates the state file to record the new value
- D) Terraform destroys and recreates the instance to restore the original tag value

### Question 6 — Terraform vs Ansible Idempotency

**Difficulty**: Medium
**Answer Type**: many
**Topic**: Behavioural differences between Terraform (declarative) and Ansible (imperative) on repeated runs

**Question**:
A team uses Terraform to provision a server and also has an Ansible playbook that runs shell commands to provision an equivalent server. They run each tool a second time against the same environment. Which TWO statements correctly describe the difference in behaviour? (Select two.)

- A) Terraform reports no changes on the second run because the current state already matches the desired state
- B) The Ansible playbook may attempt to re-execute commands regardless of whether they have already been applied, depending on how the playbook is written
- C) Both Terraform and a typical imperative Ansible playbook behave identically — neither makes changes on the second run
- D) Terraform destroys and recreates the server on every run to ensure a fresh state

### Question 7 — Console Change and Version History

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Audit trail behaviour when infrastructure is changed outside of code

**Question**:
An engineer modifies an RDS instance's storage size directly through the AWS console. The Terraform configuration file is never updated. Six months later, the team tries to audit what changed and when. What is the outcome?

- A) The change is captured automatically in Terraform's version history within the state file
- B) There is no record of the change in version control because it was not made through code — the audit trail has a gap
- C) AWS CloudTrail records the change, which Terraform automatically imports into its audit log
- D) The change appears in the Terraform plan output as a historical entry

### Question 8 — Multi-Cloud Resources in One Config

**Difficulty**: Medium
**Answer Type**: one
**Topic**: What happens when a config declares resources from multiple cloud providers

**Question**:
A Terraform configuration declares an `aws_s3_bucket` resource and an `azurerm_storage_account` resource in the same root module. The appropriate provider blocks for both AWS and Azure are configured. What happens when `terraform apply` runs?

- A) Terraform returns an error because only one cloud provider is allowed per configuration
- B) Terraform applies the AWS resource first, waits for confirmation, then applies the Azure resource separately
- C) Terraform provisions both resources using their respective provider plugins as part of a single apply operation
- D) Terraform applies only the AWS resource; Azure resources require a separate workspace

### Question 9 — Disaster Recovery with Config and State

**Difficulty**: Medium
**Answer Type**: one
**Topic**: What apply produces when recreating a lost environment from code and state backup

**Question**:
A cloud environment is completely destroyed by an incident. The team has their Terraform configuration files in a git repository and a recent backup of their state file. They restore the state file to their backend and run `terraform apply`. What does Terraform do?

- A) Terraform does nothing because the state file records resources as existing, even though they are gone
- B) Terraform detects that every resource recorded in state no longer exists in the cloud and proposes recreating the entire environment
- C) Terraform requires `terraform import` for every resource before any apply can succeed
- D) Terraform can only recreate resources created in the last 24 hours due to provider API limitations

### Question 10 — Zero Count Destroys All

**Difficulty**: Medium
**Answer Type**: many
**Topic**: Behavioural prediction when count is set to zero and apply runs

**Question**:
A configuration currently manages four EC2 instances. A developer updates the configuration to `count = 0` and runs `terraform apply`. Which TWO statements correctly describe what happens? (Select two.)

- A) Terraform proposes destroying all four existing EC2 instances during the plan phase
- B) Terraform reports `Plan: 0 to add, 0 to change, 4 to destroy.` and prompts for confirmation before proceeding
- C) Terraform ignores the `count = 0` change and retains the existing four instances as unmanaged orphans
- D) Terraform creates zero instances without touching the existing four, because create and destroy are separate operations

### Question 11 — Applying Same Config to Three Environments

**Difficulty**: Hard
**Answer Type**: one
**Topic**: Reproducibility across environments using identical IaC configuration

**Question**:
A team applies the exact same Terraform configuration to three separate workspaces representing development, staging, and production (each with its own state file and isolated cloud accounts). No manual changes are made in any environment. What is the expected state of each environment after apply?

- A) Each environment will differ because cloud providers assign different resource IDs, causing configuration drift
- B) Each environment will have identical infrastructure topology, resource types, and configuration — resource IDs differ but the structure is the same
- C) The production environment will differ because Terraform applies additional safety rules automatically in accounts tagged as production
- D) The staging and production environments will match, but development will differ because Terraform uses lower-cost defaults for development workspaces

### Question 12 — Switching from ClickOps to IaC

**Difficulty**: Hard
**Answer Type**: one
**Topic**: Behavioural change when a team adopts IaC after managing infrastructure manually

**Question**:
A team has been managing cloud infrastructure entirely through the AWS console (ClickOps) for two years. They decide to adopt Terraform. During the transition, an engineer imports all existing resources into Terraform state and creates matching configuration files. A second engineer later makes a change to a resource through the AWS console — not through Terraform. The first engineer then runs `terraform plan`. What does Terraform most likely report?

- A) No changes — Terraform only tracks resources that it originally created, not imported resources
- B) The console change is detected as drift, and Terraform proposes reverting the resource to match the configuration
- C) Terraform deletes all resources not originally created by Terraform, including the manually changed one
- D) Terraform updates its state file to match the console change and reports the configuration as out of date

### Question 13 — Apply Without Init

**Difficulty**: Easy
**Answer Type**: one
**Topic**: What happens when terraform apply runs before terraform init

**Question**:
A developer clones a Terraform repository and immediately runs `terraform apply` without first running `terraform init`. What happens?

- A) Terraform applies the configuration successfully using the provider versions from the previous engineer's machine
- B) Terraform returns an error because the required provider plugins have not been downloaded yet
- C) Terraform downloads the providers on-the-fly during apply and then proceeds
- D) Terraform applies the configuration but skips any resources that require provider authentication

### Question 14 — Init with `~> 5.0` Constraint

**Difficulty**: Easy
**Answer Type**: one
**Topic**: Which provider version gets installed when `~> 5.0` is specified and v5.31 is available

**Question**:
A `required_providers` block specifies `version = "~> 5.0"` for the AWS provider. The latest available versions are `5.31.0` and `6.0.0`. `terraform init` is run for the first time (no lock file exists). Which version is installed?

- A) `6.0.0` — the absolute latest version available
- B) `5.31.0` — the latest version within the `>= 5.0, < 6.0` range
- C) `5.0.0` — the minimum version satisfying the constraint
- D) The command fails because `~>` requires an exact version number

### Question 15 — Lock File Not Committed

**Difficulty**: Easy
**Answer Type**: one
**Topic**: What happens when .terraform.lock.hcl is not committed to version control

**Question**:
A team does not commit `.terraform.lock.hcl` to their git repository. Engineer A runs `terraform init` on Monday and installs AWS provider `5.28.0`. On Tuesday, AWS provider `5.31.0` is released. Engineer B clones the repo and runs `terraform init`. What happens?

- A) Engineer B gets the same `5.28.0` version because the lock file is shared through Terraform's registry cache
- B) Engineer B gets `5.28.0` because `terraform init` always installs the minimum version satisfying the constraint
- C) Engineer B installs the latest version matching the constraint — potentially `5.31.0` — resulting in a different provider version than Engineer A
- D) `terraform init` fails because there is no lock file to verify against

### Question 16 — `terraform init -upgrade` Behaviour

**Difficulty**: Medium
**Answer Type**: one
**Topic**: What terraform init -upgrade does when a newer provider version is available

**Question**:
The lock file records AWS provider `5.10.0`. The `required_providers` constraint is `~> 5.0`. AWS provider `5.31.0` has since been released. `terraform init -upgrade` is run. What happens?

- A) The command fails because the lock file must be deleted manually before upgrading
- B) The command ignores the upgrade request because `5.10.0` still satisfies the constraint
- C) Terraform updates the lock file to `5.31.0` and downloads the new provider binary
- D) Terraform upgrades to the newest available version — including `6.0.0` — ignoring the constraint

### Question 17 — Provider Alias Resource Assignment

**Difficulty**: Medium
**Answer Type**: one
**Topic**: What happens when a resource omits a provider argument when multiple provider configs exist

**Question**:
Two AWS provider configurations are declared: a default (`region = "us-east-1"`) and an aliased one (`alias = "west", region = "us-west-2"`). An `aws_instance` resource block is written without a `provider` argument. In which region is the instance created?

- A) `us-west-2` — Terraform uses the most recently declared provider
- B) `us-east-1` — Terraform uses the default (unaliased) provider configuration
- C) Terraform returns an error because the `provider` argument is required when multiple configs exist
- D) Terraform creates an instance in both regions because it cannot determine which to use

### Question 18 — `terraform state rm` Effect

**Difficulty**: Medium
**Answer Type**: one
**Topic**: What happens to a cloud resource after terraform state rm is run

**Question**:
A team runs `terraform state rm aws_s3_bucket.legacy`. The S3 bucket exists in the cloud. What is the outcome?

- A) The S3 bucket is immediately deleted from AWS
- B) The S3 bucket is deleted from AWS on the next `terraform apply`
- C) The S3 bucket continues to exist in AWS but is no longer tracked or managed by Terraform
- D) Terraform marks the bucket as tainted and schedules it for replacement on the next apply

### Question 19 — Concurrent Local State Applies

**Difficulty**: Medium
**Answer Type**: many
**Topic**: What happens when two engineers run terraform apply simultaneously with local state

**Question**:
Two engineers working on the same project both have the local `terraform.tfstate` file on their laptops. They run `terraform apply` at the same time against the same cloud environment. Which TWO outcomes are likely? (Select two.)

- A) Terraform detects the simultaneous apply and queues them sequentially without any data loss
- B) Both applies may succeed independently, but their state files will now differ and be out of sync with each other
- C) One apply may overwrite the other's state file changes, leading to state corruption or lost resource tracking
- D) Local state automatically merges changes from both applies into a unified state file

### Question 20 — Plan with Sensitive Output

**Difficulty**: Medium
**Answer Type**: one
**Topic**: What happens to a sensitive output value in plan output vs state

**Question**:
An output is declared as:

```hcl
output "db_password" {
  value     = aws_db_instance.main.password
  sensitive = true
}
```

`terraform apply` completes successfully. What is the behaviour?

- A) The password is hidden from the terminal output and is also encrypted in `terraform.tfstate`
- B) The password is displayed in the terminal but marked with a warning; it is encrypted in state
- C) The password is hidden from the terminal output (`(sensitive value)`), but it is stored in plaintext in `terraform.tfstate`
- D) The password is hidden from both the terminal and state, requiring the engineer to retrieve it from the cloud provider

### Question 21 — `terraform plan -refresh=false` After Manual Change

**Difficulty**: Medium
**Answer Type**: one
**Topic**: What plan -refresh=false reports when cloud has drifted

**Question**:
An engineer manually changes an EC2 instance's type from `t3.micro` to `t3.large` through the AWS console. The Terraform configuration still declares `t3.micro`. A team member runs `terraform plan -refresh=false`. What does Terraform report?

- A) Terraform detects the drift and proposes reverting the instance type to `t3.micro`
- B) Terraform reports no changes because `-refresh=false` uses cached state, which still records `t3.micro`, and the configuration also declares `t3.micro`
- C) Terraform reports no changes and automatically updates the configuration to match the new instance type
- D) Terraform returns an error because `-refresh=false` cannot be used after manual changes

### Question 22 — State After `terraform state mv`

**Difficulty**: Medium
**Answer Type**: one
**Topic**: What terraform state mv does to the resource in the cloud

**Question**:
An engineer runs `terraform state mv aws_instance.app aws_instance.web`. The EC2 instance is running in AWS. What is the immediate outcome?

- A) The EC2 instance is destroyed and recreated with the name `web`
- B) The state file is updated to reference the instance as `aws_instance.web`; the EC2 instance itself is untouched
- C) The command updates both the state file and the `.tf` configuration file to rename the resource
- D) The EC2 instance's Name tag is updated to `web` in AWS

### Question 23 — Applying with Multiple Providers and No Authentication

**Difficulty**: Medium
**Answer Type**: many
**Topic**: What happens when a provider config has no credentials at apply time

**Question**:
A configuration declares an AWS provider and a Google provider but no authentication credentials are set in the provider blocks, environment variables, or credential files. `terraform apply` is run. Which TWO outcomes are most likely? (Select two.)

- A) Terraform skips resources belonging to providers with missing credentials and applies only the remaining resources
- B) Terraform begins the apply, but resource operations fail with authentication errors when provider API calls are made
- C) `terraform plan` and `terraform apply` may fail or produce errors during provider initialisation if the providers cannot authenticate
- D) Terraform uses anonymous access where available and creates public-only resources without authentication

### Question 24 — Deleting the State File Before Plan

**Difficulty**: Hard
**Answer Type**: one
**Topic**: What terraform plan proposes when the state file is missing

**Question**:
A Terraform configuration manages 15 cloud resources. The `terraform.tfstate` file is accidentally deleted. `terraform plan` is run immediately after. What does Terraform propose?

- A) Terraform returns an error because it cannot run without a state file
- B) Terraform detects the 15 existing resources via API and proposes no changes
- C) Terraform treats all 15 resources as non-existent and proposes creating all of them
- D) Terraform recreates the state file automatically by querying the cloud API

### Question 25 — gRPC Failure Between Core and Provider

**Difficulty**: Hard
**Answer Type**: one
**Topic**: What happens if the provider plugin crashes during an apply

**Question**:
During a `terraform apply`, the AWS provider plugin process crashes mid-operation while creating a resource. What is the most likely consequence?

- A) Terraform Core detects the crash, rolls back all changes already made, and returns the infrastructure to its pre-apply state
- B) Terraform Core reports an error; the resource may be partially created in AWS but not recorded in state, requiring manual reconciliation
- C) Terraform Core restarts the provider plugin automatically and retries the failed operation from the beginning
- D) The crash causes Terraform Core to also terminate, leaving state permanently corrupted

### Question 26 — fmt on Already-Formatted Files

**Difficulty**: Easy
**Answer Type**: one
**Topic**: What terraform fmt reports when all files are already canonical

**Question**:
An engineer runs `terraform fmt` on a directory where all `.tf` files are already in canonical format. What happens?

- A) Terraform rewrites all `.tf` files to ensure they have the latest formatting conventions, even if nothing changes
- B) Terraform reports no output and exits with code 0 — no files are modified
- C) Terraform prompts the engineer to confirm whether files should be reformatted
- D) Terraform returns an error because `fmt` requires at least one file change to complete

### Question 27 — validate Catches Undefined Reference

**Difficulty**: Easy
**Answer Type**: one
**Topic**: What terraform validate returns when a resource references an undefined local

**Question**:
A configuration contains this expression: `name = local.environment_name`, but no `locals` block defining `environment_name` exists in any `.tf` file. `terraform validate` is run. What happens?

- A) Terraform silently ignores the undefined reference and validates the remaining configuration
- B) Terraform returns an error such as `Reference to undeclared local value` and exits with a non-zero code
- C) Terraform creates an empty `locals` block and sets `environment_name = null` to resolve the reference
- D) The error is deferred until `terraform plan` because `validate` does not check local references

### Question 28 — plan -target Scope Limiting

**Difficulty**: Easy
**Answer Type**: one
**Topic**: What terraform plan -target does to the rest of the configuration

**Question**:
A configuration manages 20 resources. An engineer runs `terraform plan -target=aws_instance.web`. What does Terraform plan for?

- A) All 20 resources, but it highlights `aws_instance.web` as the primary resource
- B) Only `aws_instance.web` and any resources that `aws_instance.web` directly or indirectly depends on
- C) Only `aws_instance.web`, ignoring all dependencies
- D) The 20 resources grouped by provider, starting with `aws_instance.web`

### Question 29 — Infrastructure Change Between Plan and Apply

**Difficulty**: Medium
**Answer Type**: one
**Topic**: What happens when a saved plan file is applied after infrastructure changes

**Question**:
An engineer runs `terraform plan -out=release.tfplan` and reviews the plan showing 3 resources to add. Before running `terraform apply release.tfplan`, another engineer manually deletes one of those resources' dependencies from the cloud. The first engineer runs `terraform apply release.tfplan`. What happens?

- A) Terraform re-plans automatically, detects the change, and updates the plan before applying
- B) Terraform applies the exact changes captured in `release.tfplan` without re-planning — the apply may fail or produce unexpected results if the dependency is missing
- C) Terraform detects the out-of-band change and refuses to apply the saved plan, prompting the engineer to re-run plan
- D) Terraform skips the resource whose dependency is missing and applies the other two successfully

### Question 30 — fmt -check in a CI Pipeline

**Difficulty**: Medium
**Answer Type**: one
**Topic**: What terraform fmt -check returns when a file has incorrect formatting

**Question**:
A CI pipeline runs `terraform fmt -check` as part of a pull request check. A developer submits a PR that contains a `.tf` file with inconsistent indentation. What does the CI step report?

- A) The check passes with a warning, and the CI pipeline auto-formats the file in-place
- B) The check fails with exit code 1, and the PR check is marked as failed — no files are modified
- C) The check passes because `fmt` only verifies syntax, not style
- D) The check fails and `fmt` rewrites the file directly in the developer's PR branch

### Question 31 — graph Command Output Format

**Difficulty**: Medium
**Answer Type**: one
**Topic**: What terraform graph outputs and how it is rendered

**Question**:
An engineer runs `terraform graph`. What does the command output, and what additional tool is required to visualise it?

- A) An SVG image of the dependency graph rendered directly in the terminal
- B) A JSON file describing all resource dependencies, viewable in any text editor
- C) A DOT format text representation of the dependency graph — Graphviz is required to render it as an image
- D) An HTML page that can be opened in a browser to interactively explore the resource graph

### Question 32 — apply -replace Resource Lifecycle

**Difficulty**: Medium
**Answer Type**: one
**Topic**: What terraform apply -replace does to the targeted resource

**Question**:
An EC2 instance `aws_instance.app` is running normally. An engineer runs `terraform apply -replace="aws_instance.app"`. The configuration has not changed. What does Terraform do?

- A) Terraform skips the command because no configuration changes exist — replace requires a config change
- B) Terraform destroys the existing instance and creates a new one, even though the configuration is unchanged
- C) Terraform updates the instance in-place without destroying it
- D) Terraform marks the instance as tainted in state but takes no immediate action

### Question 33 — output -raw vs Standard output

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Difference in output format between terraform output and terraform output -raw

**Question**:
A Terraform output is declared as:

```hcl
output "bucket_name" {
  value = aws_s3_bucket.main.id
}
```

The bucket ID is `my-app-bucket-prod`. An engineer runs both `terraform output bucket_name` and `terraform output -raw bucket_name` in a shell script. What is the difference in the values each command returns?

- A) `terraform output bucket_name` returns `"my-app-bucket-prod"` (with surrounding quotes); `terraform output -raw bucket_name` returns `my-app-bucket-prod` (no quotes)
- B) Both commands return identical output — `my-app-bucket-prod`
- C) `terraform output -raw` returns JSON; the standard command returns plain text
- D) `terraform output -raw` strips all characters except alphanumerics; standard returns the full value

### Question 34 — console Expression Evaluation

**Difficulty**: Medium
**Answer Type**: one
**Topic**: What terraform console returns when evaluating a built-in function

**Question**:
An engineer opens `terraform console` and types:

```
length(["web", "api", "db"])
```

What does the console return?

- A) `["web", "api", "db"]` — the console echoes the input unchanged
- B) `3`
- C) `error: function "length" requires a map type`
- D) The console opens a file browser to select a `.tf` file to evaluate

### Question 35 — validate Misses Live Cloud Resources

**Difficulty**: Medium
**Answer Type**: many
**Topic**: What terraform validate does and does not catch

**Question**:
A configuration references `ami = "ami-0abc12345"`, which does not exist in the target AWS region. It also has a variable reference `var.instance_count` that is not declared in any `variables.tf`. `terraform validate` is run. Which TWO statements are correct? (Select two.)

- A) Terraform validate catches the undefined `var.instance_count` reference and reports an error
- B) Terraform validate catches the invalid AMI ID and reports an error
- C) Terraform validate does not check whether the AMI ID exists in AWS — that error only surfaces during plan or apply
- D) Terraform validate requires AWS credentials to verify any `ami` attribute

### Question 36 — destroy -target Scope

**Difficulty**: Medium
**Answer Type**: one
**Topic**: What happens when terraform destroy -target targets a resource with dependents

**Question**:
A configuration has a VPC (`aws_vpc.main`) and an EC2 instance (`aws_instance.web`) that depends on the VPC. An engineer runs `terraform destroy -target=aws_vpc.main`. What does Terraform propose?

- A) Terraform destroys only the VPC; the EC2 instance is left running unaffected
- B) Terraform destroys the EC2 instance first (dependent), then the VPC (dependency) to maintain correct ordering
- C) Terraform returns an error because you cannot target a resource that other resources depend on
- D) Terraform destroys the VPC immediately without considering any dependencies

### Question 37 — Skipping init When Changing Backend

**Difficulty**: Hard
**Answer Type**: one
**Topic**: What happens when the backend changes but terraform init is not re-run

**Question**:
An engineer changes the `backend` block in the `terraform {}` configuration from local to an S3 remote backend. Without running `terraform init`, the engineer runs `terraform plan`. What happens?

- A) Terraform detects the backend change automatically and migrates state during `terraform plan`
- B) Terraform returns an error indicating that the backend configuration has changed and `terraform init` must be run
- C) Terraform runs the plan using the new S3 backend silently — no init is needed for backend changes
- D) Terraform runs the plan using the old local backend and ignores the new backend block until the next full init

### Question 38 — fmt -diff Behaviour

**Difficulty**: Hard
**Answer Type**: many
**Topic**: What terraform fmt -diff does versus terraform fmt -check

**Question**:
An engineer runs `terraform fmt -diff` on a directory containing two `.tf` files, one of which has incorrect indentation. Which TWO statements correctly describe the outcome? (Select two.)

- A) The command outputs a unified diff showing exactly what changed in the incorrectly formatted file
- B) The command rewrites the incorrectly formatted file to canonical style
- C) The command does not modify any files — it only shows what would change, like a dry run
- D) The command exits with code 1 to signal that formatting errors were found

### Question 39 — Attribute Reference Ordering

**Difficulty**: Easy
**Answer Type**: one
**Topic**: What Terraform does when a resource references another resource's attribute

**Question**:
A configuration contains the following two resources:

```hcl
resource "aws_vpc" "main" {
  cidr_block = "10.0.0.0/16"
}

resource "aws_subnet" "public" {
  vpc_id     = aws_vpc.main.id
  cidr_block = "10.0.1.0/24"
}
```

`terraform apply` is run. In what order does Terraform create these resources, and why?

- A) Both resources are created concurrently because Terraform always maximises parallelism
- B) `aws_subnet.public` is created first because it is declared last in the file
- C) `aws_vpc.main` is created first because `aws_subnet.public` references its `id` attribute, creating an implicit dependency
- D) The order is undefined; Terraform randomises creation order for performance

### Question 40 — var.* Reference Between Resources

**Difficulty**: Easy
**Answer Type**: one
**Topic**: Whether a shared variable reference creates a dependency between resources

**Question**:
Two resource blocks both use `var.region` in their configurations:

```hcl
resource "aws_instance" "web" {
  ami           = "ami-0abc123"
  instance_type = "t3.micro"
  availability_zone = var.region
}

resource "aws_s3_bucket" "logs" {
  bucket = "logs-${var.region}"
}
```

Does Terraform create a dependency between `aws_instance.web` and `aws_s3_bucket.logs`? What happens during apply?

- A) Yes — sharing `var.region` creates an implicit dependency; Terraform creates `aws_instance.web` before `aws_s3_bucket.logs`
- B) No — `var.*` references do not create dependency edges; Terraform creates both resources in parallel
- C) Yes — all resources sharing any common value are always serialised
- D) No — but Terraform still creates them sequentially to avoid API rate limits

### Question 41 — Data Source Read Timing

**Difficulty**: Easy
**Answer Type**: one
**Topic**: When a data source is read relative to plan and apply phases

**Question**:
A data source is declared as:

```hcl
data "aws_ami" "ubuntu" {
  most_recent = true
  owners      = ["099720109477"]
}

resource "aws_instance" "web" {
  ami           = data.aws_ami.ubuntu.id
  instance_type = "t3.micro"
}
```

When does Terraform read the data source and retrieve the AMI ID?

- A) When `terraform init` runs — data sources are resolved during initialisation
- B) During `terraform plan` — Terraform queries the provider API to fetch the AMI ID before generating the execution plan
- C) Only after `aws_instance.web` is created — the data source is read at the end of apply
- D) Never — data sources only use values already present in state

### Question 42 — prevent_destroy Blocks a Destroy Plan

**Difficulty**: Medium
**Answer Type**: one
**Topic**: What happens when terraform destroy runs against a resource with prevent_destroy = true

**Question**:
A production RDS instance is declared with:

```hcl
resource "aws_db_instance" "prod" {
  # ... config
  lifecycle {
    prevent_destroy = true
  }
}
```

An engineer runs `terraform destroy`. What happens?

- A) Terraform destroys the database after displaying an extra confirmation prompt
- B) Terraform destroys all other resources but skips `aws_db_instance.prod` without error
- C) Terraform returns an error during planning and refuses to generate a destroy plan for that resource
- D) Terraform creates a snapshot of the database before proceeding with the destroy

### Question 43 — ignore_changes and Subsequent Drift

**Difficulty**: Medium
**Answer Type**: one
**Topic**: What terraform plan reports when a listed attribute has drifted with ignore_changes set

**Question**:
An EC2 instance is declared with:

```hcl
resource "aws_instance" "web" {
  ami           = "ami-0abc123"
  instance_type = "t3.micro"
  tags          = { Name = "web" }

  lifecycle {
    ignore_changes = [tags]
  }
}
```

An administrator manually adds a tag `Owner = "ops"` via the AWS console. `terraform plan` is run. What does Terraform report regarding the tags?

- A) Terraform proposes removing `Owner = "ops"` to revert to the declared tag set
- B) Terraform reports no changes to the `tags` attribute — drift on `tags` is ignored
- C) Terraform returns an error because `ignore_changes` cannot be used with the `tags` attribute
- D) Terraform updates the state file to include `Owner = "ops"` and reports the config as out of date

### Question 44 — replace_triggered_by on Launch Template Change

**Difficulty**: Medium
**Answer Type**: one
**Topic**: What happens to the dependent resource when replace_triggered_by fires

**Question**:
An Auto Scaling Group is configured with:

```hcl
resource "aws_autoscaling_group" "web" {
  # ... config

  lifecycle {
    replace_triggered_by = [aws_launch_template.web]
  }
}
```

The `aws_launch_template.web` resource is updated in the configuration (e.g., the AMI ID changes). `terraform apply` is run. What happens to `aws_autoscaling_group.web`?

- A) Terraform updates `aws_autoscaling_group.web` in-place without destroying it
- B) Terraform destroys and recreates `aws_autoscaling_group.web`, even if its own configuration has not changed
- C) Terraform ignores the launch template change until `aws_autoscaling_group.web` is explicitly updated
- D) Terraform returns an error because `replace_triggered_by` requires both resources to be in the same module

### Question 45 — moved Block Prevents Destroy and Recreate

**Difficulty**: Medium
**Answer Type**: one
**Topic**: What happens when a moved block is used to rename a resource

**Question**:
A running EC2 instance is declared as `resource "aws_instance" "app"`. An engineer renames it to `resource "aws_instance" "web"` in the configuration and adds:

```hcl
moved {
  from = aws_instance.app
  to   = aws_instance.web
}
```

`terraform apply` is run. What happens to the EC2 instance?

- A) The EC2 instance is destroyed and a new one is created with the name `web`
- B) The state file is updated to track the instance as `aws_instance.web`; the running EC2 instance is not touched
- C) Terraform returns an error because renaming resources requires manual state manipulation
- D) Terraform creates a second EC2 instance named `web` and leaves the original `app` instance running

### Question 46 — depends_on Reduces Parallelism

**Difficulty**: Medium
**Answer Type**: one
**Topic**: How explicit depends_on affects apply parallelism

**Question**:
A configuration has 10 independent EC2 instances (no attribute references between them) and Terraform's default parallelism of 10. An engineer adds `depends_on = [aws_instance.web_0]` to `aws_instance.web_1` through `aws_instance.web_9`. `terraform apply` is run. What is the behaviour?

- A) All 10 instances are still created concurrently because `depends_on` is only advisory
- B) Only `aws_instance.web_0` is created first; the remaining 9 instances wait for it to complete before being created
- C) Terraform returns an error because `depends_on` is not permitted between resources of the same type
- D) The instances are created two at a time because `depends_on` halves the default parallelism

### Question 47 — Data Source Dependent on Computed Value

**Difficulty**: Medium
**Answer Type**: one
**Topic**: When a data source is deferred to apply because it depends on an unknown value

**Question**:
A data source depends on the ID of a resource that does not yet exist:

```hcl
resource "aws_vpc" "main" {
  cidr_block = "10.0.0.0/16"
}

data "aws_subnets" "available" {
  filter {
    name   = "vpc-id"
    values = [aws_vpc.main.id]
  }
}
```

`terraform plan` is run for the first time. When does Terraform read the `data.aws_subnets.available` data source?

- A) During `terraform plan` — Terraform reads all data sources before generating the plan
- B) During `terraform apply` — after `aws_vpc.main` is created and its `id` is known
- C) During `terraform init` — data sources with filters are resolved at initialisation
- D) Terraform never reads this data source because the VPC does not exist yet

### Question 48 — removed Block with destroy = false

**Difficulty**: Medium
**Answer Type**: many
**Topic**: What happens when a removed block with destroy = false is applied

**Question**:
An engineer adds the following block to a configuration that previously managed an EC2 instance:

```hcl
removed {
  from = aws_instance.legacy

  lifecycle {
    destroy = false
  }
}
```

`terraform apply` is run. Which TWO statements correctly describe the outcome? (Select two.)

- A) The EC2 instance is deleted from AWS
- B) The EC2 instance continues to run in AWS unaffected
- C) Terraform removes `aws_instance.legacy` from the state file so it is no longer managed
- D) Future `terraform plan` runs will propose recreating `aws_instance.legacy` from the configuration

### Question 49 — create_before_destroy with Immutable Attribute

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Plan output when an immutable attribute changes with create_before_destroy set

**Question**:
An EC2 instance is declared with `create_before_destroy = true`. The `ami` attribute (which forces replacement when changed) is updated in the configuration. `terraform plan` is run. What does the plan output show for this resource?

- A) `~ aws_instance.web` — the instance will be updated in-place
- B) `-/+ aws_instance.web` — the instance will be replaced, with the new instance created before the old one is destroyed
- C) `+ aws_instance.web` — a second instance will be added; the original is not touched
- D) The plan returns an error because changing `ami` requires setting `prevent_destroy = false` first

### Question 50 — apply -parallelism=1 Effect

**Difficulty**: Hard
**Answer Type**: one
**Topic**: What terraform apply -parallelism=1 does to resource creation order

**Question**:
A configuration creates 8 independent resources (no dependencies between them). An engineer runs `terraform apply -parallelism=1`. What is the behaviour compared to the default?

- A) Terraform creates all 8 resources in a single API call to improve efficiency
- B) Terraform creates one resource at a time sequentially, rather than up to 10 concurrently — the apply takes longer but reduces API concurrency
- C) Terraform creates 2 resources at a time instead of the default 10
- D) The command fails because `-parallelism=1` is not a valid value

### Question 51 — depends_on on a Data Source

**Difficulty**: Hard
**Answer Type**: many
**Topic**: Behaviour when depends_on is added to a data source

**Question**:
A data source has `depends_on = [aws_iam_role_policy.app]` added to it:

```hcl
data "aws_s3_objects" "uploads" {
  bucket = "my-app-uploads"

  depends_on = [aws_iam_role_policy.app]
}
```

Which TWO statements correctly describe the impact of this `depends_on`? (Select two.)

- A) The data source will not be read during `terraform plan` — it is deferred to apply after `aws_iam_role_policy.app` is applied
- B) The data source will still be read during plan, but only after `aws_iam_role_policy.app` is created
- C) Adding `depends_on` to a data source forces it to be read during apply instead of plan, even if no computed values are involved
- D) The `depends_on` on a data source has no effect — data sources always read during plan regardless

### Question 52 — -var Flag Overrides auto.tfvars

**Difficulty**: Easy
**Answer Type**: one
**Topic**: What value Terraform uses when the same variable is set in auto.tfvars and via -var

**Question**:
A variable `instance_type` has `default = "t3.micro"` in its declaration. A file named `prod.auto.tfvars` sets `instance_type = "t3.large"`. The engineer runs:

```bash
terraform apply -var="instance_type=t3.xlarge"
```

What value does Terraform use for `instance_type`?

- A) `"t3.micro"` — the `default` in the variable block is the authoritative source
- B) `"t3.large"` — `.auto.tfvars` files override CLI flags
- C) `"t3.xlarge"` — the `-var` flag has the highest precedence and overrides all other sources
- D) Terraform returns an error because the variable is set in multiple places

### Question 53 — sensitive = true on an Output

**Difficulty**: Easy
**Answer Type**: one
**Topic**: What terraform output displays for a sensitive output

**Question**:
An output is declared as:

```hcl
output "db_password" {
  value     = aws_db_instance.main.password
  sensitive = true
}
```

An engineer runs `terraform output db_password`. What does the terminal display?

- A) The actual database password in plaintext
- B) `(sensitive value)` — the value is redacted in the terminal
- C) An error: sensitive outputs cannot be queried directly
- D) An empty string — sensitive outputs always return `""`

### Question 54 — toset() Removes Duplicates Before for_each

**Difficulty**: Easy
**Answer Type**: one
**Topic**: How many resource instances for_each creates when toset() is applied to a list with duplicates

**Question**:
A resource is declared as:

```hcl
resource "aws_iam_user" "team" {
  for_each = toset(["alice", "bob", "alice", "carol"])
  name     = each.key
}
```

How many IAM user resources does Terraform create?

- A) 4 — Terraform creates one resource per list element, including duplicates
- B) 3 — `toset()` removes the duplicate `"alice"`, leaving `{"alice", "bob", "carol"}`
- C) 1 — `for_each` only creates the first unique value
- D) Terraform returns an error because the input list contains duplicate values

### Question 55 — for_each Map Creates Named Addresses

**Difficulty**: Medium
**Answer Type**: one
**Topic**: What resource instance addresses are created in state when for_each uses a map

**Question**:
A resource is declared as:

```hcl
variable "servers" {
  default = {
    web = "t3.micro"
    app = "t3.small"
  }
}

resource "aws_instance" "servers" {
  for_each      = var.servers
  ami           = "ami-0abc123"
  instance_type = each.value
}
```

After `terraform apply`, which resource addresses appear in Terraform state?

- A) `aws_instance.servers[0]` and `aws_instance.servers[1]`
- B) `aws_instance.servers["web"]` and `aws_instance.servers["app"]`
- C) `aws_instance.servers.web` and `aws_instance.servers.app`
- D) `aws_instance.servers` — `for_each` creates a single resource with multiple attributes

### Question 56 — count Renumbers on Middle Removal

**Difficulty**: Medium
**Answer Type**: one
**Topic**: What terraform plan shows when the middle element is removed from a count list

**Question**:
A resource is created with `count = length(var.names)` where `var.names = ["alice", "bob", "carol"]`. The index assignments are: `[0]=alice`, `[1]=bob`, `[2]=carol`. The engineer removes `"bob"` from the middle, making `var.names = ["alice", "carol"]`. What does `terraform plan` propose?

- A) Destroy only `aws_iam_user.users[1]` (bob) — the other two are untouched
- B) Destroy `aws_iam_user.users[1]` (bob) and update `aws_iam_user.users[2]` to use `"carol"` shifted to index 1 — effectively destroying and recreating carol's resource
- C) Destroy all three instances and recreate only two
- D) Terraform returns an error because `count` does not allow removing elements

### Question 57 — dynamic Block Generates Blocks per Collection Element

**Difficulty**: Medium
**Answer Type**: one
**Topic**: How many nested blocks a dynamic block generates from a 3-element list

**Question**:
A security group resource uses a `dynamic` block:

```hcl
variable "ports" {
  default = [80, 443, 8080]
}

resource "aws_security_group" "web" {
  name = "web-sg"

  dynamic "ingress" {
    for_each = var.ports
    content {
      from_port   = ingress.value
      to_port     = ingress.value
      protocol    = "tcp"
      cidr_blocks = ["0.0.0.0/0"]
    }
  }
}
```

How many `ingress` blocks does Terraform generate for this security group?

- A) 1 — `dynamic` blocks always produce a single merged block
- B) 2 — `dynamic` only iterates over the first two elements
- C) 3 — one `ingress` block is generated per element in `var.ports`
- D) Terraform returns an error because `dynamic` blocks cannot iterate over a list of numbers

### Question 58 — merge() Later Key Wins

**Difficulty**: Medium
**Answer Type**: one
**Topic**: What value merge() produces when both maps share the same key

**Question**:
A local is defined as:

```hcl
locals {
  defaults = { environment = "dev", region = "us-east-1", debug = false }
  overrides = { environment = "production", debug = true }
  config = merge(local.defaults, local.overrides)
}
```

What is the value of `local.config`?

- A) `{ environment = "dev", region = "us-east-1", debug = false }` — the first map's values are preserved
- B) `{ environment = "production", region = "us-east-1", debug = true }` — keys from `overrides` win; unique keys from `defaults` are kept
- C) Terraform returns an error because `environment` exists in both maps
- D) `{ environment = "production", region = "us-east-1", debug = false }` — `debug` is not overridden because it is a boolean

### Question 59 — Conditional Expression Selects Value

**Difficulty**: Medium
**Answer Type**: one
**Topic**: What value a conditional expression returns based on a variable

**Question**:
A resource is declared with:

```hcl
variable "environment" {
  default = "staging"
}

resource "aws_instance" "app" {
  ami           = "ami-0abc123"
  instance_type = var.environment == "production" ? "t3.large" : "t3.micro"
}
```

`terraform apply` is run without any variable overrides. What `instance_type` is used?

- A) `"t3.large"` — because `environment` has a value and the condition is evaluated
- B) `"t3.micro"` — because `var.environment` is `"staging"`, which does not equal `"production"`
- C) Terraform returns an error because conditional expressions are not allowed in resource arguments
- D) `null` — because `var.environment` has not been explicitly set by the user

### Question 60 — try() Returns Fallback When Key Missing

**Difficulty**: Medium
**Answer Type**: one
**Topic**: What try() returns when the primary expression produces an error

**Question**:
A local is defined as:

```hcl
variable "settings" {
  default = { timeout = 30 }
}

locals {
  retry_count = try(var.settings["retry_count"], 3)
}
```

What is the value of `local.retry_count`?

- A) `null` — `try()` returns null when a key is missing
- B) An error — accessing a missing map key in Terraform always raises a fatal error
- C) `3` — `try()` evaluates `var.settings["retry_count"]`, gets an error because the key doesn't exist, and returns the fallback value `3`
- D) `0` — Terraform defaults numeric values to `0` when a key is not found

### Question 61 — for Map Comprehension Result

**Difficulty**: Medium
**Answer Type**: many
**Topic**: What a for expression with map output produces

**Question**:
A local is defined as:

```hcl
locals {
  sizes = { web = "t3.micro", app = "t3.small", db = "t3.medium" }
  labels = { for k, v in local.sizes : k => "instance-type: ${v}" }
}
```

Which TWO statements correctly describe `local.labels`? (Select two.)

- A) `local.labels` is a list of strings
- B) `local.labels` is a map where each key matches the original key and each value is a formatted string
- C) `local.labels["web"]` equals `"instance-type: t3.micro"`
- D) `local.labels` contains only one entry because `for` expressions return a single value

### Question 62 — nullable = false with No Value Provided

**Difficulty**: Medium
**Answer Type**: one
**Topic**: What happens when nullable = false is set and no value is provided for the variable

**Question**:
A variable is declared as:

```hcl
variable "app_name" {
  type     = string
  nullable = false
}
```

No `default` is provided, no `.tfvars` file sets the variable, and no `-var` flag is passed. `terraform plan` is run. What happens?

- A) Terraform uses `""` (empty string) as the value because `nullable = false` implies a non-null default
- B) Terraform prompts the user interactively for a value
- C) Terraform returns an error because the variable has no default and no value was provided, making it required
- D) Terraform automatically sets the value to `null` because no source provides a value

### Question 63 — element() Wraps Around the List

**Difficulty**: Hard
**Answer Type**: one
**Topic**: What element() returns when the index exceeds the list length

**Question**:
The following expression is evaluated in `terraform console`:

```
element(["a", "b", "c"], 4)
```

What does it return?

- A) An error — the index `4` is out of bounds for a 3-element list
- B) `null` — out-of-bounds indices return null in Terraform
- C) `"a"` — `element()` wraps around using modulo, so index 4 mod 3 = 1... wait, 4 mod 3 = 1 → `"b"`
- D) `"b"` — `element()` wraps around the list using modulo arithmetic: `4 mod 3 = 1`, returning the element at index 1

### Question 64 — Sensitive Variable Value in Plan Output

**Difficulty**: Hard
**Answer Type**: many
**Topic**: Where a sensitive variable's value is and is not visible

**Question**:
A variable and resource are declared as:

```hcl
variable "api_key" {
  type      = string
  sensitive = true
}

resource "aws_ssm_parameter" "key" {
  name  = "/app/api_key"
  type  = "SecureString"
  value = var.api_key
}
```

`terraform apply` is run. Which TWO statements correctly describe where `var.api_key`'s value appears? (Select two.)

- A) The value is redacted as `(sensitive value)` in the `terraform apply` terminal output
- B) The value is encrypted automatically before being written to the state file
- C) The value is stored in plaintext in `terraform.tfstate` under the resource's attributes
- D) The value is permanently deleted after apply and cannot be retrieved from state

### Question 65 — Validation Failure Halts Plan Before Infrastructure

**Difficulty**: Easy
**Answer Type**: one
**Topic**: What happens when a variable validation condition fails during terraform plan

**Question**:
A variable is declared with a validation block:

```hcl
variable "environment" {
  type    = string

  validation {
    condition     = contains(["dev", "staging", "production"], var.environment)
    error_message = "environment must be one of: dev, staging, production."
  }
}
```

An engineer runs `terraform apply -var="environment=test"`. What happens?

- A) The apply proceeds but logs a warning about the unrecognised value
- B) Terraform evaluates the plan and fails only when the invalid value reaches a resource argument
- C) Terraform fails before generating any plan and displays: "environment must be one of: dev, staging, production."
- D) The apply succeeds because `"test"` satisfies the `string` type constraint

### Question 66 — Failing check Block Assertion Does Not Block Apply

**Difficulty**: Easy
**Answer Type**: one
**Topic**: What happens to terraform apply when a check block assertion evaluates to false

**Question**:
A `check` block asserts that a load balancer's HTTP health endpoint returns status code 200:

```hcl
check "lb_health" {
  data "http" "endpoint" {
    url = "https://${aws_lb.web.dns_name}/health"
  }

  assert {
    condition     = data.http.endpoint.status_code == 200
    error_message = "Health check returned ${data.http.endpoint.status_code}, expected 200."
  }
}
```

During `terraform apply`, all resources are created successfully but the health endpoint returns `503`. What is the exit behaviour of the apply?

- A) The apply exits with a non-zero status code because the `check` assertion failed
- B) Terraform rolls back the resources created during this apply
- C) Terraform displays a warning about the failed assertion and the apply exits successfully
- D) The `aws_lb.web` resource is marked as tainted for replacement on the next run

### Question 67 — Precondition Prevents Resource Modification

**Difficulty**: Medium
**Answer Type**: one
**Topic**: State of the resource when a precondition fails during apply

**Question**:
A resource has a `precondition` in its `lifecycle` block:

```hcl
resource "aws_instance" "web" {
  ami           = data.aws_ami.ubuntu.id
  instance_type = var.instance_type

  lifecycle {
    precondition {
      condition     = data.aws_ami.ubuntu.architecture == "x86_64"
      error_message = "The selected AMI must be x86_64 architecture."
    }
  }
}
```

During `terraform apply`, the AMI is resolved as `arm64`. Has the `aws_instance` been created or modified in AWS when the error is reported?

- A) Yes — Terraform creates the instance first and then evaluates the precondition, marking it failed
- B) No — the precondition is evaluated before the resource is changed; no instance is created or modified
- C) The instance is partially provisioned — Terraform starts the API call and rolls back on failure
- D) The instance is created but Terraform removes it from state because the precondition failed

### Question 68 — Postcondition Failure: Resource Exists in Cloud and State

**Difficulty**: Medium
**Answer Type**: many
**Topic**: What is true about a resource after its postcondition fails

**Question**:
An `aws_instance` resource has a `postcondition` checking that a public IP was assigned:

```hcl
lifecycle {
  postcondition {
    condition     = self.public_ip != null
    error_message = "Instance must have a public IP address."
  }
}
```

The instance is provisioned in a subnet without auto-assign public IP, so `self.public_ip` is `null`. Which TWO statements are true after `terraform apply` runs? (Select two.)

- A) The `aws_instance` does not exist in AWS — Terraform rolls back resource creation when a postcondition fails
- B) The `aws_instance` exists in AWS with its actual attributes
- C) The `aws_instance` IS recorded in `terraform.tfstate`
- D) The `aws_instance` is NOT recorded in `terraform.tfstate` because the postcondition invalidated the create

### Question 69 — Sensitive Variable Redacted in Plan Output

**Difficulty**: Medium
**Answer Type**: one
**Topic**: What terraform plan displays for a sensitive variable value in a resource argument

**Question**:
A variable and resource are declared as:

```hcl
variable "db_password" {
  type      = string
  sensitive = true
}

resource "aws_db_instance" "main" {
  username = "admin"
  password = var.db_password
}
```

`terraform plan` is run. What does the plan output show for the `password` argument of `aws_db_instance.main`?

- A) The actual password value in plaintext
- B) `(known after apply)` — sensitive values are deferred to apply time
- C) `(sensitive value)` — the value is redacted in the plan display
- D) The `password` field is omitted entirely from the plan output

### Question 70 — Validation Condition References a Data Source

**Difficulty**: Medium
**Answer Type**: one
**Topic**: What happens when a validation condition references a data source instead of var.<name>

**Question**:
An engineer writes a validation block that references a data source:

```hcl
variable "availability_zone" {
  type = string

  validation {
    condition     = contains(data.aws_availability_zones.available.names, var.availability_zone)
    error_message = "Must be a valid availability zone."
  }
}
```

What happens when `terraform plan` is run with this configuration?

- A) Terraform reads the data source first and then evaluates the validation condition successfully
- B) Terraform raises an error because validation conditions can only reference `var.<variable_name>`
- C) The validation is silently skipped because the data source dependency cannot be resolved at variable evaluation time
- D) Terraform prompts for the data source to be initialised before validation can proceed

### Question 71 — Scoped Data Source in check Block Errors

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Effect on terraform apply when a scoped data source inside a check block fails

**Question**:
A `check` block contains a scoped `data "http"` source that makes an HTTP request to a monitoring endpoint. During `terraform apply`, the HTTP request fails with a connection timeout. How does this affect the rest of the apply?

- A) The entire apply is aborted because the `check` block's data source returned an error
- B) Terraform marks the check as failed with a warning and continues applying all other resources normally
- C) The data source failure is silently ignored and the `check` block assertion is treated as passing
- D) Terraform retries the HTTP request three times before failing the entire apply

### Question 72 — Consuming Sensitive Output Without Marking It Sensitive

**Difficulty**: Medium
**Answer Type**: one
**Topic**: What happens when a sensitive module output is referenced in an unmarked output block

**Question**:
A child module exposes a sensitive output:

```hcl
# modules/database/outputs.tf
output "db_password" {
  value     = aws_db_instance.main.password
  sensitive = true
}
```

The root module references this output in its own output block **without** marking it sensitive:

```hcl
# root outputs.tf
output "exposed_password" {
  value = module.database.db_password
}
```

What happens when `terraform plan` runs?

- A) Terraform automatically propagates the `sensitive` flag and redacts the value without requiring any change
- B) Terraform raises an error requiring `exposed_password` to also be marked `sensitive = true`
- C) The plan succeeds with a deprecation warning advising the team to add `sensitive = true`
- D) The value is shown in plaintext in the plan output because the root module does not inherit the sensitive flag

### Question 73 — check Block Runs During terraform plan

**Difficulty**: Medium
**Answer Type**: one
**Topic**: When check block assertions are evaluated — plan, apply, or both

**Question**:
A configuration contains a `check` block with an `assert` that evaluates to `false` at the time `terraform plan` is run. What does the plan output include?

- A) The plan fails with an error and no proposed changes are shown — the assertion must pass before planning
- B) The plan succeeds; the assertion failure is displayed as a warning alongside the proposed infrastructure changes
- C) The plan output omits the `check` block results — assertions are only evaluated during `terraform apply`
- D) Terraform skips `check` block evaluation during plan if there are pending infrastructure changes

### Question 74 — Interactive Prompt Then Validation Evaluation

**Difficulty**: Medium
**Answer Type**: many
**Topic**: Sequence of events when a variable has no default and requires interactive input

**Question**:
A required variable has a validation block but no `default`:

```hcl
variable "environment" {
  type = string

  validation {
    condition     = contains(["dev", "staging", "production"], var.environment)
    error_message = "environment must be one of: dev, staging, production."
  }
}
```

No `.tfvars` file, environment variable, or `-var` flag provides a value. `terraform plan` is run interactively. Which TWO statements correctly describe what Terraform does? (Select two.)

- A) Terraform prompts the user interactively at the terminal to enter a value for `environment`
- B) Terraform fails immediately with the validation error because no value was provided
- C) After the user enters a value, the `validation` condition is evaluated against it
- D) The validation block is permanently skipped when the value comes from an interactive prompt

### Question 75 — Precondition Passes, Postcondition Fails

**Difficulty**: Hard
**Answer Type**: one
**Topic**: Final state of a resource after precondition passes and postcondition fails

**Question**:
A resource has both a `precondition` and a `postcondition` in its `lifecycle` block. During `terraform apply`:
1. The `precondition` evaluates to `true` — the resource creation proceeds
2. The resource is successfully created in AWS
3. The `postcondition` evaluates to `false` — the condition is not met

What is the final state of the resource after apply completes?

- A) The resource is destroyed in AWS — Terraform automatically cleans up resources that fail postconditions
- B) The resource exists in AWS and IS recorded in `terraform.tfstate`; the apply exits with a failure status
- C) The resource exists in AWS but is NOT recorded in `terraform.tfstate` — the postcondition failure marks it as unmanaged
- D) The resource is recorded in `terraform.tfstate` as `tainted` so it will be replaced on the next plan

### Question 76 — Mixed Sensitive and Non-Sensitive Outputs via terraform output

**Difficulty**: Hard
**Answer Type**: many
**Topic**: What terraform output (no arguments) shows for sensitive vs non-sensitive outputs

**Question**:
A configuration defines two outputs:

```hcl
output "instance_id" {
  value = aws_instance.web.id
}

output "db_password" {
  value     = aws_db_instance.main.password
  sensitive = true
}
```

An engineer runs `terraform output` (with no arguments) after apply. Which TWO statements correctly describe what is displayed? (Select two.)

- A) Both `instance_id` and `db_password` display their actual values
- B) `instance_id` is shown with its actual value
- C) `db_password` is shown as `(sensitive value)` rather than the actual password
- D) All outputs are hidden — `terraform output` without arguments only lists output names, not values

### Question 77 — New Module Source Added Without terraform init

**Difficulty**: Easy
**Answer Type**: one
**Topic**: What happens when a new module source is added but `terraform init` has not been re-run

**Question**:
An engineer adds this block to an existing configuration for the first time:

```hcl
module "networking" {
  source   = "./modules/networking"
  vpc_cidr = "10.0.0.0/16"
}
```

The `./modules/networking` directory exists but `terraform init` has not been re-run since the block was added. What happens when `terraform plan` is run?

- A) The plan succeeds and proposes all resources defined inside the networking module
- B) Terraform raises an error indicating the module is not installed and `terraform init` must be run
- C) The module resources are silently skipped without error until `terraform init` is next executed
- D) Terraform automatically downloads and installs the local module during the plan operation

### Question 78 — terraform state rm Effect on Next Plan

**Difficulty**: Easy
**Answer Type**: one
**Topic**: What `terraform plan` shows immediately after `terraform state rm` removes a managed resource

**Question**:
An engineer runs:

```bash
terraform state rm aws_s3_bucket.assets
```

The `aws_s3_bucket.assets` resource block still exists in `main.tf` and the actual S3 bucket still exists in AWS. What does the next `terraform plan` propose?

- A) No changes — the resource was removed from tracking, so Terraform ignores it in future plans
- B) Destroy `aws_s3_bucket.assets` — since it is absent from state, Terraform treats it as unmanaged drift
- C) Create `aws_s3_bucket.assets` — since it is absent from state, Terraform treats it as a new resource to provision
- D) An error: Terraform refuses to plan when the state and configuration are out of sync

### Question 79 — Accessing a Child Module Output

**Difficulty**: Easy
**Answer Type**: one
**Topic**: The address used in the root module to reference a specific output from a child module

**Question**:
A child module is instantiated in the root module as:

```hcl
module "database" {
  source = "./modules/database"
}
```

The child module exports:

```hcl
output "connection_string" {
  value = aws_db_instance.main.endpoint
}
```

How does the root module reference the `connection_string` output?

- A) `var.database.connection_string`
- B) `module.database.connection_string`
- C) `database.outputs.connection_string`
- D) `output.database.connection_string`

### Question 80 — Passing Undeclared Input to Child Module

**Difficulty**: Medium
**Answer Type**: one
**Topic**: What happens at plan time when the root module passes an argument the child module never declared

**Question**:
A root module calls a child module:

```hcl
module "compute" {
  source      = "./modules/compute"
  ami         = "ami-0abc123"
  environment = var.environment
  debug_mode  = true   # not declared in ./modules/compute/variables.tf
}
```

The child module has no `variable "debug_mode"` block. What happens when `terraform plan` is run?

- A) `debug_mode` is silently ignored — unknown inputs are discarded without error
- B) Terraform raises an error: an argument named `debug_mode` is not expected in this module
- C) The value is available inside the child module as an implicit local: `local.debug_mode`
- D) `terraform plan` succeeds but emits a warning advising the team to declare the variable

### Question 81 — version Argument on a Local Module Source

**Difficulty**: Medium
**Answer Type**: one
**Topic**: What terraform init does when `version` is specified alongside a local path module source

**Question**:
A module block is written as:

```hcl
module "networking" {
  source  = "./modules/networking"
  version = "~> 1.0"
}
```

What happens when `terraform init` is run?

- A) The `version` constraint is silently ignored because local paths have no version registry
- B) Terraform raises an error: `version` is not valid for local module sources
- C) Terraform checks the `versions.tf` file inside `./modules/networking/` to verify the constraint is satisfied
- D) Terraform creates a `MODULE_VERSION` file in the module directory to record the pinned version

### Question 82 — Backend Changed Without Re-Running terraform init

**Difficulty**: Medium
**Answer Type**: one
**Topic**: What happens when the backend block is changed but `terraform init` has not been re-run

**Question**:
A team edits `main.tf` to switch from a `local` backend to an `s3` backend. Without re-running `terraform init`, an engineer immediately runs `terraform plan`. What happens?

- A) `terraform plan` detects the backend change, automatically reconfigures to S3, and proceeds with planning
- B) `terraform plan` reads state from the old local `terraform.tfstate` file and displays a plan based on that state
- C) Terraform raises an error: the backend configuration has changed and `terraform init` must be run to apply it
- D) Terraform raises an authentication error because the S3 credentials have not been initialised

### Question 83 — terraform state mv Followed by HCL Rename

**Difficulty**: Medium
**Answer Type**: one
**Topic**: What terraform plan shows after state mv and a matching HCL resource label rename

**Question**:
An engineer executes:

```bash
terraform state mv aws_instance.web aws_instance.web_server
```

The HCL configuration is also updated to rename the resource block from `aws_instance "web"` to `aws_instance "web_server"`. What does `terraform plan` propose on the next run?

- A) Destroy `aws_instance.web` and create `aws_instance.web_server` — the rename is treated as a replacement
- B) No changes — the resource exists in state under the new name and the configuration matches
- C) An in-place update — only metadata attributes like `tags.Name` are updated to reflect the rename
- D) An error: `terraform state mv` cannot be used for renames; a `moved` block must be used instead

### Question 84 — terraform apply -refresh-only After Manual Resize

**Difficulty**: Medium
**Answer Type**: many
**Topic**: What `terraform apply -refresh-only` does and does not modify

**Question**:
After an engineer manually resizes an EC2 instance from `t3.micro` to `t3.small` in the AWS Console, a colleague runs `terraform apply -refresh-only`. Which TWO statements correctly describe what this command does? (Select two.)

- A) The EC2 instance is resized back to `t3.micro` to match the `instance_type` in the Terraform configuration
- B) The Terraform state file is updated to record `instance_type = "t3.small"` to match the actual cloud state
- C) No cloud resources are created, modified, or destroyed
- D) The `terraform.tfvars` file is updated to set `instance_type = "t3.small"`

### Question 85 — S3 Backend Without DynamoDB Locking During Concurrent Applies

**Difficulty**: Medium
**Answer Type**: one
**Topic**: What risk exists when using an S3 backend without a DynamoDB lock table configured

**Question**:
Two engineers share an S3 backend for state storage, but the backend block does not include a `dynamodb_table` argument. Both engineers run `terraform apply` at exactly the same time against the same workspace. What is the risk?

- A) Terraform automatically queues the second apply to run after the first completes
- B) Both applies succeed without issue because S3 provides native atomic write locking
- C) The state file can become corrupted — without a DynamoDB lock table, nothing prevents both applies from writing state simultaneously
- D) The second apply fails with a 409 Conflict error from S3 because concurrent uploads are rejected

### Question 86 — Root Variable Not Explicitly Passed to Child Module

**Difficulty**: Medium
**Answer Type**: one
**Topic**: What happens when a child module's required variable is not passed in the module block

**Question**:
The root module defines:

```hcl
variable "region" {
  default = "us-east-1"
}
```

The child module `./modules/network` declares:

```hcl
variable "region" {}   # no default
```

The root module calls:

```hcl
module "network" {
  source   = "./modules/network"
  vpc_cidr = "10.0.0.0/16"
  # 'region' is NOT passed here
}
```

What happens during `terraform plan`?

- A) The child module uses `"us-east-1"` — it inherits `var.region` from the root module automatically
- B) Terraform raises an error: the required input variable `region` is not set for module `network`
- C) The child module uses an empty string `""` as the value for `var.region`
- D) Terraform reads the `TF_VAR_region` environment variable and passes it to the child module automatically

### Question 87 — terraform state pull Output

**Difficulty**: Medium
**Answer Type**: many
**Topic**: What `terraform state pull` outputs and how it can be used

**Question**:
An engineer runs `terraform state pull` on a workspace that uses an S3 remote backend. Which TWO statements correctly describe the behaviour? (Select two.)

- A) `terraform state pull` downloads the current remote state and prints it to stdout as a JSON document
- B) `terraform state pull` downloads the current remote state and saves it automatically as `terraform.tfstate` in the working directory
- C) The output can be captured using shell redirection: `terraform state pull > backup.tfstate`
- D) `terraform state pull` acquires a write lock on the state file for the duration of the command

### Question 88 — Leftover Local State After terraform init -migrate-state

**Difficulty**: Hard
**Answer Type**: one
**Topic**: What happens to the old local terraform.tfstate after a successful migration to a remote backend

**Question**:
A team switches from the local backend to an S3 backend and runs `terraform init -migrate-state`. The migration completes successfully. What is the status of the old `terraform.tfstate` file in the working directory?

- A) The file is automatically deleted — Terraform removes it to prevent a stale local state from being used accidentally
- B) The file is renamed to `terraform.tfstate.migrated` to indicate it has been superseded by the remote backend
- C) The file remains in the working directory unchanged; Terraform no longer reads from it but does not remove it
- D) The file is moved to `.terraform/state-backup/` by the migration process

### Question 89 — terraform.tfstate.backup After Multiple Applies

**Difficulty**: Hard
**Answer Type**: many
**Topic**: What terraform.tfstate.backup contains after multiple applies and its limitation as a backup mechanism

**Question**:
An engineer runs three consecutive `terraform apply` operations on a local-backend configuration. After all three applies complete, which TWO statements correctly describe `terraform.tfstate.backup`? (Select two.)

- A) `terraform.tfstate.backup` contains state snapshots from all three previous applies — it is a rolling three-entry history
- B) `terraform.tfstate.backup` contains only the state snapshot from immediately before the most recent (third) apply
- C) The content of `terraform.tfstate.backup` at this point represents the state as it existed after the second apply completed
- D) `terraform.tfstate.backup` stores the two most recent snapshots and automatically prunes older ones

### Question 90 — TF_LOG Without TF_LOG_PATH

**Difficulty**: Easy
**Answer Type**: one
**Topic**: Where Terraform writes log output when `TF_LOG` is set but `TF_LOG_PATH` is not

**Question**:
An engineer sets the following before running a command:

```bash
export TF_LOG=TRACE
terraform apply
```

No `TF_LOG_PATH` variable is set. Where does Terraform write the log output?

- A) To a file named `terraform.log` created automatically in the current working directory
- B) To stderr — all log output is written to the standard error stream
- C) To stdout, interleaved with the normal plan and apply output
- D) Logging is disabled when `TF_LOG_PATH` is not configured

### Question 91 — VCS Pull Request Triggers a Run

**Difficulty**: Easy
**Answer Type**: one
**Topic**: Which HCP Terraform run type is automatically triggered when a pull request is opened

**Question**:
A team has connected an HCP Terraform workspace to a GitHub repository. A developer opens a pull request targeting the `main` branch. What does HCP Terraform automatically do?

- A) It queues a plan-and-apply run that immediately applies changes to the workspace
- B) It queues a plan-only run that waits for manual approval before it can be applied
- C) It triggers a speculative plan and posts the result as a status check on the pull request
- D) Nothing happens until the pull request is merged; HCP Terraform only reacts to merge events

### Question 92 — terraform state show Output

**Difficulty**: Easy
**Answer Type**: one
**Topic**: What `terraform state show` outputs for a specific resource

**Question**:
An engineer runs:

```bash
terraform state show aws_instance.web
```

What does this command output?

- A) A JSON document representing the entire state file
- B) The HCL resource block exactly as it appears in the Terraform configuration file
- C) All recorded attributes of the `aws_instance.web` resource as stored in the state file
- D) An execution plan showing what Terraform would change about `aws_instance.web`

### Question 93 — CLI Import When Resource Already in State

**Difficulty**: Medium
**Answer Type**: one
**Topic**: What happens when `terraform import` targets a resource address already tracked in state

**Question**:
A resource `aws_s3_bucket.logs` already exists in the Terraform state file and is actively managed. An engineer runs:

```bash
terraform import aws_s3_bucket.logs existing-log-bucket
```

What happens?

- A) The import succeeds and refreshes the state entry with the latest attributes from the cloud
- B) Terraform raises an error indicating that `aws_s3_bucket.logs` is already managed in state
- C) Terraform creates a second, duplicate state entry for the same cloud resource
- D) The existing state entry is silently overwritten with the newly imported attributes

### Question 94 — import Block With an Invalid Cloud Resource ID

**Difficulty**: Medium
**Answer Type**: one
**Topic**: When Terraform surfaces an error if the `import` block's `id` does not match any real cloud resource

**Question**:
An engineer writes this configuration:

```hcl
import {
  to = aws_instance.app
  id = "i-DOESNOTEXIST"
}

resource "aws_instance" "app" {
  ami           = "ami-0abc123"
  instance_type = "t3.micro"
}
```

The instance ID `i-DOESNOTEXIST` does not correspond to any real EC2 instance. What happens when `terraform plan` is run?

- A) The import is silently skipped and Terraform plans to create a new `aws_instance.app`
- B) The plan succeeds but Terraform logs a warning about the invalid ID
- C) Terraform raises a provider error during the planning phase because the resource with that ID was not found in the cloud
- D) The error only surfaces at `terraform apply` time; the plan phase cannot validate cloud resource IDs

### Question 95 — generate-config-out When Resource Block Already Exists

**Difficulty**: Medium
**Answer Type**: one
**Topic**: What happens when `-generate-config-out` is used but the target resource block already exists

**Question**:
An engineer has this configuration in `main.tf`:

```hcl
import {
  to = aws_vpc.main
  id = "vpc-0abc1234"
}

resource "aws_vpc" "main" {
  cidr_block = "10.0.0.0/16"
}
```

The engineer then runs:

```bash
terraform plan -generate-config-out=generated.tf
```

What happens?

- A) The existing `resource "aws_vpc" "main"` block in `main.tf` is overwritten with the generated version
- B) Terraform raises an error: `-generate-config-out` cannot be used when the resource block already exists in configuration
- C) A second copy of the resource block is written to `generated.tf`, and Terraform warns about the duplication
- D) The `-generate-config-out` flag is silently ignored since a resource block already exists; the plan proceeds normally

### Question 96 — Run Trigger From Upstream Workspace Apply

**Difficulty**: Medium
**Answer Type**: one
**Topic**: What HCP Terraform does to a downstream workspace when an upstream apply completes via a run trigger

**Question**:
Workspace B (`compute`) is configured in HCP Terraform with Workspace A (`networking`) set as a **run trigger** source. Workspace A manages the VPC and subnets that Workspace B depends on. Workspace A's `terraform apply` completes successfully. What does HCP Terraform do next?

- A) Workspace B immediately begins executing without a separate planning phase
- B) Workspace B is automatically queued for a new plan-and-apply run
- C) Workspace B receives a notification in the UI but requires a developer to manually trigger a run
- D) Workspace B triggers a run only if Workspace A's apply produced at least one resource change

### Question 97 — hard-mandatory Policy Failure Outcomes

**Difficulty**: Medium
**Answer Type**: many
**Topic**: What happens when a `hard-mandatory` Sentinel policy fails

**Question**:
A `hard-mandatory` Sentinel policy assigned to a workspace fails during a plan. Which TWO statements correctly describe what happens next? (Select two.)

- A) The run is blocked and cannot proceed to apply
- B) An organisation Owner can override the failure from the HCP Terraform UI to allow the run to proceed
- C) No user or role can override the failure — the policy code must pass before the run can continue
- D) The run proceeds to apply but records the policy failure in the audit log as a warning

### Question 98 — soft-mandatory Override Attempt by Write-Level User

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Whether a user with Write workspace permission can override a soft-mandatory policy failure

**Question**:
A `soft-mandatory` Sentinel policy fails during a run in an HCP Terraform workspace. A developer with **Write** workspace permission attempts to override the policy failure using the override button in the HCP Terraform UI. What happens?

- A) The override succeeds — Write permission includes the ability to override soft-mandatory policy failures
- B) The override fails — overriding soft-mandatory policies requires the "Manage Policy Overrides" permission, which is not included in Write access
- C) The override button is not visible to the developer — it is only shown to users with Admin workspace permission
- D) The override succeeds only if the developer is also a member of the team that manages the failing policy set

### Question 99 — Health Assessment Detects Drift

**Difficulty**: Medium
**Answer Type**: many
**Topic**: What HCP Terraform does when a scheduled health assessment detects configuration drift

**Question**:
HCP Terraform health assessments are enabled for a workspace. On its next scheduled run, the assessment detects that an EC2 instance's `instance_type` was manually changed in the AWS Console from `t3.micro` to `t3.small`. Which TWO things happen as a result? (Select two.)

- A) HCP Terraform automatically queues a `terraform apply` run to revert the instance type back to `t3.micro`
- B) The workspace's health status is marked as drifted in the HCP Terraform UI
- C) Notifications are sent to configured notification destinations alerting the team to the detected drift
- D) The workspace is locked to prevent further runs until the team manually resolves the drift

### Question 100 — terraform_remote_state Output That Does Not Exist

**Difficulty**: Medium
**Answer Type**: one
**Topic**: What happens at plan time when a `terraform_remote_state` reference targets a nonexistent output

**Question**:
A root module uses this configuration:

```hcl
data "terraform_remote_state" "network" {
  backend = "remote"
  config = {
    organization = "my-org"
    workspaces = { name = "networking" }
  }
}

resource "aws_instance" "app" {
  subnet_id = data.terraform_remote_state.network.outputs.private_subnet_id
}
```

The `networking` workspace state exists and is accessible, but it does **not** export an output named `private_subnet_id`. What happens during `terraform plan`?

- A) `subnet_id` is set to `null` — Terraform treats missing remote state outputs as null values
- B) Terraform raises an error during planning because `private_subnet_id` does not exist in the remote workspace outputs
- C) `terraform plan` succeeds but `aws_instance.app` is omitted from the plan until the output exists
- D) Terraform substitutes an empty string `""` and emits a warning about the missing output

### Question 101 — Workspace Variable Overrides Variable Set

**Difficulty**: Hard
**Answer Type**: one
**Topic**: Variable precedence when the same key is defined in both a variable set and a workspace variable

**Question**:
An HCP Terraform organisation has a variable set named "Shared Defaults" containing:

```
environment = "default"
```

This variable set is assigned to all workspaces. The `production` workspace also has a workspace-level variable defined directly:

```
environment = "production"
```

When Terraform runs in the `production` workspace, what value does `var.environment` have?

- A) `"default"` — variable sets take precedence over workspace-level variables
- B) `"production"` — workspace-level variables take precedence over variable sets
- C) An error is raised — HCP Terraform does not allow the same variable key to be defined in both a variable set and a workspace variable
- D) The run prompts the user to choose which value to use before planning begins

### Question 102 — TF_LOG_CORE and TF_LOG Interaction

**Difficulty**: Hard
**Answer Type**: many
**Topic**: How `TF_LOG_CORE` overrides `TF_LOG` and the resulting log output per component

**Question**:
An engineer configures these environment variables before running `terraform apply`:

```bash
export TF_LOG=DEBUG
export TF_LOG_CORE=OFF
```

Which TWO statements correctly describe the resulting logging behaviour? (Select two.)

- A) No logs are produced at all — `TF_LOG_CORE=OFF` disables all Terraform logging globally
- B) Provider plugin logs are produced at `DEBUG` level
- C) Terraform core logs are suppressed
- D) `TF_LOG=DEBUG` overrides `TF_LOG_CORE=OFF` for core components because it was set earlier



## Answer Key

| Q# | Answer(s) | Explanation | Source | Difficulty |
|---|---|---|---|---|
| 2 | C | N/A | What Terraform reports when infrastructure already matches the configuration | Easy |
| 3 | B | N/A | Terraform's response when a resource is manually deleted from the cloud | Easy |
| 4 | C | N/A | What happens when a declarative config reduces a resource count | Medium |
| 5 | B | N/A | What terraform plan shows when count is increased | Medium |
| 6 | B | N/A | What happens when a manual change is made outside Terraform then apply runs | Medium |
| 7 | A, B | N/A | Behavioural differences between Terraform (declarative) and Ansible (imperative) on repeated runs | Medium |
| 8 | B | N/A | Audit trail behaviour when infrastructure is changed outside of code | Medium |
| 9 | C | N/A | What happens when a config declares resources from multiple cloud providers | Medium |
| 10 | B | N/A | What apply produces when recreating a lost environment from code and state backup | Medium |
| 11 | A, B | N/A | Behavioural prediction when count is set to zero and apply runs | Medium |
| 12 | B | N/A | Reproducibility across environments using identical IaC configuration | Hard |
| 13 | B | N/A | Behavioural change when a team adopts IaC after managing infrastructure manually | Hard |
| 14 | B | N/A | What happens when terraform apply runs before terraform init | Easy |
| 15 | B | N/A | Which provider version gets installed when `~> 5.0` is specified and v5.31 is available | Easy |
| 16 | C | N/A | What happens when .terraform.lock.hcl is not committed to version control | Easy |
| 17 | C | N/A | What terraform init -upgrade does when a newer provider version is available | Medium |
| 18 | B | N/A | What happens when a resource omits a provider argument when multiple provider configs exist | Medium |
| 19 | C | N/A | What happens to a cloud resource after terraform state rm is run | Medium |
| 20 | B, C | N/A | What happens when two engineers run terraform apply simultaneously with local state | Medium |
| 21 | C | N/A | What happens to a sensitive output value in plan output vs state | Medium |
| 22 | B | N/A | What plan -refresh=false reports when cloud has drifted | Medium |
| 23 | B | N/A | What terraform state mv does to the resource in the cloud | Medium |
| 24 | B, C | N/A | What happens when a provider config has no credentials at apply time | Medium |
| 25 | C | N/A | What terraform plan proposes when the state file is missing | Hard |
| 26 | B | N/A | What happens if the provider plugin crashes during an apply | Hard |
| 27 | B | N/A | What terraform fmt reports when all files are already canonical | Easy |
| 28 | B | N/A | What terraform validate returns when a resource references an undefined local | Easy |
| 29 | B | N/A | What terraform plan -target does to the rest of the configuration | Easy |
| 30 | B | N/A | What happens when a saved plan file is applied after infrastructure changes | Medium |
| 31 | B | N/A | What terraform fmt -check returns when a file has incorrect formatting | Medium |
| 32 | C | N/A | What terraform graph outputs and how it is rendered | Medium |
| 33 | B | N/A | What terraform apply -replace does to the targeted resource | Medium |
| 34 | A | N/A | Difference in output format between terraform output and terraform output -raw | Medium |
| 35 | B | N/A | What terraform console returns when evaluating a built-in function | Medium |
| 36 | A, C | N/A | What terraform validate does and does not catch | Medium |
| 37 | B | N/A | What happens when terraform destroy -target targets a resource with dependents | Medium |
| 38 | B | N/A | What happens when the backend changes but terraform init is not re-run | Hard |
| 39 | A, B | N/A | What terraform fmt -diff does versus terraform fmt -check | Hard |
| 40 | C | N/A | What Terraform does when a resource references another resource's attribute | Easy |
| 41 | B | N/A | Whether a shared variable reference creates a dependency between resources | Easy |
| 42 | B | N/A | When a data source is read relative to plan and apply phases | Easy |
| 43 | C | N/A | What happens when terraform destroy runs against a resource with prevent_destroy = true | Medium |
| 44 | B | N/A | What terraform plan reports when a listed attribute has drifted with ignore_changes set | Medium |
| 45 | B | N/A | What happens to the dependent resource when replace_triggered_by fires | Medium |
| 46 | B | N/A | What happens when a moved block is used to rename a resource | Medium |
| 47 | B | N/A | How explicit depends_on affects apply parallelism | Medium |
| 48 | B | N/A | When a data source is deferred to apply because it depends on an unknown value | Medium |
| 49 | B, C | N/A | What happens when a removed block with destroy = false is applied | Medium |
| 50 | B | N/A | Plan output when an immutable attribute changes with create_before_destroy set | Medium |
| 51 | B | N/A | What terraform apply -parallelism=1 does to resource creation order | Hard |
| 52 | A, C | N/A | Behaviour when depends_on is added to a data source | Hard |
| 53 | C | N/A | What value Terraform uses when the same variable is set in auto.tfvars and via -var | Easy |
| 54 | A | N/A | What terraform output displays for a sensitive output | Easy |
| 55 | B | N/A | How many resource instances for_each creates when toset() is applied to a list with duplicates | Easy |
| 56 | B | N/A | What resource instance addresses are created in state when for_each uses a map | Medium |
| 57 | B | N/A | What terraform plan shows when the middle element is removed from a count list | Medium |
| 58 | C | N/A | How many nested blocks a dynamic block generates from a 3-element list | Medium |
| 59 | B | N/A | What value merge() produces when both maps share the same key | Medium |
| 60 | B | N/A | What value a conditional expression returns based on a variable | Medium |
| 61 | C | N/A | What try() returns when the primary expression produces an error | Medium |
| 62 | B, C | N/A | What a for expression with map output produces | Medium |
| 63 | C | N/A | What happens when nullable = false is set and no value is provided for the variable | Medium |
| 64 | D | N/A | What element() returns when the index exceeds the list length | Hard |
| 65 | A, C | N/A | Where a sensitive variable's value is and is not visible | Hard |
| 66 | C | N/A | What happens when a variable validation condition fails during terraform plan | Easy |
| 67 | C | N/A | What happens to terraform apply when a check block assertion evaluates to false | Easy |
| 68 | B | N/A | State of the resource when a precondition fails during apply | Medium |
| 69 | B, C | N/A | What is true about a resource after its postcondition fails | Medium |
| 70 | C | N/A | What terraform plan displays for a sensitive variable value in a resource argument | Medium |
| 71 | B | N/A | What happens when a validation condition references a data source instead of var.<name> | Medium |
| 72 | B | N/A | Effect on terraform apply when a scoped data source inside a check block fails | Medium |
| 73 | B | N/A | What happens when a sensitive module output is referenced in an unmarked output block | Medium |
| 74 | B | N/A | When check block assertions are evaluated — plan, apply, or both | Medium |
| 75 | A, C | N/A | Sequence of events when a variable has no default and requires interactive input | Medium |
| 76 | B | N/A | Final state of a resource after precondition passes and postcondition fails | Hard |
| 77 | B, C | N/A | What terraform output (no arguments) shows for sensitive vs non-sensitive outputs | Hard |
| 78 | B | N/A | What happens when a new module source is added but `terraform init` has not been re-run | Easy |
| 79 | C | N/A | What `terraform plan` shows immediately after `terraform state rm` removes a managed resource | Easy |
| 80 | B | N/A | The address used in the root module to reference a specific output from a child module | Easy |
| 81 | B | N/A | What happens at plan time when the root module passes an argument the child module never declared | Medium |
| 82 | B | N/A | What terraform init does when `version` is specified alongside a local path module source | Medium |
| 83 | C | N/A | What happens when the backend block is changed but `terraform init` has not been re-run | Medium |
| 84 | B | N/A | What terraform plan shows after state mv and a matching HCL resource label rename | Medium |
| 85 | B, C | N/A | What `terraform apply -refresh-only` does and does not modify | Medium |
| 86 | C | N/A | What risk exists when using an S3 backend without a DynamoDB lock table configured | Medium |
| 87 | B | N/A | What happens when a child module's required variable is not passed in the module block | Medium |
| 88 | A, C | N/A | What `terraform state pull` outputs and how it can be used | Medium |
| 89 | C | N/A | What happens to the old local terraform.tfstate after a successful migration to a remote backend | Hard |
| 90 | B, C | N/A | What terraform.tfstate.backup contains after multiple applies and its limitation as a backup mechanism | Hard |
| 91 | B | N/A | Where Terraform writes log output when `TF_LOG` is set but `TF_LOG_PATH` is not | Easy |
| 92 | C | N/A | Which HCP Terraform run type is automatically triggered when a pull request is opened | Easy |
| 93 | C | N/A | What `terraform state show` outputs for a specific resource | Easy |
| 94 | B | N/A | What happens when `terraform import` targets a resource address already tracked in state | Medium |
| 95 | C | N/A | When Terraform surfaces an error if the `import` block's `id` does not match any real cloud resource | Medium |
| 96 | B | N/A | What happens when `-generate-config-out` is used but the target resource block already exists | Medium |
| 97 | B | N/A | What HCP Terraform does to a downstream workspace when an upstream apply completes via a run trigger | Medium |
| 98 | A, C | N/A | What happens when a `hard-mandatory` Sentinel policy fails | Medium |
| 99 | B | N/A | Whether a user with Write workspace permission can override a soft-mandatory policy failure | Medium |
| 100 | B, C | N/A | What HCP Terraform does when a scheduled health assessment detects configuration drift | Medium |
| 101 | B | N/A | What happens at plan time when a `terraform_remote_state` reference targets a nonexistent output | Medium |
| 102 | B | N/A | Variable precedence when the same key is defined in both a variable set and a workspace variable | Hard |
| 103 | B, C | N/A | How `TF_LOG_CORE` overrides `TF_LOG` and the resulting log output per component | Hard |
