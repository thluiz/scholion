---
title: "The Art of Debugging"
date: '2015-10-16T09:26:34-03:00'
category: webclip
summary: 'Remy Sharp argues that debugging is learned through experience and shows a practical workflow: replicate the bug, isolate the cause, then eliminate it with tools and tests.'
tags: ["debugging", "javascript", "chrome-devtools", "web-development"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "The Art of Debugging"
    url: "https://remysharp.com/2015/10/14/the-art-of-debugging"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2015-10/remysharp-com--the-art-of-debugging.md"
    kind: repo
---

Remy Sharp presents debugging as a skill built through repeated exposure to bugs rather than through a single trick. He says the useful sequence is to replicate the problem, isolate the cause, and then eliminate it, often by reducing the problem to a smaller case and, when possible, turning it into a failing test.

## Reading notes

- The article accompanies his 2015 Art of Debugging talk from Fronteers in Amsterdam.
- He says there is no silver bullet for debugging and that experience matters more than rules.
- He describes learning from bugs over time, including work on bugs for new employees at a company where this became the fastest way to gain practical experience.
- He notes that framework-heavy apps can require different tools, especially sourcemaps and framework-specific devtools.
- He says he rarely cross-browser tests because much of his work is plain JavaScript that should behave the same everywhere.
- He breaks debugging into three steps: replicate, isolate, and eliminate.
- Replication starts with confirming the bug, then gathering details about the user’s environment and the steps that led to the problem.
- Incognito mode and multiple browser profiles help rule out extensions, cookies, storage, and security settings.
- Isolation means stripping away anything unnecessary, such as disabling extensions one by one or pulling code into a smaller test case.
- Elimination often means writing a failing test and fixing the bug against that test.
- When a bug cannot be replicated, he treats it as a possible Heisenbug and considers whether the test environment or the debugger itself is affecting the result.
- He divides debugging approaches into inside out, where the source is known, and outside in, where the visual problem is known but the source is not.
- His preferred tools include Workspaces and real-time updates, console shortcuts, timeline screenshots, network inspection and replay, DOM breakpoints, throttling, and memory profiling.
- For memory leaks, he suggests comparing heap dumps and looking for items that remain after garbage collection.
- He ends by saying debugging has no single solution and that stepping away from the computer can also help solve problems.
