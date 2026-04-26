---
iteration: 8
batch: 8
style: "Ordering / sequencing"
style_note: >
  Every question presents a workflow, lifecycle, or list of steps and asks the
  candidate to identify the correct order, which step comes first or last, or
  which option correctly sequences a process.
topics:
  - State Backends & Locking (Objective 6 — prompt12)
  - Importing Infrastructure & State Inspection (Objective 7 — prompt13)
  - HCP Terraform — Workspaces, Runs & State (Objective 8 — prompt14)
  - HCP Terraform — Governance, Security & Advanced (Objective 8 — prompt15)
sources:
  - prompt12-state-backends-locking-remote-state.md
  - prompt13-importing-infrastructure-state-inspection.md
  - prompt14-hcp-terraform-workspaces-runs-state.md
  - prompt15-hcp-terraform-governance-security-advanced.md
question_count: 13
difficulty_split: "3 Easy / 8 Medium / 2 Hard"
answer_type_split: "10 one / 3 many"
---

# Terraform Associate (004) — Iteration 8 · Batch 8
## State Backends, Importing & HCP Terraform · Ordering / Sequencing

---

### Question 1

**Difficulty:** Easy
**Answer Type:** one
**Topic:** Full declarative import block workflow — all 6 steps in the correct order

An engineer wants to bring an existing S3 bucket under Terraform management using the declarative `import` block introduced in Terraform 1.5. Which of the following correctly sequences ALL steps of this workflow?

A) (1) Run `terraform apply` to create the bucket → (2) Add the `import` block → (3) Run `terraform plan` to verify
B) (1) Add an `import` block to the configuration (`to = aws_s3_bucket.legacy` and `id = "existing-bucket-name"`); (2) Run `terraform plan -generate-config-out=generated.tf` — Terraform validates the import and writes an HCL resource block for the existing resource; (3) Review and adjust the generated configuration; (4) Run `terraform apply` — Terraform imports the bucket into state; (5) Remove (or leave as documentation) the `import` block; (6) Run `terraform plan` to confirm the output is "No changes" — the configuration now matches state
C) (1) Write a `resource "aws_s3_bucket" "legacy" {}` block first; (2) Run `terraform import aws_s3_bucket.legacy existing-bucket-name`; (3) Run `terraform plan -generate-config-out=generated.tf`; (4) Run `terraform apply`
D) (1) Add the `import` block and resource block simultaneously; (2) Run `terraform apply -auto-approve`; (3) Remove the `import` block; (4) Run `terraform plan -generate-config-out` to retroactively generate documentation

**Answer:** B

**Explanation:** The declarative `import` block workflow follows six steps: **(1) Add the `import` block** — specify `to` (the Terraform resource address that will manage the resource) and `id` (the cloud provider's identifier for the existing resource). No `resource` block is required yet if using config generation. **(2) Run `terraform plan -generate-config-out=generated.tf`** — Terraform contacts the provider, reads the existing resource's attributes, validates the import, and writes a fully populated HCL `resource` block to `generated.tf`. If a `resource` block already exists, Terraform validates the import against it instead. **(3) Review the generated configuration** — adjust any computed attributes, remove read-only arguments, and ensure the block reflects the desired configuration. **(4) Run `terraform apply`** — Terraform imports the existing resource into state (the cloud resource is NOT recreated — it is adopted). **(5) Remove the `import` block** — once imported, the block is no longer needed (or may be left as documentation). **(6) Run `terraform plan`** — a clean plan showing "No changes" confirms the configuration exactly matches the imported resource's actual attributes. Option C describes the legacy CLI import workflow, not the declarative import block workflow.

---

### Question 2

**Difficulty:** Easy
**Answer Type:** one
**Topic:** `TF_LOG` and `TF_LOG_PATH` — what each controls and which must be set first for file logging

An engineer wants to capture `DEBUG`-level Terraform logs to a file at `/tmp/terraform.log`. Which of the following correctly sequences the two environment variables and explains why the order matters?

A) `TF_LOG_PATH` must be set before `TF_LOG` — without a file destination, setting `TF_LOG` emits logs to stdout, which immediately mixes with plan output before the file can be opened
B) The order in which the two variables are exported in the shell does not affect the result — both must be set before the Terraform command is executed; `TF_LOG=DEBUG` activates logging at the DEBUG level, and `TF_LOG_PATH=/tmp/terraform.log` redirects that output from stderr to the specified file; if only `TF_LOG` is set, logs go to stderr; if only `TF_LOG_PATH` is set without `TF_LOG`, no logs are generated; both must be set together before the command runs for file logging to work
C) Only `TF_LOG_PATH` is needed — setting it alone automatically enables `DEBUG`-level logging; `TF_LOG` is optional
D) `TF_LOG` and `TF_LOG_PATH` must be set inside the Terraform configuration using `terraform.tfvars` — shell environment variables are not supported for log control

