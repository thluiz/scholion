---
title: "9 Observations from Building with AI Agents"
date: '2026-09-25T21:36:55+01:00'
category: webclip
summary: 'The author shares nine lessons from building AI agent systems, covering model choice, fine-tuning, static typing, team critique loops, prompt management, logging, and the cost-performance tradeoffs of current models.'
tags: ["ai-agents", "prompting", "fine-tuning", "observability"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "9 Observations from Building with AI Agents"
    url: "https://tomtunguz.com/9-observations-using-ai-agents/?utm_source=tldrai"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/tomtunguz-com--9-observations-from-building-with-ai-agents.md"
    kind: repo
---

The page lists nine observations from a year of building AI agent systems. It argues for using the best models when inputs are messy, fine-tuning when the task is stable, and static typing to catch failures earlier. It also stresses agent-to-agent critique loops, unified tooling, prompt logging, and automatic prompt reloads to support continuous improvement.

## Reading notes

- Start with state-of-the-art models when the input is unpredictable, then specialize later.
- Fine-tuning works well when the task is well defined and the input distribution stays stable.
- Static typing acts like a spell-checker or compiler for code generation and improves one-shot success on medium-complexity tasks.
- Use multiple agents to critique plans and implementations, with each agent revising the others' work.
- Keep memory, prompts, and logs in one place because the system is a closed loop of prompt, output, evaluation, and optimization.
- Current models such as Qwen 3, GLM, DeepSeek V3, and Kimi K2.5 are strong enough that cost can matter more than accuracy for workflow tool calling.
- Traces matter in AI systems, and nightly prompt optimization can use recent conversations, failures, and an LLM-as-judge to improve task success rates.
- Agents can watch prompt files and reload them automatically, which separates deployment from experimentation and allows rollback.
- Skills are easier to debug in interactive use, while code is better suited for agents that chain many function calls.
