---
url: "https://theburningmonk.com/2024/12/how-to-e2e-test-microservices-across-bounded-contexts/?ref=dailydev"
captured_at: "2026-09-25T21:17:23+01:00"
title: "How to end-to-end test microservices across bounded contexts?"
domain: "theburningmonk-com"
---

![](https://res.cloudinary.com/theburningmonk/image/upload/f_auto,c_scale,w_90/theburningmonk.com/mugshot.png)

[

Yan Cui

](https://theburningmonk.com/about)

I help clients go faster for less using serverless technologies.

[![](https://theburningmonk.com/wp-content/uploads/2024/03/connect-the-dots-variant-3-1.png)](https://productionreadyserverless.com/?utm_campaign=connect-the-dots&utm_source=blog&utm_medium=image-banner&utm_content=variant3)

One of my favourite questions from the November cohort of [Production-Ready Serverless](https://productionreadyserverless.com/?utm_campaign=e2e-test-across-bounded-contexts&utm_source=newsletter&utm_content=text-link) \[1\] is, “_How do you handle end-to-end tests involving multiple microservices across bounded contexts?_“

In a microservices environment, testing user journeys that span across multiple bounded contexts requires collaboration and a clear delineation of responsibilities.

![](https://theburningmonk.com/wp-content/uploads/2024/12/img_67636686e3c7d.png)

Depending on how your organisation is structured, different teams are responsible for testing parts or the entirety of the user journey.

For example…

### The microservice teams

Individual microservice teams are typically aligned with bounded contexts. They may own one or more microservices within their designated bounded context and should be responsible for testing them. Their job is to ensure that their microservices function correctly and adhere to the defined contracts with other microservices.

Tools like [Pact](https://pact.io/) \[2\] are great for verifying that a microservice meets consumers’ expectations (i.e. downstream services). This is a great way to catch integration problems between different microservices.

But these tests alone does not guarantee the user journey is going to work.

These service-centric tests can be very detailed and comprehensive. They are great at catching edge cases that might be missed from testing user journeys. However, they are often not broad enough to cover entire user journeys.

### The QA teams

In some organizations, a cross-functional team, which may include QA engineers, developers, and product owners, will own the user journeys. This team is responsible for end-to-end testing across bounded contexts.

They test the user journey as a whole to ensure that all system components (the frontend and the microservices) integrate seamlessly and meet business requirements.

Tools like [Cypress](https://www.cypress.io/) \[3\] or [Selenium](https://www.selenium.dev/) \[4\] can drive these end-to-end tests from the frontend. These tests cover entire user journeys and will test both the frontend and backend.

However, they do not replace the service-centric tests the microservices teams would run and own.

### Full-stack teams

In many organizations, full-stack teams own both the frontend pages and microservices within a domain.

In some cases, they would use microfrontends to allow more team autonomy. This is so that teams can more easily make changes on their pages without impacting others. If you want to learn more about microfrontends, check out [my conversation](https://realworldserverless.com/episode/77) \[5\] with mr. Microfrontend himself, Luca Mezzalira.

![](https://theburningmonk.com/wp-content/uploads/2024/12/img_6763672c4d696.png)

In situations like this, the full-stack teams can use end-to-end tests to test their parts of the user journey. Again, tools like Cypress and Selenium are a good choice here.

But here, we reach the heart of the question, “_How do you handle e2e tests involving multiple services across bounded contexts?_” (for example, for step 2. above)

**Do you deploy related services in your own environment?**

For example, if each team has its own AWS account, it can deploy other teams’ microservices into its accounts and test them together.

However, this becomes cumbersome as the system grows. To make it work, you need more and more automation.

Also, what version of the other teams’ code do you deploy?

If you deploy the latest code in development, then you risk instability.

If you deploy what’s in production, then you miss out on agreed-upon changes that have not yet made it into production.

**Do you run these tests in dedicated integration environments?**

For example, a QA/test environment designed for QA teams to run user journey tests. And where necessary, for them to run manual tests.

However, this delays the testing of integration across bounded contexts.

The full-stack teams want to test their part of the user journey and identify integration problems early. The answer shouldn’t be “let the QA team worry about it”!

From the full-stack team’s perspective, we’re back to running other teams’ services, or…

**Do you use mocks so that each team can exercise their tests independently?**

This is my preferred approach.

Tools like [WireMock Cloud](https://wiremock.org/) \[6\] are very helpful here. You can start by uploading an OpenAPI spec or manually configuring the routes.

They also support chaos testing – you can add delays or error responses for specific routes.

I find WireMock Cloud a great way to test third-party APIs. It can also be used to test integration with other teams’ services without hosting them yourself.

For example, in your dev environment:

1.  Start by uploading the OpenAPI spec for the other team’s microservice to WireMock Cloud.
2.  Configure the mock API to return success and failure responses based on routes.
3.  Configure your microservices to use the mock API.
4.  Execute end-to-end tests with Cypress or Selenium.

Sometimes, a feature requires coordinated changes across multiple microservices. You can update the mock API to reflect the agreed-upon change in other microservices and start testing your code right away. It reduces the amount of coordination and interdependence between teams.

However, this approach also requires extensive automation to keep the mock APIs up to date. It also demands that teams document their APIs rigorously—and that’s a good thing! I wish more teams practised contract-first development.

### Summary

End-to-end testing across bounded contexts in a microservices environment requires a careful balance of responsibilities and collaboration.

Microservice teams should focus on service-level testing. Tools like Pact help catch integration problems early while you’re still making code changes.

QA teams often oversee user journeys and use tools like Cypress or Selenium to test integration across the system.

Full-stack teams own both the frontend and backend. So they can test their part of the user journey autonomously.

They can host other teams’ microservices to support end-to-end tests or use tools like WireMock to test their parts of the user journey in isolation.

There is more than one way to test user journeys that span multiple bounded contexts. Your choice depends on organizational structure, team responsibilities, and the maturity of your testing practices.

Ultimately, every part of the user journey should be tested, whether it’s done piecemeal by individual teams or centrally by a QA/cross-functional team. And it’s OK to have both!

Service teams should test their parts of the user journey independently. This will allow them to be more exhaustive, help them catch edge cases, and identify problems early.

The QA team’s tests will be broader in scope and can catch integration problems that are difficult to spot at the service level, especially when 3rd party integrations and manual steps are involved.

After all, small amounts of overlapping tests will hurt a lot less than insufficient test coverage of important user journeys!

### Links

\[1\] [Production-Ready Serverless workshop](https://productionreadyserverless.com/?utm_campaign=e2e-test-across-bounded-contexts&utm_source=newsletter&utm_medium=links&utm_content=text-link)

\[2\] [Pact](https://pact.io/)

\[3\] [Cypress](https://www.cypress.io/)

\[4\] [Selenium](https://www.selenium.dev/)

\[5\] [Microfrontends with Luca Mezzalira](https://realworldserverless.com/episode/77)

\[6\] [WireMock Cloud](https://wiremock.org/)

[![](https://theburningmonk.com/wp-content/uploads/2025/02/limit-e2e-test-scope-title-300x169.png)](https://theburningmonk.com/2025/02/event-driven-architectures-how-to-limit-the-scope-of-end-to-end-tests/)

[![](https://theburningmonk.com/wp-content/uploads/2024/04/tdd-serverless-feature-300x169.jpg)](https://theburningmonk.com/2024/04/how-to-apply-the-tdd-mindset-to-serverless/)

[![](https://theburningmonk.com/wp-content/uploads/2025/04/detect-breaking-change-title-300x169.png)](https://theburningmonk.com/2025/04/how-to-detect-and-prevent-breaking-changes-in-event-schemas/)

[![](https://theburningmonk.com/wp-content/uploads/2019/09/sns-kinesis-e2e-300x166.png)](https://theburningmonk.com/2019/09/how-to-include-sns-and-kinesis-in-your-e2e-tests/)

[![](https://theburningmonk.com/wp-content/uploads/2024/07/you-are-doing-it-wrong-feature-300x171.jpg)](https://theburningmonk.com/2024/07/im-sorry-but-the-way-you-adopt-serverless-is-wrong/)

[![](https://theburningmonk.com/wp-content/uploads/2022/05/Screenshot-2023-04-04-at-17.23.31-300x166.png)](https://theburningmonk.com/2022/05/my-testing-strategy-for-serverless-applications/)

**Whenever you’re ready, here are 3 ways I can help you:**

1.  [**Production-Ready Serverless**](https://productionreadyserverless.com/?utm_campaign=3-ways-I-can-help&utm_source=blog&utm_content=text-link): Join 20+ AWS Heroes & Community Builders and 1000+ other students in levelling up your serverless game. This is your one-stop shop for **quickly levelling up your serverless skills**.
2.  I help clients **launch product ideas**, **improve their development processes** and **upskill their teams**. If you’d like to work together, then let’s [**get in touch**](https://theburningmonk.com/hire-me/).
3.  [**Join my community on Discord**](https://discord.gg/Ucc9nZBA8H), ask questions, and join the discussion on all things AWS and Serverless.