**Answer:** B

**Explanation:** Both `TF_LOG` and `TF_LOG_PATH` are read by Terraform at startup, before any operation begins. The shell does not send logs before the command runs, so the order in which you `export` them in the shell is irrelevant — what matters is that both are set in the environment by the time the Terraform command executes. The functional relationship: **(1) `TF_LOG`** — REQUIRED to enable logging; specifies the verbosity level (`TRACE`, `DEBUG`, `INFO`, `WARN`, `ERROR`); without it, no logs are produced regardless of `TF_LOG_PATH`. **(2) `TF_LOG_PATH`** — OPTIONAL; when set, redirects log output from stderr to the specified file path; when absent, logs go to stderr. A common pattern: `export TF_LOG=DEBUG && export TF_LOG_PATH=/tmp/terraform.log && terraform apply`. Separate logging by component using `TF_LOG_CORE` (Terraform core only) and `TF_LOG_PROVIDER` (provider plugins only) if finer control is needed.

---

### Question 3

**Difficulty:** Easy
**Answer Type:** many
**Topic:** Two correct sequencing facts about backend migration — `terraform init -migrate-state` vs `terraform init -reconfigure`

Which TWO of the following correctly describe sequencing differences between `terraform init -migrate-state` and `terraform init -reconfigure`?

A) `terraform init -migrate-state` must ALWAYS be run BEFORE `terraform init -reconfigure` — `-reconfigure` cannot function unless a prior migration has already occurred
B) When changing a backend configuration, `terraform init -migrate-state` copies existing state from the OLD backend to the NEW backend DURING the `terraform init` process — state migration happens as part of init, before any plan or apply; the local state file (or previous remote state) is preserved in the old location as a backup; after a successful migration, subsequent plan/apply commands use state from the new backend
C) `terraform init -reconfigure` copies all existing state to the new backend AND reconfigures the backend — it is a superset of `-migrate-state` and should always be preferred
D) `terraform init -reconfigure` updates the backend configuration WITHOUT migrating existing state — it discards the link to the old state location and starts fresh with the new backend configuration; any existing local state is effectively abandoned (not deleted from disk, but no longer used by subsequent Terraform operations); `-reconfigure` is appropriate when you intentionally want to ignore previous state (e.g., starting fresh) but dangerous when you expect state continuity

**Answer:** B, D

**Explanation:** **(B)** `terraform init -migrate-state` is the safe path when changing backends and wanting to preserve state continuity. During the `terraform init` run, Terraform reads the current state from the old backend location, writes it to the new backend location, and confirms the migration interactively (unless `-force-copy` is also passed). After init completes, all subsequent plan/apply operations read and write to the new backend. The old state file remains at its original location as an implicit backup. **(D)** `terraform init -reconfigure` takes the opposite approach — it tells Terraform to accept the new backend configuration as authoritative and NOT attempt to migrate any existing state. The result is that the new backend starts with an empty state (or whatever state already exists at the new location). Any state that was in the old backend location is NOT copied — if the old location was the only copy, that state is effectively orphaned. This flag is appropriate for scenarios like resetting a CI workspace or when you know the new backend already has the correct state. Option A is false — the two flags are independent. Option C is false — `-reconfigure` explicitly does NOT migrate state.

---

### Question 4

**Difficulty:** Medium
**Answer Type:** one
**Topic:** Full sequence to migrate from a local backend to an S3 backend — every required step in order

