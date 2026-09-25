---
title: "The Secret Life of JavaScript: The Generator"
date: "2026-09-23T14:23:36+01:00"
category: webclip
has_commentary: false
summary: "Explains JavaScript generator functions through a teaching dialogue: the yield keyword, the {value, done} object, the iterator protocol, and passing values back in via .next()."
tags:
  - javascript
  - generators
  - iterators
  - async-programming
sources:
  - title: "The Secret Life of JavaScript: The Generator - DEV Community"
    url: "https://dev.to/aaron_rose_0787cc8b4775a0/the-secret-life-of-javascript-the-generator-1fi5?context=digest"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/dev-to--the-secret-life-of-javascript-the-generator.md"
    kind: repo
---

Aaron Rose's post walks through JavaScript generator functions using a teaching dialogue between two characters, Timothy and Margaret. Timothy needs a function that hands out a new unique ID every time it's called, but runs into JavaScript's run-to-completion rule: an ordinary function can't pause partway through, so a `while (true)` loop that tries to keep counting state alive freezes the browser instead of yielding values one at a time.

Margaret's fix is the generator function, marked with an asterisk (`function*`). Unlike an ordinary function, calling it doesn't run the body straight through. It returns a generator object that yields control back to the caller at each `yield`, preserving local state like the loop counter across pauses.

Related: [Should Junior Developers Still Learn JavaScript the Hard Way?](/notes/should-junior-devs-still-learn-javascript-hard-way/) argues for learning closures, scope, and the event loop before frameworks, a different JavaScript fundamental than generators but the same case for understanding the language itself.

## Reading notes

- `yield` doesn't end the function. It pauses execution, saves the local variables, and hands a value to the caller; execution resumes exactly where it left off on the next call.
- Calling a generator function doesn't run its body. It returns a Generator Object, and the function only starts executing once `.next()` is called on that object.
- `.next()` returns a `{ value, done }` object: `value` is whatever the function yielded, `done` reports whether the generator has finished, staying `false` throughout an infinite generator like the ID example.
- Because generators implement the standard iterator protocol, they can be consumed directly with `for...of`, and a `break` inside that loop stops an otherwise infinite generator from the outside.
- The post calls this lazy evaluation: in the ID generator example, each number only gets computed when `.next()` is called, instead of a million IDs being generated and held in memory up front.
- Communication runs both ways: a value passed into `.next(value)` becomes what the paused `yield` expression evaluates to on resume, letting the caller send data, like a reset signal, back into the generator.
- The post closes by flagging async generators, used for handling network requests, as a separate topic saved for a future post.
