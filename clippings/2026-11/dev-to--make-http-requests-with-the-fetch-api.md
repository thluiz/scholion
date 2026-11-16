---
url: "https://dev.to/aumayeung/make-http-requests-with-the-fetch-api-mmk"
captured_at: "2026-11-16T01:46:51+00:00"
title: "Make HTTP Requests with the Fetch API"
domain: "dev-to"
---

**Subscribe to my email list now at [http://jauyeung.net/subscribe/](http://jauyeung.net/subscribe/)**

**Follow me on Twitter at [https://twitter.com/AuMayeung](https://twitter.com/AuMayeung)**

**Many more articles at [https://medium.com/@hohanga](https://medium.com/@hohanga)**

**Even more articles at [http://thewebdev.info/](http://thewebdev.info/)**

Before the Fetch API, HTTP requests were made with the `XmlHttpRequest` object. It’s more difficult to use and it’s not promised based since it was added before promises were built into JavaScript.

Now, we can use the Fetch API to make HTTP requests much more easily.

With it, we have a generic definition of `Request` and `Response` objects along with other things for network requests. This allows them to be used whenever they’re needed in the future.

It also provides a definition for related concepts such as CORS and HTTP origin header semantics, replacing existing definitions of them elsewhere.

In this article, we’ll look at how to make client-side HTTP requests with the Fetch API.

## [](#making-http-requests)Making HTTP Requests

Making HTTP requests starts by using the `fetch` method. It takes one mandatory argument, which is the path to the resource which we want to fetch.

It returns a promise that resolves to the `Response` to that request, whether it’s successful or not. We can optionally pass in an `init` options object as the argument.

Once the `Response` is retrieved, there’re a number of methods to define what body content is and how it should be handled.

The promise returned by `fetch` won’t reject HTTP error status even if the response is 404 or 500. It’ll resolve normally with `ok` status set to `false`.

`fetch` won’t receive cross-site cookies. There’s no way to establish a cross-site session using `fetch`.

`fetch` won’t send cookies unless we set the credentials init option.

We can call the `fetch` method as follows:  

```
(async () => {  
  const response = await fetch('https://jsonplaceholder.typicode.com/todos/1')  
  const json = await response.json();  
  console.log(json);  
})();
```

The code above gets makes a GET request with `fetch` and then converts it to a JavaScript object with the `json()` method of the `Response` object. Then we can log it in the `console.log` .

This is the simplest case for an HTTP request. We can also add more options in the second argument. We can set the following options:

*   `method` — request method
*   `headers` — request headers that we want to add
*   `body` — request body. It can be `Blob`, `BufferSource`, `FormData`, `URLSearchParams`, `USVString`, or `ReadableStream` object. GET or HEAD requests can’t have a body.
*   `mode` — mode for the request. It can be`cors`, `no-cors`, or `same-origin`
*   `credentials` — request credentials we want to use for the requests. Possible values are `omit`, `same-origin`, or `include` . This option must be provided to automatically send cookies for the current domain. Starting with Chrome 50, this property also takes a `FederatedCredential` instance or a `PasswordCredential` instance.
*   `cache` — cache mode we want to use for the request
*   `redirect` — redirect mode to use. Set this to `follow` for automatically follows redirects, `error` to abort with an error if a redirect occurs, or `manual` to handle redirects manually
*   `referrer` — a string specifying `no-referrer`, `client`, or a URL. Default value is `client`
*   `referrerPolicy` — specifies the value of the referrer HTTP header. Can be one of `no-referrer`, `no-referrer-when-downgrade`, `origin`, `origin-when-cross-origin`, `unsafe-url`
*   `integrity` — subresource integrity value of the request
*   `keepalive` — set this optional to allow the request to outlive the page
*   `signal` — an `AbortSignal` object instance to let us communicate with a fetch request and abort it via an `AbortController` .

For example, we can make a basic POST request by writing:  

```
(async () => {  
  const response = await fetch('https://jsonplaceholder.typicode.com/posts', {  
    method: 'POST',  
    body: JSON.stringify({  
      title: 'title',  
      body: 'body',  
      userId: 1  
    }),  
    headers: {  
      "Content-type": "application/json; charset=UTF-8"  
    }  
  })  
  const json = await response.json();  
  console.log(json);  
})();
```

We set all the options in the object of the second argument, including the body and headers.

To upload a file, we can get the file from a file input. Given that we have it in the HTML:  

```
<input type='file' id='file-input'>
```

Then we can write the following to watch for changes in the value of the file input and upload the file to the server:  

```
const upload = async (file) => {  
  const response = await fetch('https://jsonplaceholder.typicode.com/posts', {  
    method: 'POST',  
    body: file,  
    headers: {  
      'Content-Type': 'multipart/form-data'  
    }  
  })  
  const json = await response.json();  
  console.log(json);  
};

const input = document.getElementById('file-input');  
input.addEventListener('change', () => {  
  upload(input.files[0]);  
}, false);
```

Note that the header may change depending on the server we use. The general idea is that we get the file from the input and then send it in the body of the request.

## [](#manipulating-the-response)Manipulating the Response

The `Response` has a few properties for getting data and manipulating it. We can use the `error` method to get the error, `redirect` method creates a new response with a different URL.

The `Body` object, which the `Response` object implements have the `formData` method for reading `FormData` responses. Likewise, there’s the `json` method for reading JSON responses and `text` for reading plain text. They all resolve to promises with the corresponding objects. `arrayBuffer` method will read binary data and resolves to an `ArrayBuffer` . `blob` method reads binary data and resolves it to a `Blob` .

Value properties that may be useful to us include `headers` to get the response headers, `ok` to check if the request was successful, `redirect` to check whether redirect happened. `status` is the response status code, `statusText` has the text that corresponds to the status code. `url` has the response URL, `body` has the response body.

The Fetch API is much better than `XmlHttpRequest` for making HTTP requests. It lets us make most kinds of requests, and it’s promise based so that they can be run sequentially with other promises.

It supports both text and binary bodies. Now we don’t need a third-party HTTP client to make client-side HTTP requests.

`Request` and `Response` objects are also standardized so that they can used with other APIs.