A team has been working locally with a `terraform.tfstate` file. They want to migrate to an S3 backend for team collaboration. Which of the following correctly sequences every required step in the correct order?

A) (1) Create the S3 bucket and DynamoDB table using the AWS console or a separate Terraform configuration; (2) Add the `backend "s3"` block to the `terraform {}` block in the configuration; (3) Run `terraform init -migrate-state` — Terraform detects the new backend, copies the existing local state to S3, and confirms the migration; (4) Verify that `terraform.tfstate` in S3 now contains the migrated state; (5) Commit the updated `.tf` files (with the backend block) to version control; (6) Delete or archive the local `terraform.tfstate` and `terraform.tfstate.backup` files — they are no longer the source of truth
B) (1) Run `terraform apply` to push current state to S3 automatically; (2) Add the backend block afterward
C) (1) Add the backend block; (2) Run `terraform plan` — plan auto-migrates state before generating the plan
D) (1) Create the S3 bucket; (2) Run `terraform state push` to upload state; (3) Add the backend block; (4) Run `terraform init`

**Answer:** A

**Explanation:** Migrating to S3 is a multi-step process that must be done in a specific order: **(1) Infrastructure first** — the S3 bucket and DynamoDB lock table must ALREADY EXIST before Terraform can use them as a backend. They are typically provisioned by a separate "bootstrap" Terraform configuration or via the AWS console. **(2) Add the `backend "s3"` block** — add the block to the `terraform {}` block with `bucket`, `key`, `region`, `dynamodb_table`, and `encrypt = true` arguments. **(3) Run `terraform init -migrate-state`** — this is the critical step. Terraform detects the new backend configuration, reads the existing local `terraform.tfstate`, prompts to confirm migration, and uploads the state to S3. The `-migrate-state` flag explicitly instructs Terraform to carry the existing state forward rather than starting fresh (`-reconfigure`) or failing with a prompt. **(4) Verify** — confirm the state object exists in S3. **(5) Commit** — the backend configuration is now part of the codebase and teammates need it. **(6) Clean up local files** — the local `terraform.tfstate` is now stale. Leaving it in place is harmless (Terraform ignores it after the backend switch) but archiving it prevents confusion. Option D uses `terraform state push` in the wrong position — it cannot push to a backend that hasn't been configured yet.

---

### Question 5

**Difficulty:** Medium
**Answer Type:** one
**Topic:** Stuck state lock recovery — sequence from encountering the error to successful force-unlock

An engineer runs `terraform apply` and receives an error: "Error acquiring the state lock: Lock Info: ID: `a1b2c3d4-e5f6-7890-abcd-ef1234567890` ... the state is already locked by another process." No other engineer is actively running Terraform. Which of the following correctly sequences the steps to safely recover?

A) (1) Delete the DynamoDB lock record manually in the AWS console; (2) Re-run `terraform apply`
B) (1) Delete `terraform.tfstate.backup` and re-run `terraform apply` — the backup lock entry is the cause
C) (1) Confirm that no other `terraform apply` or `terraform plan` process is actually running — check CI/CD pipeline queues, remote workstations, and HCP Terraform run history; (2) Only after confirming the lock is stale (left by a process that died or was killed): run `terraform force-unlock a1b2c3d4-e5f6-7890-abcd-ef1234567890` using the exact lock ID from the error message; (3) Run `terraform apply` again — the lock is now available and the operation proceeds normally; (4) Investigate and fix the root cause of why the previous process did not release the lock
D) (1) Run `terraform force-unlock` immediately without checking whether another process is running — the command is safe and idempotent; (2) Run `terraform apply`

**Answer:** C

**Explanation:** The sequence for stuck lock recovery prioritizes safety before action: **(1) Verify the lock is genuinely stale** — this is the most critical first step. Running `terraform force-unlock` while another `terraform apply` is in progress releases that process's lock, allowing two concurrent state writes, which can corrupt state. Check: is any CI/CD job running this workspace? Is another engineer actively applying? Is there a pending HCP Terraform run? Only proceed if you are CERTAIN the lock is orphaned. **(2) Run `terraform force-unlock LOCK_ID`** using the exact UUID from the error message — the lock ID is required; you cannot force-unlock without it. **(3) Re-run `terraform apply`** — the lock is now released and the next operation can acquire it normally. **(4) Root cause analysis** — a stale lock usually means a process was killed mid-apply or a network interruption prevented normal cleanup. Understanding why prevents recurrence. Option A (manual DynamoDB console deletion) achieves the same result but is more error-prone than using the CLI command. Option D skipping verification is dangerous — `terraform force-unlock` is NOT idempotent and can cause state corruption if misused.

