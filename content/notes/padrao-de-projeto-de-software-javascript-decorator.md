---
title: "Padrão de projeto de software - JavaScript: Decorator"
date: '2012-03-28T11:32:14-03:00'
category: webclip
summary: 'O texto explica o padrão Decorator em JavaScript como forma de adicionar recursos a um objeto sem subclassificar. Mostra como encadear decorators com a mesma interface para estender um carro.'
tags: ["javascript", "design-patterns", "decorator"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Padrão de projeto de software - JavaScript: Decorator – iMasters"
    url: "http://imasters.com.br/artigo/23934/javascript/padrao-de-projeto-de-software-javascript-decorator"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2012-03/imasters-com-br--padrao-de-projeto-de-software-javascript-decorator.md"
    kind: repo
---

O texto apresenta o Decorator como uma forma de acrescentar funcionalidades a objetos sem criar muitas subclasses. Em vez de multiplicar classes para cada combinação de recursos, o objeto base é envolvido por decorators que mantêm a mesma interface e adicionam comportamento aos poucos.

## Fichamento

- O padrão Decorator adiciona recursos a objetos sem subclassificar nem incluir atributos extras.
- O exemplo inicial com carros mostra como as combinações de recursos viram muitas classes quando se usa herança clássica.
- O objeto base Car define a interface usada pelos decorators, com métodos como start, drive e getPrice.
- A classe CarDecorator recebe um carro e repassa as chamadas para o objeto envolvido.
- Decorators específicos, como PowerLocksDecorator e ACDecorator, chamam o carro original e depois acrescentam novo comportamento.
- O texto observa que a ordem importa, porque o decorator pode executar primeiro o objeto envolvido e depois adicionar sua própria lógica.
- O uso prático consiste em criar um Car, envolver esse objeto com decorators sucessivos e reutilizar a mesma variável para o resultado final.
- O autor diz que o padrão ajuda na manutenção a longo prazo, mas não mostra código para evitar que o mesmo recurso seja adicionado duas vezes.
