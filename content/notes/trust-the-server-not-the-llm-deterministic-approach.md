---
title: "Trust the Server, Not the LLM: A Deterministic Approach to LLM Accuracy"
date: '2025-12-09T18:30:35+00:00'
category: webclip
summary: 'The article argues that numerical reporting should be moved to deterministic server-side code, while the LLM only copies citations, follows templates, and passes validation checks.'
tags: ["llm-accuracy", "deterministic-computation", "rag", "mcp"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Trust the Server, Not the LLM: A Deterministic Approach to LLM Accuracy - DEV Community"
    url: "https://dev.to/nodefiend/trust-the-server-not-the-llm-a-deterministic-approach-to-llm-accuracy-20ag?"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2025-12/dev-to--trust-the-server-not-the-llm-deterministic-approach.md"
    kind: repo
---

The article says LLMs can hallucinate numbers in trading and financial reporting because they pattern-match instead of compute. Its proposed architecture moves all calculations to deterministic Python, adds citation and checksum tracking, constrains output with templates, grounds entities with RAG, validates drafts with a second LLM, and retries corrections when validation fails.

## Reading notes

- The problem is an MCP server pulling MT5 trading data while the LLM invents values such as an extra trade count.
- The core claim is that LLMs are not calculators and fail at arithmetic tasks, especially multi-digit or more complex ones.
- Layer 1 makes the MCP server compute totals, win rate, profit factor, and expectancy before the LLM sees the data.
- Layer 2 adds an `_accuracy_report` with preformatted citations, a CRC32 checksum, and a confidence score.
- Layer 3 uses templates so the response formatter only fills citation slots and does not calculate anything.
- Layer 4 retrieves static facts from ChromaDB so entity mappings and trading rules stay grounded.
- Layer 5 sends the draft to a second LLM for strict verification against source data and checksum rules.
- Layer 6 parses validation errors, applies corrections, and retries up to a fixed limit.
- The anti-aggregation rule requires raw values before averages so trends and changes are visible.
- Final output is expected to show citation tags, a checksum, confidence information, and no approximations.
