---
url: "https://dev.to/maleta/cors-xss-and-csrf-with-examples-in-10-minutes-35k3"
captured_at: "2026-11-16T19:18:08+00:00"
title: "CORS, XSS and CSRF with examples in 10 minutes"
domain: "dev-to"
---

This article should be your entry point for existing web security standards, most common web attacks and the methods to prevent them. At the end, you will also find out how and why Samy was everyone's hero.(except Rupert Murdoch's, I guess)

## [](#cors)CORS

Cross-origin resource sharing, or CORS, is security feature of [IE10+, Chrome 4+, Firefox 3.5+ or almost every version of browser released after 2012 except Opera Mini.](https://caniuse.com/#search=CORS)

When CORS are _configured_ on server that is available on domain `website.com` then resources from that domain those are requested trough AJAX must be initiated from assets that is served from that same domain.  
[![CORS](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fmdn.mozillademos.org%2Ffiles%2F14295%2FCORS_principle.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fmdn.mozillademos.org%2Ffiles%2F14295%2FCORS_principle.png)

In the other words, if we enable CORS on `domain-b.com` and configure it to allow only `GET` requests from domain `domain-b.com` then if you want to use image available under `https://domain-b.com/images/example.png` in canvas on your website which is hosted on `domain-a.com`, than that image will not be loaded for most of your visitors.  
Your resources protected by CORS will still be available when requested by any tool or browser that doesn't respect `CORS policy`.

### [](#cors-configuration)CORS configuration

CORS are **disabled by default** which means that there is no adequate server handler that will configure CORS which means that you cannot access resources from different origin in your XHR. Basically, if you _don't do anything_ or specifically enable CORS only for specific domains, then any AJAX request trying to access your resources will be rejected because web browsers are respectful to the `CORS policy`.  
This is the reason why you encounter _CORS issue_ when you start developing SPA using VueJS and NodeJS. Your VueJS application is hosted on `http://localhost:8080` and when you try to access NodeJS server application on `http://localhost:8000` you get "`No Access-Control-Allow-Origin header is present`" because those are two different `ORIGINS`(combination of `PROTOCOL`, `HOST` and `PORT`).

Cool fix for CORS issue in VueJS development mode is to set devServer proxy in your `vue.config.js` file as follows:

```


module.exports = {
  ...
  devServer: {
    proxy: 'http://localhost:8000',
  },
  ...
}


```

Enter fullscreen mode Exit fullscreen mode

To setup CORS in production you should add appropriate listener for `OPTIONS` request. That listener should send response `200` with `no body` but with `Headers` that will define your wanted _CORS policy_:

```


Access-Control-Allow-Origin: https://domain-b.com
Access-Control-Allow-Methods: GET


```

Enter fullscreen mode Exit fullscreen mode

For more info on how to configure CORS check [https://enable-cors.org/index.html](https://enable-cors.org/index.html), and to dive deeper in `CORS policy`check [https://livebook.manning.com/book/cors-in-action/part-1/](https://livebook.manning.com/book/cors-in-action/part-1/)

* * *

## [](#xss)XSS

XSS stands for Cross Site Scripting and it is injection type of attack. It is listed as 7th out of top 10 vulnerabilities identified by OWASP in 2017. Cross site scripting is the method where the attacker injects malicious script into trusted website.(section updated, thanks Sandor) There are 3 types of such attacks.

1.  Stored XSS - Vulnerability coming from **unprotected and not sanitized** user inputs those are directly stored in database and displayed to other users
2.  Reflected XSS - Vulnerability coming from **unprotected and not sanitized** values from URLs those are directly used in web pages
3.  DOM based XSS - Similar as reflected XSS, **unprotected and not sanitized** values from URLs used directly in web pages, with difference that DOM based XSS doesn't even go to server side

### [](#attack)Attack

1\. Stored XSS

Here is an example of attack. The attacker comes on your website and finds unprotected input field such as comment field or user name field and enters malicious script instead of expected value. After that, whenever that value should be displayed to other users it will execute malicious code. Malicious script can try to access your account on other websites, can be the involved in DDoS attack or similar. Visual representation(source geeksforgeeks.org):

[![XSS example](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fmedia.geeksforgeeks.org%2Fwp-content%2Fuploads%2F20190516152959%2FCross-Site-ScriptingXSS.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fmedia.geeksforgeeks.org%2Fwp-content%2Fuploads%2F20190516152959%2FCross-Site-ScriptingXSS.png)

2\. Reflected XSS

Reflected XSS is attack that happens when attacker discovers page with such vulnerability, for example:

expected URL: `https://mywebpage.com/search?q=javascript`  
malicious URL: `https://mywebpage.com/search?q=<script>alert('fortunately, this will not work!')</script>`

```


<body>
...
<div> showing results for keyword 
<script> document.write(window.location.href.substr(window.location.href.indexOf('q=') + 2))
</script>
</div>
...
...JavaScript results...
...
</body>


```

Enter fullscreen mode Exit fullscreen mode

After discovery, attacker baits user to click on such malicious URL and voila. User sensitive data is exploited.

Lifecycle of attack ilustrated in example provided by geekforgeeks.com:

[![Reflected XSS example](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fmedia.geeksforgeeks.org%2Fwp-content%2Fuploads%2F20190516153002%2FreflectedXSS.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fmedia.geeksforgeeks.org%2Fwp-content%2Fuploads%2F20190516153002%2FreflectedXSS.png)

3\. DOM based XSS

This kind of attack is same as reflected but with difference that malicious `URL` part will not be sent to server at all. For above example:

expected URL: `https://mywebpage.com/search?q=javascript`  
malicious URL(reflected XSS): `https://mywebpage.com/search?q=<script>alert('fortunately, this will not work!')</script>`  
malicious URL(DOM based XSS): `https://mywebpage.com/search#q=<script>alert('fortunately, this will not work!')</script>`

Difference is in the character `#` being used instead of `?`. The browsers **do not send part of URL after # to server** so they pass it directly to your client code.

### [](#protection)Protection

**Every value** that can be entered by user and is used in your app(either on server side either on client side) should be treated as **untrusted data** and therefore should be **processed before using**! You should do safety check in your server app and your client app, as well!  
As [showed in documentation](https://vuejs.org/v2/guide/security.html) VueJS by itself escapes string before getting value from variable. Newer versions of Angular also escape strings implicitly, so if you are using Vanilla JS, JQuery or similar you should implement string escape manually.

There are three most common approaches on **processing untrusted data** are listed below and ideal method depends on the actual type of the field that you need to process.

#### [](#1-string-validation)1\. String validation

Validation is the method where user defines set of rules, and demand _untrusted data_ to satisfy those rules before moving on. This method is good for _number values_, _username_, _email_, _password_ and similar fields with concrete set of syntax rules.

Check for existing libraries for your framework before considering to write validators by your own.

#### [](#2-string-escape)2\. String escape

Escape method is useful for cases where you should enable user to use punctuation marks. This method goes through string and looks for special characters, such as `<` `>` and replace them with appropriate HTML character entity name. Here is basic function that you could use:

```


function escapeText(text) {
  return text.replace(/&/g, '&amp;')
             .replace(/</g, '&lt;')
             .replace(/>/g, '&gt;')
             .replace(/"/g, '&quot;')
}



```

Enter fullscreen mode Exit fullscreen mode

Again, check for existing libraries before writing your own.

#### [](#3-string-sanitization)3\. String sanitization

Sanitizing string is used when user is allowed to enter some HTML tags in their comments, articles or similar. The sanitize method goes through text and looks for HTML tags that you specify and removes them. One of most popular libraries that uses this approach is [Google Closure](https://github.com/google/closure-library/blob/master/closure/goog/html/sanitizer/htmlsanitizer.js).  
This method is resource expensive and considered as harmful, so do more research before choosing it.

Web browsers(no available sources since what version, IE fixed this issue in 2014.) automatically escape URLs before sending them to server side and making them available in `window.location` object also, so 2nd and 3rd type of attack are here just to be aware of them and to make clear that URL params should also be treated as untrusted data.

For more detailed info about XSS and how to properly protect your application if you rotate a lot of **untrusted data**, please check [OWASP cheatsheet on XSS prevention](https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html).

* * *

## [](#csrf)CSRF

Cross site request forgery or CSRF is a type of attack that occurs when a malicious web site, email, blog, instant message, or program causes a user's web browser **to perform an unwanted action on an other trusted site** where the user is authenticated. This vulnerability is possible when browser automatically sends authorization resource, such as session cookie, IP address or similar with each request.

### [](#attack)ATTACK

Let's suppose that user is logged in to your unprotected stock exchange web application and that you are using either session cookie either JWT cookie for authentication. Attacker also uses your service and is able to check how your API works. Attacker tricks user to execute script(by clicking on SPAM link in email or similar) that will send request to your API `https://www.stockexchange.com/users/withdraw?how_much=all&address=MY_ADDRESS`(terrible API design, don't ask). Since request is executed from browser that sends authentication payload with every request, your stockexchange web server will authenticate user successfully and execute transaction and tricked user will lose all his balance **without even being aware of it** because everything happened in the background. Visual representation(source miro.medium.com)  
[![CSRF attack](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fmiro.medium.com%2Fmax%2F736%2F1%2A_DGU1bpdqTMKtTNyBc_wRw.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fmiro.medium.com%2Fmax%2F736%2F1%2A_DGU1bpdqTMKtTNyBc_wRw.png)

### [](#protection)PROTECTION

Luckily there are easy to implement patterns that prevent this web attacks. One of the most common pattern is usage of `CSRF token`. Basically procedure is following:

1.  Generate unique token for each user's request, so called `CSRF token`.
2.  Store it safely on server and send it back to user as payload of response.
3.  Store `CSRF token` on client side.
4.  When user tries to execute any state-changing\* request send that `CSRF token` with request as a payload.
5.  Before executing that request on server side check if `CSRF token` is present and it is valid.

This is the easiest way to prevent CSRF attack for all users.

If you are are dealing only with visitors that uses [modern browsers](https://caniuse.com/#feat=same-site-cookie-attribute) then you can rely on `SameSite` attribute of session cookie.(thanks Gergely)

Since server's responses are processable in XHR response, then **there is no protection on CSRF attack if your web application is XSS vulnerable!**

To dive deeper check [OWASP cheatsheet on CSRF](https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html).

## [](#bonus)BONUS

Short documentary about Samy, author of worm that took down MySpace back in 2005 abusing XSS vulnerability, passing MySpace's CSRF defense.  
[https://youtu.be/DtnuaHl378M](https://youtu.be/DtnuaHl378M)

More info on Samy's worm  
[https://samy.pl/myspace/tech.html](https://samy.pl/myspace/tech.html)
