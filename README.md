# LPD8806
LPD8806 LED Strip driver for Raspberry Pi.
https://jacobsayles.com/2020/09/28/aha2/

## Hardware
- 1 Meter, 32 LED Strip LPD8803:  https://www.adafruit.com/product/306
- 2 LED string lights:  https://www.amazon.com/Sanniu-Operated-Christmas-Centerpiece-Decoration/dp/B072NH2FQ1
- Raspberry Pi
- Seperate USB power adapters for Pi and LEDs

# LED String Light Circuit
Wire up the led string lights using an NPN transistor to connect the GPIO and the 5v rail.
https://elinux.org/RPi_GPIO_Interface_Circuits

![circuit diagram](https://raw.githubusercontent.com/jsayles/LightPi/master/docs/npn_switch.png?raw=true)

## Setup and API Service
```
sudo apt install python3-pip
pip3 install -r requirements.txt --user
python3 api
```
