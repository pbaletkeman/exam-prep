# Terraform Associate (004) — Question Bank Iter 7 Batch 8

**Iteration**: 7
**Iteration Style**: Fill-in-the-blank / complete the HCL — every question presents a partial HCL snippet or partial statement with a `___________` placeholder; select which option correctly fills the blank
**Batch**: 8
**Objectives**: 6 (State Backends & Locking) + 7 (Importing & State Inspection) + 8 (HCP Terraform)
**Source Prompts**: prompt12, prompt13, prompt14, prompt15
**Generated**: 2026-04-25
**Total Questions**: 13
**Difficulty Split**: 3 Easy / 8 Medium / 2 Hard
**Answer Types**: 10 `one` / 3 `many` / 0 `none`

---

## Questions

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

**Answer**: C

**Explanation**:
`terraform force-unlock LOCK_ID` is the command used to manually release a state lock when a Terraform process died while holding it. The lock ID is displayed in the error message when another operation encounters the existing lock — for example: `Error acquiring the state lock: Lock Info: ID: abc-12345`. You pass that ID directly to `force-unlock`. Use this command with caution: only run it when you are certain no other operation is actually in progress, because releasing a lock held by a live process could lead to concurrent state writes and corruption. Options A (`state unlock`), B (`unlock-state`), and D (`state release`) are not valid Terraform commands.

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

**Answer**: B

**Explanation**:
`terraform login` opens a browser window, prompts you to log in to HCP Terraform (or Terraform Enterprise), generates an API token, and writes it to `~/.terraform.d/credentials.tfrc.json`. This is the default credential store for Terraform CLI. The file uses a JSON format that maps hostnames to their tokens, so tokens for multiple registries can coexist. If you prefer not to use `terraform login`, you can alternatively set the `TF_TOKEN_app_terraform_io` environment variable to provide the token directly — useful in CI/CD pipelines where storing files is impractical. Option A uses a path that does not exist. Option C (`terraform.tfvars`) is for variable values, not credentials. Option D is not a path Terraform uses.

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

**Answer**: A, C

**Explanation**:
`TF_LOG` supports six values in decreasing verbosity order: `TRACE`, `DEBUG`, `INFO`, `WARN`, `ERROR`, and `OFF`. Setting a level captures all messages at that level **and all less-verbose levels** — so `INFO` includes `INFO`, `WARN`, and `ERROR` messages. `TRACE` is the most verbose and is used by HashiCorp support for deep debugging because it includes all HTTP API calls and responses (option A). The full ordering `TRACE > DEBUG > INFO > WARN > ERROR` is correct (option C). Option B is wrong — `WARN` is **less** verbose than `INFO` (fewer messages), not more. Option D is wrong — `ERROR` still emits error-level log messages; `OFF` is the level that completely disables logging output.

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

**Answer**: A

**Explanation**:
`terraform state mv <SOURCE_ADDRESS> <DESTINATION_ADDRESS>` takes exactly two positional arguments — the current resource address and the new resource address. Both are positional, not named flags. This command updates the state file to reflect the new name without modifying any cloud infrastructure. The typical workflow is: (1) rename the `resource` block label in your `.tf` file, (2) run `terraform state mv aws_instance.web aws_instance.web_server` to align state with the configuration change. Without the `state mv`, the next `terraform plan` would show a destroy of `aws_instance.web` and a create of `aws_instance.web_server`. Options B and D use non-existent flags. Option C passes separate type and label strings instead of the combined `TYPE.LABEL` address format.

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

**Answer**: C

**Explanation**:
`terraform init -migrate-state` is the flag that tells Terraform to detect the change in backend configuration and offer to copy the existing state to the new backend. If you confirm the prompt, Terraform reads the current state from the old backend (local file in this case) and writes it to the new backend (S3 bucket). This preserves state continuity — no resources need to be re-imported. The contrasting flag, `-reconfigure`, also re-initialises the backend but **discards the migration prompt** — it reconfigures the backend without attempting to copy existing state, which means existing local state would be abandoned and the new backend would start empty. Use `-reconfigure` when you intentionally want a fresh state (e.g., switching to a completely unrelated environment).

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

**Answer**: C

**Explanation**:
Inside the `cloud` block's `workspaces` sub-block, you can select workspaces in two mutually exclusive ways: by `name` (a single workspace name string) or by `tags` (a list of tag strings — only workspaces that have **all** of the specified tags are selected). Tag-based selection enables workspace-per-environment patterns where a single configuration targets multiple workspaces matching the tag filter. This is a key advantage of the `cloud` block over the legacy `backend "remote"` block, which only supports workspace selection by name. Option A (`filter`) and D (`labels`) are not valid arguments in the `workspaces` sub-block. Option B (`name`) would work for selecting a single workspace by name, but cannot accept a list of tag values.

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

**Answer**: C

