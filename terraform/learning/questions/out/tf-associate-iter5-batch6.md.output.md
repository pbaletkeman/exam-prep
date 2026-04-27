# Terraform Associate Exam Questions

---

### Question 1 — `validation` Block vs `precondition`: When Each Runs

**Difficulty**: Easy
**Answer Type**: one
**Topic**: Contrast between the timing and triggering point of variable validation and lifecycle preconditions

**Question**:
Compare a `validation` block inside a `variable` declaration with a `precondition` block inside a resource's `lifecycle`. What is the key difference in when each runs during the Terraform workflow?

- A) Both run at the same point — they are two syntactic alternatives for the same assertion mechanism
- B) A `validation` block runs **before `terraform plan`** — it is evaluated during input variable processing and halts the run before any infrastructure analysis begins; a `precondition` runs **during `terraform apply`**, just before Terraform modifies the specific resource that contains it
- C) A `precondition` runs before `terraform plan`; a `validation` block runs after the plan is approved but before apply begins
- D) Both run after `terraform apply` completes — they are post-deployment verification tools

---

### Question 2 — `precondition` vs `postcondition`: Before vs After the Resource Change

**Difficulty**: Easy
**Answer Type**: one
**Topic**: Contrast between what precondition and postcondition assert and when each runs relative to the resource change

**Question**:
Compare a `precondition` and a `postcondition` declared in the same resource's `lifecycle` block. What is the key difference in their execution order and access to resource attributes?

- A) `precondition` and `postcondition` run at the same time — they differ only in whether the condition expression returns true or false
- B) A `precondition` runs **before** the resource is created or updated — it asserts that prerequisites are met and cannot use `self` to reference the resource's new attribute values; a `postcondition` runs **after** the resource change completes — it asserts that the created/updated resource meets requirements, and `self` references the resource's post-change attributes
- C) A `postcondition` runs before the resource change and uses `self` to reference the previous state; a `precondition` runs after and uses `self` to reference the new state
- D) Both can use `self`, but `precondition` uses the current (pre-change) `self` and `postcondition` uses the planned (post-change) `self`

---

### Question 3 — `check` Block vs `precondition`: Blocking vs Non-Blocking Failures

**Difficulty**: Easy
**Answer Type**: one
**Topic**: Contrast between the failure behaviour of check blocks and preconditions

**Question**:
Compare a failing `check` block assertion with a failing `precondition`. What is the fundamental difference in how Terraform handles each failure?

- A) Both a failing `check` block and a failing `precondition` block apply and allow all resources to be created
- B) A failing `precondition` **blocks** the apply — Terraform halts before modifying the resource and exits with a non-zero status; a failing `check` block assertion is a **warning only** — Terraform displays the error message but all resource changes proceed normally and the apply exits successfully
- C) A failing `check` block blocks the apply; a failing `precondition` produces a warning only
- D) Both a failing `check` block and a failing `precondition` roll back any resources already created in the same apply run

---

### Question 4 — `validation` Block Scope vs `precondition` Scope: What Each Can Reference

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Contrast between the expression scope allowed in validation conditions and precondition conditions

**Question**:
Compare what a `validation` block's `condition` and a `precondition`'s `condition` are each allowed to reference in their expressions. What is the key difference?

- A) Both are restricted to referencing only `var.<name>` — neither can reference data sources or resource attributes
- B) A `validation` block's `condition` can **only** reference `var.<variable_name>` — the specific variable being validated; a `precondition`'s `condition` can reference any value available at plan time, including data sources, other resource attributes, locals, and variables
- C) A `precondition`'s `condition` can only reference `self`; a `validation` block's `condition` can reference any expression including resources
- D) Both can reference any expression — the difference is only in when they are evaluated, not what they can reference

---

### Question 5 — `sensitive = true` on Variable: Terminal Masking vs State Protection

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Contrast between what sensitive=true on a variable actually protects vs what it does not protect

