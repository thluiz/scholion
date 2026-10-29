---
title: "Why use www? – www. is not deprecated"
date: '2016-02-07T22:22:27-03:00'
category: webclip
summary: 'The page argues that using www keeps room for growth, works better with CDN and cloud hosting, and avoids cookie and subdomain problems that can affect larger sites.'
tags: ["www", "canonical-urls", "dns", "cookies"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Why use www? – www. is not deprecated"
    url: "http://www.yes-www.org/why-use-www/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2016-02/yes-www-org--why-use-www-www-is-not-deprecated.md"
    kind: repo
---

The page says webmasters should use www because a site may grow from small to very large, and the technical benefits mainly matter at that scale. It points to cloud hosting, DNS flexibility, and subdomain setups as reasons to prefer www over a naked domain.

## Reading notes

- www is recommended for sites that may grow into large, highly distributed services.
- Cloud providers such as Heroku want DNS records that can be updated for failover, and naked domains cannot use CNAME records.
- Using www avoids sending cookies to static subdomains by default, which helps performance and caching.
- If a site uses a naked domain and shares cookies across subdomains, it may need a separate domain for static content.
- Shared-cookie setups between a naked domain and subdomains can be awkward unless RFC 6265 cookies are implemented properly.
- Redirecting no-www to www helps visitors reach the site in either form and helps search engines index the canonical URL.
