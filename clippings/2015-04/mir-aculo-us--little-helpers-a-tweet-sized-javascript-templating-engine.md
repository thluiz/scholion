---
url: "http://mir.aculo.us/2011/03/09/little-helpers-a-tweet-sized-javascript-templating-engine/"
captured_at: "2015-04-25T22:17:40-03:00"
title: "mir.aculo.us JavaScript with Thomas Fuchs » Blog Archive » Little helpers: a tweet-sized JavaScript templating engine"
domain: "mir-aculo-us"
---

# [Little helpers: a tweet-sized JavaScript templating engine](http://mir.aculo.us/2011/03/09/little-helpers-a-tweet-sized-javascript-templating-engine/)

March 9th, 2011

JavaScript libraries don’t have to big and clunky to be useful. Often, less is more. I’m doing a lot of work with single-page apps and short-lived event sites and visualizers—often coming up with some helper code while doing it, because it’s faster to implement small things yourself then to [search for existing solutions](http://stackoverflow.com/questions/552934/what-javascript-templating-engine-do-you-recommend), with none of them really doing what you want.

An example? Templating. While there’s a gadzillion more or less awesome templating engines for JavaScript out there, in one case I needed something übersimple—and tried to fit it into a tweet (for no particular reason).

|  |
| --- |
| `function` `t(s,d){` |

|  |
| --- |
| `for``(``var` `p` `in` `d)` |

|  |
| --- |
| `s=s.replace(``new` `RegExp(``'{'``+p+``'}'``,``'g'``), d[p]);` |

|  |
| --- |
| `return` `s;` |

|  |
| --- |
| `}` |

Call it like this:

|  |
| --- |
| `t(``"Hello {who}!"``, { who:` `"JavaScript"` `});` |

|  |
| --- |
| `// "Hello JavaScript!"` |

|  |
| --- |
| `t(``"Hello {who}! It's {time} ms since epoch."``, { who:` `"JavaScript"``, time: Date.now });` |

|  |
| --- |
| `// "Hello JavaScript! It's 1299680443046 ms since epoch."` |

If I’d need larger templates, I’d probably go with one of the engines that allows you to store HTML templates in `<script>` tags, but for my use case (just some messages) this worked beautifully.

**Update** Thanks to [Daniel Herzog](http://twitter.com/danfooo) to point out that `replace` is [automatically executing functions](https://developer.mozilla.org/en/JavaScript/Reference/Global_Objects/String/replace#Specifying_a_function_as_a_parameter), which basically cut my code in half. Awesome.

## Related Posts
