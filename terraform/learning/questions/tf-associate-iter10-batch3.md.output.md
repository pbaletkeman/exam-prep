# Terraform Associate Exam Questions

---

### Question 1 — Second Provider Added to Existing Config

**Difficulty**: Easy
**Answer Type**: one
**Topic**: `terraform init` must be re-run when a new provider is added to `required_providers`

**Scenario**:
A team has been managing AWS infrastructure with Terraform for six months. Their configuration already declares the `hashicorp/aws` provider and their working directory has been initialized. A developer adds a `hashicorp/random` provider block to generate unique resource name suffixes. Without running any additional commands, they immediately run `terraform plan`. The terminal prints an error: `Provider "registry.terraform.io/hashicorp/random" was not found. Did you forget to run "terraform init"?`

**Question**:
What is the correct next action before `terraform plan` can succeed?

- A) Add the random provider to `.terraform/` manually by downloading the binary from the Terraform Registry website
- B) Run `terraform validate` first — this downloads missing providers as a side effect before performing syntax checks
- C) Run `terraform init` to download the newly declared `hashicorp/random` provider plugin and update the lock file
- D) Run `terraform apply -refresh-only` — this re-resolves provider dependencies without requiring a full init

---

### Question 2 — Production Deploy Pipeline Uses a Two-Stage Approach

**Difficulty**: Medium
**Answer Type**: one
**Topic**: `terraform plan -out` + `terraform apply <planfile>` guarantees deterministic apply of the reviewed plan

**Scenario**:
A financial services company has a strict change management process. All infrastructure changes to production must be reviewed and approved by a second engineer before being applied. The team's CI/CD pipeline is designed in two stages: Stage 1 runs during business hours and requires human approval; Stage 2 applies the change only after the Stage 1 approval ticket is signed. The infrastructure team wants to ensure that the exact changes reviewed and approved in Stage 1 are what get applied in Stage 2 — with no possibility of drift between review and apply.

**Question**:
Which approach correctly implements this two-stage guarantee?

- A) Run `terraform plan` in Stage 1; in Stage 2, run `terraform apply` — Terraform always re-runs the same plan from Stage 1 when no plan file is specified
- B) Run `terraform plan -out=prod.tfplan` in Stage 1 and store the plan file as a CI artifact; in Stage 2, run `terraform apply prod.tfplan` to apply exactly the reviewed plan
- C) Run `terraform validate` in Stage 1 to capture the intended changes; in Stage 2, run `terraform apply -auto-approve` to apply without prompting
- D) Pass a checksum of the configuration files from Stage 1 to Stage 2; Terraform verifies the checksum before applying to ensure no changes occurred

---

### Question 3 — Formatting Check Added to Pull Request Validation

**Difficulty**: Easy
**Answer Type**: one
**Topic**: `terraform fmt -check` exits with code 1 when files need reformatting — used in CI without writing files

**Scenario**:
A platform team wants to enforce consistent HCL formatting across all Terraform configurations in their monorepo. They add a new job to their pull request pipeline that validates formatting on every PR before allowing a merge. The job must fail the pipeline if any `.tf` file in any subdirectory is not in canonical Terraform format. Crucially, the CI environment is read-only — the job must not modify any source files. The team needs a single command to accomplish this.

**Question**:
Which command correctly implements the formatting check without modifying any files?

- A) `terraform fmt -recursive` — formats all files in subdirectories and exits with code 0, which fails the pipeline when changes are written
- B) `terraform fmt -check -recursive` — checks all `.tf` files recursively and exits with a non-zero code if any file needs reformatting, without writing any changes
- C) `terraform validate -recursive` — validates HCL syntax recursively across all subdirectories, including formatting style
- D) `terraform fmt -diff -recursive` — shows what would change and automatically fails the pipeline when diff output is non-empty

---

### Question 4 — Unhealthy EC2 Instance Needs a Clean Replacement

**Difficulty**: Medium
**Answer Type**: one
**Topic**: `terraform apply -replace` forces destroy+recreate of a specific resource without changing configuration

**Scenario**:
An operations engineer is troubleshooting a production EC2 instance that is exhibiting intermittent failures. The instance was correctly provisioned by Terraform and its configuration has not changed. The team suspects the instance has become corrupted at the OS level after an unexpected shutdown. The engineer wants to destroy the specific instance and provision a fresh one in its place, without touching any other resources in the Terraform-managed environment and without removing the resource block from the configuration.

**Question**:
Which command is the correct current approach for this situation?

