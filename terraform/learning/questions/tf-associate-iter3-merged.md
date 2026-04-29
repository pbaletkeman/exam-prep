# Terraform Associate Exam Questions

---

### Question 1 — State Addresses Created by count

**Difficulty**: Easy
**Answer Type**: one
**Topic**: Reading a `count` argument to determine how many state resource addresses Terraform tracks

**Question**:
Given the following configuration:

```hcl
resource "aws_instance" "app" {
  ami           = "ami-0abc1234"
  instance_type = "t3.micro"
  count         = 3
}
```

How many resource addresses does Terraform record in state after a successful apply?

- A) 1 — `aws_instance.app`
- B) 3 — `aws_instance.app[0]`, `aws_instance.app[1]`, `aws_instance.app[2]`
- C) 3 — `aws_instance.app.0`, `aws_instance.app.1`, `aws_instance.app.2`
- D) 1 — Terraform groups all instances under a single `aws_instance.app` state entry

---

### Question 2 — count = 0 Effect on Resource

**Difficulty**: Easy
**Answer Type**: one
**Topic**: Interpreting what `count = 0` means for a resource block

**Question**:
Read this configuration:

```hcl
resource "aws_instance" "bastion" {
  ami           = "ami-0abc1234"
  instance_type = "t3.nano"
  count         = 0
}
```

What does this configuration tell Terraform about the `aws_instance.bastion` resource?

- A) The resource is disabled — Terraform will create it on the next run when count is unset
- B) Zero instances of this resource should exist; if any currently exist, Terraform plans to destroy them
- C) This is a syntax error — `count` must be at least 1
- D) Terraform creates the resource but does not assign it an AMI or instance type

---

### Question 3 — Identifying Declarative vs Imperative from Snippets

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Classifying HCL vs shell script by the IaC approach each represents

**Question**:
Examine the two snippets below:

**Snippet A:**
```bash
aws ec2 run-instances \
  --image-id ami-0abc1234 \
  --instance-type t3.micro \
  --count 1
```

**Snippet B:**
```hcl
resource "aws_instance" "web" {
  ami           = "ami-0abc1234"
  instance_type = "t3.micro"
}
```

What is the correct characterisation of each snippet's approach?

- A) Both are declarative — they both describe a single EC2 instance
- B) Snippet A is declarative; Snippet B is imperative
- C) Snippet A is imperative; Snippet B is declarative
- D) Both are imperative — they both invoke AWS APIs to create resources

---

### Question 4 — Multi-Provider Config Provider Count

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Reading a multi-cloud config and identifying how many provider plugins are required

**Question**:
Read this configuration:

```hcl
provider "aws" {
  region = "us-east-1"
}

provider "azurerm" {
  features {}
}

resource "aws_s3_bucket" "data" {
  bucket = "my-data-bucket"
}

resource "azurerm_storage_account" "backup" {
  name                     = "backupstorage"
  resource_group_name      = "rg-backup"
  location                 = "eastus"
  account_tier             = "Standard"
  account_replication_type = "LRS"
}
```

How many provider plugins must `terraform init` download for this configuration to work?

- A) 1 — Terraform uses a single universal provider plugin for all cloud resources
- B) 2 — one AWS provider plugin and one Azure provider plugin
- C) 2 — one provider plugin shared between AWS and Azure resources
- D) 4 — one plugin per resource block

---

### Question 5 — What "Idempotent" Means for This Apply Output

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Interpreting an apply summary line to confirm idempotent behaviour

**Question**:
After a `terraform apply` completes, the final summary line reads:

```
Apply complete! Resources: 0 added, 0 changed, 0 destroyed.
```

What does this output tell you about the relationship between the configuration and the infrastructure?

- A) The apply failed silently — Terraform could not reach the provider API
- B) Terraform destroyed existing resources before recreating them with zero net change
- C) The infrastructure already matched the desired state — no actions were needed, demonstrating idempotency
- D) The configuration is empty — no resource blocks are declared

---

### Question 6 — Provider Constraint on Cloud Scope

**Difficulty**: Medium
**Answer Type**: many
**Topic**: Reading a provider block list and identifying correct claims about each tool's cloud scope

**Question**:
Read this excerpt from a comparison table:

```
Tool A: provider block required — "aws" only
Tool B: provider block required — "aws", "azurerm", "google", and 3000+ others
Tool C: template-based — no explicit provider concept, AWS only
```

Which TWO statements correctly identify the tools described? (Select two.)

- A) Tool A is Terraform — it only supports the AWS provider
- B) Tool B is Terraform — it is provider-agnostic with plugins for 3000+ providers
- C) Tool C is AWS CloudFormation — it is AWS-only and uses templates without explicit provider blocks
- D) Tool C is Azure ARM templates — it uses templates but supports multi-cloud via a provider concept

---

### Question 7 — Documentation Role of Config Files

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Interpreting a configuration file as living documentation of infrastructure

**Question**:
A new engineer joins a team and is given read access to the Git repository containing all Terraform `.tf` files. The repository has no separate architecture diagrams or runbooks. Which statement best describes what the engineer can determine from the Terraform files alone?

- A) Nothing useful — Terraform files only contain syntax, not meaningful infrastructure information
- B) Only the list of resource types — attributes and values are hidden by variable references
- C) The complete intended infrastructure topology: resource types, configurations, dependencies, and relationships — because configuration files serve as living documentation
- D) Only the most recently applied state — older configurations require the state file to reconstruct

---

### Question 8 — Interpreting Tool Type from Snippet

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Identifying whether a snippet represents a config management tool or a provisioning tool

**Question**:
Read the following snippet:

```yaml
- name: Install nginx
  apt:
    name: nginx
    state: present

- name: Start nginx
  service:
    name: nginx
    state: started
```

And this snippet:

```hcl
resource "aws_instance" "web" {
  ami           = "ami-0abc1234"
  instance_type = "t3.micro"
}
```

What category does each snippet belong to?

- A) Both are provisioning tools — they both create server-level resources
- B) The YAML snippet is from a **configuration management** tool (Ansible); the HCL snippet is from a **provisioning** tool (Terraform)
- C) The YAML snippet is from Terraform's YAML provider; the HCL snippet is from CloudFormation
- D) Both are declarative configuration management tools in the Ansible/Terraform ecosystem

---

### Question 9 — Audit Trail Interpretation from Git Log

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Interpreting what a Git log of `.tf` file changes provides as an IaC benefit

**Question**:
A team stores their Terraform configuration in Git. The following `git log` excerpt exists for `main.tf`:

```
abc1234 2026-03-10  alice  chore: increase web tier to t3.medium
def5678 2026-02-28  bob    feat: add RDS instance for prod
ghi9012 2026-01-15  carol  fix: reduce bastion count to 0
```

What IaC benefit does this log directly demonstrate?

- A) Repeatability — the same configuration can deploy identical environments
- B) Speed — automated provisioning is faster than manual console changes
- C) Audit trail — every infrastructure change is a version-controlled commit with author and timestamp
- D) Idempotency — running the same configuration multiple times produces the same result

---

### Question 10 — CloudFormation vs Terraform Multi-Cloud Snippet

**Difficulty**: Hard
**Answer Type**: one
**Topic**: Interpreting a snippet that declares both AWS and Azure resources to identify which tool it must be written in

**Question**:
A colleague shares this configuration snippet and claims it is valid for a popular IaC tool:

```hcl
resource "aws_vpc" "main" {
  cidr_block = "10.0.0.0/16"
}

resource "azurerm_virtual_network" "vnet" {
  name                = "prod-vnet"
  address_space       = ["10.1.0.0/16"]
  location            = "East US"
  resource_group_name = "rg-prod"
}
```

The snippet simultaneously manages resources in AWS (`aws_vpc`) and Azure (`azurerm_virtual_network`). Which tool could this configuration be written for?

- A) AWS CloudFormation — it supports multi-cloud resources via cross-account stacks
- B) Azure ARM templates — they natively support AWS resources through an Azure bridge provider
- C) Terraform — its provider plugin model supports multiple cloud providers in a single configuration
- D) Neither — no IaC tool supports declaring AWS and Azure resources in the same configuration file

---

### Question 11 — Interpreting "Drift" from a State vs Cloud Comparison

**Difficulty**: Hard
**Answer Type**: many
**Topic**: Reading a state-vs-actual comparison and identifying which attributes represent drift

**Question**:
The Terraform state file records the following for `aws_db_instance.primary`:

```
instance_class = "db.t3.medium"
backup_retention_period = 7
multi_az = false
```

A cloud administrator ran `terraform plan` and the output shows:

```
~ aws_db_instance.primary
    ~ instance_class           = "db.t3.medium" -> "db.t3.large"
    ~ backup_retention_period  = 7 -> 14
      multi_az                 = false
```

Which TWO statements correctly interpret this plan output? (Select two.)

- A) `instance_class` and `backup_retention_period` were changed outside of Terraform and represent infrastructure drift
- B) `multi_az = false` was changed outside of Terraform — Terraform plans to update it to `true`
- C) The `~` symbol before `aws_db_instance.primary` means the resource will be destroyed and recreated
- D) Terraform plans to update `instance_class` and `backup_retention_period` in-place to match the desired state in the configuration

---

### Question 12 — Reading a `~> 5.0` Version Constraint

**Difficulty**: Easy
**Answer Type**: one
**Topic**: What the pessimistic constraint operator `~> 5.0` permits

**Question**:
Read this `required_providers` block:

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

What version range does `"~> 5.0"` permit for the AWS provider?

- A) Exactly version `5.0.0` only
- B) Any version >= `5.0` and < `6.0` — minor and patch updates within major version 5
- C) Any version >= `5.0.0` and < `5.1.0` — patch updates within minor version 5.0 only
- D) Any version >= `5.0` with no upper limit

---

### Question 13 — Resolving a Short-Form Provider Source Address

**Difficulty**: Easy
**Answer Type**: one
**Topic**: How Terraform resolves a two-part provider source address to its fully qualified form

**Question**:
Read this `required_providers` block:

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

The `source` value is written as `"hashicorp/aws"`. What is the fully qualified address Terraform resolves this to?

- A) `github.com/hashicorp/aws`
- B) `registry.terraform.io/hashicorp/aws`
- C) `releases.hashicorp.com/terraform/aws`
- D) `terraform.io/providers/hashicorp/aws`

---

### Question 14 — `sensitive = true` on an Output Block

**Difficulty**: Easy
**Answer Type**: one
**Topic**: What `sensitive = true` does and does not protect in Terraform

**Question**:
Read this output block:

```hcl
output "rds_password" {
  value     = aws_db_instance.primary.password
  sensitive = true
}
```

A developer claims that `sensitive = true` fully protects this password from exposure in all Terraform contexts. Which statement correctly evaluates that claim?

- A) Correct — `sensitive = true` encrypts the password in both terminal output and `terraform.tfstate`
- B) Incorrect — `sensitive = true` hides the password from terminal output but it is stored in plaintext in `terraform.tfstate`
- C) Correct — `sensitive = true` prevents the password from being written to state altogether
- D) Incorrect — `sensitive = true` has no effect; the password appears in plaintext in both the terminal and the state file

---

### Question 15 — `~> 5.0.0` vs `~> 5.0` Constraint Range

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Distinguishing patch-only from minor+patch constraints using `~>`

**Question**:
Read this `required_providers` block:

```hcl
terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0.0"
    }
  }
}
```

How does the range permitted by `"~> 5.0.0"` differ from `"~> 5.0"`?

- A) There is no difference — both allow any `5.x.x` version
- B) `"~> 5.0.0"` allows a wider range — it permits `5.x` and `6.x` versions
- C) `"~> 5.0.0"` allows a narrower range — only patch updates are permitted (>= `5.0.0` and < `5.1.0`)
- D) `"~> 5.0.0"` is identical to `"= 5.0.0"` and pins exactly version `5.0.0`

---

### Question 16 — Default Provider Selection When Alias Exists

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Which provider configuration is used by a resource that omits the `provider` argument

**Question**:
Read this configuration:

```hcl
provider "aws" {
  region = "us-east-1"
}

provider "aws" {
  alias  = "west"
  region = "us-west-2"
}

resource "aws_instance" "api" {
  ami           = "ami-0abc1234"
  instance_type = "t3.micro"
}
```

In which AWS region will `aws_instance.api` be created?

- A) `us-west-2` — Terraform uses the most recently declared provider configuration
- B) `us-east-1` — resources with no `provider` argument use the default (unaliased) provider configuration
- C) Terraform returns an error because the `provider` argument is required when multiple configurations of the same provider exist
- D) Both regions simultaneously — Terraform creates one instance per provider configuration

---

### Question 17 — Lock File `hashes` Field Purpose

**Difficulty**: Medium
**Answer Type**: one
**Topic**: What the `hashes` entries in `.terraform.lock.hcl` provide

**Question**:
Read this `.terraform.lock.hcl` snippet:

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

