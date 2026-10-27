---
title: "As fantásticas novidades do HTTP 2.0 e do SPDY"
date: '2014-06-14T16:01:22-03:00'
category: webclip
summary: 'O texto apresenta mudanças do HTTP 2.0 e do SPDY para performance, segurança e simplicidade no desenvolvimento, com compressão, HTTPS, multiplexing, priorização e server-push.'
tags: ["http-2-0", "spdy", "web-performance", "https"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "As fantásticas novidades do HTTP 2.0 e do SPDY"
    url: "http://blog.caelum.com.br/as-fantasticas-novidades-do-http-2-0-e-do-spdy/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2014-06/blog-caelum-com-br--novidades-http-2-0-spdy.md"
    kind: repo
---

O texto resume as principais mudanças do HTTP 2.0 e do SPDY e mostra como elas afetam a Web. Entre os ganhos descritos estão compressão automática, uso de HTTPS, requisições paralelas, envio apenas de cabeçalhos que mudam, priorização de recursos e server-push.

## Fichamento

- No HTTP 2.0, o GZIP é padrão e obrigatório.
- Os headers passam a ser binários e comprimidos com HPACK, reduzindo o volume trafegado.
- O SPDY obriga o uso de HTTPS e o HTTP 2.0, na prática, também é suportado apenas com conexões seguras.
- O uso de SSL ajuda na migração do protocolo sem quebrar navegadores antigos nem intermediários como proxies e CDNs.
- No HTTP 2.0 e no SPDY, requests e responses podem ocorrer em paralelo em uma única conexão, por multiplexing.
- O navegador deixa de precisar de várias conexões e de vários hostnames para paralelizar requisições.
- O protocolo passa a enviar apenas os cabeçalhos que mudam entre requisições.
- O browser pode indicar quais requests são mais importantes, para que o servidor priorize as respostas.
- O server-push permite que o servidor envie recursos antes de o navegador requisitá-los.
- O server-push mantém os recursos separados, cacheáveis e sem as gambiarras do inline.
