---
url: "https://h3.js.org/"
captured_at: "2026-11-16T19:52:51+00:00"
title: "H3"
domain: "h3-js-org"
---

## Overview

**H3** is a microframework to build client-side single-page applications (SPAs) in modern JavaScript.

H3 is also:

*   **tiny**, less than 4KB minified and gzipped.
*   **modern**, in the sense that it runs only in modern browsers (latest versions of Chrome, Firefox, Edge & similar).
*   **easy** to learn, its API is comprised of only seven methods and two properties.

### I'm sold! Where can I get it?

Here, look, it's just one file:

[Download v600-0 (Lucky Lurian)](https://git.sr.ht/~h3rald/h3/blob/6000/h3.js)

### Hello, World?

Here's an example of an extremely minimal SPA created with H3:

```
import { h3, h } from "./h3.js";
h3.init(() => h("h1", "Hello, World!"));
```

This will render a `h1` tag within the document body, containing the text `"Hello, World!"`.

### Something more complex?

Have a look at the code of a [simple todo list](https://github.com/h3rald/h3/tree/master/docs/example) ([demo](https://h3.js.org/example/index.html)) with several components, a store and some routing.

### No, I meant a real web application...

OK, have a look at [litepad.h3rald.com](https://litepad.h3rald.com/) — it's a powerful notepad application that demonstrates how to create custom controls, route components, forms, and integrate third-party tools. The code is of course [on GitHub](https://github.com/h3rald/litepad).

### Can I use it then, no strings attached?

Yes. It's [MIT-licensed](https://github.com/h3rald/h3/blob/master/LICENSE).

### What if something is broken?

Go fix it! Or at least open an issue on the [Github repo](https://github.com/h3rald/h3), pleasy.

### Can I download a copy of all the documentation as a standalone HTML file?

What a weird thing to ask... sure you can: [here](https://h3.js.org/H3_DeveloperGuide.htm)!
