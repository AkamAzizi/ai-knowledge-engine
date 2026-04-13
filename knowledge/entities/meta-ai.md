---
title: "Meta AI"
type: entity
tags: [meta, facebook, ai-research, nlp, faiss, bart, dpr]
created: 2026-04-13
updated: 2026-04-13
sources: [retrieval-augmented-generation-lewis-2020]
---

# Meta AI

## Overview

Meta AI (formerly Facebook AI Research, FAIR) is the AI research division of Meta Platforms. It is responsible for foundational work in NLP, computer vision, and AI infrastructure, including several components central to the RAG architecture.

## Key Contributions

- **DPR (Dense Passage Retrieval):** Bi-encoder dense retrieval model used as the retriever component in RAG; enables efficient semantic search over millions of passages
- **BART:** Seq2seq pre-trained model used as the generator in RAG; fine-tuned for knowledge-intensive generation tasks
- **FAISS:** Open-source library for efficient similarity search and clustering of dense vectors; the index infrastructure underlying DPR-based retrieval at scale
- **RAG Architecture:** [[concepts/retrieval-augmented-generation|Retrieval-Augmented Generation]] — hybrid parametric/non-parametric memory for knowledge-intensive NLP tasks

## Appearances

- [[sources/retrieval-augmented-generation-lewis-2020|Lewis et al. 2020]] — RAG, DPR, BART, NeurIPS 2020

## Related

- [[entities/anthropic|Anthropic]] — AI research lab; creator of Claude, MCP, Claude Code
- [[entities/google-brain|Google Brain]] — AI research lab; origin of Chain-of-Thought and ReAct
