---
title: "CakeRobot - A Gesture Driven Robot That Follows Your Hand Movements Using Arduino, C# and Kinect"
date: '2013-11-03T15:01:47-03:00'
category: webclip
summary: 'The post outlines how to build CakeRobot with Arduino, Bluetooth, and Kinect, from choosing parts and wiring the chassis to reading skeletal hand positions and sending motor commands.'
tags: ["arduino", "kinect", "robotics", "bluetooth"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Amazedsaint's Tech Journal: CakeRobot - A Gesture Driven Robot That Follows Your Hand Movements Using Arduino, C# and Kinect"
    url: "http://www.amazedsaint.com/2013/10/cakerobot-gesture-driven-robot-that.html"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2013-11/amazedsaint-com--cakerobot-gesture-driven-robot-arduino-csharp-kinect.md"
    kind: repo
---

The post describes a DIY robot that is controlled with Kinect hand movements and communicates with the robot over Bluetooth. It gives a quick build path, links to the GitHub code, and says the same setup could also use a phone as the controller.

## Reading notes

- The author built a simple robot over a few weekends after getting interested in hobby electronics again.
- The robot can be controlled using Kinect, and the post says the code may help others build one.
- If a Kinect is not available, the controller can be made with a phone, since Bluetooth is used between controller and robot.
- The build starts with learning Arduino or Netduino, and the example uses Arduino.
- The Arduino section points readers to the IDE, a tutorial, a board to buy, and the meaning of pins such as GND, 5V, analog, digital, PWM, and AREF.
- For Kinect, the post says to install Kinect SDK 1.7 and watch Microsoft how-to videos.
- Bluetooth protocols are listed as another area to learn.
- The parts list includes a Dagu Magician chassis, an Arduino board with motor driver, a Bluetooth shield, breadboards, jumper wires, a Bluetooth dongle for the computer, a distance sensor, a battery pack, resistors, more sensors, and basic tools.
- The author says some hours are needed to learn how to program each component.
- The Arduino driver uses pins D9 and D7 for the left motor, and D10 and D8 for the right motor.
- Motor direction is set with digitalWrite, and motor speed is set with analogWrite from 0 to 255.
- The Arduino code receives Bluetooth commands as strings, such as speedl and speedr.
- The controller code tracks the skeletal frame and uses the height of the hands relative to the hips to set direction and speed.
- If a hand drops below its hip, that motor is set to zero.
- If a hand rises above its hip, speed is calculated from the hand height difference and capped at 230.
- The post closes by pointing to the GitHub repository and inviting readers to fork and expand the project.
