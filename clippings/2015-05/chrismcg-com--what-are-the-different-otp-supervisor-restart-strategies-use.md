---
url: "http://chrismcg.com/2015/04/28/what-are-the-different-otp-supervisor-restart-strategies-useful-for/"
captured_at: "2015-05-22T11:17:49-03:00"
title: "What are the different OTP supervisor restart strategies useful for? – Chris McGrath"
domain: "chrismcg-com"
---

# What are the different OTP supervisor restart strategies useful for?

28 Apr 2015

OTP Supervisors can restart their children in four different ways and to better
understand which one to use in a given scenario I wanted to summarise a few
patterns I've seen.

## One for one

You will use this strategy at least once in every OTP application. It's
how you setup supervisor hierarchies and start the different workers and
supervisors that don't need to be pooled or started dynamically.

## Simple one for one

You use this when you need to create and supervise processes of the same type.
You can create a pool of processes when the supervisor starts or have them
created when something happens. e.g. accepting a new tcp connection.

You can see this in action in
the cache in [phl.ink](http://phl.ink/), a simple
[Phoenix](http://www.phoenixframework.com/) url shortener I made.

```
defmodule Phlink.Cache.UrlCacheSupervisor 
   Supervisor

   start_link 
    Supervisorstart_link__MODULE__   __MODULE__
  

   start_child 
    Supervisorstart_child__MODULE__ 
  

    
    children  
      workerPhlink.Cache.UrlCache 
    

    supervisechildren strategy :simple_one_for_one
```

[(source)](https://github.com/chrismcg/phlink/blob/master/lib/phlink/cache/url_cache_supervisor.ex)

The `children` list in the `init/1` function is a template for the child
processes to create. The supervisor won't actually start any children until you
tell it to. When the
[`Mapper`](https://github.com/chrismcg/phlink/blob/master/lib/phlink/cache/mapper.ex)
process needs to cache the url associated with a short code it calls
`start_child(url)` which returns the pid of the started process. The `Mapper`
stores this pid in a dictionary so it can avoid a db lookup next time the
shortcode is requested.

`:simple_one_for_one` and `:one_for_one` are the most common strategies used.

## Rest for one

This is the strategy to use when processes have one way dependencies. An
example would be an chain of processes providing data to each other in a
pipeline. If you had five processes in the chain and the first one died the
rest that depend on it must be restarted. If the third one dies you only need
to restart the fourth and fifth, the first two can continue.

Another example of this would be a a registry process that maps some external
input to the PID of the process that handles it.

```
defmodule Phlink.Cache.Supervisor 
   Supervisor

   start_link 
    Supervisorstart_link__MODULE__ 
  

    
    children  
      workerPhlink.Cache.Mapper 
      supervisorPhlink.Cache.UrlCacheSupervisor 
    

    supervisechildren strategy :rest_for_one
```

[(source)](https://github.com/chrismcg/phlink/blob/master/lib/phlink/cache/supervisor.ex)

If the `Mapper` process dies then there's no way to get at the processes it was
mapping too so `:rest_for_one` will terminate the supervisor which will
terminate the children caching the urls.

## One for all

This is the strategy to use when you start several processes that depend on
each other to get the work done. An example of this would be a sync process
that talks to another node. When a new node is added you'd start sending and
receiving processes locally to handle the two way synchronisation. If either
the sender or receiver died you could bring everything back to a known state
by using this strategy and having the supervisor restart both.

There's an example of this in [Riak Core](https://github.com/basho/riak_core).

```
  ->
     one_for_all
         CHILDriak_core_handoff_receiver_supsupervisor
          CHILDriak_core_handoff_sender_supsupervisor
          CHILDriak_core_handoff_listener_supsupervisor
          CHILDriak_core_handoff_managerworker
```

[(source)](https://github.com/basho/riak_core/blob/master/src/riak_core_handoff_sup.erl)

## Summary

The four restart strategies in OTP have different use cases and give you a lot
of power in deciding how to structure your app and handle failure. You'll
mostly use `:one_for_one` and `:simple_one_for_one`, occasionally
`:rest_for_one`, and rarely `:one_for_all`.

#### When to use `one_for_one`

- You know which child processes are going to exist
- You're setting up supervisor hierarchy
- None of the child processes depend on each other

#### When to use `simple_one_for_one`

- You want a factory for processes of the same type

You could have `start_child` guard against too many children but it's worth
considering something like [poolboy](https://github.com/devinus/poolboy) for
that.

Be careful about creating a "galloping herd" if you have many children
that do something when they are terminated by the supervisor.

#### When to use `rest_for_one`

- You have a registry process that maps incoming terms to a pid
- You have a pipeline of processes that depend on each others output

#### When to use `one_for_all`

- You have related process that depend on each other where failure of one means
  the rest need to be terminated.

Seen any other patterns in the wild? Add them to the comments as I'd like to
hear about ones I haven't seen yet!

If you've some thoughts on what's above please leave a comment or tweet me [@chrismcg](https://twitter.com/chrismcg). I would love to hear from you.
