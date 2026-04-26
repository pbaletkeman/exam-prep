# Terraform Associate Exam Questions

### Question 1 — Nightly Apply Reports No Changes

**Difficulty**: Easy
**Answer Type**: one
**Topic**: Idempotency — "No changes" as expected and correct behaviour

**Scenario**:
A platform team has automated their CI/CD pipeline to run `terraform apply` every night at midnight against their production environment. On most mornings, the apply summary shows "No changes. Infrastructure is up-to-date." A junior engineer on the team is alarmed and opens a ticket saying the Terraform step in the pipeline appears broken because it never seems to do anything useful. The team lead needs to explain what is actually happening.

**Question**:
What does the "No changes. Infrastructure is up-to-date." output most accurately indicate?

- A) Terraform has lost connectivity to the state backend and cannot compare resources
- B) The infrastructure currently matches the desired state defined in the configuration files
- C) The nightly apply is being silently skipped due to a missing state lock file
- D) Terraform is operating in plan-only mode and is not permitted to execute changes

### Question 2 — New Engineer Told to "Read the Repo"

**Difficulty**: Easy
**Answer Type**: one
**Topic**: IaC as living documentation of infrastructure

**Scenario**:
A new site reliability engineer joins a company that has managed all its cloud infrastructure with Terraform for the past two years. The team maintains no architecture diagrams, no wikis, and no runbooks. On their first day, the tech lead tells the new engineer: "If you want to understand what infrastructure we run and how it is configured, just read the Terraform repository." The new engineer is unsure what value reading `.tf` files actually provides compared to, say, a written document or a diagram.

**Question**:
Which benefit of IaC most directly justifies the tech lead's instruction?

- A) Terraform configurations serve as living documentation of the infrastructure, reflecting its current desired state in a human-readable, version-controlled format
- B) Terraform logs every `apply` operation to a structured log file that describes the current state of each resource in prose
- C) Terraform automatically generates architecture diagrams and HTML documentation from HCL resource blocks
- D) Reading `.tf` files allows the engineer to run a simulation of the infrastructure locally without cloud credentials

### Question 3 — Incident Workaround Overwritten on Monday Morning

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Terraform enforces desired state — manual out-of-band changes are reverted on next apply

**Scenario**:
During a production incident late on a Friday night, an on-call engineer manually increases the minimum instance count of an Auto Scaling Group from `2` to `5` through the AWS Management Console to absorb a traffic spike. The incident is resolved and the engineer goes home for the weekend without updating the Terraform configuration. On Monday morning, a different team member runs `terraform apply` from the unchanged Git repository, which still declares `min_size = 2` for that Auto Scaling Group.

**Question**:
What does Terraform do when `terraform apply` is executed on Monday morning?

- A) Terraform detects the inconsistency but refuses to apply because the state file is stale and must be manually refreshed first
- B) Terraform reports "No changes" because the Auto Scaling Group already has a higher capacity than required
- C) Terraform reverts the Auto Scaling Group `min_size` back to `2` to match the desired state in the configuration
- D) Terraform imports the manual change into the state file and automatically updates the `.tf` configuration to `min_size = 5`

### Question 4 — Company Expanding from AWS to Azure and GCP

**Difficulty**: Medium
**Answer Type**: one
**Topic**: CloudFormation is AWS-only; Terraform provides multi-cloud support

**Scenario**:
A company has managed all of its AWS infrastructure with AWS CloudFormation for three years. They have just signed commercial agreements to run their analytics platform on Google Cloud Platform (GCP) and their disaster recovery environment on Microsoft Azure. The infrastructure team is evaluating whether they can continue using CloudFormation as their single IaC tool across all three cloud providers, or whether they need to adopt a different toolchain.

**Question**:
What is the most accurate assessment of this situation?

- A) CloudFormation supports GCP and Azure resource types through AWS Marketplace provider extensions
- B) CloudFormation is limited to AWS and cannot manage resources on GCP or Azure; the team needs a multi-cloud IaC tool such as Terraform to manage all three providers in a unified workflow
- C) CloudFormation supports multi-cloud deployments through its StackSets feature, which can federate API calls to external cloud providers
- D) CloudFormation can manage Azure resources natively using ARM template integration but requires a third-party plugin for GCP

### Question 5 — Accidental `terraform destroy` on the Wrong Workspace

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Disaster recovery using IaC — restoring infrastructure from configuration and state backup

**Scenario**:
A team member on a Friday afternoon accidentally runs `terraform destroy` on the production workspace instead of the development workspace. All 47 cloud resources in production — including VMs, databases, and networking — are destroyed within minutes. Fortunately, the team stores their Terraform configuration files in a Git repository and keeps automated daily backups of the state file in an S3 bucket. The most recent state backup is from the previous night.

**Question**:
What is the most accurate description of the recovery procedure and expected outcome?

- A) The team must manually recreate all 47 resources through the AWS console because `terraform destroy` is irreversible and cannot be undone with Terraform
- B) The team should restore the backed-up state file to the backend, then run `terraform apply` from the Git repository; Terraform will recreate all 47 resources to match the configuration
- C) The team can run `terraform apply` immediately without restoring the state file; Terraform will automatically detect the missing resources and recreate them without any risk
- D) The team must re-run `terraform init` to recover the provider plugins and configuration from the remote backend before resources can be recreated

### Question 6 — Bash Script vs Terraform for Provisioning EC2 Instances

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Idempotency contrast — imperative scripting vs declarative Terraform

**Scenario**:
Two engineers on the same team are each tasked with provisioning 3 EC2 instances for a new project. Engineer A writes a Bash script that calls `aws ec2 run-instances` three times. Engineer B writes a Terraform HCL configuration with an `aws_instance` resource block and `count = 3`. Both engineers run their solutions successfully and the 3 instances are created. A week later, both engineers are asked to re-run their respective solutions without making any code changes, to verify the desired number of instances is still in place.

**Question**:
What is the most likely difference in outcome when both solutions are re-run?

- A) Engineer A's Bash script creates 3 additional instances (6 total); Engineer B's `terraform apply` reports "No changes" because the infrastructure already matches the desired state
- B) Both solutions skip the creation step and report success, because all modern cloud automation tools are idempotent by design
- C) Engineer B's `terraform apply` fails with a conflict error because the 3 instances already exist in the cloud
- D) Engineer A's Bash script fails because the AWS CLI detects duplicate instance names and returns a `DuplicateResource` error

### Question 7 — Staging Environment Diverges from Production

**Difficulty**: Medium
**Answer Type**: many
**Topic**: Infrastructure drift and repeatability — restoring environment parity via Terraform apply

**Scenario**:
A QA engineer reports that a new feature works correctly in production but fails consistently in the staging environment. An investigation reveals that the staging environment was last updated via `terraform apply` four months ago, but since then several team members have made direct changes to staging through the AWS console to test configuration variations. The production environment has been consistently managed through Terraform with no manual changes throughout the same period. The team wants to understand what went wrong and how to fix it.

**Question**:
Which TWO statements most accurately describe the root cause and the correct remediation?

- A) The staging environment has drifted from the desired state defined in the Terraform configuration, caused by out-of-band manual changes that Terraform was not used to make
- B) The production environment is equally affected by drift because Terraform cannot reliably prevent parity issues across environments
- C) Running `terraform apply` against the staging environment using the same configuration as production will reconcile the staging environment to the desired state, restoring parity
- D) The team must use `terraform taint` on all staging resources to force a full replacement before running `apply`

### Question 8 — Compliance Audit Requests Change History

**Difficulty**: Medium
**Answer Type**: one
**Topic**: IaC audit trail — Git commit history and pull request records as compliance evidence

**Scenario**:
A compliance officer is conducting a security audit and asks an infrastructure team to provide three specific pieces of information about a database security group change made approximately six months ago: (1) who authorized the change, (2) who implemented the change, and (3) what the exact before and after configuration looked like. The team manages all infrastructure with Terraform, and all configuration changes go through GitHub pull requests with required peer review before merging to the main branch.

**Question**:
Which single artifact from the team's IaC workflow most directly provides all three pieces of required information?

- A) The Terraform state file stored in the remote backend, which records each resource's current and previous configurations
- B) The GitHub pull request and associated Git commit history for the relevant `.tf` file, which records the author, reviewer approvals, and the configuration diff
- C) The `terraform.log` output file generated automatically during the `apply` run that changed the security group
- D) The cloud provider's native activity log (e.g., AWS CloudTrail), which records every API call made to modify the security group

### Question 9 — Choosing Tools for a Two-Layer Automation Stack

**Difficulty**: Medium
**Answer Type**: many
**Topic**: Provisioning tools vs configuration management tools — Terraform and Ansible in a full-stack workflow

**Scenario**:
A startup is building a new microservices platform and needs to automate two distinct infrastructure layers: (1) provisioning cloud resources including virtual machines, VPCs, subnets, load balancers, and RDS databases on AWS; and (2) installing and configuring application runtimes, software packages, and configuration files on those virtual machines after they are provisioned. The platform team is selecting tools for each layer and wants to use purpose-built tools that follow industry best practices.

**Question**:
Which TWO tools are most appropriate for this two-layer automation approach?

- A) Terraform for provisioning cloud resources (virtual machines, networking, databases, and load balancers)
- B) AWS CloudFormation for installing and configuring software packages and application runtimes on provisioned VMs
- C) Ansible for installing and configuring software packages, application runtimes, and configuration files on the VMs after provisioning
- D) Chef for provisioning cloud VMs, networking, and databases directly from its recipe definitions

### Question 10 — Scaling Up from 3 to 5 EC2 Instances

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Desired state vs current state — Terraform computes the minimal change set

**Scenario**:
An engineer is managing an application deployment. The infrastructure was originally provisioned with `count = 3` for an `aws_instance` resource, and all three instances are currently running and healthy. Due to increased load, the engineer updates the Terraform configuration to set `count = 5` and runs `terraform plan` to preview the changes before applying.

**Question**:
What output does `terraform plan` most likely produce, and what does it reveal about Terraform's behaviour?

- A) `Plan: 5 to add, 3 to destroy, 0 to change` — Terraform always destroys existing instances and recreates all of them when the count changes
- B) `Plan: 2 to add, 0 to change, 0 to destroy` — Terraform computes only the minimal changes needed to bring the current state to the desired state
- C) `Plan: 0 to add, 3 to change, 0 to destroy` — Terraform modifies the existing three instances in place to increase their individual capacity
- D) `Plan: 5 to add, 0 to change, 0 to destroy` — Terraform ignores the 3 existing instances because they were created before the count argument was declared

### Question 11 — Engineer Describes Terraform as a Sophisticated Shell Script

**Difficulty**: Hard
**Answer Type**: one
**Topic**: Terraform's declarative model — engineers declare desired end state, not execution steps

**Scenario**:
A senior developer who is new to Terraform is explaining the tool to the rest of the team: "Terraform works like a sophisticated shell script. You write HCL blocks to describe each step that Terraform should execute — create this resource first, then that one, then set up this dependency. Terraform reads the steps in your configuration and executes them in the order you wrote them." A Terraform engineer on the team disagrees with this explanation and offers a correction.

**Question**:
Which statement most accurately describes why the senior developer's explanation is incorrect and what the correct model is?

- A) The senior developer is incorrect only about execution order; Terraform does execute steps, but it uses alphabetical ordering of resource labels rather than the order they appear in the file
- B) The senior developer is incorrect; HCL is a declarative language — engineers describe the desired end state of infrastructure, not the steps to create it. Terraform builds a dependency graph and determines execution order automatically
- C) The senior developer is correct; Terraform is fundamentally an imperative tool that reads and executes resource creation steps in the sequence they appear in the configuration files
- D) The senior developer is incorrect only about ordering; `depends_on` declarations are required for all resources, and without them Terraform creates blocks in a random order

### Question 12 — Security Team Wants Safe Drift Detection in Production

**Difficulty**: Hard
**Answer Type**: many
**Topic**: Drift detection without making changes — `terraform plan` and `terraform plan -refresh-only`

**Scenario**:
A security team at a financial services firm wants to implement a regular automated drift detection process for their Terraform-managed AWS infrastructure. Their specific goal is to identify cases where team members have made unauthorized changes directly in the AWS console — such as adding ingress rules to security groups or changing instance types — without applying any remediation changes. The process must be safe to run against the production environment at any time without risking unintended modifications to running infrastructure.

**Question**:
Which TWO Terraform actions correctly support safe drift detection without modifying infrastructure?

- A) Run `terraform plan` — Terraform refreshes the actual cloud resource state, compares it to the configuration, and shows any differences as proposed changes without modifying anything
- B) Run `terraform apply -auto-approve` — this applies all detected differences immediately and is the most efficient way to both detect and remediate drift in a single step
- C) Run `terraform plan -refresh-only` — this updates the in-memory view of current state and reports differences between the state file and actual cloud resources, without planning any configuration-driven changes
- D) Delete the `terraform.tfstate` file and run `terraform init` to force Terraform to re-scan all cloud resources and rebuild state from scratch

### Question 13 — Provider Schema Validation Catches Typo Before API Call

**Difficulty**: Easy
**Answer Type**: one
**Topic**: Provider validates resource configuration against a schema before contacting the cloud API

**Scenario**:
A developer is writing a new Terraform configuration to deploy an EC2 instance. They accidentally mistype the argument name, writing `instence_type = "t3.micro"` instead of `instance_type`. When they run `terraform validate`, Terraform immediately reports an error: `An argument named "instence_type" is not expected here.` No AWS API calls are made during this error. The developer is surprised that Terraform knows the argument is invalid without connecting to AWS.

**Question**:
What does this behaviour demonstrate about the Terraform provider's role in the workflow?

- A) Terraform Core independently maintains a built-in schema for all AWS resource types and performs all validation internally, without consulting the provider binary
- B) The AWS provider plugin contains a schema defining valid arguments and their types for each resource; Terraform validates configuration against this provider-supplied schema before contacting any cloud API
- C) Terraform queries the AWS EC2 API to retrieve the list of valid instance arguments, then compares the configuration against the API's live response to detect the typo
- D) The validation error is generated by reading `.terraform.lock.hcl` to compare the config against the installed provider version metadata

### Question 14 — Same Resource Type Deployed Across Three AWS Accounts

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Provider aliases required when multiple configurations of the same provider type are needed

**Scenario**:
A platform engineer wants to write a single Terraform configuration that provisions an identical S3 bucket in three separate AWS accounts (development, staging, and production) in a single `terraform apply`. They declare three `provider "aws"` blocks — one without an alias for development (the default), and two with the aliases `staging` and `production`, each assuming a different IAM role. They then write three `aws_s3_bucket` resource blocks, one for each account.

**Question**:
What must the resource blocks for the staging and production S3 buckets include, and why?

- A) Each resource block must include `count = 1` to indicate it belongs to a unique provider configuration
- B) Resources automatically distribute across multiple `provider "aws"` blocks in declaration order when more than one provider block is defined for the same provider type
- C) Each resource block that should use a non-default provider must include a `provider` meta-argument in the format `provider = aws.<alias>`, explicitly referencing the correct aliased configuration
- D) A `for_each` over the list of account aliases automatically assigns each resource iteration to the corresponding provider configuration with the matching alias name

### Question 15 — Security Auditor Finds Database Password in Plaintext in S3 State

**Difficulty**: Hard
**Answer Type**: many
**Topic**: `sensitive = true` masks terminal output only; state stores data in plaintext; backend encryption required for at-rest protection

**Scenario**:
A team stores Terraform state in an S3 bucket that has no server-side encryption configured. Their `output "db_password"` block includes `sensitive = true`. During a quarterly security audit, the auditor downloads the `terraform.tfstate` file directly from S3 and finds the production database password stored in plaintext within the JSON. The development team's lead argues that this is impossible because they used `sensitive = true` specifically to protect the password. The security officer states the team has a fundamental misunderstanding of what `sensitive = true` does.

**Question**:
Which TWO statements accurately describe the situation?

- A) `sensitive = true` on an output block only prevents the value from being displayed in terminal output during `terraform plan` and `terraform apply`; it does not encrypt or redact the value in the state file
- B) `sensitive = true` automatically applies AES-256 encryption to the value before Terraform writes it to any backend, protecting it at rest in S3
- C) To protect sensitive values at rest, the team must use an encrypted backend (such as S3 with server-side encryption enabled) or avoid storing secrets in Terraform state by retrieving them dynamically from a secrets manager such as HashiCorp Vault
- D) The value is only encrypted in state when `terraform apply` is run with the `-encrypt-state` flag alongside the sensitive output declaration

### Question 16 — "Error Acquiring the State Lock" During a Deployment

**Difficulty**: Easy
**Answer Type**: one
**Topic**: State locking prevents concurrent applies and protects state integrity

**Scenario**:
Two senior engineers at a company share a single Terraform workspace backed by a remote S3 backend with DynamoDB locking. On a release day, both engineers run `terraform apply` within seconds of each other. Engineer A's apply begins normally. Engineer B's terminal immediately shows: `Error acquiring the state lock. Lock Info: ID: 8f3c7b2a... Created: 2026-04-26 14:30:01`. A junior engineer watching over Engineer B's shoulder is alarmed and asks whether the infrastructure is now in a broken state.

**Question**:
What is the most accurate response to the junior engineer's concern?

- A) The error indicates both applies are running in parallel and interleaving their changes, which will corrupt the infrastructure state
- B) The error indicates the DynamoDB table used for locking has become corrupted and must be deleted and recreated before any apply can proceed
- C) This is the expected behaviour of state locking — Engineer A's apply has acquired the lock, preventing concurrent state modification. Engineer B must wait until Engineer A's apply completes and the lock is released; no infrastructure is broken
- D) The error indicates the state file was corrupted by a previous failed apply and must be manually repaired using `terraform state push` before new applies can run

### Question 17 — S3 Bucket Rename in Code Review Triggers Destroy + Create

**Difficulty**: Medium
**Answer Type**: one
**Topic**: `terraform state mv` moves a resource's state entry to a new address, preventing destroy+recreate on rename

**Scenario**:
During a code review, a senior engineer renames an S3 bucket resource block from `aws_s3_bucket.data_lake_raw` to `aws_s3_bucket.raw` to comply with the team's new naming convention. After the PR is merged to the main branch, a teammate runs `terraform plan` and sees `Plan: 1 to add, 0 to change, 1 to destroy`. The bucket contains 10 terabytes of production data. Destroying and recreating the bucket would result in permanent data loss and a severe service outage. The team needs a way to apply the rename without any actual change to the cloud resource.

**Question**:
What is the correct action before running `terraform apply`?

- A) Add `lifecycle { prevent_destroy = true }` to the new resource block; this instructs Terraform to update the state address in place without performing a destroy
- B) Run `terraform state mv aws_s3_bucket.data_lake_raw aws_s3_bucket.raw` to update the state file's resource address mapping from the old label to the new label, without touching the actual S3 bucket
- C) Revert the rename in the code, apply, then re-introduce the rename in a second commit so Terraform processes it as an in-place name attribute change
- D) Run `terraform import aws_s3_bucket.raw <bucket-name>` to register the bucket under the new address, then run `terraform apply` to clean up the old address

### Question 18 — Permissive Version Constraint Allows Major Version Jump

**Difficulty**: Medium
**Answer Type**: one
**Topic**: `>=` has no upper bound; `~>` restricts updates to a specific major or minor series

**Scenario**:
A team inherited a Terraform codebase where the AWS provider is declared with `version = ">= 4.0"`. The existing team has been running AWS provider v5.31.0 smoothly for months. A new engineer joins the team, clones the repository to a fresh workstation, and runs `terraform init`. Unknown to the team, the Terraform Registry published AWS provider v6.0.0 the week before, which contains breaking changes to several resource argument names. The new engineer's `init` installs v6.0.0, and `terraform plan` immediately fails with multiple deprecation and argument errors. The rest of the team is unaffected because their `.terraform.lock.hcl` already pins them to v5.31.0.

**Question**:
What is the root cause of this problem, and what is the correct fix?

