---
url: "https://imasters.com.br/apis-microsservicos/screenshot-com-canvas-e-javascript"
captured_at: "2012-05-24T18:22:41-03:00"
title: "html2canvas: captura de tela do navegador"
domain: "imasters-com-br"
---

Salve salve pessoal!
At pouco tempo atrs era impossvel realizar print-screens das telas de um browser utilizando javascript. Ou voc fazia um executvel ou utilizava algum componente activeX ou similar.
Com o advento do html5 novas tags foram implementadas um deles o canvas que possibilita realizar essa tarefa.
Com o elemento canvas voc pode criar grficos composies de fotos animaes imagens 2D 3D e existem vrias APIs que te fornecem inmeros recursos como a html2canvas e esta API que vamos trabalhar.
Primeiramente vamos entrar no site e baixar o arquivo. Imagino que voc j tenha baixado o arquivo jquery.js
lt;script src=quot;Scripts/html2canvas.jsquot; type=quot;text/javascriptquot;gt;lt;/scriptgt;
O html2canvas tem um mtodo inicial chamado Preload que recebe dois parmetros.
Element: o elemento que voc deseja estar renderizando por default document.body
Options: So as opes de renderizao.
Complete: funo callback que ser chamada depois do Preloading
Logging: Loga os eventos no console
Proxy: Url da pgina que vai ser usada como proxy
Timeout: Tempo para carregamento das imagens
O script executa o seguinte comportamento.
Executar o Preload da pgina
Executar o Parse dos Elementos
Executar o Render do Objeto
Vamos ao cdigo:
lt;scriptgt; $(window).ready(function () { html2canvas.Preload(document.body { complete: function (images) { var queue = html2canvas.Parse(); var canvas = html2canvas.Renderer(queue { elements: { length: 1} }); var img = canvas.toDataURL(); openConsole(quot;lt;img src='quot; img quot;'gt;lt;pgt;quot;); } }); function openConsole(content) { top.console = window.open('' 'myconsole' 'width=350height=250' 'menubar=0' 'toolbar=1' 'status=0' 'scrollbars=1' 'resizable=1') top.console.document.writeln( 'lt;htmlgt;lt;headgt;lt;titlegt;Consolelt;/titlegt;lt;/headgt;' 'lt;body bgcolor=white onLoad=quot;self.focus()quot;gt;' content 'lt;/bodygt;lt;/htmlgt;' ) top.console.document.close() }; }); lt;/scriptgt;
Um exemplo mais avanado: Vamos recuperar um print de um site
var proxyUrl = quot;http://html2canvas.appspot.comquot;; $(window).ready(function () { var a b; $.ajax({ data: { xhr2: false url: quot;http://www.globo.comquot; } url: proxyUrl dataType: quot;jsonpquot; success: function (e) { a = document.createElement(quot;iframequot;); document.body.appendChild(a); $(a).width(quot;700quot;).height(quot;500quot;); b = a.contentWindow.document; b.open(); b.write(e); b.close() $(a.contentWindow).load(function () { var g = $(a).contents().find(quot;bodyquot;)[0]; var preload = html2canvas.Preload(g { quot;completequot;: function (images) { var queue = html2canvas.Parse(g images); var canvas = $(html2canvas.Renderer(queue { elements: { length: 10} })); var img = canvas[0].toDataURL(); openConsole(quot;lt;img src='quot; img quot;'gt;lt;pgt;quot;); } }); }); } }) });
Veja: http://testes.felipehuggler.com/screenshot/
Lembrando que os browsers que aceitam canvas so Chrome FF Opera e IE7
O site Can I Use tem a lista dos elementos que so compatveis com cada browser.
Espero que seja til!
At o prximo
from iMasters - http://imasters.com.br/artigo/24443/javascript/screenshot-com-canvas-e-javascript
