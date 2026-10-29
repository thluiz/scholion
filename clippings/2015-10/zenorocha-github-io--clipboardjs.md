---
url: "https://zenorocha.github.io/clipboard.js/"
captured_at: "2015-10-19T08:55:10-03:00"
title: "clipboard.js"
domain: "zenorocha-github-io"
---

# clipboard.js

## A modern approach to copy text to clipboard

## No Flash. No dependencies. Just 2kb

Copying text to the clipboard shouldn't be hard. It shouldn't require dozens of steps to configure or hundreds of KBs to load. But most of all, it shouldn't depend on Flash or any bloated framework.

That's why clipboard.js exists.

# Install

You can get it on npm.

```
npm install clipboard --save
```

Or bower, too.

```
bower install clipboard --save
```

If you're not into package management, just [download a ZIP](https://github.com/zenorocha/clipboard.js/archive/master.zip) file.

# Setup

First, include the script located on the `dist` folder.

```
<script ="dist/clipboard.min.js"></script>
```

Or load it from a CDN.

```
<script ="https://cdn.rawgit.com/zenorocha/clipboard.js/master/dist/clipboard.min.js"></script>
```

Now, you need to instantiate it using a DOM selector. This selector corresponds to the trigger element(s), for example `<button class="btn">`.

```
 Clipboard('.btn');
```

Internally, we need to fetch all elements that matches with your selector and attach event listeners for each one. But guess what? If you have hundreds of matches, this operation can consume a lot of memory.

For this reason we use [event delegation](https://stackoverflow.com/questions/1687296/what-is-dom-event-delegation) which replaces multiple event listeners with just a single listener. After all, [#perfmatters](https://twitter.com/hashtag/perfmatters).

# Usage

We're living a *declarative renaissance*, that's why we decided to take advantage of [HTML5 data attributes](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/Using_data_attributes) for better usability.

### Copy text from another element

A pretty common use case is to copy content from another element. You can do that by adding a `data-clipboard-target` attribute in your trigger element.

The value you include on this attribute needs to match another's element selector.

```
<!-- Target -->
<input ="foo" value="https://github.com/zenorocha/clipboard.js.git">

<!-- Trigger -->
<button class="btn" data-clipboard-target="#foo">
    < ="assets/clippy.svg" ="Copy to clipboard">
</button>
```

### Cut text from another element

Additionally, you can define a `data-clipboard-action` attribute to specify if you want to either `copy` or `cut` content.

If you omit this attribute, `copy` will be used by default.

```
<!-- Target -->
<textarea ="bar">Mussum ipsum cacilds...</textarea>

<!-- Trigger -->
<button class="btn" data-clipboard-action="cut" data-clipboard-target="#bar">
    Cut to clipboard
</button>
```

As you may expect, the `cut` action only works on `<input>` or `<textarea>` elements.

### Copy text from attribute

Truth is, you don't even need another element to copy its content from. You can just include a `data-clipboard-text` attribute in your trigger element.

```
<!-- Trigger -->
<button class="btn" data-clipboard-text="Just because you can doesn't mean you should — clipboard.js">
    Copy to clipboard
</button>
```

# Events

There are cases where you'd like to show some user feedback or capture what has been selected after a copy/cut operation.

That's why we fire custom events such as `success` and `error` for you to listen and implement your custom logic.

```
 clipboard =  Clipboard('.btn');

clipboard.on('success', function() {
    console.info('Action:', e.action);
    console.info('Text:', e.text);
    console.info('Trigger:', e.trigger);

    e.clearSelection();
});

clipboard.on('error', function() {
    console.error('Action:', e.action);
    console.error('Trigger:', e.trigger);
});
```

For a live demonstration, just open your console :)

# Advanced Usage

If you don't want to modify your HTML, there's a pretty handy imperative API for you to use. All you need to do is declare a function, do your thing, and return a value.

For instance, if you want to dynamically set a `target`, you'll need to return a Node.

```
 Clipboard('.btn', {
    target: function(trigger) {
        return trigger.nextElementSibling;
    }
});
```

If you want to dynamically set a `text`, you'll return a String.

```
 Clipboard('.btn', {
    text: function(trigger) {
        return trigger.getAttribute('aria-label');
    }
});
```

Also, with are working with single page apps, you may want to manage the lifecycle of the DOM more precisely. Here's how you clean up the events and objects that we create.

```
 clipboard =  Clipboard('.btn');
clipboard.destroy();
```

# Browser Support

This library relies on both [Selection](https://developer.mozilla.org/en-US/docs/Web/API/Selection) and [execCommand](https://developer.mozilla.org/en-US/docs/Web/API/Document/execCommand) APIs. The second one is supported in the following browsers.

Although copy/cut operations with [execCommand](https://developer.mozilla.org/en-US/docs/Web/API/Document/execCommand) aren't supported on Safari yet (including mobile), it gracefully degrades because [Selection](https://developer.mozilla.org/en-US/docs/Web/API/Selection) is supported.

That means you can show a tooltip saying `Copied!` when `success` event is called and `Press Ctrl+C to copy` when `error` event is called because the text is already selected.

For a live demonstration, open this site on Safari.

Made with by [Zeno Rocha](http://zenorocha.com/) under [MIT license](http://zenorocha.mit-license.org/)