- A) Remove the `aws_instance.app` resource block from the configuration temporarily, run `terraform apply`, then re-add the block and run `terraform apply` again
- B) Run `terraform destroy -target=aws_instance.app` followed by `terraform apply -target=aws_instance.app`
- C) Run `terraform apply -replace="aws_instance.app"` to force Terraform to destroy the existing instance and create a new one in a single apply operation
- D) Run `terraform taint aws_instance.app` — this is the current recommended command for forcing resource replacement

---

### Question 5 — Platform Team Visualizes a Dependency Graph for a New Hire

**Difficulty**: Medium
**Answer Type**: one
**Topic**: `terraform graph` outputs DOT format; Graphviz (`dot`) is required to render it as an image

**Scenario**:
A new infrastructure engineer joins a team managing a complex Terraform configuration with 30+ resources across VPCs, EC2 instances, RDS databases, security groups, and IAM roles. To help the new hire understand the dependency relationships between resources, the team lead wants to produce a visual diagram showing which resources depend on which. The team lead's workstation has Graphviz installed. They run a Terraform command and pipe its output to produce an SVG file.

**Question**:
Which command produces the rendered SVG dependency diagram?

- A) `terraform show -json | jq '.resources' > graph.svg`
- B) `terraform graph | dot -Tsvg > graph.svg`
- C) `terraform plan -out=graph.svg` — saves the execution plan as an SVG diagram when the file extension is `.svg`
- D) `terraform state list | dot -Tsvg > graph.svg`

---

### Question 6 — Script Assigns a Terraform Output to a Shell Variable

**Difficulty**: Easy
**Answer Type**: one
**Topic**: `terraform output -raw` produces unquoted string values suitable for shell variable assignment

**Scenario**:
A deployment script written in Bash needs to retrieve the public IP address of an EC2 instance that was provisioned by Terraform, then SSH into the instance to run a configuration command. The script runs `terraform output instance_ip` and captures the result with `IP=$(terraform output instance_ip)`. When the script attempts `ssh ubuntu@$IP`, the connection fails because the SSH command is receiving the value with surrounding double quotes: `"54.12.34.56"` instead of `54.12.34.56`.

**Question**:
What change to the `terraform output` command eliminates the surrounding quotes?

- A) Use `terraform output -json instance_ip | jq -r '.value'` to strip quotes from the JSON wrapper
- B) Use `terraform output -raw instance_ip` — the `-raw` flag outputs the value as a plain string without surrounding quotes, suitable for direct shell variable assignment
- C) Use `terraform show instance_ip` — the `show` command omits quotation marks from scalar output values
- D) Use `terraform output instance_ip | tr -d '"'` — pipe through `tr` to remove quotes as a post-processing step

---

### Question 7 — Large Environment Plan Takes 20 Minutes Due to API Throttling

**Difficulty**: Medium
**Answer Type**: many
**Topic**: `terraform plan -refresh=false` skips live API queries; trades freshness for speed in trusted environments

**Scenario**:
A team manages a Terraform workspace with over 600 cloud resources across AWS. Their standard `terraform plan` takes 20–25 minutes to complete because Terraform makes hundreds of individual AWS API calls to refresh the current state of every resource, and they are frequently hitting AWS API rate limits. The team's lead architect wants to speed up the planning cycle for routine code review without migrating to a different tool or architecture. The team's CI environment does not make any out-of-band changes — all infrastructure modifications go through Terraform.

**Question**:
Which TWO statements accurately describe the trade-off of using `terraform plan -refresh=false` in this scenario?

- A) `terraform plan -refresh=false` skips the live API refresh phase entirely, relying on the cached state in the state file — this significantly reduces API calls and plan duration
- B) `terraform plan -refresh=false` queries the API for resources that have changed since the last apply, but skips resources that are unchanged — it provides a partial refresh with improved performance
- C) Since the team's policy ensures no out-of-band infrastructure changes occur, the cached state in the state file is reliable, making `-refresh=false` a reasonable trade-off in this specific context
- D) `terraform plan -refresh=false` is inherently unsafe regardless of the environment because it disables all state consistency checks and may corrupt the state file

---

### Question 8 — Validate Passes, Plan Fails on First Deployment

**Difficulty**: Medium
**Answer Type**: one
**Topic**: `terraform validate` checks static config only; `terraform plan` catches live resource issues like invalid AMIs

**Scenario**:
A developer has written a new Terraform configuration to provision a set of EC2 instances using a specific AMI ID. They run `terraform validate` in their local environment and it exits successfully with `Success! The configuration is valid.` Confident the configuration is correct, they commit it and the team's CI pipeline runs `terraform plan` against the development AWS account. The plan fails with: `Error: ami-0deadbeef123 does not exist in region us-east-1`.

**Question**:
Why did `terraform validate` pass while `terraform plan` failed?