---

### Question 6

**Difficulty:** Medium
**Answer Type:** one
**Topic:** VCS-driven HCP Terraform run lifecycle — from PR creation to successful apply in correct order

A team has connected an HCP Terraform workspace to a GitHub repository with the main branch as the trigger branch. Which of the following correctly sequences the full run lifecycle from a developer's first commit to a successful production apply?

A) (1) Developer opens a PR → (2) HCP Terraform queues a plan-and-apply run that immediately changes infrastructure → (3) The PR is merged if the apply succeeds
B) (1) Developer creates a feature branch and opens a pull request targeting `main`; (2) HCP Terraform automatically triggers a **speculative plan** for the PR — a read-only plan whose result is posted as a status check on the PR; (3) Team reviews the plan output (what infrastructure would change) and the code; (4) Developer merges the PR to `main`; (5) HCP Terraform triggers a new **plan-and-apply** run; (6) If the workspace requires manual confirmation: the plan completes, a team member reviews and approves (or discards) the apply; (7) Apply executes and the run reaches the "Applied" state
C) (1) Developer merges to `main` first → (2) HCP Terraform triggers a speculative plan → (3) If the plan is clean, an apply is auto-queued
D) (1) Developer runs `terraform plan` locally → (2) Uploads the saved plan to HCP Terraform → (3) HCP Terraform applies the uploaded plan

**Answer:** B

**Explanation:** The VCS-driven HCP Terraform workflow uses two distinct run types triggered by different events: **(1) PR creation** triggers a **speculative plan** — a read-only plan that cannot progress to apply. Its purpose is to give the PR reviewer visibility into the infrastructure impact of the proposed code change. The result is posted as a GitHub status check (green/red). **(2) Merge to main** triggers a **plan-and-apply run** — this is the run that can actually change infrastructure. **(3) Plan phase** — HCP Terraform checks out the merged code and runs `terraform plan`. **(4) Manual approval gate** (if configured) — the plan output is presented in the HCP Terraform UI; an authorized team member reviews and clicks "Confirm & Apply" or "Discard". Workspaces can alternatively be configured for auto-apply, which skips this gate. **(5) Apply phase** — `terraform apply` executes the approved plan. **(6) Applied** — the run completes and state is updated. The key sequencing fact: a PR NEVER triggers an apply — only a speculative plan. A merge NEVER triggers a speculative plan — only a real plan-and-apply run.

---

### Question 7

**Difficulty:** Medium
**Answer Type:** one
**Topic:** HCP Terraform policy enforcement levels — sequence from least to most restrictive and what each does to the run

A policy check in HCP Terraform fails during a run. Which of the following correctly sequences the three enforcement levels from least to most restrictive, and describes what each does to the run?

A) `hard-mandatory` (least restrictive, warning only) → `soft-mandatory` (blocks run but can be overridden) → `advisory` (most restrictive, cannot be overridden)
B) `advisory` → `hard-mandatory` → `soft-mandatory` — the middle level blocks the run while the others allow continuation
C) `advisory` (least restrictive — a failed policy check generates a **warning only**; the run is NOT blocked and proceeds to apply normally; the failure is informational); `soft-mandatory` (middle — a failed policy check **blocks the run**; however, an authorized user can override the policy failure and allow the run to continue to apply); `hard-mandatory` (most restrictive — a failed policy check **blocks the run** AND **cannot be overridden** by any user, including organization owners; the only way to continue is to fix the policy or the code)
D) All three levels block the run — they differ only in who can see the policy failure notification, not in whether the run continues

**Answer:** C

