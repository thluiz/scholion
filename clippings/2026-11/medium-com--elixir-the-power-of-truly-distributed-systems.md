---
url: "https://medium.com/unbabel/elixir-the-power-of-truly-distributed-systems-c4c79ed9f97d"
captured_at: "2026-11-16T06:19:26+00:00"
title: "Elixir: The power of truly distributed systems | by Eduardo Pereira | Medium"
domain: "medium-com"
---

Elixir: The power of truly distributed systems
Everyone needs to scale
Eduardo Pereira
6 min read
·
Oct 29, 2018

Most tech startups’ lifecycles start with a dark age. There you are, grasping about for product-market fit, not worrying too much about the future. You might not actually find one.

But then, hopefully, others start showing interest in your idea, and it’s time to produce a proof of concept, your first iteration. Your MK1.

MK1

It serves its purpose. You will be able to demo it, pitch it and show what the future could look like, given time and money.

Scaling 2 or 3 times is quite easy

During your growth, you can react to every challenge that shows up. Adding infrastructure to cope with immediate needs is common practice. You can also improve some queries to the database and optimize some algorithms. Everything will seem faster and smoother… for the next 5 minutes.

One night, your whole team gets woken up by a client because your service went down at 4 AM on a Sunday.

You open up your telemetry and are greeted by the following landscape:

Diagram of both a core service’s CPU usage and my heart rate.

Thanos arrived and you were not ready for him. You need to be ahead of the curve. You need to build MK50.

MK50
Scaling 10 to 20 times, not that easy

Scaling to the next zero is expected of you, but often hard, if you are not prepared.

At Unbabel, we are quite fond of a little book called the Toyota Way. There’s a lot to it but we can extract three basic rules to guide our way:

Eliminate waste
Be efficient
Be prepared

Try to eliminate waste from your process, your daily routine and your code. Always try to optimize what you are doing and be as efficient as possible: deliver quality fast. Plan for the future. Adapt your way of thinking and your tools.

Elixir

The embodiment of this mindset for us was adopting Elixir. It embraces this way of thinking at its core. This language produces low-latency, scalable apps that are fault-tolerant and distributed.

It is also surrounded by a great, healthy community that is quite active and helpful. Great documentation is the cherry on top of the cake.

OTP

Stands for Open Telecom Platform and is a set of building blocks, no longer only used in telecoms, that leverage Erlang itself, tools and libraries made available by the virtual machine and a set of design principles. One of these principles is using a process-based architecture.

Processes

Are the foundation of programming in Elixir. All your code runs inside processes. These are not your standard operating system processes, but Erlang virtual machine (BEAM) processes. They are extremely lightweight, both in terms of CPU and Memory usage, allowing us to have several hundred thousand of them running at the same time. Super efficient.

They are also completely isolated, sharing no state or memory space among them, thus allowing for true concurrency. They store state, but, as they share no memory, the only way to communicate this is through messages. It also helps that Elixir is a functional programming language and one of its features is immutability. This ensures that we are not controlling state in any weird way. Forget about threads.

Each process has a queue on which it will receive messages and will act on them asynchronously. You should not be blocked waiting for a response.

Supervisors

These are a special kind of process. These processes are linked to other processes with the goal of monitoring their state. When a process fails, the supervisor will identify it, terminate it and restart it, restoring its initial state.

The impact of these failures is always very low as these processes are isolated, which will give us time to solve the issue.

Thinking Concurrently
Generic VS Concurrent Approach

When you think concurrently, you change your approach and your mindset. You solve problems differently. You start to see the advantages of what we talked about before.

You conclude that, instead of using one big web server that handles millions of sessions, what you need is millions of web servers, each one handling one session. You start to approach every single problem, even the small ones, like this.

You are creating an optimisation-based mindset. You just adapted.

In practice

How do you approach problems in a concurrent way?

We ran one scenario to showcase this concurrent way of thinking:

We populated a simple database table with 20,000 rows. This table has only 2 columns: the ID and an Integer called Value. This value starts at 3 and we should subtract 1 from it each second until it reaches 0. We want to repeat this process every 2 seconds.

Problem-solving with processes

We will launch 1 process that will be responsible for monitoring the database. This process will decide to launch 10,000 processes that will, individually, handle one, and only one, database row. We will keep launching new processes until all rows are processed. When all is finished the process will end, releasing all memory.

How about code?

Clean, simple and functional, this is how we implement one of these 10.000 processes:

This micro web server is actually a GenServer. In Elixir/Erlang a GenServer is process that can be used to keep state and execute code asynchronously. Its behaviour abstracts a client-server interaction and we only need to implement the callbacks. It fits into a supervision tree.

We have an init() function that we use to initialize its state. We initialize it with the ID of the record we want to handle.

We also have defined the handle_info() function that will handle messages with the symbol work, triggering the transaction where we update the record and schedule the next execution, asynchronously.

Finally, we defined a schedule() function responsible that will essentially make the process self-managed by executing a call to itself in the future.

This is our microserver and we can have several thousand of them.

Elixir allows for clean, simple code. Easily we can feel productive and fast, eliminating more waste.

How does this behave?

Fortunately, Elixir allows us to monitor BEAM easily. We can monitor the process tree, memory usage, IO and other useful information during development.

During execution we can monitor the number of processes being used, and that they correspond roughly to how many processes we decided to launch.

BEAM Telemetry

We can track memory usage and notice that processes release it when they finish. We can fully understand how our code is behaving during execution while developing and it encourages us to keep our code efficient. Visibility is key.

So what’s the impact?

Elixir, while being extremely efficient by itself, allows us to take an efficient approach to problem-solving. It is both a tool and a mindset that allow us to write scalable, fault-tolerant applications for our most processing-intensive services.

And when we finally apply these principles what do we get?

A byproduct of this is boring telemetry.

We get 20ms average response time, stable low memory usage and peak CPU use of 2%. We get boring telemetry (the best telemetry).

We get the peace of mind that our system is healthy and stable. We control the variables, they don’t control us. We can stop being reactive and start being proactive and focused. We are able to leave the loop of fixing stuff and start focusing on the loop of building stuff.

It perfectly resonates with us as an Engineering Team and it is how we intend to defeat Thanos.

Now, go be Tony Stark and go build your own scalable applications with Elixir.
