---
title: "Thoughts on Claude Code - Slava Akhmechet"
date: '2026-01-08T17:09:34+00:00'
category: webclip
summary: 'The author describes using Claude Code to build Beep, highlighting refactors, design help, and parser work, while noting limits on newline-sensitive grammar and npm publishing.'
tags: ["claude-code", "programming", "parser-combinators", "beep-lang"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Thoughts on Claude Code - Slava Akhmechet"
    url: "https://spakhm.com/claude-code?utm_source=tldrai"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-01/spakhm-com--thoughts-on-claude-code-slava-akhmechet.md"
    kind: repo
---

The post argues that Claude Code is most useful as a programming partner for medium-complexity work. It helped with refactors, design choices, and parser tasks, but still got stuck on a few harder edge cases. The author says it made coding faster and more enjoyable without replacing the need to understand the problem.

## Reading notes

- The author built Beep during winter break and wrote most of it with Claude Code/Opus 4.5.
- For lexical scoping and shadowing, Claude suggested changing the interpreter to return the current frame along with the value, which removed the need for explicit state tracking.
- For dynamic scoping, Claude suggested adding a set to each lexical binding frame so the interpreter can track which dynamic variables were introduced there.
- Claude was especially strong on parser work, including adding new syntax and fixing keyword parsing issues in `ts-parsec`.
- The author says Claude did not make the codebase well-structured on its own, but it was very effective at obscure parser tasks and type-system-heavy code.
- Claude got stuck on newline sensitivity in the grammar because the underlying parser library lacked support for keeping newlines.
- Claude also failed to resolve an npm publishing issue for a scoped package, which the author eventually fixed by reading the docs.
- The author argues that AI lowers the cost of refactors, brainstorming, and annoying maintenance work, and that this made the project better than it would have been otherwise.
- He concludes that Claude Code is a strong companion for problems at about a good undergraduate level, even though it still has clear limits.
