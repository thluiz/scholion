---
title: "Image processing with comonads and phantom types"
date: '2016-04-04T12:45:55-03:00'
category: webclip
summary: 'The page shows how a 2D image comonad can express neighborhood-based filters, then uses phantom types to prevent expensive compositions and keep array-based performance.'
tags: ["comonads", "phantom-types", "image-processing", "f-sharp"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Image processing with comonads and phantom types"
    url: "http://hodzanassredin.github.io/2016/03/28/image_processing_with_comonads.html"
    kind: repo
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2016-04/hodzanassredin-github-io--image-processing-with-comonads-and-phantom-types.md"
    kind: repo
---

The page introduces comonads as the dual of monads, then uses a 2D array with indexes to model grayscale images and neighborhood filters. It shows that plain array-based composition can become slow, and that phantom types can separate raw and composed values at compile time.

## Reading notes

- A comonad is presented as the dual of a monad, with `extract` and `extend` as the corresponding operations.
- The text motivates comonads by cases where functions need extra context, like a runtime context or neighboring cells in an image.
- A grayscale image is represented as a 2D array of ints with indexes.
- The array wrapper defines `get`, `extract`, and `extend`, where `extend` behaves like a mapped neighborhood computation over the whole array.
- Filters such as `laplace2d` and `gauss2D` use values from the current cell and adjacent cells.
- Filter composition is built by applying `extend` to existing filters and combining intermediate results.
- The first array-based version can become slow because some compositions lead to O(N^2) behavior.
- A lazy array version avoids the complexity blowup, but the text says it duplicates underlying filter calls and is still not ideal.
- Phantom types are introduced as extra type parameters used only for compile-time checks.
- The final design marks raw arrays and composed arrays differently, so `extend` accepts only raw inputs and returns composed outputs.
- This type separation makes incorrect compositions fail at compile time.
- The final example rewrites `contours` and `gaussLaplace` so they typecheck under the phantom-type rules.
- The page reports runtime comparisons for the contour filter, with the final version faster than both the original and lazy versions.