What do the `hashes` entries in this lock file provide?

- A) The SHA-256 hash of the Terraform state file at the time the provider was last used
- B) Cryptographic checksums that allow Terraform to verify the downloaded provider binary has not been tampered with
- C) A record of which team member last ran `terraform init` to install this provider version
- D) Encoded authentication tokens used to download the provider from the registry

---

### Question 18 — State JSON `id` Field Role

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Identifying which field in `terraform.tfstate` links the config address to the real cloud resource

**Question**:
Read this `terraform.tfstate` excerpt:

```json
{
  "resources": [
    {
      "type": "aws_instance",
      "name": "db_server",
      "instances": [
        {
          "attributes": {
            "id": "i-0aaa1111bb2222cc3",
            "ami": "ami-0def5678",
            "instance_type": "t3.large",
            "private_ip": "10.0.1.5"
          }
        }
      ]
    }
  ]
}
```

Which field in this state excerpt is the primary link between the Terraform resource address `aws_instance.db_server` and the actual AWS cloud resource?

- A) `instance_type` — this uniquely identifies the resource family in AWS
- B) `ami` — AWS uses the AMI ID to track running instances
- C) `id` — `"i-0aaa1111bb2222cc3"` is the AWS-assigned instance ID that Terraform uses to reference the real resource in API calls
- D) `name` — `"db_server"` is registered as the unique identifier in the AWS API

---

### Question 19 — Provider Alias Reference on a Resource

**Difficulty**: Medium
**Answer Type**: one
**Topic**: What `provider = aws.west` on a resource block instructs Terraform to do

**Question**:
Read this configuration:

```hcl
provider "aws" {
  region = "us-east-1"
}

provider "aws" {
  alias  = "west"
  region = "us-west-2"
}

resource "aws_instance" "replica" {
  provider      = aws.west
  ami           = "ami-0xyz"
  instance_type = "t3.micro"
}
```

What does `provider = aws.west` on the `aws_instance.replica` resource accomplish?

- A) It creates the instance in both `us-east-1` and `us-west-2` simultaneously
- B) It instructs Terraform to use the aliased provider configuration with `region = "us-west-2"` for this specific resource
- C) It overrides the provider's configuration at runtime to use a custom region named `aws.west`
- D) It causes a validation error because the `provider` argument cannot be set on individual resources — only at module level

---

### Question 20 — Lock File Content After `terraform init`

**Difficulty**: Medium
**Answer Type**: many
**Topic**: What two pieces of information `.terraform.lock.hcl` records per provider

**Question**:
Read this `required_providers` block:

```hcl
terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
    google = {
      source  = "hashicorp/google"
      version = "~> 5.0"
    }
  }
}
```

After running `terraform init`, which TWO statements correctly describe what is recorded in `.terraform.lock.hcl`? (Select two.)

- A) The lock file records the exact version installed for each provider (e.g., `5.31.0` for AWS and `5.12.0` for Google)
- B) The lock file records the full source address for each provider (e.g., `registry.terraform.io/hashicorp/aws`)
- C) The lock file records the Terraform workspace name active at the time `init` was run
- D) The lock file records the path to the `.terraform/providers/` cache directory on the local machine

---

### Question 21 — Reading the `!=` Version Constraint

**Difficulty**: Medium
**Answer Type**: one
**Topic**: What the `!=` version constraint operator excludes

**Question**:
Read this `required_providers` block:

```hcl
terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "!= 5.0.0"
    }
  }
}
```

What does this version constraint tell `terraform init` to do?

- A) Install only version `5.0.0` of the AWS provider
- B) Install any available AWS provider version except `5.0.0`
- C) This is a syntax error — the `!=` operator is not supported in provider version constraints
- D) Exclude the entire `5.x` version family from consideration

---

### Question 22 — State Attributes Displayed by `terraform state show`

**Difficulty**: Medium
**Answer Type**: many
**Topic**: Interpreting a state JSON excerpt to identify what `terraform state show` returns

**Question**:
Read this `terraform.tfstate` excerpt:

```json
{
  "type": "aws_instance",
  "name": "db_server",
  "instances": [
    {
      "attributes": {
        "id": "i-0aaa1111bb2222cc3",
        "ami": "ami-0def5678",
        "instance_type": "t3.large",
        "private_ip": "10.0.1.5",
        "public_ip": "52.1.2.3"
      }
    }
  ]
}
```

Which TWO statements correctly describe what `terraform state show aws_instance.db_server` would display? (Select two.)

- A) The command displays the state-tracked attributes of the instance, including `id`, `ami`, `instance_type`, `private_ip`, and `public_ip` as recorded in state
- B) The `id` value `"i-0aaa1111bb2222cc3"` is the AWS-assigned instance ID visible in the state show output
- C) The command displays only the `id` attribute — all other attributes require `terraform refresh` before they appear in `state show`
- D) `terraform state show` retrieves the instance's current live attributes from the AWS API, not from the state file

---

### Question 23 — Comparing Two `~>` Constraints

**Difficulty**: Hard
**Answer Type**: many
**Topic**: Identifying the precise version ranges permitted by two different pessimistic constraints

**Question**:
Read these two version constraint values:

```hcl
# Constraint A
version = "~> 4.0"

# Constraint B
version = "~> 4.67.0"
```

Which TWO statements correctly describe the version range each constraint allows? (Select two.)

- A) Constraint A (`~> 4.0`) allows versions >= `4.0` and < `5.0` — any `4.x` minor or patch version
- B) Constraint A (`~> 4.0`) allows versions >= `4.0` and < `4.1` — only `4.0.x` patch versions
- C) Constraint B (`~> 4.67.0`) allows versions >= `4.67.0` and < `4.68.0` — only patch updates within `4.67`
- D) Constraint B (`~> 4.67.0`) allows versions >= `4.67.0` and < `5.0` — any version from `4.67` onward within major 4

---

### Question 24 — Lock File After `terraform init -upgrade`

**Difficulty**: Hard
**Answer Type**: one
**Topic**: What fields change in `.terraform.lock.hcl` when a newer provider version is installed via `-upgrade`

**Question**:
Read this `.terraform.lock.hcl` entry:

```hcl
provider "registry.terraform.io/hashicorp/aws" {
  version     = "5.10.0"
  constraints = "~> 5.0"
  hashes = [
    "h1:oldhash...",
  ]
}
```

AWS provider `5.31.0` has since been released. `terraform init -upgrade` is run. What does the lock file look like after the command completes?

- A) Nothing changes — the lock file is read-only and can only be modified by deleting and regenerating it
- B) The `version` field updates to `5.31.0` and the `hashes` field updates to reflect the new binary's checksums; `constraints` remains `"~> 5.0"` unchanged
- C) The `constraints` field changes to `"= 5.31.0"` to pin the exact new version; `version` and `hashes` also update
- D) The `version` field updates to `5.31.0` but the `hashes` field remains unchanged because hashes are stable across versions

---

### Question 25 — Identifying the Pure-Create Resource in a Plan

**Difficulty**: Easy
**Answer Type**: one
**Topic**: Reading plan output symbols to identify which resource will be created without a corresponding destruction

**Question**:
Read this `terraform plan` output:

```
  # aws_vpc.main will be created
+ resource "aws_vpc" "main" {
    + cidr_block = "10.0.0.0/16"
  }

  # aws_instance.web will be updated in-place
~ resource "aws_instance" "web" {
    ~ instance_type = "t3.micro" -> "t3.medium"
  }

  # aws_db_instance.primary must be replaced
-/+ resource "aws_db_instance" "primary" {
    ~ instance_class = "db.t3.micro" -> "db.t3.medium" # forces replacement
  }

Plan: 2 to add, 1 to change, 1 to destroy.
```

Which resource does the `+` symbol (without any `-`) indicate will be **created with no corresponding destruction**?

- A) `aws_db_instance.primary` — its `-/+` symbol includes a create step
- B) `aws_vpc.main` — the `+` prefix alone means a net-new object will be created
- C) `aws_instance.web` — the `~` symbol includes a create for the updated attributes
- D) All three resources will result in newly created objects after apply

---

### Question 26 — `terraform console` Evaluating a Map with `length`

**Difficulty**: Easy
**Answer Type**: one
**Topic**: Reading a `terraform console` REPL expression to identify the return value

**Question**:
An engineer opens `terraform console` and types:

```
length({"us-east-1" = "ami-111", "us-west-2" = "ami-222", "eu-west-1" = "ami-333"})
```

What value does the console return?

- A) `0` — `length()` returns 0 for map types; it only counts list elements
- B) `3`
- C) `{"us-east-1", "us-west-2", "eu-west-1"}` — the set of keys in the map
- D) An error — `length()` is not a valid built-in function in `terraform console`

---

### Question 27 — Reading `terraform workspace list` Output

**Difficulty**: Easy
**Answer Type**: one
**Topic**: Identifying the currently active workspace from `terraform workspace list` output

**Question**:
Read this output from `terraform workspace list`:

```
  default
  dev
* staging
  production
```

Which workspace is currently selected?

- A) `default` — the default workspace is always active unless explicitly changed
- B) `dev` — it is listed second, indicating it was most recently used
- C) `staging` — the `*` prefix marks the currently active workspace
- D) `production` — it is the last workspace listed, indicating it is the current context

---

### Question 28 — Interpreting a `-/+` Plan Block

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Reading a plan resource block with the `-/+` replace symbol to identify what Terraform will do

**Question**:
Read this `terraform plan` output block:

```
  # aws_instance.app must be replaced
-/+ resource "aws_instance" "app" {
    ~ id           = "i-0abc123def456" -> (known after apply)
    ~ ami          = "ami-0old12345678" -> "ami-0new87654321" # forces replacement
      instance_type = "t3.micro"
}
```

What does the `-/+` symbol on `aws_instance.app` indicate Terraform will do during apply?

- A) The instance will be updated in-place — only the `ami` attribute will change without downtime
- B) The instance will be imported from an existing cloud resource with a new Terraform address
- C) The existing instance will be destroyed and a brand-new instance will be created (replacement)
- D) The change is deferred — Terraform will update the instance on the next apply cycle, not the current one

---

### Question 29 — `terraform output -json` Structure

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Identifying which `terraform output` flag produces structured JSON with type metadata

**Question**:
Read this command output:

```json
{
  "vpc_id": {
    "sensitive": false,
    "type": "string",
    "value": "vpc-0abc12345ef678"
  },
  "subnet_ids": {
    "sensitive": false,
    "type": ["list", "string"],
    "value": ["subnet-111aaa", "subnet-222bbb"]
  }
}
```

Which `terraform output` flag produces this structured JSON format that includes `sensitive`, `type`, and `value` fields for each output?

- A) `terraform output --format=structured`
- B) `terraform output -raw`
- C) `terraform output -json`
- D) `terraform output -show-types`

---

### Question 30 — `terraform fmt -check` vs `terraform fmt -diff`

**Difficulty**: Medium
**Answer Type**: many
**Topic**: Reading two `terraform fmt` flag invocations and identifying what each does

**Question**:
Read these two commands:

```bash
terraform fmt -check
terraform fmt -diff
```

Which TWO statements correctly describe the behaviour of these two flags? (Select two.)

- A) `-check` exits with code 1 if any files need reformatting, without modifying any files — used to enforce formatting in CI pipelines
- B) `-diff` writes reformatted content to disk and then displays a summary of changes made
- C) `-diff` displays the formatting changes that would be made as a unified diff, without writing any changes to disk
- D) `-check` modifies files to canonical format and then verifies the result, exiting with code 0 on success

---

### Question 31 — `terraform show plan.tfplan`

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Identifying what `terraform show` displays when given a saved plan file

**Question**:
An engineer runs:

```bash
terraform plan -out=release.tfplan
terraform show release.tfplan
```

What does `terraform show release.tfplan` display?

- A) The current Terraform state — `show` always reads from `terraform.tfstate` regardless of the argument
- B) The human-readable contents of the saved plan file — the resource changes that would be applied when `terraform apply release.tfplan` is run
- C) The Terraform configuration files compiled into a single canonical HCL representation
- D) A comparison between the saved plan and the current live infrastructure to detect drift since the plan was saved

---

### Question 32 — Inline `-var` Flag Override

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Reading a `terraform plan -var` command to identify which value `var.instance_type` takes

**Question**:
A `variables.tf` file declares:

```hcl
variable "instance_type" {
  default = "t3.micro"
}
```

An engineer runs:

```bash
terraform plan -var "instance_type=t3.large"
```

What value does `var.instance_type` take during this plan run?

- A) `"t3.micro"` — the default value in `variables.tf` always takes precedence
- B) An error is raised because `-var` can only override variables that have no default
- C) `"t3.large"` — the inline `-var` flag value overrides the default declared in `variables.tf`
- D) Both values are used — Terraform creates a `t3.micro` instance and a `t3.large` instance to satisfy both declarations

---

