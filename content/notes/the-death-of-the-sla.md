---
title: "The Death of the SLA"
date: '2015-02-19T06:21:10-03:00'
category: webclip
summary: 'The article argues that negotiating cloud SLAs is a waste of time because providers already focus on availability, penalties are limited, and the legal approach distracts from technical design for failure.'
tags: ["cloud-computing", "service-level-agreement", "availability", "microservices"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "The Death of the SLA"
    url: "http://www.cio.com/article/2883770/cloud-computing/the-death-of-the-sla.html"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2015-02/cio-com--the-death-of-the-sla.md"
    kind: repo
---

The article says the traditional SLA no longer solves cloud availability problems. Providers already work hard on uptime, standard contracts limit their responsibility for outages, and SLA penalties only refund fees rather than covering real losses.

It argues that focusing on SLAs is distracting because it frames infrastructure failure as a legal issue instead of a technical one. The practical response is to design applications for redundancy, partitioning, and elasticity, with automation, standardized components, monitoring, and analytics.

## Reading notes

- Cloud providers already spend time on availability and respond quickly to outages.
- Standard contracts usually promise only best efforts to restore availability.
- SLA penalties refund provider fees, not the losses caused by downtime.
- Continuity insurance is presented as an expensive and difficult alternative.
- Focusing on SLAs can push buyers toward providers who are easier to negotiate with, not those with better capacity, ecosystem, or services.
- The article argues that infrastructure failure should be handled technically, not legally.
- Redundancy is needed because infrastructure can fail and parts of the application can fail too.
- Partitioning, described as microservices, makes updates easier by breaking apps into self-contained components.
- Elasticity requires applications to add or shed components as traffic changes.
- Automation, standardized components, automated configuration, monitoring, metrics, and analytics are needed to operate elastic systems.
- The article concludes that relying on stricter vendor SLAs is misguided and can be irresponsible.
