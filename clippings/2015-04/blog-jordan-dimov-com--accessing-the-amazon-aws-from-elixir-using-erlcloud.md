---
url: "http://blog.jordan-dimov.com/accessing-the-amazon-aws-from-elixir-using-erlcloud/"
captured_at: "2015-04-30T13:10:11-03:00"
title: "Accessing the Amazon AWS from Elixir (using erlcloud)"
domain: "blog-jordan-dimov-com"
---

# Accessing the Amazon AWS from Elixir (using erlcloud)

26 March 2015

Amazon does not (yet) provide an official Elixir SDK for its AWS cloud services. However, you can already do an awful lot with the wonderful Erlang module [erlcloud](https://github.com/gleber/erlcloud)

Because the documentation for `erlcloud` is a bit lacking and there are not many examples of using the library from Elixir, I put together the following quick and dirty guide with some S3 examples (for more general information about the AWS API, consult the [AWS API documentation for S3](http://docs.aws.amazon.com/AmazonS3/latest/API/APISoap.html) and [other services](http://aws.amazon.com/documentation/)).

## Setting up erlcloud from Elixir

To start using `erlcloud` from your Elixir app, first add it to the `deps` function of your `mix.exs` file, like so:

```
defp deps 
  [{:erlcloud,  "https://github.com/gleber/erlcloud"}]
```

While you're at it, make sure you also start the `ssl` and `erlcloud` applications by adding them to the `application` function like this:

```
  application 
    [applications: [:logger, , :erlcloud]]
```

Save the `mix.exs` file and download and compile the dependencies:

```
mix deps.get
mix deps.compile
```

You should now have `erlcloud` installed and ready to be used from your project.

## Configuring your AWS security credentials

Before you can make any AWS API calls with `erlcloud`, you need to provide it with your AWS credentials. You can store these as environment variables in your shell, e.g. in Bash you can do:

```
export AWS_ACCESS_KEY_ID="my-aws-access-key"
export AWS_SECRET_ACCESS_KEY="my-aws-secret-key"
```

**SECURITY NOTICE**: Amazon recommends that you set up and use [IAM roles](http://docs.aws.amazon.com/IAM/latest/UserGuide/roles-toplevel.html) instead of using your secret key directly (similar to the way you wouldn't use the `root` user on Unix systems, but use something like `sudo` instead to control access and limit damage.) I will not cover the use of IAM roles here, but `erlcloud` does support them and you should explore this further.

Once you have stored your credentials in environment variables, you can retrieve them from your Elixir code and pass them on to `erlcloud`'s `configure/2` function:

```
access_key_id = System.get_env("AWS_ACCESS_KEY_ID") |> String.to_char_list
secret_access_key = System.get_env("AWS_SECRET_ACCESS_KEY") |> String.to_char_list
:erlcloud_s3.configure(access_key_id, secret_access_key)
```

Notice that we're using `String.to_char_list/1` to convert Elixir strings to character lists before passing them on to `configure`. You have to remember to do this every time you're passing strings to Erlang functions - usually Erlang functions expect character lists and can not handle double-quoted Elixir strings.

Ok, so now that we have everything configured, let's play a bit with S3 directly from `iex`.

## Examples of using AWS S3 from Elixir

To begin with, we can create a new bucket:

```
iex(1)> :erlcloud_s3.create_bucket('test2.media')
```

**N.B.** S3 is super picky about bucket names, because they are shared across all accounts. I didn't realise this initially and kept getting errors like this, when I tried with other names, e.g. with `test1.bucket` I got:

```
** (ErlangError) erlang error: {:aws_error, {:http_error, 409, 'Conflict', "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<Error><>BucketAlreadyExists</><Message>The requested bucket name is not available. The bucket namespace is shared by all users of the system. Please select a different name and try again.</Message><BucketName>test1.bucket</BucketName><RequestId>8C8AD7689C01858B</RequestId><HostId>GI6c1Z4xnNS0WC1xMb6Tnjwm6UQOS517/lxvLzRi461HeS6IR/R4jeKubEqFYkISlNGOHlAgk7Q=</HostId></Error>"}}
```

To avoid this, make sure you pick a unique or randomly generated name for your buckets.

Assuming you managed to pick a unique name and did not a get an error from `create_bucket/1`, you can now check that your bucket is actually on S3:

```
iex(1)> :erlcloud_s3.list_buckets()           

[buckets: [[name: 'test2.media', creation_date: {{, , }, {, , }}]]]
```

Now that we have a bucket, we can create a new key-value pair:

```
iex(1)> :erlcloud_s3.put_object('test2.media', 'key1', 'value1')
[version_id: 'null']
```

Let's check the contents of our bucket to see if your key-value pair is there:

```
iex(1)> :erlcloud_s3.list_objects('test2.media')
[name: 'test2.media', prefix: [], marker: [], delimiter: [], max_keys: , is_truncated: false, common_prefixes: [], contents: [[ 'key1', last_modified: {{, , }, {, , }}, etag: '"9946687e5fa0dab5993ededddb398d2e"', size: , storage_class: 'STANDARD', owner: [ 'a336f10ec3d864ef562acf347d3e19702a6a4633fcccccef5d6697f57089c454', display_name: 'jdimov']]]]
```

Yep, there it is. We can get a nicer looking list of all keys in the bucket by using an Elixir comprehension:

```
iex(1)> objects = :erlcloud_s3.list_objects('test2.media')
iex(2)> for obj <- objects[:contents],  obj[]
['key1']
```

This tells us what keys we have in our bucket. We can get the value for a given key in the bucket using `get_object/2` (we pass it the bucket name and the key):

```
iex(1)> :erlcloud_s3.get_object('test2.media', 'key1')
[etag: '"9946687e5fa0dab5993ededddb398d2e"', content_length: , content_type: [], content_encoding: :undefined, delete_marker: false, version_id: 'null', content: "value1"]
```

Or, if we just want the content:

```
iex(11)> :erlcloud_s3.get_object('test2.media', 'key1')[:content]      
"value1"
```

This should be enough to get you started. Look inside the source code of `erlcloud` if you want to find out all of the things you can possibly do with a given AWS service. For example, for all the implemented S3 functions look here: <https://github.com/gleber/erlcloud/blob/master/src/erlcloud_s3.erl>
