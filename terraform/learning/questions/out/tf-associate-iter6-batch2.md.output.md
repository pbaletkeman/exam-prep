# Terraform Associate Exam Questions

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

## Answer Key

| Q# | Answer(s) | Explanation | Source | Difficulty |
|----|-----------|-----------:|--------|------------|
| 1 | C | N/A | Understanding that terraform init is required after cloning before any other terraform commands | Easy |
| 2 | B | N/A | Understanding the role of .terraform.lock.hcl in preventing unintended provider upgrades | Easy |
| 3 | C | N/A | Understanding that provider alias must be explicitly referenced in a resource block or Terraform uses the default provider | Easy |
| 4 | B | N/A | Understanding the consequences of losing the state file and the recovery path | Medium |
| 5 | B | N/A | Understanding that .backup holds only the immediately previous state, not a full version history | Medium |
| 6 | B | N/A | Understanding that sensitive=true masks terminal output but does not protect state | Medium |
| 7 | B | N/A | Understanding that terraform plan refreshes live state via API and how -refresh=false can speed it up | Medium |
| 8 | A, B | N/A | Identifying TWO correct statements about the effects of running terraform init -upgrade | Medium |
| 9 | B | N/A | Understanding why terraform show may reflect stale state if terraform refresh/plan has not been run | Medium |
| 10 | C | N/A | Diagnosing a provider init failure caused by a malformed source address | Medium |
| 11 | B | N/A | Understanding the dangers of terraform state push and the safer alternatives | Hard |
| 12 | A, B | N/A | Identifying TWO consequences of running terraform apply concurrently without state locking | Hard |
| 13 | B | N/A | Understanding the correct use case for terraform state pull when inspecting or backing up remote state | Medium |
