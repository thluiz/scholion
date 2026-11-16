---
url: "https://dev.to/teamxenox/philosophy-of-a-good-developer-30c2"
captured_at: "2026-11-16T00:57:54+00:00"
title: "Philosophy of a Good Developer"
domain: "dev-to"
---

It’s been a long time since we talked about something philosophical. So I thought I'd write a new post for you all, this time going back to basics. There's something I've been thinking about a lot lately.

#### [](#who-is-actually-a-good-developer)Who is actually a good developer?

Well, of course, the answer we're exploring today is not strictly technical, but goes beyond that. Even if you are technically super strong, you can still be a bad developer. I’m sharing my thoughts as a long-time product manager, programmer and techie. To some of you, a few of the points might feel familiar and perhaps even obvious, but there's a reason they're here. I am certain most of you will find something to learn and improve upon, so stay with me until the end, because Rule #6 is the most important of them all.

Let’s explore what it takes to actually be a good developer. 😇😇

### [](#rule-1-dont-be-a-lone-wolf)Rule 1: Don’t be a lone wolf 🐺

When you are working on a commercial application or project, the first thing you need to understand is that your code is not just your code; it will be read and reviewed by multiple people. Even if right now, you are the only one working on the project, someone else will have to read and understand it in the future. Your code should be readable, not only for you but also for anyone else who might join the project down the line.

So make sure that you:

**_1\. Don't use silly variables names_**

Oh yeah, I know most of us have been there and done that. To some of us, it might even seem like a bit of harmless fun, but that's far from the truth. Don't use random variable names; that's what rookies do. Your variable name should always make it clear what its purpose is. You need to understand that code will not only be interpreted by the computer but by humans as well.  

```

    let vx34 = "Something" // ❌
    let x = "Something" // ❌
    let boxycat = "Something" // ❌

    let catCount = 34 // ✅
    let user_message = "Something" // ✅

```

Enter fullscreen mode Exit fullscreen mode

**_2\. Always use comments_**

When defining a function, along with giving it a proper name, make sure that you use comments. Of course, you don't have to do it everywhere, but more often than not, it helps to further clarify your intent with code comments. The rule of thumb is _Write a comment if it can save another developer's time to understand the code_. If another dev has to go back and forth in the code just to understand a single function and what it's actually doing, that's bad code. Be foresighted, add appropriate comments where needed.

Using Documentation Generators like JSdoc can also be efficient. Not only will your comments look good but it will also support a few cool IDE features like function definitions preview.  

```

/**
 * Represents a book.
 * @constructor
 * @param {string} title - The title of the book.
 * @param {string} author - The author of the book.
 */
function Book(title, author) {

}
```

Enter fullscreen mode Exit fullscreen mode

To learn more about JSdoc, check out [this](https://dev.to/paulasantamaria/document-your-javascript-code-with-jsdoc-2fbf) article.

**_3\. Make a project wiki_**

This is mostly ignored, but it's a highly critical rule to follow. See, the thing is programming is not a linear process. You might stumble upon a dozen problems while trying to make something work. Whatever it is, write it down. Let's say, even if it's just a problem that you faced while installing MongoDB on your Linux machine, write down every piece of information that can help your teammates solve this same problem if they ever run into it in the future. A well-documented code always has a well-documented wiki. How to run the dev env, how to use the design system, how to export env variables locally, whatever it is, **write a wiki!** Trust me, you will save a lot of your (and your team's) time. Here are some useful links that I found:

