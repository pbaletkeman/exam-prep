# Terraform Associate Exam Questions

---

### Question 1 — `create_before_destroy` Replacement Order

**Difficulty**: Easy
**Answer Type**: one
**Topic**: Reading a `lifecycle` block to identify the order of destroy and create during a forced replacement

**Question**:
Read this resource block:

```hcl
resource "aws_instance" "web" {
  ami           = data.aws_ami.ubuntu.id
  instance_type = "t3.micro"

  lifecycle {
    create_before_destroy = true
  }
}
```

The AMI referenced by `data.aws_ami.ubuntu.id` changes. Terraform determines that a replacement is required. In what order does Terraform perform the operations?

- A) Terraform destroys the existing instance first, then creates the new one
- B) Terraform creates the new instance first, then destroys the old one only after the new one is successfully provisioned
- C) Terraform updates the existing instance in-place — `create_before_destroy` prevents any destroy operation
- D) Terraform creates both instances simultaneously and destroys whichever completes last

---

### Question 2 — Distinguishing a Data Source Reference from a Resource Reference

**Difficulty**: Easy
**Answer Type**: one
**Topic**: Identifying which expression references a data source vs a managed resource attribute

**Question**:
Read this resource block:

```hcl
resource "aws_instance" "web" {
  ami           = data.aws_ami.ubuntu.id
  subnet_id     = aws_subnet.public.id
  instance_type = "t3.micro"
}
```

Which of the two attribute references — `data.aws_ami.ubuntu.id` and `aws_subnet.public.id` — references a **data source**, and what syntactically distinguishes it?

- A) `aws_subnet.public.id` — resource references always include a `data.` prefix
- B) `data.aws_ami.ubuntu.id` — the `data.` prefix identifies it as a data source reference, not a managed resource
- C) Both are data source references — all attribute references in Terraform begin with a provider keyword
- D) Neither is a data source reference — both reference managed resources declared with a `resource` block

---

### Question 3 — `moved` Block Address After Apply

**Difficulty**: Easy
**Answer Type**: one
**Topic**: Identifying which state address Terraform uses after a `moved` block is applied

**Question**:
Read this `moved` block:

```hcl
moved {
  from = aws_instance.server
  to   = aws_instance.api
}
```

The `aws_instance.server` resource is running in AWS and tracked in state. After `terraform apply` processes this block, under which address is the EC2 instance tracked in the state file?

- A) `aws_instance.server` — the `moved` block creates an alias but keeps the original address
- B) Both `aws_instance.server` and `aws_instance.api` — state records both addresses until the block is removed
- C) `aws_instance.api` — the state file is updated to use the new address; the real EC2 instance is not touched
- D) The instance is destroyed and a new instance is created under `aws_instance.api`

---

### Question 4 — Three-Resource Implicit Dependency Chain

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Reading a three-resource configuration to identify which resource is created last and why

**Question**:
Read this configuration:

```hcl
resource "aws_vpc" "main" {
  cidr_block = "10.0.0.0/16"
}

resource "aws_subnet" "public" {
  vpc_id     = aws_vpc.main.id
  cidr_block = "10.0.1.0/24"
}

resource "aws_instance" "web" {
  ami       = "ami-0abc123"
  subnet_id = aws_subnet.public.id
}
```

Which resource is created **last**, and what in the HCL determines this ordering?

- A) `aws_vpc.main` — it is declared first, so Terraform creates it last to allow dependencies to resolve
- B) `aws_subnet.public` — it has the most arguments, indicating the highest complexity
- C) `aws_instance.web` — it references `aws_subnet.public.id`, which itself references `aws_vpc.main.id`, creating a three-level dependency chain
- D) All three are created in parallel — HCL declaration order is the only ordering Terraform respects

---

### Question 5 — `ignore_changes` on a Modified Attribute

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Reading a plan output for a resource whose changed attribute is listed in `ignore_changes`

**Question**:
Read this resource block:

```hcl
resource "aws_instance" "web" {
  ami           = "ami-0abc123"
  instance_type = "t3.micro"

  lifecycle {
    ignore_changes = [ami]
  }
}
```

The AMI in the AWS account has been manually changed from `ami-0abc123` to `ami-0new9876`. A `terraform plan` is run. What does Terraform report for `aws_instance.web`?

- A) `~ ami = "ami-0abc123" -> "ami-0new9876"` — Terraform will update the AMI to match the new value
- B) No changes to `aws_instance.web` — the `ami` attribute is listed in `ignore_changes`, so drift on it is silently ignored
- C) Terraform returns an error because `ignore_changes` cannot be used with the `ami` argument
- D) Terraform destroys the instance and recreates it with the new AMI

---

### Question 6 — `removed` Block with `destroy = false`

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Reading a `removed` block to identify the effect on the real cloud resource

**Question**:
Read this `removed` block:

