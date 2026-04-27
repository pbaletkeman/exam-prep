# Terraform Associate (004) — Question Bank Iter 7 Batch 3

**Iteration**: 7
**Iteration Style**: Fill-in-the-blank / complete the HCL — given a partial configuration or partial statement, select the term or argument that correctly fills the blank
**Batch**: 3
**Objective**: 3 — Core Workflow & CLI
**Generated**: 2026-04-25
**Total Questions**: 13
**Difficulty Split**: 3 Easy / 8 Medium / 2 Hard
**Answer Types**: 10 `one` / 3 `many` / 0 `none`

---

## Questions

---

### Question 1 — Saving a Plan to a File with `-out`

**Difficulty**: Easy
**Answer Type**: one
**Topic**: The `-out` flag saves the execution plan to a binary file for a deterministic later apply

**Question**:
A CI pipeline should generate a plan in one stage and apply it in a later stage — ensuring the exact same changes reviewed in the plan are the ones applied. Complete the plan command:

```bash
terraform plan ___________ plan.tfplan
```

What flag fills the blank to save the plan to a file named `plan.tfplan`?

- A) `-save`
- B) `-export`
- C) **`-out=`**
- D) `-write`

**Answer**: C

**Explanation**:
`terraform plan -out=plan.tfplan` serialises the execution plan to a binary file called `plan.tfplan`. This file captures the exact proposed changes at the moment the plan was generated — including any variable values and the refreshed state. When `terraform apply plan.tfplan` is later run, Terraform applies precisely those changes without re-evaluating the configuration or prompting for confirmation. This two-stage pattern is the recommended CI/CD approach: plan in one job (get human or automated review), then apply the saved file in a separate job. The flag is `-out=<filename>` — not `-save`, `-export`, or `-write`.

---

### Question 2 — `terraform output -raw` for Scripting

**Difficulty**: Easy
**Answer Type**: one
**Topic**: The -raw flag outputs a single output value as a plain string without surrounding quotes — suitable for shell variable assignment

**Question**:
A shell script needs to capture the database endpoint output value as a plain string for use in another command. When the engineer runs `terraform output db_endpoint`, the result is printed with surrounding quotes: `"rds.example.com"`. Complete the command to get the value without quotes:

```bash
terraform output ___________ db_endpoint
```

What flag fills the blank?

- A) `-plain`
- B) `-string`
- C) `-noformat`
- D) **`-raw`**

**Answer**: D

**Explanation**:
`terraform output -raw <name>` outputs a single string output value with no surrounding quotes, no trailing newline when piped, and no additional formatting — making it suitable for direct shell variable assignment: `DB_HOST=$(terraform output -raw db_endpoint)`. Without `-raw`, `terraform output db_endpoint` prints the value with its type annotation and quotes. The `-json` flag (not shown as an option here) outputs all values as a JSON object. `-raw` is only valid for string-type outputs; using it on a list or map output will produce an error. `-plain`, `-string`, and `-noformat` are not valid `terraform output` flags.

---

### Question 3 — `terraform workspace show`

**Difficulty**: Easy
**Answer Type**: one
**Topic**: The workspace show subcommand prints the name of the currently active workspace

**Question**:
An engineer is working in a terminal and cannot remember which workspace is currently active. Complete the command to display the current workspace name:

```bash
terraform workspace ___________
```

What subcommand fills the blank?

- A) `current`
- B) `active`
- C) `status`
- D) **`show`**

**Answer**: D

**Explanation**:
`terraform workspace show` prints the name of the currently active Terraform workspace to stdout — for example, `staging` or `default`. This is useful in scripts and shell prompts to conditionally behave based on the active workspace. The full workspace subcommand set is: `list` (show all), `new <name>` (create), `select <name>` (switch), `delete <name>` (remove), and `show` (display current). `current`, `active`, and `status` are not valid workspace subcommands.

---

### Question 4 — `terraform fmt -diff` Shows Changes Without Writing

**Difficulty**: Medium
**Answer Type**: one
**Topic**: The -diff flag prints the formatting diff to stdout without modifying any files on disk

**Question**:
An engineer wants to see exactly what `terraform fmt` would change in their files — without actually writing those changes to disk. Complete the command:

```bash
terraform fmt ___________
```

What flag fills the blank?