**Question**:
A variable is declared `sensitive = true` for a database password. Compare the protection this provides in two contexts: terminal output and the Terraform state file. What is the accurate description of each?

- A) `sensitive = true` both masks the value in terminal output AND encrypts it in the state file — it provides complete protection in both contexts
- B) `sensitive = true` **masks** the value in terminal output during `plan` and `apply` (showing `(sensitive value)` instead of the plaintext), but it provides **no protection** in the state file — the value is still stored in plaintext in `terraform.tfstate`; protecting it at rest requires an encrypted remote backend
- C) `sensitive = true` protects the value in the state file but has no effect on terminal output — the plaintext value is always shown during plan and apply
- D) `sensitive = true` removes the value from the state file entirely — it is never persisted anywhere

---

### Question 6 — `validation` Block vs `check` Block: Where Each Is Declared

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Contrast between the structural location of a validation block and a check block in HCL

**Question**:
Compare where a `validation` block and a `check` block are declared in a Terraform configuration. How does their structural location differ, and what does that difference imply?

- A) Both `validation` and `check` blocks are top-level HCL blocks — they sit at the root of any `.tf` file alongside `resource` and `provider` blocks
- B) A `validation` block is declared **nested inside a `variable` block** — it is scoped to that specific variable and can only reference that variable; a `check` block is a **top-level block** — it sits at the root of a `.tf` file like a `resource` or `output` block, and it can reference any infrastructure value in scope, optionally including a scoped `data` source
- C) A `check` block is nested inside a `resource` block's `lifecycle`; a `validation` block is a top-level block
- D) Both are nested inside the `lifecycle` block of the resource they guard

---

### Question 7 — `precondition` Failure vs `postcondition` Failure: Resource State After Each

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Contrast between the resource's state in AWS after a precondition failure vs a postcondition failure

**Question**:
An `aws_instance` resource has both a `precondition` and a `postcondition`. Compare the state of the EC2 instance in AWS after each type of failure:

- **Scenario A**: The `precondition` condition evaluates to `false` during apply
- **Scenario B**: The `postcondition` condition evaluates to `false` during apply

What is the difference in the real-world resource state between the two scenarios?

- A) In both scenarios, the EC2 instance is created in AWS — Terraform only removes it after the failure is acknowledged
- B) In Scenario A (precondition failure), the EC2 instance is **never created** in AWS — Terraform halts before making the API call; in Scenario B (postcondition failure), the EC2 instance **has been created** in AWS — Terraform only evaluates the postcondition after the API call succeeds, meaning the resource exists even though Terraform's apply failed
- C) In both scenarios, Terraform automatically destroys the resource and returns the infrastructure to its pre-apply state
- D) In Scenario A, the EC2 instance is created and then immediately destroyed; in Scenario B, the instance is never created

---

### Question 8 — `sensitive` Variable Propagation vs Explicit `sensitive` Output

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Contrast between automatic sensitive propagation and explicit output sensitivity declaration

**Question**:
Compare two approaches for preventing a database password from appearing in terminal output:

- **Approach A**: Declare `variable "db_password" { sensitive = true }` and use `var.db_password` in a resource; do not declare any output
- **Approach B**: Declare the variable without `sensitive`, but declare `output "db_password" { value = var.db_password; sensitive = true }`

What is a key difference between these two approaches?

- A) Both approaches are exactly equivalent in all scenarios — sensitive propagation and explicit output sensitivity are interchangeable
- B) In Approach A, the `sensitive = true` on the variable causes Terraform to **automatically propagate** the sensitive marker to any expression that uses `var.db_password` — plan output, error messages, and any output that references it will be masked without needing explicit `sensitive = true` on the output; in Approach B, only the specific `output` block is masked — `var.db_password` itself is not marked sensitive, so if it appears in plan output or error messages elsewhere in the configuration, it may not be automatically redacted
- C) Approach B is more secure than Approach A because explicitly marking an output as sensitive also encrypts the value in the state file
- D) Approach A prevents the value from being stored in state; Approach B stores it in state but masks it in terminal output

