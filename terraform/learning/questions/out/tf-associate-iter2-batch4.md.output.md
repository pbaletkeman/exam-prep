# Terraform Associate Exam Questions

---

### Question 1 — Attribute Reference Ordering

**Difficulty**: Easy
**Answer Type**: one
**Topic**: What Terraform does when a resource references another resource's attribute

**Question**:
A configuration contains the following two resources:

```hcl
resource "aws_vpc" "main" {
  cidr_block = "10.0.0.0/16"
}

resource "aws_subnet" "public" {
  vpc_id     = aws_vpc.main.id
  cidr_block = "10.0.1.0/24"
}
```

`terraform apply` is run. In what order does Terraform create these resources, and why?

- A) Both resources are created concurrently because Terraform always maximises parallelism
- B) `aws_subnet.public` is created first because it is declared last in the file
- C) `aws_vpc.main` is created first because `aws_subnet.public` references its `id` attribute, creating an implicit dependency
- D) The order is undefined; Terraform randomises creation order for performance

---

### Question 2 — var.* Reference Between Resources

**Difficulty**: Easy
**Answer Type**: one
**Topic**: Whether a shared variable reference creates a dependency between resources

**Question**:
Two resource blocks both use `var.region` in their configurations:

```hcl
resource "aws_instance" "web" {
  ami           = "ami-0abc123"
  instance_type = "t3.micro"
  availability_zone = var.region
}

resource "aws_s3_bucket" "logs" {
  bucket = "logs-${var.region}"
}
```

Does Terraform create a dependency between `aws_instance.web` and `aws_s3_bucket.logs`? What happens during apply?

- A) Yes — sharing `var.region` creates an implicit dependency; Terraform creates `aws_instance.web` before `aws_s3_bucket.logs`
- B) No — `var.*` references do not create dependency edges; Terraform creates both resources in parallel
- C) Yes — all resources sharing any common value are always serialised
- D) No — but Terraform still creates them sequentially to avoid API rate limits

---

### Question 3 — Data Source Read Timing

**Difficulty**: Easy
**Answer Type**: one
**Topic**: When a data source is read relative to plan and apply phases

**Question**:
A data source is declared as:

```hcl
data "aws_ami" "ubuntu" {
  most_recent = true
  owners      = ["099720109477"]
}

resource "aws_instance" "web" {
  ami           = data.aws_ami.ubuntu.id
  instance_type = "t3.micro"
}
```

When does Terraform read the data source and retrieve the AMI ID?

- A) When `terraform init` runs — data sources are resolved during initialisation
- B) During `terraform plan` — Terraform queries the provider API to fetch the AMI ID before generating the execution plan
- C) Only after `aws_instance.web` is created — the data source is read at the end of apply
- D) Never — data sources only use values already present in state

---

### Question 4 — prevent_destroy Blocks a Destroy Plan

**Difficulty**: Medium
**Answer Type**: one
**Topic**: What happens when terraform destroy runs against a resource with prevent_destroy = true

**Question**:
A production RDS instance is declared with:

```hcl
resource "aws_db_instance" "prod" {
  # ... config
  lifecycle {
    prevent_destroy = true
  }
}
```

An engineer runs `terraform destroy`. What happens?

- A) Terraform destroys the database after displaying an extra confirmation prompt
- B) Terraform destroys all other resources but skips `aws_db_instance.prod` without error
- C) Terraform returns an error during planning and refuses to generate a destroy plan for that resource
- D) Terraform creates a snapshot of the database before proceeding with the destroy

---

### Question 5 — ignore_changes and Subsequent Drift

**Difficulty**: Medium
**Answer Type**: one
**Topic**: What terraform plan reports when a listed attribute has drifted with ignore_changes set

**Question**:
An EC2 instance is declared with:

```hcl
resource "aws_instance" "web" {
  ami           = "ami-0abc123"
  instance_type = "t3.micro"
  tags          = { Name = "web" }

  lifecycle {
    ignore_changes = [tags]
  }
}
```

An administrator manually adds a tag `Owner = "ops"` via the AWS console. `terraform plan` is run. What does Terraform report regarding the tags?

