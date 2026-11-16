---
url: "https://dev.to/aumayeung/how-to-speed-up-angular-tests-5e5h"
captured_at: "2026-11-16T19:19:56+00:00"
title: "How to Speed Up Angular Tests"
domain: "dev-to"
---

[![John Au-Yeung](https://media2.dev.to/dynamic/image/width=50,height=50,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F302439%2F26242d08-e738-4741-bde5-2ec03569764c.jpg)](https://dev.to/aumayeung)

**Subscribe to my email list now at [http://jauyeung.net/subscribe/](http://jauyeung.net/subscribe/)**

**Follow me on Twitter at [https://twitter.com/AuMayeung](https://twitter.com/AuMayeung)**

**Many more articles at [https://medium.com/@hohanga](https://medium.com/@hohanga)**

By default, Angular tests run very slowly because a lot of dependencies are injected and components being tested are reloaded when each test is run.

As a result, you get tests that take 30 minutes or more to run.

It is bad enough that an issue is opened on GitHub about it [https://github.com/angular/angular/issues/12409](https://github.com/angular/angular/issues/12409).

To remedy this, we have to load all the dependencies only once when each test file is executed and then let the test run without reloading everything again.

We make a new spec file called `spec-helper.spec.ts` and add the following:  

```
export const beforeTest=()=> {
  beforeAll((done)=> (async ()=> {
    TestBed.resetTestingModule();
    TestBed.configureTestingModule({
      declarations: [
        AppComponent,
        LoginPageComponent,
        MonitorPageComponent,
        SettingsPageComponent,
        AccountsPageComponent,
        TopBarComponent,
        SignUpPageComponent,
        ImagesPageComponent,
        AccountDialogComponent
      ],
      imports: [
        BrowserModule,
        BrowserAnimationsModule,
        MatButtonModule,
        MatCheckboxModule,
        MatToolbarModule,
        MatInputModule,
        MatSidenavModule,
        MatIconModule,
        MatListModule,
        MatTableModule,
        MatDialogModule,
        MatGridListModule,
        RouterTestingModule.withRoutes(appRoutes),
        FormsModule,
        StoreModule.forRoot({
          openSideNav: openSideNavReducer
        }),
        ClickOutsideModule,
        HttpClientTestingModule,
        CustomFormsModule
      ],
      providers: [
        UserService,
        SecurityService,
        AuthenticatedGuard,
        {
          provide: HTTP_INTERCEPTORS,
          useClass: HttpReqInterceptor,
          multi: true
        },
        {
          provide: MatDialogRef,
          useValue: {}
        },
        {
          provide: MAT_DIALOG_DATA,
          useValue: []
        },
      ],
    })
    await TestBed.compileComponents();
    // prevent Angular from resetting testing module
    TestBed.resetTestingModule=()=> TestBed;
  })().then(done).catch(done.fail));
}
```

Enter fullscreen mode Exit fullscreen mode

given all these items exist in our code and libraries. The file will include all the dependencies and code in our Angular module.

Then we import the file in our specs and run the `beforeTest` function that we exported.

After this, our unit tests will run orders of magnitude faster, from 30 minutes down to a few seconds.

Also, now we don't have to worry about including our dependencies in every test file and worry about missing dependencies for every test module.
