---
title: "DDD – Introdução a Domain Driven Design"
date: '2014-06-24T10:14:42-03:00'
category: webclip
summary: 'O artigo apresenta DDD como projeto orientado a domínio, mostra linguagem ubíqua e projeto dirigido pelo modelo, e reúne padrões para modelar, refinar e organizar sistemas complexos.'
tags: ["domain-driven-design", "linguagem-ubiqua", "projecto-dirigido-pelo-modelo", "projeto-estrategico"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "DDD – Introdução a Domain Driven Design | AgileAndArt"
    url: "http://www.agileandart.com/2010/07/16/ddd-introducao-a-domain-driven-design/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2014-06/agileandart-com--ddd-introducao-a-domain-driven-design.md"
    kind: repo
---

O artigo define DDD como projeto orientado a domínio e o liga ao livro de Eric Evans. Também o apresenta como um conjunto de padrões vindo de práticas de orientação a objetos, com foco em regras de negócio, comunicação entre times e refinamento contínuo do modelo.

## Fichamento

- DDD é apresentado como projeto orientado a domínio, a partir do livro de Eric Evans e de padrões reunidos ao longo de mais de 20 anos de experiência em software.
- O texto relaciona orientação a objetos com alinhamento do código ao negócio, reutilização, baixo acoplamento e independência de tecnologia.
- A Linguagem Ubíqua é descrita como um vocabulário comum entre especialistas de negócio e desenvolvedores, com os mesmos termos usados na conversa e no código.
- O Projeto Dirigido pelo Modelo é descrito como a construção de um modelo abstrato que represente o domínio, com participação de todo o time.
- O artigo diz que o modelo e o código devem se aprimorar continuamente, por meio do contato com o código e da refatoração.
- A arquitetura em camadas isola a camada de domínio da interface de usuário, da aplicação e da infraestrutura.
- Os blocos de construção listados são entidades, objetos de valores, agregados, fábricas, serviços, repositórios e módulos.
- O texto explica que objetos de valores são imutáveis e que agregados expõem uma raiz pela qual seus dados internos são manipulados.
- Serviços são descritos como classes com lógica de negócio que não pertence a entidades nem a objetos de valores, e que não guardam estado.
- Repositórios são apresentados como responsáveis pelo ciclo de vida dos objetos, com exemplos de uso em Hibernate, Nhibernate e ActiveRecord.
- Os padrões de refinamento citados incluem Interface de Intenção Revelada, Funções sem Efeitos-Colaterais e Asserções.
- A parte estratégica introduz Contextos Delimitados, Mapa de Contextos, relação Produtor-Consumidor, Conformista, Núcleo Compartilhado, Camada Anti-corrupção, Caminhos Separados e Serviço Aberto de Funcionalidades com Linguagem Publicada.
- O artigo encerra destacando a destilação do domínio, a identificação do núcleo do domínio, a separação de subdomínios genéricos e a documentação da visão do domínio.
- O texto recomenda refatoração contínua e trata DDD como um meio de extrair a essência de um sistema complexo.
