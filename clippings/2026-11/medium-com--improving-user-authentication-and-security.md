---
url: "https://medium.com/javascript-scene/improving-user-authentication-and-security-ddb60b1ef69b"
captured_at: "2026-11-16T05:51:05+00:00"
title: "Improving User Authentication and Security | by Eric Elliott | JavaScript Scene | Medium"
domain: "medium-com"
---

Top highlight

JavaScript
Technology
Security
React
Programming
Improving User Authentication and Security
Eric Elliott
6 min read
·
Dec 4, 2019

Photo: Brandon Bailey — Midnight Cowboy (CC-BY-2.0)

Managing user authentication and authorization is a very serious responsibility, and getting it wrong can cost a lot more than unauthorized access to your app. It can also compromise user privacy or lead to financial damage or identity theft for your users. Unless you are a huge company with a huge security team, you don’t want that kind of responsibility or liability for your app.

Most apps today are built with username and password authentication, and once a user is signed in, that user session can do anything it wants to do, without revalidating the user’s intention.

That security model is broken for a number of reasons:

Password-only security models are obsolete. If you have any doubt about that, head over to HaveIBeenPwned and plunk in your email address. Sensitive data has been stolen in many high profile data breaches impacting companies like Dropbox, Adobe, Disqus, Kickstarter, LinkedIn, Tumblr, and many, many more. If there’s a database with passwords in it, it’s only a matter of time before it gets stolen.

Hashing passwords won’t save you or your users. Once a database of passwords has been stolen, hackers aim huge distributed computing power at those password databases, utilizing parallel GPUs or giant botnets with hundreds of thousands of nodes to try hundreds of billions of password combinations per second in hopes of recovering plaintext username/password pairs.

If an attacker can discover a password that hashes to the same hash as the one stored in your database, they’ll take that combination and try it on things like bank account websites. In many cases, even a salted, hashed password database will give up another valid username/password pair every minute or so. That’s about half a million leaked passwords per year — and that rate is doubling every few years. I wrote about this topic in 2013. The bad guys are now hashing passwords more than 10 times faster than they were then.

User Sessions Get Hijacked. User sessions are commonly hijacked after authentication, allowing attackers to exploit that user’s application resources. In order to prevent that, you’d need to re-authenticate the user with every request, and in the land of usernames and passwords, that would create an awkward user experience.

Upgrading Authentication

One of the coolest features of decentralized applications is the decentralized security model. Using the Ethereum blockchain ecosystem, each user gets a public and private key pair. Every request can be signed by the user’s private key, and verified using the user’s public key. That means that every request is uniquely authenticated, which reduces the chance of hijacking to nearly zero.

A hijacker would need the ability to sign on behalf of the user, but they can’t do that without access to the user’s private key, and that data can be protected using hardware-level security. Private keys can be protected from access to the internet. Instead of sending the private key over the network, we send the data to be signed to the private key. The user authorizes the signature, and the signed request gets authenticated and processed. If the signature is invalid, the request gets rejected.

Additionally, those key pairs can be used to encrypt user data so that only the user who owns the data can read it. If an app developer chooses to let users encrypt their data, even the application can’t decrypt the data without the user’s permission. With this security model, we can put users in control of their own private information.

How To Get Key Pairs for Users

In order to add this extra layer of security to your app, you need all your users to authenticate with a crypto wallet. Until recently, that meant forcing your user to download extra apps or browser plugins, but thanks to projects like Fortmatic, it’s now possible to integrate a crypto wallet experience directly into your app in a mainstream browser with no extensions.

In the latest video episode of Shotgun for members of EricElliottJS.com, we walked through the process of creating a useFortmatic hook to authenticate users in your app and set them each up with a key pair. Let’s take a look at the code we came up with:

Note: This code is slightly different from the code in the video, to guard against trying to use the fm and web3 APIs before they’ve been initialized. In this new version, the only way to get them is by using the web3Ready promise.

First, we use the useState hook to keep track of the state. In this case, a list of authenticated user wallet accounts. You’ll use those wallets to sign requests and process transactions.

We’re using a web3Ready promise, which is a reference that always refers to the same object, even after additional renders. We resolve that promise after web3 has initialized. The promise will resolve with the initialized fm and web3 objects, ready to use. In this version of the code, the web3Ready promise is the only way to get a handle on the fm and web3 objects. This helps us avoid race conditions, where you try to call signIn or web3 methods before those objects are ready to use.

We initialize automatically with the useEffect hook. During the initialize process, we check the user’s authentication status with Fortmatic, and sign the user into our app automatically if they’re already authenticated:

(await fm.user.isLoggedIn()) && signIn();

Users of the useFortmatic hook should now have everything they need to sign in, sign out, manage user wallet accounts, and access the web3 API. For example, a calling component could use code like this:

const {
accounts, // an array of addresses
signOut, // a function to sign the user out
signIn, // a function to sign the user in `=> Promise`
isSignedIn, // (accounts: [address]) => Boolean
web3Ready, // Promise
web3IsInitialized // Boolean
} = useFortmatic(
'pk_live_248876B2BC93BD1A'
);
// If you want, you can trigger the sign in dialog
// automatically when your component mounts. We wrap
// the signIn() call in another function to avoid returning
// a promise to useEffect(), which makes React complain.
useEffect(() => signIn(), []);
// You can also listen for sign in and sign out
// and handle it however you like (e.g., Redux action).
useEffect(() => {
// you can listen for auth status changes
// and dispatch Redux actions here:
console.log('accounts changed!', accounts);
}, [accounts]);

Note: API keys are not secrets, but you definitely need to get your own. Fortmatic requires you to register your authorized domain with your API key, and will refuse to work if you try to use it from an unauthorized domain.

You may have noticed that the useFortmatic hook is not falling back if the browser has a built-in Web3 wallet. For UX and user privacy reasons, we’re not going to expose the app to the user’s native browser wallet by default. As an app developer, you can choose to detect this situation and also expose a built-in wallet to the user if you wish. For example, to let users access their browser wallet assets from within your application.

Conclusion

Using decentralized security models can improve your user’s security by giving each user a public/private key pair. Using that technology, they can sign each transaction, reducing several risks:

Man in the middle and session hijacking attacks
Password database theft
Brute force password cracking attempts

You can also use those key pairs in interesting ways:

Users sign messages and requests to prove that the message came from somebody with access to the user’s private key
Encrypt data so that only the user can unlock it
Use user signatures to authorize actions and transactions
Require signatures from multiple users to access shared resources
Next Steps

Members can watch the new episode on EricElliottJS.com. If you’re not a member, now’s a great time to see what you’ve been missing!

Start your free lesson on EricElliottJS.com

Eric Elliott is the author of the books, “Composing Software” and “Programming JavaScript Applications”. As co-founder of EricElliottJS.com and DevAnywhere.io, he teaches developers essential software development skills. He builds and advises development teams for crypto projects, and has contributed to software experiences for Adobe Systems, Zumba Fitness, The Wall Street Journal, ESPN, BBC, and top recording artists including Usher, Frank Ocean, Metallica, and many more.

He enjoys a remote lifestyle with the most beautiful woman in the world.
