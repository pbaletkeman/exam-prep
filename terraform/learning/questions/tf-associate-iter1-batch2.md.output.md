# Terraform Associate Exam Questions

---

### Question 1 — Provider Definition

**Difficulty**: Easy
**Answer Type**: one
**Topic**: What a Terraform provider is

**Question**:
Which of the following best describes a Terraform provider?

- A) A HashiCorp-managed cloud platform that stores Terraform state remotely
- B) A plugin that bridges Terraform's HCL configuration to a target cloud or service API
- C) A built-in Terraform block that defines authentication credentials in a `.tf` file
- D) A version of the Terraform CLI binary compiled for a specific operating system

---

### Question 2 — Provider Tiers

**Difficulty**: Easy
**Answer Type**: one
**Topic**: Provider tier classification

**Question**:
Terraform providers are classified into three tiers. Which tier is maintained directly by HashiCorp and carries the highest level of trust?

- A) Community
- B) Partner
- C) Official
- D) Verified

---

### Question 3 — Plugin Architecture Communication

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Terraform Core and provider communication protocol

**Question**:
How does Terraform Core communicate with a provider plugin during execution?

- A) Through direct function calls within the same process binary
- B) Via HTTP REST API calls to a locally running provider web server
- C) Via gRPC, with the provider running as a separate process from Terraform Core
- D) Through shared memory mapped files in the `.terraform/` directory

---

### Question 4 — Provider Source Address Format

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Provider source address and default registry hostname

**Question**:
A `required_providers` block declares `source = "hashicorp/aws"`. What is the fully qualified source address that Terraform resolves this to?

- A) `github.com/hashicorp/aws`
- B) `registry.terraform.io/hashicorp/aws`
- C) `releases.hashicorp.com/hashicorp/aws`
- D) `hashicorp.com/terraform/providers/aws`

---

### Question 5 — `terraform init` Provider Download

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Where terraform init installs providers

**Question**:
When `terraform init` is run, where are provider plugins downloaded to?

- A) `~/.terraform.d/plugins/`
- B) `terraform.tfstate`
- C) `.terraform/providers/`
- D) `providers.lock/`

---

### Question 6 — Dependency Lock File

**Difficulty**: Medium
**Answer Type**: one
**Topic**: `.terraform.lock.hcl` purpose and version control

**Question**:
What is the purpose of the `.terraform.lock.hcl` file, and how should it be treated with respect to version control?

- A) It records the current Terraform state and must never be committed to version control
- B) It records exact provider versions and checksums installed; it must be committed to version control
- C) It is a temporary cache file generated on each `terraform init` run and should be added to `.gitignore`
- D) It stores encrypted provider credentials and must be committed but kept private

---

### Question 7 — Pessimistic Constraint Operator

**Difficulty**: Medium
**Answer Type**: one
**Topic**: `~>` version constraint operator behaviour

**Question**:
A `required_providers` block specifies `version = "~> 5.0"` for the AWS provider. Which versions are permitted by this constraint?

- A) Exactly version 5.0.0 only
- B) Any version >= 5.0.0 with no upper limit
- C) Any version >= 5.0 and < 6.0 (minor and patch updates within major version 5)
- D) Any version >= 5.0.0 and < 5.1.0 (patch updates only within minor version 5.0)

---

### Question 8 — Provider Alias

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Provider alias for multiple configurations

**Question**:
When is a provider `alias` required in a Terraform configuration?

- A) Whenever a provider block is declared inside a module rather than the root module
- B) When more than one configuration of the same provider is needed, such as managing resources in multiple regions
- C) Whenever a provider version constraint is specified in the `required_providers` block
- D) When Terraform is run with a non-default workspace

---

### Question 9 — What `terraform.tfstate` Stores

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Content and purpose of the Terraform state file

**Question**:
What does the `terraform.tfstate` file contain?

- A) The raw HCL configuration for all resources managed by Terraform
- B) A log of every `terraform apply` command that has been executed
- C) A JSON mapping of Terraform resource addresses to their real-world resource IDs and attributes
- D) The compiled binary representation of a Terraform execution plan

---

### Question 10 — Three Sources During Plan

**Difficulty**: Medium
**Answer Type**: many
**Topic**: Sources Terraform compares during `terraform plan`

**Question**:
When `terraform plan` runs, Terraform compares information from multiple sources to determine what changes are needed. Which TWO of the following are sources that Terraform uses during planning? (Select two.)

- A) The Terraform Registry API to check for provider updates
- B) The `.tf` configuration files representing the desired state
- C) The `terraform.tfstate` file representing the last-known resource state
- D) The `.terraform.lock.hcl` file representing installed provider versions

---

### Question 11 — Local vs Remote State

**Difficulty**: Hard
**Answer Type**: one
**Topic**: Differences between local and remote Terraform state

**Question**:
Which of the following is a characteristic of local Terraform state that makes it unsuitable for team environments?

- A) Local state files use a binary format that cannot be read or backed up
- B) Local state provides no locking mechanism, meaning concurrent `terraform apply` runs by different team members can corrupt state
- C) Local state is automatically deleted after each `terraform apply` completes
- D) Local state cannot store resource attribute values, only resource addresses

---

### Question 12 — `sensitive = true` and State

**Difficulty**: Hard
**Answer Type**: one
**Topic**: Behaviour of `sensitive = true` in outputs vs state storage

**Question**:
A Terraform output is declared with `sensitive = true`. What is the effect of this setting on how the value is handled?

- A) The value is encrypted with AES-256 before being written to `terraform.tfstate`
- B) The value is redacted from `terraform.tfstate` entirely and stored in a separate secrets file
- C) The value is masked in terminal output but is still stored in plaintext in `terraform.tfstate`
- D) The value is masked in terminal output and also removed from any remote backend storage

---

### Question 13 — `terraform state` Commands

**Difficulty**: Medium
**Answer Type**: many
**Topic**: Terraform state CLI subcommands

**Question**:
Which TWO `terraform state` subcommands would be appropriate for inspecting state without modifying it? (Select two.)

- A) `terraform state rm`
- B) `terraform state list`
- C) `terraform state push`
- D) `terraform state show`

## Answer Key

| Q# | Answer(s) | Explanation | Source | Difficulty |
|----|-----------|-----------:|--------|------------|
| 1 | B | N/A | What a Terraform provider is | Easy |
| 2 | C | N/A | Provider tier classification | Easy |
| 3 | C | N/A | Terraform Core and provider communication protocol | Medium |
| 4 | B | N/A | Provider source address and default registry hostname | Medium |
| 5 | C | N/A | Where terraform init installs providers | Medium |
| 6 | B | N/A | `.terraform.lock.hcl` purpose and version control | Medium |
| 7 | C | N/A | `~>` version constraint operator behaviour | Medium |
| 8 | B | N/A | Provider alias for multiple configurations | Medium |
| 9 | C | N/A | Content and purpose of the Terraform state file | Medium |
| 10 | B, C | N/A | Sources Terraform compares during `terraform plan` | Medium |
| 11 | B | N/A | Differences between local and remote Terraform state | Hard |
| 12 | C | N/A | Behaviour of `sensitive = true` in outputs vs state storage | Hard |
| 13 | B, D | N/A | Terraform state CLI subcommands | Medium |
