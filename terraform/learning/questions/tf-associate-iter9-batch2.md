---
iteration: 9
batch: 2
style: "Which is true / which is false?"
style_note: >
  Every question presents one or more statements about a concept and asks the
  candidate to identify which statement(s) are TRUE, or which statement(s) are
  FALSE. Distractors are plausible-sounding misconceptions.
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

# Terraform Associate (004) — Iteration 9 · Batch 2
## Providers & State · Which Is True / Which Is False?

---

### Question 1

**Difficulty:** Easy
**Answer Type:** one
**Topic:** Five provider responsibilities — which statement is TRUE?

Which of the following statements about what a Terraform provider plugin is responsible for is TRUE?

A) A provider is responsible only for authenticating to the cloud API — the Terraform Core binary is responsible for all CRUD operations (create, read, update, delete) and maps resource attributes directly to the state file without provider involvement
B) A provider's responsibilities include: authenticating to the cloud/service API, implementing CRUD operations for resources, exposing data sources, validating resource configuration against a schema, and mapping resource attributes to and from Terraform state
C) A provider plugin must be included in every `.tf` configuration file using an `import` statement — without an explicit `import`, Terraform Core cannot locate the provider binary
D) A provider is responsible for maintaining the `terraform.tfstate` file and is the only component with write access to it — Terraform Core reads state but cannot write to it directly

**Answer:** B

**Explanation:** Option B correctly enumerates all five responsibilities of a Terraform provider plugin: (1) **Authentication** — the provider handles credentials and API authentication so engineers don't write auth logic in HCL; (2) **CRUD operations** — the provider implements Create, Read, Update, Delete for every resource type it manages; (3) **Data sources** — providers expose read-only data sources for querying existing infrastructure; (4) **Validation** — the provider validates resource configuration against its schema before any API call is made; (5) **State mapping** — the provider maps resource attributes (including computed attributes like resource IDs and IP addresses assigned by the cloud) to and from the state file format. Option A is false — providers handle CRUD, not just auth. Option C is false — providers are declared in `required_providers`, not imported via an `import` statement; `import` in Terraform is an entirely different concept (importing existing infrastructure into state). Option D is false — Terraform Core manages writes to the state file; the provider populates attribute values that Core then persists.

---

### Question 2

**Difficulty:** Easy
**Answer Type:** one
**Topic:** `sensitive = true` — which statement is FALSE?

Which of the following statements about the `sensitive = true` argument on an output block is FALSE?

A) Setting `sensitive = true` on an output causes Terraform to display the value as `(sensitive value)` in `terraform apply` and `terraform output` terminal output, preventing accidental exposure in logs
B) Setting `sensitive = true` on an output encrypts the corresponding attribute value before writing it to `terraform.tfstate`, ensuring the value cannot be read from the state file by anyone with access to it
C) `sensitive = true` only affects terminal display — the actual attribute value is still stored in plaintext inside `terraform.tfstate` regardless of the sensitive setting
D) Because sensitive values are stored in plaintext in state, teams handling secrets should use an encrypted remote backend (such as S3 with server-side encryption) for production state files

**Answer:** B

**Explanation:** Option B is FALSE and represents one of the most important security misconceptions in Terraform. `sensitive = true` is a DISPLAY-ONLY flag — it tells Terraform to redact the value in CLI output (terminal display, `terraform output`, plan summaries) by showing `(sensitive value)` instead of the raw value. It does NOT encrypt the value in `terraform.tfstate`. All resource attributes — including passwords, secret keys, tokens, and other credentials — are stored in plaintext JSON inside the state file, regardless of any `sensitive` annotation. This means anyone with access to the state file (or the remote storage bucket containing it) can read those values. Options A, C, and D are all true, correct statements that accurately describe this security reality and the appropriate mitigation (encrypted remote backend).

---

### Question 3

**Difficulty:** Easy
**Answer Type:** many
**Topic:** Which TWO statements about `.terraform.lock.hcl` are TRUE?

Which TWO of the following statements about the `.terraform.lock.hcl` dependency lock file are TRUE?

