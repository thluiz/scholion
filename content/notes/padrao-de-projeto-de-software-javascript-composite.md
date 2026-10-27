---
title: "Padrão de projeto de software - JavaScript: Composite"
date: '2012-03-23T16:21:09-03:00'
category: webclip
summary: 'O texto explica o padrão Composite em JavaScript, sua estrutura em árvore e como ele permite aplicar uma operação a toda a hierarquia mantendo folhas e composites sob a mesma interface.'
tags: ["javascript", "composite", "padroes-de-projeto"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Padrão de projeto de software - JavaScript: Composite – iMasters"
    url: "http://imasters.com.br/artigo/23898/javascript/padrao-de-projeto-de-software-javascript-composite"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2012-03/imasters-com-br--padrao-de-projeto-de-software-javascript-composite.md"
    kind: repo
---

O artigo apresenta o Composite como um padrão formado por partes que compõem um todo, com dois ganhos centrais: tratar uma coleção como objetos individuais e organizar objetos em uma estrutura de árvore com a implementação interna escondida. O exemplo em JavaScript usa uma galeria de imagens para mostrar como composites e folhas compartilham a mesma interface, mesmo quando as folhas não têm filhos.

## Fichamento

- Composite é descrito como uma composição de várias peças para formar uma entidade inteira.
- Um benefício é aplicar a mesma operação ao conjunto e a cada objeto da coleção.
- Outro benefício é organizar os objetos em uma árvore e ocultar como os filhos são armazenados.
- A hierarquia do padrão tem dois tipos de objetos: folha e composite.
- Folhas não têm filhos, enquanto composites têm.
- O sistema de arquivos aparece como exemplo comum, com discos e pastas como composites e arquivos como folhas.
- A árvore binária é citada como um tipo especial de composite, com no máximo dois filhos por nó.
- O exemplo em JavaScript usa uma galeria de imagens em vez de um sistema de arquivos.
- O código define os métodos add, remove e getChild para o composite.
- A galeria também define hide e show para afetar o composite e todos os seus filhos.
- A classe folha da imagem implementa os mesmos métodos, mas add, remove e getChild não fazem nada.
- jQuery é usado para ajudar no trabalho com o DOM.
- Um contêiner principal é adicionado ao body e depois exibido.
- O texto diz que o padrão torna o código mais fácil de usar, mantém os objetos fracamente acoplados e dá uma estrutura clara.
- O artigo também alerta que um composite grande pode esconder custos de desempenho.
- O texto encerra dizendo que Composite é uma ferramenta poderosa e deve ser usada com cuidado.
