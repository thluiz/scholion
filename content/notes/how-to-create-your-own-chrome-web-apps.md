---
title: "How To Create Your Own Chrome Web Apps"
date: '2012-03-30T19:25:57-03:00'
category: webclip
summary: 'Explains how to make a basic Chrome Web App from an existing website by creating a manifest.json, adding a 128×128 icon, testing the unpacked app, and packaging it into a .crx file.'
tags: ["chrome-web-apps", "manifest-json", "crx", "chrome-web-store"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "How To Create Your Own Chrome Web Apps | VikiTech.com"
    url: "http://www.vikitech.com/2398/create-chrome-web-apps"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2012-03/vikitech-com--how-to-create-your-own-chrome-web-apps.md"
    kind: repo
---

The post says a Chrome Web App can be made from an existing website by preparing just two required files: a manifest and an icon. It also explains that the manifest defines the app’s name, description, version, launch URL, and permissions, while the icon appears on Chrome’s New Tab page.

## Reading notes

- A Chrome Web App consists of a .crx file with metadata for the app.
- A hosted app must include an icon and a manifest.
- The manifest is a JSON file named manifest.json.
- The icon should be 128×128 pixels.
- The example manifest includes name, description, version, icons, app URLs, launch web_url, and permissions.
- Permissions such as unlimitedStorage and notifications are requested through the manifest.
- To verify the app, put manifest.json and 128.png in a folder and load it as an unpacked extension in Chrome.
- If Chrome reports an error, the manifest should be checked for valid JSON and the correct filename.
- If the app works, it appears in the Chrome launcher and can be tested by clicking its icon.
- To share or upload the app, use Pack Extension to create a .crx file and a .pem private key.
- The .crx file can be installed by dragging it into Chrome.
- The .pem file is needed for later updates to the app.
