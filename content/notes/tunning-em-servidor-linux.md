---
title: "Tunning em servidor Linux"
date: '2015-04-20T09:10:10-03:00'
category: webclip
summary: 'O post lista ajustes de servidor Linux para elevar a performance, mexer nos limites do kernel e no sysctl, reduzir gargalos e aproveitar melhor o hardware.'
tags: ["linux", "tunacao-de-servidor", "kernel", "sysctl"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Tunning em servidor Linux | Underground WebDev"
    url: "http://udgwebdev.com/tunning-em-servidor-linux"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2015-04/udgwebdev-com--tunning-em-servidor-linux.md"
    kind: repo
---

O post reúne configurações para servidores Linux com foco em desempenho. Ele diz que os ajustes podem aumentar a performance das aplicações entre 10% e 40% e, em alguns casos, resolver gargalos melhor do que adicionar outra máquina ao balanceamento de carga.

## Fichamento

- Sugere editar /etc/security/limits.conf para ampliar limites de processos, arquivos abertos, memória, CPU, tamanho de arquivo, msgqueue e locks.
- Sugere editar /etc/sysctl.conf para ajustar file descriptors, swap, faixa de portas, buffers de rede, backlog, reutilização de sockets e timeout do TCP.
- Inclui ajustes para UDP, desvio de redirecionamento e roteamento, log de pacotes e parâmetros de escalonamento de processos.
- Depois de aplicar as configurações, recomenda reiniciar o sistema operacional e monitorar o servidor para medir os ganhos de performance.
