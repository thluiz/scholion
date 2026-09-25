---
url: "https://dev.to/wafa_bergaoui/applying-solid-principles-in-javascript-and-typescript-framework-2d1d?context=digest"
captured_at: "2026-09-25T01:20:49+01:00"
title: "Applying SOLID Principles in JavaScript and TypeScript Framework"
domain: "dev-to"
---

## [](#introduction)**Introduction**

The SOLID principles form the foundation of clean, scalable, and maintainable software development. Though these principles originated in Object-Oriented Programming (OOP), they can be effectively applied in JavaScript (JS) and TypeScript (TS) frameworks like React and Angular. This article explains each principle with real-life examples in both JS and TS.

* * *

## [](#1-single-responsibility-principle-srp)**1\. Single Responsibility Principle (SRP)**

**Principle:** A class or module should have only one reason to change. It should be responsible for a single piece of functionality.

*   **Example in JavaScript (React):**

In React, we often see components responsible for too many things—such as managing both UI and business logic.

**Anti-pattern:**  

```
function UserProfile({ userId }) {
  const [user, setUser] = useState(null);

  useEffect(() => {
    fetchUserData();
  }, [userId]);

  async function fetchUserData() {
    const response = await fetch(`/api/users/${userId}`);
    const data = await response.json();
    setUser(data);
  }

  return <div>{user?.name}</div>;
}

```

Enter fullscreen mode Exit fullscreen mode

Here, the **UserProfile** component violates SRP because it handles both UI rendering and data fetching.

**Refactor:**  

```
// Custom hook for fetching user data
function useUserData(userId) {
  const [user, setUser] = useState(null);

  useEffect(() => {
    async function fetchUserData() {
      const response = await fetch(`/api/users/${userId}`);
      const data = await response.json();
      setUser(data);
    }
    fetchUserData();
  }, [userId]);

  return user;
}

// UI Component
function UserProfile({ userId }) {
  const user = useUserData(userId); // Moved data fetching logic to a hook

  return <div>{user?.name}</div>;
}

```

Enter fullscreen mode Exit fullscreen mode

By using a **custom hook** **(useUserData)**, we separate the data-fetching logic from the UI, keeping each part responsible for a single task.

*   **Example in TypeScript (Angular):**

In Angular, services and components can become cluttered with multiple responsibilities.

**Anti-pattern:**  

```
@Injectable()
export class UserService {
  constructor(private http: HttpClient) {}

  getUser(userId: string) {
    return this.http.get(`/api/users/${userId}`);
  }

  updateUserProfile(userId: string, data: any) {
    // Updating the profile and handling notifications
    return this.http.put(`/api/users/${userId}`, data).subscribe(() => {
      console.log('User updated');
      alert('Profile updated successfully');
    });
  }
}

```

Enter fullscreen mode Exit fullscreen mode

This **UserService** has multiple responsibilities: fetching, updating, and handling notifications.

**Refactor:**  

```

@Injectable()
export class UserService {
  constructor(private http: HttpClient) {}

  getUser(userId: string) {
    return this.http.get(`/api/users/${userId}`);
  }

  updateUserProfile(userId: string, data: any) {
    return this.http.put(`/api/users/${userId}`, data);
  }
}

// Separate notification service
@Injectable()
export class NotificationService {
  notify(message: string) {
    alert(message);
  }
}

```

Enter fullscreen mode Exit fullscreen mode

By splitting the notification handling into a separate service (NotificationService), we ensure that each class has a single responsibility.

* * *

## [](#2-openclosed-principle-ocp)**2\. Open/Closed Principle (OCP)**

**Principle:** Software entities should be open for extension but closed for modification. This means that you should be able to extend the behavior of a module without altering its source code.

*   **Example in JavaScript (React):**

You might have a form validation function that works well but could require additional validation logic in the future.

**Anti-pattern:**  

```
function validate(input) {
  if (input.length < 5) {
    return 'Input is too short';
  }
  if (!input.includes('@')) {
    return 'Invalid email';
  }
  return 'Valid input';
}
```

Enter fullscreen mode Exit fullscreen mode

Whenever you need a new validation rule, you'd have to modify this function, violating OCP.

**Refactor:**  

```
function validate(input, rules) {
  return rules.map(rule => rule(input)).find(result => result !== 'Valid') || 'Valid input';
}

const lengthRule = input => input.length >= 5 ? 'Valid' : 'Input is too short';
const emailRule = input => input.includes('@') ? 'Valid' : 'Invalid email';

validate('test@domain.com', [lengthRule, emailRule]);
```

Enter fullscreen mode Exit fullscreen mode

