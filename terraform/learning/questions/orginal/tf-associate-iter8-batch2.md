---
iteration: 8
batch: 2
style: "Ordering / sequencing"
style_note: >
  Every question presents a workflow, lifecycle, or list of steps and asks the
  candidate to identify the correct order, which step comes first or last, or
  which option correctly sequences a process.
topics:
  - Providers & Plugin Model (Objective 2 — prompt02)
  - Terraform State (Objective 6 — prompt03)
sources:
  - prompt02-providers-plugin-model.md
  - prompt03-terraform-state.md
question_count: 13
difficulty_split: "3 Easy / 8 Medium / 2 Hard"
answer_type_split: "10 one / 3 many"
---

# Terraform Associate (004) — Iteration 8 · Batch 2
## Providers & State · Ordering / Sequencing

---

### Question 1

**Difficulty:** Easy
**Answer Type:** one
**Topic:** Which step comes FIRST inside `terraform init` when installing a provider

When `terraform init` installs a provider for the first time, it performs several sub-steps in a fixed order. Which of the following occurs FIRST?

A) Terraform downloads the provider binary from the registry
B) Terraform verifies the downloaded binary's cryptographic hash
C) Terraform reads the `required_providers` block in the configuration to determine which providers are needed
D) Terraform writes the provider version to `.terraform.lock.hcl`

**Answer:** C

**Explanation:** `terraform init` must know WHAT to install before it can do anything else. The first step is always reading the `required_providers` block to learn the provider source addresses and version constraints. Only after that does it contact the registry, resolve the matching version, download the binary, verify its hash, and finally write the resolved version and hashes to `.terraform.lock.hcl`. Option A (download) and B (hash verification) both come after the registry lookup. Option D (write lock file) is the last step.

---

### Question 2

**Difficulty:** Easy
**Answer Type:** one
**Topic:** Order of calls in the provider communication chain

Terraform Core, the provider plugin, and the cloud API form a three-tier communication chain. Which of the following correctly orders the calls from FIRST to LAST when Terraform creates a resource?

A) Cloud provider API → Provider plugin binary → Terraform Core
B) Terraform Core → Provider plugin binary (via gRPC) → Cloud provider API (via HTTPS)
C) Provider plugin binary → Terraform Core (via gRPC) → Cloud provider API
D) Terraform Core → Cloud provider API (via HTTPS) → Provider plugin binary (via gRPC)

**Answer:** B

**Explanation:** The communication flows in one direction: Terraform Core sends instructions to the provider plugin over gRPC (the two run as separate processes). The provider plugin then translates those instructions into HTTPS API calls to the actual cloud service. Terraform Core never contacts the cloud API directly — that is the provider's responsibility. Options A and C reverse the direction. Option D skips the provider layer and has Core contacting the API directly, which is incorrect.

---

### Question 3

**Difficulty:** Easy
**Answer Type:** many
**Topic:** Correct ordering of state file backup creation during `terraform apply`

Which TWO of the following correctly describe the ordering relationship between `terraform.tfstate.backup` and `terraform.tfstate` during a `terraform apply` operation?

A) Terraform creates `terraform.tfstate.backup` BEFORE overwriting `terraform.tfstate` — the backup is taken from the existing state file so that the previous state is preserved if the apply is interrupted or fails
B) `terraform.tfstate.backup` is created AFTER `terraform.tfstate` is updated — the backup captures the new state so it can be promoted if needed
C) There is only ever ONE `terraform.tfstate.backup` file on disk — each apply overwrites the previous backup with the state from the BEGINNING of that apply run
D) Terraform keeps 10 rotating backup files (`.backup.1` through `.backup.10`) — it never overwrites a backup until all 10 slots are full

**Answer:** A, C

**Explanation:** During `terraform apply`, Terraform first copies the EXISTING `terraform.tfstate` into `terraform.tfstate.backup` (A) — so you always have the previous state if something goes wrong. It then overwrites `terraform.tfstate` with the new state after resources are changed. Only ONE backup is kept (C) — each apply overwrites the single `.backup` file with the state from just before that run. Option B incorrectly states the backup is made after the update. Option D is false — Terraform maintains exactly one backup, not a rotating set.

---

### Question 4

**Difficulty:** Medium
**Answer Type:** one
**Topic:** Correct sequence to update a locked provider version

A team's `.terraform.lock.hcl` pins the AWS provider at `5.28.0`. A new version `5.31.0` is available and the team wants to upgrade. Which of the following correctly orders the steps to safely update to `5.31.0`?

