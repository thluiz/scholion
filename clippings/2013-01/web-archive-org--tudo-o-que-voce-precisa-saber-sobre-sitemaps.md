---
url: "https://web.archive.org/web/20131226192742/http://tableless.com.br/tudo-que-voce-precisa-saber-sobre-sitemaps/"
captured_at: "2013-01-21T10:13:00-03:00"
title: "Tudo o que você precisa saber sobre Sitemaps"
domain: "web-archive-org"
---

Sitemap é uma maneira fácil de informar aos motores de buscas sobre as páginas do seu site que estão disponíveis para indexação, esse tipo de arquivo é útil e válido para qualquer tipo de site seja institucional, e-commerce, blog, sites de pequeno médio ou grande porte.

  

Graças ao padrão definido pelas empresas Google, Microsoft e Yahoo, os motores de buscas podem encontrar as suas páginas muito mais rápido, reduzindo assim a quantidade de tempo que leva para o seu site ou uma nova página aparecer nos resultados de busca.

  

**Ao criar um Sitemap** para nossos sites temos que ter em mente duas coisas:

  

  

O Sitemap não garante que uma página será adicionada ao índice do buscador ou que o seu site tenha um posicionamento melhor.

  

O Sitemap é para um “robô” ler, então é primordial que você responsável pelo site, envie as URLs válidas, caso contrário a autoridade do seu site pode estar abalada.

  

## Conheça os tipos de Sitemap

  

Todos os tipos de sitemap tem um limite de tamanho, é recomendado que fique com menos de 50MB ou até 50 mil URLs por arquivo, caso seu site seja muito grande nada impede de você criar uma segmentação de Sitemaps.

  

### Estrutura Básica de um Sitemap

  

Certifique-se que todas as URLs do seu arquivo estejam no mesmo host, outro ponto importante é o tamanho da URL é permitido até 2.048 caracteres.

  

```
 <?xml version="1.0" encoding="UTF-8"?>  
 <urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">  
     <url>  
         <loc> http://www.seusite.com.br/</loc>  
         <lastmod>2013-01-13</lastmod>  
         <changefreq>weekly</changefreq>  
         <priority>0.6</priority>  
     </url>  
 </urlset>
```

  

A tag **loc** é utilizado para ligar a página, basta digitar a URL entre as tags

  

A tag **lastmod** apresenta a data em que a página foi modificada pela última vez

  

A tag **changefreq** é a freqüencia de variação média da página (horária, diária, semanal, mensal, anual)

  

Você também pode priorizar determinadas páginas através da tag **priority**. Valores de prioridade variam 0,0 até 1,0 (1,0 é o mais importante)

### Índice de Sitemaps

  

Se você tiver mais de um Sitemap, poderá listá-los em um arquivo de **índice de Sitemaps** e enviar esse arquivo ao Google, nesse caso você não precisa enviar cada arquivo de Sitemap individualmente.

  

```
 <?xml version="1.0" encoding="UTF-8"?>  
 <sitemapindex xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">  
     <sitemap>  
         <loc> http://www.website.com/sitemap1.xml</loc>  
     </sitemap>  
     <sitemap>  
         <loc> http://www.website.com/sitemap2.xml</loc>  
     </sitemap>  
 </sitemapindex>
```

  

### Sitemap de Notícias

  

Essa é a **estrutura de um Sitemap** voltado para o Google News, geralmente utilizado por grandes portais pois possuem uma grande demanda de URLs com constantes atualizações.

  

```
 <?xml version="1.0" encoding="UTF-8"?>  
 <urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"  
 xmlns:news="http://www.google.com/schemas/sitemap-news/0.9">  
     <url>  
         <loc> http://www.example.org/business/article55.html</loc>  
         <news:news>  
             <news:publication>  
                 <news:name>Jornal de Exemplo</news:name>  
                 <news:language>en</news:language>  
             </news:publication>  
             <news:access>Subscription</news:access>  
             <news:genres>PressRelease, Blog</news:genres>  
             <news:publication_date>2008-12-23</news:publication_date>  
             <news:title>Empresas A e B discutem fusão</news:title>  
             <news:keywords>negócios, fusão</news:keywords>  
             <news:stock_tickers>NASDAQ:A, NASDAQ:B</news:stock_tickers>  
         </news:news>  
     </url>  
 </urlset>
```

  

### Sitemap de Vídeos

  

Também é possível criar um **Sitemap para vídeos**, os formatos permitidos para os buscador rastrear são: WMV, MP4, MPEG, MPG, m4v, asf, fvl, swf, avi, RA e RAM.

  

```
 <urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"  
 xmlns:video="http://www.google.com/schemas/sitemap-video/1.1">  
 <url>  
     <loc> http://www.website.com/video-page.html</loc>  
     <video:video>  
     <video:thumbnail_loc> http://www.website.com/video-thumbnail.jpg</video:thumbnail_loc>  
     <video:title>Most Awesome Video Ever</video:title>  
     <video:description>As the title says: this is the most awesome video ever.</video:description>  
     <video:content_loc> http://www.website.com/video.mp4</video:content_loc>  
     <video:duration>120</video:duration>  
     </video:video>  
     </url>  
 </urlset>
```

  

