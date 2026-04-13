---
title: "Writing Effective Tools for AI Agents — Using AI Agents"
type: source
tags: [ai-agents, mcp, tool-design, evaluation, anthropic, llm-engineering]
created: 2026-04-13
updated: 2026-04-13
sources: [writing-effective-tools-for-ai-agents]
---

# Writing Effective Tools for AI Agents — Using AI Agents

**Author:** [[entities/ken-aizawa|Ken Aizawa]] (with contributions from [[entities/anthropic|Anthropic]] Research, MCP, Product Engineering, Applied AI teams)
**Origin:** Anthropic Engineering Blog
**Raw source:** `raw/Writing effective tools for AI agents—using AI agents.md`

---

## Summary

Tools are a new kind of software interface — not APIs written for deterministic systems, but contracts between deterministic code and non-deterministic agents. Because agents perceive and interact with tools differently than traditional software consumers, tool design requires a fundamentally different approach. This article describes Anthropic's methodology for writing effective tools: a prototype → evaluate → agent-assisted improvement loop, distilled into five key design principles. Most of the advice comes from Anthropic's own internal experience iterating on tools for Slack, Asana, and other workspace integrations — using Claude Code itself as the collaborator.

---

## Key Points

**What makes tools different**
- Traditional software: deterministic function calls produce identical outputs every time.
- Agent tools: agents may call a tool, answer from memory, ask a clarifying question, or hallucinate — varied behavior even with the same input.
- Agents have limited context; computer memory is cheap. Tools must do the filtering and synthesis work instead of dumping raw data into context.
- Tools that are ergonomic for agents tend to also be intuitive for humans.

**Workflow: Prototype → Evaluate → Improve**

1. **Prototype** — stand up tools quickly; wrap in a local MCP server or DXT to test in Claude Code or Claude Desktop. Give Claude documentation (llms.txt files) for any SDK it needs to understand.
2. **Evaluate** — generate dozens of realistic prompt/response pairs grounded in real-world complexity. Run programmatic evals using agentic while-loops. Collect: accuracy, runtime, token consumption, tool errors, tool call counts.
3. **Improve with agents** — paste eval transcripts into Claude Code; let it analyze failures and refactor tools. Repeat until strong held-out test performance.

**Strong vs. weak evaluation tasks**
- Strong: multi-step, realistic data, require chaining multiple tool calls (e.g. "Schedule a meeting with Jane, attach notes from last planning meeting, reserve a room")
- Weak: oversimplified, single-step, sandbox-like (e.g. "Schedule a meeting with jane@acme.corp next week")

**5 Principles for Effective Tools**

1. **Choose the right tools** — fewer, targeted tools beat many overlapping ones. Consolidate multi-step operations: `schedule_event` instead of `list_users + list_events + create_event`. `get_customer_context` instead of three separate get/list calls. Each tool should match how a human would naturally subdivide the task.

2. **Namespace tools** — prefix or suffix by service and resource (e.g. `asana_projects_search`, `jira_search`). Reduces confusion when agents have access to hundreds of tools across many MCP servers. Prefix vs. suffix choice has non-trivial measured effects — evaluate both.

3. **Return meaningful context** — return high-signal fields, not everything. Prefer `name`, `file_type`, `image_url` over `uuid`, `mime_type`, `256px_image_url`. Resolve alphanumeric UUIDs to semantic identifiers — dramatically reduces hallucinations in retrieval tasks. Use a `response_format` enum (DETAILED / CONCISE) to give agents control over verbosity when both human-readable and technical IDs are needed downstream.

4. **Optimize for token efficiency** — implement pagination, range selection, filtering, truncation with sensible defaults. Claude Code restricts tool responses to 25,000 tokens by default. When truncating, steer agents with helpful instructions. Error responses should be actionable (explain what went wrong and how to fix it) not opaque (no raw tracebacks or error codes).

5. **Prompt-engineer descriptions** — treat tool descriptions like onboarding a new hire: make implicit context explicit (query formats, niche terminology, resource relationships). Use unambiguous parameter names (`user_id` not `user`). Even small description refinements yield dramatic improvements: Claude Sonnet 3.5 hit SWE-bench Verified state-of-the-art after description refinements alone, dramatically reducing error rates.

**On interleaved thinking**
- Instructing eval agents to output reasoning + feedback *before* tool calls triggers chain-of-thought (CoT) behavior that increases effective intelligence.
- Claude's built-in interleaved thinking feature provides this off-the-shelf.

**On evaluation verifiers**
- Avoid overly strict verifiers that reject valid responses due to formatting/punctuation differences.
- Verifiers range from exact string match to Claude-as-judge.
- Don't overspecify expected tool call sequences — multiple valid paths may exist.

---

## Entities

- [[entities/ken-aizawa|Ken Aizawa]] — primary author
- [[entities/anthropic|Anthropic]] — source organization; internal tools (Slack, Asana) were the primary test bed

---

## Concepts

- [[concepts/agent-tool-design|Agent Tool Design]] — primary topic; the full framework
- [[concepts/tool-evaluation|Tool Evaluation]] — the prototype → eval → improve workflow
- [[concepts/model-context-protocol|Model Context Protocol (MCP)]] — the protocol tools are deployed through
- [[concepts/naming-conventions|Naming Conventions]] — namespacing tools follows the same principle as naming code; consistency matters

---

## Contradictions

_No contradictions with existing wiki knowledge. New domain — AI agent systems engineering._

---

## Questions

- How does tool design change as LLM context windows expand (the article notes this will happen)?
- What is the relationship between MCP tool annotations and the namespacing principles described here?
- How do these principles apply to tools that interact with real-time data (vs. static knowledge bases)?
- The article mentions `response_format` enums — are there other parameter patterns like this that are broadly useful?
- How does interleaved thinking interact with tool selection specifically (not just overall task performance)?
