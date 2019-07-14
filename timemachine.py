import outputters
import inputters
import psucontrol
import time
import yaml
import os, random, shlex, sys


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

def pairs(lst):
    if not lst:
        return []

    if len(lst) <= 2:
        return [lst]

    return [lst[0:2]] + pairs(lst[2:])

def display_message(message=[]):
    for p in pairs(message):
        display.cls();
        display.line(0, p[0]);
        if len(p) > 1:
            display.line(1, p[1])
        time.sleep(4)

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

def random_file(root=''):
    file = random.choice(os.listdir(root))
    return os.path.join(root, file)

console = False
if len(sys.argv) == 2 and sys.argv[1] == 'console':
    console = True

button = psucontrol.PushButton(27)
button.wait_for_push()
del button

psu = psucontrol.PSU(17) # pin 11 on the connector
psu.turn_on(); time.sleep(0.5)

os.system('sudo python NotLinuxAjazzAK33RGB/ajazz.py --accept -d /dev/hidraw1 -l 5 -m {mode}'.format(mode=random.choice(list(range(1,6)) + list(range(10,18)))))

display = outputters.get_outputter(console)
inputter = inputters.Inputter(display)
time_destinations = yaml.load(open('destinations.yml', 'r'), Loader=yaml.FullLoader)

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
        #os.system('tvservice --preferred')
        os.system('tvservice --explicit="CEA 4 HDMI"')
        os.system('omxplayer -o hdmi {video}'.format(video=shlex.quote(random_file('video/splash'))))
        os.system('omxplayer -o hdmi {video}'.format(video=shlex.quote(destination['video'])))
        os.system('tvservice --off')

    if 'message' in destination:
        display_message(destination['message'])

display.cls(); display.line(0, "Time machine is"); display.line(1, "shutting down ..."); time.sleep(1)
time.sleep(2)
display.visibility(False)
del psu
