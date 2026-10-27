---
title: "Why I can't install postgresql with rails 4.0.0.rc1 (ruby 2.0)"
date: '2013-11-12T22:28:31-03:00'
category: webclip
summary: 'Describes a Bundler platform detection problem on Windows 7 x64 with Ruby 2.0, Rails 4.0.0, and pg 0.15.1. The temporary fix is to edit Gemfile.lock and add the x64 mingw32 pg variant.'
tags: ["bundler", "postgresql", "rails"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Why I can't install postgresql with rails 4.0.0.rc1 (ruby 2.0) - Stack Overflow"
    url: "http://stackoverflow.com/questions/17003917/why-i-cant-install-postgresql-with-rails-4-0-0-rc1-ruby-2-0"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2013-11/stackoverflow-com--why-i-cant-install-postgresql-with-rails-4-0-0-rc1-ruby-2-0.md"
    kind: repo
---

The page says Bundler has a platform detection and verification problem on Windows 7 x64 with Ruby 2.0, Rails 4.0.0, PostgreSQL 9.2.4 x64, pg 0.15.1, and mysql2 0.3.11. It gives a temporary workaround that edits Gemfile.lock to include the x64 mingw32 version of pg alongside the x86 one.

## Reading notes

- Reports a Bundler platform detection and verification problem on Windows 7 x64 with Ruby 2.0, Rails 4.0.0, PostgreSQL 9.2.4 x64, pg 0.15.1, and mysql2 0.3.11.
- Suggests a manual edit to Gemfile.lock as a temporary workaround.
- Replaces the pg line that lists only pg (0.15.1-x86-mingw32) with one that also includes pg (0.15.1-x64-mingw32).
