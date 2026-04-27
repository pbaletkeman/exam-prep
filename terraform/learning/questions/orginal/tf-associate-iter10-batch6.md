# Terraform Associate (004) — Question Bank Iter 10 Batch 6

**Iteration**: 10
**Iteration Style**: Exam-style scenarios — multi-sentence real-world context questions
**Batch**: 6
**Objective**: Custom Conditions & Sensitive Data
**Sources**: prompt10-custom-conditions-sensitive-data.md
**Generated**: 2026-04-26
**Total Questions**: 12
**Difficulty Split**: 3 Easy / 6 Medium / 3 Hard
**Answer Types**: 9 `one` / 3 `many` / 0 `none`

---

## Questions

---

### Question 1 — CI Pipeline Expected `check` Block to Block the Deploy

**Difficulty**: Medium
**Answer Type**: one
**Topic**: `check` block assertion failures emit a warning and do not set a non-zero exit code — a failing `check` block never prevents `terraform apply` from completing successfully

**Scenario**:
A platform team adds a `check` block to their Terraform configuration to verify that a newly deployed web application's `/health` endpoint returns HTTP 200 before the pipeline marks the deployment as successful:

```hcl
check "app_health" {
  data "http" "endpoint" {
    url = "https://${aws_lb.web.dns_name}/health"
  }

  assert {
    condition     = data.http.endpoint.status_code == 200
    error_message = "Health endpoint returned ${data.http.endpoint.status_code}, expected 200."
  }
}
```

During a problematic deployment the health endpoint returns HTTP 503, but the CI pipeline still marks the deployment green and Terraform exits with code `0`. The team is surprised — they expected the `check` block to fail the pipeline.

**Question**:
Why did the CI pipeline continue to report success despite the health check failure?

- A) The `check` block only evaluates during `terraform plan`, not `terraform apply` — it never runs after resources are deployed, so the HTTP 503 was not captured
- B) A `check` block assertion failure is a warning, not an error — Terraform prints a warning message to stderr but continues executing and exits with code `0`, so the pipeline's success/failure detection (based on exit code) sees a clean exit
- C) The scoped `data "http"` source inside the `check` block suppresses all HTTP errors — only assertions that reference module-level resources can produce non-zero exit codes
- D) The `check` block requires `depends_on = [aws_lb.web]` inside the assertion block to evaluate after the load balancer is created — without it, the assertion is skipped entirely

**Answer**: B

**Explanation**:
`check` blocks are designed as a non-blocking observability mechanism, not as deployment gates. When a `check` block's `assert` condition evaluates to `false`, Terraform emits a warning message but completes the apply successfully and exits with code `0`. This means CI pipelines that gate on Terraform's exit code will not catch `check` block failures. If a team needs to block a deployment based on a condition, they should use a `precondition` (to block before a resource change) or a `postcondition` (to block after a resource change) — both of which cause Terraform to exit non-zero when their conditions fail.

---

### Question 2 — AMI Architecture Mismatch Detected by `precondition`

**Difficulty**: Medium
**Answer Type**: many
**Topic**: A failing `precondition` prevents the resource change from occurring — the resource is left in its previous state (unchanged or non-existent); the apply fails before the provider makes any API call for that resource

**Scenario**:
A team provisions an EC2 instance and uses a `precondition` to verify the selected AMI is `x86_64` before the instance is created:

```hcl
resource "aws_instance" "web" {
  ami           = data.aws_ami.selected.id
  instance_type = "t3.micro"

  lifecycle {
    precondition {
      condition     = data.aws_ami.selected.architecture == "x86_64"
      error_message = "The selected AMI must be x86_64 architecture, got ${data.aws_ami.selected.architecture}."
    }
  }
}
```

This is a brand-new environment — `aws_instance.web` does not yet exist in state. The data source returns an ARM64 AMI. Running `terraform apply` fails with the precondition error.

**Question**:
Which TWO statements accurately describe the state of the system after the failed apply?

