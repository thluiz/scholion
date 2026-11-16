---
url: "https://dev.to/jcolag/colors-the-programming-way-5bf2"
captured_at: "2026-11-16T01:51:17+00:00"
title: "Colors, the Programming Way"
domain: "dev-to"
---

As a quick note, I [released](https://john.colagioia.net/blog/2020/03/11/colors.html) this on my blog today and so it can get to be (as I tend to be) a bit rambling. One big change is that the blog version has an additional section at the end with a bunch of non-color design resources that I recommend. Oh, and the original text is [on GitHub](https://github.com/jcolag/entropy-arbitrage) (licensed CC-BY-SA), so if anything seems muddy, by all means:

*   Leave a comment here,
*   Leave a comment on the blog,
*   File an issue on GitHub, or
*   Add a pull request!

* * *

I somehow end up involved in a lot of projects where a design needs a new color and it seems like a lot of people---developers, especially, but not exclusively---are terrified to work with color. But, here's the thing: It's possible to fake your way through most decisions like this with math.

The obstacle, though, is that the industry mostly operates on the [RGB color model](https://en.wikipedia.org/wiki/RGB_color_model), which is _terrible_ for showing relationships. It works well from a display standpoint, because most humans physically see the world through sensors detecting red, green, and blue light. However, there are at least two confounding factors.

First, our brain obviously reinterprets the physical input in a way that doesn't match reality. An important example of this is that visible colors are transmitted as photons with wavelengths from about 380 (violet) to 740 (red) nanometers. However, despite red and violet being as far apart in the spectrum as possible, we _see_ those two colors to be as similar as yellow (580nm) is to green (530nm).

The other big problem is that---surely related to the brain lying to you---as you've surely seen if you've tried to pick a color off a single on-screen pallete, is that RGB color spaces feel strangely asymmetrical, with reds and purples seeming to dominate the spectrum.

Something similar goes for the [CMY color model](https://en.wikipedia.org/wiki/CMY_color_model), commonly used in printing, with the most recognizable difference being that two of the three component colors (cyan and magenta) aren't generally a part of the natural world.

[![two colors](https://res.cloudinary.com/practicaldev/image/fetch/s--Wnr3SkJt--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://dev-to-uploads.s3.amazonaws.com/i/54jf3b5kdy2ne0dmqup4.png "two colors")](https://res.cloudinary.com/practicaldev/image/fetch/s--Wnr3SkJt--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://dev-to-uploads.s3.amazonaws.com/i/54jf3b5kdy2ne0dmqup4.png)

All that is to say that, if I present a pair of colors that we agree look nice together---let's say #e27d60 and #085dcb as shown to the right, for the sake of the example---and then ask for a third color that might work, finding that third color in the RGB space is a matter of trial and error or "taste." Give it a shot. I'll wait. And no, "gray" isn't a legitimate answer, since that has almost certainly already been taken. Nice try, though...

OK, so what can we do instead?

## [](#hue-can-do-it)Hue Can Do It!

The biggest change we need to make is to describe colors based on how they look, rather than how they can be broken down into components. The relevant broad terms, there, are [hue](https://en.wikipedia.org/wiki/Hue), [colorfulness](https://en.wikipedia.org/wiki/Colorfulness), and [lightness](https://en.wikipedia.org/wiki/Lightness). Lightness talks about how closely the color resembles black or white. Colorfulness deals with how closely the color resembles a gray of some lightness value. And hue involves how well the color can be described as a common color, such as red, blue, or yellow.

If every color in an image is the same (within some tolerance, of course) hue, that's a monochrome image. If we change the colorfulness and lightness together, we're creating a shade (mixing the color with black) or tint (mixing the color with white), because those change the lightness while reducing the colorfulness. If we change the colorfulness without the lightness, we're adding or removing a neutral gray. I can't find a term for changing the lightness without changing the colorfulness, but that's what you generally see in a "monochrome color scheme."

The hue, as mentioned is a number that gives a sense of how we would describe a color.

Hue

Color

0°

Red

30°

Orange

60°

Yellow

120°

Green

180°

Cyan

240°

Blue

270°

Violet

300°

Magenta

360°

Red, Again

That's not _quite_ how we imagine a rainbow---cyan and magenta seem to take up an oddly large amount of space for colors we don't ordinarily see---but it's pretty close and red does meet at both ends of the spectrum.

Let's look at our colors above, again, this time in terms of hue, saturation (the computer-y term for colorfulness), and lightness.

RGB

Hue

Saturation

Lightness

#e27d60

13.4°

69.1%

63.1%

#085dcb

213.8°

92.4%

41.4%

Hopefully, that's a bit more enlightening. The first color is a red-orange or a rust that's somewhat dull. The second is a bold but medium-lightness cyanish-blue. Right off the top, I think it's obvious that this is a useful notation, just because it gives a better intuition for what the color looks like, if you can remember most of that table above. And, y'know, you can just look it up quickly; no shame in that.

Have you ever heard a designer complain that the boss or client "would like the blue to be bluer"? They _might_ want the hue closer to 240°, but more likely is that they want to increase the saturation. They want the color to be "softer"? They probably mean bringing the lightness closer to its neighboring colors.

Anyway, let's pick our third color! I'm going to assume that the orange color is being used as a background, since otherwise we're guessing. The most naive color we can pick takes the difference between each of the three values and swings them around the other side of our background. So...

Color

Hue

Saturation

Lightness

Orange

13.4°

69.1%

63.1%

Blue

213.8°

92.4%

41.4%

Difference

200.4°

23.3%

\-21.7%

Orange - Δ

173.0°

45.8%

84.8

[![with a third color](https://res.cloudinary.com/practicaldev/image/fetch/s--VwN2qYMd--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://dev-to-uploads.s3.amazonaws.com/i/e0t58rlkf4l4c62h3uqm.png "with a third color")](https://res.cloudinary.com/practicaldev/image/fetch/s--VwN2qYMd--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://dev-to-uploads.s3.amazonaws.com/i/e0t58rlkf4l4c62h3uqm.png)

That gives us our new color (#c6eae6, if you want to play along in RGB), calculated to look as different from the orange as the blue is, sounds like---based on the middle-of-the-road saturation and high lightness---a washed-out cyan. Yes, the blue and cyan sound close, but this isn't necessarily bad. In fact, refer to the example to the right; the cyan is definitely not as bold part of the mix as the other two, but it's distinctive and doesn't clash with either color. Success!

And, of course, keep in mind that the monochrome discussion applies here, too: Adjust the lightness and saturation for the colors for supplemental colors. I'm just mechanically coming up with the non-hue values because I'm more confident in them, but a bolder or darker cyan is almost certainly a decent choice, too.

There's also a good chance we can take intermediate colors, too. Let's say 93.2° hue, 57.45% saturation, 73.95% lightness? That's a faded yellow-green (#b9e396), which you can draw on the sample on your own time.

This approach is referred to as choosing "adjacent colors," even though the colors are pretty far apart. It's what I suggested earlier, that you have one "main" color and then one color to either side, the same angle away. You'll occasionally hear the term "triadic" used in cases like this, where the main color is far (more than 90°) from its neighbors.

Oh, and there's one other important color to consider: The **complementary** color. Not "compl\*_i_\*ment," like free things that say nice things about you, but the opposite of a thing that makes it whole. Complementary colors are those whose hues are 180° apart from each other, so the complement to our rusty orange is 193.4° (#60c5e2), which is sort of a sky blue, and you'll hopefully notice that it's right between the bold blue and the cyan.

Generally speaking, complementary colors are too bold to use as more than an occasional accent or one color has a saturation or lightness that makes it feel muted. But that accent generally works inside any color scheme.

Notice that triadic colors are adjacent to the complementary color.

In addition to adjacent/triadic schemes, you'll also generally see reference to "tetradic" color choices. This is sort of a mix of adjacent and triadic, where the main color and its complement each get an adjacent "partner." Five colors generally get a spread that looks like triadic, but taking adjacent colors of the non-primary. Likewise, six colors split the primary color to two adjacent colors. If you need more than six colors with all of saturation and lightness values available, your vision might be too complicated.

Anyway, if the rusty orange is our main color, know the sky blue is complementary, and we have the bold blue as our secondary color, then the fourth color should be the bold blue's complement, 33.8° hue, 92.4% saturation, and 41.4% lightness (#cb7608), which is a brownish-orange. That doesn't look _so_ great, but it's more because the orange colors are too similar.

Let's take a more random example, and when I say _random_, I mean "let [http://randomcolour.com](http://randomcolour.com/) pick the main color." In this case, it gave me #8d1450, or 330.2° hue, 85.8% saturation, and 55.3% lightness, a dark reddish-magenta. We know the complementary hue is 330.2° - 180° = 150.2°, somewhere between green and cyan. Now we need a random angle, something less than 90° but larger than the 20° that felt too close to eyeball. Generating a random number in that range gives me 37°. So, 330.2 + 37 = 367.2° (or 7.2°, since this is a circle) and 150.2 + 37 = 187.2°.

[![Tetradic example](https://res.cloudinary.com/practicaldev/image/fetch/s--vS48T1qC--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://dev-to-uploads.s3.amazonaws.com/i/o27d4lan4up1t8dcmtys.png "Tetradic example")](https://res.cloudinary.com/practicaldev/image/fetch/s--vS48T1qC--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://dev-to-uploads.s3.amazonaws.com/i/o27d4lan4up1t8dcmtys.png)

(If you look at the table of hues above, you might notice that an angle of 30° or 60° is probably going to give recognizable results.

Is this a color scheme that's going to win awards? Probably not. The red looks pretty muddy against the purple, but the other combinations work well enough to function (especially with black, white, and grays added to the mix), it's not jarring (just invisible), and the red and cyan could almost certainly stand to be lightened instead of leaving all the saturation and lightness values the same. So, I'd call that a success.

If you have a keen eye (or downloaded the stylesheet to check), you should notice that my website uses a triadic color scheme, the background color being yellow, headers being red, and text in blue, with variants being steps up and down in lightness.

### [](#does-that-color-have-a-name)Does That Color Have a Name?

So, here's a related question with...yes, _obviously_ with the same answer: Given an arbitrary color, can we find the closest color with an official name?

As it turns out, I [created a tool](https://github.com/jcolag/color-namer) to solve this in [Go](https://golang.org/), back in 2016, mostly to experiment with the language. The hardest part of solving the problem was getting the list of named colors, which I just stripped out of [Wikipedia](https://en.wikipedia.org/wiki/List_of_colors_%28compact%29).

The program does what you would probably expect, at this point: It converts the RGB values to HSL (or HSV, which is mostly interchangeable) values and then calculates the distance between the input and all the colors to find the nearest.

I recommend trying the same thing---you can adapt the conversion algorithm/formula from my code or [this answer](https://stackoverflow.com/questions/39118528/rgb-to-hsl-conversion#39147465) on Stack Overflow---and comparing the results to the nearest color in RGB space (that is, the color with the nearest red, green, and blue intensities) to see which finds a better match. It might be interesting to try to find a color that matches better using the RGB distance.

## [](#contrast)Contrast

An important aspect of what makes a good color scheme, beyond just the colors looking acceptable next to each other. The World-Wide Web Consortium [suggests](https://www.w3.org/TR/2008/REC-WCAG20-20081211/#contrast-ratiodef) calculating contrast as (approximately) the ratio of [luminances](https://en.wikipedia.org/wiki/Luminance), which...OK, this is a little bit intricate.

*   Take each of the three color components (R, G, and B) as fractions between zero and one (i.e., the integer ÷ 255);
*   For values less than or equal to 0.03928, divide by 12.92;
*   For all _other_ values...
    *   Add 0.055,
    *   Divide by 1.055, and
    *   Raise to the 2.4 power;
*   Sum as 0.2126 × **R** + 0.7152 × **G** + 0.0722 × **B**.

[This Stack Overflow answer](https://stackoverflow.com/a/9733420/3438854) converts that mess to fairly straightforward JavaScript.  

```
function luminanace(r, g, b) {
    var a = [r, g, b].map(function (v) {
        v /= 255;
        return v <= 0.03928
            ? v / 12.92
            : Math.pow( (v + 0.055) / 1.055, 2.4 );
    });
    return a[0] * 0.2126 + a[1] * 0.7152 + a[2] * 0.0722;
}
function contrast(rgb1, rgb2) {
    var lum1 = luminanace(rgb1[0], rgb1[1], rgb1[2]);
    var lum2 = luminanace(rgb2[0], rgb2[1], rgb2[2]);
    var brightest = Math.max(lum1, lum2);
    var darkest = Math.min(lum1, lum2);
    return (brightest + 0.05)
         / (darkest + 0.05);
}
```

Enter fullscreen mode Exit fullscreen mode

If the results are better than 50% for each pair of colors in use, then the colors are probably readable against each other. Personally, I find it nice that this is something that can quickly work for user-defined color schemes---providing feedback without much overhead---in _addition_ to making it easier to know if a color scheme is usable.

## [](#color-blindness)Color Blindness

Closely related to ensuring contrast is validating color schemes for people with different kinds of color blindness. For example, I was once on a project where a client was using their corporate branding colors to highlight the most recent selections in a list. Our team's problem with fixing problems was that several people were color blind (they still are, individually, but the team no longer exists...) and so couldn't see much difference between the colors they gave us.

Unfortunately, converting colors to simulate color blindness is non-trivial for most programming, because it requires applying matrices to the color space. Each color "channel" (one of the technical terms for one of the R, G, or B values)is a weighted mix of magnitudes of of the three original channels.

We can do something like this, assuming that the "matrix" is a linear array with all the rows combined, for simpler notation.  

```
function crop(n) {
  return Math.floor(10 * (n<0 ? 0 : (n<255 ? n : 255))) / 10;
}
function AdjustChannelByMatrix(c, m, ch) {
  var offsets = {
    r: 0,
    g: 5,
    b: 10,
    a: 15
  };
  var i0 = 0 + offsets[ch];
  var i1 = 1 + offsets[ch];
  var i2 = 2 + offsets[ch];
  var i3 = 3 + offsets[ch];
  var i4 = 4 + offsets[ch];
  return crop(
    c.R * m[i0] +
    c.G * m[i1] +
    c.B * m[i2] +
    c.A * m[i3] +
    m[4]
  );
}
function AdjustColorByMatrix(c, m) {
    return({
      R: AdjustChannelByMatrix(c, m, 'r'),
      G: AdjustChannelByMatrix(c, m, 'g'),
      B: AdjustChannelByMatrix(c, m, 'b'),
      A: AdjustChannelByMatrix(c, m, 'a')
    });
};
```

Enter fullscreen mode Exit fullscreen mode

We're missing the matrices, of course. The best information I can find is based on the [Color Blindness Emulation](https://github.com/hail2u/color-blindness-emulation) project, made available under the terms of the [CC0 1.0 Universal Public Domain Dedication](https://creativecommons.org/publicdomain/zero/1.0/).  

```
{
  'Normal': [
    1,0,0,0,0,
    0,1,0,0,0,
    0,0,1,0,0,
    0,0,0,1,0,
    0,0,0,0,1
    ],
  'Protanopia': [
    0.567,0.433,0,0,0,
    0.558,0.442,0,0,0,
    0,0.242,0.758,0,0,
    0,0,0,1,0,
    0,0,0,0,1
  ],
  'Protanomaly': [
    0.817,0.183,0,0,0,
    0.333,0.667,0,0,0,
    0,0.125,0.875,0,0,
    0,0,0,1,0,
    0,0,0,0,1
  ],
  'Deuteranopia': [
    0.625,0.375,0,0,0,
    0.7,0.3,0,0,0,
    0,0.3,0.7,0,0,
    0,0,0,1,0,
    0,0,0,0,1
  ],
  'Deuteranomaly': [
    0.8,0.2,0,0,0,
    0.258,0.742,0,0,0,
    0,0.142,0.858,0,0,
    0,0,0,1,0,
    0,0,0,0,1
  ],
  'Tritanopia': [
    0.95,0.05,0,0,0,
    0,0.433,0.567,0,0,
    0,0.475,0.525,0,0,
    0,0,0,1,0,
    0,0,0,0,1
  ],
  'Tritanomaly': [
    0.967,0.033,0,0,0,
    0,0.733,0.267,0,0,
    0,0.183,0.817,0,0,
    0,0,0,1,0,
    0,0,0,0,1
  ],
  'Achromatopsia': [
    0.299,0.587,0.114,0,0,
    0.299,0.587,0.114,0,0,
    0.299,0.587,0.114,0,0,
    0,0,0,1,0,
    0,0,0,0,1
  ],
  'Achromatomaly': [
    0.618,0.320,0.062,0,0,
    0.163,0.775,0.062,0,0,
    0.163,0.320,0.516,0,0,
    0,0,0,1,0,
    0,0,0,0,0]
}
```

Enter fullscreen mode Exit fullscreen mode

So, for every color scheme we generate, we actually have _nine_ schemes to validate for usable contrast.

## [](#putting-it-together)Putting It Together

That might sound daunting, but bear in mind that most of the joy of software is that that we only need to work out (or find, as the case may be) the tedious math like this once, and we can apply that solution in bulk.

So, given what we know, we should be able to accept a primary color, angle, and geometry (adjacent, triadic, etc.), generate a color scheme, and validate---possibly adjust, if you're willing to have code iterate on saturation and lightness---the contrast of the resulting color scheme and how it will look to each of the eight kinds of people who are color blind.

It's still important to visually inspect the results, of course, but I'd call that a pretty long way to go without needing to think much about preference or taste.

### [](#however)However...

All of this should be taken as thinking about **new** work. If you're working on something for a company that exists, you can usually short-cut most of this work through the simple expedient of asking someone for the company's branding guidelines. I mean that literally. If the company has graphic artists, their manager is probably the keeper of the document. Otherwise, Human Resources often knows where to find it, since someone there is generally responsible for job fair banners and the like.

If you don't have inside contact with the organization or are too shy to ask your colleagues for help, you can also try searching the web for the company name and "branding guidelines." Companies involved in a lot of partnerships or have significant media attention generally keep their expected color palette, fonts, and assorted branding assets public.

If you have a branding guide, avoid deviating from it, if you can. Adding a small amount of an accent color is usually acceptable, but generally speaking, the further you are from the text, the more likely a manager is going to reject the design.

Good luck!

* * *

**Credits**: The header image is [Eine Innenansicht der Nasir-ol-Molk-Moschee in Schiras, Iran](https://commons.wikimedia.org/wiki/File:Nasir-al_molk_-1.jpg) by [Ayyoubsabawiki](https://commons.wikimedia.org/w/index.php?title=User:Ayyoubsabawiki&action=edit&redlink=1) and is released under the [Creative Commons Attribution-Share Alike 4.0 International](https://creativecommons.org/licenses/by-sa/4.0/deed.en) license.
