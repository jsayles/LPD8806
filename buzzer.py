################################################################################
# Based on code from:
# From http://www.linuxcircle.com/2015/04/12/how-to-play-piezo-buzzer-tunes-on-raspberry-pi-gpio-with-pwm/
################################################################################

import time
import RPi.GPIO as GPIO
from rtttl import parse_rtttl

DIXIE = "Dixie:d=4,o=5,b=225:8g#,8f,c#,c#,8c#,8d#,8f,8f#,g#,g#,g#,f"


class Buzzer(object):

    def __init__(self, bcm_pin):
        self.buzzer_pin = pin

        # Setup the GPIO pins
        GPIO.setmode(self.buzzer_pin)
        GPIO.setup(self.buzzer_pin, GPIO.IN)
        GPIO.setup(self.buzzer_pin, GPIO.OUT)

    def __del__(self):
        class_name = self.__class__.__name__

    def buzz(self, pitch, duration):
        if(pitch == 0):
            time.sleep(duration)
            return

        # In physics, the period (sec/cyc) is the inverse of the frequency (cyc/sec)
        period = 1.0 / pitch

        # Calcuate the time for half of the wave
        delay = period / 2

        # Number of waves to produce is the duration times the frequency
        cycles = int(duration * pitch)

        for i in range(cycles):
            GPIO.output(self.buzzer_pin, True)
            time.sleep(delay)
            GPIO.output(self.buzzer_pin, False)
            time.sleep(delay)

    def play_rtttl(self, rtttl_tune):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.buzzer_pin, GPIO.OUT)
        tune = parse_rtttl(rtttl_tune)
        print("Playing: %s" % tune['title'])
        for note in tune['notes']:
            p = note['frequency']
            d = 1.0 * note['duration'] / 1000
            self.buzz(p, d)
