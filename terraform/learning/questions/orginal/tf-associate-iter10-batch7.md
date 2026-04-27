# Terraform Associate (004) — Question Bank Iter 10 Batch 7

**Iteration**: 10
**Iteration Style**: Exam-style scenarios — multi-sentence real-world context questions
**Batch**: 7
**Objective**: Modules + State Backends
**Sources**: prompt11-terraform-modules.md, prompt12-state-backends-locking-remote-state.md
**Generated**: 2026-04-26
**Total Questions**: 13
**Difficulty Split**: 3 Easy / 7 Medium / 3 Hard
**Answer Types**: 10 `one` / 3 `many` / 0 `none`

---

## Questions

---

### Question 1 — Registry Module Without a `version` Constraint Breaks in CI

**Difficulty**: Medium
**Answer Type**: one
**Topic**: A Terraform Registry module source without a `version` constraint causes `terraform init` to always download the latest available version — a future major release with breaking changes will silently break the configuration

**Scenario**:
A platform team adds a VPC module from the Terraform Registry to their production configuration without specifying a version constraint:

```hcl
module "vpc" {
  source = "terraform-aws-modules/vpc/aws"

  cidr = "10.0.0.0/16"
  azs  = ["us-east-1a", "us-east-1b"]
}
```

The configuration works correctly for six months. The module publisher then releases `v6.0.0`, which renames the `private_subnets` argument to `private_subnet_cidrs` and removes the old argument entirely. The next CI run calls `terraform init`, downloads `v6.0.0`, and the plan immediately fails with "An argument named 'private_subnets' is not expected here."

**Question**:
What is the root cause of this failure, and what change prevents it from recurring?

- A) The module source path is missing the provider suffix — the correct format is `terraform-aws-modules/vpc/aws/v6` and the version must be embedded in the source string
- B) Without a `version` constraint, `terraform init` always resolves and downloads the latest published version of the module. When a new major version with breaking changes was published, the CI run silently adopted it. Adding `version = "~> 5.0"` to the module block pins the resolution to compatible 5.x releases and prevents automatic adoption of v6.x
- C) The issue is caused by using `~>` pessimistic pinning in the backend, which propagates to module version resolution — using exact version pinning with `version = "= 5.9.0"` is the only safe approach
- D) CI pipelines should add `-no-upgrade` flag to `terraform init` to prevent version resolution — without this flag, `terraform init` always upgrades all modules to their latest versions regardless of whether a version constraint is present

**Answer**: B

**Explanation**:
When no `version` constraint is present on a registry module source, `terraform init` resolves to the latest available version on every fresh initialisation. This is fine until a breaking major version is published. Adding `version = "~> 5.0"` (or `version = "~> 5.9"` for tighter pinning) uses the pessimistic constraint operator to allow patch and minor updates within the 5.x series while blocking automatic adoption of v6.x. This is the standard practice for production configurations: always pin registry modules to a version range. Local path and Git-sourced modules use different mechanisms (`?ref=` for Git) — the `version` argument is only valid for registry sources.

---

### Question 2 — Child Module Needs a Non-Default Provider Alias (Multi-Region)

**Difficulty**: Hard
**Answer Type**: many
**Topic**: The `providers` meta-argument on a module block maps provider aliases from the root module to the provider names expected by the child module — without it, child modules always use the default (non-aliased) provider configuration

**Scenario**:
A team's root module configures two AWS providers: the default configuration for `us-east-1` and an aliased configuration for `eu-west-1`:

```hcl
provider "aws" {
  region = "us-east-1"
}

provider "aws" {
  alias  = "eu"
  region = "eu-west-1"
}
```

A networking child module provisions subnets. The team wants this module's resources to be created in `eu-west-1`. They add:

```hcl
module "networking_eu" {
  source = "./modules/networking"

  providers = {
    aws = aws.eu
  }
}
```

A colleague questions whether the `providers` map is actually necessary, arguing "provider configurations flow to child modules automatically."

