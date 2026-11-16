---
url: "https://dev.to/liaowow/8-css-best-practices-to-keep-in-mind-4n5h"
captured_at: "2026-11-16T00:27:35+00:00"
title: "8 SCSS Best Practices to Keep in Mind"
domain: "dev-to"
---

This past week I had an opportunity to browse through a company's coding guideline, some of which I found very useful not only in collaborative settings but also in developing personal projects.

Here are eight of SCSS best practices from the guideline that made me rethink the way I structure my CSS code:

_Note: The following tips are geared toward SCSS, so some might not apply to pure CSS. Big thanks to [@yzoja](https://dev.to/yzoja) and [@8detect](https://dev.to/8detect) for the great reminder!_

## [](#1-mobile-first)1\. Mobile First

When it comes to responsive design, it's common to prioritize the desktop version, which can make customizing for mobile a painful process. Instead, we should design to expand, not cram things to fit mobile.

Don't:  

```
.bad {
  // Desktop code

  @media (max-width: 768px) {
    // Mobile code
  }
}
```

Enter fullscreen mode Exit fullscreen mode

Do:  

```
.good {
  // Mobile code

  @media (min-width: 768px) {
    // Desktop code
  }
}
```

Enter fullscreen mode Exit fullscreen mode

## [](#2-set-variables)2\. Set Variables

Defining CSS variables and mixins should be part of the initial setup, which can make the project much more maintainable.

According to the guideline, here are some common properties that will benefit from variables:

*   `border-radius`
*   `color`
*   `font-family`
*   `font-weight`
*   `margin` (gutters, grid gutters)
*   `transition` (duration, easing) – consider a mixin

## [](#3-avoid-raw-id-endraw-and-raw-important-endraw-)3\. Avoid `#id` and `!important`

Both `!important` and `#id`s are considered overly specific and can mess with the order of CSS rendering especially when developing collaboratively.

Don't:  

```
#bad {
  #worse {
     background-color: #000;
  }
}
```

Enter fullscreen mode Exit fullscreen mode

Do:  

```
.good {
  .better {
     background-color: rgb(0, 0, 0);
  }
}
```

Enter fullscreen mode Exit fullscreen mode

## [](#4-avoid-magic-numbers)4\. Avoid Magic Numbers

Try not to set arbitrary numbers because they "just work"; other developers might not understand why the property has to be set in such particular numbers. Instead, create relative values whenever possible.

If you're interested, CSS Tricks have a [clear explainer](https://css-tricks.com/magic-numbers-in-css/) of why Magic Numbers are bad.

Don't:  

```
.bad {
  left: 20px;
}
```

Enter fullscreen mode Exit fullscreen mode

Do:  

```
.good {
  // 20px because of font height
  left: ($GUTTER - 20px - ($NAV_HEIGHT / 2));
}
```

Enter fullscreen mode Exit fullscreen mode

## [](#5-descriptive-naming)5\. Descriptive Naming

It's easy to define CSS selectors according to the looks. It's better to describe the hierarchy.

Don't:  

```
.huge-font {
  font-family: 'Impact', sans-serif;
}

.blue {
  color: $COLOR_BLUE;
}
```

Enter fullscreen mode Exit fullscreen mode

Do:  

```
.brand__title {
  font-family: 'Impact', serif;
}

.u-highlight {
  color: $COLOR_BLUE;
}
```

Enter fullscreen mode Exit fullscreen mode

## [](#6-zero-values-and-units)6\. Zero Values and Units

This one might be up to personal choice or specific project style guide, but consistency is key. The rule below asks that you specify units on zero-duration times, but not on zero-length values. Also, add a leading zero for decimal places, but don't go crazy (more than three) on decimal places.

Don't:  

```
.not-so-good {
  animation-delay: 0;
  margin: 0px;
  opacity: .4567;
}
```

Enter fullscreen mode Exit fullscreen mode

Do:  

```
.better {
  animation-delay: 0s;
  margin: 0;
  opacity: 0.4;
}
```

Enter fullscreen mode Exit fullscreen mode

## [](#7-inline-commenting)7\. Inline Commenting

The best practice here is to comment on top of the property you're describing. Also, use inline commenting (`//`) instead of block-level comments (`/* */`), which is harder to uncomment.

Don't:  

```
.bad {
  background-color: red; // Not commenting on top of property
  /* padding-top: 30px;
  width: 100% */
}
```

Enter fullscreen mode Exit fullscreen mode

Do:  

```
.good {
  // Commenting on top of property
  background-color: red;
  // padding-top: 30px;
  // width: 100%;
}
```

Enter fullscreen mode Exit fullscreen mode

## [](#8-nesting-media-queries)8\. Nesting Media Queries

In order to easily locate media queries, it is recommended that you keep the media queries at the root of the declaration instead of nesting them inside each selector.

Don't:  

```
.bad {

  &__area {
    // Code

    @media (min-width: 568px) {
      // Code
    }
  }

  &__section {
    // Code

    @media (min-width: 568px) {
      // Code
    }
  }
}
```

Enter fullscreen mode Exit fullscreen mode

Do:  

```
.good {

  &__area {
    // Code
  }

  &__section {
    // Code
  }

  @media (min-width: 568px) {
    &__area {
      // Code
    }

    &__section {
      // Code
    }
  }
}
```

Enter fullscreen mode Exit fullscreen mode

* * *

These are by no means an exhaustive list of best coding practices, but they certainly play a vital role in designing readable, scalable web apps. Is there any CSS guideline that you follow as your north star? Let me know in the comments!
