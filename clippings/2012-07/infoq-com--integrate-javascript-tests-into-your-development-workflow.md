---
url: "http://www.infoq.com/news/2012/07/javascript-test-vs"
captured_at: "2012-07-13T17:01:53-03:00"
title: "Integrate JavaScript Tests Into Your Development Workflow"
domain: "infoq-com"
---

[Chutzpah](http://chutzpah.codeplex.com/) can run JavaScript tests from inside Visual Studio 2012. And TFS extends this by allowing you to run JavaScript Unit tests into your builds.

Visual Studio 2012 comes with much better unit testing support and [supports several open source frameworks](http://blogs.msdn.com/b/visualstudioalm/archive/2012/03/02/visual-studio-11-beta-unit-testing-plugins-list.aspx) through a plugin architecture for test runners. Chutzpah leverages this to bring JavaScript Unit testing within Visual Studio. One interesting thing is that you can mix your C# and .js tests in a single run, instead of having to run them separately. You can read [Anatomy of the Chutzpah test Adapter…](http://matthewmanela.com/blog/anatomy-of-the-chutzpah-test-adapter-for-vs-2012-rc/) by Matthew to learn more about how this Test Adapter works or even how to write your own adapter.

Chutzpah supports both [QUnit](http://docs.jquery.com/QUnit) and [Jasmine](http://pivotal.github.com/jasmine/) testing frameworks. [This article](http://blogs.msdn.com/b/visualstudioalm/archive/2012/07/09/javascript-unit-tests-on-team-foundation-service-with-chutzpah.aspx) from the Visual Studio ALM team gives more details about how to setup TFS build runners to run these tests.

Note that Chutzpah also supports [TeamCity](http://www.jetbrains.com/teamcity/). And if you don’t use TFS or TeamCity for running your builds? You could use the Chutzpah command line api to integrate it into your build server. You can even use other tools such as [js-test-driver](http://www.slideshare.net/emwendelin/javascript-ci) or [PhantomJS](http://www.readmore.ch/post/18940470535). 

Visual Studio 2012 RC brings several other [unit testing improvements](http://blogs.msdn.com/b/visualstudioalm/archive/2012/06/18/visual-studio-2012-rc-what-s-new-in-unit-testing.aspx) as well, such as a continuous test runner, Smart test discovery and several enhancements for Metro Unit Testing.
