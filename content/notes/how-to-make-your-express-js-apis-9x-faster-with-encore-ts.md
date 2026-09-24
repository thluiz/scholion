---
title: "How to make your Express.js APIs 9x faster with Encore.ts"
date: '2026-09-24T23:59:37+01:00'
category: webclip
summary: 'O guia mostra como migrar uma app Express.js para Encore.ts para ganhar APIs type-safe, runtime em Rust e um boost de desempenho de 9x, com migração parcial ou completa.'
tags: ["express-js", "encore-ts", "typescript", "performance"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "How to make your Express.js APIs 9x faster with Encore.ts"
    url: "https://dev.to/encore/how-to-make-your-expressjs-apis-9x-faster-with-encorets-1ke2?context=digest"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/dev-to--how-to-make-your-express-js-apis-9x-faster-with-encore-ts.md"
    kind: repo
---

Encore.ts is presented as an open source backend framework for TypeScript that helps migrate an Express.js app toward type-safe APIs and higher performance. The article says Encore.ts has no npm dependencies, includes built-in backend features, and can be self-hosted or used with Encore Cloud.

It then compares Express.js and Encore.ts across migration paths and features. A quick forklift migration can wrap an existing router as a catch-all handler and give partial performance gains, while a full migration unlocks distributed tracing, architecture diagrams, API client generation, and the full 9x speedup. The rest of the guide walks through APIs, microservice communication, authentication, request validation, error handling, static files, template rendering, testing, databases, and logging.

## Fichamento

- O texto apresenta o Encore.ts como um framework backend open source para TypeScript pensado para backends robustos e type-safe.
- A proposta central é migrar uma app Express.js para Encore.ts para obter APIs com tipagem e um ganho de desempenho de 9x.
- O artigo afirma que o Encore.ts tem zero dependências npm, inclui funcionalidades prontas para uso e pode ser executado em qualquer serviço que aceite contêineres Docker ou no Encore Cloud Platform.
- O runtime do Encore.ts roda em Rust, usa um event loop assíncrono e multithread, e o texto atribui a isso 9x mais requests por segundo e 80% menos latência de resposta em relação ao Express.js.
- Na migração rápida, o texto propõe embrulhar o roteador HTTP existente em um handler catch-all para mover a aplicação de uma vez e depois ir extraindo endpoints para Encore.ts.
- Essa abordagem dá um ganho parcial imediato, mas impede aproveitar totalmente tracing distribuído, diagramas automáticos, documentação de API e geração de client enquanto tudo continuar passando pelo handler genérico.
- Na migração completa, o objetivo é substituir de vez a dependência de Express.js e passar a usar todos os recursos e o ganho total de desempenho do Encore.ts.
- A comparação por recursos cobre APIs, comunicação entre serviços, autenticação, validação de requisições, tratamento de erros, arquivos estáticos, templates, testes, banco de dados e logging.
- Em APIs, o texto mostra que Express.js usa `app.get` e similares, enquanto Encore.ts usa `api` com schema tipado e também suporta endpoints raw quando for preciso acessar a requisição HTTP subjacente.
- Em comunicação entre microsserviços, o texto diz que chamadas entre serviços no Encore.ts parecem chamadas locais, mas são convertidas em chamadas HTTP reais com dados de trace.
- Em autenticação, o texto explica que o Encore.ts usa `auth: true`, `authHandler` e `getAuthData` para identificar o usuário autenticado.
- Em validação, o texto afirma que o Encore.ts valida automaticamente cabeçalhos, query params e body a partir do schema e retorna erro 400 quando a payload não bate com o esperado.
- Em erros, o texto diz que lançar exceções gera 500 e que `APIError` permite retornar códigos específicos.
- Em arquivos estáticos e templates, o texto mostra suporte nativo a `api.static` e uso de `api.raw` para servir HTML dinâmico.
- Em testes, o texto afirma que os endpoints do Encore.ts podem ser chamados diretamente nos testes e executados com `encore test`.
- Em banco de dados, o texto diz que o Encore.ts provisiona bancos automaticamente, usa migrações e fornece métodos como `.query`, `.queryRow` e `.exec`.
- Em logging, o texto destaca suporte nativo a structured logging integrado ao tracing distribuído.
