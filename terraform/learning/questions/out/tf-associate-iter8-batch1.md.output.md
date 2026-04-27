# Terraform Associate Exam Questions

---

### Question 1

**Difficulty:** Easy
**Answer Type:** one
**Topic:** Correct order of `terraform plan` internal phases

When you run `terraform plan`, Terraform follows a fixed sequence of internal phases before displaying the execution plan. Which of the following correctly orders the phases from FIRST to LAST?

A) Compute diff between desired and current state → Refresh current state from cloud provider → Parse configuration files → Output plan
B) Refresh current state from cloud provider → Parse configuration files → Compute diff → Output plan
C) Parse and validate configuration files → Refresh current state by querying the cloud provider API → Compute the diff between desired and current state → Output the plan
D) Output plan → Compute diff → Parse configuration files → Refresh current state

---

### Question 2

**Difficulty:** Easy
**Answer Type:** one
**Topic:** Which step comes LAST in a first-time IaC adoption workflow

A developer is adopting Terraform for the first time and completes the following steps: writes a Terraform configuration file, runs `terraform init`, reviews the `terraform plan` output, and runs `terraform apply`. Which of these steps comes LAST?

A) Write the Terraform configuration files
B) Run `terraform init` to initialize the working directory and download providers
C) Review the `terraform plan` output to verify intended changes
D) Run `terraform apply` to provision the infrastructure

---

### Question 3

**Difficulty:** Easy
**Answer Type:** many
**Topic:** Which workflow-ordering statements are correct

Which TWO of the following statements about the ordering of core Terraform workflow steps are correct?

A) `terraform init` must be run BEFORE `terraform plan` or `terraform apply` — it downloads the provider plugins and modules that subsequent commands depend on
B) `terraform apply` can be run BEFORE `terraform init` — Terraform automatically detects missing providers and installs them on demand during apply
C) When using a saved plan file (`terraform plan -out=plan.tfplan`), the plan step always PRECEDES the apply step — `terraform apply plan.tfplan` executes the previously saved plan without re-planning
D) `terraform destroy` is always run BEFORE `terraform plan` to clear existing state so the plan can calculate what needs to be created

---

### Question 4

**Difficulty:** Medium
**Answer Type:** one
**Topic:** Sequence of operations Terraform performs when it detects configuration drift

An engineer manually deletes an EC2 instance that Terraform manages. The next time `terraform plan` is run with no configuration changes, which of the following correctly orders the operations Terraform performs to produce its output?

A) Read the state file to find the last-known resource attributes → Skip provider refresh → Compute diff → Show plan proposing to delete the resource
B) Show the plan → Read configuration → Query the cloud API → Compute the diff
C) Read configuration (desired state) → Query the cloud provider API to refresh current state → Compute diff between desired state and refreshed state → Output plan proposing to recreate the deleted instance
D) Compute the diff immediately using the cached state file → Output plan → Optionally refresh state afterward

---

### Question 5

**Difficulty:** Medium
**Answer Type:** one
**Topic:** Ordering IaC tools from most to least restrictive cloud scope

An architect is evaluating IaC tools for a company with workloads on AWS, Azure, and GCP. They need a single tool to manage all three. Which of the following correctly orders the listed tools from MOST RESTRICTIVE (single cloud only) to LEAST RESTRICTIVE (broadest cloud support)?

A) Terraform (most restrictive) → AWS CloudFormation → ARM Templates (least restrictive)
B) AWS CloudFormation and ARM Templates (both single-cloud, tied for most restrictive) → Terraform (multi-cloud, least restrictive)
C) Terraform = ARM Templates (both limited to two clouds each) → CloudFormation (broadest)
D) CloudFormation (most restrictive, AWS-only) → ARM Templates → Terraform (least restrictive, supports only AWS and Azure)

---

### Question 6

**Difficulty:** Medium
**Answer Type:** one
**Topic:** Idempotency — which apply run first produces "No changes"

A Terraform configuration creates exactly one VPC. An engineer runs `terraform apply` three times consecutively, with no configuration changes between runs and no external modifications to the cloud infrastructure. Which option correctly describes the SEQUENCE of outputs across the three runs?

