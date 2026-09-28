---
title: "Background jobs with Oban, part 1: stop blocking your LiveView"
date: '2026-09-28T14:17:38+01:00'
category: webclip
summary: 'The post moves preview fetching out of a LiveView into an Oban background job, showing installation, migration, configuration, worker code, and job enqueueing.'
tags: ["elixir", "oban", "liveview", "background-jobs"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Background jobs with Oban, part 1: stop blocking your LiveView"
    url: "https://potions.io/blog/background-jobs-with-oban-part-1"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/potions-io--background-jobs-with-oban-part-1-stop-blocking-your-liveview.md"
    kind: repo
---

This post moves slow preview fetching out of a LiveView event handler and into an Oban job. It shows how the app keeps the link creation flow responsive by inserting a job after the link is saved, then letting a worker fetch the page, store the metadata, and mark the link ready or failed.

## Reading notes

- Oban stores jobs in the database, so if PostgreSQL is already in use there is no separate queue server to deploy.
- The example app, Unfurl, pastes in a URL, fetches page data, stores title, description, and preview image, and displays the result.
- The current implementation fetches preview data inside the LiveView `save` handler, so a slow site blocks the user.
- The setup adds `oban` and `oban_web`, runs `mix deps.get`, and creates an Oban jobs table with a migration based on Oban's manual installation guide.
- The configuration uses `Oban.Engines.Basic`, points Oban at `Unfurl.Repo`, defines a `previews` queue with concurrency 5, sets `pruner` to delete finished jobs after seven days, and sets `lifeline` to rescue jobs after one hour.
- Oban is added to the application's supervision tree, and test configuration sets `testing: :manual` so jobs are inserted but not executed automatically.
- A `PreviewWorker` module uses `Oban.Worker` with the `previews` queue and up to five attempts.
- The worker receives a job with a link ID, looks up the link, fetches preview data, applies it on success, and marks the link as failed on error.
- If the link no longer exists, the worker returns `{:cancel, :link_deleted}` so Oban stops retrying.
- The `Links` module gains `fetch_link`, `apply_preview`, `mark_failed`, and `schedule_preview`.
- `apply_preview` sets `fetched_at` to the current time and stores the fetched attributes with status `ready`.
- `schedule_preview` builds a job from the link ID with `PreviewWorker.new` and inserts it with `Oban.insert`.
- The LiveView `save` handler now creates the link, enqueues the job, and shows a flash message instead of fetching immediately.
- After the change, the page stays responsive, and the preview appears after refresh once the background work finishes.
