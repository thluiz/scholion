---
title: "Working Effectively With Legacy Code"
date: '2023-11-12T06:26:21+00:00'
category: webclip
summary: 'Thread summarizes key ideas from Michael Feathers’ book on working with legacy code: definition as code without tests, reasons to change software, a 4‑step change algorithm, and techniques like seams, sprout, and wrap methods/classes.'
tags: ["legacy-code", "software-engineering", "unit-testing", "refactoring"]
has_commentary: false
generated_by: "openai/gpt-5.1"
sources:
  - title: "Thread by @milan_milanovic: 𝗪𝗼𝗿𝗸𝗶𝗻𝗴 𝗘𝗳𝗳𝗲𝗰𝘁𝗶𝘃𝗲𝗹𝘆 𝗪𝗶𝘁𝗵 𝗟𝗲𝗴𝗮𝗰𝘆 𝗖𝗼𝗱𝗲 In his book \"Working Effectively With Legacy Code,\" M…"
    url: "https://x.com/milan_milanovic/status/1721837211794997519"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2023-11/x-com--working-effectively-with-legacy-code-thread.md"
    kind: repo
---

Short thread summarizing key ideas from Michael Feathers’ book "Working Effectively With Legacy Code." It notes that although the book is from 2004, its guidance on using focused, incremental unit testing and refactoring to improve legacy software while adding new features still holds up. Legacy code is defined as code without tests, which makes safe changes harder because unintended side effects and regressions are difficult to detect. The author lists four reasons to change software, introduces the Legacy Code Change Algorithm, and outlines several practical techniques such as seams, sprout methods/classes, and wrap methods/classes.

## Reading notes

- The thread presents Michael Feathers’ book as guidance for working with legacy software, emphasizing that despite being from 2004 it still contains valuable points.
- The book encourages using focused, incremental unit testing and refactoring so teams can improve testability, comprehension, and extensibility of legacy systems while delivering new functionality.
- Legacy code is defined as code without tests, highlighting that lack of tests makes it difficult to ensure changes do not introduce unintended side effects or break existing behavior.
- Four reasons to change software are listed: adding a feature, fixing a bug, improving the design through refactoring, and optimizing resource usage.
- The thread stresses that when code is altered, behaviors that are not intentionally being changed must still be preserved.
- The main contribution highlighted is the Legacy Code Change Algorithm, described as a structured approach for modifying legacy code safely.
- Step 1 of the algorithm is to identify the targeted legacy code by finding change points (seams) relevant to the change or addition and locating test points where behavior can be observed.
- Step 2 is to get the targeted legacy code into a test harness and cover it with tests, which involves carefully breaking dependencies and writing characterization unit tests for that code.
- Step 3 is to add new functionality guided by new tests, following a Test Driven Development (TDD) process.
- Step 4 is to refactor the code that is now under tests to remove duplication and clean it up.
- The thread summarizes the technique of identifying seams as finding places where behavior can be changed without modifying the surrounding code, at class, method, or function level, to isolate parts for testing and refactoring.
- Sprout method and sprout class are described as techniques where new functionality is placed in a new method or class instead of directly editing existing code, then unit tested and invoked from an identified insertion point in the legacy code.
- Wrap method and wrap class are described as creating a new method or class with the same signature that delegates to the original renamed one, allowing new logic to run before or after calling the old behavior.
- The second tweet invites readers to subscribe to the author’s free weekly newsletter for further learning and includes a link to the newsletter site.
