---
url: "https://journal.optivem.com/p/spec-driven-development-make-specs"
captured_at: "2026-09-28T14:33:42+01:00"
title: "Spec-Driven Development: Make Specs Enforceable with ATDD"
domain: "journal-optivem-com"
---

_I help teams adopt Spec-Driven Development, so that they can write code faster with AI agents. I have a few spots left for 2027._

[Book a call](https://calendly.com/valentinajemuovic/call)

“Spec-driven development” is everywhere in AI tooling right now: Kiro, GitHub’s spec-kit, Tessl. Write the spec first, then let the agent build against it. Birgitta Böckeler reviewed all three in [Understanding Spec-Driven-Development: Kiro, spec-kit, and Tessl](https://martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html) on martinfowler.com and found the catch.

In every one of them, “spec” means a Markdown document the agent is supposed to read. **Nothing checks that the code matches it, and the agents don’t always follow it.** As she put it: “I frequently saw the agent ultimately not follow all the instructions.”

The problem isn’t the tools. It’s that the spec is a Markdown file, and **you can’t run a Markdown file against the code.** To find out whether the agent followed it, a person has to read the code line by line. That’s the work you hoped the spec would save.

We’ve had a spec without this problem since 1999. Kent Beck’s first Extreme Programming book, [Extreme Programming Explained](https://dl.acm.org/doi/abs/10.5555/318762) (1999), already had acceptance tests, and the [XP rules](http://www.extremeprogramming.org/rules/functionaltests.html) on extremeprogramming.org spell out how they work: acceptance tests “are created from user stories” and “should be automated so they can be run often.”

In 2010, Jez Humble and Dave Farley’s [Continuous Delivery](https://www.amazon.com/dp/B003YMNVC0) gave automated acceptance tests their own chapter: “Acceptance tests are a crucial stage in the deployment pipeline: They take delivery teams beyond basic continuous integration. Once you have automated acceptance tests in place, you are testing the business acceptance criteria of your application, that is, validating that it provides users with valuable functionality.”

An acceptance test is the spec and the check in one: it describes what the system should do, and it fails until the system does it.

**An agent can ignore a Markdown file.**

**It can’t ignore a test that won’t pass.**

An acceptance test doesn’t call the system directly. It calls a DSL, and the DSL calls two kinds of drivers. System drivers talk to the system through its UI or API. External-system drivers talk to the external systems it depends on, such as an ERP.

[

![](https://substackcdn.com/image/fetch/$s_!ol6t!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc3640883-04bc-47c3-9204-41e9f9eeccd4_1760x1778.png)

](https://substackcdn.com/image/fetch/$s_!ol6t!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc3640883-04bc-47c3-9204-41e9f9eeccd4_1760x1778.png)

In acceptance test-driven development (ATDD), the Red step is where you write that test, before any system code exists. When an AI agent does the work, the Red step is split into four small steps, and a human reviews each one.

[

![](https://substackcdn.com/image/fetch/$s_!-OUs!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc95d581b-fab0-4902-a97a-edddd337345f_1760x3354.png)

](https://substackcdn.com/image/fetch/$s_!-OUs!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc95d581b-fab0-4902-a97a-edddd337345f_1760x3354.png)

In every box, the AI writes the code, a human reviews it, and then it’s committed.

Example: placing an order in an online shop.

It starts with a ticket. Its acceptance criteria are agreed before any code is written:

```
Scenario: Calculate the base price from unit price and quantity
  Given a product with unit price 20.00
  When I place an order for 5 of that product
  Then the order is placed successfully
  And the order’s base price is 100.00
```

**1\. Write Acceptance Tests**

The agent turns the acceptance criteria into a test. The test is written in a DSL, the test code’s own vocabulary (`placeOrder().withQuantity(...)`). Here’s the acceptance test, from `PlaceOrderPositiveTest.java`:
