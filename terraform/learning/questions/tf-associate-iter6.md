# Terraform Associate (004) — Question Bank Iter 6 Batch 1

**Iteration**: 6
**Iteration Style**: Scenario-based troubleshooting — an engineer encounters a problem or unexpected outcome; identify the most likely cause and correct resolution
**Batch**: 1
**Objective**: 1 — IaC Concepts
**Generated**: 2026-04-25
**Total Questions**: 13
**Difficulty Split**: 3 Easy / 8 Medium / 2 Hard
**Answer Types**: 10 `one` / 3 `many` / 0 `none`

---

# Terraform Associate (004) — Question Bank Iter 6 Batch 2

**Iteration**: 6
**Iteration Style**: Scenario-based troubleshooting — an engineer encounters a problem or unexpected outcome; identify the most likely cause and correct resolution
**Batch**: 2
**Objective**: 2 — Terraform Fundamentals (Providers & State)
**Generated**: 2026-04-25
**Total Questions**: 13
**Difficulty Split**: 3 Easy / 8 Medium / 2 Hard
**Answer Types**: 10 `one` / 3 `many` / 0 `none`

---

# Terraform Associate (004) — Question Bank Iter 6 Batch 3

**Iteration**: 6
**Iteration Style**: Scenario-based troubleshooting — an engineer encounters a problem or unexpected outcome; identify the most likely cause and correct resolution
**Batch**: 3
**Objective**: 3 — Core Workflow & CLI
**Generated**: 2026-04-25
**Total Questions**: 13
**Difficulty Split**: 3 Easy / 8 Medium / 2 Hard
**Answer Types**: 10 `one` / 3 `many` / 0 `none`

---

# Terraform Associate (004) — Question Bank Iter 6 Batch 4

**Iteration**: 6
**Iteration Style**: Scenario-based troubleshooting — an engineer encounters a problem or unexpected outcome; identify the most likely cause and correct resolution
**Batch**: 4
**Objective**: 4a — Resources, Data & Dependencies
**Generated**: 2026-04-25
**Total Questions**: 13
**Difficulty Split**: 3 Easy / 8 Medium / 2 Hard
**Answer Types**: 10 `one` / 3 `many` / 0 `none`

---

# Terraform Associate (004) — Question Bank Iter 6 Batch 5

**Iteration**: 6
**Iteration Style**: Scenario-based troubleshooting — an engineer encounters a problem or unexpected outcome; identify the most likely cause and correct resolution
**Batch**: 5
**Objective**: 4b — Variables, Outputs, Types & Functions
**Generated**: 2026-04-25
**Total Questions**: 13
**Difficulty Split**: 3 Easy / 8 Medium / 2 Hard
**Answer Types**: 10 `one` / 3 `many` / 0 `none`

---

# Terraform Associate (004) — Question Bank Iter 6 Batch 6

**Iteration**: 6
**Iteration Style**: Scenario-based troubleshooting — an engineer encounters a problem or unexpected outcome; identify the most likely cause and correct resolution
**Batch**: 6
**Objective**: 4c — Custom Conditions & Sensitive Data
**Generated**: 2026-04-25
**Total Questions**: 13
**Difficulty Split**: 3 Easy / 8 Medium / 2 Hard
**Answer Types**: 10 `one` / 3 `many` / 0 `none`

---

# Terraform Associate (004) — Question Bank Iter 6 Batch 7

**Iteration**: 6
**Iteration Style**: Scenario-based troubleshooting — an engineer encounters a problem or unexpected outcome; identify the most likely cause and correct resolution
**Batch**: 7
**Objective**: 5 — Terraform Modules
**Generated**: 2026-04-25
**Total Questions**: 13
**Difficulty Split**: 3 Easy / 8 Medium / 2 Hard
**Answer Types**: 10 `one` / 3 `many` / 0 `none`

---

# Terraform Associate (004) — Question Bank Iter 6 Batch 8

**Iteration**: 6
**Iteration Style**: Scenario-based troubleshooting — an engineer encounters a problem or unexpected outcome; identify the most likely cause and correct resolution
**Batch**: 8
**Objective**: 6/7/8 — State Backends, Locking, Importing & HCP Terraform
**Generated**: 2026-04-25
**Total Questions**: 13
**Difficulty Split**: 3 Easy / 8 Medium / 2 Hard
**Answer Types**: 10 `one` / 3 `many` / 0 `none`

---

---

## Questions

---

### Question 1 — Duplicate Resources From a Shell Script

**Difficulty**: Easy
**Answer Type**: one
**Topic**: Understanding why an imperative provisioning script is not idempotent and how Terraform's declarative model avoids the same problem

**Question**:
An engineer has been provisioning S3 buckets by running a shell script that calls `aws s3api create-bucket --bucket my-data-bucket`. After running the script on Monday and again on Friday (forgetting the first run), a second bucket was attempted. The engineer asks: "Could I have avoided this by writing the bucket in a Terraform configuration instead?" What is the most accurate answer?

- A) No — Terraform would also attempt to create a second bucket because it has no memory of what was created before
- B) No — Terraform only manages EC2 and VPC resources natively; S3 requires a separate tool
- C) Yes — a Terraform resource block is **declarative**: on the second apply, Terraform compares desired state to current state, detects the bucket already exists, and makes no changes; the shell script is **imperative** and executes the create command unconditionally every time it is run
- D) Yes — but only if the engineer runs `terraform import` first to register the bucket with Terraform before either apply

**Answer**: C

**Explanation**:
The shell script is imperative — it issues a direct "create" command and has no awareness of whether the resource already exists. Running it twice attempts to create the resource twice. Terraform's declarative model operates differently: the configuration file describes *what should exist*, and Terraform queries the provider to determine whether it already does. If the S3 bucket is already present and matches the configuration, Terraform reports no changes needed. This idempotent behaviour — applying the same configuration N times always yields the same outcome — is one of the central reasons IaC tools like Terraform are preferred over ad-hoc scripting for infrastructure management.

---

### Question 2 — Manual Console Change Reverted by Terraform

**Difficulty**: Easy
**Answer Type**: one
**Topic**: Understanding that Terraform enforces desired state and will revert manual changes on the next apply

**Question**:
An engineer manually changes an EC2 instance's instance type from `t3.micro` to `t3.large` using the AWS console. The Terraform configuration still declares `instance_type = "t3.micro"`. A colleague then runs `terraform apply`. The engineer is surprised to see the instance type change back to `t3.micro`. What explains this behaviour?

- A) Terraform detected the console change as a security violation and triggered an automatic rollback
- B) Terraform uses the **configuration file as the source of desired state** — the configuration still declares `t3.micro`, so Terraform plans and applies a change to bring the current state back in line with the desired state, effectively reverting the manual change
- C) Running `terraform apply` always rolls back the last 24 hours of changes as a safety measure
- D) The colleague accidentally ran `terraform destroy` and `terraform apply` in sequence

**Answer**: B

**Explanation**:
This is drift remediation in action. During `terraform plan` (which runs at the start of `terraform apply`), Terraform refreshes the current state by querying the AWS API and discovers the instance type is now `t3.large`. The configuration, however, declares `t3.micro`. Because the configuration is the authoritative desired state, Terraform plans to change the instance type back to `t3.micro` and applies it. This behaviour is intentional and desirable in a managed environment — the configuration is the single source of truth, and manual console changes will be overwritten on the next apply. Teams that use Terraform should commit to the discipline of making all infrastructure changes through configuration, not the console.

---

### Question 3 — Engineer Confused by "No Changes" Message

**Difficulty**: Easy
**Answer Type**: one
**Topic**: Recognising that "No changes" is the correct idempotent outcome — not an error or a skipped step

**Question**:
A junior engineer runs `terraform apply` and receives the message: `No changes. Your infrastructure matches the configuration.` They open a support ticket reporting: "Terraform is broken — it skipped creating my resources." The configuration was applied successfully the previous day by another engineer. What should the support engineer explain?

- A) The junior engineer is correct — `No changes` indicates Terraform encountered an error and aborted before creating any resources
- B) Terraform requires a `--force` flag on subsequent applies to re-create resources that already exist
- C) "No changes" is the **expected, correct outcome** of running `terraform apply` when the current infrastructure already matches the configuration — Terraform detected that all declared resources already exist in the correct state and correctly took no action; this is called idempotency
- D) The message indicates the state file is corrupted — the engineer should delete `terraform.tfstate` and re-apply

**Answer**: C

**Explanation**:
`No changes. Your infrastructure matches the configuration.` is one of the most important messages in Terraform — it means everything is working exactly as designed. Terraform compared the desired state (configuration files) to the current state (state file, validated against the cloud provider) and found no differences. All declared resources already exist with the correct attributes. This idempotent property is fundamental to IaC: you can safely run `terraform apply` at any time and it will only make changes if the infrastructure has actually diverged from the configuration. The junior engineer's confusion is common among those new to declarative tools — they expect "apply" to always *do* something.

---

### Question 4 — Direct State File Edit

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Understanding why directly editing terraform.tfstate is dangerous and what the file's actual role is

**Question**:
An engineer wants to "manually add" a resource that was created outside of Terraform. They open `terraform.tfstate` in a text editor, copy an existing resource block, and paste a modified version with the new resource's attributes. They then run `terraform plan`. What is the most likely problem with this approach?

- A) There is no problem — editing the state file directly is the recommended way to onboard manually created resources
- B) The state file uses a format that Terraform regenerates automatically; any manual edits will be ignored on the next `terraform init`
- C) Editing the state file directly is **fragile and unsupported** — state is in a structured JSON format with checksums and schema versioning; an incorrect edit can corrupt state, causing Terraform to misidentify resources, plan unnecessary destroys, or fail entirely; the correct approach is to use the `import` block or `terraform import` CLI to bring the resource under management properly
- D) Terraform will accept the manual state edit but will immediately destroy the resource because there is no matching resource block in the `.tf` configuration files

**Answer**: C

**Explanation**:
`terraform.tfstate` is a structured JSON file that Terraform manages internally — it is not intended to be hand-edited. It contains checksums, serial numbers, schema versions, and provider metadata that must be consistent. A manual edit that misses any of these details can corrupt the file, potentially causing Terraform to plan destructive operations or fail to run at all. More importantly, the state file is not the *configuration* — adding an entry to state without a corresponding resource block in a `.tf` file means Terraform will see the state entry and either ignore it or (depending on the Terraform version and configuration) plan to remove it. The correct path for onboarding an existing resource is `terraform import` (CLI) or the declarative `import` block (Terraform 1.5+), which both validate the resource against provider schema and add it to state safely.

---

### Question 5 — Resource Deleted From Config Gets Planned for Destruction

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Understanding that Terraform owns resources it manages and plans to destroy them when removed from configuration

**Question**:
An engineer removes a `resource "aws_security_group" "allow_ssh"` block from their Terraform configuration. They did not intend to delete the security group — they just wanted to "stop managing it with Terraform." When they run `terraform plan`, they see `1 to destroy`. What explains this, and what should the engineer do instead?

- A) `terraform plan` is wrong — removing a block from configuration never causes a destroy in Terraform; the engineer should open a bug report
- B) Removing a resource block from configuration signals to Terraform that the resource should no longer exist — Terraform plans to destroy it; to **stop managing a resource without destroying it**, the engineer should instead run `terraform state rm aws_security_group.allow_ssh` to remove it from state, after which Terraform will no longer track it and the cloud resource will remain untouched
- C) The engineer should run `terraform apply -target=aws_security_group.allow_ssh` to skip the security group during apply
- D) Removing a resource block only causes a destroy if `prevent_destroy = false` is set in the lifecycle block; without a lifecycle block, removal is safe

**Answer**: B

**Explanation**:
When a resource block exists in state but is absent from the configuration, Terraform interprets this as intent to remove the resource — the desired state no longer includes it, so Terraform plans to destroy it. This is the correct behaviour for the common case (you genuinely want to delete the infrastructure). However, when the goal is to "hand off" management — keep the resource running but stop Terraform from tracking it — the right tool is `terraform state rm <address>`. This removes the resource from Terraform's state without touching the cloud resource. After this, the resource becomes unmanaged drift: Terraform no longer knows about it and will not create, update, or destroy it. The engineer should also remove the resource block from the configuration (or leave it out) to avoid Terraform trying to create a new one.

---

### Question 6 — Staging Drifted from Production

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Identifying which IaC benefit directly addresses environment drift between staging and production

**Question**:
A company has a production environment and a staging environment. Both were originally set up manually via the AWS console. Over six months, engineers have made small ad-hoc changes to each independently. The production team is now seeing bugs that cannot be reproduced in staging because the two environments have diverged significantly. Which IaC benefit most directly addresses this class of problem?

- A) **Speed** — IaC tools provision resources faster than manual console clicks, so environments can be rebuilt more quickly
- B) **Audit trail** — storing infrastructure in version control lets engineers see a history of every change
- C) **Repeatability** — the same Terraform configuration applied to both environments produces identical infrastructure in each; any manual change that drifts an environment from the configuration will be detected and corrected on the next apply, preventing long-term divergence
- D) **Cost estimation** — IaC tools calculate the cost difference between environments so discrepancies can be identified

**Answer**: C

**Explanation**:
The root cause of the staging/production divergence is that neither environment has a shared, version-controlled definition of its desired state — each was built and modified manually and independently. **Repeatability** is the IaC benefit that solves this: a single Terraform configuration applied against both environments (with environment-specific variables for names, sizing, etc.) ensures both are built from the same specification. Any manual drift is detected on the next `terraform plan` and corrected on `terraform apply`. While an audit trail (B) would help trace *how* the divergence occurred, it does not prevent it. Repeatability — the ability to reproducibly create identical environments from code — is the fundamental fix.

---

### Question 7 — Plan Output Shows "1 to add" but the Resource Is in the Config

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Understanding why terraform plan shows a resource as "to add" even though it is declared in configuration

**Question**:
A Terraform configuration declares an `aws_instance` resource. The engineer runs `terraform plan` and sees `Plan: 1 to add, 0 to change, 0 to destroy.` They are confused — the instance already exists in AWS, they can see it in the console. What is the most likely explanation?

- A) Terraform always plans to add all declared resources on the first plan — the `1 to add` is a display artefact and no resource will actually be created on apply
- B) The instance exists in AWS but has **not been imported into Terraform state** — Terraform has no record of it in state, so from Terraform's perspective the desired state (the resource block) is unfulfilled; Terraform will create a second new instance unless the existing instance is first imported
- C) The `aws_instance` resource type is deprecated and Terraform is planning to recreate it using an updated resource type
- D) This means the state file is locked — Terraform is re-planning an earlier failed apply

**Answer**: B

**Explanation**:
Terraform's planning is based on its **state file**, not direct cloud observation alone. When an instance exists in AWS but has never been managed by Terraform (no entry in state), Terraform has no knowledge of it. The configuration declares it should exist, state says it doesn't, so Terraform plans to create it. Running `terraform apply` would create a second, duplicate instance alongside the existing one. To correct this, the engineer should import the existing instance using the `import` block or `terraform import aws_instance.<name> <instance-id>`, which adds the instance to state and allows Terraform to manage it going forward. After a successful import, `terraform plan` should show no changes if the configuration attributes match the actual instance.

---

### Question 8 — Colleague Claims CloudFormation Is Better for Multi-Cloud

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Recognising Terraform's multi-cloud advantage over provider-specific IaC tools

**Question**:
An engineer proposes using AWS CloudFormation to manage all company infrastructure because it is a "mature, native AWS service." A colleague argues that Terraform would be a better choice given that the company also has workloads on Azure and GCP. What is the most accurate reason to favour Terraform in this scenario?

- A) Terraform is faster than CloudFormation because it uses a compiled language under the hood, while CloudFormation uses interpreted JSON
- B) **CloudFormation is AWS-only** — it cannot provision Azure or GCP resources; Terraform uses provider plugins and a single unified workflow to manage resources across AWS, Azure, GCP, and many other platforms, making it the natural choice for organisations with multi-cloud or hybrid-cloud infrastructure
- C) Terraform replaces CloudFormation entirely — AWS itself recommends migrating all existing CloudFormation stacks to Terraform
- D) CloudFormation requires separate credentials for each AWS region; Terraform uses a single credential set for all regions and all cloud providers

**Answer**: B

**Explanation**:
CloudFormation is a highly capable IaC tool but is architecturally scoped to AWS. It cannot provision Azure virtual machines, GCP storage buckets, or resources in any non-AWS provider. Terraform's plugin-based architecture means providers exist for AWS, Azure, GCP, Kubernetes, Datadog, GitHub, and hundreds of other platforms — all managed through the same HCL syntax and workflow. A company with workloads on AWS and Azure would need two separate tools (CloudFormation + ARM/Bicep) if they chose provider-native tools, while Terraform provides a single unified workflow. This is one of Terraform's defining advantages. The same applies to Azure Bicep/ARM (Azure-only) — each provider-native tool is limited to its cloud.

---

### Question 9 — Three Benefits of Migrating From ClickOps to IaC

**Difficulty**: Medium
**Answer Type**: many
**Topic**: Identifying valid IaC benefits over manual console-based provisioning

**Question**:
A company is evaluating a migration from "ClickOps" (provisioning via cloud console) to Terraform-based IaC. Which THREE of the following are genuine benefits they should cite in their proposal? (Select three.)

- A) **Repeatability** — the same Terraform configuration can be applied to create identical staging, production, and disaster-recovery environments without manual steps, eliminating environment drift
- B) **Audit trail** — every infrastructure change is a version-controlled commit with author, timestamp, and diff, enabling full change history and compliance traceability
- C) **Guaranteed zero downtime** — Terraform performs all changes in a blue-green pattern that ensures no service interruption during apply
- D) **Disaster recovery** — if an environment is destroyed, it can be recreated from the configuration files in minutes, without manually remembering every resource and setting
- E) **Elimination of all cloud provider costs** — IaC tools negotiate lower cloud rates by batching API calls to the provider

**Answer**: A, B, D

**Explanation**:
(A) Repeatability is a core IaC benefit — the same code produces the same infrastructure every time, across any environment. (B) Version-controlled commits are the IaC answer to "who changed what and when?" — something ClickOps cannot provide. (D) Disaster recovery is dramatically improved by IaC: an entire environment can be reconstructed from configuration files rather than reconstructed from memory and scattered documentation. (C) is incorrect — Terraform has no zero-downtime guarantee; some resource changes (e.g., replacing a database instance) cause downtime, and blue-green deployments must be designed explicitly. (E) is entirely false — Terraform is an orchestration tool with no influence over cloud pricing.

---

### Question 10 — Engineer Confused by "1 to change" vs "1 to add" in Plan

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Understanding what terraform plan's "to add", "to change", and "to destroy" counts mean for in-place vs replace operations

**Question**:
An engineer modifies an existing EC2 instance's `tags` attribute in the configuration and runs `terraform plan`. The plan shows `Plan: 0 to add, 1 to change, 0 to destroy.` The engineer expected to see `1 to add` because they were "adding a tag." What is the correct interpretation of `1 to change`?

- A) `1 to change` means Terraform will destroy the instance and create a new one with the updated tags
- B) `1 to change` means the **existing resource will be updated in place** — Terraform will call the provider API to modify the tag on the running instance without destroying or recreating it; this is an in-place update; `1 to add` would mean a brand new resource would be created that does not currently exist in state
- C) `1 to change` means the change is optional — the engineer can skip it by running `terraform apply -skip-changes`
- D) `1 to change` is shown only when `count` or `for_each` is used; for single resources, the plan always shows `1 to add` regardless of whether the resource exists

**Answer**: B

**Explanation**:
Terraform's plan output uses three categories that directly map to API operations. `to add` (or `to create`) means a resource does not exist and will be created. `to change` (or `to update`) means the resource exists and one or more of its attributes will be modified in place — the resource continues to exist throughout. `to destroy` means the resource will be deleted. The engineer was confused because "adding a tag" feels like creating something new, but from Terraform's perspective the *resource* (the EC2 instance) already exists and is simply being modified. The tag update is an attribute change, not a new resource — hence `1 to change`. A fourth category, `(replace)`, appears when a required attribute change forces destruction and recreation of the resource.

---

### Question 11 — Why Does Plan Re-Run on `terraform apply`?

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Understanding that terraform apply always performs a fresh plan to account for changes that may have occurred since the last plan

**Question**:
An engineer runs `terraform plan` and reviews the output carefully. They then run `terraform apply` immediately after. To their surprise, Terraform runs a planning phase again before asking for confirmation. The engineer asks: "Why is Terraform planning again? I just ran plan!" What is the correct explanation?

- A) This is a bug — `terraform apply` should use the output from the previous `plan` command without re-running
- B) `terraform apply` **always performs a fresh plan** before applying because infrastructure may have changed in the time between `terraform plan` and `terraform apply` — a colleague could have applied changes, a resource could have been manually modified, or a plan file could have been applied elsewhere; the fresh plan ensures Terraform acts on the actual current state, not a potentially stale snapshot
- C) The plan phase runs again only when the configuration files have been modified since the last `terraform plan`
- D) Terraform re-plans because `terraform plan` does not save its results — each command is stateless

**Answer**: B

**Explanation**:
By default, `terraform apply` always runs a fresh plan immediately before applying. The reason is safety: the state of cloud infrastructure can change between the time `terraform plan` was run and the time `terraform apply` executes. A teammate could have run their own apply, a resource could have been manually modified, or an automated process could have changed something. If Terraform used a stale plan from minutes (or hours) ago, it might apply changes that are no longer appropriate. To skip the re-plan and use an exact saved plan, the engineer should run `terraform plan -out=plan.tfplan` to save the plan to a file, then `terraform apply plan.tfplan` to apply that specific plan without re-planning. This two-step pattern is also recommended in CI/CD pipelines for deterministic applies.

---

### Question 12 — Renamed Resource Block Causes Destroy and Recreate

**Difficulty**: Hard
**Answer Type**: many
**Topic**: Understanding that renaming a resource label causes plan to show destroy + create, and knowing TWO ways to handle this correctly

**Question**:
An engineer renames a resource block in their configuration from `resource "aws_instance" "web"` to `resource "aws_instance" "web_server"`. When they run `terraform plan`, they see `Plan: 1 to add, 0 to change, 1 to destroy.` The engineer does not want to destroy and recreate the instance. Which TWO approaches correctly resolve this? (Select two.)

- A) Run `terraform state mv aws_instance.web aws_instance.web_server` **before** running `terraform apply` — this updates the state entry to reference the new name, so Terraform sees the renamed block as the same resource and plans zero changes instead of destroy + create
- B) Add a `moved` block to the configuration declaring that `aws_instance.web` has moved to `aws_instance.web_server` — Terraform 1.1+ supports `moved` blocks as a declarative way to inform Terraform of refactors, causing it to update state during apply without destroying the resource
- C) Run `terraform apply -target=aws_instance.web_server` to create the new resource first, then manually delete the old one from the console
- D) Add `prevent_destroy = true` to the lifecycle block of `aws_instance.web_server` — this prevents the destroy and causes Terraform to skip the create as well

**Answer**: A, B

**Explanation**:
When a resource block is renamed, Terraform sees a new address (`aws_instance.web_server`) with no state entry and an old address (`aws_instance.web`) in state with no configuration block. This is interpreted as "destroy the old, create the new." To avoid destroy + recreate: **(A) `terraform state mv`** imperatively updates the state file to use the new address before apply runs — when Terraform then plans, it sees both the configuration block and state entry under `aws_instance.web_server` and recognises them as the same resource, planning no changes. This is the pre-1.1 approach and still valid. **(B) `moved` block** is the declarative equivalent introduced in Terraform 1.1: you add a `moved { from = aws_instance.web; to = aws_instance.web_server }` block to the configuration, and Terraform processes the refactor during the next apply, updating state without any destroy/create. After the moved block has been applied, it can be removed. (C) is a manual workaround that would still cause downtime. (D) is incorrect — `prevent_destroy` prevents destruction but does not suppress the create; it would cause the apply to error.

---

### Question 13 — IaC as Living Documentation

**Difficulty**: Hard
**Answer Type**: one
**Topic**: Understanding the documentation benefit of IaC and the limits of that claim in a scenario where config and reality have diverged

**Question**:
A new engineer joins a team and is told: "Our Terraform configuration files are our infrastructure documentation — you can read the `.tf` files to understand exactly what we have deployed." Six months later, the engineer discovers that the actual cloud environment contains several resources not present in the configuration. What is the most precise statement about the "living documentation" claim of IaC, and what condition is required for it to remain true?

- A) The claim is always false — configuration files describe intent, not actual infrastructure; real documentation must be maintained separately
- B) Terraform configuration files are accurate documentation **only for the resources Terraform manages** — the claim holds when all infrastructure changes flow through Terraform with no manual console changes, no resources created outside Terraform, and no state manipulation that removes resources from tracking; when engineers bypass Terraform (ClickOps, other tools, manual `terraform state rm`), the configuration no longer reflects reality and the documentation value is lost
- C) The claim is fully accurate regardless of manual changes — Terraform automatically discovers all cloud resources during `terraform plan` and adds them to the configuration
- D) Configuration files are only reliable documentation after running `terraform refresh` — between refreshes, they may be outdated

