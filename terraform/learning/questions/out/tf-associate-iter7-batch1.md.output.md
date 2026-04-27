# Terraform Associate Exam Questions

---

### Question 1 — IaC Benefit Name for Identical Environments

**Difficulty**: Easy
**Answer Type**: one
**Topic**: Repeatability — the IaC benefit that guarantees the same code deploys identical environments across staging and production

**Question**:
Complete the following statement by selecting the term that fills the blank:

> "Running the same Terraform configuration in the staging and production environments guarantees identical infrastructure. This IaC benefit is called ___________."

- A) Atomicity
- B) Convergence
- C) Modularity
- D) **Repeatability**

---

### Question 2 — `instance_type` Argument in an EC2 Resource Block

**Difficulty**: Easy
**Answer Type**: one
**Topic**: Completing a basic `aws_instance` resource block — the argument that specifies the EC2 instance type

**Question**:
A developer is writing their first Terraform resource block and leaves one argument name incomplete:

```hcl
resource "aws_instance" "web" {
  ami           = "ami-0abcd1234"
  ___________   = "t3.micro"
}
```

What argument name fills the blank to specify the EC2 instance size?

- A) `machine_type`
- B) `instance_size`
- C) **`instance_type`**
- D) `type`

---

### Question 3 — "Desired" End State in Declarative IaC

**Difficulty**: Easy
**Answer Type**: one
**Topic**: Completing the definition of declarative IaC — configurations express the desired end state

**Question**:
Complete the following statement:

> "Terraform configurations describe the ___________ end state of infrastructure. The tool determines what steps are necessary to reach that state, whether that means creating, modifying, or destroying resources."

- A) procedural
- B) scripted
- C) **desired**
- D) imperative

---

### Question 4 — `count = 0` to Conditionally Disable a Resource

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Using `count = 0` to declare that no instances of a resource should exist, while keeping the block in configuration

**Question**:
An engineer wants the bastion host resource block to remain in the configuration file for documentation purposes, but needs to ensure **no instances are created in the current environment**. Complete the resource block:

```hcl
resource "aws_instance" "bastion" {
  ami           = "ami-0abc1234"
  instance_type = "t3.nano"
  count         = ___________
}
```

What value fills the blank?

- A) `null`
- B) `false`
- C) `"disabled"`
- D) **`0`**

---

### Question 5 — "Drift" — Infrastructure Deviation From Desired State

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Completing the definition of infrastructure drift — when actual cloud resources diverge from the Terraform configuration

**Question**:
Complete the following statement:

> "When a cloud engineer manually modifies an EC2 instance's security group through the AWS Console — without updating the Terraform configuration — the actual state of that resource diverges from what the `.tf` files describe. This divergence is called infrastructure ___________."

- A) contamination
- B) corruption
- C) divergence
- D) **drift**

---

### Question 6 — "Audit Trail" Benefit of Version-Controlled IaC

**Difficulty**: Medium
**Answer Type**: one
**Topic**: The IaC benefit that provides a historical record of every infrastructure change via version control commits

**Question**:
Complete the following statement:

> "When infrastructure configuration files are stored in a version control system such as Git, every infrastructure change is captured as a commit — recording who made the change, when, and what was modified. This gives teams a complete ___________ of infrastructure changes."

- A) Terraform plan output
- B) `terraform.tfstate.backup`
- C) speculative plan history
- D) **audit trail**

---

### Question 7 — TWO Provisioning Tools in the IaC Landscape

**Difficulty**: Medium
**Answer Type**: many
**Topic**: Distinguishing provisioning tools (Terraform category) from configuration management tools — CloudFormation and Pulumi are provisioning tools

**Question**:
An engineer is building a comparison table of IaC tools with a "Provisioning" vs "Configuration Management" category column. Terraform belongs in the **Provisioning** category. Which TWO other tools from the list below also belong in the **Provisioning** category? (Select two.)

- A) Ansible
- B) **AWS CloudFormation**
- C) Chef
- D) **Pulumi**

---

### Question 8 — "Documentation" Benefit of IaC Configuration Files

**Difficulty**: Medium
**Answer Type**: one
**Topic**: IaC configuration files serve as living documentation of infrastructure

**Question**:
Complete the following statement from Terraform's IaC benefits:

> "Unlike a ClickOps environment where the exact infrastructure setup exists only in someone's memory or informal runbooks, IaC configuration files serve as living ___________ of what has been provisioned — always up to date because they are the authoritative source used to apply infrastructure."

- A) backups
- B) **documentation**
- C) snapshots
- D) manifests

---

### Question 9 — Declarative IaC Describes WHAT, Not HOW

**Difficulty**: Medium
**Answer Type**: one
**Topic**: In a declarative IaC approach, the engineer describes WHAT the infrastructure should look like — not the steps to create it

**Question**:
Complete the following statement that describes the Terraform configuration model:

> "In Terraform's declarative approach, the engineer describes ___________ the infrastructure should look like. Terraform determines the sequence of API calls and resource operations needed to produce that outcome."

