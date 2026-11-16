---
title: "Unit Tests in Elixir - Part 2"
date: '2026-11-16T20:09:25+00:00'
category: webclip
summary: 'Explains how to unit test Elixir functions that talk to other processes by injecting dependencies, and by treating GenServer casts as commands and calls as queries.'
tags: ["elixir", "unit-testing", "genserver", "test-doubles"]
has_commentary: false
generated_by: "openai/gpt-5.1"
sources:
  - title: "Unit Tests in Elixir - Part 2"
    url: "https://devonestes.com/unit-tests-in-elixir-part-2"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/devonestes-com--unit-tests-in-elixir-part-2-testing-genserver.md"
    kind: repo
---

This article tackles how to unit test Elixir functions that communicate with another process, using a `Persist` module that talks to a `KVStore` GenServer as an example. The author introduces dependency injection via default module arguments so that tests can replace the real GenServer with a simple test double. Commands (cast-style calls) are tested by sending messages to the test process and asserting they were received, while queries (call-style calls) are tested by asserting on the return values of the mocked module.

## Reading notes

- The author continues from part 1, shifting focus from general unit test rules to specifics of testing behaviors that involve inter-process communication.
- `KVStore` is defined as a `GenServer` that stores key/value pairs with `write/2` using `GenServer.cast/2` and `read/1` using `GenServer.call/2`.
- `Persist.write_all/1` and `Persist.read_all/1` are shown initially calling `KVStore` directly, which couples them to inter-process communication.
- In the original `Persist` version, testing is hard because all behavior depends on talking to `KVStore`'s process.
- The author dismisses adding a configurable adapter in `KVStore` for this scenario, considering it awkward and still difficult to test, though adapter patterns can suit other cases.
- To enable unit testing, the author introduces a seam for dependency injection by adding a `kvstore` argument with a default value of `KVStore` in both `write_all/2` and `read_all/2`.
- With default arguments, production code continues to use the real `KVStore` module, while tests can pass in a test double module.
- The modified `Persist` keeps its behavior but gains the ability to inject a dependency as a simple function argument.
- The author notes that default arguments on every function make the API less visually appealing, but they make proper unit testing possible.
- In tests, a nested `KVStore` module acts as a test double: its `write/2` sends a message to `self()`, and its `read/1` returns a tagged tuple.
- The test for `write_all/2` calls `Persist.write_all/2` with a map and the test double module, then uses `assert_receive/1` to ensure the expected `{:write, {key, value}}` messages arrive in the test process.
- The test for `read_all/2` directly asserts that `Persist.read_all/2` returns a list of the tagged tuples produced by the test double's `read/1`.
- The test double is not a `GenServer`; instead, it hardcodes behaviors that make verification trivial for the tests.
- The implementation's `write/2` is described as a command, and `read/1` as a query, borrowing terminology from object-oriented design.
- A command corresponds to a `GenServer.cast/2` where no response is expected and the receiving process privately decides what to do with the message.
- For commands, the test's responsibility is limited to verifying that the correct message was sent with the proper arguments, not what the other process does internally.
- This verification for commands is done by having the mock send a message to the test process and asserting that the test process received it.
- A query corresponds to a `GenServer.call/2` where a response is expected from the receiving process.
- For queries, the unit tests for the calling module only need to ensure the function is invoked with the right argument, which can be checked by asserting against the return value from the test double.
- The logic that determines what a real query should return for given input belongs in separate unit tests for the `KVStore` module itself.
- The author closes with three key guidelines for testing functions that talk to other processes: inject dependencies as function arguments, test commands via messages to `self()`, and test queries via assertions on return values.