- A) The root cause is that the lock file on the rest of the team's machines is stale; every team member should run `terraform init -upgrade` to align on v6.0.0
- B) The root cause is that `>= 4.0` imposes no upper bound and allows installation of any version including v6.0.0; the team should change the constraint to `~> 5.0` (which allows `>= 5.0` and `< 6.0`) and commit the lock file so all team members pin to the same version
- C) The root cause is that the new engineer ran `terraform init -upgrade` without realising it; they should re-run `terraform init` without the `-upgrade` flag to downgrade to v5.31.0
- D) The root cause is that the team's lock file is outdated and should not be committed to version control; each engineer should generate their own lock file from scratch

### Question 19 — Colleague Suggests Restoring the Backup State After a Partial Apply Failure

**Difficulty**: Hard
**Answer Type**: many
**Topic**: `.tfstate.backup` is a single pre-apply snapshot; partial applies create resources unknown to the backup

**Scenario**:
An engineer runs `terraform apply` to create five new cloud resources: two subnets, two security groups, and one EC2 instance. The apply creates all four network resources successfully but fails with an API rate limit error while creating the EC2 instance. The current `terraform.tfstate` now reflects the four successfully created resources. A colleague suggests: "Just delete the current state file and restore `.terraform.tfstate.backup` — that gets you back to a clean slate." The engineer pauses before following this advice.

**Question**:
Which TWO statements explain why restoring the backup state file is the wrong approach?

- A) `.terraform.tfstate.backup` captures the state immediately before this apply ran — it has no record of the four resources that were successfully created. Restoring it causes Terraform to lose track of those resources, which could lead to orphaned cloud resources or duplicate creation on the next apply
- B) Restoring the backup is always safe and correct; the backup file contains a complete history of all resource states and is the intended recovery mechanism for failed applies
- C) With the backup restored, the next `terraform apply` would plan to create all five resources again; the four that already exist in the cloud would either cause API conflict errors or result in duplicate resources, depending on the resource type
- D) The `.terraform.tfstate.backup` file uses a different JSON schema version and cannot be used as the primary state file without running `terraform state push` first

### Question 20 — New Engineer Needs a Quick Resource Inventory

**Difficulty**: Easy
**Answer Type**: one
**Topic**: `terraform state list` outputs all resource addresses currently tracked in state

**Scenario**:
A new engineer joins an infrastructure team that manages a large environment through Terraform. On their first week, they want to get a quick overview of every cloud resource that Terraform is actively tracking in the current workspace, without having to read through hundreds of lines of `.tf` configuration files. They run a single Terraform CLI subcommand from the working directory. Their terminal prints a clean list:

```
aws_instance.web
aws_s3_bucket.logs
aws_db_instance.main
aws_security_group.app
module.vpc.aws_vpc.main
```

**Question**:
Which command produced this output?

- A) `terraform show`
- B) `terraform output`
- C) `terraform state list`
- D) `terraform state show`

### Question 21 — Migrating from Local to Remote S3 Backend in CI

**Difficulty**: Medium
**Answer Type**: one
**Topic**: `terraform init -migrate-state` performs backend state migration non-interactively

**Scenario**:
A solo developer has managed a Terraform project for three months using a local backend — the state lives in `terraform.tfstate` on their laptop. They now want to onboard two colleagues and move to a shared remote backend: S3 with DynamoDB state locking. They update the `backend "s3"` block in their configuration and run `terraform init`. Terraform detects the backend change and prints: `Do you want to copy existing state to the new backend? Enter "yes" to copy...`. For the migration to work in their CI pipeline without human input, they need the command to run non-interactively.

**Question**:
Which flag enables the state migration non-interactively?

- A) `terraform init -reconfigure`
- B) `terraform init -backend-config=backend.hcl`
- C) `terraform init -migrate-state`
- D) `terraform init -upgrade`

### Question 22 — Enterprise Team Evaluates a Partner-Tier Provider

**Difficulty**: Medium
**Answer Type**: many
**Topic**: Partner providers are maintained by technology partners with HashiCorp review; different from Official and Community tiers

**Scenario**:
An enterprise team is evaluating a Terraform provider for a Splunk Cloud integration. The Terraform Registry listing shows a "Partner" badge next to the provider name. The team's security policy requires that any provider used in production must be: (1) maintained by a trusted organization, not a random individual, and (2) carry some level of review or approval from HashiCorp. The team's security officer asks the team to confirm whether the Partner badge satisfies both criteria before approving the provider for production use.

**Question**:
Which TWO statements accurately describe Partner-tier providers on the Terraform Registry?

- A) Partner providers are built and maintained by technology companies that have a formal relationship with HashiCorp — they are not maintained by HashiCorp directly
- B) Partner providers are subject to the same internal code review process as Official providers because HashiCorp applies uniform standards across both tiers
- C) HashiCorp reviews and approves Partner providers before awarding the Partner badge, placing them above Community providers (unverified) in the trust hierarchy, though below Official providers (maintained by HashiCorp)
- D) Partner providers are self-published by individual open-source contributors on GitHub and carry no HashiCorp endorsement or verification

### Question 23 — Terraform CLI Upgrade Breaks a Shared Module

**Difficulty**: Medium
**Answer Type**: one
**Topic**: `~> 1.5.0` restricts to patch updates within the 1.5.x series; Terraform v1.8.0 is outside this range

**Scenario**:
A team upgrades their local Terraform CLI from v1.5.7 to v1.8.0 as part of a routine toolchain update. Most of their own configurations work correctly after the upgrade. However, when they try to initialize a reusable module stored in a shared internal registry, the `terraform init` fails with:

```
Error: Unsupported Terraform Core version
  This configuration does not support Terraform version 1.8.0.
  To proceed, either choose another supported Terraform version
  or update the constraint in the configuration:
  required_version = "~> 1.5.0"
```

**Question**:
Why does this module reject Terraform v1.8.0?

- A) `~> 1.5.0` requires exactly Terraform v1.5.0 and no other patch version
- B) `~> 1.5.0` allows only patch updates within the 1.5.x series: it permits `>= 1.5.0` and `< 1.6.0`. Terraform v1.8.0 falls outside this upper boundary and is therefore rejected
- C) `~> 1.5.0` sets a minimum of v1.5.0 with no upper limit, so v1.8.0 should be accepted — the error is caused by a binary mismatch unrelated to the version constraint
- D) `~> 1.5.0` is identical in behaviour to `~> 1.5`, which permits all v1.x releases including v1.8.0; the error is caused by a corrupted module cache

### Question 24 — Internal Provider Crashes Without Taking Down Terraform Core

**Difficulty**: Hard
**Answer Type**: one
**Topic**: Providers run as separate OS processes via gRPC; provider crash is isolated from Terraform Core

**Scenario**:
A platform team has developed a custom internal Terraform provider in Go that wraps their company's proprietary infrastructure orchestration API. During a large `terraform apply` involving 20 resources across three providers (AWS, Azure, and the internal custom provider), the internal provider binary panics due to an unhandled nil pointer dereference in its Go code for a specific resource type. An engineer observing the apply run notices that the Terraform Core process continues running, reports a provider-specific error for that single resource, and cleanly finishes processing all AWS and Azure resources. The internal provider crash does not abort the entire apply or affect the other providers.

**Question**:
Which architectural characteristic of the Terraform plugin model explains why the internal provider crash is isolated and does not terminate Terraform Core?

- A) Terraform Core executes all provider operations as goroutines; Go's runtime automatically recovers panics from goroutines and converts them into errors without affecting the main process
- B) Each Terraform provider plugin runs as a separate operating system process that communicates with Terraform Core over gRPC; the crash of one provider's process is isolated from Terraform Core and from all other provider processes
- C) Terraform Core maintains a watchdog subprocess for each provider; when a provider crashes, the watchdog automatically restarts the binary and retries the failed operation before reporting an error
- D) Terraform Core compiles provider operation wrappers into its own binary at `init` time; the provider binary is no longer needed at `apply` time and cannot cause Terraform Core to crash

### Question 25 — Handing Off an RDS Instance to Another Team Without Downtime

**Difficulty**: Medium
**Answer Type**: one
**Topic**: `terraform state rm` removes a resource from state management without deleting the cloud resource

**Scenario**:
A team has been managing a production PostgreSQL RDS instance in Terraform for two years using the resource address `aws_db_instance.postgres`. The company has reorganized and a dedicated database operations team will take ownership of this database going forward, managing it in their own separate Terraform workspace. The transition must not interrupt database service — the RDS instance must continue running with all its data, connections, and configuration intact while the handoff occurs. The database operations team will import it into their workspace afterwards.

**Question**:
What is the correct Terraform command for the current team to use, and what is its effect?

- A) Run `terraform destroy -target=aws_db_instance.postgres`; this removes the resource from state and deletes the RDS instance from AWS so the other team can provision a fresh replacement
- B) Run `terraform state rm aws_db_instance.postgres`; this removes the RDS instance from the current workspace's state file without making any API call to AWS — the database continues running unchanged
- C) Run `terraform state mv aws_db_instance.postgres ../db-team/aws_db_instance.postgres`; this automatically transfers the resource entry into the database team's local state file
- D) Delete the `aws_db_instance.postgres` resource block from the configuration and run `terraform apply`; Terraform will silently drop it from state without touching the cloud resource

### Question 26 — Second Provider Added to Existing Config

**Difficulty**: Easy
**Answer Type**: one
**Topic**: `terraform init` must be re-run when a new provider is added to `required_providers`

**Scenario**:
A team has been managing AWS infrastructure with Terraform for six months. Their configuration already declares the `hashicorp/aws` provider and their working directory has been initialized. A developer adds a `hashicorp/random` provider block to generate unique resource name suffixes. Without running any additional commands, they immediately run `terraform plan`. The terminal prints an error: `Provider "registry.terraform.io/hashicorp/random" was not found. Did you forget to run "terraform init"?`

**Question**:
What is the correct next action before `terraform plan` can succeed?

- A) Add the random provider to `.terraform/` manually by downloading the binary from the Terraform Registry website
- B) Run `terraform validate` first — this downloads missing providers as a side effect before performing syntax checks
- C) Run `terraform init` to download the newly declared `hashicorp/random` provider plugin and update the lock file
- D) Run `terraform apply -refresh-only` — this re-resolves provider dependencies without requiring a full init

### Question 27 — Production Deploy Pipeline Uses a Two-Stage Approach

**Difficulty**: Medium
**Answer Type**: one
**Topic**: `terraform plan -out` + `terraform apply <planfile>` guarantees deterministic apply of the reviewed plan

**Scenario**:
A financial services company has a strict change management process. All infrastructure changes to production must be reviewed and approved by a second engineer before being applied. The team's CI/CD pipeline is designed in two stages: Stage 1 runs during business hours and requires human approval; Stage 2 applies the change only after the Stage 1 approval ticket is signed. The infrastructure team wants to ensure that the exact changes reviewed and approved in Stage 1 are what get applied in Stage 2 — with no possibility of drift between review and apply.

**Question**:
Which approach correctly implements this two-stage guarantee?

- A) Run `terraform plan` in Stage 1; in Stage 2, run `terraform apply` — Terraform always re-runs the same plan from Stage 1 when no plan file is specified
- B) Run `terraform plan -out=prod.tfplan` in Stage 1 and store the plan file as a CI artifact; in Stage 2, run `terraform apply prod.tfplan` to apply exactly the reviewed plan
- C) Run `terraform validate` in Stage 1 to capture the intended changes; in Stage 2, run `terraform apply -auto-approve` to apply without prompting
- D) Pass a checksum of the configuration files from Stage 1 to Stage 2; Terraform verifies the checksum before applying to ensure no changes occurred

### Question 28 — Formatting Check Added to Pull Request Validation

**Difficulty**: Easy
**Answer Type**: one
**Topic**: `terraform fmt -check` exits with code 1 when files need reformatting — used in CI without writing files

**Scenario**:
A platform team wants to enforce consistent HCL formatting across all Terraform configurations in their monorepo. They add a new job to their pull request pipeline that validates formatting on every PR before allowing a merge. The job must fail the pipeline if any `.tf` file in any subdirectory is not in canonical Terraform format. Crucially, the CI environment is read-only — the job must not modify any source files. The team needs a single command to accomplish this.

**Question**:
Which command correctly implements the formatting check without modifying any files?

- A) `terraform fmt -recursive` — formats all files in subdirectories and exits with code 0, which fails the pipeline when changes are written
- B) `terraform fmt -check -recursive` — checks all `.tf` files recursively and exits with a non-zero code if any file needs reformatting, without writing any changes
- C) `terraform validate -recursive` — validates HCL syntax recursively across all subdirectories, including formatting style
- D) `terraform fmt -diff -recursive` — shows what would change and automatically fails the pipeline when diff output is non-empty

### Question 29 — Unhealthy EC2 Instance Needs a Clean Replacement

**Difficulty**: Medium
**Answer Type**: one
**Topic**: `terraform apply -replace` forces destroy+recreate of a specific resource without changing configuration

**Scenario**:
An operations engineer is troubleshooting a production EC2 instance that is exhibiting intermittent failures. The instance was correctly provisioned by Terraform and its configuration has not changed. The team suspects the instance has become corrupted at the OS level after an unexpected shutdown. The engineer wants to destroy the specific instance and provision a fresh one in its place, without touching any other resources in the Terraform-managed environment and without removing the resource block from the configuration.

**Question**:
Which command is the correct current approach for this situation?

- A) Remove the `aws_instance.app` resource block from the configuration temporarily, run `terraform apply`, then re-add the block and run `terraform apply` again
- B) Run `terraform destroy -target=aws_instance.app` followed by `terraform apply -target=aws_instance.app`
- C) Run `terraform apply -replace="aws_instance.app"` to force Terraform to destroy the existing instance and create a new one in a single apply operation
- D) Run `terraform taint aws_instance.app` — this is the current recommended command for forcing resource replacement

### Question 30 — Platform Team Visualizes a Dependency Graph for a New Hire

**Difficulty**: Medium
**Answer Type**: one
**Topic**: `terraform graph` outputs DOT format; Graphviz (`dot`) is required to render it as an image

**Scenario**:
A new infrastructure engineer joins a team managing a complex Terraform configuration with 30+ resources across VPCs, EC2 instances, RDS databases, security groups, and IAM roles. To help the new hire understand the dependency relationships between resources, the team lead wants to produce a visual diagram showing which resources depend on which. The team lead's workstation has Graphviz installed. They run a Terraform command and pipe its output to produce an SVG file.

**Question**:
Which command produces the rendered SVG dependency diagram?

- A) `terraform show -json | jq '.resources' > graph.svg`
- B) `terraform graph | dot -Tsvg > graph.svg`
- C) `terraform plan -out=graph.svg` — saves the execution plan as an SVG diagram when the file extension is `.svg`
- D) `terraform state list | dot -Tsvg > graph.svg`

### Question 31 — Script Assigns a Terraform Output to a Shell Variable

**Difficulty**: Easy
**Answer Type**: one
**Topic**: `terraform output -raw` produces unquoted string values suitable for shell variable assignment

**Scenario**:
A deployment script written in Bash needs to retrieve the public IP address of an EC2 instance that was provisioned by Terraform, then SSH into the instance to run a configuration command. The script runs `terraform output instance_ip` and captures the result with `IP=$(terraform output instance_ip)`. When the script attempts `ssh ubuntu@$IP`, the connection fails because the SSH command is receiving the value with surrounding double quotes: `"54.12.34.56"` instead of `54.12.34.56`.

**Question**:
What change to the `terraform output` command eliminates the surrounding quotes?

- A) Use `terraform output -json instance_ip | jq -r '.value'` to strip quotes from the JSON wrapper
- B) Use `terraform output -raw instance_ip` — the `-raw` flag outputs the value as a plain string without surrounding quotes, suitable for direct shell variable assignment
- C) Use `terraform show instance_ip` — the `show` command omits quotation marks from scalar output values
- D) Use `terraform output instance_ip | tr -d '"'` — pipe through `tr` to remove quotes as a post-processing step

### Question 32 — Large Environment Plan Takes 20 Minutes Due to API Throttling

**Difficulty**: Medium
**Answer Type**: many
**Topic**: `terraform plan -refresh=false` skips live API queries; trades freshness for speed in trusted environments

**Scenario**:
A team manages a Terraform workspace with over 600 cloud resources across AWS. Their standard `terraform plan` takes 20–25 minutes to complete because Terraform makes hundreds of individual AWS API calls to refresh the current state of every resource, and they are frequently hitting AWS API rate limits. The team's lead architect wants to speed up the planning cycle for routine code review without migrating to a different tool or architecture. The team's CI environment does not make any out-of-band changes — all infrastructure modifications go through Terraform.

**Question**:
Which TWO statements accurately describe the trade-off of using `terraform plan -refresh=false` in this scenario?

- A) `terraform plan -refresh=false` skips the live API refresh phase entirely, relying on the cached state in the state file — this significantly reduces API calls and plan duration
- B) `terraform plan -refresh=false` queries the API for resources that have changed since the last apply, but skips resources that are unchanged — it provides a partial refresh with improved performance
- C) Since the team's policy ensures no out-of-band infrastructure changes occur, the cached state in the state file is reliable, making `-refresh=false` a reasonable trade-off in this specific context
- D) `terraform plan -refresh=false` is inherently unsafe regardless of the environment because it disables all state consistency checks and may corrupt the state file

### Question 33 — Validate Passes, Plan Fails on First Deployment

**Difficulty**: Medium
**Answer Type**: one
**Topic**: `terraform validate` checks static config only; `terraform plan` catches live resource issues like invalid AMIs

**Scenario**:
A developer has written a new Terraform configuration to provision a set of EC2 instances using a specific AMI ID. They run `terraform validate` in their local environment and it exits successfully with `Success! The configuration is valid.` Confident the configuration is correct, they commit it and the team's CI pipeline runs `terraform plan` against the development AWS account. The plan fails with: `Error: ami-0deadbeef123 does not exist in region us-east-1`.

**Question**:
Why did `terraform validate` pass while `terraform plan` failed?

- A) `terraform validate` incorrectly ignored the `ami` argument because it is optional; `terraform plan` enforces required arguments with a stricter parser
- B) `terraform validate` performs only static analysis of the HCL syntax and references — it does not verify that referenced cloud resources (such as an AMI) actually exist. `terraform plan` contacts the AWS API during the refresh phase, which is when it discovers the AMI is invalid in that region
- C) The failure is caused by a missing provider version constraint; `terraform validate` does not enforce version constraints but `terraform plan` does
- D) `terraform validate` succeeded because the AMI ID was syntactically a valid string; `terraform plan` checks AMI IDs against a local cached list maintained in `.terraform/`

### Question 34 — Workspace Verification Before a Destructive Command

**Difficulty**: Medium
**Answer Type**: one
**Topic**: `terraform workspace show` displays the currently active workspace — critical safety check before destructive operations

**Scenario**:
A senior engineer is preparing to run `terraform destroy` to tear down a temporary load testing environment that was provisioned in the `loadtest` workspace. Their workflow involves switching between the `loadtest`, `staging`, and `production` workspaces multiple times per day. Before executing the destroy command, they want to verify with absolute certainty that the currently active workspace is `loadtest` and not `staging` or `production`. They need a single, concise command that outputs only the name of the currently active workspace.

**Question**:
Which command provides this information?

- A) `terraform workspace list` — lists all workspaces and marks the active one with an asterisk (`*`)
- B) `terraform workspace show` — outputs only the name of the currently active workspace as a plain string
- C) `terraform env` — the legacy command alias that outputs the active workspace name
- D) `terraform state list | head -1` — the first line of state list output always contains the workspace name

### Question 35 — Developer Tests a Conditional Expression Before Embedding It

**Difficulty**: Medium
**Answer Type**: one
**Topic**: `terraform console` lets developers interactively evaluate HCL expressions and functions before embedding them in configuration

