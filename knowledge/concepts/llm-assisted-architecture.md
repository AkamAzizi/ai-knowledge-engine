---
title: "LLM-Assisted Architecture"
type: concept
tags: [llm, software-architecture, ai-agents, prompt-engineering, human-in-the-loop, system-design, add, state-management]
created: 2026-04-13
updated: 2026-04-13
sources: [llm-assisted-add-architecture]
---

# LLM-Assisted Architecture

## Definition

The practice of using large language models as collaborative partners in software architecture design — guided by explicit process scaffolding, structured prompting patterns, and active human oversight at each design step. Distinct from autonomous design: the LLM proposes and documents; the architect reviews, corrects, and decides. The value is acceleration and documentation quality, not autonomy.

## How It Works

### The Core Insight: Explicit Process Scaffolding

LLMs cannot reliably perform complex, multi-step design reasoning from prompting alone — they hallucinate about methodology, mix abstraction levels, and lose context across long sessions. The solution is **explicit process scaffolding**: providing the LLM with a complete, step-by-step description of the design methodology (e.g., ADD) rather than relying on what it absorbed during training.

This is the architecture design parallel to [[concepts/agent-tool-design|Agent Tool Design]]: just as tools must be explicitly described to make LLM tool use predictable, design processes must be explicitly provided to make design reasoning reliable. In both cases, the LLM has general knowledge from training, but that knowledge is insufficient for consistent, structured execution. The explicit scaffold — not the LLM's training — is the mechanism that produces reliable output.

> **Key finding:** Asking the LLM to design using ADD from training data alone results in hallucinated or incorrect ADD steps. Providing the ADD description explicitly produces dramatically better, consistent results.

### The Four-Element Approach

Effective LLM-assisted architecture design requires four structured inputs working together:

| Element | Role | Prompting technique |
|---|---|---|
| **Process description** | Provides step-by-step design methodology (ADD) | Chain-of-Thought |
| **Architect persona** | Scopes expertise, responsibilities, constraints | Persona pattern |
| **Prioritized architectural drivers** | Defines what the design must satisfy | Context injection |
| **Iteration plan** | Structures work, scopes each iteration, prevents BDUF | Plan-and-Solve |

The iteration plan is the most underrated element: by asking the LLM to plan design iterations *before* executing them, the architect and LLM agree on scope upfront — preventing the LLM from producing an over-engineered monolith in a single pass and creating natural human review checkpoints.

### Human-in-the-Loop: Non-Negotiable

Architecture design cannot be delegated to an LLM. The value of this approach is acceleration and documentation quality, not automation. A human architect must:

- Review LLM output **after every ADD step** before proceeding
- Correct context omissions, abstraction inconsistencies, and hallucinated components
- Make final design decisions — the LLM proposes, the architect disposes
- Catch when the LLM deviates from the iteration plan or mixes abstraction levels

**The risk of skipping human review is not just poor quality** — an inexperienced architect may accept structurally flawed decisions that introduce technical debt from the start. The paper found that even when the LLM's "out of the box" output was impressive, it contained inconsistencies that required expert correction.

### The Single Living Document as State Management

A centralized architecture document — modified by the LLM across all design iterations — is essential for coherent output. This is fundamentally a **state management pattern**: the document externalizes the design state that the LLM cannot reliably hold in its context window across a multi-hour, multi-file design session.

Without this pattern:
- Each iteration produces structures focused on its own drivers, with no coherent whole
- The LLM loses track of elements defined in earlier iterations
- Diagrams become inconsistent across iterations
- There is no authoritative record of the current design state

The single living document is the architecture-domain equivalent of the centralized state store in [[concepts/state-management|State Management]] patterns: a single source of truth that every iteration reads from and writes back to.

### LLM Limitations as State Management Failures

The recurring failure modes are not random errors — they are predictable state management failures caused by context window limits and instruction drift over long sessions:

| Observed failure | Root cause |
|---|---|
| Forgot to update architecture document | Document state not in active context window |
| Mixed abstraction levels across iterations | No persistent record of which layer was being addressed |
| Omitted earlier elements from diagrams | Context loss as session grows longer |
| Sequence diagrams inconsistent with container diagrams | No cross-document consistency check mechanism |
| Forgot to pause after each ADD step | Instruction drift over a long session |
| Used different architectural style mid-design | No mechanism to enforce pattern consistency |

Understanding these as **state management failures** — not intelligence failures — suggests concrete mitigations: explicit context re-injection at each prompt, frequent re-grounding in the architecture document, and structured check-in prompts that recap the current design state.

### Evidence: ADD vs. No-ADD

The paper directly tested ADD-scaffolded design against three unguided approaches:

| Approach | What was provided | Result quality |
|---|---|---|
| Zero-shot | Requirements only | Least detailed; integration errors; incomplete diagrams |
| Empty template | Requirements + document structure | Similar errors; slightly more structured output |
| Template with instructions | Requirements + structure + embedded instructions | Better, but LLM only partially followed instructions |
| **ADD + iteration plan + persona** | Full scaffold | Comprehensive, multi-view, consistent; partially satisfies QA drivers |

The structured process — not the template, not the persona — is the differentiating factor. The ADD scaffold gave the LLM a reasoning framework it could follow step-by-step, producing output that professional architects described as more comprehensive than many real-project architecture documents.

## Key Sources

- [[sources/llm-assisted-add-architecture|LLM-Assisted ADD Architecture (Cervantes et al., 2025)]] — primary source; case studies with Claude Sonnet 3.7 in Cursor IDE; two validated case studies

## Related Concepts

- [[concepts/attribute-driven-design|Attribute-Driven Design (ADD)]] — the design method that provides the process scaffold
- [[concepts/agent-tool-design|Agent Tool Design]] — direct parallel: process descriptions scaffold design reasoning; tool descriptions scaffold tool use. Both make LLM behavior predictable through explicit, externalized context — not training data assumptions.
- [[concepts/tool-evaluation|Tool Evaluation]] — the ATAM-like scenario-based architect evaluation in the paper is a domain-specific instance of the structured validation loop: define expected outcomes, run the process, measure satisfaction, iterate
- [[concepts/state-management|State Management]] — context loss and abstraction mixing in LLM design sessions are state management failures; the single living document is the state store mitigation
- [[concepts/modular-architecture|Modular Architecture]] — LLM-assisted ADD consistently produces microservices, CQRS, and Clean Architecture as default patterns; reliable pattern selection is one of ADD's strengths in practice

## Open Questions

- Can a fine-tuned architect LLM (trained on ADD literature, pattern catalogs, architecture case studies) outperform the persona + process description approach?
- How does this compare to RAG-based alternatives like DRAFT (retrieval-augmented generation + fine-tuning for architectural design decisions)?
- At what point in session length does context degradation become critical, and how can that threshold be measured and managed?
- Is fully autonomous architecture design ("vibe architecting") eventually possible with sufficiently large context windows and better context management?
- How should the human review checkpoints be structured to be both efficient and thorough — what is the minimum viable review at each ADD step?
