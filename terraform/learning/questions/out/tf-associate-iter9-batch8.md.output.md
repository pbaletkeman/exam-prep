# Terraform Associate Exam Questions

---

### Question 1

**Difficulty:** Easy
**Answer Type:** one
**Topic:** `terraform.tfstate.backup` — which statement is TRUE?

Which of the following statements about the `terraform.tfstate.backup` file is TRUE?

A) `terraform.tfstate.backup` maintains a complete version history of every `terraform apply` ever run — Terraform appends a new entry on every apply, so you can recover any earlier state by reading back through the file's history
B) `terraform.tfstate.backup` stores only the **most recent previous state** — it is overwritten on every `terraform apply` with the prior state, meaning it holds exactly one snapshot; for full version history across multiple applies, you need a backend that supports versioning (such as S3 with object versioning enabled, or HCP Terraform)
C) `terraform.tfstate.backup` is created only when Terraform detects that resources will be destroyed — it is a safety copy made automatically before any destructive operation; non-destructive applies do not update the backup file
D) `terraform.tfstate.backup` is stored in `.terraform/` alongside provider plugins and module cache — it is an internal Terraform file and should never be inspected or modified directly by operators

---

### Question 2

**Difficulty:** Easy
**Answer Type:** one
**Topic:** `terraform state list` vs `terraform state show` — which statement is TRUE?

Which of the following statements about `terraform state list` and `terraform state show` is TRUE?

A) `terraform state list` and `terraform state show` are aliases for the same command — both display all attributes for every resource currently tracked in state; the only difference is that `terraform state show` uses a condensed single-line format
B) `terraform state list` outputs ALL resource addresses currently tracked in state (e.g., `aws_vpc.main`, `module.networking.aws_subnet.public`) — it provides a full index of managed resources but shows NO attribute values; `terraform state show <address>` outputs ALL attribute key-value pairs for ONE specific resource at the given address, displaying the same information Terraform stores in state for that resource
C) `terraform state list` requires a resource address argument — without it, the command returns an error because Terraform cannot determine which resource to list
D) `terraform state show` is not a standard subcommand of `terraform state` — attributes for a specific resource are viewed using `terraform inspect <address>` instead

---

### Question 3

**Difficulty:** Easy
**Answer Type:** many
**Topic:** HCP Terraform state storage — which TWO statements are TRUE?

Which TWO of the following statements about how HCP Terraform stores Terraform state are TRUE?

A) HCP Terraform stores state remotely for every workspace — state is encrypted at rest and in transit; each workspace has its own completely independent state file that is isolated from all other workspaces in the organisation
B) HCP Terraform automatically versions all state — a full history of every state version for every workspace is retained; operators can view the version history and roll back to any previous state version directly from the HCP Terraform UI or API
C) HCP Terraform's remote state storage is built on top of the AWS S3 backend — organisations must first provision an S3 bucket in their own AWS account and provide HCP Terraform with write access before remote state can be activated for a workspace
D) All workspaces within the same HCP Terraform organisation share a single logical state file — HCP Terraform uses resource namespacing internally to prevent resource address collisions, but the underlying state is a single shared document

---

### Question 4

**Difficulty:** Medium
**Answer Type:** one
**Topic:** `terraform state rm` — which statement is FALSE?

Which of the following statements about `terraform state rm` is FALSE?

A) `terraform state rm` removes the specified resource from Terraform's state file, but takes NO action against the actual cloud resource — the infrastructure object (EC2 instance, S3 bucket, etc.) continues to exist in the cloud completely unaffected; after the command runs, Terraform no longer tracks or manages that resource
B) A common use case for `terraform state rm` is deliberately abandoning management of a resource that should be preserved — for example, removing a database from state before deleting the Terraform configuration, so that `terraform destroy` does not attempt to delete the database
C) `terraform state rm aws_instance.web` destroys the EC2 instance in AWS — removing a resource from state is equivalent to destroying it because Terraform treats a resource absent from state as if it has never been provisioned and will attempt to recreate it on the next `terraform apply`
D) After running `terraform state rm aws_s3_bucket.media`, a subsequent `terraform plan` will show the bucket as a resource to be created — because the bucket is no longer in state, Terraform treats it as new infrastructure that needs to be provisioned, even though the bucket already exists in AWS

