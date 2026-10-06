---
url: "https://danielrapp.github.io/doppler/"
captured_at: "2015-03-10T21:53:24-03:00"
title: "Motion sensing using the doppler effect"
domain: "danielrapp-github-io"
---

# Motion sensing using the doppler effect

Recently I stumbled upon [an interesting paper](http://research.microsoft.com/en-us/um/redmond/groups/cue/publications/guptasoundwavechi2012.pdf) for
implementing motion sensing requiring no special hardware, *only a speaker and mic*! Unfortunately the paper didn't include
code to test it, so I decided to reproduce it here on the web!

![]()

## What is the doppler effect?

First of all, what is the doppler effect?
The [doppler effect](http://en.wikipedia.org/wiki/Doppler_effect) is a physical phenomenom which affects waves in motion.
The standard example is the effect on a fire engine siren as it quickly drives
past. When it moves *towards* you the sound waves are compressed, and so the
frequency becomes *higher*, and
when it moves *away* from you the frequency becomes *lower*.

This phenomenon actually has really wonderful applications in astronomy for figuring the speed
at which galaxies are moving towards or away from us by looking at the frequency shift of light,
but I digress.

Anyway, it's important to realize that the doppler effect would also occur
if you were to run towards the siren, rather than the siren moving towards you.
We'll use this principle in the next section.

## Measuring the doppler effect

In order to measure the doppler effect for motion detection on a conventional computer,
what you can do is send out a sinusoid at some known (inaudible) frequency, say, 20 kHz.
If something is moving in the room, then, after the sinusoid has bounced around on the walls and into the microphone, the
sound will shift in frequency. This can be measured by looking at the frequency spectrum
in the nearby region of the 20 kHz tone.

Note that you'll need to run Chrome with a fairly high speaker-volume for this to work optimally.

The frequency spectrum of the microphone input is plotted above. The peak towards the right
is due to the 20 kHz tone we're sending out. Try whistling to see the spectrum change.

Here's a closer look, zooming in on the 20 kHz region.
Try moving your hand *towards*
the mic/computer to see the bulge shift to *higher* frequencies, and
*away* from the computer to see it shift to *lower* frequencies.

## Applications

Now for the fun applications!

### Motion sensing

The most obvious application for this is motion sensing.
Below I've calculated the left and right bandwidth of the 20 kHz
region (defined as the number of frequencies to the left and right
that are within 99.9% in amplitude of the 20 kHz tone).
I've then attached their difference to the size of the box.

The effect this produces is that when you move your hand *towards*
the microphone, the box becomes smaller (you're *pushing*
it inwards), and if you move your hand *away* from the microphone,
the box becomes larger (you're *pulling* it outwards).

### Scrolling

A cool application to motion sensing, as suggested by the
[SoundWave paper](http://research.microsoft.com/en-us/um/redmond/groups/cue/publications/guptasoundwavechi2012.pdf),
is scrolling (see the video above). Click below to try it out.

This implementation doesn't have the double-tap feature for reversing
the scrolling-direction, instead it's just using the left and right bandwidth-difference.
Thus if you want to scroll down you have to move your hand
*quickly towards* the computer, and *slowly away* from the computer.

### Theremin

We can also create an instrument with this by simply modulating
the frequency of some base-tone, say at 440 Hz, based on the
difference between the left and right bandwidth!

This is reminiscent of a Theremin, in that you can contol
sound by moving your hands in free space, yet different
in that the Theremin is able to measure absolute distance from the base,
whereas we can only measure relative motion.

## Library

Did this give you any ideas? I also created [a small library](https://github.com/DanielRapp/doppler) to play around with this.
Just run

```
  doppler.init(function(bandwidth) {
     diff = bandwidth.left - bandwidth.right;
  });
```

to start experimenting.

Written by [Daniel Rapp](https://github.com/DanielRapp).
Check out the code for this [on Github](https://github.com/DanielRapp/doppler).
