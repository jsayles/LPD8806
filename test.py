from time
from LPD8806 import LPD8806

strip = LPD8806(32, 10, 11)

strip.fillStrip(255, 0, 0)
time.sleep(0.3)
strip.fillStrip(0, 255, 0)
time.sleep(0.3)
strip.fillStrip(0, 0, 255)
time.sleep(0.3)
strip.off()