**Answer**: B

**Explanation**:
"Infrastructure as living documentation" is a genuine and significant benefit of IaC — but it is **conditional**, not automatic. The configuration accurately documents the infrastructure exactly as long as Terraform is the *exclusive* method of change. The moment an engineer creates a resource via the console, modifies one manually, or uses another provisioning tool, the configuration and reality diverge. Terraform cannot retroactively discover and add unmanaged resources to configuration files (it can detect drift for *managed* resources, but cannot auto-import new ones). Maintaining the documentation value requires organisational discipline: all infrastructure changes go through version-controlled Terraform configuration, pull request review, and `terraform apply`. The scenario describes a team that violated this discipline, which is a common real-world challenge when adopting IaC in an existing environment.

---

---

## Questions

---

### Question 1 — Providers Not Found After Cloning

**Difficulty**: Easy
**Answer Type**: one
**Topic**: Understanding that terraform init is required after cloning before any other terraform commands

**Question**:
A new engineer clones a Terraform repository and runs `terraform validate` to check the configuration syntax. Terraform returns an error saying the provider plugins are not installed. The engineer's configuration has a valid `required_providers` block. What is the most likely cause and fix?

- A) The `required_providers` block is missing a `version` constraint — Terraform cannot validate without an exact version specified
- B) `terraform validate` requires elevated OS permissions to read provider plugins — the engineer should run the command as an administrator
- C) The engineer has not run **`terraform init`** — until `terraform init` is executed in the working directory, no provider plugins are downloaded; the `.terraform/providers/` directory does not exist yet; running `terraform init` will download the required providers and allow validation (and apply) to proceed
- D) The engineer must manually download the provider binary from the Terraform Registry and place it in the `.terraform/` directory

**Answer**: C

**Explanation**:
`terraform init` is the mandatory first step in any Terraform workflow. It reads the `required_providers` block, downloads the specified provider plugins from the Terraform Registry into `.terraform/providers/`, and creates or updates the `.terraform.lock.hcl` dependency lock file. No other Terraform command (`validate`, `plan`, `apply`) can function without the provider plugins being present. When cloning an existing repository, the `.terraform/` directory is intentionally absent from version control (it belongs in `.gitignore`), so every new clone requires a fresh `terraform init` before anything else.

---

### Question 2 — Unexpected Provider Upgrade Breaks a Pipeline

**Difficulty**: Easy
**Answer Type**: one
**Topic**: Understanding the role of .terraform.lock.hcl in preventing unintended provider upgrades

**Question**:
A CI pipeline runs `terraform init` and `terraform plan` on every pull request. After a new AWS provider minor version is released, the pipeline starts failing with API compatibility errors — but no configuration files have changed. What is the most likely cause?

- A) The CI pipeline is running `terraform init -upgrade` by default, which always installs the latest provider regardless of constraints
- B) The `.terraform.lock.hcl` file is **not committed to version control** — without it, each `terraform init` run resolves the newest version matching the constraint; when the new provider version was released, the pipeline installed it automatically, introducing the API compatibility issue; committing `.terraform.lock.hcl` would pin the exact version and prevent unintended upgrades
- C) The `required_providers` block uses `>=` instead of `~>`, which always installs the absolute latest provider version regardless of major version boundaries
- D) CI pipelines cannot use `.terraform.lock.hcl` — lock files only work on developer machines

**Answer**: B

**Explanation**:
`.terraform.lock.hcl` records the exact provider version (and cryptographic hash) that was installed, ensuring every subsequent `terraform init` — on any machine, in any CI system — installs the same version rather than re-resolving from scratch. When the lock file is absent from version control, `terraform init` is free to pick the newest version satisfying the constraint. As soon as a new provider version is published, the next CI run installs it. If that version introduced a breaking change or API behaviour difference, the pipeline breaks without any code change. The fix is straightforward: commit `.terraform.lock.hcl` to the repository alongside the `.tf` files. Use `terraform init -upgrade` intentionally when you want to advance the locked version.

---

### Question 3 — Provider Alias Configurations Deployed to Wrong Region

**Difficulty**: Easy
**Answer Type**: one
**Topic**: Understanding that provider alias must be explicitly referenced in a resource block or Terraform uses the default provider

**Question**:
An engineer configures two AWS provider blocks — one for `us-east-1` (default) and one for `eu-west-1` (with `alias = "europe"`). They intend to create an S3 bucket in `eu-west-1` but forget to add `provider = aws.europe` to the resource block. After `terraform apply`, they find the bucket was created in `us-east-1`. What explains this?

- A) Terraform randomly selects a provider configuration for each resource; the engineer got unlucky
- B) The `alias = "europe"` configuration is ignored unless a `region` argument is also added to the resource block
- C) When a resource block does **not specify a `provider` meta-argument**, Terraform uses the **default (non-aliased) provider configuration** — in this case `us-east-1`; aliased providers are only used when explicitly referenced with `provider = aws.europe` in the resource block
- D) Terraform always uses the last declared provider block; since the `eu-west-1` block was declared second, it should have been used

**Answer**: C

**Explanation**:
Provider aliases exist so that multiple configurations of the same provider (e.g., multiple AWS regions) can coexist. The provider block without an `alias` is the **default** — it is used by any resource that does not explicitly specify a provider. Aliased providers are intentionally opt-in: a resource must declare `provider = aws.europe` (using the format `<provider_type>.<alias>`) to use the aliased configuration. Without this declaration, the resource silently falls back to the default provider, which in this case is `us-east-1`. The fix is to add `provider = aws.europe` to the S3 bucket resource block.

---

### Question 4 — State File Deleted Accidentally

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Understanding the consequences of losing the state file and the recovery path

**Question**:
An engineer accidentally deletes `terraform.tfstate` from a project using a local backend. The actual AWS infrastructure (several EC2 instances, a VPC, and S3 buckets) still exists. When the engineer runs `terraform plan`, Terraform proposes creating all the resources from scratch. What explains this, and what is the correct recovery path?

- A) Terraform proposes creating resources because it detected the missing state file and automatically marked all resources for replacement; the engineer should run `terraform apply` to proceed
- B) Terraform's plan is based on **state**, not direct cloud observation during planning — with no state file, Terraform sees no known resources and plans to create everything to match the configuration; the correct recovery is to **import each existing resource** using `import` blocks or the `terraform import` CLI, which re-establishes the state file entries so Terraform knows what already exists; after importing, `terraform plan` should show no changes
- C) The plan is safe to apply — Terraform detects existing resources before creating them and will skip any that already exist
- D) The engineer should restore the state file from `.terraform.tfstate.backup` which Terraform keeps permanently as a full history

**Answer**: B

**Explanation**:
State is Terraform's only record of what infrastructure it manages. When the state file is deleted, Terraform's known state is empty — it has no record that the EC2 instances, VPC, or S3 buckets exist. During planning, Terraform compares the configuration (desired state) to the known state (empty) and concludes everything needs to be created. Running `terraform apply` at this point would attempt to create duplicate resources alongside the existing ones — most would fail (e.g., S3 bucket names are globally unique, VPC CIDR conflicts) while others might partially succeed. The recovery path is to import each existing resource, which writes the resource ID and attributes back into state. Once all resources are imported, `terraform plan` should show no changes. This scenario also illustrates why remote state with versioning (S3 + versioning, HCP Terraform) is critical for production: deleted or corrupted state can be recovered from a prior version.

---

### Question 5 — terraform.tfstate.backup Not a Full History

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Understanding that .backup holds only the immediately previous state, not a full version history

**Question**:
An engineer's team relies on `terraform.tfstate.backup` as their state history strategy. They run `terraform apply` on Monday (apply 1), Wednesday (apply 2), and Friday (apply 3). On Friday evening they discover a serious misconfiguration introduced on Wednesday. They try to restore the state from `.backup`. What problem will they encounter?

- A) No problem — `.terraform.tfstate.backup` retains the last 30 days of state history as rotated snapshots
- B) `terraform.tfstate.backup` contains the state from before the **most recent apply only** — it holds the state from after apply 2 (Wednesday), not after apply 1 (Monday); there is no built-in mechanism to recover the state from before Wednesday; this is why production teams use remote backends with versioning (e.g., S3 with versioning enabled) or HCP Terraform, which retain a full state version history
- C) `.terraform.tfstate.backup` cannot be restored — it is a read-only audit file
- D) Terraform replaces `.terraform.tfstate.backup` only when a destroy is run — the file still contains the state from before apply 1

**Answer**: B

**Explanation**:
`terraform.tfstate.backup` is a single file that Terraform overwrites with the **previous** state before every apply. After apply 3 (Friday), the backup contains the state from after apply 2 (Wednesday) — the state from Monday was overwritten on Wednesday. There is only ever one backup, not a history. For production environments, this single-file backup is insufficient: it cannot recover from a configuration error introduced two applies ago. The solution is a remote backend with native versioning: S3 with versioning enabled keeps every state version indefinitely, and HCP Terraform maintains a full state version history with the ability to roll back to any prior version. This is one of the primary motivations for moving to a remote backend.

---

### Question 6 — Sensitive Output Visible in State

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Understanding that sensitive=true masks terminal output but does not protect state

**Question**:
A security auditor reviews a Terraform project and raises a finding: "The database password is stored in plaintext in the state file." The team responds: "We marked the output as `sensitive = true`, so the password is protected." Is the team's response correct, and what is the actual security posture?

- A) The team is correct — `sensitive = true` encrypts the value in the state file using AES-256
- B) The team is incorrect — **`sensitive = true` only suppresses the value in terminal output and plan output**; it does NOT encrypt or redact the value in `terraform.tfstate`; all resource attributes, including passwords and secrets, are stored in the state file in plaintext regardless of sensitivity markings; the correct protection is to store state in an **encrypted remote backend** (e.g., S3 with `encrypt = true`, or HCP Terraform which encrypts state at rest automatically)
- C) The team is correct — `sensitive = true` on a variable also prevents Terraform from writing the value to state
- D) The team is partially correct — `sensitive = true` encrypts the value in state using the provider's encryption key, but the key is stored next to the state file

**Answer**: B

**Explanation**:
`sensitive = true` is a display control, not a security control. When a variable, local, or output is marked sensitive, Terraform redacts the value in plan output (`(sensitive value)`) and terminal output — preventing accidental exposure in logs and console sessions. However, this marking has zero effect on the state file. Every attribute of every managed resource is written to `terraform.tfstate` in plaintext JSON, including passwords returned by database providers, private keys generated by key pair resources, and any other sensitive attributes. The security auditor is correct. The proper mitigation is two-fold: (1) use an encrypted remote backend so the state file at rest is encrypted, and (2) consider using a secrets manager (Vault, AWS Secrets Manager) to retrieve credentials dynamically rather than storing them in Terraform config or state at all.

---

### Question 7 — Plan is Slower Than Expected

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Understanding that terraform plan refreshes live state via API and how -refresh=false can speed it up

**Question**:
An engineer manages 500 resources in a single Terraform workspace. `terraform plan` takes over 10 minutes because Terraform is making hundreds of API calls. The engineer asks: "Is there a way to speed up planning when I'm confident the state is accurate?" What is the correct approach?

- A) Split the resources across multiple state files — Terraform cannot plan efficiently with more than 100 resources in a single state
- B) Use `terraform plan -refresh=false` — this **skips the live API refresh phase** and plans based solely on the cached values in the state file; when the engineer has recently applied and is confident the state accurately reflects reality (no manual changes have occurred), this flag dramatically reduces planning time by eliminating all provider API calls during the plan
- C) Run `terraform plan -parallelism=1` to reduce API throttling — the default parallelism causes the slowdown
- D) Upgrade to Terraform Enterprise — community Terraform has a hard limit of 100 API calls per plan

**Answer**: B

**Explanation**:
During a standard `terraform plan`, Terraform calls the cloud provider API to refresh the current state of every tracked resource — this is the "refresh" phase. For workspaces with hundreds of resources, this generates many API calls and can take a significant amount of time (and may trigger provider API rate limits). `terraform plan -refresh=false` skips this refresh entirely, planning based on the values cached in the state file. This is appropriate when the engineer has just applied and is confident no out-of-band changes have occurred. It is not appropriate when drift detection is important. A middle ground is `terraform plan -target=<specific_resource>` to limit the scope, or workspaces divided by team or environment to keep individual workspace sizes manageable.

---

### Question 8 — Two Provider Version Changes After Lock File Update

**Difficulty**: Medium
**Answer Type**: many
**Topic**: Identifying TWO correct statements about the effects of running terraform init -upgrade

**Question**:
A team's `.terraform.lock.hcl` currently pins the AWS provider to `5.20.0`. The `required_providers` constraint is `~> 5.0`. AWS provider `5.40.0` is now available. An engineer runs `terraform init -upgrade`. Which TWO statements correctly describe what happens? (Select two.)

- A) `terraform init -upgrade` **re-resolves all provider versions** against the current constraints and installs the newest version that satisfies each constraint — in this case, `5.40.0` replaces `5.20.0` because it satisfies `~> 5.0`
- B) The `.terraform.lock.hcl` file is **updated to record the new version `5.40.0`** and its cryptographic hashes — the lock file must be committed to version control so teammates get the upgraded version on their next `terraform init`
- C) `terraform init -upgrade` ignores version constraints and always installs the absolute latest provider version available, even if it violates the `required_providers` constraint
- D) Running `terraform init -upgrade` automatically runs `terraform apply` to ensure the upgraded provider is compatible with the current state

**Answer**: A, B

**Explanation**:
(A) `-upgrade` instructs `terraform init` to ignore the currently locked versions and re-resolve against the declared constraints, installing the newest satisfying version. Without `-upgrade`, `terraform init` respects the lock file and installs exactly the pinned version. (B) After upgrading, the lock file is rewritten with the new version and hashes. Committing this update is essential — teammates running `terraform init` (without `-upgrade`) will then get `5.40.0` from the lock file. (C) is incorrect — `-upgrade` still respects `required_providers` constraints; `6.0.0` would not be installed because it violates `~> 5.0`. (D) is incorrect — `terraform init -upgrade` only manages provider installation; it never triggers an apply.

---

### Question 9 — `terraform show` Reports Different Values Than the Console

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Understanding why terraform show may reflect stale state if terraform refresh/plan has not been run

**Question**:
An engineer runs `terraform show` to check the public IP of an EC2 instance. The output shows `54.1.2.3`. They then check the AWS console and see the instance's public IP is `54.9.9.9` — the instance was stopped and restarted, which assigned a new IP. Why does `terraform show` display the old IP?

- A) `terraform show` always shows the IP from when the instance was first created and never updates
- B) `terraform show` displays the values **stored in the local state file** — state is only updated when Terraform runs a plan or apply that includes a refresh; the instance was restarted outside Terraform, so the state file still contains the old IP (`54.1.2.3`); running `terraform plan` or `terraform apply -refresh-only` will query the AWS API, detect the changed IP, and update the state file, after which `terraform show` will reflect `54.9.9.9`
- C) `terraform show` is a deprecated command that reads from a cached snapshot taken at install time
- D) The discrepancy means the instance is now unmanaged — Terraform lost track of it when it was restarted

**Answer**: B

**Explanation**:
`terraform show` reads from the **state file** — it displays the last-known attribute values that Terraform recorded during its most recent plan or apply. When the EC2 instance was stopped and restarted outside of Terraform (a manual action or an AWS auto-recovery event), the IP changed at the cloud level but Terraform was not involved and therefore did not update its state. The state file still holds `54.1.2.3`. Running `terraform plan` causes Terraform to refresh state by querying the AWS EC2 API — it will detect the IP change and update the state file accordingly. After that, `terraform show` will display the new IP. This also illustrates why state should be thought of as Terraform's "last-known-good" snapshot rather than a real-time view of infrastructure.

---

### Question 10 — Provider Source Address Produces 404 on Init

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Diagnosing a provider init failure caused by a malformed source address

**Question**:
An engineer adds a third-party provider to their configuration with this source address:

```hcl
required_providers {
  datadog = {
    source  = "DataDog/datadog"
    version = "~> 3.0"
  }
}
```

`terraform init` fails with: `Failed to query available provider packages: Could not retrieve the list of available versions for provider DataDog/datadog`. The provider exists on the public Terraform Registry. What is the most likely cause?

- A) The Terraform Registry is temporarily unavailable — the engineer should retry later
- B) The `version` constraint `~> 3.0` is invalid — a patch version is required (e.g., `~> 3.0.0`)
- C) **Provider source addresses are case-sensitive** — the namespace on the Terraform Registry is `DataDog` with a capital D; however Terraform normalises namespace lookups to lowercase; the actual issue is that the registry namespace is `datadog` (all lowercase); the correct source address is `"datadog/datadog"` and `terraform init` is sending a query with the wrong casing, which resolves to a 404
- D) Third-party providers cannot be declared in `required_providers` — they must be installed manually

**Answer**: C

**Explanation**:
Terraform Registry provider namespaces and types are case-insensitive in the Registry lookup, but practical experience shows that using the incorrect casing in the source address can cause lookup failures depending on the Terraform version and registry endpoint behaviour. More broadly, the correct canonical source address for the Datadog provider as listed on the public registry is `datadog/datadog` (all lowercase). Any deviation — whether incorrect casing, a GitHub URL, or a misspelling — causes `terraform init` to query a path that doesn't exist on the registry, resulting in a 404-style failure. The fix is to use the exact source address from the provider's page on registry.terraform.io, which for Datadog is `datadog/datadog`.

---

### Question 11 — `terraform state push` Used Carelessly in Recovery

**Difficulty**: Hard
**Answer Type**: one
**Topic**: Understanding the dangers of terraform state push and the safer alternatives

**Question**:
During an incident, an engineer attempts to recover from a corrupted remote state by running `terraform state push ./old-backup.tfstate` without fully understanding its effect. A senior engineer stops them urgently. What is the specific danger of this command in this scenario?

- A) `terraform state push` is not a real Terraform command — it does not exist and would return an error
- B) `terraform state push` is dangerous because it **overwrites the current remote state file entirely with whatever local file is provided**, with no merge or diff — pushing an old backup would discard any state changes made since that backup was taken, potentially causing Terraform to lose track of resources created after the backup, which would lead to duplicate resource creation or unmanaged drift on the next apply; the safer alternatives are using the remote backend's native versioning (S3 versioned bucket, HCP Terraform state history) to roll back to a specific prior version under controlled conditions
- C) The danger is that `terraform state push` requires elevated cloud provider permissions that the engineer does not have — it will silently fail and report success
- D) `terraform state push` pushes state to all workspaces simultaneously, potentially corrupting unrelated environments

**Answer**: B

**Explanation**:
`terraform state push` is a low-level escape hatch that uploads a local state file directly to the configured remote backend, **replacing** the remote state entirely. It bypasses all safety checks (no plan, no confirmation) and the pushed file becomes the new authoritative state. If the backup being pushed is outdated, Terraform will have no record of any resources created or modified since that backup — on the next plan, it will propose to create them again (or leave them as unmanaged drift if the config has also changed). This is a destructive operation that can cause significant infrastructure and state inconsistency. The correct approach during an incident is to use the remote backend's versioning feature to roll back to a specific prior state version (e.g., via S3 version history or HCP Terraform's state versions UI), which provides a controlled, audited rollback without overwriting the entire state in one untested step.

---

### Question 12 — Multiple Problems When Two Engineers Apply Simultaneously

**Difficulty**: Hard
**Answer Type**: many
**Topic**: Identifying TWO consequences of running terraform apply concurrently without state locking

**Question**:
Two engineers on a team using a local backend both run `terraform apply` at the same time against the same infrastructure. Neither apply errors immediately. Which TWO consequences are most likely? (Select two.)

- A) The **state file becomes corrupted or inconsistent** — both apply processes may read the same initial state, each compute their own diff, and both write their own version of the updated state file, with the second write potentially overwriting changes recorded by the first; the result is a state file that no longer accurately reflects all the resources that were created or modified
- B) **Duplicate resources may be created** — if both processes plan to create the same resource (because neither sees the other's in-progress work in state), both may attempt to provision it; some provider APIs will create a second resource rather than erroring, leaving orphaned infrastructure not tracked by state
- C) The local backend automatically detects concurrent access and queues the second apply to run after the first completes safely
- D) Both applies will succeed cleanly — the local backend uses OS-level file locking to serialise concurrent access reliably across all operating systems

**Answer**: A, B

**Explanation**:
The local backend has no reliable cross-process state locking. Two concurrent applies against a local state file create a classic read-modify-write race condition. **(A)** Each process reads the current state, computes a plan, executes changes, and then writes its updated state. The second write will overwrite the first, potentially discarding the records of resources the first apply created — the state becomes a partial view of reality. **(B)** If both processes plan to create the same resource (e.g., both see `count = 1` for a resource not yet in state), both may attempt to create it. Some cloud APIs create a second resource without error; others fail. Either outcome is problematic. This is the primary reason teams must use a remote backend with proper locking (DynamoDB for S3, native locking for HCP Terraform) — locking serialises applies and prevents both consequences.

---

### Question 13 — `terraform state pull` to Inspect Remote State

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Understanding the correct use case for terraform state pull when inspecting or backing up remote state

**Question**:
A team uses an S3 remote backend. An engineer wants to inspect the raw state file to debug an unexpected plan output but does not have direct S3 bucket access. What is the correct Terraform-native approach?

- A) Run `terraform show -json` — this streams the remote state file to stdout in JSON format with full attribute details
- B) Run **`terraform state pull`** — this **downloads the current remote state from the configured backend and writes it to stdout**; the engineer can pipe the output to a file (`terraform state pull > debug.tfstate`) or parse it with `jq` for inspection; it uses the Terraform credentials and backend configuration to authenticate, so no direct S3 access is required
- C) Run `terraform plan -json` — this includes the full state file in the plan output
- D) The engineer must request direct S3 access — there is no Terraform command that can retrieve remote state

**Answer**: B

**Explanation**:
`terraform state pull` is the correct tool for this scenario. It authenticates using the backend configuration (S3 bucket, key, region, and IAM role or credentials as configured) and downloads the current state file, writing it to stdout. The engineer can redirect this to a local file for inspection (`terraform state pull > state-debug.json`) and then use tools like `jq` to query specific resources and attributes. This is also the recommended approach for creating a manual backup before a risky state manipulation (`terraform state mv`, `terraform state rm`). `terraform show` (A) reads from local state or a saved plan file and does not fetch remote state in the same way. `terraform plan -json` (C) includes plan details but not the full raw state. Direct S3 access (D) works but requires bucket-level permissions that bypass Terraform's access control layer.

---

---

## Questions

---

### Question 1 — CI Pipeline Fails Because Files Are Not Formatted

**Difficulty**: Easy
**Answer Type**: one
**Topic**: Using terraform fmt -check in CI to enforce formatting without writing files

**Question**:
A team's CI pipeline runs `terraform fmt` as a formatting gate. A developer notices that every time the pipeline runs, it reformats the committed files and then reports a diff that must be manually committed. The team wants the pipeline to **report a failure** when files are unformatted rather than silently rewrite them. What is the correct flag to use?

- A) `terraform fmt -dry-run` — preview changes without writing to disk
- B) `terraform fmt -no-write` — display unformatted files without modifying them
- C) `terraform fmt -check` — this flag makes `terraform fmt` **exit with a non-zero exit code** if any `.tf` files need reformatting, without writing any changes to disk; the CI pipeline fails on the non-zero exit, prompting the developer to format their code locally and recommit; this is the standard CI usage of `fmt`
- D) `terraform fmt -validate` — combines formatting and validation in a single pass

**Answer**: C

**Explanation**:
`terraform fmt -check` is the CI-friendly form of the command. Without `-check`, `terraform fmt` rewrites files in place — useful locally but counterproductive in CI where you want to fail fast and tell the developer to fix their code, not silently patch it in the pipeline. With `-check`, Terraform reads each `.tf` file, computes what the canonical format would be, and exits with code `1` if any file differs — without making any changes. The pipeline sees the non-zero exit code and reports a failure. Most teams also use `-recursive` to catch files in subdirectories: `terraform fmt -check -recursive`. Developers fix formatting locally (by running `terraform fmt` without `-check`) and push the corrected files.

---

### Question 2 — `terraform validate` Passes But `terraform plan` Fails

**Difficulty**: Easy
**Answer Type**: one
**Topic**: Understanding the boundary between what validate checks (static) and what plan checks (live)

**Question**:
An engineer runs `terraform validate` on a configuration that references an AMI ID: `ami = "ami-0deadbeef1234567"`. Validation passes. They then run `terraform plan` and receive an error: `InvalidAMIID.NotFound: The image id '[ami-0deadbeef1234567]' does not exist`. The engineer is confused — they thought `validate` would catch this. What explains the discrepancy?

- A) `terraform validate` only checks files in the root module; AMI references in child modules are skipped
- B) `terraform validate` is **fully offline and makes no API calls** — it checks HCL syntax and static references but cannot verify whether cloud resources such as AMI IDs actually exist; `terraform plan` calls the AWS provider API, which verifies the AMI ID against the AWS catalogue and returns the error when it is not found; `validate` passing is correct — it cannot know the AMI is invalid without querying AWS
- C) `terraform validate` found the error but suppressed it because `ami` is a computed attribute
- D) `terraform plan` is stricter than `validate` because it re-parses the `.tf` files from scratch

