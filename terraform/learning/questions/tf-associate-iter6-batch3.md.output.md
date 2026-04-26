# Terraform Associate Exam Questions

---

### Question 1 — CI Pipeline Fails Because Files Are Not Formatted

**Difficulty**: Easy
**Answer Type**: one
**Topic**: Using terraform fmt -check in CI to enforce formatting without writing files

**Question**:
A team's CI pipeline runs `terraform fmt` as a formatting gate. A developer notices that every time the pipeline runs, it reformats the committed files and then reports a diff that must be manually committed. The team wants the pipeline to **report a failure** when files are unformatted rather than silently rewrite them. What is the correct flag to use?

- A) `terraform fmt -dry-run` — preview changes without writing to disk
- B) `terraform fmt -no-write` — display unformatted files without modifying them
- C) `terraform fmt -check` — this flag makes `terraform fmt` **exit with a non-zero exit code** if any `.tf` files need reformatting, without writing any changes to disk; the CI pipeline fails on the non-zero exit, prompting the developer to format their code locally and recommit; this is the standard CI usage of `fmt`
- D) `terraform fmt -validate` — combines formatting and validation in a single pass

---

### Question 2 — `terraform validate` Passes But `terraform plan` Fails

**Difficulty**: Easy
**Answer Type**: one
**Topic**: Understanding the boundary between what validate checks (static) and what plan checks (live)

**Question**:
An engineer runs `terraform validate` on a configuration that references an AMI ID: `ami = "ami-0deadbeef1234567"`. Validation passes. They then run `terraform plan` and receive an error: `InvalidAMIID.NotFound: The image id '[ami-0deadbeef1234567]' does not exist`. The engineer is confused — they thought `validate` would catch this. What explains the discrepancy?

- A) `terraform validate` only checks files in the root module; AMI references in child modules are skipped
- B) `terraform validate` is **fully offline and makes no API calls** — it checks HCL syntax and static references but cannot verify whether cloud resources such as AMI IDs actually exist; `terraform plan` calls the AWS provider API, which verifies the AMI ID against the AWS catalogue and returns the error when it is not found; `validate` passing is correct — it cannot know the AMI is invalid without querying AWS
- C) `terraform validate` found the error but suppressed it because `ami` is a computed attribute
- D) `terraform plan` is stricter than `validate` because it re-parses the `.tf` files from scratch

---

### Question 3 — Apply Prompt Appears Unexpectedly in Automation

**Difficulty**: Easy
**Answer Type**: one
**Topic**: Using -auto-approve to suppress the interactive apply confirmation in CI/CD

**Question**:
An engineer sets up a CI/CD pipeline that runs `terraform apply` as the final step. The pipeline hangs indefinitely after printing the execution plan, waiting for user input. The engineer needs the apply to proceed automatically without prompting. What is the correct fix?

- A) Set the environment variable `TF_APPLY_AUTO=true` before running `terraform apply`
- B) Run `terraform apply -no-prompt` to skip the confirmation dialog
- C) Add **`-auto-approve`** to the `terraform apply` command — this flag suppresses the interactive confirmation prompt and applies the plan immediately; it is the standard flag for non-interactive environments such as CI/CD pipelines; without it, `terraform apply` always pauses and waits for `yes` before proceeding
- D) Use `terraform apply -force` to bypass the confirmation check

---

### Question 4 — `-target` Used Regularly Causes State Drift

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Understanding why routine use of -target is an anti-pattern and what problems it causes

**Question**:
An engineer discovers they can run `terraform apply -target=aws_instance.web` to apply changes faster, skipping the other 40 resources in the configuration. They start using `-target` routinely for every change. A senior engineer warns them this is dangerous. What is the most likely problem this practice will cause over time?

