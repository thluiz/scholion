---
url: "http://www.littlelines.com/blog/2014/07/08/elixir-vs-ruby-showdown-phoenix-vs-rails/"
captured_at: "2015-01-16T20:25:58-03:00"
title: "Elixir vs Ruby Showdown - Phoenix vs Rails"
domain: "littlelines-com"
---

# [Elixir vs Ruby Showdown - Phoenix vs Rails](http://www.littlelines.com/blog/2014/07/08/elixir-vs-ruby-showdown-phoenix-vs-rails/)

###### Written by Chris McCord

![ed6068d2892a2f76ce84f62446545f32.png](littlelines-com--elixir-vs-ruby-showdown-phoenix-vs-rails/ed6068d2892a2f76ce84f62446545f32.png)

This is the second post in our *Elixir vs Ruby Showdown* series. In this latest installment, we're exploring the performance of the [Phoenix](https://github.com/phoenixframework/phoenix) and [Rails](http://rubyonrails.org/) web frameworks when put up against the same task. Before we get into code samples and benchmark results, let's answer a few common questions about these kinds of tests:

**tl;dr** Phoenix showed **10.63x** more throughput over Rails when performing the same task, with a fraction of CPU load

## Isn't this apples to oranges?

No. These tests are a direct comparison of our favorite aspects of Ruby and Rails with Elixir and Phoenix. Elixir has the promise to provide the things we love most about Ruby: productivity, metaprogramming, elegant APIs, and DSLs, but much faster, with a battle-tested concurrency and distribution model. The goals of this post are to explore how Elixir can match or exceed our favorite aspects of Ruby without sacrificing elegant APIs and the productive nature of the web frameworks we use.

## Are benchmarks meaningful?

Benchmarks are only as meaningful as the work you do upfront to make your results as reliable as possible for the programs being tested. Even then, benchmarks only provide a "good idea" of performance. Moral of the story: *never trust benchmarks, always measure yourself*.

## What are we comparing?

### Elixir Phoenix Framework

- Phoenix 0.3.1
- Cowboy webserver (single Elixir node)
- Erlang 17.1

### Ruby on Rails

- Rails 4.0.4
- Puma webserver (4 workers - 1 per cpu core)
- MRI Ruby 2.1.0

We're measuring the throughput of an "equivalent" Phoenix and Rails app where specific tasks have been as isolated as possible to best compare features and performance. Here's what we are measuring:

1. Match a request from the webserver and route it to a controller action, merging any named parameters from the route
2. In the controller action, render a view based on the request Accept header, contained within a rendered parent layout
3. Within the view, render a collection of partial views from data provided by the controller
4. Views are rendered with a *pure language templating engine (ERB, EEx)*
5. Return the response to the client

