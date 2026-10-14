---
url: "http://tableless.com.br/criando-um-plugin-javascript-sem-jquery/"
captured_at: "2012-11-07T09:20:31-03:00"
title: "Criando um plugin JavaScript (sem jQuery!)"
domain: "tableless-com-br"
---

Neste artigo vamos criar um slider de imagens utilizando apenas JavaScript e CSS3, sem nenhuma biblioteca. O resultado final é um script de aproximadamente 160 linhas e menos de 3kb minificado. Poderia ser menor do que isso, mas nosso código vai ser extensível e 100% válido em uma [verificação JSLint](http://tableless.com.br/qualidade-codigo-javascript/).

  
 

---

[Um plugin jQuery](http://tableless.com.br/anatomia-de-um-plugin-jquery/) é basicamente um código que pode ser aplicado em um ou mais elementos do DOM. Para justificar sua existência, um plugin precisa ser, principalmente, flexível.

  

O objetivo final é podermos instanciar nosso plugin com a seguinte chamada:

  

1

  

var slider = new JSlider('.slider');

  

Antes de tudo vamos precisar de um pequeno trecho de CSS que garantirá o estilo básico do nosso slider.

  

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
 20  
 21  
 22  
 23  
 24  
 25  
 26  
 27  
 28  
 29  
 30  
 31  
 32

  

.jslider-stage {  
     position: relative;  
 }  
   
 .jslider-track {  
     overflow: hidden;  
 }  
   
 .jslider-track ul {  
     transition: margin-left .5s ease;  
     -webkit-transition: margin-left .5s ease;  
     -moz-transition: margin-left .5s ease;  
     -o-transition: margin-left .5s ease;  
 }  
   
 .jslider-track ul li {  
     display: table-cell;  
     text-align: center;  
     vertical-align: middle;  
 }  
   
 .jslider-navigation {  
     position: absolute;  
     top: 0;  
     width: 60px;  
     height: 80px;  
     background: #000;  
     color: #fff;  
 }  
 .jslider-stage .left {  
     left: 0;  
 }

  

Não vou explicar muito as declarações acima já que o nosso foco principal é o código JavaScript. O mais importante é que toda a parte de animação, responsável pelas transições entre imagens, é feita via CSS3, representando um belo ganho de performance:

  

1  
 2  
 3  
 4  
 5  
 6

  

.jslider-track ul {  
     transition: margin-left .5s ease;  
     -webkit-transition: margin-left .5s ease;  
     -moz-transition: margin-left .5s ease;  
     -o-transition: margin-left .5s ease;  
 }

  

Pensando um pouco na composição do código do nosso plugin, vamos criar dois objetos: um que será responsável pelo plugin em si e outro para representar cada slider instanciado na página. O próximo passo, então, é criar duas funções construtoras para nossos objetos:

  

1  
 2  
 3  
 4  
 5  
 6  
 7  
 8

  

function JSlider(selector) {  
     this.init(selector);  
 }  
   
 function JSliderStage(el) {  
     this.doc = document;  
     this.init(el);  
 }

  

JSlider é o objeto do nosso plugin que armazenará um ou mais objetos JSliderStage.

  

O objeto JSlider possui um único método, *init*, responsável por inicializar nosso plugin e os objetos do tipo stage. Este método receberá um único parâmetro, o seletor no qual aplicaremos o plugin.

  

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

  

JSlider.prototype.init = function (selector) {  
     var elements = document.querySelectorAll(selector),  
         i;  
   
     this.slidersList = [];  
   
     if (elements.length < 1) {  
         return;  
     }  
   
     for (i = 0; i < elements.length; i += 1) {  
         this.slidersList.push(new JSliderStage(elements[i]));  
     }  
 };

  

Não existem classes em JavaScript, tudo é um objeto. No entanto, com o uso de prototypes, conseguimos criar objetos que servem como modelos. Ao adicionar um método ao prototype de um objeto, todas as instâncias que compartilham o mesmo prototype automaticamente herdam este novo método.

  

Agora chegou a hora de estruturarmos o objeto responsável pelo slider em si. Vamos, antes de tudo, montar uma lista das funcionalidades a serem implementadas.

  

  

inicialização, listando as imagens encontradas no seletor;

  

construção do “palco”, definindo as dimensões de acordo com a maior foto;

  

construção do “trilho” e carregamento das imagens;

  

construção e inicialização da navegação entre imagens e

  

carregamento de uma nova página.

  

O palco “esconde” boa parte do trilho que armazena as imagens, exibindo apenas a imagem atual. Ao clicar nos botões de navegação, o usuário desloca esse trilho no eixo X.

  

### querySelectorAll

  

O método *querySelectorAll*, nativo do JavaScript, tem funcionamento parecido com um seletor jQuery, podendo receber tanto um id como uma classe. Primeiro verificamos se foi encontrado algum elemento e depois instanciamos os objetos JSliderStage para cada elemento encontrado.

  

## 1. Inicialização

  

A função de inicialização é responsável por configurar os valores padrões de algumas variáveis e listar as imagens disponíveis no elemento pai. Caso não exista nenhuma imagem, nosso plugin cancela qualquer execução.

  

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

  

JSliderStage.prototype.init = function (el) {  
     this.root = el;  
     this.currentPage = 1;  
     this.images = this.root.querySelectorAll('img');  
   
     if (this.images.length === 0) {  
         return;  
     }  
   
     this.build();  
 };

  

## 2. Palco

  

Para construir o palco precisamos definir uma largura e uma altura máxima, baseada nas maiores imagens – é isso que o método *getPageDimensions* faz.

  

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
 20  
 21  
 22  
 23  
 24  
 25  
 26  
 27  
 28  
 29  
 30  
 31  
 32  
 33

  

JSliderStage.prototype.build = function () {  
     this.getPageDimensions()  
         .createStage()  
         .initNavigation();  
     this.root.innerHTML = '';  
     this.root.appendChild(this.stage);  
 };  
   
 JSliderStage.prototype.getPageDimensions = function () {  
     var i;  
     this.pageWidth = this.pageHeight = 0;  
     for (i = 0; i  this.pageWidth) {  
             this.pageWidth = this.images[i].width;  
         }  
         if (this.images[i].height > this.pageHeight) {  
             this.pageHeight = this.images[i].height;  
         }  
     }  
     return this;  
 };  
   
 JSliderStage.prototype.createStage = function () {  
     this.stage = this.doc.createElement('div');  
     this.stage.className = 'jslider-stage';  
     this.stage.style.width = this.pageWidth + 'px';  
   
     this.buildTrack()  
         .loadImages();  
   
     this.stage.appendChild(this.sliderTrack);  
   
     return this;  
 };

  

O método *createStage* adiciona ao DOM os elementos necessários para nosso palco e executa dois outros métodos: um para carregar o trilho e outro para carregar as imagens. Por fim, iniciamos a navegação com o método *initNavigation*.

  

### createElement

  

Este método da API JavaScript permite a criação de elementos que depois podem ser inseridos na árvore do DOM. É recomendado, por questões de performance, finalizar toda e qualquer manipulação antes de adicionar o elemento ao DOM.

  

### appendChild

  

O método appendChild adiciona um elemento criado a outro já existente na árvore do DOM. É semelhante aos métodos append/appendTo do jQuery.

  

## 3. Trilho

  

Nosso trilho é um elemento DIV com uma lista (UL) contendo as imagens do slider. A largura do DIV corresponde à largura da maior imagem, enquanto que a largura da lista representa a soma da largura de todas as imagens. Dessa forma, através do nosso CSS lá do início, a lista de imagens fica “escondida” atrás da DIV principal do trilho.

  

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
 20  
 21  
 22  
 23  
 24

  

JSliderStage.prototype.buildTrack = function () {  
     this.sliderTrack = this.doc.createElement('div');  
     this.sliderTrack.className = 'jslider-track';  
     this.sliderTrack.style.height = this.pageHeight + 'px';  
     return this;  
 };  
   
 JSliderStage.prototype.loadImages = function () {  
     var i,  
         li;  
   
     this.imageList = this.doc.createElement('ul');  
     this.imageList.style.width = (this.images.length \* this.pageWidth) + 'px';  
   
     for (i = 0; i < this.images.length; i += 1) {  
         li = this.doc.createElement('li');  
         li.style.width = this.pageWidth + 'px';  
         li.style.height = this.pageHeight + 'px';  
         li.appendChild(this.images[i]);  
         this.imageList.appendChild(li);  
     }  
   
     this.sliderTrack.appendChild(this.imageList);  
 };

  

## 4. Navegação

  

Finalizando nosso slide, precisamos implementar a navegação entre imagens. O método *initNavigation* cria, caso necessário, os botões de anterior e próximo.

  

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
 20  
 21  
 22  
 23  
 24  
 25  
 26  
 27  
 28  
 29  
 30  
 31  
 32  
 33  
 34  
 35  
 36

  

JSliderStage.prototype.initNavigation = function () {  
     var positionTop = ((this.pageHeight / 2) - 40) + 'px';  
   
     if (this.images.length < 2) {  
         return this;  
     }  
   
     this.createNavigationButton('left', positionTop)  
         .createNavigationButton('right', positionTop);  
   
     this.navButtonsList = this.stage.querySelectorAll('.jslider-navigation');  
   
     return this;  
 };  
   
 JSliderStage.prototype.createNavigationButton = function (direction, positionTop) {  
     var navButton = this.doc.createElement('a'),  
         self = this,  
         slidingLeft = (direction === 'left'),  
         page;  
   
     navButton.className = 'jslider-navigation ' + direction + (slidingLeft ? ' off' : '');  
     navButton.style.top = positionTop;  
     navButton.href = '#';  
     navButton.innerHTML = (slidingLeft ? '‹' : '›');  
   
     navButton.onclick = function (e) {  
         e.preventDefault();  
         page = (slidingLeft ? self.currentPage - 1 : self.currentPage + 1);  
         self.gotoPage(page);  
     };  
   
     this.stage.appendChild(navButton);  
   
     return this;  
 };

  

Já o método *gotoPage* é responsável por carregar a imagem correta e habilitar/desabilitar os botões de navegação de acordo com a imagem atual.

  

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
 20  
 21  
 22  
 23  
 24  
 25

  

JSliderStage.prototype.gotoPage = function (page) {  
     var marginLeft = (-1) \* ((page - 1) \* this.pageWidth);  
     if (page  this.images.length) {  
         return;  
     }  
   
     this.setNavigationState(page);  
   
     this.imageList.style.marginLeft = marginLeft + 'px';  
     this.currentPage = page;  
 };  
   
 JSliderStage.prototype.setNavigationState = function (page) {  
     if (page === 1) {  
         this.navButtonsList[0].classList.add('off');  
         this.navButtonsList[1].classList.remove('off');  
     } else {  
         this.navButtonsList[0].classList.remove('off');  
         if (page === this.images.length) {  
             this.navButtonsList[1].classList.add('off');  
         } else {  
             this.navButtonsList[1].classList.remove('off');  
         }  
     }  
 };

  

### escopo

  

No método *createNavigationButton* armazenamos o objeto *this* na variável self. Isso é necessário porque precisamos referenciar o escopo anterior quando associamos a navegação no evento de clique dos links. Se tivéssemos utilizado diretamente o *this*, estaríamos referenciando o escopo do clique, o que não era nosso objetivo. Além de self, é comum encontrar nomes como instance e that em variáveis que armazenam o escopo atual de um método.

  

### classList

  

A propriedade classList permite a manipulação de classes em um elemento do DOM. Podemos consultar, remover a adicionar novas classes. Os métodos addClass e removeClass do jQuery utilizam essa propriedade. [CONFIRMAR]

  

## TODO

  

É claro que o código final é bem simples, mas a ideia principal era mostrar que nem sempre precisamos utilizar jQuery em nossas aplicações, mesmo com o jQuery disponível na estrutura do projeto.

  

Finalizando, algumas melhorias que ficam de dever de casa para vocês:

  

temporizador para trocar imagens, sendo configurável na inicialização do plugin

  

suporte a browsers mais antigos, mantendo a funcionalidade

  

carregamento de qualquer conteúdo nos slides, não só imagens

  

navegação via teclado

  

exibir miniaturas navegáveis

  

[escrever testes com Jasmine](http://tableless.com.br/testando-seu-codigo-jquery-com-jasmine-parte-1/)

## Código completo do plugin

  

[Nosso plugin em ação no jsFiddle](http://jsfiddle.net/jnQJu/)

  

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
 20  
 21  
 22  
 23  
 24  
 25  
 26  
 27  
 28  
 29  
 30  
 31  
 32  
 33  
 34  
 35  
 36  
 37  
 38  
 39  
 40  
 41  
 42  
 43  
 44  
 45  
 46  
 47  
 48  
 49  
 50  
 51  
 52  
 53  
 54  
 55  
 56  
 57  
 58  
 59  
 60  
 61  
 62  
 63  
 64  
 65  
 66  
 67  
 68  
 69  
 70  
 71  
 72  
 73  
 74  
 75  
 76  
 77  
 78  
 79  
 80  
 81  
 82  
 83  
 84  
 85  
 86  
 87  
 88  
 89  
 90  
 91  
 92  
 93  
 94  
 95  
 96  
 97  
 98  
 99  
 100  
 101  
 102  
 103  
 104  
 105  
 106  
 107  
 108  
 109  
 110  
 111  
 112  
 113  
 114  
 115  
 116  
 117  
 118  
 119  
 120  
 121  
 122  
 123  
 124  
 125  
 126  
 127  
 128  
 129  
 130  
 131  
 132  
 133  
 134  
 135  
 136  
 137  
 138  
 139  
 140  
 141  
 142  
 143  
 144  
 145  
 146  
 147  
 148  
 149  
 150  
 151  
 152  
 153  
 154  
 155  
 156  
 157  
 158  
 159  
 160

  

/\*jslint browser:true \*/  
 'use strict';  
   
 function JSlider(selector) {  
     this.init(selector);  
 }  
   
 function JSliderStage(el) {  
     this.doc = document;  
     this.init(el);  
 }  
   
 JSlider.prototype.init = function (selector) {  
     var elements = document.querySelectorAll(selector),  
         i;  
   
     this.slidersList = [];  
   
     if (elements.length < 1) {  
         return;  
     }  
   
     for (i = 0; i < elements.length; i += 1) {  
         this.slidersList.push(new JSliderStage(elements[i]));  
     }  
 };  
   
 JSliderStage.prototype.init = function (el) {  
     this.root = el;  
     this.currentPage = 1;  
     this.images = this.root.querySelectorAll('img');  
   
     if (this.images.length === 0) {  
         return;  
     }  
   
     this.build();  
 };  
   
 JSliderStage.prototype.build = function () {  
     this.getPageDimensions()  
         .createStage()  
         .initNavigation();  
     this.root.innerHTML = '';  
     this.root.appendChild(this.stage);  
 };  
   
 JSliderStage.prototype.getPageDimensions = function () {  
     var i;  
     this.pageWidth = this.pageHeight = 0;  
     for (i = 0; i  this.pageWidth) {  
             this.pageWidth = this.images[i].width;  
         }  
         if (this.images[i].height > this.pageHeight) {  
             this.pageHeight = this.images[i].height;  
         }  
     }  
     return this;  
 };  
   
 JSliderStage.prototype.createStage = function () {  
     this.stage = this.doc.createElement('div');  
     this.stage.className = 'jslider-stage';  
     this.stage.style.width = this.pageWidth + 'px';  
   
     this.buildTrack()  
         .loadImages();  
   
     this.stage.appendChild(this.sliderTrack);  
   
     return this;  
 };  
   
 JSliderStage.prototype.buildTrack = function () {  
     this.sliderTrack = this.doc.createElement('div');  
     this.sliderTrack.className = 'jslider-track';  
     this.sliderTrack.style.height = this.pageHeight + 'px';  
     return this;  
 };  
   
 JSliderStage.prototype.loadImages = function () {  
     var i,  
         li;  
   
     this.imageList = this.doc.createElement('ul');  
     this.imageList.style.width = (this.images.length \* this.pageWidth) + 'px';  
   
     for (i = 0; i < this.images.length; i += 1) {  
         li = this.doc.createElement('li');  
         li.style.width = this.pageWidth + 'px';  
         li.style.height = this.pageHeight + 'px';  
         li.appendChild(this.images[i]);  
         this.imageList.appendChild(li);  
     }  
   
     this.sliderTrack.appendChild(this.imageList);  
 };  
   
 JSliderStage.prototype.initNavigation = function () {  
     var positionTop = ((this.pageHeight / 2) - 40) + 'px';  
   
     if (this.images.length < 2) {  
         return this;  
     }  
   
     this.createNavigationButton('left', positionTop)  
         .createNavigationButton('right', positionTop);  
   
     this.navButtonsList = this.stage.querySelectorAll('.jslider-navigation');  
   
     return this;  
 };  
   
 JSliderStage.prototype.createNavigationButton = function (direction, positionTop) {  
     var navButton = this.doc.createElement('a'),  
         self = this,  
         slidingLeft = (direction === 'left'),  
         page;  
   
     navButton.className = 'jslider-navigation ' + direction + (slidingLeft ? ' off' : '');  
     navButton.style.top = positionTop;  
     navButton.href = '#';  
     navButton.innerHTML = (slidingLeft ? '‹' : '›');  
   
     navButton.onclick = function (e) {  
         e.preventDefault();  
         page = (slidingLeft ? self.currentPage - 1 : self.currentPage + 1);  
         self.gotoPage(page);  
     };  
   
     this.stage.appendChild(navButton);  
   
     return this;  
 };  
   
 JSliderStage.prototype.gotoPage = function (page) {  
     var marginLeft = (-1) \* ((page - 1) \* this.pageWidth);  
     if (page  this.images.length) {  
         return;  
     }  
   
     this.setNavigationState(page);  
   
     this.imageList.style.marginLeft = marginLeft + 'px';  
     this.currentPage = page;  
 };  
   
 JSliderStage.prototype.setNavigationState = function (page) {  
     if (page === 1) {  
         this.navButtonsList[0].classList.add('off');  
         this.navButtonsList[1].classList.remove('off');  
     } else {  
         this.navButtonsList[0].classList.remove('off');  
         if (page === this.images.length) {  
             this.navButtonsList[1].classList.add('off');  
         } else {  
             this.navButtonsList[1].classList.remove('off');  
         }  
     }  
 };

  

### Posts Relacionados

  

[Anatomia de um plugin jQuery](http://tableless.com.br/anatomia-de-um-plugin-jquery/)

  

[Adobe Edge](http://tableless.com.br/adobe-edge/)

  

[Underscore.js: cinto de utilidades JavaScript](http://tableless.com.br/underscore-js-cinto-de-utilidades-javascript/)

  

[Criando uma aplicação simples com AngularJS](http://tableless.com.br/criando-uma-aplicacao-simples-com-angularjs/)

  

[Retina.js – Imagens para telas retina](http://tableless.com.br/retina-js-imagens-para-telas-retina/)

  
   
 from Tableless.com.br - Web Standards com Arroz e Feijão <http://tableless.com.br/criando-um-plugin-javascript-sem-jquery/>
