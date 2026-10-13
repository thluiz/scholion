---
url: "http://stackoverflow.com/questions/6059246/how-to-include-route-handlers-in-multiple-files-in-express"
captured_at: "2012-07-24T10:33:57-03:00"
title: "node.js - How to include route handlers in multiple files in Express - Stack Overflow"
domain: "stackoverflow-com"
---

dynamically include all routes in a sub directory.

*routes/index.js*

```
var fs = require('fs'); 
 
module.exports =function(app){ 
    fs.readdirSync(__dirname).forEach(function(file){if(file =="index.js")return;var name = file.substr(0, file.indexOf('.')); 
        require('./'+ name)(app);});}
```

Then placing route files in the routes directory like so:

*routes/test1.js*

```
module.exports =function(app){ 
 
    app.get('/test1/',function(req, res){...});});//other routes..}
```

Repeating that for as many times as I needed and then finally in *app.js* placing

```
require('./routes')(app);
```
