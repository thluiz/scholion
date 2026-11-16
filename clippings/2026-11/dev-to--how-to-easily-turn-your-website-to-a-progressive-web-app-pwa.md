---
url: "https://dev.to/dfiredeveloper/how-to-easily-turn-your-website-to-a-progressive-web-app-pwa-2nm4"
captured_at: "2026-11-16T01:01:31+00:00"
title: "How to easily turn your website to a Progressive Web App(PWA)"
domain: "dev-to"
---

Progressive Web App is the new and trending way to bring a native app feeling into a normal or traditional web app. Progressive Web Apps are very much in use by some of the biggest companies like Twitter, Forbes, Alibaba, Instagram, Flipkart e.t.c and have gained popularity.

So in this tutorial, we’ll be turning our already existing website into a Progressive Web App. Let’s Get Started :)

## [](#intro)Intro

I’m sure by now you must have heard or read about Progressive Web Applications and if you haven’t here is it.

A progressive web application (PWA) is a type of application software delivered through the web, built using common web technologies including HTML, CSS, and JavaScript. It is intended to work on any platform that uses a standards-compliant browser. Functionality includes working offline, push notifications, and device hardware access, enabling creating user experiences similar to native applications on desktop and mobile devices.

Progressive Web Apps are largely characterized by the following:

*   **Reliable** — They load instantly and never show the “No Internet Connection” page, even in uncertain network conditions with help from Service workers caching.
    
*   **Fast** — They respond quickly to user interactions with smooth animations.
    
*   **Engaging** — They feel like a natural app on the device, with immersive user experience.
    

### [](#requirements-for-this-tutorial)Requirements for this tutorial

1.  Basic web design skills (HTML, CSS & JS)
    
2.  You need to be running on HTTPS
    
3.  A working website you wish to tun to PWA.
    

Like I said, building a Progressive Web App is quite simple and easy if you understand the whole concept and how it actually works.

### [](#what-makes-up-a-pwa)What Makes up a PWA

1.  Web Manifest
2.  Service Worker
3.  Your static website

##### [](#lets-start)Let’s Start

