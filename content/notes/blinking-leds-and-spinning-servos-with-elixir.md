---
title: "Blinking LEDs and Spinning Servos with Elixir"
date: '2016-01-03T09:11:26-03:00'
category: webclip
summary: 'The author describes building an Elixir-based Raspberry Pi setup for an automated cat feeder, starting with an LED blink test, then a servo, then a proximity sensor, using Adafruit parts and library help.'
tags: ["elixir", "raspberry-pi", "adafruit", "embedded-hardware"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Blinking LEDs and Spinning Servos with Elixir"
    url: "http://wsmoak.net/2016/01/01/led-servo-elixir.html"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2016-01/wsmoak-net--blinking-leds-and-spinning-servos-with-elixir.md"
    kind: repo
---

The post follows the author's effort to build an automated cat feeder with Elixir on a Raspberry Pi. She begins with a simple LED blink as the first embedded project, then moves on to a servo driven by an Adafruit HAT, and finally adds a VCNL4010 proximity sensor. The main thread is that each step required more wiring, more reading, and more help from library documentation and datasheets.

## Reading notes

- She wanted a feeder that dispenses a very small amount only when the cat is present.
- She chose Elixir for the project and bought a Raspberry Pi starter kit plus a Servo HAT.
- Blinking an LED was the first hardware test after a long break from embedded work.
- The LED example used the elixir_ale library and GPIO pin access through sysfs.
- For the servo, she had to solder the HAT headers and learn from the PCA9685 datasheet.
- She says the Adafruit Python example was hard to reverse engineer, but the datasheet made the task easier.
- The proximity sensor was wired to the Raspberry Pi so the LED could respond to nearby objects.
- She notes that SDA and SCL are the pins that place a device on the i2c bus.
- The next step was to attach the servo and proximity sensor at the same time so the servo could spin when something is near.
