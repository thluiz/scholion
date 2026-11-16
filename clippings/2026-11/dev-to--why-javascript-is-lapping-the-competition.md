---
url: "https://dev.to/bytebodger/why-javascript-is-lapping-the-competition-4jic"
captured_at: "2026-11-16T01:16:58+00:00"
title: "Why JavaScript Is Lapping The Competition"
domain: "dev-to"
---

If you've been around as long as I have, you've probably noticed something remarkable about JavaScript (as compared to other languages). It's evolving at a _breakneck_ pace.

In general, this is a very _good_ thing (although it can make it quite challenging to keep your skills current). And if you're part of the "new generation" of coders - many of whom _only_ code in JavaScript - this might not even strike you as extraordinary. But as someone who's watched numerous languages evolve over the better part of three decades, let me assure you that, in this category, JavaScript is in a class of its own.

## [](#history)History

Most "modern" languages are maintained (in the worst-case scenario) by a single company. Or they're maintained (in the best-case scenario) by a vast, (virtually) nameless, open-source consortium.

Single-company stewardship isn't necessarily "bad". On one hand, it can allow the (small) braintrust of stewards to make quick-and-decisive corrections wherever the language is deemed to be "lacking". On the other hand, it can lead to stagnation if the company's braintrust doesn't favor Improvement X, even in the face of a development community that may be clamoring for Improvement X. It can also cause serious headaches if the parent company has objectives that clash with the broader community - or if they ever decide to abandon the project altogether.

Open-source projects are generally assumed to be "better". But even they have their downsides. Open-source projects are often plagued with "groupthink" and "analysis paralysis". If you think it's difficult to get a single room of people in your company to agree _on anything_, try getting a new feature proposal approved in a well-established open-source project.

You can submit a proposal saying that, "Bugs are bad." And you can almost be assured that _someone_ in the open-source community (probably, a well-established and respected _senior_ voice in the community) will chime in and say, "Ummm... No, they're not. And we definitely don't need a `removeBugs()` function in the core language."

## [](#javascripts-accidental-solution)JavaScript's Accidental Solution

If you're part of the latest-generation of JavaScript devs, you can be forgiven if you think that the language has _always_ evolved at its current pace. After all, the 2010s have seen an impressive array of new features and syntactic shortcuts added to the language. But let me assure you, it hasn't always been so.

The early days of JavaScript were strikingly similar to other trying-to-get-a-foothold languages. The ECMAScript committee had good intentions - but change was _slowwwww_. (Like it is for nearly any decision-by-large-committee process.)

If you don't believe me, just look at what happened (or... _didn't_ happen) with the ECMAScript standard for nearly 10 years, starting in the early 00s. We went many years without having any substantive improvements to the language. And for most of those years, JavaScript was much more of a "toy" than a serious programming language.

This was, perhaps, best illustrated by TypeScript. TypeScript wasn't _supposed to be_ a separate "language". It was _supposed to be_ a major enhancement to _core JavaScript_ - an enhancement that was heralded by none other than: Microsoft.

But through a series of last-minute backtracking decisions that would require _multiple_ blog posts to explain, MS's TypeScript modifications ended up being rejected. This eventually led to MS releasing TypeScript as its own, separate, open-source project. It also led to _years_ of stagnation in JavaScript.

We might still be wallowing in that general malaise if it weren't for the introduction of several key technologies. I'm talking about:

1.  Node.JS
2.  Node Package Manager (NPM)
3.  Babel

