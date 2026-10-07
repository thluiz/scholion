---
title: "Add subdomains to the Compatibility View List"
date: '2014-12-18T17:59:06-03:00'
category: webclip
summary: 'The page explains how to add only a problematic subdomain to Internet Explorer’s Compatibility View list by using Group Policy, instead of applying Compatibility View to the whole domain.'
tags: ["internet-explorer", "compatibility-view", "group-policy"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Add *subdomains* to the Compatibility View List"
    url: "http://www.codeproject.com/Articles/662444/Add-subdomains-to-the-Compatibility-View-List"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2014-12/codeproject-com--add-subdomains-to-the-compatibility-view-list.md"
    kind: repo
---

The page says IE’s Internet Options will not accept a subdomain such as `something.mysite.com` in the Compatibility List, so the default workaround is to add the full domain instead. It then shows a Group Policy-based method for managing the list so that only the subdomain uses Compatibility Mode.

## Reading notes

- IE’s Internet Options reject a subdomain entry for the Compatibility List, which pushes the user toward adding the full domain.
- The article says this can be handled through Group Policy, using the policy list for Internet Explorer 7 sites.
- It instructs the user to open `gpedit.msc`, go to `Computer Configuration > Administrative Templates > Windows Components > Internet Explorer > Compatibility View`, and choose `Use Policy List of Internet Explorer 7 sites`.
- The text says the user must be an administrator to perform the changes.
- After logging out and back in, the full domain no longer uses Compatibility Mode while the chosen subdomain does.
