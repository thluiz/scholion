---
url: "https://peterullrich.com/async-testing-with-eventually"
captured_at: "2026-09-25T20:15:41+01:00"
title: "Test async work in Elixir with assert_eventually"
domain: "peterullrich-com"
---

Welcome to another blog post, folks! First another dad joke:

```
What do you call a medieval spy?
Sir Veillance
```

Alrighty, today's a quick one. How to assert that an async task succeeds eventually in your Elixir tests.

## The Problem

Elixir makes writing asynchronous work easy, but testing it is still a bit tricky. Let's have a look at an example test:

```
test "async task updates my database record eventually" do
file = insert(:file, status: :unprocessed)
# This task processes a file and updates its db record asynchronously.
MyProcessingTask.process_async(file)
# Wait for the task to finish.
Process.sleep(100)
# Assert that the db record was updated.
assert %{status: :processed} = Repo.reload!(file)
end
```

In this example test, we execute a task that runs asynchronously to our test process. It processes a file and updates its database record when the process finishes. The problem here is that we don't know when the process finishes and when to reload our file to check its status. We could probably monitor the task and write a callback that notifies us when the task shuts down, but we're lazy, so we simply sleep for 100ms and assume that the process has finished by then.

Using `Process.sleep/1` to wait for an async task to finish is meeeh. If our task takes longer than 100ms, our test fails although the task might have succeeded eventually. Also, if the task only takes 10ms, our test will still wait 90ms more which might balloon the overall execution time of our test suite if we have many such tests.

Luckily, there's a better way: `assert_eventually/1`.

## The Solution

This little helper function checks whether our assertion succeeds ... eventually. By default, it checks every 10ms if our condition succeeds until a threshold of 100ms is reached at which it raises an `ExUnit.AssertionError`.

```
# test/support/data_case.ex
@doc """
A test helper for asserting that a function will return
a truthy value eventually within a given time frame.
"""
def assert_eventually(fun, timeout \\ 100, interval \\ 10)
def assert_eventually(_fun, timeout, _interval) when timeout <= 0 do
raise ExUnit.AssertionError, "Eventually assertion failed to receive a truthy result before timeout."
end
def assert_eventually(fun, timeout, interval) do
result = fun.()
ExUnit.Assertions.assert(result)
result
rescue
ExUnit.AssertionError ->
Process.sleep(interval)
assert_eventually(fun, timeout - interval, interval)
end
```

Using this helper, we can check every 10ms whether our async task has updated the file record already:

```
test "async task updates my database record eventually" do
file = insert(:file, status: :unprocessed)
# This task processes a file and updates its db record asynchronously.
MyProcessingTask.process_async(file)
assert_eventually(fn ->
assert %{status: :processed} = Repo.reload!(file)
end)
end
```

If the record isn't updated within 100ms, our test fails. If the record is updated earlier, our test succeeds. Nice!

## Conclusion

And that's it! I hope you enjoyed this article! If you want to support me, you can buy my firewall for Phoenix [Phx2Ban](https://ezsuite.dev/) or my [book](https://pragprog.com/titles/puphoe/building-table-views-with-phoenix-liveview/) or video courses ([one](https://indiecourses.com/catalog/build-an-mvp-with-elixir-6i4V9yOqLL54GuG0HkV9HR) and [two](https://indiecourses.com/catalog/building-forms-with-phoenix-liveview-2OPYIqaekkZwrpgLUZOyZV)). Follow me on [Bluesky](https://bsky.app/profile/peterullrich.com) or subscribe to my newsletter below if you want to get notified when I publish the next blog post. Until next time! Cheerio 👋