### Question 33 — Interpreting an Update Plan Block

**Difficulty**: Medium
**Answer Type**: many
**Topic**: Reading a `~` plan block to identify which statements correctly describe the operation

**Question**:
Read this `terraform plan` output block:

```
~ resource "aws_security_group" "web" {
    ~ description = "allow http traffic" -> "allow http and https traffic"
    ~ name        = "web-sg-v1"          -> "web-sg-v2"
      vpc_id      = "vpc-0abc12345"
  }
```

Which TWO statements correctly interpret this output? (Select two.)

- A) The `~` prefix on the resource block means `aws_security_group.web` will be destroyed and recreated as a replacement
- B) `vpc_id` is not changing — lines without a `~` or `+/-` prefix show attributes that remain the same
- C) Both `description` and `name` will be updated in-place without destroying the security group
- D) The `->` arrow on individual attribute lines means those attributes will be moved to a different resource address

---

### Question 34 — `terraform init -migrate-state` Backend Block

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Reading a backend block addition and identifying which `terraform init` flag copies existing state to the new backend

**Question**:
A team adds this block to their configuration to move from local state to S3:

```hcl
terraform {
  backend "s3" {
    bucket = "my-company-tf-state"
    key    = "prod/terraform.tfstate"
    region = "us-east-1"
  }
}
```

They run `terraform init` and Terraform detects existing local state in `terraform.tfstate`. Which `terraform init` flag must they include to copy the existing state to the new S3 backend?

- A) `terraform init -migrate-state` — copies existing state to the new backend during initialisation
- B) `terraform init -upgrade` — upgrades the backend configuration and transfers state automatically
- C) `terraform init -reconfigure` — replaces the backend configuration and migrates state in one step
- D) `terraform init -backend=true` — enables the backend and imports the local state file

---

### Question 35 — `-auto-approve` with a Saved Plan File

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Identifying the effect of combining `-auto-approve` with a saved plan file argument

**Question**:
An engineer runs:

```bash
terraform apply -auto-approve release.tfplan
```

What is the effect of including `-auto-approve` when a saved plan file (`release.tfplan`) is also provided?

- A) `-auto-approve` causes Terraform to skip the plan phase and apply all resource changes unconditionally
- B) `-auto-approve` is required alongside a saved plan file to unlock the apply — without it, the apply is blocked
- C) `-auto-approve` is required to prevent Terraform from re-planning after loading the saved plan file
- D) `-auto-approve` is redundant — applying a saved plan file never prompts for confirmation; the plan has already been reviewed

---

### Question 36 — Plan Summary with Only Replacements

**Difficulty**: Hard
**Answer Type**: many
**Topic**: Interpreting a plan summary line where all changes are `-/+` replacements

**Question**:
Read this `terraform plan` summary line:

```
Plan: 2 to add, 0 to change, 2 to destroy.
```

The full plan output shows exactly two resources, both marked with `-/+` (replace). No resource has a `+`, `~`, or `-` prefix alone. Which TWO statements correctly interpret this plan summary? (Select two.)

- A) The "2 to add" refers to the new objects that will be created as part of the replacement operations
- B) The "2 to destroy" means two resources will be permanently deleted with no new objects created in their place
- C) `0 to change` confirms that no resource will be modified in-place — both operations require a destroy-then-create cycle
- D) The "2 to add" and "2 to destroy" must refer to four different resource addresses — adds and destroys are always distinct resources

---

### Question 37 — `terraform apply -replace` Plan Symbol

**Difficulty**: Hard
**Answer Type**: one
**Topic**: Identifying what plan symbol appears for a resource targeted by `terraform apply -replace` when the configuration is unchanged

**Question**:
A running EC2 instance is managed by Terraform as `aws_instance.web`. The configuration for this resource has not changed since the last apply. An engineer runs:

```bash
terraform apply -replace="aws_instance.web"
```

What symbol does the plan output show for `aws_instance.web`, and what does that symbol mean?

- A) No symbol — Terraform skips resources with no configuration changes even when `-replace` is specified
- B) `~` — the instance will be updated in-place because the configuration is unchanged
- C) `-/+` — the instance will be destroyed and recreated even though no configuration change triggered it
- D) `+` — a second instance will be created alongside the existing one before the original is removed

---

### Question 38 — `create_before_destroy` Replacement Order

**Difficulty**: Easy
**Answer Type**: one
**Topic**: Reading a `lifecycle` block to identify the order of destroy and create during a forced replacement

**Question**:
Read this resource block:

```hcl
resource "aws_instance" "web" {
  ami           = data.aws_ami.ubuntu.id
  instance_type = "t3.micro"

  lifecycle {
    create_before_destroy = true
  }
}
```

The AMI referenced by `data.aws_ami.ubuntu.id` changes. Terraform determines that a replacement is required. In what order does Terraform perform the operations?

- A) Terraform destroys the existing instance first, then creates the new one
- B) Terraform creates the new instance first, then destroys the old one only after the new one is successfully provisioned
- C) Terraform updates the existing instance in-place — `create_before_destroy` prevents any destroy operation
- D) Terraform creates both instances simultaneously and destroys whichever completes last

---

### Question 39 — Distinguishing a Data Source Reference from a Resource Reference

**Difficulty**: Easy
**Answer Type**: one
**Topic**: Identifying which expression references a data source vs a managed resource attribute

**Question**:
Read this resource block:

```hcl
resource "aws_instance" "web" {
  ami           = data.aws_ami.ubuntu.id
  subnet_id     = aws_subnet.public.id
  instance_type = "t3.micro"
}
```

Which of the two attribute references — `data.aws_ami.ubuntu.id` and `aws_subnet.public.id` — references a **data source**, and what syntactically distinguishes it?

- A) `aws_subnet.public.id` — resource references always include a `data.` prefix
- B) `data.aws_ami.ubuntu.id` — the `data.` prefix identifies it as a data source reference, not a managed resource
- C) Both are data source references — all attribute references in Terraform begin with a provider keyword
- D) Neither is a data source reference — both reference managed resources declared with a `resource` block

---

### Question 40 — `moved` Block Address After Apply

**Difficulty**: Easy
**Answer Type**: one
**Topic**: Identifying which state address Terraform uses after a `moved` block is applied

**Question**:
Read this `moved` block:

```hcl
moved {
  from = aws_instance.server
  to   = aws_instance.api
}
```

The `aws_instance.server` resource is running in AWS and tracked in state. After `terraform apply` processes this block, under which address is the EC2 instance tracked in the state file?

- A) `aws_instance.server` — the `moved` block creates an alias but keeps the original address
- B) Both `aws_instance.server` and `aws_instance.api` — state records both addresses until the block is removed
- C) `aws_instance.api` — the state file is updated to use the new address; the real EC2 instance is not touched
- D) The instance is destroyed and a new instance is created under `aws_instance.api`

---

### Question 41 — Three-Resource Implicit Dependency Chain

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Reading a three-resource configuration to identify which resource is created last and why

**Question**:
Read this configuration:

```hcl
resource "aws_vpc" "main" {
  cidr_block = "10.0.0.0/16"
}

resource "aws_subnet" "public" {
  vpc_id     = aws_vpc.main.id
  cidr_block = "10.0.1.0/24"
}

resource "aws_instance" "web" {
  ami       = "ami-0abc123"
  subnet_id = aws_subnet.public.id
}
```

Which resource is created **last**, and what in the HCL determines this ordering?

- A) `aws_vpc.main` — it is declared first, so Terraform creates it last to allow dependencies to resolve
- B) `aws_subnet.public` — it has the most arguments, indicating the highest complexity
- C) `aws_instance.web` — it references `aws_subnet.public.id`, which itself references `aws_vpc.main.id`, creating a three-level dependency chain
- D) All three are created in parallel — HCL declaration order is the only ordering Terraform respects

---

### Question 42 — `ignore_changes` on a Modified Attribute

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Reading a plan output for a resource whose changed attribute is listed in `ignore_changes`

**Question**:
Read this resource block:

```hcl
resource "aws_instance" "web" {
  ami           = "ami-0abc123"
  instance_type = "t3.micro"

  lifecycle {
    ignore_changes = [ami]
  }
}
```

The AMI in the AWS account has been manually changed from `ami-0abc123` to `ami-0new9876`. A `terraform plan` is run. What does Terraform report for `aws_instance.web`?

- A) `~ ami = "ami-0abc123" -> "ami-0new9876"` — Terraform will update the AMI to match the new value
- B) No changes to `aws_instance.web` — the `ami` attribute is listed in `ignore_changes`, so drift on it is silently ignored
- C) Terraform returns an error because `ignore_changes` cannot be used with the `ami` argument
- D) Terraform destroys the instance and recreates it with the new AMI

---

### Question 43 — `removed` Block with `destroy = false`

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Reading a `removed` block to identify the effect on the real cloud resource

**Question**:
Read this `removed` block:

```hcl
removed {
  from = aws_s3_bucket.legacy

  lifecycle {
    destroy = false
  }
}
```

The `aws_s3_bucket.legacy` bucket currently exists in AWS and is tracked in state. After `terraform apply` processes this block, what happens to the S3 bucket?

- A) The bucket is deleted from AWS because the `removed` block explicitly removes the resource
- B) The bucket remains in AWS unchanged — Terraform removes it from state but does not destroy the real cloud resource
- C) The bucket is moved to a new state address `aws_s3_bucket.removed_legacy` as an archived entry
- D) Terraform returns an error because `destroy = false` is not a valid lifecycle argument inside a `removed` block

---

### Question 44 — `depends_on` Ordering Guarantee

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Reading a `depends_on` list to identify which resource Terraform is guaranteed to apply first

**Question**:
Read this configuration:

```hcl
resource "aws_iam_role_policy" "s3_access" {
  role   = aws_iam_role.app.name
  policy = data.aws_iam_policy_document.s3.json
}

resource "aws_instance" "app" {
  ami           = "ami-0abc123"
  instance_type = "t3.micro"

  depends_on = [aws_iam_role_policy.s3_access]
}
```

What ordering does the `depends_on` on `aws_instance.app` guarantee?

- A) `aws_instance.app` is created first so it can begin using the S3 policy as soon as the policy is ready
- B) `aws_iam_role_policy.s3_access` is fully applied before `aws_instance.app` is created, even though no attribute of the policy is directly referenced by the instance
- C) Both resources are created in parallel — `depends_on` only affects destroy ordering, not create ordering
- D) Terraform returns a warning because `depends_on` is redundant when both resources reference the same IAM role

---

### Question 45 — `replace_triggered_by` with a Specific Attribute

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Reading a `replace_triggered_by` referencing an attribute vs an entire resource

**Question**:
Read this configuration:

```hcl
resource "aws_launch_template" "web" {
  image_id      = var.ami_id
  instance_type = "t3.micro"
}

resource "aws_autoscaling_group" "web" {
  min_size = 1
  max_size = 3

  lifecycle {
    replace_triggered_by = [aws_launch_template.web.image_id]
  }
}
```

How does `replace_triggered_by = [aws_launch_template.web.image_id]` differ from `replace_triggered_by = [aws_launch_template.web]`?

- A) There is no difference — referencing a resource and referencing one of its attributes produce identical behaviour
- B) Referencing the attribute `image_id` means the ASG is replaced **only** when `image_id` changes; updating other launch template attributes (e.g., `instance_type`) does not trigger ASG replacement
- C) Referencing an attribute reference is a syntax error — `replace_triggered_by` only accepts full resource addresses, not attribute paths
- D) Referencing `aws_launch_template.web.image_id` makes the trigger one-directional — changes to the ASG no longer propagate back to the launch template

---

### Question 46 — `terraform apply -parallelism=1`

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Reading a `terraform apply -parallelism` flag to identify its effect on execution

**Question**:
An engineer runs:

```bash
terraform apply -parallelism=1
```

The configuration manages 8 independent resources with no dependency relationships between them. What does `-parallelism=1` do to the apply execution?

- A) Terraform creates all 8 resources simultaneously — `-parallelism=1` sets the first resource as the primary and applies the rest in parallel
- B) Terraform creates exactly one resource at a time in strict sequence, even though all 8 could safely run in parallel
- C) Terraform returns an error — `-parallelism` must be set to at least 2 when independent resources exist
- D) `-parallelism=1` is the default value and has no effect; Terraform always applies one resource at a time without this flag

---

### Question 47 — `lifecycle` Block with Multiple Arguments

**Difficulty**: Medium
**Answer Type**: many
**Topic**: Reading a lifecycle block with three arguments to identify TWO correct behavioural statements

**Question**:
Read this resource block:

```hcl
resource "aws_db_instance" "prod" {
  instance_class = "db.t3.medium"
  engine_version = "14.5"

  lifecycle {
    create_before_destroy = true
    prevent_destroy       = true
    ignore_changes        = [engine_version]
  }
}
```

Which TWO statements correctly describe the behaviour this `lifecycle` block enforces? (Select two.)

