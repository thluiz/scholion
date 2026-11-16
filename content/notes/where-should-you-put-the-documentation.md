---
title: "Where should you put the documentation?"
date: '2020-08-26T19:31:12+00:00'
category: webclip
summary: 'The post argues that good documentation is easy to find, easy to read, and easy to write. It recommends one place for shared docs, codebase-specific docs in the repo, and a low-friction way to keep everything current.'
tags: ["documentation", "knowledge-sharing", "confluence", "notion"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Where should you put the documentation? - Change Messy Software Without Breaking It"
    url: "https://understandlegacycode.com/blog/where-to-put-documentation"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/understandlegacycode-com--where-should-you-put-the-documentation.md"
    kind: repo
---

The post says documentation is often neglected in legacy codebases, but it matters because teams forget what only one person knows. It answers where to put it by separating codebase-specific material from everything else and by favoring a single, consistent place for shared knowledge.

## Reading notes

- Great documentation is easy to find, easy to read, and easy to write.
- Documentation should live in a single place when possible, so people are not searching across wikis, docs, emails, and tickets.
- Search needs to be strong enough that people can find specific information by themselves.
- Documentation should stay short, readable, and skimmable, with only the details that matter.
- The content should be easy to update, because heavy validation slows updates and makes docs stale.
- Out-of-date documentation should be corrected or removed.
- Change history and frequent backups help people update docs without fear of losing information.
- Codebase-specific instructions should be versioned with the source code, in a README or similar file.
- Architectural decisions should be documented in ADRs.
- Everything else should be kept in one place chosen consistently by the team or company.
- If there is no standard, the team should decide on one location and make that clear.
- As of 2020, the author recommends Notion because it supports search, formatting, in-place editing, collaboration, and change history.
- The post ends by warning against perfectionism and saying useful knowledge in one place is enough to start.