- A) `terraform validate` incorrectly ignored the `ami` argument because it is optional; `terraform plan` enforces required arguments with a stricter parser
- B) `terraform validate` performs only static analysis of the HCL syntax and references — it does not verify that referenced cloud resources (such as an AMI) actually exist. `terraform plan` contacts the AWS API during the refresh phase, which is when it discovers the AMI is invalid in that region
- C) The failure is caused by a missing provider version constraint; `terraform validate` does not enforce version constraints but `terraform plan` does
- D) `terraform validate` succeeded because the AMI ID was syntactically a valid string; `terraform plan` checks AMI IDs against a local cached list maintained in `.terraform/`

---

### Question 9 — Workspace Verification Before a Destructive Command

**Difficulty**: Medium
**Answer Type**: one
**Topic**: `terraform workspace show` displays the currently active workspace — critical safety check before destructive operations

**Scenario**:
A senior engineer is preparing to run `terraform destroy` to tear down a temporary load testing environment that was provisioned in the `loadtest` workspace. Their workflow involves switching between the `loadtest`, `staging`, and `production` workspaces multiple times per day. Before executing the destroy command, they want to verify with absolute certainty that the currently active workspace is `loadtest` and not `staging` or `production`. They need a single, concise command that outputs only the name of the currently active workspace.

**Question**:
Which command provides this information?

- A) `terraform workspace list` — lists all workspaces and marks the active one with an asterisk (`*`)
- B) `terraform workspace show` — outputs only the name of the currently active workspace as a plain string
- C) `terraform env` — the legacy command alias that outputs the active workspace name
- D) `terraform state list | head -1` — the first line of state list output always contains the workspace name

---

### Question 10 — Developer Tests a Conditional Expression Before Embedding It

**Difficulty**: Medium
**Answer Type**: one
**Topic**: `terraform console` lets developers interactively evaluate HCL expressions and functions before embedding them in configuration

**Scenario**:
A developer is writing a Terraform configuration that needs to conditionally set a resource tag based on whether a boolean variable `var.is_production` is `true`. They plan to use the ternary expression `var.is_production ? "prod" : "dev"` as the tag value. Before embedding this expression in the configuration, they want to test both branches interactively to confirm the syntax is correct and the output is exactly what they expect — without modifying any configuration files or running a full plan.

**Question**:
Which Terraform command provides this interactive testing capability?

- A) `terraform validate` — accepts expression syntax as an argument and evaluates it against the current variable values
- B) `terraform plan -var "is_production=true"` — this mode shows only the computed expression value without applying any changes
- C) `terraform console` — opens an interactive REPL where the developer can evaluate HCL expressions, test functions, and inspect variable values without modifying configuration or state
- D) `terraform output` — displays the result of arbitrary HCL expressions entered as arguments when run in debug mode

---

### Question 11 — CI Pipeline Must Pass Only Reviewed Changes to Production

**Difficulty**: Hard
**Answer Type**: one
**Topic**: Applying a saved plan file skips re-planning and interactive confirmation; changes between plan and apply cannot slip through

**Scenario**:
A DevSecOps team has implemented a two-stage production deployment pipeline. In Stage 1, `terraform plan -out=approved.tfplan` runs and the plan output is attached to a change request ticket for human review. A change advisory board reviews the plan, approves the ticket, and triggers Stage 2. In Stage 2, a pipeline job runs and must apply the exact, reviewed plan — no more, no fewer changes. A team member proposes replacing Stage 2's `terraform apply approved.tfplan` with `terraform apply -auto-approve` to simplify the pipeline, arguing both approaches skip the interactive prompt.

**Question**:
Why is the team member's proposed simplification incorrect and potentially dangerous?

- A) `-auto-approve` is not permitted in CI environments and will always cause an exit code 1 failure when run outside of an interactive terminal
- B) `terraform apply -auto-approve` runs a fresh plan at apply time, meaning any infrastructure changes that occurred between Stage 1 and Stage 2 (such as manual console changes or concurrent pipeline runs) would be included in the apply — producing different changes from what the change advisory board reviewed and approved
- C) `terraform apply approved.tfplan` and `terraform apply -auto-approve` are functionally identical when the configuration has not changed between the two stages, so the simplification is safe
- D) `-auto-approve` requires the `-input=false` flag to be specified alongside it in CI environments; omitting `-input=false` will cause Stage 2 to pause waiting for user input

---

### Question 12 — Emergency Fix Targets One Resource in a Shared Workspace

**Difficulty**: Hard
**Answer Type**: many
**Topic**: `terraform apply -target` applies only to the specified resource; known risks include partial state and dependency gaps

