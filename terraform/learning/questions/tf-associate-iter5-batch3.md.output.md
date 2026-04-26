# Terraform Associate Exam Questions

---

### Question 1 — `terraform fmt` vs `terraform validate`: What Each Checks

**Difficulty**: Easy
**Answer Type**: one
**Topic**: Contrast between what `fmt` enforces and what `validate` enforces, and what they share in common

**Question**:
Compare `terraform fmt` and `terraform validate`. What does each command check, and what do they have in common?

- A) `terraform fmt` checks for undeclared variables; `terraform validate` checks for inconsistent indentation — both require cloud provider credentials
- B) `terraform fmt` corrects HCL code style and formatting (indentation, alignment, whitespace); `terraform validate` checks syntax correctness, undeclared references, type errors, and invalid argument names — both are fully offline and require no provider credentials or network access
- C) `terraform fmt` validates that resource arguments match the provider schema; `terraform validate` formats the output of `terraform plan` for readability
- D) Both commands are identical in what they check — `validate` is simply the strict mode of `fmt`

---

### Question 2 — `terraform plan` vs `terraform apply`: State File Impact

**Difficulty**: Easy
**Answer Type**: one
**Topic**: Contrast between which command reads state without modifying it and which modifies state

**Question**:
Compare `terraform plan` and `terraform apply` with respect to how each interacts with the Terraform state file. Which statement correctly describes the difference?

- A) `terraform plan` reads and writes the state file; `terraform apply` writes a new state file and archives the old one
- B) `terraform plan` generates and displays an execution plan without modifying the state file; `terraform apply` executes the plan and updates the state file to reflect the changes made
- C) Both commands modify the state file — `plan` updates it with the proposed changes and `apply` confirms them
- D) Neither command modifies the state file — state is only changed by `terraform state mv` and `terraform state rm`

---

### Question 3 — `terraform workspace new` vs `terraform workspace select`

**Difficulty**: Easy
**Answer Type**: one
**Topic**: Contrast between creating a new workspace and selecting an existing one

**Question**:
Compare `terraform workspace new staging` and `terraform workspace select staging`. What is the key functional difference between these two commands?

- A) Both commands are identical — `new` and `select` are aliases for the same operation
- B) `terraform workspace new staging` creates a new workspace named `staging` (it fails if `staging` already exists) and switches to it; `terraform workspace select staging` switches to the existing workspace named `staging` (it fails if `staging` does not yet exist)
- C) `terraform workspace new staging` copies the current workspace's state to `staging`; `terraform workspace select staging` creates an empty new workspace
- D) `terraform workspace new staging` creates the workspace but does not switch to it; `terraform workspace select staging` switches to it without creating it

---

### Question 4 — `terraform apply` with No Saved Plan vs `terraform apply plan.tfplan`

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Contrast between implicit re-planning and deterministic saved-plan execution

**Question**:
An engineer reviews the output of `terraform plan` showing 3 resources to add. They then wait 10 minutes before applying. Compare the two approaches below — what is the key difference in what actually gets applied?

- **Approach A**: Run `terraform apply` (no saved plan) 10 minutes after reviewing the plan
- **Approach B**: Run `terraform plan -out=release.tfplan`, review the output, then run `terraform apply release.tfplan`

- A) Both approaches apply the same changes — Terraform re-uses the plan output from the previous run regardless
- B) In Approach A, Terraform performs a **new implicit plan** at apply time — if the infrastructure changed in the 10-minute gap, the actual changes may differ from what was reviewed; in Approach B, the exact plan that was reviewed is applied with no re-planning, guaranteeing deterministic execution
- C) Approach A is safer because Terraform re-plans to incorporate any recent changes; Approach B may apply a stale plan that is no longer valid
- D) Both approaches result in an interactive prompt — the only difference is file I/O overhead

---

### Question 5 — `terraform init` vs `terraform init -reconfigure`

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Contrast between standard backend init and forced backend reconfiguration

**Question**:
A team changes the backend configuration in their `terraform` block from one S3 bucket to a different S3 bucket. They run `terraform init`. Terraform prompts them to choose between migrating state or continuing without migrating. Compare this behaviour to running `terraform init -reconfigure`. What is the operational difference?

- A) `terraform init -reconfigure` migrates all state from the old backend to the new backend automatically; standard `terraform init` requires manual confirmation
- B) `terraform init -reconfigure` initialises the new backend configuration without migrating any existing state and without prompting — the old backend's state is left in place and the new backend starts empty; standard `terraform init` offers the option to migrate state to the new backend
- C) Both commands produce identical behaviour — `-reconfigure` is simply a flag that suppresses the interactive prompt while still migrating state
- D) `-reconfigure` is only valid for the first `terraform init` run; after a backend exists, only standard `terraform init` can be used