- A) The precondition fires before Terraform makes any API call to create the EC2 instance — `aws_instance.web` is not created in AWS and is not present in the state file
- B) Terraform partially creates the EC2 instance (allocates the instance ID) and then rolls back the creation after the precondition fails — the instance briefly exists in AWS before being deleted
- C) The error message includes the actual architecture value from the data source because `data.aws_ami.selected.architecture` is interpolated directly into the `error_message` string
- D) The apply failure causes Terraform to delete the data source's results from the state file — the next `terraform plan` will re-fetch the AMI information from scratch

**Answer**: A, C

**Explanation**:
**(A)** is correct — a `precondition` is evaluated *before* the resource's create, update, or destroy API call is issued. If it fails, Terraform aborts the operation for that resource without making any infrastructure change. Since the EC2 instance didn't previously exist, it remains absent from both AWS and the state file. **(C)** is correct — the `error_message` in a condition block is a string expression and can interpolate any in-scope values, including the data source attribute that caused the failure. This is useful for producing actionable error messages that show the actual vs. expected value. **(B)** is incorrect — Terraform does not implement rollback of partial resource creation; the precondition prevents the API call entirely. **(D)** is incorrect — data source results are stored in state independently; a precondition failure on a resource does not clear data source state.

---

### Question 3 — Attempt to Use `self` Inside a `precondition`

**Difficulty**: Easy
**Answer Type**: one
**Topic**: `self` is only valid inside `postcondition` blocks, where it references the resource's attributes after the change has been applied — `self` is not available in `precondition` blocks

**Scenario**:
A developer writes a lifecycle block with both a `precondition` and a `postcondition` for an S3 bucket:

```hcl
resource "aws_s3_bucket" "logs" {
  bucket = var.bucket_name

  lifecycle {
    precondition {
      condition     = self.bucket != ""
      error_message = "Bucket name must not be empty."
    }

    postcondition {
      condition     = self.id != ""
      error_message = "Bucket must have a non-empty ID after creation."
    }
  }
}
```

Running `terraform validate` produces an error on the `precondition` block referencing `self`.

**Question**:
Why is `self` invalid inside the `precondition` block?

- A) `self` is not a valid keyword in any Terraform lifecycle block — it is only available inside `provisioner` blocks and is not supported in `precondition` or `postcondition`
- B) `self` references the resource's attributes *after* the create, update, or destroy operation has completed. In a `precondition`, the resource change has not yet happened — there are no post-change attributes to reference, so `self` is meaningless and is not available
- C) `self` is available in both `precondition` and `postcondition`, but it can only reference attributes that are known at plan time — dynamic attributes like `bucket` are not eligible
- D) `self` is only invalid when the resource does not yet exist in state — on a subsequent apply where the resource already exists, `self` would work correctly in a `precondition`

**Answer**: B

**Explanation**:
`self` is a special reference that represents the resource's attributes *after* the change has been applied. It is only valid inside `postcondition` blocks, where the resource has just been created, updated, or destroyed and its resulting attributes are available. In a `precondition`, the resource change hasn't happened yet — there is no "post-change self" to reference. The purpose of a `precondition` is to assert something about the environment *before* the change (typically checking a data source attribute, another resource's attribute, or a variable value). The correct fix is to use `var.bucket_name` instead of `self.bucket` in the precondition condition.

---

### Question 4 — Security Audit Finds DB Password in Plaintext State Despite `sensitive = true`

**Difficulty**: Hard
**Answer Type**: many
**Topic**: `sensitive = true` only masks terminal output — the value is still written as plaintext to `terraform.tfstate`; protecting state requires an encrypted remote backend and strict access controls

**Scenario**:
A security audit scans the team's infrastructure configuration. The auditor notes that the RDS master password is declared as a sensitive variable and the output is also marked sensitive:

```hcl
variable "db_master_password" {
  type      = string
  sensitive = true
}

output "db_password_hint" {
  value     = var.db_master_password
  sensitive = true
}
```

Despite both being marked `sensitive = true`, the auditor finds the actual password value in plaintext inside `terraform.tfstate` stored in the team's S3 bucket. The team lead is confused — they believed `sensitive = true` protected the password.

**Question**:
Which TWO statements accurately explain the audit finding and the corrective actions required?

- A) `sensitive = true` is purely a display-level control — it suppresses the value in `terraform plan`, `terraform apply`, and `terraform output` terminal output, but Terraform always writes resource attribute values (including sensitive ones) to `terraform.tfstate` in plaintext. The `sensitive` flag has no effect on what is stored in state
- B) `sensitive = true` on an output block encrypts the value in `terraform.tfstate` using Terraform's built-in AES encryption — the auditor must have used `terraform state pull` with elevated permissions to bypass the encryption
- C) To protect the password in state, the team should store state in an encrypted remote backend — for example, an S3 bucket with server-side encryption (SSE-KMS) enabled, or HCP Terraform's encrypted state storage — and apply strict IAM policies to restrict who can read the state file
- D) The correct long-term solution is to stop storing the password in Terraform configuration entirely by using the HashiCorp Vault provider to retrieve dynamic credentials at apply time — this prevents the password from ever appearing in the Terraform state file as a static value

