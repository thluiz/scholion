---
url: "https://www.angularspace.com/fascinating-dependency-injection/?ref=dailydev"
captured_at: "2026-09-25T21:52:04+01:00"
title: "Fascinating Dependency Injection"
domain: "angularspace-com"
---

![Fascinating Dependency Injection](https://storage.ghost.io/c/3f/63/3f6333b8-1f83-4017-8426-91bfbc264d81/content/images/size/w1075h650/2024/09/Screenshot-2024-09-20-at-16.14.23.png)

Dependency Injection is a technique that we use every single day as Angular developers. It allows us to reuse things, access native constructs like `HttpClient`, retrieve data from routing, and much more. However, my general feeling has been that Angular developers often underestimate the capabilities of DI. In this article, we will explore some of the more interesting and useful features that sometimes go overlooked. Let's get started!

## What actually is DI?

Often, getting an answer to this question is enough to unlock more features that this mechanism has to offer. And, even more often, people slightly misunderstand how it actually works, leaving us with limited capacity when it comes to problems that could actually be solved with ease using DI.

One mental mistake that we can often encounter is when developers think of DI as some sort of a "pool", from which we can "retrieve" instances to work with them afterwards. However, DI is not a pool, or, let's say, an abstract dictionary of objects tied to some keys, but rather a strictly hierarchical system in which the same  
"key" (what we professionally refer to as "`InjectionToken`") can return very different things depending on the context in which it is being requested.

How is this being achieved? Well, we are not going **too** deep into the details (there are many more nuances than we can cover here), but we will mention that DI is closely tied to the DOM structure of the application. Yes, you read it right, the "thing" that helps us get service instances is actually closely related to our DOM tree.

What does it mean? Well, when our application renders the UI, for each HTML element it renders in the DOM, it also creates a special object, named `ElementInjector`, that is responsible for dependency injection **in the context of** that element and its children.

Now, again, without going into too much details, an element injector can be imagined as an object that has a parent injector (the one that has been created for this element's parent), and has a "dictionary" of tokens and their corresponding instances. Consider this:

```
@Directive({
    selector: '[appSome]',
})
export class SomeDirective implements OnInit {
    private readonly elementRef = inject(ElementRef);

    ngOnInit() {
        console.log(this.elementRef.nativeElement);
    }
}
```

TypeScript

Now, if we use this directive twice in the same template...

```
<div appSome>
    <span appSome>Text</span>
</div>
```

HTML

We will get different elements logged in the console, despite having injected the same `ElementRef`! This is because each of these elements has its own element injector, for which Angular automatically provides the `ElementRef` instance. Then, when we use the directive, Angular will ask the element injector for the instance of the token, and it will return different objects for each element.

This, of course, reveals to us how the dependency injection mechanism operates. When we ask for a dependency, Angular first looks at the nearest element injector (what we know as the host element - in this case, the element on which the directive is applied), and, if it finds the token, it will return the instance that was previously provided for that token (`ElementRef` in our case).

If it does not find the token, however, it will ask its parent element injector, and so on, until it reaches the root injector. After the root injector, it will ask the [platform injector](https://angular.dev/guide/di/hierarchical-dependency-injection?ref=angularspace.com#platform-injector), which is irrelevant to this article. Finally, if the dependency is not also found there, Angular will move to the very top of the hierarchy, where it stumbles upon the `NullInjector`, a word familiar to all Angular developers from the iconic "`NullInjectorError`: No provider for {token}". `NullInjector` is a special injector that is empty and always throws an error when asked for any token.

You might notice that this process is similar to how prototypes work in JavaScript. When we ask for a property in any object, it first looks into the object itself, then its prototype, and so on, until it reaches the `Object.prototype`, and then tries accessing its prototype, which is `null`, thus throwing an error. This is beautiful similarity that is useful to remember when we are dealing with DI.

> \[!NOTE\] The process of hierarchical lookup of DI tokens can be modified by different options like `Host`, `Optional`, and so on. We will look at them further down this article.

So, as we now understand (at least) how DI lookup works, let's now understand how dependencies are created, or, as the more proper term is, provided.

## Providing dependencies

Now this is the place where a lot of our DI magic happens. Obviously, following the lookup process, any dependency that want to inject must first be provided somewhere. Some dependencies, like `ElementRef` that we encountered previously, are automatically provided by Angular when the corresponding element and its injector are being created. Some, of course, more well known to us, have to be manually provided.

Understanding what options we have when providing dependencies will help us utilize it in a way that minimizes boilerplate code _everywhere_ in our application. Let's start with the simplest one: providing a dependency via a class:

```
export const appConfig: ApplicationConfig = {
    providers: [
        SomeService, 
    ],
};
```

TypeScript

This is equivalent to the following:

```
export const appConfig: ApplicationConfig = {
    providers: [
        {provide: SomeService, useClass: SomeService},
    ],
};
```

TypeScript

As this is self-describing, Angular just gives us a shorthand way to simply declare the class we want to provide. Of course, this is nowadays found only when some service is not provided in the root of our application, which is not often (although an absolutely valid case!).

Now, we can also provide a value instead of a class that needs to be instantiated. This is useful for sharing some global configurations wile keeping the type-safety. For instance, lots of Angular apps utilize [environments](https://angular.dev/tools/cli/environments?ref=angularspace.com), special files that get replaced with specific values depending on the type of a build we perform (development, staging, production, etc.).

A good practice is to create a token (or maybe a class) that has the same type as whatever data we have in the environment files, for instant, if we have an environment like this:

```
export const environment = {
    production: true,
    apiUrl: 'https://api.example.com',
};
```

TypeScript

We can create a class that reflects this data so we can inject it anywhere:

```
export class ApplicationConfig {
    readonly production: boolean;
    readonly apiUrl: string;
}
```

TypeScript

Finally, we can utilize the `useValue` option to provide the value of the class we created:

```
import { environment } from './environments/environment';

export const appConfig: ApplicationConfig = [
    {provide: ApplicationConfig, useValue: environment},
];
```

TypeScript

And then we can just inject the environment anywhere without the need to reference the environment file:

```
@Injectable()
export class SomeService {
    private readonly environment = inject(Environment);
    private readonly http = inject(HttpClient);

    getData() {
        return this.http.get(this.environment.apiUrl + '/data');
    }
}
```

TypeScript

Now, the next option that is of interest to us is the `useExisting` option. This is rarely used, however it can be useful if we want to limit our developers using a third-party API. For instance, some other Angular service that we do not own might have multiple methods and properties that can do dramatic things like manipulate the DOM structure of our application or maybe register multiple event listeners, affecting the change detection process.

However, we might only be interested in some utility methods from the service, and want to restrict unintended access to other, heavier methods. This way, we can create a shell class with the limited functionality we want to expose, and then provide it as is, while actually using the full-blown third-party service under the hood.

```
// list only the methods we want
type ExposedThirdPartyApi = Pick<ThirdPartyService, 'someMethod' | 'someOtherMethod'>;

export abstract class ShellService implements ExposedThirdPartyApi {
    abstract someMethod(): void;
    abstract someOtherMethod(): void;
}
```

TypeScript

And then we can just provide the third-party service through this shell service:

```
export const appConfig: ApplicationConfig = {
    providers: [
        {provide: ShellService, useExisting: ThirdPartyService},
    ],
};
```

TypeScript

And then, we can simply use the shell service to only access the methods that our application configuration allows:

```
@Injectable()
export class SomeService {
    private readonly shellService = inject(ShellService);

    getData() {
        return this.shellService.someMethod();
    }
}
```

TypeScript

> \[!NOTE\] These options like `useValue`, `useExisting` and so on can be used anywhere where providers can be defined, like routes or specific components (in the metadata `providers` option), not just in the application config.

However, other methods are inaccessible. This approach is really good for making things private while not directly owning the code that defines them, as is the case with third-party APIs.

Finally, we arrive at the most important and interesting piece of this puzzle, and that is providing a dependency dynamically, through the `useFactory` option. This option allows us to define a function that will be called when the dependency is requested, and it will return the instance which will be determined programmatically. For instance, a very basic example of this would be to determine which service to use depending on an environment.

For example, we might have several different logging services; the one used in local development should just log messages to the console, while the one used in production should log to a third-party service. We can create a factory function that will return the correct service based on the environment:

```
import { environment } from './environments/environment';

export const appConfig: ApplicationConfig = {
    providers: [
        {
            provide: LoggerService,
            useFactory: () => {
                if (environment.production) {
                    return new ThirdPartyLoggerService();
                }

                return new ConsoleLoggerService();
            },
        },
    ],
};
```

TypeScript

And then, we can simply inject the logger service anywhere in our application:

```
@Injectable()
export class SomeService {
    private readonly logger = inject(LoggerService);

    getData() {
        this.logger.log('Some data');
    }
}
```

TypeScript

> \[!WARNING\] We should be careful to make the different implementation of the same service to have the same methods, for instance, through defining an interface and having both services implement it.

Now, as we are familiar with all options, we can further dive into the `useFactory` pattern and discover some scenarios that might even sound crazy to us at first!

### Dynamic dependencies with query parameters?!

When writing Angular apps, we are always careful to notice some "static" (for the lack of a better word) things like services and providers, and "dynamic" things like component state, routing data (like query parameters), and so on.

Usually, we think of those as two separate worlds - services get provided and configured when the the app starts, and then components get injected with the services and data they need. But what if I told you we can actually provide services dynamically, based on, say, query parameters?

Let's review the following scenario. We have an app to show financial transactions, of which we have expenses and incomes. While the two are related, there are some internal concerns of how a service working with an expense should behave differently than one working with an income. Both services, however, have the same interface, and, furthermore, both the expenses and income components have absolutely the same UI. So, for us, it would make sense to have two services, but only one component, but determine which one to use based on a, for instance, query parameter.

Let's see this in action. First, we need an interface that both services will strictly implement:

```
export abstract class TransactionService {
    abstract getTransactions(): Observable<Transaction[]>;
    abstract addTransaction(transaction: Transaction): void;
    abstract deleteTransaction(id: number): void;
}
```

TypeScript

> \[!NOTE\] We are using an abstract class instead of an interface because interfaces get removed when TypeScript compiles the code, so it cannot be used as a DI token. Abstract classes, on the other hand, are not removed, and can be used as a DI token, and also implemented like an interface, as we are going to do in this example.

Now, we can have two services, one for expenses and one for incomes:

```
@Injectable()
export class ExpensesService implements TransactionService {
    private readonly http = inject(HttpClient);

    getTransactions() {
        return this.http.get<Transaction[]>('/api/transactions');
    }

    addTransaction(transaction: Transaction) {
        this.http.post('/api/transactions', transaction);
    }

    deleteTransaction(id: number) {
        this.http.delete(`/api/transactions/${id}`);
    }
}
```

TypeScript

```
@Injectable()
export class IncomeService implements TransactionService {
    private readonly http = inject(HttpClient);

    getTransactions() {
        return this.http.get<Transaction[]>('/api/transactions/income');
    }

    addTransaction(transaction: Transaction) {
        this.http.post('/api/transactions/income', transaction);
    }

    deleteTransaction(id: number) {
        this.http.delete(`/api/transactions/income/${id}`);
    }
}
```

TypeScript

Now, all of this has been fairly simple, but how do we then provide the correct one for a specific component, and based on a query parameter no less? Turns out, factories can help us here massively.

```
@Component({
    providers: [
        {
            provide: TransactionService,
            useFactory: (route: ActivatedRoute) => {
                switch (route.snapshot.queryParamMap.get('type')) {
                    case 'income':
                        return new IncomeService();
                    case 'expense':
                        return new ExpensesService();
                    default:
                        throw new Error('Invalid query parameter');
                }
            },
            deps: [ActivatedRoute],
        }
    ],
})
export class TransactionsComponent {
    private readonly transactionService = inject(TransactionService);

    addTransaction(transaction: Transaction) {
        this.transactionService.addTransaction(transaction);
    }
}
```

TypeScript

As you can see, we are using a factory function that will be called when the component is created. The component then injects the `TransactionService` abstract class, which is guaranteed to have the same interface as the two services we created. So, based on the query parameter we get, we can provide the correct service to the component.

Now, this gives us a fantastic level of flexibility here. Now, next, let's tackle an issue that lots of people do not realized is essentially fixable with DI, and that is sharing complex data structures between components.

### Sharing a form instance from parent to child?

Imagine we have a large form that we want to split into multiple components. For instance, we might have a registration form that asks for many fields (first name, last name, email, etc.), but also contains a nested form for the address, with multiple other fields (street, city, zip code, etc.). Our template and component get too big, and we think (rightfully so) that it is a good idea to split the registration component into two, one for the form itself, and one for the address form.

Now, we have a problem to solve; we want the child component be as lean as possible, and the parent to handle all the logic, including the definition of the form. Let's imagine the parent component first:

```
@Component({...})
export class RegistrationComponent {
    private readonly form = new FormGroup({
        firstName: new FormControl(),
        lastName: new FormControl(),
        email: new FormControl(),
        address: new FormGroup({
            street: new FormControl(),
            city: new FormControl(),
            zipCode: new FormControl(),
        }),
    });

    onSubmit() {
        // submit the form
    }
}
```

TypeScript

Now, how do we send the `this.form.controls.address` to the child component? Well, the most basic way we can achieve this is by creating an input:

```
@Component({...})
export class AddressComponent {
    form = input.required<FormGroup>();
}
```

TypeScript

This solves the problem in principle, however, there are some issues with this approach. For instance, the `form` in the `AddressComponent` is not strongly typed, and to achieve this, we have to create a separate type definition for the form, moving away from an inferred type, which makes it less maintainable. Also, using an input means introducing all the problems that inputs can have: potential race conditions, added complexity, and so on. So, what can we do instead? We can create a token that will be used to retrieve the form as a whole, which then both components can inject and use:

```
export function createRegistrationForm(): FormGroup {
    return new FormGroup({
        firstName: new FormControl(),
        lastName: new FormControl(),
        email: new FormControl(),
        address: new FormGroup({
            street: new FormControl(),
            city: new FormControl(),
            zipCode: new FormControl(),
        }),
    });
}
export const AddressForm = new InjectionToken<FormGroup<ReturnType<typeof createRegistrationForm>>>('AddressForm');
```

TypeScript

And then, we can simply inject the token in both components:

```
@Component({...})
export class RegistrationComponent {
    private readonly form = inject(AddressForm);

    onSubmit() {
        // submit the form
    }
}
```

TypeScript

```
@Component({...})
export class AddressComponent {
    form = inject(AddressForm).controls.address;
}
```

TypeScript

This is a much better approach, and it is also more flexible. There is also another way to do this. If we are 100% sure that the address form will only ever be used inside the registration component, we can simply define the form in the parent component, and then use hierarchical DI, which we discussed earlier, to inject the parent component into child and access the form:

```
@Component({...})
export class AddressComponent {
    form = inject(RegistrationComponent).form.controls.address;
}
```

TypeScript

However, as this is a very specific scenario, this should be used with caution, on a case-by-case basis, as to not confuse anyone wo tries to read the `AddressComponent` code.

Now, on to our last example. Here, we will explore the capability of providing global configurations than can, in fact, be overridden by the developer.

### Providing global configuration

Imagine we are writing a reusable component, for instance, one that is showing an overlay with a loading indicator. We use this overlay all over our application, and usually, we also want a text saying "Loading..." under the spinning icon. However, in 1-2 cases, we might want a different text. Of course, we can simply create an input with a default value:

```
@Component({...})
export class LoadingComponent {
    text = input('Loading...');
}
```

TypeScript

This is mostly enough. However, if we want the component to be a part of a library that other developers might use, this can become an issue, because other apps might want a slightly different text (or maybe another language). This becomes even more evident if we are using some sort of a monorepo solution like Nx, where we have multiple apps that depend on this same library, but might want a slightly different configuration.

So, what can we do about this? The solution is to use DI in couple with a `optional` lookup configuration:

```
export const LoadingText = new InjectionToken<string>('LoadingText');

@Component({...})
export class LoadingComponent {
    text = input<string>(inject(LoadingText, { optional: true }) ?? '');
}
```

TypeScript

Now, any consumer of the `LoadingComponent` can simply provide the text they want to use as default:

```
export const appConfig: ApplicationConfig = {
    providers: [
        {provide: LoadingText, useValue: 'Some other loading text...'}, 
    ],
};
```

TypeScript

And this will be used to override the default value of the input. This won't affect the situations where we provide a custom text via the component input:

```
<app-loading text="Yet another loading text...">
    Content
</app-loading>
```

HTML

Here, we are using the `optional` lookup modifier to ensure Angular does not throw an error if the token was not provided by the developer. Instead, in this case, the component will rely on the provided input value.

## Conclusion

Dependency Injection in Angular is, as the title of this article suggests, truly fascinating. In this article, we managed to cover some slightly unconventional scenarios that might be fixed clearly with DI, but we have only touched the tip of the iceberg here. Dependency injection is powerful, but underutilized, and with this article, I hope to help Angular developers understand and use it more effectively, as it can really be a huge time saver in large applications.

![Modern Angular.jpeg](https://storage.ghost.io/c/3f/63/3f6333b8-1f83-4017-8426-91bfbc264d81/content/images/2024/09/Modern-Angular.jpeg)

You might have noticed this article is using signal inputs and the `inejct` function only. The recent upheaval in Angular has caused many developers to be confused about what solutions to chose, how to implement them, and how to migrate their existing codebases to the most recent features. Thankfully, I have a response to this concern: very soon, my very first book is going into print!

It is called "Modern Angular" and it is a comprehensive guide to all the new amazing features we got in recent versions (v14-v18), including standalone, improved inputs, signals (of course!), better RxJS interoperability, SSR, and much more. If this interested you, you can find it [here](https://www.manning.com/books/modern-angular?ref=angularspace.com). The book is now in the copy-editing phase with a release scheduled shortly, so it is currently in Early Access, with all the 10 chapters already available online. If you want to keep yourself updated on the print release, you can follow me on [Twitter](https://twitter.com/Armandotrue?ref=angularspace.com) or [LinkedIn](https://www.linkedin.com/in/armen-vardanyan-am/?ref=angularspace.com), where I will be posting whenever there are news or promotions available.

P.S. Hey! Check out chapter 3 of my book to uncover more in-depth insights about dependency injection ;)

* * *

![](https://storage.ghost.io/c/3f/63/3f6333b8-1f83-4017-8426-91bfbc264d81/content/images/2024/09/Screenshot-2024-09-20-at-16.10.33.png)

**Last Update:** September 20, 2024
