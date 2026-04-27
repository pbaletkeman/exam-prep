# Terraform Associate Exam Questions

---

### Question 1

**Difficulty:** Easy
**Answer Type:** one
**Topic:** `terraform graph` output format — which statement is TRUE?

Which of the following statements about `terraform graph` is TRUE?

A) `terraform graph` outputs the resource dependency graph as an SVG image file directly to disk — the file is saved to `graph.svg` in the working directory by default and can be opened in any browser
B) `terraform graph` generates an interactive HTML page that visualises the dependency graph in the browser, similar to a network diagram tool
C) `terraform graph` outputs the dependency graph as plain text in DOT format — DOT is a graph description language processed by external tools such as Graphviz (`dot -Tsvg`) to render a visual diagram; `terraform graph` itself only writes DOT text to stdout
D) `terraform graph` produces JSON output compatible with `terraform show -json`, allowing the dependency graph to be merged with state data for reporting purposes

---

### Question 2

**Difficulty:** Easy
**Answer Type:** one
**Topic:** `terraform show` — which statement is FALSE?

Which of the following statements about `terraform show` is FALSE?

A) `terraform show` displays the contents of the current `terraform.tfstate` in a human-readable format — useful for inspecting what Terraform knows about existing managed resources
B) `terraform show plan.tfplan` reads and displays a previously saved plan file in human-readable format — this allows engineers to review exactly what changes a plan captured before applying it
C) `terraform show -json` outputs the current state as a JSON object — this is the machine-readable form useful for feeding state data into scripts, dashboards, or external tooling
D) `terraform show` modifies the state file to refresh attribute values from the live cloud API — every time it is run, it updates the recorded state with the latest resource attributes

---

### Question 3

**Difficulty:** Easy
**Answer Type:** many
**Topic:** Network and state-modification characteristics of CLI commands — which TWO are TRUE?

Which TWO of the following statements about Terraform command characteristics are TRUE?

A) `terraform validate` requires a network connection to download provider schemas before it can check argument names and types — without internet access, `validate` will fail
B) `terraform apply` both requires a network connection (to make cloud API calls) and modifies the state file (to record the results of changes made) — it is one of the few commands that both connects to the network AND writes to state
C) `terraform plan` modifies the state file with the proposed changes so that `terraform apply` can read them from state — a plan without `-out` still writes the proposed plan to state
D) `terraform output` and `terraform show` both require a network connection to retrieve the latest resource attribute values directly from the cloud provider API

---

### Question 4

**Difficulty:** Medium
**Answer Type:** one
**Topic:** `terraform taint` deprecation — which statement is TRUE?

Which of the following statements about forcing a resource to be destroyed and recreated is TRUE?

A) `terraform taint aws_instance.web` is the current, recommended command in Terraform 1.5+ for marking a resource for forced replacement on the next apply — it is stable and has no plans for removal
B) `terraform apply -replace="aws_instance.web"` is the current approach in Terraform 1.5+ for forcing a resource to be destroyed and recreated in a single atomic operation — `terraform taint` is deprecated in favour of this flag
C) `terraform apply -replace` destroys the specified resource immediately without generating a plan preview — it is equivalent to running `terraform destroy -target` followed by `terraform apply`
D) Both `terraform taint` and `terraform apply -replace` mark the resource for replacement but differ in timing: `taint` takes effect immediately; `-replace` defers replacement until the next scheduled maintenance window

---

### Question 5

**Difficulty:** Medium
**Answer Type:** one
**Topic:** `terraform init -upgrade` — which statement is FALSE?

Which of the following statements about `terraform init -upgrade` is FALSE?

A) `terraform init -upgrade` instructs Terraform to ignore the version constraints recorded in `.terraform.lock.hcl` and resolve the newest provider version that satisfies the `version` constraint declared in `required_providers`
B) After running `terraform init -upgrade`, the `.terraform.lock.hcl` file is rewritten to record the new provider version and updated hashes — future plain `terraform init` runs will install this newer version
C) `terraform init -upgrade` is required any time you want to advance a provider past the version currently recorded in the lock file — running plain `terraform init` will always install the exact locked version and never upgrade it
D) `terraform init -upgrade` also upgrades the Terraform CLI binary to the latest available release — after the command completes, `terraform -version` will report a newer version if one is available

