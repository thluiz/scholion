---
title: "Why I Migrated My Laravel App to AWS Serverless"
date: '2025-02-05T16:51:07+00:00'
category: webclip
summary: 'Author explains migrating a Laravel app from EC2 to AWS serverless, detailing cost savings, scaling and maintenance benefits, tradeoffs, and when serverless Laravel fits or not.'
tags: ["laravel", "aws-serverless", "cloud-architecture", "cost-optimization"]
has_commentary: false
generated_by: "openai/gpt-5.1"
sources:
  - title: "HDS Solutions - Desarrollo de Soluciones Digitales"
    url: "https://hds-solutions.net/blog/2025-01-27-why-i-migrated-my-laravel-app-to-aws-serverless"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/hds-solutions-net--why-i-migrated-my-laravel-app-to-aws-serverless.md"
    kind: repo
---

The author describes moving a Laravel application from EC2-based hosting to AWS serverless, after struggling with underutilized instances, scaling complexity, and unwanted DevOps work. By adopting Lambda and managed AWS services, they cut monthly infrastructure costs from about $110 to $34, gained automatic scaling, and offloaded most maintenance. The article outlines how Laravel must be adapted for stateless, event-driven execution and clarifies that serverless is powerful but not ideal for every workload.

## Reading notes

- The initial Laravel deployment ran on EC2, with the app often idle while still incurring continuous costs for instances, load balancer, and shared storage.
- As a solo developer, the author found ~$110/month significant for infrastructure that was mostly underused.
- Autoscaling on EC2 required manual tuning of scaling groups and load balancers and felt like an extra job to manage.
- Traditional hosting forced the author into sysadmin tasks such as applying security patches, debugging web server configs, and handling `sudo` issues.
- Exploring alternatives led them to serverless as a way to relieve cost, scaling, and maintenance pain points.
- The author clarifies that serverless still uses servers but shifts responsibility for them to AWS so they can focus on coding.
- AWS Lambda executes code only in response to events like HTTP requests, SQS messages, or scheduled jobs, then shuts down afterward.
- Lambda’s billing model charges only for execution time in milliseconds, avoiding charges for idle capacity.
- Lambda automatically scales to handle large request spikes, such as 100,000 requests, without manual intervention.
- Lambda’s stateless design encourages modular architecture and avoids relying on local state between requests.
- Serverless architectures use an ecosystem of managed services, including Aurora Serverless for SQL databases, S3 for file storage, and SQS for decoupled asynchronous processing.
- PHP and Laravel were not originally designed for Lambda’s environment, so adjustments are needed for sessions, storage, queues, caching, and configuration.
- To work on Lambda, Laravel sessions must be stored in external systems like MySQL or Redis instead of the filesystem.
- File operations must be redirected to S3 through Laravel’s Storage facade so the app does not rely on local disk.
- Queues should use SQS as the driver for asynchronous jobs in a serverless context.
- Caching must be moved to external services like Redis or DynamoDB instead of using local storage.
- The author recommends trimming unused dependencies and optimizing boot time to reduce Lambda cold starts.
- Environment configuration should use AWS Secrets Manager or Parameter Store rather than `.env` files on disk.
- The article stresses that adopting serverless requires rethinking architecture so AWS can handle operational concerns.
- The author argues serverless Laravel resolves traditional hosting pain points while enabling faster, more scalable, and cost-effective solutions.
- Cold starts for PHP + Laravel on Lambda are reported at roughly 3–5 seconds.
- Laravel Octane can keep the application in memory between requests, bringing subsequent request times down to around 200ms or less.
- Provisioned Concurrency can pre-warm Lambda instances to reduce cold starts further, with extra cost, useful for critical endpoints.
- The author considers sub-3-second delays during low traffic acceptable for many applications because users rarely notice, especially when Lambdas are warm during high traffic.
- Under viral traffic scenarios, the old EC2 setup required manual scaling and careful balancing across availability zones while suffering latency.
- In the Lambda-based setup, AWS automatically scales out to handle large amounts of concurrent traffic without manual action, leaving the developer to just observe metrics.
- Billing under serverless corresponds to actual compute time used rather than pre-provisioned capacity kept idle for potential spikes.
- The prior EC2 stack, with four t3.small instances, a load balancer, shared EBS volume, and an RDS MySQL instance, cost about $110/month.
- After migrating, the Lambda-based architecture cost about $34/month, including Lambda, API Gateway handling about 2.5M requests at 500ms/512MB, managed services like S3, SQS, CloudWatch, and the same RDS instance.
- The author frames serverless cost benefits not only as monetary savings but also as reductions in mental overhead about capacity planning.
- They note that at the time measured, the database still ran on MySQL, with plans to explore DynamoDB later to cut costs further.
- With serverless, AWS handles server patching, OS updates, and runtime upgrades, so the app runs on secure, updated infrastructure without manual effort.
- API Gateway and S3 reduce the need to manage nginx or custom deployment configurations.
- Lambda’s elastic nature removes the need to overpay for idle servers or rush to add capacity during spikes, since scaling and idle cutoff are automatic.
- The author says the time once spent on operational tasks now goes into building features and improving user experience.
- They emphasize that serverless removes many operational distractions rather than just reducing them slightly.
- The article cautions that serverless Laravel is not suitable for every application and depends on workload characteristics.
- Laravel’s default reliance on local filesystem for sessions, file storage, and logs conflicts with Lambda’s statelessness and must be adapted.
- For serverless use, sessions should rely on databases or Redis, files and uploads should go to S3 or via pre-signed URLs, and logs should be sent to CloudWatch.
- Configuration values formerly stored in `.env` need to be moved to centralized AWS services like Secrets Manager or Parameter Store.
- Queues should be migrated to SQS to take advantage of scalable, message-based processing.
- The author warns about vendor lock-in, noting that switching from SQS to Redis queues later may require code rewrites.
- Moving from Lambda to Docker-based hosting is portrayed as a potentially time-consuming migration.
- They suggest avoiding serverless when applications require WebSockets, since using API Gateway WebSocket APIs or services like Ably adds architectural complexity.
- Serverless is also a weaker fit for workloads with heavy computation such as AI/ML inference or video encoding because of Lambda’s 15-minute timeout.
- Apps that assume persistent disk or server state can be expensive and involved to refactor for stateless execution.
- The post concludes by promising a follow-up article that will describe the concrete steps to implement a serverless Laravel architecture.