**Question**:
Which TWO statements accurately describe the `providers` meta-argument and the behaviour without it?

- A) Without the `providers` map, the child module automatically uses the provider configuration that matches its resources' region — Terraform inspects each resource and routes it to the correct provider based on the `region` attribute
- B) Without the `providers` map, the child module uses the **default** (non-aliased) `aws` provider configuration — all module resources would be created in `us-east-1` regardless of what the team intended, because child modules inherit only the default provider unless explicitly overridden
- C) The `providers` map `{ aws = aws.eu }` tells Terraform: "when this child module refers to provider `aws`, use the aliased provider `aws.eu` from the root module." This is the only mechanism for directing a child module to use a non-default provider alias
- D) The `providers` meta-argument is only required when the child module declares its own `provider` block — if the child module has no `provider` block, provider configuration always flows automatically from the root

**Answer**: B, C

**Explanation**:
**(B)** is correct — provider configurations are not automatically distributed based on resource region. By default, a child module receives only the **default** (non-aliased) instance of each provider from its parent. Without the `providers` map, `module.networking_eu` would use the default `aws` provider (us-east-1) and create all resources there, contradicting the team's intent. **(C)** is correct — the `providers` map is the explicit mechanism for passing a non-default provider alias to a child module. The key in the map (`aws`) is the name the child module expects; the value (`aws.eu`) is the aliased provider in the parent. There is no automatic region-based routing — the mapping must be explicit.

---

### Question 3 — Renaming a Module Block Label Triggers Full Destroy and Recreate

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Terraform tracks all resources inside a child module under the module's label in state — renaming `module "network"` to `module "networking"` changes every resource's state address, causing Terraform to plan destroying all old-address resources and creating all new-address resources

**Scenario**:
A team decides to rename their networking module block from `module "network"` to `module "networking"` for clarity. The child module code is unchanged — only the label in the root module block is updated. No other changes are made. Running `terraform plan` outputs:

```
Plan: 47 to add, 0 to change, 47 to destroy.
```

The team is alarmed — they expected zero changes since no infrastructure code changed.

**Question**:
Why does renaming the module block label cause a full destroy-and-recreate plan?

- A) Renaming a module label triggers a forced replacement of all child module resources because Terraform treats the label as a hash seed for resource IDs — changing the label changes the generated IDs
- B) Terraform stores all resources inside a module using their full address, which includes the module label. `module.network.aws_subnet.public[0]` and `module.networking.aws_subnet.public[0]` are two completely different state addresses. Terraform sees no state entry for `module.networking.*` (create 47) and sees orphaned entries for `module.network.*` (destroy 47) — it has no way to know these refer to the same infrastructure
- C) The rename triggers an automatic `terraform init` to re-download the module source, and during re-initialisation the module version is bumped, which causes breaking changes in the resource schema
- D) Module block labels must match the `module_name` metadata field declared inside the child module's `versions.tf` — a mismatch between the call label and the declared name causes a full replacement cycle

**Answer**: B

**Explanation**:
Terraform's state file records every resource with its complete address, and for resources inside a module, that address is `module.<label>.<resource_type>.<name>`. Renaming the label portion of this address (`network` → `networking`) changes every single address inside the module. Terraform's plan algorithm compares configuration addresses against state addresses: it finds 47 unknown addresses in configuration (`module.networking.*`) that must be created, and 47 orphaned addresses in state (`module.network.*`) that must be destroyed. The fix is to either use a `moved` block to declare the rename — `moved { from = module.network; to = module.networking }` — or to run `terraform state mv module.network module.networking` before the plan.

---

### Question 4 — Plain `terraform init` Doesn't Update a Cached Module to a Newer Patch Version

**Difficulty**: Medium
**Answer Type**: one
**Topic**: `terraform init` without flags reuses a cached module version if it satisfies the constraint — to download a newer compatible version within the allowed range, `terraform init -upgrade` is required

