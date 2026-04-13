---
title: "ReAct: Reasoning and Acting"
type: concept
tags: [react, reasoning, acting, agents, tool-use, llm, cognitive-architecture]
created: 2026-04-13
updated: 2026-04-13
sources: [react-reasoning-acting-yao-2022]
---

# ReAct: Reasoning and Acting

## Definition

ReAct is a prompting framework and cognitive architecture for LLM agents that interleaves reasoning traces ("Thought:") with tool-calling actions ("Action:") and their results ("Observation:"). Rather than treating reasoning and acting as separate pipeline stages, ReAct generates both in a single LLM output stream — each thought informs the next action, and each observation updates the next thought.

## How It Works

Each step in a ReAct trajectory follows the pattern:

```
Thought: [reasoning about what to do next]
Action: [tool_name][input]
Observation: [result returned by the tool]
```

This repeats until the agent produces a final answer. The key property is that the reasoning trace is **explicit, inspectable output** — not hidden internal state. Every decision is visible in the transcript.

**Example (knowledge-intensive QA):**
```
Thought: I need to find the year the Eiffel Tower was completed.
Action: Search[Eiffel Tower construction]
Observation: The Eiffel Tower was completed in 1889 for the World's Fair...
Thought: I have the answer.
Action: Finish[1889]
```

## Why ReAct Works

Three mechanisms:

1. **Grounding prevents hallucination:** Retrieval actions anchor each reasoning step to external evidence; CoT-only agents fabricate facts when internal knowledge is insufficient
2. **Dynamic plan adjustment:** Observations feed back into reasoning, letting the agent update plans mid-task rather than committing upfront to a fixed plan
3. **Error localization:** When things go wrong, the Thought-Action-Observation trace reveals exactly which step failed — making debugging tractable

## Connection to Scaffolding

ReAct is the agentic-execution-level instance of the scaffolding principle:
- [[concepts/chain-of-thought-prompting|Chain-of-Thought]] provides explicit reasoning steps for single-turn tasks
- ReAct adds action steps that ground reasoning in external observation
- [[concepts/llm-assisted-architecture|LLM-Assisted Architecture]] provides explicit process scaffolding (ADD) for open-ended design tasks
- [[concepts/agent-tool-design|Agent Tool Design]] provides explicit tool descriptions that scaffold tool selection

All four use the same lever: explicit structure activates reliable behaviour from LLMs that already have latent capability.

## Key Sources

- [[sources/react-reasoning-acting-yao-2022|Yao et al. 2022]] — original ReAct paper; 34% improvement on ALFWorld; HotpotQA and FEVER results

## Related Concepts

- [[concepts/chain-of-thought-prompting|Chain-of-Thought Prompting]] — reasoning precursor to ReAct; CoT is the "Thought" component
- [[concepts/agent-tool-design|Agent Tool Design]] — tool descriptions shape the Thought step; poor descriptions corrupt reasoning, not just action selection
- [[concepts/retrieval-augmented-generation|Retrieval-Augmented Generation]] — RAG retrieves once then generates; ReAct retrieves dynamically, interleaved with reasoning
- [[concepts/tool-evaluation|Tool Evaluation]] — ReAct trajectories are a natural eval surface: the Thought traces expose agent reasoning quality beyond just final answer correctness

## Open Questions

- Can Thought traces serve as automatic verifiers in tool evaluation loops?
- How does ReAct generalize to multi-agent settings where multiple agents share an observation space?
- What recovery strategies exist when a retrieval action returns irrelevant results mid-trajectory?
