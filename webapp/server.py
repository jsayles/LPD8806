import logging
import logging.config
import traceback

from flask import Flask, render_template, request, session, url_for, g
from flask.logging import default_handler

from lightpi.hardware import strip, string1, string2


################################################################################
# Application Definition
################################################################################


app = Flask(__name__)
app.config.from_object('webapp.settings')

logging_config = app.config['LOGGING']
# if logging_config:
#     app.logger.removeHandler(default_handler)
#     logging.config.dictConfig(logging_config)


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
    strip.orange()
    string1.on()
    string2.on()
    return "ON"


@app.route("/api/off")
def light_off():
    strip.off()
    string1.fadeOut()
    string2.fadeOut()
    return 'OFF'


@app.route("/api/dim")
def light_dim():
    strip.off()
    string1.off()
    b = g.pop('brightness', app.config['DEFAULT_BRIGHTNESS'])
    string2.fadeIn(b)
    return 'DIM'


@app.route("/api/red")
def light_red():
    string1.off()
    string2.off()
    b = g.pop('brightness', app.config['DEFAULT_BRIGHTNESS'])
    strip.fadeInRed(max=b, step=2, delay=0.05)
    return 'RED'


@app.route('/api/brightness/<int:level>')
def brightness(level):
    if level < 0 or level > 100:
        return "Invalid Brightness"
    g.brightness = level
    return "New Brightess: %d" % level