A) Delete `.terraform.lock.hcl` manually → Run `terraform plan` → Commit the resulting lock file
B) Run `terraform init -upgrade` to resolve the newest version within the existing constraint and update the lock file → Review the updated `.terraform.lock.hcl` → Run `terraform plan` to verify there are no unexpected changes → Commit the updated lock file to version control
C) Edit `.terraform.lock.hcl` directly to change the version field from `5.28.0` to `5.31.0` → Run `terraform apply`
D) Change the version constraint from `~> 5.0` to `= 5.31.0` → Run `terraform init` → Change the constraint back to `~> 5.0`

**Answer:** B

**Explanation:** The correct sequence is: run `terraform init -upgrade` (this is the only supported way to advance a locked provider version — it re-resolves the constraint and updates the lock file with the new version and new hashes) → review the lock file change to confirm the expected version was selected → run `terraform plan` to confirm no unexpected API changes come with the new provider → commit the updated lock file. Option A (deleting the lock file manually) works but skips review and is not the recommended approach. Option C is unsafe — manually editing the lock file leaves mismatched hashes. Option D is unnecessarily roundabout.

---

### Question 5

**Difficulty:** Medium
**Answer Type:** one
**Topic:** Sequence of Terraform's three sources of truth during `terraform plan`

When `terraform plan` runs, it consults three sources of information. Which of the following correctly orders them from FIRST consulted to LAST consulted?

A) Live cloud API (actual state) → `terraform.tfstate` (known state) → `.tf` files (desired state)
B) `.tf` configuration files (desired state) → `terraform.tfstate` (known/cached state) → Live cloud provider API (actual state refreshed) — all three are then compared to compute the diff
C) `terraform.tfstate` → Live cloud API → `.tf` files — the plan is computed after all three are gathered in this order
D) Live cloud API → `.tf` files → `terraform.tfstate` — state is always read last to avoid stale comparisons

**Answer:** B

**Explanation:** Terraform establishes desired state by parsing the `.tf` configuration files first. It then reads the existing `terraform.tfstate` for the last-known attributes. Finally it queries the live cloud provider APIs to get the actual current state (the refresh step). With all three inputs gathered, Terraform computes the diff and outputs the plan. Options A, C, and D all misorder the sequence. The `.tf` files are always read first because they define the desired endpoint the plan is working toward.

---

### Question 6

**Difficulty:** Medium
**Answer Type:** one
**Topic:** Correct sequence to rename a resource without triggering destroy + recreate

An engineer renames `resource "aws_instance" "web"` to `resource "aws_instance" "app_server"` in the HCL configuration and then runs `terraform plan`. The plan shows one instance being DESTROYED and one being CREATED. Which of the following correctly orders the steps to rename the resource WITHOUT destroying and recreating it?

A) Run `terraform apply` first to destroy and recreate the instance — then rename in HCL
B) Rename in HCL → run `terraform plan` → run `terraform apply -refresh-only` to skip the destroy
C) Run `terraform state mv aws_instance.web aws_instance.app_server` FIRST to update the state file to the new name → THEN rename the block in the HCL configuration → run `terraform plan` to confirm "No changes"
D) Edit `terraform.tfstate` directly to change the resource name → rename in HCL → run `terraform plan`

**Answer:** C

**Explanation:** When Terraform sees a renamed resource block, it treats the old name as destroyed and the new name as a new resource to create. To prevent this, run `terraform state mv aws_instance.web aws_instance.app_server` FIRST — this renames the resource in the state file so Terraform knows the new block name refers to the same physical resource. Then rename the HCL block. The subsequent `terraform plan` should show "No changes" because the state and config now agree. Option A destroys infrastructure unnecessarily. Option B does not help — `-refresh-only` is for drift detection, not renames. Option D (manual state file editing) is dangerous and unsupported.

---

### Question 7

**Difficulty:** Medium
**Answer Type:** one
**Topic:** Sequence of operations to stop Terraform from managing a resource WITHOUT destroying it

An engineer wants to remove an S3 bucket from Terraform management — keeping the bucket in AWS — because it will be managed by a different tool going forward. Which of the following correctly orders the steps?

A) Run `terraform destroy -target aws_s3_bucket.logs` → Remove the resource block from HCL → Run `terraform plan` to confirm
B) Remove the resource block from the HCL configuration → Run `terraform apply` (Terraform will detect the missing block and delete the resource from the cloud)
C) Run `terraform state rm aws_s3_bucket.logs` FIRST to remove the resource from state (this does NOT delete the real bucket) → THEN remove the resource block from the HCL configuration → Run `terraform plan` to confirm "No changes"
D) Run `terraform state push` → Remove the resource block → Run `terraform apply`

**Answer:** C

