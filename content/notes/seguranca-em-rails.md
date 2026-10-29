---
title: "Segurança em Rails"
date: '2016-04-11T12:08:37-03:00'
category: webclip
summary: 'O post reúne referências e ferramentas para acompanhar vulnerabilidades em Rails, checar gems do projeto com Bundler Audit e usar Rack::Attack para limitar abuso e força-bruta.'
tags: ["seguranca", "ruby-on-rails", "bundler-audit", "rack-attack"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Segurança em Rails | AkitaOnRails.com"
    url: "http://www.akitaonrails.com/2014/05/22/seguranca-em-rails"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2016-04/akitaonrails-com--seguranca-em-rails.md"
    kind: repo
---

O texto reúne referências e ferramentas úteis para quem quer acompanhar segurança em Ruby on Rails sem tratar o tema como algo fechado. A ideia central é que uma aplicação não pode ser chamada de totalmente segura; no máximo, ela parece não ter vulnerabilidades conhecidas.

## Fichamento

- O post indica o guia oficial de segurança do Rails, o grupo oficial de segurança, o Brakeman e o RubySec como referências iniciais.
- A aplicação só pode ser vista como livre de vulnerabilidades conhecidas, nunca como segura de forma absoluta.
- O Ruby Advisory DB organiza advisories de segurança para gems e pode ser usado em conjunto com o Bundler Audit.
- O Bundler Audit cruza o Gemfile.lock com o banco de advisories para apontar gems vulneráveis.
- O texto mostra o uso de `bundle-audit`, a leitura da saída com versões afetadas e a necessidade de atualizar gems com `bundle update`.
- O autor alerta para o cuidado com dependências apontadas direto para repositórios do GitHub, porque isso dificulta a checagem de vulnerabilidades conhecidas.
- O `bundle-audit update` serve para atualizar o banco de advisories antes de um novo scan.
- Como complemento, o texto apresenta o Rack::Attack para lidar com scrapers, ataques de força-bruta e listas de permissões ou bloqueios de IP.
- O Rack::Attack pode ser instalado pela Gemfile, habilitado no `config.ru` e personalizado com um initializer.
- A documentação do Rack::Attack é comparada ao fail2ban pela forma como lida com padrões de invasão.