---

### Question 9 — `check` Block With Scoped Data Source vs `check` Block Without

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Contrast between a check block that embeds a scoped data source and one that references module-level values

**Question**:
Compare these two `check` block patterns:

**Pattern A** — scoped data source inside check:
```hcl
check "endpoint_health" {
  data "http" "ping" {
    url = "https://${aws_lb.web.dns_name}/health"
  }
  assert {
    condition     = data.http.ping.status_code == 200
    error_message = "Health endpoint returned ${data.http.ping.status_code}."
  }
}
```

**Pattern B** — no scoped data source:
```hcl
check "db_endpoint_set" {
  assert {
    condition     = can(tostring(aws_db_instance.main.endpoint))
    error_message = "Database endpoint attribute is not set."
  }
}
```

What is the key difference in scope between the two patterns?

- A) Pattern A is invalid — a `check` block cannot contain a `data` source; only `assert` blocks are allowed
- B) In Pattern A, the `data "http" "ping"` source is **scoped to the `check` block** — it is only evaluated during the check and its result is not accessible elsewhere in the module; in Pattern B, no data source is needed because the assert references an attribute directly from a resource already in state — the check block's assert can reference any module-level resource or data source without embedding a scoped source
- C) Pattern B is invalid because a `check` block must always contain a `data` source block
- D) The scoped data source in Pattern A is automatically added to the module's data sources and can be referenced from other resources

---

### Question 10 — Three Condition Mechanisms: Failure Behaviour Comparison

**Difficulty**: Medium
**Answer Type**: many
**Topic**: Contrasting TWO failure behaviour differences across the three assertion mechanisms

**Question**:
Terraform provides three condition assertion mechanisms: `validation`, `precondition`/`postcondition`, and `check`. Which TWO statements correctly describe a contrast in their failure behaviour? (Select two.)

- A) A failing `validation` condition halts Terraform **before any plan is generated** — the run aborts with the error_message and no infrastructure analysis is performed; a failing `check` assertion produces a **warning** that is displayed but does not prevent the apply from completing
- B) A failing `precondition` halts the apply **before modifying the target resource** — the resource is never created or updated; a failing `postcondition` halts the apply **after the resource has been created or updated** — the resource already exists in the cloud provider when the failure is reported
- C) `validation`, `precondition`, and `postcondition` all produce warnings only — none of them block the apply
- D) A failing `check` assertion blocks the apply and triggers a rollback of any resources created during the run

---

### Question 11 — `validation` Block vs `check` Block: What Each Can Reference

**Difficulty**: Hard
**Answer Type**: one
**Topic**: Deep contrast between the expression scope and structural rules governing validation conditions and check assertions

**Question**:
Both `validation` blocks and `check` block assertions use a `condition` expression that must evaluate to a boolean. Compare the expression scope rules for each — what can each reference, and what structural rule constrains the `check` block that does not apply to `validation`?

- A) Both `validation` and `check` block conditions are restricted to referencing only `var.<name>` — no other values are permitted in either context
- B) A `validation` block's `condition` can only reference `var.<variable_name>` — all other references are forbidden; a `check` block's `assert` condition can reference any module-level value (resources, data sources, locals, variables); however, if a `check` block includes a scoped `data` source, the data source reference in the assert must use the `data.<type>.<name>` form scoped to the check — and that scoped source cannot be referenced outside the `check` block
- C) A `check` block's condition is restricted to referencing only `data` source attributes; a `validation` block can reference any value including resource attributes
- D) Both can reference resource attributes and data source results — the only difference is that `validation` is evaluated earlier in the workflow

---

### Question 12 — `postcondition` with `self` vs `precondition` with External References

**Difficulty**: Hard
**Answer Type**: many
**Topic**: Contrasting TWO specific technical rules about expression references in preconditions and postconditions

