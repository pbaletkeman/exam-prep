# Terraform Associate Exam Questions

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

---

### Question 14 — Providers Not Found After Cloning

**Difficulty**: Easy
**Answer Type**: one
**Topic**: Understanding that terraform init is required after cloning before any other terraform commands

**Question**:
A new engineer clones a Terraform repository and runs `terraform validate` to check the configuration syntax. Terraform returns an error saying the provider plugins are not installed. The engineer's configuration has a valid `required_providers` block. What is the most likely cause and fix?

- A) The `required_providers` block is missing a `version` constraint — Terraform cannot validate without an exact version specified
- B) `terraform validate` requires elevated OS permissions to read provider plugins — the engineer should run the command as an administrator
- C) The engineer has not run **`terraform init`** — until `terraform init` is executed in the working directory, no provider plugins are downloaded; the `.terraform/providers/` directory does not exist yet; running `terraform init` will download the required providers and allow validation (and apply) to proceed
- D) The engineer must manually download the provider binary from the Terraform Registry and place it in the `.terraform/` directory

---

### Question 15 — Unexpected Provider Upgrade Breaks a Pipeline

**Difficulty**: Easy
**Answer Type**: one
**Topic**: Understanding the role of .terraform.lock.hcl in preventing unintended provider upgrades

**Question**:
A CI pipeline runs `terraform init` and `terraform plan` on every pull request. After a new AWS provider minor version is released, the pipeline starts failing with API compatibility errors — but no configuration files have changed. What is the most likely cause?

- A) The CI pipeline is running `terraform init -upgrade` by default, which always installs the latest provider regardless of constraints
- B) The `.terraform.lock.hcl` file is **not committed to version control** — without it, each `terraform init` run resolves the newest version matching the constraint; when the new provider version was released, the pipeline installed it automatically, introducing the API compatibility issue; committing `.terraform.lock.hcl` would pin the exact version and prevent unintended upgrades
- C) The `required_providers` block uses `>=` instead of `~>`, which always installs the absolute latest provider version regardless of major version boundaries
- D) CI pipelines cannot use `.terraform.lock.hcl` — lock files only work on developer machines

---

### Question 16 — Provider Alias Configurations Deployed to Wrong Region

**Difficulty**: Easy
**Answer Type**: one
**Topic**: Understanding that provider alias must be explicitly referenced in a resource block or Terraform uses the default provider

**Question**:
An engineer configures two AWS provider blocks — one for `us-east-1` (default) and one for `eu-west-1` (with `alias = "europe"`). They intend to create an S3 bucket in `eu-west-1` but forget to add `provider = aws.europe` to the resource block. After `terraform apply`, they find the bucket was created in `us-east-1`. What explains this?

- A) Terraform randomly selects a provider configuration for each resource; the engineer got unlucky
- B) The `alias = "europe"` configuration is ignored unless a `region` argument is also added to the resource block
- C) When a resource block does **not specify a `provider` meta-argument**, Terraform uses the **default (non-aliased) provider configuration** — in this case `us-east-1`; aliased providers are only used when explicitly referenced with `provider = aws.europe` in the resource block
- D) Terraform always uses the last declared provider block; since the `eu-west-1` block was declared second, it should have been used

---

### Question 17 — State File Deleted Accidentally

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Understanding the consequences of losing the state file and the recovery path

**Question**:
An engineer accidentally deletes `terraform.tfstate` from a project using a local backend. The actual AWS infrastructure (several EC2 instances, a VPC, and S3 buckets) still exists. When the engineer runs `terraform plan`, Terraform proposes creating all the resources from scratch. What explains this, and what is the correct recovery path?

- A) Terraform proposes creating resources because it detected the missing state file and automatically marked all resources for replacement; the engineer should run `terraform apply` to proceed
- B) Terraform's plan is based on **state**, not direct cloud observation during planning — with no state file, Terraform sees no known resources and plans to create everything to match the configuration; the correct recovery is to **import each existing resource** using `import` blocks or the `terraform import` CLI, which re-establishes the state file entries so Terraform knows what already exists; after importing, `terraform plan` should show no changes
- C) The plan is safe to apply — Terraform detects existing resources before creating them and will skip any that already exist
- D) The engineer should restore the state file from `.terraform.tfstate.backup` which Terraform keeps permanently as a full history

---

### Question 18 — terraform.tfstate.backup Not a Full History

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Understanding that .backup holds only the immediately previous state, not a full version history

**Question**:
An engineer's team relies on `terraform.tfstate.backup` as their state history strategy. They run `terraform apply` on Monday (apply 1), Wednesday (apply 2), and Friday (apply 3). On Friday evening they discover a serious misconfiguration introduced on Wednesday. They try to restore the state from `.backup`. What problem will they encounter?

- A) No problem — `.terraform.tfstate.backup` retains the last 30 days of state history as rotated snapshots
- B) `terraform.tfstate.backup` contains the state from before the **most recent apply only** — it holds the state from after apply 2 (Wednesday), not after apply 1 (Monday); there is no built-in mechanism to recover the state from before Wednesday; this is why production teams use remote backends with versioning (e.g., S3 with versioning enabled) or HCP Terraform, which retain a full state version history
- C) `.terraform.tfstate.backup` cannot be restored — it is a read-only audit file
- D) Terraform replaces `.terraform.tfstate.backup` only when a destroy is run — the file still contains the state from before apply 1

---

### Question 19 — Sensitive Output Visible in State

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Understanding that sensitive=true masks terminal output but does not protect state

**Question**:
A security auditor reviews a Terraform project and raises a finding: "The database password is stored in plaintext in the state file." The team responds: "We marked the output as `sensitive = true`, so the password is protected." Is the team's response correct, and what is the actual security posture?

- A) The team is correct — `sensitive = true` encrypts the value in the state file using AES-256
- B) The team is incorrect — **`sensitive = true` only suppresses the value in terminal output and plan output**; it does NOT encrypt or redact the value in `terraform.tfstate`; all resource attributes, including passwords and secrets, are stored in the state file in plaintext regardless of sensitivity markings; the correct protection is to store state in an **encrypted remote backend** (e.g., S3 with `encrypt = true`, or HCP Terraform which encrypts state at rest automatically)
- C) The team is correct — `sensitive = true` on a variable also prevents Terraform from writing the value to state
- D) The team is partially correct — `sensitive = true` encrypts the value in state using the provider's encryption key, but the key is stored next to the state file

---

### Question 20 — Plan is Slower Than Expected

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Understanding that terraform plan refreshes live state via API and how -refresh=false can speed it up

**Question**:
An engineer manages 500 resources in a single Terraform workspace. `terraform plan` takes over 10 minutes because Terraform is making hundreds of API calls. The engineer asks: "Is there a way to speed up planning when I'm confident the state is accurate?" What is the correct approach?

- A) Split the resources across multiple state files — Terraform cannot plan efficiently with more than 100 resources in a single state
- B) Use `terraform plan -refresh=false` — this **skips the live API refresh phase** and plans based solely on the cached values in the state file; when the engineer has recently applied and is confident the state accurately reflects reality (no manual changes have occurred), this flag dramatically reduces planning time by eliminating all provider API calls during the plan
- C) Run `terraform plan -parallelism=1` to reduce API throttling — the default parallelism causes the slowdown
- D) Upgrade to Terraform Enterprise — community Terraform has a hard limit of 100 API calls per plan

---

### Question 21 — Two Provider Version Changes After Lock File Update

**Difficulty**: Medium
**Answer Type**: many
**Topic**: Identifying TWO correct statements about the effects of running terraform init -upgrade

**Question**:
A team's `.terraform.lock.hcl` currently pins the AWS provider to `5.20.0`. The `required_providers` constraint is `~> 5.0`. AWS provider `5.40.0` is now available. An engineer runs `terraform init -upgrade`. Which TWO statements correctly describe what happens? (Select two.)

- A) `terraform init -upgrade` **re-resolves all provider versions** against the current constraints and installs the newest version that satisfies each constraint — in this case, `5.40.0` replaces `5.20.0` because it satisfies `~> 5.0`
- B) The `.terraform.lock.hcl` file is **updated to record the new version `5.40.0`** and its cryptographic hashes — the lock file must be committed to version control so teammates get the upgraded version on their next `terraform init`
- C) `terraform init -upgrade` ignores version constraints and always installs the absolute latest provider version available, even if it violates the `required_providers` constraint
- D) Running `terraform init -upgrade` automatically runs `terraform apply` to ensure the upgraded provider is compatible with the current state

---

### Question 22 — `terraform show` Reports Different Values Than the Console

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Understanding why terraform show may reflect stale state if terraform refresh/plan has not been run

**Question**:
An engineer runs `terraform show` to check the public IP of an EC2 instance. The output shows `54.1.2.3`. They then check the AWS console and see the instance's public IP is `54.9.9.9` — the instance was stopped and restarted, which assigned a new IP. Why does `terraform show` display the old IP?

- A) `terraform show` always shows the IP from when the instance was first created and never updates
- B) `terraform show` displays the values **stored in the local state file** — state is only updated when Terraform runs a plan or apply that includes a refresh; the instance was restarted outside Terraform, so the state file still contains the old IP (`54.1.2.3`); running `terraform plan` or `terraform apply -refresh-only` will query the AWS API, detect the changed IP, and update the state file, after which `terraform show` will reflect `54.9.9.9`
- C) `terraform show` is a deprecated command that reads from a cached snapshot taken at install time
- D) The discrepancy means the instance is now unmanaged — Terraform lost track of it when it was restarted

