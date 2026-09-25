---
url: "https://thetshaped.dev/p/pin-your-dependencies-in-packagejson"
captured_at: "2026-09-25T21:34:14+01:00"
title: "Pin your dependencies in package.json"
domain: "thetshaped-dev"
---

When you manage a JavaScript project, especially one using Node.js, npm, or yarn, your `package.json` plays a crucial role.

Your `package.json` defines your project’s dependencies - the external packages and libraries your project relies on to work.

Properly managing these dependencies ensures the project runs consistently and reliably across different environments.

In your `package.json` you can have **4 types of versioning for your dependencies**:

It allows changes that do not modify the left-most non-zero digit in the version number, introducing minor updates and patches automatically.

Example:

```
{
  "name": "https://thetshaped.dev/",
  "version": "1.0",
  "dependencies": {
    "react": "^18.2.0"
  }
}
```

For example, the next time you run `npm install`, the `react` version could resolve to `18.3.0` or `18.2.3`.

It allows changes that update only the patch version automatically.

Example:

```
{
  "name": "https://thetshaped.dev/",
  "version": "1.0",
  "dependencies": {
    "react": "~18.2.0"
  }
}
```

For example, the next time you run `npm install`, the `react` version could resolve to `18.2.3`.

It allows changes that update the major version automatically.

Example:

```
{
  "name": "https://thetshaped.dev/",
  "version": "1.0",
  "dependencies": {
    "react": ">=18.2.0"
  }
}
```

For example, the next time you run `npm install`, the `react` version could resolve to `19.0.0`.

Example:

```
{
  "name": "https://thetshaped.dev/",
  "version": "1.0",
  "dependencies": {
    "react": "18.2.0"
  }
}
```

For example, the next time you run `npm install`, the `react` version will resolve to `18.2.0` which is the same version.

Pinning dependencies means specifying exact versions of dependencies instead of using version ranges like \`~\`, \`~\`, or \`>=\`.

This practice is key to maintaining consistency and reliability across all environments.

It ensures everyone is working with the exact same modules.

*   **Consistency** - pinning dependencies prevents issues like “it works on my machine” by ensuring every environment uses identical dependency versions.  
    For example, specifying `"react": "18.2.0"` instead of `"react": "^18.2.0"` guarantees that the same react version will be installed everywhere.
    
*   **Reliability** - by using exact/pinned versions, you will have fewer surprises from updates that introduces bugs and break the functionality.
    
*   **Security** - pinning versions helps avoid automatic updates to new versions that may have security vulnerabilities or compromised code.
    

*   **Maintenance Overhead** - regularly updating dependencies to include new features or fixes of bugs could be time-consuming but it is necessary for the project’s health and stability.
    
*   **Outdated Packages** - if the packages are not reviewed and updated regularly, you might miss critical enhancements or security patches.
    

Always specify exact versions in `package.json` to avoid any ambiguities.

You can integrate automation tools like _[Renovate](https://docs.renovatebot.com/)_ or _[Dependabot](https://github.com/dependabot)_ into your project to help keep your dependencies up-to-date by automatically creating pull requests for each update.

These PRs can be configured to be merged automatically if all checks pass. That’s why it’s important to have a good test coverage to ensure no bugs are introduced.

Use tools like _[npm audit](https://docs.npmjs.com/cli/v10/commands/npm-audit/)_ or _[Snyk](https://snyk.io/)_ to automatically detect vulnerabilities and suggest or event apply patches without manual oversight.

By using `package-lock.json` or `yarn.lock` files you enforce the use of the exact dependencies versions recorded during the last successful installation. This ensures consistency and reliability.

*   Pinning dependencies in `package.json` is crucial for the project’s health, stability, consistency, and security.
    
*   Use exact versions (ex: `"react": "18.2.0"`).
    
*   Regularly review and update your dependencies in `package.json`.
    
*   Use automation tools like _[Renovate](https://docs.renovatebot.com/)_, _[Dependabot](https://github.com/dependabot), [npm audit](https://docs.npmjs.com/cli/v10/commands/npm-audit/)_ or _[Snyk](https://snyk.io/),_ in your project to help keep dependencies up-to-date and avoid security vulnerabilities.
    

You can find me on **[LinkedIn](https://www.linkedin.com/in/petarivanovv9/)** or **[Twitter](https://twitter.com/petarivanovv9)**.

This newsletter is funded by paid subscriptions from readers like yourself.

If you aren’t already, consider becoming a paid subscriber to receive the full experience!

Think of it as buying me a coffee twice a month, with the bonus that you also get all my products for FREE.

[Check the benefits of the paid plan](https://thetshaped.dev/about#%C2%A7why-subscribe)

You can also hit the like ❤️ button at the bottom to help support me or share this with a friend to [get referral rewards](https://thetshaped.dev/?r=643nm). It helps me a lot! 🙏

[

![10 ways to better organize and design your React Application](https://substackcdn.com/image/fetch/$s_!cZEv!,w_140,h_140,c_fill,f_auto,q_auto:good,fl_progressive:steep,g_auto/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F51e272ef-694f-439a-8159-49e7ffabe109_600x400.png)

](https://thetshaped.dev/p/10-ways-organize-and-design-react-application)

[

![How SoundCloud scaled its Architecture using BFF and Value-Added Services?](https://substackcdn.com/image/fetch/$s_!-Ky9!,w_140,h_140,c_fill,f_auto,q_auto:good,fl_progressive:steep,g_auto/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5d1b89d3-af3c-4971-8a84-02f59ac563e8_600x400.png)

](https://thetshaped.dev/p/how-soundcloud-scaled-its-architecture)

[

![State Management & Data Fetching Libraries in React](https://substackcdn.com/image/fetch/$s_!rifd!,w_140,h_140,c_fill,f_auto,q_auto:good,fl_progressive:steep,g_auto/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fcf07e1ef-b72b-4eb4-88c3-216b72c40359_1456x1048.png)

](https://thetshaped.dev/p/state-management-and-data-fetching-libraries)

*   **[How Facebook Scaled Live Video to a Billion Users](https://newsletter.systemdesign.one/p/live-streaming-architecture?r=643nm&utm_campaign=post&utm_medium=web)** by [Neo Kim](https://open.substack.com/users/135589200-neo-kim?utm_source=mentions)
    
*   **[The 3 Big Mistakes That Almost Cost Me My Promotion (And How You Can Avoid Them)](https://read.highgrowthengineer.com/p/3-mistakes-almost-cost-me-my-promotion?r=643nm&utm_campaign=post&utm_medium=web)** by [Jordan Cutler](https://open.substack.com/users/58854493-jordan-cutler?utm_source=mentions)
    
*   **[Engineer’s guide to convincing your Product Manager to prioritize technical debt](https://newsletter.eng-leadership.com/p/engineers-guide-to-convincing-your?r=643nm&utm_campaign=post&utm_medium=web)** by [Gregor Ojstersek](https://open.substack.com/users/106098672-gregor-ojstersek?utm_source=mentions)
    
*   **[Build Your Credibility As You Grow](https://www.leadership-letters.com/p/build-your-credibility-as-you-grow?r=643nm&utm_campaign=post&utm_medium=web)** by [Akash Mukherjee](https://open.substack.com/users/197891722-akash-mukherjee?utm_source=mentions)
    
*   **[Keep is Simple, Software Engineer (KISS)](https://open.substack.com/pub/thehustlingengineer/p/keep-is-simple-software-engineer?r=643nm&utm_campaign=post&utm_medium=web)** by [Hemant Pandey](https://open.substack.com/users/58770480-hemant-pandey?utm_source=mentions)
