---
url: "https://dev.to/illarious/what-i-learned-while-implementing-a-colorblind-mode-for-my-belgian-wage-calculator-site-51f0?"
captured_at: "2026-09-25T00:09:49+01:00"
title: "What I learned while implementing a colorblind mode for my Belgian Wage Calculator site"
domain: "dev-to"
---

This is a retrospective article about what I learned while implementing a colorblind mode for my [Belgian Wage Calculator](https://belgian-wage-calculator.vercel.app/?share=EQjcPs)(no ads or selling of data) that should work well for both green(Deuteranomaly/Deuteranopia) and red(Protanomaly, protanopia) colorblindness.

* * *

Opia, Anomaly...

Explaining those is as good a starting point as any, I suppose!

Colorblindness is a spectrum for each of these:

*   Those who are completely colorblind(Achromatopsia, loss/dysfunction of all cone types, extremely rare: 0.003% of the population)
*   Those who have blue colorblindness(Tritanomaly, tritanopia, happens in +- 0.3% of the population, female and male alike)
*   Those who have green colorblindness(Deuteranomaly, Deuteranopia)
*   and those who have red colorblindness(Protanomaly, protanopia)

When considered together, red/green colorblindness occur in approximately 8% of men and 0.5% of women.

Of these, there's both those with a complete lack of that type of receptors(green or red or blue) as well as those that fall anywhere between there and regular vision.

Those that fall in between have (deuteran/protan/tritan)omaly while those who have complete colorblindness in one receptor have (deuteran/protan/tritan)opia.

* * *

Now that we've got that out of the way, what mistaken preconception did I have?

The major preconception I had was that I could choose the proper counter colors for one receptor and that those with that type of colorblindness would be able to properly distinguish it, even with full colorblindness in that receptor.

However, when I used this extension for Firefox that I had found, called "Let's get colorblind', which simulates these conditions and allows setting the strength of the deficiency...

I noticed that when I'm looking at the actual RGB color scale that total colorblindness in either the red or green receptor mostly reduces your available color palette to shades of white, black, yellow and blue, with some differences between both types.

Nothing explains better than some visual examples though so, here's the color spectrum as those with regular vision see it:  
[![ ](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fuhwd2yickt07hqo2lf9o.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fuhwd2yickt07hqo2lf9o.png)

and here is the exact same color spectrum with 100% green colorblindness:  
[![ ](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fmb4k9zlvgto9azo54ogb.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fmb4k9zlvgto9azo54ogb.png)

And for 100% red colorblindness:  
[![ ](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fmm5h01crt8ee3dbbxd51.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fmm5h01crt8ee3dbbxd51.png)

To be honest, I did not expect that the end result for both would be a relatively similar colorspectrum, I assumed the difference would be more significant and similarly contrasting just like with blue colorblindness:  
[![ ](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fvibki10p1pexgbnztq41.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fvibki10p1pexgbnztq41.png)

From what I can tell, the blue filter is mostly accurate as well, but the extension didn't make it as "washed out/dark" as it should be near the darker blue section in the image for those with tritanopia:

[![ ](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fbuhxykchmp9poa0ul0yx.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fbuhxykchmp9poa0ul0yx.png)

* * *

In any case... This leads me into part two of that preconception I had.

I assumed picking certain colors would result in certain colors, but in reality everything is shifted depending on the severity, for example, this is at 100%:  
[![ ](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F6bj09r6xa7i7xtwh7la9.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F6bj09r6xa7i7xtwh7la9.png)

To get a light blue equivalent for a person with green colorblindness, the intuitive move, namely moving further into the cyan spectrum is wrong.

Instead, to achieve it, we must move into the purple/pink spectrum.

* * *

I also got advice from the r/Colorblind subreddit that I should work more with light and dark gradations for backgrounds rather than relying on colors

Once I realized these things and put it all together, finding a better color palette suddenly became a lot more manageable.

Note: When hosted here, for this article the images appear to be more blurry when opened in a new tab and less distinguishable than when looking at the site with the filter active directly, so keep that in mind.

Before I arrive at my solution though, let me first show you exactly what my site looks like to me, and what it looks like to those who suffer from red or green colorblindness with severe deficiency, starting with regular vision:  
[![ ](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F7d6xeclgd2q2wdt96gxx.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F7d6xeclgd2q2wdt96gxx.png)

Looks quite readable right? Clear red for negative, clear green for positive, proper contrast everywhere....

Yet this is what those with 100% green colorblindness see. The negative and positive colours become relatively undistinguishable, especially when combined with certain background colors:  
[![ ](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fup0gvut8jhemwufy2p9o.webp)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fup0gvut8jhemwufy2p9o.webp)

And now we get to what to me is especially interesting, how funky my green colorblind version is, exactly!

[![ ](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fmeosbq6o5pxwifb78jce.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fmeosbq6o5pxwifb78jce.png)

Your first instinct may be "WHAT IS GOING ON WITH THE aggressive purple?!"

But remember, the color spectrum shifted!

So then, what does someone with 100% green colorblindness truly see?

[![ ](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F2redppuk2qgetc3v8aep.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F2redppuk2qgetc3v8aep.png)

Interesting, no?

That was for total green colorblindness but what if we consider what those with partial green colorblindness see instead?

Is it still such an aggressive purple?  
This is at 50%:  
[![ ](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Flv3ly1ahtrey5mgknwo9.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Flv3ly1ahtrey5mgknwo9.png)

Quite a bit more pink/purple, but readable and easily distinguishable!

After my first attempt at a combined colorblind mode for both green and purple, I decided to make two versions instead that the user can toggle through.

I chose to provide one for green colorblindness and one for red colorblindness(image is at 100% red colorblindness):  
[![ ](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F8cqy9m83b5f8amxe43n7.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F8cqy9m83b5f8amxe43n7.png)

I didn't add a specific mode for blue colorblindness, considering the non-colorblind version actually looks properly distinguishable, even if it does look a bit errr... cyberpunky.  
[![ ](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fhwqoumsi8862l9n01cia.webp)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fhwqoumsi8862l9n01cia.webp)

* * *

Something else that was interesting to me too, though, is that the red colorblind mode is actually quite usable as well for those with certain degrees of green colorblindness.

So it's quite possible some with green colorblindness might prefer the red colorblind mode instead, which makes sense if you consider the similarities in color spectrum for both, as mentioned earlier.

My hope is that at least one mode will be perfect for each person, no matter what severity of colorblindness they may have, even total colorblindness. For those, basic design principles like clear + and - for positive/negative values were employed.

But again, apart from the extension, I have no way to know unless those who actually have these conditions test it out, so do let me know!

* * *

While I have no idea how many who suffer from colorblindness will actually use the site, I'm glad I did it either way.

It was a lovely rabbit hole of information to dive into and ended up giving me a whole new perspective and consideration for those who suffer from any of these conditions.

Making this post was just as much fun for me, so I certainly hope you enjoyed it too(and perhaps learned a thing or two as well!)

* * *

A genuine heartfelt shoutout to all those at r/Colorblind for the feedback provided and entertaining my first, less than ideal version!

P.S, I'm still fiddling around with the backgrounds here and there to ensure proper contrast for the entire page, so despite being 90% of the way there, it's still a WIP.

Feel free to ask questions, and, if you yourself are colorblind and notice any issue or remaining misconceptions, do let me know in the comments :)

* * *

Originally posted on my Patreon as a [free post](https://www.patreon.com/posts/148728858).  
If you found this interesting or helpful, you can support my work via [Buy Me A Coffee](https://buymeacoffee.com/illarious) as well as [Patreon](https://www.patreon.com/cw/illarious).

Have a lovely day!