That's it. We're testing a standard route matching, view rendering stack that goes beyond a Hello World example. Both apps render a layout, view, and collection of partials to tests real-world throughput of a general web framework task. No view caching was used and request logging was disabled in both apps to prevent IO overhead. The [wrk](https://github.com/wg/wrk) benchmarking tool was used for all tests, both against localhost, and remotely against heroku dynos to rule out `wrk` overhead on localhost. Enough talk, let's take a look at some code.

## Routers

Phoenix

```
defmodule BenchmarkerRouter 
   PhoenixRouter
  alias BenchmarkerControllers

   "/:title" ControllersPages :index as: :page
```

Rails

```
BenchmarkerApplication.routes.draw 
   "pages#index"
   "/:title" "pages#index" as: :page
```

## Controllers

Phoenix (request parameters can be pattern-matched directly in the second argument)

```
defmodule BenchmarkerControllersPages 
   PhoenixController

  index %{"title" => title} 
    render  "index" title: title members: 
      %{name: "Chris McCord"}
      %{name: "Matt Sears"}
      %{name: "David Stump"}
      %{name: "Ricardo Thompson"}
```

Rails

```
class PagesController  ApplicationController

  index
    @title  params:title
    @members  
       "Chris McCord"
       "Matt Sears"
       "David Stump"
       "Ricardo Thompson"
    
    render "index"
```

## Views

Phoenix (EEx)

```
...
    <h4>Team Members</h4>
    <ul>
      <%=  member <- @members  %>
        <li>
          <%= render "bio.html" member: member %>
        </li>
      <%  %>
    </ul>
...
```

```
<b>Name:</b> <%= @member.name %>
```

Rails (ERB)

```
...
    <h4>Team Members</h4>
    <ul>
      <%  member  @members  %>
        <li>
          <%= render partial: "bio.html" locals: member: member %>
        </li>
      <%  %>
    </ul>
...
```

```
<b>Name:</b> <%= member:name %>
```

## Localhost Results

Phoenix showed **10.63x more throughput**, with a much more consistent standard deviation of latency. Elixir's concurrency model really shines in these results. A single Elixir node is able to use all CPU/memory resources it requires, while our puma webserver must start a Rails process for each of our CPU cores to achieve councurrency.

```
Phoenix:
  req/s: 12,120.00
  Stdev: 3.35ms
  Max latency: 43.30ms

Rails:
  req/s: 1,140.53
  Stdev: 18.96ms
  Max latency: 159.43ms
```

### Phoenix

```
$ mix do deps.get, compile
$ MIX_ENV=prod mix compile.protocols
$ MIX_ENV=prod elixir -pa _build/prod/consolidated -S mix phoenix.start
Running Elixir.Benchmarker.Router with Cowboy on port 4000

$ wrk -t4 -c100 -d30S --timeout 2000 "http://127.0.0.1:4000/showdown"
Running 10s test @ http://127.0.0.1:4000/showdown
  4 threads and 100 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency     8.31ms    3.53ms  43.30ms   79.38%
    Req/Sec     3.11k   376.89     4.73k    79.83%
  121202 requests in 10.00s, 254.29MB read
Requests/sec:  12120.94
Transfer/sec:     25.43MB
```

### Rails

```
$ bundle
$ RACK_ENV=production bundle exec puma -w 4
[13057] Puma starting in cluster mode...
[13057] * Version 2.8.2 (ruby 2.1.0-p0), codename: Sir Edmund Percival Hillary
[13057] * Min threads: 0, max threads: 16
[13057] * Environment: production
[13057] * Process workers: 4
[13057] * Phased restart available
[13185] * Listening on tcp://0.0.0.0:9292

$ wrk -t4 -c100 -d30S --timeout 2000 "http://127.0.0.1:9292/showdown"
Running 10s test @ http://127.0.0.1:9292/showdown
  4 threads and 100 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    21.67ms   18.96ms 159.43ms   85.53%
    Req/Sec   449.74    413.36     1.10k    63.82%
  11414 requests in 10.01s, 25.50MB read
Requests/sec:   1140.53
Transfer/sec:      2.55MB
```

## Heroku Results (1 Dyno)

Phoenix showed **8.94x more throughput**, again with a much more consistent standard deviation of latency and with **3.74x less CPU load**. We ran out of available socket connections when trying to push the Phoenix dyno harder to match the CPU load seen by the Rails dyno. It's possible the Phoenix app could have more throughput available if our client network links had higher capacity. The standard deviation is particularly important here against a remote host. The Rails app struggled to maintain consistent response times, hitting 8+ second latency as a result. In real world terms, a Phoenix app should respond much more consistently under load than a Rails app.

```
Phoenix:
  req/s: 2,691.03
  Stdev: 139.92ms
  Max latency: 1.39s

Rails:
  req/s: 301.36
  Stdev: 2.06s
  Max latency: 8.36s
```

### Phoenix (Cold)

```
$ ./wrk -t12 -c800 -d30S --timeout 2000 "http://tranquil-brushlands-6459.herokuapp.com/showdown"
Running 30s test @ http://tranquil-brushlands-6459.herokuapp.com/showdown
  12 threads and 800 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency   317.15ms  139.55ms 970.43ms   81.12%
    Req/Sec   231.43     66.07   382.00     63.92%
  83240 requests in 30.00s, 174.65MB read
  Socket errors: connect 0, read 1, write 0, timeout 0
Requests/sec:   2774.59
Transfer/sec:      5.82MB
```

### Phoenix (Warm)

```
$ ./wrk -t12 -c800 -d180S --timeout 2000 "http://tranquil-brushlands-6459.herokuapp.com/showdown"
Running 3m test @ http://tranquil-brushlands-6459.herokuapp.com/showdown
  12 threads and 800 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency   318.52ms  139.92ms   1.39s    82.03%
    Req/Sec   224.42     57.23   368.00     68.50%
  484444 requests in 3.00m, 0.99GB read
  Socket errors: connect 0, read 9, write 0, timeout 0
Requests/sec:   2691.03
Transfer/sec:      5.65MB
```

```
load_avg_1m=2.78

sample#memory_total=34.69MB
sample#memory_rss=33.57MB 
sample#memory_cache=0.09MB
sample#memory_swap=1.03MB
sample#memory_pgpgin=204996pages sample#memory_pgpgout=196379pages
```

### Rails (Cold)

```
$ ./wrk -t12 -c800 -d30S --timeout 2000 "http://dry-ocean-9525.herokuapp.com/showdown"
Running 30s test @ http://dry-ocean-9525.herokuapp.com/showdown
  12 threads and 800 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency     2.85s     1.33s    5.75s    65.73%
    Req/Sec    22.68      7.18    61.00     69.71%
  8276 requests in 30.03s, 18.70MB read
Requests/sec:    275.64
Transfer/sec:    637.86KB
```

### Rails (Warm)

```
$ ./wrk -t12 -c800 -d180S --timeout 2000 "http://dry-ocean-9525.herokuapp.com/showdown"
Running 3m test @ http://dry-ocean-9525.herokuapp.com/showdown
  12 threads and 800 connections
	  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency     3.07s     2.06s    8.36s    70.39%
    Req/Sec    24.65      9.97    63.00     67.10%
  54256 requests in 3.00m, 122.50MB read
  Socket errors: connect 0, read 1, write 0, timeout 0
Requests/sec:    301.36
Transfer/sec:    696.77KB
```

```
sample#load_avg_1m=10.40

sample#memory_total=235.37MB
sample#memory_rss=235.35MB
sample#memory_cache=0.02MB
sample#memory_swap=0.00MB
sample#memory_pgpgin=66703pages
sample#memory_pgpgout=6449pages
```

## Summary

Elixir provides the joy and productivity of Ruby with the concurrency and fault-tolerance of Erlang. We've shown we can have the best of both worlds with Elixir and I encourage you to [get involved](https://github.com/phoenixframework/phoenix) with Phoenix. There's much work to do for Phoenix to match the robust ecosystem of Rails, but we're just getting started and have very big plans this year.

Both applications are available [on Github](https://github.com/chrismccord/phoenix_vs_rails_showdown) if want to recreate the benchmarks. We would love to see results on different hardware, particularly hardware that can put greater load on the Phoenix app.

Shoutout to [Jason Stiebs](https://twitter.com/peregrine) for his help getting the Heroku applications setup and remotely benchmarked!

---
