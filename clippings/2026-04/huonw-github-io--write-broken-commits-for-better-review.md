---
url: "https://huonw.github.io/blog/2026/04/broken-commits/?utm_source=tldrnewsletter"
captured_at: "2026-04-17T15:51:15+01:00"
title: "Write broken commits for better review | Huon on the internet"
domain: "huonw-github-io"
---

---
I spend a lot of time reviewing code, and I think it’d be easier if I saw more tastefully broken commits. Commits construct a story about a change: “first this happened, then that, that another thing” is a good narrative; “first everything happened, the end”… not so much. Sometimes, telling that story is impossible without having a commit that breaks tests or doesn’t compile!

The principle that usually drives me to commit broken code is making **mechanical changes obviously mechanical and mechanically obvious**: reformatting, renaming a function or file, re-indenting, … are not “real” changes like adding new code or optimising a loop, and intermixing mechanical & real changes all at once makes verifying either of them hard.

If mechanical changes are separate, it’s easy to be sure of huge changes: “yes, this commit is solely running a code formatter on 3k files”. I can literally check out the parent commit, and run the same formatting command, and get the same result. Mechanically obvious!

I’m feeling acute pressure on my ability to review code as I use more AI. I’m personally accountable for code that I’ve only reviewed, so it better be a damn good review. Any trick that makes that review easier is a good one.

The technique is unlocked by separating commits into two buckets, “units of review” and “units of persistence”, via squash merges: we can be deliberate about nice commits for a reviewer now, without cluttering the long-term history.

## Review dance

Code review is a dance between code author and code reviewer<sup id="fnref:split"><a href="https://huonw.github.io/blog/2026/04/broken-commits/?utm_source=tldrnewsletter#fn:split" rel="footnote" role="doc-noteref">0</a></sup> that requires **coordination and anticipation**: the code author should be planning how to make their change easier for a reviewer to validate, before writing the final code<sup id="fnref:ai"><a href="https://huonw.github.io/blog/2026/04/broken-commits/?utm_source=tldrnewsletter#fn:ai" rel="footnote" role="doc-noteref">1</a></sup>. When I prepare a change, I want to help the reviewer help me!

A common technique is smaller changes building into a big one: each small step is individually green (passing tests, compiling, whatever validation is used) and ‘clearly’ correct. If each is correct, then the overall change is likely correct too. I can review each step, get a sense of the overall diff, and feel confident.

However, I hit the limits of always-green: sometimes it’s very hard to break a particular step into smaller understandable sub-steps that still ‘work’, like when a small manual change entails a large automated one. In this case, tasteful breakage is useful to **achieve separation**: the overall change is built of several commits, and the last one is where it all comes together.

## Unit of review, vs. unit of persistence

Writing intentionally-broken commits makes most sense when using “Squash and merge” for merging changes. Using squashes separates two lives that commits live:

-   they’re **units of review**: the pieces that can be assessed to understand a change
-   they’re **units of persistence**: the pieces that are actually landed in long lived branches

Using squash and merge, one can tailor work to benefit from both, by preparing small pull or merge requests (PR, hereafter) that are:

-   a **single atomic change** overall (the combined change that’s landed in `main` as a single commit, the unit of persistence),
-   built from several **non-atomic subsections** (several commits written locally, the unit of review).

A code archaeologist sometimes finds a persisted commit via `git log` & `git blame` and wants to understand the nitty-gritty details. Given this, it can feel unsatisfactory to squash away a PR’s internal commits<sup id="fnref:merge"><a href="https://huonw.github.io/blog/2026/04/broken-commits/?utm_source=tldrnewsletter#fn:merge" rel="footnote" role="doc-noteref">2</a></sup>. I’ve found this fine in practice, the PR and its “units of review” commits still exist<sup id="fnref:history"><a href="https://huonw.github.io/blog/2026/04/broken-commits/?utm_source=tldrnewsletter#fn:history" rel="footnote" role="doc-noteref">3</a></sup>, and someone who cares about a particular change in that much detail probably also cares about any discussion on the PR: they’re gonna be opening the PR anyway.

This is not an excuse to make huge PRs though: this is about commit granularity finer than the usual “make small commits/PRs” advice. Both are helpful.

## When to do it

I’ll systematically and habitually use broken commits when…

