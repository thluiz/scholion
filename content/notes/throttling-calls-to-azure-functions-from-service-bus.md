---
title: "Throttling Calls to Azure Functions from Azure Service Bus"
date: '2022-03-17T12:17:09-03:00'
category: webclip
summary: 'The post shows that Azure Functions triggered from Service Bus can be throttled by setting maxConcurrentCalls in host.json, limiting concurrent executions without custom sleep logic.'
tags: ["azure-functions", "service-bus", "serverless"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Throttling Calls to Azure Functions from Azure Service Bus | Blog"
    url: "https://ballardchalmers.com/2019/02/07/throttling-calls-azure-functions-service-bus/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2022-03/ballardchalmers-com--throttling-calls-to-azure-functions-from-service-bus.md"
    kind: repo
---

The post explains that Azure Functions triggered from Service Bus can be throttled with the maxConcurrentCalls setting in host.json. That setting limits how many function instances run at once, which can help keep SQL Database load and costs under control when queued work can take longer.

## Reading notes

- The author says the main benefit of Azure serverless is not having to think about scaling most of the time, but sometimes costs or database load still need to be limited.
- The example problem is function calls running reports against SQL Database, where too many concurrent calls could force the database to scale up.
- Rather than adding custom sleeps and pauses in the function, the Service Bus trigger already supports a concurrency limit through host.json.
- The maxConcurrentCalls property under the Service Bus section sets how many functions run at the same time.
- The author tested this with a function that writes a queue message GUID into a FunctionsLog table, marks it Started, waits a random 1 to 60 seconds, then updates it to Completed.
- A test created 10 queue messages in sequence.
- In the results, only two entries were ever in Started status at the same time.
- The Azure Portal also showed the 10 Service Bus messages being logged.
- The post closes by saying that different priorities could be handled with multiple queues, or by moving messages to another queue based on priority.
