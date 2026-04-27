# Terraform Associate Exam Questions

---

### Question 1 — Required Variable Not Prompted in CI Pipeline

**Difficulty**: Easy
**Answer Type**: one
**Topic**: Understanding that a required variable (no default) causes a non-interactive failure in CI, not a prompt

**Question**:
An engineer declares a variable with no `default`:

```hcl
variable "db_password" {
  type = string
}
```

Locally, running `terraform apply` prompts them to type the value interactively. In the CI pipeline, the step fails with: `No value for required variable; The root module variable "db_password" is not set`. The engineer expected the same interactive prompt to appear in CI. What explains the difference and how should it be fixed?

- A) CI environments always run Terraform with `-no-prompt`, which is why the prompt is suppressed — remove that flag
- B) The variable must have a `default = ""` to work in CI — required variables are not supported in automated pipelines
- C) Terraform's interactive prompt only appears when running in an **interactive terminal (TTY)**; CI pipelines run in non-interactive mode, so instead of prompting, Terraform errors immediately when a required variable has no value; the fix is to supply the value through a CI-appropriate mechanism — such as setting the `TF_VAR_db_password` environment variable (from a secrets store), passing `-var "db_password=..."` in the apply command, or using a `terraform.tfvars` file injected at pipeline runtime
- D) CI pipelines require all variables to be declared in a `terraform.tfvars` file — environment variables are not supported for CI variable injection

---

### Question 2 — `lookup()` Fails With Error Instead of Returning a Default

**Difficulty**: Easy
**Answer Type**: one
**Topic**: Understanding the correct 3-argument form of lookup() to avoid errors on missing keys

**Question**:
An engineer writes:

```hcl
locals {
  instance_type = lookup(var.instance_types, var.environment)
}
```

When `var.environment = "dr"` and the map does not have a `"dr"` key, Terraform throws: `Error in function call: Call to function "lookup" failed: lookup failed to find key "dr"`. The engineer expected a fallback to a default value. What is wrong and how should it be fixed?

- A) `lookup()` does not support fallback values — use a `try()` block to catch missing key errors
- B) The engineer should use `var.instance_types[var.environment]` instead — direct index access returns `null` on missing keys
- C) The **two-argument form `lookup(map, key)`** throws an error when the key is absent; to provide a fallback, the engineer must use the **three-argument form: `lookup(map, key, default)`** — for example, `lookup(var.instance_types, var.environment, "t3.micro")`; the third argument is returned whenever the specified key is not found in the map, preventing the error
- D) `lookup()` only works on `map(string)` types — if `var.instance_types` is declared as `map(any)`, the function always errors on missing keys

---

### Question 3 — Wrong Variable Value Used When Both `.tfvars` Files Set It

**Difficulty**: Easy
**Answer Type**: one
**Topic**: Understanding that auto.tfvars takes precedence over terraform.tfvars

**Question**:
An engineer has both `terraform.tfvars` (sets `region = "us-east-1"`) and a file named `overrides.auto.tfvars` (sets `region = "eu-west-1"`) in the same directory. They expect `terraform.tfvars` to win because it is the "main" file. Terraform uses `"eu-west-1"`. Why?

- A) Terraform reads `.tfvars` files in alphabetical order and the last value wins — `overrides` comes after `terraform` alphabetically
- B) `terraform.tfvars` is only loaded when no `.auto.tfvars` files are present — the two file types are mutually exclusive
- C) **`*.auto.tfvars` files have higher precedence than `terraform.tfvars`** in Terraform's variable resolution order — any file matching the pattern `*.auto.tfvars` is automatically loaded and takes priority over the manually-loaded `terraform.tfvars`; the engineer's mental model of `terraform.tfvars` as the "most authoritative" file is incorrect; to override an `auto.tfvars` file, the engineer must use a CLI `-var` flag or a `TF_VAR_*` environment variable, both of which rank higher than any `.tfvars` file
- D) Terraform merges values from both files and uses the region declared in `overrides.auto.tfvars` because it was the most recently modified file

---

### Question 4 — `timestamp()` Causes Perpetual Diff on Every Plan

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Understanding why timestamp() in a resource attribute causes Terraform to always show a change

**Question**:
An engineer adds a `last_deployed` tag to all EC2 instances using `timestamp()`:

```hcl
resource "aws_instance" "web" {
  ami           = data.aws_ami.ubuntu.id
  instance_type = "t3.micro"

  tags = {
    Name          = "web"
    LastDeployed  = timestamp()
  }
}
```

Every time `terraform plan` runs — even when nothing else has changed — the plan shows `1 to change` for the `LastDeployed` tag. The engineer cannot understand why. What is the cause?

