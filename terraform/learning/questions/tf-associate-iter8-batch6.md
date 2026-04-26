---
iteration: 8
batch: 6
style: "Ordering / sequencing"
style_note: >
  Every question presents a workflow, lifecycle, or list of steps and asks the
  candidate to identify the correct order, which step comes first or last, or
  which option correctly sequences a process.
topics:
  - Custom Conditions & Sensitive Data (Objective 4 — prompt10)
sources:
  - prompt10-custom-conditions-sensitive-data.md
question_count: 13
difficulty_split: "3 Easy / 8 Medium / 2 Hard"
answer_type_split: "10 one / 3 many"
---

# Terraform Associate (004) — Iteration 8 · Batch 6
## Custom Conditions & Sensitive Data · Ordering / Sequencing

---

### Question 1

**Difficulty:** Easy
**Answer Type:** one
**Topic:** Full sequence of when each condition mechanism fires across the Terraform workflow

An engineer adds all three Terraform condition mechanisms to a configuration: a `validation` block on a variable, a `precondition` and `postcondition` on a resource's `lifecycle`, and a top-level `check` block. Which of the following correctly sequences when each mechanism fires during a single `terraform apply` run?

A) check assertion → validation block → precondition → resource change → postcondition
B) precondition → validation block → resource change → postcondition → check assertion
C) validation block (before plan) → precondition (before the resource is changed, during apply) → resource change → postcondition (after the resource is changed, during apply) → check assertion (after all resource operations complete)
D) All four mechanisms run simultaneously at the start of `terraform apply` — Terraform batches condition evaluation before any infrastructure changes occur

**Answer:** C

**Explanation:** Each condition mechanism fires at a distinct phase of the Terraform workflow. **(1) validation block** — runs first, during input variable processing, before `terraform plan` generates any execution plan. A failure here means no plan is ever created. **(2) precondition** — runs during `terraform apply`, immediately before Terraform modifies the specific resource that declares it. Other resources may already have been changed by this point; the precondition blocks only the one resource it belongs to. **(3) Resource change** — Terraform makes the API call to create, update, or destroy the resource. **(4) postcondition** — runs immediately after the resource change completes and Terraform has read back the resulting attributes. `self` references the resource in its new post-change state. **(5) check assertion** — runs at the end of every `plan` and `apply`, after all resource operations have completed. A failed check assertion is a warning only — it does not affect the exit status of the apply. This ordering means `validation` catches bad inputs earliest, while `check` provides the latest health snapshot.

---

### Question 2

**Difficulty:** Easy
**Answer Type:** one
**Topic:** Resource state when a `postcondition` fails — the resource HAS already been modified

An engineer adds a `postcondition` to an `aws_instance` resource that asserts `self.public_ip != null`. During `terraform apply`, the instance is created without a public IP and the postcondition fires. Which of the following correctly describes the state of the resource at the point the postcondition fails?

A) The instance has NOT been created — a failing `postcondition` works like a `precondition` and blocks the API call; no cloud resource was provisioned
B) The instance HAS already been created in AWS — the API call completed and the instance exists with its actual attributes before the `postcondition` evaluates; the apply exits non-zero, but the instance is running and may need manual cleanup
C) The instance was created and then automatically destroyed when the postcondition failed — Terraform rolls back the resource change
D) The instance is in a `tainted` state — it exists in AWS but is flagged in state as needing replacement on the next apply

**Answer:** B

**Explanation:** A `postcondition` is evaluated AFTER the resource change has already happened. The sequence is: (1) API call to create the instance is made and completes; (2) Terraform reads back the instance attributes (including `public_ip`); (3) `postcondition` evaluates `self.public_ip != null` using those real attributes. If the condition is false, Terraform displays the `error_message` and exits with a non-zero status — but the instance already exists in AWS. Terraform does NOT roll back or auto-destroy the resource. This is a critical operational fact: a failing `postcondition` means the resource was created (or updated) but does not meet requirements. The engineer must investigate and either fix the configuration or manually reconcile the real-world state. This behavior contrasts with `precondition`, which fails BEFORE the API call, guaranteeing the resource is never touched.

---

### Question 3

**Difficulty:** Easy
**Answer Type:** many
**Topic:** Two correct ordering/timing facts about `validation` blocks

Which TWO of the following correctly describe sequencing facts about variable `validation` blocks?

