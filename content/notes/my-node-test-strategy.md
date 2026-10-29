---
title: "My node test strategy"
date: '2016-01-02T11:55:23-03:00'
category: webclip
summary: 'The author outlines a Node testing workflow built around automation, tape and tap, proxyquire, sinon, JSCS, and Travis, with emphasis on easy setup, resettable tests, and coverage.'
tags: ["node-testing", "tape", "travis-ci", "code-coverage"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "My node test strategy"
    url: "https://remysharp.com/2015/12/14/my-node-test-strategy"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2016-01/remysharp-com--my-node-test-strategy.md"
    kind: repo
---

The post describes a Node test workflow that the author says has become increasingly systematic over the last few years. It centers on automation through CLI or CI, with Travis as the main service, and it keeps client-side testing outside the scope because that setup is still messy to him.

## Reading notes

- Tests should run automatically from a commit, repo push, or CLI, and failures must return a non-zero exit code so Travis can detect them.
- The author settles on tape for test code and increasingly uses tap to run tests, mainly for coverage support.
- He prefers assert.plan(n) for async tests and notes tape’s lack of beforeEach and afterEach, which can be patched.
- He pipes TAP output to tap-spec, though he reports that older tap-spec versions handle thrown exceptions correctly.
- proxyquire lets him intercept dependency loading, which he uses to control inquirer and other modules during tests.
- sinon is used to wrap functions and inspect calls, arguments, returns, and call counts.
- Before tests run, JSCS checks coding style with a project-specific .jscsrc configuration.
- His project layout puts fixtures under test/fixtures and names test files with .test.js, with .browser.js for browser-specific tests.
- His npm test command runs style checks and then executes test files through tape and tap-spec.
- To avoid shared state between test files, he sometimes runs each test file in a separate process, even though he calls the approach clunky and warns against using it unless necessary.
- For watch mode, he uses nodemon to rerun npm test on file changes.
- tap’s coverage integration provides Istanbul reports, and he also connects tap with Coveralls through Travis environment variables.
- He recommends using assert.equal instead of assert.ok when possible because failures are easier to debug.
- He also suggests making tests reusable when the problem allows it, using fixture-driven test suites.
- His closing point is that testing has to be easy, or it gets pushed aside and eventually lost.
