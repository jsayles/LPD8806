from flask import Flask, g

from lightpi.hardware import strip, string1, string2


app = Flask(__name__)

DEFAULT_BRIGHTNESS = 50

@app.route("/")
def home():
    return 'Hello, World!'


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
    b = g.pop('brightness', DEFAULT_BRIGHTNESS)
    string2.fadeIn(b)
    return 'DIM'


@app.route("/api/red")
def light_red():
    string1.off()
    string2.off()
    b = g.pop('brightness', DEFAULT_BRIGHTNESS)
    strip.fadeInRed(max=b, step=2, delay=0.05)
    return 'RED'


@app.route('/api/brightness/<int:level>')
def brightness(level):
    if level < 0 or level > 100:
        return "Invalid Brightness"
    g.brightness = level
    return "New Brightess: %d" % level


if __name__ == "__main__":
    app.run(host='lightpi.local')
