import RPi.GPIO as GPIO


class LEDString:

    def __init__(self, bcm_pin):
        self.pin = bcm_pin

        # Setup the GPIO pins
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin, GPIO.OUT, initial=GPIO.LOW)

    def on(self):
        GPIO.output(self.pin, GPIO.HIGH)

    def off(self):
        GPIO.output(self.pin, GPIO.LOW)
