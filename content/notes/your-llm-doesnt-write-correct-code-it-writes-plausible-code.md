---
title: "Your LLM Doesn't Write Correct Code. It Writes Plausible Code."
date: '2026-03-09T15:43:33+00:00'
category: webclip
summary: 'The piece argues that LLMs optimize for plausibility over correctness, using benchmarked SQLite and disk-management examples to show code that compiles, tests, and still fails on the real performance problem.'
tags: ["llm", "code-correctness", "sqlite", "benchmarks"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Hōrōshi バガボンド no X: \"Your LLM Doesn't Write Correct Code. It Writes Plausible Code.\" / X"
    url: "https://x.com/KatanaLarp/status/2029928471632224486?utm_source=tldrai"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-03/x-com--your-llm-doesnt-write-correct-code-it-writes-plausible-code.md"
    kind: repo
---

The article argues that LLM output can look complete while missing the critical details that make software correct. It uses a Rust SQLite rewrite to show how a query planner can compile, pass tests, and still run a primary-key lookup as a full table scan, and it links that pattern to other LLM-built systems that solve the prompt instead of the underlying need.

## Reading notes

- A primary-key lookup on 100 rows is used as the simplest benchmark, and the Rust rewrite is reported as 20,171 times slower than SQLite.
- The rewrite compiles, passes tests, matches the SQLite file format, and presents itself as a working database engine.
- The article’s main claim is that LLMs optimize for plausibility over correctness, so acceptance criteria need to be defined before code is generated.
- In the SQLite case, the planner fails to recognize `id INTEGER PRIMARY KEY` as the special rowid case.
- The function `is_rowid_ref()` only matches `rowid`, `_rowid_`, and `oid`, so `WHERE id = N` goes through a full table scan.
- The Rust code has a working B-tree search, but the planner never uses it for named integer primary keys.
- A second bug is fsync on every statement, which makes individual inserts much slower than batched inserts.
- Several smaller choices compound the slowdown: AST cloning, heap allocation on reads, schema reloads after autocommit, eager formatting, and new objects per statement.
- The piece treats these choices as individually defensible but collectively harmful in a database hot path.
- A second case study describes a disk-cleanup system that builds a large monitoring and forecasting tool instead of a simple cleanup job.
- The article contrasts this with SQLite’s long history of performance-aware design, including zero-copy page caching, statement reuse, schema-cookie checks, fdatasync, and the rowid primary-key optimization.
- It argues that correctness depends on measured invariants, not on code that merely resembles the intended architecture.
- The broader claim is that LLMs are most useful when the developer can state and verify exact acceptance criteria.
