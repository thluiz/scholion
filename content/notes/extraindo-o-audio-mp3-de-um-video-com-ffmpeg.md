---
title: "Extraindo o áudio MP3 de um vídeo com ffmpeg"
date: '2012-05-08T10:27:57-03:00'
category: webclip
summary: 'Mostra como converter um vídeo em MP3 com ffmpeg usando um comando simples, depois de explicar por que ouvir videopodcasts em áudio é mais prático no carro.'
tags: ["ffmpeg", "mp3", "audio-de-video"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Extraindo o áudio MP3 de um vídeo com ffmpeg"
    url: "http://elcio.com.br/extraindo-o-audio-mp3-de-um-video-com-ffmpeg/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2012-05/elcio-com-br--extraindo-o-audio-mp3-de-um-video-com-ffmpeg.md"
    kind: repo
---

O texto diz que ouvir videopodcasts no carro torna o vídeo dispensável, então ter os arquivos em MP3 é mais prático. Também menciona o uso do Easy YouTube Video Downloader para baixar vídeos e a ideia de automatizar esse processo com Miro.

## Fichamento

- Videopodcasts em vídeo perdem relevância quando serão ouvidos no carro, então a versão em MP3 fica mais útil.
- O autor diz que usa o Easy YouTube Video Downloader para baixar os vídeos.
- O próximo projeto pessoal dele é automatizar o download, talvez com Miro.
- Para extrair apenas o áudio em MP3, ele usa o comando `ffmpeg -i entrada_video.mp4 -vn saida_audio.mp3`.
- Ele descreve o comando como simples, rápido e fácil de automatizar.
