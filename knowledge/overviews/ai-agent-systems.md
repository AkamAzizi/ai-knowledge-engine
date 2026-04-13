---
title: "AI Agent Systems — Domain Overview"
type: overview
tags: [ai-agents, llm-engineering, tool-design, software-architecture, prompt-engineering, overview]
created: 2026-04-13
updated: 2026-04-13
sources: [writing-effective-tools-for-ai-agents, llm-assisted-add-architecture, react-reasoning-acting-yao-2022, chain-of-thought-prompting-wei-2022, retrieval-augmented-generation-lewis-2020]
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

**7. Understand how scaffolding manifests at the prompting level**
→ [[concepts/chain-of-thought-prompting|Chain-of-Thought Prompting]] — intermediate reasoning steps as the prompting-level instance of the scaffolding principle. Emergent at scale; the "Thought" in ReAct is CoT applied to agentic execution.

**8. See scaffolding and retrieval combined in an agent loop**
→ [[concepts/react-framework|ReAct]] — interleaved Thought-Action-Observation traces. Explains why tool descriptions shape agent reasoning (not just action selection), and how retrieval grounding prevents hallucination.

**9. Understand the alternative to compile-once knowledge management**
→ [[concepts/retrieval-augmented-generation|Retrieval-Augmented Generation]] — parametric + non-parametric hybrid memory. The architectural counterpoint to this project's compile-once approach; the comparison is filed in [[analyses/rag-vs-compile-once-knowledge-graph|RAG vs. Compile-Once Knowledge Graph]].

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
| [[concepts/chain-of-thought-prompting\|Chain-of-Thought Prompting]] | Intermediate reasoning steps elicit complex multi-step reasoning; emergent at ~100B+ scale |
| [[concepts/react-framework\|ReAct]] | Interleaved Thought-Action-Observation traces; grounding prevents hallucination |
| [[concepts/retrieval-augmented-generation\|Retrieval-Augmented Generation]] | Hybrid parametric + non-parametric memory; index hot-swapping; alternative to compile-once |

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
- **Empirical comparison across LLM providers** — every source in this domain used Claude or Google's PaLM. A source comparing tool use or reasoning quality across models (GPT-4, Gemini, open-weight) would either validate or challenge the generalizability of current findings.
- **A source on context compression and long-context management** — context loss remains the primary failure mode in LLM-assisted architecture. External memory, compression, and RAG-augmented agents are now covered at the concept level, but no dedicated empirical source exists for long-context management strategies.

_Previously identified gaps now addressed:_ RAG ([[sources/retrieval-augmented-generation-lewis-2020|Lewis et al. 2020]]), agent memory/context ([[concepts/retrieval-augmented-generation|RAG concept]] + [[analyses/rag-vs-compile-once-knowledge-graph|analysis]]), and reasoning foundations ([[sources/chain-of-thought-prompting-wei-2022|Wei et al. 2022]], [[sources/react-reasoning-acting-yao-2022|Yao et al. 2022]]).
