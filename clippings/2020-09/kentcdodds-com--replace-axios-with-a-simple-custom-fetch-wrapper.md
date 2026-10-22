---
url: "https://kentcdodds.com/blog/replace-axios-with-a-simple-custom-fetch-wrapper"
captured_at: "2020-09-10T19:13:29-03:00"
title: "Replace axios with a simple custom fetch wrapper"
domain: "kentcdodds-com"
---

# Replace axios with a simple custom fetch wrapper

![banner.webp](kentcdodds-com--replace-axios-with-a-simple-custom-fetch-wrapper/be36b2119545cf7e41a821724b2dba75.webp)

![banner.webp](kentcdodds-com--replace-axios-with-a-simple-custom-fetch-wrapper/be36b2119545cf7e41a821724b2dba75.webp)

Photo by [K. Mitch Hodge](https://unsplash.com/photos/kqPlrOrir5g)

*Axios can do a ton of stuff, but here's a simpler solution that can handle most use cases*

I remember being with [Matt Zabriskie](https://twitter.com/mzabriskie) when he
hatched the idea of a vanilla JavaScript version of AngularJS's `$http` service.
It seemed like a brilliant idea and that night in his hotel room at MidwestJS,
he put together the first iteration.

It was awesome because working with raw
[XMLHttpRequest](https://developer.mozilla.org/en-US/docs/Web/API/XMLHttpRequest)
to make HTTP requests was not very fun. His library, which he later called
[`axios`](https://github.com/axios/axios) is a brilliant work and functioned
both in NodeJS and the Browser which I remember him being really excited about
(and I was too).

It's been almost six years now and if you're reading this chances are you've at
least heard of it and very likely used it in the past or are using it now. It
has an enormous and growing number of
[downloads on npm](https://www.npmtrends.com/axios). And while Matt's long moved
on from the project, it is still actively maintained.

Since it was released, the browser standard has evolved to add a new,
promise-based API for making HTTP requests that provided a much nicer developer
experience. This API is called
[fetch](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API) and if you
haven't used it yet, you really ought to check it out. It's widely supported and
easily polyfillable (my favorite is
[unfetch](https://github.com/developit/unfetch) because the dog mascot is cute
).

Here are a few reasons you might consider swapping `axios` for a simple custom
wrapper around `fetch`:

1. Less API to learn
2. Smaller bundle size
3. Reduced trouble when updating packages/managing breaking changes
4. Immediate bug fixes/releases
5. Conceptually simpler

I have a fetch wrapper for
[my bookshelf app](https://github.com/kentcdodds/bookshelf) which has served me
well. Let's build it together:

```
1functionclient(endpoint, customConfig){

2const config ={

3    method:'GET',

4...customConfig,

5}

6

7returnwindow

8.fetch(`${process.env.REACT_APP_API_URL}/${endpoint}`, config)

9.then(response=> response.json())

10}
```

This `client` function allows me to make calls to my app's API like so:

```
1client(`books?query=${encodeURIComponent(query)}`).then(

2data=>{

3console.log('here are the books', data.books)

4},

5error=>{

6console.error('oh no, an error happened', error)

7},

8)
```

However, the built-in `window.fetch` API doesn't handle errors in the same way
`axios` does. By default, `window.fetch` will only reject a promise if the
actual request itself failed (network error), not if it returned a "Client error
response". Luckily, the `Response` object has
[an `ok`](https://developer.mozilla.org/en-US/docs/Web/API/Response/ok) property
which we can use to reject the promise in our wrapper:

```
1functionclient(endpoint, customConfig ={}){

2const config ={

3    method:'GET',

4...customConfig,

5}

6

7returnwindow

8.fetch(`${process.env.REACT_APP_API_URL}/${endpoint}`, config)

9.then(asyncresponse=>{

10const data =await response.json()

11if(response.ok){

12return data

13}else{

14returnPromise.reject(data)

15}

16})

17}
```

Great, now our promise chain will reject if the response is not ok.

The next thing we want to do is be able to send data to the backend. We *can* do
this with our current API, but let's make it easier:

```
1functionclient(endpoint,{body,...customConfig}={}){

2const headers ={'Content-Type':'application/json'}

3const config ={

4    method: body ?'POST':'GET',

5...customConfig,

6    headers:{

7...headers,

8...customConfig.headers,

9},

10}

11if(body){

12    config.body=JSON.stringify(body)

13}

14

15returnwindow

16.fetch(`${process.env.REACT_APP_API_URL}/${endpoint}`, config)

17.then(asyncresponse=>{

18const data =await response.json()

19if(response.ok){

20return data

21}else{

22returnPromise.reject(data)

23}

24})

25}
```

Sweet, so now we can do stuff like this:

```
1client('login',{body:{username, password}}).then(

2data=>{

3console.log('here the logged in user data', data)

4},

5error=>{

6console.error('oh no, login failed', error)

7},

8)
```

Next we want to be able to make authenticated requests. There are various
approaches for doing this, but here's how I do it in the bookshelf app:

```
1const localStorageKey ='__bookshelf_token__'

2

3functionclient(endpoint,{body,...customConfig}={}){

4const token =window.localStorage.getItem(localStorageKey)

5const headers ={'Content-Type':'application/json'}

6if(token){

7    headers.Authorization=`Bearer ${token}`

8}

9const config ={

10    method: body ?'POST':'GET',

11...customConfig,

12    headers:{

13...headers,

14...customConfig.headers,

15},

16}

17if(body){

18    config.body=JSON.stringify(body)

19}

20

21returnwindow

22.fetch(`${process.env.REACT_APP_API_URL}/${endpoint}`, config)

23.then(asyncresponse=>{

24const data =await response.json()

25if(response.ok){

26return data

27}else{

28returnPromise.reject(data)

29}

30})

31}
```

So basically if we have a token in `localStorage` by that key, then we add the
`Authorization` header (per [the JWT spec](https://jwt.io/)) which our server
can then use to determine whether the user is authorized. Very common practice
there.

Another handy thing that we can do is if the `response.status` is `401`, that
means the user's token is invalid (maybe it expired or something) so we can
automatically log the user out and refresh the page for them:

```
1const localStorageKey ='__bookshelf_token__'

2

3functionclient(endpoint,{body,...customConfig}={}){

4const token =window.localStorage.getItem(localStorageKey)

5const headers ={'content-type':'application/json'}

6if(token){

7    headers.Authorization=`Bearer ${token}`

8}

9const config ={

10    method: body ?'POST':'GET',

11...customConfig,

12    headers:{

13...headers,

14...customConfig.headers,

15},

16}

17if(body){

18    config.body=JSON.stringify(body)

19}

20

21returnwindow

22.fetch(`${process.env.REACT_APP_API_URL}/${endpoint}`, config)

23.then(asyncresponse=>{

24if(response.status===401){

25logout()

26window.location.assign(window.location)

27return

28}

29const data =await response.json()

30if(response.ok){

31return data

32}else{

33returnPromise.reject(data)

34}

35})

36}

37

38functionlogout(){

39window.localStorage.removeItem(localStorageKey)

40}
```

Depending on your situation, maybe you'd re-route them to the login screen
instead.

On top of this, the bookshelf app has a few other wrappers for making requests.
Like the `list-items-client.js`:

```
1import{client}from'./api-client'

2

3functioncreate(listItemData){

4returnclient('list-items',{body: listItemData})

5}

6

7functionread(){

8returnclient('list-items')

9}

10

11functionupdate(listItemId, updates){

12returnclient(`list-items/${listItemId}`,{

13    method:'PUT',

14    body: updates,

15})

16}

17

18functionremove(listItemId){

19returnclient(`list-items/${listItemId}`,{method:'DELETE'})

20}

21

22export{create, read, remove, update}
```

## Conclusion

Axios does a LOT for you and if you're happy with it then feel free to keep
using it (I use it for node projects because it's just great and I haven't been
motivated to investigate the alternatives that I'm sure you're dying to tell me
all about right now). But for the browser, I think that you'll often be better
off making your own simple wrapper around `fetch` that does exactly what you
need it to do and no more. Anything you can think of for an axios interceptor or
transform to do, you can make your wrapper do it. If you don't want it applied
to all requests, then you can make a wrapper for your wrapper.

> [pic.twitter.com/cKCLwHNJBp](https://t.co/cKCLwHNJBp)
>
> — Kent C. Dodds ‍ (@kentcdodds) [March 31, 2020](https://twitter.com/kentcdodds/status/1244820744564965376)

Good luck!
