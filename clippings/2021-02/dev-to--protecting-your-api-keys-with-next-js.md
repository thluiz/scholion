---
url: "https://dev.to/ivanms1/protecting-your-api-keys-with-next-js-21ej"
captured_at: "2021-02-13T08:47:31-03:00"
title: "Protecting your API keys with Next JS - DEV Community 👩‍💻👨‍💻"
domain: "dev-to"
---

# Protecting your API keys with Next JS

12 de fev.
・3 min read

#### This is the story of Max.

Max thought his API keys were safe because he put them inside an `.env` file.

[![giphy.gif](dev-to--protecting-your-api-keys-with-next-js/3b05f8548d1e8331fe2dd5e8be16b47e.gif)](https://i.giphy.com/media/XreQmk7ETCak0/giphy.gif)

Max didn't know his keys were visible in the network tab.

[![i0K3IR3U3.jpeg](dev-to--protecting-your-api-keys-with-next-js/437a461f78c365a7ace39cc79508f4d8.jpeg)](https://res.cloudinary.com/practicaldev/image/fetch/s--B9IgU_U4--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://cdn.hashnode.com/res/hashnode/image/upload/v1613111422990/i0K3IR3U3.jpeg)

Max is actually me, Max is actually everyone.

Especially when we are just learning and start playing with public APIs that require a private key.

There is not a good (or any) way to protect your keys in the frontend.  
One good alternative is to create a proxy in your own server, since backend code is not exposed to the browser. But many people using these APIs are beginners that don't know much about backend yet.

Well, Next JS comes to save the with its integrated and ready to use [API Routes](https://nextjs.org/docs/api-routes/introduction). Which is basically a Node JS environment that you can use to create API endpoints, a server ready to go.

Let's take a look.

### Initial setup

First let's create a next js app.

In the terminal run

```
npx create-next-app next-api-key
# or
yarn create next-app next-api-key
```

Then move to the app folder

```
cd next-api-key
```

### A different .env file

Once inside the project we can create a `.env.local` file. This looks the same as your normal `.env` files if you are familiar with them. The difference is that the variables inside `.env.local` are only available in the Node JS environment of Next. This means the browser doesn't have access to them.

So where can we use these variables?

Inside `pages`, there is another folder called `api`, any file inside here will be treated as an API endpoint.

It works more or less like this.

On the server side we have `pages/api/hello.js`

```
export default (req, res) => {
  res.status(200).json({ name: 'John Doe' })
}
```

On the client side we can call.

```
const fetchHello = async (page) => {
  const res = await fetch(`/api/hello`); // notice the naming
  const data = await res.json();
// data = { name: "John Doe" }
  return data;
};
```

### Protecting the keys

So now that we know how that works, let's add a key in the `.env.local` file.

Let's pretend I have a key that I need to send in the url of my request.

Let's add the key inside `.env.local`

```
SECRET_KEY=someSecretKeyThatNoOneShouldSee
```

And instead of using our key on the client side, we use it inside `hello.js`.

*This variable won't work on the client anyways, read more [here](https://nextjs.org/docs/basic-features/environment-variables#exposing-environment-variables-to-the-browser)*

```
// pages/api/hello.js
import axios from "axios";

export default async (req, res) => {
  const URL = `https://api.i.require.keys/?&api_key=${process.env.SECRET_KEY}`;
  const response = await axios.get(URL);
  res.status(200).json({ data: response.data })
}
```

*You will need to install axios, node-fetch or a similar library to manage the fetching, since `fetch` API is not available in Node.*

Nothing really changes on the client side, but let's use `axios` since we already installed it for the server.

```
const fetchHello = (page) => axios.get('/api/hello')
```

**And that's about it, our key is nowhere to be seen in the network tab.**

That wasn't too hard right?

Please like and share if you found this helpful.

Until next time!
