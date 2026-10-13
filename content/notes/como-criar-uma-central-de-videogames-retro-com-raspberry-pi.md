---
title: "Como criar uma central de videogames retrô usando um Raspberry Pi"
date: '2015-06-05T14:10:35-03:00'
category: webclip
summary: 'Guia de montagem de um Raspberry Pi 2 com RetroPie para rodar consoles antigos, configurar controles, copiar ROMs, fazer scraper e usar save states.'
tags: ["raspberry-pi", "retropie", "emulacao", "videogames-retro"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Como criar uma central de videogames retrô usando um Raspberry Pi"
    url: "http://papodehomem.com.br/como-criar-uma-central-de-videogames-retro-usando-um-raspberry-pi/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2015-06/papodehomem-com-br--como-criar-uma-central-de-videogames-retro-com-raspberry-pi.md"
    kind: repo
---

O texto ensina a montar uma central de videogames retrô com um Raspberry Pi 2 e o RetroPie. Ele lista os componentes necessários, mostra como gravar a imagem no cartão, ligar o aparelho e ajustar controles, memória e overclock para rodar jogos antigos.

## Fichamento

- O tutorial parte da ideia de reunir jogos da infância em um mini-PC e usa um Raspberry Pi 2 com RetroPie para criar um menu de emuladores, jogos e computadores antigos.
- A montagem pede cartão microSD de 8 GB, fonte 5V 2A, cabo micro USB, HDMI, teclado e mouse USB, pendrive, leitor de cartão e um joystick USB.
- O processo começa baixando a imagem do RetroPie e gravando no cartão com o Win32DiskManager.
- Depois de ligar o Raspberry Pi na TV, o sistema identifica o joystick e leva à configuração inicial.
- O texto orienta entrar em Configure RetroArch Keyboard/Joystick para definir os botões do controle para uso nos jogos.
- Em Raspberry Pi Configuration Tool, o tutorial manda expandir o cartão, ativar o overclock na opção Pi2 e ajustar o memory split para 128.
- As ROMs são copiadas por pendrive para as pastas correspondentes de cada console.
- Após reiniciar, o emulador aparece na tela principal e a lista de jogos é exibida.
- O scraper baixa informações dos jogos pela internet para organizar título e imagem, mas pode levar horas.
- Os comandos especiais citados são Select + Start para sair do jogo, Select + B para reset, Select + X para abrir opções do emulador, Select + L2 para carregar estado e Select + R2 para salvar estado.
- O texto explica que jogos de SCUMM precisam ser copiados para a pasta SCUMM e adicionados manualmente no SCUMMVM.
- Para MAME, a ROM precisa ser da versão 0.37b5.
- Entre as observações pessoais, o autor diz que Nintendo 64 não roda bem, que Playstation 1 funciona melhor e que alguns jogos de SNES podem ter pequenos defeitos.
- O artigo também sugere formas de montar case, ligar o Raspberry Pi na TV e escolher o que jogar.