Now, we can extend validation rules without modifying the original validate function, adhering to OCP.

*   **Example in TypeScript (Angular):**

In Angular, services and components should be designed to allow new features to be added without modifying the core logic.

**Anti-pattern:**  

```
export class NotificationService {
  send(type: 'email' | 'sms', message: string) {
    if (type === 'email') {
      // Send email
    } else if (type === 'sms') {
      // Send SMS
    }
  }
}
```

Enter fullscreen mode Exit fullscreen mode

This service violates OCP since you'd need to modify the send method every time you add a new notification type (e.g., push notifications).

**Refactor:**  

```
interface Notification {
  send(message: string): void;
}

@Injectable()
export class EmailNotification implements Notification {
  send(message: string) {
    // Send email logic
  }
}

@Injectable()
export class SMSNotification implements Notification {
  send(message: string) {
    // Send SMS logic
  }
}

@Injectable()
export class NotificationService {
  constructor(private notifications: Notification[]) {}

  notify(message: string) {
    this.notifications.forEach(n => n.send(message));
  }
}
```

Enter fullscreen mode Exit fullscreen mode

Now, adding new notification types only requires creating new classes without changing the NotificationService itself.

* * *

## [](#3-liskov-substitution-principle-lsp)**3\. Liskov Substitution Principle (LSP)**

**Principle:** Subtypes must be substitutable for their base types. Derived classes or components should be able to replace base classes without affecting the correctness of the program.

*   **Example in JavaScript (React):**

When using higher-order components (HOCs) or rendering different components conditionally, LSP helps ensure that all components behave predictably.

**Anti-pattern:**  

```
function Button({ onClick }) {
  return <button onClick={onClick}>Click me</button>;
}

function LinkButton({ href }) {
  return <a href={href}>Click me</a>;
}

// Inconsistent use of onClick and href makes substitution difficult
<Button onClick={() => {}} />;
<LinkButton href="/home" />;

```

Enter fullscreen mode Exit fullscreen mode

Here, and aren't interchangeable since they use different props (onClick vs href).

**Refactor:**  

```
function Actionable({ onClick, href, children }) {
  if (href) {
    return <a href={href}>{children}</a>;
  } else {
    return <button onClick={onClick}>{children}</button>;
  }
}

function Button({ onClick }) {
  return <Actionable onClick={onClick}>Click me</Actionable>;
}

function LinkButton({ href }) {
  return <Actionable href={href}>Go Home</Actionable>;
}

```

Enter fullscreen mode Exit fullscreen mode

Now both components (Button and LinkButton) are semantically correct, adhere to HTML accessibility standards, and behave consistently while following LSP.

*   **Example in TypeScript (Angular):**

**Anti-pattern:**  

```
class Rectangle {
  constructor(protected width: number, protected height: number) {}

  area() {
    return this.width * this.height;
  }
}

class Square extends Rectangle {
  constructor(size: number) {
    super(size, size);
  }

  setWidth(width: number) {
    this.width = width;
    this.height = width; // Breaks LSP
  }
}
```

Enter fullscreen mode Exit fullscreen mode

Modifying setWidth in Square violates LSP because Square behaves differently from Rectangle.

**Refactor:**  

```
class Shape {
  area(): number {
    throw new Error('Method not implemented');
  }
}

class Rectangle extends Shape {
  constructor(private width: number, private height: number) {
    super();
  }

  area() {
    return this.width * this.height;
  }
}

class Square extends Shape {
  constructor(private size: number) {
    super();
  }

  area() {
    return this.size * this.size;
  }
}
```

Enter fullscreen mode Exit fullscreen mode

Now, Square and Rectangle can be substituted without violating LSP.

* * *

## [](#4-interface-segregation-principle-isp)**4\. Interface Segregation Principle (ISP):**

**Principle:** Clients should not be forced to depend on interfaces they do not use.

*   **Example in JavaScript (React):**

React components sometimes receive unnecessary props, leading to tightly coupled and bulky code.

**Anti-pattern:**  

```
function MultiPurposeComponent({ user, posts, comments }) {
  return (
    <div>
      <UserProfile user={user} />
      <UserPosts posts={posts} />
      <UserComments comments={comments} />
    </div>
  );
}
```

Enter fullscreen mode Exit fullscreen mode

Here, the component depends on multiple props, even though it might not always use them.

**Refactor:**  

```
function UserProfileComponent({ user }) {
  return <UserProfile user={user} />;
}

function UserPostsComponent({ posts }) {
  return <UserPosts posts={posts} />;
}

function UserCommentsComponent({ comments }) {
  return <UserComments comments={comments} />;
}
```

