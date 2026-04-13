---
title: "CI/CD Pipelines"
type: concept
tags: [cicd, automation, devops, deployment, testing, version-control]
created: 2026-04-13
updated: 2026-04-13
sources: [mobile-app-best-practices-2025]
---

# CI/CD Pipelines

## Definition

**Continuous Integration (CI):** Developers frequently merge code changes into a shared repository; every merge automatically triggers a build and test suite.

**Continuous Deployment (CD):** Every change that passes CI is automatically deployed to a test or production environment.

Together they form a pipeline that transforms code commits into verified, deployable releases — removing manual steps, reducing human error, and creating a rapid feedback loop.

## How It Works

### The Pipeline Stages

```
Code commit → Build → Unit tests → Integration tests → UI tests → Quality gate → Deploy → Monitor
```

Each stage must pass before the next begins. A failure at any gate blocks the merge and alerts the developer immediately — when the context is still fresh.

### Quality Gates
- **Static code analysis** — linting, style enforcement, security scanning.
- **Unit tests** — fast, isolated function-level checks.
- **Integration tests** — verify component interactions.
- **UI / end-to-end tests** — validate critical user flows (login, checkout, core features).

A build **automatically fails** and blocks merging if any gate is not met. This prevents regressions from entering the main branch.

### For Mobile Apps Specifically
The CD stage handles the complex mobile release process automatically:
- **Code signing** — iOS certificates, Android keystores.
- **Versioning** — auto-increment build numbers.
- **Distribution** — upload to Apple TestFlight (beta) or Google Play Console.

This removes the most error-prone and time-consuming manual steps from every release cycle.

### Platforms

| Platform | Notes |
|---|---|
| GitHub Actions | Tightly integrated with GitHub repos; YAML-based |
| GitLab CI | Built into GitLab; powerful multi-stage pipelines |
| CircleCI | Strong mobile support; fast parallelism |
| Jenkins | Self-hosted; highly configurable; more operational overhead |

### Starting Small
1. Begin with CI only: auto-build + unit tests on every commit.
2. Add integration tests and UI tests as quality gates.
3. Extend to CD: automate deployment to staging, then production/app stores.

## Key Sources

- [[sources/mobile-app-best-practices-2025|Mobile App Best Practices 2025]] — primary treatment; mobile-specific CI/CD with app store deployment automation

## Related Concepts

- [[concepts/version-control|Version Control]] — CI/CD is the automation layer that runs on top of Git workflows; every push/PR triggers the pipeline
- [[concepts/test-driven-development|Test-Driven Development]] — tests are what make CI/CD reliable; a pipeline is only as good as its test suite
- [[concepts/modular-architecture|Modular Architecture]] — modular codebases enable faster, more parallelizable CI builds
- [[concepts/analytics-and-monitoring|Analytics and Monitoring]] — the monitoring layer that catches issues CI/CD missed after deployment

## Open Questions

- How do CI/CD pipelines handle A/B test variants or feature flags across releases?
- What are the best practices for rollback automation when a production deploy fails?
- How does CI/CD differ for React Native vs. Flutter vs. native iOS/Android builds?