---

### Question 5

**Difficulty:** Medium
**Answer Type:** one
**Topic:** `terraform_remote_state` data source — which statement is TRUE?

Which of the following statements about the `terraform_remote_state` data source is TRUE?

A) The `terraform_remote_state` data source can access any attribute of any resource in the remote state file — for example, you can read `data.terraform_remote_state.vpc.outputs.aws_vpc.main.id` to directly access the VPC resource's ID without the remote configuration needing to expose it as an output
B) The `terraform_remote_state` data source requires the remote state to be stored in HCP Terraform — it does not work with self-managed backends like S3 or Azure Blob Storage; for cross-configuration state sharing with non-HCP backends, you must copy state values manually
C) The `terraform_remote_state` data source exposes only the **output values** declared in the remote configuration's `output` blocks — individual resource attributes are NOT directly accessible; operators who want to share infrastructure values across configurations must declare them as `output` blocks in the producing configuration; the consuming configuration then reads them as `data.terraform_remote_state.<name>.outputs.<output_name>`
D) The `terraform_remote_state` data source automatically re-triggers a plan in the consuming configuration whenever the remote state changes — HCP Terraform detects state version changes in the referenced workspace and immediately queues a run in the consuming workspace to incorporate the new values

---

### Question 6

**Difficulty:** Medium
**Answer Type:** one
**Topic:** HCP Terraform workspace execution modes — which statement is FALSE?

Which of the following statements about HCP Terraform workspace execution modes (CLI-driven, VCS-driven, API-driven) is FALSE?

A) A **VCS-driven workspace** is connected to a specific branch in a VCS repository — pushing commits to that branch automatically triggers a Terraform run in HCP Terraform; the plan runs immediately, and if auto-apply is disabled, a human must approve before apply executes
B) A **CLI-driven workspace** uses HCP Terraform as the remote execution backend — when a developer runs `terraform plan` or `terraform apply` locally, the operation streams to HCP Terraform's managed infrastructure for execution; state and the run history are stored in HCP Terraform, but the trigger comes from the developer's local CLI
C) **API-driven workspaces** have no VCS connection and no CLI trigger — all runs are initiated programmatically via HCP Terraform's API, making them suitable for custom CI/CD pipelines or external orchestration tools that need precise control over when and what Terraform runs
D) When a workspace is configured as VCS-driven, developers can also trigger additional runs directly from the `terraform apply` CLI command on their workstations — both the VCS webhook and CLI triggers are simultaneously active; HCP Terraform merges runs from both sources into a single queue using timestamp ordering

---

### Question 7

**Difficulty:** Medium
**Answer Type:** one
**Topic:** Sentinel policy enforcement levels — which statement is TRUE?

Which of the following statements about HCP Terraform's Sentinel policy enforcement levels is TRUE?

A) `advisory` enforcement blocks a run until a team member acknowledges the policy failure — the run cannot proceed automatically even if auto-apply is enabled; a human must review and dismiss the advisory before the apply phase begins
B) `soft-mandatory` enforcement blocks a run if a policy fails, but any user with at least Write permission on the workspace can override the failure and allow the run to proceed — this makes soft-mandatory suitable for team-level guardrails where workspace owners need flexibility
C) `hard-mandatory` enforcement blocks a run if a policy fails AND the failure **cannot be overridden by any user**, including organisation owners — it is the strictest enforcement level, designed for regulatory or compliance requirements that must never be bypassed under any circumstances
D) All three enforcement levels (`advisory`, `soft-mandatory`, `hard-mandatory`) apply the same way regardless of whether the policy framework is Sentinel or OPA — the enforcement level is a run-level setting, not a policy-level setting, so a single enforcement level governs all policies that evaluate during a run

---

### Question 8

**Difficulty:** Medium
**Answer Type:** one
**Topic:** OPA (Rego) vs Sentinel as policy frameworks — which statement is TRUE?

Which of the following statements about HCP Terraform's support for policy-as-code frameworks is TRUE?

