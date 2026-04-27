# Terraform Associate Exam Questions

---

### Question 1 — Identifying the Pure-Create Resource in a Plan

**Difficulty**: Easy
**Answer Type**: one
**Topic**: Reading plan output symbols to identify which resource will be created without a corresponding destruction

**Question**:
Read this `terraform plan` output:

```
  # aws_vpc.main will be created
+ resource "aws_vpc" "main" {
    + cidr_block = "10.0.0.0/16"
  }

  # aws_instance.web will be updated in-place
~ resource "aws_instance" "web" {
    ~ instance_type = "t3.micro" -> "t3.medium"
  }

  # aws_db_instance.primary must be replaced
-/+ resource "aws_db_instance" "primary" {
    ~ instance_class = "db.t3.micro" -> "db.t3.medium" # forces replacement
  }

Plan: 2 to add, 1 to change, 1 to destroy.
```

Which resource does the `+` symbol (without any `-`) indicate will be **created with no corresponding destruction**?

- A) `aws_db_instance.primary` — its `-/+` symbol includes a create step
- B) `aws_vpc.main` — the `+` prefix alone means a net-new object will be created
- C) `aws_instance.web` — the `~` symbol includes a create for the updated attributes
- D) All three resources will result in newly created objects after apply

---

### Question 2 — `terraform console` Evaluating a Map with `length`

**Difficulty**: Easy
**Answer Type**: one
**Topic**: Reading a `terraform console` REPL expression to identify the return value

**Question**:
An engineer opens `terraform console` and types:

```
length({"us-east-1" = "ami-111", "us-west-2" = "ami-222", "eu-west-1" = "ami-333"})
```

What value does the console return?

- A) `0` — `length()` returns 0 for map types; it only counts list elements
- B) `3`
- C) `{"us-east-1", "us-west-2", "eu-west-1"}` — the set of keys in the map
- D) An error — `length()` is not a valid built-in function in `terraform console`

---

### Question 3 — Reading `terraform workspace list` Output

**Difficulty**: Easy
**Answer Type**: one
**Topic**: Identifying the currently active workspace from `terraform workspace list` output

**Question**:
Read this output from `terraform workspace list`:

```
  default
  dev
* staging
  production
```

Which workspace is currently selected?

- A) `default` — the default workspace is always active unless explicitly changed
- B) `dev` — it is listed second, indicating it was most recently used
- C) `staging` — the `*` prefix marks the currently active workspace
- D) `production` — it is the last workspace listed, indicating it is the current context

---

### Question 4 — Interpreting a `-/+` Plan Block

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Reading a plan resource block with the `-/+` replace symbol to identify what Terraform will do

**Question**:
Read this `terraform plan` output block:

```
  # aws_instance.app must be replaced
-/+ resource "aws_instance" "app" {
    ~ id           = "i-0abc123def456" -> (known after apply)
    ~ ami          = "ami-0old12345678" -> "ami-0new87654321" # forces replacement
      instance_type = "t3.micro"
}
```

What does the `-/+` symbol on `aws_instance.app` indicate Terraform will do during apply?

- A) The instance will be updated in-place — only the `ami` attribute will change without downtime
- B) The instance will be imported from an existing cloud resource with a new Terraform address
- C) The existing instance will be destroyed and a brand-new instance will be created (replacement)
- D) The change is deferred — Terraform will update the instance on the next apply cycle, not the current one

---

### Question 5 — `terraform output -json` Structure

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Identifying which `terraform output` flag produces structured JSON with type metadata

**Question**:
Read this command output:

```json
{
  "vpc_id": {
    "sensitive": false,
    "type": "string",
    "value": "vpc-0abc12345ef678"
  },
  "subnet_ids": {
    "sensitive": false,
    "type": ["list", "string"],
    "value": ["subnet-111aaa", "subnet-222bbb"]
  }
}
```

Which `terraform output` flag produces this structured JSON format that includes `sensitive`, `type`, and `value` fields for each output?

