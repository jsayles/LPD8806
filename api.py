from flask import Flask

from lightpi.hardware import strip, string1, string2


app = Flask(__name__)


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
    string1.off()
    string2.off()
    return 'OFF'


@app.route("/api/dim")
def light_dim():
    strip.off()
    string1.on()
    string2.off()
    return 'DIM'


@app.route("/api/red")
def light_red():
    string1.off()
    string2.off()
    strip.fadeInRed(max=50, step=2, delay=0.05)
    return 'RED'


if __name__ == "__main__":
    app.run(host='lightpi.local')
