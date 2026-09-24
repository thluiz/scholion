---
title: "Announcing NgRx 19: NgRx Signals Features, Action Signals, and more!"
date: '2026-09-25T00:40:25+01:00'
category: webclip
summary: 'NgRx 19 adds new Signals features, a signalMethod utility, dev-mode mutation checks, and Store support for dispatching actions from signal changes, and recommends NgRx Signals for local state.'
tags: ["ngrx", "angular-signals", "state-management", "signals"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Announcing NgRx 19: NgRx Signals Features, Action Signals, and more!"
    url: "https://dev.to/ngrx/announcing-ngrx-19-ngrx-signals-features-action-signals-and-more-2b35?ref=dailydev"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/dev-to--announcing-ngrx-19-ngrx-signals-features-action-signals-and-.md"
    kind: repo
---

NgRx 19 introduces updates to NgRx Signals, support for dispatching actions when signals change, and a recommendation to use NgRx Signals as the default local state library for Angular apps. It also announces workshops, a new docs site, and upgrade guidance for Angular 19, TypeScript 5.5, and RxJS.

## Fichamento

- A versão 19 traz melhorias para NgRx Signals, que já estava estável desde a v18 e recebeu atualizações para melhorar a experiência de desenvolvimento.
- O novo `withProps` permite definir props ao criar um SignalStore, organizar dependências em um só lugar e integrar recursos como `resource` e `linkedSignal`.
- A utilidade `signalMethod` oferece uma forma de lidar com side effects usando apenas signals, com entrada flexível, sem exigir injection context e com tracking explícito do signal do parâmetro.
- Em modo de desenvolvimento, `patchState` passa a aplicar deep freeze no estado para impedir mutações e preservar atualizações imutáveis.
- O NgRx Store agora aceita dispatch de ações que leem signals, executando inicialmente e sempre que o signal observado muda, com cuidado extra fora do injection context.
- O texto diz que NgRx Signals se tornou a biblioteca recomendada para state local em aplicações Angular, com sugestão de começar pelo SignalStore em projetos novos e migrar para `@ngrx/signals` em projetos existentes.
- A publicação também anuncia workshops do time NgRx, um novo site de documentação e mudanças deprecation/breaking changes com guia de migração para a versão 19.
- Para atualizar, o texto informa versões mínimas de Angular, Angular CLI, TypeScript e RxJS e mostra os comandos `ng update` para `@ngrx/store@19` e `@ngrx/signals@19`.
