# Terraform Associate (004) — Question Bank Iter 7 Batch 5

**Iteration**: 7
**Iteration Style**: Fill-in-the-blank / complete the HCL — given a partial configuration or partial statement, select the term or argument that correctly fills the blank
**Batch**: 5
**Objective**: 4b — Variables, Outputs, Types & Functions (prompt06 + prompt07 + prompt08)
**Generated**: 2026-04-25
**Total Questions**: 13
**Difficulty Split**: 3 Easy / 8 Medium / 2 Hard
**Answer Types**: 10 `one` / 3 `many` / 0 `none`

---

## Questions

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

**Answer**: D

**Explanation**:
By default, Terraform variables have `nullable = true` — a caller can explicitly pass `null` to any variable, overriding any `default` value (resulting in `null` being used). Setting `nullable = false` causes Terraform to reject `null` as a supplied value — if a caller passes `null`, Terraform returns a validation error. This is useful for required string or object variables where `null` would cause downstream errors. `required`, `non_null`, and `allow_null` are not valid variable block arguments; `nullable` is the correct argument.

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

**Answer**: D

**Explanation**:
When `count` is used, Terraform exposes `count.index` inside the resource block — a zero-based integer representing which instance is currently being evaluated. For `count = 3`, the three instances have `count.index` values of `0`, `1`, and `2`. Instances are addressed externally as `aws_instance.web[0]`, `aws_instance.web[1]`, and `aws_instance.web[2]`. Interpolating `count.index` into a tag or name is the standard pattern for distinguishing `count`-created instances. `count.number`, `count.position`, and `count.id` are not valid — `count.index` is the only attribute exposed by the `count` object.

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

**Answer**: D

**Explanation**:
Child module outputs are accessed from the parent module using `module.<MODULE_LABEL>.<OUTPUT_NAME>`. The `<MODULE_LABEL>` is the name given in the `module` block declaration — here `"network"`. The full reference is `module.network.public_subnet_id`. This reference also creates an implicit dependency: `aws_instance.web` will not be created until the `module.network` resources have been applied and `public_subnet_id` is known. `network.public_subnet_id` (missing the `module.` prefix), `var.network.public_subnet_id`, and `output.network.public_subnet_id` are all invalid reference formats.

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

**Answer**: D

**Explanation**:
`flatten(list)` takes a list that may contain nested lists (at any depth) and returns a single-level list of all elements. `flatten([["subnet-aaa", "subnet-bbb"], ["subnet-ccc", "subnet-ddd"]])` produces `["subnet-aaa", "subnet-bbb", "subnet-ccc", "subnet-ddd"]`. This is commonly needed when `for` expressions iterate over modules that each output a list, resulting in a list-of-lists. `concat()` joins multiple list *arguments* passed separately — it does not unwrap a pre-existing nested list variable. `merge()` is for maps. `tolist()` converts a set to a list but does not remove nesting.

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

**Answer**: D

**Explanation**:
`compact(list)` returns a new list with all empty strings (`""`) and `null` values removed. It is specifically designed for cleaning up lists that may contain conditionally absent values. `distinct()` removes duplicate values but retains empty strings. `trim()` removes characters from the edges of a single string — it does not operate on lists. `filter()` is not a built-in Terraform function; filtering in Terraform is done with a `for` expression using an `if` condition: `[for v in local.raw_sg_ids : v if v != ""]`. `compact()` is the correct and idiomatic choice for this pattern.

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

**Answer**: D

**Explanation**:
`merge(map1, map2, ...)` combines all provided maps into one. When the same key appears in multiple arguments, the value from the **rightmost (last) argument wins**. Here, `Environment = "unknown"` from `local.default_tags` is overridden by `Environment = var.environment` from `local.env_tags` because `local.env_tags` is the second argument. The result is `{ ManagedBy = "terraform", Environment = <var.environment>, Team = "platform" }`. This makes `merge()` the standard pattern for base-tags-plus-overrides composition. `concat()` joins lists, `zipmap()` creates a map from two separate key/value lists, and `coalesce()` returns the first non-null scalar value from a list of arguments.

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

**Answer**: D

