---
title: "How to handle external dependencies of your domain in a command-event architecture"
date: '2026-09-25T09:07:11+01:00'
category: webclip
summary: 'O artigo compara cinco formas de lidar com dependências externas num domínio de command-event architecture, da injeção clássica ao reader monad, e conclui a favor de comandos internos com dependências explícitas.'
tags: ["command-event-architecture", "dependency-injection", "fsharp", "reader-monad"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "How to handle external dependencies of your domain in a command-event architecture"
    url: "https://hardt.software/how-to-handle-external-dependencies-of-your-domain-in-a-command-event-architecture/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/hardt-software--how-to-handle-external-dependencies-of-your-domain-in-a-comm.md"
    kind: repo
---

The article walks through several ways to handle external data needed by a domain in a command-event architecture. It compares classic OOP dependency injection, a more idiomatic F# function-based approach, dependency records, a pure execute function fed by the service layer, internal and external commands, and a reader monad on the service level.

Its main point is that the best fit, for the author, is to keep the domain execute function pure and move the needed data into internal commands instead of one growing dependency record. The reader monad is presented as interesting, but not clearly better for this example.

## Fichamento

- O artigo trata de como gerir dependências externas e dados adicionais num domínio de command-event architecture.
- O autor avisa que o foco não é modelar melhor o domínio, mas lidar com a gestão das dependências.
- No exemplo, uma invoice precisa de customer e product data para ser criada e enriquecida com linhas.
- O modelo guarda name, address, price e quantity dentro dos eventos e do estado da invoice.
- Na abordagem clássica OOP, o aggregate root recebe repositórios no construtor e chama esses repositórios nos métodos de comando.
- Essa abordagem é direta, mas exige mais boilerplate e testes mais pesados com mocks.
- Na abordagem mais idiomática em F#, a lógica vira funções execute, apply e applyEvents.
- Nessa versão, as funções de acesso a dados entram como parâmetros e depois são parcialmente aplicadas no service.
- O autor diz que isso continua a espalhar dependências pelos parâmetros e não melhora muito os testes.
- Numa tentativa de esconder dependências, ele agrupa funções de acesso num registro Dependencies.
- Essa versão reduz a lista de parâmetros, mas desloca o problema para o crescimento do próprio registro.
- Depois, o artigo torna o execute puro ao mover as chamadas externas para o service e deixar nele apenas dados já carregados.
- Nesse cenário, o service monta um registro de dependências com customer ou product e chama o execute puro.
- O autor observa que isso melhora a testabilidade, mas ainda centraliza demais as dependências num único registro.
- Na última abordagem antes do reader monad, ele separa ExternalCommand e Command internos.
- Os comandos internos carregam customer ou product opcionais no payload, e cada comando passa a levar suas próprias dependências.
- O autor prefere essa solução por dar mais clareza e separar melhor responsabilidades.
- Na versão com reader monad, ele cria uma interface única IDependencies e encapsula a injeção no computation expression dependency.
- Mesmo assim, para este exemplo, ele não vê vantagem clara sobre passar a interface diretamente ao executeCommand.
- Ele conclui que o reader monad pode fazer mais sentido quando a aplicação crescer e houver mais dependências para esconder.
