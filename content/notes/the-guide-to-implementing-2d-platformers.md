---
title: "The guide to implementing 2D platformers"
date: '2014-06-19T09:31:20-03:00'
category: webclip
summary: 'The page classifies four main ways to implement 2D platformers and compares their collision rules, strengths, and tradeoffs, then reviews acceleration, jump control, animation timing, and smoother movement.'
tags: ["2d-platformers", "collision", "game-physics", "movement"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "The guide to implementing 2D platformers | Higher-Order Fun"
    url: "http://higherorderfun.com/blog/2012/05/20/the-guide-to-implementing-2d-platformers/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2014-06/higherorderfun-com--the-guide-to-implementing-2d-platformers.md"
    kind: repo
---

The page organizes 2D platformer implementation into four broad systems, from pure tile movement to vector-based collision. It also points out how each approach handles slopes, one-way platforms, ladders, stairs, moving platforms, and the kinds of games each method fits best.

It then covers general movement concerns that shape how a platformer feels, including acceleration, jump behavior, animation timing, and ways to keep motion smooth without making collision unstable.

## Reading notes

- The author aims to categorize different ways to implement 2D platform games, compare strengths and weaknesses, and collect implementation details.
- The first approach is pure tile-based movement, where the player always occupies tiles and movement is limited to tile steps.
- Pure tile movement is simple and precise, but it strongly restricts control and is better suited to puzzle or cinematic platformers.
- In the pure tile model, movement is handled by copying the character to a target tile position, checking collisions, and only moving if the path is clear.
- The second approach keeps collision tile-based but lets characters move freely with pixel-level resolution.
- Tile-based smooth movement is presented as the most common classic platformer approach and as a strong default for action games.
- In that model, the character uses an axis-aligned bounding box, often smaller than the visible sprite.
- Movement is resolved one axis at a time by scanning tiles in the direction of travel and limiting displacement by the nearest obstacle.
- Slopes in the smooth tile system require special handling, including floor interpolation and careful collision rules on both horizontal and vertical movement.
- One-way platforms only block the player when the player was already above them before movement.
- Ladders are treated as a separate state that replaces most normal collision rules.
- Stairs behave like ladders in some games, while in others they are only a visual feature that uses slope-like motion.
- Moving platforms are handled as normal obstacles plus an extra step that carries characters along by the platform’s own movement delta.
- The third approach uses a bitmask, effectively treating each pixel as a collision unit.
- Bitmask collision allows finer terrain detail and destructible environments, but it increases complexity and memory use.
- Slopes are a major difficulty for bitmask systems, and the page presents them as a reason this method is hard to get right.
- The bitmask example described uses per-axis stepping, a small upward offset for horizontal climbing, and rollback if movement ends in overlap.
- The fourth approach uses vector data such as lines or polygons for collision boundaries.
- Vectorial collision can be handled manually or through a physics engine such as Box2D.
- The page warns that physics-based platformers can easily feel generic if the physics are not shaped carefully.
- Compound character bodies can use separate polygons or sensors for feet, sides, and head to detect standing, wall contact, and jump readiness.
- Acceleration is presented as one of the biggest factors in how a platformer feels.
- Low acceleration creates slippery motion, while high acceleration creates twitchier and more immediate control.
- The page describes weighted averaging and additive acceleration as two ways to implement speed changes.
- Jump control can preserve momentum, allow air control, let the player control jump height by holding the button, or support multiple jumps.
- Animations should not delay responsive actions in action-oriented platformers; they should stay cosmetic when responsiveness matters.
- Several methods are given for smoother movement while still keeping collision stable, including floats, fixed point numbers, and an integer position with fractional remainder.
