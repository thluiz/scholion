---
url: "https://medium.com/@fagnerbrack/one-commit-one-change-3d10b10cebbf?ct=t(BrazilJS_Weekly_468_9_2013)"
captured_at: "2016-05-19T14:06:56-03:00"
title: "One Commit. One Change. — Medium"
domain: "medium-com"
---

# One Commit. One Change.

A few weeks ago I attended a series of [3 talks from Martin Fowler in Australian Technology Park, Redfern, Sydney](http://www.eventbrite.com.au/e/yow-thoughtworks-bring-you-martin-fowler-sydney-march-29-tickets-22103248411). One of the talks was about deriving the application state from a sequence of persisted events. A.K.A [Event Sourcing](http://martinfowler.com/eaaDev/EventSourcing.html):

> The fundamental idea of Event Sourcing is that of ensuring every change to the state of an application is captured in an event object, and that these event objects are themselves stored in the sequence they were applied for the same lifetime as the application state itself.

That talk reminded me a lot about Git, which is built using the principle that if you replay all committed changes since the beginning and in the same chronological order, you will get the exact same result. The current state.

> In Git, if you replay all committed changes since the beginning and in the same chronological order, you will get the exact same result.

However Git is just a tool. It is the responsibility of the engineer to use it in a way that brings the most valuable possible outcome. One of these responsibilities is taking care of how changes are inserted into the SCM, creating a commit which purpose should reflect one change, and one change only. Also known as an **atomic change**.

As from the [emacs manual](https://www.gnu.org/software/emacs/manual/html_node/elisp/Atomic-Changes.html), in database terminology, an **atomic change** is an indivisible **change** — it can succeed entirely or it can fail entirely, but it cannot partly succeed.

In Git, it means that a change should be able to be reverted ([git-revert](https://www.atlassian.com/git/tutorials/undoing-changes/git-revert)) and not cause any side effects or conflicts in other parts of the system other than the one that is being reverted. Also, it should contain a single change that doesn't have real value if applied partially.

> An atomic commit should be able to be reverted or applied without side effects.

Another important point about atomic commits is the fact that it should not break the normal flow of your build, it should just remove or add something cleanly. If you have a build routine or tests, you should be able to run it successfully whether the commit is there or not, just by assuming a specific set of premisses. “Premisses” in this context represents the **required state of the codebase** in which the commit can be applied with the least amount of codeconflicts.

This is more important if you are committing into the master branch, the one branch in which the history should always be in a consistent and immutable state.

> An atomic change is a piece of functionality that can be replayed over and over again against a specific set of premisses.

Not breaking the build is an important aspect of atomicity, because then it is possible to reset your application to any state in order to see how the application was working at that time. It is also possible to easily leverage built-in tools to find bugs in the history (such as [git bisect](http://webchick.net/node/99)), something that can't be easily done if one can't run the build after a [reset](https://jwiegley.github.io/git-from-the-bottom-up/3-Reset/4-doing-a-hard-reset.html).

As a last point, we have the principle of traceability of changes. Ideally one should be able to track the whole source and purpose of a change through the history of the commits without having to talk with the original author, because he or she might not be available anymore or not even remember what that change was all about. If a commit does more than one thing, it might be impossible to understand in the future why those lines in the system were changed.

#### Conclusion

If you create commits with more than one change, it will be hard to find the point in time in which a mistake or feature was introduced in the codebase, it will be hard to reset the codebase to a previous state, and might be impossible to revert a modification without side effects.

This is a principle, not a law. Be thoughtful and make the best decision given the circumstances.

> Have some feedback? Check out [Twitter](https://twitter.com/FagnerBrack) | [Facebook](https://www.facebook.com/fagner.brack) | [Github](http://github.com/FagnerMartinsBrack)

![1*ULpvg21u7psQW5k0p6ZjFQ.gif](medium-com--one-commit-one-change/103bc0fb1a920fd08958edd8cd5c39b3.gif)

*Enjoyed reading this? Share or click “recommend” to support more articles!*
