# Terraform Associate Exam Questions

---

### Question 1 — Variable Input Precedence

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Order of variable value precedence (highest wins)

**Question**:
A Terraform variable named `region` has a `default` of `"us-east-1"` in its declaration, a value of `"eu-west-1"` in `terraform.tfvars`, and is also set via `TF_VAR_region=ap-southeast-1` in the shell environment. Which value does Terraform use?

- A) `"us-east-1"` — the `default` in the variable block always wins
- B) `"eu-west-1"` — `terraform.tfvars` overrides environment variables
- C) `"ap-southeast-1"` — `TF_VAR_*` environment variables have higher precedence than `.tfvars` files
- D) Terraform raises an error because the variable is set in multiple places

---

### Question 2 — Variable Block Argument: `sensitive`

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Effect of `sensitive = true` on variables vs state

**Question**:
What is the effect of declaring `sensitive = true` on an input variable?

- A) The variable's value is encrypted before being stored in `terraform.tfstate`
- B) The variable's value is hidden in terminal output during `plan` and `apply` but is still stored in plaintext in the state file
- C) The variable's value is excluded from the state file entirely
- D) The variable cannot be passed via environment variables — only via `-var` flag

---

### Question 3 — Validation Block Scope

**Difficulty**: Medium
**Answer Type**: one
**Topic**: What a variable `validation` block can reference

**Question**:
Which of the following expressions is valid inside a variable's `validation` block `condition` argument?

- A) `length(aws_instance.web.id) > 0`
- B) `local.environment != ""`
- C) `contains(["dev", "staging", "prod"], var.environment)`
- D) `data.aws_ami.ubuntu.id != ""`

---

### Question 4 — Locals vs Input Variables

**Difficulty**: Easy
**Answer Type**: one
**Topic**: Difference between `locals` and `variable` blocks

**Question**:
What is the key difference between a `locals` block and a `variable` block in Terraform?

- A) Locals can only hold string values; variables can hold any type
- B) Variables are external inputs that can be set by the caller; locals are internal computed values that cannot be set from outside the module
- C) Locals are shared across all modules in a configuration; variables are scoped to a single module
- D) Variables must always have a `default` value; locals do not require a value expression

---

### Question 5 — Module Output Reference Syntax

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Referencing a child module's output value

**Question**:
A root configuration uses a child module declared as `module "network" { ... }`. The child module has an output named `vpc_id`. What is the correct way to reference this output in the root module?

- A) `network.vpc_id`
- B) `output.network.vpc_id`
- C) `module.network.vpc_id`
- D) `var.network.vpc_id`

---

### Question 6 — `count` vs `for_each` — Preferred Usage

**Difficulty**: Easy
**Answer Type**: one
**Topic**: When to prefer `for_each` over `count`

**Question**:
Why is `for_each` generally preferred over `count` when creating multiple resource instances in Terraform?

- A) `for_each` supports more resource types than `count`
- B) `for_each` uses named keys to identify instances, so removing one item does not force recreation of all subsequent instances
- C) `for_each` is faster to apply because it uses parallel execution; `count` is sequential
- D) `for_each` allows resources to span multiple providers; `count` is limited to a single provider

---

### Question 7 — `count.index` and Splat Expressions

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Accessing `count`-based resource instances

**Question**:
A resource is declared with `count = 3`. What does the splat expression `aws_instance.web[*].id` return?

- A) The ID of the first instance only (`aws_instance.web[0].id`)
- B) A map of index-to-ID pairs: `{ 0 = "i-aaa", 1 = "i-bbb", 2 = "i-ccc" }`
- C) A list containing the `id` attribute of all three instances
- D) An error — splat expressions only work with `for_each`, not `count`

---

### Question 8 — `for_each` with a Set — `each.key` vs `each.value`

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Behaviour of `each.key` and `each.value` when `for_each` uses a set

**Question**:
When `for_each` is assigned a **set** of strings (e.g., `toset(["alice", "bob"])`), what is the relationship between `each.key` and `each.value` inside the resource block?

