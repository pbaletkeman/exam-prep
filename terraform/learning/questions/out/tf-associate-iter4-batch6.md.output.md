# Terraform Associate Exam Questions

---

### Question 1 — Flawed Claim: `check` Block Failure Blocks Apply

**Difficulty**: Easy
**Answer Type**: one
**Topic**: Whether a failing `check` block assertion blocks `terraform apply`

**Question**:
A colleague explains the three Terraform condition mechanisms and states:

> "A failed `check` block assertion works just like a failed `precondition` — it blocks `terraform apply` and prevents the infrastructure from being created or modified."

What is wrong with this explanation?

- A) Nothing — `check` block failures and `precondition` failures both block apply
- B) The explanation is wrong: `check` block failures are **warnings only** — they do not block apply; all resources are still created or updated and the apply exits successfully
- C) The explanation is wrong: `check` block failures are more severe than `precondition` failures — they abort the entire Terraform run including `init`
- D) The explanation is wrong: `check` block failures only block apply if they contain a scoped `data` source

---

### Question 2 — Flawed Claim: `validation` Runs During Apply

**Difficulty**: Easy
**Answer Type**: one
**Topic**: When variable `validation` blocks are evaluated in the Terraform workflow

**Question**:
A team's internal wiki states:

> "Variable `validation` blocks run during `terraform apply`, after the operator has reviewed and approved the execution plan. If a variable fails validation at this point, Terraform aborts the apply."

What is wrong with this description?

- A) Nothing — variable validation runs during `terraform apply` after plan approval
- B) The description is wrong: variable `validation` blocks run **before `terraform plan`** — they are evaluated during input variable processing, which happens before any planning; an invalid variable aborts before a plan is ever generated
- C) The description is wrong: variable `validation` blocks only run when explicitly invoked with `terraform validate`
- D) The description is wrong: variable `validation` blocks run at `terraform init` time when providers are registered

---

### Question 3 — Flawed HCL: `validation` Condition References a Local

**Difficulty**: Medium
**Answer Type**: one
**Topic**: What a `validation` block's `condition` is allowed to reference

**Question**:
An engineer writes the following to validate that an environment variable matches an allowed list defined in a local:

```hcl
locals {
  allowed_envs = ["dev", "staging", "production"]
}

variable "environment" {
  type = string

  validation {
    condition     = contains(local.allowed_envs, var.environment)
    error_message = "environment must be one of: dev, staging, production."
  }
}
```

What is wrong with this configuration?

- A) Nothing — a `validation` block can reference any value available in the module
- B) The configuration is wrong: `validation` block conditions can only reference `var.<variable_name>`; referencing `local.allowed_envs` is not permitted and causes a Terraform error
- C) The configuration is wrong: `contains()` cannot be used inside a `validation` block condition
- D) The configuration is wrong: `locals` must be declared after all `variable` blocks in a Terraform file

---

### Question 4 — Flawed Claim: `self` Available in `precondition`

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Which lifecycle condition blocks allow use of the `self` reference

**Question**:
An engineer documents lifecycle conditions and writes:

> "`self` is available in both `precondition` and `postcondition` blocks — you can use `self.<attribute>` in either to inspect the resource's current or desired state before or after a change."

What is wrong with this documentation?

- A) Nothing — `self` is available in both `precondition` and `postcondition`
- B) The documentation is wrong: `self` is only available in `postcondition` blocks; `precondition` blocks cannot use `self` because the resource has not yet been created or updated when the precondition is evaluated
- C) The documentation is wrong: `self` is only available in `precondition` blocks; `postcondition` blocks must reference the resource by its full address
- D) The documentation is wrong: `self` is not valid in either block; resource attributes must always be referenced by their full address

---

### Question 5 — Flawed Claim: `check` Block Introduced in Terraform 1.3

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Which Terraform version introduced the `check` block

**Question**:
A team's migration runbook contains the following statement:

> "The `check` block was introduced in Terraform 1.3 as part of the same release that added `moved` blocks, enabling non-blocking infrastructure health assertions."

Which two facts in this statement are incorrect?

- A) Nothing — the `check` block was introduced in 1.3 alongside `moved` blocks
- B) The `check` block was introduced in **Terraform 1.5**, not 1.3; and `moved` blocks were introduced in **Terraform 1.1**, not in the same release as `check` — the two features were added in different versions
- C) The `check` block was introduced in Terraform 1.7; `moved` blocks were introduced in 1.3
- D) The `check` block was introduced in Terraform 1.5; `moved` blocks were also introduced in Terraform 1.5 in the same release

---

### Question 6 — Flawed Claim: Failed `postcondition` Destroys Resource and Removes from State

