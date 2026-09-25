---
title: "Why is F# code so robust and reliable?"
date: '2026-09-25T07:58:14+01:00'
category: webclip
summary: 'The post argues that F# reduces bugs through immutability, exhaustive matching, no nulls by default, explicit errors, typed primitives, and explicit dependencies in functional code.'
tags: ["fsharp", "robustez-de-codigo", "programacao-funcional", "dotnet"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Why is F# code so robust and reliable?"
    url: "https://devblogs.microsoft.com/dotnet/why-is-fsharp-code-so-robust-and-reliable/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/devblogs-microsoft-com--why-is-fsharp-code-so-robust-and-reliable.md"
    kind: repo
---

The post says Access Softek used F# for EasyCoin after years of bugs in C# and .NET work. It attributes the low bug count in production to language features that make state, errors, dependencies, and concurrency more explicit.

## Fichamento

- Valores e records são imutáveis por padrão, o que ajuda na previsibilidade do código e na segurança em concorrência.
- Discriminated unions com `match` exaustivo fazem o compilador avisar quando um caso ainda não foi tratado.
- O uso de `null` não é o padrão; valores ausentes são tratados com `Option<'T>`, o que obriga a lidar explicitamente com `Some` e `None`.
- Erros na lógica de negócio devem ser tratados com `Result<'T>` ou com DUs específicas, em vez de exceções customizadas no meio da transação.
- Em F#, variáveis, funções, tipos e arquivos só podem depender do que foi definido antes, o que evita dependências circulares e deixa claro o que depende do quê.
- O compilador avisa sobre resultados de expressões não usados, o que chama atenção para casos que poderiam passar despercebidos.
- Primitivos tipados com units of measure ajudam a distinguir tipos parecidos, como IDs diferentes, sem custo em runtime.
- Conversões implícitas não são aceitas; conversões explícitas reduzem erros de tipo e problemas em interpolação de strings.
- A concorrência pode ser modelada com atores e mensagens, usando `MailboxProcessor<'Msg>` ou Channels.
- A injeção de dependência é feita por argumentos explícitos, o que permite verificação em tempo de compilação e facilita testes.
- O texto também menciona SQL, HTML, IaC e parâmetros de rota tipados, além de transpilers do projeto Fable para JavaScript e Python.
