---
title: "Chain of Responsibility Design Pattern in C#"
date: '2026-09-24T23:17:17+01:00'
category: webclip
summary: 'O artigo explica o padrão Chain of Responsibility em C#, mostra o caso de middleware no ASP.NET Core e refatora um fluxo de empréstimo de livros em handlers encadeados.'
tags: ["chain-of-responsibility", "csharp", "design-patterns", "aspnet-core"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Chain of Responsibility Design Pattern in C# - Code Maze"
    url: "https://code-maze.com/csharp-chain-of-responsibility-design-pattern/?ref=dailydev"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/code-maze-com--chain-of-responsibility-design-pattern-in-csharp.md"
    kind: repo
---

The article presents Chain of Responsibility as a behavioral pattern for splitting a complex task into independent handlers linked in sequence. It uses ASP.NET Core middleware and a library rental request as the main examples, then shows how to move from a monolithic service to separate handler classes.

## Fichamento

- O padrão passa uma requisição por uma cadeia de handlers, e cada handler decide se processa a requisição ou se a encaminha ao próximo.
- Ele é apresentado como útil para quebrar lógica em partes menores, cada uma com responsabilidade própria, o que favorece baixo acoplamento e o Single Responsibility Principle.
- O texto aponta o middleware do ASP.NET Core como exemplo direto desse padrão, porque múltiplos handlers podem tratar a mesma requisição de forma independente.
- Na descrição geral, a cadeia é formada pelo cliente, que organiza os handlers em sequência e inicia a execução no primeiro deles.
- O artigo distingue um fluxo com vários handlers, em que a requisição pode avançar por várias etapas, de um fluxo com um único handler efetivo, em que a cadeia só segue até encontrar o handler adequado.
- No exemplo da biblioteca, um `RentalAssistService` monolítico reúne verificação de disponibilidade do livro, elegibilidade do membro, saldo e emissão, o que deixa a classe acoplada e difícil de evoluir.
- A refatoração proposta transforma cada etapa em um handler independente e liga esses handlers com um método `SetNext()` que armazena a referência para o próximo.
- O código exemplo mostra um `BookAvailabilityCheckHandler` que valida a disponibilidade do livro e, se houver próximo handler, encaminha a requisição adiante.
- O fluxo completo monta a cadeia com verificação de disponibilidade, verificação de acesso do membro, verificação de saldo e emissão do livro.
- O artigo destaca que o cliente passa a cuidar só da ordem dos handlers e da chamada inicial de `Handle()`.
- Um uso implícito do padrão é montar uma cadeia menor para apenas avaliar a requisição, sem chegar à etapa de emissão do livro.
- Entre os problemas, o texto cita a necessidade de definir bem a ordem dos handlers, porque uma etapa de validação colocada depois de um processamento pode deixar uma requisição inválida avançar.
- Também aponta que a troca de estados entre handlers pode aumentar a complexidade e gerar acoplamento entre etapas.
- Outro risco é que a requisição pode não ser tratada por nenhum handler, caso todos apenas encaminhem a execução.