**Answer**: B

**Explanation**:
`terraform validate` operates entirely without network access or provider credentials. It checks whether HCL syntax is correct, all references resolve to declared symbols, argument names are valid for each resource type, and types are compatible. It cannot check whether a specific value (like an AMI ID) actually exists in the cloud — that requires a live API call. `terraform plan` invokes the provider plugin, which in turn calls the AWS EC2 API to look up the AMI ID. When the API returns a "not found" error, Terraform surfaces it as a plan failure. This is expected and correct: `validate` is a fast, offline sanity check; live resource existence is validated during planning.

---

### Question 3 — Apply Prompt Appears Unexpectedly in Automation

**Difficulty**: Easy
**Answer Type**: one
**Topic**: Using -auto-approve to suppress the interactive apply confirmation in CI/CD

**Question**:
An engineer sets up a CI/CD pipeline that runs `terraform apply` as the final step. The pipeline hangs indefinitely after printing the execution plan, waiting for user input. The engineer needs the apply to proceed automatically without prompting. What is the correct fix?

- A) Set the environment variable `TF_APPLY_AUTO=true` before running `terraform apply`
- B) Run `terraform apply -no-prompt` to skip the confirmation dialog
- C) Add **`-auto-approve`** to the `terraform apply` command — this flag suppresses the interactive confirmation prompt and applies the plan immediately; it is the standard flag for non-interactive environments such as CI/CD pipelines; without it, `terraform apply` always pauses and waits for `yes` before proceeding
- D) Use `terraform apply -force` to bypass the confirmation check

**Answer**: C

**Explanation**:
By default, `terraform apply` displays the execution plan and then pauses with the prompt `Do you want to perform these actions? Enter a value:`. This interactive step is intentional for human review but causes CI/CD pipelines to hang indefinitely because no one is there to type `yes`. The `-auto-approve` flag tells Terraform to skip the confirmation step and proceed directly with the apply. It is the standard flag for automated pipelines. Teams typically combine it with a saved plan file for fully deterministic CI runs: `terraform plan -out=plan.tfplan` in one stage, then `terraform apply plan.tfplan` (which does not prompt, because a saved plan file is provided) in the apply stage. `-auto-approve` is appropriate in that two-stage pattern as well.

---

### Question 4 — `-target` Used Regularly Causes State Drift

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Understanding why routine use of -target is an anti-pattern and what problems it causes

**Question**:
An engineer discovers they can run `terraform apply -target=aws_instance.web` to apply changes faster, skipping the other 40 resources in the configuration. They start using `-target` routinely for every change. A senior engineer warns them this is dangerous. What is the most likely problem this practice will cause over time?

- A) Using `-target` more than three times in a row permanently locks the state file
- B) `terraform apply -target` does not update the state file for the targeted resource — changes are applied to the cloud but not recorded
- C) **Routine use of `-target` causes state drift**: when only a subset of resources is planned and applied, Terraform does not evaluate the full dependency graph; changes to the targeted resource may leave dependent resources in an inconsistent or stale state that Terraform is unaware of; over time, the state file diverges from the full desired configuration, and a full `terraform apply` may plan unexpected changes or errors because the inter-resource relationships were never reconciled; `-target` is intended only for emergency recovery or one-off debugging, not routine use
- D) `-target` is deprecated in Terraform 1.x and will be removed in a future version

**Answer**: C

**Explanation**:
`terraform apply -target` is a surgical tool for emergency situations — for example, applying a fix to one broken resource while the rest of the plan has unrelated unresolved issues. HashiCorp explicitly warns against using it in normal workflows. The problem is that Terraform's dependency graph ensures resources are applied in the correct order and that dependent resources are updated when their dependencies change. When `-target` is used routinely, these cross-resource relationships are never evaluated fully. A change to a security group might affect five EC2 instances — applying only the security group leaves those instances in an unchecked state. The next full `terraform apply` may then produce a large and confusing plan because weeks of targeted applies never resolved the complete desired state. The correct practice is to always run full plans, and fix the root cause of issues that make full plans unworkable.

---

### Question 5 — Saved Plan File Applied After Configuration Change

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Understanding that a saved plan file is tied to the state and config at the time it was created

**Question**:
An engineer runs `terraform plan -out=plan.tfplan` and saves the plan. Before running `terraform apply plan.tfplan`, a colleague merges a pull request that adds a new resource to the configuration. The engineer applies the saved plan. What is the most likely problem?

- A) Terraform detects the configuration change and automatically re-plans before applying
- B) The apply fails immediately with a "plan file is out of date" error that prevents any changes from being made
- C) The **saved plan was generated against the configuration and state at the time `terraform plan` was run** — it does not include the new resource added by the colleague's PR; applying it will provision only the changes in the saved plan, not the new resource; the new resource will not be created until a fresh `terraform plan` and `terraform apply` are run; in some versions of Terraform, if the state has diverged significantly from the plan's recorded state, Terraform will also emit a warning or error
- D) The apply creates the new resource automatically because Terraform reads the current configuration files during `terraform apply plan.tfplan`

**Answer**: C

**Explanation**:
A saved plan file (`.tfplan`) captures a complete snapshot of the proposed changes at the moment `terraform plan -out` is run — the configuration, state, and intended cloud operations are all frozen into that file. Applying a saved plan does not re-read the current `.tf` files; it executes exactly what was planned. Changes made to configuration files after the plan was saved are therefore invisible to `terraform apply plan.tfplan`. The new resource will be absent from the apply. This is actually a feature in controlled pipelines (the plan is reviewed and then applied exactly as reviewed), but it requires discipline: if configuration changes occur between plan and apply, a new plan must be generated. CI/CD pipelines should always treat the plan and apply as a single atomic pipeline stage.

---

### Question 6 — `terraform graph` Output Is Unreadable

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Understanding that terraform graph outputs DOT format and requires an external tool to render

**Question**:
An engineer runs `terraform graph` to visualise the resource dependency graph. The terminal output is a large block of text that looks like this:

```
digraph {
  compound = "true"
  newrank  = "true"
  subgraph "root" {
    "[root] aws_instance.web (expand)" -> "[root] aws_security_group.allow_ssh (expand)"
  }
}
```

The engineer expects a visual diagram but sees only text. What is the correct explanation and next step?

- A) The engineer must run `terraform graph -render` to trigger the visual rendering
- B) `terraform graph` outputs the graph in **DOT format** — a plain-text graph description language used by the Graphviz tool; the text output is correct and expected; to render it as a visual diagram, the engineer should pipe the output to Graphviz: `terraform graph | dot -Tsvg > graph.svg` and then open `graph.svg` in a browser or image viewer
- C) The output indicates a circular dependency in the configuration — the `->` arrows show the cycle that must be fixed
- D) The DOT output is only generated when there are dependency errors; normal graphs are rendered as PNGs automatically

**Answer**: B

**Explanation**:
`terraform graph` produces output in the DOT language, which is a plain-text notation for directed graphs used by the Graphviz toolset. The raw output is not intended to be read directly — it describes nodes and edges in a structured text format. To produce a human-readable visual, the output must be passed to a Graphviz rendering tool such as `dot` (part of the Graphviz package). The standard pipeline is: `terraform graph | dot -Tsvg > graph.svg`. Other output formats are also supported: `-Tpng` for PNG, `-Tpdf` for PDF. Once rendered, the graph shows resource nodes connected by dependency arrows, making it easy to understand the apply order Terraform will use. This is primarily a debugging and documentation tool rather than a routine workflow step.

---

### Question 7 — `terraform output` Returns Nothing After Apply

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Understanding why terraform output returns nothing when no output blocks are declared

**Question**:
An engineer provisions infrastructure with `terraform apply`. After apply completes, they run `terraform output` expecting to see resource IDs and IP addresses, but the command prints nothing. The engineer is confused because the apply succeeded. What is the most likely cause?

- A) `terraform output` requires the `-state` flag to point to the state file — without it, the command cannot find the output values
- B) Output values are only available for 24 hours after apply; running the command the next day always returns nothing
- C) The engineer's configuration has **no `output` blocks declared** — `terraform output` can only display values that are explicitly defined in `output` blocks in the configuration; Terraform does not automatically expose resource attributes as outputs; to see the instance ID, the engineer must add an `output` block such as `output "instance_id" { value = aws_instance.web.id }` and re-apply
- D) The outputs were cleared because `terraform apply` was run with `-auto-approve`

**Answer**: C

**Explanation**:
`terraform output` reads from the `outputs` section of the state file. That section is only populated when the configuration contains `output` blocks. Terraform does not automatically export resource attributes — every value the engineer wants accessible via `terraform output` must be explicitly declared. This is by design: outputs are a structured interface for surfacing specific values (IDs, endpoints, IP addresses) without exposing the entire resource object. The fix is to add the desired `output` blocks to the configuration and run `terraform apply` (or `terraform refresh`) so the values are written to state. After that, `terraform output instance_id` will return the value.

---

### Question 8 — Plan Shows Resource Replaced When Only a Tag Changed

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Understanding that certain attributes force resource replacement and how to recognise this in plan output

**Question**:
An engineer changes only the `Name` tag on an RDS database instance and runs `terraform plan`. They expect to see `1 to change` (an in-place update) but instead see `-/+ 1 to add, 1 to destroy` with the note `# forces replacement`. The engineer is alarmed — they did not intend to recreate the database. What is the most likely explanation?

- A) Changing a tag on any AWS resource always forces a full replacement in Terraform — tag changes are never applied in place
- B) The engineer accidentally changed the `engine_version` attribute instead of the tag; engine version changes always force replacement
- C) **Some resource attributes are marked `ForceNew` in the provider schema** — changing them requires the resource to be destroyed and recreated because the underlying cloud API does not support in-place updates for that attribute; however, `Name` tags on RDS instances are not normally `ForceNew`; the most likely explanation is that the engineer also changed (intentionally or accidentally) a `ForceNew` attribute such as `identifier`, `engine`, `engine_version`, or `db_subnet_group_name` alongside the tag change; the plan output's `# forces replacement` note will list the specific attribute responsible
- D) `-/+` in the plan always means the engineer has changed more than five attributes at once, triggering a safety replacement

**Answer**: C

**Explanation**:
`-/+` (destroy then create) appears when one or more of the changed attributes are `ForceNew` in the provider's schema — meaning the underlying cloud API cannot update them on a live resource and Terraform must destroy and recreate it to apply the change. Tag changes on RDS instances are normally in-place updates (`~`), not replacements. The most reliable way to diagnose why `-/+` is appearing is to read the full plan output carefully: the specific attribute that `# forces replacement` will be identified by name in the plan. Common `ForceNew` attributes on RDS instances include `identifier`, `engine`, `engine_version`, `db_subnet_group_name`, `availability_zone`, and `allocated_storage` (in some configurations). The engineer should scroll up in the plan output to find the `# forces replacement` annotation on the specific attribute line.

---

### Question 9 — `terraform console` Used to Debug an Unexpected Expression

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Using terraform console to test and debug HCL expressions interactively before embedding in config

**Question**:
An engineer writes a complex `for` expression in their configuration but is unsure whether it produces the expected output. They keep running `terraform plan` to test it, but the plan is slow because it refreshes 300 resources each time. What is the most efficient way to test the expression in isolation?

- A) Run `terraform validate --expression` to evaluate and print the result of a single HCL expression
- B) Create a separate test `.tf` file with just the expression and run `terraform apply` on it in an empty workspace
- C) Use **`terraform console`** — an interactive REPL (Read-Eval-Print Loop) that evaluates HCL expressions against the current state and variable values without running a full plan or making any provider API calls; the engineer can type the `for` expression directly at the prompt and see the result immediately, iterating quickly until the output is correct before embedding it in the configuration
- D) Use `terraform output --eval` to evaluate an expression without declaring an output block

**Answer**: C

**Explanation**:
`terraform console` is the correct tool for this task. It opens an interactive session where any valid HCL expression can be typed and evaluated immediately. It reads the current state file (so `resource.type.name.attribute` references resolve to actual state values) and has access to all declared variables, locals, and functions. Critically, it does **not** run a plan, does not refresh provider state, and makes no API calls — it is very fast. The engineer can iteratively test the `for` expression, adjusting the logic and immediately seeing the result, without triggering a full plan cycle. Once the expression produces the expected output, it can be copied directly into the configuration. This is also useful for testing string interpolation, function calls (`cidrsubnet()`, `lookup()`, `merge()`), and type conversions before using them in resources.

---

### Question 10 — `terraform destroy` Run in Wrong Workspace

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Understanding terraform workspaces and the risk of running destructive commands in the wrong workspace

**Question**:
An engineer intends to destroy the `staging` environment. They run `terraform destroy -auto-approve` but realise halfway through that they are in the `default` workspace, which corresponds to the **production** environment. What TWO immediate actions should the engineer take? (Select two.)

**Answer Type**: many

- A) **Run `terraform apply -auto-approve` immediately** — `terraform apply` in the same workspace will recreate all the destroyed resources from the configuration files
- B) Run `terraform workspace select staging` to move to the correct workspace — this does not undo the destruction already performed in the `default` workspace
- C) Escalate to the team and use the **remote backend's state version history** (if available) to identify exactly which resources were destroyed and what their configuration was, then prioritise restoring production resources — either by re-running `terraform apply` or by recovering from backup depending on the resource type
- D) Run `terraform plan -destroy` — this re-creates the destroy plan and effectively reverses the previous destroy

**Answer**: A, C

**Explanation**:
This is a production incident scenario. **(A)** Running `terraform apply -auto-approve` in the same (`default`) workspace will re-plan against the current configuration and recreate any resources that were destroyed and are still declared in the configuration — this is the fastest path to restoring declaratively managed resources. For resources like EC2 instances and load balancers, this can restore service quickly. **(C)** Not all resources can be trivially recreated (databases, stateful storage, DNS records with downstream dependencies) — escalation and using state version history to understand the exact blast radius is essential for a structured recovery. (B) switching workspace is correct procedure for future work but does not help restore production. (D) `terraform plan -destroy` generates a destroy plan, not a creation plan — it would make the situation worse, not better.

---

### Question 11 — `terraform apply -replace` vs Deleting from Config

**Difficulty**: Hard
**Answer Type**: one
**Topic**: Understanding terraform apply -replace as the correct way to force-recreate a resource without removing it from config

**Question**:
An EC2 instance has become corrupted. An engineer needs to destroy and recreate it using its current Terraform configuration, without changing any configuration attributes. A colleague suggests removing the resource block from the configuration, running `terraform apply`, and then adding it back and running `terraform apply` again. What is the problem with this approach, and what is the correct alternative?

- A) There is no problem — removing and re-adding a resource block is the standard Terraform procedure for recreating a resource
- B) The two-step remove-and-add approach has two significant problems: (1) removing the block plans a destroy, which deletes the instance — this is correct — but (2) re-adding the block then plans a **create of a brand-new instance** which has a **different resource ID, IP, and configuration** than the original; this process also requires two separate apply operations, increasing the window for errors; the correct approach is **`terraform apply -replace=aws_instance.web`**, which plans a single destroy-then-recreate (shown as `-/+` in the plan) in one apply operation, preserving all configuration attributes and minimising the outage window
- C) The approach is correct but only works if `lifecycle { create_before_destroy = true }` is set on the resource block
- D) The two-step approach is required because `terraform apply -replace` is only available in Terraform Enterprise

**Answer**: B

**Explanation**:
`terraform apply -replace=<address>` (introduced in Terraform 1.0) is the purpose-built command for force-recreating a specific resource. It generates a `-/+` plan for that resource — destroy followed immediately by create — in a single apply, using the current configuration attributes. The two-step approach (remove from config → apply → re-add → apply) technically achieves the same result but is inferior for several reasons: it requires two separate apply operations (doubling the change windows and state write events), the second apply creates a new resource with the same configuration but a new cloud resource ID, and the pattern is error-prone if the engineer forgets to re-add the block or makes a typo. Using `-replace` is cleaner, faster, and the HashiCorp-recommended approach for this scenario.

---

### Question 12 — `terraform output -raw` vs `terraform output` for Scripting

**Difficulty**: Hard
**Answer Type**: one
**Topic**: Understanding why -raw is needed when using terraform output in shell scripts

**Question**:
An engineer writes a deployment script that retrieves a database endpoint from Terraform outputs:

```bash
DB_HOST=$(terraform output db_endpoint)
psql -h "$DB_HOST" -U admin mydb
```

The `psql` connection fails with: `could not translate host name '"db.example.com"' to address`. The engineer notices the hostname has double-quote characters around it. What is the cause and fix?

- A) The output block must include `quote = false` to suppress quote characters in the returned value
- B) The `terraform output` command returns values in **HCL-formatted strings with surrounding double quotes** by default (e.g., `"db.example.com"`); when this is captured in a shell variable, the quotes become part of the string value passed to `psql`; the fix is to use **`terraform output -raw db_endpoint`** — the `-raw` flag returns the value as a plain string without any surrounding quotes or newline formatting, making it safe for direct use in shell scripts and command substitutions
- C) The issue is that `psql` does not accept hostnames from environment variables — the engineer should hard-code the hostname in the script
- D) The output value must be marked `sensitive = true` to strip the formatting characters before shell capture

**Answer**: B

**Explanation**:
`terraform output <name>` returns a human-readable formatted value. For string outputs, this includes surrounding double quotes: `"db.example.com"`. When captured with `$(...)` in a shell script, the quotes are included in the variable, so `$DB_HOST` becomes `"db.example.com"` (with literal quote marks). Tools like `psql`, `curl`, and `ssh` receive this quoted string rather than the bare hostname, causing lookup failures. `terraform output -raw <name>` solves this by returning the raw string value with no surrounding quotes and no trailing newline — exactly what shell variable capture needs for downstream use. `-raw` only works for string-type outputs; for complex types (lists, maps), use `terraform output -json` and parse with `jq`.

---

### Question 13 — `terraform plan -destroy` Unexpected Scope

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Understanding that terraform plan -destroy plans destruction of ALL resources, not just unused ones

**Question**:
An engineer runs `terraform plan -destroy` expecting it to plan the removal of only the resources that are no longer in the configuration (i.e., orphaned resources). Instead, the plan shows all 47 managed resources will be destroyed. The engineer panics and asks: "Is something wrong?" What is the correct explanation?

- A) `terraform plan -destroy` has detected that all 47 resources are misconfigured and must be replaced — the engineer should review each resource
- B) `terraform plan -destroy` plans the **destruction of ALL resources currently tracked in state**, regardless of whether they are in the configuration or not — it is equivalent to removing every resource block and running `terraform plan`; it is used when the intention is to completely tear down the environment; it does not selectively destroy only orphaned resources; to remove only resources that have been removed from configuration, the engineer should simply run a normal `terraform plan` and look for any `-` (destroy) entries
- C) Something is wrong with the state file — `terraform plan -destroy` should never show more than 10 resources
- D) The engineer accidentally appended `-destroy` to their `terraform plan -target` command, overriding the target scope

**Answer**: B

**Explanation**:
`terraform plan -destroy` (equivalent to `terraform destroy` without applying) generates a plan to destroy **every resource Terraform currently tracks in state**. It is the preview of what `terraform destroy` would do. It is not a selective or differential command — it destroys everything managed in the current workspace's state. For reviewing what would be removed by a configuration change (removed resource blocks), the engineer should run a standard `terraform plan` and look for resources marked with `-` (destroy). Those are the orphaned resources whose blocks have been removed. `terraform plan -destroy` is appropriate for environment teardown scenarios: decommissioning a staging environment, cleaning up a feature branch, or verifying what a full destroy would affect before committing to it.

---

---

## Questions

---

### Question 1 — Subnet Created Before VPC

**Difficulty**: Easy
**Answer Type**: one
**Topic**: Understanding that implicit dependency from attribute reference controls creation order

**Question**:
An engineer writes a Terraform configuration with an `aws_vpc` and an `aws_subnet`. They expect Terraform to create the subnet first because it is declared first in the file. Instead, Terraform creates the VPC first. The engineer asks why. What is the correct explanation?

- A) Terraform creates resources in alphabetical order by resource type — `aws_subnet` comes before `aws_vpc` alphabetically, but Terraform uses the reverse alphabetical order as a safety measure
- B) Terraform creates resources in the order they are declared in configuration files — the VPC being created first means it must have been declared first
- C) Terraform infers creation order from the **dependency graph, not file declaration order** — because the subnet's `vpc_id` argument references `aws_vpc.main.id`, Terraform detects an implicit dependency and ensures the VPC is created before the subnet; file order is irrelevant to execution order
- D) The VPC is created first only because it uses the default provider; resources using aliased providers are always created last

**Answer**: C

**Explanation**:
Terraform builds a Directed Acyclic Graph (DAG) by scanning attribute references in the configuration. When `aws_subnet.public` uses `vpc_id = aws_vpc.main.id`, Terraform detects that the subnet's `vpc_id` argument depends on the VPC's `id` attribute — an attribute that is only known after the VPC is created. This creates an implicit dependency edge in the graph: VPC → subnet. Terraform respects this ordering during apply regardless of how the blocks are arranged in the `.tf` files. Declaration order in HCL has no effect on execution order; only the dependency graph does.

---

### Question 2 — Data Source Returns Stale AMI

**Difficulty**: Easy
**Answer Type**: one
**Topic**: Understanding when data sources are evaluated and how to force a refresh

**Question**:
An engineer uses a data source to look up the latest Ubuntu AMI and passes it to an EC2 instance. Six months later, a new Ubuntu AMI is released. The engineer runs `terraform apply` but the EC2 instance is not updated — it still uses the old AMI. The engineer assumes the data source is refreshing automatically. What explains this behaviour?

- A) Data sources are evaluated only during `terraform init` — after initialisation, the result is cached permanently
- B) The data source is re-evaluated on every `terraform plan` and `terraform apply`; if the AMI has changed, Terraform will detect the new value and plan a replacement for the EC2 instance automatically
- C) Data sources **are** re-evaluated on each plan, but changing the AMI ID returned by the data source does not automatically cause the EC2 instance to be replaced unless the resource has a `ForceNew` constraint on `ami` — and `aws_instance.ami` is indeed `ForceNew`; if the plan shows no changes, the most likely explanation is that the data source filter is still returning the same AMI (e.g., the `most_recent = true` filter resolved to the same ID), not that the data source is stale; the engineer should verify by running `terraform plan` and examining the data source result
- D) Data sources cache their results in `.terraform/` for 30 days to avoid repeated API calls during planning

**Answer**: C

**Explanation**:
Data sources are re-evaluated on every `terraform plan` and `terraform apply` — they are not permanently cached. If the data source filter (e.g., `most_recent = true` for Ubuntu AMIs) resolves to a new AMI ID, Terraform will detect that the `aws_instance.ami` attribute would change and, because `ami` is a `ForceNew` attribute, will plan a replacement (`-/+`) for the EC2 instance. If the plan shows no changes, the most likely reason is that the data source is still returning the same AMI ID it always has — perhaps the filter is not matching the newest AMI, or the newer AMI hasn't appeared under the queried owner or name pattern. The engineer should examine the data source output in `terraform plan` to confirm which AMI ID is being returned.

---

### Question 3 — `prevent_destroy` Blocks Teardown Pipeline

**Difficulty**: Easy
**Answer Type**: one
**Topic**: Understanding that prevent_destroy causes terraform apply/destroy to error and how to override it

**Question**:
A team has `lifecycle { prevent_destroy = true }` on their production RDS instance. When a junior engineer runs `terraform destroy` on the environment teardown pipeline, it fails with: `Error: Instance cannot be destroyed`. The engineer asks: "How do we destroy this resource when we're ready to decommission the environment?" What is the correct answer?

- A) Run `terraform destroy -force` — this flag overrides `prevent_destroy` for a single destroy operation
- B) The only way to destroy a `prevent_destroy`-protected resource is to use the AWS console directly
- C) `prevent_destroy = true` is a **configuration-level guard** — to destroy the resource, the engineer must **remove or change the `prevent_destroy` setting** in the configuration file and then run `terraform apply` (or `terraform destroy`) again; there is no runtime flag to override it; this is by design — the guard forces a deliberate code change before destruction can proceed
- D) Set `TF_PREVENT_DESTROY=false` in the environment before running `terraform destroy`

**Answer**: C

**Explanation**:
`prevent_destroy = true` is a safeguard that causes `terraform plan` to error if the plan includes destroying the protected resource — whether triggered by `terraform destroy` or by removing the resource block. It is intentionally impossible to override at runtime with a flag, because the purpose is to require a human to make a deliberate, version-controlled change to the configuration before destruction can proceed. The process for decommissioning a `prevent_destroy`-protected resource is: (1) remove `prevent_destroy = true` (or set it to `false`) in the `.tf` file, (2) commit and merge the change, (3) run `terraform apply` or `terraform destroy`. This ensures the removal of the guard is tracked in version history and reviewed.

---

### Question 4 — Two Resources Created in Wrong Order Despite `depends_on`

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Diagnosing why depends_on alone on a data source may not be enough to control ordering with IAM

