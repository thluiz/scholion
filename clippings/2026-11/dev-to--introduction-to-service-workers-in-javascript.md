---
url: "https://dev.to/attacomsian/introduction-to-server-workers-in-javascript-1epa"
captured_at: "2026-11-16T19:08:35+00:00"
title: "Introduction to Service Workers in JavaScript"
domain: "dev-to"
---

_This post was originally published on [attacomsian.com/blog](https://attacomsian.com/blog/service-workers-javascript)._

* * *

Service workers are a core part of Progressive Web Apps that allow caching of resources and [web push notifications](https://attacomsian.com/blog/desktop-notifications-javascript), among other things, to create an effective offline experience. They act as a proxy between web applications, the browser, and the network, allowing developers to intercept and cache network requests and take appropriate action based on the availability of the network.

A service worker runs on a separate thread, so it is non-blocking. This also means that it does not have access to [DOM](https://attacomsian.com/blog/getting-dom-elements-javascript) and other APIs available in the main JavaScript thread like cookies, XHR, web storage APIs (local storage and session storage), etc. Since they are designed to be fully asynchronous, they heavily use [promises](https://attacomsian.com/blog/promises-javascript) to wait for responses of network requests.

> Due to security concerns, service workers only run over HTTPS and cannot be used in private browsing mode. However, you do not need a secure connection while making location requests (good enough for testing).

## [](#browser-support)Browser Support

The service worker is a relatively new API that is only supported by [modern web browsers](https://caniuse.com/#feat=serviceworkers). Therefore, we first need to check if the API is supported by the browser:  

```
if('serviceWorker' in navigator) {
    // Supported 😍
} else {
    // Not supported 😥
}
```

Enter fullscreen mode Exit fullscreen mode

## [](#service-worker-registration)Service Worker Registration

Before we start caching the resources or intercepting network requests, we must install a service worker in the browser. Since a service worker is essentially a JavaScript file, it can be registered by specifying the path of the file. The file must be accessible over the network and should only contain service worker code.

You should wait until the page is loaded, then pass the service worker file path to `navigator.serviceWorker.register()` method:  

```
window.addEventListener('load', () => {
    if ('serviceWorker' in navigator) {
        // register service worker
        navigator.serviceWorker.register('/sw-worker.js').then(
            () => {
                console.log('SW registration succesful 😍');
            },
            err => {
                console.error('SW registration failed 😠', err)
            });
    } else {
        // Not supported 😥
    }
});
```

Enter fullscreen mode Exit fullscreen mode

You can run the above code every time a page loads without any trouble; the browser will decide if the service worker is already installed or not and handle it accordingly.

## [](#service-worker-lifecycle)Service Worker Lifecycle

The registration lifecycle consists of three steps:

1.  Download
2.  Install
3.  Activate

When a user first visits your website, the service worker file is immediately downloaded and installation is attempted. If the installation is successful, the service worker is activated. Any functionality that's inside the service worker file is not made available until the user visits another page or refresh the current page.

## [](#browser-events)Browser Events

Once the service worker is installed and activated, it can start intercepting network requests and caching resources. This can be done by listening to events emitted by the browser inside the service worker file. The browser emits the following events:

*   `install` is emitted when the service worker is being installed.
*   `activate` is sent when the service worker has been successfully registered and installed. This event can be used to remove outdated cache resources before installing a new version.
*   `fetch` is emitted whenever the web page requests a network resource. It can be anything: a new HTML document, an image, a JSON API, a stylesheet or JavaScript file, whatever that is available on a remote location.
*   `push` is sent by the Push API when a new push notification is received. You can use this event to [display a notification](https://attacomsian.com/blog/desktop-notifications-javascript#showing-notification) to the user.
*   `sync` is invoked when the browser detects network availability after the connection was lost.

## [](#serving-cached-resources)Serving Cached Resources

We can listen to `install` event when the service worker is installing to cache specific resources that would be need to serve the page when we are out of network:  

```
const CACHE_NAME = 'site-name-cache';

self.addEventListener('install', event => {
    event.waitUntil(
        caches
            .open(CACHE_NAME)
            .then(cache =>
                cache.addAll([
                    'favicon.ico',
                    'projects.json',
                    'style.css',
                    'index.js',
                    'https://fonts.googleapis.com/css?family=Open+Sans:400,700'
                ])
            )
    );
});
```

Enter fullscreen mode Exit fullscreen mode

The above example code uses the Cache API to store the resources in a cache named `site-name-cache`.

> The `self` is a read-only global property that is used by the service workers to get access to themselves.

Now let us listen for a `fetch` event to check if the requested resource was already stored in the cache, and return it back if found:  

```
// ...
self.addEventListener('fetch', event => {
    event.respondWith(
        caches.match(event.request).then(response => {
            if (response) {
                //found cached resource
                return response;
            }
            return fetch(event.request);
        })
    );
});
```

Enter fullscreen mode Exit fullscreen mode

We look for a cache entry for the resource identified by the `request` property, and if not found, we make a [fetch request](https://attacomsian.com/blog/javascript-fetch-api) to get it. If you want to cache new requests too, you can do it by handling the response of the fetch request and then adding it to the cache, like below:  

```
//...
self.addEventListener('fetch', event => {
    event.respondWith(
        caches.match(event.request).then(response => {
            if (response) {
                //found cached resource
                return response;
            }

            // get resource and add it to cache
            return fetch(event.request)
                .then(response => {
                    // check if the response is valid
                    if (!response.ok) {
                        return response;
                    }

                    // clone the response
                    const newResponse = response.clone();

                    // add it to cache
                    caches.open(CACHE_NAME)
                        .then(cache =>
                            cache.put(event.request, newResponse)
                        );

                    // return response
                    return response;
                });
        })
    );
});
```

Enter fullscreen mode Exit fullscreen mode

## [](#service-worker-update)Service Worker Update

When the service worker is installed, it continues to run until it is removed by the user or updated. To update a service worker, all you need to do is upload a new version of the service worker file on the server. When the user visits your site, the browser will automatically detect the file changes (even just one byte is enough), and install the new version.

Just like the first time installation, the new service worker functionality will only be available when the user navigates to another page or refresh the current page.

On thing we can do is listen for `activate` event and remove the old cache resources. The following code does this by looping over all caches and deleting the cache that matches our cache name:  

```
// ...
self.addEventListener('activate', event => {
    event.waitUntil(
        caches.keys().then(keys => {
            return Promise.all(
                keys.map(cache => {
                    if (cache === CACHE_NAME) {
                        return caches.delete(cache);
                    }
                })
            );
        })
    );
});
```

Enter fullscreen mode Exit fullscreen mode

That's all for service workers introduction. If you want to learn more, check out [ServiceWorker Cookbook](https://serviceworke.rs/) — a collection of working, practical examples of using service workers in modern web sites.

* * *

✌️ I write about **modern JavaScript, Node.js, Spring Boot**, and all things **web development**. [**Subscribe to my newsletter**](https://attacomsian.com/newsletter) to get web development tutorials & protips every week.

* * *

**Like this article?** [Follow @attacomsian on Twitter](https://twitter.com/attacomsian). You can also follow me on [LinkedIn](https://linkedin.com/in/attacomsian) and [DEV](https://dev.to/attacomsian).