**Explanation:** `terraform state rm` removes a resource from the state file without touching the actual cloud resource — the S3 bucket remains in AWS. Once removed from state, Terraform no longer tracks it. You can then safely delete the HCL block: because Terraform has no state entry for the resource, it does not plan a destroy action. Running `terraform plan` afterward confirms "No changes." Option A uses `terraform destroy` which actually deletes the bucket. Option B removes the HCL first — this would cause `terraform apply` to destroy the bucket. Option D (`state push`) is for uploading an entire state file, not for removing individual resources.

---

### Question 8

**Difficulty:** Medium
**Answer Type:** one
**Topic:** Correct order of state inspection commands in a debugging workflow

An engineer is debugging an unknown Terraform-managed environment and needs to investigate a specific resource's attributes. Which of the following correctly orders the commands from FIRST to LAST for an efficient investigation workflow?

A) `terraform state show` → `terraform state list` → `terraform show`
B) `terraform state list` (enumerate all managed resources and their addresses) → `terraform state show <specific_address>` (display all attributes of the specific resource of interest)
C) `terraform state pull` → `terraform show` → `terraform state list`
D) `terraform show` → `terraform state rm` → `terraform state list`

**Answer:** B

**Explanation:** When you don't know which resources exist, the first step is always `terraform state list` — it outputs all resource addresses currently tracked in state, giving you the exact address strings you need. You then pass a specific address to `terraform state show <address>` to display all attributes for that resource. You cannot run `terraform state show` effectively before `terraform state list` because you need the exact resource address. Option A reverses this order. Option C introduces `terraform state pull` (which downloads raw state JSON) unnecessarily as a first step. Option D includes `terraform state rm` which is destructive and irrelevant to investigation.

---

### Question 9

**Difficulty:** Medium
**Answer Type:** many
**Topic:** Which sequencing statements about the lock file lifecycle are correct

Which TWO of the following correctly describe the lifecycle ordering of `.terraform.lock.hcl`?

A) On the FIRST `terraform init` in a new working directory (no lock file exists), Terraform resolves providers from the registry, downloads them, and CREATES `.terraform.lock.hcl` with the resolved versions and cryptographic hashes
B) On SUBSEQUENT `terraform init` runs (lock file already exists), Terraform downloads whatever new provider version is available and OVERWRITES the lock file automatically, even if no `-upgrade` flag was passed
C) Running `terraform init -upgrade` is the ONLY supported way to advance a locked provider to a newer version — it re-resolves the version constraint, downloads the newer binary, and UPDATES the lock file with the new version and hashes
D) The lock file is read during `terraform apply` but NEVER during `terraform init` — it is exclusively an apply-time verification mechanism

**Answer:** A, C

**Explanation:** Option A correctly describes the lock file's creation: the first `terraform init` creates `.terraform.lock.hcl` recording the exact version and hashes. Option C correctly describes the update path: `terraform init -upgrade` is the supported mechanism to advance a locked version. Option B is false — on subsequent `terraform init` runs WITH an existing lock file, Terraform RESPECTS the locked version and does NOT upgrade unless `-upgrade` is explicitly passed. Option D is false — the lock file is read DURING `terraform init` (to verify or enforce the pinned version), not only during apply.

---

### Question 10

**Difficulty:** Medium
**Answer Type:** one
**Topic:** Sequence of events when a plan computes a diff using three state sources

When `terraform plan` detects a difference between desired and actual state, it follows a specific sequence before reporting that difference to the operator. Which answer correctly describes the sequence of events from the point where the configuration is already parsed to the point where the diff is reported?

A) Refresh live state from cloud API → Compare refreshed state to `terraform.tfstate` to detect lock conflicts → Output plan
B) Read `terraform.tfstate` for last-known attributes → Refresh actual state by calling cloud provider APIs → Compute diff between desired (config), known (state), and actual (live) → Output the plan to the operator
C) Compute diff from config and state file → Refresh live state only if a difference is found → Re-compute diff including live state → Output plan
D) Query cloud API for actual state → Write new `terraform.tfstate` with actual values → Compute diff against config → Output plan

**Answer:** B

**Explanation:** After the config is parsed (desired state is known), Terraform reads `terraform.tfstate` for the last-known resource attributes. It then calls provider APIs to refresh actual state. With all three inputs available, it computes the diff across all three sources and outputs the plan. Option A skips reading the existing state file. Option C defers the live refresh to after an initial diff — Terraform does not work this way; refresh always precedes diff. Option D writes to `terraform.tfstate` before the plan is output, which is incorrect — the state file is only updated after a successful `terraform apply`, not during plan.

---

### Question 11

**Difficulty:** Hard
**Answer Type:** one
**Topic:** Complete sequence of sub-steps when `terraform init` installs a provider with an existing lock file

An engineer runs `terraform init` in a directory that already has `.terraform.lock.hcl` pinning the AWS provider at `5.28.0`. No `-upgrade` flag is used. Which of the following correctly orders ALL sub-steps Terraform performs during this init run from FIRST to LAST?

