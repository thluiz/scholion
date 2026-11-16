---
url: "https://dev.to/thisdotmedia/intro-to-pwa-and-service-workers-15d4"
captured_at: "2026-11-16T00:46:15+00:00"
title: "Intro to PWAs and Service Workers"
domain: "dev-to"
---

## [](#progressive-web-apps)Progressive Web Apps

Progressive Web Apps, aka PWAs, are becoming more and more popular everyday. In this article, I'm going to tell you what a progressive web app is, and how to create one using a service worker.

## [](#what-is-a-pwa)What is a PWA?

A PWA is an app that is intended to behave like a native app on your phone. It's a regular web app that, when you open it on your browser, displays a message saying  
"**Add to Home Screen**" once you click on the message, your app will be installed on your phone and you will see the logo on your device's home screen.

PWAs are becoming very popular because they help increasing the user experience when visiting a website. When visiting a traditional website, it can take several seconds. A PWA's loading time, however, is significantly faster thanks to the use of Service Workers.

There are 3 types of apps you can have on your device:

\-Native  
\-Hybrid  
\-PWA

**Native**: in my opinion unless you are using high graphics, and performing heavy user interaction with the a device (like playing games), I would go with a Native app. Native Apps are expensive to build since they require double effort and time - two separate apps need to be built for Android and iOS.

**Hybrid**: a good way to go, since you have one stack that creates separate builds for Android and iOS platforms from the same sources. I would use hybrid apps if you don't require high speed and graphics on your app. With hybrid apps, you do have access to the device hardware via plugins that are built with native code.

**What about PWA?**

**PWA**: They are cheaper than the previous types of apps when it comes to developing, quick to develop, and they work offline! The same way that you develop a regular responsive web app, you can develop a PWA with the difference of adding a **service worker** to enable offline support, and things like installing the app on your home screen.

## [](#what-is-a-service-worker)What is a Service Worker?

A service worker is a script that is running separately from our website - in the background. Service workers are awesome, they can help us reach different things like caching pages, caching API calls, push notifications, background sync, and more.

*   A service worker **can cache** network requests.
    
*   A service worker **can handle** how network requests are done in your website.
    
*   A service worker **can make the use** of the\_\_ Background Sync API\_\_ which allows you to defer actions until the user has stable connectivity.
    
*   A service worker can't access/interact the DOM directly.
    
*   A service worker **can cache** your things from your website, like static assets.
    
*   A service worker **can receive** push notifications when the app is not active.
    
*   A service worker stays inactive when it's not in use. When it gets the "**signal**" to be used, it reactivates again.
    
*   A service worker **can be used** to make your app work offline.
    

## [](#service-workers-lifecycle)Service Worker's Lifecycle

\-**Register the service worker**:

The first step into the service worker's lifecycle is to register the service worker. You can do so using the following code:  

```
if ('serviceWorker' in navigator) {
  navigator.serviceWorker.register('/sw.js');
}
```

Enter fullscreen mode Exit fullscreen mode

Jeff Posnick from Google taught me a little trick in one of his articles about service workers. This trick is a simple way to improve the registration of the service worker.  

```
if ('serviceWorker' in navigator) {
  window.addEventListener('load',()=> {
    navigator.serviceWorker.register('/service-worker.js');
  });
}
```

Enter fullscreen mode Exit fullscreen mode

This code will register the service worker once the whole page has loaded, but keep in mind that you might delay the registration of the service worker this way.

\-**Installing the service worker**: This process is only called once after the service worker has been loaded. If you modify the existing service worker, the browser will update, and install the service worker again.

There is an `install` event that gets emitted while the service worker is being installed. You can handle this event, and perform some async actions if needed (e.g., caching static assets). For this purpose, you can use _**event.waitUntil()**_. This method will keep the service worker in the `install` phase until the promise passed to _**event.waitUntil()**_ is settled. Depending on whether that promise is resolved or rejected, the `install` phase will either finish successfully, or won't.

In order to install the service worker, we need to do the following:

1) Open a cache.  
2) Cache our files.  
3) Confirm whether all the required assets are cached or not.  

```
const web_cache = 'web-app-cache-v1.0';
const filesToCache = [
  '/',
  '/styles/styles.css',
  '/script/main.js'
  ....
];

self.addEventListener('install',(event)=> {
  event.waitUntil(
    caches.open(web_cache)
      .then((cache)=> {
        //Cache has been opened successfully
        return cache.addAll(filesToCache);
      })
  );
});
```

Enter fullscreen mode Exit fullscreen mode

The following are instruction on how to check if your service workers have been successfully installed and registered directly in the browser.

In Chrome (duhhh)

1) Open dev tools  
2) In the toolbar click on _**Application**_  
3) On your left side, you will see a sidebar. Click on service worker.  
4) You should see something like the following:  
[![Screen Shot 2020-01-12 at 4.03.27 PM](https://images.ctfassets.net/zojzzdop0fzx/53NzTWyIk07RoS8QXQGbSA/d2f562d8ba19e0af9d0990bfc9c8f2ce/Screen_Shot_2020-01-12_at_4.03.27_PM.png)](https://images.ctfassets.net/zojzzdop0fzx/53NzTWyIk07RoS8QXQGbSA/d2f562d8ba19e0af9d0990bfc9c8f2ce/Screen_Shot_2020-01-12_at_4.03.27_PM.png)

\-**Activating the service worker**:

The service worker can get into the activating state in different scenarios. Here are some of those scenarios:

*   we don't have the existing service worker in our app
*   we run the _**self.skipWaiting()**_ method in the service worker
*   the user has navigated away from the page, releasing the previous active worker
*   a set period of time has passed releasing the previous active worker

\-**Active service worker:**

When a service worker is active, you can check its status inside of the register object.  

```
navigator.serviceWorker.register('./service-worker.js').then((registration)=> {
    if (registration.active) {
        console.log('Service worker is active');
    }
})
```

Enter fullscreen mode Exit fullscreen mode

\-**Redundant service worker**:

A Service Worker can be redundant (aka something went WRONG) because of the following reasons:

*   the installation of the service worker failed
*   the service worker failed when it was getting activated
*   a new service worker replaces the existing service worker as the active service worker

**That's all folks!**

**Sources**:

\-[https://developers.google.com/web/fundamentals/primers/service-workers](https://developers.google.com/web/fundamentals/primers/service-workers)  
\-[https://bitsofco.de/the-service-worker-lifecycle/](https://bitsofco.de/the-service-worker-lifecycle/)  
\-[https://developers.google.com/web/fundamentals/primers/service-workers/lifecycle](https://developers.google.com/web/fundamentals/primers/service-workers/lifecycle)
