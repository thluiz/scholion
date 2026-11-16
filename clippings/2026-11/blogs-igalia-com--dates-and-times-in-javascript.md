---
url: "https://blogs.igalia.com/compilers/2020/06/23/dates-and-times-in-javascript"
captured_at: "2026-11-16T02:59:48+00:00"
title: "Dates and Times in JavaScript"
domain: "blogs-igalia-com"
---

*   By Compilers Team,
*   23 June 2020
*   [date](https://blogs.igalia.com/compilers/tags/date/)
*   [feedback](https://blogs.igalia.com/compilers/tags/feedback/)
*   [javascript](https://blogs.igalia.com/compilers/tags/javascript/)
*   [proposal](https://blogs.igalia.com/compilers/tags/proposal/)
*   [standards](https://blogs.igalia.com/compilers/tags/standards/)
*   [tc39](https://blogs.igalia.com/compilers/tags/tc39/)
*   [temporal](https://blogs.igalia.com/compilers/tags/temporal/)
*   [time](https://blogs.igalia.com/compilers/tags/time/)

**tl;dr: We are looking for feedback on the [Temporal proposal](https://tc39.es/proposal-temporal/docs/index.html). Try out the [polyfill](https://www.npmjs.com/package/proposal-temporal), and complete the [survey](https://forms.gle/iL9iZg7Y9LvH41Nv8); but don't use it in production yet!**

JavaScript `Date` is broken in ways that cannot be fixed without breaking the web. As the story goes, it was included in the original 10-day JavaScript engine hack and based on java.util.Date, which itself was deprecated in 1997 due to being a terrible API and replaced with a better one. The result has been for all of JavaScript's history, the built-in `Date` has remained very hard to work with directly.

Starting a few years ago, a proposal has been developing, to add a new globally available object to JavaScript, `Temporal`. Temporal is a robust and modern API for working with dates, times, and timestamps, and also makes it easy to do things that were hard or impossible with `Date`, like converting dates between time zones, adding and subtracting while accounting for daylight saving time, working with date-only or time-only data, and even handling dates in non-Gregorian calendars. Although Temporal has "just works" defaults, it also provides fine-grained opt-in control of overflows, interpreting ambiguous times, and other corner cases. For more on the history of the proposal, and why it's not possible to fix `Date` itself, read [Maggie Pint's two-part blog post "Fixing JavaScript Date"](https://maggiepint.com/2017/04/09/fixing-javascript-date-getting-started/).

For examples of the power of Temporal, check out the [cookbook](https://tc39.es/proposal-temporal/docs/cookbook.html). Many of these examples would be difficult to do with legacy `Date`, particularly the ones involving time zones. (We would have put an example in this post, but the code might soon become stale, for reasons which will hopefully become clear!)

This [proposal](https://github.com/tc39/proposal-temporal) is currently at Stage 2 in TC39's proposal process, and we[\[1\]](#fn1) are hoping to move it along to Stage 3 soon.[\[2\]](#fn2) We have been working on the feature set of `Temporal` and the API for a long time, and we believe it's full-featured and that the API is reasonable. You don't design good APIs solely on the drawing board, however, so it's time to put it to the test and let the JavaScript developer community try it out and see whether what we've come up with meets people's needs.

It is still early enough that we can make drastic changes to the API if we find we need to, based on the feedback that we get. So please, try it out and let us know!

## How to Try Temporal [#](#how-to-try-temporal)

If you just want to try Temporal out casually, with an interactive prompt, that's easy! Visit the [API documentation](https://tc39.es/proposal-temporal/docs/) in your browser. On any of the documentation or cookbook pages, you can [open your browser console](http://tinyurl.com/jscons) and Temporal will be already loaded, ready for you to try out the examples. Or you can try it out on [RunKit](https://npm.runkit.com/proposal-temporal).

Or, maybe you are interested in a bit more in-depth evaluation, like building a small test project using Temporal. We know this takes up people's valuable project time, but it's also the best way that we can get the most valuable feedback, so we'd really appreciate this! We have released a [polyfill](https://www.npmjs.com/package/proposal-temporal) for the Temporal API on npm. You can use it in your project with `npm install --save proposal-temporal`, and import it in your project with `const { Temporal } = require('proposal-temporal');`.

However, don't use the polyfill in production applications! The proposal is still at Stage 2, and the polyfill has an 0.x version, so that should make it clear that the API is subject to change, and we do intend to keep changing it when we get feedback from you!

## How to Give Feedback [#](#how-to-give-feedback)

We would _love_ to hear from you about your experiences with Temporal! Once you've tried it, we have a short [survey](https://forms.gle/iL9iZg7Y9LvH41Nv8) for you to fill out. If you feel comfortable doing so, please leave us your contact information, since we might want to ask some follow up questions.

Please also open an issue on our [issue tracker](https://github.com/tc39/proposal-temporal/issues) if you have some suggestion! We welcome suggestions whether or not you filled out the survey. You can also browse the feedback that's already been given in the issue tracker, and give it a thumbs-up if you agree or thumbs-down if you disagree.

Thanks for participating if you can! All the feedback that we receive now will help us make the right decisions as the proposal moves along to Stage 3 and Temporal eventually appears in your browser.

* * *

1.  "We" in this post means the [Temporal champions group](https://github.com/tc39/proposal-temporal#champions), a group of TC39 delegates and interested people. As you may guess from where this blog post is hosted, it includes members of Igalia's Compilers team, but this was written on behalf of the Temporal champions. [↩︎](#fnref1)
    
2.  Read the [TC39 process document](https://tc39.es/process-document/) for more information on what these stages mean. tl;dr: Stage 2 is the time to give feedback on the proposal that can still be incorporated even if it requires drastic changes. Stage 3 is when the proposal remains stable except for serious problems discovered during implementation in browsers. [↩︎](#fnref2)
    

*   Previous: [What we do at Igalia's Compiler Team](https://blogs.igalia.com/compilers/2020/06/05/what-we-do-at-igalias-compiler-team/)
*   Next: [Igalia's Compilers Team in 2020](https://blogs.igalia.com/compilers/2021/03/09/igalias-compilers-team-in-2020/)
