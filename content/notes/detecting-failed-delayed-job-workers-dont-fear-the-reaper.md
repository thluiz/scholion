---
title: "Don’t Fear the Reaper: Detecting Failed Delayed Job Workers"
date: '2013-11-30T23:15:31-03:00'
category: webclip
summary: 'The post explains how to detect failed Delayed Job workers sooner by adding worker heartbeats and a reaper process that unlocks orphaned jobs instead of waiting for max_run_time.'
tags: ["delayed-job", "rails", "worker-heartbeat", "background-jobs"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Detecting Failed Delayed Job Workers: Don't Fear the Reaper"
    url: "http://www.salsify.com/blog/detect-failed-delayed-job-workers/1571?utm_source=rubyweekly&utm_medium=email"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2013-11/salsify-com--detecting-failed-delayed-job-workers-dont-fear-the-reaper.md"
    kind: repo
---

The post proposes a way to retry Delayed Job tasks sooner when a worker crashes, is restarted, or is shut down by autoscaling. Instead of waiting for max_run_time to expire, it adds heartbeat tracking and a reaper that unlocks jobs tied to workers that have stopped reporting.

## Reading notes

- Delayed Job stores lock metadata in the delayed_jobs table, including locked_at and locked_by.
- A job becomes eligible again when it is not locked by another worker or when the lock is older than max_run_time.
- The author says max_run_time is too long in their setup because it must accommodate long-running bulk import and export jobs.
- The solution has two parts: a plugin that writes heartbeat data for each worker and a reaper that unlocks jobs for workers without recent heartbeats.
- The heartbeat design uses three pieces: WorkerModel, WorkerHeartbeat, and a Plugin that hooks into the worker lifecycle.
- WorkerModel keeps each worker name and last heartbeat timestamp, and it includes scopes for dead workers and active names.
- WorkerHeartbeat runs a background thread that updates the heartbeat on an interval and shuts down with a self-pipe trick.
- The heartbeat thread is set to abort on exception, and on shutdown it removes the worker record and clears active database connections.
- The plugin starts the heartbeat before worker execution and stops it after execution.
- The reaper deletes dead worker records, finds jobs whose locked_by value is not among active workers, and clears locked_at, locked_by, and increments attempts.
- In the author’s Heroku setup, a clockwork process runs the unlock routine on a schedule.
- The article ends with configuration values for enabling heartbeats, setting heartbeat interval, setting timeout, and setting the dead-worker polling interval.
