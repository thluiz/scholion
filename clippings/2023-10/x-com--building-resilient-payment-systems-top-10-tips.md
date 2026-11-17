---
url: "https://x.com/milan_milanovic/status/1683357943037657090"
captured_at: "2023-10-24T14:26:38+00:00"
title: "Thread by @milan_milanovic: 𝗕𝘂𝗶𝗹𝗱𝗶𝗻𝗴 𝗥𝗲𝘀𝗶𝗹𝗶𝗲𝗻𝘁 𝗣𝗮𝘆𝗺𝗲𝗻𝘁 𝗦𝘆𝘀𝘁𝗲𝗺𝘀 The recent article by Shopify Engineering explained the…"
domain: "x-com"
---

Thread by Dr Milan Milanović (@milan_milanovic), 2 tweets.

## 1/2

𝗕𝘂𝗶𝗹𝗱𝗶𝗻𝗴 𝗥𝗲𝘀𝗶𝗹𝗶𝗲𝗻𝘁 𝗣𝗮𝘆𝗺𝗲𝗻𝘁 𝗦𝘆𝘀𝘁𝗲𝗺𝘀

The recent article by Shopify Engineering explained the top 10 most useful tips and tricks for building resilient payment systems.

Here is the list:

𝟭. 𝗟𝗼𝘄𝗲𝗿 𝗬𝗼𝘂𝗿 𝗧𝗶𝗺𝗲𝗼𝘂𝘁𝘀: They suggest investigating and setting low timeouts everywhere possible. For instance, Ruby's built-in Net::HTTP client has a default timeout of 60 seconds to open a connection, write data, and read a response. This is too long for online applications where a user is waiting.

𝟮. 𝗜𝗻𝘀𝘁𝗮𝗹𝗹 𝗖𝗶𝗿𝗰𝘂𝗶𝘁 𝗕𝗿𝗲𝗮𝗸𝗲𝗿𝘀: Circuit breakers, like Shopify's Semian, protect services by raising an exception once a service is detected as being down. This saves resources by not waiting for another timeout.

𝟯. 𝗨𝗻𝗱𝗲𝗿𝘀𝘁𝗮𝗻𝗱 𝗖𝗮𝗽𝗮𝗰𝗶𝘁𝘆: The author discusses Little's Law, which states that the average number of customers in a system equals their average arrival rate, multiplied by their average time. Understanding this relationship between queue size, throughput, and latency can help design systems that can handle load efficiently.

𝟰. 𝗔𝗱𝗱 𝗠𝗼𝗻𝗶𝘁𝗼𝗿𝗶𝗻𝗴 𝗮𝗻𝗱 𝗔𝗹𝗲𝗿𝘁𝗶𝗻𝗴: Google's site reliability engineering (SRE) book lists four golden signals a user-facing system should be monitored for latency, traffic, errors, and saturation. Monitoring these metrics can help identify when a system is at risk of going down due to overload.

𝟱. 𝗜𝗺𝗽𝗹𝗲𝗺𝗲𝗻𝘁 𝗦𝘁𝗿𝘂𝗰𝘁𝘂𝗿𝗲𝗱 𝗟𝗼𝗴𝗴𝗶𝗻𝗴: They recommend using structured logging in a machine-readable format.

𝟲. 𝗨𝘀𝗲 𝗜𝗱𝗲𝗺𝗽𝗼𝘁𝗲𝗻𝗰𝘆 𝗞𝗲𝘆𝘀: To ensure payment or refund happens exactly once, they recommend using Idempotency keys, which track attempts and provide only a single request is sent to financial partners.

𝟳. 𝗕𝗲 𝗖𝗼𝗻𝘀𝗶𝘀𝘁𝗲𝗻𝘁 𝗪𝗶𝘁𝗵 𝗥𝗲𝗰𝗼𝗻𝗰𝗶𝗹𝗶𝗮𝘁𝗶𝗼𝗻: Reconciliation ensures that records are consistent with those of financial partners. Any discrepancies are recorded and automatically remediated where possible.

𝟴. 𝗜𝗻𝗰𝗼𝗿𝗽𝗼𝗿𝗮𝘁𝗲 𝗟𝗼𝗮𝗱 𝗧𝗲𝘀𝘁𝗶𝗻𝗴: Regular load testing helps test systems limits and protection mechanisms by simulating large-volume flash sales. Shopify uses scriptable load balancers to throttle the number of checkouts happening at any time.

𝟵. 𝗚𝗲𝘁 𝗼𝗻 𝗧𝗼𝗽 𝗼𝗳 𝗜𝗻𝗰𝗶𝗱𝗲𝗻𝘁 𝗠𝗮𝗻𝗮𝗴𝗲𝗺𝗲𝗻𝘁: Shopify uses a Slack bot to manage incidents, with roles for coordinating the incident, public communication, and restoring stability. This process starts when the on-call service owners get paged, either by an automatic alert based on monitoring or by hand, if someone notices a problem.

𝟭𝟬. 𝗢𝗿𝗴𝗮𝗻𝗶𝘇𝗲 𝗜𝗻𝗰𝗶𝗱𝗲𝗻𝘁 𝗥𝗲𝘁𝗿𝗼𝘀𝗽𝗲𝗰𝘁𝗶𝘃𝗲𝘀: Retrospective meetings are held within a week after an incident to understand what happened, correct incorrect assumptions, and prevent the same thing from happening again.

#technology #softwareengineering #programming #techworldwithmilan #distributedsystems

![image](https://pbs.twimg.com/media/F1x9FCfX0AINxog?format=jpg&name=orig)

([tweet](https://x.com/milan_milanovic/status/1683357943037657090), 2023-07-24 06:06 UTC)

## 2/2

If you want to learn more about it, subscribe to my newsletter: 
https://
newsletter.techworld-with-milan.com.

Links: https://t.co/q02IQfGGH8

Card: https://t.co/q02IQfGGH8

([tweet](https://x.com/milan_milanovic/status/1683358073040130049), 2023-07-24 06:06 UTC)
