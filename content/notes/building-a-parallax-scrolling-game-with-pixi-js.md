---
title: "Building a Parallax Scrolling Game with Pixi.js"
date: '2013-12-02T16:49:19-03:00'
category: webclip
summary: 'The tutorial shows how to set up an HTML5 canvas, load Pixi.js, create a stage and renderer, and use tiling sprites to make far and mid layers scroll at different speeds.'
tags: ["pixi-js", "html5-games", "parallax-scrolling"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Building a Parallax Scrolling Game with Pixi.js | Flippin' Awesome"
    url: "http://flippinawesome.org/2013/11/04/building-a-parallax-scrolling-game-with-pixi-js/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2013-12/flippinawesome-org--building-a-parallax-scrolling-game-with-pixi-js.md"
    kind: repo
---

The article walks through a basic Pixi.js parallax scroller. It starts with an HTML page and canvas, adds the Pixi.js library, initializes a stage and renderer, then loads background textures as sprites.

## Reading notes

- A basic HTML page uses a centered 512 by 384 canvas and loads `pixi.dev.js` from a local project folder.
- The page calls `init()` on body load, and `init()` is used as the main entry point for the scroller.
- Pixi.js is initialized by creating a `PIXI.Stage` and a renderer through `PIXI.autoDetectRenderer()`.
- The stage is rendered to the canvas with `renderer.render(stage)`.
- Display objects are added to the stage with `addChild()`, which controls stacking order.
- The tutorial first uses `PIXI.Sprite` to place a far background layer at the top-left of the stage.
- A mid layer is added below it by positioning it at `y = 128` and adding it after the far layer.
- Parallax motion is introduced with an `update()` loop driven by `requestAnimFrame()`.
- The far and mid layers move at different speeds to create depth.
- `PIXI.TilingSprite` is then used so the background textures wrap seamlessly instead of leaving gaps.
- The scrolling effect is produced by changing `tilePosition.x` instead of moving the sprite itself.
- The conclusion says the next steps are viewport and world positioning, adding a foreground layer, and refactoring away from global variables.
