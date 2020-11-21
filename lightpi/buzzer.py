################################################################################
# Based on code from:
# From http://www.linuxcircle.com/2015/04/12/how-to-play-piezo-buzzer-tunes-on-raspberry-pi-gpio-with-pwm/
################################################################################

import time
import logging
import RPi.GPIO as GPIO
from rtttl import parse_rtttl

DIXIE = "Dixie:d=4,o=5,b=225:8g#,8f,c#,c#,8c#,8d#,8f,8f#,g#,g#,g#,f"


class Buzzer(object):

    def __init__(self, bcm_pin):
        self.buzzer_pin = bcm_pin

        # Setup the GPIO pins
        GPIO.setmode(GPIO.BCM)
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

    def play(self, tune):
        x=0
        
        if(tune==1):
            pitches=[262,294,330,349,392,440,494,523,587,659,698,784,880,988,1047]
            duration=0.1
            for p in pitches:
                self.buzz(p, duration)
                time.sleep(duration * 0.5)
            for p in reversed(pitches):
                self.buzz(p, duration)
                time.sleep(duration * 0.5)

        elif(tune==2):
            pitches=[262,330,392,523,1047]
            duration=[0.2,0.2,0.2,0.2,0.2,0,5]
            for p in pitches:
                self.buzz(p, duration[x])
                time.sleep(duration[x] * 0.5)
                x += 1

        elif(tune==3):
            pitches=[392,294,0,392,294,0,392,0,392,392,392,0,1047,262]
            duration=[0.2,0.2,0.2,0.2,0.2,0.2,0.1,0.1,0.1,0.1,0.1,0.1,0.8,0.4]
            for p in pitches:
                self.buzz(p, duration[x])
                time.sleep(duration[x] * 0.5)
                x += 1

        elif(tune==4):
            pitches=[1047, 988,659]
            duration=[0.1,0.1,0.2]
            for p in pitches:
                self.buzz(p, duration[x])
                time.sleep(duration[x] *0.5)
                x += 1

        elif(tune==5):
            pitches=[1047, 988,523]
            duration=[0.1,0.1,0.2]
            for p in pitches:
                self.buzz(p, duration[x])
                time.sleep(duration[x] * 0.5)
                x += 1

    def play_rtttl(self, rtttl_tune):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.buzzer_pin, GPIO.OUT)
        tune = parse_rtttl(rtttl_tune)
        logging.info("Playing: %s" % tune['title'])
        for note in tune['notes']:
            p = note['frequency']
            d = 1.0 * note['duration'] / 1000
            self.buzz(p, d)
