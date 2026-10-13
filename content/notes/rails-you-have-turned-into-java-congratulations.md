---
title: "Rails, You Have Turned into Java. Congratulations!"
date: '2013-02-21T15:28:09-03:00'
category: webclip
summary: 'The post argues that Rails has grown heavier and harder to understand as more frameworks, hosting tools, and customizations get layered on top of it, making upgrades, debugging, and integration increasingly opaque.'
tags: ["rails", "frameworks", "complexity", "heroku"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Rails, You Have Turned into Java. Congratulations! « Discursive"
    url: "http://discursive.com/2013/02/19/rails-you-have-turned-into-java-congratulations/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2013-02/discursive-com--rails-you-have-turned-into-java-congratulations.md"
    kind: repo
---

Rails is described as no longer being the easy framework it once was. The author says that deployment and the number of technologies needed to make useful applications now add complexity, and that Rails has become heavier over time.

## Reading notes

- Rails itself is said to be straightforward, but the frameworks layered on top of it can become burdensome abstractions.
- The post lists tools and services such as RefineryCMS, Devise, Omniauth, Carrierwave, Unicorn, Rack Rewrite, Fog, New Relic, Foreman, AMQP, Honeybadger, and Heroku gems as part of that stack.
- The author describes troubleshooting as opaque, with slow sites, configuration checks, restarts, and fixes whose causes are not clear.
- Refinery is presented as a beast that can lead to too many Engines and a messy file explosion.
- Combining Devise, Refinery, and Omniauth is described as difficult to understand and poorly documented.
- Once Rails and the frameworks built on it are customized, the result is an opaque mess that makes upgrades hard.
- The post says routes become incomprehensible when many Refinery engines are involved.
- The author also points to mega-frameworks maintained with little concern for documentation and to the pattern of a single Rails application running an entire business.
- The closing claim is that Rails has become the new Java, followed by a question about whether Java has learned to be easy.
