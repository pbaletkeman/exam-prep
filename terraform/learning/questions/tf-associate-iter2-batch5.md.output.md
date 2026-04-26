# Terraform Associate Exam Questions

---

### Question 1 — -var Flag Overrides auto.tfvars

**Difficulty**: Easy
**Answer Type**: one
**Topic**: What value Terraform uses when the same variable is set in auto.tfvars and via -var

**Question**:
A variable `instance_type` has `default = "t3.micro"` in its declaration. A file named `prod.auto.tfvars` sets `instance_type = "t3.large"`. The engineer runs:

```bash
terraform apply -var="instance_type=t3.xlarge"
```

What value does Terraform use for `instance_type`?

- A) `"t3.micro"` — the `default` in the variable block is the authoritative source
- B) `"t3.large"` — `.auto.tfvars` files override CLI flags
- C) `"t3.xlarge"` — the `-var` flag has the highest precedence and overrides all other sources
- D) Terraform returns an error because the variable is set in multiple places

---

### Question 2 — sensitive = true on an Output

**Difficulty**: Easy
**Answer Type**: one
**Topic**: What terraform output displays for a sensitive output

**Question**:
An output is declared as:

```hcl
output "db_password" {
  value     = aws_db_instance.main.password
  sensitive = true
}
```

An engineer runs `terraform output db_password`. What does the terminal display?

- A) The actual database password in plaintext
- B) `(sensitive value)` — the value is redacted in the terminal
- C) An error: sensitive outputs cannot be queried directly
- D) An empty string — sensitive outputs always return `""`

---

### Question 3 — toset() Removes Duplicates Before for_each

**Difficulty**: Easy
**Answer Type**: one
**Topic**: How many resource instances for_each creates when toset() is applied to a list with duplicates

**Question**:
A resource is declared as:

```hcl
resource "aws_iam_user" "team" {
  for_each = toset(["alice", "bob", "alice", "carol"])
  name     = each.key
}
```

How many IAM user resources does Terraform create?

- A) 4 — Terraform creates one resource per list element, including duplicates
- B) 3 — `toset()` removes the duplicate `"alice"`, leaving `{"alice", "bob", "carol"}`
- C) 1 — `for_each` only creates the first unique value
- D) Terraform returns an error because the input list contains duplicate values

---

### Question 4 — for_each Map Creates Named Addresses

**Difficulty**: Medium
**Answer Type**: one
**Topic**: What resource instance addresses are created in state when for_each uses a map

**Question**:
A resource is declared as:

```hcl
variable "servers" {
  default = {
    web = "t3.micro"
    app = "t3.small"
  }
}

resource "aws_instance" "servers" {
  for_each      = var.servers
  ami           = "ami-0abc123"
  instance_type = each.value
}
```

After `terraform apply`, which resource addresses appear in Terraform state?

- A) `aws_instance.servers[0]` and `aws_instance.servers[1]`
- B) `aws_instance.servers["web"]` and `aws_instance.servers["app"]`
- C) `aws_instance.servers.web` and `aws_instance.servers.app`
- D) `aws_instance.servers` — `for_each` creates a single resource with multiple attributes

---

### Question 5 — count Renumbers on Middle Removal

**Difficulty**: Medium
**Answer Type**: one
**Topic**: What terraform plan shows when the middle element is removed from a count list

**Question**:
A resource is created with `count = length(var.names)` where `var.names = ["alice", "bob", "carol"]`. The index assignments are: `[0]=alice`, `[1]=bob`, `[2]=carol`. The engineer removes `"bob"` from the middle, making `var.names = ["alice", "carol"]`. What does `terraform plan` propose?

- A) Destroy only `aws_iam_user.users[1]` (bob) — the other two are untouched
- B) Destroy `aws_iam_user.users[1]` (bob) and update `aws_iam_user.users[2]` to use `"carol"` shifted to index 1 — effectively destroying and recreating carol's resource
- C) Destroy all three instances and recreate only two
- D) Terraform returns an error because `count` does not allow removing elements

---

### Question 6 — dynamic Block Generates Blocks per Collection Element

**Difficulty**: Medium
**Answer Type**: one
**Topic**: How many nested blocks a dynamic block generates from a 3-element list

**Question**:
A security group resource uses a `dynamic` block:

```hcl
variable "ports" {
  default = [80, 443, 8080]
}

resource "aws_security_group" "web" {
  name = "web-sg"

  dynamic "ingress" {
    for_each = var.ports
    content {
      from_port   = ingress.value
      to_port     = ingress.value
      protocol    = "tcp"
      cidr_blocks = ["0.0.0.0/0"]
    }
  }
}
```

How many `ingress` blocks does Terraform generate for this security group?

- A) 1 — `dynamic` blocks always produce a single merged block
- B) 2 — `dynamic` only iterates over the first two elements
- C) 3 — one `ingress` block is generated per element in `var.ports`
- D) Terraform returns an error because `dynamic` blocks cannot iterate over a list of numbers

---

### Question 7 — merge() Later Key Wins

**Difficulty**: Medium
**Answer Type**: one
**Topic**: What value merge() produces when both maps share the same key

**Question**:
A local is defined as:

```hcl
locals {
  defaults = { environment = "dev", region = "us-east-1", debug = false }
  overrides = { environment = "production", debug = true }
  config = merge(local.defaults, local.overrides)
}
```

What is the value of `local.config`?

- A) `{ environment = "dev", region = "us-east-1", debug = false }` — the first map's values are preserved
- B) `{ environment = "production", region = "us-east-1", debug = true }` — keys from `overrides` win; unique keys from `defaults` are kept
- C) Terraform returns an error because `environment` exists in both maps
- D) `{ environment = "production", region = "us-east-1", debug = false }` — `debug` is not overridden because it is a boolean

