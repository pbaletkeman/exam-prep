---
# Merged Metadata (Iteration 1)

## Batch 1 Metadata
**Difficulty**: Easy
**Answer Type**: one
**Topic**: Desired state and current state concepts

## Batch 2 Metadata
**Difficulty**: Easy
**Answer Type**: one
**Topic**: Provider tier classification

## Batch 3 Metadata
**Difficulty**: Easy
**Answer Type**: one
**Topic**: What `terraform init` does

## Batch 4 Metadata
**Difficulty**: Easy
**Answer Type**: one
**Topic**: What a data source does

## Batch 5 Metadata
**Difficulty**: Medium
**Answer Type**: one
**Topic**: Effect of `sensitive = true` on variables vs state

## Batch 6 Metadata
**Difficulty**: Medium
**Answer Type**: many
**Topic**: Which source types are valid for the `source` argument in a module block

## Batch 7 Metadata
**Difficulty**: Easy
**Answer Type**: one
**Topic**: When variable `validation` blocks are evaluated

## Batch 8 Metadata
**Difficulty**: Easy
**Answer Type**: one
**Topic**: Required arguments in an `import` block

---
# Questions (Iteration 1)

## Batch 1
### Question 1 — Desired State
In the context of Terraform, what does "desired state" refer to?
- A) The actual infrastructure resources that exist in the cloud provider right now
- B) The previous version of infrastructure before the last `terraform apply`
- C) What your `.tf` configuration files say the infrastructure should look like
- D) The contents of the `terraform.tfstate` file after the last successful apply
**Answer**: C

### Question 2 — Idempotency
A Terraform configuration that creates three EC2 instances is applied successfully. An operator runs `terraform apply` a second time against the same unchanged configuration. What is the expected result?
- A) Terraform creates three additional EC2 instances, resulting in six total
- B) Terraform destroys the existing instances and recreates them
- C) Terraform reports that no changes are needed and makes no modifications
- D) Terraform returns an error because the resources already exist
**Answer**: C

### Question 3 — Declarative vs Imperative
Which statement correctly describes the declarative approach used by Terraform?
- A) You write step-by-step instructions telling Terraform exactly how to create each resource
- B) You describe the desired end state of your infrastructure and Terraform determines the steps required to reach it
- C) You provide Terraform with shell scripts that it executes in order on the target cloud provider
- D) You specify only the resources to delete; Terraform infers what should be created from provider defaults
**Answer**: B

### Question 4 — IaC Benefits
Which TWO of the following are recognized benefits of managing infrastructure with IaC tools like Terraform? (Select two.)
- A) Infrastructure changes require no code review since they are applied automatically
- B) Every infrastructure change is captured as a version-controlled commit, providing a full audit trail
- C) Provider-specific web consoles become unnecessary and are disabled by the IaC tool
- D) Identical environments can be reproduced reliably from the same configuration code
**Answer**: B, D

### Question 5 — Multi-Cloud Support
Which of the following best describes Terraform's approach to managing resources across multiple cloud providers?
- A) Terraform requires a separate state file and CLI installation for each cloud provider
- B) Terraform can manage resources across AWS, Azure, GCP, and other providers within a single workflow using provider plugins
- C) Terraform delegates cross-cloud provisioning to AWS CloudFormation, which acts as a broker
- D) Terraform supports only one cloud provider per workspace; multi-cloud requires separate root modules that cannot share state
**Answer**: B

### Question 6 — IaC Tooling Landscape
An operator wants to provision infrastructure on both AWS and Azure from a single set of configuration files. Which tool is best suited for this requirement?
- A) AWS CloudFormation
- B) Azure Resource Manager (ARM) templates
- C) Terraform
- D) Google Cloud Deployment Manager
**Answer**: C

### Question 7 — Drift Detection
What is "infrastructure drift" in the context of IaC?
- A) The gradual increase in cost of cloud resources over time
- B) A discrepancy between the infrastructure described in configuration files and the actual infrastructure that exists in the cloud
- C) The latency introduced when Terraform communicates with a remote cloud API
- D) A versioning conflict between two different Terraform providers
**Answer**: B

### Question 8 — IaC vs Manual Provisioning
Which TWO of the following are drawbacks of manually provisioning infrastructure through a cloud provider's web console instead of using IaC? (Select two.)
- A) Web consoles require a paid subscription that IaC tools eliminate
- B) Manual changes leave no automatic version-controlled audit trail of who changed what and when
- C) Manually provisioned environments are difficult to reproduce identically, leading to environment inconsistencies
- D) Web consoles do not support creating virtual machines or networking resources
**Answer**: B, C

### Question 9 — Declarative vs Imperative Tools
A team currently uses Ansible playbooks to configure servers step by step and is evaluating Terraform as an addition to their toolchain. Which statement correctly describes how the two tools differ in their primary approach?
- A) Ansible is declarative; Terraform is imperative
- B) Both Ansible and Terraform are declarative; they differ only in the cloud providers they support
- C) Ansible playbooks are primarily imperative — specifying steps to execute; Terraform is declarative — specifying the desired end state
- D) Terraform is imperative for resource creation but declarative for resource deletion
**Answer**: C

### Question 10 — IaC and Disaster Recovery
A production environment is completely lost due to a datacenter failure. The team has their Terraform configuration files and a backup of the Terraform state stored in a remote backend. Which statement best describes how IaC helps in this scenario?
- A) IaC cannot help because the cloud resources themselves are gone and must be rebuilt manually
- B) The team can run `terraform apply` using the existing configuration to recreate the entire environment reproducibly, with the state backup used to avoid recreating already-restored resources
- C) The team must first run `terraform import` for every resource before any apply can proceed
- D) IaC helps only if the same Terraform version that created the original infrastructure is installed
**Answer**: B

### Question 11 — IaC Audit Trail
Which TWO of the following capabilities does storing Terraform configuration in a version control system (such as Git) provide? (Select two.)
- A) Automatic application of infrastructure changes whenever a commit is pushed, without any additional tooling
- B) A historical record of every infrastructure change, including who made it and when
- C) The ability to review proposed infrastructure changes through pull requests before they are applied
- D) Real-time synchronization of cloud resources with the repository without needing `terraform apply`
**Answer**: B, C

---
## Batch 2
[Batch 2 questions go here]

---
## Batch 3
[Batch 3 questions go here]

---
## Batch 4
[Batch 4 questions go here]

---
## Batch 5
[Batch 5 questions go here]

---
## Batch 6
[Batch 6 questions go here]

---
## Batch 7
[Batch 7 questions go here]

---
## Batch 8
[Batch 8 questions go here]

---
