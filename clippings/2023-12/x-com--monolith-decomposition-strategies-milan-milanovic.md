---
url: "https://x.com/milan_milanovic/status/1731263367854047301"
captured_at: "2023-12-04T10:03:58+00:00"
title: "Thread by @milan_milanovic: 𝗠𝗼𝗻𝗼𝗹𝗶𝘁𝗵 𝗗𝗲𝗰𝗼𝗺𝗽𝗼𝘀𝗶𝘁𝗶𝗼𝗻 𝗦𝘁𝗿𝗮𝘁𝗲𝗴𝗶𝗲𝘀 We have three types of monoliths. In 𝘁𝗿𝗮𝗱𝗶𝘁𝗶𝗼𝗻𝗮𝗹 ones, w…"
domain: "x-com"
---

Thread by Dr Milan Milanović (@milan_milanovic), 2 tweets.

## 1/2

𝗠𝗼𝗻𝗼𝗹𝗶𝘁𝗵 𝗗𝗲𝗰𝗼𝗺𝗽𝗼𝘀𝗶𝘁𝗶𝗼𝗻 𝗦𝘁𝗿𝗮𝘁𝗲𝗴𝗶𝗲𝘀

We have three types of monoliths. In 𝘁𝗿𝗮𝗱𝗶𝘁𝗶𝗼𝗻𝗮𝗹 ones, we have everything bundled together in a layered form. We have also 𝗺𝗼𝗱𝘂𝗹𝗮𝗿 𝗺𝗼𝗻𝗼𝗹𝗶𝘁𝗵𝘀, where we have defined functional boundaries and dependencies, but still single deployment. And we have 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲𝗱 𝗺𝗼𝗻𝗼𝗹𝗶𝘁𝗵𝘀 which are built like monoliths but deployed similarly to microservices. Here, we have the worst of both worlds: tightly coupled services with the complexity of microservices. We usually get here by 𝗱𝗲𝘃𝗲𝗹𝗼𝗽𝗶𝗻𝗴 𝗺𝗶𝗰𝗿𝗼𝘀𝗲𝗿𝘃𝗶𝗰𝗲 𝗮𝗿𝗰𝗵𝗶𝘁𝗲𝗰𝘁𝘂𝗿𝗲 𝘄𝗿𝗼𝗻𝗴𝗹𝘆.

So, to fix this, we need to do some kind of 𝗺𝗼𝗻𝗼𝗹𝗶𝘁𝗵 𝗱𝗲𝗰𝗼𝗺𝗽𝗼𝘀𝗶𝘁𝗶𝗼𝗻𝘀. There are a few approaches that can help here:

𝟭. 𝗦𝘁𝗿𝗮𝗻𝗴𝗹𝗲𝗿 𝗙𝗶𝗴 𝗣𝗮𝘁𝘁𝗲𝗿𝗻

The Strangler Fig Pattern (Coined by Martin Fowler) comes from a collection of plants that grow by "strangling" their hosts. This pattern enables the replacement of specific functionality with new services. Here, we create a façade that intercepts requests going to the monolith and routes these requests to the monolith or new services. And we gradually migrate old functionality to new services, yet consumers always hit the façade.

Here, you can also use 𝗗𝗼𝗺𝗮𝗶𝗻-𝗗𝗿𝗶𝘃𝗲𝗻 𝗗𝗲𝘀𝗶𝗴𝗻 (𝗗𝗗𝗗) to incrementally refactor the application into more minor services, where you first find ubiquitous languages (common vocabulary) between all stakeholders, then identify relevant modules to apply this vocabulary to them and define domain models of the monolithic application. In the last step, you define bounded contexts for the models, which are boundaries within a domain. 

𝟮. 𝗕𝗿𝗮𝗻𝗰𝗵 𝗯𝘆 𝗮𝗯𝘀𝘁𝗿𝗮𝗰𝘁𝗶𝗼𝗻

With this approach, we create an abstraction layer over our original component so that we can replace it step by step. Client requests are directed to this layer, allowing us to change everything behind it. The client will hit only the new component when we finish the changes. With this pattern, we can coexist two implementations of the same functionality, which is the true Liskov substitution principle. Although, like the Strangler Fig pattern, with this one, we are working on a bit lower level of abstraction, where our focus is more on components than on the systems.

If you're interested in this approach, I recommend the book "𝗠𝗼𝗻𝗼𝗹𝗶𝘁𝗵 𝘁𝗼 𝗠𝗶𝗰𝗿𝗼𝘀𝗲𝗿𝘃𝗶𝗰𝗲𝘀" by Sam Newman. 

#softwarearchitecture

![image](https://pbs.twimg.com/media/GAauz8uW8AAPTn9?format=jpg&name=orig)

([tweet](https://x.com/milan_milanovic/status/1731263367854047301), 2023-12-03 10:45 UTC)

## 2/2

To expand your knowledge and personal growth, subscribe to my free weekly newsletter with 19,000+ people: 
https://
newsletter.techworld-with-milan.com.

Links: https://t.co/MMCXxQQR4F

([tweet](https://x.com/milan_milanovic/status/1731263425865502910), 2023-12-03 10:45 UTC)
