---
title: "Série Backbone.js: Parte 01 - Introdução"
date: '2012-06-11T12:08:24-03:00'
category: webclip
summary: 'Apresenta o Backbone.js como um framework para organizar aplicações web com Models, Collections e Views, e mostra um Hello World com uma View renderizada no body.'
tags: ["backbone-js", "javascript", "views", "models"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Série Backbone.js: Parte 01 - Introdução"
    url: "https://imasters.com.br/front-end/serie-backbonejs-parte-01-introducao"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2012-06/imasters-com-br--serie-backbonejs-parte-01-introducao.md"
    kind: repo
---

O texto apresenta o Backbone.js como um framework JavaScript para estruturar aplicações web com Models, Collections e Views, além de integração nativa com backends RESTful e JSON. A proposta da série é mostrar esses componentes e, ao final, construir uma aplicação simples de contatos.

A introdução relaciona o uso do Backbone.js com aplicações que tendem a acoplar a UI ao DOM e a depender de seletores jQuery e callbacks. No exemplo inicial, uma View renderiza "Hello World" no body da página, com initialize chamando render e a View sendo instanciada após o carregamento do documento.

## Fichamento

- O Backbone.js fornece componentes para melhorar a estrutura de aplicações web.
- A série terá 6 artigos e terminará com uma aplicação simples de contatos.
- O texto descreve um problema comum em aplicações web: UI acoplada ao DOM, uso intenso de seletores jQuery e falta de padrão para dados e código JavaScript.
- Com Backbone.js, dados do servidor podem ser representados como Models no código JavaScript.
- O Model pode ter suporte a validação, exclusão e gravação no servidor.
- A View apresenta o Model ao usuário e pode reagir a eventos do Model, como mudanças de atributos e remoção.
- Esse modelo de organização reduz a dependência de inspeção manual do DOM para atualizar o HTML.
- A separação entre partes do JavaScript melhora a manutenibilidade.
- A principal dependência do Backbone.js é o Underscore.js.
- Para RESTful, DOM básico e histórico, o texto cita json2.js e jQuery ou Zepto.
- O Hello World é implementado com uma View renderizada na página.
- No exemplo, a View usa `body` como `el` e adiciona um `<h1>Hello World</h1>`.
- O método `initialize` é chamado ao criar a instância da View.
- O código-fonte da série está no repositório backbone-tutorial-series no GitHub.
- A documentação do Backbone.js, tutoriais e um exemplo de aplicação são indicados como referências.
