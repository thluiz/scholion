---
url: "https://gkogan.co/blog/simple-systems"
captured_at: "2026-11-16T02:18:00+00:00"
title: "Simple Systems Have Less Downtime"
domain: "gkogan-co"
---

The Maersk Triple-E Class container ship is 1,300 feet long, carries over 18,000 containers across 11,000 miles between Europe and Asia, and… Its entire crew can fit inside a passenger van.

![](https://storage.ghost.io/c/d0/6d/d06d2768-1e39-4bc0-baab-7dfb7d336fd2/content/images/2024/07/maersk-container-ship.jpg)

As a former naval architect and a current [marketing consultant to startups](https://www.gkogan.co/), I found that the same principle that lets a 13-person crew navigate the world’s largest container ship to a port halfway around the world without breaking down also applies to startups working towards aggressive growth goals:

**Simple systems have less downtime.**

Ships contain simple systems that are easy to operate and easy to understand, which makes them easy to fix, which means they have less downtime. An important quality, considering that “downtime” for a ship could mean being stranded thousands of miles from help.

Take the ship’s steering system, for instance. The rudder is pushed left or right by metal rods. Those rods are moved by hydraulic pressure. That pressure is controlled by a hydraulic pump. That pump is controlled by an electronic signal from the wheelhouse. That signal is controlled by the autopilot. It doesn’t require a rocket scientist or a naval architect to find the cause of and solution to any problem:

*   If the autopilot fails, steer the ship manually from the wheelhouse.
*   If the electronic signals fail, go to the rudder control room to control the pump by hand, while talking with the bridge through a [simple sound-powered phone](https://en.wikipedia.org/wiki/Sound-powered_telephone?ref=gkogan.co).
*   If the hydraulics fail, use the mechanically linked emergency steering wheel.
*   If the mechanical linkage fails, hook a chain to both sides of the rudder and pull in the direction you want!

![](https://storage.ghost.io/c/d0/6d/d06d2768-1e39-4bc0-baab-7dfb7d336fd2/content/images/2024/07/174.jpg)

Startups, like ships, can’t afford to stall from system downtimes. Extended downtime in sales, marketing, web, customer support, hiring, product, and other systems may cause irreparable damage to the growth rate.

(Although automation is prevalent on modern ships, it only affects the time it takes to do things and the attention required to monitor everything. The propulsion and auxiliary systems are more simple than ever, thanks to modern diesel and electric propulsion systems that replaced pipe-laden steam plants.)

## Why Simplicity Leads to Less Downtime

### 1\. Proficiency takes less time.

If the person responsible for the system leaves, falls overboard, [gets hit by a bus](https://en.wikipedia.org/wiki/Bus_factor?ref=gkogan.co), or gets pulled into another project, another person can take over without much learning or training. That means more people are able to step in to troubleshoot and fix issues.

For example, an analytics dashboard built with Tableau is likely to have more qualified people to fix it than one built with a patchwork of custom scripts and APIs. Nobody should have to pull data scientists or product developers away from their work to fix a bar chart.

### 2\. Troubleshooting takes less time.

In a system where the behavior of each component and its relationship to other comments is easily understood, ruling out issues and finding the broken component — the root cause — is more intuitive.

For example, if a company has many downloadable whitepapers on their website, and they’re all gated behind a single form—as opposed to a custom form for each one — then they need only troubleshoot one form and one automation workflow if the whitepaper downloads stop working.

![](https://storage.ghost.io/c/d0/6d/d06d2768-1e39-4bc0-baab-7dfb7d336fd2/content/images/2024/07/91.jpg)

### 3\. More alternative solutions.

When each part of the system has a clear function, alternatives are easier to find.

For example, imagine a Salesforce process that uses a mishmash of automation and third-party tools to score, filter, classify, and assign new sales leads. If that fails then there is no obvious replacement. Everything will be put on hold until the process is fixed or replaced with a similarly complex solution.

Now imagine a sales process in which the sales team is simply notified of each new sales lead along with pertinent details, letting them decide whether or not to follow up with the lead. If the Salesforce notification step fails, it’s easy to come up with a hundred other ways of getting that information to the sales team: Reports, Slack notifications, list exports, manual observation, or using Zapier to send an alert through virtually any medium. The downtime would last a few minutes, at most.

![](https://storage.ghost.io/c/d0/6d/d06d2768-1e39-4bc0-baab-7dfb7d336fd2/content/images/2024/07/77.jpg)

* * *

## Startup Story

One of my clients was using a legacy enterprise marketing automation platform (Marketo) with 629 automated processes built up over several years. When something broke or needed tweaking, there was only one person among the 150+ employees who could do it. Each issue took several days or even weeks to fix, all the while marketing campaigns stalled. And with each patch, the overall system only grew more complex.

![](https://storage.ghost.io/c/d0/6d/d06d2768-1e39-4bc0-baab-7dfb7d336fd2/content/images/2024/07/127.jpg)

When that person left the company, there was nobody left to operate the system. With every passing week a new issue would come up, faster than we could find and fix them.

To keep the marketing operation from coming to a standstill, I rushed to migrate the company from Marketo to HubSpot, a more simple platform that would be easier to operate and troubleshoot.

The migration took just one week. Along the way, however, another complex system reared its head: Salesforce. There were 10 automated processes in Salesforce with over 100 combined operations, all dependent on various delicately timed automations in Marketo. It took two weeks—twice as long as the migration—to understand and integrate those processes with the new marketing platform.

![Cartoon about being stranded on an island](https://storage.ghost.io/c/d0/6d/d06d2768-1e39-4bc0-baab-7dfb7d336fd2/content/images/2024/07/193.jpg)

Overall, these two complex systems (in Marketo and in Salesforce) resulted in six weeks of downtime for the marketing team and three weeks of downtime for the sales team. That’s not counting the many weeks of downtime they experienced throughout the past few years, nor the many weeks of downtime they would experience in the future if we did not overhaul the underlying systems.

In the end, the system I put in place had 97% fewer processes (from 629 to 20) while providing all the same capabilities. A bug that was found a few days later got resolved in four minutes.

This experience made me wonder what principles startups can adopt to avoid the pitfalls of complex systems.

## Principles for Simple Systems

Rip-and-replace projects are painful and disruptive, even when the long-term benefits are worth it. Many startups—as with ships—don’t have the luxury of time and resources to perform overhauls once they’re underway.

Here are my three principles to follow when evaluating or implementing new systems:

1.  **Features don’t justify complexity.** What good is a complicated flight control system if it grounds an entire fleet of aircraft, or an enterprise marketing platform like Marketo if nobody can run a marketing campaign? Choose tools that are simple to operate over those that promise the most features. A frequent recommendation I give to startups is to choose HubSpot for their marketing platform instead of an enterprise platform like Marketo, Eloqua, or Pardot.
2.  **Complex ideas lead to complex implementations.** If it takes too long to explain or grasp an idea, then its implementation will be complex, and it will take too long to fix when something inevitably breaks. For example, a proposed sales process that requires an hour-long presentation will be a nightmare to maintain, regardless of how clever it seems.
3.  **Modifications before additions.** When new requirements come up, the tendency is to add layers on top of the existing system—by way of additional steps or integrations. Instead, see if the system’s core can be modified to meet the new requirements. The change may cause (planned) downtime upfront, as with my Marketo-to-HubSpot migration example, but less (unplanned) downtime over the long term.

## Smooth Sailing

> “… the more simple any thing is, the less liable it is to be disordered, and the easier repaired when disordered.” — Thomas Paine, Common Sense, 1776

There’s no question things will break along the startup journey, just as surely as they do on a ship crossing the globe. However, if the onboard systems are simple, those issues won’t leave the startup drifting helplessly in the middle of the ocean.
