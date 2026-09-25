---
url: "https://decodeclaude.com/ultrathink-deprecated/?utm_source=tldrai"
captured_at: "2026-01-20T09:30:15+00:00"
title: "UltraThink is Dead. Long Live Extended Thinking. — Decode Claude"
domain: "decodeclaude-com"
---

---
Remember `ultrathink`? The magic keyword that unlocked Claude’s maximum reasoning power?

**It’s deprecated.**

But here’s what replaced it — and a hidden trick to get _twice_ the thinking budget on 64K output models.

___

## The Old Way: The `ultrathink` Keyword

For months, `ultrathink` was the magic word. Add it to your prompt, get 31,999 thinking tokens.

[Hacker News threads](https://news.ycombinator.com/item?id=43739997) debated its effectiveness. Power users swore by the “Opus + Ultrathink + Plan Mode” combo.

Under the hood, Claude Code detected the keyword and set the thinking budget:

```
<span><span>// Simplified (other keywords like "megathink" and "think" existed too)</span></span>
<span><span>const</span><span> thinkingBudget</span><span> =</span><span> prompt.</span><span>includes</span><span>(</span><span>"ultrathink"</span><span>) </span><span>?</span><span> 31999</span><span> :</span><span> 0</span><span>;</span></span>
<span></span>
<span><span>// Passed to the Anthropic API</span></span>
<span><span>await</span><span> client.messages.</span><span>create</span><span>({</span></span>
<span><span>  model: </span><span>"claude-sonnet-4-..."</span><span>,</span></span>
<span><span>  messages: [</span><span>...</span><span>],</span></span>
<span><span>  thinking: thinkingBudget </span><span>&gt;</span><span> 0</span><span> ?</span><span> {</span></span>
<span><span>    type: </span><span>"enabled"</span><span>,</span></span>
<span><span>    budget_tokens: thinkingBudget  </span><span>// ← This is what matters</span></span>
<span><span>  } </span><span>:</span><span> undefined</span></span>
<span><span>});</span></span>
```

___

## What Changed

On January 16, 2026, [Anthropic closed the book](https://github.com/anthropics/claude-code/issues/18072#issuecomment-3760451441) on ultrathink:

> “Closing as ultrathink is now deprecated and thinking mode is enabled by default.” — Sarah Deaton, Anthropic

If you type “ultrathink” now, you’ll see this message:

![RIP ultrathink - Claude Code showing deprecation message](https://decodeclaude.com/images/ultrathink-rip.png)

___

## The New Default

Extended thinking is now **automatically enabled** for supported models:

-   Opus 4.5 ✓
-   Sonnet 4.5 ✓
-   Sonnet 4 ✓
-   Haiku 4.5 ✓
-   Opus 4 ✓
-   Claude 3.x ✗ (not supported)

The default budget? **31,999 tokens** — the same as the old `ultrathink` maximum.

Here’s what happens now on every API call:

```
<span><span>// 1. Determine thinking budget</span></span>
<span><span>let</span><span> budgetTokens </span><span>=</span><span> 31999</span><span>;  </span><span>// Default: max</span></span>
<span></span>
<span><span>if</span><span> (process.env.</span><span>MAX_THINKING_TOKENS</span><span>) {</span></span>
<span><span>  budgetTokens </span><span>=</span><span> parseInt</span><span>(process.env.</span><span>MAX_THINKING_TOKENS</span><span>);</span></span>
<span><span>}</span></span>
<span></span>
<span><span>// 2. Auto-enabled for supported models</span></span>
<span><span>const</span><span> thinkingEnabled</span><span> =</span><span> isSupportedModel</span><span>(model);  </span><span>// Opus 4.5, Sonnet 4/4.5, Haiku 4.5, Opus 4</span></span>
<span></span>
<span><span>// 3. Passed to Anthropic API on every request</span></span>
<span><span>await</span><span> client.messages.</span><span>create</span><span>({</span></span>
<span><span>  model: </span><span>"claude-sonnet-4-..."</span><span>,</span></span>
<span><span>  messages: [</span><span>...</span><span>],</span></span>
<span><span>  thinking: thinkingEnabled </span><span>?</span><span> {</span></span>
<span><span>    type: </span><span>"enabled"</span><span>,</span></span>
<span><span>    budget_tokens: budgetTokens  </span><span>// ← 31,999 by default</span></span>
<span><span>  } </span><span>:</span><span> undefined</span></span>
<span><span>});</span></span>
```

**Translation:** You no longer need magic keywords. Every prompt gets maximum thinking by default.

___

Here’s what most people don’t know.

The 31,999 default exists for backward compatibility with **Opus 4** (which has a 32K output limit). But 64K output models support _much more_:

| Model | Max Output | Max Thinking Budget |
| --- | --- | --- |
| **Opus 4.5** | 64,000 | **63,999** |
| **Sonnet 4.5** | 64,000 | **63,999** |
| **Sonnet 4** | 64,000 | **63,999** |
| **Haiku 4.5** | 64,000 | **63,999** |
| Opus 4 | 32,000 | 31,999 |

The thinking budget is capped at `max_tokens - 1` because `budget_tokens` must be strictly less than `max_tokens` (which includes thinking), leaving at least 1 token for output:

```
<span><span>// With MAX_THINKING_TOKENS=63999 on 64K output models</span></span>
<span><span>await</span><span> client.messages.</span><span>create</span><span>({</span></span>
<span><span>  model: </span><span>"claude-opus-4-5-..."</span><span>,</span></span>
<span><span>  max_tokens: </span><span>64000</span><span>,</span></span>
<span><span>  thinking: {</span></span>
<span><span>    type: </span><span>"enabled"</span><span>,</span></span>
<span><span>    budget_tokens: </span><span>63999</span><span>  // ← 2x the default!</span></span>
<span><span>  }</span></span>
<span><span>});</span></span>
```

**To unlock the full 63,999 tokens on 64K output models (Opus 4.5, Sonnet 4/4.5, Haiku 4.5):**

```
<span><span># Sets thinking budget for this session</span></span>
<span><span>MAX_THINKING_TOKENS</span><span>=</span><span>63999</span><span> claude</span><span> --dangerously-skip-permissions</span></span>
```

Or make it permanent (add to `~/.zshrc` or `~/.bashrc`):

```
<span><span>export</span><span> MAX_THINKING_TOKENS</span><span>=</span><span>63999</span></span>
```

That’s **2x the default thinking budget** — entirely undocumented.

___

## When to Use Max Thinking

More thinking isn’t always better. It costs tokens and takes time.

**Default (31,999) is good for:**

-   Most coding tasks
-   Debugging
-   Refactoring
-   Standard architectural decisions

**Max (63,999) is worth it for:**

-   Complex system design
-   Multi-file refactors with intricate dependencies
-   Performance optimization requiring deep analysis
-   Problems where the cost of error > cost of extra tokens

___

## Disabling Extended Thinking

If you want the old behavior (no automatic thinking), you have two options:

**Option 1: Environment variable**

```
<span><span># Disables thinking for this session</span></span>
<span><span>MAX_THINKING_TOKENS</span><span>=</span><span>0</span><span> claude</span><span> --dangerously-skip-permissions</span></span>
```

**Option 2: Settings**

In your settings, set:

```
<span><span>{</span></span>
<span><span>  "alwaysThinkingEnabled"</span><span>: </span><span>false</span></span>
<span><span>}</span></span>
```

___

## TL;DR

1.  **`ultrathink` is deprecated** — the keyword does nothing now
2.  **Extended thinking is on by default** — 31,999 tokens for all supported models
3.  **Hidden unlock:** `MAX_THINKING_TOKENS=63999` gives you 2x more on 64K output models
4.  **To disable:** Set `MAX_THINKING_TOKENS=0` or `alwaysThinkingEnabled: false`

The magic words are gone. The magic is now automatic.

___

## Appendix: Why Thinking Tokens Work

_The practical guide ends here. What follows is the computational theory behind why more thinking tokens = better results._

### The Core Idea: Test-Time Compute

Traditional AI scaling focused on **training**: bigger models, more data, longer training runs. But there’s another dimension — **inference-time compute** (also called “test-time compute”).

The insight: instead of just making models bigger, let them _think longer_ on hard problems.

This was formalized in the seminal paper [“Chain-of-Thought Prompting Elicits Reasoning in Large Language Models”](https://arxiv.org/abs/2201.11903) (Wei et al., 2022). The authors showed that prompting models to generate intermediate reasoning steps dramatically improved performance on math, logic, and commonsense tasks.

### Why It Actually Works: The Theory

There’s a deep computational reason why intermediate tokens help. It’s not just “more time to think” — it’s about **breaking through fundamental architectural limits**.

#### The Depth Problem

Transformers process all tokens in parallel through a fixed number of layers. Without intermediate steps, a transformer’s computational power is bounded by its depth. Research has shown that constant-depth transformers can only solve problems in [TC⁰](https://en.wikipedia.org/wiki/TC0) — a limited complexity class that excludes many reasoning tasks.

This means standard transformers **cannot solve**:

-   Graph connectivity (are two nodes connected?)
-   Finite-state machine simulation
-   Arithmetic formula evaluation (e.g., computing nested expressions like `((3+2)×4)-1`)

These aren’t just hard — they’re _provably impossible_ without intermediate computation.

#### How CoT Breaks the Limit

Each intermediate token acts as a **computational step**. [“Chain of Thought Empowers Transformers to Solve Inherently Serial Problems”](https://openreview.net/forum?id=3EWTEy9MTM) (ICLR, 2024) proved:

> “With T steps of CoT, constant-depth transformers can solve any problem solvable by boolean circuits of size T.”

In plain terms:

-   **Without CoT**: Limited to shallow parallel computation
-   **With linear CoT steps**: Can recognize all regular languages
-   **With polynomial CoT steps**: Can solve all polynomial-time problems (P)

The thinking tokens aren’t just “working memory” — they’re literally expanding what’s computationally possible.

#### The Scratchpad Insight

[“Show Your Work: Scratchpads for Intermediate Computation”](https://arxiv.org/abs/2112.00114) (Google, 2021) demonstrated this empirically:

> “Transformers can be trained to perform multi-step computations by asking them to emit intermediate computation steps into a ‘scratchpad’. On tasks ranging from long addition to program execution, scratchpads dramatically improve the ability of language models to perform multi-step computations.”

The key realization: LLMs are **stateless** between generation cycles. The only way to carry state forward is through the tokens themselves. Thinking tokens are the model’s only persistent memory during reasoning.

### The Scaling Law

[“Scaling LLM Test-Time Compute Optimally”](https://arxiv.org/abs/2408.03314) (DeepMind, 2024) showed that **test-time compute can outperform model scaling**:

> “In a FLOPs-matched evaluation, test-time compute can be used to outperform a 14x larger model.”

The relationship is **logarithmic** — doubling thinking tokens doesn’t double accuracy, but it consistently improves it. Anthropic’s own research showed Claude’s math accuracy improves predictably with thinking budget ([“Visible Extended Thinking”](https://www.anthropic.com/news/visible-extended-thinking), 2025).

### Industry Adoption

This isn’t just academic. Thinking tokens have gone from experimental to **default behavior** across all major labs:

| Provider | Product | Approach |
| --- | --- | --- |
| **OpenAI** | GPT-5, o3, o4-mini | Thinking built into GPT-5; o-series succeeded by GPT-5 family |
| **Anthropic** | Extended Thinking | Visible thinking via `budget_tokens` parameter |
| **Google** | Gemini 3 Pro/Flash | `thinking_level` parameter (low/high); Deep Think mode |

OpenAI’s o1 started the trend in late 2024 with hidden reasoning tokens ([“Learning to Reason with LLMs”](https://openai.com/index/learning-to-reason-with-llms/)). Now in 2026, reasoning is baked into the flagship models — GPT-5, Claude Sonnet/Opus 4, Gemini 3 — no longer a separate “reasoning model” you have to opt into.

### The Trade-off

More thinking = better results, but also:

-   **Higher latency** (you’re waiting for more tokens)
-   **Higher cost** (thinking tokens are billed)
-   **Diminishing returns** (easy problems don’t benefit)

That’s why Claude Code’s default of 31,999 tokens is a sweet spot — enough for complex reasoning, not so much that simple tasks become slow and expensive.

### Key Papers & Sources

| Year | Paper | Key Contribution |
| --- | --- | --- |
| 2021 | [Scratchpads for Intermediate Computation](https://arxiv.org/abs/2112.00114) | Empirical proof that intermediate tokens enable multi-step computation |
| 2022 | [Chain-of-Thought Prompting](https://arxiv.org/abs/2201.11903) | Original CoT paper (Wei et al.) |
| 2023 | [The Expressive Power of Transformers with CoT](https://arxiv.org/abs/2310.07923) | Formal complexity theory analysis |
| 2024 | [CoT Empowers Transformers for Serial Problems](https://openreview.net/forum?id=3EWTEy9MTM) | ICLR paper proving CoT breaks TC⁰ limits |
| 2024 | [Scaling LLM Test-Time Compute](https://arxiv.org/abs/2408.03314) | Optimal compute allocation strategies |
| 2024 | [Learning to Reason with LLMs](https://openai.com/index/learning-to-reason-with-llms/) | OpenAI o1 announcement |
| 2025 | [Visible Extended Thinking](https://www.anthropic.com/news/visible-extended-thinking) | Anthropic’s design philosophy for visible reasoning |

___

_All findings verified against Claude Code v2.1.11 (January 2026). Want to verify yourself? `npm pack @anthropic-ai/claude-code`, extract, deobfuscate with [webcrack](https://github.com/nicolo-ribaudo/webcrack), and search the source._
