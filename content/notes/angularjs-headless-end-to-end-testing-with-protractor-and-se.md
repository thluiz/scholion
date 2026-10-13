---
title: "AngularJS Headless End to End Testing With Protractor and Selenium"
date: '2014-02-24T22:57:21-03:00'
category: webclip
summary: 'The page explains end to end testing for AngularJS, compares it with unit testing, and outlines a Selenium-based headless setup on Ubuntu using Protractor, Xvfb, Chrome, Firefox, and PhantomJS.'
tags: ["angularjs", "protractor", "selenium", "headless-testing"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "AngularJS Headless End to End Testing With Protractor and Selenium"
    url: "https://www.exratione.com/2013/12/angularjs-headless-end-to-end-testing-with-protractor-and-selenium/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2014-02/exratione-com--angularjs-headless-end-to-end-testing-with-protractor-and-se.md"
    kind: repo
---

The page argues for a testing split where service logic gets unit tests and the rest of the AngularJS app is covered by end to end tests against a known backend. It treats Protractor as the practical layer on top of Selenium and WebDriver, and it walks through a headless Ubuntu setup for running browser tests on a server.

## Reading notes

- End to end tests run against the front-end of a fully functional application, driving a browser through pages, JavaScript, the DOM, and form submission.
- Unit tests cover small pieces of functionality in isolation, with application data mocked as needed.
- A REST-like backend and business logic pushed into services make AngularJS code easier to unit test.
- Controllers are presented as glue between routes, directives, and services.
- End to end tests cover directives, glue controllers, and application behavior against a known backend.
- Mock server responses are described as costly to create and maintain.
- Karma and ngScenario are described as obsolete for AngularJS end to end testing.
- Selenium and WebDriver provide APIs for driving browsers and inspecting loaded pages.
- Protractor sits on top of Selenium and WebDriver to make AngularJS end to end tests easier to write.
- With an existing Selenium setup, Protractor is installed, configured, and run with test specs.
- The example Protractor config uses Jasmine, a Selenium standalone server, and an AngularJS app at a base URL.
- Protractor tests are described as promise-based and asynchronous, with expect() handling promise resolution for assertions.
- If there is no existing Selenium infrastructure, the page outlines a headless Ubuntu server setup.
- The setup includes installing Node.js from source, Xvfb, browser dependencies, Chromium, Firefox, PhantomJS, ChromeDriver, and Java.
- A Selenium standalone server is installed as a service under a selenium user with a home directory.
- The Selenium service uses the same DISPLAY value as Xvfb and adds ChromeDriver to PATH.
- A PhantomJS driver log file must be created and made writable for the selenium user.
- The page notes a known issue between Protractor and PhantomJS.
- Imagemagick is needed if snapshots are required.
- A Vagrant and Chef configuration is offered as an easier way to provision the full environment.