- A) `-preview`
- B) `-dry-run`
- C) `-show`
- D) **`-diff`**

**Answer**: D

**Explanation**:
`terraform fmt -diff` computes the canonical format for each `.tf` file and prints the diff to stdout (in unified diff format) without writing any changes to disk. This is useful when an engineer wants to review what formatting corrections would be made before committing to them. It differs from `-check`, which exits non-zero when files need formatting but produces no diff output. Combining both is possible: `terraform fmt -check -diff` exits non-zero AND shows the diff — a common CI pattern that both fails the build and provides actionable output. `-preview`, `-dry-run`, and `-show` are not valid `terraform fmt` flags.

---

### Question 5 — `terraform plan -destroy`

**Difficulty**: Medium
**Answer Type**: one
**Topic**: The -destroy flag on terraform plan shows a preview of what terraform destroy would remove, without making any changes

**Question**:
Before running `terraform destroy` in a production environment, a team wants to review exactly which resources will be deleted. Complete the command that generates a **read-only preview** of the destruction without making any changes:

```bash
terraform plan ___________
```

What flag fills the blank?

- A) `-preview-destroy`
- B) `-simulate-destroy`
- C) `-dry-destroy`
- D) **`-destroy`**

**Answer**: D

**Explanation**:
`terraform plan -destroy` produces an execution plan showing all the resources Terraform would remove if `terraform destroy` were run — using the familiar `-` prefix symbols in the output. No changes are made to infrastructure or state. This is the recommended pre-flight check before a destructive operation. The saved-plan variant also works: `terraform plan -destroy -out=destroy.tfplan` saves the destruction plan, which can then be reviewed and applied with `terraform apply destroy.tfplan` for a fully deterministic, reviewable destroy workflow. `terraform destroy` itself is equivalent to `terraform apply -destroy`, but neither performs a preview — they prompt for and then execute the destruction.

---

### Question 6 — TWO Plan Symbols That Result in a Net-New Resource After Apply

**Difficulty**: Medium
**Answer Type**: many
**Topic**: Both + (pure create) and -/+ (replacement — destroy then create) result in a new resource existing after apply

**Question**:
A `terraform plan` output contains four types of operations. Which TWO operation symbols result in a **brand-new resource object being created in the cloud** after `terraform apply` completes? (Select two.)

- A) **`+`** — a pure create: a new resource that does not yet exist will be provisioned
- B) `~` — an in-place update: the existing resource is modified without replacement
- C) **`-/+`** — a replacement: the existing resource is destroyed and a completely new one is created in its place
- D) `-` — a pure destroy: the existing resource is removed and nothing is created

**Answer**: A, C

**Explanation**:
**(A) `+`** represents a pure creation — Terraform will call the provider's Create API to provision a new resource that currently has no corresponding object in state or in the cloud. **(C) `-/+`** represents a replacement — Terraform must destroy the existing resource and create a brand-new one because the changed attribute (marked `# forces replacement`) cannot be modified in-place; after apply, a new resource with a new ID exists. **(B) `~`** is an in-place update — the same resource continues to exist with modified attribute values, no new object is created. **(D) `-`** is a pure destroy — the resource is removed and nothing is created in its place. Both `+` and `-/+` contribute to the "N to add" count in the plan summary line.

---

### Question 7 — `terraform apply -replace` to Force Recreate a Resource

**Difficulty**: Medium
**Answer Type**: one
**Topic**: The -replace flag forces a specific resource to be destroyed and recreated — the current replacement for the deprecated terraform taint command

**Question**:
An EC2 instance has become unhealthy and an engineer wants to force Terraform to destroy and recreate it on the next apply. The deprecated `terraform taint` command used to handle this. Complete the current (Terraform 1.5+) approach:

```bash
terraform apply ___________="aws_instance.web"
```

What flag fills the blank?

- A) `-recreate`
- B) `-taint`
- C) `-force-replace`
- D) **`-replace`**

**Answer**: D

**Explanation**:
`terraform apply -replace="aws_instance.web"` marks the specified resource for forced replacement: Terraform plans a `-/+` operation (destroy then create) for that resource even if its configuration has not changed, then immediately applies it. This is the current approach introduced in Terraform 0.15.2 and made the primary recommendation with `terraform taint` being deprecated. The `-replace` flag is preferred because it combines the "mark for replacement" and "apply" steps into a single operation with full plan visibility — the engineer sees the `-/+` in the plan before committing. `terraform taint` required a separate state-modification step and could be confusing. `-recreate`, `-taint`, and `-force-replace` are not valid flags.