---

### Question 6 — `terraform fmt` (No Flags) vs `terraform fmt -diff`

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Contrast between in-place formatting and diff-only preview

**Question**:
Compare running `terraform fmt` with no flags versus `terraform fmt -diff`. A `.tf` file has inconsistent indentation. What happens to the file in each case?

- A) Both commands modify the file — `-diff` additionally shows the changes that were made
- B) `terraform fmt` (no flags) rewrites the file directly on disk to canonical format; `terraform fmt -diff` displays a unified diff showing what would change **without writing any changes to disk**
- C) `terraform fmt` (no flags) only prints the file names that need formatting; `-diff` both shows and applies the changes
- D) Both commands are read-only — to actually reformat a file you must pipe the diff output back to the file manually

---

### Question 7 — `terraform plan -refresh=false` vs Standard `terraform plan`

**Difficulty**: Medium
**Answer Type**: many
**Topic**: Contrasting two key differences between a refresh-skipping plan and a full live-query plan

**Question**:
Compare `terraform plan` (standard) with `terraform plan -refresh=false`. Which TWO statements correctly describe a difference between the two? (Select two.)

- A) Standard `terraform plan` queries the live provider API to refresh each resource's actual current attributes before computing the diff; `terraform plan -refresh=false` uses the cached state from the last apply without making any API calls
- B) `terraform plan -refresh=false` is more accurate than standard `terraform plan` because it avoids potential API rate-limiting errors
- C) If an out-of-band change was made to a resource in the cloud (e.g., a tag changed via the console), standard `terraform plan` detects this and includes it in the plan diff; `terraform plan -refresh=false` does not detect the drift because it never queries the live API
- D) Both commands always produce identical plan output — the `-refresh=false` flag only affects performance, not the content of the plan

---

### Question 8 — `terraform output` vs `terraform output -json`

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Contrast between human-readable output display and structured JSON output for scripting

**Question**:
Compare `terraform output` (no flags) and `terraform output -json`. A configuration has two outputs: a string `vpc_id` and a list `subnet_ids`. How does the format of each command's response differ, and which is more appropriate for use in a CI script?

- A) Both return identical data — the only difference is that `-json` wraps the output in a JSON array
- B) `terraform output` prints all output values in human-readable format (strings quoted, lists formatted); `terraform output -json` returns a structured JSON object with `sensitive`, `type`, and `value` metadata fields for each output — the JSON format is the appropriate choice for CI scripts and programmatic processing
- C) `terraform output -json` is only valid for outputs declared with `type = "string"` — list outputs require `terraform output` without flags
- D) `terraform output` returns values without quotes for scripting; `-json` adds quotes and type annotations for documentation purposes

---

### Question 9 — `terraform plan -target` vs Full `terraform plan`

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Contrast between a targeted partial plan and a complete plan covering all resources

**Question**:
A configuration manages 30 resources. An engineer is debugging a single resource and runs `terraform plan -target=aws_instance.debug`. Compare this to running a full `terraform plan` with no target. What risk does the targeted approach introduce that the full plan does not?

- A) Targeted plans are more accurate because fewer resources are evaluated — there is no additional risk
- B) Targeted plans take longer because Terraform must first scan all 30 resources before filtering to the target
- C) A targeted plan only evaluates the specified resource and its direct dependencies — it may miss cascading changes to downstream resources that depend on the target, producing an **incomplete view** that does not reflect all the changes a full apply would cause; a full plan shows the complete picture
- D) Targeted plans lock the state file, preventing other engineers from running plans simultaneously

---

### Question 10 — `terraform destroy` (Full) vs `terraform destroy -target`

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Contrast between full environment destruction and targeted single-resource destruction

**Question**:
A production environment has 50 resources. An engineer needs to destroy only one obsolete EC2 instance (`aws_instance.legacy`). Compare running `terraform destroy` (no flags) versus `terraform destroy -target=aws_instance.legacy`. What is the critical difference in scope?

- A) Both commands destroy the same set of resources — `-target` is only valid with `apply`, not `destroy`
- B) `terraform destroy` (no flags) plans to destroy **all 50 resources** managed by the configuration; `terraform destroy -target=aws_instance.legacy` destroys only the targeted resource (and any resources that depend on it) — the other 49 resources are unaffected
- C) `terraform destroy -target` is not recommended because it deletes the entire resource group containing the target
- D) `terraform destroy` (no flags) only destroys resources in the current workspace; `-target` destroys the resource across all workspaces

