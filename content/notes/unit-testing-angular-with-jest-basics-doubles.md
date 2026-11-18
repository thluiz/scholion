---
title: "Unit testing Angular with Jest"
date: '2023-10-24T14:26:38+00:00'
category: webclip
summary: 'Explains how to set up Jest in an Angular project, write narrow unit tests, and use doubles and Angular’s DI/testing utilities to isolate dependencies and detect bugs early.'
tags: ["angular", "jest", "unit-testing", "test-doubles"]
has_commentary: false
generated_by: "openai/gpt-5.1"
sources:
  - title: "Unit testing Angular with Jest"
    url: "https://albertobasalo.medium.com/unit-testing-angular-with-jest-7de62ae2acd8"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2023-10/medium-com--unit-testing-angular-with-jest-basics-doubles.md"
    kind: repo
---

The article introduces using Jest instead of Karma/Jasmine for testing Angular apps, highlighting Jest’s speed, developer experience, and framework‑agnostic adoption. It walks through installing and configuring Jest in a clean Angular CLI repo, then shows how to write narrow unit tests for pure functions and classes, stressing clear naming, the AAA pattern, and the SUT concept. The text explains isolation, defines when to replace dependencies with doubles based on cost and reliability, and demonstrates creating Jest mocks.

The Angular section shows how to leverage Angular’s dependency injection and TestBed to wire real services and testing modules, and when to substitute them with doubles via providers. It includes examples for testing an HTTP‑based service with HttpClientTestingModule and HttpTestingController, and a facade that uses stubbed services and state, using jest.fn and jest.spyOn. The post closes by emphasizing that understanding why we test (finding bugs quickly and locating offending code) matters more than syntax, and points to future content on testing Angular components and handling the TypeScript/HTML mix.

## Reading notes

