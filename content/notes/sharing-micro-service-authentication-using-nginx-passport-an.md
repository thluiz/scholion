---
title: "Sharing micro-service authentication using Nginx, Passport and Redis"
date: '2015-04-10T22:15:26-03:00'
category: webclip
summary: 'The post explains how Nginx, Passport and Redis can make authentication shared across micro-services by keeping the browser on one domain, sharing the session cookie, and moving session data into Redis.'
tags: ["micro-services", "authentication", "nginx", "redis"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Sharing micro-service authentication using Nginx, Passport and Redis"
    url: "http://dejanglozic.com/2014/10/07/sharing-micro-service-authentication-using-nginx-passport-and-redis/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2015-04/dejanglozic-com--sharing-micro-service-authentication-using-nginx-passport-an.md"
    kind: repo
---

The post argues that micro-services should stay secure without making users feel the system is fragmented. It proposes a proxy in front of the services, Passport in each Node.js app, and Redis as an external session store so authentication and session data can be shared across services and instances.

## Reading notes

- A proxy such as Nginx gives friendly URLs, load balancing, and a single domain for cookies and Ajax calls.
- Passport can be added as middleware in each micro-service, with shared client ID, secret, and authentication strategy.
- Each service can use a different callback URL as long as the callback roots share the same domain through the proxy.
- The default Express session store keeps data in memory, so shared session cookies alone do not create single sign-on across services or instances.
- Redis can serve as an external session store, letting all proxied services read the same session data after authentication.
- Redis pub/sub can also propagate logout events so the system does not stay partially logged in.
- Some services can skip full Passport support and only check for an Authorization header with a bearer token.
- The approach is easier when services are written in Node.js, while Java or Go raise questions about cookie signing and session support across stacks.
