---
title: "NodeJS + Restify + PassportJS + Facebook + Bearer"
date: '2016-08-29T18:55:35-03:00'
category: webclip
summary: 'O texto apresenta um fluxo de autenticação para API REST com Restify e PassportJS sem sessões, usando Facebook OAuth para validar o usuário localmente e devolver um JWT para as requisições seguintes.'
tags: ["nodejs", "restify", "passportjs", "jwt"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "NodeJS + Restify + PassportJS + Facebook + Bearer"
    url: "http://douglaspicolotto.com/2016/05/01/passportjs-facebook-oauth-bearer/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2016-08/douglaspicolotto-com--nodejs-restify-passportjs-facebook-bearer.md"
    kind: repo
---

O texto descreve uma forma de montar autenticação para uma API REST com Restify e PassportJS sem sessões. A solução combina Facebook OAuth com bearer token, usa Mongoose para persistir dados do usuário e devolve um JWT depois do login no Facebook para autenticar as próximas requisições.

## Fichamento

- O autor diz que quer implementar autenticação com Facebook OAuth e bearer token em uma API REST usando Restify e PassportJS, sem usar sessões.
- A configuração inclui Mongoose com um model de usuário para guardar informações localmente.
- O Passport é inicializado no pipeline do servidor Restify com o método initialize.
- A strategy do Facebook usa OAuth 2.0, recebe um profile depois da validação do usuário, verifica o id do Facebook e cria um novo usuário local quando necessário.
- A strategy bearer lê um JWT, extrai dele o id local salvo e verifica se o usuário existe.
- A API define rotas para login com Facebook, callback do Facebook e um endpoint protegido /api/users/me autenticado com bearer strategy.
- No callback do Facebook, um JWT é gerado com validade de 30 dias e devolvido na resposta.
- O login com Facebook serve só para confirmar que o usuário existe localmente, enquanto as requisições seguintes usam o JWT para autenticação na API.
- O autor conclui que essa abordagem permite usar várias strategies sem sessões no Passport e facilita adicionar outros provedores de autenticação.
