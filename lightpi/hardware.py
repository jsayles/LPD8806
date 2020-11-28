import logging

fake_gpio = False
try:
    import RPi.GPIO as GPIO
except ModuleNotFoundError:
    logging.info("Raspberry Pi GPIO Unavailable")
    fake_gpio = True

from lightpi.buzzer import Buzzer
from lightpi.LPD8806 import LPD8806
from lightpi.ledstring import LEDStringArray


BUZZ_PIN = 18

STRIP_DATA = 7      # Blue wire
STRIP_CLCK = 8      # Orange Wire
STRIP_COUNT = 32

STRING_PINS = [23, 24, 25, 16, 20, 21]

# Setup the GPIO Pins
if fake_gpio:
    logging.info("Fake GPIO: Hardware Initialized")
else:
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(BUZZ_PIN, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(STRIP_CLCK, GPIO.OUT)
    GPIO.setup(STRIP_DATA, GPIO.OUT)
    for pin in STRING_PINS:
        GPIO.setup(pin, GPIO.OUT, initial=GPIO.HIGH)

# Instantiate our hardware
buzzer = Buzzer(BUZZ_PIN)
strip = LPD8806(STRIP_COUNT, STRIP_DATA, STRIP_CLCK)
strings = LEDStringArray(STRING_PINS)
