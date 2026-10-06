---
title: "Doubts about layers and application's organization"
date: '2015-05-25T09:11:24-03:00'
category: webclip
summary: 'A thread about how to organize Elixir code with Phoenix and Ecto. José Valim and others advise delaying architecture decisions, avoiding premature optimization, and separating database queries into explicit query modules.'
tags: ["elixir", "phoenix", "ecto", "code-organization"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "[elixir-talk:8520] Doubts about layers and application's organization - th.luiz@gmail.com - Gmail"
    url: "https://mail.google.com/mail/u/0/?pli=1#label/Listas%2F05+-+Principais/14d6c234c32cf644"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2015-05/mail-google-com--doubts-about-layers-and-application-organization.md"
    kind: repo
---

The thread asks how to divide layers in an Elixir app with Phoenix and Ecto. Ivan proposes moving logic into model modules and keeping queries in separate repo-like modules, worried that scattered controller queries will hurt maintenance in a large app.

José Valim answers that the application should be built first and organized better only when complexity actually appears. He also says those modules should not be called repos if they only hold queries, suggesting names like `user_query`. Another participant agrees that it is better to leave room for change than to spend too much time planning complexity in advance.

## Reading notes

- Ivan asks how to organize layers in an Elixir app using Phoenix and Ecto, comparing it to Java-style layering.
- He suggests putting user data and related logic in `User` while moving all queries into separate repo modules.
- His concern is that queries scattered through controllers will become hard to maintain in a large application.
- José Valim says to build the application first and rethink organization when real complexity shows up.
- He says it is hard to plan around complexity without actual data from the app.
- He adds that the database abstraction should be called repository only when it handles database operations like update and delete.
- For modules that only hold queries, he suggests a name like `user_query`.
- Onorio Catenacci agrees that planning is useful but says spending too much time on architecture before coding is premature optimization.
- He says flexibility matters because applications change before they are finished.
- Ivan later describes a structure with `Character`, `Character.Query`, and `Character.Builder` modules.
- He says this reduced aliasing, improved readability, encapsulated logic, and allowed optimized queries.
- He finishes by saying he is satisfied with the results in his game project.