**Scenario**:
A developer is writing a Terraform configuration that needs to conditionally set a resource tag based on whether a boolean variable `var.is_production` is `true`. They plan to use the ternary expression `var.is_production ? "prod" : "dev"` as the tag value. Before embedding this expression in the configuration, they want to test both branches interactively to confirm the syntax is correct and the output is exactly what they expect — without modifying any configuration files or running a full plan.

**Question**:
Which Terraform command provides this interactive testing capability?

- A) `terraform validate` — accepts expression syntax as an argument and evaluates it against the current variable values
- B) `terraform plan -var "is_production=true"` — this mode shows only the computed expression value without applying any changes
- C) `terraform console` — opens an interactive REPL where the developer can evaluate HCL expressions, test functions, and inspect variable values without modifying configuration or state
- D) `terraform output` — displays the result of arbitrary HCL expressions entered as arguments when run in debug mode

### Question 36 — CI Pipeline Must Pass Only Reviewed Changes to Production

**Difficulty**: Hard
**Answer Type**: one
**Topic**: Applying a saved plan file skips re-planning and interactive confirmation; changes between plan and apply cannot slip through

**Scenario**:
A DevSecOps team has implemented a two-stage production deployment pipeline. In Stage 1, `terraform plan -out=approved.tfplan` runs and the plan output is attached to a change request ticket for human review. A change advisory board reviews the plan, approves the ticket, and triggers Stage 2. In Stage 2, a pipeline job runs and must apply the exact, reviewed plan — no more, no fewer changes. A team member proposes replacing Stage 2's `terraform apply approved.tfplan` with `terraform apply -auto-approve` to simplify the pipeline, arguing both approaches skip the interactive prompt.

**Question**:
Why is the team member's proposed simplification incorrect and potentially dangerous?

- A) `-auto-approve` is not permitted in CI environments and will always cause an exit code 1 failure when run outside of an interactive terminal
- B) `terraform apply -auto-approve` runs a fresh plan at apply time, meaning any infrastructure changes that occurred between Stage 1 and Stage 2 (such as manual console changes or concurrent pipeline runs) would be included in the apply — producing different changes from what the change advisory board reviewed and approved
- C) `terraform apply approved.tfplan` and `terraform apply -auto-approve` are functionally identical when the configuration has not changed between the two stages, so the simplification is safe
- D) `-auto-approve` requires the `-input=false` flag to be specified alongside it in CI environments; omitting `-input=false` will cause Stage 2 to pause waiting for user input

### Question 37 — Emergency Fix Targets One Resource in a Shared Workspace

**Difficulty**: Hard
**Answer Type**: many
**Topic**: `terraform apply -target` applies only to the specified resource; known risks include partial state and dependency gaps

**Scenario**:
During a production incident, a load balancer security group rule allowing port 443 was accidentally removed via the AWS console by another team, causing a service outage. The Terraform configuration still contains the correct rule. The on-call engineer wants to immediately restore only the security group rule using Terraform without potentially modifying the 80 other resources in the same workspace, since many of those resources are actively serving traffic. The engineer runs `terraform apply -target=aws_security_group_rule.allow_https`. The rule is restored and the outage is resolved. The team lead later reviews the incident and raises a concern about the long-term use of `-target`.

**Question**:
Which TWO concerns correctly describe the risks of using `-target` regularly (not just in this emergency)?

- A) Regular use of `-target` can lead to a configuration drift where the Terraform state does not accurately reflect the full desired state — resources that depend on the targeted resource may be in a different state than the configuration specifies, creating inconsistencies that accumulate over time
- B) `-target` is not a supported flag on `terraform apply` — it is only valid with `terraform plan`; using it with `apply` will silently apply all resources instead
- C) After a `-target` apply, the remainder of the configuration has not been fully evaluated — running a full `terraform plan` afterwards may reveal planned changes to resources that were not included in the targeted apply, because their dependencies changed
- D) `-target` causes Terraform to permanently lock the targeted resource's state entry, preventing future full applies from modifying it unless the lock is manually removed with `terraform state rm`

### Question 38 — Engineer Mistakes `terraform plan -destroy` for `terraform destroy`

**Difficulty**: Hard
**Answer Type**: one
**Topic**: `terraform plan -destroy` is a read-only preview; `terraform destroy` actually destroys resources

**Scenario**:
A junior engineer is tasked with reviewing what would be deleted if the staging environment were torn down. Their team lead tells them: "Use `terraform plan -destroy` to see what would be removed." The junior engineer misremembers the instruction and instead runs `terraform destroy` in the staging workspace. Within seconds, Terraform begins destroying resources. The engineer panics and presses Ctrl+C to interrupt the process. Five resources are destroyed before the interrupt takes effect. The team lead later reviews the incident to explain the difference between the two commands.

**Question**:
Which statement most accurately describes the distinction between `terraform plan -destroy` and `terraform destroy`?

- A) `terraform plan -destroy` and `terraform destroy` are aliases for the same operation; both always prompt for interactive confirmation before making any changes, so the engineer should have seen a prompt and cancelled before any resources were destroyed
- B) `terraform plan -destroy` generates a read-only preview showing what `terraform destroy` would remove, without making any API calls or changes to infrastructure. `terraform destroy` actually executes the destruction — it prompts for confirmation by default, but once "yes" is entered (or `-auto-approve` is used), it immediately begins deleting resources
- C) `terraform plan -destroy` also destroys resources, but it destroys them in reverse dependency order to avoid errors; `terraform destroy` uses alphabetical order and is therefore more likely to produce errors
- D) `terraform plan -destroy` is only valid when used with a `-out` flag to save the destroy plan; running it without `-out` is equivalent to `terraform destroy`

### Question 39 — Zero-Downtime RDS Replacement Required

**Difficulty**: Medium
**Answer Type**: one
**Topic**: `create_before_destroy = true` reverses replacement order to avoid downtime when a resource must be replaced

**Scenario**:
A team is updating a production RDS instance parameter group. The parameter group argument is immutable, so changing it forces a replacement: Terraform's plan shows `-/+`. By default, Terraform will destroy the old RDS instance first and then create the new one. Even a few seconds of downtime is unacceptable because the database serves a real-time payment processing service. The team wants Terraform to provision the replacement RDS instance, confirm it is healthy, and only then remove the old one.

**Question**:
Which lifecycle configuration correctly implements this zero-downtime replacement order?

- A) Add `prevent_destroy = true` to the `lifecycle` block — this forces Terraform to create the new instance before it is permitted to schedule the destroy
- B) Add `create_before_destroy = true` to the `lifecycle` block — this instructs Terraform to provision the replacement resource first and only destroy the original after the new one exists
- C) Add `replace_triggered_by = [aws_db_parameter_group.new]` to the `lifecycle` block — this triggers the replacement in a create-first order automatically
- D) Add `ignore_changes = [parameter_group_name]` — this prevents the replacement from occurring and allows the parameter group change to be applied in-place

### Question 40 — Auto Scaling Group Keeps Reverting to Minimum Capacity

**Difficulty**: Medium
**Answer Type**: one
**Topic**: `ignore_changes` suppresses drift detection for specified attributes managed outside Terraform

**Scenario**:
An operations team uses Terraform to manage an AWS Auto Scaling Group (ASG) with `min_size = 2`. During production incidents, the on-call engineer manually scales the ASG up via the AWS console — setting `min_size = 10` to handle a traffic surge. When the incident is resolved and the next scheduled `terraform apply` runs, Terraform detects the drift and reverts `min_size` back to `2`, which causes the group to scale in aggressively. The team wants Terraform to stop overwriting `min_size` on every apply while still managing all other ASG attributes.

**Question**:
Which configuration change correctly prevents Terraform from reverting `min_size`?

- A) Remove the `min_size` argument from the resource block entirely — Terraform will use the AWS default and stop detecting changes to that attribute
- B) Add a `lifecycle` block with `ignore_changes = [min_size]` to the ASG resource — Terraform will no longer detect or revert drift on that specific attribute
- C) Add `depends_on = [aws_cloudwatch_metric_alarm.traffic]` — this tells Terraform to defer changes to the ASG until the alarm fires, preventing premature reverts
- D) Set `create_before_destroy = true` — this pauses the apply until manual changes are confirmed, avoiding the revert

### Question 41 — `for_each` Fails with a `list(string)` Variable

**Difficulty**: Easy
**Answer Type**: one
**Topic**: `for_each` requires a `map` or `set(string)`; a `list(string)` must be converted with `toset()`

**Scenario**:
A developer wants to create one AWS IAM user for each username in a list. They write:

```hcl
variable "usernames" {
  type    = list(string)
  default = ["alice", "bob", "carol"]
}

resource "aws_iam_user" "team" {
  for_each = var.usernames
  name     = each.key
}
```

Running `terraform plan` immediately fails with: `The given "for_each" argument value is unsuitable: the "for_each" meta-argument must be a map, or a set of strings, and you have provided a value of type list of string.`

**Question**:
What is the minimal fix to the `for_each` argument that resolves the error?

- A) Change `for_each = var.usernames` to `for_each = count(var.usernames)` — the `count()` function converts a list to the correct type
- B) Change the `for_each` meta-argument to `count = length(var.usernames)` and reference users by `count.index`
- C) Change `for_each = var.usernames` to `for_each = toset(var.usernames)` — the `toset()` function converts the list to a `set(string)`, which `for_each` accepts
- D) Change the variable type from `list(string)` to `tuple` — tuples are accepted directly by `for_each`

### Question 42 — Legacy S3 Bucket Must Be Removed from Terraform Without Deletion

**Difficulty**: Medium
**Answer Type**: one
**Topic**: `removed` block with `lifecycle { destroy = false }` stops Terraform managing a resource without deleting it

**Scenario**:
An organisation has a legacy S3 bucket that was provisioned by Terraform three years ago and contains compliance archives that must be retained permanently. The infrastructure team decides to remove the bucket from Terraform management entirely — it will no longer be tracked or modified by Terraform — but under no circumstances should the bucket or its contents be deleted. A junior engineer suggests deleting the `aws_s3_bucket.compliance_archive` resource block from the configuration and running `terraform apply`. The team lead rejects this approach.

**Question**:
Why does the team lead reject the proposed approach, and what is the correct alternative?

- A) The team lead rejects it because deleting a resource block and running `terraform apply` causes Terraform to destroy the corresponding cloud resource. The correct alternative is to add a `removed` block with `lifecycle { destroy = false }` to explicitly stop tracking the resource without issuing a delete API call
- B) The team lead rejects it because Terraform requires a two-step process: first run `terraform state rm` to remove it from state, then delete the resource block. Running `terraform apply` with only the block deleted would cause a validation error
- C) The team lead rejects it because deleting a resource block does nothing — Terraform continues to manage resources whose blocks are removed, reading their state from the state file
- D) The team lead rejects it because `terraform apply` requires the `-confirm-orphan` flag when resource blocks are deliberately removed to prevent accidental deletions

### Question 43 — Module Refactoring Moves Resources from Root to Child Module

**Difficulty**: Medium
**Answer Type**: one
**Topic**: `moved` block with `to = module.<name>.<type>.<name>` relocates a resource's state entry to a module address

**Scenario**:
A team has been managing several networking resources at the root module level for months: `aws_vpc.main`, `aws_subnet.public`, and `aws_internet_gateway.main`. The team is refactoring the configuration to introduce a reusable `networking` module. After creating the module and moving the resource blocks into `modules/networking/`, they update the root configuration to call the module. Running `terraform plan` shows three destroys and three creates — Terraform treats the new module-path addresses as entirely new resources and the old root-level addresses as orphans to be destroyed.

**Question**:
What must the team add to prevent the destroy+create cycle for each resource being moved into the module?

- A) Add `lifecycle { prevent_destroy = true }` to each resource block inside the module — this prevents Terraform from scheduling the root-level resources for deletion
- B) Add a `moved` block for each resource in the root configuration, mapping from the old root address to the new module address, e.g., `from = aws_vpc.main` / `to = module.networking.aws_vpc.main`
- C) Export the existing resource IDs as outputs from the root module and pass them as inputs to the child module, then run `terraform apply` with `-target=module.networking`
- D) Run `terraform state mv aws_vpc.main module.networking.aws_vpc.main` for each resource before applying — `moved` blocks are only for renaming within the same module level

### Question 44 — EC2 Instance Fails on Startup Because IAM Policy Isn't Ready

**Difficulty**: Medium
**Answer Type**: one
**Topic**: `depends_on` required for IAM policy attachments because no attribute reference exists between the IAM resource and the consuming resource

**Scenario**:
A team provisions an EC2 instance with an IAM instance profile that grants S3 read access. The Terraform configuration creates the IAM role, attaches the policy, creates the instance profile, and associates it with the EC2 instance. Terraform successfully applies all resources, but the application running on the EC2 instance intermittently fails to read from S3 at startup because the IAM policy has not fully propagated by the time the instance boots. The team adds a `depends_on` reference to the EC2 instance pointing to the IAM role policy attachment. The intermittent failures stop.

**Question**:
Why was `depends_on` necessary here when Terraform already references `aws_iam_instance_profile.app` in the EC2 resource block?

- A) `depends_on` is always required between IAM resources and compute resources — Terraform never infers IAM dependencies automatically regardless of attribute references
- B) Terraform detected the `aws_iam_instance_profile.app` attribute reference and created a dependency edge between the instance profile and the EC2 instance. However, the `aws_iam_role_policy.s3_read` attachment has no attribute referenced in the EC2 block — Terraform cannot detect that dependency through attributes alone. `depends_on` explicitly adds the missing edge so Terraform waits for the policy attachment before creating the instance
- C) `depends_on` prevents Terraform from parallelising the apply, which gives IAM time to propagate before the instance starts — it works purely as a timing delay mechanism and has nothing to do with the dependency graph
- D) The IAM policy attachment creates a dependency cycle with the instance profile, which Terraform normally skips. `depends_on` overrides cycle detection to allow the attachment to be applied first

### Question 45 — Data Source Returns a Value That Won't Be Known Until Apply

**Difficulty**: Hard
**Answer Type**: one
**Topic**: Data sources whose arguments contain computed (unknown-until-apply) values are deferred and read during `apply`, not `plan`

**Scenario**:
A team is writing a configuration that creates a new VPC and then immediately uses a data source to look up the route tables associated with that VPC in order to configure VPN gateway attachments. The data source's `filter` block references `aws_vpc.main.id`. When the team runs `terraform plan`, the data source section shows `(known after apply)` for its result. The team is surprised — they expected the data source to resolve during the plan phase so they could see the full plan output.

**Question**:
Why does the data source show `(known after apply)` during plan?

- A) Data sources are always deferred to the apply phase; they never resolve during `terraform plan` regardless of whether their arguments are known or unknown
- B) The VPC's `id` attribute is assigned by AWS only after the resource is created. Since `aws_vpc.main.id` is not known at plan time (the VPC does not yet exist), Terraform cannot evaluate the data source's filter during plan — the data source is deferred to the apply phase when the VPC's ID becomes available
- C) The `(known after apply)` marker means the data source has no matching results and will create the resource instead of querying existing ones during apply
- D) Data sources referenced from the same Terraform configuration as their filter dependency always fail with errors; they must be placed in a separate Terraform workspace

### Question 46 — Launch Template Update Does Not Refresh Running Instances

**Difficulty**: Medium
**Answer Type**: one
**Topic**: `replace_triggered_by` forces the dependent resource to be replaced when a referenced upstream resource changes

**Scenario**:
A team manages an Auto Scaling Group (ASG) and an associated Launch Template in Terraform. The launch template specifies the AMI, instance type, and user data script. When the team updates the launch template to use a new hardened AMI, `terraform apply` succeeds and creates a new launch template version. However, the ASG continues running instances based on the old launch template version — Terraform does not replace the ASG because none of the ASG's own configuration attributes changed. The team needs existing ASG instances to be replaced when the launch template changes.

**Question**:
Which lifecycle configuration on the ASG resource causes Terraform to replace the ASG whenever the launch template changes?

- A) Add `depends_on = [aws_launch_template.web]` to the ASG resource — this ensures Terraform always applies the launch template before the ASG, propagating template changes automatically to running instances
- B) Add `ignore_changes = [aws_launch_template.web]` to the ASG's `lifecycle` block — this prevents the ASG from being replaced when the launch template changes unexpectedly
- C) Add `replace_triggered_by = [aws_launch_template.web]` in the ASG resource's `lifecycle` block — this instructs Terraform to replace the ASG whenever the launch template resource changes, even if none of the ASG's own attributes changed
- D) Add `create_before_destroy = true` to the launch template's `lifecycle` block — creating the new template version first automatically triggers instance refresh in the ASG

### Question 47 — Nightly Teardown Pipeline Blocked by `prevent_destroy`

**Difficulty**: Medium
**Answer Type**: many
**Topic**: `prevent_destroy = true` causes `terraform apply` and `terraform destroy` to error; must be removed from config before destroying

**Scenario**:
A team runs an automated nightly pipeline that destroys a temporary integration testing environment to save costs, using `terraform destroy -auto-approve`. Last week, a developer added `lifecycle { prevent_destroy = true }` to a test database resource to avoid accidental deletion during development. The nightly destroy pipeline now fails every night with: `Error: Instance cannot be destroyed. Resource aws_db_instance.test has lifecycle.prevent_destroy set to true`. The developer is on vacation and is unavailable to review. The pipeline owner needs to understand the options.

**Question**:
Which TWO statements accurately describe the situation and the available remediation?

- A) `prevent_destroy = true` causes Terraform to error on any plan that includes a destroy operation for that resource — whether from `terraform destroy` or from a configuration-driven replacement. It does not prevent `terraform state rm` from removing the resource's state entry without destroying the cloud resource
- B) `prevent_destroy = true` is enforced at the cloud provider API level — the protection cannot be bypassed even if removed from the Terraform configuration, requiring a support ticket to AWS to unlock
- C) To allow the nightly destroy to succeed, the `prevent_destroy = true` setting must be removed from the resource block's `lifecycle` configuration, and `terraform init` must be re-run to update the provider schema before the destroy can proceed
- D) To allow the nightly destroy to succeed, `prevent_destroy = true` must be removed from the resource block's `lifecycle` configuration and the configuration re-applied or the destroy re-run — `prevent_destroy` is a Terraform-only guard evaluated at plan time; once removed from the config, the destroy plan will no longer error

### Question 48 — Middle Username Removed from `count`-Based IAM Users Causes Unexpected Replacements

**Difficulty**: Hard
**Answer Type**: one
**Topic**: Removing an element from the middle of a `count`-indexed list causes all subsequent instances to shift indices and be replaced

**Scenario**:
A team manages five IAM users using `count` and a `list(string)` variable:

```hcl
variable "usernames" {
  default = ["alice", "bob", "carol", "dave", "eve"]
}

resource "aws_iam_user" "team" {
  count = length(var.usernames)
  name  = var.usernames[count.index]
}
```

When `bob` leaves the company, the team removes `"bob"` from the list, leaving `["alice", "carol", "dave", "eve"]`. They expect Terraform to plan a single deletion of `aws_iam_user.team[1]`. Instead, `terraform plan` shows one deletion and three replacements. The team is confused.

**Question**:
What causes the three unexpected replacements?

- A) The `aws_iam_user` resource type does not support `count` — using it with `for_each` instead would have prevented the replacements entirely
- B) Removing `"bob"` at index 1 causes all subsequent list elements to shift down by one index: `carol` moves from index 2 to 1, `dave` from 3 to 2, and `eve` from 4 to 3. Terraform sees `team[1]` through `team[3]` as having new `name` values and plans to replace them. Only `team[4]` (the former `eve` at the last index) is deleted
- C) Terraform detects that the list length decreased and plans to delete all existing `count` instances before creating the new set, resulting in five deletes and four creates
- D) The `count.index` is not recalculated after an element is removed — Terraform reuses the old indices, causing the last element `eve` to have an orphaned index that triggers a cascade replacement

### Question 49 — Terraform Detects a Circular Dependency and Errors

**Difficulty**: Hard
**Answer Type**: one
**Topic**: Circular dependencies (cycles) in the resource graph cause Terraform to error; resolution requires restructuring references or using `data` sources