- A) how
- B) why
- C) when
- D) **what**

---

### Question 10 — Conditional `count` Expression for Optional Resources

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Using a ternary conditional expression to set count = 1 when a boolean variable is true, otherwise count = 0

**Question**:
An engineer wants to conditionally create a bastion host only when the `create_bastion` variable is set to `true`. Complete the resource block:

```hcl
variable "create_bastion" {
  type    = bool
  default = false
}

resource "aws_instance" "bastion" {
  ami           = "ami-0abc1234"
  instance_type = "t3.nano"
  count         = var.create_bastion ? ___ : 0
}
```

What value fills the blank to create exactly one bastion instance when `create_bastion` is `true`?

- A) `true`
- B) **`1`**
- C) `"enabled"`
- D) `var.bastion_count`

---

### Question 11 — TWO Accurate Statements About IaC Solving ClickOps Problems

**Difficulty**: Medium
**Answer Type**: many
**Topic**: Identifying which IaC benefits directly address the reproducibility and drift problems of the manual ClickOps approach

**Question**:
A team is documenting why they are adopting Terraform to replace their ClickOps workflow. Which TWO of the following statements correctly complete the sentence: "We are adopting IaC because ___________"? (Select two.)

- A) **The same configuration can be applied to staging and production to guarantee identical environments, solving the problem of environments drifting apart over time through individual manual changes**
- B) IaC removes the need for cloud providers because infrastructure is simulated locally in configuration files
- C) IaC configurations run faster than manual provisioning because they use compiled binary formats
- D) **An IaC tool can compare the desired state in configuration files against the actual cloud state, detect manual changes made outside Terraform, and propose corrections**

---

### Question 12 — `resource` Keyword in HCL Block Declaration

**Difficulty**: Hard
**Answer Type**: one
**Topic**: Completing an HCL block declaration — the `resource` keyword identifies a managed infrastructure object

**Question**:
A new engineer is writing their first Terraform file. They accidentally leave out the opening keyword of the block:

```hcl
___________ "aws_s3_bucket" "assets" {
  bucket = "acme-company-assets-2024"
}
```

What keyword fills the blank to correctly declare an S3 bucket that Terraform will create and manage?

- A) `data`
- B) `module`
- C) `provider`
- D) **`resource`**

---

### Question 13 — TWO Advantages of Terraform Over AWS CloudFormation

**Difficulty**: Hard
**Answer Type**: many
**Topic**: Terraform's multi-cloud support and open-source/non-vendor-locked nature versus CloudFormation's AWS-only scope

**Question**:
A platform engineering team is choosing between Terraform and AWS CloudFormation for a new infrastructure project. Which TWO of the following correctly complete the statement: "We should choose Terraform over CloudFormation because ___________"? (Select two.)

- A) **Terraform can manage resources across AWS, Azure, and GCP in a single configuration and workflow, whereas CloudFormation only manages AWS resources**
- B) CloudFormation uses an imperative scripting model, while Terraform uses a superior declarative model
- C) Terraform plan output includes cost estimation for every resource type, while CloudFormation does not support cost estimation
- D) **Terraform is not tied to a single cloud vendor — the same tool, workflow, and skills apply whether managing AWS, Azure, GCP, or on-premises resources**

## Answer Key

| Q# | Answer(s) | Explanation | Source | Difficulty |
|----|-----------|-----------:|--------|------------|
| 1 | D | N/A | Repeatability — the IaC benefit that guarantees the same code deploys identical environments across staging and production | Easy |
| 2 | C | N/A | Completing a basic `aws_instance` resource block — the argument that specifies the EC2 instance type | Easy |
| 3 | C | N/A | Completing the definition of declarative IaC — configurations express the desired end state | Easy |
| 4 | D | N/A | Using `count = 0` to declare that no instances of a resource should exist, while keeping the block in configuration | Medium |
| 5 | D | N/A | Completing the definition of infrastructure drift — when actual cloud resources diverge from the Terraform configuration | Medium |
| 6 | D | N/A | The IaC benefit that provides a historical record of every infrastructure change via version control commits | Medium |
| 7 | B, D | N/A | Distinguishing provisioning tools (Terraform category) from configuration management tools — CloudFormation and Pulumi are provisioning tools | Medium |
| 8 | B | N/A | IaC configuration files serve as living documentation of infrastructure | Medium |
| 9 | D | N/A | In a declarative IaC approach, the engineer describes WHAT the infrastructure should look like — not the steps to create it | Medium |
| 10 | B | N/A | Using a ternary conditional expression to set count = 1 when a boolean variable is true, otherwise count = 0 | Medium |
| 11 | A, D | N/A | Identifying which IaC benefits directly address the reproducibility and drift problems of the manual ClickOps approach | Medium |
| 12 | D | N/A | Completing an HCL block declaration — the `resource` keyword identifies a managed infrastructure object | Hard |
| 13 | A, D | N/A | Terraform's multi-cloud support and open-source/non-vendor-locked nature versus CloudFormation's AWS-only scope | Hard |
