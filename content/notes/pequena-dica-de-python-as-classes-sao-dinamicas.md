---
title: "Pequena dica de Python: as classes são dinâmicas"
date: '2012-12-05T10:14:27-03:00'
category: webclip
summary: 'O texto mostra que classes em Python podem receber métodos depois de criadas, e que essas mudanças aparecem nos objetos já instanciados.'
tags: ["python", "classes", "metodos-dinamicos"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Pequena dica de Python: as classes são dinâmicas"
    url: "http://elcio.com.br/pequena-dica-de-python-as-classes-sao-dinamicas/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2012-12/elcio-com-br--pequena-dica-de-python-as-classes-sao-dinamicas.md"
    kind: repo
---

As classes em Python são dinâmicas e podem receber novos métodos depois de definidas. O exemplo mostra que esses métodos passam a funcionar nos objetos já criados com a mesma classe.

## Fichamento

- A classe é definida com um método que retorna 1, e uma instância chama esse método.
- Uma função externa é atribuída à classe como `dois`, e a instância passa a chamá-la.
- Uma lambda é atribuída como `tres`, e a instância também a chama.
- A reatribuição de `Class.um` altera o resultado do método na instância já criada.
- O texto compara esse comportamento ao uso de prototype no JavaScript.
