# Terraform Associate (004) — Question Bank Iter 3 Batch 1

**Iteration**: 3
**Iteration Style**: HCL interpretation — read a snippet and identify output/effect
**Batch**: 1
**Objective**: 1 — IaC Concepts
**Generated**: 2026-04-25
**Total Questions**: 12
**Difficulty Split**: 2 Easy / 8 Medium / 2 Hard
**Answer Types**: 9 `one` / 3 `many` / 0 `none`

---

# Terraform Associate (004) — Question Bank Iter 3 Batch 2

**Iteration**: 3
**Iteration Style**: HCL interpretation — read a snippet and identify output/effect
**Batch**: 2
**Objective**: 2 — Terraform Fundamentals (Providers & State)
**Generated**: 2026-04-25
**Total Questions**: 13
**Difficulty Split**: 3 Easy / 8 Medium / 2 Hard
**Answer Types**: 10 `one` / 3 `many` / 0 `none`

---

# Terraform Associate (004) — Question Bank Iter 3 Batch 3

**Iteration**: 3
**Iteration Style**: HCL interpretation — read a snippet and identify output/effect
**Batch**: 3
**Objective**: 3 — Core Workflow & CLI
**Generated**: 2026-04-25
**Total Questions**: 13
**Difficulty Split**: 3 Easy / 8 Medium / 2 Hard
**Answer Types**: 10 `one` / 3 `many` / 0 `none`

---

# Terraform Associate (004) — Question Bank Iter 3 Batch 4

**Iteration**: 3
**Iteration Style**: HCL interpretation — read a snippet and identify output/effect
**Batch**: 4
**Objective**: 4a — Resources, Data & Dependencies
**Generated**: 2026-04-25
**Total Questions**: 13
**Difficulty Split**: 3 Easy / 8 Medium / 2 Hard
**Answer Types**: 10 `one` / 3 `many` / 0 `none`

---

# Terraform Associate (004) — Question Bank Iter 3 Batch 5

**Iteration**: 3
**Iteration Style**: HCL interpretation — read a snippet and identify output/effect
**Batch**: 5
**Objective**: 4b — Variables, Outputs, Types & Functions
**Generated**: 2026-04-25
**Total Questions**: 13
**Difficulty Split**: 3 Easy / 8 Medium / 2 Hard
**Answer Types**: 10 `one` / 3 `many` / 0 `none`

---

# Terraform Associate (004) — Question Bank Iter 3 Batch 6

**Iteration**: 3
**Iteration Style**: HCL interpretation — read a snippet and identify output/effect
**Batch**: 6
**Objective**: 4c — Custom Conditions & Sensitive Data
**Generated**: 2026-04-25
**Total Questions**: 12
**Difficulty Split**: 3 Easy / 7 Medium / 2 Hard
**Answer Types**: 9 `one` / 3 `many` / 0 `none`

---

# Terraform Associate (004) — Question Bank Iter 3 Batch 7

**Iteration**: 3
**Iteration Style**: HCL interpretation — read a snippet and identify output/effect
**Batch**: 7
**Objective**: 5 — Modules + 6 — State Backends
**Generated**: 2026-04-25
**Total Questions**: 13
**Difficulty Split**: 3 Easy / 8 Medium / 2 Hard
**Answer Types**: 10 `one` / 3 `many` / 0 `none`

---

# Terraform Associate (004) — Question Bank Iter 3 Batch 8

**Iteration**: 3
**Iteration Style**: HCL interpretation — read a snippet and identify output/effect
**Batch**: 8
**Objective**: 7 — Maintaining Infra + 8 — HCP Terraform
**Generated**: 2026-04-25
**Total Questions**: 13
**Difficulty Split**: 3 Easy / 8 Medium / 2 Hard
**Answer Types**: 10 `one` / 3 `many` / 0 `none`

---

---

## Questions

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

**Answer**: B

**Explanation**:
When `count` is used, Terraform creates one state entry per instance using zero-based bracket notation: `aws_instance.app[0]`, `aws_instance.app[1]`, and `aws_instance.app[2]`. Dot notation (option C) is an older format occasionally seen in legacy documentation but is not the canonical address format for `count`-based resources in current Terraform versions.

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

**Answer**: B

**Explanation**:
Setting `count = 0` is a valid and intentional pattern in Terraform. It declares that zero instances of the resource should exist. If any instances are currently tracked in state, Terraform will plan to destroy them on the next apply. This technique is commonly used to conditionally enable or disable a resource without removing its block from the configuration.

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

**Answer**: C

**Explanation**:
Snippet A is an **imperative** approach — it issues a CLI command that tells AWS exactly what steps to take to create an instance right now. Snippet B is **declarative** — it describes the desired end state (an EC2 instance of type `t3.micro`) and lets Terraform determine whether to create, update, or take no action based on the current state. Terraform HCL is always declarative; shell scripts issuing API calls are imperative.

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

**Answer**: B

**Explanation**:
Each distinct `provider` block requires its own separate provider plugin. This configuration declares two providers — `"aws"` and `"azurerm"` — so `terraform init` must download and install two provider plugins: one from the AWS provider registry and one from the AzureRM provider registry. Resources are associated with provider plugins based on their type prefix, not on a one-per-resource basis.

---

### Question 5 — Desired vs Current State Table Interpretation

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Reading a desired vs current state comparison to predict what terraform plan proposes

**Question**:
A team's Terraform configuration and current cloud state can be summarised as:

| Resource | Desired State (config) | Current State (cloud) |
|----------|----------------------|----------------------|
| `aws_instance.web[0]` | `t3.micro` | `t3.micro` |
| `aws_instance.web[1]` | `t3.micro` | Does not exist |
| `aws_instance.web[2]` | Does not exist | `t3.micro` |

What does `terraform plan` propose?

- A) No changes — all three instances are accounted for
- B) Create `aws_instance.web[1]`, destroy `aws_instance.web[2]`
- C) Destroy all three existing instances and recreate them
- D) Create `aws_instance.web[1]` only; `aws_instance.web[2]` is kept as unmanaged

**Answer**: B

**Explanation**:
Terraform reconciles differences between desired and current state. `aws_instance.web[0]` is already in the desired state — no action. `aws_instance.web[1]` exists in configuration but not in the cloud — Terraform plans to **create** it. `aws_instance.web[2]` exists in the cloud (and in state) but is not in the configuration — Terraform plans to **destroy** it. This targeted reconciliation is characteristic of declarative IaC.

---

### Question 6 — What "Idempotent" Means for This Apply Output

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

**Answer**: C

**Explanation**:
An apply summary of `0 added, 0 changed, 0 destroyed` confirms that the current state of the infrastructure already matched the desired state expressed in the configuration. No modifications were required. This is Terraform's idempotent behaviour in action — running apply multiple times against an unchanged configuration is always safe and produces this output once the desired state is reached.

---

### Question 7 — Provider Constraint on Cloud Scope

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

**Answer**: B, C

**Explanation**:
Tool B is Terraform — its provider plugin ecosystem spans 3000+ providers (AWS, Azure, GCP, Kubernetes, and more), making it the canonical multi-cloud IaC tool. Tool C matches AWS CloudFormation — it uses JSON/YAML templates (not HCL) and is AWS-only with no explicit provider concept. Tool A does not match Terraform; Terraform is not limited to AWS.

---

### Question 8 — Documentation Role of Config Files

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Interpreting a configuration file as living documentation of infrastructure

