---
title: "Elixir and Phoenix: The Future of Web APIs and Apps?"
date: '2020-04-20T21:22:22+00:00'
category: webclip
summary: 'The post reports on a rewrite of an internal app in Elixir and Phoenix, finding strong performance, lower resource use, easy Channels, and promising productivity, while still comparing the stack to Rails.'
tags: ["elixir", "phoenix", "web-frameworks", "performance"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Elixir and Phoenix: The Future of Web APIs and Apps?"
    url: "https://web.archive.org/web/20200226082723id_/https://blog.carbonfive.com/2016/04/19/elixir-and-phoenix-the-future-of-web-apis-and-apps/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/web-archive-org--elixir-and-phoenix-the-future-of-web-apis-and-apps.md"
    kind: repo
---

The post explains why the team tried Elixir and Phoenix, then summarizes what they learned after rewriting an internal project- and people-tracking app. The main theme is productivity across short, medium, and long-term development, along with performance, stability, scalability, and a welcoming community.

## Reading notes

- The team rewrote one in-house web application in Elixir and Phoenix to test productivity, emergent benefits, gotchas, performance, and community.
- Their target for any stack is to ship features quickly and stay productive as products grow more complex.
- Elixir is presented as a functional language that runs on the Erlang VM, and Phoenix as a framework for APIs and web apps with strong concurrency support.
- The application they rewrote tracks projects, people, skills, vacations, rotations, real-time updates, and collaboration.
- The rewrite took 5 to 6 developer-weeks, and the team kept code quality, tests, CDN asset loading, database bootstrapping, and efficient Ecto queries in place.
- The developers said immutable data and functional programming made the code easier to reason about and reduced cognitive load.
- Pattern matching, supervisors, and pipelined data transformations were described as useful parts of writing Elixir.
- The team says Phoenix is productive, but still not as productive as Rails, mainly because of limited experience and a younger ecosystem.
- A large JSON request that took about 1.5 to 2.0 seconds on Rails took about 400 ms on Phoenix with the same hardware, queries, and data.
- Channels were easy to use, replaced Pusher, reduced external service use and operational complexity, and made the app feel much more responsive.
- The Erlang VM reduced resource use from nearly 1 GB across 2 dynos to less than 100 MB on one dyno, while handling about 10 times more concurrency.
- The post says Elixir and Erlang are less fiddly operationally because they use all cores, avoid MRI Ruby’s GIL, and do not have long unpredictable GC pauses.
- The team expects productivity, scalability, maintainability, and stability to keep improving as the community and platform mature.
- They also note that there are fewer Elixir developers, but fewer companies competing for them, and that senior Ruby developers are showing interest in moving to Elixir.
- GitHub, Heroku, and CircleCI worked well, while New Relic did not yet support Elixir/Phoenix and Code Climate was not straightforward out of the box.
