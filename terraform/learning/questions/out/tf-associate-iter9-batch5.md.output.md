# Terraform Associate Exam Questions

---

### Question 1

**Difficulty:** Easy
**Answer Type:** one
**Topic:** `for` expression `if` filter clause — which statement is TRUE?

Which of the following statements about adding an `if` filter to a `for` expression is TRUE?

A) Adding `if condition` to a `for` expression is a syntax error in Terraform — filtering must be done with a separate `compact()` call on the result of the `for` expression, not inline
B) The `if` clause in a `for` expression filters the INPUT collection before the transformation expression is evaluated — only elements for which the `if` condition is `true` are included in the resulting list or map; elements where the condition is `false` are silently discarded from the output
C) The `if` clause in a `for` expression must always appear BEFORE the transformation value expression — writing `[for n in names : upper(n) if length(n) > 3]` is a syntax error because the `if` must precede the `:`
D) The `if` clause in a `for` expression can only filter on the LENGTH of the element — other conditions such as type comparisons or `contains()` checks are not supported

---

### Question 2

**Difficulty:** Easy
**Answer Type:** one
**Topic:** `compact()` function scope — which statement is FALSE?

Which of the following statements about the `compact()` function is FALSE?

A) `compact(["a", "", "b", null, "c"])` returns `["a", "b", "c"]` — both empty strings `""` and `null` values are removed from the list
B) `compact()` is specifically designed for `list(string)` — it removes elements that are either `null` or empty strings (`""`); it does NOT remove other falsy values such as `false` (boolean), `0` (number), or `"0"` (the string zero)
C) `compact()` removes all "falsy" values from any collection type — passing a `list(number)` with zeroes (`0`) will remove those zeroes from the output alongside any `null` values
D) `compact()` is frequently used to clean up lists produced by conditional expressions where some elements may be `null` when a condition is false — for example, when building a list of optional security group IDs

---

### Question 3

**Difficulty:** Easy
**Answer Type:** many
**Topic:** `dynamic` block iterator naming — which TWO statements are TRUE?

Which TWO of the following statements about the `dynamic` block's iterator variable are TRUE?

A) The iterator variable inside a `dynamic` block defaults to the name of the block type being generated — for `dynamic "ingress" { ... }`, the iterator variable is automatically named `ingress`, giving access to `ingress.value` and `ingress.key` inside the `content` block
B) The iterator variable name is always fixed as `each` regardless of the block type — inside any `dynamic` block, you access the current element with `each.value` and `each.key`, exactly as with `for_each` on resource blocks
C) The `iterator` argument inside a `dynamic` block overrides the default iterator name — for example, setting `iterator = rule` changes the iterator from `ingress` to `rule`, so the content block uses `rule.value` and `rule.key` instead of `ingress.value` and `ingress.key`
D) The iterator variable inside a `dynamic` block always exposes only `iterator.value` — `iterator.key` is not available because `dynamic` blocks only support `list` collections as the `for_each` value, and lists have no string keys

---

### Question 4

**Difficulty:** Medium
**Answer Type:** one
**Topic:** `object` type vs `map` type — which statement is TRUE?

Which of the following statements about the difference between an `object` type and a `map` type in Terraform variable declarations is TRUE?

A) `map(string)` and `object({...})` are fully interchangeable — either can be used to represent structured data with named attributes, and Terraform will automatically convert between them as needed
B) An `object` type constraint (e.g., `object({ name = string, port = number })`) allows each attribute to have a DIFFERENT type — `name` can be a `string` while `port` is a `number`; a `map` type (e.g., `map(string)`) requires ALL values to be the SAME type; this is the fundamental structural difference between the two
C) `map(string)` supports an arbitrary number of dynamically-named keys at runtime; `object({...})` also supports arbitrary keys — the declared attribute names in an `object` are only hints for documentation, not enforced at evaluation time
D) An `object` type produces better performance than `map(string)` for large collections because Terraform uses a hash-indexed internal structure for objects but a linked list for maps

---

### Question 5

**Difficulty:** Medium
**Answer Type:** one
**Topic:** `element()` index wrapping — which statement is TRUE?

Which of the following statements about the `element()` function is TRUE?

