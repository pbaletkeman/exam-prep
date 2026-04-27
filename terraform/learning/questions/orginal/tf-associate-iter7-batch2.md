# Terraform Associate (004) — Question Bank Iter 7 Batch 2

**Iteration**: 7
**Iteration Style**: Fill-in-the-blank / complete the HCL — given a partial configuration or partial statement, select the term or argument that correctly fills the blank
**Batch**: 2
**Objective**: 2 — Terraform Fundamentals (Providers & State)
**Generated**: 2026-04-25
**Total Questions**: 13
**Difficulty Split**: 3 Easy / 8 Medium / 2 Hard
**Answer Types**: 10 `one` / 3 `many` / 0 `none`

---

## Questions

---

### Question 1 — `required_version` in the `terraform` Block

**Difficulty**: Easy
**Answer Type**: one
**Topic**: The `required_version` argument sets the minimum Terraform CLI version required to use this configuration

**Question**:
Complete the `terraform` block so that Terraform will refuse to run with any CLI version older than `1.5.0`:

```hcl
terraform {
  ___________ = ">= 1.5"

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}
```

What argument name fills the blank?

- A) `minimum_version`
- B) `terraform_version`
- C) **`required_version`**
- D) `cli_version`

**Answer**: C

**Explanation**:
`required_version` is the argument in the `terraform {}` block that constrains which versions of the Terraform CLI can execute the configuration. If a team member runs an older CLI that does not satisfy the constraint (e.g., Terraform 1.3.x with `>= 1.5`), Terraform will immediately return an error and refuse to proceed. This prevents accidental use of older CLI versions that may behave differently or lack features the configuration depends on. The argument name is `required_version` — not `minimum_version`, `terraform_version`, or `cli_version`, which do not exist.

---

### Question 2 — Default Registry Hostname in Provider Source Addresses

**Difficulty**: Easy
**Answer Type**: one
**Topic**: The default hostname in a Terraform provider source address is registry.terraform.io when no hostname is specified

**Question**:
Complete the following statement:

> "When a provider source address is written in the short form `hashicorp/aws`, Terraform expands it to the fully qualified address `___________.terraform.io/hashicorp/aws` by supplying the default registry hostname."

What word fills the blank?

- A) `releases`
- B) `providers`
- C) `app`
- D) **`registry`**

**Answer**: D

**Explanation**:
Provider source addresses follow the format `<hostname>/<namespace>/<type>`. When the hostname is omitted — as in the short form `"hashicorp/aws"` — Terraform uses the default hostname `registry.terraform.io`. The fully qualified address is therefore `registry.terraform.io/hashicorp/aws`. This is the public Terraform Provider Registry where Official, Partner, and Community providers are hosted. `releases.hashicorp.com` is where HashiCorp CLI binaries are distributed; `app.terraform.io` is the HCP Terraform (formerly Terraform Cloud) hostname; neither is the default provider registry host.

---

### Question 3 — `terraform init -upgrade` Flag

**Difficulty**: Easy
**Answer Type**: one
**Topic**: The -upgrade flag on terraform init advances locked provider versions to the newest versions satisfying constraints

**Question**:
A team has `.terraform.lock.hcl` pinned to AWS provider `5.28.0`. A new `5.35.0` version has been released. The team wants to deliberately update the lock file to use the newer version. Complete the command:

```bash
terraform init ___________
```

What flag fills the blank?

- A) `--refresh`
- B) `--update`
- C) `-reconfigure`
- D) **`-upgrade`**

**Answer**: D

**Explanation**:
`terraform init -upgrade` instructs Terraform to ignore the existing lock file and re-resolve all providers to the newest versions that satisfy the declared constraints. After the upgrade, it writes the new versions and updated checksums back to `.terraform.lock.hcl`. This is the correct deliberate workflow for advancing provider versions: run `terraform init -upgrade`, review the updated lock file diff, commit the new lock file to version control. Without `-upgrade`, `terraform init` honours the existing lock file and will not install a newer version even if one is available. `-reconfigure` is for backend reconfiguration, not provider versions.

---

### Question 4 — Provider Alias Reference in a Resource Block

**Difficulty**: Medium
**Answer Type**: one
**Topic**: A resource block references an aliased provider using the `provider = <type>.<alias>` syntax

**Question**:
An engineer defines two AWS provider configurations — a default (`us-east-1`) and an aliased (`eu-west-1`). Complete the resource block so the S3 bucket is created in `eu-west-1`:

