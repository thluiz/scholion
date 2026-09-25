---
url: "https://www.angularspace.com/mastering-component-communication-in-angular/?ref=dailydev"
captured_at: "2026-09-25T21:43:13+01:00"
title: "Mastering Component Communication in Angular"
domain: "angularspace-com"
---

![Mastering Component Communication in Angular](https://storage.ghost.io/c/3f/63/3f6333b8-1f83-4017-8426-91bfbc264d81/content/images/size/w1075h650/2024/12/rainer-angularspace--13-.jpg)

![](https://storage.ghost.io/c/3f/63/3f6333b8-1f83-4017-8426-91bfbc264d81/content/images/2024/12/thumbnail-1.png)

## Intro

Hey Angular devs! This guide explores how components can communicate with each other in your applications - from simple one-way data binding to more complex interactions, like passing data via router. While there are many different methods for component communication in Angular, we'll focus on providing an overview of different approaches without diving too deep into each one, because that would make this post endless.

I assure you that some techniques mentioned in this article will work better in certain situations, so it's essential to know all available options, proper use cases and differences. This helps you to choose the best solution for your application through your critical thinking and understanding the context of the problem.

Every approach will be explained with [code examples](https://github.com/michalgrzegorczyk-dev/angular-component-communication/tree/master/src/app?ref=angularspace.com), that you can run and test by yourself. The code examples shown in this blog post will be as simple, as possible, so I really recommend you to check the full examples in the mentioned code repository.

### Here's what we'll cover

*   Input and Output
    *   `@Input` and `@Output` decorators
    *   Brand new `input()` and `output()` functions
    *   Setter methods with `@Input` decorator
    *   `Input` and `Output` inheritance
    *   `OnChanges` lifecycle hook with `@Input` decorators and `computed()` alternatives
*   `@Injectable` Services
*   Component/Directive injection
*   Template variables (`#`)
*   Content Projection
    *   `@ContentChild` and `@ContentChildren` with `<ng-content>`
    *   `contentChild()` and `contentChildren()` with signals
*   View and Query List
    *   `@ViewChild` and `@ViewChildren` decorators
    *   `viewChild()` and `viewChildren()` with signals
*   Routing
    *   Routing Parameters and Queries (`/:id` and `?query=param`)
    *   Routing with `Input` and `withComponentInputBinding()` function
    *   Routing State Objects

## `Input`, `Output`, `Setter` and `ngOnChanges` Lifecycle Hook

![](https://storage.ghost.io/c/3f/63/3f6333b8-1f83-4017-8426-91bfbc264d81/content/images/2024/12/input-output.png)

### `Input` and `Output` in Angular

Let's explore the fundamental way components talk to each other in Angular - our first and probably most famous pair: `Input` and `Output`. We'll look at both traditional (decorator with `@`) and modern (functions) approaches to handle this communication. But before that, let's explore some practical uses of `Input` and `Output` and when to use them.

#### 💡 Examples of Practical Uses of `Input` and `Output`

1.  Develop more interactive components that notify parent elements of changes, e.g. dropdown menu or search.
2.  Pass data like user details to a child component and `Output` to emit user update events from the child to the parent component.
3.  Navigate from a product list to a detailed view using `Input` to pass the selected product ID to the detail component.

Good/Bad

Description

❌

Providing `Input` and `Output` via metadata properties can be harder to understand and can be less concise.

❌

Component inheritance is rarely used in Angular, so you may never need this.

⚠️

With `OnPush`, changing object properties won't update the view - you must assign a new object reference.

✅

It's the standard way to communicate between components, well-tested and recommended.

✅

The newest Angular version lets you transform data through `@Input()` decorator's metadata `transform` function, similar to `Setter`.

✅

Always good to use and recommended with signals (with `Signal`s from Angular 17+ as `input()` functions).

✅

`input()` and `output()` provide improved performance and change detection.

✅

Two-way binding simplifies code by reducing boilerplate for managing `Input`/`Output` pairs in common scenarios.

✅

Usage of `model()` function offers unification of `Input` and `Output`, which is typically useful in two-way data binding approaches.

#### Traditional Approach with Decorators

The classic way uses `@Input()` and `@Output()` decorators, which let child components receive data and send it back to their parents. To achieve this, we need to pass our data through brackets `[searchTerm]="myData"`, and if we need to receive data back, we need to assign it as `(searchTermChange)="handle($event)"` to handle the event.

```
// Component with traditional `Input` and `Output`.
@Component({
  selector: 'app-search-box'
})
class SearchBoxComponent {
  // Receives data from parent.
  @Input()
  searchTerm = '';

  // Sends data to parent.
  @Output()
  searchTermChange = new EventEmitter<string>();
}

// Using in parent template with two-way binding approach.
<app-search-box [(searchTerm)]="searchTermInitial" />
```

TypeScript

#### Modern Approach with `input()` and `output()`

Angular 17+ introduces a powerful new way using signal `input()` signal function and `output()` function. This approach offers better performance, smarter change detection and smoother integration with signals architecture, making it the go-to choice for new applications.

```
// Modern approach with signal `input()` function and `output()` function.
@Component()
class SearchBoxComponent {
  initialValue = input<string>();
  searchTermChange = output<string>();
} 
```

TypeScript

#### `Input` and `Output` Inheritance

While it's not a common practice in Angular projects, Angular supports inheriting `Input` and `Output` properties from parent components.

```
// Parent component with `Input`.
@Component({
  selector: 'app-base-card',
})
class BaseCardComponent {
  @Input()
  title = 'Header';
}

// Child component inheriting parent's `Input`.
@Component({
  selector: 'app-product-card',
})
class ProductCardComponent extends BaseCardComponent {
  // Child gets access to `title` property.
  constructor() {
    super();
    console.log(this.title);
  }
}
```

TypeScript

### `Setter` Methods

![](https://storage.ghost.io/c/3f/63/3f6333b8-1f83-4017-8426-91bfbc264d81/content/images/2024/12/setter.png)

Want more control over your `Input`? Angular's `Setter` methods let you intercept and handle `Input` values before they're set. Let's firstly evaluate it's pros and cons:

Good/Bad

Description

❌

Requires additional property for storing the value.

❌

More verbose than simple `Input` declarations.

❌

Input setters are executed individually, potentially leading to race conditions, if setters depend on the state of other inputs.

❌

Updating e.g. global updates from `Setter` or lifecycle hooks can cause `NG0100 ExpressionChanged` error.

⚠️

Improper use can cause side effects that you may not want (sometimes you might want them).

✅

Signals resolve these issues by ensuring a consistent state across all inputs and removing order dependencies entirely.

✅

Enables input validation on the fly.

✅

Allows data transformation as values come in.

✅

Can trigger side effects when new values change.

```
// Example of `Setter` usage.
@Input()
set name(value: string) {
  console.log('New name:', value);
  // Store the value in component from setter.
  this._name = value.trim();
}
```

TypeScript

Full set of examples around this topic you can find [here](https://github.com/michalgrzegorczyk-dev/angular-component-communication/tree/master/src/app/1-input-output?ref=angularspace.com).

* * *

### Understanding `ngOnChanges` Lifecycle Hook

![](https://storage.ghost.io/c/3f/63/3f6333b8-1f83-4017-8426-91bfbc264d81/content/images/2024/12/ng-on-changes.png)

Now, let's explore `ngOnChanges`, a helpful lifecycle hook in Angular that tracks changes to your component's input values. When `Input` change, Angular automatically runs this method, providing you with `SimpleChanges` argument that tell you three key things: what changed, if it's the first change, and both the old and new values.

#### 💡 Examples of Practical Uses of `ngOnChanges`

1.  Implementing undo/redo functionality by tracking previous values.
2.  Validating dependent `Input` when multiple `Input` change together (like form validation rules).

Good/Bad

Description

❌

Executes on every input change, which may affect performance if not used carefully.

❌

Runs for all input changes, even when you're interested in specific ones only.

❌

Requires setting up additional properties to track changes.

❌

It should be never used with signal `Input`. That's useless since we have computed signals.

⚠️

Runs first before `ngOnInit` Lifecycle Hook.

⚠️

Improper use can cause side effects that you may not want.

⚠️

With `OnPush`, changing object properties won't update the view - you must assign a new object reference.

✅

Efficiently handles multiple `Input` changes in a single lifecycle hook.

✅

Provides easy detection of first-time changes to `Input` properties.

✅

Enables comparison between previous and current `Input` values.

```
// Component that tracks `Input` changes with `ngOnChanges`.
@Component()
class NameDisplay implements OnChanges {
  @Input() name = '';
  @Input() title = '';  // Adding a second input for title (Mr., Ms., Dr., etc).

  greeting = signal('Hello!')
    
  ngOnChanges(changes: SimpleChanges) {
    // Combine both inputs whenever either changes.
    if ('name' in changes || 'title' in changes) {
      const currentName = 'name' in changes ? changes['name'].currentValue : this.name;
      const currentTitle = 'title' in changes ? changes['title'].currentValue : this.title;
      
      // Create combined greeting.
      const fullGreeting = currentTitle
        ? `Hello, ${currentTitle} ${currentName}!`
        : `Hello, ${currentName}!`
        
      if ('name' in changes) {
        console.log('Name changed:', changes['name'].previousValue, '->', currentName);
      }
      
      if ('title' in changes) {
        console.log('Title changed:', changes['title'].previousValue, '->', currentTitle);
        this.greeting.set(fullGreeting);
      }
    }
  }
}
```

TypeScript

```
// Alternative solution that tracks `Input` with computed signals instead.
@Component()
class NameDisplay {
  name = input('');
  title = input('');
  
  // Create a computed signal that automatically updates when inputs change.
  greeting = computed(() => {
    const currentName = this.name();
    const currentTitle = this.title()
    
    console.log('Name or title updated:', { name: currentName, title: currentTitle })
    return currentTitle ? `Hello, ${currentTitle} ${currentName}!` : `Hello, ${currentName}!`;
  });
}
```

TypeScript

Full set of examples around this topic you can find [here](https://github.com/michalgrzegorczyk-dev/angular-component-communication/tree/master/src/app/2-input-ng-on-changes?ref=angularspace.com).

* * *

## Services in Angular

![](https://storage.ghost.io/c/3f/63/3f6333b8-1f83-4017-8426-91bfbc264d81/content/images/2024/12/service.png)

Services are a fundamental feature in Angular that serve multiple purposes, with one of their most powerful uses being data sharing between components. When provided at the `root` level, services create a centralized way for components to communicate and exchange information effectively.

Think of a service as a central hub where components can store and access shared data. Any component can read from or write to this hub, creating a smooth two-way flow of information.

#### 💡 Examples of Practical Uses of Services

1.  Store user login states, preferences, and session tokens, providing a consistent user experience across different parts of the application.
2.  Manage all backend API calls from a single service, simplifying the process of fetching, posting, and handling data across components.
3.  Creating utility functions used across multiple components (formatters, validators).

Good/Bad

Description

❌

Requires understanding of Angular's dependency injection system.

⚠️

Simple class that can be injected, usually used with `Signal`s or `Observable`s.

✅

Enables component communication without creating direct dependencies.

✅

Works across multiple components throughout your application.

✅

Provides a centralized place for sharing data and logic.

✅

Makes testing easier by separating concerns.

```
// Service that manages shared data.
@Injectable({
  providedIn: 'root'
})
class CartStore {
  cart = signal(['candy', 'chips', 'soda']);

  addItem(item: string) {
    this.cart.set([...this.cart(), item]);
  }
}

// Component using the shared service.
class CartComponent {
  cartStore = inject(CartStore);
  cart = this.cartStore.cart;
  
  addItem(item: string) {
    this.cartStore.addItem(item);
  }
}
```

TypeScript

Full set of examples around this topic you can find [here](https://github.com/michalgrzegorczyk-dev/angular-component-communication/tree/master/src/app/3-service?ref=angularspace.com).

* * *

## Template Variables in Angular

![](https://storage.ghost.io/c/3f/63/3f6333b8-1f83-4017-8426-91bfbc264d81/content/images/2024/12/template-variable.jpeg)

Template variables are a really cool feature in Angular marked by the `#` symbol in the template. Think of them as quick references you can create in your template to connect parent and child components. It's like giving your components nicknames they can use to talk to each other!

#### 💡 Examples of Practical Uses of Template Variables

1.  Managing component state from parent templates (expand/collapse panels, pagination controls).
2.  Form manipulation (accessing form values, triggering validation, resetting forms).
3.  Quickly access and manipulate DOM elements directly from the template without additional logic in the component class.

Good/Bad

Description

❌

Limited scalability due to tight coupling between components.

❌

Variables are only accessible within the template unless passed through events.

❌

Timing issues can occur if accessing elements before they're rendered.

✅

Enables bi-directional communication between parent and child components within templates.

✅

Works smoothly with `ViewChild` and template functions for element access.

✅

Provides quick, direct access to component references.

✅

Reduces boilerplate code by eliminating need for `Input`, `Output`, or services.

✅

Gives parent components full access to child methods and properties.

```
// Child component with todo management.
@Component()
class TodoListComponent {
  todos = ['Learn Angular', 'Build an app'];

  addTodo() {
    this.todos.push(`New Todo ${this.todos.length + 1}`);
  }
}

// Parent component using template variable.
@Component({
  template: `
    <todo-list #todoList/>
    <button (click)="addTodo(todoList)">Add Todo</button>
  `,
  imports: [TodoListComponent]
})
class ParentComponent {
  addTodo(todoList: TodoListComponent) {
    // Access child component through template variable.
    todoList.addTodo();
  }
}
```

TypeScript

Full set of examples around this topic you can find [here](https://github.com/michalgrzegorczyk-dev/angular-component-communication/tree/master/src/app/4-template-variable?ref=angularspace.com).

* * *

## Injected Components in Angular

![](https://storage.ghost.io/c/3f/63/3f6333b8-1f83-4017-8426-91bfbc264d81/content/images/2024/12/injected-component.png)

Let's explore an interesting but rarely-used technique of component injection. This approach lets a child component directly access its parent by injecting the parent component into the child's constructor. While not common usage with components, it's worth understanding for specific use cases.

#### 💡 Examples of Practical Uses of Injected Components

1.  Complex form components where child fields need parent form context.
2.  Nested menu structures where child items need parent menu state.
3.  Wizard/stepper components where steps need access to the main wizard state.

Good/Bad

Description

❌

Rare in real-world applications, which may make the code less maintainable for teams.

❌

Creates strong dependencies between components, reducing reusability.

❌

Limited to one-way communication from child to parent.

❌

Only works with direct parent components in the hierarchy.

⚠️

Rare usage with components but not with directives.

✅

Simplifies parent-child communication in specific cases without extra services.

✅

Provides direct access to parent methods and properties from the child component.

```
// Parent component that child can access.
@Component()
class DialogManagerComponent {
  openDialog() {
    alert('Opening modal dialog!');
  }

  closeDialog() {
    alert('Closing modal dialog!');
  }
}

// Child component with injected parent.
class DialogButtonComponent {
  constructor(private dialogManager: DialogManagerComponent) {
    this.dialogManager.openDialog(); // Direct access to parent's methods.
  }
  
  handleClick() {
    this.dialogManager.closeDialog();
  }
}
```

TypeScript

Full set of examples around this topic you can find [here](https://github.com/michalgrzegorczyk-dev/angular-component-communication/tree/master/src/app/5-injected-component?ref=angularspace.com).

* * *

## ViewChild and ViewChildren

![](https://storage.ghost.io/c/3f/63/3f6333b8-1f83-4017-8426-91bfbc264d81/content/images/2024/12/view-child.png)

### Understanding ViewChild in Angular

`ViewChild` is a versatile Angular tool that lets parent components interact directly with their child components. By default, it selects the first matching element or component in the view, making it perfect for one-to-one parent-child communication through the template.

#### 💡 Examples of Practical Uses of `ViewChild`

1.  Controlling UI components programmatically (modal dialogs, accordion panels).
2.  Interacting with third-party components (maps, charts, date pickers).
3.  Managing multiple similar components (tabs, carousel slides, list items).

Good/Bad

Description

❌

Creates tight coupling between parent and child components, which can limit reusability.

❌

Limited to direct parent-child relationships only.

❌

Extensive use of `ViewChild` can make applications harder to maintain and test.

✅

Provides direct access to child component's public methods and properties.

✅

Enables real-time access to child component's state and behavior.

#### Traditional approach

The classic method uses the `@ViewChild()` decorator to connect a parent with its child component. You'll reference the child component's class in the decorator to establish this connection.

```
// Child component with a method parent can call.
@Component({
  selector: 'app-search-input',
})
class SearchInputComponent {
  clearInput() {
    console.log('Clearing search input');
  }

  focus() {
    console.log('Focusing search input');
  }
}

// Parent component that controls the child.
@Component({
  selector: 'app-search-bar',
  template: `
    <app-search-input />
    <button (click)="resetSearch()">Reset Search</button>
  `,
  imports: [SearchInputComponent]
})
class SearchBarComponent {
  @ViewChild(SearchInputComponent)
  searchInput: SearchInputComponent;

  resetSearch() {
    this.searchInput.clearInput();
    this.searchInput.focus();
  }
}
```

TypeScript

#### Modern Signal-Based Approach

Angular 17.2 introduces a cleaner way to use `ViewChild` with the `viewChild()` signal function (stable from Angular 19). You can specify either a template reference variable or a component class to locate the child component.

```
// Parent component using signal-based ViewChild.
@Component({
  template: `
    <app-search-input />
    <button (click)="resetSearch()">Reset Search</button>
  `,
  imports: [SearchInputComponent]
})
class SearchBarComponent {
  searchInput = viewChild<SearchInputComponent>(SearchInputComponent);

  resetSearch() {
    this.searchInput().clearInput();
    this.searchInput().focus();
  }
}
```

TypeScript

Full set of examples around this topic you can find [here](https://github.com/michalgrzegorczyk-dev/angular-component-communication/tree/master/src/app/6-view-child?ref=angularspace.com).

* * *

### Understanding ViewChildren in Angular

Building on our knowledge of `ViewChild` comes its sibling feature, `ViewChildren`. This robust tool lets a parent component work with multiple child components or elements in its template. While `ViewChild` gives you one element, `ViewChildren` provides a `QueryList` containing all matching elements.

#### 💡 Examples of Practical Uses of `ViewChildren`

1.  Managing dynamic lists of components (todo items, form fields, list items).
2.  Managing form array elements for dynamic forms.
3.  Controlling multiple tab panels or accordion sections.

#### Traditional Approach

The classic method uses the `@ViewChildren()` decorator to access multiple  
child components from the parent. You'll reference the child component's class in the decorator - it's similar to `ViewChild` but gives you access to all instances instead of just one.

```
// Parent component that manages multiple children.
@Component({
  selector: 'app-tab-group',
  template: `
    @for (tab of ['Dashboard', 'Profile', 'Settings']) {
      // Child components we want to access.
      <app-tab/>
    }
    <button (click)="closeAllTabs()">Close All Tabs</button>
  `,
  imports: [TabComponent]
})
class TamGroupComponent {
  @ViewChildren(TabComponent) 
  tabs: QueryList<TabComponent>;

  closeAllTabs() {
    this.tabs.forEach(child => child.close());
  }
}

// Child component with method that parent can call.
@Component({
  selector: 'app-tab',
})
class TabComponent {
  close() {
    console.log('Closing tab');
  }
}
```

TypeScript

#### Modern Signal-Based Approach

Angular 17+ introduces a cleaner way to use `ViewChildren` with the `viewChildren()` signal function. It works the same way but leverages Angular's reactive signal system for better performance and cleaner code.

```
// Parent component using signal-based ViewChildren.
@Component({
  selector: 'app-tab-group',
  template: `
    @for (tab of ['Dashboard', 'Profile', 'Settings']) {
      // Child components we want to access.
      <app-tab/>
    }
    <button (click)="closeAllTabs()">Close All Tabs</button>
  `,
  imports: [TabComponent]
})
class TabGroupComponent {
  tabs = viewChildren<TabComponent>(TabComponent);

  closeAllTabs() {
    this.tabs().forEach(child => child.close());
  }
}

// Child component with method that parent can call.
@Component({
  selector: 'app-tab',
})
class TabComponent {
  close() {
    console.log('Closing tab');
  }
}
```

TypeScript

Full set of examples around this topic you can find [here](https://github.com/michalgrzegorczyk-dev/angular-component-communication/tree/master/src/app/7-view-children?ref=angularspace.com).

* * *

## ContentChild and ContentChildren in Angular

![](https://storage.ghost.io/c/3f/63/3f6333b8-1f83-4017-8426-91bfbc264d81/content/images/2024/12/content-projection.png)

Here's how to work with projected content in Angular components. While `ViewChild` and `ViewChildren` handle elements in a component's template,  
`ContentChild` and `ContentChildren` deal with content that's projected between component tags. This advanced feature helps you manage content passed from parent components.

#### 💡 Examples of Practical Uses of Content Projection

1.  Card component might have a predefined style and layout (like header, body, and footer areas), but the actual content of these areas can be projected by the parent component, allowing for versatile reuse across different parts of an application.
2.  Tab set component where each tab’s content is projected from a parent component, allowing each tab content to be uniquely defined while using the same tab navigation system.

Good/Bad

Description

❌

Content is only available after the `ngAfterContentInit` lifecycle hook, not during initialization.

❌

Component initialization cannot access or manipulate projected content.

❌

Lacks strong typing, making it harder to ensure type safety for projected content.

⚠️

Using multiple `<ng-content>` slots adds complexity, but enables powerful component compositions when used carefully.

✅

Creates flexible and reusable components through content projection features.

✅

Provides direct access to projected content, making it easy to interact with nested elements.

#### Traditional Approach Explained

The classic way uses `@ContentChild()` and `@ContentChildren()` decorators along  
with the `<ng-content>` tag. This combination gives you flexible ways to project and manage content.

```
// Parent component with content projection slots.
@Component({
  selector: 'app-panel',
  template: `
    <div class="parent">
      <ng-content select="[header]" />
      <ng-content />
    </div>
  `
})
class PanelComponent implements AfterContentInit {
  @ContentChild('title') 
  title: ElementRef;

  @ContentChildren(PanelItemComponent) 
  items: QueryList<PanelItemComponent>;

  ngAfterContentInit() {
    // Access projected content after initialization.
    this.items.forEach(item => console.log(item.title));
  }
}

// Child item component.
@Component({
  selector: 'app-panel-item',
  template: `<div class="item">{{ text() }}</div>`
})
class PanelItemComponent {
  text = signal('');
}

// Example usage in a parent component.
@Component({
  template: `
    <app-panel>
      <h2 title>Title Here</h2>
      <app-panel-item text="First item" />
      <app-panel-item text="Second item" />
    </app-panel>
  `
})
```

TypeScript

#### Modern Signal-Based Approach

Angular 17+ introduces signal-based versions with `contentChild()` and `contentChildren()` functions. They work similarly, but give you the power of signals.

Full set of examples around this topic you can find [here](https://github.com/michalgrzegorczyk-dev/angular-component-communication/tree/master/src/app/8-content-projection?ref=angularspace.com).

* * *

## Routing Parameters & Queries in Angular

![](https://storage.ghost.io/c/3f/63/3f6333b8-1f83-4017-8426-91bfbc264d81/content/images/2024/12/router.png)

### Routing Parameters

This section explores how to pass data between Angular components using route parameters. This is especially helpful when you need to share information between components that aren't directly connected in your component tree.

To get started, you'll need to set up your routes in the configuration and pass them to the `provideRouter(routes)` function (or `RouterModule` if you're using the older approach). Once set up, you can pass values through these routes when navigating. Your components can then easily access these parameters.

#### 💡 Examples of Practical Uses of Routing Params

1.  Most common use case is navigation to detailed view of specific item.
2.  Steps in multistep process or workflow, can help to keep track of the current step like `/checkout/step-2`.
3.  Filtering subsections of data like `products/category/electronics`.

Good/Bad

Description

❌

Params are always strings, so you may need to parse or convert complex data types.

❌

Sensitive data passed through the URL can be visible and prone to tampering.

✅

Allows passing data between components without direct parent-child relationships, enabling more flexible component interaction.

✅

Data in URL params is preserved during navigation and can be shared easily through links.

✅

Components can easily access params via `ActivatedRoute` service.

```
// Sets up the routing configuration.
const routes = [
  { path: 'details/:id', component: DetailsComponent },
];

const appConfig = {
  providers: [provideRouter(routes)]
};

// Parent component handles navigation to details.
@Component({
  selector: 'app-product',
  template: `
    <button (click)="showDetails()">Show details</button>
    <router-outlet />
  `,
  imports: [RouterOutlet]
})
class ProductComponent {
  router = inject(Router);

  showDetails() {
    this.router.navigate(['/details', '123']);
  }
}

// Child component uses the route parameter value.
@Component({
  selector: 'app-details',
})
class DetailsComponent implements OnInit {
  productId = signal('');
  activatedRoute = inject(ActivatedRoute);

  ngOnInit() {
    this.activatedRoute.params.subscribe(params => { // Remember to unsubscribe in real app or use `toSignal`.
      this.productId.set(params['id']); // Will use product id '123' from router params.
    });
  }
}
```

TypeScript

Full set of examples around this topic you can find [here](https://github.com/michalgrzegorczyk-dev/angular-component-communication/tree/master/src/app/9-routing-params?ref=angularspace.com).

* * *

### Routing Queries in Angular

Routing queries offer a perfect solution for handling optional parameters. Unlike regular route parameters that are part of the URL path, query parameters come after a question mark (`?`) in your URL. For example: `localhost:4200/table?sort=asc`. They're great for handling things like sorting, filtering, or page numbers.

You can add, change, or remove query parameters without changing your main route path. Your components can then read these parameters to adjust what they show or how they behave.

#### How Are Query Parameters Different from Route Parameters?

*   Let's take a look on URL structures:
    *   Route parameters: `/details/123`
    *   Query parameters: `/details?id=123&sort=name&order=asc`

#### 💡 Examples of Practical Uses of Routing Queries

1.  Filtering and Sorting, e.g. list view data are common uses for query parameters.
2.  Pagination - query parameters can be used to store the current page number.
3.  Search terms - useful for any application that has a search feature, enhancing user experience by allowing direct navigation to pre-searched results.
4.  Pre-populating forms through link, query parameters can carry the necessary data to populate form fields.

Good/Bad

Description

❌

Can only handle string data, complex data types need parsing or conversion.

❌

Sensitive data is exposed in the URL, making it vulnerable to tampering.

❌

Handling large or nested data with query params can become messy.

❌

Browser URL length limits restrict passing large data sets via query params.

❌

Not suitable for real-time communication, only for passing state during navigation.

✅

Easy to share application state across users or sessions.

✅

Persist in the URL, allowing bookmarking and sharing links with current state.

✅

Ideal for optional, changeable data that doesn't define the route.

✅

Can pass multiple key-value pairs in a single URL, making it flexible for data sharing.

```
// Parent component handles navigation to details page.
@Component({
  selector: 'app-product',
  template: `
    <button (click)="showDetails()">Show details</button>
  `,
})
class ProductComponent {
  router = inject(Router);

  showDetails() {
    this.router.navigate(['/details'], {
      queryParams: {
        id: '123',
        name: 'John',
        role: 'Developer'
      }
    });
  }
}

// Child component displays the query parameter values.
@Component({
  selector: 'app-details',
  template: `
    <p>ID: {{ id() }}</p>
    <p>Name: {{ name() }}</p>
    <p>Role: {{ role() }}</p>
  `,
})
class DetailsComponent implements OnInit {
  route = inject(ActivatedRoute);
  queryParams = toSignal(this.route.queryParams, { 
    initialValue: {} as Params 
  });

  id = computed(() => this.queryParams()['id'] || '');
  name = computed(() => this.queryParams()['name'] || '');
  role = computed(() => this.queryParams()['role'] || '');
}
```

TypeScript

Full set of examples around this topic you can find in the [here](https://github.com/michalgrzegorczyk-dev/angular-component-communication/tree/master/src/app/10-routing-queries?ref=angularspace.com).

* * *

### Using `withComponentInputBinding()` for Easier Routing

Angular 16+ introduced a game-changing feature that does exactly that! Let's explore how `withComponentInputBinding()` makes routing and data handling much smoother.

This new approach creates a direct connection between your URL parameters and component `Input`. It's like having an automatic pipeline that connects your URLs to your components, saving you from writing extra code!

To use this feature, you'll need the `withComponentInputBinding()` function from the Angular router. Once set up, the router will automatically connect your URL parameters to your component `Input` when someone visits a page.

#### 💡 Examples of Practical Uses of Routing `Input` Binding

1.  Product detail pages with product information in route (e.g. `/products/:productId`)
2.  Blog post pages with slug parameters (e.g. `/blog/:category/:slug`)

Good/Bad

Description

❌

Can make routing more complex if used too much.

❌

Not great for complex data that changes often.

❌

Data only flows one way.

❌

Types aren't checked automatically.

⚠️

It can only be used with the routed components.

✅

Clean, organized route setup.

✅

Components can talk through routes.

✅

Less code needed to implement simple solution.

```
// Parent component handles navigation.
@Component({
  template: `
    <button (click)="viewProductDetails('155')">View Product</button>
    <router-outlet />
  `,
  imports: [
    ProductDetailsComponent,
    RouterOutlet
  ],
})
class ProductListComponent {
  router = inject(Router);

  viewProductDetails(productId: string) {
    this.router.navigate(['/product', productId]);
  }
}

// Child component receives the productId.
@Component({
  template: `
    Product ID: {{ productId() }}
  `,
})
class ProductDetailsComponent {
  // Updates to '155' when you click the button in the parent.
  productId = input(''); 
}
```

TypeScript

Full set of examples around this topic you can find [here](https://github.com/michalgrzegorczyk-dev/angular-component-communication/tree/master/src/app/11-routing-input?ref=angularspace.com).

* * *

### Routing State Object

When you perform navigation actions in Angular, you can also pass along a state object in the navigation extras. This object is transient, meaning it is only available during the lifetime of the navigation and does not persist if the page is reloaded.

You can pass the state object using the `navigate()` method of the `Router` service, or through a `[routerLink]` directive with binding.

Once you navigate to the destination component, you can access the state from the `Router` service. This is typically done in the `ngOnInit` lifecycle hook or directly in the constructor, depending on when you need to access the data.

#### 💡 Examples of Practical Uses of State Objects

1.  Pre-populating - if you navigate to a form component, and you want pre-populate it with data from the previous component, you can pass this data through the state object.
2.  Confirming actions - if a user performs an action, and you need to pass results or confirmation messages to the next component, you can use the state object.
3.  Avoid secure data in URL - if you have sensitive data that you don't want to expose in the URL, you can pass it through the state object.

Good/Bad

Description

❌

Does not work properly with SSR, because it loses the state.

❌

Impossible to share a link to a specific application state with another user.

❌

State object is not inherently type-safe by default.

⚠️

Data passed in the state object is not retained after a refresh or if the navigation history is modified.

⚠️

Actually, it's possible to pass data via URL and retrieve it even after a refresh (it depends how object is created), but in this example, we don't want to add anything more to the URL. We did it in previous topics about routing communication via queries or params.

✅

Ability to pass complex data objects between components during navigation.

✅

The router state object allows you to pass sensitive or personal data between components without exposing it in the URL

```
// Parent component navigate to next component.
@Component({
  template: `
    <button (click)="navigateToDetails()">View Full Profile</button>
  `,
})
class ProfileSummaryComponent {
  router = inject(Router);
  
  changeRoute() {
    this.router.navigate(['profile-details'], { state: { userProfile: { name: 'JohnDoe', memberSince: 2020 }}});
  }
}

// Child component receives the state object.
@Component()
class ProfileDetailsComponent {
  router = inject(Router);

  constructor() {
    this.router.events.pipe(
      filter(e => e instanceof NavigationStart),
      map(() => this.router.getCurrentNavigation()?.extras.state),
    ).subscribe(profileData => { // Remember to unsubscribe in real app or use `toSignal`.
      if (profileData) {
        console.log('Received profile data:', profileData);
      }
    });
  }
}
```

TypeScript

Full set of examples around this topic you can find [here](https://github.com/michalgrzegorczyk-dev/angular-component-communication/tree/master/src/app/12-routing-object?ref=angularspace.com).

* * *

## Outro

That's it, you finally reached to the end of this blog post. We've covered all the ways of component communication in Angular, showed cases for "old" syntax and most recent with usage of signals.

Remember that all the examples are available in the [GitHub repository](https://github.com/michalgrzegorczyk-dev/angular-component-communication/tree/master/src/app?ref=angularspace.com).

I hope you found this guide helpful! Feel free to leave a comment below with any questions, or if you encounter any errors in the code, please open an issue on [GitHub](https://github.com/michalgrzegorczyk-dev/angular-component-communication/issues/new?ref=angularspace.com).

* * *

![](https://storage.ghost.io/c/3f/63/3f6333b8-1f83-4017-8426-91bfbc264d81/content/images/2024/12/Screenshot-2024-11-13-at-15.jpg)

* * *

![](https://storage.ghost.io/c/3f/63/3f6333b8-1f83-4017-8426-91bfbc264d81/content/images/2024/12/angular-university-banner-4--1--1.jpg)

**Last Update:** December 16, 2024
