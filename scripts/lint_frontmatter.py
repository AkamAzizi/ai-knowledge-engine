#!/usr/bin/env python3
"""Validate YAML frontmatter on all knowledge/ pages.

Checks that every .md file under knowledge/ has a frontmatter block with all
required fields and a valid type value. Used by the GitHub Actions CI workflow.

Usage:
    python scripts/lint_frontmatter.py

Exit codes:
    0  — all files valid
    1  — one or more errors found
"""

import re
import sys
from pathlib import Path

REQUIRED_FIELDS = {"title", "type", "tags", "created", "updated", "sources"}
VALID_TYPES = {"concept", "entity", "source", "analysis", "overview"}
KNOWLEDGE_DIR = Path(__file__).parent.parent / "knowledge"


def extract_frontmatter(text: str) -> str | None:
    """Return the raw frontmatter block content, or None if not present."""
    m = re.match(r"^---\n(.*?)\n---", text, re.DOTALL)
    return m.group(1) if m else None


def parse_frontmatter_keys(text: str) -> dict[str, str]:
    """Extract top-level key: value pairs. Ignores list/nested values."""
    fields = {}
    for line in text.splitlines():
        m = re.match(r"^(\w[\w-]*):\s*(.*)", line)
        if m:
            fields[m.group(1)] = m.group(2).strip()
    return fields


def lint_file(path: Path) -> list[str]:
    errors = []
    rel = path.relative_to(KNOWLEDGE_DIR.parent)
    text = path.read_text(encoding="utf-8")

    fm = extract_frontmatter(text)
    if fm is None:
        return [f"{rel}: missing frontmatter block"]

    fields = parse_frontmatter_keys(fm)

    missing = REQUIRED_FIELDS - set(fields.keys())
    if missing:
        errors.append(f"{rel}: missing required field(s): {', '.join(sorted(missing))}")

    if "type" in fields:
        t = fields["type"].strip("\"'")
        if t not in VALID_TYPES:
            errors.append(
                f"{rel}: invalid type '{t}' — expected one of: {', '.join(sorted(VALID_TYPES))}"
            )

    return errors


def main() -> None:
    files = sorted(KNOWLEDGE_DIR.rglob("*.md"))
    errors: list[str] = []

    for f in files:
        errors.extend(lint_file(f))

    print(f"Checked {len(files)} file(s) in knowledge/")

    if errors:
        print(f"\n{len(errors)} error(s) found:\n")
        for e in errors:
            print(f"  ✗  {e}")
        sys.exit(1)

    print("All frontmatter valid. ✓")


if __name__ == "__main__":
    main()
