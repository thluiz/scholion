---
url: "https://albertobasalo.medium.com/unit-testing-angular-with-jest-7de62ae2acd8"
captured_at: "2023-10-24T14:26:38+00:00"
title: "Unit testing Angular with Jest"
domain: "medium-com"
---

Angular
Jest
Testing
Unit testing Angular with Jest
Alberto Basalo
Jul 23, 2023



Traditionally, Angular applications were tested with Karma and Jasmine. But, in the last years, Jest has become a popular alternative.

The main reasons for using Jest with angular are:

Jest is faster, has a better developer experience, and has wider usage by not being specific to a single framework.


In this post, I will introduce you to the foundations to test with Jest and how you can use it in your Angular applications.

🎒Prerequisites
Proficient as an Angular developer
Basic knowledge of testing (read my other articles if you need to refresh something)
Test your TypeScript code with ease.
Learn how to test TypeScript code effectively and confidently with a solid grasp of testing principles.

albertobasalo.medium.com

🌲 Jest, installation, and configuration.

I will start adding Jest to a clean CLI repo (without Karma…). In case you have installed the official testing framework, you only need to remove it as a final step.

So, start by installing any dependency needed.

npm install jest @types/jest jest-preset-angular --save-dev

The first step is to create a jest.config.json file, fill it with the Angular preset, and point to the next configuration setup.

{
  "preset": "jest-preset-angular,"
  "setupFilesAfterEnv": ["<rootDir>/setup-jest.ts"]
}

Now add thejest.config.json and import the Angular preset

import 'jest-preset-angular/setup-jest';

At your current tsconfig.jsonfile adds this flag to allow Jest and Typescript to be friends.

{
  "compilerOptions": {
    "esModuleInterop": true
  }
}

Create or fill thetsconfig.spec.jsonfile with the types info and the name pattern to discover tests.

{
  "extends": "./tsconfig.json",
  "compilerOptions": {
    "outDir": "./out-tsc/spec",
    "types": ["jest"]
  },
  "include": ["src/**/*.spec.ts", "src/**/*.d.ts"]
}

Finally, go to package.json and add the following scripts to start Jest as you wish.

{
  "scripts": {
    "test": "jest",
    "test:watch": "jest --watch"
  }
}
1️⃣ Writing unit tests with just Jest.

When writing tests, you are looking for two different emotions: joy and pain. Let me explain. Some tests are meant to give you the confidence that your code works as expected when it passes. On the other hand, some tests can pinpoint the exact line of code causing the problem when failing.

Narrow tests for business logic.

Each type of test has its pros and cons. But if you want to ensure the code doesn’t break and find any bugs as soon as possible, then you should test as little code as possible.

For this case, I prefer the term narrow testing over unit testing because it is more descriptive of the goal of the tests and does not set any expectations about what a unit is. Despite that, you and I can interchangeably use the terms unit testing and narrow testing.

Time to write code. I will start with the domain libraries because they are the most important ones and have fewer dependencies, making them easier to test. Win-win.

The first sample is a simple test for a pure function. It is a function that does not depend on any external resource and always returns the same result for the same input.

Getting familiar with the Jest syntax is easy. The describe function is used to group tests, and theit function defines a test. The expectfunction is used to make assertions.

describe('The getNewId function', function () {
  it('should produce hexadecimal strings of 12 chars', function () {
    const actualId = getNewId();
    expect(actualId).toMatch(/^[0-9a-f]+$/);
    expect(actualId.length).toBe(12);
  });
  it('should produce unique ids', function () {
    const oneId = getNewId();
    const otherId = getNewId();
    expect(oneId).not.toBe(otherId);
  });
});

describe('The getSlug function', function () {
  it('should return the correct slug for each edge cases', function () {
    const SAMPLE_CASES = [
      ['This is a Test 123', 'this_is_a_test_123'],
      ['This is Español', 'this_is_espa-ol'],
      ['This is a Test with spaces', 'this_is_a_test_with_spaces'],
      ['This has inv@lid chars', 'this_has_inv-lid_chars'],
    ];
    SAMPLE_CASES.forEach(([source, expected]) => {
      const actualSlug = getSlug(source);
      expect(actualSlug).toBe(expected);
    });
  });
});

The second sample is a test for a class. It is a class that does not depend on any external resource and always returns the same result for the same input. So very similar to the previous one.

I want to introduce some practices I use in my tests, like the AAA pattern and naming conventions.

I like to use theSUTacronym to refer to the System Under Test. It is a common practice in the testing community. Also, I use the INPUT_* constants to define the input values and the EXPECTED_* constants to define the expected values. Both in SCREAMING_SNAKE_CASE.

describe('The CommandState class', () => {
  const INPUT_RESULT = { data: 'input' };
  const INPUT_NULL = { data: '' };
  const INPUT_ERROR = { message: 'error' };
  let commandStateSUT: CommandState<{ data: string }>;
  beforeEach(() => {
    // Arrange
    commandStateSUT = new CommandState(INPUT_NULL);
  });
  it('should create be instantiable', () => {
    expect(commandStateSUT) // Act
      .toBeTruthy(); // Assert
  });
  it('should set correct states when setStarted is called', () => {
    // Act
    commandStateSUT.setStarted();
    // Assert
    expect(commandStateSUT.isWorking()).toBe(true);
    expect(commandStateSUT.result()).toBe(INPUT_NULL);
    expect(commandStateSUT.error()).toBeNull();
  });
});

Isolation and unit testing

So far, I’ve been talking about unit testing, but I haven’t explained what a unit is. The most accepted definition tells us that a unit is a piece of code that can be tested isolated. This brings us to isolation as the ability to work without depending on any external resource.

