---
url: "http://keithclark.co.uk/articles/pure-css-parallax-websites/"
captured_at: "2014-10-31T09:23:05-03:00"
title: "Pure CSS Parallax Websites"
domain: "keithclark-co-uk"
---

# Pure CSS Parallax Websites

04 August 2014

This article demonstrates how to use CSS transforms, perspective and some scaling trickery to create a pure CSS parallax scrolling website.

Parallax is almost always handled with JavaScript and, more often than not, it's implemented badly with the worst offenders listenening for the `scroll` event, modifying the DOM directly in the handler and triggering needless reflows and paints. All this happens out of sync with the browsers rendering pipeline causing dropped frames and stuttering. It's not all bad though, `requestAnimationFrame` and deferring DOM updates can transform parallax websites - but what if you could remove the JavaScript dependency completely?

Deferring the parallax effect to CSS removes all these issues and allows the browser to leverage hardware acceleration resulting in almost everything being handled by the compositor. The result is consistent frame rates and perfectly smooth scrolling. You can also combine the effect with other CSS features such as [media queries](http://www.w3.org/TR/css3-mediaqueries/) or [supports](http://www.w3.org/TR/css3-conditional/) - responsive parallax anyone?

[Try the demo](http://keithclark.co.uk/articles/pure-css-parallax-websites/demo3/)

## The theory

Before we dive into how the effect works, let's establish some barebones markup:

```
<div class="parallax">
  <div class="parallax__layer parallax__layer--back">
    ...
  </div>
  <div class="parallax__layer parallax__layer--base">
    ...
  </div>
</div>
```

And here are the basic style rules:

```
.parallax 
  perspective
  height 100vh
  overflow-x hidden
  overflow-y
.parallax__layer 
  position absolute
  right
  bottom
.parallax__layer--base 
  transform translateZ0
.parallax__layer--back 
  transform translateZ-1px
```

The `parallax` class is where the parallax magic happens. Defining the `height` and `perspective` style properties of an element will lock the perspective to its centre, creating a fixed origin 3D viewport. Setting `overflow-y: auto` will allow the content inside the element to scroll in the usual way, but now descendant elements will be rendered relative to the fixed perspective. This is the key to creating the parallax effect.

Next is the `parallax__layer` class. As the name suggests, it defines a layer of content to which the parallax effect will be applied; the element is pulled out of content flow and configured to fill the space of the container.

Finally we have the modifier classes `parallax__layer--base` and `parallax__layer--back`. These are used to determine the scrolling speed of a parallax element by translating it along the Z axis (moving it farther away, or closer to the viewport). For brevity I have only defined two layer speeds - we'll add more later.

[Try it](http://keithclark.co.uk/articles/pure-css-parallax-websites/demo1/)

## Depth correction

Since the parallax effect is created using 3D transforms, translating an element along the Z axis has a side effect - its effective size changes as we move it closer to or farther away from the viewport. To counter this we need to apply a `scale()` transform to the element so that it appears to be rendered at its original size:

```
.parallax__layer--back 
  transform translateZ-1px scale2
```

The scale factor can be calculated with `1 + (translateZ * -1) / perspective`. For example, if our viewport `perspective` is set to `1px` and we translate an element `-2px` along the Z axis the correction scale factor would be 3:

```
.parallax__layer--deep 
  transform translateZ-2px scale3
```

[Try it depth corrected](http://keithclark.co.uk/articles/pure-css-parallax-websites/demo2/)

## Controlling layer speed

Layer speed is controlled by a combination of the perspective and the Z translation values. Elements with negative Z values will scroll slower than those with a positive value. The further the value is from `0` the more pronounced the parallax effect (i.e. `translateZ(-10px)` will scroll slower than `translateZ(-1px)`).

## Parallax sections

The previous examples demonstrated the basic techniques using very simple content but most parallax sites break the page into distinct sections where different effects can be applied. Here's how to do that.

Firstly, we need a `parallax__group` element to group our layers together:

```
<div class="parallax">
  <div class="parallax__group">
    <div class="parallax__layer parallax__layer--back">
      ...
    </div>
    <div class="parallax__layer parallax__layer--base">
      ...
    </div>
  </div>
  <div class="parallax__group">
    ...
  </div>
</div>
```

Here's the CSS for the group element:

```
.parallax__group 
  position relative
  height 100vh
  transform-style preserve-3d
```

In this example, I want each group to fill the viewport so I've set `height: 100vh`, however arbitrary values can be set for each group if required. `transform-style: preserve-3d` prevents the browser flattening the `parallax__layer` elements and `position: relative` is used to allow the child `parallax__layer` elements to be positioned relative to the group element.

One important rule to keep in mind when grouping elements is, we cannot clip the content of a group. Setting `overflow: hidden` on a `parallax__group` will break the parallax effect. Unclipped content will result in descendant elements overflowing, so we need to be creative with the `z-index` values of the groups to ensure content is correctly revealed/hidden as the visitor scrolls through the document.

There are no hard and fast rules for dealing with layering as implementations will differ between designs. It's much easier to debug layering issues if you can see how the parallax effect works - you can do that by applying simple transform to the group elements:

```
.parallax__group 
    transform translate3d700px 0 -800px rotateY30deg
```

Have a look at the following example - note the **debug** option!

[Try it with groups](http://keithclark.co.uk/articles/pure-css-parallax-websites/demo3/)

## Browser support

- Firefox, Safari, Opera and Chrome all support this effect.
- Firefox works too but there is currently a minor issue with alignment.
- IE doesn't support `preserve-3d` yet (it's coming) so the parallax effect won't work. That's ok though, you should still design your content to work without the parallax effect - You know, progressive enhancement and all that!
