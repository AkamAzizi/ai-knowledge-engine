#!/usr/bin/env python3
"""Search the knowledge base by keyword or regex.

Scans all .md files under knowledge/ and prints matching lines with file context.
Supports optional filtering by page type.

Usage:
    python scripts/search.py <query>
    python scripts/search.py <query> --type concept
    python scripts/search.py "OAuth|JWT" --type concept
    python scripts/search.py "open question" --type analysis

Arguments:
    query        Search term. Supports Python regex syntax (case-insensitive).
    --type TYPE  Filter results to a specific page type:
                 concept, entity, source, analysis, overview
"""

import argparse
import re
import sys
from pathlib import Path

KNOWLEDGE_DIR = Path(__file__).parent.parent / "knowledge"
VALID_TYPES = {"concept", "entity", "source", "analysis", "overview"}
MAX_MATCHES_PER_FILE = 4


def get_frontmatter_field(text: str, field: str) -> str | None:
    m = re.search(rf"^{field}:\s*['\"]?(.+?)['\"]?\s*$", text, re.MULTILINE)
    return m.group(1).strip("\"'") if m else None


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Search the AI Knowledge Engine",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__.strip(),
    )
    parser.add_argument("query", help="Search term or regex (case-insensitive)")
    parser.add_argument(
        "--type",
        choices=sorted(VALID_TYPES),
        metavar="TYPE",
        help=f"Filter by page type: {', '.join(sorted(VALID_TYPES))}",
    )
    args = parser.parse_args()

    try:
        pattern = re.compile(args.query, re.IGNORECASE)
    except re.error as e:
        print(f"Invalid regex: {e}", file=sys.stderr)
        sys.exit(1)

    root = KNOWLEDGE_DIR.parent
    results = []

    for path in sorted(KNOWLEDGE_DIR.rglob("*.md")):
        text = path.read_text(encoding="utf-8")

        if args.type and get_frontmatter_field(text, "type") != args.type:
            continue

        matches = [
            (i + 1, line)
            for i, line in enumerate(text.splitlines())
            if pattern.search(line)
        ]

        if matches:
            title = get_frontmatter_field(text, "title") or path.stem
            results.append((path.relative_to(root), title, matches))

    if not results:
        qualifier = f" [type={args.type}]" if args.type else ""
        print(f"No results for '{args.query}'{qualifier}.")
        return

    qualifier = f" [type={args.type}]" if args.type else ""
    print(f"Found {len(results)} page(s) matching '{args.query}'{qualifier}:\n")

    for rel_path, title, matches in results:
        print(f"  {rel_path}")
        print(f"  {title}")
        for lineno, line in matches[:MAX_MATCHES_PER_FILE]:
            print(f"    {lineno:>4}  {line.strip()[:100]}")
        if len(matches) > MAX_MATCHES_PER_FILE:
            print(f"         … {len(matches) - MAX_MATCHES_PER_FILE} more match(es)")
        print()


if __name__ == "__main__":
    main()
