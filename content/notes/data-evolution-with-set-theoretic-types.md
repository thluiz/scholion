---
title: "Data evolution with set-theoretic types"
date: '2026-09-24T23:31:16+01:00'
category: webclip
summary: 'O texto propõe usar tipos conjuntistas e revisões em structs para manter compatibilidade ao evoluir dados, preservando segurança de tipo entre versões antigas e novas.'
tags: ["elixir", "types", "structs"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Data evolution with set-theoretic types"
    url: "https://dashbit.co/blog/data-evolution-with-set-theoretic-types"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/dashbit-co--data-evolution-with-set-theoretic-types.md"
    kind: repo
---

The article argues that libraries need a way to evolve public data definitions without forcing breaking changes on every consumer. It uses an Elixir struct example to show how set-theoretic types, structural subtyping, and explicit revisions could let old and new versions of a struct coexist while preserving type safety.

It proposes that the compiler rewrite a generic `Schema.t()` signature into version-aware signatures that preserve the revision of the input. The same idea is extended to multiple fields, transitive dependencies, downcasting, and higher-order functions, with the compiler enforcing that each new revision is a supertype of the previous one.

## Fichamento

- O texto parte de um caso em Rust e C em que um campo que deveria aceitar `null` acabou causando incompatibilidade entre bibliotecas.
- A mudança mais correta seria tornar o campo `name` opcional, mas isso quebraria usuários existentes da biblioteca.
- Converter `null` em string vazia preserva compatibilidade, mas mantém o tipo divergente da especificação.
- O artigo quer mostrar como tipos conjuntistas podem ajudar bibliotecas a evoluir definições públicas de dados sem perder segurança de tipo.
- A discussão toma Elixir como campo de testes para explorar structs, subtipos estruturais e revisões.
- Em tipos nominais, mudar a definição de uma struct altera o tipo associado a todos os valores instanciados com ela.
- Com subtipagem estrutural, o tipo depende dos campos efetivos do valor, então ampliar a definição da struct não altera os dados já instanciados.
- O problema aparece nas funções: uma função que recebia uma struct com `name` como string passa a falhar na tipagem quando o campo passa a aceitar `nil`.
- O texto defende que uma versão nova da struct pode coexistir com a antiga sem tornar inválido o código antigo, porque a presença de `nil` ainda não existe nos valores antigos.
- Para isso, o artigo propõe revisões explícitas nas structs, com a revisão 1 correspondendo aos campos originais e a revisão 2 ampliando tipos.
- `Schema.t()` passa a representar a revisão mais recente, mas o tipo pode ser refinado explicitamente por campo.
- A propriedade central proposta é que uma função preserve a revisão recebida: se entra uma revisão antiga, sai a mesma revisão; se entra uma revisão nova, sai a revisão nova.
- O texto diz que isso pode ser expresso com tipos de interseção, gerando assinaturas diferentes para cada revisão compatível.
- Quando há vários campos revisados, o número de casos a verificar cresce com o número de campos alterados.
- O autor sugere que usuários escolham explicitamente quais revisões aceitam, sendo mais útil para autores de bibliotecas do que para aplicações comuns.
- A configuração de revisões se aplica também a dependências transitivas, permitindo combinações válidas desde que revisões não sejam removidas ao descer na árvore de dependências.
- O texto mostra que é possível fazer downcast de uma revisão nova para uma antiga, seja preenchendo o campo com string vazia, seja falhando em tempo de execução quando o valor não for compatível.
- Na formalização, o compilador gera uma cláusula por revisão, com domínio restrito pelos tipos anteriores e codomínio acumulando as revisões anteriores e atuais.
- O texto também trata de funções de ordem superior e mostra que a semântica resultante preserva a leitura mais segura possível para entradas e saídas.
- As mudanças permitidas em uma revisão são tornar um campo mais amplo, adicionar campo com valor padrão e marcar campo como obsoleto.
- Remover campos, estreitar tipos ou usar tipos disjuntos é tratado como mudança quebradora.
- A conclusão é que revisões poderiam tornar a evolução de dados progressiva e segura para bibliotecas, especialmente no ecossistema Elixir.
