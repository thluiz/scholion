---
title: "Price per 1M tokens is meaningless"
date: '2026-07-09T18:12:39+01:00'
category: webclip
summary: 'The post argues that per-token pricing is a poor way to compare AI models because tokenizers differ and token efficiency varies. It favors cost per completed task as the more useful metric.'
tags: ["machine-learning", "ai-pricing", "tokenization", "benchmarking"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Price per 1M tokens is meaningless | Jan Iłowski"
    url: "https://janilowski.pl/en/blog/2026/price-per-m-tokens/?utm_source=tldrnewsletter"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-07/janilowski-pl--price-per-1m-tokens-is-meaningless.md"
    kind: repo
---

The post argues that comparing AI models by price per 1M tokens is misleading. Different tokenizers split the same text into different numbers of tokens, and models also vary in how efficiently they turn tokens into useful output. Because of that, a lower sticker price can still lead to a higher real cost.

The table compares several frontier models by token price, Artificial Analysis benchmark score, and cost per task. It shows cases where a more expensive model per token is cheaper per task, and cases where a cheaper model per token is less efficient. The conclusion is that model selection should be based on cost per completed task, not token price alone.

## Reading notes

- Different labs use different tokenizers, so the same text can be billed as different token counts.
- Anthropic recently changed its tokenizer, which increased Claude’s token count for the same text.
- Token price does not capture how much work a model gets done with each token.
- Hidden thinking tokens are billed like visible output tokens and can dominate usage cost.
- The benchmark table compares model prices, intelligence scores, and cost per task.
- GPT-5.5 is more expensive per token than Claude Opus 4.8 but cheaper per completed benchmark task.
- GLM-5.2 is much cheaper per token than GPT and Claude, but not proportionally cheaper per task.
- Sonnet 5 is presented as less efficient than Opus 4.8 despite a lower sticker price.
- DeepSeek V4 Pro stands out as a strong cost-efficiency outlier.
- The post concludes that price per 1M tokens is not a meaningful cost indicator.
