---
title: "Arquitetura Hexagonal não é sobre pastas"
date: 2026-04-09T18:27:03+01:00
summary: "Ports and Adapters, Onion, Clean Architecture. Três nomes para a mesma ideia: o domínio não depende de infraestrutura."
tags: ["arquitetura", "software", "hexagonal"]
has_commentary: true
sources:
  - title: "Hexagonal Architecture"
    author: "Alistair Cockburn"
    year: 2005
    kind: article
  - title: "The Onion Architecture"
    author: "Jeffrey Palermo"
    year: 2008
    kind: article
  - title: "Clean Architecture"
    author: "Robert C. Martin"
    year: 2017
    publisher: "Prentice Hall"
    kind: book
---

Ports and Adapters (Cockburn, 2005), Onion Architecture (Palermo, 2008), Clean Architecture (Martin, 2017). Três nomes, mesma regra: **dependências apontam para dentro**. O domínio não conhece banco, não conhece HTTP, não conhece framework.

## O que significa "apontar para dentro"

Uma classe de domínio nunca faz `import` de nada que viva fora do domínio. Não referencia `DbContext`, não recebe `HttpRequest`, não herda de `ControllerBase`. Se precisa persistir, define uma interface (port). Quem implementa essa interface (adapter) vive na camada de fora.

O domínio dita o contrato. A infraestrutura obedece.

## Port não é Repository

Port é qualquer fronteira entre domínio e mundo externo. Repository é um caso particular. Enviar email é port. Consultar API de terceiro é port. Gerar PDF é port. Publicar evento é port.

Projetos que só têm `IRepository<T>` como port estão usando a arquitetura pela metade. O domínio continua acoplado a tudo que não passa por repositório.

## O teste revela o acoplamento

Se para testar uma regra de negócio você precisa subir banco, configurar container ou mockar HTTP, o domínio está acoplado à infraestrutura. O teste de domínio deveria rodar com mocks simples das ports. Se não roda, a fronteira está furada.

## Adapter não é camada

Adapter é plugin. Banco de dados é um adapter. API REST é outro. CLI é outro. Fila de mensagens é outro. Todos plugam nas mesmas ports. Trocar Postgres por DynamoDB é trocar um adapter, não reescrever o sistema.

Na prática quase ninguém troca banco. O valor real é outro: testar sem infraestrutura e manter o domínio legível sem ruído de framework.

## O erro das pastas

Criar `Application/`, `Domain/`, `Infrastructure/`, `Presentation/` e achar que implementou a arquitetura. As pastas existem, as dependências vão em qualquer direção. `Domain/` referencia `Infrastructure/` direto. O compilador não reclama (em linguagens sem enforcement de módulo), o code review não pega, e a arquitetura vira ficção.

Se a regra de dependência não é verificável por tooling ou teste, ela vai ser violada.

## Quando não usar

Aplicações simples, scripts, protótipos, CRUDs sem regra de negócio. A indireção das ports e adapters tem custo em boilerplate e navegação de código. Se o domínio cabe em um arquivo, a indireção atrapalha mais do que ajuda.
