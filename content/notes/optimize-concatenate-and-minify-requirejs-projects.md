---
title: "Optimize (Concatenate and Minify) RequireJS Projects"
date: '2016-03-03T13:30:18-03:00'
category: webclip
summary: 'The article shows how to use the RequireJS Optimizer with a build profile to concatenate and minify a TodoMVC Backbone.js app, reducing requests and file size while keeping the app behavior the same.'
tags: ["requirejs", "javascript-optimization", "nodejs", "amd"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Optimize (Concatenate and Minify) RequireJS Projects - WebDevEasy"
    url: "http://www.webdeveasy.com/optimize-requirejs-projects/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2016-03/webdeveasy-com--optimize-concatenate-and-minify-requirejs-projects.md"
    kind: repo
---

The page explains why RequireJS projects are optimized in production: many small module files increase requests, while concatenation and minification reduce load time and file size. It then walks through optimizing a TodoMVC Backbone.js + RequireJS application with r.js from Node.js, using a build profile that defines app paths, modules, shims, and CSS optimization.

It also notes a limitation of the optimized output: the app still needs code that implements define() and require(), which creates overhead. As a workaround, the article points to almond as a minimal AMD loader that can replace RequireJS implementation in optimized builds.

## Reading notes

- RequireJS lets JavaScript code be split into modules that are loaded through dependencies.
- In production, keeping many separate JavaScript files is described as a bad practice because each request adds time.
- Minification reduces file size by changing code without changing behavior, such as removing spaces and mangling names.
- The article uses Addy Osmani’s TodoMVC Backbone.js + RequireJS project as the example.
- The example project’s HTML loads RequireJS with one script tag, and RequireJS loads the rest of the JavaScript files.
- The optimizer used is r.js, which includes the RequireJS Optimizer.
- The article shows using a build profile file instead of command-line arguments.
- The sample build file sets appDir, baseUrl, dir, modules, fileExclusionRegExp, optimizeCss, removeCombined, paths, and shim.
- appDir is the application directory, baseUrl is the anchor path for finding files, and dir is the output directory.
- modules lists the module or modules to optimize.
- fileExclusionRegExp excludes r.js and build.js from the output.
- optimizeCss controls CSS optimization.
- removeCombined removes concatenated files from the output directory.
- paths maps module names to relative locations.
- shim defines dependencies and exports for scripts that do not call define().
- Running the optimizer creates a dist folder.
- In the optimized version, main.js contains combined and minified dependencies, and base.css is also optimized.
- The optimized app keeps the same behavior as the unoptimized one.
- The article reports a reduction from 13 server script requests to 2, and from 164KB to 58.6KB.
- Even after optimization, the app still needs define() and require() to work.
- The article says this dependency is overhead because it is not part of the application itself.
- Almond is presented as a minimal AMD loader that can ease this overhead.
- The page ends by linking to unoptimized and optimized downloads and live demos.
