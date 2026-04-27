# Terraform Associate Exam Questions

---

### Question 1 — Validation Block Tries to Reference a Data Source

**Difficulty**: Medium
**Answer Type**: one
**Topic**: `variable` validation `condition` can only reference `var.<name>` — referencing data sources, locals, or other resources causes an error at parse time

**Scenario**:
A platform team wants to restrict deployments to AWS regions where their organisation has approved accounts. They write the following variable block:

```hcl
variable "region" {
  type = string

  validation {
    condition     = contains(data.aws_regions.available.names, var.region)
    error_message = "Region must be one of the approved AWS regions."
  }
}
```

Running `terraform plan` immediately fails before any API calls are made. The team is confused because `data.aws_regions.available` is defined elsewhere in the configuration and works fine outside the validation block.

**Question**:
Why does Terraform reject this validation block?

- A) The `contains()` function is not permitted inside `validation` blocks — only string comparison operators are allowed in `condition` expressions
- B) Validation `condition` expressions can only reference `var.<name>` for the variable being validated. References to data sources, locals, or other resources are not permitted — the validation is evaluated before any infrastructure queries can run
- C) The data source `data.aws_regions.available` must be declared inside the `variable` block for the reference to resolve correctly within the validation scope
- D) Validation blocks do not support multi-argument functions like `contains()` — each condition must be a single boolean expression using comparison operators

---

### Question 2 — Sensitive Output: What It Protects and What It Does Not

**Difficulty**: Medium
**Answer Type**: many
**Topic**: `sensitive = true` on an output masks the value in CLI output but the value remains in plaintext in `terraform.tfstate` — protecting state requires an encrypted remote backend

**Scenario**:
A security review flags that an RDS master password is exposed in Terraform's terminal output during deploys. The team adds `sensitive = true` to the output block:

```hcl
output "db_password" {
  value     = aws_db_instance.main.password
  sensitive = true
}
```

After applying, the team's security officer asks two specific questions: (1) Does this prevent the password from appearing in the terminal during `terraform apply`? (2) Does this encrypt the value in the state file?

**Question**:
Which TWO statements accurately describe what `sensitive = true` on an output block does and does not do?

- A) `sensitive = true` causes the value to appear as `(sensitive value)` in `terraform apply` and `terraform output` CLI output — it does not encrypt or redact the value in `terraform.tfstate`, where it is still stored in plaintext
- B) `sensitive = true` encrypts the output value in `terraform.tfstate` using AES-256, making the state file safe to store in an unencrypted S3 bucket
- C) `sensitive = true` prevents anyone with `terraform output` access from ever retrieving the actual value — the value can only be recovered by re-running `terraform apply`
- D) Even with `sensitive = true`, the actual plaintext value remains accessible in the state file — protecting it from unauthorized access requires storing state in an encrypted remote backend (such as S3 with server-side encryption or HCP Terraform)

---

### Question 3 — CI Pipeline: Which Variable Source Wins?

**Difficulty**: Easy
**Answer Type**: one
**Topic**: CLI `-var` flag takes the highest precedence over all other variable input sources, including `*.auto.tfvars` files

**Scenario**:
A CI/CD pipeline for a multi-environment deployment manages Terraform configuration for both staging and production. The repository contains a `prod.auto.tfvars` file (automatically loaded by Terraform) with `region = "us-east-1"`. A DevOps engineer adds a pipeline override step that passes `-var "region=eu-west-1"` on the `terraform apply` command. Both the auto-loaded file and the CLI flag specify the `region` variable.

**Question**:
Which value does Terraform use for `var.region` during this apply?

- A) `"us-east-1"` — `*.auto.tfvars` files take precedence over CLI flags because they are committed to the repository and represent the declarative source of truth
- B) `"eu-west-1"` — the CLI `-var` flag has the highest precedence of all variable input sources; it overrides `*.auto.tfvars`, `terraform.tfvars`, `-var-file` flags, and environment variables
- C) Terraform errors because the same variable is specified in two sources simultaneously — duplicate variable assignments are not permitted
- D) `"us-east-1"` — `*.auto.tfvars` is processed last in the input chain and therefore takes final precedence

