---
title: "Version Control"
type: concept
tags: [git, collaboration, workflow, best-practices]
created: 2026-04-13
updated: 2026-04-13
sources: [coding-best-practices-and-guidelines]
---

# Version Control

## Definition

A system that records changes to files over time so that specific versions can be recalled later. Git is by far the dominant version control system. Hosted on platforms like GitHub and Bitbucket.

## How It Works

### Core Concepts

| Term | Meaning |
|---|---|
| **Repository (repo)** | The project folder tracked by Git |
| **Branch** | A divergent version of the codebase for isolated work |
| **Merge** | Reconciling two branches into one |
| **Pull request** | A request to incorporate a branch into another (typically `main`) |
| **Push** | Uploading local commits to the remote repository |
| **Commit** | A saved snapshot with a descriptive message |
| **Merge conflict** | When two branches modify the same lines — requires manual resolution |

### For Teams
- Developers branch off `main`, work independently, then submit pull requests.
- Git merges changes and flags conflicts.
- Pull requests double as code review checkpoints.
- Eliminates file-passing workflows ("email me the latest version").

### For Solo Developers
Even without collaborators, Git provides:
- **Revert history** — roll back to any previous working state.
- **Side-by-side comparison** — trace regressions to specific commits.
- **Publishing** — share code via GitHub for portfolio or open-source use.
- **Branching for experiments** — try an approach without risking the working version.

### Commit Message Best Practices
- Write clear, concise messages describing the *purpose* of the change, not just *what* changed.
- Consistent format across the team makes history readable.
- Clean commit history = project timeline + debugging aid.

## Key Sources

- [[sources/coding-best-practices-and-guidelines|Coding Best Practices and Guidelines]] — covers collaborative and solo Git workflows

## Related Concepts

- [[concepts/code-review|Code Review & Refactoring]] — pull requests are the standard entry point for code review
- [[concepts/code-documentation|Code Documentation]] — commit messages are a form of documentation
- [[concepts/test-driven-development|Test-Driven Development]] — tests in CI/CD run on each push/PR

## Open Questions

- Git flow vs trunk-based development — when is each appropriate?
- How do commit signing and branch protection rules factor in for security-sensitive repos?
