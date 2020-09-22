################################################################################
# Based on code from:
# http://russnelson.com/LPD8806.py
################################################################################


import RPi.GPIO as GPIO
import time


class LPD8806:

    RED_I = 0
    GRN_I = 1
    BLU_I = 2

    def __init__(self, count, dataPin, clkPin):
        self.data_pin = dataPin
        self.clock_pin = clkPin
        self.pixel_count = count
        self.pixels = [0] * count * 3
        self.colour = [0, 0, 0]

        # Setup the GPIO pins
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(self.clock_pin, GPIO.OUT)
        GPIO.setup(self.data_pin, GPIO.OUT)

    ############################################################################
    # Core Methods
    ############################################################################

    def getColour(self, r, g, b):
        # Take the lowest 7 bits of each value and append them end to end
        # We have the top bit set high
        # (its a 'parity-like' bit in the protocol and must be set!)
        x = g | 0x80
        x <<= 8
        x |= r | 0x80
        x <<= 8
        x |= b | 0x80
        return x

    def _setPixelColour(self, n, c):
        if n >= self.pixel_count:
            raise Exception("Pixel number is greater than the total pixel count")

        self.pixels[n*3] = (c >> 16) | 0x80
        self.pixels[n*3+1] = (c >> 8) | 0x80
        self.pixels[n*3+2] = (c) | 0x80

    def _write8(self, d):
        # Basic, push SPI data out
        for i in range(8):
            #GPIO.output(self.d, (d & (0x80 >> i)) <> 0)
            GPIO.output(self.data_pin, (d & (0x80 >> i)) != 0)
            GPIO.output(self.clock_pin, True)
            GPIO.output(self.clock_pin, False)

    # This is how data is pushed to the strip.
    # Unfortunately, the company that makes the chip didnt release the
    # protocol document or you need to sign an NDA or something stupid
    # like that, but we reverse engineered this from a strip
    # controller and it seems to work very nicely!
    def show(self):
        # Get the strip's attention
        self._write8(0)
        self._write8(0)
        self._write8(0)
        self._write8(0)

        # Write 24 bits per pixel
        for i in range(self.pixel_count):
            self._write8(self.pixels[i*3])
            self._write8(self.pixels[i*3+1])
            self._write8(self.pixels[i*3+2])

        # To 'latch' the data, we send just zeros
        for i in range(self.pixel_count * 2):
            self._write8(0)
            self._write8(0)
            self._write8(0)

        # We need to have a delay here, 10ms seems to do the job
        # shorter may be OK as well - need to experiment :(
        time.sleep(0.005)

    ############################################################################
    # Generic Helper Methods
    ############################################################################

    def setPixel(self, n, r, g, b):
        c = self.getColour(r, g, b)
        self._setPixelColour(n, c)

    def fillStrip(self, r, g, b, autoUpdate=True):
        for i in range(self.pixel_count):
            self.setPixel(i, r, g, b)
        if autoUpdate:
            self.show()

    def off(self):
        self.fillStrip(0, 0, 0)

    ############################################################################
    # Colour Specific Helper Methods
    ############################################################################

    def red(self):
        self.fillStrip(100, 0, 0)

    def green(self):
        self.fillStrip(0, 100, 0)

    def blue(self):
        self.fillStrip(0, 0, 100)

    def fadeInRed(self, delay=0.1):
        for i in range(0, 100, 1):
            self.fillStrip(i, 0, 0)
            time.sleep(delay)

    def fadeInGreen(self, delay=0.1):
        for i in range(0, 100, 1):
            self.fillStrip(0, i, 0)
            time.sleep(delay)

    def fadeInBlue(self, delay=0.1):
        for i in range(0, 100, 1):
            self.fillStrip(0, 0, i)
            time.sleep(delay)
