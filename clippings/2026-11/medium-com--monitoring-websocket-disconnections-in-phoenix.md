---
url: "https://medium.com/@fxn/monitoring-websocket-disconnections-in-phoenix-bbe24f54d996"
captured_at: "2026-11-16T06:07:14+00:00"
title: "Monitoring WebSocket disconnections in Phoenix | by Xavier Noria | Medium"
domain: "medium-com"
---

Monitoring WebSocket disconnections in Phoenix
Xavier Noria
4 min read
·
May 20, 2020

Introduction

Say you want to robustly execute some actions when a WebSocket is closed in Phoenix. For instance, logging the disconnection, or decreasing a gauge.

This post shows a way to do that using monitors and a little hack.

First steps

Let’s define a couple of functions in the socket module that implement what we want to do at the start and at the end of a WebSocket connection:

As you see, on_connect/2 calls monitor/2, which spawns a process that monitors the connection. That monitor invokes on_disconnect/1 when the socket is closed. That is the idea.

The next section shows monitor/2, and we’ll see who calls on_connect/2 later below, but let’s pause for a moment to understand what we are doing.

In Phoenix, each WebSocket is managed by a dedicated process. When a socket gets closed, its associated process terminates, and so its monitor receives a :DOWN message.

The monitor gets a :DOWN message regardless of why the process died, this is important. Reason could be a regular disconnection using the API, a phone entering a tunnel, a runtime error, shutting down, …. Doesn’t matter, language semantics guarantee the monitor will get the message.

Cool! Let’s implement the monitor!

The monitor

This is monitor/2, also in MyAppWeb.UserSocket:

That spawns a task that monitors the process managing the connection. Such monitor is very cheap because it blocks on receive and so enters a suspended state until the monitored process terminates. The overhead is neglibible.

A supervised task trapping exits, why?

As you see, that monitor is a supervised task, and it traps exits. Let’s explain why we do it this way.

The purpose of supervisors is generally to restart failed processes. However, the default restart strategy of tasks supervisors is :temporary. Those tasks are never restarted. Why use a supervisor then?

In any Elixir application with a supervision tree, we have to intentionally think what has to happen when the application shuts down. For example, during a deploy.

Supervisors help us specify how our applications start and stop. When an application shuts down, its supervision tree shuts down. By creating tasks under a supervisor, we hook into the shutdown procedure to orderly finish and do not miss pending callbacks.

However, a supervisor by itself is not enough. When stopping, supervisors send their children an exit signal. If those signals are not trapped, the processes are killed immediately. Pending callbacks would be missed.

By trapping exits, the monitors have time to complete their job when their supervisor shuts down. By default, they have up to 5 seconds to do so, but that timeout is configurable via the :shutdown option. This timeout is per process.

What about race conditions?

How do we know all sockets are closed when the tasks supervisor starts shutting down its children? Monitors get notified when their monitored process dies, but when? How can we be sure tasks won’t timeout just because their mailbox have still not received their expected :DOWN messages?

The solution addresses those questions by setting up the tasks supervisor in a certain position in the supervision tree, together with monitor semantics.

Let’s see this in the next section.

Setting things up when the application boots

Supervisors start their children in order, from left to right.

To be able to spawn those supervised tasks in sockets, the tasks supervisor needs to be already up and running when the application is ready to accept connections. That means that we need to spawn the tasks supervisor before the endpoint:

Reciprocally, on shut down, the root supervisor shuts its children down in inverse order. Therefore, when the turn of the tasks supervisor arrives, the endpoint is down, and with the endpoint, all its sockets.

That is how we know tasks won’t block waiting for their sockets, when the tasks supervisor shuts down, all sockets have been already closed.

Wait, the processes managing sockets terminated with the endpoint, cool, but are the messages in the mailboxes of the monitors? Yes, they are.

When a process terminates, all its monitors are conceptually notified at once. When a supervisor shuts its children down, it monitors them. That means that if the endpoint has finished shutting down, the supervisor got notified, and therefore all our tasks too, at the same time. That is a runtime guarantee.

So yes, all monitors have their :DOWN messages ready in the mailbox when the tasks supervisor starts sending exit signals.

A little hack
The problem

We only need one last thing, where do we invoke on_connect/2?

The first idea that comes to mind is to run it within connect/2,3 right? That is the callback invoked by Phoenix when a user wants to establish a connection, so that would be the natural spot.

It would not work. The process running connect/2,3 dies when the callback returns, it is transient. The process actually managing the WebSocket is created by Phoenix only if the connection is accepted by connect/2,3.

Here’s the dilemma: Phoenix needs the return value of the callback to know if it has to create that process, but we are in the callback! The process we want to monitor does not event exist!

The solution

We need a little hack.

The key observation is that self() is the process we want to monitor in the init/1 callback of MyAppWeb.UserSocket. This is not documented, but it will be soon 😉.

Let’s decorate init/1:

There you have it!

An alternative approach

Instead of spawning a dedicated monitor per socket, the application may have one single GenServer that monitors all sockets.

On :DOWN, such server would pop on_disconnect/1 arguments from its state, and spawn a task as we did above for error isolation, parallelism, and controlled shutdowns.

However, that solution is more complicated for my taste due to the additional indirection and code. Cost/benefit is dubious for me. I prefer the simplicity of the approach explained in this post, but other people may have different trade-offs. Your call!

PS: Would like to thank José for helping me with this, and for reviewing this post. ❤️
