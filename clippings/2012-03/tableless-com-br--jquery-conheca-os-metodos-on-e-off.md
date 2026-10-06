---
url: "https://tableless.com.br/jquery-conheca-os-metodos-on-e-off/"
captured_at: "2012-03-13T20:34:35-03:00"
title: "jQuery: conheça os métodos on() e off()"
domain: "tableless-com-br"
---

### Sent to you by Thiago Silva via Google Reader:

## 

[jQuery: conheça os métodos on() e off()](http://feedproxy.google.com/~r/tableless/~3/yL1K5BiqEnA/)

via [Tableless.com.br - Web Standards com Arroz e Feijão](http://tableless.com.br) by diego@tableless.com.br (Tableless.com.br) on 3/13/12

  

Em outubro de 2010 escrevi um [artigo](http://tableless.com.br/associando-eventos-dinamicamente/ "jQuery: associando eventos dinamicamente") aqui mesmo no Tableless sobre a associação dinâmica de eventos. Na época, reinava uma confusão sobre quais métodos utilizar e quando utilizá-los. Eram três as opções: bind(), live() e delegate().

Com o lançamento da versão 1.7 do jQuery, dois métodos definitivos (assim espero) devem acabar com a confusão em torno da associação de eventos: os métodos on() e off().

## Eventos diretos

A associação direta de eventos ocorre quando o seletor (ou escopo) é omitido nos parâmetros do on(). Por exemplo:

|  |  |
| --- | --- |
| 1 2 3 4 5 | function exibeMenu(e) {    e.preventDefault();    $('#menu').[show](http://docs.jquery.com/Effects/show)();  }  $('#lnk-menu').on('click', exibeMenu); |

No código acima, o elemento com id #lnk-menu recebe uma associação no evento click para executar a função exibeMenu(). A associação ocorre de forma direta, ou seja, quando o on() é executado o evento passa a estar associado ao elemento, antes mesmo do clique ocorrer.

Essa opção equivale ao bind() e deve ser utilizada em casos de elementos únicos, ou com poucos elementos, para evitar problemas de performance.

## Múltiplos eventos

Também é possível associar múltiplos eventos a um ou mais elementos. Para isso, basta passar um mapa onde cada chave representa um evento ao invés de um evento como string:

|  |  |
| --- | --- |
| 1 2 3 4 5 6 7 8 9 10 11 | $('#lnk-menu').on({    [click](http://docs.jquery.com/Events/click): function(){      $('#menu').[show](http://docs.jquery.com/Effects/show)();    },    [dblclick](http://docs.jquery.com/Events/dblclick): function(){      $('#submenu').[show](http://docs.jquery.com/Effects/show)();    },    [mouseenter](http://docs.jquery.com/Events/mouseenter): function(){      $(this).[addClass](http://docs.jquery.com/Attributes/addClass)('ativo');    }  }); |

## Removendo associações de eventos diretos

Remover associações de eventos diretos é simples:

|  |  |
| --- | --- |
| 1 | $('#lnk-menu').off(); |

Para remover eventos específicos, mantendo qualquer outra associação, basta informar o nome do evento:

|  |  |
| --- | --- |
| 1 | $('#lnk-menu').off('click'); |

## Eventos delegados

A delegação de eventos (antigos live() e delegate()) ocorre quando passamos um ou mais seletores nos parâmetros do on. O evento não será  
associado diretamente quando o código for executado, tampouco será executado para o seletor que chama o on() e sim para os elementos descendentes que se encaixem no parâmetro passado.

A associação ocorre quando o evento é acionado. Esse tipo de associação funciona tanto para elementos já presentes no DOM como para elementos criados posteriormente.

|  |  |
| --- | --- |
| 1 2 3 4 5 | function exibeConteudo(e){    $(this).[find](http://docs.jquery.com/Traversing/find)('conteudo').[fadeIn](http://docs.jquery.com/Effects/fadeIn)();  }    $('table').on('click', 'a', exibeConteudo); |

## Removendo a associação de eventos específicos

Em alguns momentos será preciso associar eventos diretos e, ao mesmo tempo, delegar eventos. Nesses casos, é possível remover apenas os eventos delegados utilizando o parâmetro especial “\*\*”.

|  |  |
| --- | --- |
| 1 | $('a').off('click', '\*\*'); |

Outra opção é remover a associação com base na função utilizada:

|  |  |
| --- | --- |
| 1 | $('#lnk-menu').off('click', 'a', exibeConteudo); |

## Namespaces

Uma importante implementação do on() é a possibilidade de utilizar namespaces nos eventos – uma grande novidade para desenvolvedores de plugins. Um evento pode, agora, ser associado a um namespace específico, facilitando o controle sobre associações específicas de um plugin ou uma funcionalidade.

|  |  |
| --- | --- |
| 1 2 3 4 | $('#lnk-menu').on('click.menu', exibeMenu);  $('.menu-item').on('mouseleave.menu', escondeMenu);    $('#lnk-menu, .menu-item').off('.menu'); |

## Enviando dados para o evento

O método on() também permite enviar dados específicos para um evento. O objeto de dados fica associado ao objeto do evento.

|  |  |
| --- | --- |
| 1 2 3 4 5 6 | function exibeMenu(e) {     $('.ativo').[text](http://docs.jquery.com/Attributes/text)(e.[data](http://docs.jquery.com/Core/data).descricao);  }    $('#lnk-home').on('click', { descricao: 'Página inicial' }, exibeMenu);  $('#lnk-sobre').on('click', { descricao: 'Sobre a empresa' }, exibeMenu); |

No exemplo acima, cada link passa uma descrição diferente durante o evento. Essa descrição passa a ser o conteúdo dos elementos com a classe “.ativo”.

## Este evento se autodestruirá…

O método .one() poderia ter entrado na lista dos [métodos desconhecidos do meu último artigo](http://tableless.com.br/jquery-metodos-desconhecidos/ "jQuery: métodos desconhecidos"), já que existe desde a versão 1.1 do jQuery. No entanto, junto com a implementação do .on() ele ganhou uma nova cara.

Sua implementação segue as mesmas regras do .on() com uma importante diferença: o evento associado é executado apenas uma vez. Após a execução a associação é automaticamente removida, seja ela uma associação direta ou delegada.

|  |  |
| --- | --- |
| 1 2 3 | $('#lnk-menu').[one](http://docs.jquery.com/Events/one)('click', function() {    alert('Este evento não será mais executado.');  }); |

Caso o seletor possua mais de um elemento, o evento será associado uma vez a cada um deles, ou seja, cada elemento possuirá uma execução do evento.

---

Essas são as novidades com relação a eventos utilizando jQuery. Os métodos .on() e .off() devem “matar” seus antecessores (.live() e .delegate()) e padronizar de uma vez por todas a associação de eventos em aplicações.

### Posts Relacionados

- [Navegando com a jQuery](http://tableless.com.br/navegando-com-a-jquery/ "Navegando com a jQuery")
- [Manipulação de classes com JQuery](http://tableless.com.br/manipulacao-de-classes-com-jquery/ "Manipulação de classes com JQuery")
- [jQuery: métodos desconhecidos](http://tableless.com.br/jquery-metodos-desconhecidos/ "jQuery: métodos desconhecidos")
- [20 plugins jQuery que marcaram 2011](http://tableless.com.br/20-plugins-jquery-que-marcaram-2011/ "20 plugins jQuery que marcaram 2011")
- [Testando seu código jQuery com Jasmine – Parte 1](http://tableless.com.br/testando-seu-codigo-jquery-com-jasmine-parte-1/ "Testando seu código jQuery com Jasmine – Parte 1")

[[anexo ausente]](http://feeds.feedburner.com/~ff/tableless?a=yL1K5BiqEnA:uZQaaTsx9NI:yIl2AUoC8zA) [![95f22289de1325f5828caf402adfbae1.gif](tableless-com-br--jquery-conheca-os-metodos-on-e-off/95f22289de1325f5828caf402adfbae1.gif)](http://feeds.feedburner.com/~ff/tableless?a=yL1K5BiqEnA:uZQaaTsx9NI:D7DqB2pKExk) [[anexo ausente]](http://feeds.feedburner.com/~ff/tableless?a=yL1K5BiqEnA:uZQaaTsx9NI:7Q72WNTAKBA) [[anexo ausente]](http://feeds.feedburner.com/~ff/tableless?a=yL1K5BiqEnA:uZQaaTsx9NI:aKCwKftKxY0) [[anexo ausente]](http://feeds.feedburner.com/~ff/tableless?a=yL1K5BiqEnA:uZQaaTsx9NI:dnMXMwOfBR0) [![461e440a1d3becc7e11e0f65f4ce18e3.gif](tableless-com-br--jquery-conheca-os-metodos-on-e-off/461e440a1d3becc7e11e0f65f4ce18e3.gif)](http://feeds.feedburner.com/~ff/tableless?a=yL1K5BiqEnA:uZQaaTsx9NI:YwkR-u9nhCs) [[anexo ausente]](http://feeds.feedburner.com/~ff/tableless?a=yL1K5BiqEnA:uZQaaTsx9NI:JEwB19i1-c4) [[anexo ausente]](http://feeds.feedburner.com/~ff/tableless?a=yL1K5BiqEnA:uZQaaTsx9NI:wF9xT3WuBAs) [[anexo ausente]](http://feeds.feedburner.com/~ff/tableless?a=yL1K5BiqEnA:uZQaaTsx9NI:V_sGLiPBpWU) [![f8ff8d12b338a41748c29ac226ea526f.gif](tableless-com-br--jquery-conheca-os-metodos-on-e-off/f8ff8d12b338a41748c29ac226ea526f.gif)](http://feeds.feedburner.com/~ff/tableless?a=yL1K5BiqEnA:uZQaaTsx9NI:tYZ39nBRSfM)

[anexo ausente]

  

### Things you can do from here:

- [Subscribe to Tableless.com.br - Web Standards com Arroz e Feijão](http://www.google.com/reader/view/feed%2Fhttp%3A%2F%2Ffeeds.feedburner.com%2Ftableless?source=email) using **Google Reader**
- [Get started using Google Reader](http://www.google.com/reader/?source=email) to easily keep up with **all your favorite sites**
