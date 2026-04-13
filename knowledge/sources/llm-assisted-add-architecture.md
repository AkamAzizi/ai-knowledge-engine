---
title: "An LLM-Assisted Approach to Designing Software Architectures Using ADD"
type: source
tags: [llm, software-architecture, add, system-design, ai-agents, prompt-engineering, human-in-the-loop]
created: 2026-04-13
updated: 2026-04-13
sources: [llm-assisted-add-architecture]
---

**Author:** Humberto Cervantes (UAM Iztapalapa), Rick Kazman (University of Hawaii at Manoa), Yuanfang Cai (Drexel University)
**Published:** 2025 — arXiv:2506.22688
**Origin:** Academic preprint
**Raw source:** `raw/An LLM-assisted approach to designing software architectures using ADD.md`

## Summary

This paper proposes an LLM-assisted approach to software architecture design using the Attribute-Driven Design (ADD) method. The core method provides four structured inputs to the LLM: an explicit ADD process description, an architect persona, prioritized architectural drivers, and a Plan-and-Solve iteration plan. These scaffolds guide the LLM to collaboratively produce architecture artifacts with a human architect across multiple design iterations, with the human reviewing and correcting output at each ADD step. Two case studies — a Hotel Pricing System and an Event Ticketing System — validate the approach against proven solutions and professional architect evaluation. Results show LLM-generated designs are broadly consistent with established solutions but only partially satisfy quality attribute drivers without active human correction. The paper explicitly rejects autonomous "vibe architecting" in favour of structured human-LLM collaboration.

## Key Points

- **Explicit process scaffolding is the primary mechanism:** LLMs hallucinate about ADD steps when prompted from training data alone. The ADD description must be provided explicitly — the LLM cannot be trusted to reconstruct the methodology from memory.
- **Four-element approach:** (1) ADD process description (Chain-of-Thought), (2) architect persona (roles, specialties, constraints), (3) prioritized architectural drivers (functional requirements, QA scenarios, constraints, concerns), (4) Plan-and-Solve iteration plan.
- **Iteration plan prevents BDUF:** Asking the LLM to plan iterations before designing creates natural human review checkpoints and avoids over-engineering. Without it, the LLM risks producing an excessively complex Big Design Up Front.
- **Single living document is critical:** A centralized architecture document modified across all iterations — not per-iteration documents alone — is required for coherent output. Per-iteration-only documentation leads to fragmented structures with no consistent whole.
- **ADD outperforms all zero-shot approaches:** ADD + iteration plan produces significantly more detailed, comprehensive, and consistent designs than zero-shot, empty-template, or template-with-instructions prompting. The structured process is the differentiating factor, not the template or persona alone.
- **Context loss and abstraction mixing are the primary failure modes:** The LLM frequently forgot to update the architecture document, mixed abstraction levels across iterations, and omitted elements from context. These are state management failures in a long, multi-file design session — not intelligence failures.
- **Partial driver satisfaction:** Professional architect evaluation found most drivers only partially addressed without active human correction — particularly around sequence diagram consistency and cross-service recovery mechanisms.
- **Human oversight is non-negotiable:** The value is in accelerated, high-quality documentation produced in a couple of hours, not autonomous design. An inexperienced architect risks accepting flawed decisions uncritically.
- **RQ3 confirmed:** Using ADD makes a significant, measurable difference. The structured process — more than any individual prompt technique — is what produces reliable output.

## Entities

- Humberto Cervantes — primary author; co-creator of ADD; Universidad Autónoma Metropolitana
- Rick Kazman — co-author; University of Hawaii; co-author of *Software Architecture in Practice*
- Yuanfang Cai — co-author; Drexel University

## Concepts

- [[concepts/attribute-driven-design|Attribute-Driven Design (ADD)]] — the design method applied as scaffolding
- [[concepts/llm-assisted-architecture|LLM-Assisted Architecture]] — the core contribution of the paper
- [[concepts/agent-tool-design|Agent Tool Design]] — parallel: process descriptions scaffold LLM behavior the same way tool descriptions do
- [[concepts/tool-evaluation|Tool Evaluation]] — the ATAM-like scenario-based evaluation mirrors the structured validation loop
- [[concepts/modular-architecture|Modular Architecture]] — case study designs produced microservices, CQRS, Clean Architecture
- [[concepts/state-management|State Management]] — context loss and abstraction mixing are state management failures; single living document is the mitigation

## Contradictions

None with existing knowledge. The paper's central finding — that explicit process scaffolding makes LLM behavior reliable — directly extends the `agent-tool-design` principle that explicit descriptions outperform assumptions from training. The paper generalizes this from tool descriptions to entire design methodologies.

## Questions

- How does this approach scale to very large systems with hundreds of requirements and many teams?
- Can a fine-tuned architect LLM (trained on ADD literature, pattern catalogs, case studies) outperform the persona + process description approach?
- What is the minimum architect experience level needed to effectively review and correct LLM outputs at each step?
- How does this approach compare to DRAFT (RAG + fine-tuning for architectural design decisions) or ARLO (integer linear programming on requirements)?
- The experiments used Claude Sonnet 3.7 in Cursor. Would results differ significantly with other LLMs or IDE-agnostic prompting?
