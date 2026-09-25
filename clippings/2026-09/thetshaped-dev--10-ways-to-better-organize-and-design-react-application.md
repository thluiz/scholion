---
url: "https://thetshaped.dev/p/10-ways-organize-and-design-react-application"
captured_at: "2026-09-25T21:26:19+01:00"
title: "10 ways to better organize and design your React Application"
domain: "thetshaped-dev"
---

When building a React Application, **the way you organize and design your code has a tremendous impact**. It can either help you and your team **find things easier**, **make updates quicker**, and **better handle the app as it grows**, or make everything much worse.

It’s the same principle as with buildings. If you’ve laid the foundations and organized the building well, it can last longer and its residents will be happy. Otherwise, the building might fall.

> **Shaky foundations lead to shake results.**

1.  [Group components by Domain Responsibilities](https://thetshaped.dev/i/147475149/group-components-by-domain-responsibilities)
    
2.  [Put components into folders](https://thetshaped.dev/i/147475149/put-components-into-folders)
    
3.  [Favor Absolute Paths](https://thetshaped.dev/i/147475149/favor-absolute-paths)
    
4.  [Use a common module](https://thetshaped.dev/i/147475149/use-a-common-module)
    
5.  [Abstract external libraries and modules](https://thetshaped.dev/i/147475149/abstract-external-libraries-and-modules)
    
6.  [Manage dependencies between modules/pages](https://thetshaped.dev/i/147475149/manage-dependencies-between-modulespages)
    
7.  [Keep things as close as where they’re used (LoB)](https://thetshaped.dev/i/147475149/keep-things-as-close-as-where-theyre-used-lob)
    
8.  [Be careful with utility functions](https://thetshaped.dev/i/147475149/be-careful-with-utility-functions)
    
9.  [Be careful with business logic](https://thetshaped.dev/i/147475149/be-careful-with-business-logic)
    
10.  [Pin Dependencies](https://thetshaped.dev/i/147475149/pin-dependencies)
     

The **organization of files and folders** in a React application is **crucial for maintaining clarity and manageability**. The easier it is to navigate throughout the project, the less wasted time for developers to navigate and wonder where and how to change stuff.

**It’s important to structure files not just by technical roles but by their domain responsibilities.**

**⛔ Avoid** grouping components by technical responsibilities.

```
/src
│   ...
│
└───components
│    │   Header.js
│    │   Footer.js
│    │   ...
└───containers
│    │   InvoicesContainer.js
│    │   PaymentProfilesContainer.js
│    │   ...
└───presenters
│     │   InvoicesPresenter.js
│     │   PaymentProfilesPresenter.js
│     │   ...
│   ...
```

**✅ Prefer** grouping components by **domain responsibilities** by **pages**(routes) or **modules**(domains).

```
/src
│   ...
│
└───pages --> Actual Pages representing different parts of the app
│    └───billing
│    │    └───invoices
│    │    │   │   index.js
│    │    │   │   ...
│    │    └───payment-profiles
│    │    │   │   index.js
│    │    │   │   ...
│    │    │   ...
│    │    │   index.ts
│    └───login
│        │   index.js
│        │   ...
│   ...
```

For complex components, it’s better to organize them into separate folders where you can list their subcomponents.

**⛔ Avoid** having a single file for each component.

```
/src
│
└───components         
│   │   Accordion.ts
|   |   Alert.ts
│   │   ...
│
└───...
```

**✅ Prefer** having a single folder for each component.

```
/src
│
└───components
│   │   ...
│   └───accordion             
│   │    │   index.ts
│   │    │   ...
│   └───alert             
│       │   index.ts
│       │   types.ts
│       │   Alert.tsx
│       │   AlertTitle.tsx
│       │   Alert.stories.tsx
│       │   Alert.test.tsx
│       │   ...
│
└───...
```

[

![](https://substackcdn.com/image/fetch/$s_!MAAf!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd58ffcba-a1c8-40b3-be25-ca31024ea7d8_532x406.png)

](https://substackcdn.com/image/fetch/$s_!MAAf!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd58ffcba-a1c8-40b3-be25-ca31024ea7d8_532x406.png)

Example of how having separate folder per component.

Using the right type of paths in your project can **simplify navigation and maintenance**, especially as your project grows. **Refactoring will be much easier.**

**⛔ Avoid** using relative paths which can become hard to manage and error-prone in large projects.

```
import { formatDate } from '../../../utils';
```

**✅ Prefer** using absolute paths which improve readability and make refactoring easier.

```
import { formatDate } from '@common/utils';
```

**Common modules play a vital role in avoiding redundancy and promoting reusability across your application.**

You can store utility methods, constants, components, calculations, etc. in this common module.

**This centralization helps for better management and reuse.**

**⛔ Avoid** spreading common utilities and components across various locations in your project.

**✅ Prefer** having a dedicated common module for all generic components and utilities used across different pages or modules.

```
/src
│   ...
│
└───common
│    └───components
│    │    └───dialogs
│    │    │   │   index.js
│    │    └───forms
│    │    │   │   index.js
│    │    │   ...
│    └───hooks
│    │    │   useDialog.js
│    │    │   useForm.js
│    │    │   ...
│    └───utils
│    │    │   ...
└───pages
│    └───billing
│    │    └───invoices
│    │    │   │   index.js
│    │    │   │   ...
│   ...
```

The integration of external libraries or modules requires careful consideration to **ensure future flexibility and easier maintenance**.

Using 3rd party libraries or components directly in your project can lead to issues if the external APIs change or you want to replace the components or library with something else. Then, you’ll have to go through all the places it is being used instead of updating them only into a single place.

**Wrapping the 3rd party library or module in a custom component allows you to maintain a consistent API within your application and makes it easier to replace the module if needed in the future.**

**⛔ Avoid** direct use of 3rd party components or libraries in your project.

```
// XYZ_Component.ts (file 1)
import { Button } from 'react-bootstrap';

// ABC_Component.ts (file 2)
import { Button } from 'react-bootstrap';
```

**✅ Prefer** wrapping external modules or components in a custom component.

```
// XYZ_Component.ts (file 1)
import { Button } from '@components/ui';

// ABC_Component.ts (file 2)
import { Button } from '@components/ui';
```

Managing dependencies wisely by centralizing commonly used resources in a shared common module can significantly **enhance the code’s manageability and reusability**.

> **If something is used more than once across two or more pages and modules, consider moving it to the common module.**

Storing shared components or utilities in a common module **eliminates the need to duplicate code across different parts of the application**, making the codebase leaner and easier to maintain.

It also makes clear the dependencies per module and page.

> **The easier and faster for a developer to find a piece of code, the better.**

The principle of Locality of Behavior (LoB) suggests **organizing the codebase so that components, functions, and resources are located near where they are used within the application**. The strategy promotes a modular architecture, where **each part of the system is self-contained**.

**This improves readability and maintainability.** When developers work on a feature, they have all related code in proximity which makes it easier to understand and modify. It also **reduces the cognitive load** of tracing through distant files and modules.

```
/src
│   ...
│
└───common
│    └───components
│    │    │   ...
│    └───hooks
│    │    │   ...
│    └───utils
│    │    │   ...
└───pages
│    └───billing
│    │    └───invoices
│    │    │   │   index.js
│    │    │   │   ...
│    │    └───payment-profiles
│    │    │   │   index.js
│    │    │   │   ...
│    │    └───hooks
│    │    │   │   index.js
│    │    │   │   useInvoices.js
│    │    │   │   usePaymentProfiles.js
│    │    │   │   ...
│    │    └───utils
│    │    │   │   index.js
│    │    │   │   formatAmount.js
│    │    │   │   ...
│   ...
```

Utility functions typically handle reusable snippets of code that aren’t tied to the business rules or the application logic. They rather provide g**eneral assistance across the system**.

**Utility functions should remain pure and purpose-specific**, focusing on general tasks like formatting dates, converting data types, etc. **Mixing them with business logic like how data is processed or business-specific decisions, can make these utilities overly complex and less reusable.**

Also, business logic and rules change more often than utilities, so by separating them you will improve the overall maintainability of the code.

**⛔ Avoid** adding business logic to utils.

**✅ Prefer** extracting business logic into separate functions.

**Integrating business logic directly into UI components can lead to problems like harder-to-test code and poor separation of concerns.** This can also lead to bulky components that are difficult to manage and update.

In React, **custom hooks are a great tool for abstracting business logic from components**. By using hooks, you can encapsulate business logic and keep your UI clean and focused on rendering.

This separation not only **makes your components more modular and easier to manage but also enhances reusability and maintainability**.

**⛔ Avoid** mixing business logic with UI.

**✅ Prefer** separating business logic from UI. Use custom hooks.

When managing a JavaScript project, your **package.json** file plays a crucial role. It defines your project’s dependencies - the external packages your project relies on to function. **Pinning these dependencies refers to specifying exact versions of these packages rather than allowing version ranges.**

**Pinning dependencies ensures that everyone working on the projects**, as well as the production environment, **uses the exact same version of each package**, **eliminating discrepancies** that might occur due to minor updates or patches.

**⛔ Avoid** using version ranges in your package.json.

```
{
  "dependencies": {
    "express": "^4.17.1",
    "react": ">=16.8.0"
  }
}
```

**✅ Prefer** using exact versions in your `package.json`.

```
{
  "dependencies": {
    "express": "4.17.1",
    "react": "16.8.0"
  }
}
```

*   **[How Stripe Prevents Double Payment Using Idempotent API](https://newsletter.systemdesign.one/p/idempotent-api?r=643nm&utm_campaign=post&utm_medium=web)** by [Neo Kim](https://open.substack.com/users/135589200-neo-kim?utm_source=mentions)
    
*   **[How to say "No" and win back your time as a software engineer](https://read.highgrowthengineer.com/p/how-to-say-no-and-win-back-your-time?r=643nm&utm_campaign=post&utm_medium=web)** by [Jordan Cutler](https://open.substack.com/users/58854493-jordan-cutler?utm_source=mentions)
    
*   **[How to propose an impactful improvement to the codebase and own the implementation](https://newsletter.eng-leadership.com/p/how-to-propose-an-impactful-improvement?r=643nm&utm_campaign=post&utm_medium=web)** by [Gregor Ojstersek](https://open.substack.com/users/106098672-gregor-ojstersek?utm_source=mentions)
    
*   **["20% for tech debt" doesn't work](https://open.substack.com/pub/zaidesanton/p/how-to-implement-20-for-tech-debt-?r=643nm&utm_campaign=post&utm_medium=web)** by [Anton Zaides](https://open.substack.com/users/121956618-anton-zaides?utm_source=mentions)
    
*   **[9 Things I Wish I Knew When I Started Programming](https://blog.algomaster.io/p/things-i-wish-i-knew-when-i-started-programming?r=643nm&utm_campaign=post&utm_medium=web)** by [Ashish Pratap Singh](https://open.substack.com/users/83602743-ashish-pratap-singh?utm_source=mentions)
    

[

![15 React Component Principles & Best Practices for Better Software Architecture & Design](https://substackcdn.com/image/fetch/$s_!B8D2!,w_140,h_140,c_fill,f_auto,q_auto:good,fl_progressive:steep,g_auto/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2d896123-25da-4d25-aeb4-65b4447c76f5_1456x1048.png)

](https://thetshaped.dev/p/15-react-component-principles-for-better-design)

[

![GraphQL Intro 101 (part 1)](https://substackcdn.com/image/fetch/$s_!WOrE!,w_140,h_140,c_fill,f_auto,q_auto:good,fl_progressive:steep,g_auto/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fab4c8a87-7221-44d9-9baa-59b7014456ba_1456x1048.png)

](https://thetshaped.dev/p/graphql-intro-101-part-1)

[

![Comparison Guide: Bootstrap vs. Tailwind CSS. When and What to choose?](https://substackcdn.com/image/fetch/$s_!aCH6!,w_140,h_140,c_fill,f_auto,q_auto:good,fl_progressive:steep,g_auto/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3f7bf69d-ab44-48fb-a7ef-c860a495618c_1456x1048.png)

](https://thetshaped.dev/p/comparison-guide-bootstrap-vs-tailwindcss)

You can find me on **[LinkedIn](https://www.linkedin.com/in/petarivanovv9/)** or **[Twitter](https://twitter.com/petarivanovv9)**.

This newsletter is funded by paid subscriptions from readers like yourself.

If you aren’t already, consider becoming a paid subscriber to receive the full experience!

Think of it as buying me a coffee twice a month, with the bonus that you also get all my products for FREE.

[Check the benefits of the paid plan](https://thetshaped.dev/about#%C2%A7why-subscribe)

You can also hit the like ❤️ button at the bottom of this email to help support me or share this with a friend to [get referral rewards](https://thetshaped.dev/?r=643nm). It helps me a ton!