A) HCP Terraform supports only HashiCorp Sentinel for policy enforcement — OPA (Open Policy Agent) integration is available only in Terraform Enterprise on-premise deployments, not in the SaaS HCP Terraform product
B) Sentinel and OPA are both supported in HCP Terraform — Sentinel uses the proprietary HashiCorp Sentinel DSL, while OPA uses the Rego language developed by the Open Policy Agent community; organisations can use either or both frameworks simultaneously in their policy sets, and the same three enforcement levels (`advisory`, `soft-mandatory`, `hard-mandatory`) apply to policies written in either language
C) OPA policies in HCP Terraform use HCL syntax for consistency with the rest of the Terraform toolchain — since OPA was contributed to the Cloud Native Computing Foundation (CNCF) by HashiCorp, its policy language was aligned with HCL to reduce the learning curve for existing Terraform operators
D) When both Sentinel and OPA policies are configured in an organisation, Sentinel policies always evaluate first — if any Sentinel policy blocks a run, OPA policies are skipped entirely; this precedence ordering is fixed and cannot be changed in the policy set configuration

---

### Question 9

**Difficulty:** Medium
**Answer Type:** one
**Topic:** HCP Terraform health assessments (drift detection) — which statement is TRUE?

Which of the following statements about HCP Terraform health assessments is TRUE?

A) HCP Terraform health assessments automatically apply drift corrections — when a scheduled health assessment detects that a cloud resource has drifted from its Terraform-managed state, HCP Terraform immediately queues and auto-approves an apply to restore the resource to its defined configuration; no human action is required
B) Health assessments detect infrastructure drift by running `terraform plan -refresh-only` on a configurable schedule — the assessment queries cloud provider APIs to check current resource attribute values against what Terraform has in state; any differences are flagged as drift; results are visible in the HCP Terraform UI and notifications can be sent; the assessment does NOT apply any changes — it is purely observational
C) Health assessments are available in all HCP Terraform tiers starting from the free tier — drift detection is enabled by default for all workspaces and cannot be disabled without contacting HashiCorp support
D) Health assessments require Sentinel policy sets to be configured for the workspace — drift detected during an assessment is evaluated against active policies, and if no policies are defined, the assessment exits immediately without reporting any results

---

### Question 10

**Difficulty:** Medium
**Answer Type:** many
**Topic:** HCP Terraform workspace RBAC — which TWO statements are TRUE?

Which TWO of the following statements about HCP Terraform's role-based access control (RBAC) model are TRUE?

A) HCP Terraform defines four workspace-level permission tiers: **Read** (view runs, state, and variables), **Plan** (trigger speculative plans), **Write** (trigger runs and approve applies), and **Admin** (manage workspace settings, variables, VCS connections, and team access) — each tier is a superset of the permissions below it
B) In HCP Terraform, access permissions are assigned per individual user for each workspace — there is no concept of a team or group; every user must be individually granted a workspace permission level; this per-user model is the only way to manage access
C) A HCP Terraform **team token** provides API authentication that carries the access level of the team it represents — CI/CD pipelines can use a single team token to authenticate and trigger plans and applies across all workspaces the team has been granted Write access to, without needing individual user credentials
D) HCP Terraform's workspace permission model has two levels only: Read and Write — there are no intermediate levels; the Plan-only and Admin tiers described in documentation are legacy terms that map to Read and Write respectively in the current platform

---

### Question 11

**Difficulty:** Medium
**Answer Type:** one
**Topic:** `terraform state mv` — which statement is FALSE?

Which of the following statements about `terraform state mv` is FALSE?

A) `terraform state mv` updates resource addresses within the state file — it is the correct tool to use when you rename a resource block in configuration (e.g., changing `resource "aws_instance" "old_name" {}` to `resource "aws_instance" "new_name" {}`) without wanting Terraform to destroy and recreate the resource
B) `terraform state mv aws_instance.old aws_instance.new` renames the cloud EC2 instance in AWS — the command sends an API call to the AWS provider that updates the instance's Name tag and associated identifier to reflect the new Terraform resource name; this is why the command is called "move"
C) After running `terraform state mv aws_instance.old aws_instance.new`, a subsequent `terraform plan` should show "No changes" — because the state address now matches the resource block address in configuration, Terraform sees no difference between desired and actual state for that resource
D) `terraform state mv` can also move a resource into a child module — for example, `terraform state mv aws_vpc.main module.networking.aws_vpc.main` updates the state address to reflect that the resource is now managed inside the `networking` module, without affecting the real VPC in AWS

