---
title: "No, AWS, Aurora Serverless v2 Is Not Serverless"
date: '2022-06-24T11:49:38-03:00'
category: webclip
summary: 'The post argues that Aurora Serverless v2 keeps charging for idle capacity, so it behaves like auto-scaling rather than serverless. The name is misleading for users, costs, and cloud terminology.'
tags: ["aws", "serverless", "aurora", "costs"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "No, AWS, Aurora Serverless v2 Is Not Serverless - Last Week in AWS Blog"
    url: "https://www.lastweekinaws.com/blog/no-aws-aurora-serverless-v2-is-not-serverless/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2022-06/lastweekinaws-com--no-aws-aurora-serverless-v2-is-not-serverless.md"
    kind: repo
---

The post argues that Aurora Serverless v2 is not serverless in the usual sense because it stays at 0.5 ACU when idle instead of pausing or scaling to zero. That means it can keep generating costs even when an application is not being used.

It also says the term is misleading because serverless is commonly understood as pay-as-you-go with no idle charges. The post extends the criticism to other AWS services that use the same label while still billing for baseline capacity, and suggests that Aurora Serverless v2 is better described as auto-scaling.

## Reading notes

- Aurora Serverless v2 is marketed as highly scalable, highly available, and fully managed, but the post says it does not behave as serverless because it does not suspend itself.
- The pricing model charges for Aurora Capacity Unit hours, with a starting capacity of 0.5 ACU.
- A test mentioned in the post found that the database scales down to 0.5 ACU when unused and stays there.
- The post contrasts Aurora with API Gateway and Lambda, which would cost $0.00 after a month of no use, while Aurora would still cost money.
- The author defines serverless as avoiding concern about scaling, configuration, management, and maintenance of underlying servers or containers.
- The post also ties serverless to pay-as-you-go pricing and no cost during idle time.
- It argues that true serverless matters because it keeps development environments cheap and close to production.
- The post says naming this kind of service serverless misleads newer users and adds confusion in the cloud community.
- It calls Aurora Serverless v2 auto-scaling rather than serverless.
- The post extends the same criticism to Amazon MSK and Amazon Kinesis Data Streams, which also use the serverless label while still charging for baseline usage.
