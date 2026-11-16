---
url: "https://web.archive.org/web/20201108121502id_/http://learningelixir.joekain.com/using-gen-stage-to-notify-a-channel/"
captured_at: "2026-11-16T08:13:09+00:00"
title: "Using GenStage to Notify a Phoenix Channel of Updates in Elixir"
domain: "web-archive-org"
---

Last week I [learned about `GenStage`](https://web.archive.org/gen-stage/) by reading the [announcement](http://elixir-lang.org/blog/2016/07/14/announcing-genstage/) . It was a good introduction, but now I’m ready to get my hands dirty and write some `GenStage` code myself. From the previous post I built up a TODO list of things to try:

1.  Watch the ElixirConf 2016 Keynote
2.  Use `GenStage` to notify a Phoenix Channel of new events.
3.  Experiment with `Flow`
4.  Rewrite Domain Scrapper to use `GenStage`.

I’ve watched the Keynote, so let’s dive into 2.

## Use GenStage to Notify a Phoenix Channel of new events.

This post will follow in the footsteps of [Using GenEvent to Notify a Channel of Updates in Elixir](https://web.archive.org/using-genevent-to-notify-a-channel/).

In the post using `GenEvent`, we had a channel that we were using to broadcast changes to a model to all web clients. But, we wanted to decouple the controller that was performing updates to the model and the channel. The thought being that we would use an observer pattern to communicate changes. There could be many observers to the changes in addition to the channel and the controller shouldn’t have to be aware of any of them.

I have a [play channel project in github](https://github.com/joekain/play_channel). I went back and created a branch called pre-gen-event and will begin work from there.

First, I need to insure that I can still build everything. There are some warnings in the deps. These are because the deps are old but I’ve upgraded to Elixir 1.3.2. I don’t want to update Phoenix yet so I’m going to live with the warnings for now.

There is one warning in my code:

```
warning: variable payload is unused
  web/channels/toy_channel.ex:4
```

This is easy enough to fix by renaming `payload` to `_payload` in the argument list to `join/3`.

At this point the project compiles and all the tests pass.

To get started with our GenStage changes, we’ll have to add `Experimental.GenStage` to our dependencies in mix.exs by adding a line like this to `deps`:

```
{:gen_stage, "~> 0.5"}]
```

Then, I’ll add `alias Experimental.GenStage` to the top of toy\_channel.ex and I’ll add `use GenStage` just after `use PlayChannel.Web, :channel` at the begining of the module.

These changes trigger a few warnings:

```
warning: undefined behaviour function init/1 (for behaviour Experimental.GenStage)
web/channels/toy_channel.ex:3

warning: conflicting behaviours - callback code_change/3 required by both ''Elixir.Phoenix.Channel'' and ''Elixir.Experimental.GenStage'' (line 3)
web/channels/toy_channel.ex:3

warning: conflicting behaviours - callback handle_info/2 required by both ''Elixir.Phoenix.Channel'' and ''Elixir.Experimental.GenStage'' (line 3)
web/channels/toy_channel.ex:3

warning: conflicting behaviours - callback terminate/2 required by both ''Elixir.Phoenix.Channel'' and ''Elixir.Experimental.GenStage'' (line 3)
web/channels/toy_channel.ex:3
```

The tests still pass but I’m worried about these warnings. There are two types. Here’s the first:

```
warning: undefined behaviour function init/1 (for behaviour Experimental.GenStage)
```

This is a good warning and we can deal with it. I just haven’t implemented GenStage’s required `init/1` function. Once we add the function it should address the warning. We’re left with:

```
warning: conflicting behaviours - callback code_change/3 required by both ''Elixir.Phoenix.Channel'' and ''Elixir.Experimental.GenStage'' (line 3)

warning: conflicting behaviours - callback handle_info/2 required by both ''Elixir.Phoenix.Channel'' and ''Elixir.Experimental.GenStage'' (line 3)
web/channels/toy_channel.ex:3

warning: conflicting behaviours - callback terminate/2 required by both ''Elixir.Phoenix.Channel'' and ''Elixir.Experimental.GenStage'' (line 3)
web/channels/toy_channel.ex:3
```

For these three, we had similar warning when adding GenEvent to the channel. And again, these are the OTP compliant callbacks and will have the same purpose for both `GenStage` and `Phoenix.Channel`. So I think we’re ok to proceed here.

Well, with that out of the way let’s go ahead and implement the `init/1` function. To do this, we need to decide if `PlayChannel.ToyChannel` is a `GenStage` producer or consumer.

Our goal here is to use GenStage “to Notify a Channel of Updates”. That means that

*   a change will original in the controller
*   there is a notification center to broadcast an event about the change
*   `PlayChannel.ToyChannel` receives the event and sends the payload over the channel.

This means the notification center will be the event producer and `PlayChannel.ToyChannel` will be the consumer.

Now we can write the `init/1` function and intialize as a consumer. Here’s the function we need:

```
  # GenStage callbacks
  def init(_) do
    {:consumer, nil}
  end
```

Our `init/1` needs no arguments and no state. It only need to return that it will behave as a `GenStage` `:consumer`.

At this point the tests still pass. However, we need to add a `handle_events/3` function in order to receive events from our notification center. I think this should do it:

```
def handle_events(events, _from, _state) do
  Enum.each events, fn
    {:update, toy} -> PlayChannel.ToyChannel.broadcast_change(toy)
  end

  {:noreply, [], nil}
end
```

This is similar to what we wrote for `GenEvent`:

```
def handle_event({:update, toy}, _) do
  PlayChannel.ToyChannel.broadcast_change(toy)
  {:ok, nil}
end
```

Except that `GenStage.handle_events/3` accepts a list of events. To process the list we use `Enum.each` and broadcast each update on the channel. `handle_events` returns no events (it’s a consumer) and needs no state.

## Build the GenStage Producer

Next, we need to create the producer. We’ll call it `PlayChannel.Toy.UpdateEventHandler` (this is the same name we used in the GenEvent version). We’ll start with

```
alias Experimental.GenStage

defmodule PlayChannel.Toy.UpdateEventHandler do
  use GenStage
end
```

There’s actually a great example of what we need in the [GenStage annoucement](http://elixir-lang.org/blog/2016/07/14/announcing-genstage/)

```
alias Experimental.GenStage

defmodule PlayChannel.Toy.UpdateEventHandler do
	use GenStage

  def start_link() do
    GenStage.start_link(__MODULE__, :ok, name: __MODULE__)
  end

  def sync_notify(event, timeout \\ 5000) do
    GenStage.call(__MODULE__, {:notify, event}, timeout)
  end

  ## Callbacks

  def init(:ok) do
    {:producer, {:queue.new, 0}, dispatcher: GenStage.BroadcastDispatcher}
  end

  def handle_call({:notify, event}, from, {queue, demand}) do
    dispatch_events(:queue.in({from, event}, queue), demand, [])
  end

  def handle_demand(incoming_demand, {queue, demand}) do
    dispatch_events(queue, incoming_demand + demand, [])
  end

  defp dispatch_events(queue, demand, events) do
    with d when d > 0 <- demand,
         {item, queue} = :queue.out(queue),
         {:value, {from, event}} <- item do
      GenStage.reply(from, :ok)
      dispatch_events(queue, demand - 1, [event | events])
    else
      _ -> {:noreply, Enum.reverse(events), {queue, demand}}
    end
  end
end
```

Let’s go over this.

First there is the `start_link` function. This will be used to start and name the GenStage.

Next, `sync_notify`. This is the function that our controller will call to notify observers that an update has been made. It uses `GenStage.call` to send the update event to the GenStage server.

Next come the callbacks, the first is `init`. This initializes the GenStage as a producer and sets a custom dispatch. `GenStage.BroadcastDispatcher` is describe in the documentation as:

> A dispatcher that accumulates demand from all consumers before broadcasting events to all of them

This is the behavior we need for an notification center. Finally, we set up a state for the stage. Out state is a queue, and a demand. The initial queue is created with `:queue.new`. This queue will hold events waiting to be broadcast. The initial demand is 0.

At the end of the module is a function, `dispatch_events` which is used to implement both `handle_call` and `handle_demand`.

Let’s think first about `handle_demand`. There are two cases to consider First, there are events in the queue ready to be returned. In this case we can just return them in `handle_demand`. Second, the queue is empty. In this case we can’t return a result to the consumer, we have to defer it’s return until there is an event.

The next callback is `handle_call/3` This is just like `GenServer`’s `handle_call` and will receive the messages sent by our `sync_notify` function.

Next is `handle_demand/2` which is the GenStage callback for a producer to provide more events. This calls `dispatch_events` which is an interesting function. It recursively calls itself and for each element in queue up to the demand. For each recursive call it calls `GenStage.reply/2`. This is the reply back to the `call` for `{:notfy event}`

I’m actually having a hard time understanding and explaining this code. I think I’ll try writing my own version.

## Building a GenStage producer for Event Notification

I want to TDD a solution for `UpdateEventHandler`. I had one false start trying to write this up and ended up with tests like this:

```
alias Experimental.GenStage

defmodule PlayChannel.Toy.UpdateEventHandlerTest do
  use ExUnit.Case, async: true

  alias PlayChannel.Toy.UpdateEventHandler

  test "it can init" do
    UpdateEventHandler.init(nil)
  end

  test "it is a producer" do
    result = UpdateEventHandler.init(nil)
    assert elem(result, 0) == :producer
  end

  test "it should start_link" do
    {:ok, stage} = UpdateEventHandler.start_link()
    GenStage.stop(stage)
  end

  test "it should accept events" do
    {:ok, stage} = UpdateEventHandler.start_link()
    UpdateEventHandler.notify(stage, "Hi")
    GenStage.stop(stage)
  end

  test "it should broadcast the events" do
    assert false
  end
end
```

As I wrote more and more tests, I started to think that this is too tied to my implementation. Yes, I want to use `GenStage`. And in fact I’m writing a blog post about `GenStage`. But should my tests really require that? The fact that I’ll use `GenStage` is a implementation detail and the tests should really only test the externally visible behavior, right? I’m throwing these tests away and starting over. I’ll focus on the behaviors.

That said, I do have a `GenStage` in `PlayChannel.ToyChannel` (the observer) and it will need to subscribe the the `UpdateEventHandler`. But that’s the only `GenStage` detail that I should depend on.

I’ll start with this test:

```
test "it should start_link and stop" do
  {:ok, pid} = UpdateEventHandler.start_link()
  UpdateEventHandler.stop(pid)
end
```

This is adapated from test tests I had before, but I’ve created a new `UpdateEventHandler.stop/1` interface. This is nice, it abstracts me away from `GenStage.stop/1`.

Here’s an implementation that passes the tests:

```
alias Experimental.GenStage

defmodule PlayChannel.Toy.UpdateEventHandler do
  use GenStage

  def start_link(), do: GenStage.start_link(__MODULE__, nil)
  def stop(stage), do: GenStage.stop(stage)

  # Callbacks
  def init(_), do:  {:producer, nil}
end
```

Now, I could have written a simpler implementation that passed the tests. But I’m going to go ahead and write this as a `GenStage` because I know I’ll need to.

The next test I’ll add is:

```
test "it should accept events" do
  {:ok, pid} = UpdateEventHandler.start_link()
  UpdateEventHandler.notify(pid, "Hi")
  UpdateEventHandler.stop(pid)
end
```

which requires that I have a `notify` function. This is part of the behavior I want in my module. I want callers to be able to notify all observers of an event.

Here’s a very simple implementation that passes:

```
def notify(handler, event) do
end
```

I should also note that I get a few warnings when compiling:

```
warning: variable event is unused
  lib/play_channel/toy/update_event_handler.ex:9

warning: variable handler is unused
  lib/play_channel/toy/update_event_handler.ex:9
```

I could easily fix these, but I keep them as a reminder that `notify` is imcomplete, I’m not actually notifying anything yet.

The next behavior that I want to test for is that I can subscribe a `GenStage` consumer to the UpdateEventHandler. This test requires that I setup such a consumer. Here’s my shot at it:

```
defmodule TestObserver do
  use GenStage

  def init(_), do: {:consumer, nil}
  def handle_events(events, _, state) do
    {:noreply, [], state}
  end
end


test "an observer can subscribe to it" do
  {:ok, observer} = GenStage.start_link(TestObserver, nil)
  {:ok, updater} = UpdateEventHandler.start_link()
  GenStage.sync_subscribe(observer, to: updater)

  UpdateEventHandler.stop(updater)
  GenStage.stop(observer)
end
```

Adding `TestObserver` is kind of a lot of code to write for a test. But I’ve tried to keep it as simple as possible. When I run this test I get:

```
1) test an observer can subscribe to it (PlayChannel.Toy.UpdateEventHandlerTest)
   test/update_event_handler_test.exs:32
   ** (EXIT from #PID<0.256.0>) an exception was raised:
       ** (UndefinedFunctionError) function PlayChannel.Toy.UpdateEventHandler.handle_demand/2 is undefined or private.
```

This means that I need to add the `handle_demand/2` callback. Let’s do it:

```
  def handle_demand(demand, state) do
    {:noreply, [], state}
  end
```

This doesn’t do anything yet. When I run the test it still fails, now with this error:

```
1) test an observer can subscribe to it (PlayChannel.Toy.UpdateEventHandlerTest)
   test/update_event_handler_test.exs:32
   ** (exit) no process
   stacktrace:
     (stdlib) proc_lib.erl:794: :proc_lib.stop/3
     test/update_event_handler_test.exs:38: (test)
```

Line 38, in the test, coresponds to the call to `GenStage.stop(observer)`. I guess that when I stop `updater` the subscribed consumers must also shutdown. So I can just remove the call.

With this change the test passes.

Next, I want to write a test that calls notify on `updater` then verifies that `observer` sees the event. To do this I’m going to need to add something to `TestObserer` to allow me to verify what it observes. I’ll do this before writing any new tests. I think this should do it:

```
   defmodule TestObserver do
     use GenStage

-    def init(_), do: {:consumer, nil}
+    def init(_), do: {:consumer, []}
     def handle_events(events, _, state) do
-      {:noreply, [], state}
+      {:noreply, [], state ++ events}
     end
+
+    def get(stage), do: GenStage.call(stage, :get)
+    def handle_call(:get, _, state), do: {:reply, state, [], state}
   end
```

Here I’ve added an interface `get/1` which is procesed by `handle_call/3`. The get functionality returns the state of the `TestObserver`. I’ve also updated `handle_events` to just accumulate events into the state. That is, `TestObserver` collects its events and returns them when you call `get`.

After making this change I reran the existing tests to make sure I didn’t break `TestObserver`. All was good.

Next, I wrote this test which uses the new `get` function:

```
test "a subscribed observer is notified of all events" do
  {:ok, observer} = GenStage.start_link(TestObserver, nil)
  {:ok, updater} = UpdateEventHandler.start_link()
  GenStage.sync_subscribe(observer, to: updater)

  UpdateEventHandler.notify(updater, "Hi")

  assert TestObserver.get(observer) == ["Hi"]

  UpdateEventHandler.stop(updater)
end
```

This is very similar to the previous test except that we’ve added the assert:

```
assert TestObserver.get(observer) == ["Hi"]
```

This uses the new `get` function to retrieve any observed events. And we expect to get the single event “Hi” because that’s the event we notified to the updater.

We can make this new test pass by updating `handle_call`:

```
def handle_call({:notify, event}, _from, state) do
  {:reply, :ok, [event], state}
end
```

This version declares `[event]` as available events, ready to be dispatched. The `GenStage` logic will see to it that these events are stored in an internal buffer and dispatched when there is demand.

After writing this I found that the documentation has an example that uses almost the same exact code as I have just written! And it goes on to describe the reason for the more complex version.

The motivation for a more complex implementation is that unserved demand is being held in `GenStage`’s internal buffer. Unserved demand refers to events that have arrived through the `notify` function but have not yet been delivered to subscribers through the `handle_demand` function. If this internal buffer becomes too full a log message will be emitted. A better solution is to manage a queue within our code to hold all the pending events.

Let’s try adding a queue to our version. There’s no test that should motivate this change as the externally visible behavior stays the same.

Our `UpdateEventHandler` will need state. Let’s think for a minute what this state is:

*   A queue to hold incoming events. This queue fills up when the rate of incoming events exceeds the demand.
*   Unfilled demand. This can be a simple counter that records demand that we haven’t been able to fill because the demand exceeds the suppy of events.

Let’s put this together. First, in `init` we have to intialize our state. We need an empty queue and 0 for outstanding demand.

```
def init(_), do:  {:producer, {:queue.new, 0}}
```

With this change the tests still pass.

Now, in `handle_call` we accept new events. There are two cases to deal with

1.  There is no outstanding demand, so we put the new event in our queue.
2.  There is outstanding demand, so we forward the new event on immediately.

```
def handle_call({:notify, event}, _from, {queue, 0}) do
  queue = :queue.in(event, queue)
  {:reply, :ok, [], {queue, 0}}
end

def handle_call({:notify, event}, _from, {queue, demand}) do
  queue = :queue.in(event, queue)
  { {:value, event}, queue} = :queue.out(queue)
  {:reply, :ok, [event], {queue, demand - 1}}
end
```

Here, we handle the two cases using two separate function clauses. The first, handles the case where there is no outstanding demand (demand is 0).

The second function clause handles the case where there is demand. It inserts the event at the rear of the queue and then pops off an event from the head of the queue and returns it.

Do I need to handle the case that `demand > 1` and the queue is not empty in `handle_call`? If so, it means that I should return more than one event. But, if there is demand and there were events waiting why were they not already dispatched? This is something to look into a little later.

Also, our tests fail after this change:

```
1) test a subscribed observer is notified of all events (PlayChannel.Toy.UpdateEventHandlerTest)
   test/update_event_handler_test.exs:39
   Assertion with == failed
   code: TestObserver.get(observer) == ["Hi"]
   lhs:  []
   rhs:  ["Hi"]
   stacktrace:
     test/update_event_handler_test.exs:46: (test)
```

Ok, this failure makes sense because we’re never increasing the demand stored in our state. So we always use the first case (demand is 0) and never return the events.

To fix this, we need to update `handle_demand`. Again, there are two cases.

1.  There are waiting events in the queue. In this case satisfy the demand from the queue.
2.  There are no waiting events in the queue. In this case save the demand in the state.

Here’s an implementation

```
def handle_demand(demand, {queue, old_demand}) do
  {events, new_queue, new_demand} = take(queue, demand + old_demand)
  {:noreply, events, {queue, new_demand}}
end

defp take(queue, count, items \\ [])
defp take(queue, 0, items), do: {items, queue, 0}
defp take(queue, count, items) do
  case :queue.out(queue) do
    { {:value, item}, queue} -> take(queue, count - 1, items ++ [item])
    {:empty, queue} -> {items, queue, count}
  end
end
```

I’ve introduced the function `take` to take multiple items out of the queue. It’s a simple recursive function though it would be nice to have tests for it. It returns a tuple of the taken events, a new queue with the remaining events, and the remaining demand.

With this change the tests (the ones we already had) pass.

An interesting thing to note is that we could apply `take` in `handle_call` to deal with the case of `demand > 1` and queue not empty that I asked about earlier. It would look something like this:

```
def handle_call({:notify, event}, _from, {queue, demand}) do
  queue = :queue.in(event, queue)
  {events, new_queue, new_demand} = take(queue, demand)
  {:reply, :ok, events, {new_queue, new_demand}}
end
```

I guess there is no reason not to use this version.

Here’s the whole module:

```
alias Experimental.GenStage

defmodule PlayChannel.Toy.UpdateEventHandler do
  use GenStage

  def start_link(), do: GenStage.start_link(__MODULE__, nil)
  def stop(stage), do: GenStage.stop(stage)

  def notify(handler, event) do
    GenStage.call(handler, {:notify, event})
  end

  # Callbacks
  def init(_), do:  {:producer, {:queue.new, 0}}

  def handle_demand(demand, {queue, old_demand}) do
    {events, new_queue, new_demand} = take(queue, demand + old_demand)
    {:noreply, events, {new_queue, new_demand}}
  end

  defp take(queue, count, items \\ [])
  defp take(queue, 0, items), do: {items, queue, 0}
  defp take(queue, count, items) do
    case :queue.out(queue) do
      { {:value, item}, queue} -> take(queue, count - 1, items ++ [item])
      {:empty, queue} -> {items, queue, count}
    end
  end

  def handle_call({:notify, event}, _from, {queue, demand}) do
    queue = :queue.in(event, queue)
    {events, new_queue, new_demand} = take(queue, demand)
    {:reply, :ok, events, {new_queue, new_demand}}
  end
end
```

This is now pretty close to `QueueBroadcaster` in the `GenStage` docs. The difference is that I opted for the abstraction of `take` which is inspired by `Enum.take/2`.

`QueueBroadcaster` does the same thing but combines extracting items from the queue with building up the return values for `handle_demand` and `handle_call` in the `dispatch_events` function.

Conceptually, I find my version a little easier to read because `handle_demand` and `handle_call` build their own return values. This way `take` just focuses on the single tasks of extracting items from the queue.

That said, there are a couple of things that `QueueBroadcaster` does better than `UpdateEventHandler`

1.  `dispatch_events` has an optimization in building up the lists. It uses `[event | events]` where `take` has `items ++ [item]`. Inserting at the head of the list is more efficient. `dispatch_events` then reverse the list before returning the final result.
    
2.  `dispatch_events` uses `:noreply` in `handle_call` if the value isn’t being sent to the observers immediately. Then, when the event is finally consumed it uses `GenStage.reply/2` to send the reply. This keeps the caller from going on until the notification is delivered.
    

I think point number 2 is really important and I need that functionality as well. And I think this is what necessitates `dispatch_events` being as complex as it is.

Give this, I think it makes sense to use the `QueueBroadcaster` implementation. But working through this implementation has given me a much better understanding of what’s going on.

Also, there is one more thing we should have done with `UpdateEventHandler`. We needed to write a test for multiple subscribers. And this would have revealed that we needed to change our init function to use the `BroadcastDispatcher` as `QueueBroadcaster` does. This would like this:

```
def init(_), do:  {:producer, {:queue.new, 0},
                   dispatcher: GenStage.BroadcastDispatcher}
```

## Using QueueBroadcaster

I’ll switch over to the implementaiton from `QueueBroadcaster` but in doing so I’ll need to remove this test:

```
test "it should accept events" do
  {:ok, pid} = UpdateEventHandler.start_link()
  UpdateEventHandler.notify(pid, "Hi")
  UpdateEventHandler.stop(pid)
end
```

Here `notify` waits for the event to be accepted by the subscribers. As this test sets up no subscribers it ends up timing out. This is no longer a suported behavior and it wasn’t a behavior that was important to me anyway. So I can remove the test. The behavior or accepting events and delivering them to subscribers is already tested in this test:

```
test "a subscribed observer is notified of all events" do
  {:ok, observer} = GenStage.start_link(TestObserver, nil)
  {:ok, updater} = UpdateEventHandler.start_link()
  GenStage.sync_subscribe(observer, to: updater)

  UpdateEventHandler.notify(updater, "Hi")

  assert TestObserver.get(observer) == ["Hi"]

  UpdateEventHandler.stop(updater)
end
```

My final version looks like this:

```
alias Experimental.GenStage

defmodule PlayChannel.Toy.UpdateEventHandler do
  use GenStage

  def start_link(), do: GenStage.start_link(__MODULE__, :ok)
  def stop(stage), do: GenStage.stop(stage)

  def notify(handler, event) do
    GenStage.call(handler, {:notify, event})
  end

  ## Callbacks

  def init(:ok) do
    {:producer, {:queue.new, 0}, dispatcher: GenStage.BroadcastDispatcher}
  end

  def handle_call({:notify, event}, from, {queue, demand}) do
    dispatch_events(:queue.in({from, event}, queue), demand, [])
  end

  def handle_demand(incoming_demand, {queue, demand}) do
    dispatch_events(queue, incoming_demand + demand, [])
  end

  defp dispatch_events(queue, demand, events) do
    with d when d > 0 <- demand,
    {item, queue} = :queue.out(queue),
    {:value, {from, event}} <- item do
      GenStage.reply(from, :ok)
      dispatch_events(queue, demand - 1, [event | events])
    else
      _ -> {:noreply, Enum.reverse(events), {queue, demand}}
    end
  end
end
```

I’ve maintained my `stop` and `notify` functions. Also, I haven’t named my server after the module. I expect to be able to have many instances of it.

Now, the last step is to actually call our `UpdateEventHandler` to make an update. We do this from the controller like this:

```
@@ -2,6 +2,7 @@ defmodule PlayChannel.ToyController do
   use PlayChannel.Web, :controller

   alias PlayChannel.Toy
+  alias PlayChannel.Toy.UpdateEventHandler

   plug :scrub_params, "toy" when action in [:create, :update]

@@ -45,7 +46,9 @@ defmodule PlayChannel.ToyController do

     case Repo.update(changeset) do
       {:ok, toy} ->
-        PlayChannel.ToyChannel.broadcast_change(toy)
+        UpdateEventHandler.notify(:toy_event_manager, {:update, toy})

         conn
         |> put_flash(:info, "Toy updated successfully.")
```

Well, wait, that isn’t quite right. I’ve adapted this from the GenEvent version but in this case what’s `:toy_event_manager`?

I guess I do need to name my `GenStage`. Se we need to:

1.  Start an `UpdateEventHandler` in our supervision tree.
2.  Add support for naming `UpdateEventHandler` instances.
3.  Name our instance `:toy_event_manager`
4.  Register the channel with the `UpdateEventHandler`

Let’s start with a test for naming first.

```
test "an updater can be referenced by name" do
  {:ok, observer} = GenStage.start_link(TestObserver, nil)
  {:ok, _} = UpdateEventHandler.start_link(name: :a_name)
  GenStage.sync_subscribe(observer, to: :a_name)

  UpdateEventHandler.notify(:a_name, "Hi")

  assert TestObserver.get(observer) == ["Hi"]

  UpdateEventHandler.stop(updater)
end
```

The implementation is easy enough. We’ll just allow any options accepted by `GenStage.startlink`:

```
@@ -3,7 +3,7 @@ alias Experimental.GenStage
 defmodule PlayChannel.Toy.UpdateEventHandler do
   use GenStage

-  def start_link(), do: GenStage.start_link(__MODULE__, :ok)
+  def start_link(opts \\ []), do: GenStage.start_link(__MODULE__, :ok, opts)
   def stop(stage), do: GenStage.stop(stage)

   def notify(handler, event) do
```

and the tests pass. Now we just need to start an `UpdateEventHandler` in our supervision tree like this:

```
@@ -1,5 +1,6 @@
defmodule PlayChannel do
use Application
+  alias PlayChannel.Toy.UpdateEventHandler

# See http://elixir-lang.org/docs/stable/elixir/Application.html
# for more information on OTP Applications
@@ -13,6 +14,7 @@ defmodule PlayChannel do
supervisor(PlayChannel.Repo, []),
# Here you could define other workers and supervisors as children
# worker(PlayChannel.Worker, [arg1, arg2, arg3]),
+      worker(UpdateEventHandler, [[name: :toy_event_manager]])
]

# See http://elixir-lang.org/docs/stable/elixir/Supervisor.html
```

## What am I doing?

Ugh, I think I’m totally lost here. In the GenEvent case, `UpdateEventHandler` was actually a separate GenServer, not part of the channel. And `GenEvent` played the role of the notification server. I need something like this again. I really should have reivewed the old post better. (And honestly, I think I made this same mistake with `GenEvent`)

Ok, we can fix this. I rename `UpdateEventHandler` to `NotificationCenter` which feels good. I like that name better.

Then, I extract what I’d written in the channel into a separate `GenStage`. And it is this new actor that should be named `UpdateEventHandler`. It looks like this:

```
alias Experimental.GenStage

defmodule PlayChannel.Toy.UpdateEventHandler do
  use GenStage

  def start_link(opts \\ []), do: GenStage.start_link(__MODULE__, :ok, opts)
  def stop(stage), do: GenStage.stop(stage)

  # Callbacks
  def init(_) do
    {:consumer, nil, subscribe_to: [:toy_notifcation_center]}
  end

  def handle_events(events, _from, _state) do
    Enum.each events, fn
      {:update, toy} -> PlayChannel.ToyChannel.broadcast_change(toy)
    end

    {:noreply, [], nil}
  end
end
```

There’s also one change that I’ve added here which I’ve taken from the `GenStage` announcment. The `init` function now uses `subscribe_to: [:toy_notifcation_center` to automatically subscribe to the notification center. `:toy_notifcation_center` is the name I setup for that notification center when setting up my supervisor, like this:

```
worker(NotificationCenter, [[name: :toy_notifcation_center]]),
worker(UpdateEventHandler, [[name: :toy_event_manager]])
```

The `subscribe_to` functionality in `GenStage` is nice in that I don’t have to write extra code after the supervisor is started to build up the connections.

And now it works!

## Conclusion

Well, that was quite a long post. Part of the length came from a few mistakes I made along the way but I know I learned something from them and I hope you can too.

It was good to explore using `GenStage` in an observer pattern and as a replacement for `GenEvent`. It felt like a lot of code to write though I guesss I went though several iterations with `QueueBroadcaster` / `NotificationCenter`. If I needed to do this again elsewhere the understanding I came to here would allow me to move a lot faster.

One thing I found really interesting is that some of the work involved in managing the queue in `NotificationCenter` reminded me of the `BlockingQueue` that I wrote a long time back in [Blocking Queue](https://web.archive.org/blocking-queue/). And the `BlockingQueue` is something I’ve used in many posts to solve similar problems to those solved by `GenStage`. Though I think in the `GenStage` model, the queue is primarily used up front at the producer stage and supply/demand between consumer stages is managed by the demand system build into `GenStage`.

Coming up in future posts, we still have a few items left on our `GenStage` TODO list:

1.  Experiment with `Flow`
2.  Rewrite Domain Scrapper to use `GenStage`.

Next week I hope to learn more about `Flow`. I hope you’ll join me.

* * *
