---
title: "The Fundamental Law Of Software Dependencies"
date: '2026-09-25T17:53:36+01:00'
category: webclip
summary: 'The article argues that canonical source code should include checksums for every dependency, including transitive libraries and the compiler, so builds become reproducible and trust shifts from distributors to hashes.'
tags: ["software-dependencies", "checksums", "reproducible-builds", "git"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "The Fundamental Law Of Software Dependencies"
    url: "https://matklad.github.io/2024/09/03/the-fundamental-law-of-dependencies.html?ref=dailydev"
    kind: repo
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/matklad-github-io--the-fundamental-law-of-software-dependencies.md"
    kind: repo
---

The article states that canonical source code should include checksums for all dependencies. That includes the source tree itself, third-party libraries, transitive dependencies, and the compiler. It also says a compiler manifest can hold platform-specific hashes, with downstream consumers verifying the manifest hash and then the binary hash for their platform.

## Reading notes

- The source tree itself should be hashed, which implies a content-addressed VCS such as git.
- Third-party libraries need a lockfile that covers the full dependency set and includes checksums.
- The lockfile is part of source code and is mixed into the VCS root hash.
- The compiler hash should be included in the lockfile, not just its version.
- Specifying both version and hash lets users trust the checksum instead of the distributor.
- Compiler distribution can use a manifest listing platform-specific hashes, with consumers verifying the manifest hash first.
- The law is an instrumental goal rather than an end in itself.
- Reaching known hashes requires identifying dependencies, automating downloads, making builds reproducible, and isolating dependencies per project.
- These are the changes the article says actually make software development easier.