- A) Terraform proposes removing `Owner = "ops"` to revert to the declared tag set
- B) Terraform reports no changes to the `tags` attribute — drift on `tags` is ignored
- C) Terraform returns an error because `ignore_changes` cannot be used with the `tags` attribute
- D) Terraform updates the state file to include `Owner = "ops"` and reports the config as out of date

---

### Question 6 — replace_triggered_by on Launch Template Change

**Difficulty**: Medium
**Answer Type**: one
**Topic**: What happens to the dependent resource when replace_triggered_by fires

**Question**:
An Auto Scaling Group is configured with:

```hcl
resource "aws_autoscaling_group" "web" {
  # ... config

  lifecycle {
    replace_triggered_by = [aws_launch_template.web]
  }
}
```

The `aws_launch_template.web` resource is updated in the configuration (e.g., the AMI ID changes). `terraform apply` is run. What happens to `aws_autoscaling_group.web`?

- A) Terraform updates `aws_autoscaling_group.web` in-place without destroying it
- B) Terraform destroys and recreates `aws_autoscaling_group.web`, even if its own configuration has not changed
- C) Terraform ignores the launch template change until `aws_autoscaling_group.web` is explicitly updated
- D) Terraform returns an error because `replace_triggered_by` requires both resources to be in the same module

---

### Question 7 — moved Block Prevents Destroy and Recreate

**Difficulty**: Medium
**Answer Type**: one
**Topic**: What happens when a moved block is used to rename a resource

**Question**:
A running EC2 instance is declared as `resource "aws_instance" "app"`. An engineer renames it to `resource "aws_instance" "web"` in the configuration and adds:

```hcl
moved {
  from = aws_instance.app
  to   = aws_instance.web
}
```

`terraform apply` is run. What happens to the EC2 instance?

- A) The EC2 instance is destroyed and a new one is created with the name `web`
- B) The state file is updated to track the instance as `aws_instance.web`; the running EC2 instance is not touched
- C) Terraform returns an error because renaming resources requires manual state manipulation
- D) Terraform creates a second EC2 instance named `web` and leaves the original `app` instance running

---

### Question 8 — depends_on Reduces Parallelism

**Difficulty**: Medium
**Answer Type**: one
**Topic**: How explicit depends_on affects apply parallelism

**Question**:
A configuration has 10 independent EC2 instances (no attribute references between them) and Terraform's default parallelism of 10. An engineer adds `depends_on = [aws_instance.web_0]` to `aws_instance.web_1` through `aws_instance.web_9`. `terraform apply` is run. What is the behaviour?

- A) All 10 instances are still created concurrently because `depends_on` is only advisory
- B) Only `aws_instance.web_0` is created first; the remaining 9 instances wait for it to complete before being created
- C) Terraform returns an error because `depends_on` is not permitted between resources of the same type
- D) The instances are created two at a time because `depends_on` halves the default parallelism

---

### Question 9 — Data Source Dependent on Computed Value

**Difficulty**: Medium
**Answer Type**: one
**Topic**: When a data source is deferred to apply because it depends on an unknown value

**Question**:
A data source depends on the ID of a resource that does not yet exist:

```hcl
resource "aws_vpc" "main" {
  cidr_block = "10.0.0.0/16"
}

data "aws_subnets" "available" {
  filter {
    name   = "vpc-id"
    values = [aws_vpc.main.id]
  }
}
```

`terraform plan` is run for the first time. When does Terraform read the `data.aws_subnets.available` data source?

- A) During `terraform plan` — Terraform reads all data sources before generating the plan
- B) During `terraform apply` — after `aws_vpc.main` is created and its `id` is known
- C) During `terraform init` — data sources with filters are resolved at initialisation
- D) Terraform never reads this data source because the VPC does not exist yet

---

### Question 10 — removed Block with destroy = false

**Difficulty**: Medium
**Answer Type**: many
**Topic**: What happens when a removed block with destroy = false is applied

**Question**:
An engineer adds the following block to a configuration that previously managed an EC2 instance:

