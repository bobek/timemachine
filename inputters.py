from getch import getch


class Inputter:
    """Manage input char by char"""

    def __init__(self, display=None):
        self.display = display

    def input_by_char(self):
        string = ''
        while True:
            ch = getch()
            if ch == '\r': break
            if ch == '\x7f':
                #Backspace
                string = string[:-1]
                self.display.backspace()
            else:
                string += ch
                self.display.character(ch)
        return string