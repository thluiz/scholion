---
title: "Let’s go Serverless"
date: '2022-07-22T16:50:44-03:00'
category: webclip
summary: 'The page shows a simple serverless setup with API Gateway, Lambda, DynamoDB, S3, SNS, and SQS. A POST request is scanned, stored, logged, and failures are sent to a queue for later handling.'
tags: ["serverless", "aws-lambda", "api-gateway", "dynamodb"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Let’s go Serverless.. Opting for a serverless architecture… | by Asna Siji | Jun, 2022 | AWS Tip"
    url: "https://awstip.com/lets-go-serverless-b56da97b8bb6"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2022-07/awstip-com--lets-go-serverless-aws-tip.md"
    kind: repo
---

The article defines serverless as a cloud-native execution model where the provider allocates resources dynamically, with automatic scaling, high availability, and pay-per-use billing. It then outlines a small architecture that receives a text document through API Gateway, processes it in Lambda, stores extracted details in DynamoDB, saves the received message in S3, and sends failures to SNS and SQS.

## Reading notes

- Serverless reduces management and administration overhead, but it still uses servers managed by the cloud provider.
- The described setup uses API Gateway, Lambda, DynamoDB, and S3 for the main flow.
- A URL endpoint receives a small text document over REST and HTTPS.
- Lambda scans the message, extracts document details, and saves them in DynamoDB.
- The full received message is logged in S3 for later reference.
- Errors during processing are published to an SNS topic.
- An SQS queue subscribes to that topic so error messages can be polled later.
- The Lambda execution role needs access to S3, DynamoDB, CloudWatch, and SNS.
- Environment variables store the extraction parameters used by the function.
- The function accepts HTTP POST and returns an error for other request methods.
- The article notes that API Gateway-triggered Lambda does not use asynchronous Destinations, so failures are pushed to SNS in code.
- Testing shows successful writes to S3 and DynamoDB, and a PUT request produces an error message that appears in SQS.