**Answer**: A, C

**Explanation**:
**(A)** is correct — `sensitive = true` is a Terraform-level display control only. It prevents the value from being printed in CLI output (plan, apply, and `terraform output`), but it has no effect on state file storage. Terraform writes all resource and variable values to `terraform.tfstate` in plaintext JSON, regardless of sensitivity markings. **(C)** is correct — the standard mitigation is to use an encrypted remote backend. S3 with SSE-KMS ensures the state file is encrypted at rest; HCP Terraform provides managed encrypted state. Additionally, IAM policies should restrict access to the state bucket/object to only the principals that need it. **(B)** is incorrect — Terraform performs no field-level encryption in state files. **(D)** describes a valid and superior architectural approach (Vault dynamic secrets prevent static password storage in state entirely), but the question asks about the audit finding and immediate corrective actions — the most direct and accurate answers are A and C.

---

### Question 5 — Variable Has Two `validation` Blocks; Both Conditions Fail

**Difficulty**: Medium
**Answer Type**: one
**Topic**: When a variable has multiple `validation` blocks, all blocks are evaluated independently and all failures are reported simultaneously — not just the first one

**Scenario**:
A team defines an `instance_type` variable with two separate validation rules: one requiring the value to start with `"t3."` and one requiring the value to be in a specific approved list:

```hcl
variable "instance_type" {
  type = string

  validation {
    condition     = startswith(var.instance_type, "t3.")
    error_message = "Instance type must be in the t3 family."
  }

  validation {
    condition     = contains(["t3.micro", "t3.small", "t3.medium"], var.instance_type)
    error_message = "Instance type must be one of: t3.micro, t3.small, t3.medium."
  }
}
```

A developer passes `-var "instance_type=m5.xlarge"` during a plan. This value fails both validation conditions.

**Question**:
What does Terraform report when both validation conditions fail?

- A) Terraform evaluates validation blocks in order and stops at the first failure — only the error message from the first `validation` block ("Instance type must be in the t3 family.") is displayed
- B) Terraform evaluates all `validation` blocks independently and reports error messages for every block whose `condition` evaluates to `false` — the developer sees both error messages in the same plan failure output
- C) Terraform merges all failing `validation` error messages into a single combined error string separated by semicolons — only one error block appears in the output regardless of how many validations fail
- D) Terraform evaluates both `validation` blocks but only reports the error from the block with the stricter (more specific) condition, determined by the length of the `error_message` string

**Answer**: B

**Explanation**:
Multiple `validation` blocks on a single variable are all evaluated independently and simultaneously. Terraform does not short-circuit on the first failure — it evaluates every `validation` block and collects all failing error messages. When a `terraform plan` fails due to variable validation, every failing `validation` block contributes its `error_message` to the error output. This means the developer sees all validation failures at once, which is intentional: it allows multiple orthogonal rules to be surfaced in a single feedback cycle rather than requiring the user to fix one issue at a time and re-run.

