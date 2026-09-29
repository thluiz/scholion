---
url: "https://dev.to/cmcodes/my-website-now-loads-in-less-than-2-sec-here-s-how-i-did-it-hoj"
captured_at: "2020-07-05T10:19:22-03:00"
title: "My website now loads in less than 2 sec! Here's how I did it! ⚡ - DEV"
domain: "dev-to"
---

# My website now loads in less than 2 sec! Here's how I did it! ⚡

Jul 4
・4 min read

Hi there!

The reason why you're here is probably because you wanna know what I did to load my portfolio website in just **1.8 seconds** and achieved a **performance score of 94** on lighthouse.

Link to my portfolio website is at the bottom.

I will lay out all my tips and tricks over here, which I implemented to achieve this! Let's get this thing started!

# Tip #1

# Don't use a large DOM tree.

> My portfolio contains 440 DOM elements with a maximum DOM depth of 13 and a maximum of 23 child elements.

If your DOM tree is very large, then it will slow down the performance of your webpage:

- Memory performance

Using general query selectors such as document.querySelectorAll('li'), stores references to a multiple nodes which can consume the memory capabilities of the device.

- Network efficiency and load performance

A big DOM tree has many nodes (not visible in first load), which slows down load time and increases data costs for your users.

- Runtime performance
  Whenever a user/ script interacts with your webpage, the browser needs to recompute the position and styling of nodes. having complicated style rules can slow down the rendering.

# Tip #2

# Don't use enormous network payloads.

> My portfolio has a total network payloads size of just 826 KB.

The total payload size of your website should be below 1600 KB.  
To keep it low, you can do the following:

- Defer requests until they're needed.
- Minify and compress network payloads.
- Set the compression level of JPEG images to 85.

> Always remember, large network payloads cost large amounts of money.

# Tip #3

# Don't use GIFs.

Rather use PNG/ WebP format for dispalying static images. But if you want to display animated content then instead of using large GIFs (inefficient & pixelated) consider using MPEG4/ WebM video format.

Now, you will say what if I want their features like:

- Automatic play.
- Continuous loop.
- No audio.

Well let me rescue you from this, the HTML5 `<video>` element allows recreating these behaviors.

```
<video autoplay loop muted playsinline>
  <source src="my-animation.webm" type="video/webm">
  <source src="my-animation.mp4" type="video/mp4">
</video>
```

# Tip #4

# Preload key requests

Suppose your page is loading a JS file which fetched another JS and a CSS file, the page won't appear completely until both of those resources are downloaded, parsed, and executed.

If the browser would be able to start the requests earlier, then there would be much time saving. Luckily, you can do so by declaring preload links.

`<link rel="preload" href="style.css" as="style">`

# Tip #5

# Don't try multiple page redirects.

Redirecting slows down the load speed of your webpage. When a browser requests a resource that has been redirected, the server returns an HTTP response. The browser must then make another HTTP request at the new location to retrieve that resource. This additional trip across the network can delay the loading of the resource by hundreds of milliseconds.

If you want to divert your mobile users to the mobile version of your webpage, consider redesigning your website to make it responsive.

# Tip #6

# Preconnect to required origins.

Using the keyword `preconnect` gives a signal to the bowser to establish early connections to important third-party origins.

`<link rel="preconnect" href="https://www.google.com">`

Doing so establishes a connection to the origin, and that informs the bowser that you want the process to start ASAP.

# Tip #7

# Encode your images efficiently.

A compression level of 85 is considerd good enough for JPEG images. You can optimize your images in many ways:

- Compressing images.
- Using image CDNs.
- Avoiding GIFs.
- Serving responsive images.
- Lazy loading images.

# Tip #8

# Minify your JavaScript files.

Minification is the process of removing whitespace and any code that is not necessary to create a smaller but perfectly valid code file.

By minifying your JavaScript files, you can reduce the payload size and parsing time for the script.

> I use [JavaScript Minifier](https://javascript-minifier.com/) for the same.

# Tip #9

# Minify your CSS files.

CSS files occupy more whitespace than any other file. By minifying them, we can save some bytes for sure!  
Do you know that you can evem change a color value to its shorthand equivalent, like #000000 can be reduced to #000, and will work just fine!

> I use [CSS Minifier](https://cssminifier.com/) for the same.

# Tip #10

# Resize your images.

I can bet this is the most given advice when it comes to webperf because the size of images is far far far greater than any text script file, so an oversized image might be an overkill.

You should never upload images that are larger than what's rendered on the screen, that will do no good.

You can either just simply resize your image dimensions or use:

- Responsive images.
- Image CDNs.
- SVG instead of icons.

Thank you for reading so far!   
Hope you learned something new from this!

Here's the link to my portfolio website [cmcodes](https://cmcodes1.github.io/)

Check it out and do let me know your views! Eager to hear your opinion.

Feel free to share your portfolio link in the comments below. I would be very happy to have a look at them.

Happy Coding! ‍
