---
url: "https://www.lastweekinaws.com/blog/no-aws-aurora-serverless-v2-is-not-serverless/"
captured_at: "2022-06-24T11:49:38-03:00"
title: "No, AWS, Aurora Serverless v2 Is Not Serverless - Last Week in AWS Blog"
domain: "lastweekinaws-com"
---

# No, AWS, Aurora Serverless v2 Is Not Serverless

[By Maciej Radzikowski](https://www.lastweekinaws.com/blog/author/maciejradzikowski-com-pl/)

The freshly released Amazon Aurora Serverless v2 is a highly scalable, highly available, fully managed SQL database.  If only it were serverless. How AWS prices Aurora Serverless v2 When AWS released Aurora…

[Home](https://www.lastweekinaws.com/) [Blog](https://www.lastweekinaws.com/blog/) No, AWS, Aurora Serverless v2 Is Not Serverless

[Prev](https://www.lastweekinaws.com/blog/the-strange-too-familiar-tale-of-uncle-suitcase/)

[Next](https://www.lastweekinaws.com/blog/reinvent-keynote-incident/)

The freshly released Amazon Aurora Serverless v2 is a highly scalable, highly available, fully managed SQL database.

If only it were serverless.

## How AWS prices Aurora Serverless v2

When AWS released Aurora Serverless v2 as generally available on April 21, I had to double-check the date. No, it was too late for April Fool’s.

It was true. Aurora Serverless v2’s GA release, which no one actually expected anymore, came only a year and a half after it was announced at re:Invent 2020.

But my joy was only temporary.

A quick look at [the pricing page](https://aws.amazon.com/rds/aurora/pricing/) reveals that you pay for Aurora Capacity Unit hours, with starting capacity set at 0.5 ACU. Wait: Does “starting” mean “minimum” here? Would Aurora still pause or scale down to 0 ACU if it’s not in use?

When in doubt, always consult ~~documentation~~ Twitter. The Aurora Serverless v2 release was the topic of the day in the AWS and serverless world, and it didn’t take long for someone to test it. Matthieu Napoli made a simple test to find the answer.

> Will Aurora Serverless v2 actually suspend itself after a while? If so, what would the DB cold start look like?  
> Hold my Lambda, I’m going in… [pic.twitter.com/L8JBj0xJEb](https://t.co/L8JBj0xJEb)
>
> — Matthieu Napoli (@matthieunapoli) [April 22, 2022](https://twitter.com/matthieunapoli/status/1517443082358251521?ref_src=twsrc%5Etfw)

The test results are conclusive. When not used, Aurora Serverless v2 scales down to 0.5 ACU and stays there. It does not suspend or pause itself.

## Why it’s a problem that Aurora doesn’t scale down to 0

Aurora Serverless v2 should be, well, *serverless*. It’s in the name, so you have the right to assume it is.

If you create an API Gateway with Lambda function and Aurora Serverless v2 in the us-east-1 region and never call the API, after a month, you would pay:

- **$0.00** for the API Gateway.
- **$0.00** for the Lambda.
- **$43.20** for the Aurora.

I bet you can spot the outlier here.

## What is serverless, really?

Everyone agrees that serverless infrastructure means you shouldn’t have to worry about scaling, configuration, management, or maintenance of underlying servers or containers.

But how do you define serverless pricing? Does serverless also mean pay as you go, with no minimum charges for when you don’t actually use the infrastructure?

[Wikipedia](https://en.wikipedia.org/wiki/Serverless_computing) tells you that “when an app is not in use, there are no computing resources allocated to the app” with serverless.

AWS Blog shares that one of the benefits of [serverless microservices](https://aws.amazon.com/blogs/industries/how-sgk-reduced-operating-costs-by-83-with-noops-serverless-microservices/) is that “you pay for only what you use and only when you use it; there is no cost during idle time with serverless architectures.” And that [serverless is the way of the future](https://aws.amazon.com/blogs/publicsector/scaling-zero-serverless-way-future-university-of-york/) because you have “the ability to scale down to zero, which helps … better manage applications, reduce costs, and increase agility.”

And if you ask people on Twitter, a [majority of them say](https://twitter.com/JannikWempe/status/1517227391009140736) they expect serverless services to scale down to zero. Various [people who know a thing or two](https://twitter.com/jeremy_daly/status/1517634070145949696) about serverless articulate the problem as well.

The promise of serverless includes pay-as-you-go pricing. It does not include paying for resources waiting to be used.

## Why we need true serverless

In serverless, it’s critical not to pay for idle resources.

A pay-as-you-go serverless model empowers innovation without much risk and allows for high development velocity.

To enable it, developers work on their own environments deployed to AWS, as similar to production as possible. With serverless, the cost of running multiple instances of the whole application should be close to zero, whether it’s one per developer or one per feature branch. Those are environments with barely any traffic.

If the pay-as-you-go pricing promise is broken, the costs of development environments increases. While not scaling down to zero on production environments is rarely a problem for big players, individual developers and small startups may feel it. This would lead them to look for cost savings, like sharing resources that should be separate instances. Such workarounds impact delivery speed in two ways. First, developers spend time creating workarounds instead of delivering product value. Second, combining instances moves the development architecture further away from the production one, increasing the chances of bugs and deployment problems.

There’s also the sales case for serverless. I can’t overemphasize how wonderful the phrase “you only pay when people use it” works on a company’s business people. Push the people making decisions to question the pricing, and we’re back to server request forms.

## Aurora Serverless v2 is auto-scaling, not serverless

The term best describing the offering of Aurora Serverless v2 is “auto-scaling,” which isn’t nearly as trendy or as hyped as “serverless.” But naming it “Aurora Auto-Scaling v2” would actually be accurate.

Calling things serverless when they cost money to run — even when they’re not in use — leads to two problems.

**1. It’s misleading for new and less-experienced users.**

It’s not difficult to imagine a student launching a database with “serverless” in the name and forgetting about it after completing the semester project. They say life is the best teacher, but does it really have to come with an AWS bill for something you don’t use?

There are enough [misunderstandings with AWS Free Tier](https://www.lastweekinaws.com/blog/is-the-aws-free-tier-really-free/) and people assuming they won’t get billed, [only to be surprised](https://www.lastweekinaws.com/blog/its-time-to-rethink-the-aws-free-tier/). Naming such a service “serverless” is the same kind of a false promise.

**2. It introduces confusion in the cloud community.**

If a term is ambiguous, it loses its meaning in the long run. If you see a service advertised as “serverless” but need to read all the details to know how you’d be billed for usage, the term itself doesn’t bring any value.

![PPyJCA9PzTev1TIFx8L2fLc4VnLnkjmPxKX8jej7qOfL0Ux91IaKlts5_Q-8gMXa2SYSm6FXYANwyfXiKX6qlKOaxXwn0oc8wjVuOqv6EIeYO6B8wCT8triEYFjFF_5PS21Loum6Q-1dcaeZew](lastweekinaws-com--no-aws-aurora-serverless-v2-is-not-serverless/1d379c132a56fe8d0b7d7d9466ea6d18.png)

Communication isn’t easier either. Your colleague suggesting that you “use service X for this; it’s serverless” means nothing about the character of the service. Instead, “what *is* serverless?” becomes a thing to argue on Twitter, exactly like “cloud native.”

## AWS, stop misleading with the ‘serverless’ descriptor

Unfortunately, Aurora Serverless v2 is only the latest not-exactly-serverless-but-let’s-name-it-serverless offering.

Amazon MSK, the managed Apache Kafka solution, just released [a serverless version](https://aws.amazon.com/msk/features/msk-serverless/) as well. In addition to storage, data-in charges, and data-out charges, you pay for cluster hours and partition hours. As a result, in the us-east-1 region, you spend $558 per month for the cluster’s bare existence.

Amazon Kinesis Data Streams is another example. On the [product page](https://aws.amazon.com/kinesis/data-streams/), it’s described as “a serverless streaming data service that makes it easy to capture, process, and store data streams at any scale.” However, in the on-demand mode that was released during the last re:Invent, you pay $28.80 per month per stream, in addition to usage costs.

It’s almost three times more than you pay for a single-shard stream in provisioned mode. I work in Big Data projects, where I highly utilize Kinesis in development environments. Imagine my disappointment when I realized a low-usage Kinesis stream costs me *even more* on demand.

Funnily enough, there are a whole bunch of machine learning services with pay-as-you-go pricing that are not described as serverless: Amazon Comprehend, Amazon Forecast, Amazon Lex, Amazon Rekognition, Amazon Textract, Amazon Transcribe, Amazon Translate, and Amazon Polly, to name a few.

Don’t get me wrong. I fully appreciate the incredible AWS engineers that created an auto-scaled SQL database. I recognize this is a huge thing for applications with a varied workload. My only issue here lies in its naming.

AWS, I’m waiting for you to stop abusing the “serverless” term.