**Question**:
An engineer creates an EC2 instance with an IAM instance profile. The instance starts but immediately fails because the attached IAM role does not yet have the S3 read policy attached — the policy attachment resource is not complete by the time the instance boots and attempts to use it. The engineer added `aws_instance.app` to depend on `aws_iam_role.app`, but forgot to include the policy resource in `depends_on`. What is the most precise diagnosis and fix?

- A) IAM propagation is always instant — the instance failure is caused by a misconfigured security group blocking S3 access, not a missing dependency
- B) The implicit dependency on `aws_iam_role.app` ensures the role exists before the instance, but does not guarantee the **policy attachment** (`aws_iam_role_policy` or `aws_iam_role_policy_attachment`) is complete; the engineer must add the policy attachment resource to the `depends_on` list on `aws_instance.app` so Terraform waits for the policy to be attached before creating the instance
- C) Adding any `depends_on` entry to a resource causes Terraform to serialize all subsequent resource creations — the issue must be something else
- D) `depends_on` cannot reference `aws_iam_role_policy` resources — it only accepts module references

**Answer**: B

**Explanation**:
This is the canonical use case for `depends_on`. When an EC2 instance uses an IAM instance profile, Terraform can detect implicit dependencies on the role and profile objects through attribute references — but it cannot detect that the instance's startup behaviour depends on a policy being attached to that role, because there is no attribute reference from the instance to the policy resource. Terraform creates the instance after the role exists but potentially before the policy attachment completes. The instance then tries to call the S3 API using permissions that haven't propagated yet. The fix is explicit: add the policy attachment to `depends_on` on the `aws_instance` resource — `depends_on = [aws_iam_role_policy.s3_read]`. This forces Terraform to wait for the policy attachment to complete before provisioning the instance, ensuring IAM permissions are in place before the instance attempts to use them.

---

### Question 5 — `count` Removal Causes Unexpected Destroy+Create

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Understanding that removing a count item by index causes all subsequent instances to shift and be replaced

**Question**:
An engineer uses `count = 3` to create three S3 buckets, named `bucket-0`, `bucket-1`, and `bucket-2`. They later need to remove `bucket-1`. They remove element 1 from the list and set `count = 2`. On running `terraform plan`, they see that `bucket-1` will be destroyed and `bucket-2` will also be destroyed and recreated as a different bucket. Why does `bucket-2` get recreated?

- A) `count` always destroys and recreates all instances when the count value is reduced
- B) Removing element 1 from the list **shifts the index of the remaining elements** — what was index 2 (`bucket-2`) becomes index 1 (`bucket-1`) in the new count; Terraform sees `aws_s3_bucket.this[1]` as a different instance in state vs the new configuration, triggering a destroy+create; this index-shifting problem is why `for_each` with stable string keys is preferred over `count` when the set of instances may change
- C) S3 bucket names are globally unique — Terraform must destroy all buckets with sequential names when any one is removed
- D) This only happens when `count` is reduced from 3 to 2 — reducing to 1 or 0 would not trigger the shift

**Answer**: B

**Explanation**:
`count` identifies each resource instance by its zero-based integer index. When an item in the middle of the list is removed and `count` is reduced, all indexes above the removed item shift down by one. Terraform compares state (which has instances at indexes 0, 1, and 2) to the new configuration (which has instances at indexes 0 and 1 with updated names or attributes). Index 2 in state no longer matches index 1 in the new config — Terraform plans to destroy the old index-2 instance and create a new index-1 instance. This is a well-known pain point of `count` for managing collections that may have items removed from the middle. The idiomatic solution is to switch to `for_each` with a `set(string)` or `map`, where each instance is keyed by a stable string (e.g., the bucket name). Removing one key from a `for_each` collection only destroys that specific instance — all others retain their stable keys and are unaffected.

---

### Question 6 — `ignore_changes` Not Preventing Drift Detection

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Understanding the correct syntax for ignore_changes and common mistakes

**Question**:
An engineer uses Auto Scaling Groups and wants Terraform to ignore the `desired_capacity` attribute (which the ASG manages automatically). They add this lifecycle block:

```hcl
lifecycle {
  ignore_changes = "desired_capacity"
}
```

On the next `terraform plan`, Terraform still shows a change to `desired_capacity`. What is the error?

- A) `desired_capacity` cannot be ignored — it is a required attribute that Terraform always manages
- B) `ignore_changes` is only available in Terraform Enterprise — the community edition always manages all attributes
- C) The **`ignore_changes` argument requires a list value**, not a bare string — the correct syntax is `ignore_changes = [desired_capacity]` (square brackets, no quotes around the attribute name); using a string instead of a list causes Terraform to silently ignore the argument or return a validation error, leaving the attribute tracked normally
- D) The engineer must also add `create_before_destroy = true` alongside `ignore_changes` for the latter to take effect

**Answer**: C

**Explanation**:
`ignore_changes` takes a **list of attribute references** (not strings). The correct syntax is:
```hcl
lifecycle {
  ignore_changes = [desired_capacity]
}
```
The attribute names inside the list are written without quotes — they are symbolic references to the resource's schema attributes, not string literals. Using a bare quoted string (`ignore_changes = "desired_capacity"`) is a type error: the argument expects a list and receives a string, which Terraform either rejects with a validation error or silently ignores (depending on the version), with the result that the attribute is still tracked and drift is still detected. The square bracket list syntax is required. To ignore all attributes, use the special value `ignore_changes = all`.

---

### Question 7 — `for_each` Fails on a `list(string)`

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Understanding that for_each does not accept a plain list and requires a set or map

**Question**:
An engineer writes:

```hcl
variable "bucket_names" {
  type    = list(string)
  default = ["logs", "backups", "assets"]
}

resource "aws_s3_bucket" "this" {
  for_each = var.bucket_names
  bucket   = each.key
}
```

`terraform plan` returns an error: `The given "for_each" argument value is unsuitable: must be a map, or set of strings, and you have provided a value of type list of string`. What is the fix?

- A) Change `for_each = var.bucket_names` to `for_each = count(var.bucket_names)` — `for_each` requires a count value, not the list directly
- B) `for_each` does not support string resources — it only works with numeric types; use `count = length(var.bucket_names)` instead
- C) Wrap the list in the `toset()` function: `for_each = toset(var.bucket_names)` — `for_each` requires a `set(string)` or `map`; `toset()` converts a `list(string)` to a `set(string)` by deduplicating values and removing ordering; after this conversion, `each.key` and `each.value` will both hold the bucket name for each iteration
- D) Change the variable type to `set(string)` in the variable declaration and leave `for_each` as-is — `for_each` accepts sets only from variable declarations, not inline values

**Answer**: C

**Explanation**:
`for_each` requires a value of type `map` or `set(string)` — it does not accept `list(string)` directly. This is because lists are ordered and can contain duplicates, while `for_each` needs stable, unique keys for each instance. The standard fix is to convert the list to a set using `toset()`: `for_each = toset(var.bucket_names)`. After this, `each.key` and `each.value` both equal the bucket name for each iteration (in a set, the key and value are the same). Note that `toset()` deduplicates the input — if the list contained duplicate names, the set would have fewer elements. Alternatively, changing the variable type declaration to `type = set(string)` also works and is the cleaner long-term approach if duplicates are not meaningful.

---

### Question 8 — Resource Recreated Every Apply Due to `replace_triggered_by`

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Diagnosing unintended constant replacement caused by replace_triggered_by referencing a frequently changing resource

**Question**:
An engineer adds `replace_triggered_by = [aws_launch_template.web]` to an Auto Scaling Group resource to ensure the ASG is recycled when the launch template changes. After deploying, the ASG is replaced on every `terraform apply` — even when nothing has changed. What is the most likely cause?

- A) `replace_triggered_by` always forces a replacement on every apply — this is the expected behaviour
- B) The `aws_launch_template.web` resource itself has **`create_before_destroy = true`**, causing it to be replaced on every apply, which then triggers the ASG replacement through `replace_triggered_by`; the fix is to remove `create_before_destroy` from the launch template
- C) The `aws_launch_template.web` resource **has an attribute that changes on every apply** — for example, if the launch template has `latest_version` or similar computed attribute that increments on each apply even with no configuration changes, `replace_triggered_by` detects this as a change and triggers ASG replacement; the engineer should scope `replace_triggered_by` to a specific stable attribute rather than the entire resource, or investigate why the launch template resource reports changes on every apply
- D) `replace_triggered_by` is incompatible with Auto Scaling Groups — it should only be used with stateless resources like EC2 instances

**Answer**: C

**Explanation**:
`replace_triggered_by` monitors the referenced resource (or a specific attribute of it) and forces a replacement of the current resource whenever a change is detected. If the referenced resource itself changes on every apply — for example, because it has a computed attribute like `latest_version` that increments whenever the template is touched, or because some attribute is not stable across plan cycles — then `replace_triggered_by` will trigger the ASG replacement every time. To fix this, the engineer can scope the trigger to a specific, stable attribute rather than the whole resource: `replace_triggered_by = [aws_launch_template.web.id]` rather than the entire resource object. Alternatively, investigate why the launch template is reporting changes on every apply and stabilise it. The pattern `replace_triggered_by = [resource]` triggers on any change to any attribute of that resource — scoping to a specific attribute gives more control.

---

### Question 9 — `removed` Block Destroys Resource Unexpectedly

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Understanding that removed block destroy=false is needed to stop managing without destroying

**Question**:
An engineer wants to stop managing an EC2 instance with Terraform without deleting it from AWS. They have heard about the `removed` block (Terraform 1.7+) and add it to their configuration. On the next `terraform apply`, the instance is deleted. What did the engineer most likely forget?

- A) The `removed` block always stops Terraform from managing a resource without any cloud-side effect — the instance deletion must have been triggered by something else
- B) The engineer forgot to run `terraform state rm` before using the `removed` block — the two must be used together
- C) The `removed` block has a **`lifecycle { destroy = false }` sub-block** that must be explicitly set — without it, the default behaviour of `removed` is to **destroy** the resource and remove it from state; setting `destroy = false` tells Terraform to stop tracking the resource but leave it running in the cloud; the engineer forgot this sub-block and got the default destroy behaviour
- D) `removed` blocks are only supported in HCP Terraform — in the open-source CLI, they always destroy the resource

**Answer**: C

**Explanation**:
The `removed` block (introduced in Terraform 1.7) is the declarative way to stop managing a resource. Its `lifecycle` sub-block controls what happens to the cloud resource: `destroy = true` (the default) destroys the resource and removes it from state; `destroy = false` removes it from state only, leaving the cloud resource intact and unmanaged. The engineer who wanted to "stop managing without deleting" needed:
```hcl
removed {
  from = aws_instance.old_server
  lifecycle {
    destroy = false
  }
}
```
Without the `destroy = false` sub-block, Terraform uses the default (`destroy = true`) and deletes the instance. This is analogous to `terraform state rm` (which also removes from state without destroying) but in a declarative, version-controlled form.

---

### Question 10 — Two Scenarios Where `depends_on` Is Required

**Difficulty**: Medium
**Answer Type**: many
**Topic**: Identifying TWO scenarios where implicit dependency detection is insufficient and depends_on is needed

**Question**:
Which TWO of the following scenarios require `depends_on` because Terraform cannot detect the dependency through attribute references alone? (Select two.)

- A) An EC2 instance references `aws_subnet.public.id` in its `subnet_id` argument — Terraform must be told explicitly via `depends_on` that the instance depends on the subnet
- B) An EC2 instance uses an IAM instance profile, and the instance's startup script reads from an S3 bucket that the attached IAM role must have permission to access — the policy attachment has no attribute referenced by the instance, so Terraform has no way to detect the dependency automatically
- C) A `null_resource` with a `local-exec` provisioner runs a script that calls an API exposed by an `aws_api_gateway_rest_api` resource — no attribute of the API gateway is referenced in the `null_resource` block, so `depends_on` is needed to ensure the API is deployed before the script runs
- D) An `aws_db_instance` is referenced by its endpoint in an `aws_instance` user_data script using string interpolation — Terraform must be told via `depends_on` that the instance depends on the database

**Answer**: B, C

**Explanation**:
`depends_on` is for dependencies that Terraform **cannot** detect through attribute references. **(A)** is incorrect — `subnet_id = aws_subnet.public.id` is an explicit attribute reference, which Terraform automatically resolves into a dependency edge; no `depends_on` is needed. **(D)** is also incorrect — using `aws_db_instance.main.endpoint` in string interpolation is also an attribute reference that creates an implicit dependency. **(B)** is a genuine `depends_on` use case: the IAM policy attachment resource has no attribute referenced by the EC2 instance, yet the instance's runtime behaviour depends on the policy being attached before it starts. Terraform cannot infer this. **(C)** is the other canonical case: a `null_resource` provisioner that calls an external API has no Terraform attribute reference to that API resource, so `depends_on` is required to guarantee ordering.

---

### Question 11 — Circular Dependency Error

**Difficulty**: Hard
**Answer Type**: one
**Topic**: Diagnosing a cycle in the dependency graph and knowing how to resolve it

**Question**:
An engineer receives the error: `Error: Cycle: aws_security_group.app, aws_instance.web`. Their configuration has `aws_instance.web` referencing `aws_security_group.app.id` in its `vpc_security_group_ids`, and `aws_security_group.app` referencing `aws_instance.web.private_ip` in an ingress rule. What explains the error and how should it be resolved?

- A) The error means both resources have `prevent_destroy = true` — removing those lifecycle blocks will resolve the cycle
- B) A **dependency cycle** exists: `aws_instance.web` depends on `aws_security_group.app` (for the security group ID), and simultaneously `aws_security_group.app` depends on `aws_instance.web` (for the private IP in the ingress rule); Terraform's DAG cannot resolve circular dependencies and errors immediately; the resolution is to break the cycle — for example, remove the private IP reference from the security group ingress rule and use a CIDR block instead, or restructure the ingress rule to reference a different stable value
- C) Cycles are resolved automatically on `terraform apply` — the error only appears during `terraform plan` and can be ignored
- D) The cycle is caused by both resources being in the same `.tf` file — moving one to a separate file resolves the dependency conflict

**Answer**: B

**Explanation**:
Terraform constructs a Directed Acyclic Graph (DAG) to determine creation and destruction order. A cycle occurs when resource A depends on resource B, and resource B also depends on resource A — creating a circular chain that cannot be ordered. In this case: the instance needs the security group ID to be created → but the security group needs the instance's private IP to be created → deadlock. Terraform detects this during graph construction and errors with a "Cycle" message rather than attempting an impossible ordering. The fix requires breaking the cycle by removing one of the circular references. Common approaches: (1) remove the private IP from the security group ingress and use a broader CIDR; (2) use a separate `aws_security_group_rule` resource for the instance-IP-based rule, applied after the instance is created; (3) redesign the architecture so the circular reference is not needed.

---

### Question 12 — `moved` Block Applied But Resource Still Recreated

**Difficulty**: Hard
**Answer Type**: one
**Topic**: Diagnosing why a moved block did not prevent destroy+create — common mistakes in moved block syntax

**Question**:
An engineer renames `resource "aws_instance" "web"` to `resource "aws_instance" "web_server"` and adds:

```hcl
moved {
  from = "aws_instance.web"
  to   = "aws_instance.web_server"
}
```

Running `terraform plan` still shows `1 to destroy, 1 to add`. What is the error in the `moved` block?

- A) The `moved` block is in the wrong file — it must be in `main.tf` and cannot be in any other `.tf` file
- B) The `moved` block requires a `provider` argument to be specified alongside the `from` and `to` addresses
- C) The **`from` and `to` values in a `moved` block must be bare references, not quoted strings** — the correct syntax is `from = aws_instance.web` and `to = aws_instance.web_server` (without quotes); using quoted strings causes Terraform to treat the values as string literals rather than resource address references, which fails validation or is ignored; without a valid `moved` block, Terraform does not know about the rename and plans a destroy+create as it would without any `moved` block
- D) `moved` blocks can only be used when the resource is being moved between modules — renaming within the same module requires `terraform state mv` instead

**Answer**: C

**Explanation**:
`moved` block `from` and `to` arguments are **resource address references**, not strings. The correct syntax does not use quotes:
```hcl
moved {
  from = aws_instance.web
  to   = aws_instance.web_server
}
```
Quoting the addresses — `from = "aws_instance.web"` — is a syntax error or causes Terraform to misinterpret the block, depending on the version. When the `moved` block is invalid or unrecognised, Terraform falls back to the default behaviour: it sees a new address (`aws_instance.web_server`) with no state entry and an old address (`aws_instance.web`) with no configuration block, and plans a destroy+create. The `moved` block is valid for renaming within a module, moving into or out of a module, and refactoring `count`/`for_each` addresses — `terraform state mv` remains a valid imperative alternative.

---

### Question 13 — `data` Source Reads Stale Value During Apply

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Understanding the known-after-apply problem for data sources that depend on resources being created in the same apply

**Question**:
An engineer creates an `aws_security_group` resource and a `data "aws_security_group"` data source that filters by the security group's name in the same Terraform configuration. They expect the data source to return the newly created security group. During `terraform plan`, the data source shows `(known after apply)` instead of the security group's attributes. The engineer asks why. What is the correct explanation?

- A) Data sources can never reference resources created in the same Terraform configuration — they are always evaluated before any resources are created
- B) The data source must use the resource's `id` attribute, not the `name` filter — `name`-based filters only work against pre-existing resources
- C) The data source **depends on the security group being created**, but during `terraform plan` the security group does not exist yet (it will be created on apply); Terraform detects this dependency and defers the data source read until `terraform apply`, when the security group will exist — this is the "known after apply" behaviour; the attributes are shown as `(known after apply)` in the plan; after apply completes, the data source will have been read and its attributes will be available; the preferred alternative is to reference the resource's attributes directly (`aws_security_group.app.id`) rather than re-querying via a data source for a resource Terraform itself is creating
- D) The `(known after apply)` message means the data source is misconfigured — it cannot be used in the same configuration as a resource of the same type

**Answer**: C

**Explanation**:
When a data source's filter depends on a value that is only known after a resource is created (e.g., the name of a security group being created in the same apply), Terraform cannot evaluate the data source during planning — the value hasn't been set yet. Terraform defers the data source read to the apply phase and shows `(known after apply)` in the plan for any attributes that depend on the deferred result. This is correct behaviour and not an error. However, using a data source to look up a resource that Terraform itself manages is generally unnecessary and adds complexity. The idiomatic approach is to reference the managed resource's attributes directly — `aws_security_group.app.id` — rather than creating a data source that queries back for the same resource. Data sources are most valuable for referencing resources that exist outside the current Terraform configuration.

---

---

## Questions

---

### Question 1 — Required Variable Not Prompted in CI Pipeline

**Difficulty**: Easy
**Answer Type**: one
**Topic**: Understanding that a required variable (no default) causes a non-interactive failure in CI, not a prompt

**Question**:
An engineer declares a variable with no `default`:

```hcl
variable "db_password" {
  type = string
}
```

Locally, running `terraform apply` prompts them to type the value interactively. In the CI pipeline, the step fails with: `No value for required variable; The root module variable "db_password" is not set`. The engineer expected the same interactive prompt to appear in CI. What explains the difference and how should it be fixed?

- A) CI environments always run Terraform with `-no-prompt`, which is why the prompt is suppressed — remove that flag
- B) The variable must have a `default = ""` to work in CI — required variables are not supported in automated pipelines
- C) Terraform's interactive prompt only appears when running in an **interactive terminal (TTY)**; CI pipelines run in non-interactive mode, so instead of prompting, Terraform errors immediately when a required variable has no value; the fix is to supply the value through a CI-appropriate mechanism — such as setting the `TF_VAR_db_password` environment variable (from a secrets store), passing `-var "db_password=..."` in the apply command, or using a `terraform.tfvars` file injected at pipeline runtime
- D) CI pipelines require all variables to be declared in a `terraform.tfvars` file — environment variables are not supported for CI variable injection

**Answer**: C

**Explanation**:
The interactive prompt is a terminal feature — Terraform checks whether `stdin` is a TTY (interactive terminal) and only prompts if it is. In CI environments, `stdin` is not a TTY, so Terraform skips the prompt and immediately fails with an error when a required variable has no supplied value. This is correct behaviour — automated pipelines should never depend on interactive input. The standard patterns for injecting secrets into CI pipelines are: (1) set `TF_VAR_<name>` as a CI secret/environment variable, which Terraform reads automatically; (2) pass `-var "name=value"` directly in the command, injecting from CI secrets; (3) generate a `.tfvars` file from a secrets vault at pipeline runtime. Option (1) is the most common and keeps the secret out of command-line arguments (which may appear in logs).

---

### Question 2 — `lookup()` Fails With Error Instead of Returning a Default

**Difficulty**: Easy
**Answer Type**: one
**Topic**: Understanding the correct 3-argument form of lookup() to avoid errors on missing keys

**Question**:
An engineer writes:

```hcl
locals {
  instance_type = lookup(var.instance_types, var.environment)
}
```

When `var.environment = "dr"` and the map does not have a `"dr"` key, Terraform throws: `Error in function call: Call to function "lookup" failed: lookup failed to find key "dr"`. The engineer expected a fallback to a default value. What is wrong and how should it be fixed?

- A) `lookup()` does not support fallback values — use a `try()` block to catch missing key errors
- B) The engineer should use `var.instance_types[var.environment]` instead — direct index access returns `null` on missing keys
- C) The **two-argument form `lookup(map, key)`** throws an error when the key is absent; to provide a fallback, the engineer must use the **three-argument form: `lookup(map, key, default)`** — for example, `lookup(var.instance_types, var.environment, "t3.micro")`; the third argument is returned whenever the specified key is not found in the map, preventing the error
- D) `lookup()` only works on `map(string)` types — if `var.instance_types` is declared as `map(any)`, the function always errors on missing keys

**Answer**: C

**Explanation**:
`lookup(map, key)` — the two-argument form — errors when the key is not present in the map. This is often surprising to engineers who expect it to return `null` silently. The three-argument form `lookup(map, key, default)` is the correct pattern for providing a fallback: `lookup(var.instance_types, var.environment, "t3.micro")` returns `"t3.micro"` if `"dr"` is not in the map. Alternatively, `try(var.instance_types[var.environment], "t3.micro")` achieves the same result using the `try()` function, which catches errors from the index access. The `try()` approach is more flexible and handles any expression, while `lookup()` is specifically designed for map key lookups with optional defaults.

---

### Question 3 — Wrong Variable Value Used When Both `.tfvars` Files Set It

**Difficulty**: Easy
**Answer Type**: one
**Topic**: Understanding that auto.tfvars takes precedence over terraform.tfvars

**Question**:
An engineer has both `terraform.tfvars` (sets `region = "us-east-1"`) and a file named `overrides.auto.tfvars` (sets `region = "eu-west-1"`) in the same directory. They expect `terraform.tfvars` to win because it is the "main" file. Terraform uses `"eu-west-1"`. Why?

- A) Terraform reads `.tfvars` files in alphabetical order and the last value wins — `overrides` comes after `terraform` alphabetically
- B) `terraform.tfvars` is only loaded when no `.auto.tfvars` files are present — the two file types are mutually exclusive
- C) **`*.auto.tfvars` files have higher precedence than `terraform.tfvars`** in Terraform's variable resolution order — any file matching the pattern `*.auto.tfvars` is automatically loaded and takes priority over the manually-loaded `terraform.tfvars`; the engineer's mental model of `terraform.tfvars` as the "most authoritative" file is incorrect; to override an `auto.tfvars` file, the engineer must use a CLI `-var` flag or a `TF_VAR_*` environment variable, both of which rank higher than any `.tfvars` file
- D) Terraform merges values from both files and uses the region declared in `overrides.auto.tfvars` because it was the most recently modified file

**Answer**: C

**Explanation**:
Terraform's variable precedence order (highest to lowest): CLI `-var` flag = `TF_VAR_*` environment variables → `*.auto.tfvars` files → `terraform.tfvars` → `-var-file` flag → `default` in the variable block. `*.auto.tfvars` files — any file in the working directory whose name ends in `.auto.tfvars` — are loaded automatically and ranked above `terraform.tfvars`. This means `overrides.auto.tfvars` correctly overrides `terraform.tfvars`. If the engineer wants their `terraform.tfvars` value to win, they should either rename the override file to remove the `.auto.` suffix (so it needs an explicit `-var-file` flag), or simply ensure the desired value is in the highest-precedence source.

---

### Question 4 — `timestamp()` Causes Perpetual Diff on Every Plan

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Understanding why timestamp() in a resource attribute causes Terraform to always show a change

**Question**:
An engineer adds a `last_deployed` tag to all EC2 instances using `timestamp()`:

```hcl
resource "aws_instance" "web" {
  ami           = data.aws_ami.ubuntu.id
  instance_type = "t3.micro"

  tags = {
    Name          = "web"
    LastDeployed  = timestamp()
  }
}
```

Every time `terraform plan` runs — even when nothing else has changed — the plan shows `1 to change` for the `LastDeployed` tag. The engineer cannot understand why. What is the cause?

