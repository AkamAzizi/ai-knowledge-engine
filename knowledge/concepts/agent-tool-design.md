---
title: "Agent Tool Design"
type: concept
tags: [ai-agents, tool-design, mcp, llm-engineering, context-efficiency]
created: 2026-04-13
updated: 2026-04-13
sources: [writing-effective-tools-for-ai-agents]
---

# Agent Tool Design

## Definition

The discipline of designing software tools specifically for use by LLM agents — distinct from writing APIs or functions for deterministic software systems. Because agents are non-deterministic and context-limited, tools must be built with different affordances than traditional software interfaces.

## How It Works

### The Fundamental Difference

| Traditional software | Agent tools |
|---|---|
| Deterministic — same input → same output | Non-deterministic — agents vary behavior with identical inputs |
| Memory is cheap and abundant | Context is limited and precious |
| Consumes all returned data efficiently | Wastes limited context on irrelevant information |
| Strict API contract | Probabilistic interface — agents may misuse, hallucinate, or skip tools |

**Key implication:** a tool that dumps all contacts into context (for the agent to search through) is wrong. A `search_contacts` tool that returns only the relevant result is right — same reasoning a human would apply.

### The 5 Principles

**1. Choose the right tools**
- Fewer, targeted tools beat many overlapping ones.
- Tools should match natural human task subdivisions.
- Consolidate multi-step workflows into a single tool call:
  - `schedule_event` instead of `list_users + list_events + create_event`
  - `get_customer_context` instead of separate `get_customer_by_id + list_transactions + list_notes`
  - `search_logs` instead of `read_logs` (returns relevant lines + context only)
- Too many overlapping tools distract agents from efficient strategies.

**2. Namespace tools**
- Group related tools under consistent prefixes or suffixes by service and resource.
- Example: `asana_projects_search`, `asana_users_search`, `jira_search`
- Reduces confusion when agents have access to hundreds of tools across many [[concepts/model-context-protocol|MCP]] servers.
- Prefix vs. suffix choice has measurable, non-trivial effects — test both against your eval.

**3. Return meaningful context**
- Return only high-signal fields. Prefer:
  - `name` over `uuid`
  - `file_type` over `mime_type`
  - `image_url` over `256px_image_url`
- Resolving alphanumeric UUIDs to semantic identifiers significantly reduces hallucinations in retrieval tasks.
- Use a `response_format` enum (DETAILED / CONCISE) when agents need both human-readable names and technical IDs for downstream tool calls.
- Response structure (XML vs JSON vs Markdown) affects eval performance — no universal best; test for your domain.

**4. Optimize for token efficiency**
- Implement pagination, range selection, filtering, truncation with sensible defaults.
- Claude Code restricts tool responses to 25,000 tokens by default.
- When truncating, include instructions steering agents toward efficient follow-up strategies.
- Error responses must be actionable: explain what went wrong and how to fix it. Opaque tracebacks or error codes are actively harmful.

**5. Prompt-engineer descriptions**
- Treat tool descriptions like onboarding documentation for a new hire.
- Make implicit context explicit: query formats, niche terminology, resource relationships.
- Use unambiguous parameter names: `user_id` not `user`, `event_start_date` not `start`.
- Small refinements to descriptions yield dramatic performance improvements.
- **Key example:** Claude Sonnet 3.5 hit SWE-bench Verified state-of-the-art after description refinements alone — no code changes.
- Web search tool example: Claude was appending `2025` to all queries until description was fixed.

### Tool Design is Iterative
Tool design is not a one-shot task. The correct workflow is:
1. Build a prototype
2. Run evaluations (see [[concepts/tool-evaluation|Tool Evaluation]])
3. Let agents analyze transcripts and suggest improvements
4. Repeat until held-out test performance is strong

## Key Sources

- [[sources/writing-effective-tools-for-ai-agents|Writing Effective Tools for AI Agents — Using AI Agents]] — primary and sole source; Anthropic's internal learnings

## Related Concepts

- [[concepts/tool-evaluation|Tool Evaluation]] — the methodology for measuring and improving tool performance
- [[concepts/model-context-protocol|Model Context Protocol (MCP)]] — the protocol through which tools are exposed to agents
- [[concepts/naming-conventions|Naming Conventions]] — namespacing tools is an extension of naming principles from general software development

## Open Questions

- How do these principles change as LLM context windows expand significantly?
- Are there tool design patterns for real-time / streaming data sources?
- How does tool design differ between Claude models vs. other LLMs?
- What is the relationship between MCP tool annotations (destructive/open-world flags) and these design principles?