**Scenario**:
A developer writes a Terraform configuration where `aws_security_group.app` references `aws_security_group.db.id` (the app security group allows outbound traffic to the DB security group), and `aws_security_group.db` references `aws_security_group.app.id` (the DB security group allows inbound traffic from the app security group). Running `terraform plan` fails immediately with: `Error: Cycle: aws_security_group.app, aws_security_group.db`. The developer is unsure how to model this bidirectional security group relationship.

**Question**:
Which approach correctly resolves the circular dependency while preserving the intended security group rules?

- A) Add `depends_on = [aws_security_group.db]` to `aws_security_group.app` and `depends_on = [aws_security_group.app]` to `aws_security_group.db` — explicit `depends_on` overrides cycle detection and establishes a valid ordering
- B) Create both security groups without referencing each other (no ingress/egress rules in the group blocks themselves), then define the ingress and egress rules as separate `aws_security_group_rule` resources that reference each security group's `id` — this breaks the cycle by removing the circular attribute references from the group blocks
- C) Merge both security groups into a single `aws_security_group` resource — Terraform can handle self-referential rules within a single resource block without cycle errors
- D) Use `ignore_changes = [ingress, egress]` on both security group resources — this tells Terraform to ignore the circular references during planning

### Question 50 — Data Source Looks Up a Resource Created in the Same Apply

**Difficulty**: Hard
**Answer Type**: many
**Topic**: Data sources depending on newly created resources are deferred to apply phase; plan output shows `(known after apply)` for data source results

**Scenario**:
A team is writing a configuration that creates a new AWS KMS key and then immediately uses a data source (`data "aws_kms_alias"`) to look up the alias ARN of that same key, which they need to pass to an S3 bucket encryption configuration. During `terraform plan`, the S3 bucket's `kms_master_key_id` argument shows `(known after apply)` and the data source itself shows `(known after apply)` for all its outputs. The team is trying to understand why the plan is not fully resolvable.

**Question**:
Which TWO statements accurately explain the behaviour?

- A) The KMS key's alias ARN is assigned by AWS only after the key is created. Since the key does not exist yet at plan time, the data source's query cannot be executed — it is deferred to the apply phase when the key exists and the alias ARN is retrievable
- B) Data sources that reference newly created resource attributes always produce errors during plan — the only solution is to use `terraform apply` with `-refresh-only` before a standard apply
- C) The `(known after apply)` value propagates downstream: because the data source result is unknown at plan time, any resource arguments that reference the data source result are also shown as `(known after apply)` in the plan output
- D) Terraform resolves all data sources at plan time regardless of their dependencies; the `(known after apply)` marker means the S3 bucket is misconfigured and will fail during apply

### Question 51 — New Resource Must Be Deployed into a Specific AWS Region

**Difficulty**: Easy
**Answer Type**: one
**Topic**: The `provider` meta-argument on a resource selects an aliased provider configuration for that specific resource

**Scenario**:
A team manages infrastructure in `us-east-1` as their primary region. Their Terraform configuration declares a default AWS provider for `us-east-1` and an aliased provider for `eu-west-1`:

```hcl
provider "aws" {
  region = "us-east-1"
}

provider "aws" {
  alias  = "ireland"
  region = "eu-west-1"
}
```

The team needs to create a new S3 bucket specifically in `eu-west-1` for GDPR data residency compliance. All other resources in the configuration should remain in `us-east-1`.

**Question**:
What must the S3 bucket resource block include to deploy into `eu-west-1`?

- A) Set `region = "eu-west-1"` as a top-level argument inside the `aws_s3_bucket` resource block
- B) Include `provider = aws.ireland` as a meta-argument in the `aws_s3_bucket` resource block, referencing the aliased provider configuration for `eu-west-1`
- C) Create a new `terraform workspace` named `ireland` — workspaces automatically route resources to the region matching the workspace name
- D) Include `alias = "ireland"` as a meta-argument in the `aws_s3_bucket` resource block to select the aliased provider

### Question 52 — Validation Block Tries to Reference a Data Source

**Difficulty**: Medium
**Answer Type**: one
**Topic**: `variable` validation `condition` can only reference `var.<name>` — referencing data sources, locals, or other resources causes an error at parse time

**Scenario**:
A platform team wants to restrict deployments to AWS regions where their organisation has approved accounts. They write the following variable block:

```hcl
variable "region" {
  type = string

  validation {
    condition     = contains(data.aws_regions.available.names, var.region)
    error_message = "Region must be one of the approved AWS regions."
  }
}
```

Running `terraform plan` immediately fails before any API calls are made. The team is confused because `data.aws_regions.available` is defined elsewhere in the configuration and works fine outside the validation block.

**Question**:
Why does Terraform reject this validation block?

- A) The `contains()` function is not permitted inside `validation` blocks — only string comparison operators are allowed in `condition` expressions
- B) Validation `condition` expressions can only reference `var.<name>` for the variable being validated. References to data sources, locals, or other resources are not permitted — the validation is evaluated before any infrastructure queries can run
- C) The data source `data.aws_regions.available` must be declared inside the `variable` block for the reference to resolve correctly within the validation scope
- D) Validation blocks do not support multi-argument functions like `contains()` — each condition must be a single boolean expression using comparison operators

### Question 53 — Sensitive Output: What It Protects and What It Does Not

**Difficulty**: Medium
**Answer Type**: many
**Topic**: `sensitive = true` on an output masks the value in CLI output but the value remains in plaintext in `terraform.tfstate` — protecting state requires an encrypted remote backend

**Scenario**:
A security review flags that an RDS master password is exposed in Terraform's terminal output during deploys. The team adds `sensitive = true` to the output block:

```hcl
output "db_password" {
  value     = aws_db_instance.main.password
  sensitive = true
}
```

After applying, the team's security officer asks two specific questions: (1) Does this prevent the password from appearing in the terminal during `terraform apply`? (2) Does this encrypt the value in the state file?

**Question**:
Which TWO statements accurately describe what `sensitive = true` on an output block does and does not do?

- A) `sensitive = true` causes the value to appear as `(sensitive value)` in `terraform apply` and `terraform output` CLI output — it does not encrypt or redact the value in `terraform.tfstate`, where it is still stored in plaintext
- B) `sensitive = true` encrypts the output value in `terraform.tfstate` using AES-256, making the state file safe to store in an unencrypted S3 bucket
- C) `sensitive = true` prevents anyone with `terraform output` access from ever retrieving the actual value — the value can only be recovered by re-running `terraform apply`
- D) Even with `sensitive = true`, the actual plaintext value remains accessible in the state file — protecting it from unauthorized access requires storing state in an encrypted remote backend (such as S3 with server-side encryption or HCP Terraform)

### Question 54 — CI Pipeline: Which Variable Source Wins?

**Difficulty**: Easy
**Answer Type**: one
**Topic**: CLI `-var` flag takes the highest precedence over all other variable input sources, including `*.auto.tfvars` files

**Scenario**:
A CI/CD pipeline for a multi-environment deployment manages Terraform configuration for both staging and production. The repository contains a `prod.auto.tfvars` file (automatically loaded by Terraform) with `region = "us-east-1"`. A DevOps engineer adds a pipeline override step that passes `-var "region=eu-west-1"` on the `terraform apply` command. Both the auto-loaded file and the CLI flag specify the `region` variable.

**Question**:
Which value does Terraform use for `var.region` during this apply?

- A) `"us-east-1"` — `*.auto.tfvars` files take precedence over CLI flags because they are committed to the repository and represent the declarative source of truth
- B) `"eu-west-1"` — the CLI `-var` flag has the highest precedence of all variable input sources; it overrides `*.auto.tfvars`, `terraform.tfvars`, `-var-file` flags, and environment variables
- C) Terraform errors because the same variable is specified in two sources simultaneously — duplicate variable assignments are not permitted
- D) `"us-east-1"` — `*.auto.tfvars` is processed last in the input chain and therefore takes final precedence

### Question 55 — Inline IAM Policy Using `jsonencode()`

**Difficulty**: Medium
**Answer Type**: one
**Topic**: `jsonencode()` converts a Terraform HCL object/map/list to its JSON string representation — commonly used for inline IAM policies and ECS task definitions to avoid a separate `aws_iam_policy_document` data source

**Scenario**:
A team is writing a Terraform configuration that attaches an inline policy to an IAM role. A colleague suggests using a separate `data "aws_iam_policy_document"` block, but the team lead prefers to use `jsonencode()` directly in the resource block to keep everything in a single file. The team lead writes:

```hcl
resource "aws_iam_role_policy" "s3_read" {
  name = "s3-read"
  role = aws_iam_role.lambda.id

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Effect   = "Allow"
      Action   = ["s3:GetObject"]
      Resource = "*"
    }]
  })
}
```

A new team member asks what type of value `jsonencode()` returns and whether the `policy` argument accepts it.

**Question**:
What does `jsonencode()` return, and why is it valid for the `policy` argument?

- A) `jsonencode()` returns an HCL object — the `policy` argument accepts HCL objects natively, so no conversion is needed
- B) `jsonencode()` returns a JSON string — the `policy` argument on `aws_iam_role_policy` expects a JSON-encoded string, making `jsonencode()` the idiomatic way to define inline policies in HCL without a separate data source
- C) `jsonencode()` returns a Terraform map type — it is equivalent to writing `var.policy_map` and is only useful for outputs, not resource arguments
- D) `jsonencode()` returns a Base64-encoded string — this is required because the AWS provider internally base64-encodes IAM policy documents before sending them to the API

### Question 56 — Custom Iterator Name in `dynamic` Block Changes Reference Syntax

**Difficulty**: Medium
**Answer Type**: one
**Topic**: When `iterator = <name>` is set in a `dynamic` block, the `content` block must use `<name>.value.*` instead of the default block-type name

**Scenario**:
A team inherits a Terraform configuration that uses a `dynamic "ingress"` block to generate security group rules from a list variable. The original code references `ingress.value.from_port` inside the `content` block. A team member refactors the block by adding `iterator = rule` to make the code more readable:

```hcl
dynamic "ingress" {
  for_each = var.ingress_rules
  iterator = rule

  content {
    from_port   = ingress.value.from_port   # ← still using original name
    to_port     = ingress.value.to_port
    protocol    = ingress.value.protocol
    cidr_blocks = ["0.0.0.0/0"]
  }
}
```

Running `terraform validate` fails. The team member is puzzled because `ingress.value` worked before the `iterator` was added.

**Question**:
What is the cause of the validation failure, and what is the correct fix?

- A) `iterator` is not a valid argument in `dynamic` blocks — it should be removed and the original `ingress.value.*` references restored
- B) Adding `iterator = rule` changes the name of the loop variable inside the `content` block from `ingress` to `rule`. The content references must be updated from `ingress.value.*` to `rule.value.*` — using the old name after setting a custom iterator is invalid
- C) The `iterator` argument requires the same name as the block type — `iterator = ingress` is the only valid assignment, making `iterator = rule` always invalid
- D) The `for_each` in a `dynamic` block must be a set, not a list — the failure is caused by `var.ingress_rules` being a `list(object(...))` rather than a `set(object(...))`

### Question 57 — Using `locals` with `merge()` to Centralise Resource Tags

**Difficulty**: Easy
**Answer Type**: one
**Topic**: `local.*` values are internal computed values that centralise reusable expressions within a module — they are not module interface inputs and cannot be overridden by callers

**Scenario**:
A team manages 25 AWS resources in a Terraform module and needs every resource to carry a consistent set of tags including `Environment`, `Team`, and `ManagedBy`. Rather than duplicating the tag map in each resource block, a senior engineer proposes the following approach:

```hcl
locals {
  base_tags = {
    ManagedBy   = "terraform"
    Team        = "platform"
  }

  common_tags = merge(local.base_tags, {
    Environment = var.environment
  })
}
```

Each resource then uses `tags = local.common_tags`. A junior developer asks: "Why use `locals` instead of just adding a `variable` block for `common_tags` so callers can override the whole tag map?"

**Question**:
Which answer best explains why `locals` is the appropriate choice here?

- A) `locals` blocks are evaluated at plan time, while `variable` blocks are only evaluated at apply time — using `locals` makes the tags available earlier in the Terraform execution lifecycle
- B) Locals are internal computed values scoped to the module — they cannot be set by callers, which is correct here because the tag map should be automatically derived from other inputs, not overridden arbitrarily. A `variable` block would expose `common_tags` as part of the module interface, allowing callers to pass in conflicting or incomplete tag maps
- C) Locals must be used instead of variables whenever a `merge()` call is involved — Terraform does not support `merge()` inside variable `default` values
- D) Using a `variable` block for the tag map would cause Terraform to treat each tag as a sensitive value and suppress it in terminal output

### Question 58 — `for` Expression with `[...]` Extracts Map Values as a List

**Difficulty**: Medium
**Answer Type**: one
**Topic**: A `for` expression enclosed in `[...]` produces a `list`; enclosing in `{...}` with `key => value` syntax produces a `map` — the outer delimiters determine the output type

**Scenario**:
A team has a Terraform variable that maps server names to instance types:

```hcl
variable "servers" {
  type = map(string)
  default = {
    web = "t3.micro"
    app = "t3.small"
    db  = "t3.medium"
  }
}
```

A developer writes the following local to extract just the instance types for passing to a monitoring module that expects a `list(string)`:

```hcl
locals {
  instance_types = [for k, v in var.servers : v]
}
```

The developer is unsure whether this produces a list or a map.

**Question**:
What type and content does `local.instance_types` hold?

- A) A `map(string)` — the `for` expression iterates over a map, so the result is always a map regardless of the outer delimiters used
- B) A `list(string)` containing the instance type values (e.g., `["t3.micro", "t3.small", "t3.medium"]`) — wrapping a `for` expression in `[...]` always produces a list; the key variable `k` is iterated but not included because the expression only emits `v`
- C) A `set(string)` — Terraform automatically deduplicates the results when a `for` expression iterates over a map's values
- D) An error — iterating a map with two loop variables (`k, v`) is only valid when producing a map output; a list `for` expression must use a single variable

### Question 59 — `cidrsubnet` for Three Availability Zone Subnets

**Difficulty**: Hard
**Answer Type**: one
**Topic**: `cidrsubnet(prefix, newbits, netnum)` — `newbits` is additional bits borrowed from the host portion to extend prefix length; `netnum` is zero-based subnet index; `cidrsubnet("10.0.0.0/16", 8, N)` produces a `/24` subnet

**Scenario**:
A network engineer needs to create three subnets — one per availability zone — from a `10.0.0.0/16` VPC CIDR. They want each subnet to be a `/24`. They use `count` and `cidrsubnet()`:

```hcl
resource "aws_subnet" "az" {
  count             = 3
  vpc_id            = aws_vpc.main.id
  cidr_block        = cidrsubnet("10.0.0.0/16", 8, count.index)
  availability_zone = var.availability_zones[count.index]
}
```

A colleague asks: "For `count.index` values of 0, 1, and 2, what CIDRs does this produce?"

**Question**:
Which option correctly lists the three subnet CIDRs produced by `cidrsubnet("10.0.0.0/16", 8, count.index)` for `count.index` = 0, 1, and 2?

- A) `10.0.0.0/16`, `10.0.1.0/16`, `10.0.2.0/16` — `newbits = 8` extends the prefix by 8, but the `/16` base is preserved in the output
- B) `10.0.0.0/8`, `10.0.1.0/8`, `10.0.2.0/8` — `cidrsubnet` with `newbits = 8` subtracts 8 bits from the base prefix to produce larger supernets
- C) `10.0.0.0/24`, `10.0.1.0/24`, `10.0.2.0/24` — `newbits = 8` extends the `/16` prefix by 8 bits to produce `/24` subnets; `netnum` 0, 1, 2 selects the first, second, and third `/24` block within `10.0.0.0/16`
- D) `10.0.0.0/24`, `10.0.8.0/24`, `10.0.16.0/24` — `newbits = 8` shifts the third octet by 8 with each `netnum` increment

### Question 60 — `flatten()` to Consolidate Per-AZ Subnet ID Lists from a Module

**Difficulty**: Hard
**Answer Type**: many
**Topic**: `flatten()` recursively unwraps a list-of-lists into a single flat list, preserving order without deduplicating; it differs from `concat()` which joins multiple separate flat lists

**Scenario**:
A team calls a reusable networking module three times — once per availability zone. Each module instance outputs `subnet_ids` as a `list(string)`. The root module collects these in a local:

```hcl
locals {
  all_subnet_ids = [
    module.network_az1.subnet_ids,   # ["subnet-a1", "subnet-a2"]
    module.network_az2.subnet_ids,   # ["subnet-b1"]
    module.network_az3.subnet_ids,   # ["subnet-c1", "subnet-c2"]
  ]
}
```

`local.all_subnet_ids` is currently a `list(list(string))`. They need a flat `list(string)` to pass to an `aws_lb` resource's `subnets` argument, which does not accept nested lists. The team applies `flatten(local.all_subnet_ids)`.

**Question**:
Which TWO statements accurately describe what `flatten()` does in this scenario?

- A) `flatten(local.all_subnet_ids)` produces `["subnet-a1", "subnet-a2", "subnet-b1", "subnet-c1", "subnet-c2"]` — a single flat `list(string)` in the original order, with no deduplication
- B) `flatten()` removes duplicate subnet IDs — if `"subnet-a1"` appeared in both `module.network_az1` and `module.network_az2`, `flatten()` would produce it only once
- C) `flatten()` is distinct from `concat()` in this use case: `concat()` requires separate list arguments (e.g., `concat(module.network_az1.subnet_ids, module.network_az2.subnet_ids, module.network_az3.subnet_ids)`), while `flatten()` operates on a single collection that already contains the nested lists
- D) `flatten()` only unwraps one level of nesting — it cannot handle more than two levels deep, so `list(list(list(string)))` would require multiple nested `flatten()` calls

### Question 61 — `nullable = false` Rejects Explicit `null` Even When a Default Exists

**Difficulty**: Medium
**Answer Type**: one
**Topic**: `nullable = false` prevents callers from explicitly passing `null` to override a variable's default — Terraform errors even if a `default` is defined; by contrast the default `nullable = true` permits explicit null overrides

**Scenario**:
A team writes a module with the following variable:

```hcl
variable "log_retention_days" {
  type     = number
  default  = 90
  nullable = false
}
```

A CI system that consumes this module passes all optional variables as explicit `null` to signal "use the default":

```hcl
module "app" {
  source             = "./modules/app"
  log_retention_days = null
}
```

Running `terraform plan` produces an error: `The argument "log_retention_days" is required. The root module input variable "log_retention_days" has its nullable attribute set to "false" which means null values cannot be provided.`

**Question**:
Why does Terraform error even though `default = 90` is set?

- A) Setting `nullable = false` removes the variable's `default` value — once `nullable = false` is set, the variable becomes required and `default` is silently ignored
- B) Terraform errors because variables of type `number` never accept `null` regardless of the `nullable` setting — the error would occur even without `nullable = false`
- C) `nullable = false` prevents callers from explicitly passing `null` to the variable. Normally, passing `null` overrides the `default` (because `null` is a valid explicit value when `nullable = true`). With `nullable = false`, Terraform rejects the explicit `null` assignment — the `default` is only used when the caller provides no value at all, not when they actively pass `null`
- D) The error is caused by a type mismatch: `null` cannot be coerced to `number`, so Terraform errors before evaluating the `nullable` constraint

### Question 62 — `try()` to Safely Access an Optional Map Key

**Difficulty**: Medium
**Answer Type**: one
**Topic**: `try(expr, fallback)` returns the fallback value when the primary expression raises a Terraform evaluation error — the idiomatic pattern for optional map keys that may not be present

**Scenario**:
A team writes a configuration that reads application settings from a variable of type `map(string)`. Some deployments include a `"log_level"` key; others omit it. The team wants to use `"info"` as the default log level whenever the key is absent. A developer writes:

