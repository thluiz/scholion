---
title: "How to write clean functions"
date: '2020-07-05T14:10:39+00:00'
category: webclip
summary: 'The tutorial shows how to refactor a JavaScript function by making it smaller, focusing it on one job, keeping one abstraction level, reducing arguments, and removing side effects.'
tags: ["clean-code", "javascript", "refactoring"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "How to write clean functions"
    url: "https://dev.to/manu4216/how-to-write-clean-functions-bmh"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/dev-to--how-to-write-clean-functions.md"
    kind: repo
---

The tutorial refactors a JavaScript example step by step to make the function easier to read and update. It uses the ideas of small functions, one responsibility, one level of abstraction, fewer arguments, and no side effects.

## Reading notes

- The article is inspired by *Clean Code* by Robert C. Martin.
- It presents a JavaScript function that initially mixes price lookup, error handling, discount logic, rounding, and a mutation on the product object.
- The first refactoring extracts discount handling into a separate function so the main function becomes smaller.
- The next step narrows the main function to the price itself and moves error handling to the caller.
- The article then removes rounding details from the main function by replacing inline arithmetic with a helper.
- It argues that functions are easier to reason about when they take fewer arguments, ideally zero, one, or two.
- To reduce arguments, it turns the discount logic into a fraction and then separates coupon validity from price reduction.
- It identifies the mutation of `product.userCheckedPrice` as a side effect and recommends moving that update outside the price function.
- The final version of `getProductPrice` only gets the price, applies a fraction, and rounds the result.
