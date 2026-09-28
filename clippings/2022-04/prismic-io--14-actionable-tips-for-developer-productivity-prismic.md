---
url: "https://prismic.io/blog/14-actionable-tips-for-developer-productivity?utm_campaign=Codecon%20Newsletter&utm_medium=email&utm_source=Revue%20newsletter"
captured_at: "2022-04-27T16:14:01-03:00"
title: "14 Actionable Tips For Developer Productivity - Prismic"
domain: "prismic-io"
---

# 14 Actionable Tips For Developer Productivity

Written by
*[Alex Trost](https://prismic.io/blog/authors/alex-trost)*
in
 [*concept*](https://prismic.io/blog/?category=concept)
on
*April 10, 2022*

My first years as a professional web developer were stressful and frustrating. I loved learning and working in this exciting industry but hated feeling so darn *unproductive*.

Seemingly small tasks took me hours. I'd jump between assignments and end the day with little accomplished. I'd lose focus on Slack or Reddit and wonder where the hours went.

Becoming proficient in HTML, CSS, and JavaScript was only half the battle. I had to learn how to use my tools, keep focus, and deliver projects on time.

I love productivity books like *Atomic Habits* and *Make Time*. I love the idea of getting tasks done faster and doing all the things I plan to pack into my day. Those books offer good general advice but nothing about getting websites shipped on time.

Unfortunately, much of the start-up tech scene is filled with toxic ideas like “rise and grind,” or “be a 10x developer.” These are methods for unhappiness and burnout, not developer productivity.

Instead of “10x,” I try to be a “1% better every day” developer. Minor changes to the tools I use, the way I focus, and how I approach my work have made a world of difference.

Here’s everything I know to be a developer who gets things done without burning out.

> Instead of “10x,” I try to be a “1% better every day” developer.
>
> ~ @trostcodes

[Tweet](https://twitter.com/share?ref_src=twsrc%5Etfw)

## Efficient Development

### 1. Use existing tools

While poor craftspeople blame their tools, there's no doubt that good tools used well can make you much more productive at your craft.

If you're building a website or web app, I recommend using a framework like Next.js, Nuxt, SvelteKit, or Astro. Frameworks handle the basics like routing, server-side, or static rendering so that you can focus on unique problems.

Your manager won't appreciate you delivering a project late because you wanted to write a new routing library. Pick up Next.js and ship the site on time.

Lean on battle-tested utility libraries like [Lodash](https://lodash.com/) and state management libraries like [Zustand](https://zustand-demo.pmnd.rs/) or [Pinia](https://pinia.vuejs.org/) before inventing your own.

### 2. Choose high-quality tools

I know when I’ve chosen the wrong tool, it becomes the central part of frustration throughout a project. A couple of hours of research upfront can save you hours or days throughout a website build. Don't be afraid to try new things, but also don't waste time on tools that aren't going to help you get the job done.

For example, responsive design and accessibility should be a high priority when making websites, so choose a browser built for developers. [Polypane](https://polypane.app/) lets you see multiple device sizes simultaneously and has many accessibility features, helping you catch issues before you ship them.

If you're building modern websites for clients who want a page-builder experience, Prismic's [Slice Machine](http://slicemachine.dev/) is an excellent choice. Slice Machine plugs into your local development workflow and makes creating page sections a breeze. The process of modeling data and wiring up my CMS used to slow me down, but now my productivity soars with Slice Machine.

Don't get emotionally attached to any tool. Choose a tool because it's best suited for the task, not just because it's your favorite or trendy.

### 3. Use Code Snippets

Code snippets are a great way to speed up development.

I guarantee you'll find some snippets for every popular IDE, language, and framework. Here's the list of [VS Code snippet plugins](https://marketplace.visualstudio.com/search?target=VSCode&category=Snippets&sortBy=Installs). You can even create your own snippet if you find yourself typing the same thing repeatedly. Plugins like [Snippet](https://marketplace.visualstudio.com/items?itemName=devonray.snippet) make it simple.

If you use VS Code, give [GitHub's CoPilot](https://copilot.github.com/) a try. It's far from perfect, but it's terrific at autocompleting and building things from comments or good function names. It won't write your entire app, but it can handle tedious boilerplate code for you.

![6759323b-606c-410e-892d-94434bd4ac6f_office-g28bdd5397_640.jpg](prismic-io--14-actionable-tips-for-developer-productivity-prismic/db03773fa5204b6b6fe01936a1f3f236.jpg)

### 4. Automate

Like creating your own code snippets, if you find yourself doing the same task repeatedly, find a way to automate it. Use task runners like [npm scripts](https://docs.npmjs.com/cli/v8/using-npm/scripts) to run tests, code linters, and any node scripts you might need to run often.

In the early days of responsive design, developers spent a lot of time creating desktop, mobile, and tablet versions of all their images. Now, that can all be automated! If you’re using Prismic, all of your images can be [transformed on the fly](https://prismic.io/docs/core-concepts/image#apply-your-own-transformations) with URL parameters, saving you a *ton* of time. You can even use services like [imgix](https://imgix.com/) or [Cloudinary](https://cloudinary.com/) to [generate social images](https://www.learnwithjason.dev/blog/auto-generate-social-image) automatically!

Regardless of what you're automating, [be sure it's worth the time invested](https://xkcd.com/1205/).

### 5. Reuse past work

Whenever I try something new, I’m slower at first, but then I have code and experience to revisit and reuse.

I’m *always* pillaging previous projects for some code to reuse or check how I did something.

Whenever you can, try to make the things you build reusable. We use reusable classes and components in modern web development to save time and make our code less error-prone. Josh Comeau, for example, brings a utils.js file [with him from project to project](https://www.joshwcomeau.com/react/file-structure/#:~:text=These%20utilities%20live%20in%20src/utils.js%2C%20and%20they%20come%20with%20me%20from%20project%20to%20project.%20I%20copy/paste%20the%20file%20when%20I%20create%20a%20new%20project.), filled with generic and useful functions.

We design and build websites with the same types of large components: heroes, testimonials, logo grids, pricing sections, etc. Don’t lock content editors into rigid page structures that you have to create. Instead, let them reuse those components to build pages with a system like Prismic Slices.

Because you’ve handed your editors a webpage builder, they can make sites independently, allowing you to tackle more interesting problems. You’ve delegated the mundane tasks to Prismic, and now you can build more sites for more happy clients.

Just make sure you’re not repeating past mistakes over and over. Writing tests can help with that.

> It's your call: write tests on Monday or fix production on Saturday.
>
> ~@trostcodes

[Tweet](https://twitter.com/share?ref_src=twsrc%5Etfw)

### 6. Write tests

Writing tests might be an up-front cost, but they pay dividends the longer you work on a project.

Not only do they reduce your chances of shipping bugs, but each well-written test defends you against breaking your code in that specific way. This lets you move quickly when modifying your code, knowing your tests will stop you from shipping certain bugs.

The testing ecosystem has never been better than it is right now. [Testing Library](https://testing-library.com/), [Vitest](https://vitest.dev/), and [Storybook](https://storybook.js.org/) give you a ton of power with a great developer experience.

So, it's your call: write tests on Monday or fix production on Saturday.

## Productive Work Habits

You can be the most efficient programmer in the world, but you’ll get nothing done if you can’t get yourself to do the work. Let’s look at some strategies to keep you on task and effective throughout the workday.

### 7. Work in focus sessions

Development is a job that needs your full attention, often for hours at a time.

If you're working in a large and complex codebase, getting your bearings inside the project can take some time. Make sure you give yourself time to get situated, then deeply work on the problem.

Focus sessions can range from long two-hour blocks to thirty-minute bursts of productivity, but the key is to work uninterrupted for that period of time. Set a timer, close your email and Twitter tabs, and only work on the task at hand. You’ll be surprised how much you can get done in a short amount of time when you’re completely focused.

Make sure you take breaks between your focus sessions, though. This keeps your mind fresh and focused on the task at hand. It also improves your productivity over time by preventing fatigue.

Many people love patterns like the [Pomodoro Method](https://todoist.com/productivity-methods/pomodoro-technique), where you work for 25 minutes, break for 5, and repeat. I like 50-minute blocks with 10-minute breaks, because it lets me dip into a flow state better. Try different lengths of time and see what works best for you.

If you find it hard to stay on task, I highly recommend accountability programs like [FocusMate](https://focusmate.com/) or [Centered](https://www.centered.app/). They pair you with other folks looking to focus, giving you an accountability buddy for the session. It’s incredibly effective for me.

However you schedule your sessions, don’t try to skip the break: it’s vital for your productivity. It's easier to resist checking your notifications if you know you'll be able to do it soon.

### 8. Don't Multitask

We were raised with the myth that getting lots of things done simultaneously is wise and beneficial. But it's not true. People who multitask are doing *worse* at all of the tasks they're trying to do.

Jumping between tasks is called *context switching*, and it can crush your productivity.

It turns out developers are especially vulnerable to context switching. [A study](https://reclaim.ai/blog/context-switching#:~:text=A%20field%20study%20in%20Rethinking%20Productivity%20in%20Software%20Engineering%20showed%20developers%20switched%20tasks%2013%20times%20per%20hour%20and%20spent%20only%20six%20minutes%20on%20a%20task%20before%20switching%20to%20another.) showed that developers only spent six minutes on tasks before switching and averaged 13 tasks per hour.

How much progress can you *really* make in six minutes?

To be efficient and effective, focus on one thing at a time. Don't try to build six different components at once. Take one to completion, then move on to the next.

### 9. Block distracting sites and apps

Notifications are a focus-killer, so you need to cut those off at the source. When you're focused, turn off notifications from email, Slack, Discord, and anything else that might try to steal your attention. Only check notifications during predefined times.

Some great apps like [ColdTurkey](https://getcoldturkey.com/) can block you from accessing distracting websites like Facebook, Reddit, and Twitter. If you're not sure how you're spending your time, [RescueTime](https://www.rescuetime.com/) will help you track your time to see exactly where the day went.

### 10. Stick to a schedule

If you're working from home, the flexible lifestyle can be a double-edged sword. Working whenever you want means you can be prone to putting work off.

First, make sure you have set hours for starting and ending work and taking breaks. Keep it as straightforward and consistent as possible. Then plan when you'll work on it and how long you expect each task to take. Without a plan, you're subject to [Parkinson's law](https://en.wikipedia.org/wiki/Parkinson%27s_law), which says "work expands to fill the time available for its completion."

## Grow as a Developer

Education doesn’t stop once you leave school. I consider myself a life-long learner and know that improving old skills and learning new ones is the best thing I can do for my career.

### 11. Learn the fundamentals

It's not as fun to start from the basics and master the fundamentals, but you'll be glad you did. If you don't know fundamental JavaScript concepts, debugging React code will be a frustrating and challenging process.

Don’t jump to Bootstrap before you understand the CSS, or you’ll have a terrible time when you need to customize or extend the components.

If you try to make a real-time chat app before you understand the basics of databases, you will struggle more than if you laid a solid foundation first.

Like atoms building into molecules, everything complex combines simpler concepts. A solid understanding of the basics will allow you to learn new frameworks more quickly.

![2b612cef-107d-4897-88a3-c9f467014385_laptop-g12bdd3b80_640.jpg](prismic-io--14-actionable-tips-for-developer-productivity-prismic/6d92498db3ee0b9b5e0edaaf6363965b.jpg)

### 12. Get faster at typing

Your words-per-minute is a bottleneck when getting your thoughts into your code editor. The fastest programmers that I know are incredibly fast typers and navigate their code with just their keyboards.

Any time you reach for your mouse, ask yourself why. Then learn the keyboard shortcut for that action. Learn the shortcuts for navigating to different tabs, scrolling to line numbers, shifting lines up and down, searching your repository, and anything else you often do.

### 13. Seek feedback

Frequent feedback is excellent for quickly improving any skill, and software development is no different. If you work in an environment where you can get feedback on code, that’s great!

If your team doesn’t do code reviews, ask for feedback from your teammates. If they give you a generic “looks good to me,” ask them for feedback on specific things. Ask them to check for functional errors, missing validation, or edge cases in your tests, and to evaluate whether you’re keeping to the coding conventions for the project.

If you're working solo, find a friend or colleague who can give you feedback. You can even hire mentors to help you level up your skills faster.

While it’s not *feedback*, I recommend reading as much code as possible, too. Look through other people’s projects to see how they structure files, create components, and handle state.

### 14. Staying current

We constantly get new browser features, JavaScript frameworks, and European privacy laws. Most of these things are evolving to make our jobs more accessible and more efficient.

Make it a point to learn one new thing each day. Take a course, read articles, listen to podcasts, and experiment with the latest technology.

You don't need to keep up with every new technology, but stay aware.

## Bonus: Take care of yourself

It may seem counterintuitive, but the most significant things that will affect your development happen *away* from the computer.

Exercise, quality sleep, and getting outside are essential for your health and your mental performance. If you need to, think of these as *hacks* to improve your cognitive abilities, reduce stress and frustration, and gain more energy.

Developers who get a good night's sleep are more alert and focused during the day. They're also less likely to make mistakes.

I know devs aren’t typically known for their fitness, but regular exercise reduces stress and helps your brain focus better. Find a form of exercise you enjoy and stick with it. Whether climbing, hiking, biking, yoga, or Wii Fit, whatever gets you moving is a valid form of exercise.

Going for walks around your neighborhood can help clear your head and allow you to come up with new ideas. Something about the fresh air and sunlight puts things into perspective. Plus, it gets you out of the chair you've been spending too much time in.

Think of it this way: if you overclock your CPU, you can always get a new one. It's not nearly as easy with your health.

## Final Thoughts on Developer Productivity

That's all I've got for you. If you've read this article as a way to procrastinate doing your work, it's time to get back to it!

Using the right tools and developing good habits is important for any web developer. These productivity tips will help you work smarter, not harder.

Are there any tips that you're looking to try? Let me know on [Twitter](https://twitter.com/trostcodes)!

Don't forget to check out [Prismic’s Slice Machine](https://prismic.io/docs/core-concepts/slice-machine) for the quickest CMS development workflow you can imagine.
