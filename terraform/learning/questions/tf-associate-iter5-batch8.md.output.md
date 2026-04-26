# Terraform Associate Exam Questions

---

### Question 1 — Local Backend vs S3 Backend: Collaboration and Safety

**Difficulty**: Easy
**Answer Type**: one
**Topic**: Contrast between the limitations of the local backend and the capabilities of a remote S3 backend

**Question**:
Compare the **local backend** (default `terraform.tfstate` file) with the **S3 backend**. What is the most significant operational difference between the two?

- A) The local backend encrypts state automatically; the S3 backend stores state in plaintext unless `encrypt = true` is set
- B) The local backend stores state in a file on the workstation running Terraform — it offers no collaboration support, no built-in locking, and no encryption; the S3 backend stores state in a shared S3 bucket — it enables team collaboration, supports state locking via DynamoDB, and supports server-side encryption at rest
- C) Both backends support state locking — the local backend uses a file lock while S3 uses DynamoDB; encryption is optional in both cases
- D) The S3 backend can only be used with AWS resources; the local backend supports all providers

---

### Question 2 — `terraform plan -refresh-only` vs `terraform apply -refresh-only`

**Difficulty**: Easy
**Answer Type**: one
**Topic**: Contrast between the plan-only and apply forms of the refresh-only flag

**Question**:
Compare `terraform plan -refresh-only` with `terraform apply -refresh-only`. What is the key difference between the two commands?

- A) `terraform plan -refresh-only` updates state to match the cloud; `terraform apply -refresh-only` only shows what has drifted without changing state
- B) `terraform plan -refresh-only` shows what drift exists between actual cloud resources and Terraform state — it **does not change state** and makes no modifications anywhere; `terraform apply -refresh-only` **updates state** to match the actual cloud resource values, reconciling drift — no infrastructure is created, modified, or destroyed in either case
- C) Both commands are identical — `-refresh-only` has the same effect regardless of whether it is used with `plan` or `apply`
- D) `terraform apply -refresh-only` creates new resources to match any detected drift; `terraform plan -refresh-only` only shows the diff

---

### Question 3 — `cloud` Block vs `backend "remote"`: Preferred HCP Terraform Connection

**Difficulty**: Easy
**Answer Type**: one
**Topic**: Contrast between the cloud block and the legacy remote backend for connecting to HCP Terraform

**Question**:
Compare the `cloud` block (Terraform 1.1+) with the `backend "remote"` block as methods for connecting to HCP Terraform. What is the key difference?

- A) `backend "remote"` is the current standard; the `cloud` block is a deprecated alias introduced for backward compatibility
- B) The `cloud` block is the **preferred, modern method** for connecting to HCP Terraform — it supports workspace selection by tags (in addition to name) and integrates features specific to HCP Terraform; `backend "remote"` is the **legacy method** — it is still valid and functional but predates HCP Terraform-specific features; HashiCorp recommends migrating to the `cloud` block
- C) Both blocks are exactly equivalent — the `cloud` block is simply renamed from `backend "remote"` with no functional differences
- D) The `cloud` block only supports HCP Terraform Free tier; `backend "remote"` is required for paid HCP Terraform tiers

---

### Question 4 — `terraform init -migrate-state` vs `terraform init -reconfigure`

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Contrast between the two init flags used when changing a backend configuration

**Question**:
Compare `terraform init -migrate-state` with `terraform init -reconfigure`. When would you use each, and what does each do with existing state?

- A) Both flags are equivalent — they both migrate state to the new backend without user confirmation
- B) `terraform init -migrate-state` **copies existing state** from the old backend to the newly configured backend — it is used when you want to preserve your state history when switching backends; `terraform init -reconfigure` **ignores the existing state** and reconfigures the backend without migrating — it is used when you want to start fresh or when the state has already been manually moved
- C) `terraform init -reconfigure` migrates state; `terraform init -migrate-state` discards it — the flags are inverted from what their names suggest
- D) `-migrate-state` only works when switching between two remote backends; it cannot migrate from the local backend to a remote backend

