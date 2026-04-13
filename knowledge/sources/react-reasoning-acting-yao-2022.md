---
title: "ReAct: Synergizing Reasoning and Acting in Language Models"
type: source
tags: [react, reasoning, acting, agents, llm, tool-use, hotpotqa, decision-making]
created: 2026-04-13
updated: 2026-04-13
sources: []
---

**Author:** Shunyu Yao, Jeffrey Zhao, Dian Yu, Nan Du, Izhak Shafran, Karthik Narasimhan, Yuan Cao
**Published:** ICLR 2023 (arXiv 2022)
**Origin:** Princeton University / [[entities/google-brain|Google Brain]]
**Raw source:** `raw/react-reasoning-acting-yao-2022.md`

## Summary

ReAct proposes interleaving reasoning traces ("Thought:") with observable actions ("Action:") and their results ("Observation:") within LLM prompts. On knowledge-intensive tasks (HotpotQA, FEVER), this grounding via external retrieval prevents the hallucination and error propagation that chain-of-thought reasoning alone suffers when internal knowledge is insufficient. On interactive decision-making benchmarks (ALFWorld, WebShop), ReAct outperforms imitation and reinforcement learning methods by 34% and 10% respectively, with only 1–2 in-context examples.

## Key Points

- **Thought-Action-Observation loop:** Each step produces an explicit reasoning trace, a tool call, and an observation fed back into the next step — making agent reasoning inspectable and auditable
- **Grounding prevents hallucination:** When chain-of-thought runs on internal knowledge alone, it fabricates facts; ReAct's retrieval actions anchor each reasoning step to retrieved evidence
- **Sample efficiency:** 1–2 in-context examples are sufficient to elicit the ReAct pattern — the format is natural given the model's training distribution
- **Cognitive architecture for agents:** ReAct provides the reasoning layer that decides *which* tool to call and *why* — tool descriptions shape this reasoning directly
- **34% improvement on ALFWorld:** Against imitation learning baselines on household task completion
- **Not always better than CoT:** On tasks where no external knowledge is needed, pure chain-of-thought can match or beat ReAct; the external action step adds overhead

## Entities

- [[entities/google-brain|Google Brain]] — research lab, co-origin of ReAct and Chain-of-Thought

## Concepts

- [[concepts/react-framework|ReAct]] — the full cognitive architecture introduced by this paper
- [[concepts/chain-of-thought-prompting|Chain-of-Thought Prompting]] — reasoning-only precursor; ReAct extends CoT by adding action steps
- [[concepts/agent-tool-design|Agent Tool Design]] — tool descriptions shape the Thought step; bad descriptions corrupt the reasoning, not just action selection
- [[concepts/retrieval-augmented-generation|Retrieval-Augmented Generation]] — RAG is static retrieve-then-generate; ReAct is dynamic, interleaved retrieval during agentic execution

## Contradictions

None with existing knowledge. ReAct extends and operationalizes the scaffolding principle from [[concepts/llm-assisted-architecture|LLM-Assisted Architecture]] and [[concepts/agent-tool-design|Agent Tool Design]] into the agentic execution layer.

## Questions

- How does ReAct interact with tool evaluation loops? Could the Thought traces serve as automatic verifiers?
- Multi-agent ReAct: if multiple agents share an observation space, how are reasoning traces coordinated?
- What happens when the retrieval action returns irrelevant results — does the agent recover or spiral?
