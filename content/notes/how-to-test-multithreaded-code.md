---
title: "How to Test Multithreaded Code"
date: '2015-12-23T13:15:34-03:00'
category: webclip
summary: 'Mike Perham says multithreaded code is hard to write and harder to test, and recommends separating threading from work and using callbacks to make threaded APIs testable without sleep calls.'
tags: ["multithreading", "testing", "ruby"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "How to Test Multithreaded Code"
    url: "http://www.mikeperham.com/2015/12/14/how-to-test-multithreaded-code"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2015-12/mikeperham-com--how-to-test-multithreaded-code.md"
    kind: repo
---

Mike Perham says multithreaded code is hard to write and even harder to test. His advice is to keep thread management simple, move complexity into smaller methods that can be called directly, and design APIs so threaded behavior can be tested without relying on sleep.

## Reading notes

- Separate threading from work so the test suite can call smaller internal methods directly.
- Keep the run loop as simple as possible and move most complexity into methods such as fetch and process.
- In some cases, thread management code is verified manually instead of being covered by tests.
- To test threaded code, start the other thread, tell it to process something, wait for the result, and then assert the results.
- Avoid sleep-based tests by using a callback block that sends results back and signals the waiting thread.
- The example uses a queue, a mutex, and a condition variable to coordinate work between threads.
