# Time Machine

This is code and tooling for a game during a summer "camp". It is written Rasbian on Raspberry Pi3.

## Getting Raspberry Pi ready

Let's start with couple dependencies:
```bash
sudo apt install omxplayer python3-spidev python3-yaml
```

As it is expected to be run as automatically as possible, we leverage autologin to console. Which can be also enabled via `raspi-config`. Go to `3 Boot Options`, then `B1 Desktop / CLI` and then `B2 Console Autologin`. In your `.profile` you can then call wrapper:

```bash
/home/pi/timemachine/wrapper.sh
```




tvservice --explicit="DMT 35 HDMI"
tvservice --off

omxplayer -o hdmi -s showmax_logo_animation.mkv

XDG_VTNR=1