```hcl
provider "aws" {
  region = "us-east-1"
}

provider "aws" {
  alias  = "europe"
  region = "eu-west-1"
}

resource "aws_s3_bucket" "eu_assets" {
  bucket   = "acme-eu-assets-2024"
  provider = ___________
}
```

What value fills the blank?

- A) `"aws.europe"`
- B) `aws_europe`
- C) `"europe"`
- D) **`aws.europe`**

**Answer**: D

**Explanation**:
The `provider` meta-argument in a resource block takes the value `<provider_type>.<alias>` — written **without quotes** as a reference expression, not a string. For an AWS provider with `alias = "europe"`, the reference is `aws.europe`. The format is always the provider type label (matching the key in `required_providers`, e.g., `aws`) followed by a dot and the alias name. `"aws.europe"` (with quotes) would be a string literal — not a provider reference — and would cause a validation error. `"europe"` alone is missing the provider type prefix. Using the correct unquoted `aws.europe` reference tells Terraform to use the `eu-west-1` provider configuration for this resource.

---

### Question 5 — `terraform.tfstate.backup` — Only One Backup Kept

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Terraform keeps only one .tfstate.backup file — the previous state from the most recent apply

**Question**:
Complete the following statement:

> "Terraform automatically creates `terraform.tfstate.backup` before each apply. This file contains the state from the ___________ successful apply — **not** a full history of all previous states."

What word or phrase fills the blank?

- A) original
- B) first
- C) oldest
- D) **previous (most recent)**

**Answer**: D

**Explanation**:
`terraform.tfstate.backup` is overwritten on every apply — it always contains the state from the **most recently completed** apply, not the one before that or an original snapshot. Terraform does not maintain a rolling history of state files locally; the backup file provides only one level of undo. This is why remote backends with versioning enabled (such as S3 with `versioning = true`) are strongly recommended for production use — they retain the full history of every state version, allowing recovery from any previous point. After each successful apply: the old `terraform.tfstate` becomes the new `terraform.tfstate.backup`, and the newly written state becomes the new `terraform.tfstate`.

---

### Question 6 — `terraform plan -refresh=false`

**Difficulty**: Medium
**Answer Type**: one
**Topic**: The -refresh=false flag skips live API queries and plans against the cached state — faster but potentially stale

**Question**:
A team runs `terraform plan` in a large production environment with hundreds of resources. Each plan takes 8 minutes because Terraform queries the live API for every resource. An engineer wants to run a faster plan using only the cached state file without making any live API calls. Complete the command:

```bash
terraform plan ___________
```

What flag fills the blank?

- A) `-no-refresh`
- B) `-fast`
- C) `-cached`
- D) **`-refresh=false`**

**Answer**: D

**Explanation**:
`terraform plan -refresh=false` tells Terraform to skip the live resource refresh step and generate the plan entirely from the values cached in the state file. This significantly reduces planning time in large environments where API round-trips dominate. The trade-off is that any drift — resources changed outside Terraform since the last apply — will not be detected. This flag is appropriate when you have high confidence that the state file accurately reflects reality (e.g., immediately after a clean apply in a controlled environment). `-no-refresh`, `-fast`, and `-cached` are not valid Terraform flags. The correct syntax is `-refresh=false` (using the equals form).

---

### Question 7 — `terraform show -json` for Machine-Readable State

**Difficulty**: Medium
**Answer Type**: one
**Topic**: The -json flag on terraform show outputs state in machine-readable JSON format suitable for parsing by scripts

**Question**:
A CI/CD pipeline needs to parse Terraform state values programmatically using a script. Complete the command to produce machine-readable JSON output of the current state:

```bash
terraform show ___________
```

What flag fills the blank?

- A) `-machine`
- B) `-output`
- C) `-parse`
- D) **`-json`**

**Answer**: D

**Explanation**:
`terraform show` without flags produces a human-readable text representation of the current state — useful for reading in a terminal but not suitable for scripting. Adding the `-json` flag switches the output format to structured JSON, which can be parsed by tools like `jq`, processed by CI scripts, or consumed by other automation. This is the standard approach for extracting specific resource attributes from state in automated pipelines. `terraform show plan.tfplan -json` also works to output a saved plan file as JSON. `-machine`, `-output`, and `-parse` are not valid `terraform show` flags.

---

### Question 8 — `terraform state pull` Writes to stdout

**Difficulty**: Medium
**Answer Type**: one
**Topic**: terraform state pull downloads the current remote state and writes it to stdout for inspection or backup

**Question**:
Complete the following statement about the `terraform state pull` command:

> "Running `terraform state pull` downloads the current remote state and writes it to ___________, making it easy to inspect the raw state JSON or create a local backup file using shell redirection."

What word or phrase fills the blank?

- A) a file named `state-backup.json` in the current directory
- B) the `.terraform/` directory
- C) `terraform.tfstate` in the current directory, overwriting the local copy
- D) **`stdout`**

**Answer**: D

**Explanation**:
`terraform state pull` outputs the current state — whether from a local backend or a remote backend like S3 or HCP Terraform — directly to **stdout**. This makes it useful in two ways: (1) for inspection: pipe it to `jq` to query specific values (`terraform state pull | jq '.resources[] | select(.type=="aws_instance")'`); (2) for backup: redirect to a file (`terraform state pull > backup.tfstate`). Writing to stdout rather than to a fixed file preserves the existing `terraform.tfstate` on disk and gives the operator full control over what to do with the output. This is the read counterpart to `terraform state push`, which uploads a local file to the remote backend.

---

### Question 9 — `sensitive = true` Scope

**Difficulty**: Medium
**Answer Type**: one
**Topic**: sensitive = true only controls terminal display — the value is still written to state in plaintext

**Question**:
Complete the following statement about Terraform's `sensitive = true` argument:

> "Setting `sensitive = true` on an output variable prevents the value from appearing in ___________ output. It does **not** encrypt or redact the value from the `terraform.tfstate` file, where it remains stored in plaintext."

What word fills the blank?

- A) state
- B) log file
- C) remote backend
- D) **terminal**

**Answer**: D

**Explanation**:
`sensitive = true` on an output variable (or a variable declaration) instructs Terraform to mask the value in **terminal** display — replacing it with `(sensitive value)` when printing plan or apply output. It is a display-only protection. The underlying value is still written to `terraform.tfstate` in plaintext JSON, just like any other resource attribute. This is a critical security distinction: an operator who can read the state file (or run `terraform output -json`) can always retrieve sensitive values. Proper protection requires an **encrypted remote backend** (e.g., S3 with server-side encryption, HCP Terraform with native encryption) — not just `sensitive = true`. The exam frequently tests this "display-only, not encryption" distinction.

---

### Question 10 — Fourth State Purpose: Performance

**Difficulty**: Medium
**Answer Type**: one
**Topic**: One of the four state purposes is performance caching — avoiding live API queries for every resource on every plan

**Question**:
Terraform state serves four primary purposes. Complete the fourth one:

> 1. **Resource identity mapping** — maps `aws_instance.web` → `i-0abcd1234ef567890`
> 2. **Computing diffs** — compares desired state vs known state vs actual state
> 3. **Metadata tracking** — stores dependency information and provider details
> 4. **___________ ** — caches resource attribute values so Terraform does not need to query every resource from the live API on every plan

What word fills the blank for the fourth purpose?

- A) Encryption
- B) Serialisation
- C) Locking
- D) **Performance**

**Answer**: D

**Explanation**:
The fourth explicitly named purpose of Terraform state is **performance**. In a large infrastructure with hundreds or thousands of resources, querying every resource's current attributes from the cloud API on every plan would be prohibitively slow. The state file caches resource attributes from the last apply, so Terraform can compute the plan diff using local data without a complete API refresh. When a full refresh is needed, `terraform plan` (without `-refresh=false`) still queries the API to detect drift, but the cached state means the refresh is targeted rather than exhaustive. The other three purposes — identity mapping, diff computation, and metadata — are equally important but performance is a commonly overlooked fourth reason that state is required.

---

### Question 11 — TWO Limitations of Local State vs Remote State

**Difficulty**: Medium
**Answer Type**: many
**Topic**: Local state has no locking and no sharing — both are required for team collaboration and production safety

**Question**:
A solo developer has been using a local `terraform.tfstate` file for a prototype. Their team is now growing. Which TWO limitations of local state make it unsuitable for team use? (Select two.)

- A) **Local state has no locking** — when two team members run `terraform apply` concurrently, there is no mechanism to prevent both writes from corrupting the state file; remote backends like S3 + DynamoDB provide locking to ensure only one operation modifies state at a time
- B) Local state cannot store resource attribute values — it only stores resource addresses
- C) **Local state has no built-in sharing mechanism** — the `terraform.tfstate` file lives on one engineer's workstation; other team members cannot access it without manually copying the file, making collaboration impractical and error-prone; remote backends (S3, Azure Blob, HCP Terraform) store state in a location all team members can reach
- D) Local state cannot track more than 50 resources — it has a hard limit for small projects only

