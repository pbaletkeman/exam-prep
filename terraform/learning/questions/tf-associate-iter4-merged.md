# Terraform Associate Exam Questions

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

### Question 13 — Wrong Provider Source Address Format

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

### Question 14 — Lock File Incorrectly Added to `.gitignore`

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

### Question 15 — `~> 5.0.0` Claimed Equivalent to `~> 5.0`

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

### Question 16 — Provider Reference Written as Quoted String

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

### Question 17 — Duplicate Provider Blocks Without Alias

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

### Question 18 — `terraform state rm` Claimed to Delete Cloud Resource

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

### Question 19 — `terraform plan -refresh=false` Claimed to Detect Drift

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

### Question 20 — `required_version` Placed Inside `required_providers`

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

### Question 21 — Incorrect Claims About `terraform.tfstate.backup`

**Difficulty**: Medium
**Answer Type**: many
**Topic**: Identifying TWO errors in claims about what `terraform.tfstate.backup` stores and retains

**Question**:
A wiki article makes four claims about `terraform.tfstate.backup`. Which TWO contain errors? (Select two.)

- A) "`terraform.tfstate.backup` is automatically created before each `terraform apply` to preserve the previous state"
- B) "`terraform.tfstate.backup` maintains a rolling history of every previous state, allowing rollback to any earlier version"
- C) "Only one `terraform.tfstate.backup` file exists at a time — it is overwritten on each apply with the state from the previous apply"
- D) "`terraform.tfstate.backup` provides the same versioning capability as enabling S3 bucket versioning for a remote backend"

### Question 22 — `terraform state push` Used to Read State

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

### Question 23 — Core↔Provider Communication Described as HTTP REST

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

### Question 24 — Alias Name Mismatch Between Provider Block and Resource Reference

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

### Question 25 — `>= 5.0` Claimed Equivalent to `~> 5.0`

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

### Question 26 — `terraform validate` Claimed to Require Credentials

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

### Question 27 — `-` Plan Symbol Described as Update

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

### Question 28 — `terraform fmt -check` Claimed to Reformat Files

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

### Question 29 — `terraform init -reconfigure` Claimed to Migrate State

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

### Question 30 — `terraform plan -target` Claims About Dependencies

**Difficulty**: Medium
**Answer Type**: many
**Topic**: Identifying TWO errors in claims about how `-target` handles dependencies

**Question**:
A wiki article makes four claims about `terraform plan -target`. Which TWO contain errors? (Select two.)

- A) "Using `-target` emits a warning that the resulting plan may be incomplete and is not a reliable representation of the full configuration"
- B) "`terraform plan -target=aws_instance.web` plans only `aws_instance.web` exactly — its upstream dependencies (such as a security group or subnet it references) are excluded from the plan entirely"
- C) "`terraform plan -target` is the recommended approach for routine production applies because it limits the blast radius to only the intended resource"
- D) "The targeted resource and any resources it transitively depends on are included in the plan"

### Question 31 — `terraform graph` Output Described as JSON

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

### Question 32 — `terraform destroy` Claimed to Delete the State File

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

### Question 33 — `terraform apply` Without Saved Plan Claimed to Guarantee Reviewed Changes

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

### Question 34 — `terraform fmt` Claimed to Recurse by Default

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

### Question 35 — Wrong Conditions Claimed to Require `terraform init` Re-run

**Difficulty**: Medium
**Answer Type**: many
**Topic**: Identifying TWO conditions incorrectly listed as requiring `terraform init` to be re-run

**Question**:
A team's wiki lists five actions that it claims require re-running `terraform init`. Which TWO are **incorrectly** listed as requiring a re-run? (Select two.)

- A) Adding a new provider to `required_providers` in `main.tf`
- B) Adding a new `output` block to an existing module that the root configuration already sources
- C) Changing the `backend` block from local to a remote S3 backend
- D) Updating the `default` value of an existing `variable` block in `variables.tf`

### Question 36 — `terraform console` Claimed to Modify State

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

### Question 37 — `terraform plan` Run Before `terraform init`

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

### Question 38 — Wrong Claims About `terraform apply -replace` and `terraform taint`

**Difficulty**: Hard
**Answer Type**: many
**Topic**: Identifying TWO errors in claims comparing `terraform apply -replace` with `terraform taint`

