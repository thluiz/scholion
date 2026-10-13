---
title: "Integrate JavaScript Tests Into Your Development Workflow"
date: '2012-07-13T17:01:53-03:00'
category: webclip
summary: 'The page explains how Chutzpah brings JavaScript unit tests into Visual Studio 2012, lets C# and .js tests run together, and can be used with TFS, TeamCity, or the command line.'
tags: ["javascript-tests", "visual-studio-2012", "chutzpah", "continuous-integration"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Integrate JavaScript Tests Into Your Development Workflow"
    url: "http://www.infoq.com/news/2012/07/javascript-test-vs"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2012-07/infoq-com--integrate-javascript-tests-into-your-development-workflow.md"
    kind: repo
---

Chutzpah runs JavaScript tests inside Visual Studio 2012 and can be extended into build workflows through TFS. Visual Studio 2012’s test runner plugin architecture lets it support several open source frameworks, and Chutzpah uses that support to bring JavaScript unit testing into the IDE.

It also lets C# and .js tests run in a single pass. The text says Chutzpah supports QUnit and Jasmine, works with TeamCity, and can be integrated through its command-line API when TFS or TeamCity are not used. Visual Studio 2012 RC also adds a continuous test runner, Smart test discovery, and Metro unit testing improvements.

## Reading notes

- Chutzpah runs JavaScript tests from inside Visual Studio 2012.
- TFS can run JavaScript unit tests in builds.
- Visual Studio 2012 supports several open source frameworks through a plugin architecture for test runners.
- Chutzpah uses that architecture to bring JavaScript unit testing into Visual Studio.
- C# and .js tests can run together in one run.
- Chutzpah supports QUnit and Jasmine.
- The Visual Studio ALM team article has more details about setting up TFS build runners for these tests.
- Chutzpah also supports TeamCity.
- If TFS or TeamCity are not used, the Chutzpah command-line API can integrate it into a build server.
- Other tools mentioned for integration are js-test-driver and PhantomJS.
- Visual Studio 2012 RC also adds a continuous test runner, Smart test discovery, and Metro unit testing enhancements.
