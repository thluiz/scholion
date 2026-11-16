---
title: "Creating Thumbnails of uploaded Images and PDF in Phoenix"
date: '2026-11-16T04:16:09+00:00'
category: webclip
summary: 'The article adds thumbnail generation to a Phoenix upload app, using ImageMagick and Mogrify for images and System.cmd with convert for PDFs, then stores and serves the thumbnails through a new route.'
tags: ["phoenix", "imagemagick", "mogrify", "pdf"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Creating Thumbnails of uploaded Images and PDF in Phoenix · Poeticoding"
    url: "https://poeticoding.com/creating-thumbnails-of-uploaded-images-and-pdf-in-phoenix"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/poeticoding-com--creating-thumbnails-of-uploaded-images-and-pdf-in-phoenix.md"
    kind: repo
---

The article extends a Phoenix upload app so it can generate thumbnails for image files and PDF files. It adds a boolean field to track whether an upload has a thumbnail, creates thumbnail paths in the uploads directory, and updates the upload flow so the thumbnail is created during upload processing.

It also shows how to serve the thumbnail through a new controller action and display it in the uploads list, with a generic image used when no thumbnail exists. For images it uses Mogrify and ImageMagick, and for PDFs it runs ImageMagick's convert command through System.cmd.

## Reading notes

- The app starts from the previous Phoenix upload tutorial and uses the same repository state as part 1.
- The setup includes getting dependencies, compiling assets, creating the database, and running the Phoenix server.
- ImageMagick is required to process images and PDFs into resized JPEG thumbnails.
- Mogrify wraps ImageMagick's mogrify command and is used to resize images to a maximum of 300 by 300 pixels.
- A new boolean database column, has_thumb, is added to the uploads table with a migration.
- The Upload schema maps thumbnail? to the has_thumb column with the source option.
- The changeset must cast thumbnail? so the field can be updated.
- Thumbnails are stored in the same directory as uploaded files, with a path based on the upload id.
- The image thumbnail function opens the source file, resizes it, saves it as a JPEG, and returns an updated changeset.
- The image thumbnail logic handles files whose content type starts with image/.
- The Documents context calls thumbnail creation during the upload transaction and persists the change with Repo.update/1.
- A new route under uploads points to a thumbnail action in UploadController.
- The controller action finds the thumbnail path, sets the response type to image/jpeg, and sends the file.
- The upload list shows the thumbnail when thumbnail? is true and a generic thumbnail otherwise.
- PDF thumbnails are created from the first page of the document by calling ImageMagick's convert command.
- The PDF thumbnail function uses System.cmd/3 and returns either {:ok, thumb_path} or {:error, reason}.
- The Upload module adds a create_thumbnail clause for application/pdf files.
- The article notes that error output from convert can be verbose and may need processing.
- The full code for this part is available in the project's GitHub repository.