A) A `validation` block fires BEFORE `terraform plan` evaluates any infrastructure — it runs during input variable processing; if the condition returns `false`, Terraform halts immediately and no plan is ever generated
B) A `validation` block fires AFTER `terraform plan` has completed, when the engineer is reviewing the plan output — it provides a final check before the engineer approves the apply
C) A `validation` block always fires BEFORE any `precondition` in the same configuration — validation is the earliest condition mechanism in the Terraform workflow because it runs before planning begins, while preconditions run during apply
D) A `validation` block fires AFTER `precondition` blocks because preconditions run at the planning phase while validation runs at the apply phase

**Answer:** A, C

**Explanation:** **(A)** Variable `validation` blocks run during input variable processing, which is the very first evaluation stage in the Terraform workflow — before `terraform plan` builds a dependency graph or evaluates any resource configurations. A failed validation condition halts the run immediately with the configured `error_message` and zero planning has occurred. **(C)** Because `validation` runs before planning and `precondition` runs during apply, `validation` always fires first in any run that reaches the apply stage. In a typical pipeline: `terraform plan` (validation runs here) → engineer reviews plan → `terraform apply` (preconditions run here before each resource change). This makes `validation` the earliest opportunity to catch a problem in the entire workflow. Option B is false — validation is not an apply-time prompt to the engineer. Option D reverses the actual order.

---

### Question 4

**Difficulty:** Medium
**Answer Type:** one
**Topic:** `check` block sequence — scoped data source evaluated BEFORE the assert condition

A `check` block contains a scoped `data "http"` source and an `assert` block:

```hcl
check "endpoint_health" {
  data "http" "probe" {
    url = "https://${aws_lb.web.dns_name}/health"
  }

  assert {
    condition     = data.http.probe.status_code == 200
    error_message = "Health returned ${data.http.probe.status_code}, expected 200."
  }
}
```

Which of the following correctly sequences the steps Terraform takes when evaluating this `check` block?

A) (1) Evaluate the `assert` condition first using a cached response → (2) If the condition is false, fetch the URL to confirm → (3) Display the warning if still false
B) (1) Evaluate the `assert` condition immediately using the current value of `aws_lb.web.dns_name` → (2) Fetch the URL only if the condition fails, to gather diagnostic data
C) (1) Wait for all resource apply operations to complete → (2) Resolve `aws_lb.web.dns_name` from state → (3) Construct the URL and execute the HTTP request (scoped data source evaluation) → (4) Read `data.http.probe.status_code` → (5) Evaluate the `assert` condition using the status code → (6) If `false`, emit a warning; the apply still exits successfully
D) The scoped `data` source and the `assert` condition are evaluated simultaneously — Terraform resolves both in a single pass and does not guarantee which is evaluated first

**Answer:** C

**Explanation:** When a `check` block contains a scoped `data` source, Terraform follows a strict sequence: **(1)** All regular resource apply operations complete first — the `check` block runs after all planned resource changes. **(2)** `aws_lb.web.dns_name` is resolved from state (the load balancer was created in step 1). **(3)** The scoped `data "http" "probe"` source is evaluated — Terraform constructs the URL and performs the HTTP GET request. The scoped data source EXISTS only within the `check` block and cannot be referenced anywhere else in the configuration. **(4)** The response attributes (including `status_code`) are now populated. **(5)** The `assert` condition `data.http.probe.status_code == 200` is evaluated — it can only run AFTER the data source has fetched the response. **(6)** If false, a warning is displayed; the apply exits successfully. The data source MUST be evaluated before the `assert` condition — this ordering is guaranteed because the `assert` references the data source's output attribute.

---

### Question 5

**Difficulty:** Medium
**Answer Type:** one
**Topic:** `terraform validate` does NOT trigger variable validation blocks or any condition mechanism

An engineer has a variable with a `validation` block that prevents the empty string, and a resource with a `precondition`. They run `terraform validate` with a `terraform.tfvars` that assigns an empty string to the variable. Which of the following correctly sequences what `terraform validate` does and does NOT do?

A) `terraform validate` evaluates variable `validation` blocks and preconditions — it is a comprehensive static check that catches all configuration errors before plan or apply
B) `terraform validate` only runs during `terraform plan` — running it as a standalone command is equivalent to running `terraform plan -target=none` and will trigger validation blocks
C) `terraform validate` checks HCL syntax for well-formedness and verifies that resource configurations conform to provider schemas — it does NOT evaluate variable `validation` block conditions, `precondition`/`postcondition` expressions, or `check` block assertions; the empty string passes `terraform validate` without error; the validation failure only surfaces when `terraform plan` or `terraform apply` processes the variable value
D) `terraform validate` triggers all three condition mechanisms in a dry-run mode — conditions are evaluated but failures are shown as warnings rather than errors

