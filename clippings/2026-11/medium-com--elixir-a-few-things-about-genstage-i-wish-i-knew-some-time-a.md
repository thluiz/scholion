---
url: "https://medium.com/@andreichernykh/elixir-a-few-things-about-genstage-id-wish-to-knew-some-time-ago-b826ca7d48ba"
captured_at: "2026-11-16T06:05:25+00:00"
title: "Elixir: a few things about GenStage I wish I knew some time ago | by Andrey Chernykh | Medium"
domain: "medium-com"
---

Elixir: a few things about GenStage I wish I knew some time ago
Andrey Chernykh
5 min read
·
Jun 14, 2018

Today I want to talk about GenStage. Although this behaviour was introduced a while ago in Elixir ecosystem not every developer has tried it out. And there is a bunch of questions that you’ll probably face while dealing with GenStage for the first time.

Press enter or click to view image in full size
Stages are data-exchange steps that send and/or receive data from other stages. When a stage sends data, it acts as a producer. When it receives data, it acts as a consumer.

I don’t want to duplicate all the information available in the GenStage’s documentation. I’d rather to make an emphasis on some key aspects I’ve faced on my own during GenStage implementation and usage in production.

Two usage approaches

There are various use cases for GenStage but in general I split them (my humble opinion) on two groups depending on the ownership of events (data) source, and they are simple:

You own events source (demand handling)

In this case it is your responsibility to fetch more events, you can control the load and the demand received from Consumers. GenStage’s buffer is needed for some corner cases (for example, when your Consumer(-s) went down in the moment of events dispatching).

An events source might be a database or third-party application, API, etc. Producer is going to fetch events only in order to cover an incoming demand from its consumers.

Press enter or click to view image in full size

Example: you need to import data from another application and this application exposes an API which allows you to fetch data by batches or pages.

Once your Consumers handled a batch they start asking for more and the producers makes a call to that external API in order to fetch exact amount of data and emit events, satisfy the Consumers demand.

If your GenStages where designed properly there is no chance for a Producer to be overloaded by data.

In this case GenStages are implemented for parallel or even distributed data handling.

You don’t own events source (events pushing)

In this case you can not control events coming into a Producer, therefore you can not control the load. Producer’s buffer starts to play an important role: as built-in backpressure mechanism.

Producer is going to receive various and unpredictable amount of events from time to time or serve infinite data stream.

Press enter or click to view image in full size

Example: you need to send push notifications depending on some events from your application (received from RabbitMQ for example). You can not predict the amount of push notifications needed to be sent. At some moment you should to handle only 10 requests for pushes but in a next few minutes this amount can turn into 10000 (marketing team did their job great and users started to use your application like crazy).

In this case Consumers wait for work and Producer itself ignores Consumers demand, receives incoming external events and dispatches them to the Consumers while trying not to die under the pressure.

So GenStages should be implemented for backpreassure purpose mainly.

Now when I introduced two main GenStage’s usage approaches, let’s take a closer look at each of them and things you should be aware of.

Events pushing

This approach is very straightforward and actually doesn’t hide any problems.

Here is a Producer and a Consumer examples:

Under the hood, actually, the Consumer sends a demand to the Producer, but the Producer ignores it end replies with no events. “No events” response is then successfully ignored by the Consumer. So both the Consumer and the Producer await for an incoming event constantly. None of them initiate work to do. Work comes from outside of GenStages.

Demand handling

This approach has a few things you need to know in order to implement GenStages properly.

Let’s start with a code:

There are Producer’s and Consumer’s code above. The Producer should take care of a demand: store Consumer’s demand that wasn’t satisfied by this Producer and at the same time store events that were odd on previous demand handling. Why?

One thing you should keep in mind working with a Consumer’s min. demand: it doesn’t define the lower limit when a Consumer will go for more events. Actually, a Consumer asks for more job when it has max_demand — min_demand events in its queue. For example above it equals to 3.

A Consumer initially asks for 4 events
Receives only 2
Awaits for 1 more (and while it waits for this event it does nothing)
Receives the required 1 event
Starts to handle those 3 events
Asks for more events then

So if you have a requirement to handle an event immediately this could be a surprise for you that a Consumer doesn’t serve events when they come, but awaits for more to satisfy this formula.

This is why you need to keep demand in a Producer — to let it know that not all demand was covered and some Consumers still waiting for a work (not asking for events explicitly). And may be you should go and try to fetch more events on timeout/schedule or just try to fetch them constantly in a recursion.

If you forget about it and your Producer listens only for incoming demand you will get hanging events in one of your Consumers at some moment.

A few tips
How to start Consumers dynamically?

Almost every tutorial describes a situation when you have a Producer and a bunch of pre-spawned Consumers. Which is not suitable for all cases you might face.

Here a simple example code shows how to spawn Consumers dynamically from a Producer.

Consumers Supervisor:

Producer:

What are Consumer’s subscription approaches?

In some cases you might need to have a Producer and Consumers on different nodes/servers. Here are subscription approaches for a Consumer:

Learn more about GenStage.Dispatcher behaviour

You can dramatically change the way how your GenStages behave with a right Dispatcher usage.

During an initialisation you can apply one of three predefined Dispatchers to a Producer:

GenStage.DemandDispatcher - dispatches the given batch of events to the consumer with the biggest demand in a FIFO ordering. This is the default dispatcher.
GenStage.BroadcastDispatcher - dispatches all events to all consumers. The demand is only sent upstream once all consumers ask for data.
GenStage.PartitionDispatcher - dispatches all events to a fixed amount of consumers that works as partitions according to a hash function.

…or create one on your own implementing the behaviour.

Thank you for your time. Happy coding!
