import logging
import logging.config
import traceback

from flask import Flask
from flask import render_template, request, url_for, g
from flask import jsonify, make_response
from flask.logging import default_handler

from lightpi.hardware import strip, strings


################################################################################
# Application Definition
################################################################################


app = Flask(__name__)
app.config.from_object('webapp.settings')

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
    return render_template('home.html', cam_url=cam_url)


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


@app.route("/api/dim")
def light_dim():
    strip.off()
    strings.off()
    strings.on(1)
    # b = g.pop('brightness', app.config['DEFAULT_BRIGHTNESS'])
    # string2.fadeIn(b)
    return 'DIM'

@app.route("/api/red")
def light_red():
    strings.off()
    b = g.pop('brightness', app.config['DEFAULT_BRIGHTNESS'])
    strip.fadeInRed(max=b, step=2, delay=0.05)
    return 'RED'

@app.route("/api/temperature/", methods=['GET'])
def get_temperature():
    temp = g.temperature
    return make_response(jsonify({"temperature": temp}), 200)

@app.route("/api/temperature/<float:temp>", methods=['POST'])
def update_temperature(temp):
    g.temperature = temp
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
    g.brightness = level
    return "New Brightess: %d" % level
