---
url: "https://thetshaped.dev/p/4-tools-to-supercharge-your-jest-testing-increase-productivity?ref=dailydev"
captured_at: "2026-09-25T21:26:16+01:00"
title: "4 tools to supercharge your Jest Testing and increase your productivity while testing"
domain: "thetshaped-dev"
---

The importance of having tests in place is undeniable.

However, the importance of having a fast feedback loop from your tests is usually neglected.

> **A fast feedback loop from tests helps developers to quickly identify and fix issues.**

It improves the overall throughput of a developer.

The first thing I do, when I start a new project or join an older one, is to add a `jest watch` command inside the `package.json`.

It can look something like:

```
{
  ...
  "scripts": {
    ...
    "test:watch": "jest --watch --verbose",
    ...
  },
  ...
}
```

You can learn more about the `--watch` and `--verbose` jest flags on the official **[Jest CLI Documentation](https://jestjs.io/docs/cli)**.

When you run the `test:watch` command, it provides a real-time feedback and detailed output of your tests.

It will automatically rerun tests related to the changed files and speed up the feedback loop from your tests.

Usually, when I start refactoring a piece of code or start working on a new feature, I run the `test:watch` command and monitor how the changes impact the tests and vice versa.

`jest-watch-typeahead` is a plugin to speed up your testing workflow.

**It allows you to filter tests by file name and test name which makes it easier to run specific tests while developing.**

The tool is very useful for large projects where you have hundreds of tests.

Instead of remembering specific filenames, with the `jest-watch-typeahead` plugin you can quickly find and run the test you need.

[

![](https://substackcdn.com/image/fetch/$s_!Uaf2!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fee627c84-e4eb-4c55-8c80-e6aad636ed48_863x399.gif)

](https://substackcdn.com/image/fetch/$s_!Uaf2!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fee627c84-e4eb-4c55-8c80-e6aad636ed48_863x399.gif)

Source: https://github.com/jest-community/jest-watch-typeahead

You can find more info about the plugin and its installation **[here](https://github.com/jest-community/jest-watch-typeahead)**.

I’ve seen many codebases where several jest matchers are used to assert for something.

For example:

```
expect(<something>).toHaveBeenCalledTimes(1);
expect(<something>).toHaveBeenCalledWith(<xyz>);
```

You can enhance the capabilities of Jest’s default matchers by adding custom jest matchers.

`jest-extended` is a great package adding a set of additional matchers to make assertions more expressive and code more readable.

I’ve personally used the following custom matchers:

*   `toHaveBeenCalledExactlyOnceWith`
    

```
expect(<something>).toHaveBeenCalledExactlyOnceWith(<xyz>);
```

*   `toThrowWithMessage`
    

```
await expect(
  register.execute(registerInput),
).rejects.toThrowWithMessage(
  ValidationError,
  `Must contain 8-64 characters, 1 uppercase, 1 lowercase,...`,
);
```

*   `toHaveBeenCalledAfter`
    

```
expect(connector.verifyMfa).toHaveBeenCalledExactlyOnceWith(
    'at',
    'abc123',
);
expect(connector.enableMfa).toHaveBeenCalledExactlyOnceWith('at');
expect(connector.enableMfa).toHaveBeenCalledAfter(connector.verifyMfa);
```

**[Here](https://jest-extended.jestcommunity.dev/docs/matchers)** is the complete set of the additional matchers from `jest-extended`.

Sometimes we add `console.log()` , `console.error()`, etc. while debugging, testing or even developing new stuff.

We can later forget to remove these logs and pollute the console.

In a large codebase, we can end up with the test output overloaded by a lot of errors, warnings, etc.

We can automate that through the `jest-fail-on-console` utility and make our jest tests fail when `console.error()`, `console.warn()`, etc. are used.

It’s crucial to keep the console clean because it helps us identify real issues quickly.

You can learn more about the package **[here](https://github.com/ValentinH/jest-fail-on-console)**.

1.  Add a `"test:watch": "jest --watch --verbose"` command inside your package.json to speed up the feedback loop from your tests.
    
2.  Add a `jest-watch-typeahead` plugin to additionally speed up your testing workflow.
    
3.  Consider adding additional custom jest matchers if needed to make assertions more expressive and code more readable through `jest-extended`.
    
4.  Optionally, add `jest-fail-on-console` to prevent adding code with `console` statements and have a clear console output.
    

You can find me on **[LinkedIn](https://www.linkedin.com/in/petarivanovv9/)** or **[Twitter](https://twitter.com/petarivanovv9)**.

This newsletter is funded by paid subscriptions from readers like yourself.

If you aren’t already, consider becoming a paid subscriber to receive the full experience!

Think of it as buying me a coffee twice a month, with the bonus that you also get all my products for FREE.

[Check the benefits of the paid plan](https://thetshaped.dev/about#%C2%A7why-subscribe)

You can also hit the like ❤️ button at the bottom to help support me or share this with a friend to [get referral rewards](https://thetshaped.dev/?r=643nm). It helps me a lot! 🙏

*   **[The Resume Ghostbuster course](https://www.topengineermethod.com/the-resume-ghostbuster)** from **[Taha Hussain](https://www.linkedin.com/in/tahahussain/overlay/about-this-profile/)**, an Engineering Career Coach. You can claim a **85% discount** until Sep 30th.  
    It’s $40 off making it **$7 only**. Code: **NEWLIFE** 🎉 🎉 🎉
    

*   **[How Amazon Lambda Works](https://newsletter.systemdesign.one/p/how-does-aws-lambda-work?r=643nm&utm_campaign=post&utm_medium=web)** by [Neo Kim](https://open.substack.com/users/135589200-neo-kim?utm_source=mentions)
    
*   **[My Tech Promotion Algorithm](https://read.highgrowthengineer.com/p/my-tech-promotion-algorithm?r=643nm&utm_campaign=post&utm_medium=web)** by [Jordan Cutler](https://open.substack.com/users/58854493-jordan-cutler?utm_source=mentions)
    
*   **[The importance of having a career growth plan in the engineering industry](https://newsletter.eng-leadership.com/p/the-importance-of-having-a-career)** by [Gregor Ojstersek](https://open.substack.com/users/106098672-gregor-ojstersek?utm_source=mentions) and [Omar Halabieh](https://open.substack.com/users/161961759-omar-halabieh?utm_source=mentions)
    
*   **[Hexagonal Architecture with TDD](https://craftbettersoftware.com/p/hexagonal-architecture-with-tdd?r=643nm&utm_campaign=post&utm_medium=web)** by [Daniel Moka](https://open.substack.com/users/5505375-daniel-moka?utm_source=mentions)
    
*   **[Message Queues & Message Brokers](https://newsletter.systemdesigncodex.com/p/message-queues-and-message-brokers?r=643nm&utm_campaign=post&utm_medium=web)** by [Saurabh Dashora](https://open.substack.com/users/97484183-saurabh-dashora?utm_source=mentions)
