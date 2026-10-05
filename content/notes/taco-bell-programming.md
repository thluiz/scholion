---
title: "Taco Bell Programming"
date: '2016-01-04T13:32:30-03:00'
category: webclip
summary: 'The essay argues that many systems problems can be solved by reconfiguring basic Unix tools instead of adding complex stacks. Simplicity reduces failure risk and often gets the job done.'
tags: ["unix", "simplicity", "system-design", "shell"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Taco Bell Programming"
    url: "http://web.archive.org/web/20101202135616/http://teddziuba.com/2010/10/taco-bell-programming.html"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2016-01/web-archive-org--taco-bell-programming.md"
    kind: repo
---

Ted Dziuba compares Taco Bell's menu logic to software design: many results can come from a small set of ingredients or tools arranged differently. He uses that idea to argue for building systems with basic Unix utilities instead of overengineering with distributed frameworks and extra services.

## Reading notes

- Many menu items at Taco Bell come from about eight ingredients, and the author uses that as a model for software built from a small Unix toolkit.
- He contrasts the ordinary Unix approach with more complex choices like a distributed crawler in Clojure on EC2 with a message queue.
- For downloading many web pages, he proposes `xargs` and `wget`, with `split` and `rsync` only if the network becomes saturated.
- For processing large numbers of files, he shows `find ... | xargs -n1 -0 -P32 ./process` as a way to run many parsing jobs in parallel.
- He says each new piece of code or third-party service adds failure risk, and he trusts simple tools like `xargs` and `syslog` more than heavier systems.
- He treats Taco Bell programming as part of a path toward Unix Zen and says he once built most of a SOAP server from static files and Apache `mod_rewrite`.
- The closing point is practical: using proven tools may not win conference invitations, but it lowers risk and helps keep the pager quiet.
