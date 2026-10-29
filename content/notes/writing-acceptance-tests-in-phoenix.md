---
title: "Writing Acceptance tests in Phoenix"
date: '2016-02-07T22:54:30-03:00'
category: webclip
summary: 'The post shows how to write acceptance tests in Phoenix with Hound, from setup and an IntegrationCase to form interactions, while noting the runtime cost of these tests.'
tags: ["phoenix", "acceptance-tests", "hound", "elixir"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Writing Acceptance tests in Phoenix"
    url: "http://blog.plataformatec.com.br/2016/01/writing-acceptance-tests-in-phoenix/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2016-02/blog-plataformatec-com-br--writing-acceptance-tests-in-phoenix.md"
    kind: repo
---

The post walks through adding Hound to a Phoenix app and using PhantomJS as a headless driver for acceptance tests. It also shows how to set up a shared IntegrationCase, start Hound during test runtime, and configure the test server so browser-driven tests can run.

## Reading notes

- Hound is presented as a tool for writing acceptance tests in the Elixir ecosystem.
- The example uses an expenses report listing page and interacts with report data and form elements.
- Hound supports chrome_driver, firefox, phantomjs, and selenium, and the author chooses phantomjs for headless execution.
- The setup adds Hound to mix.exs, starts it in the test helper, configures the driver in config.exs, and enables the server in config/test.exs.
- A shared IntegrationCase is created to include Hound.Helpers, Ecto helpers, router helpers, and hound_session.
- The test file defines helpers to check whether an expense appears in the list, collect table rows, and select a status value in a form.
- The tests navigate directly to the city expenses page in setup and reuse that city across the examples.
- One test filters expenses by supplier, fills the supplier field, submits the form, and checks that only the expected expense remains.
- Another test filters by status, first selecting cancelled and then paid, reloading the form between submissions because the element cache can become invalid.
- The post says acceptance tests are slower and the suite runtime tripled after adding two such tests.
- It recommends keeping acceptance tests as a small part of the test pyramid and preferring controller tests in most cases.
- PhantomJS is described as faster than the other options mentioned.
- The post notes that Hound does not start the browser automatically, so it must be started separately before running tests.