**Question**:
A blog post makes four claims about `terraform apply -replace` and `terraform taint`. Which TWO contain errors? (Select two.)

- A) "`terraform taint` was deprecated in favour of `terraform apply -replace`, which is the recommended approach for forcing resource replacement in Terraform 1.x"
- B) "`terraform apply -replace` requires a configuration change to the targeted resource — if the configuration is unchanged, the command has no effect and Terraform skips the replacement"
- C) "Running `terraform apply -replace=<address>` causes the plan output to show a `-/+` symbol for the targeted resource, indicating destroy-then-recreate"
- D) "`terraform apply -replace` can only be used in conjunction with `terraform plan -out` — the saved plan file is required to invoke the replace behaviour"

### Question 39 — `data` Block Claimed to Create Resources

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

### Question 40 — `create_before_destroy` Described as the Default Behaviour

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

### Question 41 — `count` and `for_each` Claimed Usable Together

**Difficulty**: Medium
**Answer Type**: many
**Topic**: Identifying TWO errors in claims about the `count` and `for_each` meta-arguments

**Question**:
A wiki article makes four claims about Terraform meta-arguments. Which TWO contain errors? (Select two.)

- A) "A resource block can use both `count` and `for_each` simultaneously — `count` controls how many copies exist while `for_each` provides a named key for each copy, allowing combined matrix-style resource creation"
- B) "With `count = 3`, the valid values of `count.index` are 0, 1, and 2 — indexing starts at zero, so the third instance has `count.index = 2`"
- C) "`for_each` accepts a plain `list(string)` value directly, without requiring any type conversion — Terraform iterates over the list elements natively"
- D) "When `for_each` is assigned a `map`, `each.key` holds the map key and `each.value` holds the corresponding map value for each iteration"

### Question 42 — Implicit Dependency Described as Requiring `depends_on`

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

### Question 43 — `prevent_destroy` Claimed to Block `terraform state rm`

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

### Question 44 — `ignore_changes` Claimed to Hide Resource from `terraform plan`

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

### Question 45 — `count.index` Starting Value Claimed as 1

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

### Question 46 — Wrong Claims About `depends_on` on a Data Source

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

### Question 47 — Resource `id` Attribute Claimed to Be User-Defined

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

### Question 48 — `for_each` with a `list(string)` Variable

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

### Question 49 — `depends_on` Claimed to Override Lifecycle Hooks

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

### Question 50 — Wrong Claims About the `removed` Block

**Difficulty**: Hard
**Answer Type**: many
**Topic**: Identifying TWO errors in claims about the `removed` block's behaviour

**Question**:
A Terraform 1.7+ runbook makes four claims about the `removed` block. Which TWO contain errors? (Select two.)

- A) "The `removed` block with `lifecycle { destroy = false }` stops Terraform from managing the resource but leaves the real cloud resource running and unaffected in the provider account"
- B) "A `removed` block with `lifecycle { destroy = false }` deletes both the Terraform state entry **and** the real cloud resource — the `destroy = false` setting only suppresses the interactive confirmation prompt before deletion"
- C) "After `terraform apply` successfully processes a `removed` block, the block must remain in the configuration permanently to prevent future `terraform plan` runs from flagging the resource address as unknown and attempting to recreate it"
- D) "After `terraform apply` processes a `removed` block, the block can be safely deleted from the configuration — subsequent plans will not attempt to recreate or re-manage the resource because it is no longer in state"

### Question 51 — `replace_triggered_by` Claimed to Work on Data Sources

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

### Question 52 — Flawed Claim: `default` Sets the Type

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

### Question 53 — Flawed Claim: `sensitive = true` Encrypts State

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

### Question 54 — Flawed Claim: Locals Are Evaluated at Apply Time Only

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

### Question 55 — Flawed Claim: `output sensitive = true` Removes Value from State

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

### Question 56 — Flawed Variable Precedence Order

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

### Question 57 — Flawed Claim: `toset()` Preserves List Order

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

### Question 58 — Flawed Claim: `for` on a Map Always Produces a List

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

### Question 59 — Flawed Claim: `lookup()` Default Argument Is Optional

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

### Question 60 — Flawed Claim: `merge()` Deep-Merges Nested Maps

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

