---
title: "How To Handle Exceptions With Aspect Programming And Blame Covfefe"
date: '2026-09-25T00:21:09+01:00'
category: webclip
summary: 'The text shows how to use AOP with kaop-ts to handle exceptions and other common concerns in one place, access join point metadata, and even inject asynchronous data into decorated methods.'
tags: ["aspect-oriented-programming","kaop-ts","exceptions","react"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "How To Handle Exceptions With Aspect Programming And Blame Covfefe"
    url: "https://dev.to/k1r0s/how-to-handle-exceptions-with-aspect-programming-and-blame-covfefe"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/dev-to--how-to-handle-exceptions-with-aspect-programming-and-blame-c.md"
    kind: repo
---

The page uses kaop-ts to show how Aspect Oriented Programming can centralize exception handling and other repeated concerns. It first decorates a React render method to append text to an exception, then shows an advice that can replace the result with an error component. The rest of the text explains that AOP helps manage common problems in one place, gives access to join points and metadata, and can work with async requests while keeping the code declarative.

## Reading notes

- The initial example uses `onException` and `afterMethod` to handle an error thrown in the `render` of a React component.
- The `Advices` class shows two actions: one changes the exception message and the other rethrows the exception when it exists.
- The text says that AOP serves to deal with common problems in one place and access the necessary context.
- The author links AOP to reducing repetition and organizing logic at several execution points called join points.
- The article states that frameworks already handle many common problems, and cites Express as an example in NodeJS environments.
- The text compares modern frameworks such as Vue, Angular, and React, highlighting declarative programming and fewer side effects.
- The kaop-ts library is presented as a way to build large applications with more abstraction and access to join points.
- The text lists the available join points as `AfterInstance`, `BeforeInstance`, `AfterMethod`, `BeforeMethod`, and `OnException`.
- The `Registry` example shows that an advice can read `args`, `propertyKey`, `scope`, `rawMethod`, `target`, and `result`.
- The author says that this data can be read and written and that it is also possible to make asynchronous requests without messing up the call stack.
- In the example with `View` and `PersistanceAdvices`, the `update` method receives data from a request inserted by the advice.
- The text explains that `this.next` indicates to kaop-ts that the current operation still needs to finish before the next ones continue.
