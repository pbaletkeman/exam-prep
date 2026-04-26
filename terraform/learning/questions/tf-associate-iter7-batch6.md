# Terraform Associate (004) — Question Bank Iter 7 Batch 6

**Iteration**: 7
**Iteration Style**: Fill-in-the-blank / complete the HCL — every question presents a partial HCL snippet or partial statement with a `___________` placeholder; select which option correctly fills the blank
**Batch**: 6
**Objective**: 4c — Custom Conditions & Sensitive Data
**Generated**: 2026-04-25
**Total Questions**: 13
**Difficulty Split**: 3 Easy / 8 Medium / 2 Hard
**Answer Types**: 10 `one` / 3 `many` / 0 `none`

---

## Questions

---

### Question 1 — `check` Block Terraform Version

**Difficulty**: Easy
**Answer Type**: one
**Topic**: Which Terraform version introduced the `check` block

**Question**:
Complete the statement with the correct Terraform version:

> "The `check` block for top-level infrastructure health assertions was introduced in Terraform ___________."

- A) `0.14`
- B) `1.0`
- C) `1.3`
- D) `1.5`

**Answer**: D

**Explanation**:
The `check` block is a relatively recent addition — it shipped in **Terraform 1.5**. Prior to 1.5, Terraform had `validation` blocks (for variables) and `precondition`/`postcondition` blocks (inside `lifecycle`), but no top-level non-blocking assertion mechanism. The `check` block runs on every `plan` and `apply`, optionally contains a scoped `data` source, and produces warnings (not errors) when its `assert` condition fails. Knowing the version is a direct exam fact.

---

### Question 2 — `sensitive = true` on an Output Block

**Difficulty**: Easy
**Answer Type**: one
**Topic**: The argument that prevents an output value from appearing in terminal output

**Question**:
Complete the output block so that the database connection endpoint does not appear in plain text during `terraform apply` or `terraform output`:

```hcl
output "db_connection_string" {
  value       = aws_db_instance.main.endpoint
  description = "Database connection endpoint"
  ___________ = true
}
```

- A) `secret`
- B) `masked`
- C) `redact`
- D) `sensitive`

**Answer**: D

**Explanation**:
The `sensitive` argument is valid on both `variable` and `output` blocks. Setting `sensitive = true` on an output instructs Terraform to show `(sensitive value)` in terminal output, plan summaries, and the default `terraform output` listing instead of the actual value. When a sensitive output is consumed by a parent module, the parent module also treats that value as sensitive. Critically, `sensitive = true` only controls **display** — the value is still stored in plaintext in `terraform.tfstate`. Options A, B, and C (`secret`, `masked`, `redact`) are not valid Terraform arguments.

---

### Question 3 — `self` Keyword Inside a `postcondition`

**Difficulty**: Easy
**Answer Type**: one
**Topic**: Which keyword references the resource's post-change attributes inside a `postcondition`

**Question**:
Complete the `postcondition` condition to verify that the EC2 instance has a public IP address after it is created:

```hcl
resource "aws_instance" "app" {
  ami           = data.aws_ami.ubuntu.id
  instance_type = "t3.micro"

  lifecycle {
    postcondition {
      condition     = ___________.public_ip != null
      error_message = "Instance must have a public IP address."
    }
  }
}
```

- A) `resource`
- B) `this`
- C) `aws_instance`
- D) `self`

**Answer**: D

**Explanation**:
Inside a `postcondition` block, the special keyword `self` refers to the resource that declares the `lifecycle` block — specifically, the resource **as it exists after the change has been applied**. This means `self.public_ip` refers to the newly assigned public IP, `self.id` refers to the just-created resource ID, and so on. `self` is only valid inside `postcondition` — it is not available in `precondition` for referencing the new resource's attributes (since the resource hasn't been created or updated yet when `precondition` runs). Options A, B, and C are not valid references in this context.

---

### Question 4 — `error_message` Argument in a `validation` Block

**Difficulty**: Medium
**Answer Type**: one
**Topic**: The argument name that provides user feedback when a validation condition fails

**Question**:
Complete the `validation` block with the argument that supplies the message Terraform displays when the condition evaluates to `false`:

```hcl
variable "instance_count" {
  type = number

  validation {
    condition     = var.instance_count >= 1 && var.instance_count <= 10
    ___________ = "instance_count must be between 1 and 10."
  }
}
```

