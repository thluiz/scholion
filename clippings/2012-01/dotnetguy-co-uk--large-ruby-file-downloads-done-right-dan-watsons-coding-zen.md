---
url: "http://www.dotnetguy.co.uk/post/2011/09/27/large-ruby-file-downloads-done-right?utm_source=feedburner&utm_medium=feed&utm_campaign=Feed%3A+railsquicktips+%28Rails+Quick+Tips%29"
captured_at: "2012-01-02T12:22:30-03:00"
title: "Large Ruby File Downloads Done Right! - Dan Watsons Coding Zen"
domain: "dotnetguy-co-uk"
---

## [Large Ruby File Downloads Done Right!](http://www.dotnetguy.co.uk/post/2011/09/27/large-ruby-file-downloads-done-right)

I have recently been writing a utility in ruby to move some very large files across from Rackspace's Cloud to Amazon S3. Basically the utility firstly downloads a file from Rackspace and then uploads it to S3. Well this all seems very straight forwards but there are considerations that have to be made when you download large files using any scripted utility.

Some of the file's that are being downloaded are 1GB or more in size and I am using an Amazon Micro EC2 server that only has 613 mg of RAM. Due to the available RAM usually being smaller than the file size of the download the last thing I want to do is to put the http response stream into memory before writing it out to disk. This would cause all kinds of fail. Basically the server will run out of memory and kill the download process before it is complete. What is needed is to download and stream the file directly to disk leaving the RAM well alone.

Below is code I have extracted from my utility and simplified.

```
      Net::HTTP.start("someurl_without_the_protocol.com") do |http|  
       begin  
        file = open("/path/to/file.mov", 'wb')  
        http.request_get('/' + URI.encode("file.mov")) do |response|  
         response.read_body do |segment|  
          file.write(segment)  
         end  
        end  
       ensure  
        file.close  
       end  
      end
```
