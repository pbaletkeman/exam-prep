# GitHub Actions Certification (GH-200) Exam Overview

## Skills at a Glance

| Domain | Weight |
| ------ | ------ |
| [Author and manage workflows](#domain-1-author-and-manage-workflows) | 20–25% |
| [Consume and troubleshoot workflows](#domain-2-consume-and-troubleshoot-workflows) | 15–20% |
| [Author and maintain actions](#domain-3-author-and-maintain-actions) | 15–20% |
| [Manage GitHub Actions for the enterprise](#domain-4-manage-github-actions-for-the-enterprise) | 20–25% |
| [Secure and optimize automation](#domain-5-secure-and-optimize-automation) | 10–15% |

---

## Domain 1: Author and Manage Workflows (20–25%)

### Configure Workflow Triggers and Events

- Configure workflows to run for scheduled, manual, webhook, and repository events
- Choose appropriate scope, permissions, and events for workflow automation
- Define and validate `workflow_dispatch` inputs (types, required, defaults)
- Pass inputs to reusable workflows via `workflow_call` with inputs and secrets mapping

### Design and Implement Workflow Structure

- Use jobs, steps, and conditional logic
- Implement dependencies between jobs
- Use workflow commands and environment variables
- Use service containers (`services:`) for dependent services (databases, queues); configure ports, health checks, and container options
- Use `strategy` and `matrix` to generate job variations (OS, language/runtime versions)
  - Apply `include`/`exclude` rules
  - Control `fail-fast` and `max-parallel`
  - Optimize matrix size for cost and performance
  - Account for runner image changes (Ubuntu 20.04 deprecation, Windows Server 2025 migration for `windows-latest`)
- Implement YAML anchors and aliases (`&`, `*`, and merge `<<`) to reuse repeated mappings/steps within a single workflow file
- Use predefined contexts (`github`, `runner`, `env`, `vars`, `secrets`, `inputs`, `matrix`, `needs`, `strategy`, `job`, `steps`, `github.event`, `github.ref`)
  - Access workflow, repository, and runtime metadata
  - Understand immutable actions behavior and version pinning requirements
- Evaluate expressions with `${{ }}` referencing contexts
  - Distinguish static (workflow parse) vs runtime evaluation
  - Prevent secret leakage in logs and expressions
- Leverage editor tooling (GitHub Actions VS Code extension, YAML schema completion, metadata IntelliSense, validation)

### Manage Workflow Execution and Outputs

- Configure caching and artifact management
- Apply retention policies via REST APIs (logs, artifacts, workflow runs) at org/repo level
- Pass data between jobs and steps
  - Artifacts, outputs, environment files
  - `GITHUB_ENV` and `GITHUB_OUTPUT`
  - Reusable workflow outputs
- Generate job summaries using `GITHUB_STEP_SUMMARY` for rich Markdown reports (test results, coverage, links)
- Add workflow status badges and environment protections

---

## Domain 2: Consume and Troubleshoot Workflows (15–20%)

### Interpret Workflow Behavior and Results

- Identify workflow triggers and effects from configuration and logs
- Diagnose failed workflow runs using logs and run history
- Expand and interpret YAML anchors, aliases, and merged mappings when analyzing workflow configuration
- Interpret matrix expansions, correlate job names to matrix axes, analyze failures across variants
- Selectively rerun individual matrix jobs

### Access Workflow Artifacts and Logs

- Locate workflows, logs, and artifacts in the UI and via API
- Download and manage workflow artifacts

### Use and Manage Workflow Templates

- Consume organization-level and reusable workflows
- Consume non-public organization workflow templates
- Use starter workflows (public and private/non-public templates)
  - Customize and adapt
  - Distinguish from reusable workflows and composite actions
- Differentiate between:
  - **Starter workflows**: Copy scaffold, independent after creation
  - **Reusable workflows**: Central versioned definition invoked via `workflow_call`
  - **Composite actions**: Encapsulated step logic
- Contrast disabling and deleting workflows

---

## Domain 3: Author and Maintain Actions (15–20%)

### Create and Troubleshoot Custom Actions

- Identify and implement action types (JavaScript, Docker, composite)
- Understand immutable actions rollout on hosted runners
- Implications for version pinning and registry sources
- Troubleshoot action execution and errors

### Define Action Structure and Metadata

- Specify required files, directory structure, and metadata
- Implement workflow commands within actions

### Distribute and Maintain Actions

- Select distribution models (public, private, marketplace)
- Publish actions to the GitHub Marketplace
- Apply versioning and release strategies

---

## Domain 4: Manage GitHub Actions for the Enterprise (20–25%)

### Distribute and Govern Actions and Workflows

- Define and manage reusable components and templates
- Control access to actions and workflows within the enterprise
- Configure organizational use policies

### Manage Runners at Scale

- Configure and monitor GitHub-hosted and self-hosted runners
- Apply IP allow lists and networking settings
- Manage runner groups and troubleshoot runner issues
- Identify preinstalled software/tool versions on GitHub-hosted runners
  - Image release notes, toolcache
  - Install additional software at runtime
  - `setup-*` actions, package managers, caching, container images, custom self-hosted images

### Manage Encrypted Secrets and Variables

- Define and scope encrypted secrets and variables at multiple levels
  - Organization level
  - Repository level
  - Environment level
- Access and use secrets and variables in workflows and actions
- Manage secrets and variables programmatically via REST APIs

---

## Domain 5: Secure and Optimize Automation (10–15%)

### Implement Security Best Practices

- Use environment protections and approval gates
- Identify and use trustworthy actions from the Marketplace
- Mitigate script injection
  - Sanitize/validate inputs
  - Least-privilege permissions
  - Avoid untrusted data in `run:`
  - Proper shell quoting
  - Prefer vetted actions over inline scripts
- Understand `GITHUB_TOKEN` lifecycle
  - Ephemeral and scoped
  - Configure granular permissions
  - Contrast with PAT
  - Restrict write scopes
- Use OIDC token (`id-token` permission) for cloud provider federation
  - Eliminate long-lived cloud secrets
- Pin third-party actions to full commit SHAs
  - Align with immutable actions enforcement on hosted runners
  - Avoid floating `@main`/`@v*` without justification
- Enforce action usage policies (organization/repository allow/deny lists, required reviewers for unverified actions)
- Generate and verify artifact attestations / provenance (e.g., SLSA, build metadata)
  - Integrate into deployment verification

### Optimize Workflow Performance and Cost

- Configure caching and artifact retention for efficiency
- Apply retention policies programmatically via REST APIs
- Recommend strategies for scaling and optimizing workflows
