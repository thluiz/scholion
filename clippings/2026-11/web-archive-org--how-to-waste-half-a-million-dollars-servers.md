---
url: "https://web.archive.org/web/20200617050314id_/https://dev.to/heroku/how-to-waste-half-a-million-dollars-474e"
captured_at: "2026-11-18T12:10:22+00:00"
title: "How to waste half a million dollars"
domain: "web-archive-org"
---

![Cover image for  How to waste half a million dollars](https://res.cloudinary.com/practicaldev/image/fetch/s--1K0zf7fL--/c_imagga_scale,f_auto,fl_progressive,h_420,q_auto,w_1000/https://dev-to-uploads.s3.amazonaws.com/i/wf87udwggzpiuwnsjrhs.jpg)

 [![Heroku profile image](https://res.cloudinary.com/practicaldev/image/fetch/s--npu9qqtP--/c_fill,f_auto,fl_progressive,h_50,q_auto,w_50/https://dev-to-uploads.s3.amazonaws.com/uploads/organization/profile_image/123/38b10714-65da-4f1d-88ae-e9b28c1d7a5e.png) Heroku](https://web.archive.org/heroku)

###  [![nocnica profile image](https://res.cloudinary.com/practicaldev/image/fetch/s--Bb-sNIgC--/c_fill,f_auto,fl_progressive,h_50,q_auto,w_50/https://dev-to-uploads.s3.amazonaws.com/uploads/user/profile_image/162459/e4bdaf67-0c0c-4e9d-959a-1d3ef484ae5f.gif) Nočnica Fee](https://web.archive.org/nocnica) [github logo](http://github.com/tobyfee) Jun 15 ・4 min read

Every startup I’ve worked for had the same mission statement. It might not have been the mission statement etched into a plaque on the wall, but it existed just the same. Here it was:

_Make a product so good that people who don’t work for you are excited to tell their friends. Charge people for the product. Make money._

The ‘how’ is missing from this statement, but it’s not the point of this article. I want to talk about how teams get distracted. How some of your best, brightest, most effective people can spend all day working on things that won’t help this mission at all.

## [](#how-we-go-from-make-money-to-run-servers)How we go from ‘make money’ to ‘run servers’

No one starts a company with a goal of getting really good at running servers. They start with a product or service that they want to deliver to customers.

> hey for this whole article I’m pretending like platform/hosting startups don’t exist. Please let me live. Also, this example is centered around a startup but is equally applicable for orgs of all sizes.

Let’s create a company called GoCo. They have a fantastic product that will improve the lives of other software companies and want to take it to the world. The first version of the product will be hosted on something like Heroku. Heroku handles all the updating, patching, and general concerns of making servers serve. Once the product is built GoCo delivers demos, gets some first users, and generates interest at meetups and conferences.

And for a time it is good.

Then as the product grows, and the user base grows, the CFO of GoCo says:

“We’re spending hundreds of dollars on Heroku, we need to set up our own servers to reduce that bill”

One of the most capable engineers at GoCo, let’s call her Grace, spends a couple weeks getting the application running on low cost virtual machines. This is cheaper than a platform and sure enough, the bill goes down.

Money saved, right?

Even right here our theoretical startup has made an error. They saw a reduction of a bill and said they saved money. What everyone forgot was that _they paid Grace the engineer for several weeks of work_ to make this changeover happen. Did the cash saved even equal what they paid, in cash, for Grace to do the work? Probably not, but it gets worse because in that same time Grace could have built something for the product.

### [](#what-could-your-best-engineers-build-if-they-werent-trying-to-save-you-a-few-hundred-bucks-on-servers)What could your best engineers build if they weren’t trying to save you a few hundred bucks on servers?

By tasking Grace the engineer to save you on operational costs, GoCo was depriving itself of the new features and optimizations that could have been delivered in that time. Missing features don’t show up on a balance sheet, but if we don’t deliver cool features and better product _there is no way the startup is going to make money._

The #1 best way for a company to save money is to fire everyone and go out of business. And that’s not in anyone’s mission statement.

### [](#it-gets-worse-eventually-servers-become-a-fulltime-job)It gets worse: eventually servers become a full-time job

Sooner or later GoCo’s servers go down. That discount server farm they use only guarantees that it won’t catch on fire or be physically penetrated, but patching, updating, and configuring servers is GoCo’s job. And Grace, who is just as smart and capable as can be, isn’t even a full-time operations engineer and is probably evaluated on how many features she ships and not how well she patches servers.

GoCo’s executives sit down for a ‘post-mortem:’ the servers went down during a critical conference and everyone is upset. The solution at the time seems clear: GoCo needs an operations specialist or maybe a whole team.

There may be some discussion about what the new salary for this full-time Ops specialist will cost, there probably _won’t \_be a discussion of how bringing on a new engineer can cost [$50,000 in engineer time](https://blog.usejournal.com/it-costs-50k-to-hire-a-software-engineer-d06a0d051abf), bonuses, and start up time. And there definitely won’t be a discussion of how suddenly one of our highest-paid employees is someone whose job has \_absolutely nothing to do with the mission._

I’ve seen executives complain about the cost of customer support, about the cost of team building events and of course the cost of software services. I’ve never seen one complain that some portion of the engineering team no longer deliver great features but instead deliver great servers.

### [](#no-one-ever-says-what-if-we-got-rid-of-all-these-servers)No one ever says ‘what if we got rid of all these servers?’

A year later and GoCo is thriving. Customers are excited, and marketing is talking about a GoCoCon in 2021. The new operations team has great reviews, and in all-staff meetings they celebrate delivering “Five Nines” or 99.999% uptime.

And again, and I’m sorry if I’m hammering the same point, no one ever sits down and says ‘What would Heroku or another Platform-as-a-Service cost us compared to what our entire operation teams costs us?” Because I would submit that a team of 3-4 operations engineers is costing GoCo _half a million dollars a year_.

*   Salary
*   Benefits
*   Stock options
*   Hiring and EOY bonuses
*   Communications overhead
*   Office Overhead

I think $500,000 is a conservative guess for these costs.

And think most managers need to go back and take a look at Platform-as-a-Service as a way to host their products. A comparison with a low-cost EC2-style service should not be based on the relative service bill, but what you’ll spend on the engineers you’ll need and how your entire team will be affected by losing sight of the mission.

 [![twitter logo](https://practicaldev-herokuapp-com.freetls.fastly.net/assets/twitter-f95605061196010f91e64806688390eb1a4dbc9e913682e043eb8b1e06ca484f.svg)](https://twitter.com/intent/tweet?text=%22How%20to%20waste%20half%20a%20million%20dollars%22%20by%20No%C4%8Dnica%20Fee%20%23DEVCommunity%20https://dev.to/heroku/how-to-waste-half-a-million-dollars-474e)[DISCUSS (4)](#comments)

![Copy to Clipboard](https://practicaldev-herokuapp-com.freetls.fastly.net/assets/content-copy-8cf07612d6f4decff7188a5910c4fcd8caf1e7bb73f5a88eb7753a20c728d00e.svg)

## Let's DEV (Together)

### [Join DEV Now](https://web.archive.org/enter)

Open source

Free forever

Level up every day

🔥

Heroku is a container-based cloud Platform as a Service (PaaS). Developers use Heroku to deploy, manage, and scale modern apps. Our platform is elegant, flexible, and easy to use, offering developers the simplest path to getting their apps to market.

[![Heroku](https://res.cloudinary.com/practicaldev/image/fetch/s--sH1bnNH9--/c_fill,f_auto,fl_progressive,h_120,q_auto,w_120/https://dev-to-uploads.s3.amazonaws.com/uploads/organization/profile_image/123/38b10714-65da-4f1d-88ae-e9b28c1d7a5e.png)](https://web.archive.org/heroku)
