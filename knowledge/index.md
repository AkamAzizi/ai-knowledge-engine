---
title: "Knowledge Index"
type: overview
tags: [meta, index]
created: 2026-04-13
updated: 2026-04-13
sources: []
---

# Knowledge Index

_Last updated: 2026-04-13 — 5 sources, 34 pages_

Master catalog of all knowledge pages. Read this first on every session to orient before querying or ingesting. Updated on every ingest, update, or lint operation. Full operations history in [`logs/ingestion.md`](../logs/ingestion.md).

---

## Sources
- [[sources/llm-assisted-add-architecture|An LLM-Assisted Approach to Software Architecture Design Using ADD]] — Cervantes, Kazman, Cai (2025); LLM-assisted ADD; explicit process scaffolding; human-in-the-loop; case studies with Claude Sonnet 3.7
- [[sources/coding-best-practices-and-guidelines|Coding Best Practices and Guidelines for Better Code]] — DataCamp tutorial by Amberle McKee; structure, documentation, performance, version control, testing, security
- [[sources/oligo-secure-coding-best-practices|Secure Coding: Top 7 Best Practices, Risks, and Future Trends]] — Oligo Security article by Mic McCully; deep security focus: input sanitization, obfuscation, least privilege, cryptography, vulnerability types, standards (OWASP/CERT/NIST/ISO), runtime security, future trends
- [[sources/writing-effective-tools-for-ai-agents|Writing Effective Tools for AI Agents — Using AI Agents]] — Anthropic engineering blog by Ken Aizawa; tool design for LLM agents: the 5 principles, evaluation-driven workflow, MCP, token efficiency, prompt-engineered descriptions
- [[sources/mobile-app-best-practices-2025|10 Best Practices for Mobile App Development in 2025]] — Wonderment Apps blog; mobile-first design, cross-platform frameworks, state management, CI/CD, modular architecture, user-centric design, analytics/monitoring

## Entities
- [[entities/amberle-mckee|Amberle McKee]] — DataCamp author; coding best practices tutorial
- [[entities/mic-mccully|Mic McCully]] — Oligo Security author; secure coding top 7 article
- [[entities/gal-elbaz|Gal Elbaz]] — Co-Founder & CTO of Oligo Security; expert contributor on secure coding and runtime security
- [[entities/oligo-security|Oligo Security]] — runtime application security company
- [[entities/ken-aizawa|Ken Aizawa]] — Anthropic engineer; agent tool design article
- [[entities/anthropic|Anthropic]] — creator of Claude, MCP, Claude Code; source of the agent tool design article

## Concepts

### Software Engineering & Best Practices
- [[concepts/naming-conventions|Naming Conventions]] — camelCase vs snake_case; meaningful names; consistency within a project
- [[concepts/code-documentation|Code Documentation]] — inline comments, docstrings, README files
- [[concepts/version-control|Version Control]] — Git workflows; branching, merging, pull requests, commit hygiene
- [[concepts/test-driven-development|Test-Driven Development]] — TDD cycle; testing pyramid; unit/integration/E2E tests; mobile frameworks (Espresso, XCTest) *(2 sources)*
- [[concepts/code-review|Code Review & Refactoring]] — code smells; refactoring; security-focused review
- [[concepts/performance-optimization|Performance Optimization]] — profile first; vectorization; chunking; mobile-specific: lazy loading, main thread, WebP *(2 sources)*

### Security
- [[concepts/secure-coding|Secure Coding]] — input sanitization, least privilege, cryptography, obfuscation, mobile security (Keychain, certificate pinning, OAuth 2.0) *(2 sources)*
- [[concepts/runtime-security|Runtime Security]] — production monitoring; RASP; DevSecOps integration
- [[concepts/vulnerability-types|Common Vulnerability Types]] — buffer overflows, integer overflows, format strings, race conditions, injection
- [[concepts/security-standards|Security Standards]] — OWASP, CERT, NIST SP 800-53/218, ISO/IEC 27001 Control 8.28

### AI Agent Systems
- [[concepts/agent-tool-design|Agent Tool Design]] — tools for non-deterministic LLM agents; 5 principles: selection, namespacing, context quality, token efficiency, prompt-engineered descriptions
- [[concepts/tool-evaluation|Tool Evaluation]] — prototype → eval → agent-assisted improvement loop; task design, metrics, verifiers
- [[concepts/model-context-protocol|Model Context Protocol (MCP)]] — Anthropic's open protocol for connecting agents to tools

### Software Architecture
- [[concepts/attribute-driven-design|Attribute-Driven Design (ADD)]] — iterative architecture method driven by quality attributes, functional requirements, constraints, and concerns; 7-step iteration cycle
- [[concepts/llm-assisted-architecture|LLM-Assisted Architecture]] — LLM as collaborative design partner; requires explicit process scaffolding (ADD), iteration plan, human-in-the-loop oversight, and single living document as state management

### Mobile App Development
- [[concepts/mobile-first-design|Mobile-First Design]] — design for smallest screen first; cross-platform frameworks (React Native, Flutter, .NET MAUI); hot reloading
- [[concepts/cicd-pipelines|CI/CD Pipelines]] — automated build/test/deploy; quality gates; app store deployment automation (TestFlight, Google Play)
- [[concepts/state-management|State Management]] — single source of truth; immutable state; Redux, Bloc, MVVM, MVI patterns
- [[concepts/modular-architecture|Modular Architecture]] — Clean Architecture, MVVM, MVI; dependency injection; module contracts; scales to large teams
- [[concepts/analytics-and-monitoring|Analytics and Monitoring]] — Firebase Analytics/Crashlytics; KPIs (DAU, retention, conversion); A/B testing; review cadence
- [[concepts/user-centric-design|User-Centric Design]] — user research, personas, journey mapping, prototype testing (Figma/Maze), post-launch feedback loops

## Analyses
- [[analyses/llm-assisted-vs-traditional-architecture|LLM-Assisted vs. Traditional Architecture Design]] — comparative analysis across speed, documentation quality, driver satisfaction, expertise requirements, failure modes, and scalability; includes cross-source insights and actionable recommendation

## Overviews
- [[overviews/ai-agent-systems|AI Agent Systems]] — domain synthesis across tool design and LLM-assisted architecture; thesis: explicit scaffolding is the primary mechanism for reliable LLM behaviour; reading map, gaps, open questions
