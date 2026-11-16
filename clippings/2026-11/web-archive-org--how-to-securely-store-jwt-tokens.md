---
url: "https://web.archive.org/web/20200412170205id_/https://dev.to/gkoniaris/how-to-securely-store-jwt-tokens-51cf"
captured_at: "2026-11-16T07:49:17+00:00"
title: "How to securely store JWT tokens."
domain: "web-archive-org"
---

Article originally published [here](https://gkoniaris.gr/security/how-to-securely-store-jwt-tokens).

In the last years, JWT tokens are widely used as an authentication and authorization method for web applications. They allow backend developers to authenticate users, without making a single query to the database server or any other type of storage. They are super easy to use and they also use the most common format currently used for data on the Internet, JSON.

Because of these facts, there is an increasing number of cases where users store JWT tokens in the wrong way, making web applications vulnerable to different kinds of attacks.

## [](#but-first-what-is-a-jwt-token)But first, what is a JWT token?

JWT is an abbreviation for JSON Web Token. JWTs are nothing more than a cryptographically signed, base64 representation of a JSON object. By signing the token, we make sure that its content was not altered in any way. This is achieved by verifying the received token with the exact same key that was used to sign it in the first place. In case the signature that we generate does not match the one in the token, we should consider that the token is invalid.

JWT tokens have three parts, all represented as base64 strings:

*   A header that usually contains the token’s expiration date, the algorithm used for signing, and extra metadata.
    
*   A JSON payload.
    
*   A signature created by signing the header and the payload
    

The header and payload are stored in JSON format before signed. The final token is a concatenation of the base64 data of the above, delimited by a period. So, a JWT token would look like the following:

\[header\].\[payload\].\[signature\]

Now, let’s explore which is the best way to store a JWT token.

## [](#should-i-store-my-jwt-in-local-storage)Should I store my JWT in local storage?

Most people tend to store their JWTs in the local storage of the web browser. This tactic leaves your applications open to an attack called XSS. We will only discuss XSS in the JWT context, you can find more about it [here](https://owasp.org/www-community/attacks/xss/). In this kind of attack, an attacker takes advantage of the fact that local storage is accessible by any javascript code running on the same domain that the web applications hosted. So, for example, if the attacker can find a way to inject maliciously javascript code inside your application (by injecting the code in a node module that you use without knowing about it), your JWT token is immediately available to their.

So the answer to this question is: **No, never store a JWT in local storage.**

## [](#but-what-about-session-storage)But what about session storage?

Hmm, let’s see what happens in this case. Like local storage, session storage is accessible by any javascript code running on the same domain that the web application is hosted. So the only thing that changes, is that when a user closes their browser, the JWT will disappear and the user will have to login again in their next visit to your web application.

So again, the answer is the same: **Never store a JWT in session storage.**

## [](#ok-but-i-can-always-use-the-browsers-memory-right)Ok, but I can always use the browser’s memory, right?

Sure, if you make your token available only by your code, that’s a secure solution. The only caveat is that when the user refreshes the browser, they have to log in again. Not so cool right?

I recommend using this approach when the user, for some unknown reason, MUST log in again when refreshing the browser,

## [](#but-if-i-cannot-use-any-of-these-then-what-cookies-cookies-are-so-2010-)But if I cannot use any of these then what? Cookies? Cookies are so 2010 …

Stop dissing cookies, cookies are great. We have been using them for years, they are automatically sent in every browser request (including ajax if we want them to) and they are **SUPER SECURE!!!**

> Distant voice: But cookies are also accessible through javascript.

That’s true, but only if the server doesn’t set the HttpOnly flag, something you should always set for authentication or authorization cookies. So distant voice, are we ok with that?

> Distant voice: Of course not, what if someone sents them through a non-secure HTTP request?

First of all, nobody should use plain HTTP these days, but even this way, we can set the Secure flag when creating the cookie, so it will be never sent through a non-secure connection. I think we can move on…

> Distant voice: Are you in a hurry bro? You forgot CSRF.

F@!k. It’s true, I forgot CSRF attacks. So, **what is a CSRF attack**?

A CSRF attack is performed when an attacker takes advantage of the browser’s default behavior, to send all cookies even on cross-domain requests. This can lead to great security vulnerabilities if not handled correctly. An example of this attack is the following:

*   The attacker sends an email with a beautiful offer, and adds a CTA button at the end, “GET A 50% DISCOUNT”.
    
*   The user is thrilled by this awesome offer and clicks the button.
    
*   In reality, the button submits a POST form to your web application, and more specifically to the endpoint that changes the user’s password with a new one.
    
*   Because cookies are sent in every request, even cross-domain ones, the endpoint works as expected if the user has logged in, in an earlier step to your web application.
    
*   Now the user is logged out and cannot log in to your web application anymore.
    

We have to mention that this attack would be performed by an attacker that just wants to play a little bit and test its skills. More serious operations could have been performed like making the user upgrade to a very expensive plan, or even transferring money from their bank account to the attacker’s account.

## [](#so-what-can-i-do-about-it)So what can I do about it?

The first option is to just forget about it, never tell anyone, and hope that nobody ever finds out (especially a malicious hacker). You are ready to go!!! Just kidding…

You can use a backend generated token in every request that you perform to the server (usually any POST, PUT, DELETE request), so when the user performs the request, you check if the token is valid by fetching it from some cache or even directly from the database. But this requires that you create a new token every time the user redirects to a new page? So is there an alternative?

For many years, unfortunately, the only way to be safe was to use a CSRF token when using cookie-based authentication. From 2016, modern browsers started implementing a cookie policy called SameSite. SameSite can take one of the following three values:

Each of them is useful in its own case.

The first one, None, allow the cookie to be sent in every possible request, including cross-domain. This is how browsers were treating cookies for many years. The new default value for SameSite of most modern browsers is Lax, although not all browsers are using Lax as the default SameSite cookie policy yet.

You can find browser compatibility [here](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Set-Cookie#Browser_compatibility).

So what is Lax? Lax allows cookies to be sent in cross-domain requests if the request verb is GET. All other requests will not contain cookies with the Lax SameSite policy. This way, it allows cookies to be used when, for example, redirecting the user from an email to a dashboard screen of your app, but don’t allow a malicious form post data to a sensitive endpoint.

We have to mention that Lax works for all redirect GET requests. It won’t sent cookies in ajax request, so nobody can just add some code in their site and request, for example, the **_/me_** endpoint, stealing the logged-in user personal data. It will be also ignored in the case of iframes, even for redirect requests.

So the most usual ways a Lax cookie is sent from a cross-domain GET request are the following.

*   A user clicks a link that redirects to your website
    
*   A user submits a GET form request that redirects to your website (useful in case you want to provide a way to pass dynamic arguments to the query string using a form, from another site)
    
*   If a command like **_window.location.href=”yoursite…”_** is used.
    

Now, Strict SameSite policy will not allow the cookie to be passed through cross-domain requests in any way. This can be useful in some edge cases, but you have to understand that even a simple link redirect will leave your user logged out from your web application if you use this policy. Of course, it’s the safest one.

## [](#so-i-just-use-lax-or-strict-and-i-can-now-sleep-without-the-fear-of-a-csrf-or-xss-attack-right)So, I just use Lax or Strict, and I can now sleep without the fear of a CSRF or XSS attack. Right?

Almost. You have to make sure that your users are using a modern browser that supports this kind of functionality. In case they don’t, the best thing to do is to inform the user that your application is not currently supported by the specific browser version and that they should upgrade to a newer version.

In case you don’t use a message like this, there is the possibility that the server will try to set the SameSite policy, but the browser is going to ignore it. For example, Internet Explorer does not support this kind of functionality. If you need explicit support for an older browser, you should fallback to the CSRF token implementation.

Background vector created by vectorpocket – [www.freepik.com](https://www.freepik.com/)
