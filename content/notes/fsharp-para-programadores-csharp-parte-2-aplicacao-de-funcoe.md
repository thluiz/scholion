---
title: "F# para programadores C# – Parte 2 – Aplicação de Funções"
date: '2012-06-15T09:42:55-03:00'
category: webclip
summary: 'O post compara a aplicação de funções em F# com a invocação de métodos em C#, mostra a sintaxe para funções de um e dois argumentos e apresenta funções como valores de primeira classe.'
tags: ["fsharp", "csharp", "funcoes", "programacao-funcional"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "F# para programadores C# – Parte 2 – Aplicação de Funções"
    url: "http://rodrigovidal.net/?p=737"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2012-06/rodrigovidal-net--fsharp-para-programadores-csharp-parte-2-aplicacao-de-funcoe.md"
    kind: repo
---

O post continua a série com a indicação do livro *Programming F#*, de Chris Smith, para quem está começando. Depois compara como F# aplica funções diretamente e como C# invoca métodos em objetos, além de mostrar que F# usa uma sintaxe mais curta para vários argumentos e chamadas aninhadas.

## Fichamento

- O autor recomenda o livro *Programming F#*, de Chris Smith, para quem está começando na linguagem.
- Em F#, o termo usado é aplicação de função, isto é, uma função executada com um conjunto de argumentos.
- Em C#, um método é invocado a partir de um objeto, como em `obj.Foo(x)`.
- Em F#, uma função pode ser aplicada diretamente, como em `foo x`.
- Para dois argumentos, F# usa `foo a b`, enquanto C# usa `obj.Foo(a,b)`.
- F# dispensa parênteses, vírgulas e ponto e vírgula no fim, deixando a sintaxe mais curta.
- Quando o resultado de uma função vira argumento de outra, F# escreve `foo (fee x)` e `foo a (fee b)`.
- Em F#, parênteses mudam a prioridade de execução, como em Haskell.
- O post mostra definições em F# para `add`, `inc`, `double` e `quadruple` num script `.fsx`.
- No Visual Studio, o script pode rodar no console interativo com Alt+Enter.
- No REPL de linha de comando, o autor orienta adicionar o caminho do F# SDK às variáveis de ambiente do Windows e digitar `fsi`.
- A versão em C# usa `Func<int, int, int>` e `Func<int, int>` para funções equivalentes.
- O autor diz que F# trata funções como membros de primeira classe e infere tipos de função com mais facilidade.
- O post encerra dizendo que C# trata a função como um objeto `Func` e que a inferência não funciona tão bem nesse caso.
