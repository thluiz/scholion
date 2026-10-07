---
url: "http://techcrunch.com/2015/01/31/three-reasons-why-your-software-is-so-far-behind-schedule/"
captured_at: "2015-02-02T21:17:58-03:00"
title: "Three Reasons Why Your Software Is So Far Behind Schedule | TechCrunch"
domain: "techcrunch-com"
---

# Three Reasons Why Your Software Is So Far Behind Schedule

[Next Story](http://techcrunch.com/2015/01/30/crunchweek-apples-huge-quarter-snapchat-discover-and-newsweeks-cover-fail/)

![john-cleese.jpg](techcrunch-com--three-reasons-why-your-software-is-so-far-behind-schedule/34bcf04ad0348827f3e50a364c314ec0.jpg)

When not opining here on TechCrunch I’m a software engineer for the fine folks at [HappyFunCorp](http://www.happyfuncorp.com/) (1) and I’m occasionally called on to diagnose and fix projects that have gone horribly wrong (2). The more I do this, the more I notice commonalities among problem projects–“[antipatterns](http://en.wikipedia.org/wiki/Anti-pattern),” if you will. Here I give you three more of my [ongoing list](http://techcrunch.com/2014/06/07/dear-clients-please-stop-ten-ways-founders-sabotage-themselves/) of such. Names have been changed to protect the guilty.

**1. Onboarding Time == Technical Debt**

[Technical debt](http://en.wikipedia.org/wiki/Technical_debt) is not always [a bad thing](https://sendgrid.com/blog/technical-debt-bad-thing/), but if you accrue too much of it, [it will kill you](http://techcrunch.com/2013/02/09/technical-debt-will-kill-you/). When under schedule pressure, or when new devs keep coming onto and going off a project, people tend to build new software subsystems and connect them to the old ones Rube-Goldberg style, instead of doing it right. It’s like turning a family home into a cantilevered skyscraper one room at a time, and waiting with dread for an earthquake to hit, instead of razing it and pouring a new foundation as you should have.

But sometimes taking on short-term technical debt is the right thing to do. The real problem with technical debt is that it often lurks off the metaphorical balance sheet: it’s hard to measure, especially if you’re non-technical. What I’ve noticed of late is that there exists an excellent proxy measure for a project’s technical debt: the onboarding time for a new developer.

So ask yourself: how long does it take a new dev to get set up and start pushing good new code to the repo? In many cases the answer should be an hour or less. No, really. “git pull”, “bundle install”, “rails s” and away you go. Or “git pull”, “pod update”, open the workspace in XCode, hit Command-R, and boom. It’s been some months since I did any Android work, but Android Studio ought to be comparably easy.

But, I hear you sputtering, my environment is very complicated! We have virtual machines and multiple databases and virtual private networks! Systems talking to systems talking to systems! No *way* we can get a new dev set up in an hour! Uh-huh. Facebook’s pretty large and complicated too, you know … and Facebook engineers famously write real code on [their first day](http://info.profilesinternational.com/profiles-employee-assessment-blog/bid/205963/Facebook-s-Onboarding-Bootcamp-Pushing-Codes-Instead-of-Ups) and push it to the live site their first week. If your new developers are spending hours wrestling with configuration and environments, you have probably run up more technical debt than you care to think about.

**2. The Test Suite Sweet Spot**

Obviously you need to write, and run, tests for your code. And in an ideal world, you would have up-to-date tests for all of your code, which run automatically whenever you commit a change to the repo. Unfortunately, in testing as in life, the perfect is often the enemy of the good. It’s amazing how often I’ve encountered projects with elaborate test suites that have been hopelessly broken for months and/or take forever to run.

Developers write tests but don’t run them regularly, so they begin to fall out-of-date, and schedule pressure means that fixing the tests is non-critical whereas getting the new release out is critical, so the vicious circle compounds and the test suite decays into uselessness. Or–more rarely–test-*driven* development becomes test-*centered* development, and actually Getting Stuff Done takes a back seat to writing ever more and more elaborate test code, the refactoring of which takes so much time that development progress gets slower and slower.

There are costs to maintaining a huge and complex test suite; after you refactor code, you may have to either refactor your tests, which takes time, or let them break, which (ultimately) takes even more time. If your organization / management / development pressures are such that keeping all your tests up to date isn’t a valid option, and you can’t alleviate those pressures, then it’s actually better to shrink your test suite. I know that doesn’t sound appealing. I don’t like it either. But a smaller test suite you actually run and maintain is much better than a larger one you ignore.

**3. Please Just Stop Running Your Own Servers Already**

Big Company problem projects tend to have something else in common: they’re still running their own servers. No AWS or Google Compute Engine for them, much less Heroku or Elastic Beanstalk or App Engine. They have their own machines. And their own sysadmins. And their own homegrown processes for patching and updating and deploying code. And their own incredibly paranoid security, which often means “no developer may lay hands on the production machines,” which often makes it pretty hard to get anything done.

Big companies need to ask themselves: *are our sysadmins better than Google’s or Amazon’s*? And since the answer is probably no, the conclusion is: *why don’t we let the experts handle it?* (To be fair, they often are better than those of some cloud hosts — eg I’ve never had a good experience with Rackspace.) Yes, there are downsides. Yes, it means a loss of control. It’s not a panacea.

But unless your circumstances are truly exceptional, a full cost/benefit analysis usually points very firmly towards moving your servers to The Cloud. Back in the early days of electricity, every factory had its own generator, and many protested loudly at the loss of control inherent in this whole newfangled “power grid” notion. But there’s a reason the grid succeeded, and it’s the same reason the cloud is succeeding today. Don’t get stuck in the twentieth century. Stop making the old mistakes. After all, there are so many bold new mistakes to make.

---

(1) Recently [profiled on video](http://techcrunch.com/2015/01/12/built-in-brooklyn-happyfuncorp/) here, to my great surprise. (Nobody will believe this, but despite my TC-columnist gig, I had no idea this was happening until the week it happened.)

(2) Usually either internal projects at large clients, or startup apps built by a cheap third-party dev shop. There is some truth to the notion that you get what you pay for.
