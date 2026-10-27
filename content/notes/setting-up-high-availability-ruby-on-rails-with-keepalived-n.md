---
title: "Setting up a High Availability Ruby on Rails environment with keepalived, nginx, HA Proxy and Thin on Debian Lenny"
date: '2012-03-29T22:43:45-03:00'
category: webclip
summary: 'The article describes a Rails deployment with two Nginx reverse proxies, two HAProxy nodes and a Thin cluster behind a virtual IP, using keepalived to move the VIP when a node fails.'
tags: ["ruby-on-rails", "high-availability", "nginx", "haproxy"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Sleekd » Setting up a High Availability Ruby on Rails environment with keepalived, nginx, HA Proxy and Thin on Debian Lenny"
    url: "http://sleekd.com/general/keepalived_nginx_haproxy_thin_ruby_on_rails/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2012-03/sleekd-com--setting-up-high-availability-ruby-on-rails-with-keepalived-n.md"
    kind: repo
---

The article lays out a Rails deployment with keepalived, nginx, HA Proxy and Thin on Debian Lenny. Nginx sits at the front as the reverse proxy, HA Proxy handles load balancing and connection limits, and keepalived moves a virtual IP between paired machines.

## Reading notes

- Nginx and HA Proxy are described as separate layers with different roles, since nginx handles SSL, gzip and cache-server traffic while HA Proxy balances requests and checks whether Thin servers are ready.
- The setup uses two nginx boxes with keepalived so one can take over the virtual IP if the other fails.
- Keepalived is configured with a MASTER and a BACKUP, both using the same virtual router ID and virtual IP address, but the BACKUP has lower priority.
- Nginx forwards requests to an HA Proxy upstream at 192.168.1.98 on port 3100 and passes through the client IP and host headers.
- HA Proxy is configured with roundrobin balancing, maxconn 10000, a stats page on port 8080, and five Thin backends on ports 3000 to 3004.
- The Thin cluster runs on 192.168.1.101 and is started from a YAML config that sets the app directory, production environment, port 3000 and multiple servers.
- The example Rails app used for testing is Eldorado, installed from GitHub and started before Thin is launched against it.
- The article says the setup can be extended with Varnish between nginx and HA Proxy, or with memcached in nginx, but leaves those benchmarks for another article.