**Explanation**:
`jsonencode(value)` converts any Terraform value — a map, list, object, string, number, or bool — to its JSON string representation. It is the standard way to inline structured data (IAM policies, ECS task definitions, Lambda configurations) directly in HCL without a separate JSON file. The inverse is `jsondecode(str)`, which parses a JSON string back to a Terraform value. `tojson()`, `encode_json()`, and `json()` are not built-in Terraform functions — only `jsonencode()` and `jsondecode()` exist for JSON encoding/decoding.

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

**Answer**: D

**Explanation**:
Inside a `dynamic` block's `content` body, the iterator variable defaults to the **same name as the block type label** — here `ingress`. You reference the current element's value with `ingress.value.<attribute>` and its key with `ingress.key`. This is analogous to `each.value` / `each.key` in a `for_each` resource block, but the variable name is derived from the `dynamic` block's label rather than being fixed as `each`. If the default name is unsuitable, you can override it with the `iterator` argument: adding `iterator = rule` inside the `dynamic` block means you'd write `rule.value.from_port` in `content`. `each`, `self`, and `item` are not the default iterator name — the block type label is.

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

**Answer**: D

**Explanation**:
The splat expression `[*]` extracts a single named attribute from every element of a list resource reference. `aws_instance.web[*].id` is exactly equivalent to `[for r in aws_instance.web : r.id]` — it produces a `list(string)` containing the `id` of each of the three `count`-created instances. Splat expressions work on any `count`-based resource reference (which behaves as a list). They do not work directly on `for_each`-based resources (which produce maps); those require an explicit `for` expression: `[for k, v in aws_instance.server : v.id]`. `[0]` accesses only the first element. `.all` and `[count]` are not valid Terraform expressions.

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

**Answer**: A, C

**Explanation**:
**(A)** `try()` accepts one or more expressions and evaluates them left to right. It returns the value of the first expression that succeeds without a runtime error. If all expressions error, Terraform raises an error. **(C)** A common use case is optional map key access: `try(var.settings["optional_key"], "default_value")`. If the key doesn't exist, the index expression errors, `try()` catches that silently, and returns `"default_value"`. **(B)** is false — `try()` is not a conditional; it does not test truthiness and does not evaluate branches in parallel. It is an error-catching mechanism that evaluates expressions in sequence. **(D)** is false — `try()` works with any Terraform expression type: strings, numbers, booleans, lists, maps, and objects.

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

**Answer**: D

**Explanation**:
`path.module` is the filesystem path of the directory containing the current module's `.tf` files. Using `"${path.module}/user_data.sh.tpl"` ensures the template is found relative to the module that declares it — regardless of where `terraform` is invoked or whether the module is called from a different root. `path.root` refers to the root module's directory, which would break if this code lives in a child module. `path.cwd` is the process working directory at the time `terraform` is run — this changes based on where the CLI is invoked and is unsuitable for module-relative file references. `path.workspace` is not a valid Terraform path variable.

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

**Answer**: D

**Explanation**:
`cidrsubnet(prefix, newbits, netnum)` has three parameters: **prefix** — the base CIDR block; **newbits** — the number of *additional* bits to borrow from the host portion (extending the prefix length by that many bits); **netnum** — the zero-based index of the desired subnet. A `/16` plus 8 borrowed bits produces `/24` subnets (16 + 8 = 24). With `netnum = 1`: subnet 0 = `10.0.0.0/24`, subnet 1 = `10.0.1.0/24`. The answer is `8` (the additional bits to borrow), not `24` (the resulting prefix length). Passing `24` for `newbits` would attempt to borrow 24 bits from a `/16`, creating a `/40` prefix — invalid for IPv4. Passing `16` would produce a `/32`, and `4` would produce a `/20`.

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

**Answer**: A, C

**Explanation**:
**(A)** The `if` clause is an optional filter evaluated per element — elements where the condition is `true` are included, those where it is `false` are skipped. `[for n in var.names : n if length(n) > 4]` produces a list of only the names with more than 4 characters. **(C)** The `if` clause is valid in both list comprehensions (`[for ...]`) and map comprehensions (`{for ... : key => value}`). The example `{for k, v in var.servers : k => v if v != ""}` builds a filtered map. **(B)** is false — the `if` clause is entirely optional; `[for n in var.names : upper(n)]` is a valid `for` expression with no filter. **(D)** is false — `if` clause conditions can freely invoke any built-in Terraform function: `length()`, `contains()`, `startswith()`, `can()`, and others are all permitted inside filter conditions.
