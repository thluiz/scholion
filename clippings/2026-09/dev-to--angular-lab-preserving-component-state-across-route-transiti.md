---
url: "https://dev.to/this-is-angular/angular-lab-preserving-component-state-across-route-transitions-3f7j?ref=dailydev"
captured_at: "2026-09-25T01:14:19+01:00"
title: "Angular LAB: Preserving Component State Across Route Transitions"
domain: "dev-to"
---

**Let’s dive into a fun new exercise!**

Imagine you have an application with two routes:

*   One displays a list of users.
*   The other shows details for a specific user.

You can navigate between these routes by clicking links, and you can also switch between user details using "Previous" and "Next" buttons.

Here’s an example of what it might look like:

![Demo 1](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fq7nq8kof4r7niadp1pu7.gif)

#### [](#the-first-challenge)The First Challenge

When navigating back to a route you've already visited, the application fetches the data from the server again.

While this can be addressed in several ways—such as implementing a cache or using a global store to maintain state across route transitions—there’s another, more nuanced issue.

#### [](#the-second-challenge-losing-dom-state)The Second Challenge: Losing DOM State

When navigating away from a route, you lose all DOM state. This is particularly problematic with forms. When you return to the form, any entered data, validation states, and UI modifications are lost:

![Demo 2](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fnt1821iugxrgq3i9ykor.gif)

Although proper state management could solve this, it’s not straightforward. You’d need to:

*   Save the component state.
*   Reapply all DOM modifications to restore the previous look and behavior.

This involves patching form values, states, errors, and more. And it’s not limited to forms—other UI elements like accordions also require similar treatment.

Fortunately, Angular provides a powerful tool to address this: the `RouteReuseStrategy` class.

## [](#routereusestrategy-what-does-it-do)RouteReuseStrategy: what does it do?

You’ll find plenty of in-depth articles on `RouteReuseStrategy`, but here’s the gist: it allows you to control when Angular should dispose of or retain a component during navigation.

In our scenario, we want Angular to “set aside” (hide) components instead of destroying them when leaving a route, and to retrieve them as-is when navigating back.

By default, Angular uses an internal strategy, but we can override it with a custom implementation.

#### [](#creating-a-custom-reuse-strategy)Creating a Custom Reuse Strategy

Here’s how we can define a custom `RouteReuseStrategy`:  

```
@Injectable({
  providedIn: 'root',
})
export class CustomReuseStrategy implements RouteReuseStrategy {}

// main.ts
bootstrapApplication(AppComponent, {
  providers: [
    // ...
    {
      provide: RouteReuseStrategy,
      useExisting: CustomReuseStrategy,
    },
  ],
});
```

Enter fullscreen mode Exit fullscreen mode

**Note**: Marking it as `Injectable` isn’t strictly required since Angular handles it internally, but this approach offers flexibility—more on that in a moment.

#### [](#defining-route-reuse-behavior)Defining Route Reuse Behavior

Let’s establish a convention for managing routes:

*   Use `storeRoute: true` for routes that should not be destroyed.
*   Use `noReuse: true` for routes that must not reuse components, even if the paths are identical.

The `noReuse` flag is critical for routes with parameters (e.g., `/users/1` vs. `/users/2`). Without it, these routes would share the same component instance, leading to unintended state sharing.

Here’s how your routes might look:  

```
const routes: Routes = [
  {
    path: 'users',
    component: UsersComponent,
    data: {
      storeRoute: true,
    },
  },
  {
    path: 'users/:id',
    component: UserComponent,
    data: {
      noReuse: true,
      storeRoute: true,
    },
  },
  {
    path: '**',
    redirectTo: '/users',
  },
];
```

Enter fullscreen mode Exit fullscreen mode

#### [](#a-couple-of-helpers)A couple of helpers

For our implementation we'll need a couple of helpers:

*   A function which constructs the full path of a route, in order to identify it
*   A function which compares two objects, for comparing parameters and query parameters

Here an example for both:  

```
function compareObjects(a: any, b: any): boolean {
  return Object.keys(a).every(prop => 
    b.hasOwnProperty(prop) &&
    (typeof a[prop] === typeof b[prop]) &&
    (
      (typeof a[prop] === "object" && compareObjects(a[prop], b[prop])) ||
      (typeof a[prop] === "function" && a[prop].toString() === b[prop].toString()) ||
      a[prop] == b[prop]
    )
  );
}

// Returns the full path of a route, as a string
 export function getFullPath(route: ActivatedRouteSnapshot): string {
  return route.pathFromRoot
    .map(v => v.url.map(segment => segment.toString()).join("/"))
    .join("/")
    .trim()
    .replace(/\/$/, ""); // Remove trailing slash
}
```

Enter fullscreen mode Exit fullscreen mode

## [](#implementing-raw-routereusestrategy-endraw-)Implementing `RouteReuseStrategy`

Let's implement the class. First, we must create an object to cache our components:  

```
import {
  ActivatedRouteSnapshot,
  DetachedRouteHandle,
  RouteReuseStrategy
} from "@angular/router";

interface StoredRoute {
  route: ActivatedRouteSnapshot;
  handle: DetachedRouteHandle;
}

@Injectable({
  providedIn: 'root'
})
export class CustomReuseStrategy implements RouteReuseStrategy {
  storedRoutes: Record<string, StoredRoute | null> = {};
}
```

