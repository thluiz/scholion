---
title: "Race conditions on Facebook, DigitalOcean and others"
date: '2015-04-27T09:22:46-03:00'
category: webclip
summary: 'The post describes race condition bugs that let the author inflate Facebook page reviews, create multiple usernames on one account, and redeem DigitalOcean promo codes multiple times before the fixes arrived.'
tags: ["race-conditions", "facebook", "digitalocean", "security-bug-reports"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Race conditions on Facebook, DigitalOcean and others"
    url: "http://josipfranjkovic.blogspot.com.br/2015/04/race-conditions-on-facebook.html?m=1"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2015-04/josipfranjkovic-blogspot-com-br--race-conditions-on-facebook-digitalocean-and-others.md"
    kind: repo
---

The post collects race condition reports against Facebook and DigitalOcean. In each case, the author sends many requests in a short time window so the server processes them inconsistently, which lets one account produce effects the site was supposed to limit.

## Reading notes

- On Facebook, repeated /ajax/pages/review/add requests let one account create multiple reviews, delete one, and repeat the process to inflate or deflate page ratings.
- Another Facebook race condition let one account end up with multiple usernames by sending a list of desired usernames to the endpoint at the same time.
- The Facebook review bug was reported on April 14, 2014, fixed on June 15, 2014, and paid a $3000 bounty on June 25, 2014.
- The multiple-username bug was reported on April 14, 2014 and confirmed fixed on October 16, 2014, but no bounty was awarded.
- On DigitalOcean, the same promo code could be reused by sending the POST request to /promos many times in a short time frame, which added money multiple times to the account.
- The DigitalOcean issue was reported on January 11, 2015, confirmed on January 13, 2015, and fixed on January 21, 2015.
- DigitalOcean let the author keep test accounts with about $550 total, while LastPass is mentioned as having fixed a similar promo-code issue in three days.
