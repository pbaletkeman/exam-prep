# Terraform Associate Exam Questions

---

### Question 1

**Difficulty:** Easy
**Answer Type:** one
**Topic:** Multi-cloud scope of Terraform vs single-cloud tools — which statement is TRUE?

Which of the following statements about the IaC tooling landscape is TRUE?

A) AWS CloudFormation supports multi-cloud deployments including AWS, Azure, and GCP — its plugin model allows any provider to be registered in the same stack
B) Azure ARM templates (Bicep) and AWS CloudFormation can be used interchangeably to deploy resources to either cloud
C) Terraform is unique among common IaC provisioning tools in natively supporting multi-cloud deployments from a single configuration — a single set of `.tf` files can contain AWS, Azure, and GCP resources managed by their respective provider plugins
D) Bicep supports deployment to AWS via a compatibility layer maintained by Microsoft, making it a viable alternative to Terraform for multi-cloud teams

---

### Question 2

**Difficulty:** Easy
**Answer Type:** one
**Topic:** Which statement about idempotency is FALSE?

Which of the following statements about Terraform's idempotency is FALSE?

A) Applying the same Terraform configuration twice in a row to already-matching infrastructure produces the same outcome — the second apply finds nothing to change and reports "No changes"
B) Idempotency guarantees that Terraform will never destroy existing resources — it only creates new resources or updates attributes; destruction is outside the scope of idempotent behavior
C) An idempotent operation produces the same end state regardless of how many times it is executed, given unchanged inputs
D) If the infrastructure already matches the configuration, `terraform apply` will report "No changes. Your infrastructure matches the configuration." and make no modifications

---

### Question 3

**Difficulty:** Easy
**Answer Type:** many
**Topic:** Which TWO statements about IaC benefits are TRUE?

Which TWO of the following statements about the benefits of Infrastructure as Code are TRUE?

A) When infrastructure is defined in version-controlled configuration files, every change is a code commit — this creates an audit trail that records who changed what and when, enabling change review and rollback
B) IaC eliminates the need for state management entirely — because all infrastructure is defined in code, no state file is required; Terraform operates purely from configuration files on every run
C) IaC enables disaster recovery: an entire environment can be rebuilt from the configuration files after a catastrophic failure — the code contains all the definitions needed to recreate servers, networks, databases, and other resources from scratch
D) Writing infrastructure in any IaC tool automatically encrypts all cloud resources and enforces security best practices — IaC tooling applies encryption by default without any additional configuration

---

### Question 4

**Difficulty:** Medium
**Answer Type:** one
**Topic:** Which statement about "desired state" is TRUE?

Which of the following statements about "desired state" in Terraform is TRUE?

A) "Desired state" refers to the contents of the `terraform.tfstate` file — this is the file Terraform reads to determine what infrastructure should exist on the next apply
B) "Desired state" is expressed in the Terraform configuration files (`.tf` files) — it describes what the engineer intends the infrastructure to look like; during `terraform plan`, Terraform compares desired state to current state and proposes changes to close the gap
C) "Desired state" and "current state" refer to the same data — they represent identical views of infrastructure from the perspective of the configuration and the cloud respectively
D) Desired state can only be expressed in JSON format; HCL (HashiCorp Configuration Language) is a human-readable display format that Terraform converts internally to JSON before reading the desired state

---

### Question 5

**Difficulty:** Medium
**Answer Type:** one
**Topic:** Which statement about the declarative IaC approach is TRUE?

Which of the following statements about the declarative approach to Infrastructure as Code is TRUE?

A) In a declarative IaC approach, the engineer writes a sequence of step-by-step commands that the tool executes in order — the tool does exactly what the script specifies, in the exact sequence written
B) Declarative IaC configurations describe the desired end state of infrastructure — the engineer specifies WHAT should exist, and the tool determines whether to create, update, or destroy resources to reach that state
C) Declarative IaC tools like Terraform always delete all existing resources before recreating them on every apply to ensure a clean, known state — this destroy-and-recreate pattern guarantees the infrastructure matches the configuration exactly
D) Declarative and imperative IaC approaches are functionally identical in practice — both result in the same infrastructure being created and neither approach has an advantage over the other for managing drift

