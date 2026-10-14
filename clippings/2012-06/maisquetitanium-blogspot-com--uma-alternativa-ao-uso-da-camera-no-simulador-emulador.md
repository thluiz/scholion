---
url: "https://maisquetitanium.blogspot.com/2012/05/uma-alternativa-ao-uso-da-camera-no.html"
captured_at: "2012-06-12T15:18:08-03:00"
title: "Uma alternativa ao uso da câmera no simulador/emulador"
domain: "maisquetitanium-blogspot-com"
---

Uma das coisas chatas de trabalhar com a câmera é ter que testar seu código usando o device, já que o simulador iOS não dá suporte a câmera e o suporte do emulador Android nunca funciona como deveria (pelo menos comigo). Trabalhar com devices tem dois problema: a lentidão para o deploy e a falta de suporte a debugging.

  
  

Porém, durante o desenvolvimento, uma simples alteração numa chamada de API facilita bastante a vida na hora de testar o código que depende da câmera: ao invés de usar **Ti.Media.showCamera**, use **Ti.Media.openPhotoGallery**. Ambos recebem os mesmos parâmetros e disparam as mesmas callbacks. Assim, você pode testar seu código usando o simulador, com direito a debugging e tudo mais. A diferença é que ao invés você fazer uma foto, vai ter que selecionar uma da galeria. Depois dos testes no simulador, você volta a usar showCamera para testar no device.

  

Mas como adicionar fotos na galeria do Simulador? No iOS, arraste uma foto para cima do simulador e solte. Ela será aberta com o browser. Então, clique na imagem, segure por 1 segundo e selecione "Save" no menu que aparecerá. No emulador Android, faça uma pesquisa de imagem no Google, escolha uma imagem e salve. Ou use o [DDMS](http://developer.android.com/guide/developing/debugging/ddms.html) para transferir arquivos do seu computador.

  

Essas dicas economizam muito do meu tempo, espero que economizem o seu também. :)

  

—

  

Se você gosta dos meus artigos, é provável que também gostará dos meus tweets. Siga [@DirleiDionisio](http://twitter.com/DirleiDionisio) no Twitter!

  
[anexo ausente]

  
  
  
from Mais que Titanium <http://maisquetitanium.blogspot.com/2012/05/uma-alternativa-ao-uso-da-camera-no.html>
