---
title: "Programmers, Don't Use Windows!"
date: '2025-10-28T22:11:18+00:00'
category: webclip
summary: 'The post argues that macOS fits programming better because it inherits Unix abstractions, POSIX tools, pipelines, and shell workflows, while Windows grew from different assumptions and stays more GUI-centered.'
tags: ["macos", "windows", "unix", "pipelines"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Programmers, Don't Use Windows!"
    url: "https://www.yegor256.com/2025/10/05/windows-vs-macos.html"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2025-10/yegor256-com--programmers-dont-use-windows.md"
    kind: repo
---

The post argues that current macOS and Windows are both solid systems, but that macOS fits programmers better because it is built on Unix foundations. It presents Unix as the source of files, processes, pipelines, and composable command-line tools, and says macOS inherits that model through NeXTSTEP.

## Reading notes

- The author says he still believes Windows is not suitable for programmers and that a professional programmer should use macOS instead.
- He lists POSIX compliance, native Unix tools, Homebrew, terminal apps, Docker behavior, SSH key integration, and predictable Git behavior as advantages of macOS.
- He traces Unix to Bell Labs and credits Ken Thompson and Dennis Ritchie with the ideas of “everything is a file,” pipelines, and one-tool-per-task programs.
- He describes CP/M and MS-DOS as systems for small single-user machines, then says Windows began as a GUI on top of MS-DOS.
- He says Windows NT later moved away from DOS and gained features like protected memory and kernel/user separation, but still is not Unix.
- He says macOS comes from NeXTSTEP, inherited by Apple through NeXT, and that modern macOS remains POSIX-compliant and Unix-like.
- He contrasts Unix’s uniform file-based abstractions with Windows objects and says this makes composition and shell pipelines easier on Unix.
- He uses a Unix pipeline example with git log, grep, sort, uniq, and head to show how command-line tools can be composed.
- He argues that GUI work makes users consumers, while CLI work makes them creators, because shell commands can be reasoned about, automated, combined, and kept over time.
