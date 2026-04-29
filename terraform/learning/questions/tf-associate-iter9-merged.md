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

---

### Question 1

**Difficulty:** Easy
**Answer Type:** one
**Topic:** Five provider responsibilities — which statement is TRUE?

Which of the following statements about what a Terraform provider plugin is responsible for is TRUE?

A) A provider is responsible only for authenticating to the cloud API — the Terraform Core binary is responsible for all CRUD operations (create, read, update, delete) and maps resource attributes directly to the state file without provider involvement
B) A provider's responsibilities include: authenticating to the cloud/service API, implementing CRUD operations for resources, exposing data sources, validating resource configuration against a schema, and mapping resource attributes to and from Terraform state
C) A provider plugin must be included in every `.tf` configuration file using an `import` statement — without an explicit `import`, Terraform Core cannot locate the provider binary
D) A provider is responsible for maintaining the `terraform.tfstate` file and is the only component with write access to it — Terraform Core reads state but cannot write to it directly

---

### Question 2

**Difficulty:** Easy
**Answer Type:** one
**Topic:** `sensitive = true` — which statement is FALSE?

Which of the following statements about the `sensitive = true` argument on an output block is FALSE?

A) Setting `sensitive = true` on an output causes Terraform to display the value as `(sensitive value)` in `terraform apply` and `terraform output` terminal output, preventing accidental exposure in logs
B) Setting `sensitive = true` on an output encrypts the corresponding attribute value before writing it to `terraform.tfstate`, ensuring the value cannot be read from the state file by anyone with access to it
C) `sensitive = true` only affects terminal display — the actual attribute value is still stored in plaintext inside `terraform.tfstate` regardless of the sensitive setting
D) Because sensitive values are stored in plaintext in state, teams handling secrets should use an encrypted remote backend (such as S3 with server-side encryption) for production state files

---

### Question 3

**Difficulty:** Easy
**Answer Type:** many
**Topic:** Which TWO statements about `.terraform.lock.hcl` are TRUE?

Which TWO of the following statements about the `.terraform.lock.hcl` dependency lock file are TRUE?

A) `.terraform.lock.hcl` records the exact provider version (e.g., `5.31.0`) and cryptographic hashes of the installed provider binaries, ensuring that subsequent `terraform init` runs install the identical version and verify binary integrity
B) `.terraform.lock.hcl` should be added to `.gitignore` alongside the `.terraform/` directory — both are auto-generated by `terraform init` and should never be committed to version control
C) To intentionally advance a provider to a newer version within the declared constraint, an engineer runs `terraform init -upgrade` — this updates the lock file to record the new version
D) `.terraform.lock.hcl` contains the full text of all provider source code, making it the authoritative documentation for which provider APIs are available in the configuration

---

### Question 4

**Difficulty:** Medium
**Answer Type:** one
**Topic:** Local vs remote state — which statement about locking is TRUE?

Which of the following statements about the difference between local and remote Terraform state is TRUE?

A) Local state stored in `terraform.tfstate` supports concurrent apply operations by multiple team members because Terraform automatically detects when another apply is in progress and waits before proceeding
B) Both local and remote state backends implement state locking by default — locking is a built-in feature of the `terraform.tfstate` format and does not depend on the storage backend
C) Local state provides NO state locking — if two engineers run `terraform apply` simultaneously against a local state file, both operations may proceed concurrently and corrupt the state file; remote backends such as S3 with DynamoDB, HCP Terraform, or Azure Blob provide state locking to prevent concurrent applies
D) Remote state locking is only available in paid HCP Terraform plans — free-tier and open-source Terraform users must use local state and manually coordinate applies to prevent conflicts

---

### Question 5

**Difficulty:** Medium
**Answer Type:** one
**Topic:** Provider source address format — which statement is FALSE?

Which of the following statements about Terraform provider source addresses is FALSE?

A) The fully qualified provider source address format is `<hostname>/<namespace>/<type>` — when the hostname is omitted (short form like `"hashicorp/aws"`), Terraform defaults to `registry.terraform.io`
B) The local name used in a `required_providers` block (e.g., `aws` in `aws = { source = "hashicorp/aws" }`) must always exactly match the provider type in the source address — for example, the AWS provider can only be referenced as `aws` anywhere in the configuration
C) A Terraform configuration can declare multiple providers from different namespaces — for example, the official `hashicorp/aws` and a community provider `myorg/customprovider` can both be declared in the same `required_providers` block
D) Provider source addresses pointing to `registry.terraform.io` are resolved from the public Terraform Provider Registry — providers on this registry include Official, Partner, and Community tiers

---

### Question 6

**Difficulty:** Medium
**Answer Type:** one
**Topic:** `terraform state rm` — which statement is TRUE?

Which of the following statements about `terraform state rm` is TRUE?

A) `terraform state rm` permanently deletes the specified resource from both Terraform state AND from the actual cloud infrastructure — it is equivalent to running `terraform destroy` for a single resource
B) `terraform state rm` removes the specified resource from Terraform's state file while leaving the actual cloud resource running and intact — after removal, Terraform no longer manages that resource and will not include it in future plans
C) `terraform state rm` is the recommended way to rename a resource when you change its label in the `.tf` file — it removes the old name from state and re-applies the new name automatically
D) `terraform state rm` is only available in HCP Terraform — the open-source Terraform CLI does not include state manipulation commands to prevent accidental state corruption

---

### Question 7

**Difficulty:** Medium
**Answer Type:** one
**Topic:** Provider tier trust levels — which statement about the Partner tier is FALSE?

Which of the following statements about the **Partner** provider tier in the Terraform Registry is FALSE?

A) Partner providers are maintained by technology companies that have a partnership relationship with HashiCorp and have had their provider reviewed and approved by HashiCorp
B) The Partner tier sits between the Official tier (maintained by HashiCorp) and the Community tier (maintained by individuals with no HashiCorp review) in terms of trust and vetting
C) Partner providers carry the same trust level as Official providers because both tiers require HashiCorp to review and maintain the provider source code directly
D) Examples of Partner providers include providers maintained by cloud vendors, database companies, or SaaS platforms that have partnered with HashiCorp to provide official integrations

---

### Question 8

**Difficulty:** Medium
**Answer Type:** one
**Topic:** `terraform plan -refresh=false` — which statement is TRUE?

Which of the following statements about `terraform plan -refresh=false` is TRUE?

A) `terraform plan -refresh=false` is the recommended default for all production plans because skipping the refresh step improves plan accuracy — without refresh, Terraform uses the most recent configuration rather than potentially stale cloud API responses
B) `terraform plan -refresh=false` skips the step where Terraform queries live cloud provider APIs to update the known state — the plan is computed using the cached attribute values in the state file rather than fresh API responses; this is faster but may produce inaccurate results if the actual infrastructure has drifted from the recorded state
C) `-refresh=false` and `-refresh-only` are equivalent flags that both skip infrastructure API calls and produce identical plan output
D) `terraform plan -refresh=false` is required when using remote state backends — remote backends cache state and do not support real-time cloud API refreshes during plan

---

### Question 9

**Difficulty:** Medium
**Answer Type:** many
**Topic:** Three sources of truth in `terraform plan` — which TWO are TRUE?

Which TWO of the following statements about how Terraform computes a plan are TRUE?

A) During `terraform plan`, Terraform consults three sources of information: the desired state (`.tf` configuration files), the known state (`terraform.tfstate` — last recorded resource attributes), and the actual state (live cloud resources queried via API calls) — the plan proposes changes needed to bring actual state into alignment with desired state
B) The `terraform.tfstate` file is the sole source of truth during planning — Terraform never makes live API calls because doing so would be too slow and would risk rate-limiting on large environments
C) If `terraform.tfstate` does not yet exist (first apply of a new configuration), Terraform treats the known state as empty — this means Terraform will propose creating all resources declared in the configuration because no current state exists to compare against
D) Terraform uses the actual live cloud state as its desired state — the `.tf` configuration files are advisory only, and Terraform will not make changes that conflict with what the cloud reports as the current resource attributes

---

### Question 10

**Difficulty:** Medium
**Answer Type:** one
**Topic:** `terraform state mv` purpose — which statement is TRUE?

Which of the following statements about `terraform state mv` is TRUE?

A) `terraform state mv` destroys the source resource in the cloud and recreates it under the new address — it is functionally equivalent to removing and re-adding a resource block in the configuration and running `terraform apply`
B) `terraform state mv` renames a resource in the Terraform state file without destroying or recreating the underlying cloud resource — it is the correct way to update state when you rename a resource label in your configuration, preventing Terraform from planning a destroy-and-recreate cycle
C) `terraform state mv` only works with resources that use the `count` meta-argument — it cannot be used to rename resources that use `for_each` or resources without either meta-argument
D) `terraform state mv` is only required when migrating between remote backends — for local renames within the same configuration it is unnecessary because Terraform automatically tracks resource label changes between applies

---

### Question 11

**Difficulty:** Medium
**Answer Type:** one
**Topic:** Provider alias usage — which statement about the default provider is TRUE?

Which of the following statements about Terraform provider aliases is TRUE?

A) When two `provider "aws"` blocks exist (one without an alias and one with `alias = "secondary"`), Terraform distributes resources between the two configurations automatically — resources are allocated in round-robin order to load-balance API calls
B) A provider block without an `alias` argument is the default configuration for that provider type — any resource block of that provider type that does NOT specify a `provider` meta-argument will use this default configuration
C) Once a provider alias is declared, all resource blocks for that provider type MUST explicitly specify which configuration to use via the `provider` meta-argument — the concept of a "default" provider no longer applies when any alias exists
D) Provider aliases are only supported for the official HashiCorp providers (AWS, Azure, GCP) — community and partner providers cannot define aliases

---

### Question 12

**Difficulty:** Hard
**Answer Type:** one
**Topic:** Four statements about Terraform state — only ONE is TRUE

Four statements about Terraform state are presented below. Which is the ONLY TRUE statement?

A) The `terraform.tfstate` file contains only the resource labels and types declared in the `.tf` configuration — computed attributes such as resource IDs, IP addresses, and ARNs assigned by the cloud provider are not stored in state because they are fetched fresh from the cloud API on every plan
B) Because `sensitive = true` on a variable or output causes Terraform to encrypt the value before writing it to state, engineers can safely store API keys and database passwords in Terraform variables without needing an encrypted backend
C) Manually editing `terraform.tfstate` with a text editor is the officially recommended approach for renaming resources, fixing state corruption, and performing state migrations — it is faster and more precise than using `terraform state` commands
D) The `terraform.tfstate` file stores computed resource attributes (IDs, IP addresses, ARNs, and other values that the cloud provider assigns after resource creation) alongside the configuration-declared attributes — these stored values enable Terraform to compute accurate diffs without querying every resource on every plan, and they are stored in plaintext JSON regardless of any `sensitive` annotations

---

### Question 13

**Difficulty:** Hard
**Answer Type:** many
**Topic:** Which TWO statements about Terraform version constraints are TRUE?

Which TWO of the following statements about Terraform provider version constraints are TRUE?

A) The constraint `version = ">= 5.0, < 6.0"` is functionally equivalent to `version = "~> 5.0"` — both allow any version from `5.0` up to (but not including) `6.0`, and either form is acceptable in `required_providers`
B) The constraint `version = "~> 5.0.0"` allows the AWS provider to be upgraded to version `5.1.0` — the `~>` operator permits minor version increments within the major version declared
C) When multiple version constraints are combined (e.g., `version = ">= 5.0, < 5.20"`), Terraform selects the NEWEST version that satisfies ALL constraints simultaneously — not the minimum version, and not the first constraint alone
D) The `=` exact version constraint (e.g., `version = "= 5.31.0"`) is considered a poor practice because it prevents the provider from ever receiving security patches — if a security fix is released as `5.31.1`, the constraint will block its installation; `~>` with a patch-level lock (e.g., `~> 5.31.0`) is the preferred approach for maximum stability with patch-level updates

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

---

### Question 1

**Difficulty:** Easy
**Answer Type:** one
**Topic:** Variable and local references — which statement is TRUE?

Which of the following statements about how `var.*` and `local.*` references affect Terraform's dependency graph is TRUE?

A) Referencing `var.region` inside two different resource blocks creates an implicit dependency edge between those resources — Terraform will serialise their creation in the order they appear in the configuration file
B) `local.*` references create the strongest type of dependency edge in Terraform's graph — resources that reference the same local value are always created last, after all other resources
C) `var.*` and `local.*` references do NOT create dependency edges between resources — variables and locals are simply resolved values, not resources; only direct references to another resource's attribute (e.g., `aws_vpc.main.id`) create implicit dependency edges in the DAG
D) `var.*` references create dependency edges only when the variable type is `string` — list and map variable references are ignored by the dependency graph builder

---

### Question 2

**Difficulty:** Easy
**Answer Type:** one
**Topic:** `ignore_changes = all` — which statement is FALSE?

Which of the following statements about the `ignore_changes = all` lifecycle argument is FALSE?

A) `ignore_changes = all` instructs Terraform to ignore ALL attribute drift on the resource — on every subsequent plan, Terraform will detect zero differences for that resource regardless of what has changed in the actual cloud infrastructure
B) `ignore_changes = all` is the broadest form of `ignore_changes` — instead of listing specific attributes, it suppresses drift detection for every attribute of the resource simultaneously
C) `ignore_changes = all` is restricted to compute resources (such as `aws_instance`) — it cannot be applied to networking, storage, or database resources because those resource types do not support the `all` keyword in their lifecycle blocks
D) `ignore_changes = all` can be useful for resources that are heavily managed by external tooling or processes outside Terraform, where drift detection would always produce noisy false-positive changes

---

### Question 3

**Difficulty:** Easy
**Answer Type:** many
**Topic:** Which TWO statements about `for_each` are TRUE?

Which TWO of the following statements about the `for_each` meta-argument are TRUE?

A) `for_each` accepts a `set(string)` or a `map` as its value — it does NOT accept a plain `list(string)` directly; to use a list, it must first be converted to a set using `toset()` (e.g., `for_each = toset(var.names)`)
B) `for_each` accepts any collection type including `list(string)`, `set(string)`, and `map` — no type conversion is needed regardless of whether the input is a list or a set
C) Inside a resource block that uses `for_each`, `each.key` holds the current iteration's key (the map key or the set element value) and `each.value` holds the corresponding value from the map; for a set, `each.key` and `each.value` are identical since each element IS its own key
D) `for_each` and `count` can be declared together on the same resource block — `for_each` controls the naming while `count` controls the total number of instances

---

### Question 4

**Difficulty:** Medium
**Answer Type:** one
**Topic:** `replace_triggered_by` lifecycle argument — which statement is TRUE?

Which of the following statements about the `replace_triggered_by` lifecycle argument is TRUE?

A) `replace_triggered_by` is a shorthand alias for `depends_on` — both arguments create the same type of dependency edge and are interchangeable
B) `replace_triggered_by` forces a resource to be replaced (destroyed and recreated) whenever any resource or attribute listed in it changes — even if the resource's own configuration attributes have not changed; this is useful for resources like Auto Scaling Groups that should cycle when their launch template changes
C) `replace_triggered_by` only works with resources in the same module — you cannot reference a resource from a parent or child module in the `replace_triggered_by` list
D) `replace_triggered_by` is equivalent to `ignore_changes` with the opposite effect — where `ignore_changes` suppresses replacements, `replace_triggered_by` forces them for listed attributes during in-place updates

---

### Question 5

**Difficulty:** Medium
**Answer Type:** one
**Topic:** `removed` block — which statement is FALSE?

Which of the following statements about the `removed` block (Terraform 1.7+) is FALSE?

A) The `removed` block is used to stop Terraform from managing a resource while optionally keeping the actual cloud resource intact — it provides a declarative way to "forget" a resource without destroying it
B) Setting `lifecycle { destroy = false }` inside a `removed` block tells Terraform to remove the resource's state entry without issuing any destroy API call — the cloud resource continues to exist and run normally after the apply
C) The `removed` block is the only way to stop Terraform from managing a resource in Terraform 1.7+ — running `terraform state rm` to achieve the same result is deprecated and will be removed in a future version
D) The `removed` block is a version-controlled, declarative alternative to `terraform state rm` — it achieves the same state-removal outcome but is expressed in HCL and goes through the normal plan/apply workflow

---

### Question 6

**Difficulty:** Medium
**Answer Type:** one
**Topic:** `depends_on` and parallelism — which statement is TRUE?

Which of the following statements about `depends_on` and its effect on performance is TRUE?

A) `depends_on` has no performance impact — Terraform's scheduler ignores explicit dependency declarations and always maximises parallelism regardless of any `depends_on` declarations
B) `depends_on` increases parallelism by giving Terraform advance knowledge of the dependency structure — without it, Terraform must wait to discover dependencies at runtime, which is slower
C) `depends_on` adds an explicit dependency edge to the Terraform DAG, serialising the creation of the dependent resource after ALL resources listed in `depends_on` complete — this reduces the potential parallelism of the apply, which is why `depends_on` should be used sparingly and only when implicit dependencies cannot capture the relationship
D) `depends_on` is only evaluated during `terraform destroy` — it has no effect on the ordering of resource creation during `terraform apply`

---

### Question 7

**Difficulty:** Medium
**Answer Type:** one
**Topic:** `terraform apply -target` — which statement is FALSE?

Which of the following statements about `terraform apply -target` is FALSE?

A) `terraform apply -target=aws_instance.web` limits the apply to the specified resource and its dependency chain — only the targeted resource and any resources it depends on are included in the apply operation
B) Using `-target` is recommended as a standard day-to-day workflow practice because it allows precise, surgical updates to individual resources and prevents unintended changes to other infrastructure in the same configuration
C) Frequent use of `-target` can cause state drift — by applying changes to only a subset of resources, other resources in the configuration may become out of sync with the state file, leading to unexpected plan output on subsequent full applies
D) Terraform emits a warning when `-target` is used, reminding the engineer that the resulting plan and state may be incomplete

---

### Question 8

**Difficulty:** Medium
**Answer Type:** one
**Topic:** Resource address format — which statement is TRUE?

Which of the following statements about Terraform resource address formats is TRUE?

A) A resource's address within its own module is always prefixed with `module.root.` — for example, an EC2 instance declared in the root module as `resource "aws_instance" "web"` has the address `module.root.aws_instance.web`
B) The address `aws_instance.web` refers to a resource only when used within the same module where it is declared — when referenced from the root module, the address automatically includes the full provider namespace, becoming `hashicorp/aws.aws_instance.web`
C) A resource declared in the root module as `resource "aws_instance" "web"` has the local address `aws_instance.web` within that module; when the same resource is referenced from an external context (such as a `terraform state` command or an error message), its fully qualified address is `aws_instance.web` (root module resources have no module prefix); a resource inside a child module called `compute` would be addressed as `module.compute.aws_instance.web`
D) Resource addresses always include the provider name as a prefix — for example, `aws.aws_instance.web` or `azurerm.azurerm_resource_group.rg` — to disambiguate resources when multiple providers are in use

---

### Question 9

**Difficulty:** Medium
**Answer Type:** one
**Topic:** Data source with computed inputs — which statement is TRUE?

Which of the following statements about a data source whose filter arguments depend on computed values from unbuilt resources is TRUE?

A) Terraform prohibits data source filter arguments from referencing computed attributes of resources that do not yet exist — the configuration will fail validation with an error at plan time if any data source references an attribute that is "known after apply"
B) When a data source's filter arguments depend on an attribute of a resource that does not yet exist (a computed/"known after apply" value), Terraform defers reading the data source until the apply phase — the plan output shows the data source result and any resources depending on it as "(known after apply)", and the actual API call to read the data source happens during apply after the dependency is created
C) When a data source references a "(known after apply)" attribute, Terraform uses the last known value from the state file as a substitute — this prevents any "unknown" values from propagating to downstream resources
D) Data sources are always read during the plan phase, regardless of whether their inputs are known — Terraform uses placeholder values for any unknown inputs and corrects them automatically during apply without any visible indication in the plan output

---

### Question 10

