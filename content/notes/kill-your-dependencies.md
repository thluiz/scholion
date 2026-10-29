---
title: "Kill Your Dependencies"
date: '2016-02-12T10:51:24-03:00'
category: webclip
summary: 'The post argues that dependencies bloat apps, add bugs, and waste memory, so developers should remove unnecessary gems, prefer stdlib or simpler options, and keep runtime dependencies minimal.'
tags: ["dependencies", "ruby", "gems", "rails"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Kill Your Dependencies"
    url: "http://www.mikeperham.com/2016/02/09/kill-your-dependencies/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2016-02/mikeperham-com--kill-your-dependencies.md"
    kind: repo
---

The post argues that dependency sprawl hurts Ruby apps and, by extension, other language ecosystems too. It points to large Gemfiles, test gems loaded in production, and high memory use as common signs that too many dependencies are being pulled in transitively.

## Reading notes

- Rubygems makes reuse easy, but that same ease allows gems to pull in many other gems transitively.
- A dependency in a published gem becomes a dependency for every app that uses that gem, multiplying the impact of bugs.
- The `mime-types` example shows how a deeply nested dependency can waste memory in every Rails app.
- App developers should first ask whether they need a dependency at all, and whether they can implement only the minimal needed functionality themselves.
- If a gem is needed, check for native extensions and for how many other gems it pulls in transitively.
- Gems with native extensions can destabilize systems and cause bugs or crashes.
- Test gems should be loaded only when needed, using Bundler groups.
- Library authors should minimize their own dependencies and consider memory use, require time, and monkeypatching effects.
- The post says Sidekiq keeps only three runtime dependencies: `concurrent-ruby`, `connection_pool`, and `redis`.
- JSON dependencies should be removed because JSON is already in Ruby’s stdlib; `require 'json'` is enough.
- Rubygems should use `Net::HTTP` internally instead of depending on multiple HTTP client libraries.
- Optional alternatives should default to stdlib or simpler libraries when possible.
- Rails 5.0 work reduced dependency counts by removing several gems.
- The post closes by urging both gem authors and app developers to audit and remove unnecessary dependencies.