---

### Question 23 — Provider Source Address Produces 404 on Init

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

---

### Question 24 — `terraform state push` Used Carelessly in Recovery

**Difficulty**: Hard
**Answer Type**: one
**Topic**: Understanding the dangers of terraform state push and the safer alternatives

**Question**:
During an incident, an engineer attempts to recover from a corrupted remote state by running `terraform state push ./old-backup.tfstate` without fully understanding its effect. A senior engineer stops them urgently. What is the specific danger of this command in this scenario?

- A) `terraform state push` is not a real Terraform command — it does not exist and would return an error
- B) `terraform state push` is dangerous because it **overwrites the current remote state file entirely with whatever local file is provided**, with no merge or diff — pushing an old backup would discard any state changes made since that backup was taken, potentially causing Terraform to lose track of resources created after the backup, which would lead to duplicate resource creation or unmanaged drift on the next apply; the safer alternatives are using the remote backend's native versioning (S3 versioned bucket, HCP Terraform state history) to roll back to a specific prior version under controlled conditions
- C) The danger is that `terraform state push` requires elevated cloud provider permissions that the engineer does not have — it will silently fail and report success
- D) `terraform state push` pushes state to all workspaces simultaneously, potentially corrupting unrelated environments

---

### Question 25 — Multiple Problems When Two Engineers Apply Simultaneously

**Difficulty**: Hard
**Answer Type**: many
**Topic**: Identifying TWO consequences of running terraform apply concurrently without state locking

**Question**:
Two engineers on a team using a local backend both run `terraform apply` at the same time against the same infrastructure. Neither apply errors immediately. Which TWO consequences are most likely? (Select two.)

- A) The **state file becomes corrupted or inconsistent** — both apply processes may read the same initial state, each compute their own diff, and both write their own version of the updated state file, with the second write potentially overwriting changes recorded by the first; the result is a state file that no longer accurately reflects all the resources that were created or modified
- B) **Duplicate resources may be created** — if both processes plan to create the same resource (because neither sees the other's in-progress work in state), both may attempt to provision it; some provider APIs will create a second resource rather than erroring, leaving orphaned infrastructure not tracked by state
- C) The local backend automatically detects concurrent access and queues the second apply to run after the first completes safely
- D) Both applies will succeed cleanly — the local backend uses OS-level file locking to serialise concurrent access reliably across all operating systems

---

### Question 26 — `terraform state pull` to Inspect Remote State

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Understanding the correct use case for terraform state pull when inspecting or backing up remote state

**Question**:
A team uses an S3 remote backend. An engineer wants to inspect the raw state file to debug an unexpected plan output but does not have direct S3 bucket access. What is the correct Terraform-native approach?

- A) Run `terraform show -json` — this streams the remote state file to stdout in JSON format with full attribute details
- B) Run **`terraform state pull`** — this **downloads the current remote state from the configured backend and writes it to stdout**; the engineer can pipe the output to a file (`terraform state pull > debug.tfstate`) or parse it with `jq` for inspection; it uses the Terraform credentials and backend configuration to authenticate, so no direct S3 access is required
- C) Run `terraform plan -json` — this includes the full state file in the plan output
- D) The engineer must request direct S3 access — there is no Terraform command that can retrieve remote state

---

### Question 27 — CI Pipeline Fails Because Files Are Not Formatted

**Difficulty**: Easy
**Answer Type**: one
**Topic**: Using terraform fmt -check in CI to enforce formatting without writing files

**Question**:
A team's CI pipeline runs `terraform fmt` as a formatting gate. A developer notices that every time the pipeline runs, it reformats the committed files and then reports a diff that must be manually committed. The team wants the pipeline to **report a failure** when files are unformatted rather than silently rewrite them. What is the correct flag to use?

- A) `terraform fmt -dry-run` — preview changes without writing to disk
- B) `terraform fmt -no-write` — display unformatted files without modifying them
- C) `terraform fmt -check` — this flag makes `terraform fmt` **exit with a non-zero exit code** if any `.tf` files need reformatting, without writing any changes to disk; the CI pipeline fails on the non-zero exit, prompting the developer to format their code locally and recommit; this is the standard CI usage of `fmt`
- D) `terraform fmt -validate` — combines formatting and validation in a single pass

---

### Question 28 — `terraform validate` Passes But `terraform plan` Fails

**Difficulty**: Easy
**Answer Type**: one
**Topic**: Understanding the boundary between what validate checks (static) and what plan checks (live)

**Question**:
An engineer runs `terraform validate` on a configuration that references an AMI ID: `ami = "ami-0deadbeef1234567"`. Validation passes. They then run `terraform plan` and receive an error: `InvalidAMIID.NotFound: The image id '[ami-0deadbeef1234567]' does not exist`. The engineer is confused — they thought `validate` would catch this. What explains the discrepancy?

- A) `terraform validate` only checks files in the root module; AMI references in child modules are skipped
- B) `terraform validate` is **fully offline and makes no API calls** — it checks HCL syntax and static references but cannot verify whether cloud resources such as AMI IDs actually exist; `terraform plan` calls the AWS provider API, which verifies the AMI ID against the AWS catalogue and returns the error when it is not found; `validate` passing is correct — it cannot know the AMI is invalid without querying AWS
- C) `terraform validate` found the error but suppressed it because `ami` is a computed attribute
- D) `terraform plan` is stricter than `validate` because it re-parses the `.tf` files from scratch

---

### Question 29 — Apply Prompt Appears Unexpectedly in Automation

**Difficulty**: Easy
**Answer Type**: one
**Topic**: Using -auto-approve to suppress the interactive apply confirmation in CI/CD

**Question**:
An engineer sets up a CI/CD pipeline that runs `terraform apply` as the final step. The pipeline hangs indefinitely after printing the execution plan, waiting for user input. The engineer needs the apply to proceed automatically without prompting. What is the correct fix?

- A) Set the environment variable `TF_APPLY_AUTO=true` before running `terraform apply`
- B) Run `terraform apply -no-prompt` to skip the confirmation dialog
- C) Add **`-auto-approve`** to the `terraform apply` command — this flag suppresses the interactive confirmation prompt and applies the plan immediately; it is the standard flag for non-interactive environments such as CI/CD pipelines; without it, `terraform apply` always pauses and waits for `yes` before proceeding
- D) Use `terraform apply -force` to bypass the confirmation check

---

### Question 30 — `-target` Used Regularly Causes State Drift

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Understanding why routine use of -target is an anti-pattern and what problems it causes

**Question**:
An engineer discovers they can run `terraform apply -target=aws_instance.web` to apply changes faster, skipping the other 40 resources in the configuration. They start using `-target` routinely for every change. A senior engineer warns them this is dangerous. What is the most likely problem this practice will cause over time?

- A) Using `-target` more than three times in a row permanently locks the state file
- B) `terraform apply -target` does not update the state file for the targeted resource — changes are applied to the cloud but not recorded
- C) **Routine use of `-target` causes state drift**: when only a subset of resources is planned and applied, Terraform does not evaluate the full dependency graph; changes to the targeted resource may leave dependent resources in an inconsistent or stale state that Terraform is unaware of; over time, the state file diverges from the full desired configuration, and a full `terraform apply` may plan unexpected changes or errors because the inter-resource relationships were never reconciled; `-target` is intended only for emergency recovery or one-off debugging, not routine use
- D) `-target` is deprecated in Terraform 1.x and will be removed in a future version

---

### Question 31 — Saved Plan File Applied After Configuration Change

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Understanding that a saved plan file is tied to the state and config at the time it was created

**Question**:
An engineer runs `terraform plan -out=plan.tfplan` and saves the plan. Before running `terraform apply plan.tfplan`, a colleague merges a pull request that adds a new resource to the configuration. The engineer applies the saved plan. What is the most likely problem?

- A) Terraform detects the configuration change and automatically re-plans before applying
- B) The apply fails immediately with a "plan file is out of date" error that prevents any changes from being made
- C) The **saved plan was generated against the configuration and state at the time `terraform plan` was run** — it does not include the new resource added by the colleague's PR; applying it will provision only the changes in the saved plan, not the new resource; the new resource will not be created until a fresh `terraform plan` and `terraform apply` are run; in some versions of Terraform, if the state has diverged significantly from the plan's recorded state, Terraform will also emit a warning or error
- D) The apply creates the new resource automatically because Terraform reads the current configuration files during `terraform apply plan.tfplan`

---

### Question 32 — `terraform graph` Output Is Unreadable

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

---

### Question 33 — `terraform output` Returns Nothing After Apply

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Understanding why terraform output returns nothing when no output blocks are declared

**Question**:
An engineer provisions infrastructure with `terraform apply`. After apply completes, they run `terraform output` expecting to see resource IDs and IP addresses, but the command prints nothing. The engineer is confused because the apply succeeded. What is the most likely cause?

- A) `terraform output` requires the `-state` flag to point to the state file — without it, the command cannot find the output values
- B) Output values are only available for 24 hours after apply; running the command the next day always returns nothing
- C) The engineer's configuration has **no `output` blocks declared** — `terraform output` can only display values that are explicitly defined in `output` blocks in the configuration; Terraform does not automatically expose resource attributes as outputs; to see the instance ID, the engineer must add an `output` block such as `output "instance_id" { value = aws_instance.web.id }` and re-apply
- D) The outputs were cleared because `terraform apply` was run with `-auto-approve`

