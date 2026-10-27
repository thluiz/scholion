---
title: "Pequena dica de Python: módulo webbrowser"
date: '2013-01-21T14:03:39-03:00'
category: webclip
summary: 'O módulo webbrowser abre uma URL no navegador do usuário. Em scripts de terminal, ele usa o navegador padrão na interface gráfica ou um navegador de linha de comando se não houver ambiente gráfico.'
tags: ["python", "webbrowser", "terminal"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Pequena dica de Python: módulo webbrowser"
    url: "https://elcio.com.br/pequena-dica-de-python-modulo-webbrowser/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2013-01/elcio-com-br--pequena-dica-de-python-modulo-webbrowser.md"
    kind: repo
---

O módulo webbrowser serve para abrir uma URL no navegador do usuário. A postagem mostra um exemplo simples com webbrowser.open("http://visie.com.br") e diz que isso é útil em programas de desktop e em scripts de terminal.

## Fichamento

- O módulo webbrowser abre uma URL no navegador do usuário.
- O exemplo usa webbrowser.open("http://visie.com.br") para abrir o site da Visie.
- Em programas de desktop, o uso é apresentado como útil.
- Em scripts de terminal, se houver interface gráfica, o site abre no navegador padrão do usuário.
- Se o script estiver rodando via ssh ou em outro terminal sem interface gráfica, o sistema usa um navegador de CLI, como o Lynx, se ele estiver disponível.
