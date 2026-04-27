# Terraform Associate Exam Questions

---

### Question 1 — fmt on Already-Formatted Files

**Difficulty**: Easy
**Answer Type**: one
**Topic**: What terraform fmt reports when all files are already canonical

**Question**:
An engineer runs `terraform fmt` on a directory where all `.tf` files are already in canonical format. What happens?

- A) Terraform rewrites all `.tf` files to ensure they have the latest formatting conventions, even if nothing changes
- B) Terraform reports no output and exits with code 0 — no files are modified
- C) Terraform prompts the engineer to confirm whether files should be reformatted
- D) Terraform returns an error because `fmt` requires at least one file change to complete

---

### Question 2 — validate Catches Undefined Reference

**Difficulty**: Easy
**Answer Type**: one
**Topic**: What terraform validate returns when a resource references an undefined local

**Question**:
A configuration contains this expression: `name = local.environment_name`, but no `locals` block defining `environment_name` exists in any `.tf` file. `terraform validate` is run. What happens?

- A) Terraform silently ignores the undefined reference and validates the remaining configuration
- B) Terraform returns an error such as `Reference to undeclared local value` and exits with a non-zero code
- C) Terraform creates an empty `locals` block and sets `environment_name = null` to resolve the reference
- D) The error is deferred until `terraform plan` because `validate` does not check local references

---

### Question 3 — plan -target Scope Limiting

**Difficulty**: Easy
**Answer Type**: one
**Topic**: What terraform plan -target does to the rest of the configuration

**Question**:
A configuration manages 20 resources. An engineer runs `terraform plan -target=aws_instance.web`. What does Terraform plan for?

- A) All 20 resources, but it highlights `aws_instance.web` as the primary resource
- B) Only `aws_instance.web` and any resources that `aws_instance.web` directly or indirectly depends on
- C) Only `aws_instance.web`, ignoring all dependencies
- D) The 20 resources grouped by provider, starting with `aws_instance.web`

---

### Question 4 — Infrastructure Change Between Plan and Apply

**Difficulty**: Medium
**Answer Type**: one
**Topic**: What happens when a saved plan file is applied after infrastructure changes

**Question**:
An engineer runs `terraform plan -out=release.tfplan` and reviews the plan showing 3 resources to add. Before running `terraform apply release.tfplan`, another engineer manually deletes one of those resources' dependencies from the cloud. The first engineer runs `terraform apply release.tfplan`. What happens?

- A) Terraform re-plans automatically, detects the change, and updates the plan before applying
- B) Terraform applies the exact changes captured in `release.tfplan` without re-planning — the apply may fail or produce unexpected results if the dependency is missing
- C) Terraform detects the out-of-band change and refuses to apply the saved plan, prompting the engineer to re-run plan
- D) Terraform skips the resource whose dependency is missing and applies the other two successfully

---

### Question 5 — fmt -check in a CI Pipeline

**Difficulty**: Medium
**Answer Type**: one
**Topic**: What terraform fmt -check returns when a file has incorrect formatting

**Question**:
A CI pipeline runs `terraform fmt -check` as part of a pull request check. A developer submits a PR that contains a `.tf` file with inconsistent indentation. What does the CI step report?

- A) The check passes with a warning, and the CI pipeline auto-formats the file in-place
- B) The check fails with exit code 1, and the PR check is marked as failed — no files are modified
- C) The check passes because `fmt` only verifies syntax, not style
- D) The check fails and `fmt` rewrites the file directly in the developer's PR branch

---

### Question 6 — graph Command Output Format

**Difficulty**: Medium
**Answer Type**: one
**Topic**: What terraform graph outputs and how it is rendered

**Question**:
An engineer runs `terraform graph`. What does the command output, and what additional tool is required to visualise it?

- A) An SVG image of the dependency graph rendered directly in the terminal
- B) A JSON file describing all resource dependencies, viewable in any text editor
- C) A DOT format text representation of the dependency graph — Graphviz is required to render it as an image
- D) An HTML page that can be opened in a browser to interactively explore the resource graph

---

### Question 7 — apply -replace Resource Lifecycle

**Difficulty**: Medium
**Answer Type**: one
**Topic**: What terraform apply -replace does to the targeted resource

**Question**:
An EC2 instance `aws_instance.app` is running normally. An engineer runs `terraform apply -replace="aws_instance.app"`. The configuration has not changed. What does Terraform do?

- A) Terraform skips the command because no configuration changes exist — replace requires a config change
- B) Terraform destroys the existing instance and creates a new one, even though the configuration is unchanged
- C) Terraform updates the instance in-place without destroying it
- D) Terraform marks the instance as tainted in state but takes no immediate action

---

### Question 8 — output -raw vs Standard output

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Difference in output format between terraform output and terraform output -raw

**Question**:
A Terraform output is declared as:

```hcl
output "bucket_name" {
  value = aws_s3_bucket.main.id
}
```

The bucket ID is `my-app-bucket-prod`. An engineer runs both `terraform output bucket_name` and `terraform output -raw bucket_name` in a shell script. What is the difference in the values each command returns?

