---
url: "https://dev.to/nodefiend/trust-the-server-not-the-llm-a-deterministic-approach-to-llm-accuracy-20ag?"
captured_at: "2025-12-09T18:30:35+00:00"
title: "Trust the Server, Not the LLM: A Deterministic Approach to LLM Accuracy - DEV Community"
domain: "dev-to"
---

---
### [](https://dev.to/nodefiend/trust-the-server-not-the-llm-a-deterministic-approach-to-llm-accuracy-20ag?#zero-mental-math-an-antihallucination-architecture-for-llmdriven-analysis)🚫 Zero Mental Math: An Anti-Hallucination Architecture for LLM-Driven Analysis

> A six-layer system for achieving 100% accurate numerical reporting from Large Language Models

## [](https://dev.to/nodefiend/trust-the-server-not-the-llm-a-deterministic-approach-to-llm-accuracy-20ag?#the-problem)🎯 The problem

> I built an MCP server that extracts data from my MT5 terminals on a VPS. Basically its a load of financial data reports, like trades, averages, technical indicators etc.
> 
> I built it all out and I realized that my LLM would randomly hallucinate random things, for example it would say there was a 16th trade when there only had been 15 trades for that day.
> 
> When it comes to financial reporting I realize there is probaly a lot on this topic, so I grabbed some ideas from a lot of the latest research on RAG topics, and i threw something together.

**_I wrote tests that actually test the accuracy of the results from the tools over a period of 10 times, and each MCP tool has 100% accuracy on end to end integration tests._**

I had the AI summarize it, but if anyone is curious about the exact code maybe I can open source a repeatable process, but i'm hoping from this Article you will have everything you need.

( incoming AI gen content )

___

## [](https://dev.to/nodefiend/trust-the-server-not-the-llm-a-deterministic-approach-to-llm-accuracy-20ag?#abstract)📋 Abstract

Large Language Models (LLMs) are fundamentally pattern matchers, not calculators. When asked to analyze data, they generate "plausible-looking" numbers based on statistical patterns in training data—not deterministic computation. This is catastrophic for domains requiring precision, such as trading analysis, financial reporting, or medical diagnostics.

This document describes the **Zero Mental Math Architecture**, a multi-layered system that achieves accurate numerical reporting by shifting all computation to deterministic Python code and reducing the LLM to a "citation copy machine."

___

## [](https://dev.to/nodefiend/trust-the-server-not-the-llm-a-deterministic-approach-to-llm-accuracy-20ag?#the-core-problem)⚠️ The Core Problem

### [](https://dev.to/nodefiend/trust-the-server-not-the-llm-a-deterministic-approach-to-llm-accuracy-20ag?#llms-hallucinate-numbers)🤖 LLMs Hallucinate Numbers

Given raw trading data, an LLM will confidently state:

> "Your win rate is approximately 70%"

...without performing any calculation. The model pattern-matched to a "reasonable-sounding" percentage. The actual win rate might be 65.52%, but the LLM has no mechanism to know this.

### [](https://dev.to/nodefiend/trust-the-server-not-the-llm-a-deterministic-approach-to-llm-accuracy-20ag?#why-this-happens)🧠 Why This Happens

LLMs predict the next token based on learned probability distributions. When they encounter a context suggesting a percentage is needed, they sample from the distribution of "percentages that appeared in similar contexts during training." This is fundamentally different from computation.

**Research backing**: Google's work on arithmetic capabilities in transformers (Nogueira et al., 2021) demonstrated that LLMs fail reliably at multi-digit arithmetic. The error rate increases with operand size and operation complexity. This isn't a bug to be fixed—it's an architectural limitation of attention-based sequence models.

___

## [](https://dev.to/nodefiend/trust-the-server-not-the-llm-a-deterministic-approach-to-llm-accuracy-20ag?#architecture-overview)🏗️ Architecture Overview

```
┌─────────────────────────────────────────────────────────────────┐
│                    ZERO MENTAL MATH ARCHITECTURE                │
├─────────────────────────────────────────────────────────────────┤
│  LAYER 1: Fat MCP Server (Pre-Calculation)                      │
│  └── Shift ALL computation to deterministic Python              │
├─────────────────────────────────────────────────────────────────┤
│  LAYER 2: Accuracy Reports (Provenance Tracking)                │
│  └── Pre-formatted citations with cryptographic checksums       │
├─────────────────────────────────────────────────────────────────┤
│  LAYER 3: Response Formatter (Constrained Generation)           │
│  └── Template-based output with zero degrees of freedom         │
├─────────────────────────────────────────────────────────────────┤
│  LAYER 4: RAG Context (Semantic Grounding)                      │
│  └── Retrieval-augmented generation for entity resolution       │
├─────────────────────────────────────────────────────────────────┤
│  LAYER 5: LLM Validation (Adversarial Verification)             │
│  └── Second LLM fact-checks against source data                 │
├─────────────────────────────────────────────────────────────────┤
│  LAYER 6: Auto-Retry (Iterative Refinement)                     │
│  └── Automatic correction loop with convergence guarantees      │
└─────────────────────────────────────────────────────────────────┘
```

