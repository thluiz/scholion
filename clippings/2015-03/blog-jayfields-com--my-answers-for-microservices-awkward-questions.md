---
url: "http://blog.jayfields.com/2015/03/my-answers-for-microservices-awkward.html"
captured_at: "2015-03-19T11:59:10-03:00"
title: "Jay Fields' Thoughts: My Answers for Microservices Awkward Questions"
domain: "blog-jayfields-com"
---

# My Answers for Microservices Awkward Questions

Earlier this year, Ade published *[Awkward questions for those boarding the microservices bandwagon](http://blog.oshineye.com/2015/01/awkward-microservices-questions.html)*. I think the list is pretty solid, and (with a small push from Ade) I decided to write concise details on my experience.
  
  
I think it's reasonable to start with a little context building. When I started working on the application I'm primarily responsible for microservices were very much fringe. Fred George was already giving (great) presentations on the topic, but the idea had gained neither momentum nor hype. I never set out to write "microsevices"; I set out to write a few small projects (codebases) that collaborated to provide a (single) solid user experience.
  
  
I pushed to move the team to small codebases after becoming frustrated with a monolith I was a part of building and a monolith I ended up inheriting. I have no idea if several small codebases are the right choice for the majority, but I find they help me write more maintainable software. Practically everything is a tradeoff in software development; when people ask me what the best aspect of a small services approach is, I always respond: I find accidental coupling to be the largest productivity drain on projects with monolithic codebases. Independent codebases reduce what can be reasonably accidentally coupled.
  
  
As I said, I never set out to create microservices; I set out to reduce accidental coupling. 3 years later, it seems I have around 3 years of experience working with Microservies (according to the [wikipedia definition](http://en.wikipedia.org/wiki/Microservices)). I have nothing to do with microservices advocacy, and you shouldn't see this entry as confirmation or condemnation of a microservices approach. The entry is an experience report, nothing more, nothing less.
  
  
On to Ade's questions (in bold).
  
  
**Why isn't this a library?**:  
It is. Each of our services compile to a jar that can be run independently, but could just as easily be used as a library.  
  
**What heuristics do you use to decide when to build (or extract) a service versus building (or extracting) a library?**:  
Something that's strictly a library provides no business value on it's own.  
  
**How do you plan to deploy your microservices?**:  
Shell scripts copy jars around, and we have a web UI that provides easy deployment via a browser on your laptop, phone, or anywhere else.  
  
**What is your deployable unit?**:  
A jar.  
  
**Will you be deploying each microservice in isolation or deploying the set of microservices needed to implement some business functionality?**:  
In isolation. We have a strict rule that no feature should require deploying separate services at the same time. If a new feature requires deploying new versions of two services, one of them must support old and new behavior - that one can be deployed first. After it's run in production for a day the other service can be deployed. Once the second service has run in production for a day the backwards compatibility for the first service can be safely removed.  
  
**Are you capable of deploying different instances (where an instance may represent multiple processes on multiple machines) of the same microservice with different configurations?**:  
If I'm understanding your question correctly, absolutely. We currently run a different instance for each trading desk.  
  
**Is it acceptable for another team to take your code and spin up another instance of your microservice?**:  
Yes.  
  
**Can team A use team B's microservice or are they only used within rather than between teams?**:  
Anyone can request a supported instance or fork individual services. If a supported instance is requested the requestor has essentially become a
customer, a peer of the trading desks, and will be charged the appropriate costs allocated to each customer. Forking a service is free, but comes with zero guarantees. You fork it, you own it.  
  
**Do you have consumer contacts for your microservices or is it the consumer's responsibility to keep up with the changes to your API?**:  
It is the consumer's responsibility.
  
  
**Is each microservice a snowflake or are there common conventions?**:  
There are common conventions, and yet, each is also a snowflake. There are common libraries that we use, and patterns that we follow, but many services require sightly different behavior. A service owner ([or primary](http://blog.jayfields.com/2015/02/experience-report-weak-code-ownership.html)) is free to make whatever decision best fits the problem space.
  
  
**How are these conventions enforced?**:  
Each service has a primary, who is responsible for ensuring consistency ([more here](http://blog.jayfields.com/2015/02/experience-report-weak-code-ownership.html)). Before you become a primary you'll have spent a significant amount of time on the team; thus you'll be equipped with the knowledge required to apply conventions appropriately.  
  
**How are these conventions documented?**:  
They are documented strictly by the code.  
  
**What's involved in supporting these conventions?**:  
When you first join the team you pair exclusively for around 4 weeks. During those 4 weeks you drive the entire time. By pairing and being the primary driver, you're forced to become comfortable working within the various codebases, and you have complete access to someone who knows the history of the overall project. Following those 4 weeks you're free to request a pair whenever you want. You're unlikely to become a service owner until you've been on the team for at least 6 months.
  
  
**Are there common libraries that help with supporting these conventions?**:  
A few, but not many to be honest. Logging, [testing](http://jayfields.com/expectations/), and [some common functions](https://github.com/jaycfields/jry) - that's about it.  
  
**How do you plan to monitor your microservices?**:  
We use proprietary monitoring software managed by another team. We also have front line support that is on call and knows who to contact when they encounter issues they cannot solve on their own.  
  
**How do you plan to trace the interactions between different microservices in a production environment?**:  
We log as much as is reasonable. User generated interactions are infrequent enough that every single one is logged. Other interactions, such as snapshots of large pieces of data, or data that is updated 10 or more times per second, are generally not logged. We have a test environment were we can bring the system up and mirror prod, so interactions we miss in prod can (likely) be reproduced in dev if necessary. A few of our systems are also experimenting with a logging system that logs every interaction shape, and a sample per shape. For example, if the message {foo: {bar:4 baz:45 cat:["dog", "elephant"]}} is sent, the message and the shape {foo {bar:Int, baz:Int, cat:[String]}} will be logged. If that shape previous existed, neither the shape nor the message will be logged. In practice, logging what you can and having an environment to reproduce what you can't log is all you need 95% of the time.  
  
**What constitutes a production-ready microservice in your environment?**:  
Something that provides any value whatsoever, and has been hardened enough that it should create zero production issues under normal working circumstances.  
  
**What does the smallest possible deployable microservice look like in your environment?**:  
A single webpage that displays (readonly) data it's collecting from various other services.  
  
I'm happy to share more of my experiences with a microservice architecture, if people find that helpful. If you'd like elaboration on a question above or you'd like an additional question answered, please leave a comment.
