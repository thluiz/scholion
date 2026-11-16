---
url: "https://ckeditor.com/blog/Aborting-a-signal-how-to-cancel-an-asynchronous-task-in-JavaScript"
captured_at: "2026-11-16T04:29:06+00:00"
title: "Aborting a signal: How to cancel an asynchronous task in JavaScript"
domain: "ckeditor-com"
---

Performing asynchronous tasks can be hard, especially when a particular programming language does not allow for canceling mistakenly started or no longer needed actions. Fortunately, JavaScript offers a very handy piece of functionality for aborting an asynchronous activity. In this article, you can learn how to use it to create your own cancel async function.

## Abort signal

The [need to cancel asynchronous tasks emerged](https://github.com/whatwg/fetch/issues/27) shortly after introducing `Promise` into ES2015 and the appearance of several Web APIs supporting the new asynchronous solution. The first attempt focused on [creating a universal solution](https://github.com/tc39/proposal-cancellation) that could later become a part of the ECMAScript standard. However, discussions quickly became stuck without solving the problem. Due to that WHATWG prepared their own solution and [introduced it directly into the DOM in the form of `AbortController`](https://dom.spec.whatwg.org/#aborting-ongoing-activities). The obvious downside of such resolution is the fact that `AbortController` is not available in Node.js, leaving this environment without any elegant or official way to cancel asynchronous tasks.

As you can see in the DOM specification, `AbortController` is described in a very general way. Thanks to this you can use it in any kind of asynchronous APIs — even ones that do not exist yet. At the moment only Fetch API officially supports it, but nothing stops you from using it inside your own code!

But before jumping to it, let us spend a moment analyzing how `AbortController` works:

```
const abortController = new AbortController(); // 1
const abortSignal = abortController.signal; // 2

fetch( 'http://example.com', {
  signal: abortSignal // 3
} ).catch( ( { message } ) => { // 5
  console.log( message );
} );

abortController.abort(); // 4
```

Looking at the code above you can see that at the beginning, you create a new instance of the `AbortController` DOM interface (1) and bind its `signal` property to a variable (2). Then you invoke `fetch()` and pass `signal` as one of its options (3). To abort fetching the resource you just call `abortController.abort()` (4). It will automatically reject the promise of `fetch()` and the control will be passed to the `catch()` block (5).

The `signal` property itself is quite interesting and it is the main star of this show. The property is an instance of the [`AbortSignal` DOM interface](https://dom.spec.whatwg.org/#interface-AbortSignal) that has an `aborted` property with information whether the user has already invoked the `abortController.abort()` method. You can also bind the `abort` event listener to it that will be called when `abortController.abort()` is called. In other words: `AbortController` is just a public interface of `AbortSignal`.

## Abortable function

Let us imagine that you have an asynchronous function that does some very complicated calculations (for example, [it asynchronously processes data from a big array](https://humanwhocodes.com/blog/2009/08/11/timed-array-processing-in-javascript/)). To keep it simple, the sample function will be simulating the hard work by waiting five seconds before returning the result:

```
function calculate() {
  return new Promise( ( resolve, reject ) => {
    setTimeout( ()=> {
      resolve( 1 );
    }, 5000 );
  } );
}

calculate().then( ( result ) => {
  console.log( result );
} );
```

However, sometimes the user would want to abort such a costly operation. And rightly so — they should have such an ability. Add a button that will start and stop the calculation:

```
<button id="calculate">Calculate</button>

<script type="module">
  document.querySelector( '#calculate' ).addEventListener( 'click', async ( { target } ) => { // 1
    target.innerText = 'Stop calculation';

    const result = await calculate(); // 2

    alert( result ); // 3

    target.innerText = 'Calculate';
  } );

  function calculate() {
    return new Promise( ( resolve, reject ) => {
      setTimeout( ()=> {
        resolve( 1 );
      }, 5000 );
    } );
  }
</script>
```

In the code above you add an asynchronous `click` event listener to the button (1) and call the `calculate()` function inside it (2). After five seconds the alert dialog with the result will appear (3). Additionally, `script[type=module]` is used to force JavaScript code into strict mode — as it is more elegant than the `'use strict'` pragma.

Now add the ability to abort an asynchronous task:

```
{ // 1
  let abortController = null; // 2

  document.querySelector( '#calculate' ).addEventListener( 'click', async ( { target } ) => {
    if ( abortController ) {
      abortController.abort(); // 5

      abortController = null;
      target.innerText = 'Calculate';

      return;
    }

    abortController = new AbortController(); // 3
    target.innerText = 'Stop calculation';

    try {
      const result = await calculate( abortController.signal ); // 4

      alert( result );
    } catch {
      alert( 'WHY DID YOU DO THAT?!' ); // 9
    } finally { // 10
      abortController = null;
      target.innerText = 'Calculate';
    }
  } );

  function calculate( abortSignal ) {
    return new Promise( ( resolve, reject ) => {
      const timeout = setTimeout( ()=> {
        resolve( 1 );
      }, 5000 );

      abortSignal.addEventListener( 'abort', () => { // 6
        const error = new DOMException( 'Calculation aborted by the user', 'AbortError' );

        clearTimeout( timeout ); // 7
        reject( error ); // 8
      } );
    } );
  }
}
```

As you can see, the code has become much longer. But there is no reason to panic — it has not become much harder to understand!

Everything is enclosed inside the block (1), which is an [equivalent of IIFE](https://exploringjs.com/es6/ch_core-features.html#sec_from-iifes-to-blocks). Thanks to this, the `abortController` variable (2) will not leak into the global scope.

At first, you set its value to `null`. This value changes at the mouse click on the button. Then you set its value to a new instance of `AbortController` (3). After that, you pass the instance’s `signal` property directly to your `calculate()` function (4).

If the user clicks the button again before five seconds elapsed, it will cause the invocation of the `abortController.abort()` function (5). This, in turn, will fire the `abort` event on the `AbortSignal` instance you passed earlier to `calculate()` (6).

Inside the `abort` event listener you remove the ticking timer (7) and reject the promise with an appropriate error (8; [according to the specification](https://dom.spec.whatwg.org/#abortcontroller-api-integration) it must be a `DOMException` with an `'AbortError'` type). The error eventually passes control to `catch` (9) and `finally` blocks (10).

You should also prepare your code to handle a situation like this:

```
const abortController = new AbortController();

abortController.abort();
calculate( abortController.signal );
```

In such case, the `abort` event will not be fired because it happened _before_ passing the signal to the `calculate()` function. Due to this, you should refactor it a little:

```
function calculate( abortSignal ) {
  return new Promise( ( resolve, reject ) => {
    const error = new DOMException( 'Calculation aborted by the user', 'AbortError' ); // 1

    if ( abortSignal.aborted ) { // 2
      return reject( error );
    }

    const timeout = setTimeout( ()=> {
      resolve( 1 );
    }, 5000 );

    abortSignal.addEventListener( 'abort', () => {
      clearTimeout( timeout );
      reject( error );
    } );
  } );
}
```

The error was moved to the top (1). Thanks to this, you can reuse it in two different parts of the code (yet it would be more elegant to just create a factory of errors, however silly it sounds). Additionally, a guard clause appeared, checking the value of `abortSignal.aborted` (2). If it equals `true`, the `calculate()` function rejects the promise with an appropriate error without doing anything further.

And this is how you can create a fully abortable async function. The [demo is available online](https://blog.comandeer.pl/assets/i-ciecie/). Enjoy!

See other How to articles:

*   [Middleware-based clipboard handling - meet clipboar](https://ckeditor.com/blog/Middleware-based-clipboard-handling-meet-clipboar/ "Middleware-based clipboard handling - meet clipboar")
*   [The best way to export your WYSIWYG editor content to PDF and Word](https://ckeditor.com/blog/The-best-way-to-export-your-WYSIWYG-editor-content-to-PDF-and-Word-file-formats/ "The best way to export your WYSIWYG editor content to PDF and Word")
*   [Swinging on an AST branch](https://ckeditor.com/blog/Swinging-on-an-AST-branch/ "Swinging on an AST branch")
*   [How to detect human faces (and other shapes) in JavaScript](https://ckeditor.com/blog/How-to-detect-human-faces-and-other-shapes-in-JavaScript/ "How to detect human faces (and other shapes) in JavaScript")
*   [HTML in Node.js](https://ckeditor.com/blog/html-in-node-js/ "HTML in Node.js")
*   [Implementing single-file Web Components](https://ckeditor.com/blog/implementing-single-file-web-components/ "Implementing single-file Web Components")
