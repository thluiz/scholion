---
title: "Test async work in Elixir with assert_eventually"
date: '2026-09-25T20:15:41+01:00'
category: webclip
summary: 'The post shows that sleeping in tests is fragile for async Elixir work and presents assert_eventually/1 as a helper that retries an assertion until it succeeds or times out.'
tags: ["elixir", "async-testing", "exunit"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Test async work in Elixir with assert_eventually"
    url: "https://peterullrich.com/async-testing-with-eventually"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/peterullrich-com--test-async-work-in-elixir-with-assert-eventually.md"
    kind: repo
---

The post argues that waiting with Process.sleep/1 is a poor way to test asynchronous Elixir work, because the task may finish later than expected or much earlier than the chosen delay. It presents assert_eventually/1 as a helper that keeps checking an assertion at short intervals until it passes or a timeout is reached.

## Reading notes

- Async tasks can update database state after the test process continues, which makes the moment for reloading the record uncertain.
- Sleeping for a fixed time can fail when the task takes longer than expected.
- Sleeping for a fixed time can also waste time when the task finishes quickly.
- assert_eventually/1 retries the assertion every 10ms by default.
- The helper raises ExUnit.AssertionError after the timeout is reached.
- In the example, the test checks whether the file record has changed to status :processed.
- The post says the test passes as soon as the record is updated and fails if that does not happen within 100ms.
