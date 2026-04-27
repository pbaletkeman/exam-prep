# Terraform Associate Exam Questions

---

### Question 1 — `nullable = false` Prevents Null Assignment

**Difficulty**: Easy
**Answer Type**: one
**Topic**: The nullable argument on a variable controls whether callers can explicitly pass null — setting nullable = false makes the variable reject null even though variables accept null by default

**Question**:
A module declares a required string variable and wants to ensure callers can never explicitly pass `null` — even though Terraform variables accept `null` by default. Complete the variable block:

```hcl
variable "environment" {
  type        = string
  description = "Deployment environment"
  ___________ = false
}
```

What argument fills the blank?

- A) `required`
- B) `non_null`
- C) `allow_null`
- D) `nullable`

---

### Question 2 — `count.index` Is Zero-Based

**Difficulty**: Easy
**Answer Type**: one
**Topic**: count.index provides the zero-based position of the current resource instance when the count meta-argument is used

**Question**:
Complete the resource block to tag each EC2 instance with a unique name that includes its zero-based position number:

```hcl
resource "aws_instance" "web" {
  count         = 3
  ami           = "ami-0abc123"
  instance_type = "t3.micro"

  tags = {
    Name = "web-server-${___________}"
  }
}
```

What expression fills the blank?

- A) `count.number`
- B) `count.position`
- C) `count.id`
- D) `count.index`

---

### Question 3 — Referencing a Child Module Output

**Difficulty**: Easy
**Answer Type**: one
**Topic**: A parent module accesses a child module's output using the syntax module.<module_label>.<output_name>

**Question**:
A root configuration calls a child module that exposes an output named `public_subnet_id`. Complete the resource block to use that output as the subnet for an EC2 instance:

```hcl
module "network" {
  source = "./modules/network"
}

resource "aws_instance" "web" {
  ami       = data.aws_ami.ubuntu.id
  subnet_id = ___________
}
```

What expression fills the blank?

- A) `network.public_subnet_id`
- B) `var.network.public_subnet_id`
- C) `output.network.public_subnet_id`
- D) `module.network.public_subnet_id`

---

### Question 4 — `flatten()` Removes Nesting from a List of Lists

**Difficulty**: Medium
**Answer Type**: one
**Topic**: The flatten() function collapses a nested list-of-lists into a single flat list — useful when for expressions or module outputs produce lists of lists

**Question**:
A local value aggregates subnet IDs across two availability zones, producing a list of lists. Complete the local to produce a single flat list:

```hcl
locals {
  nested_ids = [
    ["subnet-aaa", "subnet-bbb"],
    ["subnet-ccc", "subnet-ddd"],
  ]
  all_subnet_ids = ___________(local.nested_ids)
}
```

After evaluation, `local.all_subnet_ids` should be `["subnet-aaa", "subnet-bbb", "subnet-ccc", "subnet-ddd"]`. What function fills the blank?

- A) `concat()`
- B) `merge()`
- C) `tolist()`
- D) `flatten()`

---

### Question 5 — `compact()` Removes Nulls and Empty Strings

**Difficulty**: Medium
**Answer Type**: one
**Topic**: The compact() function removes null values and empty strings from a list — useful for cleaning up optional or conditionally populated lists before using them as resource arguments

**Question**:
A local builds a list of security group IDs where some entries may be empty strings (from conditionally created resources). Complete the local to remove the empty strings:

```hcl
locals {
  raw_sg_ids   = ["sg-aaa", "", "sg-bbb", ""]
  clean_sg_ids = ___________(local.raw_sg_ids)
}
```

After evaluation, `local.clean_sg_ids` should be `["sg-aaa", "sg-bbb"]`. What function fills the blank?

- A) `distinct()`
- B) `trim()`
- C) `filter()`
- D) `compact()`

---

### Question 6 — `merge()` Combines Maps with Later Values Winning

**Difficulty**: Medium
**Answer Type**: one
**Topic**: The merge() function combines multiple maps — when the same key appears in more than one argument, the value from the rightmost (last) argument wins

**Question**:
Complete the local so that the final tags map combines default tags with environment-specific overrides — and when both maps share a key, the environment-specific value takes precedence:

```hcl
locals {
  default_tags = {
    ManagedBy   = "terraform"
    Environment = "unknown"
  }

  env_tags = {
    Environment = var.environment
    Team        = "platform"
  }

  final_tags = ___________(local.default_tags, local.env_tags)
}
```

