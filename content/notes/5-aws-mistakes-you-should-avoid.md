---
title: "5 AWS mistakes you should avoid"
date: '2016-01-02T17:37:36-03:00'
category: webclip
summary: 'The post lists five common AWS mistakes in typical web applications: manual infrastructure, no Auto Scaling Groups, ignored CloudWatch metrics, ignored Trusted Advisor, and underused virtual machines.'
tags: ["aws", "cloudwatch", "autoscaling-groups", "trusted-advisor"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "5 AWS mistakes you should avoid"
    url: "http://cloudonaut.io/5-aws-mistakes-you-should-avoid/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2016-01/cloudonaut-io--5-aws-mistakes-you-should-avoid.md"
    kind: repo
---

The post says typical AWS web applications should use a load balancer, a scalable web backend, and a database. It then lists five recurring mistakes the author sees in small and medium AWS deployments and says they should be avoided.

## Reading notes

- Infrastructure should not be managed manually through the console; CloudFormation is presented as the way to describe resources in a template and create or update a stack reproducibly.
- Every EC2 instance should run inside an Auto Scaling Group, even a single instance, because the group monitors the instance and can later support scaling based on alarms.
- CloudWatch metrics should be analyzed, not just collected; the example shows a daily CPU spike caused by a cron job, and alarms should be defined after the metrics are understood.
- Trusted Advisor checks an AWS account against AWS best practices in cost optimization, performance, security, and fault tolerance, and the post recommends paying attention to security first.
- Virtual machines should be downsized when underutilized, using CloudWatch metrics to decide whether instance size or fleet size can be reduced.
