---
url: "https://web.archive.org/web/20190328163157id_/https://blog.usejournal.com/elixir-scenic-snake-game-b8616b1d7ee0"
captured_at: "2026-11-16T08:21:11+00:00"
title: "Getting started with Scenic in Elixir — Crafting a simple snake game"
domain: "web-archive-org"
---

## There’s a new UI framework in town, how hard is it to build a simple game with it? Not much, actually!

[![Go to the profile of Giancarlo França](https://cdn-images-1.medium.com/fit/c/100/100/0*lbntSwSTPytK4PG2.)](https://blog.usejournal.com/@giandr?source=post_header_lockup)

Over the last few years, it’s been proven by the community that one can create pretty much anything in **Elixir** given enough determination. From [lightning-fast APIs](http://www.akitaonrails.com/2015/10/27/how-fast-is-elixir-phoenix) with processing times in the range of microseconds to an [artificial pancreas](https://www.youtube.com/watch?v=ARQD4BN_5ns), these creations show how delightful the language is to tinker with, not to mention that some [big names are already reaping the benefits of running it in production](https://blog.discordapp.com/scaling-elixir-f9b8e1e7c29b).

While I was browsing the [lineup for the last ElixirConf](https://www.youtube.com/playlist?list=PLqj39LCvnOWaxI87jVkxSdtjG8tlhl7U6), one talk in particular really caught my eye: [**Introducing Scenic, A Functional UI Framework**](https://www.youtube.com/watch?v=1QNxLNMq3Uw) by **Boyd Multerer**, founder of Xbox Live and maker of several other cool things.

It is as magical as it sounds — with **Scenic**, your Elixir code can now render stylish native interfaces without being tied to web pages! Images, buttons, sliders, dropdowns, primitive shapes, you name it. Stuffing a standalone window with UI elements certainly feels like a breath of fresh air after working non-stop on console-based applications. Better yet, it’s being primarily targeted at IoT devices with support for remote controlling, which means now is a good time to dust off that Raspberry Pi that’s been sitting inside a drawer (but not for this tutorial, no, any regular computer should do!).

Now, do you know what makes extensive use of graphical interfaces? Games do! If you can make a GUI, you can make a game out of it. Sure you can make console-based games too, but let us appreciate the freedom of a blank OpenGL-powered canvas and have some fun! In this tutorial, we’ll dive right in and implement a fully functional game of **Snake**.

### Setting up

For this, you’ll want a working **Elixir** installation. Older versions might not have the requirements to run Scenic, so I recommend grabbing at least **v1.7**. If you’re unsure on how to get it running, I personally found that [an asdf setup was super easy to follow and maintain](https://elixircasts.io/installing-elixir-with-asdf). Alternatively, [check out the official guides on installation](https://elixir-lang.org/install.html).

We also want to make sure Scenic’s system dependencies are present. Specifically, it requires GLEW and GLFW. For Ubuntu 16, the following two commands usually suffice:

sudo apt-get update  
sudo apt-get install pkgconf libglfw3 libglfw3-dev libglew1.13 libglew-dev

For other systems, [please check the scenic\_new repository for instructions](https://github.com/boydm/scenic_new#install-prerequisites).

Next, we want to actually install the _scenic\_new_ package so that we may bootstrap our brand new project with a single, convenient command. Let’s create a folder for our project and install the package:

mkdir elixir\_snake  
cd elixir\_snake  
mix archive.install hex scenic\_new

Now, we can create our project's structure in the current directory:

mix scenic.new .  
mix deps.get

First things first, we want to make sure we’re now ready to display Scenic apps. Run the following command to build and start our app:

mix scenic.run

Hopefully it worked, but don’t fret if it didn’t! Carefully go through the steps once again to check if you missed something. Once it’s up and running, you should see the following screen:

![](https://cdn-images-1.medium.com/max/1600/1*arYn3CXeUUJ8eNotLaaMmQ.png)

Scenic's default starter application

Great, now it is time to get our hands dirty!

### Our first scene

According to the Scenic docs, **scenes** are to webpages just as a **graph** is to the DOM. This means our main game screen will be a **scene**, described by a **graph**. Let’s see if we can assemble a simple static screen. We’ll start by writing a new source file in _lib/scenes/game.ex_.

The first thing we need is an entry point for our scene. This role is filled by the `init/2` callback, which every scene must implement. The two parameters available are:

1.  An argument that is passed by whoever starts this scene. The starting scene for your application is defined in the configuration (as we’ll see shortly), and you can jump to another scene by setting the target scene as the root with `Scenic.ViewPort.set_root/2` .
2.  Contextual options provided by the viewport (each window in your app corresponds to a viewport). These options include the PID for the viewport process, which we’ll use to extract some info such as the window’s width and height later on.

Since our game will need to constantly update the screen, we’ll build an empty graph at compile-time with the `Graph.build/1` function. Then, at run-time, we’ll pipe our existing graph into some useful helper functions from `Scenic.Primitives` to transform it as we wish. We’ll begin by adding some text: the **player’s score**.

As with any [GenServer](https://hexdocs.pm/elixir/GenServer.html), our scene will maintain a **state** during its lifetime. For our snake game, this means it'll need to hold mostly _everything_ that can change during play: the position of the snake, which way it is facing, the position of the pellet(s)… however, we only need the **score** for now, so we start the game state with an integer score of 0 and make sure we can display it as a text on the scene graph with our `draw_score/2` helper function.

Just run it again with `mix scenic.run` and… nothing changed? That's because our root graph is still being set to `Scene.Home` on application start. Fortunately, that's easy to change: open `config/config.exs` and look for the line:

default\_scene: {ElixirSnake.Scene.Home, nil},

Change the value to `{ElixirSnake.Scene.Game, nil}` and we're set. And what does that`nil` actually mean, you might ask? This is one of the places where you can set the first parameter that is passed to `init/2`. As we aren't using any parameters, this value won't matter. Run the game again and there's our score display:

![](https://cdn-images-1.medium.com/max/1600/1*tA_Oazgz5OUAbl1QLx8JGA.png)

Looking like a game now!

### A reptile steals the scene

We cannot call our game a _snake game_ without a snake, though, so let's fill that gap. We'll introduce some changes to our `init/2` function to prepare our game state to maintain relevant information about every 'game object' (the snake and the pellet) in a way that we can later push them to a single function that will render them to the screen according to their specific rules. This is our updated function:

We use the `ViewPort.info/1` function to find out the size, in pixels, of our current viewport. Since our play field will be a grid, it's useful to know how many tiles we can fit in each dimension for two reasons: we can determine the snake's initial position such that it always starts in the center of the grid, and we can make the snake wrap around the screen later on.

Notice we're storing our game objects inside a key named `objects` in the game state. We store three important pieces of data about the `snake` object:

*   A list of ordered pairs that describe the snake's full`body` . Each pair corresponds to a cell in the grid that the snake is currently occupying.
*   The snake's current `size` in cells. We'll use it soon to determine whether the `body` should grow at any given step.
*   The `direction` in which the snake is currently heading. It is an ordered pair that tells us how many cells the snake head's position is shifting in each direction, per update. For instance, the starting value of `{1, 0}` means that it will jump 1 cell to the right and 0 cells down at a time.

The `draw_game_objects/2` function will apply the transforms from all objects in the state to the scene graph. Its implementation follows:

The main concept here is that each object will have its `draw_object/3` entry describing how it should be rendered, starting with `:snake` . To bring the game's protagonist to life, all we need are a few cells painted lime. For this purpose, we create a nice `draw_tile/4` function to help us fill a cell at coordinate (x,y) whenever we need. Don't forget to update our imports list as we're now using `rrect/3` from `Scenic.Primitives` and, while we're at it, take a moment to insert the new `tile_radius` module attribute that defines how rounded our rectangles will be:

import Scenic.Primitives, only: \[rrect: 3, text: 3\]

@tile\_radius 8

Boot up the game once more, lo and behold:

![](https://cdn-images-1.medium.com/max/1600/1*1MRBD3WCMb6uU3Ijarqwqg.png)

It lives! Sorta?

Well, it certainly _is_ a rounded rectangle. But it still needs to move and grow in order to resemble a virtual snake. However, right now, our game screen is only updated exactly once: when the scene starts. Before we get to gameplay mechanics, we need to set up a mechanism to periodically update whatever has to be updated and re-render the game screen. Fortunately, Erlang's `:timer` provides a method that is simple enough for our purposes, one that fits in our `init/2`:

This will make sure our scene receives a `:frame` message every `@frame_ms` milliseconds, so don't forget to define this module attribute. Some value like `192` is okay for starters. Lower values will speed up the game's pace.

Now that we're receiving a periodic message, we should be capable of handling it:

Even though it doesn't look too exciting yet, this is the essence of our **game loop**! It takes the current state as a parameter, utilizes `move_snake/1` (which we'll implement next) to update it, and runs the same draw pipeline as `init/2` resulting in a new graph push, which is what triggers the rendering process. Now, to get the snake to move:

Our movement logic boils down to this:

1.  Take the snake's current head position;
2.  Create a new head by shifting a copy of the old one in the snake's current direction;
3.  Limit the snake's size to the current known size.

Just like nature itself… right? As you can see, these operations can be expressed without much effort in Elixir's `[head | tail]` notation for lists, as is commonly found in functional programming languages. In fact, what better way to work with a head and a tail than to program a snake?

To help us with the shifting part, `move/3` adds a `{vec_x, vec_y}` tuple (the displacement) to a `{pos_x, pos_y}` tuple (the original position). Wrapping around the screen is done with the modulo operator in the form of `rem/2` .

Now, when you run the game once more, you should see this:

![](https://cdn-images-1.medium.com/max/1600/1*4635TGUJegt-JC-i94cGJw.gif)

A free-range snake! Just look it him go!

Our snake has finally learned how to slither! Such unbounded excitement, it now knows no limits. It also won't listen to orders, so if you want it to follow another direction, tough luck. We can remedy this, however, by handling keyboard events.

### Learning to turn

Scenic conveniently provides the `handle_input/3` callback for us to implement. Its parameters are: the **event**, the event's **context** (a `Scenic.Viewport.Context` struct) and the scene's current **state**. Generally, we'll use the **event** data to modify our **state**.

As an example, when we press the Left Arrow key on our keyboard, we get the following event data:

{:key, {"left", :press, 0}}

Which is pretty self explanatory except for the mysterious zero at the end. If you're curious, that's a [modifier](http://www.glfw.org/docs/latest/group__mods.html), which becomes non-zero when we press the key while holding another key like Shift or CTRL.

Naturally, pattern matching comes to the rescue:

With this, the snake should be fully controllable now! Notice how it's even able to make 180 degree turns on the spot (e.g. when you're going right and press the left arrow). When we implement collision checking later, this would cause an instant game over so, as an exercise, try implementing some checks that prevent this behavior!

![](https://cdn-images-1.medium.com/max/1600/1*OZuHiFKRBjfdHec4pVgnRg.gif)

Ready to explore the axis-aligned world!

### I have no mouth and I must eat

With the snake now able to freely roam all of the universe, we must make sure it is able to feed on tasty pellets. Thus, now it is time to create a new game object, the pellet:

In contrast to the snake that required a map with various information to describe it, the pellet can be described by a simple tuple that tells us in which cell it is located. Drawing it is much simpler as well, down to a single call of our `draw_tile/4` function. The pellet should now be visible:

![](https://cdn-images-1.medium.com/max/1600/1*Tu0cGSRqnqjXD4uTPA0T3g.png)

Finally, food!

But the naive snake just runs over it. We haven't taught it how to eat, so that's the next step. We'll start by amending our `move_snake/1` script to check whether we've just moved onto a cell that contains food:

Might seem like a lot to take in, but let's go over it bit by bit:

*   The `maybe_eat_pellet/2` function checks whether the snake head overlaps with the pellet's current position via pattern matching. If so, it changes the game state to place the pellet in a new position at random.
*   `randomize_pellet/1` is responsible for generating a new coordinate pair for the pellet. It keeps trying recursively until the position is valid according to `validate_pellet_coords/2`(i.e. when the pellet is not in one of the cells that the snake's body occupies).
*   `add_score/2` and `grow_snake/1` allow us to increment the player's score and the snake's size, respectively.

Run the game once more and _voilà_! The snake is now able to feast on the pellets and the score updates accordingly.

![](https://cdn-images-1.medium.com/max/1600/1*8_4_n9fZsQSX0z1OoVVPAg.gif)

A nutritious lunch.

Now all is well except for one thing: our game doesn't ever end. If the snake becomes large enough so that there's no room for the pellet anymore, the game will hang due to `randomize_pellet/1` calling itself recursively forever.

### Watch your head

Lastly, we want to make sure that the player loses the game whenever the snake crashes into its own body. Surprisingly, it's not too tough! We just need another change in our `move_snake/1` :

Here we take a shortcut to check for the snake's collisions with itself: since the snake's `:body` is a list of cells that are occupied by the snake's segments, it **should not contain duplicates** otherwise the snake has two segments that are in the same cell, which constitutes a collision point. To detect duplicates, we use `Enum.uniq/1` to generate a copy of the snake's body with any duplicates removed, and check whether it remains with the same number of elements as the original. In other words, if the snake's body is:

\[ {0, 0}, {0, 1}, {0, 2}, {1, 2}, {1, 1}, {0, 1} \]

We know there's a collision because the list above contains 6 elements and the result of `Enum.uniq/1` would contain only 5 elements (`{0, 1}` would be removed).

Once the collision is detected, we must switch to another scene, the **game over scene**. For this to work, define the following module attribute:

@game\_over\_scene ElixirSnake.Scenes.GameOver

And here comes the module itself! Create a new source file called _lib/scenes/game\_over.ex_:

This scene is much less dynamic than the game scene, so we can get away without using a frame timer. One thing you might notice is that this time we're actually using `init/2` 's first argument! Since the player's score was part of the state in the **Game** scene, we conveniently handed it over to the **Game Over** scene by passing it via `ViewPort.set_root/2` in the `maybe_die/1` function.

Moreover, the `:on_cooldown` flag is used to prevent the player from exiting the game over screen too quickly. It starts as `true` and becomes `false` once the `:end_cooldown` message is received. This is also when the text changes, as you can see below:

![](https://cdn-images-1.medium.com/max/1600/1*zFonpc-9SRk3h0FSE6dMUQ.gif)

The tragic end of a reckless snake.

And now…

### …You've just made a playable game in Elixir!

Hopefully this tutorial has shown you some of the possibilities of Scenic in conjunction with Elixir. It's an interesting challenge to structure a game application in a non-procedural language and even though the Erlang VM is typically best used in server applications, with its stellar fault tolerance and what not, [Scenic's GLFW driver](https://github.com/boydm/scenic_driver_glfw) is a great example of leveraging the language's interoperability with C code to produce a performant native graphical application.

[This game's project is also on GitHub](https://github.com/gVirtu/scenic-snake), drop by to check it out. :)  
If you're planning on making more complex games, consider separating game logic from the scene itself, which provides more flexibility to carry information over between scenes and leads to slimmer modules with well bounded responsibilities. This was a little out of scope here since it involves communication between GenServers and I wanted to keep this walkthrough simple and straightforward.

Congratulations on bringing this snake game to life, and thank you for reading through!

[![](https://cdn-images-1.medium.com/max/2400/1*f2IVAl0TbsfES9cFGYr40g.png)](https://blog.usejournal.com/meet-journal-d222fce8db1d)

**This story is published in Noteworthy, where 10,000+ readers come every day to learn about the people & ideas shaping the products we love.**

**Follow our publication to see more product & design stories featured by the** [**Journal**](https://usejournal.com/?/utm_source=usejournal.com&utm_medium=blog&utm_campaign=guest_post) **team.**