- A) `terraform output --format=structured`
- B) `terraform output -raw`
- C) `terraform output -json`
- D) `terraform output -show-types`

---

### Question 6 — `terraform fmt -check` vs `terraform fmt -diff`

**Difficulty**: Medium
**Answer Type**: many
**Topic**: Reading two `terraform fmt` flag invocations and identifying what each does

**Question**:
Read these two commands:

```bash
terraform fmt -check
terraform fmt -diff
```

Which TWO statements correctly describe the behaviour of these two flags? (Select two.)

- A) `-check` exits with code 1 if any files need reformatting, without modifying any files — used to enforce formatting in CI pipelines
- B) `-diff` writes reformatted content to disk and then displays a summary of changes made
- C) `-diff` displays the formatting changes that would be made as a unified diff, without writing any changes to disk
- D) `-check` modifies files to canonical format and then verifies the result, exiting with code 0 on success

---

### Question 7 — `terraform show plan.tfplan`

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Identifying what `terraform show` displays when given a saved plan file

**Question**:
An engineer runs:

```bash
terraform plan -out=release.tfplan
terraform show release.tfplan
```

What does `terraform show release.tfplan` display?

- A) The current Terraform state — `show` always reads from `terraform.tfstate` regardless of the argument
- B) The human-readable contents of the saved plan file — the resource changes that would be applied when `terraform apply release.tfplan` is run
- C) The Terraform configuration files compiled into a single canonical HCL representation
- D) A comparison between the saved plan and the current live infrastructure to detect drift since the plan was saved

---

### Question 8 — Inline `-var` Flag Override

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Reading a `terraform plan -var` command to identify which value `var.instance_type` takes

**Question**:
A `variables.tf` file declares:

```hcl
variable "instance_type" {
  default = "t3.micro"
}
```

An engineer runs:

```bash
terraform plan -var "instance_type=t3.large"
```

What value does `var.instance_type` take during this plan run?

- A) `"t3.micro"` — the default value in `variables.tf` always takes precedence
- B) An error is raised because `-var` can only override variables that have no default
- C) `"t3.large"` — the inline `-var` flag value overrides the default declared in `variables.tf`
- D) Both values are used — Terraform creates a `t3.micro` instance and a `t3.large` instance to satisfy both declarations

---

### Question 9 — Interpreting an Update Plan Block

**Difficulty**: Medium
**Answer Type**: many
**Topic**: Reading a `~` plan block to identify which statements correctly describe the operation

**Question**:
Read this `terraform plan` output block:

```
~ resource "aws_security_group" "web" {
    ~ description = "allow http traffic" -> "allow http and https traffic"
    ~ name        = "web-sg-v1"          -> "web-sg-v2"
      vpc_id      = "vpc-0abc12345"
  }
```

Which TWO statements correctly interpret this output? (Select two.)

- A) The `~` prefix on the resource block means `aws_security_group.web` will be destroyed and recreated as a replacement
- B) `vpc_id` is not changing — lines without a `~` or `+/-` prefix show attributes that remain the same
- C) Both `description` and `name` will be updated in-place without destroying the security group
- D) The `->` arrow on individual attribute lines means those attributes will be moved to a different resource address

---

### Question 10 — `terraform init -migrate-state` Backend Block

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Reading a backend block addition and identifying which `terraform init` flag copies existing state to the new backend

**Question**:
A team adds this block to their configuration to move from local state to S3:

```hcl
terraform {
  backend "s3" {
    bucket = "my-company-tf-state"
    key    = "prod/terraform.tfstate"
    region = "us-east-1"
  }
}
```

They run `terraform init` and Terraform detects existing local state in `terraform.tfstate`. Which `terraform init` flag must they include to copy the existing state to the new S3 backend?

- A) `terraform init -migrate-state` — copies existing state to the new backend during initialisation
- B) `terraform init -upgrade` — upgrades the backend configuration and transfers state automatically
- C) `terraform init -reconfigure` — replaces the backend configuration and migrates state in one step
- D) `terraform init -backend=true` — enables the backend and imports the local state file

---

