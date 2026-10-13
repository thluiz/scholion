---
title: "Primeiros passos com Passport e Express em Node.js"
date: '2013-08-22T08:51:09-03:00'
category: webclip
summary: 'O texto apresenta Passport como middleware de autenticação modular para Node.js e mostra como integrar login com Twitter em uma aplicação Express, usando OAuth, sessões e rotas protegidas.'
tags: ["passport", "express", "oauth", "twitter"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Primeiros passos com Passport e Express em Node.js - NodeBR - NodeJS Brasil"
    url: "http://nodebr.com/primeiros-passos-com-passport-e-express-em-node-js/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2013-08/nodebr-com--primeiros-passos-com-passport-e-express-em-node-js.md"
    kind: repo
---

O texto explica que o Passport é um middleware para autenticação em Node.js com arquitetura modular, em que cada estratégia fica separada. No exemplo, a aplicação Express recebe suporte para login com Twitter, usando OAuth, rotas de autenticação e proteção de páginas para usuários já logados.

## Fichamento

- Passport é apresentado como um middleware para implementar autenticação em Node.js de forma rápida e com estratégias separadas
- O exemplo usa uma aplicação Express simples e adiciona dependências para Passport, Twitter, login protegido e sessão
- A implementação pede três passos: configurar sessão, configurar estratégias de autenticação e adicionar rotas de autenticação
- A rota `/account` usa `ensureLoggedIn('/login')` para impedir acesso sem login e exibir dados da conta
- A rota `/login` mostra um link para iniciar o login com Twitter
- A configuração do Twitter exige `consumerKey`, `consumerSecret` e `callbackURL`, obtidos ao registrar a aplicação no Twitter
- O callback de verificação recebe `token`, `tokenSecret` e `profile`, e retorna o usuário para `req.user`
- O texto diz que, em aplicações reais, a conta do Twitter costuma ser associada a um registro de usuário no banco de dados
- As rotas `/auth/twitter` e `/auth/twitter/callback` iniciam e concluem o fluxo OAuth com redirecionamentos
- Para manter o usuário autenticado, a aplicação usa `cookieParser`, `session`, `passport.initialize()` e `passport.session()`
- `serializeUser` e `deserializeUser` controlam o que é guardado na sessão e como o usuário é recuperado
- O exemplo serializa o registro inteiro do usuário, embora o texto diga que seria possível guardar só o ID
- Ao final, o artigo mostra como rodar a aplicação com `node app.js` e acessar `http://localhost:3000`
