---
title: "Refactoring a Function in Elixir"
date: '2026-11-16T03:09:54+00:00'
category: webclip
summary: 'The post refactors a quiz game''s `answer_question` function by reducing abstraction layers, naming concepts with functions, and moving decisions into function heads to make the code clearer and more composable.'
tags: ["elixir", "refactoring", "functional-programming"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Refactoring a Function in Elixir - DockYard"
    url: "https://dockyard.com/blog/2020/04/01/refactoring-a-function-in-elixir"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/dockyard-com--refactoring-a-function-in-elixir.md"
    kind: repo
---

The post revisits a quiz game's `answer_question` function and refactors it to follow core programming principles from *Designing Elixir Systems with OTP*. The goal is to make the function easier to understand by reducing abstraction layers and by breaking out small, focused pieces of behavior.

## Reading notes

- The original `answer_question` mixed guess checking, game updates, and datatype-level updates in one function.
- The first refactor pulls `Map.put(:current_question, get_random_question())` into a `select_question` function.
- `select_question` names the game-level idea of selecting a question and is shaped to fit the pipeline.
- A new `Response` module wraps the correctness check for a guess and stores `correct` in a struct.
- The function is then rewritten to use `Response.new(game, guess, user_name)` and branch on `response.correct`.
- The final refactor replaces the `case` with multiple `answer_question` clauses that pattern match on `%Response{correct: true}` and `%Response{correct: false}`.
- The author says these changes make the function's intention clearer, and the code more testable and maintainable over time.
