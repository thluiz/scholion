---
url: "https://refactoringenglish.com/chapters/techniques-for-writing-emails/"
captured_at: "2025-07-28T08:29:24+01:00"
title: "Underused Techniques for Effective Emails · Refactoring English"
domain: "refactoringenglish-com"
---

---
For software developers, there’s tremendous value in writing effective emails. Good emails save time, reduce misunderstandings, and earn you recognition within your company.

You can drastically improve your emails with a few simple techniques, but too few developers know about them.

-   [What’s an effective email?](https://refactoringenglish.com/chapters/techniques-for-writing-emails/#whats-an-effective-email)
-   [Deliver the most important information first](https://refactoringenglish.com/chapters/techniques-for-writing-emails/#deliver-the-most-important-information-first)
-   [Use the Markdown Here browser extension](https://refactoringenglish.com/chapters/techniques-for-writing-emails/#use-the-markdown-here-browser-extension)
-   [Write complete replies rather than quick ones](https://refactoringenglish.com/chapters/techniques-for-writing-emails/#write-complete-replies-rather-than-quick-ones)
-   [Split threads and curate recipients](https://refactoringenglish.com/chapters/techniques-for-writing-emails/#split-threads-and-curate-recipients)
-   [Create structure with headings and paragraph breaks](https://refactoringenglish.com/chapters/techniques-for-writing-emails/#create-structure-with-headings-and-paragraph-breaks)

## What’s an effective email?[🔗](https://refactoringenglish.com/chapters/techniques-for-writing-emails/#whats-an-effective-email)

An effective email has five key qualities:

1.  **Clear**: Recipients understand what the email is telling them without additional clarification.
2.  **Action-oriented**: The email makes it clear what actions you expect of the email’s recipients.
3.  **Relevant**: Recipients quickly recognize why the information is relevant to them.
4.  **Efficient**: You and your recipients achieve your goals while minimizing everyone’s time reading and responding to the email thread.
5.  **Succinct**: The email maintains a high signal-to-noise ratio.

## Deliver the most important information first[🔗](https://refactoringenglish.com/chapters/techniques-for-writing-emails/#deliver-the-most-important-information-first)

When you see a co-worker in person, you typically don’t blurt out your most important thought before even saying hello, but that’s the right thing to do in email.

Your co-workers receive hundreds of emails per day. They don’t have time to read every email in full, so they skim their inbox to find what’s relevant to them.

To ensure that your recipients see the information they need, present the most important information in your email first.

As an exercise, here’s an intentionally boring and long-winded email. Give it a quick skim to see if you can spot anything worth reading:

> Subject: A surprise discovery  
> To: hamsterchat-team@example.com, devops@example.com  
> 
> ___
> 
> Hi All,
> 
> I was playing checkers with my dog, Sgt. Francisco, when I noticed that his ID tag had fallen off his collar. It may have been gone for months.
> 
> It made me wonder about other safety measures that I might be taking for granted. So, I started thinking about HamsterChat’s data backups.
> 
> On a hunch, I went to our data center last night at around 8 PM to test my theory. I talked to Tony, the admin there, and he set me up with a crash cart at our server. Sure enough, every backup snapshot I tested was corrupt and unrecoverable. I was able to isolate the problem to a faulty RAM stick. Boy, was that a surprise! Tony had never seen anything like it.
> 
> Goes to show that thinking about adjacent problems is worthwhile!
> 
> Sincerely,  
> William Hamsterton-Chatsworth

Unless you read the above email in full, you probably missed the most important detail: **all the backups are gone**.

For important emails, start with a one-line summary or a short list of bullet points before you even get to “Hello.” After the summary, present the supporting details in descending order of importance.

Here’s the previous email, rewritten to present the most important information first:

> Subject: Failure in HamsterChat backups - all backups lost  
> To: hamsterchat-team@example.com, devops@example.com  
> 
> ___
> 
> **tl;dr: All historical HamsterChat backups are corrupt and unusable. Backups are healthy again starting today.**
> 
> Hi All,
> 
> Due to a hardware failure in our storage server, all of our HamsterChat backups are corrupt. I’ve replaced the faulty hardware and verified that backup and restore operations are healthy.
> 
> I’m working with our DevOps team to automate a weekly backup and restore test. If anything corrupts our backups in the future, we’ll catch it within a week rather than stumbling across the issue months later by chance.
> 
> From digging into the logs and running diagnostics, I isolated the cause to a faulty RAM stick in our storage server. It appears that it was silently flipping bits on disk writes, so the filesystem thought the write succeeded, but the data that landed on the disk was corrupt.
> 
> After replacing the RAM stick, I took a backup and successfully restored it to a fresh disk. This strongly supports my hypothesis that the faulty RAM stick was to blame.
> 
> Sincerely,  
> William Hamsterton-Chatsworth

Some organizations call this style of writing [bottom-line, up front (BLUF)](https://en.wikipedia.org/wiki/BLUF_(communication)). Journalists call this [“the inverted pyramid”](https://en.wikipedia.org/wiki/Inverted_pyramid_(journalism)) because the information becomes relevant to a smaller and smaller audience as you get deeper into the text.

![An inverted pyramid](https://refactoringenglish.com/chapters/techniques-for-writing-emails/inverted-pyramid.svg)

Journalists structure news reports in an inverted pyramid, where the information relevant to the most people is at the top.

Note how the information in the email above matches the inverted pyramid style:

![An inverted pyramid](https://refactoringenglish.com/chapters/techniques-for-writing-emails/inverted-pyramid-applied.svg)

Details from the original email about the dog and the data center admin no longer appear in the revised email. Those details were irrelevant, so cutting them maintains a high signal-to-noise ratio, making it easier for recipients to capture important details.

## Use the [Markdown Here](https://markdown-here.com/) browser extension[🔗](https://refactoringenglish.com/chapters/techniques-for-writing-emails/#use-the-markdown-here-browser-extension)

Markdown Here is [a free, open-source browser extension](https://markdown-here.com/) that lets you write emails in Markdown.

As a software developer, my emails frequently contain code snippets and inline code. Markdown Here makes it easy to format code clearly and add simple formatting right from the keyboard.

I compose emails in Markdown like this:

[![](https://refactoringenglish.com/chapters/techniques-for-writing-emails/markdown-here-before.webp)](https://refactoringenglish.com/chapters/techniques-for-writing-emails/markdown-here-before.webp)

Then, I hit `Ctrl+Alt+M`, and Markdown Here turns my email into this:

[![](https://refactoringenglish.com/chapters/techniques-for-writing-emails/markdown-here-after.webp)](https://refactoringenglish.com/chapters/techniques-for-writing-emails/markdown-here-after.webp)

I’m baffled that Markdown Here isn’t a thousand times more popular. I’ve been recommending it for a decade, and whenever I tell people about it, I feel like I’m in [that movie](https://en.wikipedia.org/wiki/Yesterday_(2019_film)) where the guy wakes up one day, and nobody else knows who The Beatles are.

When an email is sitting in your inbox, a part of you just wants to get rid of it as quickly as possible. The email represents work, and the sooner you reply, the sooner you can stop thinking about that work.

Sending a quick reply feels like completing a work task, but you’re actually creating more work for yourself and your teammates.

To show what I mean, here’s an email thread where everyone responds quickly:

> Subject: Custom build for Optimoji  
> To: pm-team@example.com; dev-team@example.com
> 
> ___
> 
> Optimoji agreed to participate in our HamsterChat beta, but they only have ARM servers.
> 
> Can you compile an out-of-band ARM build for them?

> Subject: Custom build for Optimoji  
> To: pm-team@example.com; dev-team@example.com
> 
> ___
> 
> Which version of ARM?

> Subject: Custom build for Optimoji  
> To: pm-team@example.com; dev-team@example.com
> 
> ___
> 
> I’m not sure. They’re running Ampere Altra Max machines.

> Subject: Custom build for Optimoji  
> To: pm-team@example.com; dev-team@example.com
> 
> ___
> 
> Okay, Ampere Altra Max is ARM v8.2a.
> 
> Do you want the Pro or Enterprise version for them?

> Subject: Custom build for Optimoji  
> To: pm-team@example.com; dev-team@example.com
> 
> ___
> 
> Enterprise.

> Subject: Custom build for Optimoji  
> To: pm-team@example.com; dev-team@example.com
> 
> ___
> 
> Do they need the multi-language extension, or is it just `en-US`?

> Subject: Custom build for Optimoji  
> To: pm-team@example.com; dev-team@example.com
> 
> ___
> 
> English only.

> Subject: Custom build for Optimoji  
> To: pm-team@example.com; dev-team@example.com
> 
> ___
> 
> Okay, here you go.

Had either participant in the thread put more care into their emails, they would have recognized that they were omitting critical details or failing to solicit them.

The thread above is eight emails, but let’s assume that there were 10 people on the thread. That’s now 80 emails, meaning this trivial thread caused 80 collective context switches for employees across this company.

Had the participants instead optimized for complete replies, they could have resolved this thread in two emails:

> Subject: Custom build for Optimoji  
> To: pm-team@example.com; dev-team@example.com
> 
> ___
> 
> Optimoji agreed to participate in our HamsterChat beta, but they only have ARM servers (Ampere Altra Max).
> 
> Can you do a custom build for them with these properties?
> 
> -   Architecture: ARM
> -   Tier: Enterprise
> -   Language: en-US only

> Subject: Custom build for Optimoji  
> To: pm-team@example.com; dev-team@example.com
> 
> ___
> 
> Sure, see attached.
> 
> Ampere Altra Max is ARMv8, so I added that to our build matrix for the next release.
> 
> If they need updates in the future, they can download our standard release builds as long as they choose ARMv8 flavor.

Cal Newport describes this style of managing email as [process-centric email](https://calnewport.com/write-longer-emails/). Newport recommends treating every email thread as a problem the recipients must solve. The goal is to create a process for solving that problem in as few emails as possible.

## Split threads and curate recipients[🔗](https://refactoringenglish.com/chapters/techniques-for-writing-emails/#split-threads-and-curate-recipients)

Sometimes an email thread drifts beyond its original scope. The subject line no longer represents the conversation accurately, and the recipients are no longer be the right participants for the discussion.

When an email’s scope changes, actively split the thread to eliminate noise by doing the following:

1.  Update the subject line to match the new scope of the discussion.
2.  Move any recipients to bcc if the thread is no longer relevant to them.
3.  Add any new recipients for whom the thread is relevant.
4.  Briefly explain the context of the thread for the people you added.

As a concrete example, imagine that you start an email thread to review a design document:

> Subject: HamsterChat v2 design review  
> To: architecture-astronauts@example.com; hamsterchat-dev@example.com
> 
> ___
> 
> Hi All,
> 
> The HamsterChat v2 design document is now ready for review:
> 
> https://example.com/docs/hamsterchat-v2-spec/edit
> 
> \-William

Everyone signs off on the design, but someone suggests looping in the infrastructure team to coordinate hardware resources.

The anti-pattern at this stage would be to add the infrastructure team to the thread and ask them a vague question:

> Subject: HamsterChat v2 design review  
> To: **infrastructure@example.com**  
> Cc: hamsterchat-dev@example.com; architecture-astronauts@example.com
> 
> ___
> 
> Infrastructure folks - can you weigh in here?

What’s wrong with that email?

A lot, actually:

1.  You’re forcing the infrastructure team to dig through the thread to understand what you’re asking them.
2.  The subject line is still “HamsterChat design review,” even though it’s no longer a design review.
3.  You’re dragging along a bunch of people from the design review who don’t care about coordinating hardware resources, so the email is now pure distraction for them.

You can solve all of those problems by splitting the thread:

> Subject: HamsterChat Q3 infra resources WAS: HamsterChat v2 design review  
> To: infrastructure@example.com  
> Cc: hamsterchat-dev@example.com  
> Bcc: architecture-astronauts@example.com
> 
> ___
> 
> _\[adding infrastructure@, moving architecture-astronauts@ to bcc\]_
> 
> Hi Infrastructure Folks,
> 
> We’re planning to introduce a new version of HamsterChat in Q3 (see thread below).
> 
> The new service will require at least two 4-vCPU application servers and one 2-vCPU database server for testing. Will the infrastructure team be able to provide that by Q3?
> 
> \-William

## Create structure with headings and paragraph breaks[🔗](https://refactoringenglish.com/chapters/techniques-for-writing-emails/#create-structure-with-headings-and-paragraph-breaks)

When talented speakers give presentations, they write every slide with care. They break up their talking points into small, digestable chunks, and they choose descriptive yet succinct headings.

When you’re writing a long email, think about it the same way you’d present a slide deck. Focus each paragraph around a single idea. When in doubt, err on the side of shorter sentences and paragraphs. If your emails begin to look like LinkedIn clickbait, that’s too short.

> Subject: Severe HamsterChat outage - all regions affected  
> To: all-staff@example.com
> 
> ___
> 
> Have you ever noticed that our website is unreachable?
> 
> I noticed.
> 
> And once I saw it, I couldn’t unsee it.
> 
> The cause? A stray curly brace in our nginx config.
> 
> Click below👇 for five unbeatable strategies to prevent outages.

For emails longer than about five paragraphs, use headings to help your readers recognize the structure of your email.

> Subject: HamsterChat rollout plan  
> To: all-staff@example.com
> 
> ___
> 
> We are still on track for **the HamsterChat global release on Wednesday, July 16**.
> 
> There are many delicate pieces to this launch, so I’ve summarized them all to ensure that we’re all on the same page.
> 
> ### Release announcement[🔗](https://refactoringenglish.com/chapters/techniques-for-writing-emails/#release-announcement)
> 
> We’ll publish the release announcement to our blog on Wednesday at 12:01am ET.
> 
> We got a lot of great tips from [the release announcements chapter in _Refactoring English_](https://refactoringenglish.com/chapters/release-announcements/), so we anticipate 10+ million visitors within the first few minutes.
> 
> ### Product Hunt launch[🔗](https://refactoringenglish.com/chapters/techniques-for-writing-emails/#product-hunt-launch)
> 
> HamsterChat will launch on Product Hunt on Wednesday at 3:01am ET.
> 
> We purchased Product Hunt’s Authentic Indie Platinum package, which guarantees that HamsterChat finishes the day in the #1 spot from organic votes.
> 
> We anticipate the visibility on PH to bring in as many as four (4) unique visitors.
> 
> ### TechCrunch interview[🔗](https://refactoringenglish.com/chapters/techniques-for-writing-emails/#techcrunch-interview)
> 
> …

Section headings are also helpful when your email has multiple audiences who care about different subsets of your email. When you’re emailing multiple teams, headings allow readers to zero in on the parts of your email that matter to them.

## Summary[🔗](https://refactoringenglish.com/chapters/techniques-for-writing-emails/#summary)

-   Effective emails are clear, action-oriented, relevant, efficient, and succinct.
-   Structure emails to deliver the most important information first, potentially with one-line summaries or bullet points.
-   Use the Markdown Here browser extension to format your emails beautifully.
-   Replying quickly is less important than minimizing the number of emails in a thread.
-   Update the subject line and recipients when a thread’s scope drifts from its original purpose.
-   Use headings and paragraph breaks to help recipients understand the structure of your emails.
