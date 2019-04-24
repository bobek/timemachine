import RPi.GPIO as GPIO


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
