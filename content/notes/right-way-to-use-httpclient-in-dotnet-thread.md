---
title: "Thread by @mjovanovictech: What is the RIGHT way to use HttpClient in .NET?"
date: '2023-12-11T16:49:32+00:00'
category: webclip
summary: 'Short thread pointing to a blog post on correct HttpClient usage in .NET, warning about common misuses like port exhaustion and noting benefits of typed clients.'
tags: ["dotnet", "httpclient", "software-engineering"]
has_commentary: false
generated_by: "openai/gpt-5.1"
sources:
  - title: "Thread by @mjovanovictech: What is the RIGHT way to use HttpClient in .NET? HttpClient is an excellent abstraction an…"
    url: "https://x.com/mjovanovictech/status/1733834641591746856"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2023-12/x-com--right-way-to-use-httpclient-in-dotnet-thread.md"
    kind: repo
---

The thread introduces the question of how to correctly use HttpClient in .NET, emphasizing that while the abstraction is powerful and easy to use, it is also easy to misuse in ways that can cause issues such as port exhaustion. It notes that IHttpClientFactory is only a partial solution and raises questions about choosing between named and typed clients, directing readers to a blog post for detailed guidance. The author adds that typed clients rely on a factory internally and highlights their strong typing as a key advantage. In follow-up replies, the author mentions implementing certain behavior inside a DelegatingHandler and promotes a weekly newsletter on software engineering and architecture for .NET developers.

## Reading notes

- HttpClient in .NET is described as an excellent and easy-to-use abstraction.
- Misuse of HttpClient can cause problems, including port exhaustion.
- The author stresses the importance of understanding incorrect usage patterns for HttpClient.
- IHttpClientFactory is presented as a partial solution that does not address every HttpClient-related problem.
- The thread raises the choice between named clients and typed clients as a key design question.
- Readers are directed to a specific blog post for answers on correct HttpClient usage.
- Typed clients are said to rely on a factory implementation under the hood.
- The main benefit of typed clients mentioned is that they provide strong typing.
- The author notes that some logic is implemented inside a DelegatingHandler.
- In replies, the author promotes a weekly newsletter focused on practical .NET engineering and architecture tips.