For the sake of this tutorial, we’ll be turning a simple random quote web app to a PWA. All the files are hosted here on [Github](https://github.com/IgalaDigital/Igala-Facts) and the demo is available [Here](https://igalafacts.netlify.app/)

So for the sake of making sure things go right, we’ll rebuild the simple random quote web app using HTML, CSS, and JavaScript.

[![Final Project](https://media2.dev.to/cdn-cgi/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fi%2F5nc4uk3nqftz2z9gefkz.png)](https://media2.dev.to/cdn-cgi/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fi%2F5nc4uk3nqftz2z9gefkz.png)  
That's how the final project will look like.

So let’s build the UI.

Make a new directory and create these files

*   `index.html`
    
*   `css/style.css`
    
*   `js/app.js`
    

**Let's Build the Markup**.

Add the below codes in the `index.html`  

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>The Igala Facts you never knew</title>
    <link rel="stylesheet" href="css/style.css">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/font-awesome/4.5.0/css/font-awesome.min.css">
    <link href='https://fonts.googleapis.com/css?family=Roboto+Slab:400,700' rel='stylesheet' type='text/css'>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/animate.css/3.2.3/animate.min.css">
</head>
<body>
    <div class="container">
        <div class="row">
          <div class="col-sm-6">
            <h1><span class="main-color">Random Igala</span><br />Facts</h1>
            <p>The best facts about Igala in one place. You can easily see the best facts and  share the ones you love on twitter with one click.</p>
          </div>
          <div class="col-sm-6">
            <div class="row">
              <div class="col-xs-6">
                <a id="next-quote" class="btn btn-lg btn-default btn-block" href="#"><i class="fa fa-refresh"></i> Next Fact</a>
              </div>
              <div class="col-xs-6">
                <a id="share" class="btn btn-lg btn-default btn-block" href="#" target="_top"><i class="fa fa-twitter"></i> Share</a>
              </div>
            </div>

            <div id="quote-box">
              <i id="quote-left" class="fa fa-quote-left"></i>
              <p id="quote"></p>
              <span id="author" class="main-color"></span>
              <i id="quote-right" class="fa fa-quote-right"></i>
            </div>

            <div class="row">       
              <div class="col-xs-12">
                <ul>
                  <li>Follow Us</li>
                  <li><a class="main-color" href="https://facebook.com/theigaladigital" target="_blank">@theigaladigital</a></li>
                    </ul>
                  </div>
              </div>
            </div>
          </div>
        </div>
      </div>

      <div id="hidden"></div>
      <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/2.1.3/jquery.min.js"></script>
      <script src="js/app.js"></script>
</body>
</html>
```

Enter fullscreen mode Exit fullscreen mode

Like I said earlier, this tutorial is mainly teaching you how to convert your already existing website into a Progressive Web App so I won’t be going in detail on the HTML or rest.

— Add this in `css/app.css`  

```
body {
    background-color: rgb(0, 0, 0);
    color: white;
    padding-top: 50px;
    font-size: 18px;
    font-family: 'Roboto Slab', serif;
  }

  h1 {
    font-size: 4em;
    line-height: 70px;
    margin-bottom: 40px;
    font-weight: bold;
  }

  a:hover, a:focus, a:active {
    text-decoration: none;
    color: white;
    transition: color 0.8s;
  }

  .main-color {
    color: yellow;
    text-shadow: 1px 1px 0 rgba(255, 255, 255, 0.2);
    font-weight: bold;
  }

  #quote-box {
    background-color: rgba(255, 255, 255, 0.3);
    border-radius: 10px;
    padding: 100px 40px;
    position: relative;
    margin-top: 20px;
  }

  #quote-left, #quote-right {
    color: yellow;
    font-size: 3em;
    position: absolute;
  }

  #quote-left {
    top: 20px;
    left: 20px;
  }

  #quote-right {
    bottom: 20px;
    right: 20px;
  }

  #quote {
    font-size: 1.5em;
    text-align: center;
  }

  #author {
    position: absolute;
    font-size: 1.1em;
    left: 50px;
    bottom: 30px;
  }

  .btn {
    border-radius: 10px;
    color: yellow;
    border: 1px solid white !important;
    transition: background 0.8s, color 0.8s;
    line-height: 30px;
    margin-top: 30px;
  }

  .btn:hover, .btn:active, .btn:focus {
    color: white !important;
    background-color: yellow !important;
    box-shadow: none;
  }

  ul {
    list-style-type: none;
    padding: 0;
    margin: 10px 0 0 0;
    float: right;
    white-space: nowrap;
    overflow: hidden;
  }

  li {
    display: inline-block;
    margin: 0 0 0 1px;
  }

  #hidden {
    display: none;
  }