---

### Question 34 — Plan Shows Resource Replaced When Only a Tag Changed

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Understanding that certain attributes force resource replacement and how to recognise this in plan output

**Question**:
An engineer changes only the `Name` tag on an RDS database instance and runs `terraform plan`. They expect to see `1 to change` (an in-place update) but instead see `-/+ 1 to add, 1 to destroy` with the note `# forces replacement`. The engineer is alarmed — they did not intend to recreate the database. What is the most likely explanation?

- A) Changing a tag on any AWS resource always forces a full replacement in Terraform — tag changes are never applied in place
- B) The engineer accidentally changed the `engine_version` attribute instead of the tag; engine version changes always force replacement
- C) **Some resource attributes are marked `ForceNew` in the provider schema** — changing them requires the resource to be destroyed and recreated because the underlying cloud API does not support in-place updates for that attribute; however, `Name` tags on RDS instances are not normally `ForceNew`; the most likely explanation is that the engineer also changed (intentionally or accidentally) a `ForceNew` attribute such as `identifier`, `engine`, `engine_version`, or `db_subnet_group_name` alongside the tag change; the plan output's `# forces replacement` note will list the specific attribute responsible
- D) `-/+` in the plan always means the engineer has changed more than five attributes at once, triggering a safety replacement

---

### Question 35 — `terraform console` Used to Debug an Unexpected Expression

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Using terraform console to test and debug HCL expressions interactively before embedding in config

**Question**:
An engineer writes a complex `for` expression in their configuration but is unsure whether it produces the expected output. They keep running `terraform plan` to test it, but the plan is slow because it refreshes 300 resources each time. What is the most efficient way to test the expression in isolation?

- A) Run `terraform validate --expression` to evaluate and print the result of a single HCL expression
- B) Create a separate test `.tf` file with just the expression and run `terraform apply` on it in an empty workspace
- C) Use **`terraform console`** — an interactive REPL (Read-Eval-Print Loop) that evaluates HCL expressions against the current state and variable values without running a full plan or making any provider API calls; the engineer can type the `for` expression directly at the prompt and see the result immediately, iterating quickly until the output is correct before embedding it in the configuration
- D) Use `terraform output --eval` to evaluate an expression without declaring an output block

---

### Question 36 — `terraform destroy` Run in Wrong Workspace

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

---

### Question 37 — `terraform apply -replace` vs Deleting from Config

**Difficulty**: Hard
**Answer Type**: one
**Topic**: Understanding terraform apply -replace as the correct way to force-recreate a resource without removing it from config

**Question**:
An EC2 instance has become corrupted. An engineer needs to destroy and recreate it using its current Terraform configuration, without changing any configuration attributes. A colleague suggests removing the resource block from the configuration, running `terraform apply`, and then adding it back and running `terraform apply` again. What is the problem with this approach, and what is the correct alternative?

- A) There is no problem — removing and re-adding a resource block is the standard Terraform procedure for recreating a resource
- B) The two-step remove-and-add approach has two significant problems: (1) removing the block plans a destroy, which deletes the instance — this is correct — but (2) re-adding the block then plans a **create of a brand-new instance** which has a **different resource ID, IP, and configuration** than the original; this process also requires two separate apply operations, increasing the window for errors; the correct approach is **`terraform apply -replace=aws_instance.web`**, which plans a single destroy-then-recreate (shown as `-/+` in the plan) in one apply operation, preserving all configuration attributes and minimising the outage window
- C) The approach is correct but only works if `lifecycle { create_before_destroy = true }` is set on the resource block
- D) The two-step approach is required because `terraform apply -replace` is only available in Terraform Enterprise

---

### Question 38 — `terraform output -raw` vs `terraform output` for Scripting

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

---

### Question 39 — `terraform plan -destroy` Unexpected Scope

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Understanding that terraform plan -destroy plans destruction of ALL resources, not just unused ones

**Question**:
An engineer runs `terraform plan -destroy` expecting it to plan the removal of only the resources that are no longer in the configuration (i.e., orphaned resources). Instead, the plan shows all 47 managed resources will be destroyed. The engineer panics and asks: "Is something wrong?" What is the correct explanation?

- A) `terraform plan -destroy` has detected that all 47 resources are misconfigured and must be replaced — the engineer should review each resource
- B) `terraform plan -destroy` plans the **destruction of ALL resources currently tracked in state**, regardless of whether they are in the configuration or not — it is equivalent to removing every resource block and running `terraform plan`; it is used when the intention is to completely tear down the environment; it does not selectively destroy only orphaned resources; to remove only resources that have been removed from configuration, the engineer should simply run a normal `terraform plan` and look for any `-` (destroy) entries
- C) Something is wrong with the state file — `terraform plan -destroy` should never show more than 10 resources
- D) The engineer accidentally appended `-destroy` to their `terraform plan -target` command, overriding the target scope

---

### Question 40 — Subnet Created Before VPC

**Difficulty**: Easy
**Answer Type**: one
**Topic**: Understanding that implicit dependency from attribute reference controls creation order

**Question**:
An engineer writes a Terraform configuration with an `aws_vpc` and an `aws_subnet`. They expect Terraform to create the subnet first because it is declared first in the file. Instead, Terraform creates the VPC first. The engineer asks why. What is the correct explanation?

- A) Terraform creates resources in alphabetical order by resource type — `aws_subnet` comes before `aws_vpc` alphabetically, but Terraform uses the reverse alphabetical order as a safety measure
- B) Terraform creates resources in the order they are declared in configuration files — the VPC being created first means it must have been declared first
- C) Terraform infers creation order from the **dependency graph, not file declaration order** — because the subnet's `vpc_id` argument references `aws_vpc.main.id`, Terraform detects an implicit dependency and ensures the VPC is created before the subnet; file order is irrelevant to execution order
- D) The VPC is created first only because it uses the default provider; resources using aliased providers are always created last

---

### Question 41 — Data Source Returns Stale AMI

**Difficulty**: Easy
**Answer Type**: one
**Topic**: Understanding when data sources are evaluated and how to force a refresh

**Question**:
An engineer uses a data source to look up the latest Ubuntu AMI and passes it to an EC2 instance. Six months later, a new Ubuntu AMI is released. The engineer runs `terraform apply` but the EC2 instance is not updated — it still uses the old AMI. The engineer assumes the data source is refreshing automatically. What explains this behaviour?

- A) Data sources are evaluated only during `terraform init` — after initialisation, the result is cached permanently
- B) The data source is re-evaluated on every `terraform plan` and `terraform apply`; if the AMI has changed, Terraform will detect the new value and plan a replacement for the EC2 instance automatically
- C) Data sources **are** re-evaluated on each plan, but changing the AMI ID returned by the data source does not automatically cause the EC2 instance to be replaced unless the resource has a `ForceNew` constraint on `ami` — and `aws_instance.ami` is indeed `ForceNew`; if the plan shows no changes, the most likely explanation is that the data source filter is still returning the same AMI (e.g., the `most_recent = true` filter resolved to the same ID), not that the data source is stale; the engineer should verify by running `terraform plan` and examining the data source result
- D) Data sources cache their results in `.terraform/` for 30 days to avoid repeated API calls during planning

---

### Question 42 — `prevent_destroy` Blocks Teardown Pipeline

**Difficulty**: Easy
**Answer Type**: one
**Topic**: Understanding that prevent_destroy causes terraform apply/destroy to error and how to override it

**Question**:
A team has `lifecycle { prevent_destroy = true }` on their production RDS instance. When a junior engineer runs `terraform destroy` on the environment teardown pipeline, it fails with: `Error: Instance cannot be destroyed`. The engineer asks: "How do we destroy this resource when we're ready to decommission the environment?" What is the correct answer?

- A) Run `terraform destroy -force` — this flag overrides `prevent_destroy` for a single destroy operation
- B) The only way to destroy a `prevent_destroy`-protected resource is to use the AWS console directly
- C) `prevent_destroy = true` is a **configuration-level guard** — to destroy the resource, the engineer must **remove or change the `prevent_destroy` setting** in the configuration file and then run `terraform apply` (or `terraform destroy`) again; there is no runtime flag to override it; this is by design — the guard forces a deliberate code change before destruction can proceed
- D) Set `TF_PREVENT_DESTROY=false` in the environment before running `terraform destroy`

---

### Question 43 — Two Resources Created in Wrong Order Despite `depends_on`

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Diagnosing why depends_on alone on a data source may not be enough to control ordering with IAM

**Question**:
An engineer creates an EC2 instance with an IAM instance profile. The instance starts but immediately fails because the attached IAM role does not yet have the S3 read policy attached — the policy attachment resource is not complete by the time the instance boots and attempts to use it. The engineer added `aws_instance.app` to depend on `aws_iam_role.app`, but forgot to include the policy resource in `depends_on`. What is the most precise diagnosis and fix?

- A) IAM propagation is always instant — the instance failure is caused by a misconfigured security group blocking S3 access, not a missing dependency
- B) The implicit dependency on `aws_iam_role.app` ensures the role exists before the instance, but does not guarantee the **policy attachment** (`aws_iam_role_policy` or `aws_iam_role_policy_attachment`) is complete; the engineer must add the policy attachment resource to the `depends_on` list on `aws_instance.app` so Terraform waits for the policy to be attached before creating the instance
- C) Adding any `depends_on` entry to a resource causes Terraform to serialize all subsequent resource creations — the issue must be something else
- D) `depends_on` cannot reference `aws_iam_role_policy` resources — it only accepts module references

