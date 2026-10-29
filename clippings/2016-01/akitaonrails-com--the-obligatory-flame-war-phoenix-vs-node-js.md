---
url: "http://www.akitaonrails.com/2015/12/03/the-obligatory-flame-war-phoenix-vs-node-js"
captured_at: "2016-01-10T07:39:41-03:00"
title: "The Obligatory &quot;Flame War&quot; Phoenix vs Node.js | AkitaOnRails.com"
domain: "akitaonrails-com"
---

# The Obligatory &quot;Flame War&quot; Phoenix vs Node.js

### The Obligatory “Hello World” warm up

For this very short post, I just created a Node.js + Express “hello world” and I will point to it’s root endpoint, which is Express rendering a super simple template with one title and one paragraph, and that’s it.

For Elixir, I just bootstrapped a bare bone Phoenix project and added one extra endpoint called “/teste” in the Router which will call the PageController, then the “teste” function and render a template with the same title and paragraph as in the Express example.

Simple enough. Phoenix does more than Express, but this is not supposed to be a fair trial anyway. I chose [Siege](https://www.joedog.org/siege-home/) as the testing tool for no particular reason, you can pick the testing tool you like the most. And I am running this over my 2013 Macbook Pro with 8 cores and 16GB of , so this benchmark will never max out my machine.

The first test is a simple run of 200 concurrent connections (the number of CPUs I have) firing just 8 requests each, for a total of 1,600 requests. First, the Node.js + Express results:

Node.js x Siege -r 8 -c 200

![58b5e83100f9b57a8b2b2af100313fa0.png](akitaonrails-com--the-obligatory-flame-war-phoenix-vs-node-js/58b5e83100f9b57a8b2b2af100313fa0.png)00:0000:00

[Video download link](https://s3.amazonaws.com/videos-akitaonrails/Elixir/Node+8+x+200.mp4)

The first run already broke a few connections, but the 2nd run picked up and finished all 1,600 requests. And this is the Phoenix results:

Phoenix x Siege -r 8 -c 200

![58b5e83100f9b57a8b2b2af100313fa0.png](akitaonrails-com--the-obligatory-flame-war-phoenix-vs-node-js/58b5e83100f9b57a8b2b2af100313fa0.png)00:0000:00

[Video download link](https://s3.amazonaws.com/videos-akitaonrails/Elixir/Phoenix+8+x+200.mp4)

As you can see, Node.js has the upper hand in terms of total time spent. One single Node.js process can only run one single real OS thread. Therefore it had to use just a single core (although I had 7 other cores to spare). On the other hand, Elixir can reach all 8 cores of my machine, each running a Scheduler in a single real OS thread. So, if this test was bound, it should have run 8 times faster than the Node.js version. As the test is largely a case of I/O bound operations, the clever async construction of Node.js does the job just fine.

This is not an impressive test by any stretch of the imagination. But we’re just warming up.

Oh, and by the way, notice how Phoenix logs show the request processing times in MICROseconds instead of Miliseconds!

### The Real Fun

Now comes the real fun. In this second run, I added a blocking “sleep” call to both projects, so each request will sleep for 1 full second, and this is not absurd, many programmers will do poor code that blocks for that ammount of time, procesing too much data from the database, rendering templates that are too complex, and so on. Never trust a programmer to do the right best practices all the time.

And then I fire up Siege with 10 concurrent connections and just 1 request each, for starters.

Node.js (sleep) x Siege -r 1 -c 10

![58b5e83100f9b57a8b2b2af100313fa0.png](akitaonrails-com--the-obligatory-flame-war-phoenix-vs-node-js/58b5e83100f9b57a8b2b2af100313fa0.png)00:0000:00

[Video download link](https://s3.amazonaws.com/videos-akitaonrails/Elixir/Node+1+x+10+Sleep.mp4)

And this is why in my [previous article of ‘Why Elixir?’](http://www.akitaonrails.com/2015/12/01/the-obligatory-why-elixir-personal-take) I repeated many times how **“rudimentary”** a Reactor pattern based solution is. It is super easy to block a single threaded event loop.

If you didn’t know that already, how does Node.js work? In summary it is a simple infinite loop. When a Javascript function runs it blocks that event loop. The function has to explicitly yield control back to the loop for another function to have a chance to run. I/O calls take time and just sits back idly waiting for a response, so it can yield control back and wait for a callback to continue running. Which is why you end up with the dreaded *“callback pyramid hell”*.

Now, with what I explained in all my previous articles, you may already know how Elixir + Phoenix will perform:

Phoenix (sleep) x Siege -r 2 -c 400

![58b5e83100f9b57a8b2b2af100313fa0.png](akitaonrails-com--the-obligatory-flame-war-phoenix-vs-node-js/58b5e83100f9b57a8b2b2af100313fa0.png)00:0000:00

[Video download link](https://s3.amazonaws.com/videos-akitaonrails/Elixir/Phoenix+2+x+400+-+Sleep.mp4)

As expected, this is a walk in the park for Phoenix. It not only doesn’t have a rudimentary single thread loop waiting for the running functions to willingly yield control back. The Schedulers can forcefully suspend running coroutines/processes if it thinks they are taking too much time (the 2,000 reductions count, and priority configurations), so every running process has a fair share of resources to run.

Because of that I can keep increasing the number of requests and concurrent connections and it’s still **fast**.

In Node.js, if a function takes 1 second to run, it blocks the loop. When it finally returns, now the next 1 second function can run, and that’s why if I have 10 requests taking 1 second each to run, the entire process will linearly take 10 entire seconds!

Which obviously **does not scale**! If you “do it right” you do can scale. But why bother?

### “Node” done right

As a side note, I find it very ironic that “Node” is called “Node”. I would assume that it should be easy to connect multiple Nodes that communicate between each other. And as a matter of fact, [it is not](http://www.sitepoint.com/how-to-create-a-node-js-cluster-for-speeding-up-your-apps/).

If I had spinned up 5 Node process, instead of 10 seconds, everything would take 2 seconds as 5 request would block the 5 Node processes for 1 second, and when returned, the next 5 requests would block again. This is similar to what we need to do with Ruby or Python, that have the dreaded big Global Interpreter Locks () and that in reality can only run one blocking computation at a time. (Ruby with Eventmachine and Python with Tornado or Twisted are similar to Node.js implementation of a reactor event loop).

Elixir can do much better in terms of actually coordinating different nodes, and it is the Erlang underpinnings that allow highly distributed systems such as [ejabberd](https://www.ejabberd.im/) or [RabbitMQ](https://www.rabbitmq.com/) to do their thing as efficiently as they can.

Check out how simple it is for one Elixir Node to notice the presence of other Elixir nodes and make them send and receive messages between each other:

Node done right in Elixir

![58b5e83100f9b57a8b2b2af100313fa0.png](akitaonrails-com--the-obligatory-flame-war-phoenix-vs-node-js/58b5e83100f9b57a8b2b2af100313fa0.png)00:0000:00

[Video download link](https://s3.amazonaws.com/videos-akitaonrails/Elixir/7+-+Nodes.mp4)

Yep, it is this simple. We do Remote Procedure Calls () for decades, this is not something new. Erlang has this implemented for years and it is built-in and available for easy usage out-of-the-box.

In their websites, ejabbed calls itself “Robust, Scalable and Extensible Server”, and RabbitMQ calls itself “Robust messaging for applications”. Now we know they deserve the labels of “Robust” and “Scalable”.

So, we are struggling to do things that are already polished and ready for years. Elixir is the key to unlock all this Erlang goodness right now, let’s just use it and stop shrugging.