What function fills the blank so that `Environment` uses `var.environment` instead of `"unknown"`?

- A) `concat()`
- B) `zipmap()`
- C) `coalesce()`
- D) `merge()`

---

### Question 7 — `jsonencode()` Serialises a Value to JSON

**Difficulty**: Medium
**Answer Type**: one
**Topic**: The jsonencode() function converts any Terraform value (map, list, object) to its JSON string representation — commonly used for inline IAM policies and ECS task definitions

**Question**:
An IAM policy document is constructed as a Terraform map and must be serialised to a JSON string for the `policy` argument. Complete the resource block:

```hcl
resource "aws_iam_role_policy" "s3_read" {
  name = "s3-read"
  role = aws_iam_role.app.id

  policy = ___________(
    {
      Version = "2012-10-17"
      Statement = [
        {
          Effect   = "Allow"
          Action   = ["s3:GetObject"]
          Resource = "*"
        }
      ]
    }
  )
}
```

What function fills the blank?

- A) `tojson()`
- B) `encode_json()`
- C) `json()`
- D) `jsonencode()`

---

### Question 8 — `dynamic` Block Iterator Variable Defaults to the Block Type Label

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Inside a dynamic block's content, the iterator variable name defaults to the block type label — used to access each.value and each.key for the current element

**Question**:
A `dynamic` block generates multiple `ingress` rules for a security group. Complete the `content` block to reference the current rule's `from_port`:

```hcl
resource "aws_security_group" "web" {
  name = "web-sg"

  dynamic "ingress" {
    for_each = var.ingress_rules

    content {
      from_port   = ___________.value.from_port
      to_port     = ingress.value.to_port
      protocol    = ingress.value.protocol
      cidr_blocks = ["0.0.0.0/0"]
    }
  }
}
```

What iterator variable name fills the blank?

- A) `each`
- B) `self`
- C) `item`
- D) `ingress`

---

### Question 9 — Splat Expression Extracts an Attribute from Every Instance

**Difficulty**: Medium
**Answer Type**: one
**Topic**: The splat expression [*] extracts the same attribute from every element of a list-type resource reference — it is shorthand for a for expression iterating the list

**Question**:
Three EC2 instances are created with `count = 3`. An output should expose all three instance IDs as a list. Complete the output value:

```hcl
resource "aws_instance" "web" {
  count         = 3
  ami           = "ami-0abc123"
  instance_type = "t3.micro"
}

output "all_instance_ids" {
  value = aws_instance.web___________.id
}
```

What expression fills the blank (inserted between `web` and `.id`) to collect all IDs as a list?

- A) `[0]`
- B) `.all`
- C) `[count]`
- D) `[*]`

---

### Question 10 — TWO Correct Statements About the `try()` Function

**Difficulty**: Medium
**Answer Type**: many
**Topic**: try() evaluates each expression left to right and returns the first one that does not produce an error — it is the idiomatic fallback pattern for optional map keys or absent object attributes

**Question**:
Which TWO of the following statements about the `try()` function are correct? (Select two.)

- A) `try(expr1, expr2, ...)` evaluates each expression left to right and returns the result of the first expression that does not produce an error — if `expr1` errors, Terraform silently tries `expr2`, and so on
- B) `try()` is equivalent to a standard ternary conditional — it evaluates both branches and chooses based on the truthiness of the first argument
- C) `try()` can safely access a potentially absent map key: `try(var.settings["optional_key"], "default_value")` returns `"default_value"` if `"optional_key"` is absent or if accessing it produces any error
- D) `try()` only accepts string expressions — using it with numeric or boolean expressions causes a type error

---

### Question 11 — `templatefile()` Uses `path.module` for Reliable Template Paths

**Difficulty**: Hard
**Answer Type**: one
**Topic**: templatefile(path, vars) renders a file as a template substituting supplied variables — path.module provides the path to the current module directory, ensuring the file is found regardless of where terraform is invoked

**Question**:
A module needs to generate EC2 user data by rendering a shell script template stored in the same directory as the module's `.tf` files. Complete the `user_data` argument:

```hcl
resource "aws_instance" "app" {
  ami           = data.aws_ami.ubuntu.id
  instance_type = "t3.micro"

  user_data = templatefile("${___________}/user_data.sh.tpl", {
    environment = var.environment
    app_name    = local.app_name
  })
}
```