- A) EC2 tag updates are not idempotent in AWS — any tag with a computed value always triggers an update
- B) `timestamp()` is a non-deterministic function that **returns the current UTC time at the moment `terraform plan` is evaluated** — its value changes on every plan run; Terraform compares the new `timestamp()` value against the value stored in state from the last apply, and since they differ, it always plans an update to the tag; to fix this, the engineer should use `ignore_changes = [tags["LastDeployed"]]` in a `lifecycle` block if they want the tag set once on creation and not updated, or use a static value or a variable for the timestamp if they want it controlled
- C) `timestamp()` is only valid in `locals` blocks — using it directly in a resource attribute is unsupported and the result is undefined
- D) The perpetual diff is caused by the `LastDeployed` key containing uppercase letters — tag keys must be lowercase in Terraform

---

### Question 5 — Validation Condition References a `local` — Error

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Understanding that variable validation conditions can only reference var.<name>, not locals or other resources

**Question**:
An engineer wants to validate that `var.environment` is one of the values in a centrally managed list. They write:

```hcl
locals {
  allowed_envs = ["dev", "staging", "prod"]
}

variable "environment" {
  type = string

  validation {
    condition     = contains(local.allowed_envs, var.environment)
    error_message = "environment must be one of: dev, staging, prod"
  }
}
```

`terraform validate` returns: `A validation condition may only refer to the variable being validated`. What is the cause and fix?

- A) The error is caused by `contains()` not being allowed in validation blocks — use `== "dev" || == "staging"` instead
- B) Locals must be declared after the variable they reference — move the `locals` block below the `variable` block to fix the ordering error
- C) **A `validation` block's `condition` can only reference `var.<name>` — the variable being validated** — it cannot reference `local.*`, other `var.*`, resources, data sources, or any value that requires prior evaluation; the fix is to inline the allowed values list directly in the condition: `contains(["dev", "staging", "prod"], var.environment)`; if the list must be maintained in one place, it should be documented or managed outside Terraform's variable validation
- D) The `local.allowed_envs` reference would work if the locals block were in the same file as the variable — cross-file references are not allowed in validation conditions

---

### Question 6 — `templatefile()` Fails With "File Not Found"

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Using path.module correctly to reference template files relative to the current module

**Question**:
An engineer stores a startup script template at `modules/web/templates/user_data.sh.tpl` and references it in `modules/web/main.tf`:

```hcl
user_data = templatefile("templates/user_data.sh.tpl", {
  app_name = var.app_name
})
```

Running `terraform apply` from the repository root (`/repo`) fails with: `Error: Invalid function argument — No file exists at /repo/templates/user_data.sh.tpl`. What is the cause and fix?

- A) `templatefile()` does not support relative paths — use an absolute path starting with `/`
- B) Template files must be in the root module directory — they cannot be stored inside module subdirectories
- C) The path `"templates/user_data.sh.tpl"` is resolved **relative to the directory where `terraform apply` is run** (the working directory / root module), not relative to the module file containing the call; since the apply is run from `/repo`, Terraform looks for `/repo/templates/user_data.sh.tpl` rather than `/repo/modules/web/templates/user_data.sh.tpl`; the fix is to use `path.module` to anchor the path to the current module: `templatefile("${path.module}/templates/user_data.sh.tpl", {...})`
- D) The `.tpl` extension is not recognised by `templatefile()` — the file must be named with a `.tftpl` extension

---

### Question 7 — `merge()` Silently Overwrites Expected Key

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Understanding that merge() uses last-key-wins when maps share duplicate keys

**Question**:
An engineer merges two tag maps:

```hcl
locals {
  default_tags = {
    Owner       = "platform-team"
    Environment = "production"
  }
  resource_tags = {
    Environment = "staging"
    Service     = "api"
  }
  all_tags = merge(local.default_tags, local.resource_tags)
}
```

The engineer expects `all_tags.Environment` to be `"production"` (from `default_tags`) because it was defined first. Instead it is `"staging"`. What is the cause?

- A) `merge()` errors when two maps share duplicate keys — the engineer should remove the duplicate before calling `merge()`
- B) `merge()` keeps the value from the **first** map when a duplicate key is encountered — the behaviour is correct but the engineer specified the maps in the wrong order
- C) **`merge()` uses last-wins for duplicate keys** — when the same key appears in multiple maps, the value from the **rightmost** (last) map argument overrides all earlier values; `local.resource_tags` is the last argument, so its `Environment = "staging"` overwrites `default_tags`'s `Environment = "production"`; to make `default_tags` win on conflicts, swap the argument order: `merge(local.resource_tags, local.default_tags)`
- D) `merge()` is non-deterministic on duplicate keys — the result depends on internal map iteration order and cannot be relied upon

