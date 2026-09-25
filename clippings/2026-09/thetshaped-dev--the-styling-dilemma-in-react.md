---
url: "https://thetshaped.dev/p/the-styling-dilemma-in-react"
captured_at: "2026-09-25T21:30:51+01:00"
title: "The styling dilemma in React"
domain: "thetshaped-dev"
---

Styling a React application can be a tricky task.

With so many options available, it’s easy to feel overwhelmed.

Choosing the appropriate styling method enhances your development experience, improves the application’s performance, and makes your code easier to manage and scale.

It’s important to get it right from the beginning.

In this article, I’ll share my experience with different styling methods in React.

I’ll discuss their pros and cons and share my preferred approach and advice.

This is the traditional way of styling websites.

You write plain [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS) files and link them to your React components.

```
// styles.css
.button {
  background-color: blue;
  color: white;
  padding: 10px;
}

// Button.js
import React from 'react';
import './styles.css';

function Button() {
  return (
    <button className="button">
      Follow The T-Shaped Dev
    </button>
  );
}

export default Button;
```

Pros:

*   **Simple and familiar to most of the developers**
    
*   **No additional setup**
    

Cons:

*   **Global scope issues**. All styles are global by default which can lead to class name collisions.
    
*   **Lack of style encapsulation** which can lead to hard times managing the project and its styles
    
*   **Limited support for dynamic styling** based on component props
    
*   **You should come up with many class names**
    
*   **Separate files for styles and components, context switching, no Locality of Behavior (LoB)**
    