- A) If any execution plan includes destroying `aws_db_instance.prod`, Terraform will return an error at plan time
- B) If `engine_version` is upgraded in the AWS console, `terraform plan` will propose reverting it to `"14.5"`
- C) If a replacement of the database is required, Terraform will provision the new instance before deleting the old one
- D) `prevent_destroy = true` only protects against `terraform destroy` — it does not block replacements triggered by config changes

---

### Question 48 — Data Source Block TWO Correct Statements

**Difficulty**: Medium
**Answer Type**: many
**Topic**: Reading a data source block and its consumer resource to identify TWO correct statements

**Question**:
Read this configuration:

```hcl
data "aws_ami" "ubuntu" {
  most_recent = true
  owners      = ["099720109477"]

  filter {
    name   = "name"
    values = ["ubuntu/images/hvm-ssd/ubuntu-jammy-22.04-amd64-server-*"]
  }
}

resource "aws_instance" "web" {
  ami           = data.aws_ami.ubuntu.id
  instance_type = "t3.micro"
}
```

Which TWO statements correctly describe this configuration? (Select two.)

- A) `data.aws_ami.ubuntu` does not create a new AMI in AWS — it queries an existing AMI that matches the filter criteria
- B) The `filter` block inside the `data` source instructs Terraform to create a new Ubuntu AMI if no existing AMI matches the pattern
- C) The reference `data.aws_ami.ubuntu.id` uses the `data.` prefix to distinguish it as a data source reference, not a managed resource reference
- D) The `most_recent = true` argument causes Terraform to create a new AMI version on every `terraform plan` to ensure freshness

---

### Question 49 — Parallel vs Sequential Resource Creation

**Difficulty**: Hard
**Answer Type**: one
**Topic**: Reading a multi-resource configuration to identify which resources run concurrently and which must wait

**Question**:
Read this configuration (assume `aws_vpc.main` and `aws_iam_role.web` already exist in state):

```hcl
resource "aws_security_group" "web_sg" {
  name   = "web-sg"
  vpc_id = aws_vpc.main.id
}

resource "aws_iam_instance_profile" "web" {
  name = "web-profile"
  role = aws_iam_role.web.name
}

resource "aws_instance" "web" {
  ami                    = "ami-0abc123"
  instance_type          = "t3.micro"
  vpc_security_group_ids = [aws_security_group.web_sg.id]
  iam_instance_profile   = aws_iam_instance_profile.web.name
}
```

Which statement correctly describes how Terraform schedules creation of these three resources?

- A) All three resources are created sequentially in file declaration order: `aws_security_group.web_sg` → `aws_iam_instance_profile.web` → `aws_instance.web`
- B) `aws_security_group.web_sg` and `aws_iam_instance_profile.web` are independent — Terraform creates them in parallel; `aws_instance.web` is created last because it references both
- C) `aws_instance.web` is created first because it is declared last — Terraform processes bottom-up
- D) All three are created in parallel because Terraform always maximises concurrency regardless of references

---

### Question 50 — `moved` Block into a Module

**Difficulty**: Hard
**Answer Type**: many
**Topic**: Reading a `moved` block that relocates a resource from root module into a child module

**Question**:
Read this `moved` block:

```hcl
moved {
  from = aws_s3_bucket.app_data
  to   = module.storage.aws_s3_bucket.app_data
}
```

The S3 bucket `aws_s3_bucket.app_data` exists in state and in AWS. A `module "storage"` block has been added to the configuration that declares the same `aws_s3_bucket.app_data` resource. Which TWO statements correctly describe the effect of this `moved` block? (Select two.)

- A) Terraform updates the state file to track the bucket under `module.storage.aws_s3_bucket.app_data` without destroying and recreating the real S3 bucket
- B) Terraform destroys the existing bucket at `aws_s3_bucket.app_data` and creates a new bucket inside the `module.storage` module
- C) After a successful `terraform apply`, the `moved` block can be safely removed from the configuration — the state already records the updated address
- D) The `moved` block must remain in the configuration permanently to prevent Terraform from flagging the address difference on each subsequent plan

---

### Question 51 — `locals` String Interpolation Result

**Difficulty**: Easy
**Answer Type**: one
**Topic**: Reading a `locals` block with interpolation to identify the computed string value

**Question**:
Read this `locals` block:

```hcl
locals {
  app_name    = "my-app"
  environment = "production"
  full_name   = "${local.app_name}-${local.environment}"
}
```

What is the value of `local.full_name`?

- A) `"my-app"` — the second interpolation is ignored when locals reference other locals
- B) `"my-app-${local.environment}"` — Terraform does not resolve nested local references
- C) `"my-app-production"` — both local references are resolved and joined with a hyphen
- D) Terraform returns an error because a local cannot reference another local in the same block

---

### Question 52 — `for` Expression: List Brackets vs Map Braces

**Difficulty**: Easy
**Answer Type**: one
**Topic**: Identifying the output type of a `for` expression based on its outer delimiters

**Question**:
Read these two local definitions:

```hcl
locals {
  names    = ["alice", "bob", "carol"]
  result_a = [for n in local.names : upper(n)]
  result_b = {for n in local.names : n => upper(n)}
}
```

What are the types of `local.result_a` and `local.result_b`?

- A) Both are lists — `for` expressions always produce lists regardless of the outer delimiter
- B) `local.result_a` is a list; `local.result_b` is a map — the outer `[...]` vs `{...}` determines the output type
- C) `local.result_a` is a map; `local.result_b` is a list — braces indicate a list in Terraform
- D) Both are maps — Terraform converts all `for` expression outputs to maps for consistency

---

### Question 53 — `zipmap()` Result

**Difficulty**: Easy
**Answer Type**: one
**Topic**: Reading a `zipmap()` call to identify the resulting map

**Question**:
Read this `locals` block:

```hcl
locals {
  keys   = ["us-east-1", "eu-west-1"]
  values = ["prod-east", "prod-west"]
  region_map = zipmap(local.keys, local.values)
}
```

What is the value of `local.region_map`?

- A) `["us-east-1", "prod-east", "eu-west-1", "prod-west"]` — `zipmap` interleaves the two lists
- B) `{ "us-east-1" = "prod-east", "eu-west-1" = "prod-west" }` — the first list provides keys and the second provides values
- C) `{ "prod-east" = "us-east-1", "prod-west" = "eu-west-1" }` — `zipmap` uses the second list as keys
- D) Terraform returns an error because `zipmap` requires both lists to have the same value type

---

### Question 54 — `dynamic` Block with Custom `iterator` Name

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Identifying the correct attribute reference inside a `dynamic` block that uses a custom `iterator` name

**Question**:
Read this resource block:

```hcl
variable "ingress_rules" {
  default = [
    { from_port = 80,  to_port = 80,  protocol = "tcp" },
    { from_port = 443, to_port = 443, protocol = "tcp" },
  ]
}

resource "aws_security_group" "web" {
  name = "web-sg"

  dynamic "ingress" {
    for_each = var.ingress_rules
    iterator = rule

    content {
      from_port   = rule.value.from_port
      to_port     = rule.value.to_port
      protocol    = rule.value.protocol
      cidr_blocks = ["0.0.0.0/0"]
    }
  }
}
```

Inside the `content` block, what does `rule.value.from_port` reference, and why is `ingress.value.from_port` not used instead?

- A) `rule.value.from_port` and `ingress.value.from_port` are identical — both reference the same element; the names are interchangeable
- B) `rule.value.from_port` references the current element's `from_port` because `iterator = rule` overrides the default iterator name (`ingress`); `ingress.value.from_port` would produce an error in this block
- C) `rule` is a reserved keyword in Terraform that automatically references the loop variable regardless of the `iterator` setting
- D) `ingress.value.from_port` should always be used in `content` blocks; `rule` is only valid outside the `dynamic` block

---

### Question 55 — `for` Map Comprehension with Key Transformation

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Reading a map `for` expression that transforms keys to identify the resulting map content

**Question**:
Read this `locals` block:

```hcl
variable "environments" {
  default = {
    dev  = "us-east-1"
    prod = "eu-west-1"
  }
}

locals {
  env_labels = { for k, v in var.environments : upper(k) => v }
}
```

What is the value of `local.env_labels`?

- A) `{ dev = "us-east-1", prod = "eu-west-1" }` — `upper()` has no effect on map keys
- B) `{ DEV = "us-east-1", PROD = "eu-west-1" }` — the `upper(k)` call transforms each key to uppercase while keeping values unchanged
- C) `{ DEV = "US-EAST-1", PROD = "EU-WEST-1" }` — `upper()` is applied to both keys and values
- D) Terraform returns an error because `upper()` cannot be called in the key position of a `for` expression

---

### Question 56 — `cidrhost()` Returns a Host IP

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Reading a `cidrhost()` call to identify the resulting IP address

**Question**:
Read this `locals` block:

```hcl
locals {
  subnet_cidr = "10.0.1.0/24"
  gateway_ip  = cidrhost(local.subnet_cidr, 1)
  broadcast   = cidrhost(local.subnet_cidr, 254)
}
```

What is the value of `local.gateway_ip`?

- A) `"10.0.1.0"` — `cidrhost()` with host number 1 returns the network address
- B) `"10.0.1.1"` — `cidrhost()` adds the host number to the network portion to produce the host address
- C) `"10.0.0.1"` — `cidrhost()` subtracts from the network address
- D) `"10.0.1.0/24"` — `cidrhost()` returns the full CIDR notation, not a bare IP

---

### Question 57 — `concat()` Combines Two Lists

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Reading a `concat()` call to identify the resulting list

**Question**:
Read this `locals` block:

```hcl
locals {
  web_ips = ["10.0.1.10", "10.0.1.11"]
  app_ips = ["10.0.2.10"]
  all_ips = concat(local.web_ips, local.app_ips)
}
```

What is the value of `local.all_ips`?

- A) `["10.0.1.10", "10.0.1.11", "10.0.2.10"]` — `concat()` appends the second list to the first, producing a flat list
- B) `[["10.0.1.10", "10.0.1.11"], ["10.0.2.10"]]` — `concat()` creates a nested list preserving the original structure
- C) `{ web = ["10.0.1.10", "10.0.1.11"], app = ["10.0.2.10"] }` — `concat()` converts the lists to a map
- D) `"10.0.1.10,10.0.1.11,10.0.2.10"` — `concat()` joins the lists into a comma-separated string

---

### Question 58 — `jsonencode()` Output Type

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Reading a `jsonencode()` call to identify the type and structure of the output

**Question**:
Read this `locals` block:

```hcl
locals {
  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Effect   = "Allow"
      Action   = "s3:GetObject"
      Resource = "*"
    }]
  })
}
```

What is the type of `local.policy`, and how is it used in practice?

- A) `object` — `jsonencode()` keeps the input as a structured Terraform object for use in resource arguments
- B) `string` — `jsonencode()` serialises the Terraform object to a JSON-formatted string, suitable for arguments that expect a JSON document
- C) `map(string)` — `jsonencode()` flattens all nested structures into a flat string-to-string map
- D) `list(string)` — `jsonencode()` converts each top-level key into a separate string element

---

### Question 59 — `validation` Block Condition Evaluation

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Reading a `validation` block to determine whether a given input value passes or fails

**Question**:
Read this variable declaration:

```hcl
variable "environment" {
  type = string

  validation {
    condition     = contains(["dev", "staging", "production"], var.environment)
    error_message = "environment must be one of: dev, staging, production."
  }
}
```

An engineer runs `terraform plan -var="environment=test"`. What happens?

- A) The plan proceeds normally — `"test"` is a valid string and satisfies the `type = string` constraint
- B) Terraform evaluates `contains(["dev", "staging", "production"], "test")` as `false` and raises a validation error with the `error_message` before planning begins
- C) The plan proceeds and Terraform issues a warning, but does not fail
- D) Terraform evaluates the condition as `true` because `"test"` is not `null`

---

### Question 60 — `can()` and `try()` on a Missing Map Key

**Difficulty**: Medium
**Answer Type**: many
**Topic**: Reading `can()` and `try()` expressions on a map with a missing key to identify TWO correct results

**Question**:
Read this configuration:

```hcl
variable "config" {
  default = {
    timeout = 30
    region  = "us-east-1"
  }
}

locals {
  has_retry  = can(var.config["retry_count"])
  safe_retry = try(var.config["retry_count"], 5)
}
```

Which TWO statements correctly describe the values of `local.has_retry` and `local.safe_retry`? (Select two.)

- A) `local.has_retry` is `false` — `can()` evaluates the expression and returns `false` because accessing a missing key produces an error
- B) `local.has_retry` is `true` — `can()` returns `true` whenever the variable exists, regardless of its keys
- C) `local.safe_retry` is `5` — `try()` evaluates `var.config["retry_count"]`, gets an error because the key is absent, then returns the fallback value `5`
- D) `local.safe_retry` is `null` — `try()` always returns `null` when the primary expression fails

