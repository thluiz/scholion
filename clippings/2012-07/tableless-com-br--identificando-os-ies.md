---
url: "https://tableless.com.br/identificando-os-ies/"
captured_at: "2012-07-10T13:48:19-03:00"
title: "Identificando os IEs"
domain: "tableless-com-br"
---

Os browsers caminham para um status interessantes. Os usuários estão cada vez mais utilizando browsers mais atuais e espertos. Considere um vencedor se você não precisa mais desenvolver para IE8 e só foca seu esforço para desenvolver acima do IE9. Acontece que uma hora ou outra você vai precisar fixar alguns erros em browsers antigos. Seu cliente vai pedir, seu chefe vai chorar ou qualquer outro motivo vai te fazer resolver um bugzinho no IE7.

  

Aqui vai uma dica simples que pode salvar seu dia: adicione uma classe na tag HTML identificando o browser, assim você poderá direcionar um código para este browser específico. Fazemos isso com um código simples em Javascript ou JQuery. Veja abaixo:

  

Versão em Javascript:

  

1  
 2  
 3  
 4  
 5  
 6  
 7  
 8  
 9  
 10  
 11  
 12  
 13  
 14

  

<script type="text/javascript">  
 if (/MSIE (\d+\.\d+);/.test(navigator.userAgent)) {  
  var ieversion=new Number(RegExp.$1)  
  if (ieversion>=8)  
      // Para IE8  
      document.getElementsByTagName('html')[0].className+='ie8';  
  else if (ieversion>=7)  
      // Para IE7  
      document.getElementsByTagName('html')[0].className+='ie7';  
  else if (ieversion>=6)  
      // Para IE6  
      document.getElementsByTagName('html')[0].className+='ie6';  
 }  
 </script>

  

Versão em JQuery:

  

1  
 2  
 3  
 4  
 5  
 6  
 7  
 8  
 9  
 10  
 11  
 12

  

if ($.browser.msie) {  
     if(parseInt($.browser.version) == 8){  
          // Para IE8  
          $("html").addClass("ie8");  
     } else if(parseInt($.browser.version) == 7){  
          // Para IE7  
          $("html").addClass("ie7");  
     } else if(parseInt($.browser.version) == 6){  
          // Para IE6  
          $("html").addClass("ie6");  
     }  
 }

  

Eu prefiro usar isso a ter que usar CSS Hacks ou ter que usar comentários condicionais para adicionar uma classe na tag HTML. Assim nós precisamos sujar a sintaxe do CSS e quando quisermos retirar esse código adicional e nem sujamos muito no código HTML. Com comentários condicionais ficaria assim:

  

1  
 2  
 3  
 4  
 5  
 6  
 7  
 8  
 9  
 10  
 11  
 12  
 13  
 14  
 15  
 16  
 17  
 18  
 19

  

