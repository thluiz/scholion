---
title: "Automate your getters and setters with Proxies"
date: '2020-02-22T12:12:01+00:00'
category: webclip
summary: 'The article shows how a JavaScript Proxy can intercept property access and generate getter and setter methods at runtime, reducing boilerplate for simple classes.'
tags: ["javascript", "proxy", "getters-and-setters"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Automate your getters and setters with Proxies"
    url: "https://web.archive.org/web/20191224110410id_/https://dev.to/aminnairi/automate-your-getters-and-setters-with-proxies-5bgp"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/web-archive-org--automate-your-getters-and-setters-with-proxies.md"
    kind: repo
---

The page explains that a Proxy can handle property access on a class instance and turn method names like getConstructionYear into access to the underlying property. It first covers getters, then extends the same pattern to setters, and finally shows how to wrap the object in the class constructor or in a base class.

## Reading notes

- A motorcycle class stores plain properties, and a Proxy can expose both direct property access and getter-style method calls for them.
- The get trap checks whether the accessed name starts with get, converts the method name into the matching property name, and returns a function that reads that property.
- If the name does not start with get, the trap returns the property value directly.
- The same approach can be extended to setters by checking for names that start with set and assigning the new value to the computed property.
- The Proxy can be created inside the class constructor so instances already come wrapped with the getter and setter behavior.
- A base class can also return a Proxy from its constructor so child classes inherit the same automated getter and setter access.
- The article says this is useful for simple classes with little getter and setter logic, for faster manual coding, and for avoiding unused getter and setter methods when properties change.
- It also says Proxies can be used for more advanced patterns, including turning a class into something that communicates with an API.