**Answer**: A, C

**Explanation**:
The two critical local state limitations for team environments are locking and sharing. **(A) No locking**: local state relies on OS file locking, which is unreliable across machines and completely absent when working with a shared file. Two concurrent `terraform apply` runs can interleave state writes, producing corrupted or inconsistent state. Remote backends provide atomic locking (DynamoDB for S3, native locking for HCP Terraform) that serialises operations. **(C) No sharing**: the `terraform.tfstate` file is just a local file. If Engineer A has it on their laptop, Engineer B cannot see current state without a manual file transfer — which introduces version conflicts, lost changes, and confusion about which copy is authoritative. Remote backends give all team members (and CI pipelines) a single shared source of truth. **(B)** is false — local state stores full attribute values. **(D)** is false — there is no resource count limit.

---

### Question 12 — gRPC Protocol Between Terraform Core and Provider

**Difficulty**: Hard
**Answer Type**: one
**Topic**: Terraform Core communicates with provider plugins over gRPC — providers run as separate processes

**Question**:
Complete the following description of Terraform's plugin architecture:

> "When Terraform executes a plan or apply, it launches each required provider as a **separate process**. Terraform Core communicates with these provider processes using **___________** — a high-performance remote procedure call framework. The provider process then makes HTTPS API calls to the target cloud service."

What protocol name fills the blank?

- A) REST
- B) JSON-RPC
- C) SOAP
- D) **gRPC**

**Answer**: D

**Explanation**:
Terraform's plugin architecture uses **gRPC** (Google Remote Procedure Call) for communication between the Terraform Core binary and provider plugin processes. gRPC was chosen because it provides strong typing via Protocol Buffers, efficient binary serialisation, and bidirectional streaming — suitable for the high-frequency CRUD calls Terraform makes to providers during plan and apply. The separation into distinct processes means providers can be upgraded, versioned, and distributed independently of Terraform Core. The provider process, in turn, translates Terraform's gRPC calls into the specific HTTPS API calls required by the target service (AWS, Azure, GCP, etc.). REST, JSON-RPC, and SOAP are other RPC/API protocols but are not used for Terraform Core ↔ provider plugin communication.

---

### Question 13 — TWO Contents of a `.terraform.lock.hcl` Provider Entry

**Difficulty**: Hard
**Answer Type**: many
**Topic**: Each provider entry in the lock file contains the exact installed version and cryptographic hashes — both are required for reproducibility and verification

**Question**:
A team reviews a `.terraform.lock.hcl` file entry:

```hcl
provider "registry.terraform.io/hashicorp/aws" {
  version     = "5.31.0"
  constraints = "~> 5.0"
  hashes = [
    "h1:abc123...",
    "zh:def456...",
  ]
}
```

Which TWO of the following correctly describe the purpose of properties in this lock file entry? (Select two.)

- A) **The `version` field records the exact provider version that was installed** — on every subsequent `terraform init` (without `-upgrade`), Terraform installs this exact version rather than re-resolving from the constraint; this ensures all team members and CI pipelines use identical provider behaviour regardless of when they initialise
- B) The `constraints` field is used by Terraform to re-download the provider if the `version` field is missing; it is only a fallback and serves no purpose when `version` is present
- C) **The `hashes` field contains cryptographic checksums of the provider binary for each supported platform** — when `terraform init` downloads the provider, it verifies the binary's hash against the recorded values; if the hash does not match (e.g., the binary has been tampered with or the wrong binary was downloaded), Terraform refuses to proceed; this prevents supply-chain attacks
- D) The `hashes` field stores the SHA-256 checksum of the `.terraform.lock.hcl` file itself, used to detect if the lock file was manually modified

**Answer**: A, C

**Explanation**:
**(A)** The `version` property is the lock file's primary reproducibility mechanism — it pins the exact installed version so that `terraform init` on any machine at any future time installs `5.31.0`, not the newest `~> 5.0`-compatible version available at that moment. This is what makes provider installations deterministic across team members and CI pipelines. **(C)** The `hashes` array contains platform-specific cryptographic checksums (`h1:` prefix for the zip archive hash, `zh:` for the individual binary) that `terraform init` verifies on download. This prevents a compromised registry or man-in-the-middle attack from substituting a malicious binary without detection. **(B)** is false — `constraints` records what constraint was in effect when the version was selected, primarily for informational/audit purposes; it is not a fallback. **(D)** is false — hashes verify the **provider binary**, not the lock file itself.

---
