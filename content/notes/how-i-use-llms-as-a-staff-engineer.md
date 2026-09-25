---
title: "How I use LLMs as a staff engineer"
date: '2026-09-25T22:47:22+01:00'
category: webclip
summary: 'The author uses LLMs as smart autocomplete, a tutor for new domains, a fallback for bugs, and a proofreading tool, while avoiding them for full drafts and familiar production work.'
tags: ["llms", "software-engineering", "copilot", "learning"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "How I use LLMs as a staff engineer"
    url: "https://www.seangoedecke.com/how-i-use-llms/?utm_source=tldrnewsletter"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/seangoedecke-com--how-i-use-llms-as-a-staff-engineer.md"
    kind: repo
---

The post describes a practical, limited way of using LLMs in staff-engineer work. The author relies on them for boilerplate, unfamiliar tactical changes, throwaway research code, learning new topics, occasional bug hunting, and checking long-form writing for typos and logic errors. He avoids using them for work he can do better himself, such as production logic in familiar areas, full technical drafts, and large-codebase research.

## Reading notes

- Uses Copilot completions for code, mostly for boilerplate such as arguments and types
- Accepts more LLM help in unfamiliar languages or systems, but still asks a subject-matter expert to review the change
- Uses LLMs heavily for one-off research code that only needs to work once and does not need maintenance
- Treats the model as an on-demand tutor for learning new domains, asking follow-up and self-check questions
- Feeds learning notes back to the LLM for review and correction
- Uses Copilot chat as a last resort when stuck on a bug, usually only once and without much iteration
- Uses LLMs to review drafts for typos and logic mistakes, but does not let them write the documents
- Avoids using LLMs for full PRs in familiar areas, ADRs, and research in large codebases
