---
title: "Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks"
type: source
tags: [rag, retrieval, generation, nlp, knowledge-intensive, dense-retrieval, bart, dpr]
created: 2026-04-13
updated: 2026-04-13
sources: []
---

**Author:** Patrick Lewis, Ethan Perez, Aleksandra Piktus, et al.
**Published:** NeurIPS 2020
**Origin:** Facebook AI Research / University College London
**Raw source:** `raw/retrieval-augmented-generation-lewis-2020.md`

## Summary

RAG introduces a hybrid memory architecture for language generation: a pre-trained seq2seq generator ([[entities/meta-ai|Meta AI]]'s BART, ~406M parameters) combined with a non-parametric dense vector index over Wikipedia, accessed via Dense Passage Retrieval (DPR). By separating knowledge storage from model weights, RAG achieves state-of-the-art results on multiple open-domain QA benchmarks — including outperforming T5-11B (17× larger) on Natural Questions — while enabling index hot-swapping to update knowledge without retraining. The core insight is that explicit retrieval can substitute for massive model scaling.

## Key Points

- **Hybrid memory beats pure parametric or pure retrieval:** RAG outperforms both retrieve-then-extract systems and large seq2seq models on knowledge-intensive generation tasks
- **Index hot-swapping:** Because knowledge is stored in an external FAISS index rather than model weights, the index can be updated or replaced without retraining — directly solving the knowledge staleness problem
- **Two formulations:** RAG-Sequence (same retrieved passages for the full output) and RAG-Token (different passages per generated token); RAG-Token slightly outperforms
- **Parameter efficiency:** RAG-626M outperforms T5-11B on NQ (44.5% EM), TriviaQA (56.8% EM), and WebQuestions (45.5% EM)
- **Interpretability:** Retrieved passages provide provenance — the model's knowledge source is visible and auditable
- **Retrieval bottleneck:** If the DPR retriever fails to surface relevant passages, generation fails regardless of generator quality

## Entities

- [[entities/meta-ai|Meta AI]] (Facebook AI Research) — research lab behind RAG, DPR, and BART

## Concepts

- [[concepts/retrieval-augmented-generation|Retrieval-Augmented Generation]] — the architectural pattern introduced by this paper
- [[concepts/chain-of-thought-prompting|Chain-of-Thought Prompting]] — orthogonal technique: CoT improves reasoning; RAG improves knowledge access
- [[concepts/react-framework|ReAct]] — extends RAG-style retrieval into agentic decision loops with interleaved reasoning

## Contradictions

The compile-once knowledge graph pattern used in this project is architecturally opposite to RAG: RAG retrieves at query time from a large unstructured index; this project pre-digests sources into structured, cross-linked pages. Neither is universally superior — see [[analyses/rag-vs-compile-once-knowledge-graph|RAG vs. Compile-Once Knowledge Graph]] for the full comparison.

## Questions

- How does RAG perform when the knowledge base is structured (e.g., tables, code) rather than free text?
- Multi-hop reasoning is a known weakness — how do later systems (FiD, FLARE, Self-RAG) address this?
- At what corpus size does the compile-once approach become impractical, and does RAG degrade gracefully at that scale?