---

### Question 12

**Difficulty:** Hard
**Answer Type:** one
**Topic:** Four statements about local Terraform workspaces vs HCP Terraform workspaces — only ONE is TRUE

Four statements about Terraform workspaces are presented below. Which is the ONLY TRUE statement?

A) Terraform OSS workspaces (`terraform workspace new`, `terraform workspace select`) and HCP Terraform workspaces are the same underlying feature — both create isolated environments with separate state, variables, execution environments, and RBAC; the only distinction is where the state is hosted (local filesystem vs HCP Terraform cloud); migrating from OSS workspaces to HCP Terraform requires only changing the backend block
B) Terraform OSS workspaces are a **state segregation feature within a single backend and a single configuration** — all OSS workspaces in a configuration set share the same `.tf` files and differ only in their state files; HCP Terraform workspaces, by contrast, are fully isolated environments with independent state, **separate variable sets** (including environment variables), run history, access permissions, and execution infrastructure; the two concepts share the word "workspace" but represent fundamentally different models; using OSS workspaces is not the same as using HCP Terraform
C) When connected to HCP Terraform via a `cloud` block, running `terraform workspace new staging` creates a temporary staging copy of the configuration that is automatically discarded after the next `terraform apply` on the production workspace — the staging workspace acts as a short-lived preview environment managed entirely by HCP Terraform with no further operator action needed
D) Local `terraform workspace select prod` and HCP Terraform workspace selection are identical operations — selecting a workspace in either context causes Terraform to immediately trigger a speculative plan against the selected workspace and display the current difference between local configuration and the workspace's remote state; this plan preview is required before any subsequent `terraform apply`

---

### Question 13

**Difficulty:** Hard
**Answer Type:** one
**Topic:** Four statements about dynamic provider credentials (OIDC) in HCP Terraform — only ONE is TRUE

Four statements about HCP Terraform dynamic provider credentials are presented below. Which is the ONLY TRUE statement?

A) Dynamic provider credentials in HCP Terraform work only with AWS — Azure and GCP require static long-lived credentials (service account keys or client secrets) stored as workspace environment variables, because those providers' identity platforms use proprietary token formats incompatible with the OIDC protocol that HCP Terraform generates
B) Dynamic provider credentials are enabled by default for all new HCP Terraform workspaces — no additional configuration is required; every workspace automatically uses OIDC authentication with whatever cloud provider is detected from the provider block in the configuration
C) Dynamic provider credentials use OIDC (OpenID Connect) to issue a **short-lived token for each individual run** — instead of storing a static access key or service account credential in workspace variables, HCP Terraform's identity acts as an OIDC provider; the cloud provider (AWS, Azure, or GCP) is configured to trust tokens from HCP Terraform; when a run starts, HCP Terraform requests a short-lived credential by exchanging its OIDC token; this eliminates long-lived static credentials from workspace variables entirely and creates a per-run audit trail
D) Dynamic provider credentials require Terraform Enterprise — HCP Terraform SaaS does not support OIDC-based authentication because the multi-tenant architecture of the SaaS platform prevents the OIDC handshake required between HCP Terraform's identity service and external cloud provider IAM systems

## Answer Key

