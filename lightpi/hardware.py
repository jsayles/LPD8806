import logging

fake_gpio = False
try:
    import RPi.GPIO as GPIO
except ModuleNotFoundError:
    logging.info("Raspberry Pi GPIO Unavailable")
    fake_gpio = True

# import seeed_dht
#from lightpi.buzzer import Buzzer
from lightpi.LPD8806 import LPD8806
from lightpi.ledstring import PWMString


BUZZ_PIN = 18

STRIP_DATA = 10
STRIP_CLCK = 11
STRIP_COUNT = 32

STRING1_PIN = 7
STRING2_PIN = 8
STRING3_PIN = 9
STRING4_PIN = 23
STRING5_PIN = 24
STRING6_PIN = 25


# Setup the GPIO Pins
if fake_gpio:
    logging.info("Fake GPIO: Hardware Initialized")
else:
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(STRIP_CLCK, GPIO.OUT)
    GPIO.setup(STRIP_DATA, GPIO.OUT)
    GPIO.setup(STRING1_PIN, GPIO.OUT, initial=GPIO.HIGH)
    GPIO.setup(STRING2_PIN, GPIO.OUT, initial=GPIO.HIGH)
    GPIO.setup(BUZZ_PIN, GPIO.OUT, initial=GPIO.LOW)

# Instantiate our hardware
strip = LPD8806(STRIP_COUNT, STRIP_DATA, STRIP_CLCK)
string1 = PWMString(STRING1_PIN)
string2 = PWMString(STRING2_PIN)
# temp_sensor = seeed_dht.DHT("22", TEMP_PIN)
#buzzer = Buzzer(BUZZ_PIN)
