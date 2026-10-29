---
title: "Prevent information leaking in Rails"
date: '2016-01-02T14:08:45-03:00'
category: webclip
summary: 'Rails sets a browser cache policy that still leaves pages on disk. The post says this can expose sensitive content after logout and suggests overriding Cache-Control for authenticated pages.'
tags: ["rails", "caching", "information-leaking"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Greg Molnar | Prevent information leaking in Rails"
    url: "https://greg.molnar.io/tech/2015/10/28/prevent-rails-information-leaking.html"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2016-01/greg-molnar-io--prevent-information-leaking-in-rails.md"
    kind: repo
---

Rails’ default Cache-Control header makes the browser revalidate pages, but it still stores a cached copy. That can expose sensitive information if someone uses the back button after a logout or if an attacker can read browser cache files.

## Reading notes

- By default, Rails sends `Cache-Control: max-age=0, private, must-revalidate`, which revalidates pages but still caches them.
- The back button may load a page from cache without revalidation.
- This can leak sensitive information after logout on a shared computer.
- The post suggests setting `Cache-Control` explicitly with a before filter.
- The suggested value is `no-cache, no-store`.
- The filter should be used in controllers that show sensitive information, usually those behind authentication.
- Another option is to ask users at sign in whether they are on a public or private computer and choose the cache header accordingly.