---

### Question 5 — `terraform state mv` vs `terraform state rm`

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Contrast between the purpose and effect of terraform state mv and terraform state rm

**Question**:
Compare `terraform state mv` with `terraform state rm`. Both modify what Terraform tracks in state — what is the fundamental difference between them?

- A) `terraform state mv` deletes a resource from both state and the cloud; `terraform state rm` only removes it from state while leaving the cloud resource intact
- B) `terraform state mv` **relocates** a resource within state — it renames or moves the resource's address (e.g., from `aws_instance.web` to `aws_instance.web_server`, or from a root resource into a module) without destroying or re-creating anything; `terraform state rm` **removes** a resource entry from state entirely — Terraform stops managing it, but the actual cloud resource is left untouched; the resource becomes unmanaged drift
- C) `terraform state rm` renames a resource; `terraform state mv` deletes it permanently from both state and the cloud provider
- D) Both commands are equivalent — the only difference is that `terraform state mv` requires confirmation while `terraform state rm` does not

---

### Question 6 — HCP Terraform Workspace Variables vs Variable Sets

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Contrast between workspace-specific variables and variable sets in HCP Terraform

**Question**:
Compare **workspace variables** with **variable sets** in HCP Terraform. What is the key difference in scope and reusability?

- A) Workspace variables are reusable across all workspaces in an organisation; variable sets are scoped to a single workspace only
- B) Workspace variables are defined **per workspace** — they apply only to that specific workspace and must be configured individually for each workspace that needs them; variable sets are **reusable collections** of variables that can be assigned to multiple workspaces or an entire organisation — a single change to a variable set propagates to all assigned workspaces
- C) Both workspace variables and variable sets work identically — the only difference is that variable sets have a different UI panel in HCP Terraform
- D) Variable sets are used only for Terraform input variables; workspace variables are used only for environment variables (like `AWS_ACCESS_KEY_ID`)

---

### Question 7 — Speculative Plan vs Plan-and-Apply Run in HCP Terraform

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Contrast between a speculative plan run and a plan-and-apply run in HCP Terraform

**Question**:
Compare a **speculative plan** run with a **plan-and-apply** run in HCP Terraform. What is the fundamental difference?

- A) A speculative plan is faster because it skips the refresh phase; a plan-and-apply run always refreshes state before planning
- B) A speculative plan is **read-only** — it computes what changes would occur but **can never progress to an apply**; it is triggered by pull requests or API calls and posts its results as status checks; a plan-and-apply run **can apply changes** — it proceeds through planning and, based on workspace settings, either auto-applies or waits for manual confirmation before applying
- C) A plan-and-apply run is triggered only by manual CLI commands; a speculative plan is triggered only by VCS events
- D) Both run types can apply infrastructure changes — the difference is that a speculative plan requires an additional approval step before applying

---

### Question 8 — `TF_LOG_CORE` vs `TF_LOG_PROVIDER` vs `TF_LOG`

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Contrast between the granular log variables and the combined TF_LOG variable

**Question**:
Compare `TF_LOG_CORE`, `TF_LOG_PROVIDER`, and `TF_LOG`. How do the granular variables differ from the single combined variable?

- A) `TF_LOG_CORE` and `TF_LOG_PROVIDER` are deprecated aliases for `TF_LOG` — they all control the same log stream
- B) `TF_LOG` sets a **single log level for all Terraform output** — both the core engine and provider plugins log at the same verbosity; `TF_LOG_CORE` and `TF_LOG_PROVIDER` are **independent controls** — `TF_LOG_CORE` controls only the Terraform core engine's log output, and `TF_LOG_PROVIDER` controls only the provider plugin log output; this allows operators to enable `TRACE` for a specific provider while keeping core logs at a quieter level (or vice versa), reducing noise when debugging provider-specific issues
- C) `TF_LOG_PROVIDER` sets log output for all Terraform runs in a project; `TF_LOG_CORE` sets it for a specific workspace; `TF_LOG` is the organisation-wide default
- D) `TF_LOG_CORE` and `TF_LOG_PROVIDER` only apply when `TF_LOG_PATH` is also set — without a path, only `TF_LOG` produces output

