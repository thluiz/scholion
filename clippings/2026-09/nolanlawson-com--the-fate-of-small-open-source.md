---
url: "https://nolanlawson.com/2025/11/16/the-fate-of-small-open-source/?utm_source=tldrnewsletter"
captured_at: "2026-09-25T18:25:20+01:00"
title: "The fate of “small” open source"
domain: "nolanlawson-com"
---

By far the most popular npm package I’ve ever written is [`blob-util`](https://www.npmjs.com/package/blob-util), which is ~10 years old and still gets 5+ million weekly downloads.

It’s a small collection of utilities for working with [`Blob`s](https://developer.mozilla.org/en-US/docs/Web/API/Blob) in JavaScript. I wrote it because I found that PouchDB users were endlessly confused about how to work with `Blob`s and how to convert them to strings, `ArrayBuffer`s, etc.

Given that [some 80% of developers](https://survey.stackoverflow.co/2025/ai#sentiment-and-usage) are now using AI in their regular work, `blob-util` is almost certainly the kind of thing that most developers would just happily have an LLM generate for them. Sure, you _could_ use `blob-util`, but then you’d be taking on an extra dependency, with unknown performance, maintenance, and supply-chain risks.

And sure enough, Claude will happily spit out whatever `Blob` utilities you need when prompted:

_\> Write me a utility function in TypeScript to convert a Blob to an ArrayBuffer. It should return a Promise._

1

2

3

4

5

6

7

8

9

10

11

12

13

14

15

16

17

18

19

`function` `blobToArrayBuffer(blob: Blob): Promise<ArrayBuffer> {`

  `return` `new` `Promise((resolve, reject) => {`

    `const reader =` `new` `FileReader();`

    `reader.onload = () => {`

      `if` `(reader.result` `instanceof` `ArrayBuffer) {`

        `resolve(reader.result);`

      `}` `else` `{`

        `reject(``new` `Error(``'Failed to read Blob as ArrayBuffer'``));`

      `}`

    `};`

    `reader.onerror = () => {`

      `reject(reader.error);`

    `};`

    `reader.readAsArrayBuffer(blob);`

  `});`

`}`

Claude’s version is pretty close to [the `blob-util` version](https://github.com/nolanlawson/blob-util/blob/99c06472d18329eda1421286692bd875d76d5c9c/src/blob-util.ts#L384-L394) (unsurprising, since it was probably trained on it!). Although it’s much more verbose, unnecessarily checking if `readAsArrayBuffer` actually gives you an `ArrayBuffer` (although this does make TypeScript happy). To be fair, it also improves on my implementation by directly `reject`ing with an error rather than the more awkward `onerror` event.

I suppose some people would see this as progress: fewer dependencies, more robust code (even if it’s a bit more verbose), quicker turnaround time than the old “search npm, find a package, read the docs, install it” approach.

I don’t have any excessive pride in this library, and I don’t particularly care if the download numbers go up or down. But I do think something is lost with the AI approach. When I wrote `blob-util`, I took a teacher’s mentality: the README has [a cutesy and whimsical tutorial](https://www.npmjs.com/package/blob-util#tutorial) featuring Kirby, in all his blobby glory. (I had a thing for putting Nintendo characters in all my stuff at the time.)

The goal wasn’t just to give you a utility to solve your problem (although it does that) – the goal was also to _teach_ people how to use JavaScript effectively, so that you’d have an understanding of how to solve other problems in the future.

I don’t know which direction we’re going in with AI (well, ~80% of us; to the remaining holdouts, I salute you and wish you godspeed!), but I do think it’s a future where we prize instant answers over teaching and understanding. There’s less reason to use something like `blob-util`, which means there’s less reason to write it in the first place, and therefore less reason to educate people about the problem space.

Even now there’s a movement toward putting documentation in an [`llms.txt`](https://llmstxt.org/) file, so you can just point an agent at it and save your brain cells the effort of deciphering English prose. (Is this even documentation anymore? What _is_ documentation?)

## Conclusion

I still believe in open source, and I’m still doing it (in fits and starts). But one thing has become clear to me: the era of small, low-value libraries like `blob-util` is over. They were already on their way out thanks to Node.js and the browser taking on more and more of their functionality (see `node:glob`, `structuredClone`, etc.), but LLMs are the final nail in the coffin.

This does mean that there’s less opportunity to use these libraries as a springboard for user education (Underscore.js [also had this philosophy](https://underscorejs.org/docs/underscore-esm.html)), but maybe that’s okay. If there’s no need to find a library to, say, [group the items in an array](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/groupBy), then maybe learning about the mechanics of such libraries is unnecessary. Many software developers will argue that asking a candidate to reverse a binary tree is pointless, since it never comes up in the day-to-day job, so maybe the same can be said for utility libraries.

I’m still trying to figure out what _kinds_ of open source are worth writing in this new era (hint: ones that an LLM can’t just spit out on command), and where education is the most lacking. My current thinking is that the most value is in bigger projects, more inventive projects, or in more niche topics not covered in an LLM’s training data. For example, I look back on my work on [`fuite`](https://github.com/nolanlawson/fuite) and various [memory-leak-hunting blog posts](https://nolanlawson.com/2022/01/05/memory-leaks-the-forgotten-side-of-web-performance/), and I’m pretty satisfied that an LLM couldn’t reproduce this, because it requires novel research and creative techniques. (Although who knows: maybe someday an agent will be able to just bang its head against Chrome heap snapshots until it finds the leak. I’ll believe it when I see it.)

There’s been a lot of hand-wringing lately about where open source fits in in a world of LLMs, but I still see people pushing the boundaries. For example, a lot of naysayers think there’s no point in writing a new JavaScript framework, since LLMs are so heavily trained on React, but then there goes the indefatigable [Dominic Gannaway](https://github.com/trueadm) writing [Ripple.js](https://www.ripplejs.com/), yet another JavaScript framework (and with [some new ideas](https://podrocket.logrocket.com/ripple-js-dominic-gannaway-logrocket-podrocket), to boot!). This is the kind of thing I like to see: humans laughing in the face of the machine, going on with their human thing.

So if there’s a conclusion to this meandering blog post (excuse my squishy human brain; I didn’t use an LLM to write this), it’s just that: yes, LLMs have made some kinds of open source obsolete, but there’s still plenty of open source left to write. I’m excited to see what kinds of novel and unexpected things you all come up with.
