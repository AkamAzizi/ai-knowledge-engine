---
title: "Google Brain / Google DeepMind"
type: entity
tags: [google, google-brain, deepmind, ai-research, llm, reasoning]
created: 2026-04-13
updated: 2026-04-13
sources: [chain-of-thought-prompting-wei-2022, react-reasoning-acting-yao-2022]
---

# Google Brain / Google DeepMind

## Overview

Google Brain was Google's deep learning research team, merged with DeepMind in 2023 to form Google DeepMind. It produced foundational work in large language model reasoning, including two of the most-cited prompting techniques: Chain-of-Thought prompting and the ReAct framework.

## Key Contributions

- **Chain-of-Thought Prompting:** Wei et al. 2022 — demonstrated that intermediate reasoning steps elicit complex multi-step reasoning in large models; established CoT as an emergent capability at scale
- **PaLM:** Large language model used as the backbone for CoT and ReAct experiments; 540B parameter model
- **Self-consistency:** Wang et al. 2022 (Google Brain) — sample multiple CoT paths, take majority vote; improves reasoning reliability
- **ReAct (co-author):** Yao et al. 2022 — interleaved reasoning and acting for LLM agents; Google Brain collaborated with Princeton on this work

## Appearances

- [[sources/chain-of-thought-prompting-wei-2022|Wei et al. 2022]] — CoT prompting; GSM8K SOTA; emergent capability finding
- [[sources/react-reasoning-acting-yao-2022|Yao et al. 2022]] — ReAct framework; ALFWorld +34%; HotpotQA, FEVER

## Related

- [[entities/anthropic|Anthropic]] — AI research lab; creator of Claude and Claude Code; source of agent tool design principles
- [[entities/meta-ai|Meta AI]] — AI research lab; creator of RAG, DPR, BART, FAISS
