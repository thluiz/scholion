---
url: "https://web.archive.org/web/20191014111157id_/https://blog.fullstacktraining.com/debugging-typescript-in-the-browser/"
captured_at: "2026-11-16T08:03:44+00:00"
title: "Debugging TypeScript in the browser"
domain: "web-archive-org"
---

Introduction

Debugging TypeScript in the browser

TypeScript, being the superset of JavaScript, makes it very convenient to write applications that have support for things like data types and generics to mention a few. However in order to be able to execute TypeScript code we need to transpile it to JavaScript. Having this JavaScript code also means that, when looking at our application code in the browser, we won't be able to see the TypeScript source code.

There are of course ways that we can do to overcome this and in this article we are going to be discussing how to debug TypeScript in web browsers by using source maps.

## Source maps

Source maps are special files that get created explicitly for JavaScript or CSS files. The idea is simple - imagine a bunch of JavaScript files or even SASS generated CSS files that get minified and concatinated in one single file. There's no way that we can debug using these files in the browser.

Having a source map will allow us to map our minified (or otherwise modified files) to their sources and be able to view the source in the browser.

On top of being able to see the original source we can also add breakpoints easily and further debug our application.

## Generate source maps

Now, in order to generate a source map, we'll be using the `tsc` transpiler with the `--sourceMaps true` option. Let's take a look at a very simple example and write some TypeScript code first:

```
interface IWarrior {
  name: string;
  health: number;
  fight: Function;
}

let myWarrior: IWarrior = {
  name: 'John the Nomad',
  health: 100,
  fight: function() {
    return `"${this.name}" attack!`;
  }
};

console.log(
  myWarrior.fight()
);
```

Now let's go ahead and transpile our code by executing `tsc --sourceMaps true`.

The result is going to be a JavaScript file with the following line appended at the end:

```
//# sourceMappingURL=app.js.map
```

And we also have a map file generated with the following content:

```
{
	"version": 3,
	"file": "app.js",
	"sourceRoot": "",
	"sources": ["app.ts"],
	"names": [],
	"mappings": "AAMA,IAAI,SAAS,GAAa;IACxB,IAAI,EAAE,gBAAgB;IACtB,MAAM,EAAE,GAAG;IACX,KAAK,EAAE;QACL,MAAM,CAAC,OAAI,IAAI,CAAC,IAAI,eAAW,CAAC;IAClC,CAAC;CACF,CAAC;AAEF,OAAO,CAAC,GAAG,CACT,SAAS,CAAC,KAAK,EAAE,CAClB,CAAC"
}
```

### Understanding the source map

The source map is really just a JSON document that has a few properties:

*   **version** - indicating the [source map standard](https://docs.google.com/document/d/1U1RGAehQwRypUTovF1KRlpiOFze0b-_2gc6fAH0KY0k/edit#)'s version
*   **file** - the transpiled filename
*   **sourceRoot** - An optional source root, useful for relocating source files on a server or removing repeated values in the “sources” entry
*   **sources**: the original TypeScript source file
*   **names**: a list of symbol names used by the following, mappings entry
*   **mappings**: encoded mapping data

So we have the generated filename, the source and the mapping between the two that uses Base 64 VLQ (Variable-Length Quality) encoding. This encoding stores letters against numbers: for example `0 - A`, `1 - C` so on and so forth. (There are some [online Base64 VLQ (de)coders](http://www.murzwin.com/base64vlq.html) available)

### Interpret Base 64 VLQ

We can use a [source map visualization tool](http://sokra.github.io/source-map-visualization/#base64,dmFyIG15V2FycmlvciA9IHsKICAgIG5hbWU6ICdKb2huIHRoZSBOb21hZCcsCiAgICBoZWFsdGg6IDEwMCwKICAgIGZpZ2h0OiBmdW5jdGlvbiAoKSB7CiAgICAgICAgcmV0dXJuICJcIiIgKyB0aGlzLm5hbWUgKyAiXCIgYXR0YWNrISI7CiAgICB9Cn07CmNvbnNvbGUubG9nKG15V2Fycmlvci5maWdodCgpKTsKLy8jIHNvdXJjZU1hcHBpbmdVUkw9YXBwLmpzLm1hcA==,eyJ2ZXJzaW9uIjozLCJmaWxlIjoiYXBwLmpzIiwic291cmNlUm9vdCI6IiIsInNvdXJjZXMiOlsiYXBwLnRzIl0sIm5hbWVzIjpbXSwibWFwcGluZ3MiOiJBQU1BLElBQUksU0FBUyxHQUFhO0lBQ3hCLElBQUksRUFBRSxnQkFBZ0I7SUFDdEIsTUFBTSxFQUFFLEdBQUc7SUFDWCxLQUFLLEVBQUU7UUFDTCxNQUFNLENBQUMsT0FBSSxJQUFJLENBQUMsSUFBSSxlQUFXLENBQUM7SUFDbEMsQ0FBQztDQUNGLENBQUM7QUFFRixPQUFPLENBQUMsR0FBRyxDQUNULFNBQVMsQ0FBQyxLQUFLLEVBQUUsQ0FDbEIsQ0FBQyJ9,aW50ZXJmYWNlIElXYXJyaW9yIHsKICBuYW1lOiBzdHJpbmc7CiAgaGVhbHRoOiBudW1iZXI7CiAgZmlnaHQ6IEZ1bmN0aW9uOwp9CgpsZXQgbXlXYXJyaW9yOiBJV2FycmlvciA9IHsKICBuYW1lOiAnSm9obiB0aGUgTm9tYWQnLAogIGhlYWx0aDogMTAwLAogIGZpZ2h0OiBmdW5jdGlvbigpIHsKICAgIHJldHVybiBgIiR7dGhpcy5uYW1lfSIgYXR0YWNrIWA7CiAgfQp9OwoKY29uc29sZS5sb2coCiAgbXlXYXJyaW9yLmZpZ2h0KCkKKTsK) to actually explore how the mapping works. This tool is really great at showing us how the original source (app.ts) maps to the generated file (app.js) pretty much term by term.

![Screen-Shot-2017-11-24-at-16.14.43](https://web.archive.org/content/images/2017/11/Screen-Shot-2017-11-24-at-16.14.43.png)

## Use the maps for debugging

Now that we have a source map available we can open the application in a browser and see that under the 'Sources' tab (for Chrome) or 'Debug' (Firefox/Safari) the original `.ts` file also appears:

![Screen-Shot-2017-11-24-at-16.09.22](https://web.archive.org/content/images/2017/11/Screen-Shot-2017-11-24-at-16.09.22.png)

Notice how we can also add breakpoints and see the values of the variables during runtime.
