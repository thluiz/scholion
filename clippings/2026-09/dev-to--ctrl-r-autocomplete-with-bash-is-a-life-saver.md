---
url: "https://dev.to/ben/ctrlr-autocomplete-with-bash-is-a-life-saver"
captured_at: "2026-09-24T23:43:26+01:00"
title: "Ctrl+R Autocomplete with Bash is a Life Saver"
domain: "dev-to"
---

[![Ben Halpern](https://media2.dev.to/dynamic/image/width=50,height=50,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F1%2Fbabb96d0-9cd2-49bc-a412-2dc4caf94c2a.png)](https://dev.to/ben)

[Ben Halpern](https://dev.to/ben) [![Subscriber](https://assets.dev.to/assets/subscription-icon-805dfa7ac7dd660f07ed8d654877270825b07a92a03841aa99a1093bd00431b2.png)](https://dev.to/++)

Posted on Jan 17, 2017 Edited on Sep 7, 2017

I only recently started integrating `Ctrl+R` into my command-line workflow, and I am happy I did! The command, called `reverse-i-search`, starts an autocomplete within one's history and eliminates most of my `up`, `up`, `up`, `up`, `up` behavior.

![ctrl+r bash](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fvri59sdm5y2uccc2e5cf.gif)

From a UX perspective, `Ctrl+R` works perfectly for me. It's already part of my muscle memory on a few key commands I run a lot. It works by searching through your recent `.bash_history`. Once you see the command you are looking for, you can press return to execute it or use the left and right arrow buttons to modify it. If you are not seeing the command you want, or can't quite remember the params you need, you can keep hitting `Ctrl+R` to cycle through the results. It's a very natural flow.

If you're still addicted to `up`, `up`, `up`, `up`, `up`, I hope you try this command for yourself.