**Scenario**:
A team's Terraform configuration pins a registry module with `version = "~> 5.0"`. Six months ago they ran `terraform init`, which downloaded and cached version `5.0.0` in `.terraform/modules/`. The module publisher has since released `5.7.3` with several important bug fixes the team wants to adopt. A developer runs `terraform init` again, expecting the module to update to `5.7.3`. The plan output still references `5.0.0`.

**Question**:
Why did the re-run of `terraform init` not update the module to `5.7.3`?

- A) Version `5.7.3` exceeds the `~> 5.0` constraint — the pessimistic operator `~>` only allows patch increments (5.0.0, 5.0.1, 5.0.2…), not minor version bumps (5.1.0, 5.7.3)
- B) `terraform init` without any flags does not check for newer versions if a module version already exists in the local cache that satisfies the declared constraint. Since `5.0.0` satisfies `~> 5.0`, no network request is made. To resolve the latest compatible version within the constraint, the developer must run `terraform init -upgrade`
- C) Module version upgrades require editing the `.terraform/modules/modules.json` file manually to update the version field before running `terraform init` — `terraform init` alone never changes a cached module version
- D) The `version` argument in a module block is evaluated only on the first `terraform init` — subsequent runs always use the same version that was downloaded initially, regardless of flags

**Answer**: B

**Explanation**:
`terraform init` uses a conservative strategy: if the local `.terraform/modules/` cache already contains a version that satisfies the declared constraint, it considers initialisation complete without checking for newer compatible versions. This prevents accidental upgrades during routine operations. To proactively adopt the latest version within the allowed constraint range, `terraform init -upgrade` is required — it forces Terraform to re-query the registry and download the newest version that satisfies the constraint. Note that `~> 5.0` permits any version `>= 5.0.0, < 6.0.0`, so `5.7.3` is valid and would be adopted after running `-upgrade`.

---

### Question 5 — Root Module References a Child Module Output That Was Never Declared

**Difficulty**: Easy
**Answer Type**: one
**Topic**: Child module outputs must be explicitly declared with an `output` block — referencing `module.<name>.<value>` from the root module when no matching `output` block exists in the child causes an error at plan time

**Scenario**:
A team's root module creates an EC2 instance inside a child module and needs the instance's private IP address to create a Route 53 DNS record. The developer writes:

```hcl
resource "aws_route53_record" "app" {
  zone_id = var.zone_id
  name    = "app.internal.example.com"
  type    = "A"
  ttl     = 60
  records = [module.compute.private_ip]
}
```

The child module (`modules/compute/main.tf`) creates `aws_instance.server` but the module's `outputs.tf` file is empty. Running `terraform plan` fails immediately.

**Question**:
What error does Terraform produce, and what is the minimal fix?

- A) Terraform produces a type error — `records` expects a `list(string)` but `module.compute.private_ip` resolves to a single string. The fix is to wrap it in brackets: `records = [module.compute.private_ip]`
- B) Terraform produces a reference error stating that the module has no output named `private_ip`. The minimal fix is to add an output block to the child module's `outputs.tf`: `output "private_ip" { value = aws_instance.server.private_ip }`
- C) Terraform produces an error because `private_ip` is a computed attribute — it cannot be referenced in another resource until after the EC2 instance has been created. The fix is to run `terraform apply` first to create the instance, then re-run `terraform plan`
- D) Terraform produces a module encapsulation error — resource attributes from inside a child module can only be used by other resources inside the same module, never by the root module

**Answer**: B

**Explanation**:
Child modules are encapsulated — the root module cannot directly reference any resource attribute inside a child module. The only way to expose a value from a child module to its caller is to declare an explicit `output` block inside the child module. Without an `output "private_ip"` block in the compute module, the reference `module.compute.private_ip` in the root module has no target and Terraform raises a reference error at plan time. The fix is strictly additive: add `output "private_ip" { value = aws_instance.server.private_ip }` to the child module's `outputs.tf`. No changes to the root module are needed.