- A) Using `-target` more than three times in a row permanently locks the state file
- B) `terraform apply -target` does not update the state file for the targeted resource — changes are applied to the cloud but not recorded
- C) **Routine use of `-target` causes state drift**: when only a subset of resources is planned and applied, Terraform does not evaluate the full dependency graph; changes to the targeted resource may leave dependent resources in an inconsistent or stale state that Terraform is unaware of; over time, the state file diverges from the full desired configuration, and a full `terraform apply` may plan unexpected changes or errors because the inter-resource relationships were never reconciled; `-target` is intended only for emergency recovery or one-off debugging, not routine use
- D) `-target` is deprecated in Terraform 1.x and will be removed in a future version

---

### Question 5 — Saved Plan File Applied After Configuration Change

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Understanding that a saved plan file is tied to the state and config at the time it was created

**Question**:
An engineer runs `terraform plan -out=plan.tfplan` and saves the plan. Before running `terraform apply plan.tfplan`, a colleague merges a pull request that adds a new resource to the configuration. The engineer applies the saved plan. What is the most likely problem?

- A) Terraform detects the configuration change and automatically re-plans before applying
- B) The apply fails immediately with a "plan file is out of date" error that prevents any changes from being made
- C) The **saved plan was generated against the configuration and state at the time `terraform plan` was run** — it does not include the new resource added by the colleague's PR; applying it will provision only the changes in the saved plan, not the new resource; the new resource will not be created until a fresh `terraform plan` and `terraform apply` are run; in some versions of Terraform, if the state has diverged significantly from the plan's recorded state, Terraform will also emit a warning or error
- D) The apply creates the new resource automatically because Terraform reads the current configuration files during `terraform apply plan.tfplan`

---

### Question 6 — `terraform graph` Output Is Unreadable

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Understanding that terraform graph outputs DOT format and requires an external tool to render

**Question**:
An engineer runs `terraform graph` to visualise the resource dependency graph. The terminal output is a large block of text that looks like this:

```
digraph {
  compound = "true"
  newrank  = "true"
  subgraph "root" {
    "[root] aws_instance.web (expand)" -> "[root] aws_security_group.allow_ssh (expand)"
  }
}
```

The engineer expects a visual diagram but sees only text. What is the correct explanation and next step?

- A) The engineer must run `terraform graph -render` to trigger the visual rendering
- B) `terraform graph` outputs the graph in **DOT format** — a plain-text graph description language used by the Graphviz tool; the text output is correct and expected; to render it as a visual diagram, the engineer should pipe the output to Graphviz: `terraform graph | dot -Tsvg > graph.svg` and then open `graph.svg` in a browser or image viewer
- C) The output indicates a circular dependency in the configuration — the `->` arrows show the cycle that must be fixed
- D) The DOT output is only generated when there are dependency errors; normal graphs are rendered as PNGs automatically

---

### Question 7 — `terraform output` Returns Nothing After Apply

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Understanding why terraform output returns nothing when no output blocks are declared

**Question**:
An engineer provisions infrastructure with `terraform apply`. After apply completes, they run `terraform output` expecting to see resource IDs and IP addresses, but the command prints nothing. The engineer is confused because the apply succeeded. What is the most likely cause?

- A) `terraform output` requires the `-state` flag to point to the state file — without it, the command cannot find the output values
- B) Output values are only available for 24 hours after apply; running the command the next day always returns nothing
- C) The engineer's configuration has **no `output` blocks declared** — `terraform output` can only display values that are explicitly defined in `output` blocks in the configuration; Terraform does not automatically expose resource attributes as outputs; to see the instance ID, the engineer must add an `output` block such as `output "instance_id" { value = aws_instance.web.id }` and re-apply
- D) The outputs were cleared because `terraform apply` was run with `-auto-approve`

---

### Question 8 — Plan Shows Resource Replaced When Only a Tag Changed

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Understanding that certain attributes force resource replacement and how to recognise this in plan output

**Question**:
An engineer changes only the `Name` tag on an RDS database instance and runs `terraform plan`. They expect to see `1 to change` (an in-place update) but instead see `-/+ 1 to add, 1 to destroy` with the note `# forces replacement`. The engineer is alarmed — they did not intend to recreate the database. What is the most likely explanation?

