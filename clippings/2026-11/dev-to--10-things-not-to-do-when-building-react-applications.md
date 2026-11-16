---
url: "https://dev.to/jsmanifest/10-things-not-to-do-when-building-react-applications-58a7"
captured_at: "2026-11-16T18:49:18+00:00"
title: "10 Things NOT To Do When Building React Applications"
domain: "dev-to"
---

Follow me on [medium](https://medium.com/@jsmanifest) if you haven't already :)

[React](https://reactjs.org/) is such a popular tool for developing in the web and i'm sure you react fans out there are feeling blessed to be able to get your hands dirty with such a great library :)

Unfortunately nothing is perfect in life, and react is no different.

React comes with its own set of _gotchas_\--some of it potentially becoming a severe problem to your applications if you don't take care of them _now_.

Here are 10 Things NOT To Do When Building React Applications:

## [](#1-spending-too-much-time-in-your-own-private-world)1\. Spending Too Much Time In Your Own Private World

[![react isolation](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fbmygn4nakizylshzstwa.jpg)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fbmygn4nakizylshzstwa.jpg)

If you're spending too much time coding everything in your project and not taking some time to read on what's happening in the community, you _might_ be at risk of _coding bad practices that have been reported in the community_. And you might be at risk of continuing to code those bad practices until you did it 20 times before you finally got the chance to find out on a medium post that it was _bad_.

When that happens, _now_ you have to go back and refactor those 20 code implementations because you found out too late while everybody else is ahead of you and moved on with newer news.

When react released [hooks](https://reactjs.org/docs/hooks-overview.html), I was so excited and began building a bunch of mini projects to play with these new toys that everybody was all hyped up about. After reading a couple sources that hooks were going to be stable I began implementing these more seriously to my projects. I was using _useState_ and _useEffect_ like a boss _everywhere_.

And then I came across someone linking to [this twitter tweet](https://twitter.com/dan_abramov/status/1083330668522864640?lang=en), which lead me to do some more research about useReducer.

That _30 minutes of research_ was enough to have me go back and refactor a good amount of code.

## [](#2-using-bind-not-class-component-constructors)2\. Using _.bind_ (Not class component constructors)

I think the majority of us react developers are aware that we should _.bind_ our class methods if we want to reference _this_ to access their own class instance inside their methods. (Unless you're using a [transpiler](https://babeljs.io/docs/en/babel-plugin-proposal-class-properties) to transpile your class properties and methods.

That's great and I agree to prefer declaring them with _arrow functions_.

But this part I am going to talk about isn't about that. It's about _inline functions_\--or functions that is defined within the _render method_ of a react component and passed down as a prop to a child component.

When inline functions are defined in the render method, react begins to designate a new function instance each time the component re-renders. This is known to cause performance issues due to [wasteful re-rendering](https://www.freecodecamp.org/news/how-to-identify-and-resolve-wasted-renders-in-react-cc4b1e910d10/).

Let's take a look at this example:  

```
const ShowMeTheMoney = () => {
  const [money, setMoney] = useState(0)

  const showThemTheMoney = (money) => {
    setMoney(money)
  }

  const hideTheMoney = () => {
    setMoney(null)
  }

  const sayWhereTheMoneyIs = (msg) => {
    console.log(msg)
  }

  return (
    <div>
      <h4>Where is the money?</h4>
      <hr />
      <div style={{ display: 'flex', alignItems: 'center' }}>
        <SomeCustomButton
          type="button"
          onClick={() => sayWhereTheMoneyIs("I don't know")}
        >
          I'll tell you
        </SomeCustomButton>{' '}
        <SomeCustomButton type="button" onClick={() => showThemTheMoney(0.05)}>
          I'll show you
        </SomeCustomButton>
      </div>
    </div>
  )
}
```

Enter fullscreen mode Exit fullscreen mode

We _know_ that `onClick={() => sayWhereTheMoneyIs("I don't know")}` and `onClick={() => showThemTheMoney(0.05)}` are _inline functions_.

I've seen a couple of tutorials (including one from _Udemy_) that encourage doing this:  

```
return (
  <div>
    <h4>Where is the money?</h4>
    <hr />
    <div style={{ display: 'flex', alignItems: 'center' }}>
      <SomeCustomButton
        type="button"
        onClick={sayWhereTheMoneyIs.bind(null, "I don't know")}
      >
        I'll tell you
      </SomeCustomButton>{' '}
      <SomeCustomButton
        type="button"
        onClick={showThemTheMoney.bind(null, 0.05)}
      >
        I'll show you
      </SomeCustomButton>
    </div>
  </div>
)
```

Enter fullscreen mode Exit fullscreen mode

This _seems_ like it caches the reference thus avoiding unnecessary re-renders because they _aren't using arrow inline functions in the render method_, but they are actually still [creating new functions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_objects/Function/bind) on each render phase!

Some of us may have already known that if we'd been following the community in the react ecosystem during the times when class components were trending.

However, since react hooks were released the talks about .bind have been swaying away since class components are becoming less popular---and usually, when _.bind_ was the topic to talk about, it'd usually _be_ about binding class methods. And to addon to that, these examples above aren't even binding to class methods at all, so that makes it even harder to notice the consequences here if you aren't careful enough.

The _newcomers_ should especially be aware of this anti-pattern!

## [](#3-passing-dynamic-values-as-keys-to-children)3\. Passing Dynamic Values As Keys to Children

Have you ever come across a time where you _felt_ forced to provide unique keys to children that were being mapped over?

It's good to provide unique keys:  

```
const Cereal = ({ items, ...otherProps }) => {
  const indexHalf = Math.floor(items.length / 2)
  const items1 = items.slice(0, indexHalf)
  const items2 = items.slice(indexHalf)
  return (
    <>
      <ul>
        {items1.map(({ to, label }) => (
          <li key={to}>
            <Link to={to}>{label}</Link>
          </li>
        ))}
      </ul>
      <ul>
        {items2.map(({ to, label }) => (
          <li key={to}>
            <Link to={to}>{label}</Link>
          </li>
        ))}
      </ul>
    </>
  )
}
```

Enter fullscreen mode Exit fullscreen mode

Now pretend that some _to_ values in _items1_ happen to be the same as some in _items2_.

I've seen that when some people want to refactor a similar component to this, they'd end up doing something like this:  

```
import { generateRandomUniqueKey } from 'utils/generating'

const Cereal = ({ items, ...otherProps }) => {
  const indexHalf = Math.floor(items.length / 2)
  const items1 = items.slice(0, indexHalf)
  const items2 = items.slice(indexHalf)
  return (
    <>
      <ul>
        {items1.map(({ to, label }) => (
          <li key={generateRandomUniqueKey()}>
            <Link to={to}>{label}</Link>
          </li>
        ))}
      </ul>
      <ul>
        {items2.map(({ to, label }) => (
          <li key={generateRandomUniqueKey()}>
            <Link to={to}>{label}</Link>
          </li>
        ))}
      </ul>
    </>
  )
}
```

Enter fullscreen mode Exit fullscreen mode

This _does_ get the job done with providing unique keys to each children. But there are two things wrong:

1.  Not only are we making react do unnecessary work with generating unique values, but we're also ending up [recreating all of our nodes on every render because the key is different each time](https://github.com/facebook/react/issues/1342).
    
2.  The _key_ concept in react is _all about identity_. And to identify which component is which, the keys _do_ need to be unique, but _not like that_.
    

Something like this would have become a little better:  

```
import { generateRandomUniqueKey } from 'utils/generating'

const Cereal = ({ items, ...otherProps }) => {
  const indexHalf = Math.floor(items.length / 2)
  const items1 = items.slice(0, indexHalf)
  const items2 = items.slice(indexHalf)
  return (
    <>
      <ul>
        {items1.map(({ to, label }) => (
          <li key={`items1_${to}`}>
            <Link to={to}>{label}</Link>
          </li>
        ))}
      </ul>
      <ul>
        {items2.map(({ to, label }) => (
          <li key={`items2_${to}`}>
            <Link to={to}>{label}</Link>
          </li>
        ))}
      </ul>
    </>
  )
}
```

Enter fullscreen mode Exit fullscreen mode

Now we should feel confident that each item will have their own unique key value while _preserving_ their identity.

## [](#4-declaring-default-parameters-over-null)4\. Declaring Default Parameters Over Null

I was once guilty of spending a good amount of time debugging something similar to this:  

```
const SomeComponent = ({ items = [], todaysDate, tomorrowsDate }) => {
  const [someState, setSomeState] = useState(null)

  return (
    <div>
      <h2>Today is {todaysDate}</h2>
      <small>And tomorrow is {tomorrowsDate}</small>
      <hr />
      {items.map((item, index) => (
        <span key={`item_${index}`}>{item.email}</span>
      ))}
    </div>
  )
}

const App = ({ dates, ...otherProps }) => {
  let items
  if (dates) {
    items = dates ? dates.map((d) => new Date(d).toLocaleDateString()) : null
  }

  return (
    <div>
      <SomeComponent {...otherProps} items={items} />
    </div>
  )
}
```

Enter fullscreen mode Exit fullscreen mode

Inside our _App_ component, if _dates_ ends up being _falsey_, it will be initialized with _null_.

And if we run the code--if you're like me, our instincts tell us that _items_ should be initialized to an empty array by default if it was a falsey value. But our app will crash when _dates_ is falsey because _items_ is null. What?

Default function parameters allow named parameters to become initialized with default values if [_no value or undefined_ is passed](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Default_parameters)!

In our case, even though _null_ is falsey, it's still a value!

This mistake caused me a lot of time to debug, especially when the _null_ value was coming from the redux reducers! Ugh.

## [](#5-leaving-repetitive-code-untouched)5\. Leaving Repetitive Code Untouched

it can be tempting to copy and paste code when you're being rushed to push out a fix as it can sometimes be the quickest solution.

Here is an example of repetitive code:  

```
const SomeComponent = () => (
  <Body noBottom>
    <Header center>Title</Header>
    <Divider />
    <Background grey>
      <Section height={500}>
        <Grid spacing={16} container>
          <Grid xs={12} sm={6} item>
            <div className={classes.groupsHeader}>
              <Header center>Groups</Header>
            </div>
          </Grid>
          <Grid xs={12} sm={6} item>
            <div>
              <img src={photos.groups} alt="" className={classes.img} />
            </div>
          </Grid>
        </Grid>
      </Section>
    </Background>
    <Background grey>
      <Section height={500}>
        <Grid spacing={16} container>
          <Grid xs={12} sm={6} item>
            <div className={classes.labsHeader}>
              <Header center>Labs</Header>
            </div>
          </Grid>
          <Grid xs={12} sm={6} item>
            <div>
              <img src={photos.labs} alt="" className={classes.img} />
            </div>
          </Grid>
        </Grid>
      </Section>
    </Background>
    <Background grey>
      <Section height={300}>
        <Grid spacing={16} container>
          <Grid xs={12} sm={6} item>
            <div className={classes.partnersHeader}>
              <Header center>Partners</Header>
            </div>
          </Grid>
          <Grid xs={12} sm={6} item>
            <div>
              <img src={photos.partners} alt="" className={classes.img} />
            </div>
          </Grid>
        </Grid>
      </Section>
    </Background>
  </Body>
)
```

Enter fullscreen mode Exit fullscreen mode

Now's a good time to begin thinking about how to abstract these components in a way where they can be reused multiple times _without changing the implementation_. If there was a styling issue in one of the _Grid_ components relative to their surrounding \*Grid container\*s, you'd have to manually change every single one of them.

A better way to have this coded is probably abstracting out the repeated parts, and passing in the props that are slightly different:  

```
const SectionContainer = ({
  bgProps,
  height = 500,
  header,
  headerProps,
  imgProps,
}) => (
  <Background {...bgProps}>
    <Section height={height}>
      <Grid spacing={16} container>
        <Grid xs={12} sm={6} item>
          <div {...headerProps}>
            <Header center>{header}</Header>
          </div>
        </Grid>
        <Grid xs={12} sm={6} item>
          <div>
            <img {...imgProps} />
          </div>
        </Grid>
      </Grid>
    </Section>
  </Background>
)

const SomeComponent = () => (
  <Body noBottom>
    <Header center>Title</Header>
    <Divider />
    <SectionContainer
      header="Groups"
      headerProps={{ className: classes.groupsHeader }}
      imgProps={{ src: photos.groups, className: classes.img }}
    />
    <SectionContainer
      bgProps={{ grey: true }}
      header="Labs"
      headerProps={{ className: classes.labsHeader }}
      imgProps={{ src: photos.labs, className: classes.img }}
    />
    <SectionContainer
      height={300}
      header="Partners"
      headerProps={{ className: classes.partnersHeader }}
      imgProps={{ src: photos.partners, className: classes.img }}
    />
  </Body>
)
```

Enter fullscreen mode Exit fullscreen mode

So now if your boss ends up changing his mind and wants to make all of these sections about _300px_ in height, you only have _one_ place to change it.

Now i'm not trying to recommend a solution like this if we were looking to make a component supporting several use cases, this is for specific uses where we _know_ it is going to be re-used _only in_ that environment. A more dynamic re-usable solution for _SectionContainer_ that support multiple use cases would have probably been coded to be more generic like this, _still without_ changing the implementation:  

```
const SectionContainer = ({
  bgProps,
  sectionProps,
  children,
  gridContainerProps,
  gridColumnLeftProps,
  gridColumnRightProps,
  columnLeft,
  columnRight,
}) => (
  <Background {...bgProps}>
    <Section {...sectionProps}>
      {children || (
        <Grid spacing={16} container {...gridContainerProps}>
          <Grid xs={12} sm={6} item {...gridColumnLeftProps}>
            {columnLeft}
          </Grid>
          <Grid xs={12} sm={6} item {...gridColumnRightProps}>
            {columnRight}
          </Grid>
        </Grid>
      )}
    </Section>
  </Background>
)
```

Enter fullscreen mode Exit fullscreen mode

That way we now allow the developer to optionally extend any part of the components as needed while retaining the underlying implementation.

## [](#6-initializing-props-in-the-constructor)6\. Initializing Props in the constructor

When you initialize state in the constructor:  

```
import React from 'react'

class App extends React.Component {
  constructor(props) {
    super(props)
    this.state = {
      items: props.items,
    }
  }
}
```

Enter fullscreen mode Exit fullscreen mode

You might run into bugs. That's because the _constructor_ is only called _once_, which is the time the component first gets created.

The next time you try to change props, the state will retain its previous value because the constructor won't be getting called in re-renders.

If you haven't come across this problem yet, I hope this helps you!

And if you were wondering how to make the props synchronize with the state, a better approach would be something like this:  

```
import React from 'react'

class App extends React.Component {
  constructor(props) {
    super(props)
    // Initialize the state on mount
    this.state = {
      items: props.items,
    }
  }

  // Keep the state in sync with props in further updates
  componentDidUpdate = (prevProps) => {
    const items = []
    // after  calculations comparing prevProps with this.props
    if (...) {
      this.setState({ items })
    }
  }
}
```

Enter fullscreen mode Exit fullscreen mode

## [](#7-conditional-rendering-with-ampamp)7\. Conditional Rendering with _&&_

A common _gotcha_ when conditionally rendering components is using the && operator.

React will attempt to render _anything_ you provide as the alternative output if a condition doesn't meet its requirements. As such, when we look at this:  

```
const App = ({ items = [] }) => (
  <div>
    <h2>Here are your items:</h2>
    <div>
      {items.length &&
        items.map((item) => <div key={item.label}>{item.label}</div>)}
    </div>
  </div>
)
```

Enter fullscreen mode Exit fullscreen mode

This will actually render a number _0_ on the screen when _items.length_ is empty. JavaScript considers the number _0_ as a [falsey value](https://developer.mozilla.org/en-US/docs/Glossary/Falsy), so when _items_ is an empty array, the _&&_ operator won't be evaluating the expression to the right of it, and will just return the first value.

What I usually do if I want to keep the syntax is using double negation:  

```
const App = ({ items = [] }) => (
  <div>
    <h2>Here are your items:</h2>
    <div>
      {!!items.length &&
        items.map((item) => <div key={item.label}>{item.label}</div>)}
    </div>
  </div>
)
```

Enter fullscreen mode Exit fullscreen mode

That way, if _items_ is an empty array, react will not render anything on the screen if the evaluated output is a boolean.

## [](#8-not-spreading-previous-states)8\. Not Spreading Previous States

Something that can occasionally creep up to my list of bugs comes from carelessly implementing state update logic.

A recent situation involved react hooks, specifically a _useReducer_ implementation. Here's a basic example of this becoming an issue:  

```
const something = (state) => {
  let newState = { ...state }
  const indexPanda = newState.items.indexOf('panda')
  if (indexPanda !== -1) {
    newState.items.splice(indexPanda, 1)
  }
  return newState
}

const initialState = {
  items: [],
}

const reducer = (state, action) => {
  switch (action.type) {
    case 'add-item':
      return { ...state, items: [...something(state).items, action.item] }
    case 'clear':
      return { ...initialState }
    default:
      return state
  }
}
```

Enter fullscreen mode Exit fullscreen mode

When the _something_ function invokes and copies the state over, the underlying _items_ property has not changed. When we mutate it using _.splice_, this mutates _state.items_ and will introduce bugs.

Be especially weary about this in larger code. We would all probably get passed a small example like the above, but when things get messy, this _always_ has to be kept in mind at all times as it is easy to forget, especially when you're being pressured to ship code to production!

## [](#9-not-explicitly-passing-down-props-to-child-components)9\. Not Explicitly Passing Down Props To Child Components

It's a generally recommended practice to be explicit in the props you pass down to child components.

There are a couple good reasons for this:

1.  Easier Debugging Experience
    1.  You as a developer _know_ what is being passed to each child.
        1.  Other developers will also know that and will have an easier time reading the code
2.  Easier to Understand What a Component Will Do
    1.  Another great thing about passing down props explicity is that when you do this, it's also documenting your code in a way where everyone understands without even needing a formal documentation. And that _saves time_!
3.  There will be _fewer_ props needed in order to determine if the component should re-render or not.

Although there _can_ be some pretty neat use cases for spreading _all_ the props.

For example, if a parent quickly needed one or two things before passing the props down to child components, it can be easy for them (and you) to do so:  

```
const Parent = (props) => {
  if (props.user && props.user.email) {
    // Fire some redux action to update something globally that another
    //    component might need to know about
  }

  // Continue on with the app
  return <Child {...props} />
}
```

Enter fullscreen mode Exit fullscreen mode

Just make sure you don't find yourself in a situation like this:  

```
<ModalComponent
  open={aFormIsOpened}
  onClose={() => closeModal(formName)}
  arial-labelledby={`${formName}-modal`}
  arial-describedby={`${formName}-modal`}
  classes={{
    root: cx(classes.modal, { [classes.dialog]: shouldUseDialog }),
    ...additionalDialogClasses,
  }}
  disableAutoFocus
>
  <div>
    {!dialog.opened && (
      <ModalFormRoot
        animieId={animieId}
        alreadySubmitted={alreadySubmitted}
        academy={academy}
        user={user}
        clearSignature={clearSignature}
        closeModal={closeModal}
        closeImageViewer={closeImageViewer}
        dialog={dialog}
        fetchAcademyMember={fetchAcademyMember}
        formName={formName}
        formId={formId}
        getCurrentValues={getCurrentValues}
        header={header}
        hideActions={formName === 'signup'}
        hideClear={formName === 'review'}
        movieId={movie}
        tvId={tvId}
        openPdfViewer={openPdfViewer}
        onSubmit={onSubmit}
        onTogglerClick={onToggle}
        seniorMember={seniorMember}
        seniorMemberId={seniorMemberId}
        pdfViewer={pdfViewer}
        screenViewRef={screenViewRef}
        screenRef={screenRef}
        screenInputRef={screenInputRef}
        updateSignupFormValues={updateSignupFormValues}
        updateSigninFormValues={updateSigninFormValues}
        updateCommentFormValues={updateCommentFormValues}
        updateReplyFormValues={updateReplyFormValues}
        validateFormId={validateFormId}
        waitingForPreviousForm={waitingForPreviousForm}
        initialValues={getCurrentValues(formName)}
        uploadStatus={uploadStatus}
        uploadError={uploadError}
        setUploadError={setUploadError}
        filterRolesFalseys={filterRolesFalseys}
      />
    )}
  </div>
</ModalComponent>
```

Enter fullscreen mode Exit fullscreen mode

And if you do, consider splitting the component parts to separate components so that it's cleaner and more customizable.

## [](#10-prop-drilling)10\. Prop Drilling

Passing down props to multiple child components is what they call a _"code smell"_.

If you don't know what prop drilling is, it means when a parent is passing down props to _multiple levels of components_ deep down the tree.

Now the problem there isn't the parent nor the child. They _should keep their implementation_ the same. It's the _components in the middle_ that might become an issue in your react apps.

That's because now the components in the middle are tightly coupled and are exposed to too much information that they don't even need. The worst part is that when the parent re-renders, the _components in the middle will also re-render_, making a domino effect to all the child components down the chain.

A good solution is to use [context](https://reactjs.org/docs/context.html) instead. Or alternatively, _redux_ for props (which consequently are going to be serialized however).

## [](#conclusion)Conclusion

That concludes the end of this post :) I hope you found this article helpful to you, and make sure to follow me for future posts!

Follow me on [medium](https://medium.com/@jsmanifest) if you haven't already :)