---

### Question 6 — `for_each` Module: Adding a New Environment Key Affects Only That Instance

**Difficulty**: Hard
**Answer Type**: many
**Topic**: A `for_each` module block keyed by a map creates one module instance per map entry addressed by string key in state — adding a new key creates only that new instance; existing instances are unaffected

**Scenario**:
A team uses `for_each` on a module block to provision per-environment networking infrastructure:

```hcl
module "env" {
  for_each = {
    dev     = "10.0.0.0/16"
    staging = "10.1.0.0/16"
    prod    = "10.2.0.0/16"
  }
  source   = "./modules/networking"
  vpc_cidr = each.value
}
```

After a successful `terraform apply`, the state contains `module.env["dev"]`, `module.env["staging"]`, and `module.env["prod"]` with all their child resources. The team adds a fourth entry `dr = "10.3.0.0/16"` to the map and runs `terraform plan`.

**Question**:
Which TWO statements accurately describe what the plan shows?

- A) Terraform plans to create a new module instance `module.env["dr"]` and all child resources inside it — the three existing module instances (`module.env["dev"]`, `module.env["staging"]`, `module.env["prod"]`) are shown as unchanged and are not touched
- B) Because `for_each` re-evaluates the entire map on every plan, Terraform destroys all four instances and recreates them — adding any key to the map always triggers a full replacement cycle
- C) Each module instance created by `for_each` is addressed in state using the map key as a string — the new `"dr"` entry creates a new `module.env["dr"]` address in state independent of the three existing entries
- D) Terraform errors when a new entry is added to a `for_each` module map after the initial apply — the map must be finalized before the first apply and cannot be extended without using `terraform state import`

**Answer**: A, C

**Explanation**:
**(A)** is correct — `for_each` on a module block creates one module instance per map entry, each tracked independently by its string key. Adding `"dr"` to the map only introduces a new state address (`module.env["dr"]`). Terraform plans the creation of that one new instance and all its child resources; the three existing instances retain their state entries and are shown as unchanged. **(C)** is correct — the state addressing for `for_each` module instances uses the map key as a string, exactly analogous to `for_each` on a resource. This stable string addressing is the reason `for_each` is preferred over `count` for module instances: adding or removing individual entries is surgical and does not affect other instances. **(B)** is incorrect — Terraform does not destroy and recreate all instances on map changes. **(D)** is incorrect — `for_each` maps can be freely extended after the initial apply.

---

### Question 7 — Detecting Configuration Drift Without Proposing Infrastructure Changes

**Difficulty**: Easy
**Answer Type**: one
**Topic**: `terraform plan -refresh-only` shows drift between recorded state and live cloud state without producing a plan to modify infrastructure; `terraform apply -refresh-only` accepts the drift by updating state — only `-refresh-only` plan is read-only

**Scenario**:
An operations engineer discovers that a colleague manually changed a production EC2 instance type from `t3.small` to `t3.large` using the AWS console, bypassing Terraform. The Terraform configuration still declares `instance_type = "t3.small"`. The engineer wants to inspect exactly what has drifted before deciding whether to revert the manual change (restore t3.small) or accept it (update the configuration to `t3.large`). The engineer does not want Terraform to make any changes to infrastructure or write anything to the state file during this inspection step.

**Question**:
Which command satisfies these requirements — showing the drift without modifying infrastructure or state?

- A) `terraform plan` — a standard plan always shows configuration drift as a proposed change in the plan output and does not write anything to state
- B) `terraform plan -refresh-only` — this command refreshes Terraform's view of the live infrastructure and displays what has changed relative to the recorded state, but it does not generate a plan to modify any infrastructure resources and does not write changes to the state file
- C) `terraform apply -refresh-only` — the `-refresh-only` flag prevents infrastructure changes; it only updates the state file to reflect the live cloud, which is a safe read-only operation
- D) `terraform show -json` — this command reads the current state file and displays the recorded values; comparing its output to the live AWS console shows what has drifted

