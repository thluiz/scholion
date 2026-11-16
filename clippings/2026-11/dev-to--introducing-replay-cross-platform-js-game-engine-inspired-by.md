---
url: "https://dev.to/edbentley/introducing-replay-a-cross-platform-js-game-engine-inspired-by-react-pif"
captured_at: "2026-11-16T20:03:03+00:00"
title: "Introducing Replay: a cross-platform JS game engine inspired by React"
domain: "dev-to"
---

[![Cover image for Introducing Replay: a cross-platform JS game engine inspired by React](https://media2.dev.to/dynamic/image/width=1000,height=420,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fuser-images.githubusercontent.com%2F15923595%2F80872097-c3c33a00-8ca7-11ea-8043-8b47e4138042.png)](https://media2.dev.to/dynamic/image/width=1000,height=420,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fuser-images.githubusercontent.com%2F15923595%2F80872097-c3c33a00-8ca7-11ea-8043-8b47e4138042.png)

[![Ed Bentley](https://media2.dev.to/dynamic/image/width=50,height=50,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F145861%2F0185c61d-3753-4034-aa63-7f972b123d69.png)](https://dev.to/edbentley)

Today I'm publishing a new open-source library for creating games: [Replay](https://replay.js.org/).

I've built many indie games over the years (such as [The Impossible Game](https://www.flukedude.com/theimpossiblegame/)). I've also built many web apps using [React](https://reactjs.org/).

[Replay](https://replay.js.org/) takes the ideas and concepts that makes React such a great library for building user interfaces, and brings them to game development. Take a look at how Replay manages state and rendering through a declarative API:  

```
const Player = makeSprite({
  init() {
    // Initial state
    return {
      posX: 0,
      posY: 0,
    };
  },

  loop({ state }) {
    // Return new state at 60 fps
    return {
      posX: state.posX + 1,
      posY: state.posY + 1,
    };
  },

  render({ state }) {
    // Draw a circle based on current state
    return [
      t.circle({
        position: {
          x: state.posX,
          y: state.posY,
        },
        color: "#147aff",
        radius: 10,
      }),
    ];
  },
});
```

Enter fullscreen mode Exit fullscreen mode

Check out [the docs](https://replay.js.org/docs/intro) on how to quickly get setup with a new JavaScript or TypeScript project, and then deploy to the web or iOS.

I hope you enjoy using it to build some new games!

[![Strands harness](https://media2.dev.to/dynamic/image/width=775%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Farticles%2Fhw6m8qng9z1njxbtewf9.png)](https://strandsagents.com/?trk=1c097af3-4db9-4f1f-b0c4-4ea3fa25f1c3&sc_channel=display+ads&bb=264932)

## [](#strands-harness-is-a-stateoftheart-fully-assembled-agent-harness)[Strands harness is a state-of-the-art, fully assembled agent harness.](https://strandsagents.com/?trk=1c097af3-4db9-4f1f-b0c4-4ea3fa25f1c3&sc_channel=display+ads&bb=264932)

Strands harness is a complete, production-ready agent the moment you install it. Shell, file, and web tools, plus context management, memory, sessions, and subagents, are tuned and ready. Run it as a library or from the strands CLI, on any model and any cloud. Every default is yours to change through the open-source Harness SDK.

[Get Started with Strands](https://strandsagents.com/?trk=1c097af3-4db9-4f1f-b0c4-4ea3fa25f1c3&sc_channel=display+ads&bb=264932)
