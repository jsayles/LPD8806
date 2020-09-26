import time

from lightpi.hardware import strip, chain1, chain2


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

################################################################################
# Helper Methods
################################################################################

def allOn():
    strip.white()
    chain1.on()
    chain2.on()

def allOff():
    strip.off()
    chain1.off()
    chain2.off()
