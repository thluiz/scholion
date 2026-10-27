---
title: "PyCharm: Dynamic runtime type inference in PyCharm 2.7"
date: '2013-02-14T15:27:21-03:00'
category: webclip
summary: 'PyCharm 2.7 can collect type information while debugging and reuse it for code completion, code insight, quick documentation popups, and generated docstrings, if the feature is enabled.'
tags: ["pycharm", "dynamic-type-inference", "debugger", "docstrings"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "PyCharm: Dynamic runtime type inference in PyCharm 2.7"
    url: "https://blog.jetbrains.com/pycharm/2013/02/dynamic-runtime-type-inference-in-pycharm-2-7/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2013-02/blog-jetbrains-com--pycharm-dynamic-runtime-type-inference-in-pycharm-2-7.md"
    kind: repo
---

PyCharm’s debugger can collect type information at runtime and feed it back into code completion, code insight, quick documentation popups, and docstring generation. The feature must be enabled in debugger settings, and JetBrains warns that it may affect debugger performance.

## Reading notes

- Enable “Collect run-time types information for code insight” in debugger settings before running the debugger.
- While debugging, PyCharm records the types used when execution steps into a function.
- The collected types can be used for auto-completion during the same debugger session.
- PyCharm also uses the collected runtime types outside the function body, together with its static type inference.
- If different calls use different argument types, PyCharm remembers all encountered variants.
- Quick Documentation Lookup shows the inferred types when the caret is on a symbol and Ctrl+Q is pressed.
- The debugger-collected type information can also be used to generate docstrings.
- To generate docstrings with types, place the caret inside the function body and press Alt+Enter, then choose “Generate docstrings with types.”