Almost all the code that we write depends on other resources. A function calling another function, a class using a library, a component instantiating a service, etc. So isolation should be taken in a more relaxed way.

How can we test a piece of code that depends on other resources? The answer is using doubles.

When and how to use doubles.

Doubles are objects that replace the real dependencies in the tests. And what about dependencies? Are all of them equal? No, they are not. I like to classify collaborators in two dimensions: cost of execution and reliability.


The cost of execution is the time and resources it takes to execute the dependency. The reliability value means the confidence or probability that the dependency does not fail.

With this classification in mind, we can decide when to use doubles and real dependencies. The rule is simple: use doubles when the cost is high or the confidence is low.

Creating a double with Jest is easy. You can use the jest.fn() function to create a double that returns undefined by default. Or you can use the jest.mock() function to create a double that returns a mock object.

I hope you can get a grasp of what testing with Jest is. This is a good foundation for any framework or library. But, if you are using Angular, you can use the Angular testing tools to make your life easier.

🅰️ Angular Inversion of Control.

Angular has a built-in dependency injection system, a powerful tool allowing you to inject dependencies in your classes. And it is the perfect tool for using doubles.

To do so, you must return to your Module knowledge and register the dependencies as providers. Any element of the provider’s array will allow substituting the actual dependency with a double.

I like explicitly creating a provider mock with filled provide and useValue properties. Any prior experience using Jest to create doubles will help you to understand this code.

describe('ActivitiesService', () => {
  let activitiesService: ActivitiesService;
  let httpTestingController: HttpTestingController;
  const MOCK_RESULT: any[] = [
    { id: 1, name: 'Activity 1' },
    { id: 2, name: 'Activity 2' },
  ];

  beforeEach(() => {
    TestBed.configureTestingModule({
      imports: [HttpClientTestingModule],
      providers: [ActivitiesService],
    });

    activitiesService = TestBed.inject(ActivitiesService);
    httpTestingController = TestBed.inject(HttpTestingController);
  });

  afterEach(() => {
    httpTestingController.verify();
  });

  it('should be instantiable', () => {
    expect(activitiesService).toBeTruthy();
  });

  it('should get the activities from the expected endpoint', () => {
    // Act
    activitiesService.getActivities().subscribe((activities) => {
      expect(activities.length).toBe(2);
    });
    // Assert
    const expectedUrl = 'http://localhost:3000/activities';
    const req = httpTestingController.expectOne(expectedUrl);
    expect(req.request.method).toEqual('GET');
    // Arrange
    req.flush(MOCK_RESULT);
  });

  it('should call the api filtering by userId', () => {
    // Act
    activitiesService.getByUserId('1').subscribe();
    // Assert
    const expectedUrl = 'http://localhost:3000/activities?userId=1';
    const req = httpTestingController.expectOne(expectedUrl);
    // Arrange
    req.flush(MOCK_RESULT);
  });
});

Sometimes creating doubles is trickier.

At this point, you should have confidence in both classes, as they have been tested before. In such cases, you can use them as they are. It is arguable that you can still consider such a unit test, but it is definitely a narrow test because the offending code must be in the SUT class when it fails.

describe('MyActivitiesFacade', () => {
  let myActivitiesFacadeSUT: MyActivitiesFacade;
  const globalStateStub = {
    userId: () => '1',
  };
  const activitiesServiceStub = {
    getByUserId: jest.fn(),
    putActivity: jest.fn(),
  };

  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [
        MyActivitiesFacade,
        {
          provide: ActivitiesService,
          useValue: activitiesServiceStub,
        },
        {
          provide: GlobalState,
          useValue: globalStateStub,
        },
      ],
    });
    myActivitiesFacadeSUT = TestBed.inject(MyActivitiesFacade);
  });

  it('should be instantiable', () => {
    expect(myActivitiesFacadeSUT).toBeTruthy();
  });

  it('should call the service to get the activities', () => {
    // Arrange
    activitiesServiceStub.getByUserId.mockReturnValue(of([]));
    const getByUserIdSpy = jest.spyOn(activitiesServiceStub, 'getByUserId');
    // Act
    myActivitiesFacadeSUT.getMyActivities();
    // Assert
    expect(getByUserIdSpy).toHaveBeenCalled();
  });

  it('should call the state to execute the command', () => {
    // Arrange
    activitiesServiceStub.getByUserId.mockReturnValue(of([]));
    const executeSpy = jest.spyOn(
      myActivitiesFacadeSUT.getMyActivitiesState,
      'execute'
    );
    // Act
    myActivitiesFacadeSUT.getMyActivities();
    // Assert
    expect(executeSpy).toHaveBeenCalled();
  });
});

Find the code used in this post here:

GitHub - AlbertoBasalo/ng-dev: 🅰️ Sample code for Angular development courses by…
🅰️ Sample code for Angular development courses by https://albertobasalo.dev - GitHub - AlbertoBasalo/ng-dev: 🅰️…

github.com

🌅 Summary

In this post, you have learned two important technical concepts: how to create doubles and how to use them to test your code.

But the important point is not related to syntax. It is to reason why we write these tests. And for me that reason is cristal clear: detect bugs as soon as possible. To do so, I only need one thing, when the test fails, it should point me to the offending code.

Of course, writing tests means using and learning tools like Jest or Angular specifics. But before you must understand the principles behind testing.

In the following posts, I will teach you how to test your Angular components, your next step in the testing pyramid. We will face the unit vs. integration test dilemma again.

And another challenge: the technology mixing of TypeScript and HTML.
