---
url: "https://dev.to/kgprajwal/building-a-progressive-web-app-and-deploying-it-10p7"
captured_at: "2026-11-16T01:29:25+00:00"
title: "Building a Progressive Web App and Deploying it"
domain: "dev-to"
---

In my [previous article](https://dev.to/kgprajwal/learn-react-by-building-a-weather-app-3229) (which, thanks to you guys, became the top article of the week) I had discussed about how to build a weather app using ReactJS. In this article, you will learn what progressive web apps are and how to deploy the weather app to the PWA store.

## [](#introduction-to-pwa)**Introduction to PWA**

Progressive web apps are websites that bring web capabilities to an app-like experience. What it basically means is that instead of having to build a separate mobile app for your company or business interest, you can just build a progressive web app and take advantage of both web and native features. To make it even simpler, think of PWA as the best combination of both web and mobile apps.

#### [](#advantages-of-pwa)**Advantages of PWA**:

*   Progressive web apps are incredibly fast.
*   Easier to visit the website than having to install the application.
*   Native apps are well integrated and configured to the operating systems which provides better performance.
*   Offline access.
*   Less data usage.

#### [](#getting-started)**Getting Started**

While building the weather app we focused all our attention on the _src_ folder. For building our PWA application we can concentrate on the _public_ folder. Let's start by clearing the clutter in this folder until only _index.html_ file remains.

Let's start of by creating a Service Worker in the index.html. Service worker is a script that runs in the background of a website. This can be very helpful because it can run even after termination of our application and hence can be capable of delivering notifications and working offline. A new service worker can be created using the following code in the _index.html_ file just below the div with _root_ id.  

```
<script>
      if('serviceWorker' in navigator) {
        window.addEventListener('load', () => {
          navigator.serviceWorker.register('./serviceworker.js')
          .then(reg => console.log(reg.scope))
          .catch(err => console.log(err))
        })
      }
</script>
```

Enter fullscreen mode Exit fullscreen mode

Create a _serviceworker.js_ file in the public folder. In this folder paste the following code:  

```
const CACHE = "dev";
const URL = ["index.html", "offline.html"];
const self = this;
```

Enter fullscreen mode Exit fullscreen mode

As I mentioned earlier, PWA are extremely fast. The reason for this is that they maintain a cache. So, we create a variable _CACHE_ and give it a name. Then, in variable _URL_ we provide the URLs to be cached.

Now, there are three events that needs to be performed in this file:

*   **Installing the service worker**

Add the URLs into the Cache Storage.  

```
self.addEventListener("install", (e) => {
  e.waitUntil(
    caches.open(CACHE).then((cache) => {
      return cache.addAll(URL);
    })
  );
```

Enter fullscreen mode Exit fullscreen mode

*   **Listen for requests**

Match the request the page recieves and return the request if the fetch is a success, else render the offline page.  

```
self.addEventListener("fetch", (e) => {
  e.respondWith(
    caches.match(e.request).then(() => {
      return fetch(e.request).catch(() => caches.match("offline.html"));
    })
  );
});
```

Enter fullscreen mode Exit fullscreen mode

*   **Activate the service worker**

Remove old cache and store a new one.  

```
self.addEventListener("activate", (e) => {
  const newCache = [];
  newCache.push(CACHE);
  e.waitUntil(
    caches.keys().then((cacheNames) =>
      Promise.all(
        cacheNames.map((cacheName) => {
          if (!newCache.includes(cacheName)) {
            return caches.delete(cacheName);
          }
        })
      )
    )
  );
});
```

Enter fullscreen mode Exit fullscreen mode

If you would like to learn more about caching, please refer to this [link](https://developer.mozilla.org/en-US/docs/Web/API/CacheStorage).

To make to sure we test this hit `npm start` on your terminal, go to your chrome developer console and select _Application_ tab and on the _Service workers_ Panel make sure to check _Update on reload_ and then on the _Clear storage_ panel hit _Clear site data_.

[![Alt Text](https://res.cloudinary.com/practicaldev/image/fetch/s--g9IvjuRu--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_800/https://dev-to-uploads.s3.amazonaws.com/i/lomhkw5c2vy0tbn5h5ag.png)](https://res.cloudinary.com/practicaldev/image/fetch/s--g9IvjuRu--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_800/https://dev-to-uploads.s3.amazonaws.com/i/lomhkw5c2vy0tbn5h5ag.png)  
[![Alt Text](https://res.cloudinary.com/practicaldev/image/fetch/s--5EsYNlSV--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_800/https://dev-to-uploads.s3.amazonaws.com/i/spz9u360ffsi6gzq6nrz.png)](https://res.cloudinary.com/practicaldev/image/fetch/s--5EsYNlSV--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_800/https://dev-to-uploads.s3.amazonaws.com/i/spz9u360ffsi6gzq6nrz.png)

It's time to build our _offline.html_ page. I will be using minimal styling for this page, but feel free to make this offline page look extraordinary.  

```
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Weather App</title>
        <link href="https://fonts.googleapis.com/css2?family=Balsamiq+Sans:wght@700&display=swap" rel="stylesheet">
        <style type="text/css">
            html {
                height: 100%;
            }
            body {
                height: 100%;
                background-image: linear-gradient( to right, rgba(255, 100, 0, 0.52), rgba(0, 195, 255, 0.73) );
                display: flex;
                font-size: 30px;
                color: white;
                font-family: 'Balsamiq Sans', cursive;
                align-items: center;
                text-align: center;
                justify-content: center;
            }
            .lds-ripple {
                display: inline-block;
                position: relative;
                width: 80px;
                height: 80px;
            }
            .lds-ripple div {
                position: absolute;
                border: 4px solid #fff;
                opacity: 1;
                margin: -120px 170px;
                border-radius: 50%;
                animation: lds-ripple 1s cubic-bezier(0, 0.2, 0.8, 1) infinite;
            }
            .lds-ripple div:nth-child(2) {
                animation-delay: -0.5s;
            }
                @keyframes lds-ripple {
                0% {
                    top: 36px;
                    left: 36px;
                    width: 0;
                    height: 0;
                    opacity: 1;
                }
                100% {
                    top: 0px;
                    left: 0px;
                    width: 72px;
                    height: 72px;
                    opacity: 0;
                }
            }
        </style>
    </head>
    <body>
        <div class="lds-ripple"><div></div><div></div></div>
        <span>You are currently offline. Please go online to check the weather.</span>
    </body>
</html>
```

Enter fullscreen mode Exit fullscreen mode

Now, reload the page and watch your cache storage. If it looks something like the picture below, Congratulations! You've just cached your web pages for faster and offline access.

[![Alt Text](https://res.cloudinary.com/practicaldev/image/fetch/s--0qs47kD7--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_800/https://dev-to-uploads.s3.amazonaws.com/i/ooiccran0tg0ry9w53ca.png)](https://res.cloudinary.com/practicaldev/image/fetch/s--0qs47kD7--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_800/https://dev-to-uploads.s3.amazonaws.com/i/ooiccran0tg0ry9w53ca.png)

For further testing, go to the _Network_ tab and select _Offline_.

[![Alt Text](https://res.cloudinary.com/practicaldev/image/fetch/s--hOp68Jhg--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_800/https://dev-to-uploads.s3.amazonaws.com/i/zfky6i9gqgwlbnawt3ss.png)](https://res.cloudinary.com/practicaldev/image/fetch/s--hOp68Jhg--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_800/https://dev-to-uploads.s3.amazonaws.com/i/zfky6i9gqgwlbnawt3ss.png)

Now reload your page to see your cached _offline.html_ page.

[![Alt Text](https://res.cloudinary.com/practicaldev/image/fetch/s--_oy_j4L3--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_800/https://dev-to-uploads.s3.amazonaws.com/i/0mbiplhaitgsv8hgklx0.png)](https://res.cloudinary.com/practicaldev/image/fetch/s--_oy_j4L3--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_800/https://dev-to-uploads.s3.amazonaws.com/i/0mbiplhaitgsv8hgklx0.png)

#### [](#manifest)Manifest

A manifest file is a simple JSON file that provides information about the application. So create a _manifest.json_ file and paste this piece of code in there.  

```
{
  "name": "Weather App PWA",
  "short_name": "Weather App",
  "icons": [
    {
      "src": "./logo.png",
      "type": "image/png",
      "sizes": "1024x1024"
    }
  ],
  "start_url": ".",
  "display": "standalone",
  "theme_color": "#000000",
  "background_color": "#ffffff"
}

```

Enter fullscreen mode Exit fullscreen mode

To learn more about manifest files check out this [link](https://web.dev/installable-manifest/).

#### [](#lighthouse)Lighthouse

[Lighthouse](https://chrome.google.com/webstore/detail/lighthouse/blipmdconlkpinefehnmjammfjpmpbjk?utm_source=chrome-ntp-icon) is a tool to assess the quality of web applications. Install it and then on your chrome developer console click _Generate report_. Now let's check how our app performs:

[![Alt Text](https://res.cloudinary.com/practicaldev/image/fetch/s--pnaPQAfd--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_800/https://dev-to-uploads.s3.amazonaws.com/i/r4pi3neut8ffk9q1zk2n.png)](https://res.cloudinary.com/practicaldev/image/fetch/s--pnaPQAfd--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_800/https://dev-to-uploads.s3.amazonaws.com/i/r4pi3neut8ffk9q1zk2n.png)

Well, we have a pretty good score as per _Lighthouse_. As you can see there is one test that is still not passing which is responsible for keeping our _Performance_ score low.

[![Alt Text](https://res.cloudinary.com/practicaldev/image/fetch/s--99mVyzME--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_800/https://dev-to-uploads.s3.amazonaws.com/i/ig20ipdb5bvwhoydcv9s.png)](https://res.cloudinary.com/practicaldev/image/fetch/s--99mVyzME--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_800/https://dev-to-uploads.s3.amazonaws.com/i/ig20ipdb5bvwhoydcv9s.png)

#### [](#deploying-the-application)Deploying the application

In order to overcome the error of not redirecting HTTP traffic to HTTPS, we will have to deploy our application.  
Go to your terminal and enter, `npm run build` to create build folder in your project directory.  
Create an account on [Netlify](https://www.netlify.com/) and on your dashboard that looks something like this:

[![Alt Text](https://res.cloudinary.com/practicaldev/image/fetch/s--UJfYV0IR--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_800/https://dev-to-uploads.s3.amazonaws.com/i/l73pl961nlldkumuimc9.png)](https://res.cloudinary.com/practicaldev/image/fetch/s--UJfYV0IR--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_800/https://dev-to-uploads.s3.amazonaws.com/i/l73pl961nlldkumuimc9.png)

Just drag and drop your build folder onto this screen and that's all it takes to deploy your application online on netlify.

Click the generated [URL](https://weather-application-pwa.netlify.app/) to see your application for real on the internet, try and disconnect your internet to see the offline page too.

## [](#result)**Result**

Now, let's run a Lighthouse test on our deployed application:

[![Alt Text](https://res.cloudinary.com/practicaldev/image/fetch/s--3Afi6BS3--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_800/https://dev-to-uploads.s3.amazonaws.com/i/ngigz6j64t8mpvfz05i7.png)](https://res.cloudinary.com/practicaldev/image/fetch/s--3Afi6BS3--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_800/https://dev-to-uploads.s3.amazonaws.com/i/ngigz6j64t8mpvfz05i7.png)

Amazing! That's a great score for our PWA application.  
Now, if you have done everything right, then you should see a **+** icon next to your bookmark icon on url search bar on chrome.

[![Alt Text](https://res.cloudinary.com/practicaldev/image/fetch/s--zkkDgoyv--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_800/https://dev-to-uploads.s3.amazonaws.com/i/8many9vex3k1bfz208c2.png)](https://res.cloudinary.com/practicaldev/image/fetch/s--zkkDgoyv--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_800/https://dev-to-uploads.s3.amazonaws.com/i/8many9vex3k1bfz208c2.png)

Now, this is the button that will allow you to install this application on your device. Click on the **+** icon and install the application.

[![Alt Text](https://res.cloudinary.com/practicaldev/image/fetch/s--_RSjbwUz--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_800/https://dev-to-uploads.s3.amazonaws.com/i/5vfgl8pe5kpyw7y71g86.png)](https://res.cloudinary.com/practicaldev/image/fetch/s--_RSjbwUz--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_800/https://dev-to-uploads.s3.amazonaws.com/i/5vfgl8pe5kpyw7y71g86.png)

Disconnect your internet connection to see the offline page.

[![Alt Text](https://res.cloudinary.com/practicaldev/image/fetch/s--rb4XMKcs--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_800/https://dev-to-uploads.s3.amazonaws.com/i/kvertm63yc3x5s2govxb.png)](https://res.cloudinary.com/practicaldev/image/fetch/s--rb4XMKcs--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_800/https://dev-to-uploads.s3.amazonaws.com/i/kvertm63yc3x5s2govxb.png)

That's really wonderful. The application is now native to your system and you can use it on your mobile too.

Now for the most amazing part - Publishing the app on PWA store. Head over to [PWA Store](https://progressiveapp.store/home) and signup. After logging in, go to your profile page and click on the hamburger icon on the far right, and click on the little **+** symbol. Enter all the details of your application including name, description, screenshots, etc. Finally, run the Lighthouse PWA check. After getting all three ticks, you can submit it for review.

Voila! That's it. After review, your app will be published on the PWA store and after some time you can find it under _Discover_ section.

This has been a long article, yet an informative one. I hope you understood every bit of what a Progressive Web App is, how you could build one, testing it using Lighthouse tool and also deploying the PWA application.

In case of any queries, please feel free to contact me on my [LinkedIn](https://www.linkedin.com/in/k-g-prajwal-a6b3b517a/). The code is available on my [Github](https://github.com/K-G-PRAJWAL/ReactJS-Projects/tree/master/weather-app).

#### [](#thank-you)**_Thank You!_**
