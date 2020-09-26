# LPD8806
LPD8806 LED Strip driver for Raspberry Pi

## Hardware
- 1 Meter
- 32 LED
- LPD8803
- https://www.adafruit.com/product/306?length=1

## Driver Origin
http://russnelson.com/LPD8806.py

# LED Chain Circuit
Wire the led chains up using an NPN transistor to connect the GPIO and the 5v rail.
https://elinux.org/RPi_GPIO_Interface_Circuits

## Setup
```
sudo apt install python3-pip
pip install -r requirements.txt --user
```
