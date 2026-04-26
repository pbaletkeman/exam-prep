# Terraform Associate Exam Questions

---

### Question 1

**Difficulty:** Easy
**Answer Type:** one
**Topic:** Multiple `validation` blocks per variable — which statement is TRUE?

Which of the following statements about the number of `validation` blocks allowed on a single variable declaration is TRUE?

A) A variable declaration can contain AT MOST one `validation` block — to check multiple conditions, the engineer must combine them into a single boolean expression using `&&` within one block
B) Multiple `validation` blocks can be declared on the same variable — each block's `condition` is evaluated independently; if any block's condition returns `false`, that block's `error_message` is displayed and the run halts; all conditions must pass for the variable to be accepted
C) Multiple `validation` blocks on a variable are valid HCL syntax but Terraform only evaluates the LAST `validation` block and silently ignores all earlier ones
D) Multiple `validation` blocks are only permitted on variables of type `string` — `number` and `bool` variables are restricted to a single `validation` block

---

### Question 2

**Difficulty:** Easy
**Answer Type:** one
**Topic:** `self` keyword in `precondition` — which statement is FALSE?

Which of the following statements about using the `self` keyword inside a `precondition` block is FALSE?

A) Inside a `postcondition` block, `self` references the resource's attributes as they exist AFTER the resource has been created or updated — this is the primary use of `self` in lifecycle conditions
B) `self` is a valid and commonly used keyword inside `precondition` blocks — it references the resource's CURRENT state before the planned change is applied, allowing the engineer to validate the resource's existing attributes
C) Inside a `precondition` block, `self` is NOT available — a `precondition` runs BEFORE the resource is modified, so there is no "new" state for `self` to reference; `precondition` conditions must reference other data sources, variables, or resources rather than `self`
D) A `precondition` that needs to assert something about the resource's planned instance type should reference `var.instance_type` or `data.something.attribute` — not `self`, which is undefined in `precondition` scope

---

### Question 3

**Difficulty:** Easy
**Answer Type:** many
**Topic:** `sensitive = true` on output blocks — which TWO statements are TRUE?

Which TWO of the following statements about setting `sensitive = true` on an output block are TRUE?

A) When `sensitive = true` is set on an output, the value is encrypted at rest in `terraform.tfstate` — this is the primary reason to mark outputs as sensitive, because it protects the data if the state file is ever read by an unauthorized party
B) When a child module declares an output with `sensitive = true`, the parent module that references that output via `module.name.output_name` automatically treats the value as sensitive — the sensitivity propagates through module composition without requiring the parent to redeclare it
C) Marking an output `sensitive = true` suppresses the value in `terraform apply` terminal output and in the default `terraform output` listing — the actual value is replaced with `(sensitive value)` in those contexts
D) Sensitive outputs can never be retrieved in plaintext — once `sensitive = true` is set, the value is permanently opaque and cannot be accessed by any means, including scripts or downstream configurations

---

### Question 4

**Difficulty:** Medium
**Answer Type:** one
**Topic:** `check` block scoped `data` source — which statement is TRUE?

Which of the following statements about the optional `data` source block inside a `check` block is TRUE?

A) The `data` source declared inside a `check` block is identical in behaviour to a top-level `data` source — it is added to the resource dependency graph and other resources can reference its output using the standard `data.<type>.<name>.<attribute>` syntax
B) The `data` source inside a `check` block is **scoped to the `check` block** — it exists only within the context of that check's assertions and is NOT accessible from outside the `check` block via the standard `data.*` reference syntax; because it is outside the main dependency graph, a failure to read it does not fail the apply
C) The `data` source inside a `check` block is only evaluated during `terraform apply` — it is skipped during `terraform plan` to avoid making network calls before infrastructure is deployed
D) Only a single type of `data` source is allowed inside a `check` block — the `http` data source from the `hashicorp/http` provider; other provider data sources cannot be used as scoped check data sources

---

### Question 5

**Difficulty:** Medium
**Answer Type:** one
**Topic:** Outputting a sensitive variable without marking the output sensitive — which statement is TRUE?

Which of the following statements about referencing a `sensitive = true` variable in an output block WITHOUT setting `sensitive = true` on the output is TRUE?

