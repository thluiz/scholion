---
title: "Create your own AWS lambda function (Server-less)"
date: '2022-07-27T19:18:11-03:00'
category: webclip
summary: 'The page walks through creating a Hello World AWS Lambda in us-east-1 with Node.js 14.x, then deploying and testing a handler that returns a JSON response with statusCode, body, and headers.'
tags: ["aws-lambda", "serverless", "nodejs", "api-gateway"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Create your own AWS lambda function (Server-less) | by Vikash Kumar | Jun, 2022 | AWS Tip"
    url: "https://awstip.com/create-your-own-aws-lambda-function-server-less-11c855d8e310"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2022-07/awstip-com--create-your-own-aws-lambda-function-serverless.md"
    kind: repo
---

The page shows how to create a Hello World AWS Lambda function in the AWS Console. It uses the us-east-1 region, chooses the Lambda service, sets the runtime to Node.js 14.x, and deploys a handler from index.js inside the HelloWorld folder.

The sample handler logs functionName, memoryLimitInMB, and the remaining execution time, then builds a todo object with id, description, and isDone fields. It returns a JSON response with statusCode, body, and headers, and the page says this response will be mapped to API Gateway later.

## Reading notes

- Select us-east-1 as the region for the lab resources.
- In the AWS Console, open Lambda from the Services menu and create a function.
- Set the runtime to Node.js 14.x and keep the other options as defaults.
- In the source code screen, open index.js under HelloWorld.
- The handler logs functionName, memoryLimitInMB, and remaining time.
- The response object includes statusCode, body, and headers.
- The body is created from a todo object with id 100, description, and isDone set to false.
- Deploy the function and test it with a new hello-world test event.
- The JSON response is meant to be mapped to the REST API response from API Gateway.
