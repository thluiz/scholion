---
title: "Criteria Hibernate na prática"
date: '2012-04-03T10:15:28-03:00'
category: webclip
summary: 'O texto apresenta uma introdução ao Criteria API do Hibernate, mostrando criação de consultas em Java, uso de restrictions, tratamento de null, like e ilike, e correspondência por MatchMode.'
tags: ["hibernate", "criteria-api", "java", "restrictions"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Criteria Hibernate na prática"
    url: "https://imasters.com.br/back-end/criteria-hibernate-na-pratica"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2012-04/imasters-com-br--criteria-hibernate-na-pratica.md"
    kind: repo
---

O texto introduz o Criteria API como uma forma programática de montar consultas em Java, com checagem em tempo de compilação. Também mostra que o método createCriteria() da Session retorna um Criteria para acessar a persistência da classe.

## Fichamento

- O Criteria API permite construir expressões de consulta em Java, com checagem em tempo de compilação, ao contrário de HQL ou SQL.
- O método createCriteria() pertence à Session e retorna um Criteria para trabalhar com a classe persistida.
- Para listar todas as propriedades de uma classe, o exemplo usa session.createCriteria(Produto.class) e depois list().
- O método add() serve para incluir restrições no Criteria.
- A classe Restrictions, do pacote org.hibernate.Criterion, reúne métodos estáticos para as condições de restrição.
- Os métodos eq e ne não devem ser usados para propriedades com valor null; nesses casos, o texto indica isNull() e isNotNull().
- Os métodos like() e ilike() servem para buscas parciais, e ilike() é case-insensitive.
- O texto explica que é possível buscar no início, no fim ou em qualquer parte da string.
- O símbolo % indica busca por partes da string.
- O MatchMode tem quatro tipos: anywhere, end, exact e start.