A) (1) Read `required_providers` block → (2) Contact registry to check for newer versions → (3) Download newest version → (4) Overwrite lock file
B) (1) Read `required_providers` block → (2) Read existing `.terraform.lock.hcl` to find the pinned version → (3) Download the pinned version (`5.28.0`) if not already in local cache → (4) Verify the downloaded binary's hash matches the hash recorded in the lock file → (5) Make provider available in `.terraform/providers/` — lock file is NOT updated
C) (1) Check `.terraform/providers/` cache → (2) Read `required_providers` → (3) Read lock file → (4) Download newest version → (5) Verify hash
D) (1) Delete existing `.terraform.lock.hcl` → (2) Re-resolve providers from registry → (3) Download → (4) Write new lock file

**Answer:** B

**Explanation:** With an existing lock file and no `-upgrade` flag, Terraform respects the lock. The sequence is: (1) read `required_providers` to know which providers are needed → (2) read `.terraform.lock.hcl` to find the pinned version and its hashes → (3) download that exact pinned version if it is not already in the local cache (if it is cached, the download is skipped) → (4) verify the binary hash matches the lock file to detect tampering → (5) make the provider available in `.terraform/providers/` without touching the lock file. The lock file is ONLY updated when `terraform init -upgrade` is run. Option A incorrectly checks for newer versions. Option D incorrectly deletes the lock file.

---

### Question 12

**Difficulty:** Hard
**Answer Type:** one
**Topic:** Sequence of risk exposure steps when state is stored locally on a single developer's machine in a team environment

A team of three engineers all run `terraform apply` from their own laptops, with `terraform.tfstate` stored locally (no remote backend). Which of the following correctly orders the risk events from the FIRST risk that emerges to the LAST and most severe?

A) (1) Inconsistent plan outputs because each engineer's state file may diverge → (2) Concurrent applies may corrupt state due to no locking mechanism → (3) A developer's laptop is lost and the only state file is gone → (4) The team cannot determine which cloud resources Terraform is managing
B) (1) The team cannot use version constraints because local state does not support them → (2) Provider plugins are lost when the laptop is off → (3) State corruption
C) (1) All applies succeed identically because local state files are automatically merged → (2) Encryption fails because local state is cloud-hosted → (3) Lock file conflicts
D) (1) Remote backends are created automatically to compensate → (2) Terraform rejects local state after the second apply → (3) Plan output is suppressed

**Answer:** A

**Explanation:** With local state on multiple laptops, risks emerge in this order: (1) each engineer works from a potentially different (diverged) state file, causing inconsistent or duplicate plan outputs; (2) without any locking mechanism, two engineers can run `terraform apply` concurrently and write conflicting state — corrupting it; (3) if a laptop is lost, the only copy of the state file (mapping HCL configs to real resource IDs) is gone; (4) without the state file, the team cannot determine what Terraform manages, making future plans unreliable. This escalating sequence is exactly why HashiCorp requires a remote backend with locking for all team and production work. Options B, C, and D describe impossible or fictitious scenarios.

---

### Question 13

**Difficulty:** Hard
**Answer Type:** many
**Topic:** Two correct ordering contrasts between provider plugin installation and state file updates

Which TWO of the following correctly contrast WHEN provider plugin installation and state file updates occur in the Terraform lifecycle?

A) Provider plugin installation happens during `terraform init` — the provider binary is downloaded and locked BEFORE any `terraform plan` or `terraform apply` is ever run; the `terraform.tfstate` file is updated AFTER a successful `terraform apply` — not during plan, and not during init
B) Both provider plugin installation and state file updates occur simultaneously during `terraform apply` — init is only for syntax checking and does not affect providers or state
C) The `terraform.tfstate` file is written BEFORE provider plugin installation — Terraform pre-creates a state file skeleton during init and populates it as providers are downloaded
D) Provider plugin installation (during `terraform init`) must be completed and the lock file committed BEFORE running `terraform apply` in a CI pipeline; the state file is written at the END of `terraform apply` after all resource changes have been made — this ordering ensures that if apply is interrupted, the state reflects only the changes that actually completed up to that point

**Answer:** A, D

**Explanation:** Option A correctly identifies the sequencing boundary: provider installation is an `init`-time operation that always PRECEDES any plan or apply. State file updates are an `apply`-time operation that happen AFTER resources are changed. Option D correctly describes the CI pipeline implication of this ordering — init (including lock file verification) must precede apply, and state is written at apply's end to reflect only completed changes. Option B is false — `terraform apply` does not download providers; that is `terraform init`'s job. Option C is false — `terraform.tfstate` is never pre-created during init; it is written only after apply completes resource changes.
