---
title: "Creating a Lego Mindstorms DSL in F#"
date: '2026-11-16T02:52:39+00:00'
category: webclip
summary: 'The post builds an F# DSL on top of an existing C# Mindstorms API by using custom computation expressions, then maps the DSL actions to commands and shows simple reactive and stateful programs.'
tags: ["fsharp", "lego-mindstorms", "dsl", "computation-expressions"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Creating a Lego Mindstorms DSL in F#"
    url: "https://atlemann.github.io/fsharp/2019/12/11/mindstorms-dsl.html"
    kind: repo
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/atlemann-github-io--creating-a-lego-mindstorms-dsl-in-fsharp.md"
    kind: repo
---

The post shows how to layer an F# DSL over an existing C# Lego Mindstorms API. It defines ports and motor actions, then uses custom computation expressions to let code read like command sentences while still producing a sequence of actions for a Brick command.

## Reading notes

- The author builds on a .NET Lego Mindstorms API by Brian Peek and mentions a fork patched for .NET Core, SDK project files, and observables.
- The DSL is designed to configure actions on a `Command` through an F# computation expression named `mindstorms`.
- Ports are modeled first with separate output and input unions.
- Motor behavior is reduced to a subset of actions such as start, stop, turn at power, turn for time, step, and synchronized stepping.
- A `BrickAction` type wraps an output port list together with one motor action, so a single action can target multiple motors.
- The builder adds custom operations like `Turn`, `TurnForTime`, `Step`, `StepSync`, `Start`, and `Stop`.
- Placeholder keywords such as `With`, `Power`, `Then`, `Steps`, `And`, and `TurnRatio` are introduced so the DSL reads like a sentence.
- The builder accumulates a sequence of actions and returns it from each custom operation.
- An `updateCommand` function translates each `BrickAction` into the corresponding C# `Command` method call.
- `createCommand` folds the actions over a freshly created command, and `invokeCommand` sends it to the brick.
- The post then shows a reactive example where a pressed sensor starts two motors and a released sensor stops them.
- It also shows a recursive async state machine with states that wait for a push button, drive forwards, wait for a light sensor threshold, turn, and loop back.
- A `Run` member can change the computation expression result into a function from `Brick` to `Async<unit>`, which makes the DSL directly runnable.
- The conclusion says the example is intentionally simple but demonstrates how custom computation expressions can make commands look close to plain English.
