---
title: "What the Team Behind Cursor Knows About the Future of Code"
date: '2026-09-25T08:41:20+01:00'
category: webclip
summary: 'Cursor’s team argues that code work is shifting from typing in an IDE to directing and reviewing AI agents, with planning, model choice, and long-running workflows becoming central.'
tags: ["cursor","ai-coding","software-development","ai-agents"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "What the Team Behind Cursor Knows About the Future of Code"
    url: "https://every.to/source-code/what-the-team-behind-cursor-knows-about-the-future-of-code?utm_source=substack&utm_medium=email"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/every-to--what-team-behind-cursor-knows-about-future-of-code.md"
    kind: repo
---

Cursor’s team describes a post-IDE workflow where developers spend less time typing code by hand and more time planning work, directing agents, and reviewing what they produce. They also say cloud and local agents are starting to blend, and that choosing the right model matters more than prompt tricks.

## Reading notes

- The IDE continues to exist, but the center of the work is shifting to the agent interface, where conversation with the AI becomes the main part of the process.
- In some cases, writing code by hand may represent only a small part of the work time, while the rest goes to guiding the AI and reviewing the result.
- The model and the harness matter together, because the infrastructure around the model defines how it receives context, handles errors, and executes long tasks.
- The team tested this limit with a web browser built from scratch by agents, in a task that ran for weeks, generated 3 million lines of code, and cost about 80 thousand dollars in tokens.
- The group works to allow an agent to start on the local computer, continue in the cloud, and then resume on the user’s computer without losing context.
- Before coding, Sam spends time in plan mode to detail what she wants to build, using designs and screenshots when the project is more complex.
- For larger projects, she divides the work among several agents in parallel; for simple fixes, she sometimes skips planning.
- Sam chooses models by her own heuristics: Claude Opus for brainstorming and poorly specified problems, GPT 5.2 Codex High for bug-finding and very literal tasks.
- When necessary, she runs several models at the same time, compares the responses, and asks one to justify the approach before another.
- Cursor includes review tools, such as find issues and Bugbot, and the internal team does not merge before addressing all of Bugbot’s comments.
- Sam prefers a retrieval first approach, with pointers to conversations and plan documents, instead of relying only on compressed summaries.
- The promise of agents becomes stronger in complex and multi-step tasks; for direct translation from Figma to code, the gains are still limited.
