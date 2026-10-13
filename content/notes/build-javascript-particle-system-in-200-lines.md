---
title: "Build a JavaScript Particle System in 200 Lines"
date: '2014-10-03T17:21:29-03:00'
category: webclip
summary: 'The article shows how to build a flexible particle system with vanilla JavaScript, using a canvas, an animation loop, vectors, emitters, particles, and fields that attract or repel.'
tags: ["javascript", "canvas", "particle-system", "animation-loop"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "HTML5 Hub | Build a JavaScript Particle System in 200 Lines"
    url: "http://html5hub.com/build-a-javascript-particle-system/?utm_source=javascriptweekly&utm_medium=email"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2014-10/html5hub-com--build-javascript-particle-system-in-200-lines.md"
    kind: repo
---

The page explains how to build a flexible particle system in under 200 lines of vanilla JavaScript. It starts from a full-window canvas, then sets up an animation loop that separates update and draw work with requestAnimationFrame.

## Reading notes

- The project began as a personal demo and later became a Chrome Experiment, and the author says it helped them learn JavaScript performance.
- The article treats graphic development as accessible if you have a text editor and a browser.
- The canvas setup uses a full-window canvas and a black background.
- The animation loop clears the canvas, updates state, and queues the next frame with requestAnimationFrame.
- A particle is modeled as position, velocity, and acceleration, each stored as a 2D vector.
- The Vector object includes methods for adding vectors, getting magnitude, getting angle, and creating a vector from angle and magnitude.
- A Particle updates by adding acceleration to velocity and then velocity to position.
- An Emitter stores position, velocity, spread, and draw color, and emits particles with randomized angle across the spread.
- The system keeps particles and emitters in arrays, creates new particles up to a maximum, and removes particles that go out of bounds.
- The draw step renders particles as squares and can also draw fields and emitters as circles.
- A Field has a position and a mass that can be positive for attraction or negative for repulsion.
- Particle acceleration can be adjusted by fields using the distance between the particle and each field.
- The article ends with demos and suggests trying different emitter and field combinations, including turning the mouse into a field or emitter.
