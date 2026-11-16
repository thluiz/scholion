---
title: "Pure Bash Bible"
date: '2019-09-23T10:29:45+00:00'
category: webclip
summary: 'A reference of built-in Bash techniques that replace external commands, reduce dependencies, and often run faster, with tested snippets for common scripting tasks.'
tags: ["bash", "shell-scripting", "builtins", "performance"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "GitHub - dylanaraps/pure-bash-bible: 📖 A collection of pure bash alternatives to external processes."
    url: "https://github.com/dylanaraps/pure-bash-bible"
    kind: repo
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/github-com--pure-bash-bible.md"
    kind: repo
---

A reference of built-in Bash techniques that replace external processes and programs. The book says Bash can handle many common tasks without external dependencies, which can make scripts faster and easier to understand.

## Reading notes

- Collects pure Bash alternatives to external commands and programs.
- Says external processes are expensive in Bash and can slow scripts down.
- Presents snippets as function examples for use in scripts.
- Notes that snippets are linted with shellcheck and tests are written where applicable.
- Invites contributions through the repository’s contributing guide.
- Covers strings, arrays, loops, file handling, file paths, variables, escape sequences, parameter expansion, brace expansion, conditionals, arithmetic operators, traps, performance, obsolete syntax, internal variables, terminal information, conversion, code golf, and other utilities.
- Includes examples for trimming strings, splitting text, changing case, handling files, counting lines, working with paths, using traps, reading terminal size, converting colors, and checking whether a program is in PATH.
- Recommends using built-ins like `printf`, parameter expansion, globbing, and traps instead of external tools when possible.
- Advises using `#!/usr/bin/env bash`, `$()` command substitution, and function declarations without the `function` keyword for compatibility.
- Notes that Unicode can be disabled for a performance increase in some cases.
- Ends by encouraging readers to donate or share the repository if it helped.
