---
url: "https://medium.com/@mrjoelkemp/giving-better-code-reviews-16109e0fdd36"
captured_at: "2016-02-07T22:54:23-03:00"
title: "Giving better code reviews — Medium"
domain: "medium-com"
---

# Giving better code reviews

I take code reviews very seriously. It’s one of the crucial processes for ensuring the spread of knowledge transfer and best practices throughout a development team.

As important as code reviews are, we typically leave it up to the reviewer to improve his/her process. This results in an inconsistent review quality across a team. The poor reviewers become known and folks looking for an easy approval know who to go to.

**Your team is only as good as your weakest reviewer.**

There are at least two phases of reviewing code. Most stop at the first (least valuable) phase.

#### Phase 1: The light pass

In this first pass of a code diff, we typically look for the following:

- Obvious mistakes: typos, poor variable names, unclear function names, large function definitions.
- At least one test. This assumes mandatory tests are part of the dev culture.
- Commented out code that should be deleted.
- Violations of our styleguide that linters don’t catch yet.

If the pull request author proofread their diff (which they should be doing) before pinging for a review, then there’s a good chance that there are only a few violations of the above points. Many reviewers, at this point, will just go ahead and give the “looks good to me” (LGTM). Also at this phase, sloppy or lazy reviewers will do a “terms of service” review: scroll, scroll, scroll, accept. We can do better.

#### Phase 2: The contextual pass

This deeper pass of the diff potentially takes a lot of time. Many reviewers are unsure of how much time to spend on a review, so they’ll punt on digging deep into a diff and trust the author.

Trust no one. Question everything (kindly). Assume that the author has made mistakes that you need to catch. Save your users from those bugs.

As an aside, I find that this trust happens a ton with less experienced developers. They believe that authors with more experience *must* know what they’re doing, so there’s no need to question the code. Make sure that you address and correct this assumption. This deprives less experienced devs with the context that they desperately need.

In this contextual phase, we’re looking for the following:

- More idiomatic ways of using our frameworks/libraries.
- Adequate test coverage for changed lines or critical code paths.
- That the tests (non-trivially) pass, assert a valuable behavior, and do not (if you can help it) test implementation details.
- Ways of strengthening tests
- Alternative implementations or [refactors](https://sourcemaking.com/refactoring) that increase readability/understandability and/or maintainability.
- Unhandled edge-cases based on data-type/data-existence assumptions in a function.
- That you can actually understand what the code is doing. I used to think it was my fault for not being able to understand part of a diff. It’s not. Hard to reason about code should be corrected. If *you’re* struggling to understand, folks with even less experience have no hope.
- Can you gather context for that diff? i.e., if you’re totally unfamiliar with that part of the codebase, could you roughly tell what that part of the system does and how the diff affects it?
- Logical omissions or errors
- If you know the feature requirements, look for spec omissions. “Shouldn’t this component also do X?”

Feel free to ask questions on particular lines. It’s okay for you to want to know what’s going on; it’s not a burden on the author. It’s crucial that this context is spread across many team members.

Also be aware of how you ask questions. Suggest approaches or provoke exploration. Try not to give solutions.

#### But this diff will take forever to review

Giving a valuable code review requires that pull requests are small (<200 lines as a rough gauge). It’s unfair to give a reviewer a diff consisting of hundreds or thousands of lines of code changes. They’ll end up spending anywhere up to 30 minutes reviewing that diff and then have to do re-reviews when you make suggested changes. There’s definitely an inverse correlation between lines of code and review quality.

Sometimes, folks from other feature teams will send you a diff to review, but you might not have any real context as to what they’re working on. Naturally, it would take you a long time to gather enough context to give an effective review. In those cases, I tell the author that I can’t really give a quality review on that diff and that they should look for another reviewer. If no one else is available, I’d sit with the author and have them talk me through the diff — allowing me to ask questions at each step. It’s a time sink for both of us, but we, the code, and our users will end up better-off for the detailed analysis.

We have to be pragmatic though. Issues with a hotfix can be addressed in a follow-up diff. Have we hit the point of diminishing returns with our comments? Are we spinning our wheels with subjective nitpicks?

If you’d like to save some time, consider labeling “blocking” and “non-blocking” review comments. If a reviewer has the time and agrees with the benefit in the non-blocking comment, they can address it.

#### Can we do even better?

I firmly believe that reviewing code is as much of a craft as writing code. As reviewers, it’s our mission to improve on a number of fronts: our ability to understand code; our process, awareness, and criteria for analysis; and our teammates’ ability to write correct diffs.

I’d love to hear your thoughts/improvements/additions on my guidelines for reviewing diffs. Find me on twitter: [mrjoelkemp](https://twitter.com/mrjoelkemp).