---

### Question 4 — Inline IAM Policy Using `jsonencode()`

**Difficulty**: Medium
**Answer Type**: one
**Topic**: `jsonencode()` converts a Terraform HCL object/map/list to its JSON string representation — commonly used for inline IAM policies and ECS task definitions to avoid a separate `aws_iam_policy_document` data source

**Scenario**:
A team is writing a Terraform configuration that attaches an inline policy to an IAM role. A colleague suggests using a separate `data "aws_iam_policy_document"` block, but the team lead prefers to use `jsonencode()` directly in the resource block to keep everything in a single file. The team lead writes:

```hcl
resource "aws_iam_role_policy" "s3_read" {
  name = "s3-read"
  role = aws_iam_role.lambda.id

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Effect   = "Allow"
      Action   = ["s3:GetObject"]
      Resource = "*"
    }]
  })
}
```

A new team member asks what type of value `jsonencode()` returns and whether the `policy` argument accepts it.

**Question**:
What does `jsonencode()` return, and why is it valid for the `policy` argument?

- A) `jsonencode()` returns an HCL object — the `policy` argument accepts HCL objects natively, so no conversion is needed
- B) `jsonencode()` returns a JSON string — the `policy` argument on `aws_iam_role_policy` expects a JSON-encoded string, making `jsonencode()` the idiomatic way to define inline policies in HCL without a separate data source
- C) `jsonencode()` returns a Terraform map type — it is equivalent to writing `var.policy_map` and is only useful for outputs, not resource arguments
- D) `jsonencode()` returns a Base64-encoded string — this is required because the AWS provider internally base64-encodes IAM policy documents before sending them to the API

---

### Question 5 — Custom Iterator Name in `dynamic` Block Changes Reference Syntax

**Difficulty**: Medium
**Answer Type**: one
**Topic**: When `iterator = <name>` is set in a `dynamic` block, the `content` block must use `<name>.value.*` instead of the default block-type name

**Scenario**:
A team inherits a Terraform configuration that uses a `dynamic "ingress"` block to generate security group rules from a list variable. The original code references `ingress.value.from_port` inside the `content` block. A team member refactors the block by adding `iterator = rule` to make the code more readable:

```hcl
dynamic "ingress" {
  for_each = var.ingress_rules
  iterator = rule

  content {
    from_port   = ingress.value.from_port   # ← still using original name
    to_port     = ingress.value.to_port
    protocol    = ingress.value.protocol
    cidr_blocks = ["0.0.0.0/0"]
  }
}
```

Running `terraform validate` fails. The team member is puzzled because `ingress.value` worked before the `iterator` was added.

**Question**:
What is the cause of the validation failure, and what is the correct fix?

- A) `iterator` is not a valid argument in `dynamic` blocks — it should be removed and the original `ingress.value.*` references restored
- B) Adding `iterator = rule` changes the name of the loop variable inside the `content` block from `ingress` to `rule`. The content references must be updated from `ingress.value.*` to `rule.value.*` — using the old name after setting a custom iterator is invalid
- C) The `iterator` argument requires the same name as the block type — `iterator = ingress` is the only valid assignment, making `iterator = rule` always invalid
- D) The `for_each` in a `dynamic` block must be a set, not a list — the failure is caused by `var.ingress_rules` being a `list(object(...))` rather than a `set(object(...))`

---

### Question 6 — Using `locals` with `merge()` to Centralise Resource Tags

**Difficulty**: Easy
**Answer Type**: one
**Topic**: `local.*` values are internal computed values that centralise reusable expressions within a module — they are not module interface inputs and cannot be overridden by callers