- A) `terraform output bucket_name` returns `"my-app-bucket-prod"` (with surrounding quotes); `terraform output -raw bucket_name` returns `my-app-bucket-prod` (no quotes)
- B) Both commands return identical output — `my-app-bucket-prod`
- C) `terraform output -raw` returns JSON; the standard command returns plain text
- D) `terraform output -raw` strips all characters except alphanumerics; standard returns the full value

---

### Question 9 — console Expression Evaluation

**Difficulty**: Medium
**Answer Type**: one
**Topic**: What terraform console returns when evaluating a built-in function

**Question**:
An engineer opens `terraform console` and types:

```
length(["web", "api", "db"])
```

What does the console return?

- A) `["web", "api", "db"]` — the console echoes the input unchanged
- B) `3`
- C) `error: function "length" requires a map type`
- D) The console opens a file browser to select a `.tf` file to evaluate

---

### Question 10 — validate Misses Live Cloud Resources

**Difficulty**: Medium
**Answer Type**: many
**Topic**: What terraform validate does and does not catch

**Question**:
A configuration references `ami = "ami-0abc12345"`, which does not exist in the target AWS region. It also has a variable reference `var.instance_count` that is not declared in any `variables.tf`. `terraform validate` is run. Which TWO statements are correct? (Select two.)

- A) Terraform validate catches the undefined `var.instance_count` reference and reports an error
- B) Terraform validate catches the invalid AMI ID and reports an error
- C) Terraform validate does not check whether the AMI ID exists in AWS — that error only surfaces during plan or apply
- D) Terraform validate requires AWS credentials to verify any `ami` attribute

---

### Question 11 — destroy -target Scope

**Difficulty**: Medium
**Answer Type**: one
**Topic**: What happens when terraform destroy -target targets a resource with dependents

**Question**:
A configuration has a VPC (`aws_vpc.main`) and an EC2 instance (`aws_instance.web`) that depends on the VPC. An engineer runs `terraform destroy -target=aws_vpc.main`. What does Terraform propose?

- A) Terraform destroys only the VPC; the EC2 instance is left running unaffected
- B) Terraform destroys the EC2 instance first (dependent), then the VPC (dependency) to maintain correct ordering
- C) Terraform returns an error because you cannot target a resource that other resources depend on
- D) Terraform destroys the VPC immediately without considering any dependencies

---

### Question 12 — Skipping init When Changing Backend

**Difficulty**: Hard
**Answer Type**: one
**Topic**: What happens when the backend changes but terraform init is not re-run

**Question**:
An engineer changes the `backend` block in the `terraform {}` configuration from local to an S3 remote backend. Without running `terraform init`, the engineer runs `terraform plan`. What happens?

- A) Terraform detects the backend change automatically and migrates state during `terraform plan`
- B) Terraform returns an error indicating that the backend configuration has changed and `terraform init` must be run
- C) Terraform runs the plan using the new S3 backend silently — no init is needed for backend changes
- D) Terraform runs the plan using the old local backend and ignores the new backend block until the next full init

---

### Question 13 — fmt -diff Behaviour

**Difficulty**: Hard
**Answer Type**: many
**Topic**: What terraform fmt -diff does versus terraform fmt -check

**Question**:
An engineer runs `terraform fmt -diff` on a directory containing two `.tf` files, one of which has incorrect indentation. Which TWO statements correctly describe the outcome? (Select two.)

- A) The command outputs a unified diff showing exactly what changed in the incorrectly formatted file
- B) The command rewrites the incorrectly formatted file to canonical style
- C) The command does not modify any files — it only shows what would change, like a dry run
- D) The command exits with code 1 to signal that formatting errors were found

## Answer Key

| Q# | Answer(s) | Explanation | Source | Difficulty |
|----|-----------|-----------:|--------|------------|
| 1 | B | N/A | What terraform fmt reports when all files are already canonical | Easy |
| 2 | B | N/A | What terraform validate returns when a resource references an undefined local | Easy |
| 3 | B | N/A | What terraform plan -target does to the rest of the configuration | Easy |
| 4 | B | N/A | What happens when a saved plan file is applied after infrastructure changes | Medium |
| 5 | B | N/A | What terraform fmt -check returns when a file has incorrect formatting | Medium |
| 6 | C | N/A | What terraform graph outputs and how it is rendered | Medium |
| 7 | B | N/A | What terraform apply -replace does to the targeted resource | Medium |
| 8 | A | N/A | Difference in output format between terraform output and terraform output -raw | Medium |
| 9 | B | N/A | What terraform console returns when evaluating a built-in function | Medium |
| 10 | A, C | N/A | What terraform validate does and does not catch | Medium |
| 11 | B | N/A | What happens when terraform destroy -target targets a resource with dependents | Medium |
| 12 | B | N/A | What happens when the backend changes but terraform init is not re-run | Hard |
| 13 | A, B | N/A | What terraform fmt -diff does versus terraform fmt -check | Hard |
