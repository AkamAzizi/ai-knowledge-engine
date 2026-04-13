---
title: "Attribute-Driven Design (ADD)"
type: concept
tags: [software-architecture, add, system-design, quality-attributes, design-method, iterative-design]
created: 2026-04-13
updated: 2026-04-13
sources: [llm-assisted-add-architecture]
---

# Attribute-Driven Design (ADD)

## Definition

Attribute-Driven Design (ADD) is a structured, iterative method for designing software architectures that explicitly satisfies architectural drivers — quality attributes, primary functional requirements, constraints, and concerns. Rather than producing a design in a single pass, ADD decomposes the design across multiple focused iterations, each addressing a prioritized subset of drivers. The method provides the architect with clear steps, artifacts, and stopping criteria.

## How It Works

### Architectural Drivers

The inputs to every ADD session are prioritized architectural drivers:

| Driver type | Description | Example |
|---|---|---|
| Primary functional requirements | Core use cases that drive structural decisions | "Users can purchase tickets in real time" |
| Quality attribute scenarios | Measurable non-functional requirements with stimulus, environment, and response measure | "System serves 10,000 concurrent users at <2s response time" |
| Constraints | Fixed decisions that limit design options | "Must deploy on AWS; must use existing identity service" |
| Concerns | Development concerns not in formal requirements | "Establish CI/CD; avoid technical debt; log errors" |

Prioritization — by customer importance and implementation difficulty — determines which drivers are addressed in early iterations and which are deferred.

### The 7 Steps of an ADD Iteration

```
Step 1  Review architectural drivers (inputs)          ← first iteration only
Step 2  Establish the iteration goal                   ← select key drivers for this iteration
Step 3  Choose elements to refine or decompose         ← identify what to break down
Step 4  Select design concepts                         ← patterns, tactics, frameworks, cloud resources
Step 5  Instantiate elements + sketch views            ← create structures, assign responsibilities, define interfaces
Step 6  Record design decisions                        ← rationale, discarded alternatives
Step 7  Analyse the iteration                          ← assess driver satisfaction; decide if more iterations needed
```

**Steps 4 and 5 are the hardest.** Step 4 requires selecting from a vast catalog of design patterns, reference architectures, tactics, and externally developed components. Step 5 requires correctly instantiating and connecting those elements into concrete structures. These are precisely the steps where LLM assistance provides the most value — and where errors from insufficient context are most consequential. See [[concepts/llm-assisted-architecture|LLM-Assisted Architecture]].

### The Iteration Plan

Before executing design iterations, an iteration plan is created that maps each iteration to a goal and set of drivers. This serves two purposes:
1. **Scope control** — each iteration addresses a defined set of concerns, preventing scope creep and over-engineering (Big Design Up Front).
2. **Stopping criteria** — the architect knows when the design is complete. Without a plan, there is a risk of indefinite design elaboration.

When used with an LLM, the iteration plan creation is an instance of Plan-and-Solve prompting: the LLM is asked to plan before it executes, producing better-structured output.

### Key Artifacts

| Artifact | Contents | Mutability |
|---|---|---|
| Architectural drivers document | Prioritized functional requirements, QA scenarios, constraints, concerns | Input — may be clarified but not changed arbitrarily |
| Domain model | Key entities and relationships (DDD or simpler) | Created before iteration 1 |
| Iteration plan | Iteration goals and drivers per iteration | Created before iteration 1; may be revised |
| Iteration documents | Steps 2–7 outputs per iteration; design rationale | Created per iteration |
| Architecture document | Single living document; C4-style views, interfaces, design decisions | Updated across all iterations |

### The Single Living Document Pattern

Maintain one centralized architecture document that is modified across all design iterations — rather than relying on per-iteration documents alone. This document gives both architect and LLM a complete, consistent view of the current design state at every step.

Per-iteration-only documentation leads to fragmented outputs: each iteration produces structures focused on its own drivers, with no coherent overarching design. The single document is both an architectural record and a **state management mechanism** for the design session.

## Key Sources

- [[sources/llm-assisted-add-architecture|LLM-Assisted ADD Architecture (Cervantes et al., 2025)]] — describes ADD and its application as LLM scaffolding; provides case studies with Claude Sonnet 3.7

## Related Concepts

- [[concepts/llm-assisted-architecture|LLM-Assisted Architecture]] — how ADD is used as the explicit process scaffold for LLM-guided design
- [[concepts/modular-architecture|Modular Architecture]] — ADD is architecture-pattern-agnostic but guides pattern selection; case studies produced microservices, CQRS, and Clean Architecture
- [[concepts/tool-evaluation|Tool Evaluation]] — ADD step 7 (are drivers satisfied?) is analogous to the eval loop: define success criteria first, then measure and iterate

## Open Questions

- How does ADD compare to arc42, C4 + ADRs, or TOGAF as architecture methodology and documentation framework?
- At what system complexity does a full 7-step ADD process pay off vs. a lighter-weight approach?
- How does ADD handle emergent architectural decisions made during implementation that weren't anticipated at design time?
- How should ADD iteration cadence be structured in agile teams — a few iterations upfront, then revisited per sprint?