A) `element(list, index)` behaves identically to `list[index]` — if the index is greater than or equal to the length of the list, both return an error
B) `element(list, index)` wraps the index using the modulo of the list length — `element(["a", "b", "c"], 4)` returns `"b"` because `4 mod 3 = 1`, which is the index of `"b"`; this wrapping behaviour makes `element()` useful for cycling through a fixed list of values (such as availability zones) as a counter increases
C) `element(list, index)` always returns the LAST element of the list when the index exceeds the list length — it never wraps and never errors
D) `element(list, index)` is only valid when used with `count.index` — it cannot be used with arbitrary integer expressions or variable values

---

### Question 6

**Difficulty:** Medium
**Answer Type:** one
**Topic:** `templatefile()` vs `file()` — which statement is FALSE?

Which of the following statements comparing `templatefile()` and `file()` is FALSE?

A) `file(path)` reads the contents of a file at the given path and returns it as a raw string — no template rendering is performed and no variable substitution occurs; the file is returned exactly as it exists on disk
B) `templatefile(path, vars)` renders a template file by substituting `${var_name}` expressions in the file content with values from the `vars` map — the second argument is required and must be a map containing all variables referenced in the template
C) `templatefile()` automatically has access to all variables, locals, and resource attributes in the calling module's scope — you do not need to pass them explicitly in the `vars` argument; the `vars` map is optional and is only needed for variables not already in module scope
D) A common use case for `templatefile()` is generating `user_data` scripts for EC2 instances — the template file (e.g., `user_data.sh.tpl`) can contain `${app_name}` placeholders that are replaced by values from the `vars` map passed to `templatefile()`

---

### Question 7

**Difficulty:** Medium
**Answer Type:** one
**Topic:** `try()` function — which statement is TRUE?

Which of the following statements about the `try()` function is TRUE?

A) `try(expr1, expr2, fallback)` evaluates ALL expressions and returns the LAST one that evaluates without error — it always executes every expression even if the first one succeeds
B) `try(expr1, expr2, fallback)` evaluates expressions left to right and returns the value of the FIRST expression that evaluates successfully without an error — subsequent expressions are not evaluated once a successful one is found; if ALL expressions error, Terraform returns a configuration error
C) `try()` is equivalent to the `||` (OR) logical operator in other languages — it returns `true` if any expression is truthy and `false` otherwise; it is used for boolean short-circuit evaluation, not for error handling
D) `try()` can only be used with map key access expressions such as `var.settings["key"]` — it cannot be used with function calls, attribute access chains, or type conversion expressions

---

### Question 8

**Difficulty:** Medium
**Answer Type:** one
**Topic:** `cidrsubnet()` parameters — which statement is TRUE?

Which of the following statements about the `cidrsubnet()` function is TRUE?

A) The `newbits` argument in `cidrsubnet(prefix, newbits, netnum)` specifies the FINAL prefix length of the resulting subnet — for example, `cidrsubnet("10.0.0.0/16", 24, 0)` produces a `/24` subnet because `newbits = 24`
B) The `newbits` argument specifies how many ADDITIONAL bits to add to the base prefix length — `cidrsubnet("10.0.0.0/16", 8, 0)` produces a `/24` subnet because `16 + 8 = 24`; and `cidrsubnet("10.0.0.0/16", 8, 1)` produces `"10.0.1.0/24"` — the `netnum` argument selects which subnet number to return
C) `cidrsubnet("10.0.0.0/16", 8, 1)` produces the CIDR `"10.0.0.1/24"` — the `netnum` argument offsets the HOST portion of the address by the given number
D) `cidrsubnet()` requires the base CIDR to be a class A network (`/8`) — it cannot be applied to `/16` or smaller prefix lengths

---

### Question 9

**Difficulty:** Medium
**Answer Type:** one
**Topic:** Output block `depends_on` — which statement is FALSE?

Which of the following statements about the `depends_on` meta-argument on output blocks is FALSE?

A) Output blocks support a `depends_on` meta-argument, just as resource blocks do — this allows an output to declare that its value should not be considered available until certain resources or modules have been fully applied
B) The `depends_on` argument on an output is most commonly needed when the output's value does not directly reference a resource's attribute but the output is logically dependent on a side effect of that resource — for example, an output that exposes a computed URL that depends on a DNS record being created, where the DNS creation is not reflected in the URL string itself
C) Output `depends_on` is required on any output that references a resource attribute — without it, Terraform cannot determine when to make the output available and will always show `(known after apply)` for resource attribute outputs
D) When an output in a child module has `depends_on`, the parent module's reference to that output will also be blocked until the declared dependencies complete — the `depends_on` constraint propagates through module composition