**Answer:** C

**Explanation:** `terraform validate` performs two checks: (1) it parses all `.tf` files and verifies that the HCL syntax is well-formed; (2) it validates that resource configurations (argument names, types, required arguments) match the schemas declared by the providers that have been initialized. Crucially, `terraform validate` does NOT evaluate any dynamic condition expressions: not variable `validation` block conditions, not `precondition`/`postcondition` conditions, and not `check` block assertions. This means an empty string for a validated variable passes `terraform validate` completely silently — the validation failure only fires during input variable processing, which occurs at `terraform plan` time. This sequencing is important for CI pipelines: `terraform validate` is a fast syntactic/schema check that runs without needing variable values, while `terraform plan` is needed to catch validation failures. Both are typically run in sequence in a CI pipeline.

---

### Question 6

**Difficulty:** Medium
**Answer Type:** one
**Topic:** Sensitive output propagation — child module marks sensitive, parent inherits automatically

A child module `./network` declares an output:

```hcl
output "internal_api_key" {
  value     = aws_secretsmanager_secret_version.api_key.secret_string
  sensitive = true
}
```

The root module references this output in a resource argument:

```hcl
resource "aws_lambda_function" "app" {
  environment {
    variables = {
      API_KEY = module.network.internal_api_key
    }
  }
}
```

Which of the following correctly sequences how the `sensitive = true` marking propagates through this configuration?

A) The root module must explicitly re-declare `sensitive = true` on its own output to suppress the value — sensitivity is NOT automatically inherited from child module outputs; without re-declaration, the value appears in terminal output in the root module
B) (1) The child module marks `internal_api_key` as sensitive → (2) When the root module references `module.network.internal_api_key`, Terraform automatically treats that reference as a sensitive value → (3) Any resource argument that receives this value is automatically treated as sensitive in plan output — `(sensitive value)` appears wherever the value would be shown; no re-declaration of `sensitive = true` is needed in the root module
C) Sensitive outputs from child modules are automatically decrypted and re-encrypted at module boundaries — the root module sees the plaintext value but it is re-masked before being written to state
D) Sensitivity propagation only works when both the child output AND the root module resource argument are explicitly marked `sensitive = true` — a partial declaration causes Terraform to error during plan

**Answer:** B

**Explanation:** Terraform's sensitivity tracking is automatic and propagates through references. The sequence is: **(1)** The child module marks `internal_api_key` with `sensitive = true` — this tells Terraform to treat this value as sensitive throughout. **(2)** When the root module evaluates `module.network.internal_api_key`, Terraform recognizes the source as a sensitive output and automatically marks the resulting value as sensitive in its expression graph — no re-declaration needed. **(3)** The sensitive value flows into the `API_KEY` environment variable — in plan output, Terraform shows `(sensitive value)` for that argument rather than the actual string. This automatic propagation ensures that once a value is marked sensitive at any point in the reference chain, it remains masked in terminal output everywhere it flows. The critical caveat applies throughout: `sensitive = true` is a display-level control — the value is still stored in plaintext in `terraform.tfstate`.

---

### Question 7

**Difficulty:** Medium
**Answer Type:** one
**Topic:** Vault dynamic secrets — 3-step sequence to use credentials without hardcoding

An engineer wants to use database credentials managed by HashiCorp Vault without hardcoding them in `.tf` files or storing long-lived secrets in state. Which of the following correctly sequences the three steps required to use the Vault provider for this pattern?

A) (1) Hardcode the Vault token in the provider block → (2) Store a copy of the credentials in `terraform.tfvars` as a fallback → (3) Reference the hardcoded value in the resource
B) (1) Declare the `vault` provider with the Vault server address and authentication method → (2) Declare a `data "vault_generic_secret"` (or equivalent) source that reads the desired secret path from Vault → (3) Reference the data source attributes (e.g., `data.vault_generic_secret.db_creds.data["password"]`) directly in the resource block — credentials are fetched from Vault at plan/apply time and never stored in `.tf` configuration files
C) (1) Export credentials as environment variables → (2) Read them in Terraform using `var.` references → (3) Pass them to resources — the Vault provider is not required for this pattern
D) (1) Run `vault kv get` in a shell script to extract credentials → (2) Write the output to a `.tfvars` file → (3) Run `terraform apply -var-file=credentials.tfvars` — this is the recommended Vault integration sequence

