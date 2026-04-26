---
iteration: 8
batch: 5
style: "Ordering / sequencing"
style_note: >
  Every question presents a workflow, lifecycle, or list of steps and asks the
  candidate to identify the correct order, which step comes first or last, or
  which option correctly sequences a process.
topics:
  - Variables, Locals & Outputs (Objective 4 — prompt06)
  - Complex Types & Collections (Objective 4 — prompt07)
  - Built-in Functions & Expressions (Objective 4 — prompt08)
sources:
  - prompt06-variables-locals-outputs.md
  - prompt07-complex-types-collections.md
  - prompt08-builtin-functions-expressions.md
question_count: 13
difficulty_split: "3 Easy / 8 Medium / 2 Hard"
answer_type_split: "10 one / 3 many"
---

# Terraform Associate (004) — Iteration 8 · Batch 5
## Variables, Outputs, Types & Functions · Ordering / Sequencing

---

### Question 1

**Difficulty:** Easy
**Answer Type:** one
**Topic:** `merge()` argument ordering — which map's value wins when keys conflict

An engineer writes the following local:

```hcl
locals {
  config = merge(
    { instance_type = "t3.micro", region = "us-east-1" },
    { instance_type = "t3.large", env = "prod" }
  )
}
```

Both maps contain the key `instance_type`. Which value does `local.config.instance_type` hold, and why?

A) `"t3.micro"` — the FIRST argument in `merge()` has priority; later arguments can only add new keys, not override existing ones
B) Terraform returns an error — duplicate keys across merged maps are not allowed
C) `"t3.large"` — when `merge()` encounters a key that exists in multiple maps, the value from the LAST argument containing that key overwrites all earlier values; maps are applied left to right and the rightmost map wins any conflict
D) The result is undefined — `merge()` does not guarantee which value wins for duplicate keys

**Answer:** C

**Explanation:** `merge()` applies its map arguments left to right. For any key present in more than one argument, the value from the LAST (rightmost) argument containing that key overwrites the earlier value. In this example, `instance_type = "t3.micro"` is set by the first argument, then immediately overwritten by `instance_type = "t3.large"` from the second argument. The final map is `{ instance_type = "t3.large", region = "us-east-1", env = "prod" }`. This left-to-right override ordering means the calling code controls which values take precedence by controlling the argument order — placing a more-specific map after a more-general "defaults" map is a common pattern.

---

### Question 2

**Difficulty:** Easy
**Answer Type:** one
**Topic:** `flatten()` recursive unwrapping — sequence of operations and result

An engineer evaluates the following in `terraform console`:

```hcl
flatten(["a", ["b", "c"], ["d", ["e", "f"]]])
```

Which of the following correctly describes the sequence of operations and the final result?

A) `flatten()` only removes one level of nesting; the result is `["a", ["b","c"], ["d",["e","f"]]]` — identical to the input
B) `flatten()` reverses the list first, then removes nesting; the result is `["f","e","d","c","b","a"]`
C) `flatten()` recursively unwraps all levels of nested lists into a single flat list, processing outer elements first and inner elements in their original order; the result is `["a", "b", "c", "d", "e", "f"]`
D) `flatten()` raises an error when it encounters lists nested more than two levels deep

**Answer:** C

**Explanation:** `flatten()` recursively removes ALL levels of nesting — not just one level. It traverses the structure, processing each element in order: scalar elements are added directly; list elements are unwrapped and their contents processed recursively. The traversal preserves left-to-right, outer-to-inner order: `"a"` (scalar, added directly) → `["b","c"]` unwrapped to `"b"`, `"c"` → `["d",["e","f"]]` unwrapped: `"d"` added, then `["e","f"]` unwrapped to `"e"`, `"f"`. Final result: `["a","b","c","d","e","f"]`. This is useful for flattening the output of `for` expressions that produce lists of lists, such as when generating multiple security group rules from a nested variable.

---

### Question 3

**Difficulty:** Easy
**Answer Type:** many
**Topic:** `compact()` and `distinct()` — processing order and which occurrence is preserved

Which TWO of the following correctly describe how `compact()` and `distinct()` process their input lists in order?