- A) Changing a tag on any AWS resource always forces a full replacement in Terraform — tag changes are never applied in place
- B) The engineer accidentally changed the `engine_version` attribute instead of the tag; engine version changes always force replacement
- C) **Some resource attributes are marked `ForceNew` in the provider schema** — changing them requires the resource to be destroyed and recreated because the underlying cloud API does not support in-place updates for that attribute; however, `Name` tags on RDS instances are not normally `ForceNew`; the most likely explanation is that the engineer also changed (intentionally or accidentally) a `ForceNew` attribute such as `identifier`, `engine`, `engine_version`, or `db_subnet_group_name` alongside the tag change; the plan output's `# forces replacement` note will list the specific attribute responsible
- D) `-/+` in the plan always means the engineer has changed more than five attributes at once, triggering a safety replacement

---

### Question 9 — `terraform console` Used to Debug an Unexpected Expression

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Using terraform console to test and debug HCL expressions interactively before embedding in config

**Question**:
An engineer writes a complex `for` expression in their configuration but is unsure whether it produces the expected output. They keep running `terraform plan` to test it, but the plan is slow because it refreshes 300 resources each time. What is the most efficient way to test the expression in isolation?

- A) Run `terraform validate --expression` to evaluate and print the result of a single HCL expression
- B) Create a separate test `.tf` file with just the expression and run `terraform apply` on it in an empty workspace
- C) Use **`terraform console`** — an interactive REPL (Read-Eval-Print Loop) that evaluates HCL expressions against the current state and variable values without running a full plan or making any provider API calls; the engineer can type the `for` expression directly at the prompt and see the result immediately, iterating quickly until the output is correct before embedding it in the configuration
- D) Use `terraform output --eval` to evaluate an expression without declaring an output block

---

### Question 10 — `terraform destroy` Run in Wrong Workspace

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Understanding terraform workspaces and the risk of running destructive commands in the wrong workspace

**Question**:
An engineer intends to destroy the `staging` environment. They run `terraform destroy -auto-approve` but realise halfway through that they are in the `default` workspace, which corresponds to the **production** environment. What TWO immediate actions should the engineer take? (Select two.)

**Answer Type**: many

- A) **Run `terraform apply -auto-approve` immediately** — `terraform apply` in the same workspace will recreate all the destroyed resources from the configuration files
- B) Run `terraform workspace select staging` to move to the correct workspace — this does not undo the destruction already performed in the `default` workspace
- C) Escalate to the team and use the **remote backend's state version history** (if available) to identify exactly which resources were destroyed and what their configuration was, then prioritise restoring production resources — either by re-running `terraform apply` or by recovering from backup depending on the resource type
- D) Run `terraform plan -destroy` — this re-creates the destroy plan and effectively reverses the previous destroy

---

### Question 11 — `terraform apply -replace` vs Deleting from Config

**Difficulty**: Hard
**Answer Type**: one
**Topic**: Understanding terraform apply -replace as the correct way to force-recreate a resource without removing it from config

**Question**:
An EC2 instance has become corrupted. An engineer needs to destroy and recreate it using its current Terraform configuration, without changing any configuration attributes. A colleague suggests removing the resource block from the configuration, running `terraform apply`, and then adding it back and running `terraform apply` again. What is the problem with this approach, and what is the correct alternative?

- A) There is no problem — removing and re-adding a resource block is the standard Terraform procedure for recreating a resource
- B) The two-step remove-and-add approach has two significant problems: (1) removing the block plans a destroy, which deletes the instance — this is correct — but (2) re-adding the block then plans a **create of a brand-new instance** which has a **different resource ID, IP, and configuration** than the original; this process also requires two separate apply operations, increasing the window for errors; the correct approach is **`terraform apply -replace=aws_instance.web`**, which plans a single destroy-then-recreate (shown as `-/+` in the plan) in one apply operation, preserving all configuration attributes and minimising the outage window
- C) The approach is correct but only works if `lifecycle { create_before_destroy = true }` is set on the resource block
- D) The two-step approach is required because `terraform apply -replace` is only available in Terraform Enterprise

