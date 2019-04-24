import outputters
import inputters
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

    while dst is None:
        key = ask_for_key()
        try:
            dst = time_destinations[key]
        except KeyError:
            display.line(0, 'Spatny kod!')
            time.sleep(2)

    return(dst)


console = False
if len(sys.argv) == 2 and sys.argv[1] == 'console':
    console = True

display = outputters.get_outputter(console)
inputter = inputters.Inputter(display)
time_destinations = yaml.load(open('destinations.yml', 'r'))

if not console:
    boot()

if console:
    print(repr(time_destinations))

destination = get_destination()
display.cls()
display.line(0, destination['name'])
display.line(1, '   ... jedeme ...')

if not console:
    os.system('omxplayer -o hdmi video/news.mkv')

display.cls(); display.line(0, "Time machine is"); display.line(1, "shutting down ..."); time.sleep(1)
time.sleep(2)
display.visibility(False)