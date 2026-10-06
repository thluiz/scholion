---
title: "Installing Erlang"
date: '2015-04-05T09:20:25-03:00'
category: webclip
summary: 'Riak built from source requires Erlang, and Basho recommends a patched Erlang version for Riak 2.0 so security features work. The page lists kerl, source, and package-based install paths by platform.'
tags: ["erlang", "riak", "source-install", "build-dependencies"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Installing Erlang"
    url: "http://docs.basho.com/riak/latest/ops/building/installing/erlang/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2015-04/docs-basho-com--installing-erlang.md"
    kind: repo
---

Riak binaries include Erlang, but building and running Riak from source requires installing Erlang separately. Basho recommends its patched Erlang build for Riak 2.0 because later official Erlang/OTP releases include the patches, and the recommended version is needed for Riak security features.

The page outlines installation paths with kerl, manual source builds, Homebrew, and MacPorts, and it lists platform-specific prerequisites for macOS, GNU/Linux, FreeBSD, Solaris, Debian/Ubuntu, and RHEL/CentOS.

## Reading notes

- Riak source builds require an Erlang installation.
- Basho recommends its patched Erlang version for Riak 2.0.
- Using another Erlang version prevents use of Riak security features.
- Building Erlang needs a GNU-compatible build system and ncurses and OpenSSL development bindings.
- Riak binary packages for Debian, Ubuntu, Mac OS X, RHEL, and CentOS already include Erlang.
- The Five-Minute Install requires downloading and installing Erlang.
- kerl is presented as the easiest way to install Erlang from source.
- On macOS, kerl may need a ~/.kerlrc file with configure options for 64-bit builds.
- On OS X 10.9 and later, autoconf may need to be installed with Homebrew.
- On FreeBSD, Solaris, and SmartOS, HIPE should be disabled when building with kerl.
- On GNU/Linux, most distributions require installing Erlang from source.
- Debian and Ubuntu need build-essential, libncurses5-dev, openssl, libssl-dev, fop, xsltproc, and unixodbc-dev.
- Graphics support packages are only needed if Erlang GUI utilities will be used.
- RHEL and CentOS need gcc, gcc-c++, glibc-devel, make, ncurses-devel, openssl-devel, autoconf, and java-openjdk-devel.
- On some RHEL6 and CentOS6 systems, CFLAGS="-DOPENSSL_NO_EC=1" must be added to ./configure.
- On macOS, Erlang can be built from source, installed with Homebrew, or installed with MacPorts.
- Homebrew installs Erlang automatically when installing Riak on macOS.
- MacPorts installs Erlang with `port install erlang +ssl`.
