---
url: "https://web.archive.org/web/20201108015122id_/https://whitfin.io/easy-concurrency-locking-in-erlang-elixir/"
captured_at: "2026-11-18T11:28:04+00:00"
title: "Easy Concurrency Locking in Erlang/Elixir"
domain: "web-archive-org"
---

Out of the box, Elixir and Erlang offer a very powerful tool for serializing access to a resource via the GenServer included in [OTP](http://erlang.org/doc/man/gen_server.html) and surfaced in the Elixir [standard library](https://hexdocs.pm/elixir/GenServer.html). As a GenServer processes messages it receives both in order and synchronously, it becomes a great tool for simulating a lock pattern from other languages. If you wanted to serialize writes to a database, you could simply roll all of your database interaction into a GenServer implementation and you're done!

In the last few weeks however, I realised that there isn't much in the space of multiple processes holding a lock at the same time. An obvious use case for this is the ability to "throttle" some sort of access where a GenServer does not suffice (i.e. when you want more than one process holding a lock). Applications of such a lock include throttling HTTP requests, or controlling rates that processes are spawned, etc. Although a GenServer can be used for these purposes, it essentially limits the lock to only a single owner.

Due to needing this pattern, and to also practice my Erlang a little, I wrote a small library; [sleeplocks](https://github.com/whitfin/sleeplocks). In essence, sleeplocks is a more BEAM-friendly implementation of [spinlocking](https://en.wikipedia.org/wiki/Spinlock). At a high level, a spinlock is an attempt to gain a lock by repeatedly checking for an available lock (thus "spinning" the current thread). In sleeplocks though, the concept is similar but achieves the checking via the use of basic OTP principles such as message passing and GenServers. Rather than waste a bunch of time trying to come up with something complicated, I decided that this library should be little more than a binding around existing tools provided by OTP. There's already a perfectly good "notification" system in the way messages are passed around the VM, and there's a perfectly good "manager" abstraction with the GenServer concept. Re-using these tools reduces the surface area for potential bugs, and makes good use of tools written by people smarter than I.

### A Quick Tour

The way you interact with it is very simple; each created lock has a number of "slots" which can be populated. This is synonymous with the number of processes that can hold a lock at a given time. If a lock has 5 slots, then up to 5 processes can acquire the lock at the same time. A lock looks quite similar to other GenServers (all examples here will be in Erlang, but check out the [README](https://github.com/whitfin/sleeplocks/blob/master/README.md) for Elixir examples):

```
%% You can create a new lock using a very simple function.
sleeplocks:new(1).

%% Or you can also name your lock, to access it from anywhere.
sleeplocks:new(1, [{name, {local, my_lock}}]).
```

The number provided to `new/2` is the number of slots the lock allows; in the case above, this is a lock which will allow only a single holder at once (i.e. a Mutex). We can very easily acquire and release our lock, using a straightforward API:

```
%% Acquire a lock by name.
sleeplocks:acquire(my_lock).

%% Release a previously acquired lock.
sleeplocks:release(my_lock).
```

When we acquire a lock, we do not need to provide anything beyond the name of the lock. This is because the backing implementation makes use of the information we already have at hand in the message, such as the channel reference and the calling process identifier. If there is a slot available, the lock is acquired. If there is no slot available, the `acquire/1` call **will block until there is**. However if you wish to try to acquire a lock and fail fast, you can make use of `attempt/1` which will return `{error, unavailable}` rather than waiting. To avoid potentially forgetting to release a lock, you can also make use of `execute/2` which is quite simply a wrapper around `acquire/1` and `release/1`:

```
%% Execute this function once a lock is acquired.
sleeplocks:execute(my_lock, fun() ->
  %% Do stuff here!
end).
```

The code running inside the provided function scope is wrapped with `catch` clauses to ensure that locks are correctly removed, so even if your code crashes your lock should be correctly released before the error is raised properly. This is important to avoid slots which can't be released due to their parent process no longer existing!

### Lock Internals

For those of you already familiar with locking and message passing, this will likely appear trivial so you might want to skip this section. For others though, this might be a good example of how you can re-use OTP to create your own abstractions easily. It's also good for my memory!

When you create a lock, a backing process is spawned and linked to your current process via the use of `gen_server`. This process behaves like any other and relies on OTP messages to know what's happening with a lock. Each lock has (currently) 3 simple fields; the total number of slots, the processes currently holding references to the lock, and a queue of waiting processes trying to acquire a lock. To store the processes currently holding references to a lock, we store a map of process identifiers to a basic `ok` atom (which will be explained in a moment).

When a lock is acquired, we check to see if the number of slots is filled. This is easy as we just need to check the size of the processes map in memory. If the map isn't full, we can grant a handle to the lock. To do this we very simply have to update the processes map to contain the new process. This has a nice side effect that if a process tries to acquire a lock when it already has one, there's no way to deadlock as the entry is duplicated and thus ignored (it essentially becomes a no-op). Similarly when a lock is released, we only have to drop that entry from the processes map.

The case where the number of slots is filled is a little more complicated, but not much. Each lock contains a `queue` to dictate the processes currently waiting on a lock. When there are no slots available, we just append the calling process to this queue. Rather than reply back to the caller though, we use `noreply` so that we can reply at a later point in time (thus making the call block the calling process). At this point, nothing happens. We simply wait for a lock to be released. When a lock is released and a slot becomes available in the lock, we look for the next process in the queue. If there isn't one, we do nothing else and there's simply a spare slot in the lock for the next time someone tries to acquire it. If there **is** a process in the queue, we remove it and use the process identifier to manually reply (via `gen_server:reply`). This then unblocks that process as they now have a lock and can continue what they were doing. Of course, we then insert this process into the map tracking the processes which currently have a handle on the lock.

### Feedback

If anyone has any feedback, please do let me know. This is only the second library I've written in Erlang itself, so style pointers are also appreciated. You can find the repository (as usual) on my [GitHub](https://github.com/whitfin/sleeplocks) and it's published on [Hex](https://hex.pm/packages/sleeplocks) so you can easily use it in your projects. We're already using it for a couple of utilities at work, and it serves a small role inside [Cachex](https://github.com/whitfin/cachex) to limit access to the main state table. Touch wood, it seems solid so far!
