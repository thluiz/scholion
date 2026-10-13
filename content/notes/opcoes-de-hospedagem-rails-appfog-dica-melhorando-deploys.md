---
title: "Opções de hospedagem Rails: AppFog (#dica melhorando deploys)"
date: '2013-05-13T15:25:26-03:00'
category: webclip
summary: 'A página explica como lidar com deploys Rails no AppFog: precompilar assets localmente, ajustar o desenvolvimento para não usar public/assets, e contornar problemas de compilação da libv8 no staging.'
tags: ["rails", "appfog", "deploy", "asset-pipeline"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "AkitaOnRails.com - Opções de hospedagem Rails: AppFog (#dica melhorando deploys)"
    url: "http://www.akitaonrails.com/2013/05/04/opcoes-de-hospedagem-rails-appfog-dica-melhorando-deploys#.UZEq-LWG0rU"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2013-05/akitaonrails-com--opcoes-de-hospedagem-rails-appfog-dica-melhorando-deploys.md"
    kind: repo
---

O texto descreve uma forma de fazer deploy de uma aplicação Rails no AppFog sem depender da compilação de assets no servidor. A orientação principal é precompilar os assets localmente, usar turbo-sprockets para acelerar o processo e ajustar o ambiente de desenvolvimento para continuar compilando os assets dinamicamente sem interferência da pasta public/assets.

## Fichamento

- O AppFog usa af update em vez de git push, e isso leva a um upload dos arquivos do projeto.
- Como o AppFog não lida bem com assets:precompile, a solução recomendada é precompilar localmente antes do deploy.
- Para não quebrar o desenvolvimento local depois da precompilação, o texto sugere mudar config.assets.prefix para /assets_dev em development.rb.
- Com esse ajuste, o Rails ignora public/assets em desenvolvimento e volta a compilar a partir de app/assets.
- O texto aponta um problema grave no deploy ligado à gem libv8, que falha ao compilar nos servidores da AppFog.
- A libv8 entra no processo por causa do Asset Pipeline e de dependências como less e Twitter Bootstrap.
- A explicação dada é que o AppFog tenta instalar gems do grupo assets durante o staging e esbarra na compilação da libv8.
- Para contornar isso, o texto recomenda usar uma versão ímpar da libv8 no Gemfile.lock, porque essa versão já traz binários.
- Também diz que pode ser preciso incluir as gems do grupo assets na production dentro da Gemfile.
- O arquivo production.rb deve ter config.serve_static_assets = true.
- Antes do deploy, o procedimento indicado é rodar rake assets:precompile bundle package.
- Mesmo quando o comando af update termina com erro, o texto relata que a aplicação pode subir se a fase de Staging tiver concluído.
- A conclusão é que o processo de deployment da AppFog ainda precisa melhorar bastante.
