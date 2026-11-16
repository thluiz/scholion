---
title: "It's probably time to stop recommending Clean Code"
date: '2020-07-05T14:10:30+00:00'
category: webclip
summary: 'The essay argues that Clean Code mixes useful advice with dated or questionable prescriptions, and that its own code examples often undermine the rules the book promotes.'
tags: ["clean-code", "software-design", "java", "code-quality"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "It's probably time to stop recommending Clean Code"
    url: "https://qntm.org/clean"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/qntm-org--its-probably-time-to-stop-recommending-clean-code.md"
    kind: repo
---

The essay argues that _Clean Code_ mixes solid advice with dated or questionable claims, and that its own examples often violate the rules it teaches. It focuses on chapter 3, the testing chapter, the objects-versus-data chapter, and the prime-number example to show how the book can be hard to trust as guidance.

## Reading notes

- The author says judgments about "clean code" are necessarily subjective, but the main objection is that much of the example code in the book is bad.
- Chapter 3 gives useful advice about descriptive names, single responsibility, commands versus queries, and avoiding side effects, but it also pushes claims that the author finds questionable.
- The book argues for very small functions, no nested control structures, and minimal arguments, but the author sees this as exaggerated and often impractical.
- The FitNesse refactoring example is presented as a preferred solution, yet the author says it is full of tiny methods that depend on hidden state and are hard to follow.
- The code mutates member variables and also destructively changes passed-in `pageData`, which the author says is buried by the refactoring instead of clarified.
- The book is described as dated in scope and style, with filler chapters, a heavy focus on Java and object-oriented code, and little relevance to newer practice.
- The unit-testing chapter is criticized for turning a clear test into a compressed domain-specific helper that obscures behavior instead of explaining it.
- The book’s treatment of data structures is said to use a narrow, unusual definition, while ignoring common structures such as arrays, lists, maps, trees, graphs, stacks, and queues.
- The prime-number example is used as another case where the book’s recommended style produces code that is hard to read, hard to reason about, and questionable as an algorithm.
- The author concludes that the book is not worth recommending, even as a beginner text or historical snapshot.
- In the update, the author says _A Philosophy of Software Design_ was a better experience and is more likely to age well.
- In the afterword, the author rejects the defense that readers can simply ignore the bad parts, arguing that beginners are the audience most likely to be misled by the book.
