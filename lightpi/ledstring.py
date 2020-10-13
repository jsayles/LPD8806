import time
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


class PWMString:

    def __init__(self, bcm_pin, frequency=200):
        self.pin = bcm_pin
        self.frequency = frequency

        # Setup the GPIO pins
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin, GPIO.OUT)
        self.pwm = GPIO.PWM(self.pin, self.frequency)
        self.pwm.start(0)

    def __del__(self):
        self.pwm.stop()

    def setBrightness(self, level):
        self.pwm.ChangeDutyCycle(level)

    def on(self):
        self.setBrightness(100)

    def off(self):
        self.setBrightness(0)

    def fadeIn(self, delay=0.05):
        # Loop 0 to 100 stepping by 5 each loop
        for l in range(0, 100, 5):
            self.setBrightness(l)
            time.sleep(delay)
        self.on()

    def fadeOut(self, delay=0.05):
        # Loop 95 to 5 stepping down by 5 each loop
        for l in range(100, 0, -5):
            self.setBrightness(l)
            time.sleep(delay)
        self.off()
