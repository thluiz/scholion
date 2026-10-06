---
url: "https://journal.helabs.com/3d-modeling-for-ui-designers-3c59a75caad0#.d6zeevyvv"
captured_at: "2016-05-02T10:03:01-03:00"
title: "3D modeling for UI Designers — The HE:journal"
domain: "journal-helabs-com"
---

# 3D modeling for UI Designers

#### Part 1 — Creating 3D objects

Recently I've had the opportunity to work in an awesome project at [HE:labs](http://helabs.com/en/). It was an interactive isometric map where each building represented a project and on mouse over we displayed a short looping animation as a preview of what that project was about. I got some really good feedback for this app and the client was really happy with it, so I felt like it could be a good opportunity to explain a really simple approach for creating 3D images and animations for apps using Maya.

If you never ever opened Maya, the interface can be a bit scary. With so many little buttons and options, it’s quite easy to get lost.

![1*1J_qUKbBo9my7xoEZDlONA.gif](journal-helabs-com--3d-modeling-for-ui-designers-the-he-journal/ab3fee8d269ad7caff77c6720e9eca0f.gif)

This was me, opening Maya for the first time

But I'll try my best to make this tutorial simple, so let's focus on what's important for us. I'm going to split this tutorial into 3 parts. The first one for creating 3D models, the 2nd one for rendering out images and the third part for creating simple 3D animations.

I’m using **Maya 2015**. The interface tends to change a bit from one version to the other, so if you don’t have Maya installed on your computer, I suggest installing the same version to follow along :)

#### Understanding the interface

First of all, make sure that the dropdown menu on the top left corner is set to "**polygons**". Each option of this dropdown unlocks several other options on the top menu, so it's important that it's set to polygons while we're creating 3D objects.

![1*n-Dbv4ZH-7b4aBVlX1Yg4w.png](journal-helabs-com--3d-modeling-for-ui-designers-the-he-journal/35296f3744b573fd7729659c47095256.png)

![1*n-Dbv4ZH-7b4aBVlX1Yg4w.png](journal-helabs-com--3d-modeling-for-ui-designers-the-he-journal/db050db2eb5b3395e5d660574c90b9bf.png)

When you change the option on the dropdown, you'll notice that the top menu also changes

On the top menu, if you select *Create > Polygon primitives,* you'll see a bunch of options for creating basic objects like cubes, spheres and cylinders. Every time that you create a *primitive,* you'll notice that inside the *Channel box/Layer editor* tab on the right side of your monitor, a new *Input* with the name of the primitive will be created ( something like *polyCube1* ). Clicking on this name, you'll be able to modify some attributes of the primitive, like width, height and depth.

![1*EZQ-boJFx4AH4mbK5sKqLA.png](journal-helabs-com--3d-modeling-for-ui-designers-the-he-journal/4ca9e14f05b71037e5b118bbbcc912c5.png)

![1*EZQ-boJFx4AH4mbK5sKqLA.png](journal-helabs-com--3d-modeling-for-ui-designers-the-he-journal/bec2fee2174686ce498305fce727e00c.png)

Now that we have created our first primitive, let's explore the main tools for modelling. On the left side of your monitor, you'll notice 3 buttons with primitives and red arrows. Those buttons allow you to *Translate ( Move ), Rotate* or *Scale* an object in a Maya scene.

![1*86-1HBhT_ptRNDmaGQZgdw.jpeg](journal-helabs-com--3d-modeling-for-ui-designers-the-he-journal/b4aa347a6195a0e1499130417e153f54.jpeg)

![1*86-1HBhT_ptRNDmaGQZgdw.jpeg](journal-helabs-com--3d-modeling-for-ui-designers-the-he-journal/216dd8ec5f75e0f95d74b670b71caeb2.jpeg)

Using the scale tool to change the size of a cube

These tools can also be used for *vertices, edges* and *faces*. If you right click on an object, you'll see some options that allow you to change the selection mode between them.

![1*d_SDPqMjPFh6XmLYGNaBuA.gif](journal-helabs-com--3d-modeling-for-ui-designers-the-he-journal/d5c4fce06c576d87136f5267a446fedc.gif)

Scaling a face, rotating an edge and moving a vertice

By default, you should see a viewport with 4 different cameras. I like to work using a single panel with a perspective view. If you’d like the same, you can change it by selecting *Panels > Layouts > Single Pane.*

![1*tJ6mA1EAdKNcEXleIDoDsw.jpeg](journal-helabs-com--3d-modeling-for-ui-designers-the-he-journal/bf8e20e72afb0cc7ea64634b66ccfe5c.jpeg)

![]()

You should also try holding down alt and middle mouse dragging to move the camera around. If you hold down alt and left drag instead, you’ll rotate the camera. If you want to set the camera to an object, just select the object and press F :)

#### Modeling an old Factory

Now that we understand a bit better how things work, let's create this factory icon to explore modelling techniques.

![1*CI3u5vBSenHIx0C5zkJNNQ.jpeg](journal-helabs-com--3d-modeling-for-ui-designers-the-he-journal/fddf0517e798f6adb7befb2a8448a24e.jpeg)

![]()

The final result should look like this :)

We can start by creating a cube. Select an edge and hold down *command* ( or *ctrl* if you're using Windows ) and right click on the cube. You'll see another menu show up. While still holding down the right mouse button, move the mouse to *Edge ring utilities* and then to *Edge ring and split.* Inside *INPUTS,* you can change the *split type* from *relative* to *multi* and select how many *divisions* you want. We'll use these divisions to create the roof.

![1*qjV_N_XZmwGa3Xfeg-sGbw.gif](journal-helabs-com--3d-modeling-for-ui-designers-the-he-journal/ddbf08698543025216ba2944b9388cc6.gif)

Hovering to select can be tricky at first but it makes the flow faster once you get it :)

Now you can select the faces on top of the cube, and extrude them ( *edit mesh > face > extrude* ) This will allow you to pull those faces out, creating the roof. You should also turn off the option *"Keep Faces Together"* on the side panel and increase the *Offset* on the black and yellow menu close to the control arrows. After that, if you delete one edge from each "roof" you'll get a triangle shape.

![1*8LwJj6GnjofIxqj6HxWNrg.gif](journal-helabs-com--3d-modeling-for-ui-designers-the-he-journal/7566d7f6f2852ad2650c0fa1a4ba6238.gif)

To create the door, for example, you can start with a cube, then extrude and offset the front face to create the door trim. You can detach the front face from the door trim by going to *Mesh > Separate > Extract.* Keeping it separated will allow you to model the door without affecting the trim. To create the metal bars of a rolling door, use the *edge ring and split*, and then *extrude* the faces. Once you have one door ready, you can duplicate it by pressing *Ctrl + D.*
