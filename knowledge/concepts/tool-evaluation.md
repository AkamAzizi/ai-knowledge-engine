---
title: "Tool Evaluation"
type: concept
tags: [ai-agents, evaluation, evals, testing, llm-engineering, tool-design]
created: 2026-04-13
updated: 2026-04-13
sources: [writing-effective-tools-for-ai-agents]
---

# Tool Evaluation

## Definition

A systematic methodology for measuring how well LLM agents use a set of tools, then iteratively improving those tools based on evidence. The evaluation-driven loop is the core development workflow for agent tool design — analogous to how unit tests guide software development, but applied to probabilistic agent behavior.

## How It Works

### The Loop

```
Prototype → Generate eval tasks → Run evals → Analyze results → Improve tools → Repeat
```

Use a held-out test set to avoid overfitting to training evaluations. Anthropic found that even after "expert" human-written implementations, additional performance gains were extractable through this loop.

### Generating Evaluation Tasks

Tasks must be:
- **Grounded in real-world complexity** — real data sources, realistic workflows, not sandbox environments
- **Multi-step** — strong tasks require multiple chained tool calls (potentially dozens)
- **Paired with verifiable outcomes** — exact string match, structured output check, or Claude-as-judge

| Strong task | Weak task |
|---|---|
| "Schedule a meeting with Jane next week, attach notes from last planning meeting, reserve a conference room" | "Schedule a meeting with jane@acme.corp next week" |
| "Customer 9182 was triple-charged. Find all relevant logs and check if other customers were affected" | "Search payment logs for purchase_complete and customer_id=9182" |

Avoid overspecifying the expected tool call sequence — multiple valid paths to the correct answer may exist. Don't overfit verifiers to one strategy.

### Running Evaluations

- Run programmatically via direct LLM API calls — not through a UI.
- Use simple agentic `while`-loops: one loop per task, alternating LLM API calls and tool calls.
- Give each eval agent: a single task prompt + the tools.
- Instruct agents to output **reasoning and feedback blocks before tool call blocks** — triggers chain-of-thought (CoT), increases effective intelligence.
- For Claude: enable **interleaved thinking** off-the-shelf for the same effect.

**Metrics to collect (beyond top-level accuracy):**
- Total runtime per task and per tool call
- Total number of tool calls (high counts → consolidation opportunity)
- Total token consumption
- Tool error counts and types

### Analyzing Results

Metric signals and what they mean:

| Signal | Likely cause | Fix |
|---|---|---|
| Redundant / many tool calls | Pagination or token limit too tight | Rightsize default parameters |
| Frequent invalid parameter errors | Unclear tool description or schema | Improve description; add examples |
| Agent calls wrong tool | Overlapping tool names/purposes | Namespacing; remove or consolidate |
| Agent appends noise to parameters | Vague parameter description | Make description more specific |

**Read between the lines.** What agents *omit* from their reasoning is often more important than what they include. LLMs don't always say what they mean — review raw transcripts including tool calls, not just the CoT summaries.

### Agent-Assisted Improvement

- Paste evaluation transcripts directly into Claude Code.
- Claude can analyze large batches of transcripts, spot patterns, and refactor tools — including keeping descriptions self-consistent when implementations change.
- Anthropic used this to generate most of the advice in the source article.

### Verifier Design

- Too strict → rejects valid responses due to formatting/punctuation → inflates false failure rate
- Too loose → accepts incorrect responses → understates real failure rate
- Claude-as-judge is appropriate for open-ended or complex tasks

## Key Sources

- [[sources/writing-effective-tools-for-ai-agents|Writing Effective Tools for AI Agents — Using AI Agents]] — describes the full workflow; includes internal Slack and Asana eval results

## Related Concepts

- [[concepts/agent-tool-design|Agent Tool Design]] — tool evaluation is the feedback mechanism that drives tool improvement
- [[concepts/test-driven-development|Test-Driven Development]] — analogous philosophy: define correct behavior first, then write/improve code to pass. Key difference: evals are probabilistic, not deterministic.
- [[concepts/model-context-protocol|Model Context Protocol (MCP)]] — tools being evaluated are typically MCP server tools
- [[concepts/llm-assisted-architecture|LLM-Assisted Architecture]] — the ATAM-like scenario-based architect evaluation used in the ADD paper is a domain-specific instance of this loop: define expected driver satisfaction upfront, run the design, measure against those criteria, iterate

## Open Questions

- How do you build evaluations for tools with side effects (sending messages, modifying data)?
- At what eval set size does the signal become reliable enough to make decisions?
- How should evals account for cost — optimizing for fewer tokens vs. higher accuracy?