```

Enter fullscreen mode Exit fullscreen mode

Now your app should look like this:  
[![Front Page](https://media2.dev.to/cdn-cgi/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fi%2Fyk9djxzmb6lwe1k6g20i.png)](https://media2.dev.to/cdn-cgi/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fi%2Fyk9djxzmb6lwe1k6g20i.png)

If you look up closely, you will discover no quote shows, so we’ll have to add JavaScript functionality that handles that.

— Add this in `js/app.js`  

```
$(document).ready(function () {  
    $("#next-quote").on("click", function (e) {
      e.preventDefault();

      var randomQuoteNumber = getRandomQuoteNumber();
      updateQuote(randomQuoteNumber);
    });

    var q = location.search.split("?q=")[1];

    if (q >= 0 && q < quotes.length) {
      updateQuote(q);
    } else {
      $("#next-quote").click();
    }
  });

  function updateQuote(quoteNumber) {
    var randomQuote = quotes[quoteNumber];

    $("#quote").html(randomQuote.quote);
    $("#author").html(randomQuote.author);
    $("#quote-box").removeClass().addClass("animated bounceIn").one('webkitAnimationEnd mozAnimationEnd MSAnimationEnd oanimationend animationend', function() {
      $(this).removeClass();
    });

    $("#share").attr("href", "https://twitter.com/intent/tweet?text=\"" + encodeURIComponent($("#hidden").html(randomQuote.quote).text()) + "\" https://igalafacts.igaladigital.org?q=" + quoteNumber);
  }

  function getRandomQuoteNumber() {
    return Math.floor(Math.random() * quotes.length);
  }

  var quotes = [{"author": "IgalaDigital", "quote": "Did You Know That Ojaina is the place where the Attah's of Igala are burried?"},
{"author": "IgalaDigital", "quote": "Did You Know That the first aircraft that visited the Igala Kingdom landed at Idah in 1955?"},
{"author": "IgalaDigital", "quote": "Did You Know That Attah Ameh Oboni, had seen to the completion of an aerodrome in 1954 at Idah?"},

  {"author": "Ilemona", "quote": "Did you know that the Igala alphabet was adopted from the English alphabet. The latter has five (5) vowels: “a,” “e,” “i,” “o,” “u.”?"},
{"author": "Achimugu Ilemona", "quote": "Did you know the Igala alphabet is made up of thirty-one (31) letters: some vowels, others consonants?"},
{"author": "IgalaDigital", "quote": "Did You Know That Ojaina is a restricted place only allowed for members from the Attah Ruling House?"},
{"author": "IgalaDigital", "quote": "Did you know that Ata Ameh Oboni speak fluently in Igala, Ebira & Hausa?"},
{"author": "Onuche Joseph", "quote": "Did you know that the Ígálá language has seven (7) vowels: “a,” “e,” “ẹ,” “i,” “o,” “ọ,” “u” (encompassing both all the 5 English vowels and two indigenous ones, ‘ẹ’ and  ‘ọ’).?"},

  {"author": "Naomi", "quote": "Did You Know That Idah is also called Idah Alu Ogo Oja Abutu Eje?"},

  {"author": "Inikpi", "quote": "Did you know that Abutu- Eje was the first Igala Ruler?"},
{"author": "IgalaDigital", "quote": "Did you know that you may likely come home to meet one of your family member dead if you kill an animal at Ojaina?"},
{"author": "IgalaDigital", "quote": "Did you know that ata Ameh Oboni took his own life on the night of June 26, 1956?"},
{"author": "IgalaDigital", "quote": "Did you know that the mighty Ata Ameh Oboni died at the age of 51?"},
{"author": "IgalaDigital", "quote": "Did you know that attah Ameh Oboni schooled in Okene(Ebira Land) between 1934 and 1939? Learned in Hausa Literature"},
{"author": "IgalaDigital", "quote": "Did you know that ata Ameh Oboni started off as a market stall tax collector for Idah and Ejule market?"},
{"author": "IgalaDigital", "quote": "Did you know that Ata Obaje Ocheje moved Ameh Oboni from being a market stall tax collector to be come a cheif as onu ugwolawo due to his hard work?"},
{"author": "IgalaDigital", "quote": "Did you know that Ameh Oboni was moved to ankpa from ugwolawo as the judge, commonly known as *Wakali, to be in charge of seven districts?"},
{"author": "IgalaDigital", "quote": "Did you know that Patrick A. Okpanachi, Mallam Garba and Peter Achimugwu were the first in Igala Land that speaks and write in English Language?"},
{"author": "IgalaDigital", "quote": "Did you know that Peter Achimugwu was the man that led the campaign to remove Ameh Oboni as the Attah?"}
]
```

Enter fullscreen mode Exit fullscreen mode

> This is just basic JavaScript, if you have no idea what all this means, you should get [JavaScript Teacher’s](https://medium.com/u/6727c1eb71f8?source=post_page-----b55ed4a86413----------------------) _`Grammar JavaScript`_ book. This will teach you all the basics and contents of Modern JavaScript. Get a free copy [here](http://www.javascriptgrammar.com/)

Now you should have a functioning app with the facts showing.

[![Functioning App](https://media2.dev.to/cdn-cgi/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fi%2F5nc4uk3nqftz2z9gefkz.png)](https://media2.dev.to/cdn-cgi/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fi%2F5nc4uk3nqftz2z9gefkz.png)

## [](#lets-turn-it-to-a-pwa)Let’s Turn it to a PWA

The three basic criteria for a PWA:

*   **Web Manifest**

The web app manifest is a JSON file that tells the browser about your Progressive Web App and how it should behave when installed on the user’s desktop or mobile device. A typical manifest file includes the app name, the icons the app should use, and the URL that should be opened when the app is launched.

*   **Service Worker**  
    A service worker is a script that allows your browser to run in the background, separate from a web page, opening the door to features that don’t need a web page or user interaction. Today, they already include features like push notifications and background sync.
    
*   **Icons**  
    These icons control your application and are provided in different sizes for different devices. Your PWA app will not work without them.
    

Now let’s get started.

> Before we proceed, ensure you’re using a live server  
> Use ([Web server for Chrome](https://chrome.google.com/webstore/detail/web-server-for-chrome/ofhbbkphhbklhfoeikjpcbhemlocgigb?hl=en), or [VSCode Live Server](https://marketplace.visualstudio.com/items?itemName=ritwickdey.LiveServer)

Create the following files:

`sw.js` (In root directory)

`manifest.json` (In root directory)

`img/icons` (Where we’d store our icons

> First, we need to check if the browser supports service workers and register a new one.

In `js/app.js` add  

```
if ('serviceWorker' in navigator) {
  window.addEventListener('load', () => {
   navigator.serviceWorker.register('../sw.js').then( () => {
    console.log('Service Worker Registered')
   })
 })
}
```

Enter fullscreen mode Exit fullscreen mode

[![Dev Tool](https://media2.dev.to/cdn-cgi/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fi%2Ftu9uxl1zoj3v8cx0l46e.png)](https://media2.dev.to/cdn-cgi/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fi%2Ftu9uxl1zoj3v8cx0l46e.png)

[![Dev Tool](https://media2.dev.to/cdn-cgi/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fi%2Fnumvk4pf5pr9vayaauae.png)](https://media2.dev.to/cdn-cgi/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fi%2Fnumvk4pf5pr9vayaauae.png)

Your final `app.js` should look like this  

```
$(document).ready(function () {  
    $("#next-quote").on("click", function (e) {
      e.preventDefault();

      var randomQuoteNumber = getRandomQuoteNumber();
      updateQuote(randomQuoteNumber);
    });

    var q = location.search.split("?q=")[1];

    if (q >= 0 && q < quotes.length) {
      updateQuote(q);
    } else {
      $("#next-quote").click();
    }
  });

  function updateQuote(quoteNumber) {
    var randomQuote = quotes[quoteNumber];

    $("#quote").html(randomQuote.quote);
    $("#author").html(randomQuote.author);
    $("#quote-box").removeClass().addClass("animated bounceIn").one('webkitAnimationEnd mozAnimationEnd MSAnimationEnd oanimationend animationend', function() {
      $(this).removeClass();
    });

    $("#share").attr("href", "https://twitter.com/intent/tweet?text=\"" + encodeURIComponent($("#hidden").html(randomQuote.quote).text()) + "\" https://igalafacts.igaladigital.org?q=" + quoteNumber);
  }

  function getRandomQuoteNumber() {
    return Math.floor(Math.random() * quotes.length);
  }

  var quotes = [{"author": "IgalaDigital", "quote": "Did You Know That Ojaina is the place where the Attah's of Igala are burried?"},
{"author": "IgalaDigital", "quote": "Did You Know That the first aircraft that visited the Igala Kingdom landed at Idah in 1955?"},
{"author": "IgalaDigital", "quote": "Did You Know That Attah Ameh Oboni, had seen to the completion of an aerodrome in 1954 at Idah?"},

  {"author": "Ilemona", "quote": "Did you know that the Igala alphabet was adopted from the English alphabet. The latter has five (5) vowels: “a,” “e,” “i,” “o,” “u.”?"},
{"author": "Achimugu Ilemona", "quote": "Did you know the Igala alphabet is made up of thirty-one (31) letters: some vowels, others consonants?"},
{"author": "IgalaDigital", "quote": "Did You Know That Ojaina is a restricted place only allowed for members from the Attah Ruling House?"},
{"author": "IgalaDigital", "quote": "Did you know that Ata Ameh Oboni speak fluently in Igala, Ebira & Hausa?"},
{"author": "Onuche Joseph", "quote": "Did you know that the Ígálá language has seven (7) vowels: “a,” “e,” “ẹ,” “i,” “o,” “ọ,” “u” (encompassing both all the 5 English vowels and two indigenous ones, ‘ẹ’ and  ‘ọ’).?"},

  {"author": "Naomi", "quote": "Did You Know That Idah is also called Idah Alu Ogo Oja Abutu Eje?"},

  {"author": "Inikpi", "quote": "Did you know that Abutu- Eje was the first Igala Ruler?"},
{"author": "IgalaDigital", "quote": "Did you know that you may likely come home to meet one of your family member dead if you kill an animal at Ojaina?"},
{"author": "IgalaDigital", "quote": "Did you know that ata Ameh Oboni took his own life on the night of June 26, 1956?"},
{"author": "IgalaDigital", "quote": "Did you know that the mighty Ata Ameh Oboni died at the age of 51?"},
{"author": "IgalaDigital", "quote": "Did you know that attah Ameh Oboni schooled in Okene(Ebira Land) between 1934 and 1939? Learned in Hausa Literature"},
{"author": "IgalaDigital", "quote": "Did you know that ata Ameh Oboni started off as a market stall tax collector for Idah and Ejule market?"},
{"author": "IgalaDigital", "quote": "Did you know that Ata Obaje Ocheje moved Ameh Oboni from being a market stall tax collector to be come a cheif as onu ugwolawo due to his hard work?"},
{"author": "IgalaDigital", "quote": "Did you know that Ameh Oboni was moved to ankpa from ugwolawo as the judge, commonly known as *Wakali, to be in charge of seven districts?"},
{"author": "IgalaDigital", "quote": "Did you know that Patrick A. Okpanachi, Mallam Garba and Peter Achimugwu were the first in Igala Land that speaks and write in English Language?"},
{"author": "IgalaDigital", "quote": "Did you know that Peter Achimugwu was the man that led the campaign to remove Ameh Oboni as the Attah?"}
]
if ('serviceWorker' in navigator) {
  window.addEventListener('load', () => {
   navigator.serviceWorker.register('../sw.js').then( () => {
    console.log('Service Worker Registered')
   })
 })
}
```

Enter fullscreen mode Exit fullscreen mode

We’re going to use the Workbox library to power our service worker

> Workbox is a set of libraries and Node modules developed by Google that make it easy to cache assets and take full advantage of features used to build Progressive Web Apps.

The idea of our service worker is to cache all files (Fonts, JavaScript, CSS, Images, e.t.c) so we can access them offline after the page loads.

The important thing to understand about the **Service Worker** is that you are in control of the network. You get to decide what is cached, how it is cached, and how it should be returned to the user.

— In `sw.js` add this:  

```
importScripts('https://storage.googleapis.com/workbox-cdn/releases/4.3.1/workbox-sw.js');
if (workbox) {
    console.log("Yay! Workbox is loaded !");
    workbox.precaching.precacheAndRoute([]);
/*  cache images in the e.g others folder; edit to other folders you got
   and config in the sw-config.js file
    */
    workbox.routing.registerRoute(
        /(.*)others(.*)\.(?:png|gif|jpg)/,
        new workbox.strategies.CacheFirst({
            cacheName: "images",
            plugins: [
                new workbox.expiration.Plugin({
                    maxEntries: 50,
                    maxAgeSeconds: 30 * 24 * 60 * 60, // 30 Days
                })
            ]
        })
    );
    /* Make your JS and CSS âš¡ fast by returning the assets from the cache,
  while making sure they are updated in the background for the next use.
  */
    workbox.routing.registerRoute(
    // cache js, css, scc files
        /.*\.(?:css|js|scss|)/,
        // use cache but update in the background ASAP
        new workbox.strategies.StaleWhileRevalidate({
            // use a custom cache name
            cacheName: "assets",
        })
    );
// cache google fonts
    workbox.routing.registerRoute(
        new RegExp("https://fonts.(?:googleapis|gstatic).com/(.*)"),
        new workbox.strategies.CacheFirst({
            cacheName: "google-fonts",
            plugins: [
                new workbox.cacheableResponse.Plugin({
                    statuses: [0, 200],
                }),
            ],
        })
    );
// add offline analytics
    workbox.googleAnalytics.initialize();
/* Install a new service worker and have it update
and control a web page as soon as possible
*/
workbox.core.skipWaiting();
    workbox.core.clientsClaim();
} else {
    console.log("Oops! Workbox didn't load ðŸ‘º");
}
```

Enter fullscreen mode Exit fullscreen mode

Now our service worker works and would cache files once the page loads.

Now let’s make our app installable.

— Add this in `manifest.json`  

```
{
    "name": "Igala Facts",
    "short_name": "Igala Facts",
    "icons": [
      {
        "src": "img/icons/icon-72x72.png",
        "sizes": "72x72",
        "type": "image/png"
      },
      {
        "src": "img/icons/icon-96x96.png",
        "sizes": "96x96",
        "type": "image/png"
      },
      {
        "src": "img/icons/icon-128x128.png",
        "sizes": "128x128",
        "type": "image/png"
      },
      {
        "src": "img/icons/icon-144x144.png",
        "sizes": "144x144",
        "type": "image/png"
      },
      {
        "src": "img/icons/icon-152x152.png",
        "sizes": "152x152",
        "type": "image/png"
      },
      {
        "src": "img/icons/icon-192x192.png",
        "sizes": "192x192",
        "type": "image/png"
      },
      {
        "src": "img/icons/icon-384x384.png",
        "sizes": "384x384",
        "type": "image/png"
      },
      {
        "src": "img/icons/icon-512x512.png",
        "sizes": "512x512",
        "type": "image/png"
      }
    ],
    "start_url": "/index.html",
    "display": "standalone",
    "background_color": "#000",
    "theme_color": "#ffff00"
  }
