---
title: "AI Agent Systems — Domain Overview"
type: overview
tags: [ai-agents, llm-engineering, tool-design, software-architecture, prompt-engineering, overview]
created: 2026-04-13
updated: 2026-04-13
sources: [writing-effective-tools-for-ai-agents, llm-assisted-add-architecture]
---

# AI Agent Systems — Domain Overview

## Thesis

**Explicit scaffolding — not raw model capability — is the primary mechanism that makes LLMs reliable in structured engineering tasks.**

This principle emerges independently from both sources in this domain, across two very different application areas:

- In tool design, [[concepts/agent-tool-design|Agent Tool Design]] shows that small, targeted improvements to tool descriptions — not model upgrades — drove Claude Sonnet 3.5 to SWE-bench Verified state-of-the-art performance. The LLM's behaviour is only as reliable as the explicit context it is given.
- In architecture design, [[concepts/llm-assisted-architecture|LLM-Assisted Architecture]] shows that providing an explicit ADD process description produces dramatically better designs than any unguided approach — even though the LLM has general architectural knowledge from training. The scaffold, not the model, is the differentiating factor.

The implication is practical: when LLM output is unreliable or inconsistent, the first question is not "is this model capable?" but "what explicit context, process, or structure is missing?"

---

## Reading Map

Read in this order to build a coherent mental model:

**1. Start with the fundamentals of how agents use tools**
→ [[concepts/agent-tool-design|Agent Tool Design]] — the 5 principles: selection, namespacing, context quality, token efficiency, prompt-engineered descriptions. Establishes the core insight that tools are interfaces designed for non-deterministic systems, not traditional APIs.

**2. Understand how to measure and improve agent performance**
→ [[concepts/tool-evaluation|Tool Evaluation]] — the prototype → eval → improve loop. Defines what "working" means in a probabilistic context and how to close the feedback loop systematically.

**3. Understand the protocol layer**
→ [[concepts/model-context-protocol|Model Context Protocol (MCP)]] — how tools are deployed and discovered in practice. Short but necessary for understanding how principles translate to production systems.

**4. See the scaffolding principle applied to architecture design**
→ [[concepts/attribute-driven-design|Attribute-Driven Design (ADD)]] — the design method used as explicit process scaffolding. Understand this before reading the LLM-assisted application of it.

**5. Read the synthesis**
→ [[concepts/llm-assisted-architecture|LLM-Assisted Architecture]] — how the tool design and architecture domains converge. The four-element approach, the failure modes as state management problems, and the evidence for ADD over all unguided approaches.

**6. For the applied comparison**
→ [[analyses/llm-assisted-vs-traditional-architecture|LLM-Assisted vs. Traditional Architecture Design]] — cross-source synthesis; six dimensions; recommendation section.

---

## Key Entities

- [[entities/anthropic|Anthropic]] — creator of Claude, MCP, and Claude Code; source of the tool design principles
- [[entities/ken-aizawa|Ken Aizawa]] — Anthropic engineer; primary author of the tool design article

---

## Key Concepts

| Concept | One-line summary |
|---|---|
| [[concepts/agent-tool-design\|Agent Tool Design]] | 5 principles for designing tools for non-deterministic LLM agents |
| [[concepts/tool-evaluation\|Tool Evaluation]] | Prototype → eval → improve loop; the TDD equivalent for probabilistic systems |
| [[concepts/model-context-protocol\|Model Context Protocol]] | Anthropic's open protocol for connecting agents to tools at scale |
| [[concepts/attribute-driven-design\|Attribute-Driven Design]] | Iterative architecture method; 7-step iteration cycle driven by quality attributes |
| [[concepts/llm-assisted-architecture\|LLM-Assisted Architecture]] | LLM as collaborative design partner; explicit scaffolding; human-in-the-loop |

---

## Open Questions

- **Scaling context:** Both tool design and architecture design hit context window limits at scale. How does the scaffolding approach adapt as sessions grow longer and systems more complex?
- **Fine-tuned specialist models:** Would an architect LLM fine-tuned on ADD literature and pattern catalogs outperform the persona + process description approach? At what cost?
- **Cross-LLM consistency:** Tool design and architecture design experiments used Claude. Do the same scaffolding principles hold with GPT-4, Gemini, or open-weight models?
- **Vibe architecting threshold:** The ADD paper explicitly rejects autonomous design today. What capability or context-management improvements would make autonomous design viable, and what would need to remain human-supervised?
- **Evaluation for open-ended tasks:** Both domains struggle with verifying quality for complex outputs. Tool evals use accuracy metrics; architecture evals use expert judges. Neither scales cheaply. What does a scalable, automated quality signal look like for complex generative tasks?

---

## Gaps

Sources not yet ingested that would materially strengthen this domain:

- **A multi-agent coordination paper** — current knowledge covers single-agent tool use and single-LLM design sessions. Multi-agent systems (agent orchestration, agent-to-agent communication, shared context management) are entirely absent.
- **An LLM safety / alignment source** — the knowledge base has no coverage of agent failure modes from a safety perspective: prompt injection, goal misgeneralization, or unsafe tool use in agentic settings.
- **A source on retrieval-augmented generation (RAG)** — RAG is the alternative architectural pattern to the index-first approach used in this knowledge base. Understanding the tradeoffs requires a dedicated source.
- **Empirical comparison across LLM providers** — every source in this domain used Claude. A source comparing tool use or reasoning quality across models would either validate or challenge the generalizability of current findings.
- **A source on agent memory and context management** — context loss is identified as the primary failure mode in LLM-assisted architecture but is treated as an unsolved problem. A dedicated source on external memory, context compression, or RAG-augmented agents would directly address the most pressing open question.
