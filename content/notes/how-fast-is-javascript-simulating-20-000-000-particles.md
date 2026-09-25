---
title: "how fast is javascript? Simulating 20,000,000 particles"
date: '2026-09-25T08:01:04+01:00'
category: webclip
summary: 'The text shows, step by step, how the JavaScript simulation improves by using TypedArrays, SharedArrayBuffers, web workers, double buffering, and a final shader to reach 20 million particles.'
tags: ["javascript","sharedarraybuffer","web-workers","particle-simulation"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "how fast is javascript? Simulating 20,000,000 particles"
    url: "https://dgerrells.com/blog/how-fast-is-javascript-simulating-20-000-000-particles?ref=dailydev"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/dgerrells-com--how-fast-is-javascript-simulating-20-000-000-particles.md"
    kind: repo
---

The page follows a particle simulation in JavaScript from a simple single-threaded approach to a version that uses TypedArrays, SharedArrayBuffers, web workers, double buffering, and finally a GPU-based render path. The main constraint is to keep the simulation in JS and on the CPU as much as possible, while reducing cache misses and data-transfer costs.

The later versions change the bottleneck from rendering on the main thread to memory access and buffer accumulation. In the final comparison, the simulation stays on the CPU but rendering uses a full-screen quad with a texture based on particle counts, which lets the project reach 20,000,000 particles on an M1 Mac and scale better with more CPU cores.

## Reading notes

- The initial goal is to simulate 1,000,000 particles in pure JavaScript, at 60 fps, on a cell phone and using only the CPU.
- The text rejects the GPU-based solution and also avoids WebAssembly, to keep the work in JavaScript.
- The first idea uses an array of objects, but the author begins to prefer contiguous and compact data in memory.
- TypedArrays enter as an alternative to store particle data in a flat and contiguous buffer.
- The first design divides the work among several web workers with SharedArrayBuffer and shared signaling.
- Each particle now has x, y, dx, and dy, stored as 32-bit floating-point numbers.
- The initial rendering uses ImageData on the canvas, with each particle occupying one pixel.
- The author observes that most of the time goes into drawing the particles on the main thread, and not into the simulation in the workers.
- The second version adds mouse and touch input to the simulation buffer to pull the particles toward the touched point.
- The force used in the interaction is based on an approximation of gravity with distance squared in the denominator, but adjusted to produce a more interesting effect.
- The third version moves rendering to the workers, but this creates flickering because the workers clear buffers while the main thread reads the same data.
- The fourth version fixes the flickering by making the main thread wait for the workers to finish before rendering.
- The fifth version uses double buffering to allow the workers to prepare one buffer while the main thread draws the other.
- The text explains that pixel access becomes slow because the reading pattern is not very contiguous and causes cache misses.
- The author concludes that the amount of data exceeds what fits in cache, which limits the performance gain.
- In the sixth version, each particle also stores its initial position, and the simulation starts pulling it back to that point, producing a fluid or jelly effect.
- In the seventh version, the pixel buffer is replaced by a grid with the count of particles per pixel, reducing memory and pressure on the cache.
- The text compares the performance of Apple and Ryzen chips and relates the difference to the size of the L1 cache.
- In the final comparison, the author shows that instancing in three.js still suffers from the cost of sending simulation data to the GPU every frame.
- The final solution uses the count grid as a texture and draws a full-screen quad with a shader, keeping the data sent to the GPU fixed at the resolution size.
- The final result reaches 20 million particles on an M1 Mac at around 20 fps, with better scaling on CPUs with more cores.
