---
url: "http://learningelixir.joekain.com/stream-patterns-in-elixir/"
captured_at: "2015-05-07T13:16:40-03:00"
title: "Elixir Stream Patterns"
domain: "learningelixir-joekain-com"
---

# [Elixir Stream Patterns](http://learningelixir.joekain.com/stream-patterns-in-elixir/ "Elixir Stream Patterns")

I’ve written about [Streams](http://learningelixir.joekain.com/streams/) before in my series on functional programming in Elixir but that was a largely theoretical post. This week I tried to take a more practial look at my code and other code to see what patterns are used with Streams in Elixir. However, while looking at several projects I found that Streams don’t seem to be in wide use. I also tweeted to #elixirlang to see if I could get any suggestions:

but have not received any replies.

I will discuss the examples I found and hopefully this post will encourage people to explore streams and use them where appropriate.

## Bmark

My own [Bmark](https://github.com/joekain/bmark) benchmarking tool uses the `Stream` module to run benchmarks:

```
# From lib/bmark/server.ex
 collect_single_benchmarkentry 
  
    entrymodule
    entry
    Streamrepeatedly -> entry  |> Streamentry
```

I like this pattern of using `Stream.repeatedly/1` to run a function multiple times with `Stream.take/1` to control the number of times. It works like a for loop construct without needing a mutable counter. This of course only works with `Stream` because there is no `repeatedly` function in the `List` module.

I feel like I should use this pattern more often, but thinking about it may not always be that useful. The escence of teh pattern

> ```
> Streamrepeatedly |> Streamcount
> ```

implies that the function `f` is not referentially transparent. That is, `f` does not give the same result each time it is called with the same input (though in this case f has no input). If `f` were referentially transparent it could be memoized so that only the first call would be necessary. The fact that I want to call `f` multiple times suggests that I believe that each call will have a different result.

The `time` function, which uses `:timer.tc/3`, used to measure the time of a real event will not always give the same result due to dynamic conditions on the system. This is why this pattern is useful for Bmark. But in general, this may not be so useful.

For this post I spent a little time thinking about ways I could write this without using streams. While experimenting to get the syntax right, and to confirm correctness I wrote them as tests and pushed them to github. You can see the code [here](https://github.com/joekain/stream_patterns) or you can just read on.

My first thought was to use ranges and `map` like this:

```
count
```

except that this doesn’t work, the arity of the function passed to map has to be 1 but `f` has arity 0. I need to write:

```
count   ->
```

Having to wrap the `f` this way decreases the readability a lot. I also think the `1..` doesn’t contribute much to readability either. Next, I tried a comprehension

> ```
>   <- count
> ```

Now, this is quite compact and fairly readable even if it is a bit imperative. Again `1..` doesn’t contribute much in this case but overal this version is cleaner that my original `Stream.repeatedly(f) |> Stream.take(count)`. I’ll probably use this version from now on.

## ExUnit

ExUnit uses `Stream` in two functions in the ExUnit.DocTest module. The first depends on the second so I’ll start by looking at `filter_by_opts`

```
 filter_by_optstests  
      :only  
  except  :except  

  Streamfiltertests  ->
      fun_arity
    except
```

This function takes a list of tests and passes it to `Stream.filter`. The filter function is pretty involved. Looking at the [history of the code](https://github.com/elixir-lang/elixir/commit/bbc0fe0a6344f6c698e5bdfee2a7744f5097c4f4#diff-523da743d62635a44900f16f8cd7f504L146), it looks like this was originally `Enum.filter`.

`filter_by_opts` is called by `__doctests__`

```
 __doctests__module  
  do_import  Keyword :import false

  extractmodule
  |> filter_by_opts
  |> Streamwith_index
  |>    ->
    compile_test module do_import
```

This function has a pipeline with a four stages. These stages do the following:

- extract - Extracts all the tests from the module and returns a `List` of tests.
- filter\_by\_opts - Filters the `List` using `Stream.filter` and returns a `Stream`.
  - This is finite Stream as it is a filter over a finite List.
- Stream.with\_index - Just numbers the elements in the previous stream.
- Enum.map - Builds a `List` of compiled tests.

So this pattern boils down to:

> ```
> Streamfilter  |> Streamwith_index |>
> ```

Given the use of `Enum.map` which eagerly consumes its argument, I don’t understand the need to use `Stream.filter` and `Stream.with_index` over their `Enum` counterparts here. That is, I think this is really the same as:

```
filter  |> with_index |>
```

If you have any thoughts on this please share them in the comments.

elixir/lib/mix/lib/mix/utils.ex has a nice use of Streams:

```
 """
Returns `true` if any of the `sources` are stale
compared to the given `targets`.
"""
 stale?sources targets 
   stale_streamsources targets

 extract_stalesources targets 
  stale_streamsources targets |> to_list

 stale_streamsources targets 
  modified_target  targets |> last_modified |> 

  Streamfiltersources source ->
    last_modifiedsource  modified_target
```

`stale_stream` is used in two public functions, `stale?` and `extract_stale`. Because of `extract_stale` the `Stream` must be able to produce the entire list of stale files. But, `stale?` uses `Enum.any` which can stop evaluation of the `Stream` as soon as it finds a match. This pattern can be boiled down to

> ```
> Streamfiltercollection  |>
> ```

This pattern leverages the lazy evaluation of `Stream`s to save work. It only needs to evaluate elements until it finds one that is truthy. It can avoid evaluating any elements after the match is found.

In Mix’s case this can potentially save a lot of work as the filter used in `stale_stream` calls `last_modified` has to look at the filesystem to get the file’s last modified timestamp.

## Conclusion

I hope you’ve learned something about using Streams in Elixir, I know have. I think the most important thing to take away from this post is that Elixir has a rich syntax and there are many ways to express your ideas. Experiment with the syntax, find the most expressive way to write your code, and have fun with it. If you come up with interesting ways to use streams or to not use streams I’d love to hear about them.

---

**Elixir Stream Patterns** was published on March 17, 2015.
