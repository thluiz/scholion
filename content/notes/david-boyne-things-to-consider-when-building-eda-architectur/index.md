---
title: "David Boyne: things to consider when building EDA architectures"
date: '2023-10-24T14:26:39+00:00'
category: comic
summary: "David Boyne's illustrated list of things that can catch you out in event-driven architectures, from idempotency and commands versus events to documentation and standards."
tags: ["david-boyne", "event-driven-architecture", "software-architecture"]
has_commentary: false
sources:
  - title: "David Boyne: things to consider when building EDA architectures"
    author: "David Boyne"
    url: "https://x.com/boyney123/status/1682330601657974785"
    kind: web
---

Posted by David Boyne (@boyney123) on X, 2023-07-21. [Tweet](https://x.com/boyney123/status/1682330601657974785).

> Thinking about building event-driven architectures/applications?
>
> Here are my thoughts on what you should consider when building EDA applications.
>
> 1. Lack of idempotency handling
> Consumers may process events more then once (or you may need to replay them, failures etc). Thinking about idempotency can help you build solutions without side effects.
>
> 2. Mistaking commands vs events
> Easy to do when you start, but there is a difference between commands and events. What is the intent of your message/event? Do you want to perform an action or raise a factual event? Understand differences can help.
>
> 3. Multi purpose events
> It's easy to add fields onto your events, without thinking too much about it's design and impact. Doing this can impact the intent of your events, consumers may have a hard to time understanding that. One event to rule them all? Or split into multiple events? Something to think about....
>
> 4. Lack of documentation
> Usual story here, lack of documentation for systems can hurt. When building event-driven architectures lack of knowledge of consumers/producers can lead to a mess. Think about how you can document this, where you put this information and how your architecture can evolve. Visibility on this stuff can help.
>
> 5. Leaking implementation details
> Raising events can be simple, but knowing what to put in them is hard. Don't leak too much implementation details in your events. Consumers may not want to know about internal domain information, split your domains keep your events clean.
>
> 6. Lack of standards/structures
> At the start you may have a few events, standards may not emerge, but over time when you have 100s of them, you may wish you have standards in your events. What structure should your events follow? What metadata should they all contain? What open standards can you use?
>
> These are just a few of my thoughts and lessons learnt in the past, I have written up more with extra resources for you do dive deep, hope it helps 
>
> Visual and resources 
> https://serverlessland.com/event-driven-a
> rchitecture/visuals/things-to-consider
> …

![Infographic titled Things to consider when building EDA architectures, by David Boyne: six small diagrams labeled Lack of idempotency handling, Mistaking commands and events, The multi-purpose event, Explicit events, Lack of documentation, Leaking implementation details and Lack of standards/structure.](david-boyne-things-to-consider-when-building-eda-architectur.jpg)