**Question**:
A new engineer joins a team and is given read access to the Git repository containing all Terraform `.tf` files. The repository has no separate architecture diagrams or runbooks. Which statement best describes what the engineer can determine from the Terraform files alone?

- A) Nothing useful — Terraform files only contain syntax, not meaningful infrastructure information
- B) Only the list of resource types — attributes and values are hidden by variable references
- C) The complete intended infrastructure topology: resource types, configurations, dependencies, and relationships — because configuration files serve as living documentation
- D) Only the most recently applied state — older configurations require the state file to reconstruct

**Answer**: C

**Explanation**:
One of the key benefits of IaC is that configuration files serve as living documentation. A well-written Terraform repository describes the full desired infrastructure topology — resource types, attribute values, inter-resource references, and dependency relationships — in human-readable HCL. An engineer who can read HCL can understand the intended architecture without separate runbooks or diagrams, because the code is the authoritative description of the system.

---

### Question 9 — Interpreting Tool Type from Snippet

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

**Answer**: B

**Explanation**:
The YAML snippet uses Ansible's task syntax (`apt` module to install packages, `service` module to manage daemons) — a **configuration management** tool focused on what runs *inside* a server. The HCL snippet uses Terraform's `resource` block syntax to declare cloud infrastructure — a **provisioning** tool focused on creating the server itself. Terraform and Ansible are complementary in the toolchain: Terraform provisions the VM; Ansible configures it.

---

### Question 10 — Audit Trail Interpretation from Git Log

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

**Answer**: C

**Explanation**:
The `git log` shows that every infrastructure change — resizing instances, adding databases, disabling resources — was committed with the author's name and a timestamp. This is the **audit trail** benefit of IaC: all changes are traceable, reviewable, and attributable without relying on cloud provider activity logs alone. Repeatability and idempotency are also IaC benefits, but they are not directly demonstrated by a commit history.

---

### Question 11 — CloudFormation vs Terraform Multi-Cloud Snippet

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

**Answer**: C

**Explanation**:
Only Terraform's provider plugin model supports declaring resources from multiple cloud providers within a single root module configuration. AWS CloudFormation is AWS-only and cannot manage Azure resources. Azure ARM templates (and Bicep) are Azure-only. This multi-cloud capability — using `aws_*` and `azurerm_*` resources together in one configuration — is a defining characteristic of Terraform.

---

### Question 12 — Interpreting "Drift" from a State vs Cloud Comparison

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

**Answer**: A, D

**Explanation**:
The `~` prefix on an attribute line means an in-place update — the resource will be modified without being destroyed. The plan shows `instance_class` changing from `db.t3.medium` to `db.t3.large` and `backup_retention_period` from `7` to `14` — these attributes were either changed outside Terraform (drift) or updated in the configuration. `multi_az = false` appears without a `~` or change arrow, meaning no change is proposed for that attribute. Option B is incorrect; option C is incorrect — `~` on the resource line means update, not replace. Option D correctly describes the update semantics.

---

---

## Questions

---

### Question 1 — Reading a `~> 5.0` Version Constraint

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

**Answer**: B

**Explanation**:
The `~>` pessimistic constraint operator allows updates to the rightmost non-zero component. `~> 5.0` means >= `5.0` and < `6.0` — permitting any `5.x.x` version. This keeps the provider within major version 5 while allowing minor and patch updates. By contrast, `~> 5.0.0` would allow only patch updates (>= `5.0.0` and < `5.1.0`).

---

### Question 2 — Resolving a Short-Form Provider Source Address

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

**Answer**: B

**Explanation**:
The full provider source address format is `<hostname>/<namespace>/<type>`. When the hostname is omitted — as it is in `"hashicorp/aws"` — Terraform defaults to `registry.terraform.io`. The two-part shorthand `hashicorp/aws` therefore resolves to `registry.terraform.io/hashicorp/aws`, which is the address of the official HashiCorp AWS provider on the public Terraform registry.

---

### Question 3 — `sensitive = true` on an Output Block

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

**Answer**: B

**Explanation**:
`sensitive = true` on an output suppresses the value from being printed in terminal output — it appears as `(sensitive value)`. However, it provides no protection for the state file: Terraform stores **all resource attributes in plaintext** in `terraform.tfstate`, regardless of the `sensitive` flag. The raw password is visible in the state file JSON. Protecting secrets in state requires encrypting the remote backend and restricting access to the state file.

---

### Question 4 — `~> 5.0.0` vs `~> 5.0` Constraint Range

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

**Answer**: C

**Explanation**:
The `~>` operator allows updates to the rightmost component specified. `"~> 5.0"` has two components, so the rightmost (`0`) can increment — allowing `5.1`, `5.2`, ..., but not `6.0`. `"~> 5.0.0"` has three components, so only the last (`0`) can increment — allowing `5.0.1`, `5.0.2`, ..., but not `5.1.0`. This patch-only behaviour is common when stricter version pinning is required.

---

### Question 5 — Default Provider Selection When Alias Exists

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

**Answer**: B

**Explanation**:
When multiple configurations of the same provider are declared (one default, one or more aliased), resources that omit the `provider` argument are automatically assigned to the **default (unaliased)** configuration. The aliased provider (`aws.west`) is only used by resources that explicitly declare `provider = aws.west`. Here, `aws_instance.api` has no `provider` argument, so it uses the default `"us-east-1"` configuration.

---

### Question 6 — Lock File `hashes` Field Purpose

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

**Answer**: B

**Explanation**:
The `hashes` field in `.terraform.lock.hcl` contains cryptographic checksums (in both `h1:` and `zh:` formats) of the provider binary for each supported platform. When a team member runs `terraform init` with the lock file present, Terraform verifies that the downloaded binary matches these hashes. This prevents supply-chain attacks where a malicious version of a provider could be silently substituted for the expected one.

---

### Question 7 — State JSON `id` Field Role

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

**Answer**: C

**Explanation**:
The `id` field in a Terraform state resource entry is the cloud provider's unique identifier for the real resource — in this case, the AWS EC2 instance ID `i-0aaa1111bb2222cc3`. Terraform uses this ID in all subsequent provider API calls (reads, updates, deletes) to reference the correct real-world resource. Without this mapping, Terraform would have no way to associate a config-level name like `aws_instance.db_server` with the actual instance running in AWS.

---

### Question 8 — Provider Alias Reference on a Resource

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

**Answer**: B

**Explanation**:
`provider = aws.west` explicitly assigns `aws_instance.replica` to the aliased provider configuration that has `alias = "west"` and `region = "us-west-2"`. Without this argument, the resource would use the default (unaliased) `us-east-1` configuration. This per-resource provider assignment is the standard pattern for multi-region architectures where different resources must be created in different regions using the same provider type.

---

### Question 9 — Lock File Content After `terraform init`

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

**Answer**: A, B

**Explanation**:
`.terraform.lock.hcl` records three things per provider: the **exact version** installed, the **version constraint** from `required_providers`, and **cryptographic hashes** for verification. It also uses the **full source address** (e.g., `registry.terraform.io/hashicorp/aws`) as the key for each provider entry. Workspace names and local filesystem paths are not stored in the lock file. Committing this file ensures all team members install the same provider versions.

---

### Question 10 — Reading the `!=` Version Constraint

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

**Answer**: B

**Explanation**:
The `!=` operator is a valid Terraform version constraint that excludes a single specific version. `"!= 5.0.0"` tells Terraform to install any available AWS provider version except exactly `5.0.0` — for example, `4.67.0`, `5.0.1`, or `5.31.0` would all be acceptable. This operator is typically combined with other constraints (e.g., `>= 5.0, != 5.0.0`) to avoid a known broken release while still allowing other versions in a range.