- A) `each.key` is the zero-based index; `each.value` is the string element
- B) `each.key` and `each.value` are both equal to the set element string
- C) `each.key` is the set element string; `each.value` is always `null` for sets
- D) Sets do not support `each.key` — only `each.value` is available

---

### Question 9 — `for` Expression with Filter

**Difficulty**: Medium
**Answer Type**: one
**Topic**: `for` expression syntax with an `if` filter clause

**Question**:
Which `for` expression correctly produces a list of names from `var.names` that are longer than 4 characters?

- A) `[for name in var.names : name where length(name) > 4]`
- B) `[for name in var.names : name if length(name) > 4]`
- C) `[for name in var.names | length(name) > 4 : name]`
- D) `filter(var.names, n => length(n) > 4)`

---

### Question 10 — `lookup` Function

**Difficulty**: Medium
**Answer Type**: one
**Topic**: `lookup()` function signature and default value

**Question**:
What does `lookup({a = 1, b = 2}, "c", 99)` return?

- A) `null` — the key `"c"` does not exist in the map
- B) An error — `lookup` raises an exception when the key is not found
- C) `99` — the third argument is returned as the default when the key is not found
- D) `0` — `lookup` always returns 0 for missing numeric map entries

---

### Question 11 — `cidrsubnet` Function

**Difficulty**: Hard
**Answer Type**: one
**Topic**: `cidrsubnet()` function parameters and result

**Question**:
What does `cidrsubnet("10.0.0.0/16", 8, 2)` return?

- A) `"10.0.0.0/24"`
- B) `"10.0.1.0/24"`
- C) `"10.0.2.0/24"`
- D) `"10.2.0.0/24"`

---

### Question 12 — `flatten` vs `compact` Functions

**Difficulty**: Hard
**Answer Type**: many
**Topic**: Distinguishing `flatten()` and `compact()` use cases

**Question**:
Which TWO statements correctly describe the difference between `flatten()` and `compact()`? (Select two.)

- A) `flatten(["a", ["b", "c"]])` returns `["a", "b", "c"]` by removing nested list structure
- B) `compact(["a", "", null, "b"])` returns `["a", "b"]` by removing empty strings and null values
- C) `flatten()` removes duplicate values from a flat list
- D) `compact()` recursively unwraps nested lists into a single flat list

---

### Question 13 — `templatefile` vs `file` Functions

**Difficulty**: Medium
**Answer Type**: many
**Topic**: When to use `templatefile()` instead of `file()`

**Question**:
Which TWO statements correctly describe the difference between `file()` and `templatefile()`? (Select two.)

- A) `file(path)` reads the file content as a raw string with no variable substitution
- B) `templatefile(path, vars)` renders the file as a template, substituting `${var_name}` placeholders with values from the `vars` map
- C) `file()` supports `.tpl` template files; `templatefile()` only supports `.txt` files
- D) `templatefile()` can only reference Terraform input variables; it cannot reference locals or computed values

## Answer Key

| Q# | Answer(s) | Explanation | Source | Difficulty |
|----|-----------|-----------:|--------|------------|
| 1 | C | N/A | Order of variable value precedence (highest wins) | Medium |
| 2 | B | N/A | Effect of `sensitive = true` on variables vs state | Medium |
| 3 | C | N/A | What a variable `validation` block can reference | Medium |
| 4 | B | N/A | Difference between `locals` and `variable` blocks | Easy |
| 5 | C | N/A | Referencing a child module's output value | Medium |
| 6 | B | N/A | When to prefer `for_each` over `count` | Easy |
| 7 | C | N/A | Accessing `count`-based resource instances | Medium |
| 8 | B | N/A | Behaviour of `each.key` and `each.value` when `for_each` uses a set | Medium |
| 9 | B | N/A | `for` expression syntax with an `if` filter clause | Medium |
| 10 | C | N/A | `lookup()` function signature and default value | Medium |
| 11 | C | N/A | `cidrsubnet()` function parameters and result | Hard |
| 12 | A, B | N/A | Distinguishing `flatten()` and `compact()` use cases | Hard |
| 13 | A, B | N/A | When to use `templatefile()` instead of `file()` | Medium |