___

## [](https://dev.to/nodefiend/trust-the-server-not-the-llm-a-deterministic-approach-to-llm-accuracy-20ag?#layer-1-fat-mcp-server-precalculation)🔧 Layer 1: Fat MCP Server (Pre-Calculation)

### [](https://dev.to/nodefiend/trust-the-server-not-the-llm-a-deterministic-approach-to-llm-accuracy-20ag?#what-it-does)📊 What It Does

The MCP (Model Context Protocol) server performs ALL numerical calculations before returning data to the LLM. The LLM never sees raw data that would require arithmetic.  

```
<span># ❌ BAD: Raw data requires LLM to calculate
</span><span>get_mt5_history_deals</span><span>()</span> <span>→</span> <span>[</span><span>deal1</span><span>,</span> <span>deal2</span><span>,</span> <span>deal3</span><span>,</span> <span>...]</span>
<span># LLM must: count deals, group by position, sum P&amp;L, calculate ratios
</span>
<span># ✅ GOOD: Pre-calculated metrics
</span><span>get_mt5_position_history</span><span>()</span> <span>→</span> <span>{</span>
    <span>"</span><span>summary</span><span>"</span><span>:</span> <span>{</span>
        <span>"</span><span>total_positions</span><span>"</span><span>:</span> <span>29</span><span>,</span>      <span># Server counted
</span>        <span>"</span><span>win_rate</span><span>"</span><span>:</span> <span>65.52</span><span>,</span>          <span># Server calculated: (19/29)*100
</span>        <span>"</span><span>profit_factor</span><span>"</span><span>:</span> <span>2.34</span><span>,</span>      <span># Server calculated: sum(wins)/abs(sum(losses))
</span>        <span>"</span><span>expectancy</span><span>"</span><span>:</span> <span>42.57</span>         <span># Server calculated: total_pl/total_positions
</span>    <span>}</span>
<span>}</span>
```

### [](https://dev.to/nodefiend/trust-the-server-not-the-llm-a-deterministic-approach-to-llm-accuracy-20ag?#why-this-works)✅ Why This Works

**Principle: Tool-Augmented LLMs**

The insight from Meta's "Toolformer" (Schick et al., 2023) and the broader ReAct paradigm (Yao et al., 2022) is that LLMs should delegate to external tools for tasks they perform poorly. Arithmetic is the canonical example.

**Principle: Separation of Concerns**

Asking an LLM to calculate percentages is like asking a poet to do accounting. Language models are trained on text prediction, not numerical computation. By moving calculation to Python—a language designed for computation—we use each system for its strengths.

**Principle: Determinism Over Stochasticity**

Python's `19/29*100 = 65.517...` is deterministic. Running it 1000 times yields identical results. An LLM's "calculation" is stochastic—it samples from a probability distribution, introducing variance even at temperature 0 (due to floating-point non-determinism in GPU operations).

**Research Foundation**

-   Toolformer (Schick et al., 2023): LLMs can learn to call APIs for tasks like calculation
-   Program-Aided Language Models (Gao et al., 2022): Offloading computation to code interpreters
-   Chain-of-Thought Arithmetic Failures (Wei et al., 2022): Even with step-by-step reasoning, LLMs make arithmetic errors

___

## [](https://dev.to/nodefiend/trust-the-server-not-the-llm-a-deterministic-approach-to-llm-accuracy-20ag?#layer-2-accuracy-reports-provenance-tracking)📝 Layer 2: Accuracy Reports (Provenance Tracking)

### [](https://dev.to/nodefiend/trust-the-server-not-the-llm-a-deterministic-approach-to-llm-accuracy-20ag?#what-it-does)🎯 What It Does

Every tool response includes an `_accuracy_report` field containing:

1.  Pre-formatted citations — Complete sentences ready for copy-paste
2.  CRC32 checksum — Cryptographic fingerprint of all metric values
3.  Confidence score — Data quality assessment