A) Run 1: "No changes. Infrastructure is up-to-date." → Run 2: "1 added, 0 changed, 0 destroyed" → Run 3: "No changes"
B) Run 1: "1 added, 0 changed, 0 destroyed" → Run 2: "No changes. Infrastructure is up-to-date." → Run 3: "No changes. Infrastructure is up-to-date."
C) Run 1: "1 added" → Run 2: "1 added" → Run 3: "1 added" (Terraform recreates the resource on every apply)
D) Run 1: "No changes" → Run 2: "1 added" → Run 3: "No changes" (Terraform skips the first apply if no state file exists)

---

### Question 7

**Difficulty:** Medium
**Answer Type:** one
**Topic:** Correct sequence of steps to detect and remediate configuration drift

A cloud resource has drifted from its Terraform-managed configuration — someone manually changed a resource tag via the AWS console. Which of the following correctly orders the steps to DETECT the drift and RESTORE the desired state?

A) Edit the Terraform state file directly to match the new cloud attribute → Run `terraform apply` to propagate the change → Run `terraform plan` to verify
B) Run `terraform destroy` to remove the drifted resource → Rewrite the configuration → Run `terraform apply` to recreate it with the correct tag
C) Run `terraform plan` to detect the drift and see the attribute difference → Review the plan output showing the tag change → Run `terraform apply` to restore desired state → Confirm with a second `terraform plan` showing no changes
D) Run `terraform apply -auto-approve` immediately → Run `terraform plan` afterward to verify the state matches

---

### Question 8

**Difficulty:** Medium
**Answer Type:** one
**Topic:** Which IaC benefit requires time to accumulate value

A team applies their first Terraform configuration on day one. Which of the following IaC benefits requires the MOST TIME to accumulate value — specifically, it is NOT fully realised until the team has made and committed multiple infrastructure changes over weeks or months?

A) Speed — automated provisioning is faster than manual console work starting from the very first apply
B) Repeatability — the same configuration can be applied immediately to create an identical staging environment on day one
C) Audit trail — a history of who changed what and when only accumulates as version-controlled commits build up over multiple changes over time
D) Disaster recovery — the configuration can be reapplied to recreate infrastructure from scratch on day one if needed

---

### Question 9

**Difficulty:** Medium
**Answer Type:** many
**Topic:** Correct ordering statements about refresh and diff in Terraform's plan cycle

Which TWO of the following correctly describe the ordering relationship between Terraform's state refresh and diff computation during a `terraform plan`?

A) Terraform queries the cloud provider API to refresh current state BEFORE computing the diff — computing a diff against a stale state file could result in a plan that does not reflect real-world infrastructure
B) Terraform computes the diff BEFORE refreshing current state — the diff is computed from the cached state file and the refresh is optional and performed afterward
C) The diff between desired and current state is computed AFTER both inputs are known — Terraform requires both the configuration (desired state) and the refreshed provider state (current state) before it can determine what changes are needed
D) Terraform refreshes state only when it detects a difference in configuration — if the `.tf` files have not changed since the last run, no API calls are made to providers

---

### Question 10

**Difficulty:** Medium
**Answer Type:** one
**Topic:** What comes first in declarative vs imperative models

In a declarative IaC tool like Terraform, an operator specifies the DESIRED END STATE and the tool determines the steps. In an imperative approach like a shell script, the operator specifies each step in order. Which of the following correctly describes what comes FIRST in each model?

A) Declarative: the tool generates a list of steps first, then asks the operator to confirm the end state / Imperative: the end state is defined first, then steps are generated
B) Declarative: the DESIRED END STATE is specified first in the configuration file; the tool determines and executes the steps at runtime / Imperative: each STEP is specified explicitly in order; the end state is the emergent result of running all steps
C) Both models require the operator to specify steps in order — declarative tools simply abstract the steps using a higher-level syntax
D) Declarative and imperative models are identical in ordering; the difference is only in which tools are used

---

### Question 11

**Difficulty:** Medium
**Answer Type:** one
**Topic:** Correct sequence to recover infrastructure using IaC after a catastrophic failure

A cloud region suffers a catastrophic failure and all infrastructure is lost. The team manages their infrastructure with Terraform and has the configuration stored in version control. Which of the following correctly orders the steps to recover the infrastructure in a new region?