**Explanation:** HCP Terraform's three policy enforcement levels form a strict severity ladder: **(1) `advisory`** — the policy is informational. A failure shows a warning in the run output but does NOT block the apply. The run proceeds as if the check passed. Use for awareness-level policies where teams are being notified of non-compliance but not yet forced to fix it. **(2) `soft-mandatory`** — a failure BLOCKS the run at the policy check stage. The run pauses and waits. However, a user with sufficient permissions (e.g., organization owner or policy manager) can manually override the failure and allow the run to continue. Use when compliance is important but exceptions must be possible. **(3) `hard-mandatory`** — a failure BLOCKS the run and the block CANNOT be overridden by any user — not even organization owners. The run can only proceed if the policy condition is satisfied (either by fixing the infrastructure code or updating the policy). Use for absolute compliance requirements (e.g., "encryption must always be enabled"). The correct order from least to most restrictive is: `advisory` < `soft-mandatory` < `hard-mandatory`.

---

### Question 8

**Difficulty:** Medium
**Answer Type:** one
**Topic:** `terraform state mv` sequence — how to rename a resource in state without destroying and recreating it

An engineer has a resource `aws_instance.old_name` in state. They want to rename it to `aws_instance.new_name` in both the `.tf` configuration and in state without destroying and recreating the EC2 instance. Which of the following correctly sequences the steps?

A) (1) Rename the resource block in the `.tf` file from `"old_name"` to `"new_name"`; (2) Run `terraform apply` — Terraform detects the rename and updates state automatically without destroying the resource
B) (1) Rename the resource block in the `.tf` file from `"old_name"` to `"new_name"`; (2) Run `terraform plan` — the plan shows "destroy `aws_instance.old_name`" and "create `aws_instance.new_name`"; (3) Run `terraform state mv aws_instance.old_name aws_instance.new_name` BEFORE applying — this updates the state address so the renamed resource block maps to the existing cloud resource; (4) Run `terraform plan` again — the plan should now show "No changes" (or only attribute-level changes if the config differs from current state)
C) (1) Run `terraform state mv aws_instance.old_name aws_instance.new_name` FIRST before changing any `.tf` file; (2) Rename the resource block in the `.tf` file; (3) Run `terraform plan`; (4) Run `terraform apply`
D) Both B and C describe valid sequences — `terraform state mv` can be run either before or after renaming the resource block in the configuration; the outcome is identical in either case

**Answer:** C

**Explanation:** The correct sequence for renaming a resource using `terraform state mv` is: **(1) Run `terraform state mv` FIRST** — before touching the `.tf` file. This updates the state file so that the existing cloud resource is now recorded under the new address `aws_instance.new_name`. At this point, the `.tf` file still has `aws_instance.old_name` — which means after the `state mv`, `terraform plan` would show "create `aws_instance.old_name`" (it's gone from state) and "no-op on `aws_instance.new_name`" (it's in state but not in config yet). **(2) Rename the resource block in the `.tf` file** — change `resource "aws_instance" "old_name"` to `resource "aws_instance" "new_name"`. Now both state and configuration agree on the new name. **(3) Run `terraform plan`** — the plan should show "No changes" if the config attributes match the existing resource's attributes. **(4) Run `terraform apply`** if any attribute-level changes are needed. Option B's sequence (rename `.tf` first, then `state mv`) also works but involves an intermediate state where `terraform plan` shows a destructive change — that intermediate plan can be alarming and is a potential source of accidental applies. The recommended practice is `state mv` before the rename to avoid ever seeing the destroy/create plan.

---

### Question 9

**Difficulty:** Medium
**Answer Type:** many
**Topic:** Two correct sequencing facts about using `terraform_remote_state` to share outputs across workspaces

Which TWO of the following correctly describe sequencing requirements for the `terraform_remote_state` data source to work correctly across HCP Terraform workspaces?

A) The **producing workspace** (the one whose outputs are being read) must have at minimum a successful `terraform apply` in its history BEFORE the consuming workspace can read its outputs — the `terraform_remote_state` data source reads from the remote state file, which is only populated after a successful apply; if the producing workspace has never been applied (state is empty), the consuming workspace's plan will fail or return null outputs
B) The `terraform_remote_state` data source resolves its outputs during `terraform init` — the producing workspace's state is downloaded at init time, not at plan time; re-running `terraform plan` in the consuming workspace does NOT pick up new outputs from the producing workspace unless `terraform init` is re-run
C) The **consuming workspace** must trigger a new plan/apply run AFTER the producing workspace updates its state — if workspace A (networking) applies and updates `output "vpc_id"`, workspace B (compute) must run a new plan that reads the freshly updated state to get the new `vpc_id` value; workspace B's existing state does not automatically refresh from workspace A's outputs without a new run
D) Both workspaces must be in the same HCP Terraform organization AND the same project — cross-project `terraform_remote_state` references are not supported

