# Terraform Associate Exam Questions

---

### Question 1 — CLI Import and HCL Generation

**Difficulty**: Easy
**Answer Type**: one
**Topic**: Whether the CLI `terraform import` command supports the `-generate-config-out` flag

**Question**:
A developer states: "The `terraform import` CLI command supports the `-generate-config-out` flag just like the declarative `import` block — you can run `terraform import -generate-config-out=generated.tf aws_instance.web i-0abc123` to automatically create the HCL resource block for the imported resource."

What is wrong with this claim?

- A) The flag is named `-config-out`, not `-generate-config-out`, for the CLI import command
- B) The `-generate-config-out` flag is exclusive to `terraform plan` when used with a declarative `import` block — the CLI `terraform import` command does not support this flag and never generates HCL
- C) The flag works but requires an existing resource block to be present before it can generate the configuration
- D) The flag is valid but only outputs JSON, not HCL

---

### Question 2 — TF_LOG Default Output Destination

**Difficulty**: Easy
**Answer Type**: one
**Topic**: Where Terraform writes log output when `TF_LOG` is set but `TF_LOG_PATH` is not

**Question**:
An operator says: "If you set `TF_LOG=DEBUG` without setting `TF_LOG_PATH`, Terraform has nowhere to write the logs — logging is effectively disabled. You must set `TF_LOG_PATH=terraform.log` to activate debug output."

What is wrong with this claim?

- A) `TF_LOG=DEBUG` is not a valid log level — the minimum valid level is `INFO`
- B) When `TF_LOG` is set but `TF_LOG_PATH` is not, Terraform writes log output to **stderr** — `TF_LOG_PATH` is optional and only redirects output from stderr to a file
- C) `TF_LOG_PATH` defaults to `terraform.log` in the working directory, so logging is active by default without explicitly setting it
- D) Terraform writes logs to stdout when `TF_LOG_PATH` is absent, which may mix with plan output

---

### Question 3 — Swapped `import` Block Arguments

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Correct use of the `to` and `id` arguments in a declarative `import` block

**Question**:
Read this `import` block:

```hcl
import {
  to = "i-0abcd1234ef567890"
  id = aws_instance.web
}
```

A colleague reviews this and says: "Looks correct — `to` takes the cloud resource identifier and `id` takes the Terraform resource address."

What is wrong with this configuration and the colleague's explanation?

- A) The `import` block requires a `provider` argument in addition to `to` and `id`
- B) The arguments are swapped — `to` must be the Terraform resource address (unquoted, e.g., `aws_instance.web`) and `id` must be the cloud provider's resource identifier (e.g., `"i-0abcd1234ef567890"`)
- C) Both values must be quoted strings — using an unquoted reference for `id` causes a syntax error
- D) The `import` block must be placed inside the `resource "aws_instance" "web"` block, not at the root level

---

### Question 4 — `cloud` Block and `backend` Block Coexistence

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Whether `cloud` and `backend` blocks can be used together in the same `terraform {}` block

**Question**:
A team uses HCP Terraform for production and a local backend for local development. A developer proposes this configuration to support both:

```hcl
terraform {
  cloud {
    organization = "acme-corp"
    workspaces {
      name = "production"
    }
  }

  backend "local" {}
}
```

The developer claims: "This configuration lets Terraform fall back to the local backend when HCP Terraform is unavailable and use the `cloud` block when it is reachable."

What is the error in this configuration and claim?

- A) The `cloud` block and `backend` block are mutually exclusive within a single `terraform {}` block — Terraform raises a configuration error if both are declared simultaneously
- B) The `backend "local"` block overrides the `cloud` block because backend declarations always take precedence
- C) The `cloud` block overrides `backend "local"` silently, making the `backend` block unreachable but not an error
- D) This is valid Terraform syntax; the blocks serve different lifecycle phases and do not conflict

---

### Question 5 — Sentinel Enforcement Level Descriptions

**Difficulty**: Medium
**Answer Type**: many
**Topic**: Distinguishing `advisory`, `soft-mandatory`, and `hard-mandatory` enforcement level behaviour

**Question**:
A team lead explains Sentinel policy enforcement levels to new engineers. Which TWO of the following statements contain an error? (Select two.)

- A) The `advisory` enforcement level logs a warning when a policy fails but allows the run to continue — it does not block the apply
- B) The `advisory` enforcement level blocks the apply when a policy fails — it is less strict than `soft-mandatory` only because the failure is displayed as a warning rather than a hard stop
- C) There is no mechanism to override a `soft-mandatory` policy failure — once blocked, the only resolution is to fix the configuration or remove the policy
- D) The `hard-mandatory` enforcement level blocks the run and provides no override mechanism — not even organisation Owners can bypass a `hard-mandatory` failure