A) `.terraform.lock.hcl` records the exact provider version (e.g., `5.31.0`) and cryptographic hashes of the installed provider binaries, ensuring that subsequent `terraform init` runs install the identical version and verify binary integrity
B) `.terraform.lock.hcl` should be added to `.gitignore` alongside the `.terraform/` directory — both are auto-generated by `terraform init` and should never be committed to version control
C) To intentionally advance a provider to a newer version within the declared constraint, an engineer runs `terraform init -upgrade` — this updates the lock file to record the new version
D) `.terraform.lock.hcl` contains the full text of all provider source code, making it the authoritative documentation for which provider APIs are available in the configuration

**Answer:** A, C

**Explanation:** **(A)** is TRUE. The lock file records the exact version installed (e.g., `version = "5.31.0"`), the original constraint from `required_providers` (e.g., `constraints = "~> 5.0"`), and cryptographic hashes (`h1:` and `zh:` entries). On subsequent `terraform init` runs, Terraform uses these hashes to verify that the downloaded binary matches what was originally installed — protecting against supply chain tampering. **(C)** is TRUE. `terraform init -upgrade` is the deliberate mechanism for advancing locked provider versions — it ignores the current lock file entries, resolves the newest version matching the constraint, downloads it, verifies it, and rewrites the lock file. Without `-upgrade`, `terraform init` respects the locked version and will not upgrade even if a newer version exists within the constraints. **(B)** is FALSE — this is a critical error. `.terraform.lock.hcl` MUST be committed to version control; `.terraform/` should be gitignored. **(D)** is false — the lock file contains version and hash metadata only, not provider source code.

---

### Question 4

**Difficulty:** Medium
**Answer Type:** one
**Topic:** Local vs remote state — which statement about locking is TRUE?

Which of the following statements about the difference between local and remote Terraform state is TRUE?

A) Local state stored in `terraform.tfstate` supports concurrent apply operations by multiple team members because Terraform automatically detects when another apply is in progress and waits before proceeding
B) Both local and remote state backends implement state locking by default — locking is a built-in feature of the `terraform.tfstate` format and does not depend on the storage backend
C) Local state provides NO state locking — if two engineers run `terraform apply` simultaneously against a local state file, both operations may proceed concurrently and corrupt the state file; remote backends such as S3 with DynamoDB, HCP Terraform, or Azure Blob provide state locking to prevent concurrent applies
D) Remote state locking is only available in paid HCP Terraform plans — free-tier and open-source Terraform users must use local state and manually coordinate applies to prevent conflicts

**Answer:** C

**Explanation:** State locking is a critical feature for team safety and is one of the key advantages of remote state over local state. Local state (`terraform.tfstate` on disk) has NO locking mechanism — there is nothing preventing two engineers from running `terraform apply` simultaneously, and concurrent applies can produce corrupted state or conflicting resource changes. Remote backends implement locking differently by backend: S3 uses a DynamoDB table for lock records; HCP Terraform (formerly Terraform Cloud) uses its own internal locking; Azure Blob Storage uses blob leases; GCS uses object versioning and generation conditions. When a remote lock is acquired, any other `terraform plan` or `terraform apply` will fail with a lock error until the first operation completes (or the lock is force-released). Option A is false — local state has no concurrent-detection mechanism. Option B is false — locking is NOT a feature of the local state format. Option D is false — S3 + DynamoDB locking is available to any Terraform user at no extra cost beyond standard AWS pricing.

---

### Question 5

**Difficulty:** Medium
**Answer Type:** one
**Topic:** Provider source address format — which statement is FALSE?

Which of the following statements about Terraform provider source addresses is FALSE?

A) The fully qualified provider source address format is `<hostname>/<namespace>/<type>` — when the hostname is omitted (short form like `"hashicorp/aws"`), Terraform defaults to `registry.terraform.io`
B) The local name used in a `required_providers` block (e.g., `aws` in `aws = { source = "hashicorp/aws" }`) must always exactly match the provider type in the source address — for example, the AWS provider can only be referenced as `aws` anywhere in the configuration
C) A Terraform configuration can declare multiple providers from different namespaces — for example, the official `hashicorp/aws` and a community provider `myorg/customprovider` can both be declared in the same `required_providers` block
D) Provider source addresses pointing to `registry.terraform.io` are resolved from the public Terraform Provider Registry — providers on this registry include Official, Partner, and Community tiers