**Answer:** A, C

**Explanation:** **(A)** `terraform_remote_state` reads the state file of another workspace at plan/apply time. For this to return real values, the producing workspace must have previously run `terraform apply` — the state file must exist and contain the declared outputs. If the producing workspace has never been applied (empty state), the consuming workspace's plan will either fail with an error ("output does not exist") or show `null` outputs. This creates a dependency ordering requirement for initial deployment: provision the networking workspace first (apply), then provision the compute workspace (which depends on networking outputs). **(C)** `terraform_remote_state` reads the producing workspace's state at the time the consuming workspace runs a plan or apply. If workspace A subsequently applies and changes `vpc_id`, workspace B will NOT automatically re-plan — it will continue to use the old `vpc_id` value from its last run. For workspace B to pick up the updated output, a new plan/apply run must be triggered in workspace B. This is why HCP Terraform offers **run triggers** — workspace B can be configured to automatically trigger a run when workspace A's apply completes. Option B is false — `terraform_remote_state` resolves at plan/apply time, not at init time. Option D is false — `terraform_remote_state` supports cross-organization and cross-project references given proper access credentials.

---

### Question 10

**Difficulty:** Medium
**Answer Type:** one
**Topic:** Legacy CLI import workflow sequence — from finding the existing resource to a clean plan

An engineer needs to import an existing `aws_security_group` (ID `sg-0abc1234def5678`) using the legacy `terraform import` CLI command. Which of the following correctly sequences every required step in the correct order?

A) (1) Run `terraform import aws_security_group.web sg-0abc1234def5678`; (2) Write the resource block after import is complete — the CLI import creates the HCL automatically
B) (1) Write a `resource "aws_security_group" "web" {}` block in the configuration — the resource block MUST exist BEFORE the CLI import command runs; (2) Run `terraform import aws_security_group.web sg-0abc1234def5678` — this writes the resource into state at the address `aws_security_group.web`; (3) Run `terraform state show aws_security_group.web` — inspect all attributes that the provider populated in state; (4) Update the `resource "aws_security_group" "web"` block in the configuration to match the actual attribute values shown; (5) Run `terraform plan` — the goal is "No changes. Your infrastructure matches the configuration."; (6) If the plan shows changes, adjust the configuration and repeat steps 4-5 until the plan is clean
C) (1) Run `terraform import`; (2) Run `terraform plan -generate-config-out=generated.tf`; (3) Run `terraform apply`
D) (1) Run `terraform state pull > backup.tfstate`; (2) Run `terraform import`; (3) Run `terraform plan`

**Answer:** B

**Explanation:** The legacy CLI import workflow has a specific sequence that differs critically from the declarative `import` block: **(1) Write the resource block first** — unlike the `import` block workflow (where config generation is optional), the CLI `terraform import` command REQUIRES an existing resource block at the target address. Without it, the command fails: "Before importing this resource, please create its configuration in the root module." The block can start nearly empty, but it must exist. **(2) Run `terraform import <address> <id>`** — this writes the resource into state at `aws_security_group.web`. The cloud resource is NOT modified. **(3) Run `terraform state show`** — the CLI import does NOT generate HCL. You must manually inspect the state to discover all the attribute values. `terraform state show` shows the resource in HCL-like format with all provider-populated attributes. **(4) Update the configuration** — populate the resource block arguments to match the actual values. **(5) Run `terraform plan`** — check whether the configuration matches state. A clean plan ("No changes") means success. **(6) Iterate** — if the plan shows changes (e.g., Terraform wants to add/change/remove an argument), the configuration still disagrees with state; adjust and re-plan. Option C incorrectly mixes CLI import with the `import` block's `-generate-config-out` flag — that flag only works with the declarative `import` block, not the CLI command.

