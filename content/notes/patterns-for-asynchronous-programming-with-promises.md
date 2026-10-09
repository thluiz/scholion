---
title: "Patterns for Asynchronous Programming with Promises"
date: '2014-04-25T18:02:19-03:00'
category: webclip
summary: 'The post shows promise-based patterns for running asynchronous work in parallel or in sequence, using map, Q.all, each, and reduce to control order and collect results.'
tags: ["promises", "asynchronous-programming", "javascript", "q"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Patterns for Asynchronous Programming with Promises | Joe Zim's JavaScript Blog"
    url: "http://www.joezimjs.com/javascript/patterns-asynchronous-programming-promises/?utm_source=javascriptweekly&utm_medium=email"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2014-04/joezimjs-com--patterns-for-asynchronous-programming-with-promises.md"
    kind: repo
---

The post lays out a few ways to handle asynchronous operations with promises. It starts with parallel work, either waiting for all operations before running synchronous steps in order, or attaching a callback to each promise so synchronous work happens as soon as each operation finishes. It then shows two sequential patterns, one built with each and one with reduce, both chaining each async step off the previous one and gathering results in an array.

## Reading notes

- Promises are presented as the main tool for asynchronous programming for now, especially when handling multiple operations.
- The examples use Q for promises and Underscore or Lodash for map, each, and reduce.
- For parallel async work followed by ordered synchronous processing, map creates the promise array and Q.all waits for completion before looping through the results.
- For parallel async work with unordered synchronous follow-up, map is used with a callback that calls then immediately after each async operation.
- For sequential async work, each chains promises one by one, storing the chain in a promise variable.
- The reduce version passes the promise chain as the memo and uses the same chaining approach.
- Both sequential patterns use a blank resolved promise to start the chain.
- Both sequential patterns push new values into an array and return that array at the end.