```hcl
removed {
  from = aws_s3_bucket.legacy

  lifecycle {
    destroy = false
  }
}
```

The `aws_s3_bucket.legacy` bucket currently exists in AWS and is tracked in state. After `terraform apply` processes this block, what happens to the S3 bucket?

- A) The bucket is deleted from AWS because the `removed` block explicitly removes the resource
- B) The bucket remains in AWS unchanged — Terraform removes it from state but does not destroy the real cloud resource
- C) The bucket is moved to a new state address `aws_s3_bucket.removed_legacy` as an archived entry
- D) Terraform returns an error because `destroy = false` is not a valid lifecycle argument inside a `removed` block

---

### Question 7 — `depends_on` Ordering Guarantee

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Reading a `depends_on` list to identify which resource Terraform is guaranteed to apply first

**Question**:
Read this configuration:

```hcl
resource "aws_iam_role_policy" "s3_access" {
  role   = aws_iam_role.app.name
  policy = data.aws_iam_policy_document.s3.json
}

resource "aws_instance" "app" {
  ami           = "ami-0abc123"
  instance_type = "t3.micro"

  depends_on = [aws_iam_role_policy.s3_access]
}
```

What ordering does the `depends_on` on `aws_instance.app` guarantee?

- A) `aws_instance.app` is created first so it can begin using the S3 policy as soon as the policy is ready
- B) `aws_iam_role_policy.s3_access` is fully applied before `aws_instance.app` is created, even though no attribute of the policy is directly referenced by the instance
- C) Both resources are created in parallel — `depends_on` only affects destroy ordering, not create ordering
- D) Terraform returns a warning because `depends_on` is redundant when both resources reference the same IAM role

---

### Question 8 — `replace_triggered_by` with a Specific Attribute

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Reading a `replace_triggered_by` referencing an attribute vs an entire resource

**Question**:
Read this configuration:

```hcl
resource "aws_launch_template" "web" {
  image_id      = var.ami_id
  instance_type = "t3.micro"
}

resource "aws_autoscaling_group" "web" {
  min_size = 1
  max_size = 3

  lifecycle {
    replace_triggered_by = [aws_launch_template.web.image_id]
  }
}
```

How does `replace_triggered_by = [aws_launch_template.web.image_id]` differ from `replace_triggered_by = [aws_launch_template.web]`?

- A) There is no difference — referencing a resource and referencing one of its attributes produce identical behaviour
- B) Referencing the attribute `image_id` means the ASG is replaced **only** when `image_id` changes; updating other launch template attributes (e.g., `instance_type`) does not trigger ASG replacement
- C) Referencing an attribute reference is a syntax error — `replace_triggered_by` only accepts full resource addresses, not attribute paths
- D) Referencing `aws_launch_template.web.image_id` makes the trigger one-directional — changes to the ASG no longer propagate back to the launch template

---

### Question 9 — `terraform apply -parallelism=1`

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Reading a `terraform apply -parallelism` flag to identify its effect on execution

**Question**:
An engineer runs:

```bash
terraform apply -parallelism=1
```

The configuration manages 8 independent resources with no dependency relationships between them. What does `-parallelism=1` do to the apply execution?

- A) Terraform creates all 8 resources simultaneously — `-parallelism=1` sets the first resource as the primary and applies the rest in parallel
- B) Terraform creates exactly one resource at a time in strict sequence, even though all 8 could safely run in parallel
- C) Terraform returns an error — `-parallelism` must be set to at least 2 when independent resources exist
- D) `-parallelism=1` is the default value and has no effect; Terraform always applies one resource at a time without this flag

---

### Question 10 — `lifecycle` Block with Multiple Arguments

**Difficulty**: Medium
**Answer Type**: many
**Topic**: Reading a lifecycle block with three arguments to identify TWO correct behavioural statements

**Question**:
Read this resource block:

```hcl
resource "aws_db_instance" "prod" {
  instance_class = "db.t3.medium"
  engine_version = "14.5"

  lifecycle {
    create_before_destroy = true
    prevent_destroy       = true
    ignore_changes        = [engine_version]
  }
}
```

Which TWO statements correctly describe the behaviour this `lifecycle` block enforces? (Select two.)

- A) If any execution plan includes destroying `aws_db_instance.prod`, Terraform will return an error at plan time
- B) If `engine_version` is upgraded in the AWS console, `terraform plan` will propose reverting it to `"14.5"`
- C) If a replacement of the database is required, Terraform will provision the new instance before deleting the old one
- D) `prevent_destroy = true` only protects against `terraform destroy` — it does not block replacements triggered by config changes

---

### Question 11 — Data Source Block TWO Correct Statements

**Difficulty**: Medium
**Answer Type**: many
**Topic**: Reading a data source block and its consumer resource to identify TWO correct statements

**Question**:
Read this configuration:

