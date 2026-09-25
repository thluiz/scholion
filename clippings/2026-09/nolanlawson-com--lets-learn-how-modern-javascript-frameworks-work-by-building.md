---
url: "https://nolanlawson.com/2023/12/02/lets-learn-how-modern-javascript-frameworks-work-by-building-one/"
captured_at: "2026-09-25T18:24:52+01:00"
title: "Let’s learn how modern JavaScript frameworks work by building one"
domain: "nolanlawson-com"
---

![Hand-drawn looking JavaScript logo saying DIY JS](https://nolanlawson.com/wp-content/uploads/2023/12/js-diy.png?w=570&h=570)

In my day job, I work on a JavaScript framework ([LWC](https://lwc.dev/)). And although I’ve been working on it for almost three years, I still feel like a dilettante. When I read about what’s going on in the larger framework world, I often feel overwhelmed by all the things I don’t know.

One of the best ways to learn how something works, though, is to build it yourself. And plus, we gotta keep those [“days since last JavaScript framework”](https://dayssincelastjavascriptframework.com/) memes going. So let’s write our own modern JavaScript framework!

## What is a “modern JavaScript framework”?

React is a great framework, and I’m not here to dunk on it. But for the purposes of this post, “modern JavaScript framework” means “a framework from the post-React era” – i.e. [Lit](https://lit.dev/), [Solid](https://www.solidjs.com/), [Svelte](https://svelte.dev/), [Vue](https://vuejs.org/), etc.

React has dominated the frontend landscape for so long that every newer framework has grown up in its shadow. These frameworks were all heavily inspired by React, but they’ve evolved away from it in surprisingly similar ways. And although React itself has continued innovating, I find that the post-React frameworks are more similar to each other than to React nowadays.

To keep things simple, I’m also going to avoid talking about server-first frameworks like [Astro](https://astro.build/), [Marko](https://markojs.com/), and [Qwik](https://qwik.builder.io/docs/). These frameworks are excellent in their own way, but they come from a slightly different intellectual tradition compared to the client-focused frameworks. So for this post, let’s only talk about client-side rendering.

## What sets modern frameworks apart?

From my perspective, the post-React frameworks have all converged on the same foundational ideas:

1.  Using reactivity (e.g. [signals](https://dev.to/this-is-learning/the-evolution-of-signals-in-javascript-8ob)) for DOM updates.
2.  Using cloned templates for DOM rendering.
3.  Using modern web APIs like `<template>` and `Proxy`, which make all of the above easier.

Now to be clear, these frameworks differ a lot at the micro level, and in how they handle things like web components, compilation, and user-facing APIs. [Not all frameworks](https://github.com/sveltejs/svelte/issues/2626#issuecomment-489894747) even use `Proxy`s. But broadly speaking, most framework authors seem to agree on the above ideas, or they’re moving in that direction.

So for our own framework, let’s try to do the bare minimum to implement these ideas, starting with reactivity.

## Reactivity

It’s often said that [“React is not reactive”](https://dev.to/this-is-learning/how-react-isn-t-reactive-and-why-you-shouldn-t-care-152m). What this means is that React has a more pull-based rather than a push-based model. To grossly oversimplify things: in the worst case, React assumes that your entire virtual DOM tree needs to be rebuilt from scratch, and the only way to prevent these updates is to implement `React.memo` (or in the old days, `shouldComponentUpdate`).

Using a virtual DOM mitigates some of the cost of the “blow everything away and start from scratch” strategy, but it doesn’t fully solve it. And asking developers to write the correct memo code is a losing battle. (See [React Forget](https://react.dev/blog/2023/03/22/react-labs-what-we-have-been-working-on-march-2023) for an ongoing attempt to solve this.)

Instead, modern frameworks use a push-based reactive model. In this model, individual parts of the component tree subscribe to state updates and only update the DOM when the relevant state changes. This prioritizes a “performant by default” design in exchange for some upfront bookkeeping cost (especially in terms of memory) to keep track of which parts of the state are tied to which parts of the UI.

Note that this technique is not necessarily incompatible with the virtual DOM approach: tools like [Preact Signals](https://preactjs.com/guide/v10/signals/) and [Million](https://million.dev/) show that you can have a hybrid system. This is useful if your goal is to keep your existing virtual DOM framework (e.g. React) but to selectively apply the push-based model for more performance-sensitive scenarios.

For this post, I’m not going to rehash the details of signals themselves, or subtler topics like [fine-grained reactivity](https://dev.to/ryansolid/a-hands-on-introduction-to-fine-grained-reactivity-3ndf), but I am going to assume that we’ll use a reactive system.

## Cloning DOM trees

For a long time, the collective wisdom in JavaScript frameworks was that the fastest way to render the DOM is to create and mount each DOM node individually. In other words, you use APIs like `createElement`, `setAttribute`, and `textContent` to build the DOM piece-by-piece:

1

2

3

`const div = document.createElement(``'div'``)`

`div.setAttribute(``'class'``,` `'blue'``)`

`div.textContent =` `'Blue!'`

One alternative is to just shove a big ol’ HTML string into `innerHTML` and let the browser parse it for you:

1

2

3

4

`const container = document.createElement(``'div'``)`

`` container.innerHTML = ` ``

  `<div` `class``=``"blue"``>Blue!</div>`

`` ` ``

This naïve approach has a big downside: if there is any dynamic content in your HTML (for instance, `red` instead of `blue`), then you would need to parse HTML strings over and over again. Plus, you are blowing away the DOM with every update, which would reset state such as the `value` of `<input>`s.

At some point, though, folks figured out that parsing the HTML _once_ and then calling `cloneNode(true)` on the whole thing is pretty danged fast:

1

2

3

4

5

`const template = document.createElement(``'template'``)`

`` template.innerHTML = ` ``

  `<div` `class``=``"blue"``>Blue!</div>`

`` ` ``

`template.content.cloneNode(``true``)`

Here I’m using a [`<template>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/template) tag, which has the advantage of creating “inert” DOM. In other words, things like `<img>` or `<video autoplay>` don’t automatically start downloading anything.

How fast is this compared to manual DOM APIs? To demonstrate, here’s [a small benchmark](https://github.com/nolanlawson/template-clone-demo). [Tachometer](https://github.com/google/tachometer) reports that the cloning technique is about 50% faster in Chrome, 15% faster in Firefox, and 10% faster in Safari. (This will vary based on DOM size and number of iterations, but you get the gist.)

What’s interesting is that `<template>` is a new-ish browser API, not available in IE11, and originally designed for web components. Somewhat ironically, this technique is now used in a variety of JavaScript frameworks, regardless of whether they use web components or not.

There is one major challenge with this technique, which is how to efficiently update dynamic content without blowing away DOM state. We’ll cover this later when we build our toy framework.

## Modern JavaScript APIs

We’ve already encountered one new API that helps a lot, which is `<template>`. Another one that’s steadily gaining traction is [`Proxy`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Proxy), which can make building a reactivity system much simpler.

When we build our toy example, we’ll also use [tagged template literals](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Template_literals#tagged_templates) to create an API like this:

1

2

3

`` const dom = html` ``

  `<div>Hello ${ name }!</div>`

`` ` ``

Not all frameworks use this tool, but notable ones include Lit, [HyperHTML](https://viperhtml.js.org/hyper.html), and [ArrowJS](https://www.arrow-js.com/). Tagged template literals can make it much simpler to build ergonomic HTML templating APIs without needing a compiler.

## Step 1: building reactivity

Reactivity is the foundation upon which we'll build the rest of the framework. Reactivity will define how state is managed, and how the DOM updates when state changes.

Let's start with some ["dream code"](https://nobackend.org/2013/05/welcome-to-noBackend.html) to illustrate what we want:

1

2

3

4

5

6

7

8

`const state = {}`

`state.a = 1`

`state.b = 2`

`createEffect(() => {`

  `state.sum = state.a + state.b`

`})`

Basically, we want a “magic object” called `state`, with two props: `a` and `b`. And whenever those props change, we want to set `sum` to be the sum of the two.

Assuming we don’t know the props in advance (or have a compiler to determine them), a plain object will not suffice for this. So let’s use a `Proxy`, which can react whenever a new value is set:

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

`const state =` `new` `Proxy({}, {`

  `get(obj, prop) {`

    `onGet(prop)`

    `return` `obj[prop]`

  `},`

  `set(obj, prop, value) {`

    `obj[prop] = value`

    `onSet(prop, value)`

    `return` `true`

  `}`

`})`

Right now, our `Proxy` doesn’t do anything interesting, except give us some `onGet` and `onSet` hooks. So let’s make it flush updates after a microtask:

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

`let` `queued =` `false`

`function` `onSet(prop, value) {`

  `if` `(!queued) {`

    `queued =` `true`

    `queueMicrotask(() => {`

      `queued =` `false`

      `flush()`

    `})`

  `}`

`}`

Why flush updates? Mostly because we don’t want to run too many computations. If we update whenever both `a` and `b` change, then we’ll uselessly compute the `sum` twice. By coalescing the flush into a single microtask, we can be much more efficient.

Next, let’s make `flush` update the sum:

1

2

3

`function` `flush() {`

  `state.sum = state.a + state.b`

`}`

This is great, but it’s not yet our “dream code.” We’ll need to implement `createEffect` so that the `sum` is computed only when `a` and `b` change (and not when something else changes!).

To do this, let’s use an object to keep track of which effects need to be run for which props:

1

`const propsToEffects = {}`

Next comes the crucial part! We need to make sure that our effects can _subscribe_ to the right props. To do so, we’ll run the effect, note any `get` calls it makes, and create a mapping between the prop and the effect.

To break it down, remember our “dream code” is:

1

2

3

`createEffect(() => {`

  `state.sum = state.a + state.b`

`})`

When this function runs, it calls two getters: `state.a` and `state.b`. These getters should trigger the reactive system to notice that the function relies on the two props.

To make this happen, we’ll start with a simple global to keep track of what the “current” effect is:

1

`let` `currentEffect`

Then, the `createEffect` function will set this global before calling the function:

1

2

3

4

5

`function` `createEffect(effect) {`

  `currentEffect = effect`

  `effect()`

  `currentEffect = undefined`

`}`

The important thing here is that the effect is _immediately_ invoked, with the global `currentEffect` being set in advance. This is how we can track whatever getters it might be calling.

Now, we can implement the `onGet` in our `Proxy`, which will set up the mapping between the global `currentEffect` and the property:

1

2

3

4

5

`function` `onGet(prop) {`

  `const effects = propsToEffects[prop] ??`

      `(propsToEffects[prop] = [])`

  `effects.push(currentEffect)`

`}`

After this runs once, `propsToEffects` should look like this:

1

2

3

4

`{`

  `"a"``: [theEffect],`

  `"b"``: [theEffect]`

`}`

…where `theEffect` is the “sum” function we want to run.

Next, our `onSet` should add any effects that need to be run to a `dirtyEffects` array:

1

2

3

4

5

6

7

8

`const dirtyEffects = []`

`function` `onSet(prop, value) {`

  `if` `(propsToEffects[prop]) {`

    `dirtyEffects.push(...propsToEffects[prop])`

  `}`

`}`

At this point, we have all the pieces in place for `flush` to call all the `dirtyEffects`:

1

2

3

4

5

`function` `flush() {`

  `while` `(dirtyEffects.length) {`

    `dirtyEffects.shift()()`

  `}`

`}`

Putting it all together, we now have a fully functional reactivity system! You can play around with it yourself and try setting `state.a` and `state.b` in the DevTools console – the `state.sum` will update whenever either one changes.

Now, there are plenty of advanced cases that we’re _not_ covering here:

1.  Using `try`/`catch` in case an effect throws an error
2.  Avoiding running the same effect twice
3.  Preventing infinite cycles
4.  Subscribing effects to new props on subsequent runs (e.g. if certain getters are only called in an `if` block)

However, this is more than enough for our toy example. Let’s move on to DOM rendering.

## Step 2: DOM rendering

We now have a functional reactivity system, but it’s essentially “headless.” It can track changes and compute effects, but that’s about it.

At some point, though, our JavaScript framework needs to actually render some DOM to the screen. (That’s kind of the whole point.)

For this section, let’s forget about reactivity for a moment and imagine we’re just trying to build a function that can 1) build a DOM tree, and 2) update it efficiently.

Once again, let’s start off with some dream code:

1

2

3

4

5

`function` `render(state) {`

  `return` `` html` ``

    `<div` `class``=``"${state.color}"``>${state.text}</div>`

  `` ` ``

`}`

As I mentioned, I’m using tagged template literals, ala Lit, because I found them to be a nice way to write HTML templates without needing a compiler. (We’ll see in a moment why we might actually _want_ a compiler instead.)

We’re re-using our `state` object from before, this time with a `color` and `text` property. Maybe the state is something like:

1

2

`state.color = 'blue'`

`state.text = 'Blue!'`

When we pass this `state` into `render`, it should return the DOM tree with the state applied:

1

`<``div` `class``=``"blue"``>Blue!</``div``>`

Before we go any further, though, we need a quick primer on tagged template literals. Our `html` tag is just a function that receives two arguments: the `tokens` (array of static HTML strings) and `expressions` (the evaluated dynamic expressions):

1

2

`function` `html(tokens, ...expressions) {`

`}`

In this case, the `tokens` are (whitespace removed):

1

2

3

4

5

`[`

  `"<div class=\""``,`

  `"\">"``,`

  `"</div>"`

`]`

And the `expressions` are:

1

2

3

4

`[`

  `"blue"``,`

  `"Blue!"`

`]`

The `tokens` array will always be exactly 1 longer than the `expressions` array, so we can trivially zip them up together:

1

2

`const allTokens = tokens`

    `.map((token, i) => (expressions[i - 1] ??` `''``) + token)`

This will give us an array of strings:

1

2

3

4

5

`[`

  `"<div class=\""``,`

  `"blue\">"``,`

  `"Blue!</div>"`

`]`

We can join these strings together to make our HTML:

1

`const htmlString = allTokens.join(``''``)`

And then we can use `innerHTML` to parse it into a `<template>`:

1

2

3

4

5

`function` `parseTemplate(htmlString) {`

  `const template = document.createElement(``'template'``)`

  `template.innerHTML = htmlString`

  `return` `template`

`}`

This template contains our inert DOM (technically a [`DocumentFragment`](https://developer.mozilla.org/en-US/docs/Web/API/DocumentFragment)), which we can clone at will:

1

`const cloned = template.content.cloneNode(``true``)`

Of course, parsing the full HTML whenever the `html` function is called would not be great for performance. Luckily, tagged template literals have a built-in feature that will help out a lot here.

For every unique usage of a tagged template literal, the `tokens` array is [always the same](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Template_literals#tagged_templates) whenever the function is called – in fact, it’s the exact same object!

For example, consider this case:

1

2

3

`function` `sayHello(name) {`

  `return` `` html`<div>Hello ${name}</div>` ``

`}`

Whenever `sayHello` is called, the `tokens` array will always be identical:

1

2

3

4

`[`

  `"<div>Hello "``,`

  `"</div>"`

`]`

The only time `tokens` will be different is for completely different locations of the tagged template:

1

2

`` html`<div></div>` ``

`` html`<span></span>` ``

We can use this to our advantage by using a `WeakMap` to keep a mapping of the `tokens` array to the resulting `template`:

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

`const tokensToTemplate =` `new` `WeakMap()`

`function` `html(tokens, ...expressions) {`

  `let` `template = tokensToTemplate.get(tokens)`

  `if` `(!template) {`

    `template = parseTemplate(htmlString)`

    `tokensToTemplate.set(tokens, template)`

  `}`

  `return` `template`

`}`

This is kind of a mind-blowing concept, but the uniqueness of the `tokens` array essentially means that we can ensure that each call to `` html`...` `` only parses the HTML once.

Next, we just need a way to update the cloned DOM node with the `expressions` array (which is likely to be different every time, unlike `tokens`).

To keep things simple, let’s just replace the `expressions` array with a placeholder for each index:

1

``const stubs = expressions.map((_, i) => `__stub-${i}__`)``

If we zip this up like before, it will create this HTML:

1

2

3

`<``div` `class``=``"__stub-0__"``>`

  `__stub-1__`

`</``div``>`

We can write a simple string replacement function to replace the stubs:

1

2

3

4

5

`function` `replaceStubs (string) {`

  `return` `string.replaceAll(/__stub-(\d+)__/g, (_, i) => (`

    `expressions[i]`

  `))`

`}`

And now whenever the `html` function is called, we can clone the template and update the placeholders:

1

2

3

4

5

`const element = cloned.firstElementChild`

`for` `(const { name, value } of element.attributes) {`

  `element.setAttribute(name, replaceStubs(value))`

`}`

`element.textContent = replaceStubs(element.textContent)`

Now, this is still not terribly efficient – notably, we are updating `textContent` and attributes that don’t necessarily need to be updated. But for our toy framework, this is good enough.

We can test it out by rendering with different `state`:

1

2

`document.body.appendChild(render({ color:` `'blue'``, text:` `'Blue!'` `}))`

`document.body.appendChild(render({ color:` `'red'``, text:` `'Red!'` `}))`

This works!

## Step 3: combining reactivity and DOM rendering

Since we already have a `createEffect` from the rendering system above, we can now combine the two to update the DOM based on the state:

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

`const container = document.getElementById(``'container'``)`

`createEffect(() => {`

  `const dom = render(state)`

  `if` `(container.firstElementChild) {`

    `container.firstElementChild.replaceWith(dom)`

  `}` `else` `{`

    `container.appendChild(dom)`

  `}`

`})`

This actually works! We can combine this with the “sum” example from the reactivity section by merely creating another effect to set the `text`:

1

2

3

`createEffect(() => {`

  `` state.text = `Sum is: ${state.sum}` ``

`})`

This renders “Sum is 3”:

You can play around with this toy example. If you set `state.a = 5`, then the text will automatically update to say “Sum is 7.”

## Next steps

There are lots of improvements we could make to this system, especially the DOM rendering bit.

Most notably, we are missing a way to update content for elements inside a deep DOM tree, e.g.:

1

2

3

`<``div` `class``=``"${color}"``>`

  `<``span``>${text}</``span``>`

`</``div``>`

For this, we would need a way to uniquely identify every element inside of the template. There are lots of ways to do this:

1.  Lit, when parsing HTML, uses a system of [regexes and character matching](https://github.com/lit/lit/blob/1af7991c27456c7e6073a3ee6f18f102c2adc026/packages/lit-html/src/lit-html.ts#L779-L857) to determine whether a placeholder is within an attribute or text content, plus the index of the target element (in depth-first [`TreeWalker`](https://developer.mozilla.org/en-US/docs/Web/API/TreeWalker) order).
2.  Frameworks like Svelte and Solid have the luxury of parsing the entire HTML template during compilation, which provides the same information. They also generate code that calls `firstChild` and `nextSibling` to traverse the DOM to find the element to update.

Whether we decided to do Lit-style client-side parsing or Svelte/Solid-style compile-time parsing, what we want is some kind of mapping like this:

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

`[`

  `{`

    `elementIndex: 0,`

    `attributeName:` `'class'``,`

    `stubIndex: 0`

  `},`

  `{`

    `elementIndex: 1`

    `textContent:` `true``,`

    `stubIndex: 1`

  `}`

`]`

These bindings would tell us exactly which elements need to be updated, which attribute (or `textContent`) needs to be set, and where to find the `expression` to replace the stub.

The next step would be to avoid cloning the template every time, and to just directly update the DOM based on the `expressions`. In other words, we not only want to parse once – we want to only clone and set up the bindings once. This would reduce each subsequent update to the bare minimum of `setAttribute` and `textContent` calls.

Another interesting pattern to implement would be iterations (or repeaters), which come with their own set of challenges, like reconciling lists between updates and handling “keys” for efficient replacement.

I’m tired, though, and this blog post has gone on long enough. So I leave the rest as an exercise to the reader!

## Conclusion

So there you have it. In the span of one (lengthy) blog post, we’ve implemented our very own JavaScript framework. Feel free to use this as the foundation for your brand-new JavaScript framework, to release to the world and enrage the Hacker News crowd.

Personally I found this project very educational, which is partly why I did it in the first place. I was also looking to replace the current framework for [my emoji picker component](https://github.com/nolanlawson/emoji-picker-element/) with a smaller, more custom-built solution. In the process, I managed to write [a tiny framework](https://github.com/nolanlawson/emoji-picker-element/pull/381) that passes all the existing tests and is ~6kB smaller than the current implementation, which I’m pretty proud of.

In the future, I think it would be neat if browser APIs were full-featured enough to make it even easier to build a custom framework. For example, the [DOM Part API proposal](https://github.com/WICG/webcomponents/blob/gh-pages/proposals/DOM-Parts.md) would take out a lot of the drudgery of the DOM parsing-and-replacement system we built above, while also opening the door to potential browser performance optimizations. I could also imagine (with some wild gesticulation) that an extension to `Proxy` could make it easier to build a full reactivity system without worrying about details like flushing, batching, or cycle detection.

If all those things were in place, then you could imagine effectively having a “Lit in the browser,” or at least a way to quickly build your own “Lit in the browser.” In the meantime, I hope that this small exercise helped to illustrate some of the things framework authors think about, and some of the machinery under the hood of your favorite JavaScript framework.

_Thanks to [Pierre-Marie Dartus](https://pm.dartus.fr/) for feedback on a draft of this post._

## Footnotes

_[1.](#footnote-1) Now that we’ve built the framework, you can see why the content passed to `innerHTML` can be considered trusted. All HTML tokens either come from tagged template literals (in which case they’re fully static and authored by the developer) or are placeholders (which are also written by the developer). User content is only set using `setAttribute` or `textContent`, which means that no HTML sanitization is required to avoid [XSS attacks](https://developer.mozilla.org/en-US/docs/Glossary/Cross-site_scripting). Although you should probably just use [CSP](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Security-Policy) anyway!_
