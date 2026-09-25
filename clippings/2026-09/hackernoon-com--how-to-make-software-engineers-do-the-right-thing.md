---
url: "https://hackernoon.com/how-to-make-software-engineers-do-the-right-thing?ref=dailydev"
captured_at: "2026-09-25T09:04:25+01:00"
title: "How to Make Software Engineers Do the 'Right Thing'"
domain: "hackernoon-com"
---

## Is a Green Build and Fixing Flaky Tests Your #1 Priority?

I recently had a discussion with the founder of a CI delivery platform about the value of fixing flaky tests, and it led to the following observation/question on LinkedIn:

> _“Over my career, I’ve been in maybe 50 software development teams as an IC. In my current role, I get exposed to 10,000+. If I picked a random person across my entire sample set, they wouldn’t even know where to start with ‘doing the right thing.’ I see way more disengaged engineers who have a ‘give me a ticket and I’ll give you code’ mindset. How would you go about rebooting that?”_

It’s a great question. I thought I’d write about how we’ve approached this in my last two companies. It’s easy to say that culture is the answer, but how do you build that culture? How do you get every member of the team to care about doing the right thing — and what is the _right thing_?

## So Many Priority #1s

It often feels that everything is a top priority. But that, in itself, is part of the problem. Particularly in start-ups and scale-ups, Engineering and Product teams experience immense pressure to deliver. This pressure is often self-imposed - at most of my previous companies, stakeholders were generally willing to accept a temporary slowdown for a long-term increase in quality. Here’s the thing: achieving a stable environment with few bugs takes time, but once you’re there, you can actually deliver faster and more efficiently.

With so much emphasis on features and delivery, it’s no wonder engineers feel torn between addressing quality and stability issues or pushing out new features. So, how do you approach this? While the question of priority is nuanced and will vary from company to company, here’s a list of priorities based on my recent experiences.

## 1\. Build a Culture of Ownership and Accountability

Building a culture of ownership takes time. Like any change, it requires repetition and reinforcement. Start immediately, as this will form the foundation for the following priorities.

## 2\. Record, Prioritize, and Monitor Production Bugs and Defects

It’s surprising how often teams fail to record and prioritize production issues. At UberCarshare, we had a successful product but no way to track bug count or severity. Once you record your production issues, you can start measuring and reporting them. This opens up meaningful conversations with stakeholders about the trade-offs between quality, stability, and new features.

## 3\. Complete Root Cause Analysis (RCA) or Incident Reports for Significant Production Issues

This complements the previous item and is a fundamental pillar of creating a culture of transparency, accountability, and autonomy. RCAs should be blameless: a celebration of transparency, learning, and self-improvement. When engineers feel comfortable writing RCA’s and see that transparency and accountability do not mean blame or punishment, they will feel a greater level of psychological safety.

Tech debt is the root cause of many issues, and while we can’t fix everything immediately, completing RCAs and prioritizing follow-ups against other work is a major step toward prioritizing stability and quality over new features.

## 4\. Establish a Continuous Green Build in CI

I recognize there is an argument that this is a pre-requisite to any of the above but, like I said, it’s nuanced 🤷‍♂️, and a lot of this stuff can happen in parallel. In both of my previous companies, a flaky, unstable CI had become the norm, which is common in teams trying to scale quickly.

You cannot overstate how expensive this is in terms of its impact on productivity, but when there is unclear ownership and accountability, it can be hard to know where to start in fixing it. Getting to a stable build can be a significant effort and may require dedicated resources.

Our approach was as follows:

1.  Get the build consistently green and fast enough — exclude flaky tests as necessary! Address performance or timeout issues through sufficient resourcing and parallelization of tests.
    
2.  Clarify and assign ownership of the excluded flaky tests — the squads owning them can decide whether they need to be fixed and reintroduced.
    

1.  Maintain zero tolerance for flaky tests: if tests become flaky, exclude them from the build until they are fixed

## 5\. Monitoring System Health and Actually Caring About Your Logs

It’s easy to set up error logging and reporting. However, getting your team to care about the logs and respond to them in real-time is far more challenging. Like performance and broken builds, system health needs to be a whole team effort and cannot be left to a DX, DevOps, or maintenance squad. System health relies on culture as much as anything else and once again requires a zero-tolerance approach.

Agree on your tolerance thresholds with the team, ensure that alerts for exceeded thresholds are sent to a public channel, and set an expectation that no one in the team is allowed to walk by a problem. At Carshare, we established an expectation that no one should push an alert further into history by adding a new comment below without first ensuring someone was investigating the issue.

## Use These Principles to Drive a Culture of Autonomy and Accountability

Document these principles and ways of working, workshop with the team on how best to implement them, share them with your product team and stakeholders, and then demand continuous improvement from your team. RCAs, error alerts, and broken builds should be attended to without prompting. Initially, you may need to prompt, nag, coach, and mentor your team.

Above all, reassure them that fixing alerts, broken builds, or bugs really _is_ their highest priority. Eventually, these issues will start to solve themselves, and productivity and output improvements will follow the noticeable improvement in quality and stability.

## Rinse and Repeat: The Path to Continuous Improvement

The five priorities I’ve outlined are just the beginning. Continuous improvement should be ingrained in your process, and there will be many things to perfect:

*   writing efficient tests
*   improving build speed
*   reducing handoffs
*   shifting quality left
*   improved collaboration with partners such as product and design teams
*   measuring quality, uptime, and cycle time
*   etc.

Originally published at [https://medium.com/vertical-slice/getting-software-engineers-to-do-the-right-thing-d42a0b923408](https://medium.com/vertical-slice/getting-software-engineers-to-do-the-right-thing-d42a0b923408?ref=hackernoon.com)