```hcl
data "aws_ami" "ubuntu" {
  most_recent = true
  owners      = ["099720109477"]

  filter {
    name   = "name"
    values = ["ubuntu/images/hvm-ssd/ubuntu-jammy-22.04-amd64-server-*"]
  }
}

resource "aws_instance" "web" {
  ami           = data.aws_ami.ubuntu.id
  instance_type = "t3.micro"
}
```

Which TWO statements correctly describe this configuration? (Select two.)

- A) `data.aws_ami.ubuntu` does not create a new AMI in AWS — it queries an existing AMI that matches the filter criteria
- B) The `filter` block inside the `data` source instructs Terraform to create a new Ubuntu AMI if no existing AMI matches the pattern
- C) The reference `data.aws_ami.ubuntu.id` uses the `data.` prefix to distinguish it as a data source reference, not a managed resource reference
- D) The `most_recent = true` argument causes Terraform to create a new AMI version on every `terraform plan` to ensure freshness

---

### Question 12 — Parallel vs Sequential Resource Creation

**Difficulty**: Hard
**Answer Type**: one
**Topic**: Reading a multi-resource configuration to identify which resources run concurrently and which must wait

**Question**:
Read this configuration (assume `aws_vpc.main` and `aws_iam_role.web` already exist in state):

```hcl
resource "aws_security_group" "web_sg" {
  name   = "web-sg"
  vpc_id = aws_vpc.main.id
}

resource "aws_iam_instance_profile" "web" {
  name = "web-profile"
  role = aws_iam_role.web.name
}

resource "aws_instance" "web" {
  ami                    = "ami-0abc123"
  instance_type          = "t3.micro"
  vpc_security_group_ids = [aws_security_group.web_sg.id]
  iam_instance_profile   = aws_iam_instance_profile.web.name
}
```

Which statement correctly describes how Terraform schedules creation of these three resources?

- A) All three resources are created sequentially in file declaration order: `aws_security_group.web_sg` → `aws_iam_instance_profile.web` → `aws_instance.web`
- B) `aws_security_group.web_sg` and `aws_iam_instance_profile.web` are independent — Terraform creates them in parallel; `aws_instance.web` is created last because it references both
- C) `aws_instance.web` is created first because it is declared last — Terraform processes bottom-up
- D) All three are created in parallel because Terraform always maximises concurrency regardless of references

---

### Question 13 — `moved` Block into a Module

**Difficulty**: Hard
**Answer Type**: many
**Topic**: Reading a `moved` block that relocates a resource from root module into a child module

**Question**:
Read this `moved` block:

```hcl
moved {
  from = aws_s3_bucket.app_data
  to   = module.storage.aws_s3_bucket.app_data
}
```

The S3 bucket `aws_s3_bucket.app_data` exists in state and in AWS. A `module "storage"` block has been added to the configuration that declares the same `aws_s3_bucket.app_data` resource. Which TWO statements correctly describe the effect of this `moved` block? (Select two.)

- A) Terraform updates the state file to track the bucket under `module.storage.aws_s3_bucket.app_data` without destroying and recreating the real S3 bucket
- B) Terraform destroys the existing bucket at `aws_s3_bucket.app_data` and creates a new bucket inside the `module.storage` module
- C) After a successful `terraform apply`, the `moved` block can be safely removed from the configuration — the state already records the updated address
- D) The `moved` block must remain in the configuration permanently to prevent Terraform from flagging the address difference on each subsequent plan

## Answer Key

| Q# | Answer(s) | Explanation | Source | Difficulty |
|----|-----------|-----------:|--------|------------|
| 1 | B | N/A | Reading a `lifecycle` block to identify the order of destroy and create during a forced replacement | Easy |
| 2 | B | N/A | Identifying which expression references a data source vs a managed resource attribute | Easy |
| 3 | C | N/A | Identifying which state address Terraform uses after a `moved` block is applied | Easy |
| 4 | C | N/A | Reading a three-resource configuration to identify which resource is created last and why | Medium |
| 5 | B | N/A | Reading a plan output for a resource whose changed attribute is listed in `ignore_changes` | Medium |
| 6 | B | N/A | Reading a `removed` block to identify the effect on the real cloud resource | Medium |
| 7 | B | N/A | Reading a `depends_on` list to identify which resource Terraform is guaranteed to apply first | Medium |
| 8 | B | N/A | Reading a `replace_triggered_by` referencing an attribute vs an entire resource | Medium |
| 9 | B | N/A | Reading a `terraform apply -parallelism` flag to identify its effect on execution | Medium |
| 10 | A, C | N/A | Reading a lifecycle block with three arguments to identify TWO correct behavioural statements | Medium |
| 11 | A, C | N/A | Reading a data source block and its consumer resource to identify TWO correct statements | Medium |
| 12 | B | N/A | Reading a multi-resource configuration to identify which resources run concurrently and which must wait | Hard |
| 13 | A, C | N/A | Reading a `moved` block that relocates a resource from root module into a child module | Hard |
