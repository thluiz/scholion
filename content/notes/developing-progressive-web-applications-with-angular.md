---
title: "Developing Progressive Web Applications with Angular (and Ionic)"
date: '2020-04-23T02:14:26+00:00'
category: webclip
summary: 'A hands-on guide for Angular developers to turn an existing web app into an installable PWA, with offline caching, Lighthouse checks, home-screen install, splash screens, and update flows.'
tags: ["angular", "progressive-web-apps", "typescript", "mobile-app-development"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Amazon.com: Developing Progressive Web Applications with Angular (and Ionic): How to Build and Deploy Mobile Applications without Paying Apple or Google for the Privilege (Coding Crusaders) eBook : Callaghan, Michael D.: Kindle Store"
    url: "https://www.amazon.com/dp/B087J1TF29/ref=cm_sw_r_tw_api_i_qInOEbHBE4VZM"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/amazon-com--developing-progressive-web-applications-with-angular.md"
    kind: repo
---

The book presents a practical route from a deployed Angular app to an installable PWA. It follows the Ends Well sample from a non-PWA version to PWA and update handling, and says the same steps can be applied to an existing project. The focus is on commands, file names, and working sample code for developers who want mobile and desktop reach from one codebase.

## Reading notes

- It walks experienced web developers through Angular 22 and the steps needed to add PWA support.
- It covers HTTPS hosting and Lighthouse audits to check whether the app is ready to ship.
- It shows how to add @angular/pwa and configure offline mode with ngsw-config.json.
- It explains caching APIs and images with dataGroups so repeat visits load faster.
- It includes install prompts, icons, custom splash screens, and home-screen installation.
- It describes the modern SwUpdate.versionUpdates flow and VERSION_READY for shipping updates.
- The second edition adds iOS PWA guidance, expanded hosting and performance notes, and pointers to push notifications, Trusted Web Activities, and Capacitor when a PWA is not enough.
