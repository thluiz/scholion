---
url: "https://dev.to/aumayeung/build-a-native-desktop-app-with-angular-and-electron-2259"
captured_at: "2026-11-16T00:43:42+00:00"
title: "Build a Native Desktop App with Angular and Electron"
domain: "dev-to"
---

**Subscribe to my email list now at [http://jauyeung.net/subscribe/](http://jauyeung.net/subscribe/)**

**Follow me on Twitter at [https://twitter.com/AuMayeung](https://twitter.com/AuMayeung)**

**Many more articles at [https://medium.com/@hohanga](https://medium.com/@hohanga)**

Electron is a JavaScript framework that allows you to build cross-platform apps by converting a web app into a native app for the supported platforms. This provides a convenient way for web developers to write software for the platform that they are not familiar with by using web technologies. By using Node.js, it supports some native functionality like file manipulation and hardware interaction. Electron has been getting more popular over time, and now it is used for companies like Slack and Microsoft to develop their popular apps.

Angular is a popular framework for building web apps, and it has a powerful CLI that makes the building process seamless. However, it does not support building an app into an Electron without some changes. There is an Angular Electron [boilerplate repository](https://github.com/maximegris/angular-electron) that combines the 2, making it easy for you to get started.

In this story, we will build an Electron app based on Angular which gets news headlines from the New York Times API, located at [https://developer.nytimes.com/](https://developer.nytimes.com/). To use it, you have to register for a free API key.

The API supports CORS, so front-end apps from domains outside of nytimes.com can access their APIs. This means that we can build an Angular app with it. To build our app, you have to go to the website and register for an API key.

To start building the app, we install the Angular CLI by running `npm i -g @angular/cli`. After that, instead of running `ng new` to create the project, we check out the `angular-electron` repo located at [https://github.com/maximegris/angular-electron.git](https://github.com/maximegris/angular-electron.git) and use the latest version on the master branch.

Next, copy the code into your own project folder. Now we can start building the app. To start, we rename the app name to `new-york-times`. The renaming has to be done in multiple files: `electron-builer.json`, `package.json`, `angular.json`.

In `electron-builder.json`, we replace the existing code with the following:  

```
{  
  "productName": "new-york-times",  
  "directories": {  
    "output": "release/"  
  },  
    "files": [  
        "**/*",  
        "!**/*.ts",  
        "!*.code-workspace",  
        "!LICENSE.md",  
        "!package.json",  
        "!package-lock.json",  
        "!src/",  
        "!e2e/",  
        "!hooks/",  
        "!angular.json",  
        "!_config.yml",  
        "!karma.conf.js",  
        "!tsconfig.json",  
        "!tslint.json"  
    ],  
  "win": {  
    "icon": "dist",  
    "target": [  
      "portable"  
    ]  
  },  
  "mac": {  
    "icon": "dist",  
    "target": [  
      "dmg"  
    ]  
  },  
  "linux": {  
    "icon": "dist",  
    "target": [  
      "AppImage"  
    ]  
  }  
}
```

Note the `productName`’s value is different from the original.

Then in `package.json`, we replace the existing code with:  

```
{
  "name": "new-york-times",
  "version": "1.0.0",
  "description": "Angular 8 with Electron (Typescript + SASS + Hot Reload)",
  "homepage": "https://github.com/maximegris/angular-electron",
  "author": {
    "name": "Maxime GRIS",
    "email": "maxime.gris@gmail.com"
  },
  "keywords": [
    "angular",
    "angular 8",
    "electron",
    "typescript",
    "sass"
  ],
  "main": "main.js",
  "private": true,
  "scripts": {
    "postinstall": "npm run postinstall:electron && electron-builder install-app-deps",
    "postinstall:web": "node postinstall-web",
    "postinstall:electron": "node postinstall",
    "ng": "ng",
    "start": "npm run postinstall:electron && npm-run-all -p ng:serve electron:serve",
    "build": "npm run postinstall:electron && npm run electron:serve-tsc && ng build --base-href ./",
    "build:dev": "npm run build -- -c dev",
    "build:prod": "npm run build -- -c production",
    "ng:serve": "ng serve",
    "ng:serve:web": "npm run postinstall:web && ng serve -o",
    "electron:serve-tsc": "tsc -p tsconfig-serve.json",
    "electron:serve": "wait-on http-get://localhost:4200/ && npm run electron:serve-tsc && electron . --serve",
    "electron:local": "npm run build:prod && electron .",
    "electron:linux": "npm run build:prod && electron-builder build --linux",
    "electron:windows": "npm run build:prod && electron-builder build --windows",
    "electron:mac": "npm run build:prod && electron-builder build --mac",
    "test": "npm run postinstall:web && ng test",
    "e2e": "npm run build:prod && mocha --timeout 300000 --require ts-node/register e2e/**/*.spec.ts",
    "version": "conventional-changelog -i CHANGELOG.md -s -r 0 && git add CHANGELOG.md",
    "lint": "ng lint"
  },
  "devDependencies": {
    "@angular-devkit/build-angular": "0.802.2",
    "@angular/cli": "8.2.2",
    "@angular/common": "8.2.2",
    "@angular/compiler": "8.2.2",
    "@angular/compiler-cli": "8.2.2",
    "@angular/core": "8.2.2",
    "@angular/forms": "8.2.2",
    "@angular/language-service": "8.2.2",
    "@angular/platform-browser": "8.2.2",
    "@angular/platform-browser-dynamic": "8.2.2",
    "@angular/router": "8.2.2",
    "@ngx-translate/core": "11.0.1",
    "@ngx-translate/http-loader": "4.0.0",
    "@types/jasmine": "3.3.16",
    "@types/jasminewd2": "2.0.6",
    "@types/mocha": "5.2.7",
    "@types/node": "12.6.8",
    "chai": "4.2.0",
    "codelyzer": "5.1.0",
    "conventional-changelog-cli": "2.0.21",
    "core-js": "3.1.4",
    "electron": "6.0.2",
    "electron-builder": "21.2.0",
    "electron-reload": "1.5.0",
    "jasmine-core": "3.4.0",
    "jasmine-spec-reporter": "4.2.1",
    "karma": "4.2.0",
    "karma-chrome-launcher": "3.0.0",
    "karma-coverage-istanbul-reporter": "2.1.0",
    "karma-jasmine": "2.0.1",
    "karma-jasmine-html-reporter": "1.4.2",
    "mocha": "6.2.0",
    "npm-run-all": "4.1.5",
    "rxjs": "6.5.2",
    "spectron": "8.0.0",
    "ts-node": "8.3.0",
    "tslint": "5.18.0",
    "typescript": "3.5.3",
    "wait-on": "3.3.0",
    "webdriver-manager": "12.1.5",
    "zone.js": "0.9.1"
  },
  "engines": {
    "node": ">=10.9.0"
  },
  "dependencies": {
    "@angular/animations": "^8.2.3",
    "@angular/cdk": "^8.1.3",
    "@angular/material": "^8.1.3",
    "@angular/material-moment-adapter": "^8.1.3",
    "@ngrx/store": "^8.2.0",
    "moment": "^2.24.0"
  }
}
```

Note that in the `build` script, we have `--base-href ./` at the end. This is important because the styles and script will have the wrong path if we didn’t add it. The `base-href` is needed to specify that we tell the Electron web view to find the scripts and style files by their relative path instead of the absolute path.

We also included all the libraries we need like Angular Material, Moment.js, NGRX store, and the scripts for building and running our app. We changed the first key value pair to `“name”: “new-york-times”`.

After that, we do a similar renaming in `angular.json` by replacing what is there with the following:  

```
{
  "$schema": "./node_modules/@angular/cli/lib/config/schema.json",
  "version": 1,
  "newProjectRoot": "projects",
  "projects": {
    "new-york-times": {
      "root": "",
      "sourceRoot": "src",
      "projectType": "application",
      "architect": {
        "build": {
          "builder": "@angular-devkit/build-angular:browser",
          "options": {
            "outputPath": "dist",
            "index": "src/index.html",
            "main": "src/main.ts",
            "tsConfig": "src/tsconfig.app.json",
            "polyfills": "src/polyfills.ts",
            "assets": [
              "src/assets",
              "src/favicon.ico",
              "src/favicon.png",
              "src/favicon.icns",
              "src/favicon.256x256.png",
              "src/favicon.512x512.png"
            ],
            "styles": [
              "src/styles.scss"
            ],
            "scripts": []
          },
          "configurations": {
            "dev": {
              "optimization": false,
              "outputHashing": "all",
              "sourceMap": true,
              "extractCss": true,
              "namedChunks": false,
              "aot": false,
              "extractLicenses": true,
              "vendorChunk": false,
              "buildOptimizer": false,
              "fileReplacements": [
                {
                  "replace": "src/environments/environment.ts",
                  "with": "src/environments/environment.dev.ts"
                }
              ]
            },
            "production": {
              "optimization": true,
              "outputHashing": "all",
              "sourceMap": false,
              "extractCss": true,
              "namedChunks": false,
              "aot": true,
              "extractLicenses": true,
              "vendorChunk": false,
              "buildOptimizer": true,
              "fileReplacements": [
                {
                  "replace": "src/environments/environment.ts",
                  "with": "src/environments/environment.prod.ts"
                }
              ]
            }
          }
        },
        "serve": {
          "builder": "@angular-devkit/build-angular:dev-server",
          "options": {
            "browserTarget": "new-york-times:build"
          },
          "configurations": {
            "dev": {
              "browserTarget": "new-york-times:build:dev"
            },
            "production": {
              "browserTarget": "new-york-times:build:production"
            }
          }
        },
        "extract-i18n": {
          "builder": "@angular-devkit/build-angular:extract-i18n",
          "options": {
            "browserTarget": "new-york-times:build"
          }
        },
        "test": {
          "builder": "@angular-devkit/build-angular:karma",
          "options": {
            "main": "src/test.ts",
            "polyfills": "src/polyfills-test.ts",
            "tsConfig": "src/tsconfig.spec.json",
            "karmaConfig": "src/karma.conf.js",
            "scripts": [],
            "styles": [
              "src/styles.scss"
            ],
            "assets": [
              "src/assets",
              "src/favicon.ico",
              "src/favicon.png",
              "src/favicon.icns",
              "src/favicon.256x256.png",
              "src/favicon.512x512.png"
            ]
          }
        },
        "lint": {
          "builder": "@angular-devkit/build-angular:tslint",
          "options": {
            "tsConfig": [
              "src/tsconfig.app.json",
              "src/tsconfig.spec.json"
            ],
            "exclude": [
              "**/node_modules/**"
            ]
          }
        }
      }
    },
    "new-york-times-e2e": {
      "root": "e2e",
      "projectType": "application",
      "architect": {
        "lint": {
          "builder": "@angular-devkit/build-angular:tslint",
          "options": {
            "tsConfig": [
              "e2e/tsconfig.e2e.json"
            ],
            "exclude": [
              "**/node_modules/**"
            ]
          }
        }
      }
    }
  },
  "defaultProject": "new-york-times",
  "schematics": {
    "@schematics/angular:component": {
      "prefix": "app",
      "styleext": "scss"
    },
    "@schematics/angular:directive": {
      "prefix": "app"
    }
  }
}
```

We renamed all instances of `angular-electron` with `new-york-times` in this file.

Next, in `environment.ts`, `environment.prod.ts`, and `environment.dev.ts`, we put  

```
apikey: 'new york times api key',  
apiUrl: 'https://api.nytimes.com/svc'
```

into the `AppConfig` object. Replace the New York Times API key with your own.

In `index.html`, we change it to:  

```
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>New York Times</title>
  <base href="/">
  <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
  <link href="https://fonts.googleapis.com/css?family=Roboto&display=swap" rel="stylesheet">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="icon" type="image/x-icon" href="favicon.ico">
</head>
<body>
  <app-root></app-root>
</body>
</html>
```

The text between the `<title>` tags will be the title that will be displayed in our app.

Also, we need to install the packages listed in `package.json`. We do this by running `npm i`. Next we run `ng add @ngrx/store` to add the boilerplate of `@ngrx/store` flux store into our app.

With that completed, we can begin building the app. To start, we run the following commands:  

```
$ ng g component homePage  
$ ng g component articleSearchPage  
$ ng g component articleSearchResults  
$ ng g component toolBar  
$ ng g class menuReducer  
$ ng g class searchResultsReducer  
$ ng g service nyt
```

These commands will create the files that we need for our app. Now we can include the library modules into our main app module. To do this, we put the following into `app.module.ts`:  

```
import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { HomePageComponent } from './home-page/home-page.component';
import { ArticleSearchPageComponent } from './article-search-page/article-search-page.component';
import { ArticleSearchResultsComponent } from './article-search-results/article-search-results.component';
import { StoreModule } from '@ngrx/store';
import { reducers } from './reducers';
import { NytService } from './nyt.service';
import { MatSidenavModule } from '@angular/material/sidenav';
import { MatToolbarModule } from '@angular/material/toolbar';
import { MatInputModule } from '@angular/material/input';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatDatepickerModule } from '@angular/material/datepicker';
import { ToolBarComponent } from './tool-bar/tool-bar.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { MatButtonModule } from '@angular/material/button';
import { MatMomentDateModule } from '@angular/material-moment-adapter';
import { HttpClientModule } from '@angular/common/http';
import { MatSelectModule } from '@angular/material/select';
import { MatCardModule } from '@angular/material/card';
import { MatListModule } from '@angular/material/list';
import { MatMenuModule } from '@angular/material/menu';
import { MatIconModule } from '@angular/material/icon';
import { MatGridListModule } from '@angular/material/grid-list';
@NgModule({
  declarations: [
    AppComponent,
    HomePageComponent,
    ArticleSearchPageComponent,
    ArticleSearchResultsComponent,
    ToolBarComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    StoreModule.forRoot(reducers),
    FormsModule,
    MatSidenavModule,
    MatToolbarModule,
    MatInputModule,
    MatFormFieldModule,
    MatDatepickerModule,
    BrowserAnimationsModule,
    MatButtonModule,
    MatMomentDateModule,
    HttpClientModule,
    MatSelectModule,
    MatCardModule,
    MatListModule,
    MatMenuModule,
    MatIconModule,
    MatGridListModule
  ],
  providers: [
    NytService
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
```

Most of the modules in the `import` array are Angular Material modules. We will use them throughout the app.

Now we have to create the part of the app where we get and store data. To do this, run:  

```
$ ng g service nyt
```

This is where we make our `HTTP` calls to the New York Times API. Now we should have a file called `nyt.service.ts`. In there, we put:  

```
import { Injectable } from '@angular/core';
import { HttpClient, HttpParams } from '@angular/common/http';
import { environment } from 'src/environments/environment';
@Injectable({
  providedIn: 'root'
})
export class NytService {
  constructor(
    private http: HttpClient
  ) { }

  search(data) {
    let params: HttpParams = new HttpParams();
    params = params.set('api-key', environment.apikey);
    if (data.q !== undefined) {
      params = params.set('q', data.q);
    }
    if (data.begin_date !== undefined) {
      params = params.set('begin_date', data.begin_date);
    }
    if (data.end_date !== undefined) {
      params = params.set('end_date', data.end_date);
    }
    if (data.sort !== undefined) {
      params = params.set('sort', data.sort);
    }
    return this.http.get(`${environment.apiUrl}/search/v2/articlesearch.json`, { params });
  }
getArticles(section: string = 'home') {
    let params: HttpParams = new HttpParams();
    params = params.set('api-key', environment.apikey);
return this.http.get(`${environment.apiUrl}/topstories/v2/${section}.json`, { params });
  }
}
```

The `search` function takes the `data` we will pass in, and if it is defined, then it will be included in the GET request’s query string. The second parameter in the `this.http.get` function takes a variety of options, including headers and query parameters. `HttpParams` objects are converted to query strings when the code is executed. `getArticles` does similar things as the `search` function except with a different URL.

Then in `environment.ts`, we put:  

```
export const environment = {  
  production: false,  
  apikey: 'your api key',  
  apiUrl: 'https://api.nytimes.com/svc' 
};
```

This makes the URL and API key referenced in the service file available.

Next, we need to add a Flux data store to persist our menu state and search results. First, we have to run:  

```
$ ng add @ngrx/store
```

This adds the boilerplate code to the Flux store. Then, we run:  

```
$ ng g class menuReducer  
$ ng g class searchResultsReducer
$ ng g class searchData
```

We execute this in the `src\app\reducers` folder, which was created after running `ng add @ngrx/store` to make the files for our reducers.

Then in `menu-reducer.ts`, we put:  

```
export const SET_MENU_STATE = 'SET_MENU_STATE';

export function MenuReducer(state: boolean, action) {  
    switch (action.type) {  
        case SET_MENU_STATE:  
            return action.payload;default:  
            return state;  
    }  
}
```

And in `search-result-reducer.ts`, we put:  

```
export const SET_SEARCH_RESULT = 'SET_SEARCH_RESULT';

export function SearchResultReducer(state, action) {  
    switch (action.type) {  
        case SET_SEARCH_RESULT:  
            return action.payload;default:  
            return state;  
    }  
}
```

In `search-data.ts`, we put:  

```
export class SearchData {
    public begin_date: string;
    public end_date: string;
    public facet: string;
    public facet_fields: string;
    public facet_filter: string;
    public fl: string;
    public fq: string;
    public page: string;
    public q: string;
    public sort: string = 'newest';
}

```

These two pieces of code will allow the menu and search results to be stored in memory and be propagated to components that subscribe to the data.

Next in `src\app\reducers\index.ts`, we put:  

```
import { SearchResultReducer } from './search-results-reducer';  
import { MenuReducer } from './menu-reducer';

export const reducers = {  
  searchResults: SearchResultReducer,  
  menuState: MenuReducer  
};
```

This will allow our module to access our reducers since we have `StoreModule.forRoot(reducers)` in `app.module.ts`.

Now we’ll work on our app’s toolbar. To make the toolbar, we put the following in `tool-bar.component.ts`:  

```
import { Component, OnInit } from '@angular/core';
import { Store, select } from '@ngrx/store';
import { SET_MENU_STATE } from '../reducers/menu-reducer';
@Component({
  selector: 'app-tool-bar',
  templateUrl: './tool-bar.component.html',
  styleUrls: ['./tool-bar.component.scss']
})
export class ToolBarComponent implements OnInit {
  menuOpen: boolean;
  constructor(
    private store: Store<any>
  ) {
    store.pipe(select('menuState'))
      .subscribe(menuOpen => {
        this.menuOpen = menuOpen;
      })
  }

  ngOnInit() {
  }

  toggleMenu() {
    this.store.dispatch({ type: SET_MENU_STATE, payload: !this.menuOpen });
  }
}
this.store.dispatch({ type: SET_MENU_STATE, payload: !this.menuOpen });
```

This sends the state of the menu to the rest of the app.  

```
store.pipe(select('menuState'))  
  .subscribe(menuOpen => {  
    this.menuOpen = menuOpen;  
  })
```

The above gets the state of the menu and is used for displaying and toggling the menu state.

In the corresponding template, `tool-bar.component.html`, we put:  

```
<mat-toolbar>  
    <a (click)='toggleMenu()' class="menu-button">  
        <i class="material-icons">  
            menu  
        </i>  
    </a>  
    New York Times App  
</mat-toolbar>
```

And in `tool-bar.component.scss`, we put:  

```
.menu-button {  
  margin-top: 6px;  
  margin-right: 10px;  
  cursor: pointer;  
}

.mat-toolbar {  
  background: #009688;  
  color: white;  
}
```

In `app.component.scss`, we put:  

```
#content {  
  padding: 20px;  
  min-height: 100vh;  
}

ul {  
  list-style-type: none;  
  margin: 0;  
  li {  
    padding: 20px 5px;  
  }  
}
```

This changes the color of the toolbar.

Then in `app.component.ts`, we put:  

```
import { Component, HostListener } from '@angular/core';
import { SET_MENU_STATE } from './reducers/menu-reducer';
import { Store, select } from '@ngrx/store';
@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent {
  menuOpen: boolean;

  constructor(
    private store: Store<any>,
  ) {
    store.pipe(select('menuState'))
      .subscribe(menuOpen => {
        this.menuOpen = menuOpen;
      })
  }

  @HostListener('document:click', ['$event'])
  public onClick(event) {
    const isOutside = !event.target.className.includes("menu-button") &&
      !event.target.className.includes("material-icons") &&
      !event.target.className.includes("mat-drawer-inner-container")
    if (isOutside) {
      this.menuOpen = false;
      this.store.dispatch({ type: SET_MENU_STATE, payload: this.menuOpen });
    }
  }
}
```

This makes it so when we click outside of the left side menu, it’ll be closed.

In `app.component.html`, we put:  

```
<mat-sidenav-container class="example-container">
    <mat-sidenav mode="side" [opened]='menuOpen'>
        <ul>
            <li>
                <b>
                    New York Times
                </b>
            </li>
            <li>
                <a routerLink='/'>Home</a>
            </li>
            <li>
                <a routerLink='/search'>Search</a>
            </li>
        </ul>
    </mat-sidenav>
    <mat-sidenav-content>
        <app-tool-bar></app-tool-bar>
        <div id='content'>
            <router-outlet></router-outlet>
        </div>
    </mat-sidenav-content>
</mat-sidenav-container>
```

This displays our left side menu and routes.

In `style.scss`, we put:  

```
/* You can add global styles to this file, and also import other style files */
@import "~@angular/material/prebuilt-themes/indigo-pink.css";
body {
  font-family: "Roboto", sans-serif;
  margin: 0;
}
form {
  mat-form-field {
    width: 95vw;
    margin: 0 auto;
  }
}
.center {
  text-align: center;
}
```

This imports the Material Design styles and sets the width of our forms.

Then in `app-routing.module.ts`, we put the following so we can see the pages we made when we go the specified URLs:  

```
import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { HomePageComponent } from './home-page/home-page.component';
import { ArticleSearchPageComponent } from './article-search-page/article-search-page.component';
const routes: Routes = [
  { path: '', component: HomePageComponent },
  { path: 'search', component: ArticleSearchPageComponent }
];
@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
```

In `index.html`, we put:  

```
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>New York Time</title>
  <base href="/">
  <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
  <link href="https://fonts.googleapis.com/css?family=Roboto&display=swap" rel="stylesheet">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="icon" type="image/x-icon" href="favicon.ico">
</head>
<body>
  <app-root></app-root>
</body>
</html>
```

This includes the Roboto font commonly used with Material Design and Material Icons.

Now we build the logic for our two pages. First we start with our home page. In `home-page.component.html`, we put:  

```
import { Component, OnInit } from '@angular/core';
import { NytService } from '../nyt.service';
@Component({
  selector: 'app-home-page',
  templateUrl: './home-page.component.html',
  styleUrls: ['./home-page.component.scss']
})
export class HomePageComponent implements OnInit {
  sections: string[] =
    `arts, automobiles, books, business, fashion, food, health,
    home, insider, magazine, movies, national, nyregion, obituaries,
    opinion, politics, realestate, science, sports, sundayreview,
    technology, theater, tmagazine, travel, upshot, world`
      .replace(/ /g, '')
      .split(',');
  results: any[] = [];
  selectedSection: string = 'home';

  constructor(
    private nytService: NytService
  ) { }
ngOnInit() {
    this.getArticles();
  }
getArticles() {
    this.nytService.getArticles(this.selectedSection)
      .subscribe(res => {
        this.results = (res as any).results;
      })
  }
}
```

We get the articles on the first load with the `ngOnInit` function, and then once the page is loaded, we can choose which section to load.

In `home-page.component.html`, we put:  

```
<div class="center">  
    <h1>{{selectedSection | titlecase }}</h1>  
    <mat-menu #appMenu="matMenu">  
        <button mat-menu-item \*ngFor='let s of sections' (click)='selectedSection = s; getArticles()'>{{s | titlecase }}  
        </button>  
    </mat-menu><button mat-raised-button \[matMenuTriggerFor\]="appMenu">  
        Sections  
    </button>  
</div>  
<br><mat-card \*ngFor='let r of results'>  
    <mat-list role="list">  
        <mat-list-item>  
            <mat-card-title>  
                {{r.title}}  
            </mat-card-title>  
        </mat-list-item>  
    </mat-list>  
    <mat-card-subtitle>  
        <mat-list role="list">  
            <mat-list-item>Published Date: {{r.published\_date | date: 'full' }}</mat-list-item>  
            <mat-list-item><a href='{{r.url}}'>Link</a></mat-list-item>  
            <mat-list-item \*ngIf='r.byline'>{{r.byline}}</mat-list-item>  
        </mat-list>  
    </mat-card-subtitle>  
    <mat-card-content>  
        <mat-list role="list">  
            <mat-list-item>{{r.abstract}}</mat-list-item>  
        </mat-list>  
        <img \*ngIf='r.multimedia\[r.multimedia.length - 1\]?.url' \[src\]='r.multimedia\[r.multimedia.length - 1\]?.url'  
            \[alt\]='r.multimedia\[r.multimedia.length - 1\]?.caption' class="image">  
    </mat-card-content>  
</mat-card>
```

This is where we display the results from the _New York Times_ API, including headline titles, pictures, publication date, and other data. `| titlecase` is called a pipe. It maps the object to the left of the pipe symbol by calling the function on the right.

The `titlecase` pipe for example, converts a string to a title-case string. Pipes can also take arguments like `date: ‘full’` to set options that can used with the pipe.

The code on the top of the file is where we enable users to select the section they want to load by letting them choose the section they want to load. It’s here:  

```
<div class="center">  
    <h1>{{selectedSection | titlecase }}</h1>  
    <mat-menu #appMenu="matMenu">  
        <button mat-menu-item \*ngFor='let s of sections' (click)='selectedSection = s; getArticles()'>{{s | titlecase }}  
        </button>  
    </mat-menu><button mat-raised-button \[matMenuTriggerFor\]="appMenu">  
        Sections  
    </button>  
</div>  
<br>
```

This block splits the string into an array of strings with those names and without the spaces:  

```
sections: string\[\] =  
    \`arts, automobiles, books, business, fashion, food, health,  
    home, insider, magazine, movies, national, nyregion, obituaries,  
    opinion, politics, realestate, science, sports, sundayreview,  
    technology, theater, tmagazine, travel, upshot, world\`  
      .replace(/ /g, '')  
      .split(',');
```

Then in `home-page.component.scss`, we put:  

```
.image {  
  width: 100%;  
  margin-top: 30px;  
}
```

This styles the pictures displayed.

Next we build the page to search for articles. It has a form and a space to display the results.

In `article-search.component.ts`, we put:  

```
import { Component, OnInit } from '[@angular/core](http://twitter.com/angular/core)';  
import { SearchData } from '../search-data';  
import { NgForm } from '[@angular/forms](http://twitter.com/angular/forms)';  
import { NytService } from '../nyt.service';  
import \* as moment from 'moment';  
import { Store } from '[@ngrx/store](http://twitter.com/ngrx/store)';  
import { SET\_SEARCH\_RESULT } from '../reducers/search-results-reducer';[@Component](http://twitter.com/Component)({  
  selector: 'app-article-search-page',  
  templateUrl: './article-search-page.component.html',  
  styleUrls: \['./article-search-page.component.scss'\]  
})  
export class ArticleSearchPageComponent implements OnInit {  
  searchData: SearchData = <SearchData>{  
    sort: 'newest'  
  };  
  today: Date = new Date();

  constructor(  
    private nytService: NytService,  
    private store: Store<any>  
  ) {}

  ngOnInit() {  
  }

  search(searchForm: NgForm) {  
    if (searchForm.invalid) {  
      return;  
    }  
    const data: any = {  
      begin_date: moment(this.searchData.begin_date).format('YYYYMMDD'),  
      end_date: moment(this.searchData.end_date).format('YYYYMMDD'),  
      q: this.searchData.q  
    }  
    this.nytService.search(data)  
      .subscribe(res => {  
        this.store.dispatch({ type: SET_SEARCH_RESULT, payload: (res as any).response.docs });  
      })  
  }}
```

This gets the data when we click search and propagates the results to the Flux store, which will be used to display the data at the end.

In `article-search.component.html`, we put:  

```
<div class="center">
    <h1>Search</h1>
</div>
<br>
<form #searchForm='ngForm' (ngSubmit)='search(searchForm)'>
    <mat-form-field>
        <input matInput placeholder="Keyword" required #keyword='ngModel' name='keyword' [(ngModel)]='searchData.q'>
        <mat-error *ngIf="keyword.invalid && (keyword.dirty || keyword.touched)">
            <div *ngIf="keyword.errors.required">
                Keyword is required.
            </div>
        </mat-error>
    </mat-form-field>
    <br>
    <mat-form-field>
        <input matInput [matDatepicker]="startDatePicker" placeholder="Start Date" [max]="today" #startDate='ngModel'
            name='startDate' [(ngModel)]='searchData.begin_date'>
        <mat-datepicker-toggle matSuffix [for]="startDatePicker"></mat-datepicker-toggle>
        <mat-datepicker #startDatePicker></mat-datepicker>
    </mat-form-field>
    <br>
    <mat-form-field>
        <input matInput [matDatepicker]="endDatePicker" placeholder="End Date" [max]="today" #endDate='ngModel'
            name='endDate' [(ngModel)]='searchData.end_date'>
        <mat-datepicker-toggle matSuffix [for]="endDatePicker"></mat-datepicker-toggle>
        <mat-datepicker #endDatePicker></mat-datepicker>
    </mat-form-field>
    <br>
    <mat-form-field>
        <mat-label>Sort By</mat-label>
        <mat-select required [(value)]="searchData.sort">
            <mat-option value="newest">Newest</mat-option>
            <mat-option value="oldest">Oldest</mat-option>
            <mat-option value="relevance">Relevance</mat-option>
        </mat-select>
    </mat-form-field>
    <br>
    <button mat-raised-button type='submit'>Search</button>
</form>
<br>
<app-article-search-results></app-article-search-results>
```

This is the search form for the articles. It includes a keyword field, start and end date datepickers, and a drop-down to select the way to sort. These are all Angular Material components. `<app-article-search-results></app-article-search-results>` is the article search result component which we generated but have not built yet.

Note that the `[(` in `[(ngModel)]` denotes two-way data binding between the component or directive, and the current component and `[` denote one-way binding from the current component to the directive or component.

Next in `article-search.results.ts`, we put:  

```
import { Component, OnInit } from '@angular/core';
import { Store, select } from '@ngrx/store';
@Component({
  selector: 'app-article-search-results',
  templateUrl: './article-search-results.component.html',
  styleUrls: ['./article-search-results.component.scss']
})
export class ArticleSearchResultsComponent implements OnInit {
  searchResults: any[] = [];
  constructor(
    private store: Store<any>
  ) {
    store.pipe(select('searchResults'))
      .subscribe(searchResults => {
        this.searchResults = searchResults;
      })
  }

  ngOnInit() {
  }
}
```

This block gets the article search results stored in our Flux store and sends it to our template for displaying:  

```
store.pipe(select('searchResults'))  
      .subscribe(searchResults => {  
        this.searchResults = searchResults;  
      })
```

In `article-search.results.html`, we put:  

```
<mat-card *ngFor='let s of searchResults'>
    <mat-list role="list">
        <mat-list-item>
            <mat-card-title>
                {{s.headline.main}}
            </mat-card-title>
        </mat-list-item>
    </mat-list>
    <mat-card-subtitle>
        <mat-list role="list">
            <mat-list-item>Date: {{s.pub_date | date: 'full' }}</mat-list-item>
            <mat-list-item><a href='{{s.web_url}}'>Link</a></mat-list-item>
            <mat-list-item *ngIf='s.byline.original'>{{s.byline.original}}</mat-list-item>
        </mat-list>
    </mat-card-subtitle>
    <mat-card-content>
        <div class="content">
            <p>{{s.lead_paragraph}}</p>
            <p>{{s.snippet}}</p>
        </div>
    </mat-card-content>
</mat-card>
```

This just displays the results from the store.

In `article-search-results.component.scss`, we add:  

```
.content {  
  padding: 0px 15px;  
}
```

This adds some padding to the paragraphs.

With the logic done, we just need to replace the code in `core.module.ts`, with the following:  

```
import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { AppModule } from '../app.module';
@NgModule({
  declarations: [],
  imports: [
    CommonModule,
    AppModule
  ]
})
export class CoreModule { }
```

And in `shared.module.ts`, we put:  

```
import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { TranslateModule } from '@ngx-translate/core';
import { WebviewDirective } from './directives/';
import { PageNotFoundComponent } from './components';
@NgModule({
  declarations: [ WebviewDirective, PageNotFoundComponent],
  imports: [CommonModule, TranslateModule],
  exports: [TranslateModule, WebviewDirective]
})
export class SharedModule {}
```

to include the `PageNotFoundComponent` in the module so that the build will proceed.

After adding all the code, we can run `npm run ng:serve:web` to preview the app in a browser, and to preview it as an Electron, we run `npm run electron:local` .

Finally, to build the app into a Windows executable, run `npm run electron:windows` . The executable should be located in the root of the `release` folder in the project folder.