A) `compact(["a", "", "b", null, "c"])` processes the list LEFT TO RIGHT and removes all empty strings and `null` values while preserving the relative order of retained elements — the result is `["a", "b", "c"]`
B) `compact()` sorts the list alphabetically before removing empty strings and nulls — the result order is determined by sorted position, not original position
C) `distinct(["a", "b", "a", "c", "b"])` processes the list LEFT TO RIGHT and keeps only the FIRST occurrence of each value, discarding all subsequent duplicates while preserving original order — the result is `["a", "b", "c"]`
D) `distinct()` keeps the LAST occurrence of each duplicate value rather than the first — values encountered later in the list overwrite earlier entries

**Answer:** A, C

**Explanation:** Both functions process lists in left-to-right order while preserving relative position. **(A)** `compact()` scans from left to right, copying elements to the output only when they are neither an empty string (`""`) nor `null` — non-empty, non-null elements retain their original relative order. **(C)** `distinct()` scans from left to right, adding each element to the output only if it has not been seen before — the first occurrence of each unique value is kept and all later duplicates are discarded, preserving original order for retained elements. Option B is false — `compact()` never sorts. Option D is false — `distinct()` always keeps the FIRST occurrence, not the last.

---

### Question 4

**Difficulty:** Medium
**Answer Type:** one
**Topic:** `cidrsubnet()` — correct 3-step calculation sequence to identify the result

An engineer evaluates `cidrsubnet("10.0.0.0/16", 8, 3)` in `terraform console`. Which of the following correctly sequences ALL three calculation steps and identifies the correct result?

A) Step 1: Borrow 8 bits from the host space → Step 2: Apply netnum `3` → Step 3: Add base prefix → Result: `"10.0.8.0/24"` (netnum is multiplied by 8)
B) Step 1: Start with base prefix `"10.0.0.0/16"` → Step 2: Borrow `newbits=8` additional bits, extending the prefix from `/16` to `/24` — creating a subnet pool where each subnet spans 256 addresses → Step 3: Select subnet number `netnum=3` (zero-based), counting up from `10.0.0.0/24` → Result: `"10.0.3.0/24"`
C) Step 1: Divide the address space by `newbits=8` → Step 2: Multiply by `netnum=3` → Step 3: Add to base → Result: `"10.0.6.0/24"`
D) Step 1: Start with base `/16` → Step 2: Apply `netnum=3` directly as the third octet → Step 3: Append `/8` as the new mask → Result: `"10.0.3.0/8"`

**Answer:** B

**Explanation:** `cidrsubnet(prefix, newbits, netnum)` follows a three-step process: **(1)** Begin with the base CIDR block `"10.0.0.0/16"` — this defines the address space to subdivide. **(2)** Borrow `newbits=8` additional bits from the host portion, increasing the prefix length from `/16` to `/24` (16 + 8 = 24). This creates 256 possible `/24` subnets within the `10.0.x.0/24` range. **(3)** Select subnet number `netnum=3` (zero-based): subnet 0 = `10.0.0.0/24`, subnet 1 = `10.0.1.0/24`, subnet 2 = `10.0.2.0/24`, subnet 3 = `10.0.3.0/24`. The result is `"10.0.3.0/24"`. Option A applies an incorrect multiplication to the netnum. Option C also applies incorrect arithmetic. Option D applies the netnum before the prefix calculation.

---

### Question 5

**Difficulty:** Medium
**Answer Type:** one
**Topic:** `for` expression with `if` filter — per-element evaluation sequence

An engineer writes this expression:

```hcl
[for name in ["alice", "bob", "ann", "charlie"] : upper(name) if startswith(name, "a")]
```

For each element in the input list, which of the following correctly sequences the operations Terraform performs?

A) (1) Apply `upper(name)` to every element first → (2) Apply `startswith()` filter to each uppercased result → (3) Keep elements where `startswith` returns `true` → Result: `["ALICE","ANN"]` (but using incorrect uppercased input for the filter)
B) (1) For each element, evaluate the `if` condition — `startswith(name, "a")` — FIRST → (2) If the condition is `true`, THEN evaluate the value expression `upper(name)` → (3) Add the result to the output list → (4) After all elements, return the final list
C) (1) Sort the input list alphabetically → (2) Apply the `if` filter → (3) Apply `upper()` to surviving elements → return list
D) The `if` condition and `upper()` expression are evaluated simultaneously for every element — Terraform evaluates both regardless of whether the condition is true or false

