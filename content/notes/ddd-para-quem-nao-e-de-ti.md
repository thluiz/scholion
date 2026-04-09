---
title: "DDD para quem não é de TI"
date: 2026-04-09T16:02:31+01:00
summary: "Domain-Driven Design parte de uma premissa: software bom nasce quando programadores e especialistas do negócio falam a mesma língua."
tags: ["ddd", "software", "modelagem"]
has_commentary: true
sources:
  - title: "Domain Modeling Made Functional"
    author: "Scott Wlaschin"
    year: 2018
    publisher: "Pragmatic Bookshelf"
    kind: book
---

Domain-Driven Design (DDD) é uma abordagem de construção de software criada por Eric Evans em 2003. A premissa: o maior problema de um projeto de software não é a tecnologia — é a comunicação entre quem entende o problema e quem escreve o código.

## A língua comum

Um sistema para clínica veterinária. O veterinário fala em "consulta", "retorno", "vacina polivalente". O programador fala em "registro", "entidade", "tabela". DDD diz: parem de traduzir. O código deve usar as mesmas palavras que o veterinário usa. Se ele diz "agendar um retorno", o código tem uma função chamada `agendarRetorno` — não `criarRegistroTipo2`.

Evans chama isso de **Linguagem Ubíqua**: um vocabulário que aparece nas conversas, nos documentos e no código. Uma língua só.

## Contextos delimitados

Num hospital, "paciente" significa uma coisa para a recepção (nome, convênio, CPF) e outra para o laboratório (amostra, exame, resultado). DDD não força uma definição única — aceita a ambiguidade. Cada área do negócio tem seu **contexto delimitado**, um perímetro onde as palavras têm significado preciso. Entre perímetros, tradução explícita.

## O que Wlaschin acrescenta

Em *Domain Modeling Made Functional*, Scott Wlaschin pega o DDD e mostra que tipos de dados bem escolhidos fazem o compilador trabalhar a favor do modelo. Se o código compila, o modelo está correto. Três lições que ficam:

- **Tornar estados ilegais irrepresentáveis.** Se um pedido aceita de 1 a 99 itens, o tipo não aceita zero nem cem. Não é validação posterior — é design.
- **Workflows como pipelines.** Um processo de negócio vira uma sequência de transformações: entrada → validação → decisão → saída. Cada passo é uma função pura, testável sozinha.
- **Erros são dados, não exceções.** O resultado de cada passo carrega a possibilidade de falha. Quem chama decide o que fazer com ela.
