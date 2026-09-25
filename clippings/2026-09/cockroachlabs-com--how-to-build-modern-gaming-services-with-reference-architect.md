---
url: "https://www.cockroachlabs.com/blog/how-to-build-modern-gaming-services-with-reference-architecture/"
captured_at: "2026-09-25T21:59:23+01:00"
title: "How to build modern gaming services — with reference architecture"
domain: "cockroachlabs-com"
---

Let game developers develop games. It doesn’t exactly sound revolutionary.

But back in the day, that’s not always how things worked. Every game had its own systems for things like stat tracking, item purchases, user entitlements (in-game items a user has purchased or unlocked), and game devs often got bogged down building bespoke functionality into each of their games to handle these user features.

These days, that approach is a thing of the past. Developers both large and small have realized that games largely have the same “plumbing,” and there’s no reason to rebuild these systems again and again for every new game. Instead, game development has largely separated into two camps:

1.  The artists and developers creating the actual game content
    
2.  The backend developers building those plumbing services
    

This shift has made development more efficient, especially for big shops that can dedicate a backend team to building services that can be called by all of the different games they publish.

But this shift has also introduced challenges for the people attempting to architect those backend services. A social service that’s going to be called by a dozen different games in countries all over the world has dramatically different requirements for consistency, availability, and scaling than the single-game backends game developers built in the old days.

Building out a services architecture that can stand up to the requirements of the modern gaming industry is no easy task. Let’s take a closer look at what’s required.

## Requirements and challenges for building video game architecture![Copy Icon](https://www.cockroachlabs.com/images/icons/copy-icon.svg)