### Question 61 — Flawed Claim: `nonsensitive()` Permanently Removes Sensitive Marking from State

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

### Question 62 — Flawed Claim: `coalesce()` and `coalescelist()` Are Interchangeable

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

### Question 63 — Flawed Claim: `can()` Returns the Value on Success

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

### Question 64 — Flawed Claim: `length()` on `null` Returns Zero

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

### Question 65 — Flawed Claim: `check` Block Failure Blocks Apply

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

### Question 66 — Flawed Claim: `validation` Runs During Apply

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

### Question 67 — Flawed HCL: `validation` Condition References a Local

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

### Question 68 — Flawed Claim: `self` Available in `precondition`

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

### Question 69 — Flawed Claim: `check` Block Introduced in Terraform 1.3

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

### Question 70 — Flawed Claim: Failed `postcondition` Destroys Resource and Removes from State

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

### Question 71 — Flawed HCL: `precondition` Placed Outside `lifecycle` Block

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

### Question 72 — Two Flawed Claims About `check` Block Structure

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

### Question 73 — Flawed Claim: Sensitive Variable Propagates Automatically to Output

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

### Question 74 — Two Flawed Claims About Condition Mechanism Failure Behaviour

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

### Question 75 — Flawed Claim: Scoped `data` Source in `check` Block Has Fatal Errors Like Top-Level `data`

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

### Question 76 — Two Flawed Claims About Retrieving Sensitive Output Values

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

### Question 77 — Flawed Claim: `version` Argument Valid with GitHub Module Source

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

### Question 78 — Flawed HCL: Module Output Referenced with Wrong Syntax

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

### Question 79 — Flawed Claim: `.terraform/modules/` Should Be Committed to Git

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

### Question 80 — Flawed Claim: `terraform init` Is a One-Time Step

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

### Question 81 — Flawed HCL: DynamoDB Lock Table with Wrong `hash_key` Attribute Name

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

### Question 82 — Flawed Claim: `terraform state rm` Deletes the Cloud Resource

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

### Question 83 — Flawed Claim: `terraform plan -refresh-only` Updates the State File

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

### Question 84 — Flawed Claim: Every Child Module Requires Its Own `provider` Block

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

### Question 85 — Flawed HCL: `version` Constraint on Local Path Module Source

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

### Question 86 — Two Errors in `for_each` Module Block

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

### Question 87 — Two Flawed Claims About `terraform.tfstate.backup`

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

### Question 88 — Flawed Claim: `terraform state push` Prompts Before Overwriting

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

### Question 89 — Two Errors About `terraform state mv` and `moved` Blocks

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

### Question 90 — CLI Import and HCL Generation

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

### Question 91 — TF_LOG Default Output Destination

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

### Question 92 — Swapped `import` Block Arguments

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

### Question 93 — `cloud` Block and `backend` Block Coexistence

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

### Question 94 — Sentinel Enforcement Level Descriptions

**Difficulty**: Medium
**Answer Type**: many
**Topic**: Distinguishing `advisory`, `soft-mandatory`, and `hard-mandatory` enforcement level behaviour

**Question**:
A team lead explains Sentinel policy enforcement levels to new engineers. Which TWO of the following statements contain an error? (Select two.)

- A) The `advisory` enforcement level logs a warning when a policy fails but allows the run to continue — it does not block the apply
- B) The `advisory` enforcement level blocks the apply when a policy fails — it is less strict than `soft-mandatory` only because the failure is displayed as a warning rather than a hard stop
- C) There is no mechanism to override a `soft-mandatory` policy failure — once blocked, the only resolution is to fix the configuration or remove the policy
- D) The `hard-mandatory` enforcement level blocks the run and provides no override mechanism — not even organisation Owners can bypass a `hard-mandatory` failure

### Question 95 — Health Assessment Auto-Apply Claim

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

### Question 96 — Speculative Plan Approval Claim

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

### Question 97 — `terraform login` Token Storage Location

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

### Question 98 — HCP Terraform Audit Log Properties

**Difficulty**: Medium
**Answer Type**: many
**Topic**: The immutability and exportability of HCP Terraform audit logs

**Question**:
A compliance officer reviews HCP Terraform's audit logging capabilities. Which TWO of the following statements about HCP Terraform audit logs contain an error? (Select two.)