---

### Question 8 — `cidrsubnet()` Returns Unexpected CIDR Block

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Understanding how cidrsubnet() calculates subnets — newbits and netnum parameters

**Question**:
An engineer calls `cidrsubnet("10.0.0.0/16", 8, 3)` expecting to get the third `/24` subnet. They expect `10.0.3.0/24`. Running `terraform console` confirms this returns `"10.0.3.0/24"`. However, a colleague calls `cidrsubnet("10.0.0.0/16", 4, 3)` and gets `10.0.48.0/20` instead of what the engineer expected. The engineer asks why the colleague's call produces a different result. What explains the difference?

- A) `cidrsubnet()` only works correctly when the base prefix is `/16` or larger — `/4` arguments are invalid
- B) The second argument (`newbits = 4`) adds 4 bits to the base prefix, creating `/20` subnets (not `/24` subnets); `netnum = 3` then selects the **third** `/20` subnet within `10.0.0.0/16` — which starts at `10.0.48.0`; the result is correct: `cidrsubnet("10.0.0.0/16", 4, 3)` computes `/16 + 4 bits = /20`, and the third `/20` block in that space is `10.0.48.0/20`; the engineer's assumption that both calls would produce `/24` subnets is wrong — `newbits` controls the number of **additional bits** borrowed, not the final prefix length
- C) The difference is caused by the two engineers running different versions of Terraform — `cidrsubnet()` changed its calculation method in Terraform 1.5
- D) `cidrsubnet()` requires the third argument (`netnum`) to start at 1, not 0 — the colleague used `3` to get the third subnet, but should have used `2`

---

### Question 9 — `compact()` Does Not Remove Duplicate Values

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Understanding the difference between compact() (removes nulls/empties) and distinct() (removes duplicates)

**Question**:
An engineer has a list with duplicate values and uses `compact()` to remove them:

```hcl
locals {
  regions = compact(["us-east-1", "eu-west-1", "us-east-1", "ap-southeast-1"])
}
```

They expect `local.regions` to contain three unique values, but it still contains four — including the duplicate `"us-east-1"`. What is wrong?

- A) `compact()` only works on lists of numbers — it does not process lists of strings
- B) `compact()` requires `null` values in the list before it can remove anything — it cannot detect string duplicates
- C) **`compact()` removes `null` values and empty strings (`""`) from a list — it does not remove duplicate non-empty values**; to remove duplicates while keeping unique values, the engineer should use `distinct()`: `distinct(["us-east-1", "eu-west-1", "us-east-1", "ap-southeast-1"])` returns `["us-east-1", "eu-west-1", "ap-southeast-1"]`; alternatively, converting to a set with `toset()` also deduplicates (but removes ordering)
- D) There is no built-in Terraform function to remove duplicates from a list — the engineer must use a `for` expression with a filter

---

### Question 10 — Output Exposes a Sensitive Local Without `sensitive = true`

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Understanding that Terraform warns when an output references a sensitive value without marking the output sensitive

**Question**:
An engineer has a local declared as:

```hcl
locals {
  connection_string = "postgresql://admin:${var.db_password}@${aws_db_instance.main.address}:5432/app"
}

output "db_connection" {
  value = local.connection_string
}
```

`var.db_password` is declared with `sensitive = true`. Running `terraform apply` produces an error: `Error: Output refers to sensitive values`. What is the cause and fix?

- A) Sensitive variables cannot be used in locals — the engineer must reference `var.db_password` directly in the output block
- B) `local.connection_string` cannot include interpolation — sensitive variables must be output separately
- C) When an output's `value` expression references a **sensitive value** (directly or transitively via a local or resource attribute), Terraform requires the output to also be **explicitly marked `sensitive = true`**; without this, Terraform errors rather than accidentally exposing the sensitive value; the fix is to add `sensitive = true` to the output block: `output "db_connection" { value = local.connection_string; sensitive = true }`
- D) The error is caused by the local — locals cannot contain sensitive values; the engineer must use a `nonsensitive()` wrapper to strip the sensitivity before assigning to a local

---

### Question 11 — Variable Declared as `type = any` Causes Downstream Type Error

**Difficulty**: Hard
**Answer Type**: many
**Topic**: TWO problems caused by using type = any instead of a specific type constraint

**Question**:
An engineer declares a module variable as `type = any` to avoid dealing with type constraints. A caller passes a `number` where the module internally expects a `string`. Which TWO of the following are consequences of using `type = any` in this scenario? (Select two.)

