---
url: "https://dev.to/giteden/4-tips-for-building-reusable-and-shareable-react-components-4k9a"
captured_at: "2026-11-16T01:44:56+00:00"
title: "4 Tips for Building Reusable and Shareable React Components"
domain: "dev-to"
---

### [](#1-typecheck-components-with-typescript)1\. Type-check components with TypeScript

Type-checking is essential for positive developer experience and optimized code collaboration - it what makes your reusable code easy to use and maintain.

**Why TypeScript (or, why not prop-types)?**  
TS and prop-types are not alone in this game but they are certainly the most popular. The two are different in the way they operate and even in the way they're used (TS validates types at compile-time, whereas prop-types performs at runtime) - nevertheless, it is a fact of reality that the two are rarely used on the same project. That isn't surprising as the two do overlap quite considerably in the way they're used - and, with all due respect to dev ex, there's still a product to deliver.

If you ever used TypeScript you know it serves a much greater role than prop-types. It offers intelligent code suggestions in supported IDEs, it shortens useful and otherwise cumbersome JS code (e.g, Enums) and in general, once you get the hang of it, it shows its strengths by saving time in fixing bugs or simply figuring out your teammates' code. 

Moreover, TS is trending and may even become the new standard for web development. That certainly makes it something worth investing your time and effort.

When using tools to collaborate on components across repositories (e.g, shared [Bit](https://bit.dev/) components or even [Git Submodules](https://git-scm.com/book/en/v2/Git-Tools-Submodules), TS really shows its strengths by providing component consumers with a clear API, and component collaborators with a more explicit and intelligible code.

![Example: Browsing through shared components @ Bit.dev](https://res.cloudinary.com/practicaldev/image/fetch/s--HXGuFzKC--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_66%2Cw_800/https://miro.medium.com/max/800/1%2ANj2EzGOskF51B5AKuR-szw.gif)

Example: Browsing through shared components @ Bit.dev

### [](#2-defining-props-amp-event-is-not%C2%A0enough)2\. Defining Props & Event is Not Enough

Components should be typed as well; otherwise, implicit assumptions are not communicated to TS and unwanted errors start to appear.

For example, a functional component should be types like so:  

`const AComponent: React.FC<IProps> = (props : IProps) => {...}`  

Otherwise, TS will not expect the ‘children’ prop or a return type that must be assignable to JSX.Element

For example (an un-typed component):

import React from 'react';

import './Button.css';

interface IButtonProps {

color: 'day' | 'night';

}

const Button \= ({color} : IButtonProps) \=> {

return (

<button className\={color}\></button\>

)

}

export default Button;

Used like so:  

```
function App() {
return (
<div className="App">
        <Button color='day'>a lable!</ButtonA>
    </div>
  );
}
```

Enter fullscreen mode Exit fullscreen mode

Will produce an error, informing you that 'children' were not expected:  

```
Type '{ children: string; color: "day"; }' is not assignable to type 'IntrinsicAttributes & IButtonProps'.

Property 'children' does not exist on type 'IntrinsicAttributes & IButtonProps'.
```

Enter fullscreen mode Exit fullscreen mode

### [](#3-write-react-with-ts-to-auto-generate-docs)3\. Write React with TS to Auto Generate Docs

Auto doc-generation is another great thing you can expect to enjoy when using TS (but in that case, also with prop-types). To make that happen, make sure you define your components' type/interface both as a generic of `React.FC<T>` and (directly) as the function's argument type. Otherwise, your props would simply not be included in the generated docs (at least not when using [react-docgen](https://github.com/reactjs/react-docgen) / [Bit.dev](https://bit.dev/))

For example:  

const ExtendedButton \= ({text, type, action} : IButtonProps) \=> {

}

Moreover, make sure to complement your TS with descriptions written using the JSDocs syntax.

For Example, this:

type RemovableListItemProps \= {

/\*\* The item's text \*/

text: string,

id: string,

/\*\* A callback function for the "X" click event \*/

removeItem: (id: string) \=> void

}

const RemovableListItem \= ({text, id, removeItem} : RemovableListItemProps) \=> {

const \[isCompleted, setIsCompleted\] \= useState(false);

return(

<li className\={styles.listItem}\>

<span data-iscompleted\={isCompleted} className\={styles.text} onClick\={() \=> setIsCompleted(!isCompleted)}\>{text}</span\>

<button className\={styles.delete} onClick\={() \=> removeItem(id)}\>X</button\>

</li\>

)

}

export default RemovableListItem;

Will generate this:

[![Generated Doc on a component page.](https://res.cloudinary.com/practicaldev/image/fetch/s--UnEQG-DR--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_800/https://miro.medium.com/max/807/0%2Ai-Ju6f8Iua81rg-f.png)](https://bit.dev/eden/react-ts-demo/removable-list-item)  
[](https://bit.dev/eden/react-ts-demo/removable-list-item)

[Auto-generated documentation on component page.](https://bit.dev/eden/react-ts-demo/removable-list-item)

[Check out React-docgen playground](http://reactcommunity.org/react-docgen/)

### [](#4-extend-nativehtmllike-components-with-reacts-interfaces)4\. Extend Native-HTML-like Components with React's Interfaces

[![](https://res.cloudinary.com/practicaldev/image/fetch/s--1Tj90358--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_800/https://miro.medium.com/max/1654/1%2Ad_cNV9_7GO3XsdcGf4SMeQ.png)](https://res.cloudinary.com/practicaldev/image/fetch/s--1Tj90358--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_800/https://miro.medium.com/max/1654/1%2Ad_cNV9_7GO3XsdcGf4SMeQ.png)

Before we start, two files you should definitely get familiar with are: React's index.d.ts and the global.d.ts files.

They're both installed when you add React to your project (if you used npm, you'll find them inside the npm\_modules/@types/react folder.

These files contain type and interface definitions used and offered by React, so if you need to extend a native-HTML-like component - that is where you'd find it.

For example, let's say I have a Button component that behaves, more or less, like a native HTML button element (e.g., it can have a label, it has a 'disable' prop, etc.). I can and should enjoy all the implicit definitions that come with such a component, using React's types.

import React, {ButtonHTMLAttributes} from 'react';

interface IButtonProps extends ButtonHTMLAttributes<HTMLButtonElement\> {

uniqueProp: string

}

const ExtendedButton : React.FC<IButtonProps\> \= (props : IButtonProps) \=> {

const {uniqueProp, ...buttonAttributes} \= props;

return (

<div\>

<button {...buttonAttributes}\>{uniqueProp}</button\>

</div\>

)

}

[![](https://res.cloudinary.com/practicaldev/image/fetch/s--cpUlvGNs--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_800/https://storage.googleapis.com/static.bit.dev/lp-assets/devto/Screen%2520Shot%25202020-03-23%2520at%252023.12.03.png)](https://res.cloudinary.com/practicaldev/image/fetch/s--cpUlvGNs--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_800/https://storage.googleapis.com/static.bit.dev/lp-assets/devto/Screen%2520Shot%25202020-03-23%2520at%252023.12.03.png)

### [](#conclusion)Conclusion

This post is far from being a comprehensive guide to building reusable components but I do hope I've managed to clear up a few important issues. React with TypeScript, together with the right tools for component collaboration, offer a great way to increase collaboration and build a more maintainable and scalable code.

### [](#related-posts)Related posts