- A) EC2 tag updates are not idempotent in AWS — any tag with a computed value always triggers an update
- B) `timestamp()` is a non-deterministic function that **returns the current UTC time at the moment `terraform plan` is evaluated** — its value changes on every plan run; Terraform compares the new `timestamp()` value against the value stored in state from the last apply, and since they differ, it always plans an update to the tag; to fix this, the engineer should use `ignore_changes = [tags["LastDeployed"]]` in a `lifecycle` block if they want the tag set once on creation and not updated, or use a static value or a variable for the timestamp if they want it controlled
- C) `timestamp()` is only valid in `locals` blocks — using it directly in a resource attribute is unsupported and the result is undefined
- D) The perpetual diff is caused by the `LastDeployed` key containing uppercase letters — tag keys must be lowercase in Terraform

**Answer**: B

**Explanation**:
`timestamp()` returns the current UTC time at the moment the function is evaluated. Because Terraform evaluates all expressions during every `plan` and `apply` run, `timestamp()` produces a new value on every execution. The state file records the value from the last `apply`, but the next `plan` computes a fresh timestamp — so a difference is always detected, and Terraform always plans an update. This applies to all non-deterministic functions (`uuid()` has the same behaviour). The fix depends on intent: if the tag should record when the resource was last _modified by Terraform_, use `lifecycle { ignore_changes = [tags["LastDeployed"]] }` combined with setting it only once. If a truly dynamic timestamp is needed, control it externally (e.g., pass it as a variable from the CI pipeline) rather than generating it inside the Terraform configuration.

---

### Question 5 — Validation Condition References a `local` — Error

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Understanding that variable validation conditions can only reference var.<name>, not locals or other resources

**Question**:
An engineer wants to validate that `var.environment` is one of the values in a centrally managed list. They write:

```hcl
locals {
  allowed_envs = ["dev", "staging", "prod"]
}

variable "environment" {
  type = string

  validation {
    condition     = contains(local.allowed_envs, var.environment)
    error_message = "environment must be one of: dev, staging, prod"
  }
}
```

`terraform validate` returns: `A validation condition may only refer to the variable being validated`. What is the cause and fix?

- A) The error is caused by `contains()` not being allowed in validation blocks — use `== "dev" || == "staging"` instead
- B) Locals must be declared after the variable they reference — move the `locals` block below the `variable` block to fix the ordering error
- C) **A `validation` block's `condition` can only reference `var.<name>` — the variable being validated** — it cannot reference `local.*`, other `var.*`, resources, data sources, or any value that requires prior evaluation; the fix is to inline the allowed values list directly in the condition: `contains(["dev", "staging", "prod"], var.environment)`; if the list must be maintained in one place, it should be documented or managed outside Terraform's variable validation
- D) The `local.allowed_envs` reference would work if the locals block were in the same file as the variable — cross-file references are not allowed in validation conditions

**Answer**: C

**Explanation**:
Variable validation runs very early in the Terraform workflow — before planning, before locals are computed, and before any provider or resource evaluation. At the time validation runs, only the variable's own value is available. This is why the `condition` expression is restricted to references of the form `var.<name>`. Any reference to `local.*`, `data.*`, another `var.*`, or a resource causes the validation error. The correct fix is to inline the list in the condition: `contains(["dev", "staging", "prod"], var.environment)`. If the list needs to be a single source of truth shared across multiple validations, consider using a comment in the validation block noting the authoritative source, or enforcing the constraint in a wrapper module that also declares the local.

---

### Question 6 — `templatefile()` Fails With "File Not Found"

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Using path.module correctly to reference template files relative to the current module

**Question**:
An engineer stores a startup script template at `modules/web/templates/user_data.sh.tpl` and references it in `modules/web/main.tf`:

```hcl
user_data = templatefile("templates/user_data.sh.tpl", {
  app_name = var.app_name
})
```

Running `terraform apply` from the repository root (`/repo`) fails with: `Error: Invalid function argument — No file exists at /repo/templates/user_data.sh.tpl`. What is the cause and fix?

- A) `templatefile()` does not support relative paths — use an absolute path starting with `/`
- B) Template files must be in the root module directory — they cannot be stored inside module subdirectories
- C) The path `"templates/user_data.sh.tpl"` is resolved **relative to the directory where `terraform apply` is run** (the working directory / root module), not relative to the module file containing the call; since the apply is run from `/repo`, Terraform looks for `/repo/templates/user_data.sh.tpl` rather than `/repo/modules/web/templates/user_data.sh.tpl`; the fix is to use `path.module` to anchor the path to the current module: `templatefile("${path.module}/templates/user_data.sh.tpl", {...})`
- D) The `.tpl` extension is not recognised by `templatefile()` — the file must be named with a `.tftpl` extension

**Answer**: C

**Explanation**:
Terraform resolves bare relative paths (like `"templates/user_data.sh.tpl"`) relative to the **current working directory** — the directory where `terraform apply` is invoked. For root module files this is fine, but for resources inside a module the working directory is the root, not the module's own directory. `path.module` is the built-in variable that contains the filesystem path to the directory containing the current `.tf` file. Using `"${path.module}/templates/user_data.sh.tpl"` ensures the template is always found relative to the module, regardless of where Terraform is run from. This is the standard pattern for modules that bundle file resources (templates, scripts, policy documents) alongside their `.tf` files.

---

### Question 7 — `merge()` Silently Overwrites Expected Key

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Understanding that merge() uses last-key-wins when maps share duplicate keys

**Question**:
An engineer merges two tag maps:

```hcl
locals {
  default_tags = {
    Owner       = "platform-team"
    Environment = "production"
  }
  resource_tags = {
    Environment = "staging"
    Service     = "api"
  }
  all_tags = merge(local.default_tags, local.resource_tags)
}
```

The engineer expects `all_tags.Environment` to be `"production"` (from `default_tags`) because it was defined first. Instead it is `"staging"`. What is the cause?

- A) `merge()` errors when two maps share duplicate keys — the engineer should remove the duplicate before calling `merge()`
- B) `merge()` keeps the value from the **first** map when a duplicate key is encountered — the behaviour is correct but the engineer specified the maps in the wrong order
- C) **`merge()` uses last-wins for duplicate keys** — when the same key appears in multiple maps, the value from the **rightmost** (last) map argument overrides all earlier values; `local.resource_tags` is the last argument, so its `Environment = "staging"` overwrites `default_tags`'s `Environment = "production"`; to make `default_tags` win on conflicts, swap the argument order: `merge(local.resource_tags, local.default_tags)`
- D) `merge()` is non-deterministic on duplicate keys — the result depends on internal map iteration order and cannot be relied upon

**Answer**: C

**Explanation**:
`merge(map1, map2, ...)` merges all provided maps into a single map. When two or more maps share a key, the value from the **last map** (rightmost argument) wins. This is intentional — it allows a pattern where a "base" or "default" map is provided first, and an "override" map is provided last, so the override values take precedence. In this example, if the engineer wants `default_tags` to be the authoritative source for `Environment`, they should place `default_tags` last: `merge(local.resource_tags, local.default_tags)`. This is a common pattern for tag management: `merge(local.common_tags, var.resource_specific_tags)` — the resource-specific tags overlay the common defaults.

---

### Question 8 — `cidrsubnet()` Returns Unexpected CIDR Block

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Understanding how cidrsubnet() calculates subnets — newbits and netnum parameters

**Question**:
An engineer calls `cidrsubnet("10.0.0.0/16", 8, 3)` expecting to get the third `/24` subnet. They expect `10.0.3.0/24`. Running `terraform console` confirms this returns `"10.0.3.0/24"`. However, a colleague calls `cidrsubnet("10.0.0.0/16", 4, 3)` and gets `10.0.48.0/20` instead of what the engineer expected. The engineer asks why the colleague's call produces a different result. What explains the difference?

- A) `cidrsubnet()` only works correctly when the base prefix is `/16` or larger — `/4` arguments are invalid
- B) The second argument (`newbits = 4`) adds 4 bits to the base prefix, creating `/20` subnets (not `/24` subnets); `netnum = 3` then selects the **third** `/20` subnet within `10.0.0.0/16` — which starts at `10.0.48.0`; the result is correct: `cidrsubnet("10.0.0.0/16", 4, 3)` computes `/16 + 4 bits = /20`, and the third `/20` block in that space is `10.0.48.0/20`; the engineer's assumption that both calls would produce `/24` subnets is wrong — `newbits` controls the number of **additional bits** borrowed, not the final prefix length
- C) The difference is caused by the two engineers running different versions of Terraform — `cidrsubnet()` changed its calculation method in Terraform 1.5
- D) `cidrsubnet()` requires the third argument (`netnum`) to start at 1, not 0 — the colleague used `3` to get the third subnet, but should have used `2`

**Answer**: B

**Explanation**:
`cidrsubnet(prefix, newbits, netnum)` works as follows: `newbits` is the number of **additional bits** to borrow from the host portion of the address, increasing the prefix length. `netnum` selects which subnet number to return (zero-based). With `cidrsubnet("10.0.0.0/16", 8, 3)`: `16 + 8 = /24` subnets; the 3rd (zero-based) `/24` is `10.0.3.0/24`. With `cidrsubnet("10.0.0.0/16", 4, 3)`: `16 + 4 = /20` subnets; each `/20` covers 4096 addresses (`2^12`); the 3rd `/20` starts at offset `3 × 4096 = 12288` addresses into the `/16`, which is `10.0.48.0/20`. The `newbits` parameter is the key variable — it determines the resulting subnet size, not an absolute prefix length.

---

### Question 9 — `compact()` Does Not Remove Duplicate Values

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Understanding the difference between compact() (removes nulls/empties) and distinct() (removes duplicates)

**Question**:
An engineer has a list with duplicate values and uses `compact()` to remove them:

```hcl
locals {
  regions = compact(["us-east-1", "eu-west-1", "us-east-1", "ap-southeast-1"])
}
```

They expect `local.regions` to contain three unique values, but it still contains four — including the duplicate `"us-east-1"`. What is wrong?

- A) `compact()` only works on lists of numbers — it does not process lists of strings
- B) `compact()` requires `null` values in the list before it can remove anything — it cannot detect string duplicates
- C) **`compact()` removes `null` values and empty strings (`""`) from a list — it does not remove duplicate non-empty values**; to remove duplicates while keeping unique values, the engineer should use `distinct()`: `distinct(["us-east-1", "eu-west-1", "us-east-1", "ap-southeast-1"])` returns `["us-east-1", "eu-west-1", "ap-southeast-1"]`; alternatively, converting to a set with `toset()` also deduplicates (but removes ordering)
- D) There is no built-in Terraform function to remove duplicates from a list — the engineer must use a `for` expression with a filter

**Answer**: C

**Explanation**:
`compact(list)` has a specific purpose: it removes `null` values and empty string (`""`) elements from a list. It does not touch non-empty, non-null values, even if they appear multiple times. `distinct(list)` is the correct function for deduplication — it returns a new list with duplicate values removed, preserving the order of first occurrence. The two functions serve different purposes: `compact` for cleaning up lists that may contain null or empty placeholders (common after conditional expressions), and `distinct` for ensuring uniqueness. Knowing which cleaning function to apply in each context is a practical exam topic.

---

### Question 10 — Output Exposes a Sensitive Local Without `sensitive = true`

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Understanding that Terraform warns when an output references a sensitive value without marking the output sensitive

**Question**:
An engineer has a local declared as:

```hcl
locals {
  connection_string = "postgresql://admin:${var.db_password}@${aws_db_instance.main.address}:5432/app"
}

output "db_connection" {
  value = local.connection_string
}
```

`var.db_password` is declared with `sensitive = true`. Running `terraform apply` produces an error: `Error: Output refers to sensitive values`. What is the cause and fix?

- A) Sensitive variables cannot be used in locals — the engineer must reference `var.db_password` directly in the output block
- B) `local.connection_string` cannot include interpolation — sensitive variables must be output separately
- C) When an output's `value` expression references a **sensitive value** (directly or transitively via a local or resource attribute), Terraform requires the output to also be **explicitly marked `sensitive = true`**; without this, Terraform errors rather than accidentally exposing the sensitive value; the fix is to add `sensitive = true` to the output block: `output "db_connection" { value = local.connection_string; sensitive = true }`
- D) The error is caused by the local — locals cannot contain sensitive values; the engineer must use a `nonsensitive()` wrapper to strip the sensitivity before assigning to a local

**Answer**: C

**Explanation**:
Terraform tracks sensitivity through the expression graph. When `var.db_password` is declared `sensitive = true`, any expression that includes it — including string interpolation in a `local` — inherits the sensitive taint. `local.connection_string` is therefore a sensitive value. If an `output` block references a sensitive value without declaring `sensitive = true` on the output itself, Terraform errors with "Output refers to sensitive values" to prevent the engineer from accidentally publishing sensitive data in output. The fix is straightforward: add `sensitive = true` to the output. This causes the output value to be redacted in terminal display while still being available via `terraform output -raw db_connection` or `terraform output -json`. The `nonsensitive()` function exists but should be used carefully — it explicitly strips the sensitivity marking and allows the value to appear in plain text output.

---

### Question 11 — Variable Declared as `type = any` Causes Downstream Type Error

**Difficulty**: Hard
**Answer Type**: many
**Topic**: TWO problems caused by using type = any instead of a specific type constraint

**Question**:
An engineer declares a module variable as `type = any` to avoid dealing with type constraints. A caller passes a `number` where the module internally expects a `string`. Which TWO of the following are consequences of using `type = any` in this scenario? (Select two.)

- A) Terraform rejects `type = any` at `terraform validate` — it is not a valid type constraint
- B) **Type errors are deferred to the point of use** — with `type = any`, Terraform accepts any value the caller provides (number, string, list, etc.) without validation at variable assignment time; the type mismatch is only discovered when the value reaches an argument that requires a specific type (e.g., a resource attribute that requires `string`), producing a potentially confusing error deep in the configuration rather than at the variable boundary
- C) **The calling module gets no documentation signal about what type is expected** — `type = any` removes the self-documenting contract that a specific type constraint provides; callers must inspect the module internals to determine what type is actually needed, increasing integration errors and maintenance burden
- D) `type = any` causes Terraform to silently coerce all input values to strings before they reach the module internals — numeric inputs become their string representation automatically

**Answer**: B, C

**Explanation**:
`type = any` is a valid type constraint (A is wrong) that disables type checking entirely. Its two main practical problems are: **(B)** type mismatch errors are not caught at the variable assignment boundary — Terraform accepts the value without complaint, and the error only surfaces when the mistyped value reaches a context that requires a specific type (a resource attribute, function argument, etc.), making the error message harder to trace back to the input. **(C)** the module's interface loses its self-documenting nature — callers and operators cannot tell from the variable declaration what type to provide, leading to integration errors. `type = any` is occasionally legitimate for generic utility modules that genuinely accept multiple types, but should be used sparingly and with clear documentation. (D) is wrong — Terraform does not silently coerce types; a number passed where a string is expected will still fail with a type error when the mismatch is encountered.

---

### Question 12 — `for` Expression Filter Produces Empty List Unexpectedly

**Difficulty**: Hard
**Answer Type**: one
**Topic**: Diagnosing a for expression with an if clause that filters out all elements due to a logic error

**Question**:
An engineer writes a `for` expression to extract all production environment names from a map:

```hcl
variable "environments" {
  default = {
    web-prod  = "production"
    web-dev   = "development"
    api-prod  = "production"
    api-stage = "staging"
  }
}

locals {
  prod_names = [for name, env in var.environments : name if env != "production"]
}
```

The engineer expects `local.prod_names` to be `["web-prod", "api-prod"]` but instead gets `["web-dev", "api-stage"]`. What is wrong?

- A) `for` expressions do not support `if` clauses in Terraform — the filter must be done with `compact()` after the expression
- B) Map `for` expressions require `key => value` syntax — the engineer used list syntax and the filter is applied in reverse
- C) The **`if` clause condition is inverted** — `if env != "production"` keeps elements where the environment is **not** production, which is the opposite of the engineer's intent; to keep only production environments, the condition should be `if env == "production"`; the corrected expression is `[for name, env in var.environments : name if env == "production"]`
- D) The expression iterates over map values, not keys — `name` and `env` are swapped, so the filter is comparing the name string against `"production"` rather than the environment value

**Answer**: C

**Explanation**:
In a `for` expression, the `if <condition>` clause is a **filter that keeps elements for which the condition is `true`**. `if env != "production"` retains every element where the environment value is anything other than `"production"` — exactly the opposite of the intended behaviour. The fix is to invert the condition: `if env == "production"`. This is a straightforward logic error but one that produces a silently wrong result (no error, just the wrong data), which can be difficult to spot without testing the expression in `terraform console`. When writing `for` expressions with filters, it helps to read the condition aloud: "keep this element if env is NOT equal to production" — if that's not the intent, flip the operator.

---

### Question 13 — TWO Things `sensitive = true` on an Output Does and Does Not Protect

**Difficulty**: Hard
**Answer Type**: many
**Topic**: Understanding the precise scope of what output-level sensitive = true protects

**Question**:
Which TWO of the following statements accurately describe the behaviour of `sensitive = true` on an output block? (Select two.)

- A) **`sensitive = true` on an output suppresses the value in `terraform apply` summary output and in the `terraform output` (all-outputs) command, displaying `(sensitive value)` instead** — this prevents the value from appearing accidentally in terminal logs or CI pipeline output
- B) `sensitive = true` on an output encrypts the value before writing it to `terraform.tfstate`, protecting it from anyone with read access to the state file
- C) `sensitive = true` on an output prevents the value from being accessed by a parent module that calls the current module as a child — the output is invisible to callers
- D) **`sensitive = true` on an output does NOT prevent the value from being exposed when queried directly by name (`terraform output <name>`) or via `terraform output -json` — both commands reveal the plaintext value**, meaning the protection is limited to incidental terminal display, not direct programmatic access

**Answer**: A, D

**Explanation**:
**(A)** is correct — `sensitive = true` on an output causes Terraform to replace the value with `(sensitive value)` in the `terraform apply` completion summary and when running `terraform output` (listing all outputs). This is the primary protection: preventing values from appearing in CI logs or terminal sessions where observers are present. **(D)** is also correct — the protection is display-level only. `terraform output <name>` queries a specific output by name and reveals the plaintext value. `terraform output -json` also reveals all sensitive output values in plaintext JSON. Parent modules that access child module outputs via `module.<name>.<output>` also receive the raw value. **(B)** is wrong — `sensitive = true` does not encrypt the state file; the value is plaintext in `.tfstate`. **(C)** is wrong — parent modules can fully access sensitive outputs from child modules; the sensitivity flag affects display, not access control.

---

---

## Questions

---

### Question 1 — `check` Block Does Not Fail a Production Deployment Gate

**Difficulty**: Easy
**Answer Type**: one
**Topic**: Understanding that check block failures are non-blocking warnings — wrong tool for a deployment gate

**Question**:
An engineer wants to prevent a production deployment from completing if the application's health endpoint does not return HTTP 200. They add a `check` block:

```hcl
check "app_health" {
  data "http" "probe" {
    url = "https://${aws_lb.web.dns_name}/health"
  }

  assert {
    condition     = data.http.probe.status_code == 200
    error_message = "Health check failed: got ${data.http.probe.status_code}."
  }
}
```

During a deploy, all resources are created successfully but the health endpoint returns `503`. The engineer expects the deployment to fail. Instead, `terraform apply` exits successfully, showing the assertion failure as a warning. What is the cause, and what is the correct fix?

- A) The `check` block is syntactically wrong — the scoped `data` source must be declared outside the `check` block
- B) The health check is evaluated before the load balancer DNS is ready — add a `depends_on` inside the `check` block to delay evaluation
- C) **`check` blocks are intentionally non-blocking** — a failing `assert` inside a `check` block produces a **warning** but never prevents the apply from succeeding; this is by design for continuous health monitoring; to create a hard deployment gate, the engineer should instead use a `postcondition` inside the `aws_lb` resource's `lifecycle` block — a failing `postcondition` halts apply with a non-zero exit code after the resource is changed but before the run is considered successful
- D) `check` blocks only fail the apply when the `data` source inside them returns a non-2xx status code — any other assertion failure is treated as a warning

**Answer**: C

**Explanation**:
The `check` block was deliberately designed as a **non-blocking** health monitor. Its failures are warnings, not errors — the apply exits `0` (success) regardless of assertion results. This makes `check` useful for surfacing infrastructure health issues in dashboards and logs without risking blocked deployments for transient failures. For a hard deployment gate (where a failed health check must abort the run), the correct tool is a `postcondition` inside the resource's `lifecycle` block. A failing `postcondition` halts the apply immediately after the resource change, exits with a non-zero status code, and marks the run as failed — which is what CI/CD pipeline gates require.

---

### Question 2 — Sensitive Variable Value Found in Plaintext in State File

**Difficulty**: Easy
**Answer Type**: one
**Topic**: Understanding that sensitive = true masks terminal output but does not protect state

**Question**:
An engineer declares a database password as sensitive:

```hcl
variable "db_password" {
  type      = string
  sensitive = true
}
```

After running `terraform apply`, the engineer is auditing their security posture and opens `terraform.tfstate`. They find the password stored in plaintext under the resource's attribute map. They assumed `sensitive = true` would protect the value in state. What is the actual behaviour?

- A) This is a bug — `sensitive = true` should encrypt state file values and the engineer should file an issue with HashiCorp
- B) `sensitive = true` encrypts the value in state using a key derived from the Terraform workspace name — the engineer's state viewer is decrypting it automatically
- C) **`sensitive = true` only controls terminal display** — it causes Terraform to show `(sensitive value)` instead of the actual value in `terraform plan` and `terraform apply` output; it has **no effect on the state file**, where the value is always stored in **plaintext**; to protect sensitive values at rest, the engineer must use an **encrypted remote backend** (such as S3 with SSE-KMS or HCP Terraform), restrict access to the state file, and never commit `terraform.tfstate` to source control
- D) The state file shows plaintext only on first apply — after the next apply, Terraform replaces the plaintext with a hash of the value

**Answer**: C

**Explanation**:
`sensitive = true` is purely a **display-level** control. It instructs Terraform to suppress the value in terminal output — plan summaries, apply logs, and the `terraform output` all-outputs listing all show `(sensitive value)` instead. The actual value in `terraform.tfstate` is always stored in plaintext JSON, regardless of any `sensitive` flag. This is one of the most important security facts for the exam. The mitigation strategy has three parts: (1) use an encrypted remote backend so the state file is encrypted at rest; (2) apply strict IAM/RBAC policies to restrict who can read the state; (3) never commit `.tfstate` files to source control. For the highest security, consider using the HashiCorp Vault provider to inject dynamic, short-lived credentials rather than storing long-lived secrets in state at all.

---

### Question 3 — `self` Used in a `precondition` Causes an Error

**Difficulty**: Easy
**Answer Type**: one
**Topic**: Understanding that self is only valid in postcondition, not precondition

**Question**:
An engineer wants to verify that an EC2 instance will be placed in the correct subnet before it is created. They write:

```hcl
resource "aws_instance" "app" {
  ami           = data.aws_ami.ubuntu.id
  instance_type = "t3.micro"
  subnet_id     = var.subnet_id

  lifecycle {
    precondition {
      condition     = self.subnet_id == var.expected_subnet_id
      error_message = "Instance must be placed in the expected subnet."
    }
  }
}
```

Running `terraform plan` produces: `Error: Invalid reference — The "self" object is not available in precondition blocks`. What is the cause and fix?

- A) `self` is a reserved keyword in Terraform and cannot be used in any `lifecycle` block — replace it with the full resource reference `aws_instance.app.subnet_id`
- B) `self` is not supported for EC2 instances — it is only available in `null_resource` lifecycle blocks
- C) **`self` is only valid in `postcondition` blocks**, where it references the resource's attributes after the resource has been created or updated; in a `precondition`, the resource does not yet exist (or has not yet been changed), so `self` cannot reference any post-change attributes; to check a value that is known before the resource is changed, the condition should reference the input directly — in this case, `var.subnet_id == var.expected_subnet_id` — or reference a data source or another already-computed resource
- D) `self` requires the resource to be referenced using its full address — replace `self.subnet_id` with `module.this.aws_instance.app.subnet_id`

**Answer**: C

**Explanation**:
`self` is a special reference that represents the resource being managed, available only in contexts where the resource's post-change state is accessible. In a `postcondition`, the resource has already been created or updated, so `self` correctly refers to the resulting resource attributes. In a `precondition`, the resource change has not yet occurred — the new attribute values do not exist yet — making `self` invalid. For the specific use case in this scenario (verifying the subnet before creation), the correct approach is to compare the input value directly: `condition = var.subnet_id == var.expected_subnet_id`. Alternatively, if the subnet must be looked up (e.g., to check it belongs to the right VPC), reference a `data "aws_subnet"` block instead.

---

### Question 4 — `postcondition` Fails After Resource Is Already Created

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Understanding that a failing postcondition leaves the resource created but marks the apply as failed

**Question**:
An engineer adds a `postcondition` to an EC2 instance requiring a public IP:

```hcl
resource "aws_instance" "web" {
  ami                         = data.aws_ami.ubuntu.id
  instance_type               = "t3.micro"
  associate_public_ip_address = false

  lifecycle {
    postcondition {
      condition     = self.public_ip != null
      error_message = "Instance must have a public IP address."
    }
  }
}
```