---

### Question 8 — `terraform init -reconfigure`

**Difficulty**: Medium
**Answer Type**: one
**Topic**: The -reconfigure flag forces terraform init to reconfigure the backend without migrating or asking about existing state

**Question**:
An engineer changes the backend configuration in a CI environment where state migration is handled separately. They want `terraform init` to accept the new backend configuration without prompting about state migration. Complete the command:

```bash
terraform init ___________
```

What flag fills the blank?

- A) `-force`
- B) `-skip-migrate`
- C) `-reset`
- D) **`-reconfigure`**

**Answer**: D

**Explanation**:
`terraform init -reconfigure` forces Terraform to adopt the new backend configuration defined in the `terraform {}` block without asking about migrating existing state or consulting any previous backend configuration. It discards the cached backend configuration and starts fresh with what is currently declared. This is appropriate when: (1) state migration is handled by a separate out-of-band process, (2) switching to a completely different backend type, or (3) the CI environment should not be prompted interactively. The alternative, `terraform init -migrate-state`, attempts to copy the existing state to the new backend. `-force`, `-skip-migrate`, and `-reset` are not valid `terraform init` flags.

---

### Question 9 — `terraform graph` Outputs DOT Format

**Difficulty**: Medium
**Answer Type**: one
**Topic**: terraform graph outputs the resource dependency graph in DOT language format — renderable by Graphviz

**Question**:
Complete the following statement about the `terraform graph` command:

> "Running `terraform graph` prints the resource dependency graph to stdout in ___________ format — a graph description language used by the Graphviz toolset. Pipe the output to `dot -Tsvg > graph.svg` to produce a visual diagram."

What word fills the blank?

- A) JSON
- B) XML
- C) Mermaid
- D) **DOT**

**Answer**: D

**Explanation**:
`terraform graph` outputs the dependency graph between all resources, data sources, and modules in a configuration using the **DOT** graph description language (defined by the Graphviz project). DOT is a simple plain-text format that describes nodes and edges. To turn the DOT output into a visual image, pipe it through Graphviz's `dot` command: `terraform graph | dot -Tsvg > graph.svg` (SVG) or `terraform graph | dot -Tpng > graph.png` (PNG). This is useful for understanding complex dependency chains, debugging unexpected plan ordering, or documenting infrastructure topology. JSON, XML, and Mermaid are not the output format of `terraform graph`.

---

### Question 10 — TWO Flags That Work on Both `terraform plan` and `terraform apply`

**Difficulty**: Medium
**Answer Type**: many
**Topic**: -var and -var-file are valid flags on both terraform plan and terraform apply for supplying input variable values

**Question**:
An engineer is writing a deployment script. They need to pass input variable values to both the plan and apply steps. Which TWO of the following flags are valid on **both** `terraform plan` and `terraform apply`? (Select two.)

- A) **`-var "region=us-east-1"`** — passes a single variable value inline; accepted by both plan and apply
- B) `-approve` — skips the apply confirmation prompt; only valid on apply
- C) `-out=plan.tfplan` — saves the plan to a file; only valid on plan
- D) **`-var-file=prod.tfvars`** — loads variable values from a `.tfvars` file; accepted by both plan and apply

**Answer**: A, D

**Explanation**:
Both `terraform plan` and `terraform apply` accept variable-supplying flags because both commands may need to evaluate the full configuration (and therefore resolve variable values). **(A) `-var "key=value"`** passes a single variable value inline and is valid on both. **(D) `-var-file=<file>`** loads a file of variable assignments (`.tfvars` format) and is also valid on both. Using the same flags on both commands ensures the plan and apply see identical variable values — critical for the two-stage CI pattern where `plan` and `apply` run as separate steps (though in that case a saved plan file is even better). **(B) `-approve`** does not exist — the flag is `-auto-approve`, and it only applies to `terraform apply`. **(C) `-out=`** saves a plan file and is only a `terraform plan` flag.

---

### Question 11 — Applying a Saved Plan File Skips the Confirmation Prompt

