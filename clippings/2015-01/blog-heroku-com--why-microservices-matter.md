---
url: "https://blog.heroku.com/archives/2015/1/20/why_microservices_matter"
captured_at: "2015-01-24T08:16:32-03:00"
title: "Heroku | Why Microservices Matter"
domain: "blog-heroku-com"
---

# [Why Microservices Matter](https://blog.heroku.com/archives/2015/1/20/why_microservices_matter)

## Posted 2015-01-20 22:06:01 UTC by Hunter

All successful applications grow more complex over time, and that complexity creates challenges in development. There are two essential strategies to manage this problem: a team can keep everything together (create a monolith) or a team can divide a project into smaller pieces (create microservices).

The monolith at its most extreme is a single code base that contains all of an application’s logic and to which all programmers involved contribute. This approach is perhaps the most natural, and organic growth often tends towards this model. It’s also, in many ways, the easiest to reason about and operate. A single codebase can reduce many of the costs involved in distributed systems. Unfortunately, the practical costs of deploying a very large project can reduce velocity over time and can make it difficult for larger teams to collaborate.

Microservices, on the other hand, describe a strategy for decomposing a large project into smaller, more manageable pieces. Although decomposing big projects into smaller pieces is a practice we’ve seen in the field for as long as software has been written, the recent microservices movement captures a number of best practices and hypotheses about how to scale software development. Microservices encapsulate many of the best practices of some of the industry’s biggest software development organizations, and are at the core of the development practice of many organizations today, not least among them Heroku, Netflix, or Amazon.

It’s worth noting that there is no such thing as a free lunch, and the advantages of microservice based development bring new challenges as well.

## [Microservices Concepts](https://blog.heroku.com/archives/2015/1/20/why_microservices_matter#microservices-concepts)

Put simply, a microservice is a piece of application functionality factored out into its own code base, speaking to other microservices over a standard protocol. To accomplish this, first divide your business requirements into related groups like account management logic, advertising logic, and a web user interface. Write a program to provide each service - thus the name - and connect each service to a language-agnostic protocol like HTTP, AMQP, or Redis. Finally, pass messages via the protocol to exchange data with other services.

This approach maps exceptionally well to the way people use software today. Gone are the days of single programs dominating workflows, or even single devices. Instead, ephemeral APIs provide a flow of data to users through phones, tablets, laptops, wearables, automobiles, and other interfacing hardware. Blog posts, reviews, or even tweets can drastically alter the shape of requests to an organization - but users expect always-reliable, always-fast responses. Microservices can be distributed globally for low latency and can even run multiple versions of the same service simultaneously for redundancy. And, since services are organized by business function rather than compelled by code structure, embracing the technology and interfaces of the future becomes a much less frightening proposition.

However, microservices aren’t a silver bullet, and they won’t make a sluggish IT organization fast. While individual services become more robust and less complex, the overall system takes on the many challenges of distributed systems at the network level. Despite their challenges, they’re here to stay because they map better than anything else to the software landscape of the future: parallel development, platform-as-a-service deployment, and ubiquitous use.

## [What’s Driving this Trend?](https://blog.heroku.com/archives/2015/1/20/why_microservices_matter#what-s-driving-this-trend)

The first force that led to the surge in microservices was a reaction against traditional, monolithic architecture. While a monolithic app is One Big Program with many responsibilities, microservice-based apps are composed of several small programs, each with a single responsibility. This allows teams of engineers to work relatively independently on different services. The inherent decoupling also encourages smaller, simpler programs that are easier to understand, so new developers can start contributing more quickly. Finally, since no single program represents the whole of the application, services can change direction without massive costs. If new technology becomes available that makes more sense for a particular service, it’s feasible to rewrite just that service. Similarly, since microservices communicate across a language-agnostic protocol, an application can be composed of several different platforms - Java, PHP, Ruby, Node, Go, Erlang, etc - without issue.

Of course, software is useless until deployed. As you might imagine, deploying dozens of small services incurs a much greater overhead than shipping a single codebase. Each service requires supporting technologies like load balancing, discovery, and process monitoring - the same type of support you would set up just once for a monolith. This grows even more complex to take advantage of another opportunity in microservices: independently scaling different types of work. Since each service will require a different combination of processing, memory, and I/O to operate at maximum efficiency, they should be housed in different types of containers. Similarly, as workloads change, the scale of each type of service should be able to grow and shrink to adapt to user demand. While this results in incredible levels of flexibility, responsiveness, and efficiency, it also comes with a huge operational cost in terms of IT support.

This led to the second force precipitating microservices: the availability of reliable Platform-as-a-Service providers. Fundamentally, a PaaS provides you with a container, an abstraction in which you house your software. All of the supporting technologies discussed above, from load balancing to independent scaling and process monitoring, are provided by the platform, outside of your container. Without such providers, deploying even a single monolithic app can take whole teams of IT operations specialists. However, with a PaaS, the range of people qualified to deploy applications grows to include generalists like application developers or even project managers, reducing deployment effort to near-zero. For instance some of our customers have no one devoted full-time to IT operations, and can deploy to countries all over the world made by any developer on the team. With the advent of PaaS, microservice deployment has become a reasonable endeavor.

## [What All This Means to You](https://blog.heroku.com/archives/2015/1/20/why_microservices_matter#what-all-this-means-to-you)

You should definitely consider a microservice strategy as part how you scale your projects over time, but you should be mindful of the operational challenges inherent in running multiple codebases.

Dividing your project into components running in their own environment will help you to enforce a separation of responsibility in healthy ways, make it easier to onboard new developers, enable you to choose different languages and technologies for different components, and can help prevent a problem in one part of your code from bringing down the whole system.

That said, microservices are not a free lunch. Each service has its own overhead, and though that cost is reduced by an order of magnitude by running in a PaaS environment, you still need to configure monitoring and alerting and similar services for each microservice. Microservices also make testing and releases easier for individual components, but incur a cost at the system integration level. Plan for how will your system behave if one of the services goes offline.

Don’t start by splitting your code up too finely. Each division point becomes an API your team will need to support over time. At Heroku, we tend to have slightly fewer services than the number of developers on a project. Separating mobile and web clients from their APIs is a very sensible place to start. Over time, decompose projects further when they become unwieldy.

Overall, though, a considered strategy of decomposing your application into smaller pieces will allow you to make better technology choices, give your team more velocity, and can give you more ways to maintain availability.

## [Learn More](https://blog.heroku.com/archives/2015/1/20/why_microservices_matter#learn-more)

If you’d like to learn more about how your organization can take advantage of microservices on Heroku take a look at this Nodevember talk on 'Production-Ready Node Architecture' <http://bit.ly/1yF6vJt> and Fred George's NodeConf EU talk on 'Microservice Challenges' <http://bit.ly/1EnKHEc>

Tags: [microservices](https://blog.heroku.com/tags/microservices)