A) Terraform automatically propagates the sensitivity from the variable to the output — if the output's `value` references a sensitive variable, Terraform silently marks the output sensitive without requiring any explicit declaration on the output block
B) Terraform displays a warning about the potential exposure but proceeds with the apply — the sensitive value appears in plaintext in the output
C) Terraform raises an **error** at plan time if an output's `value` references a sensitive variable and the output block does not declare `sensitive = true` — the engineer must explicitly acknowledge the sensitive nature of the data by adding `sensitive = true` to the output block
D) The output is simply omitted from `terraform output` listings when it references a sensitive variable without being marked sensitive — the value is silently suppressed with no error

---

### Question 6

**Difficulty:** Medium
**Answer Type:** one
**Topic:** `precondition` and `postcondition` on data sources — which statement is TRUE?

Which of the following statements about using `precondition` and `postcondition` blocks with data sources is TRUE?

A) `precondition` and `postcondition` blocks can only be declared inside `resource` blocks — they are not supported on `data` source blocks; attempts to use them with data sources produce a syntax error
B) Only `postcondition` is supported on data source `lifecycle` blocks — `precondition` is not valid on data sources because data sources do not have a pre-change state to evaluate
C) `precondition` and `postcondition` blocks are both valid inside a data source's `lifecycle` block — a data source `postcondition` is commonly used to assert that the fetched data meets expected requirements (e.g., verifying that a looked-up AMI has the correct architecture) before other resources consume it
D) `precondition` and `postcondition` blocks on data sources run at `terraform init` — unlike resource lifecycle conditions which run during plan and apply, data source conditions are validated when providers are initialized

---

### Question 7

**Difficulty:** Medium
**Answer Type:** one
**Topic:** `check` block exit code on assertion failure — which statement is FALSE?

Which of the following statements about the exit code of `terraform apply` when a `check` block assertion fails is FALSE?

A) When a `check` block assertion fails, `terraform apply` exits with code `0` (success) — the failed assertion is reported as a warning in the output but does not change the exit code
B) Because `check` block failures exit with `0`, CI/CD pipelines that rely solely on the `terraform apply` exit code to detect failures will NOT catch a failed `check` assertion — pipelines must parse the Terraform output or use a tool that inspects the check results to detect check assertion failures
C) A failing `check` block assertion causes `terraform apply` to exit with a **non-zero exit code** — this is what distinguishes `check` from `precondition`: both block apply completion, but `check` failures are labelled as "warnings" while `precondition` failures are labelled as "errors"
D) The non-blocking, exit-code-0 behaviour of `check` blocks makes them suitable for health monitoring dashboards and observability tooling — where surfacing a health status without blocking deployments is the desired outcome

---

### Question 8

**Difficulty:** Medium
**Answer Type:** many
**Topic:** `check` block — which TWO statements are TRUE?

Which TWO of the following statements about `check` blocks are TRUE?

A) A `check` block MUST include a scoped `data` source block — a `check` block that contains only `assert` blocks without a `data` source is invalid HCL syntax
B) `check` blocks run on BOTH `terraform plan` and `terraform apply` — they are evaluated after all resource operations complete in each run; this means health assertions are checked on every plan, giving continuous visibility even in runs that make no changes
C) A single `check` block can contain AT MOST one `assert` block — to check multiple conditions in the same `check` context, the engineer must declare multiple separate `check` blocks
D) The `data` source declared inside a `check` block can be referenced by resource blocks elsewhere in the configuration using the standard `data.<type>.<name>.<attribute>` syntax — this allows resource configurations to consume values fetched by the health check

---

### Question 9

**Difficulty:** Medium
**Answer Type:** one
**Topic:** `error_message` in condition blocks — which statement is TRUE?

Which of the following statements about the `error_message` argument in `validation`, `precondition`, and `postcondition` blocks is TRUE?

A) The `error_message` must be a static string literal with no interpolation — referencing `var.<name>` or any expression inside the `error_message` is a syntax error; this is the same restriction that applies to the `condition` expression
B) The `error_message` argument is optional in all three condition block types — if omitted, Terraform uses a default message such as "Condition failed"
C) The `error_message` is a string expression and CAN include interpolation — for example, a `validation` block's `error_message` can reference `var.<variable_name>` to include the invalid value in the message, such as `"${var.environment} is not an allowed environment"`; this helps engineers produce informative error messages that show the offending value
D) The `error_message` in a `postcondition` can reference `self.<attribute>` to include the resource's post-change attribute values, but the `error_message` in a `precondition` and `validation` cannot use any interpolation at all

