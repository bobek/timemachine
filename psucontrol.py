import RPi.GPIO as GPIO
import time


class PSU:
    """Simple wrapper for controlling ATX PSU via GPIO PIN"""

    def __init__(self, psu_pin):
        self.psu_pin = psu_pin
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.psu_pin, GPIO.OUT)

    def __del__(self):
        self.turn_off()
        GPIO.cleanup(self.psu_pin)

    def turn_on(self):
        GPIO.output(self.psu_pin, GPIO.HIGH)

    def turn_off(self):
        GPIO.output(self.psu_pin, GPIO.LOW)

class PushButton:
    """Simple wrapper from getting push button state"""

    def __init__(self, button_pin):
        self.button_pin = button_pin
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    def __del__(self):
        GPIO.cleanup(self.button_pin)

    def is_pushed(self):
        return not GPIO.input(self.button_pin)

    def wait_for_push(self, sleep=0.5):
        while True:
            if self.is_pushed(): break
            time.sleep(sleep)
