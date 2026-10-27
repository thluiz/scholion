---
title: "Why You Should Use Continuous Integration and Continuous Deployment"
date: '2013-12-11T09:29:32-03:00'
category: webclip
summary: 'Explains how automated testing, continuous integration, and continuous deployment help teams catch breakages early, ship smaller changes, and keep staging and production in sync.'
tags: ["continuous-integration", "continuous-deployment", "automated-testing"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Why You Should Use Continuous Integration and Continuous Deployment | CSS-Tricks"
    url: "http://css-tricks.com/continuous-integration-continuous-deployment/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2013-12/css-tricks-com--why-use-continuous-integration-and-deployment.md"
    kind: repo
---

The article argues that a strong development workflow makes teams more productive and that Continuous Integration and Continuous Deployment are key practices for it. CI means testing each change automatically and as early as possible, while CD pushes passing changes to staging or production so a working version stays available.

## Reading notes

- Automation is presented as a core part of a good workflow, and testing is treated as one task that should be automated.
- Testing should begin from the user’s perspective, by checking the most important workflows first.
- Tools mentioned for UI and behavior testing include Selenium, PhantomJS, Jasmine, CasperJS, Cucumber, and Lettuce.
- Tests should run continuously for every change on an automated and separate system to avoid the “it works on my machine” problem.
- Running tests only at the end of a sprint can make it hard to find the commit that broke them.
- Continuous Integration is described as the first step in Continuous Deployment.
- Code can rot when it is not running somewhere, because dependencies, packages, APIs, and operating systems change.
- Continuous Deployment is described as pushing code that passes tests into staging or, ideally, production.
- Deployment pipelines define the steps from codebase to production and may include manual approval steps.
- Pipelines should be easy to follow and replicate so changes can be shipped regularly.
- The article recommends automated rollback, including database backups that are regularly restored and tested.
- A staging environment should receive the main branch whenever changes are made, and it can be used for automated tests.
- If a team uses the product in daily work, it should use staging instead of production.
- Automatically deploying to production is presented as a way to reduce fear of change and ship fixes quickly.
- The conclusion says automated testing and continuous deployment help teams deliver more stable software and deploy new versions several times a day.
