---
url: "https://dev.to/a_sandrina_p/bringing-a-healthy-code-review-mindset-to-your-team-f8o"
captured_at: "2026-11-16T19:08:59+00:00"
title: "Bringing A Healthy Code Review Mindset To Your Team"
domain: "dev-to"
---

Take a moment to remember the last time you collaborated in a code review. Did your team overcome feedback resistance and manage time expectations? Fostering a healthy mindset is the key to build trust and sharing knowledge with your colleagues.

A code review is a moment in the development process in which you (as a developer) and your colleagues work together and look for bugs within a recent piece of code before it gets released. In such a moment, you can be either the code author or one of the reviewers.

When doing a code review, you might not be sure of what you are looking for. On the other side, when submitting a code review, you might not know what to wait for. This lack of empathy and wrong expectations between the two sides can trigger unfortunate situations and rush the process until it ends in an unpleasant experience for both sides.

In this article, I’ll share how this outcome can be changed by changing your mindset during a code review:

*   [As a team](#as-a-team)
*   [As an author](#as-an-author)
*   [As a reviewer](#as-a-reviewer)

## [](#as-a-team)👩‍💻👨‍💻 As A Team

### [](#foster-out-a-culture-of-collaboration)Foster Out A Culture of Collaboration

Before we start, it’s fundamental to understand the value of [why code needs to be reviewed](https://sophiebits.com/2018/12/25/why-review-code.html). Knowledge sharing and team cohesion are beneficial to everyone, however, if done with a poor mindset, a code review can be a huge time consumer with unpleasant outcomes.

The team attitude and behavior should embrace the value of a nonjudgmental collaboration, with the **common goal of learning and sharing** — regardless of someone else’s experience.

### [](#include-code-reviews-in-your-estimations)Include Code Reviews in Your Estimations

A complete code review takes time. If a change took one week to be made, don’t expect the code review to take less than a day. It just doesn’t work like that. Don’t try to rush a code review nor look at it as a bottleneck.

Code reviews are as important as writing the actual code. As a team, remember to **include code reviews in your workflow** and set expectations about how long a code review might take, so everyone is synced and confident about their work.

### [](#save-time-with-guidelines-and-automatization)Save Time With Guidelines and Automatization

An effective way to guarantee consistent contributions is to integrate a [Pull Request template](https://github.com/stevemao/github-issue-templates) in the project. This will help the author to submit a healthy PR with a complete description. A PR description should explain what’s the change purpose, the reason behind it, and how to reproduce it. Screenshots and reference links (Git issue, design file, and so on) are the final touches for a self-explanatory submission.

Doing all of this will prevent early comments from reviewers asking for more details. Another way of making code reviews seem less nitpicky is to use [linters](https://github.com/collections/clean-code-linters) to find code formatting and code-quality issues before a reviewer even gets involved. Whenever you see a repetitive comment during the review process, look for ways to minimize it (being with better guidelines or code automatization).

### [](#stay-a-student)Stay A Student

Anyone can do a code review, and everyone must receive a code review — no matter the seniority level. Receive any feedback gratefully as an opportunity to learn and to share knowledge. **Look at any feedback as an open discussion rather than a defensive reaction.** As Ryan Holiday says:

> “An amateur is defensive. The professional finds learning (and even, occasionally, being shown up) to be enjoyable; they like being challenged and humbled, and engage in education as an ongoing and endless process. (...)”
> 
> — Ryan Holiday, Ego Is the Enemy

Stay humble because the second you stop being a student, your knowledge becomes fragile.

### [](#the-art-of-selecting-reviewers)The Art Of Selecting Reviewers

In my opinion, picking the reviewers is one of the most important decisions for an effective and healthy code review as a team.

Let’s say your colleague is submitting a code review and decides to tag “everyone” because, unconsciously, she/he might want to speed up the process, deliver the best code possible or making sure everyone knows about the code change. Each one of the reviewers receives a notification, then opens the PR link and sees a lot of people tagged as reviewers. The thought of “someone else will do it” pops up in their minds, leading to ignore the code review and close the link.

Since nobody started the review yet, your colleague will remind each one of the reviewers to do it, i.e. creating pressure on them. Once the reviewers start to do it, the review process takes forever because everyone has their own opinion and it’s a nightmare to reach a common agreement. Meanwhile, whoever decided to not review the code, is then spammed with zillions of e-mail notifications with all of the review comments, thus creating noise in their productivity.

This is something I see happening more than I’d like: Pull Requests with a bunch of people tagged as reviewers and ending, ironically, in a non-productive code review.

There are some common effective flows when selecting the reviewers: A possible flow is to pick two to three colleagues who are familiar with the code and ask them to be reviewers. Another approach, explained by Gitlab team is to have a [chained review flow](https://about.gitlab.com/2017/03/17/demo-mastering-code-review-with-gitlab/) in which the author picks one reviewer who picks another reviewer until at least two reviewers agree with the code. Regardless of the flow you choose, **avoid having too many reviewers**. Being able to trust your colleagues’ code’s judgment is the key to conduct an effective and healthy code review.

### [](#have-empathy)Have Empathy

Spotting pieces of code to improve is just a part of a successful code review. Just as important is to communicate that feedback in a healthy way by showing empathy towards your colleagues.

Before writing a comment, remember to put yourself in the other people’s shoes. It’s easy to be misunderstood when writing, so review your own words before sending them. Even if a conversation starts being ugly, don’t let it affect you — always stay respectful. Speaking well to others is never a bad decision.

### [](#know-how-to-compromise)Know how to compromise

When a discussion isn’t solved quickly, take it to a personal call or chat. Analyze together if it’s a subject worth paralyzing the current change request or if it can be addressed in another one.

**Be flexible but pragmatic** and know how to balance efficiency (delivering) and effectiveness (quality). It’s a compromise to be made as a team. In these moments I like to think of a code review as an iteration rather than a final solution. There’s always room for improvement in the next round.

### [](#inperson-code-reviews)In-person Code Reviews

Gathering the author and the reviewer together in a pair programming style can be highly effective. Personally, I prefer this approach when the code review involves complex changes or there’s an opportunity for a large amount of knowledge sharing. Despite this being an offline code review, it’s a good habit to leave online comments about the discussions taken, especially when changes need to be made after the meeting. This is also useful to keep other online reviewers up to date.

### [](#learn-from-code-reviews-outcomes)Learn from Code Reviews Outcomes

When a code review has suffered a lot of changes, took too long or has already had too many discussions, gather your team together and analyze the causes and which actions can be taken from it. When the code review is complex, **splitting a future task into smaller tasks** makes each code review easier.

When the experience gap is big, adopting pair programming is a strategy with incredible results — not only for knowledge sharing but also for off-line collaboration and communication. Whatever the outcome, always aim for a healthy dynamic team with clear expectations.

## [](#as-an-author)📝 As An Author

One of the main concerns when working on a code review as an author is to minimize the reviewer’s surprise when reading the code for the first time. That’s the first step to a predictable and smooth code review. Here’s how you can do it.

### [](#establish-early-communication)Establish Early Communication

It’s never a bad idea to talk with your future reviewers before coding too much. Whenever it’s an internal or external contribution, you could do a refinement together or a little bit of pair programming at the beginning of the development to discuss solutions.

There’s nothing wrong in asking for help as a first step. In fact, working together outside the review is a first important step to prevent early mistakes and guarantee an initial agreement. At the same time, your reviewers get aware of a future code review to be made.

### [](#follow-the-guidelines)Follow the Guidelines

When submitting a Pull Request to be reviewed, remember to add a description and to follow the guidelines. This will save the reviewers from spending time to understand the context of the new code. Even if your reviewers already know what it is about, you can also take this opportunity as a way to improve your writing and communication skills.

### [](#be-your-first-reviewer)Be your First Reviewer

Seeing your own code in a different context allows you to find things you would miss in your code editor. Do a code review of your own code before asking your colleagues. Have a reviewer mindset and really go through every line of code.

Personally, **I like to annotate my own code reviews** to better guide my reviewers. The goal here is to prevent comments related to a possible lack of attention and making sure you followed the contribution guidelines. Aim to submit a code review just as you would like to receive one.

### [](#be-patient)Be Patient

After submitting a code review, don’t jump right into a new private message asking your reviewers to “take a look, it only takes a few minutes” and indirectly craving for that thumbs-up emoji. Trying to rush your colleagues to do their work is not a healthy mindset. Instead, **trust your colleagues’ workflow** as they trust you to submit a good code review. Meanwhile, wait for them to get back to you when they are available. Don’t look at your reviewers as a bottleneck. Remember to be patient because hard things take time.

### [](#be-a-listener)Be a Listener

Once a code review is submitted, comments will come, questions will be asked, and changes will be proposed. The golden rule here is to not take any feedback as a personal attack. Remember that **any code can benefit from an outside perspective.**

Don’t look at your reviewers as an enemy. Instead, take this moment to set aside your ego, accept that you make mistakes, and be open to learning from your colleagues, so that you can do a better job the next time.

## [](#as-a-reviewer)👀 As A Reviewer

### [](#plan-ahead-of-your-time)Plan Ahead of your time

When you are asked to be a reviewer, don’t interrupt things right away. That’s a common mistake I see all the time. Reviewing code demands your full attention, and each time you switch code contexts, you are decreasing your productivity by wasting time in recalibrating your focus. Instead, plan ahead by allocating time slots of your day to do code reviews.

Personally, I prefer to do code reviews first thing in the morning or after lunch before picking any other of my tasks. That’s what works best for me because my brain is still fresh without a previous code context to switch off from. Besides that, once I’m done with the review, I can focus on my own tasks, while the author can reevaluate the code based on the feedback.

### [](#be-supportive)Be Supportive

When a Pull Request doesn’t follow the contribution guidelines, be supportive — especially to newcomers. Take that moment as an opportunity to guide the author to improve his/her contribution. Meanwhile, try to understand why the author didn’t follow the guidelines in the first place. **Perhaps there’s room for improvement** that you were not aware of before.

### [](#check-out-the-branch-and-run-it)Check Out The Branch And Run It

While reviewing the code, make it run on your own computer — especially when it involves user interfaces. This habit will help you to better understand the new code and spot things you might miss if you just used a default diff-tool in the browser which limits your review scope to the changed code (without having the full context as in your code editor).

### [](#ask-before-assuming)Ask Before Assuming

When you don’t understand something, don’t be afraid to say it and ask questions. When asking, remember to first read the surrounding code and avoid making assumptions.

Most of the questions fit in these two types of categories:

1.  **“How” Questions**  
    When you don’t understand how something works or what it does, evaluate with the author if the code is clear enough. Don’t mistake simple code with ignorance. There’s a difference between code that is hard to read and code that you are not aware of. Be open to learn and use a new language feature, even if you don’t know it deeply yet. However, use it only if it simplifies the codebase.
    
2.  **“Why” Questions**  
    When you don’t understand the “why”, don’t be afraid of suggesting to commenting the code, especially if it’s an [edge case or a bug fix](https://twitter.com/sophiebits/status/1063180141872898048). The code should be self-explanatory when it comes to explaining what it does. Comments are a complement to explaining the why behind a certain approach. Explaining the context is highly valuable when it comes to maintainability and it will save someone from [deleting a block of code that thought was useless](https://cdn-images-1.medium.com/max/1200/0*xhqIOAyiCzYl2z0G.gif). (Personally, I like to comment on the code until I feel safe about forgetting it later.)
    

### [](#constructive-criticism)Constructive Criticism

Once you find a piece of code you believe it should be improved, always remember to recognize the author’s effort in contributing to the project and express yourself in a receptive and transparent way.

#### [](#open-discussions)Open discussions.

Avoid formalizing your feedback as a command or accusation such as “You should…” or “You forgot…”. Express your feedback as an open discussion instead of a mandatory request. Remember to comment on the code, not the author. If the comment is not about the code, then it shouldn’t belong in a code review. As said before, be supportive. Using a passive voice, talking in the plural, expressing questions or suggestions are good approaches to emphasize empathy with the author.

> Instead of “Extract this method from here…” prefer “This method should be extracted…” or “What do you think of extracting this method…”

#### [](#be-clear)Be clear.

A feedback can easily be misinterpreted, especially when it comes to expressing an opinion versus sharing a fact or a guideline. Always remember to clear that right away on your comment.

> Unclear: “This code should be….”
> 
> Opinion: “I believe this code should be…”
> 
> Fact: “Following \[our guidelines\], this code should be…”.

#### [](#explain-why)Explain why.

What’s obvious for you, might not be for others. It’s never too much explaining the motivation behind your feedback, so the author not only understands how to change something but also what’s the benefit from it.

> Opinion: “I believe this code could be…”
> 
> Explained: “I believe this code could be (…) because this will improve readability and simplify the unit tests.”

#### [](#provide-examples)Provide examples.

When sharing a code feature or a pattern which the author is not familiar with, complement your suggestion with a reference as guidance. When possible, go beyond MDN docs and share a snippet or a working example adapted to the current code scenario. When writing an example is too complex, be supportive and offer to help in person or by a video call.

> Besides saying something such as “Using filter will help us to \[motivation\],” also say, “In this case, it could be something like: \[snippet of code\]. You can check \[an example at Finder.js\]. Any doubt, feel free to ping me on Slack.”

#### [](#be-reasonable)Be reasonable.

If the same error is made multiple times, prefer to just leave one comment about it and remember the author to review it in the other places, too. Adding redundant comments only creates noise and might be contra-productive.

### [](#keep-the-focus)Keep the Focus

Avoid proposing code changes unrelated to the current code. Before suggesting a change, ask yourself if it’s strictly necessary at that moment. This type of feedback is especially common in refactors. It’s one of the many trade-offs between efficiency and effectiveness that we need to make as a team.

When it comes to refactors, personally, I tend to **prefer small but effective improvements.** Those are easier to review and there’s less chance of having code conflicts when updating the branch with the target branch.

### [](#set-expectations)Set Expectations

If you leave a code review half-done, let the author know about it, so time expectations are under control. In the end, also let the author know if you agree with the new code or if you would like to re-review it once again later.

Before approving a code review, ask yourself if you are comfortable about the possibility of touching that code in the future. If yes, that’s a sign you did a successful code review!

### [](#learn-to-refuse-a-code-review)Learn to Refuse a Code Review

Although nobody admits it, sometimes you have to refuse a code review. The moment you decide to accept a code review but try to rush it, the project’s quality is being compromised as well as your team’s mindset.

When you accept to review someone’s else code, that person is trusting your capabilities — it’s a commitment. If you don’t have the time to be a reviewer, just say no to your colleague(s). I really mean it; don’t let your colleagues wait for a code review that will never be done. **Remember to communicate and keep expectations clear.** Be honest with your team and — even better — with yourself. Whatever your choice, do it healthily, and do it right.

### [](#conclusion)Conclusion

Given enough time and experience, doing code reviews will teach you much more than just technical knowledge. You’ll learn to give and receive feedback from others, as well as make decisions with more thought put into it.

Each code review is an opportunity to grow as a community and individually. Even outside code reviews, remember to foster a healthy mindset until the day it comes naturally to you and your colleagues. Because sharing is what makes us better!

* * *

This article was [originally written at Smashing Magazine](https://www.smashingmagazine.com/2019/06/bringing-healthy-code-review-mindset/).