**Answer:** B

**Explanation:** In a `for` expression with an `if` filter, Terraform evaluates operations in this per-element sequence: **(1)** Evaluate the `if` condition using the current element — if `startswith(name, "a")` returns `false`, skip this element entirely and move to the next; **(2)** Only if the condition is `true`, evaluate the value expression (`upper(name)`) — this means `upper()` is NEVER called for elements that fail the filter; **(3)** Add the transformed value to the output list; **(4)** After all elements have been processed, return the completed list. For the input `["alice","bob","ann","charlie"]`: `"alice"` passes (condition true → `upper("alice")` = `"ALICE"` added); `"bob"` fails (skipped); `"ann"` passes (`"ANN"` added); `"charlie"` fails (skipped). Result: `["ALICE","ANN"]`. Option A incorrectly applies `upper()` before the filter.

---

### Question 6

**Difficulty:** Medium
**Answer Type:** one
**Topic:** `try()` left-to-right evaluation — sequence for finding the first non-erroring expression

An engineer writes this local:

```hcl
locals {
  port = try(
    var.config["http_port"],
    var.config["port"],
    8080
  )
}
```

`var.config` is a map that does not contain either `"http_port"` or `"port"`. Which of the following correctly sequences how Terraform evaluates this `try()` expression?

A) Terraform evaluates ALL three expressions simultaneously and uses the one that does not error — if more than one succeeds, it picks the last one
B) Terraform evaluates `var.config["http_port"]` FIRST — it errors because the key does not exist; Terraform then moves to `var.config["port"]` — it also errors; Terraform then evaluates `8080` — this is a literal and never errors; Terraform returns `8080` as the final value
C) `try()` short-circuits at the first error and returns `null` — none of the fallback expressions are evaluated once an error occurs
D) Terraform evaluates the expressions in REVERSE order (last to first) — `8080` is evaluated first as the "base case," then earlier expressions are checked to see if they would override it

**Answer:** B

**Explanation:** `try()` evaluates its arguments strictly left to right. For each expression: if it evaluates without error, `try()` immediately returns that value and stops — subsequent expressions are never evaluated (short-circuit on success). If the expression errors (e.g., accessing a missing map key throws an error), `try()` discards the error and moves to the next argument. The sequence here: **(1)** evaluate `var.config["http_port"]` — errors (key absent) → discard error, move on; **(2)** evaluate `var.config["port"]` — errors (key absent) → discard error, move on; **(3)** evaluate `8080` — a literal that always succeeds → return `8080`. The result is `8080`. `try()` is particularly useful as a safe wrapper for map key accesses and object attribute accesses where the key or attribute may not exist. Option C is wrong — `try()` catches errors and continues to the next expression; it does not return `null` on first error.

---

### Question 7

**Difficulty:** Medium
**Answer Type:** one
**Topic:** `zipmap()` positional pairing order — key list position determines key-value assignment

An engineer calls `zipmap(["z", "a", "m"], [100, 200, 300])`. Which of the following correctly describes the SEQUENCE of pairing operations and the resulting map?

A) `zipmap()` sorts the keys list alphabetically first, then pairs in sorted order — result: `{ a = 200, m = 300, z = 100 }`
B) `zipmap()` pairs by POSITION: `keys[0]` → `values[0]`, `keys[1]` → `values[1]`, `keys[2]` → `values[2]` — the order of the keys list directly determines which value each key receives; result: `{ z = 100, a = 200, m = 300 }`
C) `zipmap()` pairs by POSITION but applies the values in reverse order — `keys[0]` receives the last value; result: `{ z = 300, a = 200, m = 100 }`
D) `zipmap()` sorts both lists independently then pairs in sorted order — result: `{ a = 100, m = 200, z = 300 }`

**Answer:** B