**Difficulty:** Medium
**Answer Type:** many
**Topic:** Which TWO statements about the `moved` block are TRUE?

Which TWO of the following statements about the `moved` block are TRUE?

A) After a successful `terraform apply` that processes a `moved` block, the `moved` block has served its purpose and can be safely deleted from the configuration — the resource is now tracked under its new address and no further `moved` block is needed
B) If a `moved` block is accidentally removed from a configuration BEFORE the apply that would process it, Terraform will silently skip the rename and the resource will retain its old address in state permanently with no further action possible
C) A `moved` block can relocate a resource FROM the root module INTO a child module — for example, `from = aws_instance.web` and `to = module.compute.aws_instance.server` is valid and moves the state entry into the child module's address namespace without destroying the cloud resource
D) `moved` blocks are processed by Terraform only when `terraform init -upgrade` is run — they are not processed during a normal `terraform plan` or `terraform apply` cycle

---

### Question 11

**Difficulty:** Medium
**Answer Type:** one
**Topic:** `prevent_destroy` scope — which statement is FALSE?

Which of the following statements about `prevent_destroy = true` is FALSE?

A) `prevent_destroy = true` causes `terraform plan` to return an error if the proposed plan includes destroying the protected resource — it does not wait until `terraform apply` to raise the error
B) `prevent_destroy = true` can be bypassed at runtime by passing the `-force-destroy` flag to `terraform destroy` — this allows emergency teardowns without modifying the configuration
C) The only way to destroy a resource protected by `prevent_destroy = true` is to first remove or disable the `prevent_destroy` setting in the configuration, then run `terraform apply` or `terraform destroy` — there is no runtime flag to override it, by design
D) `prevent_destroy = true` is intentionally impossible to bypass with a flag because its purpose is to force a deliberate, reviewable, version-controlled configuration change before destruction can occur

---

### Question 12

**Difficulty:** Hard
**Answer Type:** one
**Topic:** Four statements about lifecycle meta-arguments — only ONE is TRUE

Four statements about Terraform lifecycle meta-arguments are presented below. Which is the ONLY TRUE statement?

A) `create_before_destroy = true` and `prevent_destroy = true` can never be declared together in the same `lifecycle` block — Terraform raises a configuration error because the two arguments conflict: `create_before_destroy` assumes a replacement will happen, while `prevent_destroy` blocks any replacement
B) `ignore_changes` with a list of attributes (e.g., `ignore_changes = [tags]`) tells Terraform to never create or update the resource for those attributes — Terraform will also skip creating the resource if the initial `terraform apply` only has values for the ignored attributes
C) `replace_triggered_by` accepts a list of resource references or specific resource attributes — when a referenced resource OR attribute changes on apply, Terraform plans the resource as a forced replacement (`-/+`), even if none of that resource's own declared attributes have changed; `replace_triggered_by` only triggers on changes, not on initial resource creation
D) The four lifecycle arguments (`create_before_destroy`, `prevent_destroy`, `ignore_changes`, `replace_triggered_by`) are mutually exclusive — only one can be declared per `lifecycle` block; declaring two or more causes a validation error

---

### Question 13

**Difficulty:** Hard
**Answer Type:** many
**Topic:** Which TWO statements about Terraform's dependency graph (DAG) are TRUE?

Which TWO of the following statements about Terraform's dependency graph are TRUE?

A) Terraform builds a Directed Acyclic Graph (DAG) where each node represents a resource and each directed edge represents a dependency — the "acyclic" property guarantees no circular dependencies exist; if a circular dependency is detected (e.g., resource A references B and B references A), Terraform returns a configuration error rather than attempting to execute an infinite loop
B) Resources with no dependencies between them are always executed strictly sequentially — Terraform processes one resource at a time in alphabetical order by resource type to ensure reproducible, deterministic apply outputs
C) The destroy order in Terraform is the topological REVERSE of the create order — in a chain where A ← B ← C (C depends on B, B depends on A), creation order is A → B → C and destruction order is C → B → A; this guarantees that no resource is destroyed while another resource that depends on it still exists
D) Adding `depends_on` between two resources that already have an implicit attribute-reference dependency is harmless but redundant — the graph edge already exists, so the explicit `depends_on` adds no new constraint and has no effect on execution order or parallelism

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

---

### Question 1

**Difficulty:** Easy
**Answer Type:** one
**Topic:** Multiple `validation` blocks per variable — which statement is TRUE?

Which of the following statements about the number of `validation` blocks allowed on a single variable declaration is TRUE?

A) A variable declaration can contain AT MOST one `validation` block — to check multiple conditions, the engineer must combine them into a single boolean expression using `&&` within one block
B) Multiple `validation` blocks can be declared on the same variable — each block's `condition` is evaluated independently; if any block's condition returns `false`, that block's `error_message` is displayed and the run halts; all conditions must pass for the variable to be accepted
C) Multiple `validation` blocks on a variable are valid HCL syntax but Terraform only evaluates the LAST `validation` block and silently ignores all earlier ones
D) Multiple `validation` blocks are only permitted on variables of type `string` — `number` and `bool` variables are restricted to a single `validation` block

---

### Question 2

**Difficulty:** Easy
**Answer Type:** one
**Topic:** `self` keyword in `precondition` — which statement is FALSE?

Which of the following statements about using the `self` keyword inside a `precondition` block is FALSE?

A) Inside a `postcondition` block, `self` references the resource's attributes as they exist AFTER the resource has been created or updated — this is the primary use of `self` in lifecycle conditions
B) `self` is a valid and commonly used keyword inside `precondition` blocks — it references the resource's CURRENT state before the planned change is applied, allowing the engineer to validate the resource's existing attributes
C) Inside a `precondition` block, `self` is NOT available — a `precondition` runs BEFORE the resource is modified, so there is no "new" state for `self` to reference; `precondition` conditions must reference other data sources, variables, or resources rather than `self`
D) A `precondition` that needs to assert something about the resource's planned instance type should reference `var.instance_type` or `data.something.attribute` — not `self`, which is undefined in `precondition` scope

---

### Question 3

**Difficulty:** Easy
**Answer Type:** many
**Topic:** `sensitive = true` on output blocks — which TWO statements are TRUE?

Which TWO of the following statements about setting `sensitive = true` on an output block are TRUE?

A) When `sensitive = true` is set on an output, the value is encrypted at rest in `terraform.tfstate` — this is the primary reason to mark outputs as sensitive, because it protects the data if the state file is ever read by an unauthorized party
B) When a child module declares an output with `sensitive = true`, the parent module that references that output via `module.name.output_name` automatically treats the value as sensitive — the sensitivity propagates through module composition without requiring the parent to redeclare it
C) Marking an output `sensitive = true` suppresses the value in `terraform apply` terminal output and in the default `terraform output` listing — the actual value is replaced with `(sensitive value)` in those contexts
D) Sensitive outputs can never be retrieved in plaintext — once `sensitive = true` is set, the value is permanently opaque and cannot be accessed by any means, including scripts or downstream configurations

---

### Question 4

**Difficulty:** Medium
**Answer Type:** one
**Topic:** `check` block scoped `data` source — which statement is TRUE?

Which of the following statements about the optional `data` source block inside a `check` block is TRUE?

A) The `data` source declared inside a `check` block is identical in behaviour to a top-level `data` source — it is added to the resource dependency graph and other resources can reference its output using the standard `data.<type>.<name>.<attribute>` syntax
B) The `data` source inside a `check` block is **scoped to the `check` block** — it exists only within the context of that check's assertions and is NOT accessible from outside the `check` block via the standard `data.*` reference syntax; because it is outside the main dependency graph, a failure to read it does not fail the apply
C) The `data` source inside a `check` block is only evaluated during `terraform apply` — it is skipped during `terraform plan` to avoid making network calls before infrastructure is deployed
D) Only a single type of `data` source is allowed inside a `check` block — the `http` data source from the `hashicorp/http` provider; other provider data sources cannot be used as scoped check data sources

---

### Question 5

**Difficulty:** Medium
**Answer Type:** one
**Topic:** Outputting a sensitive variable without marking the output sensitive — which statement is TRUE?

Which of the following statements about referencing a `sensitive = true` variable in an output block WITHOUT setting `sensitive = true` on the output is TRUE?

A) Terraform automatically propagates the sensitivity from the variable to the output — if the output's `value` references a sensitive variable, Terraform silently marks the output sensitive without requiring any explicit declaration on the output block
B) Terraform displays a warning about the potential exposure but proceeds with the apply — the sensitive value appears in plaintext in the output
C) Terraform raises an **error** at plan time if an output's `value` references a sensitive variable and the output block does not declare `sensitive = true` — the engineer must explicitly acknowledge the sensitive nature of the data by adding `sensitive = true` to the output block
D) The output is simply omitted from `terraform output` listings when it references a sensitive variable without being marked sensitive — the value is silently suppressed with no error

---

### Question 6

**Difficulty:** Medium
**Answer Type:** one
**Topic:** `precondition` and `postcondition` on data sources — which statement is TRUE?

Which of the following statements about using `precondition` and `postcondition` blocks with data sources is TRUE?

A) `precondition` and `postcondition` blocks can only be declared inside `resource` blocks — they are not supported on `data` source blocks; attempts to use them with data sources produce a syntax error
B) Only `postcondition` is supported on data source `lifecycle` blocks — `precondition` is not valid on data sources because data sources do not have a pre-change state to evaluate
C) `precondition` and `postcondition` blocks are both valid inside a data source's `lifecycle` block — a data source `postcondition` is commonly used to assert that the fetched data meets expected requirements (e.g., verifying that a looked-up AMI has the correct architecture) before other resources consume it
D) `precondition` and `postcondition` blocks on data sources run at `terraform init` — unlike resource lifecycle conditions which run during plan and apply, data source conditions are validated when providers are initialized

---

### Question 7

**Difficulty:** Medium
**Answer Type:** one
**Topic:** `check` block exit code on assertion failure — which statement is FALSE?

Which of the following statements about the exit code of `terraform apply` when a `check` block assertion fails is FALSE?

A) When a `check` block assertion fails, `terraform apply` exits with code `0` (success) — the failed assertion is reported as a warning in the output but does not change the exit code
B) Because `check` block failures exit with `0`, CI/CD pipelines that rely solely on the `terraform apply` exit code to detect failures will NOT catch a failed `check` assertion — pipelines must parse the Terraform output or use a tool that inspects the check results to detect check assertion failures
C) A failing `check` block assertion causes `terraform apply` to exit with a **non-zero exit code** — this is what distinguishes `check` from `precondition`: both block apply completion, but `check` failures are labelled as "warnings" while `precondition` failures are labelled as "errors"
D) The non-blocking, exit-code-0 behaviour of `check` blocks makes them suitable for health monitoring dashboards and observability tooling — where surfacing a health status without blocking deployments is the desired outcome

---

### Question 8

**Difficulty:** Medium
**Answer Type:** many
**Topic:** `check` block — which TWO statements are TRUE?

Which TWO of the following statements about `check` blocks are TRUE?

A) A `check` block MUST include a scoped `data` source block — a `check` block that contains only `assert` blocks without a `data` source is invalid HCL syntax
B) `check` blocks run on BOTH `terraform plan` and `terraform apply` — they are evaluated after all resource operations complete in each run; this means health assertions are checked on every plan, giving continuous visibility even in runs that make no changes
C) A single `check` block can contain AT MOST one `assert` block — to check multiple conditions in the same `check` context, the engineer must declare multiple separate `check` blocks
D) The `data` source declared inside a `check` block can be referenced by resource blocks elsewhere in the configuration using the standard `data.<type>.<name>.<attribute>` syntax — this allows resource configurations to consume values fetched by the health check

---

### Question 9

**Difficulty:** Medium
**Answer Type:** one
**Topic:** `error_message` in condition blocks — which statement is TRUE?

Which of the following statements about the `error_message` argument in `validation`, `precondition`, and `postcondition` blocks is TRUE?

A) The `error_message` must be a static string literal with no interpolation — referencing `var.<name>` or any expression inside the `error_message` is a syntax error; this is the same restriction that applies to the `condition` expression
B) The `error_message` argument is optional in all three condition block types — if omitted, Terraform uses a default message such as "Condition failed"
C) The `error_message` is a string expression and CAN include interpolation — for example, a `validation` block's `error_message` can reference `var.<variable_name>` to include the invalid value in the message, such as `"${var.environment} is not an allowed environment"`; this helps engineers produce informative error messages that show the offending value
D) The `error_message` in a `postcondition` can reference `self.<attribute>` to include the resource's post-change attribute values, but the `error_message` in a `precondition` and `validation` cannot use any interpolation at all

---

### Question 10

**Difficulty:** Medium
**Answer Type:** one
**Topic:** `precondition` failing mid-apply — which statement is FALSE?

Which of the following statements about what happens when a `precondition` fails during `terraform apply` is FALSE?

A) When a `precondition` fails, Terraform halts the apply immediately — the resource that declares the failing `precondition` is NOT modified; its state is unchanged
B) When a `precondition` fails mid-apply, resources that were already successfully applied BEFORE the failing resource are NOT automatically rolled back — Terraform does not perform automatic rollback of completed resource changes
C) A failing `precondition` exits `terraform apply` with a non-zero exit code — this is what makes `precondition` suitable as a hard deployment gate in CI/CD pipelines, unlike `check` blocks which exit with code `0`
D) When a `precondition` fails on Resource B, and Resource A was already successfully applied in the same run, Terraform automatically destroys Resource A and reverts the infrastructure to the state it was in before the apply began — this transactional rollback is the key safety feature of `precondition`

---

### Question 11

**Difficulty:** Hard
**Answer Type:** one
**Topic:** Four statements about the three condition mechanisms — only ONE is TRUE

Four statements about Terraform's three condition mechanisms are presented below. Which is the ONLY TRUE statement?

A) A `postcondition` that fails causes Terraform to automatically taint the resource — the resource is marked in state as needing replacement, so the next `terraform apply` will destroy and recreate it; this auto-taint is what prevents a broken resource from persisting in the infrastructure
B) Variable `validation` blocks run after `terraform plan` is generated and displayed to the operator but before the operator types `yes` to approve — this gives the operator a chance to review both the plan and any validation warnings before committing
C) The `check` block's `assert` condition can reference ANY value available in the Terraform configuration, including resource attributes, data source outputs, local values, and variables — it is not restricted like `validation` conditions (which can only reference `var.<name>`) because `check` blocks run after all resource operations complete when those values are known
D) When a `precondition` fails on a resource that is being DESTROYED (not created or updated), Terraform ignores the `precondition` and proceeds with the destroy — `precondition` checks only apply to create and update operations, not destroy

---

### Question 12

**Difficulty:** Hard
**Answer Type:** many
**Topic:** Sensitive data handling — which TWO statements are TRUE?

Which TWO of the following statements about Terraform sensitive data handling are TRUE?

A) When a resource attribute is automatically marked sensitive by its provider (for example, `aws_db_instance.main.password`), any `output` or `local` that references that attribute must also be explicitly marked `sensitive = true` — otherwise Terraform raises a plan-time error about exposing a sensitive value
B) The `nonsensitive()` function removes the sensitive marking from a value, allowing it to be used in contexts that would otherwise require `sensitive = true`; using `nonsensitive()` is appropriate when an engineer has reviewed the data and determined it is safe to expose — for example, when wrapping a value in `base64encode()` or `sha256()` has made the original secret unrecoverable from the output
C) Sensitive values marked with `sensitive = true` on a variable are automatically excluded from `terraform.tfstate` — the state file omits them entirely so that even unrestricted access to the state file does not expose the original value
D) When Terraform performs a `terraform plan`, sensitive variable values are ALWAYS omitted from the plan output entirely — even in the diff showing what will change, the old and new values are always shown as `(sensitive value)` regardless of whether the value is actually changing

---

### Question 13

**Difficulty:** Hard
**Answer Type:** one
**Topic:** Four statements about `precondition` + `postcondition` placement and scope — only ONE is TRUE

Four statements about where and how `precondition` and `postcondition` blocks can be declared are presented below. Which is the ONLY TRUE statement?

A) A resource block can contain at most ONE `precondition` and ONE `postcondition` — declaring multiple of the same type (e.g., two `precondition` blocks in the same `lifecycle`) causes a Terraform configuration error
B) `precondition` and `postcondition` blocks are only valid inside `resource` blocks — they cannot be used inside `data` source blocks, `module` blocks, or `output` blocks
C) A resource's `lifecycle` block can contain multiple `precondition` blocks and multiple `postcondition` blocks — there is no limit on the number of each; every `precondition` is evaluated before the resource is changed and every `postcondition` is evaluated after; if any condition fails, Terraform halts with that condition's `error_message`
D) `postcondition` blocks support a special `rollback = true` argument that instructs Terraform to automatically destroy the just-created resource if the condition fails — without this argument, a failing `postcondition` leaves the resource in place and only exits non-zero

---

### Question 1

**Difficulty:** Easy
**Answer Type:** one
**Topic:** `terraform get` vs `terraform init` for module installation — which statement is FALSE?

Which of the following statements about the `terraform get` command is FALSE?

A) `terraform get` downloads and installs module sources into `.terraform/modules/` — it performs the same module-caching work that `terraform init` performs for modules
B) `terraform get` is a standalone command that downloads module sources but does NOT install or update providers — to install providers, a full `terraform init` (or `terraform init -upgrade`) is still required
C) `terraform get` also installs required providers defined in `terraform { required_providers {} }` blocks — because modules often declare their own required providers, `terraform get` automatically resolves and installs those providers at the same time to keep the local cache consistent
D) Running `terraform init` performs a superset of what `terraform get` does — `terraform init` installs providers, initialises the backend, AND downloads modules; `terraform get` handles only the module download step

---

### Question 2

**Difficulty:** Easy
**Answer Type:** one
**Topic:** Standard module file naming convention — which statement is TRUE?

Which of the following statements about the standard file structure for a publishable Terraform module is TRUE?

A) Terraform enforces a mandatory file structure — a module MUST contain exactly three files named `main.tf`, `variables.tf`, and `outputs.tf`; any other filenames cause `terraform init` to ignore the module directory
B) The standard module file structure (`main.tf`, `variables.tf`, `outputs.tf`, `versions.tf`, `README.md`) is a **convention** recommended for readability and registry publishing — Terraform itself does not enforce specific filenames; any `.tf` file in the directory is processed equally regardless of name; multiple `.tf` files are merged into a single logical configuration
C) `variables.tf` and `outputs.tf` are special filenames that Terraform processes before `main.tf` — this processing order is guaranteed and means input variables are always resolved before resource blocks are evaluated
D) The `versions.tf` file, which contains the `terraform { required_providers {} }` block, must exist in the module root directory — placing `required_providers` in `main.tf` is not supported and causes a provider resolution error

---

### Question 3

**Difficulty:** Easy
**Answer Type:** many
**Topic:** `count` and `for_each` meta-arguments on module blocks — which TWO statements are TRUE?

Which TWO of the following statements about using `count` and `for_each` on a `module` block are TRUE?

A) `count` and `for_each` are NOT valid meta-arguments on `module` blocks — they are supported only on `resource` and `data` blocks; applying them to a `module` block causes a syntax error
B) When `for_each = { prod = "10.0.0.0/16", dev = "10.1.0.0/16" }` is set on a module block, Terraform creates two module instances; inside the module, `each.key` and `each.value` are available just as they are in a `for_each` resource; the instances are addressed as `module.<name>["prod"]` and `module.<name>["dev"]`
C) When `count = 3` is set on a module block, Terraform creates three separate module instances; the instances are addressed as `module.<name>[0]`, `module.<name>[1]`, and `module.<name>[2]`, and `count.index` is available inside the module for distinguishing instances
D) `for_each` on a module block requires that the module itself contain no resources — only data sources are permitted inside a module instantiated with `for_each`

---

### Question 4

**Difficulty:** Medium
**Answer Type:** one
**Topic:** `depends_on` on a module block — which statement is TRUE?

Which of the following statements about using `depends_on` in a `module` block is TRUE?

