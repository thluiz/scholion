---
title: "Uma alternativa ao uso da câmera no simulador/emulador"
date: '2012-06-12T15:18:08-03:00'
category: webclip
summary: 'Trocar Ti.Media.showCamera por Ti.Media.openPhotoGallery permite testar código com câmera no simulador, com as mesmas callbacks e parâmetros, e depois voltar ao device.'
tags: ["camera", "simulador", "emulador", "titanium"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Uma alternativa ao uso da câmera no simulador/emulador"
    url: "https://maisquetitanium.blogspot.com/2012/05/uma-alternativa-ao-uso-da-camera-no.html"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2012-06/maisquetitanium-blogspot-com--uma-alternativa-ao-uso-da-camera-no-simulador-emulador.md"
    kind: repo
---

Durante o desenvolvimento, a página propõe trocar Ti.Media.showCamera por Ti.Media.openPhotoGallery para testar código que depende da câmera no simulador. A ideia funciona porque os dois métodos recebem os mesmos parâmetros e disparam as mesmas callbacks, permitindo usar debugging no simulador antes de voltar a showCamera no device.

## Fichamento

- Trabalhar com a câmera obriga a testar no device, porque o simulador iOS não oferece suporte e o emulador Android costuma falhar.
- Testar em devices traz lentidão no deploy e falta de debugging.
- Durante o desenvolvimento, substituir Ti.Media.showCamera por Ti.Media.openPhotoGallery facilita os testes.
- Os dois métodos recebem os mesmos parâmetros e acionam as mesmas callbacks.
- No simulador, em vez de tirar foto, o teste usa uma imagem escolhida da galeria.
- Depois dos testes no simulador, a orientação é voltar a usar showCamera no device.
- No iOS, é possível adicionar fotos ao simulador arrastando uma imagem para ele, abrindo-a no browser e salvando a imagem.
- No emulador Android, a página sugere buscar uma imagem no Google e salvá-la, ou usar DDMS para transferir arquivos do computador.
