---
title: "Applying the Well-Architected Framework, Small Edition"
date: '2026-11-16T02:03:32+00:00'
category: webclip
summary: 'The post compares a Lambda/EFS design with an EC2-based approach for building and publishing super feeds, and weighs both against the five AWS Well-Architected pillars, especially cost and security.'
tags: ["aws-well-architected-framework", "aws-lambda", "amazon-ec2", "cost-optimization"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Applying the Well-Architected Framework, Small Edition"
    url: "https://dev.to/aws-heroes/applying-the-well-architected-framework-small-edition-18fj"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/dev-to--applying-well-architected-framework-small-edition.md"
    kind: repo
---

The post starts with the goal of combining many feeds into one super feed and publishing it through a Hugo site. A Python script can write feed items as Hugo posts, but keeping it updated on a schedule leads to a cloud design choice.

The first approach uses AWS Lambda, CloudWatch Events, and Amazon EFS, but the Lambda /tmp limit and the need for a NAT gateway in a VPC make the cost unattractive. The final choice is an EC2 instance started on demand, configured with user-data and cloud-init, then used to run the update script, build the site, sync it to S3, and terminate itself.

## Reading notes

- The problem is to combine many feeds into one super feed and publish it on a Hugo site.
- Hugo stores content as text files, so the solution writes feed items as unique posts in the content tree.
- A Python script can collect feeds and write them into Hugo posts.
- Lambda can run the script on a schedule, but the repo size exceeds the 512 MB /tmp limit.
- Lambda needs a VPC to access Amazon EFS, and internet access from that VPC requires a NAT gateway.
- The NAT gateway makes the Lambda plus EFS setup too expensive for a site whose hosting cost is otherwise very low.
- EC2 in a public subnet avoids the NAT gateway and can run the workflow with user-data and cloud-init.
- The EC2 instance installs tools, gets a GitHub token from Secrets Manager, clones the repo, runs the feed update, builds the site, syncs to S3, clears cache, and terminates itself.
- The author weighs the solution against the five Well-Architected pillars, with cost optimization and security as the main concerns.
- Reliability is addressed through a low blast radius, shutdown behavior, and billing alerts.
- Security is handled with a locked-down security group, least-privilege IAM roles, Secrets Manager, and tag-based permission control.
- The main lesson is that the Well-Architected Framework applies continuously, and the best design can change when cost or other constraints change.
