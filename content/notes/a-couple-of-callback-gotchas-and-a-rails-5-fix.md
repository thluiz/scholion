---
title: "A Couple of Callback Gotchas (and a Rails 5 Fix)"
date: '2015-08-03T20:49:57-03:00'
category: webclip
summary: 'The post explains why `after_save` can trigger background jobs before other processes can see the record, why `after_commit` avoids that race, and why test suites need a separate fix until Rails 5.'
tags: ["rails", "active-record-callbacks", "after-commit", "testing"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "A couple of callback gotchas (and a Rails 5 fix) - Weissblog"
    url: "http://www.justinweiss.com/blog/2015/03/10/a-couple-callback-gotchas-and-a-rails-5-fix"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2015-08/justinweiss-com--a-couple-of-callback-gotchas-and-a-rails-5-fix.md"
    kind: repo
---

Rails callbacks can run code during different stages of a model’s lifecycle, but using `after_save` to enqueue background work can race with the database transaction. A job may try to load a record before the commit finishes, so another process cannot find it yet.

## Reading notes

- `after_save` runs before the surrounding transaction is committed, so Sidekiq may not be able to see the saved record yet.
- The example switches the indexing hook from `after_save` to `after_commit` so the job is queued only after the record becomes visible to other database connections.
- Rails test cases wrap each test in a transaction, which prevents `after_commit` from running in the usual way.
- The `test_after_commit` gem makes those callbacks run in tests after the relevant transaction boundary.
- The post says Rails 5 fixed this testing problem, so the extra gem would no longer be needed there.
