---
title: "Homemade analytics with Ecto and Elixir"
date: '2020-08-26T19:31:19+00:00'
category: webclip
summary: 'The post shows how Dashbit built its own analytics to avoid cookies, first with Ecto upserts and then with Elixir processes and Registry to batch writes and reduce database pressure.'
tags: ["ecto", "elixir", "processes", "registry"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Homemade analytics with Ecto and Elixir"
    url: "https://dashbit.co/blog/homemade-analytics-with-ecto-and-elixir"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/dashbit-co--homemade-analytics-with-ecto-and-elixir.md"
    kind: repo
---

The article explains a small analytics system built for the Dashbit website. It avoids cookies, stores page access counts by date and path, and uses Ecto upserts to increment counters when the same page is accessed again.

## Reading notes

- The goal is to avoid tracking users as much as possible, so the site uses no cookies.
- The system still records which pages are frequently accessed.
- Each access is stored by date and path, with the date and path forming a composite primary key.
- An Ecto upsert increments the counter when a matching row already exists.
- The first version depends on the database accepting every write.
- To reduce pressure on the database, writes move to separate Elixir processes.
- A worker process collects page visits and writes them after a delay.
- The worker traps exits so it can flush pending writes on shutdown.
- The delay is randomized between 10 and 20 seconds to avoid many processes writing at once.
- A Registry maps each page path to its worker process.
- A DynamicSupervisor starts workers on demand.
- If two requests race to start the same worker, the code handles the already-started case.
- The worker registers itself with the Registry when it starts.
- The bump function is called after a successful 200 response, using the request path.
- The article notes that with many pages, the design could be changed so workers stop after each upsert.