A) Manually reprovision the infrastructure in the new region via the console → Export a cloud config summary → Write new Terraform configuration from scratch → Run apply
B) Run `terraform destroy` in the failed region → Update the provider region → Run `terraform init` → Run `terraform plan`
C) Clone the repository containing the Terraform configuration → Update the provider region variable → Run `terraform init` to initialise in the new region → Run `terraform apply` to recreate all infrastructure from code
D) Restore servers from backup → Configure networking manually → Update the Terraform state file to reflect the recovered resources

---

### Question 12

**Difficulty:** Hard
**Answer Type:** one
**Topic:** Complete 5-phase sequence of a full `terraform apply` cycle

Which of the following correctly orders ALL FIVE phases of a complete `terraform apply` operation from FIRST to LAST?

A) (1) Execute resource changes in the cloud → (2) Query providers for current state → (3) Parse configuration files → (4) Compute diff → (5) Write updated state file
B) (1) Parse and validate configuration files (desired state) → (2) Query cloud provider APIs to refresh current state → (3) Compute the diff between desired and current state → (4) Present the plan and wait for user confirmation → (5) Execute changes and write updated state file
C) (1) Write updated state file → (2) Compute diff → (3) Parse configuration → (4) Execute changes → (5) Query providers
D) (1) Query providers → (2) Execute changes → (3) Parse configuration → (4) Compute diff → (5) Write state

---

### Question 13

**Difficulty:** Hard
**Answer Type:** many
**Topic:** Two correct contrasts between ordering in Terraform's declarative model and imperative scripting

Which TWO of the following correctly contrast how operations are ORDERED in Terraform's declarative model versus an imperative shell script?

A) In a shell script, operations are executed in the exact sequence they are written — the script has no awareness of what currently exists and runs the same commands in the same order on every execution; in Terraform, the order of operations is determined by the tool at runtime based on resource dependencies and the diff between desired and current state
B) In Terraform, the operator must explicitly write `aws_vpc` blocks before `aws_subnet` blocks in the configuration file to ensure the VPC is created before the subnet; in a shell script, commands must also be explicitly ordered, but using `aws ec2` CLI calls instead of HCL blocks — the ordering constraint is the same in both models
C) A shell script applies the same sequence of commands regardless of current state — running it twice against a cloud environment that already has the resources will create duplicates; Terraform determines which operations are needed by comparing desired to current state and applies ZERO operations when the state already matches, even though the same configuration was used
D) Both Terraform and shell scripts determine the order of operations dynamically at runtime based on the current state of the infrastructure — the only difference is the language used to express the operations

## Answer Key