Enter fullscreen mode Exit fullscreen mode

I won't go into details about `DetachedRouteHandle`, but that's what will bring our component back when the route is visited again.

Now we must implement the required methods of `RouteReuseStrategy`.

* * *

A `shouldDetach` method decides whether to detach a route or not: we'll decide based on the `storeRoute` property in our route configuration.  

```
  // Should we store the route? Defaults to false.
  shouldDetach(route: ActivatedRouteSnapshot): boolean {
    return !!route.data['storeRoute'];
  }
```

Enter fullscreen mode Exit fullscreen mode

A `store` method allows us to store our route when navigating away from it. We'll store it by full path with our helper from before:  

```
  // Store the route
  store(
    route: ActivatedRouteSnapshot,
    handle: DetachedRouteHandle
  ): void {
    // Ex. users/1, users/2, users/3, ...
    const key = getFullPath(route);
    this.storedRoutes[key] = { route, handle };
  }
```

Enter fullscreen mode Exit fullscreen mode

A `shouldAttach` method decides whether to grab the route from our cache or not. Here, we compare all route parameters, including `queryParams`.  

```
  // Should we retrieve a route from the store?
  shouldAttach(route: ActivatedRouteSnapshot): boolean {
    const key = getFullPath(route);
    const isStored = !!route.routeConfig && !!this.storedRoutes[key];

    if (isStored) {
      // Compare params and queryParams.
      // Params, however, have already been compared because the key includes them.
      const paramsMatch = compareObjects(
        route.params,
        this.storedRoutes[key]!.route.params
      );
      const queryParamsMatch = compareObjects(
        route.queryParams,
        this.storedRoutes[key]!.route.queryParams
      );

      return paramsMatch && queryParamsMatch;
    }
    return false;
  }
```

Enter fullscreen mode Exit fullscreen mode

A `retrieve` method is used to grab the route from our cache:  

```
  // Retrieve from the store (it only needs the handle)
  retrieve(route: ActivatedRouteSnapshot) {
    const key = getFullPath(route);
    if (!route.routeConfig || !this.storedRoutes[key]) return null;
    return this.storedRoutes[key].handle;
  }
```

Enter fullscreen mode Exit fullscreen mode

Finally, `shouldReuseRoute` decides whether a route with the same path as the previous one should be reused. Again, we'll refer to our convention, and `true` will be the default:  

```
  // Should the route be reused?
  shouldReuseRoute(
    previous: ActivatedRouteSnapshot,
    next: ActivatedRouteSnapshot
  ): boolean {
    const isSameConfig = previous.routeConfig === next.routeConfig;
    const shouldReuse = !next.data['noReuse'];
    return isSameConfig && shouldReuse;
  }
```

Enter fullscreen mode Exit fullscreen mode

## [](#convenience-methods-for-purging-the-cache)Convenience methods for purging the cache

It's important to understand that when a route is cached, the associated component is never destroyed. This also means that `ngOnInit` will not be triggered again when the user navigates back to the route. While this can be beneficial for preserving state, it also introduces the risk of memory leaks if not handled properly.

To mitigate this, I recommend implementing convenience methods to manually purge the cache: one for clearing a single route and another for clearing all routes.  

```
  // Destroys the components of all stored routes
  clearAllRoutes() {
    for (const key in this.storedRoutes) {
      if (this.storedRoutes[key]!.handle) {
        this.destroyComponent(this.storedRoutes[key]!.handle);
      }
    }
    this.storedRoutes = {};
  }

  // Destroys the component of a particular route.
  clearRoute(fullPath: string) {
    if (this.storedRoutes[fullPath]?.handle) {
      this.destroyComponent(this.storedRoutes[fullPath].handle);
      this.storedRoutes[fullPath] = null;
    }
  }

  // A bit of a hack: manually destroy a particular component.
  private destroyComponent(handle: DetachedRouteHandle): void {
    const componentRef: ComponentRef<any> = (handle as any).componentRef;
    if (componentRef) {
      componentRef.destroy();
    }
  }
```

Enter fullscreen mode Exit fullscreen mode

## [](#conclusion)Conclusion

Here's the end result:

![Demo 3](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fkqidndhtpp6h21oiqpkv.gif)

When navigating back to a cached route, the component retains all of its state seamlessly. Additionally, you can manually clear the cache whenever needed.

This solution is highly "plug-and-play" and can be easily integrated into your projects. However, use it wisely—improper use can make your app prone to memory leaks.

[Link to the full demo here.](https://stackblitz.com/edit/stackblitz-starters-93gnhp4k?file=src%2Fapp.component.ts)

* * *

[![AccademiaDev](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F6d1fjwldghrnfybftgpl.png)](https://accademia.dev/)

### [](#accademiadev-textbased-web-development-courses)[AccademiaDev](https://accademia.dev/): text-based web development courses!

I believe in providing concise, valuable content without the unnecessary length and filler found in traditional books. Drawing from my years as a consultant and trainer, these resources—designed as interactive, online courses—deliver practical insights through text, code snippets, and quizzes, providing an efficient and engaging learning experience.

[![Available courses](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fnquwklnhyhhvvx9oucnr.png)](https://accademia.dev/)
