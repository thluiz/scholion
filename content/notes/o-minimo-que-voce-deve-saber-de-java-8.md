---
title: "O mínimo que você deve saber de Java 8"
date: '2014-03-19T15:17:53-03:00'
category: webclip
summary: 'Java 8 traz default methods, lambdas, method references e Streams, encurtando código com coleções e permitindo operações como filter, map, reduce e collect.'
tags: ["java8", "lambda", "stream", "method-reference"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "O mínimo que você deve saber de Java 8 | blog.caelum.com.br"
    url: "http://blog.caelum.com.br/o-minimo-que-voce-deve-saber-de-java-8/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2014-03/blog-caelum-com-br--o-minimo-que-voce-deve-saber-de-java-8.md"
    kind: repo
---

Java 8 é apresentado como uma versão centrada em três pontos: default methods em interfaces, expressões lambda e a API de Streams. O texto mostra como essas mudanças deixam mais curto o uso de coleções e permitem evoluir interfaces sem quebrar implementações já existentes.

## Fichamento

- `List.sort` pode ser chamada diretamente porque interfaces passaram a poder definir métodos concretos com `default`.
- Default methods permitem adicionar comportamento sem quebrar compatibilidade; o texto cita `Collection.removeIf`, `Map.getOrDefault` e `Comparator.reversed`.
- Lambdas substituem classes anônimas quando o alvo é uma interface funcional, com apenas um método abstrato.
- Um lambda pode ser escrito com ou sem chaves e `return` quando tem só uma expressão.
- O mesmo lambda pode ser passado diretamente para `Thread`, porque o construtor espera uma interface funcional.
- `forEach` recebe um `Consumer`, e o texto mostra que um lambda com um argumento pode dispensar parênteses.
- `Comparator.comparing` recebe uma função, e `String::length` aparece como referência de método equivalente a `s -> s.length()`.
- `filter`, `map` e `reduce` entram como operações de Stream, e não como métodos de Collection.
- `Collection.stream()` cria um Stream a partir de uma coleção.
- `filter` é usado para manter apenas strings com menos de seis caracteres, e `forEach(System.out::println)` imprime o resultado.
- `map` é mostrado transformando strings em seus tamanhos.
- `IntStream`, `LongStream` e `DoubleStream` aparecem para evitar boxing em tipos primitivos.
- `Comparator.comparingInt` é mostrado como outra forma de evitar boxing ao ordenar pelo tamanho da string.
- `average()` retorna um `OptionalDouble`, e `orElse(0)` é usado para exibir um valor padrão.
- `collect(Collectors.toList())` converte o Stream filtrado de volta para `List`.
- O texto também menciona recursos deixados de fora do artigo, como anotações repetidas, `java.time`, melhora na inferência de generics e ajustes no operador diamante.