**Difficulty**: Medium
**Answer Type**: one
**Topic**: What happens to a resource in AWS and in state when its `postcondition` fails

**Question**:
A developer explains postcondition behaviour to their team:

> "When a `postcondition` fails after a resource is created, Terraform automatically destroys the resource to maintain a consistent, valid state — it removes the resource from AWS and from `terraform.tfstate` so the next apply starts clean."

What is wrong with this explanation?

- A) Nothing — Terraform does automatically destroy resources that fail postconditions
- B) The explanation is wrong: when a `postcondition` fails, the resource **remains in AWS and remains recorded in `terraform.tfstate`**; Terraform does not perform an automatic rollback, destroy, or state removal — the apply exits with a failure status and the team must investigate manually
- C) The explanation is wrong: when a `postcondition` fails, the resource is kept in AWS but is removed from state so the next plan treats it as a new resource to be imported
- D) The explanation is wrong: when a `postcondition` fails, the resource is destroyed in AWS but remains in state as an orphaned record

---

### Question 7 — Flawed HCL: `precondition` Placed Outside `lifecycle` Block

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Where `precondition` and `postcondition` blocks must be declared inside a resource

**Question**:
An engineer writes the following resource to prevent deployment to a test environment:

```hcl
resource "aws_instance" "web" {
  ami           = "ami-0abc123"
  instance_type = "t3.micro"

  precondition {
    condition     = var.environment != "test"
    error_message = "This resource cannot be deployed to the test environment."
  }
}
```

What is wrong with this configuration?

- A) Nothing — `precondition` blocks can be placed directly inside any resource block
- B) The configuration is wrong: `precondition` blocks must be declared **inside a `lifecycle` block** within the resource; placing `precondition` directly as a resource argument is invalid syntax
- C) The configuration is wrong: `precondition` cannot reference variables — it can only reference data source attributes
- D) The configuration is wrong: `precondition` blocks must be placed in a separate `conditions` file, not inside the resource block

---

### Question 8 — Two Flawed Claims About `check` Block Structure

**Difficulty**: Medium
**Answer Type**: many
**Topic**: Where `check` blocks can be placed and whether a scoped `data` source is required

**Question**:
A developer documents the `check` block and makes two structural claims:

> **Claim 1**: "A `check` block can be placed inside a resource block to validate that specific resource's post-deployment state, similar to `postcondition`."
> **Claim 2**: "A `check` block must always include both a `data` block and an `assert` block — the `data` block is required; an `assert` block alone is not valid."

Which TWO statements correctly identify what is wrong with these claims? (Select two.)

- A) Claim 1 is **wrong**: `check` blocks are **top-level configuration blocks** — they cannot be nested inside resource blocks; their placement is similar to `resource` or `data` blocks at the root of a module
- B) Claim 1 is **correct**: `check` blocks can be placed inside resource blocks
- C) Claim 2 is **wrong**: the `data` block inside a `check` block is **optional** — a `check` block with only an `assert` block is perfectly valid
- D) Claim 2 is **correct**: a `check` block with only an `assert` and no `data` block causes a Terraform parse error

---

### Question 9 — Flawed Claim: Sensitive Variable Propagates Automatically to Output

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Whether `sensitive = true` on a variable automatically marks referencing outputs as sensitive

**Question**:
A developer marks a variable as sensitive and then creates an output referencing it:

```hcl
variable "db_password" {
  type      = string
  sensitive = true
}

output "db_connection_string" {
  value = "postgresql://admin:${var.db_password}@db.example.com/prod"
}
```

The developer says: "Since I've marked `var.db_password` as sensitive, Terraform will automatically treat `db_connection_string` as sensitive too — no changes to the output block are needed."

What is wrong with this claim?

- A) Nothing — Terraform automatically marks outputs as sensitive when they reference sensitive variables
- B) The claim is wrong: Terraform **detects** that the output references a sensitive value and raises a **plan error** requiring `sensitive = true` to be explicitly added to the output block — automatic propagation does not occur without user action
- C) The claim is wrong: Terraform silently allows the output to expose the sensitive value in plaintext; no error or automatic protection is applied
- D) The claim is wrong: sensitive variables cannot be interpolated into output values at all — they must be referenced directly with `value = var.db_password`

---

### Question 10 — Two Flawed Claims About Condition Mechanism Failure Behaviour

**Difficulty**: Hard
**Answer Type**: many
**Topic**: When and how `validation`, `precondition`, and `check` failures are raised

**Question**:
A team's study guide contains the following two statements about condition mechanism failure behaviour:

> **Claim 1**: "A failed `validation` block is treated as a non-fatal warning during `terraform plan` — the plan still generates and shows proposed changes, but an advisory message is displayed."
> **Claim 2**: "A failed `precondition` produces a warning and allows the resource to be created anyway — it is the operator's responsibility to act on the warning."

