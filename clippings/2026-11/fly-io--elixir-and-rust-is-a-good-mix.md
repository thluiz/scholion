---
url: "https://fly.io/phoenix-files/elixir-and-rust-is-a-good-mix"
captured_at: "2026-11-18T11:04:09+00:00"
title: "Elixir and Rust is a good mix"
domain: "fly-io"
---

Author

![Jason Stiebs](https://fly.io/static/images/jason.webp)

Name

Jason Stiebs

@peregrine

[@peregrine](https://twitter.com/peregrine)

![An purple droplet representing Elixir and a red crab, Ferris, representing Rust.](https://fly.io/phoenix-files/elixir-and-rust-is-a-good-mix/assets/elixir-rust-cover.webp)

Image by [Annie Ruygt](https://annieruygtillustration.com/)

This post is about using Rust with Elixir and how easily it can be done! If you want to deploy your Phoenix LiveView app right now, then check out how to [get started](https://docs.fly.io/elixir). You could be up and running in minutes.

## [](#problem)Problem

We need to perform a CPU intensive or system level programming task and there are just no good solutions in [hex.pm](https://hex.pm/), in this example let’s pretend there [are no good ways to do image](https://fly.io/phoenix-files/resizing-images-using-elixir/) processing with Elixir.

As is often the case, there IS a high quality [Rust](https://www.rust-lang.org/) library called [image](https://github.com/image-rs/image) that claims to be just the solution! But shoot, our entire application is written in Elixir already, and we really don’t know how to use [Rust](https://www.rust-lang.org/) that well.

How can Elixir turn to Rust code for high-performance operations?

## [](#solution)Solution

Enter [rustler](https://github.com/rusterlium/rustler), this library is designed to make using Rust and its package ecosystem trivial. Let’s dive in!

Following the getting started guide, first add [rustler](https://hex.pm/packages/rustler) to our `mix.exs` file:

```
{:rustler, "~> 0.38.0"}
```

Once we run `mix deps.get` use the built-in mix task to generate our empty rust project:

```
mix rustler.new
```

```
This is the name of the Elixir module the NIF module will be registered to.
Module name > MyApp.RustImage
This is the name used for the generated Rust crate. The default is most likely fine.
Library name (myapp_rustimage) > rust_image
* creating native/rust_image/.cargo/config.toml
* creating native/rust_image/README.md
* creating native/rust_image/Cargo.toml
* creating native/rust_image/src/lib.rs
* creating native/rust_image/.gitignore
Ready to go! See /Users/me/projects/my_app/native/rust_image/README.md for further instructions.
```

You should go open up that `README.md`, but I’ll save you the hassle, we need to make an Elixir module in `lib/my_app/rust_image.ex` that has the following contents:

```
defmodule MyApp.RustImage do
  use Rustler, otp_app: :my_app, crate: "rust_image"

  # When your NIF is loaded, it will override this function.
  def add(_a, _b), do: :erlang.nif_error(:nif_not_loaded)
end
```

And from then on out we’re ready to do some Rust. The default generator gives us an `add/2` function implemented in `native/rust_image/src/lib.rs` let’s take a look

```
#[rustler::nif]
fn add(a: i64, b: i64) -> i64 {
    a + b
}

rustler::init!("Elixir.MyApp.RustImage");
```

#### [](#what-is-a-nif)What is a NIF?

Native Implemented Functions are the BEAM’s method of allowing processes to directly call native functions. They normally have a _ton_ of boilerplate and you need to be serious about cleaning up your memory, handling errors and being safe. Luckily that’s Rust’s entire thing! For example here is the [Erlang NIF tutorial](https://www.erlang.org/doc/tutorial/nif.html). We didn’t need to do any of that!

Our hyper optimized code will add two integers of size i64 and return the result. Note the Rustler specific parts here:

*   `#[rustler::nif]` is a macro that tells Rustler to expose this function as a NIF.
*   `rustler::init!("Elixir.MyApp.RustImage");` This initializes the Erlang NIF runtime so that the beam can put every `#[rustler::nif]` function (like `add/2`) on the `Elixir.MyApp.RustImage` module and replace the stubs we left.

This is _amazing_. To see if this works, lets fire up `iex -S mix`

```
iex(1)> MyApp.RustImage.add(100, 20)
120
```

If everything worked the first time, you should have seen cargo building the app in release mode and succeeding before opening the iex term. If you didn’t already have Rust installed it would have shown an error, you can install Rust the [usual way](https://rustup.rs/).

Rustler is even smart and will recompile automatically, leave iex open and change our `lib.rs`

```
#[rustler::nif]
fn add(a: i64, b: i64) -> i64 {
    a + b + 1
}
```

Save and then open that running iex session again:

```
iex(2)> r(MyApp.RustImage)
... truncated output of cargo doing it's thing an maybe some beam warnings
{:reloaded, [MyApp.RustImage]}
iex(3)> MyApp.RustImage.add(1,1)
3
```

Incredible! We get the same workflow and nice bits of working with Elixir, with minimal fussing about with Rust.

### [](#images)Images

First add our image dependency to our `Cargo.toml` file:

```
[dependencies]
rustler = "0.38.0"
image = "0.25.10"
```

Then alter our `lib.rs` to create a function that accepts an `input` path, an `output` path and `quality` and changes any image to a JPEG with our set quality.

```
use image::ImageReader;
use image::codecs::jpeg::JpegEncoder;
use std::fs::File;

#[rustler::nif]
fn jpg(input: String, output: String, quality: i64) -> Result<String, String> {
    let img = ImageReader::open(&input).unwrap().decode().unwrap();
    let out_file = std::fs::File::create(&output).unwrap();
    let mut jpg = JpegEncoder::new_with_quality(&out_file, quality as u8);

    jpg.encode_image(&img).unwrap();
    Ok(output.to_string())
}

// add code...

rustler::init!("Elixir.MyApp.RustImage");
```

We also want to update our RustImage module to include a stub for `jpg/3`, but that’s left as an exercise to the reader.

Now let’s try it out! `iex -S mix`

```
iex(1)> MyApp.RustImage.jpg("input.png", "output.jpeg", 75)
{:ok, "output.jpeg"}
```

And boom! We’ve converted a PNG to a JPEG with 75% quality.

## [](#being-a-good-beam-citizen)Being a good BEAM citizen

There is one more thing we should consider here, and that’s CPU load. While this function likely runs near instantly on our laptop, when deployed it might take longer on shared CPU/RAM.

And because the BEAM runs our code directly, and it will lock an the runtime until it has completed running. What we mean by directly is that when using a NIF the beam will treat it like any other code, with the major caveat that it can’t prempt the Rust code automatically.

On the BEAM this is a big issue since the entire runtime expects to be able to switch contexts between millions of processes at any time.

Luckily the Rustler and BEAM teams have thought of this and given us a solution. Simply change that macro on top of `jpeg` to this

```
-- #[rustler::nif]
++ #[rustler::nif(schedule = "DirtyCpu")]
```

This tells the Rustler and BEAM to automagically schedule this in a way that won’t block the entire world while it works. Again _amazing_, this is called a [DirtyNif](https://www.erlang.org/doc/man/erl_nif.html) and is way more difficult to work with when you are manually using this via C.

## [](#deployment)Deployment

Deploying this to Fly.io with Docker isn’t as automagic, we need to make some small changes so that our Docker environment can build Rust. First, update the Dockerfile by adding a build step right before our Elixir build step:

```
#... ARG stuff..
FROM rust:1.97.1 as rust
# install build dependencies
RUN apt-get update -y && apt-get install -y build-essential git \
    && apt-get clean && rm -f /var/lib/apt/lists/*_*

workdir /app
COPY native/rust_images ./
RUN cargo rustc --release 

#..Elixir builder.....
# compile assets
RUN mix assets.deploy

#NEW STUFF
COPY --from=rust /app/target/release/librust_images.so priv/native/librust_images.so
#/NEW
# Compile the release
RUN mix compile
```

Then update our `config/prod.exs` adding the following line:

```
config :my_app, MyApp.RustImage,
  crate: :rust_image,
  skip_compilation?: true,
  load_from: {:my_app, "priv/native/librust_image"}
```

What we did here is build the library in its own Docker builder context, so it runs in parallel with the rest of our Docker steps and can be cache’d easily. Then we told Rustler to skip compiling and to load it directly from our where we put it.

And we’re all set, simply `fly deploy` and you’re off!

## [](#discussion)Discussion

We have only really scratched the surface about what is possible using the power of NIFs and Rust together. From [loading massive datasets to do science](https://github.com/elixir-nx/explorer) to connecting via [WebRTC](https://github.com/livinginthepast/specter), the Rust community has built out an impressive suite of packages and tools that are also now available to us. And Rustler makes it possible!

**Note**: This post was updated in August 2026 to bump the Elixir/JS dependencies to their latest versions. We keep these posts fresh so the examples work with current releases—and so LLMs over-indexing on old blog posts stop recommending ancient dependency versions.

## Fly.io ❤️ Elixir

Fly.io is a great way to run your Phoenix LiveView app close to your users. It’s really easy to get started. You can be running in minutes.

[Deploy a Phoenix app today! →](https://docs.fly.io/elixir)

![](https://fly.io/static/images/cta-kitty.webp)

Next post ↑

[Phoenix LiveView Zipped Uploads](https://fly.io/phoenix-files/phoenix-liveview-zipped-uploads/)

Previous post ↓

[Can Phoenix Safely use the Zip Module?](https://fly.io/phoenix-files/can-phoenix-safely-use-the-zip-module/)
