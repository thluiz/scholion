---
title: "Unit Tests in Elixir - Part 2"
date: '2026-11-16T20:10:41+00:00'
category: webclip
summary: 'Explains how to unit test Elixir functions that talk to other processes by injecting dependencies, and treating commands and queries differently in tests.'
tags: ["elixir", "unit-testing", "genserver", "test-doubles"]
has_commentary: false
generated_by: "openai/gpt-5.1"
sources:
  - title: "Unit Tests in Elixir - Part 2"
    url: "https://devonestes.com/unit-tests-in-elixir-part-2"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/devonestes-com--unit-tests-in-elixir-part-2-testing-processes.md"
    kind: repo
---

This article continues a series about unit testing in Elixir, focusing on functions that interact with other processes. The author takes a `Persist` module that calls a `GenServer`-backed `KVStore` and shows that unit tests should avoid real inter-process communication by injecting dependencies. Using default arguments, `Persist` receives a module implementing the same API as `KVStore`, which in tests is replaced by a simple test double. The article distinguishes between commands (asynchronous, no response expected) and queries (synchronous, response expected) and explains how to test each kind.

## Reading notes

- The initial `Persist` functions call `KVStore` directly, so their behavior depends on `GenServer` inter-process communication.
- Removing real inter-process communication is necessary to keep these tests as unit tests.
- Introducing a configurable adapter in `KVStore` is mentioned as possible but described as awkward and not a good fit here.
- The author introduces a seam by adding a module argument with a default (`kvstore \\ KVStore`) to the `Persist` functions.
- With default arguments, `Persist` keeps the original behavior in production but accepts an injected dependency in tests.
- In tests, a nested `KVStore` module acts as a test double, not as a real `GenServer`.
- The test double’s `write/2` sends a message to `self()`, which is the test process, allowing assertions with `assert_receive`.
- The test double’s `read/1` returns a tagged tuple that the test can compare directly.
- The author labels `write/2` in the real implementation as a command, since it corresponds to a `cast` where no response is expected.
- Commands are described as messages whose handling is internal to the receiving process and not the concern of the caller.
- For commands, the unit test should only verify that the correct function was called with the correct arguments, observed via received messages.
- The real `read/1` is labeled a query, matching a `call` where a response is expected.
- For queries, what matters in this test is that something is returned and that the function is called with the right argument, not the internal logic of the response.
- The article states that the detailed logic of what `KVStore` returns should be unit tested in `KVStoreTest`, not in `PersistTest`.
- In tests for queries, the verification consists in asserting against the return values of the mocked function.
- The author summarizes a three-part approach: inject dependencies as function arguments so mocks or test doubles can be used, test commands by sending messages to `self()`, and test queries by asserting on return values.
- The article claims that following these three rules allows effective unit testing of functions that interact with other processes.
