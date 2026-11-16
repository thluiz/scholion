---
url: "https://web.archive.org/web/20200615010700id_/https://dev.to/nas5w/failing-faster-and-iterating-with-modern-software-development-practices-2ae7"
captured_at: "2026-11-16T07:50:44+00:00"
title: "Failing Faster and Iterating with Modern Software Development Practices"
domain: "web-archive-org"
---

![Cover image for Failing Faster and Iterating with Modern Software Development Practices](https://res.cloudinary.com/practicaldev/image/fetch/s--wFCsOo4x--/c_imagga_scale,f_auto,fl_progressive,h_420,q_auto,w_1000/https://dev-to-uploads.s3.amazonaws.com/i/1r6547nolj42fas22x2k.jpg)

###  [![nas5w profile image](https://res.cloudinary.com/practicaldev/image/fetch/s--DPoT-fOU--/c_fill,f_auto,fl_progressive,h_50,q_auto,w_50/https://dev-to-uploads.s3.amazonaws.com/uploads/user/profile_image/135219/f7e49646-7ace-4fc2-810e-29e2087e56a0.jpeg) Nick Scialli (he/him)](https://web.archive.org/nas5w) [twitter logo](http://twitter.com/nas5w) [github logo](http://github.com/nas5w) May 26 _Updated on May 27, 2020_ ・5 min read

Using modern software development practices enable us to find and fix bugs faster and iterate. This post offers a primer into some of these modern practices.

——-  
If you enjoy this post, consider signing up for my [free weekly software development mailing list](https://buttondown.email/devtuts)!  
——-

## [](#1-version-control)1\. Version Control

[![branching example](https://res.cloudinary.com/practicaldev/image/fetch/s--ccbQBlEq--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://dev-to-uploads.s3.amazonaws.com/i/1r6547nolj42fas22x2k.jpg)](https://res.cloudinary.com/practicaldev/image/fetch/s--ccbQBlEq--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://dev-to-uploads.s3.amazonaws.com/i/1r6547nolj42fas22x2k.jpg)

Use version control on your code (e.g., git). This allows for mobility, collaboration, backup, and enables all sorts of other modern web development practices.

## [](#how-version-control-helps-you-fail-faster-and-iterate)How version control helps you fail faster and iterate

Version control enables pretty much all other quality control measures. It allows you to implement hooks to force things like code testing and linting when you push your code remote repositories. You can hook your code repository up to Continuous Integration servers. The bottom line: modern software development starts at version control!

## [](#2-automated-testing)2\. Automated Testing

[![automated test results](https://res.cloudinary.com/practicaldev/image/fetch/s--596oLis_--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://dev-to-uploads.s3.amazonaws.com/i/qmuukatxze58a3ctc121.jpg)](https://res.cloudinary.com/practicaldev/image/fetch/s--596oLis_--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://dev-to-uploads.s3.amazonaws.com/i/qmuukatxze58a3ctc121.jpg)

Automated testing allows you to develop with confidence. They serve as a form of documentation as they assert what your app should do. Automated testing also helps you refactor without fear since you are relatively confident in your new code if tests pass.

## [](#how-automated-testing-helps-you-fail-faster-and-iterate)How automated testing helps you fail faster and iterate

You can write your code and "smoke test" it, meaning you try playing with your app a bit to make sure it works right. But how do you know your users won't hit a weird edge case that blows up the app? You don't, but you can help mitigate this concern by writing automated tests. Once written, these tests live forever, meaning less concern about software regression since your exists tests will (hopefully) fail if your code regresses.

As a bonus, you can use version control hooks and/or Continuous Integration to require your tests to pass before you can move forward in deploying your code.

## [](#3-continuous-integration)3\. Continuous Integration

[![jenkins logo](https://res.cloudinary.com/practicaldev/image/fetch/s--yrcJxfkn--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://dev-to-uploads.s3.amazonaws.com/i/i63h43crmbvlkxz8o9i9.png)](https://res.cloudinary.com/practicaldev/image/fetch/s--yrcJxfkn--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://dev-to-uploads.s3.amazonaws.com/i/i63h43crmbvlkxz8o9i9.png)

CI allows you to merge your code into a single repository frequently. A CI server can run automated tests and other checks to make sure your code is ready to be merged and, in conjunction with your version control service, can be a quality gate.

## [](#how-ci-helps-you-fail-faster-and-iterate)How CI helps you fail faster and iterate

When you push your code to a remote repository, you can know _immediately_ if your quality measures (e.g., tests, linting) have failed. This is a whole lot better than finding out because a user has emailed you that something is broken!

## [](#4-continuous-deliverydeployment)4\. Continuous Delivery/Deployment

[![arrow pointing right](https://res.cloudinary.com/practicaldev/image/fetch/s--0QnMa4Zk--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://dev-to-uploads.s3.amazonaws.com/i/r31ref4rrl2buydx3bsr.jpg)](https://res.cloudinary.com/practicaldev/image/fetch/s--0QnMa4Zk--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://dev-to-uploads.s3.amazonaws.com/i/r31ref4rrl2buydx3bsr.jpg)

Continuous delivery means you continuously deliver new code into a releasable state, ready to be sent to production at the click of a button. Continuous deployment goes one step further and deploys code, usually as soon as it's merged into a branch.

## [](#how-cd-helps-you-fail-faster-and-iterate)How CD helps you fail faster and iterate

Making it easy to integrate really small changes into your production environent is critical for iterating. The truth is that you _will_ merge some breaking changes into production. Software development is error prone and we all ship bugs. However, if we ship _really_ small chunks of code to production, our lives become much easier when we eventually do ship a bug. First, if you need to revert your production code, it's much easier to do so with a very small change set. Second, when you need to figure out what went wrong, you have a pretty small amount of code to investigate. It's much easier to find a bug in a couple days worth of code than a couple months worth of code!

## [](#5-intellisense-and-linting)5\. Intellisense and Linting

[![code highlighting](https://res.cloudinary.com/practicaldev/image/fetch/s--ae3QjlzV--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://dev-to-uploads.s3.amazonaws.com/i/z9ildaeacvmpdc63wh92.png)](https://res.cloudinary.com/practicaldev/image/fetch/s--ae3QjlzV--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://dev-to-uploads.s3.amazonaws.com/i/z9ildaeacvmpdc63wh92.png)

Use a code editor that has language services for your language. Ideally it provides autocomplete and lints your code. It highlights any compilation, syntax, and lint rule issues real-time as you're writing code.

## [](#how-intellisense-and-linting-helps-you-fail-faster-and-iterate)How intellisense and linting helps you fail faster and iterate

Features like autocomplete and code highlighting eliminates a lot of bugs _as you write them_. This may be the fastest way to fail and therefore it might be the most important item on the list! Linting keeps your code consistently-formatted, which makes it a lot easier to read for things like code review and facilitates identifying bugs.

## [](#6-feature-flagging)6\. Feature Flagging

[![flag](https://res.cloudinary.com/practicaldev/image/fetch/s--5lC28NJ6--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://dev-to-uploads.s3.amazonaws.com/i/qkrw276tp9h37bu352fa.jpg)](https://res.cloudinary.com/practicaldev/image/fetch/s--5lC28NJ6--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://dev-to-uploads.s3.amazonaws.com/i/qkrw276tp9h37bu352fa.jpg)

Feature flags are variables in your code that hide functionality that's in development from your users. It allows you to keep releasing code as new features are mid-development, meaning those features don't block continuous delivery.

## [](#how-feature-flagging-helps-you-fail-faster-and-iterate)How feature flagging helps you fail faster and iterate

Releasing constantly is a cornerstone of failing faster. Without feature flags, we might hold off on shipping code for a while because we don't want to ship a half-baked feature. Feature flags let us ship constantly without worrying about these not-quite-done features!

## [](#7-instrumentation-and-monitoring)7\. Instrumentation and Monitoring

[![graphs and charts](https://res.cloudinary.com/practicaldev/image/fetch/s--uNLZhuKJ--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://dev-to-uploads.s3.amazonaws.com/i/d8fkq68d9ftjfqxbyi97.jpg)](https://res.cloudinary.com/practicaldev/image/fetch/s--uNLZhuKJ--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://dev-to-uploads.s3.amazonaws.com/i/d8fkq68d9ftjfqxbyi97.jpg)

Use a service like New Relic or Datadog that monitors your app for errors. Set up notification thresholds that notify you or your team when a particularly high number of errors are encountered.

## [](#how-instrumentation-and-monitoring-helps-you-fail-faster-and-iterate)How instrumentation and monitoring helps you fail faster and iterate

Let's say we ship a change that causes our web server to start spewing 500-level errors. We don't necessarily want to wait until a bunch of users complain—monitoring tools let us know immediately when we're getting a high level of abnormal responses. We can then investigate and mitigate the situation before too many users are affected.

## [](#8-containerization)8\. Containerization

[![docker logo](https://res.cloudinary.com/practicaldev/image/fetch/s--yMav_4ZB--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://dev-to-uploads.s3.amazonaws.com/i/qp4i8wf23rr3zfii8mc1.jpg)](https://res.cloudinary.com/practicaldev/image/fetch/s--yMav_4ZB--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://dev-to-uploads.s3.amazonaws.com/i/qp4i8wf23rr3zfii8mc1.jpg)

Reduce concerns about different environments and simplify deployments by using a containerization service (e.g., Docker). If an app can run locally in a Docker container, it can run deployed on a server as a Docker container.

## [](#how-containerization-helps-you-fail-faster-and-iterate)How containerization helps you fail faster and iterate

Containerization allows us to be working locally in an environment (pretty much) identical to our deployment. This increases the chances that we detect any environment-related issues locally rather than in our production environment. We like figuring out issues locally rather than in production.

## [](#conclusion)Conclusion

Failing faster enables us to find and fix bugs faster and ship higher quality code. We should all aspire to ship better higher quality code and ensure a better experience for our users!

 [![twitter logo](https://practicaldev-herokuapp-com.freetls.fastly.net/assets/twitter-f95605061196010f91e64806688390eb1a4dbc9e913682e043eb8b1e06ca484f.svg)](https://twitter.com/intent/tweet?text=%22Failing%20Faster%20and%20Iterating%20with%20Modern%20Software%20Development%20Practices%22%20by%20@nas5w%20%23DEVCommunity%20https://dev.to/nas5w/failing-faster-and-iterating-with-modern-software-development-practices-2ae7)[DISCUSS (3)](#comments)

![Copy to Clipboard](https://practicaldev-herokuapp-com.freetls.fastly.net/assets/content-copy-8cf07612d6f4decff7188a5910c4fcd8caf1e7bb73f5a88eb7753a20c728d00e.svg)

Classic DEV Post from Aug 16 '19

[![Kayla Sween profile image](https://res.cloudinary.com/practicaldev/image/fetch/s--7yLPTAs5--/c_fill,f_auto,fl_progressive,h_200,q_auto,w_200/https://dev-to-uploads.s3.amazonaws.com/uploads/user/profile_image/187691/a39de9e8-186c-485a-b4b6-a4ef158c0476.jpeg)](https://web.archive.org/kaylasween?utm_source=additional_box&utm_medium=internal&utm_campaign=regular&booster_org=)
