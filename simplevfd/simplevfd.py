import spidev
import time


class SimpleVFD:
    def __init__(self, spi_num, spi_ce):
        self.spi = spidev.SpiDev()
        self.spi.open(spi_num, spi_ce)
        self.spi.max_speed_hz = 5000
        self.spi.mode = 0b11
        self.spi.bits_per_word = 8
        self.configure_display(True, True, True)
        self.set_cursor_direction(True, False)

    def write(self, data, rs):
        if rs:
            self.spi.xfer2([0xFA, data])
        else:
            self.spi.xfer2([0xF8, data])
        time.sleep(0.00001)

    def write_command(self, cmd):
        self.write(cmd, False)

    def write_str(self, string, sleep=0):
        for ch in string:
            self.write(ord(ch), True)
            time.sleep(sleep)

    def configure_display(self, display, cursor, blink):
        cmd = 0b00001000
        if display:
            cmd = cmd | 0b00000100
        if cursor:
            cmd = cmd | 0b00000010
        if blink:
            cmd = cmd | 0b00000001

        self.write_command(cmd)

    def cls(self):
        self.write_command(0x01)
        time.sleep(0.005)

    def set_cursor_positions(self, x, y):
        self.write_command(0x80 | (0x40 * y + x))
        time.sleep(0.005)

    def set_cursor_direction(self, leftToRight, autoScroll):
        if leftToRight:
            cmd = 0b00000110
        else:
            cmd = 0b00000100
        if autoScroll:
            cmd = cmd | 1

        self.write_command(cmd)

    def move_cursor(self, right, autoScroll):
        if right:
            cmd = 0b00010100
        else:
            cmd = 0b00010000
        if autoScroll:
            cmd = cmd | 0b00001000

        self.write_command(cmd)
