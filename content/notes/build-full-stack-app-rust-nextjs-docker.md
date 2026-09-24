---
title: "Build a full stack app with Rust, Next.js and Docker"
date: '2026-09-25T00:02:36+01:00'
category: webclip
summary: 'The article walks through a simple full stack app built bottom-up with PostgreSQL, a Rust API, Next.js 14, and Docker Compose, then tests CRUD endpoints and the frontend.'
tags: ["rust", "nextjs", "docker", "postgres"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Build a full stack app with Rust, Next.js and Docker"
    url: "https://dev.to/francescoxx/build-a-full-stack-app-with-rust-nextjs-and-docker-436h"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/dev-to--build-full-stack-app-rust-nextjs-docker.md"
    kind: repo
---

The article explains how to build a simple full stack app with Next.js 14, Tailwind CSS, Rust, PostgreSQL, Docker, and Docker Compose. It starts from the database, moves to the Rust backend, and ends with the Next.js frontend.

## Fichamento

- O projeto usa uma abordagem de baixo para cima, começando pelo banco de dados e terminando no frontend.
- O backend é escrito em Rust puro, sem framework, e usa Serde para serialização e desserialização.
- O banco de dados escolhido é PostgreSQL, rodando em container com Docker.
- O Docker Compose reúne frontend, backend e banco no mesmo ambiente.
- O backend expõe endpoints CRUD para usuários, com create, read, update e delete.
- A aplicação Rust cria a tabela `users` se ela ainda não existir.
- O servidor Rust escuta na porta 8080 e responde a requisições TCP simples.
- No frontend, o autor usa Next.js 14 com TypeScript e Tailwind CSS.
- O frontend consome a API com Axios e permite listar, criar, atualizar e excluir usuários.
- O artigo também mostra como empacotar o backend e o frontend com Docker para execução conjunta.
