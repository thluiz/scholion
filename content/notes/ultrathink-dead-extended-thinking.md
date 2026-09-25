---
title: "UltraThink is Dead. Long Live Extended Thinking. — Decode Claude"
date: '2026-01-20T09:30:15+00:00'
category: webclip
summary: 'The page says `ultrathink` is deprecated, extended thinking is now enabled by default, and 64K-output models can use `MAX_THINKING_TOKENS=63999` for twice the default budget.'
tags: ["extended-thinking", "claude-code", "thinking-tokens"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "UltraThink is Dead. Long Live Extended Thinking. — Decode Claude"
    url: "https://decodeclaude.com/ultrathink-deprecated/?utm_source=tldrai"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-01/decodeclaude-com--ultrathink-dead-extended-thinking.md"
    kind: repo
---

The page says `ultrathink` no longer matters in Claude Code because extended thinking is now enabled by default for supported models. It keeps the default budget at 31,999 tokens, and says 64K-output models can be pushed to 63,999 tokens with `MAX_THINKING_TOKENS=63999`.

It also says the old keyword was deprecated on January 16, 2026, that extended thinking can be disabled with `MAX_THINKING_TOKENS=0` or `alwaysThinkingEnabled: false`, and that more thinking is useful mainly for harder tasks where extra tokens and latency are worth it.

## Reading notes

- `ultrathink` is deprecated and no longer changes Claude Code behavior
- supported models now get extended thinking automatically
- the default thinking budget is 31,999 tokens
- 64K-output models can use 63,999 thinking tokens with `MAX_THINKING_TOKENS=63999`
- the old behavior can be disabled with `MAX_THINKING_TOKENS=0` or `alwaysThinkingEnabled: false`
- the page says more thinking fits complex system design, multi-file refactors, performance work, and other tasks where error cost is high
- the appendix links thinking tokens to test-time compute, chain-of-thought, scratchpads, and the idea that intermediate tokens support multi-step reasoning
