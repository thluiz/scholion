---
title: "Melhorando validações no domínio com melhores assinaturas de método e lógica funcional (Parte 2)"
date: '2016-12-28T08:26:53-03:00'
category: webclip
summary: 'O texto propõe assinaturas mais claras para recuperar, modificar e persistir entidades, usando tipos como Try, Untrusted e Unit para explicitar falhas, entrada duvidosa e evitar null.'
tags: ["domain-validation", "functional-programming", "method-signatures", "immutability"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Melhorando validações no domínio com melhores assinaturas de método e lógica funcional (Parte 2)"
    url: "http://elemarjr.com/2016/12/26/melhorando-validacoes-no-dominio-com-melhores-assinaturas-de-metodo-e-logica-funcional-parte-2/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2016-12/elemarjr-com--melhorando-validacoes-no-dominio-com-melhores-assinaturas-de.md"
    kind: repo
---

O texto retoma o cenário de recuperar uma entidade, aplicar uma mudança e persistir o resultado, para mostrar que assinaturas comuns escondem muitas dúvidas sobre null, exceptions e falhas de banco. A proposta é tornar esses contratos explícitos com tipos mais ricos e com um fluxo de chamada que expõe o caminho de sucesso sem misturar tratamento de erro.

## Fichamento

- Um repositório com `GetById(string id)` e `Save(Employee employee)` deixa em aberto o que acontece com id inválido, ausência de entidade e falhas de conexão.
- A assinatura `Try<Exception, Employee> GetById(Untrusted<string> id)` deixa explícito que a recuperação pode falhar e que o id recebido não é confiável.
- O texto sugere usar um tipo de domínio como `Cpf` no lugar de `string`, para enriquecer o modelo e afastar a possibilidade de retornar `null` quando não houver entidade correspondente.
- Em vez de uma entidade mutável, a proposta é usar `Try<Exception, Employee> RaiseSalary(decimal amount)`, indicando que a mudança pode falhar e produzir uma nova instância atualizada.
- Para persistência, `Try<Exception, Unit> Save(Employee employee)` torna visível que o método pode falhar, em vez de esconder isso atrás de `void`.
- A versão revisada encadeia `GetById`, `RaiseSalary` e `Save` com `Bind`, ou com o atalho `Then`, mantendo o fluxo de sucesso e deixando as falhas expressas no tipo retornado.
