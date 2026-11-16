---
url: "https://dev.to/juliang/how-swr-works-4lkb"
captured_at: "2026-11-16T00:31:05+00:00"
title: "How SWR works behind the scenes"
domain: "dev-to"
---

I first learned about [SWR](https://swr.now.sh/) thanks to a video tutorial by Leigh Halliday: "[React Data Fetching with Hooks using SWR](https://youtu.be/oWVW8IqpQ-A)". If you're not familiar with SWR, you can watch Leigh's video, [read the official docs](https://swr.now.sh/) or [find more on dev.to](https://dev.to/t/swr).

In this post we're going to build our own version of SWR, if only to understand how it works. But first a disclaimer:

⚠️ Warning!

**This is is not production code.** It's a simplified implementation and it doesn't include all the great features of [SWR](https://swr.now.sh/).

In previous blog posts I had written a `useAsyncFunction` hook to fetch data in React function components. That hook works not only with `fetch`, but with any function returning a promise.

Here's the hook:  

```
type State<T> = { data?: T; error?: string }

export function useAsyncFunction<T>(asyncFunction: () => Promise<T>): State<T> {
  const [state, setState] = React.useState<State<T>>({})

  React.useEffect(() => {
    asyncFunction()
      .then(data => setState({ data, error: undefined }))
      .catch(error => setState({ data: undefined, error: error.toString() }))
  }, [asyncFunction])

  return state
}
```

Enter fullscreen mode Exit fullscreen mode

If we pretend the `fetchAllGames` is a function returning a promise, here's how we use the hook:  

```
function MyComponent() {
  const { data, error } = useAsyncFunction(fetchAllGames)
  // ...
}
```

Enter fullscreen mode Exit fullscreen mode

SWR has a similar API, so let's start from this hook, and make changes as needed.

### [](#changing-data-store)Changing data store

Instead of storing the data in `React.useState` we can store it in a static variable in the module scope, then we can remove the `data` property from our state:  

```
const cache: Map<string, unknown> = new Map()

type State<T> = { error?: string }
```

Enter fullscreen mode Exit fullscreen mode

Our cache is a `Map` because otherwise different consumers of the hook would overwrite the cache with their unrelated data.

This means we need to add a `key` parameter to the hook:  

```
export function useAsyncFunction<T>(key: string, asyncFunction: () => Promise<T>) {
  ...
}
```

Enter fullscreen mode Exit fullscreen mode

Next, we change what happens when the promise resolves:  

```
asyncFunction()
  .then(data => {
    cache.set(key, data) // <<<<<<<<<<<<< setting cache here!
    setState({ error: undefined })
  })
  .catch(error => {
    setState({ error: error.toString() })
  })
```

Enter fullscreen mode Exit fullscreen mode

Now our "state" is just the error, so we can simplify it. The custom hook now looks like this:  

```
const cache: Map<string, unknown> = new Map()

export function useAsyncFunction<T>(
  key: string,
  asyncFunction: () => Promise<T>
) {
  const [error, setError] = React.useState<string | undefined>(undefined)

  React.useEffect(() => {
    asyncFunction()
      .then(data => {
        cache.set(key, data)
        setError(undefined)
      })
      .catch(error => setError(error.toString()))
  }, [key, asyncFunction])

  const data = cache.get(key) as T | undefined
  return { data, error }
}
```

Enter fullscreen mode Exit fullscreen mode

### [](#mutating-local-data)Mutating local data

This works but it doesn't provide a mechanism to mutate the local data, or to reload it.

We can create a "mutate" method that will update the data in the cache, and we can expose it by adding it to the return object. We want to memoise it so that the function reference doesn't change on every render. ([React docs on useCallback](https://reactjs.org/docs/hooks-reference.html#usecallback)):  

```
  ...
  const mutate = React.useCallback(
    (data: T) => void cache.set(key, data),
    [key]
  );
  return { data, error, mutate };
}
```

Enter fullscreen mode Exit fullscreen mode

Next, in order to provide a "reload" function we extract the existing "load" implementation which is currently inside our `useEffect`'s anonymous function:  

```
React.useEffect(() => {
  asyncFunction()
    .then(data => {
      cache.set(key, data)
      setError(undefined)
    })
    .catch(error => setError(error.toString()))
}, [key, asyncFunction])
```

Enter fullscreen mode Exit fullscreen mode

Again, we need to wrap the function in `useCallback`. ([React docs on useCallback](https://reactjs.org/docs/hooks-reference.html#usecallback)):  

```
const load = React.useCallback(() => {
  asyncFunction()
    .then(data => {
      mutate(data); // <<<<<<< we call `mutate` instead of `cache.set`
      setError(undefined);
    })
    .catch(error => setError(error.toString()));
}, [asyncFunction, mutate]);

React.useEffect(load, [load]); // executes when the components mounts, and when props change

...

return { data, error, mutate, reload: load };
```

Enter fullscreen mode Exit fullscreen mode

### [](#almost-there)Almost there

The entire module now looks like this: (⚠️ but it doesn't work)  

```
const cache: Map<string, unknown> = new Map()

export function useAsyncFunction<T>(
  key: string,
  asyncFunction: () => Promise<T>
) {
  const [error, setError] = React.useState<string | undefined>(undefined)

  const mutate = React.useCallback(
    (data: T) => void cache.set(key, data),
    [key]
  );

  const load = React.useCallback(() => {
    asyncFunction()
      .then(data => {
        mutate(data) 
        setError(undefined)
      })
      .catch(error => setError(error.toString()))
  }, [asyncFunction, mutate])

  React.useEffect(load, [load])

  const data = cache.get(key) as T | undefined
  return { data, error, mutate, reload: load }
}
```

Enter fullscreen mode Exit fullscreen mode

⚠️ This doesn't work because the first time this executes, `data` is undefined. After that, the promise resolves and the `cache` is updated, but since we're not using `useState`, React doesn't re-render the component.

### [](#shamelessly-forceupdating)Shamelessly force-updating

Here's a quick hook to force-update our component.  

```
function useForceUpdate() {
  const [, setState] = React.useState<number[]>([])
  return React.useCallback(() => setState([]), [setState])
}
```

Enter fullscreen mode Exit fullscreen mode

We use it like this:  

```
...
const forceUpdate = useForceUpdate();

const mutate = React.useCallback(
  (data: T) => {
    cache.set(key, data);
    forceUpdate(); // <<<<<<< calling forceUpdate after setting the cache!
  },
  [key, forceUpdate]
);
...
```

Enter fullscreen mode Exit fullscreen mode

✅ **And now it works!** When the promise resolves and the cache is set, the component is force-updated and finally `data` points to the value in cache.  

```
const data = cache.get(key) as T | undefined
return { data, error, mutate, reload: load }
```

Enter fullscreen mode Exit fullscreen mode

### [](#notifying-other-components)Notifying other components

**This works, but is not good enough.**

When more than one React component use this hook, only the one that loads first, or the one that mutates local data gets re-rendered. **The other components are not notified of any changes.**

One of the benefits of SWR is that we don't need to setup a React Context to share the loaded data. **How can we achieve this functionality?**

### [](#subscribing-to-cache-updates)Subscribing to cache updates

We move the `cache` object to a separate file because it will grow in complexity.  

```
const cache: Map<string, unknown> = new Map();
const subscribers: Map<string, Function[]> = new Map();

export function getCache(key: string): unknown {
  return cache.get(key);
}
export function setCache(key: string, value: unknown) {
  cache.set(key, value);
  getSubscribers(key).forEach(cb => cb());
}

export function subscribe(key: string, callback: Function) {
  getSubscribers(key).push(callback);
}

export function unsubscribe(key: string, callback: Function) {
  const subs = getSubscribers(key);
  const index = subs.indexOf(callback);
  if (index >= 0) {
    subs.splice(index, 1);
  }
}

function getSubscribers(key: string) {
  if (!subscribers.has(key)) subscribers.set(key, []);
  return subscribers.get(key)!;
}

```

Enter fullscreen mode Exit fullscreen mode

Note that we're not exporting the `cache` object directly anymore. In its place we have the `getCache` and `setCache` functions. But more importantly, we also export the `subscribe` and `unsubscribe` functions. These are for our components to subscribe to changes even if those were not initiated by them.

Let's update our custom hook to use these functions. First:  

```
-cache.set(key, data);
+setCache(key, data);
...
-const data = cache.get(key) as T | undefined;
+const data = getCache(key) as T | undefined;
```

Enter fullscreen mode Exit fullscreen mode

Then, in order to subscribe to changes we need a new `useEffect`:  

```
React.useEffect(() =>{
  subscribe(key, forceUpdate);
  return () => unsubscribe(key, forceUpdate)
}, [key, forceUpdate])
```

Enter fullscreen mode Exit fullscreen mode

Here we're subscribing to the cache for our specific key when the component mounts, and we `unsubscribe` when it unmounts (or if props change) in the returned cleanup function. ([React docs on useEffect](https://reactjs.org/docs/hooks-reference.html#useeffect))

We can clean up our `mutate` function a bit. We don't need to call `forceUpdate` from it, because it's now being called as a result of `setCache` and the subscription:  

```
  const mutate = React.useCallback(
    (data: T) => {
      setCache(key, data);
-     forceUpdate();
    },
-   [key, forceUpdate]
+   [key]
  );
```

Enter fullscreen mode Exit fullscreen mode

### [](#final-version)Final version

Our custom hook now looks like this:  

```
import { getCache, setCache, subscribe, unsubscribe } from './cache';

export function useAsyncFunction<T>(key: string, asyncFunction: () => Promise<T>) {
  const [error, setError] = React.useState<string | undefined>(undefined);
  const forceUpdate = useForceUpdate();

  const mutate = React.useCallback((data: T) => setCache(key, data), [key]);

  const load = React.useCallback(() => {
    asyncFunction()
      .then(data => {
        mutate(data);
        setError(undefined);
      })
      .catch(error => setError(error.toString()));
  }, [asyncFunction, mutate]);

  React.useEffect(load, [load]);

  React.useEffect(() =>{
    subscribe(key, forceUpdate);
    return () => unsubscribe(key, forceUpdate)
  }, [key, forceUpdate])

  const data = getCache(key) as T | undefined;
  return { data, error, mutate, reload: load };
}

function useForceUpdate() {
  const [, setState] = React.useState<number[]>([]);
  return React.useCallback(() => setState([]), [setState]);
}
```

Enter fullscreen mode Exit fullscreen mode

This implementation is not meant to be used in production. It's a basic approximation to what SWR does, but it's lacking many of the great features of the library.

✅ Included

❌ Not included

Return cached value while fetching

Dedupe identical requests

Provide a (revalidate) reload function

Focus revalidation

Local mutation

Refetch on interval

Scroll Position Recovery and Pagination

Dependent Fetching

Suspense

## [](#conclusion)Conclusion

I think [SWR](https://swr.now.sh/) (or [react-query](https://github.com/tannerlinsley/react-query#readme)) is a much better solution than storing fetched data in a React component using `useState` or `useReducer`.

I continue to store my application state using custom hooks that use `useReducer` and `useState` but for remote data, I prefer to store it in a cache.

* * *

Photo by [Umberto](https://unsplash.com/@umby?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText) on [Unsplash](https://unsplash.com/s/photos/circuit-board?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText)