```hcl
locals {
  log_level = try(var.app_config["log_level"], "info")
}
```

A colleague suggests replacing this with `lookup(var.app_config, "log_level", "info")`. Both approaches compile without errors.

**Question**:
Which statement correctly explains how `try()` works in this expression, and when `try()` is preferable to `lookup()`?

- A) `try()` and `lookup()` are identical in behaviour — `try()` is simply an alias for `lookup()` introduced in a later Terraform version for readability
- B) `try(var.app_config["log_level"], "info")` evaluates `var.app_config["log_level"]`. If the key does not exist, bracket indexing raises an error, and `try()` catches that error and returns the fallback `"info"`. `try()` is more general than `lookup()` because it can wrap any expression — not just map lookups — making it the preferred pattern when the optional access involves type coercions, attribute traversals, or function calls that might fail
- C) `try()` only catches errors from network calls — it is not designed for map key lookups. Using bracket indexing `[]` with a missing key always returns `null` rather than an error, so `try()` has no effect in this scenario
- D) `try()` evaluates all of its arguments simultaneously and returns the one with the highest non-null type priority — it does not return the first non-erroring expression

### Question 63 — `for_each` with a Map: Two True Facts About Instance Addressing

**Difficulty**: Hard
**Answer Type**: many
**Topic**: `for_each` with a map creates resource instances addressed by string key in state; adding or removing an individual key only creates or destroys that specific instance without affecting others

**Scenario**:
A team migrates from `count`-based EC2 instances to `for_each`-based instances using a map variable after experiencing unexpected replacements when server names were reordered. Their new configuration:

```hcl
variable "servers" {
  type = map(string)
  default = {
    web = "t3.micro"
    app = "t3.small"
    db  = "t3.medium"
  }
}

resource "aws_instance" "app" {
  for_each      = var.servers
  ami           = "ami-0abc123"
  instance_type = each.value
  tags          = { Name = each.key }
}
```

After the first successful `terraform apply`, the team later removes the `"app"` key from the map and runs `terraform plan`.

**Question**:
Which TWO statements accurately describe how Terraform handles the `for_each` map in this configuration?

- A) After the initial apply, each instance is tracked in state with a string-key address — `aws_instance.app["web"]`, `aws_instance.app["app"]`, and `aws_instance.app["db"]` — not by numeric index
- B) Removing `"app"` from the map causes Terraform to destroy all three instances and recreate only the two remaining ones, because `for_each` re-evaluates the entire collection on every apply
- C) Removing the `"app"` key from the map causes Terraform to plan the destruction of only `aws_instance.app["app"]` — the `"web"` and `"db"` instances are unaffected because they retain their stable string-key identifiers
- D) `for_each` with a map requires the map values to be unique — if two keys shared the value `"t3.micro"`, Terraform would error and refuse to create the instances

### Question 64 — `terraform output -raw` for Shell Variable Assignment in CI

**Difficulty**: Easy
**Answer Type**: one
**Topic**: `terraform output -raw <name>` prints the raw string value without surrounding double quotes — required for clean shell variable assignment in CI scripts

**Scenario**:
A CI pipeline script deploys infrastructure with Terraform and then configures an application using the provisioned RDS endpoint. The script runs:

```bash
DB_ENDPOINT=$(terraform output db_endpoint)
```

When the engineer inspects `$DB_ENDPOINT`, it contains `"mydb.cluster-abc123.us-east-1.rds.amazonaws.com"` — with surrounding double-quote characters included. This causes the subsequent `psql` connection command to fail because the hostname has literal quotes around it.

**Question**:
Which `terraform output` flag resolves this by printing the value without surrounding quotes?

- A) `terraform output --strip-quotes db_endpoint` — the `--strip-quotes` flag is the standard way to remove surrounding quotation marks from string outputs
- B) `terraform output -json db_endpoint | jq -r '.value'` — piping to `jq` with the `-r` flag is the only supported method to extract a raw string from a Terraform output
- C) `terraform output -raw db_endpoint` — the `-raw` flag prints the string value without surrounding quotes or newline padding, making it suitable for direct shell variable assignment
- D) `terraform output -plain db_endpoint` — the `-plain` flag suppresses all formatting including quotes and is the recommended flag for CI pipeline usage

### Question 65 — CI Pipeline Expected `check` Block to Block the Deploy

**Difficulty**: Medium
**Answer Type**: one
**Topic**: `check` block assertion failures emit a warning and do not set a non-zero exit code — a failing `check` block never prevents `terraform apply` from completing successfully

**Scenario**:
A platform team adds a `check` block to their Terraform configuration to verify that a newly deployed web application's `/health` endpoint returns HTTP 200 before the pipeline marks the deployment as successful:

```hcl
check "app_health" {
  data "http" "endpoint" {
    url = "https://${aws_lb.web.dns_name}/health"
  }

  assert {
    condition     = data.http.endpoint.status_code == 200
    error_message = "Health endpoint returned ${data.http.endpoint.status_code}, expected 200."
  }
}
```

During a problematic deployment the health endpoint returns HTTP 503, but the CI pipeline still marks the deployment green and Terraform exits with code `0`. The team is surprised — they expected the `check` block to fail the pipeline.

**Question**:
Why did the CI pipeline continue to report success despite the health check failure?

- A) The `check` block only evaluates during `terraform plan`, not `terraform apply` — it never runs after resources are deployed, so the HTTP 503 was not captured
- B) A `check` block assertion failure is a warning, not an error — Terraform prints a warning message to stderr but continues executing and exits with code `0`, so the pipeline's success/failure detection (based on exit code) sees a clean exit
- C) The scoped `data "http"` source inside the `check` block suppresses all HTTP errors — only assertions that reference module-level resources can produce non-zero exit codes
- D) The `check` block requires `depends_on = [aws_lb.web]` inside the assertion block to evaluate after the load balancer is created — without it, the assertion is skipped entirely

### Question 66 — AMI Architecture Mismatch Detected by `precondition`

**Difficulty**: Medium
**Answer Type**: many
**Topic**: A failing `precondition` prevents the resource change from occurring — the resource is left in its previous state (unchanged or non-existent); the apply fails before the provider makes any API call for that resource

**Scenario**:
A team provisions an EC2 instance and uses a `precondition` to verify the selected AMI is `x86_64` before the instance is created:

```hcl
resource "aws_instance" "web" {
  ami           = data.aws_ami.selected.id
  instance_type = "t3.micro"

  lifecycle {
    precondition {
      condition     = data.aws_ami.selected.architecture == "x86_64"
      error_message = "The selected AMI must be x86_64 architecture, got ${data.aws_ami.selected.architecture}."
    }
  }
}
```

This is a brand-new environment — `aws_instance.web` does not yet exist in state. The data source returns an ARM64 AMI. Running `terraform apply` fails with the precondition error.

**Question**:
Which TWO statements accurately describe the state of the system after the failed apply?

- A) The precondition fires before Terraform makes any API call to create the EC2 instance — `aws_instance.web` is not created in AWS and is not present in the state file
- B) Terraform partially creates the EC2 instance (allocates the instance ID) and then rolls back the creation after the precondition fails — the instance briefly exists in AWS before being deleted
- C) The error message includes the actual architecture value from the data source because `data.aws_ami.selected.architecture` is interpolated directly into the `error_message` string
- D) The apply failure causes Terraform to delete the data source's results from the state file — the next `terraform plan` will re-fetch the AMI information from scratch

### Question 67 — Attempt to Use `self` Inside a `precondition`

**Difficulty**: Easy
**Answer Type**: one
**Topic**: `self` is only valid inside `postcondition` blocks, where it references the resource's attributes after the change has been applied — `self` is not available in `precondition` blocks

**Scenario**:
A developer writes a lifecycle block with both a `precondition` and a `postcondition` for an S3 bucket:

```hcl
resource "aws_s3_bucket" "logs" {
  bucket = var.bucket_name

  lifecycle {
    precondition {
      condition     = self.bucket != ""
      error_message = "Bucket name must not be empty."
    }

    postcondition {
      condition     = self.id != ""
      error_message = "Bucket must have a non-empty ID after creation."
    }
  }
}
```

Running `terraform validate` produces an error on the `precondition` block referencing `self`.

**Question**:
Why is `self` invalid inside the `precondition` block?

- A) `self` is not a valid keyword in any Terraform lifecycle block — it is only available inside `provisioner` blocks and is not supported in `precondition` or `postcondition`
- B) `self` references the resource's attributes *after* the create, update, or destroy operation has completed. In a `precondition`, the resource change has not yet happened — there are no post-change attributes to reference, so `self` is meaningless and is not available
- C) `self` is available in both `precondition` and `postcondition`, but it can only reference attributes that are known at plan time — dynamic attributes like `bucket` are not eligible
- D) `self` is only invalid when the resource does not yet exist in state — on a subsequent apply where the resource already exists, `self` would work correctly in a `precondition`

### Question 68 — Security Audit Finds DB Password in Plaintext State Despite `sensitive = true`

**Difficulty**: Hard
**Answer Type**: many
**Topic**: `sensitive = true` only masks terminal output — the value is still written as plaintext to `terraform.tfstate`; protecting state requires an encrypted remote backend and strict access controls

**Scenario**:
A security audit scans the team's infrastructure configuration. The auditor notes that the RDS master password is declared as a sensitive variable and the output is also marked sensitive:

```hcl
variable "db_master_password" {
  type      = string
  sensitive = true
}

output "db_password_hint" {
  value     = var.db_master_password
  sensitive = true
}
```

Despite both being marked `sensitive = true`, the auditor finds the actual password value in plaintext inside `terraform.tfstate` stored in the team's S3 bucket. The team lead is confused — they believed `sensitive = true` protected the password.

**Question**:
Which TWO statements accurately explain the audit finding and the corrective actions required?

- A) `sensitive = true` is purely a display-level control — it suppresses the value in `terraform plan`, `terraform apply`, and `terraform output` terminal output, but Terraform always writes resource attribute values (including sensitive ones) to `terraform.tfstate` in plaintext. The `sensitive` flag has no effect on what is stored in state
- B) `sensitive = true` on an output block encrypts the value in `terraform.tfstate` using Terraform's built-in AES encryption — the auditor must have used `terraform state pull` with elevated permissions to bypass the encryption
- C) To protect the password in state, the team should store state in an encrypted remote backend — for example, an S3 bucket with server-side encryption (SSE-KMS) enabled, or HCP Terraform's encrypted state storage — and apply strict IAM policies to restrict who can read the state file
- D) The correct long-term solution is to stop storing the password in Terraform configuration entirely by using the HashiCorp Vault provider to retrieve dynamic credentials at apply time — this prevents the password from ever appearing in the Terraform state file as a static value

### Question 69 — Variable Has Two `validation` Blocks; Both Conditions Fail

**Difficulty**: Medium
**Answer Type**: one
**Topic**: When a variable has multiple `validation` blocks, all blocks are evaluated independently and all failures are reported simultaneously — not just the first one

**Scenario**:
A team defines an `instance_type` variable with two separate validation rules: one requiring the value to start with `"t3."` and one requiring the value to be in a specific approved list:

```hcl
variable "instance_type" {
  type = string

  validation {
    condition     = startswith(var.instance_type, "t3.")
    error_message = "Instance type must be in the t3 family."
  }

  validation {
    condition     = contains(["t3.micro", "t3.small", "t3.medium"], var.instance_type)
    error_message = "Instance type must be one of: t3.micro, t3.small, t3.medium."
  }
}
```

A developer passes `-var "instance_type=m5.xlarge"` during a plan. This value fails both validation conditions.

**Question**:
What does Terraform report when both validation conditions fail?

- A) Terraform evaluates validation blocks in order and stops at the first failure — only the error message from the first `validation` block ("Instance type must be in the t3 family.") is displayed
- B) Terraform evaluates all `validation` blocks independently and reports error messages for every block whose `condition` evaluates to `false` — the developer sees both error messages in the same plan failure output
- C) Terraform merges all failing `validation` error messages into a single combined error string separated by semicolons — only one error block appears in the output regardless of how many validations fail
- D) Terraform evaluates both `validation` blocks but only reports the error from the block with the stricter (more specific) condition, determined by the length of the `error_message` string

### Question 70 — `check` Block Scoped Data Source Returns 503 During `terraform plan`

**Difficulty**: Medium
**Answer Type**: one
**Topic**: A failing scoped `data` source inside a `check` block generates a warning (not an error) and does not abort the plan or apply — unlike top-level `data` source failures which abort the plan

**Scenario**:
A team's Terraform configuration contains a `check` block that uses a scoped `data "http"` source to verify their API gateway is reachable. During a routine `terraform plan` in CI, the API gateway is temporarily unavailable and the HTTP request fails with a connection timeout. The team is debating whether this will cause the plan to fail and block the CI pipeline.

```hcl
check "api_reachable" {
  data "http" "gateway" {
    url = "https://api.example.com/ping"
  }

  assert {
    condition     = data.http.gateway.status_code == 200
    error_message = "API gateway is not reachable (status: ${data.http.gateway.status_code})."
  }
}
```

**Question**:
What happens when the scoped `data "http"` source inside the `check` block fails due to a connection timeout?

- A) The plan fails with a provider error and the CI pipeline receives a non-zero exit code — a failing data source inside a `check` block behaves identically to a failing top-level data source
- B) Because the data source is declared inside a `check` block (not at the top level), its failure is treated as a warning. Terraform emits a warning about the data source error, skips the `assert` evaluation, and the plan/apply continues normally — the CI pipeline receives exit code `0`
- C) A connection timeout inside a `check` block causes Terraform to retry the HTTP request three times before giving up and aborting the plan with a hard error
- D) The scoped data source failure is silently ignored — Terraform does not print any warning or message when a `check` block's embedded data source fails to retrieve data

### Question 71 — Colleague Claims `precondition` Has the Same `var`-Only Scope as `validation`

**Difficulty**: Hard
**Answer Type**: one
**Topic**: `precondition` and `postcondition` blocks can reference any in-scope value — data sources, locals, module outputs, other resource attributes — unlike `validation` blocks which are restricted to `var.<name>` only

**Scenario**:
A senior developer reviews a pull request where a teammate has written a `precondition` in an EC2 resource's `lifecycle` block that references a data source attribute:

```hcl
resource "aws_instance" "web" {
  ami           = data.aws_ami.selected.id
  instance_type = var.instance_type

  lifecycle {
    precondition {
      condition     = data.aws_ami.selected.architecture == "x86_64"
      error_message = "Selected AMI must be x86_64 architecture."
    }
  }
}
```

The senior developer comments: "This will fail at plan time because `precondition` has the same restriction as `validation` blocks — you can only reference `var.<name>` in the condition. You need to move this to a validation block and check `var.ami_id` instead."

**Question**:
Is the senior developer's review comment correct?

- A) Yes — `precondition` blocks share the same expression scope restriction as `validation` blocks. Both can only reference `var.<name>` in their `condition` expression; referencing data sources causes a parse error
- B) No — `precondition` and `postcondition` blocks can reference any value that is in scope at the point in the Terraform evaluation where they run, including data source attributes, locals, module outputs, and other resource attributes. Only `variable` `validation` blocks are restricted to `var.<name>`. The pull request code is valid
- C) Yes — `precondition` blocks can reference locals and variables but not data sources, because data sources may not be read until apply time and their values could be unknown during the precondition evaluation
- D) The comment is partially correct — `precondition` can reference data sources, but only data sources declared within the same resource block, not top-level data sources

### Question 72 — Output Block References Sensitive Variable Without `sensitive = true`

**Difficulty**: Easy
**Answer Type**: one
**Topic**: Terraform raises an error during plan when an output block references a sensitive value (variable, local, or resource attribute) without marking the output block itself as `sensitive = true`

**Scenario**:
A team has a sensitive database password variable and wants to expose a connection string as a Terraform output for use by an application deployment step. They write:

```hcl
variable "db_password" {
  type      = string
  sensitive = true
}

output "connection_string" {
  value = "postgres://admin:${var.db_password}@${aws_db_instance.main.endpoint}/appdb"
}
```

Running `terraform plan` fails immediately before any infrastructure changes are planned.

**Question**:
What error does Terraform produce, and what is the minimal fix?

- A) Terraform errors with `Output refers to sensitive values` — the output block must either add `sensitive = true` to suppress the value in CLI output, or the interpolation must be replaced with a non-sensitive value
- B) Terraform errors with `Sensitive variable cannot be used in string interpolation` — the password must be kept separate from the connection string and passed as an environment variable to the application instead
- C) Terraform errors with `Unknown value in output` — sensitive variables are treated as `(known after apply)` and cannot be referenced in outputs at plan time; they can only be referenced inside resource blocks
- D) Terraform silently replaces `${var.db_password}` with `(sensitive value)` in the output string and proceeds — no error is produced because the interpolation produces a masked string automatically

### Question 73 — `nonsensitive()` Used to Demote a Value for a Diagnostic Output

**Difficulty**: Medium
**Answer Type**: one
**Topic**: `nonsensitive()` explicitly removes the sensitive marking from a value, allowing it to appear in plaintext in outputs or expressions — the author takes responsibility for the security implications

**Scenario**:
A platform team stores a Kubernetes cluster CA certificate in Terraform as a sensitive value (because it is a secret). For internal debugging during development, a senior engineer wants to expose the base64-decoded certificate in a Terraform output so the team can quickly inspect it during `terraform output`. The output block:

```hcl
output "cluster_ca_cert_debug" {
  value = nonsensitive(base64decode(data.kubernetes_cluster.main.cluster_ca_certificate))
}
```

A junior developer asks what `nonsensitive()` does here and whether it is safe to use in production.

**Question**:
Which answer correctly explains `nonsensitive()` and when it should be used?

- A) `nonsensitive()` permanently removes the sensitive marking from the source data — after calling `nonsensitive()`, the original `data.kubernetes_cluster.main.cluster_ca_certificate` attribute also loses its sensitive marking throughout the entire configuration
- B) `nonsensitive()` creates a new copy of the value with the sensitive marking removed. The output will display the certificate in plaintext in `terraform output`. The author is explicitly taking responsibility for the security implications — in production environments, this would expose the certificate to anyone who can run `terraform output`, so it should be used only when the team has explicitly accepted that risk
- C) `nonsensitive()` is only valid when called inside `check` block assertions — using it in an `output` block causes a validation error
- D) `nonsensitive()` has no effect on storage — it is equivalent to setting `sensitive = false` on the output block, which is the default, so the function call is redundant

### Question 74 — Vault Dynamic Secrets vs `sensitive = true` for a Long-Lived DB Password

**Difficulty**: Hard
**Answer Type**: many
**Topic**: HashiCorp Vault dynamic secrets prevent static secret storage in state and configuration entirely; `sensitive = true` only masks terminal output but leaves the secret in plaintext state — these are complementary but distinct controls

**Scenario**:
A compliance team reviews two approaches for managing a production database password in Terraform. Approach A uses a `sensitive = true` variable with the password hardcoded in a `.tfvars` file (excluded from version control). Approach B uses the HashiCorp Vault provider to retrieve dynamic credentials at apply time:

```hcl
data "vault_generic_secret" "db_creds" {
  path = "secret/database/prod"
}

resource "aws_db_instance" "main" {
  password = data.vault_generic_secret.db_creds.data["password"]
}
```

The compliance team needs to understand what security guarantees each approach provides.

**Question**:
Which TWO statements accurately describe what the Vault dynamic secrets approach achieves that `sensitive = true` alone cannot?

- A) With the Vault approach, the database password never needs to appear as a static value in the Terraform configuration or in a `.tfvars` file — the password is generated or retrieved by Vault at apply time and is never stored in the source code repository
- B) The Vault approach prevents the database password from being written to `terraform.tfstate` — because the password is not a static Terraform value, it is never recorded in the state file at all
- C) With `sensitive = true` on a variable, the password is stored as an encrypted value in `terraform.tfstate` — the Vault approach and the `sensitive = true` approach provide identical state-level protection
- D) Vault supports secret rotation and dynamic credentials with short TTLs — if Vault is configured to generate short-lived dynamic database credentials, the password retrieved during one apply is different from the one retrieved during the next apply, reducing the blast radius of a credential leak

