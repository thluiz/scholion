---
title: "Dependency Injection made simple"
date: '2026-09-24T23:58:50+01:00'
category: webclip
summary: 'A página explica dependency injection como passar um objeto para o construtor ou setter de uma classe dependente, o que desacopla o código, facilita testes e usa interfaces em linguagens fortemente tipadas.'
tags: ["dependency-injection", "javascript", "csharp", "interfaces"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Dependency Injection made simple."
    url: "https://dev.to/emanuelgustafzon/dependency-injection-made-simple-3d4c?ref=dailydev"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/dev-to--dependency-injection-made-simple.md"
    kind: repo
---

A página define dependency injection como uma forma simples de lidar com objetos que dependem de outros objetos. Primeiro mostra um exemplo acoplado em JavaScript e depois troca a criação direta da conexão por injeção no construtor, para permitir usar conexões diferentes sem alterar a rota.

## Fichamento

- Dependency injection é apresentada como o ato de passar um objeto para o construtor ou setter de uma classe que depende dele.
- O exemplo inicial mostra uma rota de posts que cria diretamente uma DatabaseConnection, o que deixa o código acoplado e pouco flexível.
- A alternativa com SQLiteConnection e MySqlConnection passa a conexão ao construtor de PostsRouter, permitindo trocar a implementação usada.
- O texto diz que essa abordagem desacopla os objetos e facilita o gerenciamento do código.
- Também afirma que dependency injection ajuda nos testes, porque é possível passar um mock object para o post router.
- Em linguagens fortemente tipadas, o texto diz que é preciso definir um tipo para o objeto passado.
- Para isso, a página introduz interfaces como estrutura de tipos sem implementação de métodos ou propriedades.
- No exemplo em C#, as classes SQLiteConnection e MySqlConnection implementam IDb.
- PostsRouter recebe IDb no construtor e usa a conexão por meio da interface.
- O texto encerra com um exemplo completo em C# usando SQLiteConnection e MySqlConnection em dois objetos PostsRouter diferentes.