---

### Question 6 — `check` Block Scoped Data Source Returns 503 During `terraform plan`

**Difficulty**: Medium
**Answer Type**: one
**Topic**: A failing scoped `data` source inside a `check` block generates a warning (not an error) and does not abort the plan or apply — unlike top-level `data` source failures which abort the plan

**Scenario**:
A team's Terraform configuration contains a `check` block that uses a scoped `data "http"` source to verify their API gateway is reachable. During a routine `terraform plan` in CI, the API gateway is temporarily unavailable and the HTTP request fails with a connection timeout. The team is debating whether this will cause the plan to fail and block the CI pipeline.

```hcl
check "api_reachable" {
  data "http" "gateway" {
    url = "https://api.example.com/ping"
  }

  assert {
    condition     = data.http.gateway.status_code == 200
    error_message = "API gateway is not reachable (status: ${data.http.gateway.status_code})."
  }
}
```

**Question**:
What happens when the scoped `data "http"` source inside the `check` block fails due to a connection timeout?

- A) The plan fails with a provider error and the CI pipeline receives a non-zero exit code — a failing data source inside a `check` block behaves identically to a failing top-level data source
- B) Because the data source is declared inside a `check` block (not at the top level), its failure is treated as a warning. Terraform emits a warning about the data source error, skips the `assert` evaluation, and the plan/apply continues normally — the CI pipeline receives exit code `0`
- C) A connection timeout inside a `check` block causes Terraform to retry the HTTP request three times before giving up and aborting the plan with a hard error
- D) The scoped data source failure is silently ignored — Terraform does not print any warning or message when a `check` block's embedded data source fails to retrieve data

**Answer**: B

**Explanation**:
A scoped `data` source declared inside a `check` block has different failure semantics from a top-level `data` source. If a top-level `data` source fails (e.g., due to a connection error or API error), the plan/apply is aborted with an error. In contrast, a scoped `data` source inside a `check` block is treated as part of the check's assertion infrastructure: its failure degrades to a warning. Terraform prints a warning indicating the check could not be evaluated due to the data source error, skips the `assert` condition evaluation, and continues with the rest of the plan or apply. The exit code remains `0`. This design deliberately prevents transient infrastructure health issues from blocking Terraform operations.

---

### Question 7 — Colleague Claims `precondition` Has the Same `var`-Only Scope as `validation`

**Difficulty**: Hard
**Answer Type**: one
**Topic**: `precondition` and `postcondition` blocks can reference any in-scope value — data sources, locals, module outputs, other resource attributes — unlike `validation` blocks which are restricted to `var.<name>` only

**Scenario**:
A senior developer reviews a pull request where a teammate has written a `precondition` in an EC2 resource's `lifecycle` block that references a data source attribute:

```hcl
resource "aws_instance" "web" {
  ami           = data.aws_ami.selected.id
  instance_type = var.instance_type

  lifecycle {
    precondition {
      condition     = data.aws_ami.selected.architecture == "x86_64"
      error_message = "Selected AMI must be x86_64 architecture."
    }
  }
}
```

The senior developer comments: "This will fail at plan time because `precondition` has the same restriction as `validation` blocks — you can only reference `var.<name>` in the condition. You need to move this to a validation block and check `var.ami_id` instead."

**Question**:
Is the senior developer's review comment correct?

- A) Yes — `precondition` blocks share the same expression scope restriction as `validation` blocks. Both can only reference `var.<name>` in their `condition` expression; referencing data sources causes a parse error
- B) No — `precondition` and `postcondition` blocks can reference any value that is in scope at the point in the Terraform evaluation where they run, including data source attributes, locals, module outputs, and other resource attributes. Only `variable` `validation` blocks are restricted to `var.<name>`. The pull request code is valid
- C) Yes — `precondition` blocks can reference locals and variables but not data sources, because data sources may not be read until apply time and their values could be unknown during the precondition evaluation
- D) The comment is partially correct — `precondition` can reference data sources, but only data sources declared within the same resource block, not top-level data sources

