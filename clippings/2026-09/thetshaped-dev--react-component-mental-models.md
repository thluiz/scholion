---
url: "https://thetshaped.dev/p/react-component-mental-models"
captured_at: "2026-09-25T21:34:49+01:00"
title: "React Component Mental Models"
domain: "thetshaped-dev"
---

In React we write Components. Then we combine these components into bigger components. Then we continue and in the end, we have a Page - a combination of many smaller components.

**Understanding the different types of components in React helps to create well-designed applications and write quality code.**

After reading the article, **you’ll learn**:

*   What are Container and Presentational Components?
    
*   How did hooks change the way we look at Container and Presentational Components?
    
*   A better mental model for designing React Components?
    
*   What are Stateful and Stateless Components?
    

The **Container and Presentational mental model**, or pattern, suggests **separating the view from the application and business logic**. This way of structuring our components helps to better organize our React applications. Another way of looking into these components is **smart** (container) and **dumb** (presentational).

**Container components** are responsible for things like **state and data fetching**. They care about _**what**_ **data is shown to the user**.

**Presentational components** focus on **how things look**. They care about _**how**_ **data is shown to the user**.

The main idea is that **some components hold our business and application logic**, while **others receive data through their props and visualize it**.

This mental model is similar to the MVC (Model-View-Controller) structure used in back-end applications. Because this pattern is generic enough and can work almost everywhere, you can’t go wrong with using it.

However, in modern UI applications, this pattern and mental model doesn’t work well. We have a few components that hold the logic. They end up with **too many responsibilities which makes them very hard to manage, extend and test**. With the application’s growth and maturity, **the maintainability of these places becomes a nightmare**.

[

![](https://substackcdn.com/image/fetch/$s_!MlJq!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6b120441-7538-49c7-9c75-c1c29b56927f_2282x2196.png)

](https://substackcdn.com/image/fetch/$s_!MlJq!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6b120441-7538-49c7-9c75-c1c29b56927f_2282x2196.png)

With the introduction of hooks, the Container and Presentational mental model becomes slightly unnecessary. **The pattern can be replaced with hooks**.

**Hooks made it easy for developers to add statefulness without needing a container component to provide the state.**

We can refactor and simplify the example from above to:

[

![](https://substackcdn.com/image/fetch/$s_!E-Va!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F39bc7fe4-65d5-4131-bf74-52d6ee269242_2354x2280.png)

](https://substackcdn.com/image/fetch/$s_!E-Va!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F39bc7fe4-65d5-4131-bf74-52d6ee269242_2354x2280.png)

By using a custom hook, we no longer need to wrap the `UserList` component with a Container component to fetch the data and send it to the Presentational component (`UserList`).

We also don’t violate the separation of concerns principle since the business and application logic is extracted into a custom hook (`useUsers`), without modifying the data inside the `UserList` component.

The above-mentioned mental model (Container and Presentational components) suggests that you should have a few components that manage a lot of complexity while many others are only responsible for visualization.

As we discussed earlier, the Container and Presentational components mental model falls short with the maturity of the application because it’s maintainability becomes very hard.

Instead, the Stateful and Stateless components mental model suggests about **spreading the complexity throughout the whole application**.

> **The state and business logic should live as close as possible to its usage.**

We should think of the different responsibilities our components have, instead of having containers. **Think of the most suitable and appropriate place where a** _**responsibility**_ **(state / business logic), should live**.

For example, a **<Form />** component should be responsible for handling the data of the form. An **<Input />** field should be receiving data from the outside and call the appropriate callbacks when a change occurs. A **<Button />** should be responsible for indicating it was pressed and let the form do the necessary.

Even with the **<Form />** example, we may end up with many questions regarding its design like “_Who does the validation of the form?_ _Should we add it to the **<Input />** field?_ _How do we show errors?_ _How do we refresh the state in case of an error?_ _If we have an error, how will prevent the submit of the form?_

If we let the **<Input />** field manage the validation then the **<Input />** component will be aware of the business logic of our application.

In this example, the better approach is to let the **<Input />** component to be **stateless** and leave the rest to the **<Form />**. The error message will be passed from the **<Form />** to the **<Input />**, so the business logic will be inside the **<Form />** and the visualization of the error will be responsibility of the **<Input />** component.

[

![](https://substackcdn.com/image/fetch/$s_!qlaB!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd2f4693d-38ef-4370-9a04-0c0a394af5ee_3286x1608.png)

](https://substackcdn.com/image/fetch/$s_!qlaB!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd2f4693d-38ef-4370-9a04-0c0a394af5ee_3286x1608.png)

Even for a simple example like the **<ToggleButton />**, we have state. If we try to fit this component into the Container and Presentational components mental model, it won’t be very suitable.

However, this suits well into the Stateful and Stateless components mental model. **The responsibility of whether the button is active or inactive leaves inside it.**

Understanding these mental models in React can greatly enhance your ability to **write efficient and maintainable code**. **By choosing the right type of component for the right job, you can keep your codebase clean and well organized**.

> **✅ Prefer the Stateful and Stateless Components mental model.**

By embracing the Stateful and Stateless Components mental model, our application becomes much **easier to manage, extend, maintain and test**.

**We now have many components with different responsibilities, instead of a few big ones.**

*   [Presentational and Container Components - Dan Abramov](https://medium.com/@dan_abramov/smart-and-dumb-components-7ca2f9a7c7d0)
    
*   [Container/Presentational Pattern - pattern.dev](https://www.patterns.dev/react/presentational-container-pattern/)
    

[

![15 React Component Principles & Best Practices for Better Software Architecture & Design](https://substackcdn.com/image/fetch/$s_!B8D2!,w_140,h_140,c_fill,f_auto,q_auto:good,fl_progressive:steep,g_auto/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2d896123-25da-4d25-aeb4-65b4447c76f5_1456x1048.png)

](https://thetshaped.dev/p/15-react-component-principles-for-better-design)

[

![GraphQL Intro 101 (part 2)](https://substackcdn.com/image/fetch/$s_!ZZYf!,w_140,h_140,c_fill,f_auto,q_auto:good,fl_progressive:steep,g_auto/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fab5d7582-0a3e-49ff-ae83-23d566e21f35_1456x1048.png)

](https://thetshaped.dev/p/graphql-intro-101-part-2)
