---
url: "https://thetshaped.dev/p/7-practical-tips-on-performance-optimizations-in-react-applications"
captured_at: "2026-09-25T21:26:49+01:00"
title: "7 practical tips on performance optimizations in React applications"
domain: "thetshaped-dev"
---

_**Is optimizing every line of code worth your time?**_

Over the years, I’ve worked on several React projects.

Along the way, I’ve learned some **valuable lessons about performance optimization**.

**Not all performance issues are equal**.

It’s important to **focus on the ones that make the biggest difference**.

_**Chasing after every minor optimization is a trap.**_

It’s tempting to try to optimize every part of your application from the start. However, this might waste your time on issues that don’t matter so much.

Instead, measure which performance problems have the biggest impact. Focus on fixing those first.

This way, you spend your time where it makes a difference.

**⛔ Avoid** spending time optimizing parts of your app without evidence they’re slow.

**✅ Prefer** to measure your app’s performance to find the bottlenecks before optimizing.

> **Keep your codebase clean from unnecessary optimizations.**

**What if doing less could actually achieve more? Remember the 80-20 rule?**

If something isn’t critical, don’t spend time improving it right now.

Do the least amount of work necessary to get the job done.

If a task or issue can wait, defer it for later.

This way, you avoid adding stuff to your codebase that you don’t need.

You deliver features and fixes that matter the most to your users.

**⛔ Avoid** working on non-essential improvements.

**✅ Prefer** focusing on tasks with immediate impact on functionality and performance.

> **Focus on what truly matters. Make better use of your time.**

_**Initial load times can make or break user engagement.**_

Loading all assets at once can slow down your app’s initial load time.

Instead, split your app into bundles. Load assets only when they’re needed.

Reduce the amount of code the browser has to download and process upfront.

This is known as Code-Splitting (see the next section).

**⛔ Avoid** including all your code in a single, large bundle that loads on startup.

**✅ Prefer** splitting your code and loading multiple bundles only when they’re needed.

> **Take care of your User Experience.**

_**Sending less code can make your app more robust and responsive.**_

JavaScript size affects performance in two main ways:

1.  **Sending files to the browser** - large files take longer to download.
    
2.  **Parsing and executing files** - more code means more work for the browser.
    

By implementing [code-splitting](https://react.dev/reference/react/lazy) into your project, you send only what’s necessary right away. This reduces download and execution times, which speeds up the loading time of your app.

Using HTTP/2 helps handle multiple small files efficiently. It supports request and response multiplexing.

**✅ Prefer** implementing [Code-Splitting](https://hpbn.co/optimizing-application-delivery/#minimize-concatenation-and-image-spriting) into your application.

_**Unnecessary rerenders are silent performance killers.**_

Unnecessary rerenders can slow down your application.

They often happen when components receive props that are compared by reference, like arrays, objects, and functions.

Passing a new function or object each time causes React to think something has changed.

You can use the built-in hooks to manage that - [useMemo](https://react.dev/reference/react/useMemo) and [useCallback](https://react.dev/reference/react/useCallback).

**⛔ Avoid** passing new object or function references as props unless necessary.

**✅ Prefer** memoizing expensive calculations, objects or functions to prevent unnecessary rerenders.

> **Reduce the workload on React’s rendering process.**

Keep an eye on how much JavaScript you’re sending to the browser.

Large bundles can slow down your app.

Regularly check your bundle size and look for ways to reduce it.

_**The real performance gains often lie in our own code, not the framework.**_

React is fast at updating the DOM.

Sometimes, the slowdown comes from our own code.

By **understanding the business domain well**, we can make certain trade-offs and choices and improve the overall performance.

For example, you can:

*   cache frequently used data in memory
    
*   memoize expensive calculations
    
*   avoid repetitive data fetching
    
*   implement pagination or infinite scrolling
    
*   use throttling and debouncing
    
*   use web workers for heavy computations
    
*   and etc.
    

**⛔ Avoid** writing inefficient business logic that slows down your application.

**✅ Prefer** optimizing your business logic first.

> **Be careful with your business logic. Usually, that’s the bottleneck, not the framework.**

*   Avoid premature optimizations. Keep your codebase clean from unnecessary optimizations.
    
*   Focus on Critical tasks and issues. Focus on what truly matters. Make better use of your time.
    
*   Defer non-essential. Take care of your User Experience.
    
*   Use Code-Splitting. Sending less code can make your app more robust and responsive.
    
*   Manage Rerenders. Reduce the workload on React’s rendering process.
    
*   Monitor the bundle size.
    
*   Optimize business logic. Usually, that’s the bottleneck, not the framework.
    

You can find me on **[LinkedIn](https://www.linkedin.com/in/petarivanovv9/)** or **[Twitter](https://twitter.com/petarivanovv9)**.

I share daily practical tips to level up your skills and become a better engineer.

_Thank you for being a great supporter, reader, and for your help in growing to 13.7K+ subscribers this week 🙏_

This newsletter is funded by paid subscriptions from readers like yourself.

If you aren’t already, consider becoming a paid subscriber to receive the full experience!

Think of it as buying me a coffee twice a month, with the bonus that you also get all my templates and products for FREE.

[Check the benefits of the paid plan](https://thetshaped.dev/about#%C2%A7why-subscribe)

_You can also hit the like ❤️ button at the bottom to help support me or share this with a friend to [get referral rewards](https://thetshaped.dev/?r=643nm). It helps me a lot! 🙏_

*   [Why Is Redis a Distributed Swiss Army Knife](https://newsletter.systemdesign.one/p/redis-use-cases?r=643nm&utm_campaign=post&utm_medium=web) by [Neo Kim](https://open.substack.com/users/135589200-neo-kim?utm_source=mentions)
    
*   [5 Frameworks To Master Communication And Influence As An Engineer](https://read.highgrowthengineer.com/p/5-frameworks-to-master-communication-and-influence?r=643nm&utm_campaign=post&utm_medium=web) by [Jordan Cutler](https://open.substack.com/users/58854493-jordan-cutler?utm_source=mentions) and [Wes Kao](https://open.substack.com/users/4005715-wes-kao?utm_source=mentions)
    
*   [Should you do on-call rotations in your engineering org?](https://newsletter.eng-leadership.com/p/should-you-do-on-call-rotations-in?r=643nm&utm_campaign=post&utm_medium=web) by [Gregor Ojstersek](https://open.substack.com/users/106098672-gregor-ojstersek?utm_source=mentions)
    
*   [Top 5 Caching Strategies Explained](https://blog.algomaster.io/p/top-5-caching-strategies-explained?r=643nm&utm_campaign=post&utm_medium=web) by [Ashish Pratap Singh](https://open.substack.com/users/83602743-ashish-pratap-singh?utm_source=mentions)
    
*   [Intro to GraphQL](https://newsletter.systemdesigncodex.com/p/intro-to-graphql?r=643nm&utm_campaign=post&utm_medium=web) by [Saurabh Dashora](https://open.substack.com/users/97484183-saurabh-dashora?utm_source=mentions)
    
*   [Horizontal Scaling Starts with Load Balancers – But Doesn’t Stop There](https://newsletter.systemdesignclassroom.com/p/horizontal-scaling-starts-with-load?r=643nm&utm_campaign=post&utm_medium=web) by [Raul Junco](https://open.substack.com/users/98661477-raul-junco?utm_source=mentions)
