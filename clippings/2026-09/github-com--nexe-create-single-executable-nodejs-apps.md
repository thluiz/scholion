---
url: "https://github.com/crcn/nexe?utm_source=nodeweekly&utm_medium=email"
captured_at: "2026-09-25T08:53:44+01:00"
title: "GitHub - nexe/nexe: 🎉 create a single executable out of your node.js apps"
domain: "github-com"
---

[![](https://cloud.githubusercontent.com/assets/2391349/23598327/a17bb68a-01ee-11e7-8f55-88a5fc96e997.png)](https://cloud.githubusercontent.com/assets/2391349/23598327/a17bb68a-01ee-11e7-8f55-88a5fc96e997.png)

[![Build Status](https://camo.githubusercontent.com/64eb6d911a68e480c3ea806f9bf969d671df4c3e68714b08929fe43756359675/68747470733a2f2f696d672e736869656c64732e696f2f617a7572652d6465766f70732f6275696c642f6e6578652d63692f6e6578652f312f6d61737465722e737667)](https://dev.azure.com/nexe-ci/Nexe/_build?definitionId=1) [![Downloads](https://camo.githubusercontent.com/57d36ccb403577928b9f4ed2634bee5f194f5ee37cbbcda5032b5318d38d41b5/68747470733a2f2f696d672e736869656c64732e696f2f6e706d2f64742f6e6578652e737667)](https://www.npmjs.com/package/nexe) [![Version](https://camo.githubusercontent.com/0557d901adaf3d91c6b41804b386640bbaa3af406f12f1b4e21a6fcc535a03e3/68747470733a2f2f696d672e736869656c64732e696f2f6e706d2f762f6e6578652e737667)](https://www.npmjs.com/package/nexe) [![License](https://camo.githubusercontent.com/38aafffa33159aeb7c11e749ee7c92a88ebea94e6fc1ed40b852b0ebdffacd5c/68747470733a2f2f696d672e736869656c64732e696f2f6e706d2f6c2f6e6578652e737667)](https://www.npmjs.com/package/nexe) [![](https://camo.githubusercontent.com/4f8870d5ee3eebc00b3e5841247f8363b790ff9186362f38d8edaf26d31b22ac/68747470733a2f2f646973636f72646170702e636f6d2f6170692f6775696c64732f3831343333343932353034393536313136382f7769646765742e706e673f7374796c653d736869656c64)](https://discord.gg/2qTH52zNcZ)

Install: `npm i nexe -g`

Nexe is a command-line utility that compiles your Node.js application into a single executable file.

[![](https://user-images.githubusercontent.com/5818726/30999006-df7e0ae0-a497-11e7-96db-9ce87ae67b34.gif)](https://user-images.githubusercontent.com/5818726/30999006-df7e0ae0-a497-11e7-96db-9ce87ae67b34.gif)

## Motivation and Features

[](#motivation-and-features)

*   Self contained applications
*   Ability to run multiple applications with _different_ node.js runtimes.
*   Distribute binaries without needing node / npm.
*   Idempotent builds
*   Start and deploy faster.
*   Lockdown specific application versions, and easily rollback.
*   Flexible build pipeline
*   Cross platform builds

## Usage

[](#usage)

*   Application entrypoint:
    
    `nexe my-app.js`
    
*   stdin interface
    
    `rollup -c | nexe --resource "./public/**/*" -o my-app.exe`
    

For more CLI options see: `nexe --help`

### Examples

[](#examples)

*   `nexe server.js -r "public/**/*.html"`
*   `nexe --build`
*   `nexe -t x86-8.0.0`

## Resources

[](#resources)

Additional files or resources can be added to the binary by passing `-r "glob/pattern/**/*"`. These included files can be read in the application by using `fs.readFile` or `fs.readFileSync`.

## Compiling the nexe Executable

[](#compiling-the-nexe-executable)

By default `nexe` will attempt to download a pre-built executable. These are listed on the [releases page](https://github.com/nexe/nexe/releases/tag/v3.3.3). The exact version you want may be unavailable or you may want to customize what is built. See `nexe --help` for a list of options available when passing the [`--build`](#build-boolean) option. You will also need to ensure your environment is setup to [build node](https://github.com/nodejs/node/blob/master/BUILDING.md). Note: the `python` binary in your path should be an acceptable version of python 3; you can create a [symlink](https://github.com/nexe/nexe/issues/354#issuecomment-319874486) or use the `--python` parameter (e.g. `nexe --build --python=$(which python3)`).

### Linux and macOS

[](#linux-and-macos)

[Prerequisites & details](https://github.com/nodejs/node/blob/master/BUILDING.md#unix-and-macos)

### Windows

[](#windows)

The fastest and most reliable way to get started is simply to run the commands below. If you'd rather read the details or perform a manual install of the prerequisites, [you can find that here](https://github.com/nodejs/node/blob/master/BUILDING.md#windows).

The instructions below are the fastest and most reliable method. Run the following sets of commands with PowerShell (running as Administrator).

**Install all required build tools (and dependencies):**

```
Set-ExecutionPolicy Unrestricted -Force
iex ((New-Object System.Net.WebClient).DownloadString('https://boxstarter.org/bootstrapper.ps1'))
get-boxstarter -Force
Install-BoxstarterPackage https://raw.githubusercontent.com/nodejs/node/master/tools/bootstrap/windows_boxstarter -DisableReboots
```

**Set config:**

```
npm config set msvs_version 2019
npm config set python python3.8
```

Where `2019` is the version of Visual Studio you have (if you have it).

**Notes:**

*   The above works and has been tested with node.js `14.5.4` and `15.8.0`
*   Python 3 and Python 2 can coexist and `nexe` will still work, considering the `set config` area above
*   Don't use `npm install windows-build-tools` unless you're having some type of issue, because the above commands configures and installs the latest/preferred too.

## Node.js API

[](#nodejs-api)

#### Example

[](#example)

const { compile } \= require('nexe')

compile({
  input: './my-app.js',
  build: true, //required to use patches
  patches: \[
    async (compiler, next) \=> {
      await compiler.setFileContentsAsync(
        'lib/new-native-module.js',
        'module.exports = 42'
      )
      return next()
    }
  \]
}).then(() \=> {
  console.log('success')
})

## NexeOptions

[](#nexeoptions)

### `options: object`

[](#options-object)

*   #### `input: string`
    
    [](#input-string)
    
    *   Input bundle file path
    *   default: stdin or the current directory's main file (package.json)
*   #### `output: string`
    
    [](#output-string)
    
    *   Output executable file path
    *   default: same as `name` with an OS specific extension.
*   #### `target: string | object`
    
    [](#target-string--object)
    
    *   An object or string describing platform-arch-version. e.g. `'windows-ia32-10.13.0'`
        *   each segment is optional, and will be merged with the current environment
            
        *   Examples: ([full list](https://github.com/nexe/nexe/releases))
            
            *   `'win32-x86-10.13.0`
            *   `{ platform: 'alpine' }`
            *   `darwin-10.13.0`
            *   `linux-x64`
            *   `macos-10.13.0`
            
            See [test/target.spec.ts](https://github.com/nexe/nexe/blob/master/test/target.spec.ts)
            
    *   If the [`build`](#build-boolean) flag is set, the platform portion of the target is ignored.
    *   default: `process`
*   #### `bundle: string | boolean`
    
    [](#bundle-string--boolean)
    
    *   If a string is provided it must be a valid relative module path and should provide an export with the following signature:
    
    export function createBundle (options: NexeOptions): Promise<string\>
    
    *   default: true
*   #### `name: string`
    
    [](#name-string)
    
    *   Module friendly name of the application
    *   default: basename of the input file, or `nexe_${Date.now()}`
*   #### `cwd: string`
    
    [](#cwd-string)
    
    *   Directory nexe will operate on as though it is the cwd
    *   default: process.cwd()
*   #### `mangle: boolean`
    
    [](#mangle-boolean)
    
    *   If set to false, nexe will not include the virtual filesystem (your application and resources) on the output.
    *   This will cause the output to error as an "Invalid Binary" unless a userland patch alters the contents of lib/\_third\_party\_main.js in the nodejs source.
    *   default: true
*   #### `build: boolean`
    
    [](#build-boolean)
    
    *   Build node from source, passing this flag tells nexe to download and build from source. Subsequently using this flag will cause nexe to use the previously built binary. To rebuild, first add [`--clean`](#clean-boolean)
*   #### `remote: string`
    
    [](#remote-string)
    
    *   Provide a custom remote location for fetching pre-built nexe binaries from. This can either be an HTTP or HTTPS URL.
    *   default: `null`
*   #### `asset: string`
    
    [](#asset-string)
    
    *   Provide a pre-built nexe binary asset, this is a file path is resolved relative to cwd.
*   #### `python: string`
    
    [](#python-string)
    
    *   On Linux this is the path pointing to your python3 executable
    *   On Windows this is the directory where `python` can be accessed
    *   default: `null`
*   #### `flags: string[]`
    
    [](#flags-string)
    
    *   Array of node runtime flags to build node with.
    *   Example: `['--expose-gc']`
    *   default: `[]`
*   #### `configure: string[]`
    
    [](#configure-string)
    
    *   Array of arguments for the node build configure step
    *   Example: `['--with-dtrace', '--dest-cpu=x64']`
    *   default: `[]`
*   #### `make: string[]`
    
    [](#make-string)
    
    *   Array of arguments for the node build make step
    *   default: `[]`
*   #### `vcBuild: string[]`
    
    [](#vcbuild-string)
    
    *   Options for windows build
    *   default: `['nosign', 'release']`
*   #### `snapshot: string`
    
    [](#snapshot-string)
    
    *   path to a file to be used as the warmup snapshot for the build
    *   default: `null`
*   #### `resources: string[]`
    
    [](#resources-string)
    
    *   Array of globs with files to include in the build
    *   Example: `['./public/**/*']`
    *   default: `[]`
*   #### `temp: string`
    
    [](#temp-string)
    
    *   Path to use for storing nexe's build files
    *   Override in the env with `NEXE_TEMP`
    *   default: `~/.nexe`
*   #### `ico: string`
    
    [](#ico-string)
    
    *   Path to a user provided icon to be used (Windows only). Requires `--build` to be set.
*   #### `rc: object`
    
    [](#rc-object)
    
    *   Settings for patching the [node.rc](https://github.com/nodejs/node/blob/master/src/res/node.rc) configuration file (Windows only).
    *   Example (keys may vary depending on the version. Reference the file linked above):
        
          {
            CompanyName: "ACME Corp",
            PRODUCTVERSION: "17,3,0,0",
            FILEVERSION: "1,2,3,4"
            ...
          }
        
    *   default: `{}`
*   #### `clean: boolean`
    
    [](#clean-boolean)
    
    *   If included, nexe will remove temporary files for the accompanying configuration and exit
*   #### `enableNodeCli: boolean`
    
    [](#enablenodecli-boolean)
    
    *   Enable the original Node CLI (will prevent application cli from working).
    *   Node CLI arguments passed via the [NODE\_OPTIONS](https://nodejs.org/api/cli.html#cli_node_options_options) environment variable will still be processed. NODE\_OPTIONS support can be disabled with the `--without-node-options` configure flag.
    *   default: `false`
*   #### `fakeArgv: boolean`
    
    [](#fakeargv-boolean)
    
    *   fake the entry point file name (`process.argv[1]`). If nexe was used with stdin this will be `'[stdin]'`.
*   #### `ghToken: string`
    
    [](#ghtoken-string)
    
    *   Provide a Github Token for accessing nexe releases
    *   This is usually needed in CI environments
    *   default: `process.env.GITHUB_TOKEN`
*   #### `sourceUrl: string`
    
    [](#sourceurl-string)
    
    *   Provide an alternate url for the node source code
    *   Note: temporary files will still be created for this under the specified version
*   #### `loglevel: string`
    
    [](#loglevel-string)
    
    *   Set the loglevel, info, silent, or verbose
    *   default: `'info'`
*   #### `patches: NexePatch[]`
    
    [](#patches-nexepatch)
    
    *   Userland patches for patching or modifying node source
    *   default: `[]`
*   #### `plugins: NexePatch[]`
    
    [](#plugins-nexepatch)
    
    *   Userland plugins for modifying nexe executable behavior
    *   default: `[]`

### `NexePatch: (compiler: NexeCompiler, next: () => Promise<void>) => Promise<void>`

[](#nexepatch-compiler-nexecompiler-next---promisevoid--promisevoid)

Patches and Plugins are just a middleware functions that take two arguments, the `compiler`, and `next`. The compiler is described below, and `next` ensures that the pipeline continues. Its invocation should always be awaited or returned to ensure correct behavior. Patches also require that [`--build`](#build-boolean) be set, while plugins do not.

For examples, see the built in patches: [src/patches](https://github.com/nexe/nexe/blob/master/src/patches).

### `NexeCompiler`

[](#nexecompiler)

*   `setFileContentsAsync(filename: string, contents: string): Promise<void>`
    *   Quickly set a file's contents within the downloaded Node.js source.
*   `replaceInFileAsync(filename: string, ...replaceArgs): Promise<void>`
    *   Quickly perform a replace in a file within the downloaded Node.js source. The rest arguments are passed along to `String.prototype.replace`
*   `readFileAsync(filename: string): Promise<NexeFile>`
    *   Access (or create) a file within the downloaded Node.js source.
*   `addResource(filename: string, contents: Buffer): Promise<void>`
    *   Add a resource to the nexe bundle
*   `files: NexeFile[]`
    *   The cache of the currently read, modified, or created files within the downloaded Node.js source.

#### `NexeFile`

[](#nexefile)

*   `contents: string`
*   `absPath: string`
*   `filename: string`

Any modifications made to `NexeFile#contents` will be maintained in the cache _without_ the need to explicitly write them back out, e.g. using `NexeCompiler#setFileContentsAsync`.

## Native Modules

[](#native-modules)

In order to use native modules, the native binaries must be shipped alongside the binary generated by nexe.

## Troubleshooting

[](#troubleshooting)

`Error: Entry file "" not found!` means you need to provide `nexe` with input. Either use `-i` or pipe data to it.

`Error: https://github.com/nexe/nexe/releases/download/v3.3.3/windows-x64-15.8.0 is not available, create it using the --build flag` or similar message means that it either:

*   You are having networking issues such as the download being blocked
*   You should specify the target so `nexe` knows what version of the executable to use.
    *   See the [releases page](https://github.com/nexe/nexe/releases) to find the executable's version number
    *   Example
        *   `nexe -i "app.js" -r "public/**/*.html" -o "dist/myApp.exe" -t x64-14.15.3`
        *   where `-i` specifies the input, `-r` specifies resources to embed, `-o` specifies the output, `-t` specifies the target.
    *   Alternatively you can compile the executable yourself, see that section for details

## Contributing

[](#contributing)

Building

```
$ git clone git@github.com:nexe/nexe.git
$ cd nexe
$ npm i && npm run build
```

Testing

```
$ npm test
```
