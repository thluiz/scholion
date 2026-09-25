---
url: "https://tigerabrodi.blog/performance-principles?ref=dailydev"
captured_at: "2026-09-25T21:37:41+01:00"
title: "Performance Principles"
domain: "tigerabrodi-blog"
---

## Introduction

When I think about performance, it's not rocket science.

Lately, I've been thinking a lot about what performance means and questions you can ask to identify performance improvements.

Some of the stuff applies to all fields in programming.

## Can we do less work?

```
// Doing more work than needed
function getTotalSpending(transactions: Transaction[]): number {
  // Processing ALL transactions even though we only need those from 2024
  return transactions
    .filter((t) => t.year === 2024)
    .reduce((sum, t) => sum + t.amount, 0);
}

// Doing less work
function getTotalSpending(transactions: Transaction[]): number {
  // Early termination - stop once we hit 2023 since transactions are sorted by date
  let total = 0;
  for (const t of transactions) {
    if (t.year < 2024) break; // Stop processing - we know we won't need older transactions
    total += t.amount;
  }
  return total;
}
```

This may not be the best example, but if we know we only need to process transactions up to 2024, we can stop processing once we hit 2023.

If we were to use `.filter` in JS, we'd be looping through the entire transactions array.

This is more efficient assuming the transactions are sorted by date.

## What's the shorter route?

```
// Longer route
function findUser(users: User[][], targetId: string): User | null {
  // Checking every single user in every subarray
  for (const userGroup of users) {
    for (const user of userGroup) {
      if (user.id === targetId) return user;
    }
  }
  return null;
}

// Shorter route
const userMap = new Map<string, User>();
// Build map once, lookup many times in O(1)
function findUser(targetId: string): User | null {
  return userMap.get(targetId) || null;
}
```

When you need to do nested loops (this also means using array methods like `.map`, `.filter`, `.includes`, etc.), try to build a map or a Set containing ids of the items you need to lookup. This would be O(n) for building the map and O(1) for lookups, as opposed to O(n^2) for nested loops.

This is a simple example, but it's really good to think about the work you're doing and if you can do it in a different way.

**Performance improvements is either about size of assets usually or "what's the shorter route for doing the work".**

## Avoiding repeated work (caching)

Caching is a famous example that applies to all fields in programming. Whether CPU or frontend stuff.

```
// Without caching - expensive computation done repeatedly
function computeUserStats(userId: string): UserStats {
  // Expensive DB queries and calculations done every time
  return calculateExpensiveStats(userId);
}

// With caching
const statsCache = new Map<string, UserStats>();
function computeUserStats(userId: string): UserStats {
  if (statsCache.has(userId)) {
    return statsCache.get(userId)!;
  }

  const stats = calculateExpensiveStats(userId);
  statsCache.set(userId, stats);
  return stats;
}
```

Here after calculating the stats, we store them in a map. When doing so again, we look in the cache first to see if we've already calculated them.

## Can we do any work ahead of time (perceived performance)?

A typical user flow in all sites is to hover over a link, click on it, and go to a page. On the new page, we'd be loading the resources and data needed for the page.

Why not load the resources and data needed for the page ahead of time?

If we know the user is near to clicking the link, let's prefetch the resources and data needed for the page and store it in the cache.

When the navigation happens, it's instant.

If you're using React Query, you can use `prefetchQuery` to prefetch the data needed for the page.

To prefetch the page's resources and data, you can use `prefetch` in the `Link` component (which uses `<link rel="prefetch">` under the hood).

Preloading images is another interesting example. Think of a carousel, when the user hovers over the first image, we can preload all the other images:

```
// Preload on first swipe/hover
const preloadImages = (urls: string[]) => {
  urls.forEach((url) => {
    const img = new Image();
    img.src = url;
  });
};
```

## Mobile considerations

I talked a lot about "hovering". It's important to note that on mobile, this is not a thing.

So when do we prefetch or preload on mobile?

There are different approaches to this.

### Prefetching

Let's focus on prefetching first.

Let's say you've got a list of items. Clicking on an item would navigate to a detail page.

You don't really know which one the user is going to click on, but what you can do upfront is to prefetch the data for each item. Other concerns to keep in mind is when you clear it from the cache, but let's not think about that for now.

The question is, when do you prefetch?

If know we'll prefetch them in order. We still need to ask, when do we prefetch?

**We don't wanna interfere with the browser. If it's doing important work, we don't wanna block or make it slower.**

So how do we do it?

We could use `requestIdleCallback` to prefetch the data. `requestIdleCallback` is a function that allows us to run a function at a time when the browser is idle. This way, we don't interfere with the browser.

It's important to note that safari doesn't support `requestIdleCallback`. So we can fallback to `setTimeout`. I would say a timeout of 1 second should be enough. This way, we don't immediately begin prefetching.

### Preloading

Going back to the carousel example, we can't hover. However, we do know when the user swipes the first image. **When they swipe to see the second image. If that happens, we can preload all the remaining images for the carousel.**

To be smart about this, we can even preload all the second images (think airbnb, list of properties you're scrolling through). So when you swipe and let's say there is 6 more images, we just preload all of them for the specific carousel.
