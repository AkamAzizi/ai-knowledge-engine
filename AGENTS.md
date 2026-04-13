# AI Knowledge Engine — Agent Operating Manual

This file defines how an LLM agent should read, write, and maintain this knowledge base. Read this file completely at the start of every session before doing anything else.

Compatible with: Claude, GPT-4, Gemini, or any LLM with file access and multi-step reasoning.

---

## Identity and Roles

**Your role (LLM agent):** Read, write, and maintain the knowledge base. You do the filing, cross-referencing, synthesis, and bookkeeping. You write every file in `knowledge/`. You never modify `raw/`.

**Human's role:** Curate sources, direct the analysis, ask questions, and decide what matters. The human is the editor; you are the writer.

**Core constraint:** `raw/` is immutable. Read from it; never write to it.

---

## File Structure

```
ai-knowledge-engine/
├── AGENTS.md                  ← this file
├── knowledge/
│   ├── index.md               ← master catalog; read this first on every session
│   ├── concepts/              ← idea and framework pages
│   ├── sources/               ← one summary page per ingested raw document
│   ├── entities/              ← people, organizations, products, tools
│   ├── analyses/              ← deep dives, comparisons, synthesis pages
│   └── overviews/             ← domain-level synthesis and reading maps
├── templates/                 ← blank templates; copy these when creating new pages
├── logs/
│   └── ingestion.md           ← append-only operations log
└── raw/                       ← source documents (read-only)
    └── assets/
```

---

## File Conventions

### Frontmatter (YAML)
Every file in `knowledge/` must begin with YAML frontmatter:

```yaml
---
title: "Page Title"
type: source | entity | concept | analysis | overview
tags: [tag1, tag2]
created: YYYY-MM-DD
updated: YYYY-MM-DD
sources: [source-slug-1, source-slug-2]
---
```

All fields are required. No exceptions.

### Naming
- Files use `kebab-case.md`
- Source pages: named after the source slug, e.g. `attention-is-all-you-need.md`
- Entity pages: canonical name, e.g. `andrej-karpathy.md`
- Concept pages: concept name, e.g. `transformer-architecture.md`
- Analysis pages: descriptive slug, e.g. `gpt4-vs-claude-comparison.md`

### Internal Links
Use Obsidian wiki-link syntax: `[[page-name|Display Name]]`

When referencing pages across folders, use path-relative links:
- Concepts: `[[concepts/slug|Display Name]]`
- Sources: `[[sources/slug|Display Name]]`
- Entities: `[[entities/slug|Display Name]]`

**Link aggressively.** Every entity or concept that has its own page must be linked on its first mention in any page.

---

## Page Structure Standards

### Concept pages (`knowledge/concepts/`)
```
## Definition
## How It Works
## Key Sources
## Related Concepts
## Open Questions
```

### Source pages (`knowledge/sources/`)
```
**Author:** / **Published:** / **Origin:** / **Raw source:**

## Summary        ← 3–5 sentence synthesis
## Key Points     ← bulleted; most important claims
## Entities       ← linked entity pages
## Concepts       ← linked concept pages
## Contradictions ← conflicts with existing wiki, or "None."
## Questions      ← open questions this source raises
```

### Entity pages (`knowledge/entities/`)
```
## Overview
## Key Contributions  (or ## Role)
## Appearances        ← sources where this entity appears
## Related
```

### Analysis pages (`knowledge/analyses/`)
Free-form, but must include:
```
## Sources    ← what informed this analysis
## Conclusion ← the synthesis claim
```

### Overview pages (`knowledge/overviews/`)
```
## Thesis           ← current best synthesis across all sources
## Reading Map      ← what to read and in what order
## Key Entities
## Key Concepts
## Open Questions
## Gaps             ← what sources are missing
```

---

## Workflows

### INGEST — adding a new source

Triggered by: user drops a file in `raw/` and says "ingest raw/filename.md"

