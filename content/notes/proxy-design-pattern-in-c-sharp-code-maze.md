---
title: "Proxy Design Pattern in C# - Code Maze"
date: '2026-09-24T23:18:02+01:00'
category: webclip
summary: 'The Proxy pattern adds a wrapper around a real object to control access and add logic without changing the original service. The article shows a caching proxy in C# and mentions logging, protection, remote, virtual and selection proxies.'
tags: ["proxy-pattern", "csharp", "caching", "design-patterns"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Proxy Design Pattern in C# - Code Maze"
    url: "https://code-maze.com/csharp-proxy-design-pattern/?ref=dailydev"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/code-maze-com--proxy-design-pattern-in-c-sharp-code-maze.md"
    kind: repo
---

The article explains the Proxy design pattern as an extra layer of control over access to an object. The proxy implements the same contract as the real subject, holds a reference to it, and can run its own actions before or after delegating a call.

It uses an exchange-rate service to show why a proxy is useful when repeated remote calls hurt performance. A caching proxy keeps the client and the original service unchanged, stores the first result, and serves later requests from cache. The text also mentions logging, protection, remote, virtual, and selection proxies, and notes that proxies can add complexity, maintenance overhead, performance cost, cache invalidation issues, leaky abstraction, and security risks when used alone.

## Fichamento

- O proxy é um padrão estrutural que coloca uma camada extra de controle sobre o acesso a um objeto, usando um wrapper que age em nome do objeto real.
- O proxy implementa os mesmos contratos do sujeito real e mantém uma referência a ele para delegar a operação antes ou depois de executar outras ações.
- O padrão resolve casos em que se quer acrescentar lógica sem alterar a funcionalidade nem a intenção do objeto original.
- No exemplo de exchange rates, chamadas repetidas a um serviço remoto geram requisições desnecessárias e pioram o desempenho.
- A solução proposta é carregar os dados uma vez, guardá-los em cache por um tempo e reutilizá-los nas chamadas seguintes.
- O código do proxy de cache implementa `IExchangeRateService`, cria um `ExchangeRateService` interno e guarda o retorno em `_exchangeRates`.
- Se `_exchangeRates` já tem dados, o proxy devolve o cache; se não tem, chama o serviço real, guarda o resultado e então retorna os dados.
- O cliente só precisa passar a usar `CachedExchangeRateService`, sem mudar a lógica de consumo.
- O artigo também cita proxy de logging, proxy de proteção, proxy remoto, proxy virtual e proxy de seleção como outros usos.
- Entre os cuidados apontados estão complexidade extra, custo de manutenção, possível impacto de desempenho, dificuldade de sincronizar estado, abstração vazada e riscos de confiar apenas no proxy para segurança.