---

### Question 10

**Difficulty:** Medium
**Answer Type:** many
**Topic:** Splat expressions `[*]` — which TWO statements are TRUE?

Which TWO of the following statements about splat expressions (`[*]`) are TRUE?

A) The splat expression `aws_instance.web[*].id` is only valid when the resource uses `count` — it cannot be used on a resource that uses `for_each` because `for_each` instances are keyed by string, not by integer index
B) For a resource using `count`, `aws_instance.web[*].id` and `[for r in aws_instance.web : r.id]` are equivalent — both produce a list of all `id` attribute values across all `count` instances; the splat expression is a more concise shorthand for the `for` expression
C) The splat expression `[*]` is a legacy syntax that has been deprecated since Terraform 0.14 — it should be replaced with explicit `for` expressions in all new configurations
D) Applying a splat expression to a single resource instance (not using `count` or `for_each`) returns a list containing exactly one element — `aws_instance.web[*].id` where `aws_instance.web` is a single instance produces `["<id>"]`, not just `"<id>"`

---

### Question 11

**Difficulty:** Medium
**Answer Type:** one
**Topic:** `jsonencode()` and `jsondecode()` — which statement is FALSE?

Which of the following statements about `jsonencode()` and `jsondecode()` is FALSE?

A) `jsonencode(value)` converts any Terraform value (maps, lists, strings, numbers, booleans, null) into its JSON string representation — this is useful for generating inline JSON configuration such as IAM policy documents
B) `jsondecode(str)` parses a JSON-formatted string and returns a Terraform value — a JSON object becomes a Terraform `map`, a JSON array becomes a Terraform `list`, and JSON primitives map to their Terraform equivalents (string, number, bool, null)
C) `jsonencode()` and `jsondecode()` are inverses of each other — `jsondecode(jsonencode(value))` always returns a value that is structurally identical to the original `value` with no information loss, regardless of the input type
D) `jsonencode()` is commonly used with IAM policy documents in AWS configurations — instead of writing a heredoc or using the `aws_iam_policy_document` data source, engineers can write the policy as a Terraform map literal and pass it to `jsonencode()` to produce a valid JSON policy string

---

### Question 12

**Difficulty:** Hard
**Answer Type:** one
**Topic:** Four statements about `for_each` on resources — only ONE is TRUE

Four statements about the `for_each` meta-argument on resource blocks are presented below. Which is the ONLY TRUE statement?

A) When an element is removed from a `for_each` map or set and `terraform apply` runs, Terraform destroys the resource instance for the removed key AND renumbers all remaining instances to fill the gap — this is the main advantage of `for_each` over `count`, which also renumbers remaining instances when an element is removed
B) Inside a resource block that uses `for_each`, both `each.key` and `each.value` are always available — for a `set(string)`, `each.key` holds the set element (the string itself) and `each.value` is also the same string because set elements have no separate key and value; for a `map`, `each.key` is the map key and `each.value` is the corresponding map value
C) `for_each` can accept a `list(string)` directly without any type conversion — Terraform internally deduplicates list elements and builds a string key for each one; `toset()` is a convenience function but is not required
D) Resource instances created by `for_each` are addressed using integer indexes — for example, `aws_iam_user.users[0]`, `aws_iam_user.users[1]`, etc. — and accessing a specific instance by key is not supported in `terraform state` commands or `-target` flags

---

### Question 13

**Difficulty:** Hard
**Answer Type:** many
**Topic:** Which TWO statements about type constraints and type conversion functions are TRUE?

Which TWO of the following statements about Terraform type constraints and the type conversion functions (`tostring()`, `tonumber()`, `tobool()`, `tolist()`, `toset()`, `tomap()`) are TRUE?

