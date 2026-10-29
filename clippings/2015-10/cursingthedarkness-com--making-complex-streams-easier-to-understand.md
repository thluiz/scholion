---
url: "http://www.cursingthedarkness.com/2015/08/making-complex-streams-easier-to.html"
captured_at: "2015-10-02T07:49:46-03:00"
title: "Curse the Darkness: Making Complex Streams Easier to Understand"
domain: "cursingthedarkness-com"
---

# Making Complex Streams Easier to Understand

Recently the topic of complicated pipe sequences came up on the Elixir Slack channel and there were comments about the inscrutability of a really complicated Stream built of pipes. This is a typical example:

```
 File.stream!("priv/data/stops.csv")
    |> Stream.drop(1)
    |> Stream.map(&(Station.fromCSVRow &1)
    |> Enum.each(&(Station.Store.put(&1)))
```

One thing to always keep in mind is that Elixir is an expression based language and any result can always be replaced by a function. The other is that Streams are merely a composition of functions.
A more readable way to write the above would be

```
def station_stream(file) do
```

```
   File.stream!(file) 
```

```
   |> Stream.drop(1)
```

```
   |> Stream.map((&(Station.fromCSVRow &1))
```

```
station_stream("priv/data/stops.csv")
```

```
  |> Enum.each(&(Station.Store.put(&1))
```

Additionally, you can put that Stream in a variable and use it anywhere in the program.
As long as the underlying file does not change, the values of the enumeration will not change.

```
stops = station_stream("priv/data/stops.csv")

A File.stream always enumerates through the whole file each time it is evaluated. 
Pipes are one of the features that draws programmers to Elixir, but like anything good you can always over do it. Readability and maintainability should be the first goal. I'm not sure where the exact limit is, but I am sure that pipes can be abused to make code very difficult to reason about. My personal limit seems to be about 3-4 in a sequence.
```
