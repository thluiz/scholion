---
url: "https://newsletter.manager.dev/p/the-price-of-mandatory-code-reviews?hide_intro_popup=true"
captured_at: "2025-10-28T19:07:09+00:00"
title: "The price of mandatory code reviews - by Anton Zaides"
domain: "newsletter-manager-dev"
---

---
“You should do code reviews” is an unwritten law of software engineering. Like “Always have a rollback plan” and “Everything should be saved in Git”.

In every company I worked for in the last 15 years, we had mandatory code reviews (at least one, usually two reviewers per PR).

Over the last month, I’ve begun to reconsider this ‘law’. For the first time, I’ve met production teams that don’t have mandatory code reviews.

For example, at [Pylon](https://www.usepylon.com/), engineers merge their own code and only request reviews if they need input, think they have a risky change, or are still onboarding. Their thought process is: if we hire skilled engineers and trust them, there’s no reason to bottleneck every change with mandatory reviews.

This actually makes a lot of sense, but I still felt uncomfortable.

So I decided to check the data (400+ companies and 3000+ engineers on [Weave](https://workweave.dev/)) in the past month to answer 5 questions:

1.  Are teams without code reviews actually faster?
    
2.  Are code reviews reducing bugs?
    
3.  Does the quality of code reviews matter?
    
4.  Does the turnaround speed of code reviews matter?
    
5.  How do top organizations work?
    

## **No code reviews - is it worth it?**

Clear answer here: no reviews means faster shipping, but way more bugs.

[

![](https://substackcdn.com/image/fetch/$s_!Z8rO!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8194f9d7-655a-43c9-b5fe-dfbe38a10939_1024x768.png)

](https://substackcdn.com/image/fetch/$s_!Z8rO!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8194f9d7-655a-43c9-b5fe-dfbe38a10939_1024x768.png)

#### **The bottom line**

Teams with reviews: 31 expert hours, 3.7 bugs per developer.

Teams that **didn’t** perform code reviews had a x1.9 times higher output (~59 expert hours/developer), but **x2.4 times more bugs! (**8.9/developer).

Even accounting for higher productivity, that’s 25% more bugs per expert hour of work. So yes, skipping reviews makes you faster. But you’re also shipping significantly buggier code.

Now a quick explanation of the terms used:

#### **Bug**

For every PR we analyze, we use an LLM to classify the type of work. Relying only on project management tools (like Jira) isn’t accurate, as many changes happen without being related to tickets.

We have 3 types:

-   **Feature** - introduces new functionality or innovation.
    
-   **Bug** - fixes something that is broken or not working as intended.
    
-   **KLTO** (Keep the lights on) - maintenance work that keeps the system running but doesn’t introduce new functionality.
    

The data in the charts shows the average number of bugs per developer during September.

#### **Output**

We use a metric we call ‘expert hours’. We define an expert as an engineer with 5+ years of experience who is deeply familiar with the codebase. To evaluate the PRs, we use a combination of LLMs and our own models.

To provide a reference point, the average is ~10 expert hours per week, ~40 per month.

#### **Reviews per PR**

The number of pull requests, divided by the number of reviews done with at least one comment.

How I defined the groups:

-   No reviews - orgs with less than 1 review per 10 PRs.
    
-   With reviews - orgs with more than 1 review per 2 PRs.
    

Now let’s look at the full spectrum:

## \# of code reviews vs bugs

[

![](https://substackcdn.com/image/fetch/$s_!31jt!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff3deaf34-0d93-4095-8b5f-38eb801de25b_1024x768.png)

](https://substackcdn.com/image/fetch/$s_!31jt!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff3deaf34-0d93-4095-8b5f-38eb801de25b_1024x768.png)

As you would expect, more code reviews => fewer bugs.

The biggest gains happen between 0 and 0.5 reviews per PR - after that, diminishing returns kick in.

I think it makes sense - for some PRs it’s ok to not have mandatory code reviews. Let’s say you want to improve a log message - it’s very annoying to need to ask people to review it.

Code reviews work, but you don’t have them on every single PR.

Next, let’s talk about code review quality:

## **The quality of code reviews matters**

How I defined quality groups: companies with average review scores below 75 vs. above 75 (with at least 1 review per 10 PRs):

[

![](https://substackcdn.com/image/fetch/$s_!u8qB!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2b86cbe5-a07e-4a43-b596-f1b3a2a7dbeb_1024x768.png)

](https://substackcdn.com/image/fetch/$s_!u8qB!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2b86cbe5-a07e-4a43-b596-f1b3a2a7dbeb_1024x768.png)

Yes, higher quality reviews make you go 38% slower - but you get 61% fewer bugs.

If you’re going to do reviews, make them count.

_For each code review, we measure review quality based on depth of engagement, clarity of communication, and practicality of feedback. The average review score is ~75._

## **Fast PR turnaround is critical**

[

![](https://substackcdn.com/image/fetch/$s_!ZRCR!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Feed7f168-2f48-4a92-9b77-6952e9413cf8_1024x768.png)

](https://substackcdn.com/image/fetch/$s_!ZRCR!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Feed7f168-2f48-4a92-9b77-6952e9413cf8_1024x768.png)

If you do code reviews, at least do them fast enough to not block people.

Teams reviewing PRs in under 3 hours are 2.1x more productive than teams taking 8+ hours!

Looking at 500K PRs opened by 3K+ engineers, here’s the breakdown:

\- 25% get reviewed in <1 hour  
\- 31% in 1-3 hours  
\- 34% in 3-8 hours  
\- 10% wait 24+ hours

In my experience, slow reviews don’t just hurt productivity, they also create a lot of frustration and kill morale.

I love [Google’s guidelines](https://google.github.io/eng-practices/review/reviewer/standard.html): “If you are not in the middle of a focused task, you should do a code review shortly after it comes in.”

## **How do top-performing teams work**

Here’s the surprising part: the best teams ship fast AND maintain quality. Top 10% teams are 2.7x faster while keeping bugs per feature 33% lower:

[

![](https://substackcdn.com/image/fetch/$s_!n5WZ!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa57587d2-e65d-4b5b-b6d3-67e5e2aac770_1024x768.png)

](https://substackcdn.com/image/fetch/$s_!n5WZ!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa57587d2-e65d-4b5b-b6d3-67e5e2aac770_1024x768.png)

_Our dataset focuses on startups and high-growth companies where these patterns are most visible._

Let’s take a team of 5 in a median company:

-   It will have ~185 expert hours in a month.
    
-   Let’s assume it translates to ~5 new features
    
-   They will have 30 bugs - an average of 6 bugs per feature
    

Now let’s take a similar team of 5 in a 90th percentile company:

-   It will have ~500 expert hours in a month
    
-   Resulting in 14 new features
    
-   They will have 60 bugs - meaning a bit above 4 bugs per feature!
    

Yes, **more total bugs - but better bugs-per-feature ratio.**

As for PRs:

-   In a median company, an engineer opens ~1 PR a day.
    
-   In a top 10% company, the number jumps to ~2.2 PRs per day.
    

## **What you give is what you get**

One last question: are there engineers who give great reviews but get garbage back? Or free-riders who get thorough reviews without contributing?

[

![](https://substackcdn.com/image/fetch/$s_!eq4V!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9243cfc9-e192-4fe0-b942-bcba8f3e41db_1024x768.png)

](https://substackcdn.com/image/fetch/$s_!eq4V!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9243cfc9-e192-4fe0-b942-bcba8f3e41db_1024x768.png)

The circle sizes are the clusters. As Canva allows for only 1000 rows, I clustered similar values together.

The answer is no. There’s a strong correlation between the quality of reviews you give and what you receive. In most cases, the company culture wins - if you’re giving low-effort reviews, you’re probably getting them too.

## **Final words**

There’s a lot of value in code reviews beyond just catching bugs. They help everyone get on the same page about how we write code, and they spread knowledge so everything isn’t stuck in a single engineer’s head.

Still, it’s worth rethinking your flow once in a while. It’s very easy to get stuck with [inertia](https://read.perspectiveship.com/p/inertia) and keep doing things the same way just because that’s how you’ve always done them. As we saw [last week](https://newsletter.manager.dev/p/what-a-10x-team-looks-like), there’s a lot of room for innovation in how teams work.

I don’t plan to abandon code reviews anytime soon. But I will experiment with making them selective - thinking about which cases actually need reviews, and making sure the ones we do are **high quality and fast**.

### Discover Weekly

1.  [Everyone should be using Claude Code more](https://www.lennysnewsletter.com/p/everyone-should-be-using-claude-code) by
    
    . I’ve fallen in love with Claude Code in the past few month. Some amazing ideas in the article!
2.  [Culture = Results](https://gregtidanian.substack.com/p/culture-results) by
    
    . Interesting take on company culture.
3.  [Maximizers vs. Focusers](https://cutlefish.substack.com/p/tbm-383-maximizers-vs-focusers) by
    
    . On working with **Maximizers** (biased to speed, optionality, breadth, momentum, opportunism, parallel bets, hype) and **focusers** (biased to focus, coherence, depth, meaningful constraints, doing less for more, sequential experiments, intentionality, sustainability).
4.  [Observe, assert, and validate (OAV)](https://newsletter.weskao.com/p/observe-assert-and-validate-oav) by
    
    . A refreshing take on why asking ‘how can I be helpful to you’ is not such a code practice.