**Answer**: B

**Explanation**:
The `var.<name>`-only restriction applies exclusively to `variable` `validation` blocks, not to `precondition` or `postcondition` blocks. `precondition` and `postcondition` are evaluated during the apply phase (before and after the resource change, respectively), at which point Terraform has access to data source results, locals, other resource attributes, and module outputs. This broader scope is intentional — `precondition` exists precisely to assert conditions about the environment that may involve queried data, not just raw input variables. The senior developer's review comment is incorrect; the PR code is valid and is the canonical pattern for asserting AMI compatibility before instance creation.

---

### Question 8 — Output Block References Sensitive Variable Without `sensitive = true`

**Difficulty**: Easy
**Answer Type**: one
**Topic**: Terraform raises an error during plan when an output block references a sensitive value (variable, local, or resource attribute) without marking the output block itself as `sensitive = true`

**Scenario**:
A team has a sensitive database password variable and wants to expose a connection string as a Terraform output for use by an application deployment step. They write:

```hcl
variable "db_password" {
  type      = string
  sensitive = true
}

output "connection_string" {
  value = "postgres://admin:${var.db_password}@${aws_db_instance.main.endpoint}/appdb"
}
```

Running `terraform plan` fails immediately before any infrastructure changes are planned.

**Question**:
What error does Terraform produce, and what is the minimal fix?

- A) Terraform errors with `Output refers to sensitive values` — the output block must either add `sensitive = true` to suppress the value in CLI output, or the interpolation must be replaced with a non-sensitive value
- B) Terraform errors with `Sensitive variable cannot be used in string interpolation` — the password must be kept separate from the connection string and passed as an environment variable to the application instead
- C) Terraform errors with `Unknown value in output` — sensitive variables are treated as `(known after apply)` and cannot be referenced in outputs at plan time; they can only be referenced inside resource blocks
- D) Terraform silently replaces `${var.db_password}` with `(sensitive value)` in the output string and proceeds — no error is produced because the interpolation produces a masked string automatically

**Answer**: A

**Explanation**:
When an output block's `value` expression references a sensitive value (any value marked `sensitive = true` — whether a variable, local, or resource attribute), Terraform requires the output block itself to be explicitly marked `sensitive = true`. This is intentional: Terraform forces the author to consciously acknowledge that the output contains sensitive data and opts in to the masking behaviour. The minimal fix is to add `sensitive = true` to the `output "connection_string"` block. After this fix, the connection string will be shown as `(sensitive value)` in terminal output. Note that the actual value will still be stored in plaintext in `terraform.tfstate`.

---

### Question 9 — `nonsensitive()` Used to Demote a Value for a Diagnostic Output

**Difficulty**: Medium
**Answer Type**: one
**Topic**: `nonsensitive()` explicitly removes the sensitive marking from a value, allowing it to appear in plaintext in outputs or expressions — the author takes responsibility for the security implications

**Scenario**:
A platform team stores a Kubernetes cluster CA certificate in Terraform as a sensitive value (because it is a secret). For internal debugging during development, a senior engineer wants to expose the base64-decoded certificate in a Terraform output so the team can quickly inspect it during `terraform output`. The output block:

```hcl
output "cluster_ca_cert_debug" {
  value = nonsensitive(base64decode(data.kubernetes_cluster.main.cluster_ca_certificate))
}
```

A junior developer asks what `nonsensitive()` does here and whether it is safe to use in production.

**Question**:
Which answer correctly explains `nonsensitive()` and when it should be used?

- A) `nonsensitive()` permanently removes the sensitive marking from the source data — after calling `nonsensitive()`, the original `data.kubernetes_cluster.main.cluster_ca_certificate` attribute also loses its sensitive marking throughout the entire configuration
- B) `nonsensitive()` creates a new copy of the value with the sensitive marking removed. The output will display the certificate in plaintext in `terraform output`. The author is explicitly taking responsibility for the security implications — in production environments, this would expose the certificate to anyone who can run `terraform output`, so it should be used only when the team has explicitly accepted that risk
- C) `nonsensitive()` is only valid when called inside `check` block assertions — using it in an `output` block causes a validation error
- D) `nonsensitive()` has no effect on storage — it is equivalent to setting `sensitive = false` on the output block, which is the default, so the function call is redundant

