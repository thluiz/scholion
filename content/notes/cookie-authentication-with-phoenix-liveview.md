---
title: "Cookie Authentication with Phoenix LiveView"
date: '2020-07-05T14:10:30+00:00'
category: webclip
summary: 'The post explains how Phoenix session cookies identify a user, why LiveView login forms cannot call `Plug.Conn.put_session` from event handlers, and how ETS plus a signed token can bridge that gap.'
tags: ["phoenix-liveview", "cookie-authentication", "ets", "phoenix-token"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Cookie Authentication with Phoenix LiveView"
    url: "https://toranbillups.com/blog/archive/2020/06/26/cookie-authentication-with-phoenix-liveview"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/toranbillups-com--cookie-authentication-with-phoenix-liveview.md"
    kind: repo
---

The post shows how Phoenix uses a signed cookie session to identify a user, starting from the default `Plug.Session` setup and a sample `Set-Cookie` header. It then traces how a server-rendered login flow stores a user id in the session and how plugs read that value to assign `current_user_id` and redirect unauthorized requests.

## Reading notes

- Phoenix stores the session in a signed cookie by default, so the cookie contents can be read but not changed.
- A sample response from Phoenix includes a `Set-Cookie` header that carries the session cookie.
- Decoding the cookie shows that the initial request contains only a CSRF token.
- In a traditional server-rendered login flow, a successful password check calls `put_session(:user_id, id)` and redirects the user.
- A plug can read `get_session(conn, :user_id)` and assign `current_user_id` onto `conn`.
- Another plug can redirect restricted requests when `current_user_id` is missing.
- LiveView event handlers cannot use `Plug.Conn.put_session`, which creates the login problem.
- The workaround stores a user id in ETS after successful login and uses a plug to copy it into `conn.assigns`.
- The first version of that workaround is described as not sound for production because one inserted user id would make every request appear authenticated.
- The improved version introduces a `session_uuid` stored in the cookie on the first request.
- The LiveView login mount receives `session_uuid` from the session and assigns it for later use.
- On login success, the LiveView handler signs the user id with `Phoenix.Token` and stores the token in ETS under the `session_uuid` key.
- A plug later looks up the token with `session_uuid`, verifies it, and assigns `user_id` onto `conn`.
- The same redirect plug still blocks restricted routes when `user_id` is missing.
- Because `mount` does not have access to `conn.assigns`, the restricted LiveView reads `session_uuid` from the session and resolves the user id through ETS and token verification.
- A bonus variant also writes `user_id` into the session so restricted LiveView mounts can receive it directly.
- The post ends by pointing to the GitHub commits containing the full source code.
