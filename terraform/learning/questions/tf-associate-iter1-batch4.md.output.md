# Terraform Associate Exam Questions

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

## Answer Key

| Q# | Answer(s) | Explanation | Source | Difficulty |
|----|-----------|-----------:|--------|------------|
| 1 | B | N/A | Resource block syntax and components | Easy |
| 2 | B | N/A | What a data source does | Easy |
| 3 | C | N/A | How to reference a data source attribute | Medium |
| 4 | B, D | N/A | Resource meta-arguments | Medium |
| 5 | B | N/A | How implicit dependencies are created | Medium |
| 6 | C | N/A | When to use `depends_on` | Medium |
| 7 | B | N/A | `create_before_destroy` lifecycle argument | Medium |
| 8 | C | N/A | `prevent_destroy` lifecycle argument | Medium |
| 9 | B | N/A | `ignore_changes` lifecycle argument | Medium |
| 10 | B | N/A | `replace_triggered_by` lifecycle argument | Medium |
| 11 | B | N/A | What the `moved` block does in Terraform state | Hard |
| 12 | B | N/A | Terraform default parallelism and the `-parallelism` flag | Hard |
| 13 | B, C | N/A | Timing of data source reads during plan and apply | Medium |