---

### Question 11 — State Attributes Displayed by `terraform state show`

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

**Answer**: A, B

**Explanation**:
`terraform state show <address>` reads from the state file and displays all state-tracked attributes for the specified resource. It does not make live API calls — it shows the attributes as they were last recorded in state. From this excerpt, the output would include `id`, `ami`, `instance_type`, `private_ip`, and `public_ip`, along with `id = "i-0aaa1111bb2222cc3"` as the primary cloud identifier. Option C is incorrect (all attributes are shown, not just `id`); Option D is incorrect (`state show` reads from state, not from a live API refresh).

---

### Question 12 — Comparing Two `~>` Constraints

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

**Answer**: A, C

**Explanation**:
`~>` allows increments to the rightmost version component. `~> 4.0` has two parts — the rightmost (`0`) can increment, so minor versions change: >= `4.0`, < `5.0`. `~> 4.67.0` has three parts — the rightmost (`0` in patch position) can increment, so only the patch changes: >= `4.67.0`, < `4.68.0`. Option B is incorrect (that would be the behaviour of `~> 4.0.0`). Option D is incorrect (stopping at `4.68.0`, not `5.0`).

---

### Question 13 — Lock File After `terraform init -upgrade`

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

**Answer**: B

**Explanation**:
`terraform init -upgrade` re-evaluates the version constraint and installs the newest available version within the constraint range. For `~> 5.0`, `5.31.0` qualifies (>= `5.0`, < `6.0`). Terraform updates the lock file with the new exact `version = "5.31.0"` and the corresponding `hashes` for the new binary. The `constraints` field is never modified by `init -upgrade` — it always reflects the constraint as written in `required_providers`. The old hashes are replaced because they are specific to the `5.10.0` binary.

---

---

## Questions

---

### Question 1 — Identifying the Pure-Create Resource in a Plan

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

**Answer**: B

**Explanation**:
The `+` prefix without a `-` means Terraform will create a brand-new resource with no existing object to destroy first. `aws_vpc.main` is the only pure creation here. `aws_instance.web` uses `~` (update in-place — no new object created) and `aws_db_instance.primary` uses `-/+` (destroy then create as a replacement). The `Plan: 2 to add` includes both `aws_vpc.main` and the replacement create for `aws_db_instance.primary`, but only `aws_vpc.main` has no corresponding destruction.

---

### Question 2 — `terraform console` Evaluating a Map with `length`

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

**Answer**: B

**Explanation**:
`terraform console` is an interactive REPL that evaluates HCL expressions and built-in functions. The `length()` function returns the number of elements in a list, tuple, set, or map. This map has three key-value pairs (`"us-east-1"`, `"us-west-2"`, `"eu-west-1"`), so `length()` returns `3`. The `terraform console` is commonly used to test expressions like this before embedding them in configuration files.

---

### Question 3 — Reading `terraform workspace list` Output

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

**Answer**: C

**Explanation**:
`terraform workspace list` displays all available workspaces and uses a `*` prefix to mark the currently active one. In this output, `staging` is prefixed with `*`, meaning all plan, apply, and state operations will use the `staging` workspace's isolated state. The position in the list (first, second, last) has no meaning for determining which workspace is active.

---

### Question 4 — Interpreting a `-/+` Plan Block

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

**Answer**: C

**Explanation**:
The `-/+` symbol signals a **replacement** operation: Terraform will first destroy the existing `aws_instance.app` (identified by `i-0abc123def456`) and then create a new instance with the updated `ami` value. The `# forces replacement` comment on the `ami` line indicates that this specific attribute change cannot be applied in-place — AWS requires a new instance when the AMI is changed. The `id` value is shown as `(known after apply)` because the new instance will receive a different AWS-assigned ID.

---

### Question 5 — `terraform output -json` Structure

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

**Answer**: C

**Explanation**:
`terraform output -json` returns all output values as a structured JSON object where each output name is a key and the value is an object containing `sensitive` (boolean), `type` (the Terraform type), and `value` (the actual value). This format is machine-readable and is commonly used in scripts and CI pipelines that need to process multiple outputs. `terraform output -raw` returns a single output value as a plain unquoted string — it does not produce JSON or include type metadata.

---

### Question 6 — `terraform fmt -check` vs `terraform fmt -diff`

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

**Answer**: A, C

**Explanation**:
Both `-check` and `-diff` are **read-only** flags — neither writes changes to disk. `-check` is a gate: it exits with code 1 if formatting is needed and code 0 if all files are already canonical, making it ideal for CI checks. `-diff` shows a unified diff of what would change if `terraform fmt` were run, letting an engineer preview formatting corrections before applying them. To actually reformat files, run `terraform fmt` without either flag.

---

### Question 7 — `terraform show plan.tfplan`

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

**Answer**: B

**Explanation**:
`terraform show` accepts either no argument (reads current state) or a saved plan file. When given a plan file such as `release.tfplan`, it displays the human-readable representation of that plan — the same resource additions, changes, and destructions that were computed by `terraform plan -out`. This allows a reviewer to inspect the exact operations that will be performed before running `terraform apply release.tfplan`. Use `terraform show -json release.tfplan` for machine-readable output.

---

### Question 8 — Inline `-var` Flag Override

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

**Answer**: C

**Explanation**:
Terraform variable value precedence (from lowest to highest) is: default in `variable` block → `terraform.tfvars` → `*.auto.tfvars` → `-var-file` flag → `-var` flag → environment variables. The inline `-var` flag is near the top of this precedence order, so `-var "instance_type=t3.large"` overrides the `"t3.micro"` default for this run only. The `variables.tf` file is not modified.

---

### Question 9 — Interpreting an Update Plan Block

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

**Answer**: B, C

**Explanation**:
The `~` prefix on a resource block means **update in-place** — the existing resource will be modified without being destroyed or recreated. Lines with `~` prefix show old → new attribute values being changed in-place (`description` and `name`). Lines without any prefix — like `vpc_id = "vpc-0abc12345"` — show attributes that are **not changing**; Terraform includes them for context. The `->` arrow separates the current value (left) from the planned new value (right). A `-/+` symbol (not `~`) is what indicates destroy-then-recreate.

---

### Question 10 — `terraform init -migrate-state` Backend Block

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

**Answer**: A

**Explanation**:
When changing backends, `terraform init -migrate-state` prompts Terraform to copy the existing state from the old backend (local file) to the new backend (S3) during initialisation. Without this flag, Terraform may warn about existing state and refuse to proceed. `-reconfigure` is used to force reconfiguration of the backend without migrating state — it discards the existing state location and starts fresh with the new backend. `-upgrade` is for updating provider versions, not for state migration.

---

### Question 11 — `-auto-approve` with a Saved Plan File

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

**Answer**: D

**Explanation**:
When `terraform apply` receives a saved plan file as an argument, it applies the exact plan without asking for confirmation — the interactive `yes` prompt is only shown when no plan file is provided. Providing `-auto-approve` alongside a plan file is harmless but redundant. This is distinct from `terraform apply` with no plan file, where the command re-runs the plan internally and then asks for confirmation unless `-auto-approve` is specified.

---

### Question 12 — Plan Summary with Only Replacements

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

**Answer**: A, C

**Explanation**:
A `-/+` replacement contributes to **both** the `to add` and `to destroy` counts in the plan summary — the old object is destroyed (contributing to `2 to destroy`) and a new object is created (contributing to `2 to add`). With two replacements and no pure creates, `2 to add` counts only the replacement creates. `0 to change` confirms there are no `~` (update in-place) operations. Option B is incorrect — the destroyed objects ARE replaced by new ones. Option D is incorrect — the same resource address contributes to both the destroy count and the add count during a replacement.

