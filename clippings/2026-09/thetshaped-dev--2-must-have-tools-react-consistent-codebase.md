---
url: "https://thetshaped.dev/p/must-have-tools-in-your-react-project-consistent-codebase-prettier-eslint"
captured_at: "2026-09-25T21:33:42+01:00"
title: "2 must-have tools in your React Project for having a consistent codebase"
domain: "thetshaped-dev"
---

I’ve seen many consistent and non-consistent codebases.

I can’t remember the number of times I cried when I touched something in a non-consistent codebase.

It’s a nightmare you want to avoid.

Code consistency is a **practice embraced by great software developers** and engineers.

**If you take your craft seriously, you must have a consistent codebase.**

Make yourself and your teammates a favor.

**Consistency in the codebase** is a **fundamental aspect of effective collaboration and maintainability**.

The consistent codebase:

*   **Enhances readability** - developers can read and navigate throughout the code much easier which helps for faster development
    
*   **Simplifies onboarding of new team members** - when the codebase follows a consistent pattern, styling, and formatting, it’s much easier for new engineers to grasp it
    
*   **Streamlines code reviews** - reviewers can focus on the logic and business requirements, instead of leaving unnecessary comments related to the code styling and formatting
    

_[Prettier](https://prettier.io/)_ and _[Dprint](https://dprint.dev/)_ are two of the most popular code formatting tools in the JavaScript ecosystem.

They help enforce consistent styling across the codebase by parsing the code and “rewriting” it with their own rules.

You can either apply the tool's already present rules, integrate open-sourced ones, write your own custom rules, or even combine all four options.

These tools give you a lot of flexibility, which is great, and fit 99% of the code formatting cases in a codebase.

_**Note:** My personal preference is [Prettier](https://prettier.io/) since it’s largely adopted, there’re a lot of plugins, and the community is bigger than [Dprint](https://dprint.dev/). However, in one of the latest projects we adopted Dprint because it had better performance._

Whether you choose _[Prettier](https://prettier.io/)_ or _[Dprint](https://dprint.dev/)_, it will be a step forward to a more consistent codebase and project. Swapping the tools is a no-brainer.

> **💡Hint:** You can configure your editor to run and apply the formatting on auto-save.

```
// Before
function Component(){return <div><h1>Without code formatting!</h1></div>}

// After
function Component() {
  return (
    <div>
      <h1>With code formatting!</h1>
    </div>
  );
}
```

_[ESLint](https://eslint.org/)_ is the most popular linting tool for JavaScript and JSX in the JavaScript community.

_[ESLint](https://eslint.org/)_ helps to detect problematic patterns and areas in your code that don’t follow certain rules, styles, and guidelines.

Similar to _[Prettier](https://prettier.io/)_ and _[Dprint](https://dprint.dev/)_, _[ESLint](https://eslint.org/)_ is highly customizable and flexible to fit almost every project and style guide.

You can also write your own ESLint rule, so basically, you can cover 100% of the cases.

Keep in mind that some rules might be applied automatically while others will appear as warnings/errors inside the IDE and you will have to fix them by yourself.

> 💡 **Hint:** You can configure your editor to run and apply the linting on auto-save.

```
import React, { useState, useEffect } from 'react';

function UserProfile({ userId }) {
  if (userId) {
    const [userData, setUserData] = useState(null);

    useEffect(() => {
      fetch(`/api/users/${userId}`)
        .then(response => response.json())
        .then(data => setUserData(data));
    }, [userId]);

    return <div>{userData ? userData.name : 'Loading...'}</div>;
  } else {
    return <div>No User ID Provided</div>;
  }
}

export default UserProfile;
```

In the example from above, we violate the _[rules-of-hooks](https://react.dev/reference/rules/rules-of-hooks)_ rule.

ESLint gave us a warning that something in our code was not correct.

```
// After applying the `rules-of-hooks` eslint rule

import React, { useState, useEffect } from 'react';

function UserProfile({ userId }) {
  const [userData, setUserData] = useState(null);

  useEffect(() => {
    if (userId) {
      fetch(`/api/users/${userId}`)
        .then(response => response.json())
        .then(data => setUserData(data));
    }
  }, [userId]);

  if (userId) {
    return <div>{userData ? userData.name : 'Loading...'}</div>;
  } else {
    return <div>No User ID Provided</div>;
  }
}

export default UserProfile;
```

By integrating both a **formatter and a linter into your React project**, you ensure the **code is consistently formatted and follows the best practices and guidelines**.

**Automating that will improve the overall Developer Experience and developer’s throughput.**

In my experience, these tools are an **irreplaceable part of my toolbox in every project** I start or join.

*   **Stick to the standard configurations.** Usually, the standard set of rules is just enough. They’re a good starting point.
    
*   **Keep tools updated.** This way you will leverage the newly added fixes and improvements of the tools.
    
*   **Introduce new rules and guidelines gradually.** Don’t worry about introducing a new rule later when you see a potential for an improvement.
    
*   **Enforce style guides and practices through rules.** Don’t rely on people to follow them. Automate this process. Keep everyone on the same page.
    
*   **Add a formatting and styling check inside your CI/CD.**
    

The T-Shaped Dev is a reader-supported publication. To receive new posts and support my work, consider becoming a free or paid subscriber.

*   Consistent codebase is crucial for better readability, maintainability, and DX.
    
*   Use a code formatting tool like Prettier or Dprint for a more consistent codebase.
    
*   Use a code quality and code styling tool like ESLint for a more consistent and error-prone codebase.
    
*   Automate whatever you can. Don’t rely on people to follow rules and guidelines manually.
    
*   Make these steps part of your CI/CD so no “bad” code enters production.
    

You can find me on **[LinkedIn](https://www.linkedin.com/in/petarivanovv9/)** or **[Twitter](https://twitter.com/petarivanovv9)**.

I share daily practical tips to level up your skills and become a better engineer.

_Thank you for being a great supporter, reader, and for your help in growing to 12.7K+ subscribers this week 🙏_

This newsletter is funded by paid subscriptions from readers like yourself.

If you aren’t already, consider becoming a paid subscriber to receive the full experience!

Think of it as buying me a coffee twice a month, with the bonus that you also get all my templates and products for FREE.

[Check the benefits of the paid plan](https://thetshaped.dev/about#%C2%A7why-subscribe)

_You can also hit the like ❤️ button at the bottom to help support me or share this with a friend to [get referral rewards](https://thetshaped.dev/?r=643nm). It helps me a lot! 🙏_

*   **[How Amazon S3 Works](https://newsletter.systemdesign.one/p/s3-architecture?r=643nm&utm_campaign=post&utm_medium=web)** by [Neo Kim](https://open.substack.com/users/135589200-neo-kim?utm_source=mentions)
    
*   **[How to use engineering metrics for the success of engineers and teams](https://newsletter.eng-leadership.com/p/how-to-use-engineering-metrics-for?r=643nm&utm_campaign=post&utm_medium=web)** by [Gregor Ojstersek](https://open.substack.com/users/106098672-gregor-ojstersek?utm_source=mentions)
    
*   **[Eventual Consistency is Tricky](https://newsletter.systemdesigncodex.com/p/eventual-consistency-is-tricky?r=643nm&utm_campaign=post&utm_medium=web)** by [Saurabh Dashora](https://open.substack.com/users/97484183-saurabh-dashora?utm_source=mentions)
    
*   **[How To Create Your Own Luck](https://read.developingskills.fyi/p/how-to-create-your-own-luck?r=643nm&utm_campaign=post&utm_medium=web)** by [John Crickett](https://open.substack.com/users/27801024-john-crickett?utm_source=mentions)
    
*   **[Don’t Start Coding Yet: Here’s What Great Engineers Do First](https://strategizeyourcareer.com/p/dont-start-coding-yet-heres-what-great-engineers-do-first?r=643nm&utm_campaign=post&utm_medium=web)** by [Fran Soto](https://open.substack.com/users/170998285-fran-soto?utm_source=mentions)
    
*   **[How to Stay Calm Under Pressure?](https://newsletter.techleadmentor.com/p/how-to-stay-calm-under-pressure?r=643nm&utm_campaign=post&utm_medium=web)** by [Raviraj Achar](https://open.substack.com/users/167123667-raviraj-achar?utm_source=mentions)
