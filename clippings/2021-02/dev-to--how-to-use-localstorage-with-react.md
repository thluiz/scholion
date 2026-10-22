---
url: "https://dev.to/antdp425/how-to-use-localstorage-with-react-2cpn"
captured_at: "2021-02-25T08:39:24-03:00"
title: "How To: Use LocalStorage with React - DEV Community"
domain: "dev-to"
---

# How To: Use LocalStorage with React

When building a React app, there will be times where you'll want to persist data in one way or another. Typically you'd use some type of backend, especially for more sensitive data, but sometimes you just need to save something locally on the users machine — you can do this with LocalStorage. This article will show you how to incorporate LocalStorage with React

**Note 1:** This article assumes that you have a general understanding of React, React Hooks, and localStorage.

**Note 2:** You should only use LocalStorage for simple / trivial data. **DO NOT store sensitive data in LocalStorage.**

**Setup**

Here is what we'll start with — we'll create a simple component where we'll show the user a welcome message or welcome back message depending on if they've visited the site before (on this device/browser) — which we'll know by making use of localStorage. Right now, it will always show the "first time?" welcome message since we haven't persisted anything to localStorage yet.

Here is our component so far:

```
// importing useState and useEffect so that we can make us of them when setting/getting
// data from localStorage
import React, {useState, useEffect} from 'react';

function App() {
 let [welcomeMessage, setWelcomeMessage] = useState("Welcome -- is it your first time? (It is, we know )")

  return (
    <div className="App">
    {welcomeMessage}
    </div>
  );
}

export default App;
```

**Persisting To Local Storage**

Ok, so once the user visits the page, we want to remember that and let localStorage know that they've officially visited the page at least once. Doing this will allow us to welcome them back when they visit the page again, instead of seeing the "first time" message every time.

The way we'll do this is by using useEffect — so once the App component is rendered it will:

- check if localStorage has a "hasVisited" key
  - if it does, it will set the state of welcomeMessage to "Welcome back!"
  - if it doesn't, it will create the key value pair in localStorage

```
import React, {useState, useEffect} from 'react';

function App() {

  let [welcomeMessage, setWelcomeMessage] = useState("Welcome -- is it your first time? (It is, we know )")

  useEffect(() => {
    // checking if localStorage has a "hasVisited" key
    if (localStorage.getItem("hasVisited")){
        // setting the state of welcomeMessage to "Welcome back!" if it does
      setWelcomeMessage("Welcome back!")  
    } else {
        // creating the "hasVisited" key value pair in localStorage if it doesnt exist
      localStorage.setItem("hasVisited", "true")
    }
    // we are only running this useEffect on the first render of app because we passed an
    // empty array
  },[])

  return (
    <div className="App">
    {welcomeMessage}
    </div>
  );
}

export default App;
```

Once the user refreshes the page or revists the page the welcomeMessage will say "Welcome back!"

This is a very simple example of how to make use of localStorage in React. One thing to keep in mind is that localStorage will always store / retrieve as strings, so if you are persisting data that is not a string (numbers, arrays, objects) you'll have to stringify / parse them. You can learn more about that process by checking out my other post about [how to use localStorage](https://dev.to/antdp425/how-to-use-localstorage-ldn) in general.

As always refer to the docs for more info:

[MDN — localStorage](https://developer.mozilla.org/en-US/docs/Web/API/Window/localStorage)

[React — useState](https://reactjs.org/docs/hooks-state.html)

[React — useEffect](https://reactjs.org/docs/hooks-effect.html)

Feel free to reach out here or on my socials for any questions, suggestions, or to say hello