```hcl
removed {
  from = aws_instance.legacy

  lifecycle {
    destroy = false
  }
}
```

`terraform apply` is run. Which TWO statements correctly describe the outcome? (Select two.)

- A) The EC2 instance is deleted from AWS
- B) The EC2 instance continues to run in AWS unaffected
- C) Terraform removes `aws_instance.legacy` from the state file so it is no longer managed
- D) Future `terraform plan` runs will propose recreating `aws_instance.legacy` from the configuration

---

### Question 11 — create_before_destroy with Immutable Attribute

**Difficulty**: Medium
**Answer Type**: one
**Topic**: Plan output when an immutable attribute changes with create_before_destroy set

**Question**:
An EC2 instance is declared with `create_before_destroy = true`. The `ami` attribute (which forces replacement when changed) is updated in the configuration. `terraform plan` is run. What does the plan output show for this resource?

- A) `~ aws_instance.web` — the instance will be updated in-place
- B) `-/+ aws_instance.web` — the instance will be replaced, with the new instance created before the old one is destroyed
- C) `+ aws_instance.web` — a second instance will be added; the original is not touched
- D) The plan returns an error because changing `ami` requires setting `prevent_destroy = false` first

---

### Question 12 — apply -parallelism=1 Effect

**Difficulty**: Hard
**Answer Type**: one
**Topic**: What terraform apply -parallelism=1 does to resource creation order

**Question**:
A configuration creates 8 independent resources (no dependencies between them). An engineer runs `terraform apply -parallelism=1`. What is the behaviour compared to the default?

- A) Terraform creates all 8 resources in a single API call to improve efficiency
- B) Terraform creates one resource at a time sequentially, rather than up to 10 concurrently — the apply takes longer but reduces API concurrency
- C) Terraform creates 2 resources at a time instead of the default 10
- D) The command fails because `-parallelism=1` is not a valid value

---

### Question 13 — depends_on on a Data Source

**Difficulty**: Hard
**Answer Type**: many
**Topic**: Behaviour when depends_on is added to a data source

**Question**:
A data source has `depends_on = [aws_iam_role_policy.app]` added to it:

```hcl
data "aws_s3_objects" "uploads" {
  bucket = "my-app-uploads"

  depends_on = [aws_iam_role_policy.app]
}
```

Which TWO statements correctly describe the impact of this `depends_on`? (Select two.)

- A) The data source will not be read during `terraform plan` — it is deferred to apply after `aws_iam_role_policy.app` is applied
- B) The data source will still be read during plan, but only after `aws_iam_role_policy.app` is created
- C) Adding `depends_on` to a data source forces it to be read during apply instead of plan, even if no computed values are involved
- D) The `depends_on` on a data source has no effect — data sources always read during plan regardless

## Answer Key

| Q# | Answer(s) | Explanation | Source | Difficulty |
|----|-----------|-----------:|--------|------------|
| 1 | C | N/A | What Terraform does when a resource references another resource's attribute | Easy |
| 2 | B | N/A | Whether a shared variable reference creates a dependency between resources | Easy |
| 3 | B | N/A | When a data source is read relative to plan and apply phases | Easy |
| 4 | C | N/A | What happens when terraform destroy runs against a resource with prevent_destroy = true | Medium |
| 5 | B | N/A | What terraform plan reports when a listed attribute has drifted with ignore_changes set | Medium |
| 6 | B | N/A | What happens to the dependent resource when replace_triggered_by fires | Medium |
| 7 | B | N/A | What happens when a moved block is used to rename a resource | Medium |
| 8 | B | N/A | How explicit depends_on affects apply parallelism | Medium |
| 9 | B | N/A | When a data source is deferred to apply because it depends on an unknown value | Medium |
| 10 | B, C | N/A | What happens when a removed block with destroy = false is applied | Medium |
| 11 | B | N/A | Plan output when an immutable attribute changes with create_before_destroy set | Medium |
| 12 | B | N/A | What terraform apply -parallelism=1 does to resource creation order | Hard |
| 13 | A, C | N/A | Behaviour when depends_on is added to a data source | Hard |