- A) Terraform rejects `type = any` at `terraform validate` — it is not a valid type constraint
- B) **Type errors are deferred to the point of use** — with `type = any`, Terraform accepts any value the caller provides (number, string, list, etc.) without validation at variable assignment time; the type mismatch is only discovered when the value reaches an argument that requires a specific type (e.g., a resource attribute that requires `string`), producing a potentially confusing error deep in the configuration rather than at the variable boundary
- C) **The calling module gets no documentation signal about what type is expected** — `type = any` removes the self-documenting contract that a specific type constraint provides; callers must inspect the module internals to determine what type is actually needed, increasing integration errors and maintenance burden
- D) `type = any` causes Terraform to silently coerce all input values to strings before they reach the module internals — numeric inputs become their string representation automatically

---

### Question 12 — `for` Expression Filter Produces Empty List Unexpectedly

**Difficulty**: Hard
**Answer Type**: one
**Topic**: Diagnosing a for expression with an if clause that filters out all elements due to a logic error

**Question**:
An engineer writes a `for` expression to extract all production environment names from a map:

```hcl
variable "environments" {
  default = {
    web-prod  = "production"
    web-dev   = "development"
    api-prod  = "production"
    api-stage = "staging"
  }
}

locals {
  prod_names = [for name, env in var.environments : name if env != "production"]
}
```

The engineer expects `local.prod_names` to be `["web-prod", "api-prod"]` but instead gets `["web-dev", "api-stage"]`. What is wrong?

- A) `for` expressions do not support `if` clauses in Terraform — the filter must be done with `compact()` after the expression
- B) Map `for` expressions require `key => value` syntax — the engineer used list syntax and the filter is applied in reverse
- C) The **`if` clause condition is inverted** — `if env != "production"` keeps elements where the environment is **not** production, which is the opposite of the engineer's intent; to keep only production environments, the condition should be `if env == "production"`; the corrected expression is `[for name, env in var.environments : name if env == "production"]`
- D) The expression iterates over map values, not keys — `name` and `env` are swapped, so the filter is comparing the name string against `"production"` rather than the environment value

---

### Question 13 — TWO Things `sensitive = true` on an Output Does and Does Not Protect

**Difficulty**: Hard
**Answer Type**: many
**Topic**: Understanding the precise scope of what output-level sensitive = true protects

**Question**:
Which TWO of the following statements accurately describe the behaviour of `sensitive = true` on an output block? (Select two.)

- A) **`sensitive = true` on an output suppresses the value in `terraform apply` summary output and in the `terraform output` (all-outputs) command, displaying `(sensitive value)` instead** — this prevents the value from appearing accidentally in terminal logs or CI pipeline output
- B) `sensitive = true` on an output encrypts the value before writing it to `terraform.tfstate`, protecting it from anyone with read access to the state file
- C) `sensitive = true` on an output prevents the value from being accessed by a parent module that calls the current module as a child — the output is invisible to callers
- D) **`sensitive = true` on an output does NOT prevent the value from being exposed when queried directly by name (`terraform output <name>`) or via `terraform output -json` — both commands reveal the plaintext value**, meaning the protection is limited to incidental terminal display, not direct programmatic access

## Answer Key

| Q# | Answer(s) | Explanation | Source | Difficulty |
|----|-----------|-----------:|--------|------------|
| 1 | C | N/A | Understanding that a required variable (no default) causes a non-interactive failure in CI, not a prompt | Easy |
| 2 | C | N/A | Understanding the correct 3-argument form of lookup() to avoid errors on missing keys | Easy |
| 3 | C | N/A | Understanding that auto.tfvars takes precedence over terraform.tfvars | Easy |
| 4 | B | N/A | Understanding why timestamp() in a resource attribute causes Terraform to always show a change | Medium |
| 5 | C | N/A | Understanding that variable validation conditions can only reference var.<name>, not locals or other resources | Medium |
| 6 | C | N/A | Using path.module correctly to reference template files relative to the current module | Medium |
| 7 | C | N/A | Understanding that merge() uses last-key-wins when maps share duplicate keys | Medium |
| 8 | B | N/A | Understanding how cidrsubnet() calculates subnets — newbits and netnum parameters | Medium |
| 9 | C | N/A | Understanding the difference between compact() (removes nulls/empties) and distinct() (removes duplicates) | Medium |
| 10 | C | N/A | Understanding that Terraform warns when an output references a sensitive value without marking the output sensitive | Medium |
| 11 | B, C | N/A | TWO problems caused by using type = any instead of a specific type constraint | Hard |
| 12 | C | N/A | Diagnosing a for expression with an if clause that filters out all elements due to a logic error | Hard |
| 13 | A, D | N/A | Understanding the precise scope of what output-level sensitive = true protects | Hard |