1.  **Adding or updating a code formatter**: add/update the formatter in the first commit (manual change), actually run it in the next (fully automatic), then do any fix-ups (if required) in the last (again, manual). This sequence is only correct at the end, once the codebase is formatted according to the new formatter… but a single commit mixing manual changes with the automatic ones means thousands of lines of automated reformatting drowning the handful of interesting manual ones. That makes for hard reviews and hard rebases<sup id="fnref:rebase"><a href="https://huonw.github.io/blog/2026/04/broken-commits/?utm_source=tldrnewsletter#fn:rebase" rel="footnote" role="doc-noteref">4</a></sup>.
2.  **Adding or updating a lint rule**, especially one with automatic fixes: similar to a formatter, a mix of “tweaking configuration” and “fixing consequences” makes for harder review.
3.  **Renaming functions or named arguments**: rename the ‘declaration’ in one commit, update uses in another, then apply any reformatting in a third (if the new name is longer or shorter and causes different line-wrapping).
4.  **Renaming files**: if I’m doing a larger refactor and it requires renaming a file (like moving it to a new location, or matching a new function/class name, for function/class-per-file), doing that rename at the same time as other changes risks disguising the rename as a delete/recreate<sup id="fnref:recreate"><a href="https://huonw.github.io/blog/2026/04/broken-commits/?utm_source=tldrnewsletter#fn:recreate" rel="footnote" role="doc-noteref">5</a></sup>, if those other changes are extensive. Having a single commit that just does the rename (not even updating the imports) makes that clearer.
5.  **Re-indenting significant blocks**: similar to renaming, a large re-indent from adding or removing an `if` or loop can disguise changes<sup id="fnref:ignore-whitespace"><a href="https://huonw.github.io/blog/2026/04/broken-commits/?utm_source=tldrnewsletter#fn:ignore-whitespace" rel="footnote" role="doc-noteref">6</a></sup>. Doing a commit that’s (close to) just the re-indent alone can help keep things focused.
6.  **Moving large code chunks**: similar to renaming and re-indenting, shifting a block of code or function around can be hard to understand if it’s both shifted and changed at the same time.

The common thread through these is that we’re building a PR that involves some mechanical changes and some ‘real’ ones. Separating them at the commit level, even if invalid, makes **both types** of changes easier to understand: verify the config, then rerun the formatter yourself; see the ‘renamed’ description for the file, guaranteed; extract the two blocks that were supposedly moved into separate files (or use a fancier diff viewer) and compare them<sup id="fnref:adversarial"><a href="https://huonw.github.io/blog/2026/04/broken-commits/?utm_source=tldrnewsletter#fn:adversarial" rel="footnote" role="doc-noteref">7</a></sup>.

Beyond that list, I’ll use it whenever I think it’ll help my reviewer and myself be sure the code is correct: this is all just guidelines and vibes. **Do what is useful**!

This technique can easily be taken too far: individual commits for each character added or deleted won’t help the reviewer.

It also requires a little thought and preparation: slamming out all the code, and then committing later can be hard to detangle, even with `git add --patch`. Instead, I’ll estimate where the code is likely to go, plan ahead, commit often, and then quickly rewrite history to streamline down to a useful story (`git rebase --interactive` is magic).

## Brook no lAIziness

With AI slopping out a lot of code, I find myself doing even more code review than I ever have before. I need to be **aggressively sure** that the code is sensible, because I’m still accountable for everything shipped under my name, whether brain- or vibe-coded. Unfortunately, AI tools don’t help: they seem to often default to Just Do It… Just Do It All In One Go Plus Some Bonus Unrelated Changes And Then “Done. Should I commit it?”.

Forcing them to commit progressively makes my life easier: I see more of the story, review is easier, and revisiting/removing silly changes is easier too.

Unfortunately, AI is often fixated on having everything work before committing (“Let me check tests pass…”). I find myself needing to give strong encouragement and reminders, so that it commits with more nuance and tells a better narrative.

I expect a good commit story from the indefatigable machine, and I brook no laziness from it. Encouraging broken commits where appropriate helps me review more closely and ‘sit’ in the code more deeply, building understanding as best I can without brain-coding it myself.

## Break;

I assume that all code is broken. Despite this, intentionally broken code can lead to better outcomes: for some changes, splitting them to tell a good story is more valuable than every commit passing tests. Better stories mean better review, better review means deeper understanding and better code.

In this age of AI, good reviews are how I build the deep understanding that lets me feel comfortable being accountable for my code.

This article is from a human: I used no AI to write it.
