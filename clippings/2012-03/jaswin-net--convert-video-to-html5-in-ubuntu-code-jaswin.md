---
url: "http://jaswin.net/code/convert-video-to-html5-in-ubuntu/"
captured_at: "2012-03-01T13:10:29-03:00"
title: "Convert Video to HTML5 in Ubuntu – Code – Jaswin"
domain: "jaswin-net"
---

28
Jan

# Convert Video to HTML5 in Ubuntu

## [Code](http://jaswin.net/category/code/ "View all posts in Code")

I wanted an easy way to convert videos to HTML5 formats (mp4/ogg/webm). With Linux, I could easily create a bash script to do all three and even create a screencap for the `poster` attribute.

The install process is a bit tedious and time consuming, but after it’s all installed you’re good to run the script for all your videos. The script uses ffmpeg to convert to all 3 formats, and it supports most any video format. The script also uses ffmpeg to generate a random screenshot, and even writes the HTML5 code for you.

### Installation

For the most part, this portion of the tutorial was derived from the [Ubuntu Forums](http://ubuntuforums.org/showpost.php?p=9868359&postcount=1289) .

1. #### Uninstall Old Versions

   |  |  |
   | --- | --- |
   |  | sudo apt-get remove ffmpeg x264 libx264-dev yasm |
2. #### Install Dependencies and Install Tools

   |  |  |
   | --- | --- |
   |  | sudo apt-get update  sudo apt-get install build-essential git-core checkinstall texi2html libfaac-dev \      libopencore-amrnb-dev libopencore-amrwb-dev libsdl1.2-dev libtheora-dev \      libvorbis-dev libx11-dev libxfixes-dev zlib1g-dev |
3. #### Install Yasm

   |  |  |
   | --- | --- |
   | 1 2 3 4 5 6 7 | cd ~/Downloads  wget http://www.tortall.net/projects/yasm/releases/yasm-1.2.0.tar.gz  tar xzvf yasm-1.2.0.tar.gz  cd yasm-1.2.0  ./configure  make  sudo checkinstall --pkgname=yasm --pkgversion="1.2.0" --backup=no --deldoc=yes --default |
4. #### Install x264

   |  |  |
   | --- | --- |
   | 1 2 3 4 5 6 7 | cd ~/Downloads  git clone git://git.videolan.org/x264  cd x264  ./configure --enable-static  make  sudo checkinstall --pkgname=x264 --default --pkgversion="3:$(./version.sh | \      awk -F'[" ]' '/POINT/{print $4"+git"$5}')" --backup=no --deldoc=yes |
5. #### Install LAME

   |  |  |
   | --- | --- |
   | 1 2 3 4 5 6 7 8 9 10 | sudo apt-get remove libmp3lame-dev  sudo apt-get install nasm  cd ~/Downloads  wget http://downloads.sourceforge.net/project/lame/lame/3.99/lame-3.99.tar.gz  tar xzvf lame-3.99.tar.gz  cd lame-3.99  ./configure --enable-nasm --disable-shared  make  sudo checkinstall --pkgname=lame-ffmpeg --pkgversion="3.99" --backup=no --default \      --deldoc=yes |
6. #### Install libvpx

   |  |  |
   | --- | --- |
   | 1 2 3 4 5 6 7 | cd ~/Downloads  git clone http://git.chromium.org/webm/libvpx.git  cd libvpx  ./configure  make  sudo checkinstall --pkgname=libvpx --pkgversion="$(date +%Y%m%d%H%M)-git" --backup=no \      --default --deldoc=yes |
7. #### Install ffmpeg

   |  |  |
   | --- | --- |
   | 1 2 3 4 5 6 7 8 9 | cd ~/Downloads  git clone --depth 1 git://source.ffmpeg.org/ffmpeg  cd ffmpeg  ./configure --enable-gpl --enable-libfaac --enable-libmp3lame --enable-libopencore-amrnb \      --enable-libopencore-amrwb --enable-libtheora --enable-libvorbis --enable-libvpx \      --enable-libx264 --enable-nonfree --enable-postproc --enable-version3 --enable-x11grab  make  sudo checkinstall --pkgname=ffmpeg --pkgversion="$(date +%Y%m%d%H%M)-git" --backup=no \      --deldoc=yes --default |

The part that will take the longest is the ffmpeg, so be prepared to wait.

Sidenote: You may have to create some directories if you get a “No such file or directory” error. Just use the `mkdir` command and re-run the prior command.

### The Script

Usage:

|  |  |
| --- | --- |
|  | ./convertHTML5 video-file.ext |

The script will output “video-file.ogv”, “video-file.webm”, “video-file.mp4″, and “video-file.html” while keeping the original video intact. The HTML document just has the plain `<video>` code with nothing else, easily copied and pasted.

|  |  |
| --- | --- |
| 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 | #!/bin/bash  if [[ $1 ]]  then      filename=$(basename "$1")      filename=${filename%.\*}      directory=$(dirname "$1")  duration=$(ffmpeg -i "$1" 2>&1 | grep Duration | awk '{print $2}' | tr -d ,)      minutes=${duration%:\*}      hours=${minutes%:\*}      minutes=${minutes##\*:}      seconds=${duration##\*:}      seconds=${seconds%.\*}        hours=$((hours\*3600))      minutes=$((minutes\*60))  total=$(expr $hours + $minutes + $seconds)      number=$RANDOM      let "number %= $total"  echo "Generating thumbnail"      ffmpeg -i "$1" -deinterlace -an -ss $number -t 00:00:01 -r 1 -y -vcodec mjpeg -f mjpeg "$directory/$filename.jpg" 2>&1      echo "Converting $filename to ogv"      ffmpeg -i "$1" -acodec libvorbis -ac 2 -ab 96k -ar 44100 -b 345k "$directory/$filename.ogv"      echo "Finished ogv"  echo "Converting $filename to webm"      ffmpeg -i "$1" -acodec libvorbis -ac 2 -ab 96k -ar 44100 -b 345k "$directory/$filename.webm"      echo "Finished webm"  echo "Converting $filename to h264"      ffmpeg -i "$1" -acodec libfaac -ab 96k -vcodec libx264 -level 21 -refs 2 -b 345k -bt 345k -threads 0 "$directory/$filename.mp4"      echo "Finished h264"  echo "Writing HTML..."  echo "<video controls poster=\"$filename.jpg\" preload>" > "$directory/$filename.html"      echo "  <source type=\"video/ogg\" src=\"$filename.ogv\">" >> "$directory/$filename.html"      echo "  <source type=\"video/webm\" src=\"$filename.webm\">" >> "$directory/$filename.html"      echo "  <source type=\"video/mp4\" src=\"$filename.mp4\">" >> "$directory/$filename.html"      echo "  Sorry, your browser does not support HTML5 video" >> "$directory/$filename.html"      echo "</video>" >> "$directory/$filename.html"  echo "All Done!"  else      echo "Usage: [filename]"  fi |
