---
url: "https://dev.to/rajajaganathan/why-skip-nav-link-is-important-14bc"
captured_at: "2026-11-16T01:22:52+00:00"
title: "Why \"Skip Nav\" Link is important!"
domain: "dev-to"
---

A little while back, I'd the opportunity to work for accessibility implementation. one of my colleague [Nawaz Khan](https://twitter.com/mpnkhan) a11y expert asked me to implement SkipNav for the page. The term "Skip Navigation" links are completely new for me and I've come up with a decent implementation that might be useful to everyone who cares about accessibility and usability. In this article, I'd like to discuss what is the problem without Skip Navigation links and how to build a Skip Navigation links for our website or application.

## [](#problem)Problem:

Take a glance at [https://www.nytimes.com/](https://www.nytimes.com/) for a minute, see how many links present in the header, sidebar, footer etc..,?

The main content is not usually the first thing on a web page. Keyboard and screen reader users generally must navigate a long list of navigation links, sub-lists of links, corporate icons, site searches, and other elements before ever arriving at the main content

1.  How to navigate to the main content without visiting all header navigation links?
    
2.  How to avoid visiting all the links for every page when navigating to another page.
    

The solution is **"Skip Navigation"** Links

## [](#solution)Solution:

Generally, skip nav links are placed first or second links of the website so that users can easily navigate to the main content or desired section easily in a few tabbing. we might have seen many different approaches to solve the problem but I see below two-approach are used widely

1.  Providing visible links at the top of the page
2.  Making the link invisible until it receives keyboard focus

We'll talk about the 2nd approach and its implementation.

Let's see how [https://www.nytimes.com/](https://www.nytimes.com/) solved this problem visually.

![a11y skip nav link](https://res.cloudinary.com/practicaldev/image/fetch/s--fBGbLEUn--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_66%2Cw_880/https://dev-to-uploads.s3.amazonaws.com/i/d2hhn3iqsuq12jh0iura.gif)

As you can see in the clip, showing the skip nav link when the link receives the keyboard focus.

That's cool. Now see how user navigates to the _site to index_ section of the site which declared way down in the site.

![a11y skip nav link2](https://res.cloudinary.com/practicaldev/image/fetch/s--GcDa1WgV--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_66%2Cw_880/https://dev-to-uploads.s3.amazonaws.com/i/ncgt3qz31j9ggb14ft69.gif)

Let's implement the same functionality with the help of CSS and React.

Here we're controlling link toggle logic only in CSS through **:focus** pseudo selector like below, we are hiding the element normally then we'll show link in the screen only when the link element receives the focus. Note that we are not using **display: none** or **visibility: hidden** these make it inaccessible, Technically those types of elements (applied _display: none_ and _visibility: hidden_) are not part of Accessibility tree. Hence we are using **clip** CSS properties.  

```
.skip-nav-link {
    border: 0;
    clip: rect(0 0 0 0);
    height: 1px;
    margin: -1px;
    overflow: hidden;
    padding: 0;
    position: absolute;
    width: 1px;
}

.skip-nav-link:focus {
    background: white;
    clip: auto;
    height: auto;
    left: 10px;
    padding: 1rem;
    position: fixed;
    top: 0px;
    width: auto;
    z-index: 1001;
}

```

Enter fullscreen mode Exit fullscreen mode

React implementation is dead simple and self-explanatory too. These 2 component does the job better _SkipNavLink_ and _SkipNavContent_  

```

export const SkipNavLink = ({ id, children = 'Skip to content', ...props }) => {
  return (
    <a {...props} href={`#${id}`} className="skip-nav-link">
      {children}
    </a>
  );
};

export const SkipNavContent = ({ id, ...props }) => {
  return <div id={id} {...props} />;
};
```

Enter fullscreen mode Exit fullscreen mode

Here is the usage of components  

```
...
<SkipNavContent id="main-content">
    <main>
        Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod
        tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,
        quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo
        consequat. Duis aute irure dolor in reprehenderit in voluptate velit ease
    </main>
</SkipNavContent>
...

ReactDOM.createPortal(
    <React.Fragment>
        <SkipNavLink id="main-content">
            Skip to main
        </SkipNavLink>
        <SkipNavLink id="sitemap-links">
            Skip to sitemap
        </SkipNavLink>
    </React.Fragment>,
    document.getElementById('skip-links-root')!
)
```

Enter fullscreen mode Exit fullscreen mode

To get some rough ideas on how laid out our HTML page.  

```
<body>
    <div class="wrapper">
        <div id="skip-links-root">
            <!-- Skip Nav links -->
        </div>
        <header>
            <nav>
                <!-- Nav links -->
            </nav>
        </header>
        <div id="root">
            <!-- React content goes here -->
        </div>
    </div>
</body>

```

Enter fullscreen mode Exit fullscreen mode

Just take a moment to think about how tiny changes improved the user experience a lot better.

That's it.

Happy Tabbing ⌨️! ❤️

#### [](#reference)Reference:

[https://webaim.org/techniques/skipnav/](https://webaim.org/techniques/skipnav/)