---

### Question 9 — Sentinel vs OPA: Two HCP Terraform Policy Frameworks

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Contrast between Sentinel and OPA as the two policy enforcement frameworks in HCP Terraform

**Question**:
HCP Terraform supports two policy enforcement frameworks: **Sentinel** and **OPA (Open Policy Agent)**. What is the key difference between them?

- A) Sentinel is used for cost estimation policies; OPA is used for security compliance policies — they target different policy domains
- B) Sentinel uses **HashiCorp's proprietary Sentinel DSL** — it is developed and maintained by HashiCorp and is tightly integrated with HCP Terraform's policy workflow; OPA uses **Rego**, an open-source policy language maintained by the Open Policy Agent community — it offers broader ecosystem support and is used across many tools beyond Terraform; both frameworks enforce the same three enforcement levels (advisory, soft-mandatory, hard-mandatory) in HCP Terraform
- C) OPA policies run before the plan; Sentinel policies run after the plan but before the apply — they execute at different points in the run lifecycle
- D) Sentinel is available on all HCP Terraform tiers; OPA is only available on the Enterprise tier and cannot be used in the Free or Plus plans

---

### Question 10 — Three Policy Enforcement Levels: Two Key Contrasts

**Difficulty**: Medium
**Answer Type**: many
**Topic**: Contrasting TWO of the three HCP Terraform policy enforcement levels

**Question**:
HCP Terraform policy sets support three enforcement levels: `advisory`, `soft-mandatory`, and `hard-mandatory`. Which TWO statements correctly describe a contrast between these levels? (Select two.)

- A) An `advisory` policy failure displays a warning but **does not block the run** — the plan-and-apply continues regardless of the policy result; a `hard-mandatory` policy failure **always blocks the run** and cannot be overridden by any user, including organisation owners
- B) A `soft-mandatory` policy failure blocks the run by default but can be **overridden** by a user with sufficient permissions (typically an organisation owner or designated override role) — the run can then proceed despite the policy failure; `hard-mandatory` failure **cannot be overridden** by any user under any circumstances
- C) `advisory` policies only apply to speculative plans; `soft-mandatory` and `hard-mandatory` policies apply to plan-and-apply runs
- D) All three enforcement levels cause the run to fail with a non-zero exit code — the difference is only in how the failure message is displayed in the UI

---

### Question 11 — HCP Terraform Owner Role vs Workspace Admin Permission

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Contrast between organisation-level Owner role and workspace-level Admin permission in HCP Terraform

**Question**:
Compare the **Owner** organisation-level role with the **Admin** workspace-level permission in HCP Terraform. What is the scope difference?

- A) Owner and Admin are the same role — "Owner" is the UI label and "Admin" is the API name for the same permission level
- B) **Owner** is an **organisation-level role** — it grants full access to all settings, workspaces, teams, and governance across the entire organisation; **Admin** is a **workspace-level permission** — it grants full control over a specific workspace (managing variables, team access, workspace settings, and run approvals) but has no authority over other workspaces or organisation-level settings unless that permission is explicitly granted on each workspace
- C) Admin is a superset of Owner — an Admin can manage organisation-level settings in addition to workspace-level settings
- D) Owner role is limited to read-only access across all workspaces; Admin is the role that allows applying changes

---

### Question 12 — Import Block Workflow vs CLI Import Workflow: Two Key Differences

**Difficulty**: Hard
**Answer Type**: many
**Topic**: Contrasting TWO workflow differences between the declarative import block (Terraform 1.5+) and the legacy terraform import CLI command

**Question**:
Compare the workflow for importing an existing resource using the declarative `import` block versus the legacy `terraform import` CLI command. Which TWO statements correctly describe a difference between the two workflows? (Select two.)

