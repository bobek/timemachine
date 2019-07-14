#!/bin/bash

if [[ -z "$XDG_VTNR" ]] || [ $XDG_VTNR -ne 1 ]; then
  #We are not the first virtual console => nop
  exit 0
fi

BASEDIR=$(dirname "$0")
cd $BASEDIR

while [[ true ]] ; do
  tvservice -o
  sudo python NotLinuxAjazzAK33RGB/ajazz.py --accept -d /dev/hidraw1 -l 0 -v
  sleep 1
  python3 timemachine.py
  sleep 1
done

#tvservice --explicit="DMT 81 HDMI"
# tvservice --preferred
#omxplayer -o hdmi -s /home/pi/showmax_logo_animation.mkv