**Explanation:** `zipmap(keys_list, values_list)` pairs elements strictly by position: the element at index 0 of the keys list is paired with the element at index 0 of the values list, index 1 with index 1, and so on. No sorting is applied to either list — the original order of both lists is preserved during pairing. For `zipmap(["z","a","m"], [100,200,300])`: `"z"` pairs with `100`, `"a"` pairs with `200`, `"m"` pairs with `300`. If the order of the keys list is changed, the key-value assignments change too — swapping to `["a","m","z"]` would produce `{ a=100, m=200, z=300 }`. This positional dependency means the caller controls the assignment through argument order. Note: `zipmap()` requires both lists to have the same length — if they differ, Terraform returns an error.

---

### Question 8

**Difficulty:** Medium
**Answer Type:** one
**Topic:** Variable type constraint checked BEFORE custom validation block condition

A variable is declared as:

```hcl
variable "port" {
  type = number

  validation {
    condition     = var.port >= 1 && var.port <= 65535
    error_message = "port must be between 1 and 65535."
  }
}
```

A caller passes `-var="port=not-a-number"`. Which of the following correctly sequences the checks Terraform performs, and which error fires?

A) Terraform evaluates the `validation` condition FIRST — `"not-a-number" >= 1` is checked and returns a type error from the comparison, causing the `error_message` to be displayed
B) The `type = number` constraint is evaluated FIRST — Terraform rejects `"not-a-number"` because it cannot be converted to a number, and returns a type error before the `validation` block's `condition` is ever evaluated
C) Both checks run simultaneously — Terraform returns both a type error and a validation error at the same time
D) The `validation` block runs BEFORE the `type` constraint because validation is defined closer to the bottom of the variable block

**Answer:** B

**Explanation:** Terraform evaluates variable constraints in a strict sequence: **(1)** type constraint (`type = number`) is checked first — if the provided value cannot be converted to the declared type, Terraform immediately returns a type conversion error and stops. The custom `validation` block is never reached. **(2)** Only if the value passes the type constraint is the `validation` block's `condition` evaluated. For `port = "not-a-number"`: the `type = number` check fires first with an error such as `"The given value is not suitable for var.port: a number is required"` — the validation condition `var.port >= 1 && var.port <= 65535` is never evaluated. This sequencing is by design — it makes no sense to evaluate a range check on a value that isn't even the correct type. Physical block order in the file has no bearing on evaluation order.

---

### Question 9

**Difficulty:** Medium
**Answer Type:** one
**Topic:** Sequence for a parent module to access a child module output with a REAL (non-placeholder) value

A root module declares `module "network" { source = "./network" }`. The child module exposes `output "vpc_id" { value = aws_vpc.main.id }`. An engineer wants `module.network.vpc_id` to resolve to the actual VPC ID (not `"(known after apply)"`). Which of the following correctly sequences the steps required for the reference to hold a real value?

A) (1) Declare the output in the child module → (2) Reference `module.network.vpc_id` in the root module → the reference resolves immediately because Terraform pre-populates all output values during `terraform init`
B) (1) Declare `output "vpc_id"` in the child module → (2) Reference `module.network.vpc_id` in the root module → (3) Run `terraform plan` — at this point, if `aws_vpc.main` does not yet exist, the reference shows `"(known after apply)"` → (4) Run `terraform apply` — Terraform creates `aws_vpc.main`, writes its `id` to state, evaluates the child module output, and the parent's reference is now populated with the real VPC ID for that apply and all subsequent plans
C) (1) Run `terraform apply` first with only the child module → (2) Add the output declaration → (3) Run `terraform apply` a second time to propagate the output to the parent
D) Module outputs are only available when queried with `terraform output module.network.vpc_id` — they cannot be referenced inline in other resource arguments

**Answer:** B

**Explanation:** The full sequence for a parent module reference to hold a real (non-placeholder) value is: **(1)** The child module must declare the output block — without it, the reference `module.network.vpc_id` is invalid. **(2)** The root module references `module.network.vpc_id` in a resource argument or local. **(3)** During `terraform plan`, if `aws_vpc.main` has not yet been created, its `id` is a computed value — the plan shows `module.network.vpc_id` as `"(known after apply)"` and any attributes downstream also show the same uncertainty. **(4)** After `terraform apply` completes, the VPC is created, its `id` is known and written to state, the child module output is evaluated, and the value is available. All subsequent plans and applies can reference the resolved value. The LAST required step for the real value to be available is a successful `terraform apply` that creates the underlying resource. Option A is false — `terraform init` never evaluates outputs.

