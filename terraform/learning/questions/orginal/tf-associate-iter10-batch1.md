# Terraform Associate (004) — Question Bank Iter 10 Batch 1

**Iteration**: 10
**Iteration Style**: Exam-style scenarios — multi-sentence real-world context questions
**Batch**: 1
**Objective**: 1 — IaC Concepts
**Generated**: 2026-04-26
**Total Questions**: 12
**Difficulty Split**: 2 Easy / 8 Medium / 2 Hard
**Answer Types**: 9 `one` / 3 `many` / 0 `none`

---

## Questions

---

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

**Answer**: B

**Explanation**:
"No changes. Infrastructure is up-to-date." is the correct idempotent behaviour of Terraform — it means the actual cloud resources already match the desired state expressed in the `.tf` configuration files, so no actions are required. This is a feature, not a malfunction. Terraform re-evaluates state on every run, and if nothing has drifted, it correctly takes no action.

---

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

**Answer**: A

**Explanation**:
One of the named benefits of IaC is that configuration files act as living documentation — they describe exactly what infrastructure exists, how it is configured, and how resources relate to each other. Because the files are version-controlled and the actual cloud state is reconciled to match them, they represent an authoritative and up-to-date description of the system. No separate document is needed.

---

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

**Answer**: C

**Explanation**:
Terraform enforces the desired state declared in the configuration files. The configuration still declares `min_size = 2`, and Terraform's state file still reflects that. When `apply` runs, Terraform refreshes the actual cloud state, detects the divergence (`min_size = 5` in AWS vs. `min_size = 2` in the config), and plans a change to revert it to `2`. Manual console changes are overwritten on the next `apply` unless the configuration is updated to reflect the new desired state.

---

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

**Answer**: B

**Explanation**:
AWS CloudFormation is an AWS-proprietary IaC tool. It has no capability to provision or manage resources in GCP or Azure. For multi-cloud infrastructure management from a single workflow, the team would need a provider-agnostic tool such as Terraform, which supports all three major cloud providers (and many others) through installable provider plugins. This is one of Terraform's primary advantages over provider-specific tools like CloudFormation, Azure Bicep, and Google Cloud Deployment Manager.

---

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

**Answer**: B

**Explanation**:
This scenario demonstrates the disaster recovery benefit of IaC. Restoring the state backup first is important — it gives Terraform accurate resource address tracking, which avoids duplicate resource creation and ensures correct dependency ordering. After the state is restored, `terraform apply` compares the desired state (the Git-stored configuration) with the now-empty current state and plans the creation of all 47 resources. Running `apply` without a state file (option C) is possible but risks resource orphaning and address conflicts for resources with existing identifiers.

---

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

**Answer**: A

**Explanation**:
Imperative shell scripts using `aws ec2 run-instances` are not idempotent — each execution issues new API calls to create additional resources regardless of what already exists. Terraform, as a declarative tool, compares the desired state (`count = 3`) to the current state (3 instances already running), finds no difference, and makes no changes. This idempotency is a fundamental advantage of Terraform's declarative model over imperative scripting approaches.

---

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

**Answer**: A, C

**Explanation**:
**(A)** is correct — staging has drifted because team members bypassed Terraform and made manual out-of-band changes through the console, causing the actual state to diverge from the Terraform-defined desired state. **(C)** is correct — running `terraform apply` with the shared configuration will reconcile staging back to the desired state, demonstrating IaC's repeatability benefit. **(B)** is incorrect because production shows no drift since it was managed exclusively through Terraform. **(D)** is incorrect — `terraform taint` (deprecated; replaced by `-replace`) is unnecessary here; a standard `apply` is sufficient to correct drift.

---

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

**Answer**: B

**Explanation**:
The Git commit history and the associated pull request record together provide a complete audit trail: the PR review approval shows who authorized the change, the commit author shows who made it, and the diff shown in the PR or commit shows exactly what changed (before and after). This is the audit trail benefit of managing infrastructure as code in version control — every change is a reviewable, attributable commit. The state file captures current state, not history. CloudTrail captures API calls but not authorization intent or structured configuration diffs.

---

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

**Answer**: A, C

**Explanation**:
**(A)** is correct — Terraform is a provisioning tool designed to create and manage cloud infrastructure resources such as VMs, networks, databases, and load balancers across cloud providers. **(C)** is correct — Ansible is a configuration management tool designed to install software, manage configuration files, and set up application environments on existing servers after they are provisioned. These two tools represent complementary layers of a full infrastructure automation stack. **(B)** is incorrect — CloudFormation is also a provisioning tool (AWS-only) and has no capability for in-guest software configuration. **(D)** is incorrect — Chef is a configuration management tool focused on software configuration, not cloud resource provisioning.

---

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

**Answer**: B

**Explanation**:
Terraform reconciles the current state with the desired state by computing the minimal diff. The current state has 3 instances; the desired state requires 5. Therefore, Terraform plans to add exactly 2 new instances without touching the 3 that already exist and match their configuration. This minimal-change reconciliation is a core property of Terraform's declarative model — it never destroys and recreates resources unnecessarily, nor does it ignore existing resources.

---

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

**Answer**: B

**Explanation**:
Terraform is a declarative tool. Engineers declare *what* infrastructure should exist (the desired end state) in HCL, not the procedural steps to create it. Terraform analyzes attribute references between resources to build a dependency graph, then uses that graph to determine creation order — often executing independent resources in parallel. This is the fundamental distinction between declarative IaC (Terraform) and imperative scripting (Bash scripts, sequential Ansible tasks). The senior developer has conflated Terraform's configuration model with step-by-step imperative scripting.

---

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

**Answer**: A, C

**Explanation**:
**(A)** is correct — `terraform plan` performs a read-only comparison between the current cloud state (refreshed live) and the desired configuration, showing any proposed changes without executing them. It is safe to run in production at any time. **(C)** is correct — `terraform plan -refresh-only` (introduced in Terraform 0.15.4) specifically focuses on detecting the difference between the state file and actual infrastructure without proposing configuration-driven changes; it is the targeted command for drift auditing. **(B)** is incorrect and dangerous — `apply -auto-approve` immediately makes real infrastructure changes without human review, which is unsafe for production and violates the security team's constraint. **(D)** is incorrect — deleting the state file causes Terraform to lose all resource tracking, which would result in duplicate resource creation or errors on the next apply.

---