**Answer:** B

**Explanation:** The Vault provider pattern for dynamic secrets follows three steps: **(1)** Declare `provider "vault"` with the server address and authentication configuration (token, AppRole, IAM, etc.) — Terraform authenticates to Vault when the provider is initialized. **(2)** Declare a `data "vault_generic_secret"` (or more specific type like `data "vault_aws_access_credentials"`) that specifies the Vault secret path — this data source fetches the secret from Vault during `terraform plan` and `terraform apply`. **(3)** Reference the data source attributes directly in resource blocks: `data.vault_generic_secret.db_creds.data["username"]` — the actual secret string flows from Vault through the data source to the resource without ever being written into a `.tf` file. The key benefit of this sequence: credentials are never hardcoded in source-controlled configuration files. Option D describes a dangerously insecure anti-pattern — writing credentials to a `.tfvars` file risks committing them to source control and creates a long-lived plaintext file on disk.

---

### Question 8

**Difficulty:** Medium
**Answer Type:** one
**Topic:** Precondition failure — resource UNCHANGED because the change never occurred

A resource has a `precondition` that checks whether a referenced AMI is `x86_64` architecture:

```hcl
resource "aws_instance" "web" {
  ami           = data.aws_ami.ubuntu.id
  instance_type = var.instance_type

  lifecycle {
    precondition {
      condition     = data.aws_ami.ubuntu.architecture == "x86_64"
      error_message = "The AMI must be x86_64 architecture."
    }
  }
}
```

During `terraform apply`, `data.aws_ami.ubuntu.architecture` resolves to `"arm64"` and the precondition fails. Which of the following correctly describes the sequence up to and including the failure, and what the resource state is after the failure?

A) Terraform attempts to create the instance first, reads the architecture from the running instance, then fails — the instance was provisioned but is now in a `tainted` state
B) Terraform evaluates the `precondition` BEFORE making any API call to AWS for this resource — the instance is NEVER created; the apply exits non-zero but `aws_instance.web` remains in whatever state it was in before the apply (not created if it did not exist; unchanged if it already existed)
C) Terraform fails during `terraform plan` when the `precondition` expression is evaluated — the failure occurs before apply begins
D) The precondition halts all resource processing in the entire apply — all previously planned changes are rolled back when a precondition fails

**Answer:** B

**Explanation:** The `precondition` sequence is: **(1)** During `terraform plan`, Terraform identifies that `aws_instance.web` needs to be created or updated. **(2)** `data.aws_ami.ubuntu` is evaluated during plan and its attributes are available. **(3)** At `terraform apply` time, just before Terraform would make the API call to create/update `aws_instance.web`, the `precondition` is evaluated. In this case, `data.aws_ami.ubuntu.architecture == "x86_64"` returns `false` — the condition fails. **(4)** Terraform immediately halts the operation for THIS resource, displays the `error_message`, and exits with a non-zero status. The AWS API call for this instance was NEVER made — the resource is in exactly the same state as before the apply. This makes `precondition` safe for catching bad prerequisites: it guarantees the resource is not touched when conditions aren't met. Note: resources that were already applied earlier in the same apply run (and succeeded) are NOT rolled back — Terraform does not do transactional rollback of already-completed changes.

---

### Question 9

**Difficulty:** Medium
**Answer Type:** many
**Topic:** Two correct ordering contrasts — what validation can reference vs what precondition can reference, and why

Which TWO of the following correctly describe ordering-based constraints on what a `validation` block versus a `precondition` can reference?

A) A `validation` block's `condition` can ONLY reference `var.<variable_name>` — it cannot reference `local.*`, `data.*`, or other resources — because it runs BEFORE `terraform plan`, when no resources, data sources, or locals have been evaluated; referencing anything other than the variable itself would fail because those values do not yet exist
B) A `validation` block's `condition` can reference any value in the same module — locals, data sources, and other variables are all available — because validation runs simultaneously with planning
C) A `precondition` block's `condition` CAN reference data source attributes, other resource attributes, and module outputs — because it runs DURING `terraform apply`, when data sources have already been read and other resources in the dependency graph may already be in a known state; data sources in particular are evaluated during the planning phase, making their attributes available to precondition conditions
D) A `precondition` block's `condition` is as restricted as a `validation` block — it can only reference `var.*` and `local.*` values; references to data sources in a precondition cause a configuration error

**Answer:** A, C

