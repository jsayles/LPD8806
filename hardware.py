import RPi.GPIO as GPIO

from LPD8806 import LPD8806
from ledchain import LEDChain
from buzzer import Buzzer


LED1_PIN = 7
LED2_PIN = 8
BUZZ_PIN = 9
STRIP_DATA = 10
STRIP_CLCK = 11
STRIP_COUNT = 32

# Setup the GPIO Pins
GPIO.cleanup()
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(self.STRIP_CLCK, GPIO.OUT)
GPIO.setup(self.STRIP_DATA, GPIO.OUT)
GPIO.setup(LED1_PIN, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(LED2_PIN, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(BUZZ_PIN, GPIO.OUT, initial=GPIO.LOW)

# Instantiate our hardware
strip = LPD8806(STRIP_COUNT, STRIP_DATA, STRIP_CLCK)
chain1 = LEDChain(LED1_PIN)
chain2 = LEDChain(LED2_PIN)
buzzer = Buzzer(BUZZ_PIN)
