---
title: "Internationalização (I18n) Mínima em Rails 3.2 - Parte 2"
date: '2012-07-15T01:27:42-03:00'
category: webclip
summary: 'A parte 2 mostra como cachear HTML gerado a partir de Markdown, integrar Bootstrap e ActiveAdmin com Globalize 3, e traduzir rotas públicas com troca de idioma pela URL.'
tags: ["rails", "i18n", "activeadmin", "routes"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Internationalização (I18n) Mínima em Rails 3.2 - Parte 2"
    url: "https://akitaonrails.com/2012/07/14/internationalizacao-i18n-minima-em-rails-3-2-parte-2/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2012-07/akitaonrails-com--internationalizacao-i18n-minima-em-rails-3-2-parte-2.md"
    kind: repo
---

O texto continua a demonstração de I18n mínima em Rails 3.2 com três frentes práticas. Primeiro, mostra como converter Markdown em HTML no model, guardar a versão cacheada em body_html e renderizar com raw na view. Depois, apresenta a instalação básica do Twitter Bootstrap e o uso de ActiveAdmin com Globalize 3 para exibir e editar traduções.

## Fichamento

- O artigo continua a Parte 1 e organiza esta parte em seções de bônus, incluindo Markdown, Twitter Bootstrap, ActiveAdmin com Globalize 3, rotas internacionalizadas e conclusão.
- Para conteúdo em formato Markdown, o texto recomenda gerar HTML com RDiscount e evitar fazer essa conversão no controller a cada requisição.
- A conversão é movida para um callback before_save no model Article, que grava o HTML em body_html junto com o texto original.
- Na view, o conteúdo cacheado é exibido com raw porque o Rails escaparia o HTML por padrão.
- O Twitter Bootstrap é usado para estilizar rapidamente a aplicação, com gems como therubyracer, less-rails e twitter-bootstrap-rails.
- O autor usa o gerador bootstrap:install para instalar os arquivos estáticos e bootstrap:themed para criar views inicializadas para Articles.
- O texto destaca que não se deve deixar require_tree solto sem entender o que está sendo carregado no pipeline de assets.
- O layout inclui navbar no topo, container para o conteúdo principal e form-actions no rodapé, além de um helper navigation_links para destacar o controller ativo.
- O ActiveAdmin é apresentado como forma rápida de montar um painel CRUD, e o artigo mostra a instalação com activeadmin e ActiveAdmin-Globalize3-inputs.
- Para evitar falha no deploy, o texto manda declarar active_admin.js e active_admin.css em config.assets.precompile.
- No show do ActiveAdmin, o artigo usa translations para exibir as versões localizadas do título e do corpo uma abaixo da outra.
- Para editar traduções no mesmo formulário, o modelo Article recebe accepts_nested_attributes_for :translations e attr_accessible para translations_attributes.
- O formulário do ActiveAdmin usa globalize_inputs para criar campos separados por locale, mantendo slug fora do bloco traduzido.
- As rotas públicas são traduzidas com rails-translate-routes, enquanto as rotas do ActiveAdmin ficam fora desse bloco de tradução.
- O arquivo config/locales/routes.yml define as palavras traduzidas para pt-BR, como welcome, users, sign_in, article e articles.
- O exemplo de rake routes mostra versões em en, pt-BR e a rota padrão para artigos, welcome e root.
- O ApplicationController passa a definir I18n.locale a partir de params[:locale] ou do cabeçalho HTTP_ACCEPT_LANGUAGE.
- O helper language_links monta botões para alternar entre os idiomas disponíveis usando url_for com o locale atual.
- O texto defende manter o idioma na URL como a forma mais prática, simples e eficiente, embora cite subdomínio, cookie e navegador como alternativas.
- Na conclusão, o autor recomenda manter UTF8 em todo o ambiente, não colocar textos em views, helpers, controllers ou models e separar strings em arquivos de locale.
- Também orienta não depender cedo de Globalize3 se o modelo ainda não precisa de traduções e evitar strftime direto em templates, preferindo helpers ou presenters.
- O fechamento lembra que data, hora e moeda exigem cuidado por causa de fusos e conversões.