---

### Question 13 — `terraform apply -replace` Plan Symbol

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

**Answer**: C

**Explanation**:
`terraform apply -replace` forces Terraform to treat the specified resource as requiring replacement regardless of whether the configuration has changed. The plan shows `-/+` for `aws_instance.web`, meaning the existing instance (currently tracked in state) will be destroyed and a new instance will be created. This is the modern replacement for the deprecated `terraform taint` command. It is useful when a resource has become unhealthy, is in an unknown state, or needs to be refreshed without modifying its configuration.

---

---

## Questions

---

### Question 1 — `create_before_destroy` Replacement Order

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

**Answer**: B

**Explanation**:
By default, when a replacement is required, Terraform destroys the existing resource first and then creates the replacement. `create_before_destroy = true` reverses this order: the new instance is provisioned first, and only after it succeeds is the old instance destroyed. This minimises downtime for resources that serve live traffic. The plan still shows a `-/+` symbol for the resource — the replacement is required, but the sequencing is reversed.

---

### Question 2 — Distinguishing a Data Source Reference from a Resource Reference

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

**Answer**: B

**Explanation**:
Terraform uses distinct reference formats for data sources and managed resources. Data source references follow the pattern `data.<TYPE>.<NAME>.<ATTRIBUTE>` — the `data.` prefix is the syntactic signal that the value comes from a `data` block, not a `resource` block. `aws_subnet.public.id` omits the `data.` prefix, confirming it references a managed resource declared with `resource "aws_subnet" "public"`. This distinction is important when reading configuration snippets to understand what each value represents.

---

### Question 3 — `moved` Block Address After Apply

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

**Answer**: C

**Explanation**:
The `moved` block instructs Terraform to update the state file so the resource is tracked under the new address (`aws_instance.api`) instead of the old one (`aws_instance.server`). No API calls are made to the cloud provider — the running EC2 instance is not affected. After a successful apply, the `moved` block can be removed from the configuration. If the `moved` block were absent, Terraform would plan to destroy `aws_instance.server` and create a new `aws_instance.api`.

---

### Question 4 — Three-Resource Implicit Dependency Chain

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

**Answer**: C

**Explanation**:
Terraform builds a dependency graph from attribute references. `aws_subnet.public` references `aws_vpc.main.id`, so the VPC must exist before the subnet. `aws_instance.web` references `aws_subnet.public.id`, so the subnet must exist before the instance. This creates a strict sequential chain: VPC → subnet → instance. `aws_instance.web` is always created last. File declaration order and argument count have no effect on execution order.

---

### Question 5 — `ignore_changes` on a Modified Attribute

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

**Answer**: B

**Explanation**:
`ignore_changes = [ami]` tells Terraform to skip drift detection for the `ami` attribute. During `terraform plan`, even if the real-world value differs from what is in state or config, Terraform does not propose any change to that attribute. The plan reports no changes for `aws_instance.web`. This is commonly used for AMIs managed externally (e.g., updated by a pipeline) where Terraform should not interfere with the value.

---

### Question 6 — `removed` Block with `destroy = false`

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

**Answer**: B

**Explanation**:
The `removed` block (available since Terraform 1.7) instructs Terraform to stop managing a resource without destroying it. With `destroy = false`, Terraform removes the resource from state but issues no API delete call — the S3 bucket continues to exist in AWS, unmanaged by Terraform. This is useful when a resource should be "adopted" by another tool or managed manually going forward. Without `destroy = false` (the default is `destroy = true`), the resource would be destroyed during apply.

---

### Question 7 — `depends_on` Ordering Guarantee

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

**Answer**: B

**Explanation**:
`depends_on` is used for dependencies that Terraform cannot detect through attribute references. Here, `aws_instance.app` does not directly reference any output of `aws_iam_role_policy.s3_access`, so Terraform would normally have no knowledge that the policy must be attached before the instance is launched. Adding `depends_on = [aws_iam_role_policy.s3_access]` forces Terraform to apply the policy first. This is the standard pattern for IAM policy attachments that the instance relies on at boot time but does not reference in its HCL arguments.

---

### Question 8 — `replace_triggered_by` with a Specific Attribute

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

**Answer**: B

**Explanation**:
`replace_triggered_by` accepts both resource addresses and resource attribute addresses. When a full resource address (e.g., `aws_launch_template.web`) is given, any change to the resource triggers replacement. When a specific attribute address (e.g., `aws_launch_template.web.image_id`) is given, only a change to that particular attribute triggers replacement. This provides finer-grained control — in this case, updating `instance_type` on the launch template would not force an ASG replacement, but changing `image_id` would.

---

### Question 9 — `terraform apply -parallelism=1`

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

**Answer**: B

**Explanation**:
`-parallelism=N` controls the maximum number of concurrent resource operations during apply. The default is `10`. Setting `-parallelism=1` limits Terraform to applying exactly one resource at a time, effectively serialising all operations. Even though the 8 resources have no dependencies and could safely run concurrently, Terraform will apply them one at a time. This is sometimes used to avoid rate-limiting by cloud provider APIs. The normal default of `10` allows up to 10 concurrent operations.

---

### Question 10 — `lifecycle` Block with Multiple Arguments

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

**Answer**: A, C

**Explanation**:
`prevent_destroy = true` causes Terraform to error during **plan** time if any operation would destroy the resource — this includes both `terraform destroy` and replacements triggered by config changes. Option D is incorrect: `prevent_destroy` blocks all destroy operations, not just `terraform destroy`. `create_before_destroy = true` ensures the replacement instance is provisioned first, then the old one is deleted. Option B is incorrect because `ignore_changes = [engine_version]` tells Terraform to ignore drift on that attribute — it will NOT propose reverting an externally changed `engine_version`.

---

### Question 11 — Data Source Block TWO Correct Statements

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

**Answer**: A, C

**Explanation**:
Data sources are **read-only** — `data "aws_ami" "ubuntu"` queries the AWS API to find an existing AMI matching the filter; it does not create anything. Option B is incorrect. The `data.` prefix in `data.aws_ami.ubuntu.id` is the syntactic marker that distinguishes a data source reference from a managed resource reference (which would be `aws_ami.ubuntu.id` without the prefix). `most_recent = true` selects the newest matching AMI from existing ones — it does not create AMIs. Options B and D are both incorrect.

---

### Question 12 — Parallel vs Sequential Resource Creation

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

**Answer**: B

**Explanation**:
`aws_security_group.web_sg` references only `aws_vpc.main.id` (already in state). `aws_iam_instance_profile.web` references only `aws_iam_role.web.name` (already in state). Because neither references the other, Terraform identifies them as independent and creates them concurrently. `aws_instance.web` references both `aws_security_group.web_sg.id` and `aws_iam_instance_profile.web.name`, creating two implicit dependencies. Terraform waits for both to complete before creating the instance. File declaration order has no effect on execution order.

---

### Question 13 — `moved` Block into a Module

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

**Answer**: A, C

**Explanation**:
The `moved` block handles resource address relocations purely as state updates — no cloud API calls are made to destroy or recreate the bucket. Terraform maps the old root-level address (`aws_s3_bucket.app_data`) to the new module-scoped address (`module.storage.aws_s3_bucket.app_data`) in state. The plan shows no resource changes — only a state rename. After the apply succeeds, the `moved` block has served its purpose and can be deleted. Keeping it permanently (Option D) is unnecessary and eventually confusing — it only needs to exist for the transitional apply.

