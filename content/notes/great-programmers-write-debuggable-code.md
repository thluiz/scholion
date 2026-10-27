---
title: "Great Programmers Write Debuggable Code"
date: '2013-09-27T10:17:58-03:00'
category: webclip
summary: 'The post argues that good programmers add logging and tools that make failures easier to debug, because when code breaks, useful logs help narrow down the cause without needing a special debug build.'
tags: ["debugging", "logging", "software-development"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Great Programmers Write Debuggable Code | Henrik Warne's blog"
    url: "http://henrikwarne.com/2013/05/05/great-programmers-write-debuggable-code/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2013-09/henrikwarne-com--great-programmers-write-debuggable-code.md"
    kind: repo
---

Great programmers build logging into programs so failures can be observed and traced. The post says that when software works, logging quality may look similar across programmers, but when it fails the difference becomes clear.

It gives two examples: a case where a missing explanation in the logs led someone to suggest making a debug version, and a routing system where detailed logs show the candidate routes and why each one was eliminated. It also says programmers may neglect debuggable code because they do not expect failures, do not test enough cases, or do not troubleshoot their own systems in production.

## Reading notes

- Logging should make it possible to see what a program is doing, especially when something goes wrong.
- A good log should give clues about why a failure happened, not just record that a failure occurred.
- In the SMS routing system, the log lists possible routes, their costs, and the reasons routes were eliminated.
- Detailed logs make it easier to understand why route A was chosen instead of route B.
- Some cases still require a debug version, but regular logging should at least point toward the problem.
- The post links debuggable code to humility, thorough testing, and experience troubleshooting production systems.
