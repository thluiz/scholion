---
title: "My New Favorite Elixir Testing Trick"
date: '2026-11-16T20:10:00+00:00'
category: webclip
summary: 'Author shows how to replace IO-heavy modules with a fake that sends messages to the test process, allowing ExUnit `assert_receive` assertions similar to Ruby test doubles.'
tags: ["elixir", "testing", "test-doubles", "otp"]
has_commentary: false
generated_by: "openai/gpt-5.1"
sources:
  - title: "My New Favorite Elixir Testing Trick"
    url: "https://devonestes.com/my-new-favorite-elixir-testing-trick"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/devonestes-com--elixir-testing-with-fake-printer-and-messages.md"
    kind: repo
---

The author compares their Ruby habit of using test doubles and message assertions (Discovery Testing) with a pattern they found in Elixir tests. While refactoring Benchee, they discovered a technique where a fake printer module mirrors the real printer’s interface but sends messages to the test process instead of writing to IO, allowing ExUnit’s `assert_receive` to verify behavior at the application’s IO boundaries.

## Reading notes

- The author enjoys using test doubles in Ruby to assert that doubles receive messages with correct arguments, following Justin Searls’ Discovery Testing.
- They like how easy Elixir is to test but missed the isolation that test doubles provide in Ruby.
- During a refactor of Benchee, they encountered a test that pipelines a test suite into `benchmark/2` and `measure/2`, then uses `assert_receive` to check that `{:benchmarking, "Something"}` was received.
- This pattern reminded the author of Ruby-style message expectations, prompting curiosity about how it works in Elixir.
- In production, the code passes a `Printer` module to `measure/2`, whose functions print information to the console.
- The tests need to ensure the printer-related code runs without actually printing to the console during the test run.
- The exact console output is outside the scope of that particular test, so capturing IO and applying regular expressions would duplicate test behavior.
- Instead of interacting with real IO, a `Benchee.Test.FakeBenchmarkPrinter` module is defined with the same function interface as the real `Printer`.
- Each function in the fake printer sends a specific message (often including the benchmark or input name) to the current test process using `send self(), ...`.
- Because the fake printer sends messages to the test process, tests can use ExUnit’s built-in `assert_receive` to assert that expected messages were received.
- This approach uses dependency injection by passing the fake printer module into the function under test, enabling isolation from side effects like console IO.
- The author notes they have seen other dependency injection examples in Elixir tests, including a previous post they wrote about similar refactoring for tests.
- This is the first time the author had seen a pattern where a fake module sends messages to the test process to verify behavior.
- They describe this as a particularly appealing technique for testing the edges of an application that interact with the outside world, such as IO.
- The author attributes the idea to Tobias Pfeiffer and explicitly states they are not taking credit for the pattern.
