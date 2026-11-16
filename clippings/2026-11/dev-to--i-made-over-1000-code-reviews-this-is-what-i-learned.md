---
url: "https://dev.to/mjuraj/i-made-over-1-000-code-reviews-this-is-what-i-learned-4e9e"
captured_at: "2026-11-16T01:33:49+00:00"
title: "I made over 1,000 code reviews - this is what I learned"
domain: "dev-to"
---

Over the last 3 years, I’ve reviewed more than 1,000 pull (merge) requests. During that time I learned a lot – mostly about how not to review code, how to make the process less painful, what makes good-quality code and so on.

## [](#pull-request-needs-to-do-just-one-thing)Pull request needs to do just one thing

This is the single most important thing to watch out for!

While doing a code review, you need to keep a lot of things in your head. _“What is the intention behind this?”_, _“How does this comply with the rest of the code?”_ and _“Will this perform well?”_ are just some of the questions that need to be answered. So, when you have a focused pull request that is trying to solve a single problem, some of those questions become easier to answer.

Another important aspect is the size of the pull request. Bigger requests require exponentially more time to review. And when I know that I’ll need to spend more than 15 minutes on the request, you’ll have to wait up to a couple of hours.

Larger pull requests also have more mistakes, so the time to get approved will also increase significantly. That means that you could have code waiting to get approved for days. And if your company is agile, that increases the chances for merge conflicts which are just painful.

> The best thing to do is split pull requests into meaningful pieces – one pull request should solve just one thing.

So, watch out for the common traps like _renamings_, _code generalizations_, and such. Although innocent and done with good intent, it removes focus from important parts – raising code quality and reducing error count. Just do your genius idea in another pull request.

## [](#automate-as-many-checks-as-possible)Automate as many checks as possible

Continuing on the notion that a reviewer has to keep a lot of things in his head, that also includes checking code formatting, the existence of appropriate documentation, passable tests, and so on. I remember the time when I had to take all that into consideration – it was distracting and time-consuming.

Good thing is that the solution is pretty simple – integrate all the checks into the CI pipeline. That basically runs all the checks whenever someone submits a pull request, and won’t allow merging before all the checks pass. You as the reviewer will never have to worry about formatting again.

_Automated tests_ help make sure that the author didn’t break anything, and that the tests are still passing. Depending on your approach to tests, this is easily the most important check to have in your pull request CI.

_Automated code_ formatting makes all the arguments around ideal line-length or where to add newline disappear. Just pick a set of formatting rules as a team and give it to the auto-formatter. This will rid you of a lot of nuisance. If you’re having problems agreeing to a format, take a look at how Google, Facebook, or some other big companies are doing it.

_Automated lint_ checker is also very important for languages like Python where code formatting affects code logic. Most code formatters for Python will only format code for which they know for sure won’t affect any logic. By adding the lint checker you’ll cover everything.

Some honorable mentions are _type checker_ and _documentation checker_, but the most important thing is to automate checks that make sense for you and your team. If you think something would help, talk it out and try it for a week or two.

## [](#sit-with-the-author-to-review-the-code)Sit with the author to review the code

It makes the review process faster since you’re able to iterate faster over the code with the author and share your point of view. The author can also better explain the reasoning behind his approach, like if he tried something already and why it didn’t work.

This can also be a great opportunity to connect with people more, which is very important. When your fellow developers see that you’re invested in their personal and business growth, they will appreciate it. This is also a great opportunity for you and the author to practice your communication which is crucial for well-functioning teams.

Watch out not to over-do this though. Some pull requests are too small and too simple to have any impactful conversation. In that case sitting down with the author might be a waste of time.

## [](#be-considerate-when-writing-reviews)Be considerate when writing reviews

If you’re more experienced than the author of the code, you need to take into account that how you say things matters – a lot. A criticism written nicely can empower a developer to become better in the future, but it can also crush someone’s dreams.

What I found that works best is to ask open-ended questions – it’s not aggressive and even encourages the developer to think critically. Will this take more time than just telling someone what the solution is? Yes, short-term. But long-term you’re helping them grow and they’re less likely to repeat their mistakes.

So, next time someone opens the file inside the for-loop and not before it, instead of plainly pointing that out, ask _“How would you reduce complexity here?“_. It will mean a lot.

## [](#add-a-flag-called-i-ran-this-code-locally)Add a flag called I ran this code locally

The thing that bugs me the most is finding an error in some small pull request because of which a functionality doesn’t work at all. That means that the developer didn’t even run the code – probably thinking it’s not necessary since the change is so small.

After that happened a couple of times, I added a flag called _I ran this code locally_ which solved the problem completely. I stopped reviewing code that wasn’t run locally and people didn’t lie about doing it. There were no hard feelings because we all actually knew that it should be done.

_Bonus:_ this is our template that every developer has to fill out when creating pull requests:

> ### [](#merge-request-description)Merge request description
> 
> *   What is new?
>     
>     *   Implemented...
> *   What has changed?
>     
>     *   Changed...
> 
> ### [](#checklist)Checklist
> 
> *   \[ \] I ran this code locally
> *   \[ \] I wrote the necessary tests
> *   \[ \] I covered my code with type-hints
> *   \[ \] I updated CHANGELOG
> 
> ### [](#trello-card)Trello card
> 
> [https://trello.com/c/](https://trello.com/c/)
> 
> ### [](#should-know-about)Should know about
> 
> *   Is there anything else that should be known?
> *   Any deployment notes?
> *   Any additional documentation?

### [](#in-other-news)In other news

I've been inspired by dev.to to write more, so I've started a [blog](https://devwayoflife.com/). If you're interested in this kind of content, feel free to check it out and subscribe