---

### Question 8 — Conditional Expression Selects Value

**Difficulty**: Medium
**Answer Type**: one
**Topic**: What value a conditional expression returns based on a variable

**Question**:
A resource is declared with:

```hcl
variable "environment" {
  default = "staging"
}

resource "aws_instance" "app" {
  ami           = "ami-0abc123"
  instance_type = var.environment == "production" ? "t3.large" : "t3.micro"
}
```

`terraform apply` is run without any variable overrides. What `instance_type` is used?

- A) `"t3.large"` — because `environment` has a value and the condition is evaluated
- B) `"t3.micro"` — because `var.environment` is `"staging"`, which does not equal `"production"`
- C) Terraform returns an error because conditional expressions are not allowed in resource arguments
- D) `null` — because `var.environment` has not been explicitly set by the user

---

### Question 9 — try() Returns Fallback When Key Missing

**Difficulty**: Medium
**Answer Type**: one
**Topic**: What try() returns when the primary expression produces an error

**Question**:
A local is defined as:

```hcl
variable "settings" {
  default = { timeout = 30 }
}

locals {
  retry_count = try(var.settings["retry_count"], 3)
}
```

What is the value of `local.retry_count`?

- A) `null` — `try()` returns null when a key is missing
- B) An error — accessing a missing map key in Terraform always raises a fatal error
- C) `3` — `try()` evaluates `var.settings["retry_count"]`, gets an error because the key doesn't exist, and returns the fallback value `3`
- D) `0` — Terraform defaults numeric values to `0` when a key is not found

---

### Question 10 — for Map Comprehension Result

**Difficulty**: Medium
**Answer Type**: many
**Topic**: What a for expression with map output produces

**Question**:
A local is defined as:

```hcl
locals {
  sizes = { web = "t3.micro", app = "t3.small", db = "t3.medium" }
  labels = { for k, v in local.sizes : k => "instance-type: ${v}" }
}
```

Which TWO statements correctly describe `local.labels`? (Select two.)

- A) `local.labels` is a list of strings
- B) `local.labels` is a map where each key matches the original key and each value is a formatted string
- C) `local.labels["web"]` equals `"instance-type: t3.micro"`
- D) `local.labels` contains only one entry because `for` expressions return a single value

---

### Question 11 — nullable = false with No Value Provided

**Difficulty**: Medium
**Answer Type**: one
**Topic**: What happens when nullable = false is set and no value is provided for the variable

**Question**:
A variable is declared as:

```hcl
variable "app_name" {
  type     = string
  nullable = false
}
```

No `default` is provided, no `.tfvars` file sets the variable, and no `-var` flag is passed. `terraform plan` is run. What happens?

- A) Terraform uses `""` (empty string) as the value because `nullable = false` implies a non-null default
- B) Terraform prompts the user interactively for a value
- C) Terraform returns an error because the variable has no default and no value was provided, making it required
- D) Terraform automatically sets the value to `null` because no source provides a value

---

### Question 12 — element() Wraps Around the List

**Difficulty**: Hard
**Answer Type**: one
**Topic**: What element() returns when the index exceeds the list length

**Question**:
The following expression is evaluated in `terraform console`:

```
element(["a", "b", "c"], 4)
```

What does it return?

- A) An error — the index `4` is out of bounds for a 3-element list
- B) `null` — out-of-bounds indices return null in Terraform
- C) `"a"` — `element()` wraps around using modulo, so index 4 mod 3 = 1... wait, 4 mod 3 = 1 → `"b"`
- D) `"b"` — `element()` wraps around the list using modulo arithmetic: `4 mod 3 = 1`, returning the element at index 1

---

### Question 13 — Sensitive Variable Value in Plan Output

**Difficulty**: Hard
**Answer Type**: many
**Topic**: Where a sensitive variable's value is and is not visible

**Question**:
A variable and resource are declared as:

```hcl
variable "api_key" {
  type      = string
  sensitive = true
}

resource "aws_ssm_parameter" "key" {
  name  = "/app/api_key"
  type  = "SecureString"
  value = var.api_key
}
```

`terraform apply` is run. Which TWO statements correctly describe where `var.api_key`'s value appears? (Select two.)

- A) The value is redacted as `(sensitive value)` in the `terraform apply` terminal output
- B) The value is encrypted automatically before being written to the state file
- C) The value is stored in plaintext in `terraform.tfstate` under the resource's attributes
- D) The value is permanently deleted after apply and cannot be retrieved from state

## Answer Key

| Q# | Answer(s) | Explanation | Source | Difficulty |
|----|-----------|-----------:|--------|------------|
| 1 | C | N/A | What value Terraform uses when the same variable is set in auto.tfvars and via -var | Easy |
| 2 | A | N/A | What terraform output displays for a sensitive output | Easy |
| 3 | B | N/A | How many resource instances for_each creates when toset() is applied to a list with duplicates | Easy |
| 4 | B | N/A | What resource instance addresses are created in state when for_each uses a map | Medium |
| 5 | B | N/A | What terraform plan shows when the middle element is removed from a count list | Medium |
| 6 | C | N/A | How many nested blocks a dynamic block generates from a 3-element list | Medium |
| 7 | B | N/A | What value merge() produces when both maps share the same key | Medium |
| 8 | B | N/A | What value a conditional expression returns based on a variable | Medium |
| 9 | C | N/A | What try() returns when the primary expression produces an error | Medium |
| 10 | B, C | N/A | What a for expression with map output produces | Medium |
| 11 | C | N/A | What happens when nullable = false is set and no value is provided for the variable | Medium |
| 12 | D | N/A | What element() returns when the index exceeds the list length | Hard |
| 13 | A, C | N/A | Where a sensitive variable's value is and is not visible | Hard |
