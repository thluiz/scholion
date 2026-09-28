---
title: "JavaScript Concepts Every Programmer Should Know"
date: '2022-05-27T09:57:07-03:00'
category: webclip
summary: 'The article reviews core JavaScript ideas that make development easier, including arrow functions, reduce, asynchronous execution, async scripts, async/await, and promises.'
tags: ["javascript", "arrow-functions", "promises", "async-await"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "JavaScript Concepts Every Programmer Should Know | JavaScript in Plain English"
    url: "https://javascript.plainenglish.io/javascript-concepts-every-programmer-should-know-d04731fe7a7c"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2022-05/javascript-plainenglish-io--javascript-concepts-every-programmer-should-know.md"
    kind: repo
---

The article selects a few JavaScript fundamentals that are useful for beginners and experienced programmers alike. It focuses on language features and execution model details that help explain how JavaScript code is written and runs.

## Reading notes

- JavaScript is presented as the main language for the web, and the article argues that developers should still learn its fundamentals because some concepts are easier than others.
- Arrow functions are introduced as a shorter syntax than traditional functions, and the text shows that they can use rest parameters, default parameter values, and destructured object parameters.
- `reduce()` is described as a function that turns an array into a single value by passing each element the previous computed value, with an initial value available for the first step.
- The article says `reduce()` can be powerful but harder to read, so its benefits should be weighed against simpler code.
- JavaScript is described as synchronous by default and single-threaded, while asynchronous execution is used for long-running tasks and background work such as HTTP requests.
- The async script tag is explained as a way to load JavaScript without blocking HTML parsing, and it is kept separate from async/await.
- `async` marks a function as asynchronous, `await` is used to get the returned value, and the text notes that `await` can only be used inside async functions.
- The article says async/await is built on Promises.
- Promises are explained through the idea of a task that runs later and returns either a result or an error, with `then` and `catch` handling the outcomes.
- The example shows that asynchronous work does not block the rest of the code while it is being handled in the background.
