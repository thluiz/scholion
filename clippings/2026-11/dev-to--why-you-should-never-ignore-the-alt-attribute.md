---
url: "https://dev.to/nataliedeweerd/why-you-should-never-ignore-the-alt-attribute-2gh0"
captured_at: "2026-11-16T19:49:02+00:00"
title: "Why you should never ignore the alt attribute"
domain: "dev-to"
---

The alt attribute was first introduced in HTML 2 (1995), so it’s been with us for an awfully long time. This little three-letter attribute is so important; not only does it help with Search Engine Optimisation (SEO), but it also improves the accessibility of your site.

## [](#what-is-the-alt-attribute)What is the Alt Attribute?

The alt attribute is a bit of code which gets added to your image to allow screen readers and search engine crawlers to understand what the image is. Below is an example of how you would add the alt attribute to your HTML.  

```
<img src="image_url.jpg" alt="Alt attribute text goes here" />
```

Alt attributes are an alternative to an image and the text should reflect the nature of the image; for example, an error icon should state “Error!” rather than a literal description of the image (e.g. “Red circle with a white X inside”).

Context is also incredibly important when thinking about the text to add to your alt attribute. The detail you add needs to correspond to the content of the rest of your page.

If you don’t include your alt attribute then screen readers may spend an eternity reading out the URL for an image. Decorative images may not need any text within their alt attribute, so an empty alt attribute should be used rather than excluding it completely.

## [](#alt-attributes-and-accessibility)Alt attributes and accessibility

Accessibility on any site is vital, and alt attributes help by offering a readable text version of an image. If a user has to use a screen reader (due to visual impairment) then they will have the alt text read to them. This means that the text you put into your alt attribute needs to make sense within the context of your page.

## [](#how-the-alt-attribute-aids-your-seo)How the alt attribute aids your SEO

Bots can’t read an image; however, they can read alt text. As long as you choose a logical file name, and sensible text for your alt attribute, it will help improve your SEO as it gives the search engine crawler a broader picture of the content on your page, and website as a whole.

Be aware, that if you copy text from the same page and paste it into the alt attribute, bots crawling your site may think that you’re purposefully spamming the phrase and thus it can be detrimental to your overall SEO score.

## [](#good-examples)Good Examples

[![A good example of an Alt Attribute - "A single potted plant on a windowsill"](https://res.cloudinary.com/practicaldev/image/fetch/s--kiV0VoQK--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://dev-to-uploads.s3.amazonaws.com/i/thqwm5ufudrv1972rnh7.jpg)](https://res.cloudinary.com/practicaldev/image/fetch/s--kiV0VoQK--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://dev-to-uploads.s3.amazonaws.com/i/thqwm5ufudrv1972rnh7.jpg)  
_A single potted plant on a windowsill_

This is clear and concise, and tells us exactly what is happening in the picture. By including the fact that the potted plant is on its own, alleviates any ambiguity as to how many plants there are.

[![A good example of an Alt Attribute - "A refreshing glass of water with sliced lemon and mint"](https://res.cloudinary.com/practicaldev/image/fetch/s--aphb-SGB--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://dev-to-uploads.s3.amazonaws.com/i/p992tbrdyxrrddn0frh5.jpg)](https://res.cloudinary.com/practicaldev/image/fetch/s--aphb-SGB--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://dev-to-uploads.s3.amazonaws.com/i/p992tbrdyxrrddn0frh5.jpg)  
_A refreshing glass of water with sliced lemon and mint_

Whilst including the fact that the drink is refreshing is subjective, it may be useful if the site is about a person’s well-being, or mental health. Only include adjectives if it makes sense within the context of your site.

## [](#bad-examples)Bad Examples

[![A bad example of an Alt Attribute - "Boat"](https://res.cloudinary.com/practicaldev/image/fetch/s--SvEoCZvA--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://dev-to-uploads.s3.amazonaws.com/i/bentthrps407ha9q2pia.jpg)](https://res.cloudinary.com/practicaldev/image/fetch/s--SvEoCZvA--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://dev-to-uploads.s3.amazonaws.com/i/bentthrps407ha9q2pia.jpg)  
_Boat_

There just isn’t enough information here about the image - plus, I'd argue it's a ship, not a boat. Depending on the context of the site, the location and type of ship may be important. If they’re not, include detail about the appearance of the ship, whether it’s decrepit, etc. For example, a better alt attribute here could be "A white cruise ship named Seaborn Quest".

[![A bad example of an Alt attribute - "The word RESOLUTIONS spelt out in Scrabble letters. The R is worth 1 point, the E is worth 1 point, the S is worth 1 point, the O is worth 1 point, the L is worth 2 points, the U is worth 3 points, the T is worth 3 points, the I is worth 1 point, the N is worth 1 point. In total the word scores 15 points."](https://res.cloudinary.com/practicaldev/image/fetch/s--9b5kEblf--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://dev-to-uploads.s3.amazonaws.com/i/cez0xxgoysveqtoea1kc.jpg)](https://res.cloudinary.com/practicaldev/image/fetch/s--9b5kEblf--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://dev-to-uploads.s3.amazonaws.com/i/cez0xxgoysveqtoea1kc.jpg)  
_The word RESOLUTIONS spelt out in Scrabble letters. The R is worth 1 point, the E is worth 1 point, the S is worth 1 point, the O is worth 1 point, the L is worth 2 points, the U is worth 3 points, the T is worth 3 points, the I is worth 1 point, the N is worth 1 point. In total the word scores 15 points._

This is just unnecessarily long... Alt text this long belongs in a caption, rather than an alt attribute – especially if the information is important. Ideally, just the first sentence should be used. It’s important not to make your alt text too long. It needs to be as succinct and descriptive as possible.

## [](#in-summary)In Summary

_Don't forget the alt attribute!_

Even if its left empty, those with screen readers will thank you! And if you are adding text, make sure it's relevant to the content.

##### [](#photo-credits)Photo Credits

[A single potted plant on a windowsill](https://www.pexels.com/photo/green-potted-plant-beside-window-3686293/)  
[A refreshing glass of water with sliced lemon and mine](https://www.pexels.com/photo/water-drink-fresh-lemons-3303/)  
[A white cruise ship named Seaborn Quest](https://www.pexels.com/photo/white-cruise-ship-on-blue-body-of-water-during-daytime-144237/)  
[The word RESOLUTIONS spelt out in Scrabble letters](https://www.pexels.com/photo/scrabble-resolutions-3237/)
