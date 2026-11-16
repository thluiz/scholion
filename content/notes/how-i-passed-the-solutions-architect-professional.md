---
title: "How I passed the Solutions Architect Professional with mostly free content🥇"
date: '2020-07-05T14:10:32+00:00'
category: webclip
summary: 'The author says the AWS SA Pro exam rewards broad architectural understanding, practice exams, and focused study across networking, IAM, multi-account setups, migration, and core AWS services.'
tags: ["aws", "solutions-architect-professional", "cloud-certification", "devops"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "How I passed the Solutions Architect Professional with mostly free content🥇"
    url: "https://dev.to/aws-heroes/how-i-passed-the-solutions-architect-professional-with-mostly-free-content-ine"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/dev-to--how-i-passed-the-solutions-architect-professional.md"
    kind: repo
---

The author describes how they passed the AWS Solutions Architect Professional exam by focusing on core services, practice exams, and free or low-cost study material. They emphasize that the test checks architectural judgment more than detailed trivia, and that time management matters during the exam.

## Reading notes

- The author says the exam is widely seen as AWS’s hardest, but advises focusing on core services and common use cases instead of trying to master every service in detail.
- Practice exams are presented as the most helpful study tool, along with AWS Training, free online material, re:Invent and re:Inforce videos, whitepapers, and service FAQs.
- Network and VPC design is treated as a crucial topic, including security groups, NACLs, subnets, NAT gateways, internet gateways, egress-only gateways, CIDR ranges, and VPC-to-VPC or on-premises connectivity.
- IAM is another key area, with emphasis on policy types, least privilege, cross-account roles, STS, and identity federation through SAML or web identity.
- The PARC model is mentioned as a memory aid for IAM policies: Principal, Action, Resource, and Condition.
- The article gives examples of IAM conditions, including restricting access to SSL-only traffic and limiting requests to specific AWS regions.
- Multi-account design is tied to AWS Organizations, service control policies, consolidated billing, and AWS Budgets.
- Migration planning is described as its own exam domain and includes application and data migration, hybrid storage, and choosing between online and offline transfer options.
- For new solutions and improvements, the author highlights the AWS Well-Architected Framework, serverless design, Lambda, X-Ray, API Gateway, Cognito, DynamoDB, SQS, SNS, Kinesis, EventBridge, Route 53, load balancers, CloudFormation, deployment services, EC2 instance families, EBS volume types, and database model choices.
- The author also notes some service limits, such as Lambda’s 15-minute execution limit and the fact that a standard SQS queue cannot be converted into FIFO.
- Taking the exam online involved software checks, workspace photos, and waiting for proctor approval before starting.
- During the exam, the author recommends reading carefully, comparing answer choices by small differences, using elimination when needed, and marking uncertain questions for review.