---

### Question 6

**Difficulty:** Medium
**Answer Type:** one
**Topic:** `terraform plan -destroy` — which statement is TRUE?

Which of the following statements about `terraform plan -destroy` is TRUE?

A) `terraform plan -destroy` immediately destroys all resources managed by the configuration — it is equivalent to `terraform destroy -auto-approve` because the `-destroy` flag implies immediate execution
B) `terraform plan -destroy` generates a destroy plan showing which resources would be deleted and in what order, but does NOT execute any changes — it is the preview-only equivalent of `terraform destroy`, useful for reviewing what will be removed before committing to destruction
C) `terraform plan -destroy` can only be used with the `-target` flag — without a target, it returns an error saying that a full destroy requires `terraform destroy` instead
D) `terraform plan -destroy` creates a special read-only state snapshot that Terraform Cloud can use to automatically schedule and execute the destroy — it cannot be applied locally

---

### Question 7

**Difficulty:** Medium
**Answer Type:** one
**Topic:** `terraform apply -replace` — which statement is TRUE?

Which of the following statements about `terraform apply -replace` is TRUE?

A) `terraform apply -replace="aws_instance.web"` only destroys the specified resource — after the destroy, the resource must be manually re-added to the configuration and applied again to recreate it
B) `terraform apply -replace="aws_instance.web"` forces Terraform to destroy and then recreate the specified resource within a single apply, even if no configuration changes have been made to that resource; Terraform marks the resource for replacement in the generated plan (shown with the `-/+` symbol) before proceeding
C) `terraform apply -replace` is a hidden alias for `terraform taint` — both commands are fully equivalent and neither is deprecated
D) `terraform apply -replace="aws_instance.web"` only recreates the instance if the EC2 API reports it is in a degraded or stopped state — Terraform checks the live resource health before deciding whether replacement is warranted

---

### Question 8

**Difficulty:** Medium
**Answer Type:** one
**Topic:** `terraform fmt -diff` — which statement is FALSE?

Which of the following statements about `terraform fmt` flags used for preview purposes is FALSE?

A) `terraform fmt -diff` displays a unified diff showing exactly what formatting changes WOULD be made to each `.tf` file, without writing any changes to disk — it is useful for reviewing formatting issues in a code review context
B) `terraform fmt -check` exits with code 1 if any files need reformatting, without writing changes — it is designed for CI enforcement gates
C) `terraform fmt -diff` and `terraform fmt -check` can be combined: `terraform fmt -check -diff` will both exit with code 1 AND display the formatting diff for each non-compliant file — this is the most informative CI usage because it both fails the pipeline and shows the engineer exactly what needs to be fixed
D) `terraform fmt -diff` rewrites all `.tf` files to canonical format AND generates a diff report showing a summary of character-level changes — unlike `-check`, it still writes files to disk while also producing the diff output

---

### Question 9

**Difficulty:** Medium
**Answer Type:** many
**Topic:** `terraform console` — which TWO statements are TRUE?

Which TWO of the following statements about `terraform console` are TRUE?

A) `terraform console` is an interactive REPL (Read-Eval-Print Loop) that evaluates HCL expressions and Terraform built-in functions — it is useful for testing expressions like `format()`, `length()`, `toset()`, and `cidrsubnet()` before embedding them in configuration
B) `terraform console` modifies the state file when it evaluates expressions that reference managed resources — querying `aws_instance.web.id` in the console makes an API call and refreshes the stored attribute value
C) `terraform console` requires no network connection and does not modify the state file — it reads the existing state for resource attribute values but makes no API calls and writes nothing; it is a safe, side-effect-free tool for expression testing
D) `terraform console` can only evaluate simple arithmetic expressions — it does not support Terraform-specific functions, resource references, or variable lookups because it runs outside the context of the configuration

