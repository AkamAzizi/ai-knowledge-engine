---
title: "Retrieval-Augmented Generation (RAG)"
type: concept
tags: [rag, retrieval, generation, knowledge, memory, vector-search, nlp]
created: 2026-04-13
updated: 2026-04-13
sources: [retrieval-augmented-generation-lewis-2020]
---

# Retrieval-Augmented Generation (RAG)

## Definition

RAG is an architectural pattern for knowledge-intensive language tasks that augments a language model's parametric memory (knowledge encoded in weights) with non-parametric memory (an external document index queried at runtime). The model retrieves relevant passages before generating a response, grounding output in retrieved evidence rather than relying solely on knowledge baked into model weights during training.

## How It Works

A RAG system has two components:

**Retriever:** Given a query, encodes it into a dense vector and searches a pre-built document index (typically FAISS) for the top-k most similar passages. The original implementation uses Dense Passage Retrieval (DPR) — a bi-encoder that independently encodes queries and passages.

**Generator:** A seq2seq model (BART in the original paper) that conditions on both the original query and the retrieved passages to produce the final output.

Two formulations exist:
| Variant | Description | When to use |
|---|---|---|
| RAG-Sequence | Same retrieved passages for entire output | When the full answer draws from one context |
| RAG-Token | Different passages can inform each generated token | When the answer draws from multiple distinct sources |

**Index hot-swapping** is a key operational advantage: because knowledge is external, the index can be updated or fully replaced without retraining the generator. Parametric-only models require full retraining to update knowledge.

## Key Sources

- [[sources/retrieval-augmented-generation-lewis-2020|Lewis et al. 2020]] — original RAG paper; DPR + BART; NeurIPS 2020 SOTA on NQ, TriviaQA, WebQuestions

## Related Concepts

- [[concepts/react-framework|ReAct]] — extends retrieval into agentic loops: rather than one retrieve-then-generate step, ReAct interleaves retrieval actions with explicit reasoning traces throughout execution
- [[concepts/chain-of-thought-prompting|Chain-of-Thought Prompting]] — orthogonal axis: CoT improves reasoning quality; RAG improves knowledge access; they compose (ReAct uses both)
- [[concepts/agent-tool-design|Agent Tool Design]] — in agentic settings, RAG retrieval is often packaged as a tool; the quality of tool descriptions shapes how well agents invoke it
- [[concepts/modular-architecture|Modular Architecture]] — RAG is a two-module architecture; the retriever and generator can be independently updated or swapped

## RAG vs. Compile-Once Knowledge Graph

This project uses the opposite pattern to RAG — see [[analyses/rag-vs-compile-once-knowledge-graph|RAG vs. Compile-Once Knowledge Graph]] for a full comparison. In brief:

| Dimension | RAG | Compile-Once |
|---|---|---|
| Knowledge update | Replace the index | Human curation required |
| Query consistency | Varies by retrieval | Deterministic |
| Auditability | Retrieved passages visible | Full page readable |
| Scale | Millions of documents | Tens to hundreds of pages |
| Synthesis | Generated at query time | Pre-synthesised by human + LLM |

## Open Questions

- At what corpus size does the compile-once approach break down, and does RAG scale gracefully beyond Wikipedia-sized indexes?
- How does RAG perform on structured knowledge (tables, schemas, code) vs. free text?
- Multi-hop reasoning is a known RAG weakness — how do systems like FiD, Self-RAG, and FLARE address it?
