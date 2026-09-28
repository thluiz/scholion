---
title: "Why End-to-End (E2E) Testing is Often Good Enough"
date: '2022-06-10T19:08:20-03:00'
category: webclip
summary: 'The page argues that E2E tests verify system integrity by exercising real user scenarios in a production-like environment, even though they are costlier, flakier, and harder to maintain than smaller test layers.'
tags: ["end-to-end-testing", "testing-pyramid", "ci-pipelines"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Why End-to-End (E2E) Testing is Often Good Enough - Semaphore"
    url: "https://semaphoreci.com/blog/e2e-testing"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2022-06/semaphoreci-com--why-end-to-end-e2e-testing-is-often-good-enough.md"
    kind: repo
---

End-to-end testing is presented as a way to check the integrity of a whole system by running common user scenarios in an environment similar to production. The page says it can be more useful than UI testing for some apps because it focuses on how components work together and on whether the system delivers the expected output.

## Reading notes

- E2E tests sit near the top of the testing pyramid, below UI testing.
- They check whether all components produce the desired output when they interact.
- Testing components in isolation cannot guarantee that the full system meets requirements.
- E2E tests should run in an environment similar to production.
- Compared with UI tests, they target system integrity and do not go through the UI.
- UI tests can produce false alarms when UI issues appear even if the backend works.
- The E2E process includes planning, design, execution, and analysis.
- Planning focuses on business requirements and relevant scenarios such as login, signup, cart, checkout, and payment.
- Test design should cover all relevant conditions and support parallel execution.
- Execution usually happens in a shadow environment set up before CI and torn down after it finishes.
- Analysis includes finding why tests failed and sending reports to stakeholders.
- E2E tests can be flaky, environment-dependent, costly to simulate, and harder to maintain.
- Distributed architectures raise questions about which team owns the tests.
- Their main benefits are user experience, coverage of real-world cases, and reliability in production-like environments.
- Tools mentioned for API E2E testing are Postman, Assertible, and JMeter.
- Better CI integration comes from parallel execution and private CI machines.