---

### Question 10

**Difficulty:** Medium
**Answer Type:** one
**Topic:** `dynamic` block `for_each` iteration order — list vs map ordering

An engineer uses a `dynamic "ingress"` block in two different security groups: one uses `for_each = var.ingress_list` (a `list(object(...))`) and another uses `for_each = var.ingress_map` (a `map(object(...))`). Which of the following correctly describes the sequence in which Terraform generates the nested `ingress` blocks for each case?

A) Both list and map produce blocks in the same order — alphabetical by the stringified representation of the value
B) For a LIST: Terraform generates blocks in original list order (index 0 first, index 1 second, etc.) — `for_each.key` is the zero-based index; for a MAP: Terraform generates blocks in lexicographic key order — `for_each.key` is the string map key; the two approaches produce different orderings when the same data is structured differently
C) For a MAP: Terraform generates blocks in the order the key-value pairs were declared in the `.tf` file — declaration order is preserved; for a LIST: blocks are generated in reverse list order
D) Terraform always generates `dynamic` blocks in the same order regardless of the collection type — ordering is determined by the block's `content` expression, not the `for_each` collection

**Answer:** B

**Explanation:** The iteration order of a `dynamic` block's `for_each` depends on the collection type: **List**: blocks are generated in the original list order — the element at index 0 generates the first block, index 1 the second, etc. The iterator's `.key` is the zero-based numeric index. **Map**: blocks are generated in lexicographic (alphabetical) key order — Terraform always iterates map keys in sorted order for deterministic plan output. The iterator's `.key` is the string key. This distinction matters when the ORDER of nested blocks has semantic significance (e.g., firewall rules are evaluated top to bottom). If a map is used but the insertion-order of the original data matters, converting to a list or encoding sequence as a key prefix (e.g., `"01-http"`, `"02-https"`) can control the ordering. Option C is false — HCL map declaration order is not preserved; Terraform always sorts map keys.

---

### Question 11

**Difficulty:** Medium
**Answer Type:** many
**Topic:** `toset()` deduplication happens BEFORE `for_each` iterates — and iteration order is lexicographic

Which TWO of the following correctly describe the sequencing of operations when `for_each = toset(var.names)` is used on a resource?

A) `toset()` removes duplicate values FIRST — deduplication occurs when the `toset()` call is evaluated (before `for_each` begins iterating); `for_each` only ever sees a collection of unique string keys because the set already has duplicates removed
B) `for_each` iterates the original list first, detects duplicates at iteration time, and silently skips them — `toset()` is a no-op hint that does not actually transform the collection before iteration
C) When `for_each` uses a set produced by `toset()`, the resource instances are created in LEXICOGRAPHIC (alphabetical) key order — the original positional order of the list is NOT preserved because sets are unordered, and Terraform sorts set keys alphabetically for deterministic plan output
D) `toset()` preserves the original list order when converting to a set — the set iterates in the same order as the source list

**Answer:** A, C

**Explanation:** **(A)** `toset()` is a type conversion function that executes immediately when evaluated — it removes duplicates from the list and produces a `set(string)` value before `for_each` ever begins. The resulting set has no duplicates, and `for_each` iterates only the unique keys in the set. **(C)** Sets in Terraform have no defined positional order. When `for_each` iterates a set, it does so in lexicographic (alphabetical) key order for determinism — this ensures that `terraform plan` produces consistent output regardless of the order items were added to the source list. If your list is `["charlie","alice","bob"]`, the `for_each` instances are created in key order: `resource["alice"]`, `resource["bob"]`, `resource["charlie"]`. The original list order is not preserved. Option B is false — `toset()` actively transforms the collection; it is not a no-op. Option D is false — sets discard positional order by definition.

---

### Question 12

**Difficulty:** Hard
**Answer Type:** one
**Topic:** Full multi-source variable value resolution — complete sequence from all sources to final value

An engineer runs `terraform apply` with the following variable inputs all set for the same variable `env`:

- Variable block: `default = "dev"`
- `terraform.tfvars`: `env = "staging"`
- `production.auto.tfvars`: `env = "production"`
- Shell environment: `TF_VAR_env=test`
- CLI: `-var="env=live"`

Which of the following correctly sequences how Terraform determines the final value?

A) Terraform reads the sources in this order: default → `terraform.tfvars` → `*.auto.tfvars` → `TF_VAR_*` → CLI flag; each source overwrites the previous; the LAST source read (CLI flag) wins; final value: `"live"`
B) Terraform reads ALL input sources during initialisation/planning, then applies a fixed precedence hierarchy to select the winner: CLI `-var` flag (highest) overrides `TF_VAR_*` env var, which overrides `*.auto.tfvars`, which overrides `terraform.tfvars`, which overrides the `default` (lowest); because the CLI flag `"live"` is at the top of the hierarchy, the final value is `"live"` regardless of what the other sources say
C) Terraform uses the value from `terraform.tfvars` by default and only checks `TF_VAR_*` env vars if `terraform.tfvars` does not exist; the CLI flag is only applied on interactive runs; final value: `"staging"`
D) Terraform errors when a variable is set from more than two sources simultaneously — only two input methods can be active at once

**Answer:** B

**Explanation:** Terraform reads and considers ALL provided input sources simultaneously — it does not process them sequentially and stop at the first match. After reading all sources, it applies a fixed, documented precedence hierarchy to determine the winning value: **(Highest)** CLI `-var` flag and `-var-file` flag → `TF_VAR_*` environment variables → `*.auto.tfvars` files (automatically loaded) → `terraform.tfvars` (automatically loaded) → `default` in the variable block **(Lowest)**. In this scenario, all five sources are set. The CLI `-var="env=live"` is at the top of the hierarchy and overrides every other source — the final value is `"live"`. Terraform never errors when multiple sources set the same variable; it silently applies precedence rules. Option A incorrectly describes the process as sequential overwriting — the behavior is precedence-based, not last-read-wins in a sequential scan. The practical impact is identical in most cases, but the mental model of "precedence hierarchy applied to all sources simultaneously" is more accurate.

---

### Question 13

**Difficulty:** Hard
**Answer Type:** many
**Topic:** Two correct ordering contrasts: variable type check sequence and `for_each` with map vs set iteration

Which TWO of the following correctly describe ordering or sequencing behavior related to variable evaluation and `for_each` iteration?

A) When a variable has both a `type` constraint and a `validation` block, Terraform always evaluates the `type` constraint FIRST — if the value cannot be converted to the declared type, Terraform returns a type error immediately and the `validation` condition is NEVER evaluated; `validation` conditions only run after the value is confirmed to be the correct type
B) When a variable has both a `type` constraint and a `validation` block, the `validation` condition is evaluated FIRST — the type constraint is only checked afterward as a secondary safeguard
C) When `for_each` uses a `map(string)`, Terraform iterates keys in lexicographic order — when `for_each` uses a `set(string)` (from `toset()`), Terraform ALSO iterates in lexicographic order; both map and set `for_each` produce resource instances in alphabetical key order, making the ordering behavior consistent regardless of whether the source was a map or a set
D) When `for_each` uses a `map`, resource instances are created in the declaration order of the map's key-value pairs in the `.tf` file — when `for_each` uses a `set`, instances are created in the original list order before `toset()` was applied

**Answer:** A, C

**Explanation:** **(A)** This is the documented evaluation sequence for variables with both constraints: the `type` argument is processed first as a basic validity gate — if the value cannot be converted (e.g., a string where a number is expected), Terraform rejects it with a type error before running any custom logic. Only values that pass the type check are passed to the `validation` block. This prevents nonsensical comparisons in validation conditions (e.g., comparing a string to a number). **(C)** Both `map` and `set` collections cause `for_each` to iterate in lexicographic key order — this is a deliberate Terraform design choice for deterministic, reproducible plan output. A map's keys are iterated alphabetically, and a set's elements (which ARE the keys in `for_each`) are also iterated alphabetically. The two collection types behave identically in terms of iteration ordering. Option B is false — as described in A, type is checked before validation. Option D is false — HCL map declaration order is not preserved; Terraform sorts map keys alphabetically, and `toset()` discards the original list order.
