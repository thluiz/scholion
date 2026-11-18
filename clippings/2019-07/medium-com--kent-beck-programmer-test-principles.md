---
url: "https://medium.com/@kentbeck_7670/programmer-test-principles-d01c064d7934"
captured_at: "2019-07-05T11:45:53+00:00"
title: "Programmer Test Principles"
domain: "medium-com"
---

Programmer Test Principles

Kent Beck · Jun 27, 2019

BDD versus TDD. This test tool versus that test tool. Test-before versus test-after versus this-works-trust-me. At some point I got tired of the debates about details. I prefer to discuss principles.

Details go back and forth without any push to conclusion. Chocolate versus vanilla. Chocolate. Vanilla. Chocolate. Vanilla.

Even if someone is compelled to concede an argument about details, that concession is at risk. What if something about my context says chocolate but I let you make me eat vanilla? Not progress.

## Principles

Principles, on the other hand, provide a generative basis for discussion. If we agree on principles but my context is different, then our answers can differ without disagreement. The principles generates different answers in different contexts.

Disagreement in principle is also more productive than disagreement in detail. I can say I prioritize speed over completeness while you prioritize completeness over speed. We can both be “right” in our context, that is our decisions can best meet our needs, but by discussing at the level of principles we give ourselves the best chance to understand our differences.

## Programmer Tests

Tests are an oracle. Oh great oracle, what will happen if I deploy now? Disaster, my child. Tests predict deployment consequences.

Programmer tests are an oracle providing feedback coding-decision-by-coding-decision. Programmer tests are a subject to a difficult set of constraints.

Programmer tests should be fast. Feedback should not disrupt programming flow. Slow tests encourage batching coding decisions. Subsequent test failures are harder to debug. Was it decision 1, decision 2, or the combination of the two?

How fast is fast? Sub-second seems to be one discontinuity. That’s the amount of wait time that is not worth glancing away. Ten seconds is long enough to sit back and glance away, but not long enough to start something new. A minute is a context switch. A minute is long enough that you are tempted to reduce the number of times you run the tests, increasing the cost of debugging.

Programmer tests should be deterministic. I wouldn’t have thought that this would be controversial, except I regularly see “flaky” tests. I liked the Facebook policy of simply deleting non-deterministic tests. If you don’t want to lose coverage, change the design so it’s testable and write the test again.

Programmer tests should be predictive. If your oracle says, “Go ahead, deploy,” and deployment fails, you’ll stop believing your oracle.

Programmer tests should be sensitive to behavior changes and insensitive to structure changes. If the program’s behavior is stable from an observer’s perspective, no tests should change.

Structure-invariant tests requires a particular style of programming and design as well as a particular style of design. I frequently see tests that assert, “Assert that this object sends this message to that object with these parameters and then sends this other message to that other object.” An assertion like this is basically the world’s clumsiest programming language syntax. If I care about the order of operations, I’ve designed the system wrong.

Programmer tests should be cheap to write. We don’t get paid for tests, we get paid for code that a) works and b) can be changed. Tests can help with that but, all else equal, less effort on tests is better.

Programmer tests should be cheap to read. Tests, like code, are read more than written.

Programmer tests should be cheap to change. The common counter-example is a single behavior change that results in a pile of red tests. If each test now has to be examined and modified individually, then tests become a parking brake on change.

Summary — programmer tests should:

- Minimize programmer waiting.
- Run reliably.
- Predict deployability.
- Respond to behavior changes.
- Not respond to structure changes.
- Be cheap to write.
- Be cheap to read.
- Be cheap to change.

That’s a difficult set of constraints to resolve. Some of them are contradictory. Figuring out which are more important and how best to satisfy the most important — that’s your job.

## Space

My concern as I coach programmers is that they haven’t explored the space of tests. Tests just have to run in a minute or more. Tests just have to be non-deterministic. Tests just have change when code structure changes. Nope.

Take these principles. Find a test that violates them. Imagine the equivalent test that would satisfy the principles. If you can’t write that test, imagine the design of the software under test that would enable you to write a test satisfying the principles of programmer tests.
