---
url: "https://dev.to/selbekk/how-to-get-started-with-react-in-2020-4po3"
captured_at: "2026-11-16T19:24:19+00:00"
title: "How to get started with React in 2020"
domain: "dev-to"
---

React is the most popular frontend framework by any standard today. There are in excess of two million developers using it, and a lot has been written about it.

Even though this is great in many regards, it also comes with downside - it's impossible to figure out where to turn for good content! So with a bit of tongue in cheek - here's yet **another** article on how you could get started with React.

What makes this one a bit different, is that I'm in charge of training hundreds of aspiring (or newly hired) developers every year. I've spent a lot of time researching ways to both teach and learn React, and I think I got it down to a science by now. The list is in order, so if you've touched on some of these topics before, feel free to skip ahead.

So if you're a senior systems engineer that's looking to pick up some frontend skills on the side, or if you're just starting out - this list should help you to get started

## [](#skip-redux-webpack-babel-et-al)Skip Redux, Webpack, Babel et al

React is often coupled with a state management tool called Redux. Redux is a _great tool_ for when you need it, but it's not something you need to know right away. Same goes for other tools you might encounter with React, such as Webpack, Babel, sagas, GraphQL and tons of other ones.  
**Skip all of that**. If you see a tutorial with one of those in the title - Marie Kondo that shit, or save it for later.

## [](#read-the-react-docs-from-beginning-to-end)Read the React docs from beginning to end

It might sound a bit boring, sure, but it's the best advice you're gonna get. The React documentation has been written, vetted and improved by hundreds of people over the course of half a decade. It's being translated into [48 different languages](https://isreacttranslatedyet.com/) (!), and is just a fantastic resource in every single way. It's well written, well structured, and is split up into chewable parts you can fly through in a few minutes each.

Read through its [main concepts](https://reactjs.org/docs/hello-world.html), [cool game tutorial](https://reactjs.org/tutorial/tutorial.html), and even some of the [advanced guides](https://reactjs.org/docs/accessibility.html) if you're feeling adventurous.

There's a huge section on the more "modern" way to use React as well - [hooks](https://reactjs.org/docs/hooks-intro.html) - which you should skim through as well. It's definitely the way forward, so spend the time you need to with this material, too.

Finally, I suggest you get familiar with the [API reference](https://reactjs.org/docs/react-api.html). You don't need to go through this one right away, but know that it's there for when you finally need to use one of those exotic APIs you rarely see in the wild.

## [](#check-out-kent-c-dodds-beginners-guide-to-react)Check out Kent C. Dodds' Beginners Guide to React

If you're into video courses and screen casts, you're going to love this. Honestly, even if you're _not_ into screen casts, you're going to love this.

You'll find it for free on [Egghead](https://egghead.io/courses/the-beginner-s-guide-to-react), and it's 19 videos totalling a very manageable 77 minutes of content.

Even seasoned React vets have something to learn in this video series. He'll take you through creating and updating nodes in the DOM manually, doing the same with regular JS-based React, and then showing you how to turn that into that mystical super juice called JSX. And tons of other stuff.

## [](#follow-along-with-michael-chan-on-his-holiday-adventures)Follow along with Michael Chan on his holiday adventures

After reading the docs and watching Dodds' beginner guide, you're starting to really have the good feels for this fantastic little framework we all love and enjoy.

Michael Chan - also known as chantastic - runs the React Podcast, but every holiday season he sits down to do something really cool for the community. This year, he's created a 24 part series, where he's presenting React step by step.

It's perfect for both experienced devs and for people just starting out.  
You can watch it on [YouTube](https://www.youtube.com/watch?v=YurJDf8JIks&list=PLnc_NxpmOxaP2lgtchapTNNhb_BMFXdgi&index=1) or on [dev.to](https://dev.to/chantastic/learn-react-in-25-short-lessons-react-holiday-2019-24np)

## [](#start-building-something-yourself)Start building something yourself

So you've read the docs, done the tutorials and seen some incredible videos of smart people introducing increasingly complex topics. Congratulations - you've at the end of this road of teaching.

The next step in your learning journey shouldn't be more advanced tutorials and courses, it should be building something yourself. Come up with an [app idea](https://www.google.com/search?q=app+ideas), and create something at least you'll use!

This way, you get to get into the _real_ part of learning React - trying to ship features to actual users in a timely manner. You know how props work - now it's time to learn how they'll work after a couple of weeks of adding features and neglecting debt. It's a lot to learn!

## [](#consider-a-paid-course)Consider a paid course

The React community is lucky in that it has an abundance of free options to get you up to date on the latest and greatest in React. However, some of the most polished content is only available at a premium - as it should be.

If you're employed, ask your employer to shell out a few bucks for your program of choice. There's a lot to choose from, but here's some of my favorite resources:

### [](#egghead)Egghead

Egghead is an incredible resource, with tons of great, free resources for any skill level. They do have some paid content, though, which can be accessed at a pretty decent price. Check them out at [egghead.io](https://egghead.io/)

### [](#frontend-masters)Frontend Masters

Frontend Masters is pretty similar to Egghead, but has different content from different authors. You can browse their catalog and find something you're interested in before you shell out for a monthly subscription. Check them out at [frontendmasters.com](https://frontendmasters.com/).

### [](#testingjavascript)TestingJavaScript

Not directly React related, but still some of the best money I've spent online. This is Kent C. Dodds' opus to front end testing, which has really kicked off a renewed interest in testing my code for me. If you can afford it, check it out at [testingjavascript.com](https://testingjavascript.com/).

### [](#tylermcginnis)TylerMcGinnis

A bit smaller than the previous platforms, but known for some of the very best content in the React business. Tyler also happens to be a stand up guy, and I'd be happy to give him my moneys. Check out his courses at [tylermcginnis.com/courses](https://tylermcginnis.com/courses)

### [](#wes-bos)Wes Bos

Finally, Wes Bos. He was listed as an option for "best resource to learn from" in the State of JS survey this year, so you know he's good. He's got a lot of [free stuff on YouTube](https://www.youtube.com/user/wesbos), as well as a long list of paid courses in everything from GraphQL to Markdown. Check them out at [wesbos.com/courses](https://wesbos.com/courses/)

## [](#build-your-own-version-of-react)Build your own version of React

As a bonus, I want to share a workshop some colleagues of mine created last year. It's a workshop where you re-implement a basic, yet working version of React and ReactDOM from scratch!

It was an incredible deep dive into why React works the way it works, and how you can leverage that to your advantage. It's completely free, and will probably be held as an actual workshop at a conference near you in 2019.

[Check it out here!](https://github.com/sveinpg/build-your-own-react)

* * *

So that's it - the definite guide to get started with React development in 2020. At least for now.

I hope this will get you started on your React journey. If you have any questions, or need a resource to learn a particular type of React development, leave me a comment and I'll try to help you along. This is - after all - for the community. ❤️
