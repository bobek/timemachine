import time

try:
    import simplevfd
except ModuleNotFoundError:
    print('Unable to import VDF module')

def get_outputter(console=True):
    if console:
        return ConsoleOutputter()
    else:
        return VFDOutputter()


class GenericOutputter(object):
    """Generic class for Outputter"""

    def __init__(self):
        self.cls()

    def cls(self):
        pass

    def goto(self, line=0, column=0):
        pass

    def line(self, num, string, delay=0.0):
        pass

    def write(self, string, delay=0.0):
        pass

    def backspace(self):
        pass

    def character(self, ch):
        pass

    def visibility(self, displayOn=True):
        pass


class ConsoleOutputter(GenericOutputter):
    """Wraps normal console / stdout for debugging"""

    def cls(self):
        print('CLS')

    def goto(self, line=0, column=0):
        print('GOTO({}, {})'.format(x,y))

    def line(self, num, string, delay=0.05):
        print('{}: '.format(num), end='', flush=True)
        self.write(string, delay)

    def write(self, string, delay=0.05):
        for ch in string:
            print(ch, end='', flush=True)
            time.sleep(delay)
        print()

    def character(self, ch):
        print(repr(ch))

    def backspace(self):
        print('␈')


class VFDOutputter(GenericOutputter):
    """Wraps VFD"""

    def __init__(self):
        self.vfd = simplevfd.simplevfd.SimpleVFD(0,0)
        super(VFDOutputter, self).__init__()

    def cls(self):
        self.vfd.cls()

    def write(self, string, delay=0.05):
        self.vfd.write_str(string, delay)

    def line(self, num, string, delay=0.05):
        self.goto(num, 0)
        self.write(string, delay)

    def goto(self, line=0, column=0):
        self.vfd.set_cursor_positions(column, line)

    def character(self, ch):
        self.vfd.write_str(ch)

    def backspace(self):
        self.vfd.move_cursor(False, False)
        self.vfd.write_str(' ')
        self.vfd.move_cursor(False, False)

    def visibility(self, displayOn=True):
        self.vfd.configure_display(displayOn, True, True)
