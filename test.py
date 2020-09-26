import time

import RPi.GPIO as GPIO
from LPD8806 import LPD8806


LED1_PIN = 7
LED2_PIN = 8
BUZZ_PIN = 9
STRIP_DATA = 10
STRIP_CLCK = 11


# Test the RGB Strip
strip = LPD8806(32, STRIP_DATA, STRIP_CLCK)
strip.red()
time.sleep(0.3)
strip.green()
time.sleep(0.3)
strip.blue()
time.sleep(0.3)
strip.off()


# Test the LED Chains
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED1_PIN, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(LED2_PIN, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(BUZZ_PIN, GPIO.OUT, initial=GPIO.LOW)

GPIO.cleanup()
GPIO.output(LED1_PIN, GPIO.HIGH)
GPIO.output(LED2_PIN, GPIO.HIGH)
time.sleep(0.3)
GPIO.output(LED1_PIN, GPIO.LOW)
GPIO.output(LED2_PIN, GPIO.LOW)
