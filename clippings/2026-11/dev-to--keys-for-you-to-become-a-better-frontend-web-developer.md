---
url: "https://dev.to/gurutobe/keys-for-you-to-become-a-better-frontend-web-developer-1ba8"
captured_at: "2026-11-16T01:23:08+00:00"
title: "Keys for You to Become a Better Frontend Web Developer"
domain: "dev-to"
---

I keep getting asked from a fair amount of people who happen to have a good experience in learning Web Development but got stuck in making tens of UI templates and dummy projects, this is really frustrating, seriously, how could they move to the next level?  
This one will be more like a cheat sheet or a checklist than an article.  
I assume that it's like if we were talking in a friendly chat, and you'll take my words, write notes, then go search for what these terms actually mean if you don't know some of them.  
Let's dive in, we have no time to waste!

## [](#1-know-your-programming-language)1\. Know your Programming Language:

This part will be the longest, it could've taken a separate article by itself, but it's good to have it with the other parts.  
Mostly, people have mistaken programming languages with their native-spoken languages.  
In contrary to problem-solving, in order to use a programming language you don't need common sense, it's a set of rules written by someone to help you communicate with your machine, in our case, we used to use it to communicate with our browser, and nowadays, we use it everywhere.  
**JavaScript** has specs and rules that should be respected, not to go out of it, and expect it to be written the same way as another language.

These are my notes:

#### [](#1-types)1\. Types:

Learn how JS is **value-typed** and know the different types the language offers to access and use memory, store data, not to mention defining your code parts.

#### [](#2-scopes-amp-closures)2\. Scopes & Closures:

How variables and pieces of code you have in a function will communicate with other pieces in the outer scope or another scope.

#### [](#3-hoisting)3\. Hoisting:

The language offers solutions to read and execute your code, in a very unique way and order, you should know about that.

#### [](#4-oop-in-js)4\. OOP in JS:

How JS was developed over the years to provide solutions and empower engineers to use well-known programming paradigms.

#### [](#5-async-js)5\. Async JS:

You're a developer that targets to build dynamic, single-page apps, real-time apps, you should gradually learn how to write code that waits for something then does something else.  
Cover **Callback Functions** first, then move to **Promises**, have fun with **async-await** solutions, and maybe get to know Generator Functions, blend all of these topics into fetching data with XHR Requests, wait for the data and use it to update your HTML content and make operations on it.

#### [](#6-arrays-higherorder-functions)6\. Array's Higher-Order Functions:

Instead of making for loops and using conditionals inside of it to target or restructure array elements, why not introduce yourself to **"map, find, filter, reduce"**, these are all handy functions that you won't pass a day as a skilled JS developer without using them.

#### [](#7-how-js-interacts-with-the-browser)7\. How JS interacts with the browser:

Using **global objects** like **window**, **document**, and how JS accesses HTML elements and subscribes to events and actions happening to it.

#### [](#8-object-destructuring-and-spread-operator)8\. Object Destructuring and Spread Operator:

Very handy especially when you need to access a part in your data structure or state, or changing it without losing immutability approaches.

## [](#2-git-version-control)2\. Git Version Control:

Hopefully, you'll be working in a big company, even if it's a small one, we all aim for using good Code Delivery Systems and well-established ones, you'll handle multiple environments: production, staging, etc.  
So, you really need to have confidence in Git branching commands, git **checkout**, checkout -b, git **merge** and its different types "what does it mean fast-forward vs no-ff vs squash", you'll need to **cherry-pick** a feature in order to release it, there's a command for that, you may need to **revert** something you did, reset another thing, not to mention pushing, pulling and other basic ways to interact with your colleagues to add awesome features to your codebase.  
Be bold, don't be shy to ask, seek reviews, and get into experience-sharing conversations.

## [](#3-dont-get-satisfied-with-one-framework-or-library)3\. Don't get satisfied with one Framework or Library:

Better than the skill of acing one frontend JS framework, is to have transitioned between two of them, not to get lost or confused, but gaining the experience when you go to the second one and ask it: "I used to do this thing in that way in the previous one, in what way do you offer to do it?", this skill, in my opinion, is by far the most important skill and what separates a person who's shy and can't move from being a junior to a person with high potential to deal with senior level problems, who don't have a problem to hop in with one of his teammates and solve a problem, even if he's working with different technology and/or didn't use this technology before.

## [](#4-dont-be-stingy-with-yourself-in-backend-topics)4\. Don't be stingy with yourself in Backend Topics:

As the consumer of BE produced APIs and the one responsible for showing it to the user, also responsible for collecting data from user and delivering it to BE, you'll need to have some knowledge about how they design the system you're presenting, not in a complicated or a detailed way, of course, just have a fair knowledge about **ERD** "Relational Diagrams" and how Entities and Models "Ex: In a social network app: Posts, Comments, Users" are talking and related to each other in databases, especially relational database, Learn basic **SQL** "Structured Query Language", just try CRUD operations "Create a model we mention in a Table, create a record, read from it, updated it, delete it", maybe create another table and apply relations and joins to it "use foreign keys", go search for all of these terms!

## [](#5-get-your-hands-dirty-with-module-bundlers)5\. Get your hands dirty with Module Bundlers:

Webpack, Parcel, and other tools that use node and npm's ecosystem to host your development experience or empower your framework of choice, dig deep into documentation and know how it works, how it tracks your files and deals with them as trees of imported files inside of imported files until you get to your main index.js, knowing how using code-splitting and optimization options can boost your performance, how does a bundler build your code into just a classic set of files needed for your server to respond with just an HTML file, a CSS file, and a JS chunk, just that simple.

## [](#6-have-your-working-tools-personalized-for-you)6\. Have your working tools personalized for you:

Your text editor, your terminal, should help you to be in control of the development process, monitor your Git branches,  
Ex: using Gitlens extension in VSCode helps you to know who made which change in the code, and when.  
Your terminal can be helpful, not just for writing commands but for knowing about your branch status, what changes did you do, are you ahead or behind, use your text editor before you push to compare changed files and to make changes as less as possible.

I really hope this was helpful, you'll find previous articles I wrote that'll help a lot with the first part of this one, also, if you have any question, please don't hesitate to reach out.
