# Light Pi
LED Lights controlled by a Raspberry Pi.

Blog Post:  https://jacobsayles.com/2020/09/28/aha2/

## Hardware
- Raspberry Pi (Original Model A in this case)
- 1 Meter, 32 LED Strip LPD8806:  https://www.adafruit.com/product/306
- 2 LED string lights:  https://www.amazon.com/Sanniu-Operated-Christmas-Centerpiece-Decoration/dp/B072NH2FQ1
- Seperate USB power adapters for Pi and LEDs

# LED String Light Circuit
Wire up the led string lights using an NPN transistor to connect the GPIO and the 5v rail.
https://elinux.org/RPi_GPIO_Interface_Circuits

![circuit diagram](https://raw.githubusercontent.com/jsayles/LightPi/master/docs/npn_switch.png?raw=true)

## Grove Sensors
The temperature/humidity sensor uses a Seeed Studio Grove module and thus the Grove base platform
needs to be installed.  For detailed information:  [Grove Wiki](https://wiki.seeedstudio.com/Grove_Base_Hat_for_Raspberry_Pi/#installation)

```
curl -sL https://github.com/Seeed-Studio/grove.py/raw/master/install.sh | sudo bash -s -
```

## Setup Python
The step to setup Grove Sensors installs python3 and python3-pip but just to be thorough
I'm including those steps here too.  

```
sudo apt install python3 python3-pip
pip3 install -r requirements.txt --user
```

## Start Webapp
There is a startup script ([start_webapp.sh](start_webapp.sh)) that simply starts a tmux
session (webapp) and fires up flask.  To see the output, you need to attach to the tmux sesson.

```
tmux attach -t webapp
```

## Crontab
A simple way to make sure the webapp is running upon reboot is to install a crontab.

```
crontab -e
@reboot cd LightPi; ./start_webapp.sh
```
