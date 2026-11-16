---
url: "https://dev.to/kefranabg/demystifying-ssr-csr-universal-and-static-rendering-with-animations-m7d"
captured_at: "2026-11-16T00:28:42+00:00"
title: "🛠✨ Demystifying SSR, CSR, universal and static rendering with animations"
domain: "dev-to"
---

[![Cover image for 🛠✨ Demystifying SSR, CSR, universal and static rendering with animations ](https://media2.dev.to/dynamic/image/width=1000,height=420,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fi%2Fpl7f52xnyatk7y3d7yjc.jpg)](https://media2.dev.to/dynamic/image/width=1000,height=420,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fi%2Fpl7f52xnyatk7y3d7yjc.jpg)

[![Franck Abgrall](https://media2.dev.to/dynamic/image/width=50,height=50,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F160055%2F57f5d7e1-1523-43ba-aea8-45e6e5d98ff3.jpeg)](https://dev.to/kefranabg)

📖 Parts

1) [Server Side Rendering](#ssr)

2) [Client Side Rendering](#csr)

3) [Universal Rendering](#ur)

4) [Static Rendering](#sr)

5) [Comparisons](#comparisons)

Sometimes it might be hard to understand the differences between the different web rendering solutions. If you're a web developer, you've probably heard these words:

*   Server Side Rendering (SSR)
*   Client Side Rendering (CSR)
*   Universal Rendering (sometimes simplified to "SSR")
*   Static Rendering (or JAMStack depending on the tool you're using)

Here are 4 videos explaining in a simplified manner the process of each solution from a user's perspective. Know that the user scenario is the exact same in the 4 videos.

In the [last section](#comparisons) you'll find a comparison listing benefits and drawbacks of each solution.

## [](#server-side-rendering-ssr)Server Side Rendering (SSR)

**⚠️ Note:** Here I'm talking about full server side rendered websites (you know, old SSR websites 😉). This architecture was widely used before Single Page Apps were introduced.

## [](#client-side-rendering-csr)Client Side Rendering (CSR)

**Frameworks using CSR:** Vue, React, Angular

## [](#universal-rendering)Universal Rendering

**Frameworks using Universal Rendering:** Nuxt.js, Next.js, Angular Universal

## [](#static-rendering)Static Rendering

**Frameworks/Tools using Static Rendering:** Gatsby, VuePress, Gridsome, Next.js, Hugo, Jekyll

## [](#comparisons)Comparisons

Server Side Rendering

Client Side Rendering

Universal Rendering

Static Rendering

SEO

👍

👎

👍

👍

Fast initial load to show the full content of the page

⚡️⚡️

⚡️

⚡️⚡️

⚡️⚡️⚡️

Full page reload when navigating

yes

no

no

it depends on the tool you're using

Requires server hosting

yes

no

yes

no

Fluid seamless user experience on page navigation

👎

👍

👍

👍

Integrates well with websites based on frequent/real-time updates

👍

👍

👍

😕

Feel free to contact me on [twitter](https://twitter.com/FranckAbgrall) if you have questions!

🐦 [Twitter](https://twitter.com/FranckAbgrall)

💻 [GitHub](https://github.com/kefranabg)
