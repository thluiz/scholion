---
title: "Estrutura de diretórios e arquivos em projetos Node.js"
date: '2016-10-27T10:25:38-03:00'
category: webclip
summary: 'O texto reúne padrões comuns para organizar projetos Node.js, separando src, root, execução, testes e áreas por responsabilidade ou funcionalidade para manter legibilidade e escalabilidade.'
tags: ["node-js", "arquitetura-de-projeto", "estrutura-de-diretorios"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Estrutura de diretórios e arquivos em projetos Node.js - Waldemar Neto Blog"
    url: "http://walde.co/2016/10/24/estrutura-de-diretorios-e-arquivos-em-projetos-node-js/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2016-10/walde-co--estrutura-de-diretorios-e-arquivos-em-projetos-node-js.md"
    kind: repo
---

O texto defende que a organização de um projeto Node.js deve equilibrar liberdade e clareza. Ele sugere isolar o código da aplicação em `src`, manter no root o que é usado na execução e nos testes, e separar server e app para distinguir inicialização de aplicação.

## Fichamento

- A liberdade do Node.js para estruturar código pode gerar confusão, então vale aproveitar padrões comuns para manter o projeto extensível e legível.
- Colocar o código da aplicação em `src` ajuda a limpar o root e evita misturar código, testes e arquivos de configuração.
- O root pode guardar testes, scripts, arquivos de ambiente, conteúdo público e arquivos ligados à execução da aplicação.
- `server.js` pode ficar no root para chamar `app.js` e inicializar a aplicação, separando execução de aplicação.
- Dentro de `src`, é comum organizar por controllers, routes, models e middlewares para deixar as responsabilidades mais claras.
- Em alguns casos, o `src` pode ser dividido por cliente, como `mobile` e `web`, quando houver APIs diferentes.
- Quando backend e front-end estão no mesmo repositório, uma divisão em `server` e `client` facilita a manutenção e permite testes conjuntos no root.
- Outra forma comum é separar por funcionalidade, com pastas como `products` e `orders`, reunindo controller, model e routes de cada domínio.
- Ao nomear arquivos dentro de pastas de responsabilidade, o texto sugere evitar sufixos repetidos e usar o nome do módulo na importação para manter a leitura simples.
