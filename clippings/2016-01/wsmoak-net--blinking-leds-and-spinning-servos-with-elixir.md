---
url: "http://wsmoak.net/2016/01/01/led-servo-elixir.html"
captured_at: "2016-01-03T09:11:26-03:00"
title: "Blinking LEDs and Spinning Servos with Elixir"
domain: "wsmoak-net"
---

# Blinking LEDs and Spinning Servos with Elixir

Jan 1, 2016

I’ve been looking for an automated cat feeder, and haven’t been very happy with the options. I need it to dispense a very small amount, and only when the cat is present, to avoid it piling up and letting her eat too much at once. (Bad things happen then.) The closest thing I found was the [Wireless Whiskers](http://www.wirelesswhiskers.com/ec/index.php) feeder, but I just wasn’t inspired to spend $150 and then fuss with programming it on a tiny screen. And then [@bitsandhops](https://twitter.com/bitsandhops) posted this:

Following the link from the [Robokitty source code](https://github.com/rachelnicole/robokitty) to the [servo](https://www.adafruit.com/products/154) she used, I discovered [Adafruit](https://www.adafruit.com/) and promptly sent them all my money.

I knew I wanted to use Elixir (of course!) so I went with a Raspberry Pi starter kit, and then discovered that the RPi doesn’t really *do* servos, so I added the Servo HAT. And a proximity sensor, etc., etc. Once it works I’ll do a post with all the details and a parts list.

Not having done anything with hardware since college (that course where I spent hours and hours in a windowless basement sticking Motorola chips into breadboards…) I started with the “Hello World” of the embedded space: blinking an LED.

(Actually I first wired it directly to power, which is what you see above. Later I moved that red wire over to GPIO pin #4 as described [here](https://projects.drogon.net/raspberry-pi/gpio-examples/tux-crossing/gpio-examples-1-a-single-led/).)

After reading a bunch of blog posts and with [@fhunleth](https://twitter.com/fhunleth)’s excellent [elixir\_ale](https://github.com/fhunleth/elixir_ale) library, (and his patience in answering LOTS of questions,) it turned out to be as simple as:

```
defmodule BlinkyAle 

   start 
      start_link:output
    blink_forever
  

   blink_forever 
    write
    :timersleep 
    write
    :timersleep 
    blink_forever
```

The elixir\_ale library even exports the pin you want to use to make it available, which is described in [this blog post](http://wtfleming.github.io/2015/12/10/embedded-elixir-raspberry-pi/). Under the covers this uses `sysfs` which entails writing a value to a file, after which Linux does the right thing.

## Servo

Having conquered blinking an LED, I turned to the servo. This meant soldering the header and some pins onto the HAT. I watched:

I spent a frustrating afternoon trying to reverse engineer [the Python example code](https://github.com/adafruit/Adafruit-Raspberry-Pi-Python-Code/blob/master/Adafruit_PWM_Servo_Driver/Adafruit_PWM_Servo_Driver.py) that Adafruit provided, and (after reading more blogs and asking more questions) I figured out that I was *supposed* to have a Datasheet to work from.

Some searching and one [Support Forum post](https://forums.adafruit.com/viewtopic.php?f=50&t=86471) later, I confirmed that the [PCA9685 Datasheet](https://www.adafruit.com/datasheets/PCA9685.pdf) is what I needed, and things got MUCH easier.

With it all plugged in and working:

[ElixirSpinny](https://vimeo.com/150140381) from [Wendy Smoak](https://vimeo.com/user1032254) on [Vimeo](https://vimeo.com/).

The code is here: [Spinny](https://gist.github.com/wsmoak/6da34768fdfd6d4c2d1d).

## Proximity

For our last trick, it’s back to the LED, this time with the VCNL4010 proximity sensor wired up.

[ElixirProximityBlinky](https://vimeo.com/150217372) from [Wendy Smoak](https://vimeo.com/user1032254) on [Vimeo](https://vimeo.com/).

Here is the [code that makes it work](https://gist.github.com/wsmoak/c1fd4e95578933e23388).

This was a matter of connecting the right pins from the sensor to the RPi, as shown in in the [Adafruit example project](https://learn.adafruit.com/festive-feather-holiday-lights) and the [Datasheet](https://www.adafruit.com/images/product-files/466/vcnl4010.pdf). [@fhunleth](https://twitter.com/fhunleth) explained that the SDA and SCL pins are what put something “on the i2c bus” so it can be addressed and written to / read from.

## Next Up

Next up I’ll need to get both the servo and the proximity sensor attached at the same time, so that instead of turning on a light when something is near, I can spin the servo. As soon as the next box from Adafruit arrives, I’ll have the additional parts I need to make that happen.

### References
