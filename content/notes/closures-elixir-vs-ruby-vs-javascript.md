---
title: "Closures: Elixir vs. Ruby vs. JavaScript"
date: '2015-06-14T19:27:54-03:00'
category: webclip
summary: 'The page compares closure behavior in JavaScript, Ruby, and Elixir. JavaScript shows side effects from mutable state, Ruby is safer with iterators but not perfect, and Elixir benefits from immutability.'
tags: ["closures", "javascript", "ruby", "elixir"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Closures: Elixir vs. Ruby vs. JavaScript"
    url: "https://www.amberbit.com/blog/2015/6/14/closures-elixir-vs-ruby-vs-javascript/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2015-06/amberbit-com--closures-elixir-vs-ruby-vs-javascript.md"
    kind: repo
---

The page argues that closures behave very differently across JavaScript, Ruby, and Elixir. In JavaScript, mutable state can produce unexpected results when a closure captures a loop variable. Ruby avoids that in common iterator patterns, but the same issue can still appear with bare language constructs. Elixir is presented as the safest of the three because immutable data structures prevent the captured value from changing later.

## Reading notes

- JavaScript closures keep the environment where they were defined, so a loop variable can end up with the last mutated value in every function call.
- The usual workaround in JavaScript is to wrap the anonymous function in another anonymous function to create a new context.
- Ruby’s built-in iterators can avoid the problem, but the same closure issue appears when using simpler language constructs.
- Elixir uses immutable data structures, so reusing a variable label does not change the earlier values that closures reference.
- The author recommends using iterators in JavaScript and Ruby and says functional programming habits can reduce headaches.
- The page ends by encouraging readers to learn Elixir.
