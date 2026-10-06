---
url: "https://www.toptal.com/front-end/eight-expert-css-tips"
captured_at: "2017-06-09T15:13:36-03:00"
title: "Eight CSS Tips for Advanced Layouts and Effects"
domain: "toptal-com"
---

# Eight CSS Tips for Advanced Layouts and Effects

[View all articles](https://www.toptal.com/developers/blog)

The realm of web front-end development has made considerable progress over the last few years. However, the web front-end, as the users see it, is still the same: HTML markup styled with CSS.

Many layout problems can seem simple at first but often proves to be tricky. Without extensive knowledge of how certain CSS features work, these advanced layouts can seem impossible to achieve with CSS alone.

![toptal-blog-image-1496992177402-1b8a1fe3282c43dfb6bb01fd4536fb6c.jpg](toptal-com--eight-css-tips-for-advanced-layouts-and-effects/1b8a1fe3282c43dfb6bb01fd4536fb6c.jpg)

In this article, you will find eight expert CSS tips and tricks that leverage lesser known CSS features to implement some of these advanced layouts and effects.

## 1. Maximizing CSS Sibling Selectors

**The problem:** You are losing optimization opportunities by not using sibling selectors.

**The solution:** Use sibling selectors whenever it makes sense.
Whenever you are working with a list of items, and you need to treat the first or the last item differently, your first instinct may be to use the `:first-child` and `:last-child` pseudo CSS selectors.

For example, when creating a CSS-only hamburger menu icon:

This makes sense: Each bar has a margin-bottom, except for the last one.

Yet the same effect is also possible through the adjacent sibling selector (+):

This also makes sense: Everything after the first bar has a margin-top. Not only does this CSS trick save a few extra bytes (which can easily add up for any medium-sized project), but it also opens up a world of possibilities.

Consider this list of cards:

Each one has a title and text, the latter of which is hidden by default.
If you want to make only the text of the active card (with the `.active` class) and the ones following it visible you can do it quickly using just CSS:

With a little JavaScript, this can be interactive as well.

Relying on JavaScript alone for all that, however, would result in a script like this:

where including jQuery as a dependency lets you have somewhat short code.

## 2. Consistent HTML Element Sizing

**The problem:** HTML elements have inconsistent sizes across different browsers.

**The solution:** Set `box-sizing` for all elements to `border-box`.
A long-time bane for web developers, Internet Explorer did one thing right: It sized boxes properly.

Other browsers only look at the content when calculating the width of an HTML element, with everything else treated as surplus. A `width: 200px` div, with `20px` padding and a `2px` border, renders as 242 pixels wide.

Internet Explorer considers padding and border as a part of the width. Here, the div from above would be 200 pixels wide.

Once you get the hang of it, you will find the latter approach [to be more logical](https://www.paulirish.com/2012/box-sizing-border-box-ftw/), even if it doesn’t follow [standards](https://www.w3.org/TR/CSS21/box.html#box-dimensions).

> *If I say the width is 200px, gosh darn it, it’s gonna be a 200px wide box even if I have 20px of padding.*

In any case, the following CSS keeps element sizes (and therefore layouts) consistent across all browsers:

The second set of CSS selectors protects HTML elements styled without border-box in mind from layout disruption.

`box-sizing: border-box` is so useful that it’s part of a relatively popular CSS framework called [sanitize.css](https://jonathantneal.github.io/sanitize.css/).

## 3. Dynamic Height Elements

**The problem:** Keeping an HTML element’s height proportional to its width.

**The solution:** Use vertical padding as a replacement for height.

Let’s say you want an HTML element’s height to always match its CSS width. `height: 100%` doesn’t change the default behavior of elements matching the height of its content.

The answer is to set the height to 0 and use padding-top or padding-bottom to set `.container`’s actual height instead. Either property can be a percentage of the element’s width:

Now `.container` will remain a square no matter how wide it becomes. `overflow: hidden` keeps long content from breaking this ratio.

This technique, with some modification, is great for creating video embeds that retain their aspect ratio at any size. Just align the embed with `.container`’s top and left through `position: absolute`, set both dimensions of the embed to 100% so that it “fills up” `.container`, and change `.container`’s `padding-bottom` to match the video’s aspect ratio.

`position: relative` for `.container` ensures that the `iframe` [absolute positioning works properly](https://developer.mozilla.org/en/docs/Web/CSS/position?v=control#Absolute_positioning). The new `padding-bottom` is just the aspect ratio’s height divided by its width, times 100. For example, if the aspect ratio of the video embed is 16:9, the padding-bottom percentage should be 9 divided by 16 (.5625) and multiplied by 100 (56.25).

## 4. Dynamic Width Elements

**The problem:** Keeping an HTML element’s width proportional to its height.

**The solution:** Use font-size as the basis for the element’s dimensions.

Now, what about the reverse, or containers that change width as their height does? This time, it’s `font-size` to the rescue. Remember that width and height can be in `em`s, meaning they can be a ratio of the element’s `font-size`.

An element with a `font-size` of 40px, a width of `2em`, and a height of `1em` would be 80 pixels (40 x 2) wide and 40 pixels (40 x 1) tall.

Want to change `.container`’s height? Change font-size.

The only caveat is that it’s impossible to make an element’s font-size match the height of its parent automatically through only CSS. Yet this technique allows a Javascript resize script to be cut down from:

```
var container = document.querySelector( '.container' );
container.style.height = yourDesiredHeight + 'px';
container.style.width = yourDesiredHeight * yourDesiredRatio + 'px';
```

to:

```
document.querySelector( '.container' ).style.fontSize = yourDesiredHeight + 'px';
```

## 5. Vertical Centering of Dynamic Content

**The problem:** Keeping an HTML element (with unknown height) vertically centered inside another.

**The solution:** Set the outer element to `display: table`, then convert the inner element into a CSS `table-cell`. Or just use [CSS Flexbox](https://www.toptal.com/front-end/how-to-build-css-only-smart-layouts-with-flexbox).

It’s possible to vertically center one line of text with `line-height`:

For multiple lines of text or non-text content, CSS tables are the answer. Set `.container`’s display to `table`, then use `display: table-cell` and `vertical-align: middle` for `.text`:

Think of this CSS trick as the vertical equivalent of `margin: 0 auto`.
CSS3’s Flexbox is a great alternative for this technique if [Internet Explorer’s buggy support](http://caniuse.com/#feat=flexbox) is acceptable:

## 6. Same-Height Columns

**The problem:** Keeping columns the same height.

**The solution:** For each column, use a large negative `margin-bottom` value, and cancel that out with an equally large `padding-bottom`. CSS tables and Flexbox also work.

Using `float` or `display: inline-block`, it’s possible to create side-by-side columns through CSS.

Note the use of `box-sizing: border-box` to properly size the `.cols`. See Consistent HTML Element Sizing above.

The borders of the first and last column don’t go all the way down; they don’t match the height of the taller second column. To fix this, just add `overflow: hidden` to `.row`. Then set each `.col`’s `margin-bottom` to 99999px and its `padding-bottom` to 100009px (99999px + the 10px padding applied to `.col`’s other sides).

A more straightforward alternative is Flexbox. Again, only use this if Internet Explorer support isn’t a must.

One more alternative with better browser support: CSS tables (without `vertical-align: middle`).

Like what you're reading?

Get the latest updates first.

No spam. Just great engineering posts.

Like what you're reading?

Get the latest updates first.

Thank you for subscribing!

You can edit your subscription preferences [here](https://www.toptal.com/front-end/eight-expert-css-tips?utm_campaign=blog_post_eight_expert_css_tips&utm_medium=email&utm_source=blog_subscribers#).

- 0shares

## 7. Going Beyond the Box

**The problem:** Boxes and straight lines are so clichéd.

**The solution:** Use `transform: rotate(x)`, or `border-radius`.

Take a typical series of panes from a marketing or brochure website: a vertical stack of slides with a singular point. Its markup and CSS could look something like this:

At the cost of making the markup much more complicated, these boxy panes could be turned into a stack of parallelograms.

There’s a lot going on here:

The height of each pane is controlled by .pane-container. The negative margin-bottom makes sure the panes stack up snugly.

- `.pane-background`, its child `.mask-box`, and its grandchild `.image` are all set to `position: absolute`. Each element has different `top`, `left`, `bottom`, and `right` values. This eliminates any spacing created by the rotations detailed below.
- `.mask-box` is rotated 2 degrees (counter-clockwise).
- `.image` is rotated -2 degrees to counteract `.mask-box`’s rotation.
- `.mask-box`’s overflow is hidden so that its rotated top and bottom sides clip the `.image` element.

Feel free to play around with [this codepen](https://codepen.io/ricotheque/pen/GmVgYE?editors=1100). Try using lower rotate values and see what happens.

On a related note, turning an image into a circle or oval is dead simple. Just apply `border-radius: 100%` to the `img` element.

Real-time CSS modifications such as these lessen the need to prepare content before it’s published on a website. Instead of applying a circle mask to a photo in Photoshop, the web developer can just apply the same effect through CSS without changing the original photo.

The additional advantage is that by leaving the content untouched and not reliant on the website’s current design, future redesigns or revamps are facilitated.

## 8. Night Mode

**The problem:** Implementing a night mode without creating a new stylesheet.

**The solution:** Use CSS filters.

Some apps feature a night mode, where the interface darkens for better readability under low light. On newer browsers, CSS filters can create the same effect, by applying Photoshop-like effects.

A useful CSS filter is `invert`, which (no surprise) inverts the colors of everything inside an element. This makes creating and applying a new set of styles unnecessary.

Using this filter on black text and a white background simulates night mode. `!important` ensures that these new colors override any existing styles.

Unfortunately, the image looks weird, because its colors were inverted with everything else. The good news is that multiple filters can apply at the same time. Adding the hue-rotate filter switches images and other visual content back to normal:

Why does this work? `hue-rotate(180deg)` just creates the same effect as `invert(1)` did. [Here’s a demo](https://codepen.io/ricotheque/pen/qrbwZP?css-preprocessor=sass) of how night-mode CSS would work when toggled through a JavaScript-powered button.

## Make the Most out of CSS

Unless the browser or how websites are built changes dramatically in the future, a good knowledge of CSS will remain a fundamental skill in the web development space.

All of these CSS tips share something in common: They maximize the use of [CSS](https://www.toptal.com/css) as a styling language, letting the browser itself do the heavy lifting. And, when done right, this will always yield better results, better performance, and hence a better user experience.

Let us know if you have any CSS trick that you find interesting and useful in the comments section below.

## Key Learnings

### How can I set the height of a DIV as a percentage of its width?

Use vertical padding instead of height. The height property, when set as a percentage, is calculated relative to the height of the parent. However, a DIV with its height set to 0 can have either its padding-top or padding-bottom set to a percentage of its width.

### How can I vertically center contents of a DIV?

If it’s just one line of text, set "line-height" to the height of the container. If it’s non-text contents, wrap the DIV in a "display: table" DIV, and set the inner DIV to "display: table-cell". If supporting primitive web browsers is not on your todo list, you can always use Flexbox.

## About the author

[![large_fed34ef1156a4406d2102111fac36c15.jpg](toptal-com--eight-css-tips-for-advanced-layouts-and-effects/ea4902d558c95c86030e84364dde8e7a.jpg)

View full profile »](https://www.toptal.com/resume/rico-mossesgeld)

[Hire the Author](https://www.toptal.com/companies/apply?interested_in=developers)

[Rico Mossesgeld, Philippines](https://www.toptal.com/resume/rico-mossesgeld)

Rico has built online publications and services for big agencies, media companies, establishments, foundations, and a major daily. He relies on his proactive communication skills to help partners find solutions, and has shared his development expertise with teammates from different nationalities and timezones. [[click to continue...]](https://www.toptal.com/resume/rico-mossesgeld)

[Hiring? Meet the Top 10 Freelance Front-End Developers for Hire in June 2017](https://www.toptal.com/front-end)