*   [Documenting your projects on GitHub](https://guides.github.com/features/wikis/)
*   [How to write wikis in Gitlab](https://docs.gitlab.com/ee/user/project/wiki/)

**And oh, while we're on the topic of documentation, here's a neat little tool you can use to read your node modules' documentation easily.**

## Article No Longer Available

**_4\. Format code properly_**

Last but not the least, indenting code well. I recommend using tools like prettier to make this easy. You can enable the "format on save" feature also; I love this feature. Here is the [full guide](https://dev.to/robertcoopercode/using-eslint-and-prettier-in-a-typescript-project-53jb) on how to do it.  

```

// Bad 🙅🏻‍♂️ ❌
function Book(title, author) {
if(data){
let data = false
}
}

// Good 🤩 ✅
function Book(title, author) {
  if(data){
    let data = false
  }
}

```

Enter fullscreen mode Exit fullscreen mode

So do remember that working on a project is a collaborative effort. Save everyone's time by using the above tips. As Ned Stark said:

> "The lone wolf dies but the pack survives." 🐺☠

[![Ned Stark nodding gif](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F5j7seu8zki5r4fueo8p9.gif)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F5j7seu8zki5r4fueo8p9.gif)

### [](#rule-2-you-cant-remember-it-all)Rule 2: You can't remember it all 🤔

So imagine it's a regular day, you're working on something and then suddenly, you notice that something else is broken. You know how to fix it but really don't have the bandwidth right now. So you decide to make a mental note of it and get back to it later. But you never do.

Sounds familiar? Well, that's just how the human brain works. 🧠 In this particular context, think of your brain as RAM. It remembers certain things during a process and then erases them later, which is exactly why we need to write things down. Computers save things to their hard drives, and in the same manner, we should be writing down important things as well if we want to recall them later. It sounds like such a basic thing to do and yet so many of us struggle with it.

Writing these things down is also supremely helpful in building great software because it lets you focus on the task at hand while also giving you a big picture view when needed. **More on this later in Point #6**!

Using `TODO:` comments is highly effective. This can not only help _you_ remember to do certain tasks later but can also encourage your fellow teammates to do those tasks instead if you couldn't get to them for some reason.

But if you wanna step up your game, I recommend using a tool like Todo Plus

[![ToDo Plus in action gif](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fs25mye7jadwuw74b27x8.gif)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fs25mye7jadwuw74b27x8.gif)

With this, you can either create a to-do file or track all your `TODO:` comments in a single file. Highly recommend it.

So don't just keep things in your mind palace. **Write them down!**.

[![Sherlock Holmes mind palace gif](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/http%3A%2F%2Fgiphygifs.s3.amazonaws.com%2Fmedia%2F6SaVutI40pCKc%2Fgiphy.gif)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/http%3A%2F%2Fgiphygifs.s3.amazonaws.com%2Fmedia%2F6SaVutI40pCKc%2Fgiphy.gif)

### [](#rule-3-get-into-the-users-shoes)Rule 3: Get into the user's shoes 🥾

As developers, technically you are the first users of the app. Your work is not limited to writing logic or completing features. You also need to ensure that the feature(s) you are building is actually usable. Always ask yourself: If I were the intended user of this app, would I be able to use it? The answer to this should always be a resonant yes. Test all the features to pass _your_ standards first, and as a computer engineer, those standards - as well as your expectations from a feature - should be high. Don't wait until the QA team gives you a list of bugs, NO! If you are having trouble understanding the user's perspective, sit down with your PM and understand it. It's okay if you can't fully wrap your mind around it, but you must always try.

[![Michael Fassbender ](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F6ezpfn1cish6bwvh0ahd.gif)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F6ezpfn1cish6bwvh0ahd.gif)  
This is especially important for full stack developers. If you don't just want to be a full stack developer in name but rather a champion of the people 🏆, you _must_ learn how to do many things well, including UIX design. I talk about this in detail in my article on how to improve your CSS, which is a powerful tool for any full stack dev.  

## Article No Longer Available

### [](#rule-4-no-shortcuts)Rule 4: No Shortcuts...

...except the application shortcuts. 😜  
There are many best practices for devs based on this rule only. I'm sure you have been in a situation where you have to make the same or similar thing multiple times, and you find yourself copy-pasting the same code over and over again. In a corner of your heart, you _know_ that redundancy isn't good, and following the separation-of-concern rule, you should probably make a function out of it. But your lazy brain tells you it could take a long time, so you decide to skip it. After all, you're saving time you could put into building a new feature, right? Wrong! By doing so, you decrease the performance of the app and end up wasting more time when you revisit it to remove that redundant code. And trust me, it's damn frustrating!

[![frustrated man gif](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fxsfju02x5wr5ffhud04p.gif)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fxsfju02x5wr5ffhud04p.gif)  
Anything worth doing, is worth doing right!

You will face many other situations like this on a daily basis, and you will have two choices: the easy one and the right one. So just take that extra leap and do it. **There are no shortcuts.** 🙅🏼‍♂️🚫

### [](#rule-5-dont-play-the-blame-game)Rule 5: Don't play the blame game 😡

[![Hasan Minhaj pointing finger gif](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fst68n7r1x6usr59pe1ym.gif)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fst68n7r1x6usr59pe1ym.gif)

As a PM, I have faced this problem countless times that whenever something is broken, developers are quick to point fingers at each other. This does nothing but damages the teamwork. We need to understand that it's a team game. If you knew about the existence of a certain issue already and you did nothing to fix it or even bring it to light, you are equally responsible. Always take full responsibility and ownership for the project and don't play the blame game.

Great teams do it on a subconscious level, and I've seen it work so well. Good managers help in fostering this approach while bad ones do the exact opposite (but that's a discussion for another time).

### [](#rule-6-look-at-the-bigger-picture-%F0%9F%96%BC)Rule 6: Look at the bigger picture 🤨🖼

In the end, this is the most important mindset that can differentiate you from others. Of course, you are doing your job just like anyone else, and at the end of the month, you will get your salary for the work you've done. Now, that's great and you can stop there, but I dare you to think beyond that. Whether you've considered it or not, your name is associated with the company or product you are working on. You are not just writing code, my friend, **you are leaving behind a legacy.**

You need to create opportunities for yourself to step back and get an overview of things. Having a big picture view is important to stay aligned with the mission and reassess tasks/priorities with respect to how they help you achieve the ultimate goal, i.e. build great software that helps users be awesome.

At the end of the day, if your creation is garbage, that's on you. Inversely, if your creation is flawless, that's on you as well. Do your best work, and your work will speak for you.

[![big brain meme gif](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fgdvoovussjewdz1i5ib3.gif)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fgdvoovussjewdz1i5ib3.gif)

## [](#conclusion)Conclusion

Being a good developer takes more than just technical skills. If improving technical skills is all you have your sights set upon, that's a low bar. You need to keep in mind that:

*   When working on a commercial project, you shouldn't operate like a lone wolf; write easily understandable code and document everything!
*   You can't remember everything, so write stuff down; use To-do comments to get back to things you skipped earlier.
*   You must put yourself in the user's shoes and build features they can use; judge what you build on your own standards before anything goes to QA.
*   Shortcuts will only come back to bite you in the behind; when you do something, do it right.
*   Blaming others when things break down will lead you nowhere; take extreme ownership of what you're building and foster teamwork.
*   A software is more than just a collection of features, so make sure you step back and look at the big picture every so often. What you build is your legacy.

So expand your mind and be the best developer you can be. I've written at length about how you can improve your focus and increase your brainpower to deliver your best work. 🧠 See the article below to explore this more.

## Article No Longer Available

**What tips would _you_ give to someone to help them become a good developer? I'd love to hear, so write them down in the comments!** 👇🏼💬

* * *

### [](#ps-are-you-an-opensource-enthusiast)P.S. Are you an Open-Source enthusiast?

There are many reasons to love OSS. It's fundamentally collaborative in nature, and everyone involved is building something for the love of it. I've met so many great developers through open-source ever since I started Team XenoX. 🔥 If _you_ are also someone who is an open-source enthusiast and looking to build cool products in a collaborative environment and meet awesome people, I welcome you to join me in [XenoX Multiverse](http://bit.ly/xnxmltvrs). Check out some of the [stuff we've made](http://bit.ly/madebyxenox) this year.

[![open arms join us gif](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F6qgwmjtjci3q0dr12jci.gif)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F6qgwmjtjci3q0dr12jci.gif)

**_Oh, and if you're looking for work, we're hiring at Skynox Tech! Go ahead and apply [here](http://bit.ly/2CA3qDe)._** 😀💯  
Have a great day and I'll see you all again very soon!