Which TWO statements correctly identify the errors? (Select two.)

- A) Claim 1 is **wrong**: a failed `validation` block is a **fatal error that halts Terraform before any plan is generated** — it is not a warning, and no execution plan is produced
- B) Claim 1 is **correct**: validation failures are non-fatal warnings and the plan proceeds
- C) Claim 2 is **wrong**: a failed `precondition` is a **fatal error that halts `terraform apply` before the resource is created or modified** — the resource is not created and the apply exits with a failure
- D) Claim 2 is **correct**: precondition failures are warnings that allow the resource to be created

---

### Question 11 — Flawed Claim: Scoped `data` Source in `check` Block Has Fatal Errors Like Top-Level `data`

**Difficulty**: Hard
**Answer Type**: one
**Topic**: How errors from a scoped `data` source inside a `check` block differ from top-level `data` source errors

**Question**:
A developer adds a `check` block with a scoped HTTP data source:

```hcl
check "api_health" {
  data "http" "probe" {
    url = "https://api.internal.example.com/health"
  }

  assert {
    condition     = data.http.probe.status_code == 200
    error_message = "API health check failed with status ${data.http.probe.status_code}."
  }
}
```

During `terraform apply`, the internal API is unreachable and the HTTP request times out. The developer claims: "This HTTP data source inside the `check` block will behave exactly like a top-level `data` source — a connection failure will cause a fatal error and abort the apply."

What is wrong with this claim?

- A) Nothing — a data source error inside a `check` block is fatal and aborts apply, just like a top-level `data` source error
- B) The claim is wrong: a data source error inside a `check` block is treated the same as a failing `assert` condition — it produces a **warning** and does not abort the apply; this is one of the key differences between scoped and top-level `data` sources
- C) The claim is wrong: the scoped `data` source inside a `check` block is never actually executed during apply — it is only evaluated during `terraform plan`
- D) The claim is wrong: `check` block data sources automatically retry three times before deciding whether to fail or warn

---

### Question 12 — Two Flawed Claims About Retrieving Sensitive Output Values

**Difficulty**: Medium
**Answer Type**: many
**Topic**: Which `terraform output` command forms expose sensitive output values in plaintext

**Question**:
A developer sets `sensitive = true` on an output named `db_password` and makes two claims about retrieval:

> **Claim 1**: "Running `terraform output -json` will display sensitive outputs as `(sensitive value)` in the JSON, the same way `terraform output` (no arguments) does — sensitive values are always hidden in any output format."
> **Claim 2**: "Running `terraform output db_password` (querying the single output by name) will display `(sensitive value)` — there is no way to retrieve the actual value using the `terraform output` command."

Which TWO statements correctly identify the errors? (Select two.)

- A) Claim 1 is **wrong**: `terraform output -json` **reveals sensitive output values in plaintext** in the JSON response — it does not redact them as `(sensitive value)`
- B) Claim 1 is **correct**: `terraform output -json` always hides sensitive values
- C) Claim 2 is **wrong**: `terraform output db_password` (querying a single output by name) **displays the actual plaintext value** — only the aggregate `terraform output` (no arguments) listing redacts sensitive values
- D) Claim 2 is **correct**: querying a sensitive output by name always returns `(sensitive value)`

## Answer Key

| Q# | Answer(s) | Explanation | Source | Difficulty |
|----|-----------|-----------:|--------|------------|
| 1 | B | N/A | Whether a failing `check` block assertion blocks `terraform apply` | Easy |
| 2 | B | N/A | When variable `validation` blocks are evaluated in the Terraform workflow | Easy |
| 3 | B | N/A | What a `validation` block's `condition` is allowed to reference | Medium |
| 4 | B | N/A | Which lifecycle condition blocks allow use of the `self` reference | Medium |
| 5 | B | N/A | Which Terraform version introduced the `check` block | Medium |
| 6 | B | N/A | What happens to a resource in AWS and in state when its `postcondition` fails | Medium |
| 7 | B | N/A | Where `precondition` and `postcondition` blocks must be declared inside a resource | Medium |
| 8 | A, C | N/A | Where `check` blocks can be placed and whether a scoped `data` source is required | Medium |
| 9 | B | N/A | Whether `sensitive = true` on a variable automatically marks referencing outputs as sensitive | Medium |
| 10 | A, C | N/A | When and how `validation`, `precondition`, and `check` failures are raised | Hard |
| 11 | B | N/A | How errors from a scoped `data` source inside a `check` block differ from top-level `data` source errors | Hard |
| 12 | A, C | N/A | Which `terraform output` command forms expose sensitive output values in plaintext | Medium |
