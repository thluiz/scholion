---
url: "https://dev.to/moruno21/99-of-frontend-devs-dont-use-this-1g44?context=digest"
captured_at: "2025-07-17T13:22:43+01:00"
title: "99% of frontend devs don't use this"
domain: "dev.to"
---

# 99% of frontend devs don't use this - DEV Community

> ## Excerpt
> In the React world, most developers don't think twice before using closures in their component render...

---
In the React world, most developers don't think twice before using **closures** in their component render methods, especially when mapping over lists.

But what if I told you there's an underutilized, yet powerful alternative that can help with performance, readability, and even better integration with tools?

Let's talk about **HTML data-\* attributes**: a feature that's rarely used by frontend developers, but deserves a second look.

## ❓ What are data-\* Attributes?

HTML's `data-*` attributes allow you to **embed custom data inside DOM elements**. In plain HTML:

```
<div data-user-id="123" data-role="admin">John</div>
```

In **React**, you can use them the same way:

```
<div data-user-id={user.id} data-role={user.role}>
  {user.name}
</div>
```

They are accessible in event handlers via the dataset object:

```
e.currentTarget.dataset.userId;
```

## 🧠 The Common Pattern: Closures in .map()

Let's say you're rendering a list of items:

```
{items.map((item) => (
  <button key={item.id} onClick={() => handleClick(item.id)}>
    {item.name}
  </button>
))}
```

This works fine. It's readable and easy to write.

But behind the scenes, **you're creating a new function for each item on every render**: a closure that captures `item.id`.

In many apps, this has no practical impact. However...

## ⚠️ The Downsides of Closures

While closures are a fundamental part of JavaScript and React, using them inside `.map()` can have drawbacks:

### 1. Unnecessary Re-Renders

If you're using `React.memo`, `React.useCallback`, or virtualized lists (like [react-window](https://github.com/bvaughn/react-window)), **new function references can cause unwanted re-renders**. Since the function is recreated every time, memoization doesn't help.

### 2. Harder to Optimize

Imagine you're building a highly interactive list that renders hundreds of items. Minimizing re-renders becomes important, and **inline closures can work against that**.

## ✅ The Alternative: `data-*`

Instead of creating a closure for each item, attach metadata directly to the DOM using `data-*`:

```
function handleClick(e) {
  const id = e.currentTarget.dataset.id;
  console.log("Clicked item:", id);
}

{items.map((item) => (
  <button key={item.id} data-id={item.id} onClick={handleClick}>
    {item.name}
  </button>
))}
```

-   **Single function reference** → plays nicely with `React.memo` or `React.useCallback`
-   **Improved performance** for large lists or re-render-sensitive components

## 🤔 So Why Isn't Everyone Doing This?

Because closures are easy, intuitive, and performant enough for most apps. `data-*` feels a bit "old-school," and it's rarely mentioned in modern React/Frontend tutorials.

But in situations where performance or memoization matters, **this approach can be a hidden gem**.

## ✨ In Summary

While `data-*` attributes aren't a common tool in a React developer's toolbox, they offer real advantages in specific scenarios:

-   **Reduce unnecessary function creations**
-   **Improve memoization and rendering performance**
-   **Enable simpler and cleaner event handling**

They're not a replacement for closures, but they're a great alternative when performance or architecture calls for it.

Have you ever used `data-*` attributes like this? Or do you usually stick with closures? **I'd love to hear your thoughts and experiences**!

I hope you found this post interesting. Let me know what you think in the comments 👇
