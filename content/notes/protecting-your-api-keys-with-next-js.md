---
title: "Protecting your API keys with Next JS"
date: '2021-02-13T08:47:31-03:00'
category: webclip
summary: 'The page shows how Next.js API Routes and a .env.local file can keep a private key out of client-side code by moving the request through server-side code instead.'
tags: ["next-js", "api-routes", "environment-variables", "api-keys"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Protecting your API keys with Next JS - DEV Community 👩‍💻👨‍💻"
    url: "https://dev.to/ivanms1/protecting-your-api-keys-with-next-js-21ej"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2021-02/dev-to--protecting-your-api-keys-with-next-js.md"
    kind: repo
---

The page explains that API keys placed in frontend code can still appear in the network tab. It recommends using a server-side proxy instead, and presents Next.js API Routes as a ready-to-use Node.js environment for that purpose.

## Reading notes

- It frames the problem through Max, who thinks an `.env` file keeps API keys safe, but the keys are still visible in the network tab.
- It says there is no good way to protect keys in the frontend, so the request should go through a backend proxy because backend code is not exposed to the browser.
- It describes Next.js API Routes as an integrated server-side option that can serve API endpoints.
- It shows a basic setup with `npx create-next-app next-api-key` or `yarn create next-app next-api-key`, then `cd next-api-key`.
- It introduces `.env.local` as a file whose variables are only available in Next.js’s Node.js environment, not in the browser.
- It shows an example `pages/api/hello.js` endpoint that returns JSON from the server side.
- It shows the client calling `/api/hello` from the browser.
- It places `SECRET_KEY=someSecretKeyThatNoOneShouldSee` in `.env.local` and uses `process.env.SECRET_KEY` inside `pages/api/hello.js`.
- It notes that `fetch` is not available in Node, so a library like `axios` or `node-fetch` is needed for server-side requests.
- It ends by saying the key is no longer visible in the network tab when the request goes through the API route.