**Steps:**
1. **Read** `knowledge/index.md` — understand current state
2. **Read** the source file in `raw/`
3. **Discuss** — surface 2–3 key takeaways with the user; confirm emphasis before writing
4. **Create** `knowledge/sources/<slug>.md` — full source summary page
5. **Update** existing entity pages touched by this source (or create new ones)
6. **Update** existing concept pages touched by this source (or create new ones)
7. **Update** any relevant overview pages if they exist
8. **Update** `knowledge/index.md` — add new page; update summaries of modified pages; increment counts
9. **Append** to `logs/ingestion.md` — one entry with date, operation, pages created/updated

**Rule:** Do all file touches in one session. Don't leave cross-references half-done.

---

### QUERY — answering a question

Triggered by: user asks any question

**Steps:**
1. **Read** `knowledge/index.md` to identify relevant pages
2. **Read** the relevant `knowledge/` pages (not raw sources — the knowledge base is the compiled layer)
3. **Answer** with inline citations linking to knowledge pages
4. **Offer** to file the answer as `knowledge/analyses/<slug>.md` if it is substantive

---

### LINT — health-checking the knowledge base

Triggered by: user says "lint"

**Steps:**
1. Read `knowledge/index.md` for all pages
2. Read a representative sample (or all, if the base is small)
3. **Report:**
   - Contradictions between pages
   - Stale claims superseded by newer sources
   - Orphan pages (no inbound links)
   - Concepts mentioned in pages but lacking their own page
   - Missing cross-references
   - Data gaps (important questions with no source coverage)
4. Suggest new sources to find or questions to investigate
5. **Ask the user before applying fixes if >5 files will change**
6. Apply agreed fixes and append to `logs/ingestion.md`

---

### UPDATE — revising an existing page

Triggered by: user asks you to update a page, or a new ingest touches an existing page

**Steps:**
1. Read the existing page
2. Make targeted changes — do not rewrite sections that don't need changing
3. Update `updated:` in frontmatter to today's date
4. Add new source slugs to the `sources:` list if applicable
5. Update the page's one-line summary in `knowledge/index.md`

---

## knowledge/index.md Format

```markdown
---
title: "Knowledge Index"
type: overview
tags: [meta, index]
created: YYYY-MM-DD
updated: YYYY-MM-DD
sources: []
---

# Knowledge Index

_Last updated: YYYY-MM-DD — N sources, M pages_

## Sources
- [[sources/slug|Title]] — one-line summary

## Entities
- [[entities/slug|Name]] — one-line description

## Concepts
- [[concepts/slug|Name]] — one-line definition (grouped by domain if >10 concepts)

## Analyses
- [[analyses/slug|Title]] — one-line description

## Overviews
- [[overviews/slug|Title]] — one-line description
```

Update the count line and the relevant section on every ingest or update.

---

## logs/ingestion.md Format

Append-only. Most recent entries at the **top**. Never edit past entries.

```markdown
## [YYYY-MM-DD] operation | Title or description
Brief note on what was done — pages created/updated, key finding, notable contradiction or gap.
```

Operations: `ingest`, `query`, `lint`, `update`, `init`

---

## Behavioral Rules

1. **Read before writing.** Always read `AGENTS.md` and `knowledge/index.md` at session start.
2. **Link aggressively.** Every entity or concept with its own page must be linked on first mention.
3. **Contradictions are first-class.** When a new source conflicts with an existing claim, note it explicitly in both the source page and the affected concept/entity page. Never silently overwrite.
4. **Answers compound.** Substantive query answers should be filed in `knowledge/analyses/`. Knowledge must not evaporate into chat history.
5. **Stay in scope.** Do not modify `raw/`. Do not create files outside the defined structure.
6. **One log entry per operation.** Every ingest, lint, or significant update closes with a `logs/ingestion.md` entry.
7. **Keep the index current.** An outdated `knowledge/index.md` degrades the entire system. Update it on every operation.
8. **Ask before bulk changes.** If a lint pass would touch more than 5 files, present the plan and get confirmation first.
9. **Frontmatter always.** Every knowledge file needs valid YAML frontmatter. No exceptions.
10. **Don't over-create.** Prefer updating an existing page over creating a new one. Only create a new page when the concept, entity, or source is genuinely distinct and would be linked from multiple other pages.