---

### Question 6 — Health Assessment Auto-Apply Claim

**Difficulty**: Medium
**Answer Type**: one
**Topic**: What HCP Terraform health assessments do when they detect drift, and what they cannot do

**Question**:
A platform engineer describes HCP Terraform health assessments: "When a health assessment detects that cloud resources have drifted from the configuration — for example, an EC2 instance type was manually changed in the AWS Console — HCP Terraform automatically queues a `terraform apply -refresh-only` run to pull the drift into state, keeping your state file accurate without any manual intervention."

What is the error in this description?

- A) Health assessments run `terraform apply` (not `-refresh-only`) to restore the resource to the configuration-defined state
- B) Health assessments run `terraform plan -refresh-only` — they are read-only drift detection operations and **never automatically queue or execute any apply**, even a `-refresh-only` apply
- C) Health assessments do not detect instance type changes — they only detect resource deletions
- D) Health assessments are triggered manually, not on a schedule

---

### Question 7 — Speculative Plan Approval Claim

**Difficulty**: Medium
**Answer Type**: one
**Topic**: The lifecycle limitations of speculative plans in HCP Terraform

**Question**:
A developer explains HCP Terraform run types: "A speculative plan is like a standard plan but with lower risk — it runs through the planning phase and shows what changes would occur. If the speculative plan shows **no infrastructure changes** (i.e., no resources will be created, modified, or destroyed), a workspace Admin can approve it to proceed to apply, since there is nothing harmful to execute."

What is the error in this statement?

- A) Speculative plans cannot be approved for apply under any circumstance — they are strictly informational and the run lifecycle ends at the plan stage regardless of the plan output
- B) Only organisation Owners (not workspace Admins) can approve a speculative plan that shows no changes
- C) Speculative plans that show no changes are automatically applied by HCP Terraform without requiring approval
- D) Speculative plans can only be triggered via the HCP Terraform UI, not via VCS pull request webhooks

---

### Question 8 — `terraform login` Token Storage Location

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Where `terraform login` stores the HCP Terraform API token on disk

**Question**:
A DevOps engineer documents the `terraform login` workflow: "Running `terraform login` opens a browser to authenticate with HCP Terraform. Once complete, the API token is saved to `.terraform/credentials.json` inside your current working directory — this is why you should add `.terraform/` to your `.gitignore` to prevent the token from being committed to version control."

What is the specific error in this documentation?

- A) The token is stored in memory only for the duration of the current shell session — no file is written to disk
- B) The file is written to `.terraform.d/credentials.tfrc.json` inside the current working directory, not `.terraform/credentials.json`
- C) The token is saved to `~/.terraform.d/credentials.tfrc.json` in the user's **home directory** — not in the project's `.terraform/` directory
- D) `terraform login` saves the token to the system keychain, not a file, on supported operating systems

---

### Question 9 — HCP Terraform Audit Log Properties

**Difficulty**: Medium
**Answer Type**: many
**Topic**: The immutability and exportability of HCP Terraform audit logs

**Question**:
A compliance officer reviews HCP Terraform's audit logging capabilities. Which TWO of the following statements about HCP Terraform audit logs contain an error? (Select two.)

- A) Every action taken in an HCP Terraform organisation is logged, including run triggers, variable changes, team membership updates, and policy overrides
- B) Organisation Owners can edit or redact audit log entries containing sensitive information before exporting them to external systems
- C) Audit logs are immutable — no user, including Owners, can modify or delete individual log entries
- D) Audit logs are stored internally within HCP Terraform and cannot be exported to external SIEM or log management systems

---

### Question 10 — `import` Block Workflow Step Order

**Difficulty**: Medium
**Answer Type**: one
**Topic**: The correct sequence of steps when using a declarative `import` block with `-generate-config-out`

**Question**:
A developer explains the `import` block workflow to a colleague:

> "Step 1: Run `terraform plan -generate-config-out=generated.tf` — this scans the `import` requirements and generates the HCL skeleton.
> Step 2: Add an `import` block to your configuration with the correct `to` and `id` values to match the generated skeleton.
> Step 3: Run `terraform apply` to complete the import."

What is the error in this workflow description?

- A) Step 3 should be `terraform import`, not `terraform apply`
- B) The `import` block must be added to the configuration **before** running `terraform plan -generate-config-out` — the flag generates HCL for resources already referenced by existing `import` blocks and cannot discover what to generate without them
- C) Step 1 should use `terraform apply -generate-config-out`, not `terraform plan -generate-config-out`
- D) The generated file from `-generate-config-out` must be manually renamed to `main.tf` before `terraform apply` will process it

---

### Question 11 — `terraform state list` Capabilities

