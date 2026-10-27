---
title: "Vagrant, setuping machine for Node.js - Chef failure - Stack Overflow"
date: '2013-03-16T14:10:21-03:00'
category: webclip
summary: 'The Chef run fails because Vagrant cannot find the `nodejs` cookbook. The issue is resolved by renaming the cookbook folder to `nodejs` and correcting the Vagrant recipe reference.'
tags: ["vagrant", "chef", "nodejs", "cookbook"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Vagrant, setuping machine for Node.js - Chef failure - Stack Overflow"
    url: "http://stackoverflow.com/questions/13549020/vagrant-setuping-machine-for-node-js-chef-failure"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2013-03/stackoverflow-com--vagrant-setuping-machine-for-node-js-chef-failure-stack-over.md"
    kind: repo
---

The post shows a Vagrant setup for a Node.js machine that fails during `vagrant reload` with a Chef exception. The reported error says the `nodejs` cookbook is missing even though the configuration adds `nodejs-cookbook` as a recipe.

## Reading notes

- The Vagrant file provisions the box with Chef Solo and adds recipes for `apt`, `build-essential`, `nodejs-cookbook`, `chef-hosts`, and `git`.
- The Chef JSON sets Node.js version `0.8.12`, install method `source`, and npm `1.1.62`.
- The failure message is `Chef::Exceptions::CookbookNotFound: Cookbook nodejs not found`.
- The solution is to rename the cookbook folder from `nodejs-cookbook` to `nodejs` and correct the Vagrant file.
- After running `vagrant provision`, the installation completes successfully.