**Scenario**:
During a production incident, a load balancer security group rule allowing port 443 was accidentally removed via the AWS console by another team, causing a service outage. The Terraform configuration still contains the correct rule. The on-call engineer wants to immediately restore only the security group rule using Terraform without potentially modifying the 80 other resources in the same workspace, since many of those resources are actively serving traffic. The engineer runs `terraform apply -target=aws_security_group_rule.allow_https`. The rule is restored and the outage is resolved. The team lead later reviews the incident and raises a concern about the long-term use of `-target`.

**Question**:
Which TWO concerns correctly describe the risks of using `-target` regularly (not just in this emergency)?

- A) Regular use of `-target` can lead to a configuration drift where the Terraform state does not accurately reflect the full desired state — resources that depend on the targeted resource may be in a different state than the configuration specifies, creating inconsistencies that accumulate over time
- B) `-target` is not a supported flag on `terraform apply` — it is only valid with `terraform plan`; using it with `apply` will silently apply all resources instead
- C) After a `-target` apply, the remainder of the configuration has not been fully evaluated — running a full `terraform plan` afterwards may reveal planned changes to resources that were not included in the targeted apply, because their dependencies changed
- D) `-target` causes Terraform to permanently lock the targeted resource's state entry, preventing future full applies from modifying it unless the lock is manually removed with `terraform state rm`

---

### Question 13 — Engineer Mistakes `terraform plan -destroy` for `terraform destroy`

**Difficulty**: Hard
**Answer Type**: one
**Topic**: `terraform plan -destroy` is a read-only preview; `terraform destroy` actually destroys resources

**Scenario**:
A junior engineer is tasked with reviewing what would be deleted if the staging environment were torn down. Their team lead tells them: "Use `terraform plan -destroy` to see what would be removed." The junior engineer misremembers the instruction and instead runs `terraform destroy` in the staging workspace. Within seconds, Terraform begins destroying resources. The engineer panics and presses Ctrl+C to interrupt the process. Five resources are destroyed before the interrupt takes effect. The team lead later reviews the incident to explain the difference between the two commands.

**Question**:
Which statement most accurately describes the distinction between `terraform plan -destroy` and `terraform destroy`?

- A) `terraform plan -destroy` and `terraform destroy` are aliases for the same operation; both always prompt for interactive confirmation before making any changes, so the engineer should have seen a prompt and cancelled before any resources were destroyed
- B) `terraform plan -destroy` generates a read-only preview showing what `terraform destroy` would remove, without making any API calls or changes to infrastructure. `terraform destroy` actually executes the destruction — it prompts for confirmation by default, but once "yes" is entered (or `-auto-approve` is used), it immediately begins deleting resources
- C) `terraform plan -destroy` also destroys resources, but it destroys them in reverse dependency order to avoid errors; `terraform destroy` uses alphabetical order and is therefore more likely to produce errors
- D) `terraform plan -destroy` is only valid when used with a `-out` flag to save the destroy plan; running it without `-out` is equivalent to `terraform destroy`

## Answer Key

| Q# | Answer(s) | Explanation | Source | Difficulty |
|----|-----------|-----------:|--------|------------|
| 1 | C | N/A | `terraform init` must be re-run when a new provider is added to `required_providers` | Easy |
| 2 | B | N/A | `terraform plan -out` + `terraform apply <planfile>` guarantees deterministic apply of the reviewed plan | Medium |
| 3 | B | N/A | `terraform fmt -check` exits with code 1 when files need reformatting — used in CI without writing files | Easy |
| 4 | C | N/A | `terraform apply -replace` forces destroy+recreate of a specific resource without changing configuration | Medium |
| 5 | B | N/A | `terraform graph` outputs DOT format; Graphviz (`dot`) is required to render it as an image | Medium |
| 6 | B | N/A | `terraform output -raw` produces unquoted string values suitable for shell variable assignment | Easy |
| 7 | A, C | N/A | `terraform plan -refresh=false` skips live API queries; trades freshness for speed in trusted environments | Medium |
| 8 | B | N/A | `terraform validate` checks static config only; `terraform plan` catches live resource issues like invalid AMIs | Medium |
| 9 | B | N/A | `terraform workspace show` displays the currently active workspace — critical safety check before destructive operations | Medium |
| 10 | C | N/A | `terraform console` lets developers interactively evaluate HCL expressions and functions before embedding them in configuration | Medium |
| 11 | B | N/A | Applying a saved plan file skips re-planning and interactive confirmation; changes between plan and apply cannot slip through | Hard |
| 12 | A, C | N/A | `terraform apply -target` applies only to the specified resource; known risks include partial state and dependency gaps | Hard |
| 13 | B | N/A | `terraform plan -destroy` is a read-only preview; `terraform destroy` actually destroys resources | Hard |
