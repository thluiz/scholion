---
title: "How to securely store JWT tokens"
date: '2020-04-20T21:22:24+00:00'
category: webclip
summary: 'The article argues that JWTs should not be stored in local storage or session storage, recommends browser memory only with re-login on refresh, and favors cookies with HttpOnly, Secure, and SameSite settings to reduce XSS and CSRF risk.'
tags: ["jwt", "cookies", "xss", "csrf"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "How to securely store JWT tokens."
    url: "https://web.archive.org/web/20200412170205id_/https://dev.to/gkoniaris/how-to-securely-store-jwt-tokens-51cf"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/web-archive-org--how-to-securely-store-jwt-tokens.md"
    kind: repo
---

The article explains that JWTs are cryptographically signed JSON objects used for authentication and authorization. It then compares common storage options and says local storage and session storage are unsafe because JavaScript on the same domain can access them. Browser memory is presented as secure if the token is kept only in code, but it forces the user to log in again after a refresh.

Cookies are presented as the preferred option when they are configured with HttpOnly and Secure. The article also explains CSRF and says SameSite can help, with Lax allowing cross-domain GET requests and Strict blocking cross-domain requests entirely. It adds that older browsers may ignore SameSite, so CSRF tokens or a browser support warning may still be needed.

## Reading notes

- JWT is described as a cryptographically signed base64 representation of a JSON object, made of a header, a payload, and a signature.
- Local storage is rejected because any JavaScript running on the same domain can read it, which exposes the token to XSS.
- Session storage is also rejected for the same reason, even though it disappears when the browser closes.
- Storing the token only in browser memory is described as secure, but it requires the user to log in again after a refresh.
- Cookies are recommended when the server sets HttpOnly so JavaScript cannot access them.
- Cookies should also use Secure so they are not sent over non-secure HTTP.
- The article warns that cookies can enable CSRF because browsers send them on cross-domain requests.
- A CSRF example is given in which a malicious link submits a password-change request on behalf of a logged-in user.
- One mitigation is a backend-generated token checked on sensitive requests such as POST, PUT, and DELETE.
- SameSite is described as a browser cookie policy with None, Lax, and Strict values.
- Lax allows cross-domain GET requests but blocks cookies on other cross-domain request types.
- Strict blocks cookies on all cross-domain requests, including simple link redirects.
- If a browser does not support SameSite, the article says to warn the user or fall back to CSRF tokens.
