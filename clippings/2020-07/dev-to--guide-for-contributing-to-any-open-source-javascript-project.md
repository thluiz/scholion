---
url: "https://dev.to/saurabhdaware/a-guide-for-contributing-to-any-open-source-javascript-project-ever-hi"
captured_at: "2020-07-05T10:19:35-03:00"
title: "A Guide for Contributing to Any Open Source JavaScript Project Ever 💛 - DEV"
domain: "dev-to"
---

# A Guide for Contributing to Any Open Source JavaScript Project Ever

Jul 4
・6 min read

Lately, I had people asking how can they contribute to open-source projects when the codebase is large, or issues are taken, or good first issues seem difficult.

Initially, I've faced these questions as well and In this article, I will talk about how we can explore repositories, find the right issues to work on, and I will also try to answer some of the questions I just mentioned.

Let's goooo

**Table of Content**

## 1. Finding the Right Repository

**Contribute to something you use or find something that excites you and play around it before trying to contribute.**

I will highly suggest using the tool/library/website, before contributing to it. This will give you a nice overview of what it does and how it works.

If you're uncomfortable with the process of making PR, you can first contribute to [First Contributions Repository](https://github.com/firstcontributions/first-contributions). You have to add your name to the list and send a PR! They have a nice guide to explain the process.

## 2. Finding the Right Issue

In the issues section, you will find issues that have `good first issue` tag. Though it is not necessary, it is usually a sign from maintainers that 'hey these issues are relatively easy to tackle'. If you find any other issue that excites you more, go for it!

I will suggest trying to find issues related to documentation since they will be easier to get started but if you couldn't find such issues, that's ok as well you can pick whichever you like. As you get comfortable with the repository, you can go on picking more challenging issues.

And before we move forward, I know you might've heard this a lot and I am probably the 1000th person saying this but

**EVERY. CONTRIBUTION. MATTERS**

Even a spelling fix in documentation is a huge help to maintainers and you should totally be proud of such contributions!

Here's something I am proud of:

There was an extra bracket in the editor guide of DEV.to and I removed it :D

PR: <https://github.com/thepracticaldev/dev.to/pull/4500>

### Q. Every issue is taken, how do we find one?

A lot of times in popular open-source projects, you will find that most of the good first issues are taken and someone is already working on them. In this case, you can join their chat channels. Projects use Slack, Discord, Spectrum, GitHub Discussions, or other chat channels where you can ask for help. In those chat channels, you can drop a message asking for help in finding issues. Maintainers will then help you in finding an issue for you.

### Q. Did find an issue but it seems difficult...

This is very normal and even if you are experienced in contributing, you will likely find issues difficult in the first look when you're trying to contribute to a new organization.

You can always ask for help in comments of issues. Maintainers will then help you debug the problem and can point you to the right files that need changes but try exploring it yourself before asking for help.

## 3. Exploring Code

Before you start exploring the code, always read CONTRIBUTING.md file in the repository (If a repository does not have CONTRIBUTING.md, whoop whoop That's your chance to send a Pull Request that adds CONTRIBUTING.md). It usually has a local setup guide and other information that you may need for contributing. You can either set it up locally and then explore, or explore on the GitHub itself and then do a local setup to make changes.

I prefer exploring locally since you get to play around and execute the code.

Awesome so now you've,  
Decided the issue that you want to work on  
Read the CONTRIBUTING.md

Now we exploreeeee yayyyyy!!! oh.. but wait..

### Q. CODEBASES ARE HUGEE! How can we understand the whole codebase?

Fun fact, **You don't have to understand the whole code**

You will only have to care about the code that is related to the issue you've chosen.

### 3a. Finding the right files in the code.

*Tip: In VSCode, you can CTRL + SHIFT + F to find something in a complete project or On GitHub, you can use the search bar to find the related code.*

#### In websites/frontend repositories

If the project you're contributing to is a website, you can search for the words you see on the interface. E.g. If you want to contribute to the navigation bar of DEV, you can search for "Write a Post" button.

If it is not a website you can start finding the related functions by following the imports starting with an entry file.

#### In libraries, NPM Packages, and CLIs

In NPM packages, you would find package.json that has `main` attribute, the value of the `main` is the file that gets imported when you import/require that NPM package.

If you're contributing to a CLI, you would find `bin` in package.json that points to the file which is executed when you run a CLI command.

#### Mono-repos

Some projects like React, Gatsby, Next follow a mono repo. They have all the related projects in the same repository. In such projects, you would most probably find a folder called `packages` on root level and inside the `packages` you would find a folder with the name of the npm library (e.g `packages/react`, `packages/next`, `packages/gatsby`).

If you see the package.json file inside these packages, you would find the `main` key that points to the file which exports the functions that we usually import from these libraries.

##### Example

If you've used React, we usually import `useEffect` and other hooks like this, right?

```
import { useEffect } from 'react';
```

Which means the package react must be exporting the `useEffect` function

Let's find out!

As I've mentioned earlier, the mono-repos usually have a `packages` folder and inside that there is a package with the name of the NPM library ('react' in this case). So let's go inside `packages/react/`

Now we want to find the entry file so we will look into `package.json` file.

[Package.json of React](https://github.com/facebook/react/blob/master/packages/react/package.json) has `{'main': 'index.js'}` which means everything that we import from `react` package, has to be exported from `index.js`. Let's see if it has `useEffect` function!

Whoop whoop Yes it does!

Now you can follow the imports to that function to find a file that handles useEffect logic.

### 3b. Projects that require additional knowledge

If you've been building websites and webapps and then see the source code of React, the code will look different. Some repositories require knowledge of few additional topics which you may not come across otherwise.

Some projects are built on top of [Abstract Syntax Trees](https://en.wikipedia.org/wiki/Abstract_syntax_tree) whereas some repositories use a different language/libraries.

It is likely that you will find this code difficult in first look but more than difficult, it is different. It is different from what we JavaScript developers usually come across.

You can spend some time playing around the codebase and if you get stuck, you can always ask questions to the maintainers.

## Some Useful Links

### GitHub Repositories for Initial Contributions

- [First Contributions GitHub Repository](https://github.com/firstcontributions/first-contributions) - This is great to actually practice sending Pull Request (Fun Fact: I too started here :D)
- [Knaxus GitHub Organization](https://github.com/knaxus) - The aim is similar to first contributions but they will let you contribute to actual coding projects.

### Resources to learn git and GitHub

- YouTube Video, "Contributing to Open Source on GitHub for Beginners" by [Kent C. Dodds](https://twitter.com/kentcdodds)
  <https://youtu.be/k6KcaMffxac>
- YouTube Video, "git\_basics - The basics that you need for Git & GitHub!" by [Harsh Kapadia](https://twitter.com/harshgkapadia)
  <https://youtu.be/HF12-91iazM>
- Resources to learn git by GitHub
  <https://try.github.io/>

---

Thank you for reading this If you have any questions about git, GitHub, or contributing, you can ask them in comments or reach out to me on my [Twitter DMs @saurabhcodes](https://twitter.com/saurabhcodes).
