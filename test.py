import time

from lightpi.hardware import strip, string1, string2


DELAY_SEC = 0.3

# Test the RGB Strip
strip.red()
time.sleep(DELAY_SEC)
strip.green()
time.sleep(DELAY_SEC)
strip.blue()
time.sleep(DELAY_SEC)
strip.off()

# Test the LED Strings
string1.on()
time.sleep(DELAY_SEC)
string1.off()
time.sleep(DELAY_SEC)
string2.on()
time.sleep(DELAY_SEC)
string2.off()

################################################################################
# Helper Methods
################################################################################

def allOn():
    strip.white()
    string1.on()
    string2.on()

def allOff():
    strip.off()
    string1.off()
    string2.off()
