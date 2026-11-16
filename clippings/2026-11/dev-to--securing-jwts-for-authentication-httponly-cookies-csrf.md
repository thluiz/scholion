---
url: "https://dev.to/petrussola/today-s-rabbit-hole-jwts-in-httponly-cookies-csrf-tokens-secrets-more-1jbp"
captured_at: "2026-11-16T01:59:15+00:00"
title: "Today's rabbit hole: securing JWTs for authentication, httpOnly cookies, CSRF tokens, secrets & more"
domain: "dev-to"
---

_Note: this is first and foremost the tale of a journey. It acts as a how-to, but I also want to share my thought process and how I learnt along the way. If any of the below is total nonsense, let me know in the comments!_

Trigger: [JWT authentication: When and how to use it by Flavio Copes](https://blog.logrocket.com/jwt-authentication-best-practices/)

He says `Don’t store it in local storage (or session storage). If any of the third-party scripts you include in your page gets compromised, it can access all your users’ tokens.`

I knew that localStorage is not safe. But if not in localStorage, where can I store them?

Flavio adds `The JWT needs to be stored inside an httpOnly cookie, a special kind of cookie that’s only sent in HTTP requests to the server, and it’s never accessible (both for reading or writing) from JavaScript running in the browser.`.

Good lead. I head to [Using HTTP cookies, in MDN,](https://developer.mozilla.org/en-US/docs/Web/HTTP/Cookies) to learn what a httpOnly cookie is. httpOnly is an attribute added to cookies that make it unaccesible client side.

Ok. How to store JWT in an httpOnly cookie? A Google search returned [this article by Ryan Chenkie](https://medium.com/@ryanchenkie_40935/react-authentication-how-to-store-jwt-in-a-cookie-346519310e81).

He says there are two options to securely store a JWT:

1.  Browser memory (React state) - super safe. However, if User refreshes browser, JWT is lost, and login is required again. Not a good user experience.
2.  httpOnly cookie. This is what I am looking for!

My login endoint needs to generate the JWT and save it in a cookie:  

```
    res.cookie('token', token, { httpOnly: true });
```

Enter fullscreen mode Exit fullscreen mode

`token` is previously generated in my code by the library `jsonwebtoken`. `httpOnly: true` is what makes the cookie not visible to client. I did a test: when `httpOnly` was set to `false` I could access the content of the cookie in the Console with `document.cookie`. Setting `httpOnly: true` prevents this.

Now, the problem is that my client and my server are running on different ports (3000 and 5000) in localhost. As [this StackOverflow thread reminded me](https://stackoverflow.com/a/3342167/3630417) there is no such thing as cross-domain cookies - cookies can only be set in the same domain as the server. Ughh, how to circumvent this?

I created my client with Create-React-App and they have something called [proxying](https://create-react-app.dev/docs/proxying-api-requests-in-development). Adding `"proxy": "http://localhost:4000",` in my package.json and making the URLs to which I make the API calls relative (i.e. instead of `${baseAPI}/auth/login` I used `/auth/login`) was enough.

After this, the responses from the server started to come back with a `Set-cookie` header and I then could see the Cookie in my Chrome Dev Tools.

As Ryan says, `Now that the JWT is in a cookie, it will automatically be sent to the API in any calls we make to it. This is how the browser behaves by default.`. As he advises, I started using `cookie-parser` library to transform the cookie header into a clean `req.cookies` from where I can easily fetch the token to run the JWT validation.

**Next question: how to protect Routes when the token is stored in a cookie?**

By definition, an `httpOnly` cookies cannot be accessed by the client, so how can we protect Routes after User has logged in? Somone came up with an idea in [this StackOverflow question](https://stackoverflow.com/a/51965652/3630417). Basically, you continue to generate the `httpOnly: true` cookie containing the token and you generate another one, `httpOnly: false` this time, with no sensitive info, that only informs that User has logged in. I suppose that following that logic, you don't even need a cookie: upon receiving the succesful login API response, you can save a `loggedIn: true` in `localStorage`. In any case, I continued with Cookies.

So you can check the `httpOnly: false` cookie (or localStorage) and determine if User is logged in or not. If they are not, redirect to Login page.

Now, how to access cookies in React?

I found [this conversation](https://stackoverflow.com/questions/51109559/get-cookie-with-react) about the topic. There are of course 2 ways: use a library or do it yourself.

While I want to build logic myself as much as possible, this time as a first pass I decided to use a library. I was having enough headaches with the Private Route that I didn't want to add additional opportunities for bugs. I used [js-cookie](https://www.npmjs.com/package/js-cookie). _For when I am ready to stretch myself, the last answer [here](https://stackoverflow.com/questions/51109559/get-cookie-with-react) points to [examples in MDN](https://developer.mozilla.org/en-US/docs/Web/API/document/cookie#Example_2_Get_a_sample_cookie_named_test2) to fetch cookies yourself._

Next, I needed to protect Routes so only Users that are logged in (aka have the `isLoggedIn` cookie set to `true` can access it.

I knew how to create a `<PrivateRoute />`, but I did some research to confirm I was not missing anything. I found [Tyler McGinnis post](https://ui.dev/react-router-v4-protected-routes-authentication/), it is perfect as a step by step guide.

My Private Route:  

```
const PrivateRoute = ({ render: Component, ...rest }) => (
    <Route
        {...rest}
        render={(props) =>
            Cookie.get('isLoggedIn') === 'true' ? (
                <Component {...props} />
            ) : (
                <Redirect to='/login' />
            )
        }
    />
);
```

Enter fullscreen mode Exit fullscreen mode

I used the `PrivateRoute` to protect my Route:  

```
<PrivateRoute
    exact
    path='/'
    render={(props) => (
        <AddUrl {...props} shortUrl={shortUrl} setShortUrl={setShortUrl} />
    )}
/>
```

Enter fullscreen mode Exit fullscreen mode

`render: Component` was originally `component: Component` because this is the syntax I had read in tutorials. However, it was not working, and couldn't figure out why for a while. I read [this answer](https://stackoverflow.com/a/47910354/3630417) and I realised that the key needs to match the attribute you are passing in the Route. So if you pass `component={WHATEVER_COMPONENT_NAME}` the Private Route should have `component: Component`. Since my Route had `render={bla bla bla}` the Private Route had to have `render: Component`.

**Next question: how to logout?**

Since the cookie with the token is `httpOnly: true` it won't be accessible in the client, so you need the server to remove it. As someone pointed out in [this StackOverflow question](https://stackoverflow.com/a/5285982/3630417), you can update the cookie server side with a rubbish or empty text.

[This conversation](https://stackoverflow.com/questions/44401785/overwrite-update-browser-cookie), confused me. The person replying says you can set `overwrite: true` but I could not find the attribute in [the Express docs about res.cookie](https://expressjs.com/en/api.html#res.cookie). This is when I realised that the person answering was talking about a library, not the express native method.

So, I ended up setting a cookie server side with the same name but a dummy value, and keeping `httpOnly: true`. And I am also modifying the client visible cookie that I called `isLoggedIn` and setting it to false.  

```
res.cookie('token', 'deleted', { httpOnly: true });
res.cookie('isLoggedIn', false);
```

Enter fullscreen mode Exit fullscreen mode

**Ok. Is there something else?**

I am afraid yes... Ryan talks about _adding Cross-Site Request Forgery Protection_ and _adding an anti-CSRF token_. Hmm, what is that? First time I hear about these cookies, I continue digging...

**What is a Cross Site Request Forgery attack**

There are million of resources out there, a lot of them hard to understand, and I found [this one](https://www.imperva.com/learn/application-security/csrf-cross-site-request-forgery/) helpful. Basically the attacker creates a HTTP request url to some service (your ebank account, for instance) that is hidden inside a malicious site. You may be tricked into going to that site an by doing so, inadvertedly, you trigger this HTTP request. The point of the attack is that, because you are authenticated, authentication cookies are passed with the request and, to the server, the request is legit.

AFAIK, there are protections the server should take in order to protect from these attacks: strict CORS policy (only allowing requests from specific origins, if necessary) and CSRF tokens.

**What is a CSRF token**

I found [this answer](https://stackoverflow.com/a/33829607/3630417) and [this answer](https://stackoverflow.com/a/5207418/3630417) quite clarifying.

I generate the CSRF token server side using [csurf library](https://www.npmjs.com/package/csurf) and once passed to the client in the body of the response it is set as a header to every AJAX request you make to your server. You should generate the token as early as possible in your application because the CSRF token check is a middleware that is placed as early as possible in your server. The way Ryan recommends to do it is:

1.  `useEffect` on your React App calling a custom end point to fetch the CSRF token. This token is generated by a library, he recommends `csurf`.
2.  The token is returned in the body of the response and the secret to check that the token has not been tampered is returned as a cookie. The former should be set as a header to every subsequent AJAX request with an `axios.default.headers.post['X-CSRF-Token]'. The latter should be returned to the client as a`httpOnly`and`secure`cookie. This is sent in a`Set-cookie\` header and the cookies should then be added to every subsequent request by the client.

Now, I found the following problematic. Ryan is suggesting to create an endpoint that sends the token to the client. However, if you go to the [npm page of the csurf library](https://www.npmjs.com/package/csurf) they have a header linking to this page: [Understanding CSRF, section on CSRF Tokens](https://github.com/pillarjs/understanding-csrf#csrf-tokens). They say `Don't create a /csrf route just to grab a token, and especially don't support CORS on that route!`.

Apparently I am not the same asking this same question - see examples [here](https://stackoverflow.com/questions/54571247/do-i-have-to-use-csrf-protection-in-react-spa) or [here](https://stackoverflow.com/questions/28996315/passing-csrf-token-to-react-flux-from-node). Based on my reading, while everyone seems to have a different receipe, everyone seems to agree that there is no bullet-proof way to do it.

I found [this post by Harleen Mann](https://mannharleen.github.io/2020-03-19-handling-jwt-securely-part-1/) where he explains how to mitigate the risks when using cookies to store JWTs:

1.  XSS - can be mitigated by using `httpOnly` cookies. Ok, done.
2.  CSRF - Can be mitigated by using:

i. CORS Policy - in development I am hosting my frontend in a different URLs as my server. Therefore, if I configure CORS in my server so as to only allow data to be read if the request comes from the authorised url. Similar in production, I ended up hosting the client in a subdomain (as in `subdomain.example.com`) and the server in the root domain (as in `example.com`). I learn through much pain and hours afterwards that the same setting for development and production are needed. So, `cors` library will be configured as:

\`  

```
const corsProtection = require('cors');

const cors = corsProtection({
    origin: process.env.DEV_FRONTEND_URL, // url of the client making the http requests
    optionsSuccessStatus: 200,
});

module.exports = cors;
```

Enter fullscreen mode Exit fullscreen mode

ii. X-CSRF-TOKEN Header - as discussed above, I am getting the csrf token from a dedicated endpoint when my React app loads. Because of the config above, the endpoint is protected and only requests coming from the authorized url are allowed. Because CSRF attacks originate in other domains (the malicious website) I believe I am protected.  
iii. [SameSite cookie](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Set-Cookie/SameSite) - similar to the previous point, my understanding is that CSRF attacks are initiated by 3rd party malicious websites. Therefore, when this attribute is set to `strict`, the cookies won't be sent to the server because the request would be initiated by a 3rd party. Except for Internet Explorer, `sameSite` seems to be supported by the rest of browsers.

I am sparing you the hours I spent troubleshooting my code, that worked perfectly fine in development and local host, when hosted in production. Long story short, I thought that as long as client and server are hosted on the same domain, cookies are shared fine. No, you need to specifiy `domain: example.com` and you need the \[`Access-Control-Allow-Credentials` header\]([https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Access-Control-Allow-Credentials#:~:text=The%20Access%2DControl%2DAllow%2D,the%20request's%20credentials%20mode%20(%20Request.&text=When%20used%20as%20part%20of,can%20be%20made%20using%20credentials.)](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Access-Control-Allow-Credentials#:%7E:text=The%20Access%2DControl%2DAllow%2D,the%20request's%20credentials%20mode%20\(%20Request.&text=When%20used%20as%20part%20of,can%20be%20made%20using%20credentials.\)) and the [`withCredentials` property](https://developer.mozilla.org/en-US/docs/Web/API/XMLHttpRequest/withCredentials). The latter is done adding a property `withCredentials: true` to and `axios` instance and `credentials: true` in the server `cors` config. My [own question and answer](https://stackoverflow.com/questions/63513651/cookie-set-on-root-domain-not-available-to-subdomain-what-am-i-doing-wrong) may be helpful to clarify what I mean.

At this point, I took a step back and realised that I didn't really really understand what `csurf` library does. I read, and re-read, [their docs](https://www.npmjs.com/package/csurf). It does 2 things:

1.  As a middleware, it adds a `req.csrfToken()` function that you call to generate the csrf token. This token should be passed to the frontend, which in turn, should add it to a `'x-csrf-token'` header. This header, upon hitting the server, will then get verified with the secret that comes back as a cookie - see below.
2.  Generates a token secret either in a cookie or in `req.session`. Since I am using JWTs for authentication, I am not going to use `req.session` - I set the secret in a cookie.

The `csurf` config object looks something like this for me:  

```
let csrfProtection = null;

if (process.env.NODE_ENV === 'development') {
    csrfProtection = csrf({
        cookie: {
            httpOnly: true,
            secure: false,
            domain: process.env.CSRF_PROTECTION_HOST, // host (NOT DOMAIN, NOT HTTP:// OR HTTPS://)!
        },
    });
} else {
    csrfProtection = csrf({
        cookie: {
            maxAge: 60 * 60 * 24, // 1 day in seconds
            httpOnly: process.env.HTTP_ONLY,
            secure: process.env.SECURE,
            domain: process.env.CSRF_PROTECTION_HOST, // host (NOT DOMAIN, NOT HTTP:// OR HTTPS://)!
            sameSite: process.env.SAME_SITE,
        },
    });
}
```

Enter fullscreen mode Exit fullscreen mode

As `csurf` explains in the docs, when cookie option is chosen, something called the `double submit cookie pattern` (DSCP) is implemented. DSCP is explained (here)\[[https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site\_Request\_Forgery\_Prevention\_Cheat\_Sheet.html#double-submit-cookie](https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html#double-submit-cookie)\]. My understanding is that the token is encrypted with a secret that only the server knows, and this secret is passed on as a cookie.

[Another interesting resource about DSCP](https://security.stackexchange.com/questions/220797/is-the-double-submit-cookie-pattern-still-effective).

In my case, I have set up `csurf` to send the token in the response of an API call, and the secret in an `httpOnly` and `secure` cookie:

*   The token gets set on the endpoint that generates the token and returned to the client. Since the server does not allow cors, I believe that I have protected my endpoint.

```
const token = req.csrfToken();
res.status(200).json({ csrfToken: token });
res.status(200).send();
```

Enter fullscreen mode Exit fullscreen mode

The client, upon receiving the token, sets it as a `['x-csrf-token']` header:  

```
const { data } = await axiosInstance.get(`${baseApi}/auth/csrf-token`);
axiosInstance.defaults.headers.post['x-csrf-token'] = data.csrfToken;
```

Enter fullscreen mode Exit fullscreen mode

I have created an Axios instance in order to include `withCredentials: true` in development. In production, since it is all the same domain, I don't add anything but I still need it to add the header later on:  

```
if (process.env.NODE_ENV === 'development') {
    axiosInstance = axios.create({
        withCredentials: true,
    });
} else {
    axiosInstance = axios.create();
}
```

Enter fullscreen mode Exit fullscreen mode

As a result, every subsequent request to the server will have this header added.

*   The secret gets added to `_csrf` cookie by `csurf` by default when selecting the cookie option (read above).

When the server receives any subsequent client request:

*   `csurf` looks for the token in the places listed [here](https://www.npmjs.com/package/csurf#value) and checks it with the the secret.
    
*   The secret comes back in the `_csrf` cookie.
    

If the token has been tampered with, `csurf` throws an error because it cannot verify it with the secret.

Other `csurf` related content that I found useful:

*   [How to secure my react app api with csurf?](https://stackoverflow.com/questions/59547873/how-to-secure-my-react-app-api-with-csurf)
*   [Express CSRF token validation](https://stackoverflow.com/questions/33060044/express-csrf-token-validation)
*   [How csurf middleware validates tokens?](https://stackoverflow.com/questions/57812757/how-csurf-middleware-validates-tokens#:~:text=1%20Answer&text=The%20csurf%20works%20by%20storing,case%20of%20cookie%2Dparser%20).&text=The%20middleware%20will%20then%20fetch,secret%20owned%20by%20the%20user.)

**However, there is more!**

Both [Ryan](https://medium.com/@ryanchenkie_40935/react-authentication-how-to-store-jwt-in-a-cookie-346519310e81) and [Harleen](https://mannharleen.github.io/2020-03-19-handling-jwt-securely-part-1/) say that the safest method is storing the JWT in-memory and using refresh tokens.

`If you can, store your JWTs in your app state and refresh them either through a central auth server or using a refresh token in a cookie, as outlined in this post by [Hasura](https://hasura.io/blog/best-practices-of-using-jwt-with-graphql/).`

`In-memory is definitely the most secure!` `As you will see the Part-2 of this series, we can overcome these limitations quite easily. See you in Part-2. Hint: refresh_tokens`

What does it all mean?! The Rabbit hole continues..

But I am exhausted, so I am stopping here for today. More in future posts!