---

### Question 61 — `for_each` Map: Identifying `each.value` for a Named Key

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Reading a `for_each` resource block with a map variable to identify the attribute value for a specific instance

**Question**:
Read this configuration:

```hcl
variable "instance_sizes" {
  default = {
    web = "t3.micro"
    app = "t3.small"
    db  = "t3.medium"
  }
}

resource "aws_instance" "servers" {
  for_each      = var.instance_sizes
  ami           = "ami-0abc123"
  instance_type = each.value

  tags = {
    Name = each.key
  }
}
```

For the resource instance `aws_instance.servers["app"]`, what is the `instance_type` argument's value?

- A) `"t3.micro"` — `each.value` always returns the first value in the map
- B) `"t3.medium"` — `app` maps to the largest instance type
- C) `"t3.small"` — `each.value` for the `"app"` key resolves to `"t3.small"` from `var.instance_sizes`
- D) `each.key` — `instance_type` takes the key name, not the value

---

### Question 62 — `for` Expression with `if` Filter on a Map

**Difficulty**: Hard
**Answer Type**: many
**Topic**: Reading a `for` list expression with an `if` filter on a map to identify TWO correct statements about the result

**Question**:
Read this `locals` block:

```hcl
variable "users" {
  default = {
    alice = "admin"
    bob   = "viewer"
    carol = "admin"
    dave  = "viewer"
  }
}

locals {
  admins = [for name, role in var.users : name if role == "admin"]
}
```

Which TWO statements correctly describe `local.admins`? (Select two.)

- A) `local.admins` is a **list** — the outer `[...]` delimiter produces a list, not a map
- B) `local.admins` is a **map** — the `for` expression iterates over a map input, so the output is also a map
- C) `local.admins` contains exactly two elements: the names of users whose role equals `"admin"`
- D) `local.admins` contains all four user names — the `if` clause is only advisory and does not exclude elements

---

### Question 63 — `for` Expression with `cidrsubnet()` Applied to Index

**Difficulty**: Hard
**Answer Type**: many
**Topic**: Reading a `for` expression that uses `cidrsubnet()` with the element index to identify TWO correct facts about the resulting list

**Question**:
Read this `locals` block:

```hcl
variable "availability_zones" {
  default = ["us-east-1a", "us-east-1b", "us-east-1c"]
}

locals {
  subnet_cidrs = [for idx, az in var.availability_zones : cidrsubnet("10.0.0.0/16", 8, idx)]
}
```

Which TWO statements correctly describe `local.subnet_cidrs`? (Select two.)

- A) `local.subnet_cidrs` is a list of 3 CIDR strings — one for each availability zone
- B) The first element of `local.subnet_cidrs` is `"10.0.1.0/24"` — `idx` starts at 1 for `for` expressions over lists
- C) The third element of `local.subnet_cidrs` is `"10.0.2.0/24"` — `idx` is 2 for the third element, and `cidrsubnet("10.0.0.0/16", 8, 2)` produces that CIDR
- D) `local.subnet_cidrs` is a map keyed by AZ name — iterating a list with `for idx, az in ...` produces a map

---

### Question 64 — `validation` Condition with `startswith()`

**Difficulty**: Easy
**Answer Type**: one
**Topic**: Reading a `validation` block using `startswith()` to identify which value passes the condition

**Question**:
Read this variable declaration:

```hcl
variable "instance_type" {
  type = string

  validation {
    condition     = startswith(var.instance_type, "t3.")
    error_message = "Only t3 family instances are allowed."
  }
}
```

Which value satisfies this `validation` condition?

- A) `"t2.micro"` — starts with `"t"`, which is within the `"t3."` family
- B) `"T3.micro"` — the prefix `"T3."` is equivalent to `"t3."` in Terraform comparisons
- C) `"t3.small"` — the value begins with `"t3."`, satisfying the `startswith()` condition
- D) `"m5.t3.large"` — contains `"t3."` somewhere in the string

---

### Question 65 — `self` Reference in a `postcondition`

**Difficulty**: Easy
**Answer Type**: one
**Topic**: Reading a `postcondition` block to identify what `self` refers to and when the block is evaluated

**Question**:
Read this resource block:

```hcl
resource "aws_instance" "web" {
  ami           = "ami-0abc123"
  instance_type = "t3.micro"

  lifecycle {
    postcondition {
      condition     = self.public_ip != null
      error_message = "Instance must have a public IP address."
    }
  }
}
```

What does `self` refer to inside the `postcondition`, and when is this block evaluated?

- A) `self` refers to the previous state of the instance; the block runs before any changes are applied
- B) `self` refers to the `aws_instance.web` resource after it has been created or updated; the block runs after the resource change completes
- C) `self` refers to the entire Terraform module containing the resource; it is evaluated during `terraform validate`
- D) `self` is a shorthand for `this` and refers to the variable block declaring the resource type

---

### Question 66 — `check` Block `error_message` Interpolation

**Difficulty**: Easy
**Answer Type**: one
**Topic**: Reading a `check` block's interpolated `error_message` to identify the exact message displayed when the assertion fails

**Question**:
Read this `check` block:

```hcl
check "endpoint_healthy" {
  data "http" "probe" {
    url = "https://api.example.com/health"
  }

  assert {
    condition     = data.http.probe.status_code == 200
    error_message = "Health check failed: got ${data.http.probe.status_code}, expected 200."
  }
}
```

The health endpoint returns HTTP status `503`. What does Terraform display?

- A) `"Health check failed: got 503, expected 200."` — the interpolation resolves the actual status code into the message
- B) No message — `check` blocks produce only a generic "assertion failed" notice without custom text
- C) `"Health check failed: got 200, expected 200."` — the message always interpolates the expected value
- D) Terraform raises a fatal error instead of a warning because the endpoint is unreachable

---

### Question 67 — Variable with Two `validation` Blocks

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Reading a variable with two separate `validation` blocks to identify which value satisfies both conditions

**Question**:
Read this variable declaration:

```hcl
variable "port" {
  type = number

  validation {
    condition     = var.port >= 1024
    error_message = "Port must be >= 1024 (unprivileged ports only)."
  }

  validation {
    condition     = var.port <= 65535
    error_message = "Port must be <= 65535."
  }
}
```

Which value satisfies **both** validation conditions?

- A) `80` — a well-known HTTP port
- B) `1023` — one below the unprivileged port boundary
- C) `8080` — an unprivileged port within the valid range
- D) `70000` — above the maximum valid port number

---

### Question 68 — `precondition` Referencing a Data Source Attribute

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Reading a `precondition` that checks a data source attribute to identify when and how it triggers a failure

**Question**:
Read this configuration:

```hcl
data "aws_ami" "ubuntu" {
  most_recent = true
  owners      = ["099720109477"]
}

resource "aws_instance" "web" {
  ami           = data.aws_ami.ubuntu.id
  instance_type = "t3.micro"

  lifecycle {
    precondition {
      condition     = data.aws_ami.ubuntu.architecture == "x86_64"
      error_message = "AMI must be x86_64 architecture, found: ${data.aws_ami.ubuntu.architecture}."
    }
  }
}
```

The data source resolves to an AMI with `architecture = "arm64"`. What happens during `terraform apply`?

- A) The instance is created with `arm64` architecture; Terraform logs a warning about the architecture mismatch
- B) The precondition condition evaluates to `false`; apply halts and `aws_instance.web` is NOT created in AWS
- C) Terraform silently skips the architecture check and creates the instance because the type constraint is satisfied
- D) The plan succeeds but apply pauses for interactive confirmation before creating the instance

---

### Question 69 — `check` Block Without a Scoped Data Source

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Reading a `check` block that uses only an `assert` (no scoped `data` source) to identify its effect on apply

**Question**:
Read this `check` block:

```hcl
check "ha_check" {
  assert {
    condition     = length(aws_autoscaling_group.web.availability_zones) >= 2
    error_message = "Auto-scaling group should span at least 2 AZs for high availability."
  }
}
```

After `terraform apply`, the ASG is created spanning only one availability zone, so `length(aws_autoscaling_group.web.availability_zones)` equals `1`. What does Terraform do?

- A) Apply fails with: "Auto-scaling group should span at least 2 AZs for high availability."
- B) Terraform emits a warning with the `error_message` and completes apply successfully — the ASG is created
- C) Terraform destroys the ASG and recreates it across 2 AZs to satisfy the assertion
- D) The `check` block is ignored because it does not contain a scoped `data` source

---

### Question 70 — Sensitivity Propagation Through `locals` to Two Outputs

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Reading a configuration with two outputs — one referencing a sensitive local and one not — to identify which requires `sensitive = true`

**Question**:
Read this configuration:

```hcl
variable "password" {
  type      = string
  sensitive = true
}

locals {
  greeting = "Hello, infrastructure!"
  db_url   = "postgresql://admin:${var.password}@db.example.com/prod"
}

output "greeting_output" {
  value = local.greeting
}

output "db_url_output" {
  value = local.db_url
}
```

Which output requires `sensitive = true` to be explicitly added, and why?

- A) Both outputs — all values that flow through `locals` must be marked sensitive in their outputs
- B) Neither output — `sensitive = true` on the `password` variable is sufficient to protect it everywhere
- C) Only `db_url_output` — `local.db_url` interpolates the sensitive variable, making it sensitive; `local.greeting` does not reference any sensitive value
- D) Only `greeting_output` — it is the non-sensitive output and must be explicitly marked to prevent accidental exposure

---

### Question 71 — Lifecycle Block with Both `precondition` and `postcondition`

**Difficulty**: Medium
**Answer Type**: many
**Topic**: Reading a lifecycle block with both condition types to identify TWO correct statements about their timing

**Question**:
Read this resource block:

```hcl
resource "aws_db_instance" "prod" {
  identifier     = "prod-db"
  engine         = "postgres"
  instance_class = var.db_instance_class

  lifecycle {
    precondition {
      condition     = var.db_instance_class != "db.t3.micro"
      error_message = "Production databases must not use db.t3.micro."
    }

    postcondition {
      condition     = self.endpoint != ""
      error_message = "Database did not receive a valid endpoint."
    }
  }
}
```

Which TWO statements correctly describe when each condition is evaluated? (Select two.)

- A) The `precondition` is evaluated before `aws_db_instance.prod` is created or modified in AWS
- B) The `postcondition` is evaluated at the same time as the `precondition`, before the database is created
- C) If `var.db_instance_class` is `"db.t3.micro"`, the `precondition` fails and the database is never created
- D) `self.endpoint` in the `postcondition` refers to the endpoint from the previous state, not the newly provisioned instance

---

### Question 72 — Sensitive Variable Through `local` to Resource Argument

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Reading a sensitive variable referenced in a `locals` interpolation used as a resource argument — identifying what `terraform plan` shows

**Question**:
Read this configuration:

```hcl
variable "api_secret" {
  type      = string
  sensitive = true
}

locals {
  connection_string = "Server=db.example.com;Password=${var.api_secret}"
}

resource "aws_ssm_parameter" "conn" {
  name  = "/app/connection_string"
  type  = "SecureString"
  value = local.connection_string
}
```

What does `terraform plan` display for the `value` argument of `aws_ssm_parameter.conn`?

- A) The full connection string with the actual password substituted in plaintext
- B) `(sensitive value)` — the local interpolates a sensitive variable, so the result is also treated as sensitive
- C) `"Server=db.example.com;Password=(sensitive value)"` — Terraform partially redacts only the sensitive portion
- D) An error — locals cannot interpolate sensitive variables; they must be referenced directly in resource arguments

---

### Question 73 — `validation` with `&&` — Identifying Values That Pass

**Difficulty**: Medium
**Answer Type**: many
**Topic**: Reading a `validation` block with a compound `&&` condition to identify TWO values that satisfy both sub-conditions

**Question**:
Read this variable declaration:

```hcl
variable "cidr_block" {
  type = string

  validation {
    condition     = startswith(var.cidr_block, "10.") && length(split(".", var.cidr_block)) == 4
    error_message = "Must start with 10. and have exactly 4 dot-separated segments."
  }
}
```

Which TWO values satisfy **both** parts of the `&&` condition? (Select two.)

- A) `"10.0.0.0/16"` — starts with `"10."` and `split(".", "10.0.0.0/16")` produces 4 segments
- B) `"192.168.1.0/24"` — standard private CIDR
- C) `"10.0.1.0"` — starts with `"10."` and `split(".", "10.0.1.0")` produces 4 segments
- D) `"10.0.0"` — starts with `"10."` but only 3 dot-separated segments

---

### Question 74 — `precondition` with `can(regex())` Pattern

**Difficulty**: Hard
**Answer Type**: one
**Topic**: Reading a `precondition` that uses `can(regex())` to validate a data source attribute format

**Question**:
Read this resource block:

```hcl
data "aws_ami" "ubuntu" {
  most_recent = true
  owners      = ["099720109477"]
}

resource "aws_instance" "web" {
  ami           = data.aws_ami.ubuntu.id
  instance_type = "t3.micro"

  lifecycle {
    precondition {
      condition     = can(regex("^ami-[0-9a-f]{8,17}$", data.aws_ami.ubuntu.id))
      error_message = "AMI ID must match the format ami-xxxxxxxx (8-17 hex chars)."
    }
  }
}
```

What does this `precondition` check, and what is the effect of using `can()` around `regex()`?

- A) It validates the `ami` input variable format before planning; `can()` makes the check optional so it never blocks
- B) It checks that the AMI ID returned by the data source matches the expected `ami-xxxxxxxx` format before the instance is created; `can()` catches a regex error (e.g., if the AMI ID is null) and returns `false` instead of propagating the error
- C) It runs after the instance is created and inspects `self.ami`; `can()` is required to access `self` attributes safely
- D) It runs during `terraform validate` and does not require provider credentials; `can()` provides the null-safety needed for offline validation

---

### Question 75 — Three Condition Mechanisms for `var.env = "dev"`

**Difficulty**: Hard
**Answer Type**: many
**Topic**: Reading three parallel snippets — one `validation`, one `precondition`, one `check` — to identify TWO correct statements when the variable value is `"dev"`

**Question**:
Read these three configuration snippets. Assume `var.env = "dev"` is provided.

```hcl
# Snippet 1 — validation block
variable "env" {
  type = string
  validation {
    condition     = contains(["dev", "prod"], var.env)
    error_message = "env must be dev or prod."
  }
}

# Snippet 2 — resource precondition
resource "aws_instance" "web" {
  ami           = "ami-0abc123"
  instance_type = "t3.micro"

  lifecycle {
    precondition {
      condition     = var.env == "prod"
      error_message = "This resource may only be created in the prod environment."
    }
  }
}

# Snippet 3 — check block
check "env_check" {
  assert {
    condition     = var.env != ""
    error_message = "env must not be empty."
  }
}
```

With `var.env = "dev"`, which TWO statements correctly describe Terraform's behaviour? (Select two.)

- A) Snippet 1's `validation` passes — `"dev"` is in `["dev", "prod"]`, so the condition is `true`
- B) Snippet 2's `precondition` passes — `var.env` has a value, and preconditions only fail when the variable is `null`
- C) Snippet 2's `precondition` fails — `"dev" == "prod"` is `false`; apply halts before `aws_instance.web` is created
- D) Snippet 3's `check` block fails — `"dev" != ""` is `false`, so a warning is emitted

---

### Question 76 — S3 Backend `encrypt = true`

**Difficulty**: Easy
**Answer Type**: one
**Topic**: Reading an S3 backend block to identify what `encrypt = true` protects

**Question**:
Read this backend configuration:

```hcl
terraform {
  backend "s3" {
    bucket         = "acme-tf-state"
    key            = "production/terraform.tfstate"
    region         = "us-east-1"
    dynamodb_table = "terraform-locks"
    encrypt        = true
  }
}
```

What does the `encrypt = true` argument configure?

- A) It enables TLS encryption for the network connection between Terraform and S3 — required to prevent data interception in transit
- B) It instructs Terraform to encrypt the state file in memory before writing it; the object stored in S3 remains plaintext
- C) It enables server-side encryption (SSE) on the state object stored in S3, so the file is encrypted at rest in the bucket
- D) It generates and rotates a local encryption key stored in `.terraform/` that wraps all sensitive values

---

### Question 77 — Module Source Git `?ref=` Query Parameter

**Difficulty**: Easy
**Answer Type**: one
**Topic**: Reading a Git-based module source URL to identify what `?ref=v2.0.0` pins

**Question**:
Read this module block:

```hcl
module "vpc" {
  source = "git::https://github.com/acme/terraform-modules.git//modules/vpc?ref=v2.0.0"
}
```

What does the `?ref=v2.0.0` query parameter specify?

- A) It specifies the subdirectory within the repository to use as the module root — equivalent to the `//` separator
- B) It sets a registry version constraint equivalent to `version = "~> 2.0"` for the module
- C) It pins the module source to the `v2.0.0` git ref — which may be a tag, branch name, or commit SHA
- D) It instructs `terraform init` to validate that a GitHub Release named `v2.0.0` exists before downloading

---

### Question 78 — Module Output Reference with List Index

**Difficulty**: Easy
**Answer Type**: one
**Topic**: Reading a root module resource that indexes a child module's list output

**Question**:
Read this configuration:

```hcl
# modules/networking/outputs.tf
output "public_subnet_ids" {
  value = aws_subnet.public[*].id
}

# root main.tf
resource "aws_instance" "web" {
  ami       = "ami-0abc123"
  subnet_id = module.networking.public_subnet_ids[0]
}
```

What does `module.networking.public_subnet_ids[0]` evaluate to?

- A) The integer `0` — the index is returned as a number when applied to a module output reference
- B) The first element of the `public_subnet_ids` list output from the `networking` module — the subnet ID string of the first public subnet
- C) The entire `public_subnet_ids` list — the `[0]` notation on a module output selects the full output, not a single element
- D) An error — module output references cannot be indexed with `[0]`; the full list must be assigned to a local first

---

### Question 79 — DynamoDB Lock Table `hash_key = "LockID"`

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Reading a DynamoDB table resource for Terraform state locking to identify why `hash_key` must be `"LockID"`

**Question**:
Read this DynamoDB table resource, which will be used for Terraform state locking with an S3 backend:

```hcl
resource "aws_dynamodb_table" "tf_locks" {
  name         = "my-terraform-state-locks"
  billing_mode = "PAY_PER_REQUEST"
  hash_key     = "LockID"

  attribute {
    name = "LockID"
    type = "S"
  }
}
```

Why must `hash_key` be set to exactly `"LockID"`, and not any other name?

- A) `"LockID"` is a DynamoDB-reserved keyword that automatically enables TTL expiry for abandoned lock items
- B) The Terraform S3 backend hardcodes the partition key attribute name `"LockID"` when writing and reading lock records — using any other name causes locking to fail
- C) `"LockID"` is required by the DynamoDB service API for all tables that will be accessed by AWS SDKs
- D) The value `"LockID"` is stored as the item value and must match the S3 bucket name in the backend block

---

### Question 80 — Module `for_each` Map — Instance Addresses

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Reading a module block with `for_each` on a map to identify the state addresses of the two instances

**Question**:
Read this module block:

```hcl
module "vpc" {
  for_each = {
    production = "10.0.0.0/16"
    staging    = "10.1.0.0/16"
  }

  source   = "./modules/vpc"
  vpc_cidr = each.value
  env_name = each.key
}
```

What are the state addresses for the two module instances?

- A) `module.vpc[0]` and `module.vpc[1]` — `for_each` on a map uses zero-based numeric indices for module addressing
- B) `module.vpc["production"]` and `module.vpc["staging"]` — `for_each` uses the map keys as instance identifiers in bracket notation
- C) `module.production` and `module.staging` — the map key replaces the module block label in state
- D) `module.vpc.production` and `module.vpc.staging` — dot notation is used for map-keyed module instances

---

### Question 81 — S3 Backend `key` Argument

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Reading an S3 backend block to identify what the `key` argument specifies

**Question**:
Read this backend configuration:

```hcl
terraform {
  backend "s3" {
    bucket = "acme-company-tfstate"
    key    = "environments/production/networking.tfstate"
    region = "us-east-1"
  }
}
```

What does the `key` argument specify?

- A) The AWS IAM access key ID used to authenticate Terraform's API calls to S3
- B) The name of the S3 bucket — it is an alias for the `bucket` argument
- C) The S3 object key (path and filename within the bucket) where Terraform writes and reads the state file
- D) The KMS key ID for server-side encryption — required when the bucket enforces SSE-KMS

---

### Question 82 — Module `count = 2` — Instance Addresses and `count.index`

**Difficulty**: Medium
**Answer Type**: many
**Topic**: Reading a module block with `count = 2` to identify TWO correct statements about instance addressing and `count.index`

**Question**:
Read this module block:

```hcl
module "web_server" {
  count         = 2
  source        = "./modules/web-server"
  ami           = "ami-0abc123"
  instance_name = "web-${count.index}"
}
```

Which TWO statements correctly describe the instances created by this `count = 2` module block? (Select two.)

- A) The two instances are addressed as `module.web_server[0]` and `module.web_server[1]` in the Terraform state
- B) The two instances are addressed as `module.web_server_0` and `module.web_server_1` — underscores replace brackets for count-indexed modules
- C) Inside the `module` block, `count.index` is available in argument expressions such as `"web-${count.index}"`, evaluating to `0` for the first instance and `1` for the second
- D) `count.index` is not usable within a `module` block — it is only valid inside `resource` blocks

---

### Question 83 — Module `depends_on` Argument

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Reading a module block with `depends_on` to identify what dependency it creates

**Question**:
Read this configuration:

```hcl
resource "aws_iam_role_policy_attachment" "lambda_logs" {
  role       = aws_iam_role.lambda.name
  policy_arn = "arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole"
}

module "lambda_function" {
  source        = "./modules/lambda"
  function_name = "data-processor"
  role_arn      = aws_iam_role.lambda.arn

  depends_on = [aws_iam_role_policy_attachment.lambda_logs]
}
```

What does `depends_on = [aws_iam_role_policy_attachment.lambda_logs]` achieve in this `module` block?

- A) It imports `aws_iam_role_policy_attachment.lambda_logs` into the module's state scope
- B) It creates an explicit dependency edge ensuring that `aws_iam_role_policy_attachment.lambda_logs` is fully applied before any resource inside `module.lambda_function` is created
- C) It applies the dependency only to the first resource declared inside the module — subsequent module resources still run in parallel with the policy attachment
- D) It is redundant because Terraform already infers this dependency from the `role_arn = aws_iam_role.lambda.arn` attribute reference

---

### Question 84 — Missing Required Variable in Module Call

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Reading a child module's `variables.tf` alongside a root module call to identify which required input is missing

**Question**:
Read this configuration:

```hcl
# ./modules/database/variables.tf
variable "db_name"       { type = string }
variable "db_username"   { type = string }
variable "db_password"   { type = string }
variable "instance_class" {
  type    = string
  default = "db.t3.micro"
}

# root main.tf
module "database" {
  source      = "./modules/database"
  db_name     = "appdb"
  db_username = "admin"
}
```

What error does `terraform plan` produce with this configuration?

- A) A warning is displayed advising the team to supply `db_password`, but the plan proceeds
- B) Terraform generates the plan with `db_password = null` because variables without a passed value default to `null`
- C) Terraform raises an error because the required input variable `db_password` has no value — it has no default and is not passed in the `module` block
- D) Terraform raises an error because `instance_class` is not passed — all module variables must be explicitly provided

---

### Question 85 — `terraform state list` Output — Module Resource Address Format

**Difficulty**: Medium
**Answer Type**: many
**Topic**: Reading `terraform state list` output to identify TWO correct statements about module resource address format

**Question**:
Read this `terraform state list` output:

```
aws_security_group.web
module.vpc.aws_vpc.main
module.vpc.aws_subnet.public[0]
module.vpc.aws_subnet.public[1]
module.vpc.module.nat.aws_eip.nat
```

Which TWO statements correctly describe what this output reveals about the configuration? (Select two.)

- A) `module.vpc.aws_vpc.main` identifies an `aws_vpc` resource named `main` that is managed inside the `vpc` child module
- B) `module.vpc.module.nat.aws_eip.nat` indicates a module named `nat` is nested inside the `vpc` module, and that nested module manages an `aws_eip` resource named `nat`
- C) `aws_security_group.web` is managed by a child module — the absence of a `module.` prefix means Terraform omitted the module path for brevity
- D) `module.vpc.aws_subnet.public[0]` and `module.vpc.aws_subnet.public[1]` are two separate modules with numeric labels

---

### Question 86 — `version = "~> 5.0"` Registry Constraint Range

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Reading a registry module block to identify the version range allowed by the `~>` pessimistic constraint operator

**Question**:
Read this module block:

```hcl
module "vpc" {
  source  = "terraform-aws-modules/vpc/aws"
  version = "~> 5.0"
}
```

What range of module versions does `"~> 5.0"` allow `terraform init` to select?

- A) Exactly version `5.0.0` only — the `~>` operator pins to an exact version
- B) Any version `>= 5.0` with no upper bound — including `6.0`, `7.0`, and beyond
- C) Any version `>= 5.0` and `< 6.0` — the `~>` operator locks the major version and allows the minor to increment freely
- D) Any version `>= 5.0.0` and `< 5.1.0` — the constraint only allows patch releases within `5.0.x`

---

### Question 87 — Module `providers` Argument with Provider Aliases

**Difficulty**: Hard
**Answer Type**: one
**Topic**: Reading a module block with a `providers` map to identify what provider alias mapping achieves

