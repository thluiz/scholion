---
title: "Brincando de Crawlers e algumas Dicas Úteis"
date: '2015-05-18T07:55:25-03:00'
category: webclip
summary: 'O texto mostra um script Ruby para limpar arquivos no Slack e, a partir dele, recomenda Bundler, Faraday com Typhoeus, Oj e Parallel para lidar com crawling, JSON e trabalho paralelo com menos custo.'
tags: ["ruby", "crawlers", "parallel", "json"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Brincando de Crawlers e algumas Dicas Úteis"
    url: "http://www.akitaonrails.com/2015/05/15/small-bites-brincando-de-crawlers-e-algumas-dicas-uteis#.VVnE9ZdVikq"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2015-05/akitaonrails-com--brincando-de-crawlers-e-algumas-dicas-uteis.md"
    kind: repo
---

O texto parte de um script em Ruby para apagar arquivos no Slack usando a API, já que a interface de administração não oferece marcar tudo nem deletar tudo. A partir desse exemplo, reúne quatro dicas para scripts de crawler e tarefas parecidas, com foco em dependências, requisições HTTP, parsing de JSON e paralelismo.

## Fichamento

- Usa Bundler mesmo em scripts pequenos.
- Para acessar páginas web, combina Faraday com Typhoeus.
- Faraday abstrai clientes HTTP diferentes e permite trocar adapters com pouco esforço.
- Typhoeus faz várias requisições em paralelo, o que ajuda em crawlers, mas exige cuidado para não acumular dados demais em memória.
- Em vez de guardar tudo em um array, o texto sugere usar Dalli com Memcached, Redis, MongoDB ou outro armazenamento que aceite inserções assíncronas.
- Para respostas JSON, recomenda Oj junto com oj_mimic_json em projetos Rails.
- O texto diz que Oj é de 2 a 4 vezes mais rápida que a gem JSON e depende de extensão em C, então não funciona com JRuby, apenas com MRI.
- Para processar muitas respostas, indica a gem Parallel.
- No Ruby MRI, o GIL limita a execução paralela real, mas threads ainda ajudam em operações bloqueantes de I/O.
- Para tarefas CPU-bound, o texto orienta usar :in_processes em vez de :in_threads.
- Desde o Ruby 2.0, Copy on Write torna o uso de processos paralelos menos caro em memória.
- Para crawlers e ETL, Parallel pode ser útil, mas o texto recomenda medir para evitar falsa impressão de paralelismo.
