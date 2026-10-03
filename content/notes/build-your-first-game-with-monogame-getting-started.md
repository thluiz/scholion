---
title: "Build Your First Game with MonoGame: Getting Started"
date: '2016-03-06T11:54:22-03:00'
category: webclip
summary: 'The post walks through setting up a shared MonoGame project, loading assets, and building a portrait grid UI for MonkeyTap, with sprites, sound, and cell timers.'
tags: ["monogame", "game-development", "xamarin", "ui"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Build Your First Game with MonoGame: Getting Started |"
    url: "https://blog.xamarin.com/build-your-first-game-with-monogame-getting-started/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2016-03/blog-xamarin-com--build-your-first-game-with-monogame-getting-started.md"
    kind: repo
---

The post introduces MonoGame as a cross-platform framework based on XNA and uses MonkeyTap as the example game. It outlines the project setup in Xamarin Studio, explains the main Game1 methods, and shows how content is loaded and drawn.

It then builds the MonkeyTap interface with a shared content pipeline, a GridCell class, viewport-based layout, and a portrait-only grid of monkeys. The post closes by pointing to the next step, where the game logic is added.

## Reading notes

- MonoGame is presented as an easy-to-learn cross-platform gaming framework based on Microsoft’s XNA framework.
- The tutorial uses MonkeyTap, where the player taps monkeys before they run off with bananas.
- The setup requires Xamarin and the latest development build of MonoGame.
- A shared project is created first so the game logic can be reused across target platforms.
- An Android application project is added to the solution, and its `Game1` class can be removed because the shared project holds the game logic.
- The `Game1` class is described as having five main methods: constructor, Initialize, LoadContent, Update, and Draw.
- Constructor and Initialize handle startup work before the game runs.
- LoadContent is used for textures, sounds, shaders, and other game content.
- Update handles game logic and input while the game runs.
- Draw is reserved for rendering graphics.
- Game assets are handled through MonoGame’s content pipeline in `Content.mgcb`.
- The Content directory is moved into the shared project so assets can be shared across platforms.
- The `Content.mgcb` file must use the `MonoGameContentReference` build action.
- The MonkeyTap assets are downloaded and extracted into the shared project’s Content folder.
- The MonoGame Pipeline Editor is used to add the asset files.
- Content is loaded through the `ContentManager` exposed by the Game class.
- The tutorial imports namespaces for collections, audio, touch input, and media.
- Game fields are declared for graphics, sprites, textures, fonts, and sound effects.
- Assets such as monkey, background, logo, font, hit sound, and title music are loaded in LoadContent.
- `MediaPlayer.IsRepeating` is set so the title music loops.
- `SpriteBatch` is used to draw 2D images and text between its Begin and End calls.
- The first drawing step places the monkey texture on the screen.
- The example uses a background color and plays the music loaded earlier.
- A `GridCell` class is added with a display rectangle, color, countdown timer, and transition value.
- `Reset` hides the monkey by restoring the cell to its default state.
- `Update` counts down five seconds for each cell and is used to detect when a monkey was not tapped in time.
- The grid is built as a list of cells rather than placing monkeys randomly.
- Cell rectangles are calculated from the current viewport instead of hardcoded coordinates.
- Padding is derived from 10 percent of the screen width.
- The code loops through row and column coordinates to create the grid.
- The draw loop renders monkeys into each cell.
- The game is set to run only in Portrait orientation.
- The result is a grid full of monkeys, and the post points to a follow-up about adding game logic.
