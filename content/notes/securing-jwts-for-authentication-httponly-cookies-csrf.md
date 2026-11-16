---
title: "Today's rabbit hole: securing JWTs for authentication, httpOnly cookies, CSRF tokens, secrets & more"
date: '2026-11-16T01:59:15+00:00'
category: webclip
summary: 'The post walks through storing JWTs in httpOnly cookies, protecting routes with a separate login flag, handling logout server-side, and adding CSRF protection with csurf, CORS, SameSite, and headers.'
tags: ["jwt-authentication", "httponly-cookies", "csrf-protection", "react-auth"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Today's rabbit hole: securing JWTs for authentication, httpOnly cookies, CSRF tokens, secrets & more"
    url: "https://dev.to/petrussola/today-s-rabbit-hole-jwts-in-httponly-cookies-csrf-tokens-secrets-more-1jbp"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/dev-to--securing-jwts-for-authentication-httponly-cookies-csrf.md"
    kind: repo
---

The post follows a debugging journey through JWT storage and protection in a React and Express setup. It argues for storing the token in an httpOnly cookie rather than localStorage, using a separate client-visible cookie to detect login state, and handling logout by overwriting the server cookie and clearing the visible flag.

## Reading notes

- localStorage is described as unsafe because third-party scripts can access stored tokens.
- an httpOnly cookie is presented as the safer place to store the JWT because browser JavaScript cannot read or write it.
- the login endpoint generates the JWT and saves it with `res.cookie('token', token, { httpOnly: true })`.
- `document.cookie` can read the cookie when `httpOnly` is false, but not when it is true.
- browser memory is mentioned as a safe option, but the token is lost on refresh and login must happen again.
- a second cookie, with `httpOnly: false`, is used only to show whether the user is logged in.
- route protection is done with a `PrivateRoute` that checks `isLoggedIn === 'true'` and redirects to `/login` otherwise.
- the author uses `js-cookie` to read cookies in React.
- logout removes the token by sending a server cookie with the same name and a dummy value, and sets `isLoggedIn` to false.
- the post frames CSRF as a risk for authenticated requests because browser cookies are sent automatically.
- it mentions CORS policy, CSRF tokens, and SameSite cookies as defenses.
- `csurf` is used to generate a CSRF token and a secret, with the token sent to the client and the secret stored in a cookie.
- the client stores the token in an `X-CSRF-Token` header for later AJAX requests.
- the author uses Axios `withCredentials: true` in development and relies on credentials handling and domain settings in production.
- `csurf` is described as validating the token against the secret and throwing an error if verification fails.
- both Ryan Chenkie and Harleen Mann are cited as saying that in-memory JWT storage with refresh tokens is the safest approach.
