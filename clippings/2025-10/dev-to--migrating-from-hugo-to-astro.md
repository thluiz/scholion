---
url: "https://dev.to/huijing/migrating-from-hugo-to-astro-3j95?"
captured_at: "2025-10-22T11:20:47+01:00"
title: "Migrating from Hugo to Astro - DEV Community"
domain: "dev-to"
---

---
I'm migrating my blog again. This blog has been in existence for more than 11 years. It started as a Jekyll site. Then I [moved to Hugo](https://dev.to/blog/migrating-from-jekyll-to-hugo/). Now I'm moving it to [Astro](https://astro.build/). The design has NEVER changed, which makes me quite contrarian to most frontend developers in the industry. But when I came up with the design back then, I wanted it to feel like me. And today, when I look at my blog, it still feels like me. I guess this says more about me as a person than my actual blog design, but I'm past the age where I care any more.

Hugo says I have 287 pages on my blog but I only have 226 blog posts 🤔. But the point is, I have a lot of pages to migrate. Do I really have to port over everything, you might ask? Well, yes. I do. This is my entire web developer journey, how could I possibly leave anything behind? Also, why am I migrating to begin with? Honestly, I completely lost the plot with Hugo.

When they released their revamped template system in [v0.146.0](https://github.com/gohugoio/hugo/releases/tag/v0.146.0), I couldn't wrap my head around it. My listing pages all broke locally. If you check my blog statistics, I clearly haven't been writing that much since 2021 anyway, but I don't actually know Go or work on Hugo websites. So this is not a Hugo problem, it's a me problem. I also started living in Astro since 2023, when I was documentation infrastructure czar (this is a fake title) at the [Interledger Foundation](https://interledger.org/).

Needless to say, I have fallen in love with Astro and its fantastic community. I will always have good things to say about Astro. At this point in my career, I feel reasonably confident in my migration capabilities. I've built my career on similar projects, enough to learn that it's never easy, and things will break, but nothing can't be fixed. Probably not going to be a single day project this time though.

However, this is now a mid-sized website (that earns NOTHING, haha), so I did need to think through some migration strategies.

## [](https://dev.to/huijing/migrating-from-hugo-to-astro-3j95?#set-up-astro-site)Set up Astro site

I also love [bun](https://bun.com/). At first, it was because I liked the logo, because I'm superficial like that. But I've felt the benefits of its package manager, how it does `.env` files, how it supports TypeScript natively and so on. Yay, bun.

Anyway, first step was creating a new Astro project:  

```
bunx create-astro@latest website
```

Astro [warns you](https://docs.astro.build/en/recipes/bun/) that using Astro with Bun is a little rough around the edges, but it was alright for me. I went with the blog template.

## [](https://dev.to/huijing/migrating-from-hugo-to-astro-3j95?#migrate-generated-components)Migrate generated components

The blog template has some Astro components like the site header and footer. I figured those could be the first things to go over. I did have quite a lot of template logic going on, but low-hanging fruit first tends to be how I do things. I had not looked at my styling code in years, but the Sass features I had been using are pretty much native CSS at this point, so this was a good time for a styles refactor.

I had previously broken up my files into different Sass files loosely based on Harry Robert's [ITCSS](https://www.creativebloq.com/web-design/manage-large-css-projects-itcss-101517528), so it did make porting over to Astro components relatively easy. I rewrote all the Sass back to native CSS because I really wasn't doing anything spectacular Sassy to begin with. Just some nesting and colour functions. Nothing today's native CSS couldn't handle.

Once the base styles came over, there was an illusion that things were progressing quickly. No, they were not. This was largely due to the amount of template logic I had introduced over the years. Porting over the stuff in the `head` element took a good while, because I had relied on a lot of post frontmatter to do that. So that also meant setting up the frontmatter in Astro via the _content.config.ts_ file.

I also needed to inject some logic into the [RSS feed implementation](https://docs.astro.build/en/recipes/rss/) because my blog listed writing that I did for external publications and I wanted the canonical links to point to those external URLs. The external URL thing ended up taking a lot more time than I expected, but at least it works now. By now the plan to migrate generated components first had gone out the window, because I got distracted by migrating pages instead.  

```
<span>import</span> <span>{</span> <span>getCollection</span> <span>}</span> <span>from</span> <span>"</span><span>astro:content</span><span>"</span><span>;</span>
<span>import</span> <span>rss</span> <span>from</span> <span>"</span><span>@astrojs/rss</span><span>"</span><span>;</span>
<span>import</span> <span>{</span> <span>SITE_DESCRIPTION</span><span>,</span> <span>SITE_TITLE</span> <span>}</span> <span>from</span> <span>"</span><span>@/consts</span><span>"</span><span>;</span>

<span>export</span> <span>async</span> <span>function</span> <span>GET</span><span>(</span><span>context</span><span>)</span> <span>{</span>
  <span>const</span> <span>posts</span> <span>=</span> <span>await</span> <span>getCollection</span><span>(</span><span>"</span><span>blog</span><span>"</span><span>);</span>
  <span>return</span> <span>rss</span><span>({</span>
    <span>title</span><span>:</span> <span>SITE_TITLE</span><span>,</span>
    <span>description</span><span>:</span> <span>SITE_DESCRIPTION</span><span>,</span>
    <span>site</span><span>:</span> <span>context</span><span>.</span><span>site</span><span>,</span>
    <span>items</span><span>:</span> <span>posts</span>
      <span>.</span><span>sort</span><span>((</span><span>a</span><span>,</span> <span>b</span><span>)</span> <span>=&gt;</span> <span>+</span><span>new</span> <span>Date</span><span>(</span><span>b</span><span>.</span><span>data</span><span>.</span><span>date</span><span>)</span> <span>-</span> <span>+</span><span>new</span> <span>Date</span><span>(</span><span>a</span><span>.</span><span>data</span><span>.</span><span>date</span><span>))</span>
      <span>.</span><span>filter</span><span>((</span><span>post</span><span>)</span> <span>=&gt;</span> <span>!</span><span>post</span><span>.</span><span>data</span><span>.</span><span>nofeed</span><span>)</span>
      <span>.</span><span>map</span><span>((</span><span>post</span><span>)</span> <span>=&gt;</span> <span>({</span>
        <span>...</span><span>post</span><span>.</span><span>data</span><span>,</span>
        <span>link</span><span>:</span> <span>post</span><span>.</span><span>data</span><span>.</span><span>external_url</span> <span>?</span> <span>post</span><span>.</span><span>data</span><span>.</span><span>external_url</span> <span>:</span> <span>`/blog/</span><span>${</span><span>post</span><span>.</span><span>id</span><span>}</span><span>/`</span><span>,</span>
        <span>pubDate</span><span>:</span> <span>new</span> <span>Date</span><span>(</span><span>post</span><span>.</span><span>data</span><span>.</span><span>date</span><span>),</span>
      <span>})),</span>
  <span>});</span>
<span>}</span>
```

## [](https://dev.to/huijing/migrating-from-hugo-to-astro-3j95?#migrate-pages)Migrate pages

There were not that many pages (i.e. not blog posts) on my website, but the only straight-forward page was the "About" page. My "Talks" and "Work" pages were a combination of frontmatter filtering and looping over external data files. The meat of the site was my blog, so there was the full listing page, tag pages and the home page which showed the latest 10 posts. Also had a contact page, résumé page and custom 404 page.

By this point, I had fully realised that my brain reads Javascript with a fluency that does not exist for Hugo's style of Go templating syntax. Migrating the tag pages were a good example of this. For Astro, creating tag pages was a matter of filtering the blog [content collection](https://docs.astro.build/en/guides/content-collections/) for posts with tags in their frontmatter. I'll probably write up the details of the implementation in a separate post.

I also had data for my talk slides and side projects in separate YAML files, and had some logic that would display different URLs, if it should link to a blog post or an external URL. That logic in Hugo was… let's just say I'm not that great with double curly braces? I'm just more used to mapping arrays. Honestly, the most complicated logic was probably the `head` element if I'm being honest. Those OG tags, canonical URLs and `noindex` scenarios needed some extra scrutiny.

But in a nutshell, compare this:  

```
<span>&lt;head&gt;</span>
  <span>&lt;meta</span> <span>charset=</span><span>"utf-8"</span><span>&gt;</span>
  <span>&lt;meta</span> <span>http-equiv=</span><span>"X-UA-Compatible"</span> <span>content=</span><span>"IE=edge"</span><span>&gt;</span>
  <span>&lt;meta</span> <span>name=</span><span>viewport</span> <span>content=</span><span>"width=device-width, initial-scale=1"</span><span>&gt;</span>

  <span>&lt;title&gt;</span>{{ if .Params.title }}{{ .Params.title | safeHTML }}{{ else }}{{ .Site.Title }}{{ end }}<span>&lt;/title&gt;</span>
  <span>&lt;meta</span> <span>name=</span><span>"description"</span> <span>content=</span><span>"{{ if (eq .Type "</span><span>blog</span><span>")</span> <span>}}{{</span> <span>.</span><span>Summary</span> <span>|</span> <span>truncate</span> <span>130</span> <span>}}{{</span> <span>else</span> <span>}}{{</span> <span>.</span><span>Site.Params.description</span> <span>}}{{</span> <span>end</span> <span>}}"</span><span>&gt;</span>

  {{ if .Params.noindex }}
  <span>&lt;meta</span> <span>name=</span><span>"robots"</span> <span>content=</span><span>"noindex"</span><span>&gt;</span>
  {{ end }}

  {{ template "_internal/opengraph.html" . }}
  {{ template "_internal/twitter_cards.html" . }}

  <span>&lt;meta</span> <span>name=</span><span>"twitter:site"</span> <span>content=</span><span>"@hj_chen"</span><span>&gt;</span>
  <span>&lt;meta</span> <span>name=</span><span>"p:domain_verify"</span> <span>content=</span><span>"1623582e8d2881f774efff746a6f3f1f"</span><span>&gt;</span>
  <span>&lt;meta</span> <span>name=</span><span>"msvalidate.01"</span> <span>content=</span><span>"30F5181A4C23EE64C2F947E2910DDBBA"</span><span>&gt;</span>

  {{ if .Params.external_url }}
  <span>&lt;link</span> <span>rel=</span><span>"canonical"</span> <span>href=</span><span>"{{ .Params.external_url }}"</span><span>&gt;</span>
  {{ else }}
  <span>&lt;link</span> <span>rel=</span><span>"canonical"</span> <span>href=</span><span>"{{ .Permalink }}"</span><span>&gt;</span>
  {{ end }}

  {{ with .OutputFormats.Get "RSS" -}}
    {{ printf `<span>&lt;link</span> <span>rel=</span><span>"%s"</span> <span>type=</span><span>"%s"</span> <span>href=</span><span>"%s"</span> <span>title=</span><span>"%s"</span><span>&gt;</span>` .Rel .MediaType.Type .Permalink $.Site.Title | safeHTML }}
  {{ end -}}

  <span>&lt;link</span> <span>href=</span><span>"https://micro.blog/huijing"</span> <span>rel=</span><span>"me"</span><span>&gt;</span>
  <span>&lt;link</span> <span>rel=</span><span>"monetization"</span> <span>href=</span><span>"https://ilp.gatehub.net/747467740/USD"</span> <span>/&gt;</span>

  {{ if (eq .Type "blog") }}
  {{ $options := (dict "targetPath" "posts.css" "outputStyle" "compressed" "enableSourceMap" true) }}
  {{ $style := resources.Get "sass/posts.scss" | resources.ToCSS $options }}
  <span>&lt;link</span> <span>rel=</span><span>"stylesheet"</span> <span>href=</span><span>"{{ $style.RelPermalink }}"</span><span>&gt;</span>
  {{ else }}
  {{ $options := (dict "targetPath" "pages.css" "outputStyle" "compressed" "enableSourceMap" true) }}
  {{ $style := resources.Get "sass/pages.scss" | resources.ToCSS $options }}
  <span>&lt;link</span> <span>rel=</span><span>"stylesheet"</span> <span>href=</span><span>"{{ $style.RelPermalink }}"</span><span>&gt;</span>
  {{ end }}

  <span>&lt;link</span> <span>rel=</span><span>"preload"</span> <span>href=</span><span>"/assets/fonts/eightbitoperatorplus8-bold-webfont.woff2"</span> <span>as=</span><span>"font"</span> <span>type=</span><span>"font/woff2"</span> <span>crossorigin</span><span>&gt;</span>
  <span>&lt;link</span> <span>rel=</span><span>"preload"</span> <span>href=</span><span>"/assets/fonts/eightbitoperatorplus-regular-webfont.woff2"</span> <span>as=</span><span>"font"</span> <span>type=</span><span>"font/woff2"</span> <span>crossorigin</span><span>&gt;</span>
  <span>&lt;link</span> <span>rel=</span><span>"preload"</span> <span>href=</span><span>"/assets/fonts/magnetic-pro-black.woff2"</span> <span>as=</span><span>"font"</span> <span>type=</span><span>"font/woff2"</span> <span>crossorigin</span><span>&gt;</span>
  <span>&lt;link</span> <span>rel=</span><span>"preload"</span> <span>href=</span><span>"/assets/fonts/magnetic-pro-light.woff2"</span> <span>as=</span><span>"font"</span> <span>type=</span><span>"font/woff2"</span> <span>crossorigin</span><span>&gt;</span>

  <span>&lt;link</span> <span>rel=</span><span>"apple-touch-icon"</span> <span>sizes=</span><span>"180x180"</span> <span>href=</span><span>"/assets/favicons/apple-touch-icon.png"</span><span>&gt;</span>
  <span>&lt;link</span> <span>rel=</span><span>"icon"</span> <span>type=</span><span>"image/png"</span> <span>href=</span><span>"/assets/favicons/favicon-32x32.png"</span> <span>sizes=</span><span>"32x32"</span><span>&gt;</span>
  <span>&lt;link</span> <span>rel=</span><span>"icon"</span> <span>type=</span><span>"image/png"</span> <span>href=</span><span>"/assets/favicons/favicon-16x16.png"</span> <span>sizes=</span><span>"16x16"</span><span>&gt;</span>
  <span>&lt;link</span> <span>rel=</span><span>"manifest"</span> <span>href=</span><span>"/assets/favicons/manifest.json"</span><span>&gt;</span>
  <span>&lt;link</span> <span>rel=</span><span>"mask-icon"</span> <span>href=</span><span>"/assets/favicons/safari-pinned-tab.svg"</span> <span>color=</span><span>"#009418"</span><span>&gt;</span>
  <span>&lt;link</span> <span>rel=</span><span>"shortcut icon"</span> <span>href=</span><span>"/assets/favicons/favicon.ico"</span><span>&gt;</span>
  <span>&lt;meta</span> <span>name=</span><span>"msapplication-config"</span> <span>content=</span><span>"/assets/favicons/browserconfig.xml"</span><span>&gt;</span>
  <span>&lt;meta</span> <span>name=</span><span>"theme-color"</span> <span>content=</span><span>"#ffffff"</span><span>&gt;</span>
<span>&lt;/head&gt;</span>
```

with this:  

```
<span>&lt;head&gt;</span>
  <span>&lt;meta</span> <span>charset=</span><span>"utf-8"</span> <span>/&gt;</span>
  <span>&lt;meta</span> <span>name=</span><span>"viewport"</span> <span>content=</span><span>"width=device-width,initial-scale=1"</span> <span>/&gt;</span>
  <span>&lt;link</span> <span>rel=</span><span>"sitemap"</span> <span>href=</span><span>"/sitemap-index.xml"</span> <span>/&gt;</span>
  <span>&lt;link</span> <span>rel=</span><span>"alternate"</span> <span>type=</span><span>"application/rss+xml"</span> <span>title=</span><span>{SITE_TITLE}</span> <span>href=</span><span>{new</span> <span>URL</span><span>("</span><span>rss.xml</span><span>",</span> <span>Astro.site</span><span>)}</span>
  <span>/&gt;</span>
  <span>&lt;meta</span> <span>name=</span><span>"generator"</span> <span>content=</span><span>{Astro.generator}</span> <span>/&gt;</span>

  <span>&lt;title&gt;</span>{title ? `${title} | ${SITE_TITLE}` : SITE_TITLE}<span>&lt;/title&gt;</span>
  <span>&lt;meta</span> <span>name=</span><span>"author"</span> <span>content=</span><span>"Chen Hui Jing"</span> <span>/&gt;</span>
  <span>&lt;meta</span> <span>name=</span><span>"title"</span> <span>content=</span><span>{title</span> <span>?</span> <span>`${</span><span>title</span><span>}</span> <span>|</span> <span>${</span><span>SITE_TITLE</span><span>}`</span> <span>:</span> <span>SITE_TITLE</span><span>}</span> <span>/&gt;</span>
  <span>&lt;meta</span> <span>name=</span><span>"description"</span> <span>content=</span><span>{description</span> <span>?</span> <span>description</span> <span>:</span> <span>SITE_DESCRIPTION</span><span>}</span> <span>/&gt;</span>
  {noindex <span>&amp;&amp;</span> <span>&lt;meta</span> <span>name=</span><span>"robots"</span> <span>content=</span><span>"noindex, nofollow"</span> <span>/&gt;</span>}
  <span>&lt;link</span> <span>rel=</span><span>"canonical"</span> <span>href=</span><span>{canonicalURL}</span> <span>/&gt;</span>

  <span>&lt;link</span> <span>rel=</span><span>"preload"</span> <span>href=</span><span>"/assets/fonts/eightbitoperatorplus8-bold-webfont.woff2"</span> <span>as=</span><span>"font"</span> <span>type=</span><span>"font/woff2"</span> <span>crossorigin</span><span>&gt;</span>
  <span>&lt;link</span> <span>rel=</span><span>"preload"</span> <span>href=</span><span>"/assets/fonts/eightbitoperatorplus-regular-webfont.woff2"</span> <span>as=</span><span>"font"</span> <span>type=</span><span>"font/woff2"</span> <span>crossorigin</span><span>&gt;</span>
  <span>&lt;link</span> <span>rel=</span><span>"preload"</span> <span>href=</span><span>"/assets/fonts/magnetic-pro-black.woff2"</span> <span>as=</span><span>"font"</span> <span>type=</span><span>"font/woff2"</span> <span>crossorigin</span><span>&gt;</span>
  <span>&lt;link</span> <span>rel=</span><span>"preload"</span> <span>href=</span><span>"/assets/fonts/magnetic-pro-light.woff2"</span> <span>as=</span><span>"font"</span> <span>type=</span><span>"font/woff2"</span> <span>crossorigin</span><span>&gt;</span>

  <span>&lt;meta</span> <span>property=</span><span>"og:title"</span> <span>content=</span><span>{title</span> <span>?</span> <span>`${</span><span>title</span><span>}</span> <span>|</span> <span>${</span><span>SITE_TITLE</span><span>}`</span> <span>:</span> <span>SITE_TITLE</span><span>}</span> <span>/&gt;</span>
  <span>&lt;meta</span> <span>property=</span><span>"og:type"</span> <span>content=</span><span>{ogType</span> <span>?</span> <span>ogType</span> <span>:</span> <span>"</span><span>website</span><span>"}</span> <span>/&gt;</span>
  <span>&lt;meta</span> <span>property=</span><span>"og:image"</span> <span>content=</span><span>{ogImageUrl</span> <span>?</span> <span>ogImageUrl</span> <span>:</span> <span>new</span> <span>URL</span><span>("/</span><span>images</span><span>/</span><span>avatar-ponytail</span><span>@2</span><span>x.png</span><span>",</span> <span>Astro.site</span><span>).</span><span>href</span><span>}</span> <span>/&gt;</span>
  <span>&lt;meta</span> <span>property=</span><span>"og:url"</span> <span>content=</span><span>{canonicalURL}</span> <span>/&gt;</span>
  <span>&lt;meta</span> <span>property=</span><span>"og:description"</span> <span>content=</span><span>{description</span> <span>?</span> <span>description</span> <span>:</span> <span>SITE_DESCRIPTION</span><span>}</span> <span>/&gt;</span>

  <span>&lt;meta</span> <span>name=</span><span>"twitter:card"</span> <span>content=</span><span>"summary_large_image"</span> <span>/&gt;</span>
  <span>&lt;meta</span> <span>name=</span><span>"twitter:title"</span> <span>content=</span><span>{title</span> <span>?</span> <span>`${</span><span>title</span><span>}</span> <span>|</span> <span>${</span><span>SITE_TITLE</span><span>}`</span> <span>:</span> <span>SITE_TITLE</span><span>}</span> <span>/&gt;</span>
  <span>&lt;meta</span> <span>name=</span><span>"twitter:image"</span> <span>content=</span><span>{ogImageUrl</span> <span>?</span> <span>ogImageUrl</span> <span>:</span> <span>new</span> <span>URL</span><span>("/</span><span>images</span><span>/</span><span>avatar-ponytail</span><span>@2</span><span>x.png</span><span>",</span> <span>Astro.site</span><span>).</span><span>href</span><span>}</span> <span>/&gt;</span>
  <span>&lt;meta</span> <span>name=</span><span>"twitter:description"</span> <span>content=</span><span>{description</span> <span>?</span> <span>description</span> <span>:</span> <span>SITE_DESCRIPTION</span><span>}</span> <span>/&gt;</span>

  <span>&lt;link</span> <span>rel=</span><span>"apple-touch-icon"</span> <span>sizes=</span><span>"180x180"</span> <span>href=</span><span>"/favicons/apple-touch-icon.png"</span> <span>/&gt;</span>
  <span>&lt;link</span> <span>rel=</span><span>"icon"</span> <span>type=</span><span>"image/png"</span> <span>href=</span><span>"/favicons/favicon-32x32.png"</span> <span>sizes=</span><span>"32x32"</span> <span>/&gt;</span>
  <span>&lt;link</span> <span>rel=</span><span>"icon"</span> <span>type=</span><span>"image/png"</span> <span>href=</span><span>"/favicons/favicon-16x16.png"</span> <span>sizes=</span><span>"16x16"</span> <span>/&gt;</span>
  <span>&lt;link</span> <span>rel=</span><span>"manifest"</span> <span>href=</span><span>"/favicons/manifest.json"</span> <span>/&gt;</span>
  <span>&lt;link</span> <span>rel=</span><span>"mask-icon"</span> <span>href=</span><span>"/favicons/safari-pinned-tab.svg"</span> <span>color=</span><span>"#009418"</span> <span>/&gt;</span>
  <span>&lt;link</span> <span>rel=</span><span>"shortcut icon"</span> <span>href=</span><span>"/favicons/favicon.ico"</span> <span>/&gt;</span>
  <span>&lt;meta</span> <span>name=</span><span>"msapplication-config"</span> <span>content=</span><span>"/favicons/browserconfig.xml"</span> <span>/&gt;</span>
  <span>&lt;meta</span> <span>name=</span><span>"theme-color"</span> <span>content=</span><span>"#ffffff"</span> <span>/&gt;</span>

  <span>&lt;meta</span> <span>name=</span><span>"twitter:site"</span> <span>content=</span><span>"@hj_chen"</span> <span>/&gt;</span>
  <span>&lt;meta</span> <span>name=</span><span>"p:domain_verify"</span> <span>content=</span><span>"1623582e8d2881f774efff746a6f3f1f"</span> <span>/&gt;</span>
  <span>&lt;meta</span> <span>name=</span><span>"msvalidate.01"</span> <span>content=</span><span>"30F5181A4C23EE64C2F947E2910DDBBA"</span> <span>/&gt;</span>
  <span>&lt;link</span> <span>href=</span><span>"https://micro.blog/huijing"</span> <span>rel=</span><span>"me"</span> <span>/&gt;</span>
  <span>&lt;link</span> <span>rel=</span><span>"monetization"</span> <span>href=</span><span>"https://ilp.gatehub.net/747467740/USD"</span> <span>/&gt;</span>
<span>&lt;/head&gt;</span>
```

## [](https://dev.to/huijing/migrating-from-hugo-to-astro-3j95?#migrate-blog-posts)Migrate blog posts

For the blog posts themselves, my content had always been in markdown since day 1 (which would be 4257 days ago). However, given that this is my third migration, I have started to think more about the use of components to keep things DRY. I then recalled the first time I did the migration, I had similar concerns. It was evident, looking at the current state of the blog posts this time, that I was in two minds back then.

In that previous migration blogpost, former me literally said:

> But I oscillated between using Hugo’s custom shortcodes versus writing out HTML in full for my responsive images because I kept thinking what would happen if I migrated again. That would mean writing the stuff in the shortcodes within my content.

Somewhere along the lines in 2023, I sort of lost the plot, and ended up using shortcodes for a bit. Thankfully, my decreased writing output meant that it wasn't that much to deal with. But for now, I did create temporary components in Astro, that I plan to slowly migrate anyway from back to just the HTML in full. I hope I remember this, if not, it's gonna be kinda hilarious for migration number 3.

You know what, I'll create an issue to track this. I don't understand why previous me did not do this when all my stuff is on GitHub to begin with. 🙄

Astro is a TypeScript-first kind of framework, so type safety is totally a thing. Anyway, the documentation states: “Every frontmatter or data property of your collection entries must be defined using a Zod data type”. Considering I had 1001 frontmatter properties for all kinds of rendering logic (see the above section), my schema was a little long-ish.  

```
<span>const</span> <span>blog</span> <span>=</span> <span>defineCollection</span><span>({</span>
  <span>loader</span><span>:</span> <span>glob</span><span>({</span> <span>base</span><span>:</span> <span>"</span><span>./src/content/blog</span><span>"</span><span>,</span> <span>pattern</span><span>:</span> <span>"</span><span>**/*.{md,mdx}</span><span>"</span> <span>}),</span>
  <span>schema</span><span>:</span> <span>()</span> <span>=&gt;</span>
    <span>z</span><span>.</span><span>object</span><span>({</span>
      <span>title</span><span>:</span> <span>z</span><span>.</span><span>string</span><span>(),</span>
      <span>date</span><span>:</span> <span>z</span><span>.</span><span>coerce</span><span>.</span><span>date</span><span>(),</span>
      <span>tags</span><span>:</span> <span>z</span><span>.</span><span>array</span><span>(</span><span>z</span><span>.</span><span>string</span><span>()).</span><span>default</span><span>([]),</span>
      <span>og_image</span><span>:</span> <span>z</span><span>.</span><span>string</span><span>().</span><span>optional</span><span>(),</span>
      <span>description</span><span>:</span> <span>z</span><span>.</span><span>string</span><span>().</span><span>optional</span><span>(),</span>
      <span>hastweet</span><span>:</span> <span>z</span><span>.</span><span>boolean</span><span>().</span><span>default</span><span>(</span><span>false</span><span>),</span>
      <span>hascaniuse</span><span>:</span> <span>z</span><span>.</span><span>boolean</span><span>().</span><span>default</span><span>(</span><span>false</span><span>),</span>
      <span>hascodepen</span><span>:</span> <span>z</span><span>.</span><span>boolean</span><span>().</span><span>default</span><span>(</span><span>false</span><span>),</span>
      <span>project</span><span>:</span> <span>z</span><span>.</span><span>string</span><span>().</span><span>optional</span><span>(),</span>
      <span>project_image</span><span>:</span> <span>z</span><span>.</span><span>string</span><span>().</span><span>optional</span><span>(),</span>
      <span>external_url</span><span>:</span> <span>z</span><span>.</span><span>string</span><span>().</span><span>url</span><span>().</span><span>optional</span><span>(),</span>
      <span>external_site</span><span>:</span> <span>z</span><span>.</span><span>string</span><span>().</span><span>optional</span><span>(),</span>
      <span>nofeed</span><span>:</span> <span>z</span><span>.</span><span>boolean</span><span>().</span><span>default</span><span>(</span><span>false</span><span>),</span>
      <span>noindex</span><span>:</span> <span>z</span><span>.</span><span>boolean</span><span>().</span><span>default</span><span>(</span><span>false</span><span>),</span>
    <span>}),</span>
<span>});</span>
```

I had run the blog template when I first created the site and the schema had included `Image` as a type, and I'd thought to use it for my 2 image frontmatter properties but turns out, it doesn't really work? I did not dig into it but there was a [whole GitHub issue](https://github.com/withastro/astro/issues/12673) and the conclusion was, just use a string. ¯\\\_(ツ)\_/¯

## [](https://dev.to/huijing/migrating-from-hugo-to-astro-3j95?#wrapping-up)Wrapping up

The first time I migrated, it took 3 days. This one sort of took 3 days as well. So maybe that's the average amount of time needed to migrate a website. I'm sure it will take less time if I ever complete paying off my tech debt of framework-locked partials/shortcodes/components. But maybe I'll actually stick with Astro since it's really close to HTML, CSS and Javascript.

Check back in 5 years I guess.