**Answer:** B

**Explanation:** Option B is FALSE. The LOCAL NAME used in the `required_providers` block is an arbitrary label chosen by the engineer — it does NOT need to match the provider type in the source address. The local name is simply a reference key used within that Terraform configuration. For example, you could write `myaws = { source = "hashicorp/aws" }` and then use `provider "myaws" {}` and `provider = myaws.alias_name` throughout the configuration. The local name is distinct from the provider type in the source address. This flexibility exists to handle cases where two different providers might have the same type name (e.g., two DNS providers both named `dns` from different namespaces). Options A, C, and D are all true statements about provider source addresses.

---

### Question 6

**Difficulty:** Medium
**Answer Type:** one
**Topic:** `terraform state rm` — which statement is TRUE?

Which of the following statements about `terraform state rm` is TRUE?

A) `terraform state rm` permanently deletes the specified resource from both Terraform state AND from the actual cloud infrastructure — it is equivalent to running `terraform destroy` for a single resource
B) `terraform state rm` removes the specified resource from Terraform's state file while leaving the actual cloud resource running and intact — after removal, Terraform no longer manages that resource and will not include it in future plans
C) `terraform state rm` is the recommended way to rename a resource when you change its label in the `.tf` file — it removes the old name from state and re-applies the new name automatically
D) `terraform state rm` is only available in HCP Terraform — the open-source Terraform CLI does not include state manipulation commands to prevent accidental state corruption

**Answer:** B

**Explanation:** `terraform state rm` performs a state-only operation — it removes the resource's entry from `terraform.tfstate` but takes NO action against the actual cloud infrastructure. The real resource (EC2 instance, S3 bucket, RDS database, etc.) continues to run and exist in the cloud unaffected. The use cases for `terraform state rm` include: (1) stopping Terraform management of a resource without destroying it (e.g., handing it off to another team or tool), (2) removing orphaned state entries that no longer correspond to real resources, and (3) preparing for a state migration. After `state rm`, the resource is effectively invisible to Terraform — a subsequent `terraform plan` will show it as "no action needed" from Terraform's perspective (or if the resource block still exists in configuration, Terraform may propose to recreate it as if it were new). Option A is false — `state rm` does NOT delete the cloud resource. Option C is false — renaming a resource in state is done with `terraform state mv`, not `state rm`. Option D is false — all `terraform state` subcommands are available in the open-source CLI.

---

### Question 7

**Difficulty:** Medium
**Answer Type:** one
**Topic:** Provider tier trust levels — which statement about the Partner tier is FALSE?

Which of the following statements about the **Partner** provider tier in the Terraform Registry is FALSE?

A) Partner providers are maintained by technology companies that have a partnership relationship with HashiCorp and have had their provider reviewed and approved by HashiCorp
B) The Partner tier sits between the Official tier (maintained by HashiCorp) and the Community tier (maintained by individuals with no HashiCorp review) in terms of trust and vetting
C) Partner providers carry the same trust level as Official providers because both tiers require HashiCorp to review and maintain the provider source code directly
D) Examples of Partner providers include providers maintained by cloud vendors, database companies, or SaaS platforms that have partnered with HashiCorp to provide official integrations

**Answer:** C

**Explanation:** Option C is FALSE. The Partner tier does NOT carry the same trust level as the Official tier. The key distinction is: **Official** providers are maintained DIRECTLY by HashiCorp — HashiCorp writes the code, manages releases, and is fully accountable. **Partner** providers are maintained by the TECHNOLOGY PARTNER (the third-party company) — HashiCorp has reviewed and approved the provider and the company has a formal partnership agreement, but HashiCorp does not write or own the code. This means the trust level is lower than Official: the partner company's reliability, security practices, and maintenance commitment determine the quality. Option C falsely claims both tiers require HashiCorp to "review and maintain the provider source code directly" — Partners maintain their own code. Options A, B, and D are accurate descriptions of the Partner tier.

---

### Question 8

