#!/bin/bash

if [[ -z "$XDG_VTNR" ]] || [ $XDG_VTNR -ne 1 ]; then
  #We are not the first virtual console => nop
  exit 0
fi

BASEDIR=$(dirname "$0")
cd $BASEDIR

while [[ true ]] ; do
  tvservice -o
  python3 timemachine.py
  sleep 1
done

#tvservice --explicit="DMT 35 HDMI"
#omxplayer -o hdmi -s /home/pi/showmax_logo_animation.mkv
