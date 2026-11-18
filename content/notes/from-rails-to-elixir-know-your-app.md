---
title: "From Rails to Elixir: Know Your App"
date: '2020-04-10T16:58:25+00:00'
category: webclip
summary: 'The author explains how a price tracker built in Rails was easy to ship but costly to run, then argues for understanding workload patterns, concurrency, and memory use before choosing Elixir for a rewrite.'
tags: ["rails", "elixir", "concurrency", "migration"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "From Rails to Elixir: Know Your App"
    url: "https://dev.to/jdcosta/from-rails-to-elixir-know-your-app-131m"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/dev-to--from-rails-to-elixir-know-your-app.md"
    kind: repo
---

The article describes a price tracker app built quickly with Rails, PostgreSQL, Redis, and Sidekiq, then hit deployment and hosting costs that made the setup feel too heavy for a side project. The author uses that experience to argue that system design should start with understanding the app’s workload, resource use, and separable concerns.

## Reading notes

- The app was a price tracker that let users save items, scrape product pages, and receive email alerts when prices changed.
- The initial stack was Rails, PostgreSQL, Redis, and Sidekiq, chosen because it let the author prototype quickly.
- Deployment on a single small server failed when the machine ran out of memory during asset compilation and process startup.
- A larger virtual machine fixed the immediate problem, but the monthly bill was too high for a low-effort side project.
- The author says the system was mostly I/O bound and could be split into four concerns: web server, page downloader, page parser, and notifications.
- Each of those concerns could run independently, so the workload was suited to concurrent execution.
- The author values monitoring and understanding hot paths before trying to optimize a system.
- Elixir and Go were considered because of concurrency, but Elixir felt like the better fit.
- Elixir’s appeal came from BEAM, the actor model, Phoenix, ecosystem tools, umbrella projects, and the expectation of lower memory use.
- The rewrite also felt appealing because it was enjoyable to learn and explore.
- The author notes that companies should weigh migration costs, developer availability, risk, and short-term disruption before replacing a mature stack.
- The series will continue with more technical posts about the migration process and how to switch platforms safely.
