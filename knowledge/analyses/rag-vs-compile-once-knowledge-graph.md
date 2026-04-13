---
title: "RAG vs. Compile-Once Knowledge Graph"
type: analysis
tags: [rag, knowledge-graph, retrieval, architecture, tradeoffs, memory]
created: 2026-04-13
updated: 2026-04-13
sources: [retrieval-augmented-generation-lewis-2020, writing-effective-tools-for-ai-agents, llm-assisted-add-architecture]
---

# RAG vs. Compile-Once Knowledge Graph

## Conclusion

**RAG and compile-once knowledge graphs are not competing solutions to the same problem — they are solutions to different problems.** RAG optimises for scale and freshness across large, dynamic corpora. Compile-once optimises for synthesis quality, consistency, and human auditability across a curated, slowly-evolving body of knowledge. Choosing between them requires clarity on what kind of knowledge you are managing and what queries you need to answer reliably.

The AI Knowledge Engine in this repository uses the compile-once pattern. That is the right choice for a knowledge base of hand-selected sources where synthesis quality and cross-referencing fidelity matter more than scale or update frequency.

---

## Sources

- [[sources/retrieval-augmented-generation-lewis-2020|Lewis et al. 2020]] — RAG architecture; parametric vs. non-parametric memory
- [[sources/writing-effective-tools-for-ai-agents|Aizawa (Anthropic)]] — agent tool design; evaluation-driven development; knowledge as compiled context
- [[sources/llm-assisted-add-architecture|Cervantes, Kazman, Cai 2025]] — context loss as state management failure; single living document as state management for LLM design sessions

---

## The Two Patterns

**RAG (Retrieval-Augmented Generation):** At query time, retrieve the most relevant passages from a large unstructured index, then condition generation on those passages. Knowledge is stored externally; the model's weights capture only reasoning capability, not factual content.

**Compile-Once:** Before any query, process every source into structured, cross-linked knowledge pages written by a human+LLM pair. At query time, read the pre-compiled pages. Knowledge is stored in explicit, human-readable documents.

---

## Comparison

| Dimension | RAG | Compile-Once |
|---|---|---|
| **Scale** | Millions of documents | Tens to hundreds of curated sources |
| **Query response** | Generated at query time — varies across runs | Reads pre-compiled pages — consistent and deterministic |
| **Knowledge freshness** | Index hot-swap; no retraining needed | Requires human curation to update |
| **Synthesis quality** | Generated synthesis; quality depends on retrieval + model | Pre-synthesised by human + LLM; explicitly cross-linked |
| **Cross-referencing** | Implicit, generated on the fly | Explicit wiki-links; traceable paths |
| **Auditability** | Retrieved passages visible, but synthesis opaque | Full page readable; every link traceable |
| **Provenance** | Retrieved passage IDs | Source slug + raw file path |
| **Contradictions** | Surfaced probabilistically, may be silently missed | Explicitly flagged during ingest and filed in Contradictions sections |
| **Infrastructure cost** | FAISS index, vector DB, retriever model | Plain Markdown files; zero infrastructure |
| **Setup cost** | High (index build, embedding, retriever fine-tuning) | Moderate (ingest workflow per source) |
| **Maintenance cost** | Low (re-index on update) | Moderate (human curation per update) |
| **Answer consistency** | Varies by retrieval ranking | Consistent — same page, same answer |

---

## When RAG Wins

1. **Large, dynamic corpora:** When the knowledge base is Wikipedia-scale or a live document stream (support tickets, news, internal documentation), compile-once becomes intractable.
2. **Factual recall at scale:** RAG's retrieval precision on open-domain QA (44.5% EM on NQ for RAG-626M) is competitive with fine-tuned models 17× larger.
3. **No curation budget:** When there is no human available to synthesise sources, RAG can operate from raw documents.
4. **Knowledge that changes daily:** Index hot-swapping means the knowledge base can be updated without changing the model or the query interface.

## When Compile-Once Wins

1. **Curated, slowly-evolving knowledge:** When sources are selected by a domain expert and change infrequently, the upfront curation cost pays for itself in persistent synthesis quality.
2. **Cross-domain synthesis:** The explicit wiki-link graph enables queries that traverse multiple domains — questions like "how does [[concepts/chain-of-thought-prompting|chain-of-thought]] connect to [[concepts/llm-assisted-architecture|LLM-assisted architecture]]?" are answered by following pre-compiled links, not by hoping retrieval surfaces the right combination.
3. **Human auditability:** Every claim is traceable to a specific page, which links to a specific source, which links to a specific raw file. RAG retrieval is opaque about which passage drove which clause of the generated answer.
4. **Contradiction tracking:** Compile-once ingestion explicitly surfaces and files contradictions between sources. RAG may silently present contradictory retrieved passages.
5. **Multi-LLM portability:** The compiled knowledge pages are plain Markdown — any LLM can read them. RAG requires a compatible retriever and embedding model.

---

## Cross-Source Insight

The context-loss finding from [[concepts/llm-assisted-architecture|LLM-Assisted Architecture]] is directly relevant here. The ADD paper identifies context loss — the LLM losing earlier design decisions as sessions grow longer — as the primary failure mode in LLM-assisted design work. The compile-once pattern solves a version of this problem: by pre-compiling knowledge into structured, cross-linked pages, the agent does not need to re-derive synthesis from raw sources in every session. The compiled knowledge base *is* the persistent context.

RAG, by contrast, generates synthesis at query time from retrieved chunks. Each query starts from scratch — the system has no memory of past synthesis. For a knowledge base where the value is in the *connections between sources*, not just the individual source content, this is a significant limitation.

---

## Recommendation

Use compile-once for knowledge bases where:
- Sources are curated and number in the tens to low hundreds
- Cross-domain synthesis and traceability are primary query requirements
- The knowledge base must be portable across different LLMs

Use RAG for knowledge bases where:
- Documents number in the thousands or more
- Knowledge changes frequently
- No human curation budget exists
- Exact recall on specific facts is the primary query type

Consider a hybrid: compile-once for the synthesised knowledge graph (concepts, analyses, overviews), with a RAG layer over the raw source documents for verbatim passage lookup. The two layers serve different query types and compose cleanly.
