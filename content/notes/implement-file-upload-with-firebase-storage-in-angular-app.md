---
title: "Implement file upload with Firebase Storage in our Angular App: The simple way"
date: '2020-07-05T14:11:26+00:00'
category: webclip
summary: 'The article shows how to build a cat photo upload flow in Angular with Reactive Forms, custom file validation, preview rendering, Firebase Storage, upload progress, and post-upload navigation.'
tags: ["angular", "firebase-storage", "reactive-forms", "file-upload"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Implement file upload with Firebase Storage 🔥 in our Angular App: The simple way"
    url: "https://dev.to/martinakraus11/implement-file-upload-with-firebase-storage-in-our-angular-app-the-simple-way-1ofi"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/dev-to--implement-file-upload-with-firebase-storage-in-angular-app.md"
    kind: repo
---

The article walks through a file upload feature for KittyGram in Angular. It combines Reactive Forms, Angular Material, a custom validator for image files, a preview created with FileReader, and a disabled submit state until the form is valid.

## Reading notes

- It adds `ReactiveFormsModule` and several Angular Material modules, including a file input module, to support the upload UI.
- The form has two controls, one for the photo and one for the description, both required.
- A custom `image` validator checks whether the uploaded file is an image by calling a utility service.
- The component subscribes to the photo control’s `valueChanges` to store the file and build an image preview.
- The template shows the user avatar and name, the preview image, the file input, the description field, and validation errors.
- The submit button stays disabled while the form is invalid or the upload is already running.
- Firebase Storage is enabled in the Firebase console before using it in the app.
- A `StorageService` wraps `AngularFireStorage` and returns upload progress and download URL observables.
- The upload path uses a timestamp plus the original file name to keep the storage path unique.
- The component uses the progress observable for a Material progress bar.
- After a successful upload, the app navigates back to the feed.
- Errors are shown through a snack bar, and the stream returns `EMPTY` after handling the error.
- The article says the next step will be storing the download URL and other post data for the feed.