- A) Every action taken in an HCP Terraform organisation is logged, including run triggers, variable changes, team membership updates, and policy overrides
- B) Organisation Owners can edit or redact audit log entries containing sensitive information before exporting them to external systems
- C) Audit logs are immutable — no user, including Owners, can modify or delete individual log entries
- D) Audit logs are stored internally within HCP Terraform and cannot be exported to external SIEM or log management systems

### Question 99 — `import` Block Workflow Step Order

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

### Question 100 — `terraform state list` Capabilities

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

### Question 101 — HCP Terraform Private Registry Source Address

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

### Question 102 — Dynamic Provider Credentials (OIDC) Misconceptions

**Difficulty**: Hard
**Answer Type**: many
**Topic**: How OIDC dynamic provider credentials work and what they replace in HCP Terraform

**Question**:
An engineer prepares training material on dynamic provider credentials. Which TWO of the following statements contain an error? (Select two.)

- A) With OIDC dynamic credentials, no long-lived static cloud credentials (e.g., AWS access key + secret key) need to be stored in HCP Terraform workspace variables — each run receives a short-lived token scoped to that run
- B) OIDC trust is established by storing the cloud provider's OIDC client secret as a sensitive environment variable in HCP Terraform — HCP Terraform presents this secret to authenticate itself to the cloud provider during each run
- C) When a run begins, HCP Terraform generates a signed JWT (JSON Web Token) that it presents to the cloud provider; the cloud provider validates the token against its configured OIDC trust relationship with HCP Terraform's issuer endpoint
- D) OIDC dynamic credentials are available for any Terraform provider registered in the public registry — any provider that supports AWS-compatible API calls can automatically use OIDC authentication with HCP Terraform



## Answer Key

