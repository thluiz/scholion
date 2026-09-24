---
title: "This Is Why We Don't Test Private Methods"
date: '2026-09-24T23:52:57+01:00'
category: webclip
summary: 'The post argues that private methods should be tested indirectly through public behavior, because direct tests break encapsulation and expose internals that other code should not use.'
tags: ["unit-testing", "encapsulation", "private-methods", "csharp"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "This Is Why We Don't Test Private Methods"
    url: "https://dev.to/canro91/this-is-why-we-dont-test-private-methods-28ef?context=digest"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/dev-to--this-is-why-we-dont-test-private-methods.md"
    kind: repo
---

Trying to test private methods creates confusion, especially for people who are new to unit testing. The post answers that the reason to avoid it is encapsulation. Private methods are only accessible inside the same class, and access modifiers exist to restrict access to a class’s internal state.

Instead of making private methods public just for tests, the post says to test what they affect through public methods. If a private method changes a return value or internal state, create the object with the right data, call the public method, and check the observable result. In the example, `HasAdmin()` should be covered by testing whether a user with certain relations and permissions gets admin-only behavior or a blocked action.

## Fichamento

- Testar métodos privados costuma gerar confusão para quem está começando em unit testing.
- A justificativa para não testá-los diretamente é preservar o encapsulamento.
- Métodos privados só podem ser acessados dentro da mesma classe, e esse é justamente o papel dos modificadores de acesso.
- Não é uma boa ideia tornar métodos privados públicos ou estáticos só para chamá-los em testes.
- Expor internals é apontado como um erro comum ao escrever testes.
- Se um método privado não tiver referências, ele deve ser removido.
- Um método privado na cadeia de chamadas altera algo observável por métodos públicos.
- O teste deve cobrir esse comportamento observável, seja por valor de retorno, seja por estado interno visível por getters.
- No exemplo de `HasAdmin()`, o teste deve criar um `User` com relações e permissões adequadas e verificar o que muda quando o usuário é admin ou não.
- O método privado é testado indiretamente ao testar o comportamento exposto por métodos públicos.