```

Enter fullscreen mode Exit fullscreen mode

> Your PWA Icons sizes should be in `px` and in the following sizes: `72x72` , `96x96` , `128x128` , `144x144` , `152x152` , `192x192` , `384x384` , `512x512`  
> You can use the [Web Manifest Generator](https://app-manifest.firebaseapp.com/) to generate your `manifest.json`

[![Manifest in Dev tools](https://media2.dev.to/cdn-cgi/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fi%2Fe7k86ydeg2vhk5uqzko7.png)](https://media2.dev.to/cdn-cgi/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fi%2Fe7k86ydeg2vhk5uqzko7.png)

Now we need to connect our web app to the manifest to allow “add to home screen” from that page. Add this to your `index.html`  

```
<link rel="manifest" href="/manifest.json" />
<meta name="theme-color" content="#333" />
```

Enter fullscreen mode Exit fullscreen mode

> If you have multiple pages, you need to add this to all of them.  
> You can also use the same `theme-color` you used in `manifest.json` here

Now your final `index.html` should look like this  

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>The Igala Facts you never knew</title>
    <link rel="stylesheet" href="css/style.css">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/font-awesome/4.5.0/css/font-awesome.min.css">
    <link href='https://fonts.googleapis.com/css?family=Roboto+Slab:400,700' rel='stylesheet' type='text/css'>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/animate.css/3.2.3/animate.min.css">
    <link rel="manifest" href="manifest.json" />
  <meta name="theme-color" content="yellow" />
</head>
<body>
    <div class="container">
        <div class="row">
          <div class="col-sm-6">
            <h1><span class="main-color">Random Igala</span><br />Facts</h1>
            <p>The best facts about Igala in one place. You can easily see the best facts and  share the ones you love on twitter with one click.</p>
          </div>
          <div class="col-sm-6">
            <div class="row">
              <div class="col-xs-6">
                <a id="next-quote" class="btn btn-lg btn-default btn-block" href="#"><i class="fa fa-refresh"></i> Next Fact</a>
              </div>
              <div class="col-xs-6">
                <a id="share" class="btn btn-lg btn-default btn-block" href="#" target="_top"><i class="fa fa-twitter"></i> Share</a>
              </div>
            </div>

            <div id="quote-box">
              <i id="quote-left" class="fa fa-quote-left"></i>
              <p id="quote"></p>
              <span id="author" class="main-color"></span>
              <i id="quote-right" class="fa fa-quote-right"></i>
            </div>

            <div class="row">       
              <div class="col-xs-12">
                <ul>
                  <li>Follow Us</li>
                  <li><a class="main-color" href="https://facebook.com/theigaladigital" target="_blank">@theigaladigital</a></li>
                    </ul>
                  </div>
              </div>
            </div>
          </div>
        </div>
      </div>

      <div id="hidden"></div>
      <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/2.1.3/jquery.min.js"></script>
      <script src="js/app.js"></script>
</body>
</html>
```

Enter fullscreen mode Exit fullscreen mode

Congratulations, you’ve successfully turned your website to a Progressive Web App.

### [](#conclusion)Conclusion

Throughout this article, we have seen how simple and fast it is to build a PWA by adding a manifest file and a service worker, it increases a lot the user experience of our traditional web app. Because PWAs are fast, secure, reliable and the most important, they support offline mode.

Many frameworks out there comes now with a service worker file already set-up for us, however, knowing how to implement it with Vanilla JavaScript can help you understand PWAs.

**P.S: If you ran into issues or problem, it’s probably a problem with HTTPS. PWA doesn’t work on HTTP, so make sure you’re running this with either http-server or live-server if you’re working from your local machine**

Thank you for reading!

Follow me on [Twitter](https://twitter.com/dfiredeveloper) or [Facebook](https://facebook.com/achimugu.i) I’m everywhere [@dfiredeveloper](https://dev.to/dfiredeveloper)
