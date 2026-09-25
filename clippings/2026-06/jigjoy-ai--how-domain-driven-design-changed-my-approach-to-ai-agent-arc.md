---
url: "https://www.jigjoy.ai/blog/ddd-applied-to-agent-orchestration?ref=dailydev"
captured_at: "2026-06-04T17:25:30+01:00"
title: "How Domain-Driven Design Changed My Approach to AI agent architecture"
domain: "jigjoy-ai"
---

---
![Domain-Driven Design: Tackling Complexity in the Heart of Software by Eric Evans](https://www.jigjoy.ai/blog/ddd-applied-to-agent-orchestration/thumbnail-twitter.png)

I started reading this book last year, when I already had six years of experience as a software engineer.

I was always passionate about programming, but after years of development, I felt exhausted. Programming slowly became a routine. I had the feeling that I had already reached seniority, and that there was not much more I could learn.

Then I started my own startup.

At that point, I began reading books about marketing, finance, economics, product management, and business strategy. I thought those were the areas where I needed to grow. Software development, I believed, was already my strong side. I had the feeling that I was already an expert there.

But after almost three years of building my startup, I can now say that the biggest transformation I experienced was not in marketing, finance, or product management.

It was in software engineering.

And the credit for that goes to one book: **Domain-Driven Design: Tackling Complexity in the Heart of Software** by Eric Evans.

This book completely changed my view of programming and my mental model of how software should be designed. What feels almost absurd is that, in the era of vibe coding, I became more obsessed than ever with clean code, architecture, and thoughtful design.

At the time, I was building a vibe coding platform. The source code started growing quickly, and as a single developer working on such a complex task, the codebase became bigger and harder to understand. I even started forgetting logic I had written only a few months earlier.

I needed to tackle complexity.

## Lessons from a Microservice Split

Before that, I had led a development team in a startup where we built a no-code platform. During that period, I made many mistakes while working on a microservice architecture. I often heard from CTOs that defining the right scope of a microservice is a real science, and something that is often outside of a developer’s usual mindset.

At that time, I approached architecture with that vague feeling. We randomly split a monolith into around ten microservices. But once we reached production, limitations started appearing: latency, DevOps overhead, deployment complexity, and services that had almost no real logic or domain knowledge.

After a few months, I noticed that we were deploying services that barely represented anything meaningful in the business. I wanted to refactor the solution, but the business did not have the patience or understanding for that kind of change.

I left that job with almost zero real knowledge about the domain we were working in.

Back then, I thought business and development were two separate things. I thought solving problems happened on the Jira task level.

Now I think completely the opposite.

Because of my previous experience with microservices, when I started designing the architecture for my own startup, I decided to learn how to do it properly this time. Somewhere, I heard that the “Blue Book” contained the knowledge needed for creating well-scoped microservices.

So I decided to read it.

## Reading the Blue Book

At first, I approached the book like every other technical book. I tried to read chapters quickly and save time. But at some point, I realized that this was a different kind of book, and it required a different kind of approach.

The level of detail was insane.

Even standard concepts like entities, value objects, object lifecycle, interfaces, class names, method names, object relationships, and function side effects suddenly became important. Everything started to matter.

I had the feeling that I knew nothing about programming.

It was like discovering object-oriented programming again: polymorphism, encapsulation, design patterns, and the deeper meaning behind many paradigms I had used mechanically for years.

## Discovering Deeper Domain Insight

Eric Evans was playing with abstractions and explaining in detail how to approach complex domains. He showed how to model architecture in a way that leads to domain insight, and how that insight can lead to superior design.

And insight is one of the most important things for every startup.

Insight will come from crunching domain knowledge and doing several refactorings back and forth.

![Domain insight and modeling breakthrough while applying Domain-Driven Design](https://www.jigjoy.ai/blog/ddd-applied-to-agent-orchestration/breakthrough.jpeg)

For example, Mark Zuckerberg discovered that following people could be more effective and satisfying than only searching for information on forums. Zhang Yiming, the founder of ByteDance, later discovered that the content graph could be more effective than the social graph when it comes to consuming content.

These are not just technical insights. These are domain insights.

## Domain Distillation

Eric Evans introduced the concept of **domain distillation**, which can be used as a technique for splitting a monolith into microservices. More on bounded contexts and how we split our platform you can find [here](https://www.jigjoy.ai/blog/bounded-context), but the real reason why we should do this is not just technical separation.

The real reason is the search for domain insight.

When you are building something new, you can split the domain into multiple subdomains. But only one of them is the **core domain**.

The core domain is the essence of your business. It is the area where you need to be the best in order to win in the market. This is where your unfair advantage should live.

The main idea is to isolate the core domain from supporting domains like payments, user identity management, billing, notifications, and other well-established parts of the system. Those areas are important, but they should not pollute the core of the product.

Using this idea, I split my vibe coding platform into several domains:

-   user account and billing
-   project planning
-   project deployment
-   observability
-   version control
-   AI coding

Then I identified **AI coding** as the core domain.

This is where we need to excel. This is where our unfair advantage needs to be.

But detecting the core domain was only the first step.

The bigger question was: how do I model it?

How do I reach the kind of breakthrough Eric Evans was describing?

So I continued analyzing the book and started reading it for the second time.

## Tackling Complexity in the Heart of Software

Evans introduces several techniques for modeling domains, but the main idea is always the same: model domain concepts, not technology.

He explains layered architecture, which I had used mechanically in previous projects. But this time, I finally understood the purpose behind it.

The code should be split into four layers:

-   UI
-   application
-   domain
-   infrastructure

![Layered architecture: UI, application, domain, and infrastructure](https://www.jigjoy.ai/blog/ddd-applied-to-agent-orchestration/layered-architecture.png)

The code should be split into four layers:

The most important part is that the domain layer should be completely isolated from infrastructure.

That means the domain should not directly access the file system, send HTTP requests to an LLM, depend on a framework, or communicate with external APIs. The domain should contain only modeled concepts and relationships between them.

Infrastructure things, like sending requests or accessing external systems, should live in the infrastructure layer. The concrete use of domain classes should happen in the application layer, which can coordinate the domain and infrastructure.

The second important thing is that the domain layer should not be anemic.

It should not be just data structures with no behavior. It must contain the core concepts that domain experts are talking about. It must contain real business logic.

And this was the hardest part.

## Building Mozaik with Domain-Driven Design

I quickly realized that in order to build AI coding services properly, I needed to go deeper into agent orchestration. So I started developing **Mozaik**, a TypeScript framework for orchestrating AI agents.

But then I faced a difficult question:

How do I create a rich domain layer for AI agents without calling the LLM directly from the domain?

How do I avoid an anemic domain model, while still keeping infrastructure outside of the domain?

This was the trickiest part.

Eventually, I realized that the only way to remove \`await\` from the domain layer was to model orchestration through events.

Instead of letting the agent directly send inference requests, I moved that logic into a separate class called an **Inference Runner**. I also moved function call execution into a separate **Function Call Runner**.

The agent receives a message, and through an observer — an agentic environment — it notifies runners to execute infrastructure-related actions in the application layer. Once they are done, they notify the agent back with the result, and the agent can react.

I started modeling communication between agents without infrastructure leaking into the domain. The domain layer became rich with logic, but still clean and isolated.

And this design opened a lot of new opportunities.

Agents were no longer blocking each other. They could react to user messages, function call outputs, inference results, and messages from other agents in a non-blocking way. In theory, they could handle an infinite number of user requests and agent-to-agent communication flows.

That was the first real insight I discovered while applying Domain-Driven Design to my own startup:

**Asynchronous agents open much more opportunity than synchronous agents.**

Synchronous agents are more rigid. One agent needs to wait for another to finish before continuing. But when agents become event-driven, new possibilities appear.

I expect more insights to come as I continue designing memory, communication between AI agents, and communication between humans and agents.

## Final Thoughts

This book was transformative for my journey.

It reminded me that software engineering is not only about writing code faster. It is about understanding complexity, discovering the core of the domain, and shaping a model that reveals new possibilities.

After six years of development, I thought I had already learned most of what mattered in programming.

But this book showed me that I was only beginning to understand it.

![Miodrag Vilotijević](https://www.jigjoy.ai/profiles/miodrag-vilotijevic.jpeg)

### Miodrag Vilotijević

Co-founder @ JigJoy

Building the future of agentic systems

> With tools and technology we already have, we can build much more valuable systems than most projects today. We can write software that is a pleasure to use and a pleasure to work on; software that doesn't box us in as it grows, but creates new opportunities and continues to add value for its owners.