---

### Question 11 — `~` Symbol vs `-/+` Symbol in Plan Output

**Difficulty**: Medium
**Answer Type**: many
**Topic**: Contrasting two key differences between update-in-place and replacement plan operations

**Question**:
Compare the `~` symbol and the `-/+` symbol in `terraform plan` output. Which TWO statements correctly distinguish these two plan operations? (Select two.)

- A) `~` indicates an **update in-place** — the existing resource object continues to exist and only specific attribute values are changed without destroying and recreating the resource
- B) `-/+` indicates that the resource will be **destroyed and then recreated** — a new resource object is provisioned to replace the old one, and the resource experiences downtime during the transition
- C) Both `~` and `-/+` result in the same final state — they differ only in whether Terraform prompts for confirmation
- D) `~` means the resource is being moved to a different Terraform workspace; `-/+` means it is being moved between providers

---

### Question 12 — `terraform init -migrate-state` vs `terraform init -reconfigure`

**Difficulty**: Hard
**Answer Type**: one
**Topic**: Deep contrast between migrating state to a new backend vs discarding the old backend's state record

**Question**:
A team is changing their Terraform backend from an S3 bucket in `us-east-1` to a new S3 bucket in `eu-west-1`. Their existing state file contains 40 resources. Compare `terraform init -migrate-state` and `terraform init -reconfigure` for this scenario. What is the critical operational difference?

- A) Both flags copy the state to the new backend — `-reconfigure` additionally cleans up the old backend
- B) `-migrate-state` and `-reconfigure` are equivalent; the distinction only matters when changing backend types, not when changing buckets within the same backend type
- C) `terraform init -migrate-state` copies the existing state from the old S3 bucket to the new S3 bucket before switching the active backend — all 40 resource records are preserved and Terraform continues managing them; `terraform init -reconfigure` initialises the new backend without copying any state — the new backend starts empty, and the 40 resources would appear unmanaged on the next plan
- D) `terraform init -reconfigure` is the recommended approach for cross-region state migration because `-migrate-state` only supports same-region moves

---

### Question 13 — `terraform graph` vs `terraform console`

**Difficulty**: Hard
**Answer Type**: one
**Topic**: Contrast between static dependency graph output and interactive expression evaluation

**Question**:
Compare `terraform graph` and `terraform console` as diagnostic and development tools. What does each command help the operator understand, and how do they differ in their interaction model and output?

- A) Both tools are interactive REPLs — `terraform graph` explores the dependency graph interactively; `terraform console` explores resource attributes interactively
- B) `terraform graph` is used to test HCL expressions before committing them; `terraform console` generates a visual map of resource dependencies
- C) `terraform graph` produces a **one-shot DOT-format text output** of the static resource dependency graph — it shows how resources depend on each other and what ordering Terraform will use for operations; it is non-interactive and requires Graphviz to render visually. `terraform console` is an **interactive REPL** that evaluates HCL expressions and built-in functions against the current configuration and state — it is used to test and debug expressions, functions, and variable references before embedding them in configuration files
- D) Both commands are deprecated — `terraform graph` was replaced by `terraform state list` and `terraform console` was replaced by `terraform validate`

## Answer Key

| Q# | Answer(s) | Explanation | Source | Difficulty |
|----|-----------|-----------:|--------|------------|
| 1 | B | N/A | Contrast between what `fmt` enforces and what `validate` enforces, and what they share in common | Easy |
| 2 | B | N/A | Contrast between which command reads state without modifying it and which modifies state | Easy |
| 3 | B | N/A | Contrast between creating a new workspace and selecting an existing one | Easy |
| 4 | B | N/A | Contrast between implicit re-planning and deterministic saved-plan execution | Medium |
| 5 | B | N/A | Contrast between standard backend init and forced backend reconfiguration | Medium |
| 6 | B | N/A | Contrast between in-place formatting and diff-only preview | Medium |
| 7 | A, C | N/A | Contrasting two key differences between a refresh-skipping plan and a full live-query plan | Medium |
| 8 | B | N/A | Contrast between human-readable output display and structured JSON output for scripting | Medium |
| 9 | C | N/A | Contrast between a targeted partial plan and a complete plan covering all resources | Medium |
| 10 | B | N/A | Contrast between full environment destruction and targeted single-resource destruction | Medium |
| 11 | A, B | N/A | Contrasting two key differences between update-in-place and replacement plan operations | Medium |
| 12 | C | N/A | Deep contrast between migrating state to a new backend vs discarding the old backend's state record | Hard |
| 13 | C | N/A | Contrast between static dependency graph output and interactive expression evaluation | Hard |
