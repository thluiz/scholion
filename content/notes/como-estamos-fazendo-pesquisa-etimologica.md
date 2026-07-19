---
title: "Como estamos fazendo pesquisa etimológica"
date: '2026-07-18T11:18:54+01:00'
summary: "As notas de etimologia do Scholion saem de sete fontes cruzadas, uma de cada vez. O que as segura contra a invenção: source-or-silence, a seção de divergências, e a lacuna marcada em vez de preenchida."
tags: ["etimologia", "chinês", "linguística", "método"]
has_commentary: false
sources:
  - title: "A Academia Sinica e os 2000 anos de etimologia"
    url: "https://silva.thluiz.com/posts/academia-sinica-2000-anos-etimologia/"
    kind: article
  - title: "MDBG Chinese Dictionary"
    url: "https://www.mdbg.net/chinese/dictionary"
    kind: wiki
  - title: "chardb — Academia Sinica"
    url: "https://chardb.iis.sinica.edu.tw"
    kind: wiki
  - title: "CantoDict (cantonese.org)"
    url: "https://www.cantonese.org"
    kind: wiki
  - title: "Chinese Etymology (hanziyuan.net)"
    author: "Richard Sears"
    url: "https://hanziyuan.net"
    kind: wiki
  - title: "小學堂 — Academia Sinica"
    url: "https://xiaoxue.iis.sinica.edu.tw"
    kind: wiki
  - title: "說文解字 (shuowen.org)"
    url: "https://www.shuowen.org"
    kind: wiki
  - title: "漢語多功能字庫 (CUHK)"
    url: "https://humanum.arts.cuhk.edu.hk/Lexis/lexi-mf"
    kind: wiki
  - title: "Survey of Hallucination in Natural Language Generation (Ji et al., 2023)"
    url: "https://dl.acm.org/doi/10.1145/3571730"
    kind: article
---

Para nos aprofundar no pensamento chinês, viemos nos debruçando sobre a etimologia dos principais caracteres que usamos. O ponto de partida foi [a Academia Sinica e os dois mil anos de etimologia](https://silva.thluiz.com/posts/academia-sinica-2000-anos-etimologia/), que dá acesso ao Shuowen Jiezi e ao [comentário de Duan Yucai](/notes/duan-yucai-shuowen-jiezi-zhu/). A partir daí o material foi crescendo: o próprio [Shuowen Jiezi](/notes/shuowen-jiezi/), Richard Sears (hanziyuan) e o CantoDict para os caracteres cantoneses.



## As fontes

As sete, cada uma com um papel distinto:

- **MDBG**: definições e leituras modernas (pinyin, jyutping).
- **chardb**, da Academia Sinica: definições chinesas numeradas, verbatim.
- **CantoDict** (cantonese.org): leitura cantonesa com tons.
- **hanziyuan.net**, de Richard Sears: decomposição e formas antigas (osso oracular, bronze, selo).
- **小學堂** ([Xiaoxuetang](/notes/xiaoxuetang/)), da Academia Sinica: evolução das formas e fonologia (chinês médio pelo 廣韻, chinês antigo em cinco sistemas de reconstrução).
- **shuowen.org**: o [Shuowen Jiezi](/notes/shuowen-jiezi/) e o [comentário 段注 de Duan Yucai](/notes/duan-yucai-shuowen-jiezi-zhu/).
- **漢語多功能字庫**, da Universidade Chinesa de Hong Kong: cruzamento e etimologia interpretativa.

Os caracteres são processados um de cada vez, nunca em paralelo. Disparar consultas simultâneas a todas as bases, para vários caracteres, sobrecarregaria serviços que uso de graça.

Uma ressalva sobre o MDBG. O dado que ele serve vem do CC-CEDICT, dicionário comunitário sob licença Creative Commons (CC BY-SA). O conteúdo é livre. O site, porém, [pede que não se faça acesso automatizado à base](https://www.mdbg.net/chinese/dictionary?page=cc-cedict): livre para ler, não para varrer com robô. Por isso a consulta é manual e uma de cada vez, não um crawler solto sobre o dicionário.


## LLMs

Um modelo de linguagem lê o que as sete fontes retornam e organiza: junta as definições, alinha as formas antigas, traduz os comentários, monta a tabela de fonologia. É trabalho de leitura e ordenação, e nisso ele rende.

O que ele não faz é separar o que é verdade do que apenas soa verdadeiro. Um LLM é treinado para prever a próxima palavra e seguir o texto de forma plausível; quando o dado falta, preenche com o que caberia ali. É o fenômeno que a literatura técnica chama de [alucinação](https://dl.acm.org/doi/10.1145/3571730). Numa etimologia, uma glosa inventada tem a mesma cara de uma glosa atestada.

Os próprios crawlers que raspam essas fontes saíram do modelo também, e aí ele acerta com folga: código roda ou não roda, o erro aparece na hora. Uma glosa inventada não dispara erro nenhum, e é aí que entra a exigência de fonte.

## A seção que importa

Cada nota termina com as divergências entre as fontes: o registro de onde elas discordam, sem síntese que apare as arestas. As contagens de atestação (quantas formas em osso oracular, bronze, selo) variam entre o hanziyuan e a 小學堂, que costuma ser mais precisa. O significado primário do Shuowen nem sempre é o primeiro sentido do MDBG. A mesma decomposição pode ser lida como fonética numa fonte e semântica noutra.

A regra é não resolver a divergência por conta própria. A nota registra o desacordo e deixa o leitor vê-lo.

O papel criativo do modelo termina aqui: a partir do que as fontes atestam, sintetizar uma nota legível. Ele junta, traduz e organiza o que veio das sete bases, mas não é ele que responde pelo dado. Cada afirmação carrega a fonte que a sustenta.

## Contra a paráfrase plausível

Toda afirmação factual precisa de fonte inline. Etimologia, datação, glosa, leitura. Sem fonte atestada, a afirmação não entra.

Em etimologia, o erro mais enganoso é inventar um dado para fechar um vazio. Uma glosa que soa certa, uma datação "Ming–Qing" plausível, um comentário reconstruído de memória. São plausíveis, e verificáveis como falsos. Um modelo de linguagem preenche esse vazio por padrão; um filólogo com pressa faz o mesmo.

Quando uma fonte não retorna o dado, a nota diz isso, com o motivo:

> **段注 Duan Yucai**: (não retornou dados — shuowen.org devolveu apenas a listagem do dicionário; o fallback zdic.net retornou 404)

Isso é de uma [nota real, a de 分](/notes/etimologia-de-fan-fen-5206/) (fēn, "dividir"). As fontes não retornaram o 段注 desse caractere no momento da escrita. A nota não fabrica um. Deixa o buraco à vista, com a causa, e quem vier depois sabe o que falta e onde procurar.