**Difficulty**: Medium
**Answer Type**: one
**Topic**: When terraform apply is given a saved plan file as an argument, it does not pause for interactive confirmation — the plan was already reviewed

**Question**:
Complete the following statement:

> "When `terraform apply` is given a saved plan file as its argument — for example, `terraform apply plan.tfplan` — it does ___________ pause to prompt `Do you want to perform these actions?` because the operator reviewed the plan before saving it."

What word fills the blank?

- A) always
- B) sometimes
- C) only briefly
- D) **not**

**Answer**: D

**Explanation**:
When you run `terraform apply plan.tfplan` (providing a saved plan file as the argument), Terraform applies the plan **without pausing for confirmation** — it assumes the operator already reviewed the output of `terraform plan -out=plan.tfplan` and is now intentionally executing those changes. This is one of the key reasons the two-stage `plan -out` → `apply <file>` pattern is used in CI/CD: it separates the review step (plan) from the execution step (apply) and makes the apply step deterministic and non-interactive without requiring the `-auto-approve` flag. In contrast, running `terraform apply` without a saved plan file always shows the plan and then pauses for confirmation unless `-auto-approve` is provided.

---

### Question 12 — `terraform console` is an Interactive REPL

**Difficulty**: Hard
**Answer Type**: one
**Topic**: terraform console is an interactive REPL for evaluating HCL expressions, testing functions, and inspecting state values without modifying anything

**Question**:
Complete the following description:

> "`terraform console` opens an interactive ___________ (Read-Eval-Print Loop) where engineers can type HCL expressions — such as `length([\"a\",\"b\",\"c\"])` or `format(\"%s-%s\", var.env, var.region)` — and immediately see the evaluated result. This is useful for testing functions and expressions before using them in configuration files."

What acronym fills the blank?

- A) CLI
- B) API
- C) IDE
- D) **REPL**

**Answer**: D

**Explanation**:
`terraform console` is an interactive **REPL** (Read-Eval-Print Loop) — a shell-like interface where each expression entered is read, evaluated against the current configuration and state context, and its result printed immediately. Engineers use it to: experiment with built-in functions (`cidrsubnet`, `format`, `toset`, etc.) before putting them in `.tf` files; inspect computed values from state (e.g., `aws_instance.web.public_ip`); and verify that complex expressions like `for` expressions produce the expected output. The console does not modify infrastructure or state — it is purely a read/evaluate tool. `terraform console` requires `terraform init` to have been run (so providers and modules are available) but makes no cloud API calls.

---

### Question 13 — TWO Items That `terraform init` Downloads and Configures

**Difficulty**: Hard
**Answer Type**: many
**Topic**: terraform init downloads provider plugin binaries AND caches module source code — both go into subdirectories of .terraform/

**Question**:
A developer runs `terraform init` in a working directory that has both `required_providers` declarations and `module` blocks sourcing external modules. Which TWO items does `terraform init` download and set up in the working directory? (Select two.)

- A) **Provider plugin binaries** — downloaded from the Terraform Registry (or a mirror) into `.terraform/providers/`, based on the `required_providers` block; the exact versions installed are recorded in `.terraform.lock.hcl`
- B) The Terraform Core binary itself — `terraform init` checks for a newer CLI version and auto-updates the `terraform` executable
- C) **Module source code** — external module sources (registry modules, Git repos, or HTTP archives referenced in `module` blocks) are downloaded and cached into `.terraform/modules/`, making them available for plan and apply
- D) The `terraform.tfstate` file — `terraform init` bootstraps an empty state file if one does not already exist

**Answer**: A, C

**Explanation**:
`terraform init` performs three main setup operations: **(A)** it reads the `required_providers` block and downloads each provider plugin binary into `.terraform/providers/`, recording the exact version and checksum in `.terraform.lock.hcl`; **(C)** it reads all `module` blocks that reference external sources (Terraform Registry modules, Git URLs, HTTP archives, etc.) and downloads them into `.terraform/modules/`, making the module code available for subsequent plan/apply operations. It also configures the backend (if declared). **(B)** is false — `terraform init` never modifies the Terraform CLI binary itself; CLI upgrades are performed separately (e.g., via `tfenv`, package managers, or manual download). **(D)** is false — `terraform init` does not create `terraform.tfstate`; the state file is created on the first `terraform apply` when resources are provisioned.

---