---

### Question 11

**Difficulty:** Medium
**Answer Type:** one
**Topic:** HCP Terraform OIDC dynamic credentials sequence — no static secrets stored

An engineer configures a workspace to use OIDC (dynamic provider credentials) for AWS authentication instead of storing static `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY` environment variables. Which of the following correctly sequences the steps that occur DURING a single HCP Terraform plan run?

A) (1) HCP Terraform reads `AWS_ACCESS_KEY_ID` from the workspace variables → (2) Passes credentials to the AWS provider → (3) Plan executes
B) (1) The HCP Terraform worker that will execute the run requests a **short-lived OIDC token** from HCP Terraform's OIDC identity provider; (2) The worker presents the OIDC token to AWS STS (using a configured IAM role trust policy that trusts HCP Terraform's OIDC issuer); (3) AWS STS validates the token, verifies that the workspace/organization claims match the trust policy conditions, and returns temporary AWS credentials (access key, secret key, session token) with a short TTL; (4) The Terraform AWS provider uses these temporary credentials to make API calls during the plan; (5) The temporary credentials expire automatically after the run — no long-lived credentials were ever stored in HCP Terraform
C) (1) HCP Terraform generates a new AWS IAM user for each run → (2) Uses those credentials for the plan → (3) Deletes the IAM user after the run
D) OIDC credentials are resolved at `terraform init` time, not during plan — the credentials are cached for 24 hours across multiple runs

**Answer:** B

**Explanation:** The OIDC dynamic credentials sequence eliminates static long-lived secrets from the workflow: **(1) Token request** — at the start of each run, the HCP Terraform worker requests a signed, short-lived OIDC JWT from HCP Terraform's built-in OIDC identity provider. This token contains claims about the workspace, organization, and run context. **(2) STS exchange** — the worker calls `sts:AssumeRoleWithWebIdentity` (or the equivalent for Azure/GCP), presenting the OIDC token. The IAM role's trust policy is configured to trust HCP Terraform's OIDC issuer URL and may restrict which workspaces/organizations can assume the role using condition keys. **(3) Temporary credentials issued** — AWS STS validates the token and returns temporary credentials with a TTL (typically 1 hour or less). **(4) Plan executes** — the Terraform AWS provider uses these temporary credentials for all API calls. **(5) Expiration** — after the run completes (or the TTL elapses), the credentials are no longer valid. No static `AWS_ACCESS_KEY_ID` was ever stored in HCP Terraform, so there is nothing to rotate or accidentally expose. This pattern is considered a security best practice for production HCP Terraform environments.

---

### Question 12

**Difficulty:** Hard
**Answer Type:** one
**Topic:** Complete HCP Terraform run lifecycle including Sentinel policy check and manual approval — all phases in correct order

A team has a workspace configured with a Sentinel policy set at `soft-mandatory` enforcement and with manual apply (confirmation required). Which of the following correctly sequences ALL phases of a complete plan-and-apply run triggered by a merge to the connected VCS branch?

A) (1) Merge triggers run → (2) Apply → (3) Policy check → (4) Plan → (5) Apply confirmed
B) (1) Merge to VCS branch triggers a new run in HCP Terraform; (2) **Plan phase** — HCP Terraform clones the repository, initializes providers, and executes `terraform plan`; plan output is streamed to the UI; (3) **Policy check phase** — Sentinel evaluates the plan output against all assigned policy sets; because the policy is `soft-mandatory` and passes, the run proceeds; if it had failed, an authorized user could override; (4) **Cost estimation phase** (if enabled) — estimated monthly cost delta is computed from the plan; (5) **Awaiting confirmation** — because manual apply is required, the run pauses and shows the plan + cost estimate to team; a team member must click "Confirm & Apply" (or "Discard"); (6) **Apply phase** — `terraform apply` executes the approved plan; state is updated; (7) **Applied** — run completes successfully
C) (1) Merge → (2) Cost estimation → (3) Plan → (4) Policy check → (5) Apply
D) (1) Merge → (2) Plan → (3) Apply → (4) Policy check → (5) State updated — policy checks always run after apply, not before

**Answer:** B