**Question**:
Compare the expression reference rules for `precondition` and `postcondition` blocks. Which TWO statements correctly describe a difference? (Select two.)

- A) `self` is valid **only** in a `postcondition` — it refers to the resource after it has been created or updated; `self` is **not valid** in a `precondition` because the resource hasn't been created/modified yet when the precondition is evaluated
- B) A `precondition` can reference any value that is known at plan time — including other resource attributes, data sources, locals, and variables — but not `self`; a `postcondition` can reference all of those plus `self` to inspect the resource's own post-change attributes
- C) `self` is valid in both `precondition` and `postcondition`; the difference is that `self` in a `precondition` refers to the planned state while `self` in a `postcondition` refers to the applied state
- D) A `postcondition` can only reference `self` — it cannot reference other resources or module-level values

---

### Question 13 — `sensitive = true` vs Vault Dynamic Secrets: Protection Depth

**Difficulty**: Hard
**Answer Type**: one
**Topic**: Deep contrast between Terraform-native sensitive masking and HashiCorp Vault dynamic secrets as competing approaches to secret handling

**Question**:
Compare two approaches to managing a database password in Terraform:

- **Approach A**: Declare `variable "db_password" { sensitive = true }` and pass the password via `TF_VAR_db_password` at apply time
- **Approach B**: Use the Vault provider with a `data "vault_generic_secret"` data source to retrieve credentials dynamically during apply — no password variable in the Terraform configuration

What are the two most significant security differences between these approaches?

- A) Approach A is more secure because `sensitive = true` encrypts the value in state; Approach B stores the Vault token in state instead
- B) In Approach A, the password value **exists in the Terraform state file in plaintext** (despite the `sensitive = true` masking in terminal output) — anyone with read access to state can retrieve it; in Approach B, the credentials are **fetched dynamically** at apply time and are typically **short-lived** (dynamic secrets with a TTL) — they may never be stored in state as a sensitive value, and the Vault token used for authentication can be separately controlled and rotated independently of the database password
- C) Both approaches store the password in state — the only difference is that Approach B uses a second-factor Vault token alongside it
- D) Approach B is less secure because Vault data source results are never marked sensitive and will always appear in plaintext in terminal output and state

## Answer Key

| Q# | Answer(s) | Explanation | Source | Difficulty |
|----|-----------|-----------:|--------|------------|
| 1 | B | N/A | Contrast between the timing and triggering point of variable validation and lifecycle preconditions | Easy |
| 2 | B | N/A | Contrast between what precondition and postcondition assert and when each runs relative to the resource change | Easy |
| 3 | B | N/A | Contrast between the failure behaviour of check blocks and preconditions | Easy |
| 4 | B | N/A | Contrast between the expression scope allowed in validation conditions and precondition conditions | Medium |
| 5 | B | N/A | Contrast between what sensitive=true on a variable actually protects vs what it does not protect | Medium |
| 6 | B | N/A | Contrast between the structural location of a validation block and a check block in HCL | Medium |
| 7 | B | N/A | Contrast between the resource's state in AWS after a precondition failure vs a postcondition failure | Medium |
| 8 | B | N/A | Contrast between automatic sensitive propagation and explicit output sensitivity declaration | Medium |
| 9 | B | N/A | Contrast between a check block that embeds a scoped data source and one that references module-level values | Medium |
| 10 | A, B | N/A | Contrasting TWO failure behaviour differences across the three assertion mechanisms | Medium |
| 11 | B | N/A | Deep contrast between the expression scope and structural rules governing validation conditions and check assertions | Hard |
| 12 | A, B | N/A | Contrasting TWO specific technical rules about expression references in preconditions and postconditions | Hard |
| 13 | B | N/A | Deep contrast between Terraform-native sensitive masking and HashiCorp Vault dynamic secrets as competing approaches to secret handling | Hard |