### Question 75 — `terraform validate` Does Not Trigger Variable Validation Blocks

**Difficulty**: Medium
**Answer Type**: one
**Topic**: `terraform validate` checks HCL syntax and provider schema correctness — it does not execute variable validation blocks because it does not require variable values to be provided

**Scenario**:
A developer adds a new variable to a Terraform configuration with a `validation` block that restricts allowed values to `["dev", "staging", "production"]`. To test the new validation rule quickly, the developer runs `terraform validate` without providing a value for the variable. The command succeeds with "Success! The configuration is valid." The developer assumes the validation block is broken because it didn't catch anything.

**Question**:
Why did `terraform validate` succeed without triggering the validation block?

- A) `terraform validate` evaluates validation blocks, but only when a `.tfvars` file is present in the working directory — without a `.tfvars` file, validation blocks are silently skipped
- B) `terraform validate` checks only HCL syntax and provider schema correctness. It does not require variable values to be provided and does not evaluate variable `validation` blocks. Validation blocks are evaluated during `terraform plan`, when variable values must be resolved — running `terraform plan -var "environment=invalid_value"` would trigger the validation failure
- C) `terraform validate` triggers validation blocks only for variables that have a `default` value set — variables without defaults are skipped during validation to avoid requiring user input
- D) `terraform validate` is not supported when the configuration has unsatisfied required variables — the command would have failed before reaching the validation block evaluation, which is why the validation failure was not reported

### Question 76 — `postcondition` Fails After RDS Instance Is Successfully Created

**Difficulty**: Easy
**Answer Type**: one
**Topic**: A failing `postcondition` means the resource was already created (or changed) by the provider — it exists in AWS and is recorded in state, but the apply is marked as failed

**Scenario**:
A team adds a `postcondition` to an RDS resource to verify the instance status is `"available"` immediately after creation:

```hcl
resource "aws_db_instance" "main" {
  identifier        = "prod-db"
  instance_class    = "db.t3.micro"
  engine            = "mysql"
  engine_version    = "8.0"
  allocated_storage = 20
  username          = "admin"
  password          = var.db_password

  lifecycle {
    postcondition {
      condition     = self.status == "available"
      error_message = "RDS instance status is '${self.status}', expected 'available'."
    }
  }
}
```

Immediately after the provider creates the instance, its status is `"modifying"` (AWS is still applying the initial configuration). The postcondition fails.

**Question**:
What is the state of the RDS instance after the failed apply?

- A) The postcondition failure causes Terraform to issue a `DeleteDBInstance` API call to roll back the creation — the RDS instance is deleted from AWS and removed from state
- B) The RDS instance was already created by the AWS provider API call before the postcondition was evaluated — it exists in AWS and is recorded in `terraform.tfstate`. The apply is marked as failed with the postcondition error message, but the resource is not deleted. The team can re-run `terraform apply` once the instance reaches `"available"` status
- C) The postcondition failure is treated identically to a precondition failure — the resource never reaches a created state and is not recorded in state
- D) The RDS instance exists in AWS but is NOT recorded in `terraform.tfstate` — Terraform only records a resource in state after all its postconditions pass successfully

### Question 77 — Registry Module Without a `version` Constraint Breaks in CI

**Difficulty**: Medium
**Answer Type**: one
**Topic**: A Terraform Registry module source without a `version` constraint causes `terraform init` to always download the latest available version — a future major release with breaking changes will silently break the configuration

**Scenario**:
A platform team adds a VPC module from the Terraform Registry to their production configuration without specifying a version constraint:

```hcl
module "vpc" {
  source = "terraform-aws-modules/vpc/aws"

  cidr = "10.0.0.0/16"
  azs  = ["us-east-1a", "us-east-1b"]
}
```

The configuration works correctly for six months. The module publisher then releases `v6.0.0`, which renames the `private_subnets` argument to `private_subnet_cidrs` and removes the old argument entirely. The next CI run calls `terraform init`, downloads `v6.0.0`, and the plan immediately fails with "An argument named 'private_subnets' is not expected here."

**Question**:
What is the root cause of this failure, and what change prevents it from recurring?

- A) The module source path is missing the provider suffix — the correct format is `terraform-aws-modules/vpc/aws/v6` and the version must be embedded in the source string
- B) Without a `version` constraint, `terraform init` always resolves and downloads the latest published version of the module. When a new major version with breaking changes was published, the CI run silently adopted it. Adding `version = "~> 5.0"` to the module block pins the resolution to compatible 5.x releases and prevents automatic adoption of v6.x
- C) The issue is caused by using `~>` pessimistic pinning in the backend, which propagates to module version resolution — using exact version pinning with `version = "= 5.9.0"` is the only safe approach
- D) CI pipelines should add `-no-upgrade` flag to `terraform init` to prevent version resolution — without this flag, `terraform init` always upgrades all modules to their latest versions regardless of whether a version constraint is present

### Question 78 — Child Module Needs a Non-Default Provider Alias (Multi-Region)

**Difficulty**: Hard
**Answer Type**: many
**Topic**: The `providers` meta-argument on a module block maps provider aliases from the root module to the provider names expected by the child module — without it, child modules always use the default (non-aliased) provider configuration

**Scenario**:
A team's root module configures two AWS providers: the default configuration for `us-east-1` and an aliased configuration for `eu-west-1`:

```hcl
provider "aws" {
  region = "us-east-1"
}

provider "aws" {
  alias  = "eu"
  region = "eu-west-1"
}
```

A networking child module provisions subnets. The team wants this module's resources to be created in `eu-west-1`. They add:

```hcl
module "networking_eu" {
  source = "./modules/networking"

  providers = {
    aws = aws.eu
  }
}
```

A colleague questions whether the `providers` map is actually necessary, arguing "provider configurations flow to child modules automatically."

**Question**:
Which TWO statements accurately describe the `providers` meta-argument and the behaviour without it?

- A) Without the `providers` map, the child module automatically uses the provider configuration that matches its resources' region — Terraform inspects each resource and routes it to the correct provider based on the `region` attribute
- B) Without the `providers` map, the child module uses the **default** (non-aliased) `aws` provider configuration — all module resources would be created in `us-east-1` regardless of what the team intended, because child modules inherit only the default provider unless explicitly overridden
- C) The `providers` map `{ aws = aws.eu }` tells Terraform: "when this child module refers to provider `aws`, use the aliased provider `aws.eu` from the root module." This is the only mechanism for directing a child module to use a non-default provider alias
- D) The `providers` meta-argument is only required when the child module declares its own `provider` block — if the child module has no `provider` block, provider configuration always flows automatically from the root

### Question 79 — Renaming a Module Block Label Triggers Full Destroy and Recreate

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Terraform tracks all resources inside a child module under the module's label in state — renaming `module "network"` to `module "networking"` changes every resource's state address, causing Terraform to plan destroying all old-address resources and creating all new-address resources

**Scenario**:
A team decides to rename their networking module block from `module "network"` to `module "networking"` for clarity. The child module code is unchanged — only the label in the root module block is updated. No other changes are made. Running `terraform plan` outputs:

```
Plan: 47 to add, 0 to change, 47 to destroy.
```

The team is alarmed — they expected zero changes since no infrastructure code changed.

**Question**:
Why does renaming the module block label cause a full destroy-and-recreate plan?

- A) Renaming a module label triggers a forced replacement of all child module resources because Terraform treats the label as a hash seed for resource IDs — changing the label changes the generated IDs
- B) Terraform stores all resources inside a module using their full address, which includes the module label. `module.network.aws_subnet.public[0]` and `module.networking.aws_subnet.public[0]` are two completely different state addresses. Terraform sees no state entry for `module.networking.*` (create 47) and sees orphaned entries for `module.network.*` (destroy 47) — it has no way to know these refer to the same infrastructure
- C) The rename triggers an automatic `terraform init` to re-download the module source, and during re-initialisation the module version is bumped, which causes breaking changes in the resource schema
- D) Module block labels must match the `module_name` metadata field declared inside the child module's `versions.tf` — a mismatch between the call label and the declared name causes a full replacement cycle

### Question 80 — Plain `terraform init` Doesn't Update a Cached Module to a Newer Patch Version

**Difficulty**: Medium
**Answer Type**: one
**Topic**: `terraform init` without flags reuses a cached module version if it satisfies the constraint — to download a newer compatible version within the allowed range, `terraform init -upgrade` is required

**Scenario**:
A team's Terraform configuration pins a registry module with `version = "~> 5.0"`. Six months ago they ran `terraform init`, which downloaded and cached version `5.0.0` in `.terraform/modules/`. The module publisher has since released `5.7.3` with several important bug fixes the team wants to adopt. A developer runs `terraform init` again, expecting the module to update to `5.7.3`. The plan output still references `5.0.0`.

**Question**:
Why did the re-run of `terraform init` not update the module to `5.7.3`?

- A) Version `5.7.3` exceeds the `~> 5.0` constraint — the pessimistic operator `~>` only allows patch increments (5.0.0, 5.0.1, 5.0.2…), not minor version bumps (5.1.0, 5.7.3)
- B) `terraform init` without any flags does not check for newer versions if a module version already exists in the local cache that satisfies the declared constraint. Since `5.0.0` satisfies `~> 5.0`, no network request is made. To resolve the latest compatible version within the constraint, the developer must run `terraform init -upgrade`
- C) Module version upgrades require editing the `.terraform/modules/modules.json` file manually to update the version field before running `terraform init` — `terraform init` alone never changes a cached module version
- D) The `version` argument in a module block is evaluated only on the first `terraform init` — subsequent runs always use the same version that was downloaded initially, regardless of flags

### Question 81 — Root Module References a Child Module Output That Was Never Declared

**Difficulty**: Easy
**Answer Type**: one
**Topic**: Child module outputs must be explicitly declared with an `output` block — referencing `module.<name>.<value>` from the root module when no matching `output` block exists in the child causes an error at plan time

**Scenario**:
A team's root module creates an EC2 instance inside a child module and needs the instance's private IP address to create a Route 53 DNS record. The developer writes:

```hcl
resource "aws_route53_record" "app" {
  zone_id = var.zone_id
  name    = "app.internal.example.com"
  type    = "A"
  ttl     = 60
  records = [module.compute.private_ip]
}
```

The child module (`modules/compute/main.tf`) creates `aws_instance.server` but the module's `outputs.tf` file is empty. Running `terraform plan` fails immediately.

**Question**:
What error does Terraform produce, and what is the minimal fix?

- A) Terraform produces a type error — `records` expects a `list(string)` but `module.compute.private_ip` resolves to a single string. The fix is to wrap it in brackets: `records = [module.compute.private_ip]`
- B) Terraform produces a reference error stating that the module has no output named `private_ip`. The minimal fix is to add an output block to the child module's `outputs.tf`: `output "private_ip" { value = aws_instance.server.private_ip }`
- C) Terraform produces an error because `private_ip` is a computed attribute — it cannot be referenced in another resource until after the EC2 instance has been created. The fix is to run `terraform apply` first to create the instance, then re-run `terraform plan`
- D) Terraform produces a module encapsulation error — resource attributes from inside a child module can only be used by other resources inside the same module, never by the root module

### Question 82 — `for_each` Module: Adding a New Environment Key Affects Only That Instance

**Difficulty**: Hard
**Answer Type**: many
**Topic**: A `for_each` module block keyed by a map creates one module instance per map entry addressed by string key in state — adding a new key creates only that new instance; existing instances are unaffected

**Scenario**:
A team uses `for_each` on a module block to provision per-environment networking infrastructure:

```hcl
module "env" {
  for_each = {
    dev     = "10.0.0.0/16"
    staging = "10.1.0.0/16"
    prod    = "10.2.0.0/16"
  }
  source   = "./modules/networking"
  vpc_cidr = each.value
}
```

After a successful `terraform apply`, the state contains `module.env["dev"]`, `module.env["staging"]`, and `module.env["prod"]` with all their child resources. The team adds a fourth entry `dr = "10.3.0.0/16"` to the map and runs `terraform plan`.

**Question**:
Which TWO statements accurately describe what the plan shows?

- A) Terraform plans to create a new module instance `module.env["dr"]` and all child resources inside it — the three existing module instances (`module.env["dev"]`, `module.env["staging"]`, `module.env["prod"]`) are shown as unchanged and are not touched
- B) Because `for_each` re-evaluates the entire map on every plan, Terraform destroys all four instances and recreates them — adding any key to the map always triggers a full replacement cycle
- C) Each module instance created by `for_each` is addressed in state using the map key as a string — the new `"dr"` entry creates a new `module.env["dr"]` address in state independent of the three existing entries
- D) Terraform errors when a new entry is added to a `for_each` module map after the initial apply — the map must be finalized before the first apply and cannot be extended without using `terraform state import`

### Question 83 — Detecting Configuration Drift Without Proposing Infrastructure Changes

**Difficulty**: Easy
**Answer Type**: one
**Topic**: `terraform plan -refresh-only` shows drift between recorded state and live cloud state without producing a plan to modify infrastructure; `terraform apply -refresh-only` accepts the drift by updating state — only `-refresh-only` plan is read-only

**Scenario**:
An operations engineer discovers that a colleague manually changed a production EC2 instance type from `t3.small` to `t3.large` using the AWS console, bypassing Terraform. The Terraform configuration still declares `instance_type = "t3.small"`. The engineer wants to inspect exactly what has drifted before deciding whether to revert the manual change (restore t3.small) or accept it (update the configuration to `t3.large`). The engineer does not want Terraform to make any changes to infrastructure or write anything to the state file during this inspection step.

**Question**:
Which command satisfies these requirements — showing the drift without modifying infrastructure or state?

- A) `terraform plan` — a standard plan always shows configuration drift as a proposed change in the plan output and does not write anything to state
- B) `terraform plan -refresh-only` — this command refreshes Terraform's view of the live infrastructure and displays what has changed relative to the recorded state, but it does not generate a plan to modify any infrastructure resources and does not write changes to the state file
- C) `terraform apply -refresh-only` — the `-refresh-only` flag prevents infrastructure changes; it only updates the state file to reflect the live cloud, which is a safe read-only operation
- D) `terraform show -json` — this command reads the current state file and displays the recorded values; comparing its output to the live AWS console shows what has drifted

### Question 84 — Backend Migration: What Happens to the Old Local State File

**Difficulty**: Easy
**Answer Type**: one
**Topic**: `terraform init -migrate-state` copies state to the new backend but leaves the old `terraform.tfstate` file in the working directory — Terraform stops reading from the local file but does not delete it

**Scenario**:
A team has been using the local backend for three months. Their `terraform.tfstate` file in the working directory contains the full production state with 120 managed resources. They decide to migrate to an S3 remote backend for team collaboration. They add the backend block to their configuration and run `terraform init -migrate-state`. Terraform confirms the migration succeeds and all resources are now tracked in S3. A developer then asks: "Should we delete the local `terraform.tfstate` file now that we've migrated?"

**Question**:
What is the correct answer to the developer's question?

- A) Yes — Terraform automatically marks the local `terraform.tfstate` as invalid after migration by writing a special header to it. Deleting the now-invalid file is required to prevent Terraform from accidentally reverting to the local backend
- B) After successful migration, the local `terraform.tfstate` is left in place unchanged — Terraform will no longer read from it (all subsequent operations use the S3 backend), but the file is not deleted. The team should keep it temporarily as a backup, verify that S3 state is correct, and then delete it or move it to secure storage — but they should not commit it to version control
- C) No action is needed — Terraform automatically detects the local file on every init and will re-migrate it to S3, so keeping it present is safe and ensures continuity if the S3 backend becomes temporarily unavailable
- D) The `terraform init -migrate-state` command deletes the local `terraform.tfstate` file after confirming the migration — the developer is asking about a file that no longer exists

### Question 85 — `terraform state rm` Used to Abandon Management of a Resource

**Difficulty**: Medium
**Answer Type**: one
**Topic**: `terraform state rm` removes a resource's state entry — the actual cloud resource is unaffected, but if the resource block remains in configuration, the next `terraform plan` treats it as a new resource to create

**Scenario**:
A team has an EC2 instance `aws_instance.legacy` that was provisioned by an old process. They want Terraform to stop managing it permanently — specifically, they do not want Terraform to ever destroy it. They run `terraform state rm aws_instance.legacy`. The command succeeds. However, the `aws_instance.legacy` resource block is still present in `main.tf`. A teammate runs `terraform plan` an hour later and sees the EC2 instance scheduled for creation.

**Question**:
Why does `terraform plan` show the instance as a resource to create, and what additional step was missing?

- A) `terraform state rm` issued a `DeleteInstance` API call to AWS and removed the instance — the next plan correctly shows it as a new resource because the instance no longer exists in the cloud
- B) `terraform state rm` removed the resource's entry from the state file, but the `aws_instance.legacy` block is still present in the configuration. With no state entry and a configuration block present, Terraform treats the resource as non-existent and plans to create it. The missing step is removing (or commenting out) the `aws_instance.legacy` resource block from `main.tf` — once the block is removed, Terraform has no configuration entry and no state entry and ignores the resource entirely
- C) `terraform state rm` only flags a resource for removal — the next `terraform plan` is required to confirm and finalize the removal from state; until the plan is run, the resource is still tracked by Terraform
- D) The plan shows a create because `terraform state rm` refreshes state from the cloud before removing the entry, and the refresh detected the instance had been terminated — the instance exists in configuration but not in AWS, so Terraform correctly plans to recreate it

### Question 86 — Stale State Lock from a Crashed CI Pipeline

**Difficulty**: Medium
**Answer Type**: one
**Topic**: `terraform force-unlock <LOCK_ID>` manually releases a stale DynamoDB lock — it should only be used when certain no other Terraform operation is running, because it removes the lock regardless of whether a real concurrent process holds it

**Scenario**:
A CI pipeline applies Terraform changes to production infrastructure using an S3 backend with DynamoDB state locking. The CI runner hosting the apply job crashes mid-apply due to an out-of-memory error. The Terraform process is killed abruptly without releasing the DynamoDB lock entry. Every subsequent `terraform apply` and `terraform plan` by any engineer fails with:

```
Error: Error acquiring the state lock

  Lock Info:
    ID:   a3f7c8b2-91d4-4e2e-bb10-fd3a9c0e1234
    Operation: OperationTypeApply
    ...
```

The on-call engineer needs to unblock the team immediately.

**Question**:
What is the correct recovery command, and what critical check must the engineer perform before running it?

- A) `terraform init -reconfigure` clears all backend state including stale locks — the engineer should run this command to reset the locking state before retrying the apply
- B) The engineer must modify the DynamoDB table directly in the AWS console and delete the item with `LockID = "a3f7c8b2-91d4-4e2e-bb10-fd3a9c0e1234"` — `terraform force-unlock` is only available in HCP Terraform, not open-source Terraform
- C) The correct command is `terraform force-unlock a3f7c8b2-91d4-4e2e-bb10-fd3a9c0e1234`. Before running it, the engineer must verify that the original CI process is truly dead — not still running in a degraded state somewhere. `force-unlock` removes the lock entry unconditionally; if another Terraform process is actually still modifying state, removing the lock allows two writers simultaneously, which can corrupt the state file
- D) The engineer should wait at least 15 minutes because DynamoDB lock entries automatically expire after a configurable TTL — Terraform sets this TTL to 15 minutes by default, so the lock will self-release without any manual intervention

### Question 87 — Two Simultaneous Applies Against S3 Backend Without DynamoDB Locking

**Difficulty**: Hard
**Answer Type**: many
**Topic**: The S3 backend without a `dynamodb_table` has no locking mechanism — concurrent `terraform apply` operations can both read, modify, and write state simultaneously, causing state corruption and orphaned resources

