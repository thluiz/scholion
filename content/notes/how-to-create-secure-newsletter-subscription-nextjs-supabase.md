---
title: "How to Create a Secure Newsletter Subscription with NextJS, Supabase, Nodemailer and Arcjet 🔐💯"
date: '2026-09-25T00:33:15+01:00'
category: webclip
summary: 'Tutorial mostra como montar um formulário de newsletter com NextJS, Supabase, Nodemailer e Arcjet, usando double opt-in, validação de e-mail, rate limiting e proteção contra bots.'
tags: ["nextjs", "supabase", "arcjet", "nodemailer"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "How to Create a Secure Newsletter Subscription with NextJS, Supabase, Nodemailer and Arcjet 🔐💯"
    url: "https://dev.to/madza/how-to-create-a-secure-newsletter-subscription-with-nextjs-supabase-nodemailer-and-arcjet-3ll7?context=digest"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/dev-to--how-to-create-secure-newsletter-subscription-nextjs-supabase.md"
    kind: repo
---

The guide explains how to build a custom newsletter subscription app from scratch with NextJS, Supabase, Nodemailer, and Arcjet. It focuses on solving spam sign-ups, poor email validation, bot traffic, and other common issues through server-side checks and a double opt-in flow.

It also walks through the app structure, the UI states for landing, pending, error, and confirmation, and the backend routes for submission and confirmation. The setup uses Arcjet for protection rules, Supabase for subscriber storage, and Nodemailer for sending confirmation emails.

## Fichamento

- A newsletter pode ajudar a engajar público, gerar tráfego e construir uma comunidade fiel em torno de uma marca.
- Soluções gratuitas tendem a sofrer com cadastros de spam, validação ruim de e-mail e proteção insuficiente contra bots.
- O tutorial propõe criar um app de inscrição do zero e tratar esses problemas com medidas de segurança e validação.
- A stack inclui interface e API em NextJS, backend em Supabase, envio de confirmação com Nodemailer e proteção com Arcjet.
- O app final usa double opt-in para confirmar a inscrição por e-mail.
- O texto apresenta o Arcjet como uma solução de segurança integrada como dependência, sem exigir agentes ou infraestrutura complexa.
- O Arcjet é usado para validação de formato de e-mail, rate limiting, detecção de bots e proteção contra ataques web comuns.
- A interface é dividida em quatro estados: landing, pending, error e confirmation.
- No estado inicial, há um campo de e-mail e um botão de envio.
- No estado pending, o usuário recebe a indicação de que o processo está em andamento e deve verificar o e-mail.
- No estado de erro, a interface mostra que a inscrição falhou.
- No estado de confirmação, a mensagem informa que o e-mail foi registrado.
- O projeto NextJS é criado com `create-next-app`, e o servidor de desenvolvimento é iniciado com `npm run dev`.
- O tutorial pede cinco ícones, incluindo imagens para os estados da newsletter e um GIF para carregamento.
- O arquivo de configuração do Arcjet usa regras de shield, bot detection, fixed window de 3 requisições em 2 minutos e validação de e-mail.
- As regras do Arcjet são configuradas em modo `LIVE`, com opção `DRY_RUN` para testes ou depuração.
- O Nodemailer é configurado com variáveis SMTP e um endereço `BASE_URL`.
- A função de envio monta o e-mail de confirmação com um link para `/api/confirm?token=...`.
- No Supabase, o texto cria a tabela `pending_subscriptions` com `token`, `email` e `link_sent_at`.
- Também cria a tabela `subscribers` com `email` e `confirmed_at`.
- O cliente do Supabase é inicializado com URL e chave do projeto vindas do arquivo de ambiente.
- A rota `/api/submit` trata requisições GET e POST, aplica proteção do Arcjet e retorna erros para suspeita, bot, rate limit e problemas de e-mail.
- Antes de inserir um novo cadastro, o servidor verifica se o e-mail já existe na tabela `subscribers`.
- Se o e-mail ainda não existir, a aplicação gera um UUID, insere o dado em `pending_subscriptions` e envia o e-mail de opt-in.
- A rota `/api/confirm` lê o token da query string, procura o registro em `pending_subscriptions`, insere o e-mail em `subscribers` e remove o registro pendente.
- A página principal usa estado no cliente para alternar entre carregamento, envio, erro e confirmação, além de ler o parâmetro `approved` na URL.
- O formulário envia o e-mail por `fetch` para `/api/submit` e atualiza a mensagem conforme a resposta.
- O texto mostra testes para proteção contra ataque, detecção de bot, validação de e-mail, limitação de requisições, checagem de duplicidade e fluxo completo de confirmação.
