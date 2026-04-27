# Terraform Associate Exam Questions

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

## Answer Key

| Q# | Answer(s) | Explanation | Source | Difficulty |
|----|-----------|-----------:|--------|------------|
| 1 | C | N/A | The `required_version` argument sets the minimum Terraform CLI version required to use this configuration | Easy |
| 2 | D | N/A | The default hostname in a Terraform provider source address is registry.terraform.io when no hostname is specified | Easy |
| 3 | D | N/A | The -upgrade flag on terraform init advances locked provider versions to the newest versions satisfying constraints | Easy |
| 4 | D | N/A | A resource block references an aliased provider using the `provider = <type>.<alias>` syntax | Medium |
| 5 | D | N/A | Terraform keeps only one .tfstate.backup file — the previous state from the most recent apply | Medium |
| 6 | D | N/A | The -refresh=false flag skips live API queries and plans against the cached state — faster but potentially stale | Medium |
| 7 | D | N/A | The -json flag on terraform show outputs state in machine-readable JSON format suitable for parsing by scripts | Medium |
| 8 | D | N/A | terraform state pull downloads the current remote state and writes it to stdout for inspection or backup | Medium |
| 9 | D | N/A | sensitive = true only controls terminal display — the value is still written to state in plaintext | Medium |
| 10 | D | N/A | One of the four state purposes is performance caching — avoiding live API queries for every resource on every plan | Medium |
| 11 | A, C | N/A | Local state has no locking and no sharing — both are required for team collaboration and production safety | Medium |
| 12 | D | N/A | Terraform Core communicates with provider plugins over gRPC — providers run as separate processes | Hard |
| 13 | A, C | N/A | Each provider entry in the lock file contains the exact installed version and cryptographic hashes — both are required for reproducibility and verification | Hard |