---

### Question 44 — `count` Removal Causes Unexpected Destroy+Create

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Understanding that removing a count item by index causes all subsequent instances to shift and be replaced

**Question**:
An engineer uses `count = 3` to create three S3 buckets, named `bucket-0`, `bucket-1`, and `bucket-2`. They later need to remove `bucket-1`. They remove element 1 from the list and set `count = 2`. On running `terraform plan`, they see that `bucket-1` will be destroyed and `bucket-2` will also be destroyed and recreated as a different bucket. Why does `bucket-2` get recreated?

- A) `count` always destroys and recreates all instances when the count value is reduced
- B) Removing element 1 from the list **shifts the index of the remaining elements** — what was index 2 (`bucket-2`) becomes index 1 (`bucket-1`) in the new count; Terraform sees `aws_s3_bucket.this[1]` as a different instance in state vs the new configuration, triggering a destroy+create; this index-shifting problem is why `for_each` with stable string keys is preferred over `count` when the set of instances may change
- C) S3 bucket names are globally unique — Terraform must destroy all buckets with sequential names when any one is removed
- D) This only happens when `count` is reduced from 3 to 2 — reducing to 1 or 0 would not trigger the shift

---

### Question 45 — `ignore_changes` Not Preventing Drift Detection

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

---

### Question 46 — `for_each` Fails on a `list(string)`

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

---

### Question 47 — Resource Recreated Every Apply Due to `replace_triggered_by`

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Diagnosing unintended constant replacement caused by replace_triggered_by referencing a frequently changing resource

**Question**:
An engineer adds `replace_triggered_by = [aws_launch_template.web]` to an Auto Scaling Group resource to ensure the ASG is recycled when the launch template changes. After deploying, the ASG is replaced on every `terraform apply` — even when nothing has changed. What is the most likely cause?

- A) `replace_triggered_by` always forces a replacement on every apply — this is the expected behaviour
- B) The `aws_launch_template.web` resource itself has **`create_before_destroy = true`**, causing it to be replaced on every apply, which then triggers the ASG replacement through `replace_triggered_by`; the fix is to remove `create_before_destroy` from the launch template
- C) The `aws_launch_template.web` resource **has an attribute that changes on every apply** — for example, if the launch template has `latest_version` or similar computed attribute that increments on each apply even with no configuration changes, `replace_triggered_by` detects this as a change and triggers ASG replacement; the engineer should scope `replace_triggered_by` to a specific stable attribute rather than the entire resource, or investigate why the launch template resource reports changes on every apply
- D) `replace_triggered_by` is incompatible with Auto Scaling Groups — it should only be used with stateless resources like EC2 instances

---

### Question 48 — `removed` Block Destroys Resource Unexpectedly

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Understanding that removed block destroy=false is needed to stop managing without destroying

**Question**:
An engineer wants to stop managing an EC2 instance with Terraform without deleting it from AWS. They have heard about the `removed` block (Terraform 1.7+) and add it to their configuration. On the next `terraform apply`, the instance is deleted. What did the engineer most likely forget?

- A) The `removed` block always stops Terraform from managing a resource without any cloud-side effect — the instance deletion must have been triggered by something else
- B) The engineer forgot to run `terraform state rm` before using the `removed` block — the two must be used together
- C) The `removed` block has a **`lifecycle { destroy = false }` sub-block** that must be explicitly set — without it, the default behaviour of `removed` is to **destroy** the resource and remove it from state; setting `destroy = false` tells Terraform to stop tracking the resource but leave it running in the cloud; the engineer forgot this sub-block and got the default destroy behaviour
- D) `removed` blocks are only supported in HCP Terraform — in the open-source CLI, they always destroy the resource

---

### Question 49 — Two Scenarios Where `depends_on` Is Required

**Difficulty**: Medium
**Answer Type**: many
**Topic**: Identifying TWO scenarios where implicit dependency detection is insufficient and depends_on is needed

**Question**:
Which TWO of the following scenarios require `depends_on` because Terraform cannot detect the dependency through attribute references alone? (Select two.)

- A) An EC2 instance references `aws_subnet.public.id` in its `subnet_id` argument — Terraform must be told explicitly via `depends_on` that the instance depends on the subnet
- B) An EC2 instance uses an IAM instance profile, and the instance's startup script reads from an S3 bucket that the attached IAM role must have permission to access — the policy attachment has no attribute referenced by the instance, so Terraform has no way to detect the dependency automatically
- C) A `null_resource` with a `local-exec` provisioner runs a script that calls an API exposed by an `aws_api_gateway_rest_api` resource — no attribute of the API gateway is referenced in the `null_resource` block, so `depends_on` is needed to ensure the API is deployed before the script runs
- D) An `aws_db_instance` is referenced by its endpoint in an `aws_instance` user_data script using string interpolation — Terraform must be told via `depends_on` that the instance depends on the database

---

### Question 50 — Circular Dependency Error

**Difficulty**: Hard
**Answer Type**: one
**Topic**: Diagnosing a cycle in the dependency graph and knowing how to resolve it

**Question**:
An engineer receives the error: `Error: Cycle: aws_security_group.app, aws_instance.web`. Their configuration has `aws_instance.web` referencing `aws_security_group.app.id` in its `vpc_security_group_ids`, and `aws_security_group.app` referencing `aws_instance.web.private_ip` in an ingress rule. What explains the error and how should it be resolved?

- A) The error means both resources have `prevent_destroy = true` — removing those lifecycle blocks will resolve the cycle
- B) A **dependency cycle** exists: `aws_instance.web` depends on `aws_security_group.app` (for the security group ID), and simultaneously `aws_security_group.app` depends on `aws_instance.web` (for the private IP in the ingress rule); Terraform's DAG cannot resolve circular dependencies and errors immediately; the resolution is to break the cycle — for example, remove the private IP reference from the security group ingress rule and use a CIDR block instead, or restructure the ingress rule to reference a different stable value
- C) Cycles are resolved automatically on `terraform apply` — the error only appears during `terraform plan` and can be ignored
- D) The cycle is caused by both resources being in the same `.tf` file — moving one to a separate file resolves the dependency conflict

---

### Question 51 — `moved` Block Applied But Resource Still Recreated

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

---

### Question 52 — `data` Source Reads Stale Value During Apply

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Understanding the known-after-apply problem for data sources that depend on resources being created in the same apply

**Question**:
An engineer creates an `aws_security_group` resource and a `data "aws_security_group"` data source that filters by the security group's name in the same Terraform configuration. They expect the data source to return the newly created security group. During `terraform plan`, the data source shows `(known after apply)` instead of the security group's attributes. The engineer asks why. What is the correct explanation?

- A) Data sources can never reference resources created in the same Terraform configuration — they are always evaluated before any resources are created
- B) The data source must use the resource's `id` attribute, not the `name` filter — `name`-based filters only work against pre-existing resources
- C) The data source **depends on the security group being created**, but during `terraform plan` the security group does not exist yet (it will be created on apply); Terraform detects this dependency and defers the data source read until `terraform apply`, when the security group will exist — this is the "known after apply" behaviour; the attributes are shown as `(known after apply)` in the plan; after apply completes, the data source will have been read and its attributes will be available; the preferred alternative is to reference the resource's attributes directly (`aws_security_group.app.id`) rather than re-querying via a data source for a resource Terraform itself is creating
- D) The `(known after apply)` message means the data source is misconfigured — it cannot be used in the same configuration as a resource of the same type

---

### Question 53 — Required Variable Not Prompted in CI Pipeline

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

---

### Question 54 — `lookup()` Fails With Error Instead of Returning a Default

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

---

### Question 55 — Wrong Variable Value Used When Both `.tfvars` Files Set It

**Difficulty**: Easy
**Answer Type**: one
**Topic**: Understanding that auto.tfvars takes precedence over terraform.tfvars

**Question**:
An engineer has both `terraform.tfvars` (sets `region = "us-east-1"`) and a file named `overrides.auto.tfvars` (sets `region = "eu-west-1"`) in the same directory. They expect `terraform.tfvars` to win because it is the "main" file. Terraform uses `"eu-west-1"`. Why?

- A) Terraform reads `.tfvars` files in alphabetical order and the last value wins — `overrides` comes after `terraform` alphabetically
- B) `terraform.tfvars` is only loaded when no `.auto.tfvars` files are present — the two file types are mutually exclusive
- C) **`*.auto.tfvars` files have higher precedence than `terraform.tfvars`** in Terraform's variable resolution order — any file matching the pattern `*.auto.tfvars` is automatically loaded and takes priority over the manually-loaded `terraform.tfvars`; the engineer's mental model of `terraform.tfvars` as the "most authoritative" file is incorrect; to override an `auto.tfvars` file, the engineer must use a CLI `-var` flag or a `TF_VAR_*` environment variable, both of which rank higher than any `.tfvars` file
- D) Terraform merges values from both files and uses the region declared in `overrides.auto.tfvars` because it was the most recently modified file

---

### Question 56 — `timestamp()` Causes Perpetual Diff on Every Plan

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

---

### Question 57 — Validation Condition References a `local` — Error

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

---

### Question 58 — `templatefile()` Fails With "File Not Found"

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

---

### Question 59 — `merge()` Silently Overwrites Expected Key

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

---