**Question**:
Read this root module configuration:

```hcl
provider "aws" {
  alias  = "primary"
  region = "us-east-1"
}

provider "aws" {
  alias  = "secondary"
  region = "eu-west-1"
}

module "us_resources" {
  source = "./modules/regional"

  providers = {
    aws = aws.primary
  }
}

module "eu_resources" {
  source = "./modules/regional"

  providers = {
    aws = aws.secondary
  }
}
```

What does the `providers` argument in each `module` block achieve?

- A) It declares version constraints the module is allowed to use — overriding the root module's `required_providers` block
- B) It maps root-module provider aliases to the provider configuration each child module instance will use — enabling the same module source to deploy to different regions
- C) It creates a new isolated provider instance scoped only to that module — the root module loses access to the provider credentials passed to the child
- D) It is required for all module blocks — without a `providers` argument, child modules cannot access any provider configuration

---

### Question 88 — Nested Module Variable Passing Chain

**Difficulty**: Hard
**Answer Type**: many
**Topic**: Reading a root → child → grandchild module chain to identify TWO correct statements about required explicit variable passing

**Question**:
Read this three-level module configuration:

```hcl
# root main.tf
variable "env" { default = "prod" }

module "app" {
  source = "./modules/app"
  env    = var.env
}

# modules/app/main.tf
variable "env" {}

module "db" {
  source = "./modules/db"
  # env is NOT passed here
}

# modules/db/variables.tf
variable "env" {}   # no default
```

Which TWO statements correctly describe the outcome of running `terraform plan`? (Select two.)

- A) `module.app.module.db` inherits `var.env` from `module.app` automatically — variables propagate down nested module chains
- B) Terraform raises an error because `variable "env"` in `./modules/db/variables.tf` has no default and is not passed by the `module "db"` block in `modules/app/main.tf`
- C) The value `"prod"` flows from the root through `module.app` into `module.db` as a module-scope global because all three declare a `variable "env"` with the same name
- D) To resolve the error, the `module "db"` block inside `modules/app/main.tf` must explicitly pass `env = var.env`, where `var.env` refers to the `env` input of `modules/app`

---

### Question 89 — `import` Block `to` Argument

**Difficulty**: Easy
**Answer Type**: one
**Topic**: Reading an `import` block to identify what the `to` argument specifies

**Question**:
Read this `import` block:

```hcl
import {
  to = aws_s3_bucket.media_assets
  id = "company-media-assets-2024"
}
```

What does the `to` argument specify?

- A) The S3 bucket name in AWS — `to` is an alias for the `id` argument that accepts human-readable names
- B) The Terraform resource address (type and label) that will manage the existing cloud resource once the import completes
- C) The destination file path where Terraform writes the generated HCL configuration for the imported resource
- D) The key path within the state file where the imported resource will be stored

---

### Question 90 — `terraform show plan.tfplan`

**Difficulty**: Easy
**Answer Type**: one
**Topic**: Reading a two-command sequence to identify what `terraform show plan.tfplan` renders

**Question**:
Read this command sequence:

```bash
terraform plan -out=plan.tfplan
terraform show plan.tfplan
```

What does the second command render?

- A) A JSON document of the entire current state file, filtered to only the resources affected by the plan
- B) A summary of the most recent `terraform apply` output, sourced from the local operation log
- C) A human-readable view of the saved execution plan in `plan.tfplan`, showing the proposed creates, updates, and destroys
- D) An error — `terraform show` can only read the current state file and does not accept a plan file as an argument

---

### Question 91 — `TF_LOG=WARN` Message Filtering

**Difficulty**: Easy
**Answer Type**: one
**Topic**: Reading a shell snippet with `TF_LOG=WARN` to identify which log messages appear

**Question**:
Read this shell snippet:

```bash
export TF_LOG=WARN
terraform apply
```

Which log messages does setting `TF_LOG=WARN` produce during the apply?

- A) WARN-level messages only — messages at all other levels are suppressed
- B) WARN and ERROR messages — the log level acts as a minimum severity threshold
- C) INFO, WARN, and ERROR messages — WARN is a mid-level filter that includes less-verbose levels above it
- D) All log levels — WARN enables logging but does not filter by severity

---

### Question 92 — `terraform plan -generate-config-out` Produced File

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Reading a generated resource block to identify which workflow step produced it

**Question**:
Read this file:

```hcl
# generated.tf
# __generated__ by Terraform
# Please review these resources and move them into your main configuration files.

resource "aws_s3_bucket" "legacy_assets" {
  bucket              = "my-existing-bucket-2024"
  bucket_prefix       = null
  force_destroy       = null
  object_lock_enabled = false
  tags                = {}
  tags_all            = {}
}
```

Which command produced this file, and under what conditions?

- A) `terraform apply` — Terraform generates a record of newly created resources in a companion file after each apply
- B) `terraform plan -generate-config-out=generated.tf` — run after adding an `import` block for a resource that had no existing HCL configuration
- C) `terraform state show aws_s3_bucket.legacy_assets > generated.tf` — the state show output was redirected into a file
- D) `terraform init` — provider initialisation generates scaffold configuration files for each resource type the provider supports

---

### Question 93 — `cloud` Block with `tags` Workspace Selector

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Reading a `cloud` block with a `tags` array to identify which HCP Terraform workspaces it selects

**Question**:
Read this `cloud` block:

```hcl
terraform {
  cloud {
    organization = "acme-corp"

    workspaces {
      tags = ["component=networking", "env=production"]
    }
  }
}
```

Which workspaces in the `acme-corp` organisation does this configuration connect to?

- A) All workspaces in the organisation — tags are stored as metadata but do not filter which workspace is selected
- B) Any workspace that has AT LEAST ONE of the listed tags: either `component=networking` OR `env=production`
- C) Any workspace that has ALL of the listed tags: both `component=networking` AND `env=production`
- D) Only the workspace whose name matches the first tag value: `"component=networking"`

---

### Question 94 — `terraform_remote_state` Output Reference Value

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Reading a `terraform_remote_state` data source and root output to identify the evaluated value

**Question**:
Read this configuration:

```hcl
data "terraform_remote_state" "networking" {
  backend = "remote"
  config = {
    organization = "my-org"
    workspaces = {
      name = "networking-production"
    }
  }
}

output "app_subnet" {
  value = data.terraform_remote_state.networking.outputs.private_subnet_id
}
```

The `networking-production` workspace has this output declared and applied:

```hcl
output "private_subnet_id" {
  value = "subnet-0abc123def456"
}
```

What is the value of `output.app_subnet`?

- A) The entire `outputs` map from the remote state — the `.private_subnet_id` suffix selects a key within the map but is evaluated at apply time only
- B) `"subnet-0abc123def456"` — the string value of the `private_subnet_id` output from the remote workspace
- C) The ARN of the subnet — `terraform_remote_state` resolves subnet IDs to ARNs automatically
- D) `null` — cross-workspace remote state output references always evaluate to null during the first plan

---

### Question 95 — `TF_LOG_PROVIDER=TRACE` Without `TF_LOG`

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Reading a shell snippet with only `TF_LOG_PROVIDER` set to identify the resulting log output

**Question**:
Read this shell snippet:

```bash
export TF_LOG_PROVIDER=TRACE
# TF_LOG is NOT set
terraform apply
```

What logging does Terraform produce?

- A) No logging — `TF_LOG` must be set to any level for any logging to occur; `TF_LOG_PROVIDER` has no effect without it
- B) TRACE-level logs for provider plugins only; Terraform core produces no logs
- C) TRACE-level logs for all components — setting `TF_LOG_PROVIDER=TRACE` implicitly enables `TF_LOG=TRACE` for core as well
- D) An error is raised — `TF_LOG_PROVIDER` requires `TF_LOG` to be configured first to establish a baseline level

---

### Question 96 — Sentinel Policy Snippet Interpretation

**Difficulty**: Medium
**Answer Type**: many
**Topic**: Reading a Sentinel policy to identify TWO correct statements about what it enforces and its override behaviour

**Question**:
Read this Sentinel policy, assigned at the `soft-mandatory` enforcement level:

```python
import "tfplan/v2" as tfplan

all_resources = filter tfplan.resource_changes as _, rc {
  rc.change.actions is not ["no-op"]
}

untagged = filter all_resources as _, r {
  not (r.change.after.tags else null) != null
}

main = rule {
  length(untagged) == 0
}
```

Which TWO statements correctly describe this policy? (Select two.)

- A) The `main` rule evaluates to `true` (passes) when every resource being modified has a non-null `tags` attribute — that is, when `untagged` is empty
- B) If a resource has `tags` explicitly set to an empty map `{}`, it is added to the `untagged` collection and causes a policy failure
- C) A policy failure at `soft-mandatory` can be overridden by a user who has the "Manage Policy Overrides" permission, allowing the run to proceed
- D) If the `main` rule returns `false`, the run is blocked and cannot proceed under any circumstances regardless of user permissions

---

### Question 97 — `workspaces.name` vs `workspaces.tags` in `cloud` Block

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Reading two `cloud` block variants to identify the key behavioral difference between name and tags selectors

**Question**:
Read both configurations:

```hcl
# Config A
terraform {
  cloud {
    organization = "my-org"
    workspaces {
      name = "production"
    }
  }
}
```

```hcl
# Config B
terraform {
  cloud {
    organization = "my-org"
    workspaces {
      tags = ["env=production"]
    }
  }
}
```

What is the key behavioral difference between Config A and Config B?

- A) Config A connects this configuration directory to exactly one workspace named `"production"`; Config B allows the configuration to be used with any workspace in `my-org` tagged with `env=production`
- B) Config A creates the `production` workspace automatically if it does not exist; Config B only connects to workspaces that already exist and carry the specified tag
- C) Both configurations connect to the same workspace — `name = "production"` and `tags = ["env=production"]` are equivalent expressions when the workspace name matches the tag value
- D) Config B connects to the HCP Terraform default workspace; `tags` is a UI display filter and not a workspace selector

---

### Question 98 — `import` Block vs CLI Import Differences

**Difficulty**: Medium
**Answer Type**: many
**Topic**: Reading an `import` block and a CLI import command side-by-side to identify TWO structural differences

**Question**:
Read both import approaches for the same resource:

```hcl
# Method A — import block (Terraform 1.5+)
import {
  to = aws_instance.app
  id = "i-0abc1234567890"
}
```

```bash
# Method B — CLI import (legacy)
terraform import aws_instance.app i-0abc1234567890
```

Which TWO statements correctly describe a difference between Method A and Method B? (Select two.)

- A) Method A can be previewed with `terraform plan` before any state changes are made; Method B immediately writes to state when the command runs, with no plan preview
- B) Method A can optionally generate the HCL resource configuration using `terraform plan -generate-config-out=file.tf`; Method B only writes to state and never produces HCL configuration
- C) Method A requires a pre-existing `resource "aws_instance" "app"` block just like Method B — both methods require the resource block to already exist
- D) Method A and Method B produce identical results in every way — the `import` block is simply a declarative wrapper around the same imperative operation

---

### Question 99 — `TF_TOKEN_app_terraform_io` vs `terraform login`

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Reading a CI/CD env-var authentication snippet to identify what it achieves and why it is preferred over `terraform login`

**Question**:
Read this CI/CD pipeline configuration snippet:

```bash
export TF_TOKEN_app_terraform_io="<hcp-terraform-api-token>"
terraform init
terraform plan
```

What does setting `TF_TOKEN_app_terraform_io` achieve, and why is it preferred over `terraform login` in this context?

- A) It is functionally identical to `terraform login` — both approaches store the token in `~/.terraform.d/credentials.tfrc.json` for use by subsequent Terraform commands
- B) It provides authentication to HCP Terraform via an environment variable, avoiding the need to store a token file on disk — the recommended approach for CI/CD pipelines where no persistent home directory exists
- C) It sets a short-lived session token scoped to the current shell; `terraform login` generates a longer-lived token with broader permissions
- D) The variable is consumed only by `terraform init`; subsequent `plan` and `apply` commands require re-exporting the variable in separate shell steps

---

### Question 100 — `hard-mandatory` Sentinel Policy Override Attempt by Owner

**Difficulty**: Hard
**Answer Type**: one
**Topic**: Reading a `hard-mandatory` Sentinel policy and identifying what happens when an Owner tries to override the failure

**Question**:
Read this Sentinel policy metadata and code fragment:

```
# Policy: require-s3-encryption.sentinel
# Enforcement level: hard-mandatory

main = rule {
  length(unencrypted_buckets) == 0
}
```

An engineer creates an `aws_s3_bucket` without encryption. The `main` rule evaluates to `false`. An organisation Owner attempts to use the HCP Terraform UI override button to allow the run to proceed. What happens?

