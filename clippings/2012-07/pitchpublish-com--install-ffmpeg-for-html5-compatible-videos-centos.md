---
url: "http://pitchpublish.com/?p=158"
captured_at: "2012-07-02T01:38:50-03:00"
title: "Install FFMPEG for HTML5 Compatible Videos – MP4, OGG & WebM on CentOS"
domain: "pitchpublish-com"
---

# Install FFMPEG for HTML5 Compatible Videos – MP4, OGG & WebM on CentOS

In order to install all the necessary libraries, you have to do this manually. First install all the libraries and then compile FFMPEG last with all the –enable-options.

You have to log in as root. Some basic pre-requisites:

Type these commands into SSH:

```
# yum clean all
# yum update
# yum install gcc
# yum install gcc-c++
# yum install yasm
# yum install checkinstall
# yum install make
# yum install git
# yum install subversion
# yum install check-devel
# yum groupinstall "Development Tools" -y
```

```
# grep /usr/local/lib /etc/ld.so.conf
```

If the previous command shows nothing add the /usr/local/lib to /etc/ld.so.conf

```
# echo "/usr/local/lib" >> /etc/ld.so.conf
# ldconfig
```

**WEBM**

```
# wget http://webm.googlecode.com/files/libvpx-v0.9.6.tar.bz2
# mkdir /usr/local/src
# cd /usr/local/src
# tar -xvf libvpx-v0.9.6.tar.bz2
# cd libvpx-v0.9.6
# ./configure
# make
# make install
```

**OGG**

```
# cd /usr/local/src
# wget http://downloads.xiph.org/releases/ogg/libogg-1.2.2.tar.gz
# tar zxvf libogg-1.2.2.tar.gz
# cd /usr/local/src/libogg-1.2.2
# ./configure && make clean && make && make install
# ldconfig
```

**VORBIS**

```
# cd /usr/local/src
# wget http://downloads.xiph.org/releases/vorbis/libvorbis-1.3.2.tar.gz
# tar zxvf libvorbis-1.3.2.tar.gz
# cd /usr/local/src/libvorbis-1.3.2
# ./configure && make clean && make && make install
```

**LIBX264**

```
# wget http://download.videolan.org/pub/videolan/x264/snapshots/x264-snapshot-`date -d "-1 days" +%Y%m%d`-2245-stable.tar.bz2
# tar jxf x264-snapshot-20110419-2245-stable.tar.bz2
# cd x264-snapshot-20110419-2245-stable
# make distclean
# ./configure --enable-shared && make clean && make && make install
```

**THEORA**

```
# wget http://downloads.xiph.org/releases/theora/libtheora-1.1.1.tar.gz
# tar -xvf libtheora-1.1.1.tar.gz
# cd libtheora-1.1.1
# ./configure && make clean && make && make install
```

**FAAD**

```
# wget http://downloads.sourceforge.net/project/faac/faad2-src/faad2-2.7/faad2-2.7.tar.gz
# tar -xvf faad2-2.7.tar.gz
# cd faad2-2.7
# ./configure
# make
# make install
```

**FAAC**

```
# wget http://sourceforge.net/projects/faac/files/faac-src/faac-1.28/faac-1.28.tar.gz
# tar -xvf faac-1.28.tar.gz
# cd faac-1.28
# ./configure
# make
# make install
```

**LAME**

```
# wget http://sourceforge.net/projects/lame/files/lame/3.98.4/lame-3.98.4.tar.gz
# tar -xvf lame-3.98.4.tar.gz
# cd lame-3.98.4
# ./configure
# make
# make install
```

**AMR**

```
# wget http://sourceforge.net/projects/opencore-amr/files/vo-amrwbenc/vo-amrwbenc-0.1.0.tar.gz
# tar -xvf vo-amrwbenc-0.1.0.tar.gz
# cd vo-amrwbenc-0.1.0
# ./configure
# make
# make install
```

**AMR Cont’d**

```
# cd /usr/local/src
# wget http://downloads.sourceforge.net/project/opencore-amr/opencore-amr/0.1.2/opencore-amr-0.1.2.tar.gz
# tar zxf opencore-amr-0.1.2.tar.gz
# cd /usr/local/src/opencore-amr-0.1.2
# make distclean
# ./configure && make clean && make && make install
```

**FFMPEG**

```
# cd /usr/local/src/
# git clone git://git.videolan.org/ffmpeg.git ffmpeg
# cd ffmpeg
# make distclean
# ./configure --enable-gpl --enable-version3 --enable-nonfree --enable-shared  --enable-libmp3lame --enable-libx264 --enable-libfaac  --enable-libvorbis --enable-libopencore-amrnb --enable-libopencore-amrwb --enable-libopencore-amrnb --enable-x11grab --enable-libvpx --enable-libtheora
# make clean && make && make install
# make tools/qt-faststart
# cp tools/qt-faststart /usr/local/bin/
# ldconfig
```

**Looking for FFMPEG commands to use all this newly found tools:**  
[FFMPEG Commands for HTML5 Compatible Videos](http://pitchpublish.com/?p=205)
