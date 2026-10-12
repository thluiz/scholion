---
title: "Ruby Gotchas that will come back to haunt you"
date: '2014-03-05T11:04:25-03:00'
category: webclip
summary: 'The page lists Ruby pitfalls that can change program behavior or hide bugs, from operator precedence and equality to `super`, exceptions, scope, bang methods, assignment return values, and class-method privacy.'
tags: ["ruby", "ruby-on-rails", "gotchas", "language-subtleties"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Ruby Gotchas that will come back to haunt you"
    url: "http://blog.elpassion.com/ruby-gotchas/?utm_source=rubyweekly&utm_medium=email"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2014-03/blog-elpassion-com--ruby-gotchas-that-will-come-back-to-haunt-you.md"
    kind: repo
---

The page gathers common Ruby pitfalls and recommends habits that avoid confusion and bugs. It focuses on places where Ruby does something different from what many developers expect, especially in control flow, comparison, inheritance, scope, and method visibility.

## Reading notes

- `and / or` do not behave like `&& / ||`; the keyword versions have lower precedence, so the safe practice is to use only `&& / ||`.
- `eql?`, `equal?`, and `===` are different from `==`; the page recommends using `==` unless there is a specific reason to compare differently.
- `super` without parentheses passes the original method arguments to the parent method, while `super()` calls the parent with no arguments.
- Custom exceptions should inherit from `StandardError` or a descendant, and `rescue Exception` should be avoided.
- `class Foo::Bar` does not create the same lexical scope as `module Foo; class Bar`; the longer nested form keeps access to constants from the enclosing module.
- Many `bang!` methods return `nil` when they make no change, so their return value should not be used in conditionals or control flow.
- An assignment method like `attribute=(value)` returns the assigned value, not the explicit return value from inside the method.
- `private` does not make `self.method` private; use `private_class_method` or define the method inside `class << self`.
- The closing note says these issues can look minor at first, but they can create serious headaches during Ruby on Rails development.