**Explanation:** The difference in reference scope between `validation` and `precondition` is directly caused by WHEN each mechanism runs in the workflow. **(A)** `validation` runs during input variable processing — before `terraform plan` builds a dependency graph or evaluates any data sources, locals, or resources. Only the variable being validated has a value at that point. Attempting to reference `local.*`, `data.*`, or another `var.*` (other than the variable itself) in a validation condition results in a configuration error. **(C)** `precondition` runs during `terraform apply`, after the planning phase has completed. By apply time, all data sources that don't depend on unknown values have been read, and other resources may already exist in state. A precondition can reference `data.aws_ami.ubuntu.architecture` or `aws_security_group.main.id` because those values are known when the precondition evaluates. This wider reference scope is what makes `precondition` suitable for complex cross-resource assertions that `validation` simply cannot express. Option B is false — locals and data sources are not available to validation. Option D is false — preconditions explicitly support cross-resource references.

---

### Question 10

**Difficulty:** Medium
**Answer Type:** one
**Topic:** `check` block runs on EVERY plan AND apply — unlike preconditions which only fire when a resource changes

An engineer configures a `check` block to monitor their load balancer health endpoint. They run `terraform plan` when no resource changes are planned (a clean plan showing "No changes. Infrastructure is up-to-date."). Which of the following correctly describes whether the `check` block runs and in what sequence?

A) The `check` block does NOT run when no resource changes are planned — it only fires when at least one resource in the configuration has a planned change, similar to how preconditions only fire for resources being changed
B) The `check` block runs ONLY during `terraform apply`, not during `terraform plan` — health monitoring assertions are only meaningful after infrastructure has been deployed
C) The `check` block runs on EVERY `terraform plan` AND every `terraform apply`, including clean plans with no changes — this is a key design distinction from `precondition`/`postcondition`, which only fire when their specific resource is being created, updated, or destroyed; even a no-change plan evaluates all check assertions and reports warnings for any that fail
D) The `check` block only runs when explicitly triggered with `terraform check` — it is not automatically evaluated during plan or apply

**Answer:** C

**Explanation:** The `check` block was designed as a **continuous infrastructure health monitor** — it runs on every `terraform plan` and every `terraform apply`, regardless of whether any resource changes are planned. Even a completely clean plan (zero changes) evaluates all `check` blocks. This is fundamentally different from `precondition` and `postcondition`, which are tied to specific resource lifecycle events and only fire when that particular resource is being modified. The sequential difference: **precondition/postcondition** — run only when their resource is in the change set → if `aws_instance.web` has no planned change, its `precondition` and `postcondition` are skipped; **check** — runs unconditionally on every invocation → the load balancer health is asserted on every plan, providing ongoing visibility even between deployments. This continuous evaluation is what makes `check` useful for monitoring infrastructure drift and health over time, not just at creation time. There is no `terraform check` command — Option D describes a nonexistent command.

---

### Question 11

**Difficulty:** Medium
**Answer Type:** one
**Topic:** Multiple validation blocks on one variable — all evaluated vs first-failure-stops

A variable has THREE `validation` blocks. An engineer passes a value that fails all three conditions. Which of the following correctly describes the sequence in which Terraform evaluates the validation blocks and how many error messages are reported?

A) Terraform evaluates ALL three `validation` blocks independently and reports ALL failures at once — the engineer sees all three `error_message` strings in the output, giving them complete information about every violated constraint in a single run
B) Terraform evaluates the validation blocks in declaration order, stops at the FIRST failure, and reports only the first `error_message` — subsequent validation blocks are skipped; the engineer must fix and re-run to discover additional failures
C) Terraform evaluates all `validation` blocks in parallel and reports only the last failure (highest priority wins)
D) Multiple `validation` blocks on a single variable are not supported — Terraform returns a configuration error if more than one `validation` block is declared for the same variable

**Answer:** B

**Explanation:** When a variable has multiple `validation` blocks, Terraform evaluates them in the order they are declared in the configuration, and stops at the FIRST block whose condition returns `false`. Only the `error_message` from the first failing block is displayed. Subsequent validation blocks are not evaluated. This "fail-fast, first-error" behavior means that if a value violates multiple constraints, the engineer learns about only the first violation per run — they must fix it and re-run to discover whether additional constraints are also violated. This is different from how static analysis tools might work (reporting all issues at once). The practical implication is that validation blocks should be ordered from most-fundamental to most-specific — check type/existence first (though type is handled by the `type` constraint), then range/format, then complex business rules. Option D is false — multiple `validation` blocks per variable are fully supported and documented in the Terraform language reference.