### Question 60 — `cidrsubnet()` Returns Unexpected CIDR Block

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Understanding how cidrsubnet() calculates subnets — newbits and netnum parameters

**Question**:
An engineer calls `cidrsubnet("10.0.0.0/16", 8, 3)` expecting to get the third `/24` subnet. They expect `10.0.3.0/24`. Running `terraform console` confirms this returns `"10.0.3.0/24"`. However, a colleague calls `cidrsubnet("10.0.0.0/16", 4, 3)` and gets `10.0.48.0/20` instead of what the engineer expected. The engineer asks why the colleague's call produces a different result. What explains the difference?

- A) `cidrsubnet()` only works correctly when the base prefix is `/16` or larger — `/4` arguments are invalid
- B) The second argument (`newbits = 4`) adds 4 bits to the base prefix, creating `/20` subnets (not `/24` subnets); `netnum = 3` then selects the **third** `/20` subnet within `10.0.0.0/16` — which starts at `10.0.48.0`; the result is correct: `cidrsubnet("10.0.0.0/16", 4, 3)` computes `/16 + 4 bits = /20`, and the third `/20` block in that space is `10.0.48.0/20`; the engineer's assumption that both calls would produce `/24` subnets is wrong — `newbits` controls the number of **additional bits** borrowed, not the final prefix length
- C) The difference is caused by the two engineers running different versions of Terraform — `cidrsubnet()` changed its calculation method in Terraform 1.5
- D) `cidrsubnet()` requires the third argument (`netnum`) to start at 1, not 0 — the colleague used `3` to get the third subnet, but should have used `2`

---

### Question 61 — `compact()` Does Not Remove Duplicate Values

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

---

### Question 62 — Output Exposes a Sensitive Local Without `sensitive = true`

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

---

### Question 63 — Variable Declared as `type = any` Causes Downstream Type Error

**Difficulty**: Hard
**Answer Type**: many
**Topic**: TWO problems caused by using type = any instead of a specific type constraint

**Question**:
An engineer declares a module variable as `type = any` to avoid dealing with type constraints. A caller passes a `number` where the module internally expects a `string`. Which TWO of the following are consequences of using `type = any` in this scenario? (Select two.)

- A) Terraform rejects `type = any` at `terraform validate` — it is not a valid type constraint
- B) **Type errors are deferred to the point of use** — with `type = any`, Terraform accepts any value the caller provides (number, string, list, etc.) without validation at variable assignment time; the type mismatch is only discovered when the value reaches an argument that requires a specific type (e.g., a resource attribute that requires `string`), producing a potentially confusing error deep in the configuration rather than at the variable boundary
- C) **The calling module gets no documentation signal about what type is expected** — `type = any` removes the self-documenting contract that a specific type constraint provides; callers must inspect the module internals to determine what type is actually needed, increasing integration errors and maintenance burden
- D) `type = any` causes Terraform to silently coerce all input values to strings before they reach the module internals — numeric inputs become their string representation automatically

---

### Question 64 — `for` Expression Filter Produces Empty List Unexpectedly

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

---

### Question 65 — TWO Things `sensitive = true` on an Output Does and Does Not Protect

**Difficulty**: Hard
**Answer Type**: many
**Topic**: Understanding the precise scope of what output-level sensitive = true protects

**Question**:
Which TWO of the following statements accurately describe the behaviour of `sensitive = true` on an output block? (Select two.)

- A) **`sensitive = true` on an output suppresses the value in `terraform apply` summary output and in the `terraform output` (all-outputs) command, displaying `(sensitive value)` instead** — this prevents the value from appearing accidentally in terminal logs or CI pipeline output
- B) `sensitive = true` on an output encrypts the value before writing it to `terraform.tfstate`, protecting it from anyone with read access to the state file
- C) `sensitive = true` on an output prevents the value from being accessed by a parent module that calls the current module as a child — the output is invisible to callers
- D) **`sensitive = true` on an output does NOT prevent the value from being exposed when queried directly by name (`terraform output <name>`) or via `terraform output -json` — both commands reveal the plaintext value**, meaning the protection is limited to incidental terminal display, not direct programmatic access

---

### Question 66 — `check` Block Does Not Fail a Production Deployment Gate

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

---

### Question 67 — Sensitive Variable Value Found in Plaintext in State File

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

---

### Question 68 — `self` Used in a `precondition` Causes an Error

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

---

### Question 69 — `postcondition` Fails After Resource Is Already Created

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

---

### Question 70 — All `validation` Blocks on a Variable Are Evaluated

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

---

### Question 71 — `nonsensitive()` Strips the Sensitive Taint From a Value

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

---

### Question 72 — `precondition` Can Reference Other Resources (Unlike `validation`)

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

---

### Question 73 — `check` Block Requires Terraform 1.5+

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Understanding that the check block was introduced in Terraform 1.5 and requires setting required_version

**Question**:
A senior engineer adds `check` blocks to a shared module to monitor infrastructure health. When a junior engineer on the team runs `terraform init` on their machine, they get: `Error: Unsupported block type — Blocks of type "check" are not expected here`. The senior engineer's machine works fine. What is the most likely cause?

- A) The `check` block must be declared inside a `resource` block — using it at the top level of a module is unsupported
- B) `check` blocks are only supported in Terraform Cloud/HCP Terraform and cannot be used in local Terraform runs
- C) **The `check` block was introduced in Terraform 1.5** — the junior engineer is running an older version of Terraform that does not recognise the `check` block type; the fix is for the module to declare a minimum version requirement: `required_version = ">= 1.5"` in the `terraform {}` block, which will produce a clear "version too old" error rather than a confusing "unsupported block" message, and prompts the junior engineer to upgrade their Terraform CLI
- D) The `check` block is only unsupported on Windows — this is a platform compatibility issue

---

### Question 74 — `postcondition` Condition Expression Throws an Error Instead of Returning `false`

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

---

### Question 75 — Sensitive Output Value Revealed by `terraform output -json` in CI

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

---

### Question 76 — TWO Differences Between `check` Block and `precondition`

**Difficulty**: Hard
**Answer Type**: many
**Topic**: Two distinct behavioral differences between check blocks and preconditions beyond just blocking vs non-blocking

**Question**:
An engineer is deciding whether to use a `check` block or a `precondition` for an infrastructure assertion. They know one blocks the apply and the other doesn't. Which TWO additional differences between `check` blocks and `preconditions` should they also consider? (Select two.)

- A) **`check` blocks run on every `terraform plan` AND every `terraform apply`**, making them suitable for continuous health monitoring; a `precondition` only runs during `terraform apply` — when its resource is actually being created or modified; if no change is planned for the resource, the precondition is not evaluated during that run
- B) `check` blocks can only reference outputs from completed resources; `precondition` blocks can reference any Terraform expression
- C) **`check` blocks can optionally contain a scoped `data` source block** that is evaluated exclusively within the `check` block scope and is not available elsewhere in the configuration; `precondition` blocks do not support embedded data sources — they reference data sources declared at module scope
- D) `precondition` failures can be suppressed with a `-force` flag; `check` block failures cannot be suppressed

---

### Question 77 — TWO Measures Required to Properly Protect Sensitive Values in Terraform

**Difficulty**: Hard
**Answer Type**: many
**Topic**: Understanding the gap between what sensitive = true provides and what is required to actually protect secrets

**Question**:
A security team is reviewing a Terraform project that manages RDS database credentials. The engineer has applied `sensitive = true` to all relevant variables and outputs and believes this fully protects the secrets. Which TWO additional measures must be in place to achieve adequate protection of the credential values? (Select two.)

- A) Rename all sensitive variables to start with `_secret_` — Terraform treats these as encrypted at rest in state
- B) **Use an encrypted remote backend** — because `sensitive = true` does not protect the state file, and `terraform.tfstate` stores all values (including those marked sensitive) in **plaintext JSON**, the state file must be stored in a backend that encrypts data at rest and in transit; suitable options include S3 with SSE-KMS and strict bucket policies, HCP Terraform (which encrypts state by default), or other encrypted backends; without this, anyone with access to the state file can read all credentials regardless of `sensitive` flags
- C) Add `terraform plan -no-state` to all CI pipeline commands to prevent state from being written
- D) **Restrict access to the state file through IAM policies, bucket policies, or backend access controls** — even with encryption, if developers and CI pipelines have broad read access to the state backend, credentials can be extracted; the principle of least privilege should be applied so that only Terraform execution roles and specific operators can read state; this is independent of (and complementary to) backend encryption

---

### Question 78 — `check` Block Scoped Data Source Is Not Available Elsewhere in the Module

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

---

### Question 79 — `terraform plan` Errors After Adding a New Module Block

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

---

### Question 80 — Child Module Variable Not Receiving Value From Root

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

---

### Question 81 — Module Output Referenced Before It Is Declared in the Child Module

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

---

### Question 82 — `version` Constraint Used with a Git URL Causes `terraform init` Error

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

---

### Question 83 — Module Changes Not Reflected — `terraform init` Not Re-run After Source Change

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

---

### Question 84 — Root Module Cannot Access Resources Inside a Child Module Directly

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

---

### Question 85 — Module Destroyed Unexpectedly After Being Renamed

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

---

### Question 86 — `module.vpc` Outputs All Showing as `(known after apply)` at Plan Time

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

---

### Question 87 — TWO Issues That Require Re-running `terraform init` for Modules

**Difficulty**: Medium
**Answer Type**: many
**Topic**: Identifying which module-related changes require terraform init before plan/apply

