---
url: "https://www.telerik.com/blogs/incremental-hydration-angular?ref=dailydev"
captured_at: "2026-09-25T23:06:46+01:00"
title: "Hydration and Incremental Hydration in Angular"
domain: "telerik-com"
---

Hydration can be considered “activating” a server-side rendered HTML page on the client. Incremental hydration enables this in stages, on demand.

Hydration is an important concept in modern web development, especially in the context of server-side rendered (SSR) applications and improving performance. With Angular 19, the framework introduced incremental hydration, a more advanced approach to hydration that enables finer control over when and how parts of an application become interactive.

In this article, we’ll explore the foundations of hydration and delve into Angular’s latest innovations, particularly incremental hydration.

## Hydration

Within server-side rendered (SSR) apps, [hydration](https://angular.dev/guide/hydration#what-is-hydration) can be considered the process of “activating” a server-side rendered HTML page on the client. This means attaching event listeners, restoring application state and reusing server-rendered DOM nodes rather than recreating them. By doing so, hydration avoids redundant rendering, improving performance metrics like [First Input Delay (FID)](https://web.dev/articles/fid), [Largest Contentful Paint (LCP)](https://web.dev/articles/lcp) and [Cumulative Layout Shift (CLS)](https://web.dev/articles/cls).

Think of it like receiving a fully assembled piece of furniture. Server-side rendering delivers the assembled product, and hydration is unwrapping and tightening a few bolts to make it ready for use. Without hydration, it’s like discarding the pre-assembled furniture and rebuilding it from scratch—wasteful and inefficient.

While hydration improves performance, traditional approaches have some limitations like the following:

*   **Global activation:** Full-application hydration requires downloading all JavaScript associated with the page at once, which can result in slower initial load times for large applications.
*   **The “uncanny valley” phenomenon:** Before hydration completes, server-rendered elements may appear interactive but lack users’ expected functionality. For instance, clicking a button before its JavaScript is loaded results in no response, creating a frustrating user experience. See a great explanation of this in [Alyssa’s recent post on Angular 19](https://www.telerik.com/blogs/joy-filled-release-holiday-season-angular-19#uncanny-valley).
*   **Layout shifts:** Placeholder content used to defer loading can lead to visual instability as real content replaces it.

Angular has been iteratively addressing these issues, starting with full-application hydration in Angular 16, [deferrable views](https://angular.dev/guide/templates/defer) in Angular 17 and [EventReplay](https://angular.dev/api/platform-browser/withEventReplay) in Angular 18. Each of these features laid the groundwork for Angular 19’s **incremental hydration**.

## Incremental Hydration

[Incremental hydration](https://angular.dev/guide/incremental-hydration) builds upon full-application hydration by enabling developers to hydrate parts of an application on demand rather than all at once. This is achieved through the familiar `@defer` syntax, where hydration is triggered only when necessary. For example, a component can hydrate:

*   [On viewport entry](https://angular.dev/guide/incremental-hydration#hydrate-on-viewport): When the component scrolls into view
*   [On user interaction](https://angular.dev/guide/incremental-hydration#hydrate-on-interaction): When a user clicks or hovers over the component
*   [On idle](https://angular.dev/guide/incremental-hydration#hydrate-on-idle): When the browser is idle
*   [On a timer](https://angular.dev/guide/incremental-hydration#hydrate-on-timer): After a specified delay
*   Etc.

To enable incremental hydration, we should check that our application already uses SSR and hydration. Then, we can update our bootstrap configuration with the [withIncrementalHydration()](https://angular.dev/api/platform-browser/withIncrementalHydration#) function:

```
import {
  bootstrapApplication,
  provideClientHydration,
  withIncrementalHydration,
} from "@angular/platform-browser";

bootstrapApplication(AppComponent, {
  providers: [provideClientHydration(withIncrementalHydration())],
});
```

TypeScript

After enabling, we can use the [@defer](https://angular.dev/guide/templates/defer) directive with hydration triggers in our templates:

```
@defer (hydrate on viewport) {
  <shopping-cart/>
}
```

TypeScript

The above is an example of hydrating a component when it enters the viewport. This means the `<shopping-cart>` component will only become interactive when it scrolls into view, conserving resources until needed.

Similarly, we can hydrate a component upon user interaction, providing a placeholder until the component is ready:

```
@defer (hydrate on interaction) {
  <product-details />
} @placeholder {
  <div>Loading...</div>
}
```

TypeScript

For cases where certain components or sections of the page do not require interactivity, Angular provides the option to completely skip hydration on initial render. This is particularly useful for static content, such as footers or purely decorative elements, that don’t benefit from JavaScript activation. We can achieve this with the [hydrate never](https://angular.dev/guide/incremental-hydration#hydrate-never) directive:

```
@defer (hydrate never) {
  <static-footer />
}
```

TypeScript

The above example keeps the `<static-footer>` component from ever hydrating, keeping it static content and avoiding unnecessary JavaScript overhead. You can explore [more examples of the different hydration triggers in the official Angular documentation](https://angular.dev/guide/incremental-hydration#controlling-hydration-of-content-with-triggers).

In Angular 19, incremental hydration combines several key features:

*   **Server rendering with dehydrated content:** The server renders the main template for deferred blocks, but the client skips downloading JavaScript until a hydration trigger is fired. This way, no placeholders are required, reducing layout shifts.
*   **Event replay:** Introduced in Angular 18, this feature captures user interactions during the “uncanny valley” period and replays them once the component is hydrated.
*   **Selective activation:** Developers can control which parts of the page become interactive and when, reducing unnecessary JavaScript downloads and improving performance.

By combining these features, Angular 19 provides a robust solution for optimizing performance and user experience in SSR applications.

## Wrap-up

Overall, incremental hydration in Angular 19 represents a great advancement in optimizing web application performance. By deferring non-critical JavaScript and hydrating components only when necessary, developers can reduce bundle sizes and improve load times. This approach enhances user experience by preventing layout shifts so that components behave predictably. With the added flexibility of fine-tuned hydration triggers and the ability to exclude static content from hydration with `hydrate never`, Angular developers now have more tools to build efficient, responsive applications.

For more details, be sure to check out the following resources below:

*   [Incremental Hydration | Angular Documentation](https://angular.dev/guide/incremental-hydration)
*   [A Joy-Filled Release for the Holiday Season—Angular 19 | Alyssa Nicoll](https://www.telerik.com/blogs/joy-filled-release-holiday-season-angular-19)