### Question 11 — `-auto-approve` with a Saved Plan File

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Identifying the effect of combining `-auto-approve` with a saved plan file argument

**Question**:
An engineer runs:

```bash
terraform apply -auto-approve release.tfplan
```

What is the effect of including `-auto-approve` when a saved plan file (`release.tfplan`) is also provided?

- A) `-auto-approve` causes Terraform to skip the plan phase and apply all resource changes unconditionally
- B) `-auto-approve` is required alongside a saved plan file to unlock the apply — without it, the apply is blocked
- C) `-auto-approve` is required to prevent Terraform from re-planning after loading the saved plan file
- D) `-auto-approve` is redundant — applying a saved plan file never prompts for confirmation; the plan has already been reviewed

---

### Question 12 — Plan Summary with Only Replacements

**Difficulty**: Hard
**Answer Type**: many
**Topic**: Interpreting a plan summary line where all changes are `-/+` replacements

**Question**:
Read this `terraform plan` summary line:

```
Plan: 2 to add, 0 to change, 2 to destroy.
```

The full plan output shows exactly two resources, both marked with `-/+` (replace). No resource has a `+`, `~`, or `-` prefix alone. Which TWO statements correctly interpret this plan summary? (Select two.)

- A) The "2 to add" refers to the new objects that will be created as part of the replacement operations
- B) The "2 to destroy" means two resources will be permanently deleted with no new objects created in their place
- C) `0 to change` confirms that no resource will be modified in-place — both operations require a destroy-then-create cycle
- D) The "2 to add" and "2 to destroy" must refer to four different resource addresses — adds and destroys are always distinct resources

---

### Question 13 — `terraform apply -replace` Plan Symbol

**Difficulty**: Hard
**Answer Type**: one
**Topic**: Identifying what plan symbol appears for a resource targeted by `terraform apply -replace` when the configuration is unchanged

**Question**:
A running EC2 instance is managed by Terraform as `aws_instance.web`. The configuration for this resource has not changed since the last apply. An engineer runs:

```bash
terraform apply -replace="aws_instance.web"
```

What symbol does the plan output show for `aws_instance.web`, and what does that symbol mean?

- A) No symbol — Terraform skips resources with no configuration changes even when `-replace` is specified
- B) `~` — the instance will be updated in-place because the configuration is unchanged
- C) `-/+` — the instance will be destroyed and recreated even though no configuration change triggered it
- D) `+` — a second instance will be created alongside the existing one before the original is removed

## Answer Key

| Q# | Answer(s) | Explanation | Source | Difficulty |
|----|-----------|-----------:|--------|------------|
| 1 | B | N/A | Reading plan output symbols to identify which resource will be created without a corresponding destruction | Easy |
| 2 | B | N/A | Reading a `terraform console` REPL expression to identify the return value | Easy |
| 3 | C | N/A | Identifying the currently active workspace from `terraform workspace list` output | Easy |
| 4 | C | N/A | Reading a plan resource block with the `-/+` replace symbol to identify what Terraform will do | Medium |
| 5 | C | N/A | Identifying which `terraform output` flag produces structured JSON with type metadata | Medium |
| 6 | A, C | N/A | Reading two `terraform fmt` flag invocations and identifying what each does | Medium |
| 7 | B | N/A | Identifying what `terraform show` displays when given a saved plan file | Medium |
| 8 | C | N/A | Reading a `terraform plan -var` command to identify which value `var.instance_type` takes | Medium |
| 9 | B, C | N/A | Reading a `~` plan block to identify which statements correctly describe the operation | Medium |
| 10 | A | N/A | Reading a backend block addition and identifying which `terraform init` flag copies existing state to the new backend | Medium |
| 11 | D | N/A | Identifying the effect of combining `-auto-approve` with a saved plan file argument | Medium |
| 12 | A, C | N/A | Interpreting a plan summary line where all changes are `-/+` replacements | Hard |
| 13 | C | N/A | Identifying what plan symbol appears for a resource targeted by `terraform apply -replace` when the configuration is unchanged | Hard |
