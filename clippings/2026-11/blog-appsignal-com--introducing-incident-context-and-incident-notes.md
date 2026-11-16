---
url: "https://blog.appsignal.com/2019/06/25/introducing-context-incident-notes.html?utm_source=boostedblogpost&utm_medium=twitter&utm_campaign=product-incident-context-notes-02-organic"
captured_at: "2026-11-16T18:50:09+00:00"
title: "Introducing Incident Context and Incident Notes"
domain: "blog-appsignal-com"
---

The Incident page for errors and performance incidents is one of the most used pages in our application. It is where you land from a notification. Often, that doesn’t mean good things.

Today, we are launching two improvements to that page:

*   More context for each incident
    
*   The ability to add notes to incidents
    

## [](#adding-more-context-to-incidents)Adding more context to Incidents

The context for incidents shows you what’s going on at the time of the faulty request. We already showed host metrics, but we are now adding:

*   Did any (other) errors occur?
    
*   What performance issues were happening?
    
*   Were any Anomaly Detection Alerts active at the same time?
    

With these, it is easier to see if the root cause for an Incident could lie somewhere else, or if multiple Incidents are related.

[

![incident-context-screenshot](https://blog.appsignal.com/_next/image?url=%2Fimages%2Fblog%2F2019-06%2Fcontext-screenshot-blur.jpg&w=3840&q=90&dpl=dpl_Ax1ADjVZhnhkqd7Npas4Kx2uqF9C)



](https://blog.appsignal.com/images/blog/2019-06/context-screenshot-blur.jpg)

## [](#build-collective-knowledge-in-incident-notes)Build collective knowledge in incident notes

We understand that for many issues, it’s the combination of technical _and historical_ knowledge that enables you to solve them. When you visit an Error or Performance incident, you can now leave a note for your colleagues or future you.

[

![incident-notes-screenshot](https://blog.appsignal.com/_next/image?url=%2Fimages%2Fblog%2F2019-06%2Fnotes-screenshot-blur.jpg&w=3840&q=90&dpl=dpl_Ax1ADjVZhnhkqd7Npas4Kx2uqF9C)



](https://blog.appsignal.com/images/blog/2019-06/notes-screenshot-blur.jpg)

The incident notes make it easy to add information to an error or performance incident. With relevant knowledge stored right at the place where you’re looking when fixing an issue, you can save others (and yourself) from starting from zero again in the future. E.g., leave a note about how to solve the incident, or note the steps you took to prevent it from happening again.

Though we don’t wish any incidents upon you, we [can’t wait to hear](mailto:support@appsignal.com) how you are using this, and how you’d like us to continue improving it.