---

### Question 12

**Difficulty:** Hard
**Answer Type:** one
**Topic:** Complete 5-step apply sequence for a resource that has both a precondition and a postcondition

An `aws_instance` resource declares both a `precondition` and a `postcondition` inside its `lifecycle` block. The precondition checks that the referenced AMI architecture matches the instance type family. The postcondition checks that `self.public_ip != null`. Which of the following correctly sequences ALL five steps Terraform takes when applying a change to this resource?

A) (1) API call to create/update instance → (2) precondition evaluated → (3) postcondition evaluated → (4) Read back attributes → (5) Write state
B) (1) Precondition evaluated → (2) If passes: API call to create/update instance → (3) Terraform reads back the resulting resource attributes from the API response → (4) Postcondition evaluated using `self` = read-back attributes → (5) If postcondition passes: write the new resource state; if postcondition fails: apply exits non-zero (instance exists in cloud, state update may not reflect the postcondition error)
C) (1) Postcondition evaluated with previous `self` attributes → (2) API call → (3) Precondition evaluated → (4) Read-back → (5) State write
D) (1) Precondition evaluated → (2) Postcondition evaluated → (3) API call → (4) Read-back → (5) State write; both conditions are evaluated BEFORE the API call to maximize safety

**Answer:** B

**Explanation:** The correct 5-step sequence for a resource with both conditions is: **(1) Precondition** — Terraform evaluates the `precondition` condition BEFORE any API call. If false: apply exits non-zero, resource is untouched. If true: proceed. **(2) API call** — Terraform calls the provider API to create, update, or destroy the resource. The cloud resource now exists in its new state. **(3) Read-back** — Terraform reads back the resource attributes from the API response. For a created instance, this populates `id`, `public_ip`, `private_ip`, etc. **(4) Postcondition** — Terraform evaluates the `postcondition` condition using `self`, where `self` references the just-read-back attributes. If false: apply exits non-zero and the `error_message` is displayed — but the resource WAS created in step 2. If true: proceed. **(5) State write** — The new resource state is written to the state file. Option D is tempting but wrong — postconditions are explicitly designed to run AFTER the change so they can reference `self`'s new attributes. Evaluating them before the API call would make `self` unavailable and the postcondition meaningless.

---

### Question 13

**Difficulty:** Hard
**Answer Type:** many
**Topic:** Two correct sequencing facts distinguishing a `check` block's scoped data source from a top-level data source

Which TWO of the following correctly describe sequencing differences between a data source declared INSIDE a `check` block (scoped data source) and a data source declared at the top level of the module?

A) A scoped data source inside a `check` block is evaluated AFTER all regular resource apply operations complete — it runs as part of the check block evaluation phase which is the last thing to happen in a plan/apply; a top-level data source is typically evaluated DURING the planning phase (before apply) when its inputs are known, making the scoped data source always sequentially later in the workflow than a comparable top-level data source
B) A scoped data source inside a `check` block is evaluated BEFORE all resource operations begin — the check block runs first so it can determine health before any changes are made; a top-level data source runs after apply completes
C) A scoped data source inside a `check` block can be referenced by other resources in the same module — its results are visible to the full module scope; a top-level data source is restricted to use within the `check` block only
D) A scoped data source inside a `check` block is evaluated ONLY as part of its parent `check` block — its result CANNOT be referenced by any resource, local, or output outside the check block; a top-level data source CAN be referenced anywhere in the module; this scoping rule means the two types have completely different visibility and lifetime within the module evaluation sequence

**Answer:** A, D

**Explanation:** **(A)** Top-level data sources are evaluated during the **planning phase** when their inputs are known (i.e., not dependent on apply-time computed values) — they are "read" before any resource changes happen. Scoped data sources inside `check` blocks are evaluated as part of the `check` block evaluation, which runs at the END of every `plan` and `apply` (after all resource operations complete). This sequential difference is significant: a scoped data source that reads an HTTP endpoint is evaluated AFTER the load balancer has been created, not before, guaranteeing the endpoint is available. **(D)** A scoped data source's result is visible ONLY within its parent `check` block — it cannot be referenced from resources, locals, outputs, or any other block outside the check block. This is by design: the scoped data source exists solely to supply data to the `assert` conditions within the same check block. A top-level data source, by contrast, can be referenced anywhere within the module scope — resources, locals, outputs, and even other data sources can depend on it. Option B reverses the actual ordering. Option C incorrectly inverts the visibility rules.