```
<span>{</span><span>
    </span><span>"summary"</span><span>:</span><span> </span><span>{</span><span> </span><span>"win_rate"</span><span>:</span><span> </span><span>65.52</span><span>,</span><span> </span><span>"profit_factor"</span><span>:</span><span> </span><span>2.34</span><span> </span><span>},</span><span>
    </span><span>"_accuracy_report"</span><span>:</span><span> </span><span>{</span><span>
        </span><span>"checksum"</span><span>:</span><span> </span><span>"A7B3C2D1"</span><span>,</span><span>
        </span><span>"checksum_input"</span><span>:</span><span> </span><span>"29|19|10|65.52|1234.56|85.25|-42.15|2.34|42.57"</span><span>,</span><span>
        </span><span>"confidence"</span><span>:</span><span> </span><span>{</span><span>
            </span><span>"score"</span><span>:</span><span> </span><span>"high"</span><span>,</span><span>
            </span><span>"reason"</span><span>:</span><span> </span><span>"9/9 metrics populated, 29 positions analyzed"</span><span>
        </span><span>},</span><span>
        </span><span>"metrics"</span><span>:</span><span> </span><span>[</span><span>
            </span><span>{</span><span>
                </span><span>"path"</span><span>:</span><span> </span><span>"summary.win_rate"</span><span>,</span><span>
                </span><span>"value"</span><span>:</span><span> </span><span>65.52</span><span>,</span><span>
                </span><span>"citation"</span><span>:</span><span> </span><span>"Win rate: 65.52% [Source: get_mt5_position_history.summary.win_rate]"</span><span>
            </span><span>}</span><span>
        </span><span>],</span><span>
        </span><span>"instructions"</span><span>:</span><span> </span><span>{</span><span>
            </span><span>"checksum_required"</span><span>:</span><span> </span><span>true</span><span>,</span><span>
            </span><span>"format"</span><span>:</span><span> </span><span>"End analysis with: [Verified: A7B3C2D1]"</span><span>
        </span><span>}</span><span>
    </span><span>}</span><span>
</span><span>}</span><span>
</span>
```

### [](https://dev.to/nodefiend/trust-the-server-not-the-llm-a-deterministic-approach-to-llm-accuracy-20ag?#why-this-works)✅ Why This Works

**Principle: The LLM as Copy Machine**

The critical insight is that LLMs are excellent at copying text verbatim. By providing the exact citation string, we reduce the LLM's job from "interpret this number and write about it" to "copy this string into your response." The former invites hallucination; the latter is mechanical.

**Principle: Verifiable Provenance**

Every number in the output has a traceable source. This enables:

-   Automated verification: Scripts can check that reported values match source data
-   Human auditing: Readers can follow citations to verify claims
-   Debugging: When errors occur, the citation trail identifies the failure point

**Principle: Checksums as Commitment Devices**

The CRC32 checksum serves multiple purposes:

1.  Tamper detection: If any metric changes, the checksum changes
2.  Verification anchor: The `[Verified: A7B3C2D1]` at the end of output confirms the LLM used the correct source data
3.  Debugging aid: The `checksum_input` field shows the exact values used, enabling manual verification

**Research Foundation**

-   Attribution in RAG Systems (Liu et al., 2023): Citation improves factual accuracy
-   Self-Consistency Checking (Wang et al., 2022): Multiple verification signals improve reliability
-   Data Provenance in ML Pipelines: Standard practice in MLOps for reproducibility

___

## [](https://dev.to/nodefiend/trust-the-server-not-the-llm-a-deterministic-approach-to-llm-accuracy-20ag?#layer-3-response-formatter-constrained-generation)📄 Layer 3: Response Formatter (Constrained Generation)

### [](https://dev.to/nodefiend/trust-the-server-not-the-llm-a-deterministic-approach-to-llm-accuracy-20ag?#what-it-does)🎯 What It Does

Templates define the exact structure of outputs, with placeholder slots for citations:  

```
<span>TEMPLATE</span> <span>=</span> <span>"""</span><span>## Performance Analysis (Confidence: {confidence.score})

### Overview
{citation:summary.total_positions}
{citation:summary.win_rate}
{citation:summary.profit_factor}

[Verified: {checksum}]</span><span>"""</span>
```

The formatter replaces `{citation:summary.win_rate}` with the exact citation string from Layer 2:  

```
Win rate: 65.52% [Source: get_mt5_position_history.summary.win_rate]
```

### [](https://dev.to/nodefiend/trust-the-server-not-the-llm-a-deterministic-approach-to-llm-accuracy-20ag?#why-this-works)✅ Why This Works

**Principle: Reducing Degrees of Freedom**

Hallucination occurs when LLMs have too much freedom. Consider:

| Approach | Degrees of Freedom | Hallucination Risk |
| --- | --- | --- |
| "Analyze this data" | Unlimited | Very High |
| "Report the win rate" | High (format, precision, context) | High |
| "Copy this citation: Win rate: 65.52%" | Near Zero | Near Zero |

