import outputters
import inputters
import psucontrol
import time
import yaml
import sys, os


def boot():
    display.cls(); display.line(0, "Time machine is"); display.line(1, "starting ..."); time.sleep(1)
    display.cls(); display.line(0, "Casostroj startuje"); time.sleep(1)
    display.cls(); display.line(0, "Time machine"); display.line(1, "is ready ..."); time.sleep(1)
    display.cls(); display.line(0, "Casostroj"); display.line(1, "je pripraven ..."); time.sleep(1)
    display.cls()


def ask_for_key(prompt='Casovy kod?'):
    display.cls()
    display.line(0, prompt)
    display.goto(1,0)
    return(inputter.input_by_char())


def get_destination():
    dst = None
    retries = 5

    while dst is None:
        key = ask_for_key()
        try:
            dst = time_destinations[key]
        except KeyError:
            retries -= 1
            display.line(0, 'Spatny kod!')
            time.sleep(2)
            if retries <= 0:
                return None

    return(dst)


console = False
if len(sys.argv) == 2 and sys.argv[1] == 'console':
    console = True

button = psucontrol.PushButton(27)
button.wait_for_push()
del button

psu = psucontrol.PSU(17) # pin 11 on the connector
psu.turn_on(); time.sleep(0.5)

os.system('sudo python NotLinuxAjazzAK33RGB/ajazz.py --accept -d /dev/hidraw1 -l 5')

display = outputters.get_outputter(console)
inputter = inputters.Inputter(display)
time_destinations = yaml.load(open('destinations.yml', 'r'))

if not console:
    boot()

if console:
    print(repr(time_destinations))

destination = get_destination()

if destination is not None:
    display.cls()
    display.line(0, destination['name'])
    display.line(1, '   ... jedeme ...')

    if not console:
        os.system('tvservice --preferred')
        os.system('omxplayer -o hdmi video/splash/Earth - 1175.mp4')
        os.system('tvservice --off')

display.cls(); display.line(0, "Time machine is"); display.line(1, "shutting down ..."); time.sleep(1)
time.sleep(2)
display.visibility(False)
del psu