**Difficulty:** Medium
**Answer Type:** one
**Topic:** `terraform plan -refresh=false` — which statement is TRUE?

Which of the following statements about `terraform plan -refresh=false` is TRUE?

A) `terraform plan -refresh=false` is the recommended default for all production plans because skipping the refresh step improves plan accuracy — without refresh, Terraform uses the most recent configuration rather than potentially stale cloud API responses
B) `terraform plan -refresh=false` skips the step where Terraform queries live cloud provider APIs to update the known state — the plan is computed using the cached attribute values in the state file rather than fresh API responses; this is faster but may produce inaccurate results if the actual infrastructure has drifted from the recorded state
C) `-refresh=false` and `-refresh-only` are equivalent flags that both skip infrastructure API calls and produce identical plan output
D) `terraform plan -refresh=false` is required when using remote state backends — remote backends cache state and do not support real-time cloud API refreshes during plan

**Answer:** B

**Explanation:** `-refresh=false` disables the state refresh step — the phase where Terraform makes API calls to each cloud provider to check the current, live attributes of managed resources. Without the refresh, Terraform uses whatever attribute values are already recorded in the state file (from the last successful apply or explicit refresh). This has a legitimate use case: in large environments with hundreds of resources, the refresh phase can take minutes because it involves hundreds of API calls. Engineers who KNOW the infrastructure hasn't changed and want faster iteration can use `-refresh=false` to skip this overhead. However, if drift has occurred (a manual console change, an external process modifying a resource), the plan will NOT detect it and may propose incorrect or incomplete changes. Option A is false — `-refresh=false` is not the recommended default; it is a performance optimization with a specific trade-off. Option C is false — `-refresh=false` suppresses refresh in a normal plan/apply cycle; `-refresh-only` is a completely different mode that ONLY performs a refresh and updates state to match current cloud reality (it does NOT make infrastructure changes). Option D is false — remote backends fully support real-time cloud API refreshes during plan.

---

### Question 9

**Difficulty:** Medium
**Answer Type:** many
**Topic:** Three sources of truth in `terraform plan` — which TWO are TRUE?

Which TWO of the following statements about how Terraform computes a plan are TRUE?

A) During `terraform plan`, Terraform consults three sources of information: the desired state (`.tf` configuration files), the known state (`terraform.tfstate` — last recorded resource attributes), and the actual state (live cloud resources queried via API calls) — the plan proposes changes needed to bring actual state into alignment with desired state
B) The `terraform.tfstate` file is the sole source of truth during planning — Terraform never makes live API calls because doing so would be too slow and would risk rate-limiting on large environments
C) If `terraform.tfstate` does not yet exist (first apply of a new configuration), Terraform treats the known state as empty — this means Terraform will propose creating all resources declared in the configuration because no current state exists to compare against
D) Terraform uses the actual live cloud state as its desired state — the `.tf` configuration files are advisory only, and Terraform will not make changes that conflict with what the cloud reports as the current resource attributes

**Answer:** A, C

**Explanation:** **(A)** is TRUE. The three-source model is central to understanding how Terraform plans. Desired state (configuration) represents intent. Known state (tfstate) represents what Terraform last observed. Actual state (API refresh) represents reality. The plan bridges the gap from actual → desired, using known state to understand which resources are already managed and what their previous attributes were. **(C)** is TRUE. On a brand-new configuration with no existing state file, Terraform's known state is empty. Since there is no state to compare against, and assuming the actual cloud state is also empty (no pre-existing matching resources), Terraform proposes creating every resource in the configuration. This is correct and expected behaviour on first apply. **(B)** is FALSE — Terraform absolutely makes live API calls during the refresh phase of planning; the state file alone is not sufficient because actual infrastructure may have drifted from what's recorded. **(D)** is FALSE and inverts the model completely. The `.tf` configuration files ARE the desired state — not advisory. The cloud's current state is what Terraform tries to CHANGE to match the configuration, not the other way around.

---

### Question 10

**Difficulty:** Medium
**Answer Type:** one
**Topic:** `terraform state mv` purpose — which statement is TRUE?

Which of the following statements about `terraform state mv` is TRUE?

