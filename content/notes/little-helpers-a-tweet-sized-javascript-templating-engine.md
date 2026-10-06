---
title: "Little helpers: a tweet-sized JavaScript templating engine"
date: '2015-04-25T22:17:40-03:00'
category: webclip
summary: 'The post argues that for small, short-lived apps and messages, a tiny homemade JavaScript templating helper can be enough, and shows a tweet-sized function that replaces {placeholders}.'
tags: ["javascript", "templating", "single-page-apps"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "mir.aculo.us JavaScript with Thomas Fuchs » Blog Archive » Little helpers: a tweet-sized JavaScript templating engine"
    url: "http://mir.aculo.us/2011/03/09/little-helpers-a-tweet-sized-javascript-templating-engine/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2015-04/mir-aculo-us--little-helpers-a-tweet-sized-javascript-templating-engine.md"
    kind: repo
---

The post argues that JavaScript libraries do not need to be large to be useful, especially for single-page apps, short-lived event sites, visualizers, and small helper code. In that context, the author prefers a very simple templating function over searching for existing engines.

## Reading notes

- JavaScript libraries can be useful without being big or clunky.
- For single-page apps, short-lived event sites, and visualizers, small helper code is often faster to write than searching for a prebuilt solution.
- The example is a minimal templating function designed to fit into a tweet.
- The function loops through the data object and replaces each `{key}` occurrence in the template string with the corresponding value.
- It works for simple messages such as "Hello {who}!" and "Hello {who}! It's {time} ms since epoch."
- For larger templates, the author would likely use an engine that stores HTML templates in `<script>` tags.
- The post adds that `replace` can execute functions automatically, which halves the code size.