CSS Preprocessors: tools like [SASS](https://sass-lang.com/)/[SCSS](https://sass-lang.com/documentation/at-rules/control/for/), [LESS](https://lesscss.org/), and [Stylus](https://stylus-lang.com/). They let you write CSS with advanced features like variables, nesting, loops, etc. They then compile down to regular CSS.

CSS Postprocessors: [PostCSS](https://postcss.org/) with plugins like [Autoprefixer](https://github.com/postcss/autoprefixer) and [Tailwind CSS](https://tailwindcss.com/). It adds features after you’ve written your CSS. They can handle things like adding vendor prefixes automatically.

[

![](https://substackcdn.com/image/fetch/$s_!48Pa!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F46060fe6-47ba-49e3-a684-00339e391026_2499x1662.png)

](https://substackcdn.com/image/fetch/$s_!48Pa!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F46060fe6-47ba-49e3-a684-00339e391026_2499x1662.png)

CSS Preprocessors (SASS) and CSS Postprocessors (PostCSS)

```
// styles.scss
$primary-color: blue;

.button {
  background-color: $primary-color;
  color: white;
  padding: 10px;

  &:hover {
    background-color: darken($primary-color, 10%);
  }
}

// Button.js
import React from 'react';
import './styles.scss';

function Button() {
  return (
    <button className="button">
      Follow The T-Shaped Dev
    </button>
  );
}

export default Button;
```

Pros:

*   Offers **advanced features like variables, nesting, loops**, etc.
    
*   You can use **different styling practices to make your styles more modular** and improve the overall code organization
    

Cons:

*   Adds **complexity to the setup** which requires additional steps and tooling
    
*   Styles are still globally scoped ⇒ **class name collisions**
    
*   **You should come up with many class names**
    
*   **Separate files for styles and components, context switching, no Locality of Behavior (LoB)**
    

```
import React from 'react';

function Button() {
  return (
    <button className="bg-blue-500 text-white p-2 hover:bg-blue-700">
      Follow The T-Shaped Dev
    </button>
  );
}

export default Button;
```

Pros:

*   Gives you **many single-purpose classes and functions** where each does only one thing
    
*   **Highly customizable**
    
*   **No custom CSS**
    
*   Ensures **design consistency** because of the standardized system
    
*   **No need to come up with class names**
    

Cons:

*   Components might become **cluttered with many class names**
    
*   Some **learning curve**
    
*   **Requires additional setup and configuration**, especially for the theming and other customizations
    

[CSS Modules](https://css-tricks.com/css-modules-part-1-need/) lets you write CSS files where class names are scoped locally by default. This avoids class name conflicts and keeps styles modular.

You can also combine CSS Preprocessors (SASS/SCSS) with CSS Modules.

```
// Button.module.css
.button {
  background-color: blue;
  color: white;
  padding: 10px;
}

// Button.js
import React from 'react';
import styles from './Button.module.css';

function Button() {
  return (
    <button className={styles.button}>
      Follow The T-Shaped Dev
    </button>
  );
}

export default Button;
```

Pros:

*   Styles are locally scoped to components ⇒ **no global scope issues and class collisions**
    
*   You can use Vanilla CSS or CSS Preprocessors (SASS/SCSS)
    
*   **Enhances maintainability by modularized styles**
    

Cons:

*   **You should come up with many class names**
    

*   **Separate files for styles and components, context switching, no Locality of Behavior (LoB)**
    

Libraries like [styled-components](https://styled-components.com/), [emotion](https://emotion.sh/docs/styled), [vanilla-extract](https://vanilla-extract.style/), and [linaria](https://linaria.dev/) let you write CSS directly in your JavaScript files. This way you can style components using JavaScript syntax. Styles are scoped to individual components which avoids class name conflicts.

_**Note 1:** styled-components and emotion are runtime CSS-in-JS libraries. vanilla-extract and linaria are compile time CSS-in-JS libraries._

```
import React from 'react';
import styled from 'styled-components';

const ButtonStyled = styled.button`
  background-color: blue;
  color: white;
  padding: 10px;

  &:hover {
    background-color: brown;
  }
`;

function Button() {
  return (
    <ButtonStyled>
      Follow The T-Shaped Dev
    </ButtonStyled>
  );
}

export default Button;
```

Pros:

*   Encapsulated styles within components ⇒ **no global scope issues and class collisions**
    
*   Enables **dynamic styling** using JavaScript and component props
    
*   **No context switching between files**. Styles are closed to their usage. **(LoB principle)**
    
*   **No need to come up with class names**
    

Cons:

*   Adds **additional dependencies** which might increase the bundle size
    
*   Some **learning curve**
    
*   **Might impact the application’s performance**
    
*   There’re could be **problems with server-side rendering**
    

*   **Naming overhead.** Coming up with meaningful class names is not easy. Also, these class names might never be reused so it reduces their significance.
    
*   **Context switching.** Having to switch between JS and CSS files disrupts the development flow.
    
*   It’s **hard to find the appropriate classes and their usage** across the components.
    

**I prefer using classless styling tools like Tailwind CSS 🔥 or CSS-in-JS.**

Here’s why:

*   **Styles live within the components** which makes them easier to maintain, manage and extend. Great DX.
    
*   I can **read the file from top to bottom** and understand what’s going on inside the component.
    
*   **No need to invent class names** or manage separate CSS files.
    
*   **No context switching between files** and searching for the classes and their usages.
    

If our styled components become too large, we can extract them into separate files. This way, we keep our codebase clean without sacrificing the benefits of localized styles.

We can also use Tailwind CSS + CSS-in-JS with the help of [twin.macro](https://github.com/ben-rogerson/twin.macro).

For example:

```
import React from 'react';
import tw from 'twin.macro';

const ButtonStyled = tw.button`
  bg-blue-500 text-white p-2 hover:bg-blue-700
`;

function Button() {
  return (
    <ButtonStyled>
      Follow The T-Shaped Dev
    </ButtonStyled>
  );
}
export default Button;
```

*   **Styling in React can be tricky due to the many options available** - Vanilla CSS, CSS Preprocessors (SASS/SCSS), Tailwind CSS, CSS Modules, CSS-in-JS.
    
*   **Knowing the pros and cons of each approach is crucial** for choosing the most appropriate styling strategy for your project.
    
*   There’s **no right or wrong approach** when it comes to styling in React - Vanilla CSS, CSS Preprocessors (SASS/SCSS), Tailwind CSS, CSS Modules, CSS-in-JS.
    
*   I prefer the **classless styling tools like Tailwind CSS 🔥 or CSS-in-JS** because this approach doesn’t require inventing class names and keeps styles and components together.
    
*   **Keeping styles close to components enhances readability and ease of maintenance.**
    

You can find me on **[LinkedIn](https://www.linkedin.com/in/petarivanovv9/)** or **[Twitter](https://twitter.com/petarivanovv9)**.

I share daily practical tips to level up your skills and become a better engineer.

_Thank you for being a great supporter, reader, and for your help in growing to 13.5K+ subscribers this week 🙏_

This newsletter is funded by paid subscriptions from readers like yourself.

If you aren’t already, consider becoming a paid subscriber to receive the full experience!

Think of it as buying me a coffee twice a month, with the bonus that you also get all my templates and products for FREE.

[Check the benefits of the paid plan](https://thetshaped.dev/about#%C2%A7why-subscribe)

_You can also hit the like ❤️ button at the bottom to help support me or share this with a friend to [get referral rewards](https://thetshaped.dev/?r=643nm). It helps me a lot! 🙏_

*   [How Google Ads Was Able to Support 4.77 Billion Users With a SQL Database](https://newsletter.systemdesign.one/p/cloud-spanner-database?r=643nm&utm_campaign=post&utm_medium=web) by [Neo Kim](https://open.substack.com/users/135589200-neo-kim?utm_source=mentions)
    
*   [What is Idempotency in Distributed Systems?](https://blog.algomaster.io/p/idempotency-in-distributed-systems?r=643nm&utm_campaign=post&utm_medium=web) by [Ashish Pratap Singh](https://open.substack.com/users/83602743-ashish-pratap-singh?utm_source=mentions)
    
*   [I have seen this mistake in production. The Dual Write Problem is not a myth](https://newsletter.systemdesignclassroom.com/p/i-have-seen-this-mistake-in-production?r=643nm&utm_campaign=post&utm_medium=web) by [Raul Junco](https://open.substack.com/users/98661477-raul-junco?utm_source=mentions)
    
*   [TCP 3-Way Handshake](https://newsletter.systemdesigncodex.com/p/tcp-3-way-handshake?r=643nm&utm_campaign=post&utm_medium=web) by [Saurabh Dashora](https://open.substack.com/users/97484183-saurabh-dashora?utm_source=mentions)
    
*   [My strategy against distractions as a software engineer working in an open-floor office](https://strategizeyourcareer.com/p/my-strategy-against-distractions?r=643nm&utm_campaign=post&utm_medium=web) by [Fran Soto](https://open.substack.com/users/170998285-fran-soto?utm_source=mentions)
    
*   [5 Lessons I learned the hard way from 10+ years as a software engineer](https://read.highgrowthengineer.com/p/5-lessons-i-learned-the-hard-way-from-10-years?r=643nm&utm_campaign=post&utm_medium=web) by [Jordan Cutler](https://open.substack.com/users/58854493-jordan-cutler?utm_source=mentions) and [Gourav Khanijoe](https://open.substack.com/users/169529562-gourav-khanijoe?utm_source=mentions)