**Scenario**:
A team manages 25 AWS resources in a Terraform module and needs every resource to carry a consistent set of tags including `Environment`, `Team`, and `ManagedBy`. Rather than duplicating the tag map in each resource block, a senior engineer proposes the following approach:

```hcl
locals {
  base_tags = {
    ManagedBy   = "terraform"
    Team        = "platform"
  }

  common_tags = merge(local.base_tags, {
    Environment = var.environment
  })
}
```

Each resource then uses `tags = local.common_tags`. A junior developer asks: "Why use `locals` instead of just adding a `variable` block for `common_tags` so callers can override the whole tag map?"

**Question**:
Which answer best explains why `locals` is the appropriate choice here?

- A) `locals` blocks are evaluated at plan time, while `variable` blocks are only evaluated at apply time — using `locals` makes the tags available earlier in the Terraform execution lifecycle
- B) Locals are internal computed values scoped to the module — they cannot be set by callers, which is correct here because the tag map should be automatically derived from other inputs, not overridden arbitrarily. A `variable` block would expose `common_tags` as part of the module interface, allowing callers to pass in conflicting or incomplete tag maps
- C) Locals must be used instead of variables whenever a `merge()` call is involved — Terraform does not support `merge()` inside variable `default` values
- D) Using a `variable` block for the tag map would cause Terraform to treat each tag as a sensitive value and suppress it in terminal output

---

### Question 7 — `for` Expression with `[...]` Extracts Map Values as a List

**Difficulty**: Medium
**Answer Type**: one
**Topic**: A `for` expression enclosed in `[...]` produces a `list`; enclosing in `{...}` with `key => value` syntax produces a `map` — the outer delimiters determine the output type

**Scenario**:
A team has a Terraform variable that maps server names to instance types:

```hcl
variable "servers" {
  type = map(string)
  default = {
    web = "t3.micro"
    app = "t3.small"
    db  = "t3.medium"
  }
}
```

A developer writes the following local to extract just the instance types for passing to a monitoring module that expects a `list(string)`:

```hcl
locals {
  instance_types = [for k, v in var.servers : v]
}
```

The developer is unsure whether this produces a list or a map.

**Question**:
What type and content does `local.instance_types` hold?

- A) A `map(string)` — the `for` expression iterates over a map, so the result is always a map regardless of the outer delimiters used
- B) A `list(string)` containing the instance type values (e.g., `["t3.micro", "t3.small", "t3.medium"]`) — wrapping a `for` expression in `[...]` always produces a list; the key variable `k` is iterated but not included because the expression only emits `v`
- C) A `set(string)` — Terraform automatically deduplicates the results when a `for` expression iterates over a map's values
- D) An error — iterating a map with two loop variables (`k, v`) is only valid when producing a map output; a list `for` expression must use a single variable

---

### Question 8 — `cidrsubnet` for Three Availability Zone Subnets

**Difficulty**: Hard
**Answer Type**: one
**Topic**: `cidrsubnet(prefix, newbits, netnum)` — `newbits` is additional bits borrowed from the host portion to extend prefix length; `netnum` is zero-based subnet index; `cidrsubnet("10.0.0.0/16", 8, N)` produces a `/24` subnet

**Scenario**:
A network engineer needs to create three subnets — one per availability zone — from a `10.0.0.0/16` VPC CIDR. They want each subnet to be a `/24`. They use `count` and `cidrsubnet()`:

```hcl
resource "aws_subnet" "az" {
  count             = 3
  vpc_id            = aws_vpc.main.id
  cidr_block        = cidrsubnet("10.0.0.0/16", 8, count.index)
  availability_zone = var.availability_zones[count.index]
}
```

A colleague asks: "For `count.index` values of 0, 1, and 2, what CIDRs does this produce?"

**Question**:
Which option correctly lists the three subnet CIDRs produced by `cidrsubnet("10.0.0.0/16", 8, count.index)` for `count.index` = 0, 1, and 2?

