---
title: "A Game in F#? Why, yes indeed."
date: '2025-01-13T23:57:07+00:00'
category: webclip
summary: 'The post explains why the author made Truffle Wizard in F#, focusing on state reasoning, Elmish-style architecture, and why Fable and Feliz fit the game better than Unity or Raylib.'
tags: ["fsharp", "game-development", "elmish", "fable"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "A Game in F#? Why, yes indeed."
    url: "https://tim.knauf.kiwi/blog/posts/2024/truffle-wizard-game-in-fsharp/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2025-01/tim-knauf-kiwi--a-game-in-fsharp-why-yes-indeed.md"
    kind: repo
---

The post says Truffle Wizard was built in F# after the author struggled to reason about state in a Lua-based strategy prototype. F# appealed because it made state transitions easier to follow, reduced boilerplate, and fit a functional style the author found practical for games.

## Reading notes

- Truffle Wizard is a short incremental game written in F#, playable in a browser on desktop or mobile.
- The post is about how the game ended up being written in F# and what it was like to build a game in a functional language.
- The author’s background is mostly in Unity, C#, Objective-C, Flash, ActionScript 3, Lua, and Ruby.
- The motivation came from wanting to reason about state in a systems-heavy strategy game prototype.
- The Lua prototype felt hard to manage because state was hard to track, types needed boilerplate annotations, mutations were easy to introduce, and null checks were common.
- F# for Fun and Profit and railway-oriented programming helped make functional style feel practical and easy to reason about.
- The author wanted immutable-by-default state, rich types, and fewer null checks.
- Unity felt like a poor fit for this approach because it is heavily mutable and object-oriented.
- Raylib felt much better, and the author says F# could drive its loop cleanly.
- Truffle Wizard ultimately used a web stack because its spreadsheet-like UI and scrolling needs fit the web better than Raylib.
- Fable compiles F# to JavaScript, and Feliz provides React support while keeping the code idiomatic in F#.
- The game loop follows an Elmish-style architecture with init, dispatch, update, and render.
- The state is kept in one place, with fields for tick, inventory, unlocks, save log, and view state.
- Saving is simple because the whole state can be serialized and stored in localStorage.
- Messages such as Produce and Tick drive the game, including a timer-based autonomous tick every 250 milliseconds.
- The update function maps messages to state changes in a fairly direct way.
- The render function builds DOM elements with Feliz.
- ChatGPT was used as an F# advisor and helped make the code more concise and idiomatic.
- The author says they did not fully internalize railway-oriented programming, but found F# made prototyping, refactoring, and reasoning about gameplay state much easier.
- The author expects future side projects to use F# again, probably with Raylib, and wonders about a future Fable target for Lua.