| Q# | Answer(s) | Explanation | Source | Difficulty |
|---|---|---|---|---|
| 2 | B | N/A | Identifying the error in a definition of idempotency | Easy |
| 3 | C | N/A | Identifying the error in a claim that `count = 0` is invalid syntax | Easy |
| 4 | B | N/A | Identifying the error in conflating the state file with desired state | Medium |
| 5 | C | N/A | Identifying the error in a definition of infrastructure drift | Medium |
| 6 | C | N/A | Identifying the error in classifying Terraform as a configuration management tool | Medium |
| 7 | B | N/A | Identifying the error in a claim that CloudFormation supports multi-cloud | Medium |
| 8 | B, D | N/A | Identifying TWO incorrect statements from a list of IaC benefit claims | Medium |
| 9 | B | N/A | Identifying the error in claiming IaC removes the need for auditing | Medium |
| 10 | C, D | N/A | Identifying TWO incorrect statements about declarative and imperative IaC approaches | Medium |
| 11 | B | N/A | Identifying the error in swapping "current state" and "desired state" definitions | Medium |
| 12 | B | N/A | Identifying the error in applying idempotency to mean "zero changes always" | Hard |
| 13 | B, D | N/A | Identifying TWO incorrect claims in a developer's description of how declarative Terraform works | Hard |
| 14 | B | N/A | Identifying a GitHub URL used incorrectly as a provider source address | Easy |
| 15 | C | N/A | Identifying the error in treating `.terraform.lock.hcl` the same as `.terraform/` | Easy |
| 16 | C | N/A | Identifying the error in claiming two different pessimistic constraints allow the same range | Medium |
| 17 | B | N/A | Identifying the error in using a quoted string for the `provider` meta-argument | Medium |
| 18 | A, C | N/A | Identifying TWO correct statements about what is wrong with duplicate provider blocks that lack an alias | Medium |
| 19 | C | N/A | Identifying the error in claiming `terraform state rm` removes the resource from both state and the cloud | Medium |
| 20 | C | N/A | Identifying the error in using `-refresh=false` for infrastructure drift monitoring | Medium |
| 21 | C | N/A | Identifying the error in placing `required_version` inside a provider object in `required_providers` | Medium |
| 22 | B, D | N/A | Identifying TWO errors in claims about what `terraform.tfstate.backup` stores and retains | Medium |
| 23 | C | N/A | Identifying the error in confusing `terraform state push` with `terraform state pull` | Medium |
| 24 | C | N/A | Identifying the error in claiming Terraform Core communicates with provider plugins via HTTP REST | Hard |
| 25 | A, B | N/A | Identifying TWO problems caused by an alias mismatch between a provider block and a resource's `provider` argument | Hard |
| 26 | C | N/A | Identifying the error in claiming `>=` and `~>` produce the same version selection behaviour | Hard |
| 27 | C | N/A | Identifying the error in claiming `terraform validate` needs cloud provider credentials | Easy |
| 28 | B | N/A | Identifying the error in claiming the `-` plan symbol means an in-place update | Easy |
| 29 | C | N/A | Identifying the error in claiming `terraform fmt -check` writes formatting changes to disk | Medium |
| 30 | C | N/A | Identifying the error in using `-reconfigure` when state migration is required | Medium |
| 31 | B, C | N/A | Identifying TWO errors in claims about how `-target` handles dependencies | Medium |
| 32 | C | N/A | Identifying the error in claiming `terraform graph` produces JSON output | Medium |
| 33 | C | N/A | Identifying the error in claiming `terraform destroy` removes the state file after execution | Medium |
| 34 | C | N/A | Identifying the error in claiming `terraform apply` without a plan file applies exactly what `terraform plan` showed | Medium |
| 35 | C | N/A | Identifying the error in claiming `terraform fmt` includes subdirectories without a flag | Medium |
| 36 | B, D | N/A | Identifying TWO conditions incorrectly listed as requiring `terraform init` to be re-run | Medium |
| 37 | C | N/A | Identifying the error in claiming `terraform console` writes to the state file when expressions are evaluated | Medium |
| 38 | C | N/A | Identifying the error in a workflow that runs `terraform plan` before `terraform init` | Hard |
| 39 | B, D | N/A | Identifying TWO errors in claims comparing `terraform apply -replace` with `terraform taint` | Hard |
| 40 | C | N/A | Identifying the error in claiming a `data` block provisions infrastructure | Easy |
| 41 | C | N/A | Identifying the error in claiming Terraform's default replacement order is create-then-destroy | Easy |
| 42 | A, C | N/A | Identifying TWO errors in claims about the `count` and `for_each` meta-arguments | Medium |
| 43 | C | N/A | Identifying the error in claiming `depends_on` is required for attribute-reference dependencies | Medium |
| 44 | C | N/A | Identifying the error in claiming `prevent_destroy` protects against `terraform state rm` | Medium |
| 45 | C | N/A | Identifying the error in claiming `ignore_changes = all` makes a resource invisible to plan | Medium |
| 46 | C | N/A | Identifying the error in a comment claiming `count.index` starts at 1 | Medium |
| 47 | A, C | N/A | Identifying TWO errors in claims about adding `depends_on` to a `data` block | Medium |
| 48 | C | N/A | Identifying the error in claiming the `id` attribute of a managed resource can be set in HCL | Medium |
| 49 | C | N/A | Identifying the error in using a list-type variable directly with `for_each` | Medium |
| 50 | C | N/A | Identifying the error in claiming `depends_on` can override `prevent_destroy` | Hard |
| 51 | B, C | N/A | Identifying TWO errors in claims about the `removed` block's behaviour | Hard |
| 52 | C | N/A | Identifying the error in claiming `replace_triggered_by` is valid in a `data` block's `lifecycle` | Medium |
| 53 | C | N/A | What `default` does vs what `type` does in a variable block | Easy |
| 54 | B | N/A | What `sensitive = true` on a variable actually does vs does not do | Easy |
| 55 | B | N/A | When `locals` are evaluated in the Terraform workflow | Easy |
| 56 | B | N/A | What `sensitive = true` on an output block does vs does not do | Medium |
| 57 | B | N/A | Correct ordering of variable input precedence (highest to lowest) | Medium |
| 58 | B | N/A | What `toset()` does to ordering when converting a list | Medium |
| 59 | B | N/A | What output type a `for` expression produces based on its delimiter | Medium |
| 60 | B | N/A | Whether the default argument to `lookup()` is required or optional | Medium |
| 61 | B | N/A | How `merge()` handles nested map keys (shallow vs deep merge) | Medium |
| 62 | B | N/A | What `nonsensitive()` does and does not affect | Medium |
| 63 | B | N/A | Distinguishing `coalesce()` from `coalescelist()` and their input types | Hard |
| 64 | A, C | N/A | What `can()` returns vs what `try()` returns | Hard |
| 65 | B | N/A | What `length()` does when called with a `null` argument | Medium |
| 66 | B | N/A | Whether a failing `check` block assertion blocks `terraform apply` | Easy |
| 67 | B | N/A | When variable `validation` blocks are evaluated in the Terraform workflow | Easy |
| 68 | B | N/A | What a `validation` block's `condition` is allowed to reference | Medium |
| 69 | B | N/A | Which lifecycle condition blocks allow use of the `self` reference | Medium |
| 70 | B | N/A | Which Terraform version introduced the `check` block | Medium |
| 71 | B | N/A | What happens to a resource in AWS and in state when its `postcondition` fails | Medium |
| 72 | B | N/A | Where `precondition` and `postcondition` blocks must be declared inside a resource | Medium |
| 73 | A, C | N/A | Where `check` blocks can be placed and whether a scoped `data` source is required | Medium |
| 74 | B | N/A | Whether `sensitive = true` on a variable automatically marks referencing outputs as sensitive | Medium |
| 75 | A, C | N/A | When and how `validation`, `precondition`, and `check` failures are raised | Hard |
| 76 | B | N/A | How errors from a scoped `data` source inside a `check` block differ from top-level `data` source errors | Hard |
| 77 | A, C | N/A | Which `terraform output` command forms expose sensitive output values in plaintext | Medium |
| 78 | B | N/A | Which module source types support the `version` argument | Easy |
| 79 | B | N/A | Correct syntax for referencing a child module's output in the root module | Easy |
| 80 | B | N/A | Whether the `.terraform/modules/` directory should be committed to version control | Medium |
| 81 | B | N/A | When `terraform init` must be re-run within an existing workspace | Medium |
| 82 | B | N/A | The required partition key attribute name for a DynamoDB table used for S3 backend state locking | Medium |
| 83 | B | N/A | What `terraform state rm` does and does not do to the cloud resource | Medium |
| 84 | B | N/A | Whether `terraform plan -refresh-only` writes any changes to the state file | Medium |
| 85 | B | N/A | How provider configuration flows to child modules in Terraform | Medium |
| 86 | B | N/A | Identifying that `version` is invalid alongside a local path module source | Medium |
| 87 | A, C | N/A | Errors when using `count.index` in a `for_each` module and accessing instances with a numeric index | Medium |
| 88 | A, C | N/A | The scope and content of `terraform.tfstate.backup` and when it is created | Medium |
| 89 | B | N/A | Whether `terraform state push` provides safety prompts before overwriting remote state | Hard |
| 90 | A, C | N/A | What `terraform state mv` does and does not modify, and what `moved` blocks can address | Hard |
| 91 | B | N/A | Whether the CLI `terraform import` command supports the `-generate-config-out` flag | Easy |
| 92 | B | N/A | Where Terraform writes log output when `TF_LOG` is set but `TF_LOG_PATH` is not | Easy |
| 93 | B | N/A | Correct use of the `to` and `id` arguments in a declarative `import` block | Medium |
| 94 | A | N/A | Whether `cloud` and `backend` blocks can be used together in the same `terraform {}` block | Medium |
| 95 | B, C | N/A | Distinguishing `advisory`, `soft-mandatory`, and `hard-mandatory` enforcement level behaviour | Medium |
| 96 | B | N/A | What HCP Terraform health assessments do when they detect drift, and what they cannot do | Medium |
| 97 | A | N/A | The lifecycle limitations of speculative plans in HCP Terraform | Medium |
| 98 | C | N/A | Where `terraform login` stores the HCP Terraform API token on disk | Medium |
| 99 | B, D | N/A | The immutability and exportability of HCP Terraform audit logs | Medium |
| 100 | B | N/A | The correct sequence of steps when using a declarative `import` block with `-generate-config-out` | Medium |
| 101 | B | N/A | What `terraform state list` outputs versus what `terraform state show` outputs | Medium |
| 102 | B | N/A | Correct source address format for modules published to the HCP Terraform private registry | Hard |
| 103 | B, D | N/A | How OIDC dynamic provider credentials work and what they replace in HCP Terraform | Hard |
