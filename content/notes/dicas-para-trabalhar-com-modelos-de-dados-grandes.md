---
title: "Dicas para trabalhar com modelos de dados grandes"
date: '2013-01-30T13:44:22-03:00'
category: webclip
summary: 'O artigo reúne dicas práticas para DBAs lidarem com modelos de banco de dados grandes e complexos, com foco em documentação, inspeção, manutenção e controle dos objetos.'
tags: ["modelagem-de-dados", "dba", "documentacao", "banco-de-dados"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Dicas para trabalhar com modelos de dados grandes"
    url: "http://imasters.com.br/banco-de-dados/dicas-para-trabalhar-com-modelos-de-dados-grandes/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2013-01/imasters-com-br--dicas-para-trabalhar-com-modelos-de-dados-grandes.md"
    kind: repo
---

O artigo reúne recomendações para DBAs que precisam entender e operar modelos de banco de dados grandes e complexos. O foco está em tornar o modelo mais fácil de inspecionar, documentar e manter quando há muitos objetos relacionados, mudanças constantes e grande volume de dados.

## Fichamento

- Identificar logo as tabelas maiores, mais cheias e mais usadas, porque elas costumam concentrar boa parte do tamanho e do acesso ao banco.
- Usar ferramenta de controle de versão ou gestão de configuração para acompanhar alterações em colunas, relacionamentos e tipos de dados ao longo do tempo.
- Saber imprimir o modelo inteiro ou parcialmente, em PDF ou em páginas separadas, quando a equipe precisar de uma visão em papel.
- Reconhecer os objetos complementares mais usados, como stored procedures, triggers, funções, views e índices, porque eles também fazem parte do trabalho diário.
- Visualizar o banco em camadas separadas, mostrando ou ocultando relacionamentos, índices e constraints conforme a necessidade.
- Agrupar tabelas do mesmo subsistema com retângulos coloridos e comentários para melhorar a leitura e a documentação.
- Descobrir a ordem correta para inserir, atualizar e remover dados em tabelas relacionadas, de modo que scripts possam reproduzir o comportamento da aplicação.
- Manter uma forma rápida de pesquisar nomes de atributos e consultar metadados em muitos objetos.
- Ter um script que crie os objetos do banco com apenas uma fração dos dados, em torno de 10%, para montar ambientes novos.
- Atualizar a lista de permissões dos objetos mais comuns para verificar rapidamente o que cada usuário pode fazer.
- Prever e estimar o tamanho dos objetos com base em estatísticas e medidas reais, em vez de suposições.
- Mostrar no modelo quais objetos usam particionamento, compressão e quais grupos de arquivos eles ocupam.
- Em modelos OLAP, centralizar a tabela fato e documentar hierarquias, níveis, membros e grãos das dimensões.
- O texto encerra reforçando que essas dicas giram em torno da documentação do modelo e dos objetos, não apenas do código-fonte.