**Answer**: B

**Explanation**:
`terraform plan -refresh-only` is the purpose-built command for drift inspection. It refreshes Terraform's knowledge of the live infrastructure (by calling provider read APIs) and computes the difference between the live state and what is recorded in `terraform.tfstate`, displaying that delta. Crucially, it does not generate any proposal to create, update, or destroy resources — and it does not write anything to the state file. The engineer can review the output and decide. `terraform apply -refresh-only` (option C) is the second phase of drift acceptance: it actually updates the state file to match the live cloud, which is a write operation the engineer specifically wants to avoid in this inspection step. Option A is incorrect — a standard `terraform plan` would propose reverting the instance type to `t3.small` as an infrastructure change.

---

### Question 8 — Backend Migration: What Happens to the Old Local State File

**Difficulty**: Easy
**Answer Type**: one
**Topic**: `terraform init -migrate-state` copies state to the new backend but leaves the old `terraform.tfstate` file in the working directory — Terraform stops reading from the local file but does not delete it

**Scenario**:
A team has been using the local backend for three months. Their `terraform.tfstate` file in the working directory contains the full production state with 120 managed resources. They decide to migrate to an S3 remote backend for team collaboration. They add the backend block to their configuration and run `terraform init -migrate-state`. Terraform confirms the migration succeeds and all resources are now tracked in S3. A developer then asks: "Should we delete the local `terraform.tfstate` file now that we've migrated?"

**Question**:
What is the correct answer to the developer's question?

- A) Yes — Terraform automatically marks the local `terraform.tfstate` as invalid after migration by writing a special header to it. Deleting the now-invalid file is required to prevent Terraform from accidentally reverting to the local backend
- B) After successful migration, the local `terraform.tfstate` is left in place unchanged — Terraform will no longer read from it (all subsequent operations use the S3 backend), but the file is not deleted. The team should keep it temporarily as a backup, verify that S3 state is correct, and then delete it or move it to secure storage — but they should not commit it to version control
- C) No action is needed — Terraform automatically detects the local file on every init and will re-migrate it to S3, so keeping it present is safe and ensures continuity if the S3 backend becomes temporarily unavailable
- D) The `terraform init -migrate-state` command deletes the local `terraform.tfstate` file after confirming the migration — the developer is asking about a file that no longer exists

**Answer**: B

**Explanation**:
`terraform init -migrate-state` copies the state data from the local backend to the new remote backend and then updates the backend configuration. It deliberately leaves the original `terraform.tfstate` file in place — it does not delete it. After migration, all subsequent Terraform operations use the remote backend (S3), and the local file is inert. The team should retain it temporarily as a safety net in case the migration needs to be validated or rolled back. Once they confirm the S3 state is correct and complete, they should delete the local file or archive it securely — but it should never be committed to version control, as it contains plaintext sensitive values.

---

### Question 9 — `terraform state rm` Used to Abandon Management of a Resource

**Difficulty**: Medium
**Answer Type**: one
**Topic**: `terraform state rm` removes a resource's state entry — the actual cloud resource is unaffected, but if the resource block remains in configuration, the next `terraform plan` treats it as a new resource to create

**Scenario**:
A team has an EC2 instance `aws_instance.legacy` that was provisioned by an old process. They want Terraform to stop managing it permanently — specifically, they do not want Terraform to ever destroy it. They run `terraform state rm aws_instance.legacy`. The command succeeds. However, the `aws_instance.legacy` resource block is still present in `main.tf`. A teammate runs `terraform plan` an hour later and sees the EC2 instance scheduled for creation.

**Question**:
Why does `terraform plan` show the instance as a resource to create, and what additional step was missing?