---

### Question 10

**Difficulty:** Medium
**Answer Type:** one
**Topic:** `terraform init -migrate-state` vs `-reconfigure` — which statement is TRUE?

Which of the following statements about `terraform init` backend reconfiguration flags is TRUE?

A) `-migrate-state` and `-reconfigure` are aliases for the same flag — both instruct Terraform to reset the backend configuration without any state migration, and the choice between them is purely stylistic
B) `terraform init -migrate-state` is used when changing to a new backend and offers to copy or migrate existing state from the old backend to the new one — Terraform prompts the engineer to confirm the migration before proceeding; `-reconfigure` resets the backend configuration without attempting to migrate state, discarding the old backend connection
C) `terraform init -reconfigure` is required when adding a backend configuration for the very first time to a configuration that previously had no backend block — without it, `terraform init` refuses to configure a backend from scratch
D) `terraform init -migrate-state` bypasses all confirmation prompts and automatically migrates state to the new backend without any human interaction — it is equivalent to combining `-migrate-state -auto-approve`

---

### Question 11

**Difficulty:** Medium
**Answer Type:** one
**Topic:** `terraform output -json` — which statement is FALSE?

Which of the following statements about `terraform output -json` is FALSE?

A) `terraform output -json` outputs ALL declared output values from the current state as a single JSON object — each output name is a key, and the value includes the output's value and type metadata
B) `terraform output -json` is useful for machine-readable consumption — scripts and external tools can parse the JSON object to extract specific output values programmatically without screen-scraping human-readable text
C) `terraform output -json` requires a network connection to query the live cloud provider API for the latest attribute values before generating the JSON output
D) `terraform output -json` reads output values from the local state file — no network calls are made; the JSON reflects what is currently recorded in state, which was last updated on the most recent `terraform apply`

---

### Question 12

**Difficulty:** Hard
**Answer Type:** one
**Topic:** Four statements about `terraform plan` — only ONE is TRUE

Four statements about `terraform plan` are presented below. Which is the ONLY TRUE statement?

A) `terraform plan` modifies the state file at the end of its execution to record the proposed changes — this ensures that `terraform apply` (run immediately after) can skip the planning phase and go directly to execution, making apply faster
B) Running `terraform plan -out=plan.tfplan` followed by `terraform apply plan.tfplan` guarantees that the apply executes exactly the changes shown in the plan — the apply phase cannot generate new or different changes because it reads the serialised plan, not the live configuration
C) `terraform plan` and `terraform apply` are functionally equivalent — the only difference is that `apply` prompts the engineer to confirm before making changes, whereas `plan` proceeds without confirmation; both commands modify cloud resources
D) `terraform plan -refresh=false` is always more accurate than a standard `terraform plan` because skipping the API refresh prevents stale data from the cloud provider from interfering with Terraform's change calculation

---

### Question 13

**Difficulty:** Hard
**Answer Type:** many
**Topic:** `terraform import` — which TWO statements are TRUE?

Which TWO of the following statements about importing existing infrastructure into Terraform state are TRUE?

A) The legacy `terraform import` CLI command (pre-1.5 style) requires that a corresponding resource block already exist in the `.tf` configuration before you run the import — Terraform uses the resource block to know which resource type to import; running `import` without an existing block produces an error
B) The `import` block introduced in Terraform 1.5+ allows infrastructure import to be declared directly in HCL — Terraform generates a plan showing the import operation before executing it, making the process reviewable and version-controlled alongside the rest of the configuration
C) Both the legacy `terraform import` CLI command and the newer `import` block in HCL automatically generate the complete resource configuration block — after running either form of import, the `.tf` configuration is fully populated with all resource arguments so no manual HCL authoring is needed
D) `terraform import` adds the imported resource to the state file and simultaneously deletes the resource from the cloud provider — it is designed to "take over" management of existing resources by moving them entirely under Terraform's control, including removing their independent existence