The engineer runs `terraform apply`. The instance is created in AWS, but the apply exits with the postcondition error. On the next `terraform plan`, the engineer notices the instance is shown as already existing in state. What is happening and what is the correct fix?

- A) The `postcondition` failing prevents the resource from being written to state — the instance was not actually created in AWS
- B) Terraform automatically destroys the resource and retries the apply when a `postcondition` fails — the instance in state is from a previous run
- C) **A `postcondition` runs after the resource has been created or updated** — at that point, the resource exists in AWS and is written to state; the failing `postcondition` causes the apply to exit with an error, but the resource is already in state; the correct fix is to address the root cause: `associate_public_ip_address = false` prevents the instance from receiving a public IP, so either change this to `true`, place the instance in a subnet with `map_public_ip_on_launch = true`, or update the `postcondition` condition to match the intended design
- D) The instance exists in state only until the next `terraform refresh` — the postcondition failure marks the resource as tainted and it will be destroyed on the next plan

**Answer**: C

**Explanation**:
`postcondition` semantics are important to understand: the check runs **after** the resource change completes. This means the resource exists in AWS and is recorded in state before the postcondition is evaluated. When the condition returns `false`, the apply fails and the error message is displayed — but the resource is already created. On the next `plan`, Terraform shows the resource as existing (because it is in state). The engineer must fix the underlying issue that caused the postcondition to fail: in this case, `associate_public_ip_address = false` explicitly disables public IP assignment, so `self.public_ip` will always be `null`. The fix is to set `associate_public_ip_address = true` (or rely on the subnet's auto-assign setting), not to remove the postcondition. Postconditions catch configuration mistakes but cannot undo infrastructure that has already been provisioned.

---

### Question 5 — All `validation` Blocks on a Variable Are Evaluated

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Understanding that multiple validation blocks on a variable are all evaluated and all failures are reported

**Question**:
An engineer adds two `validation` blocks to a variable:

```hcl
variable "instance_type" {
  type = string

  validation {
    condition     = startswith(var.instance_type, "t3.")
    error_message = "Only t3 family instances are allowed."
  }

  validation {
    condition     = length(var.instance_type) <= 12
    error_message = "Instance type name must not exceed 12 characters."
  }
}
```

They run `terraform plan -var="instance_type=m5.24xlarge"` expecting Terraform to stop after the first failing validation. They are surprised to see both error messages appear. Is this correct behaviour?

- A) This is unexpected behaviour — Terraform should stop after the first failing `validation` block and only display the first error; this may indicate a bug in the version being used
- B) Only the last `validation` block is evaluated — the first block is ignored when multiple blocks exist
- C) **Yes, this is correct and expected behaviour — Terraform evaluates ALL `validation` blocks on a variable and reports every failing condition in a single error output**; this is intentional: showing all failing constraints at once allows the engineer to correct all issues with one round trip, rather than discovering them one at a time; in this case, `"m5.24xlarge"` fails both conditions (does not start with `"t3."` and is 10 characters — actually passes the length check, but the first check fails); with a value like `"m5.extremely-large"` that fails both, both messages would be reported together
- D) Multiple `validation` blocks on a single variable are not supported — Terraform will use only the first block and silently ignore subsequent ones

**Answer**: C

**Explanation**:
Multiple `validation` blocks per variable are fully supported and all are evaluated independently. When a variable value is processed, Terraform checks every `validation` block and collects all failing conditions. All error messages from all failing blocks are reported together in the error output. This batch-reporting behaviour is deliberate — it follows the principle of fail fast and report completely, so engineers can see all constraint violations at once rather than fixing one and discovering the next in a follow-up run. A variable can have as many `validation` blocks as needed, each focusing on a distinct constraint (type family check, length check, format check, etc.).

---

### Question 6 — `nonsensitive()` Strips the Sensitive Taint From a Value

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Understanding that nonsensitive() removes the sensitive marking and allows the value to appear in plain text output

**Question**:
An engineer is debugging a connection string issue in a development environment. The connection string is derived from a sensitive variable and appears as `(sensitive value)` in all output. To temporarily see the value, they wrap it in `nonsensitive()`:

```hcl
output "debug_connection" {
  value = nonsensitive(local.connection_string)
}
```

This works — the value appears in plain text during the debug session. The engineer forgets to revert the change before merging the feature branch. The change is deployed to production. What is the security risk?

- A) There is no risk — `nonsensitive()` only affects local terminal display and does not change how the value is stored in state
- B) `nonsensitive()` cannot be used with sensitive values and would have caused a validation error during `terraform validate` — the scenario is not possible
- C) **`nonsensitive()` explicitly removes the sensitive taint from a value, causing it to be displayed in plaintext in `terraform plan`, `terraform apply` summary output, and `terraform output` listings** — once merged and deployed to production, the sensitive connection string (containing the database password) will appear in CI/CD pipeline logs, any tooling that captures `terraform apply` output, and the output of `terraform output` without any masking; this represents a real credential exposure risk; the fix is to remove `nonsensitive()` and restore `sensitive = true` on the output, or remove the debug output entirely before merging
- D) The risk is minor — `nonsensitive()` only affects the current terminal session; the CI/CD pipeline will still see the value as `(sensitive value)` because it uses a different Terraform execution context

**Answer**: C

**Explanation**:
`nonsensitive(value)` is a function that **explicitly and permanently removes the sensitive taint** from a value for the purpose of that expression. Once used, the resulting value is treated as non-sensitive everywhere it flows: it appears in plan output, apply summaries, `terraform output` listings, and anywhere the value is logged. This is the correct tool when you have a value that is marked sensitive but you have verified it is safe to expose in a specific context. However, its use in a shared codebase carries the risk described in this scenario — a temporary debugging aid accidentally shipping to production. Best practice is to never commit `nonsensitive()` wrapping to shared branches; instead, use `terraform output -raw <name>` locally to view a specific sensitive output without modifying the configuration.

---

### Question 7 — `precondition` Can Reference Other Resources (Unlike `validation`)

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Understanding the broader reference scope allowed in precondition/postcondition vs the var-only restriction in validation

**Question**:
An engineer who recently learned that `validation` blocks can only reference `var.<name>` assumes the same restriction applies to `precondition` blocks. They write:

```hcl
resource "aws_instance" "web" {
  ami           = data.aws_ami.ubuntu.id
  instance_type = "t3.micro"

  lifecycle {
    precondition {
      condition     = data.aws_ami.ubuntu.architecture == "x86_64"
      error_message = "AMI must be x86_64 architecture."
    }
  }
}
```

The engineer removes this `precondition` thinking it will fail because it references `data.aws_ami.ubuntu` rather than a `var.*`. Is their assumption correct?

- A) Yes — `precondition` blocks have the same restriction as `validation` blocks and can only reference `var.<name>`
- B) Yes — `precondition` blocks can reference data sources, but only data sources declared in the same `.tf` file as the resource
- C) **No — `precondition` and `postcondition` blocks can reference any value that Terraform can resolve at apply time**, including data sources, other resource attributes, locals, and variables; the `var.<name>-only` restriction applies exclusively to `validation` blocks inside `variable` declarations, because validation runs before planning when only the variable's own value is available; by the time a `precondition` runs (just before a resource is modified during apply), data sources and other resources earlier in the dependency graph have already been resolved; the engineer's config is valid and correct — they should keep the precondition
- D) No — but `precondition` blocks cannot reference data sources; they can reference other resource attributes and variables only

**Answer**: C

**Explanation**:
The reference restriction exists because of **when** each mechanism is evaluated. `validation` blocks run before `terraform plan`, at input-variable-processing time — the only thing available at that point is the variable's own value. `precondition` and `postcondition` blocks run during `terraform apply`, after the dependency graph has been resolved and earlier resources have been applied. At that point, data sources, other resources' attributes, locals, module outputs, and variables are all available for reference. The `precondition` in this example correctly references `data.aws_ami.ubuntu.architecture` — this is a valid and idiomatic pattern for asserting prerequisite conditions about infrastructure dependencies. The engineer should keep the precondition, not remove it.

---

### Question 8 — `check` Block Requires Terraform 1.5+

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Understanding that the check block was introduced in Terraform 1.5 and requires setting required_version

**Question**:
A senior engineer adds `check` blocks to a shared module to monitor infrastructure health. When a junior engineer on the team runs `terraform init` on their machine, they get: `Error: Unsupported block type — Blocks of type "check" are not expected here`. The senior engineer's machine works fine. What is the most likely cause?

- A) The `check` block must be declared inside a `resource` block — using it at the top level of a module is unsupported
- B) `check` blocks are only supported in Terraform Cloud/HCP Terraform and cannot be used in local Terraform runs
- C) **The `check` block was introduced in Terraform 1.5** — the junior engineer is running an older version of Terraform that does not recognise the `check` block type; the fix is for the module to declare a minimum version requirement: `required_version = ">= 1.5"` in the `terraform {}` block, which will produce a clear "version too old" error rather than a confusing "unsupported block" message, and prompts the junior engineer to upgrade their Terraform CLI
- D) The `check` block is only unsupported on Windows — this is a platform compatibility issue

**Answer**: C

**Explanation**:
The `check` block was added in **Terraform 1.5** (released June 2023). Versions prior to 1.5 do not recognise it and produce an "Unsupported block type" error during parsing. The correct solution is to set the `required_version` constraint in the module's `terraform {}` block: `required_version = ">= 1.5"`. This causes Terraform to emit a clear, actionable version constraint error when an older CLI is used, rather than the confusing "unsupported block type" message. For modules using features introduced in specific versions (1.5 for `check`, 1.4 for `import` blocks, 1.3 for `optional()` in object types, etc.), setting `required_version` is a best practice that guides consumers to use a compatible CLI version.

---

### Question 9 — `postcondition` Condition Expression Throws an Error Instead of Returning `false`

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Using can() to make postcondition conditions error-tolerant when the expression might throw rather than return false

**Question**:
An engineer writes a `postcondition` to verify that at least one security group is attached to a newly created EC2 instance:

```hcl
resource "aws_instance" "app" {
  ami           = data.aws_ami.ubuntu.id
  instance_type = "t3.micro"

  lifecycle {
    postcondition {
      condition     = length(self.vpc_security_group_ids) > 0
      error_message = "Instance must have at least one security group."
    }
  }
}
```

In a specific deployment, `self.vpc_security_group_ids` is `null` (the attribute is not set). Instead of the custom `error_message`, Terraform reports: `Error in function call: Call to function "length" failed: value must not be null`. The engineer's custom message is never shown. What is the fix?

- A) `length()` cannot be used in a `postcondition` — use `self.vpc_security_group_ids != null && self.vpc_security_group_ids != []` instead
- B) `postcondition` blocks must always check for `null` using a separate `precondition` before the `postcondition` can safely call functions
- C) **The `condition` expression is throwing a function-call error rather than returning `false`** — when `self.vpc_security_group_ids` is `null`, `length(null)` errors rather than returning `0`; Terraform propagates this error directly instead of treating it as a failed condition; the fix is to **wrap the expression in `can()`** to convert any errors into `false`: `condition = can(length(self.vpc_security_group_ids) > 0)`; alternatively, add a null-guard: `condition = self.vpc_security_group_ids != null && length(self.vpc_security_group_ids) > 0`; either approach ensures the `error_message` is shown instead of a raw function error
- D) The issue is that `postcondition` does not support `length()` when the attribute type is a set — cast to a list first using `tolist()`

**Answer**: C

**Explanation**:
When a `condition` expression throws an error (rather than evaluating to `true` or `false`), Terraform reports the raw error from the function call rather than the custom `error_message`. This can produce confusing output that obscures the actual intent of the condition. Two patterns prevent this: (1) **`can(expr)`** — wraps any expression and returns `false` if the expression throws an error, making it suitable for use in `condition` where you want errors to be treated as "condition not met"; (2) **explicit null-guard** — `attr != null && length(attr) > 0` — checks for null before calling `length()`, which is more readable. The `can()` function is designed precisely for this use case: making expressions error-tolerant in contexts (conditions, validation, etc.) where a thrown error is semantically equivalent to "condition not met."

---

### Question 10 — Sensitive Output Value Revealed by `terraform output -json` in CI

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Understanding that terraform output -json reveals sensitive output values in plaintext

**Question**:
An engineer marks an output as sensitive to prevent the database connection string from appearing in CI logs:

```hcl
output "db_connection_string" {
  value     = local.connection_string
  sensitive = true
}
```

The CI pipeline uses this command to pass the connection string to a deployment script:

```bash
DB_URL=$(terraform output -json | jq -r '.db_connection_string.value')
```

A security reviewer audits the CI logs and finds the database password in plaintext in the `terraform output -json` output captured by the pipeline. The engineer is surprised — they expected `sensitive = true` to hide the value. What is the cause?

- A) `jq` strips the sensitive marking before returning the value — the issue is with the jq command, not Terraform
- B) `sensitive = true` only applies to the initial `terraform apply` output, not to subsequent `terraform output` commands
- C) **`terraform output -json` outputs all output values as plaintext JSON, including those marked `sensitive = true`** — the `sensitive` flag suppresses values in the terminal display of `terraform output` (the all-outputs listing), but programmatic queries such as `terraform output -json`, `terraform output -raw <name>`, and `terraform output <name>` all return the actual value; this is intentional — machines consuming outputs need the real value; the engineer must ensure CI pipeline output is not logged or is masked at the pipeline level (e.g., using GitHub Actions secrets masking, or marking the env var as a secret in the CI system)
- D) The CI pipeline runs as `root`, which bypasses Terraform's sensitive value masking

**Answer**: C

**Explanation**:
`sensitive = true` on an output is a **display hint for interactive terminal output** — it causes Terraform to print `(sensitive value)` instead of the actual value when running `terraform output` interactively (without a specific output name). It does not prevent the value from being retrieved programmatically. `terraform output -json` intentionally includes all values (including sensitive ones) in the JSON structure, because the primary use case is automated consumption by scripts and pipelines. The same applies to `terraform output -raw <name>` and `terraform output <name>` (single-output query). The engineer needs to apply protection at the CI layer: configure the CI system to mask the value (e.g., register it as a secret variable in the pipeline), avoid logging the `terraform output` command output, or use a secrets manager instead of Terraform outputs to pass credentials between pipeline steps.

---

### Question 11 — TWO Differences Between `check` Block and `precondition`

**Difficulty**: Hard
**Answer Type**: many
**Topic**: Two distinct behavioral differences between check blocks and preconditions beyond just blocking vs non-blocking

**Question**:
An engineer is deciding whether to use a `check` block or a `precondition` for an infrastructure assertion. They know one blocks the apply and the other doesn't. Which TWO additional differences between `check` blocks and `preconditions` should they also consider? (Select two.)

- A) **`check` blocks run on every `terraform plan` AND every `terraform apply`**, making them suitable for continuous health monitoring; a `precondition` only runs during `terraform apply` — when its resource is actually being created or modified; if no change is planned for the resource, the precondition is not evaluated during that run
- B) `check` blocks can only reference outputs from completed resources; `precondition` blocks can reference any Terraform expression
- C) **`check` blocks can optionally contain a scoped `data` source block** that is evaluated exclusively within the `check` block scope and is not available elsewhere in the configuration; `precondition` blocks do not support embedded data sources — they reference data sources declared at module scope
- D) `precondition` failures can be suppressed with a `-force` flag; `check` block failures cannot be suppressed

**Answer**: A, C

**Explanation**:
Beyond the blocking vs. non-blocking distinction, two important differences: **(A)** `check` blocks run on both `plan` and `apply` operations, providing visibility into infrastructure health on every Terraform execution, even when no changes are planned. A `precondition` only runs during apply, and only when the specific resource it is attached to is being created, updated, or destroyed — if no change is planned for that resource, the precondition is skipped entirely. **(C)** `check` blocks support an optional embedded `data` source block (a "scoped data source") that is private to the check block. This allows the check to query external state (e.g., make an HTTP request, check a DNS record) without polluting the module's data source namespace. `precondition` blocks cannot embed data sources — they reference data sources declared separately at module scope. **(B)** is wrong — preconditions can reference any resolvable Terraform expression. **(D)** is wrong — there is no `-force` flag to suppress precondition failures.

---

### Question 12 — TWO Measures Required to Properly Protect Sensitive Values in Terraform

**Difficulty**: Hard
**Answer Type**: many
**Topic**: Understanding the gap between what sensitive = true provides and what is required to actually protect secrets

**Question**:
A security team is reviewing a Terraform project that manages RDS database credentials. The engineer has applied `sensitive = true` to all relevant variables and outputs and believes this fully protects the secrets. Which TWO additional measures must be in place to achieve adequate protection of the credential values? (Select two.)

- A) Rename all sensitive variables to start with `_secret_` — Terraform treats these as encrypted at rest in state
- B) **Use an encrypted remote backend** — because `sensitive = true` does not protect the state file, and `terraform.tfstate` stores all values (including those marked sensitive) in **plaintext JSON**, the state file must be stored in a backend that encrypts data at rest and in transit; suitable options include S3 with SSE-KMS and strict bucket policies, HCP Terraform (which encrypts state by default), or other encrypted backends; without this, anyone with access to the state file can read all credentials regardless of `sensitive` flags
- C) Add `terraform plan -no-state` to all CI pipeline commands to prevent state from being written
- D) **Restrict access to the state file through IAM policies, bucket policies, or backend access controls** — even with encryption, if developers and CI pipelines have broad read access to the state backend, credentials can be extracted; the principle of least privilege should be applied so that only Terraform execution roles and specific operators can read state; this is independent of (and complementary to) backend encryption

**Answer**: B, D

**Explanation**:
`sensitive = true` provides only display-level masking — it is the thinnest layer of protection and addresses only incidental exposure in terminal logs. Two structural measures are required to actually protect credentials stored in state: **(B) Backend encryption**: the state file must reside in a backend that encrypts it at rest (S3 + SSE-KMS, HCP Terraform, etc.) and in transit (HTTPS). Without encryption, the plaintext JSON state file is readable by anyone with filesystem or bucket-level access. **(D) Access restriction**: encryption at rest is undermined if broad read access is granted to the backend. IAM/RBAC policies should limit state access to Terraform execution roles and specific operators — not to every developer or CI pipeline. Together, encryption (B) and access restriction (D) address the two threat vectors: data at rest and excessive authorized access. A third best practice (not listed here) is using dynamic secrets from HashiCorp Vault to avoid storing long-lived credentials in state at all.

---

### Question 13 — `check` Block Scoped Data Source Is Not Available Elsewhere in the Module

**Difficulty**: Hard
**Answer Type**: one
**Topic**: Understanding that a data source declared inside a check block is scoped to that check block only

**Question**:
An engineer declares an HTTP data source inside a `check` block to probe an endpoint:

```hcl
check "api_health" {
  data "http" "probe" {
    url = "https://api.example.com/health"
  }

  assert {
    condition     = data.http.probe.status_code == 200
    error_message = "API health check failed."
  }
}

output "api_status_code" {
  value = data.http.probe.status_code
}
```

Running `terraform plan` fails with: `Reference to undeclared data source — A data source "http" "probe" has not been declared`. The engineer is confused because they declared `data "http" "probe"` inside the `check` block. What is the cause?

- A) The `http` provider data source is not supported inside `check` blocks — it must be declared at module scope
- B) The `output` block must be inside the `check` block to reference its scoped data source
- C) **A `data` source declared inside a `check` block is a "scoped data source" — it exists only within the scope of that `check` block** and is not visible to the rest of the module; referencing `data.http.probe` outside the `check` block (in an `output`, resource, or local) is an error because the data source does not exist in the module's global namespace; to use the HTTP result both in a check assertion and in an output, the engineer must declare a separate `data "http" "probe"` block at module scope and reference it from both the `check` block's `assert` and the `output`
- D) Scoped data sources inside `check` blocks are only valid when the `check` block uses `depends_on` to establish ordering with the output block

**Answer**: C

**Explanation**:
Scoped data sources inside `check` blocks have **block-level scope** — they are entirely private to the `check` block that contains them and cannot be referenced from outside. This is by design: the scoped data source is a tool for the `check` block's own assertion logic (e.g., making an HTTP call to verify a health endpoint) without polluting the module's data source namespace with checks that are not part of the core infrastructure definition. If the same data source is needed both inside a `check` block assertion and in another part of the module (like an output), the solution is to declare the data source at module scope: `data "http" "probe" { url = "..." }` outside the `check` block. Both the `check` block's `assert` and the `output` can then reference `data.http.probe.status_code`. The `check` block's embedded data source is purely a convenience for self-contained assertions.

---

---

## Questions

---

### Question 1 — `terraform plan` Errors After Adding a New Module Block

**Difficulty**: Easy
**Answer Type**: one
**Topic**: New module source requires terraform init before plan/apply will work

**Question**:
An engineer adds a new module block to an existing configuration:

```hcl
module "dns" {
  source = "./modules/dns"
  zone   = var.hosted_zone
}
```

The `./modules/dns` directory exists and contains valid `.tf` files. The engineer runs `terraform plan` immediately and receives: `Error: Module not installed. Run "terraform init"`. What is the cause and fix?

- A) The `./modules/dns` directory is missing a `main.tf` file — Terraform requires this filename to recognise a local module
- B) Local path modules cannot be used until they are published to the Terraform Registry
- C) **`terraform plan` does not install or register module sources** — even for local path modules, Terraform must record the module in `.terraform/modules/modules.json` before it can be used; this registration happens during `terraform init`; the engineer must run `terraform init` after adding any new `module` block (or changing an existing `source` argument), then run `terraform plan`; `terraform init` for a local path module does not download anything — it simply registers the module path
- D) The error occurs because `./modules/dns` is a relative path — Terraform requires absolute paths for local modules

**Answer**: C

**Explanation**:
`terraform plan` and `terraform apply` require all module sources to be already installed and registered in `.terraform/modules/`. This registration step is performed by `terraform init`. For local path modules, no downloading occurs — `terraform init` simply records the relationship in `.terraform/modules/modules.json`. For remote modules (registry, Git, HTTP), `init` downloads and caches the source code. In either case, adding or changing a `module` block's `source` argument always requires re-running `terraform init` before subsequent plan/apply operations will succeed. This is a deliberate design: init is the installation step, plan/apply are execution steps.

---

### Question 2 — Child Module Variable Not Receiving Value From Root

**Difficulty**: Easy
**Answer Type**: one
**Topic**: Parent variables are not automatically inherited — must be explicitly passed as module arguments

**Question**:
An engineer has a root module variable:

```hcl
variable "environment" {
  type    = string
  default = "production"
}
```

The child module `modules/tagging/main.tf` also declares a variable named `environment`. The engineer calls the module without passing the variable:

```hcl
module "tagging" {
  source = "./modules/tagging"
}
```

Inside the child module, `var.environment` resolves to `null` (or errors if the child module has no default). The engineer expects the root `var.environment` value to be inherited automatically. What is the cause and fix?

- A) The child module must declare `inherit = true` in its `variable` block to accept values from the parent scope
- B) Variables are only automatically inherited when the child module is in the same directory as the root module
- C) **Terraform does not automatically pass any root module variables to child modules** — every input a child module needs must be explicitly assigned in the `module` block; the naming of a variable in the child module is irrelevant to whether the parent passes it; the fix is to explicitly pass the variable: `module "tagging" { source = "./modules/tagging"; environment = var.environment }`
- D) The issue is that `var.environment` has a `default`, which prevents it from being passed to child modules — only required variables are passed automatically

**Answer**: C

**Explanation**:
Module encapsulation is a core Terraform design principle. Child modules are isolated — they cannot access the calling module's variables, locals, resources, or data sources unless explicitly passed as inputs. There is no "variable inheritance" mechanism. Even if a child module declares a variable with the exact same name and type as a root module variable, the child receives nothing unless the parent explicitly assigns it in the `module` block: `environment = var.environment`. This isolation is intentional: it keeps modules self-contained, reusable, and predictable regardless of the context they are called from.

---

### Question 3 — Module Output Referenced Before It Is Declared in the Child Module

**Difficulty**: Easy
**Answer Type**: one
**Topic**: A module output that was never declared causes a reference error

**Question**:
An engineer calls a module and references one of its outputs:

```hcl
resource "aws_instance" "web" {
  subnet_id = module.networking.public_subnet_id
}
```

Running `terraform plan` fails: `Error: Unsupported attribute — This object does not have an attribute named "public_subnet_id"`. The engineer inspects `modules/networking/outputs.tf` and finds only this output declared:

```hcl
output "subnet_id" {
  value = aws_subnet.public.id
}
```

What is the cause and the two possible fixes?

- A) Module outputs must use the same name as the resource attribute they expose — `subnet_id` cannot expose `aws_subnet.public.id` without renaming the resource
- B) Module outputs are not accessible from the root module — they can only be referenced by other resources within the same child module
- C) **The output is declared as `subnet_id` in the child module, but the root module references `public_subnet_id` — the names do not match**; Terraform resolves module outputs by the exact name declared in the child module's `output` block; the two fixes are: (1) update the child module's `outputs.tf` to declare `output "public_subnet_id"` instead of `output "subnet_id"`, or (2) update the root module reference to `module.networking.subnet_id` to match the existing output name; the best choice depends on which name is more descriptive
- D) The error occurs because `outputs.tf` must be in the root module, not in the child module directory

