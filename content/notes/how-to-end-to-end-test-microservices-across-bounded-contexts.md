---
title: "How to end-to-end test microservices across bounded contexts?"
date: '2026-09-25T21:17:23+01:00'
category: webclip
summary: 'The article explains how E2E testing across bounded contexts should be split between microservice teams, QA, and full-stack teams, and compares hosted services with mocks for cross-team integration tests.'
tags: ["microservices", "end-to-end-testing", "bounded-contexts", "wiremock"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "How to end-to-end test microservices across bounded contexts?"
    url: "https://theburningmonk.com/2024/12/how-to-e2e-test-microservices-across-bounded-contexts/?ref=dailydev"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/theburningmonk-com--how-to-end-to-end-test-microservices-across-bounded-contexts.md"
    kind: repo
---

The article says that end-to-end testing across bounded contexts depends on how responsibilities are split in the organization. Microservice teams should own service-level tests and use tools like Pact to catch contract problems early, while QA or cross-functional teams can test full user journeys with Cypress or Selenium.

It also says full-stack teams can test their own parts of the journey, either by deploying related services into their environment or by using mocks such as WireMock Cloud. The preferred approach is mocks, because they let teams test independently, reflect agreed API changes quickly, and reduce coordination, though they require automation and well-documented APIs.

## Reading notes

- Microservice teams should test their own services and verify contracts with other services.
- Pact is presented as a way to catch integration problems between microservices.
- Service-level tests can cover edge cases, but they do not guarantee a complete user journey works.
- QA teams can own end-to-end user journeys across the frontend and backend.
- Cypress and Selenium are suggested for driving end-to-end tests from the frontend.
- Full-stack teams can own both frontend pages and microservices within a domain.
- In that setup, full-stack teams can test their part of the user journey autonomously.
- One option is to deploy related services into the team’s own environment, but that becomes cumbersome as the system grows.
- Another option is to run tests in dedicated integration environments, but that delays cross-bounded-context integration testing.
- The preferred option in the article is to use mocks so each team can exercise tests independently.
- WireMock Cloud is recommended for mocking third-party APIs and other teams’ services.
- The article gives a workflow of uploading an OpenAPI spec, configuring responses, pointing microservices to the mock API, and running tests with Cypress or Selenium.
- Mocks can be updated to reflect agreed changes before the other services reach production.
- This approach needs automation and rigorous API documentation, which the article connects with contract-first development.
- The conclusion is that overlapping tests are acceptable if they are less costly than missing important journey coverage.
