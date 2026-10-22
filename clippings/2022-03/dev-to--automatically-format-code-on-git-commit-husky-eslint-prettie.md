---
url: "https://dev.to/ruppysuppy/automatically-format-your-code-on-git-commit-using-husky-eslint-prettier-in-9-minutes-45eg"
captured_at: "2022-03-17T12:11:37-03:00"
title: "Automatically Format your code on Git Commit using Husky, ESLint, Prettier in 9 minutes - DEV Community 👩‍💻👨‍💻"
domain: "dev-to"
---

![pqfe10lbkh7m1z3xn72u.png](dev-to--automatically-format-code-on-git-commit-husky-eslint-prettie/99c144b995b838c7ee16a8ceb514a36f.png)

[![941751d8-06b8-41bd-9de9-6ea056b7199f.png](dev-to--automatically-format-code-on-git-commit-husky-eslint-prettie/19b9065029e9b175fa85bfb01e7bcb5f.png)](https://dev.to/ruppysuppy)

[Tapajyoti Bose](https://dev.to/ruppysuppy)

Posted on Mar 13
• Originally published at [tapajyoti-bose.Medium](https://tapajyoti-bose.medium.com/automatically-format-your-code-on-git-commit-using-husky-eslint-prettier-in-9-minutes-4dd6233f32b1)

# Automatically Format your code on Git Commit using Husky, ESLint, Prettier in 9 minutes

[#javascript](https://dev.to/t/javascript)
[#webdev](https://dev.to/t/webdev)
[#productivity](https://dev.to/t/productivity)
[#git](https://dev.to/t/git)

When collaborating on a project with several other developers, maintaining a **consistent code style** drastically improves the **code readability** and **maintainability**.

Luckily we can automate this crucial process using **Husky**, **ESLint**, **Prettier** to make sure the code is formatted, every time someone commits.

## 1. Install Packages

We need to install the following packages:

- **Husky**: A tool that makes working with `git hooks` a piece of cake
- **ESLint**: `Linter` for **JavaScript**
- **Prettier**: `Code formatter`
- **Lint-staged**: As the docs state: Run `linters` against staged `git` files and don't let slip into your codebase!

To install the packages, use:

```
npm install --save-dev eslint prettier lint-staged husky
```

![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='20px' height='20px' viewBox='0 0 24 24' class='highlight-action crayons-icon highlight-action--fullscreen-on js-evernote-checked' data-evernote-id='313'%3e%3ctitle data-evernote-id='314' class='js-evernote-checked'%3eEnter fullscreen mode%3c/title%3e %3cpath d='M16 3h6v6h-2V5h-4V3zM2 3h6v2H4v4H2V3zm18 16v-4h2v6h-6v-2h4zM4 19h4v2H2v-6h2v4z' data-evernote-id='315' class='js-evernote-checked'%3e%3c/path%3e %3c/svg%3e)
![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='20px' height='20px' viewBox='0 0 24 24' class='highlight-action crayons-icon highlight-action--fullscreen-off js-evernote-checked' data-evernote-id='316'%3e%3ctitle data-evernote-id='317' class='js-evernote-checked'%3eExit fullscreen mode%3c/title%3e %3cpath d='M18 7h4v2h-6V3h2v4zM8 9H2V7h4V3h2v6zm10 8v4h-2v-6h6v2h-4zM8 15v6H6v-4H2v-2h6z' data-evernote-id='318' class='js-evernote-checked'%3e%3c/path%3e %3c/svg%3e)

## 2. Configure ESLint

Run the following command to initialize **ESLint**:

```
npx eslint --init
```

![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='20px' height='20px' viewBox='0 0 24 24' class='highlight-action crayons-icon highlight-action--fullscreen-on js-evernote-checked' data-evernote-id='330'%3e%3ctitle data-evernote-id='331' class='js-evernote-checked'%3eEnter fullscreen mode%3c/title%3e %3cpath d='M16 3h6v6h-2V5h-4V3zM2 3h6v2H4v4H2V3zm18 16v-4h2v6h-6v-2h4zM4 19h4v2H2v-6h2v4z' data-evernote-id='332' class='js-evernote-checked'%3e%3c/path%3e %3c/svg%3e)
![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='20px' height='20px' viewBox='0 0 24 24' class='highlight-action crayons-icon highlight-action--fullscreen-off js-evernote-checked' data-evernote-id='333'%3e%3ctitle data-evernote-id='334' class='js-evernote-checked'%3eExit fullscreen mode%3c/title%3e %3cpath d='M18 7h4v2h-6V3h2v4zM8 9H2V7h4V3h2v6zm10 8v4h-2v-6h6v2h-4zM8 15v6H6v-4H2v-2h6z' data-evernote-id='335' class='js-evernote-checked'%3e%3c/path%3e %3c/svg%3e)

You will be prompted to answer a few questions, from which the **configuration** for your specific use case will be generated

[![1qjf4xq4ww5qarco9riz.png](dev-to--automatically-format-code-on-git-commit-husky-eslint-prettie/8358ee06a5c27164b7049218e22b0199.png)](https://res.cloudinary.com/practicaldev/image/fetch/s--tmGHiQUO--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://dev-to-uploads.s3.amazonaws.com/uploads/articles/1qjf4xq4ww5qarco9riz.png)

The generated **configuration** would look something like this:

```
{
  "env": {
    "browser": true,
    "es2021": true
  },
  "extends": ["eslint:recommended"]
}
```

![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='20px' height='20px' viewBox='0 0 24 24' class='highlight-action crayons-icon highlight-action--fullscreen-on js-evernote-checked' data-evernote-id='378'%3e%3ctitle data-evernote-id='379' class='js-evernote-checked'%3eEnter fullscreen mode%3c/title%3e %3cpath d='M16 3h6v6h-2V5h-4V3zM2 3h6v2H4v4H2V3zm18 16v-4h2v6h-6v-2h4zM4 19h4v2H2v-6h2v4z' data-evernote-id='380' class='js-evernote-checked'%3e%3c/path%3e %3c/svg%3e)
![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='20px' height='20px' viewBox='0 0 24 24' class='highlight-action crayons-icon highlight-action--fullscreen-off js-evernote-checked' data-evernote-id='381'%3e%3ctitle data-evernote-id='382' class='js-evernote-checked'%3eExit fullscreen mode%3c/title%3e %3cpath d='M18 7h4v2h-6V3h2v4zM8 9H2V7h4V3h2v6zm10 8v4h-2v-6h6v2h-4zM8 15v6H6v-4H2v-2h6z' data-evernote-id='383' class='js-evernote-checked'%3e%3c/path%3e %3c/svg%3e)

If you are lazy like me, just copy and paste the **configuration** into a file called `.eslintrc.json` instead of answering the long list of questions.

To check out all the available **configurations**, visit the [ESLint documentation](https://eslint.org/docs/rules/). The config provided above is just a barebone example.

## 3. Configure Prettier

Configuring **Prettier** is similar to **ESlint**, just add a `.prettierrc.json` file to your project root and you are good to go.

You can use the following **configuration** as a starting point:

```
{
  "bracketSpacing": true,
  "semi": true,
  "singleQuote": true,
  "trailingComma": "all",
  "printWidth": 80,
  "tabWidth": 2
}
```

![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='20px' height='20px' viewBox='0 0 24 24' class='highlight-action crayons-icon highlight-action--fullscreen-on js-evernote-checked' data-evernote-id='443'%3e%3ctitle data-evernote-id='444' class='js-evernote-checked'%3eEnter fullscreen mode%3c/title%3e %3cpath d='M16 3h6v6h-2V5h-4V3zM2 3h6v2H4v4H2V3zm18 16v-4h2v6h-6v-2h4zM4 19h4v2H2v-6h2v4z' data-evernote-id='445' class='js-evernote-checked'%3e%3c/path%3e %3c/svg%3e)
![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='20px' height='20px' viewBox='0 0 24 24' class='highlight-action crayons-icon highlight-action--fullscreen-off js-evernote-checked' data-evernote-id='446'%3e%3ctitle data-evernote-id='447' class='js-evernote-checked'%3eExit fullscreen mode%3c/title%3e %3cpath d='M18 7h4v2h-6V3h2v4zM8 9H2V7h4V3h2v6zm10 8v4h-2v-6h6v2h-4zM8 15v6H6v-4H2v-2h6z' data-evernote-id='448' class='js-evernote-checked'%3e%3c/path%3e %3c/svg%3e)

To check out all the available options, head over to the [Prettier Documentation](https://prettier.io/docs/en/options.html).

Also add a `.prettierignore` file to your project root to `ignore` files that you don't want to be formatted, use the following content as a base:

```
package-lock.json
yarn.lock
node_modules
# any other unwanted files or folders
```

![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='20px' height='20px' viewBox='0 0 24 24' class='highlight-action crayons-icon highlight-action--fullscreen-on js-evernote-checked' data-evernote-id='460'%3e%3ctitle data-evernote-id='461' class='js-evernote-checked'%3eEnter fullscreen mode%3c/title%3e %3cpath d='M16 3h6v6h-2V5h-4V3zM2 3h6v2H4v4H2V3zm18 16v-4h2v6h-6v-2h4zM4 19h4v2H2v-6h2v4z' data-evernote-id='462' class='js-evernote-checked'%3e%3c/path%3e %3c/svg%3e)
![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='20px' height='20px' viewBox='0 0 24 24' class='highlight-action crayons-icon highlight-action--fullscreen-off js-evernote-checked' data-evernote-id='463'%3e%3ctitle data-evernote-id='464' class='js-evernote-checked'%3eExit fullscreen mode%3c/title%3e %3cpath d='M18 7h4v2h-6V3h2v4zM8 9H2V7h4V3h2v6zm10 8v4h-2v-6h6v2h-4zM8 15v6H6v-4H2v-2h6z' data-evernote-id='465' class='js-evernote-checked'%3e%3c/path%3e %3c/svg%3e)

## 4. Configure Lint-staged

**Lint-staged** too is quite simple to configure. Just add the following to your `package.json` file and you are good to go:

```
{
  /* other configurations */
  "lint-staged": {
    "**/*.{js,jsx,json}": ["eslint . --fix", "prettier --write ."]
  }
}
```

![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='20px' height='20px' viewBox='0 0 24 24' class='highlight-action crayons-icon highlight-action--fullscreen-on js-evernote-checked' data-evernote-id='506'%3e%3ctitle data-evernote-id='507' class='js-evernote-checked'%3eEnter fullscreen mode%3c/title%3e %3cpath d='M16 3h6v6h-2V5h-4V3zM2 3h6v2H4v4H2V3zm18 16v-4h2v6h-6v-2h4zM4 19h4v2H2v-6h2v4z' data-evernote-id='508' class='js-evernote-checked'%3e%3c/path%3e %3c/svg%3e)
![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='20px' height='20px' viewBox='0 0 24 24' class='highlight-action crayons-icon highlight-action--fullscreen-off js-evernote-checked' data-evernote-id='509'%3e%3ctitle data-evernote-id='510' class='js-evernote-checked'%3eExit fullscreen mode%3c/title%3e %3cpath d='M18 7h4v2h-6V3h2v4zM8 9H2V7h4V3h2v6zm10 8v4h-2v-6h6v2h-4zM8 15v6H6v-4H2v-2h6z' data-evernote-id='511' class='js-evernote-checked'%3e%3c/path%3e %3c/svg%3e)

## 5. Configure Husky

We are at the last peg of our configuration journey. Configuring **Husky** is a bit trickier than the other **configurations**. Add the following script to your `package.json` file:

```
{
  /* other configurations */
  "scripts": {
    /* other scripts */
    "configure-husky": "npx husky install && npx husky add .husky/pre-commit "npx --no-install lint-staged""
  },
  "husky": {
    "hooks": {
      "pre-commit": "lint-staged"
    }
  }
}
```

![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='20px' height='20px' viewBox='0 0 24 24' class='highlight-action crayons-icon highlight-action--fullscreen-on js-evernote-checked' data-evernote-id='579'%3e%3ctitle data-evernote-id='580' class='js-evernote-checked'%3eEnter fullscreen mode%3c/title%3e %3cpath d='M16 3h6v6h-2V5h-4V3zM2 3h6v2H4v4H2V3zm18 16v-4h2v6h-6v-2h4zM4 19h4v2H2v-6h2v4z' data-evernote-id='581' class='js-evernote-checked'%3e%3c/path%3e %3c/svg%3e)
![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='20px' height='20px' viewBox='0 0 24 24' class='highlight-action crayons-icon highlight-action--fullscreen-off js-evernote-checked' data-evernote-id='582'%3e%3ctitle data-evernote-id='583' class='js-evernote-checked'%3eExit fullscreen mode%3c/title%3e %3cpath d='M18 7h4v2h-6V3h2v4zM8 9H2V7h4V3h2v6zm10 8v4h-2v-6h6v2h-4zM8 15v6H6v-4H2v-2h6z' data-evernote-id='584' class='js-evernote-checked'%3e%3c/path%3e %3c/svg%3e)

Run the `configure-husky` script to install **Husky** and connect it to the `pre-commit` hook:

```
npm run configure-husky
```

![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='20px' height='20px' viewBox='0 0 24 24' class='highlight-action crayons-icon highlight-action--fullscreen-on js-evernote-checked' data-evernote-id='595'%3e%3ctitle data-evernote-id='596' class='js-evernote-checked'%3eEnter fullscreen mode%3c/title%3e %3cpath d='M16 3h6v6h-2V5h-4V3zM2 3h6v2H4v4H2V3zm18 16v-4h2v6h-6v-2h4zM4 19h4v2H2v-6h2v4z' data-evernote-id='597' class='js-evernote-checked'%3e%3c/path%3e %3c/svg%3e)
![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='20px' height='20px' viewBox='0 0 24 24' class='highlight-action crayons-icon highlight-action--fullscreen-off js-evernote-checked' data-evernote-id='598'%3e%3ctitle data-evernote-id='599' class='js-evernote-checked'%3eExit fullscreen mode%3c/title%3e %3cpath d='M18 7h4v2h-6V3h2v4zM8 9H2V7h4V3h2v6zm10 8v4h-2v-6h6v2h-4zM8 15v6H6v-4H2v-2h6z' data-evernote-id='600' class='js-evernote-checked'%3e%3c/path%3e %3c/svg%3e)

You are now set! Let's try `committing` some changes

[![p2zch9zfse2qzv1c957f.PNG](dev-to--automatically-format-code-on-git-commit-husky-eslint-prettie/d654b138bd1dcdc1aa233217d306f883.png)](https://res.cloudinary.com/practicaldev/image/fetch/s--6diOu2n0--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://dev-to-uploads.s3.amazonaws.com/uploads/articles/p2zch9zfse2qzv1c957f.PNG)

**BINGO! IT WORKS!**

From now on, maintaining a **consistent code style** in your project will be a breeze.

**Happy Developing!**

Research says, **writing down your goals on pen & paper** makes you **21%** to **39%** more likely to achieve them. Check out these notebooks and journals to **make the journey of achieving your dreams easier**: <https://www.amazon.com/dp/B09VFRWBH9>

# Thanks for reading

Need a **Top Rated Front-End Development Freelancer** to chop away your development woes? Contact me on [Upwork](https://www.upwork.com/o/profiles/users/~01c12e516ee1d35044/)

Want to see what I am working on? Check out my [Personal Website](https://tapajyoti-bose.vercel.app/) and [GitHub](https://github.com/ruppysuppy)

Want to connect? Reach out to me on [LinkedIn](https://www.linkedin.com/in/tapajyoti-bose/)

I am a freelancer who will start off as a **Digital Nomad** in mid-2022. Want to catch the journey? Follow me on [Instagram](https://www.instagram.com/tapajyotib/)

Follow my blogs for **Weekly new Tidbits** on [Dev](https://dev.to/ruppysuppy)

**FAQ**

These are a few commonly asked questions I get. So, I hope this **FAQ** section solves your issues.

1. **I am a beginner, how should I learn Front-End Web Dev?**  
   Look into the following articles:

   1. [Front End Development Roadmap](https://dev.to/ruppysuppy/front-end-developer-roadmap-zero-to-hero-4pkf)
   2. [Front End Project Ideas](https://dev.to/ruppysuppy/5-projects-to-master-front-end-development-57p)

## Discussion (2)

![cc5f4526-0872-4ee6-b0b3-6dfaad5eccea.jpeg](dev-to--automatically-format-code-on-git-commit-husky-eslint-prettie/2fe4e69336215c91df3a3dadf710cb6c.jpeg)

![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24' role='img' aria-labelledby='a73qo3a55fz4mz2xymwwrwig25i9upul' class='crayons-icon expanded js-evernote-checked' data-evernote-id='125'%3e%3ctitle id='a73qo3a55fz4mz2xymwwrwig25i9upul' data-evernote-id='685' class='js-evernote-checked'%3eCollapse%3c/title%3e %3cpath d='M12 10.677L8 6.935 9 6l3 2.807L15 6l1 .935-4 3.742zm0 4.517L9 18l-1-.935 4-3.742 4 3.742-1 .934-3-2.805z' data-evernote-id='686' class='js-evernote-checked'%3e%3c/path%3e %3c/svg%3e)
![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24' role='img' aria-labelledby='amzyme0z27xerptg9aiscbp3e77os9kd' class='crayons-icon collapsed js-evernote-checked' data-evernote-id='127'%3e%3ctitle id='amzyme0z27xerptg9aiscbp3e77os9kd' data-evernote-id='687' class='js-evernote-checked'%3eExpand%3c/title%3e %3cpath d='M12 18l-4-3.771 1-.943 3 2.829 3-2.829 1 .943L12 18zm0-10.115l-3 2.829-1-.943L12 6l4 3.771-1 .942-3-2.828z' data-evernote-id='688' class='js-evernote-checked'%3e%3c/path%3e %3c/svg%3e)

[![df0ec9c8-26e5-4c1d-a1c8-f3a1ff53d924.png](dev-to--automatically-format-code-on-git-commit-husky-eslint-prettie/a38efee8f55ad7bcd5d3ceb2874c937e.png)](https://dev.to/aviavinav)

•
[Mar 14](https://dev.to/aviavinav/comment/1mlh4)

Amazing article! I was wanting to implement this in my projects, didn't know how to and then I found this.

[![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' role='img' aria-labelledby='a8o1vrwhhn5mes4xtlzj3sullesty311' class='crayons-icon reaction-icon not-reacted js-evernote-checked' data-evernote-id='67'%3e%3ctitle id='a8o1vrwhhn5mes4xtlzj3sullesty311' data-evernote-id='729' class='js-evernote-checked'%3eComment button%3c/title%3e%3cpath d='M10.5 5h3a6 6 0 110 12v2.625c-3.75-1.5-9-3.75-9-8.625a6 6 0 016-6zM12 15.5h1.5a4.501 4.501 0 001.722-8.657A4.5 4.5 0 0013.5 6.5h-3A4.5 4.5 0 006 11c0 2.707 1.846 4.475 6 6.36V15.5z' data-evernote-id='730' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)
Reply](https://dev.to/ruppysuppy/automatically-format-your-code-on-git-commit-using-husky-eslint-prettier-in-9-minutes-45eg#/ruppysuppy/automatically-format-your-code-on-git-commit-using-husky-eslint-prettier-in-9-minutes-45eg/comments/new/1mlh4)

![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24' role='img' aria-labelledby='atunnvk2qm2bfg4cu08wjnswuzffii7z' class='crayons-icon expanded js-evernote-checked' data-evernote-id='126'%3e%3ctitle id='atunnvk2qm2bfg4cu08wjnswuzffii7z' data-evernote-id='732' class='js-evernote-checked'%3eCollapse%3c/title%3e %3cpath d='M12 10.677L8 6.935 9 6l3 2.807L15 6l1 .935-4 3.742zm0 4.517L9 18l-1-.935 4-3.742 4 3.742-1 .934-3-2.805z' data-evernote-id='733' class='js-evernote-checked'%3e%3c/path%3e %3c/svg%3e)
![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24' role='img' aria-labelledby='afss96tij8jc1i2vpywx7of0ygqb4nf3' class='crayons-icon collapsed js-evernote-checked' data-evernote-id='128'%3e%3ctitle id='afss96tij8jc1i2vpywx7of0ygqb4nf3' data-evernote-id='734' class='js-evernote-checked'%3eExpand%3c/title%3e %3cpath d='M12 18l-4-3.771 1-.943 3 2.829 3-2.829 1 .943L12 18zm0-10.115l-3 2.829-1-.943L12 6l4 3.771-1 .942-3-2.828z' data-evernote-id='735' class='js-evernote-checked'%3e%3c/path%3e %3c/svg%3e)

[![280c8527-9b9c-420b-9d09-f9b69d16fc3b.png](dev-to--automatically-format-code-on-git-commit-husky-eslint-prettie/e75a64715207974103a1c35beb9ee99c.png)](https://dev.to/darkwiiplayer)

•
[Mar 16](https://dev.to/darkwiiplayer/comment/1mmm1)

Tried something similar using [git hooks](https://github.com/DarkWiiPlayer/darkrc/blob/master/githooks/pre-commit) once, but it's a bit more complicated to set up

[![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' role='img' aria-labelledby='a1zotgtr04a9jmg488gmr1kzj7zncxfo' class='crayons-icon reaction-icon not-reacted js-evernote-checked' data-evernote-id='74'%3e%3ctitle id='a1zotgtr04a9jmg488gmr1kzj7zncxfo' data-evernote-id='777' class='js-evernote-checked'%3eComment button%3c/title%3e%3cpath d='M10.5 5h3a6 6 0 110 12v2.625c-3.75-1.5-9-3.75-9-8.625a6 6 0 016-6zM12 15.5h1.5a4.501 4.501 0 001.722-8.657A4.5 4.5 0 0013.5 6.5h-3A4.5 4.5 0 006 11c0 2.707 1.846 4.475 6 6.36V15.5z' data-evernote-id='778' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)
Reply](https://dev.to/ruppysuppy/automatically-format-your-code-on-git-commit-using-husky-eslint-prettier-in-9-minutes-45eg#/ruppysuppy/automatically-format-your-code-on-git-commit-using-husky-eslint-prettier-in-9-minutes-45eg/comments/new/1mmm1)

[Code of Conduct](https://dev.to/code-of-conduct)
•
[Report abuse](https://dev.to/report-abuse)
