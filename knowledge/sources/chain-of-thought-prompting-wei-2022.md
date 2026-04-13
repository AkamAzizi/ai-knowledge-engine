---
title: "Chain-of-Thought Prompting Elicits Reasoning in Large Language Models"
type: source
tags: [chain-of-thought, reasoning, prompting, few-shot, emergent-capability, gsm8k, palm]
created: 2026-04-13
updated: 2026-04-13
sources: []
---

**Author:** Jason Wei, Xuezhi Wang, Dale Schuurmans, Maarten Bosma, Brian Ichter, Fei Xia, Ed Chi, Quoc V. Le, Denny Zhou
**Published:** NeurIPS 2022
**Origin:** [[entities/google-brain|Google Brain]]
**Raw source:** `raw/chain-of-thought-prompting-wei-2022.md`

## Summary

Chain-of-thought (CoT) prompting adds intermediate reasoning steps to few-shot examples. On PaLM 540B, prompting with just eight CoT exemplars achieves state-of-the-art on GSM8K math word problems — surpassing fine-tuned GPT-3 with a verifier. Critically, CoT is an emergent capability: it only improves performance at sufficient model scale (~100B+ parameters), and can hurt smaller models. The paper establishes that structured intermediate reasoning — not larger models or fine-tuning — is the key lever for complex multi-step tasks.

## Key Points

- **Emergent at scale:** CoT only improves performance in models ~100B+ parameters; smaller models perform worse with CoT than without
- **PaLM 540B + CoT = GSM8K SOTA:** Eight hand-written reasoning examples are enough to unlock state-of-the-art math reasoning, beating fine-tuned systems
- **Arithmetic, commonsense, symbolic:** Gains hold across all three task types, not just math
- **Robustness:** Results are stable across different annotators writing the reasoning chains and across different sets of exemplars
- **Zero-shot CoT ("Let's think step by step"):** A follow-on result showing a single phrase can elicit CoT without exemplars — makes the technique accessible at inference time
- **Self-consistency:** Sampling multiple CoT paths and taking the majority vote further improves reliability — the reasoning space can be explored, not just sampled once
- **Scaffolding principle:** CoT is the prompting-level instance of the principle that providing explicit process structure activates latent model capability — the same principle as ADD scaffolding in architecture design and tool descriptions in agent tool use

## Entities

- [[entities/google-brain|Google Brain]] — research lab; origin of chain-of-thought, ReAct, and related reasoning work

## Concepts

- [[concepts/chain-of-thought-prompting|Chain-of-Thought Prompting]] — the full technique introduced by this paper
- [[concepts/react-framework|ReAct]] — extends CoT by adding action steps; "Thought:" traces are CoT applied to agentic decision-making
- [[concepts/agent-tool-design|Agent Tool Design]] — tool descriptions scaffold agent reasoning the same way CoT exemplars scaffold task reasoning
- [[concepts/llm-assisted-architecture|LLM-Assisted Architecture]] — ADD process description plays the same role as CoT exemplars: providing explicit structure that elicits reliable LLM behaviour

## Contradictions

None with existing knowledge. CoT strengthens the scaffolding thesis that runs through [[overviews/ai-agent-systems|AI Agent Systems]]: explicit process structure — not raw model capability — is the primary differentiator.

## Questions

- Why does CoT hurt smaller models? Is it that intermediate steps introduce more surface area for errors, or that the CoT format is out-of-distribution for smaller models?
- Program-of-Thought (generating code as the reasoning chain) and Tree-of-Thoughts (tree-structured exploration) — when should each be preferred over standard CoT?
- What is the analogous "chain-of-thought" for architecture design tasks? Is the ADD iteration plan the architectural equivalent of CoT exemplars?
