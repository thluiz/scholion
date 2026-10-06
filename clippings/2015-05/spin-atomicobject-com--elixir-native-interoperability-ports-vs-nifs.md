---
url: "http://spin.atomicobject.com/2015/03/16/elixir-native-interoperability-ports-vs-nifs/"
captured_at: "2015-05-07T13:16:59-03:00"
title: "Elixir Native Interoperability – Ports vs. NIFs"
domain: "spin-atomicobject-com"
---

# Elixir Native Interoperability – Ports vs. NIFs

[![logo1.png](spin-atomicobject-com--elixir-native-interoperability-ports-vs-nifs/67428e8bd65cf2747d8a1b19f67bb3b6.png)](http://d1u2s20mo6at4b.cloudfront.net/wp-content/uploads/logo1.png)Lately I’ve been working on a personal project of creating a wireless sensor network across my home. [Elixir](http://elixir-lang.org/) is a perfect fit for this project, but I quickly hit a road block: serial device access. While there are Erlang serial libraries that I could use, I wasn’t ultimately comfortable doing so, due to many forks and adding yet another layer of complexity.

The [Erlang](http://erlang.org/) VM, which Elixir runs on top of, has a number of different mechanisms for interoperability with external programs. Two I’ll be discussing here are ports and NIFs. They are the two simplest, each with a unique set of pros and cons. For the examples, I’ll be interfacing with the operating system to read and write data to a serial device.

## NIF and Port Basics

First let’s take a high-level look at two of the most basic Erlang interoperability mechanisms Elixir supports.

(There are a few others interoperability mechanism such as Erl\_Interface, port drivers, and interoperability with Java, but I won’t cover here. For more information check out the [Erlang Interoperability Tutorial](http://www.erlang.org/doc/tutorial/introduction.html). These are particularly useful for if you need greater integration with Elixir such as access to message passing.)

### NIFs from 30,000 Feet

[NIFs, or Native Implemented Functions](http://www.erlang.org/doc/tutorial/nif.html), are the technique that we tend to think of when looking for interoperability between languages. Implemented in Erlang R13B03, they are similarly to [FFI in Ruby](https://spin.atomicobject.com/2013/02/15/ffi-foreign-function-interfaces/).

NIFs allow us to load a dynamic library and bind the libraries’ native functions to an Elixir function. NIFs appear as a normal function to the Elixir code invoking it, but invoke the underlying dynamic library’s implementation of the logic.

#### NIF Benefits

- Fast and simple implementation
- No context switch required
- Simple debugging

#### NIF Drawbacks

- Not very safe
- NIF-specific C library
- Native imperative implementation can leak into functional Elixir code

The most important thing to note here is that a crash in the C library will cause a crash of the entire Erlang VM. This goes against the inherit philosophy of Erlang errors, failing fast and using supervisors to recover.

### Ports from 30,000 Feet

A [port](http://www.erlang.org/doc/tutorial/c_port.html) is a technique to communicate with an external native process over STDIN and STDOUT. When a port is created, a connected process is created which is used to communicate via message passing to the external native process.

#### Port Benefits

- Safety
- Error trapping
- Flexible communication
- No external erlang/elixir specific libraries required

#### Port Drawback

- Awkward STDIN/STDOUT communication

## Other Pieces of the Puzzle

### Arduino Sketches

For easy testing of the library, I used 2 arduino sketches: one that sends random blocks of text over the serial connection, and another that’s a loopback. For more details on these sketches and working examples of all code shown here, checkout [the Github repository](https://github.com/asbaker/elixir-interop-examples).

### Makefiles and Mix

Elixir ships with an awesome build tool called [mix](http://elixir-lang.org/getting-started/mix-otp/introduction-to-mix.html), which is used to create, compile, test and manage dependencies. Integrating a make file for a C or C++ library into mix has enormous value in unifying a project’s build and is super simple.

Mix creates a few unsurprising directories when it creates a project: config, lib and test. We’ll create two more for the purpose of housing our native code and it’s compiled form: c\_src and priv\_dir.

A basic mix file looks like this:

```
defmodule SerialNifMixfile 
  use Project
   project 
    app :serial_nif
     version "0.0.1"
     elixir "~> 1.0"
     deps deps
  
   application 
    applications :logger
  
  defp deps
```

We will add a new task for compilation, configure the project to invoke that on compilation, create a new task for cleaning, and configure the aliases for clean to execute that task. This will allow us to execute

```
mix clean
```

```
mix compile
```

to clean and execute our Elixir code with mix and our native code with make.

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 ``` | ``` defmodule SerialNif.Mixfile    use Mix.Project      project      app: :serial_nif,      version: "0.0.1",      elixir: "~> 1.0",      compilers: :make, :elixir, , # Add the make compiler     aliases: aliases, # Configure aliases     deps: deps        defp aliases     # Execute the usual mix clean and our Makefile clean task    clean: "clean", "clean.make"     application      applications: :logger        defp deps             ################### # Make file Tasks # ###################   defmodule Mix.Tasks.Compile.    @shortdoc "Compiles helper in c_src"    result, _error_code = System."make", , stderr_to_stdout:     Mix.shell. resultdefmodule Mix.Tasks.Clean.   @shortdoc "Cleans helper in c_src"    result, _error_code = System."make", 'clean', stderr_to_stdout:     Mix.shell. result ``` |

## Elixir Serial Device Access with Ports

Next let’s take a look at how to use ports to access a C program which manipulates serial devices.

### Elixir Implementation

The Elixir implementation for our [ports example](https://github.com/asbaker/elixir-interop-examples/tree/master/serial_ports) is pretty simple:

```
defmodule Serial 
    
    Process:trap_exit 
    port  :spawn "priv_dir/serial" :packet 
  
   p device speed 
    commandp device
    commandp "#{speed}"])
  
   writep str 
    commandp  str
```

We have an init function that spawns a new port to our compiled c program located in priv\_dir. The second argument to Port.open/2 says we will be sending packets of data that are prefixed with a 2 byte length indicator. The implementation of the actual open and write functions is also minimal. We use Port.command/2 to send commands to our native program. The second argument to Port.command/2 is the packet which will be sent down to our native implementation. In the write example, we use the integer 3 to represent invoking the write function in our native implementation, and str is our string which we will be writing out to the serial device. You will notice that there isn’t a read function, this is because we are taking advantage of message passing from the port which will send data up to Elixir as it is received by our native implementation.

### C Implementation

The C implementation of the Port is a little bit more complicated:

```
#include 
#include 
#include 
#include "erl_comm.h"
#include "serial.h"
 bytes_read
 serial_bytes_read
 serial_fd  
 serial_buf
 reset_state 
  bytes_read  
  serial_bytes_read  
  strcpyserial_buf 

 process_commandbyte buf  bytes_read 
   fn  buf
  bytes_read   
     fn   
       device_name
      get_str_argbuf device_name bytes_read
      serial_fd  serial_opendevice_name
    
     fn   
      serial_speedserial_fd get_int_argbuf bytes_read
    
     fn   
       str
      get_str_argbuf str bytes_read
      serial_writeserial_fd str bytes_read
    
     
      fprintfstderr "not a valid fn %i\n" fn
    
  
   bytes_read   
    
  

 poll_serial_data serial_fd 
  serial_bytes_read  serial_fd serial_buf 
  serial_bytes_read   
    write_cmd byte serial_buf 
  

  
  byte buf
  while  
    reset_state
    input_available    
      bytes_read  read_cmdbuf
      process_commandbuf bytes_read
    
    serial_fd   
      poll_serial_dataserial_fd
```

Looking at the main function first, we have an infinite loop which checks to see if we have input available from elixir on STDIN. If so, then it parses the data based upon the 2 byte length indicator and executes the specific command. We also check to see if the serial device has been opened, and if it has, we poll it for any available serial data, writing it to STDOUT. You can see I am also using STDERR for error messages, it can also be used for debugging the C code from Elixir if needed.

For the sake of simplicity I abstracted away the details of parsing the command into erl\_comm.h and manipulating the serial port into serial.h. If you would like to view the dirty details, you can find the full code on Github. I stuck with the example protocol of a 2 byte packet since that code was provided by the Erlang Interoperability Tutorial and fit our use case well.

## Elixir Serial Device Access with NIFs

### Makefile

Since we will be using an Erlang provided C library for type conversion and communication with the Erlang VM, we need to make that library known to GCC.

```
ERLANG_PATH  shell   'format listsconcatroot_dir "/erts-" erlangsystem_infoversion "/include"'    noshell
CFLAGS     pedantic  Wextra ERLANG_PATH
```

### Elixir Implementation

The Elixir implementation for our [NIFs example](https://github.com/asbaker/elixir-interop-examples/tree/master/serial_nif) is a bit more complicated:

```
Serial 
  @on_load :init
    
    :erlangload_nif"./priv_dir/lib_elixir_serial" 
    
  
   device speed 
    _openStringto_char_listdevice speed
  
   fd 
    _readfd
  
   writefd str 
    _writefd Stringto_char_liststr
  
   closefd 
    _closefd
  
   _opendevice speed 
    "NIF library not loaded"
  
   _readfd 
    "NIF library not loaded"
  
   _closefd 
    "NIF library not loaded"
  
   _writefd str 
    "NIF library not loaded"
```

On loading of our module, we load the NIF C library we wrote which replaces \_open, \_read, \_close and \_write functions with their native implementations. I also have basic wrappers around our 4 functions for the public interface which guarantees the data is in the types we are expecting them to be in our C implementation.

### C Implementation

Looking at the C code for the NIF example:

```
#include "erl_nif.h"
#include 
#include 
#include 
#include "serial.h"
#define MAXBUFLEN 1024
static ERL_NIF_TERM _openErlNifEnv env int arc const ERL_NIF_TERM argv

  char pathMAXBUFLEN
  int fd
  int int_speed  
  enif_get_stringenv argv path  ERL_NIF_LATIN1
  enif_get_intenv argv int_speed
  fd  serial_openpath
  serial_speedfd int_speed
  return enif_make_intenv fd

static ERL_NIF_TERM _readErlNifEnv env int arc const ERL_NIF_TERM argv

  int fd
  char buf
  ErlNifBinary r
  int res
  enif_get_intenv argv fd
  res fdbuf
   res  
  
    enif_alloc_binary r
    strcpyrdata buf
    return enif_make_binaryenv r
  
  enif_alloc_binary r
  return enif_make_binaryenv r

static ERL_NIF_TERM _writeErlNifEnv env int arc const ERL_NIF_TERM argv

  char strMAXBUFLEN
  int fd size
  enif_get_intenv argv fd
  size  enif_get_stringenv argv str  ERL_NIF_LATIN1
  serial_writefd str size
  return enif_make_intenv size

static ERL_NIF_TERM _closeErlNifEnv env int arc const ERL_NIF_TERM argv

  int fd
  enif_get_intenv argv fd
  closefd
  return enif_make_intenv fd

static ErlNifFunc nif_funcs 

  "_open"  _open
  "_read"  _read
  "_write"  _write
  "_close"  _close

ERL_NIF_INITElixirSerialnif_funcs
```

Starting off at the bottom, we use ERL\_NIF\_INIT to actually invoke the Erlang VM magic to hot swap our bare functions for their native implementations. The first argument has to match the module that we load the NIF from, prefixed with `Elixir.`, so for our example it is `Elixir.Serial`. The nif\_funcs array is a mapping of our functions in Elixir, their arity, and their counterparts in C.

Now that we are set up, lets take a look at the implementation of one of our functions:

```
static ERL_NIF_TERM _openErlNifEnv env int arc const ERL_NIF_TERM argv

  char pathMAXBUFLEN
  int fd
  int int_speed  
  enif_get_stringenv argv path  ERL_NIF_LATIN1
  enif_get_intenv argv int_speed
  fd  serial_openpath
  serial_speedfd int_speed
  return enif_make_intenv fd
```

We have to return something of type ERL\_NIF\_TERM in order to get data back to Elixir and our arguments come in a form defined by `erl_nif.h`. We can use the `enif_get_string` and `enif_get_int` functions to convert from ERL\_NIF\_TERMs to C data types. We then invoke our functions. To convert from C data types back to Elixir data types, we use the `enif_make_int` function to convert back to an `ERL_NIF_TERM`.

The erl\_nif.h library has a number of other interesting functions such as enif\_send which allows the native C program to send messages to an Elixir pid. We could have used message passing to send data to our Elixir process instead of using the read/1 function, but this would have required threading, which opens up a whole can of worms given the safety concerns that NIFs bring with them.