Templates eliminate structural decisions. The LLM doesn't choose what to report, in what order, with what formatting—the template specifies everything.

**Principle: Slot-Filling vs. Generation**

This follows the "skeleton-then-fill" paradigm from structured NLG (Natural Language Generation). The template is the skeleton; citations are the fill. The LLM's role is purely mechanical substitution.

**Critical Implementation Rule:**  

```
<span>class</span> <span>ResponseFormatter</span><span>:</span>
    <span>"""</span><span>
    Critical Rule: NEVER calculates numbers. Only uses citations from
    _accuracy_report.metrics provided by the server.
    </span><span>"""</span>
```

The formatter is explicitly prohibited from performing any computation. It can only copy existing citations.

**Research Foundation**

-   Constrained Decoding (Hokamp & Liu, 2017): Forcing outputs to satisfy constraints
-   Template-Based NLG (Reiter & Dale, 1997): Classical approach to reliable text generation
-   Structured Output Forcing: JSON mode, function calling schemas

___

## [](https://dev.to/nodefiend/trust-the-server-not-the-llm-a-deterministic-approach-to-llm-accuracy-20ag?#layer-4-rag-context-semantic-grounding)🗄️ Layer 4: RAG Context (Semantic Grounding)

### [](https://dev.to/nodefiend/trust-the-server-not-the-llm-a-deterministic-approach-to-llm-accuracy-20ag?#what-it-does)🎯 What It Does

A ChromaDB knowledge base stores static facts:

-   Strategy mappings (magic numbers → strategy names)
-   Trading rules and constraints
-   Domain-specific terminology

Before generating responses, the system retrieves relevant context:  

```
<span># Query: "What strategy uses magic 106?"
# Returns: ["Magic number 106 is Goldfish Scalper trading XAUUSD"]
</span>
```

This context is injected into both the formatter and the validator.

### [](https://dev.to/nodefiend/trust-the-server-not-the-llm-a-deterministic-approach-to-llm-accuracy-20ag?#why-this-works)✅ Why This Works

**Principle: Not All Hallucinations Are Numerical**

An LLM might correctly report "Win rate: 65.52%" but incorrectly attribute it to "Dark Dione strategy" when it's actually "Goldfish Scalper." This is a semantic hallucination—the number is right, but the entity relationship is wrong.

RAG grounds the LLM in factual knowledge about entities, preventing semantic errors.

**Principle: Ephemeral Session Scope**  

```
<span>kb</span> <span>=</span> <span>KnowledgeBase</span><span>(</span><span>ephemeral</span><span>=</span><span>True</span><span>)</span>  <span># Resets each MCP session
</span><span>kb</span><span>.</span><span>load_static_rules</span><span>()</span>              <span># Loads known-good facts
</span>
```

