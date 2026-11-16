---
url: "https://dev.to/aws-heroes/how-i-passed-the-solutions-architect-professional-with-mostly-free-content-ine"
captured_at: "2026-11-16T01:26:50+00:00"
title: "How I passed the Solutions Architect Professional with mostly free content🥇"
domain: "dev-to"
---

First off, well done to anyone starting the journey to certification. Just being willing to study and take an exam puts you ahead of most others, so you should be rightly proud. For me, I like the goal of becoming certified and the structured content as a way to keep me motivated.

I was fortunate enough to pass the AWS SA Pro exam in the last month with an online proctored exam. I’ve had a few people ask what I thought of the course/exam, and also the online experience. Each individual has their own approach which works for them, so I’ll just set out what worked for me and how I found it.

## [](#course)Course

The [AWS SA Pro](https://aws.amazon.com/certification/certified-solutions-architect-professional/) is reputed to be toughest AWS exam but don't let that put you off. AWS is growing at such a rapid pace, there is no way you can have detailed knowledge about all services. Instead, I just focused on getting a good understanding of a number of core services, and then being able to understand use cases for many others. The exam is testing your understand of what makes a good architecture, and is not trying to catch you out on small technicalities.

I'm lucky to have a work subscription to [ACloudGuru](https://acloud.guru/). For anyone studying for an exam there are a number of paid-for courses including from [Linux Academy](https://app.linuxacademy.com/), [WhizLabs](https://www.whizlabs.com/) and [Exam Pro](https://www.exampro.co/). There are some fantastic free resources available online such as [AWS Training](https://www.aws.training/) and [FreeCodeCamp](https://www.freecodecamp.org/news/how-to-take-any-aws-certification-from-home/).

I found the practice exams were what helped most to get the right feel. I had a free voucher code so I also took the online AWS practice exam. I made a conscious decision I didn't want to get bogged down in detail, so for the online courses I tended to speed them up, and only make minimal notes. I also got huge value from watching re:Invent and re:Inforce videos on YouTube and reading a number of the AWS Whitepapers and Service FAQs.

Although the course content is broken down into 5 domains, many of it is cross-cutting, so the following is what I personally found most important, and this was reflected with the questions I had in the exam.

#### [](#network-and-vpc-design)Network and VPC Design

A solid understanding of network and VPC design is crucial. This covers the different ways of connecting AWS to on-premises as well as connecting VPC to VPC. This also includes VPC design. By this stage, you need to understand differences between Security Groups, NACLs, public and private subnets, NAT Gateways, Internet Gateways and Egress-only internet gateways. It also includes basic knowledge of CIDR ranges and how to expand or change these in an existing VPC.

Video:

*   [AWS re:Invent 2019: Advanced VPC design and new capabilities for Amazon VPC](https://www.youtube.com/watch?v=7acKgdDOOu4)

Whitepapers:

*   [Building a Scalable and Secure Multi-VPC AWS Network Infrastructure](https://d1.awsstatic.com/whitepapers/building-a-scalable-and-secure-multi-vpc-aws-network-infrastructure.pdf)

#### [](#iam)IAM

Another crucial topic is IAM. There is a common thread around being secure by design and applying least privilege, and this extends itself to understanding IAM and policies. You need to understand different policy types and their use cases. You also need to understand cross-account roles, the Security Token Service and federating identity either through SAML or web identity federation.

A useful tip is to remember the **PARC** model which stands for Principal, Action, Resource and Condition, and make sure you understand how each of them are used.  

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "effect",
            "Principal":"principal",
            "Action": "action",
            "Resource": "arn",
            "Condition":{
                "condition"{
                    "key":"value"
                }
            }
        }
    ]
}
```

Enter fullscreen mode Exit fullscreen mode

Conditions are particularly powerful. Common examples including enforcing SSL access only  

```
      ...
      "Effect": "Deny",
      "Resource": [...],
      "Condition": {
        "Bool": {
          "aws:SecureTransport": "false"
        }
      ...
```

Enter fullscreen mode Exit fullscreen mode

and even restricting regions:  

```
       ...
       "Condition": {
            "StringEquals": {
                "aws:RequestedRegion": [ "eu-west-1", "eu-west-2" ]
            }
        }
        ...
```

Enter fullscreen mode Exit fullscreen mode

Video:

*   [AWS re:Invent 2018: Become an IAM Policy Master in 60 Minutes or Less](https://www.youtube.com/watch?v=YQsK4MtsELU)

#### [](#multi-account)Multi Account

The exam guide talks about designing a 'multi-account AWS environment for complex organizations'. This means look out for questions on AWS Organizations and how to use it. I set up AWS Organizations with a number of member accounts and applied different service control policies and looked at different options on consolidated billing and AWS Budgets, and it meant I could answer any of the questions I got on the exam.

Video:

*   [AWS re:Inforce 2019: Managing Multi-Account AWS Environments Using AWS Organizations](https://www.youtube.com/watch?v=fxo67UeeN1A)

#### [](#migration)Migration

Migration planning is called out as its own domain in the exam guide, and is another important topic. This covers migrating both applications and data, and choosing the most appropriate approach based on timescales, amount of data to transfer, type of application. There are useful sites that look at different options for hybrid cloud storage, online data transfer and offline data transfer:

Sites:

*   [Migration and Transfer](https://docs.aws.amazon.com/whitepapers/latest/aws-overview/migration-services.html)
*   [AWS Cloud Data Migration Services](https://aws.amazon.com/cloud-data-migration/)

Videos:

*   [AWS re:Invent 2019: Get your data to AWS: How to choose and use data migration services](https://www.youtube.com/watch?v=KAuS-ge_X7Y&)

Whitepapers:

*   [Migrating Applications Running Relational Databases to AWS](https://d1.awsstatic.com/whitepapers/Migration/migrating-applications-to-aws.pdf)

#### [](#new-solutions-improving-existing-solutions)New Solutions / Improving Existing Solutions

According to the guide, 60% of the exam content is on designing new solutions and improving existing solutions. This is when knowledge of modern application design and core AWS services is crucial, so get familiar with the AWS Well Architected Framework:

*   One of the design principles for performance efficiency is to "use serverless architectures" so pay particular attention to AWS Lambda, X-Ray, API Gateway, Cognito and DynamoDB amongst other services.
*   You need to understand how to use services like SQS, SNS, Kinesis and EventBridge to decouple consumers from producers.
*   You need to understand how to use Route53 and Load Balancers to increase availablility and support failover.
*   With best practice also being infrastructure as code, you will also need to understand CloudFormation. This includes the basic template anatomy, and what a valid template may look like, for example creating an EC2 instance from an AMI

```
Resources:
  MyEC2Instance:
    Type: "AWS::EC2::Instance"
    Properties:
      ImageId: "ami-0ff8a91507f77f867"
```

Enter fullscreen mode Exit fullscreen mode

*   Repeatable builds and deployments are crucial, so understand how CodePipeline, CodeBuild, CodeDeploy and ElasticBeanstalk can support various different deployment approaches such as A/B and canary.
*   You need to understand at a high level the different EBS volume types and EC2 instance types. Personally, I didn't feel I needed to know the exact network performance or volume size, but just understand the differences between general purpose, compute optimised, memory optimised and so on
*   You need to understand when to use a relational vs key-value vs columnar vs ledger database

This is also where it's important to understand some of the key service limits. For example, if processing will take longer than 15 mins then AWS Lambda is not appropriate. If you need a FIFO SQS queue then you need to know that you can't convert an existing standard queue.

Videos:

*   [AWS re:Invent 2019: Optimizing your serverless applications](https://www.youtube.com/watch?v=5rMiq-jw1Ig)
*   [AWS re:Invent 2019: Data modeling with Amazon DynamoDB](https://www.youtube.com/watch?v=DIQVJqiSUkE)
*   [AWS re:Invent 2019: Amazon DynamoDB deep dive: Advanced design patterns](https://www.youtube.com/watch?v=6yqfmXiZTlM)
*   [AWS re:Inforce 2019: How Encryption Works in AWS](https://www.youtube.com/watch?v=plv7PQZICCM)

Whitepapers:

*   [AWS Well-Architected Framework](https://d1.awsstatic.com/whitepapers/architecture/AWS_Well-Architected_Framework.pdf)
*   [Implementing Microservices on AWS](https://d1.awsstatic.com/whitepapers/microservices-on-aws.pdf)

## [](#taking-the-exam-online)Taking the Exam Online

It was a different experience taking the exam online. To start off with, you need to have some software installed which also checks there is nothing else running. You then have to take pictures of your workspace, and you end up sitting there for around 15 minutes, waiting for these to be checked, before you can start the exam. It also felt different taking the exam at home, rather than a specific venue, but once I started it didn't have any effect.

It's important not to rush the questions and make sure you think through the approach for your chosen answer. For any question I was unsure on, I focused on the different possible answers, and it was often clear that they differentiated in one small aspect e.g. one suggested S3 and another EFS, one suggested SQS and another Kinesis. This really helped to focus on what the question was targetting, as it is very easy to get bewildered by the length of some of the questions. Where the answer was not obvious, I used a process of elimation, which is why it was good to remember some of the key service limits and what services integrate with what. This at least increased the chances of selecting the right answer.

I had flown through all of the practice exams, and expected to finish with plenty of time left. This didn't happen, but mainly as I was taking my time and making sure I didn't throw away any easy marks by rushing. You do need to keep track of the time, to make sure you don't spend so long on one question it forces you to speed up. After a number of minutes, if you still aren't sure, I always put my best answer down and marked for review so I could come back at the end.

## [](#conclusion)Conclusion

So that was it. I'd managed to gain a sought after certification but more importantly increased my knowledge of AWS that can only make me better in my role. I genuinely enjoy learning and testing myself. Hopefully this has helps some of you, and encourages others to give it a go. Reach out if you have any questions.