---

### Question 10

**Difficulty:** Medium
**Answer Type:** one
**Topic:** `precondition` failing mid-apply — which statement is FALSE?

Which of the following statements about what happens when a `precondition` fails during `terraform apply` is FALSE?

A) When a `precondition` fails, Terraform halts the apply immediately — the resource that declares the failing `precondition` is NOT modified; its state is unchanged
B) When a `precondition` fails mid-apply, resources that were already successfully applied BEFORE the failing resource are NOT automatically rolled back — Terraform does not perform automatic rollback of completed resource changes
C) A failing `precondition` exits `terraform apply` with a non-zero exit code — this is what makes `precondition` suitable as a hard deployment gate in CI/CD pipelines, unlike `check` blocks which exit with code `0`
D) When a `precondition` fails on Resource B, and Resource A was already successfully applied in the same run, Terraform automatically destroys Resource A and reverts the infrastructure to the state it was in before the apply began — this transactional rollback is the key safety feature of `precondition`

---

### Question 11

**Difficulty:** Hard
**Answer Type:** one
**Topic:** Four statements about the three condition mechanisms — only ONE is TRUE

Four statements about Terraform's three condition mechanisms are presented below. Which is the ONLY TRUE statement?

A) A `postcondition` that fails causes Terraform to automatically taint the resource — the resource is marked in state as needing replacement, so the next `terraform apply` will destroy and recreate it; this auto-taint is what prevents a broken resource from persisting in the infrastructure
B) Variable `validation` blocks run after `terraform plan` is generated and displayed to the operator but before the operator types `yes` to approve — this gives the operator a chance to review both the plan and any validation warnings before committing
C) The `check` block's `assert` condition can reference ANY value available in the Terraform configuration, including resource attributes, data source outputs, local values, and variables — it is not restricted like `validation` conditions (which can only reference `var.<name>`) because `check` blocks run after all resource operations complete when those values are known
D) When a `precondition` fails on a resource that is being DESTROYED (not created or updated), Terraform ignores the `precondition` and proceeds with the destroy — `precondition` checks only apply to create and update operations, not destroy

---

### Question 12

**Difficulty:** Hard
**Answer Type:** many
**Topic:** Sensitive data handling — which TWO statements are TRUE?

Which TWO of the following statements about Terraform sensitive data handling are TRUE?

A) When a resource attribute is automatically marked sensitive by its provider (for example, `aws_db_instance.main.password`), any `output` or `local` that references that attribute must also be explicitly marked `sensitive = true` — otherwise Terraform raises a plan-time error about exposing a sensitive value
B) The `nonsensitive()` function removes the sensitive marking from a value, allowing it to be used in contexts that would otherwise require `sensitive = true`; using `nonsensitive()` is appropriate when an engineer has reviewed the data and determined it is safe to expose — for example, when wrapping a value in `base64encode()` or `sha256()` has made the original secret unrecoverable from the output
C) Sensitive values marked with `sensitive = true` on a variable are automatically excluded from `terraform.tfstate` — the state file omits them entirely so that even unrestricted access to the state file does not expose the original value
D) When Terraform performs a `terraform plan`, sensitive variable values are ALWAYS omitted from the plan output entirely — even in the diff showing what will change, the old and new values are always shown as `(sensitive value)` regardless of whether the value is actually changing

---

### Question 13

**Difficulty:** Hard
**Answer Type:** one
**Topic:** Four statements about `precondition` + `postcondition` placement and scope — only ONE is TRUE

Four statements about where and how `precondition` and `postcondition` blocks can be declared are presented below. Which is the ONLY TRUE statement?

A) A resource block can contain at most ONE `precondition` and ONE `postcondition` — declaring multiple of the same type (e.g., two `precondition` blocks in the same `lifecycle`) causes a Terraform configuration error
B) `precondition` and `postcondition` blocks are only valid inside `resource` blocks — they cannot be used inside `data` source blocks, `module` blocks, or `output` blocks
C) A resource's `lifecycle` block can contain multiple `precondition` blocks and multiple `postcondition` blocks — there is no limit on the number of each; every `precondition` is evaluated before the resource is changed and every `postcondition` is evaluated after; if any condition fails, Terraform halts with that condition's `error_message`
D) `postcondition` blocks support a special `rollback = true` argument that instructs Terraform to automatically destroy the just-created resource if the condition fails — without this argument, a failing `postcondition` leaves the resource in place and only exits non-zero

