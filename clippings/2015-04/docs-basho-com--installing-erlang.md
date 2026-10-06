---
url: "http://docs.basho.com/riak/latest/ops/building/installing/erlang/"
captured_at: "2015-04-05T09:20:25-03:00"
title: "Installing Erlang"
domain: "docs-basho-com"
---

# Installing Erlang

## Contents

While pre-packaged versions of Riak include an
[Erlang](http://erlang.org/) installation, you will need to install
Erlang on your own if you wish to build and run Riak from source. We
strongly recommend using Basho's patched version of Erlang to install
Riak 2.0. All of the patches in this version have been incorporated into
later versions of the official Erlang/OTP release.

The tar file for this version of Erlang can be downloaded
[here](http://s3.amazonaws.com/downloads.basho.com/erlang/otp_src_R16B02-basho5.tar.gz).
**If you do not use this version, you will not be able to use Riak's
[security features](http://docs.basho.com/riak/latest/ops/running/authz/)**.

For Erlang to build and install, you must have a GNU-compatible build
system, and the development bindings of
[ncurses](http://www.gnu.org/software/ncurses/) and
[OpenSSL](https://www.openssl.org/). The Riak binary packages for Debian
and Ubuntu, Mac OS X, and RHEL and CentOS include an Erlang
distribution, and do not require that you build Erlang from source.
However, **you must download and install Erlang if you are planning on
completing the [Five-Minute Install](http://docs.basho.com/riak/latest/quickstart/)**.

## [Install using kerl](http://docs.basho.com/riak/latest/ops/building/installing/erlang/#Install-using-kerl)

You can install different Erlang versions in a simple manner using the
[kerl](https://github.com/yrashk/kerl) script. This is probably the
easiest way to install Erlang from source on a system, and typically
only requires a few commands to do so. Install kerl by running the
following commands:

- [HTTP](http://docs.basho.com/riak/latest/ops/building/installing/erlang/#curl000)

```
curl -O https://raw.githubusercontent.com/spawngrid/kerl/master/kerl
chmod a+x kerl
```

Once kerl is installed, you can install Basho's recommended version of
Erlang [from Github](https://github.com/basho/otp) using the following
command:

- [Shell](http://docs.basho.com/riak/latest/ops/building/installing/erlang/#bash001)

```
kerl build git git://github.com/basho/otp.git OTP_R16B02_basho5 R16B02-basho5
```

Note on building on Mac OS X, FreeBSD, or Solaris

If you are building Basho's recommended version of Erlang using kerl on
Mac OS X, FreeBSD, or Solaris, consult the corresponding sections below
for a list of prerequisites that should be fulfilled *prior* to
building with kerl.

This builds the Erlang distribution and performs all of the steps
required to manually install Erlang for you.

When successfully built, you can install the build as follows:

- [Shell](http://docs.basho.com/riak/latest/ops/building/installing/erlang/#bash002)

```
./kerl install R16B02-basho5 ~/erlang/R16B02-basho5
. ~/erlang/R16B02-basho5/activate
```

The last line activates the Erlang build that was just installed into
`~/erlang/R16B02-basho5`. See the kerl
[README](https://github.com/yrashk/kerl) for more details on the
available commands.

If you prefer to install Erlang manually from the source code, the
following section will show you how.

### Mac OS X Prerequisites

To compile Erlang as 64-bit on Mac OS X, prior to running the `build`
command shown above you need to instruct kerl to pass the correct flags
to the `configure` command. The easiest way to do this is by creating a
`~/.kerlrc` file with the following contents:

- [Shell](http://docs.basho.com/riak/latest/ops/building/installing/erlang/#bash003)

```
KERL_CONFIGURE_OPTIONS="--disable-hipe --enable-smp-support --enable-threads
                        --enable-kernel-poll --without-odbc --enable-darwin-64bit"
```

If you are running OS X 10.9 (Mavericks) or later, you may need to
install [autoconf](https://www.gnu.org/software/autoconf/). To check for
the presence of autoconf, run `which autoconf`. If this returns
`autoconf not found`, the simplest way to install it is via Homebrew:

- [Shell](http://docs.basho.com/riak/latest/ops/building/installing/erlang/#bash004)

```
brew install autoconf
```

### FreeBSD/Solaris Prerequisites

When building Erlang using kerl on a FreeBSD/Solaris system (including
SmartOS), HIPE should be disabled on these platforms as well with the
`--disable-hipe` option shown in the **Mac OS X Prerequisites** section
above.

## [Installing on GNU/Linux](http://docs.basho.com/riak/latest/ops/building/installing/erlang/#Installing-on-GNU-Linux)

Most GNU/Linux distributions do not make the most recent Erlang release
available, so you will need to install *from source*.

First, make sure you have a compatible build system and that you have
installed the necessary dependencies.

### Debian/Ubuntu Dependencies

Use this command to install the required dependency packages:

- [Shell](http://docs.basho.com/riak/latest/ops/building/installing/erlang/#bash005)

```
 apt-get install build-essential libncurses5-dev openssl libssl-dev fop xsltproc unixodbc-dev
```

If you'll be using a graphical environment (such as for development
purposes) and would like to use Erlang's GUI utilities, then you'll need
to install some additional dependencies.

Note on build output

Note that these packages are not required for operation of a Riak node
and notes in the build output about missing support for wxWidgets can be
safely ignored when installing Riak in a typical non-graphical server
environment.

To install packages for graphics support, use this command:

- [Shell](http://docs.basho.com/riak/latest/ops/building/installing/erlang/#bash006)

```
 apt-get install libwxbase2. libwxgtk2.-dev libqt4-opengl-dev
```

### RHEL/CentOS Dependencies

Use this command to install the required dependency packages:

- [Shell](http://docs.basho.com/riak/latest/ops/building/installing/erlang/#bash007)

```
 yum install gcc gcc-c++ glibc-devel make ncurses-devel openssl-devel autoconf java-.-openjdk-devel
```

### Erlang

Next, download, build, and install Erlang:

- [Shell](http://docs.basho.com/riak/latest/ops/building/installing/erlang/#bash008)

```
wget http://s3.amazonaws.com/downloads.basho.com/erlang/otp_src_R16B02-basho5.tar.gz
tar zxvf otp_src_R16B02-basho5.tar.gz
 otp_src_R16B02-basho5
./configure && make &&  make install
```

Note for RHEL6/CentOS6

In certain versions of RHEL6 and CentO6 the `openSSL-devel` package
ships with Elliptical Curve Cryptography partially disabled. To
communicate this to Erlang and prevent compile- and run-time errors, the
environment variable `CFLAGS="-DOPENSSL_NO_EC=1"` needs to be added to
Erlang's `./configure` call.

The full `make` invocation then becomes

- [Shell](http://docs.basho.com/riak/latest/ops/building/installing/erlang/#bash009)

```
CFLAGS="-DOPENSSL_NO_EC=1" ./configure && make &&  make install
```

## [Installing on Mac OS X](http://docs.basho.com/riak/latest/ops/building/installing/erlang/#Installing-on-Mac-OS-X)

You can install Erlang in several ways on OS X: from source, with
Homebrew, or with MacPorts.

### Source

To build from source, you must have Xcode tools installed from the Apple
[Developer website](http://developer.apple.com/).

First, download and unpack the source:

- [Shell](http://docs.basho.com/riak/latest/ops/building/installing/erlang/#bash010)

```
curl -O http://s3.amazonaws.com/downloads.basho.com/erlang/otp_src_R16B02-basho5.tar.gz
tar zxvf otp_src_R16B02-basho5.tar.gz
 otp_src_R16B02-basho5
```

Next, configure Erlang.

#### Mavericks (OS X 10.9), Mountain Lion (OS X 10.8), and Lion (OS X 10.7)

If you're on Mavericks (OS X 10.9), Mountain Lion (OS X 10.8), or Lion
(OS X 10.7) you can use LLVM (the default) or GCC to compile Erlang.

Using LLVM:

- [Shell](http://docs.basho.com/riak/latest/ops/building/installing/erlang/#bash011)

```
CFLAGS=-O0 ./configure --disable-hipe --enable-smp-support --enable-threads \
--enable-kernel-poll --enable-darwin-bit
```

Or if you prefer GCC:

- [Shell](http://docs.basho.com/riak/latest/ops/building/installing/erlang/#bash012)

```
CC=gcc- CPPFLAGS='-DNDEBUG' MAKEFLAGS='-j 3' \
./configure --disable-hipe --enable-smp-support --enable-threads \
--enable-kernel-poll --enable-darwin-bit
```

#### Snow Leopard (OS X 10.6)

If you're on Snow Leopard (OS X 10.6) or Leopard (OS X 10.5) with an
Intel processor:

- [Shell](http://docs.basho.com/riak/latest/ops/building/installing/erlang/#bash013)

```
./configure --disable-hipe --enable-smp-support --enable-threads \
--enable-kernel-poll  --enable-darwin-bit
```

If you're on a non-Intel processor or older version of OS X:

- [Shell](http://docs.basho.com/riak/latest/ops/building/installing/erlang/#bash014)

```
./configure --disable-hipe --enable-smp-support --enable-threads \
--enable-kernel-poll
```

Now build and install:

- [Shell](http://docs.basho.com/riak/latest/ops/building/installing/erlang/#bash015)

```
make &&  make install
```

You will be prompted for your sudo password.

### Homebrew

If you want to install Riak with Homebrew, follow the [Mac OS X
Installation documentation](http://docs.basho.com/riak/latest/ops/building/installing/mac-osx/), and Erlang will be
installed automatically.

To install Erlang separately with Homebrew, use this command:

- [Shell](http://docs.basho.com/riak/latest/ops/building/installing/erlang/#bash016)

```
brew install erlang
```

### MacPorts

Installing with MacPorts is easy:

- [Shell](http://docs.basho.com/riak/latest/ops/building/installing/erlang/#bash017)

```
port install erlang +ssl
```

#### Tutorial Nav: [Installing and Upgrading](http://docs.basho.com/riak/latest/ops/building/installing/)