**Scenario**:
A team runs two separate CI pipelines that both target the same S3 backend with identical `bucket` and `key` values. The backend block does not include a `dynamodb_table` argument. Both pipelines trigger simultaneously due to a CI misconfiguration. Pipeline A creates three new EC2 instances and completes in 4 minutes. Pipeline B creates two new S3 buckets and completes in 5 minutes. When the operations team later runs `terraform plan`, it shows the three EC2 instances as resources "to be created" even though they exist in AWS.

**Question**:
Which TWO statements accurately explain what happened and the ongoing risk?

- A) Without a `dynamodb_table`, the S3 backend has no distributed locking mechanism. Both pipelines read the same initial state, made their respective changes, and each wrote their final state back to S3. Pipeline B's write (completing last) overwrote Pipeline A's write — Pipeline B's state only contains the two S3 buckets, with no record of the three EC2 instances created by Pipeline A
- B) S3 provides native atomic writes through object versioning, which prevents state corruption — the DynamoDB table is only needed to display a user-friendly "locked" error message when concurrent applies are attempted, not to actually prevent corruption
- C) The next `terraform plan` shows the three EC2 instances as "to be created" because they exist in AWS but are absent from the current state file (which was overwritten by Pipeline B). Without any state entry for these instances, Terraform considers them unmanaged and would create duplicate EC2 instances if `terraform apply` is run
- D) Terraform detects the state version mismatch from the two concurrent writes and automatically merges the two state files, preserving all resource records from both pipelines — the "to be created" output indicates a separate, unrelated issue

### Question 88 — Accidentally Overwriting Remote State with `terraform state push`

**Difficulty**: Medium
**Answer Type**: one
**Topic**: `terraform state push` overwrites remote state with the provided local file with no safety confirmation prompt — pushing an older state file loses all resource records added since that snapshot was taken

**Scenario**:
An engineer is investigating a state corruption issue. They have a local backup file `backup-last-week.tfstate` from seven days ago. Intending to inspect it with `terraform show`, they accidentally run:

```bash
terraform state push backup-last-week.tfstate
```

The command executes immediately with no confirmation prompt and succeeds. The team's production Terraform state in S3 is now overwritten with the seven-day-old snapshot. The team ran six successful `terraform apply` operations during the past week, adding 23 new resources and modifying 11 existing ones.

**Question**:
What is the immediate consequence of this accidental push, and what should the team do first?

- A) The push fails silently — `terraform state push` only works when the local file is newer than the remote state (based on the state serial number), so an older backup would be rejected and the production state is unaffected
- B) The production state is now the seven-day-old snapshot. All 23 resources added during the past week exist in AWS but are no longer recorded in state — Terraform considers them unmanaged. The team's immediate priority is to restore the correct state. If S3 bucket versioning was enabled, they can retrieve the previous state version using `aws s3api get-object --version-id <id>` and push it back with `terraform state push`. If versioning was not enabled, the state must be reconstructed by importing the 23 orphaned resources
- C) `terraform state push` automatically creates a timestamped backup of the existing remote state before overwriting it — the team can run `terraform state pull > current.tfstate` to retrieve this backup and push it back
- D) The team should immediately run `terraform apply` to re-create the 23 missing resources before anyone else runs `terraform plan`, because a plan would show 23 resources scheduled for destruction (since they exist in state but not in the cloud)

### Question 89 — `terraform state mv` During a Root-to-Module Refactor

**Difficulty**: Medium
**Answer Type**: one
**Topic**: `terraform state mv <source> <destination>` changes the resource's address in the state file without making any API calls or modifying the actual cloud resource — after the move, `terraform plan` sees no difference between the new configuration address and the updated state address

**Scenario**:
A team originally managed an EC2 instance directly in the root module as `aws_instance.web`. They refactor the configuration to move the instance into a new `module "compute"` child module, where it becomes `aws_instance.server`. Without any state manipulation, `terraform plan` shows:

```
  - aws_instance.web                       (destroy)
  + module.compute.aws_instance.server     (create)
```

The EC2 instance has been running in production for two years — the team cannot tolerate a destroy-and-recreate cycle. A senior engineer recommends running:

```bash
terraform state mv aws_instance.web module.compute.aws_instance.server
```

**Question**:
What does `terraform state mv` accomplish in this scenario, and what should `terraform plan` show immediately after?

- A) `terraform state mv` terminates the old EC2 instance and provisions a new one under the new module address — it achieves an in-place replacement that avoids the destroy-and-create cycle by using the same AMI and configuration
- B) `terraform state mv` renames the resource's address in the state file from `aws_instance.web` to `module.compute.aws_instance.server` without making any AWS API calls and without modifying the EC2 instance. The actual cloud resource is completely unaffected. After this command, `terraform plan` should show no changes (or only minor drift-related attribute updates) because the configuration address (`module.compute.aws_instance.server`) now matches the updated state address
- C) `terraform state mv` is equivalent to `terraform import` — it re-discovers the EC2 instance under the new module address by querying AWS, which is why it prevents the destroy-and-create cycle
- D) `terraform state mv` updates both the state file and the Terraform configuration automatically — the root module resource block is removed and the child module block is created as part of the command

### Question 90 — Importing a `for_each` Resource: Correct `to` Address Syntax

**Difficulty**: Medium
**Answer Type**: one
**Topic**: When the target resource uses `for_each`, the `import` block's `to` argument must include the specific instance key in square bracket notation — `resource_type.name["key"]` — the same syntax used in plan output and state addresses

**Scenario**:
A team manages EC2 instances using `for_each` keyed by server role:

```hcl
resource "aws_instance" "server" {
  for_each      = var.servers
  ami           = each.value.ami
  instance_type = each.value.instance_type
}
```

Currently `var.servers` has keys `"web"` and `"api"`. A pre-existing `"db"` instance (`i-0xyz789abc123`) was created manually and needs to be brought under Terraform management. The engineer writes an import block:

```hcl
import {
  to = ???
  id = "i-0xyz789abc123"
}
```

**Question**:
What is the correct value for the `to` argument?

- A) `aws_instance.server` — the `for_each` key is implied by the `id` argument; Terraform resolves the target instance from the cloud resource ID
- B) `aws_instance.server["db"]` — when the target resource uses `for_each`, the `to` argument must include the specific instance key in square brackets using the same notation used in plan output and state addresses
- C) `aws_instance.server.db` — dot notation is valid for both module path traversal and `for_each` key references within a resource address
- D) `aws_instance.server[db]` — the key is placed in square brackets without quotes; unquoted identifiers are valid for `for_each` string keys in import blocks

### Question 91 — `TF_LOG=TRACE` in CI Exposes Plaintext Credentials in Log Files

**Difficulty**: Medium
**Answer Type**: one
**Topic**: `TF_LOG=TRACE` captures all provider plugin activity including HTTP request headers and payloads — if combined with `TF_LOG_PATH`, plaintext credentials can be persisted to files in CI artifact storage; debug logging should be unset after debugging and log files purged

**Scenario**:
A DevOps engineer adds `TF_LOG=TRACE` and `TF_LOG_PATH=/tmp/terraform-debug.log` to a CI pipeline to debug an intermittent provider API issue. The fix is confirmed and the debugging variables are left in the pipeline for "future use." A security team audit two weeks later discovers that every CI run has been writing log files that contain the AWS secret access key in plaintext within provider HTTP request payloads.

**Question**:
What is the root cause of this credential exposure, and what should the engineer have done?

- A) `TF_LOG=TRACE` is a security vulnerability in the Terraform binary that always writes provider credentials to `/var/log/syslog` — it should never be used even locally
- B) `TRACE` level logging captures all provider plugin activity including HTTP request headers and response bodies. Provider API calls include authentication data (AWS Signature headers, tokens) that appear in plaintext in the trace output. After resolving the debugging issue, the engineer should have unset `TF_LOG` (or set it to `OFF`) and removed `TF_LOG_PATH`. Any log files stored in CI artifacts should be purged or treated as sensitive. Best practice is to use short-lived, scoped credentials for debug sessions so that any inadvertently logged credentials are already expired
- C) The exposure was caused by `TF_LOG_PATH` alone — without this variable, Terraform discards log output to `/dev/null`, making it safe to leave `TF_LOG=TRACE` permanently set in CI
- D) `TF_LOG=TRACE` only captures Terraform core operations and does not include provider plugin network traffic — the credential exposure was caused by a misconfigured provider independently logging its own authentication headers, unrelated to `TF_LOG`

### Question 92 — "Plan" Workspace Permission Cannot Trigger or Confirm Applies

**Difficulty**: Easy
**Answer Type**: one
**Topic**: HCP Terraform's "Plan" workspace permission allows triggering speculative plans only — applying a plan requires at minimum "Write" permission

**Scenario**:
A junior developer is onboarded to an HCP Terraform workspace with "Plan" access. They've been asked to deploy a bug fix and attempt to click "Confirm & Apply" on a completed plan in the HCP Terraform UI. The button is greyed out and they receive an authorization error.

**Question**:
What is the explanation?

- A) The workspace is in remote execution mode — only local execution mode allows users to confirm applies from the UI regardless of permission level
- B) The "Plan" permission in HCP Terraform allows a user to trigger speculative plans but does not grant the ability to queue, trigger, or confirm apply runs. Applying a run requires at minimum "Write" permission on the workspace
- C) The apply button is disabled because the run is in "plan pending review" status — any user including those with "Plan" permission can confirm applies once a teammate with "Admin" access approves the review gate
- D) CLI-only: applies can only be confirmed via `terraform apply` from the CLI — the HCP Terraform UI always requires Admin permission to confirm an apply regardless of other permission levels

### Question 93 — `terraform_remote_state` Reading a Sensitive Output from Another Workspace

**Difficulty**: Hard
**Answer Type**: many
**Topic**: `terraform_remote_state` can access outputs marked `sensitive = true` in the source workspace — the value is not encrypted or blocked from cross-workspace reads; the sensitivity marking propagates into the consuming workspace, where the value is redacted in plan/apply output

**Scenario**:
The `networking` workspace declares an output for a database password:

```hcl
output "db_password" {
  value     = random_password.db.result
  sensitive = true
}
```

The `compute` workspace reads it:

```hcl
data "terraform_remote_state" "networking" {
  backend = "remote"
  config = {
    organization = "my-org"
    workspaces = { name = "networking" }
  }
}

resource "aws_db_instance" "app" {
  password = data.terraform_remote_state.networking.outputs.db_password
}
```

**Question**:
Which TWO statements accurately describe the behaviour?

- A) `terraform_remote_state` cannot read outputs marked `sensitive = true` — the marking encrypts the value in the source workspace's state file and prevents cross-workspace access
- B) The `db_password` output value is accessible to the `compute` workspace via `terraform_remote_state` — `sensitive = true` in the `networking` workspace controls display suppression in the producing workspace's CLI output but does not encrypt or block the value in state
- C) In the `compute` workspace, `data.terraform_remote_state.networking.outputs.db_password` is treated as a sensitive value — it will be redacted in the compute workspace's plan and apply output because the sensitivity marking propagates from the producing workspace through the remote state data source into the consuming workspace
- D) Any resource in the `compute` workspace that references this value must also declare `sensitive = true` explicitly on the resource block — failing to do so causes an apply-time sensitivity violation error

### Question 94 — VCS Integration Only Triggers Runs on the Configured Branch

**Difficulty**: Medium
**Answer Type**: one
**Topic**: HCP Terraform VCS workspaces trigger plan-and-apply runs only on pushes to the configured trigger branch — direct pushes to feature branches do not trigger runs; speculative plans for feature branches are triggered by opening a pull request targeting the configured branch

**Scenario**:
A team connects their HCP Terraform workspace to a GitHub repository with `main` as the VCS trigger branch. A developer pushes commits modifying `.tf` files to a feature branch `feature/add-security-groups`. They wait for a run to appear in HCP Terraform but nothing triggers. The developer is confused — they expected at minimum a speculative plan to run for their feature branch.

**Question**:
Why did no run trigger, and when would a speculative plan appear?

- A) HCP Terraform triggers speculative plans on all branches by default — the missing run indicates the `.tf` changes were in a subdirectory that doesn't match the workspace's configured working directory
- B) HCP Terraform VCS workspaces only trigger runs based on the configured branch. A direct push to a feature branch triggers no run. A speculative plan is triggered when the developer **opens a pull request** targeting the configured branch (e.g., `feature/add-security-groups` → `main`) — the speculative plan is displayed in the PR. A push or merge to `main` triggers a plan-and-apply run
- C) Feature branch pushes trigger speculative plans only when the branch name matches a `branch_prefix_filter` pattern configured in the workspace — the run was not triggered because no prefix filter was configured
- D) GitHub must be configured to send a new webhook event each time a feature branch is created — without this one-time setup step per branch, HCP Terraform's webhook is unaware of commits to new branches

### Question 95 — Legacy CLI Import Succeeds But `terraform plan` Shows Replacement

**Difficulty**: Medium
**Answer Type**: one
**Topic**: `terraform import` only adds the resource to the state file — it does not update the configuration; when the resource block in `.tf` files is incomplete or incorrect, the next plan computes a diff and may show destructive changes to reconcile configuration against state

**Scenario**:
An engineer imports an existing RDS instance into Terraform management:

```bash
terraform import aws_db_instance.main myapp-rds-prod
```

The command succeeds. The only resource block in the configuration is:

```hcl
resource "aws_db_instance" "main" {
  identifier = "myapp-rds-prod"
  engine     = "mysql"
}
```

Running `terraform plan` immediately after produces:

```
aws_db_instance.main must be replaced
  ~ engine_version     = "8.0.36" -> null (forces replacement)
  ~ instance_class     = "db.t3.medium" -> null (forces replacement)
  ~ allocated_storage  = 100 -> null (forces replacement)
```

**Question**:
Why does Terraform plan a replacement immediately after a successful import?

- A) `terraform import` creates a pending-state entry that requires one additional `terraform apply` to finalize — the replacement is expected and will not destroy the actual RDS instance during this finalization apply
- B) `terraform import` only adds the resource to the state file with its actual attributes — it does not modify the `.tf` configuration. The resource block declares only `identifier` and `engine`, omitting required attributes (`engine_version`, `instance_class`, `allocated_storage`). Terraform plans to reconcile the sparse configuration against the state, and because these omitted attributes would be set to null or defaults, Terraform plans a replacement. The engineer must run `terraform state show aws_db_instance.main`, record all actual attributes, and update the configuration to fully match the existing instance before re-running `terraform plan`
- C) The replacement is triggered because `engine = "mysql"` without an explicit `engine_version` causes Terraform to interpret this as a request to replace the instance with the latest MySQL version
- D) The state lock from `terraform import` expires after 60 seconds — running `terraform plan` after the lock expires causes Terraform to lose the import context and plan a full replacement

### Question 96 — Soft-Mandatory Policy Failure: Which Roles Can Override

**Difficulty**: Medium
**Answer Type**: one
**Topic**: `soft-mandatory` Sentinel/OPA policy failures block a run but can be overridden by authorised users — workspace Admins and organisation Owners can override; users with only "Write" permission cannot

**Scenario**:
An HCP Terraform workspace has a Sentinel policy set attached with `enforcement_level = "soft-mandatory"`. The policy requires all EC2 instances to include a `CostCenter` tag. A plan runs for a change that adds two new EC2 instances without the required tag. The policy check fails and the run is blocked. A DevOps engineer with "Admin" workspace permission sees the failure in the HCP Terraform UI and wants to know if they can override it and proceed — the tag will be added in a follow-up PR.

**Question**:
Can the Admin user override the soft-mandatory policy failure and allow the run to proceed?

- A) No — `soft-mandatory` and `hard-mandatory` both block runs unconditionally; the only difference between them is the icon colour in the UI
- B) Yes — a workspace Admin can override a `soft-mandatory` policy failure by clicking "Override & Continue" in the HCP Terraform UI. The override is recorded in the audit trail. The team should remediate the underlying policy violation (add the `CostCenter` tag) in a follow-up change
- C) No — `soft-mandatory` policy failures can only be overridden by the HCP Terraform organisation Owner; workspace-level Admin cannot override policy failures regardless of workspace permission
- D) Yes — any user with at least "Write" workspace permission can override a `soft-mandatory` failure, because Write is sufficient to trigger and approve all run types

### Question 97 — Run Triggers Must Be Explicitly Configured — No Implicit Chaining

**Difficulty**: Easy
**Answer Type**: one
**Topic**: HCP Terraform workspace run triggers must be explicitly configured — workspaces do not automatically run when a workspace they depend on via `terraform_remote_state` completes an apply

**Scenario**:
A team manages `networking` and `compute` as separate HCP Terraform workspaces. The `compute` workspace reads VPC and subnet IDs from `networking` via `terraform_remote_state`. After successfully applying changes in `networking` (new subnet added), the team expects `compute` to automatically queue a run to pick up the new subnet ID. Nothing happens — `compute` never runs.

**Question**:
What is the explanation?

- A) HCP Terraform automatically queues a run in all workspaces that read from a workspace via `terraform_remote_state` when that workspace's state is updated — the missing trigger indicates a misconfigured `terraform_remote_state` data source
- B) Workspace run triggers must be **explicitly configured** in HCP Terraform — workspaces are independent by default regardless of state dependencies. To automatically queue a `compute` run after `networking` applies, the team must add `networking` as a configured Run Trigger source for the `compute` workspace in the HCP Terraform settings
- C) Run triggers only function between workspaces in the same HCP Terraform Project — workspaces in separate Projects cannot trigger each other
- D) Run triggers work in the reverse direction only — the consuming workspace (`compute`) must be configured to trigger the producing workspace (`networking`), not the other way around

### Question 98 — Cost Estimation Appears in HCP Terraform Run After Planning, Before Apply

**Difficulty**: Medium
**Answer Type**: one
**Topic**: HCP Terraform cost estimation runs after the plan phase completes and displays the projected monthly cost delta in the plan review UI — before the apply button is available — allowing teams to see cost impact before confirming the apply

**Scenario**:
A team is preparing to apply a Terraform plan that provisions five `m5.xlarge` EC2 instances across two availability zones. The engineering manager wants to see the projected monthly cost increase before anyone clicks "Confirm & Apply." The team lead assures the manager that HCP Terraform will display this automatically as part of the run.

**Question**:
At which point in the HCP Terraform run lifecycle does cost estimation appear, and what does it show?

- A) Cost estimation is a post-apply report — it appears in the workspace's "Cost Reports" section after the infrastructure is created and actual billing has begun
- B) Cost estimation runs after the plan phase and is displayed in the run's plan review UI — the same screen where a user would click "Confirm & Apply." It shows the projected monthly cost change (e.g., "+$972.00/month") broken down by resource, before any apply is triggered. The manager can review the cost impact before approving
- C) Cost estimation runs during `terraform plan` on the engineer's local machine when the `TF_VAR_cost_estimation=true` environment variable is set — the estimate appears in terminal output before the plan summary
- D) Cost estimation requires a separate API call after the plan completes — the team must query the HCP Terraform API endpoint `/runs/{run-id}/cost-estimate` to retrieve the data; it is not automatically displayed in the run UI

### Question 99 — Generated Config Must Be Reviewed Before Apply; Skipping Review Causes Destructive Plan

**Difficulty**: Hard
**Answer Type**: many
**Topic**: `terraform plan -generate-config-out` produces a starting-point configuration that may have incomplete or default attribute representations — it must be reviewed and adjusted before applying; failure to verify "No changes" after the import apply leads to destructive subsequent plans

**Scenario**:
A team imports an existing S3 bucket with a complex lifecycle configuration:

```hcl
import {
  to = aws_s3_bucket.assets
  id = "company-assets-prod-2019"
}
```

They run `terraform plan -generate-config-out=generated.tf`, which produces a `generated.tf` file. Without reviewing it, they immediately run `terraform apply`. The apply reports success. On the very next `terraform plan` they see:

```
aws_s3_bucket.assets must be replaced
  ~ force_destroy   = true -> null (forces replacement)
  ~ lifecycle_rule  = [<5 complex rules>] -> null
```

**Question**:
Which TWO statements accurately explain what happened and what the correct workflow requires?

