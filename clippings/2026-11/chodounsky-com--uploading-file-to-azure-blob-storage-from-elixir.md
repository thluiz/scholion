---
url: "https://chodounsky.com/2015/05/22/uploading-file-to-azure-blob-storage-from-elixir"
captured_at: "2026-11-16T04:15:03+00:00"
title: "Uploading file to Azure Blob storage from Elixir"
domain: "chodounsky-com"
---

Firstly, create a storage account and get a account name and a secondary access key by clicking on _Manage Access Keys_ button.

After that, add a container for your files to be in. You can do it manually on Azure or with a code, for this example let’s create it manually and call it creatively `test`.

We are going to use an Erlang library [erlazure](https://github.com/dkataskin/erlazure) by Dmitry Kataskin so add a dependency to you mix file.

```
  defp deps do
    [ { :erlazure, github: "dkataskin/erlazure" } ]
  end
```

Now, we firstly _start_ the process (it doesn’t do any network communication) and pass this started process id to the actual request (this is where the network communication happens).

```
    account = 'your-storage-account-name'
    key = 'your-secondary-access-key'

    {:ok, pid} = :erlazure.start(account, key)
    :erlazure.put_block_blob(pid, 'test', 'name-of-image.jpg', File.read!("/path/to/the/photo.jpg"))
```

And your file is uploaded at `https://storage-account-name.blob.core.windows.net/your-container/your-filename` and you can use it from your website.

* * *

Would you like to get the most interesting content about C# every Monday?  
Sign up to **[C# Digest](https://csharpdigest.net/?utm_source=blog&utm_campaign=Uploading-file-to-Azure-Blob-storage-from-Elixir)** and stay up to date!
