---
url: "https://tylerbarker.com/posts/liveview-is-not-a-zero-js-framework-it-s-a-zero-boring-js-framework?utm_medium=email&utm_source=elixir-radar"
captured_at: "2026-09-25T21:42:35+01:00"
title: "LiveView Is Not a Zero-JS Framework, It’s a Zero-Boring-JS Framework - Tyler Barker"
domain: "tylerbarker-com"
---

![An image with filename: hookAutocomplete.gif](https://tylerbarker.com/rails/active_storage/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6NjM5NywicHVyIjoiYmxvYl9pZCJ9fQ==--bc4dddb29be2aeb7c26b098a9b700d865642f664/hookAutocomplete.gif)

A recent [Twitter discussion](https://x.com/ryanflorence/status/1797285294267593008) about the “ceiling” of server-side rendered frameworks like [Phoenix LiveView](https://github.com/phoenixframework/phoenix_live_view) has caused quite a stir. Most of it was in good faith, and many devs have responded with some great takes on the matter. One from Jose Valim particularly resonated with me:

> There is an implied conclusion that server-side frameworks are limited if they have to write some JS, but the same logic does not apply when client-side devs have to write auth, lambdas, or server logic.
> 
> — [@josevalim](https://x.com/josevalim/status/1798662441674719541)

You can get really far without JS using LiveView. So much so, the subtitle of [an excellent book](https://pragprog.com/titles/liveview/programming-phoenix-liveview/) on it is “Interactive Elixir Web Programming Without Writing Any JavaScript”.

Nonetheless, LiveView is not a **zero-JS** framework. It’s a **zero-boring-JS** framework.

The JS you’d otherwise need for routing, auth, and the like in another framework, you can write in Elixir instead. Any client code you end up needing tends to be just the fun stuff: Data visualisation, Web Audio, the Gamepad API, WebGL — just take a look through [MDN’s list of Web APIs](https://developer.mozilla.org/en-US/docs/Web/API).

I love JavaScript TypeScript, but if I can replace ~90% of it with Elixir and still deliver a rich, client-interactive application I’ll take that deal every time.

## The Power of Client Hooks

> You can write a lot of JS _in Elixir_, thanks to the [LiveView.JS](https://hexdocs.pm/phoenix_live_view/Phoenix.LiveView.JS.html) module, but I’m not going to cover that here. I want to talk about the [Client Hooks API](https://hexdocs.pm/phoenix_live_view/js-interop.html#client-hooks-via-phx-hook).

When I decided to build what is essentially a multi-track recording studio for the web — I chose LiveView.

A web app requiring complex orchestration of media recording and Web Audio is an obvious candidate for React or another JS UI framework. But writing client hooks to work with LiveView is _really nice_. In my time building [Prototape](https://prototape.fm/), I’ve landed on some patterns I’ll go over that demonstrate how far they can take you.

## A Quick Primer

A client hook is just a JavaScript object which implements one or more of the following methods:

*   `mounted()`
    
*   `beforeUpdate()`
    
*   `updated()`
    
*   `destroyed()`
    
*   `disconnected()`
    
*   `reconnected()`
    

These are executed by LiveView alongside the corresponding lifecycle event. Because it’s just an object, it can also hold any methods relevant to your use case, and any state. All of which is then available within the lifecycle methods you write for LiveView to execute.

Hooks become available to utilise in HEEX templates when they’re given to the LiveSocket instantiated in `app.js`. Let’s see an example courtesy of the [LiveView documentation](https://hexdocs.pm/phoenix_live_view/js-interop.html#client-hooks-via-phx-hook):

```
// app.js
let liveSocket = new LiveSocket("/live", Socket, {
  params: { _csrf_token: csrfToken },
  hooks: { InfiniteScrollHook } // <-----
});
```

```
<!-- HEEX -->
<div id="infinite-scroll" phx-hook="InfiniteScroll" data-page={@page}>
```

```
// JS
const InfiniteScrollHook = {
  page() { return this.el.dataset.page },
  mounted(){
    this.pending = this.page()
    window.addEventListener("scroll", e => {
      if(this.pending == this.page() && scrollAt() > 90){
        this.pending = this.page() + 1
        this.pushEvent("load-more", {})
      }
    })
  },
  updated(){ this.pending = this.page() }
}
```

Here, they add a helper method — `this.page()` — to more easily access the state instantiated in a HTML data attribute. When the page mounts, an event listener is registered to send a `"load-more"` event to the instantiating LiveView when the `page()` and `scrollAt()` check passes the condition.

This event is handled server-side by Elixir, inside a `handle_event/3` function. You can even push an event to a Live Component directly, by specifying its CSS selector when pushing the event with `pushEventTo`.

The hook’s state — `this.pending` — is stored on the hook object with the assignment to `this.pending`, and updated whenever the element is updated in the DOM by the server.

> _Quick thing:_ There’s basically a [whole book](https://pepa.holla.cz/wp-content/uploads/2016/08/You-Don-t-Know-JS-this-Object-Prototypes.pdf) about JavaScript’s `this` keyword, so I usually capture it at the top of larger lifecycle methods: 
> 
> `const hook = this;`

So, the “ceiling” of client hook is the same as any JS object. The parent object is the top-level scope available to the methods you implement. **But,** there is a way to take it further.

## Another Approach — Closured Hooks

At a certain level of problem complexity, trying to operate entirely within the object starts to feel unwieldy. But if we return a hook object from a function, we raise the top level scope to be that of the function’s closure, and all we can express there becomes available to the hook. Take an abridged example:

```
type Maybe<T> = T | null

function hookAudioDevices(): StatefulViewHook {
  const [viewHook, setViewHook] = hookState<Maybe<ViewHook>>(null);
    
  // now we can access viewHook() from any functions we define
  // in the closure, so it can be leveraged by any code you
  // write which requires communication with the server

  return {
    mounted() {
      const hook = setViewHook(this) as ViewHook;
    }
  }
}
```

And in your `app.js`:

```
let liveSocket = new LiveSocket("/live", Socket, {
  params: { _csrf_token: csrfToken },
  hooks: { AudioDevicesHook: hookAudioDevices() } // <-----
});
```

Closured hooks do have one very interesting drawback, but I’ll get to that later. You might be curious about `hookState`, and `StatefulViewHook`.

In my projects I use `hookState` as a state helper. It takes obvious influence from React with some minor differences — e.g. the current value is actually a function which returns the current value. A bit like `createSignal` in [Solid](https://docs.solidjs.com/reference/basic-reactivity/create-signal).

Here’s the function:

```
type HookState<T> = [() => T, (value: T) => T];

function hookState<T>(defaultValue: T): HookState<T> {
  let value = defaultValue;

  const getValue = () => value;
  const setValue = (newValue: T) => {
    value = newValue;
    return value;
  };

  return [getValue, setValue];
}
```

On the `StatefulViewHook` type: The `ViewHook` type from the community maintained LiveView `@types` doesn’t play nice with this approach. This is because it’s concerned with more than consumer-implemented hooks need to be.

I’ve been maintaining my own copy of the community-maintained Phoenix + LiveView `@types` to better suit this approach. I’ll commit my changes upstream eventually, but this should take you far enough:

```
import type { ViewHook } from "phoenix_live_view"; 

interface ViewHookCallbacks {
  mounted?: (this: ViewHook) => void;
  beforeUpdate?: (this: ViewHook) => void;
  updated?: (this: ViewHook) => void;
  beforeDestroy?: (this: ViewHook) => void;
  destroyed?: (this: ViewHook) => void;
  disconnected?: (this: ViewHook) => void;
  reconnected?: (this: ViewHook) => void;
}

type RequireAtLeastOne<T> = {
  [K in keyof T]-?: Required<Pick<T, K>> & Partial<Pick<T, Exclude<keyof T, K>>>;
}[keyof T];

export type StatefulViewHook = RequireAtLeastOne<ViewHookCallbacks>;
```

With that out of the way, let’s do something real with this!

## Pushing Audio Devices to LiveView

In Prototape, we can’t record any audio until we know the recording devices available to a user. This information is only available to us from the browser, so if we want to render these options for selection we’ll need a hook. I’ll outline the implementation piece by piece and then we’ll put it all together.

First, we’ll need to maintain some state:

```
export function hookAudioDevices(): StatefulViewHook {
  const [viewHook, setViewHook] = hookState<Maybe<ViewHook>>(null);
  const [knownDeviceIds, setKnownDeviceIds] = hookState<string[]>([]);

  return {
    // ...
  };
```

As I mentioned before, we want the hook object available to our closure, so we keep it in `viewHook()`.

We can register an `ondevicechange` callback to listen for changes to available devices, so we should maintain an array of the audio devices we’re already aware of to avoid pushing updates to LiveView needlessly.

Now we can add a function to push audio device data to LiveView when necessary:

```
export function hookAudioDevices(): StatefulViewHook {
  const [viewHook, setViewHook] = hookState<Maybe<ViewHook>>(null);
  const [knownDeviceIds, setKnownDeviceIds] = hookState<string[]>([]);

  // push microphones and speakers to LiveView
  async function maybePushAudioDevices() {
    try {
      if (!navigator.mediaDevices || !navigator.mediaDevices.enumerateDevices) {
        const error = new Error("enumerateDevices() not supported.");
        throw error;
      }

      // get available media devices, filter for audio only
      const mediaDeviceInfos: MediaDeviceInfo[] = await navigator.mediaDevices.enumerateDevices();
      const audioDevices = mediaDeviceInfos.filter((d) => d.kind !== "videoinput");
      const deviceIds = audioDevices.map((device) => device.deviceId);

      // if audio device IDs has changed, update and push latest
      if (!arrayEquals(deviceIds, knownDeviceIds())) {
        setKnownDeviceIds(deviceIds);
        viewHook() && viewHook()!.pushEvent("update_devices", audioDevices);
      }
    } catch (error) {
      // let your app monitoring provider know here
      viewHook() && viewHook()!.pushEvent("update_devices", []);
    }
  }

  return { /** ... */ };
}
```

The `viewHook() && viewHook()!` thing here is just an unfortunate TypeScript assertion I could probably improve — not important. The point is now we have a mechanism through which we can push the latest available audio device data for LiveView to receive in a `handle_event/3` and keep in `assigns` for rendering.

Now to put it all together with the necessary lifecycle methods. I’ll just include the `return` of the above function here:

```
return {
  mounted() {
    setViewHook(this);

    maybePushAudioDevices();
    navigator.mediaDevices.ondevicechange = () => maybePushAudioDevices();
  },
  reconnected() {
    setViewHook(this);
    maybePushAudioDevices();
  },
  destroyed() {
    setViewHook(null);
    setKnownDeviceIds([]);
  },
};
```

When the LiveView mounts, we set the hook in our closure state so it’s available to `maybePushAudioDevices()`. We also register `maybePushAudioDevices()` as the callback function to be called when the `ondevicechange` event fires — so if a device is unplugged or vice versa, LiveView can reflect that.

Then we eat our vegetables. If we lost connection, we repeat the same steps on `reconnected()`, and when the component that initialised the hook via `phx-hook` is removed from the page we reset the state with our `destroyed()` method.

I’ll omit the server-side code for brevity — it’s a `handle_event/3` like any other you might trigger, which also sends an update to the hook handling recording and playback — but here’s the end result:

![An image with caption: Note the live-update when I put my AirPods in](https://tylerbarker.com/rails/active_storage/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6NjQ3MSwicHVyIjoiYmxvYl9pZCJ9fQ==--f9e679eca6cbc1e8477025eca7b83fd19d9e92da/audioDevicesHookDemo.gif)

## We’ve Officially Scratched the Surface

I think this is a pretty cool example from a real application, but it’s only highlighting one-way communication to LiveView from the hook using `pushEvent`. Putting aside how much you can do with all I’ve outlined already, the possibilities stretch even further when you also receive messages from your LiveView.

For one thing, you can get replies from the server after a `pushEvent` when you give it a callback and implement your `handle_event/3` accordingly. For example:

```
// client
hook.pushEvent("hook:hello_server!", {}, (reply, _ref) => {
  console.log(reply.msg));
}
```

```
# server
def handle_event("hook:hello_server", _params, socket) do
  {:reply, %{msg: "hello client!"}, socket}
end
```

Sweet. But we can also register callbacks to fire when we receive messages from the LiveView using `hook.handleEvent`. For example: When a user selects the audio device they want to use for input in the UI, we’ll need to set it on the audio recorder:

```
# use push_event/3 in the return of some socket callback server-side
{:noreply, push_event(socket, "app:set_input_id", %{id: some_id})}
```

```
import { z } from "zod"; 

// Zod can give us runtime type-checks on the data we expect
const setInputDeviceIdSchema = z.object({ id: z.string() });

// inside a mounted() method
hook.handleEvent("app:set_input_id", (payload) => {
  const { id } = setInputDeviceIdSchema.parse(payload);
  if (id !== audioRecorder.inputDeviceId) {
    audioRecorder.setInputDeviceId(id);
  }
});
```

It’s worth noting that both of these approaches require a round trip to the server. That’s not a bad thing, but in many situations we’ll want to execute some arbitrary JS immediately on click for a snappier UX. We can do that too.

Let’s say we want a button to play/pause audio playback. We definitely don’t want to wait on the server to trigger that. This is where [LiveView.JS](https://hexdocs.pm/phoenix_live_view/Phoenix.LiveView.JS.html) comes in handy. The `dispatch` function will dispatch an event client-side without talking to the server at all:

```
<!-- some heex template -->
<button phx-click={JS.dispatch("app:toggle_playback")}>Play</button>
```

```
export function hookAudioThing(): StatefulViewHook {
  // insert relevant state here

  // kept in a function to make removing the
  // event listener on destroyed() simpler
  const togglePlayback = () => { /** do web audio stuff */ }

  return {
    mounted() {
      window.addEventListener("app:toggle_playback", togglePlayback);
    },
    destroyed() {
      window.removeEventListener("app:toggle_playback", togglePlayback);
    },
  };
}
```

## On that “Interesting Drawback”

The closured hook approach has one drawback, or advantage — depending on how you look at it.

Closured hooks are best suited to single-use hooks. By this I mean, many hooks you implement might be used more than once on a page; like to juice up some text inputs in a form in one way or another.

If you use a closured hook more than once on a page, each `phx-hook` will get it’s own hook object, **but state in the function closure is shared across all of them.**

Let me illustrate what I mean:

```
function hookSharingIsCaring(): StatefulViewHook {
  const [elemIds, setElemIds] = hookState<string[]>([]);
  const printSetElemIds = (ids: string[]) => {
    setElemIds(ids);
    console.log("elemIds!", elemIds());
  };
  const addElemId = (id: string) => printSetElemIds([...elemIds(), id]);

  return {
    mounted() {
      const hook = this;
      console.log(`mounting #${hook.el.id}...`);
      addElemId(hook.el.id);
    },
  };
}
```

Let’s skip the part where I add the hook to the LiveSocket and use this hook more than once on the page:

```
<div id="share-one" phx-hook="SharingIsCaringHook"></div>
<div id="share-two" phx-hook="SharingIsCaringHook"></div>
<div id="share-three" phx-hook="SharingIsCaringHook"></div>
```

Now when we load the page we can see the state is shared:

![An image with filename: Screenshot 2024-06-17 at 13.49.53.png](https://cdn.u.pika.page/F2uoGmkJeiIihY35rola2Miw-9rqrblG3vM9daKb56U/s:1800:1400/fn:Screenshot%202024-06-17%20at%2013.49.53/plain/s3://pika-production/dcqqxrd4xwxabulrg1og9vkduuy9)

For me, this isn’t a problem because when a hook needs this kind of approach I’m only using it in one place.

Regardless, that’s really interesting! Sharing state across multiple instances of a hook could unlock some really powerful stuff. I’ve not found that use case in my own work _yet_ but hey, let me know!

## Delegating to a JavaScript UI Framework

Even with all of the above, there are still cases where you might want to leverage a JS UI framework where some client-side state has a lot of influence on your rendered markup. Many amazing folks in the community have implemented ways to integrate [React](https://github.com/fidr/phoenix_live_react), [Svelte](https://github.com/woutdp/live_svelte), and [Vue](https://github.com/Valian/live_vue) components into LiveView really nicely.

Personally, I just can’t be bothered learning Svelte or Vue — as awesome as they both look. I’d also prefer to avoid bringing in React given the performance profile and slow move to server-side rendering by default.

For circumstances like these, I’ve been experimenting with [Solid](https://www.solidjs.com/) to render JSX from a hook and it looks really promising, as well as being lightweight to integrate.

I’ll leave that exploration for another post if people find this one interesting.

## A Closing Note On Types

As I’m sure you’ve figured out I’m pretty fond of TypeScript. It makes all this a whole lot nicer with API autocomplete suggestions and whatnot.

If you’re into this particular niche, I’m trying my hand at porting the JavaScript that powers Phoenix & LiveView to TypeScript as a bit of fun. Beyond shipping types by default, I think a TypeScript implementation would be easier for the community to extend and maintain. I’ve no expectation it’ll ever be part of Phoenix proper, but it’s a nice dream — [feel free to contribute](https://github.com/tylerbarker/phoenix_ts)! ✌️

Thanks for reading!
