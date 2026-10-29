---
title: "When to choose Elixir over Ruby for 2016 projects?"
date: '2016-01-09T18:06:09-03:00'
category: webclip
summary: 'The article says Rails still fits internal apps, prototypes, smaller user bases, cacheable sites, and systems that can be split up. Elixir is better for high traffic, async, distributed, real-time, always-on, and large systems.'
tags: ["elixir", "ruby-on-rails", "web-development", "scalability"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "When to choose Elixir over Ruby for 2016 projects?"
    url: "https://www.amberbit.com/blog/2015/12/22/when-choose-elixir-over-ruby-for-2016-projects/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2016-01/amberbit-com--when-to-choose-elixir-over-ruby-for-2016-projects.md"
    kind: repo
---

The article contrasts Ruby on Rails with Elixir by matching each stack to the kind of system it suits best. Rails is presented as enough for internal tools, quick prototypes, limited audiences, splitable systems, and pages that can rely on caching. Elixir is recommended when the system must handle heavy traffic, async work, distributed nodes, zero downtime, real-time messaging, or a large codebase.

## Reading notes

- Rails still fits internal apps with forms, user input, validations, authentication, and limited budgets.
- Rails can be useful for prototypes because scaffolding, dashboards, permissions, and authentication plugins speed up early delivery.
- Rails is a reasonable choice when the target user base is small and scaling pressure is low.
- Rails can work when the system can be split into smaller subsystems or multiple instances with dedicated databases.
- Rails can also fit systems that can cache most pages, such as blogs and news sites.
- Elixir is presented as a better fit for high-traffic systems because it handles more requests on the same hardware and uses modern multicore resources better.
- Elixir is recommended for async systems that need worker pools, supervision, and easier communication with external services.
- Elixir suits distributed and clustered systems because Erlang and Elixir use message passing instead of shared state.
- Elixir is recommended for high-availability systems that need zero downtime and code hot-swapping.
- Phoenix is described as strong for server-side push and real-time applications, with scalable websocket channels.
- Elixir is a good choice for large applications because umbrella projects and loose coupling help split and maintain the codebase.
- The article also says the stack can be used to filter for experienced developers, since fewer Elixir developers are available and many are switching from Ruby.
