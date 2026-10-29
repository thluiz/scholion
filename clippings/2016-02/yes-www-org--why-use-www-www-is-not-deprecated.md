---
url: "http://www.yes-www.org/why-use-www/"
captured_at: "2016-02-07T22:22:27-03:00"
title: "Why use www? – www. is not deprecated"
domain: "yes-www-org"
---

# Why use www?

This page is intended for webmasters who are looking for information about whether or not to use `www` in their [canonical web site URLs](http://www.mattcutts.com/blog/seo-advice-url-canonicalization/).

First, a bit of terminology. The domain name without `www` is sometimes referred to as a naked domain, and I’ll refer to it as such here.

### Why should I use www?

You should use `www` because today you have a small web site, and tomorrow you want a big web site. *Really* big.

The technical reasons to use `www` primarily apply to the largest web sites which receive millions (or more) of page views per day, web sites with a large number of services across several subdomains, and virtually any web site hosted in “the cloud” by an application service provider.

Heroku, for instance, [strongly recommends against using naked domains](https://devcenter.heroku.com/articles/avoiding-naked-domains-dns-arecords). When using a provider such as Heroku or Akamai to host your web site, the provider wants to be able to update DNS records in case it needs to redirect traffic from a failing server to a healthy server. This is set up using DNS CNAME records, and the naked domain cannot have a CNAME record. This is only an issue if your site gets large enough to require highly redundant hosting with such a service. But who *doesn’t* want their site to get that large? In order to not use `www`, you will have to run your own server farms and you will be unable to use such services to their fullest extent. (See also: [Why does Heroku warn against “naked” domain names?](http://serverfault.com/q/408017/126632))

Another reason has to do with cookies. One common web site optimization is to serve static content from a subdomain, such as `static.example.com`. If you are using `www`, then this is no problem; your site’s cookies won’t be sent to the `static` subdomain (unless you explicitly set them up to do so). If you use the naked domain, the cookies get sent to all subdomains (by recent browsers that implement [RFC 6265](http://tools.ietf.org/html/rfc6265)), slowing down access to static content, and possibly causing caching to not work properly. The only way to get around this problem and keep the naked domain is to buy a second domain name just for your static content. Twitter, for instance, which does not use `www`, had to buy new domain names just for static content. Of course, if you explicitly share your cookies across all your subdomains, for instance to implement single sign-on across various services on subdomains of your site (Google does this), then you too would have to buy a new domain name in this circumstance anyway. (See also: [What’s the point in having “www” in a URL?](http://serverfault.com/q/145777/126632))

Speaking of cookies, if you decide to use the naked domain, but want to put services on subdomains and share cookies between them, you’ll quickly find out that it doesn’t work right in all cases unless you have a subdomain set the cookie — and then it doesn’t work for the naked domain. The fix for this is to use [RFC 6265](http://tools.ietf.org/html/rfc6265) (formerly [RFC 2965](http://tools.ietf.org/html/rfc2965)) cookies, which can be shared between the naked domain and subdomains, but some popular web application packages still do not implement RFC 2965 properly or at all, let alone RFC 6265. (See also: [Can subdomain.example.com set a cookie that can be read by example.com?](http://serverfault.com/a/153466/126632))

You may not run into any of these issues today, but as your web site grows, you eventually will. Using `www` today and in the future makes you more prepared to handle the challenges of growing a web site beyond a single server. It *can* be done without using `www` in many circumstances, but it’s much easier with.

### Should I redirect no-www to www?

Redirection ensures that visitors who type in your URL reach you regardless of which form they use, and also ensures that search engines index your canonical URLs properly.
