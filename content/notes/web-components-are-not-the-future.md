---
title: "Web Components Are Not the Future"
date: '2026-09-25T00:51:57+01:00'
category: webclip
summary: 'O texto defende que Web Components oferecem alguma ergonomia, mas cobram um custo amplo em abstrações, compatibilidade e evolução, o que pode travar escolhas melhores para o futuro da web.'
tags: ["web-components", "javascript-frameworks", "front-end"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Web Components Are Not the Future"
    url: "https://dev.to/ryansolid/web-components-are-not-the-future-48bh?context=digest"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/dev-to--web-components-are-not-the-future.md"
    kind: repo
---

O autor retoma uma posição que já havia defendido antes e diz que a situação piorou. Ele vê os Web Components como uma promessa de portabilidade e interoperabilidade que parece atraente, mas que traz um custo alto para o ecossistema porque força a web a se organizar em torno de uma abstração rígida.

## Fichamento

- O texto diz que Web Components foram pensados para funcionar como elementos nativos, independentes de ferramenta, com a promessa de proteger sites e aplicações contra migração futura.
- O autor argumenta que a existência de um padrão ambicioso favorece algumas escolhas e dificulta explorar alternativas, porque um padrão passa a influenciar a forma como a plataforma inteira é pensada.
- Ele usa JSX como exemplo de tecnologia cuja padronização teria criado problemas, já que diferentes frameworks e ferramentas tratam sua semântica de maneiras distintas.
- O texto afirma que o custo de oportunidade aparece antes mesmo do código, porque decisões de arquitetura e de abstração acabam exigindo limites que depois são difíceis de desfazer.
- Segundo o autor, Web Components partem de Custom Elements, mas elementos e componentes não são a mesma coisa, então toda interface precisa passar pelo DOM, mesmo quando isso não é o encaixe ideal.
- Ele observa que atributos e propriedades, regras de booleanos, reflexão entre atributos e propriedades e extensões usadas por bibliotecas de templating tornam o suporte a custom elements mais complexo.
- O texto cita que algumas bibliotecas usam prefixos como `attr:`, `prop:` e `bool:` e que isso obriga runtimes e compiladores a conhecerem mais casos especiais.
- O autor afirma que o comportamento de clone, upgrade, lifecycle no DOM e contexto reativo cria atritos para sistemas como reatividade e APIs de contexto.
- Ele também menciona que o Shadow DOM altera o roteamento de eventos e que isso afeta casos como composição de eventos e `focusin`.
- O texto diz que há custo de performance e que, no servidor, Web Components continuam exigindo soluções específicas porque não há DOM, então SSR e hydration precisam de wrappers e overhead extra.
- O autor sustenta que a complexidade extra não fica restrita a quem usa Web Components, pois também pesa sobre as ferramentas que precisam dar suporte a eles.
- Ele afirma que avanços como resumability, partial hydration e selective hydration dependem de delegação de eventos, e que isso entra em tensão com o Shadow DOM.
- O texto diz que componentes tendem a ser mais uma questão de experiência de desenvolvimento do que um item que deva permanecer no output final.
- Na comparação com micro-frontends e microservices, o autor vê valor na portabilidade, mas diz que o custo de misturar versões, bibliotecas e frameworks aumenta, sobretudo no front-end, onde bytes de JS importam muito.
- Ele conclui que os usos mais convincentes são casos pontuais, como um widget de terceiros ou um contêiner de microfrontend, mas nesses casos a fricção já é baixa o bastante para o ganho não justificar a promessa geral.
- O texto termina dizendo que Web Components podem ser úteis em alguns cenários, mas que o problema está na promessa de serem mais do que são, porque isso distorce o resto da web e transfere o custo para todos.
