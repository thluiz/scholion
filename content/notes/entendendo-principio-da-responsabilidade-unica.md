---
title: "Entendendo o Princípio da Responsabilidade Única"
date: '2022-04-17T20:44:50-03:00'
category: webclip
summary: 'O texto explica o Princípio da Responsabilidade Única como a ideia de que cada classe deve ter um único motivo para mudar. Um exemplo com menu e funcionários mostra como separar responsabilidades melhora a coesão.'
tags: ["principio-da-responsabilidade-unica", "solid", "engenharia-de-software"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Entendendo o Princípio da Responsabilidade Única | by Carolina Dias | Apr, 2022 | Medium"
    url: "https://carodias.medium.com/entendendo-o-princ%C3%ADpio-da-responsabilidade-%C3%BAnica-4f11cd4a3caa"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2022-04/carodias-medium-com--entendendo-principio-da-responsabilidade-unica.md"
    kind: repo
---

O texto apresenta o Princípio da Responsabilidade Única como um dos princípios SOLID e destaca que ele é fácil de entender pelo nome, mas também costuma ser mal interpretado. A explicação central é que uma classe deve ter uma única responsabilidade, entendida como um único motivo para ser modificada.

## Fichamento

- Os princípios SOLID são descritos como base para estruturar projetos de software.
- O Princípio da Responsabilidade Única é apresentado como o mais autoexplicativo e também como um dos mais mal-entendidos.
- O exemplo mostra uma classe de menu de restaurante que também lista e cadastra funcionários.
- Essa classe quebra o princípio porque assume responsabilidades que não combinam com sua finalidade.
- A melhora proposta é separar o código em duas classes, uma para o menu e outra para os funcionários.
- Essa separação é associada a coesão e à Separação de Interesses.
- A definição citada diz que cada classe deve ter uma única responsabilidade, isto é, um único motivo para mudar.
- O texto observa que responsabilidade única não significa ter apenas um método.
- Na prática, o princípio é tratado como algo importante, embora o desenvolvimento diário nem sempre siga os ideais de forma perfeita.