- A) `message`
- B) `error`
- C) `fail_message`
- D) `error_message`

**Answer**: D

**Explanation**:
A `validation` block requires exactly two arguments: `condition` (the boolean expression that must be `true` for the value to be valid) and `error_message` (the string Terraform displays when `condition` is `false`). The `error_message` must be a non-empty string and should clearly describe the constraint — for example, what range or set of values is acceptable. Options A (`message`), B (`error`), and C (`fail_message`) are not valid Terraform argument names for this purpose. Note also that the `condition` in this example (`var.instance_count >= 1 && var.instance_count <= 10`) is a valid numeric range check — validation blocks are not limited to string functions.

---

### Question 5 — `precondition` Block Inside `lifecycle`

**Difficulty**: Medium
**Answer Type**: one
**Topic**: The block type name for asserting prerequisites before a resource is changed

**Question**:
An engineer wants to verify that the selected AMI is `x86_64` architecture before creating the EC2 instance. Complete the `lifecycle` block with the correct assertion block type:

```hcl
resource "aws_instance" "web" {
  ami           = data.aws_ami.ubuntu.id
  instance_type = var.instance_type

  lifecycle {
    ___________ {
      condition     = data.aws_ami.ubuntu.architecture == "x86_64"
      error_message = "The selected AMI must be x86_64 architecture."
    }
  }
}
```

- A) `assert`
- B) `validation`
- C) `check`
- D) `precondition`

**Answer**: D

**Explanation**:
`precondition` is the block type used inside a `lifecycle` block to assert conditions that must be true **before** Terraform makes changes to the resource. If the `condition` evaluates to `false`, Terraform halts the apply before touching the resource and displays the `error_message`. The condition can reference `data.*` sources, other resources, input variables, and locals — but not `self` (because the resource hasn't been changed yet). Option A (`assert`) is the block used inside a `check` block. Option B (`validation`) is only valid inside a `variable` block. Option C (`check`) is a top-level block, not a `lifecycle` sub-block.

---

### Question 6 — `check` Block Outer Structure

**Difficulty**: Medium
**Answer Type**: one
**Topic**: The top-level block keyword that contains a scoped `data` source and an `assert` block

**Question**:
Complete the outer block declaration that creates a named health monitor containing a scoped `data` source and an `assert`:

```hcl
___________ "app_health" {
  data "http" "probe" {
    url = "https://${aws_lb.web.dns_name}/health"
  }

  assert {
    condition     = data.http.probe.status_code == 200
    error_message = "Health check returned ${data.http.probe.status_code}, expected 200."
  }
}
```

- A) `lifecycle`
- B) `monitor`
- C) `validation`
- D) `check`

**Answer**: D

**Explanation**:
`check` is the top-level block keyword (introduced in Terraform 1.5) that contains infrastructure health assertions. A `check` block can optionally include a scoped `data` source — the `data` block declared inside a `check` block is **only** evaluated within that `check` block context and is not accessible outside it. The `assert` sub-block contains the `condition` and `error_message`. A failing `assert` inside a `check` block produces a **warning**, not an error — the apply continues and exits with a success code. Options A, B, and C are not valid top-level block types with this structure.

---

### Question 7 — `can()` Function in a `check` Block Assertion

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Using `can()` inside a `check` block to test whether an attribute expression succeeds

**Question**:
Complete the `check` block assertion to verify that the database endpoint can be successfully converted to a string — indicating it has been assigned and is accessible:

```hcl
check "database_accessible" {
  assert {
    condition     = ___________(tostring(aws_db_instance.main.endpoint))
    error_message = "Database endpoint is not accessible or not yet assigned."
  }
}
```

- A) `try()`
- B) `is_valid()`
- C) `coalesce()`
- D) `can()`

**Answer**: D

**Explanation**:
`can(expression)` returns `true` if the expression evaluates without producing an error, and `false` if it throws an error. Wrapping `tostring(aws_db_instance.main.endpoint)` in `can()` tests whether the endpoint attribute is accessible and can be coerced to a string — if the attribute is `null` or the resource failed to provision, the expression would fail and `can()` returns `false`, triggering the assertion message. This pattern is useful inside `check` blocks for non-blocking health checks. Option A (`try()`) returns a fallback value on error — it doesn't return a boolean. Options B and C (`is_valid()`, `coalesce()`) are not the right functions for this purpose.

