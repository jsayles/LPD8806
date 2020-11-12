import RPi.GPIO as GPIO

# import seeed_dht

from lightpi.LPD8806 import LPD8806
from lightpi.ledstring import PWMString
#from lightpi.buzzer import Buzzer


STRING1_PIN = 7
STRING2_PIN = 8
BUZZ_PIN = 9
STRIP_DATA = 10
STRIP_CLCK = 11
STRIP_COUNT = 32
TEMP_PIN = 14

# Setup the GPIO Pins
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(STRIP_CLCK, GPIO.OUT)
GPIO.setup(STRIP_DATA, GPIO.OUT)
GPIO.setup(STRING1_PIN, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(STRING2_PIN, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(BUZZ_PIN, GPIO.OUT, initial=GPIO.LOW)

# Instantiate our hardware
strip = LPD8806(STRIP_COUNT, STRIP_DATA, STRIP_CLCK)
string1 = PWMString(STRING1_PIN)
string2 = PWMString(STRING2_PIN)
# temp_sensor - seeed_dht.DHT("11", TEMP_PIN)
#buzzer = Buzzer(BUZZ_PIN)
