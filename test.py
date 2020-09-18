from time import sleep

from LPD8806 import LPD8806

strip = LPD8806(32, 10, 11)

strip.fill(255, 0, 0, pulse=0.3)
strip.fill(0, 255, 0, pulse=0.3)
strip.fill(0, 0, 255, pulse=0.3)
strip.off()