Enter fullscreen mode Exit fullscreen mode

By splitting the component into smaller ones, each only depends on the data it actually uses.

*   **Example in TypeScript (Angular):**

**Anti-pattern:**  

```
interface Worker {
  work(): void;
  eat(): void;
}

class HumanWorker implements Worker {
  work() {
    console.log('Working');
  }
  eat() {
    console.log('Eating');
  }
}

class RobotWorker implements Worker {
  work() {
    console.log('Working');
  }
  eat() {
    throw new Error('Robots do not eat'); // Violates ISP
  }
}
```

Enter fullscreen mode Exit fullscreen mode

Here, RobotWorker is forced to implement an irrelevant eat method.

**Refactor:**  

```
interface Worker {
  work(): void;
}

interface Eater {
  eat(): void;
}

class HumanWorker implements Worker, Eater {
  work() {
    console.log('Working');
  }

  eat() {
    console.log('Eating');
  }
}

class RobotWorker implements Worker {
  work() {
    console.log('Working');
  }
}
```

Enter fullscreen mode Exit fullscreen mode

By separating Worker and Eater interfaces, we ensure that clients only depend on what they need.

* * *

## [](#5-dependency-inversion-principle-dip)**5\. Dependency Inversion Principle (DIP):**

**Principle:** High-level modules should not depend on low-level modules. Both should depend on abstractions (e.g., interfaces).

*   **Example in JavaScript (React):**

**Anti-pattern:**  

```
function fetchUser(userId) {
  return fetch(`/api/users/${userId}`).then(res => res.json());
}

function UserComponent({ userId }) {
  const [user, setUser] = useState(null);

  useEffect(() => {
    fetchUser(userId).then(setUser);
  }, [userId]);

  return <div>{user?.name}</div>;
}
```

Enter fullscreen mode Exit fullscreen mode

Here, UserComponent is tightly coupled with the fetchUser function.

**Refactor:**  

```
function UserComponent({ userId, fetchUserData }) {
  const [user, setUser] = useState(null);

  useEffect(() => {
    fetchUserData(userId).then(setUser);
  }, [userId, fetchUserData]);

  return <div>{user?.name}</div>;
}

// Usage
<UserComponent userId={1} fetchUserData={fetchUser} />;
```

Enter fullscreen mode Exit fullscreen mode

By injecting fetchUserData into the component, we can easily swap out the implementation for testing or different use cases.

*   **Example in TypeScript (Angular):**

**Anti-pattern:**  

```
@Injectable()
export class UserService {
  constructor(private http: HttpClient) {}

  getUser(userId: string) {
    return this.http.get(`/api/users/${userId}`);
  }
}

@Injectable()
export class UserComponent {
  constructor(private userService: UserService) {}

  loadUser(userId: string) {
    this.userService.getUser(userId).subscribe(user => console.log(user));
  }
}
```

Enter fullscreen mode Exit fullscreen mode

UserComponent is tightly coupled with UserService, making it hard to swap out UserService.

**Refactor:**  

```
interface UserService {
  getUser(userId: string): Observable<User>;
}

@Injectable()
export class ApiUserService implements UserService {
  constructor(private http: HttpClient) {}

  getUser(userId: string) {
    return this.http.get<User>(`/api/users/${userId}`);
  }
}

@Injectable()
export class UserComponent {
  constructor(private userService: UserService) {}

  loadUser(userId: string) {
    this.userService.getUser(userId).subscribe(user => console.log(user));
  }
}
```

Enter fullscreen mode Exit fullscreen mode

By depending on an interface (UserService), UserComponent is now decoupled from the concrete implementation of ApiUserService.

* * *

## [](#next-steps)**Next Steps**

Whether you're working on the front end with frameworks like React or Angular, or on the back end with Node.js, the SOLID principles serve as a guide to ensure that your software architecture remains solid.

To fully integrate these principles into your projects:

*   **Practice regularly:** Refactor existing codebases to apply SOLID principles and review code for adherence.
*   **Collaborate with your team:** Encourage best practices through code reviews and discussions around clean architecture.
*   **Stay curious:** SOLID principles are just the beginning. Explore other architectural patterns like MVC, MVVM, or CQRS that build on these fundamentals to further improve your designs.

* * *

## [](#conclusion)**Conclusion**

The SOLID principles are highly effective for ensuring that your code is clean, maintainable, and scalable, even in JavaScript and TypeScript frameworks like React and Angular. Applying these principles enables developers to write flexible and reusable code that’s easy to extend and refactor as requirements evolve. By following SOLID, you can make your codebase robust and ready for future growth.