**Answer**: C

**Explanation**:
Module outputs are accessed in the calling module using the syntax `module.<name>.<output_name>`, where `<output_name>` must exactly match the name declared in an `output` block inside the child module. There is no fuzzy matching or aliasing. In this case, the child declares `output "subnet_id"` but the root references `module.networking.public_subnet_id` — a name mismatch. Both names are valid identifiers; the issue is simply the inconsistency between declaration and reference. The fix is to make them match, either by renaming the output in the child module or by correcting the reference in the root module. When renaming outputs in shared modules, consider that existing callers will also need to update their references.

---

### Question 4 — `version` Constraint Used with a Git URL Causes `terraform init` Error

**Difficulty**: Medium
**Answer Type**: one
**Topic**: The version argument is only valid for registry sources — Git sources use ?ref= instead

**Question**:
An engineer migrates a module source from the Terraform Registry to an internal GitHub repository. They keep the `version` argument:

```hcl
module "vpc" {
  source  = "github.com/acme/terraform-modules//modules/vpc"
  version = "~> 3.0"
  cidr    = var.vpc_cidr
}
```

Running `terraform init` produces: `Error: Invalid module configuration — Cannot use version constraint with a Git source`. What is the cause and fix?

- A) The double-slash `//` in the source path is causing a parse error — replace it with a single slash
- B) Private GitHub repositories require an OAuth token configured in the `credentials` block before `version` can be used
- C) **The `version` argument is only valid for Terraform Registry and private registry sources** — for Git-based sources (including bare GitHub URLs, `git::https://`, and `git::ssh://`), `version` is not supported and causes a `terraform init` error; to pin a Git source to a specific version, use the `?ref=` query parameter in the source URL appended after the path: `"github.com/acme/terraform-modules//modules/vpc?ref=v3.0.0"`; after updating the source URL, remove the `version` argument
- D) The `version` argument syntax `"~> 3.0"` is only valid for provider version constraints — module versions use a different syntax

**Answer**: C

**Explanation**:
`version` as a `module` block argument is a feature of the Terraform Registry protocol — it tells the registry server which versions to consider and resolves the constraint against the registry's published version list. Git hosts (GitHub, GitLab, Bitbucket, etc.) have no concept of this constraint format. When Terraform encounters `version` alongside a non-registry source, it errors immediately. For Git-based modules, the equivalent of pinning a version is the `?ref=` parameter: `?ref=v3.0.0` checks out the `v3.0.0` git tag; `?ref=main` tracks the `main` branch. Using a specific tag (not a branch) provides the same immutability guarantee as a version constraint. The corrected source would be: `"github.com/acme/terraform-modules//modules/vpc?ref=v3.0.0"`.

---

### Question 5 — Module Changes Not Reflected — `terraform init` Not Re-run After Source Change

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Changing a module source or version requires terraform init to update the cache

**Question**:
An engineer bumps a Terraform Registry module version from `~> 4.0` to `~> 5.0`:

```hcl
module "vpc" {
  source  = "terraform-aws-modules/vpc/aws"
  version = "~> 5.0"
}
```

After saving the file, they run `terraform plan`. The plan shows resources and arguments from the `v4.x` module schema — new `v5.x` arguments are not recognised, and the plan appears unchanged from before. What is the cause?

- A) The Terraform Registry caches module versions permanently — once `v4.x` is cached, it is never replaced unless the `.terraform` directory is deleted manually
- B) The `~> 5.0` constraint is ambiguous — use an exact version like `= 5.1.0` so Terraform can resolve the correct version
- C) **Changing a module's `source` or `version` argument requires re-running `terraform init`** to download and cache the new version; `terraform plan` uses the module source already cached in `.terraform/modules/` and does not re-check the version constraint; without running `init`, the plan continues to use the previously downloaded `v4.x` code; the fix is to run `terraform init -upgrade` (or just `terraform init`) to resolve the updated version constraint and download the `v5.x` module
- D) Module version changes only take effect on `terraform apply` — `terraform plan` always uses the previously applied version

**Answer**: C

**Explanation**:
`terraform plan` and `terraform apply` use whatever module code is cached in `.terraform/modules/`. They do not contact the registry or re-evaluate version constraints on every run. The purpose of `terraform init` (and specifically `terraform init -upgrade`) is to re-resolve version constraints and update the cached module code when versions change. When upgrading from `~> 4.0` to `~> 5.0`: run `terraform init -upgrade` to force re-resolution of the constraint and download the new version. The `-upgrade` flag is needed when already within a cached version range; without it, `init` may determine the cached version still satisfies the constraint and skip the download.

---

### Question 6 — Root Module Cannot Access Resources Inside a Child Module Directly

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Module encapsulation — resources inside child modules are not directly accessible from outside

**Question**:
An engineer has a child module `modules/networking` that creates a VPC (`aws_vpc.main`). In the root module, they try to reference the VPC resource directly:

```hcl
output "vpc_arn" {
  value = module.networking.aws_vpc.main.arn
}
```

Running `terraform plan` fails: `Error: Unsupported attribute`. What is the cause and fix?

- A) The VPC resource ARN is not an available attribute on `aws_vpc` — use `id` instead of `arn`
- B) Resources inside child modules must be imported into the root module state before they can be referenced
- C) **Resources inside a child module are encapsulated and not directly accessible from outside the module** — the only values a child module exposes to its callers are explicitly declared `output` blocks; to access `aws_vpc.main.arn` from the root module, the child module's `outputs.tf` must declare an output: `output "vpc_arn" { value = aws_vpc.main.arn }`, and the root module then references `module.networking.vpc_arn`
- D) The correct syntax for accessing a child module resource is `module.networking::aws_vpc.main.arn` — the double-colon operator separates the module address from the resource address

**Answer**: C

**Explanation**:
Module encapsulation is fundamental to Terraform's module system. Resources, data sources, and locals inside a child module are private — they cannot be referenced by name from outside the module. The only way to expose internal values to callers is through `output` blocks. This design makes modules reusable and refactorable: internal implementation details can change without breaking callers, as long as the outputs remain stable. The fix is to add the required output to the child module: `output "vpc_arn" { value = aws_vpc.main.arn }` in `modules/networking/outputs.tf`, then reference it as `module.networking.vpc_arn` from the root. If the child module is a published/shared module, the engineer must check whether the module author exposes this attribute as an output — if not, they may need to request it or fork the module.

---

### Question 7 — Module Destroyed Unexpectedly After Being Renamed

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Renaming a module block label changes all resource addresses and causes destroy+create

**Question**:
An engineer renames a module block from `"network"` to `"networking"` for clarity:

```hcl
# Before
module "network" { ... }

# After
module "networking" { ... }
```

Running `terraform plan` shows all resources from the module being destroyed and recreated. The engineer did not change any resource configurations inside the module — only the module block label. Why?

- A) Terraform detects that the module source changed and destroys the old module's resources to avoid conflicts
- B) The rename caused a circular dependency in the dependency graph, forcing Terraform to rebuild all resources
- C) **The module block label (`"network"` vs `"networking"`) is part of every resource's state address** — resources inside the module are tracked in state as `module.network.<resource>` and `module.network.<resource>`; when the label changes to `"networking"`, Terraform sees `module.networking.<resource>` addresses with no prior state entries, concludes they are new resources to create, and sees `module.network.<resource>` entries with no configuration, concluding they should be destroyed; the fix is to use a `moved` block to tell Terraform the resources have been relocated without recreating them: `moved { from = module.network to = module.networking }`
- D) Terraform requires `terraform state mv` to be run manually for every resource inside the renamed module before plan will show no changes

**Answer**: C

**Explanation**:
In Terraform state, every resource is identified by its full address, which includes the full chain of module labels. For example, a VPC inside `module "network"` is tracked as `module.network.aws_vpc.main`. Renaming the module block to `"networking"` changes all addresses to `module.networking.aws_vpc.main`. Terraform sees these as entirely different resources — it has no memory that the label was merely renamed. The result is a destructive plan: destroy everything at the old addresses, create everything at the new addresses. The `moved` block (introduced in Terraform 1.1) is the correct and safe mechanism for renaming or restructuring module references without triggering unnecessary recreations: `moved { from = module.network; to = module.networking }`. This is analogous to using `moved` when renaming individual resources.

---

### Question 8 — `module.vpc` Outputs All Showing as `(known after apply)` at Plan Time

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Module outputs that depend on computed values will be unknown at plan time

**Question**:
A root module calls a VPC module and references one of its outputs for a security group:

```hcl
resource "aws_security_group" "app" {
  vpc_id = module.vpc.vpc_id
}
```

During `terraform plan`, the security group shows `vpc_id = (known after apply)` even though the VPC appears to already exist in state. On closer inspection, the engineer notices that the VPC module also creates a new internet gateway in this run, and `module.vpc.vpc_id` is shown as `(known after apply)`. Why?

- A) Module outputs are always `(known after apply)` — they can never be resolved at plan time
- B) The security group resource's `vpc_id` argument does not support references to module outputs — it must reference the VPC resource directly
- C) **If the module itself is being changed during this plan run** — even if only one internal resource (like the internet gateway) is new — all of the module's outputs may be marked `(known after apply)` if any output value transitively depends on a computed attribute; the root module references `module.vpc.vpc_id`, but if the `vpc_id` output value is derived from an attribute of a resource being created or modified in this apply, it cannot be resolved until apply time; the engineer should check that `module.vpc.vpc_id` is derived from a stable, already-existing resource attribute (e.g., `aws_vpc.main.id`) rather than a newly-computed one
- D) The `(known after apply)` is caused by the security group referencing the module output indirectly — use `module.vpc.vpc_id` in a `locals` block first to materialise the value before it can be used in a resource

**Answer**: C

**Explanation**:
Terraform propagates the "known after apply" state through its expression graph. If a module output's `value` expression references an attribute that will not be known until apply time (because the resource producing it is being created or modified in this run), then any expression that references that output also becomes `(known after apply)`. Even if `aws_vpc.main` already exists, if the output is computed through expressions that involve newly-created resources, or if the module is flagged for modification, some outputs may be deferred. The correct diagnosis is to inspect the module's `outputs.tf` to verify the exact expression for `vpc_id` and whether any of its dependencies are newly-created in this run. If `vpc_id = aws_vpc.main.id` and `aws_vpc.main` already exists unchanged, the output should resolve at plan time. If it doesn't, check whether any `depends_on` in the output block references a changing resource.

---

### Question 9 — TWO Issues That Require Re-running `terraform init` for Modules

**Difficulty**: Medium
**Answer Type**: many
**Topic**: Identifying which module-related changes require terraform init before plan/apply

**Question**:
Which TWO of the following changes to a module configuration require the engineer to run `terraform init` before `terraform plan` will succeed? (Select two.)

- A) Adding a new `locals` block inside an existing child module directory
- B) **Adding a new `module` block with a new `source` argument** — Terraform must install and register the module source in `.terraform/modules/` before it can be used; running `plan` without `init` produces "Module not installed"
- C) Changing a `count` argument on an existing module block from `1` to `2`
- D) **Changing a `module` block's `source` argument to a different URL or path** — when the source changes, Terraform needs to download or re-register the new source; the old cached source in `.terraform/modules/` is no longer correct; `terraform init` resolves and caches the updated source

**Answer**: B, D

**Explanation**:
`terraform init` is responsible for installing all module sources into the local `.terraform/modules/` cache. Two actions that require re-running `init`: **(B)** adding a new `module` block with any `source` — the module has never been installed before; **(D)** changing an existing `module` block's `source` to a different URL, path, or registry address — the previously cached source is stale and the new source needs to be fetched. Changes that do NOT require `init`: updating module input arguments (like `count`, `cidr`, `environment`), changing resources inside an existing child module, modifying `locals`, outputs, or other structural elements. Rule of thumb: if the `source` argument changed (or is new), run `init`. If only the module's inputs or internal logic changed, `plan` can be run directly.

---

### Question 10 — Module Published to Terraform Registry — `version` Must Be Set

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Using a registry module without a version constraint is risky and may break on future runs

**Question**:
An engineer calls a community module from the Terraform Registry without specifying a `version`:

```hcl
module "vpc" {
  source = "terraform-aws-modules/vpc/aws"
  cidr   = "10.0.0.0/16"
}
```

After several months, they run `terraform init` on a new CI runner and `terraform plan` shows a large number of unexpected changes — new resources, removed arguments, and deprecated warnings. The engineer's configuration has not changed. What is the most likely cause?

- A) Omitting `version` causes Terraform to use the oldest available version rather than the latest — the CI runner resolved a different old version
- B) Terraform Registry modules are immutable once published — the changes must have come from a different provider version, not the module
- C) **Without a `version` constraint, `terraform init` resolves to the latest published version** of the module; over several months, the module may have released a new major version with breaking changes (new required inputs, removed resources, changed defaults); on the original machine, the previously downloaded version was cached, so `plan` was stable; on the new CI runner with an empty `.terraform/modules/` cache, `init` downloaded the latest version, which introduced breaking changes; the fix is to always pin a version constraint: `version = "~> 5.0"` — this ensures `init` resolves a compatible version on any machine
- D) The issue is that `terraform.lock.hcl` was committed to the repository — this file locks modules to old versions and prevents new CI runners from getting the current version

**Answer**: C

**Explanation**:
When no `version` is specified for a registry module, `terraform init` resolves to the **latest published version**. On a machine with an existing `.terraform/modules/` cache, the cached version continues to be used. On a fresh machine (new CI runner, clean checkout), `init` downloads whatever is currently latest. If major versions have been released since the original install, breaking changes are common. The `.terraform.lock.hcl` file records provider versions but **not module versions** — modules do not have lock file entries, which makes pinning via `version` even more important. The best practice is always: specify a `version` constraint on all registry modules, use `~>` for compatible updates, and update versions deliberately rather than automatically.

---

### Question 11 — TWO Consequences of Not Declaring an Output in a Child Module

**Difficulty**: Hard
**Answer Type**: many
**Topic**: Child module encapsulation — two effects when a needed value is not declared as an output

**Question**:
An engineer's root module needs to pass a security group ID (created inside a child module) to another resource in the root module. The child module does not declare an `output` for the security group ID. Which TWO of the following are correct descriptions of what happens? (Select two.)

- A) **Terraform raises an error when the root module references `module.<name>.<attr>` for an attribute not declared as an output** — the attribute simply does not exist on the module object; the root module cannot access any value from a child module unless that value is explicitly exported via an `output` block in the child module
- B) The security group ID can still be accessed from the root module using the `data "terraform_remote_state"` data source, which bypasses module encapsulation
- C) **The only fix is to add an `output` block to the child module that exposes the security group ID** — there is no workaround; module encapsulation is enforced at the language level; the output can be declared as `output "security_group_id" { value = aws_security_group.app.id }` in the child module's `outputs.tf`, after which `module.<name>.security_group_id` becomes a valid reference in the root module
- D) The root module can reference the security group ID using `module.<name>.resource.aws_security_group.app.id` — the `resource.` prefix provides direct resource access across module boundaries

**Answer**: A, C

**Explanation**:
**(A)** is correct — module objects in Terraform only expose attributes that are explicitly declared as `output` blocks. Referencing `module.child.anything` where `anything` is not a declared output name produces an "Unsupported attribute" error at plan time. The module object's available attributes are determined solely by its `output` declarations. **(C)** is the only valid resolution — add the `output` block. There is no mechanism to bypass module encapsulation from the calling side. **(B)** is wrong — `terraform_remote_state` reads outputs from a remote state file (a completely different configuration), not from outputs of a child module in the same run; it doesn't bypass module encapsulation. **(D)** is wrong — there is no `resource.` prefix syntax for cross-module resource access; the `module.` namespace only exposes declared outputs.

---

### Question 12 — Module Refactored Internally — Root Module Plan Shows Replacements

**Difficulty**: Hard
**Answer Type**: one
**Topic**: Internal module resource address changes (due to refactoring) cause unexpected replace plans

**Question**:
An engineer refactors a child module, renaming an internal resource from `aws_subnet.public` to `aws_subnet.public_primary`. No inputs or outputs change. After running `terraform init`, the next `terraform plan` shows the subnet being destroyed and recreated. The engineer expected no infrastructure change since only the name changed. What is the cause and fix?

- A) Terraform always recreates subnets when modules are re-initialised — this is an AWS provider constraint
- B) The `terraform init` command deleted the old subnet state entry as part of module cache refresh
- C) **The resource's state address changed** — inside the module, the resource was previously tracked as `module.<name>.aws_subnet.public`; after renaming, Terraform looks for `module.<name>.aws_subnet.public_primary`, finds no state entry, and plans to create it; simultaneously, it sees `module.<name>.aws_subnet.public` in state with no matching configuration and plans to destroy it; to resolve this without recreating infrastructure, the engineer should add a `moved` block **inside the child module's** `main.tf` or `moved.tf`: `moved { from = aws_subnet.public; to = aws_subnet.public_primary }` — this instructs Terraform to update the state address without modifying the resource
- D) The replacement is caused by the subnet's `cidr_block` being a `ForceNew` attribute — any change to the subnet triggers a replace; the resource name change is unrelated

**Answer**: C

**Explanation**:
Terraform tracks resources by their full state address, which includes the resource type, name, and the full chain of module labels. When a resource is renamed inside a module, its state address changes. Terraform has no built-in concept of "this is the same resource with a different label" — it sees a new address (create) and an orphaned old address (destroy). The `moved` block, when placed inside the module, instructs Terraform to re-map the old state address to the new one during the next plan/apply, avoiding the destroy+create cycle. Inside a module, the `moved` block uses local (non-module-qualified) addresses: `from = aws_subnet.public; to = aws_subnet.public_primary`. After the `moved` block is applied once, it can be left in place (it becomes a no-op after the state is updated) or removed if all state entries have been migrated.

---

### Question 13 — Private Registry Module Requires Token But Authentication Is Not Configured

**Difficulty**: Hard
**Answer Type**: one
**Topic**: Private registry modules require credentials configured in CLI config or environment

**Question**:
An engineer's team publishes internal modules to a private Terraform registry at `registry.acme.internal`. A new developer clones the repository and runs `terraform init`. The init fails with: `Error: Failed to query available provider mirrors — Could not retrieve module metadata; 401 Unauthorized`. The module block in question is:

```hcl
module "networking" {
  source  = "registry.acme.internal/acme/networking/aws"
  version = "~> 2.0"
}
```

The module works on all other team members' machines. What is the most likely cause and fix?

- A) Private registry hostnames must be registered with HashiCorp before modules hosted on them can be downloaded — the team needs to submit a registration request
- B) The `source` format is wrong for private registries — they require a `private::` prefix
- C) **The new developer has not configured authentication credentials for the private registry** — Terraform uses the CLI configuration file (`~/.terraformrc` on Linux/macOS, `%APPDATA%\terraform.rc` on Windows) to store credentials for private registry hosts; without a `credentials` block containing a valid token for `registry.acme.internal`, all requests to that host return `401 Unauthorized`; the fix is to add the credentials block: `credentials "registry.acme.internal" { token = "<API_TOKEN>" }` — or use the `terraform login registry.acme.internal` command if the registry supports interactive login; team members whose machines already work have this configured locally
- D) The error is caused by the `version = "~> 2.0"` constraint not matching any published version — the developer should use `version = ">= 2.0"` for broader compatibility

**Answer**: C

**Explanation**:
Private Terraform registry modules require authentication. Terraform stores registry credentials in the CLI configuration file using a `credentials` block, keyed by the registry hostname. When this configuration is absent, all API calls to the private registry return `401 Unauthorized`. The CLI config file location is `~/.terraformrc` (Linux/macOS) or `%APPDATA%\terraform.rc` (Windows). The credentials block format is: `credentials "<hostname>" { token = "<token>" }`. Alternatively, `terraform login <hostname>` performs an interactive OAuth-based login and writes the resulting token to the CLI config file automatically. Since other team members' machines work, they have this credential configured locally — it is a machine-level configuration that is never committed to source control (for obvious security reasons). Onboarding documentation for teams using private registries should include the credential setup step.

---

---

## Questions

---

### Question 1 — DynamoDB Table Attribute Name Wrong — State Locking Fails

**Difficulty**: Easy
**Answer Type**: one
**Topic**: The DynamoDB lock table hash key must be exactly "LockID" — any other name causes locking failures

**Question**:
An engineer configures an S3 backend with state locking:

```hcl
terraform {
  backend "s3" {
    bucket         = "acme-tfstate"
    key            = "prod/terraform.tfstate"
    region         = "us-east-1"
    dynamodb_table = "terraform-state-lock"
    encrypt        = true
  }
}
```

The DynamoDB table was created with this Terraform resource:

```hcl
resource "aws_dynamodb_table" "lock" {
  name         = "terraform-state-lock"
  billing_mode = "PAY_PER_REQUEST"
  hash_key     = "lockId"

  attribute {
    name = "lockId"
    type = "S"
  }
}
```

Running `terraform apply` fails with: `Error: Error acquiring the state lock: ... ValidationException: One or more parameter values were invalid: Type mismatch for key lockId expected: S got: NULL`. Concurrent runs are now possible without any locking. What is the cause?

- A) The `billing_mode = "PAY_PER_REQUEST"` is incompatible with Terraform state locking — use `PROVISIONED` mode instead
- B) DynamoDB state locking is not available in all AWS regions — the table must be in `us-east-1` specifically
- C) **The DynamoDB table's hash key must be named exactly `LockID`** (capital `L`, capital `I`, capital `D`) — Terraform's S3 backend writes and reads lock records using the hard-coded attribute name `LockID`; a table with a hash key named `lockId` (wrong casing) does not have the attribute Terraform expects, causing lock operations to fail with a validation error; the fix is to recreate the DynamoDB table with `hash_key = "LockID"` and a matching `attribute { name = "LockID" type = "S" }`
- D) The DynamoDB table must be in the same AWS account as the S3 bucket but a different region to prevent cross-service conflicts

**Answer**: C

**Explanation**:
The Terraform S3 backend expects a DynamoDB hash key with the **exact case-sensitive name `LockID`**. This is hard-coded in the S3 backend implementation. If the table uses any other attribute name — even `lockId`, `lock_id`, or `Lockid` — the backend cannot write or read lock entries and produces a `ValidationException`. The table name in the `dynamodb_table` argument can be anything, but the hash key attribute name must be `LockID`. The standard pattern from the Terraform documentation and AWS provider examples always uses `hash_key = "LockID"`. Recreating the table (or using `terraform import` to adopt a corrected table) with the correct attribute name resolves the issue.

---

### Question 2 — `-reconfigure` Used Instead of `-migrate-state` — Old State Abandoned

**Difficulty**: Easy
**Answer Type**: one
**Topic**: Understanding the difference between terraform init -reconfigure and -migrate-state when changing backends

**Question**:
An engineer adds an S3 backend to a previously local-only configuration:

```hcl
terraform {
  backend "s3" {
    bucket = "acme-tfstate"
    key    = "prod/terraform.tfstate"
    region = "us-east-1"
  }
}
```

They run:

```bash
terraform init -reconfigure
```

The init succeeds. On the next `terraform plan`, all previously-managed resources appear as new resources to be created. The engineer is alarmed — their infrastructure already exists. What happened?

- A) The S3 bucket does not have versioning enabled, so the state was overwritten with an empty file during init
- B) `-reconfigure` triggers a state refresh that clears all resources older than 30 days
- C) **`terraform init -reconfigure` reinitialises the backend without migrating existing state** — it reconfigures the backend configuration but does not copy the old `terraform.tfstate` file to the new backend; the existing local state was left behind in the working directory; the new S3 backend starts with an empty state, so the next plan treats all previously-managed resources as unprovisioned; to migrate state to a new backend, the correct flag is `terraform init -migrate-state`, which prompts Terraform to copy the existing state to the new backend before switching
- D) The issue is that the S3 bucket did not exist before `terraform init` — the backend init silently created a new empty state when it could not find an existing file

**Answer**: C

**Explanation**:
Two flags serve different purposes when changing backend configuration. `terraform init -reconfigure` tells Terraform: "use this new backend configuration, but do NOT move any existing state — just reinitialise." The old state stays wherever it was (in this case, `terraform.tfstate` in the working directory). `terraform init -migrate-state` tells Terraform: "use this new backend configuration AND copy existing state from the previous backend to the new one." For any backend migration where existing infrastructure must be preserved, `-migrate-state` is the correct flag. After migration, verify with `terraform state list` that all resources appear, and then safely delete or archive the old local `terraform.tfstate` file.

---

### Question 3 — `terraform force-unlock` Runs While a Concurrent Apply Is Active

**Difficulty**: Easy
**Answer Type**: one
**Topic**: force-unlock is dangerous and should only be used when certain no other operation is running

**Question**:
An engineer runs `terraform apply` on a shared S3/DynamoDB-backed workspace. The apply is taking a long time and they suspect it has hung. A colleague runs `terraform force-unlock <LOCK_ID>` from their workstation to clear the lock so they can investigate. Two minutes later, the original engineer's apply completes successfully and writes its final state to S3. The colleague then immediately runs `terraform apply` — the plan shows a large number of unexpected changes. What is the risk that was realised?

