---
title: "Persistent session data via a database in Phoenix LiveView"
date: '2026-11-16T03:57:28+00:00'
category: webclip
summary: 'The post shows how to persist LiveView session data by assigning a `session_id` in the Plug session, storing data in PostgreSQL, and loading it on mount instead of relying on `localStorage`.'
tags: ["elixir", "phoenix-liveview", "postgresql", "session-data"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Persistent session data via a database in Phoenix LiveView"
    url: "https://thepugautomatic.com/2020/05/persistent-session-data-via-a-database-in-phoenix-liveview"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/thepugautomatic-com--persistent-session-data-via-a-database-in-phoenix-liveview.md"
    kind: repo
---

The post describes a way to keep LiveView session data across reloads and browser restarts by storing it in PostgreSQL. It assigns a unique `session_id` in the Plug session, keeps the cookie alive with a long `max_age`, and uses that ID as the lookup key for persisted settings.

## Reading notes

- LiveView keeps state in a process that ends when the page is left, so it does not have an obvious built-in way to persist session data.
- The approach starts by adding a `session_id` to the browser session in the router with a Plug.
- Session cookies are configured with a long `max_age` so the browser can keep them after a restart.
- The app uses the `session_id` as a key to store and retrieve data from PostgreSQL.
- The example table stores `username`, `session_id`, and `read_at`.
- The `Settings` schema validates `session_id` and defines `for_session/1` to load the record for a session.
- When a record exists, `read_at` is updated so stale records can be tracked.
- Stale records older than `@stale_after_days` are deleted when `for_session/1` runs.
- If no record exists, `for_session/1` returns an unpersisted `%Settings{session_id: sid}`.
- In the LiveView example, `mount/3` loads settings from the session and assigns them to the socket.
- The form updates `username` on `phx-change`, and the handler inserts or updates the settings record depending on whether it already has an `id`.
- The author says this feels more elegant than the `localStorage` version because the data is available on the first render.
- The discussion notes that this is similar to a database-backed session store, but LiveView accesses it outside the usual HTTP request/response cycle.
