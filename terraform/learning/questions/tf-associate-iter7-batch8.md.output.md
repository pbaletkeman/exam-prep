# Terraform Associate Exam Questions

---

### Question 1 — `terraform force-unlock` Command Syntax

**Difficulty**: Easy
**Answer Type**: one
**Topic**: Correct syntax for releasing a stuck state lock using `terraform force-unlock`

**Question**:
Complete the command used to forcibly release a stuck state lock when the lock ID is `abc-12345`:

```bash
terraform ___________ abc-12345
```

- A) `state unlock`
- B) `unlock-state`
- C) `force-unlock`
- D) `state release`

---

### Question 2 — `terraform login` Credential Storage Location

**Difficulty**: Easy
**Answer Type**: one
**Topic**: Where `terraform login` writes the API token for HCP Terraform authentication

**Question**:
Complete the sentence: After running `terraform login` and authenticating via the browser, the API token is stored in ___________.

- A) `~/.terraform/credentials.json`
- B) `~/.terraform.d/credentials.tfrc.json`
- C) `./terraform.tfvars` in the working directory
- D) `~/.config/terraform/token`

---

### Question 3 — TF_LOG Verbosity Ordering

**Difficulty**: Easy
**Answer Type**: many
**Topic**: Correct relative verbosity of `TF_LOG` levels and which level is the most verbose

**Question**:
Which **TWO** of the following statements about `TF_LOG` log levels are correct?

- A) `TRACE` is the most verbose level — it captures all API calls, full request/response bodies, and internal Terraform core operations; `DEBUG` is the next level down
- B) `WARN` produces more output than `INFO` — warnings include all informational messages plus additional warning-level detail
- C) The full verbosity order from most to least verbose is: `TRACE > DEBUG > INFO > WARN > ERROR`; setting a level includes all messages at that level and less verbose levels — `INFO` would show `INFO`, `WARN`, and `ERROR` messages
- D) `ERROR` and `OFF` are the same — setting `TF_LOG=ERROR` disables logging just as `TF_LOG=OFF` does

---

### Question 4 — `terraform state mv` to Rename a Resource

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Using `terraform state mv` to rename a resource address in state without destroying it

**Question**:
Complete the command to rename the resource `aws_instance.web` to `aws_instance.web_server` in state without destroying or recreating the infrastructure:

```bash
terraform state mv ___________ ___________
```

- A) `aws_instance.web` `aws_instance.web_server`
- B) `--from aws_instance.web` `--to aws_instance.web_server`
- C) `"aws_instance" "web"` `"aws_instance" "web_server"`
- D) `-source=aws_instance.web` `-dest=aws_instance.web_server`

---

### Question 5 — `terraform init` Flag to Migrate State to a New Backend

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Which `terraform init` flag to use when changing backends and you want to transfer existing state

**Question**:
An engineer adds an S3 backend to a previously local-only configuration and wants to migrate the existing `terraform.tfstate` to the new S3 bucket. Complete the command:

```bash
terraform init ___________
```

- A) `-backend-migrate`
- B) `-reconfigure`
- C) `-migrate-state`
- D) `-force-copy`

---

### Question 6 — `cloud` Block Workspace Selection by Tags

**Difficulty**: Medium
**Answer Type**: one
**Topic**: How to configure the `cloud` block to select workspaces matching a set of tags rather than a single name

**Question**:
Complete the `cloud` block so the configuration targets all HCP Terraform workspaces tagged with `env=production`:

```hcl
terraform {
  cloud {
    organization = "acme-corp"

    workspaces {
      ___________ = ["env=production"]
    }
  }
}
```

- A) `filter`
- B) `name`
- C) `tags`
- D) `labels`

---

### Question 7 — `TF_TOKEN_` Environment Variable for HCP Terraform

**Difficulty**: Medium
**Answer Type**: one
**Topic**: The exact environment variable name used to provide an HCP Terraform API token in CI/CD pipelines

**Question**:
Complete the environment variable export that provides a Terraform API token for `app.terraform.io` without running `terraform login`:

```bash
export ___________="your-api-token-here"
```

- A) `TF_API_TOKEN`
- B) `TF_CLOUD_TOKEN`
- C) `TF_TOKEN_app_terraform_io`
- D) `TERRAFORM_CLOUD_CREDENTIAL`

---

### Question 8 — `terraform_remote_state` Backend Type for HCP Terraform

**Difficulty**: Medium
**Answer Type**: one
**Topic**: The correct `backend` value in a `terraform_remote_state` data source when reading from an HCP Terraform workspace

**Question**:
Complete the `terraform_remote_state` data source to read outputs from another HCP Terraform workspace named `networking-production`:

```hcl
data "terraform_remote_state" "networking" {
  backend = "___________"
  config = {
    organization = "acme-corp"
    workspaces = {
      name = "networking-production"
    }
  }
}
```

- A) `"hcp"`
- B) `"cloud"`
- C) `"remote"`
- D) `"terraform_cloud"`

---

### Question 9 — Sentinel Policy Enforcement Level That Cannot Be Overridden

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Which HCP Terraform policy enforcement level blocks a run and cannot be overridden by any user

**Question**:
Complete the sentence: A Sentinel or OPA policy set with enforcement level ___________ will block a run when the policy fails, and **no user in the organisation — including owners — can override the failure**.

