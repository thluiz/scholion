---
title: "Hacking Super Mario Bros. with Python"
date: '2013-01-15T11:27:53-03:00'
category: webclip
summary: 'The post shows how to scrape Super Mario Bros. graphics from an NES ROM, assemble the pattern tables, and animate Mario entirely in Python with matplotlib.'
tags: ["python", "matplotlib", "animation", "nintendo"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Hacking Super Mario Bros. with Python - Pythonic Perambulations"
    url: "http://jakevdp.github.com/blog/2013/01/13/hacking-super-mario-bros-with-python/"
    kind: repo
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2013-01/jakevdp-github-com--hacking-super-mario-bros-with-python.md"
    kind: repo
---

The post explains how to build a Super Mario Bros. animation in Python and matplotlib by extracting pixel data directly from the game ROM. It uses the NES pattern tables to recover foreground and background tiles, then combines them into frames and animates them with matplotlib tools.

## Reading notes

- The project starts from animated gifs inspired by Super Mario Bros. and asks whether matplotlib can create similar animations in Python.
- The animation was made entirely in Python and matplotlib by scraping image data from the Super Mario Bros. ROM.
- NES ROMs store graphics as raw byte strings made of 2-bit, 8x8 thumbnails, organized into separate foreground and background pattern tables.
- The raw file bits can be extracted with numpy and zipfile, using unpackbits on either the uncompressed file or the first file in a zip archive.
- The pattern tables are not at a fixed location in the file, so the author visualizes the data and finds the graphics by eye.
- Each thumbnail is built from two 64-bit chunks, giving two bits per pixel and four possible colors.
- The foreground table contains Mario, enemies, mushrooms, and fire flowers.
- The background table contains numbers, text, bricks, blocks, clouds, bushes, and coins.
- Full sprites are assembled from multiple tiles, with big Mario using eight tiles and small Mario using four.
- Colors are added by assigning a matplotlib colormap to the assembled tile images.
- The animation is built by choosing frame contents and stitching them together with matplotlib.animation.
- The code defines NESGraphics for extracting and drawing tiles and NESAnimator for composing and animating frames.
- The final animation includes a scrolling background, Mario, koopa troopas, and goombas.
- The author notes that a more interactive Mario would likely be better handled in Tkinter or pygame.
