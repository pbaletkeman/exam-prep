# Terraform Associate Exam Questions

---

### Question 1 — Validation Failure Halts Plan Before Infrastructure

**Difficulty**: Easy
**Answer Type**: one
**Topic**: What happens when a variable validation condition fails during terraform plan

**Question**:
A variable is declared with a validation block:

```hcl
variable "environment" {
  type    = string

  validation {
    condition     = contains(["dev", "staging", "production"], var.environment)
    error_message = "environment must be one of: dev, staging, production."
  }
}
```

An engineer runs `terraform apply -var="environment=test"`. What happens?

- A) The apply proceeds but logs a warning about the unrecognised value
- B) Terraform evaluates the plan and fails only when the invalid value reaches a resource argument
- C) Terraform fails before generating any plan and displays: "environment must be one of: dev, staging, production."
- D) The apply succeeds because `"test"` satisfies the `string` type constraint

---

### Question 2 — Failing check Block Assertion Does Not Block Apply

**Difficulty**: Easy
**Answer Type**: one
**Topic**: What happens to terraform apply when a check block assertion evaluates to false

**Question**:
A `check` block asserts that a load balancer's HTTP health endpoint returns status code 200:

```hcl
check "lb_health" {
  data "http" "endpoint" {
    url = "https://${aws_lb.web.dns_name}/health"
  }

  assert {
    condition     = data.http.endpoint.status_code == 200
    error_message = "Health check returned ${data.http.endpoint.status_code}, expected 200."
  }
}
```

During `terraform apply`, all resources are created successfully but the health endpoint returns `503`. What is the exit behaviour of the apply?

- A) The apply exits with a non-zero status code because the `check` assertion failed
- B) Terraform rolls back the resources created during this apply
- C) Terraform displays a warning about the failed assertion and the apply exits successfully
- D) The `aws_lb.web` resource is marked as tainted for replacement on the next run

---

### Question 3 — Precondition Prevents Resource Modification

**Difficulty**: Medium
**Answer Type**: one
**Topic**: State of the resource when a precondition fails during apply

**Question**:
A resource has a `precondition` in its `lifecycle` block:

```hcl
resource "aws_instance" "web" {
  ami           = data.aws_ami.ubuntu.id
  instance_type = var.instance_type

  lifecycle {
    precondition {
      condition     = data.aws_ami.ubuntu.architecture == "x86_64"
      error_message = "The selected AMI must be x86_64 architecture."
    }
  }
}
```

During `terraform apply`, the AMI is resolved as `arm64`. Has the `aws_instance` been created or modified in AWS when the error is reported?

- A) Yes — Terraform creates the instance first and then evaluates the precondition, marking it failed
- B) No — the precondition is evaluated before the resource is changed; no instance is created or modified
- C) The instance is partially provisioned — Terraform starts the API call and rolls back on failure
- D) The instance is created but Terraform removes it from state because the precondition failed

---

### Question 4 — Postcondition Failure: Resource Exists in Cloud and State

**Difficulty**: Medium
**Answer Type**: many
**Topic**: What is true about a resource after its postcondition fails

**Question**:
An `aws_instance` resource has a `postcondition` checking that a public IP was assigned:

```hcl
lifecycle {
  postcondition {
    condition     = self.public_ip != null
    error_message = "Instance must have a public IP address."
  }
}
```

The instance is provisioned in a subnet without auto-assign public IP, so `self.public_ip` is `null`. Which TWO statements are true after `terraform apply` runs? (Select two.)

- A) The `aws_instance` does not exist in AWS — Terraform rolls back resource creation when a postcondition fails
- B) The `aws_instance` exists in AWS with its actual attributes
- C) The `aws_instance` IS recorded in `terraform.tfstate`
- D) The `aws_instance` is NOT recorded in `terraform.tfstate` because the postcondition invalidated the create

---

### Question 5 — Sensitive Variable Redacted in Plan Output

**Difficulty**: Medium
**Answer Type**: one
**Topic**: What terraform plan displays for a sensitive variable value in a resource argument

**Question**:
A variable and resource are declared as:

```hcl
variable "db_password" {
  type      = string
  sensitive = true
}

resource "aws_db_instance" "main" {
  username = "admin"
  password = var.db_password
}
```

`terraform plan` is run. What does the plan output show for the `password` argument of `aws_db_instance.main`?

- A) The actual password value in plaintext
- B) `(known after apply)` — sensitive values are deferred to apply time
- C) `(sensitive value)` — the value is redacted in the plan display
- D) The `password` field is omitted entirely from the plan output

---

### Question 6 — Validation Condition References a Data Source

**Difficulty**: Medium
**Answer Type**: one
**Topic**: What happens when a validation condition references a data source instead of var.<name>

**Question**:
An engineer writes a validation block that references a data source:

```hcl
variable "availability_zone" {
  type = string

  validation {
    condition     = contains(data.aws_availability_zones.available.names, var.availability_zone)
    error_message = "Must be a valid availability zone."
  }
}
```

What happens when `terraform plan` is run with this configuration?

- A) Terraform reads the data source first and then evaluates the validation condition successfully
- B) Terraform raises an error because validation conditions can only reference `var.<variable_name>`
- C) The validation is silently skipped because the data source dependency cannot be resolved at variable evaluation time
- D) Terraform prompts for the data source to be initialised before validation can proceed

---

### Question 7 — Scoped Data Source in check Block Errors

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Effect on terraform apply when a scoped data source inside a check block fails

**Question**:
A `check` block contains a scoped `data "http"` source that makes an HTTP request to a monitoring endpoint. During `terraform apply`, the HTTP request fails with a connection timeout. How does this affect the rest of the apply?

