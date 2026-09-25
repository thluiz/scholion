---
title: "Why we Built a Mini-Language for a Golang Hackathon"
date: '2026-09-25T01:02:43+01:00'
category: webclip
summary: 'O grupo criou o Fractal, uma ferramenta de processamento de dados com uma mini-linguagem declarativa para validação e transformação, para tornar pipelines mais flexíveis e fáceis de configurar.'
tags: ["golang", "hackathon", "data-pipelines", "mini-language"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Why we Built a Mini-Language for a Golang Hackathon"
    url: "https://dev.to/skysingh04/why-we-built-a-mini-language-for-a-golang-hackathon-42a3"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/dev-to--why-we-built-a-mini-language-for-a-golang-hackathon.md"
    kind: repo
---

The page explains that the team wanted to build more than another tool in a Golang hackathon, so they created Fractal, a data-processing tool with a mini-language for validation and transformation rules. It also says the system was meant to work with a YAML configuration and support multiple input and output formats.

## Fichamento

- O projeto Fractal surgiu como uma ferramenta de processamento de dados para migrar dados de sistemas legados, como bancos SQL e arquivos CSV, para plataformas como MongoDB ou AWS S3.
- A equipe quis ir além de um ETL comum e criar algo mais flexível e fácil de usar, com uma sintaxe declarativa para regras de validação e transformação.
- A mini-linguagem foi pensada para reduzir a dependência de scripts rígidos e configurações que exigem mais conhecimento de programação.
- O texto destaca três objetivos para a linguagem: simplicidade, flexibilidade e escalabilidade.
- A configuração em YAML foi apresentada como parte da proposta para deixar o pipeline mais fácil de configurar.
- As regras de validação citadas incluem tipo de campo, intervalo numérico, regex de e-mail e pertencimento a um conjunto de valores.
- As regras de transformação citadas incluem renomear campos, mapear valores, adicionar campos novos e aplicar condições como desconto para idade acima de 50.
- O sistema também foi descrito como extensível, configurável e robusto, com suporte a formatos como JSON, CSV, bancos SQL e filas de mensagens.
- O trabalho do hackathon foi dividido em quatro módulos: implementação da mini-linguagem, integrações de dados, engine de pipeline e interface de linha de comando.
- Entre os desafios estiveram o desenho da sintaxe, a criação do lexer e parser em Golang, o feedback de erros em tempo real e o limite de tempo do hackathon.
- Na avaliação final, a equipe teve problema com um bug no parser durante a demonstração ao vivo, o que fez perder o primeiro lugar.
- Mesmo assim, o grupo recebeu o prêmio de Best Pitch.
- O texto conclui que hackathons servem para testar limites e explorar novas possibilidades, e associa Fractal a uma tentativa de tornar ferramentas de processamento de dados mais acessíveis, modulares e fáceis para desenvolvedores.