| Q# | Answer(s) | Explanation | Source | Difficulty |
|----|-----------|-----------:|--------|------------|
| 1 | B | ** `terraform.tfstate.backup` is a single-snapshot safety net — not a rolling history. Before every successful `terraform apply`, Terraform copies the current `terraform.tfstate` into `terraform.tfstate.backup`, then overwrites `terraform.tfstate` with the new state. The result is that `terraform.tfstate.backup` always contains the state from the apply *before* the most recent one — exactly one previous snapshot. If you run 10 applies, the backup only reflects apply 9 (the state that existed before apply 10 ran). For full version history, you need either S3 with versioning enabled (every state file write becomes a new S3 object version) or HCP Terraform (which versions all state automatically). Option A is false — there is no append-style history. Option C is false — the backup is created on every apply regardless of the operation type. Option D is false — the backup file lives in the working directory alongside `terraform.tfstate`, not inside `.terraform/`. | ** `terraform.tfstate.backup` — which statement is TRUE? | ** Easy |
| 2 | B | ** The two commands serve complementary purposes: `terraform state list` is a directory-style command — it outputs all resource addresses tracked in state, one per line, with no attribute detail. It accepts an optional pattern for filtering (e.g., `terraform state list module.networking.*`). `terraform state show <address>` is a detail command — it takes a single resource address and prints all of that resource's attribute values as they are recorded in state, formatted as HCL-like output. Together they form a common debugging workflow: use `list` to find what addresses are tracked, then use `show` to inspect a specific resource's values. Option A is false — the commands are distinct. Option C is false — `terraform state list` with no arguments lists ALL resources without filtering. Option D is false — `terraform state show` is a real, well-documented command; `terraform inspect` is not a Terraform command. | ** `terraform state list` vs `terraform state show` — which statement is TRUE? | ** Easy |
| 3 | A, B | ** **(A)** is TRUE. Each HCP Terraform workspace has its own fully isolated state file stored on HCP Terraform's infrastructure — encrypted at rest and in transit — completely independent of all other workspaces. There is no state sharing between workspaces unless explicitly configured via the `terraform_remote_state` data source. **(B)** is TRUE. HCP Terraform automatically maintains a complete version history of every state change for every workspace. Operators can navigate the version history, inspect any prior state version, and initiate a rollback directly from the workspace's States tab in the UI — no manual versioning configuration is required. **(C)** is FALSE. HCP Terraform manages its own state storage infrastructure — organisations do NOT need to provision or manage S3 buckets or any other storage infrastructure for HCP Terraform's state. The S3 backend is an alternative for organisations hosting their own state in AWS. **(D)** is FALSE. Workspaces do NOT share a single state file — full workspace isolation is one of HCP Terraform's core features and a key reason organisations use it for multi-environment management. | ** HCP Terraform state storage — which TWO statements are TRUE? | ** Easy |
| 4 | C | ** Option C is FALSE. `terraform state rm` ONLY modifies the local state file — it has zero effect on cloud infrastructure. The EC2 instance (or any other resource) continues running unaffected in AWS after `terraform state rm` removes it from state. Terraform state operations (`state rm`, `state mv`, `state show`) are strictly state management tools; they never call provider APIs to create, modify, or destroy cloud resources. The second half of option C is accurate (Terraform treats a resource absent from state as new and plans to create it), but the first claim — that `state rm` destroys the cloud resource — is completely false. This distinction is critical: if you want to destroy the cloud resource, use `terraform destroy -target=aws_instance.web`; if you want to stop managing it WITHOUT destroying it, use `terraform state rm`. Options A, B, and D are all TRUE statements about `terraform state rm` behaviour. | ** `terraform state rm` — which statement is FALSE? | ** Medium |
| 5 | C | ** The `terraform_remote_state` data source provides access ONLY to values that have been explicitly declared as `output` blocks in the remote (producing) Terraform configuration. Individual resource attributes — even ones that exist in state — are NOT directly readable. This design is intentional: it creates a well-defined interface contract between configurations. The producing configuration exposes `output "vpc_id" { value = aws_vpc.main.id }`, and the consuming configuration reads `data.terraform_remote_state.networking.outputs.vpc_id`. This access boundary also enforces the principle of least privilege — a consuming configuration cannot accidentally read sensitive attributes from the remote state unless the producer explicitly outputs them. Option A is false — you cannot traverse into resource objects in remote state directly. Option B is false — `terraform_remote_state` works with any backend that supports state storage (S3, Azure Blob, GCS, local, etc.). Option D describes a real HCP Terraform feature (run triggers), but it is not how `terraform_remote_state` itself behaves. | ** `terraform_remote_state` data source — which statement is TRUE? | ** Medium |
| 6 | D | ** Option D is FALSE. VCS-driven and CLI-driven are **mutually exclusive workspace modes** — a workspace is configured as one or the other, not both simultaneously. A VCS-driven workspace has VCS integration enabled; it responds to VCS webhook events and does NOT accept CLI-triggered runs. Conversely, a CLI-driven workspace does not have a VCS connection and only accepts runs initiated from a local `terraform plan`/`terraform apply`. This mutual exclusivity is intentional: mixing CLI and VCS triggers on the same workspace would create unpredictable run ordering and make it impossible to enforce code-review gates. Option A correctly describes VCS-driven workspace behaviour. Option B correctly describes CLI-driven workspace behaviour (remote execution, local CLI trigger). Option C correctly describes API-driven workspaces. | ** HCP Terraform workspace execution modes — which statement is FALSE? | ** Medium |
| 7 | C | ** **(C)** is TRUE. `hard-mandatory` is the most restrictive Sentinel (and OPA) enforcement level — a policy failure at this level permanently blocks the run and the failure cannot be overridden by anyone, including organization owners. This makes it appropriate for strict compliance requirements such as "all S3 buckets must have encryption enabled" or "VPCs must not have public subnets." Option A is false — `advisory` is the least restrictive level; it shows a warning but does NOT block the run; the apply proceeds automatically. Option B is false — `soft-mandatory` can be overridden, but only by users with specific elevated permissions (typically organization owners or users with the Override Policy Checks capability); workspace Write permission is NOT sufficient to override a soft-mandatory failure. Option D is false — enforcement levels are set per-policy (within the policy set configuration), not as a run-level setting; different policies in the same policy set can have different enforcement levels. | ** Sentinel policy enforcement levels — which statement is TRUE? | ** Medium |
| 8 | B | ** **(B)** is TRUE. HCP Terraform supports two distinct policy-as-code frameworks: Sentinel (using HashiCorp's proprietary Sentinel DSL) and OPA (using Rego, the policy language from the Open Policy Agent project). Organizations can adopt either or both — policy sets can contain Sentinel policies, OPA policies, or a mix. All three enforcement levels apply uniformly across both frameworks. Option A is false — OPA IS supported in HCP Terraform (not just Terraform Enterprise). Option C is false — OPA uses **Rego**, not HCL. OPA is a CNCF project developed by Styra (not HashiCorp), and its Rego language is purpose-built for policy evaluation with its own syntax unrelated to HCL. Option D is false — there is no fixed evaluation precedence between Sentinel and OPA policies; the ordering is not defined as Sentinel-first; policies from both frameworks are evaluated as part of the same policy check phase. | ** OPA (Rego) vs Sentinel as policy frameworks — which statement is TRUE? | ** Medium |
| 9 | B | ** HCP Terraform health assessments are a scheduled drift-detection mechanism. Internally, they execute the equivalent of `terraform plan -refresh-only` against the workspace on a configurable interval. The operation queries cloud provider APIs, compares the live resource attributes to what is stored in Terraform state, and identifies any attributes that have changed outside of Terraform (e.g., a security group rule added manually in the console). Results are displayed in the workspace's Health tab in the HCP Terraform UI, and webhook or email notifications can be configured for detected drift. Crucially, health assessments are **read-only** — they NEVER automatically apply corrections. Drift remediation always requires a deliberate human decision to queue and approve a run. Option A is false — there is no auto-apply of corrections. Option C is false — health assessments are a paid tier feature and are not enabled by default; they must be configured. Option D is false — health assessments operate completely independently of Sentinel or OPA policy sets. | ** HCP Terraform health assessments (drift detection) — which statement is TRUE? | ** Medium |
| 10 | A, C | ** **(A)** is TRUE. HCP Terraform defines four workspace permission levels, and each is a superset of the one below: Read → Plan → Write → Admin. Read allows viewing state and run history; Plan adds the ability to trigger speculative (plan-only) runs; Write adds the ability to queue and approve full runs; Admin adds workspace configuration management including variable management, VCS connections, and team access control. **(C)** is TRUE. Team tokens are a first-class HCP Terraform feature for CI/CD. A team token represents the collective access of a team — if the team has Write permission on five workspaces, a CI/CD pipeline authenticating with the team token can trigger runs on all five workspaces. This is the recommended pattern for automated pipelines, avoiding the security risk of using personal user tokens. **(B)** is FALSE — HCP Terraform has a full team-based RBAC model; permissions are assigned to teams, and users are added to teams; individual per-user assignment is also supported but teams are the primary mechanism. **(D)** is FALSE — there are definitely four distinct permission levels, not just Read and Write; Plan and Admin are real, active permission tiers with meaningful capability differences. | ** HCP Terraform workspace RBAC — which TWO statements are TRUE? | ** Medium |
| 11 | B | ** Option B is FALSE. `terraform state mv` ONLY modifies the Terraform state file — it does NOT contact any cloud provider or send any API calls to AWS (or any other provider). The cloud resource (the EC2 instance) is completely unchanged: its AWS instance ID, name, configuration, and running state are all unaffected. `terraform state mv` is purely a state management operation that updates the address under which Terraform tracks a resource. The command is used to fix address mismatches that would otherwise cause Terraform to plan a destroy-and-recreate cycle. After running `state mv`, the resource continues to exist in AWS exactly as before, but Terraform now tracks it under the new address. Option A correctly describes the primary use case. Option C correctly describes the expected outcome of a successful state move. Option D correctly describes a valid module-to-module or root-to-module state move. | ** `terraform state mv` — which statement is FALSE? | ** Medium |
| 12 | B | ** **(B)** is the ONLY TRUE statement. This is one of the most commonly confused topics in the Terraform Associate exam. Terraform OSS workspaces (managed with the `terraform workspace` CLI commands against a standard backend) are simply a mechanism for maintaining **multiple named state files** within the same backend configuration. All workspaces in the set share the exact same `.tf` configuration code and backend; they differ only in which state file is active. There is no variable isolation, no permission model, no run history, and no execution environment separation between OSS workspaces. HCP Terraform workspaces are an entirely different concept — each workspace is a fully isolated operational environment. The shared terminology ("workspace") is a historical naming overlap that causes confusion. Option A is false — OSS workspaces and HCP Terraform workspaces are NOT the same feature; they differ in virtually every dimension except the name. Option C is false — `terraform workspace new staging` on a cloud-block configuration creates a new HCP Terraform workspace (a persistent environment), not a temporary preview; it has nothing to do with auto-discard behaviour. Option D is false — selecting a workspace does NOT automatically trigger a plan; you must explicitly run `terraform plan` after selecting a workspace. | ** Four statements about local Terraform workspaces vs HCP Terraform workspaces — only ONE is TRUE | ** Hard |
| 13 | C | ** **(C)** is the ONLY TRUE statement. Dynamic provider credentials (also called "Workload Identity" in some cloud provider contexts) use the OIDC protocol to replace static long-lived credentials with short-lived, per-run tokens. The mechanism: (1) the cloud provider (AWS, Azure, or GCP) is configured to trust tokens issued by HCP Terraform's OIDC endpoint; (2) when a run starts, HCP Terraform's identity service generates a JWT token (the OIDC token) for that specific workspace and run; (3) HCP Terraform exchanges this token with the cloud provider for a short-lived cloud credential (e.g., temporary AWS credentials via AssumeRoleWithWebIdentity); (4) the run uses these short-lived credentials for provider API calls; they expire when the run ends. The result: no static `AWS_ACCESS_KEY_ID` or Azure client secret stored in workspace variables, and a complete per-run audit trail in the cloud provider's IAM logs. Option A is false — dynamic provider credentials support AWS, Azure, AND GCP. Option B is false — OIDC authentication requires explicit configuration of both the cloud provider's trust policy AND the HCP Terraform workspace settings; it is not enabled automatically. Option D is false — dynamic provider credentials ARE supported in HCP Terraform SaaS; this is a current, documented feature of the HCP Terraform platform. | ** Four statements about dynamic provider credentials (OIDC) in HCP Terraform — only ONE is TRUE | ** Hard |
