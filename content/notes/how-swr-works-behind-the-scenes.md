---
title: "How SWR works behind the scenes"
date: '2026-11-16T00:31:05+00:00'
category: webclip
summary: 'The post rebuilds a simplified SWR-like hook in React to show why remote data is stored in a shared cache, how mutation and reload work, and why subscription is needed for updates across components.'
tags: ["swr", "react", "cache", "hooks"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "How SWR works behind the scenes"
    url: "https://dev.to/juliang/how-swr-works-4lkb"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/dev-to--how-swr-works-behind-the-scenes.md"
    kind: repo
---

The article rebuilds a simplified version of SWR from a custom async hook. It first moves fetched data out of component state and into a module-level cache keyed by string, then adds mutate and reload behavior on top of that cache.

It then shows why that still is not enough on its own. Because cache changes do not trigger React renders automatically, the hook needs a force-update mechanism and then a subscribe/unsubscribe layer so multiple components using the same key can react to the same cached value.

## Reading notes

- The post starts from a custom `useAsyncFunction` hook that can fetch any promise-returning function, not just `fetch`.
- Data is moved from `React.useState` to a module-scope `Map`, and the hook receives a `key` so different consumers do not overwrite each other.
- The hook returns only `error` as state, while `data` is read from the cache with the given key.
- A `mutate` function is added to update cached data and exposed in the hook return value.
- A `load` function is extracted from the effect so it can also be returned as `reload`.
- The first cache-based version does not re-render after promise resolution because it no longer uses `useState` for data.
- A `useForceUpdate` hook is introduced to force a component re-render after cache mutation.
- That still leaves other components unsynchronized, because only the component that loads or mutates data re-renders.
- The cache is then split into a separate module with `getCache`, `setCache`, `subscribe`, and `unsubscribe`.
- `setCache` notifies subscribers for a key, and the hook subscribes on mount and unsubscribes on unmount or key change.
- The final version exposes `data`, `error`, `mutate`, and `reload`, but the post says it is still only a basic approximation of SWR and not production code.
- The article lists features included and not included, such as returning cached values while fetching, deduping requests, focus revalidation, interval refetching, pagination, dependent fetching, and Suspense.
- The conclusion says SWR or react-query is preferable for remote data, while custom hooks with `useState` and `useReducer` are kept for application state.
