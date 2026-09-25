---
title: "Lessons from Building AI Agents for Financial Services"
date: '2026-01-26T15:06:22+00:00'
category: webclip
summary: 'Nicolas Bustamante explains that financial AI agents depend on sandboxes, clean context, skills, S3-based storage, streaming, and evals, because small errors can destroy trust and money.'
tags: ["ai-agents", "financial-services", "sandboxes", "evaluation"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Nicolas Bustamante on X: \"Lessons from Building AI Agents for Financial Services\" / X"
    url: "https://x.com/nicbstme/status/2015174818497437834?s=12&utm_source=tldrnewsletter"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-01/x-com--nicolas-bustamante-lessons-from-building-ai-agents-for-finan.md"
    kind: repo
---

Nicolas Bustamante argues that building AI agents for financial services is mostly an exercise in reliability, because the domain punishes small mistakes and professional investors notice them quickly. The product is not the model alone but the surrounding system: data normalization, execution environments, skills, streaming, monitoring, and evaluation.

## Reading notes

- Financial services forces extreme precision because users make high-stakes decisions from the output, so every number and assumption gets checked and stress-tested.
- Sandboxes are required for multi-step agent workflows that need code execution, file changes, package installs, and isolated environments per user.
- Context is the product: messy financial sources are normalized into markdown, CSV, and JSON metadata so the agent can reason over them.
- Parsing SEC filings is difficult because they are adversarial for machine reading, with inconsistent tables, exhibits, formatting, and fiscal periods.
- Skills are presented as markdown files that define how the agent should perform tasks such as DCF analysis, with industry-specific guidance.
- The skill system supports private, shared, and public versions, with SQL-based discovery, access control, and shadowing logic.
- The author expects model improvements to remove parts of today’s scaffolding, so the system is designed to be easy to update and delete.
- S3 is used as the source of truth for user data, skills, watchlists, and memories, with PostgreSQL kept in sync for fast queries.
- Filesystem tools such as ReadFile, WriteFile, and Bash support complex workflows that involve exploration, verification, and artifact creation.
- Temporal handles long-running jobs, retries, worker crashes, and cancellation handling for tasks that can take minutes.
- Real-time streaming uses delta updates, Streamdown, and an AskUserQuestion tool so users can stay involved in key valuation choices.
- Evaluation is mandatory, with domain-specific test cases for ticker disambiguation, fiscal periods, numeric precision, grounding, and DCF skills.
- Production monitoring includes Braintrust, Temporal, GitHub issue automation, and model routing by task complexity.
- The final claim is that the surrounding experience, not the base model, is the product and the moat.
