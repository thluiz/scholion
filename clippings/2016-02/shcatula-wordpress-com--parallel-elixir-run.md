---
url: "https://shcatula.wordpress.com/2016/02/09/parallel-elixir-run/"
captured_at: "2016-02-29T11:02:45-03:00"
title: "Parallel Elixir Run"
domain: "shcatula-wordpress-com"
---

# Parallel Elixir Run

[Last time](https://shcatula.wordpress.com/2016/02/05/elixir-agent-elixir/) we’ve managed to access a worker from multiple processes. This time, we’ll try to distribute worker’s load across several processes. The [problem](http://exercism.io/exercises/elixir/parallel-letter-frequency/readme) we’re trying to solve is to calculate occurrence of letters in given list of texts. There is no need for shared state, we just want to distribute the load. Hence, the [Agent](http://elixir-lang.org/docs/v1.2/elixir/Agent.html) is not really needed. [Task](http://elixir-lang.org/docs/v1.2/elixir/Task.html) supports exactly what we need, the async call.

It works like this:

- invoke a job, asynchronously
- wait for job to finish and return results

And you have the corresponding methods:

Or, taken from the documentation:

|  |  |
| --- | --- |
|  | `task = Task.async(fn -> do_some_work()` `end``)`  `res  = do_some_other_work()`  `res + Task.await(task)` |

Here, the important thing to notice is that you need to await for the result, and that both processes are linked so any crashes on either side will cause the other to fail as well. This suits our purpose quite nicely, so no worries there.

The above example shows how to spawn and await a single process. But, we’d like to spawn more, and distribute an unknown load evenly across those processes / workers, later collecting all of their results. And, funny enough, [Enum.map/2](http://elixir-lang.org/docs/v1.2/elixir/Enum.html#map/2) to the rescue!

|  |  |
| --- | --- |
|  | `@spec` `frequency([``String``.t], pos_integer) :: Dict.t`  `def` `frequency(texts, workers)` `do`  `texts`  `|> group_by(workers)`  `|> Enum.map(fn(texts_for_a_worker) ->`  `Task.async(fn -> count_frequencies(texts_for_a_worker)` `end``)`  `end``)`  `|> Enum.map(&(Task.await(&``1``,` `10000``)))`  `|> merge_results`  `end` |

So, the actual magic happens with first [Enum.map/2](http://elixir-lang.org/docs/v1.2/elixir/Enum.html#map/2), which spawns a new worker and delivers it the texts to process and in the second [Enum.map/2](http://elixir-lang.org/docs/v1.2/elixir/Enum.html#map/2), which awaits each worker, mapping it’s results. The complete example is a bit more elaborate and can be found at [Github](https://github.com/elvanja/curly-exercisms/tree/master/elixir/parallel-letter-frequency).

So how much speed we’ve gained? To get a rough estimate, I’ve created a list of ten thousand short poems (through [List.duplicate/2](http://elixir-lang.org/docs/v1.2/elixir/List.html#duplicate/2) on some national anthems, I’m not that eager to write poems yet!) and put it through the loops, while changing the number of workers. Here are some very much informal results:

- 1 worker – 12 seconds
- 4 workers – 5 seconds
- 16 workers – 5 seconds
- 32 workers – 5 seconds
- 128 workers – 5 seconds

I didn’t go so far as to inspect the reasons behind the top off, that might be an interesting exercise for later time. The take away is that we do have some significant gain compared to a single process, with little more code than usual, so it’s a win in my book