A) `depends_on` is not supported on `module` blocks — it can only be used on `resource` blocks; adding `depends_on` to a module block causes a `terraform init` error
B) `depends_on` on a `module` block should be used routinely for all module relationships — Terraform recommends explicitly declaring all inter-module dependencies using `depends_on` to ensure correct ordering, even when output-to-input relationships already establish the order
C) `depends_on` on a `module` block instructs Terraform to apply the entire target module **after** the listed resources or modules have been applied — it is specifically intended for cases where a module depends on something that Terraform CANNOT detect automatically (a "hidden dependency"), such as a resource whose output is not directly referenced by any module input but whose side effects must complete first
D) `depends_on` on a `module` block has no effect when both dependencies are in the same Terraform root module — it only controls ordering between root modules in a workspace with multiple configurations

---

### Question 5

**Difficulty:** Medium
**Answer Type:** one
**Topic:** `.terraform.lock.hcl` and module version tracking — which statement is FALSE?

Which of the following statements about the `.terraform.lock.hcl` file and module versions is FALSE?

A) The `.terraform.lock.hcl` file tracks **provider** version selections — it records the exact provider version resolved by `terraform init` and the provider's checksums so that subsequent `terraform init` runs on any machine reproduce the same provider version
B) The `.terraform.lock.hcl` file records the resolved versions of **Terraform Registry modules** in addition to providers — this means that after `terraform init`, both the exact provider versions AND the exact module versions are pinned in the lock file, and all team members will use the identical module and provider versions when they run `terraform init`
C) Module version pinning for Terraform Registry modules is NOT managed by `.terraform.lock.hcl` — module versions are resolved each time `terraform init` runs based on the `version` constraint in the `module` block; the resolved version is cached in `.terraform/modules/modules.json` but is NOT recorded in the lock file; to ensure reproducible module versions, the `version` constraint in the `module` block should be as specific as possible (e.g., `"= 5.1.0"`)
D) The `.terraform.lock.hcl` file should be committed to version control — committing it ensures consistent provider versions across all team members and CI/CD environments; `terraform init -upgrade` is used to intentionally update the lock file to newer provider versions

---

### Question 6

**Difficulty:** Medium
**Answer Type:** one
**Topic:** Addressing module resources in Terraform commands — which statement is TRUE?

Which of the following statements about how module resources are addressed in Terraform CLI commands is TRUE?

A) Resources inside a module are addressed using the format `module.<module_name>.<resource_type>.<resource_name>` — for example, `module.networking.aws_vpc.main`; this address is used in `terraform state list`, `terraform state show`, `terraform taint`, `terraform destroy -target`, and similar commands
B) Resources inside a module cannot be targeted individually — `terraform apply -target` can only reference top-level root module resources; entire modules must be applied as a unit
C) Resources inside a module are addressed the same way as root-module resources — `aws_vpc.main` regardless of which module declares them; the module name is omitted from addresses in all CLI commands
D) The module resource address format uses a colon separator: `module:<module_name>:<resource_type>:<resource_name>` — the colon syntax is required to distinguish module addresses from root-level resource addresses in command output

---

### Question 7

**Difficulty:** Medium
**Answer Type:** one
**Topic:** Module `providers` meta-argument — which statement is TRUE?

Which of the following statements about the `providers` meta-argument in a `module` block is TRUE?

A) The `providers` argument in a `module` block is used to pass **input variables** to the module — it is an alternative to listing inputs directly in the `module` block and is useful when there are many variables to pass
B) By default, a child module inherits all provider configurations from its parent module — no explicit `providers` argument is needed unless you want the child module to use a **different** provider configuration (for example, a provider aliased to a different region); in that case, `providers = { aws = aws.us-west-2 }` passes the aliased provider to the child module
C) The `providers` argument must be specified in every `module` block — if it is omitted, Terraform raises an error about unresolved provider references inside the child module; there is no default provider inheritance behaviour
D) The `providers` argument accepts only provider aliases — passing a non-aliased default provider using `providers = { aws = aws }` is invalid HCL syntax

---

### Question 8

**Difficulty:** Medium
**Answer Type:** many
**Topic:** Terraform Registry published modules — which TWO statements are TRUE?

Which TWO of the following statements about modules published to the Terraform Registry are TRUE?

A) Any user or organisation can publish a public module to the Terraform Registry — the only requirement is that the module source code lives in a GitHub repository named following the convention `terraform-<PROVIDER>-<NAME>` (e.g., `terraform-aws-vpc`); modules from other version control systems (GitLab, Bitbucket) cannot be published to the public registry
B) Published registry modules support the `version` argument in the calling `module` block, allowing operators to use constraint expressions such as `"~> 5.0"` (compatible with 5.x), `">= 4.0, < 6.0"` (range), or `"= 5.1.0"` (exact pin) — the Terraform Registry serves as the version resolver
C) Terraform private registries (available through HCP Terraform and Terraform Enterprise) allow organisations to publish modules internally — these private modules use the same `<NAMESPACE>/<MODULE>/<PROVIDER>` source format and `version` argument as public registry modules, but are only accessible to authenticated members of the organisation
D) When a `module` block references a Terraform Registry module without specifying a `version` argument, `terraform init` always downloads the oldest published version to ensure maximum backwards compatibility — operators must explicitly set a `version` constraint to get a newer version

---

### Question 9

**Difficulty:** Medium
**Answer Type:** one
**Topic:** Passing a child module output as an input to another child module — which statement is TRUE?

Which of the following statements about passing one child module's output as an input to another child module in the root configuration is TRUE?

A) Module outputs can only be passed to `resource` blocks in the root module — they cannot be passed directly as inputs to other `module` blocks; if a value from module A needs to reach module B, it must first be assigned to a local value in the root module
B) The root module can directly pass a child module's output as an input to another child module by referencing `module.<source_module>.<output_name>` in the receiving module's `module` block argument — Terraform automatically determines the correct dependency ordering: module B will not be evaluated until module A has completed, because module B's input depends on module A's output
C) Passing a child module's output to another child module creates a circular dependency and is always rejected by Terraform's configuration validation
D) Module A's output can be passed to module B's input only if both modules are in the same local directory — cross-directory module output composition is not supported

---

### Question 10

**Difficulty:** Medium
**Answer Type:** one
**Topic:** `terraform init -upgrade` and module versions — which statement is FALSE?

Which of the following statements about `terraform init -upgrade` and module version resolution is FALSE?

A) `terraform init -upgrade` causes Terraform to re-evaluate all `version` constraints for Terraform Registry modules and download the latest version that satisfies each constraint, replacing any previously cached module version in `.terraform/modules/`
B) For local path modules, `terraform init -upgrade` performs a full module re-download from a remote source — because local modules can change at any time, `-upgrade` forces Terraform to fetch the latest code from the original remote registry location to ensure the cached copy is current
C) `terraform init -upgrade` also upgrades provider versions — it consults the `version` constraints in `required_providers` blocks and the lock file, updates the lock file to the latest satisfying provider versions, and downloads the new provider binaries
D) `terraform init -upgrade` is the recommended command to explicitly adopt a newer minor or patch version of a module or provider when your constraints permit it — after running it, the updated selections should be reviewed and committed to version control

---

### Question 11

**Difficulty:** Hard
**Answer Type:** one
**Topic:** Four statements about module `for_each` instance addressing — only ONE is TRUE

Four statements about how `for_each` module instances are addressed in Terraform are presented below. Which is the ONLY TRUE statement?

A) When `for_each` is set on a module block, all instances share a single address — Terraform identifies individual instances internally but they are all listed under `module.<name>` without a key suffix; this is why `terraform state list` shows `module.vpc` rather than `module.vpc["prod"]`
B) When `for_each = toset(["prod", "dev"])` is set on a module block, the module instances are addressed as `module.<name>["prod"]` and `module.<name>["dev"]`; referencing a specific instance's output in the root module uses `module.<name>["prod"].<output_name>`; in `terraform apply -target`, the correct flag to target only the prod instance is `-target='module.vpc["prod"]'`
C) Module `for_each` instances are addressed using numeric indices regardless of whether `for_each` was given a map or a set — Terraform converts all `for_each` collections to indexed lists internally; `module.vpc[0]` and `module.vpc[1]` are always the correct addressing format
D) When `for_each` is used on a module block, the `each.key` and `each.value` references are only available in the root module's `module` block argument list — resources inside the child module CANNOT access `each.key` or `each.value`; child module resources must use input variables to receive the key values

---

### Question 12

**Difficulty:** Hard
**Answer Type:** many
**Topic:** Module meta-arguments — which TWO statements are TRUE?

Which TWO of the following statements about module meta-arguments (`count`, `for_each`, `depends_on`, `providers`, `version`) are TRUE?

A) The `version` meta-argument is valid on `module` blocks that use EITHER a Terraform Registry source OR a Git-based source — for Git sources, `version` is interpreted as a semantic version constraint and matched against the repository's release tags
B) All five module meta-arguments (`count`, `for_each`, `depends_on`, `providers`, `version`) can be used simultaneously on the same `module` block — there are no restrictions on combining them
C) `count` and `for_each` are mutually exclusive on a module block — a single module block cannot use both at the same time; attempting to set both `count` and `for_each` on the same `module` block causes a Terraform configuration error
D) The `providers` meta-argument in a module block maps the child module's **required provider names** to provider configurations in the calling module — if a child module has `required_providers { aws = { source = "hashicorp/aws" } }`, the parent can map it using `providers = { aws = aws.us-west-2 }` to supply an aliased provider to the child

---

### Question 13

**Difficulty:** Hard
**Answer Type:** one
**Topic:** Four statements about how Terraform modules handle provider requirements — only ONE is TRUE

Four statements about provider requirements and module composition are presented below. Which is the ONLY TRUE statement?

A) A child module MUST redeclare all providers it uses in its own `terraform { required_providers {} }` block — if a child module uses `aws_instance` without declaring `hashicorp/aws` as a required provider, `terraform init` resolves no provider for the child module and the configuration errors
B) When a child module does NOT declare `required_providers`, Terraform automatically discovers all provider requirements by inspecting which resource types the module uses and resolves the appropriate provider versions from the registry — no explicit provider declaration is needed anywhere in the module tree
C) A child module should declare its own `required_providers` specifying the providers it uses and their minimum version constraints — this is best practice because it documents the module's requirements, enables independent version validation, and ensures that callers who install the module via `terraform init` get a compatible provider version; the root module's lock file still governs the actual installed version, but the child's declaration constrains what is acceptable
D) Provider requirements declared in a child module's `required_providers` are completely ignored by the root module — only the root module's `required_providers` block affects provider version resolution; child module `required_providers` declarations exist solely for documentation purposes and have no effect on `terraform init`

---

### Question 1

**Difficulty:** Easy
**Answer Type:** one
**Topic:** `terraform.tfstate.backup` — which statement is TRUE?

Which of the following statements about the `terraform.tfstate.backup` file is TRUE?

A) `terraform.tfstate.backup` maintains a complete version history of every `terraform apply` ever run — Terraform appends a new entry on every apply, so you can recover any earlier state by reading back through the file's history
B) `terraform.tfstate.backup` stores only the **most recent previous state** — it is overwritten on every `terraform apply` with the prior state, meaning it holds exactly one snapshot; for full version history across multiple applies, you need a backend that supports versioning (such as S3 with object versioning enabled, or HCP Terraform)
C) `terraform.tfstate.backup` is created only when Terraform detects that resources will be destroyed — it is a safety copy made automatically before any destructive operation; non-destructive applies do not update the backup file
D) `terraform.tfstate.backup` is stored in `.terraform/` alongside provider plugins and module cache — it is an internal Terraform file and should never be inspected or modified directly by operators

---

### Question 2

**Difficulty:** Easy
**Answer Type:** one
**Topic:** `terraform state list` vs `terraform state show` — which statement is TRUE?

Which of the following statements about `terraform state list` and `terraform state show` is TRUE?

A) `terraform state list` and `terraform state show` are aliases for the same command — both display all attributes for every resource currently tracked in state; the only difference is that `terraform state show` uses a condensed single-line format
B) `terraform state list` outputs ALL resource addresses currently tracked in state (e.g., `aws_vpc.main`, `module.networking.aws_subnet.public`) — it provides a full index of managed resources but shows NO attribute values; `terraform state show <address>` outputs ALL attribute key-value pairs for ONE specific resource at the given address, displaying the same information Terraform stores in state for that resource
C) `terraform state list` requires a resource address argument — without it, the command returns an error because Terraform cannot determine which resource to list
D) `terraform state show` is not a standard subcommand of `terraform state` — attributes for a specific resource are viewed using `terraform inspect <address>` instead

---

### Question 3

**Difficulty:** Easy
**Answer Type:** many
**Topic:** HCP Terraform state storage — which TWO statements are TRUE?

Which TWO of the following statements about how HCP Terraform stores Terraform state are TRUE?

A) HCP Terraform stores state remotely for every workspace — state is encrypted at rest and in transit; each workspace has its own completely independent state file that is isolated from all other workspaces in the organisation
B) HCP Terraform automatically versions all state — a full history of every state version for every workspace is retained; operators can view the version history and roll back to any previous state version directly from the HCP Terraform UI or API
C) HCP Terraform's remote state storage is built on top of the AWS S3 backend — organisations must first provision an S3 bucket in their own AWS account and provide HCP Terraform with write access before remote state can be activated for a workspace
D) All workspaces within the same HCP Terraform organisation share a single logical state file — HCP Terraform uses resource namespacing internally to prevent resource address collisions, but the underlying state is a single shared document

---

### Question 4

**Difficulty:** Medium
**Answer Type:** one
**Topic:** `terraform state rm` — which statement is FALSE?

Which of the following statements about `terraform state rm` is FALSE?

A) `terraform state rm` removes the specified resource from Terraform's state file, but takes NO action against the actual cloud resource — the infrastructure object (EC2 instance, S3 bucket, etc.) continues to exist in the cloud completely unaffected; after the command runs, Terraform no longer tracks or manages that resource
B) A common use case for `terraform state rm` is deliberately abandoning management of a resource that should be preserved — for example, removing a database from state before deleting the Terraform configuration, so that `terraform destroy` does not attempt to delete the database
C) `terraform state rm aws_instance.web` destroys the EC2 instance in AWS — removing a resource from state is equivalent to destroying it because Terraform treats a resource absent from state as if it has never been provisioned and will attempt to recreate it on the next `terraform apply`
D) After running `terraform state rm aws_s3_bucket.media`, a subsequent `terraform plan` will show the bucket as a resource to be created — because the bucket is no longer in state, Terraform treats it as new infrastructure that needs to be provisioned, even though the bucket already exists in AWS

---

### Question 5

**Difficulty:** Medium
**Answer Type:** one
**Topic:** `terraform_remote_state` data source — which statement is TRUE?

Which of the following statements about the `terraform_remote_state` data source is TRUE?

A) The `terraform_remote_state` data source can access any attribute of any resource in the remote state file — for example, you can read `data.terraform_remote_state.vpc.outputs.aws_vpc.main.id` to directly access the VPC resource's ID without the remote configuration needing to expose it as an output
B) The `terraform_remote_state` data source requires the remote state to be stored in HCP Terraform — it does not work with self-managed backends like S3 or Azure Blob Storage; for cross-configuration state sharing with non-HCP backends, you must copy state values manually
C) The `terraform_remote_state` data source exposes only the **output values** declared in the remote configuration's `output` blocks — individual resource attributes are NOT directly accessible; operators who want to share infrastructure values across configurations must declare them as `output` blocks in the producing configuration; the consuming configuration then reads them as `data.terraform_remote_state.<name>.outputs.<output_name>`
D) The `terraform_remote_state` data source automatically re-triggers a plan in the consuming configuration whenever the remote state changes — HCP Terraform detects state version changes in the referenced workspace and immediately queues a run in the consuming workspace to incorporate the new values

---

### Question 6

**Difficulty:** Medium
**Answer Type:** one
**Topic:** HCP Terraform workspace execution modes — which statement is FALSE?

Which of the following statements about HCP Terraform workspace execution modes (CLI-driven, VCS-driven, API-driven) is FALSE?

A) A **VCS-driven workspace** is connected to a specific branch in a VCS repository — pushing commits to that branch automatically triggers a Terraform run in HCP Terraform; the plan runs immediately, and if auto-apply is disabled, a human must approve before apply executes
B) A **CLI-driven workspace** uses HCP Terraform as the remote execution backend — when a developer runs `terraform plan` or `terraform apply` locally, the operation streams to HCP Terraform's managed infrastructure for execution; state and the run history are stored in HCP Terraform, but the trigger comes from the developer's local CLI
C) **API-driven workspaces** have no VCS connection and no CLI trigger — all runs are initiated programmatically via HCP Terraform's API, making them suitable for custom CI/CD pipelines or external orchestration tools that need precise control over when and what Terraform runs
D) When a workspace is configured as VCS-driven, developers can also trigger additional runs directly from the `terraform apply` CLI command on their workstations — both the VCS webhook and CLI triggers are simultaneously active; HCP Terraform merges runs from both sources into a single queue using timestamp ordering

---

### Question 7

**Difficulty:** Medium
**Answer Type:** one
**Topic:** Sentinel policy enforcement levels — which statement is TRUE?

Which of the following statements about HCP Terraform's Sentinel policy enforcement levels is TRUE?

A) `advisory` enforcement blocks a run until a team member acknowledges the policy failure — the run cannot proceed automatically even if auto-apply is enabled; a human must review and dismiss the advisory before the apply phase begins
B) `soft-mandatory` enforcement blocks a run if a policy fails, but any user with at least Write permission on the workspace can override the failure and allow the run to proceed — this makes soft-mandatory suitable for team-level guardrails where workspace owners need flexibility
C) `hard-mandatory` enforcement blocks a run if a policy fails AND the failure **cannot be overridden by any user**, including organisation owners — it is the strictest enforcement level, designed for regulatory or compliance requirements that must never be bypassed under any circumstances
D) All three enforcement levels (`advisory`, `soft-mandatory`, `hard-mandatory`) apply the same way regardless of whether the policy framework is Sentinel or OPA — the enforcement level is a run-level setting, not a policy-level setting, so a single enforcement level governs all policies that evaluate during a run

---

### Question 8

**Difficulty:** Medium
**Answer Type:** one
**Topic:** OPA (Rego) vs Sentinel as policy frameworks — which statement is TRUE?

Which of the following statements about HCP Terraform's support for policy-as-code frameworks is TRUE?

A) HCP Terraform supports only HashiCorp Sentinel for policy enforcement — OPA (Open Policy Agent) integration is available only in Terraform Enterprise on-premise deployments, not in the SaaS HCP Terraform product
B) Sentinel and OPA are both supported in HCP Terraform — Sentinel uses the proprietary HashiCorp Sentinel DSL, while OPA uses the Rego language developed by the Open Policy Agent community; organisations can use either or both frameworks simultaneously in their policy sets, and the same three enforcement levels (`advisory`, `soft-mandatory`, `hard-mandatory`) apply to policies written in either language
C) OPA policies in HCP Terraform use HCL syntax for consistency with the rest of the Terraform toolchain — since OPA was contributed to the Cloud Native Computing Foundation (CNCF) by HashiCorp, its policy language was aligned with HCL to reduce the learning curve for existing Terraform operators
D) When both Sentinel and OPA policies are configured in an organisation, Sentinel policies always evaluate first — if any Sentinel policy blocks a run, OPA policies are skipped entirely; this precedence ordering is fixed and cannot be changed in the policy set configuration

---

### Question 9

**Difficulty:** Medium
**Answer Type:** one
**Topic:** HCP Terraform health assessments (drift detection) — which statement is TRUE?

Which of the following statements about HCP Terraform health assessments is TRUE?

