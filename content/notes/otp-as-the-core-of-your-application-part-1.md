---
title: "OTP as the Core of Your Application Part 1"
date: '2020-08-26T19:31:29+00:00'
category: webclip
summary: 'The post explains the Actor Model on the BEAM, then builds a Phoenix bookstore that reads from GenServers in later parts. Here it sets up the app, scrapes Manning data, and seeds Postgres.'
tags: ["actor-model", "beam", "phoenix", "genserver"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "OTP as the Core of Your Application Part 1"
    url: "https://akoutmos.com/post/actor-model-genserver-app"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/akoutmos-com--otp-as-the-core-of-your-application-part-1.md"
    kind: repo
---

The post introduces a two-part series on the Actor Model in Elixir and Erlang and sets up a Phoenix bookstore application to explore it. In this first part, the app is prepared with dependencies, a Floki-based scraper for Manning catalog data is written, and sample books are loaded into Postgres.

## Reading notes

- The series will use a Phoenix application whose business logic is powered mainly by GenServers, with the database used for persistence when needed.
- The Actor Model is presented as a way to reason about concurrent programs through message passing and isolated internal state.
- On the BEAM, an actor is a lightweight process scheduled preemptively by the runtime.
- Each process has a mailbox, and messages are handled one at a time as atomic operations.
- The BEAM can run thousands of concurrent processes, with schedulers sharing CPU time across them.
- The example application is a book store exposed through a RESTful API.
- The bookstore tracks books and their quantities, and adjusts inventory when orders are placed.
- The project installs Phoenix and adds Floki and HTTPoison as dependencies.
- The scraper fetches the Manning catalog page, extracts book links, and then visits each book page.
- The scraper collects title, authors, description, and price for each book.
- The extracted data is written to a file that can be loaded later as seed data.
- The database migration creates a books table with title, authors, description, price, quantity, and timestamps.
- The Ecto schema mirrors the migration and derives JSON encoding for book data.
- The seed script loads the scraped data, assigns quantities, and inserts each book into the database.
- Books marked as not for sale get price set to "N/A" and quantity set to 0.
- The application setup is verified by running Postgres, executing `mix ecto.setup`, and starting Phoenix in IEx.
- The post ends by saying that Part 2 will use Registry and DynamicSupervisor to move more application state into GenServer processes.
