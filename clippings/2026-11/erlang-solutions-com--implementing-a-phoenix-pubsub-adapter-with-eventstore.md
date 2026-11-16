---
url: "https://erlang-solutions.com/blog/how-to-write-a-phoenix-pubsub-adapter-tutorial-example-based-on-eventstore.html"
captured_at: "2026-11-16T03:46:47+00:00"
title: "Implementing a Phoenix PubSub Adapter with EventStore"
domain: "erlang-solutions-com"
---

Distributed systems need async message delivery across nodes. Phoenix provides [Phoenix PubSub](https://hexdocs.pm/phoenix_pubsub/Phoenix.PubSub.html) for this, with pluggable adapters for different backends — officially PG2 and Redis.

This post walks through implementing a Phoenix PubSub adapter backed by [EventStore](https://hexdocs.pm/eventstore/EventStore.html), an Elixir event sourcing library that persists events to PostgreSQL as an append-only log.

Using EventStore as a PubSub backend has a few advantages over the default PG2 adapter:

*   **No Erlang distribution required**: nodes communicate through the shared database rather than through the Erlang cluster, so you can run multiple nodes without configuring Erlang node connectivity.
*   **Persistence**: every broadcast is stored and can be replayed or audited later.

The tradeoffs are the need for storage and the additional latency of a database round-trip per broadcast, making it best suited for lower-throughput messaging where persistence and cross-node decoupling matter more than raw speed. This implementation is a proof of concept — no load tests were performed.  

A full implementation of the adapter can be found [on Github](https://github.com/esl/phoenix_pubsub_eventstore).  

## Phoenix.PubSub.Adapter in a nutshell

A Phoenix PubSub adapter must implement a few callbacks specified in `[Phoenix.PubSub.Adapter](https://phoenix-pubsub.hexdocs.pm/Phoenix.PubSub.Adapter.html):`

node\_name(adapter\_name)

Returns the node name as an atom or binary. Used mainly by `Phoenix.Tracker.` In most cases:

def node\_name(nil), do: node()
def node\_name(configured\_name), do: configured\_name

child\_spec(keyword)

Generates the child spec for the adapter. GenServer provides a default; this rarely needs overriding.

broadcast(adapter\_name, topic, message, dispatcher)

Called when a message is broadcast through `Phoenix.PubSub.broadcast`. The `adapter_name` is the PubSub name with `.Adapter` appended (e.g. `MyApp.PubSub → MyApp.PubSub.Adapter`). The `dispatcher` module handles local delivery via `dispatch/3`.

direct\_broadcast(adapter\_name, node\_name, topic, message, dispatcher)

Same as `broadcast/4` with an additional `node_name` — the message should only reach subscribers on that node.

This section walks through a possible implementation of a Phoenix PubSub adapter that uses EventStore to distribute messages between nodes. This gives a solution that does not depend on Erlang/Elixir distribution, and an event log is stored in case further analysis is needed.

### How Phoenix.PubSub works

  
Phoenix.PubSub uses Elixir’s [Registry](https://hexdocs.pm/elixir/Registry.html) for subscriptions — each `subscribe` call registers an entry under the topic key. When `broadcast` is called, the framework invokes the adapter callback to distribute the message, then handles local dispatch.

The adapter’s job is to get the message to other nodes. For `direct_broadcast`, only subscribers on the target node should receive it.

## The implementation

The adapter is a GenServer that joins the PubSub supervision tree. An `eventstore` option selects which EventStore module to use (in case you have multiple):

{Phoenix.PubSub,
  \[name: MyApp.PubSub,
   adapter: Phoenix.PubSub.EventStore,
   eventstore: MyApp.EventStore\]
}

The GenServer stores the EventStore module and the PubSub name in state — both are needed later:

defmodule Phoenix.PubSub.EventStore do
  @behaviour Phoenix.PubSub.Adapter
  use GenServer

  def start\_link(opts) do
    GenServer.start\_link(\_\_MODULE\_\_, opts, name: opts\[:adapter\_name\])
  end

  def init(opts) do
    {:ok,
     %{
       eventstore: opts\[:eventstore\],
       pubsub\_name: opts\[:name\]
     }}
  end
  #... implementation will come here ...#
end

Note the difference between `opts[:name]` and `opts[:adapter_name]`. The former is the name of the PubSub as a whole and is reserved for the Registry. Publishers use it when broadcasting messages. `opts[:adapter_name]` can be used as the name of the GenServer.

## Distributing a message as an event

The GenServer appends a new event to the EventStore when `broadcast` is called:

def broadcast(server, topic, message, dispatcher, metadata \\\\ %{}) do
  metadata \= Map.put(metadata, :dispatcher, dispatcher)
  GenServer.call(server, {:broadcast, topic, message, metadata})
end

def handle\_call(
      {:broadcast, topic, message, metadata},
      \_from\_pid,
      %{id: id, eventstore: eventstore, serializer: serializer, pubsub\_name: pubsub\_name} \= state
    ) do
  event \= %EventStore.EventData{
    \# ... constructed below
  }

  res \= eventstore.append\_to\_stream(topic, :any\_version, \[event\])

  \# For direct\_broadcast targeting the current node, the framework does not
  \# call local dispatch, so the adapter must do it. For regular broadcast,
  \# the framework handles local dispatch after adapter.broadcast returns :ok.
  current\_node \= to\_string(node())
  destination\_node \= Map.get(metadata, :destination\_node)

  if destination\_node \== current\_node do
    dispatcher \= Map.get(metadata, :dispatcher, Phoenix.PubSub)
    Phoenix.PubSub.local\_broadcast(pubsub\_name, topic, message, dispatcher)
  end

  {:reply, res, state}
end

`direct_broadcast/5` is a thin wrapper that sets `destination_node` in the metadata before delegating to `broadcast/5`:

def direct\_broadcast(server, node\_name, topic, message, dispatcher) do
  metadata \= %{
    destination\_node: to\_string(node\_name),
    source\_node: to\_string(node())
  }
  broadcast(server, topic, message, dispatcher, metadata)
end

`source_node` is stored in the event metadata for auditing. Routing is handled downstream by comparing `destination_node` against the current node.

The key decision is how to wrap the message inside `%EventStore.EventData{}`. Serialization is handled by a pluggable module (defaulting to `Phoenix.PubSub.EventStore.Serializer.Base64`) so the adapter is not tied to a specific encoding. The default serializer base64-encodes `:erlang.term_to_binary/`1 output — this is necessary because EventStore stores data as JSON and raw binaries would be invalid, and because JSON cannot distinguish atoms from strings so a round-trip through term serialization preserves type fidelity.

event \= %EventStore.EventData{
  event\_type: to\_string(serializer),
  data: serializer.serialize(message)
}

A custom serializer can be provided via the `serializer` option as long as it implements `serialize/1` and `deserialize/1`.

## Handling events, local distribution

Now that events are in the event store, any subscribed process will receive them. The GenServer must subscribe to all topics (`"$all"`). If the event store is also used for another purpose, it’s best to have a separate one for PubSub. The subscription is set up via `handle_continue/2`, which runs immediately after `init/1` completes, before any other messages can be processed.

def handle\_continue(:subscribe, %{eventstore: eventstore} \= state) do
  eventstore.subscribe("$all")

  {:noreply, state}
end

def handle\_info({:subscribed, \_subscription}, state), do: {:noreply, state}

A transient subscription is used since previous messages are not needed. The event store replies with a {`:subscribed, subscription`} message, which must also be handled. After this, the server will start receiving {`:events, events`} messages.

To avoid dispatching a local message twice (once from `broadcast` and once when the event arrives back from EventStore), a unique ID is added to the process state:

def init(opts) do
  {:ok,
   %{
     id: generate\_unique\_id(opts),
     eventstore: opts\[:eventstore\],
     pubsub\_name: opts\[:name\],
     serializer: opts\[:serializer\] || Phoenix.PubSub.EventStore.Serializer.Base64
   }, {:continue, :subscribe}}
end

defp generate\_unique\_id(opts) do
  unique\_id\_fn \= opts\[:unique\_id\_fn\] || fn \_name \-> UUID.uuid4() end
  unique\_id\_fn.(opts\[:name\])
end

A custom ID generator can be provided via `unique_id_fn` — a function that receives the PubSub name and returns a unique string. Useful when UUID is unavailable or when a deterministic ID is needed for testing.

The `id` is added to the event’s metadata field as `source_id`, keeping it separate from the message data. Serialization is delegated to the configurable `serializer` module. The `handle_call` for `:broadcast` becomes:

event \= %EventStore.EventData{
  event\_type: to\_string(serializer),
  data: serializer.serialize(message),
  metadata: Map.put(metadata, :source\_id, id)
}

Where the value of id and `serializer` come from the state, and `metadata` already contains `dispatcher` and any `destination_node` for direct broadcasts. When an event arrives back, `source_id` identifies the origin node so duplicates can be skipped:

def handle\_info({:events, events}, state) do
  Enum.each(events, &local\_broadcast\_event(&1, state))

  {:noreply, state}
end

defp local\_broadcast\_event(
       %EventStore.RecordedEvent{
         data: data,
         metadata: metadata,
         stream\_uuid: topic,
         eventbies\_type: event\_type
       },
       %{id: id, serializer: serializer, pubsub\_name: pubsub\_name} \= \_state
     ) do
  current\_node \= to\_string(node())

  %{source\_id: source\_id, destination\_node: destination\_node, dispatcher: dispatcher} \=
    convert\_metadata\_keys\_to\_atoms(metadata)

  is\_destination? \= is\_nil(destination\_node) or destination\_node \== current\_node

  if not is\_nil(dispatcher) and is\_destination? and source\_id != id and
       event\_type \== to\_string(serializer) do
    Phoenix.PubSub.local\_broadcast(
      pubsub\_name,
      topic,
      serializer.deserialize(data),
      maybe\_convert\_to\_existing\_atom(dispatcher)
    )
  end
end

That’s it — a complete implementation of Phoenix PubSub using EventStore, including support for `direct_broadcast` via the `destination_node` metadata field and pluggable serialization.
