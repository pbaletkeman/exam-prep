# Terraform Associate Exam Questions

---

### Question 1 — `locals` String Interpolation Result

**Difficulty**: Easy
**Answer Type**: one
**Topic**: Reading a `locals` block with interpolation to identify the computed string value

**Question**:
Read this `locals` block:

```hcl
locals {
  app_name    = "my-app"
  environment = "production"
  full_name   = "${local.app_name}-${local.environment}"
}
```

What is the value of `local.full_name`?

- A) `"my-app"` — the second interpolation is ignored when locals reference other locals
- B) `"my-app-${local.environment}"` — Terraform does not resolve nested local references
- C) `"my-app-production"` — both local references are resolved and joined with a hyphen
- D) Terraform returns an error because a local cannot reference another local in the same block

---

### Question 2 — `for` Expression: List Brackets vs Map Braces

**Difficulty**: Easy
**Answer Type**: one
**Topic**: Identifying the output type of a `for` expression based on its outer delimiters

**Question**:
Read these two local definitions:

```hcl
locals {
  names    = ["alice", "bob", "carol"]
  result_a = [for n in local.names : upper(n)]
  result_b = {for n in local.names : n => upper(n)}
}
```

What are the types of `local.result_a` and `local.result_b`?

- A) Both are lists — `for` expressions always produce lists regardless of the outer delimiter
- B) `local.result_a` is a list; `local.result_b` is a map — the outer `[...]` vs `{...}` determines the output type
- C) `local.result_a` is a map; `local.result_b` is a list — braces indicate a list in Terraform
- D) Both are maps — Terraform converts all `for` expression outputs to maps for consistency

---

### Question 3 — `zipmap()` Result

**Difficulty**: Easy
**Answer Type**: one
**Topic**: Reading a `zipmap()` call to identify the resulting map

**Question**:
Read this `locals` block:

```hcl
locals {
  keys   = ["us-east-1", "eu-west-1"]
  values = ["prod-east", "prod-west"]
  region_map = zipmap(local.keys, local.values)
}
```

What is the value of `local.region_map`?

- A) `["us-east-1", "prod-east", "eu-west-1", "prod-west"]` — `zipmap` interleaves the two lists
- B) `{ "us-east-1" = "prod-east", "eu-west-1" = "prod-west" }` — the first list provides keys and the second provides values
- C) `{ "prod-east" = "us-east-1", "prod-west" = "eu-west-1" }` — `zipmap` uses the second list as keys
- D) Terraform returns an error because `zipmap` requires both lists to have the same value type

---

### Question 4 — `dynamic` Block with Custom `iterator` Name

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Identifying the correct attribute reference inside a `dynamic` block that uses a custom `iterator` name

**Question**:
Read this resource block:

```hcl
variable "ingress_rules" {
  default = [
    { from_port = 80,  to_port = 80,  protocol = "tcp" },
    { from_port = 443, to_port = 443, protocol = "tcp" },
  ]
}

resource "aws_security_group" "web" {
  name = "web-sg"

  dynamic "ingress" {
    for_each = var.ingress_rules
    iterator = rule

    content {
      from_port   = rule.value.from_port
      to_port     = rule.value.to_port
      protocol    = rule.value.protocol
      cidr_blocks = ["0.0.0.0/0"]
    }
  }
}
```

Inside the `content` block, what does `rule.value.from_port` reference, and why is `ingress.value.from_port` not used instead?

- A) `rule.value.from_port` and `ingress.value.from_port` are identical — both reference the same element; the names are interchangeable
- B) `rule.value.from_port` references the current element's `from_port` because `iterator = rule` overrides the default iterator name (`ingress`); `ingress.value.from_port` would produce an error in this block
- C) `rule` is a reserved keyword in Terraform that automatically references the loop variable regardless of the `iterator` setting
- D) `ingress.value.from_port` should always be used in `content` blocks; `rule` is only valid outside the `dynamic` block

---

### Question 5 — `for` Map Comprehension with Key Transformation

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Reading a map `for` expression that transforms keys to identify the resulting map content

**Question**:
Read this `locals` block:

```hcl
variable "environments" {
  default = {
    dev  = "us-east-1"
    prod = "eu-west-1"
  }
}

locals {
  env_labels = { for k, v in var.environments : upper(k) => v }
}
```

What is the value of `local.env_labels`?

- A) `{ dev = "us-east-1", prod = "eu-west-1" }` — `upper()` has no effect on map keys
- B) `{ DEV = "us-east-1", PROD = "eu-west-1" }` — the `upper(k)` call transforms each key to uppercase while keeping values unchanged
- C) `{ DEV = "US-EAST-1", PROD = "EU-WEST-1" }` — `upper()` is applied to both keys and values
- D) Terraform returns an error because `upper()` cannot be called in the key position of a `for` expression