The knowledge base is session-scoped to prevent stale data accumulation. Static rules (which don't change) are loaded fresh; dynamic trading statistics are always fetched live from MT5.

**Principle: Context for Both Generator and Validator**

The same RAG context is passed to:

1.  Formatter: To ground response generation
2.  Validator: To prevent false-positive hallucination flags

If the response says "Goldfish Scalper (Magic 106)" and the validator's context confirms this mapping, it won't incorrectly flag it as a hallucination.

**Research Foundation**

-   RAG (Lewis et al., 2020): The foundational retrieval-augmented generation paper
-   REALM (Guu et al., 2020): Retrieval-enhanced pre-training
-   In-Context Learning (Brown et al., 2020): GPT-3's ability to use context examples
-   Grounding in Dialogue Systems (Roller et al., 2020): Connecting responses to knowledge

___

## [](https://dev.to/nodefiend/trust-the-server-not-the-llm-a-deterministic-approach-to-llm-accuracy-20ag?#layer-5-llm-validation-adversarial-verification)✅ Layer 5: LLM Validation (Adversarial Verification)

### [](https://dev.to/nodefiend/trust-the-server-not-the-llm-a-deterministic-approach-to-llm-accuracy-20ag?#what-it-does)🎯 What It Does

A second LLM (Novita AI) validates the drafted response against source data before delivery to the user:  

```
<span>validation_result</span> <span>=</span> <span>validate_with_llm</span><span>(</span>
    <span>response_text</span><span>=</span><span>draft</span><span>,</span>      <span># What the LLM wants to say
</span>    <span>source_data</span><span>=</span><span>mcp_response</span><span>,</span> <span># Ground truth from server
</span>    <span>context</span><span>=</span><span>rag_context</span>       <span># Knowledge base facts
</span><span>)</span>
```

The validator checks four rules:

1.  Zero Mental Math: All numbers match source exactly
2.  Anti-Aggregation: Raw values shown before averages
3.  Citation Requirement: Every number has `[Source: ...]`
4.  Checksum Verification: Response ends with correct `[Verified: XXXX]`

### [](https://dev.to/nodefiend/trust-the-server-not-the-llm-a-deterministic-approach-to-llm-accuracy-20ag?#why-this-works)✅ Why This Works

**Principle: Verification is Easier Than Generation**

This is a fundamental asymmetry in computational complexity. Consider:

-   Generation: "Analyze this data and write a report" (open-ended, creative)
-   Verification: "Does '65.52%' match the source value '65.52'?" (closed, deterministic)

The validator has a much simpler task: pattern matching and comparison. This makes it far less prone to hallucination than the generator.

**Principle: Adversarial Checking**

This draws from:

-   Constitutional AI (Anthropic, 2022): Using AI to critique and improve AI outputs
-   Debate (Irving et al., 2018): Having models argue to expose weaknesses
-   Red-teaming: Standard security practice of adversarial testing

The validator is explicitly instructed to be strict:  

```
Be strict - any deviation from source is a hallucination
```

**Principle: Structured Error Output**

The validator returns structured JSON with specific issue categorization:  

```
<span>{</span><span>
    </span><span>"hallucinations_found"</span><span>:</span><span> </span><span>true</span><span>,</span><span>
    </span><span>"issues"</span><span>:</span><span> </span><span>[{</span><span>
        </span><span>"claim"</span><span>:</span><span> </span><span>"Win Rate: approximately 70%"</span><span>,</span><span>
        </span><span>"problem"</span><span>:</span><span> </span><span>"Source shows 65.52%, not 'approximately 70%'"</span><span>,</span><span>
        </span><span>"severity"</span><span>:</span><span> </span><span>"critical"</span><span>,</span><span>
        </span><span>"correct_value"</span><span>:</span><span> </span><span>"Win rate: 65.52% [Source: ...]"</span><span>,</span><span>
        </span><span>"rule_violated"</span><span>:</span><span> </span><span>"Zero Mental Math"</span><span>
    </span><span>}]</span><span>
</span><span>}</span><span>
</span>
```

This enables automated correction in Layer 6.

**Research Foundation**

-   Constitutional AI (Bai et al., 2022): AI systems that critique themselves
-   Self-Consistency (Wang et al., 2022): Sampling multiple times and checking agreement
-   Fact Verification (Thorne et al., 2018): FEVER dataset and verification systems
-   LLM-as-Judge (Zheng et al., 2023): Using LLMs to evaluate LLM outputs

___

## [](https://dev.to/nodefiend/trust-the-server-not-the-llm-a-deterministic-approach-to-llm-accuracy-20ag?#layer-6-autoretry-iterative-refinement)🔄 Layer 6: Auto-Retry (Iterative Refinement)

### [](https://dev.to/nodefiend/trust-the-server-not-the-llm-a-deterministic-approach-to-llm-accuracy-20ag?#what-it-does)🎯 What It Does

When validation fails, the system automatically:

1.  Parses the validation errors
2.  Applies corrections to the draft
3.  Re-validates
4.  Repeats up to N times (default: 3)

```
<span>for</span> <span>attempt</span> <span>in</span> <span>range</span><span>(</span><span>1</span><span>,</span> <span>max_retries</span> <span>+</span> <span>1</span><span>):</span>
    <span>validation</span> <span>=</span> <span>validate_with_llm</span><span>(</span><span>narrative</span><span>,</span> <span>source_data</span><span>,</span> <span>context</span><span>)</span>

    <span>if</span> <span>not</span> <span>validation</span><span>[</span><span>"</span><span>hallucinations_found</span><span>"</span><span>]:</span>
        <span># Success! Return validated response
</span>        <span>return</span> <span>{</span><span>"</span><span>analysis</span><span>"</span><span>:</span> <span>narrative</span><span>,</span> <span>"</span><span>_validation_meta</span><span>"</span><span>:</span> <span>{</span><span>"</span><span>validated</span><span>"</span><span>:</span> <span>True</span><span>}}</span>

    <span># Failed - apply corrections and retry
</span>    <span>narrative</span> <span>=</span> <span>corrector</span><span>.</span><span>apply_corrections</span><span>(</span><span>narrative</span><span>,</span> <span>validation</span><span>[</span><span>"</span><span>issues</span><span>"</span><span>])</span>
```

### [](https://dev.to/nodefiend/trust-the-server-not-the-llm-a-deterministic-approach-to-llm-accuracy-20ag?#why-this-works)✅ Why This Works

**Principle: Iterative Refinement**

Self-refinement is a well-established technique for improving LLM outputs. The key insight is that correction is easier than generation—given specific feedback ("this number is wrong, it should be X"), the fix is mechanical.

**Principle: Bounded Retry with Graceful Degradation**

The system doesn't retry forever:

-   Fixable issues (wrong numbers): Auto-correct and retry
-   Unfixable issues (structural problems): Fail immediately with diagnostics
-   Max retries exceeded: Return error with last attempt for debugging

```
<span>if</span> <span>not</span> <span>can_fix</span><span>:</span>
    <span>return</span> <span>{</span>
        <span>"</span><span>success</span><span>"</span><span>:</span> <span>False</span><span>,</span>
        <span>"</span><span>error</span><span>"</span><span>:</span> <span>"</span><span>Validation failed with unfixable issues</span><span>"</span><span>,</span>
        <span>"</span><span>validation_issues</span><span>"</span><span>:</span> <span>issues</span><span>,</span>
        <span>"</span><span>unfixable_reasons</span><span>"</span><span>:</span> <span>reasons</span>
    <span>}</span>
```

**Principle: Convergence Guarantees**

Because corrections are deterministic (replace X with Y) and the validator is consistent, the system converges. If the corrector properly applies all fixes, the next validation will pass. The retry loop guards against transient failures, not fundamental incompatibility.

**Research Foundation**

-   Self-Refine (Madaan et al., 2023): Iterative refinement with self-feedback
-   Reflexion (Shinn et al., 2023): Verbal reinforcement learning through self-reflection
-   Error Correction in Communication (Shannon, 1948): Fundamental information theory

___

## [](https://dev.to/nodefiend/trust-the-server-not-the-llm-a-deterministic-approach-to-llm-accuracy-20ag?#special-rule-antiaggregation)🚨 Special Rule: Anti-Aggregation

### [](https://dev.to/nodefiend/trust-the-server-not-the-llm-a-deterministic-approach-to-llm-accuracy-20ag?#the-problem)⚠️ The Problem

Aggregation hides critical information. Consider:  

```
❌ WRONG (Aggregation Hallucination):
Current lot sizes:
- EURUSD: 0.06 lots average (range: 0.05-0.08)
```

This hides that lot size doubled from 0.05 → 0.08 recently—a critical signal that risk management changed.

### [](https://dev.to/nodefiend/trust-the-server-not-the-llm-a-deterministic-approach-to-llm-accuracy-20ag?#the-solution)✅ The Solution

```
✅ CORRECT (Raw Data First):
Current lot sizes [Source: positions list]:
- EURUSD last 5: [0.05, 0.05, 0.05, 0.08, 0.07]
  → CURRENT: 0.07 lots
  → TREND: Scaled up 60% on Nov 24 (0.05 → 0.08)
  → Average: 0.06 lots (for reference only)
```

### [](https://dev.to/nodefiend/trust-the-server-not-the-llm-a-deterministic-approach-to-llm-accuracy-20ag?#why-this-works)✅ Why This Works

**Principle: Simpson's Paradox Awareness**

Aggregates can reverse the apparent direction of relationships. A "stable average" can hide dramatic changes in underlying data. By requiring raw values first, we prevent this information loss.

**Principle: Auditability**

Scientific reporting standards require showing raw data. If you only report "average 0.06," readers cannot detect:

-   Outliers that skew the average
-   Trends (increasing/decreasing)
-   Distribution shape (uniform vs. bimodal)

**Principle: Transparency Over Convenience**

It's easier to report a single number. But the Anti-Aggregation Rule prioritizes transparency over convenience. The small cognitive cost of reading 5 raw values prevents potentially catastrophic misunderstandings.

___

## [](https://dev.to/nodefiend/trust-the-server-not-the-llm-a-deterministic-approach-to-llm-accuracy-20ag?#accuracy-indicators-in-final-output)🎯 Accuracy Indicators in Final Output

### [](https://dev.to/nodefiend/trust-the-server-not-the-llm-a-deterministic-approach-to-llm-accuracy-20ag?#what-indicates-accuracy)✅ What Indicates Accuracy

| Indicator | Location | Example | Why It Matters |
| --- | --- | --- | --- |
| Citation tags | After every number | \[Source: tool.path\] | Traceable provenance |
| Checksum | End of response | \[Verified: A7B3C2D1\] | Data integrity proof |
| Confidence score | Header | (Confidence: high) | Data quality signal |
| Validation metadata | Response field | "validated": true | System verification passed |
| No approximations | Absence | Never: "~", "about" | Zero Mental Math compliance |
| Raw values before aggregates | Data sections | last 5: \[...\] | Anti-Aggregation compliance |

### [](https://dev.to/nodefiend/trust-the-server-not-the-llm-a-deterministic-approach-to-llm-accuracy-20ag?#red-flags-hallucination-indicators)🚩 Red Flags (Hallucination Indicators)

| Red Flag | Example | Rule Violated |
| --- | --- | --- |
| Missing citation | Win rate: 65.52% | Citation Requirement |
| Approximation words | approximately 70% | Zero Mental Math |
| Missing checksum | No \[Verified: XXXX\] | Checksum Requirement |
| Rounded numbers | 70% vs 65.52% | Zero Mental Math |
| Averages without raw data | Average: 0.06 alone | Anti-Aggregation |
| Confidence missing | No confidence score | Incomplete output |

___

## [](https://dev.to/nodefiend/trust-the-server-not-the-llm-a-deterministic-approach-to-llm-accuracy-20ag?#complete-example-endtoend-pipeline)📖 Complete Example: End-to-End Pipeline

### [](https://dev.to/nodefiend/trust-the-server-not-the-llm-a-deterministic-approach-to-llm-accuracy-20ag?#step-1-user-request)Step 1: User Request

```
"Analyze my trading performance for November"
```

### [](https://dev.to/nodefiend/trust-the-server-not-the-llm-a-deterministic-approach-to-llm-accuracy-20ag?#step-2-mcp-server-response-layers-12)Step 2: MCP Server Response (Layers 1-2)

```
<span>{</span><span>
    </span><span>"success"</span><span>:</span><span> </span><span>true</span><span>,</span><span>
    </span><span>"summary"</span><span>:</span><span> </span><span>{</span><span>
        </span><span>"total_positions"</span><span>:</span><span> </span><span>29</span><span>,</span><span>
        </span><span>"total_wins"</span><span>:</span><span> </span><span>19</span><span>,</span><span>
        </span><span>"total_losses"</span><span>:</span><span> </span><span>10</span><span>,</span><span>
        </span><span>"win_rate"</span><span>:</span><span> </span><span>65.52</span><span>,</span><span>
        </span><span>"profit_factor"</span><span>:</span><span> </span><span>2.34</span><span>,</span><span>
        </span><span>"total_pl"</span><span>:</span><span> </span><span>1234.56</span><span>
    </span><span>},</span><span>
    </span><span>"_accuracy_report"</span><span>:</span><span> </span><span>{</span><span>
        </span><span>"checksum"</span><span>:</span><span> </span><span>"A7B3C2D1"</span><span>,</span><span>
        </span><span>"confidence"</span><span>:</span><span> </span><span>{</span><span>"score"</span><span>:</span><span> </span><span>"high"</span><span>,</span><span> </span><span>"reason"</span><span>:</span><span> </span><span>"9/9 metrics, 29 positions"</span><span>},</span><span>
        </span><span>"metrics"</span><span>:</span><span> </span><span>[</span><span>
            </span><span>{</span><span>
                </span><span>"path"</span><span>:</span><span> </span><span>"summary.win_rate"</span><span>,</span><span>
                </span><span>"value"</span><span>:</span><span> </span><span>65.52</span><span>,</span><span>
                </span><span>"citation"</span><span>:</span><span> </span><span>"Win rate: 65.52% [Source: get_mt5_position_history.summary.win_rate]"</span><span>
            </span><span>},</span><span>
            </span><span>{</span><span>
                </span><span>"path"</span><span>:</span><span> </span><span>"summary.profit_factor"</span><span>,</span><span>
                </span><span>"value"</span><span>:</span><span> </span><span>2.34</span><span>,</span><span>
                </span><span>"citation"</span><span>:</span><span> </span><span>"Profit factor: 2.34 [Source: get_mt5_position_history.summary.profit_factor]"</span><span>
            </span><span>}</span><span>
        </span><span>]</span><span>
    </span><span>}</span><span>
</span><span>}</span><span>
</span>
```

### [](https://dev.to/nodefiend/trust-the-server-not-the-llm-a-deterministic-approach-to-llm-accuracy-20ag?#step-3-template-formatting-layer-3)Step 3: Template Formatting (Layer 3)

```
<span>## Performance Analysis (Confidence: high)</span>

<span>### Overview</span>
<span>-</span> Total positions: 29 [Source: get_mt5_position_history.summary.total_positions]
<span>-</span> Win rate: 65.52% [Source: get_mt5_position_history.summary.win_rate]
<span>-</span> Profit factor: 2.34 [Source: get_mt5_position_history.summary.profit_factor]

<span>### Financial Performance</span>
<span>-</span> Total P&amp;L: $1234.56 [Source: get_mt5_position_history.summary.total_pl]

[Verified: A7B3C2D1]
```

### [](https://dev.to/nodefiend/trust-the-server-not-the-llm-a-deterministic-approach-to-llm-accuracy-20ag?#step-4-rag-context-retrieval-layer-4)Step 4: RAG Context Retrieval (Layer 4)

```
Retrieved: "Magic number 106 is Goldfish Scalper trading XAUUSD"
```

### [](https://dev.to/nodefiend/trust-the-server-not-the-llm-a-deterministic-approach-to-llm-accuracy-20ag?#step-5-llm-validation-layer-5)Step 5: LLM Validation (Layer 5)

```
<span>{</span><span>
    </span><span>"hallucinations_found"</span><span>:</span><span> </span><span>false</span><span>,</span><span>
    </span><span>"checksum_valid"</span><span>:</span><span> </span><span>true</span><span>,</span><span>
    </span><span>"summary"</span><span>:</span><span> </span><span>"All claims verified against source data"</span><span>
</span><span>}</span><span>
</span>
```

### [](https://dev.to/nodefiend/trust-the-server-not-the-llm-a-deterministic-approach-to-llm-accuracy-20ag?#step-6-final-response)Step 6: Final Response

```
<span>{</span><span>
    </span><span>"success"</span><span>:</span><span> </span><span>true</span><span>,</span><span>
    </span><span>"analysis"</span><span>:</span><span> </span><span>"## Performance Analysis (Confidence: high)</span><span>\n\n</span><span>...</span><span>\n\n</span><span>[Verified: A7B3C2D1]"</span><span>,</span><span>
    </span><span>"_validation_meta"</span><span>:</span><span> </span><span>{</span><span>
        </span><span>"validated"</span><span>:</span><span> </span><span>true</span><span>,</span><span>
        </span><span>"attempts"</span><span>:</span><span> </span><span>1</span><span>,</span><span>
        </span><span>"model"</span><span>:</span><span> </span><span>"novita-default"</span><span>,</span><span>
        </span><span>"rag_context_used"</span><span>:</span><span> </span><span>true</span><span>
    </span><span>}</span><span>
</span><span>}</span><span>
</span>
```

___

## [](https://dev.to/nodefiend/trust-the-server-not-the-llm-a-deterministic-approach-to-llm-accuracy-20ag?#summary-why-this-architecture-works)📊 Summary: Why This Architecture Works

| Layer | Technique | What It Prevents | Key Insight |
| --- | --- | --- | --- |
| 1 | Server-side calculation | LLM arithmetic errors | Use the right tool for the job |
| 2 | Pre-formatted citations | LLM paraphrasing numbers | Reduce LLM to copy machine |
| 3 | Template-based output | Structural hallucination | Minimize degrees of freedom |
| 4 | RAG context grounding | Semantic hallucination | Ground entities in facts |
| 5 | Second LLM validation | Subtle errors slipping through | Verification < Generation |
| 6 | Auto-retry with correction | Transient failures | Iterative refinement converges |

### [](https://dev.to/nodefiend/trust-the-server-not-the-llm-a-deterministic-approach-to-llm-accuracy-20ag?#the-metaprinciple)💡 The Meta-Principle

**Trust flows from deterministic systems to stochastic ones, never the reverse.**  

```
Python calculates → Server stores → Citations copy → Templates structure → Validator checks
```

At no point does an LLM "decide" a number. The LLM's role is purely mechanical: copying citations into template slots. This is the fundamental insight that makes 100% accuracy achievable.

___

## [](https://dev.to/nodefiend/trust-the-server-not-the-llm-a-deterministic-approach-to-llm-accuracy-20ag?#references)📚 References

1.  Schick, T., et al. (2023). "Toolformer: Language Models Can Teach Themselves to Use Tools." arXiv:2302.04761
2.  Yao, S., et al. (2022). "ReAct: Synergizing Reasoning and Acting in Language Models." arXiv:2210.03629
3.  Lewis, P., et al. (2020). "Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks." NeurIPS 2020
4.  Wang, X., et al. (2022). "Self-Consistency Improves Chain of Thought Reasoning in Language Models." arXiv:2203.11171
5.  Bai, Y., et al. (2022). "Constitutional AI: Harmlessness from AI Feedback." arXiv:2212.08073
6.  Madaan, A., et al. (2023). "Self-Refine: Iterative Refinement with Self-Feedback." arXiv:2303.17651
7.  Gao, L., et al. (2022). "PAL: Program-Aided Language Models." arXiv:2211.10435
8.  Nogueira, R., et al. (2021). "Investigating the Limitations of Transformers with Simple Arithmetic Tasks." arXiv:2102.13019

___
