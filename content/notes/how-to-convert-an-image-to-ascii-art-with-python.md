---
title: "How to Convert an Image to ASCII Art with Python in 5 Steps"
date: '2022-08-03T10:08:22-03:00'
category: webclip
summary: 'The article explains a simple Python workflow for turning an image into ASCII art by mapping character density to pixel brightness, using Pillow to read pixels, and writing the result to a text file.'
tags: ["python", "ascii-art", "pillow", "image-processing"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "How to Convert an Image to ASCII Art with Python in 5 Steps | by Emanuel Trandafir | Aug, 2022 | Level Up Coding"
    url: "https://levelup.gitconnected.com/how-to-convert-an-image-to-ascii-art-with-python-in-5-steps-efbac8996d5e"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2022-08/levelup-gitconnected-com--how-to-convert-an-image-to-ascii-art-with-python.md"
    kind: repo
---

The article shows a simple workflow for converting an image into ASCII art with Python. It first defines a string of ASCII characters ordered by how much screen space they take, then uses pixel brightness from RGB values to choose a matching character.

It then uses Pillow to open an image, read its pixels as (r, g, b) tuples, map each pixel to an ASCII character, build rows of text, and write the result to a file. The last step is to open the file in a text editor, zoom out, and view the image as ASCII art.

## Reading notes

- The method starts with an ordered set of ASCII characters, from those that occupy less surface to those that occupy more.
- Pixel brightness is computed by summing the red, green, and blue values of each pixel.
- The maximum brightness used in the calculation is 765, which comes from (255, 255, 255).
- A brightness weight is calculated from the length of the ASCII character list divided by the maximum brightness.
- Each pixel is turned into an index in the ASCII list by multiplying its brightness by that weight.
- The article uses Pillow to open the image and read its width and height.
- The code loops through the image pixel by pixel, gets each pixel with `image.getpixel((x, y))`, and maps it to a character.
- The generated rows are written into a text file.
- The result is meant to be viewed in a text editor after zooming out.