- A) `10.0.0.0/16`, `10.0.1.0/16`, `10.0.2.0/16` — `newbits = 8` extends the prefix by 8, but the `/16` base is preserved in the output
- B) `10.0.0.0/8`, `10.0.1.0/8`, `10.0.2.0/8` — `cidrsubnet` with `newbits = 8` subtracts 8 bits from the base prefix to produce larger supernets
- C) `10.0.0.0/24`, `10.0.1.0/24`, `10.0.2.0/24` — `newbits = 8` extends the `/16` prefix by 8 bits to produce `/24` subnets; `netnum` 0, 1, 2 selects the first, second, and third `/24` block within `10.0.0.0/16`
- D) `10.0.0.0/24`, `10.0.8.0/24`, `10.0.16.0/24` — `newbits = 8` shifts the third octet by 8 with each `netnum` increment

---

### Question 9 — `flatten()` to Consolidate Per-AZ Subnet ID Lists from a Module

**Difficulty**: Hard
**Answer Type**: many
**Topic**: `flatten()` recursively unwraps a list-of-lists into a single flat list, preserving order without deduplicating; it differs from `concat()` which joins multiple separate flat lists

**Scenario**:
A team calls a reusable networking module three times — once per availability zone. Each module instance outputs `subnet_ids` as a `list(string)`. The root module collects these in a local:

```hcl
locals {
  all_subnet_ids = [
    module.network_az1.subnet_ids,   # ["subnet-a1", "subnet-a2"]
    module.network_az2.subnet_ids,   # ["subnet-b1"]
    module.network_az3.subnet_ids,   # ["subnet-c1", "subnet-c2"]
  ]
}
```

`local.all_subnet_ids` is currently a `list(list(string))`. They need a flat `list(string)` to pass to an `aws_lb` resource's `subnets` argument, which does not accept nested lists. The team applies `flatten(local.all_subnet_ids)`.

**Question**:
Which TWO statements accurately describe what `flatten()` does in this scenario?

- A) `flatten(local.all_subnet_ids)` produces `["subnet-a1", "subnet-a2", "subnet-b1", "subnet-c1", "subnet-c2"]` — a single flat `list(string)` in the original order, with no deduplication
- B) `flatten()` removes duplicate subnet IDs — if `"subnet-a1"` appeared in both `module.network_az1` and `module.network_az2`, `flatten()` would produce it only once
- C) `flatten()` is distinct from `concat()` in this use case: `concat()` requires separate list arguments (e.g., `concat(module.network_az1.subnet_ids, module.network_az2.subnet_ids, module.network_az3.subnet_ids)`), while `flatten()` operates on a single collection that already contains the nested lists
- D) `flatten()` only unwraps one level of nesting — it cannot handle more than two levels deep, so `list(list(list(string)))` would require multiple nested `flatten()` calls

---

### Question 10 — `nullable = false` Rejects Explicit `null` Even When a Default Exists

**Difficulty**: Medium
**Answer Type**: one
**Topic**: `nullable = false` prevents callers from explicitly passing `null` to override a variable's default — Terraform errors even if a `default` is defined; by contrast the default `nullable = true` permits explicit null overrides

**Scenario**:
A team writes a module with the following variable:

```hcl
variable "log_retention_days" {
  type     = number
  default  = 90
  nullable = false
}
```

A CI system that consumes this module passes all optional variables as explicit `null` to signal "use the default":

```hcl
module "app" {
  source             = "./modules/app"
  log_retention_days = null
}
```

Running `terraform plan` produces an error: `The argument "log_retention_days" is required. The root module input variable "log_retention_days" has its nullable attribute set to "false" which means null values cannot be provided.`

**Question**:
Why does Terraform error even though `default = 90` is set?