**Answer**: B

**Explanation**:
`nonsensitive(value)` returns a copy of the value without the sensitive marking, allowing it to be used in contexts that would otherwise reject sensitive values (such as an output block without `sensitive = true`). The original source attribute retains its sensitive marking — `nonsensitive()` does not mutate global sensitivity state; it creates an explicitly-unmarked copy for the specific expression. Because the output now lacks the sensitive flag, `terraform output cluster_ca_cert_debug` will print the certificate in plaintext — visible to anyone with access to run `terraform output`. This is appropriate in controlled development/debugging contexts but carries serious risk in production. The function exists for cases where the developer has explicitly assessed the risk and chosen to expose the value.

---

### Question 10 — Vault Dynamic Secrets vs `sensitive = true` for a Long-Lived DB Password

**Difficulty**: Hard
**Answer Type**: many
**Topic**: HashiCorp Vault dynamic secrets prevent static secret storage in state and configuration entirely; `sensitive = true` only masks terminal output but leaves the secret in plaintext state — these are complementary but distinct controls

**Scenario**:
A compliance team reviews two approaches for managing a production database password in Terraform. Approach A uses a `sensitive = true` variable with the password hardcoded in a `.tfvars` file (excluded from version control). Approach B uses the HashiCorp Vault provider to retrieve dynamic credentials at apply time:

```hcl
data "vault_generic_secret" "db_creds" {
  path = "secret/database/prod"
}

resource "aws_db_instance" "main" {
  password = data.vault_generic_secret.db_creds.data["password"]
}
```

The compliance team needs to understand what security guarantees each approach provides.

**Question**:
Which TWO statements accurately describe what the Vault dynamic secrets approach achieves that `sensitive = true` alone cannot?

- A) With the Vault approach, the database password never needs to appear as a static value in the Terraform configuration or in a `.tfvars` file — the password is generated or retrieved by Vault at apply time and is never stored in the source code repository
- B) The Vault approach prevents the database password from being written to `terraform.tfstate` — because the password is not a static Terraform value, it is never recorded in the state file at all
- C) With `sensitive = true` on a variable, the password is stored as an encrypted value in `terraform.tfstate` — the Vault approach and the `sensitive = true` approach provide identical state-level protection
- D) Vault supports secret rotation and dynamic credentials with short TTLs — if Vault is configured to generate short-lived dynamic database credentials, the password retrieved during one apply is different from the one retrieved during the next apply, reducing the blast radius of a credential leak

**Answer**: A, D

**Explanation**:
**(A)** is correct — with the Vault provider approach, the secret never appears as a static literal in any Terraform file. The password is retrieved from Vault's API at apply time. This eliminates the risk of the password accidentally appearing in version control (even in a `.tfvars` file that was supposed to be `.gitignore`d). **(D)** is correct — Vault's dynamic secrets engine can generate short-lived, unique credentials per operation. If these credentials are rotated or expire, the blast radius of a compromise is significantly reduced compared to a long-lived static password. **(B)** is incorrect — the Vault-retrieved secret is still written to `terraform.tfstate` (as a data source result) in plaintext. The Vault approach does not eliminate state file exposure; it eliminates source code exposure. An encrypted remote backend is still required to protect state. **(C)** is incorrect — `sensitive = true` does not encrypt values in state; both approaches leave credentials in plaintext state.

---

### Question 11 — `terraform validate` Does Not Trigger Variable Validation Blocks

**Difficulty**: Medium
**Answer Type**: one
**Topic**: `terraform validate` checks HCL syntax and provider schema correctness — it does not execute variable validation blocks because it does not require variable values to be provided

