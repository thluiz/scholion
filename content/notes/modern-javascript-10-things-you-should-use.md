---
title: "Modern JavaScript, 10 things you should be using, starting today"
date: '2026-11-17T19:41:29+00:00'
category: webclip
summary: 'Overview of ten ES6+ JavaScript features (spread/rest, template literals, object shorthand, destructuring, array helpers, promises, async/await, modules, arrow functions) with short explanations and code examples.'
tags: ["javascript", "es6", "language-features"]
has_commentary: false
generated_by: "openai/gpt-5.1"
sources:
  - title: "Modern JavaScript, 10 things you should be using, starting today"
    url: "https://web.archive.org/web/20191210040946id_/https://dev.to/itnext/modern-javascript-10-things-you-should-be-using-starting-today-22dp"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/web-archive-org--modern-javascript-10-things-you-should-use.md"
    kind: repo
---

The article introduces ten ES6+ JavaScript features the author recommends for everyday use, especially for developers returning to or starting with modern JavaScript. For each feature, it contrasts ES5-style patterns with newer syntax, showing how spread/rest parameters, template literals, shorthand/method properties, destructuring, newer array methods, promises with async/await, ES modules, and arrow functions simplify code and improve readability. It closes by noting these are the author's favorite features to adopt now.

## Reading notes

- Author positions the piece for both newcomers and developers who have used JavaScript sporadically, stressing that the language has changed and some features should now be used daily.
- Recommends two ES6+ reference resources: ES6 Features (es6-features.org) and MDN’s JavaScript reference.
- Explains the spread operator (`...`) as turning arrays or objects into comma-separated lists, with examples of appending one array to another and cloning/augmenting objects instead of manual loops.
- Shows that without array spread one would loop over `firstHalf` and `push` into `secondHalf`, and without object spread one would iterate `Object.keys(hero)` and assign properties manually.
- Defines rest parameters as collecting remaining function arguments into an array, contrasting with the older `arguments` object and demonstrating a function that sums all parameters with `reduce`.
- Highlights that rest parameters both name the collected arguments and make the intent explicit, whereas `arguments` has existed since at least ES5 but is less known.
- Presents string interpolation with template literals as a cleaner alternative to concatenating multiline strings with `+` and `\n` in a `getDescription()` method.
- Notes that backticks define multiline strings and `${}` inserts expressions into templates, improving readability for complex string construction.
- Introduces object shorthand properties by comparing an ES5-style factory function returning `{ x: x, y: y }` to an ES6 version returning `{ x, y }`, emphasizing reduced clutter when key and variable names match.
- Describes method properties shorthand: instead of `add: function(a,b) {}`, one can write `add(a,b) {}` within an object literal for methods like `add`, `sub`, and `multiply`.
- Motivates destructuring as a way to reduce repetitive property access and help developer “sanity” when pulling values from objects and arrays.
- Shows object destructuring of `req` to extract `body.name`, `body.description`, and `url` into named variables in a single line, replacing several individual assignments.
- Demonstrates array destructuring to pull specific positions (e.g. first and third element) and collect remaining elements with rest syntax, instead of indexing like `array[0]` and `array[2]`.
- Points out that skipping elements in array destructuring uses extra commas and that rest `...remaining` can gather leftover items into an array.
- Illustrates parameter destructuring by changing a function from `doSomething(config)` with `config.a`, `config.b`, `config.c` checks to `doSomething({ a, b, c })`, simplifying access to options.
- Lists useful ES6 array methods: `find()` to retrieve an item or null, `findIndex()` for its index, `some()` to test if any element matches a predicate, and `includes()` to check membership.
- Provides examples using an array of objects to demonstrate `find`, `findIndex`, and `some` (for a `checked` flag), plus a numeric array to show `includes`.
- Recaps the older callback-based pattern for asynchronous code using a `doSomething(cb)` function with `setTimeout` and invoking the callback after completion.
- Rewrites the same asynchronous behavior using native Promises: `doSomething` returns a `new Promise` that calls `resolve('done')` after a timeout, then consumed with `.then`.
- Shows promise chaining for sequential async operations (`getUser`, `getOrderByUser`, `getOrderItemsByOrder`) that pass results through successive `.then()` calls.
- Introduces `async/await` to make asynchronous flows look synchronous, rewriting the chained calls into an `async function getItems()` with successive `await` statements.
- Uses a `try/catch` block in the async example to illustrate centralized error handling and notes that the async function still returns a promise consumed with `.then`.
- Explains module syntax using `export` and `export default` in `math.js`, defining named exports `add` and `sub` plus a default export that multiplies two numbers.
- Demonstrates importing modules in `main.js` with `import mult, { add, sub } from './math';`, calling the imported functions and showing their expected results in comments.
- Describes arrow functions as a new function notation, comparing a traditional `function printArray(arr) {}` to `const printArray = (arr) => {}`.
- Gives a one-line arrow function example `const add = (a,b) => a + b` where the expression result is implicitly returned, and another that returns an object literal using parentheses.
- Discusses the lexical `this` behavior of arrow functions by first showing a problem in a `sum` function where `this` inside a regular `forEach` callback does not refer to the outer context.
- Notes the common workaround of assigning `var self = this;` and using `self.total` inside the callback, describing it as a hacky but historically used solution.
- Shows how converting the `forEach` callback to an arrow function `(item) => { this.total += item; }` causes `this` inside the callback to correctly reference the outer `sum` function’s `this`.
- Concludes by stating there are many more ES6+ features, but highlights these as the author’s favorite ones to adopt right away.
