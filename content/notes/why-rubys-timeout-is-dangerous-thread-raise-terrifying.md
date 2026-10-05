---
title: "Why Ruby’s Timeout is dangerous (and Thread.raise is terrifying)"
date: '2015-12-08T15:54:47-03:00'
category: webclip
summary: 'Julia Evans argues that Ruby’s Timeout is unsafe because it can interrupt arbitrary code at any point via Thread.raise, which may break cleanup, rescue blocks, and stateful operations.'
tags: ["ruby", "timeout", "threading", "exceptions"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Why Ruby’s Timeout is dangerous (and Thread.raise is terrifying) - Julia Evans"
    url: "http://jvns.ca/blog/2015/11/27/why-rubys-timeout-is-dangerous-and-thread-dot-raise-is-terrifying/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2015-12/jvns-ca--why-rubys-timeout-is-dangerous-thread-raise-terrifying.md"
    kind: repo
---

Julia Evans says Ruby’s Timeout looks convenient, but it works by starting another thread and using Thread.raise to interrupt the target thread after a delay. That means an exception can arrive during normal work, cleanup, rescue code, or object creation, so arbitrary code cannot defend against it safely.

She compares this with other languages: Java deprecated and disabled Thread.stop, Python’s interrupt_main is limited, C#’s Thread.Abort is considered dangerous, and C++ threads are not interruptible. Her conclusion is that a general timeout API that can stop any block of code is flawed, and that Ruby’s documentation should warn more strongly.

## Reading notes

- Timeout auto-terminates a potentially long-running operation after a fixed time.
- Its implementation starts a thread and raises an exception in the original thread when the time is up.
- Thread.raise can trigger an exception while network requests, cleanup, rescue blocks, or later database work are running.
- The problem is not just Ruby’s implementation; interrupting an arbitrary block of code is unsafe in general.
- Java’s interrupt model is presented as safer because interruption is only observed at specific points.
- The post suggests Ruby documentation should use stronger warning language about Timeout and Thread.raise.
