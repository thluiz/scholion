---
title: "2014’s JavaScript versus today’s (or: How my old code holds up today)"
date: '2016-05-30T08:14:14-03:00'
category: webclip
summary: 'The author compares his 2014 JavaScript with his current practice and says his code has become cleaner through better structure, clearer functions, JSON-based data handling, templating, and heavier use of libraries.'
tags: ["javascript", "code-style", "web-development", "d3"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "2014’s JavaScript versus today’s (or: How my old code holds up today)"
    url: "http://ejb.github.io/2016/05/09/how-my-code-has-changed-since-2014.html"
    kind: repo
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2016-05/ejb-github-io--2014s-javascript-versus-today-s.md"
    kind: repo
---

The piece contrasts the author’s early-2014 JavaScript with the way he writes code now. He says two years of work on client-side newsroom projects made his code cleaner and clearer, and he ties that change to better structure, narrower functions, more disciplined data loading and processing, and less string concatenation when rendering HTML.

## Reading notes

- He moved from one large function with globals to an `App` object and separate constructor objects for larger features such as charts.
- He now aims for functions with a single purpose, uses pure functions and closures more often, and passes objects instead of long argument lists.
- He prefers JSON files for data, uses `jQuery.when` with multiple `getJSON` calls, and sometimes converts CSV to JSON with Node scripts.
- For data processing, he now uses array methods like `forEach`, `filter`, and `map` instead of large `for` loops and repeated `if` statements.
- He has shifted from building HTML by concatenating strings to using Mustache templates earlier in a project.
- He uses more libraries than before, valuing time savings and fewer bugs over minimizing page weight, and treats Moment.js and Mustache as essentials.
- His charting practice now combines HTML and CSS for simple bars, Highcharts for simple charts, and D3 for more complex designs.
- For maps, he moved from CartoDB to Leaflet as his default interactive-map library, and notes that many maps can be shown non-interactively with ai2html.
- He credits colleagues, books, sites, and newsletters for many of the practices he describes.
