---
url: "http://elcio.com.br/pequena-dica-de-python-as-classes-sao-dinamicas/"
captured_at: "2012-12-05T10:14:27-03:00"
title: "Pequena dica de Python: as classes são dinâmicas"
domain: "elcio-com-br"
---

Veja:

  

```
 >>> class Class:  
 ...   def um(self):  
 ...     return 1  
 ...   
 >>> c=Class()  
 >>> c.um()  
 1  
 >>> def dois(self):  
 ...   return 2  
 ...   
 >>> Class.dois=dois  
 >>> c.dois()  
 2  
 >>> Class.tres=lambda self:3  
 >>> c.tres()  
 3  
 >>> Class.um=lambda self:'Um modificado.'  
 >>> c.um()  
 'Um modificado.'
```

  

As classes em Python são completamente dinâmicas. Você pode acrescentar métodos quando quiser e isso se refletirá em todos os objetos criados com aquela classe (mais ou menos como o que você faz em Javascript com prototype.)

  

[[anexo ausente]](http://feeds.feedburner.com/~ff/Fechatag?a=eKzifJEmO34:w27b2yPcsx4:yIl2AUoC8zA) [[anexo ausente]](http://feeds.feedburner.com/~ff/Fechatag?a=eKzifJEmO34:w27b2yPcsx4:D7DqB2pKExk)

  
  
  
from fechaTag [http://elcio.com.br/pequena-dica-de-python-as-classes-sao-dinamicas/?utm\_source=feedburner&utm\_medium=feed&utm\_campaign=Feed%3A+Fechatag+%28fechaTAG%29](http://elcio.com.br/pequena-dica-de-python-as-classes-sao-dinamicas/?utm_source=feedburner&amp;utm_medium=feed&amp;utm_campaign=Feed%3A+Fechatag+%28fechaTAG%29)