<!--[if IE 6]>  
 <html lang="pt-br" class="ie6">  
 <![endif]-->  
   
 <!--[if IE 7]>  
 <html lang="pt-br" class="ie7">  
 <![endif]-->  
   
 <!--[if IE 8]>  
 <html lang="pt-br" class="ie8">  
 <![endif]-->  
   
 <!--[if gte IE 8]>  
 <html lang="pt-br" class="ie9">  
 <![endif]-->  
   
 <!--[if !IE]><!-->  
 <[html](http://december.com/html/4/element/html.html) lang="pt-br">  
 <!--<![endif]-->

  

Eu acho melhor utilizar os comentários condicionais para separar os arquivos de CSS. Assim:

  

1  
 2  
 3  
 4  
 5  
 6  
 7  
 8  
 9  
 10  
 11  
 12  
 13  
 14  
 15  
 16  
 17  
 18  
 19

  

<!--[if IE 6]>  
 <link rel="stylesheet" type="text/css" href="ie6.css" />  
 <![endif]-->  
   
 <!--[if IE 7]>  
 <link rel="stylesheet" type="text/css" href="ie7.css" />  
 <![endif]-->  
   
 <!--[if IE 8]>  
 <link rel="stylesheet" type="text/css" href="ie8.css" />  
 <![endif]-->  
   
 <!--[if gte IE 8]>  
 <link rel="stylesheet" type="text/css" href="ie9.css" />  
 <![endif]-->  
   
 <!--[if !IE]><!-->  
 <[link](http://december.com/html/4/element/link.html) rel="stylesheet" type="text/css" href="application.css" />  
 <!--<![endif]-->

  

### Guerra contra o Terror

  

[Preparamos um PDF](http://tableless.com.br/browsers-antigos-guerra-contra-o-terror/) que te ajuda a convencer clientes e chefes ~~tontos~~ mostrando as deficiencias de suportarmos browsers antigos. [Dá uma olhada aqui](http://tableless.com.br/browsers-antigos-guerra-contra-o-terror/).

  

### Posts Relacionados

  

[Dicas de sobrevivência em uma era pós o IE6](http://tableless.com.br/dicas-de-sobrevivencia-ie6/)

  

[O browser que você amou odiar](http://tableless.com.br/o-browser-que-voce-amou-odiar/)

  

[Manipulação de classes com JQuery](http://tableless.com.br/manipulacao-de-classes-com-jquery/)

  

[jQuery: métodos desconhecidos](http://tableless.com.br/jquery-metodos-desconhecidos/)

  

[Entendendo os Reflows](http://tableless.com.br/entendendo-os-reflows-2/)

[![](http://feeds.feedburner.com/~ff/tableless?d=yIl2AUoC8zA)](http://feeds.feedburner.com/~ff/tableless?a=YOl9Ea4DvJk:Z5WEvvI-mjE:yIl2AUoC8zA)  [![](http://feeds.feedburner.com/~ff/tableless?i=YOl9Ea4DvJk:Z5WEvvI-mjE:D7DqB2pKExk)](http://feeds.feedburner.com/~ff/tableless?a=YOl9Ea4DvJk:Z5WEvvI-mjE:D7DqB2pKExk)  [![](http://feeds.feedburner.com/~ff/tableless?d=7Q72WNTAKBA)](http://feeds.feedburner.com/~ff/tableless?a=YOl9Ea4DvJk:Z5WEvvI-mjE:7Q72WNTAKBA)  [![](http://feeds.feedburner.com/~ff/tableless?i=YOl9Ea4DvJk:Z5WEvvI-mjE:aKCwKftKxY0)](http://feeds.feedburner.com/~ff/tableless?a=YOl9Ea4DvJk:Z5WEvvI-mjE:aKCwKftKxY0)  [![](http://feeds.feedburner.com/~ff/tableless?d=dnMXMwOfBR0)](http://feeds.feedburner.com/~ff/tableless?a=YOl9Ea4DvJk:Z5WEvvI-mjE:dnMXMwOfBR0)  [![](http://feeds.feedburner.com/~ff/tableless?d=YwkR-u9nhCs)](http://feeds.feedburner.com/~ff/tableless?a=YOl9Ea4DvJk:Z5WEvvI-mjE:YwkR-u9nhCs)  [![](http://feeds.feedburner.com/~ff/tableless?i=YOl9Ea4DvJk:Z5WEvvI-mjE:JEwB19i1-c4)](http://feeds.feedburner.com/~ff/tableless?a=YOl9Ea4DvJk:Z5WEvvI-mjE:JEwB19i1-c4)  [![](http://feeds.feedburner.com/~ff/tableless?i=YOl9Ea4DvJk:Z5WEvvI-mjE:wF9xT3WuBAs)](http://feeds.feedburner.com/~ff/tableless?a=YOl9Ea4DvJk:Z5WEvvI-mjE:wF9xT3WuBAs)  [![](http://feeds.feedburner.com/~ff/tableless?i=YOl9Ea4DvJk:Z5WEvvI-mjE:V_sGLiPBpWU)](http://feeds.feedburner.com/~ff/tableless?a=YOl9Ea4DvJk:Z5WEvvI-mjE:V_sGLiPBpWU)  [![](http://feeds.feedburner.com/~ff/tableless?i=YOl9Ea4DvJk:Z5WEvvI-mjE:tYZ39nBRSfM)](http://feeds.feedburner.com/~ff/tableless?a=YOl9Ea4DvJk:Z5WEvvI-mjE:tYZ39nBRSfM)

  
 ![](http://feeds.feedburner.com/~r/tableless/~4/YOl9Ea4DvJk)  
   
   
   
 from Tableless.com.br - Web Standards com Arroz e Feijão <http://tableless.com.br/identificando-os-ies/?utm_source=feedburner&utm_medium=feed&utm_campaign=Feed%3A+tableless+%28Tableless%29>
