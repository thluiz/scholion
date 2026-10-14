---
title: "Criando um plugin JavaScript (sem jQuery!)"
date: '2012-11-07T09:20:31-03:00'
category: webclip
summary: 'O artigo mostra como montar um slider de imagens com JavaScript e CSS3, sem biblioteca, usando prototypes, querySelectorAll, createElement e navegação entre páginas.'
tags: ["javascript", "css3", "slider", "plugin"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Criando um plugin JavaScript (sem jQuery!)"
    url: "http://tableless.com.br/criando-um-plugin-javascript-sem-jquery/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2012-11/tableless-com-br--criando-um-plugin-javascript-sem-jquery.md"
    kind: repo
---

O texto apresenta a construção de um slider de imagens feito só com JavaScript e CSS3, sem biblioteca, com foco em um código pequeno, extensível e válido em JSLint. A proposta é criar um plugin instanciável com selector, separar o objeto principal de cada estágio do slider e usar a animação via CSS para ganhar desempenho.

## Fichamento

- O plugin é pensado para ser instanciado com `new JSlider('.slider')` e para armazenar vários objetos `JSliderStage`.
- A inicialização usa `querySelectorAll` para localizar os elementos e criar uma instância de estágio para cada um.
- O estágio guarda o elemento raiz, a página atual e as imagens encontradas no container; se não houver imagem, a execução para.
- A montagem calcula largura e altura máximas a partir das imagens antes de criar o palco.
- O palco usa uma `div` principal e um trilho interno, com a animação da troca de imagens feita por `transition` no CSS.
- As imagens são colocadas em uma lista `ul`, com cada `li` recebendo a largura e a altura do palco para manter o alinhamento.
- A navegação só é criada quando há pelo menos duas imagens.
- Os botões de navegação são links com eventos de clique que impedem o comportamento padrão e chamam a troca de página.
- O método `gotoPage` ajusta o `margin-left` da lista para mostrar a imagem correta e atualiza o estado dos controles.
- O método `setNavigationState` ativa e desativa os botões conforme a posição atual, usando `classList`.
- O texto sugere como melhorias temporizador, suporte a navegadores antigos, conteúdo além de imagens, navegação por teclado, miniaturas e testes com Jasmine.
