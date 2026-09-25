---
title: "Building a single page application with vanilla js"
date: '2026-09-25T01:18:28+01:00'
category: webclip
summary: 'The post refactors a PHP blog into a framework-free SPA, outlining routing, controllers, templates, API requests, and a folder structure built with HTML, CSS, and JS.'
tags: ["single-page-application", "vanilla-js", "routing", "templates"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Building a single page application with vanilla js"
    url: "https://dev.to/vinay20045/building-a-single-page-application-with-vanilla-js/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/dev-to--building-a-single-page-application-with-vanilla-js.md"
    kind: repo
---

The post describes refactoring a PHP blog into a single-page application without a framework. It keeps the site in HTML, CSS, and JS, uses markdown posts, and aims for mobile-friendly hosting on GitHub Pages or AWS S3.

It then breaks the app into a page shell, assets, posts, and uploads, with routing based on hashchange, controllers for business logic, templates for reusable markup, views exposed through the URL, and an XHR request helper for loading content.

## Fichamento

- Critica a dependência de frameworks e defende conhecer e usar JavaScript puro com melhor estruturação do projeto.
- Reestrutura um blog PHP como SPA sem framework, com o código disponível no repositório e uma demo ao vivo.
- Define como metas evitar page loads por post, escrever posts em markdown, usar só HTML, CSS e JS, hospedar em GitHub Pages ou AWS S3 e manter compatibilidade mobile.
- Organiza o projeto em assets, index.html, posts e uploads, separando CSS, imagens, config, init, controllers, templates, utils e views.
- Usa hash-based routing para deep linking, bookmarking e SEO, registrando o roteamento no evento hashchange.
- Coloca a lógica de negócio nos controllers, que manipulam views e montam o conteúdo da página inicial a partir dos posts mais recentes.
- Reserva os templates para markup reaproveitável e deixa os hrefs como a principal exceção às regras de ligação entre camadas.
- Expõe as views ao usuário e faz uma delas chamar um controller depois de buscar o índice de posts por requisição AJAX.
- Implementa requests com XMLHttpRequest, tratando sucesso e erro por callbacks e observando cuidados com CORS.
- Diz que o site ficou rápido nas repaints, sem jank perceptível, e que ainda pretende criar um empacotador de site em Python para reduzir chamadas de rede na primeira carga.
