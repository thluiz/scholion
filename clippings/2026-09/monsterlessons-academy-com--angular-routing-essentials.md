---
url: "https://monsterlessons-academy.com/posts/angular-routing-essentials-all-you-need-to-know-in-one-post"
captured_at: "2026-09-25T17:58:57+01:00"
title: "Angular Routing Essentials: All You Need to Know in One Post"
domain: "monsterlessons-academy-com"
---

This is the only post about Angular Routing that you need in order to fully master it. I will cover all the essential concepts of Angular routing, starting with the basics like defining routes, links, and outlets, and finishing with more advanced topics like data resolvers and route protection.

**Topics that are covered:**

*   [Why do we need routing](#why-do-we-need-routing)
*   [Defining routes](#defining-routes)
*   [Router outlet](#router-outlet)
*   [Router links](#router-links)
*   [Routes order](#routes-order)
*   [Dynamic params](#dynamic-params)
*   [Accessing params](#accessing-params)
*   [Query params](#query-params)
*   [Redirects](#redirects)
*   [Not found route](#not-found-route)
*   [Redirect function](#redirect-function)
*   [Nested routes](#nested-routes)
*   [Active routes](#active-routes)
*   [Exact route match](#exact-route-match)
*   [Programmatic navigation](#programmatic-navigation)
*   [Lazy loading](#lazy-loading)
*   [Route guard](#route-guard)
*   [Route resolver](#route-resolver)

## [Why do we need routing?](https://monsterlessons-academy.com/posts/angular-routing-essentials-all-you-need-to-know-in-one-post#why-do-we-need-routing)

An Angular application is a tree of components that are rendered from top to bottom, starting with the `AppComponent`. There are no exceptions.

![components tree](https://cdn.monsterlessons-academy.com/posts/481-angular-routing/components-tree.png)

But most applications also need to render dynamic content on different pages. When we navigate to `/dashboard`, we should see the dashboard of our application, and by accessing `/posts`, it should render a list of posts.

> It is not possible to achieve this with just a tree of components.

Instead, we use a `router` to specify which component should be rendered on which page. You can think of it as a child component of `AppComponent` that switches based on the URL being accessed.

![components tree](https://cdn.monsterlessons-academy.com/posts/481-angular-routing/router-outlet.png)

It allows us to define which components we want to render for each route. Let's look at how to do that.

## [Defining routes](https://monsterlessons-academy.com/posts/angular-routing-essentials-all-you-need-to-know-in-one-post#defining-routes)

To achieve that, we must register our components as routes. If you generated a new Angular application and selected that you need routing, your `app.routes.ts` file will look like this.

```
// src/app/app.routes.ts
import { Routes } from '@angular/router';

export const routes: Routes = []
```

The `routes` is an array where we define our routes. But the question is, where do we use this configuration? There’s no magic; it must be used somewhere.

```
// src/app/app.config.ts
import { routes } from './app.routes';
...
export const appConfig: ApplicationConfig = {
  providers: [
    provideZoneChangeDetection({ eventCoalescing: true }),
    provideRouter(routes),
    provideAnimationsAsync(),
  ],
};
```

Here we have our app configuration, where we import and use our routes. We pass them to `provideRouter` to register a router in our application.

To define a route, we must add an object to our array of routes.

```
import { DashboardComponent } from './dashboard/dashboard.component';

export const routes: Routes = [
  {
    path: 'dashboard',
    component: DashboardComponent,
  }
]
```

This object contains a `path` field, which can be any string (in our case, "dashboard"). It must be a unique string and not a URL, and it should not start with a slash. We also pass a `component` field to our object. `DashboardComponent` is the component that we want to render for this path.

```
// app/dashboard/dashboard.component.ts
@Component({
  selector: 'app-dashboard',
  standalone: true,
  imports: [],
  templateUrl: './dashboard.component.html',
  styleUrl: './dashboard.component.css',
})
export class DashboardComponent {}
```

This is just a standalone component.

Now, inside the browser, we can type `/dashboard` and we won't get an error. Yes, we only see an empty layout for now, but that's fine.

![empty-layout](https://cdn.monsterlessons-academy.com/posts/481-angular-routing/empty-layout-min.png)

If we try to type a URL that doesn't exist, we will get an error.

![cannot match any error](https://cdn.monsterlessons-academy.com/posts/481-angular-routing/cannot-match-route-error-min.png)

This confirms that our `/dashboard` URL was successfully registered in the Angular application.

## [Router outlet](https://monsterlessons-academy.com/posts/angular-routing-essentials-all-you-need-to-know-in-one-post#router-outlet)

But we don't see any content — just the word "layout." Where is this coming from? It's the markup in `AppComponent`.

```
<div class="container">
  <div class="headline">Layout</div>

  <div class="links"></div>

  <div class="main">
  </div>
</div>
```

In the Angular world, `AppComponent` is essentially the layout. This is the only component being rendered on the screen right now. However, we don’t see the content of our `DashboardComponent`. For every route, the content should be different, and for `/dashboard`, it should be the `DashboardComponent`.

To do that, we must use a feature called an `outlet`.

![router-outlet-error](https://cdn.monsterlessons-academy.com/posts/481-angular-routing/router-outlet-error-min.png)

Inside the `AppComponent`, we rendered a `router-outlet` component, which comes from Angular Router. However, we get an error stating that `router-outlet` is not a known element. This is correct because we haven't imported it as a dependency in our `AppComponent`.

```
import { RouterOutlet } from '@angular/router';
...
@Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterOutlet],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css',
})
...
```

Now, this component is properly registered in our `AppComponent`.

![Dashboard component](https://cdn.monsterlessons-academy.com/posts/481-angular-routing/dashboard-component-min.png)

When we reload the page, the `DashboardComponent` is properly rendered inside our layout.

> We use the router-outlet tag to render dynamic content when we change routes.

Let's do exactly the same for several other components.

```
// src/app/app.routes.ts
import { ProductsComponent } from './products/products.component';
import { SettingsComponent } from './settings/settings.component';

export const routes: Routes = [
  ...
  {
    path: 'products',
    component: ProductsComponent
  },
  {
    path: 'settings',
    component: SettingsComponent,
  }
];
```

![settings page](https://cdn.monsterlessons-academy.com/posts/481-angular-routing/settings-page-min.png)

Now we can navigate to `/settings`, and the `SettingsComponent` is rendered there.

## [Router links](https://monsterlessons-academy.com/posts/angular-routing-essentials-all-you-need-to-know-in-one-post#router-links)

But what about links to all these pages? Here’s how we do that.

```
 <div class="links">
  <a routerLink="/dashboard">dashboard</a>
  <a routerLink="/products">products</a>
  <a routerLink="/settings">settings</a>
</div>
```

Instead of using `<a href>` like we do in regular HTML, we use `routerLink` instead of `href` because `<a>` here is a special component of Angular Router. However, this code won't work by itself.

```
import { ..., RouterLink } from '@angular/router';
...
@Component({
  ...
  imports: [..., RouterLink]
})
```

We must inject the `RouterLink` into our `AppComponent`. Only then will our links work properly.

![links](https://cdn.monsterlessons-academy.com/posts/481-angular-routing/links-min.png)

Now all these links are working, and we can navigate between pages without reloading, with the content changing accordingly.

## [Routes order](https://monsterlessons-academy.com/posts/angular-routing-essentials-all-you-need-to-know-in-one-post#routes-order)

Here is an extremely important point for you: If you don't remember it, you will encounter bugs later.

> The order of routes is extremely important.

```
export const routes: Routes = [
  {
    path: 'dashboard',
    component: DashboardComponent
  },
  {
    path: 'dashboard',
    component: ProductsComponent
  }
];
```

Angular checks routes one by one, starting from the first one. If the path is `/dashboard`, it picks the first route that matches. It doesn't matter if you have other routes that could also fit `/dashboard`. While it's true that with simple strings you usually don't encounter collisions, routes can be defined in various ways and can match different patterns. Therefore, URL collisions are not uncommon.

## [Dynamic params](https://monsterlessons-academy.com/posts/angular-routing-essentials-all-you-need-to-know-in-one-post#dynamic-params)

We learned how to render routes, but what about dynamic parameters? What are dynamic parameters? They are values that can vary within your URL.

```
/pages/1
```

In this URL, the part after the slash is a dynamic parameter that can change. We typically use dynamic parameters for URLs where we don’t have a static string. Examples of dynamic URLs include a page ID like `/pages/5` or a slug like `/products/a-dish-washer`.

```
export const routes: Routes = [
  ...
  {
    path: 'pages/:pageId',
    component: PageComponent
  }
];
```

To define a dynamic parameter, we use a similar construction with `path` and `component`. The only difference is that we include a `:pageId`, which is our dynamic parameter. It can be any string you want, but it must start with a colon.

![dynamic parameter](https://cdn.monsterlessons-academy.com/posts/481-angular-routing/dynamic-parameter-min.png)

## [Accessing params](https://monsterlessons-academy.com/posts/angular-routing-essentials-all-you-need-to-know-in-one-post#accessing-params)

But now you probably want to know how we can access these parameters inside our components. It doesn't make sense to render the same content for different parameters. Typically, we want to render one article with ID `1` and another article with ID `2`.

There are different ways to access parameters inside components but I want to show you the newest and the best because it is extremely simple and declarative. And we will use signals for that.

There are different ways to access parameters inside components, but I want to show you the newest and best method because it is extremely simple and declarative. We will use signals for that.

```
// src/app/page/page.component.ts
import { Component, input } from '@angular/core';

@Component({
  selector: 'app-pages',
  standalone: true,
  imports: [],
  templateUrl: './page.component.html',
  styleUrl: './page.component.css',
})
export class PageComponent {
  pageId = input.required<string>();
}
```

Inside our `PageComponent`, I defined a `pageId` input. Just to remind you, this is the dynamic parameter specified with a colon in our routes array. So, our input **MUST** have the same name as the dynamic parameter to be properly bound. If you don’t know what this construction `input.required` is, it’s an Angular signal, and `pageId` in this case is an `InputSignal`. But most importantly, this `pageId` value will come automatically via Angular Router without any additional code from our side.

```
<!-- src/app/page/page.component.ts -->
<h2>Page - {{pageId()}}</h2>
```

We can switch to the HTML and render our signal.

![Signal input error](https://cdn.monsterlessons-academy.com/posts/481-angular-routing/signal-input-error-min.png)

But in the browser, we see that our component was not rendered, and we get an error: `Input is required but no value is available yet`. This means that we didn't provide an input to the component. While the input is indeed provided automatically by the router, it is not done by default.

```
// src/app/app.config.ts
import { provideRouter, withComponentInputBinding } from '@angular/router';
export const appConfig: ApplicationConfig = {
  providers: [
    ...
    provideRouter(routes, withComponentInputBinding()),
  ],
};
```

We need to enable this feature by adding `withComponentInputBinding` to the configuration. This additional feature forces Angular Router to provide all the fields inside our component.

![Page id parameter](https://cdn.monsterlessons-academy.com/posts/481-angular-routing/page-id-parameter-min.png)

Now it is working; we get `Page - 2`, and we implemented it with just a single line of code. Previously, we needed to write much more code in Angular, but as you can see, it has been significantly improved with signals.

## [Query params](https://monsterlessons-academy.com/posts/angular-routing-essentials-all-you-need-to-know-in-one-post#query-params)

In exactly the same way that we read parameters from the URL, we can also read query parameters.

```
// src/app/page/page.component.ts
export class PageComponent {
  ...
  limit = input.required<string>();
}
```

Here, we added a `limit` as a parameter to our `PageComponent`, but we didn’t specify that `limit` is a query parameter. In fact, we didn’t specify that `pageId` is a parameter either. Angular Router will simply take whatever it has inside the data.

```
<!-- src/app/page/page.component.ts -->
<h2>Page - {{pageId() - {{limit()}}}}</h2>
```

Let’s render it in our HTML now.

![Query params](https://cdn.monsterlessons-academy.com/posts/481-angular-routing/query-params-min.png)

After we provided a `limit` as a query parameter, it was successfully rendered on our page. This means Angular Router reads the query parameter and provides it as an input to our component. In this way, you can read various router data through Angular signals.

## [Redirects](https://monsterlessons-academy.com/posts/angular-routing-essentials-all-you-need-to-know-in-one-post#redirects)

Another important feature of Angular Router is the ability to implement redirect logic.

```
// src/app/app.routes.ts
export const routes: Routes = [
  {
    path: '',
    redirectTo: 'dashboard',
    pathMatch: 'full',
  },
  ...
]
```

Here, we created a new route, but we didn’t provide a `path` and a `component`. Instead, we used an empty string as the `path`, which represents our home route, a `redirectTo` property that defines where we want to redirect the user, and a `pathMatch`, which ensures that the path must be fully matched. This allows us to specify how to redirect one URL to another. In this case, we want to redirect from the home URL directly to the dashboard URL.

![Dashboard component](https://cdn.monsterlessons-academy.com/posts/481-angular-routing/dashboard-component-min.png)

Now, when we navigate to the home page, we are directly redirected to `/dashboard`.

## [Not found route](https://monsterlessons-academy.com/posts/angular-routing-essentials-all-you-need-to-know-in-one-post#not-found-route)

We should also remember to handle "not found" pages correctly. Right now, when we access a page that we haven't registered, we get an error: `Cannot match any routes`.

![cannot match any error](https://cdn.monsterlessons-academy.com/posts/481-angular-routing/cannot-match-route-error-min.png)

To fix this problem, we need to register a route that will match any undefined route.

```
// src/app/app.routes.ts
import { NotFoundComponent } from './not-found/not-found.component';
export const routes: Routes = [
  ...
  {
    path: '**',
    component: NotFoundComponent,
  },
]
```

In this case, our path must be `**`, which means this component is rendered for all undefined routes. This is why it’s extremely important that this route is placed last. If you put it at the beginning, it will be used for every route, even those we have registered. This is a perfect example of why route order is important.

![not found](https://cdn.monsterlessons-academy.com/posts/481-angular-routing/not-found-min.png)

Now, when we navigate to a non-existent route like `/foo`, our `NotFoundComponent` is rendered.

## [Redirect function](https://monsterlessons-academy.com/posts/angular-routing-essentials-all-you-need-to-know-in-one-post#redirect-function)

Sometimes you may encounter a complex use case for redirection in your application where a simple redirect isn't enough. In such cases, you can create a redirect as a function with custom logic inside.

Let’s imagine that previously we had URLs like `/old-pages/1` in our application with a dynamic parameter. Now we've moved our routes to `/pages/1`, and we want to redirect from old pages to new pages, because there may still be old URLs across the internet that need to work.

```
// src/app/app.routes.ts
export const routes: Routes = [
  ...
  {
    path: 'old-pages/:pageId',
    redirectTo: (route) => {
      return `/pages/${route.params['pageId']}`;
    },
  },
]
```

For this, we can define `redirectTo` not as a string but as a function. The function receives `route` as an argument, so we can access dynamic parameters or the URL if needed. In this case, we read `pageId` from the route parameters and return a new URL to which the user will be redirected.

![dynamic parameter](https://cdn.monsterlessons-academy.com/posts/481-angular-routing/dynamic-parameter-min.png)

When we access `/old-pages/1`, Angular redirects us to `/pages/1`.

## [Nested routes](https://monsterlessons-academy.com/posts/angular-routing-essentials-all-you-need-to-know-in-one-post#nested-routes)

We learned how to create routes, but what about nested routes? Sometimes we want to nest our routes to access different parts of our application. Let’s create a nested route inside `/settings`.

```
// src/app/app.routes.ts
import { SettingsProfileComponent } from './settings/profile/profile.component';
export const routes: Routes = [
  ...
  {
    path: 'settings',
    component: SettingsComponent,
    children: [
      {
        path: 'profile',
        component: SettingsProfileComponent,
      }
    ]
  },
]
```

To do that, we add a `children` property to our `settings` route. The `children` property is an array containing different routes. It’s important to remember that the child route is not `settings/profile`; it is just `profile`. Angular will correctly interpret this declaration and create the route `/settings/profile` automatically.

![settings no outlet](https://cdn.monsterlessons-academy.com/posts/481-angular-routing/settings-no-outlet-min.png)

In the browser, we can access the `/settings/profile` route, but only the content of the settings page is visible. We don’t see our `SettingsProfileComponent`. To render it, we must use the `<router-outlet>` component, just like we did before.

```
<!-- src/app/settings/settings.component.html -->
<h2>Settings</h2>

<div class="main">
  <router-outlet />
</div>
```

We added `<router-outlet>` here, but we should also import it into our component.

```
// src/app/settings/settings.component.ts
import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';

@Component({
  selector: 'app-settings',
  standalone: true,
  imports: [RouterOutlet],
  templateUrl: './settings.component.html',
  styleUrl: './settings.component.css',
})
export class SettingsComponent {}
```

![profile](https://cdn.monsterlessons-academy.com/posts/481-angular-routing/profile-min.png)

Now it renders not only the settings page but also the profile component inside. It’s also important to remember that we can still access the `/settings` URL separately if needed.

## [Active routes](https://monsterlessons-academy.com/posts/angular-routing-essentials-all-you-need-to-know-in-one-post#active-routes)

Let’s add some links to our markup to check if there is a problem.

```
<!-- src/app/app/app.component.html -->
<div class="links">
  <a routerLink="/dashboard">dashboard</a>
  <a routerLink="/products">products</a>
  <a routerLink="/settings">settings</a>
  <a routerLink="/settings/profile">profile</a>
  <a routerLink="/pages/1">pages/1</a>
</div>
```

![not highlighted](https://cdn.monsterlessons-academy.com/posts/481-angular-routing/not-highlighted-links-min.png)

None of the links are highlighted on the screen as active. Typically, we want to highlight the active link to indicate which page we are on. How can we do that?

```
<!-- src/app/app/app.component.html -->
<div class="links">
  <a routerLink="/dashboard" routerLinkActive="active">dashboard</a>
  <a routerLink="/products" routerLinkActive="active">products</a>
  <a routerLink="/settings" routerLinkActive="active">settings</a>
  <a routerLink="/settings/profile" routerLinkActive="active">profile</a>
  <a routerLink="/pages/1" routerLinkActive="active">pages/1</a>
</div>
```

We added a `routerLinkActive` attribute which will add an `active` class when we are on this link. But in order for it to work we must inject a dependency to our component.

We added a `routerLinkActive` attribute, which will add an `active` class when the link is active. However, for it to work, we must import a dependency into our component.

```
import { RouterLink, RouterLinkActive, RouterOutlet } from '@angular/router';

@Component({
  ...
  imports: [RouterOutlet, RouterLink, RouterLinkActive]
})
```

![active link](https://cdn.monsterlessons-academy.com/posts/481-angular-routing/active-link-min.png)

Now, our active link is highlighted. We are on `/settings`, and it is red.

## [Exact route match](https://monsterlessons-academy.com/posts/angular-routing-essentials-all-you-need-to-know-in-one-post#exact-route-match)

But there’s a problem: When we navigate to `/settings/profile`, both links are highlighted.

![both highlighted](https://cdn.monsterlessons-academy.com/posts/481-angular-routing/both-highlighted-min.png)

Why does this happen? By default, Angular doesn’t do a full match for the URL. Both `/settings` and `/settings/profile` are partially matched with the route, so Angular highlights them both.

```
<!-- src/app/app/app.component.html -->
<div class="links">
  <a routerLink="/dashboard" routerLinkActive="active">dashboard</a>
  <a routerLink="/products" routerLinkActive="active">products</a>
  <a 
    routerLink="/settings" 
    routerLinkActive="active" 
    [routerLinkActiveOptions]="{exact: true}"
  >settings</a>
  <a routerLink="/settings/profile" routerLinkActive="active">profile</a>
  <a routerLink="/pages/1" routerLinkActive="active">pages/1</a>
</div>
```

This is not ideal for us, so we must provide `routerLinkActiveOptions` with `exact: true`. This will perform a full match for the URL and avoid the problem of highlighting multiple links.

![not highlighted](https://cdn.monsterlessons-academy.com/posts/481-angular-routing/not-highlighted-min.png)

Now, when we are on the profile page, the settings link is not highlighted.

## [Programmatic navigation](https://monsterlessons-academy.com/posts/angular-routing-essentials-all-you-need-to-know-in-one-post#programmatic-navigation)

One more important feature is programmatic navigation. This is when you have an event and want to trigger a router change. How can we do that?

```
<!-- src/app/dashboard/dashboard.component.html -->
<h2>Dashboard</h2>

<div>
  <button class="goToProductsBtn" (click)="goToProductsPage()">
    Go to products
  </button>
</div>
```

Inside `DashboardComponent`, I have a button where I want to add a click event called `goToProductsPage`. When the user clicks on the button, we want to redirect them to the `/products` page.

```
// src/app/dashboard/dashboard.component.ts
export class DashboardComponent {
  router = inject(Router);
  goToProductsPage(): void {
    this.router.navigateByUrl('/products');
  }
}
```

To perform navigation, we need to inject the `Router` into our component. Inside `goToProductsPage`, we can call `navigateByUrl`, which will change the page. It’s important to remember that we pass a full URL starting with a slash, not just a path like in the routes.

![programmatic](https://cdn.monsterlessons-academy.com/posts/481-angular-routing/programmatic-min.png)

We clicked on our button on the `/dashboard` page and were redirected to the `/products` page.

However, `navigateByUrl` is not the best option when you want to concatenate strings with variables.

```
// This will generate /categories/1/products/2 URL
this.router.navigate(['categories', categoryId, 'products', productId]);
```

In this case, using `navigate` is easier, as Angular will concatenate our parameters for us.

## [Lazy loading](https://monsterlessons-academy.com/posts/angular-routing-essentials-all-you-need-to-know-in-one-post#lazy-loading)

Another important functionality is lazy loading of routes. Lazy loading allows us to load a component only when we access that route, instead of bundling all components into a single file.

```
export const routes: Routes = [
  ...
  {
    path: 'products',
    loadComponent: () =>
      import('./products/products.component').then((c) => c.ProductsComponent),
  }
]
```

For the `/products` route, we used `loadComponent` with an import inside the `component` property. This is how we implement lazy loading, in contrast to normal bundling.

![lazy](https://cdn.monsterlessons-academy.com/posts/481-angular-routing/lazy-load-min.png)

When we navigate from `/dashboard` to `/products`, we can see in the Network tab that a chunk of JavaScript was loaded. This chunk contains our `ProductsComponent`, indicating that it was loaded only after we accessed this page. It is loaded separately and is not included in the main bundle.

> Lazy loading is extremely important if you want to make your bundle smaller and your application faster.

## [Route guard](https://monsterlessons-academy.com/posts/angular-routing-essentials-all-you-need-to-know-in-one-post#route-guard)

Now we need to understand how to restrict access to some pages in Angular. To do this, we use guards. What is a guard? It's a special function that checks your access before you can access the route. Here’s how it looks:

```
// src/app/auth.guard.ts
import { inject } from '@angular/core';
import { Router } from '@angular/router';
import { filter, map } from 'rxjs';
import { CurrentUserService } from './currentUser.service';

export const authGuard = () => {
  const currentUserService = inject(CurrentUserService);
  const router = inject(Router);

  return currentUserService.currentUser$.pipe(
    filter((currentUser) => currentUser !== undefined),
    map((currentUser) => {
      if (!currentUser) {
        router.navigateByUrl('/');
        return false;
      }
      return true;
    }),
  );
};
```

It is just a function which returns an `Observable` or `boolean`. We inject inside `CurrentUserService` and check the data of current user. If we have correct data inside then return true, which allows access to this page. In other case we redirect a user to the homepage.

```
import { authGuard } from './auth.guard';
export const routes: Routes = [
  ...
  {
    path: 'settings',
    component: SettingsComponent,
    children: [
      {
        path: 'profile',
        component: SettingsProfileComponent,
      },
    ],
    canActivate: [authGuard],
  },
]
```

To use this guard, we must provide it in the `canActivate` field of a route. In our case, it’s the settings route. Now, when we are not logged in, we cannot access this page.

## [Route resolver](https://monsterlessons-academy.com/posts/angular-routing-essentials-all-you-need-to-know-in-one-post#route-resolver)

The last feature you need to know about Angular Router is a resolver. What is a resolver? It can resolve some data or make an API call before you access a route. Here’s how it looks:

```
// src/app/data.resolver.ts
import { ResolveFn } from '@angular/router';
import { of } from 'rxjs';

export const pageResolver: ResolveFn<Object> = (route, state) => {
  const pageId = route.paramMap.get('pageId');
  return of({
    pageId,
    name: 'Foo',
  });
};
```

It is just a function that returns some data. Typically, you will return an `Observable` if you want to make an API call. In this case, we read a parameter from the URL and return an object.

```
import { pageResolver } from './data.resolver';
export const routes: Routes = [
  ...
  {
    path: 'pages/:pageId',
    component: PageComponent,
    resolve: {
      page: pageResolver,
    },
  },
]
```

Now, inside our routes, we can add a `resolve` property to our page route and specify that the result of `pageResolver` must be available in the `page` property.

```
// src/app/page/page.component.ts
export class PageComponent {
  pageId = input.required<string>();
  limit = input.required<string>();
  page = input.required<{ pageId: string; name: string }>();
}
```

In the same way we did with `pageId` and `limit`, we get the `page` data through the resolver, which we can then use in the component.

```
<h2>Page - {{ pageId() }} - {{ limit() }} - {{ page().name }}</h2>
```

![resolve](https://cdn.monsterlessons-academy.com/posts/481-angular-routing/resolver-min.png)

We successfully rendered the `name` property from our resolver on the screen.

**Want to conquer your next JavaScript interview?** Download my [FREE PDF - Pass Your JS Interview with Confidence](https://monsterlessons-academy.com/newsletter_subscribers/javascript_interview) and start preparing for success today!

[📚 Source code of what we've done](https://github.com/monsterlessonsacademy/monsterlessonsacademy/tree/508-angular-routing)

Don't miss a thing!

Oleksandr Kocherhin

![](https://cdn.monsterlessons-academy.com/mla-website/author-in-course.png)

Oleksandr Kocherhin is a full-stack developer with a passion for learning and sharing knowledge on [Monsterlessons Academy](https://monsterlessons-academy.com/) and on his [YouTube channel](https://youtube.com/MonsterlessonsAcademy). With around 15 years of programming experience and nearly 9 years of teaching, he has a deep understanding of both disciplines. He believes in learning by doing, a philosophy that is reflected in every course he teaches. He loves exploring new web and mobile technologies, and his courses are designed to give students an edge in the fast-moving tech industry.
