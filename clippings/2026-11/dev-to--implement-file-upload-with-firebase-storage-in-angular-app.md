---
url: "https://dev.to/martinakraus11/implement-file-upload-with-firebase-storage-in-our-angular-app-the-simple-way-1ofi"
captured_at: "2026-11-16T01:41:57+00:00"
title: "Implement file upload with Firebase Storage 🔥 in our Angular App: The simple way"
domain: "dev-to"
---

> PRELUDE: This is the second article in a series of articles where my dear friend Siddharth(who's a fellow GDE in Angular & Web Tech) and I create **_KittyGram_**: A super-minimal Instagram Clone that allows uploading only Cat 🐱 Photos.
> 
> Please find more information regarding the project overview and what we've implemented so far in our first article:

> In this article, we'll cover the feature of uploading files to a Firebase Storage Bucket using [Firebase Storage](https://firebase.google.com/docs/storage) and [Reactive Forms](https://angular.io/guide/reactive-forms) in Angular.
> 
> You'll get the best learning experience out of this article, if you have a basic understanding of Angular, Angular Material and Firebase is relevant.

If you already took some steps inside Angular development together with Angular Material and like to know more about it, this article is absolutely perfect for you. 🙂

I've also added a Tl;DR; below if you would like to directly jump to a specific section of my article 🐾

## [](#tldr)Tl;DR:

*   [Using the ReactiveFormsModule 😼](#using-reactive-forms-module)
    *   [Adding needed AngularMaterialModules 💄](#add-needed-material-modules)
    *   [Using reactive Forms 🤓](#using-reactive-forms)
*   [Setting up Angularfire Storage 🅰️🔥](#setting-up-angularfire-store)
    *   [Enabling the Firebase Storage 🔥](#enabling-firebase-store)
    *   [Creating the `StorageService` inside our App 📚](#creating-storage-service)
*   [To be continued 👣](#to-be-continued)
*   [Some final words 🧡](#some-final-words)

Perfect! Let's go ahead and start implementing our feature to upload cute cat pictures.

## [](#using-the-reactiveformsmodule)Using the ReactiveFormsModule 😼

As we [previously have set up](https://dev.to/angular/implement-google-sign-in-oauth-in-your-angular-app-in-under-15-minutes-1ebo#setting-up-an-angular-app) our Angular Application, we also already created the `CreateComponent` and added the belonging `/create` route to enable navigation.

But how can we upload our cute cat image with a super cute description? We also might need a proper validation of the uploaded files to ensure the file format is indeed an image.

This sounds like a lot we need to consider, but let's do it one step at a time.

Let’s first create the whole UI of our `CreateComponent` so it will look similiar to this:

[![Alt Text](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fi%2F7xbz6v4qmrf46pmwx3rg.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fi%2F7xbz6v4qmrf46pmwx3rg.png)

### [](#adding-needed-angularmaterialmodules-to-our-raw-appmaterialmodule-endraw-)Adding needed AngularMaterialModules to our `AppMaterialModule` 💄

Since we will use Input forms, a small progress bar and wrap it up all together inside a nice Display card we need to import the following AngularMaterialModules as well inside our `AppMaterialModule`:  

```
...
import { MatCardModule } from '@angular/material/card';
import { MaterialFileInputModule } from 'ngx-material-file-input';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatInputModule } from '@angular/material/input';
import { MatProgressBarModule } from '@angular/material/progress-bar';
...

@NgModule({
  exports: [
    ...
    MatCardModule,
    MaterialFileInputModule,
    MatFormFieldModule,
    MatInputModule,
    MatProgressBarModule,
    ...
  ],
})
export class AppMaterialModule {}
```

Enter fullscreen mode Exit fullscreen mode

**IMPORTANT** You might have recognized that we also imported another Module called `MaterialFileInputModule` from [ngx-material-file-input](https://www.npmjs.com/package/ngx-material-file-input)  
This was crucial for having an input with `type=file` being used inside the Angular Material `mat-form-field`.

### [](#using-reactive-forms)Using reactive Forms 🤓

So far so good, the next necessary step we need to take is importing the `ReactiveFormsModule` inside our `AppModule`:  

```
...
import { ReactiveFormsModule } from '@angular/forms';

@NgModule({
  ...
  imports: [
    ...
    ReactiveFormsModule,
  ],
  ...
})
export class AppModule {}
```

Enter fullscreen mode Exit fullscreen mode

Nice, this enables us to use reactive forms inside our components.  
Let's do it! 💪 Let's implement our form to upload pictures:

`create.component.ts`  

```
import { Component, OnDestroy, OnInit } from '@angular/core';
import {
  AbstractControl,
  FormBuilder,
  FormGroup,
  Validators,
} from '@angular/forms';
import { Observable, Subject } from 'rxjs';
import { takeUntil } from 'rxjs/operators';

import { AuthService } from '../../services/auth/auth.service';
import { UtilService } from '../../services/util/util.service';

@Component({
  selector: 'app-create',
  templateUrl: './create.component.html',
  styleUrls: ['./create.component.scss'],
})
export class CreateComponent implements OnInit, OnDestroy {
  destroy$: Subject<null> = new Subject();
  fileToUpload: File;
  kittyImagePreview: string | ArrayBuffer;
  pictureForm: FormGroup;
  user: firebase.User;

  constructor(
    private readonly authService: AuthService,
    private readonly formBuilder: FormBuilder,
    private readonly utilService: UtilService,
    ...
  ) {}

  ngOnInit() {
    this.pictureForm = this.formBuilder.group({
      photo: [null, Validators.required],
      description: [null, Validators.required],
    });

    this.authService.user$
      .pipe(takeUntil(this.destroy$))
      .subscribe((user: firebase.User) => (this.user = user));
}

  ngOnDestroy() {
    this.destroy$.next(null);
  }
}
```

Enter fullscreen mode Exit fullscreen mode

First, let’s inject the `FormBuilder`. It helps us to create a `FormGroup` that structures our whole form. Since we just need the photo and a small description we'll just add two `FromControls` to our `.group({[..],[..]})` function.

That said, we also pass a default Value inside the `FormControls` (which is `null` in our case) and one or many Form Validator/s, which are helping us, to validate the user input.

By doing so, we can either pass a [Built-in Validator](https://angular.io/guide/form-validation#built-in-validators) shipped by the `@angular/forms` module (Like the Required one we are using here) or implementing a custom Validator.

Since we want to be sure that the uploaded file is actually an image type we do need to implement this as a custom Validator.

Let's call this validator `image`:  

```
  private image(
    photoControl: AbstractControl,
  ): { [key: string]: boolean } | null {
    if (photoControl.value) {
      const [kittyImage] = photoControl.value.files;
      return this.utilService.validateFile(kittyImage)
        ? null
        : {
            image: true,
          };
    }
    return;
  }
```

Enter fullscreen mode Exit fullscreen mode

And add it to the `FormControl` named `photo`:  

```
this.pictureForm = this.formBuilder.group({
      photo: [
        null,
        [Validators.required, this.image.bind(this)],
      ],
      ...
    });
```

Enter fullscreen mode Exit fullscreen mode

The Validator calls a `UtilService` and checks, if the uploaded file type is an image:

`util.service.ts`  

```
import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root',
})
export class UtilService {
  private imageFileTypes = [
    ...
    'image/apng',
    'image/bmp',
    'image/gif',
    'image/jpeg',
    'image/png',
    'image/svg+xml',
    ...
  ];

  validateFile(file: File): boolean {
    return this.imageOrVideoFileTypes.includes(file.type);
  }
}
```

Enter fullscreen mode Exit fullscreen mode

If the evaluation of the user input fails by one of our Validators, the whole form - and of course the assigned `FormControl` itself - will turn immediately into an `invalid` state, hence we can react according to the thrown error. We'll come back to this point later inside our template code.

Apart from the Form Validation we also `subscribe` to the `authService` for fetching all the user data, like the `displayName` or the `userAvatar`.

As the final step, inside the `ngOninit` function we also need to `subscribe` to the `valueChanges` `Observable` offered by each `FormControl`:  

```
ngOnInit() {
    ...
    this.pictureForm
      .get('photo')
      .valueChanges.pipe(takeUntil(this.destroy$))
      .subscribe((newValue) => {
        this.handleFileChange(newValue.files);
      });
}
```

Enter fullscreen mode Exit fullscreen mode

Every single time a user changes the input value, it will be emitted through this `Observable`.

And what do we want to do as soon as an image is uploaded?  
We want to see a preview of it, right? So let’s implement the `handleFileChange` function:  

```
  handleFileChange([ kittyImage ]) {
    this.fileToUpload = kittyImage;
    const reader = new FileReader();
    reader.onload = (loadEvent) => (this.kittyImagePreview = 
    loadEvent.target.result);
    reader.readAsDataURL(kittyImage);
  }
```

Enter fullscreen mode Exit fullscreen mode

We are also using the official [FileReader](https://developer.mozilla.org/en-US/docs/Web/API/FileReader) for getting an image URL we can display inside an `image` tag. The [`readAsDataURL` function](https://developer.mozilla.org/en-US/docs/Web/API/FileReader/readAsDataURL) fulfills this purpose, as it can be read in the documentation:

> When the `read` operation is finished, the `readyState` becomes `DONE`, and the loadend is triggered.  
> At that time, the `result` attribute contains the data as a data: URL representing the file's data as a base64 encoded string.

Great, this is exactly what we needed 😊

**And do not forget:**  
Since we are subscribing to all these Observables, we also need to `unsubscribe` from it.

Following the `takeUntil` pattern described in [this article](https://dev.to/rxjs/takewhile-takeuntil-takewhat-5006) by [Jan-Niklas Wortmann](https://twitter.com/niklas_wortmann) we avoid  
memory leaks like a 🦊.

Awesome!  
Since we implemented the first important steps inside our `create.component.ts` file we should move to the `create.component.html`. file. So let's go! 💪💪💪

First we'll add all Material Components we need:

`create.component.html`  

```
<form
  *ngIf="user"
  class="form" 
  [formGroup]="pictureForm">
  <mat-card>
    <mat-card-header>
      <div mat-card-avatar>
        <img class="avatar" [src]="user.photoURL" />
      </div>
      <mat-card-title>Post a cute Kitty 😻</mat-card-title>
      <mat-card-subtitle>{{ user.displayName }}</mat-card-subtitle>
    </mat-card-header>
    <img
      *ngIf="kittyImagePreview"
      class="preview-image"
      [src]="kittyImagePreview"
      alt="Cute Kitty Picture"
    />
    <mat-card-content>
      <mat-form-field appearance="outline" class="full-width">
         ...
      </mat-form-field>
      <mat-form-field appearance="outline" class="full-width">
         ...
      </mat-form-field>
    </mat-card-content>
    <mat-card-actions>
      ...
    </mat-card-actions>
  </mat-card>
</form>
```

Enter fullscreen mode Exit fullscreen mode

As you can see we created a form and inserted the `MatCardComponent` as a child component to it. This form has a property binding to the related `pictureForm` which is the `FormGroup` we created already inside the `create.component.ts` folder.

Moving on, we see displaying the name and the avatar of the user inside the `MatCardHeaderComponent`.

Here we have the `image` tag where we'll see a small preview of our uploaded cat image

Inside the `mat-card-content` tag we'll now add our two `MatFormFieldComponents` one for having the file input and one textfield for our image description.

Let's start with the first one:  

```
<mat-form-field appearance="outline" class="full-width">
  <mat-label>Photo of your cute Kitty</mat-label>
  <ngx-mat-file-input
       accept="image/*"
       formControlName="photo"
       placeholder="Basic outline placeholder"
      >
  </ngx-mat-file-input>
  <mat-icon matSuffix>folder</mat-icon>
</mat-form-field>
```

Enter fullscreen mode Exit fullscreen mode

Do you remember that we added the `MaterialFileInputModule`? We needed it to have an `input` of `type=file` with the look and feel of Material Design.

This module exports the `ngx-mat-file-input` component. And this is exactly what we are using here.

The `accept="image/*"` property helps to prefilter the files that can be selected from the dialog.

Now, we just need to add a `textarea` HTML tag for our second `FormControl`:  

```
<mat-form-field appearance="outline" class="full-width">
   <mat-label>Describe your Kitty</mat-label>
   <textarea
        formControlName="description"
        matInput
        placeholder="Describe your cute Kitty to us 😻"
       >
   </textarea>
</mat-form-field>
```

Enter fullscreen mode Exit fullscreen mode

To create the binding between the single FormControls `photo` and `descriptions` to the corresponding HTML tag we just need to set the `formControlName` property accordingly.

The Angular reactive forms provides us a really easy way of displaying error messages beneath the associated `FormControl`.

By calling `pictureForm.controls['photo'].hasError(‘..’)` we immediately will be informed if one of our added Validators throws an error due to an invalid user input.

This enables us to put it inside a `*ngIf=".."` directive and wrapping it inside a `MatErrorComponent`, which already has an out of the box styling for displaying error messages:  

```
<-- Error messages for image FormControl -->
<mat-error *ngIf="pictureForm.controls['photo'].hasError('required')">
           Please select a cute Kitty Image 🐱
</mat-error>
<mat-error *ngIf="pictureForm.controls['photo'].hasError('image')">
          That doesn't look like a Kitty Image to me 😿
</mat-error>


<-- Error messages for description FormControl -->
<mat-error *ngIf="pictureForm.controls['description'].hasError('required')">
          You <strong>SHOULD</strong> describe your Kitty 😿
</mat-error>
```

Enter fullscreen mode Exit fullscreen mode

To ensure the user can't click the submit button with an invalid form, we also need to bind the `disabled` property to the `invalid` state of the whole form. That being said the button will be disabled as long as any evaluation of our `Validators` will return an error.  

```
<mat-card-actions>
   <button
        mat-raised-button
        color="primary"
        [disabled]="pictureForm.invalid || submitted"
        (click)="postKitty()"
      >
        Post Kitty
   </button>
</mat-card-actions>
```

Enter fullscreen mode Exit fullscreen mode

I know you have recognized the function `postKitty()` inside the button click event handler. And I'm pretty sure you are eager to know how we actually upload a cute kitty image to the Firebase Storage.

So let's go ahead and figure out how we can do that, shall we?

## [](#setting-up-angularfire-storage)Setting up Angularfire Storage 🅰️🔥

In the first article we already setup up our Firebase project. Please feel free to [go back](https://dev.to/angular/implement-google-sign-in-oauth-in-your-angular-app-in-under-15-minutes-1ebo#setting-up-a-firebase-project) if you haven't created the Firebase project yet. I'll wait here 🙂

Also, if you are completely new to Firebase, consider taking a glance into this awesome [YouTube Playlist](https://www.youtube.com/watch?v=Ld1F646b2U4&list=PLUcSYK_mU4eDp3y6Fg8BiGu6gSi43E0qM).

And also take a look here:

### [](#enabling-the-firebase-storage)Enabling the Firebase Storage 🔥

To enable the Firebase Storage we need to go back to the  
[Firebase Console](https://firebase.google.com/) with the same Google Account you have set up the Firebase project.

On the left Navigation click on the menu item `Develop`  
it will expand and some more menu items including `Storage` will appear.  
Click on it and you will see something like this:

[![Alt Text](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fi%2Fhj0p4zhnxldfa3dhxgdh.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fi%2Fhj0p4zhnxldfa3dhxgdh.png)

After clicking on the `Get started` Button you'll be guided through a small wizard asking you regarding some read or write access restrictions. But for now we don't need to consider this, so we can leave the default values there.

Closing the wizard by clicking on the `done` button and after maybe waiting for a few seconds, you should see something like this:

[![Alt Text](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fi%2Faukgxmbe3di68hwv4lds.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fi%2Faukgxmbe3di68hwv4lds.png)

Well done! You have now set up your Firebase Storage bucket to be filled with cute cat images 🎉.

That was easy, wasn't it?

Of course there's nothing in it yet. But I promise, as soon as we upload our first cute cat images, the files and folders will be created automatically inside this Firebase Storage bucket.

### [](#creating-the-raw-storageservice-endraw-inside-our-app)Creating the `StorageService` inside our App 📚

The last nail in the coffin would be to create the actual connection between our Firebase Storage and the submission of our form.

We also need a way to inform our users about the progress of the file upload via a prograss bar.

We can wrap all this business logic inside a service, which we'll call `StorageService`. Let's create it by calling the following command:

`ng g s services/storage/storage`

You might think this could be really tricky, but trust me it's not.  
Most of the heavy lifting is already done and is exposed as the `AngularFireStorage` service that we import from the package `@angular/fire/storage`.

`storage.service.ts`  

```
import {
  AngularFireStorage,
  AngularFireUploadTask,
} from '@angular/fire/storage';
import { from, Observable } from 'rxjs';
import { Injectable } from '@angular/core';
import { switchMap } from 'rxjs/operators';

export interface FilesUploadMetadata {
  uploadProgress$: Observable<number>;
  downloadUrl$: Observable<string>;
}

@Injectable({
  providedIn: 'root',
})
export class StorageService {
  constructor(private readonly storage: AngularFireStorage) {}

  uploadFileAndGetMetadata(
    mediaFolderPath: string,
    fileToUpload: File,
  ): FilesUploadMetadata {
    const { name } = fileToUpload;
    const filePath = `${mediaFolderPath}/${new Date().getTime()}_${name}`;
    const uploadTask: AngularFireUploadTask = this.storage.upload(
      filePath,
      fileToUpload,
    );
    return {
      uploadProgress$: uploadTask.percentageChanges(),
      downloadUrl$: this.getDownloadUrl$(uploadTask, filePath),
    };
  }

  private getDownloadUrl$(
    uploadTask: AngularFireUploadTask,
    path: string,
  ): Observable<string> {
    return from(uploadTask).pipe(
      switchMap((_) => this.storage.ref(path).getDownloadURL()),
    );
  }
}
```

Enter fullscreen mode Exit fullscreen mode

So, we created a function which returns two Observables, exposing them for our `CreateComponent` to `subscribe` to it.

If you look closely, we get the `AngularFireUploadTask` by calling the `upload()` function on the `AngularFireStorage` service that we injected as a dependency.

It provides us an Observable by calling `percentageChanges()` on it. It is emitting numbers. And as you already correctly guessed we can use these numbers to show the progress on our progress bar.

The `upload()` function takes two parameters: `filePath` and `fileToUpload`.

The first parameter represents the path to the file inside our Firebase Storage, and of course, the second parameter is the actual image we'll store on this path. As we need to have a unique file path, we can use the recent timestamp for it as well.

As a return value, we get a promise, but since we want to use Observables overall we need to create it by calling the [RxJS operator `from`](https://rxjs-dev.firebaseapp.com/api/index/function/from). It converts various other objects such as Arrays and Promises into Observables.

Since we just need to wait for this Observable to be resolved and we are more interested in the inner Observable that is emitted by calling the `getDownloadURL`, we need to use the [RxJS operator `switchMap`](https://rxjs-dev.firebaseapp.com/api/operators/switchMap) to switch to the so-called _inner Observable_ and returning it instead.

By calling the `ref` function of our `AngularFireStorage` we've injected, we create an AngularFire wrapped Storage Reference. This object creates Observables methods from promise-based methods, such as `getDownloadURL`.

So far so good. Let's now inject this service as a dependency in our `create.component.ts` and implement the `postKitty()` function.  

```
  constructor(
    ...
    private readonly snackBar: MatSnackBar,
    private readonly storageService: StorageService,
    ...
  ) {}
```

Enter fullscreen mode Exit fullscreen mode

Let's also add a cool `MatSnackBar` we need for displaying success or error messages to our users.

And now the last missing piece of code:  

```
  postKitty() {
    this.submitted = true;
    const mediaFolderPath = `${ MEDIA_STORAGE_PATH }/${ this.user.email }/media/`;

    const { downloadUrl$, uploadProgress$ } = this.storageService.uploadFileAndGetMetadata(
      mediaFolderPath,
      this.fileToUpload,
    );

    this.uploadProgress$ = uploadProgress$;

    downloadUrl$
      .pipe(
        takeUntil(this.destroy$),
        catchError((error) => {
          this.snackBar.open(`${ error.message } 😢`, 'Close', {
            duration: 4000,
          });
          return EMPTY;
        }),
      )
      .subscribe((downloadUrl) => {
        this.submitted = false;
        this.router.navigate([ `/${ FEED }` ]);
      });
  }
```

Enter fullscreen mode Exit fullscreen mode

All we need to do is to `subscribe` to both Observables we are getting from our `StorageService` calling the `uploadFileAndGetMetadata` function.

As explained before the `uploadProgress$` Observables just emits numbers.  
So let's add the `MatProgressbarComponent` to our `create.component.html`  
and inside our template we can `subscribe` to this Observable by using the `async` pipe as such:  

```
...
<mat-progress-bar *ngIf="submitted" [value]="uploadProgress$ | async" mode="determinate">
</mat-progress-bar>
...
```

Enter fullscreen mode Exit fullscreen mode

If the upload was successful we want to navigate back to the `FeedComponent`. And if something went wrong we'll catch the Error with the help of the [RxJS operator `catchError`](https://rxjs-dev.firebaseapp.com/api/operators/catchError). To handle errors like this and not inside the `.subscribe()` callback gives us the option to deal with errors without actually cancelling the whole stream.

In our case, we'll use our `snackBar` service sending an error message as a small toast to the user (giving Feedback is always important 😊) and returning [EMPTY](https://rxjs-dev.firebaseapp.com/api/index/const/EMPTY) which immediately emits a complete notification.

As you remember correctly we need to define our `mediaFolderPath` over here.  
Let's create a `storage.const.ts` file to define this const:  

```
export const MEDIA_STORAGE_PATH = `kittygram/media/`;
```

Enter fullscreen mode Exit fullscreen mode

And this is it 🎉  
We are done 😻. Great job! 💪💪💪  
Our Application is ready and set up for uploading any kind of images we want, and also posting a small description to it 🦄

You can find source-code of the Project here:

## ![GitHub logo](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fassets.dev.to%2Fassets%2Fgithub-logo-5a155e1f9a670af7944dd5e12375bc76ed542ea80224905ecaf878b9157cdefc.svg) [martinakraus](https://github.com/martinakraus) / [KittyGramUpload](https://github.com/martinakraus/KittyGramUpload)

### This respository demonstrates the image upload and storing them inside the Firebase Storage that we have in KittyGram

## KittyGramAuth

This project was generated with [Angular CLI](https://github.com/angular/angular-cli) version 9.0.5.

## Development server

Run `ng serve` for a dev server. Navigate to `http://localhost:4200/`. The app will automatically reload if you change any of the source files.

## Code scaffolding

Run `ng generate component component-name` to generate a new component. You can also use `ng generate directive|pipe|service|class|guard|interface|enum|module`.

## Build

Run `ng build` to build the project. The build artifacts will be stored in the `dist/` directory. Use the `--prod` flag for a production build.

## Running unit tests

Run `ng test` to execute the unit tests via [Karma](https://karma-runner.github.io/).

## Running end-to-end tests

Run `ng e2e` to execute the end-to-end tests via [Protractor](http://www.protractortest.org/).

## Further help

To get more help on the Angular CLI use `ng help` or go check out the [Angular CLI README](https://github.com/angular/angular-cli/blob/master/README.md).

  
  

  

## [](#to-be-continued)To be continued 👣

Uploading images was a crucial feature for **_KittyGram_**. But this is just the beginning. We now want to store the download URL along with some other details about this post to some sort of a database so that we can use it to populate our feed.

Our feed will also have features like infinite scroll of all the great cat pictures we have stored in the database 😼. And that is exactly what we are going to do in our next article.

So stay tuned and I will update this article with a link to it, once [Siddharth](https://twitter.com/siddajmera) finishes writing it.

## [](#some-final-words)Some final words 🧡

Thank you so much for staying with me to the very end and reading the whole article.

I am really grateful to [Siddharth Ajmera](https://dev.to/siddajmera) for proofreading this article and collaborating with me on this project.

I hope you liked the article. If you did please feel free to react with a ♥️ and/ or with a 🦄. Also add it to your reading list 🔖 just in case you might want to refer back to the code.

Also if there were points you weren't able to understand: Please feel free to comment down below and I'll be more than happy to help you out. 💪

One last thing, don't forget to follow Siddharth right here:

[

![siddajmera image](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F225716%2F2b5e24de-9022-49a8-930b-c74f602ffe35.jpg)

](https://dev.to/siddajmera)

See you all hopefully soon 👋👋👋

Icon Courtesy: [AngularIO Press Kit](https://angular.io/presskit#full-color-logo) | [File Upload by LAFS](https://thenounproject.com/search/?q=file%20upload&i=2347653) from the Noun Project
