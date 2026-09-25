---
title: "The New Software Lifecycle"
date: "2026-09-23T16:03:44+01:00"
category: webclip
summary: "Addy Osmani pulls the load-bearing ideas from a Google whitepaper he co-wrote on AI and the SDLC: an agent is 10% model and 90% harness, and verification is what separates vibe coding from engineering."
tags:
  - ai-coding
  - agent-harness
  - context-engineering
  - software-lifecycle
has_commentary: false
sources:
  - title: "AddyOsmani.com - The New Software Lifecycle"
    url: "https://addyosmani.com/blog/new-sdlc-vibe-coding/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-08/addyosmani-com--the-new-software-lifecycle.md"
    kind: repo
---

Addy Osmani co-wrote Google's "The New SDLC With Vibe Coding" whitepaper and picks out the parts he thinks matter, starting with a framing he keeps returning to: an agent is a model plus a harness, and the paper's rough split puts that at 10% model and 90% harness. Two benchmark results back the claim. One team moved a coding agent from outside the top 30 into the top 5 on Terminal Bench 2.0 by changing only the harness, same model underneath. A separate LangChain experiment added 13.7 points on the same benchmark by touching just the system prompt, tools and middleware.

That reframes where he debugs agent failures: harness first, model second. A missing tool, an overly loose rule, a forgotten guardrail, or a context window full of junk usually explains more than the model choice does. [My LLM coding workflow going into 2026](/notes/llm-coding-workflow-2026/) works through the same territory from the day-to-day practitioner side, spec.md and plan.md files, small iterative chunks, heavy context packing, where this piece works through the underlying paper's framing.

## Reading notes

- Agent context splits into six types (instructions, knowledge, memory, examples, tools, guardrails), and the load-bearing decision is what goes in static context (loaded every turn, expensive) versus dynamic context (loaded on demand via Agent Skills, cheap per turn).
- Verification is what separates vibe coding from agentic engineering on the same underlying agent. Tests cover deterministic input-output pairs; evals split into output evaluation (is the result correct) and trajectory evaluation (was the path to it sound).
- The lifecycle compresses unevenly: implementation drops from weeks to hours, but requirements, architecture and verification stay slow because they're judgment work, so specification quality becomes the new bottleneck.
- A METR study found experienced developers 19% slower on some tasks once review and fixing time is counted, even as surveyed productivity gains land at 25-39%. The two can coexist because part of the time shifts from writing code to reviewing it.
- The economics flip the usual intuition: vibe coding is cheap to start and expensive to run (token burn, maintenance tax, security cleanup), while agentic engineering costs more upfront and less per feature after a crossover point the paper estimates at 3 to 10x per feature.
- Google's Agents CLI folds building, evaluating and deploying a production agent into the same terminal workflow used for throwaway scripts, coordinating through MCP for tools and A2A for handing work between agents.
- As of early 2026, cited adoption numbers put regular AI coding agent use at 85% of professional developers, 51% using them daily, and roughly 41% of new code AI-generated.