\[**NOTE**: If you're part of the adoring _Yarn crowd_, this isn't meant to sidestep you in any way. Yarn's wonderful. It's great. But I firmly believe that, with respect to the evolution that I'm trying to outline in this article, Node/NPM/Babel were the "sparks" that drove this initial advancement.\]

## [](#sidestepping-committees)Sidestepping Committees

There's nothing "magical" about JavaScript. Like any other language, it has its strength (and its flaws). And like any other language, if a broad internet consortium needs to reach _consensus_ about the language's newest features, we could well be waiting a decade-or-more for such improvements.

But a funny thing happened on the way to the endless open-source release-candidate debates. Node spurred a dynamic package model called _NPM_. (Which has had its own share of growing pains - but that's for another article...) And NPM spurred a fantastical, automagical package called _Babel_.

For the first time, Babel gave the burgeoning JavaScript community an incredible ability to evolve the language _on their own_. Babel created a vast, real-world "proving ground" for advancements in the JavaScript language. If you look at the major advancements in the ECMAScript spec over the last 10+ years, you'd be hard-pressed to find any improvements that weren't first encapsulated _in NPM packages_, that were then transpiled to backward-compatible JavaScript _in Babel_, before they were eventually absorbed into the core language itself.

To put this another way, Babel freed JS devs from constantly having to code for the "lowest common denominator". If there was an exciting new (proposed) language construct that wasn't recognized by older browsers - but Babel could transpile it down to older-browser-compliant code, then you were free to code away with the cool new feature. And if your users were using ancient browsers, that was OK - because Babel would basically take care of the messy new-to-old translations.

## [](#innovations-are-rarely-inventions)"Innovations" Are Rarely... _Inventions_

Maybe you're thinking that an NPM package is not an innovation _in the language itself_. And many times, I would agree with you. But when something becomes sufficiently-useful to a huge portion of the programming ecosystem, it can, in fact, become an innovation in the underlying language.

Let's imagine that, in your JavaScript applications, you repeatedly have the need to `makeToast()`. Of course, JavaScript has no _native_ `makeToast()` functionality - so you've coded up some grand, extensive, convoluted utility function that will allow you to `makeToast()` right in the middle of any application where you feel the need to, well, you know... make toast.

After a while, you find yourself copying-and-pasting this amazing utility into _all_ of your applications. Eventually, you feel a bit of developer guilt over this repeated copying-and-pasting, so you encapsulate your awesome `makeToast()` functionality into an NPM package. The NPM package allows you to do this:  

```
import toast from 'make-toast';

const noToastHere = 'plain ol bread';
const itsToasted = toast.make(noToastHere);
```

Enter fullscreen mode Exit fullscreen mode

There's a good chance that your incredible `toast.make()` function utilizes a ton of _non-ECMA-standard_ language constructs. But that's OK. Because all of your _non-ECMA-standard_ language constructs are just a pile of syntactic sugar for things that you could always do in JavaScript - but with a lot more hellacious-looking code. And when you run your revolutionary new `toast.make()` function through Babel, it transpiles it back down into that old, ugly, IE7-compliant JavaScript that you never wanna have to type out manually.

You see, there's a good chance that your amazing `toast.make()` functionality isn't doing anything that you couldn't always, theoretically, do with old-skool JavaScript. `toast.make()` presumably just gives you a faster, sleeker, more-efficient way to make toast, rather than relying on every dev team, in every codebase, having to manually figure out how to make their own toast from scratch.

To be clear, such "advancements" aren't just about semantics. They absolutely are _advancements_. If we always had to do this:  

```
export default function makeToast() {
  // here are my 200 lines of custom, painfully crafted, 
  // cross-browser-compliant code that allows me to makeToast()
}
```

Enter fullscreen mode Exit fullscreen mode

And now we can just do this:  

```
import toast from 'make-toast';

const noToastHere = 'plain ol bread';
const itsToasted = toast.make(noToastHere);
```

Enter fullscreen mode Exit fullscreen mode

And, if many thousands of developers all around the world find themselves repeatedly having to either A) import your `make-toast` package, or B) figure out a way to manually craft the functionality from scratch, then your amazing `toast.make()` feature _is_ a potentially-significant advancement in the language. More important, if your `toast.make()` feature becomes so ubiquitous that it's more-or-less "standard" in modern codebases, there's a chance that the ECMAScript committee might actually decide to promote it to the level of being a _language construct_.

