---
title: "Um guia completo de tipografia para a web"
date: '2012-12-12T08:59:52-03:00'
category: webclip
summary: 'O artigo defende que tipografia é parte central da interface e reúne orientações sobre alinhamento, famílias, tamanho, largura, peso, contraste, ritmo vertical e ligaturas.'
tags: ["tipografia", "design-web", "legibilidade", "css"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Um guia completo de tipografia para a web"
    url: "http://tableless.com.br/um-guia-completo-de-tipografia-para-a-web/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2012-12/tableless-com-br--um-guia-completo-de-tipografia-para-a-web.md"
    kind: repo
---

O texto trata a tipografia como parte da usabilidade da web, porque a maior parte do conteúdo é leitura. A ideia é tornar a leitura fácil e confortável, e tratar escolhas tipográficas como parte da interface, não como decoração.

## Fichamento

- Alinhamento à esquerda ou justificado facilita a leitura porque as linhas começam no mesmo ponto; alinhamento à direita e centralizado dificulta a varredura visual e fica melhor em blocos curtos, como títulos e citações.
- Texto justificado pode abrir lacunas entre palavras na web por falta de hifenização, então deve ser usado só em trechos curtos e bem controlados.
- A tipografia para a web é apresentada em cinco famílias: serif, sans-serif, cursive, fantasy e monospace, com exemplos de cada uma.
- Para textos longos na web, o artigo sugere serifadas ou sem serifa e diz que a escolha deve seguir o estilo da página; também menciona que combinar as duas pode gerar contraste útil.
- O tamanho padrão de 16px no navegador é tratado como uma boa base porque a distância de leitura na tela é maior do que no papel.
- O texto recomenda EM para textos porque essa unidade permite redimensionamento no navegador, se adapta melhor a diferentes dispositivos e mantém proporções entre texto e espaçamento.
- A regra `font-size: 62.5%` no `html` é sugerida para fazer 1em equivaler a 10px e facilitar a conversão entre pixels e ems.
- A largura ideal de linha é colocada em cerca de 10 a 15 palavras, ou aproximadamente 65 caracteres, e a regra de Bringhurst de multiplicar o tamanho da fonte por 30 aparece como referência de largura.
- O peso da fonte é definido por `font-weight`, e o artigo alerta que forçar negrito em fontes sem esse peso pode gerar uma simulação artificial mais grosseira.
- Contraste importa em cor, tamanho, peso e distância; o texto diz que cinza escuro sobre branco cansa menos do que preto total sobre branco.
- O ritmo vertical depende de tamanho da fonte, margens, espaçamentos e entrelinha, e o artigo propõe 140% de line-height como base prática.
- Ligaturas podem ser ativadas em fontes OpenType com `font-feature-settings: 'liga'` e as versões com prefixo para navegadores.
- A conclusão diz que texto deve ser tratado como interface, não como decoração, e cita @font-face, Google Fonts, Typekit e web-safe fonts como caminhos práticos.