- A) `terraform state rm` issued a `DeleteInstance` API call to AWS and removed the instance — the next plan correctly shows it as a new resource because the instance no longer exists in the cloud
- B) `terraform state rm` removed the resource's entry from the state file, but the `aws_instance.legacy` block is still present in the configuration. With no state entry and a configuration block present, Terraform treats the resource as non-existent and plans to create it. The missing step is removing (or commenting out) the `aws_instance.legacy` resource block from `main.tf` — once the block is removed, Terraform has no configuration entry and no state entry and ignores the resource entirely
- C) `terraform state rm` only flags a resource for removal — the next `terraform plan` is required to confirm and finalize the removal from state; until the plan is run, the resource is still tracked by Terraform
- D) The plan shows a create because `terraform state rm` refreshes state from the cloud before removing the entry, and the refresh detected the instance had been terminated — the instance exists in configuration but not in AWS, so Terraform correctly plans to recreate it

**Answer**: B

**Explanation**:
`terraform state rm` removes the resource entry from the state file only — it makes no API calls to AWS and the actual EC2 instance continues running unchanged. After the command, Terraform has no knowledge that this instance exists. When the next `terraform plan` runs and encounters the `aws_instance.legacy` block in configuration with no corresponding state entry, it behaves exactly as if the resource has never been created and plans to create it. The correct procedure to stop managing a resource without destroying it is two steps: (1) `terraform state rm <address>` to remove it from state, and (2) remove the resource block from the configuration file to prevent Terraform from planning its creation on the next run.

---

### Question 10 — Stale State Lock from a Crashed CI Pipeline

**Difficulty**: Medium
**Answer Type**: one
**Topic**: `terraform force-unlock <LOCK_ID>` manually releases a stale DynamoDB lock — it should only be used when certain no other Terraform operation is running, because it removes the lock regardless of whether a real concurrent process holds it

**Scenario**:
A CI pipeline applies Terraform changes to production infrastructure using an S3 backend with DynamoDB state locking. The CI runner hosting the apply job crashes mid-apply due to an out-of-memory error. The Terraform process is killed abruptly without releasing the DynamoDB lock entry. Every subsequent `terraform apply` and `terraform plan` by any engineer fails with:

```
Error: Error acquiring the state lock

  Lock Info:
    ID:   a3f7c8b2-91d4-4e2e-bb10-fd3a9c0e1234
    Operation: OperationTypeApply
    ...
```

The on-call engineer needs to unblock the team immediately.

**Question**:
What is the correct recovery command, and what critical check must the engineer perform before running it?

- A) `terraform init -reconfigure` clears all backend state including stale locks — the engineer should run this command to reset the locking state before retrying the apply
- B) The engineer must modify the DynamoDB table directly in the AWS console and delete the item with `LockID = "a3f7c8b2-91d4-4e2e-bb10-fd3a9c0e1234"` — `terraform force-unlock` is only available in HCP Terraform, not open-source Terraform
- C) The correct command is `terraform force-unlock a3f7c8b2-91d4-4e2e-bb10-fd3a9c0e1234`. Before running it, the engineer must verify that the original CI process is truly dead — not still running in a degraded state somewhere. `force-unlock` removes the lock entry unconditionally; if another Terraform process is actually still modifying state, removing the lock allows two writers simultaneously, which can corrupt the state file
- D) The engineer should wait at least 15 minutes because DynamoDB lock entries automatically expire after a configurable TTL — Terraform sets this TTL to 15 minutes by default, so the lock will self-release without any manual intervention

**Answer**: C

**Explanation**:
`terraform force-unlock <LOCK_ID>` is the purpose-built command for releasing a stale lock. The Lock ID is displayed in the error message and is passed directly as the argument. The critical safety check before using it: confirm that the process that acquired the lock is definitively dead (not still running in a degraded, zombie, or detached state). `force-unlock` does not validate whether the lock is actually stale — it simply deletes the DynamoDB item. If a real Terraform process is still actively modifying state and the lock is removed, the locking mechanism breaks and concurrent state writes can occur, corrupting the state file. DynamoDB lock entries do not auto-expire (option D) — there is no built-in TTL; they must be manually released.