---

### Question 6

**Difficulty:** Medium
**Answer Type:** one
**Topic:** Which statement about infrastructure drift is FALSE?

Which of the following statements about infrastructure drift is FALSE?

A) Drift occurs when cloud resources are modified outside of Terraform — for example, through a manual change in the AWS console — causing the actual state of the infrastructure to diverge from what Terraform recorded in its state file
B) Terraform detects drift during `terraform plan` by querying the cloud provider API to refresh current resource attributes and comparing them to the configuration — if a resource has drifted, the plan proposes changes to restore the desired state
C) Once drift is detected in a managed environment, Terraform automatically reconciles it in the background without any engineer intervention — no plan or apply command needs to be run; the tool continuously monitors and self-heals
D) Running `terraform plan -refresh-only` shows drift between the actual cloud resources and the last recorded state, without proposing configuration-driven changes — it is useful for investigating what has changed in the cloud

---

### Question 7

**Difficulty:** Medium
**Answer Type:** one
**Topic:** Ansible vs Terraform — which claim about their design approaches is TRUE?

An engineer makes four claims about Ansible and Terraform. Which claim is TRUE?

A) Ansible and Terraform are both purely declarative tools — neither supports any imperative constructs or workflows; they operate identically in terms of how they describe desired infrastructure
B) Both Ansible and Terraform maintain a state file that tracks all managed infrastructure resources — without this state file, neither tool can detect drift or compute a plan
C) Ansible is primarily used for configuration management (installing software, managing files, configuring services) and is considered more imperative in style — it executes tasks in sequence from a playbook; Terraform is a declarative provisioning tool — it describes desired infrastructure state and reconciles differences
D) Terraform and Ansible serve identical purposes and are completely interchangeable — choosing one over the other is a matter of team preference with no functional difference

---

### Question 8

**Difficulty:** Medium
**Answer Type:** one
**Topic:** Which statement about the audit trail benefit of IaC is TRUE?

Which of the following statements about the audit trail benefit of Infrastructure as Code is TRUE?

A) The audit trail benefit of IaC only applies if the team uses a dedicated compliance tool like HashiCorp Vault alongside their IaC tool — storing `.tf` files in Git alone does not constitute a formal audit trail
B) When infrastructure is defined in version-controlled configuration files, every infrastructure change is captured as a code commit that records the author, timestamp, the exact change made (diff), and optionally the reason (commit message) — this provides a complete, reviewable, and rollback-able history of all infrastructure changes
C) IaC audit trails are only available in paid tiers of IaC platforms like HCP Terraform — when using community Terraform with local state and a simple Git repository, no audit trail is generated
D) An IaC audit trail in Git records only resource deletions — resource creation and attribute updates are not tracked in version control; a separate change management system is required for complete auditability

---

### Question 9

**Difficulty:** Medium
**Answer Type:** many
**Topic:** Which TWO statements about Infrastructure as Code are FALSE?

Which TWO of the following statements about Infrastructure as Code are FALSE?

A) Terraform's declarative model means it always deletes all existing resources and recreates them from scratch on every `terraform apply` — this ensures the infrastructure exactly matches the configuration by starting from a clean state
B) The repeatability benefit of IaC means that running the same Terraform configuration in two different environments (e.g., staging and production) will produce structurally identical infrastructure — the same code deploys the same resources
C) "ClickOps" — provisioning infrastructure manually through a web console — is fully equivalent to IaC for audit trail purposes because cloud providers record all console actions in services like AWS CloudTrail
D) IaC tools like Terraform are only practical for large-scale deployments managing hundreds of cloud resources — for small projects with only a few resources, IaC provides no meaningful advantage over manual provisioning and adds unnecessary complexity

---

### Question 10

