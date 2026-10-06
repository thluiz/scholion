---
url: "https://imasters.com.br/analytics/encontre-as-maiores-falhas-tecnicas-do-seu-site-em-60-minutos-parte-01"
captured_at: "2012-04-17T11:06:35-03:00"
title: "Encontre as maiores falhas técnicas do seu site em 60 minutos - Parte 01"
domain: "imasters-com-br"
---

### Sent to you by Thiago Silva via Google Reader:

## 

[Encontre as maiores falhas técnicas do seu site em 60 minutos - Parte 01](http://feedproxy.google.com/~r/imasters/~3/DuBh33-8vaQ/story01.htm)

via [iMasters -](http://imasters.com.br/) by David Sottimano () on 4/17/12

  

Coloquei-me, intencionalmente, em maus lençóis para demonstrar como faria uma auditoria técnica de SEO em um site em uma hora, para procurar soluções rápidas (e realmente cronometrei apenas para tornar o trabalho mais difícil). Para os profissionais, aqui está uma visão do meu fluxo de trabalho; para o aspirante, aqui está um conjunto base de verificações que você pode fazer rapidamente.

Tenho alguns adoráveis voluntários que, gentilmente, me permitiram auditar seus sites para mostrar o que pode ser feito em menos de 60 minutos.

Olharei especificamente para a indexação de rastreamento e ameaça em potencial do Panda, questões como:

1. Arquitetura (redirecionamento desnecessário páginas órfãs, e que não se deve seguir);
2. Indexação e rastreamento (canônico, sem indexação, seguir, não seguir, redirecionamentos, robots.txt, erros de servidor);
3. Conteúdo duplicado (texto repetido, paginação, baseada em parâmetro, títulos faltando, ou com erros, H1S etc.);

Não se preocupe se você não é técnico, porque a maioria das ferramentas e dos métodos que vou usar são muito bem documentados em torno da web.

Vamos conhecer os nossos voluntários!

- <http://cvcsports.com/>
- [http://www.webrevolve.com](http://www.webrevolve.com/)
- <http://www.lexingtonlaw.com/>

Aqui está o que usarei para fazer este trabalho:

- [Barra de ferramentas do SEOmoz](http://www.seomoz.org/seo-toolbar) - tenha certeza de que o destaque para os links que não se deve seguir estejam acionados - assim, poderá diagnosticar visivelmente restrições de caminho de rastreamento;
- [Rastreador Screaming Frog](http://www.screamingfrog.co.uk/seo-spider/#axzz1lYgXzctR) - rastreie o site completo com o Screaming Frog (user agent definido para Googlebot) - guia de usuário completo [aqui](http://www.screamingfrog.co.uk/seo-spider/user-guide/);
- Chrome e Firefox (FF terá Javascript, CSS desativado e User Agent como Googlebot) - para procurar por problemas de usabilidade causados ​​por CSS ou Javascript.
- Consultas de pesquisa do Google - para verificar o índice de questões, como a duplicação de conteúdo, subdomínios deturpados, penalidades etc.

Aqui estão outras verificações que fiz e que foram deixadas de fora pelo interesse o processo curto:

- [Open Site Explorer](http://www.opensiteexplorer.org/) - baixe um relatório de um link anterior para ver se você está deixando passar links que apontam para links órfãos, 302 ou URLs incorretas em seu site. Se você encontrar pessoas que linkam de forma incorreta, adicione algumas regras 301 em seu site para aproveitar aquele link juice;
- [Tomathony](http://www.tomanthony.co.uk/tools/bulk-http-header-compare/) - verifique se o site está redirecionando especificamente o Googlebot;
- [Spy on Web](http://spyonweb.com/) - existe algum outro domínio conectado que você deveria conhecer? Principalmente para o conteúdo duplicado.
- [Built With](http://builtwith.com/) - descubra se o site está usando Apache, IIS, PHP e você saberá quais vulnerabilidades procurar automaticamente;
- Verifique textos escondidos, display CSS: robots.txt que bloqueiam arquivos externos JS, páginas hackeadas/ órfãs.

Meus relatórios essenciais:

- Rastreamento completo do site com Screaming Frog (user agent definido para Googlebot);
- Um relatório geral no índice do Google usando o site: (1000 resultados por consulta, infelizmente - [é assim que eu faço](http://www.distilled.net/blog/seo/how-to-build-agile-seo-tools-using-google-docs/))

Nesta primeira parte do artigo, vou falar sobre os problemas de arquitetura dos sites. Na sequência, vou falar sobre indexação e rastreamento. Assim, vocês poderão absorver melhor o conteúdo.

#### 1. Links quebrados importantes

Sempre teremos uns links quebrados aqui e ali; e em um mundo ideal todos funcionariam. Apenas certifique-se de que o SEO e a usabilidade de links importantes (homepage) estejam sempre corretos. O link quebrado a seguir está na homepage do Webrevolve, que deveria apontar para o seu blog, mas retorna um erro 404. Este é um elo importante, porque se trata de um ótimo recurso e quero, definitivamente, ler mais a respeito.

![5b173c64e08ee9d7667fd9857da27169.jpg](imasters-com-br--encontre-as-maiores-falhas-tecnicas-do-seu-site-em-60-minuto/5b173c64e08ee9d7667fd9857da27169.jpg)

- Correção: Entre lá e aponte o link para a página correta que é <http://www.webrevolve.com/our-blog/>
- Como encontrei: Screaming Frog> relatório de códigos de resposta.

#### 2. Redirecionamento desnecessário

Isso acontece muito mais do que as pessoas pensam. O problema é que quando nós fazemos um 301 em uma página para uma nova home, muitas vezes nos esquecemos de corrigir os links internos apontando para a página antiga (aquela com o redirecionamento 301).

Esta página <http://www.lexingtonlaw.com/credit-education/foreclosure.html> redireciona para <http://www.lexingtonlaw.com/credit-education/foreclosure-2.html>

No entanto, eles ainda têm links internos apontando para a página antiga:

- http://www.lexingtonlaw.com/credit-education/bankruptcy.html?linkid=bankruptcy
- http://www.lexingtonlaw.com/blog/category/credit-repair/page/10
- http://www.lexingtonlaw.com/credit-education/bankruptcy.html?select\_state=1&linkid=selectstate
- http://www.lexingtonlaw.com/credit-education/collections.html

- Correção: Entre em que CMS e altere as ligações internas para apontar para http://www.lexingtonlaw.com/credit-education/foreclosure-2.html
- Como encontrei: Screaming Frog> relatório de códigos de resposta.

#### 3. Subdomínios múltiplos - canonicalizando a versão www ou não-www

Um dos primeiros princípios básicos de SEO e ainda há toneladas de sites antigos que estão dividindo sua autoridade por não usar o redirecionamento do www para o não-www ou vice-versa.

Desculpe por escolher você, CVSports:

- http://cvcsports.com/
- http://www.cvcsports.com/

Ah, e mais alguns têm dado seu jeito no índice do Google e que você deveria remover também:

- http://smtp.cvcsports.com/
- http://pop.cvcsports.com/
- http://mx1.cvcsports.com/
- http://ww.cvcsports.com/
- http://www.buildyourjacket.com/
- http://buildyourjacket.com/

Basicamente, você tem sete cópias do seu site no índice.

- Correção: Eu recomendo usar "www.cvcsports.com" como a página principal, e você deve usar seu arquivo htaccess para criar redirecionamentos 301 para todos esses subdomínios para o site principal;
- Como encontrá-lo? Consulte no Google "site: cvcsports.com-www" (Também defini o meu número de resultados de cem para seleção através do índice mais rápido).

#### 4. Mantendo a estrutura de URL consistente

É importante notar que isso só se torna um problema quando as ligações externas estão apontando para o URLs erradas. Quase todos links de volta são preciosos, e queremos garantir que obtemos valor máximo de cada um. Somente nós podemos controlar como ficaremos linkados, sem www, ou com letras maiúsculas, por exemplo. Se não quiser entrar em contato com o webmaster para mudá-lo, podemos sempre empregar o 301 e redirecionar para aproveitar o valor ao máximo. O único lugar em que isso não deve acontecer é no seu próprio site.

Todos nós sabemos que www.examplo.com/LETRASMAIUSCULAS é diferente de www.examplo.com/letrasminusculas quando se trata de link juice externo. Como bons SEOs, normalmente combatemos o erro humano com redirecionamento permanente para aplicar apenas uma versão de uma URL (por exemplo, forçando em minúsculas), que pode causar redirecionamentos desnecessários se alguém linka ao invés de redirecionar.

 Aqui estão alguns exemplos de nossos sites:

- http://www.lexingtonlaw.com/credit-education/rebuild-credit - 301 para fugir da barra invertida
- http://webrevolve.com/web-design-development/conversion-rate-optimisation/ - redireciona para a versão WWW

- Correção: Determinar a estrutura de sua URL: todas elas deverão ter barras à direita, www, letras minúsculas? Em qualquer decisão que tomar, seja consistente e você evitará problemas futuros. Indexe o seu site e corrija isso.

Por enquanto é isso, pessoal. Na segunda parte deste artigo, vamos ver sobre indexação e rastreamento. Até lá!

[anexo ausente]

|  |  |
| --- | --- |
| [9bcafcd24ef5e7a319a7e300c0d5b221.gif](http://share.feedsportal.com/viral/sendEmail.cfm?lang=pt&amp;title=Encontre+as+maiores+falhas+t%C3%A9cnicas+do+seu+site+em+60+minutos+-+Parte+01&amp;link=http%3A%2F%2Fimasters.com.br%2Fartigo%2F24174%2Fmetricas%2Fencontre-as-maiores-falhas-tecnicas-do-seu-site-em-60-minutos-parte-01) | [75b9131ce15803402621ad7d693d4dd1.gif](http://res.feedsportal.com/viral/bookmark_pt.cfm?title=Encontre+as+maiores+falhas+t%C3%A9cnicas+do+seu+site+em+60+minutos+-+Parte+01&amp;link=http%3A%2F%2Fimasters.com.br%2Fartigo%2F24174%2Fmetricas%2Fencontre-as-maiores-falhas-tecnicas-do-seu-site-em-60-minutos-parte-01) |

  
  
[[anexo ausente]](http://da.feedsportal.com/r/130577997578/u/49/f/546640/c/33212/s/1e77238c/a2.htm)[anexo ausente][anexo ausente]

  

### Things you can do from here:

- [Subscribe to iMasters -](http://www.google.com/reader/view/feed%2Fhttp%3A%2F%2Fimasters.uol.com.br%2Ffeed%2F?source=email) using **Google Reader**
- [Get started using Google Reader](http://www.google.com/reader/?source=email) to easily keep up with **all your favorite sites**
