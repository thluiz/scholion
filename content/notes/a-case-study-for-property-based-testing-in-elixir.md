---
title: "A case study for property based testing in Elixir"
date: '2026-11-16T02:02:51+00:00'
category: webclip
summary: 'The author explains property based testing through a simple addition example, then applies it to a poll percentage function where rounding can break the total, and shows how a preconditioned assertion catches the bug.'
tags: ["property-based-testing", "elixir", "stream-data", "testing"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "A case study for property based testing in Elixir"
    url: "https://dev.to/youroff/a-case-study-for-property-based-testing-in-elixir-44c6"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/dev-to--a-case-study-for-property-based-testing-in-elixir.md"
    kind: repo
---

The post introduces property based testing as a stochastic way to check that a condition holds across many generated inputs. It first shows how a simple addition property fails when negative integers are included, then fixes the test by filtering the input stream and adding guards to the function.

## Reading notes

- Property based testing checks a property against many generated examples, but the author notes that it can be impractical in web development because repeated runs may add too much overhead.
- A simple `add(a, b)` example is used to show a property that should hold for positive integers: the result should be greater than or equal to each operand.
- The initial property test fails because the generator produces negative integers.
- The fix is to add a guard to `add/2` and filter the integer generator so it only yields nonnegative values.
- The author then turns to a real case from a poll feature in a social app, where vote counts are converted into percentages.
- The problem is rounding: percentage values can overflow or underflow when the results are summed.
- The original implementation uses an accumulator initialized to 100 and adjusts the last option with the remaining percent.
- The property test for this function checks that the total of the percentages is 100 when there are votes, or 0 when there are no votes.
- The author says an earlier naive assertion, `total_percents == 100 || total_percents == 0`, would have allowed a buggy zero-vote poll to show 100 percent on the last option.
- The final point is that the quality of the test depends on the logic of the assertion itself.
