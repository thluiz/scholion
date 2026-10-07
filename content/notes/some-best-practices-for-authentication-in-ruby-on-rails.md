---
title: "Some best practices for authentication in Ruby on Rails"
date: '2015-01-28T09:35:52-03:00'
category: webclip
summary: 'The article distinguishes authentication from authorization, recommends clearer names for authentication accessors, argues for separate authentication sessions, and warns that auth gems can add security and maintenance risks.'
tags: ["ruby-on-rails", "authentication", "authorization", "security"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Some best practices for authentication in Ruby on Rails"
    url: "http://www.fngtps.com/2015/some-best-practices-for-authentication-in-ruby-on-rails/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2015-01/fngtps-com--some-best-practices-for-authentication-in-ruby-on-rails.md"
    kind: repo
---

The article separates authentication from authorization and argues that application names and method names should say exactly what they mean. It prefers clearer accessors such as `current_user`, `current_account`, or `authenticated`, depending on the model and on whether the app needs to represent a user, a client, or an administrator.

## Reading notes

- Authentication verifies identity; authorization enforces permissions.
- Avoid shortened names like `auth`, `authn`, and `authz` unless the language has name-length limits.
- `user` and `@user` can be misleading because they suggest only people can sign in and can blur the distinction between the record being operated on and the authenticated entity.
- Instance variables for the authenticated entity can force callback-based setup and should not be assumed to be a side effect of memoized methods.
- Methods make it easier to abstract how authentication is fetched, support lazy loading, and let controllers override the source, such as cookie-based authentication or HTTP Basic Authentication.
- `current_user` works well when the authenticated model is actually `User`; otherwise a name like `current_account` may fit better.
- In impersonation or OAuth-style cases, `current_user` may need to return the represented user rather than the connected client or administrator.
- `authenticated` can return the authentication session target and can cover entities beyond users, such as `Consumer`, `Client`, or `Administrator`.
- Values derived from `current_user` should use the same naming scheme for consistency, such as `current_organization`.
- Authentication sessions should be modeled as separate records.
- Separate sessions let the same person authenticate multiple times on multiple systems and for different purposes while keeping control over each session.
- A password reset flow can create a new authentication session with a specific purpose and validation length and send its token by email.
- Separate sessions make it possible to sign out other devices by deleting all authentication sessions.
- The same session model can support API token authentication, IP and device annotations, and named long-lived sessions.
- This approach aligns well with OAuth and can simplify a future OAuth implementation.
- The author is skeptical of authentication gems close to business logic and the database because they can be too generic or too restrictive.
- Problems with gems can lead to workarounds, discarded libraries, extra documentation overhead, repeated upgrade checks, and security issues.
- The article recommends using gems only with full-stack regression tests and regular security audits.
- It closes by noting that credential storage, credential intake, and two-factor authentication are separate topics worth looking up elsewhere.
