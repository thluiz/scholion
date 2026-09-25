---
url: "https://dev.to/wils3b/full-stack-security-essentials-preventing-csrf-clickjacking-and-ensuring-content-integrity-in-4paf?context=digest"
captured_at: "2026-09-25T01:22:21+01:00"
title: "Full Stack Security Essentials: Preventing CSRF, Clickjacking, and Ensuring Content Integrity in JavaScript"
domain: "dev-to"
---

In today’s web development landscape, security is more than a buzzword—it’s a necessity. As full stack developers, we face a wide range of threats, from backend vulnerabilities to client-side exploits. In this article, we’ll explore three critical areas of JavaScript security: CSRF, clickjacking, and content integrity. We’ll discuss what each threat entails and provide practical tips on preventing them from both Node.js and in the browser environment.

* * *

## [](#1-csrf-crosssite-request-forgery)1\. CSRF (Cross-Site Request Forgery)

### [](#what-is-csrf)What is CSRF?

CSRF is an attack where a malicious website tricks a users browser into performing unwanted actions on a trusted site where the user is authenticated. This can lead to unexpected changes, unauthorized transactions, or data exposure.

### [](#how-to-prevent-csrf)How to Prevent CSRF

#### [](#on-the-nodejs-serverside-end)On the Node.js (Server-Side) End

*   **CSRF Tokens:** Use middleware (e.g., tiny-csrf in Express.js) to generate unique tokens for each session or form submission. Verify these tokens on every state-changing request.

Example using Express.js with tiny-csrf:  

```
npm install --save tiny-csrf express-session cookie-parser
```

Enter fullscreen mode Exit fullscreen mode

```
  const express = require('express');
  const csurf = require('tiny-csrf');
  const cookieParser = require('cookie-parser');
  const session = require("express-session");

  const app = express();

  app.use(express.urlencoded({ extended: false })); 
  app.use(cookieParser("cookie-parser-secret"));
  app.use(session({ secret: "keyboard cat" }));
  // Order matters: above three must come first
  // Setup csurf protection
  const csrfProtection = csurf("123456789iamasecret987654321look");
  app.use(csrfProtection);

  app.get('/form', (req, res) => {
    // Get the csrf token from the methog injected by the middeware to the request object
    const csrfToken = req.csrfToken();
    // Token must be included in the rendered form
    res.send(`<form action="/process" method="POST">
                <input type="hidden" name="_csrf" value="${csrfToken}">
                <input type="text" name="data">
                <button type="submit">Submit</button>
              </form>`);
  });

  app.post('/process', (req, res) => {
    // Process the request only if CSRF token is valid
    res.send('Form data processed safely.');
  });

  app.listen(3000, () => console.log('Server running on http://localhost:3000'));

```

Enter fullscreen mode Exit fullscreen mode

This example uses the module `tiny-csrf`, which provides minimalist CSRF protection. For scenarios that require more robust security, consider the following alternatives:

*   **[csrf-csrf](https://www.npmjs.com/package/csrf-csrf):** This module offers the essential components to implement CSRF protection using the Double Submit Cookie Pattern—a stateless approach.
*   **[csrf-sync](https://www.npmjs.com/package/csrf-sync):** Designed for the Synchroniser Token Pattern, this alternative is particularly suited for session-based authentication and offers stateful CSRF protection.

Both options provide enhanced flexibility depending on your specific security requirements.

#### [](#in-the-browser-clientside)In the Browser (Client-Side)

*   **SameSite Cookies:** Set your cookies with the SameSite attribute to Lax or Strict to prevent them from being sent along with cross-domain requests.
    
*   **Custom Headers:** When making AJAX requests, include custom headers (like X-Requested-With) and validate them on the server to help identify legitimate requests.
    

* * *

## [](#2-clickjacking)2\. Clickjacking

### [](#what-is-clickjacking)What is Clickjacking?

Clickjacking involves tricking a user into clicking on a disguised UI element, often hidden or overlaid by another element, which can lead to unintended actions like authorizing an action, sharing data, or even performing administrative tasks.

### [](#how-to-prevent-clickjacking)How to Prevent Clickjacking

*   **X-Frame-Options Header:** Use the X-Frame-Options HTTP header to control whether your content can be embedded in frames. Options include:
    *   `DENY`: Prevent all framing.
    *   `SAMEORIGIN`: Allow framing only from the same origin.

Example in Express.js:  

```
  app.use((req, res, next) => {
    res.setHeader('X-Frame-Options', 'SAMEORIGIN');
    next();
  });
```

Enter fullscreen mode Exit fullscreen mode

*   **Content Security Policy (CSP):** Use the `frame-ancestors` directive in your CSP headers to control what domains can embed your pages. For example:

```
  app.use((req, res, next) => {
    res.setHeader("Content-Security-Policy", "frame-ancestors 'self'");
    next();
  });
```

Enter fullscreen mode Exit fullscreen mode

*   **Frame Busting Scripts:** While these can be implemented using JavaScript to “bust out” of frames, they are less reliable than server-side HTTP headers and should be used as a secondary measure.

* * *

## [](#3-content-integrity)3\. Content Integrity

### [](#what-is-content-integrity)What is Content Integrity?

Content integrity ensures that the content served by your site (e.g., scripts, stylesheets) remains unchanged from its original, trusted source. This is crucial in preventing tampering and man-in-the-middle attacks, especially when using third-party resources.

### [](#why-we-should-add-it)Why We Should Add It

*   **Trust:** Users can trust that the data and code are coming from verified sources.
*   **Security:** Protect against situations where third-party content may be compromised.
*   **Compliance:** Meet security and compliance standards that require integrity assurances.

### [](#how-to-implement-content-integrity)How to Implement Content Integrity

*   **Subresource Integrity (SRI):** SRI allows browsers to verify that files they fetch (like JavaScript libraries) are delivered without unexpected manipulation. It involves including a cryptographic hash attribute in the HTML tag linking the resource.

Example:  

```
  <script src="https://example.com/library.js"
          integrity="sha384-oqVuAfXRKap7fdgcCY5uykM6+R9Wu0g6a3JmGDXVbDt+u6p1mCA/t9zqXQGHbQ8c"
          crossorigin="anonymous"></script>
```

Enter fullscreen mode Exit fullscreen mode

*   **CSP Hashes:** When inline scripts are necessary, you can use CSP hashes to specify the expected hash of the script contents, ensuring that only approved code executes.

* * *

## [](#conclusion)Conclusion

Incorporating solid security practices into your JavaScript applications is not optional—it’s fundamental. By understanding the risks associated with CSRF, clickjacking, and the importance of content integrity, you can implement robust measures that safeguard both your application and its users.

Whether you’re tweaking your Node.js backend or reinforcing client-side defenses, these strategies help ensure that your applications remain secure in an increasingly hostile online environment. Security is a continuous journey—stay vigilant, keep your dependencies updated, and always be mindful of emerging threats.

* * *

## [](#further-readings)Further readings

To explore the concepts in this article further, you can read the following resources that provide more detailed information about CSRF, clickjacking, and content integrity.

*   [https://owasp.org/www-community/attacks/csrf](https://owasp.org/www-community/attacks/csrf)
*   [https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site\_Request\_Forgery\_Prevention\_Cheat\_Sheet.html](https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html)
*   [https://owasp.org/www-community/attacks/Clickjacking](https://owasp.org/www-community/attacks/Clickjacking)
*   [https://cheatsheetseries.owasp.org/cheatsheets/Clickjacking\_Defense\_Cheat\_Sheet.html](https://cheatsheetseries.owasp.org/cheatsheets/Clickjacking_Defense_Cheat_Sheet.html)
*   [https://developer.mozilla.org/en-US/docs/Web/Security/Subresource\_Integrity](https://developer.mozilla.org/en-US/docs/Web/Security/Subresource_Integrity)