**Difficulty:** Medium
**Answer Type:** one
**Topic:** Which statement about the disaster recovery benefit of IaC is TRUE?

Which of the following statements about Infrastructure as Code and disaster recovery is TRUE?

A) The disaster recovery benefit of IaC requires that the state file be stored in a highly available cloud service — without remote state, IaC provides no meaningful disaster recovery advantage over manual provisioning
B) With IaC, an entire infrastructure environment can be rebuilt from the configuration files after a catastrophic failure — the code contains all the resource definitions needed to recreate servers, networks, databases, and other components from scratch in a new region or account
C) IaC only aids disaster recovery for stateless applications — stateful services such as databases and message queues cannot be described in IaC configuration and must be recreated manually
D) The disaster recovery benefit of IaC is limited to recreating the same infrastructure in the exact same region — cross-region or cross-account recovery requires a different set of IaC tools

---

### Question 11

**Difficulty:** Medium
**Answer Type:** one
**Topic:** Which statement comparing Pulumi to Terraform is FALSE?

Which of the following statements comparing Pulumi to Terraform is FALSE?

A) Both Pulumi and Terraform support multi-cloud infrastructure provisioning using a provider plugin model — each provider exposes the APIs of a specific cloud platform
B) Pulumi allows engineers to write infrastructure code in general-purpose programming languages (Python, TypeScript, Go, C#) — unlike Terraform's HCL which is a domain-specific language purpose-built for infrastructure configuration
C) Pulumi uses an imperative approach to infrastructure while Terraform uses a declarative approach — this is the primary and most important architectural difference between the two tools
D) Both Pulumi and Terraform maintain a state file that records the current tracked state of deployed resources and use it to compute diffs on subsequent operations

---

### Question 12

**Difficulty:** Hard
**Answer Type:** one
**Topic:** Four statements about Terraform's declarative model — which is the ONLY TRUE statement?

Four statements about Terraform's declarative model are presented below. Which is the ONLY TRUE statement?

A) Terraform is classified as an imperative IaC tool because HCL is a procedural language — the order in which resource blocks appear in `.tf` files determines the execution order, and engineers must arrange blocks in the correct creation sequence
B) Terraform's declarative approach guarantees that resource blocks are processed in alphabetical order by resource type and label — this deterministic ordering ensures consistent applies across all environments
C) In Terraform's declarative model, the engineer specifies WHAT the end state of infrastructure should look like; Terraform determines whether to create, update, or destroy resources by comparing the desired state (configuration files) against the current state (state file and cloud provider API responses) — engineers do not write the procedural steps; the dependency graph drives execution order automatically
D) Declarative IaC tools like Terraform require the engineer to write explicit "create if not exists" conditional logic using `if` statements around every resource block — without these guards, the tool will attempt to create duplicate resources on every apply

---

### Question 13

**Difficulty:** Hard
**Answer Type:** many
**Topic:** Which TWO statements about the relationship between IaC configuration files and Terraform state are TRUE?

Which TWO of the following statements about the relationship between Terraform configuration files and the state file are TRUE?

A) Terraform configuration files (`.tf` files) are the source of DESIRED STATE — they express what the engineer intends the infrastructure to look like; this is the target that Terraform works toward on every plan and apply
B) The `terraform.tfstate` file is the source of DESIRED STATE — when Terraform runs `terraform plan`, it reads the state file to determine what resources to create; the `.tf` configuration files are merely documentation
C) The `terraform.tfstate` file records the CURRENT TRACKED STATE of all managed infrastructure — it contains real-world attributes populated by the provider after the last successful apply: resource IDs, IP addresses, ARNs, timestamps, and other computed values that did not exist before the resource was created
D) Editing `terraform.tfstate` directly is the recommended and safe method for expressing new desired infrastructure to Terraform — it is functionally equivalent to adding a resource block to a `.tf` configuration file and is the preferred approach for advanced users

## Answer Key

| Q# | Answer(s) | Explanation | Source | Difficulty |
|----|-----------|-----------:|--------|------------|
| 1 | C | ** Terraform's multi-cloud capability is one of its defining characteristics and a common exam topic. A single Terraform configuration can declare resources across multiple cloud providers simultaneously — each provider (AWS, Azure, GCP, etc.) is a separate plugin declared in the `required_providers` block, and resources from each provider coexist in the same state file. This is in contrast to provider-specific tools: AWS CloudFormation is AWS-only, Azure Bicep/ARM is Azure-only, and Google Cloud Deployment Manager is GCP-only. Pulumi also supports multi-cloud but uses general-purpose programming languages rather than HCL. Options A, B, and D are false — CloudFormation has no multi-cloud capability, ARM/Bicep are Azure-only, and there is no Microsoft-maintained Bicep-to-AWS compatibility layer. | ** Multi-cloud scope of Terraform vs single-cloud tools — which statement is TRUE? | ** Easy |
| 2 | B | ** Option B is FALSE. Idempotency means "applying the same configuration N times produces the same result" — it does NOT mean Terraform never destroys resources. Destruction is absolutely within Terraform's idempotent model. For example, setting `count = 0` in a resource block is a valid, idempotent desired state: Terraform will always converge to zero instances of that resource. If you reduce a `count` from 5 to 3, the two excess instances will be destroyed on every apply until the configuration changes again. The promise of idempotency is about repeatability of outcome, not about preventing any particular type of operation. Options A, C, and D are all true statements about idempotency. | ** Which statement about idempotency is FALSE? | ** Easy |
| 3 | A, C | ** **(A)** The audit trail benefit is a core IaC advantage: infrastructure changes committed to version control (Git) are traceable — every commit has an author, timestamp, and optional commit message explaining why the change was made. This replaces the opaque "someone clicked something in the console last Tuesday" problem of ClickOps. **(C)** Disaster recovery is explicitly listed as an IaC benefit: if an environment is destroyed, it can be fully rebuilt by running the configuration against a fresh account or region. The code IS the blueprint. Option B is false — Terraform absolutely requires state management; the state file is how Terraform tracks the real-world attributes of managed resources and computes diffs between plans. Option D is false — IaC tools provision infrastructure according to what you declare; they do not automatically add encryption or security controls not present in the configuration. | ** Which TWO statements about IaC benefits are TRUE? | ** Easy |
| 4 | B | ** "Desired state" is the infrastructure configuration that the engineer has DECLARED in `.tf` files — it represents the intended, target state of infrastructure. This is distinct from "current state," which is what Terraform believes actually exists in the cloud (recorded in the state file and refreshed by querying cloud APIs during plan). Terraform's core job is to reconcile these two: propose and apply the minimal set of changes that transform current state into desired state. Option A is a critical misconception: `terraform.tfstate` records CURRENT state, not desired state. Editing the state file does not change what Terraform will create — it changes what Terraform thinks currently exists. Option C is false — they represent different things by design. Option D is false — Terraform reads `.tf` HCL files directly; while Terraform internally uses JSON representations for provider communication, the canonical format for desired state is HCL. | ** Which statement about "desired state" is TRUE? | ** Medium |
| 5 | B | ** The declarative model is central to how Terraform works and is a major exam objective. In a declarative approach, the engineer describes the DESIRED END STATE — "I want 3 EC2 instances of type t3.micro with these properties" — and the tool figures out HOW to get there. This is the opposite of the imperative approach (e.g., Ansible playbooks, shell scripts) where the engineer writes the explicit steps. The declarative approach has significant advantages: Terraform will add only what is missing, update only what has changed, and remove only what should no longer exist — it never blindly re-creates everything. Option A describes the IMPERATIVE approach, not declarative. Option C is false — destroy-and-recreate on every apply would be extraordinarily disruptive and is NOT how Terraform works; it only destroys when the desired state explicitly removes a resource. Option D is false — the declarative approach has concrete advantages including idempotency, drift detection, and minimal-change plans. | ** Which statement about the declarative IaC approach is TRUE? | ** Medium |
| 6 | C | ** Option C is FALSE. Terraform is NOT an agent-based, continuously monitoring tool that self-heals in the background. Terraform is a CLI tool — it only acts when explicitly invoked by an engineer running a command. There is no background process watching for drift and automatically applying corrections. When drift occurs, an engineer must DETECT it (by running `terraform plan` or `terraform plan -refresh-only`) and then REMEDIATE it (by running `terraform apply` to restore desired state, or `terraform apply -refresh-only` to update state to accept the drift). HCP Terraform has a "Health Assessments" feature that runs scheduled `refresh-only` checks and sends notifications, but even this does NOT auto-apply — it only alerts. Options A, B, and D are all true statements about drift. | ** Which statement about infrastructure drift is FALSE? | ** Medium |
| 7 | C | ** Option C accurately describes the design philosophy and primary use case of each tool. Ansible operates by executing a list of tasks in order — "copy this file, then install this package, then start this service" — which is an imperative style. While Ansible has some idempotency features, the core model is task execution. Terraform operates declaratively: define the desired end state, and Terraform computes and applies the diff. Option A is false — Ansible is considered imperative (or "procedural"), not purely declarative. Option B is false — Ansible does NOT maintain a state file; it re-runs its tasks against the current state of systems on every run without recording what was previously applied (Ansible relies on module-level idempotency rather than a central state). Option D is false — Ansible excels at configuration management (OS-level, application-level); Terraform excels at infrastructure provisioning; they are complementary tools often used together, not interchangeable. | ** Ansible vs Terraform — which claim about their design approaches is TRUE? | ** Medium |
| 8 | B | ** The audit trail benefit is one of the named advantages of IaC. When infrastructure configuration files are committed to version control (Git), every change produces a commit that captures: the AUTHOR (who changed it), the TIMESTAMP (when), the DIFF (exactly what changed — which argument values, which resources were added or removed), and optionally the RATIONALE (commit message or linked pull request). This audit trail is freely available with community Terraform and a standard Git repository — no paid tier is required. The combination of version-controlled infrastructure code and pull request workflows means every infrastructure change can be reviewed, approved, and traced back to a specific decision. Option A is false — Vault is a secrets management tool, not an audit trail system; Git alone provides the audit trail. Option C is false — Git-based audit trails require no paid tooling. Option D is false — Git diffs capture all types of changes (creates, updates, and deletes) to configuration files. | ** Which statement about the audit trail benefit of IaC is TRUE? | ** Medium |
| 9 | A, D | ** **(A)** is FALSE. Terraform's declarative model is explicitly NOT destroy-and-recreate on every apply. This is a critical misconception. Terraform computes the MINIMAL set of changes needed to bring current state to desired state. If the infrastructure already matches the configuration, no actions are taken. Only resources that are new, changed, or removed from the configuration are affected. Destroying and recreating everything on every apply would be catastrophically disruptive in production environments. **(D)** is FALSE. IaC benefits apply at ANY scale. Even for a project with 3-5 resources, IaC provides: reproducibility (anyone can recreate the environment), audit trail (changes tracked in Git), documentation (config files describe the infrastructure), and safety (plan preview before apply). The learning curve exists, but the "only useful at large scale" claim is false. Option B is TRUE — repeatability is a named IaC benefit. Option C is partially true (CloudTrail does log console actions) but is subtly FALSE as a general equivalence claim — ClickOps audit trails (CloudTrail logs) are harder to tie to intent, lack structured diffs of desired state, and don't provide the review/approval workflow of PRs; however, for this question, A and D are the clearest false statements. | ** Which TWO statements about Infrastructure as Code are FALSE? | ** Medium |
| 10 | B | ** Disaster recovery is explicitly listed as a benefit of IaC. The core insight is: "infrastructure defined as code can be recreated from that code." If a region goes down, an account is compromised, or an environment is accidentally destroyed, the configuration files serve as the complete blueprint for rebuilding. Running `terraform apply` against a fresh environment recreates all declared resources. This is a massive advantage over manually provisioned infrastructure, where the knowledge of how everything was configured may exist only in a human's memory or in hard-to-parse console logs. Option A overstates the requirement — remote state is best practice but not a prerequisite for the disaster recovery benefit; even with a local state file backed up to version control, the configuration files are the recovery tool. Option C is false — databases, queues, and other stateful services ARE describable in Terraform configuration (e.g., `aws_rds_instance`, `aws_sqs_queue`) and can be recreated; recovering the DATA is a separate concern (backups), but the infrastructure is IaC-recoverable. Option D is false — Terraform supports cross-region and cross-account deployments. | ** Which statement about the disaster recovery benefit of IaC is TRUE? | ** Medium |
| 11 | C | ** Option C is FALSE. It has the labels backwards. TERRAFORM uses a declarative approach — you write HCL that describes the desired end state, and Terraform determines what actions to take. PULUMI writes infrastructure in general-purpose programming languages that look imperative (you write code with loops, conditionals, and function calls), but the underlying model is still declarative in the sense that Pulumi also tracks desired state and computes diffs. The KEY difference between the two tools is NOT "declarative vs imperative" — it is the LANGUAGE used to express desired state (HCL/DSL for Terraform vs general-purpose programming languages for Pulumi). Option A is true — both use provider plugins for multi-cloud support. Option B is true — Pulumi's language support is its defining feature compared to Terraform's HCL. Option D is true — both tools maintain state files for diff computation. | ** Which statement comparing Pulumi to Terraform is FALSE? | ** Medium |
| 12 | C | ** Option C is the correct, true statement. It captures the essence of Terraform's declarative model: the engineer declares WHAT, not HOW. The dependency graph (built from explicit `depends_on` and implicit references like `aws_subnet.main.id`) determines the order of operations, not the order of blocks in files. **(A)** is FALSE — Terraform is DECLARATIVE, not imperative. HCL is a DSL for expressing desired state, not a procedural language. Resource block order within `.tf` files is irrelevant to execution order; Terraform's DAG determines sequencing. **(B)** is FALSE — resource processing order is determined by the dependency graph, not alphabetical ordering. **(D)** is FALSE — this is one of the most important misconceptions to reject. Terraform's idempotent, declarative model means there is NO need for "create if not exists" guards. Terraform checks whether the resource already exists (by querying state and the cloud provider) and only creates it if it doesn't exist and the configuration declares it should. The entire point of the declarative model is that the engineer does not write these conditionals — the tool handles convergence automatically. | ** Four statements about Terraform's declarative model — which is the ONLY TRUE statement? | ** Hard |
| 13 | A, C | ** **(A)** is TRUE. The `.tf` configuration files are the single source of desired state — they are the human-authored declaration of what infrastructure should exist. This is what the engineer edits to add, change, or remove resources. **(C)** is TRUE. The `terraform.tfstate` file records current tracked state — specifically, the attributes of resources that Terraform has successfully created and the values that the cloud provider assigned (IDs, IPs, etc.). These are values that couldn't be known until after the resource was created (a VPC ID is assigned by AWS, not pre-determined). This state data is essential for computing diffs: Terraform compares A (desired, from `.tf`) with C (current, from state) to produce the plan. **(B)** is FALSE — a critical misconception. The state file records CURRENT state, not desired state. If you delete a resource block from your `.tf` file, that expresses the desired state of "this resource should not exist" — Terraform reads the `.tf` file for desired state, NOT the state file. **(D)** is FALSE and dangerous. Manually editing `terraform.tfstate` is explicitly NOT recommended for expressing desired infrastructure. It is a low-level operation (used occasionally for state surgery via `terraform state` commands) that bypasses all safeguards. Adding a resource block to a `.tf` file is the correct way to declare desired infrastructure. Direct state file edits can corrupt state and cause Terraform to take unexpected actions. | ** Which TWO statements about the relationship between IaC configuration files and Terraform state are TRUE? | ** Hard |
