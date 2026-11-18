---
title: "Programmer Test Principles"
date: '2019-07-05T11:45:53+00:00'
category: webclip
summary: 'Kent Beck proposes principles for programmer tests, focusing on speed, determinism, predictiveness, behavior focus, and low cost to write, read, and change instead of debating testing techniques.'
tags: ["testing", "tdd", "software-design"]
has_commentary: false
generated_by: "openai/gpt-5.1"
sources:
  - title: "Programmer Test Principles"
    url: "https://medium.com/@kentbeck_7670/programmer-test-principles-d01c064d7934"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2019-07/medium-com--kent-beck-programmer-test-principles.md"
    kind: repo
---

Kent Beck shifts attention from debates over testing styles and tools to underlying principles. He argues that agreeing on principles lets programmers reach different solutions suited to their own contexts while still understanding each other’s choices. Programmer tests are described as an oracle that predicts deployment outcomes, and they must satisfy several demanding constraints to provide reliable, useful feedback.

He outlines expectations for programmer tests: they should run fast enough to avoid breaking flow, be deterministic, and accurately predict whether code is safe to deploy. They should react when observable behavior changes but stay stable when internal structure changes. Beck criticizes tests that over-specify internal message passing as brittle and akin to a bad programming language. Tests also need to be cheap to write, read, and change, or they will hinder evolution of the code. He encourages programmers to explore the design space by spotting tests that violate these principles, imagining better tests, and if needed, redesigning the production code to make such tests possible.

## Reading notes

- The author is tired of arguments about BDD vs TDD, tools, and timing of tests, and prefers to discuss underlying principles instead of details.
- He compares detail debates to choosing between chocolate and vanilla, where arguments can drag on without real progress.
- Principles are described as a generative basis for discussion, allowing different answers in different contexts without direct disagreement.
- Disagreements about principles, such as valuing speed over completeness or vice versa, are presented as more productive than fights over specific practices.
- Tests are characterized as an oracle that answers what will happen on deployment, predicting consequences like potential disasters.
- Programmer tests provide feedback at the level of individual coding decisions but must satisfy several hard constraints.
- Tests should be fast so feedback does not interrupt programming flow, because slow tests push programmers to batch changes.
- Batching changes makes debugging harder when tests fail, since it becomes unclear which decision or combination caused the failure.
- He identifies time thresholds: under a second feels immediate, around ten seconds invites a brief pause, and a minute or more triggers a full context switch.
- Long test times tempt programmers to run tests less often, which increases the cost of debugging later failures.
- Tests must be deterministic, and the author notes that flaky tests are still common even though this seems like an obvious requirement.
- He cites Facebook’s practice of deleting non-deterministic tests, suggesting redesigning the code and then rewriting the test to retain coverage.
- Tests should be predictive so that if they say deployment is safe, the actual deployment should not fail in ways they should have caught.
- When tests repeatedly miss real deployment failures, programmers lose trust in them as an oracle.
- Tests should be sensitive to externally observable behavior changes but not to internal structural changes in the code.
- If behavior remains stable from an observer’s point of view, the author asserts that no tests should need to change.
- Structure-invariant tests call for a particular style of programming and test design focused on externally visible effects.
- He criticizes tests that assert fine-grained internal interactions between objects, including specific messages and parameters.
- Such interaction-heavy assertions are compared to a clumsy programming language syntax that over-constrains implementation details.
- The author suggests that when order of operations matters at this level, it points to design problems in the system.
- Tests should be cheap to write, since revenue comes from working, changeable code, with tests serving as a means to that end.
- Given equivalent benefits, he prefers approaches where programmers spend less time and effort on tests.
- Tests should also be cheap to read, recognizing that, like production code, they are read more frequently than they are written.
- Tests need to be cheap to change so they do not become a drag on modifying the system’s behavior.
- He points to situations where a single behavior change causes many failing tests that must each be manually updated as an example of expensive tests.
- When tests require widespread individual updates, they function like a parking brake that resists necessary changes.
- He summarizes that programmer tests should minimize waiting, run reliably, predict deployability, react to behavior changes, ignore structural changes, and be inexpensive to write, read, and change.
- The author calls this list a difficult and sometimes contradictory set of constraints that programmers must balance according to priorities.
- He expresses concern that many programmers have not fully explored the space of testing possibilities and accept limitations as fixed.
- He challenges assumptions that tests must be slow, non-deterministic, or tightly coupled to code structure, rejecting these as requirements.
- He proposes an exercise: identify a test that breaks one of the principles and imagine an alternative test that would comply.
- If it is impossible to conceive such a test within the current design, he suggests imagining a different design that would support tests aligned with these principles.
