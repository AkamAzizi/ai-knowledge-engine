#!/usr/bin/env python3
"""Print knowledge base statistics.

Reports page counts by type, the most-linked pages in the knowledge graph,
and any orphan pages (no inbound wiki-links detected).

Usage:
    python scripts/stats.py
"""

import re
from collections import Counter, defaultdict
from pathlib import Path

KNOWLEDGE_DIR = Path(__file__).parent.parent / "knowledge"
VALID_TYPES = ["concept", "source", "entity", "analysis", "overview"]


def get_frontmatter_field(text: str, field: str) -> str | None:
    m = re.search(rf"^{field}:\s*['\"]?(.+?)['\"]?\s*$", text, re.MULTILINE)
    return m.group(1).strip("\"'") if m else None


def get_wikilinks(text: str) -> list[str]:
    """Extract all [[target]] and [[target|display]] link targets."""
    return re.findall(r"\[\[([^\]|]+?)(?:\|[^\]]+)?\]\]", text)


def main() -> None:
    root = KNOWLEDGE_DIR.parent
    all_files = sorted(KNOWLEDGE_DIR.rglob("*.md"))
    # Pages: everything except index.md (counted separately as the catalog)
    files = [f for f in all_files if f.name != "index.md"]

    pages_by_type: dict[str, list[Path]] = defaultdict(list)
    inbound: Counter = Counter()

    # Build page registry: both "concepts/agent-tool-design" and "agent-tool-design" forms
    page_keys: set[str] = set()
    for path in files:
        folder = path.parent.name
        slug = path.stem
        page_keys.add(f"{folder}/{slug}")

    # Count inbound links across ALL files (including index.md)
    for path in all_files:
        text = path.read_text(encoding="utf-8")
        if path.name != "index.md":
            page_type = get_frontmatter_field(text, "type")
            pages_by_type[page_type or "unknown"].append(path)

        for link in get_wikilinks(text):
            target = link.strip()
            inbound[target] += 1
            # Also count the short form so both match
            short = target.split("/")[-1]
            if short != target:
                inbound[short] += 1

    total = sum(len(v) for v in pages_by_type.values())

    print()
    print("  AI Knowledge Engine — Stats")
    print("  " + "─" * 38)
    print(f"  Total pages: {total}\n")

    for t in VALID_TYPES:
        pages = pages_by_type.get(t, [])
        if not pages:
            continue
        bar = "▪" * len(pages)
        print(f"  {t:<12}  {len(pages):>3}  {bar}")

    unknown = pages_by_type.get("unknown", [])
    if unknown:
        print(f"  {'unknown':<12}  {len(unknown):>3}")

    # Top linked — use qualified form only to avoid double-counting
    qualified_links = {k: v for k, v in inbound.items() if "/" in k and k in page_keys}
    if qualified_links:
        top = sorted(qualified_links.items(), key=lambda x: -x[1])[:10]
        print(f"\n  Most-linked pages:")
        for target, count in top:
            print(f"    {count:>3}×  [[{target}]]")

    # Orphan detection
    orphans = []
    for key in sorted(page_keys):
        folder, slug = key.split("/", 1)
        linked = qualified_links.get(key, 0) + inbound.get(slug, 0)
        if linked == 0:
            path = KNOWLEDGE_DIR / folder / f"{slug}.md"
            orphans.append(path.relative_to(root))

    if orphans:
        print(f"\n  Orphan pages ({len(orphans)} — no inbound links detected):")
        for o in orphans:
            print(f"    {o}")
    else:
        print("\n  No orphan pages. ✓")

    print()


if __name__ == "__main__":
    main()