- A) The entire apply is aborted because the `check` block's data source returned an error
- B) Terraform marks the check as failed with a warning and continues applying all other resources normally
- C) The data source failure is silently ignored and the `check` block assertion is treated as passing
- D) Terraform retries the HTTP request three times before failing the entire apply

---

### Question 8 — Consuming Sensitive Output Without Marking It Sensitive

**Difficulty**: Medium
**Answer Type**: one
**Topic**: What happens when a sensitive module output is referenced in an unmarked output block

**Question**:
A child module exposes a sensitive output:

```hcl
# modules/database/outputs.tf
output "db_password" {
  value     = aws_db_instance.main.password
  sensitive = true
}
```

The root module references this output in its own output block **without** marking it sensitive:

```hcl
# root outputs.tf
output "exposed_password" {
  value = module.database.db_password
}
```

What happens when `terraform plan` runs?

- A) Terraform automatically propagates the `sensitive` flag and redacts the value without requiring any change
- B) Terraform raises an error requiring `exposed_password` to also be marked `sensitive = true`
- C) The plan succeeds with a deprecation warning advising the team to add `sensitive = true`
- D) The value is shown in plaintext in the plan output because the root module does not inherit the sensitive flag

---

### Question 9 — check Block Runs During terraform plan

**Difficulty**: Medium
**Answer Type**: one
**Topic**: When check block assertions are evaluated — plan, apply, or both

**Question**:
A configuration contains a `check` block with an `assert` that evaluates to `false` at the time `terraform plan` is run. What does the plan output include?

- A) The plan fails with an error and no proposed changes are shown — the assertion must pass before planning
- B) The plan succeeds; the assertion failure is displayed as a warning alongside the proposed infrastructure changes
- C) The plan output omits the `check` block results — assertions are only evaluated during `terraform apply`
- D) Terraform skips `check` block evaluation during plan if there are pending infrastructure changes

---

### Question 10 — Interactive Prompt Then Validation Evaluation

**Difficulty**: Medium
**Answer Type**: many
**Topic**: Sequence of events when a variable has no default and requires interactive input

**Question**:
A required variable has a validation block but no `default`:

```hcl
variable "environment" {
  type = string

  validation {
    condition     = contains(["dev", "staging", "production"], var.environment)
    error_message = "environment must be one of: dev, staging, production."
  }
}
```

No `.tfvars` file, environment variable, or `-var` flag provides a value. `terraform plan` is run interactively. Which TWO statements correctly describe what Terraform does? (Select two.)

- A) Terraform prompts the user interactively at the terminal to enter a value for `environment`
- B) Terraform fails immediately with the validation error because no value was provided
- C) After the user enters a value, the `validation` condition is evaluated against it
- D) The validation block is permanently skipped when the value comes from an interactive prompt

---

### Question 11 — Precondition Passes, Postcondition Fails

**Difficulty**: Hard
**Answer Type**: one
**Topic**: Final state of a resource after precondition passes and postcondition fails

**Question**:
A resource has both a `precondition` and a `postcondition` in its `lifecycle` block. During `terraform apply`:
1. The `precondition` evaluates to `true` — the resource creation proceeds
2. The resource is successfully created in AWS
3. The `postcondition` evaluates to `false` — the condition is not met

What is the final state of the resource after apply completes?

- A) The resource is destroyed in AWS — Terraform automatically cleans up resources that fail postconditions
- B) The resource exists in AWS and IS recorded in `terraform.tfstate`; the apply exits with a failure status
- C) The resource exists in AWS but is NOT recorded in `terraform.tfstate` — the postcondition failure marks it as unmanaged
- D) The resource is recorded in `terraform.tfstate` as `tainted` so it will be replaced on the next plan

---

### Question 12 — Mixed Sensitive and Non-Sensitive Outputs via terraform output

**Difficulty**: Hard
**Answer Type**: many
**Topic**: What terraform output (no arguments) shows for sensitive vs non-sensitive outputs

**Question**:
A configuration defines two outputs:

```hcl
output "instance_id" {
  value = aws_instance.web.id
}

output "db_password" {
  value     = aws_db_instance.main.password
  sensitive = true
}
```

An engineer runs `terraform output` (with no arguments) after apply. Which TWO statements correctly describe what is displayed? (Select two.)

- A) Both `instance_id` and `db_password` display their actual values
- B) `instance_id` is shown with its actual value
- C) `db_password` is shown as `(sensitive value)` rather than the actual password
- D) All outputs are hidden — `terraform output` without arguments only lists output names, not values

## Answer Key

| Q# | Answer(s) | Explanation | Source | Difficulty |
|----|-----------|-----------:|--------|------------|
| 1 | C | N/A | What happens when a variable validation condition fails during terraform plan | Easy |
| 2 | C | N/A | What happens to terraform apply when a check block assertion evaluates to false | Easy |
| 3 | B | N/A | State of the resource when a precondition fails during apply | Medium |
| 4 | B, C | N/A | What is true about a resource after its postcondition fails | Medium |
| 5 | C | N/A | What terraform plan displays for a sensitive variable value in a resource argument | Medium |
| 6 | B | N/A | What happens when a validation condition references a data source instead of var.<name> | Medium |
| 7 | B | N/A | Effect on terraform apply when a scoped data source inside a check block fails | Medium |
| 8 | B | N/A | What happens when a sensitive module output is referenced in an unmarked output block | Medium |
| 9 | B | N/A | When check block assertions are evaluated — plan, apply, or both | Medium |
| 10 | A, C | N/A | Sequence of events when a variable has no default and requires interactive input | Medium |
| 11 | B | N/A | Final state of a resource after precondition passes and postcondition fails | Hard |
| 12 | B, C | N/A | What terraform output (no arguments) shows for sensitive vs non-sensitive outputs | Hard |