Modern gaming is global. Gamers expect a consistent, low-latency experience, and they can be more demanding than users in some other industries. While a short outage at 3 AM might be no problem for some SaaS products, for example, if you’re running a competitive multiplayer game and that happens, your support team is going to [have an inbox full of angry messages](https://www.forbes.com/sites/mattgardner1/2021/09/22/online-gaming-is-the-worst-for-downtime-with-one-runaway-culprit/?sh=72d0669313f3) the next morning.

Whether you’re a major developer or an indie studio, modern gaming demands a back-end architecture that can deliver on the following things:

### 1\. Near-instant consistency![Copy Icon](https://www.cockroachlabs.com/images/icons/copy-icon.svg)

Many modern games contain some form of microtransactions, and virtually all of them contain player entitlements such as in-game items a player has unlocked. In both cases, consistency is critical, and it has to be both immediate and global. If a player purchases or unlocks an item, they will expect to be able to use it immediately, and they will expect it to be available regardless of where they’re logging in from.

This rules out approaches based on eventual consistency or active-passive replication. For example when a player unlocks or purchases an item, if your backend system is writing to a database node in us-east-1 but the player’s located in us-west-1, when they try to view or use the item right after unlocking it, they may not see it right away. This results in poor user experience, and frustrated players. The game client can be coded to work around this such that it knows it has to query only us-east-1 every time. But this requires building complex “location aware” plumbing into the game code, which slows down developers and can cause regional imbalances and single-points-of-failure issues.

### 2\. Resilient availability![Copy Icon](https://www.cockroachlabs.com/images/icons/copy-icon.svg)

As previously mentioned, gamers are _not_ big fans of outages, especially when they’re unplanned. Any kind of interruption to your game is going to make players annoyed. If any data loss occurs during an outage – say, they unlock an item while the entitlements service is down and their unlock is never written to the database – they’re going to be _furious_. So, a highly available backend with [an RPO of zero](https://www.cockroachlabs.com/blog/demand-zero-rpo/) is critical.

Modern service-based gaming backend architecture also raises the stakes here for larger gaming companies, because any interruption to a service will impact _all_ of the games that call that service. If entitlements go down in one of your games, that’s bad enough, but if they go down in _all_ of your games, that’s a potential catastrophe.

Designing a system that can deliver very high availability and zero data loss is therefore critical.

### 3\. Elastic scalability![Copy Icon](https://www.cockroachlabs.com/images/icons/copy-icon.svg)

Gaming workloads are rarely the same from day to day. Companies release new games all the time, and any game could go viral at a moment’s notice, causing massive user spikes that your system has to be able to handle without degrading performance. They also often have to support numerous older games as the playerbase slowly dwindles, requiring architecture that can scale down smoothly, too.

For this reason, most modern gaming backends are architected on Kubernetes to facilitate automated elastic scaling to meet demand. Pods and containers can be added and removed automatically to match demand as it ebbs and flows. Databases associated with the various game services also need to be able to scale in this manner, and because these services are generally being developed on Kubernetes anyway, working with a database that’s easy to deploy and operate within a k8s environment makes sense.

### 4\. Low latency![Copy Icon](https://www.cockroachlabs.com/images/icons/copy-icon.svg)

One of the best ways to reduce latency for any type of user is to locate as many of your services as possible somewhere that is geographically close to them. That, of course, is easier said than done. Delivering a smooth, low-latency experience will require a multi-region setup for all of your services _and_ for the database or databases that serve them – the latency advantage of having an entitlements service container on us-west-1 for gamers in California is somewhat nullified if that service still has to write to a centralized database or node that’s not in us-west-1.

### 5\. Minimal complexity![Copy Icon](https://www.cockroachlabs.com/images/icons/copy-icon.svg)

Obviously, meeting the previous four standards requires complexity. But to the extent that it’s possible, a great back-end for gaming should aim for simplicity by doing things like:

*   Choosing tools that can handle scaling (horizontally) and multi-region inherently, rather than having to build those capabilities yourself.
    
*   Choosing tools that work well with the systems and languages your team already knows to minimize any learning curve.
    
*   Choosing managed cloud services where budget allows to remove the burden of some maintenance and operations work from your team and allowing them more time to focus on building the game.
    

## A general reference architecture for gaming![Copy Icon](https://www.cockroachlabs.com/images/icons/copy-icon.svg)

What does all of that actually look like in practice? Here’s one simple example of how a modern gaming backend architecture could look.

[![gaming-reference-architecture-microservices](https://images.ctfassets.net/00voh0j35590/6pWXZGTsJClJxup9MvnNBC/0a5e1dfe64d4aa1074cbce48888a37ca/gaming-reference-architecture-microservices.jpg)](https://images.ctfassets.net/00voh0j35590/6pWXZGTsJClJxup9MvnNBC/0a5e1dfe64d4aa1074cbce48888a37ca/gaming-reference-architecture-microservices.jpg)

Note that this diagram has been simplified to make it easier to understand; a real-world system would include many game clients and servers, and almost certainly more than just four back-end services. The overall principle, though, is sound – leveraging Kubernetes within the public cloud of your choice, you can build your application logic into game servers that call game services, leveraging infrastructure as code (IaC) tools to add or remove containers and pods as needed.

These services, then, read and write from a distributed database that can be easily deployed within Kubernetes. CockroachDB is the obvious choice here, as it ticks all of the requirements outlined in the previous section. It offers:

*   **Ironclad consistency** thanks to ACID transactional guarantees _without_ the ikelihood of data loss during failures inherent in active-passive setups. CockroachDB uses [a setup we call multi-active to provide consistency and high availability](https://www.cockroachlabs.com/docs/stable/multi-active-availability#what-is-multi-active-availability).
    
*   **Very high availability and zero RPO**, again due to its distributed nature and cross-region or cross-zone multi-active approach.
    
*   **Elastic scalability**, as node addition and decommissioning can be automated for CockroachDB Dedicated deployments (and all scaling is automated by the database itself for [serverless deployments](https://www.cockroachlabs.com/blog/announcing-cockroachdb-serverless/)).
    
*   **Low latency** thanks to built-in multi-region capability that can be as fine-grained as you need (even down to the row level).
    
*   **Minimal complexity** thanks to the fact that it uses familiar SQL, was built to work smoothly within Kubernetes, and can be treated as a single logical database by your application and services even in the case of complex multi-region deployments.
    

Speaking of multi-region…

## Multi-region reference architecture – video games at global scale![Copy Icon](https://www.cockroachlabs.com/images/icons/copy-icon.svg)

Here’s how that same sort of architecture can look when deployed globally in a multi-region setup.

[![gaming-reference-architecture-multi-region](https://images.ctfassets.net/00voh0j35590/1GAIIQGiliXPZExzK78iUE/fbf590f9cb8897ef5c74472254603837/gaming-reference-architecture-multi-region.jpg)](https://images.ctfassets.net/00voh0j35590/1GAIIQGiliXPZExzK78iUE/fbf590f9cb8897ef5c74472254603837/gaming-reference-architecture-multi-region.jpg)

The key takeaway here is that even in a multi-region setup, your application can treat any CockroachDB database you have as a single logical database. In other words, the database itself can handle storing data in the correct places and routing queries to the correct replicas to minimize latency for users, whereas with most other databases you’d have to write all of that complexity into your application logic (and then maintain all of that code as your deployment grows and changes).

Want to learn more about CockroachDB and how it can power the next generation of gaming services? [**Read up on how DevSisters scaled up Cookie Run Kingdom using CockroachDB.**](https://www.cockroachlabs.com/customers/devsisters/)
