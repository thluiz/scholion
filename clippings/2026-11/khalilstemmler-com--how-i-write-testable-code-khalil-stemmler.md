---
url: "https://khalilstemmler.com/articles/software-design-architecture/write-testable-code"
captured_at: "2026-11-16T02:26:18+00:00"
title: "How I Write Testable Code | Khalil's Simple Methodology | Khalil Stemmler"
domain: "khalilstemmler-com"
---

[Software Design](https://khalilstemmler.com/articles/categories/software-design)

Last updated

Invalid date

The single biggest thing that improved the quality of my designs was understanding how dependencies influence my ability to write tests. In this article, I'll show you how I write testable code.

  
![](https://khalilstemmler.com/img/blog/software-architecture-design/testable-code/testable-code.png)

Understanding how to write testable code is one of the biggest frustrations I had when I finished school and started working at my first real-world job.

Today, while working on a chapter in [solidbook.io](https://solidbook.io/), breaking down some code and picking apart everything wrong with it, I realized that several principles govern how I write code to be testable.

In this article, I want to present you with a straightforward methodology you can apply to both front-end and back-end code for how to write testable code.

## Prerequisite readings[](#Prerequisite-readings)

You may want to read the following pieces beforehand. 😇

*   [Dependency Injection & Inversion Explained | Node.js w/ TypeScript](https://khalilstemmler.com/articles/tutorials/dependency-injection-inversion-explained/)
*   [The Dependency Rule](https://khalilstemmler.com/wiki/dependency-rule/)
*   [The Stable Dependency Principle - SDP](https://khalilstemmler.com/wiki/stable-dependency-principle/)

## Dependencies are relationships[](#Dependencies-are-relationships)

You may already know this, but the first thing to understand is that when we import or _even mention_ the name of another class, function, or variable from one class (let's call this the _source class_), whatever was mentioned becomes a dependency to the source class.

In the [dependency inversion & injection article](https://khalilstemmler.com/articles/tutorials/dependency-injection-inversion-explained/), we looked at an example of a `UserController` that needed access to a `UserRepo` to **get all users**.

controllers/userController.ts

```
import { UserRepo } from '../repos' // Bad

/**
 * @class UserController
 * @desc Responsible for handling API requests for the
 * /user route.
 **/

class UserController {
  private userRepo: UserRepo;

  constructor () {
    this.userRepo = new UserRepo(); // Also bad.
  }

  async handleGetUsers (req, res): Promise<void> {
    const users = await this.userRepo.getUsers();
    return res.status(200).json({ users });
  }
}
```

The problem with this approach was that when we do this, we create a hard **source-code dependency**.

The relationship looks like the following:

![](https://khalilstemmler.com/img/blog/di-container/before-dependency-inversion.svg)

UserController relies directly on UserRepo.

This means that if we ever wanted to test `UserController`, we'd need to bring `UserRepo` along for the ride as well. The thing about `UserRepo`, though, is that it also brings a whole damn database connection with it as well. And that's no good.

If we need to spin up a database to run unit tests, that makes all our unit tests slow.

Ultimately, we can fix this by using **dependency inversion**, putting an abstraction between the two dependencies.

**Abstractions** that can invert the flow of dependencies are either _interfaces_ or _abstract classes_.

![](https://khalilstemmler.com/img/blog/di-container/after-dependency-inversion.svg)

Using an interface to implement Dependency Inversion.

This works by placing an abstraction (interface or abstract class) in between the dependency you want to import and the source class. The source class imports the abstraction, and remains testable because we can pass in _anything_ that has adhered to the contract of the abstraction, even if it's a _mock object_.

controllers/userController.ts

```
import { IUserRepo } from '../repos' // Good! Refering to the abstraction.

/**
 * @class UserController
 * @desc Responsible for handling API requests for the
 * /user route.
 **/

class UserController {
  private userRepo: IUserRepo; // abstraction here

  constructor (userRepo: IUserRepo) { // and here
    this.userRepo = userRepo;
  }

  async handleGetUsers (req, res): Promise<void> {
    const users = await this.userRepo.getUsers();
    return res.status(200).json({ users });
  }
}
```

In our scenario with `UserController`, it now refers to an `IUserRepo` interface (which costs nothing) rather than referring to the potentially heavy `UserRepo` that carries a db connection with it everywhere it goes.

If we wish to test the controller, we can satisfy the `UserController`'s need for an `IUserRepo` by substituting our db-backed `UserRepo` for an _in-memory implementation_. We can create one like this:

```
class InMemoryMockUserRepo implements IUserRepo { 
  ... // implement methods and properties
}
```

## The methodology[](#The-methodology)

Here's my thought process for keeping code testable. It all starts when you want to create a relationship from one class to another.

> Start: You want to import or mention the name of a class from another file.

Question: do you care about being able to write tests against the _source class_ in the future?

If **no**, go ahead and import whatever it is because it doesn't matter.

If **yes**, consider the following restrictions. You may depend on the class only if it is _at least one_ of these:

*   The dependency is an abstraction (interface or abstract class).
*   The dependency is from the same layer or an inner layer (see [The Dependency Rule](https://khalilstemmler.com/wiki/dependency-rule/)).
*   It is a [stable dependency](https://khalilstemmler.com/wiki/stable-dependency-principle/).

> If at _least one_ of these conditions passes, import the dependency- otherwise, don't.

Importing the dependency introduces the possibility that it will be hard to test that component in the future.

Again, you can fix scenarios where the dependency breaks one of those rules by using [Dependency Inversion](https://khalilstemmler.com/articles/tutorials/dependency-injection-inversion-explained/).

## Front-end example (React w/ TypeScript)[](#Front-end-example-React-w-TypeScript)

What about front-end development?

The same rules apply!

Take this React component (pre-hooks) involving a _container component_ (inner layer concern) that depends on a `ProfileService` (outer layer - infra).

containers/ProfileContainer.tsx

```
import * as React from 'react'
import { ProfileService } from './services'; // hard source-code dependencyimport { IProfileData } from './models'      // stable dependency

interface ProfileContainerProps {}

interface ProfileContainerState {
  profileData: IProfileData | {};
}

export class ProfileContainer extends React.Component<
  ProfileContainerProps, 
  ProfileContainerState
> {

  private profileService: ProfileService;

  constructor (props: ProfileContainerProps) {
    super(props);
    this.state = {
      profileData: {}
    }
    this.profileService = new ProfileService(); // Bad.  }

  async componentDidMount () {
    try {
      const profileData: IProfileData = await this.profileService.getProfile();
      this.setState({
        ...this.state,
        profileData
      })
    } catch (err) {
      alert("Ooops")
    }
  }

  render () {
    return (
      <div>Im a profile container</div>
    )
  }
}
```

If `ProfileService` is something that makes network calls to a RESTful API, there's no way for us to test `ProfileContainer` and prevent it from making real API calls.

We can fix this by doing two things:

### 1\. Putting an interface in between the `ProfileService` and `ProfileContainer`[](#1-Putting-an-interface-in-between-the-ProfileService-and-ProfileContainer)

First, we create the abstraction and then ensure that `ProfileService` implements it.

services/index.tsx

```
import { IProfileData } from "../models";

// Create an abstraction
export interface IProfileService {   getProfile: () => Promise<IProfileData>;}
// Implement the abstraction
export class ProfileService implements IProfileService {  async getProfile(): Promise<IProfileData> {
    ...
  }
}
```

An abstraction for ProfileService in the form of an interface.

Then we update `ProfileContainer` to rely on the abstraction instead.

containers/ProfileContainer.tsx

```
import * as React from 'react'
import { 
  ProfileService, 
  IProfileService } from './services'; // import interface
import { IProfileData } from './models' 

interface ProfileContainerProps {}

interface ProfileContainerState {
  profileData: IProfileData | {};
}

export class ProfileContainer extends React.Component<
  ProfileContainerProps, 
  ProfileContainerState
> {

  private profileService: IProfileService;

  constructor (props: ProfileContainerProps) {
    super(props);
    this.state = {
      profileData: {}
    }
    this.profileService = new ProfileService(); // Still bad though  }

  async componentDidMount () {
    try {
      const profileData: IProfileData = await this.profileService.getProfile();
      this.setState({
        ...this.state,
        profileData
      })
    } catch (err) {
      alert("Ooops")
    }
  }

  render () {
    return (
      <div>Im a profile container</div>
    )
  }
}
```

### 2\. Compose a `ProfileContainer` with a HOC that contains a valid `IProfileService`.[](#2-Compose-a-ProfileContainer-with-a-HOC-that-contains-a-valid-IProfileService)

Now we can create HOCs that use whatever kind of `IProfileService` we wish. It could be the one that connects to an API like what follows:

hocs/withProfileService.tsx

```
import React from "react";
import { ProfileService } from "../services";
interface withProfileServiceProps {}

function withProfileService(WrappedComponent: any) {
  class HOC extends React.Component<withProfileServiceProps, any> {
    private profileService: ProfileService;
    constructor(props: withProfileServiceProps) {
      super(props);
      this.profileService = new ProfileService();    }

    render() {
      return (
        <WrappedComponent
          profileService={this.profileService}          {...this.props}
        />
      );
    }
  }
  return HOC;
}

export default withProfileService;
```

Or it could be a mock one that uses an in-memory profile service as well.

hocs/withMockProfileService.tsx

```
import * as React from "react";
import { MockProfileService } from "../services";
interface withProfileServiceProps {}

function withProfileService(WrappedComponent: any) {
  class HOC extends React.Component<withProfileServiceProps, any> {
    private profileService: MockProfileService;
    constructor(props: withProfileServiceProps) {
      super(props);
      this.profileService = new MockProfileService();    }

    render() {
      return (
        <WrappedComponent
          profileService={this.profileService}          {...this.props}
        />
      );
    }
  }
  return HOC;
}

export default withProfileService;
```

For our `ProfileContainer` to utilize the `IProfileService` from an HOC, it has to expect to receive an `IProfileService` as a prop within `ProfileContainer` rather than being added to the class as an attribute.

containers/ProfileContainer.tsx

```
import * as React from "react";
import { IProfileService } from "./services";import { IProfileData } from "./models";

interface ProfileContainerProps {
  profileService: IProfileService;}

interface ProfileContainerState {
  profileData: IProfileData | {};
}

export class ProfileContainer extends React.Component<
  ProfileContainerProps,
  ProfileContainerState
> {
  constructor(props: ProfileContainerProps) {
    super(props);
    this.state = {
      profileData: {}
    };
  }

  async componentDidMount() {
    try {
      const profileData: IProfileData = await this.props.profileService.getProfile();
      this.setState({
        ...this.state,
        profileData
      });
    } catch (err) {
      alert("Ooops");
    }
  }

  render() {
    return <div>Im a profile container</div>
  }
}
```

Finally, we can compose our `ProfileContainer` with whichever HOC we want- the one containing the real service, or the one containing the fake service for testing.

```
import * as React from "react";
import { render } from "react-dom";
import withProfileService from "./hocs/withProfileService";import withMockProfileService from "./hocs/withMockProfileService";import { ProfileContainer } from "./containers/profileContainer";

// The real service
const ProfileContainerWithService = withProfileService(ProfileContainer);// The mock service
const ProfileContainerWithMockService = withMockProfileService(ProfileContainer);
class App extends React.Component<{}, IState> {
  public render() {
    return (
      <div>
        <ProfileContainerWithService />      </div>
    );
  }
}

render(<App />, document.getElementById("root"));
```

* * *

  

### Stay in touch!

Join 20000+ value-creating Software Essentialists getting actionable advice on how to master what matters each week. 🖖

View more in [Software Design](https://khalilstemmler.com/articles/categories/software-design)

  

* * *