- Angular apps have traditionally used Karma and Jasmine for testing, but Jest has become a popular alternative in recent years.
- Main motivations for using Jest with Angular are better performance, developer experience, and being usable across different frameworks, not just Angular.
- The author assumes readers are proficient Angular developers with basic testing knowledge and refers to other articles for refreshing testing fundamentals.
- To add Jest to a clean Angular CLI repo, the first step is installing `jest`, `@types/jest`, and `jest-preset-angular` as dev dependencies.
- A `jest.config.json` file should be created using `jest-preset-angular` and referencing a `setup-jest.ts` file via `setupFilesAfterEnv`.
- The Jest setup file should import the Angular Jest preset from `jest-preset-angular/setup-jest`.
- The main `tsconfig.json` needs the `esModuleInterop` flag in `compilerOptions` so Jest and TypeScript work smoothly together.
- A `tsconfig.spec.json` should extend the main config, set an `outDir` for spec compilation, include Jest in `types`, and include `src/**/*.spec.ts` and `src/**/*.d.ts`.
- `package.json` test scripts can be wired to run Jest once (`"test": "jest"`) or in watch mode (`"test:watch": "jest --watch"`).
- The author distinguishes two emotional goals in testing: tests that give confidence when passing and tests that help locate the faulty line when failing.
- They advocate for testing as little code as possible to catch bugs early, preferring the term "narrow testing" over "unit testing" because it describes the goal without arguing about what a unit is.
- Domain libraries are suggested as a good starting point for tests because they are important, have fewer dependencies, and are easier to test.
- A pure function example illustrates Jest’s basic API: `describe` to group tests, `it` to define each test, and `expect` for assertions.
- The `getNewId` test checks that returned IDs are 12‑character hexadecimal strings and that successive calls produce different values.
- The `getSlug` test uses a list of edge‑case input/output pairs and iterates over them with `forEach`, asserting that the slug matches the expected string for each case.
- A class example shows testing a dependency‑free class, similar in spirit to the pure function tests.
- The author recommends the AAA (Arrange‑Act‑Assert) pattern in tests and marking those sections explicitly in the code comments.
- They use the SUT (System Under Test) acronym for the main object being tested and define input and expected values as SCREAMING_SNAKE_CASE constants like `INPUT_RESULT` and `EXPECTED_*`.
- In the `CommandState` example, `beforeEach` arranges a fresh instance before each test, ensuring test isolation.
- One test verifies that the `CommandState` instance is instantiable using a truthiness assertion.
- Another test checks `setStarted` by asserting that `isWorking` returns `true`, the `result` matches the initial input, and `error` is `null`.
- The article notes that a unit is usually defined as a piece of code that can be tested in isolation, which depends on the ability to run without external resources.
- It acknowledges that most code depends on other functions, libraries, services, or components, so isolation should be interpreted pragmatically.
- To test code with dependencies, the author introduces doubles, which are objects that replace real dependencies during tests.
- Dependencies are categorized along two dimensions: cost of execution (time and resources required) and reliability (likelihood of not failing).
- The guiding rule is to use doubles when a dependency is expensive to execute or when confidence in its reliability is low.
- Jest offers `jest.fn()` to create function doubles that return `undefined` by default and `jest.mock()` to produce mocked modules or objects.
- The author frames Jest testing skills as a foundation that applies to any framework or library beyond Angular.
- Angular’s built‑in dependency injection system is described as a powerful tool for injecting dependencies and for substituting them with doubles during tests.
- To use doubles with Angular DI, dependencies must be registered as providers in a module or TestBed configuration.
- Registering a provider allows replacing the actual dependency with a mock via `provide` and `useValue` properties.
- The author prefers explicitly defining mock providers that set both `provide` and `useValue` fields.
- Prior experience with Jest doubles helps in understanding Angular testing patterns, since the same mocking ideas transfer.
- In the `ActivitiesService` test suite, `TestBed.configureTestingModule` imports `HttpClientTestingModule` and registers `ActivitiesService` as a provider.
- The service instance and an `HttpTestingController` are obtained via `TestBed.inject`.
- An `afterEach` hook calls `httpTestingController.verify()` to ensure no unmatched HTTP requests remain after each test.
- A basic test confirms that `ActivitiesService` can be instantiated successfully.
- Another test calls `getActivities`, subscribes to the observable, and asserts the received activities array has length 2.
- That same test uses `httpTestingController.expectOne` with the expected URL to capture the outgoing HTTP request and checks that the HTTP method is `GET`.
- The test then flushes a `MOCK_RESULT` array so the observable completes with mock data.
- A further test verifies that calling `getByUserId('1')` triggers an HTTP request to `http://localhost:3000/activities?userId=1` and flushes the same mock result.
- The author notes that creating doubles is sometimes more challenging depending on the collaborators involved.
- When collaborating classes have already been tested and are considered trustworthy, the author suggests they can be used directly, even when the test is no longer a strict unit test.
- Such tests are still described as narrow tests because any failure should still localize the defect to the SUT class.
- In the `MyActivitiesFacade` tests, a `globalStateStub` exposes a `userId` method returning `'1'`.
- An `activitiesServiceStub` defines `getByUserId` and `putActivity` as `jest.fn()` mocks.
- `TestBed.configureTestingModule` provides `MyActivitiesFacade` and replaces `ActivitiesService` and `GlobalState` with the stubbed `useValue` implementations.
- The facade SUT is retrieved from the TestBed for use in each test.
- One test checks that `MyActivitiesFacade` is instantiable and truthy.
- Another test arranges `activitiesServiceStub.getByUserId` to return `of([])` and uses `jest.spyOn` to verify `getByUserId` is called when `getMyActivities` runs.
- A further test also arranges `getByUserId` to return `of([])` and then spies on the `execute` method of `getMyActivitiesState`, asserting it is called when `getMyActivities` executes.
- The sample code used in the article is available in a public GitHub repository for the author’s Angular development courses.
- The summary identifies creation and use of doubles as two key technical concepts covered in the post.
- The author stresses that the key aspect of testing is understanding why tests are written, which they see as detecting bugs as early as possible.
- For the author, an effective test should, when failing, direct attention to the specific piece of code causing the problem.
- Tools like Jest and Angular testing utilities are presented as necessary to learn, but only after grasping the principles behind testing.
- The author announces future posts that will cover testing Angular components, revisiting the unit versus integration test issue.
- They also foreshadow challenges involved in testing where TypeScript logic and HTML templates are combined.
