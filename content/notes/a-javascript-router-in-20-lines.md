---
title: "A Javascript router in 20 lines"
date: '2013-12-19T13:40:45-03:00'
category: webclip
summary: 'The post builds a simple client-side router with hash URLs, route registration, and load/hashchange handling. It then adds one-directional data binding with Object.observe to rerender the view when controller data changes.'
tags: ["javascript", "client-side-routing", "data-binding"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "A Javascript router in 20 lines"
    url: "http://joakimbeng.eu01.aws.af.cm/a-javascript-router-in-20-lines/?utm_source=BrazilJS+Weekly&utm_campaign=3712b36afb-BrazilJS_Weekly_303_22_2013&utm_medium=email&utm_term=0_e6beed4270-3712b36afb-64537241&ct=t%28BrazilJS_Weekly_468_9_2013%29"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2013-12/joakimbeng-eu01-aws-af-cm--a-javascript-router-in-20-lines.md"
    kind: repo
---

The post shows how to build a small client-side router with hash URLs and a view container identified by `view`. Routes are registered in an object, then rendered on `load` and `hashchange` by reading the current hash and swapping in a template.

It then extends the router with one-directional data binding using `Object.observe()`. A route controller can change its data after render, and the router reruns the template so the page updates automatically.

## Reading notes

- The idea comes from earlier posts about writing a template engine in 20 lines.
- The router uses `<script type="text/html">` templates so the browser does not parse them.
- Hash URLs are used instead of the HTML5 History API.
- Route changes are handled with `onhashchange`, and page load is handled with `onload`.
- Routes are stored in a `routes` object through a `route(path, templateId, controller)` function.
- The controller pattern is described as mimicking AngularJS.
- The router looks for a `view` element as the render target.
- The first version renders the selected template into `el.innerHTML`.
- A second version adds `Object.observe()` so controller changes trigger rerendering.
- The data-binding example updates `moreText` after a `setTimeout`.
- The post says the final version is 28 lines without comments and still lacks parameter support.