**Question**:
Which TWO of the following changes to a module configuration require the engineer to run `terraform init` before `terraform plan` will succeed? (Select two.)

- A) Adding a new `locals` block inside an existing child module directory
- B) **Adding a new `module` block with a new `source` argument** — Terraform must install and register the module source in `.terraform/modules/` before it can be used; running `plan` without `init` produces "Module not installed"
- C) Changing a `count` argument on an existing module block from `1` to `2`
- D) **Changing a `module` block's `source` argument to a different URL or path** — when the source changes, Terraform needs to download or re-register the new source; the old cached source in `.terraform/modules/` is no longer correct; `terraform init` resolves and caches the updated source

---

### Question 88 — Module Published to Terraform Registry — `version` Must Be Set

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

---

### Question 89 — TWO Consequences of Not Declaring an Output in a Child Module

**Difficulty**: Hard
**Answer Type**: many
**Topic**: Child module encapsulation — two effects when a needed value is not declared as an output

**Question**:
An engineer's root module needs to pass a security group ID (created inside a child module) to another resource in the root module. The child module does not declare an `output` for the security group ID. Which TWO of the following are correct descriptions of what happens? (Select two.)

- A) **Terraform raises an error when the root module references `module.<name>.<attr>` for an attribute not declared as an output** — the attribute simply does not exist on the module object; the root module cannot access any value from a child module unless that value is explicitly exported via an `output` block in the child module
- B) The security group ID can still be accessed from the root module using the `data "terraform_remote_state"` data source, which bypasses module encapsulation
- C) **The only fix is to add an `output` block to the child module that exposes the security group ID** — there is no workaround; module encapsulation is enforced at the language level; the output can be declared as `output "security_group_id" { value = aws_security_group.app.id }` in the child module's `outputs.tf`, after which `module.<name>.security_group_id` becomes a valid reference in the root module
- D) The root module can reference the security group ID using `module.<name>.resource.aws_security_group.app.id` — the `resource.` prefix provides direct resource access across module boundaries

---

### Question 90 — Module Refactored Internally — Root Module Plan Shows Replacements

**Difficulty**: Hard
**Answer Type**: one
**Topic**: Internal module resource address changes (due to refactoring) cause unexpected replace plans

**Question**:
An engineer refactors a child module, renaming an internal resource from `aws_subnet.public` to `aws_subnet.public_primary`. No inputs or outputs change. After running `terraform init`, the next `terraform plan` shows the subnet being destroyed and recreated. The engineer expected no infrastructure change since only the name changed. What is the cause and fix?

- A) Terraform always recreates subnets when modules are re-initialised — this is an AWS provider constraint
- B) The `terraform init` command deleted the old subnet state entry as part of module cache refresh
- C) **The resource's state address changed** — inside the module, the resource was previously tracked as `module.<name>.aws_subnet.public`; after renaming, Terraform looks for `module.<name>.aws_subnet.public_primary`, finds no state entry, and plans to create it; simultaneously, it sees `module.<name>.aws_subnet.public` in state with no matching configuration and plans to destroy it; to resolve this without recreating infrastructure, the engineer should add a `moved` block **inside the child module's** `main.tf` or `moved.tf`: `moved { from = aws_subnet.public; to = aws_subnet.public_primary }` — this instructs Terraform to update the state address without modifying the resource
- D) The replacement is caused by the subnet's `cidr_block` being a `ForceNew` attribute — any change to the subnet triggers a replace; the resource name change is unrelated

---

### Question 91 — Private Registry Module Requires Token But Authentication Is Not Configured

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

---

### Question 92 — DynamoDB Table Attribute Name Wrong — State Locking Fails

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

---

### Question 93 — `-reconfigure` Used Instead of `-migrate-state` — Old State Abandoned

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

---

### Question 94 — `terraform force-unlock` Runs While a Concurrent Apply Is Active

**Difficulty**: Easy
**Answer Type**: one
**Topic**: force-unlock is dangerous and should only be used when certain no other operation is running

**Question**:
An engineer runs `terraform apply` on a shared S3/DynamoDB-backed workspace. The apply is taking a long time and they suspect it has hung. A colleague runs `terraform force-unlock <LOCK_ID>` from their workstation to clear the lock so they can investigate. Two minutes later, the original engineer's apply completes successfully and writes its final state to S3. The colleague then immediately runs `terraform apply` — the plan shows a large number of unexpected changes. What is the risk that was realised?

- A) `terraform force-unlock` also rolls back any changes already made to cloud resources — the original apply's cloud changes were reverted
- B) There is no risk — `force-unlock` only releases the DynamoDB entry and has no effect on the state file itself
- C) **`terraform force-unlock` releases the DynamoDB lock record without any awareness of whether the locked operation is actually complete** — by unlocking while the original apply was still writing state, the colleague created a window where both operations could write state concurrently; the original apply wrote its final state, but a subsequent operation could read a stale state before that write landed, leading to conflicting state records; the safe use of `force-unlock` requires first **confirming with certainty** that no Terraform operation is running (e.g., the process has crashed, the CI job has been killed) — it must never be used as a shortcut to interrupt or "unstick" an operation that is still in progress
- D) The unexpected plan changes are caused by `force-unlock` incrementing the state serial number — the colleague's plan is reading a state with a higher serial than expected

---

### Question 95 — `TF_LOG_CORE=DEBUG` Set But Provider API Calls Missing From Logs

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

---

### Question 96 — `terraform state mv` Done Without Updating HCL — Plan Shows Destroy and Create

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

---

### Question 97 — Sentinel `hard-mandatory` Policy Cannot Be Overridden

**Difficulty**: Medium
**Answer Type**: one
**Topic**: hard-mandatory enforcement level blocks a run unconditionally — even org owners cannot override it

**Question**:
An HCP Terraform organisation enforces a Sentinel policy that requires all EC2 instances to use approved AMI IDs. The policy is configured with `enforcement_level = "hard-mandatory"`. A team lead deploys a new configuration using a custom AMI not in the approved list. The policy check fails. The team lead is an organisation **Owner** (the highest HCP Terraform role) and clicks the "Override" button in the HCP Terraform UI — but the button is disabled. They escalate to HashiCorp support, believing this is a bug. Is it?

- A) Yes — organisation Owners should always be able to override any policy; a disabled override button is a bug
- B) No — the override button is disabled because the workspace must be in "admin" mode for owners to override Sentinel policies
- C) **No — `hard-mandatory` is the only Sentinel enforcement level that cannot be overridden by any user, regardless of role** — the three enforcement levels are: `advisory` (failure is a warning, run proceeds automatically); `soft-mandatory` (failure blocks the run, but an authorised user such as an Owner can click Override to allow the run to proceed); `hard-mandatory` (failure unconditionally blocks the run — the Override button is permanently disabled and no role has the ability to proceed); to resolve the team lead's situation, either the configuration must be updated to use an approved AMI, or a HashiCorp Sentinel policy administrator must change the enforcement level or update the approved AMI list in the policy
- D) No — only users with the Sentinel policy management permission can override `hard-mandatory` policies, and the team lead's Owner role does not include this permission by default

---

### Question 98 — HCP Terraform Workspace Variable Silently Overrides `terraform.tfvars`

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Workspace variables in HCP Terraform take precedence over all file-based and CLI variable sources

**Question**:
A team uses HCP Terraform with a VCS-connected workspace. The repository contains a `terraform.tfvars` file setting `instance_type = "t3.large"`. Despite this, every apply deploys `t3.micro` instances. The engineer has confirmed the `terraform.tfvars` file is correct and in the right directory. Runs complete without errors. What is the most likely cause?

- A) HCP Terraform ignores `terraform.tfvars` in all cases — file-based variable files are not supported in remote runs
- B) The `terraform.tfvars` file must be named `override.tfvars` for HCP Terraform to load it during remote runs
- C) **A workspace variable named `instance_type` is set to `"t3.micro"` in the HCP Terraform workspace settings** — workspace variables have the **highest precedence** among all variable sources in HCP Terraform runs; they override `terraform.tfvars`, `.auto.tfvars`, `-var` flags, and `TF_VAR_` environment variables; the engineer should check the workspace's "Variables" tab in the HCP Terraform UI and remove or update the `instance_type` workspace variable; workspace variables are intentionally the highest-priority source so that operators can enforce environment-specific values without modifying VCS-tracked files
- D) HCP Terraform caches variable values from the first run — the workspace is using a stale variable value; run `terraform init -reconfigure` to clear the variable cache

---

### Question 99 — `terraform_remote_state` Errors Because Output Not Declared in Source Workspace

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

---

### Question 100 — `terraform login` Token Not Available in CI — Env Var Alternative Needed

**Difficulty**: Medium
**Answer Type**: one
**Topic**: terraform login stores tokens in a local file not available in CI — TF_TOKEN_* env var is the correct CI approach

**Question**:
A developer successfully authenticates to HCP Terraform using `terraform login` on their laptop. They then add the same configuration to a CI/CD pipeline (GitHub Actions) and expect the pipeline to be authenticated automatically. The CI job fails: `Error: Required token could not be found: No credentials for app.terraform.io`. The developer is confused because their local machine works perfectly. What is the cause and fix?