---

---

## Questions

---

### Question 1 — `locals` String Interpolation Result

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

**Answer**: C

**Explanation**:
Terraform `locals` blocks fully support interpolation and can reference other locals defined in the same or other `locals` blocks. The expression `"${local.app_name}-${local.environment}"` resolves `local.app_name` to `"my-app"` and `local.environment` to `"production"`, producing `"my-app-production"`. There is no restriction on locals referencing other locals, as long as no circular reference is created.

---

### Question 2 — `for` Expression: List Brackets vs Map Braces

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

**Answer**: B

**Explanation**:
The outer delimiter of a `for` expression determines its output type. `[for ... : value]` (square brackets) produces a **list**. `{for ... : key => value}` (curly braces with `=>`) produces a **map**. Here, `local.result_a` is a list of uppercase strings `["ALICE", "BOB", "CAROL"]`, and `local.result_b` is a map `{ alice = "ALICE", bob = "BOB", carol = "CAROL" }`. This distinction is important when deciding which type a downstream resource argument expects.

---

### Question 3 — `zipmap()` Result

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

**Answer**: B

**Explanation**:
`zipmap(keys_list, values_list)` creates a map by pairing each element of the first list (keys) with the corresponding element of the second list (values). The first element of `local.keys` (`"us-east-1"`) becomes a key mapped to the first element of `local.values` (`"prod-east"`), and so on. The result is `{ "us-east-1" = "prod-east", "eu-west-1" = "prod-west" }`. Both lists must have equal length.

---

### Question 4 — `dynamic` Block with Custom `iterator` Name

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

**Answer**: B

**Explanation**:
By default, a `dynamic` block's iterator variable shares the block type name — for `dynamic "ingress"`, the default iterator would be `ingress`. When `iterator = rule` is declared, it overrides this default, and the iterator variable is renamed to `rule`. Inside the `content` block, only the declared iterator name is valid — using `ingress.value.from_port` after declaring `iterator = rule` would cause an error because `ingress` is no longer the active iterator symbol. This is useful for avoiding naming conflicts when nesting `dynamic` blocks.

---

### Question 5 — `for` Map Comprehension with Key Transformation

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

**Answer**: B

**Explanation**:
In a map `for` expression (`{ for k, v in collection : key_expr => value_expr }`), both the key expression and the value expression are arbitrary Terraform expressions. Here, `upper(k)` transforms the key to uppercase while `v` passes the value through unchanged. The result maps `"dev"` → `"DEV"` for keys and preserves region strings: `{ DEV = "us-east-1", PROD = "eu-west-1" }`. Functions can be called on any part of a `for` expression.

---

### Question 6 — `cidrhost()` Returns a Host IP

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

**Answer**: B

**Explanation**:
`cidrhost(prefix, hostnum)` calculates the IP address of a specific host within a CIDR block. With `"10.0.1.0/24"` and host number `1`, it returns `"10.0.1.1"` — the first usable host address in that subnet. Host number `0` would return the network address (`10.0.1.0`), and host number `254` returns `"10.0.1.254"`. The function returns a bare IP string without the prefix length. This is commonly used to calculate gateway or DNS resolver IPs within a known subnet.

---

### Question 7 — `concat()` Combines Two Lists

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

**Answer**: A

**Explanation**:
`concat(list1, list2, ...)` takes two or more lists and combines them into a single flat list, in order. The result is not nested — all elements from all input lists are placed at the same level in the output. With `web_ips` having 2 elements and `app_ips` having 1, the result is a 3-element list: `["10.0.1.10", "10.0.1.11", "10.0.2.10"]`. Use `flatten()` if the input lists themselves contain nested lists.

---

### Question 8 — `jsonencode()` Output Type

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

**Answer**: B

**Explanation**:
`jsonencode(value)` takes any Terraform value and serialises it to a JSON-formatted **string**. The output type is always `string`, regardless of the complexity of the input. This is commonly used in AWS IAM policy documents, where the API requires the policy as a JSON string rather than a structured object. The resulting string for this example would be `"{\"Version\":\"2012-10-17\",\"Statement\":[{\"Effect\":\"Allow\",\"Action\":\"s3:GetObject\",\"Resource\":\"*\"}]}"`.

---

### Question 9 — `validation` Block Condition Evaluation

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

**Answer**: B

**Explanation**:
Terraform evaluates `validation` blocks before the plan phase. The `condition` expression `contains(["dev", "staging", "production"], "test")` returns `false` because `"test"` is not in the allowed list. When the condition is `false`, Terraform raises an error and displays the `error_message`. The type constraint (`string`) is separate from the validation constraint and is satisfied — the validation block provides an additional layer of semantic validation beyond type checking.

---

### Question 10 — `can()` and `try()` on a Missing Map Key

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

**Answer**: A, C

**Explanation**:
`can(expr)` evaluates an expression and returns `true` if it succeeds without error, or `false` if it would error. Accessing the key `"retry_count"` in a map that does not contain it raises an error, so `can(var.config["retry_count"])` returns `false`. `try(expr1, fallback)` attempts each expression in order and returns the first result that does not error. Because `var.config["retry_count"]` errors, `try()` moves to `5` and returns it. Neither function propagates the error to the user — they are specifically designed for safe optional value access.

---

### Question 11 — `for_each` Map: Identifying `each.value` for a Named Key

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

**Answer**: C

**Explanation**:
When `for_each` iterates over a map, `each.key` is the current map key and `each.value` is the corresponding value. For the instance at key `"app"`, `each.key` is `"app"` and `each.value` is `"t3.small"` — the value associated with `"app"` in `var.instance_sizes`. The `instance_type` argument is set to `each.value`, so `aws_instance.servers["app"]` uses `instance_type = "t3.small"`. The `tags.Name` uses `each.key`, giving it the tag `Name = "app"`.

---

### Question 12 — `for` Expression with `if` Filter on a Map

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

**Answer**: A, C

**Explanation**:
The outer `[...]` delimiter makes this a **list** `for` expression — regardless of whether the input is a map or list, the output type is determined by the delimiter. The `if role == "admin"` clause filters out elements where the condition is false. Only `"alice"` and `"carol"` have `role == "admin"` in `var.users`, so `local.admins` is a list of exactly 2 elements. Terraform iterates maps in lexicographic key order, so the result is `["alice", "carol"]`. Option B is incorrect — the input type does not determine the output type; the delimiter does. Option D is incorrect — the `if` clause is a real filter that excludes non-matching elements.

---

### Question 13 — `for` Expression with `cidrsubnet()` Applied to Index

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

**Answer**: A, C

**Explanation**:
The outer `[...]` delimiter makes `local.subnet_cidrs` a **list**, not a map. Option D is incorrect. When `for` iterates a list with two variables (`for idx, az in list`), `idx` is the **zero-based** numeric index. Option B is incorrect — `idx` starts at `0`, not `1`. The three elements are: `cidrsubnet("10.0.0.0/16", 8, 0)` = `"10.0.0.0/24"`, `cidrsubnet("10.0.0.0/16", 8, 1)` = `"10.0.1.0/24"`, `cidrsubnet("10.0.0.0/16", 8, 2)` = `"10.0.2.0/24"`. The list contains exactly 3 CIDR strings (option A), and the third element is `"10.0.2.0/24"` (option C).

---

---

## Questions

---

### Question 1 — `validation` Condition with `startswith()`

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

**Answer**: C