A) `terraform state mv` destroys the source resource in the cloud and recreates it under the new address — it is functionally equivalent to removing and re-adding a resource block in the configuration and running `terraform apply`
B) `terraform state mv` renames a resource in the Terraform state file without destroying or recreating the underlying cloud resource — it is the correct way to update state when you rename a resource label in your configuration, preventing Terraform from planning a destroy-and-recreate cycle
C) `terraform state mv` only works with resources that use the `count` meta-argument — it cannot be used to rename resources that use `for_each` or resources without either meta-argument
D) `terraform state mv` is only required when migrating between remote backends — for local renames within the same configuration it is unnecessary because Terraform automatically tracks resource label changes between applies

**Answer:** B

**Explanation:** `terraform state mv` is a surgical state operation that moves a resource's state entry from one address to another WITHOUT touching the underlying cloud infrastructure. The primary use case is exactly as described in option B: when you rename a resource block in your configuration (e.g., from `aws_instance.old_name` to `aws_instance.new_name`), Terraform sees the old resource gone and a new one appearing — and would plan to destroy the old and create the new. Running `terraform state mv aws_instance.old_name aws_instance.new_name` BEFORE the configuration rename reconciles state so Terraform recognises the resource at its new address without any destroy/recreate. Option A is false — `state mv` is a state-only operation; no cloud resources are destroyed or recreated. Option C is false — `state mv` works with any resource regardless of meta-arguments, including simple resources, `count` instances (e.g., `aws_instance.app[0]`), and `for_each` instances (e.g., `aws_instance.app["prod"]`). Option D is false — Terraform does NOT automatically track label changes; without `state mv`, a renamed resource will always be planned as destroy+create.

---

### Question 11

**Difficulty:** Medium
**Answer Type:** one
**Topic:** Provider alias usage — which statement about the default provider is TRUE?

Which of the following statements about Terraform provider aliases is TRUE?

A) When two `provider "aws"` blocks exist (one without an alias and one with `alias = "secondary"`), Terraform distributes resources between the two configurations automatically — resources are allocated in round-robin order to load-balance API calls
B) A provider block without an `alias` argument is the default configuration for that provider type — any resource block of that provider type that does NOT specify a `provider` meta-argument will use this default configuration
C) Once a provider alias is declared, all resource blocks for that provider type MUST explicitly specify which configuration to use via the `provider` meta-argument — the concept of a "default" provider no longer applies when any alias exists
D) Provider aliases are only supported for the official HashiCorp providers (AWS, Azure, GCP) — community and partner providers cannot define aliases

**Answer:** B

**Explanation:** Option B accurately describes the alias model. In Terraform, every provider type has at most one DEFAULT configuration — the `provider` block that has NO `alias` argument. When a resource block of that provider type does not specify a `provider` meta-argument, Terraform automatically uses this default. Aliased configurations are EXPLICITLY opt-in: a resource must declare `provider = aws.secondary` (format: `<local_name>.<alias>`) to use the aliased configuration. This design means you can add aliases without affecting existing resources that already work with the default. A common pattern is: default = primary region (e.g., `us-east-1`), alias = secondary region (e.g., `eu-west-1`); only resources that explicitly need the secondary region reference the alias. Option A is false — there is no round-robin or automatic distribution. Option C is false — the default provider still applies to resources that don't specify a `provider` argument, even when aliases exist. Option D is false — provider aliases are a Terraform Core feature available to ALL provider types regardless of tier.

---

### Question 12

**Difficulty:** Hard
**Answer Type:** one
**Topic:** Four statements about Terraform state — only ONE is TRUE

Four statements about Terraform state are presented below. Which is the ONLY TRUE statement?

