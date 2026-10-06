---
title: "Let’s Build a Simple Video Game with JRuby: A Tutorial"
date: '2012-02-11T08:44:49-03:00'
category: webclip
summary: 'The tutorial shows how JRuby can use Java game libraries to build a simple pong-style game, from installing Slick and LWJGL to moving a paddle, bouncing a ball, and resetting play.'
tags: ["jruby", "slick", "lwjgl", "game-development"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Let’s Build a Simple Video Game with JRuby: A Tutorial"
    url: "http://www.rubyinside.com/video-game-ruby-tutorial-5726.html"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2012-02/rubyinside-com--let-s-build-a-simple-video-game-with-jruby-a-tutorial.md"
    kind: repo
---

The article argues that JRuby lets Ruby use Java game libraries in a practical way, making it possible to build a simple game despite Ruby’s weaker game-development ecosystem. It introduces Slick and LWJGL, then walks through setup, a basic window, graphics, input handling, and a small bat-and-ball game.

## Reading notes

- JRuby is presented as a way to use Java libraries on the JVM from Ruby.
- Slick is described as a thin layer over LWJGL.
- LWJGL provides graphics, audio, controller input, and OpenCL.
- The setup uses RVM, Slick, and native libraries placed in the game directory.
- A basic JRuby game subclasses Slick’s `BasicGame` and defines `render`, `init`, and `update`.
- `render` draws the window contents, `init` loads resources, and `update` handles input and game changes.
- The sample game loads a background image, a ball image, and a paddle image.
- The paddle moves with the left and right arrow keys, using `delta` to scale movement.
- The ball moves with sine and cosine based on an angle value.
- Wall collisions change the ball angle.
- If the ball falls below the screen, the game resets the paddle, ball position, and angle.
- Paddle collision also changes the ball angle.
- The article says separate classes for paddle and ball would make the code cleaner.
- It mentions Slick’s `StateBasedGame` for games with menus, levels, and other states.
- It also mentions Warbler for packaging a Ruby app into a `.jar` file.
- Ludum Dare is cited as the motivation for exploring JRuby game development.
