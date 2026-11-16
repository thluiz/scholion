---
url: "https://dev.to/aws-heroes/applying-the-well-architected-framework-small-edition-18fj"
captured_at: "2026-11-16T02:03:32+00:00"
title: "Applying the Well-Architected Framework, Small Edition"
domain: "dev-to"
---

Do you ever tackle a problem and know that you’ve just spent way too much time on it? But you also know that it was worth it? This post (which is also long!) sums up my recent experience with exactly that type of problem.

## [](#tldr)tl:dr

*   AWS Lambda has a storage limit for `/tmp` of 512MB
*   AWS Lambda functions needs to be in a VPC to connect to an Amazon EFS filesystem
*   AWS Lambda functions within in a VPC **require** a NAT gateway to access the internet
*   Amazon EC2 instances can use cloud-init to run a custom script on boot
*   A solution needs to address all five pillars of the AWS Well-Architected Framework in order to be the “best”

Read on to find out the whole story…

## [](#the-problem)The Problem

I love learning and want to keep tabs on several key areas. Ironically, tabs themselves [are massive issue for me](https://twitter.com/marknca/status/1017237825199247361).

Every morning, I get a couple of tailored emails from a service called [Mailbrew](https://mailbrew.com/). Each of these emails contains the latest results from Twitter queries, subreddits, and key websites (via RSS).

The problem is that I want to track a lot of websites and Mailbrew only supports adding sites one-by-one.

This leads to a problem statement of…

> Combine N feeds into one super feed

## [](#constraints)Constraints

Ideally these _super feeds_ would be published on my website. That site is build in [Hugo](https://gohugo.io/) and deployed to [Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/dev/WebsiteHosting.html) with [CloudFlare](https://www.cloudflare.com/) in front. This setup is ideal for me.

Following the [AWS Well-Architected Framework](https://aws.amazon.com/architecture/well-architected/); it’s highly performant, low cost, has minimal operational burden, a strong security posture, and is very reliable. It’s a win across all five pillars.

Adding the feeds to this setup shouldn’t compromise any of these attributes.

> I think it’s important to point out that there a quite a few services out there that combine feeds for your. [RSSUnify](https://rssunify.com/) and [RSSMix](http://www.rssmix.com/) come to mind, but there are many, many others…

The nice thing about Hugo is that it uses text files to build out your site, including [custom RSS feeds](https://benjamincongdon.me/blog/2020/01/14/Tips-for-Customizing-Hugo-RSS-Feeds/). The solution should write these feed items as unique posts (a/k/a text files) in my Hugo content directory structure.

## [](#python-to-the-rescue)🐍 Python To The Rescue

A quick little python script ([available here](https://gist.github.com/marknca/c863d166cf91d710c247f6af563ca73b)) and I’ve got a tool that takes a list of feeds and writes them into unique Hugo posts.

Problem? **Solved.**

Hmmm…I forgot these feeds need to be kept up to date and my current build pipeline (a [GitHub Action](https://github.com/features/actions)) doesn’t support running on a schedule.

Besides, trying to run that code in the action is going to require another event to hook into or it’ll get stuck in an update loop as the new feed items are committed to the repo.

New problem statement…

> Run a python script on-demand and a set schedule

This feels like a good problem for [a serverless solution](https://markn.ca/2019/road-to-reinvent-what-is-serverless/).

## [](#aws-lambda)AWS Lambda

I immediately thought of [AWS Lambda](https://aws.amazon.com/lambda/). I run a crazy amount of little operational tasks just like this using AWS Lambda functions triggered by a scheduled [Amazon CloudWatch Event](https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/WhatIsCloudWatchEvents.html). It’s a strong, simple pattern.

It turns out that getting a Lambda function to access a git repo isn’t very straight forward. I’ll save you the sob story but here’s how I got it running using a python 3.8 runtime;

*   add the git binaries as a Lambda Layer, I used [git-lambda-layer](https://github.com/lambci/git-lambda-layer)
*   use the [GitPython](https://github.com/gitpython-developers/GitPython) module

That allows a simple code setup like this:  

```
repo = git.Repo.clone_from(REPO_URL_WITH_AUTH)
...
# do some other work, like collect RSS feeds
...
for fn in repo.untracked_file:
  print("File {} hasn't been added to the repo yet".format(fn))

# You can also use git commands directly-ish
repo.git.add('.') 
repo.git.commit('Updated from python')
```

Enter fullscreen mode Exit fullscreen mode

This makes it easy enough to work with a repo. With a little bit of hand wavy magic, I wired a Lambda function up to a scheduled CloudWatch Event and I was done.

…until I remembered—and by, “remembered”, I mean the function threw an exception—about the Lambda `/tmp` storage [limit of 512MB](https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html). The repo for my website is around 800MB and growing.

## [](#amazon-efs)Amazon EFS

Thankfully, AWS just released a new integration between [Amazon EFS and AWS Lambda](https://aws.amazon.com/blogs/compute/using-amazon-efs-for-aws-lambda-in-your-serverless-applications/). I followed along the relatively simple process to get this set up.

I hit two big hiccups.

The first, for a Lambda function to connect to an EFS file system, both need to be “in” the same VPC. This is easy enough to do if you have a VPC setup and [even if you don’t](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-getting-started.html). We’re going to come back to this one in a second.

The second issue was that I initially set the path for the EFS access point to `/`. There wasn’t a warning (that I saw) in the official documents but an off-handed remark in [a fantastic post by Peter Sbarski](https://read.acloud.guru/how-i-used-lambda-and-efs-for-massively-parallel-compute-96575bc85157) highlighted this problem.

That was a simple fix (I went with `/data`) but the VPC issue brought up a bigger challenge.

The simplest of VPCs that will solve this problem is one or two subnets with an internet gateway configured. This structure is free and only incurs [charges for inbound/outbound data transfer](https://www.duckbillgroup.com/blog/understanding-data-transfer-in-aws/).

**Except** that my Lambda function needs internet access and that requires one more piece.

[That piece is a NAT gateway](https://aws.amazon.com/premiumsupport/knowledge-center/internet-access-lambda-function/). No big deal, it’s [a one click deploy](https://aws.amazon.com/premiumsupport/knowledge-center/nat-gateway-vpc-private-subnet/) and a same routing change. The new problem is cost.

The need for a NAT gateway makes completely sense. Lambda runs adjacent to your network structure. Routing those functions into your VPC requires an explicit structure. From a security perspective, we don’t want an implicit connection between our private network (VPC) and other random bits of AWS.

[![Alt Text](https://media2.dev.to/cdn-cgi/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fi%2Fz5l0421astnspeouzzyl.jpg)](https://media2.dev.to/cdn-cgi/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fi%2Fz5l0421astnspeouzzyl.jpg)

## [](#wellarchitected-principles)Well-Architected Principles

This is where things really start to go off the of the rails. As mentioned above, the Well-Architected Framework is built on five pillars;

*   [Operational Excellence](https://d1.awsstatic.com/whitepapers/architecture/AWS-Operational-Excellence-Pillar.pdf)
*   [Reliability](https://d1.awsstatic.com/whitepapers/architecture/AWS-Reliability-Pillar.pdf)
*   [Security](https://d1.awsstatic.com/whitepapers/architecture/AWS-Security-Pillar.pdf)
*   [Performance Efficiency](https://d1.awsstatic.com/whitepapers/architecture/AWS-Performance-Efficiency-Pillar.pdf)
*   [Cost Optimization](https://d1.awsstatic.com/whitepapers/architecture/AWS-Cost-Optimization-Pillar.pdf)

The AWS Lambda + Amazon EFS route continues to perform well in all of the pillars except for one; cost optimization.

Why? Well I use accounts and VPCs as [strong security barriers](https://d0.awsstatic.com/aws-answers/AWS_Multi_Account_Security_Strategy.pdf). So the VPC that this Lambda function and EFS filesystem are running in is only for this solution. The NAT gateway would only be used during the build of my site.

The [cost of a NAT gateway](https://aws.amazon.com/vpc/pricing/) per month? **$32.94** + bandwidth consumed.

That’s not an unreasonable amount of money until you put that in the proper context of the project. The site costs less than $0.10 per month to host. If we add in the AWS Lambda function + EFS filesystem, that skyrockets to **$0.50 per month** 😉.

That NAT gateway is looking very unreasonable now

## [](#alternatives)Alternatives

Easy alternatives to AWS Lambda for computation are [AWS Fargate](https://aws.amazon.com/fargate/) and good old [Amazon EC2](https://aws.amazon.com/ec2/). As much as everyone would probably lean towards containers and I’ve heard people say it’s the next logical choice…

…I went old school and started to explore what a solution in EC2 would look like.

For an Amazon EC2 instance to access the internet, it only needs to be in a public subnet of a VPC with an internet gateway. No NAT gateway needed. This removes the $32.94 each month but does put us into a more expensive compute range.

But can we automate this easily? Is this going to be a reliable solution? What about the security aspects?

## [](#amazon-ec2-solution)Amazon EC2 Solution

The 🔑 key? Remembering the _[user-data](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/user-data.html)_ feature of EC2 and that all AWS-managed AMIs support [cloud-init](https://cloudinit.readthedocs.io/en/latest/).

This provides us with 16KB of space to configure an instance on the fly to accomplish out task. That should be plenty...if you haven't figured it out from my profile pic, I'm approaching the greybeard powers phase of my career 🧙‍♂️.

A quick bit of troubleshooting (lots of instances firing up and down), and I ended up with this [bash](https://www.gnu.org/software/bash/manual/html_node/index.html#SEC_Contents) script (yup, bash) to solve the problem;  

```
#! /bin/bash
sleep 15
sudo yum -y install git
sudo yum -y install python3
sudo pip3 install boto3
sudo pip3 install dateparser
sudo pip3 install feedparser

cat > /home/ec2-user/get_secret.py <<- PY_FILE
# Standard libraries
import base64
import json
import os
import sys

# 3rd party libraries
import boto3
from botocore.exceptions import ClientError

def get_secret(secret_name, region_name):
    secret = None
    session = boto3.session.Session()
    client = session.client(service_name='secretsmanager', region_name=region_name)
    try:
        get_secret_value_response = client.get_secret_value(SecretId=secret_name)
    except ClientError as e:
        print(e)
    else:
        if 'SecretString' in get_secret_value_response:
            secret = get_secret_value_response['SecretString']
        else:
            decoded_binary_secret = base64.b64decode(get_secret_value_response['SecretBinary'])

    return json.loads(secret)

if __name__ == '__main__':
    github_token = get_secret(secret_name="GITHUB_TOKEN", region_name="us-east-1")['GITHUB_TOKEN']
    print(github_token)
PY_FILE

git clone https://\`python3 get_secret.py\`:x-oauth-basic@github.com/USERNAME/REPO /home/ec2-user/website

python3 RUN_MY_FEED_UPDATE_SCRIPT

cd /home/ec2-user/website

# Build my website
./home/ec2-user/website/bin/hugo -b https://markn.ca

# Update the repo
git add .
git config --system user.email MY_EMAIL
git config --system user.name "MY_NAME"
git commit -m "Updated website via AWS"
git push

# Sync to S3
aws s3 sync /home/ec2-user/website/public s3://markn.ca --acl public-read

# Handy URL to clear the cache
curl -X GET "https://CACHE_PURGING_URL"

# Clean up by terminating the EC2 instance this is running on
aws ec2 terminate-instances --instance-ids `wget -q -O - http://169.254.169.254/latest/meta-data/instance-id` --region us-east-1
```

Enter fullscreen mode Exit fullscreen mode

This entire run takes on average 4 minutes. Even at the higher on-demand cost (vs. [spot](https://aws.amazon.com/ec2/spot/pricing/)), each run costs $0.000346667 on a t3.nano in us-east-1.

For the month, that’s $0.25376244 (for 732 scheduled runs).

We’re well 😉 over the AWS Lambda compute price ($0.03/mth) but still below the Lambda + EFS cost ($0.43/mth) and certainly well below the total cost including a NAT gateway. It’s weird, but this is how cloud works.

Each of these runs is triggered by a CloudWatch Event that calls an AWS Lambda function to create the EC2 instance. That’s one extra step compared to the pure Lambda solution but it’s still reasonable.

## [](#reliability)Reliability

In practice, this solution has been working well. After 200+ runs, I have experienced zero failures. That’s a solid start. Additionally, the cost of failure is low. If this process fails to run, the site isn’t updated.

Looking at the overall blast radius, there are really only two issues that need to be considered;

1.  If the sync to S3 fails and leaves the site in an incomplete state
2.  If the instance fails to terminate

The likelihood of a sync failure is very low but if it does fail the damage would only be to one asset on the site. The AWS CLI command copies files over one-by-one if they are newer. If one fails, the command stops. This means that only one asset (page, image, etc.) would be in a damaged state.

As long as that’s not the main .css file for the site, we should be ok. Even then, clean HTML markup leaves the site still readable.

The second issue could have more of an impact.

The hourly cost of the t3.nano instance is $0.0052/hr. Every time this function runs, another instance is created. This means I could have a few dozen of these instances running in a failure event…running up a bill that would quickly top $100/month if left unchecked.

In order to mitigate this risk, I added another command to the bash script; `shutdown`. Also ensuring that the API parameter of `—instance-initiated-shutdown-behavior` set to `terminate` is set on instance creation. This means the instance calls the EC2 API to terminate itself and shuts itself down to terminate…just in case.

Adding [a billing alert](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/monitor_estimated_charges_with_cloudwatch.html) rounds out the mitigations to significantly reduce the risk.

## [](#security)Security

The security aspects of this solution concerned me. AWS Lambda presents a much smaller set of responsibilities for the user. In fact, an instance is the most responsibility taken on by the builder within [the Shared Responsibility Model](https://markn.ca/2019/road-to-reinvent-the-shared-responsibility-model/). That’s the opposite way we want to be moving.

Given that this instance isn’t handling inbound requests, the security group is completely locked down. It only allows outbound traffic, nothing inbound.

Additionally, using an IAM Role, I’ve only provided the necessary permissions to accomplish the task at hand. This is called the principle of least privilege. It can be a pain to setup sometimes but does wonders to reduce the risk of any solution.

You may have noticed in the _user-data_ script above that we’re actually writing a python script to the instances on boot. This script allows the instance to access [AWS Secrets Manager](https://aws.amazon.com/secrets-manager/) to get a secret and print its value to stdout.

I’m using that to store the [GitHub Personal Access Token](https://help.github.com/en/github/authenticating-to-github/creating-a-personal-access-token) required to clone and update the private repo that holds my website. This reduces the risk to my GitHub credentials which are the most important piece of data in this entire solution.

This means that the instance needs to the following permissions;  

```
secretsmanager:GetSecretValue
secretsmanager:DescribeSecret
s3:ListBucket
s3:*Object
ec2:TerminateInstances
```

Enter fullscreen mode Exit fullscreen mode

The permissions for `secretsmanager` are locked to the specific ARN of the secret for the GitHub token. The `s3` permissions are restricted to [read/write](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_examples_s3_rw-bucket.html) my website bucket.

`ec2:TerminateInstances` was a bit trickier as we don’t know the instance ID ahead of time. You could dynamically assign the permission but that adds needless complexity. Instead, this is a great use case for resource tags as a condition for the permission. If the instance isn’t tagged properly (in this case I use a “Task” key with a value set to a random, constant value), this role can’t terminate it.

Similarly, the AWS Lambda function has standard execution rights and;  

```
iam:PassRole
ec2:CreateTags
ec2:RunInstances
```

Enter fullscreen mode Exit fullscreen mode

Cybersecurity is simply making sure that what you build does what you intend…and only what is intended.

If we run through the possibilities for this solution, there isn’t anything that an attacker could do without already having other rights and access within our account.

We’ve minimized the risk to a more than acceptable level, even though we’re using EC2. It appears that this solution can only do what is intended.

## [](#what-did-i-learn)What Did I Learn?

The Well-Architected Framework isn’t just useful for big projects or for a point-in-time review. The principles promoted by the framework apply continuously to any project.

I thought I had a simple, slam dunk solution using a serverless design. In this case, a pricing challenge required me to change the approach. Sometimes it’s a performance, sometimes it’s security, sometimes it’s another aspect.

Regardless, you need to be evaluating your solution across all five pillars to make sure you’re striking the right balance.

There’s something about the instance approach that still worries me a bit. I don’t have the same peace of mind that I do when I deploy Lambda but the data is showing this as reliable and meeting all of my needs.

This setup also leaves room for expansion. Adding addition tasks to the _user-data_ script is straightforward and would not dramatically shift any of the concerns around the five pillars if done well. The risk here is expanding this into a custom CI/CD pipeline which is something to avoid.

“I built my own…”, generally means you’ve taken a wrong turn somewhere along the way. Be concerned when you find yourself echoing those sentiments.

This is also a reminder that there are a ton of features and functionality within the big three ([AWS](https://aws.amazon.com/), [Azure](https://azure.microsoft.com/en-ca/), [Google Cloud](https://cloud.google.com/)) cloud platforms and that can be a challenge to stay on top of.

If I didn’t remember the cloud-init/user-data combo, I’m not sure I would’ve evaluated EC2 as a possible solution.

One more reason to keep on learning and sharing!

Btw, checkout the results of this work at;

*   [Security Super Feed](https://markn.ca/security-super-feed/)
*   [DevOps Super Feed](https://markn.ca/devops-super-feed/)
*   [Cloud Super Feed](https://markn.ca/cloud-super-feed/)

And if I'm missing a link with a feed that you think should be there, [please let me know](https://docs.google.com/forms/d/e/1FAIpQLSeASl4P9NEgdtVQeLrJ8sOm0x-x_1SWAsIvTGDYcfNpOW1vTA/viewform)!

## [](#total-cost)Total Cost

If you’re interested in the total cost breakdown for the solution at the end of all this, here is it;  

```
Per month
===========
24 * 30.5 = 732 scheduled runs
+ N manual runs
===========
750 runs per month

EC2 instance, t3.nano at $0.0052/hour
+ running for 4m on average
===========
(0.0052/60) * 4 = $0.000346667/run

AWS Lambda function, 128MB at $0.0000002083/100ms
+ running for 3500ms on average
============
$0.00000729/run

Per run cost
============
$0.000346667/run EC2
$0.00000729/run Lambda
============
$0.000353957/run

Monthly cost
=============
$0.26546775/mth to run the build 750 times
$0.00 for VPC with 2 public subnets and Internet Gateway
$0.00 for 2x IAM roles and 2x policies
$0.40 for 1x secret in AWS Secrets Manager
$0.00073 for 732 CloudWatch Events (billed eventually)
$0.00 for 750 GB inbound transfer to EC2 (from GitHub)
$0.09 for 2 GB outbound trasnfer (to GitHub)
=============
$0.75620775/mth

This means it'll take 3.5 years before we've spent the same as one month of NAT Gateway support.

* Everything is listed in us-east-1 pricing
```

Enter fullscreen mode Exit fullscreen mode