---

### Question 6 — `cidrhost()` Returns a Host IP

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Reading a `cidrhost()` call to identify the resulting IP address

**Question**:
Read this `locals` block:

```hcl
locals {
  subnet_cidr = "10.0.1.0/24"
  gateway_ip  = cidrhost(local.subnet_cidr, 1)
  broadcast   = cidrhost(local.subnet_cidr, 254)
}
```

What is the value of `local.gateway_ip`?

- A) `"10.0.1.0"` — `cidrhost()` with host number 1 returns the network address
- B) `"10.0.1.1"` — `cidrhost()` adds the host number to the network portion to produce the host address
- C) `"10.0.0.1"` — `cidrhost()` subtracts from the network address
- D) `"10.0.1.0/24"` — `cidrhost()` returns the full CIDR notation, not a bare IP

---

### Question 7 — `concat()` Combines Two Lists

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Reading a `concat()` call to identify the resulting list

**Question**:
Read this `locals` block:

```hcl
locals {
  web_ips = ["10.0.1.10", "10.0.1.11"]
  app_ips = ["10.0.2.10"]
  all_ips = concat(local.web_ips, local.app_ips)
}
```

What is the value of `local.all_ips`?

- A) `["10.0.1.10", "10.0.1.11", "10.0.2.10"]` — `concat()` appends the second list to the first, producing a flat list
- B) `[["10.0.1.10", "10.0.1.11"], ["10.0.2.10"]]` — `concat()` creates a nested list preserving the original structure
- C) `{ web = ["10.0.1.10", "10.0.1.11"], app = ["10.0.2.10"] }` — `concat()` converts the lists to a map
- D) `"10.0.1.10,10.0.1.11,10.0.2.10"` — `concat()` joins the lists into a comma-separated string

---

### Question 8 — `jsonencode()` Output Type

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Reading a `jsonencode()` call to identify the type and structure of the output

**Question**:
Read this `locals` block:

```hcl
locals {
  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Effect   = "Allow"
      Action   = "s3:GetObject"
      Resource = "*"
    }]
  })
}
```

What is the type of `local.policy`, and how is it used in practice?

- A) `object` — `jsonencode()` keeps the input as a structured Terraform object for use in resource arguments
- B) `string` — `jsonencode()` serialises the Terraform object to a JSON-formatted string, suitable for arguments that expect a JSON document
- C) `map(string)` — `jsonencode()` flattens all nested structures into a flat string-to-string map
- D) `list(string)` — `jsonencode()` converts each top-level key into a separate string element

---

### Question 9 — `validation` Block Condition Evaluation

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Reading a `validation` block to determine whether a given input value passes or fails

**Question**:
Read this variable declaration:

```hcl
variable "environment" {
  type = string

  validation {
    condition     = contains(["dev", "staging", "production"], var.environment)
    error_message = "environment must be one of: dev, staging, production."
  }
}
```

An engineer runs `terraform plan -var="environment=test"`. What happens?

- A) The plan proceeds normally — `"test"` is a valid string and satisfies the `type = string` constraint
- B) Terraform evaluates `contains(["dev", "staging", "production"], "test")` as `false` and raises a validation error with the `error_message` before planning begins
- C) The plan proceeds and Terraform issues a warning, but does not fail
- D) Terraform evaluates the condition as `true` because `"test"` is not `null`

---

### Question 10 — `can()` and `try()` on a Missing Map Key

**Difficulty**: Medium
**Answer Type**: many
**Topic**: Reading `can()` and `try()` expressions on a map with a missing key to identify TWO correct results

**Question**:
Read this configuration:

```hcl
variable "config" {
  default = {
    timeout = 30
    region  = "us-east-1"
  }
}

locals {
  has_retry  = can(var.config["retry_count"])
  safe_retry = try(var.config["retry_count"], 5)
}
```

Which TWO statements correctly describe the values of `local.has_retry` and `local.safe_retry`? (Select two.)

- A) `local.has_retry` is `false` — `can()` evaluates the expression and returns `false` because accessing a missing key produces an error
- B) `local.has_retry` is `true` — `can()` returns `true` whenever the variable exists, regardless of its keys
- C) `local.safe_retry` is `5` — `try()` evaluates `var.config["retry_count"]`, gets an error because the key is absent, then returns the fallback value `5`
- D) `local.safe_retry` is `null` — `try()` always returns `null` when the primary expression fails

---

