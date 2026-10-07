---
title: "Um exemplo bacana de coerção em Ruby"
date: '2014-10-29T12:11:20-03:00'
category: webclip
summary: 'O post mostra como Ruby trata operadores como métodos e usa a classe Intervalo para explicar to_s, +, coerce e to_i na soma entre tipos diferentes.'
tags: ["ruby", "coercao", "metodos", "objetos-imutaveis"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Um exemplo bacana de coerção em Ruby"
    url: "http://blog.caelum.com.br/um-exemplo-bacana-de-coercao-em-ruby/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2014-10/blog-caelum-com-br--um-exemplo-bacana-de-coercao-em-ruby.md"
    kind: repo
---

Ruby trata operadores aritméticos como métodos, e isso permite redefinir o comportamento de classes próprias. O exemplo usa a classe Intervalo, criada a partir de minutos, para mostrar como to_s pode devolver uma string formatada e como + pode retornar um novo objeto sem alterar o original.

## Fichamento

- Operadores como +, -, * e / são métodos, o que torna possível redefinir seu comportamento em classes próprias.
- A classe Intervalo guarda minutos e expõe horas e minutos para representar o tempo como horas e resto.
- Definir to_s em Intervalo permite exibir o intervalo no formato esperado, em vez da representação padrão de Object.
- Usar sprintf melhora a saída para manter os minutos com duas casas.
- O método + pode ser definido em Intervalo para somar minutos e devolver um novo objeto.
- A adição preserva a imutabilidade do objeto original, porque retorna outro Intervalo.
- Ao somar dois Intervalos, Ruby tenta coerção porque Fixnum#+ não conhece Intervalo.
- O método coerce pode devolver dois objetos compatíveis para que a operação continue dentro de Fixnum#+.
- Ao devolver um par apropriado em coerce, a soma 30 + Intervalo passa a ser resolvida pela lógica de Intervalo#+.
- Para que o resultado final continue sendo um Intervalo, o método coerce pode inverter a operação e fazer Fixnum delegar a soma de volta para Intervalo.
- Para evitar que @minutos receba um valor não inteiro, o construtor converte minutos com to_i.
- A convenção de conversão para inteiro em Ruby envolve expor um método to_i, enquanto Fixnum já responde a esse método.