**Explanation**:
`startswith(string, prefix)` returns `true` only when the string begins with the exact prefix — the check is case-sensitive and must match at position 0. `"t3.small"` begins with `"t3."` and passes. `"t2.micro"` begins with `"t2."` — close, but not `"t3."`. `"T3.micro"` fails because Terraform string comparisons are case-sensitive. `"m5.t3.large"` contains `"t3."` but does not start with it, so `startswith()` returns `false`.

---

### Question 2 — `self` Reference in a `postcondition`

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

**Answer**: B

**Explanation**:
In a `postcondition` block, `self` is a special reference to the resource instance that was just created or updated during the current apply operation. It allows the condition to inspect the resulting real-world attribute values — in this case, checking that `public_ip` was actually assigned. The `postcondition` is evaluated after the resource change completes. This is why `self` is only available in `postcondition`, not `precondition` — at precondition time, the resource does not yet have new attribute values to inspect.

---

### Question 3 — `check` Block `error_message` Interpolation

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

**Answer**: A

**Explanation**:
The `error_message` string supports interpolation — `${data.http.probe.status_code}` resolves to the actual value returned at evaluation time. Because the endpoint returns `503`, the interpolated message is `"Health check failed: got 503, expected 200."`. This message is displayed as a **warning** (not an error) since `check` blocks never block apply. The custom `error_message` is always used when an assertion fails — Terraform does not substitute a generic message.

---

### Question 4 — Variable with Two `validation` Blocks

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

**Answer**: C

**Explanation**:
Both validation blocks must pass simultaneously for the variable to be accepted. `80` fails the first condition (`80 >= 1024` is false). `1023` also fails the first condition (`1023 >= 1024` is false — it is one below the threshold). `70000` fails the second condition (`70000 <= 65535` is false). `8080` satisfies both: `8080 >= 1024` is true, and `8080 <= 65535` is true. When a variable has multiple `validation` blocks, all conditions must pass; any single failure displays that block's `error_message` and halts processing.

---

### Question 5 — `precondition` Referencing a Data Source Attribute

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

**Answer**: B

**Explanation**:
`precondition` blocks are evaluated before the resource is changed during apply. The condition `data.aws_ami.ubuntu.architecture == "x86_64"` evaluates to `false` when the AMI returns `"arm64"`. Terraform displays the `error_message` (with the interpolated architecture value) and halts apply immediately — `aws_instance.web` is never sent to the AWS API. No instance is created and no partial state is recorded. This contrasts with `postcondition`, which would only fire after the instance already exists.

---

### Question 6 — `check` Block Without a Scoped Data Source

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

**Answer**: B

**Explanation**:
`check` blocks are always **non-blocking**. A failing `assert` condition produces a warning message — the apply does not fail, no resources are rolled back, and no resources are modified to satisfy the assertion. The ASG is created with one AZ as declared in the configuration; the `check` block simply flags the HA concern to the operator. A scoped `data` source inside a `check` block is optional — the block is valid and evaluated with only an `assert`.

---

### Question 7 — Sensitivity Propagation Through `locals` to Two Outputs

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

**Answer**: C

**Explanation**:
Sensitivity propagates in Terraform: any expression that includes a reference to a sensitive value is itself treated as sensitive. `local.db_url` interpolates `var.password`, so the resulting string is sensitive. When `db_url_output` references this sensitive local without `sensitive = true`, Terraform raises a plan error requiring the flag to be added. `local.greeting` does not reference any sensitive value, so `greeting_output` requires no special marking and displays normally. This selective propagation allows non-sensitive values to remain visible while protecting sensitive ones.

---

### Question 8 — Lifecycle Block with Both `precondition` and `postcondition`

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

**Answer**: A, C

**Explanation**:
`precondition` runs before the resource is changed — if `var.db_instance_class` is `"db.t3.micro"`, the condition evaluates to `false` and apply halts before any AWS API call is made (C is correct). `postcondition` runs after the resource change completes (B is incorrect). `self` in a `postcondition` refers to the newly created or updated resource's attributes, not the previous state (D is incorrect). This means if the `precondition` passes but the DB is created without a valid endpoint, the `postcondition` catches it — but only after the DB already exists in AWS.

---

### Question 9 — Sensitive Variable Through `local` to Resource Argument

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

**Answer**: B

**Explanation**:
Sensitivity propagates through Terraform expressions. When `local.connection_string` interpolates `var.api_secret` (which is sensitive), the resulting string is also sensitive. When this sensitive local is used in a resource argument, `terraform plan` redacts the entire value as `(sensitive value)`. Terraform does not perform partial redaction — the entire expression result is treated as sensitive. The value is still stored in plaintext in `terraform.tfstate`, so an encrypted remote backend is required to protect it at rest.

---

### Question 10 — `validation` with `&&` — Identifying Values That Pass

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

**Answer**: A, C

**Explanation**:
The condition requires both sub-expressions to be `true`. `"10.0.0.0/16"` starts with `"10."` (✓) and `split(".", "10.0.0.0/16")` returns `["10", "0", "0", "0/16"]` — 4 elements (✓). `"10.0.1.0"` starts with `"10."` (✓) and `split(".", "10.0.1.0")` returns `["10", "0", "1", "0"]` — 4 elements (✓). `"192.168.1.0/24"` fails the first sub-condition (does not start with `"10."`). `"10.0.0"` starts with `"10."` but `split(".", "10.0.0")` returns only 3 elements, failing the length check.

---

### Question 11 — `precondition` with `can(regex())` Pattern

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

**Answer**: B

**Explanation**:
This `precondition` runs before `aws_instance.web` is created during apply. It uses `regex()` to confirm the AMI ID matches the expected `ami-xxxxxxxx` format. `can(expr)` wraps the `regex()` call — if `data.aws_ami.ubuntu.id` is `null` or not a string, `regex()` would raise an error; `can()` catches that error and returns `false` instead of propagating it, causing the precondition to fail cleanly with the custom `error_message` rather than a cryptic Terraform runtime error. This pattern is a common idiom for safe format validation in lifecycle conditions.

---

### Question 12 — Three Condition Mechanisms for `var.env = "dev"`

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

**Answer**: A, C

**Explanation**:
Snippet 1: `contains(["dev", "prod"], "dev")` returns `true` — the validation passes and planning proceeds. Snippet 2: `"dev" == "prod"` is `false`, making the `precondition` condition `false`. A false condition causes the precondition to fail; apply is halted before `aws_instance.web` is created. The error is not about `null` — any false condition fails a precondition. Snippet 3: `"dev" != ""` is `true` (dev is not an empty string), so the check assertion passes — no warning is emitted. Option D incorrectly states the check fails; `"dev" != ""` evaluates to `true`.

---

---

## Questions

---

### Question 1 — S3 Backend `encrypt = true`

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

**Answer**: C

**Explanation**:
`encrypt = true` in the S3 backend block enables **server-side encryption at rest** for the state object stored in S3. By default this uses SSE-S3 (AES-256 managed by S3). It does not configure the TLS connection (S3 always uses TLS for API calls regardless of this argument), does not encrypt in memory, and does not involve local key material. This is a recommended best-practice argument when storing Terraform state in S3 because state files may contain plaintext sensitive values.

---

### Question 2 — Module Source Git `?ref=` Query Parameter

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

**Answer**: C