A) The `terraform.tfstate` file contains only the resource labels and types declared in the `.tf` configuration — computed attributes such as resource IDs, IP addresses, and ARNs assigned by the cloud provider are not stored in state because they are fetched fresh from the cloud API on every plan
B) Because `sensitive = true` on a variable or output causes Terraform to encrypt the value before writing it to state, engineers can safely store API keys and database passwords in Terraform variables without needing an encrypted backend
C) Manually editing `terraform.tfstate` with a text editor is the officially recommended approach for renaming resources, fixing state corruption, and performing state migrations — it is faster and more precise than using `terraform state` commands
D) The `terraform.tfstate` file stores computed resource attributes (IDs, IP addresses, ARNs, and other values that the cloud provider assigns after resource creation) alongside the configuration-declared attributes — these stored values enable Terraform to compute accurate diffs without querying every resource on every plan, and they are stored in plaintext JSON regardless of any `sensitive` annotations

**Answer:** D

**Explanation:** Option D is the only TRUE statement, and it combines two important exam concepts. First, state stores BOTH configuration-declared attributes AND computed attributes — values the cloud provider generates after resource creation (like an EC2 instance ID `i-0abc123`, a public IP address, an S3 bucket ARN). These computed values are essential for Terraform to track resources across plan/apply cycles and for referencing outputs from one resource as inputs to another. Second, everything in state is in PLAINTEXT JSON — the `sensitive = true` annotation does NOT encrypt state. Option A is false — state absolutely stores computed attributes (IDs, IPs, ARNs, etc.); this is one of the four core purposes of state. Option B is false and dangerous — `sensitive = true` provides only terminal display masking; it offers zero encryption protection in the state file; an encrypted backend is still required for secret safety. Option C is false — HashiCorp explicitly states "Never manually edit state." Manually editing `terraform.tfstate` can corrupt state records, break resource tracking, and cause unpredictable plan behaviour; `terraform state` subcommands (mv, rm, pull, push) are the safe, supported interface.

---

### Question 13

**Difficulty:** Hard
**Answer Type:** many
**Topic:** Which TWO statements about Terraform version constraints are TRUE?

Which TWO of the following statements about Terraform provider version constraints are TRUE?

A) The constraint `version = ">= 5.0, < 6.0"` is functionally equivalent to `version = "~> 5.0"` — both allow any version from `5.0` up to (but not including) `6.0`, and either form is acceptable in `required_providers`
B) The constraint `version = "~> 5.0.0"` allows the AWS provider to be upgraded to version `5.1.0` — the `~>` operator permits minor version increments within the major version declared
C) When multiple version constraints are combined (e.g., `version = ">= 5.0, < 5.20"`), Terraform selects the NEWEST version that satisfies ALL constraints simultaneously — not the minimum version, and not the first constraint alone
D) The `=` exact version constraint (e.g., `version = "= 5.31.0"`) is considered a poor practice because it prevents the provider from ever receiving security patches — if a security fix is released as `5.31.1`, the constraint will block its installation; `~>` with a patch-level lock (e.g., `~> 5.31.0`) is the preferred approach for maximum stability with patch-level updates

**Answer:** A, C

**Explanation:** **(A)** is TRUE. `~> 5.0` is syntactic sugar for `>= 5.0, < 6.0`. Both expressions produce an identical version range — any `5.x.x` version is permitted. Using `~>` is more concise and expresses intent clearly ("stay within major version 5"), but the multi-constraint form is equally valid and sometimes useful for expressing asymmetric ranges (e.g., `>= 5.5, < 5.20` to exclude both very old and very new minor versions). **(C)** is TRUE. When multiple constraints are combined, Terraform evaluates them as a logical AND — the selected version must satisfy ALL constraints. Terraform always resolves to the NEWEST version within the intersection of all constraints (unless a lock file is present, in which case the locked version is used). Selecting the minimum or the first-constraint result would be incorrect. **(B)** is FALSE. `~> 5.0.0` allows ONLY patch updates (`>= 5.0.0, < 5.1.0`). Version `5.1.0` changes the minor component and is outside this range. For minor-version flexibility, `~> 5.0` (two components) is needed. **(D)** is PARTIALLY TRUE but contains a false assertion. Using `= 5.31.0` (exact version) IS considered poor practice for the stated reason — it blocks all future updates including security patches. However, stating that `~> 5.31.0` is the "preferred approach" is misleading — `~> 5.31.0` only allows patch updates within `5.31.x`; most teams use `~> 5.0` for broader minor-version flexibility. The claim is too specific and partially incorrect, making the whole option false.