**Difficulty**: Medium
**Answer Type**: one
**Topic**: What `terraform state list` outputs versus what `terraform state show` outputs

**Question**:
A developer states: "Use `terraform state list` to get a full inventory of your managed infrastructure — it outputs each resource along with all its current attribute values like IP addresses, ARNs, instance types, and tags. It is the fastest way to see the complete current state of every resource in one view."

What is the error in this description?

- A) `terraform state list` does not read from the state file — it queries the cloud provider API directly
- B) `terraform state list` only outputs **resource addresses** (one per line, e.g., `aws_instance.web`) — it does not display attribute values; use `terraform state show <address>` to see all recorded attributes for a specific resource
- C) `terraform state list` is a deprecated command — `terraform show` is the recommended replacement for listing all managed resources
- D) `terraform state list` only shows resources in the root module and cannot list resources inside child modules

---

### Question 12 — HCP Terraform Private Registry Source Address

**Difficulty**: Hard
**Answer Type**: one
**Topic**: Correct source address format for modules published to the HCP Terraform private registry

**Question**:
A team publishes an internal VPC module to their HCP Terraform organisation's private registry. A developer writes this module reference in a root configuration:

```hcl
module "vpc" {
  source  = "registry.terraform.io/acme-corp/vpc/aws"
  version = "~> 2.0"
}
```

The developer claims: "This is correct — private registry modules follow the same source address format as the public Terraform Registry, using `registry.terraform.io` as the hostname."

What is the error?

- A) Private registry modules do not use a hostname prefix at all — the format is `<org>/<module>/<provider>` without any host component
- B) The correct hostname for the HCP Terraform private registry is `app.terraform.io`, not `registry.terraform.io` — the source address should be `app.terraform.io/acme-corp/vpc/aws`
- C) The private registry requires the full URL format: `https://app.terraform.io/app/acme-corp/registry/modules/private/vpc/aws`
- D) Private registry modules cannot be versioned with `~>` constraints — an exact version must be specified

---

### Question 13 — Dynamic Provider Credentials (OIDC) Misconceptions

**Difficulty**: Hard
**Answer Type**: many
**Topic**: How OIDC dynamic provider credentials work and what they replace in HCP Terraform

**Question**:
An engineer prepares training material on dynamic provider credentials. Which TWO of the following statements contain an error? (Select two.)

- A) With OIDC dynamic credentials, no long-lived static cloud credentials (e.g., AWS access key + secret key) need to be stored in HCP Terraform workspace variables — each run receives a short-lived token scoped to that run
- B) OIDC trust is established by storing the cloud provider's OIDC client secret as a sensitive environment variable in HCP Terraform — HCP Terraform presents this secret to authenticate itself to the cloud provider during each run
- C) When a run begins, HCP Terraform generates a signed JWT (JSON Web Token) that it presents to the cloud provider; the cloud provider validates the token against its configured OIDC trust relationship with HCP Terraform's issuer endpoint
- D) OIDC dynamic credentials are available for any Terraform provider registered in the public registry — any provider that supports AWS-compatible API calls can automatically use OIDC authentication with HCP Terraform

## Answer Key

| Q# | Answer(s) | Explanation | Source | Difficulty |
|----|-----------|-----------:|--------|------------|
| 1 | B | N/A | Whether the CLI `terraform import` command supports the `-generate-config-out` flag | Easy |
| 2 | B | N/A | Where Terraform writes log output when `TF_LOG` is set but `TF_LOG_PATH` is not | Easy |
| 3 | B | N/A | Correct use of the `to` and `id` arguments in a declarative `import` block | Medium |
| 4 | A | N/A | Whether `cloud` and `backend` blocks can be used together in the same `terraform {}` block | Medium |
| 5 | B, C | N/A | Distinguishing `advisory`, `soft-mandatory`, and `hard-mandatory` enforcement level behaviour | Medium |
| 6 | B | N/A | What HCP Terraform health assessments do when they detect drift, and what they cannot do | Medium |
| 7 | A | N/A | The lifecycle limitations of speculative plans in HCP Terraform | Medium |
| 8 | C | N/A | Where `terraform login` stores the HCP Terraform API token on disk | Medium |
| 9 | B, D | N/A | The immutability and exportability of HCP Terraform audit logs | Medium |
| 10 | B | N/A | The correct sequence of steps when using a declarative `import` block with `-generate-config-out` | Medium |
| 11 | B | N/A | What `terraform state list` outputs versus what `terraform state show` outputs | Medium |
| 12 | B | N/A | Correct source address format for modules published to the HCP Terraform private registry | Hard |
| 13 | B, D | N/A | How OIDC dynamic provider credentials work and what they replace in HCP Terraform | Hard |
