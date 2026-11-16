---
url: "https://dev.to/taylorbeeston/you-probably-don-t-need-body-parser-in-your-express-apps-3nio"
captured_at: "2026-11-16T01:32:34+00:00"
title: "You probably don't need body-parser in your Express apps"
domain: "dev-to"
---

[![Taylor Beeston](https://media2.dev.to/dynamic/image/width=50,height=50,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F273794%2F765d9426-45cf-497b-a061-a5c63b713174.jpg)](https://dev.to/taylorbeeston)

## [](#what-is-bodyparser)What is body-parser?

Often, when I see a blog post or article describing an [Express.js](https://expressjs.com/) server, it usually starts out with something similar to the following:  

```
npm init -y
npm i express body-parser
```

Enter fullscreen mode Exit fullscreen mode

Followed by the classic  

```
const express = require('express');
const bodyParser = require('body-parser');

const app = express();
app.use(bodyParser.json());
// more express stuff
```

Enter fullscreen mode Exit fullscreen mode

I used to have these four lines of code in practically _every_ Express app I've ever made!

However, a few weeks ago I was poring over the [Express Docs](https://expressjs.com/en/api.html) and noticed that as of version 4.16.0 [(which came out three years ago!)](https://www.npmjs.com/package/express/v/4.16.0), [Express basically comes with body-parser out of the box!](https://expressjs.com/en/api.html#express.json)

## [](#how-do-i-use-the-express-version)How do I use the Express version?

Well, you can pretty much just search `bodyParser`, and replace it with `express`!

This means our four lines of code above can be refactored into the following three lines of code:  

```
const express = require('express');

const app = express();
app.use(express.json());
```

Enter fullscreen mode Exit fullscreen mode

If you are using [Babel](https://babeljs.io/) (which I would highly recommend!), you can even use a named import to make the code even more concise:  

```
import express, { json } from 'express';

const app = express();
app.use(json());
```

Enter fullscreen mode Exit fullscreen mode
