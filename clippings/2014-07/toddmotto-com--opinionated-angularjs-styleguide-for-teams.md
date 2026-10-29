---
url: "http://toddmotto.com/opinionated-angular-js-styleguide-for-teams/?utm_source=javascriptweekly&utm_medium=email"
captured_at: "2014-07-30T11:40:26-03:00"
title: "Opinionated AngularJS styleguide for teams"
domain: "toddmotto-com"
---

# Opinionated AngularJS styleguide for teams

[Edit this page on GitHub](http://github.com/toddmotto/toddmotto.github.io/blob/master/_posts/2014-07-23-opinionated-angular-js-styleguide-for-teams.md)

July 23, 2014

##### Official styleguide repo [now on GitHub](http://github.com/toddmotto/angularjs-styleguide), all future styleguide updates will be here!

After reading [Google's AngularJS guidelines](http://google-styleguide.googlecode.com/svn/trunk/angularjs-google-style.html), I felt they were a little too incomplete and also guided towards using the Closure library. They [also state](http://blog.angularjs.org/2014/02/an-angularjs-style-guide-and-best.html) *"We don't think this makes sense for all projects that use AngularJS, and we'd love to see our community of developers come up with a more general Style that's applicable to AngularJS projects large and small"*, so here goes.

From my experience with Angular, [several talks](http://speakerdeck.com/toddmotto) and working in teams, here's my opinionated styleguide for syntax, building and structuring Angular applications.

### Module definitions

Angular modules can be declared in various ways, either stored in a variable or using the getter syntax. Use the getter syntax at all times ([angular recommended](http://docs.angularjs.org/guide/module)).

```
   angularmodule'app' 
controller
factory
```

###### Good:

```
angular
  module'app' 
  controller
  factory
```

From these modules we can pass in function references.

### Module method functions

Angular modules have a lot of methods, such as `controller`, `factory`, `directive`, `service` and more. There are many syntaxes for these modules when it comes to dependency injection and formatting your code. Use a named function definition and pass it into the relevant module method, this aids in stack traces as functions aren't anonymous (this could be solved by naming the anonymous function but this method is far cleaner).

```
   angularmodule'app' 
controller'MyCtrl' function
```

###### Good:

```
function MainCtrl  
  

angular
  module'app' 
  controller'MainCtrl' MainCtrl
```

Define a module once using `angular.module('app', [])` setter, then use the `angular.module('app')` getter elsewhere (such as other files).

To avoid polluting the global namespace, wrap all your functions during *compilation/concatenation* inside an IIFE which will produce something like this:

###### Best:

```
function  
  angularmodule'app' 
  
  // MainCtrl.js
  function MainCtrl  
  
  
  
  angular
    module'app'
    controller'MainCtrl' MainCtrl
    
  // AnotherCtrl.js
  function AnotherCtrl  
  
  
  
  angular
    module'app'
    controller'AnotherCtrl' AnotherCtrl
    
  // and so on...
    
})();
```

### Controllers

Controllers are classes and can use a `controllerAs` syntax or generic `controller` syntax. Use the `controllerAs` syntax always as it aids in nested scoping and controller instance reference.

##### controllerAs DOM bindings

```
<div ng-controller="MainCtrl"
  {{ someObject }}
</div>
```

###### Good:

```
<div ng-controller="MainCtrl as main"
  {{ main.someObject }}
</div>
```

Binding these `ng-controller` attributes couples the declarations tightly with our DOM, and also means we can only use that controller for that specific view (there are rare cases we might use the same view with different controllers). Use the router to couple the controller declarations with the relevant views by telling each `route` what controller to instantiate.

###### Best:

```
<!-- main.html -->
<div>
  {{ main.someObject }}
</div>
<!-- main.html -->

<script>
// ...
function config $routeProvider 
  $routeProvider
   
    templateUrl 'views/main.html'
    controller 'MainCtrl'
    controllerAs 'main'
  

angular
  module'app'
  configconfig
//...
</script>
```

This avoids using `$parent` to access any parent controllers from a child controller, simple hit the `main` reference and you've got it. This could avoid things such as `$parent.$parent` calls.

##### controllerAs this keyword

The `controllerAs` syntax uses the `this` keyword inside controllers instead of `$scope`. When using `controllerAs`, the controller is infact *bound* to `$scope`, there is a degree of separation.

```
function MainCtrl $scope 
  $scopesomeObject  
  $scopedoSomething  function  
  
  

angular
  module'app'
  controller'MainCtrl' MainCtrl
```

You can also use the `prototype` Object to create controller classes, but this becomes messy very quickly as each dependency injected provider needs a reference bound to the `constructor` Object.

###### Bad and Good:

Good for inheritance, bad (verbose) for general use.

```
function MainCtrl $scope 
  someObject  
  _$scope  $scope

MainCtrlprototypedoSomething  function  
  // use this._$scope

angular
  module'app'
  controller'MainCtrl' MainCtrl
```

If you're using `prototype` and don't know why, then it's bad. If you are using `prototype` to inherit from other controllers, then that's good. For general use, the `prototype` pattern can be verbose.

###### Good:

```
function MainCtrl  
  someObject  
  doSomething  function  
  
  

angular
  module'app'
  controller'MainCtrl' MainCtrl
```

These just show examples of Objects/functions inside Controllers, however we don't want to put logic in controllers...

##### Avoid controller logic

Avoid writing logic in Controllers, delegate to Factories/Services.

```
function MainCtrl  
  doSomething  function  

  

angular
  module'app'
  controller'MainCtrl' MainCtrl
```

###### Good:

```
function MainCtrl SomeService 
  doSomething  SomeServicedoSomething

angular
  module'app'
  controller'MainCtrl' MainCtrl
```

This maximises reusability, encapsulated functionality and makes testing far easier and persistent.

### Services

Services are instantiated and should be class-like also and reference the `this` keyword, keep function style consistent with everything else.

###### Good:

```
function SomeService  
  someMethod  function  

  

angular
  module'app'
  service'SomeService' SomeService
```

### Factory

Factories give us a singleton module for creating service methods (such as communicating with a server over REST endpoints). Creating and returning a bound Object keeps controller bindings up to date and avoids pitfalls of binding primitive values.

Important: A "factory" is in fact a pattern/implementation, and shouldn't be part of the provider's name. All factories and services should be called "services".

```
function AnotherService  

   someValue  

   someMethod  function  

  
  
  return 
    someValue someValue
    someMethod someMethod
  

angular
  module'app'
  factory'AnotherService' AnotherService
```

###### Good:

We create an Object with the same name inside the function. This can aid documentation as well for comment-generated docs.

```
function AnotherService  

   AnotherService  
  
  AnotherServicesomeValue  

  AnotherServicesomeMethod  function  

  
  
  return AnotherService

angular
  module'app'
  factory'AnotherService' AnotherService
```

Any bindings to primitives are kept up to date, and it makes internal module namespacing a little easier, we can easily see any private methods and variables.

### Directives

Any DOM manipulation should take place inside a directive, and only directives. Any code reusability should be encapsulated (behavioural and markup related) too.

##### DOM manipulation

DOM manipulation should be done inside the `link` method of a directive.

```
// do not use a controller
function MainCtrl SomeService 

  makeActive  function  
    addClass'test'
  

angular
  module'app'
  controller'MainCtrl' MainCtrl
```

###### Good:

```
// use a directive
function SomeDirective SomeService 
  return 
    restrict 
    template 
      '<a href="" class="myawesomebutton" ng-transclude>'
        '<i class="icon-ok-sign"></i>'
      '</a>'
    
     function $scope $element $attrs 
      // DOM manipulation/events here!
      $element'click' function  
        addClass'test'
      
    
  

angular
  module'app'
  directive'SomeDirective' SomeDirective
```

Any DOM manipulation should take place inside a directive, and only directives. Any code reusability should be encapsulated (behavioural and markup related) too.

##### Naming conventions

Custom directives should *not* be `ng-*` prefixed to prevent future core overrides if your directive name happens to land in Angular (such as when `ng-focus` landed, there were many custom directives called this beforehand). It also makes it more confusing to know which are core directives and which are custom.

```
function ngFocus SomeService 

  return 

angular
  module'app'
  directive'ngFocus' ngFocus
```

###### Good:

```
function focusFire SomeService 

  return 

angular
  module'app'
  directive'focusFire' focusFire
```

Directives are the *only* providers that we have the first letter as lowercase, this is due to strict naming conventions in the way Angular translates `camelCase` to hyphenated, so `focusFire` will become `<input focus-fire>` when used on an element.

##### Usage restriction

If you need to support IE8, you'll want to avoid using the comments syntax for declaring where a directive will sit. Really, this syntax should be avoided anyway - there are no real benefits of using it - it just adds confusion of what is a comment and what isn't.

These are terribly confusing.

```
<!-- directive: my-directive -->
<div class="my-directive"></div>
```

###### Good:

Declarative custom elements and attributes are clearest.

```
<my-directive></my-directive>
<div my-directive></div>
```

You can restrict usage using the `restrict` property inside each directive's Object. Use `E` for `element`, `A` for `attribute`, `M` for `comment` (avoid) and `C` for `className` (avoid this too as it's even more confusing, but plays better with IE). You can have multiple restrictions, such as `restrict: 'EA'`.

### Resolve promises in router, defer controllers

After creating services, we will likely inject them into a controller, call them and bind any new data that comes in. This becomes problematic of keeping controllers tidy and resolving the right data.

Thankfully, using `angular-route.js` (or a third party such as `ui-router.js`) we can use a `resolve` property to resolve the next view's promises before the page is served to us. This means our controllers are instantiated when all data is available, which means zero function calls.

```
function MainCtrl SomeService 

     

  // unresolved
  something

  // resolved asynchronously
  SomeServicedoSomethingfunction response 
    something  response
  

angular
  module'app'
  controller'MainCtrl' MainCtrl
```

###### Good:

```
function config $routeProvider 
  $routeProvider
   
    templateUrl 'views/main.html'
    resolve 
      doSomething function SomeService 
        return SomeServicedoSomething
      
    
  

angular
  module'app'
  configconfig
```

At this point, our service will internally bind the response of the promise to another Object which we can reference in our "deferred-instantiated" controller:

###### Good:

```
function MainCtrl SomeService 
  // resolved!
  something  SomeServicesomething

angular
  module'app'
  controller'MainCtrl' MainCtrl
```

We can go one better, however and create a `resolve` property on our own Controllers to couple the resolves with the Controllers and avoid logic in the router.

###### Best:

```
// config with resolve pointing to relevant controller
function config $routeProvider 
  $routeProvider
   
    templateUrl 'views/main.html'
    controller 'MainCtrl'
    controllerAs 'main'
    resolve MainCtrlresolve
  

// controller as usual
function MainCtrl SomeService 
  // resolved!
  something  SomeServicesomething

// create the resolved property
MainCtrlresolve  
  doSomething function SomeService 
    return SomeServicedoSomething
  

angular
  module'app'
  controller'MainCtrl' MainCtrl
  configconfig
```

##### Route changes and ajax spinners

While the routes are being resolved we want to show the user something to indicate progress. Angular will fire the `$routeChangeStart` event as we navigate away from the page, which we can show some form of loading and ajax spinner, which can then be removed on the `$routeChangeSuccess` event ([see docs](https://docs.angularjs.org/api/ngRoute/service/$route)).

### Avoid $scope.$watch

Using `$scope.$watch` should be avoided unless there are no others options. It's less performant than binding an expression to something like `ng-change`, a list of supported events are in the Angular docs.

```
<input ng-model="myModel"
<script>
$scope$watch'myModel' callback
</script>
```

###### Good:

```
<input ng-model="myModel" ng-change="callback"
<!--
  $scope.callback = function () {

-->
```

### Project/file structure

One role, one file, rule. Separate all controllers, services/factories, directives into individual files. Don't add all controllers in one file, you will end up with a huge file that is very difficult to navigate, keeps things encapsulated and bitesize.

```
|-- app.js
|-- controllers.js
|-- filters.js
|-- services.js
|-- directives.js
```

Keep naming conventions for files consistent, don't invent fancy names for things, you'll just forget them.

###### Good:

```
|-- app.js
|-- controllers/
|   |-- MainCtrl.js
|   |-- AnotherCtrl.js
|-- filters/
|   |-- MainFilter.js
|   |-- AnotherFilter.js
|-- services/
|   |-- MainService.js
|   |-- AnotherService.js
|-- directives/
|   |-- MainDirective.js
|   |-- AnotherDirective.js
```

Depending on the size of your code base, a "feature-driven" approach may be better to split into functionality chunks.

###### Good:

```
|-- app.js
|-- dashboard/
|   |-- DashboardService.js
|   |-- DashboardCtrl.js
|-- login/
|   |-- LoginService.js
|   |-- LoginCtrl.js
|-- inbox/
|   |-- InboxService.js
|   |-- InboxCtrl.js
```

### Naming conventions and conflicts

Angular provides us many Objects such as `$scope` and `$rootScope` that are prefixed with `$`. This incites they're public and can be used. We also get shipped with things such as `$$listeners`, which are available on the Object but are considered private methods.

Avoid using `$` or `$$` when creating your own services/directives/providers/factories.

Here we create `$$SomeService` as the definition, not the function name.

```
function SomeService  

angular
  module'app'
  factory'$$SomeService' SomeService
```

###### Good:

Here we create `SomeService` as the definition, *and* the function name for consistency/stack traces.

```
function SomeService  

angular
  module'app'
  factory'SomeService' SomeService
```

### Minification and annotation

##### Annotation order

It's considered good practice to dependency inject Angular's providers in before our own custom ones.

```
// randomly ordered dependencies
function SomeCtrl MyService $scope AnotherService $rootScope
```

###### Good:

```
// ordered Angular -> custom
function SomeCtrl $scope $rootScope MyService AnotherService
```

##### Minification methods, automate it

Use `ng-annotate` for automated dependency injection annotation, as `ng-min` is [deprecated](https://github.com/btford/ngmin). You can find `ng-annotate` [here](https://github.com/olov/ng-annotate).

With our function declarations outside of the module references, we need to use the `@ngInject` comment to explicitly tell `ng-annotate` where to inject our dependencies. This method uses `$inject` which is faster than the Array syntax.

Manually specifiying the dependency injection arrays costs too much time.

```
function SomeService $scope 

// manually declaring is time wasting
SomeService$inject  '$scope'
angular
  module'app'
  factory'SomeService' SomeService
```

###### Good:

Using the `ng-annotate` keyword `@ngInject` to instruct things that need annotating:

```
 * @ngInject

function SomeService $scope 

angular
  module'app'
  factory'SomeService' SomeService
```

Will produce:

```
 * @ngInject

function SomeService $scope 

// automated
SomeService$inject  '$scope'
angular
  module'app'
  factory'SomeService' SomeService
```
