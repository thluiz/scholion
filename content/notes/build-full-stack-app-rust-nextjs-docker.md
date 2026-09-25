---
title: "Build a full stack app with Rust, Next.js and Docker"
date: '2026-09-25T00:02:36+01:00'
category: webclip
summary: 'The article walks through a simple full stack app built bottom-up with PostgreSQL, a Rust API, Next.js 14, and Docker Compose, then tests CRUD endpoints and the frontend.'
tags: ["rust","nextjs","docker","postgres"]
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

## Reading notes

- The project uses a bottom-up approach, starting with the database and ending with the frontend.
- The backend is written in pure Rust, without a framework, and uses Serde for serialization and deserialization.
- The chosen database is PostgreSQL, running in a container with Docker.
- Docker Compose brings together frontend, backend, and database in the same environment.
- The backend exposes CRUD endpoints for users, with create, read, update, and delete.
- The Rust application creates the `users` table if it does not already exist.
- The Rust server listens on port 8080 and responds to simple TCP requests.
- On the frontend, the author uses Next.js 14 with TypeScript and Tailwind CSS.
- The frontend consumes the API with Axios and allows listing, creating, updating, and deleting users.
- The article also shows how to package the backend and frontend with Docker for joint execution.
