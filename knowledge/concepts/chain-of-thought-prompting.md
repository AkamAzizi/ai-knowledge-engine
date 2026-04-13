---
title: "Chain-of-Thought Prompting"
type: concept
tags: [chain-of-thought, cot, reasoning, prompting, few-shot, emergent, llm]
created: 2026-04-13
updated: 2026-04-13
sources: [chain-of-thought-prompting-wei-2022]
---

# Chain-of-Thought Prompting

## Definition

Chain-of-thought (CoT) prompting is a few-shot prompting technique in which exemplars include intermediate reasoning steps — not just input-output pairs. By showing the model *how* to reason through a problem, CoT elicits dramatically better performance on complex multi-step tasks. It is an emergent capability: it only improves performance at sufficient model scale (~100B+ parameters).

## How It Works

**Standard prompting exemplar:**
```
Q: Roger has 5 tennis balls. He buys 2 cans of 3. How many does he have?
A: 11
```

**Chain-of-thought exemplar:**
```
Q: Roger has 5 tennis balls. He buys 2 cans of 3. How many does he have?
A: Roger started with 5. 2 cans × 3 = 6. 5 + 6 = 11. The answer is 11.
```

The same reasoning-step pattern in the exemplar is applied by the model to new questions. 8 hand-written exemplars on PaLM 540B achieved state-of-the-art on GSM8K math problems — surpassing fine-tuned GPT-3 with a verifier.

## Variants

| Variant | How | When |
|---|---|---|
| Standard CoT | Few-shot exemplars with reasoning steps | Complex tasks, access to good exemplars |
| Zero-shot CoT | Append "Let's think step by step" | No exemplars available |
| Self-consistency | Sample k CoT paths, take majority vote | Higher reliability on important queries |
| Program-of-Thought | Generate code as the reasoning chain | Tasks requiring exact computation |
| Tree of Thoughts | Tree-structured exploration of reasoning paths | Very hard planning/reasoning tasks |

## Scale Dependency

A critical finding: CoT is *not* universally beneficial. At smaller scales (<100B parameters), adding reasoning steps can *hurt* performance — the model isn't capable enough to produce useful intermediate steps, and the additional surface area introduces errors. This makes CoT a technique tied to large frontier models.

## The Scaffolding Connection

Chain-of-thought is the prompting-level instance of a general principle running through this knowledge base: **providing explicit process structure activates latent capability in LLMs.** The same principle appears across domains:

| Domain | Scaffolding mechanism | Source |
|---|---|---|
| Task reasoning | CoT exemplars with step-by-step reasoning | [[sources/chain-of-thought-prompting-wei-2022\|Wei et al. 2022]] |
| Agentic execution | Thought-Action-Observation traces | [[concepts/react-framework\|ReAct]] |
| Architecture design | ADD process description + iteration plan | [[concepts/llm-assisted-architecture\|LLM-Assisted Architecture]] |
| Tool use | Prompt-engineered tool descriptions | [[concepts/agent-tool-design\|Agent Tool Design]] |

In each case, the scaffold — not the model — is the differentiating factor.

## Key Sources

- [[sources/chain-of-thought-prompting-wei-2022|Wei et al. 2022]] — original CoT paper; PaLM 540B; GSM8K SOTA; emergent capability finding

## Related Concepts

- [[concepts/react-framework|ReAct]] — extends CoT by adding action steps; "Thought:" traces in ReAct *are* chain-of-thought applied to agentic decision-making
- [[concepts/agent-tool-design|Agent Tool Design]] — tool descriptions serve the same function as CoT exemplars: scaffolding correct model behaviour
- [[concepts/llm-assisted-architecture|LLM-Assisted Architecture]] — ADD process description plays the same role as CoT exemplars for architecture design tasks
- [[concepts/retrieval-augmented-generation|Retrieval-Augmented Generation]] — RAG and CoT compose: RAG provides knowledge access; CoT provides reasoning quality; ReAct combines both

## Open Questions

- Why does CoT hurt smaller models — is it error amplification, or out-of-distribution format?
- Is the ADD iteration plan in architecture design the architectural equivalent of CoT exemplars?
- At what point does self-consistency sampling become more cost-effective than a better CoT prompt?