**Explanation**:
For Git-based module sources, the `?ref=` query parameter pins the checkout to a specific **git ref** — a tag, branch name, or commit SHA. Here, `?ref=v2.0.0` checks out the `v2.0.0` tag. This is the Git-source equivalent of the `version` argument used with Terraform Registry sources (which cannot be used with Git URLs). The `//modules/vpc` portion before `?ref=` is the **double-slash subdirectory separator** — these are two separate mechanisms within the same URL.

---

### Question 3 — Module Output Reference with List Index

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

**Answer**: B

**Explanation**:
`module.networking.public_subnet_ids` accesses the `public_subnet_ids` output from the child module, which is a list of subnet ID strings produced by the splat expression `aws_subnet.public[*].id`. Appending `[0]` retrieves the **first element** of that list — the subnet ID string of the first public subnet. Module outputs can be indexed, iterated with `for_each`, sliced, or used in `for` expressions just like any other list or map value. This is a common pattern for selecting specific subnets from a networking module.

---

### Question 4 — DynamoDB Lock Table `hash_key = "LockID"`

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

**Answer**: B

**Explanation**:
The Terraform S3 backend writes lock entries to DynamoDB using a hardcoded item attribute named `"LockID"`. This is a **Terraform implementation requirement**, not a DynamoDB service restriction — DynamoDB accepts any valid attribute name as a hash key. If the table's `hash_key` is named anything other than `"LockID"`, Terraform cannot write or read lock items and state locking fails. This is why every S3 backend locking example uses exactly this attribute name. The `type = "S"` (String) is also required.

---

### Question 5 — Module `for_each` Map — Instance Addresses

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

**Answer**: B

**Explanation**:
When a `module` block uses `for_each`, Terraform creates one instance per collection element and addresses each using the element's key in bracket notation: `module.<label>["<key>"]`. For this map, the two instances are `module.vpc["production"]` and `module.vpc["staging"]`. Inside each instance, `each.key` holds the key string and `each.value` holds the CIDR block. This parallels `for_each` behaviour on resource blocks, where state addresses also use `resource_type.name["key"]`.

---

### Question 6 — S3 Backend `key` Argument

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

**Answer**: C

**Explanation**:
In the S3 backend, `key` is the **S3 object key** — the full path and filename within the bucket at which Terraform stores the state file. It is analogous to a file path within a directory structure. In this example, the state is stored at `s3://acme-company-tfstate/environments/production/networking.tfstate`. Multiple configurations can share a single S3 bucket by using different `key` values — for example, one per workspace or environment. The `key` has no connection to authentication keys or encryption key IDs.

---

### Question 7 — Module `count = 2` — Instance Addresses and `count.index`

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

**Answer**: A, C

**Explanation**:
When a `module` block uses `count`, instances are addressed using zero-based bracket notation: `module.web_server[0]` and `module.web_server[1]` (A is correct). Within the `module` block's own argument expressions, `count.index` is available and holds the current instance's zero-based index — exactly as it does for resource blocks. The expression `"web-${count.index}"` evaluates to `"web-0"` for the first instance and `"web-1"` for the second (C is correct). Option B uses underscores, which is incorrect syntax. Option D is incorrect — `count.index` is valid in both `resource` and `module` block expressions.

---

### Question 8 — Module `depends_on` Argument

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

**Answer**: B

**Explanation**:
`depends_on` in a `module` block creates an **explicit dependency** that forces all resources inside `module.lambda_function` to wait until `aws_iam_role_policy_attachment.lambda_logs` is fully applied. This is necessary when the dependency cannot be inferred through attribute references — here, the Lambda function needs the policy already attached (an eventual-consistency side effect) even though its arguments reference only the role ARN. Option D is incorrect: the `role_arn` reference creates a dependency on `aws_iam_role.lambda` but not on the policy attachment, which is a separate resource. `depends_on` on a module applies to all resources within that module.

---

### Question 9 — Missing Required Variable in Module Call

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

**Answer**: C

**Explanation**:
Every `variable` block without a `default` in a child module is a **required input**. The `module "database"` block provides `db_name` and `db_username` but omits `db_password`, which has no `default` value. Terraform raises a plan error identifying that the required input variable `db_password` is not set for module `database`. The `instance_class` variable (option D) is fine because it has `default = "db.t3.micro"`. Option B is incorrect — Terraform does not silently default missing required variables to `null`.

---

### Question 10 — `terraform state list` Output — Module Resource Address Format

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

**Answer**: A, B

**Explanation**:
State addresses use a dotted path where `module.<name>.` prefixes any resource inside a module. `module.vpc.aws_vpc.main` (A) is an `aws_vpc` resource named `main` inside the `vpc` module. `module.vpc.module.nat.aws_eip.nat` (B) shows two module levels: `nat` is a child module nested inside `vpc`, and within `nat` there is an `aws_eip` resource named `nat`. Option C is incorrect — `aws_security_group.web` has no `module.` prefix because it is a **root-level resource**, not inside any child module. Option D is incorrect — `public[0]` and `public[1]` are two `count`-indexed instances of the same resource within the same `vpc` module, not separate modules.

---

### Question 11 — `version = "~> 5.0"` Registry Constraint Range

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

**Answer**: C

**Explanation**:
The `~>` pessimistic constraint operator allows the rightmost version component to increment while locking the component to its left. For `"~> 5.0"` (specified as `major.minor`), the major version is locked at `5` and the minor version may freely increment: `>= 5.0` and `< 6.0`. This accepts `5.0`, `5.1`, `5.9`, `5.14`, etc., but not `6.0`. For a three-part version like `"~> 5.0.1"`, only patch versions within `5.0.x` are allowed (`>= 5.0.1`, `< 5.1.0`). The behavior scales with the specificity of the version string provided.

---

### Question 12 — Module `providers` Argument with Provider Aliases

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

**Answer**: B

**Explanation**:
The `providers` argument in a `module` block performs **provider alias mapping**: it assigns a specific root-module provider configuration (identified by its alias) to the provider slot the child module expects. Both `module.us_resources` and `module.eu_resources` use the same `./modules/regional` source, but one receives the `aws.primary` configuration (us-east-1) and the other receives `aws.secondary` (eu-west-1). Without this argument, a child module inherits the default (non-aliased) provider and cannot automatically use aliased configurations. The `providers` map does not declare version constraints, does not isolate credentials from the root, and is not required for modules that only use the default non-aliased provider.

---

### Question 13 — Nested Module Variable Passing Chain

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

**Answer**: B, D

**Explanation**:
Terraform has **no implicit variable inheritance** at any module boundary, including nested modules. The root module correctly passes `env = var.env` to `module.app`. However, within `modules/app/main.tf`, the `module "db"` block does not pass `env` to `./modules/db`. Since `variable "env"` in `modules/db` has no `default`, Terraform raises a plan error: the required input variable is not set (B is correct). Options A and C describe non-existent automatic propagation. The fix (D) is to add `env = var.env` to the `module "db"` block inside `modules/app/main.tf` — where `var.env` refers to the `env` variable declared in `modules/app/variables.tf` that was passed in from the root.

---

---

## Questions

---

### Question 1 — `import` Block `to` Argument

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

**Answer**: B

**Explanation**:
In an `import` block, `to` specifies the **Terraform resource address** — the resource type and label that will own the imported resource in state. Here, `aws_s3_bucket.media_assets` means the existing S3 bucket will be managed by a `resource "aws_s3_bucket" "media_assets"` block. The `id` argument separately provides the cloud provider's identifier for the existing resource (`"company-media-assets-2024"` — the bucket name, which is the AWS S3 resource ID format). These two arguments together tell Terraform which config block maps to which real cloud resource.

---

### Question 2 — `terraform show plan.tfplan`

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