- A) `terraform login` authentication tokens expire after 24 hours — the developer must re-run `terraform login` in the CI job before each run
- B) GitHub Actions blocks outbound connections to `app.terraform.io` for security — the organisation's GitHub Actions settings must whitelist the HCP Terraform domain
- C) **`terraform login` stores the authentication token in a local file on the developer's machine** (`~/.terraform.d/credentials.tfrc.json`) — this file exists only on that machine and is never available in CI runners, which start from a clean environment on every job; to authenticate Terraform in a CI/CD pipeline, the correct approach is to store the HCP Terraform API token as a CI secret and expose it via the `TF_TOKEN_app_terraform_io` environment variable (e.g., `TF_TOKEN_app_terraform_io: ${{ secrets.TF_API_TOKEN }}` in GitHub Actions); Terraform reads this environment variable automatically instead of the credentials file
- D) The CI pipeline must run `terraform init` with the `-token` flag pointing to a credentials file bundled in the repository

---

### Question 101 — Run Triggers Not Configured — Workspace B Not Auto-Triggered

**Difficulty**: Medium
**Answer Type**: one
**Topic**: HCP Terraform run triggers must be explicitly configured — workspace B does not automatically follow workspace A

**Question**:
A team has two HCP Terraform workspaces: `networking` (manages VPCs and subnets) and `compute` (manages EC2 instances that depend on `networking` outputs). The team assumes that when `networking` completes an apply, `compute` will automatically queue a new run to pick up any networking changes. After updating security group rules in `networking`, the `compute` workspace does not receive a new run. The EC2 instances are still using stale subnet configurations. What is the cause?

- A) HCP Terraform only auto-triggers dependent workspaces when the source workspace is connected to a VCS repository — API-driven workspaces do not support automatic triggering
- B) Auto-triggering between workspaces requires both workspaces to be in the same HCP Terraform Project
- C) **HCP Terraform does not automatically detect dependencies between workspaces or trigger runs based on them** — run triggers between workspaces must be **explicitly configured** in the `compute` workspace settings under "Run Triggers"; once configured, when `networking` completes a successful apply, HCP Terraform queues a new plan-and-apply run in `compute`; without this explicit configuration, the two workspaces are entirely independent — no matter how many times `networking` applies, `compute` never receives an automatic trigger; the engineer must navigate to the `compute` workspace settings, add `networking` as a source workspace under Run Triggers, and re-apply
- D) Run triggers require the `terraform_remote_state` data source to be configured in the dependent workspace before HCP Terraform can detect the dependency and trigger automatically

---

### Question 102 — HCP Terraform Health Assessment Does Not Auto-Remediate Drift

**Difficulty**: Hard
**Answer Type**: one
**Topic**: Health assessments detect and report drift on a schedule but never automatically apply changes to fix it

**Question**:
An operations team enables Health Assessments on their HCP Terraform workspace, setting it to run every 24 hours. After a cloud engineer manually modifies a security group in the AWS Console (creating drift), the health assessment runs and reports the drift. The operations team then waits, expecting HCP Terraform to automatically queue an apply to restore the configuration to the desired state. After several hours, no apply has run. Is this expected behaviour?

- A) No — Health Assessments are supposed to queue a remediation apply automatically; the delay indicates a workspace configuration issue such as auto-apply being disabled
- B) No — Health Assessments automatically apply corrections for drift on resources tagged with `health_assessment = "auto_remediate"` in their Terraform configuration
- C) **Yes — Health Assessments in HCP Terraform are a drift detection and reporting tool only; they never automatically queue or execute remediation applies** — when a health assessment detects drift (via an internal `terraform plan -refresh-only` equivalent), it surfaces the results in the HCP Terraform UI, sends notifications through configured channels (email, Slack), and updates the workspace's health status indicator; it is the responsibility of an operator to review the drift report and manually queue a new plan-and-apply run (or configure auto-apply) to remediate the drift; automatic remediation is not a health assessment feature because blindly re-applying in response to drift could mask legitimate manual changes or cause unintended infrastructure modifications
- D) No — Health Assessments in HCP Terraform trigger a speculative plan run that is automatically applied if the drift is smaller than a configurable threshold

---

### Question 103 — TWO Safeguards Required Before Running `terraform state push`

**Difficulty**: Hard
**Answer Type**: many
**Topic**: terraform state push is destructive — two safeguards must be in place to prevent overwriting newer or correct state

**Question**:
Which TWO safeguards must be in place before running `terraform state push` against a remote backend to prevent irreversible state damage? (Select two.)

- A) **Verify that the serial number in the local state file being pushed is equal to or greater than the serial in the remote state** — `terraform state push` overwrites the remote state unconditionally; if the local file being pushed has a lower serial number than the current remote state, the push overwrites newer remote state with older data, potentially losing records of resources created, modified, or destroyed since the local file was saved; backends with versioning (such as S3 with versioning enabled) allow recovery, but the damage may not be noticed immediately
- B) Run `terraform validate` on the local state file before pushing to check for schema errors
- C) **Confirm that no Terraform operation is currently running against the remote backend** — if a plan or apply is in progress, pushing a state file mid-operation creates a race condition where two processes have divergent views of infrastructure truth; the running operation may complete and overwrite the pushed state, or the pushed state may cause the in-progress operation to act on stale resource information; always verify the workspace/backend is idle before using `state push`
- D) Run `terraform plan -refresh-only` after pushing to confirm the state matches cloud reality before running any apply

---

### Question 104 — TWO HCP Terraform Mechanisms That Eliminate Storing Static Credentials

**Difficulty**: Hard
**Answer Type**: many
**Topic**: Dynamic provider credentials (OIDC) and team tokens eliminate two different kinds of static credential storage

**Question**:
A security team reviews an HCP Terraform organisation and identifies two categories of static credentials that create security risks: (1) long-lived cloud provider credentials (AWS access keys) stored as sensitive workspace environment variables; (2) individual user API tokens used in CI/CD pipelines. Which TWO HCP Terraform mechanisms eliminate each of these risks respectively? (Select two.)

- A) **Dynamic Provider Credentials using OIDC (OpenID Connect)** — eliminates the need for static cloud provider credentials (AWS access keys, Azure service principal secrets, GCP service account keys) stored in workspace variables; instead, HCP Terraform workspaces present a signed OIDC token to the cloud provider's IAM system; the cloud provider validates the token against a configured OIDC trust relationship and returns short-lived credentials scoped to that specific run; credentials automatically expire and are never stored in HCP Terraform; this removes static `AWS_ACCESS_KEY_ID` / `AWS_SECRET_ACCESS_KEY` environment variables from workspace settings entirely
- B) Sentinel policies with `hard-mandatory` enforcement can prevent static credentials from being added to workspace variables — this is equivalent to eliminating them
- C) **Team Tokens** — eliminate the need for individual user API tokens in CI/CD pipelines; instead of each CI pipeline authenticating to HCP Terraform with a specific user's personal token (which is tied to an individual's account, expires with their employment, and may have excessive personal permissions), a Team Token represents the team's combined access to all assigned workspaces; the team token can be rotated independently of any individual, scoped to only the workspaces the team can access, and stored as a CI system secret without tying pipeline access to any employee's personal credentials
- D) Variable Sets can store cloud credentials centrally — this reduces credential duplication but does not eliminate the static credentials themselves



## Answer Key

