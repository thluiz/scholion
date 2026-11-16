---
title: "Getting started with Scenic in Elixir — Crafting a simple snake game"
date: '2026-11-16T08:21:11+00:00'
category: webclip
summary: 'The tutorial shows how to build a simple Snake game with Scenic in Elixir, covering setup, scene rendering, frame updates, keyboard input, pellet eating, scoring, and game over handling.'
tags: ["elixir", "scenic", "snake-game", "gui"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Getting started with Scenic in Elixir — Crafting a simple snake game"
    url: "https://web.archive.org/web/20190328163157id_/https://blog.usejournal.com/elixir-scenic-snake-game-b8616b1d7ee0"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/web-archive-org--getting-started-with-scenic-in-elixir-crafting-a-simple-snak.md"
    kind: repo
---

The tutorial explains how to use Scenic with Elixir to build a playable Snake game. It starts with setup, then shows how to create a scene, draw the score, render the snake and pellet, update the screen on a timer, handle arrow-key input, and switch to a game over scene on collision.

## Reading notes

- Scenic is presented as a functional UI framework for Elixir that can render native interfaces without web pages.
- The tutorial assumes an Elixir installation, Scenic system dependencies, and the scenic_new package.
- The game starts from a scene defined in config, and the initial example switches the default scene to Game.
- A scene keeps game state during its lifetime, including the score and later the snake body, size, direction, and food position.
- The snake is drawn from tiles on a grid, with a helper function used to paint rounded rectangles at coordinates.
- A timer sends a :frame message every few milliseconds so the scene can update continuously.
- The movement logic creates a new head from the current head and direction, then trims the body to the current size.
- Keyboard events are handled with handle_input/3, using pattern matching for arrow keys to change direction.
- The pellet is represented as a simple tuple with its grid position and is redrawn with the same tile helper.
- Eating is detected when the snake head overlaps the pellet position; the pellet is randomized, the score increases, and the snake grows.
- Pellet randomization repeats until the new position does not overlap the snake body.
- Self-collision is detected by comparing the snake body with Enum.uniq/1 and checking whether duplicates remain.
- When the snake collides with itself, the scene switches to a Game Over scene, carrying over the score.
- The game over scene uses an on-cooldown flag so the player cannot leave immediately after the transition.
- The author notes that more complex games may benefit from separating game logic from the scene module.