What path variable fills the blank?

- A) `path.root`
- B) `path.cwd`
- C) `path.workspace`
- D) `path.module`

---

### Question 12 — `cidrsubnet()` Arguments: prefix, newbits, netnum

**Difficulty**: Hard
**Answer Type**: one
**Topic**: cidrsubnet(prefix, newbits, netnum) divides a CIDR block into subnets — newbits is the additional bits borrowed from the host portion to extend the prefix length, and netnum is the zero-based subnet index

**Question**:
A VPC uses `10.0.0.0/16`. An engineer wants to compute the second subnet (`netnum = 1`) with a `/24` prefix. Borrowing 8 bits from the host portion of a `/16` produces `/24` subnets. Complete the expression:

```hcl
locals {
  subnet_cidr = cidrsubnet("10.0.0.0/16", ___________, 1)
}
```

What value fills the blank so that `local.subnet_cidr` evaluates to `"10.0.1.0/24"`?

- A) `4`
- B) `16`
- C) `24`
- D) `8`

---

### Question 13 — TWO Correct Statements About `for` Expression `if` Filter Clauses

**Difficulty**: Hard
**Answer Type**: many
**Topic**: A for expression can include an if clause to filter elements — the clause is optional, works in both list and map comprehensions, and can call built-in functions in its condition

**Question**:
Which TWO of the following statements about `for` expressions with `if` filter clauses are correct? (Select two.)

- A) An `if` clause in a `for` expression filters the output — only elements for which the condition is `true` are included: `[for n in var.names : n if length(n) > 4]` returns only names longer than 4 characters
- B) The `if` clause is mandatory in a `for` expression — omitting it causes a validation error because Terraform cannot determine which elements to include
- C) The `if` clause works in both list comprehensions `[for ...]` and map comprehensions `{for ...}` — `{for k, v in var.servers : k => v if v != ""}` is valid and produces a map containing only entries whose value is non-empty
- D) A `for` expression `if` clause can reference variables and locals, but cannot call built-in functions such as `length()`, `contains()`, or `startswith()` — function calls inside `if` clauses are a syntax error

## Answer Key

| Q# | Answer(s) | Explanation | Source | Difficulty |
|----|-----------|-----------:|--------|------------|
| 1 | D | N/A | The nullable argument on a variable controls whether callers can explicitly pass null — setting nullable = false makes the variable reject null even though variables accept null by default | Easy |
| 2 | D | N/A | count.index provides the zero-based position of the current resource instance when the count meta-argument is used | Easy |
| 3 | D | N/A | A parent module accesses a child module's output using the syntax module.<module_label>.<output_name> | Easy |
| 4 | D | N/A | The flatten() function collapses a nested list-of-lists into a single flat list — useful when for expressions or module outputs produce lists of lists | Medium |
| 5 | D | N/A | The compact() function removes null values and empty strings from a list — useful for cleaning up optional or conditionally populated lists before using them as resource arguments | Medium |
| 6 | D | N/A | The merge() function combines multiple maps — when the same key appears in more than one argument, the value from the rightmost (last) argument wins | Medium |
| 7 | D | N/A | The jsonencode() function converts any Terraform value (map, list, object) to its JSON string representation — commonly used for inline IAM policies and ECS task definitions | Medium |
| 8 | D | N/A | Inside a dynamic block's content, the iterator variable name defaults to the block type label — used to access each.value and each.key for the current element | Medium |
| 9 | D | N/A | The splat expression [*] extracts the same attribute from every element of a list-type resource reference — it is shorthand for a for expression iterating the list | Medium |
| 10 | A, C | N/A | try() evaluates each expression left to right and returns the first one that does not produce an error — it is the idiomatic fallback pattern for optional map keys or absent object attributes | Medium |
| 11 | D | N/A | templatefile(path, vars) renders a file as a template substituting supplied variables — path.module provides the path to the current module directory, ensuring the file is found regardless of where terraform is invoked | Hard |
| 12 | D | N/A | cidrsubnet(prefix, newbits, netnum) divides a CIDR block into subnets — newbits is the additional bits borrowed from the host portion to extend the prefix length, and netnum is the zero-based subnet index | Hard |
| 13 | A, C | N/A | A for expression can include an if clause to filter elements — the clause is optional, works in both list and map comprehensions, and can call built-in functions in its condition | Hard |
