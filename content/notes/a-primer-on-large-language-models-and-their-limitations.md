---
title: "A Primer on Large Language Models and their Limitations"
date: "2026-09-23T15:38:15+01:00"
category: webclip
summary: "Johnson and Hyland-Wood's LLM primer argues hallucination is the wrong word: LLMs produce Frankfurtian bullshit, indifferent to truth, alongside catastrophic forgetting, model collapse, and jailbreak risk."
tags:
  - llms
  - deep-learning
  - ai
  - hallucination
has_commentary: false
sources:
  - title: "A Primer on Large Language Models and their Limitations"
    url: "https://arxiv.org/html/2412.04503v1"
    kind: paper
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/arxiv-org--a-primer-on-large-language-models-and-their-limitations.md"
    kind: repo
---

Sandra Johnson and David Hyland-Wood's fourth section, "Risks and Mitigations," covers five failure modes: catastrophic forgetting, model collapse, jailbreak attacks, hallucination, and tasks where LLMs still underperform humans.

They propose replacing "hallucination" with Harry Frankfurt's philosophical account of bullshit: speech indifferent to truth, distinct from a deliberate lie. They argue the decoder only extrapolates from token patterns in its input, with no built-in fact-checking against external reality. The authors cite Hannigan et al.'s term for the result: botshit.

## Reading notes

- Catastrophic forgetting: sequential fine-tuning on new tasks degrades performance on tasks the model previously handled well, because the fine-tuning updates weights to fit the new task at the old task's expense. Mitigations include regularisation methods like elastic weight consolidation, replay methods that mix old and new training data, and architectural methods like progressive neural networks with per-task subnetworks.
- Model collapse: as more of the public internet becomes LLM-generated, future models increasingly train on their predecessors' output, mixed with human-generated text they cannot tell apart from it. Data-provenance labeling is a proposed mitigation, but it breaks whenever a system or user skips the provenance tag; the authors call current fixes insufficient.
- Jailbreak attacks: adversarial prompts designed to bypass a model's alignment training. Xie et al.'s proposed defenses include system-mode self-reminders that wrap the user query with an instruction to behave ethically, plus RLHF, content filtering, and prompt-resistance testing.
- The "strawberry" test exposes a tokenization limit: most LLMs answer "2" r's in "strawberry" because they process a token for the word, never the string of letters itself. Prompting the model to first list the letters, then count, produces the correct answer.
- OpenAI's o1-preview (code-named Strawberry) gets the letter-count right by parsing and double-checking itself, at the cost of roughly 22 seconds of added latency versus an instant wrong answer.
- Galileo's Hallucination Index benchmarks how often named LLMs hallucinate; in its RAG-based test, Claude 3.5 Sonnet ranked highest, and most models performed best retrieving from medium-length documents.
- The authors tested ChatGPT 4, 4o, Llama 3, Claude, and Gemini with the same prompts asking for academic references on LLM orchestration and found they produced closely similar botshit: citations to papers, links, and journals that do not exist, plausible-looking but false.
- The primer closes by flagging Liquid Foundation Models, announced by Liquid AI in September 2024, as a departure from the transformer architecture: liquid neural networks that are smaller, adjust dynamically to input, and are structurally simpler.

Related: [I don't like LLMs](/notes/i-dont-like-llms/) diagnoses the discomfort of talking to a chatbot directly; [News Feature: What are the limits of deep learning?](/notes/news-feature-what-are-the-limits-of-deep-learning/) covers the pre-LLM generation of the same architecture.
