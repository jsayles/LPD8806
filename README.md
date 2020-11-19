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
![2N3904 pinout](https://raw.githubusercontent.com/jsayles/LightPi/master/docs/pinout-of-2N3904-npn-transistor_3.png?raw=true)

docs/pinout-of-2N3904-npn-transistor_3.png

## Grove Sensors
The temperature/humidity sensor uses a Seeed Studio Grove [DHT22](https://wiki.seeedstudio.com/Grove-Temperature_and_Humidity_Sensor_Pro/)
module and thus the Grove base platform
needs to be installed.  For detailed information:  [Grove Wiki](https://wiki.seeedstudio.com/Grove_Base_Hat_for_Raspberry_Pi/#installation)

```
curl -sL https://github.com/Seeed-Studio/grove.py/raw/master/install.sh | sudo bash -s -

 - or -

git clone https://github.com/Seeed-Studio/grove.py
cd grove.py
sudo pip3 install .
```

## Setup Python Environment
The step to setup Grove Sensors installs python3 and python3-pip but just to be thorough
I'm including those steps here too.  

```
sudo apt install python3 python3-pip
pip3 install pipenv --user
pipenv install --three
```

## Start Webapp
There is a startup script ([start_webapp.sh](start_webapp.sh)) that simply starts a tmux
session (webapp) and fires up pipenv and flask.  To see the output, you need to attach
to the tmux sesson. To cancel, attach and hit Ctrl-C.

```
tmux attach -t webapp
```

To start the webapp but not run it through tmux, run the following:

```
pipenv run start_webapp
```



## Crontab
A simple way to make sure the webapp is running upon reboot is to install a crontab.

```
crontab -e
@reboot cd LightPi; ./start_webapp.sh
```