**Explanation:** HCP Terraform's run lifecycle follows a strict phase order designed to maximize visibility and control before changes are made: **(1) Trigger** — a VCS merge to the connected branch starts the run. **(2) Plan phase** — the most computationally intensive phase; Terraform evaluates configuration, reads state, and generates the proposed changes. **(3) Policy check phase** — Sentinel (or OPA) evaluates the PLAN output before any infrastructure changes occur. This ordering is critical: policies check the PLAN, not the already-applied infrastructure. `soft-mandatory` failures can be overridden; `hard-mandatory` failures cannot. **(4) Cost estimation** — if enabled, HCP Terraform computes the monthly cost delta from the plan output. This also runs PRE-apply so the team sees estimated costs before committing. **(5) Awaiting confirmation** — with manual apply, the run pauses here. The team sees the full plan, policy results, and cost estimate before deciding. **(6) Apply phase** — only after explicit confirmation (or auto-apply). **(7) Applied** — state is updated, the run is complete. The critical exam point: policy checks run AFTER plan but BEFORE apply — they evaluate the plan, not the post-apply state. Option D is a common misconception; running policy checks after apply would be too late to prevent non-compliant changes.

---

### Question 13

**Difficulty:** Hard
**Answer Type:** many
**Topic:** Two correct sequencing distinctions between `terraform plan -refresh-only`, `terraform apply -refresh-only`, and a normal `terraform plan` / `terraform apply` when drift is detected

Which TWO of the following correctly describe sequencing differences between refresh-only operations and normal plan/apply operations when infrastructure drift is detected?

A) `terraform plan -refresh-only` is the FIRST and safest step for investigating drift — it queries the cloud provider for the current state of all managed resources, compares the results to the recorded state, and shows ONLY what has drifted (i.e., what is in the cloud that differs from state); it does NOT show configuration-driven changes (e.g., a new resource block added to `.tf` files) — refresh-only vs normal plan are reading two different "gaps": refresh-only reads the gap between STATE and CLOUD, while a normal plan reads the gap between CONFIGURATION and STATE (after refreshing state from cloud)
B) `terraform apply -refresh-only` creates new resources to reconcile drift — it is the inverse of a normal apply
C) In a normal `terraform plan` / `terraform apply` workflow, Terraform FIRST refreshes state from the cloud (reads current attribute values), THEN compares the refreshed state to the configuration, and THEN proposes changes to make the configuration the source of truth — this means a normal apply would REVERT any manual changes (drift) back to what the configuration specifies, which is the OPPOSITE of what `terraform apply -refresh-only` does; `apply -refresh-only` ACCEPTS drift by updating state to match the cloud, while a normal apply REJECTS drift by proposing to reverse it
D) `terraform plan -refresh-only` and a normal `terraform plan` produce identical output — the `-refresh-only` flag only affects apply behavior, not what the plan shows

**Answer:** A, C

**Explanation:** **(A)** `terraform plan -refresh-only` isolates drift investigation by reporting only the delta between current cloud state and recorded state — it ignores configuration-driven changes entirely. If you've added a new resource block but also have a drifted tag on an existing resource, the refresh-only plan shows only the tag drift, not the new resource. This makes it the cleanest tool for answering "what has changed in the cloud since my last apply?" without the noise of pending configuration changes. A normal `terraform plan` also refreshes state from the cloud first, but then proceeds to compare the (now-refreshed) state against the configuration — so it shows BOTH drift effects AND configuration-driven changes together. **(C)** This is the most important sequencing distinction between the two workflows. Normal plan/apply treats CONFIGURATION as the source of truth: it first refreshes state from the cloud (learning about drift), then proposes changes to make the cloud MATCH the configuration — which means it would REVERSE manual console changes (drift). `terraform apply -refresh-only` treats CLOUD as the source of truth: it updates state to MATCH the cloud — which means it ACCEPTS the manual console change as the new desired state. These two workflows are inverses: one enforces configuration, the other acknowledges reality. Choosing between them depends on whether the drift should be reversed (normal apply) or accepted (apply -refresh-only). Option B is false — `apply -refresh-only` never creates resources. Option D is false — the `-refresh-only` flag fundamentally changes what the plan output shows.
