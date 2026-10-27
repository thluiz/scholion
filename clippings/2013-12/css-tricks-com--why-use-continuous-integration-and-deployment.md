---
url: "http://css-tricks.com/continuous-integration-continuous-deployment/"
captured_at: "2013-12-11T09:29:32-03:00"
title: "Why You Should Use Continuous Integration and Continuous Deployment | CSS-Tricks"
domain: "css-tricks-com"
---

# **W**hy You Should Use Continuous Integration and Continuous Deployment

Published
December 9, 2013
by Guest Author

*The following is a guest post by Florian Motlik**.** Florian is CTO of [Codeship](https://www.codeship.io) , a hosted Continuous Integration and Continuous Deployment platform**.** What the heck is that, you might ask? It's kind of a philosophy and toolset for working on websites**.** That is perhaps a bit too simplified, so I'll let Florian explain**.***

A great development workflow will make your good developers great, and your great developers exceptional**.** A bad workflow will take your best engineers productivity down to a junior level and make wish he worked elsewhere**.**

It is critically important for every team and especially the leaders of those teams to get their development workflow in order**.** Two best practices that have gained a lot of traction over the last few years are Continuous Integration and Continuous Deployment**.** Here's some quick definitions.

**Continuous Integration** is the practice of testing each change done to your codebase automatically and as early as possible**.**

**Continuous Deployment** follows the testing that happens during Continuous Integration and pushes changes to a staging or production system**.** This makes sure a version of your code is accessible at all times**.**

First, we will take a close look at Continuous Integration and show you how to get started with testing**.** Then we will move on to Continuous Deployment which is the next logical step**.**

With both in place, your development team will be orders of magnitude more efficient**.**

### Continuous Integration

Automation is a cornerstone of a great development workflow**.** Every task that can be done by a machine should be**.** Automation gives you the time to focus. Testing is one such task**.**

Through testing, you can be sure that the most important steps your customers will take through your system are working, regardless of the changes you make**.** This gives you the *confidence* to experiment, implement new features, and ship updates quickly**.**

#### Start testing at the top

Good testing begins with viewing the app from a user’s perspective**.** What are the typical workflows**?** What features and steps do users go through often?

Then start testing with those in mind**.** Use tools like [Selenium](http://www.seleniumhq.org/)  or [PhantomJS](http://phantomjs.org/)  to make sure those important workflows work**.**

A great way to determine the most critical workflows is by getting everyone in your team to write down a list of them and then combine those lists**.** You can [read an in-depth guide](http://blog.codeship.io/2013/03/15/testing-top-to-bottom.html)  to this technique in one of our blog posts**.**

Here is a list of tools that you can use to start testing UI:

- [Jasmine](http://pivotal.github.io/jasmine/)  (JavaScript)
- [Selenium](http://www.seleniumhq.org/)  (Frontend Testing)
- [CasperJS](http://casperjs.org/)  (Frontend Testing)
- [Cucumber](http://cukes.info/)  or [Lettuce](https://github.com/gabrielfalcao/lettuce)  (Behaviour Driven Testing for Ruby and Python)

From this strong base of tests that make sure the workflows are working, you can go deeper and start unit testing different parts of your site**.** But beware: Your customers want your UI to work, so make sure it does with every change**!**

With all those tools in hand, the single most important step you can take for testing is getting started**.** It pays off immediately, and not just from a tech perspective**.** You can read about the [business advantages of Continuous Integration](http://blog.codeship.io/2013/04/11/a-business-case-for-continuous-integration.html)  in this blog post by Joe Green**.**

#### Run your tests continuously

Humans make mistakes**.** Sometimes people consider a change so small it can’t possibly break the app, so they don’t run tests**.** Then your product goes down and nobody knows why.  
Automated tests can only show their true power when you run them continuously and for *every* change**.** They have to be run on an automated and separate system to prevent the *‘It works on my machine’* syndrome**.** Only if the Continuous Integration infrastructure tells you the tests pass, the tests pass**.**

The advantage of running all tests immediately for every change is that you know right away if something broke**.** Consider working on a 2 week sprint**.** On day two of the sprint, one of your developers changes something that breaks a test**.** If you don’t continually run all of your tests, there is a chance nobody detects the problem**.** People keep working, and at the end of the sprint, you run the whole test suite again**.** The test fails**.** It now has been 2 weeks since the breaking change was committed**.** Finding the change that broke the tests is incredibly hard, as there now have been a lot of commits since then**.**

Lots of teams are on way longer cycles than 2 weeks**.** This is incredibly wasteful and can be easily prevented by running all your tests every time one of your developers pushes code to the repository**.** **Any failures can be fixed right away.**

Continuous Integration is the first, but very important step in Continuous Deployment**.**

If you'd like to learn more about it, Martin Fowler has released a great and very in-depth article about Continuous Integration [on his blog](http://martinfowler.com/articles/continuousIntegration.html)

### Continuous Deployment

Code rots if it doesn’t run somewhere**.** External dependencies are updated, server packages installed, API’s change or operating systems replaced**.** Often we do not have the ability to control every part of our infrastructure**.** We rely on other products and companies to maintain parts of our stack**.** All of these changes can break your app without you realizing it**.**

This is why Continuous Deployment is incredibly important**.** Whenever the main development branch in your repository passes all the tests, you should push your code at least into a staging environment or in the best case into production**.** Your development or QA team can then review the latest version of your application and give feedback**.** Furthermore you can run tests against that staging system to make sure it works in a production-like environment**.**

This helps you find problems early and fix them while it is still cheap**.** An important concept to understand when starting with Continuous Deployment are deployment pipelines**.**

#### Deployment Pipelines

A deployment pipeline defines all steps necessary to go from your codebase to the production website**.** Automating these steps is crucial to have fast deployments**.** But often, deployment pipelines also include manual steps, like a product manager signing off on a new release**.**

Deployment pipelines have to be easy to follow and replicate**.** This allows you to push new changes regularly. Especially when you need to ship a fix, predefined steps can save you from bringing more harm to your site**.**

Once you set up a Deployment Pipeline and automate the steps, you are in a position to ship small changes quickly, get feedback from your customers, and iterate on your product**.** This is a major competitive advantage to other companies who need a long time to react to customer feedback**.** Intercom did a [great blog post about this.](http://insideintercom.io/shipping-is-your-companys-heartbeat/)

It’s amazing how much lower the cost of bringing a new software product to market has gotten in last couple of years**.** It has never been easier or cheaper to build great software**.** This levels the playing field between you and your competition**.** You need to ship new features faster than your competition while delivering better and stable long term quality**.** Continuous Deployment is one of the techniques that will help you to get there**.**

#### How can I get started?

After interviews with dozens of companies and the feedback from thousands of developers using our product we’ve identified several steps you can take to get started with Continuous Deployment**.**

##### Test test test, but be smart about it

Testing is the first step that needs to be taken**.** You need to get to a point where you can change almost any part of your system and be sure you didn’t break any other feature because your tests will catch those errors**.** Once you are at this point, it liberates you from having to think about impacts this change might have**.** You can now experiment with your product and iterate to build exactly what your customers want and pay for**.**

Tests are not there to make your developers happy**.** They are there to build a stable and high quality product for your users**.** They are a tool to keep your users happy and introduce changes without destroying their experience**.** Building a product without properly and automatically testing (as your users would use it) means working with the hands tied behind your back**.** You might get new features out there, but you will never be as fast and good as you could be**.**

Testing is the basis on which Continuous Deployment is built**.** [Tests make software](http://blog.codeship.io/2013/04/16/tests-make-software.html)  as Clemens, one of our developers, explained in his blog post**.**

##### Example

[This script](https://gist.github.com/flomotlik/5113098#file-translatetest-coffee) tests Google Translate to make sure it translates **"good morning"** from German to English:

```
#Run with casperjs test translate.coffee
 
casper.start 'http://translate.google.com/', ->
  @.sendKeys('#source', 'Guten Tag');
  @.then ->
    @.click '#gt-submit'
  @.waitForText('Good day')
  @.then ->
    @.test.assertSelectorHasText '#result_box', 'Good day'
  @.then ->
    @.capture 'output.png'
 
casper.run ->
  @.test.done(1)
```

[CasperJS](http://casperjs.org/)  helps you to start testing your application quickly, and it will scale up to test more complex scenarios as you need**.**

##### Automate Deployment

Every step in your deployment should be automated**.** Once set up, you should never have to think about which steps need to be taken**.** Every choice and every manual task leads to possible mistakes, so you simply do it less often**.** By automating every part of your deployment you can push new features, but more importantly, push fixes very quickly**.** Continuous Deployment works because of automation, so don’t skip this step**.**

##### Automate Rollback

When pushing quickly you also want to be able to go back to an earlier state easily**.** Otherwise you won’t feel safe enough to do as regularly as you should be**.**

Automated Rollback includes your codebase as well as your database**.** Make sure you regularly backup your database and use those backups to recreate your system on test machines**.** If you don’t regularly restore your backups you can’t be sure they will work when you desperately need them**.**

##### Deploy to Staging

Create a staging environment and push your master branch or main line of development into that Staging application any time changes are made**.** This Staging application is your first line of defense and helps to review all changes before going into production**.** You can even run automated tests against Staging to make sure it works as expected**.**

##### Use your staging environment

If you use your product in your daily work, use your Staging and not your Production server**.** As you push changes continuously to Staging, you will see first hand when something is broken as it immediately impacts your team**.** "Eating your own dog food" makes all of your developers aware when the quality drops**.**

##### Automatically deploy to Production

As a final step, continuously deploy to your Production environment**.** This will truly change the way your organization works**.** There will be no more fear in changing your site. This means you can iterate quickly on new features, but if you ship a bug, you can quickly ship a fix as well**.** You are not tied to arbitrary cycles that slow down your team**.**

### Conclusions

Moving to Continuous Deployment will change your development dramatically**.** It will make you more productive and lead to a more stable and better product**.** There are steps like automated testing that you need to get started with first**.** Automated testing is not a tool to build better software, but a process to build a better product for your users**.** Once set up, you can then reap the benefits of deploying new versions several times a day**.**

Please let us know if any questions come up or if there is anything else we can help with either here in the comments or send us a tweet to [@codeship](https://www.twitter.com/codeship) **.** We’ve also recently released a free eBook that walks you through our development workflows and dives deeper into Continuous Deployment**.** [You can grab the book here.](http://ebooks.codeship.io/efficiency-in-development-workflows-by-codeship)

Ship long and prosper!

### More Information
