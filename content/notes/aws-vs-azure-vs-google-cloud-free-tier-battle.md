---
title: "AWS vs. Azure vs. Google Cloud: The Ultimate Free Tier Battle & Survival Guide"
date: "2026-09-23T14:29:13+01:00"
category: webclip
has_commentary: false
summary: "A side-by-side of AWS, Azure, and GCP free tiers: compute, databases, and the hidden billing traps (orphaned volumes, static IP tax, data egress) each provider uses to monetize free users."
tags:
  - cloud-computing
  - free-tier
  - pricing
  - vendor-lock-in
sources:
  - title: "AWS vs. Azure vs. Google Cloud: The Ultimate Free Tier Battle & Survival Guide - DEV Community"
    url: "https://dev.to/bradleymatera/aws-vs-azure-vs-google-cloud-the-ultimate-free-tier-battle-survival-guide-2fam?context=digest"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/dev-to--aws-vs-azure-vs-google-cloud-the-ultimate-free-tier-battle-survival-guide.md"
    kind: repo
---

Bradley Matera compares AWS, Azure, and Google Cloud Platform free tiers across compute, databases, and the billing line items that never show up on the pricing page. AWS gives twelve months of free usage on its own proprietary tools (RDS, S3, IAM) before billing starts. Azure gives $200 in credits upfront to let developers try its premium tiers. GCP keeps a narrower but permanent always-free tier aimed at hobbyists and students.

The compute comparison favors GCP's e2-micro for longevity, since the offer never expires, against AWS's stronger but time-limited t3.micro and Azure's weaker, interface-heavy B1s. On databases, AWS RDS gives a real managed SQL database for a year, Azure gives 250GB free but only on SQL Server, and GCP's free tier favors Firestore, a NoSQL database, over a managed relational option. Scholion's own [S3 + CloudFront as the default for static sites](/notes/s3-cloudfront-default-site-estatico/) covers the same AWS-versus-Azure trade-off from the deploy side, after migrating away from Azure Static Web Apps.

## Fichamento

- AWS's free-tier philosophy: get developers hooked on proprietary tools (RDS, S3, IAM) during the free 12 months, so the switching cost is too high once billing starts.
- Azure's free-tier philosophy: front-load $200 in credits to demonstrate enterprise-grade power, betting that developers will push for company-wide adoption later.
- GCP's free-tier philosophy: distant third in market share, so it offers the most generous permanent "Always Free" tier to build loyalty among hobbyists and students.
- AWS compute (EC2): 750 hours/month of a t3.micro (2 vCPU, 1GB), throttled once CPU credits run out, and billed at standard rates the moment the 12-month window closes.
- Azure compute (B-Series): the B1s (1 vCPU, 1GB) is weaker than AWS's option for multi-threaded work, and its portal makes it easy to accidentally provision a paid SSD instead of the free HDD.
- GCP compute (Compute Engine): the e2-micro is the only offer that doesn't expire after 12 months, but it's free only in specific regions (us-west1, us-central1, us-east1); deploying elsewhere bills immediately.
- AWS databases (RDS): a real managed relational database (MySQL, PostgreSQL, MariaDB) for 12 months, with egress fees complicating any later migration out.
- Azure databases (SQL Database): 250GB free is generous, but it's Microsoft SQL Server specifically, forcing a stack change for projects built on Postgres or MySQL.
- GCP databases: the free tier favors Firestore (NoSQL); the smallest managed relational (SQL) instance costs $10-15/month.
- Hidden costs common to all three providers: orphaned storage volumes left behind after a server is terminated (~$0.10/GB/month), a charge for holding a static IP while it sits unused (~$3.60/month), and data egress fees that can spike if a hosted file gets hotlinked elsewhere.
- The article's recommendation: AWS for job-market recognition and a straightforward SQL database, GCP for a permanent low-cost personal server, Azure for .NET integration or the 250GB SQL Database allowance.
