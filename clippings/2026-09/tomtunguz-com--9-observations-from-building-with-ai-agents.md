---
url: "https://tomtunguz.com/9-observations-using-ai-agents/?utm_source=tldrai"
captured_at: "2026-09-25T21:36:55+01:00"
title: "9 Observations from Building with AI Agents"
domain: "tomtunguz-com"
---

I’ve spent the last year building AI agent systems. Here are nine observations.

**1\. Prototype with the Best**

When the input is unpredictable, email parsing, voice transcription, messy data extraction, reach for state of the art. Figure out what works with the best models, then specialize them over time.

**2\. Polish Small Gems**

I fine-tuned Qwen 3 for task classification using [rLLM](https://github.com/rllm-org/rllm)[1](#fn:1). The 8B model beats GPT 5.2 zero-shot prompting & runs locally on my laptop. Fine-tuning shines when the task is well-defined & the input distribution is stable.

**3\. Use Built-In Spell-Check**

Static typing forces the AI to face a spell-check/compiler. Ruby let agents hallucinate valid-looking code that failed at runtime. Rust checks code’s grammar. One-shot success rates improve substantially for medium-complexity tasks.

**4\. Cajole your Team of Agent Rivals**

Build your agentic braintrust. Ask Claude to create a plan. Then prod Gemini & Codex to critique it; Claude addresses the critiques & implements the code. Once implemented, ask Gemini & Codex to critique the implementation relative to the plan & Claude to revise. Agents are great micromanagers.

**5\. Put All the Clay in One Pot**

Building an agent is an exercise in Play-Doh. Some yellow, some red, some green clay. Each from a different pot. I’d like all the tools in one place : manage my memory, manage my prompts, capture my logs because it’s all a single closed loop to improvement with the model. Prompt → Output → Evaluation → Optimization → Prompt.

**6\. Recognize The iPhone 15 Era of AI**

Qwen 3, GLM, DeepSeek V3, & Kimi K2.5 deliver strong performance at a [fraction of the cost](https://tomtunguz.com/inference-as-compensation/). The models are now strong enough for workflow tool calling that more intelligence may not have as concrete a benefit. [Tau2](https://artificialanalysis.ai/evaluations/tau2-bench)[2](#fn:2) shows many models have attained this threshold & now we’re comparing them on cost rather than accuracy.

**7\. Document FTW**

As Harrison Chase [put it](https://blog.langchain.com/on-agent-frameworks-and-agent-observability/) : “in software, the code documents the app; in AI, the traces do.” Our system runs a nightly prompt optimization system. It collects the last 100 agent conversations, extracts failures (task timeouts, incorrect outputs, user corrections), & generates improved prompts using an LLM-as-judge[3](#fn:3). This closed-loop improvement lifts task success rates incrementally each week without manual intervention.

**8\. Prompt Musical Chairs**

We can’t bring the system down for new prompts. The agents watch a prompt file & reload it automatically when it changes. This separates deployment from experimentation & enables [DSPy](https://github.com/stanfordnlp/dspy)[4](#fn:4)\-style optimization to run automatically. Combine with versioned prompt files & you get full rollback capability.

**9\. Who Do You Work For?**

Skills are for interactive conversations. Code is for agents. Skills are easier to debug. When a skill fails, you know exactly where to look. When an agent chains ten function calls & the output is wrong, you’re hunting through logs.

What have you learned?

* * *

1.  RLLM is a Hugging Face library for reinforcement learning from human feedback on language models. [↩︎](#fnref:1)
    
2.  Tau2 is an agentic benchmark measuring tool-calling accuracy across models. [↩︎](#fnref:2)
    
3.  LLM-as-judge uses one language model to evaluate the outputs of another. [↩︎](#fnref:3)
    
4.  DSPy is Stanford’s framework for programmatically optimizing prompts & few-shot examples. [↩︎](#fnref:4)