(Granted, they may not choose to implement it in the exact same way that you did in your NPM package. But the point is that they might eventually look at what's happening in the broader JS community, realize that vast numbers of codebases now see a need to make toast, and find a way to incorporate this as a base feature in the core language itself.)

## [](#lodash-amp-underscore)Lodash & Underscore

To see this in action, look at many of the core functions that are available in the Underscore or Lodash libraries. When those libraries first rose to prominence, they provided a ton of functionality that you just couldn't do in JavaScript without manually coding out all the functions yourself.

Nowadays, those libraries still offer _some_ useful functionality that simply doesn't exist in core JavaScript. But many of their features have actually been adopted _into the core language_. A good example of this is the `Array.prototype` functions.

One of my pet peeves is when I see a dev import Lodash _so they can loop through an array_. When Lodash was first introduced, there was no one-liner available in JavaScript that did that. Now... we have `Array.prototype` functions.

But that's not a knock on Lodash. Lodash, Underscore, and other similar libraries did their jobs so well, and become so ubiquitous, that some of their core features ended up being adopted into the language itself. And this all happened in a relatively short period of time (by the standard of typical language evolution).

## [](#innovation-vs-stagnation)Innovation vs Stagnation

If you think that JavaScript's recent barrage of advancements is "normal" for a programming language, let me assure you: _It's not._ I could probably come up with 50 sad examples of language stagnation, but let me give you one very-specific scenario where one language (JavaScript) shines and another (Java) has crawled into a corner to hide.

In JavaScript, I can now do this:  

```
import SlidingSwitch from '@material-ui/core/Switch';
import RouterSwitch from 'react-router-dom/Switch';
import CustomSwitch from './common/form-elements/Switch';

export default function Foo() {
  return (
    <>
      <RouterSwitch>
        <Route path={'/path1'} component={Path1Component}/>
        <Route path={'/path2'} component={Path2Component}/>
      </RouterSwitch> 
      <div>Here is my SlidingSwitch <SlidingSwitch/></div>
      <div>Here is my CustomSwitch <CustomSwitch/></div>
    </>
  );
}
```

Enter fullscreen mode Exit fullscreen mode

There's nothing too rocket-sciencey going on here. I'm importing three different components into my code. It just so happens that all three of them were originally written _with the same name_. But that's OK. JavaScript gives us an easy way to deal with the naming collisions by aliasing them at the point where they're imported.

This doesn't make JavaScript unique or special. Other languages have import aliasing features. But it's worthwhile to note that, a decade-or-more ago, _you couldn't do this (natively) in JavaScript_.

So how do we handle such naming collisions in Java??? It would look something like this:  

```
import material.ui.core.Switch;
import react.router.dom.Switch;
import com.companydomain.common.utils.Switch;

public class MyClass {
  material.ui.core.Switch slidingSwitch = new material.ui.core.Switch;
  react.router.dom.Switch routerSwitch = new react.router.dom.Switch;
  com.companydomain.common.utils.Switch customSwitch = new com.companydomain.common.utils.Switch;
}
```

Enter fullscreen mode Exit fullscreen mode

If that looks like a vomiting of word soup, that's because... _it is_. Since _you can't alias imports in Java_, the only way to deal with the issue is to handle each different type of `Switch` by using its fully-qualified name.

To be fair, _every_ language has quirks and, at times, some annoying little limitations. The point of this post is: When the language runs into limitations, how are those limitations resolved??

Five years ago _there were no_ imports in JavaScript. But now we have imports, with import aliasing thrown in as a bonus.

Java's had import capabilities since it was introduced. But it's _never_ had import aliasing. Is that because no one _wants_ import aliasing in Java? Nope. Import aliasing has been proposed as a new feature numerous times over the last _twenty+ years_. Every single time, it's been shot down - usually by a single, senior member of the Java open-source committee who just looks at the proposal and says, "Ummm... No. You don't need that. DENIED."

This is where Node/NPM/Babel is so critical in vaulting JavaScript past other languages. In Java, if you really want to have import aliasing, this is what that process looks like:

1.  Submit a JDK Enhancement Proposal (JEP).
2.  Have your JEP summarily dismissed with a one-line rejection like, "You don't need that."
3.  Just accept that the language doesn't have your desired feature and trudge along accordingly.
4.  Maybe, a few years later, submit a new JEP (and probably have it denied again).

This is the way it worked in JavaScript:

1.  No one had to sit around and wait for imports or import aliasing to be added to JavaScript by a committee. They went out and made their own packages - like, `RequireJS`.
2.  As it became clear that third-party import solutions were becoming ubiquitous, the ECMAScript committee began working on a formal spec.
3.  Even if the ECMAScript committee had ignored imports altogether, or had denied import aliasing as a feature, anyone who wanted it could continue to use the third-party packages such as `RequireJS` - so no one was ever beholden to the whims of a stodgy old committee.

## [](#agility-by-accident)Agility... By Accident

First it bears mentioning that JavaScript's NPM/Babel ecosystem is not a magic cure-all for the administrative hurdles inherent in upgrading an entire programming language. With these tools, we can do an amazing "end-around" to get non-standard functionality that would take years - or _decades_ - to get approved through regular channels. But it can still only provide features that could already be done, in some longer and more-manual form, through the language itself.

If you want JavaScript to to do something that it simply _cannot do_ today, you still have to go through the ECMAScript committee. But for everything else, NPM/Babel provide a dynamic playground in which proposed features can be tested in live apps. And the download/installation of those features serves as a de facto _vote_ in favor of those approaches.

I don't pretend for an instant that this state-of-affairs was a conscious _strategy_ devised by anyone involved in the planning process for JavaScript. In fact, JavaScript's early history shows that it's just as susceptible to "analysis paralysis" as any other language. But the Babel/NPM revolution has allowed for the ecosystem of devs to put natural pressure on the planning committees by allowing us to install-and-run experimental packages without the fear that they won't compile on our users' systems (i.e., browsers). This, in turn, has sparked rapid evolution from a sleepy little language, in the early part of the the century, to a full-bore programming juggernaut today.

Of course, this doesn't make JavaScript any "better" than Java (or any other language). There are certain virtues to waiting _a quarter century_ (or more) for something as simple and as basic as import aliasing. Waiting builds character. Waiting helps you appreciate life's more refined pleasures - like, _Tiger King_, or WWE wrestling. If Zen Buddhists had created software development, they would have most certainly included vast amounts of waiting. And multiple layers of petty denials.

I'm pretty sure that if I can just live to be 100, I'll probably see the day when Java finally implements import aliasing. And ohhhhh man! Will that day be _grand_!