| Q# | Answer(s) | Explanation | Source | Difficulty |
|----|-----------|-----------:|--------|------------|
| 1 | C | ** Terraform first parses and validates the `.tf` configuration files (desired state), then queries cloud provider APIs to refresh current state. With both states known, it computes the diff and finally outputs the plan. Options A and B both misorder the parse step relative to the refresh. Option D is entirely reversed. | ** Correct order of `terraform plan` internal phases | ** Easy |
| 2 | D | ** The standard first-time workflow ends with `terraform apply`. You must write configuration first (desired state), then `init` to install providers, then `plan` to preview changes, and finally `apply` to execute them. Apply is always the final step that materialises infrastructure — it cannot precede plan or init. | ** Which step comes LAST in a first-time IaC adoption workflow | ** Easy |
| 3 | A, C | ** `terraform init` is a prerequisite for all other commands — it initialises the working directory, downloads providers, and installs modules (A). When a plan file is used, the sequence is always plan first → apply second; `apply plan.tfplan` executes the saved plan exactly (C). Option B is false — running apply without init will fail with provider errors. Option D is false — destroy removes infrastructure; it is not a prerequisite for plan. | ** Which workflow-ordering statements are correct | ** Easy |
| 4 | C | ** Terraform always reads configuration first (desired state), then queries provider APIs to get the live current state. In this case the refresh reveals the instance is missing. It then diffs desired (1 instance) against current (0 instances) and outputs a plan to recreate the instance. Option A is incorrect because Terraform does query the provider — using a stale state file without refresh would miss the manual deletion. Option D is incorrect because the refresh occurs BEFORE the diff, not after. | ** Sequence of operations Terraform performs when it detects configuration drift | ** Medium |
| 5 | B | ** AWS CloudFormation is AWS-only and Azure ARM/Bicep templates are Azure-only — both are single-cloud tools and equally restrictive in scope. Terraform supports AWS, Azure, GCP, and hundreds of other providers through its plugin model, making it the least restrictive. Option D incorrectly claims Terraform only supports two clouds. Option C incorrectly claims ARM Templates and Terraform are equivalent in scope. | ** Ordering IaC tools from most to least restrictive cloud scope | ** Medium |
| 6 | B | ** This is idempotency in action. The FIRST apply creates the VPC (1 added). Every SUBSEQUENT apply finds the infrastructure already matches desired state and reports "No changes." The VPC is NOT created again on runs 2 and 3. Option A is backwards. Option C describes a non-idempotent tool. Option D is incorrect — without a state file Terraform would create resources on run 1, not skip it. | ** Idempotency — which apply run first produces "No changes" | ** Medium |
| 7 | C | ** The correct sequence is: plan first (detects drift by comparing refreshed state to config), review the plan to confirm the change is expected, apply to restore desired state, then verify with a second plan that reports "No changes." Option A is dangerous — editing the state file directly bypasses Terraform's reconciliation logic. Option B is unnecessarily destructive. Option D applies without review, which is poor practice. | ** Correct sequence of steps to detect and remediate configuration drift | ** Medium |
| 8 | C | ** Speed (A), repeatability (B), and disaster recovery (D) are all available from the very first apply. The audit trail (C) is unique in that it requires TIME — its value grows as a versioned history of commits accumulates across many changes, reviews, and deployments. On day one, there is only one commit; the trail is not yet meaningful. This makes it the benefit that is realised last in the IaC adoption sequence. | ** Which IaC benefit requires time to accumulate value | ** Medium |
| 9 | A, C | ** Both A and C describe the same correct ordering from different angles: refresh always PRECEDES the diff (A), and the diff requires BOTH states to be known before it can be computed (C). Option B reverses the sequence — the diff cannot be computed before the refresh because current state would be unknown. Option D is false — Terraform always queries providers during plan regardless of whether configuration has changed, because infrastructure may have drifted independently of the config. | ** Correct ordering statements about refresh and diff in Terraform's plan cycle | ** Medium |
| 10 | B | ** In the declarative model (Terraform), you write WHAT you want first — the end state is declared in configuration before any operation occurs. The tool determines HOW at runtime. In the imperative model (shell script), you write the HOW first — each explicit command in sequence. The end state is never directly declared; it emerges from the commands you wrote. Options C and D incorrectly claim the models are equivalent in ordering. Option A swaps the definitions. | ** What comes first in declarative vs imperative models | ** Medium |
| 11 | C | ** IaC's disaster recovery benefit is demonstrated here: the configuration already exists in version control, so recovery is: clone/pull the repo → update the region → init (installs providers) → apply (recreates everything). The infrastructure is rebuilt from code without manual steps. Option A abandons the IaC approach. Option B starts with `destroy` which is irrelevant when the region is already gone. Option D relies on manual processes and state file editing, which negates the IaC advantage. | ** Correct sequence to recover infrastructure using IaC after a catastrophic failure | ** Medium |
| 12 | B | ** The complete `terraform apply` sequence is: (1) parse/validate config to establish desired state → (2) refresh current state by querying provider APIs → (3) diff desired vs current to determine required changes → (4) present the plan and wait for approval (unless `-auto-approve`) → (5) execute the changes and persist updated state. Option A places execution before parsing, which is impossible. Option C writes state before any operations. Option D places execution before parsing and diffing. | ** Complete 5-phase sequence of a full `terraform apply` cycle | ** Hard |
| 13 | A, C | ** Option A correctly contrasts execution ordering: shell scripts are static-order and state-blind; Terraform's order is dynamic, driven by the dependency graph and the diff against current state. Option C correctly contrasts idempotency ordering: a shell script blindly re-executes all commands (creating duplicates), while Terraform checks current state first and may execute ZERO operations if nothing has changed. Option B is false — in Terraform the tool resolves dependency ordering from the reference graph (`aws_subnet.example.vpc_id = aws_vpc.main.id`), not from the physical order of blocks in the file. Option D is false — shell scripts do not query current state at all. | ** Two correct contrasts between ordering in Terraform's declarative model and imperative scripting | ** Hard |