## Answer Key

| Q# | Answer(s) | Explanation | Source | Difficulty |
|----|-----------|-----------:|--------|------------|
| 1 | C | ** `terraform graph` outputs the resource dependency graph in **DOT format** — a plain-text graph description language used by the Graphviz suite. The output is written to stdout, not to any file. To produce a rendered image, you pipe the output to a Graphviz tool: `terraform graph | dot -Tsvg > graph.svg` creates an SVG, or `terraform graph | dot -Tpng > graph.png` creates a PNG. `terraform graph` itself has no rendering capability — it only generates the DOT text description. Option A is false — no SVG is written automatically. Option B is false — there is no HTML or browser-based output. Option D is false — `terraform graph` output is DOT, not JSON, and is entirely separate from state data. | ** `terraform graph` output format — which statement is TRUE? | ** Easy |
| 2 | D | ** Option D is FALSE. `terraform show` is a purely **read-only, offline** inspection command — it reads the existing state file (or a saved plan file) and displays its contents; it makes no API calls and writes nothing to disk. It does NOT refresh or modify the state file in any way. To refresh state with live cloud values, the correct command is `terraform apply -refresh-only` (or `terraform plan -refresh-only` to preview). `terraform show` is safe to run at any time with no side effects. Options A, B, and C are all accurate: `terraform show` displays current state, `terraform show plan.tfplan` inspects a saved plan, and `terraform show -json` outputs the state as machine-readable JSON. | ** `terraform show` — which statement is FALSE? | ** Easy |
| 3 | A is FALSE, B is TRUE, C is FALSE, D is FALSE → **Answer: B only** | ** **(A)** is TRUE. `terraform validate` is entirely offline. The provider schema needed to validate argument names and types is cached locally in `.terraform/providers/` by `terraform init`. Once init has been run, validate never makes a network call — this is one of its key advantages for fast local feedback and offline/CI environments. **(B)** is TRUE. `terraform apply` is the primary command that requires both network access AND writes to state. It connects to cloud provider APIs to perform CRUD operations and, after each resource change, writes the updated attributes back to the state file so subsequent plans have accurate known state. **(C)** is FALSE — `terraform plan` without `-out` does NOT persist the plan anywhere. If you run `terraform apply` immediately after without a plan file, Terraform generates a NEW plan at apply time (and prompts for confirmation). The `-out=` flag is specifically what saves a plan to disk. **(D)** is FALSE — `terraform output` reads output values from the local state file without any network calls. | ** Network and state-modification characteristics of CLI commands — which TWO are TRUE? | ** Easy |
| 4 | B | ** `terraform taint` was the original mechanism for marking a resource "tainted" so that Terraform would destroy and recreate it on the next apply. It is **deprecated** as of Terraform 0.15.2 / 1.x and may be removed in a future version. The replacement (no pun intended) is `terraform apply -replace="<resource_address>"`, which is cleaner for several reasons: (1) it generates a full plan preview showing the destroy-and-recreate before proceeding, (2) it is a single atomic command rather than two separate steps, (3) it avoids accidentally leaving a resource in a tainted state if you decide not to apply, and (4) the intent is explicit in the apply command itself. Option A is false — `taint` is deprecated. Option C is false — `apply -replace` still generates a plan and prompts for confirmation (unless `-auto-approve` is also passed). Option D is false — neither command has a "maintenance window" concept; both take effect on the next apply. | ** `terraform taint` deprecation — which statement is TRUE? | ** Medium |
| 5 | D | ** Option D is FALSE. `terraform init -upgrade` upgrades **provider plugins** (and module sources) — it does NOT upgrade the Terraform CLI binary itself. The CLI binary is a separate executable installed through system package managers, `tfenv`, `asdf`, or direct download from hashicorp.com; it cannot update itself via `init`. To upgrade the CLI, you use the appropriate installation mechanism for your platform. Options A, B, and C are all true, accurate descriptions of `-upgrade` behaviour: it bypasses the lock file's pinned version to resolve a newer provider version, rewrites the lock file with the new version and hashes, and is the required mechanism because plain `terraform init` strictly respects the lock file. | ** `terraform init -upgrade` — which statement is FALSE? | ** Medium |
| 6 | B | ** `terraform plan -destroy` is the safe, preview-only destroy workflow. It generates the same execution plan that `terraform destroy` would execute, showing every resource marked for deletion (with the `-` symbol) and the total count, but it applies NOTHING. This makes it valuable for: (1) reviewing the scope of destruction before proceeding — especially in large environments, (2) getting approval from a senior engineer or a code review, and (3) saving the plan to a file with `-out=destroy.tfplan` for a deterministic `terraform apply destroy.tfplan` later. `terraform destroy` itself is equivalent to `terraform apply -destroy` — both generate a destroy plan AND execute it (with confirmation). Option A is false — `-destroy` on `plan` is preview-only. Option C is false — `-target` is optional. Option D is false — there is no automatic Terraform Cloud scheduling triggered by a local plan. | ** `terraform plan -destroy` — which statement is TRUE? | ** Medium |
| 7 | B | ** `terraform apply -replace="<address>"` is the recommended Terraform 1.5+ mechanism for forcing a destroy-and-recreate of a specific resource. It is used when you suspect a resource is in a degraded state (a known-bad EC2 instance, a corrupt database, a misconfigured load balancer) and want Terraform to refresh it cleanly. Critically: the `-replace` flag forces replacement **regardless of whether any configuration attribute has changed** — you are overriding Terraform's normal change-detection logic and declaring "this resource must be recreated." In the plan output, the targeted resource shows the `-/+` replacement symbol. The plan is displayed for review (or auto-approved with `-auto-approve`), and the destroy-then-create happens within the single apply run. Option A is false — `-replace` both destroys AND recreates in one operation. Option C is false — `taint` is deprecated; they are not identical. Option D is false — `-replace` is unconditional; it does not inspect the live resource health before deciding. | ** `terraform apply -replace` — which statement is TRUE? | ** Medium |
| 8 | D | ** Option D is FALSE. `terraform fmt -diff` is a **display-only** flag — it shows the unified diff of what WOULD change but does NOT write any changes to disk. It is specifically the non-destructive preview mode of `terraform fmt`. To actually rewrite files AND see the diff, you would run `terraform fmt` (without `-diff`) and separately track changes via version control. The three commonly used `terraform fmt` flags for non-modifying operation are: `-diff` (show changes without writing), `-check` (exit non-zero if any changes needed without writing), and the combination `-check -diff` (exit non-zero AND show what's wrong). Options A, B, and C are all correct: `-diff` is display-only, `-check` is CI-enforcement mode, and combining both gives the most informative CI failure message. | ** `terraform fmt -diff` — which statement is FALSE? | ** Medium |
| 9 | A, C | ** **(A)** is TRUE. `terraform console` opens an interactive command line where engineers can type any HCL expression — including built-in functions (`cidrsubnet("10.0.0.0/8", 8, 2)`), string functions (`format("Hello, %s!", "world")`), type conversions (`toset(["a","b","a"])`), and arithmetic — and see the result immediately. It is the recommended way to test expressions before committing them to configuration. **(C)** is TRUE. `terraform console` is read-only and offline. It reads the current state file to provide values for resource attribute references but makes no API calls and writes no changes. Running `aws_instance.web.id` in the console reads the `id` from state — it does not call the AWS API. **(B)** is FALSE — `console` never writes to state or makes API calls. **(D)** is FALSE — `console` fully supports Terraform functions, resource references, variable references, and local values; simple arithmetic is a subset of what it can handle. | ** `terraform console` — which TWO statements are TRUE? | ** Medium |
| 10 | B | ** When you change the backend configuration (e.g., switching from local state to an S3 backend, or moving from one S3 bucket to another), a plain `terraform init` will detect the backend change and refuse to proceed until you acknowledge what to do with the existing state. The two flags address this differently: `-migrate-state` tells Terraform "yes, I want to move my existing state to the new backend" — Terraform will copy the state records to the new backend and prompt you to confirm. `-reconfigure` tells Terraform "just reset the backend connection; do NOT try to migrate anything" — useful when you want to point to a different backend but the state is already there (or you don't care about the old state). Option A is false — they are distinct flags with different behaviours. Option C is false — adding a backend block for the first time does NOT require `-reconfigure`; a plain `terraform init` handles the initial backend setup. Option D is false — `-migrate-state` still prompts for confirmation; it does not imply auto-approve. | ** `terraform init -migrate-state` vs `-reconfigure` — which statement is TRUE? | ** Medium |
| 11 | C | ** Option C is FALSE. `terraform output -json` is an entirely **offline** command — it reads output values directly from the local state file (or remote state, if a remote backend is configured, but only to read the state object — no cloud resource API calls). It does NOT make any calls to the cloud provider API. The output values in state were written during the last `terraform apply` and reflect the attribute values at that time. If those values have changed in the cloud since the last apply (drift), `terraform output -json` will show the stale recorded values; to get fresh values you would run `terraform apply -refresh-only` first. Options A, B, and D are all accurate: `-json` outputs all outputs as a JSON object, it is machine-readable and useful for scripting, and it reads from local state without network calls. | ** `terraform output -json` — which statement is FALSE? | ** Medium |
| 12 | B | ** Option B is the ONLY TRUE statement. The two-stage pipeline (`plan -out=file` then `apply file`) is the deterministic CI/CD pattern. When `terraform apply` receives a saved plan file as its argument (e.g., `terraform apply plan.tfplan`), it applies precisely those serialised operations — it does NOT re-evaluate the configuration, re-refresh state, or re-compute a new plan. This guarantees that what was reviewed (and potentially approved by a human or automated gate) is exactly what gets applied. Option A is FALSE — `terraform plan` is read-only with respect to the state file; it never writes proposed changes to state. (State is only updated by `terraform apply`.) Option C is FALSE — `terraform plan` and `terraform apply` are NOT equivalent. `plan` is read-only and makes no infrastructure changes; `apply` creates, updates, or deletes real cloud resources. Option D is FALSE — `-refresh=false` is a performance optimisation, not an accuracy improvement. A standard `terraform plan` WITH refresh is MORE accurate because it incorporates the current live state; `-refresh=false` may produce an INACCURATE plan if resources have drifted from recorded state. | ** Four statements about `terraform plan` — only ONE is TRUE | ** Hard |
| 13 | A, B | ** **(A)** is TRUE. The legacy `terraform import` CLI command (`terraform import aws_instance.web i-0abc123`) requires a matching resource block (e.g., `resource "aws_instance" "web" {}`) to already exist in the configuration. The command uses the resource type from the address to determine which provider/resource-type logic to use for the import; without the block, Terraform cannot determine which provider to call. After the import, the state file records the resource's attributes, but the engineer must still manually populate the resource block with the correct arguments to match the imported state. **(B)** is TRUE. The `import` block (Terraform 1.5+) is declarative HCL: you define `import { to = aws_instance.web; id = "i-0abc123" }` directly in a `.tf` file. Terraform incorporates this into `terraform plan`, showing the import as a proposed operation before applying — bringing imports into the same plan-review-apply workflow as other changes. It is version-controlled alongside configuration. **(C)** is FALSE. The legacy CLI `terraform import` does NOT generate the resource configuration block — the engineer must write it manually. The newer HCL `import` block combined with `terraform plan -generate-config-out=generated.tf` CAN generate a configuration stub, but this flag is separate from the import block itself and the output still requires engineer review. **(D)** is FALSE — `terraform import` only affects the Terraform state file; it does not destroy, move, or alter the actual cloud resource. The resource continues to exist in the cloud exactly as before; Terraform simply begins tracking it. | ** `terraform import` — which TWO statements are TRUE? | ** Hard |