- A) The `import` block workflow supports **running `terraform plan` before any state changes are made** — the engineer can preview the import (and optionally generate HCL with `-generate-config-out`) before committing; the CLI `terraform import` command **immediately writes the resource to state** with no plan preview step — there is no way to preview what will be imported before the state is modified
- B) The CLI `terraform import` command **requires an existing resource block** in the configuration before it can run — the block body can be empty, but the block must exist; the `import` block can be added to configuration and used with `terraform plan -generate-config-out=generated.tf` to have Terraform **generate the resource block automatically** — the engineer starts with only the `import` block and no resource block
- C) Both workflows require the resource block to exist before the import command runs — the `import` block offers no config generation capability
- D) The CLI `terraform import` command can import multiple resources in a single run; the `import` block can only import one resource per block

---

### Question 13 — Dynamic OIDC Credentials vs Static Environment Variable Credentials in HCP Terraform

**Difficulty**: Hard
**Answer Type**: one
**Topic**: Deep contrast between dynamic OIDC-based provider authentication and static credential storage in HCP Terraform workspaces

**Question**:
Compare two approaches for authenticating an HCP Terraform workspace to AWS:

- **Approach A**: Store `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY` as sensitive environment variables in an HCP Terraform variable set
- **Approach B**: Configure dynamic provider credentials using OIDC — the workspace requests a short-lived token from HCP Terraform's OIDC provider, which AWS validates against a trusted identity provider, and returns temporary credentials

What are the two most significant security differences between these approaches?

- A) Approach A is more secure because the credentials are marked sensitive and are never shown in logs; Approach B exposes credentials in the plan output because OIDC tokens are not marked sensitive
- B) In Approach A, the **static credentials are long-lived** — they persist in HCP Terraform's variable storage indefinitely and if exfiltrated (e.g., from a compromised CI system or leaked variable export) they remain valid until manually rotated; in Approach B, credentials are **short-lived and scoped per run** — they are issued fresh for each Terraform run with a TTL, so a captured credential becomes useless quickly; additionally, Approach B **eliminates static secret storage** entirely — no `AWS_ACCESS_KEY_ID` or `AWS_SECRET_ACCESS_KEY` is stored anywhere in HCP Terraform, which removes a class of secret-leakage risk
- C) Approach A credentials are encrypted using HCP Terraform's AES-256 key management; Approach B credentials are stored in plaintext because they are temporary
- D) Both approaches have equivalent security — the static credentials in Approach A are marked sensitive, which provides the same protection as OIDC's short-lived tokens

## Answer Key

| Q# | Answer(s) | Explanation | Source | Difficulty |
|----|-----------|-----------:|--------|------------|
| 1 | B | N/A | Contrast between the limitations of the local backend and the capabilities of a remote S3 backend | Easy |
| 2 | B | N/A | Contrast between the plan-only and apply forms of the refresh-only flag | Easy |
| 3 | B | N/A | Contrast between the cloud block and the legacy remote backend for connecting to HCP Terraform | Easy |
| 4 | B | N/A | Contrast between the two init flags used when changing a backend configuration | Medium |
| 5 | B | N/A | Contrast between the purpose and effect of terraform state mv and terraform state rm | Medium |
| 6 | B | N/A | Contrast between workspace-specific variables and variable sets in HCP Terraform | Medium |
| 7 | B | N/A | Contrast between a speculative plan run and a plan-and-apply run in HCP Terraform | Medium |
| 8 | B | N/A | Contrast between the granular log variables and the combined TF_LOG variable | Medium |
| 9 | B | N/A | Contrast between Sentinel and OPA as the two policy enforcement frameworks in HCP Terraform | Medium |
| 10 | A, B | N/A | Contrasting TWO of the three HCP Terraform policy enforcement levels | Medium |
| 11 | B | N/A | Contrast between organisation-level Owner role and workspace-level Admin permission in HCP Terraform | Medium |
| 12 | A, B | N/A | Contrasting TWO workflow differences between the declarative import block (Terraform 1.5+) and the legacy terraform import CLI command | Hard |
| 13 | B | N/A | Deep contrast between dynamic OIDC-based provider authentication and static credential storage in HCP Terraform workspaces | Hard |