**Explanation**:
Terraform supports a `TF_TOKEN_<HOSTNAME>` environment variable pattern where the hostname component uses underscores in place of periods and hyphens. For the default HCP Terraform host `app.terraform.io`, the variable name is `TF_TOKEN_app_terraform_io`. Setting this variable provides the API token without requiring `terraform login` or a credentials file — making it the standard approach in CI/CD pipelines. Terraform reads this variable during `terraform init` and subsequent operations to authenticate to HCP Terraform. If both `TF_TOKEN_app_terraform_io` and a stored credentials file exist, the environment variable takes precedence. Options A (`TF_API_TOKEN`), B (`TF_CLOUD_TOKEN`), and D (`TERRAFORM_CLOUD_CREDENTIAL`) are not recognised by Terraform.

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

**Answer**: C

**Explanation**:
When reading remote state from an HCP Terraform workspace using a `terraform_remote_state` data source, the `backend` argument must be set to `"remote"`. Despite the `cloud` block being the preferred way to connect a working configuration to HCP Terraform, the `terraform_remote_state` data source still uses `backend = "remote"` with an `organization` and `workspaces.name` in its `config` block. The `config` arguments mirror the legacy `backend "remote"` configuration syntax. Setting `backend = "remote"` does not use the local filesystem; Terraform contacts the HCP Terraform API to fetch the state outputs from the specified workspace. Options A (`"hcp"`), B (`"cloud"`), and D (`"terraform_cloud"`) are not valid `terraform_remote_state` backend values.

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

**Answer**: D

**Explanation**:
HCP Terraform policy enforcement has three levels: `advisory` (policy failure is a warning only — the run continues), `soft-mandatory` (failure blocks the run but an authorised user can override and proceed), and `hard-mandatory` (failure blocks the run permanently — it **cannot be overridden** by anyone, including organisation owners). Hard-mandatory policies represent compliance requirements that must be satisfied before any apply can proceed. `soft-mandatory` is useful for policies that normally must pass but may need an escape hatch for emergencies. `advisory` is suitable for informational checks or phased rollouts of new policies. Option B (`advisory`) allows the run to continue. Option A (`soft-mandatory`) allows overriding. Option C (`blocking`) is not a valid enforcement level name.

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

**Answer**: C

**Explanation**:
Modules published in an HCP Terraform private registry use the format `app.terraform.io/<ORGANIZATION>/<MODULE>/<PROVIDER>`. The hostname `app.terraform.io` identifies the HCP Terraform registry (as opposed to `registry.terraform.io` for the public registry). The organisation name, module name, and provider name follow the same three-part structure used by the public registry. During `terraform init`, Terraform authenticates to `app.terraform.io` using the stored credential (from `terraform login` or `TF_TOKEN_app_terraform_io`) and downloads the private module. Option B (`"my-org/vpc/aws"`) is the format for the public Terraform Registry and would resolve to `registry.terraform.io`. Options A and D use fictional hostnames.

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

**Answer**: A, C

**Explanation**:
HCP Terraform natively supports two policy frameworks: Sentinel (using HashiCorp's own DSL) and OPA — Open Policy Agent (using the Rego language). Both are first-class options for writing and enforcing infrastructure policies (option A is correct). Both frameworks also share the same three enforcement levels — `advisory`, `soft-mandatory`, and `hard-mandatory` — applied at the policy set level (option C is correct). Option B is wrong — organisations can use both Sentinel and OPA simultaneously; different policy sets can use different frameworks, and all apply during runs. Option D is wrong — OPA in HCP Terraform evaluates Terraform plan data just as Sentinel does; it is not restricted to cost estimation, and both frameworks can perform resource-level checks.

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

**Answer**: B

**Explanation**:
Terraform provides two granular log environment variables that override `TF_LOG` for specific subsystems: `TF_LOG_CORE` controls log verbosity for the Terraform core binary (the orchestrator that reads configuration, manages state, and calls providers), while `TF_LOG_PROVIDER` controls log verbosity for provider plugins (the binaries that communicate with cloud APIs). When both are set, `TF_LOG` is ignored in favour of the more specific variables. This separation is valuable when debugging provider API issues (set `TF_LOG_PROVIDER=TRACE` for full API call detail) while keeping core output at a lower verbosity level to reduce noise. Options A, C, and D are not valid Terraform environment variable names.

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

**Answer**: C

**Explanation**:
HCP Terraform Health Assessments perform a `terraform plan -refresh-only` on a configurable schedule (e.g., daily or weekly). This operation queries the cloud provider APIs for the current state of all managed resources and compares them to what is recorded in Terraform state — without writing any changes to state or infrastructure. If attributes differ (e.g., a tag was manually changed, a security group rule was added outside Terraform), the assessment flags the workspace as drifted and can send notifications via email, Slack, or PagerDuty. Option A (`terraform apply -refresh-only`) is wrong — a health assessment never automatically modifies state; it is read-only. Option B (`terraform validate`) checks configuration syntax — it cannot detect live infrastructure drift. Option D (`terraform state pull`) only downloads state; it does not query the cloud provider for live resource attributes.