- A) The generated configuration may have incomplete or incorrectly defaulted attribute representations that do not match the bucket's actual desired configuration. Running `terraform apply` without reviewing and adjusting `generated.tf` accepted a configuration that does not accurately describe the existing bucket — attributes missing from the generated file will appear as planned changes on the next plan
- B) `terraform plan -generate-config-out` produces a configuration guaranteed to be a complete and accurate representation of the resource. If the next plan shows changes, it means the S3 bucket was modified by another process between the import apply and the subsequent plan
- C) The import workflow requires a post-import verification step: run `terraform plan` after the import apply and confirm the output is "No changes. Your infrastructure matches the configuration." If any changes appear, the generated configuration must be adjusted to match the actual resource attributes before proceeding
- D) The `lifecycle_rule` and `force_destroy` attributes disappeared because Terraform automatically strips lifecycle-sensitive attributes from generated configs during the apply phase as a safety mechanism

### Question 100 — Two Configurations Sharing the Same HCP Terraform Workspace Causes State Collision

**Difficulty**: Hard
**Answer Type**: many
**Topic**: Each HCP Terraform workspace maintains exactly one state file — two Terraform configurations pointing to the same workspace overwrite each other's state on every apply; the correct architecture is one workspace per environment with variable sets for shared configuration

**Scenario**:
A team manages production and staging environments. Both environment configurations have identical `cloud` blocks:

```hcl
terraform {
  cloud {
    organization = "my-org"
    workspaces {
      name = "app-shared"
    }
  }
}
```

A staging apply runs and creates five test EC2 instances. The next production plan shows those five test instances as already existing (no planned creation), and the production-exclusive resources — a load balancer and three security groups — are missing from state and shown as "to be created."

**Question**:
Which TWO statements accurately explain what happened and the correct architectural fix?

- A) Each HCP Terraform workspace holds a single state file. Both configurations target `app-shared`, so they share the same state. The staging apply wrote a new state version containing only the five test EC2 instances and overwrote the previous state, which contained the production load balancer and security groups. Production's infrastructure now exists in AWS but is absent from state
- B) HCP Terraform merges state from multiple configurations into a single workspace — this is expected shared-workspace behaviour and is safe as long as resource names do not collide
- C) The correct architecture is one dedicated workspace per environment — `app-production` and `app-staging`. Each workspace maintains independent state, run history, variables, and access permissions. For configuration that must be shared across workspaces (such as provider credentials or common tags), variable sets are the appropriate mechanism
- D) The collision is caused by the missing `prefix` argument in the `cloud` block — setting `prefix = "prod-"` and `prefix = "staging-"` in the respective configurations would allow them to coexist safely within the same `app-shared` workspace by namespacing their state

### Question 101 — `terraform show -json` for Machine-Readable State in Scripts

**Difficulty**: Easy
**Answer Type**: one
**Topic**: `terraform show -json` outputs the full current state as structured JSON for programmatic consumption — it is the correct interface for scripts and tooling that need to inspect resource attributes without parsing human-readable text

**Scenario**:
A platform team builds an internal automation tool that reads Terraform-managed EC2 instance public IPs and registers them in an internal DNS system. A junior engineer proposes calling `terraform state list` to get all resource addresses and then calling `terraform state show <address>` for each one, parsing the human-readable output with regex. A senior engineer recommends a single command instead.

**Question**:
Which command is correct for this use case, and why?

- A) `terraform state list` followed by `terraform state show` for each resource — this provides the most complete human-readable output and regex parsing is standard practice for infrastructure automation scripts
- B) `terraform show -json` — this outputs the full current state as a structured JSON document. A script can parse it with standard JSON libraries to locate all `aws_instance` resources and extract `public_ip` attributes in a single invocation, without shell-parsing human-readable text or invoking multiple commands
- C) `terraform output -json` — this outputs all declared Terraform outputs as JSON, which provides complete access to all resource attributes including those not explicitly declared as outputs
- D) `terraform state pull` — this downloads the raw backend state JSON, which is the most complete and portable machine-readable representation of all resource attributes and is the recommended interface for automation tooling



## Answer Key

| Q# | Answer(s) | Explanation | Source | Difficulty |
|---|---|---|---|---|
| 2 | B | N/A | Idempotency — "No changes" as expected and correct behaviour | Easy |
| 3 | A | N/A | IaC as living documentation of infrastructure | Easy |
| 4 | C | N/A | Terraform enforces desired state — manual out-of-band changes are reverted on next apply | Medium |
| 5 | B | N/A | CloudFormation is AWS-only; Terraform provides multi-cloud support | Medium |
| 6 | B | N/A | Disaster recovery using IaC — restoring infrastructure from configuration and state backup | Medium |
| 7 | A | N/A | Idempotency contrast — imperative scripting vs declarative Terraform | Medium |
| 8 | A, C | N/A | Infrastructure drift and repeatability — restoring environment parity via Terraform apply | Medium |
| 9 | B | N/A | IaC audit trail — Git commit history and pull request records as compliance evidence | Medium |
| 10 | A, C | N/A | Provisioning tools vs configuration management tools — Terraform and Ansible in a full-stack workflow | Medium |
| 11 | B | N/A | Desired state vs current state — Terraform computes the minimal change set | Medium |
| 12 | B | N/A | Terraform's declarative model — engineers declare desired end state, not execution steps | Hard |
| 13 | A, C | N/A | Drift detection without making changes — `terraform plan` and `terraform plan -refresh-only` | Hard |
| 14 | B | N/A | Provider validates resource configuration against a schema before contacting the cloud API | Easy |
| 15 | C | N/A | Provider aliases required when multiple configurations of the same provider type are needed | Medium |
| 16 | A, C | N/A | `sensitive = true` masks terminal output only; state stores data in plaintext; backend encryption required for at-rest protection | Hard |
| 17 | C | N/A | State locking prevents concurrent applies and protects state integrity | Easy |
| 18 | B | N/A | `terraform state mv` moves a resource's state entry to a new address, preventing destroy+recreate on rename | Medium |
| 19 | B | N/A | `>=` has no upper bound; `~>` restricts updates to a specific major or minor series | Medium |
| 20 | A, C | N/A | `.tfstate.backup` is a single pre-apply snapshot; partial applies create resources unknown to the backup | Hard |
| 21 | C | N/A | `terraform state list` outputs all resource addresses currently tracked in state | Easy |
| 22 | C | N/A | `terraform init -migrate-state` performs backend state migration non-interactively | Medium |
| 23 | A, C | N/A | Partner providers are maintained by technology partners with HashiCorp review; different from Official and Community tiers | Medium |
| 24 | B | N/A | `~> 1.5.0` restricts to patch updates within the 1.5.x series; Terraform v1.8.0 is outside this range | Medium |
| 25 | B | N/A | Providers run as separate OS processes via gRPC; provider crash is isolated from Terraform Core | Hard |
| 26 | B | N/A | `terraform state rm` removes a resource from state management without deleting the cloud resource | Medium |
| 27 | C | N/A | `terraform init` must be re-run when a new provider is added to `required_providers` | Easy |
| 28 | B | N/A | `terraform plan -out` + `terraform apply <planfile>` guarantees deterministic apply of the reviewed plan | Medium |
| 29 | B | N/A | `terraform fmt -check` exits with code 1 when files need reformatting — used in CI without writing files | Easy |
| 30 | C | N/A | `terraform apply -replace` forces destroy+recreate of a specific resource without changing configuration | Medium |
| 31 | B | N/A | `terraform graph` outputs DOT format; Graphviz (`dot`) is required to render it as an image | Medium |
| 32 | B | N/A | `terraform output -raw` produces unquoted string values suitable for shell variable assignment | Easy |
| 33 | A, C | N/A | `terraform plan -refresh=false` skips live API queries; trades freshness for speed in trusted environments | Medium |
| 34 | B | N/A | `terraform validate` checks static config only; `terraform plan` catches live resource issues like invalid AMIs | Medium |
| 35 | B | N/A | `terraform workspace show` displays the currently active workspace — critical safety check before destructive operations | Medium |
| 36 | C | N/A | `terraform console` lets developers interactively evaluate HCL expressions and functions before embedding them in configuration | Medium |
| 37 | B | N/A | Applying a saved plan file skips re-planning and interactive confirmation; changes between plan and apply cannot slip through | Hard |
| 38 | A, C | N/A | `terraform apply -target` applies only to the specified resource; known risks include partial state and dependency gaps | Hard |
| 39 | B | N/A | `terraform plan -destroy` is a read-only preview; `terraform destroy` actually destroys resources | Hard |
| 40 | B | N/A | `create_before_destroy = true` reverses replacement order to avoid downtime when a resource must be replaced | Medium |
| 41 | B | N/A | `ignore_changes` suppresses drift detection for specified attributes managed outside Terraform | Medium |
| 42 | C | N/A | `for_each` requires a `map` or `set(string)`; a `list(string)` must be converted with `toset()` | Easy |
| 43 | A | N/A | `removed` block with `lifecycle { destroy = false }` stops Terraform managing a resource without deleting it | Medium |
| 44 | B | N/A | `moved` block with `to = module.<name>.<type>.<name>` relocates a resource's state entry to a module address | Medium |
| 45 | B | N/A | `depends_on` required for IAM policy attachments because no attribute reference exists between the IAM resource and the consuming resource | Medium |
| 46 | B | N/A | Data sources whose arguments contain computed (unknown-until-apply) values are deferred and read during `apply`, not `plan` | Hard |
| 47 | C | N/A | `replace_triggered_by` forces the dependent resource to be replaced when a referenced upstream resource changes | Medium |
| 48 | A, D | N/A | `prevent_destroy = true` causes `terraform apply` and `terraform destroy` to error; must be removed from config before destroying | Medium |
| 49 | B | N/A | Removing an element from the middle of a `count`-indexed list causes all subsequent instances to shift indices and be replaced | Hard |
| 50 | B | N/A | Circular dependencies (cycles) in the resource graph cause Terraform to error; resolution requires restructuring references or using `data` sources | Hard |
| 51 | A, C | N/A | Data sources depending on newly created resources are deferred to apply phase; plan output shows `(known after apply)` for data source results | Hard |
| 52 | B | N/A | The `provider` meta-argument on a resource selects an aliased provider configuration for that specific resource | Easy |
| 53 | B | N/A | `variable` validation `condition` can only reference `var.<name>` — referencing data sources, locals, or other resources causes an error at parse time | Medium |
| 54 | A, D | N/A | `sensitive = true` on an output masks the value in CLI output but the value remains in plaintext in `terraform.tfstate` — protecting state requires an encrypted remote backend | Medium |
| 55 | B | N/A | CLI `-var` flag takes the highest precedence over all other variable input sources, including `*.auto.tfvars` files | Easy |
| 56 | B | N/A | `jsonencode()` converts a Terraform HCL object/map/list to its JSON string representation — commonly used for inline IAM policies and ECS task definitions to avoid a separate `aws_iam_policy_document` data source | Medium |
| 57 | B | N/A | When `iterator = <name>` is set in a `dynamic` block, the `content` block must use `<name>.value.*` instead of the default block-type name | Medium |
| 58 | B | N/A | `local.*` values are internal computed values that centralise reusable expressions within a module — they are not module interface inputs and cannot be overridden by callers | Easy |
| 59 | B | N/A | A `for` expression enclosed in `[...]` produces a `list`; enclosing in `{...}` with `key => value` syntax produces a `map` — the outer delimiters determine the output type | Medium |
| 60 | C | N/A | `cidrsubnet(prefix, newbits, netnum)` — `newbits` is additional bits borrowed from the host portion to extend prefix length; `netnum` is zero-based subnet index; `cidrsubnet("10.0.0.0/16", 8, N)` produces a `/24` subnet | Hard |
| 61 | A, C | N/A | `flatten()` recursively unwraps a list-of-lists into a single flat list, preserving order without deduplicating; it differs from `concat()` which joins multiple separate flat lists | Hard |
| 62 | C | N/A | `nullable = false` prevents callers from explicitly passing `null` to override a variable's default — Terraform errors even if a `default` is defined; by contrast the default `nullable = true` permits explicit null overrides | Medium |
| 63 | B | N/A | `try(expr, fallback)` returns the fallback value when the primary expression raises a Terraform evaluation error — the idiomatic pattern for optional map keys that may not be present | Medium |
| 64 | A, C | N/A | `for_each` with a map creates resource instances addressed by string key in state; adding or removing an individual key only creates or destroys that specific instance without affecting others | Hard |
| 65 | C | N/A | `terraform output -raw <name>` prints the raw string value without surrounding double quotes — required for clean shell variable assignment in CI scripts | Easy |
| 66 | B | N/A | `check` block assertion failures emit a warning and do not set a non-zero exit code — a failing `check` block never prevents `terraform apply` from completing successfully | Medium |
| 67 | A, C | N/A | A failing `precondition` prevents the resource change from occurring — the resource is left in its previous state (unchanged or non-existent); the apply fails before the provider makes any API call for that resource | Medium |
| 68 | B | N/A | `self` is only valid inside `postcondition` blocks, where it references the resource's attributes after the change has been applied — `self` is not available in `precondition` blocks | Easy |
| 69 | A, C | N/A | `sensitive = true` only masks terminal output — the value is still written as plaintext to `terraform.tfstate`; protecting state requires an encrypted remote backend and strict access controls | Hard |
| 70 | B | N/A | When a variable has multiple `validation` blocks, all blocks are evaluated independently and all failures are reported simultaneously — not just the first one | Medium |
| 71 | B | N/A | A failing scoped `data` source inside a `check` block generates a warning (not an error) and does not abort the plan or apply — unlike top-level `data` source failures which abort the plan | Medium |
| 72 | B | N/A | `precondition` and `postcondition` blocks can reference any in-scope value — data sources, locals, module outputs, other resource attributes — unlike `validation` blocks which are restricted to `var.<name>` only | Hard |
| 73 | A | N/A | Terraform raises an error during plan when an output block references a sensitive value (variable, local, or resource attribute) without marking the output block itself as `sensitive = true` | Easy |
| 74 | B | N/A | `nonsensitive()` explicitly removes the sensitive marking from a value, allowing it to appear in plaintext in outputs or expressions — the author takes responsibility for the security implications | Medium |
| 75 | A, D | N/A | HashiCorp Vault dynamic secrets prevent static secret storage in state and configuration entirely; `sensitive = true` only masks terminal output but leaves the secret in plaintext state — these are complementary but distinct controls | Hard |
| 76 | B | N/A | `terraform validate` checks HCL syntax and provider schema correctness — it does not execute variable validation blocks because it does not require variable values to be provided | Medium |
| 77 | B | N/A | A failing `postcondition` means the resource was already created (or changed) by the provider — it exists in AWS and is recorded in state, but the apply is marked as failed | Easy |
| 78 | B | N/A | A Terraform Registry module source without a `version` constraint causes `terraform init` to always download the latest available version — a future major release with breaking changes will silently break the configuration | Medium |
| 79 | B, C | N/A | The `providers` meta-argument on a module block maps provider aliases from the root module to the provider names expected by the child module — without it, child modules always use the default (non-aliased) provider configuration | Hard |
| 80 | B | N/A | Terraform tracks all resources inside a child module under the module's label in state — renaming `module "network"` to `module "networking"` changes every resource's state address, causing Terraform to plan destroying all old-address resources and creating all new-address resources | Medium |
| 81 | B | N/A | `terraform init` without flags reuses a cached module version if it satisfies the constraint — to download a newer compatible version within the allowed range, `terraform init -upgrade` is required | Medium |
| 82 | B | N/A | Child module outputs must be explicitly declared with an `output` block — referencing `module.<name>.<value>` from the root module when no matching `output` block exists in the child causes an error at plan time | Easy |
| 83 | A, C | N/A | A `for_each` module block keyed by a map creates one module instance per map entry addressed by string key in state — adding a new key creates only that new instance; existing instances are unaffected | Hard |
| 84 | B | N/A | `terraform plan -refresh-only` shows drift between recorded state and live cloud state without producing a plan to modify infrastructure; `terraform apply -refresh-only` accepts the drift by updating state — only `-refresh-only` plan is read-only | Easy |
| 85 | B | N/A | `terraform init -migrate-state` copies state to the new backend but leaves the old `terraform.tfstate` file in the working directory — Terraform stops reading from the local file but does not delete it | Easy |
| 86 | B | N/A | `terraform state rm` removes a resource's state entry — the actual cloud resource is unaffected, but if the resource block remains in configuration, the next `terraform plan` treats it as a new resource to create | Medium |
| 87 | C | N/A | `terraform force-unlock <LOCK_ID>` manually releases a stale DynamoDB lock — it should only be used when certain no other Terraform operation is running, because it removes the lock regardless of whether a real concurrent process holds it | Medium |
| 88 | A, C | N/A | The S3 backend without a `dynamodb_table` has no locking mechanism — concurrent `terraform apply` operations can both read, modify, and write state simultaneously, causing state corruption and orphaned resources | Hard |
| 89 | B | N/A | `terraform state push` overwrites remote state with the provided local file with no safety confirmation prompt — pushing an older state file loses all resource records added since that snapshot was taken | Medium |
| 90 | B | N/A | `terraform state mv <source> <destination>` changes the resource's address in the state file without making any API calls or modifying the actual cloud resource — after the move, `terraform plan` sees no difference between the new configuration address and the updated state address | Medium |
| 91 | B | N/A | When the target resource uses `for_each`, the `import` block's `to` argument must include the specific instance key in square bracket notation — `resource_type.name["key"]` — the same syntax used in plan output and state addresses | Medium |
| 92 | B | N/A | `TF_LOG=TRACE` captures all provider plugin activity including HTTP request headers and payloads — if combined with `TF_LOG_PATH`, plaintext credentials can be persisted to files in CI artifact storage; debug logging should be unset after debugging and log files purged | Medium |
| 93 | B | N/A | HCP Terraform's "Plan" workspace permission allows triggering speculative plans only — applying a plan requires at minimum "Write" permission | Easy |
| 94 | B, C | N/A | `terraform_remote_state` can access outputs marked `sensitive = true` in the source workspace — the value is not encrypted or blocked from cross-workspace reads; the sensitivity marking propagates into the consuming workspace, where the value is redacted in plan/apply output | Hard |
| 95 | B | N/A | HCP Terraform VCS workspaces trigger plan-and-apply runs only on pushes to the configured trigger branch — direct pushes to feature branches do not trigger runs; speculative plans for feature branches are triggered by opening a pull request targeting the configured branch | Medium |
| 96 | B | N/A | `terraform import` only adds the resource to the state file — it does not update the configuration; when the resource block in `.tf` files is incomplete or incorrect, the next plan computes a diff and may show destructive changes to reconcile configuration against state | Medium |
| 97 | B | N/A | `soft-mandatory` Sentinel/OPA policy failures block a run but can be overridden by authorised users — workspace Admins and organisation Owners can override; users with only "Write" permission cannot | Medium |
| 98 | B | N/A | HCP Terraform workspace run triggers must be explicitly configured — workspaces do not automatically run when a workspace they depend on via `terraform_remote_state` completes an apply | Easy |
| 99 | B | N/A | HCP Terraform cost estimation runs after the plan phase completes and displays the projected monthly cost delta in the plan review UI — before the apply button is available — allowing teams to see cost impact before confirming the apply | Medium |
| 100 | A, C | N/A | `terraform plan -generate-config-out` produces a starting-point configuration that may have incomplete or default attribute representations — it must be reviewed and adjusted before applying; failure to verify "No changes" after the import apply leads to destructive subsequent plans | Hard |
| 101 | A, C | N/A | Each HCP Terraform workspace maintains exactly one state file — two Terraform configurations pointing to the same workspace overwrite each other's state on every apply; the correct architecture is one workspace per environment with variable sets for shared configuration | Hard |
| 102 | B | N/A | `terraform show -json` outputs the full current state as structured JSON for programmatic consumption — it is the correct interface for scripts and tooling that need to inspect resource attributes without parsing human-readable text | Easy |