## Answer Key

| Q# | Answer(s) | Explanation | Source | Difficulty |
|----|-----------|-----------:|--------|------------|
| 1 | B | ** Terraform allows any number of `validation` blocks on a single variable declaration. Each block is evaluated independently — having separate blocks is functionally equivalent to combining conditions with `&&`, but produces clearer, more targeted error messages. For example, a `number` variable might have one validation block checking `var.count >= 1` and a separate block checking `var.count <= 10`, each with its own descriptive `error_message`. When multiple conditions fail, Terraform reports each failing block's `error_message`. Option A is a common misconception — it describes the single-block approach but incorrectly states it is the only approach. Options C and D describe non-existent restrictions that do not apply to Terraform's type system or validation evaluation. | ** Multiple `validation` blocks per variable — which statement is TRUE? | ** Easy |
| 2 | B | ** Option B is FALSE. `self` is NOT valid inside a `precondition` block. `self` is defined only in `postcondition` blocks, where it references the resource's attributes as they exist AFTER the resource change has been applied. A `precondition` runs BEFORE the resource is touched — there is no new state yet, and therefore `self` has nothing to reference. Using `self` in a `precondition` causes a Terraform evaluation error. For `precondition` assertions, you must reference other already-known values: other resource attributes, data source outputs, input variables, or locals. Options A, C, and D are all accurate: `self` in postcondition = post-change attributes; `self` in precondition = undefined; preconditions must reference external data. | ** `self` keyword in `precondition` — which statement is FALSE? | ** Easy |
| 3 | B, C | ** **(B)** is TRUE. Sensitivity propagates through module composition. When a child module output is marked `sensitive = true`, any reference to that output in a parent module is automatically treated as sensitive — the parent does not need to declare it sensitive again. This prevents sensitive data from accidentally appearing in parent module plan output or logs. **(C)** is TRUE. `sensitive = true` on an output suppresses the value in terminal output — `terraform apply` shows `(sensitive value)` for those outputs, and `terraform output` (all outputs) likewise redacts them. **(A)** is FALSE — this is a critical exam fact: `sensitive = true` does NOT encrypt or protect the value in `terraform.tfstate`. The value is still stored in plaintext JSON in state. Protecting state files requires encrypted remote backends and access controls. **(D)** is FALSE — sensitive output values ARE accessible in plaintext via `terraform output <name>` (querying a specific output by name), `terraform output -json`, and `terraform output -raw <name>`. The sensitive flag is a display control, not an access restriction. | ** `sensitive = true` on output blocks — which TWO statements are TRUE? | ** Easy |
| 4 | B | ** The `data` source declared inside a `check` block is scoped to that check and behaves differently from a top-level `data` source in two important ways. First, it cannot be referenced from outside the `check` block — `data.http.endpoint.status_code` is only visible within that check's `assert` conditions. Second, because check-scoped data sources are outside the main resource dependency graph, errors during their evaluation (such as a network timeout or API failure) do not fail the `terraform apply` — they contribute to the non-blocking warning behaviour of the `check` block. This design isolates health-check data fetches from the main configuration graph, preventing transient monitoring failures from blocking deployments. Option A is false — scoped data sources are NOT added to the main graph and CANNOT be referenced externally. Option C is false — `check` blocks run on BOTH `plan` and `apply`. Option D is false — any provider's data source can be used; `http` is simply the most common example. | ** `check` block scoped `data` source — which statement is TRUE? | ** Medium |
| 5 | C | ** Terraform enforces explicit acknowledgement of sensitive values in outputs. If an output's `value` expression directly or indirectly references a value marked `sensitive = true` (whether from a variable, another output, or a resource attribute that Terraform treats as sensitive), and the output block does not set `sensitive = true`, Terraform raises a plan-time error: something like `"Output refers to Terraform-sensitive values"`. The engineer must explicitly add `sensitive = true` to the output to confirm they understand the value is sensitive and will be redacted in terminal output. This design prevents accidental exposure — Terraform will not silently output a sensitive value in plaintext, nor will it silently suppress it. Option A is false — while sensitivity does propagate in some downstream contexts, Terraform still requires explicit `sensitive = true` on the output block itself. Option B is false — there is no "warning and continue" behaviour for this case. Option D is false — Terraform errors rather than silently omitting. | ** Outputting a sensitive variable without marking the output sensitive — which statement is TRUE? | ** Medium |
| 6 | C | ** Both `precondition` and `postcondition` blocks are valid inside `data` source `lifecycle` blocks, not just `resource` blocks. This is an important and sometimes overlooked feature. A typical use case: a data source that looks up an AMI by filter might return any AMI that matches — a `postcondition` on the data source can assert that the fetched result meets specific requirements (e.g., `self.architecture == "x86_64"`, `self.state == "available"`, `self.root_device_type == "ebs"`). This catches data quality issues before the value is used by resource blocks, surfacing a clear error message rather than a cryptic downstream failure. Using `self` in a data source `postcondition` references the data source's fetched attributes, just as `self` in a resource `postcondition` references the resource's attributes. Option A is false — data sources DO support lifecycle conditions. Option B is false — both `precondition` and `postcondition` are valid on data sources. Option D is false — lifecycle conditions run during plan and apply, not init. | ** `precondition` and `postcondition` on data sources — which statement is TRUE? | ** Medium |
| 7 | C | ** Option C is FALSE. A failing `check` block assertion does NOT cause `terraform apply` to exit with a non-zero exit code. The apply exits `0` (success) regardless of check assertion results — check failures are purely informational warnings and do not affect the exit code. This is a fundamental design principle: `check` blocks are for non-blocking health monitoring, not deployment gates. Options A and B correctly describe the consequence of this behaviour: exit `0` means CI/CD pipelines that gate on exit code alone will NOT detect check failures; additional output parsing or tooling is needed if check failures should trigger pipeline alerts. Option D correctly identifies the intended use case for `check` blocks — health observability without blocking risk. | ** `check` block exit code on assertion failure — which statement is FALSE? | ** Medium |
| 8 | B, C | ** **(B)** is TRUE. `check` blocks run on every `terraform plan` AND every `terraform apply`. They are not limited to apply-time execution — this means every plan run also evaluates the health assertions, giving operators continuous infrastructure health feedback even in runs that compute no changes. **(C)** is TRUE. Each `check` block supports only ONE `assert` block. To check multiple independent conditions, declare multiple `check` blocks — each with its own `assert` and optionally its own scoped `data` source. **(A)** is FALSE. The `data` source block inside a `check` block is optional. A `check` block can contain just one or more `assert` blocks without any scoped `data` source — the `assert` can reference any already-available values in the configuration. **(D)** is FALSE. The `data` source inside a `check` block is scoped exclusively to that block and CANNOT be referenced by resource blocks or other configuration elements outside the `check`. This is a deliberate design choice to keep health-check data fetches isolated from the main dependency graph. | ** `check` block — which TWO statements are TRUE? | ** Medium |
| 9 | C | ** The `error_message` in condition blocks is a standard HCL string expression — it is NOT restricted to static literals. Interpolation is fully supported, which allows the message to include the actual invalid value for clarity. In a `validation` block, the message can reference `var.<variable_name>`: `error_message = "Expected one of [dev, staging, production], got: ${var.environment}."`. In a `postcondition`, the message can reference `self.<attribute>`: `error_message = "Instance has no public IP — got: ${self.public_ip}."`. Informative error messages that include the offending value are considered best practice because they reduce debugging time. The ONLY restriction is what the `condition` expression can reference (e.g., `validation` conditions can only reference `var.<name>`), not what `error_message` can reference. Option A incorrectly applies the `condition` reference restriction to `error_message`. Option B is false — `error_message` is required, not optional. Option D incorrectly splits interpolation availability across block types. | ** `error_message` in condition blocks — which statement is TRUE? | ** Medium |
| 10 | D | ** Option D is FALSE. Terraform does NOT perform automatic transactional rollback when a `precondition` (or any other condition) fails mid-apply. Terraform's apply is not atomic — it applies resources in dependency order, and a failure mid-apply leaves the infrastructure in a partially-applied state. Resources that were successfully applied before the failure remain in their new state; the failing resource and any that depend on it are not applied. This partial-state behaviour is by design and is clearly documented — Terraform is not a database transaction system. To resolve a partial apply, operators must investigate the failure, fix the configuration, and run `terraform apply` again (Terraform will only attempt to apply the remaining un-applied resources). Options A, B, and C are all accurate: the failing resource is not touched, completed resources are not rolled back, and the exit code is non-zero. | ** `precondition` failing mid-apply — which statement is FALSE? | ** Medium |
| 11 | C | ** **(C)** is the ONLY TRUE statement. `check` block `assert` conditions can reference any value that is available in the configuration — resource attributes, data source outputs, locals, variables, and the outputs of the check block's own scoped `data` source. Unlike `validation` conditions (restricted to `var.<name>` because they run before planning), `check` assertions run AFTER all resource operations complete, when all resource attributes are known. This full access is what makes `check` suitable for cross-cutting health assertions that reference multiple resources. **(A)** is FALSE — a failing `postcondition` does NOT automatically taint the resource. Terraform marks the apply as failed (non-zero exit) but does NOT add a taint to the resource in state. The resource exists in its current state; no automatic marking for replacement occurs. **(B)** is FALSE — `validation` blocks run BEFORE `terraform plan` generates any output; they fire during input variable processing, before planning even begins. The operator never sees a plan if validation fails. **(D)** is FALSE — `precondition` checks DO apply to destroy operations. A `precondition` on a resource is evaluated before ANY change to that resource, including destruction. If a `precondition` condition evaluates to false before a destroy, the destroy is blocked. | ** Four statements about the three condition mechanisms — only ONE is TRUE | ** Hard |
| 12 | A, B | ** **(A)** is TRUE. When a provider marks a resource attribute as sensitive (e.g., `aws_db_instance.password`), Terraform propagates that sensitivity. Any `output` block that directly or indirectly references that attribute must declare `sensitive = true` — otherwise Terraform raises a plan-time error. Similarly, locals that reference sensitive-marked attributes carry the sensitive marking forward in expressions. This enforced propagation prevents accidental exposure. **(B)** is TRUE. The `nonsensitive()` function exists to explicitly unwrap the sensitive marking from a value when the engineer determines it is safe to do so — for example, after hashing a secret with `sha256()`, the hash is not itself a secret, so `nonsensitive(sha256(var.db_password))` produces a non-sensitive string that can be used freely. Using `nonsensitive()` is intentional and requires engineering judgment — Terraform trusts the caller has reviewed the exposure. **(C)** is FALSE — sensitive values are NOT excluded from `terraform.tfstate`. All attribute values, regardless of sensitivity marking, are written to state in plaintext. This is the most critical and commonly tested exam fact about sensitive data in Terraform. **(D)** is partially false. While sensitive values are shown as `(sensitive value)` in most plan output, the behaviour is not absolute for all cases — for example, when a sensitive value changes, Terraform indicates the attribute will change but still redacts the old and new values as `(sensitive value)`. However, the claim "regardless of whether the value is actually changing" is an overstatement — the exact redaction behaviour depends on context and provider implementation. More importantly, option C contains a clear factual error that makes it the definitively false option. | ** Sensitive data handling — which TWO statements are TRUE? | ** Hard |
| 13 | C | ** **(C)** is the ONLY TRUE statement. A `lifecycle` block can contain multiple `precondition` blocks AND multiple `postcondition` blocks — there is no enforced limit. Having multiple conditions allows each assertion to have a distinct, targeted `error_message` that clearly identifies which specific requirement was violated. All declared `precondition` blocks are evaluated before the resource is changed; all declared `postcondition` blocks are evaluated after. If any condition fails, Terraform halts at that point with the failing condition's `error_message`. **(A)** is FALSE — multiple `precondition` and `postcondition` blocks are explicitly supported in the same `lifecycle` block. **(B)** is FALSE — `precondition` and `postcondition` are valid on BOTH `resource` AND `data` source blocks. Data source postconditions are commonly used to validate fetched data before it is consumed by resource blocks. They are NOT valid on `module` or `output` blocks, but the claim that they're restricted to resource blocks is inaccurate. **(D)** is FALSE — there is no `rollback = true` argument on `postcondition` blocks. Such an argument does not exist in Terraform's HCL specification. A failing `postcondition` exits non-zero and leaves the resource in place — there is no automatic rollback mechanism. | ** Four statements about `precondition` + `postcondition` placement and scope — only ONE is TRUE | ** Hard |