---

### Question 11 — Two Simultaneous Applies Against S3 Backend Without DynamoDB Locking

**Difficulty**: Hard
**Answer Type**: many
**Topic**: The S3 backend without a `dynamodb_table` has no locking mechanism — concurrent `terraform apply` operations can both read, modify, and write state simultaneously, causing state corruption and orphaned resources

**Scenario**:
A team runs two separate CI pipelines that both target the same S3 backend with identical `bucket` and `key` values. The backend block does not include a `dynamodb_table` argument. Both pipelines trigger simultaneously due to a CI misconfiguration. Pipeline A creates three new EC2 instances and completes in 4 minutes. Pipeline B creates two new S3 buckets and completes in 5 minutes. When the operations team later runs `terraform plan`, it shows the three EC2 instances as resources "to be created" even though they exist in AWS.

**Question**:
Which TWO statements accurately explain what happened and the ongoing risk?

- A) Without a `dynamodb_table`, the S3 backend has no distributed locking mechanism. Both pipelines read the same initial state, made their respective changes, and each wrote their final state back to S3. Pipeline B's write (completing last) overwrote Pipeline A's write — Pipeline B's state only contains the two S3 buckets, with no record of the three EC2 instances created by Pipeline A
- B) S3 provides native atomic writes through object versioning, which prevents state corruption — the DynamoDB table is only needed to display a user-friendly "locked" error message when concurrent applies are attempted, not to actually prevent corruption
- C) The next `terraform plan` shows the three EC2 instances as "to be created" because they exist in AWS but are absent from the current state file (which was overwritten by Pipeline B). Without any state entry for these instances, Terraform considers them unmanaged and would create duplicate EC2 instances if `terraform apply` is run
- D) Terraform detects the state version mismatch from the two concurrent writes and automatically merges the two state files, preserving all resource records from both pipelines — the "to be created" output indicates a separate, unrelated issue

**Answer**: A, C

**Explanation**:
**(A)** is correct — the S3 backend uses optimistic reads and writes. Without a DynamoDB lock table, nothing prevents two Terraform processes from reading the same state version, making independent changes, and then writing their results. The last write wins — Pipeline B's state (written last, 5 minutes after start) overwrote Pipeline A's state. Since Pipeline B was not aware of the EC2 instances created by Pipeline A, its written state contains no record of them. **(C)** is correct — because the EC2 instances exist in AWS but have no entry in the current (Pipeline B-authored) state file, Terraform treats them as unmanaged infrastructure. The next `terraform plan` will show them as resources to create, and a `terraform apply` would attempt to provision duplicate instances. The remedy requires manually importing or re-associating the orphaned resources. **(B)** is incorrect — S3 object versioning preserves history but does not prevent concurrent writes or merge them. **(D)** is incorrect — Terraform has no automatic state merge capability.

---

### Question 12 — Accidentally Overwriting Remote State with `terraform state push`

**Difficulty**: Medium
**Answer Type**: one
**Topic**: `terraform state push` overwrites remote state with the provided local file with no safety confirmation prompt — pushing an older state file loses all resource records added since that snapshot was taken

**Scenario**:
An engineer is investigating a state corruption issue. They have a local backup file `backup-last-week.tfstate` from seven days ago. Intending to inspect it with `terraform show`, they accidentally run:

```bash
terraform state push backup-last-week.tfstate
```

The command executes immediately with no confirmation prompt and succeeds. The team's production Terraform state in S3 is now overwritten with the seven-day-old snapshot. The team ran six successful `terraform apply` operations during the past week, adding 23 new resources and modifying 11 existing ones.

**Question**:
What is the immediate consequence of this accidental push, and what should the team do first?

