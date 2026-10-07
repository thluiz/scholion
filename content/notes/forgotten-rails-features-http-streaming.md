---
title: "Forgotten Rails features: HTTP Streaming"
date: '2012-05-30T23:57:52-03:00'
category: webclip
summary: 'The post explains how Rails HTTP streaming sends the response in chunks, can make pages feel faster, and requires changes to render calls, templates, and server setup.'
tags: ["rails", "http-streaming", "unicorn", "performance"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Forgotten Rails features: HTTP Streaming"
    url: "http://robotmay.com/post/24054884390/forgotten-rails-features-http-streaming"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2012-05/robotmay-com--forgotten-rails-features-http-streaming.md"
    kind: repo
---

HTTP streaming in Rails sends the response in chunks, with the layout head sent before the rest of the page. The post says this does not reduce generation time, but it can make pages appear to load faster by letting the browser request assets sooner.

## Reading notes

- HTTP streaming was added in Rails 3.1 and is described as a niche feature.
- The old `stream` method is gone; the post shows `stream: true` passed to `render` or `respond_with`.
- Using delayed query execution, such as `Project.scoped` instead of `Project.all`, can make the header return faster.
- NewRelic browser monitoring can block the response unless `auto_instrument` is set to false.
- Action caching should not be used with streaming because it can cache chunk byte counts on the page.
- HAML does not work with HTTP streaming in the version mentioned, while Slim and ERB do.
- `content_for` will not work because the layout is sent before the view; `provide` is the suggested alternative.
- The post recommends putting JavaScript include tags in the `head` so the browser can load them while chunks arrive.
- The author uses Unicorn for streaming and includes a sample Unicorn config for Heroku.
- The feature is used on the homepage and search results page for Days Out Near Me because those pages benefit most from faster perceived loading.
