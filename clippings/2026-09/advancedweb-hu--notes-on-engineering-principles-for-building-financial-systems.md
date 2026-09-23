---
url: "https://advancedweb.hu/shorts/notes-on-engineering-principles-for-building-financial-systems/?ref=dailydev"
captured_at: "2026-09-23T17:31:11+01:00"
title: "Notes on \"Engineering Principles for Building Financial Systems\" - Advanced Web Machinery"
domain: "advancedweb.hu"
---

Notes on "Engineering Principles for Building Financial Systems"
Tamás Sallai
1 min
Photo by Aaron Burden on Unsplash

The three main goals of your accounting system are to be (1) Accurate, (2) Auditable and (3) Timely.

People say naming is the hardest problem in computer science, I would say a close second is addition. After working on large scale financial systems for the past few years, I can't remember how many times the smallest bugs caused large discrepancies in our data.

This is a very good example of how a specific type of bugs work: a small mistake that is not detected early as apparently everything works perfectly grows because of summation and becomes an issue only when encountered many times.

10 million transactions off by 1 cent, leads to a difference of $100k [...] but it's material enough for the government to come after you for underpaying taxes

The cost of the bug is also getting bigger: by the time it is caught it's very hard to attribute to the source. You only see that something is off but not where the discrepancy is coming from.

I see this in many places outside finance as well: a counter that is used to enforce foreign keys in DynamoDB gets out-of-sync and then prevents the parent entity from being deleted, for example someone "fixed" an issue by changing data by hand.
