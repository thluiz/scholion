---
title: "Refactoring to Serverless: From Application to Automation"
date: "2026-09-23T18:15:35+01:00"
category: webclip
has_commentary: false
summary: "AWS engineers propose 'serverless refactoring': moving logic like event publishing out of application code and into automation code (CDK, Lambda Destinations) to separate business logic from topology."
tags:
  - serverless
  - aws
  - infrastructure-as-code
  - software-architecture
sources:
  - title: "Refactoring to Serverless: From Application to Automation | AWS DevOps & Developer Productivity Blog"
    url: "https://aws.amazon.com/pt/blogs/devops/refactoring-to-serverless-from-application-to-automation/?ref=dailydev"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/aws-amazon-com--refactoring-to-serverless-from-application-to-automation.md"
    kind: repo
---

Sindhu Pillai and Gregor Hohpe describe serverless infrastructure-as-code as something that has outgrown its original job. Where early IaC tools like CloudFormation provisioned infrastructure, CDK-style automation for serverless apps now defines the application's topology itself, connecting Lambda functions to event sources and targets. They call this shift "AaC," Architecture as Code, and use it to argue for a specific technique: moving code that used to live in the application (like manually publishing an event to EventBridge) into automation code instead (Lambda Destinations configured through CDK).

They name this technique "serverless refactoring," borrowing Martin Fowler's definition of refactoring, restructuring code without changing its external behavior, and applying it across the application/automation boundary.

## Reading notes

- Moving message-sending logic from application code into the runtime (via Lambda Destinations) decouples business logic from topology: changing where a message goes no longer requires touching application code.
- Automation code keeps service dependencies in one place, which existing code analysis and refactoring tools can reason about, instead of relying on naming conventions buried in environment variables.
- Fewer hand-written integration points means fewer bugs from redundant code, and the runtime's built-in retry handling replaces custom error-handling code.
- Serverless refactoring is not fully behavior-preserving: Lambda Destinations only fire on asynchronous invocations, wrap payloads in a message envelope that changes how recipients parse them, and always fire after function completion rather than at an arbitrary point during execution.
- The authors treat these behavior differences as usually transparent to well-architected asynchronous systems, since such systems shouldn't depend on message delivery timing in the first place.
- Unlike code refactorings such as "Extract Method," serverless refactoring isn't yet a fully automated transformation; the authors frame it as a design technique for developers rather than an editor feature, even as AI tools move toward automating it.
- When application and automation code belong to different teams, AWS recommends keeping application-specific automation (Lambda Destinations, Step Functions workflows) with the development team, and reserving shared, reusable IaC constructs for a separate platform team.