**Scenario**:
A developer adds a new variable to a Terraform configuration with a `validation` block that restricts allowed values to `["dev", "staging", "production"]`. To test the new validation rule quickly, the developer runs `terraform validate` without providing a value for the variable. The command succeeds with "Success! The configuration is valid." The developer assumes the validation block is broken because it didn't catch anything.

**Question**:
Why did `terraform validate` succeed without triggering the validation block?

- A) `terraform validate` evaluates validation blocks, but only when a `.tfvars` file is present in the working directory — without a `.tfvars` file, validation blocks are silently skipped
- B) `terraform validate` checks only HCL syntax and provider schema correctness. It does not require variable values to be provided and does not evaluate variable `validation` blocks. Validation blocks are evaluated during `terraform plan`, when variable values must be resolved — running `terraform plan -var "environment=invalid_value"` would trigger the validation failure
- C) `terraform validate` triggers validation blocks only for variables that have a `default` value set — variables without defaults are skipped during validation to avoid requiring user input
- D) `terraform validate` is not supported when the configuration has unsatisfied required variables — the command would have failed before reaching the validation block evaluation, which is why the validation failure was not reported

**Answer**: B

**Explanation**:
`terraform validate` performs static analysis of the Terraform configuration: it checks HCL syntax, verifies that resource arguments match the provider schema, and confirms that all references (to locals, variables, resources, and outputs) are structurally valid. It deliberately does not require variable values to be provided and does not evaluate `validation` blocks. This is by design — `terraform validate` is intended to be runnable in environments without access to real variable values (e.g., in a CI step that only has the source code). Variable validation blocks run during `terraform plan`, when all variable values must be resolved. To test a validation block, the developer should run `terraform plan -var "environment=invalid_value"`.

---

### Question 12 — `postcondition` Fails After RDS Instance Is Successfully Created

**Difficulty**: Easy
**Answer Type**: one
**Topic**: A failing `postcondition` means the resource was already created (or changed) by the provider — it exists in AWS and is recorded in state, but the apply is marked as failed

**Scenario**:
A team adds a `postcondition` to an RDS resource to verify the instance status is `"available"` immediately after creation:

```hcl
resource "aws_db_instance" "main" {
  identifier        = "prod-db"
  instance_class    = "db.t3.micro"
  engine            = "mysql"
  engine_version    = "8.0"
  allocated_storage = 20
  username          = "admin"
  password          = var.db_password

  lifecycle {
    postcondition {
      condition     = self.status == "available"
      error_message = "RDS instance status is '${self.status}', expected 'available'."
    }
  }
}
```

Immediately after the provider creates the instance, its status is `"modifying"` (AWS is still applying the initial configuration). The postcondition fails.

**Question**:
What is the state of the RDS instance after the failed apply?

- A) The postcondition failure causes Terraform to issue a `DeleteDBInstance` API call to roll back the creation — the RDS instance is deleted from AWS and removed from state
- B) The RDS instance was already created by the AWS provider API call before the postcondition was evaluated — it exists in AWS and is recorded in `terraform.tfstate`. The apply is marked as failed with the postcondition error message, but the resource is not deleted. The team can re-run `terraform apply` once the instance reaches `"available"` status
- C) The postcondition failure is treated identically to a precondition failure — the resource never reaches a created state and is not recorded in state
- D) The RDS instance exists in AWS but is NOT recorded in `terraform.tfstate` — Terraform only records a resource in state after all its postconditions pass successfully

**Answer**: B

**Explanation**:
A `postcondition` evaluates *after* the resource has been created, updated, or destroyed by the provider. By the time the postcondition runs, the AWS API call to create the RDS instance has already completed — the instance exists in AWS and has been written to `terraform.tfstate`. The postcondition failure marks the apply as failed and surfaces the error message, but it does not trigger any rollback or deletion. The instance remains in state with whatever attributes it has. This is an important distinction from a `precondition` failure (which prevents the API call entirely). The team's next action is typically to wait for the instance to become `"available"` and re-run `terraform apply`, at which point Terraform will re-evaluate the postcondition and, if it passes, mark the apply as successful.

---
