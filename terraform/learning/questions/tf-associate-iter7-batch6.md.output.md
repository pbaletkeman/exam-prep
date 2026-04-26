# Terraform Associate Exam Questions

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

## Answer Key

| Q# | Answer(s) | Explanation | Source | Difficulty |
|----|-----------|-----------:|--------|------------|
| 1 | D | N/A | Which Terraform version introduced the `check` block | Easy |
| 2 | D | N/A | The argument that prevents an output value from appearing in terminal output | Easy |
| 3 | D | N/A | Which keyword references the resource's post-change attributes inside a `postcondition` | Easy |
| 4 | D | N/A | The argument name that provides user feedback when a validation condition fails | Medium |
| 5 | D | N/A | The block type name for asserting prerequisites before a resource is changed | Medium |
| 6 | D | N/A | The top-level block keyword that contains a scoped `data` source and an `assert` block | Medium |
| 7 | D | N/A | Using `can()` inside a `check` block to test whether an attribute expression succeeds | Medium |
| 8 | D | N/A | The function that removes the sensitive marking from a value to allow it in a non-sensitive output | Medium |
| 9 | A, C | N/A | When the check block runs and which Terraform version introduced it | Medium |
| 10 | B, C | N/A | What postcondition self references and how a failing postcondition affects apply | Medium |
| 11 | C | N/A | The correct Vault provider data source type for reading a key-value secret | Hard |
| 12 | B | N/A | Why a postcondition must be used (not a precondition) to verify a newly created resource attribute | Hard |
| 13 | A, C | N/A | What the Vault provider pattern achieves and what it does not protect | Hard |
