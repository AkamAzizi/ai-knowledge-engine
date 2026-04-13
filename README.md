<div align="center">

# AI Knowledge Engine

### A self-compounding knowledge base maintained by LLM agents

![Markdown](https://img.shields.io/badge/format-Markdown%20%2B%20YAML-blue?style=flat-square)
![Agent](https://img.shields.io/badge/agent-Claude%20Code-blueviolet?style=flat-square)
![Protocol](https://img.shields.io/badge/protocol-MCP-orange?style=flat-square)
![License](https://img.shields.io/badge/license-MIT-green?style=flat-square)

*Not a note-taking app. Not a RAG pipeline. A living knowledge graph that compounds.*

</div>

---

## The Problem with RAG

Standard RAG systems retrieve documents and re-derive answers from scratch on every query. Nothing is built up. Ask the same question a hundred times and the system does the same work each time. Add fifty documents and the synthesis still happens at query time, fragile and ephemeral.

This system takes a different approach: **compile knowledge once, compound it continuously.**

An LLM agent reads each new source, extracts what matters, and integrates it into a persistent, typed knowledge graph — updating concept pages, creating entity links, flagging contradictions, and deepening synthesis incrementally. By the time you ask a question, the answer is already mostly written. The graph reflects everything ever ingested, not just the last retrieval.

The more you feed it, the smarter it gets. The connections compound.

---

## What It Actually Does

**You drop in one article. Here is what happens:**

A 3,000-word security article on secure coding practices gets ingested. The agent reads it, surfaces three key takeaways for your review, then writes:

- `knowledge/sources/oligo-secure-coding-best-practices.md` — full structured summary with key points, entities, and open questions
- Updates `knowledge/concepts/secure-coding.md` — adds specific crypto algorithms (AES, RSA/ECC, TLS 1.3), obfuscation techniques, and a formal standards table (OWASP, CERT, NIST, ISO 27001) that weren't there before
- Creates `knowledge/concepts/runtime-security.md` — a new concept this source introduced, already cross-linked to secure-coding and vulnerability-types
- Creates `knowledge/concepts/vulnerability-types.md` — buffer overflows, integer overflows, format strings, race conditions — all categorised in a comparison table
- Creates `knowledge/entities/gal-elbaz.md` — the expert contributor, linked back to the source and to every concept he informed
- Updates `knowledge/index.md` — new pages catalogued, page count incremented
- Appends to `logs/ingestion.md` — timestamp, pages created, pages updated, contradictions found (none), open questions captured

**One article. One command. Nine files touched.**

Now you ingest a second source that covers similar ground. The agent reads the existing `secure-coding.md` page before writing anything. It finds a gap the first source didn't cover — certificate pinning and OAuth 2.0 for mobile — and adds a mobile security section. It also notes that the new source explicitly confirms the OWASP recommendations from the first, strengthening those claims. It does not duplicate; it integrates.

**After four sources, the `secure-coding` concept page draws from all of them** — synthesised, cross-referenced, with a contradictions section that tracks where sources diverge and an open questions section that tracks what remains unresolved. No single source could have produced that page. The agent built it incrementally, the same way a researcher would — except it never forgets what it read and never skips the filing.

**When you ask a question:**

> *"What are the most important secure coding practices for a mobile fintech app?"*

The agent reads `knowledge/index.md`, identifies five relevant pages, reads them, and returns a structured answer with inline citations — already synthesised across everything ingested. The answer references specific algorithms, formal standards, and mobile-specific patterns. It then offers to file the response as `knowledge/analyses/secure-coding-fintech-mobile.md` so the synthesis becomes a permanent part of the base.

---

## Architecture

```
                         ┌─────────────────────────────────────────┐
                         │            AGENTS.md                    │
                         │   Schema · Workflows · Behavioral Rules  │
                         └────────────────┬────────────────────────┘
                                          │ governs
                                          ▼
┌──────────────┐   ingest   ┌─────────────────────────┐   writes   ┌──────────────────────┐
│  Raw Sources │──────────▶ │       LLM Agent         │──────────▶ │   Knowledge Base     │
│              │            │                         │            │                      │
│  Articles    │            │  • Reads index          │            │  knowledge/          │
│  Papers      │            │  • Extracts structure   │            │  ├── concepts/   21  │
│  Transcripts │            │  • Updates cross-refs   │            │  ├── sources/     5  │
│  Reports     │            │  • Flags contradictions │            │  ├── entities/    6  │
│  Notes       │            │  • Maintains audit log  │            │  ├── analyses/    1  │
└──────────────┘            └─────────────────────────┘            │  └── overviews/   1  │
  gitignored                                                        └──────────────────────┘
  (source of truth)                                                   versioned · linked · typed
```

**The three layers:**

| Layer | Role | Mutability |
|---|---|---|
| `raw/` | Original source documents | Immutable — never modified |
| LLM agent | Reads `AGENTS.md`, maintains knowledge base | Stateless — governed by schema |
| `knowledge/` | Compiled, typed, interlinked knowledge graph | Append + update — versioned in git |

---

## Key Design Decisions

**Typed pages with enforced schema** — five distinct page types (`concept`, `entity`, `source`, `analysis`, `overview`), each with a mandatory section structure and YAML frontmatter. The schema is enforced by `AGENTS.md`, not by code — making it portable across any LLM.

**Contradiction tracking as a first-class feature** — when new sources conflict with existing claims, conflicts are flagged explicitly on both the source page and the affected concept page. Nothing is silently overwritten. The knowledge base knows what it doesn't know.

**Index-first navigation** — `knowledge/index.md` is a structured catalog the agent reads at the start of every session. At moderate scale (~100 sources, ~hundreds of pages), this outperforms embedding-based RAG for structured knowledge retrieval — no vector infrastructure required.

**Append-only audit log** — every ingest, query, lint, and update is recorded in `logs/ingestion.md` with a timestamp, pages changed, and key findings. Full operational history without a database.

**Agent-agnostic design** — `AGENTS.md` is plain English. It works with Claude, GPT-4, Gemini, or any LLM capable of reading instructions and editing files. No SDK dependency, no vendor lock-in.

---

## Features

- **5 typed page schemas** — `concept`, `entity`, `source`, `analysis`, `overview` with enforced section structure per type
- **Mandatory YAML frontmatter** — `title`, `type`, `tags`, `created`, `updated`, `sources` on every page; queryable and machine-readable
- **Graph-native cross-linking** — aggressive wiki-link cross-referencing creates a navigable knowledge graph visible in Obsidian's graph view
- **Explicit contradiction and gap tracking** — `## Contradictions` and `## Open Questions` sections on every page surface what is unresolved
- **4 agent workflows** — `ingest`, `query`, `lint`, `update` — each a deterministic step-by-step procedure in `AGENTS.md`
- **Append-only ingestion log** — full audit trail of every operation with timestamps, page counts, and findings
- **Reusable templates** — `templates/` folder with blank scaffolds for every page type; portable to any new domain or project
- **Git-native** — the knowledge base is a markdown repo; branching, history, and diffing work out of the box

---

## Current Knowledge Base

| Domain | Concept Pages | Key Topics |
|---|---|---|
| **Software Engineering** | 6 | Naming conventions, documentation, TDD + testing pyramid, code review, version control, performance |
| **Security** | 4 | Secure coding (OWASP/CERT/NIST/ISO), runtime security, vulnerability taxonomy, cryptography |
| **AI Agent Systems** | 3 | Agent tool design (5 principles), tool evaluation methodology, Model Context Protocol |
| **Mobile Development** | 6 | Mobile-first design, CI/CD pipelines, state management (Redux/Bloc), modular architecture, analytics |
| **Software Architecture** | 2 | Attribute-Driven Design (ADD), LLM-assisted architecture, human-in-the-loop design collaboration |

**5 sources ingested · 21 concept pages · 6 entity pages · 1 analysis · 1 domain overview · 5 domains**

![Knowledge Graph](docs/assets/graph.png)

*The knowledge graph in Obsidian — 34 pages across 5 domains. Red nodes are highest-linked (index, agent-tool-design, tool-evaluation). Every edge is a wiki-link maintained by the agent.*

---

## Quickstart

```bash
# 1. Clone and open in Obsidian
git clone https://github.com/akamazizi/ai-knowledge-engine
# Open the cloned folder as an Obsidian vault

# 2. Add a source
# Drop any article, paper, or notes file into raw/

# 3. Ingest it with Claude Code
# Open Claude Code in the repo root and say:
ingest raw/your-file.md

# 4. The agent will:
# → Surface key takeaways for your review
# → Create knowledge/sources/<slug>.md
# → Create or update concept and entity pages
# → Update knowledge/index.md
# → Append to logs/ingestion.md
```

**To query:** Ask any question in plain language. Answers cite specific knowledge pages and can be filed as `knowledge/analyses/` entries.

**To health-check:** Say `lint`. The agent audits for contradictions, orphan pages, missing links, and data gaps.

**Full operating instructions:** [`AGENTS.md`](./AGENTS.md)

---

## Repository Structure

```
ai-knowledge-engine/
├── README.md                  ← This file
├── AGENTS.md                  ← LLM operating manual — schema, workflows, behavioral rules
├── CLAUDE.md                  ← Claude Code session bootstrap (points to AGENTS.md)
├── .gitignore
│
├── knowledge/                 ← The compiled knowledge base (the main artifact)
│   ├── index.md               ← Master catalog; agent reads this first every session
│   ├── concepts/              ← Idea, framework, and pattern pages
│   ├── sources/               ← One summary page per ingested document
│   ├── entities/              ← Person, organization, product, and tool pages
│   ├── analyses/              ← Deep-dive, comparison, and synthesis pages
│   └── overviews/             ← Domain-level synthesis and reading maps
│
├── templates/                 ← Reusable page scaffolds
│   ├── concept.md
│   ├── source.md
│   ├── entity.md
│   ├── analysis.md
│   └── project.md
│
├── scripts/                   ← Utility scripts (stdlib only, no dependencies)
│   ├── lint_frontmatter.py    ← Validate YAML frontmatter on all knowledge/ pages
│   ├── search.py              ← Keyword/regex search with optional --type filter
│   └── stats.py               ← Page counts, most-linked concepts, orphan detection
│
├── .github/workflows/
│   └── lint.yml               ← CI: runs lint_frontmatter.py on every push
│
├── logs/
│   └── ingestion.md           ← Append-only operations log with timestamps
│
└── raw/                       ← Source documents — local only, gitignored
```

---

## Use Cases

**AI consulting and client engagements** — maintain a continuously updated knowledge base per engagement. Each new brief, research doc, or transcript ingested updates the relevant concept and entity pages automatically. Cross-engagement patterns surface through the linked graph.

**System design and architecture** — compile design patterns, ADRs (Architecture Decision Records), and trade-off analyses. Overview pages become living design documents. Link a decision to the source that informed it.

**Research and due diligence** — build domain expertise over weeks or months. Each new paper updates existing concept pages and explicitly flags where it contradicts prior sources. The overview page reflects current best understanding, not just the last thing read.

**Technical writing and thought leadership** — the analysis pages in `knowledge/analyses/` are ready-to-publish synthesis. The structured base means research is already organized when it is time to write.

**Team knowledge management** — feed meeting transcripts, Slack threads, and postmortems into the system. The wiki stays current because the LLM handles the maintenance that no one on the team wants to do.

---

## Design Philosophy

> *"The tedious part of maintaining a knowledge base is not the reading or the thinking — it is the bookkeeping."*

Humans abandon wikis because the maintenance burden grows faster than the value. Cross-references fall out of date. Contradictions accumulate silently. Summaries go stale. The graph decays.

LLMs do not get bored. They do not forget to update a cross-reference. They can touch 15 files in one pass without losing track of what changed. The maintenance cost is near zero — which means the knowledge base stays healthy and the value compounds indefinitely.

The human's job is to curate sources, ask good questions, and think about what it all means. The LLM's job is everything else.

This project is in the spirit of Vannevar Bush's 1945 Memex — a personal, associatively linked knowledge store where the connections between documents are as valuable as the documents themselves. The part Bush could not solve was who maintains the links. That problem is now solved.

---

## Tech Stack

| Layer | Tool | Purpose |
|---|---|---|
| Knowledge editor | [Obsidian](https://obsidian.md/) | Graph view, local editor, wiki-link rendering |
| LLM agent runtime | [Claude Code](https://www.anthropic.com/claude-code) | File editing, multi-step reasoning, schema adherence |
| Knowledge format | Markdown + YAML | Portable, human-readable, git-native |
| Source clipping | [Obsidian Web Clipper](https://obsidian.md/clipper) | Convert web articles to local markdown |
| Agent protocol | [Model Context Protocol](https://modelcontextprotocol.io/) | Tool integration layer for agent-tool communication |
| Version control | Git | Full history, branching, diffing of the knowledge base |

---

## Roadmap

- [x] Analysis pages — `knowledge/analyses/llm-assisted-vs-traditional-architecture.md` filed
- [x] GitHub Actions lint workflow — `.github/workflows/lint.yml` validates frontmatter on every push
- [x] Search script — `scripts/search.py` with keyword/regex search and `--type` filter
- [ ] Domain overview pages — one complete (`ai-agent-systems`); more domains to follow
- [ ] Multi-domain projects — `knowledge/projects/` for applying the base to real engagements