### Question 11 — `for_each` Map: Identifying `each.value` for a Named Key

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Reading a `for_each` resource block with a map variable to identify the attribute value for a specific instance

**Question**:
Read this configuration:

```hcl
variable "instance_sizes" {
  default = {
    web = "t3.micro"
    app = "t3.small"
    db  = "t3.medium"
  }
}

resource "aws_instance" "servers" {
  for_each      = var.instance_sizes
  ami           = "ami-0abc123"
  instance_type = each.value

  tags = {
    Name = each.key
  }
}
```

For the resource instance `aws_instance.servers["app"]`, what is the `instance_type` argument's value?

- A) `"t3.micro"` — `each.value` always returns the first value in the map
- B) `"t3.medium"` — `app` maps to the largest instance type
- C) `"t3.small"` — `each.value` for the `"app"` key resolves to `"t3.small"` from `var.instance_sizes`
- D) `each.key` — `instance_type` takes the key name, not the value

---

### Question 12 — `for` Expression with `if` Filter on a Map

**Difficulty**: Hard
**Answer Type**: many
**Topic**: Reading a `for` list expression with an `if` filter on a map to identify TWO correct statements about the result

**Question**:
Read this `locals` block:

```hcl
variable "users" {
  default = {
    alice = "admin"
    bob   = "viewer"
    carol = "admin"
    dave  = "viewer"
  }
}

locals {
  admins = [for name, role in var.users : name if role == "admin"]
}
```

Which TWO statements correctly describe `local.admins`? (Select two.)

- A) `local.admins` is a **list** — the outer `[...]` delimiter produces a list, not a map
- B) `local.admins` is a **map** — the `for` expression iterates over a map input, so the output is also a map
- C) `local.admins` contains exactly two elements: the names of users whose role equals `"admin"`
- D) `local.admins` contains all four user names — the `if` clause is only advisory and does not exclude elements

---

### Question 13 — `for` Expression with `cidrsubnet()` Applied to Index

**Difficulty**: Hard
**Answer Type**: many
**Topic**: Reading a `for` expression that uses `cidrsubnet()` with the element index to identify TWO correct facts about the resulting list

**Question**:
Read this `locals` block:

```hcl
variable "availability_zones" {
  default = ["us-east-1a", "us-east-1b", "us-east-1c"]
}

locals {
  subnet_cidrs = [for idx, az in var.availability_zones : cidrsubnet("10.0.0.0/16", 8, idx)]
}
```

Which TWO statements correctly describe `local.subnet_cidrs`? (Select two.)

- A) `local.subnet_cidrs` is a list of 3 CIDR strings — one for each availability zone
- B) The first element of `local.subnet_cidrs` is `"10.0.1.0/24"` — `idx` starts at 1 for `for` expressions over lists
- C) The third element of `local.subnet_cidrs` is `"10.0.2.0/24"` — `idx` is 2 for the third element, and `cidrsubnet("10.0.0.0/16", 8, 2)` produces that CIDR
- D) `local.subnet_cidrs` is a map keyed by AZ name — iterating a list with `for idx, az in ...` produces a map

## Answer Key

| Q# | Answer(s) | Explanation | Source | Difficulty |
|----|-----------|-----------:|--------|------------|
| 1 | C | N/A | Reading a `locals` block with interpolation to identify the computed string value | Easy |
| 2 | B | N/A | Identifying the output type of a `for` expression based on its outer delimiters | Easy |
| 3 | B | N/A | Reading a `zipmap()` call to identify the resulting map | Easy |
| 4 | B | N/A | Identifying the correct attribute reference inside a `dynamic` block that uses a custom `iterator` name | Medium |
| 5 | B | N/A | Reading a map `for` expression that transforms keys to identify the resulting map content | Medium |
| 6 | B | N/A | Reading a `cidrhost()` call to identify the resulting IP address | Medium |
| 7 | A | N/A | Reading a `concat()` call to identify the resulting list | Medium |
| 8 | B | N/A | Reading a `jsonencode()` call to identify the type and structure of the output | Medium |
| 9 | B | N/A | Reading a `validation` block to determine whether a given input value passes or fails | Medium |
| 10 | A, C | N/A | Reading `can()` and `try()` expressions on a map with a missing key to identify TWO correct results | Medium |
| 11 | C | N/A | Reading a `for_each` resource block with a map variable to identify the attribute value for a specific instance | Medium |
| 12 | A, C | N/A | Reading a `for` list expression with an `if` filter on a map to identify TWO correct statements about the result | Hard |
| 13 | A, C | N/A | Reading a `for` expression that uses `cidrsubnet()` with the element index to identify TWO correct facts about the resulting list | Hard |
