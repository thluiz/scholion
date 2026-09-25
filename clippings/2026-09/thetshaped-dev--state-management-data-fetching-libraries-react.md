---
url: "https://thetshaped.dev/p/state-management-and-data-fetching-libraries"
captured_at: "2026-09-25T21:29:38+01:00"
title: "State Management & Data Fetching Libraries in React"
domain: "thetshaped-dev"
---

State Management and Data Fetching are 2 of the most important things when building a React Application. Doing it right from the beginning is crucial.

Many people jump into using external libraries to solve these 2 big challenges from the beginning and later realize it’s hard to manage and maintain the project. This shouldn’t be the case.

External tools and libraries should be used carefully.

In today’s article, I want to share my experience and thoughts on using and not using external libraries for state management and data fetching.

*   Prefer using React’s built-in tools for managing state.
    
*   Don’t add unnecessary complexity. Keep things as simple as possible.
    
*   Opt-in for 3rd party state management libraries when the state management becomes hard to manage, update, maintain, and follow.
    
*   Use data fetching libraries.
    

State management libraries help **manage and centralize state** in React applications, which can grow complex as the application scales. However, as they might help, they can also add **extra complexity** which might not be necessary and beneficial.

*   **Small to medium-sized applications.** React’s built-in hooks like **useState**, **useReducer**, and **Context API** are often **sufficient for smaller applications** where **state management is simple**.
    
*   **Simple UI or state logic.**
    
*   **Short-term projects or prototypes**.
    

*   **Complex state logic across multiple components.** When various components rely on and modify the same state, a central state management solution can **simplify the flow and update of data**.
    
*   **Large applications.** As the application grows and many people contribute, you might want to add a **standard way of managing the state**. Since you’ll be using one tool, everyone will describe their logic with it.
    

> 💡 _My advice:_ **Always start with React’s built-in tools for state management and evolve when necessary.**  
> **Don’t add unnecessary complexity. Keep things as simple as possible.**

Keep in mind that there are no signals when you should start using a state management library or not.

Once you opt-in to using a state management library, the application’s structure and logic flow will change. So, think twice before taking this route.

For state management libraries, there are some popular options like [Redux-Toolkit](https://github.com/reduxjs/redux-toolkit) and [Zustand](https://github.com/pmndrs/zustand). I’ve used Redux-Toolkit for e-commerce websites but mostly because it was already there, before joining the project. I’ve never used Zustand for real-life apps but I’ve read good things across the community.

> ⚠️ _**Remember:**_ **You can always combine both approaches.** You can use React’s built-in tools for simpler pages and components and a state management library for the complex part of your applications.

For example, you can use the built-in tools for generic components like Forms and Inputs used across multiple pages where you use \`useState\` internally for managing their internal state. Then you can use the state management library for complex states across various pages.

**In React we don’t have a common way of fetching data**. The React team doesn’t suggest how to do that in our React application. That’s why each team creates its implementation.

This sometimes might be good because we have a lot of **freedom**. At the same time, we have to manage common scenarios like loading states and error handling on our own. This includes a lot of **boilerplate** inside our components and applications.

It’s not very hard to make our implementation but when we do create it we will have to support and maintain it which might not be justified.

Thankfully, there are open-source libraries that solve exactly this problem. For example, **[TanStack's React-Query](https://tanstack.com/query/latest/docs/framework/react/overview)** and **[Vercel’s SWR](https://swr.vercel.app/)** (for REST) or **[Apollo-Client](https://www.apollographql.com/docs/react/)** and **[urql](https://commerce.nearform.com/open-source/urql/docs/)** (for GraphQL).

These libraries make it easy to add **data-fetching capabilities to our components through simple hooks**. This way we **follow the natural component lifecycle** and mental model. They expose **loading states** and make **error handling** much easier inside our components. They only need a **fetcher function** that makes the call to the Server.

You can think of the data-fetching library as **a thin layer around our API calls**, adding additional functionality.

Another big reason for using data-fetching libraries is that they come with additional features like **caching, automatic refetching, and background updates**.

[

![](https://substackcdn.com/image/fetch/$s_!v1uv!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1ad33f5b-0c4c-4948-a0d0-8386ebbbb766_3322x3960.png)

](https://substackcdn.com/image/fetch/$s_!v1uv!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1ad33f5b-0c4c-4948-a0d0-8386ebbbb766_3322x3960.png)

In this example, we use [React-Query](https://tanstack.com/query/latest/docs/framework/react/overview).

[

![](https://substackcdn.com/image/fetch/$s_!lTx4!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4575668b-6036-4941-b29a-edeb0c831d57_3107x3120.png)

](https://substackcdn.com/image/fetch/$s_!lTx4!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4575668b-6036-4941-b29a-edeb0c831d57_3107x3120.png)

As you can see from the examples, using a data-fetching library makes the overall component’s code and boilerplate much easier to read, follow, and maintain.

> 💡 _My advice**:**_ **Use Data Fetching Libraries.**

*   _[How McDonald’s Food Delivery Platform Handles 20,000 Orders per Second](https://newsletter.systemdesign.one/p/mcdonalds-architecture)_ from [System Design Newsletter](https://open.substack.com/pub/systemdesignone) by [Neo Kim](https://open.substack.com/users/135589200-neo-kim?utm_source=mentions)
    
*   _[5 Writing Tips to Overcome the Blank Page](https://www.leadership-letters.com/p/5-writing-tips-to-overcome-the-blank)_ from [Leadership Letters](https://open.substack.com/pub/amukherjee) by [Akash Mukherjee](https://open.substack.com/users/197891722-akash-mukherjee?utm_source=mentions)
    
*   _[How to prioritize effectively](https://thehustlingengineer.substack.com/p/prioritize-your-tasks-effectively)_ from [The Hustling Engineer](https://open.substack.com/pub/thehustlingengineer) by [Hemant Pandey](https://open.substack.com/users/58770480-hemant-pandey?utm_source=mentions)
    
*   _[Managing up: 3 things I wish I realized sooner](https://read.highgrowthengineer.com/p/managing-up-realizations)_ from [High Growth Engineer](https://open.substack.com/pub/highgrowthengineer) by [Jordan Cutler](https://open.substack.com/users/58854493-jordan-cutler?utm_source=mentions)
    

[

![15 React Component Principles & Best Practices for Better Software Architecture & Design](https://substackcdn.com/image/fetch/$s_!B8D2!,w_140,h_140,c_fill,f_auto,q_auto:good,fl_progressive:steep,g_auto/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2d896123-25da-4d25-aeb4-65b4447c76f5_1456x1048.png)

](https://thetshaped.dev/p/15-react-component-principles-for-better-design)

[

![React Component Mental Models](https://substackcdn.com/image/fetch/$s_!9ezS!,w_140,h_140,c_fill,f_auto,q_auto:good,fl_progressive:steep,g_auto/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F96315a7c-33e4-43e3-8fa8-6a424862ca42_1456x1048.png)

](https://thetshaped.dev/p/react-component-mental-models)

[

![Comparison Guide: Bootstrap vs. Tailwind CSS. When and What to choose?](https://substackcdn.com/image/fetch/$s_!aCH6!,w_140,h_140,c_fill,f_auto,q_auto:good,fl_progressive:steep,g_auto/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3f7bf69d-ab44-48fb-a7ef-c860a495618c_1456x1048.png)

](https://thetshaped.dev/p/comparison-guide-bootstrap-vs-tailwindcss)