- A) Setting `nullable = false` removes the variable's `default` value — once `nullable = false` is set, the variable becomes required and `default` is silently ignored
- B) Terraform errors because variables of type `number` never accept `null` regardless of the `nullable` setting — the error would occur even without `nullable = false`
- C) `nullable = false` prevents callers from explicitly passing `null` to the variable. Normally, passing `null` overrides the `default` (because `null` is a valid explicit value when `nullable = true`). With `nullable = false`, Terraform rejects the explicit `null` assignment — the `default` is only used when the caller provides no value at all, not when they actively pass `null`
- D) The error is caused by a type mismatch: `null` cannot be coerced to `number`, so Terraform errors before evaluating the `nullable` constraint

---

### Question 11 — `try()` to Safely Access an Optional Map Key

**Difficulty**: Medium
**Answer Type**: one
**Topic**: `try(expr, fallback)` returns the fallback value when the primary expression raises a Terraform evaluation error — the idiomatic pattern for optional map keys that may not be present

**Scenario**:
A team writes a configuration that reads application settings from a variable of type `map(string)`. Some deployments include a `"log_level"` key; others omit it. The team wants to use `"info"` as the default log level whenever the key is absent. A developer writes:

```hcl
locals {
  log_level = try(var.app_config["log_level"], "info")
}
```

A colleague suggests replacing this with `lookup(var.app_config, "log_level", "info")`. Both approaches compile without errors.

**Question**:
Which statement correctly explains how `try()` works in this expression, and when `try()` is preferable to `lookup()`?

- A) `try()` and `lookup()` are identical in behaviour — `try()` is simply an alias for `lookup()` introduced in a later Terraform version for readability
- B) `try(var.app_config["log_level"], "info")` evaluates `var.app_config["log_level"]`. If the key does not exist, bracket indexing raises an error, and `try()` catches that error and returns the fallback `"info"`. `try()` is more general than `lookup()` because it can wrap any expression — not just map lookups — making it the preferred pattern when the optional access involves type coercions, attribute traversals, or function calls that might fail
- C) `try()` only catches errors from network calls — it is not designed for map key lookups. Using bracket indexing `[]` with a missing key always returns `null` rather than an error, so `try()` has no effect in this scenario
- D) `try()` evaluates all of its arguments simultaneously and returns the one with the highest non-null type priority — it does not return the first non-erroring expression

---

### Question 12 — `for_each` with a Map: Two True Facts About Instance Addressing

**Difficulty**: Hard
**Answer Type**: many
**Topic**: `for_each` with a map creates resource instances addressed by string key in state; adding or removing an individual key only creates or destroys that specific instance without affecting others

**Scenario**:
A team migrates from `count`-based EC2 instances to `for_each`-based instances using a map variable after experiencing unexpected replacements when server names were reordered. Their new configuration:

```hcl
variable "servers" {
  type = map(string)
  default = {
    web = "t3.micro"
    app = "t3.small"
    db  = "t3.medium"
  }
}

resource "aws_instance" "app" {
  for_each      = var.servers
  ami           = "ami-0abc123"
  instance_type = each.value
  tags          = { Name = each.key }
}
```

After the first successful `terraform apply`, the team later removes the `"app"` key from the map and runs `terraform plan`.

**Question**:
Which TWO statements accurately describe how Terraform handles the `for_each` map in this configuration?

- A) After the initial apply, each instance is tracked in state with a string-key address — `aws_instance.app["web"]`, `aws_instance.app["app"]`, and `aws_instance.app["db"]` — not by numeric index
- B) Removing `"app"` from the map causes Terraform to destroy all three instances and recreate only the two remaining ones, because `for_each` re-evaluates the entire collection on every apply
- C) Removing the `"app"` key from the map causes Terraform to plan the destruction of only `aws_instance.app["app"]` — the `"web"` and `"db"` instances are unaffected because they retain their stable string-key identifiers
- D) `for_each` with a map requires the map values to be unique — if two keys shared the value `"t3.micro"`, Terraform would error and refuse to create the instances

---

### Question 13 — `terraform output -raw` for Shell Variable Assignment in CI