**Answer**: C

**Explanation**:
`terraform plan -out=plan.tfplan` saves the execution plan to a binary file. `terraform show plan.tfplan` then reads that file and renders it as human-readable text showing the proposed infrastructure changes. This workflow is used in automated pipelines to separate the plan and apply steps: a human (or approval gate) reviews the output of `terraform show plan.tfplan` before the saved plan file is passed to `terraform apply plan.tfplan`. Use `terraform show -json plan.tfplan` for machine-readable output suitable for tools like Open Policy Agent.

---

### Question 3 — `TF_LOG=WARN` Message Filtering

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

**Answer**: B

**Explanation**:
`TF_LOG` sets a **minimum severity threshold**. The levels from least to most severe are: `TRACE < DEBUG < INFO < WARN < ERROR`. Setting `TF_LOG=WARN` produces messages at WARN severity and above — meaning both WARN and ERROR messages appear. INFO, DEBUG, and TRACE messages are suppressed. This is useful when you want to see only warnings and errors without the noise of detailed operational or debugging output. To silence all logging, set `TF_LOG=OFF` or unset the variable entirely.

---

### Question 4 — `terraform plan -generate-config-out` Produced File

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

**Answer**: B

**Explanation**:
The `# __generated__ by Terraform` comment and the presence of explicitly null attributes (like `bucket_prefix = null` and `force_destroy = null`) are hallmarks of Terraform's automatic config generation. This file is produced by `terraform plan -generate-config-out=generated.tf` when an `import` block references a resource that has no existing HCL configuration. Terraform calls the provider's Read function to retrieve all current attributes and writes a complete `resource` block. The team must then review, trim unnecessary nulls, and move the block into their main configuration before running `terraform apply` to complete the import.

---

### Question 5 — `cloud` Block with `tags` Workspace Selector

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

**Answer**: C

**Explanation**:
When `workspaces { tags = [...] }` is used in the `cloud` block, Terraform connects to workspaces that possess **all** of the specified tags — it is an AND condition, not OR. This configuration connects to any workspace in `acme-corp` tagged with both `component=networking` and `env=production`. A workspace tagged only with `env=production` (but not `component=networking`) would not be selected. This selector is used for configurations that should run against a dynamic set of identically-tagged workspaces rather than a single named workspace.

---

### Question 6 — `terraform_remote_state` Output Reference Value

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

**Answer**: B

**Explanation**:
`data.terraform_remote_state.<name>.outputs.<key>` evaluates to the **value stored in the remote workspace's state for the named output**. Here, the `networking-production` workspace exports `private_subnet_id = "subnet-0abc123def456"`, so `data.terraform_remote_state.networking.outputs.private_subnet_id` evaluates to the string `"subnet-0abc123def456"`. This value is then used as `output.app_subnet`. The `terraform_remote_state` data source reads outputs directly from the remote workspace's state file — no resolution or transformation occurs.

---

### Question 7 — `TF_LOG_PROVIDER=TRACE` Without `TF_LOG`

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

**Answer**: B

**Explanation**:
`TF_LOG_PROVIDER` and `TF_LOG_CORE` are independent, component-scoped overrides. When only `TF_LOG_PROVIDER=TRACE` is set (with no global `TF_LOG`), Terraform produces TRACE-level logs for **provider plugin** activity only — including all API calls made to the cloud provider. The Terraform core engine (graph walking, state management, plan generation) produces no logs because neither `TF_LOG` nor `TF_LOG_CORE` is set. This is the intended use case: debugging a misbehaving provider without the noise of core infrastructure logging.

---

### Question 8 — Sentinel Policy Snippet Interpretation

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

**Answer**: A, C

**Explanation**:
The `untagged` filter collects resources where `r.change.after.tags` is `null` or absent — `(r.change.after.tags else null) != null` evaluates to `false` for null/missing tags, so `not false` adds them to the collection. The `main` rule passes only when `untagged` is empty, meaning all modified resources carry a non-null `tags` attribute (A is correct). Option B is incorrect: a resource with `tags = {}` has a non-null (empty) map — it passes the filter and is NOT added to `untagged`. Option C is correct: `soft-mandatory` failures can be overridden by a user with the "Manage Policy Overrides" permission. Option D describes `hard-mandatory` behaviour, not `soft-mandatory`.

---

### Question 9 — `workspaces.name` vs `workspaces.tags` in `cloud` Block

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

**Answer**: A

**Explanation**:
`workspaces { name = "..." }` pins the configuration to a **single, specific workspace** by name. `workspaces { tags = [...] }` enables the configuration to work with **any workspace** in the organisation carrying the specified tag(s), turning the working directory into a workspace-agnostic configuration that selects its target at `terraform init` time. The `tags` selector is used when teams want the same root module to deploy to multiple workspaces (e.g., one per region) without hardcoding a workspace name. Options B, C, and D mischaracterise both selectors.

---

### Question 10 — `import` Block vs CLI Import Differences

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

**Answer**: A, B

**Explanation**:
The two key structural advantages of the `import` block (Method A) are: (A) it integrates into the standard plan/apply workflow, allowing `terraform plan` to preview the import before committing any state changes — Method B immediately and irrevocably modifies state; (B) it can pair with `terraform plan -generate-config-out=file.tf` to automatically generate the HCL resource block, whereas Method B only adds the resource to state and the practitioner must manually write and tune the configuration. Option C is incorrect — Method A can be used with `-generate-config-out` when no resource block exists yet. Option D is incorrect because of the plan preview and config-generation differences.

---

### Question 11 — `TF_TOKEN_app_terraform_io` vs `terraform login`

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

**Answer**: B

**Explanation**:
`TF_TOKEN_<hostname>` (with dots in the hostname replaced by underscores) is the environment variable equivalent of the credentials stored by `terraform login`. Setting it provides HCP Terraform authentication without writing any file to disk. This is the **recommended pattern for CI/CD pipelines** and automation contexts where `terraform login` is impractical (it requires interactive browser-based authentication and writes to `~/.terraform.d/credentials.tfrc.json`). The environment variable is read by all Terraform commands — `init`, `plan`, `apply` — for the duration of the process without needing to be re-exported.

---

### Question 12 — `hard-mandatory` Sentinel Policy Override Attempt by Owner

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

**Answer**: C

**Explanation**:
`hard-mandatory` is the strictest Sentinel enforcement level. When a `hard-mandatory` policy fails, the run is permanently blocked and **no override option is presented in the HCP Terraform UI** — not for Owners, not for any role. This is by design: `hard-mandatory` is used for compliance requirements that must never be bypassed (e.g., encryption, regulatory controls). The only way to unblock the run is to fix the Terraform configuration so the policy passes, or to change the policy's enforcement level (which requires policy admin access). This distinguishes it from `soft-mandatory`, where an authorised user can override the failure.

---

### Question 13 — Three Logging Variables in Combination

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

**Answer**: A, C

**Explanation**:
Component-scoped variables (`TF_LOG_CORE`, `TF_LOG_PROVIDER`) take **precedence over the global `TF_LOG`** for their respective components. `TF_LOG_CORE=ERROR` overrides `TF_LOG=TRACE` for Terraform core — only ERROR-level core messages appear (C is correct). `TF_LOG_PROVIDER=DEBUG` overrides `TF_LOG=TRACE` for provider plugins — provider logs appear at DEBUG, not TRACE (so D is incorrect). `TF_LOG_PATH=/var/log/terraform.log` redirects **all** log output from stderr to the specified file (A is correct), regardless of which levels or components are active.

---