A) HCP Terraform health assessments automatically apply drift corrections — when a scheduled health assessment detects that a cloud resource has drifted from its Terraform-managed state, HCP Terraform immediately queues and auto-approves an apply to restore the resource to its defined configuration; no human action is required
B) Health assessments detect infrastructure drift by running `terraform plan -refresh-only` on a configurable schedule — the assessment queries cloud provider APIs to check current resource attribute values against what Terraform has in state; any differences are flagged as drift; results are visible in the HCP Terraform UI and notifications can be sent; the assessment does NOT apply any changes — it is purely observational
C) Health assessments are available in all HCP Terraform tiers starting from the free tier — drift detection is enabled by default for all workspaces and cannot be disabled without contacting HashiCorp support
D) Health assessments require Sentinel policy sets to be configured for the workspace — drift detected during an assessment is evaluated against active policies, and if no policies are defined, the assessment exits immediately without reporting any results

---

### Question 10

**Difficulty:** Medium
**Answer Type:** many
**Topic:** HCP Terraform workspace RBAC — which TWO statements are TRUE?

Which TWO of the following statements about HCP Terraform's role-based access control (RBAC) model are TRUE?

A) HCP Terraform defines four workspace-level permission tiers: **Read** (view runs, state, and variables), **Plan** (trigger speculative plans), **Write** (trigger runs and approve applies), and **Admin** (manage workspace settings, variables, VCS connections, and team access) — each tier is a superset of the permissions below it
B) In HCP Terraform, access permissions are assigned per individual user for each workspace — there is no concept of a team or group; every user must be individually granted a workspace permission level; this per-user model is the only way to manage access
C) A HCP Terraform **team token** provides API authentication that carries the access level of the team it represents — CI/CD pipelines can use a single team token to authenticate and trigger plans and applies across all workspaces the team has been granted Write access to, without needing individual user credentials
D) HCP Terraform's workspace permission model has two levels only: Read and Write — there are no intermediate levels; the Plan-only and Admin tiers described in documentation are legacy terms that map to Read and Write respectively in the current platform

---

### Question 11

**Difficulty:** Medium
**Answer Type:** one
**Topic:** `terraform state mv` — which statement is FALSE?

Which of the following statements about `terraform state mv` is FALSE?

A) `terraform state mv` updates resource addresses within the state file — it is the correct tool to use when you rename a resource block in configuration (e.g., changing `resource "aws_instance" "old_name" {}` to `resource "aws_instance" "new_name" {}`) without wanting Terraform to destroy and recreate the resource
B) `terraform state mv aws_instance.old aws_instance.new` renames the cloud EC2 instance in AWS — the command sends an API call to the AWS provider that updates the instance's Name tag and associated identifier to reflect the new Terraform resource name; this is why the command is called "move"
C) After running `terraform state mv aws_instance.old aws_instance.new`, a subsequent `terraform plan` should show "No changes" — because the state address now matches the resource block address in configuration, Terraform sees no difference between desired and actual state for that resource
D) `terraform state mv` can also move a resource into a child module — for example, `terraform state mv aws_vpc.main module.networking.aws_vpc.main` updates the state address to reflect that the resource is now managed inside the `networking` module, without affecting the real VPC in AWS

---

### Question 12

**Difficulty:** Hard
**Answer Type:** one
**Topic:** Four statements about local Terraform workspaces vs HCP Terraform workspaces — only ONE is TRUE

Four statements about Terraform workspaces are presented below. Which is the ONLY TRUE statement?

A) Terraform OSS workspaces (`terraform workspace new`, `terraform workspace select`) and HCP Terraform workspaces are the same underlying feature — both create isolated environments with separate state, variables, execution environments, and RBAC; the only distinction is where the state is hosted (local filesystem vs HCP Terraform cloud); migrating from OSS workspaces to HCP Terraform requires only changing the backend block
B) Terraform OSS workspaces are a **state segregation feature within a single backend and a single configuration** — all OSS workspaces in a configuration set share the same `.tf` files and differ only in their state files; HCP Terraform workspaces, by contrast, are fully isolated environments with independent state, **separate variable sets** (including environment variables), run history, access permissions, and execution infrastructure; the two concepts share the word "workspace" but represent fundamentally different models; using OSS workspaces is not the same as using HCP Terraform
C) When connected to HCP Terraform via a `cloud` block, running `terraform workspace new staging` creates a temporary staging copy of the configuration that is automatically discarded after the next `terraform apply` on the production workspace — the staging workspace acts as a short-lived preview environment managed entirely by HCP Terraform with no further operator action needed
D) Local `terraform workspace select prod` and HCP Terraform workspace selection are identical operations — selecting a workspace in either context causes Terraform to immediately trigger a speculative plan against the selected workspace and display the current difference between local configuration and the workspace's remote state; this plan preview is required before any subsequent `terraform apply`

---

### Question 13

**Difficulty:** Hard
**Answer Type:** one
**Topic:** Four statements about dynamic provider credentials (OIDC) in HCP Terraform — only ONE is TRUE

Four statements about HCP Terraform dynamic provider credentials are presented below. Which is the ONLY TRUE statement?

A) Dynamic provider credentials in HCP Terraform work only with AWS — Azure and GCP require static long-lived credentials (service account keys or client secrets) stored as workspace environment variables, because those providers' identity platforms use proprietary token formats incompatible with the OIDC protocol that HCP Terraform generates
B) Dynamic provider credentials are enabled by default for all new HCP Terraform workspaces — no additional configuration is required; every workspace automatically uses OIDC authentication with whatever cloud provider is detected from the provider block in the configuration
C) Dynamic provider credentials use OIDC (OpenID Connect) to issue a **short-lived token for each individual run** — instead of storing a static access key or service account credential in workspace variables, HCP Terraform's identity acts as an OIDC provider; the cloud provider (AWS, Azure, or GCP) is configured to trust tokens from HCP Terraform; when a run starts, HCP Terraform requests a short-lived credential by exchanging its OIDC token; this eliminates long-lived static credentials from workspace variables entirely and creates a per-run audit trail
D) Dynamic provider credentials require Terraform Enterprise — HCP Terraform SaaS does not support OIDC-based authentication because the multi-tenant architecture of the SaaS platform prevents the OIDC handshake required between HCP Terraform's identity service and external cloud provider IAM systems



## Answer Key

