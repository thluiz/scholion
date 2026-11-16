---
url: "https://javascript.plainenglish.io/basic-javascript-patterns-events-b1795db01f26"
captured_at: "2026-11-16T17:52:27+00:00"
title: "Basic JavaScript Patterns — Events"
domain: "javascript-plainenglish-io"
---

Member-only story

Basic JavaScript Patterns — Events
John Au-Yeung
4 min read
·
May 16, 2020

JavaScript lets us do a lot of things. It’s sometimes too forgiving in its syntax.

The organize our code, we should use some basic design patterns. In the article, we’ll look at events, HTTP requests, and background tasks.

Events

Handling user events is also a problem for developers.

There were lots of inconsistencies in how we handle events.

Listening to events have to be done in a clean way.

We shouldn’t violate the separation of concerns.

For instance, we should write HTML that looks like the following:

<button id="clickme">click me</button>

We don’t want a clickme handler in our HTML markup.

This violates the separation of concerns and we would have problems when we have to change it later.

Instead, we should write:

const clickMe = document.querySelector('#clickme');
clickMe.onclick = () => {
//...
}

This makes our lives easier in the future since all the click handling code is in JavaScript.

There are a few things we’ve to do to handle evens.

We have to gain access to the event object.
