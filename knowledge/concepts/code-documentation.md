---
title: "Code Documentation"
type: concept
tags: [documentation, readme, docstrings, comments, best-practices]
created: 2026-04-13
updated: 2026-04-13
sources: [coding-best-practices-and-guidelines]
---

# Code Documentation

## Definition

The practice of embedding explanatory text within and alongside source code so that other developers (or your future self) can understand, use, and maintain it without reverse-engineering the logic from scratch.

## How It Works

Three layers of documentation:

### 1. Inline Comments
- Explain *why* a section of code does what it does — not just *what* it does.
- Mark open tasks with `TODO:` prefix (all-caps, searchable via grep).
- Don't use comments to compensate for badly structured code — fix the structure first.

### 2. Docstrings (Python)
String literals embedded in functions, classes, and modules. Accessible via `help()` and command-line docs. Standard format:

```python
def calculate_total_price(unit_price, quantity):
    """
    Calculate the total price of items.

    Args:
        unit_price (float): Price of a single item.
        quantity (int): Number of items purchased.

    Returns:
        float: Total price.

    Example:
        >>> calculate_total_price(10.0, 5)
        50.0
    """
    return unit_price * quantity
```

### 3. README Files
External documentation file (`README.txt` or `README.md`) stored alongside the code. Should include:
- **Purpose** — what the code does
- **Inputs and outputs** — what goes in, what comes out
- **Architecture and design** — how it's structured
- **Quirks** — anything non-obvious the user needs to know
- **Error and maintenance notes**
- Optionally: author, dates, version history

Put the most critical information at the top. Use ALL CAPS or visual separators (---) to make critical warnings stand out.

## Key Sources

- [[sources/coding-best-practices-and-guidelines|Coding Best Practices and Guidelines]] — full treatment of all three documentation layers

## Related Concepts

- [[concepts/naming-conventions|Naming Conventions]] — good naming reduces the documentation burden
- [[concepts/code-review|Code Review & Refactoring]] — missing or outdated docs are flagged in review
- [[concepts/test-driven-development|Test-Driven Development]] — unit tests serve as executable documentation

## Open Questions

- What's the right ratio of comments to code? When do comments become noise?
- Tools like Sphinx, pdoc, MkDocs — how do they automate README/docstring-to-site generation?
