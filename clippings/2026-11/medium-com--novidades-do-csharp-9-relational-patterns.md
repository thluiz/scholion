---
url: "https://medium.com/@renato.groffe/novidades-do-c-9-relational-patterns-3903d20e2727"
captured_at: "2026-11-16T06:11:48+00:00"
title: "Novidades do C# 9: Relational Patterns | by Renato Groffe | Medium"
domain: "medium-com"
---

Novidades do C# 9: Relational Patterns
Renato Groffe
2 min read
·
May 20, 2020

No início do Build 2020 (terça, 19/05) a Microsoft anunciou o Preview 4 do .NET 5, sendo esta a versão que sucederá o .NET Core 3. Vale destacar que o .NET 5 tem por objetivo unificar toda a plataforma .NET, o que inclui tecnologias como Xamarin e .NET web assembly.

Maiores informações sobre este release (incluindo instalação) podem ser encontrados no post:

Announcing .NET 5 Preview 4 and our journey to one .NET | .NET Blog
NET 5 is the next version and future of .NET. We are continuing the journey of unifying the .NET platform, with a…

devblogs.microsoft.com

Um dos destaques do Preview 4 está no suporte às novas funcionalidades do C# 9. Como já fiz em versões anteriores darei início a uma série cobrindo tais novidades, abordando neste primeiro artigo o uso de Relational Patterns.

Para os testes descritos aqui instalei o Preview 4 do .NET 5, bem como atualizei o Visual Studio 2019 para o Preview 1.0 da versão 16.7.0. Criei então uma nova Console Application, alterando o arquivo .csproj da mesma para que no item LangVersion constasse o valor preview:

Operadores relacionais como <, <=, > e >= poderão ser empregados em conjunto com a cláusula switch, simplificando assim tratamentos por faixas de valores. É o que demonstra a função AnalisarPeso na próxima listagem:

Através de um parâmetro contendo o Índice de Massa Corpórea (IMC) de uma pessoa e de comparações empregando o operador < e _ retornaremos a classificação de peso correspondente;
As definições possíveis foram declaradas no enum ClassificacaoIMC.

A seguir temos o resultado da execução deste projeto:

E concluo este post com um convite…

Dia 14/09/2020 (segunda) a partir das 21:00 - horário de Brasília - teremos uma live no Canal .NET cobrindo estas e outras novidades do C# 9. O evento será ONLINE e GRATUITO, com transmissão pelo YouTube.

Para participar faça sua inscrição no meetup:

https://bit.ly/live-csharp9-canaldotnet

Referências

Proposed changes for Pattern Matching in C# 9.0 — Draft Specification #2850