| Q# | Answer(s) | Explanation | Source | Difficulty |
|---|---|---|---|---|
| 2 | C | N/A | Understanding why an imperative provisioning script is not idempotent and how Terraform's declarative model avoids the same problem | Easy |
| 3 | B | N/A | Understanding that Terraform enforces desired state and will revert manual changes on the next apply | Easy |
| 4 | C | N/A | Recognising that "No changes" is the correct idempotent outcome — not an error or a skipped step | Easy |
| 5 | C | N/A | Understanding why directly editing terraform.tfstate is dangerous and what the file's actual role is | Medium |
| 6 | B | N/A | Understanding that Terraform owns resources it manages and plans to destroy them when removed from configuration | Medium |
| 7 | C | N/A | Identifying which IaC benefit directly addresses environment drift between staging and production | Medium |
| 8 | B | N/A | Understanding why terraform plan shows a resource as "to add" even though it is declared in configuration | Medium |
| 9 | B | N/A | Recognising Terraform's multi-cloud advantage over provider-specific IaC tools | Medium |
| 10 | A, B, D | N/A | Identifying valid IaC benefits over manual console-based provisioning | Medium |
| 11 | B | N/A | Understanding what terraform plan's "to add", "to change", and "to destroy" counts mean for in-place vs replace operations | Medium |
| 12 | B | N/A | Understanding that terraform apply always performs a fresh plan to account for changes that may have occurred since the last plan | Medium |
| 13 | A, B | N/A | Understanding that renaming a resource label causes plan to show destroy + create, and knowing TWO ways to handle this correctly | Hard |
| 14 | B | N/A | Understanding the documentation benefit of IaC and the limits of that claim in a scenario where config and reality have diverged | Hard |
| 15 | C | N/A | Understanding that terraform init is required after cloning before any other terraform commands | Easy |
| 16 | B | N/A | Understanding the role of .terraform.lock.hcl in preventing unintended provider upgrades | Easy |
| 17 | C | N/A | Understanding that provider alias must be explicitly referenced in a resource block or Terraform uses the default provider | Easy |
| 18 | B | N/A | Understanding the consequences of losing the state file and the recovery path | Medium |
| 19 | B | N/A | Understanding that .backup holds only the immediately previous state, not a full version history | Medium |
| 20 | B | N/A | Understanding that sensitive=true masks terminal output but does not protect state | Medium |
| 21 | B | N/A | Understanding that terraform plan refreshes live state via API and how -refresh=false can speed it up | Medium |
| 22 | A, B | N/A | Identifying TWO correct statements about the effects of running terraform init -upgrade | Medium |
| 23 | B | N/A | Understanding why terraform show may reflect stale state if terraform refresh/plan has not been run | Medium |
| 24 | C | N/A | Diagnosing a provider init failure caused by a malformed source address | Medium |
| 25 | B | N/A | Understanding the dangers of terraform state push and the safer alternatives | Hard |
| 26 | A, B | N/A | Identifying TWO consequences of running terraform apply concurrently without state locking | Hard |
| 27 | B | N/A | Understanding the correct use case for terraform state pull when inspecting or backing up remote state | Medium |
| 28 | C | N/A | Using terraform fmt -check in CI to enforce formatting without writing files | Easy |
| 29 | B | N/A | Understanding the boundary between what validate checks (static) and what plan checks (live) | Easy |
| 30 | C | N/A | Using -auto-approve to suppress the interactive apply confirmation in CI/CD | Easy |
| 31 | C | N/A | Understanding why routine use of -target is an anti-pattern and what problems it causes | Medium |
| 32 | C | N/A | Understanding that a saved plan file is tied to the state and config at the time it was created | Medium |
| 33 | B | N/A | Understanding that terraform graph outputs DOT format and requires an external tool to render | Medium |
| 34 | C | N/A | Understanding why terraform output returns nothing when no output blocks are declared | Medium |
| 35 | C | N/A | Understanding that certain attributes force resource replacement and how to recognise this in plan output | Medium |
| 36 | C | N/A | Using terraform console to test and debug HCL expressions interactively before embedding in config | Medium |
| 37 | A, C | N/A | Understanding terraform workspaces and the risk of running destructive commands in the wrong workspace | Medium |
| 38 | B | N/A | Understanding terraform apply -replace as the correct way to force-recreate a resource without removing it from config | Hard |
| 39 | B | N/A | Understanding why -raw is needed when using terraform output in shell scripts | Hard |
| 40 | B | N/A | Understanding that terraform plan -destroy plans destruction of ALL resources, not just unused ones | Medium |
| 41 | C | N/A | Understanding that implicit dependency from attribute reference controls creation order | Easy |
| 42 | C | N/A | Understanding when data sources are evaluated and how to force a refresh | Easy |
| 43 | C | N/A | Understanding that prevent_destroy causes terraform apply/destroy to error and how to override it | Easy |
| 44 | B | N/A | Diagnosing why depends_on alone on a data source may not be enough to control ordering with IAM | Medium |
| 45 | B | N/A | Understanding that removing a count item by index causes all subsequent instances to shift and be replaced | Medium |
| 46 | C | N/A | Understanding the correct syntax for ignore_changes and common mistakes | Medium |
| 47 | C | N/A | Understanding that for_each does not accept a plain list and requires a set or map | Medium |
| 48 | C | N/A | Diagnosing unintended constant replacement caused by replace_triggered_by referencing a frequently changing resource | Medium |
| 49 | C | N/A | Understanding that removed block destroy=false is needed to stop managing without destroying | Medium |
| 50 | B, C | N/A | Identifying TWO scenarios where implicit dependency detection is insufficient and depends_on is needed | Medium |
| 51 | B | N/A | Diagnosing a cycle in the dependency graph and knowing how to resolve it | Hard |
| 52 | C | N/A | Diagnosing why a moved block did not prevent destroy+create — common mistakes in moved block syntax | Hard |
| 53 | C | N/A | Understanding the known-after-apply problem for data sources that depend on resources being created in the same apply | Medium |
| 54 | C | N/A | Understanding that a required variable (no default) causes a non-interactive failure in CI, not a prompt | Easy |
| 55 | C | N/A | Understanding the correct 3-argument form of lookup() to avoid errors on missing keys | Easy |
| 56 | C | N/A | Understanding that auto.tfvars takes precedence over terraform.tfvars | Easy |
| 57 | B | N/A | Understanding why timestamp() in a resource attribute causes Terraform to always show a change | Medium |
| 58 | C | N/A | Understanding that variable validation conditions can only reference var.<name>, not locals or other resources | Medium |
| 59 | C | N/A | Using path.module correctly to reference template files relative to the current module | Medium |
| 60 | C | N/A | Understanding that merge() uses last-key-wins when maps share duplicate keys | Medium |
| 61 | B | N/A | Understanding how cidrsubnet() calculates subnets — newbits and netnum parameters | Medium |
| 62 | C | N/A | Understanding the difference between compact() (removes nulls/empties) and distinct() (removes duplicates) | Medium |
| 63 | C | N/A | Understanding that Terraform warns when an output references a sensitive value without marking the output sensitive | Medium |
| 64 | B, C | N/A | TWO problems caused by using type = any instead of a specific type constraint | Hard |
| 65 | C | N/A | Diagnosing a for expression with an if clause that filters out all elements due to a logic error | Hard |
| 66 | A, D | N/A | Understanding the precise scope of what output-level sensitive = true protects | Hard |
| 67 | C | N/A | Understanding that check block failures are non-blocking warnings — wrong tool for a deployment gate | Easy |
| 68 | C | N/A | Understanding that sensitive = true masks terminal output but does not protect state | Easy |
| 69 | C | N/A | Understanding that self is only valid in postcondition, not precondition | Easy |
| 70 | C | N/A | Understanding that a failing postcondition leaves the resource created but marks the apply as failed | Medium |
| 71 | C | N/A | Understanding that multiple validation blocks on a variable are all evaluated and all failures are reported | Medium |
| 72 | C | N/A | Understanding that nonsensitive() removes the sensitive marking and allows the value to appear in plain text output | Medium |
| 73 | C | N/A | Understanding the broader reference scope allowed in precondition/postcondition vs the var-only restriction in validation | Medium |
| 74 | C | N/A | Understanding that the check block was introduced in Terraform 1.5 and requires setting required_version | Medium |
| 75 | C | N/A | Using can() to make postcondition conditions error-tolerant when the expression might throw rather than return false | Medium |
| 76 | C | N/A | Understanding that terraform output -json reveals sensitive output values in plaintext | Medium |
| 77 | A, C | N/A | Two distinct behavioral differences between check blocks and preconditions beyond just blocking vs non-blocking | Hard |
| 78 | B, D | N/A | Understanding the gap between what sensitive = true provides and what is required to actually protect secrets | Hard |
| 79 | C | N/A | Understanding that a data source declared inside a check block is scoped to that check block only | Hard |
| 80 | C | N/A | New module source requires terraform init before plan/apply will work | Easy |
| 81 | C | N/A | Parent variables are not automatically inherited — must be explicitly passed as module arguments | Easy |
| 82 | C | N/A | A module output that was never declared causes a reference error | Easy |
| 83 | C | N/A | The version argument is only valid for registry sources — Git sources use ?ref= instead | Medium |
| 84 | C | N/A | Changing a module source or version requires terraform init to update the cache | Medium |
| 85 | C | N/A | Module encapsulation — resources inside child modules are not directly accessible from outside | Medium |
| 86 | C | N/A | Renaming a module block label changes all resource addresses and causes destroy+create | Medium |
| 87 | C | N/A | Module outputs that depend on computed values will be unknown at plan time | Medium |
| 88 | B, D | N/A | Identifying which module-related changes require terraform init before plan/apply | Medium |
| 89 | C | N/A | Using a registry module without a version constraint is risky and may break on future runs | Medium |
| 90 | A, C | N/A | Child module encapsulation — two effects when a needed value is not declared as an output | Hard |
| 91 | C | N/A | Internal module resource address changes (due to refactoring) cause unexpected replace plans | Hard |
| 92 | C | N/A | Private registry modules require credentials configured in CLI config or environment | Hard |
| 93 | C | N/A | The DynamoDB lock table hash key must be exactly "LockID" — any other name causes locking failures | Easy |
| 94 | C | N/A | Understanding the difference between terraform init -reconfigure and -migrate-state when changing backends | Easy |
| 95 | C | N/A | force-unlock is dangerous and should only be used when certain no other operation is running | Easy |
| 96 | C | N/A | TF_LOG_CORE captures only Terraform core logs — provider-level debugging requires TF_LOG_PROVIDER | Medium |
| 97 | C | N/A | terraform state mv moves the state address but if config is not updated to match, plan shows destroy+create at new/old addresses | Medium |
| 98 | C | N/A | hard-mandatory enforcement level blocks a run unconditionally — even org owners cannot override it | Medium |
| 99 | C | N/A | Workspace variables in HCP Terraform take precedence over all file-based and CLI variable sources | Medium |
| 100 | C | N/A | terraform_remote_state can only access values explicitly declared as outputs in the source workspace configuration | Medium |
| 101 | C | N/A | terraform login stores tokens in a local file not available in CI — TF_TOKEN_* env var is the correct CI approach | Medium |
| 102 | C | N/A | HCP Terraform run triggers must be explicitly configured — workspace B does not automatically follow workspace A | Medium |
| 103 | C | N/A | Health assessments detect and report drift on a schedule but never automatically apply changes to fix it | Hard |
| 104 | A, C | N/A | terraform state push is destructive — two safeguards must be in place to prevent overwriting newer or correct state | Hard |
| 105 | A, C | N/A | Dynamic provider credentials (OIDC) and team tokens eliminate two different kinds of static credential storage | Hard |