- A) `soft-mandatory`
- B) `advisory`
- C) `blocking`
- D) `hard-mandatory`

---

### Question 10 — Private Registry Module Source Format

**Difficulty**: Medium
**Answer Type**: one
**Topic**: The source string format for referencing a module from an HCP Terraform private registry

**Question**:
Complete the `source` argument to reference a module named `vpc` published in the `my-org` HCP Terraform private registry under the `aws` provider:

```hcl
module "vpc" {
  source  = "___________"
  version = "~> 2.1"
}
```

- A) `"private.terraform.io/my-org/vpc/aws"`
- B) `"my-org/vpc/aws"`
- C) `"app.terraform.io/my-org/vpc/aws"`
- D) `"registry.terraform.io/private/my-org/vpc/aws"`

---

### Question 11 — Sentinel vs OPA: Two Correct Statements

**Difficulty**: Medium
**Answer Type**: many
**Topic**: Differences between Sentinel (HashiCorp DSL) and OPA (Rego) as HCP Terraform policy frameworks

**Question**:
Which **TWO** of the following statements about HCP Terraform policy enforcement are correct?

- A) Sentinel uses HashiCorp's own domain-specific language (DSL); OPA (Open Policy Agent) policies are written in Rego — both frameworks are supported natively in HCP Terraform as policy enforcement options
- B) Sentinel and OPA are mutually exclusive — an HCP Terraform organisation must choose one framework and cannot use both simultaneously
- C) Both Sentinel and OPA policy sets can be assigned enforcement levels: `advisory`, `soft-mandatory`, or `hard-mandatory`
- D) OPA policies can only be used for cost estimation checks; Sentinel is the only framework that can evaluate Terraform plan data for resource-level policy enforcement

---

### Question 12 — `TF_LOG_CORE` and `TF_LOG_PROVIDER` Env Vars

**Difficulty**: Hard
**Answer Type**: one
**Topic**: Using `TF_LOG_CORE` and `TF_LOG_PROVIDER` to get separate log streams for the Terraform core binary and provider plugins

**Question**:
An engineer wants to see `DEBUG`-level logs from the Terraform core binary only, while seeing `TRACE`-level logs from provider plugins only. Complete the environment variable exports:

```bash
export ___________=DEBUG
export ___________=TRACE
```

- A) `TF_LOG_BINARY` and `TF_LOG_PLUGINS`
- B) `TF_LOG_CORE` and `TF_LOG_PROVIDER`
- C) `TF_CORE_LOG` and `TF_PROVIDER_LOG`
- D) `TF_LOG_TERRAFORM` and `TF_LOG_PLUGIN`

---

### Question 13 — HCP Terraform Health Assessments: Underlying Command

**Difficulty**: Hard
**Answer Type**: one
**Topic**: What operation HCP Terraform Health Assessments perform on a configurable schedule to detect infrastructure drift

**Question**:
Complete the sentence: HCP Terraform Health Assessments work by automatically running ___________ on a configurable schedule — if the result shows drift between actual cloud resources and Terraform state, the assessment is marked as unhealthy and notifications can be triggered.

- A) `terraform apply -refresh-only` — reconciling state with actual resources on every scheduled run
- B) `terraform validate` — checking configuration syntax and provider schema compliance
- C) `terraform plan -refresh-only` — detecting drift without modifying state or infrastructure
- D) `terraform state pull` — downloading and comparing the remote state to the cloud resource API responses

## Answer Key

| Q# | Answer(s) | Explanation | Source | Difficulty |
|----|-----------|-----------:|--------|------------|
| 1 | C | N/A | Correct syntax for releasing a stuck state lock using `terraform force-unlock` | Easy |
| 2 | B | N/A | Where `terraform login` writes the API token for HCP Terraform authentication | Easy |
| 3 | A, C | N/A | Correct relative verbosity of `TF_LOG` levels and which level is the most verbose | Easy |
| 4 | A | N/A | Using `terraform state mv` to rename a resource address in state without destroying it | Medium |
| 5 | C | N/A | Which `terraform init` flag to use when changing backends and you want to transfer existing state | Medium |
| 6 | C | N/A | How to configure the `cloud` block to select workspaces matching a set of tags rather than a single name | Medium |
| 7 | C | N/A | The exact environment variable name used to provide an HCP Terraform API token in CI/CD pipelines | Medium |
| 8 | C | N/A | The correct `backend` value in a `terraform_remote_state` data source when reading from an HCP Terraform workspace | Medium |
| 9 | D | N/A | Which HCP Terraform policy enforcement level blocks a run and cannot be overridden by any user | Medium |
| 10 | C | N/A | The source string format for referencing a module from an HCP Terraform private registry | Medium |
| 11 | A, C | N/A | Differences between Sentinel (HashiCorp DSL) and OPA (Rego) as HCP Terraform policy frameworks | Medium |
| 12 | B | N/A | Using `TF_LOG_CORE` and `TF_LOG_PROVIDER` to get separate log streams for the Terraform core binary and provider plugins | Hard |
| 13 | C | N/A | What operation HCP Terraform Health Assessments perform on a configurable schedule to detect infrastructure drift | Hard |
