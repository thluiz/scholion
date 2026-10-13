---
title: "The Mathematics Behind xkcd: A Conversation with Randall Munroe"
date: '2012-11-06T11:28:37-03:00'
category: webclip
summary: 'Interview with Randall Munroe about how he builds mathematically dense xkcd comics, from tic-tac-toe and self-description to movie charts, coding shortcuts, hand iteration, and his view of computer science and math.'
tags: ["xkcd", "mathematics", "comics", "computer-science"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "The Mathematics Behind xkcd: A Conversation with Randall Munroe"
    url: "http://www.maa.org/mathhorizons/MH-Sep2012_XKCD.html"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2012-11/maa-org--mathematics-behind-xkcd-conversation-with-randall-munroe.md"
    kind: repo
---

Randall Munroe explains how several xkcd comics were built from hand drawing, Photoshop, and repeated iteration rather than large programs. He says he often chooses the method that is easiest to carry through and that still produces the result he wants, even when that means doing a lot of work by hand.

## Reading notes

- In the tic-tac-toe comic, he drew only part of the chart by hand, then mirrored and flipped it in the computer, because making the whole tree by hand would have taken too long.
- He chose an upper-left opening move because it let him show winning lines that are not the moves everyone expects.
- He wanted a way to present the full game tree on one page and still make the choices at each stage feel like a grid of nine possibilities.
- He likes that the tic-tac-toe comic uses boxes only for end states, which keeps nested boxes from wasting space.
- For the self-description comic, he did not write code first; he reasoned through the panels and their fixed-point behavior.
- He measured the ink amounts with Photoshop, pixel counts, a calculator, and hand calculations.
- He generated the third panel by cloning and shrinking the image, then iterating it about 10 or 12 times by hand.
- He says he often chooses the lazy solution that does not require learning new tools.
- He estimates the self-description comic took about five hours.
- He thinks the fixed point is unique, and that solving it algebraically would be possible but hard.
- For the movie narrative chart, he drew it by hand without using a computer.
- He says people often imagine he used a program, but in that case he had the patience to do the thing that no one would bother to do.
- He notes that some comics involved more code than people might expect, and one had a bug tied to floating-point comparison in Perl’s libraries.
- On the purity chart, he distinguishes coding from computer science and says computer science studies what can be done with computers rather than computers themselves.
- He places himself between physicists and mathematicians because he likes theory but can get lost when abstraction gets too far from what he can picture.
- He mentions his wife’s cancer treatment and says he does not want to speak too harshly about biologists, since he depended on people in medicine.
- He ends by saying he enjoys detailed audience interest in how the comics are made.
