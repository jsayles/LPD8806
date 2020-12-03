import logging
import logging.config
import traceback

from flask import Flask
from flask import render_template, request, url_for, g
from flask import jsonify, make_response
from flask.logging import default_handler
from flask_caching import Cache

from lightpi.hardware import strip, strings


TEMPERATURE = "temperature"
BRIGHTNESS = "brightness"


################################################################################
# Application Definition
################################################################################


app = Flask(__name__)
app.config.from_object('webapp.settings')

cache = Cache(app, config={'CACHE_TYPE': 'simple'})

logging_config = app.config['LOGGING']
if logging_config:
    app.logger.removeHandler(default_handler)
    logging.config.dictConfig(logging_config)


################################################################################
# Webapp Routes
################################################################################


@app.route("/")
def home():
    cam_url = app.config['WEBCAM_URL']
    temp_c = get_temperature()
    temp_f = 9.0/5.0 * temp_c + 32
    return render_template('home.html', cam_url=cam_url, temp_c=temp_c, temp_f=temp_f)


################################################################################
# Helper Functions
################################################################################


def get_temperature():
    temp = cache.get(TEMPERATURE)
    if not temp:
        temp = 0
    return temp


def get_brightness():
    brightness = cache.get(BRIGHTNESS)
    if not brightness:
        brightness = app.config['DEFAULT_BRIGHTNESS']
    return brightness


################################################################################
# API Routes
################################################################################


@app.route("/api/on")
def light_on():
    strip.off()
    strings.on()
    return "ON"


@app.route("/api/off")
def light_off():
    strip.off()
    strings.off()
    return 'OFF'


@app.route("/api/dim/<int:level>")
def light_dim(level):
    if level <= 0 or level >= 6:
        return "Invalid Brightness"

    strip.off()
    strings.off()
    strings.on(level)
    # brightness = get_brightness()
    # string1.fadeIn(b)
    return f'DIM {level}'

@app.route("/api/red")
def light_red():
    strings.off()
    brightness = get_brightness()
    strip.fadeInRed(max=brightness, step=2, delay=0.05)
    return 'RED'

@app.route("/api/green")
def light_green():
    strings.off()
    brightness = get_brightness()
    strip.fadeInGreen(max=brightness, step=2, delay=0.05)
    return 'GREEN'

@app.route("/api/blue")
def light_blue():
    strings.off()
    brightness = get_brightness()
    strip.fadeInBlue(max=brightness, step=2, delay=0.05)
    return 'BLUE'

@app.route("/api/temperature/", methods=['GET'])
def temperature():
    temp_c = get_temperature()
    return make_response(jsonify({"temperature": temp_c}), 200)

@app.route("/api/temperature/<float:temp>", methods=['POST'])
def update_temperature(temp):
    cache.set(TEMPERATURE, temp)
    return make_response(jsonify({"message": "Success!"}), 200)

@app.route("/api/update", methods=['POST'])
def update():
    # Example JSON
    # {"red": 100, "green": 100, "blue": 100, "string1": 100, "string2": 100 }
    json_req = request.get_json()

    red = json_req.get("red", 0)
    green = json_req.get("green", 0)
    blue = json_req.get("blue", 0)
    s1 = json_req.get("string1", 0)
    s2 = json_req.get("string2", 0)
    s3 = json_req.get("string3", 0)
    s4 = json_req.get("string4", 0)
    s5 = json_req.get("string5", 0)
    s6 = json_req.get("string6", 0)

    strip.fillStrip(red, green, blue)
    string1.setBrightness(s1)
    string2.setBrightness(s2)
    string3.setBrightness(s3)
    string4.setBrightness(s4)
    string5.setBrightness(s5)
    string6.setBrightness(s6)

    return make_response(jsonify({"message": "Success!"}), 200)


@app.route('/api/brightness/<int:level>')
def brightness(level):
    if level < 0 or level > 100:
        return "Invalid Brightness"
    cache.set(BRIGHTNESS, level)
    return "New Brightess: %d" % level
