# Terraform Associate Exam Questions

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

## Answer Key

| Q# | Answer(s) | Explanation | Source | Difficulty |
|----|-----------|-----------:|--------|------------|
| 1 | C | N/A | The `-out` flag saves the execution plan to a binary file for a deterministic later apply | Easy |
| 2 | D | N/A | The -raw flag outputs a single output value as a plain string without surrounding quotes — suitable for shell variable assignment | Easy |
| 3 | D | N/A | The workspace show subcommand prints the name of the currently active workspace | Easy |
| 4 | D | N/A | The -diff flag prints the formatting diff to stdout without modifying any files on disk | Medium |
| 5 | D | N/A | The -destroy flag on terraform plan shows a preview of what terraform destroy would remove, without making any changes | Medium |
| 6 | A, C | N/A | Both + (pure create) and -/+ (replacement — destroy then create) result in a new resource existing after apply | Medium |
| 7 | D | N/A | The -replace flag forces a specific resource to be destroyed and recreated — the current replacement for the deprecated terraform taint command | Medium |
| 8 | D | N/A | The -reconfigure flag forces terraform init to reconfigure the backend without migrating or asking about existing state | Medium |
| 9 | D | N/A | terraform graph outputs the resource dependency graph in DOT language format — renderable by Graphviz | Medium |
| 10 | A, D | N/A | -var and -var-file are valid flags on both terraform plan and terraform apply for supplying input variable values | Medium |
| 11 | D | N/A | When terraform apply is given a saved plan file as an argument, it does not pause for interactive confirmation — the plan was already reviewed | Medium |
| 12 | D | N/A | terraform console is an interactive REPL for evaluating HCL expressions, testing functions, and inspecting state values without modifying anything | Hard |
| 13 | A, C | N/A | terraform init downloads provider plugin binaries AND caches module source code — both go into subdirectories of .terraform/ | Hard |
