---
title: "Keeping your Ruby on Rails app easy to update"
date: '2016-05-13T09:03:34-03:00'
category: webclip
summary: 'The post argues that updating Rails helps with security, bug fixes, and features, and says upgrade work stays smaller when dependencies are kept selective, monkey patches are avoided, and tests stay strong.'
tags: ["ruby-on-rails", "upgrades", "testing", "dependencies"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Keeping your Ruby on Rails app easy to update"
    url: "http://blog.plataformatec.com.br/2016/05/keeping-your-ruby-on-rails-app-easy-to-update/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2016-05/blog-plataformatec-com-br--keeping-your-ruby-on-rails-app-easy-to-update.md"
    kind: repo
---

Keeping a Rails app easy to update depends on making upgrades less disruptive from the start. The post says teams should justify updates by pointing to security, bug fixes, and new features, then reduce future work by limiting dependencies, avoiding monkey patches, and keeping test coverage strong.

## Reading notes

- Rails updates matter because supported versions receive security fixes, older versions miss bug fixes and performance improvements, and newer releases can improve developer productivity.
- Using too many gems increases coupling and can make a Rails upgrade harder, especially when a gem depends closely on the framework.
- Before adding a gem, the post asks whether it brings enough value and whether it is actively maintained, documented, and well supported by maintainers.
- Monkey patches can create hidden bugs during upgrades because they change code you do not own and can break when a gem changes its internals or public methods.
- If behavior is specific to the app, the post suggests extending the gem with normal OO patterns such as adapters, subclasses, or composition, and also mentions Ruby Refinements.
- If a monkey patch is still necessary, it should be organized and documented, with clear reasons for its existence, when it can be removed, and how to remove it.
- Good test coverage helps catch upgrade problems before deployment, even though 100% coverage does not guarantee that the right behavior is tested.
- When coverage is low, the post recommends adding tests first to the most used and most important features so the suite can give fast feedback during future changes.
