---
url: "https://dev.to/ben/headache-as-a-service-things-to-consider-before-taking-on-external-software-services"
captured_at: "2026-09-24T23:45:15+01:00"
title: "Headache as a service: Things to consider before taking on service dependencies"
domain: "dev-to"
---

[![Cover image for Headache as a service: Things to consider before taking on service dependencies](https://media2.dev.to/dynamic/image/width=1000,height=420,fit=cover,gravity=auto,format=auto/http%3A%2F%2Fwww.baliteambuildingcompany.com%2Fwp-content%2Fuploads%2Fsites%2F8%2F2013%2F11%2Fservice-excellence.jpg)](https://media2.dev.to/dynamic/image/width=1000,height=420,fit=cover,gravity=auto,format=auto/http%3A%2F%2Fwww.baliteambuildingcompany.com%2Fwp-content%2Fuploads%2Fsites%2F8%2F2013%2F11%2Fservice-excellence.jpg)

[![Ben Halpern](https://media2.dev.to/dynamic/image/width=50,height=50,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F1%2Fbabb96d0-9cd2-49bc-a412-2dc4caf94c2a.png)](https://dev.to/ben)

It is nice when you can find a great "software as a service" (SAAS) product to do just the thing you needed done. These products are often priced well, so it is better to pay for it as opposed to incurring the cost of developer hours. If it is a solo project, these services often have free tiers for small scales.

However, there are always costs, and they often occur down the line. In exchange for a few conveniences, your code now has dependencies that can be difficult to stub in your testing environments and make it your codebase more difficult to manage across development environments. In my experience, external services pose some of the biggest frustrations when trying to bring new people on to a project and get them set up to start writing code. In terms of software design, you also run the risk of the service not providing support for a critical use-case down the line that you could have easily extended your own code to do. You cannot just fork a proprietary service you subscribe to.

Software development, when you have the option to rely on services and external libraries, largely becomes about risk management. So much of the value in a service is the infrastructure, security, support or other tasks the company takes on. Each task they take on may decrease some of your personal risk and increase others.

All-in-all, it is usually preferable to take on a reasonable number of self-hosted dependencies and only add services to your codebase when you are getting clear, special value, that inherently does not lend itself to self-hosting. That is, take on innovative services that level-up your product, or services that provide essential infrastructure, not just convenience-based software APIs in the cloud. Those will often trend towards inconvenience in the long run.

If you do take on external services, write good wrappers right away. Wrappers provide an interface which will allow you to maintain internal naming conventions, swap out different services, create abstractions, maintain future extensibility and sanely test your code.

I have a particular set of experiences, so my thoughts may not be universally applicable. If you disagree or have any tack-on advice, let me know!
