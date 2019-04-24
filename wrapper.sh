#!/bin/bash

if [[ -z "$XDG_VTNR" ]] || [ $XDG_VTNR -ne 1 ]; then
  #We are not the first virtual console => nop
  exit 0
fi

BASEDIR=$(dirname "$0")
cd $BASEDIR

# Turning HDMI off and on to get rid of any boot artifacts
tvservice -o
tvservice --explicit="DMT 35 HDMI"

python3 timemachine.py
#omxplayer -o hdmi -s /home/pi/showmax_logo_animation.mkv