A) Type conversion functions in Terraform are guaranteed to succeed for any input — if `tonumber("abc")` is called with a non-numeric string, Terraform silently returns `0` (the zero value for the `number` type) rather than raising an error
B) `tostring(true)` returns the string `"true"` and `tostring(false)` returns `"false"` — Terraform's `tostring()` function converts boolean values to their string representations without error; conversely, `tobool("true")` returns `true` and `tobool("false")` returns `false`, making round-trip conversion between bool and string lossless for the canonical string representations
C) The `any` type constraint on a variable does NOT mean the variable accepts any Terraform type — it means Terraform will infer the type from whatever value is first supplied and then enforce that inferred type for all subsequent references to the variable within the same apply
D) `toset(list)` removes duplicate elements when converting a list to a set — `toset(["a", "b", "a", "c"])` produces a set containing exactly three elements: `"a"`, `"b"`, and `"c"`; the ordering of elements in the resulting set is not guaranteed because sets in Terraform are unordered

## Answer Key

| Q# | Answer(s) | Explanation | Source | Difficulty |
|----|-----------|-----------:|--------|------------|
| 1 | B | ** Terraform's `for` expression supports an optional `if` filter clause that is written AFTER the transformation expression: `[for n in var.names : upper(n) if length(n) > 3]`. Only elements where the `if` condition evaluates to `true` are included in the result — elements where it evaluates to `false` are dropped. In the example, any name with three characters or fewer is excluded from the output list. This inline filtering is cleaner and more readable than post-processing with `compact()` or a second expression. The filter condition can be any boolean HCL expression — `contains()`, type checks, comparisons, function calls, etc. Option A is false — the syntax is valid. Option C is false — the `if` clause comes AFTER the `:` transformation, not before. Option D is false — any boolean expression is permitted. | ** `for` expression `if` filter clause — which statement is TRUE? | ** Easy |
| 2 | C | ** Option C is FALSE. `compact()` is narrowly scoped: it removes only `null` values and empty strings (`""`) from a `list(string)`. It does NOT remove all "falsy" values — `false`, `0`, `"0"`, or `[]` are NOT removed. `compact()` is strictly typed for string lists; passing a `list(number)` with zero values will NOT remove those zeroes, and attempting to pass a `list(number)` may cause a type error. Options A and B are accurate descriptions of `compact()`'s behaviour. Option D describes the most common real-world use case — building conditional lists where some values may be `null` (e.g., `compact([var.optional_sg_id, aws_security_group.web.id])`) — and is also true. | ** `compact()` function scope — which statement is FALSE? | ** Easy |
| 3 | A, C | ** **(A)** is TRUE. By default, the iterator variable inside a `dynamic` block takes the same name as the block type being generated. For `dynamic "ingress"`, the iterator is `ingress` — so within the `content` block you reference `ingress.value.from_port`, `ingress.value.to_port`, etc. This is different from resource-level `for_each`, which always uses `each`. **(C)** is TRUE. The optional `iterator` argument within the `dynamic` block overrides this default name. This is useful when the block type name is long, ambiguous, or conflicts with another variable — `iterator = rule` gives you `rule.value` and `rule.key` instead of the default block-type name. **(B)** is FALSE — the iterator is NOT always `each`; it defaults to the block type name. **(D)** is FALSE — `dynamic` blocks support both `list` and `map` collections as the `for_each` value, and when iterating over a `map`, `iterator.key` holds the map key. | ** `dynamic` block iterator naming — which TWO statements are TRUE? | ** Easy |
| 4 | B | ** The fundamental distinction between `object` and `map` in Terraform's type system: a **`map`** is a homogeneous collection — every value must be the same declared type (e.g., `map(string)` means every value is a `string`). The keys are strings but are dynamic — you can have any number of key-value pairs. An **`object`** is a heterogeneous collection with a fixed set of named attributes — each attribute can have its own independent type. `object({ name = string, port = number, enabled = bool })` is valid because each attribute has a different type. This makes `object` the right choice when a variable bundles configuration fields of mixed types. Option A is false — they are structurally different and not automatically interchangeable. Option C is false — `object` attribute names ARE enforced; the object type validator checks that the supplied value has exactly the declared attributes (or a superset, depending on context). Option D is false — this is not a relevant or accurate description of Terraform's internal implementation. | ** `object` type vs `map` type — which statement is TRUE? | ** Medium |
| 5 | B | ** `element()` uses modulo arithmetic when the index equals or exceeds the length of the list: `element(list, index)` returns `list[index % length(list)]`. For a three-element list, `element(["a","b","c"], 4)` computes `4 % 3 = 1`, returning `"b"`. `element(["a","b","c"], 6)` computes `6 % 3 = 0`, returning `"a"`. This makes `element()` ideal for distributing resources across a fixed set of values in a round-robin pattern — for example, distributing EC2 instances across availability zones: `element(var.availability_zones, count.index)` cycles through the list as `count.index` increments. Direct list indexing (`list[index]`) does NOT wrap — it errors if the index is out of range. Option A incorrectly claims `element()` errors on out-of-range indexes. Option C incorrectly describes the wrapping as "returns last element." Option D is false — `element()` accepts any integer expression. | ** `element()` index wrapping — which statement is TRUE? | ** Medium |
| 6 | C | ** Option C is FALSE. `templatefile()` does NOT automatically have access to the calling module's variables, locals, or resource attributes. The ONLY values available inside a template file are those explicitly passed in the `vars` map argument. If you want `${app_name}` in the template to resolve, you must pass `templatefile("user_data.sh.tpl", { app_name = local.app_name })`. The `vars` map is NOT optional — if the template references a variable that is not in the map, Terraform throws an error at evaluation time. This explicit-passing design keeps template files self-contained and testable independently of module scope. Options A, B, and D are all accurate: `file()` reads raw content without rendering, `templatefile()` performs substitution using the explicitly passed map, and EC2 `user_data` generation is the canonical use case. | ** `templatefile()` vs `file()` — which statement is FALSE? | ** Medium |
| 7 | B | ** `try()` evaluates its arguments left to right and returns the value of the FIRST expression that succeeds (evaluates without error). As soon as one expression succeeds, evaluation stops — remaining arguments are not evaluated. Common uses: `try(var.settings["optional_key"], "default_value")` — if the map key lookup errors (key not found), `try()` falls through to the `"default_value"` string. `try(tonumber(var.port), 8080)` — if `tonumber()` fails (e.g., the port is not a valid number string), the fallback `8080` is used. If ALL expressions error, Terraform raises a configuration error — `try()` is not a universal error suppressor. Option A is false — `try()` stops at the first success, not the last. Option C confuses `try()` with a boolean operator — it is strictly for error handling in expression evaluation. Option D is false — `try()` works with any expression type. | ** `try()` function — which statement is TRUE? | ** Medium |
| 8 | B | ** `cidrsubnet(prefix, newbits, netnum)` works as follows: `newbits` is the number of ADDITIONAL bits to borrow from the host portion of the base prefix, increasing the prefix length. `cidrsubnet("10.0.0.0/16", 8, 0)` creates subnets at `/24` (16 + 8 = 24). The `netnum` argument selects WHICH subnet to return — it is the value of the newly borrowed bits. For `/16` + 8 bits: `netnum = 0` → `10.0.0.0/24`; `netnum = 1` → `10.0.1.0/24`; `netnum = 2` → `10.0.2.0/24`, and so on up to `netnum = 255`. This makes `cidrsubnet()` highly useful in `for` expressions or `count`/`for_each` loops to programmatically generate subnets: `cidrsubnet("10.0.0.0/16", 8, count.index)`. Option A confuses `newbits` with the final prefix length. Option C incorrectly describes `netnum` as a host offset — it is a NETWORK offset, not a host offset. Option D is false — `cidrsubnet()` works on any prefix length. | ** `cidrsubnet()` parameters — which statement is TRUE? | ** Medium |
| 9 | C | ** Option C is FALSE. `depends_on` on an output is NOT required for outputs that reference resource attributes. Terraform automatically tracks the dependency between an output value and the resources whose attributes the output references — this is standard implicit dependency detection. If `output "instance_ip" { value = aws_instance.web.public_ip }` references `aws_instance.web.public_ip`, Terraform already knows the output depends on that resource and will not make the output available until the resource is applied. `depends_on` on an output is only needed in the unusual case where the output has an INDIRECT dependency that Terraform cannot detect through attribute references — the scenario in option B. Options A, B, and D are all accurate: outputs do support `depends_on`, the use case is indirect/side-effect dependencies, and the constraint propagates through module outputs to parent modules. | ** Output block `depends_on` — which statement is FALSE? | ** Medium |
| 10 | B, D | ** **(B)** is TRUE. For a resource that uses `count`, `resource_type.name[*].attribute` and `[for r in resource_type.name : r.attribute]` are semantically equivalent — both produce a list of the attribute value from every instance. The splat `[*]` is syntactic sugar for the `for` expression and is more concise in outputs and variable arguments where you simply want all values as a list. **(D)** is TRUE. When a splat is applied to a single (non-count, non-for_each) resource, it produces a LIST with one element, not a scalar. `aws_instance.web[*].id` returns `["i-0abc123"]`. This wrapping behaviour is why you sometimes see `one(aws_instance.web[*].id)` — the `one()` function unwraps a single-element list to its scalar value. **(A)** is FALSE — for `for_each` resources, you use a different form of splat or a `for` expression; the `[*]` splat applies specifically to `count`-based or single resources. **(C)** is FALSE — splat expressions are NOT deprecated; they remain a fully supported and commonly used shorthand in Terraform. | ** Splat expressions `[*]` — which TWO statements are TRUE? | ** Medium |
| 11 | C | ** Option C is FALSE. `jsonencode()` and `jsondecode()` are NOT perfectly lossless inverses for all Terraform types. Specifically, Terraform's type system includes distinctions that JSON does not preserve. For example: a Terraform `set` and a `list` both encode to a JSON array — `jsondecode()` always returns a Terraform `tuple` or `list`, never a `set`. Similarly, Terraform `object` and `map` types both encode to JSON objects — `jsondecode()` returns a `map(any)`, losing any `object` attribute type information. Numeric precision can also differ. So `jsondecode(jsonencode(value))` does NOT necessarily return a value of the same TYPE as the original — the VALUES may be preserved but the type information is not always round-tripped cleanly. Options A, B, and D are accurate: `jsonencode()` converts any Terraform value to a JSON string, `jsondecode()` parses JSON to Terraform values, and IAM policy generation is the canonical use case. | ** `jsonencode()` and `jsondecode()` — which statement is FALSE? | ** Medium |
| 12 | B | ** Option B is the ONLY TRUE statement. For `for_each` over a `map`, `each.key` = map key, `each.value` = map value. For `for_each` over a `set(string)`, because a set has no separate keys — each element IS its own identifier — `each.key` and `each.value` are identical and both equal the element string itself. Option A is FALSE — `for_each` does NOT renumber remaining instances when an element is removed. This is precisely `for_each`'s KEY ADVANTAGE over `count`. When an element is removed from a `for_each` collection, only the resource instance for THAT specific key is destroyed; all other instances retain their addresses unchanged. With `count`, removing an element from the middle of a list does shift the indexes of subsequent instances, potentially causing unwanted destroy-and-recreate cycles. Option C is FALSE — `for_each` does NOT accept a `list(string)` directly; using a plain list causes an error because lists can contain duplicates (which would create ambiguous resource addresses). `toset()` is REQUIRED for list inputs. Option D is FALSE — `for_each` instances are addressed by their STRING KEY, not by integer index: `aws_iam_user.users["alice"]`, `aws_iam_user.users["bob"]`, etc. This string-key addressing works in `terraform state` commands and `-target` flags. | ** Four statements about `for_each` on resources — only ONE is TRUE | ** Hard |
| 13 | B, D | ** **(B)** is TRUE. Terraform's boolean-to-string and string-to-boolean conversions are well-defined. `tostring(true)` → `"true"`, `tostring(false)` → `"false"`. `tobool("true")` → `true`, `tobool("false")` → `false`. The round-trip is lossless for the canonical lowercase representations. Note: `tobool("1")` also returns `true` and `tobool("0")` returns `false` — Terraform accepts these as valid boolean string inputs. **(D)** is TRUE. `toset()` deduplicates — it discards any repeated elements and the result is a set, which is unordered. `toset(["a","b","a","c"])` = `{"a","b","c"}` (three elements). This is exactly why `toset()` is required before passing a list to `for_each` — the list might have duplicates, and `for_each` requires unique keys. **(A)** is FALSE. Type conversion functions DO raise errors on invalid input. `tonumber("abc")` returns an error, not `0`. This is where `try(tonumber(s), default_value)` is useful — to provide a fallback when the conversion might fail. **(C)** is FALSE. The `any` type constraint does NOT mean Terraform infers a fixed type on first use and then enforces it. It means Terraform performs NO type checking on the variable's value — any type is accepted, and Terraform uses the type of the supplied value as-is throughout the configuration. There is no "infer on first use" mechanism. | ** Which TWO statements about type constraints and type conversion functions are TRUE? | ** Hard |
