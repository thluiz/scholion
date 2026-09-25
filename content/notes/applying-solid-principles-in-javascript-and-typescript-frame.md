---
title: "Applying SOLID Principles in JavaScript and TypeScript Framework"
date: '2026-09-25T01:20:49+01:00'
category: webclip
summary: 'The article shows how SOLID principles apply in React and Angular with JS and TS examples, using refactors to separate responsibilities, ease extension, and reduce coupling.'
tags: ["solid", "javascript", "typescript", "react", "angular"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Applying SOLID Principles in JavaScript and TypeScript Framework"
    url: "https://dev.to/wafa_bergaoui/applying-solid-principles-in-javascript-and-typescript-framework-2d1d?context=digest"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/dev-to--applying-solid-principles-in-javascript-and-typescript-frame.md"
    kind: repo
---

The article applies the SOLID principles to JavaScript and TypeScript frameworks such as React and Angular. It uses anti-patterns and refactors to show how code can be split by responsibility, extended without modifying core logic, and decoupled through abstractions.

## Fichamento

- SRP aparece quando componentes, serviços ou classes acumulam UI, lógica de negócio, atualização de dados e notificações; a solução apresentada separa essas tarefas em hook, componente e serviço específico.
- OCP é mostrado em funções de validação e serviços de notificação, com a ideia de adicionar regras ou novos tipos por meio de novas implementações sem alterar o código central.
- LSP é ilustrado com componentes de botão e link em React e com Rectangle e Square em TypeScript; a proposta é manter substituição segura e comportamento consistente entre tipos relacionados.
- ISP é aplicado quando componentes recebem props demais ou quando uma interface obriga uma classe a implementar método que não usa; o texto propõe dividir interfaces e componentes menores.
- DIP é apresentado como dependência de abstrações em vez de implementações concretas, tanto por injeção de funções em React quanto por interfaces em Angular.
- O fechamento incentiva prática, revisão em equipe e exploração de padrões como MVC, MVVM e CQRS para levar esses princípios adiante.
