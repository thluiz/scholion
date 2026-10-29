---
title: "Debug delayed job in Rails"
date: '2015-07-26T11:01:51-03:00'
category: webclip
summary: 'The post shows how to debug delayed_job in a Rails app by opening Rails console, creating a Delayed::Worker with quiet: false, and starting it so debugger statements in jobs can be used.'
tags: ["rails", "delayed-job", "debug", "background-job"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Debug delayed job in Rails"
    url: "https://concluzions.wordpress.com/2015/07/18/debug-delayed-job/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2015-07/concluzions-wordpress-com--debug-delayed-job-in-rails.md"
    kind: repo
---

The post explains a simple way to debug delayed_job in a Rails project. It uses the Rails console to create a worker with quiet set to false, then starts that worker so job code can be debugged directly.

## Reading notes

- Open a Rails console in the project.
- Create a delayed_job worker with `quiet: false` so it prints to the console.
- Start the worker from the console.
- Use a debugger statement inside the jobs and debug them without loggers.