---

### Question 8 — `nonsensitive()` Function

**Difficulty**: Medium
**Answer Type**: one
**Topic**: The function that removes the sensitive marking from a value to allow it in a non-sensitive output

**Question**:
A variable is marked sensitive, but after a security review the team confirms this particular value is safe to display. Complete the output to explicitly remove the sensitive marking:

```hcl
variable "cluster_name" {
  type      = string
  sensitive = true
}

output "cluster_name_display" {
  value = ___________(var.cluster_name)
}
```

- A) `reveal()`
- B) `plaintext()`
- C) `expose()`
- D) `nonsensitive()`

**Answer**: D

**Explanation**:
`nonsensitive(value)` is a built-in Terraform function that removes the sensitive marking from a value, allowing it to be used in contexts that do not accept sensitive values — such as an output that should be displayed in terminal output without the `(sensitive value)` mask. Without `nonsensitive()`, assigning a sensitive variable to a non-sensitive output would cause Terraform to either propagate the sensitive marking or raise an error. This function should be used cautiously: only call it when you have confirmed that exposing the value is intentional and acceptable. Options A, B, and C (`reveal`, `plaintext`, `expose`) are not Terraform built-in functions.

---

### Question 9 — `check` Block: Version and Execution Timing

**Difficulty**: Medium
**Answer Type**: many
**Topic**: When the check block runs and which Terraform version introduced it

**Question**:
Which **TWO** of the following statements about the `check` block are correct?

- A) The `check` block was introduced in Terraform `1.5`
- B) A failing `check` block `assert` halts `terraform apply` with a non-zero exit code, preventing the deployment from completing
- C) The `check` block runs on every `terraform plan` AND every `terraform apply` — not just on apply
- D) The `check` block can only be declared inside a resource's `lifecycle` block — it is not a top-level block type

**Answer**: A, C

**Explanation**:
Two key exam facts about `check` blocks: (1) it was **introduced in Terraform 1.5** — earlier versions do not support the `check` block syntax; (2) it runs on **both `terraform plan` and `terraform apply`** — not just apply. This makes it useful for surfacing infrastructure health issues during planning, before any changes are applied. Option B is wrong — a failing `check` assertion is a **warning only** and never prevents the apply from completing; the exit code remains 0 (success). Option D is wrong — `check` is a **top-level block** in Terraform configuration, not a sub-block inside `lifecycle`.

---

### Question 10 — `postcondition`: `self` and Failure Behaviour

**Difficulty**: Medium
**Answer Type**: many
**Topic**: What postcondition self references and how a failing postcondition affects apply

**Question**:
Which **TWO** of the following statements about `postcondition` blocks are correct?

- A) A `postcondition` runs **before** the resource is created or modified — if the condition fails, the resource change is prevented
- B) Inside a `postcondition`, the `self` keyword references the resource as it exists **after the change has completed** — including attributes only known after creation, such as `public_ip` or `id`
- C) A failing `postcondition` condition halts the apply **after** the resource has been changed, exits with a non-zero status code, and marks the run as failed
- D) `postcondition` blocks can only reference `var.<name>` values — they cannot use `self` or reference other resource attributes

**Answer**: B, C

**Explanation**:
`postcondition` runs **after** the resource change (option A is wrong — that describes `precondition`). Inside a `postcondition`, `self` refers to the resource in its **post-change state** — all attributes that are computed during creation (such as `public_ip`, `id`, `arn`) are accessible through `self` (option B is correct). If the `condition` evaluates to `false`, Terraform halts the apply, exits with a non-zero status code, and surfaces the `error_message` — the resource has already been created or updated at this point (option C is correct). Option D is incorrect — `postcondition` can freely reference `self`, data sources, locals, and other resources; it is `validation` (not `postcondition`) that is restricted to only `var.<name>`.

---

### Question 11 — Vault Provider Data Source Type

**Difficulty**: Hard
**Answer Type**: one
**Topic**: The correct Vault provider data source type for reading a key-value secret

**Question**:
An engineer uses the HashiCorp Vault provider to dynamically fetch database credentials at apply time. Complete the `data` block with the correct Vault data source type:

```hcl
data "___________" "db_creds" {
  path = "secret/database/prod"
}

resource "aws_db_instance" "main" {
  username = data.db_creds.data["username"]
  password = data.db_creds.data["password"]
}
```

- A) `vault_secret`
- B) `vault_kv_secret`
- C) `vault_generic_secret`
- D) `vault_database_secret`

**Answer**: C

**Explanation**:
`vault_generic_secret` is the Vault provider data source used to read a key-value secret from any Vault secrets engine path. The `path` argument specifies the Vault path, and the `.data` attribute on the resulting object is a map of the key-value pairs stored at that path. This pattern — fetching credentials from Vault at plan/apply time — is a key security improvement over storing secrets in `.tf` files or `.tfvars` files, because the credentials never appear as literals in source-controlled configuration. Options A, B, and D are plausible names but not the correct Vault provider resource type for a generic KV secret.

---

### Question 12 — `precondition` Is the Wrong Tool for Post-Creation Checks

**Difficulty**: Hard
**Answer Type**: one
**Topic**: Why a postcondition must be used (not a precondition) to verify a newly created resource attribute

**Question**:
An engineer writes the following lifecycle block expecting to verify that the EC2 instance has a public IP after creation:

```hcl
resource "aws_instance" "web" {
  ami           = data.aws_ami.ubuntu.id
  instance_type = "t3.micro"

  lifecycle {
    precondition {
      condition     = self.public_ip != null
      error_message = "Instance must have a public IP."
    }
  }
}
```

Why is this the wrong assertion mechanism for this check?

- A) The `precondition` block does not support boolean expressions — it requires a numeric comparison
- B) The `precondition` runs **before** the resource is created or updated — for a brand-new resource, `self.public_ip` will always be `null` at that point because the instance has not been provisioned yet; the correct tool is a `postcondition`, which runs **after** the resource change and where `self` references the resource's newly created attributes
- C) `self` is not a valid reference inside any `lifecycle` block — both `precondition` and `postcondition` must reference other resources by their full resource address
- D) The issue is that `public_ip` is not a valid attribute of `aws_instance` — the correct attribute is `public_ip_address`

**Answer**: B

**Explanation**:
`precondition` runs **before** the resource is created or modified. For a new resource, there is no existing state — `self.public_ip` will always be `null` before provisioning. This means the precondition would always fail for a new resource, which is the opposite of the intended behaviour. The engineer should use a `postcondition` instead: it runs **after** the resource change, `self` references the resource in its newly created state, and a failing condition halts the apply with the error message. The distinction is fundamental: `precondition` = gate before change (check prerequisites); `postcondition` = gate after change (verify the created resource meets expectations). Option C is wrong — `self` is valid in `postcondition`; option D is incorrect attribute naming.

---

### Question 13 — Vault Dynamic Secrets: Two Correct Statements

**Difficulty**: Hard
**Answer Type**: many
**Topic**: What the Vault provider pattern achieves and what it does not protect

**Question**:
Which **TWO** of the following statements about using the HashiCorp Vault provider to supply dynamic secrets to Terraform are correct?

- A) When the `vault_generic_secret` data source is used, Terraform reads credentials from Vault at plan/apply time — the credentials are not stored as literals in any Terraform `.tf` configuration file or `.tfvars` file
- B) Values retrieved from Vault data sources are automatically excluded from `terraform.tfstate` — the Vault integration is specifically designed to prevent secrets from appearing in state
- C) The Vault provider pattern prevents static, long-lived credentials from being embedded in Terraform configuration files — this reduces the risk of secrets being committed to source control
- D) Using the Vault provider means Terraform never stores the retrieved secret values anywhere — neither in state nor in memory during execution

**Answer**: A, C

**Explanation**:
The primary security benefit of the Vault provider pattern is that credentials are **fetched at runtime** (plan/apply), so they never appear as plaintext strings in `.tf` files or `.tfvars` files — reducing the risk of accidental source-control commits of secrets (options A and C are correct). However, option B is **wrong**: values retrieved from `data` sources, including Vault secrets, **are stored in `terraform.tfstate`** in plaintext — Vault does not make state storage exempt from this. Option D is also **wrong**: Terraform stores all resource and data source attribute values in state, and values are held in memory during execution. The mitigation for state exposure is still required: encrypted remote backends, restricted IAM/RBAC on the state file, and never committing `.tfstate` to source control.
