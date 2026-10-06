---
title: "Bons desenvolvedores não gostam de mágica"
date: '2012-04-03T11:28:21-03:00'
category: webclip
summary: 'O texto defende que soluções “mágicas” escondem a implementação e exigem confiança cega, enquanto migrations dão visibilidade e controle sobre cada mudança no banco de dados.'
tags: ["migrations", "abstractions", "database"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Bons desenvolvedores não gostam de mágica"
    url: "http://tatiyants.com/good-devs-dont-like-magic/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2012-04/tatiyants-com--bons-desenvolvedores-nao-gostam-de-magica.md"
    kind: repo
---

O texto contrapõe soluções “mágicas”, que ocultam como funcionam por dentro, a abordagens mais transparentes. O autor usa o projeto de banco de dados do Visual Studio como exemplo de ferramenta que pede confiança na própria automação, e defende migrations como alternativa mais previsível.

## Fichamento

- Soluções “mágicas” escondem a implementação básica e pedem que o desenvolvedor aceite o resultado sem entender o processo.
- O projeto de banco de dados do Visual Studio é apresentado como caso típico de solução mágica, porque compara o esquema atual com uma linha de base e gera um delta difícil de prever.
- O autor diz que bons desenvolvedores querem entender o caminho entre A e B e manter o controle do código.
- Ele associa o custo da magia aos momentos em que algo falha e é preciso percorrer abstrações para descobrir o problema.
- Migrations aparecem como mais amigáveis porque aplicam arquivos numerados em sequência e deixam claro o que muda em cada passo.
- O texto admite que qualquer abstração pode parecer mágica, como um compilador.
- A diferença, segundo o autor, está em quando a abstração faz sentido e quando o custo de obscurecimento fica alto demais, como ele sugere no caso do CoffeeScript.
- O autor acrescenta que desenvolvedores medianos ou ruins tendem a aceitar soluções mágicas com mais facilidade.