Há uma abundância de outras tags que você pode adicionar, como uma classificação, ver contagem, restrições, etc. Todas as tags disponíveis pode ser encontrada dentro de recursos para [Webmasters do Google](https://www.google.com.br/webmasters/tools).

  

### Sitemap de Imagens

  

O **Sitemap de imagem** pode ser muito útil para obter um tráfego “extra” através de resultados de pesquisas por imagens no Google.

  

```
 <?xml version="1.0" encoding="UTF-8"?>  
  <urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"  
   xmlns:image="http://www.google.com/schemas/sitemap-image/1.1">  
  <url>  
    <loc> http://example.com/exemplo.html</loc>  
    <image:image>  
      <image:loc> http://example.com/image.jpg</image:loc>   
    </image:image>  
    <image:image>  
      <image:loc> http://example.com/foto.jpg</image:loc>  
    </image:image>  
  </url>   
 </urlset>
```

  

### Sitemap para Celular

  

Com o crescimento do mercado Mobile é natural que as pessoas comecem a buscar mais através do seus dispositivos móveis, é um fato inevitável saia na frente do seus concorrentes comece com o **Sitemap para celular** e depois saiba [como otimizar o seu site para mobile](http://www.seomonkey.com.br/mobile/dicas-para-otimizacao-mobile).

  

```
 <?xml version="1.0" encoding="UTF-8" ?>  
  <urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"  
         xmlns:mobile="http://www.google.com/schemas/sitemap-mobile/1.0">  
     <url>  
    <loc> http://celular.example.com/artigo100.html</loc>  
         <mobile:mobile/>  
     </url>  
 </urlset>
```

  

## Validando o Sitemap

  

Todos nós já esquecemos de fechar uma tag, pensando nisso o Google disponibilizou uma opção de testar o seu Sitemap antes de enviar, para acessar basta entrar no Google Webmasters Tools > Otimização > Sitemaps:  
 ![](http://www.seomonkey.com.br/img/ferramentas-para-webmasters-otimizacao-sitemaps.jpg)

  

**DICA**: Se você tiver um blog com um Feed RSS ou Atom, poderá enviar a URL desse feed como um Sitemap, outra maneira simples de fazer é criar um arquivo TXT com uma URL por linha.

  

## Conclusão

  

Deseja ter mair relevância nos buscadores, comece facilitando a indexação do seu site através do Sitemap.

  

O post [Tudo o que você precisa saber sobre Sitemaps](http://tableless.com.br/tudo-que-voce-precisa-saber-sobre-sitemaps/) foi originalmente publicado em [Tableless](http://tableless.com.br).

  

[![](http://feeds.feedburner.com/~ff/tableless?d=yIl2AUoC8zA)](http://feeds.feedburner.com/~ff/tableless?a=l9CWEwQL1ew:H54betWnzaI:yIl2AUoC8zA)  [![](http://feeds.feedburner.com/~ff/tableless?i=l9CWEwQL1ew:H54betWnzaI:D7DqB2pKExk)](http://feeds.feedburner.com/~ff/tableless?a=l9CWEwQL1ew:H54betWnzaI:D7DqB2pKExk)  [![](http://feeds.feedburner.com/~ff/tableless?d=7Q72WNTAKBA)](http://feeds.feedburner.com/~ff/tableless?a=l9CWEwQL1ew:H54betWnzaI:7Q72WNTAKBA)  [![](http://feeds.feedburner.com/~ff/tableless?i=l9CWEwQL1ew:H54betWnzaI:aKCwKftKxY0)](http://feeds.feedburner.com/~ff/tableless?a=l9CWEwQL1ew:H54betWnzaI:aKCwKftKxY0)  [![](http://feeds.feedburner.com/~ff/tableless?d=dnMXMwOfBR0)](http://feeds.feedburner.com/~ff/tableless?a=l9CWEwQL1ew:H54betWnzaI:dnMXMwOfBR0)  [![](http://feeds.feedburner.com/~ff/tableless?d=YwkR-u9nhCs)](http://feeds.feedburner.com/~ff/tableless?a=l9CWEwQL1ew:H54betWnzaI:YwkR-u9nhCs)  [![](http://feeds.feedburner.com/~ff/tableless?i=l9CWEwQL1ew:H54betWnzaI:JEwB19i1-c4)](http://feeds.feedburner.com/~ff/tableless?a=l9CWEwQL1ew:H54betWnzaI:JEwB19i1-c4)  [![](http://feeds.feedburner.com/~ff/tableless?i=l9CWEwQL1ew:H54betWnzaI:wF9xT3WuBAs)](http://feeds.feedburner.com/~ff/tableless?a=l9CWEwQL1ew:H54betWnzaI:wF9xT3WuBAs)  [![](http://feeds.feedburner.com/~ff/tableless?i=l9CWEwQL1ew:H54betWnzaI:V_sGLiPBpWU)](http://feeds.feedburner.com/~ff/tableless?a=l9CWEwQL1ew:H54betWnzaI:V_sGLiPBpWU)  [![](http://feeds.feedburner.com/~ff/tableless?i=l9CWEwQL1ew:H54betWnzaI:tYZ39nBRSfM)](http://feeds.feedburner.com/~ff/tableless?a=l9CWEwQL1ew:H54betWnzaI:tYZ39nBRSfM)

  
 ![](http://feeds.feedburner.com/~r/tableless/~4/l9CWEwQL1ew)  
   
   
   
 from Tableless.com.br - Web Standards com Arroz e Feijão <http://tableless.com.br/tudo-que-voce-precisa-saber-sobre-sitemaps/?utm_source=feedburner&utm_medium=feed&utm_campaign=Feed%3A+tableless+%28Tableless%29>
