---
title: "Série Backbone.js: Parte 02 - View"
date: '2012-07-25T18:13:11-03:00'
category: webclip
summary: 'O artigo explica Backbone.View como a camada que apresenta dados e elementos visuais, mostra el, render, $el, templates e eventos, e fecha com um exemplo de PostView.'
tags: ["backbonejs", "backbone-view", "templates", "events"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Série Backbone.js: Parte 02 - View"
    url: "http://imasters.com.br/artigo/25066/javascript/serie-backbonejs-parte-02-view"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2012-07/imasters-com-br--serie-backbonejs-parte-02-view.md"
    kind: repo
---

O artigo apresenta Backbone.View como a parte do Backbone.js responsável por mostrar dados e elementos visuais em uma aplicação MVC. Mostra como definir el, tagName, id, className e attributes, como render() preenche o elemento com HTML e como $el reduz o acoplamento com jQuery ou Zepto. Também cita remove() e make() como métodos comuns da View.

Depois, mostra o uso de templates com Underscore.js no exemplo de PostView e a definição de eventos pelo hash events, incluindo dblclick, click em #add-button e blur em #username. O artigo fecha com o código final de PostView e index.html e informa que o próximo artigo trata de Backbone.Model.

## Fichamento

- Backbone.View é a camada responsável por apresentar dados e elementos visuais aos usuários em uma aplicação MVC.
- el é o elemento DOM onde a View está ou será inserida.
- initialize() funciona como construtor de uma classe Backbone.
- tagName, id, className e attributes definem o elemento HTML criado para a View.
- render() preenche el com o HTML necessário para apresentar o model.
- $el é construído automaticamente quando o Backbone detecta jQuery ou Zepto e funciona como instância em cache de $(this.el).
- remove() remove a View do DOM da página.
- make() cria um novo elemento DOM a partir dos atributos informados e o retorna.
- Templates podem ser usados com Backbone.View por meio do Underscore.js, como em _.template().
- A notação <%= %> do template substitui identificadores por atributos correspondentes do objeto renderizado.
- O hash events define eventos da View no formato {"evento seletor": "callback"}.
- Os eventos podem chamar métodos como fullScreen, newPost e searchUsername.
- delegateEvents() aplica os eventos e undelegateEvents() remove os eventos definidos na View.
- O exemplo final combina Backbone.View, Underscore.js, jQuery e uma página HTML que adiciona a View renderizada ao body.
