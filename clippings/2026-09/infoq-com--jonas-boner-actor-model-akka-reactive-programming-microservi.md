---
url: "https://www.infoq.com/podcasts/jonas-boner-akka?utm_source=email&utm_campaign=summerpodcast"
captured_at: "2026-09-27T00:37:09+01:00"
title: "Jonas Bonér on the Actor Model, Akka, Reactive Programming, Microservices and Distributed Systems"
domain: "infoq-com"
---

[InfoQ Homepage](https://www.infoq.com/ "InfoQ Homepage") [Podcasts](https://www.infoq.com/podcasts "Podcasts") Jonas Bonér on the Actor Model, Akka, Reactive Programming, Microservices and Distributed Systems

Feb 17, 2017

by

*   [![Author photo](https://cdn.infoq.com/statics_s1_20260925154608/images/profiles/RNfXYqHnI6739zST7iZa8uc3t49LGO4G.jpg)](https://www.infoq.com/profile/Wesley-Reisz/) [Wesley Reisz](https://www.infoq.com/profile/Wesley-Reisz/)
    
    Technical Principal @Thoughtworks & Chair QCon.AI

[Jonas Bonér](https://qconlondon.com/london-2017/speakers/jonas-bon%C3%A9r?utm_source=infoq&utm_medium=podcast&utm_campaign=podcast), CTO of LightBend and creator Akka, discusses using Akka when developing distributed systems. He talks about the Actor Model, and how every Microservice needs to be viewed as a system to be successful.

### Key Takeaways

*   Akka is JVM-based toolkit design for developing distributed systems leveraging the Actor Model - an approach for writing concurrent systems that treat actors as universal primitives and the most successful model with abstraction has been streaming
*   Circuit breakers in Akka are a backup and retry policy; they protect you by capturing failure data and allow you to roll back
*   Every Microservice needs to be viewed as a system, it needs to have multiple parts that run on different machines in order to function and be fully resilient - thus is a Microsystem
*   Two different trends have emerged when it comes to hardware and environments: one is the trend toward Multi-core, the is a movement toward virtualized environments and the cloud
*   Saga pattern of managing long running transactions in a distributed system fits very well with messaging style architectures

#### Related Sponsors

*   ##### [Beyond the Data Lake: Building AI-Ready Data Foundations for Agentic AI](https://www.infoq.com/vendorcontent/show.action?vcr=216a3114-ceef-4bfc-ad6a-08ec5bc8cc51&primaryTopicId=2498&vcrPlace=EMBEDDED&pageType=PODCAST_PAGE&vcrReferrer=https%3A%2F%2Fwww.infoq.com%2Fpodcasts%2Fjonas-boner-akka%2F%3Futm_source%3Demail%26utm_campaign%3Dsummerpodcast&ha=bW91c2Vtb3Zl)
    
*   ##### [AI-Native Software Delivery - Download the eBook (By O'Reilly)](https://www.infoq.com/vendorcontent/show.action?vcr=9831f722-2945-4987-98d0-c1c46b32e5ef&primaryTopicId=2498&vcrPlace=EMBEDDED&pageType=PODCAST_PAGE&vcrReferrer=https%3A%2F%2Fwww.infoq.com%2Fpodcasts%2Fjonas-boner-akka%2F%3Futm_source%3Demail%26utm_campaign%3Dsummerpodcast&ha=bW91c2Vtb3Zl)
    
*   ##### [AI's Physical Constraints: How AI Rewired the Data Center](https://www.infoq.com/vendorcontent/show.action?vcr=7bf8495f-cd88-40d6-92aa-1afa5ad24523&primaryTopicId=2498&vcrPlace=EMBEDDED&pageType=PODCAST_PAGE&vcrReferrer=https%3A%2F%2Fwww.infoq.com%2Fpodcasts%2Fjonas-boner-akka%2F%3Futm_source%3Demail%26utm_campaign%3Dsummerpodcast&ha=bW91c2Vtb3Zl)
    
*   ##### [Context Lake vs. Data Lake: A New Architecture for Modern AI](https://www.infoq.com/vendorcontent/show.action?vcr=f16e12e1-ede3-457f-a37b-9d061aca4df6&primaryTopicId=2498&vcrPlace=EMBEDDED&pageType=PODCAST_PAGE&vcrReferrer=https%3A%2F%2Fwww.infoq.com%2Fpodcasts%2Fjonas-boner-akka%2F%3Futm_source%3Demail%26utm_campaign%3Dsummerpodcast&ha=bW91c2Vtb3Zl)
    
*   ##### [\[Webinar\] Creating Certainty in the Age of Agentic AI. Watch On-Demand.](https://www.infoq.com/vendorcontent/show.action?vcr=531d8edd-4f74-486b-aaca-10058c609c1c&primaryTopicId=2498&vcrPlace=EMBEDDED&pageType=PODCAST_PAGE&vcrReferrer=https%3A%2F%2Fwww.infoq.com%2Fpodcasts%2Fjonas-boner-akka%2F%3Futm_source%3Demail%26utm_campaign%3Dsummerpodcast&ha=bW91c2Vtb3Zl)
    

## **Show Notes**

**Akka**

*   0m:40s [Akka](http://akka.io/) a JVM-based toolkit designed for developing distributed systems that leverage the actor model - takes it’s inspiration from Erlang
*   0:50s - It offers two things; it provides a reasonably high level abstraction for building concurrent applications as well as working with multiple machines and nodes:  it unifies the two problems into one single abstraction - it makes distribution first class
*   1m:30s - This is the beauty of actors in general—they make the network distribution first class
*   1m:40s - Works very well for scaling things up on Multi-core architectures as well.

**The Actor Model**

*   1m:50s - The Actor Model is an approach for writing concurrent systems that treat actors as universal primitives.
*   1m:55s - The Idea is actors can only modify their own private state and they pass messages to each other thus avoiding locks
*   2m:50s - Akka gets these great ideas onto a platform that most people use - the JVM.

**When Akka and the Actor Model is the perfect choice**

*   3m:18s - At a high level, Akka is a sort of computing fabric, a distributed computing fabric that abstracts away the hard things, it makes the network first class for example and deals with hard problems in distributed computing like partial failures, dropped messages and so on. So you have the tools to build truly reliable systems and the abstractions are not in the way.
*   4m:56s -  Akka has added layers on top of the actor model, the most successful has been streams - the world is going streaming, it’s a hot topic.

**Circuit breakers patterns in distributed systems**

*   5m55s - Bulk heading is the foundation as it allows an instance to die and be restarted in isolation.
*   6m:40s - Circuit breakers capture any failures and you have that data. Sort of a back up and retry policy
*   6m:50s - It doesn’t currently work with retry. We don’t have tools that help with this - but it’s very much a real problem
*   8m:35s - As an industry we have very immature tools in general to understand how distributed systems work at large - the systems part, not the individual components.

**Two trends toward Multi-core**

*   9m:17s - The move back away from concurrency and towards distributed systems is driven by a few trends. On the hardware side one is the trend toward Multi-core, the other movement is toward virtualized environments and the cloud where you need the ability to scale on demand
*   10m:48s -The other driver is the users. They are picky when it comes to reliability for example - systems simply cannot fail today, and you cannot build a fully reliable system with a single node.

**Reactive Manifesto**

*   13m:49s - The Reactive Manifesto is a framework and set of principles to help build reliable systems that scale—they should be elastic and resilient
*   15m:00s - To always be responsive the system has to fully embrace asynchronous message passing
*   16m:12s - It gives you what you need to use the full promise of cloud computing—scale on demand etc.

**Event Driven vs. Message Driven**

*   16m:40s - Event driven is generally about publishing facts to anonymous listeners; it can be zero or many subscribers
*   17m:36s - The problem with it is you can’t model communication on it, you’re not working with addressable recipients like you are with message passing  
*   18m:00s - Messaging Driven is a great model for distributed communication, that’s why it’s the foundation for reactive systems
*   18m:37s - Often you need to pair these two. The event driven is exposed to the user, while message driven is the way things work under the hood.

**Reactive Programming and Streams**

*   20m:00s - - Reactive systems are what we talk about in the reactive manifesto.
*   20m:20s - Reactive Programming is another trend. It is about making individual components really efficient and making the maximum use of the hardware through non-blocking communication and asynchronous communication
*   20m:57s - Reactive streams is a simple standard for doing streaming with back pressure
*   21m:48s - Often you use many different tools in an application—it’s not just one tool, framework or library

**Microliths to Microsystems**

*   22m:48s - The title of my [QCon talk](https://qconlondon.com/london-2017/speakers/jonas-bon%C3%A9r?utm_source=infoq&utm_medium=podcast&utm_campaign=podcast) is about thinking simplistic and not going all in with what it means to build Microservices
*   24m:59s - Every Microservice needs to be viewed as a system, it needs to have multiple parts that run on different machines in order to fully function and be resilient
*   25m:53s - Thinking holistically that embracing the fact that creating one single Microservices still means you have build a distributed system.

**What do you have to get right before you start trying to deploy a distributed systems?**

*   26m:27s - Goes back to people and process and their knowledge and splitting it up into the right teams
*   26m:54s - Lots of people forget when going into Microservices, they are about to build distributed system
*   27m:28s - Embracing reality and constraints helps a lot rather than trying to pretend they don’t exist
*   28m:20s - Continuous delivery and the ability to roll back with blue/green and canary deployments are extremely important. Netflix has talked a lot about these kinds of things
*   28m:50s - Having tools that understand the system at large - visibility and transparency into what’s really going on
*   29m:01s - Understand the flows and how components interact with each other

**Working with ML / AI at Lightbend to understand tracing through distributed system**

*   29m:24s - Using machine learning to try to understand what’s going wrong in the systems, detection, predictive scaling etc.
*   30m:15s - There’s a need for embracing and moving forward - taking the Serverless mentality or operation-less mentality further but for building real systems, systems that are stateful

**Saga Pattern**

*   33m:30s - The Saga pattern is a way of managing long running transactions in a distributed system
*   34m:15s - Instead of using distributed transactions with a global lock it is a protocol of guessing and apologizing if you’re wrong with your guess, and performing a compensating action if you are wrong
*   37m:05s - This way of thinking matches reality quite well.

**Technology Discussed:**

*   [Akka](https://www.infoq.com/akka/?utm_source=infoq&utm_medium=podcast&utm_campaign=podcast)
*   [The Actor Model](https://www.infoq.com/news/2014/10/intro-actor-model?utm_source=infoq&utm_medium=podcast&utm_campaign=podcast)
*   [JVM](https://www.infoq.com/jvm/?utm_source=infoq&utm_medium=podcast&utm_campaign=podcast)
*   [Microservices](https://www.infoq.com/microservices/?utm_source=infoq&utm_medium=podcast&utm_campaign=podcast)
*   [Reactive Programming](https://www.infoq.com/reactive-programming/?utm_source=infoq&utm_medium=podcast&utm_campaign=podcast)
*   [Multi-core](https://www.infoq.com/multi-core/?utm_source=infoq&utm_medium=podcast&utm_campaign=podcast)
*   [Machine Learning](https://www.infoq.com/machinelearning/?utm_source=infoq&utm_medium=podcast&utm_campaign=podcast)
*   [Artificial Intelligence](https://www.infoq.com/artificial_intelligence?utm_source=infoq&utm_medium=podcast&utm_campaign=podcast)
*   [Erlang](https://www.infoq.com/presentations/erlang-software-for-a-concurrent-world?utm_source=infoq&utm_medium=podcast&utm_campaign=podcast)

**Companies Mentioned:**

*   [LightBend](https://www.lightbend.com/)
*   [Netflix](https://www.infoq.com/netflix/)

**Links:**

*   [The Reactive Manifesto](http://www.reactivemanifesto.org/)
*   Martin Fowler - "[You must be this tall to use microservices](https://martinfowler.com/bliki/MicroservicePrerequisites.html)"

## **More about our podcasts**

You can keep up-to-date with the podcasts via our [RSS Feed](http://www.infoq.com/podcasts/jonas-boner-akka/), and they are available via [SoundCloud](https://soundcloud.com/infoq-channel), [Apple Podcasts](https://itunes.apple.com/gb/podcast/the-infoq-podcast/id1106971805?mt=2), [Spotify](https://open.spotify.com/show/4NhWaYYpPWgWRDAOqeRQbj), [Overcast](https://overcast.fm/itunes1106971805/the-infoq-podcast) and [YouTube](https://youtube.com/playlist?list=PLndbWGuLoHeZLVC9vl0LzLvMWHzpzIpir&si=Kvb9UpSdGzObuWgg). From this page you also have access to our recorded show notes. They all have clickable links that will take you directly to that part of the audio.

## **Previous podcasts**

*   #### Related Sponsors
    
    *   ##### [Beyond the Data Lake: Building AI-Ready Data Foundations for Agentic AI](https://www.infoq.com/vendorcontent/show.action?vcr=216a3114-ceef-4bfc-ad6a-08ec5bc8cc51&primaryTopicId=2498&vcrPlace=EMBEDDED&pageType=PODCAST_PAGE&vcrReferrer=https%3A%2F%2Fwww.infoq.com%2Fpodcasts%2Fjonas-boner-akka%2F%3Futm_source%3Demail%26utm_campaign%3Dsummerpodcast&ha=bW91c2Vtb3Zl)
        
    *   ##### [AI-Native Software Delivery - Download the eBook (By O'Reilly)](https://www.infoq.com/vendorcontent/show.action?vcr=9831f722-2945-4987-98d0-c1c46b32e5ef&primaryTopicId=2498&vcrPlace=EMBEDDED&pageType=PODCAST_PAGE&vcrReferrer=https%3A%2F%2Fwww.infoq.com%2Fpodcasts%2Fjonas-boner-akka%2F%3Futm_source%3Demail%26utm_campaign%3Dsummerpodcast&ha=bW91c2Vtb3Zl)
        
    *   ##### [AI's Physical Constraints: How AI Rewired the Data Center](https://www.infoq.com/vendorcontent/show.action?vcr=7bf8495f-cd88-40d6-92aa-1afa5ad24523&primaryTopicId=2498&vcrPlace=EMBEDDED&pageType=PODCAST_PAGE&vcrReferrer=https%3A%2F%2Fwww.infoq.com%2Fpodcasts%2Fjonas-boner-akka%2F%3Futm_source%3Demail%26utm_campaign%3Dsummerpodcast&ha=bW91c2Vtb3Zl)
        
    *   ##### [Context Lake vs. Data Lake: A New Architecture for Modern AI](https://www.infoq.com/vendorcontent/show.action?vcr=f16e12e1-ede3-457f-a37b-9d061aca4df6&primaryTopicId=2498&vcrPlace=EMBEDDED&pageType=PODCAST_PAGE&vcrReferrer=https%3A%2F%2Fwww.infoq.com%2Fpodcasts%2Fjonas-boner-akka%2F%3Futm_source%3Demail%26utm_campaign%3Dsummerpodcast&ha=bW91c2Vtb3Zl)
        
    *   ##### [\[Webinar\] Creating Certainty in the Age of Agentic AI. Watch On-Demand.](https://www.infoq.com/vendorcontent/show.action?vcr=531d8edd-4f74-486b-aaca-10058c609c1c&primaryTopicId=2498&vcrPlace=EMBEDDED&pageType=PODCAST_PAGE&vcrReferrer=https%3A%2F%2Fwww.infoq.com%2Fpodcasts%2Fjonas-boner-akka%2F%3Futm_source%3Demail%26utm_campaign%3Dsummerpodcast&ha=bW91c2Vtb3Zl)
        

### Related Content

*   Icon
    
    [![Icon image](https://imgopt.infoq.com/fit-in/50x50/filters:quality\(80\)/presentations/microservices-platform-team-topology/en/smallimage/ChrisRichardson-thumbnail-1785312644032.jpeg)](https://www.infoq.com/presentations/microservices-platform-team-topology/)
    
*   [![Icon image](https://imgopt.infoq.com/fit-in/50x50/filters:quality\(80\)/articles/pull-based-migration/en/smallimage/pull-based-migration-thumbnail-1784812950594.jpg)](https://www.infoq.com/articles/pull-based-migration/)
    

*   Icon
    
    [![Icon image](https://imgopt.infoq.com/fit-in/50x50/filters:quality\(80\)/presentations/form3-multicloud-architecture/en/smallimage/ross-mcfarlane-kevin-holditch-thumbnail-1788338652847.jpg)](https://www.infoq.com/presentations/form3-multicloud-architecture/)
    

*   Icon
    
    [![Icon image](https://imgopt.infoq.com/fit-in/50x50/filters:quality\(80\)/presentations/netflix-commerce-architecture-evolution/en/smallimage/kasia-trapszo-thumbnail-1787217920531.jpg)](https://www.infoq.com/presentations/netflix-commerce-architecture-evolution/)
    
*   Icon
    
    [![Icon image](https://imgopt.infoq.com/fit-in/50x50/filters:quality\(80\)/presentations/progressive-collapse-system-resilience/en/smallimage/sam-newman-thumbnail-1785845419904.jpg)](https://www.infoq.com/presentations/progressive-collapse-system-resilience/)
    

### Related Content

*   Icon
    
    [![Icon image](https://imgopt.infoq.com/fit-in/50x50/filters:quality\(80\)/minibooks/agentic-ai-architecture/en/smallimage/agentic-ai-architecture-thumb-image-1782836155225.jpg)](https://www.infoq.com/minibooks/agentic-ai-architecture/)
    
*   [![Icon image](https://imgopt.infoq.com/fit-in/50x50/filters:quality\(80\)/articles/rdla-offline-first-reactive-android-data-layer/en/smallimage/rdla-offline-first-reactive-android-data-layer-thumbnail-1781776366032.jpg)](https://www.infoq.com/articles/rdla-offline-first-reactive-android-data-layer/)
    
*   [![Icon image](https://imgopt.infoq.com/fit-in/50x50/filters:quality\(80\)/articles/adoption-curve-twenty/en/smallimage/20-birthday-InfoQ-thumb-image-updated-1780931679034.jpg)](https://www.infoq.com/articles/adoption-curve-twenty/)
    
*   [![Icon image](https://imgopt.infoq.com/fit-in/50x50/filters:quality\(80\)/articles/event-driven-banking-architecture/en/smallimage/event-driven-banking-architecture-thumbnail-1774430827143.jpg)](https://www.infoq.com/articles/event-driven-banking-architecture/)
    
*   Icon
    
    [![Icon image](https://imgopt.infoq.com/fit-in/50x50/filters:quality\(80\)/presentations/spritely-decentralized-architecture/en/smallimage/cd-thumbnail-1789633126216.jpg)](https://www.infoq.com/presentations/spritely-decentralized-architecture/)
    

*   Icon
    
    [![Icon image](https://imgopt.infoq.com/fit-in/50x50/filters:quality\(80\)/presentations/adaptive-recommendation-systems-architecture/en/smallimage/mallika-thumbnail-1789632229433.jpeg)](https://www.infoq.com/presentations/adaptive-recommendation-systems-architecture/)
    

*   [![Icon image](https://imgopt.infoq.com/fit-in/50x50/filters:quality\(80\)/articles/agent-harness-build-one/en/smallimage/The-Agent-Harness-What-It-Is-and-Two-Ways-to-Build-One-thumb-1789997776393.jpg)](https://www.infoq.com/articles/agent-harness-build-one/)
    

### Related Content

*   Icon
    
    [![Icon image](https://imgopt.infoq.com/fit-in/50x50/filters:quality\(80\)/presentations/llm-mobile-frontend/en/smallimage/bala-thumbnail-1789631604448.jpeg)](https://www.infoq.com/presentations/llm-mobile-frontend/)
