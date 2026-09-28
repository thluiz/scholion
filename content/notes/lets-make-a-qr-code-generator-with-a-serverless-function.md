---
title: "Let’s Make a QR Code Generator With a Serverless Function!"
date: '2022-06-08T20:39:12-03:00'
category: webclip
summary: 'The article shows how to move QR code generation into a DigitalOcean serverless function so the heavy qrcode package stays off the main site bundle and the function can be called through a URL.'
tags: ["serverless-functions", "qr-codes", "digitalocean", "javascript"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Let's Make a QR Code Generator With a Serverless Function! | CSS-Tricks - CSS-Tricks"
    url: "https://css-tricks.com/lets-make-a-qr-code-generator-with-a-serverless-function/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2022-06/css-tricks-com--lets-make-a-qr-code-generator-with-a-serverless-function.md"
    kind: repo
---

The article explains that QR code generation can be moved to a cloud function instead of shipping the full `qrcode` package with a site’s scripts. It uses DigitalOcean Functions and a small Node.js function that returns either a base64 image string or an `<img>` tag.

## Reading notes

- QR code generators already exist, but the `qrcode` package is about 180 KB, so the author does not want to load it with the rest of the site scripts.
- Cloud functions are presented as a place for code that runs only when needed, like a small API.
- DigitalOcean Functions is used for this example, and the article says functions are easy to deploy.
- A local project is created with `doctl serverless init --language js qr-generator`.
- The generated project includes a `/packages` folder, and the example adds a `qr` folder beside the sample function.
- Inside `packages/sample/qr`, the `qrcode` package is installed with `npm install --save qrcode`.
- The `qr.js` function requires `qrcode` and exports `main`, which calls `qrcode.toDataURL(args.text)`.
- The function returns a response with `content-type: text/html; charset=UTF-8` and either the raw data URL or an `<img>` tag using that data URL.
- The function can be tested in the terminal with `doctl serverless functions invoke sample/qr -p "text:css-tricks.com"`.
- The `project.yml` file must match the folder and function names, so `hello` is changed to `qr`.
- Deployment uses `doctl sandbox connect` and then `doctl sandbox deploy qr-generator`.
- After deployment, `doctl sbx fn get sample/qr --url` returns the live function URL.
- The article closes by saying the API can then be fetched to generate the QR code.
