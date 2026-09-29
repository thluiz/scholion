---
url: "https://alligator.io/js/vanilla-pwa/"
captured_at: "2020-05-29T19:15:54-03:00"
title: "How to Build a PWA in Vanilla JavaScript ← Alligator.io"
domain: "alligator-io"
---

# How to Build a PWA in Vanilla JavaScript

[Jack Misteli](https://alligator.io/author/jack-misteli)

This is the first part of a three-part series about creating a Progressive Web App (PWA) which leverages the Web Push API and cron-schedule. In this article, we’ll cover the basics: the front-end, web app manifest and Service Worker aspect of the app, and we’ll be only using pure JavaScript to accomplish this. At the end of this post we’ll have a working PWA that’s cached so it can be accessed while offline.

## What We Are Building

My physician recently told me to take 3 pills a day. On my way back home I told myself: “I am a developer, I automate tasks, let’s build an app to help me take my pills”.

We’re going to build a simple Progressive Web App (PWA) which will remind me to take my pills every day.

Our app will have a web server powered by Express.js. Express will push notifications to the clients which subscribed to the push notifications. It will also serve the front-end app.

## Step one: PWA

The app we’re building has to remind us to take pills even when the browser is not opened. So we need a [Progressive Web App](https://alligator.io/js/intro-progressive-web-apps/).

## Getting the manifest up and ready

My first step building a PWA is to generate a manifest using [this generator](https://app-manifest.firebaseapp.com/). This tool will create your `manifest.json` file which holds all basic information about your app. It will also create some icons which will show on the user’s phones when they download the app.

Just unzip everything inside a folder at the root of our project that we’ll call `public`. I decided to call my app Temporas.

Module: public/manifest.js

```
"name":"Temporas","short_name":"Temporas","theme_color":"#222831","background_color":"#ffad17","display":"standalone","Scope":"","start_url":"/index.html","icons":[//Alotoficons]
```

PWAs rely on [Service Workers](https://alligator.io/js/service-workers/). Service workers are little programs that run as soon as they are registered independently from the rest of your JavaScript code. Service workers can’t interact directly with the DOM but can send messages to the rest of your code (we’ll explore this in more detail in part 2 of this series).

---

Now let’s create our frontend and register our service worker:

Module: public/index.html

```
<!DOCTYPE html>
<head>
  <metaname='viewport'content='width=device-width, initial-scale=1'>
  <metaname="theme-color"content="#222831">
  <linkrel='manifest'href='./manifest.json'>
  
  <script>// Registering our Service workerif('serviceWorker'innavigator){navigator.serviceWorker.register('sw.js',{scope:'./'})}</script>
</head>
<body>
  <divclass="hero">
    <h1>Temporas</h1>
    <h2>Take your medicine my friend</h2>
    <divid="status"></div>
    <buttonid="unsubscribe">unsubscribe</button>
  </div>
</body>
```

We are now one file away from having an installable web application. Let’s create our service worker:

Module: public/sw.js

```
const cacheName = 'Temporas';

// Cache all the files to make a PWA
self.addEventListener('install', e=> {
  e.waitUntil(
    caches.open(cacheName).then(cache=> {
      // Our application only has two files here index.html and manifest.json
      // but you can add more such as style.css as your app grows
      return cache.addAll([
        './',
        './index.html',
        './manifest.json'
      ]);
    })
  );
});

// Our service worker will intercept all fetch requests
// and check if we have cached the file
// if so it will serve the cached file
self.addEventListener('fetch', event=> {
  event.respondWith(
    caches.open(cacheName)
      .then(cache=> cache.match(event.request, { ignoreSearch: true }))
      .then(response=> {
        return response || fetch(event.request);
      })
  );
});
```

✨✨ We have a PWA ✨✨

## Setting up Express.js

The PWA will not work if you just open `/public/index.html` in your browser. We must serve our content from a web server.

First let’s set things up in our command line. In your root folder run:

```
$npm init
$npm install express body-parser
$touch app.js
```

Inside of `package.json` replace the `scripts` field with:

```
"scripts": {
  "test": "echo \"Error: no test specified\" && exit 1",
  "start": "node app.js"
}
```

And now let’s populate our app:

Module: app.js

```
const bodyParser = require('body-parser');
const express = require('express');
const app = express();
const port = 3000;

// We want to use JSON to send post request to our application
app.use(bodyParser.json());

// We tell express to serve the folder public as static content
app.use(express.static('public'));

app.get('/public');

app.listen(port, ()=> console.log(`Listening on port ${port}!`));
```

Now you can run `npm run start`. Go to http://localhost:3000, kill the server. Reload http://localhost:3000 and the app will look like it is still working! You can even turn off your laptop and go back to the web page on that port.

I highly advise disabling the caching mechanism of service workers when you are developing new features. It might cause some confusion.

[Here's a good post](https://alligator.io/nodejs/express-basics/) if you want to learn more about setting up an Express server.

## Checking your PWA

To test your PWA I highly recommend using the [Lighthouse extension](https://developers.google.com/web/tools/lighthouse) to see if everything is working. Remember also that when comes the time to deploying your app on the web, it needs to be served over HTTPS to be considered a PWA and to be installable as an app.

You can find all the code in this [Github repository](https://github.com/alligatorio/Vanilla-JS-PWA).