**Difficulty**: Easy
**Answer Type**: one
**Topic**: `terraform output -raw <name>` prints the raw string value without surrounding double quotes — required for clean shell variable assignment in CI scripts

**Scenario**:
A CI pipeline script deploys infrastructure with Terraform and then configures an application using the provisioned RDS endpoint. The script runs:

```bash
DB_ENDPOINT=$(terraform output db_endpoint)
```

When the engineer inspects `$DB_ENDPOINT`, it contains `"mydb.cluster-abc123.us-east-1.rds.amazonaws.com"` — with surrounding double-quote characters included. This causes the subsequent `psql` connection command to fail because the hostname has literal quotes around it.

**Question**:
Which `terraform output` flag resolves this by printing the value without surrounding quotes?

- A) `terraform output --strip-quotes db_endpoint` — the `--strip-quotes` flag is the standard way to remove surrounding quotation marks from string outputs
- B) `terraform output -json db_endpoint | jq -r '.value'` — piping to `jq` with the `-r` flag is the only supported method to extract a raw string from a Terraform output
- C) `terraform output -raw db_endpoint` — the `-raw` flag prints the string value without surrounding quotes or newline padding, making it suitable for direct shell variable assignment
- D) `terraform output -plain db_endpoint` — the `-plain` flag suppresses all formatting including quotes and is the recommended flag for CI pipeline usage

## Answer Key

| Q# | Answer(s) | Explanation | Source | Difficulty |
|----|-----------|-----------:|--------|------------|
| 1 | B | N/A | `variable` validation `condition` can only reference `var.<name>` — referencing data sources, locals, or other resources causes an error at parse time | Medium |
| 2 | A, D | N/A | `sensitive = true` on an output masks the value in CLI output but the value remains in plaintext in `terraform.tfstate` — protecting state requires an encrypted remote backend | Medium |
| 3 | B | N/A | CLI `-var` flag takes the highest precedence over all other variable input sources, including `*.auto.tfvars` files | Easy |
| 4 | B | N/A | `jsonencode()` converts a Terraform HCL object/map/list to its JSON string representation — commonly used for inline IAM policies and ECS task definitions to avoid a separate `aws_iam_policy_document` data source | Medium |
| 5 | B | N/A | When `iterator = <name>` is set in a `dynamic` block, the `content` block must use `<name>.value.*` instead of the default block-type name | Medium |
| 6 | B | N/A | `local.*` values are internal computed values that centralise reusable expressions within a module — they are not module interface inputs and cannot be overridden by callers | Easy |
| 7 | B | N/A | A `for` expression enclosed in `[...]` produces a `list`; enclosing in `{...}` with `key => value` syntax produces a `map` — the outer delimiters determine the output type | Medium |
| 8 | C | N/A | `cidrsubnet(prefix, newbits, netnum)` — `newbits` is additional bits borrowed from the host portion to extend prefix length; `netnum` is zero-based subnet index; `cidrsubnet("10.0.0.0/16", 8, N)` produces a `/24` subnet | Hard |
| 9 | A, C | N/A | `flatten()` recursively unwraps a list-of-lists into a single flat list, preserving order without deduplicating; it differs from `concat()` which joins multiple separate flat lists | Hard |
| 10 | C | N/A | `nullable = false` prevents callers from explicitly passing `null` to override a variable's default — Terraform errors even if a `default` is defined; by contrast the default `nullable = true` permits explicit null overrides | Medium |
| 11 | B | N/A | `try(expr, fallback)` returns the fallback value when the primary expression raises a Terraform evaluation error — the idiomatic pattern for optional map keys that may not be present | Medium |
| 12 | A, C | N/A | `for_each` with a map creates resource instances addressed by string key in state; adding or removing an individual key only creates or destroys that specific instance without affecting others | Hard |
| 13 | C | N/A | `terraform output -raw <name>` prints the raw string value without surrounding double quotes — required for clean shell variable assignment in CI scripts | Easy |