- A) The override succeeds — Owners have unrestricted access and can override any policy failure regardless of enforcement level
- B) The override button is visible but is disabled with a tooltip explaining that `hard-mandatory` policies cannot be overridden via the UI
- C) There is no override option presented in the HCP Terraform UI — `hard-mandatory` policies display the failure with no mechanism to proceed
- D) The override succeeds only if the Owner is also a member of the team that manages the failing policy set

---

### Question 101 — Three Logging Variables in Combination

**Difficulty**: Hard
**Answer Type**: many
**Topic**: Reading a shell snippet with `TF_LOG`, `TF_LOG_CORE`, `TF_LOG_PROVIDER`, and `TF_LOG_PATH` all set to identify TWO correct outcomes

**Question**:
Read this shell snippet:

```bash
export TF_LOG=TRACE
export TF_LOG_CORE=ERROR
export TF_LOG_PROVIDER=DEBUG
export TF_LOG_PATH=/var/log/terraform.log
terraform apply
```

Which TWO statements correctly describe the resulting logging behaviour? (Select two.)

- A) All log output is written to `/var/log/terraform.log` rather than stderr
- B) Terraform core logs appear at TRACE level — the global `TF_LOG=TRACE` takes precedence over `TF_LOG_CORE=ERROR` for core components
- C) Terraform core logs appear at ERROR level only — `TF_LOG_CORE=ERROR` overrides the global `TF_LOG=TRACE` for core components
- D) Provider plugin logs appear at TRACE level — the global `TF_LOG=TRACE` overrides `TF_LOG_PROVIDER=DEBUG` for provider components



## Answer Key

| Q# | Answer(s) | Explanation | Source | Difficulty |
|---|---|---|---|---|
| 2 | B | N/A | Reading a `count` argument to determine how many state resource addresses Terraform tracks | Easy |
| 3 | B | N/A | Interpreting what `count = 0` means for a resource block | Easy |
| 4 | C | N/A | Classifying HCL vs shell script by the IaC approach each represents | Medium |
| 5 | B | N/A | Reading a multi-cloud config and identifying how many provider plugins are required | Medium |
| 6 | C | N/A | Interpreting an apply summary line to confirm idempotent behaviour | Medium |
| 7 | B, C | N/A | Reading a provider block list and identifying correct claims about each tool's cloud scope | Medium |
| 8 | C | N/A | Interpreting a configuration file as living documentation of infrastructure | Medium |
| 9 | B | N/A | Identifying whether a snippet represents a config management tool or a provisioning tool | Medium |
| 10 | C | N/A | Interpreting what a Git log of `.tf` file changes provides as an IaC benefit | Medium |
| 11 | C | N/A | Interpreting a snippet that declares both AWS and Azure resources to identify which tool it must be written in | Hard |
| 12 | A, D | N/A | Reading a state-vs-actual comparison and identifying which attributes represent drift | Hard |
| 13 | B | N/A | What the pessimistic constraint operator `~> 5.0` permits | Easy |
| 14 | B | N/A | How Terraform resolves a two-part provider source address to its fully qualified form | Easy |
| 15 | B | N/A | What `sensitive = true` does and does not protect in Terraform | Easy |
| 16 | C | N/A | Distinguishing patch-only from minor+patch constraints using `~>` | Medium |
| 17 | B | N/A | Which provider configuration is used by a resource that omits the `provider` argument | Medium |
| 18 | B | N/A | What the `hashes` entries in `.terraform.lock.hcl` provide | Medium |
| 19 | C | N/A | Identifying which field in `terraform.tfstate` links the config address to the real cloud resource | Medium |
| 20 | B | N/A | What `provider = aws.west` on a resource block instructs Terraform to do | Medium |
| 21 | A, B | N/A | What two pieces of information `.terraform.lock.hcl` records per provider | Medium |
| 22 | B | N/A | What the `!=` version constraint operator excludes | Medium |
| 23 | A, B | N/A | Interpreting a state JSON excerpt to identify what `terraform state show` returns | Medium |
| 24 | A, C | N/A | Identifying the precise version ranges permitted by two different pessimistic constraints | Hard |
| 25 | B | N/A | What fields change in `.terraform.lock.hcl` when a newer provider version is installed via `-upgrade` | Hard |
| 26 | B | N/A | Reading plan output symbols to identify which resource will be created without a corresponding destruction | Easy |
| 27 | B | N/A | Reading a `terraform console` REPL expression to identify the return value | Easy |
| 28 | C | N/A | Identifying the currently active workspace from `terraform workspace list` output | Easy |
| 29 | C | N/A | Reading a plan resource block with the `-/+` replace symbol to identify what Terraform will do | Medium |
| 30 | C | N/A | Identifying which `terraform output` flag produces structured JSON with type metadata | Medium |
| 31 | A, C | N/A | Reading two `terraform fmt` flag invocations and identifying what each does | Medium |
| 32 | B | N/A | Identifying what `terraform show` displays when given a saved plan file | Medium |
| 33 | C | N/A | Reading a `terraform plan -var` command to identify which value `var.instance_type` takes | Medium |
| 34 | B, C | N/A | Reading a `~` plan block to identify which statements correctly describe the operation | Medium |
| 35 | A | N/A | Reading a backend block addition and identifying which `terraform init` flag copies existing state to the new backend | Medium |
| 36 | D | N/A | Identifying the effect of combining `-auto-approve` with a saved plan file argument | Medium |
| 37 | A, C | N/A | Interpreting a plan summary line where all changes are `-/+` replacements | Hard |
| 38 | C | N/A | Identifying what plan symbol appears for a resource targeted by `terraform apply -replace` when the configuration is unchanged | Hard |
| 39 | B | N/A | Reading a `lifecycle` block to identify the order of destroy and create during a forced replacement | Easy |
| 40 | B | N/A | Identifying which expression references a data source vs a managed resource attribute | Easy |
| 41 | C | N/A | Identifying which state address Terraform uses after a `moved` block is applied | Easy |
| 42 | C | N/A | Reading a three-resource configuration to identify which resource is created last and why | Medium |
| 43 | B | N/A | Reading a plan output for a resource whose changed attribute is listed in `ignore_changes` | Medium |
| 44 | B | N/A | Reading a `removed` block to identify the effect on the real cloud resource | Medium |
| 45 | B | N/A | Reading a `depends_on` list to identify which resource Terraform is guaranteed to apply first | Medium |
| 46 | B | N/A | Reading a `replace_triggered_by` referencing an attribute vs an entire resource | Medium |
| 47 | B | N/A | Reading a `terraform apply -parallelism` flag to identify its effect on execution | Medium |
| 48 | A, C | N/A | Reading a lifecycle block with three arguments to identify TWO correct behavioural statements | Medium |
| 49 | A, C | N/A | Reading a data source block and its consumer resource to identify TWO correct statements | Medium |
| 50 | B | N/A | Reading a multi-resource configuration to identify which resources run concurrently and which must wait | Hard |
| 51 | A, C | N/A | Reading a `moved` block that relocates a resource from root module into a child module | Hard |
| 52 | C | N/A | Reading a `locals` block with interpolation to identify the computed string value | Easy |
| 53 | B | N/A | Identifying the output type of a `for` expression based on its outer delimiters | Easy |
| 54 | B | N/A | Reading a `zipmap()` call to identify the resulting map | Easy |
| 55 | B | N/A | Identifying the correct attribute reference inside a `dynamic` block that uses a custom `iterator` name | Medium |
| 56 | B | N/A | Reading a map `for` expression that transforms keys to identify the resulting map content | Medium |
| 57 | B | N/A | Reading a `cidrhost()` call to identify the resulting IP address | Medium |
| 58 | A | N/A | Reading a `concat()` call to identify the resulting list | Medium |
| 59 | B | N/A | Reading a `jsonencode()` call to identify the type and structure of the output | Medium |
| 60 | B | N/A | Reading a `validation` block to determine whether a given input value passes or fails | Medium |
| 61 | A, C | N/A | Reading `can()` and `try()` expressions on a map with a missing key to identify TWO correct results | Medium |
| 62 | C | N/A | Reading a `for_each` resource block with a map variable to identify the attribute value for a specific instance | Medium |
| 63 | A, C | N/A | Reading a `for` list expression with an `if` filter on a map to identify TWO correct statements about the result | Hard |
| 64 | A, C | N/A | Reading a `for` expression that uses `cidrsubnet()` with the element index to identify TWO correct facts about the resulting list | Hard |
| 65 | C | N/A | Reading a `validation` block using `startswith()` to identify which value passes the condition | Easy |
| 66 | B | N/A | Reading a `postcondition` block to identify what `self` refers to and when the block is evaluated | Easy |
| 67 | A | N/A | Reading a `check` block's interpolated `error_message` to identify the exact message displayed when the assertion fails | Easy |
| 68 | C | N/A | Reading a variable with two separate `validation` blocks to identify which value satisfies both conditions | Medium |
| 69 | B | N/A | Reading a `precondition` that checks a data source attribute to identify when and how it triggers a failure | Medium |
| 70 | B | N/A | Reading a `check` block that uses only an `assert` (no scoped `data` source) to identify its effect on apply | Medium |
| 71 | C | N/A | Reading a configuration with two outputs — one referencing a sensitive local and one not — to identify which requires `sensitive = true` | Medium |
| 72 | A, C | N/A | Reading a lifecycle block with both condition types to identify TWO correct statements about their timing | Medium |
| 73 | B | N/A | Reading a sensitive variable referenced in a `locals` interpolation used as a resource argument — identifying what `terraform plan` shows | Medium |
| 74 | A, C | N/A | Reading a `validation` block with a compound `&&` condition to identify TWO values that satisfy both sub-conditions | Medium |
| 75 | B | N/A | Reading a `precondition` that uses `can(regex())` to validate a data source attribute format | Hard |
| 76 | A, C | N/A | Reading three parallel snippets — one `validation`, one `precondition`, one `check` — to identify TWO correct statements when the variable value is `"dev"` | Hard |
| 77 | C | N/A | Reading an S3 backend block to identify what `encrypt = true` protects | Easy |
| 78 | C | N/A | Reading a Git-based module source URL to identify what `?ref=v2.0.0` pins | Easy |
| 79 | B | N/A | Reading a root module resource that indexes a child module's list output | Easy |
| 80 | B | N/A | Reading a DynamoDB table resource for Terraform state locking to identify why `hash_key` must be `"LockID"` | Medium |
| 81 | B | N/A | Reading a module block with `for_each` on a map to identify the state addresses of the two instances | Medium |
| 82 | C | N/A | Reading an S3 backend block to identify what the `key` argument specifies | Medium |
| 83 | A, C | N/A | Reading a module block with `count = 2` to identify TWO correct statements about instance addressing and `count.index` | Medium |
| 84 | B | N/A | Reading a module block with `depends_on` to identify what dependency it creates | Medium |
| 85 | C | N/A | Reading a child module's `variables.tf` alongside a root module call to identify which required input is missing | Medium |
| 86 | A, B | N/A | Reading `terraform state list` output to identify TWO correct statements about module resource address format | Medium |
| 87 | C | N/A | Reading a registry module block to identify the version range allowed by the `~>` pessimistic constraint operator | Medium |
| 88 | B | N/A | Reading a module block with a `providers` map to identify what provider alias mapping achieves | Hard |
| 89 | B, D | N/A | Reading a root → child → grandchild module chain to identify TWO correct statements about required explicit variable passing | Hard |
| 90 | B | N/A | Reading an `import` block to identify what the `to` argument specifies | Easy |
| 91 | C | N/A | Reading a two-command sequence to identify what `terraform show plan.tfplan` renders | Easy |
| 92 | B | N/A | Reading a shell snippet with `TF_LOG=WARN` to identify which log messages appear | Easy |
| 93 | B | N/A | Reading a generated resource block to identify which workflow step produced it | Medium |
| 94 | C | N/A | Reading a `cloud` block with a `tags` array to identify which HCP Terraform workspaces it selects | Medium |
| 95 | B | N/A | Reading a `terraform_remote_state` data source and root output to identify the evaluated value | Medium |
| 96 | B | N/A | Reading a shell snippet with only `TF_LOG_PROVIDER` set to identify the resulting log output | Medium |
| 97 | A, C | N/A | Reading a Sentinel policy to identify TWO correct statements about what it enforces and its override behaviour | Medium |
| 98 | A | N/A | Reading two `cloud` block variants to identify the key behavioral difference between name and tags selectors | Medium |
| 99 | A, B | N/A | Reading an `import` block and a CLI import command side-by-side to identify TWO structural differences | Medium |
| 100 | B | N/A | Reading a CI/CD env-var authentication snippet to identify what it achieves and why it is preferred over `terraform login` | Medium |
| 101 | C | N/A | Reading a `hard-mandatory` Sentinel policy and identifying what happens when an Owner tries to override the failure | Hard |
| 102 | A, C | N/A | Reading a shell snippet with `TF_LOG`, `TF_LOG_CORE`, `TF_LOG_PROVIDER`, and `TF_LOG_PATH` all set to identify TWO correct outcomes | Hard |
