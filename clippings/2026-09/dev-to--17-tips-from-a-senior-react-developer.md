---
url: "https://dev.to/_ndeyefatoudiop/17-tips-from-a-senior-react-developer-2249?ref=dailydev"
captured_at: "2026-09-24T23:33:53+01:00"
title: "17 Tips from a Senior React Developer"
domain: "dev-to"
---

I've been writing React code as an engineer at Palantir for the past 5+ years.

These are the 17 tips I wish someone had shared with me when I was starting.

Ready? Let's dive in! 💪

[📚 Download my FREE 101 React Tips And Tricks Book for a head start.](https://www.frontendjoy.com/p/download-my-free-101-react-tips-tricks-book)

## [](#1-learn-javascript-before-react)1\. Learn JavaScript before React

When I first started, I jumped from writing functions and basic DOM manipulation to learning React.

As you can guess, it didn't go well 🤯.

This is a common mistake for junior developers: trying to learn React without a solid understanding of JavaScript.

It's a recipe for confusion:

*   You won't know what is React-specific and what is just JavaScript.
    
*   Debugging becomes a nightmare.
    

**What to do instead?**

*   Learn enough JavaScript to get comfortable (check out [JavaScript to Know for React)](https://kentcdodds.com/blog/javascript-to-know-for-react).
    
*   Then, dive into React.
    

[![Section Divider](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fisqsfnjxnhz9zz6gveau.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fisqsfnjxnhz9zz6gveau.png)

## [](#2-read-the-react-docs)2\. Read the React docs

You don't need money 💰, a coach, or a fancy course to learn React.

Head to the [official React website](https://react.dev/) and:

*   Follow the Quick Start [guide](https://react.dev/learn).
    
*   Read the [learning](https://react.dev/learn/describing-the-ui) chapters (even if they don't make sense initially, they'll click later).
    

[![Section Divider](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fisqsfnjxnhz9zz6gveau.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fisqsfnjxnhz9zz6gveau.png)

## [](#3-start-building-projects-early)3\. Start building projects early

Watching tutorials won't make you a React developer.

Spending $100, $200, or even $700 on courses won't either.

**What will?** Building projects.

It's the best way to:

*   Learn by making mistakes.
    
*   Discover gaps in your knowledge.
    
*   Pick up new patterns and tips.
    

Stuck for ideas? Try these resources 👇:

*   [**Frontend Mentor**](https://www.frontendmentor.io/): Projects for all skill levels.
    
*   [**Frontend Practice**](https://frontendpractice.com/): Recreate real websites.
    
*   [**Frontend Projects**](https://www.frontendprojects.io/): Varied project ideas.
    
*   [**JavaScript Mastery**](https://www.youtube.com/c/javascriptmastery): A YouTube channel with project-based tutorials.
    

[![Section Divider](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fisqsfnjxnhz9zz6gveau.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fisqsfnjxnhz9zz6gveau.png)

## [](#4-use-trusted-libraries)4\. Use trusted libraries

Not all packages are safe.

For example, in 2021, a popular NPM package, [ua-parser-js](https://www.npmjs.com/package/ua-parser-js), was hacked, spreading malware 📛.

To minimize risks:

*   Use libraries from trusted authors.
    
*   Check for good download volumes and regular updates.
    

[![Section Divider](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fisqsfnjxnhz9zz6gveau.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fisqsfnjxnhz9zz6gveau.png)

## [](#5-solve-problems-with-vanilla-js-when-possible)5\. Solve problems with Vanilla JS when possible

Previously, you needed libraries like [lodash](https://lodash.com/) for tasks like cloning, iteration, etc.

But modern JavaScript has improved a lot.

Now, you can achieve a lot with native methods.

So, don’t add a library if you don't have to.

**Why?**

Every library you add:

*   Increases your app's dependencies, making it more vulnerable to security issues.
    
*   Potentially adds to your bundle size, slowing down load times.
    
*   Increases your app’s build/compilation time
    
*   Creates maintenance overhead to keep dependencies updated.
    

Before reaching for a library, check if Vanilla JS can do the job. It often can 😉.

[![Section Divider](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fisqsfnjxnhz9zz6gveau.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fisqsfnjxnhz9zz6gveau.png)

## [](#6-optimize-bundle-size-and-lazy-load-as-much-as-possible)6\. Optimize bundle size and lazy load as much as possible

It starts slow.

You add one package here.

Then another there.

And then another.

Before you know it:

*   Users complain the app takes too long to load.
    
*   Developers complain the build process is painfully slow.
    

Why does this happen?

Packages and heavy components were added without considering their impact on bundle size 🤦‍♀️.

**How to fix it?**

*   **Lazy-load** as much as possible.
    
*   Set up checks to track bundle size increases (Pull Request actions work well for this).
    
*   Use [bundlephobia](https://bundlephobia.com/) to check package size before adding it to your project.
    

[![Section Divider](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fisqsfnjxnhz9zz6gveau.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fisqsfnjxnhz9zz6gveau.png)

## [](#7-colocate-related-logic)7\. Colocate related logic

Grouping files by type (e.g., components, utils, i18n) might seem like a good idea, but it's not.

**Why?**

*   It's harder to follow a component's logic when files are scattered.
    
*   You risk cleaning a component but forgetting related files.
    

Instead, keep all a component's logic and assets together in one folder.

[![Section Divider](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fisqsfnjxnhz9zz6gveau.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fisqsfnjxnhz9zz6gveau.png)

## [](#8-keep-components-simple)8\. Keep components simple

Avoid "God" components—those that try to do everything.

They're problematic ❌ because:

*   They're harder to read and understand.
    
*   They often lead to version control conflicts (Git, GitLab, etc.).
    
*   Modifying them can unintentionally impact the entire app.
    

**What to do instead?**

*   Think about how you'd structure your code if you were working with a teammate.
    
*   Keep your components focused on one task to minimize conflicts.
    

This approach keeps your code clean and helps your team work more efficiently.

[![Section Divider](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fisqsfnjxnhz9zz6gveau.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fisqsfnjxnhz9zz6gveau.png)

## [](#9-solve-diverse-problems)9\. Solve diverse problems

The more problems you solve with React, the better you get 🚀.

Every challenge you tackle teaches you something valuable:

*   You uncover new patterns and anti-patterns.
    
*   You add more tools to your developer toolbox.
    
*   You gain confidence in your skills.
    

But here's the key: don't just practice—**vary** your practice.

Explore different kinds of problems, projects, and solutions. That variety will help you grow faster as a React developer.

[![Section Divider](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fisqsfnjxnhz9zz6gveau.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fisqsfnjxnhz9zz6gveau.png)

## [](#10-learn-good-programming-patterns)10\. Learn good programming patterns

As a React dev, you should also focus on foundational programming skills:

*   Data Structures & Algorithms (e.g., sets, maps, recursion).
    
*   Principles like those in [The Pragmatic Programmer.](https://pragprog.com/titles/tpp20/the-pragmatic-programmer-20th-anniversary-edition/)
    

[![Section Divider](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fisqsfnjxnhz9zz6gveau.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fisqsfnjxnhz9zz6gveau.png)

## [](#11-read-a-ton-of-react-code)11\. Read a ton of React code

Building projects isn't the only way to learn—reading code is just as valuable 💪.

It helps you:

*   Pick up new tips and tricks.
    
*   Compare approaches to solving problems.
    

So, check out:

*   Open-source projects on GitHub.
    
*   Your teammates' code at work.
    

[![Section Divider](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fisqsfnjxnhz9zz6gveau.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fisqsfnjxnhz9zz6gveau.png)

## [](#12-use-typescript-asap)12\. Use TypeScript ASAP

There's a _before_ and an _after_ TypeScript 😅.

**Before:**

*   You spend extra time double-checking that you've passed the correct props.
    
*   Debugging can take hours, only to realize you passed the wrong value—or worse, `undefined`.
    

**After:**

*   You focus on structuring your components and defining types.
    
*   You catch silly mistakes before they reach production.
    

TypeScript isn't just a tool—it's a game changer for your React workflow.

[![Section Divider](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fisqsfnjxnhz9zz6gveau.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fisqsfnjxnhz9zz6gveau.png)

## [](#13-avoid-early-abstractions)13\. Avoid early abstractions

I used to be guilty of this a lot 🙈.

Whenever I designed a simple component, I'd try to make it reusable and future-proof.

**The problem?** I often created the wrong abstraction because there were no immediate needs.

This led to two outcomes:

1.  I'd end up refactoring the code later.
    
2.  Or worse, I'd have to live with the awkward abstraction, making development harder.
    

**What to do instead?**

*   Write a component that solves the problem at hand.
    
*   Extend it _only if_ there's a clear need for reuse, and do so gradually.
    

For a deeper dive into this topic, check out this great [video by Dan Abramov](https://www.youtube.com/watch?v=17KCHwOwgms).

[![Section Divider](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fisqsfnjxnhz9zz6gveau.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fisqsfnjxnhz9zz6gveau.png)

## [](#14-use-reacts-builtin-state-management-first)14\. Use React's built-in state management first

You don't need [Redux](https://redux.js.org/) or [Jotai](https://jotai.org/) right away.

React's useState, useReducer, and useContext go a long way for simple apps.

[![Section Divider](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fisqsfnjxnhz9zz6gveau.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fisqsfnjxnhz9zz6gveau.png)

## [](#15-dont-mindlessly-follow-online-advice)15\. Don't mindlessly follow online advice

A few years ago, I read online that memoization was "evil."

So, I stopped using it in my React apps.

That was until I crashed an app in production. 😅

The advice made sense for the developer who shared it, but it backfired for me because:

*   I had different use cases.
    
*   I needed to use effects in my app.
    
*   I was working with large-scale components.
    

**Main takeaway?** Don't mindlessly follow the advice you find online. Instead:

*   Discuss it with your teammates (if you have them).
    
*   Evaluate whether it applies to your specific context.
    

_Note: With React 19 optimization, this advice may finally be accurate_ 😅_._

[![Section Divider](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fisqsfnjxnhz9zz6gveau.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fisqsfnjxnhz9zz6gveau.png)

## [](#16-make-time-for-refactoring)16\. Make time for refactoring

> _“When developers are too afraid to clean bad code when they see it; then the system will start to rot. As the rot increases, so does the fear -- so the rot accelerates. At some point the code is such a horrible mess than none of the developers can estimate the effect of a particular change. Adding an icon might break other unrelated things.”_

**Uncle Bob Martin**

Every now and then, you'll notice that:

*   Your React components no longer make sense.
    
*   They've grown complex or too large.
    
*   There's room for improvement.
    

When this happens, take 5–30 minutes to refactor.

Small, regular enhancements can make your components easier to manage and prevent headaches.

[![Section Divider](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fisqsfnjxnhz9zz6gveau.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fisqsfnjxnhz9zz6gveau.png)

## [](#17-only-use-frameworks-when-necessary)17\. Only use frameworks when necessary

Spoiler: You don't need a framework to use React.

A simple React, [Vite](https://vite.dev/), and [react-router](https://reactrouter.com/) setup can go a long way.

Use frameworks like [Next.js](https://nextjs.org/) or [Remix](https://remix.run/) only when your app requires their features.

[![Section Divider](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fisqsfnjxnhz9zz6gveau.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fisqsfnjxnhz9zz6gveau.png)

That's a wrap 🎉.

Leave a comment 📩 to share your best tip.

And don't forget to drop a "💖🦄🔥".

If you're learning React, download my [101 React Tips & Tricks book](https://www.frontendjoy.com/p/download-my-free-101-react-tips-tricks-book) for **FREE**.

If you like articles like this, join my **FREE** newsletter, **[FrontendJoy](https://frontendjoy.com/)**.

If you want daily tips, find me on [X/Twitter](https://twitter.com/_ndeyefatoudiop) or [Bluesky](https://bsky.app/profile/ndeyefatoudiop.bsky.social).

## [](#spot-the-bug)🐞 SPOT THE BUG