---

### Question 12 — `terraform output -raw` vs `terraform output` for Scripting

**Difficulty**: Hard
**Answer Type**: one
**Topic**: Understanding why -raw is needed when using terraform output in shell scripts

**Question**:
An engineer writes a deployment script that retrieves a database endpoint from Terraform outputs:

```bash
DB_HOST=$(terraform output db_endpoint)
psql -h "$DB_HOST" -U admin mydb
```

The `psql` connection fails with: `could not translate host name '"db.example.com"' to address`. The engineer notices the hostname has double-quote characters around it. What is the cause and fix?

- A) The output block must include `quote = false` to suppress quote characters in the returned value
- B) The `terraform output` command returns values in **HCL-formatted strings with surrounding double quotes** by default (e.g., `"db.example.com"`); when this is captured in a shell variable, the quotes become part of the string value passed to `psql`; the fix is to use **`terraform output -raw db_endpoint`** — the `-raw` flag returns the value as a plain string without any surrounding quotes or newline formatting, making it safe for direct use in shell scripts and command substitutions
- C) The issue is that `psql` does not accept hostnames from environment variables — the engineer should hard-code the hostname in the script
- D) The output value must be marked `sensitive = true` to strip the formatting characters before shell capture

---

### Question 13 — `terraform plan -destroy` Unexpected Scope

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Understanding that terraform plan -destroy plans destruction of ALL resources, not just unused ones

**Question**:
An engineer runs `terraform plan -destroy` expecting it to plan the removal of only the resources that are no longer in the configuration (i.e., orphaned resources). Instead, the plan shows all 47 managed resources will be destroyed. The engineer panics and asks: "Is something wrong?" What is the correct explanation?

- A) `terraform plan -destroy` has detected that all 47 resources are misconfigured and must be replaced — the engineer should review each resource
- B) `terraform plan -destroy` plans the **destruction of ALL resources currently tracked in state**, regardless of whether they are in the configuration or not — it is equivalent to removing every resource block and running `terraform plan`; it is used when the intention is to completely tear down the environment; it does not selectively destroy only orphaned resources; to remove only resources that have been removed from configuration, the engineer should simply run a normal `terraform plan` and look for any `-` (destroy) entries
- C) Something is wrong with the state file — `terraform plan -destroy` should never show more than 10 resources
- D) The engineer accidentally appended `-destroy` to their `terraform plan -target` command, overriding the target scope

## Answer Key

| Q# | Answer(s) | Explanation | Source | Difficulty |
|----|-----------|-----------:|--------|------------|
| 1 | C | N/A | Using terraform fmt -check in CI to enforce formatting without writing files | Easy |
| 2 | B | N/A | Understanding the boundary between what validate checks (static) and what plan checks (live) | Easy |
| 3 | C | N/A | Using -auto-approve to suppress the interactive apply confirmation in CI/CD | Easy |
| 4 | C | N/A | Understanding why routine use of -target is an anti-pattern and what problems it causes | Medium |
| 5 | C | N/A | Understanding that a saved plan file is tied to the state and config at the time it was created | Medium |
| 6 | B | N/A | Understanding that terraform graph outputs DOT format and requires an external tool to render | Medium |
| 7 | C | N/A | Understanding why terraform output returns nothing when no output blocks are declared | Medium |
| 8 | C | N/A | Understanding that certain attributes force resource replacement and how to recognise this in plan output | Medium |
| 9 | C | N/A | Using terraform console to test and debug HCL expressions interactively before embedding in config | Medium |
| 10 | A, C | N/A | Understanding terraform workspaces and the risk of running destructive commands in the wrong workspace | Medium |
| 11 | B | N/A | Understanding terraform apply -replace as the correct way to force-recreate a resource without removing it from config | Hard |
| 12 | B | N/A | Understanding why -raw is needed when using terraform output in shell scripts | Hard |
| 13 | B | N/A | Understanding that terraform plan -destroy plans destruction of ALL resources, not just unused ones | Medium |
