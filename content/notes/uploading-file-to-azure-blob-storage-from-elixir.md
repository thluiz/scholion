---
title: "Uploading file to Azure Blob storage from Elixir"
date: '2020-07-05T14:11:27+00:00'
category: webclip
summary: 'Shows how to create an Azure storage account, add a container, add erlazure to a Mix project, start the client, and upload a file as a block blob.'
tags: ["elixir", "azure-blob-storage", "erlazure"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Uploading file to Azure Blob storage from Elixir"
    url: "https://chodounsky.com/2015/05/22/uploading-file-to-azure-blob-storage-from-elixir"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/chodounsky-com--uploading-file-to-azure-blob-storage-from-elixir.md"
    kind: repo
---

The post explains a simple workflow for uploading a file to Azure Blob storage from Elixir. It starts by creating a storage account, getting the account name and secondary access key, and adding a container for the files.

It then shows adding the erlazure dependency to a Mix project, starting the client process with the account and key, and using put_block_blob to upload a local file into the container. The uploaded file is then available at the Azure Blob URL format given in the post.

## Reading notes

- Create a storage account and use its account name and secondary access key.
- Add a container for the files, either manually in Azure or with code; the example uses a container named test.
- Use the erlazure Erlang library and add it as a Mix dependency.
- Start the client with :erlazure.start(account, key) before making the request.
- Upload the file with :erlazure.put_block_blob(pid, container, filename, file_contents).
- The file becomes available at the blob URL shown in the post.
