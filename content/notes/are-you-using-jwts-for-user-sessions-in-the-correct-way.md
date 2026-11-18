---
title: "Are you using JWTs for user sessions in the correct way?"
date: '2020-04-10T01:07:34+00:00'
category: webclip
summary: 'The article weighs JWTs against opaque session tokens for backend-frontend user sessions, then argues for short-lived JWTs paired with long-lived opaque refresh tokens to keep scalability while reducing revocation and security issues.'
tags: ["jwt", "user-sessions", "refresh-tokens", "session-management"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Are you using JWTs for user sessions in the correct way?"
    url: "https://dev.to/supertokens/are-you-using-jwts-for-user-sessions-in-the-correct-way-1e1"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/dev-to--are-you-using-jwts-for-user-sessions-in-the-correct-way.md"
    kind: repo
---

The article distinguishes JWTs for OAuth from JWTs used for user sessions, then compares their pros and cons in backend-frontend session management. It argues that JWTs mainly reduce latency by avoiding database lookups, but they also make revocation, key compromise, and device monitoring harder.

It then proposes a mixed flow: short-lived JWT access tokens plus long-lived opaque refresh tokens. In that setup, normal API requests keep the latency benefit, while refresh-time database checks restore more control over revocation and session tracking.

## Reading notes

- JWTs were originally designed for OAuth, which is different from user sessions.
- The article limits itself to session management between an app’s backend APIs and frontend, with no third-party service involved.
- Opaque tokens are long random strings that reference stored session data.
- JWTs are signed non-opaque tokens that let the backend verify the token without a database lookup.
- The main advantage of JWTs is lower latency from avoiding database lookups in session verification.
- Saving database space is presented as a myth, because the storage cost is small in practice.
- Signing does not make JWTs more secure than opaque tokens in this context.
- JWTs are not inherently easier to use, because the surrounding session system is still needed.
- JWTs are not more flexible, since similar data can be stored against an opaque token in the database.
- JWTs do not automatically prevent CSRF when cookies are used.
- Cookie consent for GDPR is not different for JWTs and opaque tokens when they are used to keep users logged in.
- JWTs are said not to work better than opaque tokens for mobile or when cookies are blocked.
- The main drawback is that JWTs are hard to revoke before expiration.
- Another drawback is dependence on one signing key, which can be compromised.
- Crypto deprecation and algorithm changes remain a concern.
- Without session data in the database, JWTs make device monitoring harder.
- Cookie size and transfer overhead are presented as myths rather than decisive problems.
- The proposed approach uses a short-lived JWT access token and a long-lived opaque refresh token.
- The access token is sent on each API call, and the refresh token is used to get a new JWT and a new opaque token when the JWT expires.
- Rotating refresh tokens help detect stolen tokens and session hijacking.
- Revocation becomes easier because removing the opaque token from the database can end the session at refresh time.
- Changing the JWT signing key invalidates current JWTs, while refresh tokens can obtain new ones.
- The article recommends this mixed approach when scalability matters more than immediate revocation and the cookie size limit is not a problem.
- For OAuth, the article still treats JWTs as a good fit.
