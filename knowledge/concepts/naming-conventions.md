---
title: "Naming Conventions"
type: concept
tags: [code-style, readability, best-practices]
created: 2026-04-13
updated: 2026-04-13
sources: [coding-best-practices-and-guidelines]
---

# Naming Conventions

## Definition

Rules governing how variables, functions, classes, and files are named in source code. Good names are self-documenting; bad names require comments to compensate for what the name fails to communicate.

## How It Works

Two dominant conventions:

| Convention | Style | Example |
|---|---|---|
| **camelCase** | Capital letter starts each new word | `accountNumber`, `calculateTotalPrice` |
| **snake_case** | Underscore separates words | `account_number`, `calculate_total_price` |

**Which to use:** Depends on language norms (Python favors snake_case; JavaScript favors camelCase), team standards, or personal preference. The critical rule is **consistency within a project** — mixing conventions is visually confusing and looks unprofessional.

**Meaningful names over short names:**
- `ab` → bad. `account_balance` → good.
- `change` → bad. `name_change` → good.
- A name should communicate what the variable holds or what the function does without requiring a comment.

**For functions:** Name should describe the action performed — `calculate_total_price`, not `calc` or `ctp`.

## Key Sources

- [[sources/coding-best-practices-and-guidelines|Coding Best Practices and Guidelines]] — primary treatment

## Related Concepts

- [[concepts/code-documentation|Code Documentation]] — naming and comments work together; good names reduce the need for comments
- [[concepts/code-review|Code Review & Refactoring]] — poor naming is a classic code smell caught in review

## Open Questions

- Are there automated tools (linters, formatters like Black or Ruff) that enforce naming conventions?
- How should naming conventions adapt for very short-lived variables in mathematical code?
