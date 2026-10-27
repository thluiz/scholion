---
title: "Dicas de desempenho do Python - Parte 01"
date: '2012-06-04T12:05:46-03:00'
category: webclip
summary: 'O texto reúne 18 dicas para melhorar o desempenho em Python, com foco em built-ins, estruturas de dados, generators, caching, módulos da biblioteca e cuidados com o GIL.'
tags: ["python", "performance", "programming"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Dicas de desempenho do Python - Parte 01 – iMasters"
    url: "http://imasters.com.br/artigo/24050/py/dicas-de-desempenho-do-python-parte-01"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2012-06/imasters-com-br--dicas-de-desempenho-do-python-parte-01.md"
    kind: repo
---

O texto reúne recomendações práticas para escrever código Python mais rápido. Ele insiste no uso de recursos embutidos, de estruturas e módulos mais adequados para cada tarefa, e lembra que às vezes o ganho vem de mover trabalho para C/C++ ou para código externo quando o desempenho exigir.

## Fichamento

- Funções internas em Python tendem a ser muito rápidas porque são escritas em C.
- Para juntar muitas strings, `join()` é preferível a usar `+` repetidamente, já que cada concatenação cria uma nova string.
- Atribuição múltipla, como `x, y = y, x`, troca variáveis de forma mais rápida e elegante do que usar uma variável temporária.
- Variáveis locais são recuperadas mais depressa que variáveis globais, então o texto recomenda evitar `global` quando possível.
- Para testar se algo existe em uma sequência, o uso de `in` é descrito como limpo e rápido.
- Importar módulos só quando forem necessários pode distribuir o custo de carregamento, embora isso não melhore o desempenho total.
- Em laços infinitos, `while 1` é apresentado como uma forma de loop mais rápida do que `while True`.
- List comprehensions podem substituir muitos blocos `for` e `while`, com ganho de velocidade e, em muitos casos, melhor legibilidade.
- `xrange()` é indicado para sequências longas porque gera valores sob demanda e economiza memória.
- Generators também economizam memória e podem melhorar o desempenho por produzirem valores quando são pedidos.
- O módulo `itertools` é destacado como eficiente para iteração e combinação, como no caso de permutações.
- `bisect` permite inserir elementos em listas ordenadas sem precisar chamar `sort()` de novo.
- Listas em Python são arrays, o que torna acesso por índice constante, mas torna custosa a inserção no início; para inserções e remoções nas duas extremidades, o texto sugere `deque`.
- `dict` e `set` são adequados para testar pertencimento porque usam tabela hash e podem oferecer busca em tempo próximo de O(1).
- `sort()` nativo é rápido, e o texto recomenda transformar os dados antes de ordenar quando for preciso usar uma ordem personalizada.
- Decorators podem ser usados para cachear resultados e memorizar valores já calculados, como em uma função Fibonacci.
- O GIL impede que várias threads executem bytecodes Python ao mesmo tempo, então threads não aceleram automaticamente o código em máquinas multi-core.
- Quando a documentação oficial não basta, o texto recomenda olhar o código-fonte do Python para entender estruturas de dados e algoritmos.
