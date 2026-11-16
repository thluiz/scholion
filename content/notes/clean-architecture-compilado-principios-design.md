---
title: "Clean Architecture: um compilado dos Princípios de Design"
date: '2026-11-16T02:01:27+00:00'
category: webclip
summary: 'A página compila como os princípios SOLID mudam no nível de arquitetura, com foco em limites entre sistemas, extensibilidade, coesão, dependências e redução de acoplamento.'
tags: ["solid", "clean-architecture", "design-de-software", "arquitetura-de-software"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Clean Architecture : um compilado dos Princípios de Design"
    url: "https://dev.to/psanrosa13/clean-architecture-um-compilado-dos-principios-de-design-2mla"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/dev-to--clean-architecture-compilado-principios-design.md"
    kind: repo
---

O texto reúne uma leitura de SOLID no contexto de arquitetura de software, não só de código. A ideia central é que esses princípios ajudam a dar flexibilidade a mudanças, organizar melhor os domínios, favorecer reuso de componentes e reduzir dependências diretas entre partes do sistema.

## Fichamento

- SOLID é apresentado como um conjunto de princípios de design que, em arquitetura, pode se referir a conceitos macro, funcionais, componentes, bibliotecas ou classes
- No nível arquitetural, a aplicação dos princípios varia conforme o nível em que são usados
- O SRP, em arquitetura, significa que um módulo deve ter apenas uma razão para mudar, ligada a um ator específico entre usuários e stakeholders
- Esse uso do SRP ajuda a identificar limites entre sistemas e suas comunicações, o que o texto chama de eixo da mudança
- O OCP é associado à ideia de um artefato ser extensível sem sofrer modificações
- Em arquitetura, o OCP ganha importância porque permite que sistemas sejam usados em outros contextos com pouco impacto neles mesmos
- O OCP também protege sistemas de alto nível do comportamento de quem os utiliza
- O LSP aparece primeiro ligado a herança, mas o texto o amplia para interfaces e implementações
- Em arquitetura, o LSP ajuda a manter o mesmo comportamento independentemente da comunicação ou do sistema usado
- O ISP orienta a evitar dependências em módulos com mais elementos do que o necessário
- O texto liga essa preocupação às dependências que podem impactar a arquitetura e menciona o Princípio do Reuso Comum como apoio à coesão dos componentes
- O DIP propõe que implementações dependam de referências e não de itens concretos
- No caso do Java, o texto cita classes abstratas e interfaces em vez do uso direto da classe que implementa o código
- Em arquitetura, o DIP ajuda a evitar vendor lock-in e reduz o acoplamento entre componentes
