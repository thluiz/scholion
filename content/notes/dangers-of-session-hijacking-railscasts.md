---
title: "#356 Dangers of Session Hijacking - RailsCasts"
date: '2014-03-29T07:44:14-03:00'
category: webclip
summary: 'Shows how a session cookie exposed over HTTP can be stolen and replayed, then explains Rails protections with force_ssl and a separate secure signed cookie for HTTPS requests.'
tags: ["security", "session-hijacking", "https", "rails"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "#356 Dangers of Session Hijacking - RailsCasts"
    url: "http://railscasts.com/episodes/356-dangers-of-session-hijacking?view=asciicast"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2014-03/railscasts-com--dangers-of-session-hijacking-railscasts.md"
    kind: repo
---

The episode explains that sending authentication cookies over an insecure connection makes a Rails session vulnerable to hijacking, also called sidejacking. It shows how traffic on localhost can reveal the session cookie, then how that cookie can be reused with curl to act as the logged-in user.

It then describes two protections in Rails. One is `config.force_ssl = true`, which redirects all requests to HTTPS. The other is a split-cookie approach for apps that only use SSL on some pages: store `session[:user_id]` as usual, add a signed `secure_user_id` cookie marked secure, and check it in `current_user` so HTTPS pages reject a hijacked session.

## Reading notes

- Authentication cookies sent over HTTP can be captured and reused to hijack a session.
- Session hijacking here is described as sidejacking, the kind popularized by Firesheep.
- `tcpdump -i lo0 -A` can expose the session cookie in request traffic.
- A stolen session cookie lets `curl` impersonate the logged-in user without knowing the password.
- `config.force_ssl = true` makes every request use HTTPS.
- If SSL is only enabled on part of the site, the app can keep a second signed cookie named `secure_user_id`.
- The secure cookie is set on login, deleted on logout, and checked in `ApplicationController#current_user`.
- With this setup, hijacked cookies still work on insecure pages but fail on pages that require HTTPS.
