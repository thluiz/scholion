---
title: "Novidades do C# 9: Relational Patterns"
date: '2020-07-05T14:10:46+00:00'
category: webclip
summary: 'O texto apresenta os Relational Patterns do C# 9 e mostra como usar operadores relacionais no switch para tratar faixas de valores, com um exemplo de classificação de IMC.'
tags: ["csharp-9", "relational-patterns", "pattern-matching", "dotnet-5"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Novidades do C# 9: Relational Patterns | by Renato Groffe | Medium"
    url: "https://medium.com/@renato.groffe/novidades-do-c-9-relational-patterns-3903d20e2727"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/medium-com--novidades-do-csharp-9-relational-patterns.md"
    kind: repo
---

O texto introduz o suporte do C# 9 a Relational Patterns como uma das novidades ligadas ao Preview 4 do .NET 5. O foco é mostrar como operadores relacionais podem ser usados com switch para simplificar decisões por faixas de valores.

## Fichamento

- A Microsoft anunciou o Preview 4 do .NET 5 no início do Build 2020, como a versão que sucederá o .NET Core 3.
- O .NET 5 tem como objetivo unificar a plataforma .NET, incluindo Xamarin e .NET web assembly.
- O Preview 4 traz suporte às novas funcionalidades do C# 9.
- O artigo inicia uma série sobre essas novidades e, neste primeiro texto, trata dos Relational Patterns.
- Para os testes, o autor instalou o Preview 4 do .NET 5 e atualizou o Visual Studio 2019 para a versão 16.7.0 Preview 1.0.
- O projeto foi criado como Console Application e recebeu LangVersion com valor preview no arquivo .csproj.
- Operadores relacionais como <, <=, > e >= podem ser usados com switch para simplificar tratamentos por faixas de valores.
- A função AnalisarPeso usa um parâmetro com o Índice de Massa Corpórea para retornar a classificação de peso correspondente.
- As classificações possíveis foram declaradas no enum ClassificacaoIMC.
- O texto encerra com um convite para uma live no Canal .NET sobre essas e outras novidades do C# 9, com inscrição pelo meetup.
