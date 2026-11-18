---
title: "Epistemology of software"
date: '2025-10-23T17:05:50+00:00'
category: webclip
summary: 'The article connects philosophy of science with software, arguing that test-driven development applies the scientific method to code and builds empirical confidence that software behaves as intended.'
tags: ["epistemology", "software-testing", "tdd", "software-development"]
has_commentary: false
generated_by: "openai/gpt-5.1"
sources:
  - title: "Epistemology of software"
    url: "https://blog.ploeh.dk/2025/10/20/epistemology-of-software"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/blog-ploeh-dk--epistemology-of-software-tdd-as-scientific-method.md"
    kind: repo
---

The text connects general epistemology and philosophy of science with software development. In empirical science we never gain certainty, only increasing confidence through hypotheses, falsifiable predictions, experiments, and subsequent adjustments. This view is applied to software: product owners and developers can only know how software behaves by forming expectations about observable behaviour and then testing those expectations.

Manual and automated tests are presented as empirical experiments on software. Manual testers follow test plans that implicitly encode hypotheses about how the application should respond. Automation speeds up and stabilizes these experiments but introduces the problem that tests themselves can be wrong. The article frames test-driven development (TDD) as a direct implementation of the scientific method, because each test is introduced with a falsifiable prediction about how it will initially fail and later pass.

## Reading notes

- In philosophy of science, knowledge is treated as approximate: experiments bring us closer to truth without ever delivering certainty.
- The scientific method is sketched as an iterative loop of forming hypotheses, predicting outcomes, experimenting, and adjusting when predictions do not match observations.
- The Galilei falling-bodies example illustrates that repeated experiments can make a hypothesis highly probable without proving it conclusively.
- The author asks what happens when this empirical, probabilistic notion of knowledge is applied to software development.
- From a non-coding product owner's perspective, determining whether software solves a problem reduces to forming expectations and testing them in practice.
- Any kind of testing, ad-hoc or planned, manual or automated, becomes the primary way to judge whether the software works.
- Traditional test plans managed by dedicated test departments still represented empirical verification, with each test encoding a conditional expectation about behaviour.
- Manual human interaction is realistic for user-facing applications but is slow and error-prone, especially when repetitive scenarios cause testers to miss details.
- Automating tests offers faster and more reliable feedback but raises the question of how to gain confidence that the test code itself is free of bugs.
- The text proposes using the scientific method on tests by making incremental falsifiable predictions about code and test behaviour.
- In TDD, the developer first writes an automated test without production code while predicting that the test will fail when run.
- If such a first test unexpectedly passes, that outcome falsifies the prediction and indicates a defect in the test, such as a tautological assertion.
- When the initial test fails as expected, this failed attempt to falsify the prediction supports the hypothesis that the test is correctly specified, though it still does not prove it.
- The next step is to implement only enough production code to satisfy the test, accompanied by a new prediction that the test will now succeed.
- If the updated test fails, the developer knows that either the fresh implementation or the test itself is flawed, or some external factor interfered.
- If the test passes after adding minimal code, this result again corroborates but does not prove the joint hypothesis about test and production correctness.
- Adding a second test leads to another prediction: running all tests should cause the new one to fail before adding new production code.
- Repeating this cycle of writing a failing test, then adding just enough code to make it pass, gradually builds evidence for two linked hypotheses: the tests behave as intended and the production code does as well.
- The author emphasizes that this process increases confidence instead of delivering proofs, mirroring empirical science.
- Skipping the step of writing the test first removes the experiment in which a new test is expected to fail and thus discards half of the available empirical evidence.
- The article explicitly claims that TDD exemplifies the scientific method because watching tests fail is fundamental to its workflow.
- Merely reading test code without executing it is compared to ancient introspective theories such as the four humours or extramission, which lacked empirical checks.
- The author points out that developers often believe code is correct until running it reveals errors, showing that understanding by inspection is unreliable.
- When tests are written after the system under test, a passing test yields ambiguous information: it might be correct, tautological, or accidentally encoding an existing bug.
- Likewise, a failing post-hoc test leaves uncertainty about whether the test is wrong or the system under test is defective.
- Characterization tests are cited as an example where the process explicitly includes writing an assertion that is expected to fail to validate the test's effectiveness.
- The author prefers to write what seems like a correct assertion and then temporarily sabotage the system under test to force a failure, again to verify test sensitivity.
- The core claim is that seeing a test fail when strongly predicted to do so is vital empirical evidence about the quality of the tests.
- In the conclusion, the text ties software verification back to the broader epistemological question of how any knowledge is formed.
- Software can be subjected to the same scientific regimen by hypothesizing behaviour under given conditions, predicting observable outcomes, testing, recording results, and fixing defects.
- TDD is described as closely aligned with this regimen and thus a highly scientific method for developing software.
- The author acknowledges that both science and TDD are demanding practices but presents TDD as one of the most rigorous and effective ways to increase confidence that software behaves as intended.