| Q# | Answer(s) | Explanation | Source | Difficulty |
|---|---|---|---|---|
| 2 | C | ** Terraform's multi-cloud capability is one of its defining characteristics and a common exam topic. A single Terraform configuration can declare resources across multiple cloud providers simultaneously — each provider (AWS, Azure, GCP, etc.) is a separate plugin declared in the `required_providers` block, and resources from each provider coexist in the same state file. This is in contrast to provider-specific tools: AWS CloudFormation is AWS-only, Azure Bicep/ARM is Azure-only, and Google Cloud Deployment Manager is GCP-only. Pulumi also supports multi-cloud but uses general-purpose programming languages rather than HCL. Options A, B, and D are false — CloudFormation has no multi-cloud capability, ARM/Bicep are Azure-only, and there is no Microsoft-maintained Bicep-to-AWS compatibility layer. | ** Multi-cloud scope of Terraform vs single-cloud tools — which statement is TRUE? | ** Easy |
| 3 | B | ** Option B is FALSE. Idempotency means "applying the same configuration N times produces the same result" — it does NOT mean Terraform never destroys resources. Destruction is absolutely within Terraform's idempotent model. For example, setting `count = 0` in a resource block is a valid, idempotent desired state: Terraform will always converge to zero instances of that resource. If you reduce a `count` from 5 to 3, the two excess instances will be destroyed on every apply until the configuration changes again. The promise of idempotency is about repeatability of outcome, not about preventing any particular type of operation. Options A, C, and D are all true statements about idempotency. | ** Which statement about idempotency is FALSE? | ** Easy |
| 4 | A, C | ** **(A)** The audit trail benefit is a core IaC advantage: infrastructure changes committed to version control (Git) are traceable — every commit has an author, timestamp, and optional commit message explaining why the change was made. This replaces the opaque "someone clicked something in the console last Tuesday" problem of ClickOps. **(C)** Disaster recovery is explicitly listed as an IaC benefit: if an environment is destroyed, it can be fully rebuilt by running the configuration against a fresh account or region. The code IS the blueprint. Option B is false — Terraform absolutely requires state management; the state file is how Terraform tracks the real-world attributes of managed resources and computes diffs between plans. Option D is false — IaC tools provision infrastructure according to what you declare; they do not automatically add encryption or security controls not present in the configuration. | ** Which TWO statements about IaC benefits are TRUE? | ** Easy |
| 5 | B | ** "Desired state" is the infrastructure configuration that the engineer has DECLARED in `.tf` files — it represents the intended, target state of infrastructure. This is distinct from "current state," which is what Terraform believes actually exists in the cloud (recorded in the state file and refreshed by querying cloud APIs during plan). Terraform's core job is to reconcile these two: propose and apply the minimal set of changes that transform current state into desired state. Option A is a critical misconception: `terraform.tfstate` records CURRENT state, not desired state. Editing the state file does not change what Terraform will create — it changes what Terraform thinks currently exists. Option C is false — they represent different things by design. Option D is false — Terraform reads `.tf` HCL files directly; while Terraform internally uses JSON representations for provider communication, the canonical format for desired state is HCL. | ** Which statement about "desired state" is TRUE? | ** Medium |
| 6 | B | ** The declarative model is central to how Terraform works and is a major exam objective. In a declarative approach, the engineer describes the DESIRED END STATE — "I want 3 EC2 instances of type t3.micro with these properties" — and the tool figures out HOW to get there. This is the opposite of the imperative approach (e.g., Ansible playbooks, shell scripts) where the engineer writes the explicit steps. The declarative approach has significant advantages: Terraform will add only what is missing, update only what has changed, and remove only what should no longer exist — it never blindly re-creates everything. Option A describes the IMPERATIVE approach, not declarative. Option C is false — destroy-and-recreate on every apply would be extraordinarily disruptive and is NOT how Terraform works; it only destroys when the desired state explicitly removes a resource. Option D is false — the declarative approach has concrete advantages including idempotency, drift detection, and minimal-change plans. | ** Which statement about the declarative IaC approach is TRUE? | ** Medium |
| 7 | C | ** Option C is FALSE. Terraform is NOT an agent-based, continuously monitoring tool that self-heals in the background. Terraform is a CLI tool — it only acts when explicitly invoked by an engineer running a command. There is no background process watching for drift and automatically applying corrections. When drift occurs, an engineer must DETECT it (by running `terraform plan` or `terraform plan -refresh-only`) and then REMEDIATE it (by running `terraform apply` to restore desired state, or `terraform apply -refresh-only` to update state to accept the drift). HCP Terraform has a "Health Assessments" feature that runs scheduled `refresh-only` checks and sends notifications, but even this does NOT auto-apply — it only alerts. Options A, B, and D are all true statements about drift. | ** Which statement about infrastructure drift is FALSE? | ** Medium |
| 8 | C | ** Option C accurately describes the design philosophy and primary use case of each tool. Ansible operates by executing a list of tasks in order — "copy this file, then install this package, then start this service" — which is an imperative style. While Ansible has some idempotency features, the core model is task execution. Terraform operates declaratively: define the desired end state, and Terraform computes and applies the diff. Option A is false — Ansible is considered imperative (or "procedural"), not purely declarative. Option B is false — Ansible does NOT maintain a state file; it re-runs its tasks against the current state of systems on every run without recording what was previously applied (Ansible relies on module-level idempotency rather than a central state). Option D is false — Ansible excels at configuration management (OS-level, application-level); Terraform excels at infrastructure provisioning; they are complementary tools often used together, not interchangeable. | ** Ansible vs Terraform — which claim about their design approaches is TRUE? | ** Medium |
| 9 | B | ** The audit trail benefit is one of the named advantages of IaC. When infrastructure configuration files are committed to version control (Git), every change produces a commit that captures: the AUTHOR (who changed it), the TIMESTAMP (when), the DIFF (exactly what changed — which argument values, which resources were added or removed), and optionally the RATIONALE (commit message or linked pull request). This audit trail is freely available with community Terraform and a standard Git repository — no paid tier is required. The combination of version-controlled infrastructure code and pull request workflows means every infrastructure change can be reviewed, approved, and traced back to a specific decision. Option A is false — Vault is a secrets management tool, not an audit trail system; Git alone provides the audit trail. Option C is false — Git-based audit trails require no paid tooling. Option D is false — Git diffs capture all types of changes (creates, updates, and deletes) to configuration files. | ** Which statement about the audit trail benefit of IaC is TRUE? | ** Medium |
| 10 | A, D | ** **(A)** is FALSE. Terraform's declarative model is explicitly NOT destroy-and-recreate on every apply. This is a critical misconception. Terraform computes the MINIMAL set of changes needed to bring current state to desired state. If the infrastructure already matches the configuration, no actions are taken. Only resources that are new, changed, or removed from the configuration are affected. Destroying and recreating everything on every apply would be catastrophically disruptive in production environments. **(D)** is FALSE. IaC benefits apply at ANY scale. Even for a project with 3-5 resources, IaC provides: reproducibility (anyone can recreate the environment), audit trail (changes tracked in Git), documentation (config files describe the infrastructure), and safety (plan preview before apply). The learning curve exists, but the "only useful at large scale" claim is false. Option B is TRUE — repeatability is a named IaC benefit. Option C is partially true (CloudTrail does log console actions) but is subtly FALSE as a general equivalence claim — ClickOps audit trails (CloudTrail logs) are harder to tie to intent, lack structured diffs of desired state, and don't provide the review/approval workflow of PRs; however, for this question, A and D are the clearest false statements. | ** Which TWO statements about Infrastructure as Code are FALSE? | ** Medium |
| 11 | B | ** Disaster recovery is explicitly listed as a benefit of IaC. The core insight is: "infrastructure defined as code can be recreated from that code." If a region goes down, an account is compromised, or an environment is accidentally destroyed, the configuration files serve as the complete blueprint for rebuilding. Running `terraform apply` against a fresh environment recreates all declared resources. This is a massive advantage over manually provisioned infrastructure, where the knowledge of how everything was configured may exist only in a human's memory or in hard-to-parse console logs. Option A overstates the requirement — remote state is best practice but not a prerequisite for the disaster recovery benefit; even with a local state file backed up to version control, the configuration files are the recovery tool. Option C is false — databases, queues, and other stateful services ARE describable in Terraform configuration (e.g., `aws_rds_instance`, `aws_sqs_queue`) and can be recreated; recovering the DATA is a separate concern (backups), but the infrastructure is IaC-recoverable. Option D is false — Terraform supports cross-region and cross-account deployments. | ** Which statement about the disaster recovery benefit of IaC is TRUE? | ** Medium |
| 12 | C | ** Option C is FALSE. It has the labels backwards. TERRAFORM uses a declarative approach — you write HCL that describes the desired end state, and Terraform determines what actions to take. PULUMI writes infrastructure in general-purpose programming languages that look imperative (you write code with loops, conditionals, and function calls), but the underlying model is still declarative in the sense that Pulumi also tracks desired state and computes diffs. The KEY difference between the two tools is NOT "declarative vs imperative" — it is the LANGUAGE used to express desired state (HCL/DSL for Terraform vs general-purpose programming languages for Pulumi). Option A is true — both use provider plugins for multi-cloud support. Option B is true — Pulumi's language support is its defining feature compared to Terraform's HCL. Option D is true — both tools maintain state files for diff computation. | ** Which statement comparing Pulumi to Terraform is FALSE? | ** Medium |
| 13 | C | ** Option C is the correct, true statement. It captures the essence of Terraform's declarative model: the engineer declares WHAT, not HOW. The dependency graph (built from explicit `depends_on` and implicit references like `aws_subnet.main.id`) determines the order of operations, not the order of blocks in files. **(A)** is FALSE — Terraform is DECLARATIVE, not imperative. HCL is a DSL for expressing desired state, not a procedural language. Resource block order within `.tf` files is irrelevant to execution order; Terraform's DAG determines sequencing. **(B)** is FALSE — resource processing order is determined by the dependency graph, not alphabetical ordering. **(D)** is FALSE — this is one of the most important misconceptions to reject. Terraform's idempotent, declarative model means there is NO need for "create if not exists" guards. Terraform checks whether the resource already exists (by querying state and the cloud provider) and only creates it if it doesn't exist and the configuration declares it should. The entire point of the declarative model is that the engineer does not write these conditionals — the tool handles convergence automatically. | ** Four statements about Terraform's declarative model — which is the ONLY TRUE statement? | ** Hard |
| 14 | A, C | ** **(A)** is TRUE. The `.tf` configuration files are the single source of desired state — they are the human-authored declaration of what infrastructure should exist. This is what the engineer edits to add, change, or remove resources. **(C)** is TRUE. The `terraform.tfstate` file records current tracked state — specifically, the attributes of resources that Terraform has successfully created and the values that the cloud provider assigned (IDs, IPs, etc.). These are values that couldn't be known until after the resource was created (a VPC ID is assigned by AWS, not pre-determined). This state data is essential for computing diffs: Terraform compares A (desired, from `.tf`) with C (current, from state) to produce the plan. **(B)** is FALSE — a critical misconception. The state file records CURRENT state, not desired state. If you delete a resource block from your `.tf` file, that expresses the desired state of "this resource should not exist" — Terraform reads the `.tf` file for desired state, NOT the state file. **(D)** is FALSE and dangerous. Manually editing `terraform.tfstate` is explicitly NOT recommended for expressing desired infrastructure. It is a low-level operation (used occasionally for state surgery via `terraform state` commands) that bypasses all safeguards. Adding a resource block to a `.tf` file is the correct way to declare desired infrastructure. Direct state file edits can corrupt state and cause Terraform to take unexpected actions. | ** Which TWO statements about the relationship between IaC configuration files and Terraform state are TRUE? | ** Hard |
| 15 | B | ** Option B correctly enumerates all five responsibilities of a Terraform provider plugin: (1) **Authentication** — the provider handles credentials and API authentication so engineers don't write auth logic in HCL; (2) **CRUD operations** — the provider implements Create, Read, Update, Delete for every resource type it manages; (3) **Data sources** — providers expose read-only data sources for querying existing infrastructure; (4) **Validation** — the provider validates resource configuration against its schema before any API call is made; (5) **State mapping** — the provider maps resource attributes (including computed attributes like resource IDs and IP addresses assigned by the cloud) to and from the state file format. Option A is false — providers handle CRUD, not just auth. Option C is false — providers are declared in `required_providers`, not imported via an `import` statement; `import` in Terraform is an entirely different concept (importing existing infrastructure into state). Option D is false — Terraform Core manages writes to the state file; the provider populates attribute values that Core then persists. | ** Five provider responsibilities — which statement is TRUE? | ** Easy |
| 16 | B | ** Option B is FALSE and represents one of the most important security misconceptions in Terraform. `sensitive = true` is a DISPLAY-ONLY flag — it tells Terraform to redact the value in CLI output (terminal display, `terraform output`, plan summaries) by showing `(sensitive value)` instead of the raw value. It does NOT encrypt the value in `terraform.tfstate`. All resource attributes — including passwords, secret keys, tokens, and other credentials — are stored in plaintext JSON inside the state file, regardless of any `sensitive` annotation. This means anyone with access to the state file (or the remote storage bucket containing it) can read those values. Options A, C, and D are all true, correct statements that accurately describe this security reality and the appropriate mitigation (encrypted remote backend). | ** `sensitive = true` — which statement is FALSE? | ** Easy |
| 17 | A, C | ** **(A)** is TRUE. The lock file records the exact version installed (e.g., `version = "5.31.0"`), the original constraint from `required_providers` (e.g., `constraints = "~> 5.0"`), and cryptographic hashes (`h1:` and `zh:` entries). On subsequent `terraform init` runs, Terraform uses these hashes to verify that the downloaded binary matches what was originally installed — protecting against supply chain tampering. **(C)** is TRUE. `terraform init -upgrade` is the deliberate mechanism for advancing locked provider versions — it ignores the current lock file entries, resolves the newest version matching the constraint, downloads it, verifies it, and rewrites the lock file. Without `-upgrade`, `terraform init` respects the locked version and will not upgrade even if a newer version exists within the constraints. **(B)** is FALSE — this is a critical error. `.terraform.lock.hcl` MUST be committed to version control; `.terraform/` should be gitignored. **(D)** is false — the lock file contains version and hash metadata only, not provider source code. | ** Which TWO statements about `.terraform.lock.hcl` are TRUE? | ** Easy |
| 18 | C | ** State locking is a critical feature for team safety and is one of the key advantages of remote state over local state. Local state (`terraform.tfstate` on disk) has NO locking mechanism — there is nothing preventing two engineers from running `terraform apply` simultaneously, and concurrent applies can produce corrupted state or conflicting resource changes. Remote backends implement locking differently by backend: S3 uses a DynamoDB table for lock records; HCP Terraform (formerly Terraform Cloud) uses its own internal locking; Azure Blob Storage uses blob leases; GCS uses object versioning and generation conditions. When a remote lock is acquired, any other `terraform plan` or `terraform apply` will fail with a lock error until the first operation completes (or the lock is force-released). Option A is false — local state has no concurrent-detection mechanism. Option B is false — locking is NOT a feature of the local state format. Option D is false — S3 + DynamoDB locking is available to any Terraform user at no extra cost beyond standard AWS pricing. | ** Local vs remote state — which statement about locking is TRUE? | ** Medium |
| 19 | B | ** Option B is FALSE. The LOCAL NAME used in the `required_providers` block is an arbitrary label chosen by the engineer — it does NOT need to match the provider type in the source address. The local name is simply a reference key used within that Terraform configuration. For example, you could write `myaws = { source = "hashicorp/aws" }` and then use `provider "myaws" {}` and `provider = myaws.alias_name` throughout the configuration. The local name is distinct from the provider type in the source address. This flexibility exists to handle cases where two different providers might have the same type name (e.g., two DNS providers both named `dns` from different namespaces). Options A, C, and D are all true statements about provider source addresses. | ** Provider source address format — which statement is FALSE? | ** Medium |
| 20 | B | ** `terraform state rm` performs a state-only operation — it removes the resource's entry from `terraform.tfstate` but takes NO action against the actual cloud infrastructure. The real resource (EC2 instance, S3 bucket, RDS database, etc.) continues to run and exist in the cloud unaffected. The use cases for `terraform state rm` include: (1) stopping Terraform management of a resource without destroying it (e.g., handing it off to another team or tool), (2) removing orphaned state entries that no longer correspond to real resources, and (3) preparing for a state migration. After `state rm`, the resource is effectively invisible to Terraform — a subsequent `terraform plan` will show it as "no action needed" from Terraform's perspective (or if the resource block still exists in configuration, Terraform may propose to recreate it as if it were new). Option A is false — `state rm` does NOT delete the cloud resource. Option C is false — renaming a resource in state is done with `terraform state mv`, not `state rm`. Option D is false — all `terraform state` subcommands are available in the open-source CLI. | ** `terraform state rm` — which statement is TRUE? | ** Medium |
| 21 | C | ** Option C is FALSE. The Partner tier does NOT carry the same trust level as the Official tier. The key distinction is: **Official** providers are maintained DIRECTLY by HashiCorp — HashiCorp writes the code, manages releases, and is fully accountable. **Partner** providers are maintained by the TECHNOLOGY PARTNER (the third-party company) — HashiCorp has reviewed and approved the provider and the company has a formal partnership agreement, but HashiCorp does not write or own the code. This means the trust level is lower than Official: the partner company's reliability, security practices, and maintenance commitment determine the quality. Option C falsely claims both tiers require HashiCorp to "review and maintain the provider source code directly" — Partners maintain their own code. Options A, B, and D are accurate descriptions of the Partner tier. | ** Provider tier trust levels — which statement about the Partner tier is FALSE? | ** Medium |
| 22 | B | ** `-refresh=false` disables the state refresh step — the phase where Terraform makes API calls to each cloud provider to check the current, live attributes of managed resources. Without the refresh, Terraform uses whatever attribute values are already recorded in the state file (from the last successful apply or explicit refresh). This has a legitimate use case: in large environments with hundreds of resources, the refresh phase can take minutes because it involves hundreds of API calls. Engineers who KNOW the infrastructure hasn't changed and want faster iteration can use `-refresh=false` to skip this overhead. However, if drift has occurred (a manual console change, an external process modifying a resource), the plan will NOT detect it and may propose incorrect or incomplete changes. Option A is false — `-refresh=false` is not the recommended default; it is a performance optimization with a specific trade-off. Option C is false — `-refresh=false` suppresses refresh in a normal plan/apply cycle; `-refresh-only` is a completely different mode that ONLY performs a refresh and updates state to match current cloud reality (it does NOT make infrastructure changes). Option D is false — remote backends fully support real-time cloud API refreshes during plan. | ** `terraform plan -refresh=false` — which statement is TRUE? | ** Medium |
| 23 | A, C | ** **(A)** is TRUE. The three-source model is central to understanding how Terraform plans. Desired state (configuration) represents intent. Known state (tfstate) represents what Terraform last observed. Actual state (API refresh) represents reality. The plan bridges the gap from actual → desired, using known state to understand which resources are already managed and what their previous attributes were. **(C)** is TRUE. On a brand-new configuration with no existing state file, Terraform's known state is empty. Since there is no state to compare against, and assuming the actual cloud state is also empty (no pre-existing matching resources), Terraform proposes creating every resource in the configuration. This is correct and expected behaviour on first apply. **(B)** is FALSE — Terraform absolutely makes live API calls during the refresh phase of planning; the state file alone is not sufficient because actual infrastructure may have drifted from what's recorded. **(D)** is FALSE and inverts the model completely. The `.tf` configuration files ARE the desired state — not advisory. The cloud's current state is what Terraform tries to CHANGE to match the configuration, not the other way around. | ** Three sources of truth in `terraform plan` — which TWO are TRUE? | ** Medium |
| 24 | B | ** `terraform state mv` is a surgical state operation that moves a resource's state entry from one address to another WITHOUT touching the underlying cloud infrastructure. The primary use case is exactly as described in option B: when you rename a resource block in your configuration (e.g., from `aws_instance.old_name` to `aws_instance.new_name`), Terraform sees the old resource gone and a new one appearing — and would plan to destroy the old and create the new. Running `terraform state mv aws_instance.old_name aws_instance.new_name` BEFORE the configuration rename reconciles state so Terraform recognises the resource at its new address without any destroy/recreate. Option A is false — `state mv` is a state-only operation; no cloud resources are destroyed or recreated. Option C is false — `state mv` works with any resource regardless of meta-arguments, including simple resources, `count` instances (e.g., `aws_instance.app[0]`), and `for_each` instances (e.g., `aws_instance.app["prod"]`). Option D is false — Terraform does NOT automatically track label changes; without `state mv`, a renamed resource will always be planned as destroy+create. | ** `terraform state mv` purpose — which statement is TRUE? | ** Medium |
| 25 | B | ** Option B accurately describes the alias model. In Terraform, every provider type has at most one DEFAULT configuration — the `provider` block that has NO `alias` argument. When a resource block of that provider type does not specify a `provider` meta-argument, Terraform automatically uses this default. Aliased configurations are EXPLICITLY opt-in: a resource must declare `provider = aws.secondary` (format: `<local_name>.<alias>`) to use the aliased configuration. This design means you can add aliases without affecting existing resources that already work with the default. A common pattern is: default = primary region (e.g., `us-east-1`), alias = secondary region (e.g., `eu-west-1`); only resources that explicitly need the secondary region reference the alias. Option A is false — there is no round-robin or automatic distribution. Option C is false — the default provider still applies to resources that don't specify a `provider` argument, even when aliases exist. Option D is false — provider aliases are a Terraform Core feature available to ALL provider types regardless of tier. | ** Provider alias usage — which statement about the default provider is TRUE? | ** Medium |
| 26 | D | ** Option D is the only TRUE statement, and it combines two important exam concepts. First, state stores BOTH configuration-declared attributes AND computed attributes — values the cloud provider generates after resource creation (like an EC2 instance ID `i-0abc123`, a public IP address, an S3 bucket ARN). These computed values are essential for Terraform to track resources across plan/apply cycles and for referencing outputs from one resource as inputs to another. Second, everything in state is in PLAINTEXT JSON — the `sensitive = true` annotation does NOT encrypt state. Option A is false — state absolutely stores computed attributes (IDs, IPs, ARNs, etc.); this is one of the four core purposes of state. Option B is false and dangerous — `sensitive = true` provides only terminal display masking; it offers zero encryption protection in the state file; an encrypted backend is still required for secret safety. Option C is false — HashiCorp explicitly states "Never manually edit state." Manually editing `terraform.tfstate` can corrupt state records, break resource tracking, and cause unpredictable plan behaviour; `terraform state` subcommands (mv, rm, pull, push) are the safe, supported interface. | ** Four statements about Terraform state — only ONE is TRUE | ** Hard |
| 27 | A, C | ** **(A)** is TRUE. `~> 5.0` is syntactic sugar for `>= 5.0, < 6.0`. Both expressions produce an identical version range — any `5.x.x` version is permitted. Using `~>` is more concise and expresses intent clearly ("stay within major version 5"), but the multi-constraint form is equally valid and sometimes useful for expressing asymmetric ranges (e.g., `>= 5.5, < 5.20` to exclude both very old and very new minor versions). **(C)** is TRUE. When multiple constraints are combined, Terraform evaluates them as a logical AND — the selected version must satisfy ALL constraints. Terraform always resolves to the NEWEST version within the intersection of all constraints (unless a lock file is present, in which case the locked version is used). Selecting the minimum or the first-constraint result would be incorrect. **(B)** is FALSE. `~> 5.0.0` allows ONLY patch updates (`>= 5.0.0, < 5.1.0`). Version `5.1.0` changes the minor component and is outside this range. For minor-version flexibility, `~> 5.0` (two components) is needed. **(D)** is PARTIALLY TRUE but contains a false assertion. Using `= 5.31.0` (exact version) IS considered poor practice for the stated reason — it blocks all future updates including security patches. However, stating that `~> 5.31.0` is the "preferred approach" is misleading — `~> 5.31.0` only allows patch updates within `5.31.x`; most teams use `~> 5.0` for broader minor-version flexibility. The claim is too specific and partially incorrect, making the whole option false. | ** Which TWO statements about Terraform version constraints are TRUE? | ** Hard |
| 28 | D | ** Option D is FALSE. `terraform show` is a purely **read-only, offline** inspection command — it reads the existing state file (or a saved plan file) and displays its contents; it makes no API calls and writes nothing to disk. It does NOT refresh or modify the state file in any way. To refresh state with live cloud values, the correct command is `terraform apply -refresh-only` (or `terraform plan -refresh-only` to preview). `terraform show` is safe to run at any time with no side effects. Options A, B, and C are all accurate: `terraform show` displays current state, `terraform show plan.tfplan` inspects a saved plan, and `terraform show -json` outputs the state as machine-readable JSON. | ** `terraform show` — which statement is FALSE? | ** Easy |
| 29 | A is FALSE, B is TRUE, C is FALSE, D is FALSE → **Answer: B only** | ** **(A)** is TRUE. `terraform validate` is entirely offline. The provider schema needed to validate argument names and types is cached locally in `.terraform/providers/` by `terraform init`. Once init has been run, validate never makes a network call — this is one of its key advantages for fast local feedback and offline/CI environments. **(B)** is TRUE. `terraform apply` is the primary command that requires both network access AND writes to state. It connects to cloud provider APIs to perform CRUD operations and, after each resource change, writes the updated attributes back to the state file so subsequent plans have accurate known state. **(C)** is FALSE — `terraform plan` without `-out` does NOT persist the plan anywhere. If you run `terraform apply` immediately after without a plan file, Terraform generates a NEW plan at apply time (and prompts for confirmation). The `-out=` flag is specifically what saves a plan to disk. **(D)** is FALSE — `terraform output` reads output values from the local state file without any network calls. | ** Network and state-modification characteristics of CLI commands — which TWO are TRUE? | ** Easy |
| 30 | B | ** `terraform taint` was the original mechanism for marking a resource "tainted" so that Terraform would destroy and recreate it on the next apply. It is **deprecated** as of Terraform 0.15.2 / 1.x and may be removed in a future version. The replacement (no pun intended) is `terraform apply -replace="<resource_address>"`, which is cleaner for several reasons: (1) it generates a full plan preview showing the destroy-and-recreate before proceeding, (2) it is a single atomic command rather than two separate steps, (3) it avoids accidentally leaving a resource in a tainted state if you decide not to apply, and (4) the intent is explicit in the apply command itself. Option A is false — `taint` is deprecated. Option C is false — `apply -replace` still generates a plan and prompts for confirmation (unless `-auto-approve` is also passed). Option D is false — neither command has a "maintenance window" concept; both take effect on the next apply. | ** `terraform taint` deprecation — which statement is TRUE? | ** Medium |
| 31 | D | ** Option D is FALSE. `terraform init -upgrade` upgrades **provider plugins** (and module sources) — it does NOT upgrade the Terraform CLI binary itself. The CLI binary is a separate executable installed through system package managers, `tfenv`, `asdf`, or direct download from hashicorp.com; it cannot update itself via `init`. To upgrade the CLI, you use the appropriate installation mechanism for your platform. Options A, B, and C are all true, accurate descriptions of `-upgrade` behaviour: it bypasses the lock file's pinned version to resolve a newer provider version, rewrites the lock file with the new version and hashes, and is the required mechanism because plain `terraform init` strictly respects the lock file. | ** `terraform init -upgrade` — which statement is FALSE? | ** Medium |
| 32 | B | ** `terraform plan -destroy` is the safe, preview-only destroy workflow. It generates the same execution plan that `terraform destroy` would execute, showing every resource marked for deletion (with the `-` symbol) and the total count, but it applies NOTHING. This makes it valuable for: (1) reviewing the scope of destruction before proceeding — especially in large environments, (2) getting approval from a senior engineer or a code review, and (3) saving the plan to a file with `-out=destroy.tfplan` for a deterministic `terraform apply destroy.tfplan` later. `terraform destroy` itself is equivalent to `terraform apply -destroy` — both generate a destroy plan AND execute it (with confirmation). Option A is false — `-destroy` on `plan` is preview-only. Option C is false — `-target` is optional. Option D is false — there is no automatic Terraform Cloud scheduling triggered by a local plan. | ** `terraform plan -destroy` — which statement is TRUE? | ** Medium |
| 33 | B | ** `terraform apply -replace="<address>"` is the recommended Terraform 1.5+ mechanism for forcing a destroy-and-recreate of a specific resource. It is used when you suspect a resource is in a degraded state (a known-bad EC2 instance, a corrupt database, a misconfigured load balancer) and want Terraform to refresh it cleanly. Critically: the `-replace` flag forces replacement **regardless of whether any configuration attribute has changed** — you are overriding Terraform's normal change-detection logic and declaring "this resource must be recreated." In the plan output, the targeted resource shows the `-/+` replacement symbol. The plan is displayed for review (or auto-approved with `-auto-approve`), and the destroy-then-create happens within the single apply run. Option A is false — `-replace` both destroys AND recreates in one operation. Option C is false — `taint` is deprecated; they are not identical. Option D is false — `-replace` is unconditional; it does not inspect the live resource health before deciding. | ** `terraform apply -replace` — which statement is TRUE? | ** Medium |
| 34 | D | ** Option D is FALSE. `terraform fmt -diff` is a **display-only** flag — it shows the unified diff of what WOULD change but does NOT write any changes to disk. It is specifically the non-destructive preview mode of `terraform fmt`. To actually rewrite files AND see the diff, you would run `terraform fmt` (without `-diff`) and separately track changes via version control. The three commonly used `terraform fmt` flags for non-modifying operation are: `-diff` (show changes without writing), `-check` (exit non-zero if any changes needed without writing), and the combination `-check -diff` (exit non-zero AND show what's wrong). Options A, B, and C are all correct: `-diff` is display-only, `-check` is CI-enforcement mode, and combining both gives the most informative CI failure message. | ** `terraform fmt -diff` — which statement is FALSE? | ** Medium |
| 35 | A, C | ** **(A)** is TRUE. `terraform console` opens an interactive command line where engineers can type any HCL expression — including built-in functions (`cidrsubnet("10.0.0.0/8", 8, 2)`), string functions (`format("Hello, %s!", "world")`), type conversions (`toset(["a","b","a"])`), and arithmetic — and see the result immediately. It is the recommended way to test expressions before committing them to configuration. **(C)** is TRUE. `terraform console` is read-only and offline. It reads the current state file to provide values for resource attribute references but makes no API calls and writes no changes. Running `aws_instance.web.id` in the console reads the `id` from state — it does not call the AWS API. **(B)** is FALSE — `console` never writes to state or makes API calls. **(D)** is FALSE — `console` fully supports Terraform functions, resource references, variable references, and local values; simple arithmetic is a subset of what it can handle. | ** `terraform console` — which TWO statements are TRUE? | ** Medium |
| 36 | B | ** When you change the backend configuration (e.g., switching from local state to an S3 backend, or moving from one S3 bucket to another), a plain `terraform init` will detect the backend change and refuse to proceed until you acknowledge what to do with the existing state. The two flags address this differently: `-migrate-state` tells Terraform "yes, I want to move my existing state to the new backend" — Terraform will copy the state records to the new backend and prompt you to confirm. `-reconfigure` tells Terraform "just reset the backend connection; do NOT try to migrate anything" — useful when you want to point to a different backend but the state is already there (or you don't care about the old state). Option A is false — they are distinct flags with different behaviours. Option C is false — adding a backend block for the first time does NOT require `-reconfigure`; a plain `terraform init` handles the initial backend setup. Option D is false — `-migrate-state` still prompts for confirmation; it does not imply auto-approve. | ** `terraform init -migrate-state` vs `-reconfigure` — which statement is TRUE? | ** Medium |
| 37 | C | ** Option C is FALSE. `terraform output -json` is an entirely **offline** command — it reads output values directly from the local state file (or remote state, if a remote backend is configured, but only to read the state object — no cloud resource API calls). It does NOT make any calls to the cloud provider API. The output values in state were written during the last `terraform apply` and reflect the attribute values at that time. If those values have changed in the cloud since the last apply (drift), `terraform output -json` will show the stale recorded values; to get fresh values you would run `terraform apply -refresh-only` first. Options A, B, and D are all accurate: `-json` outputs all outputs as a JSON object, it is machine-readable and useful for scripting, and it reads from local state without network calls. | ** `terraform output -json` — which statement is FALSE? | ** Medium |
| 38 | B | ** Option B is the ONLY TRUE statement. The two-stage pipeline (`plan -out=file` then `apply file`) is the deterministic CI/CD pattern. When `terraform apply` receives a saved plan file as its argument (e.g., `terraform apply plan.tfplan`), it applies precisely those serialised operations — it does NOT re-evaluate the configuration, re-refresh state, or re-compute a new plan. This guarantees that what was reviewed (and potentially approved by a human or automated gate) is exactly what gets applied. Option A is FALSE — `terraform plan` is read-only with respect to the state file; it never writes proposed changes to state. (State is only updated by `terraform apply`.) Option C is FALSE — `terraform plan` and `terraform apply` are NOT equivalent. `plan` is read-only and makes no infrastructure changes; `apply` creates, updates, or deletes real cloud resources. Option D is FALSE — `-refresh=false` is a performance optimisation, not an accuracy improvement. A standard `terraform plan` WITH refresh is MORE accurate because it incorporates the current live state; `-refresh=false` may produce an INACCURATE plan if resources have drifted from recorded state. | ** Four statements about `terraform plan` — only ONE is TRUE | ** Hard |
| 39 | A, B | ** **(A)** is TRUE. The legacy `terraform import` CLI command (`terraform import aws_instance.web i-0abc123`) requires a matching resource block (e.g., `resource "aws_instance" "web" {}`) to already exist in the configuration. The command uses the resource type from the address to determine which provider/resource-type logic to use for the import; without the block, Terraform cannot determine which provider to call. After the import, the state file records the resource's attributes, but the engineer must still manually populate the resource block with the correct arguments to match the imported state. **(B)** is TRUE. The `import` block (Terraform 1.5+) is declarative HCL: you define `import { to = aws_instance.web; id = "i-0abc123" }` directly in a `.tf` file. Terraform incorporates this into `terraform plan`, showing the import as a proposed operation before applying — bringing imports into the same plan-review-apply workflow as other changes. It is version-controlled alongside configuration. **(C)** is FALSE. The legacy CLI `terraform import` does NOT generate the resource configuration block — the engineer must write it manually. The newer HCL `import` block combined with `terraform plan -generate-config-out=generated.tf` CAN generate a configuration stub, but this flag is separate from the import block itself and the output still requires engineer review. **(D)** is FALSE — `terraform import` only affects the Terraform state file; it does not destroy, move, or alter the actual cloud resource. The resource continues to exist in the cloud exactly as before; Terraform simply begins tracking it. | ** `terraform import` — which TWO statements are TRUE? | ** Hard |
| 40 | C | ** Terraform's dependency graph is built exclusively from **resource attribute references** — expressions of the form `<resource_type>.<local_name>.<attribute>` (e.g., `aws_vpc.main.id`) or `module.<name>.<output>`. When two resources both reference `var.region`, there is no edge between them because `var.region` is a scalar value resolved before graph construction begins — it is not a resource and has no creation lifecycle. The two resources will be created in parallel (assuming no other dependency). Similarly, `local.*` references are computed values, not resources, and create no graph edges. Only attribute references to other managed resources or module outputs create edges. Options A, B, and D all incorrectly claim that variable or local references create dependency edges. | ** Variable and local references — which statement is TRUE? | ** Easy |
| 41 | C | ** Option C is FALSE. `ignore_changes = all` is a **Terraform Core lifecycle feature** — it is not restricted to any category of resource type. It is available on ANY resource block, regardless of provider or resource type: compute, networking, storage, database, IAM, DNS, Kubernetes objects, etc. The `lifecycle` block and all its arguments (`create_before_destroy`, `prevent_destroy`, `ignore_changes`, `replace_triggered_by`) are meta-arguments provided by Terraform Core, not by individual providers. Option A is true — with `ignore_changes = all`, Terraform treats that resource as permanently in sync and proposes zero changes for it on every plan. Option B is true — `all` is the wildcard form that replaces listing individual attributes. Option D is true — this is the intended use case for `ignore_changes = all`, such as resources managed by an external scheduler or config management tool. | ** `ignore_changes = all` — which statement is FALSE? | ** Easy |
| 42 | A, C | ** **(A)** is TRUE. `for_each` only accepts `set(string)` or `map` — NOT a raw `list(string)`. Lists are ordered and allow duplicates, which would create ambiguous resource addresses. To use a list with `for_each`, you must wrap it in `toset()`: `for_each = toset(var.subnet_names)`. `toset()` deduplicates elements and converts them to a set. **(C)** is TRUE. Inside a `for_each` resource block, `each.key` is the current key. For a `map`, `each.key` is the map key and `each.value` is the corresponding value. For a `set(string)`, each element serves as its own key — so `each.key` and `each.value` are identical (both equal the element string). **(B)** is FALSE — lists are not directly accepted by `for_each`. **(D)** is FALSE — `for_each` and `count` are mutually exclusive meta-arguments; using both on the same resource block causes an error. | ** Which TWO statements about `for_each` are TRUE? | ** Easy |
| 43 | B | ** `replace_triggered_by` is a lifecycle argument that causes the resource to be REPLACED (destroy + recreate, shown as `-/+` in the plan) when any of the listed resources or attributes change — even when the resource's own declared attributes have not changed at all. The canonical use case is an Auto Scaling Group (ASG) that references a Launch Template: if the launch template is updated, the ASG's own HCL configuration may not change (it still references the same `aws_launch_template.web` resource), but you want the ASG to cycle its instances using the new template. By adding `replace_triggered_by = [aws_launch_template.web]` to the ASG's lifecycle block, Terraform detects any change to the launch template and plans an ASG replacement. Option A is false — `replace_triggered_by` triggers replacement, while `depends_on` only orders operations. Option C is false — cross-module references are supported. Option D is false — `replace_triggered_by` and `ignore_changes` are independent mechanisms with unrelated semantics. | ** `replace_triggered_by` lifecycle argument — which statement is TRUE? | ** Medium |
| 44 | C | ** Option C is FALSE. `terraform state rm` is NOT deprecated — it remains a fully supported, actively maintained CLI command for removing resource entries from state. The `removed` block and `terraform state rm` are complementary tools, not competing replacements. The `removed` block is a declarative, version-controlled approach (express the intent in HCL, apply through the normal workflow, record the change in Git) while `terraform state rm` is an imperative, ad-hoc approach (run a CLI command directly). Both are valid. Option A is true — the `removed` block's purpose is to detach Terraform management from a resource. Option B is true — `lifecycle { destroy = false }` inside `removed` is the syntax that keeps the cloud resource alive while removing it from state. Option D is true — the `removed` block achieves state removal through the plan/apply workflow with full audit trail. | ** `removed` block — which statement is FALSE? | ** Medium |
| 45 | C | ** Every edge added to Terraform's Directed Acyclic Graph (DAG) is a serialisation constraint: resource B cannot start until all resources that B depends on (directly or transitively) have finished. `depends_on` adds explicit edges that Terraform cannot derive from attribute references alone. These additional edges are necessary for correctness in cases like IAM propagation, but they come at a cost: the dependent resource must wait for all listed resources to complete before it can start, even if those resources could otherwise have overlapped in time. This is why the Terraform documentation specifically advises using `depends_on` sparingly — every unnecessary `depends_on` reduces the concurrency Terraform can achieve, making large applies slower. Option A is false — Terraform absolutely respects dependency edges when scheduling. Option B inverts the truth. Option D is false — `depends_on` affects both apply and destroy ordering. | ** `depends_on` and parallelism — which statement is TRUE? | ** Medium |
| 46 | B | ** Option B is FALSE. HashiCorp explicitly discourages using `-target` as a regular workflow practice. The warning message Terraform prints when `-target` is used states: "WARNING: Resource targeting is in effect... The -target option is not for routine use." The risks include: state drift (other resources are not updated, leaving the configuration and state out of sync), incomplete plans (resource dependencies that were skipped may produce unexpected results on the next full apply), and a false sense of safety (assuming the skipped resources are unaffected when they may actually need changes). `-target` is a break-glass tool for specific scenarios — such as bringing up a single resource for initial testing or recovering from a partial apply failure — not a routine update mechanism. Options A, C, and D are all accurate statements about `-target` behaviour and its documented risks. | ** `terraform apply -target` — which statement is FALSE? | ** Medium |
| 47 | C | ** Terraform resource addresses follow a predictable format. Within the root module, the address is simply `<TYPE>.<LOCAL_NAME>` — e.g., `aws_instance.web`. There is no `module.root.` prefix for root module resources. In `terraform state` commands, plan output, error messages, and `moved` blocks, root module resources are referenced without any module prefix. Resources inside a child module named `compute` are addressed as `module.compute.<TYPE>.<LOCAL_NAME>` — e.g., `module.compute.aws_instance.web`. If the child module is instantiated with `count` or `for_each`, the address includes the index: `module.compute[0].aws_instance.web` or `module.compute["prod"].aws_instance.web`. Option A is false — root module resources have no `module.root.` prefix. Option B is false — the provider namespace is not included in resource addresses. Option D is false — provider names are not part of resource addresses. | ** Resource address format — which statement is TRUE? | ** Medium |
| 48 | B | ** This is a nuanced but important exam topic. If a data source's filter argument references a resource attribute that cannot be determined until that resource is actually created (a "computed" value), Terraform cannot read the data source during the planning phase because the input doesn't exist yet. Instead, Terraform defers the data source read to the apply phase. In the plan output, both the data source result and any resources that depend on the data source result appear as `(known after apply)`. After the dependency resource is created during apply, Terraform reads the data source using the now-known input value, then uses the result for any downstream resources in the same apply run. Option A is false — Terraform handles this case gracefully rather than failing validation. Option C is false — Terraform does not substitute stale state values; it marks things as unknown and resolves them during apply. Option D is false — data sources with unknown inputs are explicitly NOT read during the plan phase. | ** Data source with computed inputs — which statement is TRUE? | ** Medium |
| 49 | A, C | ** **(A)** is TRUE. The `moved` block is ephemeral in nature — once Terraform applies the state rename, the block has done its job. It is safe (and encouraged) to remove it from configuration afterwards. The resource is now tracked at its new address, and future plans will use the new address directly without needing the `moved` block. **(C)** is TRUE. `moved` blocks support cross-module relocations: `from = aws_instance.web` (root module) and `to = module.compute.aws_instance.server` (child module) is valid syntax. Terraform updates the state address to reflect the new module path without any API calls to the cloud resource. **(B)** is FALSE. If you remove a `moved` block before applying it, the situation is not permanent — the old state entry still exists. You can re-add the `moved` block, use `terraform state mv` as an alternative, or re-introduce the old resource name in HCL. Terraform does not permanently lock state addresses. **(D)** is FALSE — `moved` blocks are processed during normal `terraform plan` and `terraform apply`; `terraform init -upgrade` is unrelated to state operations. | ** Which TWO statements about the `moved` block are TRUE? | ** Medium |
| 50 | B | ** Option B is FALSE. There is NO `-force-destroy` flag on `terraform destroy` (or any other runtime flag) that bypasses `prevent_destroy = true`. This is a deliberate design decision, not an oversight: `prevent_destroy` is meant to be a code-level guard that forces a deliberate code review and commit before anything can be destroyed. If `-force-destroy` existed, the protection would be trivially defeated by any engineer with CLI access. The ONLY way to destroy a `prevent_destroy`-protected resource is to edit the `.tf` file to remove or disable `prevent_destroy = true`, commit the change, and then run apply or destroy. Options A, C, and D are all accurate: the error is raised at plan time (not apply time), the configuration change is the only override, and this behaviour is by design. | ** `prevent_destroy` scope — which statement is FALSE? | ** Medium |
| 51 | C | ** Option C is the ONLY TRUE statement. `replace_triggered_by` accepts resource references (e.g., `aws_launch_template.web`) or specific attribute references (e.g., `aws_launch_template.web.image_id`). When any listed resource or attribute changes on an apply, Terraform marks the resource for replacement in the plan (shown with `-/+`), regardless of whether the resource's own configuration attributes changed. Additionally, `replace_triggered_by` only evaluates for changes — it does not trigger on the INITIAL creation of a resource (there is nothing to "change from" on the first apply). Option A is FALSE — `create_before_destroy` and `prevent_destroy` can absolutely coexist in the same `lifecycle` block; `create_before_destroy` controls the ORDER of replacement, while `prevent_destroy` blocks replacement from being planned at all; they can coexist because they address different scenarios. Option B is FALSE — `ignore_changes` only affects DRIFT DETECTION on existing managed resources; it does not affect the initial creation of a resource. If a resource doesn't exist yet, Terraform creates it normally regardless of `ignore_changes`. Option D is FALSE — all four lifecycle arguments are independent and can be combined freely in a single `lifecycle` block. | ** Four statements about lifecycle meta-arguments — only ONE is TRUE | ** Hard |
| 52 | A, C | ** **(A)** is TRUE. The "acyclic" in DAG is a correctness requirement: Terraform cannot execute a plan if the dependency graph contains a cycle (A depends on B, B depends on A — who gets created first?). Terraform detects cycles during graph construction and immediately returns an error like `Cycle: aws_instance.web, aws_security_group.web_sg` before any plan or apply operation. Engineers must resolve cycles by redesigning the dependency structure. **(C)** is TRUE. Terraform's destroy ordering is the exact topological reverse of create ordering. This guarantees referential integrity during teardown — you can never have a situation where Terraform destroys a VPC while subnets that reference it still exist, because the subnets (being more dependent) are always destroyed first. **(B)** is FALSE — resources without dependencies between them are executed IN PARALLEL (up to the `-parallelism` limit, default 10), not sequentially. Sequential execution of independent resources would dramatically slow down large environments. **(D)** is FALSE. Adding a redundant `depends_on` that duplicates an existing implicit dependency IS NOT fully harmless. While it doesn't change correctness (the edge already exists), it CAN reduce parallelism in some cases: `depends_on` on a resource propagates to ALL resources that depend on the dependent resource, potentially creating broader serialisation than the original attribute reference alone. Terraform documentation notes this propagation effect as a reason to use `depends_on` sparingly. | ** Which TWO statements about Terraform's dependency graph (DAG) are TRUE? | ** Hard |
| 53 | B | ** Terraform's `for` expression supports an optional `if` filter clause that is written AFTER the transformation expression: `[for n in var.names : upper(n) if length(n) > 3]`. Only elements where the `if` condition evaluates to `true` are included in the result — elements where it evaluates to `false` are dropped. In the example, any name with three characters or fewer is excluded from the output list. This inline filtering is cleaner and more readable than post-processing with `compact()` or a second expression. The filter condition can be any boolean HCL expression — `contains()`, type checks, comparisons, function calls, etc. Option A is false — the syntax is valid. Option C is false — the `if` clause comes AFTER the `:` transformation, not before. Option D is false — any boolean expression is permitted. | ** `for` expression `if` filter clause — which statement is TRUE? | ** Easy |
| 54 | C | ** Option C is FALSE. `compact()` is narrowly scoped: it removes only `null` values and empty strings (`""`) from a `list(string)`. It does NOT remove all "falsy" values — `false`, `0`, `"0"`, or `[]` are NOT removed. `compact()` is strictly typed for string lists; passing a `list(number)` with zero values will NOT remove those zeroes, and attempting to pass a `list(number)` may cause a type error. Options A and B are accurate descriptions of `compact()`'s behaviour. Option D describes the most common real-world use case — building conditional lists where some values may be `null` (e.g., `compact([var.optional_sg_id, aws_security_group.web.id])`) — and is also true. | ** `compact()` function scope — which statement is FALSE? | ** Easy |
| 55 | A, C | ** **(A)** is TRUE. By default, the iterator variable inside a `dynamic` block takes the same name as the block type being generated. For `dynamic "ingress"`, the iterator is `ingress` — so within the `content` block you reference `ingress.value.from_port`, `ingress.value.to_port`, etc. This is different from resource-level `for_each`, which always uses `each`. **(C)** is TRUE. The optional `iterator` argument within the `dynamic` block overrides this default name. This is useful when the block type name is long, ambiguous, or conflicts with another variable — `iterator = rule` gives you `rule.value` and `rule.key` instead of the default block-type name. **(B)** is FALSE — the iterator is NOT always `each`; it defaults to the block type name. **(D)** is FALSE — `dynamic` blocks support both `list` and `map` collections as the `for_each` value, and when iterating over a `map`, `iterator.key` holds the map key. | ** `dynamic` block iterator naming — which TWO statements are TRUE? | ** Easy |
| 56 | B | ** The fundamental distinction between `object` and `map` in Terraform's type system: a **`map`** is a homogeneous collection — every value must be the same declared type (e.g., `map(string)` means every value is a `string`). The keys are strings but are dynamic — you can have any number of key-value pairs. An **`object`** is a heterogeneous collection with a fixed set of named attributes — each attribute can have its own independent type. `object({ name = string, port = number, enabled = bool })` is valid because each attribute has a different type. This makes `object` the right choice when a variable bundles configuration fields of mixed types. Option A is false — they are structurally different and not automatically interchangeable. Option C is false — `object` attribute names ARE enforced; the object type validator checks that the supplied value has exactly the declared attributes (or a superset, depending on context). Option D is false — this is not a relevant or accurate description of Terraform's internal implementation. | ** `object` type vs `map` type — which statement is TRUE? | ** Medium |
| 57 | B | ** `element()` uses modulo arithmetic when the index equals or exceeds the length of the list: `element(list, index)` returns `list[index % length(list)]`. For a three-element list, `element(["a","b","c"], 4)` computes `4 % 3 = 1`, returning `"b"`. `element(["a","b","c"], 6)` computes `6 % 3 = 0`, returning `"a"`. This makes `element()` ideal for distributing resources across a fixed set of values in a round-robin pattern — for example, distributing EC2 instances across availability zones: `element(var.availability_zones, count.index)` cycles through the list as `count.index` increments. Direct list indexing (`list[index]`) does NOT wrap — it errors if the index is out of range. Option A incorrectly claims `element()` errors on out-of-range indexes. Option C incorrectly describes the wrapping as "returns last element." Option D is false — `element()` accepts any integer expression. | ** `element()` index wrapping — which statement is TRUE? | ** Medium |
| 58 | C | ** Option C is FALSE. `templatefile()` does NOT automatically have access to the calling module's variables, locals, or resource attributes. The ONLY values available inside a template file are those explicitly passed in the `vars` map argument. If you want `${app_name}` in the template to resolve, you must pass `templatefile("user_data.sh.tpl", { app_name = local.app_name })`. The `vars` map is NOT optional — if the template references a variable that is not in the map, Terraform throws an error at evaluation time. This explicit-passing design keeps template files self-contained and testable independently of module scope. Options A, B, and D are all accurate: `file()` reads raw content without rendering, `templatefile()` performs substitution using the explicitly passed map, and EC2 `user_data` generation is the canonical use case. | ** `templatefile()` vs `file()` — which statement is FALSE? | ** Medium |
| 59 | B | ** `try()` evaluates its arguments left to right and returns the value of the FIRST expression that succeeds (evaluates without error). As soon as one expression succeeds, evaluation stops — remaining arguments are not evaluated. Common uses: `try(var.settings["optional_key"], "default_value")` — if the map key lookup errors (key not found), `try()` falls through to the `"default_value"` string. `try(tonumber(var.port), 8080)` — if `tonumber()` fails (e.g., the port is not a valid number string), the fallback `8080` is used. If ALL expressions error, Terraform raises a configuration error — `try()` is not a universal error suppressor. Option A is false — `try()` stops at the first success, not the last. Option C confuses `try()` with a boolean operator — it is strictly for error handling in expression evaluation. Option D is false — `try()` works with any expression type. | ** `try()` function — which statement is TRUE? | ** Medium |
| 60 | B | ** `cidrsubnet(prefix, newbits, netnum)` works as follows: `newbits` is the number of ADDITIONAL bits to borrow from the host portion of the base prefix, increasing the prefix length. `cidrsubnet("10.0.0.0/16", 8, 0)` creates subnets at `/24` (16 + 8 = 24). The `netnum` argument selects WHICH subnet to return — it is the value of the newly borrowed bits. For `/16` + 8 bits: `netnum = 0` → `10.0.0.0/24`; `netnum = 1` → `10.0.1.0/24`; `netnum = 2` → `10.0.2.0/24`, and so on up to `netnum = 255`. This makes `cidrsubnet()` highly useful in `for` expressions or `count`/`for_each` loops to programmatically generate subnets: `cidrsubnet("10.0.0.0/16", 8, count.index)`. Option A confuses `newbits` with the final prefix length. Option C incorrectly describes `netnum` as a host offset — it is a NETWORK offset, not a host offset. Option D is false — `cidrsubnet()` works on any prefix length. | ** `cidrsubnet()` parameters — which statement is TRUE? | ** Medium |
| 61 | C | ** Option C is FALSE. `depends_on` on an output is NOT required for outputs that reference resource attributes. Terraform automatically tracks the dependency between an output value and the resources whose attributes the output references — this is standard implicit dependency detection. If `output "instance_ip" { value = aws_instance.web.public_ip }` references `aws_instance.web.public_ip`, Terraform already knows the output depends on that resource and will not make the output available until the resource is applied. `depends_on` on an output is only needed in the unusual case where the output has an INDIRECT dependency that Terraform cannot detect through attribute references — the scenario in option B. Options A, B, and D are all accurate: outputs do support `depends_on`, the use case is indirect/side-effect dependencies, and the constraint propagates through module outputs to parent modules. | ** Output block `depends_on` — which statement is FALSE? | ** Medium |
| 62 | B, D | ** **(B)** is TRUE. For a resource that uses `count`, `resource_type.name[*].attribute` and `[for r in resource_type.name : r.attribute]` are semantically equivalent — both produce a list of the attribute value from every instance. The splat `[*]` is syntactic sugar for the `for` expression and is more concise in outputs and variable arguments where you simply want all values as a list. **(D)** is TRUE. When a splat is applied to a single (non-count, non-for_each) resource, it produces a LIST with one element, not a scalar. `aws_instance.web[*].id` returns `["i-0abc123"]`. This wrapping behaviour is why you sometimes see `one(aws_instance.web[*].id)` — the `one()` function unwraps a single-element list to its scalar value. **(A)** is FALSE — for `for_each` resources, you use a different form of splat or a `for` expression; the `[*]` splat applies specifically to `count`-based or single resources. **(C)** is FALSE — splat expressions are NOT deprecated; they remain a fully supported and commonly used shorthand in Terraform. | ** Splat expressions `[*]` — which TWO statements are TRUE? | ** Medium |
| 63 | C | ** Option C is FALSE. `jsonencode()` and `jsondecode()` are NOT perfectly lossless inverses for all Terraform types. Specifically, Terraform's type system includes distinctions that JSON does not preserve. For example: a Terraform `set` and a `list` both encode to a JSON array — `jsondecode()` always returns a Terraform `tuple` or `list`, never a `set`. Similarly, Terraform `object` and `map` types both encode to JSON objects — `jsondecode()` returns a `map(any)`, losing any `object` attribute type information. Numeric precision can also differ. So `jsondecode(jsonencode(value))` does NOT necessarily return a value of the same TYPE as the original — the VALUES may be preserved but the type information is not always round-tripped cleanly. Options A, B, and D are accurate: `jsonencode()` converts any Terraform value to a JSON string, `jsondecode()` parses JSON to Terraform values, and IAM policy generation is the canonical use case. | ** `jsonencode()` and `jsondecode()` — which statement is FALSE? | ** Medium |
| 64 | B | ** Option B is the ONLY TRUE statement. For `for_each` over a `map`, `each.key` = map key, `each.value` = map value. For `for_each` over a `set(string)`, because a set has no separate keys — each element IS its own identifier — `each.key` and `each.value` are identical and both equal the element string itself. Option A is FALSE — `for_each` does NOT renumber remaining instances when an element is removed. This is precisely `for_each`'s KEY ADVANTAGE over `count`. When an element is removed from a `for_each` collection, only the resource instance for THAT specific key is destroyed; all other instances retain their addresses unchanged. With `count`, removing an element from the middle of a list does shift the indexes of subsequent instances, potentially causing unwanted destroy-and-recreate cycles. Option C is FALSE — `for_each` does NOT accept a `list(string)` directly; using a plain list causes an error because lists can contain duplicates (which would create ambiguous resource addresses). `toset()` is REQUIRED for list inputs. Option D is FALSE — `for_each` instances are addressed by their STRING KEY, not by integer index: `aws_iam_user.users["alice"]`, `aws_iam_user.users["bob"]`, etc. This string-key addressing works in `terraform state` commands and `-target` flags. | ** Four statements about `for_each` on resources — only ONE is TRUE | ** Hard |
| 65 | B, D | ** **(B)** is TRUE. Terraform's boolean-to-string and string-to-boolean conversions are well-defined. `tostring(true)` → `"true"`, `tostring(false)` → `"false"`. `tobool("true")` → `true`, `tobool("false")` → `false`. The round-trip is lossless for the canonical lowercase representations. Note: `tobool("1")` also returns `true` and `tobool("0")` returns `false` — Terraform accepts these as valid boolean string inputs. **(D)** is TRUE. `toset()` deduplicates — it discards any repeated elements and the result is a set, which is unordered. `toset(["a","b","a","c"])` = `{"a","b","c"}` (three elements). This is exactly why `toset()` is required before passing a list to `for_each` — the list might have duplicates, and `for_each` requires unique keys. **(A)** is FALSE. Type conversion functions DO raise errors on invalid input. `tonumber("abc")` returns an error, not `0`. This is where `try(tonumber(s), default_value)` is useful — to provide a fallback when the conversion might fail. **(C)** is FALSE. The `any` type constraint does NOT mean Terraform infers a fixed type on first use and then enforces it. It means Terraform performs NO type checking on the variable's value — any type is accepted, and Terraform uses the type of the supplied value as-is throughout the configuration. There is no "infer on first use" mechanism. | ** Which TWO statements about type constraints and type conversion functions are TRUE? | ** Hard |
| 66 | B | ** Terraform allows any number of `validation` blocks on a single variable declaration. Each block is evaluated independently — having separate blocks is functionally equivalent to combining conditions with `&&`, but produces clearer, more targeted error messages. For example, a `number` variable might have one validation block checking `var.count >= 1` and a separate block checking `var.count <= 10`, each with its own descriptive `error_message`. When multiple conditions fail, Terraform reports each failing block's `error_message`. Option A is a common misconception — it describes the single-block approach but incorrectly states it is the only approach. Options C and D describe non-existent restrictions that do not apply to Terraform's type system or validation evaluation. | ** Multiple `validation` blocks per variable — which statement is TRUE? | ** Easy |
| 67 | B | ** Option B is FALSE. `self` is NOT valid inside a `precondition` block. `self` is defined only in `postcondition` blocks, where it references the resource's attributes as they exist AFTER the resource change has been applied. A `precondition` runs BEFORE the resource is touched — there is no new state yet, and therefore `self` has nothing to reference. Using `self` in a `precondition` causes a Terraform evaluation error. For `precondition` assertions, you must reference other already-known values: other resource attributes, data source outputs, input variables, or locals. Options A, C, and D are all accurate: `self` in postcondition = post-change attributes; `self` in precondition = undefined; preconditions must reference external data. | ** `self` keyword in `precondition` — which statement is FALSE? | ** Easy |
| 68 | B, C | ** **(B)** is TRUE. Sensitivity propagates through module composition. When a child module output is marked `sensitive = true`, any reference to that output in a parent module is automatically treated as sensitive — the parent does not need to declare it sensitive again. This prevents sensitive data from accidentally appearing in parent module plan output or logs. **(C)** is TRUE. `sensitive = true` on an output suppresses the value in terminal output — `terraform apply` shows `(sensitive value)` for those outputs, and `terraform output` (all outputs) likewise redacts them. **(A)** is FALSE — this is a critical exam fact: `sensitive = true` does NOT encrypt or protect the value in `terraform.tfstate`. The value is still stored in plaintext JSON in state. Protecting state files requires encrypted remote backends and access controls. **(D)** is FALSE — sensitive output values ARE accessible in plaintext via `terraform output <name>` (querying a specific output by name), `terraform output -json`, and `terraform output -raw <name>`. The sensitive flag is a display control, not an access restriction. | ** `sensitive = true` on output blocks — which TWO statements are TRUE? | ** Easy |
| 69 | B | ** The `data` source declared inside a `check` block is scoped to that check and behaves differently from a top-level `data` source in two important ways. First, it cannot be referenced from outside the `check` block — `data.http.endpoint.status_code` is only visible within that check's `assert` conditions. Second, because check-scoped data sources are outside the main resource dependency graph, errors during their evaluation (such as a network timeout or API failure) do not fail the `terraform apply` — they contribute to the non-blocking warning behaviour of the `check` block. This design isolates health-check data fetches from the main configuration graph, preventing transient monitoring failures from blocking deployments. Option A is false — scoped data sources are NOT added to the main graph and CANNOT be referenced externally. Option C is false — `check` blocks run on BOTH `plan` and `apply`. Option D is false — any provider's data source can be used; `http` is simply the most common example. | ** `check` block scoped `data` source — which statement is TRUE? | ** Medium |
| 70 | C | ** Terraform enforces explicit acknowledgement of sensitive values in outputs. If an output's `value` expression directly or indirectly references a value marked `sensitive = true` (whether from a variable, another output, or a resource attribute that Terraform treats as sensitive), and the output block does not set `sensitive = true`, Terraform raises a plan-time error: something like `"Output refers to Terraform-sensitive values"`. The engineer must explicitly add `sensitive = true` to the output to confirm they understand the value is sensitive and will be redacted in terminal output. This design prevents accidental exposure — Terraform will not silently output a sensitive value in plaintext, nor will it silently suppress it. Option A is false — while sensitivity does propagate in some downstream contexts, Terraform still requires explicit `sensitive = true` on the output block itself. Option B is false — there is no "warning and continue" behaviour for this case. Option D is false — Terraform errors rather than silently omitting. | ** Outputting a sensitive variable without marking the output sensitive — which statement is TRUE? | ** Medium |
| 71 | C | ** Both `precondition` and `postcondition` blocks are valid inside `data` source `lifecycle` blocks, not just `resource` blocks. This is an important and sometimes overlooked feature. A typical use case: a data source that looks up an AMI by filter might return any AMI that matches — a `postcondition` on the data source can assert that the fetched result meets specific requirements (e.g., `self.architecture == "x86_64"`, `self.state == "available"`, `self.root_device_type == "ebs"`). This catches data quality issues before the value is used by resource blocks, surfacing a clear error message rather than a cryptic downstream failure. Using `self` in a data source `postcondition` references the data source's fetched attributes, just as `self` in a resource `postcondition` references the resource's attributes. Option A is false — data sources DO support lifecycle conditions. Option B is false — both `precondition` and `postcondition` are valid on data sources. Option D is false — lifecycle conditions run during plan and apply, not init. | ** `precondition` and `postcondition` on data sources — which statement is TRUE? | ** Medium |
| 72 | C | ** Option C is FALSE. A failing `check` block assertion does NOT cause `terraform apply` to exit with a non-zero exit code. The apply exits `0` (success) regardless of check assertion results — check failures are purely informational warnings and do not affect the exit code. This is a fundamental design principle: `check` blocks are for non-blocking health monitoring, not deployment gates. Options A and B correctly describe the consequence of this behaviour: exit `0` means CI/CD pipelines that gate on exit code alone will NOT detect check failures; additional output parsing or tooling is needed if check failures should trigger pipeline alerts. Option D correctly identifies the intended use case for `check` blocks — health observability without blocking risk. | ** `check` block exit code on assertion failure — which statement is FALSE? | ** Medium |
| 73 | B, C | ** **(B)** is TRUE. `check` blocks run on every `terraform plan` AND every `terraform apply`. They are not limited to apply-time execution — this means every plan run also evaluates the health assertions, giving operators continuous infrastructure health feedback even in runs that compute no changes. **(C)** is TRUE. Each `check` block supports only ONE `assert` block. To check multiple independent conditions, declare multiple `check` blocks — each with its own `assert` and optionally its own scoped `data` source. **(A)** is FALSE. The `data` source block inside a `check` block is optional. A `check` block can contain just one or more `assert` blocks without any scoped `data` source — the `assert` can reference any already-available values in the configuration. **(D)** is FALSE. The `data` source inside a `check` block is scoped exclusively to that block and CANNOT be referenced by resource blocks or other configuration elements outside the `check`. This is a deliberate design choice to keep health-check data fetches isolated from the main dependency graph. | ** `check` block — which TWO statements are TRUE? | ** Medium |
| 74 | C | ** The `error_message` in condition blocks is a standard HCL string expression — it is NOT restricted to static literals. Interpolation is fully supported, which allows the message to include the actual invalid value for clarity. In a `validation` block, the message can reference `var.<variable_name>`: `error_message = "Expected one of [dev, staging, production], got: ${var.environment}."`. In a `postcondition`, the message can reference `self.<attribute>`: `error_message = "Instance has no public IP — got: ${self.public_ip}."`. Informative error messages that include the offending value are considered best practice because they reduce debugging time. The ONLY restriction is what the `condition` expression can reference (e.g., `validation` conditions can only reference `var.<name>`), not what `error_message` can reference. Option A incorrectly applies the `condition` reference restriction to `error_message`. Option B is false — `error_message` is required, not optional. Option D incorrectly splits interpolation availability across block types. | ** `error_message` in condition blocks — which statement is TRUE? | ** Medium |
| 75 | D | ** Option D is FALSE. Terraform does NOT perform automatic transactional rollback when a `precondition` (or any other condition) fails mid-apply. Terraform's apply is not atomic — it applies resources in dependency order, and a failure mid-apply leaves the infrastructure in a partially-applied state. Resources that were successfully applied before the failure remain in their new state; the failing resource and any that depend on it are not applied. This partial-state behaviour is by design and is clearly documented — Terraform is not a database transaction system. To resolve a partial apply, operators must investigate the failure, fix the configuration, and run `terraform apply` again (Terraform will only attempt to apply the remaining un-applied resources). Options A, B, and C are all accurate: the failing resource is not touched, completed resources are not rolled back, and the exit code is non-zero. | ** `precondition` failing mid-apply — which statement is FALSE? | ** Medium |
| 76 | C | ** **(C)** is the ONLY TRUE statement. `check` block `assert` conditions can reference any value that is available in the configuration — resource attributes, data source outputs, locals, variables, and the outputs of the check block's own scoped `data` source. Unlike `validation` conditions (restricted to `var.<name>` because they run before planning), `check` assertions run AFTER all resource operations complete, when all resource attributes are known. This full access is what makes `check` suitable for cross-cutting health assertions that reference multiple resources. **(A)** is FALSE — a failing `postcondition` does NOT automatically taint the resource. Terraform marks the apply as failed (non-zero exit) but does NOT add a taint to the resource in state. The resource exists in its current state; no automatic marking for replacement occurs. **(B)** is FALSE — `validation` blocks run BEFORE `terraform plan` generates any output; they fire during input variable processing, before planning even begins. The operator never sees a plan if validation fails. **(D)** is FALSE — `precondition` checks DO apply to destroy operations. A `precondition` on a resource is evaluated before ANY change to that resource, including destruction. If a `precondition` condition evaluates to false before a destroy, the destroy is blocked. | ** Four statements about the three condition mechanisms — only ONE is TRUE | ** Hard |
| 77 | A, B | ** **(A)** is TRUE. When a provider marks a resource attribute as sensitive (e.g., `aws_db_instance.password`), Terraform propagates that sensitivity. Any `output` block that directly or indirectly references that attribute must declare `sensitive = true` — otherwise Terraform raises a plan-time error. Similarly, locals that reference sensitive-marked attributes carry the sensitive marking forward in expressions. This enforced propagation prevents accidental exposure. **(B)** is TRUE. The `nonsensitive()` function exists to explicitly unwrap the sensitive marking from a value when the engineer determines it is safe to do so — for example, after hashing a secret with `sha256()`, the hash is not itself a secret, so `nonsensitive(sha256(var.db_password))` produces a non-sensitive string that can be used freely. Using `nonsensitive()` is intentional and requires engineering judgment — Terraform trusts the caller has reviewed the exposure. **(C)** is FALSE — sensitive values are NOT excluded from `terraform.tfstate`. All attribute values, regardless of sensitivity marking, are written to state in plaintext. This is the most critical and commonly tested exam fact about sensitive data in Terraform. **(D)** is partially false. While sensitive values are shown as `(sensitive value)` in most plan output, the behaviour is not absolute for all cases — for example, when a sensitive value changes, Terraform indicates the attribute will change but still redacts the old and new values as `(sensitive value)`. However, the claim "regardless of whether the value is actually changing" is an overstatement — the exact redaction behaviour depends on context and provider implementation. More importantly, option C contains a clear factual error that makes it the definitively false option. | ** Sensitive data handling — which TWO statements are TRUE? | ** Hard |
| 78 | C | ** **(C)** is the ONLY TRUE statement. A `lifecycle` block can contain multiple `precondition` blocks AND multiple `postcondition` blocks — there is no enforced limit. Having multiple conditions allows each assertion to have a distinct, targeted `error_message` that clearly identifies which specific requirement was violated. All declared `precondition` blocks are evaluated before the resource is changed; all declared `postcondition` blocks are evaluated after. If any condition fails, Terraform halts at that point with the failing condition's `error_message`. **(A)** is FALSE — multiple `precondition` and `postcondition` blocks are explicitly supported in the same `lifecycle` block. **(B)** is FALSE — `precondition` and `postcondition` are valid on BOTH `resource` AND `data` source blocks. Data source postconditions are commonly used to validate fetched data before it is consumed by resource blocks. They are NOT valid on `module` or `output` blocks, but the claim that they're restricted to resource blocks is inaccurate. **(D)** is FALSE — there is no `rollback = true` argument on `postcondition` blocks. Such an argument does not exist in Terraform's HCL specification. A failing `postcondition` exits non-zero and leaves the resource in place — there is no automatic rollback mechanism. | ** Four statements about `precondition` + `postcondition` placement and scope — only ONE is TRUE | ** Hard |
| 79 | C | ** Option C is FALSE. `terraform get` performs ONLY the module download step — it does NOT install providers or configure the backend. Its scope is strictly limited to populating `.terraform/modules/` with module source code. Provider installation is handled exclusively by `terraform init`. Option B is TRUE — this is the defining characteristic of `terraform get`. Option A is TRUE for the module portion of `terraform init`'s work. Option D is TRUE — `terraform init` is a superset: it handles backend initialisation, provider installation, and module downloads, while `terraform get` handles only the last part. In practice, `terraform init` is used almost exclusively; `terraform get` is rarely needed standalone. | ** `terraform get` vs `terraform init` for module installation — which statement is FALSE? | ** Easy |
| 80 | B | ** The file names `main.tf`, `variables.tf`, `outputs.tf`, `versions.tf`, and `README.md` are a widely adopted **convention**, not a Terraform requirement. Terraform processes all `.tf` files in a directory as a single logical configuration unit — file names carry no semantic meaning to the Terraform engine. You could put all resources, variables, and outputs in a single `everything.tf` file and it would work identically. The standard names are recommended because they make the module's structure immediately understandable to other engineers and are expected by the Terraform Registry for module documentation. Option A is false — Terraform imposes no file naming rules. Option C is false — Terraform does not use file processing order; all `.tf` files are merged into one configuration graph. Option D is false — `required_providers` can appear in any `.tf` file in the module root. | ** Standard module file naming convention — which statement is TRUE? | ** Easy |
| 81 | B, C | ** **(B)** is TRUE. `for_each` is fully valid on `module` blocks. When a map or set is provided, Terraform creates one module instance per element. Each instance is addressed with the map key as its index: `module.vpc["prod"]` and `module.vpc["dev"]`. Within the module, `each.key` and `each.value` are available for use in resource arguments, just as in `for_each` resources. **(C)** is TRUE. `count` is also valid on `module` blocks. Each instance is numerically indexed: `module.vpc[0]`, `module.vpc[1]`, `module.vpc[2]`. `count.index` is available inside the module for distinguishing instances. **(A)** is FALSE — `count` and `for_each` ARE supported on `module` blocks; this is an officially documented feature. **(D)** is FALSE — there is no restriction on resource types inside a module instantiated with `for_each`; all resource types are permitted. | ** `count` and `for_each` meta-arguments on module blocks — which TWO statements are TRUE? | ** Easy |
| 82 | C | ** `depends_on` is valid on `module` blocks and is the correct mechanism for expressing **hidden dependencies** — ordering requirements that Terraform cannot infer automatically from data flow. For example, if a module provisions EC2 instances but relies on an IAM policy that was created in another resource block without any attribute reference creating a graph edge, `depends_on` can explicitly declare that the module must wait. However, `depends_on` should be used sparingly and only for genuine hidden dependencies — overuse defeats Terraform's ability to parallelise and can mask design problems. Option A is false — `depends_on` IS valid on module blocks. Option B is false — using `depends_on` "routinely" is discouraged; Terraform automatically infers dependencies from output-to-input references, which is always preferred. Option D is false — `depends_on` applies within a single root module configuration and affects resource graph ordering within that module. | ** `depends_on` on a module block — which statement is TRUE? | ** Medium |
| 83 | B | ** Option B is FALSE. The `.terraform.lock.hcl` file tracks **provider** versions and checksums ONLY — it does NOT record module version selections. Module version resolution is handled separately: the version constraint in the `module` block guides `terraform init`, and the resolved version is cached in `.terraform/modules/modules.json` (which is typically NOT committed to version control). There is no module equivalent of the provider lock file. To ensure reproducible module versions, use a tight `version` constraint (e.g., `version = "= 5.1.0"`) or use a Git source with `?ref=` pinned to a specific tag or commit. Option A correctly describes what the lock file does track. Option C correctly explains the module version resolution mechanism. Option D correctly describes the commit-to-VCS recommendation for the lock file. | ** `.terraform.lock.hcl` and module version tracking — which statement is FALSE? | ** Medium |
| 84 | A | ** Module resources are addressed in the Terraform CLI using the dot-separated format `module.<module_name>.<resource_type>.<resource_name>`. For example, `terraform state show module.networking.aws_vpc.main` shows the state entry for the `aws_vpc.main` resource inside the `networking` module. For `for_each` module instances, the address includes the key: `module.vpc["prod"].aws_subnet.main`. This addressing scheme is used consistently across all commands that accept resource addresses: `terraform state list`, `terraform state show`, `terraform state mv`, `terraform destroy -target`, `terraform apply -target`, and `terraform taint`. Option B is false — individual module resources CAN be targeted with `-target` using the full module address. Option C is false — the module name is always part of the address for module-owned resources. Option D is false — colons are not used in Terraform resource addresses. | ** Addressing module resources in Terraform commands — which statement is TRUE? | ** Medium |
| 85 | B | ** By default, Terraform automatically passes the default (non-aliased) provider configurations from the calling module to child modules. No `providers` argument is needed for the common case. The `providers` meta-argument is required only when you want to pass a **different** provider configuration to the child — most commonly a provider alias. A typical use case is a child module that manages resources in a non-default AWS region: `providers = { aws = aws.us-west-2 }` maps the child module's `aws` provider to the parent's aliased `aws.us-west-2` configuration. Option A is false — `providers` is strictly for passing provider configurations, not input variables. Option C is false — provider inheritance is automatic; `providers` is optional. Option D is false — passing the default, non-aliased provider with `providers = { aws = aws }` is valid and sometimes used to be explicit. | ** Module `providers` meta-argument — which statement is TRUE? | ** Medium |
| 86 | B, C | ** **(B)** is TRUE. Registry-sourced modules support version constraints via the `version` argument. Constraint expressions follow the same syntax as provider version constraints: `~>` for compatible versions (pessimistic constraint), range expressions with `>=` and `<`, and exact pins with `=`. The registry resolves the constraint against published module versions and downloads the highest version that satisfies the constraint. **(C)** is TRUE. HCP Terraform and Terraform Enterprise both support private module registries. Private modules use the identical three-part `<NAMESPACE>/<MODULE>/<PROVIDER>` source format and the `version` argument — the only difference is that they are access-controlled and only available to authenticated users of that organisation. **(A)** is partially true but incorrect on the VCS restriction — the Terraform Registry supports GitHub as the primary VCS for module publishing, but GitLab and Bitbucket are also supported for the public registry. **(D)** is FALSE — when no `version` is specified, `terraform init` downloads the **latest** published version, not the oldest. This is why specifying a `version` constraint is recommended for production configurations. | ** Terraform Registry published modules — which TWO statements are TRUE? | ** Medium |
| 87 | B | ** The root module can compose child modules by wiring one module's output directly to another module's input. For example: `module "compute" { source = "./modules/compute"; subnet_id = module.networking.public_subnet_id }` passes the `public_subnet_id` output from the `networking` module as an input to the `compute` module. Terraform's dependency graph automatically infers that `compute` depends on `networking` — because `compute`'s input contains a reference to `networking`'s output, Terraform knows to apply `networking` first and `compute` second. This is the idiomatic way to compose Terraform modules and is strongly preferred over explicit `depends_on` when a genuine data dependency exists. Option A is false — module outputs CAN be passed directly to other module blocks. Option C is false — A → B chaining is not circular; circular would be A → B → A. Option D is false — modules from any source (local, registry, Git) can be composed this way. | ** Passing a child module output as an input to another child module — which statement is TRUE? | ** Medium |
| 88 | B | ** Option B is FALSE. Local path modules have no remote source to download from — they ARE the source (a directory on the local filesystem). `terraform init -upgrade` has no special effect on local path modules because there is nothing to upgrade from a remote location; the files on disk ARE the current version. Running `terraform init` or `terraform init -upgrade` for a local path module simply re-registers the path in `.terraform/modules/modules.json` — no downloading or version comparison occurs. Option A is TRUE — `-upgrade` refreshes Terraform Registry module version resolution and re-downloads if a newer satisfying version is available. Option C is TRUE — `-upgrade` also applies to providers, updating the lock file. Option D is TRUE — this is the intended workflow for deliberately adopting new versions while respecting constraints. | ** `terraform init -upgrade` and module versions — which statement is FALSE? | ** Medium |
| 89 | B | ** **(B)** is the ONLY TRUE statement. For `for_each` module instances, the address uses the element key as the instance index, enclosed in square brackets with quotes for string keys: `module.vpc["prod"]`, `module.vpc["dev"]`. Resources inside those instances use the full address `module.vpc["prod"].aws_subnet.main`. The `-target` flag accepts the quoted key syntax: `-target='module.vpc["prod"]'`. Option A is false — Terraform DOES include the key suffix in addresses; `terraform state list` shows `module.vpc["prod"]` and `module.vpc["dev"]` as separate entries. Option C is false — `for_each` instances use the actual map/set keys as indices (string keys), not numeric indices; numeric indices are used by `count`, not `for_each`. Option D is false — `each.key` and `each.value` ARE available inside the child module's resource blocks when the module is instantiated with `for_each`; this is a key feature that allows child module resources to differentiate between instances. | ** Four statements about module `for_each` instance addressing — only ONE is TRUE | ** Hard |
| 90 | C, D | ** **(C)** is TRUE. `count` and `for_each` are mutually exclusive on both `resource` blocks and `module` blocks. Terraform requires you to choose one or the other — you cannot set both simultaneously. Using both causes a configuration error: "The arguments count and for_each are both defined for this module; only one is allowed." **(D)** is TRUE. The `providers` meta-argument maps provider names as understood by the CHILD module (based on the provider's local name in the child's `required_providers`) to provider configurations in the PARENT. This allows a child module designed to use `aws` to receive a specifically aliased provider (e.g., `aws.us-west-2`) from the parent. **(A)** is FALSE — the `version` argument is valid ONLY for Terraform Registry and private registry sources; it causes an error when used with Git-based sources, where `?ref=` is used instead. **(B)** is FALSE — `count` and `for_each` cannot be combined (see C), and `version` is not valid with non-registry sources. | ** Module meta-arguments — which TWO statements are TRUE? | ** Hard |
| 91 | C | ** **(C)** is the ONLY TRUE statement. Best practice for publishable Terraform modules is to declare `required_providers` in a `versions.tf` file, specifying the providers the module uses along with a minimum version constraint. This serves multiple purposes: it documents the module's dependencies, enables the Terraform Registry to display provider requirements, and ensures that `terraform init` validates provider compatibility when the module is consumed. The root module's `.terraform.lock.hcl` governs the exact provider version installed in the workspace, but the child module's `required_providers` contributes its constraints to the overall resolution. **(A)** is false — child modules do NOT MUST redeclare providers; Terraform inherits provider configurations from the root. Missing `required_providers` in a child is valid (though not best practice). **(B)** is false — Terraform does NOT auto-discover providers from resource type names without declarations; while it can infer provider association from resource type prefixes, explicit `required_providers` is needed for version resolution and source specification. **(D)** is false — child module `required_providers` declarations are NOT ignored; they contribute version constraints to the overall provider resolution and are surfaced in registry documentation. | ** Four statements about how Terraform modules handle provider requirements — only ONE is TRUE | ** Hard |
| 92 | B | ** `terraform.tfstate.backup` is a single-snapshot safety net — not a rolling history. Before every successful `terraform apply`, Terraform copies the current `terraform.tfstate` into `terraform.tfstate.backup`, then overwrites `terraform.tfstate` with the new state. The result is that `terraform.tfstate.backup` always contains the state from the apply *before* the most recent one — exactly one previous snapshot. If you run 10 applies, the backup only reflects apply 9 (the state that existed before apply 10 ran). For full version history, you need either S3 with versioning enabled (every state file write becomes a new S3 object version) or HCP Terraform (which versions all state automatically). Option A is false — there is no append-style history. Option C is false — the backup is created on every apply regardless of the operation type. Option D is false — the backup file lives in the working directory alongside `terraform.tfstate`, not inside `.terraform/`. | ** `terraform.tfstate.backup` — which statement is TRUE? | ** Easy |
| 93 | B | ** The two commands serve complementary purposes: `terraform state list` is a directory-style command — it outputs all resource addresses tracked in state, one per line, with no attribute detail. It accepts an optional pattern for filtering (e.g., `terraform state list module.networking.*`). `terraform state show <address>` is a detail command — it takes a single resource address and prints all of that resource's attribute values as they are recorded in state, formatted as HCL-like output. Together they form a common debugging workflow: use `list` to find what addresses are tracked, then use `show` to inspect a specific resource's values. Option A is false — the commands are distinct. Option C is false — `terraform state list` with no arguments lists ALL resources without filtering. Option D is false — `terraform state show` is a real, well-documented command; `terraform inspect` is not a Terraform command. | ** `terraform state list` vs `terraform state show` — which statement is TRUE? | ** Easy |
| 94 | A, B | ** **(A)** is TRUE. Each HCP Terraform workspace has its own fully isolated state file stored on HCP Terraform's infrastructure — encrypted at rest and in transit — completely independent of all other workspaces. There is no state sharing between workspaces unless explicitly configured via the `terraform_remote_state` data source. **(B)** is TRUE. HCP Terraform automatically maintains a complete version history of every state change for every workspace. Operators can navigate the version history, inspect any prior state version, and initiate a rollback directly from the workspace's States tab in the UI — no manual versioning configuration is required. **(C)** is FALSE. HCP Terraform manages its own state storage infrastructure — organisations do NOT need to provision or manage S3 buckets or any other storage infrastructure for HCP Terraform's state. The S3 backend is an alternative for organisations hosting their own state in AWS. **(D)** is FALSE. Workspaces do NOT share a single state file — full workspace isolation is one of HCP Terraform's core features and a key reason organisations use it for multi-environment management. | ** HCP Terraform state storage — which TWO statements are TRUE? | ** Easy |
| 95 | C | ** Option C is FALSE. `terraform state rm` ONLY modifies the local state file — it has zero effect on cloud infrastructure. The EC2 instance (or any other resource) continues running unaffected in AWS after `terraform state rm` removes it from state. Terraform state operations (`state rm`, `state mv`, `state show`) are strictly state management tools; they never call provider APIs to create, modify, or destroy cloud resources. The second half of option C is accurate (Terraform treats a resource absent from state as new and plans to create it), but the first claim — that `state rm` destroys the cloud resource — is completely false. This distinction is critical: if you want to destroy the cloud resource, use `terraform destroy -target=aws_instance.web`; if you want to stop managing it WITHOUT destroying it, use `terraform state rm`. Options A, B, and D are all TRUE statements about `terraform state rm` behaviour. | ** `terraform state rm` — which statement is FALSE? | ** Medium |
| 96 | C | ** The `terraform_remote_state` data source provides access ONLY to values that have been explicitly declared as `output` blocks in the remote (producing) Terraform configuration. Individual resource attributes — even ones that exist in state — are NOT directly readable. This design is intentional: it creates a well-defined interface contract between configurations. The producing configuration exposes `output "vpc_id" { value = aws_vpc.main.id }`, and the consuming configuration reads `data.terraform_remote_state.networking.outputs.vpc_id`. This access boundary also enforces the principle of least privilege — a consuming configuration cannot accidentally read sensitive attributes from the remote state unless the producer explicitly outputs them. Option A is false — you cannot traverse into resource objects in remote state directly. Option B is false — `terraform_remote_state` works with any backend that supports state storage (S3, Azure Blob, GCS, local, etc.). Option D describes a real HCP Terraform feature (run triggers), but it is not how `terraform_remote_state` itself behaves. | ** `terraform_remote_state` data source — which statement is TRUE? | ** Medium |
| 97 | D | ** Option D is FALSE. VCS-driven and CLI-driven are **mutually exclusive workspace modes** — a workspace is configured as one or the other, not both simultaneously. A VCS-driven workspace has VCS integration enabled; it responds to VCS webhook events and does NOT accept CLI-triggered runs. Conversely, a CLI-driven workspace does not have a VCS connection and only accepts runs initiated from a local `terraform plan`/`terraform apply`. This mutual exclusivity is intentional: mixing CLI and VCS triggers on the same workspace would create unpredictable run ordering and make it impossible to enforce code-review gates. Option A correctly describes VCS-driven workspace behaviour. Option B correctly describes CLI-driven workspace behaviour (remote execution, local CLI trigger). Option C correctly describes API-driven workspaces. | ** HCP Terraform workspace execution modes — which statement is FALSE? | ** Medium |
| 98 | C | ** **(C)** is TRUE. `hard-mandatory` is the most restrictive Sentinel (and OPA) enforcement level — a policy failure at this level permanently blocks the run and the failure cannot be overridden by anyone, including organization owners. This makes it appropriate for strict compliance requirements such as "all S3 buckets must have encryption enabled" or "VPCs must not have public subnets." Option A is false — `advisory` is the least restrictive level; it shows a warning but does NOT block the run; the apply proceeds automatically. Option B is false — `soft-mandatory` can be overridden, but only by users with specific elevated permissions (typically organization owners or users with the Override Policy Checks capability); workspace Write permission is NOT sufficient to override a soft-mandatory failure. Option D is false — enforcement levels are set per-policy (within the policy set configuration), not as a run-level setting; different policies in the same policy set can have different enforcement levels. | ** Sentinel policy enforcement levels — which statement is TRUE? | ** Medium |
| 99 | B | ** **(B)** is TRUE. HCP Terraform supports two distinct policy-as-code frameworks: Sentinel (using HashiCorp's proprietary Sentinel DSL) and OPA (using Rego, the policy language from the Open Policy Agent project). Organizations can adopt either or both — policy sets can contain Sentinel policies, OPA policies, or a mix. All three enforcement levels apply uniformly across both frameworks. Option A is false — OPA IS supported in HCP Terraform (not just Terraform Enterprise). Option C is false — OPA uses **Rego**, not HCL. OPA is a CNCF project developed by Styra (not HashiCorp), and its Rego language is purpose-built for policy evaluation with its own syntax unrelated to HCL. Option D is false — there is no fixed evaluation precedence between Sentinel and OPA policies; the ordering is not defined as Sentinel-first; policies from both frameworks are evaluated as part of the same policy check phase. | ** OPA (Rego) vs Sentinel as policy frameworks — which statement is TRUE? | ** Medium |
| 100 | B | ** HCP Terraform health assessments are a scheduled drift-detection mechanism. Internally, they execute the equivalent of `terraform plan -refresh-only` against the workspace on a configurable interval. The operation queries cloud provider APIs, compares the live resource attributes to what is stored in Terraform state, and identifies any attributes that have changed outside of Terraform (e.g., a security group rule added manually in the console). Results are displayed in the workspace's Health tab in the HCP Terraform UI, and webhook or email notifications can be configured for detected drift. Crucially, health assessments are **read-only** — they NEVER automatically apply corrections. Drift remediation always requires a deliberate human decision to queue and approve a run. Option A is false — there is no auto-apply of corrections. Option C is false — health assessments are a paid tier feature and are not enabled by default; they must be configured. Option D is false — health assessments operate completely independently of Sentinel or OPA policy sets. | ** HCP Terraform health assessments (drift detection) — which statement is TRUE? | ** Medium |
| 101 | A, C | ** **(A)** is TRUE. HCP Terraform defines four workspace permission levels, and each is a superset of the one below: Read → Plan → Write → Admin. Read allows viewing state and run history; Plan adds the ability to trigger speculative (plan-only) runs; Write adds the ability to queue and approve full runs; Admin adds workspace configuration management including variable management, VCS connections, and team access control. **(C)** is TRUE. Team tokens are a first-class HCP Terraform feature for CI/CD. A team token represents the collective access of a team — if the team has Write permission on five workspaces, a CI/CD pipeline authenticating with the team token can trigger runs on all five workspaces. This is the recommended pattern for automated pipelines, avoiding the security risk of using personal user tokens. **(B)** is FALSE — HCP Terraform has a full team-based RBAC model; permissions are assigned to teams, and users are added to teams; individual per-user assignment is also supported but teams are the primary mechanism. **(D)** is FALSE — there are definitely four distinct permission levels, not just Read and Write; Plan and Admin are real, active permission tiers with meaningful capability differences. | ** HCP Terraform workspace RBAC — which TWO statements are TRUE? | ** Medium |
| 102 | B | ** Option B is FALSE. `terraform state mv` ONLY modifies the Terraform state file — it does NOT contact any cloud provider or send any API calls to AWS (or any other provider). The cloud resource (the EC2 instance) is completely unchanged: its AWS instance ID, name, configuration, and running state are all unaffected. `terraform state mv` is purely a state management operation that updates the address under which Terraform tracks a resource. The command is used to fix address mismatches that would otherwise cause Terraform to plan a destroy-and-recreate cycle. After running `state mv`, the resource continues to exist in AWS exactly as before, but Terraform now tracks it under the new address. Option A correctly describes the primary use case. Option C correctly describes the expected outcome of a successful state move. Option D correctly describes a valid module-to-module or root-to-module state move. | ** `terraform state mv` — which statement is FALSE? | ** Medium |
| 103 | B | ** **(B)** is the ONLY TRUE statement. This is one of the most commonly confused topics in the Terraform Associate exam. Terraform OSS workspaces (managed with the `terraform workspace` CLI commands against a standard backend) are simply a mechanism for maintaining **multiple named state files** within the same backend configuration. All workspaces in the set share the exact same `.tf` configuration code and backend; they differ only in which state file is active. There is no variable isolation, no permission model, no run history, and no execution environment separation between OSS workspaces. HCP Terraform workspaces are an entirely different concept — each workspace is a fully isolated operational environment. The shared terminology ("workspace") is a historical naming overlap that causes confusion. Option A is false — OSS workspaces and HCP Terraform workspaces are NOT the same feature; they differ in virtually every dimension except the name. Option C is false — `terraform workspace new staging` on a cloud-block configuration creates a new HCP Terraform workspace (a persistent environment), not a temporary preview; it has nothing to do with auto-discard behaviour. Option D is false — selecting a workspace does NOT automatically trigger a plan; you must explicitly run `terraform plan` after selecting a workspace. | ** Four statements about local Terraform workspaces vs HCP Terraform workspaces — only ONE is TRUE | ** Hard |
| 104 | C | ** **(C)** is the ONLY TRUE statement. Dynamic provider credentials (also called "Workload Identity" in some cloud provider contexts) use the OIDC protocol to replace static long-lived credentials with short-lived, per-run tokens. The mechanism: (1) the cloud provider (AWS, Azure, or GCP) is configured to trust tokens issued by HCP Terraform's OIDC endpoint; (2) when a run starts, HCP Terraform's identity service generates a JWT token (the OIDC token) for that specific workspace and run; (3) HCP Terraform exchanges this token with the cloud provider for a short-lived cloud credential (e.g., temporary AWS credentials via AssumeRoleWithWebIdentity); (4) the run uses these short-lived credentials for provider API calls; they expire when the run ends. The result: no static `AWS_ACCESS_KEY_ID` or Azure client secret stored in workspace variables, and a complete per-run audit trail in the cloud provider's IAM logs. Option A is false — dynamic provider credentials support AWS, Azure, AND GCP. Option B is false — OIDC authentication requires explicit configuration of both the cloud provider's trust policy AND the HCP Terraform workspace settings; it is not enabled automatically. Option D is false — dynamic provider credentials ARE supported in HCP Terraform SaaS; this is a current, documented feature of the HCP Terraform platform. | ** Four statements about dynamic provider credentials (OIDC) in HCP Terraform — only ONE is TRUE | ** Hard |