- A) `terraform force-unlock` also rolls back any changes already made to cloud resources — the original apply's cloud changes were reverted
- B) There is no risk — `force-unlock` only releases the DynamoDB entry and has no effect on the state file itself
- C) **`terraform force-unlock` releases the DynamoDB lock record without any awareness of whether the locked operation is actually complete** — by unlocking while the original apply was still writing state, the colleague created a window where both operations could write state concurrently; the original apply wrote its final state, but a subsequent operation could read a stale state before that write landed, leading to conflicting state records; the safe use of `force-unlock` requires first **confirming with certainty** that no Terraform operation is running (e.g., the process has crashed, the CI job has been killed) — it must never be used as a shortcut to interrupt or "unstick" an operation that is still in progress
- D) The unexpected plan changes are caused by `force-unlock` incrementing the state serial number — the colleague's plan is reading a state with a higher serial than expected

**Answer**: C

**Explanation**:
`terraform force-unlock` removes the DynamoDB lock record unconditionally, with no check on whether the operation holding the lock is still running. It is designed for recovery from **crashed or orphaned processes** — situations where a process died without releasing its lock. Using it while an operation is still active is dangerous because it removes the mutual exclusion that prevents concurrent state writes. Two `terraform apply` operations writing state simultaneously can produce an inconsistent state (partial writes, serial conflicts, attribute mismatches) — which explains the unexpected plan changes the colleague saw. The correct procedure when a lock appears stuck: (1) check whether the locking process is truly dead (check CI job status, check Terraform Cloud run status); (2) only run `force-unlock` with the specific lock ID from the error message if you have confirmed the process is no longer running.

---

### Question 4 — `TF_LOG_CORE=DEBUG` Set But Provider API Calls Missing From Logs

**Difficulty**: Medium
**Answer Type**: one
**Topic**: TF_LOG_CORE captures only Terraform core logs — provider-level debugging requires TF_LOG_PROVIDER

**Question**:
An engineer is troubleshooting why an AWS resource is being re-created on every apply. They enable debug logging:

```bash
export TF_LOG_CORE=DEBUG
terraform apply 2>debug.log
```

They examine `debug.log` and find core planning logic but **no AWS API call details** — no HTTP requests, no responses, no provider plugin activity. They expected to see the full API conversation between Terraform and AWS. What is the cause and fix?

- A) Provider API calls are only visible when running `terraform apply` with the `-trace` flag, not via environment variables
- B) The `2>debug.log` redirection captures stderr but provider calls are written to a separate file in `.terraform/logs/`
- C) **`TF_LOG_CORE` controls logging only for the Terraform core binary** — it excludes provider plugin processes; AWS API calls, provider startup messages, and provider-level debug output are controlled by the separate `TF_LOG_PROVIDER` variable; to capture provider API calls, the engineer should set `TF_LOG_PROVIDER=TRACE` (or `DEBUG`); to capture both core and provider output in one go, set the unified `TF_LOG=TRACE` which applies to both; `TF_LOG_CORE` and `TF_LOG_PROVIDER` exist for cases where only one layer needs verbose output, avoiding the noise of the other
- D) Provider API calls are only logged when using HCP Terraform remote execution — local runs do not capture provider HTTP traffic regardless of log settings

**Answer**: C

**Explanation**:
Terraform's logging system distinguishes between two execution layers: (1) the **Terraform core binary** (planning, state management, graph resolution) — controlled by `TF_LOG_CORE`; (2) **provider plugins** (the actual API calls to AWS, Azure, GCP etc.) — controlled by `TF_LOG_PROVIDER`. Setting only `TF_LOG_CORE=DEBUG` produces planning and internal Terraform messages but no provider plugin output. For AWS API debugging (to see request/response payloads, error details, retry logic), `TF_LOG_PROVIDER=TRACE` is needed. The simplest approach when debugging unknown issues is to set `TF_LOG=TRACE`, which applies to both layers simultaneously. Use the split variables (`TF_LOG_CORE` and `TF_LOG_PROVIDER`) when the source of a problem is known and you want to reduce log noise from the unrelated layer.

---

### Question 5 — `terraform state mv` Done Without Updating HCL — Plan Shows Destroy and Create

**Difficulty**: Medium
**Answer Type**: one
**Topic**: terraform state mv moves the state address but if config is not updated to match, plan shows destroy+create at new/old addresses

**Question**:
An engineer renames an S3 bucket resource from `aws_s3_bucket.logs` to `aws_s3_bucket.access_logs` in the state only:

```bash
terraform state mv aws_s3_bucket.logs aws_s3_bucket.access_logs
```

The command succeeds. However, the engineer forgets to rename the resource block in `main.tf` — it still reads `resource "aws_s3_bucket" "logs"`. The next `terraform plan` shows:

- Destroy `aws_s3_bucket.access_logs` (exists in state, no config)
- Create `aws_s3_bucket.logs` (exists in config, no state)

What happened and what is the fix?

- A) `terraform state mv` always triggers a recreate — use `terraform state replace-provider` instead for safe renames
- B) The plan is correct — `state mv` only works permanently after `terraform apply` confirms the rename
- C) **`terraform state mv` moves the address in state but does not modify any `.tf` files** — after the command, state has `aws_s3_bucket.access_logs` but the configuration still has `resource "aws_s3_bucket" "logs"`; Terraform sees two mismatches: an orphaned state entry (`access_logs`) with no config, and a config resource (`logs`) with no state entry; to complete the rename, the engineer must also update `main.tf` to use `resource "aws_s3_bucket" "access_logs" { ... }`; after that change, state and config are aligned and `terraform plan` will show no changes; alternatively, the modern approach is to rename only the config resource and use a `moved` block, which avoids the need to manually run `state mv`
- D) The fix is to run `terraform state mv aws_s3_bucket.access_logs aws_s3_bucket.logs` to revert the state change, then rename only the HCL resource block

**Answer**: C

**Explanation**:
`terraform state mv` is a state-only operation — it modifies the state file's internal address mapping but leaves all `.tf` configuration files untouched. When you rename a resource in state without a matching rename in configuration, you create a mismatch on both sides: the new state address (`access_logs`) has no configuration counterpart, so Terraform plans to destroy it; the old configuration resource (`logs`) has no state entry, so Terraform plans to create it. Both the state AND the configuration must use the same address for Terraform to recognise them as the same resource. The correct two-step `state mv` workflow: (1) run `terraform state mv old_address new_address`; (2) rename the resource block in configuration to match. The `moved` block (Terraform 1.1+) is cleaner because it handles both the state address update and the configuration rename in a single declarative step during `terraform apply`.

---

### Question 6 — Sentinel `hard-mandatory` Policy Cannot Be Overridden

**Difficulty**: Medium
**Answer Type**: one
**Topic**: hard-mandatory enforcement level blocks a run unconditionally — even org owners cannot override it

**Question**:
An HCP Terraform organisation enforces a Sentinel policy that requires all EC2 instances to use approved AMI IDs. The policy is configured with `enforcement_level = "hard-mandatory"`. A team lead deploys a new configuration using a custom AMI not in the approved list. The policy check fails. The team lead is an organisation **Owner** (the highest HCP Terraform role) and clicks the "Override" button in the HCP Terraform UI — but the button is disabled. They escalate to HashiCorp support, believing this is a bug. Is it?

- A) Yes — organisation Owners should always be able to override any policy; a disabled override button is a bug
- B) No — the override button is disabled because the workspace must be in "admin" mode for owners to override Sentinel policies
- C) **No — `hard-mandatory` is the only Sentinel enforcement level that cannot be overridden by any user, regardless of role** — the three enforcement levels are: `advisory` (failure is a warning, run proceeds automatically); `soft-mandatory` (failure blocks the run, but an authorised user such as an Owner can click Override to allow the run to proceed); `hard-mandatory` (failure unconditionally blocks the run — the Override button is permanently disabled and no role has the ability to proceed); to resolve the team lead's situation, either the configuration must be updated to use an approved AMI, or a HashiCorp Sentinel policy administrator must change the enforcement level or update the approved AMI list in the policy
- D) No — only users with the Sentinel policy management permission can override `hard-mandatory` policies, and the team lead's Owner role does not include this permission by default

**Answer**: C

**Explanation**:
Sentinel provides three enforcement levels with a clear escalating hierarchy. `advisory` is purely informational — it logs a warning but never blocks a run. `soft-mandatory` blocks the run until an authorised user (a user with Override permission, typically an Owner) manually approves overriding the failing policy. `hard-mandatory` provides the strongest enforcement: **no user — not even organisation Owners, not HashiCorp support — can override it through the UI or API**. The run is permanently blocked until the configuration change itself satisfies the policy. This is by design for compliance mandates that must not allow exceptions (e.g., CIS benchmarks, regulatory requirements). Organisations should use `hard-mandatory` only for truly non-negotiable controls and `soft-mandatory` for policies that might need legitimate exceptions.

---

### Question 7 — HCP Terraform Workspace Variable Silently Overrides `terraform.tfvars`

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Workspace variables in HCP Terraform take precedence over all file-based and CLI variable sources

**Question**:
A team uses HCP Terraform with a VCS-connected workspace. The repository contains a `terraform.tfvars` file setting `instance_type = "t3.large"`. Despite this, every apply deploys `t3.micro` instances. The engineer has confirmed the `terraform.tfvars` file is correct and in the right directory. Runs complete without errors. What is the most likely cause?

- A) HCP Terraform ignores `terraform.tfvars` in all cases — file-based variable files are not supported in remote runs
- B) The `terraform.tfvars` file must be named `override.tfvars` for HCP Terraform to load it during remote runs
- C) **A workspace variable named `instance_type` is set to `"t3.micro"` in the HCP Terraform workspace settings** — workspace variables have the **highest precedence** among all variable sources in HCP Terraform runs; they override `terraform.tfvars`, `.auto.tfvars`, `-var` flags, and `TF_VAR_` environment variables; the engineer should check the workspace's "Variables" tab in the HCP Terraform UI and remove or update the `instance_type` workspace variable; workspace variables are intentionally the highest-priority source so that operators can enforce environment-specific values without modifying VCS-tracked files
- D) HCP Terraform caches variable values from the first run — the workspace is using a stale variable value; run `terraform init -reconfigure` to clear the variable cache

**Answer**: C

**Explanation**:
In HCP Terraform runs, variable precedence follows a specific order (from lowest to highest): defaults in `variable` blocks → `terraform.tfvars` → `.auto.tfvars` → `TF_VAR_` env vars → workspace variables set in HCP Terraform UI/API. Workspace variables are intentionally the highest-priority source. This design allows operations teams to set environment-specific values (different regions, instance sizes, feature flags per environment) in the workspace UI without modifying tracked configuration files. When a workspace variable and a `tfvars` file set the same variable, the workspace variable always wins — silently. Engineers should always check the workspace's Variables tab when a value is not matching expectations, especially when the configuration files appear correct. This is a commonly misunderstood precedence issue on the exam.

---

### Question 8 — `terraform_remote_state` Errors Because Output Not Declared in Source Workspace

**Difficulty**: Medium
**Answer Type**: one
**Topic**: terraform_remote_state can only access values explicitly declared as outputs in the source workspace configuration

**Question**:
A team reads networking infrastructure outputs from a separate workspace:

```hcl
data "terraform_remote_state" "networking" {
  backend = "remote"
  config = {
    organization = "acme-corp"
    workspaces = {
      name = "networking-production"
    }
  }
}

resource "aws_instance" "app" {
  subnet_id = data.terraform_remote_state.networking.outputs.private_subnet_id
}
```

Running `terraform plan` fails: `Error: Unsupported attribute — This object does not have an attribute named "private_subnet_id"`. The engineer confirms the networking workspace exists and has a working state. What is the cause?

- A) The `terraform_remote_state` data source uses `backend = "remote"` but should use `backend = "cloud"` for HCP Terraform workspaces
- B) Cross-workspace state access requires a team token with Admin-level permissions on the networking workspace
- C) **`terraform_remote_state` only exposes values that are explicitly declared as `output` blocks in the source workspace's Terraform configuration** — the networking workspace's state may contain a `private_subnet_id` attribute on a resource, but unless the networking workspace declares `output "private_subnet_id" { value = ... }` in its configuration, the value is not exposed through the `outputs` object of `terraform_remote_state`; the fix is to add the required output to the networking workspace's configuration: `output "private_subnet_id" { value = aws_subnet.private.id }`, apply it, and the consuming workspace can then reference `data.terraform_remote_state.networking.outputs.private_subnet_id`
- D) The `outputs` attribute path is incorrect — use `data.terraform_remote_state.networking.state.private_subnet_id` to access resource attributes directly from remote state

**Answer**: C

**Explanation**:
`terraform_remote_state` only provides access to values that have been explicitly declared as `output` blocks in the source workspace. It does not allow arbitrary access to resource attributes in the remote state — the outputs act as a defined API between workspaces. This encapsulation is intentional: it forces workspace authors to be explicit about what they share, creating a stable interface. If `private_subnet_id` exists as a resource attribute in the networking workspace but has no corresponding `output` declaration, it is invisible to `terraform_remote_state` consumers. Adding the output, running `terraform apply` in the networking workspace to publish it, and then re-running the consuming workspace's plan resolves the error. This pattern is analogous to module output encapsulation — the `output` block is the deliberate contract.

---

### Question 9 — `terraform login` Token Not Available in CI — Env Var Alternative Needed

**Difficulty**: Medium
**Answer Type**: one
**Topic**: terraform login stores tokens in a local file not available in CI — TF_TOKEN_* env var is the correct CI approach

**Question**:
A developer successfully authenticates to HCP Terraform using `terraform login` on their laptop. They then add the same configuration to a CI/CD pipeline (GitHub Actions) and expect the pipeline to be authenticated automatically. The CI job fails: `Error: Required token could not be found: No credentials for app.terraform.io`. The developer is confused because their local machine works perfectly. What is the cause and fix?

- A) `terraform login` authentication tokens expire after 24 hours — the developer must re-run `terraform login` in the CI job before each run
- B) GitHub Actions blocks outbound connections to `app.terraform.io` for security — the organisation's GitHub Actions settings must whitelist the HCP Terraform domain
- C) **`terraform login` stores the authentication token in a local file on the developer's machine** (`~/.terraform.d/credentials.tfrc.json`) — this file exists only on that machine and is never available in CI runners, which start from a clean environment on every job; to authenticate Terraform in a CI/CD pipeline, the correct approach is to store the HCP Terraform API token as a CI secret and expose it via the `TF_TOKEN_app_terraform_io` environment variable (e.g., `TF_TOKEN_app_terraform_io: ${{ secrets.TF_API_TOKEN }}` in GitHub Actions); Terraform reads this environment variable automatically instead of the credentials file
- D) The CI pipeline must run `terraform init` with the `-token` flag pointing to a credentials file bundled in the repository

**Answer**: C

**Explanation**:
`terraform login` performs an interactive browser-based OAuth flow and writes the resulting API token to `~/.terraform.d/credentials.tfrc.json` — a user-specific file on the local machine. CI runners are ephemeral environments that start fresh on each job run, with no access to a developer's home directory. The standard CI authentication pattern is: (1) generate a team token (or user token) in the HCP Terraform UI; (2) store it as an encrypted secret in the CI system (GitHub Actions secret, GitLab CI variable, etc.); (3) expose it to the Terraform process via the `TF_TOKEN_app_terraform_io` environment variable. The environment variable format is `TF_TOKEN_<hostname_with_dots_replaced_by_underscores>`. Terraform checks for `TF_TOKEN_*` variables before the credentials file, so CI pipelines work without any file system setup. Using team tokens (rather than personal user tokens) for CI is also a security best practice.

---

### Question 10 — Run Triggers Not Configured — Workspace B Not Auto-Triggered

**Difficulty**: Medium
**Answer Type**: one
**Topic**: HCP Terraform run triggers must be explicitly configured — workspace B does not automatically follow workspace A

**Question**:
A team has two HCP Terraform workspaces: `networking` (manages VPCs and subnets) and `compute` (manages EC2 instances that depend on `networking` outputs). The team assumes that when `networking` completes an apply, `compute` will automatically queue a new run to pick up any networking changes. After updating security group rules in `networking`, the `compute` workspace does not receive a new run. The EC2 instances are still using stale subnet configurations. What is the cause?

- A) HCP Terraform only auto-triggers dependent workspaces when the source workspace is connected to a VCS repository — API-driven workspaces do not support automatic triggering
- B) Auto-triggering between workspaces requires both workspaces to be in the same HCP Terraform Project
- C) **HCP Terraform does not automatically detect dependencies between workspaces or trigger runs based on them** — run triggers between workspaces must be **explicitly configured** in the `compute` workspace settings under "Run Triggers"; once configured, when `networking` completes a successful apply, HCP Terraform queues a new plan-and-apply run in `compute`; without this explicit configuration, the two workspaces are entirely independent — no matter how many times `networking` applies, `compute` never receives an automatic trigger; the engineer must navigate to the `compute` workspace settings, add `networking` as a source workspace under Run Triggers, and re-apply
- D) Run triggers require the `terraform_remote_state` data source to be configured in the dependent workspace before HCP Terraform can detect the dependency and trigger automatically

**Answer**: C

**Explanation**:
HCP Terraform workspaces are isolated by default — there is no automatic dependency detection or cascading apply behaviour. Run triggers are an explicit, manually-configured feature. In the consuming workspace (`compute`), an operator adds the source workspace (`networking`) as a run trigger source in the workspace settings. After this configuration, whenever `networking` completes a successful apply, HCP Terraform automatically queues a new run in `compute`. This explicit configuration is intentional: implicit auto-triggering based on state-reading relationships could cause unexpected cascading applies in large organisations. The run trigger feature, combined with `terraform_remote_state` for data sharing, is the correct pattern for orchestrating dependent workspaces. Note: run triggers fire on successful apply completion, not on every plan.

---

### Question 11 — HCP Terraform Health Assessment Does Not Auto-Remediate Drift

**Difficulty**: Hard
**Answer Type**: one
**Topic**: Health assessments detect and report drift on a schedule but never automatically apply changes to fix it

**Question**:
An operations team enables Health Assessments on their HCP Terraform workspace, setting it to run every 24 hours. After a cloud engineer manually modifies a security group in the AWS Console (creating drift), the health assessment runs and reports the drift. The operations team then waits, expecting HCP Terraform to automatically queue an apply to restore the configuration to the desired state. After several hours, no apply has run. Is this expected behaviour?

- A) No — Health Assessments are supposed to queue a remediation apply automatically; the delay indicates a workspace configuration issue such as auto-apply being disabled
- B) No — Health Assessments automatically apply corrections for drift on resources tagged with `health_assessment = "auto_remediate"` in their Terraform configuration
- C) **Yes — Health Assessments in HCP Terraform are a drift detection and reporting tool only; they never automatically queue or execute remediation applies** — when a health assessment detects drift (via an internal `terraform plan -refresh-only` equivalent), it surfaces the results in the HCP Terraform UI, sends notifications through configured channels (email, Slack), and updates the workspace's health status indicator; it is the responsibility of an operator to review the drift report and manually queue a new plan-and-apply run (or configure auto-apply) to remediate the drift; automatic remediation is not a health assessment feature because blindly re-applying in response to drift could mask legitimate manual changes or cause unintended infrastructure modifications
- D) No — Health Assessments in HCP Terraform trigger a speculative plan run that is automatically applied if the drift is smaller than a configurable threshold

**Answer**: C

**Explanation**:
Health Assessments are a **scheduled drift detection** feature — they run `terraform plan -refresh-only` on a configurable schedule (e.g., every 24 hours or every hour) and surface the results in the HCP Terraform UI and notification channels. They answer the question: "has the actual state of my infrastructure drifted from what Terraform expects?" They do not answer the question by fixing the drift. There is no auto-remediation capability. This is deliberate: not all drift is undesirable (e.g., a database's allocated storage might have been legitimately increased by a DBA), and automatically re-applying could revert intentional manual changes or trigger disruptive replacements. The correct response to a health assessment drift alert is for an operator to review the change, decide whether to remediate, and manually queue or approve a plan-and-apply run.

---

### Question 12 — TWO Safeguards Required Before Running `terraform state push`

**Difficulty**: Hard
**Answer Type**: many
**Topic**: terraform state push is destructive — two safeguards must be in place to prevent overwriting newer or correct state

**Question**:
Which TWO safeguards must be in place before running `terraform state push` against a remote backend to prevent irreversible state damage? (Select two.)

- A) **Verify that the serial number in the local state file being pushed is equal to or greater than the serial in the remote state** — `terraform state push` overwrites the remote state unconditionally; if the local file being pushed has a lower serial number than the current remote state, the push overwrites newer remote state with older data, potentially losing records of resources created, modified, or destroyed since the local file was saved; backends with versioning (such as S3 with versioning enabled) allow recovery, but the damage may not be noticed immediately
- B) Run `terraform validate` on the local state file before pushing to check for schema errors
- C) **Confirm that no Terraform operation is currently running against the remote backend** — if a plan or apply is in progress, pushing a state file mid-operation creates a race condition where two processes have divergent views of infrastructure truth; the running operation may complete and overwrite the pushed state, or the pushed state may cause the in-progress operation to act on stale resource information; always verify the workspace/backend is idle before using `state push`
- D) Run `terraform plan -refresh-only` after pushing to confirm the state matches cloud reality before running any apply

**Answer**: A, C

**Explanation**:
`terraform state push` is one of the most dangerous Terraform operations because it overwrites the authoritative remote state without a safety prompt or undo mechanism. Two safeguards are critical: **(A) Serial verification** — the state serial is an integer that increments with every state write; pushing a state with a lower serial than the current remote state overwrites newer data; before pushing, run `terraform state pull | jq '.serial'` to check the remote serial and compare it to the local file's serial; only push if the local serial is at least as high, or if you are deliberately rolling back a corrupt state (in which case you need to manually increment the serial before pushing); **(C) No concurrent operations** — pushing during an active operation creates state divergence; the workspace must be idle, the backend lock should be free, and ideally the push is performed during a maintenance window. **(B)** is wrong — `terraform validate` works on configuration, not state files. **(D)** is reasonable post-push verification but is not a safeguard before pushing.

---

### Question 13 — TWO HCP Terraform Mechanisms That Eliminate Storing Static Credentials

**Difficulty**: Hard
**Answer Type**: many
**Topic**: Dynamic provider credentials (OIDC) and team tokens eliminate two different kinds of static credential storage

**Question**:
A security team reviews an HCP Terraform organisation and identifies two categories of static credentials that create security risks: (1) long-lived cloud provider credentials (AWS access keys) stored as sensitive workspace environment variables; (2) individual user API tokens used in CI/CD pipelines. Which TWO HCP Terraform mechanisms eliminate each of these risks respectively? (Select two.)

- A) **Dynamic Provider Credentials using OIDC (OpenID Connect)** — eliminates the need for static cloud provider credentials (AWS access keys, Azure service principal secrets, GCP service account keys) stored in workspace variables; instead, HCP Terraform workspaces present a signed OIDC token to the cloud provider's IAM system; the cloud provider validates the token against a configured OIDC trust relationship and returns short-lived credentials scoped to that specific run; credentials automatically expire and are never stored in HCP Terraform; this removes static `AWS_ACCESS_KEY_ID` / `AWS_SECRET_ACCESS_KEY` environment variables from workspace settings entirely
- B) Sentinel policies with `hard-mandatory` enforcement can prevent static credentials from being added to workspace variables — this is equivalent to eliminating them
- C) **Team Tokens** — eliminate the need for individual user API tokens in CI/CD pipelines; instead of each CI pipeline authenticating to HCP Terraform with a specific user's personal token (which is tied to an individual's account, expires with their employment, and may have excessive personal permissions), a Team Token represents the team's combined access to all assigned workspaces; the team token can be rotated independently of any individual, scoped to only the workspaces the team can access, and stored as a CI system secret without tying pipeline access to any employee's personal credentials
- D) Variable Sets can store cloud credentials centrally — this reduces credential duplication but does not eliminate the static credentials themselves

**Answer**: A, C

**Explanation**:
Two distinct credential categories with two distinct HCP Terraform solutions: **(A) Dynamic Provider Credentials / OIDC** addresses **cloud provider authentication** — the elimination of static AWS/Azure/GCP credentials stored as sensitive environment variables in workspace settings. With OIDC, HCP Terraform becomes a trusted identity provider; each run receives a short-lived, automatically-expiring token from the cloud provider with only the permissions needed for that run. This is significantly more secure than long-lived access keys. **(C) Team Tokens** address **HCP Terraform authentication** in automated systems — the elimination of individual user tokens in CI/CD pipelines. Team tokens are service-account-like credentials that are not tied to a specific user's lifecycle, can be scoped by team-level workspace access, and are the recommended authentication method for any non-interactive system. **(B)** is wrong — Sentinel can enforce policy but cannot eliminate credentials that are already stored. **(D)** is wrong — variable sets centralise credentials but do not eliminate them; the static values still exist, just in one place instead of many.

---