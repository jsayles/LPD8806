import time

from hardware import *

DELAY_SEC = 0.3

# Test the RGB Strip
strip.red()
time.sleep(DELAY_SEC)
strip.green()
time.sleep(DELAY_SEC)
strip.blue()
time.sleep(DELAY_SEC)
strip.off()

# Test the LED Chains
chain1.on()
time.sleep(DELAY_SEC)
chain1.off()
time.sleep(DELAY_SEC)
chain2.on()
time.sleep(DELAY_SEC)
chain2.off()

# Test the Buzzer
#buzzer.buzz(100, DELAY_SEC)