- A) The push fails silently — `terraform state push` only works when the local file is newer than the remote state (based on the state serial number), so an older backup would be rejected and the production state is unaffected
- B) The production state is now the seven-day-old snapshot. All 23 resources added during the past week exist in AWS but are no longer recorded in state — Terraform considers them unmanaged. The team's immediate priority is to restore the correct state. If S3 bucket versioning was enabled, they can retrieve the previous state version using `aws s3api get-object --version-id <id>` and push it back with `terraform state push`. If versioning was not enabled, the state must be reconstructed by importing the 23 orphaned resources
- C) `terraform state push` automatically creates a timestamped backup of the existing remote state before overwriting it — the team can run `terraform state pull > current.tfstate` to retrieve this backup and push it back
- D) The team should immediately run `terraform apply` to re-create the 23 missing resources before anyone else runs `terraform plan`, because a plan would show 23 resources scheduled for destruction (since they exist in state but not in the cloud)

**Answer**: B

**Explanation**:
`terraform state push <file>` is a destructive operation that overwrites the remote backend's state file with the provided local file, with no confirmation prompt and no built-in backup step. It does check the state serial number by default (it will warn if the local serial is lower than remote), but it can be forced with `-force`. Once executed, the production state is replaced with the old snapshot. The 23 resources created during the past week exist in AWS but are now absent from state — Terraform will treat them as unmanaged infrastructure and a future plan may attempt to create duplicates. S3 bucket versioning is the key recovery mechanism: if enabled, the previous state object version can be retrieved and re-pushed. This incident illustrates why `terraform state push` should be treated as a dangerous last resort and S3 versioning should always be enabled on state buckets.

---

### Question 13 — `terraform state mv` During a Root-to-Module Refactor

**Difficulty**: Medium
**Answer Type**: one
**Topic**: `terraform state mv <source> <destination>` changes the resource's address in the state file without making any API calls or modifying the actual cloud resource — after the move, `terraform plan` sees no difference between the new configuration address and the updated state address

**Scenario**:
A team originally managed an EC2 instance directly in the root module as `aws_instance.web`. They refactor the configuration to move the instance into a new `module "compute"` child module, where it becomes `aws_instance.server`. Without any state manipulation, `terraform plan` shows:

```
  - aws_instance.web                       (destroy)
  + module.compute.aws_instance.server     (create)
```

The EC2 instance has been running in production for two years — the team cannot tolerate a destroy-and-recreate cycle. A senior engineer recommends running:

```bash
terraform state mv aws_instance.web module.compute.aws_instance.server
```

**Question**:
What does `terraform state mv` accomplish in this scenario, and what should `terraform plan` show immediately after?

- A) `terraform state mv` terminates the old EC2 instance and provisions a new one under the new module address — it achieves an in-place replacement that avoids the destroy-and-create cycle by using the same AMI and configuration
- B) `terraform state mv` renames the resource's address in the state file from `aws_instance.web` to `module.compute.aws_instance.server` without making any AWS API calls and without modifying the EC2 instance. The actual cloud resource is completely unaffected. After this command, `terraform plan` should show no changes (or only minor drift-related attribute updates) because the configuration address (`module.compute.aws_instance.server`) now matches the updated state address
- C) `terraform state mv` is equivalent to `terraform import` — it re-discovers the EC2 instance under the new module address by querying AWS, which is why it prevents the destroy-and-create cycle
- D) `terraform state mv` updates both the state file and the Terraform configuration automatically — the root module resource block is removed and the child module block is created as part of the command

**Answer**: B

**Explanation**:
`terraform state mv <source> <destination>` is a pure state manipulation command — it changes the address of a resource record within the state file and makes no API calls to any provider. The actual EC2 instance is completely unaffected. Before the command, the state entry is `aws_instance.web`; after it, the entry is `module.compute.aws_instance.server`. When Terraform now runs a plan, it compares the configuration (which declares `module.compute.aws_instance.server`) against the state (which now also records `module.compute.aws_instance.server`) and finds a match — resulting in no planned changes. This is the standard pattern for avoiding destroy-recreate cycles during module refactoring, alongside the `moved` block which achieves the same result declaratively in HCL without a CLI command.

---
