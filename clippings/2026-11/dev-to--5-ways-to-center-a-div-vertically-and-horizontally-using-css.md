---
url: "https://dev.to/ruphaa/5-ways-to-center-a-div-vertically-and-horizontally-using-css-3i60"
captured_at: "2026-11-16T01:33:04+00:00"
title: "5 ways to center a div vertically and horizontally using CSS"
domain: "dev-to"
---

[![Alt Text](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fi%2Fw6g6lk4ysz6cy3bv9cg2.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fi%2Fw6g6lk4ysz6cy3bv9cg2.png)

Every developer should have come across this task of centering a div in their lifetime at least once or every single day. We all have our handy technique but for beginners, it might be frustrating at times.

  In this article, I have compiled a list of different CSS tricks to center a div horizontally and vertically center on a page, choose a trick or two, and make it your favorite.

### [](#method-1-using-flex)**Method 1: Using Flex**

I wanted this technique to be on top since it's my favorite of all. In this trick, all the CSS properties are defined under the parent container.

We define the parent with **_display: flex_** property along with **_justify-content_**(horizontal placement by default) and **_align-items_**(vertical placement by default) center. These properties come with Flex specifications. One glitch to make this work is by providing a fixed width and height to the parent.

[![Alt Text](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fi%2Fd1yboppbijfik58nm8ax.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fi%2Fd1yboppbijfik58nm8ax.png)

### [](#method-2-using-grid)**Method 2: Using Grid**

Using CSS Grid, we can achieve our goal in two ways. First, using **_'place-items'_** properties and second is by using **_'align and justify self'_**. Yet again, these properties are exclusive to CSS Grid.

a) Using **_place-items_**, we provide the rules to the parent, and it alone does the magic. We give the parent **_'display: grid'_** and **_'place-items: center'_** and there you go, things get super centered.

[![Alt Text](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fi%2Fpdg93ejwzoese5dpwu4d.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fi%2Fpdg93ejwzoese5dpwu4d.png)

b) Using **_'justify and align-self'_**, we provide the parent container with **_'display: grid'_** property, and the main properties are given to the child container - **_'align-self'_**(vertically placement) and **_'justify-self'_**(horizontal placement) props are given center as value.

[![Alt Text](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fi%2Fuerf3tkkj37j7hsvllt6.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fi%2Fuerf3tkkj37j7hsvllt6.png)

### [](#method-3-using-css-positioning-and-css-transform)**Method 3: Using CSS Positioning and CSS transform**

This is one of the old school methods we follow to center elements on a page. We make the child container's position **_absolute_** to the parent container and move the child container to 50% from the top and left of the parent.

[![Alt Text](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fi%2F18f9nnunoe6iwxu1boa0.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fi%2F18f9nnunoe6iwxu1boa0.png)

### [](#method-4-using-css-margin)**Method 4: Using CSS Margin**

Yet another old school method works like a charm in all the browsers. All we have to do is define **_'margin: 0 auto'_** style to the child container. I've personally faced some inconsistencies while trying this method, so I always add extra properties to center the elements.

[![Alt Text](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fi%2Fcnvo7unu19clnn3b55nx.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fi%2Fcnvo7unu19clnn3b55nx.png)

### [](#method-5-using-css-positioning)**Method 5: Using CSS Positioning**

This is one of the common methods followed since the birth of **_'CSS Positioning'_**. We make the child container **_'absolute'_** to the parent and define top, left, right, and bottom properties '0' along with **_'margin: auto'_**.

> Note: CSS Inset - It's a shorthand for top, left, right and bottom property(currently this property is supported in Firefox only)
> 
> inset: 2px 3px 4px 5px /\* top right bottom left \*/

[![Alt Text](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fi%2F90ohfgy77bha7b7bzwbd.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fi%2F90ohfgy77bha7b7bzwbd.png)

### [](#bonus-method-using-css-table)**Bonus Method: Using CSS Table**

I know we all use the **_'CSS table'_** widely across our application, which comes with plenty of table properties. I was surprised to find that we can use table property to center the content and elements in a container and it gets better we can do that in two ways.

We have to provide **_'display: table'_** to the wrapper(which is a level above the parent), then we use **_'display: table-cell'_** property in the parent.

The difference in two ways comes with child properties - one, is by using **_'margin'_** property and the other using **_'display: inline-block'_**.

[![Alt Text](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fi%2Fml1ei0nxos3tydyf4hig.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fi%2Fml1ei0nxos3tydyf4hig.png)

[![Alt Text](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fi%2Fk6b71bct2q5acxti0x4q.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fi%2Fk6b71bct2q5acxti0x4q.png)

We have reached the end of this article. I have attached a Codepen below, where you can find all of the above-mentioned tricks in one place, play around with it and share over here if you follow any cool tricks to center things.

I hope you find this article helpful and informative. If you like this article, give me a thumbs up 👍 Don't forget to bookmark it for future reference 🔖

Thanks for reading 🤓
